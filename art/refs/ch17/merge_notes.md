# Chapter 17 merge notes (art director, 2026-11-23). The lead merges these into the shared files.

Cost by ledger: about $1.65 for chapter 17 (4 sheets, 19 sprite/cut-out calls, 18 backgrounds, 19 illustrations including rejects). No file outside art/refs/ch17, game/game/images* and images_ch17.rpy was touched.

## effects.rpy PORTRAIT_LIGHT (donor in brackets)
        "c17_dead_water":     (0.90, 0.92, 0.92, -0.06, 0.88, 0.0),   # c8_belt_rain, greyer
        "c17_road_barges":    (0.92, 0.96, 0.98, -0.04, 0.92, 0.0),   # c8_brightwater_ext style, overcast with bright water
        "c17_wall_face":      (0.90, 0.92, 0.96, -0.06, 0.90, 0.0),   # c7_halcyon_office, cooler
        "c17_pit_view":       (1.00, 0.97, 0.92, -0.02, 0.94, 0.0),   # c12_apron, hazy sun on mud
        "c17_silt_street":    (0.90, 0.92, 0.94, -0.08, 0.88, 0.0),   # c8_belt_rain, no tint
        "c17_square_silt":    (1.00, 0.98, 0.94, -0.02, 0.94, 0.0),   # c12_apron
        "c17_vault_grey":     (0.82, 0.86, 0.94, -0.14, 0.84, 0.0),   # dc_heart_chamber, darker
        "c17_vault_lit":      (1.00, 1.00, 1.00, 0.00, 0.96, 0.0),    # c7_nine_spires, white glow
        "c17_square_flooded": (0.96, 0.96, 0.98, -0.04, 0.92, 0.0),   # c14/c15 dawn-ish, pale
        "c17_city_risen":     (1.00, 1.00, 1.00, -0.02, 0.95, 0.0),   # c7_nine_spires

## Which scene uses what
- c17.s01: bg c17_dead_water; cg c17_healers_line (key: six thousand sit down), c17_hush_kneels (the small healer kneels, "Sit down. All of you."), c17_barge_rows (barges lift the healers aboard, bread). Portraits: Yeva (p yeva_stern / yeva_dry), Sefa (p sefa_thoughtful / understanding), the Hush healer (p hush_healer_gentle for "We have" and her speech; hush_healer_steady for "Sit down...").
- c17.s02: bg c17_road_barges; cg c17_corin_calls (key). Portraits: Corin p corin_calling, Odo p fatman_firm (existing).
- c17.s03: bg c17_wall_face, cg c17_wall_climb, bg c17_pit_view (key: the pit seen from the wall top, no people), bg c17_silt_street + cg c17_ilan_lamps, bg c17_square_silt. Portraits: Okonta (existing), Raske raske_steady/stern, Hanne p hanne_wondering ("It knows you"), Crane crane_flat, Wrack p wrack_thread_resolved.
- c17.s04: bg c17_vault_grey (arrival), then bg c17_vault_lit when the walls turn to light; cg c17_vault_light (key). Portraits: Rook p rook_old_tired (arrival, "You came the long way"), rook_old_nearsmile ("Tuesday..."), rook_old_sharp ("The dark eyes sharpened" / "For me?"), Maelis p maelis_cropped_level ("Hello, Anselm" -- hair is cut), Wrack thread_pleading / thread_resolved.
- c17.s05: bg c17_vault_lit; cg c17_two_old (key). Portraits: Rook p rook_old_eased ("The square face eased"), Maelis p maelis_composed / cropped_level, Wrack p wrack_thread_exhausted.
- c17.s06: bg c17_square_flooded (dawn, the sea arrives), cg c17_city_rises (key), bg c17_city_risen (noon), cg c17_wall_faces (the walls showing faces), cg c17_hands_reach (welder and net-mender). Portrait: Maelis (speaks only reported speech: "the third tower was out of true"; p maelis_composed). Not made (no picture needed or too risky): Brask hauled aboard (reuse p brask_*), Garran lifting Ione (scarred arms: the filter rejects scar references), the gunboat standoff, Crane taking off his helmet, the rays hanging still.

## Image names in game/game/images_ch17.rpy
bg: c17_dead_water, c17_road_barges, c17_wall_face, c17_pit_view, c17_silt_street, c17_square_silt, c17_vault_grey, c17_vault_lit, c17_square_flooded, c17_city_risen (none underwater, no ripple).
cg: c17_healers_line, c17_hush_kneels, c17_barge_rows, c17_corin_calls, c17_wall_climb, c17_ilan_lamps, c17_vault_light, c17_two_old, c17_city_rises, c17_wall_faces, c17_hands_reach.
p: rook_old_tired, rook_old_nearsmile, rook_old_eased, rook_old_sharp, hush_healer_gentle, hush_healer_steady, corin_calling, hanne_wondering.

## art/canon.json "characters"
New entry:
"The Hush healer": {
 "fixed": "small slight woman healer of about fifty, medium brown skin, short plain black hair going grey at the temples (a grey streak above each ear), calm dark brown eyes, fine lines, quiet patient face; plain dark grey high-collared tunic, a grey band on the upper arm in illustrations (text: 'a small woman', 'in dark grey', 'kept her voice low from habit'; age, skin and hair are choices). Expressions: hush_healer_gentle (base, speaking softly), hush_healer_steady (mouth closed, level eyes).",
 "references": ["art/refs/ch17/portraits/hush_base.png"]
}
Grown lists:
- "Anselm Rook": add "Rook at ninety (ch17): the same man, white hair thinner, face deeply lined and hollow, papery pale skin, plain pale open-collared shirt, hands wrapped in stained rags in illustrations, the thin pale pen-line scars from temple past the ear down the neck. Expressions rook_old_tired (base), rook_old_nearsmile, rook_old_eased, rook_old_sharp. Reference art/refs/ch17/portraits/rook_old_tired.png (scars are faint here; rook_old_nearsmile.png shows them best)." Add reference rook_old_nearsmile.png.
- "Corin": add expression corin_calling (mouth open a little, brows level, steady).
- "Hanne (the woman from engines, ch12 expression)": add expression hanne_wondering (whispering, eyes ordinary size, lips parted).

## art/bible.md rows
- The dead water (c17): bg c17_dead_water. Flat, still, dull grey-green sea under an even grey sky, a low wall of grey still water on the horizon. The text gives no colour ("clean", "told not to listen"); grey-green is a choice. Healed water is a soft sea-green (the model drew it neon in several images; kept as is, see open points).
- The wall (c17): The wall is HELD SEA WATER, not stone, rock, metal or glass (c17: "sixty metres of sea stepped forward", "as smooth as poured glass, and it made no sound", "the wall let go"). Draw it as smooth, grey, still, glassy standing water: sheer, no seams, panels, cracks or rock layers; foam only along the top edge where it meets sky and sea; mist at the foot. bg c17_wall_face; seen from the inside as a ring of grey glassy water in c17_pit_view and cg c17_pit_city. The pit eighty kilometres across: mud plain, dead fish, a six-legged rusty platform, the grey silted city of low rounded halls, the Dragon coiled round the central hall with its ring of hoops for ribs (Dragon design from c15_dragon_ribs).
- Silted city street and square (c17): low rounded grey mud-coated halls, slender pale-metal lamp-posts that light as Ilan passes; square with the rusty platform on six legs (the text says "six rusty legs"; deck and railing are a choice).
- Vault of the Ring (c17): round chamber like the inside of a bell (no bell object), ring of pale metal forty metres across flush in the floor, two wheels in a raw steel frame at the centre, three open doorways at the top of a stair, a bench with pinned drawings; the lit version has glowing walls with soft unreadable pictures of towers and steps (the text: the pictures show the city, the quarrel and the fall; only the first and last, the happy city, are drawn).
- The risen city (c17): tall pure white obelisk-like towers (text: "white... taller than the Spires"), water pouring down in white cataracts, a broad white stair going down into the sea.
- Choices where silent: the Hush healer's looks; Rook at ninety wears a plain pale open-collared shirt (the text: "in his shirt"); Maelis keeps the very short grey hair of her ch10+ portraits (text: "You've cut your hair"); the two rowers and the docker's wife in c17_barge_rows (weathered tan skin, headscarf); the welder (short dark beard) and the net-mender (headscarf, tan skin) in c17_hands_reach.

## Verified
Every PNG above was opened and looked at at full size; portraits were checked for facing (all face right, none needed mirroring) and the cut-outs on a red backdrop (holes in white hair and one eye hole filled from the source, see tools note: hair/eye holes were filled with a small script in the scratchpad, not tools/cutout.py). Not verified in the game (no run). The Corin illustration and some others were checked only against the sentence, not against other chapter art side by side.

## Open points (flaws the owner may want redone)
- Neon green: the healed water is a saturated green in c17_barge_rows, c17_healers_line and c17_hands_reach (three prompts asked for soft sea-green; the model still draws it strong).
- c17_wall_climb: redone again 2026-11-24 (owner request): three needles (Okonta + engineer, Ilan alone, Corin + engineer) fanning up the water wall with spray streaks; riders are larger than the dizzying-scale ideal; text says thirty. Okonta's skin reads slightly lighter than her sheet.
- c17_corin_calls: Corin stands with arms spread (a bit theatrical); the text only says "hands open".
- c17_vault_light: Rook sits on the floor behind the bench (reads as kneeling); Ilan holds the tool at arm's length instead of across the ring.
- c17_pit_view: the platform is small and its legs are hard to count; the pit rim is the inside of the water wall with the sea over its top edge (redone 2026-11-24; was a rock cliff).
- rook_old_*: the scar lines are faint in tired/sharp/eased (the model keeps drawing them as wrinkles); nearsmile shows them best. The shirt colour drifts pale green to white between expressions.
- bg c17_wall_face has a vertical right-hand edge where the water wall ends (corrected 2026-11-24 from metal panels); c17_dead_water's far wall is now a smooth band of grey water (taller than 'low'). cg c17_pit_city redone 2026-11-24: seen from the rim inside the pit; the Dragon in pit_view and pit_city now matches canon (pale hoops, blunt faceless prow). Weak: the hoops read a little like a spring or slinky and the head like a smooth egg; no panel seam visible.
- Crane (tidy, calm), Raske (eyes shut) and Yeva (plain, grave) reuse existing portraits.

## Maker architecture pass (2026-11-24, owner feedback: the drowned city was a flat village of huts)
Judged wrong and redone (nano-banana-2 edits, 8 images x $0.08 + 1 retry): cg c17_pit_city, bg c17_pit_view, bg c17_silt_street, cg c17_ilan_lamps, bg c17_square_silt, bg c17_square_flooded, bg c17_city_risen, cg c17_city_rises. Old versions: previous/*_flatmaker.png. Left alone: c17_the_way_through (low plain stone buildings in the background, small, people in front), c17_seating_ring (rough brick vault wall, an interior), c17_wall_faces (flat white blocks far behind a mural). Possible follow-up if the owner wants them.
Weak spots: the city reads somewhat classical/Ottoman (domes, drum towers, arched slits) more than strange; pit_city and pit_view show one compact complex, not an endless city; the lowered "classical column drums" in the street and square images are fluted but heavy.

## Maker pass 2 (2026-11-24)

- Maker pass 2 (2026-11-24): c17_the_way_through now has the tiered pale Maker city (fluted towers, ribbed domes, set-back terraces, spiral ramp) round the flooded square at dawn; c17_wall_faces shows the faces on tall curved pale Maker walls of light before the risen tiered city, broad white stair to the sea; c17_seating_ring and bg c17_vault_grey have smooth seamless bell-shaped pale Maker walls (seating ring: walls beginning to glow; vault_grey: dull, grey, unlit), the ring, wheels and raw steel frame unchanged. Old files in art/refs/ch17/previous/ (*_plain, *_brick, *_rock, *_blocks). Left as is: bg c17_vault_lit and cg c17_vault_light (already pale bell walls). Weak: in vault_lit the ring has rivets and the walls show only faint towers, not clear moving pictures.
