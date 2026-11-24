#!/usr/bin/env python3
"""Check a German chapter translation (standard library only).

    python3 tools/check_translation.py 2          # chapter 2
    python3 tools/check_translation.py ch02 -v    # also list every line's length
    python3 tools/check_translation.py all        # chapters 1 to 18, one summary each

Reads game/game/tl/german/chNN.rpy (the Ren'Py translation file) and game/game/chNN.rpy
(the English script), and reports:
  - stale or missing lines (the English comment in the tl file no longer matches the script)
  - untranslated lines (German identical to English)
  - text tags ({i}, {/i}, {w} ...) that differ from the English
  - interpolation ([name]) and % differences
  - en dashes, em dashes, straight double quotes inside the German text
  - banned words (decisions in docs/german/decisions.md that are unambiguous)
  - length: estimated text-box lines (75 characters per line); flags above 420 characters
Exit code 1 when anything is flagged.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAME = ROOT / "game" / "game"
TL = GAME / "tl" / "german"

CHARS_PER_LINE = 75
MAX_CHARS = 420
MAX_LINES = 6

# (regex, why). Only decisions that are unambiguous.
BANNED = [
    (r"\bHorts?\b|\bHorte\b|\bHorten\b", "hold is 'die Halte', not 'Hort'"),
    (r"\bMariner\b|\bMarinern?\b", "mariners are 'Meerleute'"),
    (r"\bSeeleute\b", "mariners are 'Meerleute', not 'Seeleute'"),
    (r"\bThread(ed)?\b", "Thread is 'Faden', Threaded 'Fadenträger'"),
    (r"\bBother\b", "Bother is 'Plagegeist'"),
    (r"\bBitterwrack\b", "bitterwrack is 'Bittertang'"),
    (r"\bElder\b", "Elder is 'Ältester/Älteste'"),
    (r"\bBarge\b", "barge is 'Lastkahn'"),
    (r"Wracktaucher", "'Wrack' is the hero's name"),
    (r"\bfragen\b.*\b(Meer|See)\b|\b(Meer|See)\b.*\bfrag(e|st|t|en)\b", "the sea is 'gebeten', never 'gefragt'"),
]

TAG = re.compile(r"\{/?[a-z]+(?:=[^}]*)?\}|\{[a-z]+=[^}]*\}")
INTERP = re.compile(r"\[[^\]]*\]")


def unescape(s):
    return s.replace('\\"', '"').replace("\\\\", "\\")


def script_lines(chapter_rpy):
    """Dialogue and narration strings of the English script, in order."""
    out = []
    rx = re.compile(r'^\s+(?:c_\w+\s+)?"(.*)"\s*$')
    for line in chapter_rpy.read_text(encoding="utf-8").split("\n"):
        m = rx.match(line)
        if m and not re.match(r"\s*(scene|show|hide|with|play|stop|jump|call|\$|define|label)\b", line):
            out.append(unescape(m.group(1)))
    return out


def tl_entries(tl_file):
    text = tl_file.read_text(encoding="utf-8-sig")
    rx = re.compile(r'^translate german (\w+):\n\n    # (?:c_\w+ )?"(.*)"\n    (?:c_\w+ )?"(.*)"\n', re.M)
    return [(i, unescape(en), unescape(de)) for i, en, de in rx.findall(text)]


def est_lines(text):
    """Word-wrapped line count at CHARS_PER_LINE characters."""
    plain = TAG.sub("", text)
    n, cur = 1, 0
    for w in plain.split(" "):
        add = len(w) + (1 if cur else 0)
        if cur + add > CHARS_PER_LINE and cur:
            n += 1
            cur = len(w)
        else:
            cur += add
    return n


def main(argv):
    args = [a for a in argv if not a.startswith("-")]
    verbose = "-v" in argv
    if not args:
        print(__doc__)
        return 2
    if args[0] == "all":
        worst = 0
        for k in range(1, 19):
            worst = max(worst, main([str(k)] + [a for a in argv if a.startswith("-")]))
        return worst
    m = re.fullmatch(r"(?:ch)?0*(\d{1,2})", args[0])
    if not m:
        print("chapter must be a number or chNN")
        return 2
    name = "ch%02d" % int(m.group(1))
    tl_file, rpy = TL / (name + ".rpy"), GAME / (name + ".rpy")
    if not tl_file.exists():
        print("no translation file", tl_file)
        return 1
    entries = tl_entries(tl_file)
    english = script_lines(rpy)
    flags = []

    def flag(i, kind, msg):
        flags.append("%-14s %s  %s" % (kind, i, msg))

    if [e for _, e, _ in entries] != english:
        a, b = [e for _, e, _ in entries], english
        flag("-", "STALE", "tl file has %d lines, script has %d; first difference at line %d" % (
            len(a), len(b), next((k + 1 for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)) + 1)))

    longest_de = (0, "")
    longest_en = (0, "")
    most_lines = (0, "")
    for k, (i, en, de) in enumerate(entries, 1):
        ref = "#%d %s" % (k, i)
        if de == en and len(en.split()) > 2:
            flag(ref, "UNTRANSLATED", en[:60])
        if TAG.findall(en) != TAG.findall(de):
            flag(ref, "TAGS", "English %s, German %s" % (TAG.findall(en), TAG.findall(de)))
        if INTERP.findall(en) != INTERP.findall(de) or en.count("%") != de.count("%"):
            flag(ref, "INTERPOLATION", "differs from English")
        # any tag-like text that survived the tag regex (unbalanced braces)
        if de.count("{") != de.count("}"):
            flag(ref, "BRACES", "unbalanced { }")
        if "–" in de or "—" in de:
            flag(ref, "DASH", "en or em dash found")
        if re.search(r"(?<!\w)--(?!\w)", de):
            flag(ref, "DASH", "double hyphen found")
        if '"' in de:
            flag(ref, "QUOTE", 'straight double quote inside the German text')
        if de.count("\u201e") != de.count("\u201c") or de.count("\u201a") != de.count("\u2018"):
            flag(ref, "QUOTE", "unbalanced German quotes")
        for rx, why in BANNED:
            if re.search(rx, de):
                flag(ref, "BANNED", "%s: %s" % (why, de[:70]))
        plain_de, plain_en = TAG.sub("", de), TAG.sub("", en)
        if len(plain_de) > longest_de[0]:
            longest_de = (len(plain_de), ref)
        if len(plain_en) > longest_en[0]:
            longest_en = (len(plain_en), ref)
        nl = est_lines(de)
        if nl > most_lines[0]:
            most_lines = (nl, ref)
        if len(plain_de) > MAX_CHARS:
            flag(ref, "LENGTH", "%d characters (English %d), about %d lines" % (len(plain_de), len(plain_en), nl))
        elif nl > MAX_LINES:
            flag(ref, "LENGTH", "about %d lines (more than %d)" % (nl, MAX_LINES))
        if verbose:
            print("%-28s de %4d  en %4d  ratio %.2f  lines %d" % (ref, len(plain_de), len(plain_en),
                                                                  len(plain_de) / max(1, len(plain_en)), nl))

    tot_de = sum(len(TAG.sub("", d)) for _, _, d in entries)
    tot_en = sum(len(TAG.sub("", e)) for _, e, _ in entries)
    print("%s: %d lines in the tl file, %d in the English script" % (name, len(entries), len(english)))
    print("longest German line:  %d characters (%s)" % longest_de)
    print("longest English line: %d characters (%s)" % longest_en)
    print("most estimated German box lines: %d (%s)" % most_lines)
    print("total characters: German %d, English %d (ratio %.2f)" % (tot_de, tot_en, tot_de / max(1, tot_en)))
    if flags:
        print("\n%d flag(s):" % len(flags))
        for f in flags:
            print("  " + f)
        return 1
    print("no flags")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
