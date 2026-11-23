# Chapter 12 art. Same rules as images_ch06.rpy.

# --- backgrounds (above water or indoors: no ripple) ---
image bg c12_shelves_deck = Transform("bg/c12_shelves_deck.png", size=(1920, 1080))
image bg c12_apron = Transform("bg/c12_apron.png", size=(1920, 1080))
image bg c12_tower_room = Transform("bg/c12_tower_room.png", size=(1920, 1080))
# --- backgrounds (underwater, rippling) ---
image bg c12_tidehall_centre = At(Transform("bg/c12_tidehall_centre.png", size=(1920, 1080)), water)
image bg c12_tidehall_rim_dusk = At(Transform("bg/c12_tidehall_rim_dusk.png", size=(1920, 1080)), water)

# --- illustrations ---
image cg c12_tug_shelves = "cg/c12_tug_shelves.png"
image cg c12_alone_sand = "cg/c12_alone_sand.png"
image cg c12_swell_ring = "cg/c12_swell_ring.png"
image cg c12_swell_shelves = "cg/c12_swell_shelves.png"
image cg c12_raske_lamp = "cg/c12_raske_lamp.png"

# --- portraits (new this chapter) ---
image p odile_brisk = At("p_odile_brisk.png", lit_portrait)
image p odile_cool = At("p_odile_cool.png", lit_portrait)
image p hanne_awed = At("p_hanne_awed.png", lit_portrait)
