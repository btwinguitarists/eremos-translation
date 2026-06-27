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
