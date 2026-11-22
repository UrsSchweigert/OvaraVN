"""./vn art: the index of all art, a gallery to browse it, and a consistency check.

    ./vn art            rebuild art/index.json and art/index.html, print a summary
    ./vn art open       rebuild, then open the gallery in the browser
    ./vn art check      consistency check (exit 1 if something is wrong)
    ./vn art canon NAME print the fixed features and reference files for a character
                        (paste into prompts; pass the references with --ref)

The index ties every image in the game to: what it is, the file it came from,
the prompt and model that made it, what it cost, and which chapters use it.
Fixed features of every recurring character live in art/canon.json.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

import vnlib as L

# game portrait name -> base file name used for the source/reference image
BASE_ALIAS = {
    "sefa_wary": "sefa", "wrack_bewildered": "wrack", "wrack_tunic_troubled": "wrack_tunic",
    "oro_gentle": "oro", "ione_calm": "ione", "davin_smile": "davin", "bother_pleased": "bother",
    "hesper_stern": "hesper", "okonta_grave": "okonta",
    "brask_watchful": "brask", "fallow_woman_weary": "fallow_woman", "fallow_man_frail": "fallow_man",
    "officer_hard": "officer",
}
CHAR_NAMES = {"wrack_tunic": "Wrack", "wrack": "Wrack", "sefa": "Sefa", "bother": "Bother", "oro": "Elder Oro",
              "ione": "Ione", "davin": "Davin", "hesper": "Hesper", "okonta": "Okonta",
              "brask": "Brask", "fallow_woman": "The woman from Fallow", "fallow_man": "The old man from Fallow",
              "officer": "The diver officer"}


def _root(root=None):
    return Path(root) if root else L.ROOT


def parse_registrations(root=None):
    """Return {'p': {name: file}, 'bg': {...}, 'cg': {...}} from game/game/images*.rpy."""
    r = _root(root)
    out = {"p": {}, "bg": {}, "cg": {}}
    for path in sorted((r / "game" / "game").glob("images*.rpy")):
        for m in re.finditer(r"^image (p|bg|cg) (\S+) =\s*(.+)$", path.read_text(encoding="utf-8"), re.M):
            kind, name, rhs = m.groups()
            f = re.search(r'"([^"]+\.png)"', rhs)
            if f:
                out[kind][name] = f.group(1)
    return out


def scan_usage(root=None):
    """Return {kind: {name: {chapter number: count}}} from game/game/chNN.rpy."""
    r = _root(root)
    use = {"p": {}, "bg": {}, "cg": {}}
    pats = {"p": r"show p (\S+)", "bg": r"scene bg (\S+)", "cg": r"scene cg (\S+)"}
    for path in sorted((r / "game" / "game").glob("ch[0-9][0-9].rpy")):
        n = int(path.stem[2:])
        text = path.read_text(encoding="utf-8")
        for kind, pat in pats.items():
            for m in re.finditer(pat, text):
                d = use[kind].setdefault(m.group(1), {})
                d[n] = d.get(n, 0) + 1
    return use


def read_ledger(root=None):
    """Return {resolved output path: ledger row} (the last successful row per file)."""
    r = _root(root)
    rows = {}
    p = r / "work" / "ledger.jsonl"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                if row.get("ok"):
                    rows[str(Path(row["out"]).resolve())] = row
    return rows


def _find(root, kind_dir, name):
    for p in sorted((_root(root) / "art" / "refs").glob("ch*/%s/%s.png" % (kind_dir, name))):
        return p
    return None


def _prompt_for(path):
    t = Path(path).with_suffix(".txt")
    if t.exists():
        return t.read_text(encoding="utf-8").strip()
    return ""


def build_index(root=None):
    r = _root(root)
    regs, usage, ledger = parse_registrations(r), scan_usage(r), read_ledger(r)
    items = []

    def add(kind, name, game_file, source):
        src = Path(source) if source else None
        row = ledger.get(str(src.resolve())) if src else None
        items.append({
            "kind": {"p": "portrait", "bg": "background", "cg": "illustration"}[kind],
            "id": "%s %s" % (kind, name),
            "game_file": "game/game/images/" + game_file,
            "source": str(src.relative_to(r)) if src else None,
            "prompt": _prompt_for(src) if src else "",
            "model": row.get("model") if row else None,
            "cost": row.get("cost") if row else None,
            "chapters": {str(k): v for k, v in sorted(usage[kind].get(name, {}).items())},
            "character": None,
        })
        return items[-1]

    for name, f in sorted(regs["p"].items()):
        base = BASE_ALIAS.get(name, name)
        src = _find(r, "portraits", base)
        it = add("p", name, f, src)
        key = next((k for k in sorted(CHAR_NAMES, key=len, reverse=True) if name == k or name.startswith(k + "_")), None)
        it["character"] = CHAR_NAMES.get(key)
        it["emotion"] = name[len(key) + 1:] if key and name != key else None
    for name, f in sorted(regs["bg"].items()):
        add("bg", name, f, _find(r, "places", Path(f).stem))
    for name, f in sorted(regs["cg"].items()):
        stem = Path(f).stem
        src = _find(r, "cg", re.sub(r"^c2_", "", stem)) if stem.startswith("c2_") else _find(r, "cg", stem)
        add("cg", name, f, src)
    canon = L.read_json(r / "art" / "canon.json", {}) or {}
    return {"generated": L.now(), "count": len(items), "items": items, "canon": canon}


def check(index, root=None):
    r = _root(root)
    errs = []
    for it in index["items"]:
        if not (r / it["game_file"]).exists():
            errs.append("%s: game file missing: %s" % (it["id"], it["game_file"]))
        if it["kind"] == "portrait" and not it["source"]:
            errs.append("%s: no reference image in art/refs/*/portraits/" % it["id"])
    usage = scan_usage(r)
    regs = parse_registrations(r)
    for kind in ("p", "bg", "cg"):
        for name in usage[kind]:
            if name not in regs[kind]:
                errs.append("script uses '%s %s' but it is not registered in images*.rpy" % (kind, name))
    canon_chars = set((index.get("canon") or {}).get("characters", {}))
    shown = {it["character"] for it in index["items"] if it["kind"] == "portrait" and it["character"]}
    for c in sorted(shown - canon_chars):
        errs.append("character '%s' has portraits but no entry in art/canon.json" % c)
    for c, d in ((index.get("canon") or {}).get("characters", {})).items():
        for ref in d.get("references", []):
            if not (r / ref).exists():
                errs.append("canon: reference for %s missing: %s" % (c, ref))
    return errs


def gallery_html(index):
    esc = html.escape
    groups = {}
    for it in index["items"]:
        key = it["character"] if it["kind"] == "portrait" else it["kind"].title() + "s"
        groups.setdefault(key or "Other", []).append(it)
    parts = ["<!doctype html><meta charset=utf-8><title>Art index</title>",
             "<style>body{font:14px system-ui;margin:20px;background:#15171a;color:#e8e6df}"
             "h2{margin:28px 0 8px;border-bottom:1px solid #444}.g{display:flex;flex-wrap:wrap;gap:12px}"
             ".c{width:220px;background:#1f2226;border-radius:6px;padding:6px}.c img{width:100%;background:#445}"
             ".bg img,.cg img{background:#223}small{color:#9a9;display:block}details{margin-top:4px;color:#aaa}"
             "summary{cursor:pointer}pre{white-space:pre-wrap;font-size:11px}</style>",
             "<h1>Art index</h1><p>%d images. Generated %s. Fixed features: art/canon.json.</p>" % (index["count"], index["generated"])]
    for key, items in groups.items():
        parts.append("<h2>%s <small>(%d)</small></h2><div class=g>" % (esc(key), len(items)))
        for it in items:
            chs = ", ".join("ch%s×%d" % (k, v) for k, v in it["chapters"].items()) or "unused"
            cost = "$%.3f" % it["cost"] if it["cost"] is not None else ""
            parts.append(
                "<div class='c %s'><img src='../%s' loading=lazy><b>%s</b>"
                "<small>%s %s %s</small><small>used: %s</small><details><summary>prompt</summary><pre>%s</pre></details></div>"
                % (it["kind"][:2], esc(it["game_file"]), esc(it["id"]), esc(it.get("model") or ""), cost,
                   esc(it["source"] or ""), esc(chs), esc(it["prompt"] or "(no prompt saved)")))
        parts.append("</div>")
    canon = index.get("canon", {})
    if canon.get("characters"):
        parts.append("<h2>Fixed features (canon)</h2>")
        for n, d in canon["characters"].items():
            parts.append("<p><b>%s</b>: %s</p>" % (esc(n), esc(d.get("fixed", ""))))
    return "\n".join(parts)


def write_index(root=None):
    r = _root(root)
    idx = build_index(r)
    L.write_json(r / "art" / "index.json", idx)
    (r / "art" / "index.html").write_text(gallery_html(idx), encoding="utf-8")
    return idx


def main(argv):
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv and argv[0] == "canon":
        canon = (L.read_json(L.ROOT / "art" / "canon.json", {}) or {}).get("characters", {})
        name = " ".join(argv[1:]).lower()
        hit = next((k for k in canon if k.lower() == name), None)
        if not hit:
            print("Known: " + ", ".join(canon), file=sys.stderr)
            return 1
        d = canon[hit]
        print("%s: %s" % (hit, d.get("fixed", "")))
        for k in ("outfit", "outfits", "note"):
            if d.get(k):
                print("  %s: %s" % (k, d[k]))
        print("References (pass with --ref):")
        for ref in d.get("references", []):
            print("  " + ref)
        return 0
    idx = write_index()
    if argv and argv[0] == "check":
        errs = check(idx)
        for e in errs:
            print(" -", e)
        print("art check: %d problems in %d images" % (len(errs), idx["count"]))
        return 1 if errs else 0
    kinds = {}
    for it in idx["items"]:
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
    unused = sum(1 for it in idx["items"] if not it["chapters"])
    print("Indexed %d images (%s); %d not used in any chapter yet." % (
        idx["count"], ", ".join("%d %ss" % (v, k) for k, v in sorted(kinds.items())), unused))
    print("Gallery: art/index.html   Data: art/index.json")
    if argv and argv[0] == "open":
        subprocess.run(["open", str(L.ROOT / "art" / "index.html")])
    return 0
