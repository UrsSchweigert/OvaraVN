import json, os, sys, tempfile, unittest, zlib, struct
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vnlib as L
import image

SECRET = "sk-test-SECRET-123"


def tiny_png(path):
    raw = b"\x00\xff\x00\x00"
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
                           + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class ImageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (image.LEDGER, image.CONFIG, image.call_fal, image.download, dict(os.environ))
        image.LEDGER = self.tmp / "ledger.jsonl"
        image.CONFIG = self.tmp / "config"
        L.write_json(image.CONFIG / "budget.json", {"total_cap": 1.0, "purpose_caps": {"bakeoff": 0.1}, "warn_at": 0.8})
        L.write_json(image.CONFIG / "models.json", {"m": {"id": "x/y", "price": {"per_image": 0.04}, "refs_field": "image_urls",
                                                         "max_refs": 2, "size": "aspect_ratio", "extra": {}},
                                                   "mp": {"id": "x/mp", "price": {"per_megapixel": 0.01}, "refs_field": "image_urls",
                                                          "max_refs": 2, "size": "image_size", "extra": {}}})
        for k in image.KEY_NAMES:
            os.environ.pop(k, None)
        os.environ["FAL"] = SECRET
        self.ref = self.tmp / "ref.png"
        tiny_png(self.ref)
        self.calls = []
        image.call_fal = lambda mid, payload, key: (self.calls.append((mid, payload, key)) or {"images": [{"url": "http://x/i.png"}]})
        image.download = lambda url: b"PNGDATA"

    def tearDown(self):
        image.LEDGER, image.CONFIG, image.call_fal, image.download, env = self.saved
        os.environ.clear(); os.environ.update(env)

    def gen(self, **kw):
        a = dict(model_name="m", prompt="a hat", refs=[str(self.ref)], out=str(self.tmp / "o" / "a.png"), purpose="bakeoff")
        a.update(kw)
        return image.generate(**a)

    def test_writes_image_prompt_and_ledger(self):
        r = self.gen()
        self.assertTrue(r["ok"])
        self.assertEqual((self.tmp / "o" / "a.png").read_bytes(), b"PNGDATA")
        self.assertIn("a hat", (self.tmp / "o" / "a.txt").read_text())
        rows = image.read_ledger()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["cost"], 0.04)
        self.assertEqual(rows[0]["purpose"], "bakeoff")
        self.assertTrue(self.calls[0][1]["image_urls"][0].startswith("data:image/png;base64,"))

    def test_purpose_cap_refuses_and_does_not_call(self):
        self.gen(); self.gen()
        with self.assertRaises(image.ImageError) as e:
            self.gen()
        self.assertIn("bakeoff", str(e.exception))
        self.assertEqual(len(self.calls), 2)

    def test_total_cap_refuses(self):
        L.write_json(image.CONFIG / "budget.json", {"total_cap": 0.05})
        self.gen(purpose="sheet")
        with self.assertRaises(image.ImageError):
            self.gen(purpose="sheet")

    def test_missing_key_message_has_no_key(self):
        os.environ.pop("FAL")
        with self.assertRaises(image.ImageError) as e:
            self.gen()
        self.assertNotIn(SECRET, str(e.exception))
        self.assertIn("No fal.ai key", str(e.exception))

    def test_key_from_env_file(self):
        os.environ.pop("FAL")
        env = self.tmp / "e.env"
        env.write_text("OTHER=1\nFAL=%s\n" % SECRET)
        L.write_json(image.CONFIG / "local.json", {"fal_env_file": str(env)})
        self.assertEqual(image.find_key(), SECRET)

    def test_failure_logged_without_key(self):
        def boom(*a):
            raise image.ImageError("bad " + SECRET)
        image.call_fal = boom
        with self.assertRaises(image.ImageError):
            self.gen()
        row = image.read_ledger()[0]
        self.assertFalse(row["ok"])
        self.assertNotIn(SECRET, json.dumps(row))

    def test_dry_run_makes_no_call_and_no_ledger(self):
        r = self.gen(dry_run=True)
        self.assertTrue(r["dry_run"])
        self.assertEqual(self.calls, [])
        self.assertEqual(image.read_ledger(), [])

    def test_megapixel_estimate_counts_refs(self):
        m = {"price": {"per_megapixel": 0.01}}
        self.assertEqual(image.estimate_cost(m, 1024, 1024, 2), 0.03)

    def test_bad_inputs(self):
        for kw in ({"model_name": "nope"}, {"purpose": "x"}, {"refs": []}, {"refs": ["/no/such.png"]},
                   {"refs": [str(self.ref)] * 3}):
            with self.assertRaises(image.ImageError):
                self.gen(**kw)


if __name__ == "__main__":
    unittest.main()
