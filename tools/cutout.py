"""Remove a flat or softly shaded light background from a character image.

Standard library only. Reads an 8-bit RGB or RGBA PNG, makes transparent every
pixel that is close to the border colour and connected to the border, softens
the edge, and writes an RGBA PNG. Usage: cutout.py in.png out.png [tolerance]
"""
import struct
import sys
import zlib
from collections import deque


def read_png(path):
    data = open(path, "rb").read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    pos, idat, w = 8, b"", None
    while pos < len(data):
        n, typ = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + n]
        pos += 12 + n
        if typ == b"IHDR":
            w, h, depth, ctype, _, _, inter = struct.unpack(">IIBBBBB", body)
            assert depth == 8 and ctype in (2, 6) and inter == 0, "need 8-bit RGB/RGBA, not interlaced"
        elif typ == b"IDAT":
            idat += body
    bpp = 3 if ctype == 2 else 4
    raw = zlib.decompress(idat)
    stride = w * bpp
    rows, prev = [], bytearray(stride)
    p = 0
    for _ in range(h):
        f = raw[p]
        line = bytearray(raw[p + 1:p + 1 + stride])
        p += 1 + stride
        if f == 1:
            for i in range(bpp, stride):
                line[i] = (line[i] + line[i - bpp]) & 255
        elif f == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                b = prev[i]
                c = prev[i - bpp] if i >= bpp else 0
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if pa <= pb and pa <= pc else b if pb <= pc else c
                line[i] = (line[i] + pr) & 255
        rows.append(line)
        prev = line
    px = [[(r[i], r[i + 1], r[i + 2]) for i in range(0, stride, bpp)] for r in rows]
    return w, h, px


def write_png(path, w, h, rgba_rows):
    raw = b"".join(b"\x00" + bytes(r) for r in rgba_rows)

    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def _clear_enclosed_gaps(px, gone, w, h, tol):
    """Also clear background seen through gaps (between hair strands, inside nets).

    A gap counts only if its mean colour matches the real background and is grey
    (eye whites are brighter, skin highlights are warm), so faces keep their eyes.
    """
    n = sr = sg = sb = 0
    for y in range(0, h, 4):
        for x in range(0, w, 4):
            if gone[y][x]:
                r, g, b = px[y][x]
                n, sr, sg, sb = n + 1, sr + r, sg + g, sb + b
    if not n:
        return
    bg = (sr / n, sg / n, sb / n)

    def near(c):
        return max(abs(c[0] - bg[0]), abs(c[1] - bg[1]), abs(c[2] - bg[2])) <= 14
    seen = [[False] * w for _ in range(h)]
    for y0 in range(h):
        for x0 in range(w):
            if gone[y0][x0] or seen[y0][x0] or not near(px[y0][x0]):
                continue
            q, pts = deque([(x0, y0)]), []
            seen[y0][x0] = True
            while q:
                x, y = q.popleft()
                pts.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    u, v = x + dx, y + dy
                    if 0 <= u < w and 0 <= v < h and not seen[v][u] and not gone[v][u] and near(px[v][u]):
                        seen[v][u] = True
                        q.append((u, v))
            if len(pts) < 6:
                continue
            m = [sum(px[y][x][i] for x, y in pts) / len(pts) for i in range(3)]
            grey = max(m) - min(m) <= 6
            close = max(abs(m[i] - bg[i]) for i in range(3)) <= 8
            if grey and close:
                for x, y in pts:
                    gone[y][x] = True


def cutout(src, dst, tol=28):
    w, h, px = read_png(src)
    border = [px[0][0], px[0][w - 1], px[0][w // 2], px[h // 2][0], px[h // 2][w - 1]]
    bg = tuple(sorted(c[i] for c in border)[len(border) // 2] for i in range(3))

    def near(c):
        return max(abs(c[0] - bg[0]), abs(c[1] - bg[1]), abs(c[2] - bg[2])) <= tol
    gone = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        q += [(x, 0), (x, h - 1)]
    for y in range(h):
        q += [(0, y), (w - 1, y)]
    while q:
        x, y = q.popleft()
        if 0 <= x < w and 0 <= y < h and not gone[y][x] and near(px[y][x]):
            gone[y][x] = True
            q += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    _clear_enclosed_gaps(px, gone, w, h, tol)
    out = []
    for y in range(h):
        row = bytearray()
        for x in range(w):
            r, g, b = px[y][x]
            a = 0 if gone[y][x] else 255
            if a:  # soften: pixels touching background get partial alpha
                touch = sum(1 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                            if 0 <= x + dx < w and 0 <= y + dy < h and gone[y + dy][x + dx])
                a = 255 - 55 * touch
            row += bytes((r, g, b, a))
        out.append(row)
    write_png(dst, w, h, out)
    return bg


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    print("background", cutout(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 28))
