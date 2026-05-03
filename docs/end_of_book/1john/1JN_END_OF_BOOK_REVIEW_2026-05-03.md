# 1 John — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 5 chapters (105 verses; 228 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (47 docs).
**Trigger:** 1JN 5 shipped (commit `d1ee6af`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 5/5 chapters have green per-chapter `*_review.md` reports + `*_summary.json` + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-225-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows only the re-run-key-term artifact + already-committed `output/textual_variants/1john_05.json` Tier 2 footer. No 1JN source-file dirt.
- **1 John is the FIRST FULL Catholic-Epistle Johannine letter the project has shipped.** It strongly cross-validates the Johannine corpus locks established in JHN (paraclete, λόγος → พระวาทะ, τέκνα θεοῦ, ζωὴ αἰώνιος, μένω, μονογενής, σωτὴρ τοῦ κόσμου) and **introduces three new corpus-cross-cutting clusters**: the **ἀντίχριστος** lemma (NT-rare; only 1 + 2 JN), the **ἱλασμός** atonement-noun (NT hapax to 1JN at 2:2 + 4:10), and the **χρῖσμα** anointing-noun (NT hapax to 1JN at 2:20 + 2:27). All three lemmas are first-and-densest-occurring here and need corpus-doc lift before 2 JN ships (where ἀντίχριστος recurs at 2:7).
- **The Comma Johanneum at 5:7-8 is correctly handled as Tier 2 footer** per `inclusion_variants_absent_verses_2026-04.md` Path A — main flow has bare "เพราะมีพยานสามฝ่าย / คือพระวิญญาณ น้ำ และโลหิต" without the trinitarian-formula-interpolation; `output/textual_variants/1john_05.json` documents the variant fully (Greek + Thai + 𝔓⁷⁴/ℵ/A/B witness-list + Erasmus 1522 history). **LOCKED ✓.**
- **The triple-DECIDE cluster on the chapter-5 dense theology**: (a) ὕδωρ + αἷμα at 5:6 (3-way ambiguity preserved); (b) ἁμαρτία πρὸς θάνατον at 5:16 (3-way ambiguity preserved); (c) οὗτός ἐστιν ὁ ἀληθινὸς θεός at 5:20 (Christological-antecedent reading committed per `pastoral_corpus_locks_2026-05.md §C`). All three rely on `petrine_eschatological_disambiguation_2026-05.md` "preserve-ambiguity" principle (extended from eschatology to soteriology + Christology) — Ben should confirm the doc's principle is intentionally being applied this broadly.
- **18 inherited Johannine + Pauline + Petrine + Pastoral locks verified compliant** (λόγος → พระวาทะ; τέκνα θεοῦ; ζωὴ αἰώνιος; μονογενής; σωτὴρ τοῦ κόσμου; παράκλητος; μαρτυρέω; narrator-κύριος; pagan-εἴδωλον; Comma-Johanneum-omission; παρουσία at 2:28; etc.). See §13 for the full compliance table.
- **5 cross-cutting Johannine patterns are STABLE-but-undocumented at corpus level** (ἀντίχριστος; ἱλασμός; χρῖσμα; μένω as Johannine-keyword; γεννηθεὶς ἐκ τοῦ θεοῦ). All five are first-or-densest-occurring here, so corpus-doc lift is recommended before 2 JN + 3 JN + Revelation compound the editorial weight.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: σπέρμα-of-God metaphor at 3:9; the present-vs-aorist ἁμαρτάνω habitual-vs-occasional rendering at 3:6, 9 vs 1:8-10; παράκλητος Christ-vs-Spirit corpus-doc amendment).
- **3 items flagged DECIDE** (the πρὸς θάνατον "sin unto death" at 5:16 ambiguity-preservation strategy; the οὗτός antecedent at 5:20 high-Christology commitment; the ἱλασμός extent at 2:2 περὶ ὅλου τοῦ κόσμου Calvinist/Arminian framing).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. ἀγάπη / ἀγαπάω — the cardinal Johannine theme — **STABLE (extends JHN; consider corpus doc)**

1 John is the densest ἀγάπη / ἀγαπάω passage in the entire NT — **44 occurrences across 105 verses** (~ 0.42 per verse), capped by the twin ontological-confessions at 4:8 + 4:16 (**ὁ θεὸς ἀγάπη ἐστίν → พระเจ้าทรงเป็นความรัก**). The lexical lock is uniform throughout:

| Greek | Thai | Sense |
|---|---|---|
| ἀγάπη (love-noun, divine-source) | **ความรัก** | substantive love |
| ἀγαπάω (love-verb) | **รัก** | to love |
| ἀγαπητοί (vocative plural) | **ท่านที่รัก** | "beloved [readers]" — pastoral address |
| ἀγαπητός (singular) | **ที่รัก** | beloved (within compounds) |

**Key locking verses:**
- **4:8 + 4:16** ὁ θεὸς ἀγάπη ἐστίν → **พระเจ้าทรงเป็นความรัก** — the Johannine-signature ontological-confession; uniform double-occurrence preserves the framing-and-reframing structure of 4:7-21.
- **4:18** ἡ τελεία ἀγάπη ἔξω βάλλει τὸν φόβον → **ความรักที่สมบูρณ์ก็ขับความกลัวออกไป** — preserves the perfect-passive τελειόω → สมบูρณ์.
- **3:1** ἴδετε ποταπὴν ἀγάπην δέδωκεν ἡμῖν ὁ πατὴρ → **จงดูเถิด พระบิดาทρงประทานความรักอันยิ่งใหญ่เพียงใดแก่เรา** — preserves the exclamatory ποταπός "what manner / how-great-a-kind-of."

**Genitive-ambiguity preserved at 2:5, 2:15, 3:17, 4:9** (ἡ ἀγάπη τοῦ θεοῦ): each verse-level KD acknowledges subjective-vs-objective genitive and lets Thai readers receive the same Greek ambiguity. At 5:3 the context is explicit (αὕτη γάρ ἐστιν ἡ ἀγάπη τοῦ θεοῦ ἵνα τὰς ἐντολὰς αὐτοῦ τηρῶμεν) → **ความรักต่อพระเจ้า** (subjective-genitive, our-love-toward-God) — only departure where context demands disambiguation.

**Editorial assessment:** Single-rendering **ความรัก / รัก** is principled and uniform. The Johannine-signature pastoral-address vocative **ท่านที่รัก** (ἀγαπητοί — recurs at 2:7; 3:2, 21; 4:1, 7, 11) is consistent. The 1JN ἀγάπη-cluster effectively LOCKS the rendering for the Johannine corpus and forward into 2 JN + 3 JN.

**Recommend: STABLE; consider new corpus doc** `docs/translator_decisions/agape_johannine_2026-05.md` to lock **ความรัก / รัก** for the Johannine corpus, with sub-sections for: (a) the genitive-ambiguity-preservation rule for ἡ ἀγάπη τοῦ θεοῦ; (b) the τελειόω-of-love perfecting-formula → สมบูρณ์; (c) the ἀγαπητοί vocative → ท่านที่รัก; (d) the ontological-confession 4:8/16 phrasing-lock. Forward applicability: 2 JN 1, 3, 5; 3 JN 1, 2, 5, 11; the κἀγὼ ἀγαπῶ logic of 2 JN 1 + 3 JN 1.

---

## 2. ἀντίχριστος — antichrist (NT-rare; corpus entry-point) — **STABLE (undocumented; recommend new doc)**

ἀντίχριστος is **only-NT in 1+2 John** (1JN 2:18 ×2, 2:22, 4:3; 2JN 7). 1 John is the corpus-entry-point. All four occurrences render **ผู้ต่อต้านพระคริสต์** ("the-against-Christ" / "the-anti-Christ"):

| Verse | Greek | Thai | Number |
|---|---|---|---|
| 2:18a | καθὼς ἠκούσατε ὅτι ἀντίχριστος ἔρχεται | **ผู้ต่อต้านพระคริสต์กำลังจะมา** | sing. (eschatological-future) |
| 2:18b | καὶ νῦν ἀντίχριστοι πολλοὶ γεγόνασιν | **ผู้ต่อต้านพระคริสต์มากมายเกิดขึ้นแล้ว** | pl. (current-many) |
| 2:22 | οὗτός ἐστιν ὁ ἀντίχριστος | **ผู้นั้นแหละเป็นผู้ต่อต้านพระคริสต์** | sing.-definitional |
| 4:3 | τοῦτό ἐστιν τὸ τοῦ ἀντιχρίστου | **วิญญาณของผู้ต่อต้านพระคริสต์** | gen. (the-spirit-of-anti-Christ) |

The 2:18 KD names the principle:

> ἀντίχριστος (only 1+2 JN NT) → ผู้ต่อต้านพระคริสต์ (the-anti-Christ; preserves the deliberate 'against-and-instead-of' sense). ἀντίχριστος singular (eschatological-future) AND plural (current-many) — preserved in Thai with explicit-singular-and-plural parallel.

The 2:18 thai_summary explains the singular-future + plural-present interpretive options for Thai readers, citing 2 Thess 2:1-12 for the eschatological-future-figure reading. Per `petrine_eschatological_disambiguation_2026-05.md`: preserve-ambiguity (both interpretations exegetically defensible).

**Editorial assessment:** **ผู้ต่อต้านพระคริสต์** is principled — it preserves the ἀντί- "against / instead-of" force AND avoids importing the dispensationalist English "Antichrist" framing as a name (it reads as a descriptive title, not a proper noun). The singular-vs-plural distinction is preserved naturally in Thai (ผู้... vs ผู้... มากมาย). The 4:3 neuter τὸ τοῦ ἀντιχρίστου → **วิญญาณของผู้ต่อต้านพระคริสต์** is a natural-Thai reading of the abstract-noun-substitute.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/antichristos_johannine_2026-05.md` BEFORE 2 JN ships (where 2 JN 7 introduces ὁ πλάνος καὶ ὁ ἀντίχριστος — the deceiver-AND-antichrist construction, requiring Thai parataxis). The doc should:
1. Lock ἀντίχριστος (singular OR plural) → **ผู้ต่อต้านพระคริสต์**
2. Note the singular-future-vs-plural-present ambiguity-preservation principle (per `petrine_eschatological_disambiguation_2026-05.md`)
3. Cross-reference but DO NOT collapse with related-but-distinct lemmas: ψευδόχριστος ("false-Christ" — Matt 24:24 + Mark 13:22) → **พระคริสต์เทียมเท็จ** (different lemma, different rendering); ὁ ἄνομος / ὁ ἄνθρωπος τῆς ἀνομίας ("the lawless one" — 2 Thess 2:3, 8) → **ผู้ที่ไร้กฎหมาย** (separate locked rendering)
4. Cite 1 JN 2:18 as the locking precedent (densest first-occurrence cluster)
5. Surface the relationship to the 4:1-3 pneumatology-test (the spirit-of-antichrist doctrinal-test)

---

## 3. ἱλασμός — atonement-noun (NT hapax to 1 John) — **STABLE (undocumented; recommend new doc)**

ἱλασμός is **only-NT in 1 John 2:2 + 4:10** — both render **เครื่องบูชาไถ่บาป** ("sacrifice-of-atonement"):

| Verse | Greek | Thai |
|---|---|---|
| 2:2 | καὶ αὐτὸς ἱλασμός ἐστιν περὶ τῶν ἁμαρτιῶν ἡμῶν | **และพระองค์เองทรงเป็นเครื่องบูชาไถ่บาปของเราทั้งหลาย** |
| 4:10 | ἀπέστειλεν τὸν υἱὸν αὐτοῦ ἱλασμὸν περὶ τῶν ἁμαρτιῶν ἡμῶν | **ทรงใช้พระบุตรของพระองค์มาเป็นเครื่องบูชาไถ่บาปของเรา** |

The 2:2 KD names the principle:

> ἱλασμός → เครื่องบูชาไถ่บาป — same Thai as ἱλαστήριον at ROM 3:25 (corpus-precedent; cognate-noun in the same Levitical-atonement word-family). Per RULES §0 evangelical-Protestant default: propitiation + expiation + mercy-seat composite-sense preserved.

**Editorial assessment:** The cognate-locking with ἱλαστήριον at Rom 3:25 (the "mercy seat / propitiation" Pauline locus-classicus) is principled — it preserves the Levitical-atonement-vocabulary thread across Pauline and Johannine corpora. **เครื่องบูชาไถ่บาป** is the standard evangelical-Protestant Thai rendering (carrying both propitiation-of-divine-wrath AND expiation-of-sin senses without collapsing to one); compatible with both the Reformed-substitutionary and the Christus-Victor frameworks. The αὐτός-emphatic at 2:2 (Christ Himself IS the ἱλασμός) is preserved with พระองค์เอง + ทรงเป็น (royal-prefix for divine-action).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/hilasmos_hilasterion_atonement_2026-05.md` to formalize the cognate-locking: ἱλασμός (1 JN 2:2; 4:10) ↔ ἱλαστήριον (Rom 3:25; Heb 9:5) ↔ ἱλάσκομαι verbal (Heb 2:17 ὅθεν εἰς τὸ ἱλάσκεσθαι τὰς ἁμαρτίας — render ทรงไถ่บาป) → **เครื่องบูชาไถ่บาป / ไถ่บาป** family. The doc should:
1. Lock ἱλασμός (Christ-as-substantive-atonement) → **เครื่องบูชาไถ่บาป**
2. Lock ἱλαστήριον (the Levitical-mercy-seat) → **เครื่องบูชาไถ่บาป** (same Thai for the cognate-pair)
3. Lock ἱλάσκομαι (verbal "make-atonement") → **ทรงไถ่บาป** (royal-prefix; God/Christ-subject)
4. Note the deliberate non-narrowing: the Thai เครื่องบูชาไถ่บาป preserves both propitiation (toward God) AND expiation (of sin), matching the canonical-evangelical-Protestant non-binary reading
5. Cite 1 JN 2:2 + Rom 3:25 as the locking precedents
6. Forward applicability: Heb 9:5 ἱλαστήριον ("mercy-seat" tabernacle-context); Heb 2:17 ἱλάσκομαι (verbal); 1 JN 4:10 (here-ratifying)

(See §11 for the SEPARATE 2:2 περὶ ὅλου τοῦ κόσμου ambiguity-preservation crux — that is the Calvinist-Arminian extent-of-atonement question, distinct from the ἱλασμός-rendering question.)

---

## 4. χρῖσμα — anointing (NT hapax to 1 John) — **STABLE (undocumented; consider brief new doc)**

χρῖσμα is **only-NT in 1 John 2:20 + 2:27** (×2 in 2:27) — all three render **การเจิม** ("the anointing"):

| Verse | Greek | Thai |
|---|---|---|
| 2:20 | καὶ ὑμεῖς χρῖσμα ἔχετε ἀπὸ τοῦ ἁγίου | **ท่านได้รับการเจิมจากพระผู้บริสุทธิ์** |
| 2:27a | τὸ χρῖσμα ὃ ἐλάβετε ἀπ' αὐτοῦ μένει ἐν ὑμῖν | **การเจิมที่ท่านได้รับจากพระองค์นั้น คงอยู่ในท่าน** |
| 2:27b | ὡς τὸ αὐτοῦ χρῖσμα διδάσκει ὑμᾶς περὶ πάντων | **เหมือนการเจิมของพระองค์สอนท่านในทุกสิ่ง** |

The 2:20 KD names the OT-ritual background:

> χρῖσμα → การเจิม — preserves the OT-ritual-anointing background (cf. EXO 30:25 + LEV 21:10 anointing-with-oil). Per uW: most commentators identify χρῖσμα = the Holy Spirit (cf. JHN 14:26 + 16:13 — the Spirit-teaches-all-things, paralleling 1 JN 2:27).

**Editorial assessment:** **การเจิม** preserves the OT-priestly + royal-anointing imagery (cognate of χρίω, root of Χριστός = "the Anointed-One") and matches the broader Thai-evangelical χρίω-family rendering (1 Sam 16:13 anointing; Acts 10:38 "God anointed Jesus with the Holy Spirit" — same root). The Spirit-as-teacher-of-all-things echo at 2:27 is preserved (corpus-internal-link to JHN 14:26 + 16:13).

**Recommend: STABLE; consider brief new doc** `docs/translator_decisions/chrisma_anointing_2026-05.md` to lock χρῖσμα → **การเจิม** + cross-reference the cognate-Christological-title χριστός → พระคริสต์ + the verbal χρίω → ทรงเจิม (royal-prefix) for Heb 1:9 ἔχρισέν σε ὁ θεός + Acts 10:38 ἔχρισεν αὐτὸν ὁ θεός. Brief: this is a 3-occurrence cluster in a single passage, but the Spirit-as-anointing identification is theologically load-bearing for any future Pentecostal-Charismatic Thai-readership concerns.

---

## 5. μένω — Johannine-keyword "abide / remain" — **STABLE (undocumented; recommend corpus doc)**

μένω is **the Johannine signature verb par excellence** — 24 occurrences in 1 John (more than any other lemma except ἀγάπη). All occurrences render **คงอยู่** ("to remain / abide"):

| Sense | Verses | Example |
|---|---|---|
| Mutual-abiding (believer ↔ God) | 2:6, 24, 27, 28; 3:6, 24; 4:12, 13, 15, 16; 5:20 | 4:13 ἐν τῷ θεῷ μένει καὶ ὁ θεὸς ἐν αὐτῷ → **คงอยู่ในพระเจ้า และพระเจ้าก็คงอยู่ในผู้นั้น** |
| Word/seed/anointing-abiding | 2:14, 24; 3:9, 17; 5:38 (cited internally) | 3:9 σπέρμα αὐτοῦ ἐν αὐτῷ μένει → **พระเมล็ดพันธุ์ของพระเจ้าคงอยู่ในเขา** |
| Persons-abiding (apostates' opposite) | 2:19; 3:14 | 2:19 μεμενήκεισαν ἂν μεθ' ἡμῶν → **พวกเขาคงอยู่กับเราต่อไป** |
| Counterpart-abiding (death/darkness) | 2:11; 3:14, 15, 17 | 3:14 ὁ μὴ ἀγαπῶν μένει ἐν τῷ θανάτῳ → **ผู้ที่ไม่รักก็คงอยู่ในความตาย** |

**Editorial assessment:** Single-rendering **คงอยู่** is uniform across all 24 occurrences — preserving the Johannine-distinct theological-vocabulary that English collapses into "abide / remain / continue / dwell" depending on context. The Thai keeps the lexical-thread visible, which is essential for tracing the Johannine-mutual-indwelling theme (climaxing at 4:13-16 with the triple-μένω structure: in-love + in-God + God-in-him).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/meno_johannine_abide_2026-05.md` BEFORE 2 JN + 3 JN + Revelation. The doc should:
1. Lock μένω (all senses) → **คงอยู่**
2. Note the Johannine-mutual-abiding signature: the formula "X ἐν Y μένει καὶ Y ἐν X μένει" → **X คงอยู่ใน Y และ Y ก็คงอยู่ใน X**
3. Note the antithetical-abiding extension: those-not-abiding-in-light/love/God ↔ those-abiding-in-darkness/death (3:14)
4. Cross-reference JHN 15 (μένω ἐν ἐμοί / vine-and-branches) for the corpus-internal-locking precedent
5. Cite 1 JN 2:24 + 4:13 + 4:16 as the densest-locking-precedents

---

## 6. γεγεννημένος / γεννηθείς ἐκ τοῦ θεοῦ — "born of God" formula — **STABLE (undocumented; recommend corpus doc)**

The Johannine-signature formula γεννάω + ἐκ τοῦ θεοῦ ("to be-born of God") recurs **5 times in 1 John** at 2:29; 3:9 (×2); 4:7; 5:1; 5:4; 5:18 (×2 — believer-and-Christ distinction):

| Verse | Greek | Thai | Form |
|---|---|---|---|
| 2:29 | πᾶς ὁ ποιῶν τὴν δικαιοσύνην ἐξ αὐτοῦ γεγέννηται | **ทุกคนที่ประพฤติชอบธรรมก็ได้บังเกิดจากพระองค์** | perf.-pass. |
| 3:9 | πᾶς ὁ γεγεννημένος ἐκ τοῦ θεοῦ ἁμαρτίαν οὐ ποιεῖ | **ทุกคนที่ได้บังเกิดจากพระเจ้าก็ไม่ได้ทำบาปต่อไป** | perf.-pass.-pcpl. |
| 4:7 | πᾶς ὁ ἀγαπῶν ἐκ τοῦ θεοῦ γεγέννηται | **ทุกคนที่รักก็ได้บังเกิดจากพระเจ้า** | perf.-pass. |
| 5:1 | πᾶς ὁ πιστεύων ... ἐκ τοῦ θεοῦ γεγέννηται | **ทุกคนที่เชื่อ ... ก็ได้บังเกิดจากพระเจ้า** | perf.-pass. |
| 5:4 | πᾶν τὸ γεγεννημένον ἐκ τοῦ θεοῦ νικᾷ τὸν κόσμον | **ทุกคนที่ได้บังเกิดจากพระเจ้าก็มีชัยเหนือโลก** | perf.-pass.-pcpl. |
| 5:18 | πᾶς ὁ γεγεννημένος ἐκ τοῦ θεοῦ ... | **ทุกคนที่ได้บังเกิดจากพระเจ้า ...** | perf.-pass.-pcpl. (believer) |
| 5:18 | ὁ γεννηθεὶς ἐκ τοῦ θεοῦ τηρεῖ αὐτόν | **ผู้ที่ทรงบังเกิดจากพระเจ้าก็ทรงปกป้องเขาไว้** | aor.-pass.-pcpl. (Christ-distinct) |

The 5:18 KD names the **CRITICAL Greek-tense distinction**:

> Per uW: NB Greek-tense distinction — 'ὁ γεγεννημένος' (perfect-participle = the believer-with-permanent-result-of-having-been-born-of-God) vs 'ὁ γεννηθείς' (aorist-participle = the Christ-uniquely-born / the Begotten-One). Render preserves the distinction by using ทรง- (royal-prefix) ONLY for the second participle (Christ-as-divine-keeper-of-believer).

**Editorial assessment:** The translator's principled use of **the royal-prefix ทรง-** to mark the aorist-participle ὁ γεννηθείς (= Christ as the uniquely-born, the divine-keeper) vs **plain ได้บังเกิด** for the perfect-participle ὁ γεγεννημένος (= believers as those-who-have-been-born) is a brilliant Thai-grammatical solution to a Greek tense-distinction that English typically loses (most English translations render both "born of God" identically, footnoting the distinction). This is one of the strongest editorial moves in 1 John and warrants explicit corpus-doc documentation.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/gegenneménos_ek_theou_johannine_2026-05.md`. The doc should:
1. Lock γεγεννημένος / γεγέννηται (perf.-pass.) → **ได้บังเกิดจากพระเจ้า / ได้บังเกิดจากพระองค์** (plain register; the believer's-status-with-permanent-result)
2. Lock γεννηθείς (aor.-pass.) at 5:18b as the unique-Christological referent → **ผู้ที่ทรงบังเกิดจากพระเจ้า** (royal-prefix; preserves Christ as divinely-begotten)
3. Note the JHN 1:13 corpus-internal-link (ἐκ θεοῦ ἐγεννήθησαν) — same formula
4. Cross-reference but distinguish: μονογενής → องค์เดียว (corpus-locked from JHN 1:14, 18; 3:16, 18; 1 JN 4:9)
5. Cite 1 JN 5:18 as the locking-precedent (where the perfect-vs-aorist distinction is densest)

---

## 7. παράκλητος — Christ-as-advocate (locks-against JHN's Spirit-paraclete) — **LOCKED ✓ (consider doc amendment)**

1 JN 2:1 introduces παράκλητος as a **Christological** advocate (Christ-with-the-Father), departing from the JHN παράκλητος = the Holy Spirit (JHN 14:16, 26; 15:26; 16:7). The Thai rendering preserves the corpus-lock:

> 1 JN 2:1 GK: παράκλητον ἔχομεν πρὸς τὸν πατέρα Ἰησοῦν Χριστὸν δίκαιον
> Thai: เราก็มีพระผู้ช่วยที่อยู่ต่อพระพักตร์พระบิดา คือพระเยซูคริสต์ผู้ทรงชอบธรรม

The 2:1 KD names the cross-corpus-Christological-pneumatological logic:

> παράκλητος → พระผู้ช่วย corpus-lock from JHN 14:16, 26; 15:26; 16:7 (royal-prefix preserved when divine-Christological). NB: in JHN παράκλητος = the Holy Spirit; here in 1 JN παράκλητος = Christ Himself. The 'another παράκλητος' logic of JHN 14:16 (ἄλλον παράκλητον) implies Jesus was the FIRST παράκλητος (here at 1 JN 2:1) and the Spirit is the OTHER παράκλητος (in JHN). Thai-lock preserves the cross-corpus-Christological-pneumatological pair.

**Editorial assessment:** **พระผู้ช่วย** ("the helper / advocate," royal-prefixed) is principled — it preserves the divine-status-of-the-advocate without committing to "lawyer" (which would over-narrow to legal context) or "comforter" (which would over-narrow to consolation). Compliance with the JHN-doc-implicit lock is exact. The δίκαιος-as-Christological-title at 2:1c → **ผู้ทรงชอบธรรม** (royal-prefix) preserves the title-status (vs generic-adjective register).

**Recommend: LOCKED — consider amendment to corpus doc** (no current `paraklētos_2026-XX.md` doc exists; the rule is implicit in the JHN audit). Lift to a brief corpus doc `docs/translator_decisions/paraklētos_christological_pneumatological_2026-05.md`:
1. Lock παράκλητος → **พระผู้ช่วย** (royal-prefix)
2. Note the dual-referent rule: in JHN = the Holy Spirit (4 occurrences); in 1 JN 2:1 = Christ (1 occurrence)
3. Surface the JHN 14:16 ἄλλον παράκλητον "another paraclete" logic that ties the two referents together
4. Forward applicability: any Patristic cross-reference appendix; potential 2 JN / 3 JN citation (none explicit)

---

## 8. σπέρμα τοῦ θεοῦ at 3:9 — divine-seed metaphor — **REVIEW (rationale comprehensive at verse level)**

The famous 3:9 sentence:

> πᾶς ὁ γεγεννημένος ἐκ τοῦ θεοῦ ἁμαρτίαν οὐ ποιεῖ, ὅτι σπέρμα αὐτοῦ ἐν αὐτῷ μένει
> ทุกคนที่ได้บังเกิดจากพระเจ้าก็ไม่ได้ทำบาปต่อไป เพราะพระเมล็ดพันธุ์ของพระเจ้าคงอยู่ในเขา

The 3:9 KD names the metaphor:

> Per uW figs-metaphor: σπέρμα = divine-seed-or-life-principle (NOT physical-seed). Render พระเมล็ดพันธุ์ของพระเจ้า — preserves the divine-implanted-life metaphor + royal-prefix for divine-attribute. Most commentators identify σπέρμα = the Holy Spirit OR the divine-Word (cf. 1 PET 1:23 σπορᾶς ἀφθάρτου 'imperishable-seed').

**Editorial assessment:** **พระเมล็ดพันธุ์ของพระเจ้า** ("the seed-of-God," royal-prefix-pระ-) is a defensible compromise — it preserves the Greek metaphor's biological-implantation force while the royal-prefix prevents reading-it-as-physical-seed (which a plain เมล็ดพันธุ์ might suggest). The cross-reference to 1 PET 1:23 σπορᾶς ἀφθάρτου ("imperishable-seed") is theologically apt — both identify the implanted-divine-principle as the basis of the believer's-non-habitual-sin.

**REVIEW flag — Ben's confirmation worth getting on:**
1. The royal-prefix on a non-Christological-non-divine-direct noun (the seed is GOD'S; the seed itself is not God or Christ). Is **พระเมล็ดพันธุ์** the right register, or would plain **เมล็ดพันธุ์ของพระเจ้า** (locating the royal-only on "of God") read more naturally? The current rendering implicitly treats the seed as divine-by-extension; the alternative would treat it as a divine-possession.
2. Whether the πετρινε-corpus 1 PET 1:23 σπορά (related-but-distinct lemma) should also lock to **พระเมล็ดพันธุ์** for consistency, or whether σπορά (sowing-act, abstract) vs σπέρμα (seed, concrete) deserves a Thai distinction.

**→ Recommend: REVIEW (worth Ben's confirmation; verse-level rationale comprehensive enough that no corpus doc is required pre-tag).**

---

## 9. The present-vs-aorist ἁμαρτάνω — habitual-vs-occasional sin — **REVIEW (rationale comprehensive)**

1 John has a famous-internal-tension that English-Bible commentators have wrestled with for centuries:
- 1:8-10: "If we say we have no sin, we deceive ourselves" → ทำบาป
- 3:6, 9 + 5:18: "Whoever abides in him does not sin" / "cannot sin" → ไม่ได้ทำบาปต่อไป

The translator's solution: render the **present-tense ἁμαρτάνω** ("be-sinning" = ongoing-habitual) at 3:6, 9; 5:18 with the explicit **ไม่ได้ทำบาปต่อไป** ("does not continue-to-sin") — preserving the Greek tense-distinction that English typically renders identically as "does not sin" (creating the apparent contradiction).

**Verse-level evidence:**
- 1:8 ἐὰν εἴπωμεν ὅτι ἁμαρτίαν οὐκ ἔχομεν → **ถ้าเรากล่าวว่าเราไม่มีบาป** (existential-claim; sin-nature-denial)
- 1:10 ἐὰν εἴπωμεν ὅτι οὐχ ἡμαρτήκαμεν → **ถ้าเรากล่าวว่าเราไม่ได้ทำบาป** (perfect-claim; never-sinned-historic-denial)
- 3:6 πᾶς ὁ ἐν αὐτῷ μένων οὐχ ἁμαρτάνει → **ทุกคนที่คงอยู่ในพระองค์ก็ไม่ได้ทำบาปต่อไป** (present-habitual)
- 3:9 ἁμαρτίαν οὐ ποιεῖ ... οὐ δύναται ἁμαρτάνειν → **ก็ไม่ได้ทำบาปต่อไป ... ไม่สามารถทำบาปต่อไปได้** (present-habitual + present-infinitive)
- 5:18 ὁ γεγεννημένος ἐκ τοῦ θεοῦ οὐχ ἁμαρτάνει → **ทุกคนที่ได้บังเกิดจากพระเจ้าก็ไม่ได้ทำบาปต่อไป** (present-habitual)

The 3:6 KD + thai_summary explicitly explain the habitual-vs-momentary distinction for Thai readers:

> ข้อนี้ดูเหมือนจะขัดแย้งกับ 1 ยอห์น 1:8-10 ... การตีความที่ดีที่สุดคือ — กริยาในข้อนี้เป็นรูปปัจจุบัน (present tense) ในภาษากรีก ซึ่งหมายถึง 'การกระทำที่ดำเนินอย่างต่อเนื่อง' ผู้ที่อยู่ในพระคริสต์อาจสะดุดล้มเป็นบาปได้ในครั้งคราว แต่จะไม่ดำเนินชีวิตในความบาปอย่างเป็นนิสัย

**Editorial assessment:** The **ไม่ได้ทำบาปต่อไป** rendering ("does not continue to sin") is a principled Thai-grammatical solution to a Greek-Aktionsart distinction. It avoids the apparent contradiction that an unmarked Thai rendering would create (matching the apparent-contradiction problem in unmarked English). The thai_summary at 3:6 makes the principle explicit for Thai readers.

**REVIEW flag — Ben's confirmation worth getting on:**
1. Is **ไม่ได้ทำบาปต่อไป** the right Johannine-default? It is interpretive (committing to the habitual-aspect reading), but the alternative (plain **ไม่ทำบาป** matching 1:10's perfect-tense rendering) would import the apparent-contradiction problem into Thai.
2. Whether the principle should be made explicit in `docs/translator_decisions/aspect_johannine_habitual_2026-05.md` or whether the verse-level rationale at 3:6 + 5:18 is comprehensive enough.

**→ Recommend: REVIEW (verse-level rationale + thai_summary comprehensive; corpus doc OPTIONAL but useful pre-Revelation, where ἁμαρτάνω-aspect recurs).**

---

## 10. The Comma Johanneum at 5:7-8 — textual-criticism handling — **LOCKED ✓**

1 JN 5:7-8 is the locus-classicus of the **Comma Johanneum** — the trinitarian-formula interpolation that KJV / THKJV preserve but SBLGNT / NA28 / UBS5 / modern translations omit. The translator's handling perfectly implements `inclusion_variants_absent_verses_2026-04.md` Path A (Tier 2 footer):

**Main flow** (no Comma-text):
- 5:7 → **เพราะมีพยานสามฝ่าย** (bare "for there are three witnesses")
- 5:8 → **คือพระวิญญาณ น้ำ และโลหิต และทั้งสามฝ่ายนี้ก็เห็นเป็นหนึ่งเดียวกัน** ("namely Spirit, water, and blood — and these three are unanimous in their testimony")

**Footer file** (`output/textual_variants/1john_05.json`):
- Full Greek + Thai of the omitted trinitarian-formula clause (ἐν τῷ οὐρανῷ· ὁ Πατήρ, ὁ Λόγος, καὶ τὸ Ἅγιον Πνεῦμα ...)
- Witness lists (𝔓⁷⁴, ℵ, A, B vs late-MS-only inclusion + Vulgate-only + KJV)
- Erasmus 1522 history (added to 3rd edition under ecclesiastical pressure; copied from Latin)
- Cross-references to MAT 28:19 (Trinitarian baptism) + JHN 1:1 (Word-and-God) showing Trinitarian doctrine's independence from this verse

The 5:7 KD + thai_summary make the textual situation transparent for Thai readers (THKJV-tradition includes; modern critical-text + THSV omit). The 5:8 KD additionally clarifies that **εἰς τὸ ἕν → เห็นเป็นหนึ่งเดียวกัน** preserves the unity-of-testimony sense (NOT the ontological-unity sense, which would be the Comma's Trinitarian reading).

**Editorial assessment:** Textbook compliance with the locked Path A policy. The 1JN 5:7 case is the highest-stakes Tier 2 case in the entire NT (most-famous textual variant in Christian-translation history); the implementation is faithful to RULES §0 + the inclusion-variants doc.

**LOCKED ✓** per `inclusion_variants_absent_verses_2026-04.md`. The Tier 2 footer rendering is the canonical-precedent case for the doc's Path A choice (see `docs/end_of_book/matthew/MAT_END_OF_BOOK_REVIEW_2026-04-19.md` for the original options-A/B/C deliberation, where Option B was rejected specifically to avoid bracket-printing the Comma).

---

## 11. ἱλασμός extent at 2:2 — Calvinist-Arminian crux — **DECIDE (ambiguity preserved)**

1 JN 2:2 contains the canonical-evangelical-Protestant Calvinist-Arminian cleavage point:

> καὶ αὐτὸς ἱλασμός ἐστιν περὶ τῶν ἁμαρτιῶν ἡμῶν, οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ περὶ ὅλου τοῦ κόσμου
> และพระองค์เองทรงเป็นเครื่องบูชาไถ่บาปของเราทั้งหลาย และไม่เพียงเฉพาะของเราเท่านั้น แต่เป็นเครื่องบูชาไถ่บาปของคนทั้งโลกด้วย

The 2:2 KD invokes `petrine_eschatological_disambiguation_2026-05.md`:

> Per petrine_eschatological_disambiguation_2026-05.md: PRESERVE-AMBIGUITY (both Calvinist + Arminian readings exegetically defensible — neither contradicts canonical Scripture).

The 2:2 thai_summary documents both options explicitly:

> ข้อนี้สามารถตีความได้ 2 แบบเกี่ยวกับขอบเขตของการไถ่บาป — (1) ลัทธิ Calvinism มองว่า 'คนทั้งโลก' หมายถึงผู้ที่ทรงเลือกสรรไว้จากทุกชนชาติ ... (2) ลัทธิ Arminianism มองว่า 'คนทั้งโลก' หมายถึงทุกคนทั่วโลกที่พระคริสต์ทรงไถ่บาปสำหรับทุกคน ... ทั้งสองมุมมองยืนยันว่าการสิ้นพระชนม์ของพระคริสต์เพียงพอสำหรับทั้งโลก แต่มีประสิทธิผลสำหรับผู้ที่เชื่อเท่านั้น

**Editorial assessment:** The translator extends the locked `petrine_eschatological_disambiguation_2026-05.md` "preserve-ambiguity" principle from eschatology (where it was originally formulated, 1 PET 3:19) to **soteriology** (here, the extent-of-the-atonement). The principle is the same: both readings are exegetically irreducible and canonically-defensible; neither contradicts broader-Scripture; therefore preserve ambiguity at the main-text level (rendering literally **คนทั้งโลก** "the whole-world") + document both options in thai_summary.

**DECIDE flag — Ben's call:**
1. **Should `petrine_eschatological_disambiguation_2026-05.md` be amended to explicitly include soteriological-extent passages**, or should a new doc `docs/translator_decisions/atonement_extent_disambiguation_2026-05.md` be written? The 2:2 case is the densest soteriology-extent crux in the NT corpus; future cases include 2 PET 3:9 (already covered); 1 TIM 2:4-6; Heb 2:9; JHN 1:29; JHN 3:16. A unified disambiguation-doctrine doc would govern all of them.
2. **Is the thai_summary's framing acceptable?** The current summary names "ลัทธิ Calvinism" / "ลัทธิ Arminianism" — same critique as the 2 PET 3:9 audit (which Gemini + ChatGPT both flagged for tone-revision toward neutral descriptive language: "some interpret as the elect; others as all people"). Recommend adopting the same neutral-framing here (drop the -ism labels; describe the readings instead).

---

## 12. Chapter-5 dense-theology DECIDE cluster — 5:6 / 5:16 / 5:20

1 John 5 is the densest theological-crux chapter in the entire epistle. Three contested passages cluster here, all relying on the locked `petrine_eschatological_disambiguation_2026-05.md` "preserve-ambiguity" principle (extended from eschatology to broader-doctrinal-questions):

### 12a. ὕδωρ + αἷμα at 5:6 — **REVIEW (rationale comprehensive)**

> Οὗτός ἐστιν ὁ ἐλθὼν δι' ὕδατος καὶ αἵματος, Ἰησοῦς Χριστός
> ผู้นี้แหละคือผู้ที่ได้เสด็จมาโดยทางน้ำและโลหิต คือพระเยซูคริสต์

3 mainstream interpretations preserved in thai_summary:
- (1) water = baptism (Jordan); blood = cross (Calvary). Most-common.
- (2) water + blood = the side-pierced fluids at JHN 19:34.
- (3) water = birth (incarnation); blood = death.

The not-by-water-only emphasis explicitly counters Cerinthian-Christology (Christ left-Jesus-before-the-cross). Verse-level KD + thai_summary cover all three options.

**Recommend: REVIEW (worth Ben's confirmation that 3-way ambiguity-preservation is right; the option-(1) is mainstream-evangelical).**

### 12b. ἁμαρτία πρὸς θάνατον at 5:16 — **DECIDE**

> ἔστιν ἁμαρτία πρὸς θάνατον· οὐ περὶ ἐκείνης λέγω ἵνα ἐρωτήσῃ
> มีบาปที่ถึงตาย ข้าพเจ้าไม่ได้กล่าวว่าให้ทูลขอเกี่ยวกับบาปนั้น

The 5:16 KD invokes `petrine_eschatological_disambiguation_2026-05.md` "preserve-ambiguity" — the thai_summary documents 3 mainstream readings:
- (1) **Apostasy** (permanent abandonment of faith — Heb 6:4-6; 10:26-27).
- (2) **Continuous Christ-rejection / sin-against-the-Holy-Spirit** (Matt 12:31).
- (3) **Physical-death-discipline** (1 Cor 11:30; Acts 5:1-11 Ananias-and-Sapphira).

**DECIDE flag — Ben's call:**
1. Is the 3-way ambiguity-preservation strategy correct, or should the translator commit to one reading? The mainstream-evangelical-Protestant default tends toward (1) apostasy, but with significant minority support for (2) and (3).
2. Should this be added to the locked `petrine_eschatological_disambiguation_2026-05.md` doc as another anchor passage (extending the principle from 1 PET 3:19 + 1 PET 4:6 + 2 PET 3:9 + 1 JN 2:2 + 1 JN 5:16)?

### 12c. οὗτός ἐστιν ὁ ἀληθινὸς θεὸς at 5:20 — **DECIDE (currently committed to high-Christology)**

> οὗτός ἐστιν ὁ ἀληθινὸς θεὸς καὶ ζωὴ αἰώνιος
> ผู้นี้แหละเป็นพระเจ้าเที่ยงแท้และเป็นชีวิตนิรันดร์

The 5:20 KD invokes `pastoral_corpus_locks_2026-05.md §C` (high-Christology + scholarly-consensus) for the **οὗτος-refers-to-Jesus-Christ** reading (the immediate-antecedent grammar — same lemma-class as the Granville-Sharp constructions in 2 PET 1:1; 1:11; etc.). The thai_summary explains both options (Christ vs Father) but the main text commits to high-Christology (Jesus = "the true God and eternal life").

**Editorial assessment:** This is a conscious editorial commitment — the alternative reading (οὗτος = the Father) would require slightly different Thai phrasing (something like **ผู้นั้นเป็นพระเจ้าเที่ยงแท้** with disambiguating-distance from Christ-anaphora). The current rendering matches NIV / ESV / CSB / NASB English mainstream, and matches the JHN 1:1 + JHN 20:28 ("my Lord and my God") high-Christology corpus-internal-pattern.

**DECIDE flag — Ben's call:** Is the **high-Christology commitment** (Jesus = the true-God + eternal-life) the right Johannine-corpus default at 5:20? It is mainstream-evangelical-Protestant + scholarly-consensus + grammatically-natural (immediate-antecedent), but it commits more-explicitly than the literal-Greek-reader would receive (where οὗτος in absence of a disambiguation-marker is technically ambiguous between the two preceding masculine-singular antecedents — Jesus Christ and the True-One = the Father). Recommend confirming + lifting to a brief doc.

**→ Recommend: amend** `pastoral_corpus_locks_2026-05.md` with a §C-extension citing 1 JN 5:20 as a Johannine-corpus confirming-precedent for the Granville-Sharp / immediate-antecedent / high-Christology default. Or, write a brief new doc `docs/translator_decisions/houtos_ho_alethinos_theos_johannine_2026-05.md`.

---

## 13. Inherited locks — **all compliant**

| Doc | 1JN evidence | Status |
|---|---|---|
| `inclusion_variants_absent_verses_2026-04.md` (Path A) | 1JN 5:7-8 Comma Johanneum: main flow omits; Tier 2 footer in `output/textual_variants/1john_05.json` complete with witnesses + Erasmus history. **Most-famous Tier-2-case in the NT.** See §10. | **LOCKED ✓** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 1JN has minimal narrator-κύριος (the epistle is doctrinal-pastoral; "the Lord" appears infrequently — 1JN does not have a κύριος-narrative-voice cluster like Acts/Luke). N/A in this letter. | **LOCKED (N/A)** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for human-paternal-apostolic addresses (τεκνία → ลูกที่รัก at 2:1, 2:12, 2:28; 3:7, 18; 4:4; 5:21; παιδία → เด็ก at 2:14, 18; ἀγαπητοί → ท่านที่รัก throughout). The "father / fathers" addresses at 2:13-14 → **บิดา** (plain, addressing church-elders, NOT divine-Father). Compliant. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — the doubled-ἀμήν is a Synoptic-John-Jesus-direct-discourse pattern; 1 JN has no Jesus-direct-discourse. | **LOCKED (N/A)** |
| `parousia_christou_2026-05.md` | 1JN 2:28 (ἐν τῇ παρουσίᾳ αὐτοῦ → **ในการเสด็จมาของพระองค์**) — Christ-subject, royal register **การเสด็จมา**. Compliant with the lock. The single παρουσία occurrence in 1 JN. | **LOCKED ✓** |
| `petrine_eschatological_disambiguation_2026-05.md` | Invoked at 1JN 2:2 (atonement-extent), 5:6 (water+blood readings), 5:16 (sin-unto-death), 2:18 (antichrist singular-vs-plural). The 1JN audit broadens the doc's scope from eschatology to broader-doctrinal-disambiguation — see §11 + §12. | **LOCKED-with-amendment-recommended** (extend doc-scope to soteriology + Christology) |
| `pastoral_corpus_locks_2026-05.md` §C (high-Christology) | Invoked at 1JN 5:20 (οὗτος = Christ; Granville-Sharp / immediate-antecedent rule). Compliant. See §12c. | **LOCKED ✓** |
| `pagan_deities_2026-04.md` | 1JN 5:21 (φυλάξατε ἑαυτὰ ἀπὸ τῶν εἰδώλων → **จงปกป้องตนให้พ้นจากรูปเคารพ**) — pagan-εἴδωλα → **รูπเคารพ** (NOT พระ-prefixed; not deity-class register). Compliant. | **LOCKED ✓** |
| `divine_object_praise_verbs_2026-04.md` | N/A in 1JN — no doxological praise-verb-with-God-object constructions in this letter. | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in 1JN — no vocative κύριε / διδάσκαλε in this letter. | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | N/A in 1JN — no Roman / Jewish / civic honorifics. The Cain reference at 3:12 → **คาอิน** (plain transliteration, no honorific). Compliant. | **LOCKED ✓** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic embeds in 1 JN. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 1 JN is doctrinal-pastoral, not narrative; no historic-present pattern. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 1 JN. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from 1 JN (the conversion-vocabulary is generally absent — 1 JN's atonement-language is ἱλασμός + καθαρίζω + ἀφίημι, NOT explicit μετανοέω). | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | 1JN 1:9 (ἵνα ἀφῇ ἡμῖν τὰς ἁμαρτίας → **ทรงอภัยบาปของเรา**) and 2:12 (ἀφέωνται ὑμῖν αἱ ἁμαρτίαι → **บาปของท่านได้รับการอภัยแล้ว**) — verb-form ἀφίημι uniformly **อภัย** + royal-prefix **ทรง-** when God-subject. Compliant. The substantival-noun ἄφεσις is absent from 1 JN. | **LOCKED ✓** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 1 JN. The Christological titles in 1 JN are υἱὸς θεοῦ (4:15; 5:5, 10, 12, 13, 20) → **พระบุตรของพระเจ้า** uniformly. Distinct from-but-compatible-with the locked Son-of-Man rule. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (implicitly at 4:13 → **พระวิญญาณ** — divine-Spirit royal-prefix); ψυχή at 3:16 (Christ ↔ believer life-laying-down) — **dual-rendering** preserved (royal **พระชนม์** for Christ's-life; plain **ชีวิต** for believer's-life). Compliant with the locked split + matches the JHN 10:11 / 15:13 corpus-pattern. | **LOCKED ✓** |
| `ouranos_heaven_rendering_2026-04.md` | N/A — οὐρανός absent from 1 JN main flow (only in the omitted-Comma at 5:7 ἐν τῷ οὐρανῷ, which is footer-not-main). | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` / `markan_euthys_immediately_2026-04.md` | N/A — Mark/Acts-specific. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries in 1 JN. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A — βασιλεία absent from 1 JN (the Johannine-letters generally lack kingdom-language). | **LOCKED (N/A)** |
| `ekklesia_2026-04.md` | N/A — ἐκκλησία absent from 1 JN main flow (3 JN 6, 9, 10 has it; not 1 JN). | **LOCKED (N/A)** |
| `ethnos_2026-04.md` | N/A — ἔθνος absent from 1 JN. | **LOCKED (N/A)** |
| `spiritual_beings_hierarchy_2026-05.md` | N/A — Pauline-cosmology terms (ἀρχαί / κυριότητες / etc.) absent from 1 JN. The διάβολος (3:8, 10) → **มาร** + ὁ πονηρός (2:13-14; 3:12; 5:18, 19) → **มารร้าย** are in the related-but-distinct devil/evil-one register; compliant with the spiritual_beings doc's scope. | **LOCKED (N/A for cosmology terms; LOCKED for satanic-figures)** |
| `christ_hymn_kenosis_2026-05.md`, `dikaioo_dikaiosyne_family_2026-05.md`, `huiothesia_adoption_2026-05.md`, `nomos_pauline_2026-05.md`, `phroneo_pauline_2026-05.md`, `pistis_christou_2026-05.md`, `prototokos_pauline_2026-05.md`, `sarx_pauline_2026-05.md`, `stoicheia_tou_kosmou_2026-05.md`, `telos_paidagogos_christ_2026-05.md`, `proper_noun_wordplay_2026-05.md`, `epiphaneia_christou_2026-05.md`, `hygiaino_sound_doctrine_2026-05.md`, `diakonos_pauline_2026-05.md`, `parepidemos_paroikos_sojourner_2026-05.md`, `poimen_episkopos_register_split_2026-05.md`, `pascho_pathema_suffering_2026-05.md`, `porneia_vs_moicheia_DEFERRED_2026-05.md` | N/A in 1 JN (Pauline-corpus-specific or Pastoral / 1 PET-corpus-specific; lemmas absent or non-applicable in Johannine epistolary). | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in 1 JN). | **LOCKED (N/A)** |

---

## 14. δίκαιος + δικαιοσύνη — Christological-title cluster — **STABLE (extends Pauline pattern)**

1 JN has 3 occurrences of δίκαιος in the **Christological-title** sense (vs the Pauline-soteriological-noun sense covered by `dikaioo_dikaiosyne_family_2026-05.md`):

| Verse | Greek | Thai |
|---|---|---|
| 1:9 | πιστός ἐστιν καὶ δίκαιος | **ทรงสัตย์ซื่อและทรงชอบธรรม** (paired-divine-attributes; royal-prefix) |
| 2:1 | Ἰησοῦν Χριστὸν δίκαιον | **พระเยซูคริสต์ผู้ทรงชอบธรรม** (Christological-title; royal-prefix) |
| 2:29 / 3:7 | ἐκεῖνος δίκαιός ἐστιν | **พระองค์ทรงชอบธรรม / เหมือนพระองค์ทรงชอบธรรม** (Christological-attribute) |

Plus the substantival-derivative δικαιοσύνη at 2:29; 3:7, 10 → **ความชอบธρρม** (state-noun) / ποιεῖν τὴν δικαιοσύνην → **ประพฤติชอบธรรม** (verbal-construction; "do righteousness").

**Editorial assessment:** Compliance with the Pauline-corpus `dikaioo_dikaiosyne_family_2026-05.md` is exact — the substantival ความชอบธρρม + the verbal ประพฤติชอบธρρม + the Christological-title ผู้ทρงชอบธρρม form a principled three-form cluster. The royal-prefix ทรง- on δίκαιος as a divine-attribute is consistent with the broader divine-attribute-as-title corpus pattern.

**Recommend: STABLE — no new doc needed.** Existing `dikaioo_dikaiosyne_family_2026-05.md` covers the principle. Worth a one-line cross-reference in any future Johannine-corpus extension noting 1 JN compliance.

---

## Mechanical (§1) — **all green**

- 5/5 chapters: `output/check_reports/1john_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 5/5 chapters: `output/back_translations/1john_NN.json` ✓
- `output/textual_variants/1john_05.json` (Tier 2 Comma Johanneum footer) — present + complete ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-225-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7182 verses across 223 chapter files)
- `git status output/`: only re-ran-check artifacts (key_term_consistency_all.md count-update from re-running my §1 verification). No 1JN source-file dirt; the 5:7 textual_variants file is already committed.

---

## Pre-existing docs affirmed / unchanged

All 47 docs in `docs/translator_decisions/` reviewed. Compliance summary in §13 above. Two existing docs flagged for amendment-recommendation:
- **`petrine_eschatological_disambiguation_2026-05.md`** — extend doc-scope to explicitly include soteriology (atonement-extent at 2:2; sin-unto-death at 5:16) + the Christological-antecedent question at 5:20. The doc was originally formulated for eschatology only; 1 JN demonstrates its broader applicability.
- **`pastoral_corpus_locks_2026-05.md` §C** — add 1 JN 5:20 as a Johannine-corpus confirming-precedent for the high-Christology / Granville-Sharp / immediate-antecedent default.

No corpus doc requires verse-text revision in 1 JN.

---

## Flagged for Ben's attention

### A. ἀγάπη / ἀγαπάω uniform rendering — **STABLE, consider corpus doc** (§1)
Lift to corpus doc `agape_johannine_2026-05.md` BEFORE 2 JN + 3 JN ship (where ἀγάπη / ἀγαπητός recurs in salutations). The 1JN 4:8 / 4:16 ontological-confession **พระเจ้าทรงเป็นความรัก** is the locking-precedent.

### B. ἀντίχριστος rendering (ผู้ต่อต้านพระคริสต์) — **STABLE, lift to corpus doc** (§2)
Lift to corpus doc `antichristos_johannine_2026-05.md` BEFORE 2 JN ships. Note the singular-future + plural-present preserve-ambiguity rule.

### C. ἱλασμός + cognate-ἱλαστήριον locking — **STABLE, lift to corpus doc** (§3)
Lift to corpus doc `hilasmos_hilasterion_atonement_2026-05.md` to formalize the cognate-locking with Rom 3:25 + Heb 9:5 + Heb 2:17 ἱλάσκομαι. Pre-Hebrews ship priority.

### D. χρῖσμα anointing — **STABLE, consider brief doc** (§4)
Brief corpus doc would lock χρῖσμα → **การเจิม** + cross-reference the cognate Christological-title χριστός → **พระคริสต์** + the verbal χρίω.

### E. μένω Johannine-keyword "abide" — **STABLE, lift to corpus doc** (§5)
Lift to corpus doc `meno_johannine_abide_2026-05.md` BEFORE 2 JN + 3 JN + Revelation. The 1JN 4:13-16 triple-μένω structure is the locking-precedent.

### F. γεγεννημένος ἐκ τοῦ θεοῦ + the perfect-vs-aorist Christ-distinction at 5:18 — **STABLE, lift to corpus doc** (§6)
Lift to corpus doc `gegenneménos_ek_theou_johannine_2026-05.md`. The 5:18 royal-prefix-only-on-aorist-pcpl-for-Christ rendering is the most editorially-distinctive move in 1 JN; doc-lift will preserve this pattern in 2 JN + 3 JN + Revelation 12:5; 12:13.

### G. παράκλητος Christ-vs-Spirit dual-referent — **LOCKED; consider brief doc amendment** (§7)
A brief corpus doc would surface the cross-corpus Christ-Spirit dual-referent rule for future readers / external reviewers.

### H. σπέρμα-of-God metaphor at 3:9 — **REVIEW** (§8)
Worth Ben's confirmation that the royal-prefix on **พระเมล็ดพันธุ์** is the right register (vs plain เมล็ดพันธุ์ของพระเจ้า).

### I. Present-vs-aorist ἁμาρτάνω (habitual-vs-occasional) at 3:6, 9; 5:18 — **REVIEW** (§9)
Worth Ben's confirmation that **ไม่ได้ทำบาπต่อไป** (interpretive present-tense) is the right Johannine-default.

### J. Comma Johanneum at 5:7-8 — **LOCKED ✓** (§10)
Textbook implementation of `inclusion_variants_absent_verses_2026-04.md` Path A. No action needed; flag for Ben's confirmation only that the highest-stakes Tier-2 case is correctly handled.

### K. ἱλασμός extent at 2:2 (Calvinist-Arminian crux) — **DECIDE** (§11)
1. Should the locked `petrine_eschatological_disambiguation_2026-05.md` doc be extended to atonement-extent passages, or written as a new doc?
2. Adopt the same neutral-framing as 2 PET 3:9 (drop "ลัทธิ Calvinism / Arminianism" labels in thai_summary; describe the readings).

### L. ἁμาρτία πρὸς θάνατον at 5:16 — **DECIDE** (§12b)
1. Confirm the 3-way ambiguity-preservation strategy (apostasy / continuous-rejection / physical-discipline).
2. Add 5:16 as another anchor to `petrine_eschatological_disambiguation_2026-05.md`.

### M. οὗτός ἐστιν ὁ ἀληθινὸς θεός at 5:20 — **DECIDE** (§12c)
1. Confirm the high-Christology commitment (Jesus = the true-God + eternal-life).
2. Amend `pastoral_corpus_locks_2026-05.md` §C with 5:20 as a Johannine-corpus confirming-precedent, OR write brief new doc.

### N. New corpus docs to write (before 2 JN + 3 JN + Revelation)
1. **`docs/translator_decisions/antichristos_johannine_2026-05.md`** (§B) — locks **ผู้ต่อต้านพระคริสต์** rendering (BEFORE 2 JN 7)
2. **`docs/translator_decisions/hilasmos_hilasterion_atonement_2026-05.md`** (§C) — locks the atonement-noun cluster (pre-Hebrews)
3. **`docs/translator_decisions/meno_johannine_abide_2026-05.md`** (§E) — locks **คงอยู่** (BEFORE 2 JN + 3 JN + Revelation)
4. **`docs/translator_decisions/gegenneménos_ek_theou_johannine_2026-05.md`** (§F) — locks the perfect-vs-aorist distinction (BEFORE 2 JN + 3 JN + Revelation)
5. **(Optional)** `agape_johannine_2026-05.md` (§A) — locks the love-cluster
6. **(Optional)** `chrisma_anointing_2026-05.md` (§D) — brief; locks χρῖσμα cluster
7. **(Optional)** `paraklētos_christological_pneumatological_2026-05.md` (§G) — brief; locks the Christ-Spirit dual-referent rule

### O. Existing docs to amend
- **`petrine_eschatological_disambiguation_2026-05.md`** — extend scope to soteriology + Christology (anchor passages: 1 JN 2:2, 5:16, 5:20).
- **`pastoral_corpus_locks_2026-05.md` §C** — add 1 JN 5:20 as Johannine-corpus confirming-precedent.

### P. External AI review (§3 of checklist) — **pending**
Recommended before `book-1john-v1` tag. Suggested 4-cluster external AI packet:
1. **1JN 1:1-10** — anti-Docetic prologue + sin-claims test
2. **1JN 2:1-2 + 4:10** — ἱλασμός atonement-noun + the 2:2 extent crux
3. **1JN 2:18-27 + 4:1-6** — ἀντίχριστος + χρῖσμα + the σὰρξ-ἐληλυθότα anti-Cerinthian test
4. **1JN 5:6-8 + 5:16-21** — water+blood + Comma Johanneum disposition + sin-unto-death + the high-Christology 5:20 climax

Use ChatGPT + Gemini in parallel per the JHN/GAL/2PE pattern.

---

## Recommendation

**1 John ships in strong corpus-hygiene shape — and provides the Catholic-Epistles Johannine-vocabulary entry-point for the corpus.** The translator made consistent, principled choices on the four most-significant 1JN-introduced lemma-clusters (ἀντίχριστος; ἱλασμός; χρῖσμα; γεγεννημένος ἐκ θεοῦ — with the brilliant perfect-vs-aorist Christ-distinction at 5:18) — and **none of these four has a corpus-level doc** yet. This is the moment to lock them in before 2 JN + 3 JN compound the editorial weight (esp. the 2 JN 7 ἀντίχριστος + the 2 JN 5-6 ἀγάπη / ἐντολή recurrences).

The chapter-5 dense-theology cluster (§§11-12) is the highest-stakes set of editorial decisions in the entire epistle — three ambiguity-preservation cases (2:2 atonement-extent; 5:6 water+blood; 5:16 sin-unto-death) + one explicit high-Christology commitment (5:20). All four hinge on `petrine_eschatological_disambiguation_2026-05.md` and `pastoral_corpus_locks_2026-05.md §C` — both originally written for narrower scopes that 1 JN now broadens. **Both docs should be amended before tagging.**

Tag `book-1john-v1` after:
1. Ben's decisions on **§K + §L + §M** (DECIDE items: 2:2 atonement-extent disambiguation strategy; 5:16 sin-unto-death ambiguity; 5:20 high-Christology commitment)
2. Ben's confirmation on **§H + §I** (REVIEW items: σπέρμα-prefix-register at 3:9; present-tense interpretive-rendering of ἁμαρτάνω)
3. Three-to-four new translator_decisions docs written (§N items 1-4 minimum; optionally 5-7)
4. Two existing docs amended (`petrine_eschatological_disambiguation_2026-05.md` scope-extension; `pastoral_corpus_locks_2026-05.md` §C 1JN-confirming-precedent)
5. External AI sanity-check (§P) — items A-G in `external_review_items_1JN.md`

The Johannine-letters short-corpus (2 JN 13 verses; 3 JN 14 verses) can be queued for next; writing `antichristos_johannine`, `meno_johannine_abide`, and `gegenneménos_ek_theou_johannine` docs **before 2 JN ships** will avoid forward drift on the three densest Johannine-corpus-cross-cutting patterns.
