# Decisions

One dated line each, with the reason. Later sessions must respect these. The decisions taken before the first session are in the table at the top of `PLAN.md`.
- 2026-11-22: The fal key is stored under the variable name `FAL` in the owner's env file, not `FAL_KEY`. `./vn image` must accept `FAL` as well as `FAL_KEY` and `FAL_API_KEY`. Reason: that is what the file uses; the owner's file is not ours to change.
- 2026-11-22: Manifest format that `./vn check` expects: `work/manifest/chNN.json` is `{"scenes": [{"id": "c01.s01", "place", "time", "cast": [names], "mood", "key_moment"}, ...]}`, one entry per scene id; the merged cast list is `work/manifest/cast.json`, a list of names (or a dict keyed by name). Reason: the spec names the fields but not the layout; scene-analysts must write this layout.
