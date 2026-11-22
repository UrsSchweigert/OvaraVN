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
