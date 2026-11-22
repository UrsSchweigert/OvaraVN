#!/usr/bin/env python3
"""Make a WebP copy of the Ren'Py project for the iOS build.

usage: webp_game.py SRC_PROJECT DEST_PROJECT [--quality 90]

Copies SRC_PROJECT (the folder that holds game/) to DEST_PROJECT, converts every
PNG under game/images to WebP with cwebp, and rewrites the .png paths in the
copied .rpy files. The source project is never touched. Standard library only;
needs the `cwebp` command (brew install webp).
"""
import argparse, os, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

SKIP = shutil.ignore_patterns("cache", "saves", "*.rpyc", "*.rpymc", "*.bak", "*.rpy-E", "__pycache__", ".DS_Store")


def convert(png, quality):
    out = png[:-4] + ".webp"
    subprocess.run(["cwebp", "-quiet", "-q", str(quality), "-alpha_q", "100", "-m", "6", png, "-o", out], check=True)
    os.remove(png)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dest")
    ap.add_argument("--quality", type=int, default=90)
    a = ap.parse_args()
    if shutil.which("cwebp") is None:
        sys.exit("cwebp not found (brew install webp)")
    if os.path.exists(a.dest):
        shutil.rmtree(a.dest)
    shutil.copytree(a.src, a.dest, ignore=SKIP)
    game = os.path.join(a.dest, "game")
    pngs = [os.path.join(d, f) for d, _, fs in os.walk(os.path.join(game, "images")) for f in fs if f.endswith(".png")]
    with ThreadPoolExecutor(os.cpu_count() or 4) as ex:
        list(ex.map(lambda p: convert(p, a.quality), pngs))
    converted = {os.path.relpath(p[:-4] + ".webp", game) for p in pngs}

    def exists(ref):
        # Ren'Py looks in game/ and, for images, in game/images/
        for base in ("", "images/"):
            rel = os.path.normpath(base + ref[:-4] + ".webp")
            if rel in converted:
                return True
        return False

    pat = re.compile(r'(["\'])([^"\'\n]+?)\.png\1')
    changed = 0
    for d, _, fs in os.walk(game):
        for f in fs:
            if not f.endswith(".rpy"):
                continue
            p = os.path.join(d, f)
            s = open(p, encoding="utf-8").read()
            def sub(m):
                nonlocal changed
                if exists(m.group(2) + ".png"):
                    changed += 1
                    return f'{m.group(1)}{m.group(2)}.webp{m.group(1)}'
                return m.group(0)
            open(p, "w", encoding="utf-8").write(pat.sub(sub, s))
    print(f"webp: {len(pngs)} images converted, {changed} paths rewritten")


if __name__ == "__main__":
    main()
