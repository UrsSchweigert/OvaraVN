#!/usr/bin/env python3
"""Compare the text in a staged Ren'Py chapter with the approved text.

Usage: python3 tools/check_script.py [chapter number | all, default 1]

Reads game/game/chNN.rpy and work/cut/chNN.md. Removes Ren'Py syntax, quote
marks and speech-tag drops, then compares sentence by sentence, in order.
Reports missing, extra and reordered text. Exit code 0 means they match.
"""
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEAKERS = {"c_wrack": "Wrack", "c_sefa": "Sefa", "c_oro": "Elder Oro",
            "c_ione": "Ione", "c_davin": "Davin", "c_hesper": "Hesper",
            "c_okonta": "Okonta"}

# Speech tags that only name the speaker. These are the only text the script
# may drop. Each is (text in the approved file, what is left).
ALLOWED_DROPS = {2: [
    ('hold," Sefa said. "They', 'hold," "They'),
    ('"Two," said Elder Oro.', '"Two,"'),
    ('year," he said. "Barge', 'year," "Barge'),
    ('"You nearly killed nine people," she said.', '"You nearly killed nine people,"'),
    ('wall," she said. "Lie down', 'wall," "Lie down'),
    ('thing," she said. "It\'ll', 'thing," "It\'ll'),
    ('them," she said. "I want', 'them," "I want'),
    ('"My name is Okonta," she said.', '"My name is Okonta,"'),
    ('dome," Okonta said. "Not', 'dome," "Not'),
    ('"Come back," she said.', '"Come back,"'),
], 1: [
    ('"What is it?" he said.', '"What is it?"'),
    ('"You really don\'t know anything," she said.', '"You really don\'t know anything,"'),
    ('to them," she said. "Eat', 'to them," "Eat'),
    ('so I speak last," he said.', 'so I speak last,"'),
    ('"I don\'t know what I am," Wrack said.', '"I don\'t know what I am,"'),
    ('"The undertow," Elder Oro said.', '"The undertow,"'),
    ('"Up and across," Davin said.', '"Up and across,"'),
    ('"Lampweed," Sefa said.', '"Lampweed,"'),
    ('"I don\'t know," Wrack said.', '"I don\'t know,"'),
    ('"Somebody," he said, "had', '"Somebody," "had'),
]}

LINE = re.compile(r'^\s*(?:([A-Za-z_]\w*)\s+)?"((?:[^"\\]|\\.)*)"\s*$')


def normalise(text):
    text = text.replace('"', "")
    return re.sub(r"\s+", " ", text).strip()


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", normalise(text)) if s]


def script_text(rpy, errors):
    """Return the visible text of the script, boxes joined by spaces."""
    boxes = []
    for n, line in enumerate(rpy.splitlines(), 1):
        if line.lstrip().startswith("#"):
            continue
        m = LINE.match(line)
        if not m:
            continue
        who, body = m.groups()
        if who is not None and who not in SPEAKERS:
            errors.append(f"line {n}: unknown speaker '{who}'")
            continue
        body = re.sub(r"\\(.)", r"\1", body)
        body = body.replace("{i}", "*").replace("{/i}", "*")
        body = body.replace("[[", "[").replace("{{", "{").replace("%%", "%")
        if re.search(r"\{[^}]*\}|\[[^\]]*\]", body):
            errors.append(f"line {n}: leftover Ren'Py markup in text")
        boxes.append(body)
    return " ".join(boxes)


def approved_text(md, ch, errors):
    lines = []
    for block in md.splitlines():
        s = block.strip()
        if not s or s.startswith("#") or s.startswith("<!--") or s == "---":
            continue
        lines.append(s)
    text = " ".join(lines)
    for old, new in ALLOWED_DROPS.get(ch, []):
        if text.count(old) != 1:
            errors.append(f"allowed drop not found exactly once: {old}")
        text = text.replace(old, new)
    return text


def compare(approved, script):
    a, b = sentences(approved), sentences(script)
    errors = []
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        for s in a[i1:i2]:
            errors.append(f"missing or changed: {s}")
        for s in b[j1:j2]:
            errors.append(f"extra or changed: {s}")
    # Reordered text: same sentences, different order.
    if not errors and a != b:
        errors.append("order differs")
    if errors and sorted(a) == sorted(b):
        errors.insert(0, "reordered: the same sentences appear in a different order")
    dup = [s for s in set(b) if b.count(s) != a.count(s)]
    for s in dup:
        errors.append(f"repeated a different number of times: {s}")
    return errors


def check(ch, root=ROOT):
    errors = []
    rpy = (root / "game" / "game" / f"ch{ch:02d}.rpy").read_text(encoding="utf-8")
    md = (root / "work" / "cut" / f"ch{ch:02d}.md").read_text(encoding="utf-8")
    script = script_text(rpy, errors)
    approved = approved_text(md, ch, errors)
    errors += compare(approved, script)
    return errors, len(sentences(approved))


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "1"
    if arg == "all":
        chs = sorted(int(p.stem[2:]) for p in (ROOT / "game" / "game").glob("ch[0-9][0-9].rpy"))
    else:
        chs = [int(arg)]
    status = 0
    for ch in chs:
        errors, n = check(ch)
        if errors:
            print(f"chapter {ch}: {len(errors)} problem(s)")
            for e in errors:
                print("  " + e)
            status = 1
        else:
            print(f"chapter {ch}: script matches the approved text ({n} sentences, in order)")
    return status


if __name__ == "__main__":
    sys.exit(main())
