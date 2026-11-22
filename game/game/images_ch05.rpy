# Chapter 5 art. Same rules as images.rpy: backgrounds scaled to 1920x1080, portraits lit per
# background (effects.rpy), underwater places get the light ripple (dry halls do not).

# --- backgrounds (underwater, rippling) ---
image bg south_sea_ice = At(Transform("bg/south_sea_ice.png", size=(1920, 1080)), water)
image bg dc_canyon_above = At(Transform("bg/dc_canyon_above.png", size=(1920, 1080)), water)
image bg dc_canyon_lit60 = At(Transform("bg/dc_canyon_lit60.png", size=(1920, 1080)), water)
# --- backgrounds (dry: no ripple) ---
image bg jef_workshop = Transform("bg/jef_workshop.png", size=(1920, 1080))
image bg landing_evening = Transform("bg/landing_evening.png", size=(1920, 1080))
image bg dc_high_hall = Transform("bg/dc_high_hall.png", size=(1920, 1080))
image bg dc_service_tunnels = Transform("bg/dc_service_tunnels.png", size=(1920, 1080))
image bg dc_lowest_halls = Transform("bg/dc_lowest_halls.png", size=(1920, 1080))
image bg dc_heart_chamber = Transform("bg/dc_heart_chamber.png", size=(1920, 1080))
image bg dc_sea_door = Transform("bg/dc_sea_door.png", size=(1920, 1080))

# --- illustrations ---
image cg c5_needle_ride = "cg/c5_needle_ride.png"
image cg c5_canyon = "cg/c5_canyon.png"
image cg c5_sefa_grips = "cg/c5_sefa_grips.png"
image cg c5_lamps_down = "cg/c5_lamps_down.png"
image cg c5_dragon_lights = "cg/c5_dragon_lights.png"

# --- portraits (new this chapter) ---
image p aurel_calm = At("p_aurel_calm.png", lit_portrait)
image p aurel_tired = At("p_aurel_tired.png", lit_portrait)
image p bother_excited = At("p_bother_excited.png", lit_portrait)
image p okonta_frowning = At("p_okonta_frowning.png", lit_portrait)
image p okonta_grim = At("p_okonta_grim.png", lit_portrait)
image p sefa_eyes_filling = At("p_sefa_eyes_filling.png", lit_portrait)
image p sefa_fierce = At("p_sefa_fierce.png", lit_portrait)
image p sefa_hard = At("p_sefa_hard.png", lit_portrait)
image p sefa_tired = At("p_sefa_tired.png", lit_portrait)
image p vey_cold = At("p_vey_cold.png", lit_portrait)
image p vey_shaken = At("p_vey_shaken.png", lit_portrait)
image p vey_tight = At("p_vey_tight.png", lit_portrait)
image p wrack_tunic_dazed = At("p_wrack_tunic_dazed.png", lit_portrait)
image p wrack_tunic_exhausted = At("p_wrack_tunic_exhausted.png", lit_portrait)
image p wrack_tunic_fading = At("p_wrack_tunic_fading.png", lit_portrait)
image p wrack_tunic_grieving = At("p_wrack_tunic_grieving.png", lit_portrait)
image p wrack_tunic_resolved = At("p_wrack_tunic_resolved.png", lit_portrait)
image p wrack_tunic_stunned = At("p_wrack_tunic_stunned.png", lit_portrait)
