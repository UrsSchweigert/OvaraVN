# Chapter select: start the game at any chapter that has been built.
# Reachable from the main menu and from the in-game menu ("Chapters").
# A chapter counts as built when its label (ch01, ch02, ...) exists.
# `./vn play N` starts at a chapter from the command line (see dev.rpy).

init python:
    CHAPTERS = [
        (1, "Wrack", "One: Washed Up"), (2, "The Barge", "One: Washed Up"),
        (3, "The Dragon", "Two: The Old Man"), (4, "The Mechanic", "Two: The Old Man"),
        (5, "The Lamps Go Out", "Three: The Dark"), (6, "The Eldest Brother", "Three: The Dark"),
        (7, "The Door", "Three: The Dark"),
        (8, "Saltgate", "Four: Ashore"), (9, "The Engineers", "Four: Ashore"),
        (10, "The Table", "Four: Ashore"), (11, "Deaf Water", "Four: Ashore"),
        (12, "The Great Moot", "Five: One Sea"), (13, "The Signal", "Five: One Sea"),
        (14, "The Wave", "Five: One Sea"), (15, "The Heart", "Five: One Sea"),
        (16, "The Long Way Round", "Six: The Turning"), (17, "Site Nine", "Six: The Turning"),
        (18, "Meet", "Six: The Turning"),
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
                    text "Part " + part size 34 color gui.accent_color xoffset 4 yoffset 10
                if renpy.has_label(chapter_label(n)):
                    textbutton "Chapter [n]. [title]" action Start(chapter_label(n)) text_size 40
                else:
                    textbutton "Chapter [n]. [title]  (not built yet)" action NullAction() sensitive False text_size 40
