#!/usr/bin/env python3
"""Check an EPUB made by tools/make_epub.py (standard library only).

    python3 tools/check_epub.py publish/books/der-mann-den-die-flut-brachte.epub
    python3 tools/check_epub.py book.epub --source work/german/novel_de.md

Checks: zip and mimetype, container.xml, every XML/XHTML file parses, manifest and
spine consistency, navigation links, images, language, and that every paragraph of
every chapter equals the paragraph of the source markdown (the source defaults
to the language of the book). Also runs EPUBCheck when it is installed; if it
is not, it says so. Exit code 1 on any error.
"""
import argparse
import glob
import os
import posixpath
import re
import shutil
import subprocess
import sys
import zipfile
from html import unescape
from urllib.parse import unquote
from xml.etree import ElementTree as ET

SRC = {"en": ("source/novel.md", r"# (Part [^:]+): (.+)", r"## (Chapter \d+)\. (.+)", "*The End*", "The End"),
       "de": ("work/german/novel_de.md", r"# (Teil [^:]+): (.+)", r"## (Kapitel \d+)\. (.+)", "*Ende*", "Ende")}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []


def err(msg):
    errors.append(msg)
    print("ERROR:", msg)


def source_chapters(path, chap_re, end_mark):
    """{number: {label, title, items}} with items ('p', text) / ('sb',)."""
    chaps, chap, para = {}, None, []

    def flush():
        nonlocal para
        if para and chap is not None:
            chap["items"].append(("p", " ".join(para)))
        para = []

    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if re.match(r"# ", line):
            flush(); chap = None; continue
        m = re.match(chap_re, line)
        if m:
            flush()
            chap = {"label": m.group(1), "title": m.group(2), "items": []}
            chaps[int(m.group(1).split()[1])] = chap
            continue
        if chap is None:
            continue
        if line.strip() == "---":
            flush(); chap["items"].append(("sb",)); continue
        if not line.strip():
            flush(); continue
        para.append(line.strip())
    flush()
    return chaps


def find_epubcheck():
    exe = shutil.which("epubcheck")
    if exe:
        return [exe]
    jars = []
    for pat in (os.environ.get("EPUBCHECK_JAR", ""), "~/epubcheck*/epubcheck.jar", "~/Downloads/epubcheck*/epubcheck.jar",
                os.path.join(ROOT, "tools/epubcheck*/epubcheck.jar"), "/opt/homebrew/share/epubcheck/epubcheck.jar",
                "/usr/local/share/epubcheck/epubcheck.jar"):
        if pat:
            jars += glob.glob(os.path.expanduser(pat))
    if jars and shutil.which("java"):
        return ["java", "-jar", jars[0]]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("epub")
    ap.add_argument("--source", default=None)
    ap.add_argument("--allow-gaps", action="store_true", help="test builds with missing chapters (not a sample)")
    a = ap.parse_args()

    try:
        z = zipfile.ZipFile(a.epub)
    except Exception as e:
        print("ERROR: not a valid zip:", e); sys.exit(1)
    bad = z.testzip()
    if bad:
        err(f"corrupt zip member {bad}")
    infos = z.infolist()
    names = [i.filename for i in infos]
    if not infos or infos[0].filename != "mimetype":
        err("mimetype is not the first entry")
    else:
        if infos[0].compress_type != zipfile.ZIP_STORED:
            err("mimetype is compressed")
        if z.read("mimetype") != b"application/epub+zip":
            err("mimetype content wrong")

    # XML well-formedness
    docs = {}
    for n in names:
        if n.endswith((".xml", ".xhtml", ".opf", ".ncx", ".svg")):
            try:
                docs[n] = ET.fromstring(z.read(n))
            except ET.ParseError as e:
                err(f"{n} does not parse: {e}")
    if "META-INF/container.xml" not in docs:
        err("META-INF/container.xml missing or broken"); sys.exit(1)
    rf = docs["META-INF/container.xml"].find(".//{*}rootfile")
    opf_path = rf.get("full-path")
    if opf_path not in docs:
        err(f"package file {opf_path} missing or broken"); sys.exit(1)
    opf = docs[opf_path]
    base = posixpath.dirname(opf_path)

    def res(href):
        return posixpath.normpath(posixpath.join(base, unquote(href.split("#")[0])))

    items = {}
    for it in opf.findall(".//{*}manifest/{*}item"):
        items[it.get("id")] = it
        if res(it.get("href")) not in names:
            err(f"manifest item {it.get('href')} not in the zip")
    manifest_paths = {res(i.get("href")) for i in items.values()}
    for n in names:
        if n not in manifest_paths and not n.startswith("META-INF/") and n != "mimetype" and n != opf_path:
            err(f"{n} in the zip but not in the manifest")
    spine = []
    for r in opf.findall(".//{*}spine/{*}itemref"):
        i = r.get("idref")
        if i not in items:
            err(f"spine item {i} not in the manifest")
        else:
            spine.append(res(items[i].get("href")))
    navs = [res(i.get("href")) for i in items.values() if "nav" in (i.get("properties") or "").split()]
    if len(navs) != 1:
        err(f"expected exactly one nav document, found {len(navs)}")
    for k in ("{http://purl.org/dc/elements/1.1/}identifier", "{http://purl.org/dc/elements/1.1/}title",
              "{http://purl.org/dc/elements/1.1/}language", "{http://purl.org/dc/elements/1.1/}creator"):
        if opf.find(".//" + k) is None or not (opf.find(".//" + k).text or "").strip():
            err(f"metadata {k.split('}')[1]} missing")
    lang = (opf.findtext(".//{http://purl.org/dc/elements/1.1/}language") or "").strip()
    if lang not in SRC:
        err(f"unexpected language '{lang}'"); lang = "en"
    if not any(i.get("properties") == "cover-image" for i in items.values()):
        err("no cover-image in the manifest")

    # links, images, language per document
    ids_in = {}
    for n, root in docs.items():
        ids_in[n] = {e.get("id") for e in root.iter() if e.get("id")}
    for n in names:
        if not n.endswith(".xhtml") or n not in docs:
            continue
        root = docs[n]
        xl = root.get("{http://www.w3.org/XML/1998/namespace}lang")
        if xl != lang or root.get("lang") != lang:
            err(f"{n}: html lang '{root.get('lang')}' / xml:lang '{xl}' differ from book language '{lang}'")
        d = posixpath.dirname(n)
        for e in root.iter():
            tag = e.tag.split("}")[1] if "}" in e.tag else e.tag
            if tag == "img" and e.get("src"):
                t = posixpath.normpath(posixpath.join(d, unquote(e.get("src"))))
                if t not in names:
                    err(f"{n}: image {e.get('src')} missing")
            if tag == "a" and e.get("href") and not e.get("href").startswith(("http:", "https:", "mailto:")):
                h = e.get("href")
                t = posixpath.normpath(posixpath.join(d, unquote(h.split("#")[0]))) if h.split("#")[0] else n
                if t not in names:
                    err(f"{n}: link {h} does not resolve")
                elif "#" in h and t in ids_in and h.split("#")[1] not in ids_in[t]:
                    err(f"{n}: link {h} fragment not found")
    if navs and navs[0] in docs:
        navroot = docs[navs[0]]
        tocnav = [x for x in navroot.iter("{http://www.w3.org/1999/xhtml}nav")
                  if x.get("{http://www.idpf.org/2007/ops}type") == "toc"]
        if not tocnav:
            err("nav has no toc")
        else:
            linked = {res(posixpath.join(posixpath.relpath(posixpath.dirname(navs[0]), base), x.get("href"))) if base else
                      posixpath.normpath(posixpath.join(posixpath.dirname(navs[0]), x.get("href")))
                      for x in tocnav[0].iter("{http://www.w3.org/1999/xhtml}a")}
            for s in spine:
                if posixpath.basename(s).startswith(("ch", "part")) and s not in linked:
                    err(f"{s} is in the spine but not in the table of contents")

    # paragraph comparison
    src_path, _, chap_re, end_mark, end_text = SRC[lang]
    src_path = a.source or os.path.join(ROOT, src_path)
    if not os.path.exists(src_path):
        err(f"source {src_path} not found")
        schaps = {}
    else:
        schaps = source_chapters(src_path, chap_re, end_mark)
    n_ch = n_p = n_w = 0
    for s in spine:
        m = re.match(r".*/ch(\d+)\.xhtml$", s)
        if not m:
            continue
        num = int(m.group(1))
        raw = z.read(s).decode("utf-8")
        sc = schaps.get(num)
        if not sc:
            err(f"{s}: chapter {num} not in the source"); continue
        label = re.search(r'<p class="chnum">(.*?)</p>', raw)
        title = re.search(r"<h2>(.*?)</h2>", raw)
        if not label or unescape(label.group(1)) != sc["label"]:
            err(f"{s}: chapter label differs from the source")
        if not title or unescape(title.group(1)) != sc["title"]:
            err(f"{s}: chapter title differs from the source")
        body = raw.split("</h2>", 1)[1]
        got = []
        for pm in re.finditer(r'<p(?: class="([^"]*)")?>(.*?)</p>', body, re.S):
            cls, inner = pm.group(1) or "", pm.group(2)
            if cls == "sb":
                got.append(("sb",))
            elif cls == "end":
                got.append(("p", end_mark))
                if unescape(inner) != end_text:
                    err(f"{s}: end card text '{inner}' != '{end_text}'")
            else:
                got.append(("p", unescape(inner.replace("<em>", "*").replace("</em>", "*"))))
        if len(got) != len(sc["items"]):
            err(f"{s}: {len(got)} items in the EPUB, {len(sc['items'])} in the source")
        for i, (g, w) in enumerate(zip(got, sc["items"]), 1):
            if g != w:
                err(f"{s}: item {i} differs: EPUB '{str(g)[:70]}' vs source '{str(w)[:70]}'")
        n_ch += 1
        ps = [x for x in got if x[0] == "p"]
        n_p += len(ps)
        n_w += sum(len(x[1].split()) for x in ps)
        if lang == "de" and ("&quot;" in raw or '"' in re.sub(r"<[^>]*>", "", raw)):
            err(f"{s}: straight double quote in text")
    # sample / full: chapters in the epub must be the first N source chapters, in order
    nums = [int(re.match(r".*/ch(\d+)\.xhtml$", s).group(1)) for s in spine if re.match(r".*/ch(\d+)\.xhtml$", s)]
    if nums != list(range(1, len(nums) + 1)) and not a.allow_gaps:
        err(f"chapter order/numbering in the spine is {nums}")
    kind = "full book" if schaps and nums == list(range(1, 19)) else "sample or partial"

    print(f"{a.epub}: language {lang}, {kind}; {n_ch} chapters, {n_p} paragraphs, {n_w} words (paragraphs compared one by one with {os.path.relpath(src_path, ROOT)})")
    ec = find_epubcheck()
    if ec:
        r = subprocess.run(ec + [a.epub], capture_output=True, text=True)
        print("EPUBCheck output (tail):\n" + (r.stdout + r.stderr)[-1500:])
        if r.returncode:
            err("EPUBCheck reported problems")
    else:
        print("EPUBCheck: NOT RUN (epubcheck is not installed; no jar found). The checks above are not a substitute.")
    print("RESULT:", f"FAIL ({len(errors)} errors)" if errors else "OK")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
