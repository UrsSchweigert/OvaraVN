# Chapter pipeline

How a chapter goes from novel text to playable game. Chapter 1 was built this way; follow it for every chapter. Tools are commands of `./vn`; see `docs/tools-spec.md`.

## Gate before anything

The chapter's cuts must be approved by the owner in `./vn cutter` (`./vn status` shows "approved"). Never start the script before that. Never approve for the owner.

## Steps

1. **Cuts** (cutter, stage 4). Suggestions in `work/cuts/chNN.suggestions.json`; owner approves; `./vn apply` writes `work/cut/chNN.md`. After approval read `chNN.review.json` and update `work/cuts/guide.md`.
2. **Manifest** (scene-analyst, stage 1): `work/manifest/chNN.json`, merged `cast.json` and `places.json`.
3. **Cast art.** For each new character: read the `looks` sentences in the manifest; write the look into `art/bible.md` (mark choices where the text is silent). Generate a base portrait, then 3 to 6 expression portraits (head and shoulders, drawn facing the viewer's right), named in `art/refs/chNN/portraits/`.
   - Base: `./vn image flux-2-t2i` (text to image), size 1024x1536 then crop, or 1024x1024. Expressions: `./vn image flux-2 --ref <base>` (edit mode, up to 4 refs) with "same character, only the expression changes".
   - Cut backgrounds out with `./vn image birefnet-heavy --ref in.png --out out.png --purpose sprite`; copy to `game/game/images/p_<character>_<emotion>.png`. Do NOT use `tools/cutout.py` on faces (it removed an eye white).
   - If fal's content filter rejects a reference (wounds, scars), crop it to the head and shoulders.
4. **Place art.** Wide 1920x1080 backgrounds with `flux-2-t2i`, no people, from the manifest `needs` and the world bible. Underwater places get the ripple; indoor ones do not. Add a lighting line for each new background name in `PORTRAIT_LIGHT` (`game/game/effects.rpy`).
5. **Illustrations** for narrated key moments (manifest `key_moment`, plus other narrated actions). `flux-2` edit with portraits as references (up to 4); state in the prompt exactly who is present ("exactly one person"), the pose, and that nobody else appears. Shown full screen; no portraits over them.
6. **Review every image at full size**, not as thumbnails. Check against the sentences it depicts: anatomy (legs, hands, eyes with pupils), no duplicated characters, props right (hook, boots), no stray figures. Redo at most 6 times; keep rejects in a `rejected/` folder beside the image. Fix the real cause in the prompt each time.
7. **Script** (scriptwriter): `game/game/chNN.rpy`, text only from `work/cut/chNN.md`, word for word, in order. Name labels from speech tags. Portraits only during dialogue: Wrack left, the other speaker right (flipped), swap on speaker change; emotion chosen from the text; illustrations for the narrated passages; Bother in the corner when he acts. `python3 tools/check_script.py` must match.
8. **Checks:** `<sdk>/renpy.sh game lint`, `python3 tools/check_script.py`, `./vn check`. Commit.
9. **Launch** for the owner with `./vn play` (or `./vn play N`): it closes every old game window, starts one, and checks the log for exceptions. Never capture the whole desktop; use `renpy.screenshot` from inside the game for frames.

## Jumping to a chapter

- `./vn play N` starts the game straight at chapter N (it closes old windows first); `./vn play` opens the main menu; `./vn play --list` shows which chapters are built. A chapter counts as built when `game/game/chNN.rpy` has `label chNN:`.
- In the game, **Chapters** in the main menu and the in-game menu lists all 18 and starts any built one. Nothing to register: a new `label chNN:` makes its row clickable.
- The mechanism is `game/game/dev.rpy` (environment variable `VN_START`, also handy for test labels) and `game/game/chapter_select.rpy`.

## Testing rules

- Test scripts must NEVER set `_preferences.*` (auto-forward, skip, volume, text speed): preferences are saved to the player's persistent file and survive restarts. On 2026-11-22 a test left auto-advance on at 0.02 s and the game ran through everything by itself. For skipping use `config.skipping` (not saved); for auto-advance in tests use a Python flag, or restore the old values and call `renpy.save_persistent()` before quitting.
- Fast-skip runs skip transitions. For a real check run the chapter with transitions in real time (auto-forward by a test-only flag) and watch a progress counter file.

## Facts to remember

- Cost: portraits about $0.024 each, backgrounds $0.024, illustrations $0.04 to $0.07, cutouts about $0.01. A chapter costs roughly $3 to $6. Check `./vn spend`.
- The lamp in the meeting hall stays lit after chapter 1 (`meeting_hall_lit`).
- Underwater scenes get the light ripple; portraits are lit per background (strength 0.5).
- Add every decision that later sessions must respect to `docs/decisions.md`.
