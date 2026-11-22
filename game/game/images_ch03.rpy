# Chapter 3 art. Same rules as images.rpy: backgrounds scaled to 1920x1080, portraits lit per
# background (effects.rpy), underwater places get the light ripple (the inside of the Dragon does not).

# --- backgrounds (underwater, rippling) ---
image bg kelp_night = At(Transform("bg/kelp_night.png", size=(1920, 1080)), water)
image bg tangle = At(Transform("bg/tangle.png", size=(1920, 1080)), water)
image bg sounding_ruin = At(Transform("bg/sounding_ruin.png", size=(1920, 1080)), water)
image bg slick_edge = At(Transform("bg/slick_edge.png", size=(1920, 1080)), water)
image bg greywatch_stone = At(Transform("bg/greywatch_stone.png", size=(1920, 1080)), water)
image bg ice_shelf = At(Transform("bg/ice_shelf.png", size=(1920, 1080)), water)
# --- backgrounds (inside the Dragon: no ripple) ---
image bg gallery = Transform("bg/gallery.png", size=(1920, 1080))
image bg cradles = Transform("bg/cradles.png", size=(1920, 1080))

# --- illustrations ---
image cg c3_needle_ride = "cg/c3_needle_ride.png"
image cg c3_moored_night = "cg/c3_moored_night.png"
image cg c3_eel = "cg/c3_eel.png"
image cg c3_dragon_arrives = "cg/c3_dragon_arrives.png"
image cg c3_dragon_head = "cg/c3_dragon_head.png"
image cg c3_sleds = "cg/c3_sleds.png"
image cg c3_whales = "cg/c3_whales.png"

# --- portraits (new this chapter) ---
image p brask_awed = At("p_brask_awed.png", lit_portrait)
image p brask_gruff = At("p_brask_gruff.png", lit_portrait)
image p brask_watchful = At("p_brask_watchful.png", lit_portrait)
image p fallow_man_calm = At("p_fallow_man_calm.png", lit_portrait)
image p fallow_man_frail = At("p_fallow_man_frail.png", lit_portrait)
image p fallow_man_laboured = At("p_fallow_man_laboured.png", lit_portrait)
image p fallow_woman_hopeful = At("p_fallow_woman_hopeful.png", lit_portrait)
image p fallow_woman_relieved = At("p_fallow_woman_relieved.png", lit_portrait)
image p fallow_woman_weary = At("p_fallow_woman_weary.png", lit_portrait)
image p officer_grim = At("p_officer_grim.png", lit_portrait)
image p officer_hard = At("p_officer_hard.png", lit_portrait)
image p officer_shocked = At("p_officer_shocked.png", lit_portrait)
image p okonta_listening = At("p_okonta_listening.png", lit_portrait)
image p wrack_tunic_awed = At("p_wrack_tunic_awed.png", lit_portrait)
