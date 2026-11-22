import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cutout


class CutoutTest(unittest.TestCase):
    def test_removes_border_background_keeps_subject_and_enclosed(self):
        w = h = 20
        bg, red, hole = (230, 230, 230), (200, 30, 30), (232, 232, 232)
        rows = []
        for y in range(h):
            row = []
            for x in range(w):
                if 5 <= x < 15 and 5 <= y < 15:
                    row.append(hole if (9 <= x < 11 and 9 <= y < 11) else red)
                else:
                    row.append(bg)
            rows.append(row)
        d = Path(tempfile.mkdtemp())
        cutout.write_png(d / "in.png", w, h, [bytes(v for p in r for v in (*p, 255)) for r in rows])
        cutout.cutout(d / "in.png", d / "out.png")
        _, _, px = cutout.read_png(d / "out.png")
        ow, oh, _ = cutout.read_png(d / "out.png")
        self.assertEqual((ow, oh), (w, h))
        raw = (d / "out.png").read_bytes()
        self.assertTrue(raw.startswith(b"\x89PNG"))
        # read alpha directly: read_png drops it, so decode through the same path with RGBA
        import zlib, struct
        pos, idat = 8, b""
        while pos < len(raw):
            n, t = struct.unpack(">I4s", raw[pos:pos + 8])
            if t == b"IDAT":
                idat += raw[pos + 8:pos + 8 + n]
            pos += 12 + n
        data = zlib.decompress(idat)
        stride = w * 4 + 1
        alpha = lambda x, y: data[y * stride + 1 + x * 4 + 3]
        self.assertEqual(alpha(0, 0), 0)        # background gone
        self.assertEqual(alpha(10, 7), 255)      # subject kept
        self.assertEqual(alpha(9, 9), 255)       # enclosed patch not connected to the border stays


    def test_gap_in_subject_cleared_but_bright_eye_white_kept(self):
        w = h = 40
        bg, dark, eye = (229, 228, 229), (20, 20, 20), (250, 250, 250)
        rows = [[bg] * w for _ in range(h)]
        for y in range(5, 35):
            for x in range(5, 35):
                rows[y][x] = dark
        for y in range(10, 15):          # a hair-like gap showing the real background colour
            for x in range(10, 15):
                rows[y][x] = bg
        for y in range(25, 30):          # an eye white: brighter than the background
            for x in range(25, 30):
                rows[y][x] = eye
        d = Path(tempfile.mkdtemp())
        cutout.write_png(d / "in.png", w, h, [bytes(v for p in r for v in (*p, 255)) for r in rows])
        cutout.cutout(d / "in.png", d / "out.png")
        import zlib, struct
        raw = (d / "out.png").read_bytes()
        pos, idat = 8, b""
        while pos < len(raw):
            n, t = struct.unpack(">I4s", raw[pos:pos + 8])
            if t == b"IDAT":
                idat += raw[pos + 8:pos + 8 + n]
            pos += 12 + n
        data = zlib.decompress(idat)
        alpha = lambda x, y: data[y * (w * 4 + 1) + 1 + x * 4 + 3]
        self.assertEqual(alpha(12, 12), 0)       # gap cleared
        self.assertEqual(alpha(27, 27), 255)     # eye white kept
        self.assertEqual(alpha(20, 20), 255)     # subject kept


if __name__ == "__main__":
    unittest.main()
