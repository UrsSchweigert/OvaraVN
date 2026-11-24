# Apply log, chapter 9

Applied: must and should from style_review_ch09.md (not could).

## Counts
- Book (ch09.md): 23 applied (1 must, 22 should).
- Game (ch09.rpy): 22 applied (all except para 77, which is Game = no).
- Skipped: 2 (see below).

## Skipped
- Para 41 (first half) and para 79: "instandsetzen" -> "instand setzen". Not applied: the brief and the glossary/decision 11 keep "instandsetzen" as one word for the craft level. (The second half of para 41, the "für das niemand mehr da war, der es lehren konnte" fix, was applied.)
- All could rows left alone.

## Book only
- Para 77 "Laternen hingen in der Takelage." (Game = no; the sentence is not in the game file).

## Cross-chapter terms
- Inselleute vs Inselbewohner (para 81): glossary says Inselleute. Count before: Inselleute 13 in book chapters, Inselbewohner 8 (counted across all ch*.md at the start). Used Inselleute.
- Kohlenkai, Takelage: no cross-chapter conflict.

## Open (questions for the owner, untouched)
1. instandsetzen / instand setzen across the book (verb mostly two words elsewhere).
2. "von Ältester Oro" after a preposition.
3. Open quotation at para 45 (Raske's speech over two paragraphs; one rule for the book).
4. "Agravar-Ingenieure" vs "Ingenieure der Agravare".

## Also changed
- docs/german/review/ch09.md: German column updated for all game changes. work/german/review_ch09.md: para 77 table row updated.

## Checks
- check_translation.py 9: no flags.
- Book: 103 non-empty lines before and after; no en/em dash, no straight quotes, italics balanced; one line (47) with „ and “ unbalanced 3/2, as before (continued speech).
