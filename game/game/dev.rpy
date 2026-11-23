# Developer entry point for `./vn play`: when the environment variable VN_START
# names a label (for example ch02), the game skips the main menu and starts there.
# Without the variable nothing happens, so a normal player never sees this.

init python:
    import os

label splashscreen:
    $ vn_start = os.environ.get("VN_START")
    if vn_start and renpy.has_label(vn_start):
        jump expression vn_start
    return


# Reference tag, upper left: scene id and script line, so feedback can point at
# the exact place ("c06.s03, ch06.rpy:277"). Turn it off for a release by setting
# vn_show_ref to False (see docs/decisions.md, 2026-11-23).
define vn_show_ref = True

init python:
    import re as _re
    vn_ref_files = {}

    def vn_ref():
        try:
            fn, ln = renpy.get_filename_line()
        except Exception:
            return ""
        base = os.path.basename(fn)
        if not _re.match(r"ch\d\d\.rpy$", base):
            return ""
        lines = vn_ref_files.get(base)
        if lines is None:
            try:
                lines = renpy.open_file(base).read().decode("utf-8").split("\n")
            except Exception:
                lines = []
            vn_ref_files[base] = lines
        scene = ""
        for i in range(min(ln, len(lines)) - 1, -1, -1):
            m = _re.match(r"\s*#\s*(c\d\d\.s\d\d)", lines[i])
            if m:
                scene = m.group(1) + "  "
                break
        return "%s%s:%d" % (scene, base, ln)

default vn_cur_ref = ""

init python:
    def vn_ref_callback(event, interact=True, **kwargs):
        if event == "begin":
            store.vn_cur_ref = vn_ref()
    config.all_character_callbacks.append(vn_ref_callback)

screen vn_ref():
    zorder 300
    if vn_show_ref:
        if vn_cur_ref:
            text vn_cur_ref:
                xpos 14
                ypos 10
                size 24
                color "#ffffffcc"
                outlines [(2, "#000000cc", 0, 0)]

init 10 python:
    config.overlay_screens.append("vn_ref")
