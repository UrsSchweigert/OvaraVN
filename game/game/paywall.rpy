# One-time purchase that unlocks the second half of the story.
# Chapters 1 to PAYWALL_FROM-1 are free. From PAYWALL_FROM on, the player buys
# "full_story" once (in-app purchase, non-consumable, on the App Store).
#
# The product ID below must match App Store Connect letter for letter.
# It cannot be renamed there after it is created.

define PAYWALL_FROM = 9
define PAYWALL_PRODUCT_ID = "renpy.iap.register"

init python:
    import os

    iap.register("full_story", identifier=PAYWALL_PRODUCT_ID)

    # On a computer there is no store. The game counts as unlocked, so the
    # developer can play everything. Set VN_PAYWALL=1 to test the locked path:
    # the Buy button then pretends the purchase worked.
    def paywall_simulated():
        return bool(os.environ.get("VN_PAYWALL"))

    def paywall_has_store():
        return bool(iap.get_store_name())

    def full_story_unlocked():
        if paywall_has_store():
            return iap.has_purchased("full_story")
        if paywall_simulated():
            return bool(persistent.vn_sim_unlocked)
        return True

    def chapter_locked(n):
        return n >= PAYWALL_FROM and not full_story_unlocked()

    def paywall_buy():
        if paywall_has_store():
            iap.purchase("full_story")
        else:
            persistent.vn_sim_unlocked = True

    def paywall_restore():
        if paywall_has_store():
            iap.restore()

    def _paywall_show():
        renpy.call_screen("paywall_screen")

    # Used by locked chapters on the Chapters screen.
    def paywall_from_menu():
        renpy.invoke_in_new_context(_paywall_show)
        renpy.restart_interaction()

    def paywall_price():
        return (iap.get_price("full_story") if paywall_has_store() else None) or ""

default persistent.vn_sim_unlocked = False

# The unlock screen. Returns True when the story is unlocked.
screen paywall_screen():
    modal True
    tag menu
    add gui.main_menu_background
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 60
        ypadding 50
        has vbox
        spacing 24
        xsize 1100
        text _("Unlock the rest of the story") size 56 xalign 0.5
        text _("The first chapters are free. One purchase opens the second half, for good.") size 38 xalign 0.5 text_align 0.5
        $ price = paywall_price()
        textbutton (_("Unlock") + ((" (" + price + ")") if price else "")):
            action [Function(paywall_buy), Return(True)]
            xalign 0.5
            text_size 46
        textbutton _("Restore purchase"):
            action [Function(paywall_restore), If(full_story_unlocked(), Return(True), NullAction())]
            xalign 0.5
            text_size 36
        textbutton _("Not now"):
            action Return(False)
            xalign 0.5
            text_size 36

# Put `call paywall_gate` at the top of the first paid chapter (chapter 9).
# Unlocked: it returns at once. Locked: the player sees the unlock screen,
# and "Not now" sends them to the main menu.
label paywall_gate:
    if full_story_unlocked():
        return
    $ _unlocked = renpy.call_screen("paywall_screen")
    if _unlocked and full_story_unlocked():
        return
    $ renpy.full_restart()
