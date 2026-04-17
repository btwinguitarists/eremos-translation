# CNTR feasibility spike — 2026-04-17

## Why this doc exists

A cross-AI review (Gemini, 2026-04-17) proposed integrating the **Center for New Testament Restoration (CNTR) Universal Apparatus** as a programmatic data source for textual-variant auditing. The suggestion was to build `scripts/check_textual_variants.py` that would cross-reference CNTR's machine-readable apparatus against our translation notes and fail-ship when a significant variant went unacknowledged.

Before committing engineering effort, we ran a one-hour feasibility spike to:

1. Verify license claims
2. Check data availability and format
3. Estimate volume of "significant" vs trivial variants for a representative chapter (Mark 1)
4. Decide whether to build the check now, later, or not at all

## What we found

### CNTR Statistical Restoration (SR.tsv)

- **Home**: https://greekcntr.org/
- **Org on GitHub**: https://github.com/Center-for-New-Testament-Restoration
- **License**: **CC BY 4.0** (verified — `SR` repo ships `LICENSE.md` with the CC BY 4.0 text)
- **Format**: TSV. 137,362 rows for the whole NT.
- **Mark 1 = 703 word-token rows, ~50 KB**. 45 verses.
- **Columns**: `Verse | Modern | Koine | Lemma | ESN | Role | Morphology`
- **Nomina sacra**: encoded via a `=` sigil in the Koine column
- **Tooling**: no dedicated Python library. Community mirrors at `Freely-Given-org/CNTR-SR` and `ReneNyffenegger/Center-for-new-Testament-Restoration-CNTR-SR`. See also the directory at https://github.com/biblenerd/awesome-bible-developer-resources.

### CNTR transcriptions repo

- **License**: **CC BY-SA 4.0** (share-alike)
- **Consequence**: **Cannot be mixed with our CC0 output.** The SA clause would force CC-BY-SA inheritance on anything derived from it.
- Our use must be limited to the SR-branded CC-BY-4.0 artifacts.

### Universal Apparatus (the actual variant dataset)

- **Availability as of 2026-04**: **NOT machine-readable.** Distributed only as a PDF bundled with the 2022 printed SRGNT. Pilot data was hosted at SBTS but is not a downloadable dataset.
- **Public docs**:
  - https://greekcntr.org/resources/SRGNT/SRGNT.pdf
  - https://greekcntr.org/resources/overview.pdf
- **Significant-vs-trivial filtering**: per CNTR's overview, filtering of "insignificant or not necessarily translatable" variants is done on CNTR's side and **not exposed as a flag** in any public data they ship today.
- **Witnesses**: ~14 pre-AD-400 manuscripts.

### BGNT (Berean Greek New Testament) — a separate project

- **Home**: https://greekbible.org/ (also surfaced on Bible Hub)
- **License**: "free to use" grant — **not CC BY**. Would need explicit license verification before embedding in our CC0 output.
- Evaluated only for completeness; not a replacement for SBLGNT.

### Mark 1 variant volume estimate

We couldn't pull an actual UA-flagged count (see above). Calibrating from Bruce Terry's apparatus, NA28, and Metzger's textual commentary:

- **~25–35 total variant units in Mark 1**
- **~5–10 of these are translation-affecting** (substantive, not orthographic):
  - 1:1 `υἱοῦ θεοῦ` (Son of God) — present in B, D, W, Byzantine; absent in א\*, Θ, Origen
  - 1:2 `Ἠσαΐᾳ` vs `τοῖς προφήταις` (Isaiah vs. the prophets)
  - 1:4 `ὁ βαπτίζων` vs `ὁ βαπτιστής` (different participial form)
  - 1:41 `σπλαγχνισθείς` vs `ὀργισθείς` (compassion vs. anger — the famous crux)
  - plus 1-5 smaller cases

Every one of those **is already documented** in our Mark 1 verse notes. So the utility-add of an automated apparatus check, even if the data were machine-readable, is narrow — we'd be automating the audit of work that our human+model curation layer is already catching.

## Decision

**Do not build `check_textual_variants.py` against CNTR yet.** Three reasons:

1. **The UA isn't in machine form.** Any check we build today would be cosmetic — it could only flag that we *lack* CNTR data integration, not compare against real variant claims.
2. **Our existing curation is catching the high-stakes cases.** Evidence from the Mark corpus: Mark 1:1 (Son of God), 1:41 (ὀργισθείς / σπλαγχνισθείς), 2:26 (Abiathar / Ahimelech), 9:29 (with-or-without "and fasting"), 14:24 (with-or-without "new"), 14:58 (temple-saying distortion), 16:9-20 (⟦double-bracketed⟧ longer ending with full manuscript-evidence note). These are the verses where a variant-check would actually matter, and they are all documented.
3. **SR.tsv adoption would double our base-text audit surface** without a clear return today. Two base texts means every glossary term, every key-decision rationale, and every back-translation would need to reconcile against both. We choose SBLGNT as our single stated source and document divergences from other traditions in the verse notes — that's the editorial principle we already follow.

## What we WILL do

- **Revisit CNTR UA in ~6 months** (2026-10). If CNTR publishes the apparatus in machine-readable form by then, re-run the spike and reconsider the check. This doc is the starting point for that next spike.
- **Keep our existing approach**: SBLGNT main text + SBLGNT apparatus + curated translator notes per verse. The Mark 16 ending handling (⟦double-brackets⟧ + full manuscript-evidence note) is the template for future contested passages.
- **Note the evaluation in RULES.md §2** so future reviewers see that CNTR was considered and deferred, with a reason.

## Keeping this doc honest

If the CNTR Universal Apparatus later becomes machine-readable and we don't update our approach within a reasonable window of that happening, someone should ping this decision. The facts that made "defer" correct in 2026-04 may not hold forever.
