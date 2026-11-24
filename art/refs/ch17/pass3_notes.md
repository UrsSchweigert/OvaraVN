# Chapter 17 pass 3 (2026-11-24)

nano-banana-2 edits, 16:9, 1376x768 upscaled (Lanczos) to the old game size. Old files: art/refs/ch17/previous/c17_<name>_pass3.png. Reference copies in art/refs/ch17/cg, places and new (vault_grey) updated; game images replaced.

| Image | Result |
|---|---|
| bg c17_wall_face | FIXED (1 try): thin sharp top edge with a fine foam line; face has glassy depth, light shafts, bubbles, mist. Slight maroon/teal streaks in the depth. |
| cg c17_wall_climb | FIXED (1): wall is now the wall_face water; riders and needles unchanged. |
| bg c17_road_barges | FIXED (1): distant wall is smooth glassy water with foam edge and mist. |
| cg c17_barge_rows | FIXED (1): distant wall is glassy water; the wall's top line slopes slightly across the picture. |
| cg c17_two_old | FIXED (2): two old people sit on the rim of one wide pale hoop, bright pale water inside, feet over the water; the small oval ring removed. The hoop reads as an oval pool, wide. |
| cg c17_makers_quarrel | FIXED (2): one smooth hoop (inner ring gone); Makers have long narrow faces, large dark eyes, long limbs, broad hands, weathered skin, small pale scale marks on the cheeks (mariner and agravar mix). |
| cg c17_wall_faces | FIXED (1): the three faces are long, large-eyed, weathered, with fine scale marks; the mother now looks stern rather than soft. |
| bg c17_vault_grey | FIXED (2): walls dull cool grey; one large and one clearly smaller nested wheel. |
| bg c17_vault_lit, cg c17_vault_light | NOT DONE: fal.ai returned network errors (broken pipe) on every try. Still have two near-equal wheels. |
| bg c17_pit_view | NOT DONE (same errors). |
| bg c17_silt_street, cg c17_ilan_lamps | NOT DONE (same errors). One accidental try produced a wrong image (Victorian lamp) and was rejected; not installed. |

## Ledger note
Failed network calls are logged by ./vn image at the full $0.08 each although nothing was returned, so the ledger overstates the real spend.

## Text to add to art/bible.md
- Makers in illustrations (c17_makers_quarrel, c17_wall_faces): long narrow faces, long limbs, very large dark eyes set wide, broad large hands with long fingers, weathered leathery skin, often a mix of two kinds in one face (small pale scale marks on the cheekbones and temples for the mariner side, heavier brow and broader jaw for the agravar side). Choice where the text is silent.
- The wall (c17): top edge is a thin sharp line of fine foam, the face is translucent grey-blue glass-like water with pale vertical light shafts and a few bubbles (bg c17_wall_face, cg c17_wall_climb, bg c17_road_barges, cg c17_barge_rows).
- Vault of the Ring: the two wheels are one large and one about half its diameter nested inside it (done in bg c17_vault_grey; vault_lit and cg c17_vault_light still show near-equal wheels). Grey version: dull cool grey stone.
- cg c17_two_old: the pair sit on the rim of the hoop, water inside it.

## Remaining flaws
- vault_lit, vault_light wheels; pit_view ledge; silt_street and ilan_lamps lamp tips (all not done).
- makers_quarrel: the faces are strange rather than beautiful; scale marks look a little like a rash.
- wall_face and wall_climb: faint maroon streaks in the water depth.
- barge_rows: wall line slopes slightly.
