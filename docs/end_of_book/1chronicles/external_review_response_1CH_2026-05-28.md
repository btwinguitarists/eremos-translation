# 1 Chronicles external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini only (ChatGPT paste failed during Cowork run — retry recommended)
**Audit packet:** `docs/end_of_book/1chronicles/external_review_packet_1CH_2026-05-26.md`
**Raw replies:** `docs/end_of_book/_external_inbox/1CH_raw.md`
**Status:** proposed-edits-pending (Item D verse + cross-book 1 Samuel normalizations)

## Convergence summary

| Item | Gemini | Action |
|------|--------|--------|
| A — mal'akh-YHWH lock outside machine scope | CONCERN | Widen `check_phrase_consistency.py` to 1–2 Chronicles; tick 1 Chr 21 on `malak_yhwh_2026-05.md` §3 |
| B — Samuel↔Chronicles synoptic numerical divergence undocumented | CONCERN | Add Layer-1 divergence notes at 1 Chr 21:5, 21:25, 11:11 |
| C — human-messenger מַלְאָךְ surface variation (ทูต vs ผู้ส่งสาร) | FINE | Document contextual variation as licensed in `malak_yhwh_2026-05.md` |
| D — 1 Chr 28:12 בָּרוּחַ: MT vs BSB gloss | CONCERN | **PROPOSED VERSE EDIT** — surface MT reading; move BSB gloss to Layer-2 |
| E — "until this day" leitwort: 1 Samuel now lone outlier | CONCERN | Lock จนถึงทุกวันนี้ corpus-wide; cross-book normalize 1 Samuel's 8 occurrences |

## Items in detail

### Item A — mal'akh-YHWH lock held but unenforced by machine
- **Gemini:** CONCERN. 1 Chr 21 correctly ships ทูตสวรรค์ขององค์พระผู้เป็นเจ้า across all seven verses (21:12, 16, etc.), but the lock isn't in the permanent machine scope, risking future drift in 2 Chronicles edits. Documenting clean adherence here gives 2 Sam 24's pending cross-book retrofit its anchor.
- **Action:** Widen `check_phrase_consistency.py` scope to include 1 Chr + 2 Chr; tick "1 Chronicles 21" on `malak_yhwh_2026-05.md` §3.

### Item B — Samuel↔Chronicles numerical divergences undocumented
- **Gemini:** CONCERN. Translations correctly reflect MT (e.g., 21:5 หนึ่งล้านหนึ่งแสน vs 2 Sam 24:9's 800,000) but meet the `synoptic_parallel_passages_2026-05.md` threshold for Layer-1 notes on substantially different numbers. Missing notes create an apologetic gap for comparison readers.
- **Action:** Add Layer-1 divergence notes at 1 Chr 21:5, 21:25, 11:11; lock the threshold for synoptic numerical divergences and carry forward into 2 Chronicles.

### Item C — human-messenger מַלְאָךְ contextual surface variation
- **Gemini:** FINE. ทูต fits royal envoys (Hiram, 14:1); ผู้ส่งสาร fits battlefield runners. Forcing one surface across all books flattens meaningful sociolinguistic nuance.
- **Action:** Document the contextual variation as principled in `malak_yhwh_2026-05.md`; do not normalize.

### Item D — 1 Chr 28:12 בָּרוּחַ: MT-anchor vs BSB-gloss
- **Gemini:** CONCERN. MT-anchor policy should override BSB gloss in the surface text; effacing בָּרוּחַ erases a theological linkage to divine revelation (parallel to Exod 25). Current ordering inverts project priorities.
- **Action:** Spot-revise 1 Chr 28:12 to surface MT reading (e.g., ตามที่ดาวิดได้รับโดยพระวิญญาณ or similar); move "in mind" / BSB gloss to Layer-2 note. Lock as the precedent for MT-breaks-tie-vs-BSB.

### Item E — "until this day" leitwort: 1 Chronicles joins majority
- **Gemini:** CONCERN. עַד הַיּוֹם הַזֶּה is a fixed etiological leitwort. With 4 of 5 books now using จนถึงทุกวันนี้, 1 Samuel's bare จนถึงวันนี้ is an unjustified outlier.
- **Action:** Lock จนถึงทุกวันนี้ as the canonical corpus surface in `leitwort_handling_policy_2026-05.md`; queue cross-book normalization of 1 Samuel's 8 occurrences.

> **Note — leitwort lock conflict:** 2 Samuel's review (Item D there) proposes the *opposite* lock — bare จนถึงวันนี้ as canonical, with Judges normalized to it. 2KI, 1CH, and 2CH reviews all agree with 1CH's direction (expanded จนถึงทุกวันนี้). Ben to adjudicate before either normalization pass runs.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **1 Chr 28:12** — surface MT בָּรוּחַ reading (e.g., ตามที่ดาวิดได้รับโดยพระวิญญาณ); demote BSB "in mind" gloss to Layer-2 note. Source: Gemini (CONCERN, Item D).
2. **1 Samuel, 8 occurrences of עַד הַיּוֹם הַזֶּה** — cross-book normalization to whichever leitwort form Ben locks (see conflict note above). Source: Gemini (CONCERN, Item E) + 2KI/2CH agreement.

## Proposed new / amended translator decision docs

- Amend `malak_yhwh_2026-05.md` — tick 1 Chr 21 on §3 checklist; document human-messenger contextual variation as licensed.
- Amend `synoptic_parallel_passages_2026-05.md` — lock the Layer-1-note threshold for synoptic numerical divergences.
- Amend `leitwort_handling_policy_2026-05.md` — lock canonical "until this day" surface (pending Ben's choice; cross-book conflict).

## Proposed check-script / tooling updates

- Widen `scripts/check_phrase_consistency.py` scope to include `1CH` and `2CH` for mal'akh-YHWH + DTr formula locks.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/1CH_raw.md` (Cowork → Gemini, 2026-05-28). All content above is Gemini's findings; no fresh analysis added. **ChatGPT paste failed during the Cowork run** — recommend a retry in a clean ChatGPT session, particularly to add a second opinion on Items B (synoptic threshold), D (verse-edit), and E (leitwort conflict). Verse-edit proposals are flagged for Ben's sign-off per the read-only-translation rule.
