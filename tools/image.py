"""./vn image and ./vn spend: the only way agents generate images.

Every call is priced before it is made, refused if it would pass the cap, and
logged in work/ledger.jsonl afterwards. The key is never printed or logged.
"""
import argparse
import base64
import hashlib
import json
import mimetypes
import os
import re
import struct
import sys
import urllib.error
import urllib.request
from pathlib import Path

import vnlib as L

KEY_NAMES = ("FAL_KEY", "FAL_API_KEY", "FAL")
PURPOSES = ("bakeoff", "sheet", "background", "sprite", "illustration")
CONFIG = L.ROOT / "config"
LEDGER = L.WORK / "ledger.jsonl"


class ImageError(Exception):
    billed = True  # a failure may still have been charged, unless fal rejected the request outright


# ---- key -------------------------------------------------------------------

def find_key():
    for name in KEY_NAMES:
        if os.environ.get(name):
            return os.environ[name].strip()
    local = L.read_json(CONFIG / "local.json", {}) or {}
    path = local.get("fal_env_file")
    if path and Path(path).exists():
        for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\s*(?:export\s+)?([A-Za-z_0-9]+)\s*=\s*(.*?)\s*$", line)
            if m and m.group(1) in KEY_NAMES:
                v = m.group(2).strip("'\"")
                if v:
                    return v
    raise ImageError("No fal.ai key found. Set FAL_KEY in the environment, or put the path of an env file "
                     "that defines FAL_KEY, FAL_API_KEY or FAL in config/local.json as fal_env_file.")


# ---- money -----------------------------------------------------------------

def read_ledger(ledger=None):
    ledger = Path(ledger or LEDGER)
    rows = []
    if ledger.exists():
        for line in ledger.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


def budget():
    return L.read_json(CONFIG / "budget.json", {}) or {}


def spent(rows=None):
    rows = read_ledger() if rows is None else rows
    total, by_purpose, by_model = 0.0, {}, {}
    for r in rows:
        c = float(r.get("cost", 0))
        total += c
        by_purpose[r.get("purpose")] = by_purpose.get(r.get("purpose"), 0) + c
        by_model[r.get("model")] = by_model.get(r.get("model"), 0) + c
    return total, by_purpose, by_model


def estimate_cost(model, width, height, n_refs):
    """A cost that is never below the real one: inputs are billed at up to 1 MP each."""
    p = model["price"]
    if "per_image" in p:
        return round(p["per_image"], 6)
    out_mp = -(-width * height // 1048576)  # round up; fal counts 1024x1024 as one megapixel
    return round(p["per_megapixel"] * (max(1, out_mp) + n_refs), 6)


def check_cap(cost, purpose):
    b = budget()
    total, by_purpose, _ = spent()
    cap = b.get("total_cap")
    if cap is not None and total + cost > cap + 1e-9:
        raise ImageError("Refused: this would bring total spending to %.2f, over the cap of %s." % (total + cost, cap))
    pcap = (b.get("purpose_caps") or {}).get(purpose)
    if pcap is not None and by_purpose.get(purpose, 0) + cost > pcap + 1e-9:
        raise ImageError("Refused: this would bring '%s' spending to %.2f, over its cap of %s."
                         % (purpose, by_purpose.get(purpose, 0) + cost, pcap))
    return total + cost, cap


# ---- network (replaced in tests) ----------------------------------------------

def _http(req, timeout=300):
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        err = ImageError("fal returned HTTP %d: %s" % (e.code, e.read()[:400].decode("utf-8", "replace")))
        err.billed = e.code not in (400, 401, 403, 404, 422)  # rejected before any work
        raise err
    except urllib.error.URLError as e:
        raise ImageError("network error: %s" % e.reason)


def call_fal(model_id, payload, key):
    req = urllib.request.Request("https://fal.run/" + model_id, data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Key " + key, "Content-Type": "application/json",
                                          "User-Agent": "vn-image/1"})
    return json.loads(_http(req))


def download(url):
    if url.startswith("data:"):
        return base64.b64decode(url.split(",", 1)[1])
    return _http(urllib.request.Request(url, headers={"User-Agent": "vn-image/1"}))


# ---- the command -----------------------------------------------------------

def data_uri(path):
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    return "data:%s;base64,%s" % (mime, base64.b64encode(Path(path).read_bytes()).decode())


def parse_size(s):
    m = re.match(r"^(\d+)x(\d+)$", s or "")
    if not m:
        raise ImageError("--size must look like 1024x1024")
    return int(m.group(1)), int(m.group(2))


def generate(model_name, prompt, refs, out, purpose, chapter=None, size=(1024, 1024), aspect="1:1",
             dry_run=False, models=None):
    models = models or L.read_json(CONFIG / "models.json")
    models = {k: v for k, v in models.items() if not k.startswith("_")}
    if model_name not in models:
        raise ImageError("Unknown model '%s'. Known: %s" % (model_name, ", ".join(models)))
    if purpose not in PURPOSES:
        raise ImageError("purpose must be one of: " + ", ".join(PURPOSES))
    m = models[model_name]
    if len(refs) > m["max_refs"]:
        raise ImageError("%s takes at most %d reference images" % (model_name, m["max_refs"]))
    for r in refs:
        if not Path(r).exists():
            raise ImageError("reference image not found: %s" % r)
    w, h = size
    if m["size"] == "image_size" and m.get("min_pixels") and w * h < m["min_pixels"]:
        raise ImageError("%s needs at least %d pixels in total; use --size, for example 2560x1440"
                         % (model_name, m["min_pixels"]))
    cost = estimate_cost(m, w, h, len(refs))
    new_total, cap = check_cap(cost, purpose)
    payload = dict(m.get("extra", {}))
    payload["prompt"] = prompt
    if m["refs_field"]:
        payload[m["refs_field"]] = [data_uri(r) for r in refs]
    if m["size"] == "image_size":
        payload["image_size"] = {"width": w, "height": h}
    else:
        payload["aspect_ratio"] = aspect
    if m["refs_field"] and not refs:
        raise ImageError("%s is an edit model: give at least one reference image with --ref." % model_name)
    out = Path(out)
    phash = hashlib.sha256(prompt.encode()).hexdigest()[:16]
    if dry_run:
        return {"dry_run": True, "model": m["id"], "cost": cost, "total_after": new_total, "cap": cap,
                "payload_keys": sorted(payload), "refs": len(refs)}
    key = find_key()
    row = {"time": L.now(), "model": model_name, "model_id": m["id"], "purpose": purpose, "chapter": chapter,
           "cost": cost, "out": str(out), "prompt_hash": phash, "ok": False}
    try:
        resp = call_fal(m["id"], payload, key)
        images = resp.get("images") or []
        if not images or not images[0].get("url"):
            raise ImageError("fal answered but sent no image")
        data = download(images[0]["url"])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        out.with_suffix(".txt").write_text(
            "model: %s\npurpose: %s\nrefs: %s\n\n%s\n" % (m["id"], purpose, ", ".join(map(str, refs)), prompt),
            encoding="utf-8")
        row["ok"] = True
    except ImageError as e:
        row["error"] = str(e).replace(key, "***")[:300]
        if not e.billed:
            row["cost"] = 0.0
        _append(row)
        raise
    _append(row)
    row["warn"] = bool(cap and new_total >= budget().get("warn_at", 0.8) * cap)
    return row


def _append(row):
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def cmd_image(argv):
    ap = argparse.ArgumentParser(prog="./vn image", description="Generate one image through fal.ai, logged and capped.")
    ap.add_argument("model")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt")
    g.add_argument("--prompt-file")
    ap.add_argument("--ref", action="append", default=[], help="reference image; repeat for more")
    ap.add_argument("--out", required=True)
    ap.add_argument("--purpose", required=True, choices=PURPOSES)
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--size", default="1024x1024", help="WxH, for models that take a size")
    ap.add_argument("--aspect", default="1:1", help="for models that take an aspect ratio, e.g. 16:9")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    prompt = a.prompt if a.prompt is not None else Path(a.prompt_file).read_text(encoding="utf-8").strip()
    try:
        r = generate(a.model, prompt, a.ref, a.out, a.purpose, a.chapter, parse_size(a.size), a.aspect, a.dry_run)
    except ImageError as e:
        print(str(e), file=sys.stderr)
        return 1
    if r.get("dry_run"):
        print("dry run: %s, would cost $%.4f (total after: $%.2f of $%s), %d refs, fields %s"
              % (r["model"], r["cost"], r["total_after"], r["cap"], r["refs"], ",".join(r["payload_keys"])))
    else:
        print("saved %s  cost $%.4f" % (r["out"], r["cost"]))
        if r.get("warn"):
            print("WARNING: 80%% of the budget is spent. Tell the owner.")
    return 0


def cmd_spend():
    total, by_p, by_m = spent()
    b = budget()
    print("Spent $%.2f of $%s" % (total, b.get("total_cap")))
    for title, d in (("by purpose", by_p), ("by model", by_m)):
        print(title)
        for k, v in sorted(d.items(), key=lambda kv: -kv[1]):
            cap = (b.get("purpose_caps") or {}).get(k) if title == "by purpose" else None
            print("  %-14s $%.2f%s" % (k, v, "  (cap $%s)" % cap if cap is not None else ""))
    print("Left: $%.2f" % ((b.get("total_cap") or 0) - total))
