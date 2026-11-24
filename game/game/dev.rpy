# Developer entry point for `./vn play`: when the environment variable VN_START
# names a label (for example ch02), the game skips the main menu and starts there.
# Without the variable nothing happens, so a normal player never sees this.

init python:
    import os

# Language: the player's choice and the developer switch.
#
# The player's choice lives in Ren'Py's own language preference (Language() action
# in Preferences; saved with the persistent data, not with game saves, so every
# save loads in whichever language is on). First start only
# (persistent.vn_lang_initialised False): if the device language is German, the game
# starts in German; otherwise English. After that the flag stays True and the start
# never changes the language again.
# Device language, in this order: VN_SYSLANG (for testing, e.g. VN_SYSLANG=de),
# renpy.translation.detect_user_locale() (NSLocale on iOS and macOS), the LANG
# variables. Unknown means English.
#
# Developer switch: VN_LANG=german forces a language for this run only. The first
# forced run stores the player's current choice in persistent.vn_lang_saved; the next
# start without VN_LANG puts it back (persistent.vn_dev_lang marks "restore needed").
# A dev run never sets vn_lang_initialised, so a normal start afterwards still makes
# the first-run choice. Changing language by hand during a dev run is also undone.
default persistent.vn_dev_lang = False
default persistent.vn_lang_saved = None
default persistent.vn_lang_initialised = False

init python:
    def vn_device_language():
        """Return "german" if the device language is German, else None."""
        code = os.environ.get("VN_SYSLANG")
        if not code:
            try:
                import renpy.translation
                code = renpy.translation.detect_user_locale()[0]
            except Exception:
                code = None
        if not code:
            for key in ("LC_ALL", "LC_MESSAGES", "LANGUAGE", "LANG"):
                code = os.environ.get(key)
                if code:
                    break
        code = (code or "").strip().lower().replace("_", "-")
        if code == "de" or code.startswith("de-") or code.startswith("de."):
            return "german"
        return None

    def vn_language_startup():
        forced = os.environ.get("VN_LANG")
        if forced:
            if not persistent.vn_dev_lang:
                persistent.vn_dev_lang = True
                persistent.vn_lang_saved = _preferences.language
            renpy.change_language(forced)
            return
        if persistent.vn_dev_lang:
            persistent.vn_dev_lang = False
            renpy.change_language(persistent.vn_lang_saved)
            persistent.vn_lang_saved = None
        if not persistent.vn_lang_initialised:
            persistent.vn_lang_initialised = True
            if _preferences.language is None:
                renpy.change_language(vn_device_language())

label splashscreen:
    $ vn_language_startup()
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
