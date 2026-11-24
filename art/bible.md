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

## Chapter 7 additions

Cutouts are in `art/refs/ch07/portraits_cut/`, copies in `game/game/images/p_*.png`. Everything faces the viewer's right.

New characters (memory scene c07.s05; all other new faces are the same people at another age or state):

| Who | From the text | Choices (text silent) |
|---|---|---|
| Nerys, Ilan's mother | "a mariner", "She had come up through the locks ... when she was nineteen", "drying out slowly", "She wore high collars and long sleeves" (c07.s05.p004.1, c07.s05.p005.2), speaks c07.s05.p005.2 | about forty, pale light skin, black hair in a low bun, large dark eyes (mariners are "long-limbed, with large dark eyes", world bible), plain dark high-collared dress |
| Adler Crane | "Ilan's own chief of security", "put a cable tie round Ilan's wrists", "said he was sorry, and seemed to mean it" (c07.s05.p019.2) | about forty-five, olive-pale skin, short brown hair grey at the sides, dark high-necked jacket |
| Anselm Rook at fifty | "a broad, square, quiet man of fifty in a high collar" (c07.s05.p011.3) | short dark hair going grey at the temples (he is white-haired at seventy-two), high dark collar covering the Thread scars, no helmet |
| Maelis, hair cut | "She had cut off her hair." (c07.s04.p005.2) | grey hair cropped close to the scalp, otherwise as before (patched dark coat) |

Not drawn (no speech): Tomas, young Ilan, the Meridian man, healers, the old ray with the notched wing.

New emotions: Sefa dismayed (the snow, c07.s01.p010.1), afraid (c07.s02.p015, "Her voice was small"), swollen (c07.s07.p009.2, "eyes were swollen and her jaw was set"); Maelis cropped grave / impassive ("no softness in her face, but no disgust either", c07.s06.p006.3) / level (telling Anselm's story). Wrack and Okonta reuse existing portraits (thread set for Wrack: troubled, resolved, grieving, shaken; Okonta: grave, sorrow, smiling for "nearly smiling").

Places: see canon_additions.json. Choices: the Bright Shelves "silverbacks" are drawn as small silver fish (the word is not explained in the text; a first try produced gorillas); Nine Spires is drawn above water as slender white towers with sailing boats; the Hush's lamp-less halls are black stone with shallow pools; the rays' ring over the Hush is the Wheel's look; the school classroom and Concord room are plain stand-ins (no looks in the text); the survey-ship chart shows only depth lines and small islands.

Illustrations (`game/game/images/cg/`): `c7_girdle_snow` (c07.s01.p007.1-8 "It fell past the walls without end", p010.2 "she put her hand flat on the bound water"; Sefa, Wrack seated, Bother), `c7_ray_eye` (c07.s02.p014.3-6 "The water in front of him rose slightly ... An eye like a dark lamp looked up at him"; Wrack and one ray), `c7_wheel` (c07.s03.p001.2-4, p002.1 "He was set at the centre of it, like a stone"; Wrack and about twenty rays, not hundreds), `c7_makers_faces` (c07.s05.p016.7-14, p016.9 "The walls turned to light"; Ilan in a grey diving suit and round-faced helmet with a lamp, in a flooded hall; glowing faces on the walls), `c7_sefa_leaves` (c07.s07.p006.2-4 "walked down the black sand into the water"; Sefa from behind, Bother, the house in fog).

## Chapter 8 additions

New characters (portraits in `art/refs/ch08/portraits/`, cut-outs in `portraits_cut/`):

| Who | From the text | Choices |
|---|---|---|
| Dace | "a long weather-beaten face ... a woman of fifty or so, with a pipe in her teeth and a hat tied on with string" (c08.s01.p006.1-3); "Driftfolk, out of Lashing" (p007.2) | grey-brown hair, tanned skin, patched olive canvas coat (text silent), clay-brown pipe |
| Yeva | "a long worn face and a dry manner" (c08.s06.p003.2); "grey hair moving" (manifest key moment c08.s05.p020); "tall once" (c08.s05.p020.1) | about sixty-five, olive-tan skin, long grey hair tied back, grey-green tunic (all choices) |
| Pell | "a thin, nervous young man ... a filing clerk at the port office" (c08.s05.p001.2) | about twenty-five, pale skin, dark-brown hair, grey jacket and tie (choices) |
| Linnea Marsh | "a physician ... plain raincoat, with no guard" (c08.s07.p013.2; c08.s05.p004); she trained eleven years and spent thirty more (p016.2-3) | about sixty-five, short grey hair, light skin, dark raincoat collar turned up |
| Garran | "a big slow man with a broken nose" (c08.s07.p006.2-3) | about forty, tan skin, short dark hair, stubble, sleeveless work shirt with a rope |
| Pim, the old noodle-stall man, the stoker, the four guards | no speech: no portrait | Pim appears only in the illustration c8_porter_child as an unconscious girl of four or five (c08.s07.p006.3) |

Wrack in chapter 8 (outfit follows the text): tunic with the Thread line (text gives no change) plus the hat Dace brings (c08.s01.p010.3 "you'll want a hat"; the hat's look is a choice: plain soft dark-grey, short brim); the suit in the Brightwater lobby (c08.s05.p012.1 "a suit that Dace had procured": dark charcoal business suit, white shirt, loosened tie, a choice). The Thread line stays visible in all of them.

New emotions: Sefa sick (c08.s02.p004.1 "was sick"), Sefa eager (c08.s06.p008.4 "nearly bursting"); Wrack wry, straining (c08.s06.p008.1-3), hat guarded, hat melancholy, hat calm, suit cool ("cool and bored and faintly threatening", c08.s05.p013.2), suit sorrowful ("I'm sorry", c08.s05.p020.5). Sefa awed/amazed, tearful (eyes_filling) and Okonta use existing portraits.

Places (`art/refs/ch08/places/`, game names `c8_*`): see canon_additions.json. Choices: no readable text anywhere (poster has blank bands, signs are abstract shapes); the Saltgate stacks are tall black spires with a few coin or bowl shaped signs; Brightwater sign is a blue drop and a smiling sun; "orphan water" tank is a plain glass cylinder with a metal lid.

Illustrations (`art/refs/ch08/cg/`): `dace_boat` (c08.s01.p006.1-3, "It was painted four different colours"), `yeva_tank` (c08.s05.p020.1-4, "She was in a tank"; one arm tube visible only; she reads younger than her portrait), `cupful` (c08.s06.p011.1, p013.1-3: Ilan waist deep, Dace on the planking with her foot in the water; the canal water reads bright green), `porter_child` (c08.s07.p006.3-p007.1, "Sefa held out her arms"). The Eye (c08.s02.p002.8-9) and Saltgate (c08.s03.p003.1-9) key moments and the Wet Market basin (c08.s04.p002.1-7) are backgrounds, not illustrations.

## Chapter 9 additions

New speaking characters (portraits in `art/refs/ch09/portraits/`, cut-outs in `portraits_cut/`, game copies `p_<name>.png`):

| Who | From the text | Choices (text silent) |
|---|---|---|
| Teodora Raske | "chief designer ... twenty-two years", "came up from the fitting sheds, the daughter of a riveter" (c09.s02.p001.1, p002.1); "looked at him ... over her spectacles", "took the spectacles off" (c09.s02.p009.4, p010.2); "sixty years old ... her hand was shaking" (c09.s02.p016.2) | short grey bob; light skin; dark work jacket, white shirt; ink stains on cuffs and collar (the manifest says ink on cuffs); steel spectacles; brown eyes |
| The hull man | "a hull man, grey and stooped" (c09.s03.p003.2), sat down on a coil of rope (p007.2) | about sixty-five; grey hair, goatee; dark work coat |
| The woman from engines | "a woman from engines with burn scars on her hands" (c09.s03.p003.3), "held her scarred hands to it, as one does to a fire. Her face crumpled" (p004.1-2) | about forty-five; dark brown hair pinned back; light olive skin; dark work smock; scars drawn subtle (same skin colour) because fal's filter refuses strong scar wording |
| The fat old man in the striped jersey | "A fat old man in a striped jersey ... shouting numbers" (c09.s05.p004.3), "brass trumpet under his arm" (p025.1), "looked at Ilan unhappily" (p026.4) | about seventy; white hair and stubble; blue and cream striped jersey; trumpet not drawn in the portrait |

The young draughtsman and the two apprentices never speak and have no portrait. Dace (introduced in chapter 8; base portrait by chapter 8's art) gets two new expressions here: `dace_questioning` ("Where to?", "What do you want there?", c09.s01) and `dace_grave` ("It's what we're for", c09.s05); both made from `art/refs/ch08/portraits/dace_cheerful.png`. Sefa gets `sefa_shouting` ("Less! Ask for less!", scene c09.s04). Okonta, Wrack and Sefa otherwise reuse existing portraits (okonta_urgent/grave, wrack_thread_resolved/frightened, sefa_fierce).

Places: bg `c9_lock_rain`, `c9_keelhaven_night`, `c9_coal_wharf`, `c9_design_loft`, `c9_raske_office`, `c9_net_loft`, `c9_ferry_stage`, `c9_tug_storm`, `c9_eye_tugs`, `c9_lashing_water`, `c9_barge_night`, `c9_soup_barge`. Saltgate's lock and the Eye are drawn new (chapter 8's own backgrounds were not yet final). Lashing's "mat of stormgrass" is drawn as a dark green leafy weed (choice). Slip Nine is drawn at the coal wharf as a ribbed hull with a square void (c09.s01.p014.2-5). Warm-stone is drawn as a smooth dark egg-shaped stone (text: "a smooth dark ovoid on a stand, the size of a loaf"); the loaf size is read as about twenty centimetres.

Illustrations (`art/refs/ch09/cg/`, game `cg c9_*`):
- `c9_warm_stone` (c09.s02.p015.1, p016.2): Raske's hand over the glowing stone. Raske alone.
- `c9_engine_woman` (c09.s03.p004.1-2): the woman from engines with her hands to the glowing stone on the barrel. She alone.
- `c9_tug_bow` (c09.s04.p007.4-p008.2): Ilan in the bow in black rain; the 300 people behind him are not drawn (the model duplicated him). Plain tunic; his Thread neck line is not visible in this frame (the fal filter refused the Thread-line reference).
- `c9_needle_road` (c09.s04.p004.4): the silver needle sweeping the road at head height. Okonta lies on it (text: "Okonta took the trucks"; riding the needle is a choice from earlier chapters); trucks skid aside, nobody dead.
- `c9_teaching_deck` (c09.s05.p006.1-6): Ilan teaching engineers in yellow oilskins on the barge deck. The audience is about 100 to 150 drawn, not 300. Ilan holds one small dull lamp. Hair of the audience is varied on purpose; the first try gave everybody Ilan's black hair.

## Chapter 10 additions

Portraits. Odo is the "fat old man in the striped jersey ... with his brass trumpet" of c09.s05, named here ("The trumpet-man's name was Odo", c10.s01.p002.1). He reuses chapter 9's `fatman_unhappy`; new: `fatman_firm` ("Nobody's handed back. That means nobody lays a hand on him", c10.s01.p003) and `fatman_weary` ("He wiped his neck", c10.s01.p003.5; a pale cloth at the neck is the choice). Dace: new `dace_angry` ("He had you thrown off a ship with your wrists tied!", c10.s01.p007) from `art/refs/ch08/portraits/dace_cheerful.png`. Sefa: new `sefa_shaken` ("I felt it go", c10.s04.p002; eyes lowered, no tears, a choice). Rook (`anselm_smile` glad, `anselm_calm`, `anselm_lowered` tired, `anselm_gentle`), Raske (`raske_stern`, `raske_steady`), Okonta, Wrack (thread set) reuse existing portraits. Dace's aunt never speaks: no portrait.

Looks and choices. Rook is shown as in ch4: white hair, dark high-collared coat (c10.s02.p009 "the square calm face"; the coat is in the manifest needs; text silent on cut, choice: plain dark coat with a high collar). The afterdeck: iron grating floor with the sea below (c10.s02.p002.2-4), rusted frigate, painted-over name (not shown, no text); table, two chairs and one lantern are choices (text: "the table", "a chair", "lantern light"). Dace's aunt (c10.s02.p008.1 "mouth shut like a purse"): about sixty-five, related to Dace but older, headscarf, apron (text silent). The governor (c10.s03.p011.2 "no bigger than a plum stone, pale and ribbed"): small ribbed pale stone; the water ring (p013-p014 "a ring as high as a finger") shown in a plain white bowl. The scrip (c10.s03.p047 "a square of scrip") is drawn as a plain blank pale slip: no numbers, because the first try drew a readable banknote.

Backgrounds: c10_planking (c10.s01), c10_frigate_deck (c10.s02-s03), c10_frigate_overturned (c10.s04.p001 "the overturned chair"), c10_lamps_swell (c10.s03.p040 "the lanterns of the raft-town ... forty white lamps"), c10_storm_wall (c10.s04.p027.2 "the wall of the storm stood up all round the Eye, and the gale skates were going over"). None is underwater: no ripple.

Illustrations (`art/refs/ch10/cg/`): `rook_rail` (c10.s02.p003.1-6 "Anselm Rook was standing at the rail ... simply an old man who was glad"), `bowl` (c10.s03.p011-p014 "The water drew back"), `rail_sefa` (c10.s04.p027.1-2 "He sat down on the deck, with his back against the rail. Sefa sat beside him"; Bother at her feet), `scrip` (c10.s03 last paragraph "Then she picked it up with the tongs and dropped it through the grating").

Known flaws: in `rail_sefa` the deck is plank wood, not the grating, and birds fly over the storm wall in place of gale skates; in `bowl` the men look at each other more than at the bowl; in `scrip` the paper slip has spray and is not crisp; the storm wall in c10_storm_wall reads as a crater.

## Chapter 11 additions

New speaking character: the old caller of Fallow ("The old caller of Fallow had come to the middle of the valley. He knelt, and put his palm flat on the sand", c11.s04.p007.2; "got up, with a hand on his knee", c11.s04.p007.6). Age, skin, hair and the grey-green tunic are choices (text silent): about seventy, weathered tan skin, short white hair and goatee. The portrait also shows faint scar lines on the cheek and neck (the model added them; the text does not say he is Threaded). Portraits: fallowcaller_puzzled ("puzzled, like a man who has come home and found the house moved", c11.s04.p007.6), fallowcaller_wet ("When he opened them they were wet", c11.s04.p007.2).

The grey-lipped youth ("The young Threaded from Fallow", c11.s01.p001.1) is drawn as the young man from Fallow of chapter 6 (same identity assumed; text silent on whether he is the same person). New expression `fallowyoung_exhausted` ("He had not slept, he said, since the forest", c11.s01.p002.3). Grey lips are only faintly drawn.

New expressions for returning characters: Corin `corin_pitying` ("something nearer to pity", c11.s04.p004.1). Hesper `hesper_cold` ("quite softly", c11.s05.p005.1; "So that's how it's done", c11.s05.p003.4) and `hesper_stricken` ("something in her face flinched", c11.s05.p011.1; "She had known Sefa from the day she was born", c11.s05.p013.1). Hesper is only drawn a little thinner ("She was thinner, and the cord was on her wrist", c11.s05.p002.1); "burned dark" is NOT in the text and is not drawn. Sefa `sefa_puzzled` ("She frowned", c11.s03.p006.1) and `sefa_understanding` ("he saw her understand. She did not cry", c11.s03.p007.3-4). Wrack `wrack_thread_cold` ("When there was nothing left in him but an order", c11.s02.p028) and `wrack_thread_pleading` (Ilan: "Hesper. Don't."). Wrack stays in the plain grey-green tunic with the Thread line. All other emotions reuse existing portraits (frightened, dazed, grieving, dejected, okonta_flat/urgent, sefa_fierce/eyes_filling/hard). Nobody speaks for the Meridian sailor boy, the woman from Fallow or Tam: no new portraits (the woman uses fallow_woman_*).

Places: the Eye uses the existing `c9_barge_night`. New underwater valley backgrounds `c11_valley_gold` (c11.s02.p002-p004), `c11_valley_brown` (brown curtain, c11.s02.p010-p012), `c11_valley_silent` (after the order, s03, s04), `c11_valley_dusk` (s05), `c11_valley_night` and `c11_valley_morning` (s06). Choice: the valley is a pale-sand dip between brass-coloured kelp; a faint chain of pale ovals sits in the far dark of `c11_valley_night` (a stray model detail); `c11_valley_dusk` shows a rippling surface at the top (the kelp is tall).

Illustrations (art/refs/ch11/cg/): `youth_falls` ("The young Threaded from Fallow came into the Eye two nights later, on a dart, and fell off it at the barge rail. Okonta had him out of the water", c11.s01.p001-p002; Okonta and the youth only; the dart is drawn as a pale plank-like needle; no lantern-rail Eye storm). `twelve_hulls` ("Twelve hulls went under in the time it takes to shut a door ... the white transports opened along their keels like pods", c11.s02.p033-p034; the ships are cracked and sinking in bubbles rather than flattened; the people are small and unnamed). `sefa_hands` ("Sefa had gone to the boy on the float ... put her hands into the sea beside him and go still. Nothing happened", c11.s03.p005-p007; Sefa and the sailor boy only; the boy is drawn shouting, not coughing; her belt is a model addition). `hesper_valley` ("She came down alone into the valley. She was thinner, and the cord was on her wrist", c11.s05.p002; Hesper only, yellow-green lights behind her). `sit_row` ("He sat down at the end of the row. After a while Sefa came and sat beside him ... leaned her head against his shoulder", c11.s06.p004-p006; the dead on low sleds are drawn small and faceless; Wrack's Thread line is barely visible). Not illustrated: Okonta walking the rows (c11.s04.p002), because the cap is five.

## Chapter 12 additions

New speaking character: Odile, speaker of Nine Spires ("a brisk, handsome woman of fifty named Odile. She had the air of a person with a great many lists", c12.s01.p008.2-4; "her eyes cooled", c12.s01.p009.4). Skin, hair, eye colour and the pale blue-green island-cut sea-silk are choices (text silent): warm tan skin, dark brown hair with grey streaks in a low knot. The sea-silk is "cut in island fashions" (c12.s01.p007.1). Portraits: odile_brisk, odile_cool (the change is subtle: level, flat mouth). She is the Moot's chair at c12.s02.p007 on.

Hanne is the woman from engines of chapter 9 ("The woman from engines was another. Her name was Hanne", c12.s01.p001.5) and keeps the enginewoman portraits (guarded, weeping). New expression hanne_awed ("The engineers lined the rail and said nothing at all", c12.s01.p004.9; "There's nowhere to hide", c12.s01.p005.1); the mouth is a little more open than the text needs.

Returning characters reuse existing portraits (no new expressions): Ione (calm, grave; the "scarred forearms" c12.s02.p041.2 are not drawn in a portrait because a head-and-shoulders crop cannot show them and the filter rejects scar references), Hesper (cold for "without any expression", c12.s02.p023.2; stern, stricken; "looking at her own hands" c12.s03.p007.3 has no portrait), Brask (gruff, watchful), Elder Vey (cold, tight), Aurel, Okonta (grim, grave), Sefa, Dace, Wrack in the thread set. Teodora Raske keeps the ch09 raske portraits. Wrack stays in the grey-green tunic with the Thread line.

Places: `c12_shelves_deck` (c12.s01.p004, glass coral chiming, nine towers ahead), `c12_apron` (c12.s01.p007-p008: "nine Maker towers ... stone aprons ... Driftfolk rafts"), `c12_tower_room` (c12.s01.p015 "a room high in the eastern tower, with a window on the sea"; the model added lamps along the sill), `c12_tidehall_centre` (c12.s02: "a bowl sunk into the white sand ... terraced all the way round in tiers of the pale stone", p003.3-4; the holds are drawn as small square openings), `c12_tidehall_rim_dusk` (c12.s04, "on the rim of the bowl, in the last of the light"; drawn underwater, since the Hall is ten metres deep; the bowl is cut by a gap in the middle of the image). Existing backgrounds to reuse: c7_nine_spires for the towers from far away. The text never says the Hall stands in the open sea, so ten metres of water is the choice. No crowded-tiers background was made (backgrounds hold no people); use tidehall_centre.

Illustrations (art/refs/ch12/cg/): `tug_shelves` ("The sea was a pale green so clear that the tug seemed to hang in air", c12.s01.p004.4-6; about a dozen engineers on the rail in dark smocks; sailing boats on the horizon come from the tower reference; the nine towers read as seven). `alone_sand` ("Ilan swam to the centre of the bowl", c12.s02.p017.1; Ilan alone, seen from behind, the Thread line not visible from this angle). `swell_ring` ("They made a ring around him on the white sand", c12.s03.p001.3-4, "He stood still", p003; about eighteen callers, not three hundred; they wear plain pale blue robes and hair colours vary, not Hesper or Aurel specifically). `swell_shelves` ("A swell rose at the centre of Tidehall ... rolled outward ... the glass coral chimed", c12.s03.p006.1-2, p007.1-3; the Hall is drawn as a ring of white terraces just above the sea, which it is not: the text places it under the water). `raske_lamp` ("Teodora Raske was sitting cross-legged on the stone with a lamp in front of her. A ring of mariners sat around her, forty or fifty of them", c12.s01.p015.6-7; drawn from above and behind, so her face and spectacles are not seen).


## Chapter 13 additions
New speaking characters: Marit Coyle (silver eyeshadow on the upper lids stays readable when small; oilskin then charcoal blazer), Caspar Venn (silver temples, charcoal suit), Bertil (heavy build, high buttoned collar), the Meridian captain (cropped brown hair grey at the sides, plain grey tunic). Dace gets dace_shy. Skin, hair and age of all four are choices (the text is silent). Ilan stays in the grey-green tunic with the Thread line in the studio illustrations (the text gives him no other clothes). Places (rain or indoor, no ripple): `c13_tolla_village` (grey rain on a crag, tiny terraces, shrine at the top), `c13_tolla_shrine` (wet dark rock, carved robed woman with very large eyes, offerings), `c13_tolla_loft`, `c13_tolla_quay_night`, `c13_concord_street` (pale stone, real trees with brass plates, glass towers, giant screens with a burning freighter, dusk), `c13_spire_exchange` (slender glass tower over a blank windowless block), `c13_spire_lobby` (deep blue marble), `c13_makeup_room` (mirror ringed in bulbs), `c13_studio_one` (white desk, glass wall over clouds, camera with a red light). Known flaws: cg c13_floor_manager shows about ten soldiers where the text says eight; c13_green_wave reads as a straight dam-like wall; marit_white reads a little angry; venn_* and bertil_quiet have a flat bottom edge at 90% of the image height (check under the dialogue box).

## Chapter 15 additions
New: the man in Meridian grey (greyman_level; looks are choices), Pim (child, no portrait), new expressions garran_pensive and crane_unsteady. Places: `c15_harbour_sunset` (Port Halcyon caldera harbour: black volcanic walls, Waterline refineries in brown haze with flares, tiered grey tenements, white houses on the lip, about forty tilted grey warships, smoke on the east head), `c15_school_morning` / `_afternoon` / `_dusk` (worn grey schoolroom, green blackboard with abstract chalk, crayon ship drawings pinned along the wall, small desks pushed back, blankets on the floor, big window onto clear green harbour water; the text does not describe the room, so this is a choice). Illustrations in art/refs/ch15/cg/. Known flaws: c15_okonta_brow shows the fist raised, not landing; the three school views are separate generations so the window and blackboard move; the blanket pile reads as bedding.


## Chapter 14 additions
All characters return; new expression portraits made from existing masters: raske_fierce, okonta_shouting, corin_weary, hesper_raw, hesper_broken (quiet, realistic; Hesper's tears are the only wet-eyed ones). Everything else reuses the chapter 4 Wrack Thread set, sefa_fierce and the existing Okonta, Corin and Hesper portraits. Places (above water, no ripple): Concord lobby and avenue, open sea at sunrise, Saltgate from the sea, Port Halcyon caldera (Waterline, Stacks, Rim in three bands), the 200 m wave, the refinery quay, the harbour with the fleet and the unfinished grey hull, the harbour water. Choices where the text is silent: the wave stands beside a brown volcanic cliff with an arch; the warships are drawn with guns; Crane's grey coat is long and plain; Ilan's tunic is grey-green, bare feet; the first beam is a white line with a steam column. The Dragon's head is a smooth faceless pale hull-head followed by hoop ribs, as in chapter 4. Known flaws: see art/refs/ch14/merge_notes.md.


## Chapter 18 additions
No new characters. New expressions: wrack_thread_nervous, wrack_thread_trying, hesper_warm, maelis_sidelong. Places: Meet at dusk, market street, waterside square, canal table, Dragon square (stone-edged channel), Low Anthem terrace at evening (underwater, ripple), archive workshop (silent hall, grey silt, half-built air-heart). Illustrations: c18_empty_cradle, c18_ribs_water, c18_terrace_song, c18_archive_palm, c18_this_sleeves (the last picture: Ilan in profile, long sleeves rolled to the elbows, the small worn chapter 4 tool in his open palm). Choices where the text is silent: Meet's street lamps are round glass globes on pale stone posts; Ilan wears the grey-green tunic with long sleeves; the archive silt is grey; the tool has a curved silver blade and a dark red-brown handle. Known flaws: see art/refs/ch18/merge_notes.md (terrace_song: Ilan's mouth parted, Hesper reads about fifty; this_sleeves: faint frown; check c18_meet_* against chapter 17's Meet art).


## Maker architecture (2026-11-24)
The common look of everything the Makers built, checked by viewing c5_airheart_open, dc_heart_chamber, lantern_exterior, c4_lantern_crown, c7_nine_spires, c12_apron, c15_dragon_ribs and c17_vault_lit: milk-pale glass-stone and pearly pale metal (pearl plates and silver bands on the air-heart, white glass cages on the Lantern); smooth, flowing, seamless surfaces with no bricks, no rivets, no rust; ribbed shells and domes (the Lantern's nine ribbed glass domes, the heart's banded shell); tall fluted towers with long vertical ribs that taper to slender tips (Nine Spires); hoops and ribs for structure (the Dragon); curving walls, broad white stairs; light from within. Plain-reading choice: a Maker city is vertical, stacked in set-back tiers and terraces linked by spiral ramps and broad stairs, topped by ribbed shell domes and fluted towers with a soft pearly bulge near the tip, with long thin window slits instead of ordinary windows (text: "tier came after tier, and street after street", "a broad white stair"; the details are choices). Dull, dusty and silt-drifted when dead; blazing white when risen. Never: low rounded huts, plain flat obelisks or slabs, brick, rust. Rust belongs only to the human drilling platform.

## Chapter 17 additions
New character: the Hush healer (looks are choices). New portraits: rook_old_* (Anselm Rook at ninety), hush_healer_gentle/steady, corin_calling, hanne_wondering. Places and choices (from the art director's notes, art/refs/ch17/merge_notes.md):
- The dead water (c17): bg c17_dead_water. Flat, still, dull grey-green sea under an even grey sky, a low wall of grey still water on the horizon (the held sea, see next entry). The text gives no colour ("clean", "told not to listen"); grey-green is a choice. Healed water is a soft sea-green (the model drew it neon in several images; kept as is, see open points).
- The wall (c17): The wall is HELD SEA WATER, not stone, rock, metal or glass (c17: "sixty metres of sea stepped forward", "as smooth as poured glass, and it made no sound", "the wall let go"). Draw it as smooth, grey, still, glassy standing water: sheer, no seams, panels, cracks or rock layers; foam only along the top edge where it meets sky and sea; mist at the foot. Sixty metres high. bg c17_wall_face; bg c17_road_barges and c17_dead_water show it far off; seen from the inside as a ring of grey glassy water with the open sea over its top edge in bg c17_pit_view and cg c17_pit_city. (Corrected 2026-11-24: the first versions drew it as quarried rock and grey metal panels; old files in art/refs/ch17/previous/.) The pit eighty kilometres across: mud plain, dead fish, a six-legged rusty platform, the drowned Maker city (a vast tiered complex, six or seven set-back terraces with spiral ramps, stairs, ribbed shell domes and fluted towers, dull, dusty and half buried in grey silt, the platform on its upper terrace), the Dragon coiled round the central hall with its ring of hoops for ribs (Dragon design from c15_dragon_ribs).
- The Dragon in chapter 17 (c17_pit_view, c17_pit_city): dull PALE metal hoop ribs with grey silt on them, one behind another in one long line curving round the central hall, tapering to small hoops at the tail; NO flesh, scales, spines or black spiny tail; head a smooth blunt pale prow with NO eyes and NO mouth. The bright bound water is gone from it. (Fixed 2026-11-24: the earlier versions had a silver sharp-pointed head, a spiny tail, a dark body and an eye glint; old files in art/refs/ch17/previous/.)
- Silted city street and square (c17): sheer tall tiered Maker walls and fluted towers many storeys high on both sides, their upper storeys lost in mist, grey silt drifted at their foot; slender pale-metal lamp-posts that light as Ilan passes (bg c17_silt_street, cg c17_ilan_lamps); square with the rusty platform on six legs (the text says "six rusty legs"; deck and railing are a choice) ringed by stepped Maker terraces with curved parapets in the foreground (bg c17_square_silt, c17_square_flooded). Redone 2026-11-24: the first versions drew low rounded mud-coated huts and blocks (owner: wrong; old files in art/refs/ch17/previous/*_flatmaker.png).
- Vault of the Ring (c17): round chamber like the inside of a bell (no bell object), ring of pale metal forty metres across flush in the floor, two wheels in a raw steel frame at the centre, three open doorways at the top of a stair, a bench with pinned drawings; the lit version has glowing walls with soft unreadable pictures of towers and steps (the text: the pictures show the city, the quarrel and the fall; only the first and last, the happy city, are drawn).
- The risen city (c17): the Maker city seen risen, tall and tiered: fluted white towers with pearly bulges and slender tips taller than the Spires, ribbed shell domes, stepped terraces, spiral ramps, water pouring in white cataracts down stairs and out of doors, a broad white stair going straight down into the clear sea, half dry and half under water (bg c17_city_risen, cg c17_city_rises). Redone 2026-11-24: the first versions drew plain flat obelisk slabs.
- Choices where silent: the Hush healer's looks; Rook at ninety wears a plain pale open-collared shirt (the text: "in his shirt"); Maelis keeps the very short grey hair of her ch10+ portraits (text: "You've cut your hair"); the two rowers and the docker's wife in c17_barge_rows (weathered tan skin, headscarf); the welder (short dark beard) and the net-mender (headscarf, tan skin) in c17_hands_reach.
Known flaws: see the Open points in art/refs/ch17/merge_notes.md (neon-green healed water; c17_wall_climb now shows three needles (redrawn again 2026-11-24 by the owner's request): Okonta in front with an engineer behind, Ilan alone in grey-green tunic and bare feet (the text: "Ilan rode alone"), Corin with an engineer behind; the text says thirty, three is the owner's choice; c17_vault_light Rook reads as kneeling; scar lines faint on three Rook portraits).


- Maker pass 2 (2026-11-24): c17_the_way_through now has the tiered pale Maker city (fluted towers, ribbed domes, set-back terraces, spiral ramp) round the flooded square at dawn; c17_wall_faces shows the faces on tall curved pale Maker walls of light before the risen tiered city, broad white stair to the sea; c17_seating_ring and bg c17_vault_grey have smooth seamless bell-shaped pale Maker walls (seating ring: walls beginning to glow; vault_grey: dull, grey, unlit), the ring, wheels and raw steel frame unchanged. Old files in art/refs/ch17/previous/ (*_plain, *_brick, *_rock, *_blocks). Left as is: bg c17_vault_lit and cg c17_vault_light (already pale bell walls). Weak: in vault_lit the ring has rivets and the walls show only faint towers, not clear moving pictures.

## Chapter 16 additions
New speaking characters: the Speaker of Kelder, the Senior Lockkeeper, the noodle-stall old man (looks are choices; the text is silent beyond the quoted phrases). New expressions: corin_earnest, brask_wry, sefa_laughing_crying, hesper_eased, maelis_cropped_amused. Places: Kelder tank-town (day, evening), Saltgate with the water gone, the Girdle at the dead-water edge; eight illustrations in art/refs/ch16/cg/. Choices where silent: grey-green tunics, pale grey-white rays, cream choir robes. Known flaws (art/refs/ch16/merge_notes.md): c16_kelder_exit is a wide far view of small adults with no brass tags and a youthful look, on the wall-top not climbing out of troughs; c16_sefa_asleep has both arms hanging into the water; the wall in c16_grey_wall and c16_girdle_fleet is a plain slab with visible ends; a few neon signs are still faintly lit in c16_saltgate_stacks; hesper_eased reads as a half-smile.

## Staging pass, group a: new images

Illustrations (art/refs/stage_a/cg/) and backgrounds (art/refs/stage_a/places/). Choices are marked **choice** where the text is silent.

- `c1_night_crew` (c01.s03 night-crew talk about Jef, "lying in his hammock in the dark hall with the others talking round him"): Wrack in a hammock, six villagers in grey-green tunics, a boy who calls out, an old woman with her fingers raised in the small sign. Jef and the Dragon not shown. **choice**: brown skin and mixed ages for the crew; stone hall, one low lamp; a few others also raise fingers.
- `c2_oro_lamp` (c02.s04 "They found him in the meeting hall, under the lamp, with his stick across his knees. The lamp was still burning."): Oro seated on the floor against the lit lamp, head bowed, stick across his knees. **choice**: the dome is not shown cracked (the text does not say so).
- `c3_deaf_water` (c03 "Nothing." at the Slick edge): Wrack alone in heavy brown water with open empty hands, an eel's jaws far off. Dead water drawn as flat brown-grey.
- `c3_dragon_panel` (c03.s03 "His hands went into the open panel and found the worst of it."): Wrack from behind, arms into the panel in the Dragon's blunt head, ribs with streaming water behind. **choice**: the ribs read as pale tubular channels; the Dragon's full length is not shown.
- `c4_well_descent` (c04.s04 "Halfway down something uncoiled from the wall."): well-warden squid, gold eye with slotted pupil, small light, white star below. No Jef in frame.
- `c4_holding_pools` (c04.s04 "He sat in the centre of the ring with his hands in a channel of seawater"): Wrack (pre-Thread, tunic) in a hall of milk-white glass with sleeping people in round gold pools; lamp in a crawlway hatch. **choice**: the pools are shown as shallow round basins with one sleeper each.
- `c4_apron_tied` (c04.s09 "she stood with her forehead against the back of his neck"): Jef from behind in nightshirt and leather apron, Maelis tying it; stone kitchen at night.
- `c5_lampweed_galleries` (c05.s02 "Below that the Maker lamps were dark... long swags of something that glowed a weak greenish yellow"). The weed reads brighter than "weak"; the lamps are drawn as small dark wall lanterns.
- `c5_sefa_high_hall` (c05.s04 "seven elders on seven stone seats", net-maker from the lower tier): Sefa with the grey band, a net-maker, seven elders. **choice**: elders in black robes; net-maker in a worn grey-brown smock.
- `c6_net_falls` (c06.s03 "A net came down over him in that moment"): Wrack (with the Thread line on his neck) in the failing gallery, a net falling, needles closing from the sides. **choice**: no riders drawn on the needles; the net reads as rope-like mesh.

## Stage art, group b (chapters 7, 8, 9, 11, 12)

| Image | From the text | Choices (text silent) |
|---|---|---|
| cg c7_jef_cairn | "Behind the house, where the largest spring ran down into the sea, somebody had built a cairn of black stones. A leather apron was folded on top of it, held down with a rock." "Okonta stood in front of it ... with her hand on her temple. Sefa ... knelt and laid a strand of lampweed from her own wrist among the stones." (c07.s02, ref line 163 ff.) | Dusk with a red sky; the spring runs as a small fall beside the cairn; apron dark brown; lampweed is green; Okonta barefoot in the grey suit. |
| cg c7_old_sea | "He saw the sea as it had been. There were forests that ran from Tip to Tip ... lit cities ... children swimming between the towers ... the Dragon new" (c07.s03, line 224 ff.) | Dragon drawn per canon (pale ribs, bound water streaming back, blunt prow, no eyes); children about six to ten, plain pale wraps; towers of the Makers lit warm gold. |
| cg c7_red_line_chart | "a chart. A hand was drawing a line across it in red, and the line passed over a small dome in a golden forest. The hand signed its name at the bottom." (c07.s03, line 239 ff.) | Only hand and cuff of a dark suit; the dome is drawn as a small grey round dome; no readable marks. |
| cg c7_crane_rail | "Crane put a cable tie round Ilan's wrists in the control hall ... He walked him to the rail. It was night, and the water was deep, and no one was looking." (c07.s05, line 385 ff.) | Ilan (before the Thread, no neck line) in a plain dark-grey surveyor's work jacket, wrists tied with a white plastic cable tie; Crane in his dark security jacket; deck of the survey ship by the control hall window. |
| cg c7_engine_vault | "There was an engine in its lowest vault. The Makers had sealed it there themselves, behind three doors. It could boil a sea." (c07.s05, ch07.rpy around line 377) | No people; the engine is a pale-metal drum with coils and pipes; three round doors in a row down a passage. Looks of the engine are a choice. |
| bg c8_market_night | "after the market lamps were dimmed ... She came down the steps to the lowest tier ... the edge of the planking" (c08.s07, line 580 ff.) | Dry, night, dimmed lanterns, light rain; three basins. |
| cg c9_flimsy_notice | "a flimsy, printed in the cheap purple ink ... His own face was at the top, the smooth one, in the collar ... charts ... each had its red line, and each was signed." (c09.s05, line 344 ff.) | Two hands (no faces) hold it; portrait is a smooth printed likeness of Wrack without Thread line; text drawn as meaningless dash lines; the bottom bold line shown as solid purple blocks so nothing is readable. |
| cg c9_grey_launch | "Grey. No flag. One old gentleman in it, and a hamper." (c09.s05, line 393 ff.) | Old man seen from behind and small, white hair; wicker hamper; calm flat water in the Eye under a ring of blue sky, raft-town lanterns behind (evening). The launch is a small plain open motor boat. |
| cg c11_column_valley | "It lay along a valley in the kelp for nearly a kilometre. Nine hundred people ... sleds of kelp-floats. The old rode on them, and the babies. Tide hounds worked up and down the flanks ... Over them, like clouds, hung the shadows of twelve hulls." (c11.s02, line 60 ff.) | Hulls drawn as grey ship shadows with decks; more than 12 are visible (about 12 large ones plus small farther ones). |
| cg c11_trawl_nets | "They were trawl nets, the great ones ... low to the ground ... He saw a net close. It was full. There were forty people in it, and it went up toward the stern ramp of a white-painted transport. A child's arm stuck out through the mesh to the shoulder." (c11.s02, line 87 ff.) | Net shown on the sand just before rising; the transport is drawn from below, hanging in murky green water; the child's arm reads weakly. |
| cg c11_sefa_holds | "Two hands closed on the back of his neck." "No, you don't. I've got you. Stay there." (c11.s02, line 144 ff.) | Wrack kneeling and slumped, Sefa kneeling behind him with both hands on his neck; Wrack in the grey-green tunic with the Thread line on his neck. |
| cg c12_bowl_full | "Tidehall could have seated every speaker of every hold in the world. It never had. It was full now." (c12.s02, line 85 ff.) | Faceless crowd of seated people in dark and pale robes, a small knot of figures at the centre; walls plain, no carvings. |

# Stage art group c: illustrations (art/refs/stage_c/cg/, prompts in the .txt files beside them)

- `c16_fleet_gathered` (c16.s04, "There were boats to the horizon", "And in the water were the mariners"): grey-green milky sea; Lashing's timber hulls with patched sails in the middle, dark gate barges, tugs, smacks, boats with fish nailed to the bows, one all-white hospital ship with no markings; islanders along every rail; adult mariners in the water to the shoulders, black hair, pale skin, large dark eyes, a brass tag on a cord on some (the "brass tags of Kelder"). Choices where the text is silent: mariners wear grey-green tunics; "Agravars" drawn as ordinary islanders in grey-green and brown plain clothes; the wall is left out (narrated after the panorama).
- `c17_pit_city` (c17.s03, "It was a pit. It was eighty kilometres across", "The Dragon lay coiled on the mud"): view from above; sea standing in a ring round the rim; fish scattered on grey mud; rust-coloured platform on six legs; the tiered Maker city (see Maker architecture) rising out of the silt inside a ring of pale metal hoops (the ribs) round its foot; Dragon pale and coiled (see Dragon in chapter 17). Redone 2026-11-24 (owner: it was a flat village of huts): now a large multi-tier city. Redone 2026-11-24: seen from high on the rim INSIDE the pit, ring of grey glassy water all round with the sea over its top edge, foam only on the top edge; Dragon as in c17_pit_view. The eye-glint flaw is fixed.
- `c17_makers_quarrel` (c17.s04, "Then they showed a man. He stood where Rook was sitting. He was shouting"): Makers = ordinary people, long limbs, large dark eyes, broad hands, weathered brown skin ("ordinary people, with children", c17.s05). Choices: plain pale tunics, short dark hair; one man forcing the ring, four others standing back; wall pictures show a pit with dead fish; ring water grey.
- `c17_seating_ring` (c17.s05, "It took eleven hours. It was the largest thing Ilan ever mended"): Ilan, Hanne (lamp), Raske (calling sections, pointing), Crane (carrying). Rook, who said he would watch from the rim, is not drawn (not in the seed). Choice: vault drawn as dark round stone brick; the ring is a pale metal hoop with its sections lying in view; bright water just starting.
- `c17_the_way_through` (c17.s06, "He was standing in the central square when it came ... Yeva's hand was on the back of his neck, and Sefa's arm was round him"): Ilan barefoot, eyes lowered, still, hands open; Yeva behind with a hand at his neck and shoulder; Sefa with an arm round him; callers as tiny wading figures in the streets with threads of light running to him; colder pale light rising from the water beneath his feet. Flaw: water is about ankle deep, not knee deep; Yeva's hand rests on neck and shoulder together.

# Wrack (Ilan): confidence portraits (stage_ilan, round 2)

Edited from the real p_wrack_thread_attentive (on light grey) with nano-banana-2; only eyebrows, eyelids, gaze and mouth change. Same face, hair, plain grey-green tunic, thin pale Thread line. Cut out with birefnet-heavy. Prompts and sources: v2/. Rejects: rejected/.

Assured (after Saltgate, he told a stranger his name and nothing bad happened): level relaxed brows, open direct gaze, closed lightly firm mouth, chin slightly raised.
- wrack_assured_calm: quiet self-possession.
- wrack_assured_attentive: listening and sure.
- wrack_assured_thinking: gaze shifted aside and up, weighing a thought without worry.
- wrack_assured_easy: the faintest lift at one mouth corner, restrained.

Strong (after the Great Moot, stood alone and was heard): the same plus firmer jaw, wide clear direct eyes, chin higher, face held still; no frown, scowl or smile.
- wrack_strong_calm: settled inner strength.
- wrack_strong_attentive: same, listening.
- wrack_strong_resolved: a firm decision, mouth pressed a little firmer.
- wrack_strong_steady: steadiness under pressure, chin a touch higher.

Known: strong_* differ from assured_* mostly in brow and jaw, so subtly.

## Chapter 18 Maker pass (2026-11-24)
Meet is the risen Site Nine city from chapter 17 (the text: "a city that had no owner", "the high towers", "the third tower", "the eastern quarter", the hall "the silt had sealed"), so everything built in it is tiered Maker architecture (see Maker architecture). Ordinary things stay ordinary: stalls, canvas, crates, washing, lanterns, boats, table, basins, bench, rope posts, round glass street lamps, Low Anthem (a human hold) and Meridian's windowless building. Redone with nano-banana-2 edits (current image plus c17_city_risen as style reference), old files in art/refs/ch18/previous/*_oldmaker.png: bg c18_meet_empty, c18_waterside_square, c18_meet_market, c18_canal_table, c18_dragon_square, c18_archive_workshop; cg c18_ribs_water, c18_archive_palm, c18_this_sleeves. The Dragon head in c18_dragon_square and c18_ribs_water is now one smooth seamless blunt pale prow (no rivets, seams, mouth or eyes). The archive hall is smooth milk-pale Maker stone with fluted pilasters and a ribbed vault. Left as is: bg c18_terrace_lit (human hold), cg c18_empty_cradle (Meridian's concrete dock). Weak: c18_ribs_water still has ochre-pink, flat-walled buildings at the far left and far right edges; c18_canal_table has a few moss and block-joint marks left on the left quay; c18_dragon_square and c18_meet_empty are reframed a little by the model; the archive floor in c18_archive_workshop stays tan, in c18_this_sleeves grey (as before).
Chapter 17 ring fix (2026-11-24): the ring in bg c17_vault_grey, bg c17_vault_lit and cg c17_vault_light is now a smooth seamless pale metal hoop set flush in the floor (text: "a single hoop of the pale metal, set flush with the stone"); old files art/refs/ch17/previous/c17_vault_*_rivets.png. The small inner ring round the wheels keeps its bolts (part of the human steel frame). The model also shifted the camera slightly in vault_grey and redrew Ilan a little in vault_light.

## Chapter 18 Maker pass 2 (2026-11-24)
Shell-and-heart lean for ALL future Maker pictures (owner's note: the look read classical or Ottoman): favour ribbed shell forms and smooth flowing curves, like the banded shell of an air-heart: big scallop-ribbed domes, rounded pearly bulb and bell shapes, broad gentle curved ribs, walls that curve and flow, soft rounded low openings with light from within. Use fewer thin minaret-like spires and avoid pointed, horseshoe or Gothic arches and pointed vaults. Done with nano-banana-2 edits (current image plus c17_city_risen as style reference), pass 1 files in art/refs/ch18/previous/*_pass1.png: cg c18_ribs_water (far left and right edges are now the same pale tiered Maker buildings with shell domes and bulb towers; the ochre flat walls are gone), bg c18_canal_table (left quay and paving are smooth pale polished stone, no joints, no moss; doorways rounder), cg c18_this_sleeves (the hall is one smooth rounded shell-shaped pale chamber with broad curved ribs flowing over the ceiling and glowing from within, no pointed arches; Ilan, tool, air-heart and grey silt unchanged). Checked and left as is: bg c18_dragon_square (Dragon head, full rib row and the square all in frame) and bg c18_meet_empty (whole length of the empty street and all lit lamps in frame). Weak: c18_dragon_square, c18_meet_empty and the other ch18 backgrounds still show tall thin minaret-like spires; c18_canal_table keeps some arched doorways and one onion-shaped distant dome; c18_ribs_water still has bulb-topped towers.
