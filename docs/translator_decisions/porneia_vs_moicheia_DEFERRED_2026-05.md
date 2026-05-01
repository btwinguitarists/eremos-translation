# πορνεία / πόρνος vs μοιχεία / μοιχός — DEFERRED to native-speaker review

**Status:** 🟡 DEFERRED — corpus-wide policy question requires native-Thai-speaker semantic judgment.

**Surfaced:** 2026-05-01 during 1 Corinthians end-of-book external AI review (Item G, ChatGPT + Gemini consensus). See `docs/end_of_book/1corinthians/ai_review_response_1CO_2026-05-01.md`.

---

## The question

Greek distinguishes:
- **πορνεία / πόρνος** (broad) — sexual immorality of any kind: prostitution, fornication, illicit-sex-of-any-form, including incest at 1 Cor 5:1
- **μοιχεία / μοιχός** (narrow) — adultery specifically: violation of marriage by a married person

The NT uses both, sometimes in the same context (1 Cor 6:9 explicitly distinguishes πόρνοι from μοιχοί — both terms occur in the same vice-list).

Current Eremos rendering:
- πορνεία → **การล่วงประเวณี**
- πόρνος → **คนล่วงประเวณี**
- μοιχεία → **(check current rendering)**
- μοιχός → **(check current rendering)**

---

## The concern

ChatGPT (1 Cor end-of-book review): "If Thai readers hear **การล่วงประเวณี** mainly as adultery, the translation blurs a Greek distinction that matters across Mark, Matthew, Acts, Paul, and Revelation."

The risk: `การล่วงประเวณี` may carry primarily-adultery semantics in modern Thai, which would collapse the Greek distinction between (broad) πορνεία and (narrow) μοιχεία.

---

## What we need

A native-Thai-speaker (preferably with Thai-Bible reading background) to answer:

1. Does **การล่วงประเวณี** read broadly enough in Thai-Bible register to cover prostitution + fornication + incest + general illicit-sex (the πορνεία semantic range)?
2. If yes — keep as-is.
3. If no — recommend a broader rendering for the πορνεία family. ChatGPT suggests **การผิดศีลธรรมทางเพศ** / **คนผิดศีลธรรมทางเพศ**, while reserving `การล่วงประเวณี` for the narrower μοιχεία family.

The decision should NOT be verse-by-verse. It's a corpus-wide policy.

---

## Affected verses (forward implications)

If a corpus-wide revision is approved, these verses across the NT would be touched:
- Mark 7:21 (vice-list)
- Matt 5:32 + 19:9 (porneia exception clauses — significant)
- Acts 15:20 + 15:29 + 21:25 (apostolic-decree)
- 1 Cor 5:1 (incest), 5:9-11, 6:9, 6:13, 6:18, 7:2 (broad-sexual-immorality)
- 2 Cor 12:21 (vice-list)
- Galatians 5:19 (works of flesh)
- Ephesians 5:3
- Colossians 3:5
- 1 Thessalonians 4:3
- Hebrews 12:16, 13:4
- Revelation 9:21, 14:8, 17:2, 17:4, 18:3, 18:9, 19:2, 21:8, 22:15

---

## Workflow

1. Add a B-tier YAML at `EremosVercel2/shared/review-questions/B_corpus_porneia_vs_moicheia.yml` for native-speaker review.
2. When native-speaker(s) return a verdict via the /review form, implement the corpus-wide revision (or confirm the lock) in a single PR.
3. Move this doc to `docs/translator_decisions/porneia_moicheia_2026-XX.md` (drop the DEFERRED suffix) once decided.

Until then: NO verse-level changes. Existing renderings stand as a soft-lock pending review.

---

## Cross-reference

- `docs/end_of_book/1corinthians/ai_review_response_1CO_2026-05-01.md` Item G — full reasoning
- ChatGPT external review of 1 Co audit packet, 2026-05-01
