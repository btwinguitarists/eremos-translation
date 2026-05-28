# 2 Samuel external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini only (ChatGPT paste failed during Cowork run — retry recommended)
**Audit packet:** `docs/end_of_book/2samuel/external_review_packet_2SA_2026-05-23.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2SA_raw.md`
**Status:** proposed-edits-pending (Item A flags 15:7 / 21:19 / 24:1 Tier-2 disclosure gaps + a possible textual-base revert; Item D contradicts 2KI/1CH/2CH on leitwort)

## Convergence summary

| Item | Gemini | Action |
|------|--------|--------|
| A — Tier-2 reader-footer gap (15:7, 21:19, 24:1) | CONCERN | **PROPOSED:** add Tier-2 chapter-footer entries for at least 15:7, 21:19, 24:1; Ben to decide 15:7 emendation vs MT revert |
| B — Adonai-YHWH compound prayer-vocative (mid-sentence apposition) | FINE | Lock as-is; amend `divine_names_table_2026-05.md` to document syntactic split (ข้าแต่ initial / bare appositional) |
| C — Synoptic/parallel-passage corpus policy | CONCERN | Write `synoptic_parallel_passages_2026-05.md` before Kings/Chronicles + Psalter synoptics compound |
| D — "Until this day" leitwort: lock the *bare* form | CONCERN | ⚠ **CONFLICTS with 2KI/1CH/2CH** — those propose locking the *expanded* form |

## Items in detail

### Item A — Textual-variant Tier-2 reader-footer gap
- **Gemini:** CONCERN. Canon policy mandates Tier-2 reader-facing footnotes for Trigger-1 departures from MT, so the absence at 2 Sam 15:7 is a direct compliance failure. "Forty years" in 15:7 is technically grammatical but historically nonsensical (contradicts Absalom's lifespan), which justifies emendation — but demands consistent Layer-2 disclosure alongside the other major theological cruxes at 21:19 and 24:1.
- **Action:** Add Tier-2 chapter-footer entries for **at least** 15:7, 21:19, 24:1. Ben to decide whether to retain the 15:7 emendation ("four") or revert to MT ("forty"). Update canon policy doc to state explicitly that "historically self-contradicting within the narrative" qualifies for Trigger-1 emendation.

### Item B — Adonai-YHWH compound prayer-vocative
- **Gemini:** FINE. Thai syntax dictates ข้าแต่ as a sentence-initial / clause-initial interjection. Forcing it into mid-sentence appositional phrases (2 Sam 7:22, เพราะเหตุนี้พระองค์ยิ่งใหญ่ องค์พระผู้เป็นเจ้า) would be linguistically unnatural. Shipped text correctly adapts register to Thai grammatical reality while preserving the locked vocabulary.
- **Action:** Lock as-is. Amend `divine_names_table_2026-05.md` to formally document the syntactic split:
  - **Initial-position interjections:** `ข้าแต่องค์พระผู้เป็นเจ้า` (anchor: Josh 7:7)
  - **Mid-sentence appositional:** bare `องค์พระผู้เป็นเจ้า` (anchor: 2 Sam 7)
- **Cross-book agreement:** 1 Kings Item D independently reaches the same conclusion from the 8:53 sentence-final case.

### Item C — Synoptic / parallel-passage corpus doc
- **Gemini:** CONCERN. The ad-hoc handling of 2 Sam 22 // Ps 18 and the Samuel ↔ Chronicles overlaps is excellent in execution, but leaving the methodology undocumented guarantees drift when the project hits the massive Kings/Chronicles and Psalter synoptics. A locked policy is required *now*.
- **Action:** Write `synoptic_parallel_passages_2026-05.md` to formally lock the 2 Samuel approach: independent translation from the local MT, Layer-1 documentation for all variants, standardized reader-footer phrasing for major Tier-2 disclosures. Carries directly into 1CH/2CH (1CH Item B already proposes Layer-1 notes that would lean on this policy).

### Item D — "Until this day" leitwort: lock the *bare* form
- **Gemini:** CONCERN. עַד הַיּוֹם הַזֶּה functions as a Deuteronomistic structural pillar requiring strict cross-book uniformity. Judges variant (จนถึงทุกวันนี้) adds a slight intensifier; 1SA/2SA bare form (จนถึงวันนี้) is accurate, natural, and already the vast statistical majority of the footprint.
- **Action (Gemini's recommendation):** Lock the *bare* form `จนถึงวันนี้` in `leitwort_handling_policy_2026-05.md`; batch-script a spot-revision to normalize the 6 occurrences in Judges.
- **⚠ Direct conflict with 2KI / 1CH / 2CH:** Those three reviews (also Gemini's, on separate books) propose locking the *expanded* form `จนถึงทุกวันนี้` and normalizing 1 Samuel. So Gemini's count-based argument flips depending on which book it's reviewing. **Ben to adjudicate the canonical form before either normalization pass runs.** Decision factors: stylistic register (intensified vs plain), majority by occurrence count, theological/narrative weight in DtrH structure.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **2 Sam 15:7** — Ben to decide: retain emendation ("four") with new Tier-2 disclosure, or revert to MT ("forty") with disclosure. Source: Gemini Item A.
2. **"Until this day" cross-book normalization** — direction depends on Ben's adjudication of the lock direction. Will affect either 1 Samuel (8 occurrences) or Judges (6 occurrences). Source: Gemini Item D + cross-book conflict.

## Proposed new / amended translator decision docs

- **New: `synoptic_parallel_passages_2026-05.md`** — lock methodology before Kings/Chronicles + Psalter synoptics compound. **High priority.**
- Amend `divine_names_table_2026-05.md` — formal syntactic split for ข้าแต่ initial vs bare appositional (anchors: Josh 7:7 and 2 Sam 7).
- Amend `leitwort_handling_policy_2026-05.md` — lock canonical "until this day" surface (pending Ben's choice; conflict).
- Amend canon-policy doc (Tier-2 trigger rules) — add "historically self-contradicting within the narrative" as a Trigger-1 qualifier.

## Proposed audit / data updates

- Add Tier-2 chapter-footer entries for 2 Sam 15, 21, 24 (3 chapters).

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2SA_raw.md` (Cowork → Gemini, 2026-05-28). All content above is Gemini's findings; no fresh analysis added. **ChatGPT paste failed during the Cowork run** — recommend a retry, particularly to break the **leitwort lock conflict** (a second model's opinion on Item D would help adjudicate). Verse-edit proposals flagged for Ben's sign-off.
