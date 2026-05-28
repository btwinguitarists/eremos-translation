# 2 Chronicles external review — response + proposed actions

**Date:** 2026-05-28 (ChatGPT data added later same day)
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/2chronicles/external_review_packet_2CH_2026-05-26.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2CH_raw.md`
**Status:** proposed-edits-pending (Items B + C are pre-tag blockers per both AIs; Item A formula-drift fixes paired with Item D check-script scope widening)

> **⚠ Leitwort item is MOOT — already resolved.** Item F (`until this day` lock + 1 Samuel normalization) was proposed by both AIs but `leitwort_handling_policy_2026-05.md §7.5 v0.6` (2026-05-26) already locked `จนถึงทุกวันนี้`. Per the doc: **"2 Chronicles ships fully conformant (8× `จนถึงทุกวันนี้`, 0 bare in verse text). The 2CH audit §14's '1 Samuel is the lone outlier' was stale — superseded by v0.5, which had already normalized 1 Samuel's verse text."** Both AIs' findings simply confirm the lock — no new action.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — Evaluation formula drift (6 late kings + 29:6) | CONCERN | CONCERN | **PROPOSED VERSE EDITS** (7 verses) | Normalize to locked `ทำสิ่งชั่วร้าย`; **ChatGPT note: 29:6 needs non-royal-subject `ได้ทำสิ่งชั่วร้าย`** (different from regnal evaluations) |
| B — 2 Chr 24:20 missing ทรง (named-anchor violation) | **MAJOR** | CONCERN | **PROPOSED VERSE EDIT** | Restore ทรง → `แล้วพระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...` (ChatGPT's exact text) |
| C — 2 Chr 36:9 silent MT departure (Jehoiachin age) | **MAJOR** | **MAJOR** | **PROPOSED VERSE EDIT** | Both AIs MAJOR — restore MT "eight" + add synoptic-variant Layer-2 footer; ChatGPT: do not tag as-is |
| D — DTr-formula machine locks still Kings-scoped | CONCERN | CONCERN | WIDEN CHECK | Widen `check_phrase_consistency.py` to `2CH `; ChatGPT: Item A proves the gap isn't theoretical |
| E — Human-messenger מַלְאָךְ uniformly ผู้สื่อสาร | CONCERN | CONCERN | **PROPOSED VERSE EDITS** | 18:12 → `ผู้ส่งสาร`; 35:21 → `ทูต` / `คณะทูต`; 36:15–16 = subcategory or normalize (Ben picks) |
| ~~F — "Until this day" leitwort (5-of-6)~~ | ~~FINE~~ | ~~FINE~~ | **MOOT — already locked** | Per the doc, 2 CH already ships fully conformant; "1 Sam lone outlier" framing was stale; v0.5 normalized |

## Items in detail

### Item A — Evaluation formula drift
- **Gemini:** CONCERN. Locked formulaic surface `ทรงทำสิ่งชั่วร้ายในสายพระเนตร...` (precedent: 1 Kings) drifts to bare `ทำชั่ว` at 33:2, 33:6, 33:22, 36:5, 36:9, 36:12 + non-regnal 29:6.
- **ChatGPT:** CONCERN. Same. **Specifics added:**
  - Spot-revise 33:2, 33:6, 33:22, 36:5, 36:9, 36:12 to locked `ทรงทำสิ่งชั่วร้าย...` (preserving `มากมาย` at 33:6).
  - **29:6 needs `ได้ทำสิ่งชั่วร้าย...`** (non-royal subject — different from the regnal-evaluation pattern). Unless the lock is explicitly regnal-only.
- **Action:** Spot-revise 6 regnal-evaluation verses to `ทรงทำสิ่งชั่วร้าย`. **Spot-revise 29:6 with non-royal-subject `ได้ทำสิ่งชั่วร้าย`** (ChatGPT's specific surface).

### Item B — 2 Chr 24:20 missing ทรง (named-anchor verse) (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** **MAJOR.** This verse is **explicitly named** in `spirit_of_yhwh_empowerment` as the anchor for the לָבַשׁ-class, locked to `ทรงสวมทับ`. Dropping ทรง breaks both a named lock and corpus-wide divine-honorifics (JDG 6:34, 1 Chr 12:18).
- **ChatGPT:** CONCERN. Straightforward honorific-lock deviation. Subject is `พระวิญญาณของพระเจ้า`; locked לָבַשׁ-class surface requires `พระวิญญาณ…ทรงสวมทับ`; shipped Thai has correct verb-class `สวมทับ` but omits ทรง. **No defensible register reason** for dropping ทรง.
- **Action:** Spot-revise to ChatGPT's exact text: `แล้วพระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...`.

### Item C — 2 Chr 36:9 silent MT departure (MAJOR / MAJOR — release-blocker)
- **Gemini:** MAJOR. Project's foundational MT-base commitment is correctly upheld in 22:2 (difficult number preserved + footnote); silently adopting harmonized "18" against MT's "8" (שְׁמוֹנֶה) without a Layer-2 footer violates the core philosophy.
- **ChatGPT:** **MAJOR.** **"Do not tag as-is."** Default recommendation: restore MT 8 + synoptic-variant footer noting 2 Kgs 24:8 / many LXX read 18 (matches the 22:2 precedent). If Ben chooses to keep 18, it must receive a Trigger-1 Layer-2 MT-departure footer before tagging.
- **Action:** **Spot-revise 36:9 → restore MT reading `แปด`** + add synoptic-variant Layer-2 footer disclosing 2 Kgs 24:8 + LXX traditions read "eighteen." Aligns with 22:2 precedent.

### Item D — DTr-formula machine locks still Kings-scoped
- **Gemini:** CONCERN. 2 Chronicles is the densest regnal book; excluding it from `check_phrase_consistency.py` directly enabled Item A's drift. Must be programmatically enforced before the Prophets.
- **ChatGPT:** CONCERN. Same. **"Item A proves the gap is not theoretical: 2 Chronicles was outside the phrase-check scope, and therefore six formula drifts escaped."** The active-removal/high-place narrative concern is manageable by scoping the lock to the formulaic notice surface.
- **Action:** Widen DTr-formula locks in `check_phrase_consistency.py` to include `2CH `. Add a fourth lock: kingdom-keyed death-formula register split (if audit already verified the convention) — concurrent with Item A's revisions.

### Item E — Human-messenger מַלְאָךְ ships uniformly as `ผู้สื่อสาร`
- **Gemini:** CONCERN. Applying `ผู้สื่อสาร` to prophetic messengers in 36:15–16 is arguably defensible, but applying it to ordinary court runners (18:12) and foreign envoys (35:21) contradicts §4.4 hierarchy which steers translators to `ผู้ส่งสาร` or `ทูต`. Normalize 18:12 → ผู้ส่งสาร; 35:21 → ผู้แทน or คณะทูต. For 36:15–16, update the lock to license `ผู้สื่อสาร` specifically for prophets-as-messengers.
- **ChatGPT:** CONCERN. Same diagnosis ("not an MT-faithfulness failure, but a doc-compliance failure"). **Specifics:**
  - 18:12 → `ผู้ส่งสาร`
  - 35:21 → `ทูต` / `คณะทูต`
  - 36:15–16 → either normalize to `ผู้ส่งสาร` language **or** amend the lock to explicitly license `ผู้สื่อสาร` for prophet-as-messenger contexts.
- **Action:** Fold into the deferred cross-book human-messenger normalization pass. Spot-revise 18:12 + 35:21 per the above. For 36:15–16, **Ben picks**: normalize to `ผู้ส่งสาร` (cleaner) OR amend the lock to license `ผู้สื่อสาร` as a prophet-as-messenger subcategory.

### Item F — "Until this day" leitwort (MOOT — see top callout)
- **Gemini:** FINE. Proposes locking `จนถึงทุกวันนี้` and normalizing 1 Samuel.
- **ChatGPT:** FINE. Same direction.
- **Action:** **MOOT** — already locked in `leitwort_handling_policy_2026-05.md §7.5 v0.6`. The doc explicitly notes the 2 CH audit's "1 Samuel lone outlier" framing was stale. 2 CH ships fully conformant.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **2 Chr 33:2, 33:6, 33:22, 36:5, 36:9, 36:12** — normalize evaluation formula to locked `ทรงทำสิ่งชั่วร้าย...` (preserving `มากมาย` at 33:6) (Item A; both AIs).
2. **2 Chr 29:6** — non-royal-subject `ได้ทำสิ่งชั่วร้าย...` (ChatGPT-specific; different from regnal pattern).
3. **2 Chr 24:20** — restore ทรง → `แล้วพระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...` (Item B; Gemini MAJOR; ChatGPT's exact text).
4. **2 Chr 36:9** — restore MT reading `แปด` + add synoptic-variant Layer-2 footer (Item C; both MAJOR; release-blocker per ChatGPT).
5. **2 Chr 18:12** — `ผู้สื่อสาร` → `ผู้ส่งสาร` (Item E; both AIs).
6. **2 Chr 35:21** — `ผู้สื่อสาร` → `ทูต` or `คณะทูต` (Item E; both AIs).
7. **2 Chr 36:15–16** — Ben picks: normalize to `ผู้ส่งสาร` OR amend lock to license `ผู้สื่อสาร` for prophet-as-messenger.

## Proposed new / amended translator decision docs

- Amend `spirit_of_yhwh_empowerment` doc — confirm 2 Chr 24:20 anchor implementation; document the fix.
- Amend `malak_yhwh_2026-05.md §4.4` — license `ผู้สื่อสาร` for "prophets-as-messengers" specifically (if Ben picks that path for 36:15–16); otherwise normalize.
- Amend canon-policy / MT-departure doc — formalize requirement for synoptic-variant footers when departing MT for the harmonized synoptic reading (anchor: 22:2 + the proposed 36:9 fix).

## Proposed check-script / tooling updates

- Widen `scripts/check_phrase_consistency.py` to include `2CH ` for DTr-formula locks. Add kingdom-keyed death-formula register-split lock (4th lock; if convention verified).

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2CH_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. **Item F was MOOT** — the doc already notes the audit framing was stale; both AIs confirm the v0.4 lock. ChatGPT added the 29:6 non-royal-subject distinction (subtle but right). Both AIs MAJOR on Item C (36:9) — true release-blocker; ChatGPT explicit "do not tag as-is." Verse-edit proposals flagged for Ben's sign-off.
