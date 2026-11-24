# Brief: apply the optional ("could") style suggestions to the BOOK ONLY

The owner approved: apply ALL suggestions with priority `could` from work/german/style_review_chNN.md, in the BOOK TEXT ONLY (work/german/chNN.md). Do NOT touch the game translation (game/game/tl/german/*), the review tables in docs/german/review/*, or anything else. The book and the game will now differ at these places on purpose.

## Files you may edit (only your chapters)
- work/german/chNN.md
- A log work/german/apply_could_log_chNN.md.
Nothing else. No commit, no push, do not run the game, do not run renpy, no secrets.

## How
1. Read docs/german/decisions.md (binding, including the third-round answers at the end) and your style_review_chNN.md files. Take every row with Priority `could`.
2. For each row: find the exact `Current` text in work/german/chNN.md. It may differ slightly because earlier edits (the `must`/`should` rows and the owner's decisions) changed the text since the review; then locate the passage by the paragraph number and context and apply the same idea to the CURRENT text. Replace it with `Suggested` (adapted if needed). Re-read the whole sentence afterwards: articles, case, pronouns, commas, tense and rhythm must work.
3. Do NOT apply a row (log it as skipped with the reason) if: it contradicts a binding decision (names, decided terms, du/Sie, Instand setzen as two words, Land for ground, Tasse, einsetzen, Kalmare, Stille/Lautlosigkeit rule, 'Es tat ihm leid', 'Ältester' declined, no en or em dashes, „ “ typography); it changes the meaning against the English original (source/novel.md: check the English when in doubt); the passage no longer exists; or the suggestion would make the sentence worse. If a row is only a taste question and the existing wording is already fine, you may skip it with a short reason, but the default is to apply.
4. Keep the structure: same number of paragraphs, scene breaks, heading, italics (*...*) where they are. No new en or em dashes, no straight quotes, „ “ balance as before.
5. Checks: record the paragraph count of each chapter file before you start (blank-line-separated blocks excluding the heading and '---' lines) and verify it is unchanged after; no en/em dash; no straight double quotes; „ “ and * balance per paragraph as before (except the known continued-speech paragraphs in ch09, ch12, ch13). Run `python3 tools/assemble_german.py` at the end (writes work/german/novel_de.md; exit code 0).
6. Log: work/german/apply_could_log_chNN.md: counts applied/skipped, the skipped rows with the reason.

## Report (max 150 words)
Per chapter: applied / skipped; the three most notable skipped rows; check results.
