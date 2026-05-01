# John — External AI Review Response

**Date:** 2026-05-01
**Reviewers:** ChatGPT (independent review with citations); Gemini (independent review)
**Audit doc:** `JHN_END_OF_BOOK_REVIEW_2026-04-30.md`

This doc records the disposition of each AI-flagged item. Three spot-revisions implemented (3:11, 5:10-18, 7:8), one footer note added (1:34); other items locked or deferred to corpus-doc.

---

## Item A — Ἰουδαῖοι contextual split (5:10–18 drift)

**Both AIs flagged.** ChatGPT: "พวกผู้นำยิว at 5:10/15/16/18 looks like a one-block drift, not a principled category." Gemini: "the 1-block drift to 'พวกผู้นำยิว' in ch 5 introduces an unnecessary lexical variant."

**Disposition:** **REVISED.** John 5:10, 15, 16, 18: `พวกผู้นำยิว` → `ผู้นำชาวยิว`. Aligns with the JHN 1:19 baseline lock. Swept across thai_literal, key_decisions, and notes for full consistency.

**Doc action:** `docs/translator_decisions/john_ioudaioi_rendering.md` queued for pre-Romans/Revelation lock-in (formalize the 4-way contextual split).

**Passion narrative (ch 18-19) not touched** — ChatGPT acknowledges defensible-as-compressed-narrative-register; Gemini suggests normalizing to short `ยิว`. Mixed feedback; deferred to corpus-doc decision.

---

## Item B — λόγος seven-way contextual rendering

**Both AIs FINE.** Gemini: "masterfully navigates Thai honorifics and theological registers. The Farewell Discourse 'drift' to คำ is not an error; when Jesus refers to his *own* speech, the plain คำ correctly avoids unnatural self-aggrandizing ราชาศัพท์."

**Disposition:** **LOCK as-is.** Doc queued: `logos_translating_rule.md` (self-reference vs narrator-reference) before 1 John / Hebrews / Revelation.

---

## Item C — JHN 3:11 doubled-amen drift

**Both AIs MAJOR CONCERN.** Both flagged as a clean Johannine-formula violation.

**Disposition:** **REVISED.** JHN 3:11: `ความจริง ความจริง เราบอกท่านว่า` → `อาเมน อาเมน เราบอกท่านว่า`. Aligns with the Johannine doubled-amen lock used at 13:38, 21:18, and 25 other Johannine occurrences. Notes updated to flag the revision.

**§Z verification:** Both AIs flagged a typo `อาเมว` in the audit packet. Verified the actual corpus uses correct spelling `อาเมน`; the typo was packet-only.

---

## Item D — JHN 7:8 SBLGNT οὐκ vs Thai "ยังไม่"

**Both AIs CONCERN.** Both flagged as RULES §0 SBLGNT-strict violation. Prior `เรายังไม่ขึ้นไป` effectively translated the rejected Byzantine οὔπω reading.

**Disposition:** **REVISED.** JHN 7:8: `เรายังไม่ขึ้นไปยังเทศกาลนี้` → `เราไม่ขึ้นไปยังเทศกาลนี้`. The final clause's genuine οὔπω → `ยังไม่ครบกำหนด` preserves the Greek distinction between SBLGNT οὐκ (not) at clause 1 and οὔπω (not yet) at clause 2. Notes updated with textual-variant explanation; back-translation updated to "I am not going up" (was "I am not yet going up").

---

## Item E — JHN 1:34 ἐκλεκτός vs υἱός

**Mixed:** ChatGPT CONCERN + footer note; Gemini FINE + footer note. Both want a footer note added to acknowledge the textual variant.

**Disposition:** **FOOTER NOTE ADDED.** Translation kept (`ผู้ที่พระเจ้าทρงเลือกสρρ` per RULES §0 SBLGNT). 1:34 notes augmented with the textual-variant note recommendation: `ต้นฉบับโบราณส่วนใหญ่: 'พระบุตρของพระเจ้α'`.

---

## Items F, G, H — All FINE, lock as-is

- **F: Ἐγώ εἰμι absolute** (4:26, 6:20, 8:24/28/58, 13:19, 18:5-8): Both AIs agree contextual rendering preserves narrative pragmatics + theological force. Lock; document four-way split in corpus doc.
- **G: Father↔Son glorification idiom** (พระสิริ + causative): Both AIs agree this is a "brilliant theological distinction." Amend `divine_object_praise_verbs_2026-04.md` with Trinitarian พระสิริ sub-rule.
- **H: ἀγαπάω/φิλέω flattening to รัก** at 21:15-17: Both AIs agree synonym-hypothesis is mainstream Johannine scholarship; preserving artificial distinction would impose anachronistic-sermon-tradition. Lock; corpus-doc.

---

## §Z — Spelling audit

Both AIs flagged the audit-packet typo `อาเมว` (should be `อาเมน`). Verified actual corpus spelling: **correct as อาเมน** throughout. The typo was packet-only.

---

## Summary table

| Item | Verdict | Action | Status |
|---|---|---|---|
| A Ioudaioi 5:10-18 drift | Both flagged | **Revised** to ผู้นำชาวยิว | ✅ done |
| B λόγος seven-way | Both FINE | Lock; doc queued | ✅ no revision |
| C 3:11 doubled-amen | Both MAJOR CONCERN | **Revised** to อาเมν อาเμν | ✅ done |
| D 7:8 ยังไม่ → ไม่ | Both CONCERN | **Revised** + back-translation | ✅ done |
| E 1:34 ἐκλεκτός | Mixed CONCERN/FINE | **Footer note added** | ✅ done |
| F Ἐγώ εἰμι | Both FINE | Lock; doc queued | ✅ no revision |
| G Father↔Son glory | Both FINE | Amend praise-verbs doc | ✅ no revision |
| H ἀγαπάω/φιλέω | Both FINE | Lock; doc queued | ✅ no revision |
| §Z spelling audit | Packet-typo | Verified clean | ✅ no action |

---

## Tagging eligibility

- §1 mechanical gates: ✅ clean (verified post-revision)
- §2 audit doc: ✅ done (2026-04-30)
- §3 external AI review: ✅ done (this doc; ChatGPT + Gemini independent)
- §4 reviewer hand-off: ongoing per project async-review policy
- §5 lock the book: ready after these revisions land.

**Tag `book-john-v1` is GO.** All AI-flagged immediate revisions implemented; corpus-docs queued for pre-Acts/Romans/Revelation.
