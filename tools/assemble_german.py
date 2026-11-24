#!/usr/bin/env python3
"""Assemble the German novel from work/german/ch01.md ... ch18.md (standard library only).

    python3 tools/assemble_german.py                  # writes work/german/novel_de.md
    python3 tools/assemble_german.py --allow-missing  # test build with the chapters that exist
    python3 tools/assemble_german.py --out PATH

Structure follows source/novel.md: book title, subtitle, then a part heading
before the first chapter of each part. Chapter files are never edited; only the
output file is written. Exit code 1 when a chapter file is missing (unless
--allow-missing) or a chapter heading does not match the glossary.
Titles and part names come from docs/german/glossary.md section F (chapter 18 keeps "Meet": docs/german/decisions.md, decision 10).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_TITLE = "Der Mann, den die Flut brachte"
SUBTITLE = "Ein Roman aus Ovara"
PARTS = [  # (first chapter, heading)
    (1, "Teil Eins: Angespült"),
    (3, "Teil Zwei: Der Alte"),
    (5, "Teil Drei: Das Dunkel"),
    (8, "Teil Vier: An Land"),
    (12, "Teil Fünf: Ein Meer"),
    (16, "Teil Sechs: Die Wende"),
]
TITLES = {
    1: "Wrack", 2: "Der Lastkahn", 3: "Der Drache", 4: "Der Mechaniker",
    5: "Die Lampen erlöschen", 6: "Der älteste Bruder", 7: "Die Tür",
    8: "Saltgate", 9: "Die Ingenieure", 10: "Der Tisch", 11: "Taubes Wasser",
    12: "Das Große Moot", 13: "Das Signal", 14: "Die Welle", 15: "Das Herz",
    16: "Der lange Umweg", 17: "Standort Neun", 18: "Meet",
}
COMMA_RE = re.compile(r"([?!]“)( )([a-zäöüß])")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(ROOT / "work/german"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--allow-missing", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir)
    out = Path(a.out) if a.out else d / "novel_de.md"

    problems, notes = [], []
    counts = {"comma_added": 0}
    missing, mismatched = [], []
    chunks = [f"# {BOOK_TITLE}", f"*{SUBTITLE}*", "---"]
    part_starts = dict(PARTS)
    words = paras = chapters = 0

    for n in range(1, 19):
        f = d / f"ch{n:02d}.md"
        if not f.exists():
            missing.append(f.name)
            continue
        text = f.read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n")
        lines = text.split("\n")
        want = f"## Kapitel {n}. {TITLES[n]}"
        if lines[0] != want:
            mismatched.append(f"{f.name}: heading '{lines[0]}' (expected '{want}')")
        if any(l.startswith("# ") for l in lines):
            problems.append(f"{f.name}: contains a part heading (the assembler adds those)")
        # (a) comma after ?“ / !“ before a lowercase speech tag
        def fix(m):
            counts["comma_added"] += 1
            return f"{m.group(1)},{m.group(2)}{m.group(3)}"
        text = COMMA_RE.sub(fix, text)
        lines = text.split("\n")
        if lines[-1].strip() == "---":
            # a part separator copied from the English; chapters carry none
            counts["trailing_sb"] = counts.get("trailing_sb", 0) + 1
            text = text.rstrip("-\n ").rstrip("\n")
            notes.append(f"{f.name}: trailing '---' removed from the output")
        if n in part_starts:
            chunks.append(f"# {part_starts[n]}")
        chunks.append(text)
        chapters += 1
        # checks per paragraph
        for i, para in enumerate(p for p in re.split(r"\n\s*\n", text) if p.strip()):
            if para.startswith("## ") or para.strip() == "---":
                continue
            paras += 1
            words += len(para.split())
            tag = f"{f.name} p{paras}"
            for ch, label in (("–", "en dash"), ("—", "em dash"), ('"', "straight double quote")):
                if ch in para:
                    problems.append(f"{f.name}: {label} in '{para[:50]}...'")
            if para.count("„") != para.count("“"):
                problems.append(f"{f.name}: unbalanced „ “ ({para.count('„')}/{para.count('“')}) in '{para[:50]}...' (may continue in next paragraph)")
            if para.count("*") % 2:
                problems.append(f"{f.name}: unbalanced * in '{para[:50]}...'")
            k = para.count("Bewusstseinen")
            if k:
                problems.append(f"{f.name}: 'Bewusstseinen' x{k} (not valid German; left unchanged) in '{para[:50]}...'")

    if missing and not a.allow_missing:
        pass
    out.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")

    print(f"Wrote {out}: {chapters} chapters, {paras} paragraphs, {words} words")
    print(f"Normalisation (a): {counts['comma_added']} commas added after ?“ / !“ before a lowercase speech tag")
    for nt in notes:
        print("Normalisation (d):", nt)
    print(f"Findings left for the editor ({len(problems)}):")
    for p in problems:
        print("  -", p)
    if missing:
        print(f"Missing chapter files ({len(missing)}): {', '.join(missing)}" + ("  [allowed]" if a.allow_missing else ""))
    if mismatched:
        print("Heading mismatches:")
        for m in mismatched:
            print("  -", m)
    bad = bool(mismatched) or (bool(missing) and not a.allow_missing)
    print("RESULT:", "FAIL" if bad else "OK (with findings listed above)" if problems else "OK")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
