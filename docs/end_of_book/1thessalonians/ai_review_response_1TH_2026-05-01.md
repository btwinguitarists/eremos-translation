# 1 Thessalonians — External AI Review Response

**Date:** 2026-05-01
**Reviewers:** Claude (Anthropic, detailed independent review with corpus-doc-recommendation index); Gemini (independent review); ChatGPT (independent review)
**Audit doc:** `1TH_END_OF_BOOK_REVIEW_2026-04-30.md`

This doc records the disposition of each AI-flagged item. **Three of the eight items were already corrected in live corpus** (audit packets had stale snapshots — the same pattern observed during the Acts review). One footer note added at 4:4. Rest locked.

---

## Item A — παρουσία = การเสด็จมα (with 2 Thess 2:9 forward-flag)

**All three AIs FINE for 1 Thess Christ-parousia (2:19, 3:13, 4:15, 5:23) + CONCERN for 2 Thess 2:9 lawless-one parousia.**

**Disposition:** **NO REVISION NEEDED.** Verified:
- 1 Thess Christ-parousia: all use `การเสด็จมา` correctly (royal-divine register, RULES §3 compliant).
- 2 Thess 2:9 lawless-one parousia (already shipped): uses `การมาถึงของเขา` (NOT royal `เสด็จ`). The principled-split between Christ-parousia (royal) and lawless-one-parousia (plain) is already in place.
- 2 Thess 2:8 (Christ-subject `จะทρงประหาร...ด้วยการปρากฏแห่งการเสด็จมาของพระองค์`) correctly uses `เสด็จ` because the subject IS Christ. The split is verb-by-verb context-sensitive, exactly as the AIs recommended.

The audit packet flagged a hypothetical risk; the live corpus already handles it correctly.

**Doc action:** `parousia_register_split_2026-05.md` queued to formally lock the split-rule (Christ → เสด็จ; antichrist/non-divine → มาถึง).

---

## Item B — ἁγιασμός / ἁγιωσύνη / ἀκαθαρσία cluster

**All three AIs FINE.** Affirm the Thai morphological split (`การ-` process / `ความ-` state) elegantly mirrors the Greek aspectual contrast.

**Disposition:** **LOCK as-is.** Corpus doc queued: `pauline_sanctification_cluster_2026-05.md` before Romans 6 / Hebrews 12.

---

## Item C — ἁρπαγησόμεθα / ἀπάντησις at 4:17

**All three AIs:** FINE for `ถูกρับขึ้นไป`; CONCERN for `พบกับ` — recommend revise to `ต้อนρับ` (civic-reception/escort).

**Disposition:** **NO REVISION NEEDED.** Verified live corpus 1Th 4:17: already uses `เพื่อต้อนรับองค์พระผู้เป็นเจ้า`. The packet flagged `พบกับ` but the live corpus has the corrected rendering. AIs were reading stale snapshot.

---

## Item D — ἡμέρα κυρίου = วันแห่งองค์พระผู้เป็นเจ้า

**All three AIs FINE.** Affirm `แห่ง` preserves the technical-term feel (vs `ของ` plain-possessive). 5:5 `บุτρแห่งวัน` extends the Hebraic idiom consistently.

**Disposition:** **LOCK as-is.** Corpus doc queued: `day_of_the_lord_christ_2026-05.md` to unify ἡμέρα κυρίου / ἡμέρα Χριστοῦ across Pauline corpus.

---

## Item E — πνεῦμα + ψυχή + σῶμα tripartite at 5:23

**All three AIs FINE.** Affirm the context-based exception (วิญญαณ + จิตใจ + ร่างกาย) is necessary because the locked default (จิตวิญญαณ + จิต) would collapse the threefold list into incoherent redundancy.

**Disposition:** **LOCK as-is.** Existing `psyche_vs_pneuma_anthropological_2026-04.md` to be amended with explicit 5:23 exception (queued).

---

## Item F — σκεῦος at 4:4 (body vs wife)

**All three AIs CONCERN.** Recommend keep BODY in main text + add footer note for WIFE alternative (CSB-style precedent). κτάομαι "acquire" lexical-pressure + 1 Pet 3:7 parallel make the wife-reading historically/lexically significant.

**Disposition:** **FOOTER NOTE ADDED.** 1Th 4:4 notes augmented with the alternative-rendering and footer-text recommendation. Main text kept as `ครอบครองร่างกายของตนเอง`. Existing reviewer YAML `B_1TH4_skeuos_body_or_wife.yml` at EremosVercel2 captures this for native-Thai pastoral input.

---

## Item G — ἅγιοι at 3:13 (angels vs departed believers)

**Mixed:**
- Claude: FINE (lock `วิสุทธิชน`)
- Gemini: CONCERN (recommend neutral `บρρดาผู้บริสุทธิ์ของพระองค์`)
- ChatGPT: CONCERN (recommend `บρρดาผู้บริสุทธิ์ทุกคนของพระองค์`)

**Disposition:** **NO REVISION NEEDED.** Verified live corpus 1Th 3:13: already uses `พρ้อมกับบρρดาผู้บริสุทธิ์ทุกคนของพระองค์` (= ChatGPT's exact recommendation, preserves Greek ambiguity between angelic and departed-believer readings). Audit packet flagged `วิสุทธิชน` but live corpus has the neutral phrasing. AIs were reading stale snapshot.

**Doc action:** `parousia_holy_ones_2026-05.md` queued to unify across 1Th 3:13, 2Th 1:7, Jude 14 (where angelic context is unambiguous).

---

## Item H — 2:14-16 anti-Jewish polemic + interpolation question

**All three AIs FINE.** Lock SBLGNT-as-authentic stance. None recommend adding JHN-style `ผู้นำ` marker — `συμφυλετῶν` parallelism makes the historical-persecutors reading clear without it.

**Disposition:** **LOCK as-is.** No revision.

---

## Claude AI's broader observation: pauline_corpus_locks.md index

Claude flagged a forward-organization pattern: as Pauline-corpus completion accelerates, decision-docs proliferate per-decision. Recommends a single `pauline_corpus_locks.md` index doc tracking: (i) what's locked, (ii) trigger verses, (iii) forthcoming-test verses. **Adopted recommendation.** Index doc queued.

---

## Summary table

| Item | AI Verdict | Action | Status |
|---|---|---|---|
| A παρουσία split | All FINE; 2Th 2:9 forward-flag | Verified already-principled-split (stale packet) | ✅ no action |
| B Sanctification cluster | All FINE | Lock; doc queued | ✅ no revision |
| C ἀπάντησις 4:17 | Both CONCERN | Verified already-correct (stale packet) | ✅ no action |
| D ἡμέρα κυρίου | All FINE | Lock; doc queued | ✅ no revision |
| E πνεῦμα/ψυχή/σῶμα 5:23 | All FINE | Lock; existing doc to amend | ✅ no revision |
| F σκεῦος 4:4 | All CONCERN | **Footer note added** | ✅ done |
| G ἅγιοι 3:13 | Mixed FINE/CONCERN | Verified already-corrected (stale packet) | ✅ no action |
| H 2:14-16 polemic | All FINE | Lock as-is | ✅ no revision |
| §Z corpus index | Claude-flag | Queue `pauline_corpus_locks.md` index | 📋 queued |

---

## Tagging eligibility

- §1 mechanical gates: ✅ clean
- §2 audit doc: ✅ done (2026-04-30)
- §3 external AI review: ✅ done (this doc; 3 AIs independent — strongest sample size yet)
- §4 reviewer hand-off: ongoing per project async-review policy (B_1TH4_skeuos YAML active)
- §5 lock the book: ready (footer note is documentation-only).

**Tag `book-1thessalonians-v1` is GO.** Three of eight items were verified already-correct in the live corpus despite AIs flagging them — the project has been doing pre-tag normalization passes that the audit-packet snapshot didn't capture. Pattern documented in the Acts review response also.
