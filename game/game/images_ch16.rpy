# Chapter 16 art. Same rules as images_ch06.rpy.
# Reused backgrounds (already defined elsewhere, do not redefine): dc_high_hall, dc_canyon_above,
# dc_canyon_lit60, dc_sea_door (scene 3); c15_harbour_sunset (Port Halcyon harbour, scene 1).

# --- backgrounds (above water or indoors: no ripple) ---
image bg c16_kelder_day = Transform("bg/c16_kelder_day.png", size=(1920, 1080))
image bg c16_kelder_evening = Transform("bg/c16_kelder_evening.png", size=(1920, 1080))
image bg c16_saltgate_stacks = Transform("bg/c16_saltgate_stacks.png", size=(1920, 1080))
image bg c16_market_dry = Transform("bg/c16_market_dry.png", size=(1920, 1080))
image bg c16_sluice_dry = Transform("bg/c16_sluice_dry.png", size=(1920, 1080))
image bg c16_lock_box = Transform("bg/c16_lock_box.png", size=(1920, 1080))
image bg c16_barges_lantern = Transform("bg/c16_barges_lantern.png", size=(1920, 1080))
image bg c16_girdle_fleet = Transform("bg/c16_girdle_fleet.png", size=(1920, 1080))
image bg c16_boat_stern = Transform("bg/c16_boat_stern.png", size=(1920, 1080))
image bg c16_boat_stern_evening = Transform("bg/c16_boat_stern_evening.png", size=(1920, 1080))
image bg c16_rafts_night = Transform("bg/c16_rafts_night.png", size=(1920, 1080))

# --- illustrations ---
image cg c16_kelder_exit = "cg/c16_kelder_exit.png"
image cg c16_okonta_corin = "cg/c16_okonta_corin.png"
image cg c16_choirs_answer = "cg/c16_choirs_answer.png"
image cg c16_grey_wall = "cg/c16_grey_wall.png"
image cg c16_maelis_arrives = "cg/c16_maelis_arrives.png"
image cg c16_sefa_handful = "cg/c16_sefa_handful.png"
image cg c16_sefa_asleep = "cg/c16_sefa_asleep.png"
image cg c16_garran_west = "cg/c16_garran_west.png"

# --- portraits (new this chapter) ---
image p kelder_mild = At("p_kelder_mild.png", lit_portrait)
image p kelder_considering = At("p_kelder_considering.png", lit_portrait)
image p lockkeeper_stern = At("p_lockkeeper_stern.png", lit_portrait)
image p lockkeeper_resolved = At("p_lockkeeper_resolved.png", lit_portrait)
image p noodle_kindly = At("p_noodle_kindly.png", lit_portrait)
image p noodle_puzzled = At("p_noodle_puzzled.png", lit_portrait)
image p corin_earnest = At("p_corin_earnest.png", lit_portrait)
image p brask_wry = At("p_brask_wry.png", lit_portrait)
image p sefa_laughing_crying = At("p_sefa_laughing_crying.png", lit_portrait)
image p hesper_eased = At("p_hesper_eased.png", lit_portrait)
image p maelis_cropped_amused = At("p_maelis_cropped_amused.png", lit_portrait)
