# Start here

This file is for an AI coding agent opened in this repository. The owner starts you by saying: **"Read START.md and begin."**

You are the **lead** of a small agent team turning the novel in `source/novel.md` into an anime-style visual novel for iPhone. You make most decisions yourself. The owner approves at four gates and reviews the text cuts; apart from that, do not wait for them.

## Every session

1. Read `CLAUDE.md` (the rules) and `PLAN.md` (stages, gates, budget).
2. Run `./vn status` and read the last entry in `work/log.md`.
3. Find the first stage in `PLAN.md` that is not finished and work on it. Hand chapter-sized work to the roles in `.claude/agents/`, in parallel where chapters are independent.
4. Stop only at a gate, at a chapter waiting for the owner's cut review, when the budget cap is reached, or when something in "Ask the owner" below applies. When you stop, say exactly what the owner must do, in one or two lines, with the command or link.
5. Before you end a session, append a dated entry to `work/log.md`: what was done, what was verified and how, what is waiting on the owner, what comes next. Commit.

## First session only

Do these in order. If a step fails, stop and show the exact output.

1. **Prerequisites.** Report a table of name, required, found, status. Do not install system software; give the owner the download page or command and carry on with whatever does not need it.

   | Tool | Required | Needed from |
   |---|---|---|
   | git, Python 3.9+ | yes | now |
   | fal.ai key | yes | stage 2 |
   | Ren'Py SDK, current stable version | yes | stage 5 |
   | Xcode with command line tools | yes | stage 7 |
   | Apple developer account | owner's own | stage 9 |

2. **The fal.ai key.** The owner keeps it in an env file in another repository of theirs, called `derschweigert`. Ask for the file's path if you cannot find it. Write only the *path* into `config/local.json` as `{"fal_env_file": "..."}` (that file is ignored by git). Never copy, print or commit the key.
3. **Split the novel.** Run `./vn split`. It must report 18 chapters and 73,618 words. If it does not, stop.
4. **Build the tools** described in `docs/tools-spec.md`, in this order, each with tests, each committed separately: the cutting review app, `./vn check`, the image command with its spending ledger. `./vn split`, `status`, `apply` and `gate` exist already; the splitter was run once and the rest is untested, so test them as you build on them.
5. **Prove the cutter with chapter 1.** Act as the cutter role, write suggestions for chapter 1, start the app, and tell the owner it is ready to review. While they review, carry on with stage 1.

## Ask the owner

Ask, and carry on with other work meanwhile, when:

- a gate is reached (`PLAN.md`);
- spending would pass the cap in `config/budget.json`;
- something needs an account, a payment, a signature, a password, or a system install;
- you would change anything in `source/`;
- two rules conflict.

Everything else is yours to decide. Record decisions that later sessions must respect in `docs/decisions.md`, one dated line each with the reason.
