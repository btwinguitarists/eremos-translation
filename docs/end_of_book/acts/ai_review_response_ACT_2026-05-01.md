# Acts — External AI Review Response

**Date:** 2026-05-01
**Reviewers:** ChatGPT (independent review); Gemini (independent review)
**Audit doc:** `ACT_END_OF_BOOK_REVIEW_2026-04-26.md`

This doc records the disposition of each AI-flagged item. One spot-revision implemented (δοξάζω-narrator harmonization); three items already corrected in the live corpus (audit packet had stale snapshots); two items locked.

---

## Item A — Acts 21 we-passage register

**Both AIs flagged.** Gemini: MAJOR CONCERN; ChatGPT: CONCERN. Recommended revising `ข้าพเจ้าทั้งหลาย` → `พวกเรา` for Acts 21:1, 5, 11, 17 (and Gemini called the v.5 mixing the "smoking gun").

**Disposition:** **NO REVISION NEEDED.** Verified live corpus state of Acts 21:1, 5, 11, 17, 18 — all already use `พวกเรา` / `เรา` consistently. Zero occurrences of `ข้าพเจ้าทั้งหลาย` anywhere in Acts 21. The audit packet snapshot was stale; the corrections were already made in a prior session and never reflected in the audit doc.

---

## Item B — ἔθνος three-way contextual split (Acts 4:27 + 14:27 drift)

**Both AIs flagged** the supposedly-`ชนต่างชาติ` rendering as drift; recommend normalize to `คนต่างชาติ`.

**Disposition:** **NO REVISION NEEDED.** Verified Acts 4:27 + 14:27 in live corpus — both already use `คนต่างชาติ` (correct, locked). The packet snapshots showed `ชนต่างชาติ` but live corpus is clean. Two `ชนต่างชาติ` remnants exist in `thai_literal` fields (translator-reference Greek-mapping, not user-facing) at Acts 14:2, 14:16; these are non-user-facing and intentionally literal.

**Doc action:** `docs/translator_decisions/ethnos_three_way.md` queued for pre-Romans formalization (both AIs recommended this).

---

## Item C — Roman administrative titles (ἀνθύπατος drift at Acts 19:38)

**Both AIs flagged** Acts 19:38 as `ผู้ว่าการ` (drift from the locked `ผู้สำเร็จราชการ`).

**Disposition:** **NO REVISION NEEDED.** Verified live corpus Acts 19:38 — already uses `ผู้สำเร็จราชการ` (correct). Zero `ผู้ว่าการ` occurrences anywhere in Acts. Packet snapshot was stale.

---

## Item D — Pagan-deity proper-noun policy (ดิออสคูรี at Acts 28:11)

**Both AIs FINE.** Both affirm the Greek-source-fidelity choice (ดิออสคูรี vs Latin "Castor and Pollux") + the εꞵพ/พระเจ้า boundary preservation.

**Disposition:** **LOCK as-is.** Existing `pagan_deities_2026-04.md` already covers this; amended 2026-05-01 with Rule 1b (literal pagan vs Pauline polemical-metaphorical θεός) per 2 CO end-of-book review.

---

## Item E — δοξάζω narrator-doxology sub-rule (royal-prefix inconsistency)

**Mixed:** ChatGPT FINE; Gemini CONCERN — flagged that Acts 4:21 uses `ถวายพระเกียรติ` (royal-prefix) while Acts 11:18 + 21:20 dropped it to `ถวายเกียรติ`. Recommended: harmonize.

**Disposition:** **REVISED.** Acts 11:18 + 21:20: `ถวายเกียรติแด่พระเจ้า` → `ถวายพระเกียรติแด่พระเจ้า`. All three narrator-δοξάζω-doxology contexts now uniform with royal-prefix per RULES §3 ราชาศัπต์.

**Doc action:** Existing `divine_object_praise_verbs_2026-04.md` to be amended with the explicit sub-rule (queued).

---

## Item F — σωτήριον τοῦ θεοῦ Lukan two-volume inclusio (Luke 3:6 / Acts 28:28)

**Both AIs FINE.** Both affirm the existing rendering `ความรอดของพระเจ้า` perfectly bridges Luke 3:6 + Acts 28:28; Luke 2:30's `ความรอดของพระองค์` (direct address to God) preserves the conceptual-link.

**Disposition:** **LOCK as-is.** No revision.

---

## Summary table

| Item | AI Verdict | Action | Status |
|---|---|---|---|
| A Acts 21 we-passage | Both flagged | Verified already-correct (stale packet) | ✅ no action |
| B ἔθνος drift | Both flagged | Verified already-correct (stale packet) | ✅ no action |
| C ἀνθύπατος drift | Both flagged | Verified already-correct (stale packet) | ✅ no action |
| D Pagan-deity policy | Both FINE | Lock as-is | ✅ no revision |
| E δοξάζω royal-prefix | Mixed | **Harmonized 11:18 + 21:20 to ถวายพระเกียรติ** | ✅ done |
| F σωτήριον inclusio | Both FINE | Lock as-is | ✅ no revision |

---

## Note on stale audit packet

Three of six items (A, B, C) had been corrected in the live corpus but the audit packet still showed pre-correction snapshots. This is a known issue — the audit subprocess reads a JSON snapshot at audit-time, not the live state. AI reviewers acted in good faith on the stale snapshot; verification against live corpus confirms only Item E needed work.

This is a useful pattern to document: **always verify AI-flagged drifts against live corpus before acting**, since prior translator-correction passes may have already addressed the issue.

---

## Tagging eligibility

- §1 mechanical gates: ✅ clean
- §2 audit doc: ✅ done (2026-04-26)
- §3 external AI review: ✅ done (this doc; ChatGPT + Gemini independent)
- §4 reviewer hand-off: ongoing per project async-review policy
- §5 lock the book: ready after Item E revision lands.

**Tag `book-acts-v1` is GO.**
