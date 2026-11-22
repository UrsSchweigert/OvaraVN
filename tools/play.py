"""./vn play: start the game, optionally straight at a chapter.

    ./vn play          start the game (main menu)
    ./vn play 2        start at chapter 2  (also: ch02)
    ./vn play --list   show which chapters are built

Closes any game window that is already open first, so only one is ever running.
The game reads the environment variable VN_START (see game/game/dev.rpy).
"""
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import vnlib as L

GAME_DIR = L.ROOT / "game"


def built_chapters(script_dir=None):
    """Chapter numbers that have a `label chNN:` in the game's scripts."""
    found = set()
    for p in Path(script_dir or GAME_DIR / "game").glob("*.rpy"):
        for m in re.finditer(r"^label ch(\d\d):", p.read_text(encoding="utf-8"), re.M):
            found.add(int(m.group(1)))
    return sorted(found)


def parse_chapter(arg):
    m = re.fullmatch(r"(?:ch)?0*(\d{1,2})", arg.strip().lower())
    if not m or not 1 <= int(m.group(1)) <= 18:
        raise ValueError("chapter must be a number from 1 to 18 (or ch01 .. ch18), not '%s'" % arg)
    return int(m.group(1))


def sdk_path():
    sdk = (L.read_json(L.ROOT / "config" / "local.json", {}) or {}).get("renpy_sdk")
    if not sdk or not (Path(sdk) / "renpy.sh").exists():
        raise RuntimeError("Ren'Py is not set up: put its folder in config/local.json as renpy_sdk")
    return sdk


def build_launch(chapter, sdk):
    """Return (command, environment) that starts the game, at `chapter` if given."""
    env = dict(os.environ)
    env.pop("VN_START", None)
    if chapter is not None:
        env["VN_START"] = "ch%02d" % chapter
    return [str(Path(sdk) / "renpy.sh"), str(GAME_DIR)], env


def main(argv):
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    built = built_chapters()
    if argv and argv[0] == "--list":
        print("Built chapters: " + (", ".join(str(n) for n in built) or "none"))
        return 0
    chapter = None
    if argv:
        try:
            chapter = parse_chapter(argv[0])
        except ValueError as e:
            print(e, file=sys.stderr)
            return 1
        if chapter not in built:
            print("Chapter %d is not built yet. Built: %s" % (chapter, ", ".join(map(str, built)) or "none"),
                  file=sys.stderr)
            return 1
    try:
        sdk = sdk_path()
    except RuntimeError as e:
        print(e, file=sys.stderr)
        return 1
    subprocess.run(["pkill", "-9", "-f", "%s/lib/.*/renpy" % sdk], stdout=subprocess.DEVNULL)
    cmd, env = build_launch(chapter, sdk)
    log = Path(tempfile.gettempdir()) / "vn-play.log"
    proc = subprocess.Popen(cmd, env=env, stdout=open(log, "w"), stderr=subprocess.STDOUT, start_new_session=True)
    time.sleep(10)
    if proc.poll() is not None:
        print("The game closed straight away. See %s" % log, file=sys.stderr)
        return 1
    text = log.read_text(errors="replace")
    if "Exception" in text:
        print("The game started but reported an error. See %s" % log, file=sys.stderr)
        return 1
    subprocess.run(["osascript", "-e", 'tell application "System Events" to set frontmost of (first process whose unix id is %d) to true' % proc.pid],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Game started%s. Log: %s" % (" at chapter %d" % chapter if chapter else "", log))
    return 0
