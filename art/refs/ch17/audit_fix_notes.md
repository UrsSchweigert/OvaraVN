# Chapter 17 audit fixes (2026-11-24)

All edits: nano-banana-2 edit, 16:9, output 1376x768 upscaled (Lanczos) to the old game size. Old files: art/refs/ch17/previous/c17_<name>_audit1.png. Reference copies updated in art/refs/ch17/cg and places (vault images also in new/). Raw results and prompts: scratchpad only; prompts summarised below. 18 calls, $1.44 (one rejected, one retry).

Order changed on purpose: vault_grey first, vault_lit made from it, then the two CGs, so the vault is one room everywhere.

| Image | Change | Tries |
|---|---|---|
| bg c17_vault_grey | smooth pale floor; one smooth hoop (no bolts); frame of raw grey-black steel with exactly two wheels (one inside the other); walls dull pale Maker stone like a ribbed shell; two simple glass-globe lamps on low stands instead of tripods; bench and pinned drawings kept | 1 |
| bg c17_vault_lit | edit of the new vault_grey: only light and walls change (walls and floor glow floor to roof, projected tiered city, sea, tiny people); lamps, bench, frame same | 1 |
| cg c17_vault_light | smooth glowing floor; two-wheel steel frame at the ring centre; ring interior pale water, no cracks; Rook's hands now clean grey-white rags with faint stains, no blood. Ilan kneels with tool, Rook at bench, Maelis in coat unchanged | 1 |
| cg c17_makers_quarrel | rebuilt in the vault look: pale smooth room, smooth seamless hoop (no bolts, no raised block), pictures on the walls show the standing grey wall of water and the pit with dead fish; shouting man at the hoop edge with four frightened Makers behind | 1 |
| bg c17_city_risen, cg c17_city_rises | hills removed (open sea horizon); city_risen sky now dawn peach to pale blue | 1 each |
| bg c17_silt_street, cg c17_ilan_lamps | lamps are slender pale pearly posts with a clear glass teardrop and silver cap, no finial, no cage; still lit near, dim far | 1 each |
| cg c17_hands_reach | towers are fluted, taper, pearly bulb, slender tip, on a pale tiered base; water soft sea-green | 1 |
| bg c17_wall_face, bg c17_dead_water | redrawn with line art and flat cel shading; wall_face now a long curve sweeping off to the right with no vertical cut | 1 each |
| cg c17_seating_ring | the ring is one whole smooth hoop, no loose strips or floor plates | 1 |
| bg c17_road_barges, bg c17_square_flooded, cg c17_two_old | water toned to soft sea-green | 1 each |
| bg c17_pit_view | the grey slab with a seam is now a smooth pale curved balcony ledge | 1 |
| cg c17_wall_climb | cyan glow strips removed from the three needles | 2 (first try returned the c5 needle picture; second try had no second reference) |

Lamp decision check: no owner decision covers the chapter 17 street lamps. The owner's Maker lamp (ch 1, thick column with caged lens) is a hall lamp; the "round glass globes" note is the art director's choice for Meet. So the slender glass-and-silver design was used.

## Text for art/bible.md (lead to merge)
- Vault of the Ring (c17), replace the old entry: round chamber like the inside of a ribbed shell, smooth pale walls and floor (no cracks, no concrete), ring of pale metal as ONE seamless hoop flush in the floor with no bolts, a frame of plain raw grey-black steel at its centre holding exactly two wheels, one inside the other, three open doorways at the top of a stair, a bench with pinned drawings and two small glass-globe lamps on low stands. Grey version: dull cream-grey stone. Lit version: walls and floor glow from floor to roof with projected pictures of the tiered city, the sea and small people. cg c17_makers_quarrel shows the quarrel pictures (the wall, the pit, the fish) on the walls and the shouting man at the hoop.
- Rook's hands in illustrations: wrapped in grey-white rags with faint stains, never raw blood.
- Chapter 17 street lamps: slender pale pearly posts with a clear glass teardrop, silver cap and base, no finial or cage (bg c17_silt_street, cg c17_ilan_lamps).
- Healed water in ch17 pictures: soft pale sea-green (road_barges, square_flooded, two_old, hands_reach fixed; barge_rows and healers_line still strong green).
- c17 needles: plain pale silver-white, no glow strips (c5_needle_ride shows a faint blue underglow; wall_climb has none).
- bg c17_wall_face and c17_dead_water are now cel-lined; wall_face is a curving face.

## For art/canon.json (lead to merge)
"Vault of the Ring": update to the text above. "Anselm Rook at ninety": hands wrapped in clean grey-white rags with faint stains (replace "stained rags" wording if it reads as blood).

## merge_notes.md open points to remove
"c17_vault_light: Rook reads as kneeling" stays (he is on the floor behind the bench). "Weak: in vault_lit the ring has rivets" is fixed. Neon green remains in c17_barge_rows and c17_healers_line.

## Weak spots
- vault_grey walls read cream, not grey; the two wheels are near-equal in size and read as a double-rimmed wheel more than "one inside the other".
- makers_quarrel: the hoop shows a second inner pale ring (a low rim); the people look human, only a little long-limbed and large-eyed, not clearly Maker.
- wall_face: wall reads somewhat like an ice cliff with a snow-like top edge; glassy look is lost; dead_water wall is a flat band.
- two_old: rim of the pool is still dark cracked stone and Rook's hands still show blood (not in the audit list, not touched). In vault_light the ring now overlaps Rook's feet slightly.
- silt_street lamps have a tiny pointed teardrop tip (no finial).
- pit_view: the ledge is wide and crops a little of the foreground.
- Not touched: wall_faces faces, barge_rows, healers_line, pit_city, the_way_through.

## Second pass (2026-11-24, audit2)
Old files: art/refs/ch17/previous/c17_<name>_audit2.png (wall_face, barge_rows, healers_line, two_old). nano-banana-2 edits, 16:9, 1376x768 upscaled (Lanczos) to 1920x1088. 6 calls before this note, 8 cents each ($0.48 in all, no rejects except none).

| Image | Change | Tries |
|---|---|---|
| bg c17_wall_face | redone as sheer, smooth, grey, glassy translucent standing water (current image plus c17_pit_view as water reference): dark grey-blue depth, soft pale vertical light shafts, faint reflections, a few tiny bubbles, thin line of small white foam speckle on the top edge, mist at the foot, flat grey sea; snow, ice texture and dark wedge streaks gone; long curve with no vertical cut kept | 2 (second try thinned the crusty top edge) |
| cg c17_barge_rows | water now soft pale sea-green like road_barges; nothing else changed | 1 |
| cg c17_healers_line | water soft pale sea-green; ripples near the hands keep a faint pale-green glow | 1 |
| cg c17_two_old | pool rim and floor smooth seamless pale Maker stone, no cracks; one smooth pale ring flush in the floor (right); Rook's hands in grey-white rags with faint stains, no blood; water soft sea-green/grey, bright; both old people, hand hold, coat unchanged | 2 (first try drew a second pool behind them) |

Weak spots: wall_face top still shows a slightly thick rounded glassy lip with fine foam speckle, and the wall is a little smoother than the pit_view water; the distant wall in barge_rows is still a panelled grey band (not in this pass; same for c17_wall_climb and c17_road_barges, which were not re-edited, so they differ a little from the new wall_face); two_old: the pool is now much bigger in the foreground, the ring is a small thin oval on the floor and not a hoop round the pool; Rook's rags look bandage-like with grey-pink fingers; the camera moved slightly lower.
