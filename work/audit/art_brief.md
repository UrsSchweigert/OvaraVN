# Stage-art brief (generation job, group GROUP)

You make NEW images for the visual novel's staging pass, following docs/chapter-pipeline.md steps 3-6 (art, image rules, review) exactly. Read first: CLAUDE.md, docs/chapter-pipeline.md, docs/decisions.md, .claude/agents/art-director.md, art/canon.json (prompt_rules, characters, objects, places), art/bible.md (format and looks), the approved text work/cut/chNN.md for each chapter you touch (the only story source), source/world-bible.md as needed, game/game/images_ch06.rpy (exact registration format), work/audit/inventory.txt (existing images).
Image seeds live in work/audit/chNN.audit.json: entries with a "new_image" field (kind bg|cg, name, prompt_seed, ref, line). The text at that ref/line is what the image shows. Extra items are listed in your job below.

Rules:
- 1920x1080 backgrounds (flux-2-t2i, no people) and illustrations (cg), named exactly as given. Illustrations: say exactly who is present; pass the cast portraits / canon references as --ref (see ./vn art canon <name>); no duplicated people, no readable text or letters, eyes with pupils, one consistent skin and hair colour per character; no portraits are shown over illustrations in game. Underwater vs above water exactly as the text says.
- Do not show anything the text has not yet revealed at that point of the story (spoiler discipline: look only at what is narrated up to the line the image serves).
- Review every image at full size against the sentences it depicts. Redo up to 6 times; keep rejects in rejected/ beside the image; fix the cause in the prompt.
- Only through ./vn image (cap in config/budget.json, never raise it). At most 2 ./vn image calls at once (other agents run in parallel). No living artist, studio, series or other works' characters in prompts. Never print keys. Restrained, realistic mood.
- Copy finished files to game/game/images/bg/ or game/game/images/cg/ (check first so you never overwrite a file).
- Register ONLY in your own new file game/game/images_stage_GROUP.rpy, in the exact format of images_ch06.rpy (cg: as illustrations are registered there; underwater backgrounds wrapped in the water transform as there; dry/indoor ones not).
- Write ONLY these shared-info files for the lead to merge: art/refs/stage_GROUP/light_additions.txt (PORTRAIT_LIGHT lines for each new background; format as art/refs/ch06/light_additions.txt; none needed for cg), art/refs/stage_GROUP/canon_additions.json (format as art/refs/ch06/canon_additions.json), art/refs/stage_GROUP/bible_additions.md (looks and choices with sentence ids; mark choices where the text is silent).
- Do not edit source/, work/cut, work/cuts, decisions.json, art/canon.json, art/bible.md, art/index.*, game/game/effects.rpy, any ch*.rpy, any images_chNN.rpy, tools/. Do not run ./vn art or commit.
- Invent nothing. Where the text is silent choose the plainest reading consistent with the world bible and record it.
Report in under 250 words: every image name with the first words of the sentence it depicts, what is weak or known-flawed, rejects, cost.
