# Inclusion variants — silent omission vs. bracketed inclusion

**Status:** **POLICY-PENDING.** This doc records the inconsistency surfaced in the Matthew end-of-book review (`docs/MAT_END_OF_BOOK_REVIEW_2026-04-19.md` §14) and presents the options. The actual policy choice is Ben's call before `book-matthew-v1` is tagged.

**Scope:** Whole-verse and large-fragment inclusion variants — readings where mainstream traditions (NA28, BSB, NIV, ESV, THSV) include text that SBLGNT/NA28 critical text omits. Distinct from word-choice variants and from short-phrase inclusion variants (which RULES.md §5 already handles via single-bracket convention `[...]`).

**Decided:** Pending. Drafted 2026-04-20 during Matthew end-of-book review action items.

---

## The inconsistency

Matthew currently treats whole-verse inclusion variants two different ways:

| Verse | Source | Mainstream | Our treatment | Reader sees |
|-------|--------|------------|---------------|-------------|
| 17:21 (καὶ νηστείᾳ — fasting saying) | SBLGNT omits | TR/Byz/KJV/NIV-margin include | **Verse absent** (no JSON entry) | Verse number 21 missing — silent jump 20 → 22 |
| 18:11 (ἦλθεν γὰρ ὁ υἱὸς τοῦ ἀνθρώπου σῶσαι τὸ ἀπολωλός) | SBLGNT omits | TR/Byz/KJV-margin include | **Verse absent** | Verse number 11 missing — silent jump 10 → 12 |
| 23:14 (woe re. widows' houses + long prayers) | SBLGNT omits | TR/Byz/KJV include; ordering varies | **Bracketed-included whole verse** | Reader sees the verse with brackets + variant note |

Plus partial cases:
| 16:2b–3 (red-sky pericope) | SBLGNT includes (with apparatus) | NA28 includes (with apparatus) | **Included unmarked** | Reader sees plainly |
| 21:44 (stone grinds saying) | SBLGNT includes | D, OL omit | **Included unmarked** | Reader sees plainly |
| 23:14 | (above) | (above) | bracketed | (above) |

## The principle from RULES.md §5

> When SBLGNT flags an inclusion variant where mainstream traditions include the words, render the words in single Thai brackets `[คำ]` in the `thai` field.

This was articulated for short-phrase inclusion variants (e.g., Mark 1:1 [พระบุตรของพระเจ้า], Mark 9:29 [และการอดอาหาร]). It was not explicitly extended to whole-verse cases. The Matthean practice has drifted three different directions for whole-verse inclusion-variant treatment.

The §5 rationale is reader-trust: "silent omission reads as editorial overreach if the reader sees TR/KJV/THSV including the words." That argument applies *more* strongly to whole-verse omissions than to short phrases — a missing verse number is more visible than a missing phrase.

## Options

### Option A — Silent-skip everywhere (consistency-by-omission)

Treat every inclusion variant uniformly: omit. Roll back 23:14 to verse-absent treatment. Apply consistently to 17:21, 18:11, future cases.

**Pros:**
- Maximum textual fidelity to SBLGNT.
- Consistent across the corpus.
- Matches NA28 critical-text presentation for these specific verses.

**Cons:**
- Reader sees verse numbers skip with no explanation.
- THSV / KJV-using readers cross-checking will think the Thai is corrupt.
- Contradicts the RULES.md §5 reader-trust rationale at the whole-verse scale.

### Option B — Bracketed-include everywhere (consistency-by-inclusion) — **RECOMMENDED**

Apply 23:14's treatment to 17:21 and 18:11. Both verses appear in the JSON and Thai output, in single brackets, with notes explaining the inclusion-variant status.

**Pros:**
- Consistent with RULES.md §5 reader-trust rationale.
- Matches the pattern already established for short-phrase variants (Mark 1:1, Mark 9:29).
- Reader sees the contested text + the editorial signal.
- Preserves SBLGNT's textual judgment by bracketing rather than endorsing.
- Sets a clean precedent for Acts 8:37, Acts 15:34, Romans 16:24, 1 John 5:7–8 (Johannine Comma) — major upcoming inclusion variants.

**Cons:**
- Adds verses our base text does not have. Could be read as "translating from TR through the back door."
- Each bracketed verse needs new translation work + back-translation + checks.
- Thai readers unfamiliar with the bracket convention may misread (mitigated by clear bracket-convention note in `docs/READER_NOTES.md` or in-app help).

### Option C — Hybrid (verse-by-verse case-by-case)

Treat each variant on its individual textual-critical merits. Brackets where the inclusion has substantial Greek manuscript support (23:14 — Byz strong); silent-skip where the inclusion is clearly secondary harmonization (17:21 — likely harmonization to Mark 9:29 [longer form]).

**Pros:**
- Theologically/text-critically defensible per verse.
- Matches scholarly editing practice.

**Cons:**
- No clean rule; every future case needs adjudication.
- Hard for downstream translators (Acts, Paulines) to follow without re-litigating each variant.
- Reader-facing inconsistency continues.

## Recommendation

**Option B**, with a corpus-wide retro pass to add 17:21 + 18:11 as bracketed-included verses before `book-matthew-v1` is tagged. This:

1. Aligns the whole-verse cases with the short-phrase-variant treatment already locked.
2. Honors the RULES.md §5 reader-trust principle at all scales.
3. Establishes the policy for the major inclusion variants in Acts + Pauline + Johannine epistles before they become live questions.

Action if Option B is adopted:
- Translate 17:21 and 18:11 into Thai (in brackets), with full key_decisions + notes documenting the inclusion-variant status, the manuscripts that include vs. omit, and Matthew's likely editorial intent.
- Update `RULES.md` §5 to extend the bracket convention explicitly to whole-verse inclusion variants.
- Re-render Matthew reader doc + rebuild Eremos bundle + update HASHES.

If Option B *not* adopted (i.e., Option A or C chosen):
- Document the chosen policy in `RULES.md` §5.
- For Option A: revert 23:14 to verse-absent, update reader doc + bundle.
- For Option C: case-by-case decisions, with text-critical reasoning recorded per verse.

## Forward variants (not exhaustive)

If Option B is adopted, these will receive bracketed-include treatment:
- **Mark 16:9–20** — already done as `⟦double-brackets⟧` (longer-ending, larger block — distinct treatment per existing precedent).
- **Acts 8:37** (Ethiopian eunuch's confession) — major TR/KJV addition.
- **Acts 15:34** (Silas remained at Antioch).
- **Acts 24:6b–8a** — minor.
- **Acts 28:29** — Jews disputing among themselves.
- **Romans 16:24** — closing benediction repetition.
- **1 John 5:7b–8a** (Johannine Comma) — most famous TR addition.
- **John 5:3b–4** (angel troubling water at Bethesda) — already a candidate.
- **John 7:53–8:11** (pericope adulterae) — special case; precedent likely follows Mark 16:9–20 with `⟦double-brackets⟧`.

## Alternatives considered

See Options A / B / C above.

## When to revisit

- After Ben's policy decision (this is policy-pending).
- If a future textual edition (e.g., ECM Acts) revises the apparatus on any of the listed verses.
- If a Thai theological reviewer flags reader-confusion about brackets.
- When the first major Acts/Pauline/Johannine inclusion variant is encountered (decision will already be in force, but verse-level review may surface refinements).

## Cross-reference

- `docs/MAT_END_OF_BOOK_REVIEW_2026-04-19.md` §14 — review that surfaced the inconsistency.
- `RULES.md` §5 — current bracket-convention policy.
- `output/translations/matthew_17.json` — currently verse-absent at 17:21.
- `output/translations/matthew_18.json` — currently verse-absent at 18:11.
- `output/translations/matthew_23.json` — currently bracketed-included at 23:14.
- Earlier short-phrase precedents: `output/translations/mark_01.json` (1:1 brackets), `output/translations/mark_09.json` (9:29 brackets).
