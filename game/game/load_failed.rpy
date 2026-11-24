# Shown when a save cannot be restored because the script changed after it was
# made. See config.load_failed_label in options.rpy.
label vn_load_failed:
    scene black
    with None
    "This save was made with an older version of the game and cannot be continued."
    "Choose a chapter from the Chapters menu to carry on."
    $ renpy.full_restart()
