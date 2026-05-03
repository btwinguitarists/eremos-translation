# 3 John — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 1 chapter (15 verses; 32 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (47 docs).
**Trigger:** 3JN 1 shipped (commit `fb63db0`); per `docs/END_OF_BOOK_CHECKLIST.md`. (3JN is single-chapter; the chapter and the book are coterminous.)
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **11 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 1/1 chapter has a green per-chapter `*_review.md` report + back-translation; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-227-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows no 3JN source-file dirt (only unrelated paratext exports + a 1JN textual_variants file from the prior 1JN audit).
- **3 John is the second-shortest book in the NT** (15 verses, 1 chapter, ~219 Greek words — slightly shorter than 2 JN at ~245). It ships **the same day as 2 JN** and rides on the Johannine-letter locks 1 JN + 2 JN established. The translation is corpus-derivative on the Johannine-signature material (πρεσβύτερος self-designation, ἀλήθεια saturation, περιπατέω in-truth, μαρτυρέω witness-language, ἀγαπητέ direct-address) — the audit confirms compliance rather than introducing new locks for those.
- **3 JN is the most HAPAX-DENSE book in the NT.** 5 NT-hapaxes in 15 verses (one every three verses): **μειζοτέρος** (v.4 double-comparative), **φιλοπρωτεύω** (v.9 "love-to-be-first"), **Διοτρέφης** (v.9 proper noun), **φλυαρέω** (v.10 slander), **κάλαμος** (v.13 reed-pen). Each has a verse-level KD per RULES §5; verse-level handling is adequate (no corpus doc needed) — but the cluster-density itself merits a noting-summary (§5 below).
- **3 JN is the second of the two NT books with the `Ὁ πρεσβύτερος` self-designation** (the first being 2 JN 1:1). The 2 JN audit recommended a brief amendment to `poimen_episkopos_register_split_2026-05.md` (or to `pastoral_corpus_locks_2026-05.md`) for this Johannine-letter sub-case. 3 JN 1:1 ratifies the same construction; the amendment is now **fully overdue** (no further test cases — Revelation has no πρεσβύτερος-self-designation; the corpus closes here).
- **2 NEW corpus-doc lifts emerge from 3 JN-distinctive lemmas**:
  - **`hygiaino_sound_doctrine_2026-05.md` brief amendment** (§3) — 3 JN 1:2's literal-physical-health ὑγιαίνω is the ONLY NT occurrence outside the Pastoral metaphorical sound-doctrine usage. Documenting the 3JN sub-case closes the corpus.
  - **`propempo_missionary_sending_2026-05.md`** (§4) — first project-corpus surface of the technical-missionary-send-on-journey verb. 3 JN 1:6 + Pauline parallels (1 COR 16:6, 11; 2 COR 1:16; ROM 15:24; ACT 15:3; 20:38; 21:5; TIT 3:13; pos PHM 1:14 not-counted; some include also 3 JN 1:6 itself) form a tight Pauline-Johannine technical-vocabulary cluster.
- **4 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): (a) ὁ φιλοπρωτεύων → ผู้ที่ใฝ่หาความเป็นใหญ่ (v.9 hapax rendering); (b) ὑπολαμβάνω → สนับสนุน (v.8 — only NT support-sense occurrence); (c) φίλοι vs ἀδελφοί register-split at v.15 — เพื่อน vs พี่น้อง (the only Johannine-letter ἀσπασμός closing-formula using φίλοι rather than ἀδελφοί); (d) "the Name" absolute Christological reference at v.7 → เพื่อพระนาม (whether v.7 thai_summary should explicate "the Name = Christ's name" for typical readers).
- **1 item flagged DECIDE** (Ben choice needed before tagging): the **Diotrephes-conflict surfacing** at vv. 9–10. This is the same surfacing-strategy question as 2 JN items D + E (whether to add a thai_summary surfacing the historical-context for a passage whose bare imperative reads counter to modern Thai cultural expectations). The 3JN case is more interpretively-charged because it names a specific historical individual whose pattern of misconduct (slander + refusing-hospitality + blocking-others + excommunicating) has been read into modern church-conflict situations — a thai_summary disclaimer would help bound the application.
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πρεσβύτερος as Johannine self-designation (v.1) — **STABLE** (extends 2JN; ratifies the recommended `poimen_episkopos_register_split` amendment as fully overdue)

3 JN 1:1 opens with **Ὁ πρεσβύτερος** — the same definite-article + simple-form Johannine-self-designation as 2 JN 1:1. This is the SECOND and FINAL NT occurrence of this construction (Revelation has πρεσβύτεροι in the 24-elders heavenly-court sense, not as author-self-designation).

**Current rendering:** `ข้าพเจ้าผู้ปกครองคริสตจักร` ("I, the church-elder") — IDENTICAL to 2 JN 1:1.

The 1:1 KD names the corpus-link:

> πρεσβύτερος → ผู้ปกครองคริสตจักร corpus-lock (matches 2 JN 1:1; per pastoral_corpus_locks Johannine-letter 'the Elder' self-designation).

**Editorial assessment.** The 2 JN audit (item §1) recommended a brief amendment to `poimen_episkopos_register_split_2026-05.md` (or `pastoral_corpus_locks_2026-05.md`) noting the Johannine-letter sub-case: definite-article + simple-form `Ὁ πρεσβύτερος` (2 JN 1:1; 3 JN 1:1) → **ผู้ปกครองคริสตจักร** preserves the ecclesiastical-office register without committing to the patristic "John the Elder" identification question. That recommendation was explicitly to be done "before 3 JN ships." The amendment was NOT yet implemented when 3 JN shipped today; the verse-level KD continues to cite the 2 JN 1:1 as the locking precedent.

3 JN 1:1 is the FINAL test case for this construction. The amendment is now fully overdue — writing it closes the corpus rather than anticipating future tests.

**Recommend: STABLE → LOCKED transition** when the brief amendment is written. Single-author, ~30 minutes (the 2 JN audit already drafted the rationale).

---

## 2. ἐκκλησία in 3 JN (vv. 6, 9, 10) — **LOCKED ✓** (`ekklesia_2026-04.md`)

3 JN 1 contains THREE occurrences of ἐκκλησία in a 15-verse letter — unusually dense for so short a book. The three references span a single local congregation (Diotrephes's church, identifiably the same body throughout):

| Verse | Greek | Thai | Referent |
|---|---|---|---|
| 1:6 | οἳ ἐμαρτύρησάν σου τῇ ἀγάπῃ ἐνώπιον ἐκκλησίας | **ต่อหน้าคริสตจักร** | the brothers' destination church (could be Gaius's-or-John's local church) |
| 1:9 | Ἔγραψά τι τῇ ἐκκλησίᾳ | **ได้เขียนถึงคริสตจักร** | Diotrephes's local church |
| 1:10 | ἐκ τῆς ἐκκλησίας ἐκβάλλει | **ขับพวกเขาออกจากคริสตจักร** | same as v.9 (the church Diotrephes excommunicates from) |

All three render **คริสตจักร** uniformly per `ekklesia_2026-04.md`. The local-congregation referent across v.6 → v.9 → v.10 is preserved in the Thai with the same lexeme, allowing the reader to track the unfolding situation without confusion.

**Editorial assessment.** Compliance is exact. No interpretive surface-decision is forced — the same lexeme handles both "the brothers testified to a church" (v.6) and "Diotrephes refused/expelled from the church" (vv. 9–10). The Thai reader gets the local-congregation-referent thread cleanly.

**Recommend: LOCKED ✓.** No corpus-doc changes.

---

## 3. ὑγιαίνω at v.2 — literal-physical-health (NOT Pastoral 'sound-doctrine' metaphor) — **STABLE** (recommend brief amendment to `hygiaino_sound_doctrine_2026-05.md`)

3 JN 1:2 contains the only NT occurrence of ὑγιαίνω in the **literal-physical-health sense** (outside the Pastoral metaphorical "sound-doctrine" usage). The verse uses the Hellenistic-letter health-and-prosperity-wish formula:

> Ἀγαπητέ, περὶ πάντων εὔχομαί σε εὐοδοῦσθαι καὶ **ὑγιαίνειν**, καθὼς εὐοδοῦταί σου ἡ ψυχή.
> ท่านที่รัก ข้าพเจ้าอธิษฐานขอให้ท่านจำเริญในทุกสิ่ง และ**มีสุขภาพดี** เหมือนกับที่จิตวิญญาณของท่านก็จำเริญอยู่แล้ว

The 1:2 KD names the disambiguation:

> ὑγιαίνω here = literal-physical-health (NOT the Pastoral 'sound-doctrine' metaphorical sense at hygiaino_sound_doctrine_2026-05.md) → มีสุขภาพดี.

**Editorial assessment.** This is principled and corpus-aware. The Pastoral lock (`hygiaino_sound_doctrine_2026-05.md`) governs the metaphorical "sound-doctrine" sense at 1 TIM 1:10; 6:3; 2 TIM 1:13; 4:3; TIT 1:9, 13; 2:1, 2 — where ὑγιαίνω modifies διδασκαλία / λόγος / πίστις (teaching / word / faith). 3 JN 1:2 is the ONE place in the NT where ὑγιαίνω is used at face-value for human bodily-wellness. The Thai **มีสุขภาพดี** ("be in good health") is the obvious-and-correct natural-Thai rendering for this register. The corpus doc should record the disambiguation.

**Recommend: STABLE; brief amendment to `hygiaino_sound_doctrine_2026-05.md`** noting the 3 JN 1:2 literal-physical-health sub-case. One paragraph, ~10 minutes:

> **Disambiguation: 3 JN 1:2 literal-physical-health sense.** ὑγιαίνω at 3 JN 1:2 is the ONLY NT occurrence outside the Pastoral corpus and is the ONLY NT occurrence with literal-physical-health referent (the Hellenistic letter-opening health-wish formula `περὶ πάντων εὔχομαί σε εὐοδοῦσθαι καὶ ὑγιαίνειν`). Render → **มีสุขภาพดี** ("be in good health"). The metaphorical-doctrinal sense locked in this doc applies to all other NT occurrences (1 TIM, 2 TIM, TIT). This sub-case closes the lemma's NT corpus.

---

## 4. προπέμπω at v.6 — technical-missionary-sending vocabulary — **STABLE** (recommend new corpus doc `propempo_missionary_sending_2026-05.md`)

3 JN 1:6 introduces προπέμπω (literally "send-forward"), a NT-technical term for formal-mission-support of-traveling-preachers. This is the only Johannine occurrence; the rest of the corpus is Pauline + Lukan.

> οὓς καλῶς ποιήσεις **προπέμψας** ἀξίως τοῦ θεοῦ
> ท่านจะทำดีถ้าได้**ส่ง**พวกเขา**ไปต่อ**ในลักษณะที่สมควรแก่พระเจ้า

The 1:6 KD names the technical-NT cluster:

> προπέμπω → ส่ง ... ไป — preserves the 'send-forward-on-journey' sense (technical-NT-term for mission-support; cf. 1 COR 16:6, 11; 2 COR 1:16; ROM 15:24).

**Editorial assessment.** The Greek verb is used 9× in NT, almost all in mission-support contexts:
- ACT 15:3 (Antioch sends Paul + Barnabas to Jerusalem)
- ACT 20:38 (Ephesian elders escort Paul to the ship)
- ACT 21:5 (Tyre disciples escort Paul + family)
- ROM 15:24 (Paul asks Rome to send him onward to Spain)
- 1 COR 16:6, 11 (Corinth to send Paul / Timothy onward)
- 2 COR 1:16 (Corinth to send Paul to Judea)
- TIT 3:13 (Titus to send Zenas + Apollos onward)
- 3 JN 1:6 (Gaius to send the brothers onward)

The technical-sense is "provision-and-escort for the next leg of the missionary journey" — material support + actual physical accompaniment to the road. The Thai **ส่ง ... ไปต่อ** ("send ... onward") preserves the sense well. There is no current corpus doc.

**Recommend: STABLE → LOCKED** with new doc `docs/translator_decisions/propempo_missionary_sending_2026-05.md` documenting the technical-vocabulary cluster. Single-author, ~1 hour:

- Lemma: προπέμπω
- Lock: → **ส่ง ... ไปต่อ** (with directional + provision overtones)
- NT corpus map: ACT 15:3; 20:38; 21:5; ROM 15:24; 1 COR 16:6, 11; 2 COR 1:16; TIT 3:13; 3 JN 1:6
- Distinguishing notes: differs from generic ἀποστέλλω ("send" with no journey-provision sense) and ἐκπέμπω ("send-out," typically Acts narrator-frame for missionary-departure).

This corpus doc would be referenced retroactively by the Pauline-corpus chapters that already shipped — a low-risk lock-formalization (the Pauline KDs already render consistently per the verse-level rationales).

---

## 5. HAPAX cluster — five NT-hapaxes in 15 verses — **STABLE** (verse-level handling adequate; flag for §5 noting only)

3 JN 1 contains FIVE NT-hapax legomena, the highest-density of any NT book per verse-count:

| Verse | Greek hapax | Sense | Thai rendering |
|---|---|---|---|
| 1:4 | μειζοτέρος | "greater-er" (irregular Koine double-comparative of `μέγας`) | **ยิ่งใหญ่กว่า** ("greater than"; irregular morphology not preserved) |
| 1:9 | φιλοπρωτεύω | "love-to-be-first," ambition-for-primacy | **ใฝ่หาความเป็นใหญ่** ("seek-after greatness") |
| 1:9 | Διοτρέφης | proper noun (only-NT) | **ดิโอเตรเฟส** (Greek-form Thai-transliteration) |
| 1:10 | φλυαρέω | "talk-nonsense / babble against," slander | **ปรักปรำ** ("slander, accuse falsely") |
| 1:13 | κάλαμος | reed-pen (writing-instrument) | **ปากกา** ("pen") |

Each is flagged in the verse-level `notes` per RULES §5. Verse-level handling is adequate.

**Editorial assessment.** The cluster-density is the most striking lexical feature of 3 JN. Some observations:

1. **μειζοτέρος (v.4).** The double-comparative is irregular Koine — a "more-greater" construction that uses the comparative-suffix on an already-comparative root (μείζων + -ότερος). The Thai **ยิ่งใหญ่กว่า** drops the redundant-grammatical form (Thai can't morphologically encode a double-comparative naturally) but preserves the **superlative-emphasis** the construction was designed to convey. Principled.

2. **φιλοπρωτεύω (v.9).** Coined by John for the Diotrephes-context (no Greek-pagan-corpus parallels in TLG outside 3 JN dependence). The Thai **ใฝ่หาความเป็นใหญ่** captures the "seeking-primacy" sense; it is a Thai-corpus-hapax (no other Eremos rendering uses this phrase), matching the Greek-hapax. See §9 below for whether this is the right rendering.

3. **Διοτρέφης (v.9).** Proper-noun transliteration follows the Greek-form-Thai-transliteration pattern used for other lesser-known NT proper-nouns (e.g., Δημήτριος → เดเมตริอัส at v.12, Γάϊος → กายอัส at v.1). Standard.

4. **φλυαρέω (v.10).** Onomatopoeic-Greek "babble" verb. The Thai **ปรักปรำ** captures the slander-with-empty-words sense without preserving the babbling-sound onomatopoeia (Thai phonosemantic options would have been available — e.g., **พูดพล่าม / พูดเพ้อเจ้อ** "babble," but these are too neutral; **ปรักปรำ** carries the legal-accusatory weight that fits the context of "slandering us"). Principled.

5. **κάλαμος (v.13).** Standard Hellenistic-writing-tool. The Thai **ปากกา** ("pen") carries the modern-letter-writing-imagery cleanly without anachronism. The pair "**น้ำหมึก** + **ปากกา**" (ink + pen) at 3 JN 13 mirrors the 2 JN 1:12 pair "**กระดาษ** + **น้ำหมึก**" (paper + ink) — same letter-closing convention, different writing-tool foregrounded.

**Recommend: STABLE.** No corpus doc needed; verse-level notes carry each hapax. The cluster itself is worth flagging in the project README or a future "Johannine letter linguistic profile" note (low priority).

---

## 6. Diotrephes-conflict surfacing (vv. 9–10) — corrupt-church-leadership pattern — **DECIDE**

3 JN 1:9–10 names a specific historical individual (Diotrephes) and lists his fourfold misconduct in escalating order:

| Step | Greek | Thai | Modern-application risk |
|---|---|---|---|
| 1. Slander | λόγοις πονηροῖς **φλυαρῶν** ἡμᾶς | ใช้ถ้อยคำชั่วร้าย**ปรักปรำ**เรา | low (universal) |
| 2. Refusing hospitality | οὔτε αὐτὸς ἐπιδέχεται τοὺς ἀδελφοὺς | ไม่ยอมรับพี่น้อง | **medium** (parallel to 2 JN 10 — see 2JN audit items D+E) |
| 3. Blocking others | τοὺς βουλομένους **κωλύει** | **ห้าม**ผู้ที่ต้องการต้อนรับ | low |
| 4. Excommunication | ἐκ τῆς ἐκκλησίας **ἐκβάλλει** | ยัง**ขับ**พวกเขา**ออก**จากคริสตจักร | **high** (modern Thai church-discipline contexts) |

The verse `notes` at v.10 calls it out:

> Diotrephes's-fourfold-misconduct: slander + refusing-hospitality + blocking-others + excommunication. The pattern of-corrupt-church-leadership.

**Editorial assessment.** The Diotrephes-passage is unique in the NT — it names a specific contemporary church-leader as a negative-example. Modern Thai church-conflict contexts often pattern-match against this passage in either direction:

- **Misuse direction A:** A faction in conflict with their pastor labels him "ดิโอเตรเฟสในยุคปัจจุบัน" ("a present-day Diotrephes") to delegitimize his authority — using the passage as ad-hominem ammunition rather than as the disciplinary-template Scripture.
- **Misuse direction B:** A faction defends a controlling pastor by reading the passage as describing only-extreme-cases (excommunication in particular) and dismissing more-moderate concerns as not-rising-to-Diotrephes-level.

The bare-imperative Thai surface in 3 JN 9–10 doesn't bound either misuse. The interpretive context that:

1. The passage is APOSTOLIC, not congregational — John's authority to "call attention to" (ὑπομνήσω) is APOSTOLIC-personal, not a delegated church-discipline-tool;
2. The fourfold pattern as a CLUSTER (all four together, not just one), not any single behavior, is what marks Diotrephes as the negative example;
3. Modern application requires a structural-not-personal reading

— is invisible in the bare verse-text.

**Two surfacing options:**

**Option A (current).** Bare narrative; `notes` field carries the analysis; no thai_summary at v.9 or v.10.

**Option B (proposed).** Add a `thai_summary` at v.10 (the verse with the fourfold-pattern-listing) noting:

1. The fourfold cluster (slander + refusing-hospitality + blocking-others + excommunication) is what marks Diotrephes — not any single behavior in isolation.
2. John's "call to attention" is APOSTOLIC-personal authority, not a delegated congregational-discipline template.
3. Modern application: discernment about church-leadership conflict patterns; NOT a label-weapon for in-fighting.

**Editorial assessment of options.** Option B has higher upside than the parallel 2JN items D+E because:
- The Diotrephes-naming concrete-historicizes the passage in a way that 2 JN's anonymous "deceiver" doesn't — modern readers more naturally pattern-match Diotrephes onto contemporary individuals;
- The fourfold pattern is structurally specific (a leadership-discipline-checklist), and a thai_summary that names the cluster-as-cluster bounds misuse cleanly;
- The Pauline-historical-counterparts (2 TIM 1:15; 2:17–18; 3:1–9) where named-individuals (Phygelus, Hermogenes, Hymenaeus, Philetus, Jannes, Jambres) are flagged for misconduct DO get thai_summary-style historical-context surfacing in those chapters' shipped translations — a v.10 thai_summary here would harmonize the surfacing-strategy.

**DECIDE question for Ben.** Option A (status quo, no thai_summary at v.10) or Option B (add v.10 thai_summary surfacing the fourfold-pattern-as-cluster + apostolic-personal authority + modern-application boundary)? Lean toward Option B given the 3JN-distinctive concrete-historicizing of the passage. The cost is one paragraph; the upside is bounding the modern-Thai-church-conflict misuse vector.

This is **DECIDE** because the practical pastoral-implications of Option A's possible-misreading are significant in modern Thai church-conflict contexts. (It is NOT, however, a code/translation change — the main `thai` field at vv. 9–10 stays as-is regardless.)

---

## 7. φίλοι vs ἀδελφοί register-split (v.15) — friendship-language closing — **REVIEW**

3 JN 1:15 closes with the only Johannine-letter ἀσπασμός closing-formula using **φίλοι** ("friends") rather than **ἀδελφοί** ("brothers"):

> Εἰρήνη σοι. ἀσπάζονταί σε **οἱ φίλοι**. ἀσπάζου **τοὺς φίλους** κατ' ὄνομα.
> ขอสันติสุขจงมีแก่ท่าน **เพื่อนทั้งหลาย**ฝากความระลึกถึงท่าน ขอท่านฝากความระลึกถึง**เพื่อนทั้งหลาย**เป็นรายบุคคล

The 1:15 KD names the register-split:

> φίλοι → เพื่อน — preserves the friendship-language (distinct from ἀδελφοί 'brothers'; here-context = personal-circle of-John's-and-Gaius's mutual-acquaintance).

**Editorial assessment.** The register-distinction matters. The Johannine corpus elsewhere uses ἀδελφοί for Christian-fellowship in the abstract sense (e.g., 1 JN 3:13–18 ἀγαπώμεθα ἀλλήλους, ὁ μὴ ἀγαπῶν τὸν ἀδελφόν...). In 3 JN itself, ἀδελφοί appears at vv. 3, 5, 10 (the brothers who came / were testified about / Diotrephes refused). The closing-formula switch to φίλοι at v.15 is deliberate — these are Gaius's-and-John's mutual-friendship-circle, NOT the abstract-fellowship "brothers" referenced earlier in the letter.

The φίλοι usage echoes the Johannine-Last-Discourse:
- JHN 15:14 — ὑμεῖς φίλοι μού ἐστε
- JHN 15:15 — οὐκέτι λέγω ὑμᾶς δούλους ... ὑμᾶς δὲ εἴρηκα φίλους

— where φίλοι carries elevated theological-friendship-of-Christ register. The 3 JN 15 closing is more pedestrian (a personal-acquaintance circle, not a Christological-friendship-of-Christ statement) but the lexical-link to JHN 15:14–15 is real.

**The Thai distinction:** **เพื่อน** (friend) vs **พี่น้อง** (brother / Christian-sibling) is preserved cleanly. The Thai reader gets the personal-friendship-circle at v.15 distinct from the brothers-at-large referent at vv. 3, 5, 10.

**REVIEW question for Ben.** Is **เพื่อน** the right rendering, or would a more-specific construction (e.g., **เพื่อนสนิท** "close friend"; **มิตรสหาย** "comrade-friend" — Thai elevated-friendship register) better preserve the distinct-from-ἀδελφοί register, given that the bare **เพื่อน** can also mean a casual-everyday-friend in modern Thai? The current rendering is principled but possibly under-marked.

---

## 8. ὑπολαμβάνω → สนับสนุน (v.8) — only-NT support-sense — **REVIEW**

3 JN 1:8 contains the only NT use of ὑπολαμβάνω in the **support-sense** ("to-take-up-from-below," to support / sustain).

> ἡμεῖς οὖν ὀφείλομεν **ὑπολαμβάνειν** τοὺς τοιούτους, ἵνα συνεργοὶ γινώμεθα τῇ ἀληθείᾳ.
> เพราะฉะนั้น เราจึงต้อง**สนับสนุน**คนเช่นนี้ เพื่อเราจะได้เป็นผู้ร่วมงานกับความจริง

The 1:8 KD:

> ὑπολαμβάνω → สนับสนุน (support / take-up-from-below).

**Editorial assessment.** The verb ὑπολαμβάνω elsewhere in NT carries different senses:
- ACT 1:9 — "received him out of their sight" (the cloud takes-up Jesus at the ascension)
- LUK 7:43 — "I suppose / answer" (epistemic verb-of-saying in dialog)
- LUK 10:30 — "answering, said" (verb-of-saying in narrative)

The support-sense at 3 JN 1:8 is unique. The Thai **สนับสนุน** ("support, sponsor, back") carries the sense well — it's a standard Thai noun-verb for material-and-moral-backing, and is used elsewhere in modern Thai Christian discourse for missionary-support. **Compliant.**

**The principled question.** Is **สนับสนุน** distinct enough from related Greek-mission-vocabulary to preserve the lexical-distinctiveness? The question is whether the cross-corpus mapping is consistent:

| Greek | Sense | Eremos Thai |
|---|---|---|
| ὑπολαμβάνω (3JN 8) | support / take-up-from-below | **สนับสนุน** |
| προπέμπω (3JN 6) | send-forward-on-journey | **ส่ง ... ไปต่อ** |
| συνεργός (3JN 8) | fellow-worker | **ผู้ร่วมงาน** |
| διακονέω (Pauline) | serve / minister | locked separately |

The mappings are distinct. The 3JN 1:8 ὑπολαμβάνω + συνεργός pair (support → fellow-worker-status) is preserved cleanly.

**REVIEW question for Ben.** Is **สนับสนุน** the right rendering, or would a more contextually-specific construction (e.g., **อุปถัมภ์** "patronize, support" — more formal, mission-friendly; **ค้ำจุน** "uphold, sustain" — more literal "take-up-from-below") better preserve the under-the-load support imagery? Current rendering is principled but neutral.

---

## 9. ὁ φιλοπρωτεύων → ผู้ที่ใฝ่หาความเป็นใหญ่ (v.9) — Johannine-coined hapax — **REVIEW**

3 JN 1:9 contains the NT-hapax verb **φιλοπρωτεύω** ("love-to-be-first") substantivized as a present-participle:

> ὁ **φιλοπρωτεύων** αὐτῶν Διοτρέφης οὐκ ἐπιδέχεται ἡμᾶς
> ดิโอเตรเฟส **ผู้ที่ใฝ่หาความเป็นใหญ่**ในหมู่พวกเขา ไม่ยอมรับเรา

The 1:9 KD:

> φιλοπρωτεύω (only here NT, 'love-to-be-first') → ใฝ่หาความเป็นใหญ่ — preserves the ambition-for-primacy sense.

**Editorial assessment.** The Greek is a compound: φιλο- ("love") + πρωτεύω ("to-be-first"). Patristic Greek has scattered later occurrences (always likely under 3 JN dependence). Modern English translations vary:
- ESV / NIV: "who likes to put himself first" / "who loves to be first"
- NLT: "who loves to be the leader"
- CSB: "who likes to be in charge of everything"
- NASB: "who loves to be first among them"

Thai versions vary similarly:
- THSV: **ผู้อยากเป็นใหญ่** ("the-one-wanting-to-be-great")
- THKJV: **ที่ใคร่จะเป็นใหญ่** ("who-desires-to-be-great")
- a Thai NLT-equivalent: **ผู้ชอบเป็นใหญ่** ("who-likes-to-be-great")

**The current rendering: ใฝ่หาความเป็นใหญ่** ("seek-pursue greatness/primacy") — uses **ใฝ่หา** ("aspire-after, seek") which is stronger and more agentive than the **อยาก / ใคร่ / ชอบ** ("want / desire / like") Thai modal verbs the other versions use. This is principled — φιλο- is not a passive-want but an active-loving-pursuit.

**The trade-off:** **ใฝ่หา** is somewhat literary-register (less common in everyday Thai) and may sound elevated in a way that mismatches the personal-pastoral letter register of 3 JN. The other Thai versions opt for more colloquial Thai.

**REVIEW question for Ben.** Is **ใฝ่หาความเป็นใหญ่** the right rendering for the rest-of-corpus consistency, or should it match the THSV **อยากเป็นใหญ่** for cross-Bible Thai-readability? The choice is principled either way; the current rendering preserves the active-pursuit nuance at some cost in everyday-register accessibility.

---

## 10. "the Name" absolute Christological reference (v.7) — **REVIEW**

3 JN 1:7 contains the absolute-form `ὑπὲρ τοῦ ὀνόματος` ("on-behalf-of THE NAME"), where "the Name" is shorthand for "the name of Christ" without explicit complement:

> **ὑπὲρ γὰρ τοῦ ὀνόματος** ἐξῆλθον μηδὲν λαμβάνοντες ἀπὸ τῶν ἐθνικῶν
> เพราะพวกเขาออกไป**เพื่อพระนาม** ไม่ได้รับสิ่งใดจากคนต่างชาติ

The 1:7 KD:

> 'the Name' absolute-form = the-name-of-Christ → พระนาม (royal-prefix divine-name). Echoes ACT 5:41 'suffer-for-the-Name' — same absolute-Christological-Name usage.

**Editorial assessment.** The absolute-Name idiom recurs in:
- ACT 5:41 — χαίροντες ... ἠτιμάσθησαν ὑπὲρ τοῦ ὀνόματος ("rejoicing they were dishonored on-behalf-of-the-Name")
- ACT 9:16 — ὑπὲρ τοῦ ὀνόματός μου (Christ to Ananias about Paul)
- ACT 15:26 — ὑπὲρ τοῦ ὀνόματος τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ (with explicit complement)
- 3 JN 1:7 — ὑπὲρ ... τοῦ ὀνόματος (absolute, like ACT 5:41)

The Thai **เพื่อพระนาม** (royal-pระ + name) preserves the absolute-form without forcing an explicit complement. **Compliant** with the ACT 5:41 corpus-precedent.

**The interpretive surface:** A typical Thai reader encountering **เพื่อพระนาม** without context may not immediately decode "the Name" = Christ's name (the Thai royal-prefix พระ does mark divine-status, so the divine-name reading is preserved, but the specific Christological identification is implicit). The 3 JN 7 verse `notes` carries the analysis but is invisible to typical readers.

**REVIEW question for Ben.** Should v.7 receive a `thai_summary` (currently null) explicating "พระนาม คือ พระนามของพระคริสต์" ("the Name = the name of Christ") — making the absolute-Name → Christ identification explicit for the typical reader? Or is the royal-prefix + ACT 5:41-corpus-link sufficient lexical-marking?

---

## 11. Verse 14/15 textual numbering convention — **STABLE** (note only)

3 JN closes with what is variably numbered as 14a/14b vs 14/15 across editions:

| Numbering | Greek | Thai |
|---|---|---|
| **SBLGNT v.14** (Eremos follows) | ἐλπίζω δὲ εὐθέως σε ἰδεῖν, καὶ στόμα πρὸς στόμα λαλήσομεν | (1:14) |
| **SBLGNT v.15** (Eremos follows) | Εἰρήνη σοι. ἀσπάζονταί σε οἱ φίλοι. ἀσπάζου τοὺς φίλους κατ' ὄνομα | (1:15) |
| Older editions (KJV/Byzantine) | combine into a single verse 14 | — |

Eremos correctly follows SBLGNT (15-verse numbering) per RULES §0. The translation has 15 verse-entries, matching the SBLGNT structure. No inclusion-variant question arises (this is a modern-numbering convention, not a textual-omission issue).

**Recommend: STABLE.** No change needed.

---

## 12. Inherited Johannine + Pastoral + general locks — **all compliant**

| Lock | 3 JN evidence | Status |
|---|---|---|
| πρεσβύτερος → ผู้ปกครองคริสตจักร (`pastoral_corpus_locks_2026-05.md`) — Johannine-letter sub-case | v.1 → **ข้าพเจ้าผู้ปกครองคริสตจักร**. See §1 above. | **STABLE** (recommended amendment overdue) |
| ἀλήθεια → ความจริง (Johannine truth-saturation) | vv. 1, 3 (×2), 4, 8, 12 → **ความจริง** uniform. Five occurrences in fifteen verses (33% density). Compliant with 1 JN + 2 JN. | **LOCKED** (extends 1JN/2JN) |
| περιπατέω → ดำเนิน (walk-in-truth Johannine ethic) | vv. 3, 4 → **ดำเนิน** uniform. Compliant with 2 JN 4 + 1 JN 1:6, 7; 2:6, 11. | **LOCKED** (corpus precedent) |
| ἀγαπητέ → ที่รัก (direct address) | vv. 1, 2, 5, 11 → **ที่รัก / ท่านที่รัก** uniform. Compliant with 1 JN 2:7; 3:2, 21; 4:1, 7, 11. | **LOCKED** (corpus precedent) |
| μαρτυρέω family → เป็นพยาน / คำพยาน | vv. 3, 6, 12 (×2) — verbs and nouns uniform. The v.12 "our-testimony-is-true" Johannine-signature (cf. JHN 19:35; 21:24) preserved. | **LOCKED** (corpus precedent) |
| ἐκκλησία → คริสตจักร (`ekklesia_2026-04.md`) | vv. 6, 9, 10 → **คริสตจักร** uniform. See §2 above. | **LOCKED** ✓ |
| ἐθνικός → คนต่างชาติ (`ethnos_2026-04.md`) | v.7 → **คนต่างชาติ**. Compliant. | **LOCKED** ✓ |
| ψυχή → จิตวิญญาณ (`psyche_vs_pneuma_anthropological_2026-04.md`) | v.2 → **จิตวิญญาณ**. Compliant. | **LOCKED** ✓ |
| πατήρ register (`narrator_vs_character_voice_2026-04.md`) | **N/A** in 3 JN — no πατήρ occurrence. | **LOCKED (N/A)** |
| Royal-prefix proper-nouns (Διοτρέφης, Δημήτριος, Γάϊος) | v.1 → **กายอัส**; v.9 → **ดิโอเตรเฟส**; v.12 → **เดเมตริอัส**. Standard Greek-form Thai-transliteration. Γάϊος matches ROM 16:23, 1 COR 1:14, ACT 19:29, 20:4 (possibly same individual). | **STABLE** (corpus precedent) |
| ξένος → คนแปลกหน้า (stranger / host-context) | v.5 → **คนแปลกหน้า**. Compliant with MAT 25:35, EPH 2:19. | **STABLE** (corpus precedent) |
| πιστὸν ποιεῖς → ทำสิ่งที่สัตย์ซื่อ (act-faithfully idiom) | v.5 → **ทำสิ่งที่สัตย์ซื่อ**. πιστός → สัตย์ซื่อ corpus-locked. | **LOCKED** (corpus precedent) |
| συνεργός → ผู้ร่วมงาน (Pauline-corpus precedent) | v.8 → **ผู้ร่วมงาน**. Compliant with ROM 16:3, 9, 21; 1 COR 3:9; PHL 2:25; etc. | **LOCKED** (corpus precedent) |
| μιμέομαι → เลียนแบบ | v.11 → **เลียนแบบ**. Compliant with HEB 13:7. | **LOCKED** (corpus precedent) |
| ἀγαθοποιέω + κακοποιέω → ทำดี + ทำชั่ว | v.11 → **ทำดี + ทำชั่ว**. Compliant. | **STABLE** (corpus precedent) |
| 'οὐχ ἑώρακεν τὸν θεόν' Johannine spiritual-perception | v.11 → **ไม่ได้เห็นพระเจ้าเลย**. Compliant with 1 JN 3:6; 4:20. | **STABLE** (extends 1JN) |
| εἰρήνη → สันติสุข | v.15 → **สันติสุข**. Compliant. | **LOCKED** (corpus precedent) |
| 'στόμα πρὸς στόμα' Hebraic face-to-face idiom | v.14 → **ต่อหน้ากัน**. Compliant with 2 JN 1:12 (cf. NUM 12:8 LXX). | **STABLE** (extends 2JN) |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** in 3 JN — no SBLGNT-omits-mainstream-includes variants; the v.14/v.15 numbering split is a modern-edition convention, not a textual-omission. See §11 above. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 3 JN is a personal-pastoral letter, not narrative. | **LOCKED (N/A)** |
| Vocative kyrie / didaskale register | N/A — no vocative κύριε in 3 JN. | **LOCKED (N/A)** |
| OT citations (`data/nt_ot_citations.json`) | **None** in 3 JN — no formal OT citations. | **LOCKED (N/A)** |
| Triple-greeting formula (Pastoral-Johannine) | N/A — 3 JN opens with `ὁ πρεσβύτερος Γαΐῳ τῷ ἀγαπητῷ` (no χάρις/ἔλεος/εἰρήνη triple). | **LOCKED (N/A)** |
| ἀντίχριστος (1JN-locking-precedent) | N/A — no ἀντίχριστος occurrence in 3 JN. | **LOCKED (N/A)** |
| πεπληρωμένη-of-joy phrase-lock | N/A — 3 JN uses ἐχάρην λίαν / οὐκ ἔχω χαρά, not the πεπληρωμένη-of-joy formula (which is JHN/1JN/2JN-specific). | **LOCKED (N/A)** |

---

## Mechanical (§1) — **all green**

- 1/1 chapter: `output/check_reports/3john_01_review.md` ✓
- 1/1 chapter: `output/back_translations/3john_01.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-227-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only unrelated paratext exports + 1JN textual_variants file from earlier audit; no 3 JN source-file dirt

---

## Pre-existing docs affirmed / unchanged

All 47 docs in `docs/translator_decisions/` are unchanged by 3 JN. The audit confirms compliance with the Johannine + Pastoral + Pauline + general locks. The 1JN/2JN audit recommendation list remains valid; 3 JN ratifies three of those recommendations as fully overdue:

1. **Brief amendment to `poimen_episkopos_register_split_2026-05.md`** (or `pastoral_corpus_locks_2026-05.md`) for the Johannine-letter `Ὁ πρεσβύτερος` self-designation sub-case (§1) — RATIFIED by 3 JN 1:1 as the FINAL test case.
2. **`docs/translator_decisions/agape_johannine_2026-05.md`** (1JN audit §1) — RATIFIED but slightly less compelling for 3 JN since 3 JN ἀγάπη occurrences are sparse (only v.6 — "your love, before the church") compared to 1 JN's saturation.
3. **`docs/translator_decisions/antichristos_johannine_2026-05.md`** (1JN/2JN audits) — N/A in 3 JN (no occurrence) but still overdue from 2JN audit's recommendation.

3 JN-distinctive new corpus-doc recommendations:

1. **Brief amendment to `hygiaino_sound_doctrine_2026-05.md`** (§3) — adds the 3 JN 1:2 literal-physical-health sub-case, closing the lemma's NT corpus.
2. **NEW `docs/translator_decisions/propempo_missionary_sending_2026-05.md`** (§4) — locks the technical-missionary-send-on-journey verb across the Pauline + Lukan + Johannine corpus.

---

## Flagged for Ben's attention

### A. Brief amendment for Johannine-letter `Ὁ πρεσβύτερος` self-designation — **STABLE → LOCKED transition** (§1)
2 JN audit recommended; 3 JN 1:1 ratifies as FINAL test case. Add sub-section to `poimen_episkopos_register_split_2026-05.md` (or `pastoral_corpus_locks_2026-05.md`). Single-author, ~30 minutes.

### B. Brief amendment to `hygiaino_sound_doctrine_2026-05.md` — **STABLE → LOCKED transition** (§3)
3 JN 1:2 is the ONLY NT literal-physical-health occurrence. Documenting closes the corpus. Single-author, ~10 minutes.

### C. New corpus doc `propempo_missionary_sending_2026-05.md` — **STABLE → LOCKED transition** (§4)
First project-corpus surface of the technical-missionary-send-on-journey verb. Compounds Pauline + Lukan + Johannine attestations. Single-author, ~1 hour.

### D. Diotrephes-conflict surfacing at vv. 9–10 — **DECIDE** (§6)
Stay with bare narrative (Option A) or add v.10 thai_summary surfacing the fourfold-pattern-as-cluster + apostolic-personal authority + modern-application boundary (Option B)? Lean toward Option B given the concrete-historicizing of the passage and the Thai church-conflict misuse vector.

### E. φίλοι vs ἀδελφοί register at v.15 — **REVIEW** (§7)
**เพื่อน** is principled but possibly under-marked. Should it be elevated to **เพื่อนสนิท / มิตรสหาย** for clearer register-distinction from ἀδελφοί ("brothers" → พี่น้อง) elsewhere in the letter?

### F. ὑπολาμβάνω → สนับสนุน at v.8 — **REVIEW** (§8)
Current rendering is principled but neutral. Alternatives (**อุปถัมภ์** patronize / **ค้ำจุน** uphold-from-below) might preserve the under-the-load support imagery better. Defensible to keep as-is.

### G. ὁ φιλοπρωτεύων → ผู้ที่ใฝ่หาความเป็นใหญ่ at v.9 — **REVIEW** (§9)
**ใฝ่หาความเป็นใหญ่** is more active-pursuit than THSV's **อยากเป็นใหญ่**. Defensible either way; current rendering preserves the φιλο- "active-loving-pursuit" force.

### H. "the Name" absolute Christological reference at v.7 — **REVIEW** (§10)
Should v.7 receive a `thai_summary` explicating พระนาม = พระนามของพระคริสต์, or is the royal-prefix + ACT 5:41-corpus-link sufficient?

### I. New corpus-doc lifts (in priority order)
1. **Brief amendment to `poimen_episkopos_register_split_2026-05.md`** (§1) — write FIRST; final NT test case for the Johannine-letter `Ὁ πρεσβύτερος` self-designation sub-case
2. **Brief amendment to `hygiaino_sound_doctrine_2026-05.md`** (§3) — small, closes the lemma's NT corpus
3. **NEW `propempo_missionary_sending_2026-05.md`** (§4) — Pauline + Lukan + Johannine technical cluster

(All three can be batched into a single `docs/translator_decisions/` PR after Ben's confirmation.)

### J. External AI review (§3 of checklist) — **pending**
Recommended before `book-3john-v1` tag. Suggested 2-cluster external AI packet:
1. **3 JN 1–8** — opening + Hellenistic health-wish + walking-in-truth + Gaius's-faithfulness + προπέμπω missionary-support
2. **3 JN 9–15** — Diotrephes-conflict + imitation imperative + Demetrius-recommendation + closing letter-materials + φίλοι closing

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/1TH/1JN/2JN pattern. Foreground items D (Diotrephes surfacing), E (φίλοι), G (φιλοπρωτεύω) — the rest of 3 JN is corpus-derivative and well-locked.

---

## Recommendation

**3 John ships in strong corpus-hygiene shape.** The translator made principled choices on the few 3JN-distinctive items (the five-hapax cluster handled per RULES §5, the προπέμπω technical vocabulary, the φίλοι register-split, the πιστὸν ποιεῖς idiom). 3 JN serves principally as a RATIFICATION of the Johannine-letter locks 1 JN + 2 JN established yesterday, plus two small corpus-doc lifts that 3 JN's distinctive vocabulary closes (ὑγιαίνω literal-health sub-case; προπέμπω technical missionary-vocabulary).

The single DECIDE item (D — Diotrephes surfacing) is a thai_summary addition that does NOT touch the main `thai` field — so it does not strictly block the v1 tag if Ben prefers Option A.

Tag `book-3john-v1` after:
1. Ben's decision on **D** (Diotrephes-conflict surfacing — Option A bare or Option B thai_summary); resolves either way without code/translation change
2. Ben's confirmation on **E, F, G, H** (REVIEW items)
3. **Items A + B + C** (the three new corpus-doc lifts) — total ~2 hours; can be batched into one `docs/translator_decisions/` PR
4. External AI sanity-check (§J) via Grok / ChatGPT / Gemini

The Johannine catholic letters now close with 3 JN. Revelation is downstream and inherits the now-fully-ratified Johannine-letter lock-set. The audit confirms 3 JN is the SECOND test-case for the `Ὁ πρεσβύτερος` self-designation (closes the corpus); for ὑγιαίνω literal-health (closes the corpus); for προπέμπω technical-missionary-vocabulary (locks the cross-corpus cluster).
