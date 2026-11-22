"""Shared code for the visual-novel pipeline: paths, splitting, cut logic.

Standard library only. Python 3.9+.

Vocabulary
  unit       one sentence of the novel, with a stable id like c01.s02.p013.2
             (chapter 1, scene 2, paragraph 13, sentence 2)
  suggestion what the cutter agent proposes for a unit: cut it, or replace it
  decision   what the owner chose for a unit in the review app
  effective  the state that results: owner decision, else suggestion, else keep
"""
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source" / "novel.md"
WORK = ROOT / "work"
UNITS = WORK / "units"
CUTS = WORK / "cuts"
CUT_TEXT = WORK / "cut"
STATE = WORK / "state.json"

KINDS = {
    "shown": "The picture shows it",
    "redundant": "Says what is already clear",
    "pace": "Slows the scene",
    "condense": "Shorter wording",
    "other": "Other",
}

_ABBREV = re.compile(r"\b(Mr|Mrs|Ms|Dr|St|Mt|No)\.\s")
_SPLIT = re.compile(r"""([.!?…]["'”’)\*]*)\s+(?=["'“‘(\*]?[A-Z])""")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    """Write atomically, so a crash never leaves half a file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, path)


def words(text):
    return len(text.split())


def split_sentences(paragraph):
    guarded = _ABBREV.sub(lambda m: m.group(1) + ".\x01", paragraph)
    parts = _SPLIT.sub(lambda m: m.group(1) + "\x00", guarded).split("\x00")
    return [p.replace("\x01", " ").strip() for p in parts if p.strip()]


def split_novel(text):
    """Return a list of chapter dicts from the novel's markdown."""
    chapters, part, chapter, scene = [], "", None, None
    for block in re.split(r"\n\s*\n", text):
        block = " ".join(line.strip() for line in block.strip().splitlines())
        if not block:
            continue
        m = re.match(r"^# Part (.+)$", block)
        if m:
            part = m.group(1)
            continue
        m = re.match(r"^## Chapter (\d+)\.\s*(.+)$", block)
        if m:
            n = int(m.group(1))
            chapter = {"chapter": n, "title": m.group(2), "part": part, "scenes": []}
            chapters.append(chapter)
            scene = None
            continue
        if chapter is None or block.startswith("#"):
            continue  # title page
        if re.match(r"^(-{3,}|\*\s*\*\s*\*)$", block):
            scene = None
            continue
        if scene is None:
            scene = {"id": "c%02d.s%02d" % (chapter["chapter"], len(chapter["scenes"]) + 1), "paras": []}
            chapter["scenes"].append(scene)
        pid = "%s.p%03d" % (scene["id"], len(scene["paras"]) + 1)
        sents = [{"id": "%s.%d" % (pid, i + 1), "text": s} for i, s in enumerate(split_sentences(block))]
        scene["paras"].append({"id": pid, "sents": sents})
    return chapters


def source_sha():
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()[:16]


def chapter_numbers():
    return sorted(int(p.stem[2:]) for p in UNITS.glob("ch[0-9][0-9].json"))


def units_path(n):
    return UNITS / ("ch%02d.json" % n)


def suggestions_path(n):
    return CUTS / ("ch%02d.suggestions.json" % n)


def decisions_path(n):
    return CUTS / ("ch%02d.decisions.json" % n)


def review_path(n):
    return CUTS / ("ch%02d.review.json" % n)


def cut_text_path(n):
    return CUT_TEXT / ("ch%02d.md" % n)


def iter_sents(chapter):
    for scene in chapter["scenes"]:
        for para in scene["paras"]:
            for sent in para["sents"]:
                yield scene, para, sent


def load_suggestions(n, chapter):
    """Return ({sentence id: suggestion}, [problems]).

    A suggestion's id may name one sentence or a whole paragraph. A paragraph
    id is expanded to every sentence in it (cut only).
    """
    raw = read_json(suggestions_path(n), {"items": []})
    sent_ids = {s["id"] for _, _, s in iter_sents(chapter)}
    paras = {p["id"]: [s["id"] for s in p["sents"]] for sc in chapter["scenes"] for p in sc["paras"]}
    out, problems = {}, []
    for i, item in enumerate(raw.get("items", [])):
        where = "item %d (%s)" % (i + 1, item.get("id"))
        action, kind = item.get("action"), item.get("kind", "other")
        if action not in ("cut", "replace"):
            problems.append("%s: action must be 'cut' or 'replace'" % where)
            continue
        if kind not in KINDS:
            problems.append("%s: unknown kind '%s'" % (where, kind))
            continue
        if not item.get("reason"):
            problems.append("%s: no reason given" % where)
            continue
        if action == "replace" and not (item.get("text") or "").strip():
            problems.append("%s: replace needs text" % where)
            continue
        if item.get("id") in sent_ids:
            targets = [item["id"]]
        elif item.get("id") in paras and action == "cut":
            targets = paras[item["id"]]
        else:
            problems.append("%s: no such sentence (or a paragraph id used with replace)" % where)
            continue
        for sid in targets:
            if sid in out:
                problems.append("%s: second suggestion for %s" % (where, sid))
            out[sid] = {"action": action, "kind": kind, "reason": item["reason"], "text": item.get("text", "")}
    return out, problems


def effective(sent, suggestion, decision):
    """Return (state, text) for one sentence: state is keep, cut or edit."""
    if decision:
        st = decision.get("state")
        if st == "cut":
            return "cut", ""
        if st == "edit":
            return "edit", decision.get("text", "").strip()
        return "keep", sent["text"]
    if suggestion:
        if suggestion["action"] == "cut":
            return "cut", ""
        return "edit", suggestion["text"].strip()
    return "keep", sent["text"]


def chapter_stats(n):
    chapter = read_json(units_path(n))
    sugg, _ = load_suggestions(n, chapter)
    dec = read_json(decisions_path(n), {})
    decisions = dec.get("decisions", {})
    before = after = 0
    for _, _, s in iter_sents(chapter):
        before += words(s["text"])
        after += words(effective(s, sugg.get(s["id"]), decisions.get(s["id"]))[1])
    return {
        "chapter": n,
        "title": chapter["title"],
        "part": chapter["part"],
        "words": before,
        "words_after": after,
        "suggestions": len(sugg),
        "reviewed": sum(1 for sid in sugg if sid in decisions),
        "has_suggestions": suggestions_path(n).exists(),
        "approved": bool(dec.get("approved")),
        "stale": bool(dec.get("approved")) and dec.get("source_sha") != chapter.get("source_sha"),
    }


def apply_chapter(n):
    """Write the cut text and the review summary for one chapter."""
    chapter = read_json(units_path(n))
    sugg, _ = load_suggestions(n, chapter)
    dec = read_json(decisions_path(n), {})
    decisions = dec.get("decisions", {})
    lines = ["# Chapter %d. %s" % (n, chapter["title"]), ""]
    review = {"chapter": n, "written": now(), "note": dec.get("note", ""), "accepted": 0,
              "overruled": [], "owner_cuts": [], "owner_edits": [], "by_kind": {}}
    before = after = 0
    for si, scene in enumerate(chapter["scenes"]):
        if si:
            lines += ["---", ""]
        lines += ["<!-- %s -->" % scene["id"], ""]
        for para in scene["paras"]:
            kept = []
            for s in para["sents"]:
                sg, d = sugg.get(s["id"]), decisions.get(s["id"])
                state, text = effective(s, sg, d)
                before += words(s["text"])
                after += words(text)
                if text:
                    kept.append(text)
                entry = {"id": s["id"], "original": s["text"], "note": (d or {}).get("note", "")}
                if sg:
                    same = (state == "cut" and sg["action"] == "cut") or \
                           (state == "edit" and sg["action"] == "replace" and text == sg["text"].strip())
                    k = review["by_kind"].setdefault(sg["kind"], {"suggested": 0, "accepted": 0})
                    k["suggested"] += 1
                    if same:
                        k["accepted"] += 1
                        review["accepted"] += 1
                    else:
                        entry.update({"suggested": sg, "owner_state": state, "owner_text": text})
                        review["overruled"].append(entry)
                elif state == "cut":
                    review["owner_cuts"].append(entry)
                elif state == "edit":
                    entry["owner_text"] = text
                    review["owner_edits"].append(entry)
            if kept:
                lines += [" ".join(kept), ""]
    total = review["accepted"] + len(review["overruled"])
    review.update({"words": before, "words_after": after, "suggested": total,
                   "accept_rate": round(review["accepted"] / total, 3) if total else None})
    CUT_TEXT.mkdir(parents=True, exist_ok=True)
    cut_text_path(n).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    write_json(review_path(n), review)
    return review
