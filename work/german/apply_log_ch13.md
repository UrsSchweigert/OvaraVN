# Apply log, Kapitel 13

Source: style_review_ch13.md. Rule: `must` and `should` applied, `could` not.

## Counts
- must: 3 (para 4 Grassoden, para 71 "ihr vorsetzt", para 88 "Wenn sie bricht"), should: 18. Total 21 rows.
- Applied in book: 21 of 21 (rows applied mechanically from the table, then checked).
- Applied in game: 18 (all Game = yes rows) plus para 42 "in seinen beiden Händen": the table says Game = no, but the game file has the same wording, so it was changed there too.
- Book only: para 4 (Grassoden), para 6 (Höhlung).
- Skipped: none. 14 `could` rows not applied.

## Cross-chapter terms
- Fahrstuhl / Aufzug (my own harmonising, not a table row): "Aufzug" appears in ch06 and ch14, "Fahrstuhl" only in ch13 para 91 (the ch14 review wanted Fahrstuhl). By the more-frequent rule I changed ch13 para 91 to "Der Aufzug fuhr lange nach oben." (book, game, review table). Counts before: Aufzug 2, Fahrstuhl 1.
- Mole: ch09 and ch13 use "Mole"; ch14 was changed to Mole (see log ch14).

## Open questions left untouched
1. Linse / Objektiv. 2. Schreibtisch. 3. instand setzen / instandsetzen. 4. Firma / Konzern. 5. "mein Herr" (para 62).

## Checks
- `python3 tools/check_translation.py 13`: no flags.
- Book: paragraph count 96 before and after; no en or em dash, no straight quote; „ “ and `*` balance unchanged per paragraph.
- Review tables updated: docs/german/review/ch13.md and work/german/review_ch13.md.
