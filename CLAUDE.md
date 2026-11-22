# Rules

Every agent reads this at the start of every session. `START.md` says how to begin; `PLAN.md` says what to build.

## The project

An anime-style visual novel for iPhone, made from the novel *The Man the Tide Brought In* (`source/novel.md`, 18 chapters, about 73,600 words). It is built AI-first: agents do the work and make most decisions; the owner approves at gates and reviews the text cuts.

## Hard rules

1. **`source/` is read-only.** The novel and the world bible are the owner's. Never edit them. If you find a mistake, tell the owner.
2. **Invent nothing about the story or the world.** Every name, place, look and event comes from `source/`. If the source does not say what something looks like, choose the plainest reading that fits the world bible and record the choice in the art bible, so every later image agrees.
3. **The owner's words win.** Text in the game is the novel's text, minus approved cuts. Do not rewrite sentences outside a `replace` suggestion that the owner has seen in the cutting app. A replacement reuses the author's words and adds no fact.
4. **Only the owner approves.** Never run `./vn gate ... approve`, never mark a chapter approved, never edit a `decisions.json` file. Those record the owner's choices.
5. **Money has a cap.** All image generation goes through `./vn image`, which logs cost to `work/ledger.jsonl` and refuses past the cap in `config/budget.json`. Do not call fal.ai any other way. Do not raise the cap.
6. **Secrets stay out.** Never print, copy or commit a key or token. Never put the owner's name, email or other personal details in a prompt, a request or a committed file.
7. **Do not weaken a check to make it pass.** If `./vn check` or Ren'Py's lint fails, fix the cause or stop and report.
8. **No copying.** Do not name a living artist, a studio, a series or a character from elsewhere in an image prompt, and do not use other works' images as references. Describe the look in plain words.
9. **Say what you verified.** When you report something as done, say how you checked it. If you did not check it, say so.

## How work is stored

| Path | What | Who writes it |
|---|---|---|
| `source/` | Novel and world bible | Nobody |
| `work/units/` | The novel as sentences with stable ids (from `./vn split`; not in git) | `./vn split` |
| `work/manifest/chNN.json` | Each scene: place, time, who is present, mood, key moment | scene-analyst |
| `work/cuts/chNN.suggestions.json` | Proposed cuts | cutter |
| `work/cuts/chNN.decisions.json` | The owner's choices | The cutting app only |
| `work/cuts/chNN.review.json` | Where the owner overruled the suggestions | `./vn apply` |
| `work/cuts/guide.md` | The cutting guide, which learns from reviews | cutter |
| `work/cut/chNN.md` | Approved text | `./vn apply` |
| `art/bible.md`, `art/refs/` | The look, the cast sheets, the location sheets | art-director |
| `game/` | The Ren'Py project | scriptwriter, builder |
| `work/ledger.jsonl` | Every image generated and what it cost | `./vn image` |
| `work/log.md` | Session log | lead |
| `docs/decisions.md` | Decisions later sessions must respect | lead |

Sentence ids look like `c01.s02.p013.2`: chapter 1, scene 2, paragraph 13, sentence 2. They are stable as long as `source/novel.md` does not change. Use them whenever you point at text.

## Working habits

- One chapter per subagent. Chapters are independent, so run them in parallel.
- Commit small and often, with messages that say what changed. Never push without the owner asking.
- Standard library Python only in `tools/`, unless a decision in `docs/decisions.md` says otherwise.
- Write plainly in everything the owner reads: short sentences, no jargon, the answer first.
