# Chapter 18 merge notes (art director, 2026-11-23)

## effects.rpy PORTRAIT_LIGHT (donor place in brackets)
        "c18_meet_empty":        (0.84, 0.88, 1.00, -0.10, 0.86, 0.0),      # c12_tower_room (blue dusk, lamps)
        "c18_dragon_square":     (1.00, 0.98, 0.92, -0.03, 0.94, 0.0),      # c12_apron
        "c18_meet_market":       (1.00, 0.90, 0.86, -0.05, 0.92, 0.0),      # c8_market_low
        "c18_waterside_square":  (1.00, 0.98, 0.92, -0.03, 0.94, 0.0),      # c12_apron
        "c18_canal_table":       (1.00, 0.90, 0.86, -0.05, 0.92, 0.0),      # c8_market_low
        "c18_archive_workshop":  (0.80, 0.84, 0.92, -0.10, 0.86, 0.0),      # c7_control_hall_night, a little brighter
        "c18_terrace_lit":       (0.90, 0.94, 0.96, -0.10, 0.90, 0.0012),   # terraces_night, warmer (underwater, ripple)

## art/canon.json "characters" (all returning; expression lists grow)
- Wrack: add Thread expressions wrack_thread_nervous (brows lifted a little and drawn together, eyes glancing aside, lips pressed; c18.s04 walking with Maelis) and wrack_thread_trying (mouth a little open shaping a low note, eyes lowered and listening; c18.s03 learning the tending song). Masters art/refs/ch18/portraits/wrack_thread_nervous.png, wrack_thread_trying.png.
- Hesper: add hesper_warm (dry eyes soft and looking ahead and slightly up, mouth closed with the faintest lift at one corner, tired lined face softened; c18.s03 "It starts low. Listen."). Master art/refs/ch18/portraits/hesper_warm.png. Existing hesper_tired / hesper_raw serve "I haven't sung them since he died".
- Maelis: add maelis_sidelong (head turned slightly to the right, eyes cut sideways, one brow barely raised, mouth level; c18.s04 "She looked at him sidelong"). Master art/refs/ch18/portraits/maelis_sidelong.png. Use maelis_composed, maelis_examining, maelis_smile for the rest.
- Existing portraits to use in ch18: wrack_thread_calm / wry / resolved / attentive / ashamed; hesper_tired / hesper_raw; maelis_composed / examining / smile.
- No new characters. Hanne, Sefa, Ione, Garran, Raske, Crane, Odile, Bother and the clay-tube woman do not speak in ch18 (no portraits needed).

## art/bible.md rows
- Meet (c18): the Nine Towers city risen from the sea. bg c18_meet_empty (blue dusk, pale paving with a film of seawater, round glass street lamps on pale posts all lit, lit windows, nobody), c18_meet_market (ankle-deep high-tide street, canvas stalls, noodle stall with steam, washing from balconies, paper lanterns), c18_waterside_square (stepped quay, arcade, small boats, towels drying), c18_canal_table (canal, plain table with two stone basins, bench with grey blanket), c18_dragon_square (the Dragon lies still in a stone-edged channel in a paved square: smooth blunt head, hoop ribs dull and empty). Tidehall court, meeting hall and cracked dome reuse c12_tidehall_centre, meeting_hall_lit, dome_crown.
- Low Anthem at evening (c18): bg c18_terrace_lit, underwater: the dome glowing warm yellow all round, lamps on the terrace walls, white-glowing lampweed planted along the terrace wall.
- Archive workshop under the eastern quarter (c18): bg c18_archive_workshop. Silent stone hall, grey silt on the floor, half-built round air-heart (lower half pearl plates, silver band, gold filigree and hinge seam; upper half open ribs), parts laid out in rows, wall panels of glowing glass showing hands at work.
- Illustrations: c18_ribs_water (bright water running back through the Dragon's ribs; no people), c18_empty_cradle (flooded dock under the blank building, one empty cradle in a shaft of light), c18_terrace_song (Ilan and Hesper side by side before the lit dome, she sings to him), c18_archive_palm (Ilan from behind, right palm flat on a glowing panel, pictures of hands working), c18_this_sleeves (Ilan in profile, long sleeves rolled to the elbows, the small worn tool in his open palm, the half-built air-heart behind: the last picture).
- Choices where the text is silent: Meet's street lamps are round glass globes on pale stone posts; the Dragon lies in a stone-edged channel at the side of the square; Ilan wears the grey-green tunic with long sleeves; the archive silt is grey; the tool is the chapter 4 tool (curved silver blade, dark red-brown handle).

## Open points
- cg c18_terrace_song (5 tries): Ilan's mouth is slightly parted, not shut; Hesper looks about fifty, lined; the dome is cropped by the heads.
- cg c18_this_sleeves: a faint frown on Ilan; the tool is shown resting in the open palm, the blade is upright (text: he takes it out and rolls up his sleeves; the picture is the moment just after).
- cg c18_archive_palm: the second glass panel behind him shows a pale pearl sphere; his Thread line is faint from behind.
- bg c18_dragon_square and cg c18_ribs_water: the water is a strong mint green (same family as c12_apron). The Dragon head differs slightly from c15_dragon_ribs (smooth blunt hull-head, as in c14_harbour ref).
- Checked against chapter 17 on 2026-11-24 and redone: see 'Maker pass' below.
- Not made: the Dragon square with the nineteen lamp-holders (people), the Tidehall court with the board, Sefa at the canal table with queue (text narrates them; backgrounds are empty by rule).

## Cost
$1.40 for chapter 18 (37 calls, none failed; ledger sum).

## Maker pass (2026-11-24)
Meet is the risen Site Nine city, so its buildings were redone as tiered Maker architecture to match chapter 17 (nano-banana-2 edit, current image plus bg c17_city_risen as reference, 16:9, resized to 1920x1088). Redone: bg c18_meet_empty, c18_waterside_square, c18_meet_market, c18_canal_table, c18_dragon_square, c18_archive_workshop; cg c18_ribs_water, c18_archive_palm, c18_this_sleeves. Old versions: previous/*_oldmaker.png. Left: bg c18_terrace_lit (Low Anthem, human hold), cg c18_empty_cradle (Meridian's concrete dock). Dragon head is now a smooth seamless blunt prow. Prompts: new/*.txt (first-try prompts are in new/*.txt too; second tries in new/*_r2 files; a first batch came out square and was discarded, in new/square_try1/).
Weak: ribs_water far left/right edges stay ochre and flat-walled; canal_table left quay keeps some block joints; archive_palm now has fluted pilasters, panels unchanged; this_sleeves vault is Gothic-looking.
Cost this task: $2.00 (25 nano-banana-2 images, incl. 9 wasted on a square-format first try and 3 ring fixes).

## Maker pass 2 (2026-11-24)
Fixed with nano-banana-2 edits (current image plus c17_city_risen, 16:9, resized to 1920x1088; one try each): cg c18_ribs_water (edges now pale tiered Maker, shell domes), bg c18_canal_table (smooth pale left quay, no joints or moss), cg c18_this_sleeves (smooth shell-shaped Maker hall, no Gothic vault). Shell-and-heart lean recorded in art/bible.md. Old versions: previous/*_pass1.png. Prompts and raw outputs: new2/. Checked and left: bg c18_dragon_square, c18_meet_empty (framing still serves c18.s02 and c18.s01). Weak: minaret-like spires remain in the backgrounds not touched.
Cost this task: $0.24 (3 images).

## This_sleeves fix (2026-11-24)
cg c18_this_sleeves: air-heart redrawn as a pale ribbed shell, lower part closed, upper part only a few bare ribs, no cage, pearls, gold or filigree (world bible: 'a pale ribbed shell'); Ilan's face restored to calm and attentive using p_wrack_assured_calm as reference (mouth closed, faint soft smile, no frown). nano-banana-2 edits, 16:9, resized to 1920x1088, one try per step. Previous version: previous/this_sleeves_pass2.png. Prompts and raw outputs: new3/. Weak: the bare ribs are thin loops; the face has a very faint smile; the air-heart now differs from the pearl-and-gold air-heart in c5 images and bg c18_archive_workshop (still pearl and gold), which should be redone to match if the owner wants the shell look.
Cost this task: $0.16 (2 images).

## c18_this_sleeves, air-heart restored (2026-11-24)
The ribbed-shell air-heart in the pass 3 version contradicted the owner's choice in art/bible.md (corrections of 2026-11-23: pearl plates, silver bands, gold filigree). Restored the pearl-and-gold air-heart (reference c5_airheart_open) with Ilan's calm face from pass 3 kept. The windows now show a city and hills instead of hands at work. Shell-heart version kept in previous/this_sleeves_shellheart.png.
