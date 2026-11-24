# Chapter select: start the game at any chapter that has been built.
# Reachable from the main menu and from the in-game menu ("Chapters").
# A chapter counts as built when its label (ch01, ch02, ...) exists.
# `./vn play N` starts at a chapter from the command line (see dev.rpy).

init python:
    CHAPTERS = [
        (1, _("Wrack"), _("One: Washed Up")), (2, _("The Barge"), _("One: Washed Up")),
        (3, _("The Dragon"), _("Two: The Old Man")), (4, _("The Mechanic"), _("Two: The Old Man")),
        (5, _("The Lamps Go Out"), _("Three: The Dark")), (6, _("The Eldest Brother"), _("Three: The Dark")),
        (7, _("The Door"), _("Three: The Dark")),
        (8, _("Saltgate"), _("Four: Ashore")), (9, _("The Engineers"), _("Four: Ashore")),
        (10, _("The Table"), _("Four: Ashore")), (11, _("Deaf Water"), _("Four: Ashore")),
        (12, _("The Great Moot"), _("Five: One Sea")), (13, _("The Signal"), _("Five: One Sea")),
        (14, _("The Wave"), _("Five: One Sea")), (15, _("The Heart"), _("Five: One Sea")),
        (16, _("The Long Way Round"), _("Six: The Turning")), (17, _("Site Nine"), _("Six: The Turning")),
        (18, _("Meet"), _("Six: The Turning")),
    ]

    def chapter_label(n):
        return "ch%02d" % n

screen chapter_select():
    tag menu

    use game_menu(_("Chapters"), scroll="viewport"):

        vbox:
            spacing 6
            $ last_part = None
            for n, title, part in CHAPTERS:
                if part != last_part:
                    $ last_part = part
                    text _("Part [part!t]") size 34 color gui.accent_color xoffset 4 yoffset 10
                if chapter_locked(n):
                    textbutton _("Chapter [n]. [title!t]  (locked)") action Function(paywall_from_menu) text_size 40
                elif renpy.has_label(chapter_label(n)):
                    textbutton _("Chapter [n]. [title!t]") action Start(chapter_label(n)) text_size 40
                else:
                    textbutton _("Chapter [n]. [title!t]  (not built yet)") action NullAction() sensitive False text_size 40

