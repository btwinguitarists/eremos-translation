# 1 Peter — External AI Review Response

**Date:** 2026-05-03
**Reviewers:** ChatGPT (independent review); Gemini (independent review)
**Audit doc:** `1PE_END_OF_BOOK_REVIEW_2026-05-03.md`
**Items doc:** (audit doc + AI packet) — items lettered A–J in the AI sanity-check pass

This doc records the disposition of each AI-flagged item. **The two AIs converge on every item except Item E** (where ChatGPT raised a CONCERN about a possible **บา** + Greek-beta typo in the audit packet — verified clean in source). **No verse-text revisions required;** four corpus-doc lifts queued and one existing doc amended.

Status legend: **LOCK** = no revision; **REVISE** = AI consensus requires verse-text edit; **DOC** = corpus-doc lift queued; **DEFER** = surface for Ben's decision; **NO ACTION** = AI flagged but cross-check shows current state already correct.

---

## Item A — 1 Pet 3:19 spirits-in-prison: lexical-ambiguity-preservation

**Both AIs FINE.** ChatGPT: "The Thai preserves the Greek ambiguity of ἐν ᾧ, πορευθεὶς ἐκήρυξεν, and πνεύμασιν without forcing Noah-era, fallen-angels, or postmortem-human readings." Gemini: "Preserving the lexical ambiguity in the main text of 1 Pet 3:19 honors the project's optimal equivalence philosophy, leaving exegetical debates to commentators rather than forcing a translator's theological gloss."

**Disposition:** **LOCK** 1 Pet 3:19 main text as-is. Existing `thai_summary` already documents all three mainstream interpretations (fallen-angels / dead-humans-from-flood / pre-incarnate-Christ-through-Noah) for Thai pastors. **DOC** — covered by the new `petrine_eschatological_disambiguation_2026-05.md` (see Item B).

---

## Item B — 1 Pet 4:6 gospel-preached-to-the-dead: explicit disambiguation

**Both AIs FINE.** ChatGPT: "'ผู้ที่บัดนี้ตายไปแล้ว' is interpretive, but it rightly blocks postmortem-evangelism where the broader NT canon makes that reading theologically hazardous. This differs from 3:19 because 3:19 remains exegetically irreducible." Gemini: "The mixed strategy is entirely standard for evangelical translation (matching NIV/ESV/CSB); disambiguating 1 Pet 4:6 prevents readers from forming a post-mortem salvific theology that directly contradicts Hebrews 9:27. Documenting this implicit principle ensures consistency when tackling similar eschatological ambiguities in Hebrews, 2 Peter, and Jude."

**Disposition:** **LOCK** 1 Pet 4:6 as-is. **DOC** queued: `docs/translator_decisions/petrine_eschatological_disambiguation_2026-05.md` formally encodes the principle: *preserve ambiguity when multiple readings are exegetically irreducible; disambiguate when one reading is theologically incompatible with the rest of Scripture*. Anchors to HEB 9:27. Anticipated cross-corpus applications: 2 Pet 3:9; 2 Thess 1:9.

---

## Item C — 1 Pet 3:21 baptism: ἀντίτυπον → ภาพแทน + ἐπερώτημα → คำสัญญา

**Both AIs FINE.** ChatGPT: "ภาพแทน adequately preserves typological correspondence. คำสัญญา is a defensible pledge-reading of ἐπερώτημα and fits the verse's anti-regeneration qualifier: 'not removal of dirt…but…'" Gemini: "Both rendered terms reflect standard evangelical scholarship (NIV/CSB alignment), and the Thai explicitly retains the 'ไม่ใช่การล้างความสกปรก' qualifier, preserving Peter's theological guardrails against baptismal regeneration."

**Disposition:** **LOCK** 1 Pet 3:21 as-is. The existing `thai_summary` already explains the anti-regeneration position to Thai readers ("เปโตรไม่ได้สอนว่าน้ำบัพติศมาเองช่วยให้รอด... 'คำสัญญาของจิตสำนึกที่ดี' คือพันธสัญญาที่ผู้เชื่อยอมรับ"). **NO ACTION** — no separate footer-note required. Optional Catholic/Orthodox-context footer-note left to Ben's discretion; not blocking the v1 tag.

---

## Item D — 1 Pet 2:9 βασίλειον ἱεράτευμα single-concept "royal priesthood"

**Both AIs FINE.** ChatGPT: "βασίλειον ἱεράτευμα in 1 Peter 2:9 naturally echoes Exod 19:6 LXX as a single title, so ปุโรหิตหลวง is justified. Revelation's βασιλείαν, ἱερεῖς is grammatically different and should not be flattened back into the 1 Peter wording." Gemini: "The grammatical difference between the LXX citation in 1 Pet 2:9 (appositional/adjectival βασίλειον ἱεράτευμα) and the explicit dual-noun construction in Revelation 1:6, 5:10, and 20:6 (βασιλείαν, ἱερεῖς) justifies distinct Thai renderings."

**Disposition:** **LOCK** 1 Pet 2:9 as **ปุโรหิตหลวง** (single-concept). **NOTED-FOR-FUTURE-WORK:** when Revelation translates 1:6 / 5:10 / 20:6, render the dual-construction βασιλείαν, ἱερεῖς as **ราชอาณาจักร และปุโรหิต** (or equivalent dual-Thai) — preserving Greek-grammar fidelity at each verse rather than flattening the Petrine + Johannine vocabulary into a single rendering. **NO new doc** (the locking note is recorded here + cross-referenced in `poimēn_episkopos_register_split_2026-05.md`).

---

## Item E — 1 Pet 5:13 Babylon transliteration + συνεκλεκτή → คริสตจักร

**ChatGPT CONCERN; Gemini FINE.** ChatGPT noted: "Transliteration of Βαβυλών is correct... But the shown Thai has บา**β**ิโลน with a Greek beta character; that should be Thai-script บาบิโลน unless this is only a packet typo." Gemini: "Retaining the transliteration บาβิโลน [sic] is vital for preserving the scriptural meta-narrative and typological links to Revelation's imperial critique."

**Verification:** Source-text inspection (`output/translations/1peter_05.json` v.13) confirms Thai-script **บาบิโลน** throughout — both in the main `thai` field and `thai_summary`. Greek-script-beta does not appear. **Conclusion:** the Greek-beta in the AI packet was a copy-paste artifact of the audit packet, not present in the source.

**Disposition:** **LOCK** 1 Pet 5:13 as-is. Source clean. **NO ACTION** (no source revision needed). The existing `thai_summary` already explains the Babylon-=-Rome metaphor for Thai readers ("‘บาบิโลน’ ในที่นี้น่าจะหมายถึงเมืองโรม... หนังสือวิวรณ์ก็ใช้ ‘บาบิโลน’ ในความหมายเดียวกันเป็นภาพแทนของโรม"). Both AIs' recommendation for a footer-note (หมายถึงโรม) is satisfied by the existing summary.

---

## Item F — 1 Pet 3:7 σκεῦος → ภาชนะ (wife-context)

**Both AIs FINE.** ChatGPT: "In 1 Pet 3:7, γυναικείῳ makes the wife-referent explicit, so preserving σκεῦος as ภาชนะ is lexically justified even if culturally awkward. 1 Thess 4:4 should not be forced into the same rendering because its referent is contextually debated." Gemini: "Enforcing cross-corpus uniformity between 1 Thess 4:4 (body) and 1 Pet 3:7 (wife) would impose artificial rigidity. Preserving the literal ภาชนะที่อ่อนแอกว่า metaphor maintains optimal equivalence."

**Disposition:** **LOCK** 1 Pet 3:7 as-is. The σκεῦος → ภาชนะ rendering is contextually-correct because γυναικεῖος ("of-the-female") makes the wife-referent grammatically explicit at this verse. **NO ACTION** on 1 Thess 4:4 (contextual referent governs σκεῦος; the prior 1TH-4:4 BODY rendering remains valid). The two passages use the *same Greek lemma* in *opposite referent-roles* — the Thai correctly distinguishes them.

---

## Item G — Petrine πάσχω/πάθημα suffering register-split

**Both AIs FINE.** ChatGPT: "Christ-subject πάσχω with ทรงทนทุกข์ and believer-subject πάσχω with ทนทุกข์ preserves Thai divine honorific logic while maintaining the lexical link. 4:13 still makes participation clear through 'มีส่วนร่วม…การทนทุกข์ของพระคริสต์.'" Gemini: "The split cleanly maps the project's existing royal-register rules for divine subjects onto the shared lexical root, organically highlighting the participatory theology of 1 Pet 4:13 without forcing it."

**Disposition:** **LOCK** the register-split. **DOC** queued: `docs/translator_decisions/pascho_pathema_suffering_2026-05.md` records the subject-driven royal/plain split (Christ → ทรงทนทุกข์; believers → ทนทุกข์; πάθημα process-noun → การทนทุกข์ for both subjects). Pre-Hebrews lock — Heb 2:10, 5:8, 9:26, 13:12 + Heb 2:18 + Pauline 2 Cor 1:5, Phil 3:10, Col 1:24 all governed.

---

## Item H — Petrine ψυχή pattern (theological-anthropology vs idiomatic-counting)

**Both AIs FINE.** ChatGPT: "The split between จิตวิญญาณ for theological-anthropological ψυχή and คน for idiomatic counting-souls at 3:20 is correct. Luke 23:46 uses πνεῦμα, so preserving lexical distinction rather than harmonizing is right." Gemini: "Treating ψυχή as คน in counting contexts (3:20) and จิตวิญญาณ in theological contexts honors both Greek idiom and Thai naturalness. For 4:19, preserving the lexical distinction between Peter's ψυχὰς (จิตวิญญาณ) and Luke's πνεῦμά (จิต or พระวิญญาณ) respects the distinct authorial vocabulary over artificial cross-author harmonization."

**Disposition:** **LOCK** all 1 Pet ψυχή renderings as-is. **NO ACTION** — already governed by `psyche_vs_pneuma_anthropological_2026-04.md`; the verified-compliant verses confirm the doc holds for the Petrine corpus.

---

## Item I — Petrine ἀποκάλυψις / φανερόω as the eschatological-Christ-coming

**Both AIs FINE.** ChatGPT: "1 Peter's eschatology uses unveiling/manifestation language, not παρουσία. การสำแดง / ทรงสำแดง preserves that Petrine lexical profile while allowing παρουσία elsewhere to remain การเสด็จมา." Gemini: "Honoring the lexical variation is the very definition of optimal equivalence."

**Disposition:** **LOCK** the lexical-distinction. **DOC AMEND:** `docs/translator_decisions/parousia_christou_2026-05.md` extended with §Petrine subsection. The lock now governs:
- Pauline παρουσία → **การเสด็จมา**
- Petrine ἀποκάλυψις → **การสำแดง**
- Petrine φανερόω passive → **ทรงสำแดงพระองค์**

When **2 Peter 1:16** ships (the only Petrine use of παρουσία), it will pivot back to **การเสด็จมา** per the lemma-driven rule.

---

## Item J — Petrine 5:8 διάβολος-as-roaring-lion

**Both AIs FINE.** ChatGPT: "ปฏิปักษ์, มาร, สิงโตคำราม, and กลืนกิน preserve the legal, personal, animal, and devouring imagery. The same Greek verb καταπίνω can be rendered กลืนกิน in both 1 Pet 5:8 and 1 Cor 15:54; the contexts invert the object, not the core lexical sense." Gemini: "The plain register for διάβολος perfectly executes the project's spiritual-hierarchy rules, avoiding undue reverence."

**Disposition:** **LOCK** 1 Pet 5:8 as-is. **NO ACTION** — already governed by `spiritual_beings_hierarchy_2026-05.md` (διάβολος → มาร, plain register). ChatGPT's καταπίνω → กลืนกิน cross-link to 1 Cor 15:54 noted; verify the unification holds when this verse is encountered in subsequent translations.

---

## Item §Z — Anything else

**ChatGPT:** "Only one concrete issue: verify that บา**β**ิโลน is not actually in the Thai source. If it is, fix to บาบิโลน." → Verified clean (Item E above). No source-revision required.

---

## Pipeline summary

| Action | Status |
|---|---|
| **REVISE** verse-text | None required (0 of 10 items) |
| **DOC** new (`pascho_pathema_suffering_2026-05.md`) | Created |
| **DOC** new (`parepidemos_paroikos_sojourner_2026-05.md`) | Created |
| **DOC** new (`poimen_episkopos_register_split_2026-05.md`) | Created |
| **DOC** new (`petrine_eschatological_disambiguation_2026-05.md`) | Created |
| **DOC** amend (`parousia_christou_2026-05.md` §Petrine) | Done |
| **DEFER** to Ben | None |

All 10 items LOCK with corpus-doc support. The book-1peter-v1 tag is unblocked.

## Next steps

1. Merge this PR + the four new docs + parousia amendment to main.
2. Run `bash scripts/ship_book.sh 1PE` for the bundle PR + iOS bump + tag book-1peter-v1.
3. /loop translation can resume to 2 Peter.
