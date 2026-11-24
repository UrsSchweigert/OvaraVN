# Apply log, Kapitel 12

Source: style_review_ch12.md. Rule: `must` and `should` applied, `could` not.

## Counts
- must: 0. should: 25 rows (24 distinct edits; para 45 has three rows in one speech).
- Applied in book: 25 of 25 (one with an own fix, see below).
- Applied in game: 22 (all rows marked Game = yes). Book only (Game = no): para 15 (guard), para 39 (gebrannt).
- Skipped: none. 11 `could` rows not applied (by rule).

## Own fix
- Para 77: the suggested "keine Halte würde nach dem Grund fragen" trips the checker (BANNED: "fragen" near the sea). Used "keine Halte würde sich nach dem Grund erkundigen" (book, game, review table).

## Notes per row
- Para 33: closing mark after "Unterschrift ist es auch." removed in the book (speech continues in para 34). The game shows no quotes, so no game change.
- Para 12, 14, 19 etc.: game lines have no quotation marks; the same wording was changed without them.
- Review tables: docs/german/review/ch12.md German column updated; work/german/review_ch12.md updated (paras 15 and 39 in its table of new passages).

## Cross-chapter terms
- Inselbewohner / Inselleute: only `could` rows, not applied. Counts across all chapters before my edits: Inselleute 13, Inselbewohner 8 (book). Ch12 still has Inselbewohner in four places (paras 3, 11, 61, 88); the lead may decide.
- Meermann / Meermensch: glossary names "Meermensch"; applied.

## Open questions left untouched
1. Inselbewohner or Inselleute (see above). 2. "Offizier der Agravare" (para 28). 3. "niederstrecken" (paras 42, 77). 4. "mit der Ältesten Vey" (para 24). 5. "Giftmischer" (para 37).

## Checks
- `python3 tools/check_translation.py 12`: no flags.
- Book: paragraph count 97 before and after; no en or em dash, no straight quote; „ “ balance unchanged per paragraph except para 33 (intended); italic `*` unchanged.
