# Cross-Book Audit — Proposals (checkbox-gated)

**Rolling proposal ledger for the cross-book audit loop.** Each item is a PROPOSAL behind
Ben's gate: review → check `[x]` → merge → the change is applied to `output/translations/**`
in a follow-up. The loop never edits translations directly (see
`docs/CROSSBOOK_AUDIT_CHARTER.md` §1.1). Items are appended per iteration and deduped against
the 372 live review-questions + the per-book audits before landing here.

**Legend:** `[conformance]` = fixes a violation of an already-LOCKED policy · `[DRAFT]` =
proposed rendering for an undecided fork (paired with a review-question) · each item cites its
governing decision + the *verified* shipped text (never the sweep's summary).

---

## T8 — OT polytheistic register (Baal)

- [ ] **1 Sam 7:4 — Baal `บาอัลทั้งหลาย` → `พระบาอัลทั้งหลาย`** `[conformance]`
  - **Hebrew:** הַבְּעָלִים ("the Baals") — *identical* form to 1 Sam 12:10.
  - **Shipped 7:4:** "และลูกหลานอิสราเอลก็เอา**บาอัลทั้งหลาย**และพระอัชเทเรทออก…" (bare — no `พระ`).
  - **Shipped 12:10 (internal precedent):** "…ไปนมัสการ**พระบาอัลทั้งหลาย**และพระอัชเทเรททั้งหลาย…" (`พระ` register).
  - **Governing policy:** `ot_polytheistic_register_2026-05.md` §1.3 — foreign deities take the **`พระ` / `เทพ`** register (never bare-as-supreme, never `พระเจ้า`). Bare `บาอัล` at 7:4 under-applies the register that 12:10 (same Hebrew, same book) already uses.
  - **Proposal:** normalize 7:4 → `พระบาอัลทั้งหลาย` for within-book + policy consistency. **Forward-watch:** confirm `พระบาอัล` holds across 1KI/2KI (Elijah/Baal cycle) when those units are audited (this is the cross-book "pairs 1KI/2KI" angle the sweep flagged).
  - **Second opinion:** Gemini unavailable at audit time (HTTP 503 ×2) → single-model finding, flagged for extra human scrutiny. Grounds: identical-Hebrew + internal 12:10 precedent + locked §1.3.
  - _Source: unit `1SA-T8-002`. Not covered by any live review-question — `A_1SA_D_pagan.yml` covers only Dagon 5:7 + Ashtaroth spelling._

### FYI surfaced while auditing 1SA-T8-002 (no edit proposed — reviewer housekeeping)
- **`A_1SA_D_pagan.yml` D1 (Dagon 5:7) appears already-resolved.** Shipped 5:7 now reads "เหนือ**ดาโกนพระ**ของพวกเรา" — *not* the "ดาโกนพระเจ้า" violation the question cites. Recommend marking that sub-question resolved.
- **`A_1SA_D_pagan.yml` D2 (Ashtaroth 4-way spelling drift) appears already-normalized.** Shipped 7:3 / 7:4 / 12:10 / 31:10 all use uniform "**อัชเทเรท**". Recommend marking that sub-question resolved.
