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
