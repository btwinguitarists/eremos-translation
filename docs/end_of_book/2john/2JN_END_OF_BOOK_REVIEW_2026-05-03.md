# 2 John — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 1 chapter (13 verses; 21 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (47 docs).
**Trigger:** 2JN 1 shipped (commit `7ca2f8b`); per `docs/END_OF_BOOK_CHECKLIST.md`. (2JN is single-chapter; the chapter and the book are coterminous.)
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **8 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 1/1 chapter has a green per-chapter `*_review.md` report + back-translation; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-226-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows no 2JN source-file dirt (only unrelated paratext exports + a 1JN textual_variants file from the prior 1JN audit).
- **2 John is the SHORTEST book in the NT** (13 verses, 1 chapter, ~245 Greek words). It ships **the day after 1 JN** and rides almost entirely on the Johannine-corpus locks 1 JN established yesterday (πρεσβύτερος register, ἀντίχριστος, ἀγάπη/ἀλήθεια thread, ἐντολή royal-prefix, μένω as Johannine-keyword, ἀπ' ἀρχῆς-formula, πεπληρωμένη-of-joy phrase-lock). The translation is unusually corpus-derivative: of 21 verse-level `key_decisions`, 16 are direct verbatim corpus-internal-link citations (1 JN parallels) — the audit confirms compliance rather than introducing new editorial questions.
- **2 JN is the FIRST shipped book to test the 1JN-recommended corpus-doc lifts**: the 1 JN audit recommended a new `antichristos_johannine_2026-05.md` doc *before 2 JN ships*; that recommendation was not yet acted on at the moment of this 2JN ship. The verse-level KD at 2JN 7 cites 1 JN 2:18, 22; 4:3 as the locking precedent — the rendering is consistent — but the corpus-doc remains undocumented. Recommend prioritizing the lift NOW since 2 JN's evidence base ratifies the 1JN locking precedent and the third-and-fourth Johannine catholic letters (3 JN, no occurrence; Revelation, no occurrence) have no further test cases.
- **2 NEW Johannine-letter cross-cutting items emerge** that 1JN did not surface: (a) **πρεσβύτερος as Johannine-self-designation** ("THE elder," definite-article + simple-form, distinct from the ecclesiastical-office sense of the Pastorals + 1 Pet 5:1 συμπρεσβύτερος); (b) **ἐρχόμενον ἐν σαρκί** (present-participle vs 1JN 4:2's perfect-participle ἐληλυθότα) — anti-Docetic content but with a different aspectual shape that some readings construe as future-coming rather than ongoing-incarnated-state.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): (a) the `ἐκλεκτῇ κυρίᾳ` + `ἀδελφῆς ἐκλεκτῆς` chosen-lady interpretive surface (thai_summary commits to personified-church reading; main field is neutral); (b) προάγω → ก้าวล้ำเกินเลย at v.9 (going-beyond-bounds metaphor); (c) χάρτης + μέλαν NT-hapax at v.12.
- **2 items flagged DECIDE** (Ben choice needed before tagging): (a) `μὴ λαμβάνετε αὐτὸν εἰς οἰκίαν` at v.10 — house-church platform-refusal vs private-home hospitality-refusal (the current Thai เข้ามาในบ้าน is lexically neutral but is liable to be read as a blanket prohibition on hospitality, which would clash with love-of-enemies elsewhere); (b) `χαίρειν αὐτῷ μὴ λέγετε` at v.10-11 — whether the bare imperative needs a `thai_summary` clarifying the doctrinal-endorsement context.
- **0 items flagged DECIDE that block the v1 tag for purely-2JN reasons** — both DECIDE items above are surfacing-strategy questions (whether to add a `thai_summary` or footer note clarifying interpretation), not lemma-rendering questions. They can be addressed via low-cost surfacing edits without touching the main `thai` field.
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πρεσβύτερος as Johannine self-designation (v.1, v.13 implied) — **STABLE (extends Pastoral lock; recommend brief amendment to `pastoral_corpus_locks_2026-05.md` §G or `poimen_episkopos_register_split_2026-05.md`)**

2 JN 1:1 opens with **Ὁ πρεσβύτερος** (definite article + simple-form noun) — the famous "the Elder" Johannine-self-designation that echoes 3 JN 1:1 + the early-patristic-tradition (Papias, Irenaeus) of "John the Elder." The Greek form is bare: no article-with-author-name (contra Pauline Παῦλος ἀπόστολος); no qualifying genitive; no ecclesiastical-office descriptor.

**Current rendering:** `ข้าพเจ้าผู้ปกครองคริสตจักร` ("I, the church-elder").

The 1:1 KD names the principle:

> πρεσβύτερος → ผู้ปกครองคริสตจักร corpus-lock per pastoral_corpus_locks (ecclesiastical-office sense). NB: distinct from γενέσθαι-Petrine 'fellow-elder' (1 PET 5:1 συμπρεσβύτερος → ผู้ปกครองคริสตจักรเพื่อนร่วมงาน). The Johannine 'the elder' (definite-article + simple-form) signals the senior-apostolic-pastoral identity.

**Editorial assessment.** **ผู้ปกครองคริสตจักร** is consistent with the locked Pastoral-corpus rendering (`pastoral_corpus_locks_2026-05.md` referenced from `poimen_episkopos_register_split_2026-05.md`) and the 1 Pet 5:1 πρεσβύτερος rendering. The single-word Greek `Ὁ πρεσβύτερος` has THREE possible interpretive layers in Johannine usage that the Thai rendering necessarily commits on:

1. **Ecclesiastical-office "elder"** (the rendering chosen) — places John-the-Elder in a recognized congregational-leadership category. This is the safe, corpus-consistent choice.
2. **Senior-apostolic identity** — "the elder" as a senior-apostolic-personal title (distinct from local church elder), reflecting John's late-life authority. The Thai **ข้าพเจ้าผู้ปกครองคริสตจักร** does not explicitly carry this senior-apostolic flavor (a Thai reader hears "I, a church-elder," not "I, *the* Elder").
3. **A specific known figure called "John the Elder"** (Papias's Ἰωάννης ὁ πρεσβύτερος) — distinct from John the Apostle in some early-patristic sources. The Thai translation correctly does NOT commit to this controversial identification (none of the Thai or English mainstream Bibles do).

The 1JN audit did NOT surface this question because 1 JN has no πρεσβύτερος-self-designation (1 JN 1:1 opens with the impersonal `ὃ ἦν ἀπ' ἀρχῆς`). 2 JN + 3 JN are the only two NT books where this self-designation occurs.

**Recommend: STABLE; consider brief amendment** to `poimen_episkopos_register_split_2026-05.md` (or to a new mini-doc `presbyteros_johannine_self_designation_2026-05.md`) noting the Johannine-letter sub-case: definite-article + simple-form `Ὁ πρεσβύτερος` (2 JN 1:1; 3 JN 1:1) → **ข้าพเจ้าผู้ปกครองคริสตจักร** preserves the ecclesiastical-office register without commitment to the "John the Elder" patristic-identification question. Forward applicability: 3 JN 1:1 (where the same construction recurs).

---

## 2. ἀντίχριστος (v.7) — **LOCKED ✓** (1JN-locking-precedent ratified) **/ corpus-doc lift overdue**

2 JN 1:7 contains the second Johannine-letter occurrence of ἀντίχριστος (after 1 JN 2:18 ×2; 2:22; 4:3). The 1 JN audit recommended creating `docs/translator_decisions/antichristos_johannine_2026-05.md` "BEFORE 2 JN ships." That recommendation was not yet implemented when 2 JN shipped today; the verse-level KD continues to cite 1 JN as the locking precedent.

| Verse | Greek | Thai |
|---|---|---|
| 2 JN 7 | οὗτός ἐστιν ὁ πλάνος καὶ ὁ ἀντίχριστος | **ผู้นั้นแหละคือคนล่อลวงและผู้ต่อต้านพระคริสต์** |

The 1:7 KD cites the Johannine corpus-precedent:

> ἀντίχριστος → ผู้ต่อต้านพระคริสต์ (matches 1 JN 2:18, 22; 4:3). The deceiver-anti-Christ identification.

**Editorial assessment.** Compliance is exact with the 1 JN 5-occurrence precedent. The 2 JN 7 construction is interesting because it's the ONLY NT verse where ἀντίχριστος is paired paratactically with **ὁ πλάνος** ("the deceiver") via καί — yielding a deceiver-AND-antichrist composite-identification. The Thai parataxis **คนล่อลวงและผู้ต่อต้านพระคริสต์** preserves this pairing naturally.

**Recommend: LOCKED ✓ ratified**; flag the **already-recommended-but-not-yet-written** `docs/translator_decisions/antichristos_johannine_2026-05.md` as **overdue** — 2 JN 7 is the FINAL test case for this lemma in the NT (no further occurrences in 3 JN or Revelation; Revelation uses different lexis: ψευδοπροφήτης, θηρίον). Writing the doc now will close out the corpus rather than anticipating future tests.

---

## 3. Ἰησοῦν Χριστὸν ἐρχόμενον ἐν σαρκί (v.7) — present-participle anti-Docetic confession — **REVIEW**

2 JN 1:7 contains the present-participle `ἐρχόμενον ἐν σαρκί` ("coming-in-flesh"), DISTINCT from 1 JN 4:2's perfect-participle `ἐν σαρκὶ ἐληλυθότα` ("having-come-in-flesh"). Both are anti-Docetic confessions, but the aspectual difference is interpretively nontrivial.

| Verse | Greek | Aspect | Thai |
|---|---|---|---|
| 1 JN 4:2 | ὁμολογεῖ Ἰησοῦν Χριστὸν ἐν σαρκὶ **ἐληλυθότα** | perfect (completed-incarnation, ongoing-state) | **ที่สารภาพรับว่าพระเยซูคริสต์ได้เสด็จมาในเนื้อหนัง** |
| 2 JN 1:7 | ὁμολογοῦντες Ἰησοῦν Χριστὸν **ἐρχόμενον** ἐν σαρκί | present (ongoing OR future-coming) | **สารภาพรับว่าพระเยซูคริสต์เสด็จมาในเนื้อหนัง** |

The 1:7 KD names the interpretive question:

> 'Ἰησοῦν Χριστὸν ἐρχόμενον ἐν σαρκί' — present-participle (NOT perfect — distinct from 1 JN 4:2 ἐληλυθότα). Per scholarly debate: the present-participle may emphasize the ongoing-incarnated-state, OR the future-coming. Render preserves the simple 'เสด็จมาในเนื้อหนัง' (came-in-flesh, royal-prefix) — same anti-Docetic content as 1 JN 4:2.

**Editorial assessment.** The Thai **เสด็จมาในเนื้อหนัง** (royal-เสด็จ + simple aspect) is **identical** to the 1 JN 4:2 rendering (which used **ได้เสด็จมาในเนื้อหนัง** with the perfective marker ได้). The 2 JN rendering elects to **drop the ได้** auxiliary, producing a more aspectually-neutral Thai surface. This is principled (Thai has no morphologically-encoded perfect-participle, and forcing ได้ here would over-commit to "have-already-come" reading at the cost of preserving the present-participle ambiguity).

**The interpretive question:** Three scholarly readings of the present-participle:

1. **Ongoing-incarnated-state** (the majority view + the rendering choice): present-participle = "the one who comes-and-remains-in-flesh," anti-Docetic confession of the still-incarnated Christ. This matches the 1 JN 4:2 ἐληλυθότα content and treats the aspect-shift as stylistic-Johannine variation.
2. **Future-coming** (a minority view): present-participle as future-marking ("the one who will-come in flesh") — referring to the parousia, anti-Docetic in a different way (the *returning* Christ also-comes-in-flesh, not as a phantom).
3. **Iterative/timeless confession** (a contextual reading): present-participle as confession-of-the-ongoing-truth — the act-of-confessing tracks an ongoing Christological reality.

The current rendering **เสด็จมาในเนื้อหนัง** is compatible with all three readings (Thai has no morphological future-marking either) — but a Thai reader's *default reading* will be reading 1 (past-completed event still-relevant). Reading 2 (future) is essentially invisible without a thai_summary or footer note.

**REVIEW question for Ben.** Should the 2 JN 1:7 verse get a `thai_summary` (currently null) noting the present-vs-perfect aspectual difference and the future-coming interpretive minority view? OR is the current "preserve the simple Thai surface, let the verse-level note carry the aspectual nuance" strategy sufficient for the project's evangelical-Protestant default audience?

---

## 4. ἐκλεκτῇ κυρίᾳ + ἀδελφῆς ἐκλεκτῆς (v.1, v.13) — chosen-lady interpretive surface — **REVIEW**

The two readings of ἐκλεκτῇ κυρίᾳ are well known: (a) a literal individual woman + her literal children; (b) a personified-church + her members. 2 JN's interpretive surface needs to handle the v.13 closing **τὰ τέκνα τῆς ἀδελφῆς σου τῆς ἐκλεκτῆς** ("the children of your elect sister") in lockstep with v.1.

| Verse | Greek | Thai |
|---|---|---|
| 1:1 | ἐκλεκτῇ κυρίᾳ καὶ τοῖς τέκνοις αὐτῆς | **ถึงสตรีที่ทรงเลือกสรรและบุตรของนาง** |
| 1:13 | τὰ τέκνα τῆς ἀδελφῆς σου τῆς ἐκλεκτῆς | **บุตรของน้องสาวของท่านที่ทรงเลือกสรร** |

The v.1 thai_summary commits explicitly:

> 'สตรีที่ทรงเลือกสรร' (ἐκλεκτῇ κυρίᾳ) มีการตีความ 2 แบบ — (1) หมายถึงสตรีจริง ๆ ที่มีศรัทธา และเด็กของนาง (2) หมายถึงคริสตจักรท้องถิ่นและสมาชิก (เป็นภาพเปรียบเทียบ — 'สตรี' และ 'บุตร' คือคริสตจักรและสมาชิก) นักวิชาการสมัยใหม่ส่วนใหญ่เลือกการตีความที่ 2 เนื่องจาก — (ก) ข้อ 13 'บุตรของน้องสาวของท่านที่ทรงเลือกสรร' น่าจะหมายถึงคริสตจักรอีกแห่ง (ข) ในข้อ 8 และ 10 สรรพนามเปลี่ยนเป็นรูปพหูพจน์ 'พวกท่าน' ซึ่งบ่งชี้ว่าผู้รับเป็นกลุ่มมากกว่าบุคคลเดียว

The 1:13 KD echoes:

> 'ἀδελφῆς σου τῆς ἐκλεκτῆς' → น้องสาวของท่านที่ทรงเลือกสรร — confirms the v.1 personification-reading (sister-church-sending-greetings), per the scholarly consensus.

**Editorial assessment.** The MAIN `thai` field at both v.1 and v.13 reads **literally** (as an actual woman + her actual sister + their actual children) — only the thai_summary surfaces the personified-church interpretation. This is a principled "main-field-neutral, summary-surfaces-interpretation" strategy. The thai_summary explicitly uses **เป็นภาพเปรียบเทียบ** ("metaphor") to flag the second reading.

**The principled question is:** does the v.13 KD's claim that the sister-church reading is "confirmed" go further than the v.1 thai_summary's "นักวิชาการสมัยใหม่ส่วนใหญ่เลือกการตีความที่ 2" ("most modern scholars choose interpretation 2") warrants? The v.13 KD treats interpretation 2 as the project's committed-position; the v.1 thai_summary treats it as one-of-two-options. There is a small internal-tension here.

**Reading-level ambiguity preservation** (per `petrine_eschatological_disambiguation_2026-05.md`'s "preserve-ambiguity" principle, extended in 1JN audit to soteriology + Christology) would suggest keeping both readings on the table at v.13 too — not "confirming" interpretation 2.

**REVIEW question for Ben.** Should the project commit to interpretation 2 (personified-church) explicitly, or stay in the "main-field-literal, summary-mentions-metaphor" hybrid? If committing, should a v.13 thai_summary be added to mirror the v.1 surface? If not committing, should the v.13 KD be re-worded to drop the "confirms" framing and stay with "consistent-with"?

---

## 5. προάγω → ก้าวล้ำเกินเลย (v.9) — going-beyond-bounds metaphor — **REVIEW**

2 JN 1:9 contains the rare προάγω-as-doctrinal-progressivism warning:

> πᾶς ὁ **προάγων** καὶ μὴ μένων ἐν τῇ διδαχῇ τοῦ Χριστοῦ
> ทุกคนที่**ก้าวล้ำเกินเลย**และไม่คงอยู่ในคำสอนของพระคริสต์

The 1:9 KD names the principle:

> Per uW figs-metaphor: προάγω 'run-ahead' — preserves the ironic-progress sense (the deceivers' 'innovation' is actually 'leaving-the-faith'). Render ก้าวล้ำเกินเลย — preserves the going-beyond-bounds sense.

**Editorial assessment.** **ก้าวล้ำเกินเลย** (literally "step-cross-over-past") is a strong, principled rendering — it captures the IRONIC-PROGRESS sense (the deceiver thinks they're advancing; in fact they're trespassing-past-the-boundary). This is a hapax-style metaphor in the NT (προάγω elsewhere in NT means "lead/go-before" without the doctrinal-progressivism overtone — Mark 6:45; Matt 14:22). The Johannine-letter usage is the only NT case where προάγω carries the false-progressive theological warning.

The translation choice is unique to 2 JN. It introduces a Thai phrase **ก้าวล้ำเกินเลย** that does NOT recur in the corpus (a Thai-corpus-hapax matching the Greek-corpus-hapax in this sense).

**REVIEW question for Ben.** Is **ก้าวล้ำเกินเลย** the right rendering, or would a more idiomatic Thai construction (e.g., **ก้าวเลยขอบเขต** "step-past-the-boundary"; or **เกินไป** "go-too-far"; or **นอกแนวคำสอน** "outside-the-line-of-teaching") communicate the irony-of-false-progress more naturally to a Thai reader? The rendering is a one-shot — there's no future occurrence in the corpus to compound the editorial weight.

---

## 6. χάρτης + μέλαν (v.12) — NT-hapax letter-writing-materials — **STABLE** (verse-level note covers it)

2 JN 1:12 contains the only NT use of **χάρτης** (papyrus, "paper") and one of two NT uses of **μέλαν** (ink; the other is 2 Cor 3:3; 3 Jn 1:13):

| Greek | Thai |
|---|---|
| χάρτης | **กระดาษ** ("paper") |
| μέλαν | **น้ำหมึก** ("ink") |

The 1:12 KD names the rendering:

> HAPAX χάρτης (only here NT, 'papyrus / paper') → กระดาษ. μέλαν → น้ำหมึก. The literal-letter-writing-materials (papyrus + ink). βούλομαι aorist-passive → ไม่อยาก.

**Editorial assessment.** **กระดาษ + น้ำหมึก** is the standard modern-Thai equivalent. The Thai reader gets the contemporary-letter-writing imagery without anachronism (χάρτης specifically meant *papyrus*, but a Thai reader doesn't need that level of historical-material specificity here — the rhetorical point is "I'd rather meet face-to-face than write a longer letter," which **กระดาษ + น้ำหมึก** carries cleanly). The hapax is flagged in the verse `notes` per RULES §5.

**Recurrence forward:** 3 JN 1:13 (μέλαν + κάλαμος "reed-pen" — different second-noun, but same letter-writing-rather-than-meet rhetorical structure). The 3 JN 1:13 audit (forthcoming) should pick up the **น้ำหมึก** rendering and add a κάλαμος → "ปากกา" or similar hapax-rendering.

**Recommend: STABLE**, no corpus doc needed. Verse-level note covers it.

---

## 7. μὴ λαμβάνετε αὐτὸν εἰς οἰκίαν (v.10) — house-church platform vs private-home hospitality — **DECIDE**

2 JN 1:10 issues the strongest disciplinary instruction in the letter:

> εἴ τις ἔρχεται πρὸς ὑμᾶς καὶ ταύτην τὴν διδαχὴν οὐ φέρει, **μὴ λαμβάνετε αὐτὸν εἰς οἰκίαν**
> ถ้าผู้ใดมาหาท่าน แต่ไม่ได้นำคำสอนนี้มา **อย่าต้อนรับเขาเข้ามาในบ้าน**

The 1:10 KD names the interpretive question:

> Per uW figs-explicit: 'house' here = (a) literal-private-home (refusing-hospitality) OR (b) house-church (refusing-platform). Most-commentators read (b) — the 'house' of-the-house-church should not platform false-teachers. λαμβάνω → ต้อนรับ (with-hospitality sense).

The verse `notes` adds:

> Strong-disciplinary-action against false-teachers. Per scholarly-consensus: this addresses the church-hospitality of itinerant-teachers, NOT a prohibition on all-greetings to non-Christians (which would contradict the love-of-enemies command). thai_summary at v.1 governs the corporate-recipient frame.

**Editorial assessment.** The Thai **บ้าน** is lexically neutral — it can mean a private-home OR a meeting-place (Thai houses-of-worship borrow บ้าน in compound terms like บ้านพระเจ้า). But the *default reading* of a Thai believer encountering **อย่าต้อนรับเขาเข้ามาในบ้าน** ("don't welcome him into your house") will be the literal-private-home reading. This will potentially clash with:

- the love-of-enemies teaching (Matt 5:44; Luke 6:35) which the same Thai reader has internalized as "be hospitable to all";
- modern-Thai cultural expectation of `น้ำใจ` (warm-hearted welcome) toward visitors.

The interpretive crux is: **the historical context** is itinerant-teacher networks where house-hospitality functioned as *doctrinal-endorsement* of the visiting teacher (the host's house was the teaching-platform). Modern Thai Christianity does not generally have this house-as-platform structure; the literal application would over-translate the verse into a contemporary anti-hospitality teaching.

**Two surfacing options:**

**Option A (current).** Bare imperative `อย่าต้อนรับเขาเข้ามาในบ้าน`; `notes` field carries the historical-context disclaimer; no `thai_summary` flag for the typical reader. Pro: preserves the Greek-text fidelity. Con: a typical Thai reader does NOT see the historical-context disclaimer; a literal-application reading is the default.

**Option B (proposed).** Add a `thai_summary` at v.10 explaining the itinerant-teacher house-church context — something like:

> ในบริบทคริสตจักรยุคแรก ผู้สอนเร่ร่อนใช้ 'บ้าน' (คือบ้านที่คริสตจักรพบกัน) เป็นสถานที่สอน การต้อนรับครูผู้สอนเท่ากับการรับรองคำสอนของเขา คำสั่งนี้จึงห้ามการรับครูสอนเทียมเท็จเข้ามาสอนในคริสตจักร ไม่ใช่ห้ามการมีน้ำใจต่อคนทั่วไป (เปรียบเทียบ มัทธิว 5:44 — 'จงรักศัตรู').

(English gloss: "In the early-church context, itinerant-teachers used the 'house' [meaning the house-church] as the teaching place. Welcoming a teacher = endorsing his teaching. This command therefore prohibits receiving false-teachers to teach in the church, NOT prohibiting kindness to people in general — cf. Matt 5:44 'love your enemies'.")

**DECIDE question for Ben.** Stay with Option A (current — historical-context only in `notes`, invisible to the typical reader) or move to Option B (add a v.10 thai_summary surfacing the itinerant-teacher context + explicit cross-reference to love-of-enemies)?

This is a **DECIDE** rather than REVIEW because the practical ethical-implications of Option A's possible-misreading are non-trivial — a literal-private-home reading could harden Thai believers against ordinary cross-faith hospitality.

---

## 8. χαίρειν αὐτῷ μὴ λέγετε (v.10-11) — refusing-greeting strong-disciplinary-action — **DECIDE**

2 JN 1:10-11 closes the false-teacher prohibition with the Hellenistic-greeting-formula refusal:

> καὶ **χαίρειν αὐτῷ μὴ λέγετε**· ὁ λέγων γὰρ αὐτῷ χαίρειν κοινωνεῖ τοῖς ἔργοις αὐτοῦ τοῖς πονηροῖς
> และ**อย่าทักทายเขา** เพราะผู้ที่ทักทายเขาก็ร่วมในการกระทำที่ชั่วร้ายของเขา

The 1:10 KD names the formula:

> 'χαίρειν λέγειν' → ทักทาย (the standard-Hellenistic-greeting formula). Refusing-greeting was a strong-Jewish-cultural disassociation-from-falsehood marker.

**Editorial assessment.** Same surfacing-strategy question as item 7. The bare imperative **อย่าทักทายเขา** ("don't greet him") will read to a typical Thai reader as a personal-greeting prohibition — colliding with Thai cultural expectations of greeting (`สวัสดี` is mandatory courtesy) and with love-of-enemies elsewhere in the NT. Refusal-of-greeting was a specific Hellenistic-Jewish-cultural marker of doctrinal-disassociation-from-the-greeted-person; this is invisible in the bare Thai surface.

The `notes` field acknowledges:

> Hospitality-as-endorsement principle: greeting-the-deceiver participates-in his-evil-works. The cultural-context: itinerant-teacher network where hospitality = doctrinal-endorsement.

But again, `notes` is invisible to the typical Thai reader.

**Two surfacing options:**

**Option A (current).** Bare imperative; `notes` carries the cultural-context disclaimer.

**Option B (proposed).** Add a `thai_summary` at v.10 OR v.11 (probably v.11 since it carries the rationale-clause `ὁ λέγων γὰρ αὐτῷ χαίρειν κοινωνεῖ τοῖς ἔργοις αὐτοῦ τοῖς πονηροῖς`) noting that:
1. The "greeting" here is the formal-greeting-of-doctrinal-endorsement (a Hellenistic-Jewish-cultural marker), not the everyday `สวัสดี`-equivalent.
2. Refusing this greeting = refusing public-affirmation of the false-teacher's mission, NOT refusing personal-courtesy to the person.
3. This is consistent with — not a contradiction of — Matt 5:44's love-of-enemies.

**DECIDE question for Ben.** Same as item 7: stay with Option A (bare imperatives, all interpretive context invisible to the typical reader) or move to Option B (surface the cultural-context in thai_summary)? Items 7 and 8 should likely move together — they are the same surfacing-strategy decision applied to two adjacent verses.

---

## 9. Inherited Johannine + Pastoral + general locks — **all compliant**

| Lock | 2 JN evidence | Status |
|---|---|---|
| ἀγάπη / ἀγαπάω family (1JN audit §1; recommended new doc not yet written) | vv. 1, 3, 5, 6 — all → **ความรัก / รัก / ในความรัก**. The 1:5 ἵνα ἀγαπῶμεν ἀλλήλους ("that-we-love-one-another") matches the 1JN 3:11 + 4:7 corpus-internal-link cited in the verse KD. Compliant. | **STABLE** (extends 1JN; pending corpus doc) |
| ἀλήθεια — Johannine truth | vv. 1, 2, 3, 4 — all → **ความจริง**. The "love + truth" pairing thread is preserved across the four verses. Compliant. | **STABLE** (extends 1JN) |
| ἐντολή → พระบัญญัติ (royal-prefix) | vv. 4, 5, 6 — all → **พระบัญญัติ**. Compliant with the 1JN-corpus rendering. | **STABLE** (extends 1JN) |
| πατήρ register (`narrator_vs_character_voice_2026-04.md`) | vv. 3, 4, 9 → divine πατήρ → **พระบิดา** (royal pระ-) uniform. No human-paternal-analogy occurrences in 2JN. Compliant. | **LOCKED** |
| πρεσβύτερος → ผู้ปกครองคริสตจักร (`pastoral_corpus_locks_2026-05.md`) | v.1 → **ข้าพเจ้าผู้ปกครองคริสตจักร**. See §1 above for the Johannine-self-designation amendment recommendation. | **LOCKED** |
| ἀντίχριστος → ผู้ต่อต้านพระคริสต์ (1JN-locking-precedent) | v.7 → **ผู้ต่อต้านพระคริสต์**. See §2 above; corpus doc lift overdue. | **LOCKED** (corpus doc pending) |
| περιπατέω → ดำเนิน | vv. 4, 6 → **ดำเนิน** uniform. Compliant. | **LOCKED** (corpus precedent) |
| μένω → คงอยู่ (Johannine-keyword) | vv. 2, 9 (×2) → **คงอยู่** uniform. Compliant with 1JN audit §6's μένω-as-Johannine-keyword recommendation. | **STABLE** (pending 1JN-recommended doc) |
| ἀπ' ἀρχῆς → ตั้งแต่ปฐมกาล (Johannine-signature) | vv. 5, 6 → **ตั้งแต่ปฐมกาล** uniform. Compliant with 1 JN 1:1; 2:7, 13, 14, 24; 3:8, 11. | **STABLE** (extends 1JN) |
| πεπληρωμένη-of-joy phrase-lock (1JN audit) | v.12 → **ความยินดี ... จะเต็มบริบูรณ์**. Compliant with the 5-occurrence Johannine corpus phrase-lock (1 JN 1:4; JHN 15:11; 16:24; 17:13; 2 JN 12). The verse KD calls it out: "PHRASE-LOCK: Johannine joy-completion (matches 1 JN 1:4 + JHN 15:11 + 16:24 + 17:13 corpus-internal-Johannine)." | **LOCKED** (`check_phrase_consistency.py` clean) |
| Triple-greeting χάρις ἔλεος εἰρήνη (Pastoral-Johannine-shared formula) | v.3 → **พระคุณ พระเมตตา และสันติสุข**. Compliant with 1 Tim 1:2; 2 Tim 1:2 (Pastoral lock). | **LOCKED** (`pastoral_corpus_locks_2026-05.md` triple-greeting precedent) |
| σάρξ → เนื้อหนัง | v.7 → **เนื้อหนัง**. Compliant with 1 JN 4:2 + the corpus-locked Pauline σάρξ rendering. | **LOCKED** (`sarx_pauline_2026-05.md`) |
| πλάνος → คนล่อลวง | v.7 (×2) → **คนล่อลวง** uniform. Compliant; first project-corpus occurrence of this lemma in this exact-form (πλάνη "deception" occurs elsewhere, but πλάνος "deceiver" is rare). | **STABLE** |
| κοινωνέω → ร่วมใน | v.11 → **ร่วมใน**. Compliant with κοινωνία-family corpus-precedent. | **LOCKED** (corpus precedent) |
| ἀσπάζομαι → ฝากความระลึกถึง | v.13 → **ฝากความระลึกถึง**. Compliant with the Pauline-epistolary corpus-precedent. | **LOCKED** (corpus precedent) |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** in 2 JN — `audit_inclusion_variants.py --book 2JN --strict` would return 0 candidates (no SBLGNT-omits-mainstream-includes variants in 2 JN; no Tier 1/2/3 dispositions needed). The verse-level KDs note one minor SBLGNT-textual-choice at v.8 (`εἰργασάμεθα` 1pl + `ἀπολέσητε / ἀπολάβητε` 2pl-pl, where Byzantine has 2pl throughout); both followed SBLGNT silently per RULES §0. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 2 JN is a doctrinal-pastoral letter, not narrative. | **LOCKED (N/A)** |
| Vocative kyrie / didaskale register | N/A — no vocative κύριε in 2 JN. | **LOCKED (N/A)** |
| OT citations (`data/nt_ot_citations.json`) | **None** in 2 JN — no formal OT citations or strong allusions surfaced. | **LOCKED (N/A)** |

---

## Mechanical (§1) — **all green**

- 1/1 chapter: `output/check_reports/2john_01_review.md` ✓
- 1/1 chapter: `output/back_translations/2john_01.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-226-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (incl. the Johannine πεπληρωμένη-of-joy phrase that 2 JN 12 ratifies)
- `audit_inclusion_variants.py --book 2JN --strict`: clean (no candidates — 2 JN has no SBLGNT-omits-mainstream-includes variants)
- `git status output/`: only unrelated paratext exports + 1 textual_variants file from the 2026-05-03 1JN audit; no 2 JN source-file dirt

---

## Pre-existing docs affirmed / unchanged

All 47 docs in `docs/translator_decisions/` are unchanged by 2 JN. The audit confirms compliance with the Johannine + Pastoral + Pauline + Petrine + general locks. The 1JN audit's recommendation list (8 new docs, 2 amendments) remains valid; 2 JN does NOT add new corpus-doc recommendations beyond the 1JN list, but it RATIFIES three of them as immediately overdue:

1. **`antichristos_johannine_2026-05.md`** (1JN audit §2; ratified by 2 JN 7) — write NOW, no further test cases ahead
2. **`agape_johannine_2026-05.md`** (1JN audit §1; ratified by 2 JN 1, 3, 5, 6) — write before 3 JN ships (3 JN 1, 6 add small-but-confirming evidence base)
3. **Brief amendment to `poimen_episkopos_register_split_2026-05.md`** (or `pastoral_corpus_locks`) for the **Johannine-letter `Ὁ πρεσβύτερος` self-designation sub-case** (§1 above) — write before 3 JN ships (3 JN 1:1 has the same construction)

The 1JN audit's `petrine_eschatological_disambiguation_2026-05.md` ambiguity-preservation principle is implicitly reaffirmed in the 2 JN handling of the chosen-lady reading (§4) — the v.1 thai_summary preserves both readings, even though the v.13 KD goes a step further with "confirms."

---

## Flagged for Ben's attention

### A. Add corpus doc `antichristos_johannine_2026-05.md` — **STABLE → LOCKED transition** (§2)
The 1JN audit recommended this; 2 JN ratifies the lock with the FINAL NT test-case (no further ἀντίχριστος occurrences in 3 JN or Revelation). Writing the doc closes the corpus rather than anticipating future tests.

### B. Brief amendment for Johannine-letter `Ὁ πρεσβύτερος` self-designation — **STABLE** (§1)
Add a sub-section to `poimen_episkopos_register_split_2026-05.md` (or `pastoral_corpus_locks_2026-05.md`) noting that the definite-article + simple-form `Ὁ πρεσβύτερος` at 2 JN 1:1 + 3 JN 1:1 inherits the locked **ผู้ปกครองคริสตจักร** rendering without committing to the patristic "John the Elder" identification question. Write before 3 JN ships.

### C. ἐρχόμενον vs ἐληλυθότα aspectual difference at v.7 — **REVIEW** (§3)
Should v.7 get a thai_summary distinguishing the present-participle from 1 JN 4:2's perfect-participle, surfacing the future-coming interpretive minority view? Or is the current verse-level note sufficient? The aspectual difference is genuine but the interpretive consequences are minor for the project's evangelical-Protestant default audience.

### D. Chosen-lady (v.1) + sister-church (v.13) interpretive surface — **REVIEW** (§4)
Internal tension: v.1 thai_summary treats the personified-church reading as one-of-two scholarly options; v.13 KD says "confirms." Should the project commit to interpretation 2 explicitly (and add a v.13 thai_summary mirroring v.1), or stay with the hybrid surface and re-word the v.13 KD to drop "confirms"?

### E. προάγω → ก้าวล้ำเกินเลย at v.9 — **REVIEW** (§5)
Is the Thai-corpus-hapax **ก้าวล้ำเกินเลย** the right rendering, or would a more idiomatic alternative (**ก้าวเลยขอบเขต** / **เกินไป** / **นอกแนวคำสอน**) communicate the irony-of-false-progress better to a Thai reader?

### F. v.10 `μὴ λαμβάνετε εἰς οἰκίαν` surfacing — **DECIDE** (§7)
Stay with the bare imperative (Option A) or add a v.10 thai_summary surfacing the itinerant-teacher house-church context + explicit love-of-enemies cross-reference (Option B)?

### G. v.10-11 `χαίρειν αὐτῷ μὴ λέγετε` surfacing — **DECIDE** (§8)
Same question as F applied to the refusing-greeting imperative. The two should likely move together since they're adjacent verses with the same surfacing-strategy question.

### H. New corpus docs to write (in priority order)
1. **`docs/translator_decisions/antichristos_johannine_2026-05.md`** (§2) — locks **ผู้ต่อต้านพระคริสต์** for the Johannine corpus; 1+2 JN-only lemma in NT, no further tests needed
2. **`docs/translator_decisions/agape_johannine_2026-05.md`** (1JN audit §1) — write before 3 JN ships
3. **Brief amendment** to `poimen_episkopos_register_split_2026-05.md` for the Johannine-self-designation sub-case (§1)

### I. External AI review (§3 of checklist) — **pending**
Recommended before `book-2john-v1` tag. Suggested 3-cluster external AI packet:
1. **2 JN 1-3 + 13** — opening + chosen-lady interpretation + closing-sister-church-greetings
2. **2 JN 4-9** — love + commandment + truth-in-walking + ἀντίχριστος doctrinal-warning + προάγω
3. **2 JN 10-12** — false-teacher disciplinary-action + house-church / refusing-greeting + closing-letter-materials + joy-completion

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/1TH/1JN pattern. The packet should foreground items C (ἐρχόμενον), F+G (surfacing strategy), and the present-participle anti-Docetic question — the rest of 2 JN is corpus-derivative and well-locked.

---

## Recommendation

**2 John ships in strong corpus-hygiene shape — and serves principally as a RATIFICATION of the Johannine-corpus locks 1 JN established yesterday rather than as a new editorial entry-point.** The translator made principled choices on the few 2JN-distinctive items (πρεσβύτερος-self-designation; present-participle ἐρχόμενον; chosen-lady-as-personified-church; προάγω going-beyond-bounds). The two DECIDE items (F + G) are surfacing-strategy questions — they can be addressed via low-cost thai_summary additions without touching the main `thai` field, so they do not strictly block the v1 tag if Ben prefers Option A.

Tag `book-2john-v1` after:
1. Ben's decisions on **F + G** (surfacing strategy for v.10 house-church + v.10-11 refusing-greeting); both can resolve as Option A (status quo) without code/translation changes
2. Ben's confirmation on **C, D, E** (REVIEW items: ἐρχόμενον aspect; chosen-lady commitment; προάγω rendering)
3. **Item A** (`antichristos_johannine_2026-05.md`) written — the 1JN-recommended doc that this audit ratifies as overdue. Single-author, ~1-2 hours
4. **(Optional)** Items B + 2 (Johannine-self-designation amendment + `agape_johannine`) — lower priority; can wait until 3 JN ships
5. External AI sanity-check (§I) via Grok / ChatGPT / Gemini

The Johannine catholic letters (3 JN ahead, Revelation downstream) will inherit the now-fully-ratified Johannine-letter lock-set. 3 JN is even shorter (14 verses); its audit will likely confirm 2 JN's Johannine-self-designation amendment + add minor κάλαμος hapax handling at 3 JN 1:13.
