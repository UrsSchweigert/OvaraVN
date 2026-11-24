#!/usr/bin/env python3
"""Build the novel as an EPUB 3 for Apple Books (standard library only).

Reads source/novel.md (never changes it) and writes a reflowable EPUB.
  Full book:  python3 tools/make_epub.py --author "Name" --cover publish/books/cover.jpg --out publish/books/book.epub
  Sample:     add --sample 2     (first two chapters, with a closing page)
  German:     add --lang de      (source defaults to work/german/novel_de.md, made by tools/assemble_german.py)
The author name is a command-line argument so it never sits in a committed file.
"""
import argparse
import re
import uuid
import zipfile
from datetime import datetime, timezone
from html import escape

LANGS = {
    "en": dict(
        code="en", source="source/novel.md",
        title="The Man the Tide Brought In", subtitle="A novel of Ovara",
        uid_url="https://derschweigert.de/ovara/the-man-the-tide-brought-in",
        part_re=r"# (Part [^:]+): (.+)", chap_re=r"## (Chapter \d+)\. (.+)", end_mark="*The End*", end_text="The End",
        cover_alt="Cover of ", rights="All rights reserved.", cover_label="Cover", contents="Contents",
        guide="Guide", start="Start of the story", sample_end="End of sample",
        thanks=("Thank you for reading. The story continues in ", ", &#8220;", "&#8221;, in the full book."),
        extra_css="",
    ),
    "de": dict(
        code="de", source="work/german/novel_de.md",
        title="Der Mann, den die Flut brachte", subtitle="Ein Roman aus Ovara",
        uid_url="https://derschweigert.de/ovara/der-mann-den-die-flut-brachte",
        part_re=r"# (Teil [^:]+): (.+)", chap_re=r"## (Kapitel \d+)\. (.+)", end_mark="*Ende*", end_text="Ende",
        cover_alt="Umschlag von ", rights="Alle Rechte vorbehalten.", cover_label="Umschlag", contents="Inhalt",
        guide="Wegweiser", start="Beginn der Geschichte", sample_end="Ende der Leseprobe",
        thanks=("Danke fürs Lesen. Die Geschichte geht in ", ", &#8222;", "&#8220;, im vollständigen Buch weiter."),
        extra_css="p { hyphens: auto; -webkit-hyphens: auto; }\n",
    ),
}
L = LANGS["en"]  # set in main()
TITLE = L["title"]
SUBTITLE = L["subtitle"]
UID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, L["uid_url"]))

CSS = """\
body { margin: 0; padding: 0 0.2em; line-height: 1.45; }
h1, h2 { font-weight: normal; text-align: center; page-break-after: avoid; break-after: avoid; }
h1 { font-size: 2em; margin: 3em 0 0.4em; }
h2 { font-size: 1.5em; margin: 0.3em 0 1.6em; }
p { margin: 0; text-indent: 1.3em; text-align: left; orphans: 2; widows: 2; }
p.first, p.sb + p, p.noindent { text-indent: 0; }
p.sb { text-align: center; text-indent: 0; margin: 1.4em 0; letter-spacing: 0.4em; }
p.chnum { text-align: center; text-indent: 0; margin: 3em 0 0; text-transform: uppercase; letter-spacing: 0.2em; font-size: 0.8em; }
p.sub { text-align: center; text-indent: 0; font-style: italic; margin-bottom: 2em; }
p.center { text-align: center; text-indent: 0; }
p.end { text-align: center; text-indent: 0; margin-top: 2em; font-style: italic; }
div.cover { text-align: center; margin: 0; padding: 0; }
img.cover { max-width: 100%; max-height: 100%; }
"""


def inline(text):
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escape(text, quote=False))


def parse(path):
    """Return a list of parts: {label, name, chapters: [{label, title, items}]}.
    items are ('p', text) or ('sb',)."""
    parts, part, chap, para = [], None, None, []

    def flush():
        nonlocal para
        if para and chap is not None:
            chap["items"].append(("p", " ".join(para)))
        para = []

    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m = re.match(L["part_re"], line)
        if m:
            flush(); chap = None
            part = {"label": m.group(1), "name": m.group(2), "chapters": []}
            parts.append(part); continue
        m = re.match(L["chap_re"], line)
        if m:
            flush()
            chap = {"label": m.group(1), "title": m.group(2), "items": []}
            part["chapters"].append(chap); continue
        if chap is None:
            continue
        if line.strip() == "---":
            flush(); chap["items"].append(("sb",)); continue
        if not line.strip():
            flush(); continue
        para.append(line.strip())
    flush()
    return parts


def xhtml(title, body, cls=""):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{L['code']}" xml:lang="{L['code']}">
<head><meta charset="utf-8"/><title>{escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body{(' class="' + cls + '"') if cls else ''}>
{body}
</body>
</html>
"""


def chapter_body(chap):
    out = [f'<section epub:type="chapter"><p class="chnum">{escape(chap["label"])}</p>',
           f'<h2>{escape(chap["title"])}</h2>']
    first = True
    for it in chap["items"]:
        if it[0] == "sb":
            out.append('<p class="sb">*&#160;&#160;*&#160;&#160;*</p>'); continue
        text = it[1]
        if text == L["end_mark"]:
            out.append(f'<p class="end">{L["end_text"]}</p>'); continue
        attr = ' class="first"' if first else ""
        out.append(f"<p{attr}>{inline(text)}</p>")
        first = False
    out.append("</section>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--author", required=True)
    ap.add_argument("--cover", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--lang", choices=sorted(LANGS), default="en")
    ap.add_argument("--source", default=None)
    ap.add_argument("--sample", type=int, default=0, help="only the first N chapters, plus a closing page")
    ap.add_argument("--year", default="2026")
    a = ap.parse_args()
    global L, TITLE, SUBTITLE, UID
    L = LANGS[a.lang]
    TITLE, SUBTITLE = L["title"], L["subtitle"]
    UID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, L["uid_url"]))
    if a.source is None:
        a.source = L["source"]

    parts = parse(a.source)
    all_chaps = [c for p in parts for c in p["chapters"]]
    next_chap = None
    if a.sample:
        keep = all_chaps[: a.sample]
        next_chap = all_chaps[a.sample]
        for p in parts:
            p["chapters"] = [c for c in p["chapters"] if c in keep]
        parts = [p for p in parts if p["chapters"]]

    files = {}      # name -> (xhtml text, nav title or None)
    spine, toc = [], []   # toc: (href, label, [children])
    files["cover.xhtml"] = xhtml(L["cover_label"], '<div class="cover"><img class="cover" src="cover.jpg" alt="' + L["cover_alt"] + escape(TITLE) + '"/></div>')
    files["title.xhtml"] = xhtml(TITLE, f'<section epub:type="titlepage"><h1>{escape(TITLE)}</h1><p class="sub">{escape(SUBTITLE)}</p><p class="center">{escape(a.author)}</p></section>')
    files["copyright.xhtml"] = xhtml("Copyright", f'<section epub:type="copyright-page"><p class="noindent">{escape(TITLE)}</p><p class="noindent">&#169; {a.year} {escape(a.author)}. {L["rights"]}</p></section>')
    spine += ["cover.xhtml", "title.xhtml", "copyright.xhtml"]

    first_body = None
    for pi, part in enumerate(parts, 1):
        pf = f"part{pi}.xhtml"
        files[pf] = xhtml(part["label"], f'<section epub:type="part"><h1>{escape(part["label"])}</h1><p class="sub">{escape(part["name"])}</p></section>')
        spine.append(pf)
        kids = []
        for chap in part["chapters"]:
            num = chap["label"].split()[1]
            cf = f"ch{int(num):02d}.xhtml"
            files[cf] = xhtml(f'{chap["label"]}. {chap["title"]}', chapter_body(chap))
            spine.append(cf); kids.append((cf, f'{chap["label"]}. {chap["title"]}', []))
            first_body = first_body or cf
        toc.append((pf, f'{part["label"]}: {part["name"]}', kids))
    if a.sample:
        t1, t2, t3 = L["thanks"]
        files["sample-end.xhtml"] = xhtml(L["sample_end"], f'<section><h1>{L["sample_end"]}</h1><p class="center">{t1}{escape(next_chap["label"])}{t2}{escape(next_chap["title"])}{t3}</p></section>')
        spine.append("sample-end.xhtml")
        toc.append(("sample-end.xhtml", L["sample_end"], []))

    def nav_li(items):
        s = "<ol>"
        for href, label, kids in items:
            s += f'<li><a href="{href}">{escape(label)}</a>' + (nav_li(kids) if kids else "") + "</li>"
        return s + "</ol>"

    nav = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{L['code']}" xml:lang="{L['code']}">
<head><meta charset="utf-8"/><title>{L['contents']}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<nav epub:type="toc" id="toc"><h1>{L["contents"]}</h1>{nav_li(toc)}</nav>
<nav epub:type="landmarks" hidden="hidden"><h2>{L["guide"]}</h2><ol>
<li><a epub:type="cover" href="cover.xhtml">{L["cover_label"]}</a></li>
<li><a epub:type="toc" href="nav.xhtml">{L["contents"]}</a></li>
<li><a epub:type="bodymatter" href="{first_body}">{L["start"]}</a></li></ol></nav>
</body>
</html>
"""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="cover-image" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>']
    for n in files:
        manifest.append(f'<item id="{n.split(".")[0]}" href="{n}" media-type="application/xhtml+xml"/>')
    itemrefs = "".join('<itemref idref="%s"/>' % n.split(".")[0] for n in spine)
    # nav.xhtml sits in the spine after the copyright page so readers can reach it.
    itemrefs = itemrefs.replace('<itemref idref="part1"', '<itemref idref="nav"/><itemref idref="part1"', 1)
    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{L['code']}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{UID}</dc:identifier>
<dc:title id="t">{escape(TITLE)}</dc:title>
<dc:creator id="c1">{escape(a.author)}</dc:creator>
<meta refines="#c1" property="role" scheme="marc:relators">aut</meta>
<dc:language>{L["code"]}</dc:language>
<dc:rights>&#169; {a.year} {escape(a.author)}. {L["rights"]}</dc:rights>
<meta property="dcterms:modified">{now}</meta>
<meta name="cover" content="cover-image"/>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine>{itemrefs}</spine>
</package>
"""
    container = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    with zipfile.ZipFile(a.out, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        d = zipfile.ZIP_DEFLATED
        z.writestr("META-INF/container.xml", container, compress_type=d)
        z.writestr("OEBPS/content.opf", opf, compress_type=d)
        z.writestr("OEBPS/nav.xhtml", nav, compress_type=d)
        z.writestr("OEBPS/style.css", CSS + L["extra_css"], compress_type=d)
        z.write(a.cover, "OEBPS/cover.jpg", compress_type=zipfile.ZIP_STORED)
        for n, t in files.items():
            z.writestr("OEBPS/" + n, t, compress_type=d)
    words = sum(len(it[1].split()) for p in parts for c in p["chapters"] for it in c["items"] if it[0] == "p")
    print(f"{a.out}: {len(parts)} parts, {sum(len(p['chapters']) for p in parts)} chapters, {words} words")


if __name__ == "__main__":
    main()
