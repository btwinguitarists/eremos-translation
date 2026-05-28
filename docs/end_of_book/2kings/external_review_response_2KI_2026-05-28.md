# 2 Kings external review — response + proposed actions

**Date:** 2026-05-28 (ChatGPT data added later same day)
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/2kings/external_review_packet_2KI_2026-05-25.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2KI_raw.md`
**Status:** proposed-edits-pending (Item A Baal-zebub normalization + Item E adds 2 Kgs 19:23)

> **⚠ Leitwort item is MOOT — already resolved.** Item D (`until this day` lock + 1 Samuel normalization) was proposed by both AIs but this is the very book that **triggered the v0.4 reversal** in `leitwort_handling_policy_2026-05.md §7.5` on **2026-05-25** — the doc literally says "Triggered by: 2 Kings audit Item D + external review." Both AIs converged on `จนถึงทุกวันนี้` (which Ben already locked); 1 Samuel's verse-text was already normalized in v0.5. **No new action required** for Item D — the AIs' findings *confirm* the lock that was already chosen.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — Baal-zebub พระ-register: lone outlier | CONCERN | CONCERN | **PROPOSED VERSE EDITS** | Normalize 1:2, 1:3, 1:6, 1:16 to `พระบาอัลเซบูบ เทพเจ้าแห่งเอโครน` (ChatGPT supplies the full surface) |
| B — Rabshakeh human-imperial-blasphemer register | FINE | FINE | LOCK | Add OT-blasphemer extension to `adversary_speech_register_2026-05.md`; ChatGPT confirms the layered register |
| C — MT/LXX inclusion-variant gap (3rd DtrH book flagging) | CONCERN | CONCERN | CODIFY POLICY | Adopt standing rule: Tier-2 footers trigger only on macro-structural divergence; **don't** write a 2 Kings textual-variant note; chronology is study-Bible issue |
| ~~D — "Until this day" leitwort~~ | ~~CONCERN~~ | ~~CONCERN~~ | **MOOT — already locked** | This book *triggered* the v0.4 reversal — both AIs confirm the lock Ben already chose |
| E — mal'akh human-messenger surfaces | FINE | CONCERN | **PROPOSED VERSE EDIT** | **ChatGPT adds 2 Kgs 19:23** `ผู้สื่อสาร` → `ทูตของเจ้า` (Sennacherib's official imperial envoys); also full decision tree |

## Items in detail

### Item A — Baal-zebub register
- **Gemini:** CONCERN. Deprecation already achieved by เทพเจ้า rather than พระเจ้า (1:2, 1:3). Dropping the พระ prefix from the proper noun creates an unprincipled outlier against พระบาอัล + พระอัดรัมเมเลค (17:31).
- **ChatGPT:** CONCERN. Same. **Specific full surface:** `พระบาอัลเซบูบ เทพเจ้าแห่งเอโครน` — applies to **1:2, 1:3, 1:6, 1:16**. Do **not** create a deprecation carve-out.
- **Action:** Spot-revise all 4 verses (2 Kgs 1:2, 1:3, 1:6, 1:16) to ChatGPT's full surface `พระบาอัลเซบูบ เทพเจ้าแห่งเอโครน`.

### Item B — Adversary-speech register for Rabshakeh (18–19)
- **Gemini:** FINE. Three-way register interaction elegantly executes existing corpus logic: neutral for human envoy (18:19); royal for foreign monarch (18:28); preservation of ทรง for YHWH even within a taunt (18:35).
- **ChatGPT:** FINE. Same. **The speaker's mockery does not control the divine referent's honorific status; 18:35 should retain `องค์พระผู้เป็นเจ้าจะทรงช่วยกู้`.** Mirrors NT adversary-speech handling.
- **Action:** Lock verses as-is. Write a short "OT human-imperial-blasphemer" extension note in `adversary_speech_register_2026-05.md` or `ot_register_policy_2026-05.md` — forward-protect Isaiah/Jeremiah/Daniel.

### Item C — MT/LXX inclusion-variant gap (recurring DECIDE)
- **Gemini:** CONCERN. Continually flagging this for books without macro-structural divergence creates audit fatigue. The 2 Kings regnal-synchronism chronology crux is arithmetic/editorial within the Hebrew, not MT-vs-LXX inclusion — falls outside Tier-2.
- **ChatGPT:** CONCERN. Same. Not a 2 Kings text concern; **policy-gap concern**. 2 Kings does not need reader-facing MT/LXX footers (kaige / routine verse-level divergence, not macro-structural). Repeated audit flag shows the trigger threshold is underdefined.
- **Action:** Update `mt_vs_lxx_textual_variant_handling_2026-05.md` with the standing rule: **Tier-2 MT/LXX disclosure triggers only for macro-structural or canonically visible divergences** (1 Kings miscellanies/reordering, Jeremiah shorter LXX/reordered OAN, Daniel additions) — not ordinary kaige-character or scattered verse-level variants. **Do not add a 2 Kings textual-variant note.** Treat regnal synchronism chronology as a study-Bible/explanatory issue. Both AIs explicit on this.

### Item D — "Until this day" leitwort (MOOT — see top callout)
- **Gemini:** CONCERN. Proposes locking `จนถึงทุกวันนี้`.
- **ChatGPT:** CONCERN. Same direction.
- **Action:** **MOOT** — this audit's Item D is **literally the trigger that produced the v0.4 reversal in `leitwort_handling_policy_2026-05.md §7.5` (2026-05-25)**. Both AIs are confirming a decision already locked. 1 Samuel verse-text was normalized in v0.5. The deferred backlog (2 Sam 4× + scattered) is knowingly tracked in the doc, not a tag-blocker.

### Item E — mal'akh human-messenger surface
- **Gemini:** FINE. Human-messenger מַלְאָךְ is explicitly outside the divine-angel lock; context-sensitive surfaces are a feature. ผู้ส่งสาร for royal runner (1:2); คณะทูต for formal diplomatic delegation (20:13). Don't flatten.
- **ChatGPT:** **CONCERN.** Don't force a single surface, but **the real concern is undocumented free drift** among ผู้ส่งสาร / ผู้ส่งข่าว / ผู้สื่อสาร where the context is simply a message-carrier. **Specific verse edit:** `2 Kgs 19:23 ผู้สื่อสาร → ทูตของเจ้า` — the referent is Sennacherib's official emissaries carrying the imperial taunt (diplomatic envoy, not generic).
- **ChatGPT decision tree (worth folding into the doc):**
  - **Divine/supernatural messenger:** `ทูตสวรรค์`
  - **Generic human message-carrier:** `ผู้ส่งสาร`
  - **Diplomatic envoy:** `ทูต`
  - **Formal delegation:** `คณะทูต`
- **Action:** Keep 2 Kgs 17:4 ทูต and 20:13 คณะทูต. **Spot-revise 2 Kgs 19:23 `ผู้สื่อสาร` → `ทูตของเจ้า`.** Update `malak_yhwh_2026-05.md §4.4` with ChatGPT's decision tree; normalize generic cross-book variants to `ผู้ส่งสาร`.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **2 Kgs 1:2, 1:3, 1:6, 1:16** — Baal-zebub normalize to `พระบาอัลเซบูบ เทพเจ้าแห่งเอโครน` (Item A; both AIs).
2. **2 Kgs 19:23** — `ผู้สื่อสาร` → `ทูตของเจ้า` (Item E; ChatGPT; Sennacherib's imperial envoys are diplomatic, not generic message-carriers). **New from ChatGPT pass.**

## Proposed new / amended translator decision docs

- Amend `adversary_speech_register_2026-05.md` (or `ot_register_policy_2026-05.md`) — OT human-imperial-blasphemer extension; same content/register split as NT adversaries (neutral speech for adversary; royal for kings; divine honorifics preserved when divine referent appears in hostile speech).
- Amend `mt_vs_lxx_textual_variant_handling_2026-05.md` — standing rule: Tier-2 disclosure triggers only on macro-structural/canonically visible divergence. **Do not** add a 2 Kings textual-variant note (both AIs explicit).
- Amend `malak_yhwh_2026-05.md §4.4` — full decision tree (4 categories) per ChatGPT; normalize generic cross-book variants to `ผู้ส่งสาร` (while preserving licensed contextual surfaces like ทูต and คณะทูต).
- Amend `ot_polytheistic_register_2026-05.md` — Baal-zebud full-surface anchor (per Item A).

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2KI_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. **Item D was MOOT** — this is the audit that *triggered* the v0.4 reversal; both AIs confirm the lock Ben already chose. ChatGPT added a real new verse edit at 19:23 + a fuller decision tree at Item E. Verse-edit proposals flagged for Ben's sign-off.
