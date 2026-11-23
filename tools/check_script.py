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
            "c_okonta": "Okonta", "c_brask": "Brask",
            "c_jef": "Jef", "c_maelis": "Maelis", "c_anselm": "Anselm", "c_vey": "Elder Vey", "c_aurel": "Aurel", "c_corin": "Corin",
            "c_ilan": "Ilan", "c_nerys": "Nerys", "c_dace": "Dace", "c_yeva": "Yeva",
            "c_pell": "Pell", "c_marsh": "Linnea Marsh", "c_garran": "Garran",
            "c_raske": "Teodora Raske"}

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
], 4: [
    ('The Lantern," said Okonta. "The', 'The Lantern," "The'),
    ('"Somebody\'s been in my Dragon," Jef said.', '"Somebody\'s been in my Dragon,"'),
    ('month," she said. "They', 'month," "They'),
    ('"Somebody tied your hands," she said.', '"Somebody tied your hands,"'),
    ('walls," Jef said. "You', 'walls," "You'),
    ('"Well-wardens," said Jef. "Squid', '"Well-wardens," "Squid'),
    ('here?" he asked. "Why', 'here?" "Why'),
    ('place," Jef said. He did not', 'place," He did not'),
    ('Jef said "Hm," and went', '"Hm," and went'),
    ('gift," the old man said. He was', 'gift," He was'),
    ('end," she said. "You', 'end," "You'),
    ('me?" he said. He set', 'me?" He set'),
    ('know," said Jef. "Maelis', 'know," "Maelis'),
    ('name," Maelis said. "I think', 'name," "I think'),
    ('know," he said. "I\'m', 'know," "I\'m'),
    ('all," she said. "It', 'all," "It'),
    ('"Sorry," she said. "He', '"Sorry," "He'),
    ('Needle," she said. "One', 'Needle," "One'),
    ('"Hello, old man," the visitor said.', '"Hello, old man,"'),
    ('Anselm," said Jef. "You', 'Anselm," "You'),
    ('kitchen," Maelis said. Her', 'kitchen," Her'),
    ('"He can open a seam," Jef said.', '"He can open a seam,"'),
    ('vault," Jef said. "I\'d', 'vault," "I\'d'),
    ('"What am I to you?" Wrack said.', '"What am I to you?"'),
    ('Yes," he said. "I do', 'Yes," "I do'),
    ('"I\'ll stay," he said.', '"I\'ll stay,"'),
    ('No," said Jef. "I', 'No," "I'),
    ('time. Then Okonta said, "That', 'time. "That'),
    ('"What does he do now?" Wrack asked.', '"What does he do now?"'),
    ('you," Jef said. "I took', 'you," "I took'),
    ('it," she said. "You\'ve', 'it," "You\'ve'),
    ('me," Jef said. "She\'s', 'me," "She\'s'),
    ('notch," he said. "Don\'t', 'notch," "Don\'t'),
    ('"Lend me that," he said.', '"Lend me that,"'),
    ('back," Jef said. "Don\'t', 'back," "Don\'t'),
    ('mine," he said. "I made', 'mine," "I made'),
    ('"There are three hundred people in those pools," Maelis said.', '"There are three hundred people in those pools,"'),
    ('it," she said. "Something', 'it," "Something'),
    ('"He left something for me to tell you," Maelis said.', '"He left something for me to tell you,"'),
], 5: [
    ('"How long?" Okonta asked.', '"How long?"'),
    ('know," she said. "It\'s', 'know," "It\'s'),
    ('"Then I\'ll learn on the way," he said.', '"Then I\'ll learn on the way,"'),
    ('"Deep Chorus," Okonta said. Her', '"Deep Chorus," Her'),
    ('"Lampweed," said Okonta. Her', '"Lampweed," Her'),
    ('Lantern," Okonta said. "Nine', 'Lantern," "Nine'),
    ('things," said Elder Vey, "since', 'things," "since'),
    ('"How long for the people up there?" he said.', '"How long for the people up there?"'),
    ('name?" he said. "The', 'name?" "The'),
    ('"Bother," she said.', '"Bother,"'),
    ('"We were afraid," she said.', '"We were afraid,"'),
    ('"She does that," Wrack said.', '"She does that,"'),
    ('"Two of the hearts you could not mend," Vey said.', '"Two of the hearts you could not mend,"'),
    ('Dragon," she said. "You', 'Dragon," "You'),
    ('"We\'ll see," said Wrack.', '"We\'ll see,"'),
], 6: [
    ('"Corin," Okonta said. Something', '"Corin," Something'),
    ('"Nobody called you," Okonta said.', '"Nobody called you,"'),
    ('"You said it," said Okonta. "I was', '"You said it," "I was'),
    ('"I\'m told that somebody tried to scratch this out," he said. The voice', '"I\'m told that somebody tried to scratch this out," The voice'),
    ('"You sent that dart," Wrack said.', '"You sent that dart,"'),
    ('"I aimed at a machine," Anselm Rook said. "He', '"I aimed at a machine," "He'),
    ('"I couldn\'t do anything," he said.', '"I couldn\'t do anything,"'),
    ('"No," said Okonta.', '"No,"'),
    ('"Again," she said.', '"Again,"'),
    ('"He can stand now," Sefa said. "He', '"He can stand now," "He'),
    ('"He had us carry for him as well," she said. "He', '"He had us carry for him as well," "He'),
    ('"I\'m going to my mother," he said. He would', '"I\'m going to my mother," He would'),
    ('"Then go and keep that water," Okonta said. "It\'s', '"Then go and keep that water," "It\'s'),
    ('"He wanted it mended," he said.', '"He wanted it mended,"'),
    ('"He held all this up," Wrack said. "One', '"He held all this up," "One'),
    ('"Yes," said Okonta. She was', '"Yes," She was'),
], 7: [
    ('"The Girdle," Okonta said. She', '"The Girdle," She'),
    ('away," Okonta said. "That\'s', 'away," "That\'s'),
    ('hulls," Okonta said. "That', 'hulls," "That'),
    ('coral," Okonta said. "Don', 'coral," "Don'),
    ('open*," she said. "Where', 'open*," "Where'),
    ('"The Smokers," Okonta said. Her', '"The Smokers," Her'),
    ('"It\'s all right," he said. He did', '"It\'s all right," He did'),
    ('"*He has to ask for his memory himself,*" he said.', '"*He has to ask for his memory himself,*"'),
    ('something," he said. "I\'ve', 'something," "I\'ve'),
    ('did," he said, "I\'ll', 'did," "I\'ll'),
    ('"I did it," he said. "Low', '"I did it," "Low'),
    ('"And it was him," Ilan said. "On', '"And it was him," "On'),
    ('name," he said. "It\'s Ilan', 'name," "It\'s Ilan'),
    ('"All of it," she said. She', '"All of it," She'),
    ('"My mother\'s arms," she said.', '"My mother\'s arms,"'),
], 3: [
    ('it," he said. "Like', 'it," "Like'),
    ('singers," Okonta said. "Whales', 'singers," "Whales'),
    ('seasons," Okonta said. "The', 'seasons," "The'),
    ('you," Okonta said. "Everybody', 'you," "Everybody'),
    ('Engines," she said. "Four', 'Engines," "Four'),
    ('Breakers," Okonta said. "They', 'Breakers," "They'),
    ('Sounding," she said. "Six', 'Sounding," "Six'),
    ('us," she said. "Someone', 'us," "Someone'),
    ('Slick," said Okonta. "Twenty', 'Slick," "Twenty'),
    ('eels," Okonta said. "They', 'eels," "They'),
    ('stone," Okonta said. "There', 'stone," "There'),
    ('on," she said. She had', 'on," She had'),
    ('passenger," Okonta said. "I\'ll', 'passenger," "I\'ll'),
    ('man," he said. He had', 'man," He had'),
    ('him," she said. "Alive', 'him," "Alive'),
    ('tired," he said. "It\'s so', 'tired," "It\'s so'),
    ('in," Okonta said. She was', 'in," She was'),
    ('for," Okonta said. She had', 'for," She had'),
    ('latch," Okonta said. "Leave', 'latch," "Leave'),
    ('Pale," he said. "Since', 'Pale," "Since'),
    ('stop," Okonta said. "Except', 'stop," "Except'),
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
], 8: [
    ('Belt," she said. "That\'s', 'Belt," "That\'s'),
    ('party," she said. "I\'m Dace', 'party," "I\'m Dace'),
    ('"I am," said Ilan.', '"I am,"'),
    ('"It\'s so loud," she said. "How', '"It\'s so loud," "How'),
    ('room," he said. "Start', 'room," "Start'),
    ('it?" Sefa said. "Being', 'it?" "Being'),
    ('something," he said. "I liked', 'something," "I liked'),
    ('"Where\'s the dark?" she said. "Where', '"Where\'s the dark?" "Where'),
    ('"They don\'t keep any," said Dace.', '"They don\'t keep any,"'),
    ('Lockkeepers," Dace said. "They\'re', 'Lockkeepers," "They\'re'),
    ('"You had a different mouth," she said.', '"You had a different mouth,"'),
    ('else," Ilan said. "My mother', 'else," "My mother'),
    ('button," Ilan said.', 'button,"'),
    ('Hands," she had explained. "It\'s', 'Hands," "It\'s'),
    ('plant," he said. "I signed', 'plant," "I signed'),
    ('woman," Pell said. He spoke', 'woman," He spoke'),
    ('Wellwalker," Sefa said. She said', 'Wellwalker," She said'),
    ('one," Sefa said. "And put', 'one," "And put'),
    ('working," Ilan said. "It fades', 'working," "It fades'),
    ('"Then how do we get in?" Dace asked.', '"Then how do we get in?"'),
    ('"I\'m sorry," he said. "For all', '"I\'m sorry," "For all'),
    ('move," Yeva said. "Now', 'move," "Now'),
    ('"There," Yeva said. "That\'s', '"There," "That\'s'),
    ('one," she said. They were', 'one," They were'),
    ('too," Yeva said. "It told', 'too," "It told'),
    ('road," she said, "and I', 'road," "and I'),
    ('months," Dr Linnea Marsh said. "I signed', 'months," "I signed'),
    ('yourself," Yeva said. "I could', 'yourself," "I could'),
    ('"Why?" Yeva said.', '"Why?"'),
    ('again," Yeva said. "The girl', 'again," "The girl'),
    ('first," Sefa said. "Empty', 'first," "Empty'),
    ('"Can you do it?" Ilan asked. "It', '"Can you do it?" "It'),
    ('"No," she said. "Brightwater', '"No," "Brightwater'),
    ('"She meant it," she said. "I could', '"She meant it," "I could'),
    ('"I don\'t know," said Ilan. "I\'ve', '"I don\'t know," "I\'ve'),
    ('them," he said. "Not quite', 'them," "Not quite'),
    ('"Ilan Voss," he said. "I was', '"Ilan Voss," "I was'),
    ('"Thought you were drowned," he said.', '"Thought you were drowned,"'),
], 9: [
    ('earnest," Dace said. "Where', 'earnest," "Where'),
    ('engine," Okonta said. "Six', 'engine," "Six'),
    ('shipyard," Ilan said. "I\'m', 'shipyard," "I\'m'),
    ('day," Ilan said. "They', 'day," "They'),
    ('"Slip Nine," he said. "The', '"Slip Nine," "The'),
    ('drowned," she said. "I went', 'drowned," "I went'),
    ('this," Raske said. "They', 'this," "They'),
    ('"Show me that again," she said.', '"Show me that again."'),
    ('"A man in grey brought you to this loft," she said.', '"A man in grey brought you to this loft,"'),
    ('"How many can you carry?" Raske asked Dace.', '"How many can you carry?"'),
    ('tugs," said the hull man. "I', 'tugs," "I'),
    ('lamp," she said. "At', 'lamp," "At'),
    ('"Bring it," Ilan said.', '"Bring it,"'),
    ('"Halcyon," Dace said. "It', '"Halcyon," "It'),
    ('Moot," she said. "All', 'Moot," "All'),
    ('"Good," he said. "I', '"Good," "I'),
    ('make," he said. "I can', 'make," "I can'),
    ('built," he said. "The', 'built," "The'),
    ('Eye," he said. "Grey', 'Eye," "Grey'),
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
