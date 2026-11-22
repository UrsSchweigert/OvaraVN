# The Man the Tide Brought In: visual novel

Everything an AI coding agent needs to turn the novel into an anime-style visual novel for iPhone.

## To start

1. Open an AI coding agent (for example Claude Code) in this folder.
2. Say: **Read START.md and begin.**
3. It will report what is installed, ask where the fal.ai key file is, build its tools, and tell you when chapter 1 is ready for you to review cuts.

## Your part

- Review the suggested text cuts, chapter by chapter, in the cutting app the agent builds.
- Approve at four gates: the style, the cast, the chapter 1 slice, the release. `./vn gate` lists them.
- Install Ren'Py when the agent asks, and do the Apple account steps yourself.

## What is here

| File | What it is |
|---|---|
| [START.md](START.md) | The agent's instructions for the first and every later session |
| [CLAUDE.md](CLAUDE.md) | The rules every agent follows |
| [PLAN.md](PLAN.md) | Stages, gates, budget, and the decisions already taken |
| [docs/tools-spec.md](docs/tools-spec.md) | The tools the agent builds first, including the cutting review app |
| [work/cuts/guide.md](work/cuts/guide.md) | How cuts are suggested; it learns from your corrections |
| `.claude/agents/` | Six roles: scene analyst, cutter, scriptwriter, art director, image reviewer, builder |
| `source/` | The novel and the world bible. Read-only. |
| `vn`, `tools/` | The command script. `./vn status` shows where everything stands. |

## State of things

Instructions, plan and roles are written. The novel splitter was run once (18 chapters, 93 scenes, 73,618 words). The cutting app, the checks and the image tool are specified but not built. There is no game, no art, and no fal.ai call has been made.
