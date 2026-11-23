# Art bible (chapter 1 pilot draft)

Status: draft for the owner. Not approved. Gates `style` and `cast` are still open.

## Style, in plain words

Anime style. Clean dark line art, soft flat cel shading, gentle natural colours. Characters are drawn full length, facing the viewer, on a plain light grey ground. Model: `flux-2-t2i` (fal-ai/flux-2), $0.024 per portrait. Chosen over two others because on the same Sefa prompt it kept the text's thin, long-limbed build and her curved hook; the others drew a fork and a shell (Seedream 4.5) or invented boots and leggings (Nano Banana 2). See `art/bakeoff/`.

Every character prompt starts with the same style sentence, saved in each image's `.txt` file beside it.

## Cast (chapter 1)

Fixed features come from the text (sentence ids from `work/units/ch01.txt`). Choices where the text is silent are marked **choice**.

| Who | From the text | Choices | File |
|---|---|---|---|
| Sefa | about sixteen, thin, long arms and legs, dark hair tied back with a strip of something that shone, large nearly black eyes, harvesting hook (c01.s01.p006.1-4); grey-green sea-silk tunic (c01.s02.p002.2) | sleeveless short tunic, bare feet, silver-white hair strip | `art/refs/ch01/sefa.png` |
| Wrack | heavy surface boots, torn grey jacket with a corporate crest half ripped away, raw red cable-tie marks on both wrists (c01.s01.p008.3); later a sea-silk tunic (c01.s03.p023.3) | age (adult), short dark hair, face, grey trousers and shirt, a blue shield-shaped crest (the crest's look is not in the text) | `art/refs/ch01/wrack.png` |
| Bother | like a seal built by someone fond of dogs; seal's sleek body and broad flippers; blunt square head; brown eyes set forward; small folded ears; whiskered grey muzzle; plaited cord collar (c01.s01.p005.2-5) | grey colouring | `art/refs/ch01/bother.png` |
| Elder Oro | very old, carved stick, bald brown head, gentle slightly amused look (c01.s03.p008.3) | brown skin read from "bald brown head", long loose tunic, bare feet | `art/refs/ch01/oro.png` |
| Ione | broad, calm, sleeves rolled, forearms ridged wrist to elbow with old shiny scars (c01.s03.p012.2) | brown hair, age middle | `art/refs/ch01/ione.png` |
| Davin | quiet, big-handed, slow smile, net-mender (c01.s02, c01.s04.p002.3) | short dark hair, tunic with trousers, a net in hand | `art/refs/ch01/davin.png` |

## Places (chapter 1)

Wide 16:9, same style, no people. From the text (sentence ids from `work/units/ch01.txt`); **choice** where the text is silent.

| Place | From the text | Choices | File |
|---|---|---|---|
| Kelp forest | trunks thick as a man's waist, colour of old brass, no branch; golden blades leaning one way; light green at the edges, gold in the middle (c01.s01.p003.3-5) | sandy bed, a few rocks | `art/refs/ch01/places/kelp_forest.png` |
| Terraces and dome | kelp in rows, raked sand, stone-walled terraces; hill-sized dome of pale smooth panes with seamless white ribs, kelp up one side, worn lower panes, lit on one side only, glowing yellow-green weed on the dark half (c01.s02.p001-006) | the dome reads as translucent pitted panes | `art/refs/ch01/places/terraces_dome.png` |
| Dry room | a room, stone floor, a bench (c01.s03.p001, p008.4) | lamp, plain wooden bench, wooden door; the text gives nothing else | `art/refs/ch01/places/dry_room.png` |
| Meeting hall | round, high; a pale smooth column floor to roof as thick as a kelp stem, no mark, polished at shoulder height, a wreath of fresh weed (c01.s04.p019) | stone floor, panelled walls, a skylight | `art/refs/ch01/places/meeting_hall.png` |

Wrack's second outfit, the sea-silk tunic (c01.s03.p023.3): `art/refs/ch01/wrack_tunic.png`. Made from his first sheet with the edit model; the face matches, the cloth does not shimmer.

## The Maker lamp (owner's design change)

The owner asked for a real, old lamp-like lamp, because mobile versions of it appear later in the story. Design in `art/refs/ch01/lamp/lamp_unlit.png`: a pale ivory metal column as thick as a man's waist, with ribbed collars, old bundled cables down one side, a caged glass lens housing near the top, a hairline seam at shoulder height (polished by touch), and the weed wreath. Dark when dead; the lens blazes white when it comes on. This replaces the earlier plain column that the source text described ("a smooth pale column from floor to roof... without a mark", c01.s04.p019.3, which the owner's cuts removed). Used in: `places/meeting_hall.png`, `cg/lamp_seam.png`, `cg/lamp_on.png`. Material matches the dome's white metal (c01.s02.p006.4). Two states of the hall: `places/meeting_hall.png` (lamp dead) until c01.s04.p022, and `places/meeting_hall_lit.png` (lamp on) from then on. The lamp stays lit for the rest of the game: every later scene in this hall uses the lit version.

## Known weaknesses

- Wrack's crest is whole, not half ripped away, and its lettering is garbled. Fix before it appears large.
- Skin tone is unstated for everyone but Oro. The model's default is pale for the others.
- Sefa is not clearly visible in the lamp-on illustration.
- The dome's panes look a little like glass. The text says "neither glass nor stone".
- The dry room has no hammock or fire; the text gives none.
- Expressions (see the manifest `needs`) are not made yet.

## Rejected attempts

`art/refs/ch01/rejected/`: Oro (pale skin although the text says brown), Ione (scars drew as open wounds), and first tries of the dome (a glass greenhouse on a grass mound), the dry room (bubbles in dry air) and the meeting hall (a crowd and a black column).


## Chapter 2 additions

New characters (head-and-shoulders portraits, `art/refs/ch02/portraits/`, cut-outs in `portraits_cut/`). Looks from the text (sentence ids from `work/units/ch02.txt`); **choice** where the text is silent.

| Who | From the text | Choices |
|---|---|---|
| Hesper | the hold's Tidecaller, "a lean hard woman whom people made room for" (c01.s04.p002.8); up close "younger than he had thought, forty perhaps", "a strong tired face and a caller's hands, which are chapped white to the wrist" (c02.s03.p004.3-4); at the burial a bundle on her back and a length of knotted cord round her wrist (c02.s04.p009.2-3) | dark hair pulled back, grey-green sea-silk tunic; reads a little older than forty |
| Okonta | "dark and grey-haired and spare, perhaps sixty, in a close suit the colour of slate. Thin pale scars ran from her temples down the sides of her neck and under her collar, as fine as if they had been drawn with a pen" (c02.s05.p003.3-4; the first sentence was cut because the picture shows it) | "dark" read as dark brown skin; short grey hair; high-collared slate suit |

New emotions for existing characters: Wrack (tunic) baffled, shaken, shivering, despair, resolved; Sefa fierce; Oro delighted; Ione pain.

Places: `places/dome_crown` (underwater at night, platform on the dome's crown), `dome_dark_half` (eleven dead lamps of the approved lamp design along the ribs), `net_racks`, `terraces_night` (a split over-and-under view: the barge floats ON the surface, upper hull above the waves, lower hull below, the dome far below), `terrace_wrecked` (also `terrace_dusk`, the same picture darkened, for c02.s05), `hall_day` (no windows: the hold is under the sea), `burial_kelp` (carved marks on the stems, deliberately not readable letters).

Illustrations (`art/refs/ch02/cg/`): `lamps`, `barge`, `gunboats` (three gunboats floating on the surface, waterline across their hulls; blue shield crest on the bows, the same crest I drew on Wrack's jacket in chapter 1: the text says "the Halcyon crest" without describing it), `burial`, `needle` (Okonta alone stepping off the pale needle; earlier tries with Wrack and Sefa kept duplicating Wrack).

Not shown in any image: the sludge's source ship details, the unnamed crew faces (rough).


## Chapter 3 additions

New characters (portraits in `art/refs/ch03/portraits/`, cut-outs in `portraits_cut/`; fixed features in `art/canon.json`; browse with `./vn art open`):

| Who | From the text | Choices |
|---|---|---|
| Brask | "a huge young man with a red beard, who wore a coat of sealskin with the fur inside in spite of the warmth of the water" (c03.s03.p009.2); an ice-diver of Rime; "a voice like a slab of something being dropped" (p010.2) | red hair, light skin, grey fur at the collar |
| The woman from Fallow | "a woman of about thirty", "a tired, flat, capable way of speaking" (c03.s03.p006.3 and nearby) | dark hair tied back, light weathered skin |
| The old man from Fallow | "an old man who lay propped against a bundle, breathing as though each breath had to be lifted" (c03.s03.p006.3) | thin white hair, deeply wrinkled |
| The diver officer | "an officer, by the stripe on her helmet" (c03.s03.p017.2), "even through the helmet glass he could see her go white" (p019.1) | about forty, cropped dark hair, blue shield crest on the shoulder (as on the Halcyon gunboats) |

New emotions: Okonta listening (eyes closed, c03.s01.p009.6); Wrack quiet awe.

Places: `kelp_night`, `tangle`, `sounding_ruin`, `slick_edge`, `greywatch_stone`, `gallery`, `cradles`, `ice_shelf`. Illustrations (`art/refs/ch03/cg/`): `needle_ride`, `moored_night`, `eel`, `dragon_arrives`, `dragon_head`, `sleds`, `whales`. The gallery is inside the Dragon, so no sky, horizon or land is ever visible through the bound water.

## Chapter 4 additions

New characters (portraits in `art/refs/ch04/portraits/`, cut-outs in `portraits_cut/`). Sentence ids from `work/units/ch04.txt`; **choice** where the text is silent.

| Who | From the text | Choices |
|---|---|---|
| Jef | "small", "older than anything Wrack had ever seen", "skin like paper that has been folded many times", "walked like a man whose feet hurt" (c04.s01.p039); apron and a jersey with a hole in the elbow (c04.s07.p303 area, c04.s08); "bright dark eyes" (c04.s07) | pale skin, bald with white tufts over the ears, brown wool jersey, brown leather apron |
| Maelis | "tall and straight and grey-haired", "a patched coat with the pockets full of something" (c04.s01.p053); in her seventies (world bible) | grey hair in a low bun, brown eyes, dark coat with brown patches |
| Anselm Rook | "perhaps seventy", "the face of a man who has been listened to for a long time", "thin pale scars ran down from his temples and along his neck", hard suit with "a helmet of clear glass" (c04.s07.p247-249) | broad build, white hair, grey-blue eyes, dark suit; the suit's collar is high and dark in the portraits |

New emotions: Jef grumbling, attentive, watching, annoyed, tired; Maelis examining, smile, silent, shut, composed; Anselm helmed, calm, gentle, smile, cold; Okonta smiling (into her cup, c04.s08.p343; the cup is not drawn); Wrack grieving (one tear; chapter 4 ends in grief).

Places: `well_lip`, `kettle_house`, `kettle_interior`, `workshop`, `lantern_exterior`, `lantern_hall`, `dark_hall`, `step_night`, `step_fog` (stingray silhouettes all facing one way, c04.s07.p241), `landing_dusk`. Surface scenes at the top of the world have no ripple (the water is "perfectly still"). Only the Lantern seen from outside is underwater.

Illustrations (`art/refs/ch04/cg/`): `well_star` (c04.s01.p009), `hands_lamp` (c04.s02.p079), `lantern_crown` (c04.s04.p137, nine domes after three tries: the model drifts to eight), `sphere` (c04.s05.p177), `anselm_unhelm` (c04.s07.p247; shown from behind, faint hills in the fog are a flaw), `tool_table` (c04.s08.p347), `jef_under_heart` (c04.s09.p467), `dragon_departs` (c04.s10.p495; the Dragon reads as a ribbed boat; faint hills behind).

The Well lip: the manifest and text mix surface and water (the shelf sits at the waterline, the jellies float over the gulf). Choice: drawn at the surface with a night sky.

## Chapter 5 additions

New characters (portraits in `art/refs/ch05/portraits/`, cut-outs in `portraits_cut/`). Existing characters gain expressions only; Sefa now wears a plain grey cloth band tied round her upper arm (the healer's band).

| Who | From the text | Choices |
|---|---|---|
| Elder Vey | "a tall, exact woman of seventy named Vey" (c05.s02.p012.6); "silver hair bound close to her head, and she sat like a person who has never in her life been seen to slump" (p012.7); later "a good deal older ... not standing quite straight" (c05.s04.p015.3) | deep sea-green high-collared robe with a shell-white collar band; light skin; grey-blue eyes |
| Aurel | "a quiet grey man named Aurel" (c05.s04.p008.2) | about fifty-five, close-cropped grey hair, tan-brown skin, grey-green tunic |
| Sefa (update) | "thinner ... grown" (c05.s02.p018.1-2); "a healer's grey band on her upper arm now, over a tunic that had been mended at the shoulder" (p018.3) | band is a plain grey cloth strip |

New emotions: Wrack grieving, resolved, fading (skin gone grey, c05.s03.p010.4), dazed, exhausted, stunned; Okonta frowning (c05.s01.p006) and grim (c05.s02.p010 "Her face had gone grim"); Sefa hard, tired, fierce, eyes filling (c05.s03.p011); Vey cold, shaken, tight-mouthed; Aurel calm, tired; Bother excited (c05.s02.p018.4-5).

New places (`art/refs/ch05/places/`):

| Place | From the text | Choices |
|---|---|---|
| Jef's workshop | the warm-stone open on the bench, "the old man's mug beside it and a ring of dried tea in the bottom" (c05.s01.p002.4); a dead air-heart "the size of a barrel" laid out in pieces (p003.3-4) | grey window light, the mug drawn with a stain only (the model drew tea in it twice) |
| Landing (evening) | "the ninth evening ... went down to the landing" (c05.s01.p011-012) | dusk sky; no needle cradles drawn |
| Open sea with ice shelf | "the grind of the ice shelf" (c05.s01.p020.10) | ice shelf seen from below, no Rime dome |
| Deep Chorus canyon | c05.s02.p006.1-9; "white light of the windows gave out" past the twentieth tier (p009), lampweed below (p010.1-2) | upper galleries white, lower dark with yellow-green weed |
| Canyon lit to the sixtieth tier | c05.s04.p012.1-p013.2 | boundary drawn at one tier; tier counts are not shown |
| High hall | c05.s02.p012.1-7 (vault of clear glass, green water like a sky, shell-inlaid wave floor, seven stone seats) | white lamps on short ivory posts |
| Service tunnels | c05.s02.p021.3 ("narrow tunnels behind the galleries, where the pipes ran") | pipes, stair, lampweed |
| Lowest dry halls | c05.s02.p022.1-8 ("long and low", "green dimness", "very still") | sleepers shown as small background figures |
| Heart-chamber | c05.s02.p030.1-9 (a vault, "the size of a house", "pale ribbed thing like a great closed shell", channels "thick as his body", "furred with a fine grey dust") | door with broken wax seal (p029.1) |
| Sea-door on the rim | c05.s04.p015.1 ("waiting at the sea-door on the rim"); world bible: a round pool in the floor | arch of glass onto the kelp forest; the Dragon is shown separately |

Illustrations (`art/refs/ch05/cg/`, game names `c5_*`): needle_ride (c05.s01.p020.3, p020.8), canyon (c05.s02.p006.2-9, no people), sefa_grips (c05.s03.p010.2-3), lamps_down (c05.s04.p012.1-p013.2), dragon_lights (c05.s04.p030, "lights along the Dragon ... thirty"; light count is approximate).

## Chapter 6 additions

New characters (portraits in `art/refs/ch06/portraits/`, cut-outs in `portraits_cut/`; all Threaded wear a close slate-grey high-collared suit and have thin pale scars from the temples down the neck):

| Who | From the text | Choices |
|---|---|---|
| Corin | "a big man" (c06.s01.p007.1, p008.1), "rubbed his face with a broad hand" (c06.s01.p015.1), "sitting in his net with his big hands hanging between his knees" (c06.s02.p029.1), taught Okonta to fly in kelp (c06.s01.p014.1) | about sixty-five, tan-brown skin, short curly dark-grey hair, grey stubble |
| The woman with the clay tube | "a woman of eighty with a face like a walnut, who sat cross-legged in a net and smoked something in a clay tube that made the water round her taste of cloves" (c06.s01.p003.3) | white hair in a low bun, brown-tan skin |
| The girl with the harpoon | "a girl who could not have been twenty, with a harpoon across her knees" (c06.s01.p003.3) | about nineteen, olive-tan skin, short black hair |
| The young man from Fallow | "the last Jef had made before Wrack, six years ago, and the scars at his temples had hardly faded" (c06.s05.p017.1) | about twenty-four, light skin, sandy-brown hair, grey-green tunic |
| Tam, the scarred woman on a dart, the eels | no portrait needed (no speech); eels per the canon Slick eel (eyeless) | none drawn |

New emotions: Okonta cold, wincing, flat (expressionless), defiant; Wrack tunic angry, ashamed, dejected, thinking; Sefa lip (lip between teeth), dry; Anselm lowered (private).

Places: `c6_gallery_failing`, `c6_gallery_stern`, `c6_gallery_nineteen`, `c6_heart_under`, `c6_kelp_gold_black`, `c6_slick_inside`, `c6_forest_beneath`. Illustrations (`art/refs/ch06/cg/`): `needles_asleep` (c06.s01.p002.1, p003.2-5), `anselm_cradle` (c06.s02.p004.1-4), `towed_slick` (c06.s03.p008.2, p009.2, p013.3-4), `wet_glass` (c06.s04.p013.5-6; Okonta on the needle), `heart_laid_out` (c06.s05.p008.2-3). Choices: the clay tube drawn as a slim pipe; Anselm's helmet drawn as a clear bubble with a throat grille; the figures round the heart are about three dozen, not exactly twenty-seven; Anselm's needle lies in the cradle only in the illustration (the gallery_stern background shows the cradle with a needle-shaped fitting and silt, a leftover of the chapter 3 cradle sheet).

## Corrections after the owner's review (2026-11-23)
- **Wrack's Thread** (chapter 4 on): a single thin pale line on the side of the neck, smaller than Okonta's. Portraits `p_wrack_thread_*` (15 emotions) replace `p_wrack_tunic_*` in the script from "He woke in the box bed" in chapter 4 onward.
- **Okonta:** frowning, grim and listening redone: they had no Thread lines and looked about fifteen years younger than the base portrait. Old versions in `art/refs/ch05/portraits/okonta_fix/rejected/`. Cold, flat, urgent and wincing have the lines but smoother faces; not redone.
- **Air-heart** (chapter 5, scenes 2 and 3): an ornate round sphere of white pearl plates, silver bands and gold filigree with a gold hinge seam, house-sized, on a stone cradle. This replaces the ribbed shell and is the owner's choice; the novel text still says "a pale ribbed thing like a great closed shell", which only the owner can change. New background `dc_heart_chamber` and six illustrations `c5_airheart_touch`, `reach`, `open`, `fingers`, `tool`, `breathes` (art/refs/ch05/airheart/).
- **Dragon lights** (c05.s04): thirty small needles with a light on each flank around a dark Dragon, not lamps on the ribs.
- **Transparent hair** fixed on the clay-tube woman and on Anselm (smile, helmed, lowered, gentle): chunks of white hair had been cut away with the backdrop; refilled from the uncut sources. Originals in `art/refs/ch06/portraits/rejected/`.
- **Jef:** the closed-eye portrait `p_jef_tired` redone without the dark sockets (plain thin lids, no shadow). The old one is in `art/refs/ch04/portraits/rejected/`.
- **Maelis carrying Jef** (`c4_dragon_departs`, c04.s10): Jef is a full-sized thin old man cradled across her arms, head back on her shoulder, eyes closed. The first version showed him as a tiny doll. The model drifts to child proportions when given a close-up portrait of Jef as reference; use words and a wider shot. The Dragon lies intact and calm with a faint blue light along its ribs (the novel says "long pale light"; blue is the owner's direction).
