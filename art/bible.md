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

## Known weaknesses

- Wrack's crest is whole, not half ripped away, and its lettering is garbled. Fix before it appears large.
- Skin tone is unstated for everyone but Oro. The model's default is pale for the others.
- The meeting-hall column is lit white by a skylight. In the scene it is dark until Wrack opens it (c01.s04.p022), so a dark version is needed before that scene.
- The dome's panes look a little like glass. The text says "neither glass nor stone".
- The dry room has no hammock or fire; the text gives none.
- Expressions (see the manifest `needs`) are not made yet.

## Rejected attempts

`art/refs/ch01/rejected/`: Oro (pale skin although the text says brown), Ione (scars drew as open wounds), and first tries of the dome (a glass greenhouse on a grass mound), the dry room (bubbles in dry air) and the meeting hall (a crowd and a black column).
