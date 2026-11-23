# Chapter 16 merge notes (art director, 2026-11-23). The lead merges these into the shared files.

## effects.rpy PORTRAIT_LIGHT (also in art/refs/ch16/light_additions.txt)
Copied from: kelder_day = c15_school_morning (grey, hard white light); kelder_evening = c15_harbour_sunset; saltgate_stacks = c14_girdle_saltgate; market_dry = c8_wet_market; sluice_dry = c8_sluice made lighter (it is grey day, not night); lock_box, barges_lantern, rafts_night = c9_barge_night; girdle_fleet, boat_stern = grey overcast (new, neutral); boat_stern_evening = warm dusk (new).
        "c16_kelder_day":       (0.94, 0.95, 0.94, -0.03, 0.92, 0.0),
        "c16_kelder_evening":   (1.00, 0.76, 0.64, -0.10, 0.86, 0.0),
        "c16_saltgate_stacks":  (0.96, 0.96, 1.00, -0.04, 0.92, 0.0),
        "c16_market_dry":       (1.00, 0.94, 0.82, -0.05, 0.92, 0.0),
        "c16_sluice_dry":       (0.90, 0.90, 0.94, -0.06, 0.90, 0.0),
        "c16_lock_box":         (1.00, 0.92, 0.80, -0.06, 0.92, 0.0),
        "c16_barges_lantern":   (1.00, 0.92, 0.80, -0.08, 0.90, 0.0),
        "c16_girdle_fleet":     (0.94, 0.94, 0.96, -0.04, 0.92, 0.0),
        "c16_boat_stern":       (0.94, 0.94, 0.96, -0.04, 0.92, 0.0),
        "c16_boat_stern_evening": (1.00, 0.82, 0.70, -0.08, 0.88, 0.0),
        "c16_rafts_night":      (1.00, 0.92, 0.80, -0.08, 0.90, 0.0),

## Reused (nothing new made)
- Backgrounds: dc_high_hall (s03 hall), dc_canyon_above or dc_canyon_lit60 (s03 canyon galleries, rippling), dc_sea_door (s03 rim), c15_harbour_sunset and cg c15_harbour_clear (s01 Port Halcyon harbour with the Stacks), c8_saltgate (Saltgate lock gates, if wanted).
- Portraits: Wrack p_wrack_thread_* (pleading, resolved, exhausted, ...), Okonta p_okonta_grave / flat (unsmiling, steady), Vey p_vey_cold / p_vey_tight (upright, reserved), Sefa p_sefa_thoughtful / shaken (troubled, honest), Maelis p_maelis_cropped_level / impassive (calm), Hesper p_hesper_stern (tight-jawed), Garran p_garran_accepting (steady), Corin p_corin_weary / grief for the quiet lines.
- Maelis: chapter 16 says "Her hair had begun to grow", so use the cropped set (cropped_level, cropped_impassive, new cropped_amused), not p_maelis_smile (long hair in a bun).
- Dace, Odile, Odo, Raske, Crane, Hanne speak nothing in ch16 or already have portraits; no new ones.

## art/canon.json "characters" (new)
- "Speaker of Kelder": {"fixed": "old mariner man of about seventy, long-limbed and thin, long narrow face, light brown skin, thin white hair combed back, small tired dark brown eyes with heavy lids, deep lines, a mild defeated face; faded plain grey-green sea-silk tunic with a round collar and a little button placket (looks are choices; text says only 'an old man with a mild, defeated face'); wears a numbered brass tag on a cord at the wrist (not drawn). Expressions: kelder_mild (base), kelder_considering.", "references": ["art/refs/ch16/portraits/kelder_base.png"]}
- "Senior Lockkeeper": {"fixed": "woman of seventy, weathered tan skin, deep lines, white-grey hair in a tight low bun, dark brown eyes, strong stern face; plain dark waxed canvas coat buttoned to the throat with a small brass badge on the chest worn smooth (text: 'a brass badge worn smooth'; coat is a choice). Expressions: lockkeeper_stern (base), lockkeeper_resolved.", "references": ["art/refs/ch16/portraits/lockkeeper_base.png"]}
- "Noodle-stall old man": {"fixed": "thin old man of about seventy, islander of Saltgate, weathered light tan skin, deeply lined kindly face, bald crown with thin white hair at the sides, short white stubble beard, warm brown eyes; dark cotton shirt, clean white apron, folded cloth over one shoulder (looks are choices). Expressions: noodle_kindly (base), noodle_puzzled.", "references": ["art/refs/ch16/portraits/noodle_base.png"]}

## art/canon.json (expression lists that grew)
- Corin: add corin_earnest (brows drawn up, eyes bright but no tears running, lips pressed and trembling, jaw tight; scars kept).
- Brask: add brask_wry (one mouth corner lifted, one brow raised, sidelong dry look; not a broad smile).
- Sefa: add sefa_laughing_crying (shaky open smile, tears on both cheeks, wet hair and tunic).
- Hesper: add hesper_eased (forehead smoothed, faint tired half-smile, eyes softened).
- Maelis: add maelis_cropped_amused (short cropped grey hair, small dry smile, eyes crinkled); canon note: after chapter 7 her hair is cropped and in chapter 16 is "beginning to grow"; use the cropped set.

## art/bible.md rows
- Kelder tank-town (c16): bg c16_kelder_day / c16_kelder_evening. Parallel concrete troughs behind the Waterline sea-wall, tin-roofed sheds at the near end, an iron sluice gate at the seaward end of every row, plain steel poles with hard white lamps on wires; evening: troughs empty and dry, gates hanging open and broken at the hinge, ordinary harbour water beyond. The text says only 'tanks', 'rows', 'sheds', 'lamps on wires', 'iron gates ... sawn through at the hinge' (shapes are choices).
- Saltgate with the water gone (c16): bg c16_saltgate_stacks (black stack bottoms hung with green dripping weed and barnacles standing on mud, city on stilts above, pale overcast), c16_market_dry (Wet Market basin a bed of mud with planking, stocked empty stalls, lamps lit), c16_sluice_dry (the Sluice canal a mud bed with a bicycle, the noodle stall open on the corner), c16_lock_box (senior Lockkeeper's box at the north gate: kettle, huge logbook, brass handle on a chain), c16_barges_lantern (gate barges resting on mud, lantern poles, night).
- The Girdle at the edge of the dead water (c16): bg c16_girdle_fleet (grey flat sea, thousands of boats, the wall as one long flat band in the west), c16_boat_stern (Dace's patchwork boat, red/yellow/blue/green planks, rays wheeling), c16_boat_stern_evening (lantern rings of boats in the evening), c16_rafts_night (plank rafts, lanterns, the wall a dim dark band with a line of mist on top). The wall is drawn as a very long, plain, flat-topped grey band standing a little above the sea; the deaf-water line is a sharp line across the surface, no drop.
- Illustrations: cg c16_kelder_exit (callers walking out to the open sluice, others waist-deep in the clean harbour), c16_okonta_corin (her hand flat on his forearm, hacksaw in his other hand), c16_choirs_answer (rings of light climbing the canyon tiers), c16_grey_wall (mariners at the dead-water line, wall beyond), c16_maelis_arrives (Maelis steps from a ray into the boat; Ilan in blanket, Sefa), c16_sefa_handful (a dome of warm gold water that keeps its shape), c16_sefa_asleep (asleep in the bows, hand trailing, gold ring), c16_garran_west (Garran with sleeping Pim on his shoulder, looking west).
- Choices where the text is silent: Speaker of Kelder, Lockkeeper and noodle man looks (above); mariners wear plain grey-green tunics; the rays are pale grey-white flat fish; the choirs are in white-cream robes; singer faces are tiny and read slightly young.
