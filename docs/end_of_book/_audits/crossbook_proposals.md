# Cross-Book Audit — Proposals (checkbox-gated)

**Rolling output of the cross-book consistency audit loop** (`docs/CROSSBOOK_AUDIT_CHARTER.md`).
Two kinds of output:
1. **Proposals** — text changes behind Ben's gate: review → check `[x]` → merge → the change
   is applied to `output/translations/**` in a follow-up. The loop never edits translations
   directly (§1.1).
2. **Stale-question findings** — live review-questions whose proposed fix the loop has
   *verified is already present in shipped text*, so they can be closed or narrowed. (The
   cross-book sweep appears to predate the OT end-of-book-review fixes, so many flags are
   already resolved — verifying shipped text, never the sweep, is catching this.)

Every item cites its governing decision + the **verified** shipped text.

---

## 1. Proposals — text changes (check `[x]` to apply)

### T8 — OT polytheistic register (Baal)

- [ ] **1 Sam 7:4 — Baal `บาอัลทั้งหลาย` → `พระบาอัลทั้งหลาย`** `[conformance]`
  - **Hebrew:** הַבְּעָלִים ("the Baals") — *identical* form to 1 Sam 12:10.
  - **Shipped 7:4:** "…ก็เอา**บาอัลทั้งหลาย**และพระอัชเทเรทออก…" (bare — no `พระ`).
  - **Shipped 12:10 (internal precedent):** "…ไปนมัสการ**พระบาอัลทั้งหลาย**และพระอัชเทเรททั้งหลาย…" (`พระ` register).
  - **Governing policy:** `ot_polytheistic_register_2026-05.md` §1.3 — foreign deities take the **`พระ` / `เทพ`** register. Bare `บาอัล` at 7:4 under-applies the register that 12:10 (same Hebrew, same book) already uses.
  - **Proposal:** normalize 7:4 → `พระบาอัลทั้งหลาย`. **Forward-watch:** confirm `พระบาอัล` holds across 1KI/2KI (Elijah/Baal cycle) when those units are audited.
  - **Second opinion:** Gemini unavailable (HTTP 503) → single-model finding, flagged for extra scrutiny.
  - _Source: `1SA-T8-002`. Not covered by any live review-question._

### T2 — human-messenger avoid-form backlog (2 Kings)

- [ ] **2 Kings — reclassify `ผู้สื่อสาร` → `ผู้ส่งสาร` at 8 ordinary-messenger verses** `[DRAFT]` (contingent on `A_2KI_E_mal` decision)
  - **Verified LIVE** (not stale): `5:10, 6:32, 6:33, 9:18, 10:8, 14:8, 19:9, 19:14` all ship the §4.4 **avoid-form** `ผู้สื่อสาร` for ordinary human messengers (Elisha's runner, the king's messenger, Jehu's rider, Sennacherib's envoys, etc.).
  - **Inconsistent within the same book:** 2 Kgs 1:2 and 19:23 already use the §4.4 default `ผู้ส่งสาร` for the same kind of messenger.
  - **Governing policy:** `malak_yhwh_2026-05.md` §4.4 — human messengers use `ผู้ส่งสาร` (default) or `ทูต`/`คณะทูต` (diplomatic); **avoid `ผู้สื่อสาร`** (reclassify unless documented reason).
  - **Proposal:** reclassify all 8 to `ผู้ส่งสาร` (matching 1:2/19:23); 14:8 (Amaziah's war-challenge) and 19:9 (Sennacherib's royal envoys) may instead take `ทูต` if Ben prefers to mark diplomatic envoys.
  - **Contingency:** this is the concrete, verse-listed form of the deferred normalization that `A_2KI_E_mal.yml` asks the decision on (normalize vs. document-as-principled). These 8 are the *avoid-form* cases — distinct from the acceptable `ผู้ส่งสาร`/`ทูต`/`คณะทูต` variation that question debates. Apply only if Ben chooses to normalize.
  - _Source: `2KI-T2-002` (its headline refs 1:2/17:4/20:13/19:23 dedup to `A_2KI_E_mal`; this backlog surfaced on verification)._

---

## 2. Stale-question findings (verified already-applied — recommend close/narrow)

These live review-questions ask for a text-fix that is **already present** in the shipped
translation (verified verse-by-verse this audit). No edit needed; listed so reviewers don't
re-litigate settled text.

- **`A_1SA_D_pagan.yml` — D1 (Dagon 5:7) + D2 (Ashtaroth spelling): RESOLVED.** Shipped 5:7 reads "เหนือ**ดาโกนพระ**ของพวกเรา" (not the "ดาโกนพระเจ้า" violation cited); 7:3/7:4/12:10/31:10 all use uniform "**อัชเทเรท**". _(from `1SA-T8-002`)_
- **`B_2CH_A_the.yml` — "did evil" normalization: text-fix RESOLVED.** All 7 cited verses (29:6, 33:2, 33:6, 33:22, 36:5, 36:9, 36:12) ship the locked `ทำสิ่งชั่วร้าย`, not bare `ทำชั่ว`. _Possibly-remaining:_ widening `check_phrase_consistency.py` scope to `"2CH "` (tooling, not text). _(from `2CH-T8-001`)_
- **`B_2CH_E_human.yml` — NARROW to prophets only.** The ordinary-envoy cases it flags are already normalized to the §4.4 forms (18:12 → `ผู้ส่งสาร`, 35:21 → `คณะทูต`). Only the **prophet-as-messenger** case (36:15–16 `ผู้สื่อสาร`) remains — and that is the genuinely-open fork the question itself raises (avoid-form vs. license `ผู้สื่อสาร` for prophetic messengers). _(from `2CH-T2-002`)_

> `B_2CH_C_chr.yml` (2 Chr 36:9 age 8-vs-18 + disclosure footer) is **genuinely open** — a real
> unresolved textual fork, correctly left for reviewers (`2CH-T4-001` deduped against it).
