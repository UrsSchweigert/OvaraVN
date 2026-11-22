# Session log

Newest entry last. Each entry: date, what was done, what was verified and how, what is waiting on the owner, what comes next.

## 2026-11-22: repository prepared

- Done: novel and world bible copied into `source/`; rules, plan, roles and tool specifications written; `./vn split`, `status`, `apply` and `gate` written.
- Verified: `./vn split` was run once and reported 18 chapters, 93 scenes and 73,618 words. Nothing else has been run.
- Not built: the cutting review app, `./vn check`, `./vn image`. No Ren'Py project. No images. No fal.ai call has been made.
- Next: the first session in `START.md`.

## 2026-11-22: first session

- Done: fal key path stored in `config/local.json` (ignored by git). Built and committed: the cutting app (`./vn cutter`), `./vn check`, `./vn image` and `./vn spend` with `config/models.json`. Wrote 16 suggested cuts for chapter 1 (3500 to 3240 words, 7%).
- Verified: `./vn split` gives 18 chapters, 73,618 words. 19 unit tests pass and `./vn check` exits 0. One real fal call (`flux-2-flash`, purpose `bakeoff`) saved a 512x512 PNG, so the key, data-URI references and the ledger work. Total spent: $0.02 of $200. The cutting app answers its API on http://127.0.0.1:8765 for chapter 1.
- Not verified: the cutting page has not been opened in a real browser; only its server was tested. Chapter 1 suggestions were written without a scene manifest (stage 1 is not done), so the "shown" cuts assume the picture will show those things.
- Waiting on the owner: review chapter 1 at http://127.0.0.1:8765 (use 127.0.0.1, not localhost: another program on this Mac answers on localhost:8765). Install Ren'Py before stage 5.
- Next: stage 1, one scene-analyst per chapter, then the style bake-off. After the owner approves chapter 1, read its review file and update `work/cuts/guide.md`.

## 2026-11-22: stage 1 done

- Done: scene manifests for all 18 chapters (93 scenes), merged `work/manifest/cast.json` (67 names) and `places.json` (64 place names, not yet merged into backgrounds). `./vn check` changed to accept null `time`, `key_moment` and an empty `cast` for an end card.
- Verified: `./vn check` exits 0 with all manifests in. Sentence ids inside `looks` and `key_moment` were not checked by a tool; only some analysts checked them by hand.
- Not done: chapter 1 cuts not re-read against the manifest. The owner has not yet reviewed chapter 1.
- Open problem for stage 2: every model in `config/models.json` is an edit model and needs a reference image, but there is no art yet. The bake-off needs text-to-image variants of the candidates, or a plain first reference. Check fal's text-to-image ids and prices before spending.
- Next: resolve that, then the bake-off (cap $10).

## 2026-11-22: chapter 1 reference images

- Done: added text-to-image models to `config/models.json` (`flux-2-t2i`, `seedream-4.5-t2i`, `nano-banana-2-t2i`; the three work). Compared them on Sefa, chose flux-2. Made reference images for Sefa, Wrack, Bother, Elder Oro, Ione and Davin in `art/refs/ch01/` (two rejected and redone). Draft `art/bible.md`.
- Verified: I looked at each image and compared it with the sentences cited in the bible. I did not use the image-reviewer agent. Spend so far about $0.30 of $200.
- Waiting on the owner: gates `style` and `cast` (not approved; the owner has not seen these). Chapter 1 cut review.
