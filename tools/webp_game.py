#!/usr/bin/env python3
"""Make a WebP copy of the Ren'Py project for the iOS build.

usage: webp_game.py SRC_PROJECT DEST_PROJECT [--quality 80] [--scale 0.75]

Copies SRC_PROJECT (the folder that holds game/) to DEST_PROJECT, converts every
PNG under game/images to WebP with cwebp (quality 80), shrinks big images to 75% of
their size, and rewrites the .png paths in the copied .rpy files. A shrunk image is
named name@0.7500.webp: Ren'Py reads the @ factor and still draws it at full size. The source project is never touched. Standard library only;
needs the `cwebp` command (brew install webp).
"""
import argparse, os, re, shutil, struct, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

SKIP = shutil.ignore_patterns("cache", "saves", "*.rpyc", "*.rpymc", "*.bak", "*.rpy-E", "__pycache__", ".DS_Store")


def png_size(path):
    with open(path, "rb") as f:
        d = f.read(24)
    return struct.unpack(">II", d[16:24])


def convert(png, quality, scale, min_side):
    """Convert one PNG. Returns (png_path, new_webp_path)."""
    w, h = png_size(png)
    args = ["cwebp", "-quiet", "-q", str(quality), "-alpha_q", "100", "-m", "6"]
    base = png[:-4]
    if scale < 1 and max(w, h) >= min_side:
        nw, nh = round(w * scale), round(h * scale)
        args += ["-resize", str(nw), str(nh)]
        base += "@%.4f" % (nw / w)
    out = base + ".webp"
    subprocess.run(args + [png, "-o", out], check=True)
    os.remove(png)
    return png, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dest")
    ap.add_argument("--quality", type=int, default=80)
    ap.add_argument("--scale", type=float, default=0.75)
    ap.add_argument("--min-side", type=int, default=800, help="only shrink images at least this big")
    a = ap.parse_args()
    if shutil.which("cwebp") is None:
        sys.exit("cwebp not found (brew install webp)")
    if os.path.exists(a.dest):
        shutil.rmtree(a.dest)
    shutil.copytree(a.src, a.dest, ignore=SKIP)
    game = os.path.join(a.dest, "game")
    pngs = [os.path.join(d, f) for d, _, fs in os.walk(os.path.join(game, "images")) for f in fs if f.endswith(".png")]
    with ThreadPoolExecutor(os.cpu_count() or 4) as ex:
        results = list(ex.map(lambda p: convert(p, a.quality, a.scale, a.min_side), pngs))
    # key: path relative to game/ without extension -> new file name (no directory)
    converted = {os.path.relpath(old, game)[:-4]: os.path.basename(new)[:-5] for old, new in results}

    def lookup(ref):
        # Ren'Py looks in game/ and, for images, in game/images/
        for base in ("", "images/"):
            key = os.path.normpath(base + ref)
            if key in converted:
                return converted[key]
        return None

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
                new = lookup(m.group(2))
                if new is not None:
                    changed += 1
                    folder = os.path.dirname(m.group(2))
                    ref = (folder + "/" if folder else "") + new
                    return f'{m.group(1)}{ref}.webp{m.group(1)}'
                return m.group(0)
            open(p, "w", encoding="utf-8").write(pat.sub(sub, s))
    print(f"webp: {len(pngs)} images converted, {changed} paths rewritten")


if __name__ == "__main__":
    main()
