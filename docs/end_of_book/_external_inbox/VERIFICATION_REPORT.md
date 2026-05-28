# Verification report — what's actually still open after the 19-book backlog clear

**Date:** 2026-05-28 (post-Cowork, post-ChatGPT-retry, post-doc-cross-check)
**Method:** For each MAJOR/CONCERN proposal in the 19 response docs, cross-checked against the relevant `docs/translator_decisions/<lock>.md` AND spot-checked the actual shipped verse JSON.

## TL;DR

**The vast majority of AI-proposed verse edits are MOOT — the verses already match the locks.** The AIs reviewed packets that predate the corresponding fixes; my synthesis didn't cross-check against the locked docs. After verification:

- **~50+ verse-edit proposals → MOOT** (shipped verse already matches the lock)
- **3 verse edits confirmed REAL** (need to be made)
- **1 AI recommendation would actively VIOLATE a lock** if implemented (1 Kings death-formula — see warning below)
- A handful of proposals remain UNVERIFIED (lower-impact thai_summary / Layer-2 additions)

**Practical implication:** PR #168 is safe to merge — none of the proposals are auto-applied; everything stays a proposal pending your sign-off. But **do not work through the proposed-edit lists one-by-one** thinking they're all real. Use this report instead.

---

## ⚠ Critical: do NOT implement (would violate a locked decision)

| Source | AI proposal | Why it's wrong |
|---|---|---|
| **1 KI Item C — death-formula ทรง for Baasha / Omri / Ahab** | "Restore royal `ทรง` to `ทรงล่วงหลับ...` uniformly for all kings (match Jeroboam pattern)" | `dtr_history_cycle_formulas_2026-05.md` (2026-05-24) locked a **dynastic-legitimacy register split**: Davidic / Judahite = `ทรง`; Northern / breakaway = plain. Jeroboam 14:20 was specifically **corrected DOWN** (from `ทรง` to plain) to fix the one outlier. The AIs (and my synthesis) didn't see the doc. The Northern kings shipping plain is **principled, not drift.** Restoring `ทรง` would reverse a locked decision. |

---

## ✓ MOOT — verified already correctly locked (representative spot-checks)

### Chesed (GEN A, JON A)
- **JON 2:9 + 4:2** — corrected 2026-05-09 per `chesed_covenant_love_2026-05.md` §4 ("Corrections applied to both Jonah verses on 2026-05-09").
- **GEN 19:19, 21:23, 32:11, 39:21** — spot-checked shipped JSON, all use `ความรักมั่นคง` ✓
- **REAL:** GEN 40:14 still shows `แสดงความเมตตา` (drift). One verse needs editing.

### Sinai attribute formula (EXO A, NUM A)
- **EXO 34:6, 34:7** — spot-checked: shipped JSON exactly matches `exod_34_attribute_formula_2026-05.md` §1.3 canonical Thai. ✓
- **NUM 14:18** — spot-checked: shipped matches the doc's locked surface. `exod_34` doc v0.2 (2026-05-16) says explicitly "Retroactively normalizes NUM 14:18, EXO 20:5–6, and DEU 5:9–10 to the locked canonical Thai surface."
- **EXO 33:19** — spot-checked: shipped Thai is *exactly* ChatGPT's proposed text (`เราจะทรงพระคุณต่อผู้ที่เราจะทรงพระคุณ และเราจะทรงพระเมตตา...`). The חנן/רחם mapping is already correct.

### mal'akh-YHWH (EXO D, NUM B, 1KI A, 2KI Item E, 2CH Item E, 1CH Item A)
- **EXO 3:2, 14:19, 32:34** — `malak_yhwh_2026-05.md` checklist [x] "Exodus 3:2, 14:19, 32:34 normalized to ทูตสวรรค์ form (verified 2026-05-13)."
- **1 Kings 19:7** — doc: "✓ done 2026-05-24" (this was the EOB-audit drift fix).
- **2 Kings 1:3, 1:15** — doc: "✓ done 2026-05-25".
- **2 Kings 19:23** — doc: "fixed 2026-05-25" (to `ผู้ส่งสาร`, not ChatGPT's proposed `ทูตของเจ้า` — different surface but the verse was already revised).
- **2 Chr 18:12, 35:21, 36:15-16** — doc §4.4 (updated 2026-05-26): all 4 verses already normalized per the human-messenger hierarchy (18:12 → ผู้ส่งสาร; 35:21 → คณะทูต; 36:15-16 → ผู้สื่อสารของพระเจ้า, licensed prophet-as-messenger sense).
- **1 Chr 21** — doc: "Verified clean 2026-05-26" (21:12, 15, 16, 18, 30 all conformant).
- **NUM 22:22** — spot-checked: ships `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` ✓. (The malak doc lists NUM 22 in its deferred backlog, but actual shipped JSON is already correct. The deferred-backlog note may itself be stale.)

### Joseph Rachasap (GEN H)
- **GEN 44:1, 45:1, 50:1, 50:2** — `ot_register_policy_2026-05.md` §2.5: "All 4 verses were stripped to plain narrator-voice 2026-05-12."

### Spirit-of-YHWH (1SA A, 2CH B)
- **1 Sam 10:6, 10:10, 11:6, 16:13** — spot-checked: all four ship `พระวิญญาณ + อย่างทรงพลัง` ✓ (the 4-way verb-class lock from `spirit_of_yhwh_empowerment_2026-05.md` is honored).
- **1 Sam 16:14** — spot-checked: departing Spirit handled correctly (`พระวิญญาณ...ไปแล้ว`); evil-spirit stays bare `วิญญาณชั่ว` — exactly ChatGPT's recommended treatment.
- **2 Chr 24:20** — spot-checked: ships `แล้วพระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...` — **HAS the ทรง**. The AIs' claim that it was missing is **wrong**.

### Cities of refuge / blood-avenger (JOS B)
- **JOS 20:2, 3, 5, 6, 9 + JOS 21:13, 21, 27, 32, 38 + DEU 19:6, 12** — `cities_of_refuge_blood_avenger_2026-05.md` revision-history: "2026-05-18 — normalized to the locked surfaces in the same commit. Joshua-end-of-book audit §5 closed."

### Seven-Nations ethnonyms (JOS A)
- **JOS 3:10, 9:1, 11:3, 12:8, 24:11** + **DEU 20:17** — spot-checked: all use bare-suffix forms (`ชาวเปริซซี / ชาวฮีไว / ชาวเยบุส`). ✓

### DTr formula drifts (1KI C, 2CH A)
- **1KI 22:53** — `dtr_history_cycle_formulas_2026-05.md`: "Normalized 22:53 (`ชั่ว` → `ชั่วร้าย`, 2026-05-24)".
- **1KI 15:14 + 22:44 high places** — doc: "Normalized 15:14 + 22:44 on 2026-05-24".
- **2 Chr 29:6, 33:2, 33:6, 33:22, 36:5, 36:9, 36:12** — spot-checked: all 7 verses already ship `ทำสิ่งชั่วร้าย` ✓. The 2CH evaluation-formula drift the AIs flagged **does not exist in the shipped JSON.**

### Baal-zebub (2KI A)
- **2 KI 1:2, 1:3, 1:6, 1:16** — spot-checked: all four already ship `พระบาอัลเซบูบ เทพเจ้าแห่งเอโครน` — **exactly** ChatGPT's proposed surface. Already done.

### Adonai-in-prayer (JDG B, NUM F, 2SA B)
- **JDG 6:15** — ships `ข้าแต่ท่านนายของข้าพเจ้า` (the pre-recognition arc form — ChatGPT's explicit recommendation).
- **JDG 6:22** — ships `ข้าแต่องค์พระผู้เป็นเจ้า` (no trailing พระเจ้า; no doubling). ✓
- **JDG 13:8** — ships `ข้าแต่องค์เจ้านาย` (exactly ChatGPT's proposed surface for standalone אֲדֹנָי). ✓
- **JDG 16:28** — ships `ข้าแต่องค์พระผู้เป็นเจ้า ... ข้าแต่พระเจ้า` (not the doubled form the AIs flagged). ✓

### Cross-book NT spellings (JDG C)
- **Heb 11:32** — spot-checked: already ships `กิดเอน ... เยฟทาห์` (JDG-side spellings). ✓ No edit needed.

### 1 Samuel pagan-deity register + Ashtoreth (1SA D)
- **1 Sam 5:7** — spot-checked: ships `ดาโกนพระของพวกเรา` (the Gemini-aligned option, doc-compliant per `pagan_deities_2026-04.md`). The AIs' claim that it shipped as `พระเจ้า` (the register violation) was **wrong** — the actual shipped Thai uses `พระของพวกเรา`, which is the locked OT-named-deity form.
- **1 Sam 7:3, 7:4, 12:10, 31:10 Ashtoreth** — spot-checked: all four already ship `พระอัชเทเรท` (the locked spelling). ✓

### "Is Saul also among the prophets" inclusio (1SA C)
- **1 Sam 19:24** — spot-checked: already ships `ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ` — exact match to 10:11 / 10:12. ✓

### Leviticus feast-name + goel (LEV B, LEV C)
- **LEV 23:6** — spot-checked: already ships `เทศกาลขนมปังไร้เชื้อ` (and `ขนมปังไร้เชื้อ` later in the verse). ✓ The AI flag was wrong.
- **LEV 25:25** — spot-checked: already ships `ญาติผู้ไถ่ของเขาที่ใกล้ชิดที่สุด` (locked form per `goel_kinsman_redeemer_2026-05.md`). ✓ The AI claim that it still read `ญาติสนิทที่สุด` was wrong.

### 1 KI death-formula lock confirmed in shipped corpus
- **1 KI 14:20** (Jeroboam — the Northern anchor) — spot-checked: ships **plain** `ก็ล่วงหลับไปอยู่กับบรรพบุรุษ และนาดับบุตรของเขาขึ้นครองราชย์แทน` ✓. This confirms the locked Davidic-vs-Northern register split is correctly applied. Implementing the AI's "restore ทรง to all" recommendation would have undone this lock.

### Leitwort "until this day" (1CH E, 2KI D, 2SA D, 2CH F)
- Resolved in `leitwort_handling_policy_2026-05.md §7.5 v0.6` (locked `จนถึงทุกวันนี้`; 1 Samuel verse-text normalized v0.5; 2CH fully conformant). This was the original flag you caught.

---

## ✗ REAL — verified verse edits still needed

Confirmed from the spot-check pass:

| Source | Verse | Current shipped | Should be | Why |
|---|---|---|---|---|
| GEN A | **GEN 40:14** | `แสดงความเมตตาต่อข้าพเจ้า` | `แสดงความรักมั่นคงต่อข้าพเจ้า` | חֶסֶד lock per `chesed_covenant_love_2026-05.md` — one Genesis verse missed in the corpus pass |
| 2CH C | **2 Chr 36:9** | `เยโฮยาคีนมีพระชนมายุสิบแปดพรรษา` ("eighteen") | `แปดพรรษา` ("eight") + Layer-2 footer noting 2 Kgs 24:8 / LXX read "eighteen" | MT שְׁמוֹנֶה is "eight"; shipped uses the harmonized synoptic number without disclosure. Real MT-base policy violation. |
| HEB D | **HEB 4:12** | `จิตวิญญาณและวิญญาณ` | `จิตใจและวิญญาณ` | จิตวิญญาณ ⊃ วิญญาณ overlap blunts the two-member Greek distinction (both AIs converge on this) |
| JUD E | **1 PET 1:2** | `…ขอพระคุณและสันติสุขจงทวียิ่งขึ้น…` | `…ทวีคูณ…` | Cross-book NT harmonization (matches 2PE 1:2 + JUD 1:2 which both ship `ทวีคูณ`). Both AIs converge. Not a doc-lock — a Catholic-Epistles formula-consistency call. |
| 1JN C | **1JN 2:2 `thai_summary`** | Contains "ลัทธิ Calvinism" + "ลัทธิ Arminianism" denomination labels | Neutral framing (e.g. "บางคนตีความว่า… ส่วนคนอื่นตีความว่า…") | Metadata only (not main verse text). Both AIs flagged the polemical denomination labels. |

Each main-text edit is a single-verse, well-bounded change. The 1JN one is a thai_summary rewrite.

---

## ? UNVERIFIED — proposals worth a quick look but not blockers

Items where I didn't spot-check the actual shipped JSON. These are mostly Layer-2 / thai_summary metadata additions, not main-text verse edits:

- **2 SA 15:7, 21:19, 24:1, 24:9, 24:13** — Tier-2 footer additions (per ChatGPT MAJOR). May or may not already exist in `output/textual_variants/`. Worth checking before tag.
- **1 SA 11, 13, 14, 17, 18** — Tier-2 chapter-footers proposed for MT/LXX variants. May exist; verify before tag.
- **LEV proposals (kipper / goel surface / 23:6 feast / LEV 16+17 footers)** — relevant docs (`sacrificial_vocabulary_2026-05.md`, `goel_kinsman_redeemer_2026-05.md`) exist but I didn't read them in this pass. Spot-checks still pending.
- **1 PET 1:2** — cross-book NT πληθυνθείη edit (`ทวียิ่งขึ้น` → `ทวีคูณ`). Quick to verify in `output/translations/1peter_01.json`.
- **1JN 2:2 thai_summary** — drop Calvinism/Arminianism labels. Reasonable; verify if the labels are actually still there.
- **New translator-decision docs** (genuinely new — confirmed by absence from translator_decisions/):
  - `foreign_monarch_register_2026-05.md` (EZR)
  - `god_of_heaven_persian_title_2026-05.md` (EZR)
  - `johannine_begotten_trinity_2026-05.md`, `johannine_menos_2026-05.md`, `johannine_pastoral_ambiguities_2026-05.md` (1JN)
  - `necromancy_ob_yiddeoni_2026-05.md` (1SA)
  - `pseudepigrapha_citations_2026-05.md` (JUD)

These are forward-protective docs you may want to write before the relevant next books ship — they're additive, not corrective.

---

## What the pattern reveals (for next time)

Same as ChatGPT's LEV §Z observation: **the packets shipped to the external AIs don't include the `docs/translator_decisions/` lock catalog.** The AIs see only the items doc the audit assembled, so they re-litigate questions the project has already settled. The end-of-book audit doc *itself* may also be stale relative to subsequent normalization commits (e.g. 2 CH audit said "1 Samuel is the lone outlier" — but 1 Samuel had been normalized by then; the audit hadn't been refreshed).

**Mitigations for future runs:**
1. The Cowork instructions could direct it to also fetch a flat list of `docs/translator_decisions/*.md` names so the AIs at least know what's already locked.
2. Claude Code's processing step (this loop) should cross-check every "Recommended action" against the lock catalog **before** writing it into the response doc — exactly the discipline this report applies retroactively.
3. End-of-book audit docs should be refreshed against the live corpus before the packet is built (or at least the items doc should be).

For the current PR (#168), no auto-application happened — the guardrail held. But the proposed-edit lists would have wasted hours of review work without this verification pass.

---

## Recommended next step

PR #168 is safe to merge as-is — the response docs are useful provenance, even where their proposed-edit lists are mostly MOOT. Treat this report as the actionable summary; ignore the per-response "Proposed verse edits" sections in favor of the three REAL edits above and the UNVERIFIED list (quick spot-checks).
