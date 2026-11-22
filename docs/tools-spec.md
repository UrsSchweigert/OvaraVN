# Tools to build

All tools are commands of `./vn`, written in Python with the standard library only, in `tools/`. Shared logic is in `tools/vnlib.py`, which already defines the paths, the splitter, how suggestions are loaded and validated (`load_suggestions`), how a sentence's final state is worked out (`effective`), and how approved text and the review summary are written (`apply_chapter`). Build on it; change it if a test shows it is wrong.

Each tool gets tests under `tools/tests/`, run by `./vn check`.

## 1. The cutting review app: `./vn cutter [port]`

**Purpose.** The owner reads a chapter with the suggested cuts marked, corrects them, and approves. This is the owner's main working screen, so it must be pleasant to read for hours.

**Shape.** A local web server bound to `127.0.0.1` (default port 8765) serving one HTML page with plain JavaScript. No build step, no packages, works offline.

**Files it reads and writes.**

Suggestions, written by the cutter agent, `work/cuts/chNN.suggestions.json`:

```json
{"chapter": 1, "items": [
  {"id": "c01.s01.p003.3", "action": "cut", "kind": "shown", "reason": "The background shows the kelp trunks."},
  {"id": "c01.s01.p005.2", "action": "replace", "kind": "condense", "text": "…", "reason": "…"},
  {"id": "c01.s02.p004", "action": "cut", "kind": "pace", "reason": "A paragraph id cuts every sentence in it."}
]}
```

Kinds: `shown` (the picture shows it), `redundant`, `pace`, `condense`, `other`.

Decisions, written only by the app, `work/cuts/chNN.decisions.json`:

```json
{"chapter": 1, "approved": false, "source_sha": "…", "note": "note to the cutter for this chapter",
 "decisions": {"c01.s01.p003.3": {"state": "keep", "note": "I like this line"},
               "c01.s01.p004.1": {"state": "cut"},
               "c01.s01.p005.2": {"state": "edit", "text": "the owner's wording"}}}
```

A sentence with no decision follows its suggestion; with no suggestion it is kept.

**The page.**

- A chapter list with, for each: title, words before and after, percent cut, and whether it has no suggestions yet, awaits review, or is approved.
- The chapter as readable prose in a comfortable column, scene breaks visible. Each sentence is its own clickable span. Render `*italics*`.
- Marking, distinguishable without relying on colour alone:
  - suggested cut: struck through;
  - suggested replacement: old wording struck through, new wording beside it;
  - a suggestion the owner overruled: shown as kept, with a quiet mark that a suggestion was declined;
  - the owner's own cut or edit: marked differently from the agent's.
- Selecting a sentence shows its reason and kind, and the actions Keep, Cut, Edit, Reset (back to the suggestion), plus an optional note to the cutter.
- Keyboard: next and previous suggestion, keep, cut, edit, reset. A whole paragraph can be cut or kept at once.
- A "read the result" view that shows only the text as it would ship.
- A running count: words before, words after, suggestions still unseen.
- A note to the cutter for the whole chapter.
- Every change saves at once. Reloading the page loses nothing.
- **Approve chapter** asks for confirmation, stating how many unseen suggestions will be accepted as they are, then sets `approved`, records `source_sha`, and runs `apply_chapter`. An approved chapter can be reopened.
- Light and dark appearance following the system.

**Tests.** Server endpoints against a temporary work folder: load a chapter, save a decision, approve, reopen; a malformed suggestion file is reported on the page and not silently dropped. Then drive the real page in a browser once for chapter 1 and record what you saw.

## 2. `./vn check`

One command that says whether the project is sound. It exits non-zero and names the file on any failure. It grows with the project. To begin with:

- `./vn split` reproduces `work/units/` exactly, and the totals are 18 chapters and 73,618 words;
- every suggestions file loads with no problems (`load_suggestions`);
- every approved chapter's `source_sha` matches the current novel;
- every manifest file has, for each scene id in the chapter: `place`, `time`, `cast`, `mood`, `key_moment`; and every name in `cast` is in the merged cast list;
- the ledger total does not exceed the cap;
- the tools' own tests pass.

Later, add: every image the script names exists; every sentence of approved text appears in the Ren'Py script exactly once and in order; Ren'Py lint passes.

## 3. `./vn image` and `./vn spend`

**Purpose.** The only way agents generate images, so that cost is logged and capped.

- Reads the fal key from the environment, else from the env file whose path is in `config/local.json` (`fal_env_file`). Accept the variable names `FAL_KEY` and `FAL_API_KEY`. Never print the key.
- Models are named in `config/models.json`: a short name, the fal model id, the price per image, and how the model takes prompts and reference images. Fill this in from the fal model pages; do not guess ids, input names or prices.
- Arguments: model short name, prompt (or prompt file), zero or more reference image files, output path, a purpose tag (`bakeoff`, `sheet`, `background`, `sprite`, `illustration`), and the chapter if any.
- Before calling: add the model's price to the ledger total and refuse if it would pass the cap for that purpose or in total (`config/budget.json`).
- After calling: save the image, and append one line to `work/ledger.jsonl` with time, model, purpose, chapter, cost, output path, the prompt's hash, and whether it succeeded. Save the prompt beside the image as a `.txt` file.
- `./vn spend` prints totals by model and by purpose, and what is left.
- A `--dry-run` flag does everything except the network call.

**Tests.** With the network call replaced by a fake: the ledger line is written, the cap refuses, a missing key gives a clear message that does not contain any part of a key. Then one real call, the cheapest model, logged as `bakeoff`.
