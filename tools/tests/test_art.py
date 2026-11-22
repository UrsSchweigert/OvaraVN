import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import art


def project():
    r = Path(tempfile.mkdtemp())
    (r / "game/game/images/bg").mkdir(parents=True)
    (r / "game/game/images/cg").mkdir(parents=True)
    (r / "art/refs/ch01/portraits").mkdir(parents=True)
    (r / "art/refs/ch01/places").mkdir(parents=True)
    (r / "work").mkdir()
    for f in ("game/game/images/p_sefa_wary.png", "game/game/images/bg/kelp.png", "art/refs/ch01/portraits/sefa.png",
              "art/refs/ch01/places/kelp.png"):
        (r / f).write_bytes(b"x")
    (r / "art/refs/ch01/portraits/sefa.txt").write_text("model: m\n\nA girl.\n")
    (r / "game/game/images.rpy").write_text(
        'image p sefa_wary = At("p_sefa_wary.png", lit_portrait)\nimage bg kelp = Transform("bg/kelp.png", size=(1,1))\n')
    (r / "game/game/ch01.rpy").write_text("label ch01:\n    scene bg kelp\n    show p sefa_wary as right\n    show p sefa_wary as right\n")
    (r / "work/ledger.jsonl").write_text(json.dumps({"ok": True, "out": str(r / "art/refs/ch01/portraits/sefa.png"), "model": "flux-2", "cost": 0.024}) + "\n")
    (r / "art/canon.json").write_text(json.dumps({"characters": {"Sefa": {"fixed": "girl", "references": ["art/refs/ch01/portraits/sefa.png"]}}}))
    return r


class ArtTest(unittest.TestCase):
    def test_registrations_usage_and_index(self):
        r = project()
        regs = art.parse_registrations(r)
        self.assertEqual(regs["p"], {"sefa_wary": "p_sefa_wary.png"})
        self.assertEqual(art.scan_usage(r)["p"]["sefa_wary"], {1: 2})
        idx = art.build_index(r)
        p = [i for i in idx["items"] if i["id"] == "p sefa_wary"][0]
        self.assertEqual(p["character"], "Sefa")
        self.assertEqual(p["model"], "flux-2")
        self.assertEqual(p["chapters"], {"1": 2})
        self.assertIn("A girl.", p["prompt"])
        self.assertEqual(art.check(idx, r), [])

    def test_check_finds_problems(self):
        r = project()
        (r / "game/game/images/p_sefa_wary.png").unlink()
        (r / "game/game/ch01.rpy").write_text("label ch01:\n    show p ghost_smile as left\n")
        (r / "art/canon.json").write_text(json.dumps({"characters": {}}))
        errs = art.check(art.build_index(r), r)
        text = "\n".join(errs)
        self.assertIn("game file missing", text)
        self.assertIn("p ghost_smile", text)
        self.assertIn("no entry in art/canon.json", text)

    def test_gallery_is_written(self):
        r = project()
        art.write_index(r)
        page = (r / "art/index.html").read_text()
        self.assertIn("p sefa_wary", page)
        self.assertTrue((r / "art/index.json").exists())


if __name__ == "__main__":
    unittest.main()
