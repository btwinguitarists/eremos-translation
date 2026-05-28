# 2 Kings external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini only (ChatGPT paste failed during Cowork run — retry recommended)
**Audit packet:** `docs/end_of_book/2kings/external_review_packet_2KI_2026-05-25.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2KI_raw.md`
**Status:** proposed-edits-pending (Items A and D propose verse edits)

## Convergence summary

| Item | Gemini | Action |
|------|--------|--------|
| A — Baal-zebub พระ-register: lone foreign-deity exception | CONCERN | **PROPOSED VERSE EDIT** — normalize to พระบาอัลเซบูบ (align with พระบาอัล + พระอัดรัมเมเลค) |
| B — Adversary-speech register for human imperial blasphemer (Rabshakeh 18–19) | FINE | Lock as-is; write OT extension note in `adversary_speech_register_2026-05.md` |
| C — MT/LXX inclusion-variant gap (3rd consecutive DtrH book flagging it) | CONCERN | Adopt standing policy: Tier-2 footnotes trigger only on macro-structural divergence; don't write a Tier-2 note for chronology crux |
| D — "Until this day" leitwort: 1 Samuel lone outlier | CONCERN | Lock จนถึงทุกวันนี้ corpus-wide; **PROPOSED CROSS-BOOK EDITS** — normalize 1 Samuel's 8 occurrences |
| E — mal'akh human-messenger surface (ผู้ส่งสาร vs คณะทูต within-book variance) | FINE | Document principled variation in `malak_yhwh_2026-05.md`; do not flatten |

## Items in detail

### Item A — Baal-zebub register: lone foreign-deity exception
- **Gemini:** CONCERN. Deprecation is already achieved by using เทพเจ้า rather than พระเจ้า (1:2, 1:3). Dropping the พระ prefix from the proper noun itself creates an unprincipled outlier against พระบาอัล and even child-sacrifice gods like พระอัดรัมเมเลค (17:31), which retain the prefix.
- **Action:** Spot-revise to พระบาอัลเซบูบ (2 Kgs 1:2, 1:3, 1:6, 1:16 — wherever the bare form ships) to align with the rest of 2 Kings and `ot_polytheistic_register_2026-05.md`.

### Item B — Adversary-speech register for Rabshakeh (18–19)
- **Gemini:** FINE. Three-way register interaction executes existing corpus logic elegantly: neutral stance for the human envoy (18:19), royal register for the foreign monarch (18:28), preservation of ทรง for YHWH even within a taunt (18:35). Mirrors NT demonic-speech handling.
- **Action:** Lock the verses as-is. Write a short "OT human-imperial-blasphemer" extension note in `adversary_speech_register_2026-05.md` documenting this interaction; forward-protect Isaiah, Jeremiah, Daniel.

### Item C — MT/LXX inclusion-variant gap (recurring DECIDE)
- **Gemini:** CONCERN. Continually flagging this gap for books that lack macro-structural divergence creates audit fatigue and signals the need for a codified rule. The 2 Kings regnal-synchronism chronology crux is an arithmetic/editorial issue of the Hebrew itself, not an MT-vs-LXX inclusion-variant, so it falls outside Tier-2.
- **Action:** Adopt the standing corpus policy: Tier-2 MT/LXX footnotes trigger only for macro-structural divergence (1 Kings 3 Reigns, Jeremiah, Daniel). Accept silent MT-base adherence for routine kaige / verse-level differences. Do not write a Tier-2 textual-variant note for the chronology crux.
- **Cross-book agreement:** 1 Kings Item B independently proposes the Tier-4 macro-structural category that this CONCERN implies needs to exist.

### Item D — "Until this day" leitwort: 1 Samuel lone outlier
- **Gemini:** CONCERN. With Judges (6×), 1 Kings (5×), and now 2 Kings (10×) uniformly using จนถึงทุกวันนี้ (e.g., 17:23), the expanded form is overwhelming corpus consensus. 1 Samuel's bare จนถึงวันนี้ (8×) is an isolated outlier for this highly structured Deuteronomistic formula.
- **Action:** Lock จนถึงทุกวันนี้ in `leitwort_handling_policy_2026-05.md` as the canonical Former Prophets surface; schedule cross-book normalization pass for 1 Samuel.
- **⚠ Cross-book conflict:** 2 Samuel's review proposes the *opposite* lock (bare จนถึงวันนี้ canonical, Judges normalized). 2KI/1CH/2CH all agree with 2KI. Ben to adjudicate before normalization.

### Item E — mal'akh human-messenger within-book variance
- **Gemini:** FINE. Human-messenger מַלְאָךְ is explicitly outside the divine-angel lock, so context-sensitive surfaces are a feature: ผู้ส่งสาร fits a royal runner (1:2); คณะทูต appropriately elevates the register for a formal foreign-imperial diplomatic delegation (20:13). Flattening would damage narrative nuance.
- **Action:** Document the variation as principled in `malak_yhwh_2026-05.md`. Recommend ผู้ส่งสาร as default narrative surface; explicitly permit ทูต / คณะทูต for formal diplomatic or state-level envoys. Do not perform a flattening pass.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **2 Kgs 1:2, 1:3, 1:6, 1:16** (and any other Baal-zebub occurrences) — restore พระ prefix → พระบาอัลเซบูบ. Source: Gemini Item A.
2. **1 Samuel — 8 occurrences of עַד הַיּוֹם הַזֶּה** — cross-book normalization to whichever leitwort form Ben locks (see conflict note above). Source: Gemini Item D + 1CH/2CH agreement.

## Proposed new / amended translator decision docs

- Amend `adversary_speech_register_2026-05.md` — add OT human-imperial-blasphemer extension (Rabshakeh anchor).
- Amend `ot_polytheistic_register_2026-05.md` — confirm uniform พระ prefix for proper-noun foreign deities; Baal-zebub case-study.
- Amend `malak_yhwh_2026-05.md` — document licensed human-messenger contextual variation; ผู้ส่งสาร default, ทูต/คณะทูต for state-level envoys.
- Amend `leitwort_handling_policy_2026-05.md` — lock canonical "until this day" surface (pending Ben's choice; conflict with 2SA).
- **New corpus-policy decision:** codify the Tier-2 trigger rule (macro-structural only). This aligns with 1 Kings Item B's Tier-4 proposal.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2KI_raw.md` (Cowork → Gemini, 2026-05-28). All content above is Gemini's findings; no fresh analysis added. **ChatGPT paste failed during the Cowork run** — recommend a retry, particularly to add a second opinion on Item A (single-verse register normalization) and Item D (the leitwort conflict with 2 Samuel's review). Verse-edit proposals flagged for Ben's sign-off per the read-only-translation rule.
