# Luke — External AI Review Response

**Date:** 2026-05-01
**Reviewers:** ChatGPT (GPT-5.5 Thinking, detailed independent review); Gemini (independent corpus-level review)
**Audit doc:** `LUK_END_OF_BOOK_REVIEW_2026-04-22.md`
**External packet:** `external_review_packet_LUK_2026-04-23.md`

This doc records the disposition of each AI-flagged item. Two spot-revisions implemented (Luke 1:17, Luke 4 adversary-speech); other concerns logged as deferred-decision-docs queued before Acts 2 / Romans.

---

## Item 1 — Luke 4 adversary speech register (RULES §3 violation)

**Both AIs flagged.** ChatGPT: "spot revise adversarial speech-introductions in Luke 4. Replace ทูลพระองค์ว่า with neutral form." Gemini: "RULES.md §3 explicitly states: 'Demons/adversaries: neutral/distancing register, no honorifics.' This creates a direct, documented conflict."

**Disposition:** **REVISED.** Luke 4:3, 4:6, 4:9: `มารทูลพระองค์ว่า` → `มารกล่าวกับพระองค์ว่า`.

The translator-note at 4:3 had appealed to MAT 4 as precedent — but MAT 4 actually uses `กล่าว` (RULES §3 compliant). Luke 4 was the corpus outlier. Revised rationale at 4:3 documents the correction.

**New corpus doc:** `docs/translator_decisions/adversary_speech_register_2026-05.md` formalizes the rule for forward-enforcement (Acts, Revelation).

---

## Item 2 — Luke 1:17 πνεῦμα over-honorified (πνεῦμα Ἠλίου)

**ChatGPT flag (Gemini did not flag).** πνεῦμα at 1:17 refers to Elijah's prophetic-spirit/disposition, not πνεῦμα ἅγιον. The locked Holy-Spirit rendering `พระวิญญาณ` was being used for a non-Holy-Spirit referent, blurring the semantic boundary critical for Acts.

**Disposition:** **REVISED.** Luke 1:17: `ด้วยพระวิญญαณและฤทธิ์เดชของเอลียาห์` → `ด้วยจิตวิญญαณและฤทธิ์เดชของเอลียาห์` (lowercase anthropological-spirit register, consistent with 1 Th 5:23 lock for human-πνεῦμα). Key-decision rationale updated.

---

## Item 3 — ChatGPT-flagged drift checks (verified false-alarms)

ChatGPT flagged 2 specific verses based on packet-text excerpts that did not match current corpus state:

- **Luke 1:77**: ChatGPT said `การอภัยบาπ` (drift). Current corpus state (verified): `การยกโทษบาπ` (matches lock). **Already correct.** ChatGPT's source-text was stale.
- **Luke 10:13**: ChatGPT said `กลับใจใหม่` (drift). Current corpus state (verified): `กลับใจ` (matches lock; normalized 2026-04-23 per existing rationale). **Already correct.** ChatGPT's source-text was stale.

**No revision.** These were already locked correctly; ChatGPT was reading from a pre-normalization snapshot in the audit packet.

---

## Item 4 — Luke 18:14 δικαιόω family — `ทรงชำระ...ให้เป็นผู้ชอบธρρμ`

**ChatGPT flagged** as Pauline-forward-risk: `ทรงชำρะ` ("purify") may obscure the forensic-declarative force of δικαιόω in Romans/Galatians.

**Disposition:** **DEFERRED.** Verified Luke 18:14 is acceptable in-context per ChatGPT's own assessment ("probably acceptable in Luke by itself, but it becomes high-risk once Romans/Galatians arrive"). NOT a Luke-blocker.

**Doc action:** Stub `docs/translator_decisions/dikaioo_dikaiosyne_family_DEFERRED_2026-05.md` queued before Romans 1 ships. Will revisit Luke 18:14 + lock δικαιόω-family policy at that point.

---

## Item 5 — ἄφεσις / ἀφίημι forgiveness-release vocabulary

**ChatGPT flagged** Luke 4:18 (`ปลดปล่อย` Jubilee-release) vs Luke 1:77 + 24:47 (`การยกโทษบาπ` formal forgiveness-formula).

**Disposition:** **NOT A DRIFT — already principled.** The Luke 4:18 `ปลดปล่อย` IS the correct Jubilee/Isaiah-61-release sense (≠ forgiveness-of-sins). The Luke 1:77 + Luke 24:47 uniform `การยกโทษบาπ` matches the existing corpus lock from MAT/MRK + post-2026-04-19 phrase-consistency normalization. ChatGPT misread these as inconsistent.

**Doc action:** Existing `aphesis_forgiveness_of_sins_2026-04.md` already covers this. Verified rationale rationales at 1:77 + 24:47 explicitly cite the lock + normalization. No further action.

---

## Item 6 — Pneuma semantic domains (Luke-Acts pre-Acts lock)

**ChatGPT recommended** new corpus doc `pneuma_semantic_domains_luke_acts_2026-05.md` distinguishing Holy Spirit / human spirit / evil spirits / ghost / disposition.

**Disposition:** **DEFERRED.** Acts-forward preparation. Current Luke renderings are largely correct (1:17 just revised; other Luke πνεῦμα occurrences appear context-disambiguated). The doc itself is more useful as a forward-rule than a retrospective revision.

**Doc action:** Queued as `pneuma_semantic_domains_luke_acts_DEFERRED_2026-05.md` for pre-Acts-2-ship lock-in. NOT blocking Luke tag.

---

## Item 7 — Logos / rhema word-speech taxonomy

**ChatGPT recommended** new corpus doc for Acts-forward narrative-vocabulary stability.

**Disposition:** **DEFERRED.** Current Luke renderings are sensible-and-context-appropriate per ChatGPT's own assessment ("These are not wrong; the variation is largely contextual"). NOT a Luke-blocker.

**Doc action:** Queued for pre-Acts-2 lock-in. NOT blocking Luke tag.

---

## Item 8 — Hilaskomai / hilasterion / atonement vocabulary

**ChatGPT flagged** Luke 18:13 `ขอทρงพระเมตตα` for ἱλάσθητί as potentially flat for Romans 3:25 / Hebrews. Acceptable in Luke context.

**Disposition:** **DEFERRED.** Pre-Romans-3 / pre-Hebrews lock-in. NOT a Luke-blocker.

---

## Gemini-only items (not duplicated by ChatGPT)

**Gemini A2: OT-citation LXX-vs-MT alignment (whole-Bible philosophy).** This is a project-philosophy question for OT-translation-phase. NOT a Luke-blocker. Documented in `RULES.md` §0 stance (NT quotes the LXX faithfully; OT will be translated from MT-Hebrew). Gemini's concern is that future OT-Deut 6 will read differently from Luke 4:8's quote-of-LXX-Deut-6:13 — this is intentional and standard NT-translation practice.

**Gemini A3: pneumatology filling-vs-fullness lock.** πίμπλημι πνεύματος (`เต็มเปี่ยมด้วย`) vs πλήρης πνεύματος (`บριบูρณ์ด้วย`). Gemini affirms the current distinction is "excellent and nuanced" — recommends formal lock-doc for Acts-forward. **DEFERRED** — queued for pre-Acts-2.

**Gemini's Acts-forward prep items** (Name-formulas, "the Way", Ascension vocabulary): all deferred to Acts-prep, not Luke-blockers.

---

## Summary table

| Item | Source | Verdict | Action | Status |
|---|---|---|---|---|
| Luke 4 adversary `ทูล` | Both AIs | RULES §3 violation | **Revised + corpus doc locked** | ✅ done |
| Luke 1:17 πνεῦμα Elijah | ChatGPT | Holy-Spirit blur | **Revised** (พระวิญญαณ → จิตวิญญαณ) | ✅ done |
| Luke 1:77 / 10:13 drift | ChatGPT | Stale source-text | Already correct | ✅ no action |
| Luke 18:14 δικαιόω | ChatGPT | Pre-Romans risk | Deferred + stub doc queued | 🟡 pre-Romans |
| ἄφεσις family | ChatGPT | Misread | Already principled | ✅ no action |
| pneuma domains doc | ChatGPT | Acts-prep | Deferred + stub doc queued | 🟡 pre-Acts |
| logos/rhema doc | ChatGPT | Acts-prep | Deferred + stub doc queued | 🟡 pre-Acts |
| hilaskomai doc | ChatGPT | Pre-Romans/Hebrews | Deferred + stub doc queued | 🟡 pre-Romans |
| OT citation LXX/MT | Gemini | Project-philosophy | Documented (RULES §0 stance) | ✅ no action |
| pneuma filling lock | Gemini | Acts-prep | Deferred (current renderings correct) | 🟡 pre-Acts |
| Acts-forward prep | Gemini | Acts-prep | Deferred (Name, Way, Ascension) | 🟡 pre-Acts |

---

## Tagging eligibility

- §1 mechanical gates: ✅ clean
- §2 audit doc: ✅ done (2026-04-22)
- §3 external AI review: ✅ done (this doc; ChatGPT + Gemini independent reviews)
- §4 reviewer hand-off: 🟡 ongoing (Luke 1-2 native-speaker spot-check still pending; not blocking per audit-doc-soft-block memory)
- §5 lock the book: ready after these revisions land.

**Tag `book-luke-v1` is GO.** All AI-flagged immediate revisions implemented; Acts-forward prep-docs queued; native-speaker review remains async per project-policy `feedback_async_review.md`.
