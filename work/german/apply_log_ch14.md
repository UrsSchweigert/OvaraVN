# Apply log, Kapitel 14

Source: style_review_ch14.md. Rule: `must` and `should` applied, `could` not.

## Counts
- must: 1 (para 48, "Wir haben nicht darum gebeten"), should: 24 rows. Total 25 rows.
- Applied in book: 24. Applied in game: 24 (all rows were Game = yes).
- Skipped: 1, para 1 "Aufzug" to "Fahrstuhl": see cross-chapter terms.
- 12 `could` rows not applied.

## Own fixes
- Para 14: the game splits "Diesmal hielt er nicht für ihn an." and "Er bat ihn nicht darum." over two boxes; changed to "der Drache" and "Ilan" in each box.

## Cross-chapter terms
- Aufzug / Fahrstuhl: counts before: Aufzug 2 (ch06, ch14), Fahrstuhl 1 (ch13). Rule: more frequent wins, so ch14 keeps "Aufzug" and ch13 was changed to "Aufzug" (see log ch13). Row skipped.
- Mole / Wellenbrecher: ch09 and ch13 say "Mole" (2), "Wellenbrecher" only in ch14 (3, all mine). Changed to "Mole" in paras 59, 67, 77 (book, game, review table).

## Open questions left untouched
1. "der Kraterrand" doubling (para 24). 2. Firma / Konzern (para 72). 3. "falsch eingesetzt" (para 74). 4. "Becher voll" / "Handvoll" (para 70).

## Checks
- `python3 tools/check_translation.py 14`: no flags.
- Book: paragraph count 88 before and after; no en or em dash, no straight quote; „ “ and `*` balance unchanged per paragraph.
- Review tables updated: docs/german/review/ch14.md (work/german/review_ch14.md had no hits).
