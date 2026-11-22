"""The cutting review app: a local web server for the owner to review suggested cuts.

Standard library only. Serves one page (tools/cutter.html) and a small JSON API.
Writes only work/cuts/chNN.decisions.json (via the owner's clicks) and, on
approval, the files that apply_chapter writes.
"""
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import vnlib as L

PAGE = Path(__file__).resolve().parent / "cutter.html"
LOCK = threading.Lock()
STATES = ("keep", "cut", "edit")


class ApiError(Exception):
    def __init__(self, msg, code=400):
        super().__init__(msg)
        self.code = code


def _chapter(n):
    ch = L.read_json(L.units_path(n))
    if ch is None:
        raise ApiError("no such chapter: %s (run ./vn split)" % n, 404)
    return ch


def list_chapters():
    out = []
    for n in L.chapter_numbers():
        s = L.chapter_stats(n)
        _, problems = L.load_suggestions(n, _chapter(n))
        s["problems"] = len(problems)
        s["state"] = ("stale" if s["stale"] else "approved" if s["approved"]
                      else "review" if s["has_suggestions"] else "none")
        out.append(s)
    return out


def get_chapter(n):
    ch = _chapter(n)
    sugg, problems = L.load_suggestions(n, ch)
    dec = L.read_json(L.decisions_path(n), {})
    return {"chapter": ch, "suggestions": sugg, "problems": problems,
            "decisions": dec.get("decisions", {}), "approved": bool(dec.get("approved")),
            "note": dec.get("note", ""), "stats": L.chapter_stats(n)}


def _load_dec(n, ch):
    dec = L.read_json(L.decisions_path(n)) or {}
    dec.setdefault("chapter", n)
    dec.setdefault("approved", False)
    dec.setdefault("source_sha", None)
    dec.setdefault("note", "")
    dec.setdefault("decisions", {})
    return dec


def _expand(ch, ident):
    ids = {s["id"] for _, _, s in L.iter_sents(ch)}
    if ident in ids:
        return [ident]
    for sc in ch["scenes"]:
        for p in sc["paras"]:
            if p["id"] == ident:
                return [s["id"] for s in p["sents"]]
    raise ApiError("no such sentence: %s" % ident, 404)


def decide(n, ident, state=None, text=None, note=None, reset=False):
    """Record the owner's choice for a sentence or a whole paragraph."""
    ch = _chapter(n)
    dec = _load_dec(n, ch)
    if dec["approved"]:
        raise ApiError("chapter is approved; reopen it first", 409)
    targets = _expand(ch, ident)
    for sid in targets:
        if reset:
            dec["decisions"].pop(sid, None)
            continue
        if state not in STATES:
            raise ApiError("state must be keep, cut or edit")
        entry = {"state": state}
        if state == "edit":
            if not (text or "").strip():
                raise ApiError("edit needs text")
            if len(targets) > 1:
                raise ApiError("edit one sentence at a time")
            entry["text"] = text.strip()
        old_note = dec["decisions"].get(sid, {}).get("note")
        if note is not None:
            if note.strip():
                entry["note"] = note.strip()
        elif old_note:
            entry["note"] = old_note
        dec["decisions"][sid] = entry
    L.write_json(L.decisions_path(n), dec)
    return get_chapter(n)


def set_note(n, note):
    ch = _chapter(n)
    dec = _load_dec(n, ch)
    dec["note"] = note
    L.write_json(L.decisions_path(n), dec)
    return get_chapter(n)


def approve(n):
    ch = _chapter(n)
    _, problems = L.load_suggestions(n, ch)
    if problems:
        raise ApiError("the suggestions file has problems; fix it first: " + "; ".join(problems[:3]), 409)
    dec = _load_dec(n, ch)
    dec["approved"] = True
    dec["source_sha"] = ch.get("source_sha")
    L.write_json(L.decisions_path(n), dec)
    L.apply_chapter(n)
    return get_chapter(n)


def reopen(n):
    ch = _chapter(n)
    dec = _load_dec(n, ch)
    dec["approved"] = False
    L.write_json(L.decisions_path(n), dec)
    return get_chapter(n)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _guard(self, fn):
        try:
            with LOCK:
                self._send(200, fn())
        except ApiError as e:
            self._send(e.code, {"error": str(e)})
        except Exception as e:  # report, never hide
            self._send(500, {"error": "%s: %s" % (type(e).__name__, e)})

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/":
            self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif path == "/api/chapters":
            self._guard(list_chapters)
        elif path.startswith("/api/chapter/"):
            try:
                n = int(path.rsplit("/", 1)[1])
            except ValueError:
                return self._send(404, {"error": "bad chapter"})
            self._guard(lambda: get_chapter(n))
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.headers.get("Origin") and "127.0.0.1" not in self.headers["Origin"] \
                and "localhost" not in self.headers["Origin"]:
            return self._send(403, {"error": "forbidden"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0)) or 0) or b"{}")
            n = int(body["chapter"])
        except (ValueError, KeyError, TypeError):
            return self._send(400, {"error": "bad request"})
        path = self.path.split("?")[0]
        if path == "/api/decide":
            self._guard(lambda: decide(n, body.get("id", ""), body.get("state"), body.get("text"),
                                       body.get("note"), bool(body.get("reset"))))
        elif path == "/api/note":
            self._guard(lambda: set_note(n, str(body.get("note", ""))))
        elif path == "/api/approve":
            self._guard(lambda: approve(n))
        elif path == "/api/reopen":
            self._guard(lambda: reopen(n))
        else:
            self._send(404, {"error": "not found"})


def make_server(port=8765):
    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def serve(port=8765):
    srv = make_server(port)
    print("Cutting app: http://127.0.0.1:%d   (Ctrl-C to stop)" % port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print()
