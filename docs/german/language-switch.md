# Language switch (English / German)

## What the player sees
- Preferences has a "Language" block (German: "Sprache") with two buttons: "English" and "Deutsch". Both names are always written the same way, in their own language, and are never translated.
- The main menu has a small "Language / Sprache" button at the bottom left. It opens Preferences.
- The choice is a Ren'Py preference. It is not stored in game saves, so every save loads in whichever language is on.

## How the default is chosen
- Only on the first start (`persistent.vn_lang_initialised` is False): if the device language is German (de, de-DE, de-AT, de-CH ...), the game starts in German. Anything else, or unknown, gives English. A language already stored in the preferences is not overwritten.
- After that the flag stays True. Later starts never change the language; the player's choice sticks.
- Device language is read in this order: `VN_SYSLANG`, then `renpy.translation.detect_user_locale()` (NSLocale `preferredLanguages` on iOS and macOS), then `LC_ALL`, `LC_MESSAGES`, `LANGUAGE`, `LANG`.
- Code: `vn_device_language()` and `vn_language_startup()` in `game/game/dev.rpy`; UI in `game/game/screens.rpy`; "Language" / "Sprache" in `game/game/tl/german/screens.rpy`.

## Developer switch
`VN_LANG=german ./vn play ...` forces a language for one run. The first forced run stores the player's choice in `persistent.vn_lang_saved`; the next start without `VN_LANG` restores it. A dev run does not set the first-run flag.

## How to test
- `VN_SYSLANG=de` simulates a German device, `VN_SYSLANG=en` an English one. Use a fresh save folder, or the choice already stored wins.
- Careful: Ren'Py reads persistent data from `game/game/saves/` as well as from `~/Library/RenPy/game-1795348692/`. To test a fresh start, copy the project to another folder and set `HOME` to an empty folder.

## Not verified
- A real iPhone with German iOS. `detect_user_locale()` needs `pyobjus` inside the iOS build; if it is missing the code falls back to the environment variables, and if those are empty the game starts in English (the safe result, and the button still works).
- The baked title image (`title_wordmark.png`) is English in both languages.
