# Chapter 2 art. Same rules as images.rpy: backgrounds scaled to 1920x1080, portraits
# lit per background (effects.rpy), underwater places get the light ripple.

# --- backgrounds (underwater ones ripple) ---
image bg dome_crown = At(Transform("bg/dome_crown.png", size=(1920, 1080)), water)
image bg terraces_night = At(Transform("bg/terraces_night.png", size=(1920, 1080)), water)
image bg terrace_wrecked = At(Transform("bg/terrace_wrecked.png", size=(1920, 1080)), water)
image bg terrace_dusk = At(Transform("bg/terrace_wrecked.png", size=(1920, 1080), matrixcolor=BrightnessMatrix(-0.22) * TintMatrix((200, 215, 255))), water)
image bg burial_kelp = At(Transform("bg/burial_kelp.png", size=(1920, 1080)), water)
# --- backgrounds (inside the dome: no ripple) ---
image bg dome_dark_half = Transform("bg/dome_dark_half.png", size=(1920, 1080))
image bg net_racks = Transform("bg/net_racks.png", size=(1920, 1080))
image bg hall_day = Transform("bg/hall_day.png", size=(1920, 1080))

# --- illustrations ---
image cg c2_lamps = "cg/c2_lamps.png"
image cg c2_barge = "cg/c2_barge.png"
image cg c2_burial = "cg/c2_burial.png"
image cg c2_needle = "cg/c2_needle.png"
image cg c2_gunboats = "cg/c2_gunboats.png"

# --- portraits (new this chapter) ---
image p hesper_angry = At("p_hesper_angry.png", lit_portrait)
image p hesper_shut = At("p_hesper_shut.png", lit_portrait)
image p hesper_stern = At("p_hesper_stern.png", lit_portrait)
image p hesper_teacher = At("p_hesper_teacher.png", lit_portrait)
image p hesper_tired = At("p_hesper_tired.png", lit_portrait)
image p ione_pain = At("p_ione_pain.png", lit_portrait)
image p okonta_grave = At("p_okonta_grave.png", lit_portrait)
image p okonta_sorrow = At("p_okonta_sorrow.png", lit_portrait)
image p okonta_urgent = At("p_okonta_urgent.png", lit_portrait)
image p okonta_wry = At("p_okonta_wry.png", lit_portrait)
image p oro_delighted = At("p_oro_delighted.png", lit_portrait)
image p sefa_fierce = At("p_sefa_fierce.png", lit_portrait)
image p wrack_tunic_baffled = At("p_wrack_tunic_baffled.png", lit_portrait)
image p wrack_tunic_despair = At("p_wrack_tunic_despair.png", lit_portrait)
image p wrack_tunic_resolved = At("p_wrack_tunic_resolved.png", lit_portrait)
image p wrack_tunic_shaken = At("p_wrack_tunic_shaken.png", lit_portrait)
image p wrack_tunic_shivering = At("p_wrack_tunic_shivering.png", lit_portrait)
image p wrack_tunic_curious = At("p_wrack_tunic_curious.png", lit_portrait)
image p wrack_tunic_eager = At("p_wrack_tunic_eager.png", lit_portrait)
image p wrack_tunic_warm = At("p_wrack_tunic_warm.png", lit_portrait)
image p wrack_tunic_amused = At("p_wrack_tunic_amused.png", lit_portrait)
image p sefa_grin = At("p_sefa_grin.png", lit_portrait)
image p oro_twinkle = At("p_oro_twinkle.png", lit_portrait)
