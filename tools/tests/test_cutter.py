import json, sys, tempfile, threading, unittest, urllib.request, urllib.error
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vnlib as L
import cutter

NOVEL = """# Title

# Part One

## Chapter 1. Wrack

The tide came in. It brought a man. He was cold.

The man spoke. "Hello there." He sat.
"""


class CutterTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (L.SOURCE, L.WORK, L.UNITS, L.CUTS, L.CUT_TEXT)
        L.SOURCE = self.tmp / "novel.md"
        L.SOURCE.write_text(NOVEL, encoding="utf-8")
        L.WORK = self.tmp / "work"
        L.UNITS, L.CUTS, L.CUT_TEXT = L.WORK / "units", L.WORK / "cuts", L.WORK / "cut"
        ch = L.split_novel(NOVEL)[0]
        ch["source_sha"] = L.source_sha()
        L.write_json(L.units_path(1), ch)
        self.ids = [s["id"] for _, _, s in L.iter_sents(ch)]
        self.srv = cutter.make_server(0)
        self.port = self.srv.server_address[1]
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()

    def tearDown(self):
        self.srv.shutdown()
        self.srv.server_close()
        L.SOURCE, L.WORK, L.UNITS, L.CUTS, L.CUT_TEXT = self.saved

    def call(self, path, body=None):
        req = urllib.request.Request("http://127.0.0.1:%d%s" % (self.port, path),
                                     data=None if body is None else json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read())

    def suggest(self, items):
        L.write_json(L.suggestions_path(1), {"chapter": 1, "items": items})

    def test_page_served(self):
        with urllib.request.urlopen("http://127.0.0.1:%d/" % self.port) as r:
            self.assertIn(b"Cutting app", r.read())

    def test_load_decide_approve_reopen(self):
        self.suggest([{"id": self.ids[1], "action": "cut", "kind": "pace", "reason": "r"}])
        _, lst = self.call("/api/chapters")
        self.assertEqual(lst[0]["state"], "review")
        _, d = self.call("/api/chapter/1")
        self.assertIn(self.ids[1], d["suggestions"])
        # owner overrules
        _, d = self.call("/api/decide", {"chapter": 1, "id": self.ids[1], "state": "keep", "note": "keep it"})
        self.assertEqual(d["decisions"][self.ids[1]]["note"], "keep it")
        self.call("/api/decide", {"chapter": 1, "id": self.ids[2], "state": "cut"})
        self.call("/api/decide", {"chapter": 1, "id": self.ids[0], "state": "edit", "text": "The tide rose."})
        # reload loses nothing
        _, d = self.call("/api/chapter/1")
        self.assertEqual(len(d["decisions"]), 3)
        code, d = self.call("/api/approve", {"chapter": 1})
        self.assertEqual(code, 200)
        self.assertTrue(d["approved"])
        text = L.cut_text_path(1).read_text()
        self.assertIn("The tide rose.", text)
        self.assertIn("It brought a man.", text)
        self.assertNotIn("He was cold.", text)
        self.assertEqual(L.read_json(L.review_path(1))["overruled"][0]["id"], self.ids[1])
        self.assertEqual(L.read_json(L.decisions_path(1))["source_sha"], L.source_sha())
        code, _ = self.call("/api/decide", {"chapter": 1, "id": self.ids[0], "state": "cut"})
        self.assertEqual(code, 409)
        _, d = self.call("/api/reopen", {"chapter": 1})
        self.assertFalse(d["approved"])

    def test_paragraph_and_reset(self):
        pid = ".".join(self.ids[0].split(".")[:3])
        _, d = self.call("/api/decide", {"chapter": 1, "id": pid, "state": "cut"})
        self.assertEqual(len(d["decisions"]), 3)
        _, d = self.call("/api/decide", {"chapter": 1, "id": pid, "reset": True})
        self.assertEqual(d["decisions"], {})

    def test_bad_input(self):
        self.assertEqual(self.call("/api/decide", {"chapter": 1, "id": "nope", "state": "cut"})[0], 404)
        self.assertEqual(self.call("/api/decide", {"chapter": 1, "id": self.ids[0], "state": "zzz"})[0], 400)
        self.assertEqual(self.call("/api/decide", {"chapter": 1, "id": self.ids[0], "state": "edit", "text": " "})[0], 400)
        self.assertEqual(self.call("/api/chapter/9")[0], 404)

    def test_malformed_suggestions_reported_not_dropped(self):
        self.suggest([{"id": "c01.s09.p001.1", "action": "cut", "kind": "pace", "reason": "r"},
                      {"id": self.ids[0], "action": "cut", "kind": "bogus", "reason": "r"}])
        _, d = self.call("/api/chapter/1")
        self.assertEqual(len(d["problems"]), 2)
        _, lst = self.call("/api/chapters")
        self.assertEqual(lst[0]["problems"], 2)
        code, d = self.call("/api/approve", {"chapter": 1})
        self.assertEqual(code, 409)


if __name__ == "__main__":
    unittest.main()
