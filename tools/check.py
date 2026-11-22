"""./vn check: says whether the project is sound. Exits non-zero and names the file on any failure."""
import json
import subprocess
import sys
import tempfile
import filecmp
from pathlib import Path

import vnlib as L

EXPECT_CHAPTERS, EXPECT_WORDS = 18, 73618
MANIFEST_FIELDS = ("place", "time", "cast", "mood", "key_moment")
NULLABLE = ("time", "key_moment", "cast")  # must be present; null is a valid answer


def check_split(errs):
    chapters = L.split_novel(L.SOURCE.read_text(encoding="utf-8"))
    total = sum(L.words(s["text"]) for ch in chapters for _, _, s in L.iter_sents(ch))
    if len(chapters) != EXPECT_CHAPTERS or total != EXPECT_WORDS:
        errs.append("source/novel.md: split gives %d chapters and %d words; expected %d and %d"
                    % (len(chapters), total, EXPECT_CHAPTERS, EXPECT_WORDS))
    sha = L.source_sha()
    for ch in chapters:
        ch["source_sha"] = sha
        have = L.read_json(L.units_path(ch["chapter"]))
        if have != ch:
            errs.append("%s: differs from a fresh split; run ./vn split" % L.units_path(ch["chapter"]))
    return chapters


def merged_cast():
    for name in ("cast.json", "cast_list.json"):
        data = L.read_json(L.WORK / "manifest" / name)
        if data is not None:
            names = data.keys() if isinstance(data, dict) else data
            return {(n["name"] if isinstance(n, dict) else n) for n in names}
    return None


def check_cuts(errs):
    for n in L.chapter_numbers():
        ch = L.read_json(L.units_path(n))
        if L.suggestions_path(n).exists():
            try:
                _, problems = L.load_suggestions(n, ch)
            except (ValueError, OSError) as e:
                errs.append("%s: cannot be read: %s" % (L.suggestions_path(n), e))
                continue
            errs += ["%s: %s" % (L.suggestions_path(n), p) for p in problems]
        if L.decisions_path(n).exists():
            dec = L.read_json(L.decisions_path(n), {})
            if dec.get("approved") and dec.get("source_sha") != L.source_sha():
                errs.append("%s: approved against an older novel; review again" % L.decisions_path(n))


def check_manifests(errs):
    mdir = L.WORK / "manifest"
    cast = merged_cast()
    for p in sorted(mdir.glob("ch[0-9][0-9].json")) if mdir.exists() else []:
        n = int(p.stem[2:])
        ch = L.read_json(L.units_path(n))
        try:
            data = L.read_json(p)
        except ValueError as e:
            errs.append("%s: not valid JSON: %s" % (p, e))
            continue
        scenes = data.get("scenes", data) if isinstance(data, dict) else data
        by_id = {s.get("id"): s for s in scenes} if isinstance(scenes, list) else dict(scenes)
        for sc in ch["scenes"]:
            m = by_id.get(sc["id"])
            if m is None:
                errs.append("%s: no entry for scene %s" % (p, sc["id"]))
                continue
            for f in MANIFEST_FIELDS:
                if f in NULLABLE:
                    ok = f in m  # the role file says: where the text is silent, write null (cast: [] for an end card)
                else:
                    ok = bool(m.get(f))
                if not ok:
                    errs.append("%s: scene %s has no %s" % (p, sc["id"], f))
            if cast is not None:
                for who in m.get("cast", []):
                    if who not in cast:
                        errs.append("%s: scene %s: '%s' is not in the merged cast list" % (p, sc["id"], who))


def check_ledger(errs):
    ledger = L.WORK / "ledger.jsonl"
    if not ledger.exists():
        return
    cap = (L.read_json(L.ROOT / "config" / "budget.json", {}) or {}).get("total_cap")
    total = 0.0
    for i, line in enumerate(ledger.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            total += float(json.loads(line).get("cost", 0))
        except (ValueError, TypeError):
            errs.append("%s: line %d is not valid" % (ledger, i))
    if cap is not None and total > cap + 1e-9:
        errs.append("work/ledger.jsonl: spent %.2f, over the cap of %s" % (total, cap))


def check_art(errs):
    try:
        import art
        idx = art.build_index()
        errs += ["art: " + e for e in art.check(idx)]
    except Exception as e:  # a broken index tool must fail the check, not hide
        errs.append("art: index could not be built: %s" % e)


def run_tests(errs):
    r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(L.ROOT / "tools" / "tests")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        errs.append("tools/tests: tests failed\n" + r.stderr[-1500:])


def main():
    errs = []
    check_split(errs)
    check_cuts(errs)
    check_manifests(errs)
    check_ledger(errs)
    check_art(errs)
    run_tests(errs)
    if errs:
        print("CHECK FAILED")
        for e in errs:
            print(" -", e)
        return 1
    print("check ok: split matches, suggestions load, manifests complete, ledger within cap, art index consistent, tests pass")
    return 0
