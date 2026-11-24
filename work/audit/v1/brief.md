# Staging audit brief (read-only audit; change NO game files)

Goal: for your chapters, list where the game needs a visual change, and what.
Read game/game/chNN.rpy (the staged script), source of truth for the text is work/cut/chNN.md, world bible in source/, art/canon.json, art/bible.md, and work/audit/inventory.txt (all existing backgrounds, illustrations, portraits).

## Pass A: long runs
A "text box" is one dialogue or narration line. A run = consecutive text boxes with no `scene`, `show` or `hide` line between. Any run longer than 5 breaks the rule (max 5 boxes without a visual change). For each run over 5, propose breaks (about one per 5 boxes) at the story's own turns. Never split mid-speech or between a question and its answer. Give the line number of the box AFTER which the change happens.

## Pass B: subject art
Any narration about a LEAD character (one with portraits in the inventory and a main role) or a SIGNIFICANT place (one that matters to the story, or is arriving at / first seen) wants art, even in runs of 5 or less. Minor characters and passing places do not.

## Tiers (choose by gravity)
1 beat: expression swap on a portrait already on screen (use only existing portrait names)
2 entrance/exit: a portrait appears or leaves (narration about a lead character: bring their portrait in)
3 scene shift: a new or second background (reuse an existing bg if one fits; else mark NEW)
4 full-screen illustration: reveals, reversals, violence, intimacy, a lead's defining deed, a major place's first appearance. Over an illustration no portraits are shown. Reuse an existing cg if one fits; else mark NEW.
Prefer reuse. Prefer free tiers 1-2. Mark tier 3/4 NEW only where it earns it. Dedupe: one new image per place; a variant only when light or time changes.
Rules: Wrack stays LEFT facing right, speaker RIGHT mirrored. Portraits only during dialogue. Lamp stays lit once lit. Restrained realistic expressions. Invent nothing: names, looks and places come from source/. Do not name artists, studios or other works.

## Output
Write ONLY work/audit/chNN.audit.json for each of your chapters, an array of entries:
{"ref":"c09.s02","line":123,"pass":"A|B|A+B","run_len":12,"after_text":"first 8 words of the box the change follows","tier":1-4,"change":"what to do, e.g. 'wrack_thread_calm -> wrack_thread_resolved' or 'bg c9_coal_wharf (reuse)' or 'NEW bg: short description of the place from the text'","why":"one line: the story turn or subject","new_image":null or {"kind":"bg|cg","name":"cN_name","prompt_seed":"plain description from the text"}}
Also write a 3-line summary at the end of your final reply: number of runs over 5, number of entries per tier, number of NEW images. Do not edit any other file.
