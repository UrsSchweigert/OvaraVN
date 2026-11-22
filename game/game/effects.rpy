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
# Portraits are drawn evenly lit on grey, so they look stuck onto the scene. They
# are shown on their own layer ("portraits"), and that layer is lit to match
# whichever background is showing: tinted, a little darker, and under water
# given the same light ripple as the scene. The bottom edge fades softly.
# Nothing in the story script needs to change.

init python:
    config.layers = ["master", "portraits", "transient", "screens", "overlay"]
    config.tag_layer = dict(getattr(config, "tag_layer", {}) or {})
    for _t in ("left", "right", "bother"):
        config.tag_layer[_t] = "portraits"

    # background name -> (tint r, g, b, brightness, saturation, ripple)
    PORTRAIT_LIGHT = {
        "kelp_forest":   (0.80, 0.98, 0.78, -0.03, 0.92, 0.0012),
        "terraces_dome": (0.80, 0.96, 0.92, -0.02, 0.92, 0.0012),
        "terrace_work":  (0.82, 0.98, 0.80, -0.03, 0.92, 0.0012),
        "sea_door":      (0.98, 0.92, 0.80, -0.04, 0.95, 0.0006),
        "dry_room":      (1.00, 0.90, 0.78, -0.07, 0.95, 0.0),
        "long_dry_hall": (0.86, 0.88, 0.95, -0.16, 0.85, 0.0),
        "meeting_hall":  (0.86, 0.95, 0.94, -0.09, 0.88, 0.0),
    }
    PORTRAIT_LIGHT_DEFAULT = (1.0, 1.0, 1.0, 0.0, 1.0, 0.0)

    def portrait_light(trans, st, at):
        attrs = renpy.get_attributes("bg") or ()
        r, g, b, bright, sat, amp = PORTRAIT_LIGHT.get(attrs[0] if attrs else "", PORTRAIT_LIGHT_DEFAULT)
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
        gl_FragColor = c * (1.0 - smoothstep(0.82, 0.935, v_tex_coord.y));
    """)

    def _light_portraits():
        renpy.show_layer_at(portrait_layer, layer="portraits")

    config.start_callbacks.append(_light_portraits)
    config.after_load_callbacks.append(_light_portraits)

transform portrait_layer:
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
