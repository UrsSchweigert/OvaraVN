import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vnlib as L
import check


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (L.WORK, L.UNITS, L.CUTS)
        L.WORK = self.tmp
        L.UNITS, L.CUTS = L.WORK / "units", L.WORK / "cuts"
        self.ch = {"chapter": 1, "title": "T", "part": "One", "source_sha": "x",
                   "scenes": [{"id": "c01.s01", "paras": [{"id": "c01.s01.p001", "sents": [{"id": "c01.s01.p001.1", "text": "Hi."}]}]}]}
        L.write_json(L.units_path(1), self.ch)

    def tearDown(self):
        L.WORK, L.UNITS, L.CUTS = self.saved

    def test_manifest_missing_field_and_unknown_cast(self):
        L.write_json(L.WORK / "manifest" / "ch01.json", {"scenes": [{"id": "c01.s01", "place": "p", "time": "t", "cast": ["Zed"], "mood": "m"}]})
        L.write_json(L.WORK / "manifest" / "cast.json", ["Wrack"])
        errs = []
        check.check_manifests(errs)
        self.assertTrue(any("no key_moment" in e for e in errs))
        self.assertTrue(any("'Zed'" in e for e in errs))

    def test_manifest_null_time_and_key_moment_allowed_but_not_missing(self):
        sc = {"id": "c01.s01", "place": "p", "time": None, "cast": ["Wrack"], "mood": "m", "key_moment": None}
        L.write_json(L.WORK / "manifest" / "ch01.json", {"scenes": [sc]})
        errs = []
        check.check_manifests(errs)
        self.assertEqual(errs, [])
        del sc["time"]
        L.write_json(L.WORK / "manifest" / "ch01.json", {"scenes": [sc]})
        check.check_manifests(errs)
        self.assertTrue(any("no time" in e for e in errs))

    def test_manifest_ok(self):
        L.write_json(L.WORK / "manifest" / "ch01.json", {"scenes": [{"id": "c01.s01", "place": "p", "time": "t", "cast": ["Wrack"], "mood": "m", "key_moment": "k"}]})
        L.write_json(L.WORK / "manifest" / "cast.json", ["Wrack"])
        errs = []
        check.check_manifests(errs)
        self.assertEqual(errs, [])

    def test_bad_suggestions_named(self):
        L.write_json(L.suggestions_path(1), {"items": [{"id": "nope", "action": "cut", "reason": "r"}]})
        errs = []
        check.check_cuts(errs)
        self.assertTrue(errs and "ch01.suggestions.json" in errs[0])

    def test_stale_approval(self):
        L.write_json(L.decisions_path(1), {"approved": True, "source_sha": "old"})
        errs = []
        check.check_cuts(errs)
        self.assertTrue(any("older novel" in e for e in errs))

    def test_ledger_over_cap(self):
        (L.WORK / "ledger.jsonl").write_text('{"cost": 999}\n')
        errs = []
        check.check_ledger(errs)
        self.assertTrue(errs)


if __name__ == "__main__":
    unittest.main()
