#!/usr/bin/env python3
"""Make the book cover (JPEG, RGB) from native-resolution cover art.

Needs Pillow (the only tool here that does; the cover is a one-off).
Usage: python3 tools/make_cover.py --art art/store/cover/cover_c.png --author "Name" --out publish/books/cover.jpg
Leave --author out for a cover with the title only. The art is used at its own size (no enlarging).
"""
import argparse
from PIL import Image, ImageDraw, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Georgia.ttf"
IVORY = (245, 239, 226)


def spaced(draw, w, y, text, font, fill, spacing):
    widths = [draw.textlength(c, font=font) for c in text]
    x = (w - (sum(widths) + spacing * (len(text) - 1))) / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + spacing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--author", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title-lines", nargs="+", default=["The Man the", "Tide Brought In"],
                    help="title split into lines (default: the English two lines)")
    ap.add_argument("--title-scale", type=float, default=0.085,
                    help="title font size as a fraction of the cover width (default 0.085)")
    a = ap.parse_args()

    img = Image.open(a.art).convert("RGBA")
    W, H = img.size
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = shade.load()
    for y in range(H):
        t = max(0.0, 1 - y / (H * 0.30)) ** 1.2 * 0.72
        b = max(0.0, (y - H * 0.88) / (H * 0.12)) ** 1.3 * 0.78 if a.author else 0.0
        al = int(255 * min(1.0, t + b))
        for x in range(W):
            px[x, y] = (4, 10, 18, al)
    img = Image.alpha_composite(img, shade).convert("RGB")

    d = ImageDraw.Draw(img)
    big = ImageFont.truetype(FONT, int(W * a.title_scale))
    for i, line in enumerate(a.title_lines):
        w = d.textlength(line, font=big)
        if w > W * 0.92:
            raise SystemExit(f"title line too wide ({int(w)} px): lower --title-scale")
        d.text(((W - w) / 2, H * 0.035 + i * W * 0.105), line, font=big, fill=IVORY,
               stroke_width=2, stroke_fill=(4, 10, 18))
    if a.author:
        f = ImageFont.truetype(FONT, int(W * 0.042))
        spaced(d, W, H * 0.945, a.author.upper(), f, IVORY, 9)
    img.save(a.out, "JPEG", quality=92, subsampling=0, dpi=(300, 300))
    print(a.out, img.size)


if __name__ == "__main__":
    main()
