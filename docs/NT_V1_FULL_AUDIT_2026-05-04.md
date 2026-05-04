# NT v1.0 — Full Corpus Audit

**Generated:** 2026-05-04
**Source:** `consolidate_nt_audit.py` (Stage 1 of run_nt_full_audit)
**Scope:** All 27 NT books, corpus-wide checks, per-book audit findings,
AI review responses where present.

**Read-only consolidation.** No translations or rules modified.

---

## 1. Coverage matrix

| Book | Code | Chapters expected | Shipped | EOB audit | External response |
|---|---|---:|---:|:-:|:-:|
| matthew | MAT | 28 | 28 | yes | yes |
| mark | MRK | 16 | 16 | yes | yes |
| luke | LUK | 24 | 24 | yes | yes |
| john | JHN | 21 | 21 | yes | yes |
| acts | ACT | 28 | 28 | yes | yes |
| romans | ROM | 16 | 16 | yes | yes |
| 1corinthians | 1CO | 16 | 16 | yes | yes |
| 2corinthians | 2CO | 13 | 13 | yes | yes |
| galatians | GAL | 6 | 6 | yes | yes |
| ephesians | EPH | 6 | 6 | yes | yes |
| philippians | PHP | 4 | 4 | yes | yes |
| colossians | COL | 4 | 4 | yes | yes |
| 1thessalonians | 1TH | 5 | 5 | yes | yes |
| 2thessalonians | 2TH | 3 | 3 | yes | — |
| 1timothy | 1TI | 6 | 6 | yes | yes |
| 2timothy | 2TI | 4 | 4 | yes | yes |
| titus | TIT | 3 | 3 | yes | yes |
| philemon | PHM | 1 | 1 | yes | yes |
| hebrews | HEB | 13 | 13 | yes | — |
| james | JAS | 5 | 5 | yes | yes |
| 1peter | 1PE | 5 | 5 | yes | yes |
| 2peter | 2PE | 3 | 3 | yes | yes |
| 1john | 1JN | 5 | 5 | yes | — |
| 2john | 2JN | 1 | 1 | yes | — |
| 3john | 3JN | 1 | 1 | yes | — |
| jude | JUD | 1 | 1 | yes | — |
| revelation | REV | 22 | 22 | yes | — |
| **Total** | | **260** | **260** | **27/27** | **20/27** |

---

## 2. Corpus-wide automated checks

Each script run against the full corpus. PASS = exit 0; FAIL = non-zero exit.

### `check_key_term_consistency.py ` — **PASS**

### `check_phrase_consistency.py ` — **PASS**

### `audit_inclusion_variants.py --strict` — **PASS**

### `check_parallel_passages.py ` — **PASS**

---

## 3. Per-book audit status rollup

Status-code counts pulled from each book's end-of-book audit doc.

| Book | LOCKED | STABLE | REVIEW | DECIDE |
|---|---:|---:|---:|---:|
| matthew | 11 | 7 | 4 | 0 |
| mark | 13 | 2 | 0 | 1 |
| luke | 5 | 19 | 1 | 1 |
| john | 13 | 15 | 16 | 8 |
| acts | 8 | 7 | 7 | 6 |
| romans | 33 | 22 | 9 | 20 |
| 1corinthians | 1 | 4 | 5 | 2 |
| 2corinthians | 24 | 19 | 7 | 4 |
| galatians | 34 | 24 | 10 | 7 |
| ephesians | 45 | 17 | 19 | 13 |
| philippians | 38 | 21 | 16 | 13 |
| colossians | 52 | 22 | 15 | 15 |
| 1thessalonians | 29 | 22 | 6 | 6 |
| 2thessalonians | 1 | 11 | 1 | 1 |
| 1timothy | 33 | 27 | 17 | 15 |
| 2timothy | 57 | 16 | 13 | 8 |
| titus | 71 | 8 | 16 | 6 |
| philemon | 1 | 7 | 5 | 2 |
| hebrews | 33 | 32 | 11 | 16 |
| james | 32 | 12 | 22 | 15 |
| 1peter | 34 | 27 | 14 | 14 |
| 2peter | 70 | 23 | 12 | 16 |
| 1john | 36 | 22 | 13 | 14 |
| 2john | 17 | 13 | 13 | 12 |
| 3john | 27 | 20 | 15 | 7 |
| jude | 40 | 23 | 12 | 13 |
| revelation | 20 | 13 | 10 | 3 |
| **Total** | **778** | **455** | **289** | **238** |

> Token counts are heuristic (regex match on the status word in the doc). For decision-grade detail, open the per-book audit at `docs/end_of_book/<book>/`.

---

## 4. Outstanding items by book

Per-book audit docs containing REVIEW or DECIDE flags worth a final pass:

- **matthew** (MAT) — REVIEW: 4, DECIDE: 0 — `docs/end_of_book/matthew/MAT_END_OF_BOOK_REVIEW_2026-04-19.md`
- **mark** (MRK) — REVIEW: 0, DECIDE: 1 — `docs/end_of_book/mark/MRK_END_OF_BOOK_REVIEW_2026-04-26.md`
- **luke** (LUK) — REVIEW: 1, DECIDE: 1 — `docs/end_of_book/luke/LUK_END_OF_BOOK_REVIEW_2026-04-22.md`
- **john** (JHN) — REVIEW: 16, DECIDE: 8 — `docs/end_of_book/john/JHN_END_OF_BOOK_REVIEW_2026-04-30.md`
- **acts** (ACT) — REVIEW: 7, DECIDE: 6 — `docs/end_of_book/acts/ACT_END_OF_BOOK_REVIEW_2026-04-26.md`
- **romans** (ROM) — REVIEW: 9, DECIDE: 20 — `docs/end_of_book/romans/ROM_END_OF_BOOK_REVIEW_2026-05-02.md`
- **1corinthians** (1CO) — REVIEW: 5, DECIDE: 2 — `docs/end_of_book/1corinthians/1CO_END_OF_BOOK_REVIEW_2026-05-01.md`
- **2corinthians** (2CO) — REVIEW: 7, DECIDE: 4 — `docs/end_of_book/2corinthians/2CO_END_OF_BOOK_REVIEW_2026-05-01.md`
- **galatians** (GAL) — REVIEW: 10, DECIDE: 7 — `docs/end_of_book/galatians/GAL_END_OF_BOOK_REVIEW_2026-04-30.md`
- **ephesians** (EPH) — REVIEW: 19, DECIDE: 13 — `docs/end_of_book/ephesians/EPH_END_OF_BOOK_REVIEW_2026-05-02.md`
- **philippians** (PHP) — REVIEW: 16, DECIDE: 13 — `docs/end_of_book/philippians/PHP_END_OF_BOOK_REVIEW_2026-05-02.md`
- **colossians** (COL) — REVIEW: 15, DECIDE: 15 — `docs/end_of_book/colossians/COL_END_OF_BOOK_REVIEW_2026-05-02.md`
- **1thessalonians** (1TH) — REVIEW: 6, DECIDE: 6 — `docs/end_of_book/1thessalonians/1TH_END_OF_BOOK_REVIEW_2026-04-30.md`
- **2thessalonians** (2TH) — REVIEW: 1, DECIDE: 1 — `docs/end_of_book/2thessalonians/2TH_END_OF_BOOK_REVIEW_2026-04-30.md`
- **1timothy** (1TI) — REVIEW: 17, DECIDE: 15 — `docs/end_of_book/1timothy/1TI_END_OF_BOOK_REVIEW_2026-05-02.md`
- **2timothy** (2TI) — REVIEW: 13, DECIDE: 8 — `docs/end_of_book/2timothy/2TI_END_OF_BOOK_REVIEW_2026-05-03.md`
- **titus** (TIT) — REVIEW: 16, DECIDE: 6 — `docs/end_of_book/titus/TIT_END_OF_BOOK_REVIEW_2026-05-03.md`
- **philemon** (PHM) — REVIEW: 5, DECIDE: 2 — `docs/end_of_book/philemon/PHM_END_OF_BOOK_REVIEW_2026-05-02.md`
- **hebrews** (HEB) — REVIEW: 11, DECIDE: 16 — `docs/end_of_book/hebrews/HEB_END_OF_BOOK_REVIEW_2026-05-04.md`
- **james** (JAS) — REVIEW: 22, DECIDE: 15 — `docs/end_of_book/james/JAS_END_OF_BOOK_REVIEW_2026-05-03.md`
- **1peter** (1PE) — REVIEW: 14, DECIDE: 14 — `docs/end_of_book/1peter/1PE_END_OF_BOOK_REVIEW_2026-05-03.md`
- **2peter** (2PE) — REVIEW: 12, DECIDE: 16 — `docs/end_of_book/2peter/2PE_END_OF_BOOK_REVIEW_2026-05-03.md`
- **1john** (1JN) — REVIEW: 13, DECIDE: 14 — `docs/end_of_book/1john/1JN_END_OF_BOOK_REVIEW_2026-05-03.md`
- **2john** (2JN) — REVIEW: 13, DECIDE: 12 — `docs/end_of_book/2john/2JN_END_OF_BOOK_REVIEW_2026-05-03.md`
- **3john** (3JN) — REVIEW: 15, DECIDE: 7 — `docs/end_of_book/3john/3JN_END_OF_BOOK_REVIEW_2026-05-03.md`
- **jude** (JUD) — REVIEW: 12, DECIDE: 13 — `docs/end_of_book/jude/JUD_END_OF_BOOK_REVIEW_2026-05-03.md`
- **revelation** (REV) — REVIEW: 10, DECIDE: 3 — `docs/end_of_book/revelation/REV_END_OF_BOOK_REVIEW_2026-05-04.md`

---

## 5. Per-chapter check warnings

Warnings or failures from per-chapter summary JSONs (if any).

None. All shipped chapters have clean summary JSONs.

---

## 6. Next: Stage 2 polish sweep

Stage 1 is mechanical consolidation. Thai-flow micro-issues (double-possessives, title-collisions, redundant directionals, lexical redundancies, passive ambiguities, awkward phonetics) are caught in Stage 2.

To run Stage 2:
```
python3 scripts/polish_review.py --book <slug>     # one book
python3 scripts/polish_review.py --all              # all 27 NT books
```

Stage 2 writes proposals to `output/polish_proposals/` only. Translation files are NOT modified until you run `apply_polish_deltas.py` with explicit approvals.
