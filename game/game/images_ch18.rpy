# Chapter 18 art. Same rules as images_ch12.rpy.
# Reused as they are (defined elsewhere): bg c12_tidehall_centre (Tidehall court), bg meeting_hall_lit,
# bg dome_crown / dome_dark_half (cracked dome), bg c7_nine_spires (Meet from far).

# --- backgrounds (above water or indoors: no ripple) ---
image bg c18_meet_empty = Transform("bg/c18_meet_empty.png", size=(1920, 1080))
image bg c18_dragon_square = Transform("bg/c18_dragon_square.png", size=(1920, 1080))
image bg c18_meet_market = Transform("bg/c18_meet_market.png", size=(1920, 1080))
image bg c18_waterside_square = Transform("bg/c18_waterside_square.png", size=(1920, 1080))
image bg c18_canal_table = Transform("bg/c18_canal_table.png", size=(1920, 1080))
image bg c18_archive_workshop = Transform("bg/c18_archive_workshop.png", size=(1920, 1080))
# --- backgrounds (underwater, rippling) ---
image bg c18_terrace_lit = At(Transform("bg/c18_terrace_lit.png", size=(1920, 1080)), water)

# --- illustrations ---
image cg c18_ribs_water = "cg/c18_ribs_water.png"
image cg c18_empty_cradle = "cg/c18_empty_cradle.png"
image cg c18_terrace_song = "cg/c18_terrace_song.png"
image cg c18_archive_palm = "cg/c18_archive_palm.png"
image cg c18_this_sleeves = "cg/c18_this_sleeves.png"

# --- portraits (new this chapter) ---
image p wrack_thread_nervous = At("p_wrack_thread_nervous.png", lit_portrait)
image p wrack_thread_trying = At("p_wrack_thread_trying.png", lit_portrait)
image p hesper_warm = At("p_hesper_warm.png", lit_portrait)
image p maelis_sidelong = At("p_maelis_sidelong.png", lit_portrait)
