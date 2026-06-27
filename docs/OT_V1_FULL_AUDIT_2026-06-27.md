# OT v1.0 — Full Corpus Audit

**Generated:** 2026-06-27
**Source:** `consolidate_ot_audit.py` (Stage 1 of the OT full audit)
**Scope:** All 39 OT books, corpus-wide checks, per-book audit findings,
external AI review responses where present.

**Read-only consolidation.** No translations or rules modified.

> Chapter counts are MT versification (e.g. Joel 4, Malachi 3), read from `output/translations/` on disk.

---

## 1. Coverage matrix

| Book | Code | Chapters | EOB audit | External response |
|---|---|---:|:-:|:-:|
| genesis | GEN | 50 | yes | yes |
| exodus | EXO | 40 | yes | yes |
| leviticus | LEV | 27 | yes | yes |
| numbers | NUM | 36 | yes | yes |
| deuteronomy | DEU | 34 | yes | yes |
| joshua | JOS | 24 | yes | yes |
| judges | JDG | 21 | yes | yes |
| ruth | RUT | 4 | yes | yes |
| 1samuel | 1SA | 31 | yes | yes |
| 2samuel | 2SA | 24 | yes | yes |
| 1kings | 1KI | 22 | yes | yes |
| 2kings | 2KI | 25 | yes | yes |
| 1chronicles | 1CH | 29 | yes | yes |
| 2chronicles | 2CH | 36 | yes | yes |
| ezra | EZR | 10 | yes | yes |
| nehemiah | NEH | 13 | yes | yes |
| esther | EST | 10 | yes | yes |
| job | JOB | 42 | yes | yes |
| psalms | PSA | 150 | yes | yes |
| proverbs | PRO | 31 | yes | yes |
| ecclesiastes | ECC | 12 | yes | yes |
| songofsongs | SNG | 8 | yes | yes |
| isaiah | ISA | 66 | yes | yes |
| jeremiah | JER | 52 | yes | yes |
| lamentations | LAM | 5 | yes | yes |
| ezekiel | EZK | 48 | yes | yes |
| daniel | DAN | 12 | yes | yes |
| hosea | HOS | 14 | yes | yes |
| joel | JOL | 4 | yes | yes |
| amos | AMO | 9 | yes | yes |
| obadiah | OBA | 1 | yes | yes |
| jonah | JON | 4 | yes | yes |
| micah | MIC | 7 | yes | yes |
| nahum | NAM | 3 | yes | yes |
| habakkuk | HAB | 3 | yes | yes |
| zephaniah | ZEP | 3 | yes | yes |
| haggai | HAG | 2 | yes | yes |
| zechariah | ZEC | 14 | yes | yes |
| malachi | MAL | 3 | yes | yes |
| **Total** | | **929** | **39/39** | **39/39** |

---

## 2. Corpus-wide automated checks

Each script run against the full corpus. PASS = exit 0; FAIL = non-zero exit.
Scope notes matter for the OT — several checks were built NT-first.

### `check_key_term_consistency.py` — **PASS**

*Scope:* Greek-lemma keyed — covers NT + any OT verse carrying a `greek` field; OT Hebrew-lemma drift needs a Hebrew-aware equivalent.

### `check_phrase_consistency.py` — **PASS**

*Scope:* Thai-surface phrase drift across the whole corpus — language-agnostic, covers OT + NT (catches e.g. den-of-robbers Matt vs Jer/Mark/Luke).

### `audit_inclusion_variants.py --strict` — **PASS**

*Scope:* SBLGNT inclusion variants — NT textual-criticism scope; OT MT/LXX & Ketiv/Qere divergence is a separate dimension not covered here.

### `check_parallel_passages.py` — **PASS**

*Scope:* Parallel/synoptic + cross-testament passages — covers OT↔OT (2 Sam↔1 Chr) and OT↔NT citation parallels.

---

## 3. Per-book audit status rollup

Status-code counts pulled from each book's end-of-book audit doc.

| Book | LOCKED | STABLE | REVIEW | DECIDE |
|---|---:|---:|---:|---:|
| genesis | 34 | 17 | 20 | 15 |
| exodus | 30 | 11 | 19 | 15 |
| leviticus | 38 | 25 | 14 | 13 |
| numbers | 29 | 20 | 16 | 16 |
| deuteronomy | 56 | 16 | 20 | 31 |
| joshua | 41 | 25 | 21 | 26 |
| judges | 45 | 25 | 19 | 33 |
| ruth | 28 | 10 | 11 | 10 |
| 1samuel | 51 | 15 | 34 | 22 |
| 2samuel | 45 | 10 | 21 | 12 |
| 1kings | 32 | 16 | 26 | 18 |
| 2kings | 39 | 11 | 27 | 16 |
| 1chronicles | 40 | 15 | 26 | 15 |
| 2chronicles | 40 | 8 | 32 | 32 |
| ezra | 20 | 15 | 17 | 17 |
| nehemiah | 28 | 15 | 19 | 20 |
| esther | 22 | 13 | 18 | 14 |
| job | 22 | 13 | 13 | 9 |
| psalms | 12 | 21 | 6 | 6 |
| proverbs | 10 | 20 | 7 | 5 |
| ecclesiastes | 7 | 18 | 14 | 6 |
| songofsongs | 9 | 16 | 13 | 8 |
| isaiah | 53 | 13 | 34 | 10 |
| jeremiah | 29 | 18 | 17 | 17 |
| lamentations | 16 | 16 | 10 | 8 |
| ezekiel | 27 | 16 | 14 | 19 |
| daniel | 20 | 26 | 28 | 13 |
| hosea | 15 | 14 | 10 | 8 |
| joel | 9 | 12 | 12 | 8 |
| amos | 8 | 12 | 16 | 13 |
| obadiah | 11 | 7 | 10 | 8 |
| jonah | 24 | 15 | 14 | 9 |
| micah | 15 | 8 | 13 | 15 |
| nahum | 14 | 6 | 15 | 8 |
| habakkuk | 13 | 11 | 11 | 10 |
| zephaniah | 13 | 10 | 14 | 6 |
| haggai | 12 | 8 | 11 | 16 |
| zechariah | 12 | 10 | 7 | 6 |
| malachi | 9 | 8 | 9 | 10 |
| **Total** | **978** | **565** | **658** | **543** |

> Counts are heuristic (regex on the status word). For decision-grade detail, open the per-book audit at `docs/end_of_book/<book>/`.

---

## 4. Outstanding items by book

Per-book audit docs containing REVIEW or DECIDE flags worth a final pass:

- **genesis** (GEN) — REVIEW: 20, DECIDE: 15 — `docs/end_of_book/genesis/GEN_END_OF_BOOK_REVIEW_2026-05-11.md`
- **exodus** (EXO) — REVIEW: 19, DECIDE: 15 — `docs/end_of_book/exodus/EXO_END_OF_BOOK_REVIEW_2026-05-13.md`
- **leviticus** (LEV) — REVIEW: 14, DECIDE: 13 — `docs/end_of_book/leviticus/LEV_END_OF_BOOK_REVIEW_2026-05-15.md`
- **numbers** (NUM) — REVIEW: 16, DECIDE: 16 — `docs/end_of_book/numbers/NUM_END_OF_BOOK_REVIEW_2026-05-14.md`
- **deuteronomy** (DEU) — REVIEW: 20, DECIDE: 31 — `docs/end_of_book/deuteronomy/DEU_END_OF_BOOK_REVIEW_2026-05-16.md`
- **joshua** (JOS) — REVIEW: 21, DECIDE: 26 — `docs/end_of_book/joshua/JOS_END_OF_BOOK_REVIEW_2026-05-17.md`
- **judges** (JDG) — REVIEW: 19, DECIDE: 33 — `docs/end_of_book/judges/JDG_END_OF_BOOK_REVIEW_2026-05-19.md`
- **ruth** (RUT) — REVIEW: 11, DECIDE: 10 — `docs/end_of_book/ruth/RUT_END_OF_BOOK_REVIEW_2026-05-05.md`
- **1samuel** (1SA) — REVIEW: 34, DECIDE: 22 — `docs/end_of_book/1samuel/1SA_END_OF_BOOK_REVIEW_2026-05-22.md`
- **2samuel** (2SA) — REVIEW: 21, DECIDE: 12 — `docs/end_of_book/2samuel/2SA_END_OF_BOOK_REVIEW_2026-05-23.md`
- **1kings** (1KI) — REVIEW: 26, DECIDE: 18 — `docs/end_of_book/1kings/1KI_END_OF_BOOK_REVIEW_2026-05-23.md`
- **2kings** (2KI) — REVIEW: 27, DECIDE: 16 — `docs/end_of_book/2kings/2KI_END_OF_BOOK_REVIEW_2026-05-24.md`
- **1chronicles** (1CH) — REVIEW: 26, DECIDE: 15 — `docs/end_of_book/1chronicles/1CH_END_OF_BOOK_REVIEW_2026-05-25.md`
- **2chronicles** (2CH) — REVIEW: 32, DECIDE: 32 — `docs/end_of_book/2chronicles/2CH_END_OF_BOOK_REVIEW_2026-05-26.md`
- **ezra** (EZR) — REVIEW: 17, DECIDE: 17 — `docs/end_of_book/ezra/EZR_END_OF_BOOK_REVIEW_2026-05-27.md`
- **nehemiah** (NEH) — REVIEW: 19, DECIDE: 20 — `docs/end_of_book/nehemiah/NEH_END_OF_BOOK_REVIEW_2026-05-29.md`
- **esther** (EST) — REVIEW: 18, DECIDE: 14 — `docs/end_of_book/esther/EST_END_OF_BOOK_REVIEW_2026-05-29.md`
- **job** (JOB) — REVIEW: 13, DECIDE: 9 — `docs/end_of_book/job/JOB_END_OF_BOOK_REVIEW_2026-05-30.md`
- **psalms** (PSA) — REVIEW: 6, DECIDE: 6 — `docs/end_of_book/psalms/PSA_END_OF_BOOK_REVIEW_2026-05-31.md`
- **proverbs** (PRO) — REVIEW: 7, DECIDE: 5 — `docs/end_of_book/proverbs/PRO_END_OF_BOOK_REVIEW_2026-05-31.md`
- **ecclesiastes** (ECC) — REVIEW: 14, DECIDE: 6 — `docs/end_of_book/ecclesiastes/ECC_END_OF_BOOK_REVIEW_2026-06-04.md`
- **songofsongs** (SNG) — REVIEW: 13, DECIDE: 8 — `docs/end_of_book/songofsongs/SNG_END_OF_BOOK_REVIEW_2026-06-04.md`
- **isaiah** (ISA) — REVIEW: 34, DECIDE: 10 — `docs/end_of_book/isaiah/ISA_END_OF_BOOK_REVIEW_2026-06-05.md`
- **jeremiah** (JER) — REVIEW: 17, DECIDE: 17 — `docs/end_of_book/jeremiah/JER_END_OF_BOOK_REVIEW_2026-06-21.md`
- **lamentations** (LAM) — REVIEW: 10, DECIDE: 8 — `docs/end_of_book/lamentations/LAM_END_OF_BOOK_REVIEW_2026-06-04.md`
- **ezekiel** (EZK) — REVIEW: 14, DECIDE: 19 — `docs/end_of_book/ezekiel/EZK_END_OF_BOOK_REVIEW_2026-06-25.md`
- **daniel** (DAN) — REVIEW: 28, DECIDE: 13 — `docs/end_of_book/daniel/DAN_END_OF_BOOK_REVIEW_2026-05-29.md`
- **hosea** (HOS) — REVIEW: 10, DECIDE: 8 — `docs/end_of_book/hosea/HOS_END_OF_BOOK_REVIEW_2026-06-26.md`
- **joel** (JOL) — REVIEW: 12, DECIDE: 8 — `docs/end_of_book/joel/JOL_END_OF_BOOK_REVIEW_2026-06-26.md`
- **amos** (AMO) — REVIEW: 16, DECIDE: 13 — `docs/end_of_book/amos/AMO_END_OF_BOOK_REVIEW_2026-06-26.md`
- **obadiah** (OBA) — REVIEW: 10, DECIDE: 8 — `docs/end_of_book/obadiah/OBA_END_OF_BOOK_REVIEW_2026-06-26.md`
- **jonah** (JON) — REVIEW: 14, DECIDE: 9 — `docs/end_of_book/jonah/JON_END_OF_BOOK_REVIEW_2026-05-09.md`
- **micah** (MIC) — REVIEW: 13, DECIDE: 15 — `docs/end_of_book/micah/MIC_END_OF_BOOK_REVIEW_2026-06-26.md`
- **nahum** (NAM) — REVIEW: 15, DECIDE: 8 — `docs/end_of_book/nahum/NAM_END_OF_BOOK_REVIEW_2026-06-26.md`
- **habakkuk** (HAB) — REVIEW: 11, DECIDE: 10 — `docs/end_of_book/habakkuk/HAB_END_OF_BOOK_REVIEW_2026-06-26.md`
- **zephaniah** (ZEP) — REVIEW: 14, DECIDE: 6 — `docs/end_of_book/zephaniah/ZEP_END_OF_BOOK_REVIEW_2026-06-27.md`
- **haggai** (HAG) — REVIEW: 11, DECIDE: 16 — `docs/end_of_book/haggai/HAG_END_OF_BOOK_REVIEW_2026-06-27.md`
- **zechariah** (ZEC) — REVIEW: 7, DECIDE: 6 — `docs/end_of_book/zechariah/ZEC_END_OF_BOOK_REVIEW_2026-06-27.md`
- **malachi** (MAL) — REVIEW: 9, DECIDE: 10 — `docs/end_of_book/malachi/MAL_END_OF_BOOK_REVIEW_2026-06-27.md`

---

## 5. Per-chapter check warnings

Warnings or failures from per-chapter summary JSONs (if any).

None. All shipped chapters have clean summary JSONs.

---

## 6. Next: Stage 2 polish sweep

Stage 1 is mechanical consolidation. Thai-flow micro-issues are caught in Stage 2.
(`polish_review.py` was authored NT-first; confirm it handles OT books before a full run.)

```
python3 scripts/polish_review.py --book <slug>     # one book
python3 scripts/polish_review.py --all              # all books
```

Stage 2 writes proposals to `output/polish_proposals/` only. Translation files are NOT modified until you run `apply_polish_deltas.py` with explicit approvals.
