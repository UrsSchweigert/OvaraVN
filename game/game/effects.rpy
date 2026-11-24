# Moving backgrounds.
#
# Under the sea: a very light, slow ripple, done by a small shader. Chapter 1's
# underwater backgrounds use it (see images.rpy).
# Above the sea: sun rays, and rain. They are overlays; show them on top of a
# background and hide them when the scene ends:
#     show fx sunrays        /  hide fx sunrays
#     show fx rain           /  hide fx rain
# The sun and rain are ready for the chapters that need them; chapter 1 has no
# scene above the water.

init python:
    renpy.register_shader("vn.water", variables="""
        uniform float u_phase;
        uniform float u_amp;
        uniform sampler2D tex0;
        attribute vec4 a_position;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 uv = v_tex_coord;
        uv.x += sin(uv.y * 24.0 + u_phase) * u_amp + sin(uv.y * 61.0 - u_phase * 1.3) * u_amp * 0.5;
        uv.y += cos(uv.x * 19.0 + u_phase * 0.8) * u_amp * 0.7;
        gl_FragColor = texture2D(tex0, uv);
    """)

# One loop is 40 s and returns exactly to its start, so it never jumps.
# The picture is enlarged by 1.2% so the ripple never shows the edge.
transform water(amp=0.0022):
    mesh True
    shader "vn.water"
    u_amp amp
    u_phase 0.0
    xalign 0.5 yalign 0.5 zoom 1.012
    block:
        linear 40.0 u_phase 125.66
        u_phase 0.0
        repeat

transform water_soft:
    water(0.0012)

# Sun rays above the water: they drift a little and breathe, very slowly.
transform sun_drift:
    alpha 0.55 xoffset -20
    block:
        ease 9.0 alpha 0.8 xoffset 20
        ease 9.0 alpha 0.55 xoffset -20
        repeat

image fx sunrays = At("images/fx/sunrays.png", sun_drift)

# Rain: thin slanted streaks.
image fx rain = SnowBlossom(Solid("#c9dcec99", xsize=2, ysize=38), count=160, border=60,
                            xspeed=(-60, -30), yspeed=(1000, 1300), start=0, fast=True,
                            horizontal=False)


# ---- Portrait lighting ---------------------------------------------------------
#
# Portraits are drawn evenly lit on grey, so they look stuck onto the scene. Each
# portrait picture is lit to match whichever background is showing: tinted, a
# little darker, given the same light ripple under water, and faded softly at
# its bottom edge. It is done on the picture itself (images.rpy wraps every
# portrait in `lit_portrait`), so a `scene` statement clears portraits as usual.
# Nothing in the story script needs to change.

init python:
    # background name -> (tint r, g, b, brightness, saturation, ripple)
    PORTRAIT_LIGHT = {
        "kelp_forest":   (0.80, 0.98, 0.78, -0.03, 0.92, 0.0012),
        "terraces_dome": (0.80, 0.96, 0.92, -0.02, 0.92, 0.0012),
        "terrace_work":  (0.82, 0.98, 0.80, -0.03, 0.92, 0.0012),
        "sea_door":      (0.98, 0.92, 0.80, -0.04, 0.95, 0.0006),
        "dry_room":      (1.00, 0.90, 0.78, -0.07, 0.95, 0.0),
        "long_dry_hall": (0.86, 0.88, 0.95, -0.16, 0.85, 0.0),
        "meeting_hall":  (0.86, 0.95, 0.94, -0.09, 0.88, 0.0),
        "meeting_hall_lit": (0.96, 0.98, 0.96, 0.0, 1.0, 0.0),
        "dome_crown":    (0.78, 0.90, 1.00, -0.10, 0.90, 0.0012),
        "terraces_night": (0.74, 0.86, 1.00, -0.14, 0.88, 0.0012),
        "terrace_wrecked": (0.82, 0.95, 0.95, -0.05, 0.90, 0.0012),
        "terrace_dusk":  (0.72, 0.82, 0.95, -0.14, 0.88, 0.0012),
        "burial_kelp":   (0.82, 0.98, 0.80, -0.03, 0.92, 0.0012),
        "dome_dark_half": (0.90, 0.88, 0.95, -0.12, 0.90, 0.0),
        "net_racks":     (1.00, 0.88, 0.75, -0.05, 0.95, 0.0),
        "hall_day":      (0.95, 0.92, 0.85, -0.04, 0.95, 0.0),
        "kelp_night":    (0.74, 0.90, 0.90, -0.12, 0.90, 0.0012),
        "tangle":        (0.76, 0.92, 0.88, -0.12, 0.90, 0.0012),
        "sounding_ruin": (0.82, 0.94, 0.98, -0.04, 0.92, 0.0012),
        "slick_edge":    (1.00, 0.88, 0.70, -0.10, 0.85, 0.0012),
        "greywatch_stone": (0.82, 0.94, 1.00, -0.03, 0.92, 0.0012),
        "gallery":       (0.92, 0.96, 1.00, -0.02, 0.95, 0.0),
        "cradles":       (1.00, 0.90, 0.80, -0.06, 0.92, 0.0),
        "ice_shelf":     (0.80, 0.92, 1.00, -0.02, 0.92, 0.0012),
        "well_lip":      (0.80, 0.92, 1.00, -0.06, 0.90, 0.0),
        "kettle_house":  (1.00, 0.88, 0.90, -0.06, 0.92, 0.0),
        "kettle_interior": (1.00, 0.90, 0.76, -0.06, 0.95, 0.0),
        "workshop":      (1.00, 0.92, 0.80, -0.06, 0.95, 0.0),
        "lantern_exterior": (0.78, 0.92, 1.00, -0.10, 0.88, 0.0012),
        "lantern_hall":  (1.00, 0.96, 0.85, 0.0, 0.98, 0.0),
        "dark_hall":     (0.80, 0.88, 1.00, -0.14, 0.85, 0.0),
        "step_night":    (1.00, 0.80, 0.84, -0.10, 0.90, 0.0),
        "step_fog":      (0.88, 0.92, 0.98, -0.06, 0.80, 0.0),
        "landing_dusk":  (1.00, 0.78, 0.84, -0.12, 0.88, 0.0),
        "jef_workshop":  (0.86, 0.90, 0.94, -0.10, 0.88, 0.0),
        "landing_evening": (0.78, 0.88, 1.00, -0.12, 0.88, 0.0),
        "south_sea_ice": (0.80, 0.92, 1.00, -0.02, 0.92, 0.0012),
        "dc_canyon_above": (0.84, 0.98, 0.90, -0.03, 0.92, 0.0012),
        "dc_canyon_lit60": (0.80, 0.92, 1.00, -0.08, 0.90, 0.0012),
        "dc_high_hall":  (0.88, 1.00, 0.96, -0.02, 0.95, 0.0),
        "dc_service_tunnels": (0.88, 0.96, 0.82, -0.12, 0.88, 0.0),
        "dc_lowest_halls": (0.78, 0.98, 0.72, -0.14, 0.85, 0.0),
        "dc_heart_chamber": (0.82, 0.90, 0.98, -0.14, 0.88, 0.0),
        "dc_sea_door":   (0.86, 1.00, 0.92, -0.06, 0.92, 0.0),
        "c6_gallery_failing": (0.84, 0.90, 1.00, -0.08, 0.88, 0.0),
        "c6_gallery_stern":   (0.86, 0.90, 1.00, -0.10, 0.88, 0.0),
        "c6_gallery_nineteen": (1.00, 0.95, 0.88, -0.03, 0.92, 0.0),
        "c6_heart_under":     (0.92, 0.94, 0.90, -0.10, 0.88, 0.0),
        "c6_kelp_gold_black": (0.92, 0.88, 0.76, -0.12, 0.88, 0.0012),
        "c6_slick_inside":    (1.00, 0.86, 0.68, -0.10, 0.82, 0.0012),
        "c6_forest_beneath":  (0.82, 0.98, 0.92, -0.03, 0.92, 0.0012),
        "c7_gallery_snow":    (0.90, 0.80, 0.68, -0.10, 0.86, 0.0),
        "c7_gallery_shelves": (1.00, 1.00, 0.96, -0.02, 0.94, 0.0),
        "c7_nine_spires":     (1.00, 1.00, 1.00, -0.02, 0.95, 0.0),
        "c7_fog_landing":     (0.96, 0.94, 0.92, -0.04, 0.90, 0.0),
        "c7_smokers":         (1.00, 0.78, 0.70, -0.10, 0.84, 0.0012),
        "c7_ember_house":     (0.96, 0.92, 0.86, -0.04, 0.90, 0.0),
        "c7_ember_dusk":      (1.00, 0.72, 0.60, -0.10, 0.86, 0.0),
        "c7_hush_exterior":   (0.70, 0.86, 0.86, -0.14, 0.80, 0.0012),
        "c7_hush_hall":       (0.72, 0.86, 0.86, -0.14, 0.80, 0.0012),
        "c7_hush_room":       (0.90, 0.80, 0.70, -0.12, 0.82, 0.0012),
        "c7_hush_above":      (0.76, 0.92, 0.90, -0.12, 0.82, 0.0012),
        "c7_saltgate_kitchen": (1.00, 0.88, 0.72, -0.06, 0.90, 0.0),
        "c7_sluice_school":   (0.92, 0.92, 0.92, -0.03, 0.92, 0.0),
        "c7_concord_room":    (0.96, 0.90, 0.78, -0.06, 0.88, 0.0),
        "c7_halcyon_office":  (0.90, 0.92, 0.96, -0.03, 0.92, 0.0),
        "c7_control_hall_night": (0.80, 0.82, 0.90, -0.10, 0.84, 0.0),
        "c8_belt_under":      (0.84, 0.92, 0.90, -0.10, 0.88, 0.0012),
        "c8_belt_rain":       (0.80, 0.82, 0.92, -0.08, 0.90, 0.0),
        "c8_eye_boat":        (0.92, 1.00, 0.96, -0.02, 0.95, 0.0),
        "c8_boat_storm":      (0.78, 0.80, 0.88, -0.10, 0.88, 0.0),
        "c8_saltgate":        (1.00, 0.86, 0.96, -0.08, 0.88, 0.0),
        "c8_lock":            (0.98, 0.90, 0.96, -0.08, 0.88, 0.0),
        "c8_poster_canal":    (0.92, 0.88, 1.00, -0.08, 0.88, 0.0),
        "c8_wet_market":      (1.00, 0.94, 0.82, -0.05, 0.92, 0.0),
        "c8_sluice":          (0.84, 0.88, 1.00, -0.12, 0.84, 0.0),
        "c8_noodle_window":   (1.00, 0.90, 0.78, -0.06, 0.92, 0.0),
        "c8_brightwater_ext": (0.94, 0.94, 1.00, -0.06, 0.90, 0.0),
        "c8_lobby":           (1.00, 1.00, 1.00, 0.00, 0.95, 0.0),
        "c8_tank_room":       (0.92, 0.98, 1.00, -0.03, 0.92, 0.0),
        "c8_stair_flooded":   (0.94, 0.98, 1.00, -0.04, 0.92, 0.0),
        "c8_loading_dock":    (0.86, 0.88, 1.00, -0.10, 0.86, 0.0),
        "c8_under_market":    (0.80, 0.90, 0.88, -0.12, 0.84, 0.0),
        "c8_market_low":      (1.00, 0.90, 0.86, -0.05, 0.92, 0.0),
        "c9_lock_rain":       (0.84, 0.88, 1.00, -0.10, 0.88, 0.0),
        "c9_keelhaven_night": (1.00, 0.86, 0.72, -0.08, 0.90, 0.0),
        "c9_coal_wharf":      (1.00, 0.88, 0.76, -0.10, 0.88, 0.0),
        "c9_design_loft":     (0.86, 1.00, 0.88, -0.10, 0.88, 0.0),
        "c9_raske_office":    (0.92, 1.00, 0.88, -0.06, 0.90, 0.0),
        "c9_net_loft":        (1.00, 0.90, 0.76, -0.10, 0.88, 0.0),
        "c9_ferry_stage":     (0.88, 0.86, 0.96, -0.12, 0.86, 0.0),
        "c9_tug_storm":       (0.82, 0.88, 0.96, -0.14, 0.80, 0.0),
        "c9_eye_tugs":        (0.92, 1.00, 0.94, -0.02, 0.96, 0.0),
        "c9_lashing_water":   (0.96, 0.92, 0.92, -0.08, 0.90, 0.0),
        "c9_barge_night":     (1.00, 0.92, 0.80, -0.08, 0.90, 0.0),
        "c9_soup_barge":      (1.00, 0.90, 0.84, -0.04, 0.94, 0.0),
        "c10_planking":       (0.96, 0.98, 1.00, -0.05, 0.94, 0.0),
        "c10_frigate_deck":   (1.00, 0.93, 0.82, -0.10, 0.88, 0.0),
        "c10_frigate_overturned": (0.98, 0.92, 0.84, -0.12, 0.88, 0.0),
        "c10_lamps_swell":    (0.94, 0.92, 0.88, -0.14, 0.88, 0.0),
        "c10_storm_wall":     (0.82, 0.88, 1.00, -0.18, 0.84, 0.0),
        "c11_valley_gold":    (1.00, 0.94, 0.76, -0.04, 0.92, 0.0012),
        "c11_valley_brown":   (0.98, 0.84, 0.64, -0.10, 0.84, 0.0012),
        "c11_valley_silent":  (0.88, 0.92, 0.88, -0.08, 0.86, 0.0012),
        "c11_valley_dusk":    (0.76, 0.80, 1.00, -0.12, 0.88, 0.0012),
        "c11_valley_night":   (0.70, 0.80, 1.00, -0.16, 0.84, 0.0012),
        "c11_valley_morning": (0.88, 0.94, 1.00, -0.06, 0.88, 0.0012),
        "c12_shelves_deck":   (1.00, 1.00, 0.98, -0.02, 0.95, 0.0),
        "c12_apron":          (1.00, 0.98, 0.92, -0.03, 0.94, 0.0),
        "c12_tower_room":     (0.84, 0.88, 1.00, -0.10, 0.86, 0.0),
        "c12_tidehall_centre": (0.90, 1.00, 0.94, -0.04, 0.94, 0.0012),
        "c12_tidehall_rim_dusk": (0.82, 0.92, 1.00, -0.12, 0.88, 0.0012),
        "c13_tolla_village":     (0.80, 0.82, 0.92, -0.08, 0.90, 0.0),
        "c13_tolla_shrine":      (0.82, 0.86, 0.92, -0.10, 0.88, 0.0),
        "c13_tolla_loft":        (1.00, 0.90, 0.76, -0.10, 0.88, 0.0),
        "c13_tolla_quay_night":  (0.84, 0.88, 1.00, -0.10, 0.88, 0.0),
        "c13_concord_street":    (0.94, 0.94, 1.00, -0.06, 0.90, 0.0),
        "c13_spire_exchange":    (0.94, 0.94, 1.00, -0.06, 0.90, 0.0),
        "c13_spire_lobby":       (1.00, 1.00, 1.00, 0.00, 0.95, 0.0),
        "c13_makeup_room":       (0.96, 0.90, 0.78, -0.06, 0.88, 0.0),
        "c13_studio_one":        (0.90, 0.92, 0.96, -0.03, 0.92, 0.0),
        "c15_harbour_sunset":  (1.00, 0.76, 0.64, -0.10, 0.86, 0.0),
        "c15_school_morning":  (0.92, 0.92, 0.92, -0.03, 0.92, 0.0),
        "c15_school_afternoon": (0.98, 0.94, 0.84, -0.04, 0.92, 0.0),
        "c15_school_dusk":     (0.84, 0.84, 1.00, -0.12, 0.86, 0.0),
        "c14_concord_lobby":    (0.90, 0.94, 1.00, -0.03, 0.92, 0.0),
        "c14_concord_avenue":   (0.94, 0.94, 1.00, -0.06, 0.90, 0.0),
        "c14_sea_sunrise":      (1.00, 0.96, 0.88, -0.05, 0.92, 0.0),
        "c14_girdle_saltgate":  (0.96, 0.96, 1.00, -0.04, 0.92, 0.0),
        "c14_halcyon_caldera":  (1.00, 0.88, 0.76, -0.10, 0.88, 0.0),
        "c14_wave_mouth":       (1.00, 0.88, 0.76, -0.10, 0.88, 0.0),
        "c14_refinery_quay":    (0.96, 0.88, 0.84, -0.10, 0.86, 0.0),
        "c14_harbour_fleet":    (0.92, 0.86, 0.96, -0.12, 0.86, 0.0),
        "c14_harbour_water":    (0.92, 0.86, 0.96, -0.12, 0.86, 0.0),
        "c18_meet_empty":        (0.84, 0.88, 1.00, -0.10, 0.86, 0.0),
        "c18_dragon_square":     (1.00, 0.98, 0.92, -0.03, 0.94, 0.0),
        "c18_meet_market":       (1.00, 0.90, 0.86, -0.05, 0.92, 0.0),
        "c18_waterside_square":  (1.00, 0.98, 0.92, -0.03, 0.94, 0.0),
        "c18_canal_table":       (1.00, 0.90, 0.86, -0.05, 0.92, 0.0),
        "c18_archive_workshop":  (0.80, 0.84, 0.92, -0.10, 0.86, 0.0),
        "c18_terrace_lit":       (0.90, 0.94, 0.96, -0.10, 0.90, 0.0012),
        "c17_dead_water":     (0.90, 0.92, 0.92, -0.06, 0.88, 0.0),
        "c17_road_barges":    (0.92, 0.96, 0.98, -0.04, 0.92, 0.0),
        "c17_wall_face":      (0.90, 0.92, 0.96, -0.06, 0.90, 0.0),
        "c17_pit_view":       (1.00, 0.97, 0.92, -0.02, 0.94, 0.0),
        "c17_silt_street":    (0.90, 0.92, 0.94, -0.08, 0.88, 0.0),
        "c17_square_silt":    (1.00, 0.98, 0.94, -0.02, 0.94, 0.0),
        "c17_vault_grey":     (0.82, 0.86, 0.94, -0.14, 0.84, 0.0),
        "c17_vault_lit":      (1.00, 1.00, 1.00, 0.00, 0.96, 0.0),
        "c17_square_flooded": (0.96, 0.96, 0.98, -0.04, 0.92, 0.0),
        "c17_city_risen":     (1.00, 1.00, 1.00, -0.02, 0.95, 0.0),
        "c16_kelder_day":       (0.94, 0.95, 0.94, -0.03, 0.92, 0.0),
        "c16_kelder_evening":   (1.00, 0.76, 0.64, -0.10, 0.86, 0.0),
        "c16_saltgate_stacks":  (0.96, 0.96, 1.00, -0.04, 0.92, 0.0),
        "c16_market_dry":       (1.00, 0.94, 0.82, -0.05, 0.92, 0.0),
        "c16_sluice_dry":       (0.90, 0.90, 0.94, -0.06, 0.90, 0.0),
        "c16_lock_box":         (1.00, 0.92, 0.80, -0.06, 0.92, 0.0),
        "c16_barges_lantern":   (1.00, 0.92, 0.80, -0.08, 0.90, 0.0),
        "c16_girdle_fleet":     (0.94, 0.94, 0.96, -0.04, 0.92, 0.0),
        "c16_boat_stern":       (0.94, 0.94, 0.96, -0.04, 0.92, 0.0),
        "c16_boat_stern_evening": (1.00, 0.82, 0.70, -0.08, 0.88, 0.0),
        "c16_rafts_night":      (1.00, 0.92, 0.80, -0.08, 0.90, 0.0),
        "c4_well_descent":       (0.80, 0.90, 1.00, -0.14, 0.85, 0.0012),
        "c5_lampweed_galleries": (0.92, 0.98, 0.82, -0.08, 0.88, 0.0012),
        "c8_market_night":   (0.80, 0.86, 1.00, -0.10, 0.85, 0.0),
    }
    PORTRAIT_LIGHT_DEFAULT = (1.0, 1.0, 1.0, 0.0, 1.0, 0.0)

    # 0 = no lighting, 1 = the full table above. Skin goes sickly if this is too high.
    PORTRAIT_LIGHT_STRENGTH = 0.5

    def portrait_light(trans, st, at):
        attrs = renpy.get_attributes("bg") or ()
        r, g, b, bright, sat, amp = PORTRAIT_LIGHT.get(attrs[0] if attrs else "", PORTRAIT_LIGHT_DEFAULT)
        k = PORTRAIT_LIGHT_STRENGTH
        r, g, b = 1.0 + (r - 1.0) * k, 1.0 + (g - 1.0) * k, 1.0 + (b - 1.0) * k
        bright, sat = bright * k, 1.0 + (sat - 1.0) * k
        trans.matrixcolor = TintMatrix((int(r * 255), int(g * 255), int(b * 255))) * SaturationMatrix(sat) * BrightnessMatrix(bright)
        trans.u_amp = amp
        return 0.25

    renpy.register_shader("vn.portrait", variables="""
        uniform float u_phase;
        uniform float u_amp;
        uniform sampler2D tex0;
        attribute vec4 a_position;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 uv = v_tex_coord;
        uv.x += sin(uv.y * 24.0 + u_phase) * u_amp + sin(uv.y * 61.0 - u_phase * 1.3) * u_amp * 0.5;
        uv.y += cos(uv.x * 19.0 + u_phase * 0.8) * u_amp * 0.7;
        vec4 c = texture2D(tex0, uv);
        gl_FragColor = c * (1.0 - smoothstep(0.86, 1.0, v_tex_coord.y));
    """)

transform lit_portrait:
    mesh True
    shader "vn.portrait"
    u_amp 0.0
    u_phase 0.0
    parallel:
        function portrait_light
    parallel:
        block:
            linear 40.0 u_phase 125.66
            u_phase 0.0
            repeat
