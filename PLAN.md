# Plan

## What is being made

A visual novel for iPhone: backgrounds, character sprites with expressions, full-scene illustrations at key moments, the novel's text in a text box, music and sound. Anime style throughout.

## Decisions already taken

| Decision | Choice | Why |
|---|---|---|
| Look | Anime style, everywhere | Owner's choice |
| Who decides | Agents, except at the gates below | Owner's choice |
| Branching | None. The reader follows the novel. | Default; the owner has not asked for choices. Ask before adding any. |
| Engine | Ren'Py | Saves, history, skip and rollback come built in; the script is plain text; it has a lint check; it exports to iOS |
| Images | fal.ai, using reference-image models | One key covers every candidate model; references keep faces consistent without training |
| Cutting | Suggested by an agent, decided by the owner in a review app | Taste in cutting is the weakest automated step |

Not yet verified by anyone: that the current Ren'Py version builds for the current iOS, and the exact fal model ids, inputs and prices. Verify each from its official documentation when its stage begins, and record what you find in `docs/decisions.md`.

## The book in numbers

18 chapters in 6 parts, 73,618 words, 93 scenes. About a third of the words are spoken. About 10 characters recur heavily (Wrack, Ilan, Sefa, Okonta, Jef, the Dragon, Maelis, Rook, Dace, and the hound Bother) and about 20 more are named.

Rough asset estimate, to be replaced by the real count from the manifest: 40 backgrounds, 100 sprites and expressions, 35 illustrations.

## Stages

Stages 1 and 2 can run at the same time. Stage 4 runs alongside everything after it.

| # | Stage | Who | Output | Done when |
|---|---|---|---|---|
| 0 | Setup and tools | lead | Tools from `docs/tools-spec.md` | Their tests pass; chapter 1 is in the cutter |
| 1 | Scene manifest | scene-analyst, one per chapter | `work/manifest/chNN.json`, then a merged cast list and location list | `./vn check` passes; every scene has a place, a time, a cast and a key moment |
| 2 | Style bake-off | art-director | The same 3 characters and 2 places through each candidate model, on one comparison page | **Gate: style** |
| 3 | Art bible and sheets | art-director, image-reviewer | `art/bible.md`; a reference sheet per recurring character and place | **Gate: cast** |
| 4 | Cutting | cutter, then the owner | Suggestions per chapter; approved text in `work/cut/` | Every chapter approved in the app |
| 5 | Script | scriptwriter, one per chapter | `game/` Ren'Py script from approved text | Lint passes; every line of approved text appears once, in order |
| 6 | Assets | art-director, image-reviewer | Backgrounds, sprites, illustrations for the chapter | Every image the script names exists and passed review |
| 7 | Chapter 1 slice | builder | Chapter 1 complete, running in the iOS simulator | **Gate: slice** |
| 8 | Chapters 2 to 18 | all, in parallel | The rest, by the same route | Lint passes; an automated run reaches the end |
| 9 | Release build | builder | A TestFlight build, music and sound in place | **Gate: release** |

## Gates

The owner approves each with `./vn gate <name> approve`. Bring the owner one page or one build to look at, and a recommendation.

| Gate | The owner looks at | Approves |
|---|---|---|
| `style` | The bake-off comparison page, with cost per image for each model | The look and the model |
| `cast` | The character and location sheets | Who looks like what |
| `slice` | Chapter 1 on a phone or the simulator | Text pacing, art, interface, sound |
| `release` | The full game | Sending it to TestFlight |

## Cutting

The cutter suggests; the owner decides in the review app (`./vn cutter`).

- Start with chapter 1 alone. After the owner approves it, read `work/cuts/ch01.review.json`, update `work/cuts/guide.md`, then do chapters 2 and 3.
- When the owner has accepted at least 90% of suggestions in two chapters running, suggest all remaining chapters at once.
- Never start the script for a chapter before its cuts are approved.

## Images

- Candidates for the bake-off: the current Nano Banana (Gemini Flash Image) edit model, the current Seedream edit model, and FLUX.2. Check the fal catalogue for newer or better anime-capable models first; this list was written from price aggregators, not from testing.
- Every character image is generated with that character's approved sheet attached as a reference. Every place likewise.
- Sprites need transparent backgrounds: generate on a flat colour and remove it, or use a background-removal model. Choose one method in the bake-off.
- The image-reviewer compares each result with the sheet and the scene manifest. At most 6 attempts per image; after that, put it on a list for the owner instead of spending more.

## Budget

`config/budget.json` holds the cap for image generation: 200 US dollars in total, 10 for the bake-off. When 80% is spent, tell the owner. Expect 3,000 to 5,000 generations in all.
