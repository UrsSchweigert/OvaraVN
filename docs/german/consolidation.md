# German version: consolidation report

Status: working report for the owner. Nothing here is approved. All 18 chapters are translated; this pass made them agree and completed the shared files.

## 1. The short version

- The 18 chapter files, the strings file and the interface files are complete and consistent. Ren'Py lint, `./vn check`, `tools/check_script.py` (English unchanged, all 18 chapters) and `tools/check_translation.py all` all pass with no flags.
- I found no du/Sie mistakes against the final rules. I changed nothing there.
- I made 26 small text fixes in the chapter files (21 terms, 4 refrain lines, 1 grammar error). Each is listed in section 5.
- Eleven choices are yours (section 7). I left those texts as they are.

## 2. What I merged

**`game/game/tl/german/strings.rpy`**: now 45 entries, no duplicates with the other tl files.
- 21 speaker labels: Junge, Nachtschicht, Alte Frau, Frau aus Fallow, Offizierin, Frau mit der Tonpfeife, Mädchen mit der Harpune, Frau aus dem Maschinenbau, Mann vom Rumpfbau, Dicker alter Mann, Junger Mann aus Fallow, Alter Rufer aus Fallow, Ältester Oro, Älteste Vey, Sprecher von Kelder, Oberste Schleusenwärterin, Alter vom Nudelstand, Mann in Grau, Hauptmann, Heilerin. All other labels are names and stay.
- 16 chapter titles. "Wrack", "Saltgate" and "Meet" stay as they are, so they need no entry.
- 6 part titles (Eins: Angespült ... Sechs: Die Wende) plus the heading "Teil [part]".
- The chapter menu strings: "Kapitel [n]. [title]", "(gesperrt)", "(noch nicht fertig)".
- "A novel of Ovara" and "The End": neither is shown by the game. "The End" is translated in place in chapter 18 ("Ende"). The subtitle is not displayed anywhere, so I added no entry.

**`game/game/chapter_select.rpy`** (the one English-side file I edited): every chapter title and part title is now wrapped in `_()`, and the three chapter strings and the part heading use the same `[title!t]` / `[part!t]` pattern already used for chapters 2 and 6. English output is unchanged: "Part One: Washed Up", "Chapter 2. The Barge". I checked this by reading the diff and by running `check_script.py`.

**Interface files** (`screens.rpy`, `common.rpy`, `options.rpy`, `paywall.rpy`, `load_failed.rpy`): 409 strings. 175 of the 319 in `common.rpy` and all of `screens.rpy`, `options.rpy`, `paywall.rpy` and `load_failed.rpy` are now German. Where the Ren'Py SDK launcher ships German (115 strings) I reused its wording, with two changes: lower-case "du" (the SDK writes "Du"), and the glossary's words for Skip (Überspringen), History (Verlauf) and Unseen Text (Ungelesener Text). Menu and button words follow the glossary: Starten, Laden, Speichern, Kapitel, Einstellungen, Hauptmenü, Info, Hilfe, Beenden, Zurück. The paywall and the load-failed note use the glossary's proposed texts (the note is "Wähle im Menü „Kapitel“ ein Kapitel, um weiterzuspielen."). The book title string is "Der Mann, den die Flut brachte".
- Left in English on purpose: about 140 developer-only strings in `common.rpy` (interactive director, renderer choice, traceback and update screens). A player does not meet them.

## 3. Conflict table (terms rendered differently across chapters)

"Fixed" means I changed the chapters to agree. "Agreed" means the chapters already agreed. "Owner" means it is your choice (section 7).

| Term | Variants found | Chosen | Result |
|---|---|---|---|
| paper | Papier, Schuldscheine, Flugblatt, Blatt, Schuldtitel | by sense: a contract a hold or person signs or marks = Papier (ch05, 06, 07, 09, 11, 16); the purple notice = Flugblatt (ch09, 10, 12, 13; "das Blatt" only in Odile's and Ilan's short references in ch12); Meridian's/Halcyon's notes of debt = Schuldscheine (ch08, 10, 13) | Agreed. Two lines are unclear: ch11 line 21 ("third line of the paper") and ch16 line 4 ("That had been in the paper"). Owner |
| indenture | Dienstvertrag (ch09), Knechtschaftsvertrag (ch13) | Dienstvertrag | Fixed (ch13 line 96). Owner may prefer Knechtschaftsvertrag |
| design loft | Konstruktionshalle (ch09, ch17) | same | Agreed |
| net loft / net-store / fish-loft | Netzboden, Netzschuppen, Fischspeicher | different English words | Agreed |
| barge | Lastkahn (the Halcyon dump barge); Kahn (other boats, soup barge) | as the translators already had it | Agreed |
| gate barge | Schleusenkahn (ch16), Torkahn (ch17) | Schleusenkahn | Fixed (ch17 lines 43, 220) |
| eels | Aale, Schlickaale (once, ch03) | Aale; Schlickaale where the text says "slick eels" | Agreed |
| apron (stone landing) | Kai, Handelskais | Kai | Agreed |
| Bright Shelves | Hellen Schelfe (all chapters; "Schelf" for "shelf") | Hellen Schelfe | Agreed. Still open in decisions.md. Owner |
| the Pale | Bleiche (ch03, 07, 18) | Bleiche | Agreed. Still open. Owner |
| silence | Lautlosigkeit (dead water), Stille (plain silence, and the region "die Stille") | split by sense | Agreed. Owner (section 7) |
| Elder (title) | Ältester Oro, Älteste Vey, "der Ältesten Vey" | as in decisions.md | Agreed |
| Mend / Make / Tend | hegen, instandsetzen, erbauen; spelling of "instand setzen" varied (instandsetzen, instand setzen, instandzusetzen) | verb in running text is two words ("setzte instand", "instand zu setzen", "instand setzen lassen"); the craft level, the lists and the noun stay one word ("hegen, instandsetzen, erbauen", "das Instandsetzen") | Fixed (ch05 lines 137, 146, 161; ch16 line 78) |
| sea-silk | Meerseide (all) | same | Agreed |
| long-call | Langruf (all) | same | Agreed |
| Tidecaller | Flutruferin (once) | same | Agreed |
| Breakers | Brecher (all) | same | Agreed |
| Shallowborn | Flachgeborener (once) | same | Agreed |
| Captain | Hauptmann (Meridian soldiers: ch13, ch18); Kapitän (ship captains: ch16, ch17) | as the translators already had it | Agreed |
| Healer | Heiler / Heilerin / Heilerinnen by sex and group | same | Agreed |
| Kanyon | Kanyon, Chorkanyon (all) | same | Agreed |
| Chorus | always "Deep Chorus" | same | Agreed |
| the Spires | "Nine Spires" kept; ch17 "taller than the Spires" = "höher als die Türme" | left | Owner (minor) |
| Dragon | der Drache, "er" | same | Agreed |
| needle / cradle | Nadel, Wiege | same | Agreed |
| an old pattern (needle type) | alte Bauart (ch06, 14, 18); "altes Muster" (ch04, 2 lines) | alte Bauart | Fixed (ch04 lines 219, 386) |
| Tender | Heger / Hegerin (ch02 only) | same | Agreed |
| Mighty | die Mächtige / der Mächtige / die Mächtigen | same | Agreed |
| Hold | die Halte / die Halten (never "Hort") | same | Agreed; awkward lines listed below |
| healer's grey band | Armband (glossary, ch08, ch11, ch17); Band (ch05, ch07, ch12) | Armband | Fixed (ch05 lines 78, 82, 134; ch07 line 3; ch12 lines 28, 101, 148) |
| landing (needle moorings at the Well) | Anlegestelle (ch04, 08, 09); Anlegeplatz (ch05) | Anlegestelle | Fixed (ch05 line 30). The Dragon's own stop stays "Landeplatz" (ch03, ch07) |
| tide line | Flutlinie (ch09, 12); Flutsaum (ch14) | Flutlinie | Fixed (ch14 line 31) |
| charter | Charta (ch13); Satzung (ch18) | Charta | Fixed (ch18 line 4) |
| still-room | Vorratskammer (ch04); Destillierkammer (ch07) | Vorratskammer (it adds no fact) | Fixed (ch07 line 52) |
| hamper | Korb (ch09); Proviantkorb (ch10) | Proviantkorb | Fixed (ch09 line 158) |
| Dr. Marsh | "Dr. Marsh" in ch10, 16, 18; "Linnea Marsh" at first mention | same | Agreed |
| "Teach everybody. Teach people you don't like." | three different wordings (ch04, ch09, ch15) | "Lehre jeden. Lehre Menschen, die du nicht magst." | Fixed (ch04 line 361, ch09 line 129, ch15 line 139, ch18 line 58) |

Refrains checked and already identical wherever they recur: the Rule ("Hüte das Wasser. Besitze nichts, was du nicht tragen kannst. Komm, wenn du gerufen wirst."), "Bitte. Befiehl nicht.", "Ich würde ihn gern laufen sehen." (Rook), Yeva's two lines (ch08 and ch14), Maelis's question (ch07, ch16, and ch18 in the past form), "fremde Hände, sag es Jef" (long-calls), "Hegen, instandsetzen, erbauen" (ch04, ch09, ch18).

Words that are the same in every chapter and need no decision: Fadenträger, Faden, Agravare, Meerleute, Plagegeist, Bittertang, Luftherz, Wärmestein, Lampentang, Erbauer-, Fluthund, Rufstein, Almanach, gebundenes Wasser, Waisenwasser, Firmengeld, Wasserlinie, Kraterrand, Taucheranzug, Brunnenwanderer, Laterne, Brunnen, Schweigen (Hush).

**"Halte" read as a noun.** I checked all 142 uses. Each has an article or adjective in front of it, so none reads as the verb. The three most awkward lines (the noun beside the craft word "Halten" or the verb "halten"):
- ch04 line 359: "... ich habe es eng bei mir gehalten ... ich habe die Halten angefleht".
- ch05 line 110: "... in jede geflutete Galerie der unteren Halte ... dort zu halten".
- ch12 line 124: "... hatte hinausgegriffen und genommen und gehalten, und das Halten hatte ihn ausgehöhlt" (here "Halten" is the craft, so it is correct, but it sits near "Halte" in the same scene).

## 4. du / Sie audit

Method: I read every dialogue line that has a speaker label in all 18 files, split the speakers into Threaded and not Threaded (Wrack from ch04 line 373, "He woke in the box bed"), and checked (a) every formal form (Sie, Ihnen, Ihr, Ihre ...) said by a Threaded speaker, (b) every du/ihr form said by a non-Threaded speaker to find the addressee, (c) capitalisation (no capital "Du/Euer" in the middle of a sentence).

Result: no violations. All formal forms from Threaded speakers are Wrack's, before the Thread, to Jef, Maelis and Anselm (ch04 lines 182, 205, 270, 274, 301, 356). That is correct under rule 2. Jef and Maelis say du to everyone (4b), Hesper and Wrack/Ilan say du both ways (4c), Sefa/Wrack/Ione and Okonta/Wrack say du (4), and Maelis says du to Ilan in ch07, ch16, ch17 and ch18 (the ch18 translator feared ch07 still had Sie; it does not).

**Fixes made: none.**

**Judgement calls for you** (the text follows the rules; the rules need an age or a status the text does not give):
1. Davin and Wrack say du to each other in ch02 (about 45 and 38, both not Threaded).
2. Brask says Sie to Wrack and Wrack says du to Brask in ch03 (Brask "a young man", Wrack not yet Threaded).
3. Marsh and Yeva say du to each other in ch08 (no ages given).
4. Sefa says Sie to Maelis in ch16 line 128 (both not Threaded; younger to older). Maelis says du to Sefa (4b). Everywhere else Sefa has no direct "you" to Maelis.
5. The old man at the noodle stall says Sie to Ilan in ch16 although he knew Ilan as a boy.
6. The old caller of Fallow says Sie to Ilan in ch11 (the text does not say whether he is Threaded).
7. Crane says du to the sergeant (ch17), and Marit says Sie to the Meridian captain (ch13): ages not given.
8. Odo/Garran in ch17: the labels at lines 40 and 42 say Odo, but line 39 says Odo handed his trumpet to Garran and line 41 describes "the big man" speaking. That points to Garran. The German follows the label (Odo) and says "Mir hat man es auch versprochen, Jungs". It reads the same either way. Please check the English script label.
9. The unnamed tall grey woman in ch15 line 38 ("Lass ihn") is probably Maelis. "Lass ihn" is du either way, so the text is right whoever she is.
10. Ilan speaks "ihr" to the public in the ch13 broadcast and to the Moot (rule 1, Threaded says du/ihr).
11. Sefa/Ione to callers ("enough from you, sit down", ch17): du to a mixed group.

## 5. Every text fix I made in the chapter files

| Chapter and line | Before | After | Why |
|---|---|---|---|
| ch04 219 | Es ist ein altes Muster. | Es ist eine alte Bauart. | "old pattern" = Bauart (ch06, 14, 18) |
| ch04 386 | Altes Muster. | Alte Bauart. | same |
| ch04 361 | Bring es allen bei. Bring es Leuten bei, die du nicht magst. | Lehre jeden. Lehre Menschen, die du nicht magst. | Jef's rule line, same words as ch09 and ch15 |
| ch05 30 | zum Anlegeplatz | zur Anlegestelle | landing, as ch04 |
| ch05 78, 82, 134 | graue(s) Band | graue(s) Armband | healer's band |
| ch05 137 | instandzusetzen | instand zu setzen | spelling of the verb |
| ch05 143 | hinunter ins Krankenstation | hinunter in die Krankenstation | grammar (die Krankenstation) |
| ch05 146, 161 | nicht instandsetzen | nicht instand setzen | spelling |
| ch07 3 | graue Band | graue Armband | healer's band |
| ch07 52 | Destillierkammer | Vorratskammer | still-room, as ch04 |
| ch09 129 | Lehre jeden. Lehre auch Menschen ... | Lehre jeden. Lehre Menschen ... | no added "auch" |
| ch09 158 | ein Korb | ein Proviantkorb | hamper, as ch10 |
| ch12 28, 101, 148 | Band | Armband | healer's band |
| ch13 96 | Knechtschaftsvertrag | Dienstvertrag | indenture, as ch09 |
| ch14 31 | Flutsaum | Flutlinie | tide line |
| ch15 139 | Lehre auch Menschen ... | Lehre Menschen ... | no added "auch" |
| ch16 78 | instandsetzen lassen | instand setzen lassen | spelling |
| ch17 43, 220 | Torkahn | Schleusenkahn | gate barge |
| ch18 4 | keine Satzung | keine Charta | charter |
| ch18 58 | unterrichten | lehren | echo of Jef's rule |

Counts: 26 replacements in 26 lines (term/consistency 21, refrain 4, grammar 1; the spelling fixes of "instand setzen" are counted as term fixes). Every change was an exact one-place replacement in the German line only; the English comments and ids are untouched.

Checks run on all chapters with no problems found: balanced „ “ and ‚ ‘, no straight quotes, no en or em dashes, interrupted speech always written "Wort -", {i} counts identical to the English in every line, interpolations identical, no German line over 420 characters, no double spaces, no space before punctuation.

## 6. Tool change

`tools/check_translation.py` now has an `all` mode (chapters 1 to 18, one summary each) and a new flag for unbalanced German quotes. Nothing else changed.

## 7. Owner decisions needed

Each item has two options and my recommendation. The text stays as it is until you answer.

1. **"paper", by sense.** (a) As now: Papier for a contract, Flugblatt for the purple notice, Schuldscheine for debt notes. (b) Use "Dokument" for the contract. Recommendation: (a). Please also look at ch11 line 21 and ch16 line 4, where the English "the paper" could be the purple notice (then "Flugblatt") or the contract (then "Papier"). I left "Papier".
2. **"indenture".** (a) Dienstvertrag (now). (b) Knechtschaftsvertrag (stronger, bonded labour). Recommendation: (a); ch13's list of debts ("Jeder Dienstvertrag, jede Hypothek") reads a little mild.
3. **The Pale** (Bleiche) and **Bright Shelves** (Hellen Schelfe), still open. Recommendation: keep both.
4. **Stille and Lautlosigkeit.** Now: Lautlosigkeit for the dead sound of the Slick and dead water, Stille for ordinary silence, and "die Stille" is also the region. Two lines can read as the region: ch12 line 81 ("erhob sich in die Stille hinein") and ch11 line 136. (a) Keep. (b) Use "Ruhe" or "Schweigen" for those two. Recommendation: (a).
5. **"Wrack" and shipwrecks.** ch03 (lines 34, 54) says "Schiffswracks". ch11 avoided the word. (a) Keep "Schiffswracks". (b) "gesunkene Schiffe" in ch03. Recommendation: (b) if you want the hero's name to stand alone; otherwise (a) as a quiet echo.
6. **Sefa to Maelis: Sie** (ch16 line 128). (a) Sie (now, rule 3). (b) du, like Sefa and Wrack/Ione. Recommendation: (b) would be warmer, but (a) follows the rule you gave.
7. **Marsh and Yeva** say du to each other (ch08). (a) du (now). (b) Sie. Recommendation: (a), they share a past.
8. **"Sorry" as "Reumütig"** (Maelis's one word, ch04). (a) Reumütig (now). (b) "Tut mir leid". Recommendation: (a).
9. **"Meet" in ch18** box 37 ("Sie nannten die Stadt Meet"): the sense "treffen" is lost. (a) Keep (decision 10). (b) Add a clause. Recommendation: (a).
10. **Quick-menu word "Prefs"**: (a) Optionen (the Ren'Py word, now); (b) Einstellungen (same as the long menu, but wide on a phone). Recommendation: (a).
11. **Odo or Garran** at ch17 lines 40 and 42 (a label question in the English script, not in the German). Tell me or the builder which is right.
12. **Small word pairs** where two chapters used different words for the same English and I picked one (list in section 3). If you prefer the other word, I can switch: Charta/Satzung, Flutlinie/Flutsaum, Schleusenkahn/Torkahn, Vorratskammer/Destillierkammer.

## 8. Remaining doubts and what I could not check

- I did not run the game. I did not check the German text boxes on screen (length, German quote glyphs „ “ ‚ ‘ in the game font, the word "Armband am Arm", which is a little redundant but follows the English).
- Lint passes, but lint does not prove the chapter menu strings show in German. A quick look at the Chapters screen with the language set to German would confirm "Teil Eins: Angespült" and "Kapitel 2. Der Lastkahn".
- The 140 developer strings left in English in `common.rpy` and one long accessibility string (the key differs slightly from the stock text) are not player-facing in normal play.
- I did not re-read every line of the 3,605. I read the term files, address files, and every line that matched a grep for the terms and forms of address above, and about 30 randomly chosen long lines for tone. Quality in those samples was good.
- Terms from the translators' own lists that I did not touch: Messuhren, Paneel, Hafenambulanz, Aufnahmeleiter, Zweiundzwanzig Jahre Investition, die Leere (two meanings in ch12), "die Erste" in ch18 (an unclear English phrase). They are in `glossary_additions.md`.
