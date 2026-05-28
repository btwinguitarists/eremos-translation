# 1 Kings external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini only (ChatGPT paste failed during Cowork run — retry recommended)
**Audit packet:** `docs/end_of_book/1kings/external_review_packet_1KI_2026-05-24.md`
**Raw replies:** `docs/end_of_book/_external_inbox/1KI_raw.md`
**Status:** proposed-edits-pending (Item A is a MAJOR CONCERN verse-edit; Item C proposes a multi-king death-formula normalization pass)

## Convergence summary

| Item | Gemini | Action |
|------|--------|--------|
| A — 1 Kgs 19:7 mal'akh-YHWH lock drift | **MAJOR CONCERN** | **PROPOSED VERSE EDIT** — restore ทูตสวรรค์ขององค์พระผู้เป็นเจ้า |
| B — MT/LXX (3 Reigns) macro-structural divergence gap | CONCERN | Create Tier-4 book-level prefatory note in `1kings_intro.json`; current 3-tier framework inadequate |
| C — Deuteronomistic regnal-cycle formula drift | CONCERN | **PROPOSED VERSE EDITS** (multi-king) — write/lock `dtr_history_cycle_formulas_2026-05.md` before 2 Kings starts |
| D — Adonai-YHWH compound at 1 Kgs 8:53 | CONCERN | **PROPOSED VERSE EDIT** — normalize to bare องค์พระผู้เป็นเจ้า; do not add third position-category |
| E — Pagan-deity register + Ashtoreth spelling convergence | FINE | Lock OT พระ-prefix / NT เทพเจ้า split; lock อัชเทเรท as corpus spelling; cross-book normalize 1 Samuel |

## Items in detail

### Item A — 1 Kgs 19:7 mal'akh-YHWH lock drift  (MAJOR CONCERN)
- **Gemini:** Shipped text translates מַלְאַךְ יְהוָה as ทูตขององค์พระผู้เป็นเจ้า, directly violating the forward-protective lock that explicitly targeted this chapter. Dropping "สวรรค์" also creates internal inconsistency with 19:5 (ทูตสวรรค์), with no contextual justification.
- **Action:** Spot-revise 1 Kgs 19:7 to ทูตสวรรค์ขององค์พระผู้เป็นเจ้า; tick "1 Kings 19" on `malak_yhwh_2026-05.md` checklist; lock.

### Item B — MT/LXX (3 Reigns) macro-structural variant gap
- **Gemini:** CONCERN. The existing 3-tier framework was built for verse-level pluses/minuses (e.g., John 5:4), inadequate for macro-structural reordering and alternate parallel narratives in Greek 3 Reigns (Solomon reordering, 12:24a–z). Stuffing these into chapter-footer footnotes obscures scale and fails the transparency goal.
- **Action:** Create a Tier-4 category for macro-structural MT/LXX divergences; implement as a book-level prefatory note (`1kings_intro.json`) stating the MT-base decision and summarizing major structural differences in 3 Reigns. Don't over-stuff Tier-2 chapter files.

### Item C — Deuteronomistic regnal-cycle formula drift
- **Gemini:** CONCERN. Formulaic nature of Kings demands a locked standard. Drifts include: ชั่ว vs ชั่วร้าย (22:53 vs 11:6); inconsistent "high places" vocabulary (15:14 vs 22:44); inconsistent withholding of royal ทรง in death formulas of Baasha, Omri, Ahab (Jeroboam — also archetypally wicked — retains ทรง, so the withholding looks like drift, not principled delegitimization).
- **Action:** Write and lock `dtr_history_cycle_formulas_2026-05.md` **before 2 Kings starts**. Normalize 22:53 to ทำสิ่งชั่วร้าย; standardize one canonical "high places" surface; normalize death formula to uniform ทรงล่วงหลับ across all kings.

### Item D — Adonai-YHWH compound at 1 Kgs 8:53
- **Gemini:** CONCERN. ข้าแต่ at the sentence-final position of 1 Kgs 8:53 treats a sentence-final compound as an initial interjection, stretching both Thai grammar (where ข้าแต่ strictly opens deferential address) and the 2026-05-23 sub-rule. Adding edge-case rules over-fits.
- **Action:** Spot-revise 1 Kgs 8:53 to bare องค์พระผู้เป็นเจ้า per the existing appositional rule. Do not add a third position-category — rely on the mid-sentence/appositional anchor.
- **Cross-book agreement:** 2 Samuel's review (Item B there) reaches the same conclusion from the other direction — bare appositional in mid-sentence — and proposes a divine-names-table amendment to formalize the syntactic split.

### Item E — Pagan-deity register + Ashtoreth spelling convergence
- **Gemini:** FINE. 1 Kings successfully applies the theological boundary (never พระเจ้า for pagan deities) while keeping the พระ proper-noun prefix, solidifying a clear OT/NT register split. Independent convergence on อัชเทเรท across Judges + 1 Kings establishes an organic corpus precedent.
- **Action:** Lock OT พระ-prefix / NT เทพเจ้า generic-god distinction in `ot_polytheistic_register_2026-05.md`; establish อัชเทเรท as locked corpus spelling; spot-revise 1 Samuel's drifts (4 different spellings flagged in 1SA Item D).

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **1 Kgs 19:7** — restore ทูตสวรรค์ขององค์พระผู้เป็นเจ้า (MAJOR CONCERN; mal'akh-YHWH lock drift). Source: Gemini Item A.
2. **1 Kgs 22:53** — change ทำชั่ว → ทำสิ่งชั่วร้าย per locked DTr formula. Source: Gemini Item C.
3. **1 Kgs 15:14 + 22:44** (and other "high places" verses) — normalize to one canonical surface (Ben to pick). Source: Gemini Item C.
4. **Death-formula verses for Baasha, Omri, Ahab** — restore royal ทรง to ทรงล่วงหลับ to match Jeroboam pattern. Source: Gemini Item C.
5. **1 Kgs 8:53** — normalize Adonai-YHWH compound to bare องค์พระผู้เป็นเจ้า (drop sentence-final ข้าแต่). Source: Gemini Item D.
6. **1 Samuel — multiple Ashtoreth spellings** (4 variants flagged) → normalize to อัชเทเรท. Cross-book; depends on Ben locking the spelling. Source: Gemini Item E + 1SA Item D agreement.

## Proposed new / amended translator decision docs

- **New: `dtr_history_cycle_formulas_2026-05.md`** — lock evaluation-formula surface, "high places" surface, death-formula register before 2 Kings. **Highest priority — should land before next OT regnal book ships.**
- Amend `malak_yhwh_2026-05.md` — tick 1 Kings 19 on §3 checklist.
- Amend `ot_polytheistic_register_2026-05.md` — formalize OT พระ- / NT เทพเจ้า split; lock อัชเทเรท spelling.
- **New: Tier-4 macro-structural variant policy** — book-level prefatory notes (`<book>_intro.json`); 3 Reigns the immediate test case.

## Proposed audit doc amendments / other notes

- The audit doc already flagged 1 Kgs 19:7 as a forward-protective target; this is straightforward implementation of an existing lock, not a new decision.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/1KI_raw.md` (Cowork → Gemini, 2026-05-28). All content above is Gemini's findings; no fresh analysis added. **ChatGPT paste failed during the Cowork run** — recommend a retry, especially for Item B (Tier-4 proposal is a structural policy change) and Item C (multi-verse normalization). Verse-edit proposals are flagged for Ben's sign-off per the read-only-translation rule.
