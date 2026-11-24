# Apply decisions log (third round, 2026-11-24)

Replacements per rule. "book" = work/german/chNN.md, "game" = game/game/tl/german/chNN.rpy (German lines only), "review" = German column of docs/german/review/chNN.md (there are no review files for ch02 and ch06). Counts are replacements of a phrase, per chapter as book/game/review.

Rule 1: total book 3, game 3, review 3. Per chapter (book/game/review): ch01 1/1/1, ch07 1/1/1, ch09 1/1/1

Rule 2: total book 1, game 2, review 2. Per chapter (book/game/review): ch04 1/2/2

Rule 3: total book 7, game 7, review 11. Per chapter (book/game/review): ch04 2/2/2, ch05 0/0/3, ch09 3/3/3, ch10 1/1/1, ch16 0/0/1, ch18 1/1/1

Rule 4: total book 4, game 4, review 4. Per chapter (book/game/review): ch04 1/1/1, ch08 1/1/1, ch10 2/2/2

Rule 5: total book 2, game 2, review 2. Per chapter (book/game/review): ch01 1/1/1, ch13 1/1/1

Rule 6: total book 5, game 5, review 5. Per chapter (book/game/review): ch17 5/5/5

Rule 7: total book 2, game 2, review 1. Per chapter (book/game/review): ch02 1/1/0, ch14 1/1/1

Rule 8: total book 10, game 10, review 10. Per chapter (book/game/review): ch01 1/1/1, ch09 1/1/1, ch14 1/1/1, ch15 4/4/4, ch17 2/2/2, ch18 1/1/1

Rule 9: total book 1, game 1, review 1. Per chapter (book/game/review): ch04 1/1/1

Rule 10: total book 1, game 1, review 1. Per chapter (book/game/review): ch15 1/1/1

Rule 11: total book 3, game 3, review 3. Per chapter (book/game/review): ch07 3/3/3

## Uncertain places and the choice made

- Rule 1: Nominative uses without article stay ("sagte Ältester Oro", "Älteste Vey hat ...", "wie Ältester Oro die Lampe angesehen hatte" in ch08, "Und Ältester Oro. Er hat dich gemocht." in ch07, which reads as a listed subject). Changed only: "zu Ältester Oro" (ch01), "an Ältester Oro" (ch07), "von Ältester Oro" (ch09). Speaker labels untouched.
- Rule 3: "Instandsetzen kann ich euch beibringen" (ch09, verb in front position) became "Instand setzen kann ich euch beibringen". "Instandsetzen ist, was ich tue" (ch04) and "das Instandsetzen" (ch09) stay as nouns. "Instandsetzung" (ch12) unchanged. The review column of ch05, ch16 had older forms ("instandzusetzen", "instandsetzen") that differed from the game; they now read "instand (zu) setzen" like the game. There is no separate craft-level list in strings.rpy, common.rpy or screens.rpy; the list occurs only in the dialogue lines (ch04, ch09, ch18).
- Rule 4: Besides ch04, changed ch08 "jedes Stück Boden" (English "every bit of ground is owned", the land theme), ch10 "Zweihunderttausend Quadratkilometer Grund" and "Es gibt Grund und Tonnage" (English "ground", Rook's land). Left alone: ch09 "Nine Spires hat den Boden angeboten" (venue for the Moot, English "offered the ground"), "Kessler-Gebiet", ch07 "über Grund" (sea floor), "neutralem Boden" (ch13, neutral ground), all floors and the sea floor.
- Rule 5: Checked every place with Firma, Konzern, Gesellschaft against the English (company -> Firma, corporation -> Konzern). Only two changes: ch01 "Firmenwappen" -> "Konzernwappen" (English "corporate crest"), ch13 "tapfere Matrosen der Konzerne" -> "tapfere Firmenmatrosen" (English "brave company sailors"). All others already matched. Not changed: "Firmengeld" (scrip, with and without an English "company" word), "Gesellschaft" in ch04 (English "company" meaning companionship), "Konzerngewässern" (English "corporate waters"). ch08 "Meridian ... der Konzern, den alle mögen" refers to Brightwater, fine.
- Rule 6: Only ch17 had the group form. ch15, ch16 already say "Heiler"; ch18 "Vierzig Heilerinnen des Schweigens" stays feminine (Hush). In ch17 "Eine der Heilerinnen aus dem Schweigen" and "Eine Heilerin, die vier Stunden ... / Wenn eine Heilerin ermattete" stay feminine (English "her hands", "her"). ch07 and ch08 ("Heilerinnen" in the Hush and the hospitals) were outside the rule and untouched.
- Rule 7: Only the two "cupful" places were "Becher voll" (ch02, ch14). ch16/ch17 already "Tasse". Mugs of the old man stay "Becher".
- Rule 8: Besides ch04 (already "eingesetzt/einsetzen"), ch10 and ch06 (already fine) changed: ch01 "Sie saß schlecht" (English "seated badly", lamp), ch09 "Das hier sitzt falsch" (English "seated wrong"), ch14, ch15 (3 sentences plus "setz ihn richtig ein"), ch17 "Es sitzt falsch" and "setzte sie dorthin" -> "dort ein", ch18 "Sitzes einer Kupplung" -> "Einsetzens einer Kupplung" (English "the seating of a coupling"). ch01, ch09, ch18 are outside the chapters named by the owner but are the same word in English. ch03 "setzte Verrutschtes wieder an seinen Platz" (English "seating things that had slipped") was left, since "an seinen Platz" already says it. ch12 "seated every speaker" and ch03 "spare seat" are real seats and stay.
- Rule 9: Only the one place in ch04 ("Squid"). Other mentions of the wardens use "Wächter" and stay.
- Rule 10: Only "von ihren Rechten" (ch15) was wrong. ch13 Marit's "Starren Sie nicht hin. Sie merkt es." (English "It notices") was left: the referent is the Exchange building ("die Börse"), feminine. If the owner reads it as Meridian, it should be "Es merkt es".
- Rule 11: "Lautlosigkeit des Schlicks" kept. Three places changed (ch07 paragraphs 28, 57, 58).
- Rule 12: nothing to do.

## Checks

- tools/check_translation.py all: exit 0, no flags in all 18 chapters.
- Book paragraph counts per chapter and „ “ counts: identical to before. No en or em dashes, no straight double quotes.
- tools/assemble_german.py: exit 0, only the three known continued-speech findings (ch09, ch12, ch13).
- grep: no "Tintenfisch", no "Tut mir leid" at Maelis's line, no "reumütig", no "Becher voll", no verb "instandsetzen"/"instandzusetzen"/"instandgesetzt", no "ihren Rechten", no "Heilerinnen gingen" left.
- The game was not run and no Ren'Py translate was run.
