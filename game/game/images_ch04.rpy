# Chapter 4 art. Backgrounds scaled to 1920x1080; portraits lit per background (effects.rpy).
# Surface scenes (still black water) and interiors have no ripple; only the Lantern from outside is underwater.

# --- backgrounds (underwater, rippling) ---
image bg lantern_exterior = At(Transform("bg/lantern_exterior.png", size=(1920, 1080)), water)
# --- backgrounds (surface and interiors: no ripple) ---
image bg well_lip = Transform("bg/well_lip.png", size=(1920, 1080))
image bg kettle_house = Transform("bg/kettle_house.png", size=(1920, 1080))
image bg kettle_interior = Transform("bg/kettle_interior.png", size=(1920, 1080))
image bg workshop = Transform("bg/workshop.png", size=(1920, 1080))
image bg lantern_hall = Transform("bg/lantern_hall.png", size=(1920, 1080))
image bg dark_hall = Transform("bg/dark_hall.png", size=(1920, 1080))
image bg step_night = Transform("bg/step_night.png", size=(1920, 1080))
image bg step_fog = Transform("bg/step_fog.png", size=(1920, 1080))
image bg landing_dusk = Transform("bg/landing_dusk.png", size=(1920, 1080))

# --- illustrations ---
image cg c4_well_star = "cg/c4_well_star.png"
image cg c4_hands_lamp = "cg/c4_hands_lamp.png"
image cg c4_lantern_crown = "cg/c4_lantern_crown.png"
image cg c4_sphere = "cg/c4_sphere.png"
image cg c4_anselm_unhelm = "cg/c4_anselm_unhelm.png"
image cg c4_tool_table = "cg/c4_tool_table.png"
image cg c4_jef_under_heart = "cg/c4_jef_under_heart.png"
image cg c4_dragon_departs = "cg/c4_dragon_departs.png"

# --- portraits (new this chapter) ---
image p anselm_calm = At("p_anselm_calm.png", lit_portrait)
image p anselm_cold = At("p_anselm_cold.png", lit_portrait)
image p anselm_gentle = At("p_anselm_gentle.png", lit_portrait)
image p anselm_helmed = At("p_anselm_helmed.png", lit_portrait)
image p anselm_smile = At("p_anselm_smile.png", lit_portrait)
image p jef_annoyed = At("p_jef_annoyed.png", lit_portrait)
image p jef_attentive = At("p_jef_attentive.png", lit_portrait)
image p jef_grumbling = At("p_jef_grumbling.png", lit_portrait)
image p jef_tired = At("p_jef_tired.png", lit_portrait)
image p jef_watching = At("p_jef_watching.png", lit_portrait)
image p maelis_composed = At("p_maelis_composed.png", lit_portrait)
image p maelis_examining = At("p_maelis_examining.png", lit_portrait)
image p maelis_shut = At("p_maelis_shut.png", lit_portrait)
image p maelis_silent = At("p_maelis_silent.png", lit_portrait)
image p maelis_smile = At("p_maelis_smile.png", lit_portrait)
image p okonta_smiling = At("p_okonta_smiling.png", lit_portrait)
image p wrack_tunic_grieving = At("p_wrack_tunic_grieving.png", lit_portrait)
# Wrack after the Thread (c04 night): same portraits with the fine pale line on the neck
image p wrack_thread_calm = At("p_wrack_thread_calm.png", lit_portrait)
image p wrack_thread_troubled = At("p_wrack_thread_troubled.png", lit_portrait)
image p wrack_thread_grieving = At("p_wrack_thread_grieving.png", lit_portrait)
image p wrack_thread_thinking = At("p_wrack_thread_thinking.png", lit_portrait)
image p wrack_thread_angry = At("p_wrack_thread_angry.png", lit_portrait)
image p wrack_thread_fading = At("p_wrack_thread_fading.png", lit_portrait)
image p wrack_thread_exhausted = At("p_wrack_thread_exhausted.png", lit_portrait)
image p wrack_thread_dazed = At("p_wrack_thread_dazed.png", lit_portrait)
image p wrack_thread_dejected = At("p_wrack_thread_dejected.png", lit_portrait)
image p wrack_thread_resolved = At("p_wrack_thread_resolved.png", lit_portrait)
image p wrack_thread_frightened = At("p_wrack_thread_frightened.png", lit_portrait)
image p wrack_thread_stunned = At("p_wrack_thread_stunned.png", lit_portrait)
image p wrack_thread_shaken = At("p_wrack_thread_shaken.png", lit_portrait)
image p wrack_thread_attentive = At("p_wrack_thread_attentive.png", lit_portrait)
image p wrack_thread_ashamed = At("p_wrack_thread_ashamed.png", lit_portrait)
