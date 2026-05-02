# Philippians — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 4 chapters (104 verses; ~280 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (31 docs).
**Trigger:** PHP 4 shipped (commit `3442c59`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 4/4 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-123-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book philippians --strict` exits 0 (the 4:23 final-ἀμήν resolved via `output/textual_variants/_resolved/philippians_04_final_amen.md`); `export_to_usfm.py --book PHP` regenerates `output/paratext/PHP.SFM` cleanly. `git status output/` clean.
- **Philippians is the FIRST PRISON-EPISTLE the project has shipped** (the Captivity-Letters cluster: PHP, Eph, Col, PHM — though PHM shipped earlier on the personal-letter track). At 104 verses Philippians is short, dense, and **the most lexically distinctive Pauline letter so far**: ~30 NT-HAPAXES across 4 chapters (Pauline-corpus densest), a self-contained Christological hymn (2:5–11), Greek-philosophical virtue-vocabulary (3:13–14 athletic-runner; 4:8 virtue-list; 4:11 αὐτάρκης Stoic-borrowing), and a deliberate Pauline-pun-and-wordplay register (3:2 κατατομή/περιτομή; 3:8 σκύβαλον; 2:2 σύμψυχος + 2:20 ἰσόψυχος + 2:19 εὐψυχέω + 4:3 σύζυγος; 4:18 cultic-language reframing).
- **Cross-cutting Pauline-vocabulary inheritance verified compliant** with prior locks: ἐκκλησία (1 occ., 3:6 — LOCKED ✓), δοῦλος → ทาส (1:1 — LOCKED ✓), διάκονος → ผู้รับใช้ (1:1 plural; pairs with ἐπίσκοπος; LOCKED via `diakonos_pauline_2026-05.md`), δικαιοσύνη → ความชอบธรรม (1:11; 3:6, 9 — LOCKED via `dikaioo_dikaiosyne_family_2026-05.md`), νόμος → ธรรมบัญญัติ (3:5, 6, 9 — LOCKED via `nomos_pauline_2026-05.md`), ἅγιος → ธรรมิกชน (1:1, 4:21, 4:22 — LOCKED, matches the Matthew/Acts/Romans/Philemon corpus default).
- **The single most editorially-LOAD-BEARING item in the book is the Christ-Hymn (2:5–11):** doctrinally orthodox kenotic-Christology with high-Christology climax, deliberate μορφή-σχῆμα distinction preserved, ἁρπαγμός rendered "to-be-clung-to" (eVangelical-Protestant majority), Isa 45:23 LXX echo at vv.10–11 logged as OT-allusion, the 2:11 κύριος Ἰησοῦς Χριστός confession rendered with the locked organization-of-divine-name. **No corpus doc** for the hymn yet — recommend `christ_hymn_kenosis_2026-05.md` lifting now (before the parallel passages at Col 1:15–20, 1 Tim 3:16, Heb 1:1–4 ship).
- **6 cross-cutting Pauline patterns are STABLE-but-undocumented** (the kenosis-hymn vocabulary; φρονέω as Philippians-signature-keyword; the χαρά / χαίρω joy-saturated theme; σάρξ-polysemy resolved chapter-by-chapter; ταπεινόω-polysemy spanning 2:8 ↔ 4:12; πολιτεύομαι/πολίτευμα citizenship cluster).
- **3 items flagged REVIEW** (ἁρπαγμός 2:6 evangelical-default rendering ‘สิ่งที่ต้องยึดไว้’; πραιτώριον 1:13 Praetorian-Guard contextual gloss vs the MRK/JHN/ACT precedent; παρουσία 1:26 non-eschatological-visit sense vs the 1TH-locked eschatological-coming).
- **3 items flagged DECIDE** (πίστις Χριστοῦ 3:9 objective-vs-subjective genitive; σύζυγος 4:3 common-noun-vs-proper-name; σκύβαλον 3:8 register choice ‘เศษขยะ’ vs cruder LXX-period sense).
- **External AI review (§3) pending** — items doc + packet built in this branch.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. The Christ-Hymn (2:5–11) — kenosis-Christology vocabulary cluster — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

The single most theologically load-bearing passage in the book and a Christological-cornerstone for the entire NT. The hymn divides into descent (vv.6–8) and ascent (vv.9–11). The verse-level KDs render every doctrinally-loaded lemma with a **principled, evangelical-Protestant orthodox** rendering. There is **no corpus doc** capturing the cluster — and yet it sets precedent for the parallel high-Christology passages that the corpus will encounter ahead (Col 1:15–20 πρωτότοκος / πληρώματα / θρόνοι; 1 Tim 3:16 ἐφανερώθη ἐν σαρκί; Heb 1:1–4 ἀπαύγασμα τῆς δόξης / χαρακτὴρ τῆς ὑποστάσεως; Eph 1:20–23 / 1 Pet 3:22 / Rev 5:12–13).

| Greek (verse) | Thai | Editorial principle |
|---|---|---|
| **μορφῇ θεοῦ** ὑπάρχων (2:6) | ผู้ทรงดำรงอยู่ใน**สภาพของพระเจ้า** | μορφή = essential-nature, NOT outward appearance (Paul reserves σχῆμα for that, v.7). **สภาพ** preserves the essence-claim. Affirms Christ's full pre-existent divinity. |
| οὐχ **ἁρπαγμὸν** ἡγήσατο τὸ εἶναι ἴσα θεῷ (2:6) | มิได้ทรงถือว่าการเป็นเสมอกับพระเจ้า เป็น**สิ่งที่ต้องยึดไว้** | The classical-theological crux. "Held-onto" reading (res rapta — already possessed, chose not to cling-to/exploit) is the evangelical-Protestant majority. **REVIEW (§4)**. |
| ἑαυτὸν **ἐκένωσεν** (2:7) | ทรง**สละพระองค์เอง** | NOT "poured-out divinity" (kenotic-heresy Christology). **สละ** = "voluntarily-relinquished privileges." Per uW + corpus-evangelical orthodoxy. |
| **μορφὴν δούλου** λαβών (2:7) | ทรงรับ**สภาพของทาส** | Identical lemma-rendering with v.6 μορφή θεοῦ → **สภาพ** preserves the Pauline parallel-and-contrast structure (μορφή θεοῦ ↔ μορφή δούλου: both real-essence, not appearance). |
| ἐν **ὁμοιώματι** ἀνθρώπων γενόμενος (2:7) | ทรงบังเกิดใน**ลักษณะ**ของมนุษย์ | "Real-likeness," NOT mere docetic-appearance. ลักษณะ retains the genuine-human-nature claim. |
| **σχήματι** εὑρεθεὶς ὡς ἄνθρωπος (2:7) | เมื่อทรงปรากฏใน**รูป**ของมนุษย์ | σχῆμα → **รูป** (outward-form) — distinct lexically from μορφή → **สภาพ**. Pauline-distinctive lemma-pair preserved. |
| **ἐταπείνωσεν ἑαυτὸν** (2:8) | ทรง**ถ่อมพระองค์**เองลง | Cognate verbal-link with v.3 ταπεινοφροσύνη ‘**ความถ่อมใจ**’ — Christ-paradigm grounds the believer-imperative. |
| γενόμενος ὑπήκοος μέχρι θανάτου, **θανάτου δὲ σταυροῦ** (2:8) | ทรงเชื่อฟังจนถึงความตาย **ใช่ ความตายบนกางเขน** | Emphatic δέ rendered with Thai **ใช่** (intensifying-particle). Climactic shame-of-cross emphasis preserved. |
| **διὸ καί** ὁ θεὸς αὐτὸν **ὑπερύψωσεν** (2:9) | **เพราะเหตุนี้** พระเจ้าจึงทรง**เทิดทูนพระองค์ขึ้นสู่ที่สูงสุด** | διό as result-conclusion preserved. ὑπερύψωσεν (NT-HAPAX, ὑπέρ-intensified) → **เทิดทูน...สู่ที่สูงสุด** — preserves the intensive-superlative force. |
| τὸ **ὄνομα τὸ ὑπὲρ πᾶν ὄνομα** (2:9) | **พระนามที่อยู่เหนือพระนามทั้งปวง** | The implicit "name" = κύριος (LXX-rendering of YHWH). Made explicit at v.11. |
| ἐν τῷ ὀνόματι Ἰησοῦ **πᾶν γόνυ κάμψῃ** ... καὶ **πᾶσα γλῶσσα ἐξομολογήσηται** (2:10–11) | ทุกหัวเข่าจะคุกลง ... ทุกลิ้นจะสารภาพยอมรับ | OT ALLUSION: Isa 45:23 LXX (Paul's deliberate Christological-application of YHWH-self-reference). LOGGED in `data/nt_ot_citations.json`. |
| **κύριος Ἰησοῦς Χριστός** (2:11) | พระเยซูคริสต์ทรงเป็น**องค์พระผู้เป็นเจ้า** | κύριος → **องค์พระผู้เป็นเจ้า** — earliest-known Christian creed-formula, deliberate divine-name application to Jesus per Pauline-corpus standard. |
| εἰς **δόξαν θεοῦ πατρός** (2:11) | เพื่อ**พระสิริของพระเจ้าพระบิดา** | Trinitarian closure — Father glorified BY Son's exaltation. Compliant with `narrator_vs_character_voice_2026-04.md`. |

**Editorial significance:** The hymn's vocabulary is the SOURCE for the Eastern (Cyrillic, Chalcedonian) and Western (Augustinian, Reformed) Christological tradition. Every rendering above is doctrinally orthodox AND lexically principled. The translator preserved the Pauline μορφή/σχῆμα distinction, the κενόω-as-self-renunciation reading, the ἁρπαγμός-as-res-rapta rendering, the OT-Isaiah-45 allusion, and the LXX-divine-name-application-to-Jesus.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/christ_hymn_kenosis_2026-05.md` before Col 1:15–20 (the next major Christological hymn) + 1 Tim 3:16 + Heb 1:1–4 + the Eph 1 / 1 Pet 3 / Rev 5 high-Christology passages. The doc should:
1. Lock μορφή → **สภาพ** (essential-nature) when the contrast with σχῆμα is in view
2. Lock σχῆμα → **รูป** (outward-form) when the contrast with μορφή is in view
3. Lock κενόω (self-emptying-of-Christ context) → **ทรงสละพระองค์เอง** + the orthodox-rendering principle (NOT "poured-out divinity")
4. Lock ὑπερυψόω (sole NT occurrence) → **เทิดทูน...สู่ที่สูงสุด**
5. Cite PHP 2:5–11 as the locking precedent
6. Cross-reference the parallel high-Christology passages (Col 1:15–20; 1 Tim 3:16; Heb 1:1–4; Eph 1:20–23; 1 Pet 3:18–22; Rev 5:9–14) as forward-pertinent
7. Note the ἁρπαγμός decision (REVIEW item, see §4) as the still-open question pending external AI affirmation

---

## 2. φρονέω — Philippians-signature mindset-keyword — **STABLE (undocumented; recommend new doc)**

φρονέω occurs **10× in PHP** (1:7; 2:2 ×2; 2:5; 3:15 ×2; 3:19; 4:2; 4:10 ×2) — by far the densest distribution in any NT book. The verb organizes the letter's ethical-pastoral spine: think rightly together, model your mindset on Christ, beware those whose minds are set on earthly things, agree in the Lord. The renderings split contextually:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:7 | τοῦτο φρονεῖν ὑπὲρ πάντων ὑμῶν | **คิดถึงพวกท่านทุกคนเช่นนี้** | affectionate-devotional thinking-of |
| 2:2 | τὸ αὐτὸ φρονῆτε | มีความ**คิด**อย่างเดียวกัน | corporate-unified mindset |
| 2:2 | τὸ ἓν φρονοῦντες | **คิด**เป็นน้ำหนึ่งใจเดียวกัน | climactic-intensified unity-of-mind |
| 2:5 | τοῦτο φρονεῖτε ἐν ὑμῖν ὃ καὶ ἐν Χριστῷ Ἰησοῦ | จงมี**จิตใจ**อย่างนี้ในพวกท่าน | Christ-paradigmatic disposition (φρόνημα-noun-form-implied) |
| 3:15 (×2) | τοῦτο φρονῶμεν · καὶ εἴ τι ἑτέρως φρονεῖτε | **คิด**อย่างนี้เถิด ... **คิด**เรื่องใดอย่างอื่น | mature-Christian conviction |
| 3:19 | οἱ τὰ ἐπίγεια φρονοῦντες | พวกเขา**คิด**แต่เรื่องของโลกนี้ | mind-set-on-earthly-things (negative) |
| 4:2 | τὸ αὐτὸ φρονεῖν ἐν κυρίῳ | **คิด**อย่างเดียวกันในองค์พระผู้เป็นเจ้า | Euodia + Syntyche unity-imperative |
| 4:10 (×2) | ἀνεθάλετε τὸ ὑπὲρ ἐμοῦ φρονεῖν, ἐφ' ᾧ καὶ ἐφρονεῖτε | กลับมาแสดง**ความห่วงใย** ... **ห่วงใย** | concern / care-for (semantic specialization) |

**Editorial assessment:** The translator handled the polysemy principled-ly: **คิด** for general "think" + **จิตใจ** for "disposition / mindset" (2:5) + **ความห่วงใย / ห่วงใย** for "concern-for" (4:10). This is correct contextual-semantic disambiguation, not lemma-drift. The signature verbal-link between 2:5 (Christ-mindset imperative) → 2:6–11 (the hymn unfolding what that mindset is) → 3:15 (mature-Christian mind) → 4:2 (Euodia/Syntyche particularization) is preserved.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/phroneo_pauline_2026-05.md`. The lemma is dense in Pauline ethics-of-the-mind passages (Rom 8:5–7 Pauline-density "the mind of the flesh / the mind of the spirit"; Rom 12:3 / 12:16; 14:6; 15:5; 1 Cor 13:11; 2 Cor 13:11; Gal 5:10; Col 3:2 — the densest Pauline cluster after PHP). The doc should:
1. Lock φρονέω (general "think" / "consider") → **คิด**
2. Lock φρονέω (mindset / disposition / settled-attitude) → **จิตใจ** + verbal periphrasis as needed
3. Lock φρονέω (concern-for, care-about) → **ห่วงใย** (PHP 4:10 style)
4. Note the noun φρόνημα as related-distinct lemma (Rom 8:6, 7, 27 — not yet shipped; will need its own decision)
5. Cite PHP 2:2, 2:5, 3:19, 4:2 as the locking precedents
6. Cross-reference the Col 3:2 forward-Pauline imperative (τὰ ἄνω φρονεῖτε) which mirrors PHP 3:19's negative-inversion

---

## 3. χαρά / χαίρω + the joy-saturated PHP signature — **STABLE (undocumented; consider brief doc)**

PHP is the JOY LETTER of the NT. **16 occurrences** across the book (1:4, 1:18 ×2, 1:25, 2:2, 2:17, 2:18, 2:28, 2:29, 3:1, 4:1, 4:4 ×2, 4:10) — including:

- Joy as Pauline disposition: 1:4, 1:18, 1:25, 2:17 (paradoxical-joy-amid-suffering)
- Joy as Pauline imperative: 2:18, 2:28, 2:29, 3:1, 4:4 ×2
- Joy as Pauline endearment-noun: 4:1 ("you are my joy and crown")
- Joy as Pauline retrospective-thanksgiving: 4:10

All occurrences uniformly render **ชื่นชมยินดี** (verb / noun-phrase). The compound συγχαίρω (2:17, 2:18) → **ร่วมยินดี** preserves the σύν-prefix. The χαρά / στέφανός pair at 4:1 → **ความชื่นชมยินดีและมงกุฎ** preserves the affection-pairing.

**Editorial assessment:** Single-rendering **ชื่นชมยินดี** across all uses is uniform and idiomatically natural in Thai. The double-imperative at 4:4 (Χαίρετε ἐν κυρίῳ πάντοτε · πάλιν ἐρῶ, χαίρετε → จงชื่นชมยินดีในองค์พระผู้เป็นเจ้าเสมอ ... ข้าพเจ้าจะกล่าวอีก จงชื่นชมยินดีเถิด) reads as a satisfying Thai-rhetorical doubling.

**Recommend: STABLE; brief corpus doc optional** — `docs/translator_decisions/chara_pauline_joy_2026-05.md` to lock the **ชื่นชมยินดี** rendering as the Pauline-corpus default and document the συγχαίρω compound. Forward-pertinent: 1 Thess 1:6 / 5:16 ‘χαίρετε πάντοτε’ already used the same lemma + rendering (verified compliant); 1 Pet 1:6 / 4:13 + Jas 1:2 will recur. Lower priority than §1 + §2.

---

## 4. ἁρπαγμός 2:6 — the Christological crux — **REVIEW (rationale comprehensive at verse level; corpus-doctrinally load-bearing)**

PHP 2:6 contains one of the most-debated single Greek words in the entire NT:

> ὃς ἐν μορφῇ θεοῦ ὑπάρχων **οὐχ ἁρπαγμὸν ἡγήσατο** τὸ εἶναι ἴσα θεῷ
> พระองค์ผู้ทรงดำรงอยู่ในสภาพของพระเจ้า **แต่มิได้ทรงถือว่า**การเป็นเสมอกับพระเจ้า**เป็นสิ่งที่ต้องยึดไว้**

The lemma is a NT-HAPAX. Two scholarly readings dominate:

| Reading | Claim | Translation logic |
|---|---|---|
| **(a) res rapta** ("thing-already-grasped, held-onto") — *currently chosen* | Christ already possessed equality-with-God; the "not-grasping" is the choice not to selfishly cling-to / exploit divine prerogatives. | "did not consider equality-with-God a thing to be held onto / clung to" |
| **(b) res rapienda** ("thing-to-be-seized") | Christ did not regard equality-with-God as something to be reached-for / acquired-by-grasping. | "did not consider equality-with-God a thing to be grasped after" |

The dominant evangelical-Protestant reading is **(a)** (NIV1984 / NIV2011 "did not consider equality with God something to be used to his own advantage"; ESV "did not count equality with God a thing to be grasped"; CSB; BSB current verse rendering; affirmed by D.B. Wallace, N.T. Wright, R. Hoover's 1971 BHGNT-classic study). Reading (b) is held by some Wesleyan / Adoptionist-leaning scholars and a minority of historic-critical commentators.

**Current Thai rendering** ‘**สิ่งที่ต้องยึดไว้**’ ("a thing-to-be-held-onto") cleanly aligns with reading (a). The Thai phrasing preserves the not-clutching sense without slipping into the milder "to-be-grasped-after" of reading (b).

**REVIEW flag — Confirm with Ben + external AI:** The choice is doctrinally orthodox and aligns with the corpus's evangelical-Protestant framing per RULES §0. But because the lemma is a HAPAX with no corpus-precedent + no fallback, the rendering establishes a **Thai-evangelical convention** for any future Thai-Christological discourse. Worth one external-AI confirmation that **สิ่งที่ต้องยึดไว้** preserves reading (a) cleanly without unintentional slippage. Should also be locked into the new `christ_hymn_kenosis_2026-05.md` doc (§1).

---

## 5. πραιτώριον (1:13) → **กองทหารองครักษ์ปรีทอเรียม** — contextual-gloss expansion vs MRK/JHN/ACT precedent — **REVIEW**

The lemma πραιτώριον is contextual: in MRK 15:16 / JHN 18:28 / ACT 23:35 it = the governor's official residence/headquarters; in PHP 1:13 (Paul writing from Rome) it = the imperial Praetorian Guard or their barracks. The Thai rendering combines the corpus-precedent transliteration **ปรีทอเรียม** (matches MRK 15:16) with an explanatory **กองทหารองครักษ์** ("imperial-guard regiment"):

> ὥστε τοὺς δεσμούς μου φανεροὺς ἐν Χριστῷ γενέσθαι ἐν ὅλῳ τῷ **πραιτωρίῳ**
> ผลก็คือทั่วทั้ง**กองทหารองครักษ์ปรีทอเรียม** ... ได้รู้ว่าข้าพเจ้าถูกจองจำเพราะพระคริสต์

**Editorial assessment:** The bilingual gloss is a **contextual-disambiguation** of a polysemous lemma — preserving the corpus-precedent transliteration while clarifying the Roman-imperial-context shift. This is a principled contextual variant per RULES §5. The verse-level KD acknowledges the cross-corpus precedent (Mark/John/Acts = governor's residence) and the Rome-context-divergence (Paul = Praetorian-Guard).

**REVIEW flag:** Minor — Ben to confirm the bilingual-gloss-pattern (transliteration + Thai-explanatory) is the right register for this contextual-divergence (vs. e.g., transliteration-only **ปรีทอเรียม** with verse-level note). Forward-pertinent: 4:22 references **ราชสำนักของซีซาร์** ("the household of Caesar") which is the same imperial-administration sphere — the bilingual-gloss at 1:13 + the natural rendering at 4:22 form a coherent imperial-administration cluster. **No new doc needed**; verse-level rationale + glossary contextual variant suffice.

---

## 6. παρουσία (1:26) — the non-eschatological "visit" sense vs the 1TH-locked eschatological-coming — **REVIEW**

PHP 1:26 is the **only παρουσία occurrence in the book** AND the only NT παρουσία where the referent is explicitly Paul (not Christ):

> ἵνα τὸ καύχημα ὑμῶν περισσεύῃ ἐν Χριστῷ Ἰησοῦ ἐν ἐμοὶ διὰ τῆς ἐμῆς **παρουσίας** πάλιν πρὸς ὑμᾶς
> เพื่อว่าโดย**การกลับไป**หาพวกท่านอีกครั้งของข้าพเจ้า ความภูมิใจของพวกท่าน ... จะทวียิ่งขึ้น

The verse-level KD acknowledges the contextual-shift: NOT the technical eschatological "return of Christ" sense but plain "arrival, presence, coming-to-visit" — Paul's own anticipated apostolic visit to Philippi.

**Editorial assessment:** The translator's choice **การกลับไป** is principled: it foregrounds the relational return-to-them while avoiding the eschatological-loaded **การเสด็จมา** rendering that the 1TH audit (§1) recommended locking for παρουσία-of-Christ (1 Thess 2:19; 3:13; 4:15; 5:23). The Pauline-self-referential sense at PHP 1:26 should NOT receive the royal-เสด็จ rendering reserved for divine-action. Compliant with the 1TH audit's recommended lock-philosophy.

**REVIEW flag:** Confirm that PHP 1:26 (Paul's own visit, plain register **การกลับไป**) is the principled exception that should be carved out in any future `parousia_christou_2026-04.md` corpus doc — the doc should specify "Christ-eschatological-subject = **การเสด็จมา** (royal-divine); apostolic-or-non-divine-subject = plain register **การกลับไป / การมา**." Forward-pertinent: 2 Thess 2:9 παρουσία τοῦ ἀνόμου ("the parousia of the lawless one" — non-Christ subject) will need similar register-care; PHP 1:26 is the precedent. Recommend the 1TH-audit's recommended doc be amended at write-time to include this PHP 1:26 sub-rule.

---

## 7. σάρξ polysemy across PHP (1:22, 1:24, 3:3, 3:4) — **STABLE (rationale comprehensive at verse level; consider doc)**

Pauline σάρξ is the most polysemously-loaded Pauline lemma. In PHP it occurs 4× and the translator handles the polysemy principled-ly per RULES §5:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:22 | ἐν σαρκί | ใน**ร่างกายนี้** (with demonstrative -นี้) | physical body / earthly life |
| 1:24 | ἐν τῇ σαρκί | ใน**ร่างกายนี้**ต่อไป | physical body / earthly life (continuation) |
| 3:3 | οὐκ ἐν σαρκὶ πεποιθότες | ไม่วางใจใน**เนื้อหนัง** | external/physical religious credentials |
| 3:4 | πεποίθησιν καὶ ἐν σαρκί ... πεποιθέναι ἐν σαρκί | วางใจใน**เนื้อหนัง** ... | external/physical religious credentials |

Both KDs flag RULES §5 polysemy explicitly. The lexical split is principled:
- **ร่างกายนี้** (with the demonstrative -นี้) = Paul's specifically-this-physical-body (1:22 / 1:24 — physical-existence sense)
- **เนื้อหนัง** = Paul's general "fleshly-religion-credentials" sense (3:3 / 3:4 — external-credential sense)

The further sense **σάρξ-as-sinful-nature** (Rom 7–8 / Gal 5:13–24, the densest Pauline cluster) does NOT occur in PHP. It will be the dominant sense in Romans.

**Editorial assessment:** The two-way Thai-lexical split is principled and matches the contextual-disambiguation Pauline σάρξ requires. The contrast within ch. 3 (v.3 "we don't trust in the flesh" → v.4 "but I have grounds for trust in the flesh too" — wordplay-sarcasm) reads naturally with the unified **เนื้อหนัง** rendering across both.

**Recommend: STABLE; consider corpus doc later** — `docs/translator_decisions/sarx_polysemy_2026-05.md` is the natural future doc; defer to **after Romans 7–8 ships** so the third sense (sinful-nature) can be incorporated. Forward-pertinent: Rom 7:5–25; 8:1–13; 13:14; Gal 5:13–24; 1 Cor 5:5; Eph 2:3, all densely σάρξ-saturated. PHP's two senses + the Romans third sense will form the complete Pauline σάρξ-polysemy doc.

---

## 8. ταπεινόω polysemy (2:8 ↔ 4:12) — **STABLE (rationale comprehensive at verse level)**

The ταπεινόω verbal lemma occurs 2× in PHP, with semantically distinct senses:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 2:8 | ἐταπείνωσεν ἑαυτὸν | ทรง**ถ่อมพระองค์**เองลง | moral/Christological humility (cognate-link with 2:3 ταπεινοφροσύνη ‘**ความถ่อมใจ**’) |
| 4:12 | οἶδα καὶ ταπεινοῦσθαι | ข้าพเจ้ารู้ที่จะอยู่อย่าง**ขัดสน** | material low-state (Pauline material-deprivation context — economic, not moral) |

The 4:12 KD flags RULES §5 polysemy explicitly: "ταπεινόω here NOT the moral-humility sense (cf. PHP 2:8 ἐταπείνωσεν) but material-low-state — 'living-with-little'."

**Editorial assessment:** The lexical split is principled. **ถ่อมพระองค์** preserves the moral-humility / Christ-self-humbling sense (2:8 — the kenotic-descent-language of the hymn). **ขัดสน** preserves the material low-state sense (4:12 — paired with περισσεύειν → **อยู่อย่างเหลือล้น**, the Stoic-merism for the full economic range). Reader does not confuse the two.

**Recommend: STABLE; no new doc needed.** The contextual-polysemy is captured in verse-level KDs. Note: this two-sense split should be cross-referenced in the future `christ_hymn_kenosis_2026-05.md` doc (§1 lock #3) and the future `phroneo_pauline_2026-05.md` doc (§2 lock #4 — both hymn-vocabulary + ethics-of-mind clusters).

---

## 9. πολιτεύομαι / πολίτευμα — citizenship cluster (1:27 + 3:20) — **STABLE (undocumented; brief doc optional)**

PHP 1:27 (πολιτεύεσθε → ดำเนินชีวิต — verb, "conduct yourselves [as citizens]") and 3:20 (τὸ πολίτευμα ἐν οὐρανοῖς → สถานะการเป็นพลเมืองของเราอยู่ในสวรรค์ — noun, "citizenship-status / commonwealth") form a deliberate verb-noun bracket:

| Verse | Greek | Thai | Note |
|---|---|---|---|
| 1:27 | πολιτεύεσθε | จง**ดำเนินชีวิต**อย่างสมแก่ข่าวประเสริฐ | first-occurrence in shipped corpus |
| 3:20 | τὸ πολίτευμα ἐν οὐρανοῖς ὑπάρχει | สถานะ**การเป็นพลเมือง**ของเราอยู่ในสวรรค์ | NT-HAPAX πολίτευμα |

**Editorial assessment:** The verb-noun bracket-pair is rhetorically loaded for Philippi (a Roman colony where Roman-citizenship was prized). The translator chose **ดำเนินชีวิต** (live-out-life) for the verb (preserving the Pauline-default περιπατέω-style "walk/live" pattern) and **สถานะการเป็นพลเมือง** (citizenship-status) for the noun. The split is principled — the verb's pragmatic-force is "live-as-Christians" (which is the Pauline-corpus standard for ethical-conduct verbs); the noun's force is the citizenship-status-claim itself (which requires the explicit Thai citizenship-vocabulary).

**Recommend: STABLE; no immediate doc needed.** The cluster is essentially a Philippi-specific deployment; the citizenship-vocabulary does not recur densely elsewhere in the Pauline corpus (the next major occurrence is Eph 2:19 συμπολῖται with the related compound-stem). The verse-level KDs at 1:27 + 3:20 capture the rationale.

---

## 10. κοινωνία / συγκοινωνέω + financial-and-spiritual partnership cluster — **STABLE**

PHP κοινωνία-cluster spans 5 verses:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:5 | τῇ κοινωνίᾳ ὑμῶν εἰς τὸ εὐαγγέλιον | **การมีส่วนร่วม**ของพวกท่านในข่าวประเสริฐ | gospel-partnership (incl. financial) |
| 1:7 | συγκοινωνούς μου τῆς χάριτος | **มีส่วนร่วม**ในพระคุณกับข้าพเจ้า | grace-partnership-with-Paul |
| 2:1 | κοινωνία πνεύματος | **การมีส่วนร่วม**ใด ๆ ของพระวิญญาณ | Spirit-fellowship |
| 3:10 | κοινωνίαν παθημάτων αὐτοῦ | **การมีส่วน**ในการทรงทนทุกข์ของพระองค์ | suffering-fellowship-with-Christ |
| 4:14 | συγκοινωνήσαντές μου τῇ θλίψει | **ได้ร่วม**ในความทุกข์ลำบากของข้าพเจ้า | suffering-fellowship-with-Paul |
| 4:15 | οὐδεμία μοι ἐκκλησία **ἐκοινώνησεν** | ไม่มีคริสตจักรใด**เข้าร่วมกับ**ข้าพเจ้า | financial-partnership |

Uniform rendering family **มีส่วนร่วม / มีส่วน / ร่วม / เข้าร่วม** (the ร่วม-stem family) preserves the underlying κοινωνία semantic-thread across all 6 occurrences. The συν- prefix on συγκοινωνέω (1:7, 4:14) is captured by the prefix-equivalent particles in Thai.

**Editorial assessment:** This is a key Pauline-relational lemma cluster. The translator preserved the unified semantic-field while allowing surface-Thai-syntactic variation (verb / noun / participle as needed). Compliant with the corpus-Pauline standard.

**STABLE — no new doc needed.** Cross-reference in any future Pauline-relational-vocabulary doc would be sufficient.

---

## 11. OT echoes / allusions in PHP — **all logged; one density-cluster**

PHP has **5 explicit OT-allusions logged** in `data/nt_ot_citations.json`:

| PHP | OT source | Type | Status |
|---|---|---|---|
| 1:19 | Job 13:16 LXX | verbatim-allusion | **LOGGED** — KD names Job-figure self-positioning |
| 2:10–11 | Isa 45:23 LXX | divine-name-application | **LOGGED** — Christological climax of the hymn |
| 2:15 | Deut 32:5 LXX | reverse-application | **LOGGED** — Paul inverts the wilderness-generation indictment |
| 2:17 | Num 28:7 cultic-image | image / metaphor | acknowledged (drink-offering imagery) |
| 4:18 | Lev 1:9, 1:13, 1:17 LXX cultic-formula | verbatim-formula | **LOGGED** — sacrificial-acceptance language |

Additional unflagged echoes:
- 3:21 ὑποτάξαι αὑτῷ τὰ πάντα — Ps 8:6 LXX (cited in 1Co 15:27, Eph 1:22, Heb 2:8) — universal-sovereignty echo. Not formally cited in PHP.

**Recommend (low priority):** Add 3:21 (Ps 8:6 echo) to `data/nt_ot_citations.json` as `type: "thematic_echo"`. Not blocking.

---

## 12. Inherited Pauline locks — **all compliant**

| Doc | PHP evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 3:6 (διώκων τὴν ἐκκλησίαν → **ข่มเหงคริสตจักร**) — only PHP occurrence; collective-noun "the church" sense per uW; uniform with corpus. | **LOCKED** ✓ |
| `ethnos_2026-04.md` | N/A — ἔθνος / ἔθνη absent from PHP. | **LOCKED (N/A)** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | PHP has **15+ narrator-κύριος references** (1:2, 1:14, 2:11, 2:19, 2:24, 2:29, 3:1, 3:8, 3:20, 4:1, 4:2, 4:4, 4:5, 4:10, 4:23) — all → **องค์พระผู้เป็นเจ้า**, perfectly compliant. The doc's "Lukan-Acts signature" framing was already flagged for amendment in JHN + GAL + 1TH audits; PHP provides a **fourth independent Pauline-corpus confirmation**. | **LOCKED-with-amendment-needed** (already noted in prior audits) |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in PHP (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | 4:20 doxology τῷ θεῷ καὶ πατρὶ ἡμῶν ἡ δόξα → **ขอให้พระสิริมีแด่พระเจ้าและพระบิดาของเรา** (corporate-narrator-doxological). 1:11 εἰς δόξαν καὶ ἔπαινον θεοῦ → **เพื่อพระสิริและการสรรเสริญพระเจ้า**. 2:11 εἰς δόξαν θεοῦ πατρός → **เพื่อพระสิริของพระเจ้าพระบิดา**. All compliant with the doc's three-way rule. | **LOCKED** ✓ |
| `honorifics_non_divine_authorities_2026-04.md` | 4:22 Καίσαρ → **ซีซาร์** (plain register; no royal-pระ); 4:3 σύζυγος (yokefellow, plain register). 2:25 Epaphroditus / 2:19 Timothy / co-senders all plain register. Compliant. | **LOCKED** ✓ |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout (ทรง- prefix on every divine-action verb in the Christ-hymn, the doxological closures, etc.); plain register for human authorities + co-workers. The 2:11 πατήρ (divine-genitive) → **พระบิดา** (royal); 1:1 Paul-as-δοῦλος plain. Compliant. | **LOCKED** ✓ |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic embeds in PHP. The 4:20 ἀμήν → **อาเมน** is transliterated per the Pauline-doxology-closure pattern (matches 1Th 5:28 closure-style; consistent corpus-wide). | **LOCKED (N/A for embeds; ἀμήν compliant)** |
| `inclusion_variants_absent_verses_2026-04.md` | The 4:23 final-ἀμήν variant resolved via `output/textual_variants/_resolved/philippians_04_final_amen.md` — silent-omission per RULES §5 (mainstream evangelical-critical-text consensus matches our practice; documented). | **LOCKED** ✓ |
| `historic_present_2026-04.md` | N/A — PHP is doctrinal-pastoral, not narrative. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in PHP. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι both absent from PHP. | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — ἄφεσις absent from PHP. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | N/A — no idol/pagan-deity references in PHP. | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | 1:13 πραιτώριον (REVIEW — see §5 above); 4:22 Καίσαρ → **ซีซาร์**; "household of Caesar" → **ราชสำนักของซีซาร์**. The Roman-imperial-administration cluster is consistent. | **LOCKED with §5 REVIEW** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from PHP. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον N/A in PHP (no πνεῦμα ἅγιον references); πνεῦμα as "divine Spirit" at 1:19 (πνεῦμα Ἰησοῦ Χριστοῦ → **พระวิญญาณของพระเยซูคริสต์**); 1:27 (ἐν ἑνὶ πνεύματι → **ในจิตวิญญาณเดียวกัน**, anthropological); 2:1 (κοινωνία πνεύματος → **การมีส่วนร่วมใด ๆ ของพระวิญญาณ**, divine); 3:3 (πνεύματι θεοῦ → **พระวิญญาณของพระเจ้า**). ψυχή at 1:27 (μιᾷ ψυχῇ → **ใจเดียวกัน**); 2:30 (παραβολευσάμενος τῇ ψυχῇ → **ยอมเสี่ยงชีวิต**). The σύμψυχος (2:2), ἰσόψυχος (2:20), εὐψυχέω (2:19) compounds → **เป็นหนึ่งใจเดียวกัน / มีจิตใจเดียวกัน / ได้รับการหนุนใจ** preserve the ψυχή-stem semantic. Compliant. | **LOCKED** ✓ |
| `johannine_doubled_amen_2026-04.md` | N/A — Pauline. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A — βασιλεία absent from PHP (no kingdom-references in this letter). | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | 2:10 (ἐπουρανίων → **ในสวรรค์**); 3:14 (τῆς ἄνω κλήσεως τοῦ θεοῦ → **การทรงเรียกฝ่ายเบื้องบน**); 3:20 (τὸ πολίτευμα ἐν οὐρανοῖς → **สถานะการเป็นพลเมือง...อยู่ในสวรรค์**). All compliant with the doc's after-possessor-vs-theological-default split. | **LOCKED** ✓ |
| `adversary_speech_register_2026-05.md` | N/A — no Satan-speech in PHP. | **LOCKED (N/A)** |
| `huiothesia_adoption_2026-05.md` | N/A — υἱοθεσία absent from PHP. | **LOCKED (N/A)** |
| `dikaioo_dikaiosyne_family_2026-05.md` | 1:11 (καρπὸν δικαιοσύνης → **ผลแห่งความชอบธรรม**); 3:6 (κατὰ δικαιοσύνην τὴν ἐν νόμῳ → **ตามความชอบธรรมที่อยู่ในธรรมบัญญัติ**); 3:9 (ἐμὴν δικαιοσύνην τὴν ἐκ νόμου / τὴν ἐκ θεοῦ δικαιοσύνην → **ความชอบธรรมของข้าพเจ้าเองที่มาจากธรรมบัญญัติ / ความชอบธรรมที่มาจากพระเจ้า**). δίκαιος at 4:8 → **ชอบธรรม**. All compliant with the doc's δικαιοσύνη → **ความชอบธรรม** lock. | **LOCKED** ✓ |
| `nomos_pauline_2026-05.md` | 3:5 (κατὰ νόμον Φαρισαῖος → **ตามธรรมบัญญัติเป็นฟาริสี**); 3:6 (κατὰ δικαιοσύνην τὴν ἐν νόμῳ → **ตามความชอบธรรมที่อยู่ในธรรมบัญญัติ**); 3:9 (δικαιοσύνην τὴν ἐκ νόμου → **ความชอบธรรม...ที่มาจากธรรมบัญญัติ**). All 3 occurrences uniform per the lock. | **LOCKED** ✓ |
| `diakonos_pauline_2026-05.md` | 1:1 (διακόνοις → **ผู้รับใช้** — paired with ἐπίσκοποι in PHP's letter-opening; lay/general-service sense per the doc's lock). 2:25 λειτουργόν (Epaphroditus) → **ผู้ปรนนิบัติ** (per the doc's note that λειτουργία takes a different rendering for cultic-vs-general-service contexts). All compliant. | **LOCKED** ✓ |
| `telos_paidagogos_christ_2026-05.md` | 3:14 (κατὰ σκοπὸν διώκω εἰς τὸ βραβεῖον → **มุ่งหน้าตามเป้าหมายเพื่อรางวัล**) — adjacent vocabulary; the τέλειος-cluster at 3:12 (τετελείωμαι) + 3:15 (τέλειοι) distinct from the GAL τέλος / Χριστοῦ doc's focus but principled per the verse-level KDs. | **LOCKED (adjacent-but-distinct)** |
| `proper_noun_wordplay_2026-05.md` | 3:2–3 κατατομή / περιτομή Pauline-pun (mutilation / circumcision) — preserved with **การเชือดทำลายเนื้อหนัง / การเข้าสุหนัตที่แท้จริง**. Per doc's principle, the wordplay's force is preserved through Thai-paraphrase rather than transliterated retention. Compliant. | **LOCKED** ✓ |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | N/A — neither lemma in PHP. | **LOCKED (N/A)** |

**Note on ἅγιος → ธรรมิกชน vs วิสุทธิชน corpus split:**

PHP uses **ธรรมิกชน** at 1:1 (saints), 4:21, 4:22 — matching the corpus-wide standard (Matthew 4×, Mark 1×, Acts 16×, Romans 13×, Philemon 9× — all ธรรมิกชน). **1 Thessalonians is the SOLE OUTLIER** in the shipped Pauline corpus, using **วิสุทธิชน** at 3:13 + 5:23 etc. (4 occurrences).

PHP is **fully compliant with the corpus default**. The 1TH-end-of-book-audit's §2 (ἁγιασμός cluster) noted **วิสุทธิชน** at 3:13 without flagging the corpus-divergence — this is a 1TH-specific drift question (separate from the PHP audit). **Recommend: flag 1TH-vs-PHP/Romans/Acts/Philemon ἅγιος-rendering divergence as a corpus-cleanup item separate from the PHP v1 tag** — Ben to decide whether to (a) normalize 1TH 3:13 + 5:23 etc. to ธรรมิกชน (corpus-uniform), or (b) explicitly document วิสุทธิชน as the **eschatological-saints-context** variant rendering and add the contextual variant to glossary. Either resolution is principled; the choice is editorial register.

---

## 13. πίστις Χριστοῦ at 3:9 — the Pauline-genitive crux — **DECIDE**

PHP 3:9 is one of the loci-classici for the πίστις Χριστοῦ debate:

> καὶ εὑρεθῶ ἐν αὐτῷ, μὴ ἔχων ἐμὴν δικαιοσύνην τὴν ἐκ νόμου ἀλλὰ τὴν **διὰ πίστεως Χριστοῦ**, τὴν ἐκ θεοῦ δικαιοσύνην ἐπὶ τῇ πίστει
> ความชอบธรรมที่มาโดยทาง**ความเชื่อในพระคริสต์** ความชอบธรรมที่มาจากพระเจ้าโดยอาศัยความเชื่อ

The genitive πίστεως Χριστοῦ admits two readings:
- **(a) Objective genitive — "faith IN Christ" (Christ as object of believing)** — *currently chosen.* Traditional / Reformation / NIV / ESV / CSB / BSB / mainstream evangelical reading. Supports forensic-justification (the believer's faith-in-Christ is the means of receiving the alien-righteousness).
- **(b) Subjective genitive — "the faith / faithfulness OF Christ" (Christ as subject of believing)** — Wright / Hays / Campbell / NIV2011-marginal-note / NET-marginal-note / CEB-text reading. Supports participation-Christology (Christ's own faithfulness-to-the-Father is the means of believer-righteousness).

The 3:9 KD names the choice explicitly:
> πίστις Χριστοῦ — the genitive's interpretation is one of the great Pauline-debates ... We follow (1) — the objective-genitive reading is dominant in evangelical-Protestant scholarship and matches the ἐπὶ τῇ πίστει repetition in v.9b. Render 'ความเชื่อในพระคริสต์' — preserves the objective-genitive.

**Editorial assessment:** The choice is principled and aligns with the corpus's evangelical-Protestant framing per RULES §0. The grammatical-warrant from v.9b's ἐπὶ τῇ πίστει (which clarifies that "the faith" of v.9a is the *believer's* faith — since the ἐπί-construction is the means by-which the believer receives righteousness) is a strong tell. NIV2011 / ESV / CSB all preserve this reading.

**DECIDE flag** — The lemma cluster recurs in Pauline corpus at:
- Rom 3:22 διὰ πίστεως Ἰησοῦ Χριστοῦ
- Rom 3:26 τὸν ἐκ πίστεως Ἰησοῦ
- Gal 2:16 (×2) διὰ πίστεως Ἰησοῦ Χριστοῦ ... ἐκ πίστεως Χριστοῦ
- Gal 2:20 ἐν πίστει ζῶ τῇ τοῦ υἱοῦ τοῦ θεοῦ
- Gal 3:22 ἐκ πίστεως Ἰησοῦ Χριστοῦ
- Eph 3:12 διὰ τῆς πίστεως αὐτοῦ
- PHP 3:9 (here)

GAL 2:16, 2:20 already shipped — Ben should confirm what rendering was chosen there (audit branch indicates GAL likely also chose objective-genitive, but worth verifying). The corpus-wide consistency-question: does the project lock objective-genitive **ความเชื่อในพระคริสต์** corpus-wide, or allow contextual-variation? **Worth Ben's explicit decision before tagging book-philippians-v1**, since Romans 3:22 + 3:26 will compound the editorial weight when they ship.

**Recommend: write `docs/translator_decisions/pistis_christou_2026-05.md` capturing the objective-genitive corpus-default + cite GAL 2:16 + PHP 3:9 as the locking precedents** — IF Ben confirms the objective-genitive default. (Status: DECIDE → likely LOCK after confirmation.)

---

## 14. σύζυγος at 4:3 — common-noun vs proper-name — **DECIDE**

> ναὶ ἐρωτῶ καὶ σέ, **γνήσιε σύζυγε**, συλλαμβάνου αὐταῖς
> ใช่แล้ว ข้าพเจ้าขอร้องท่านด้วย **เพื่อนร่วมแอกที่แท้จริง** จงช่วยเหลือผู้หญิงเหล่านี้

NT-HAPAX. Two interpretive options:

| Reading | Identification | Translation |
|---|---|---|
| **(a) Common noun "true yokefellow / faithful companion-in-labor"** — *currently chosen.* | A specific person known to the Philippians whose identity is now lost — the standard scholarly view. | **เพื่อนร่วมแอกที่แท้จริง** |
| **(b) Proper name "Syzygus"** with γνήσιε as Pauline-pun on the name's meaning ("you-are-truly-named-Syzygus"). | Rare reading; held by some early Greek commentators. | (would be) **ซิซิกัส ผู้สมชื่อ** or similar |

**Editorial assessment:** Reading (a) is the standard and the Thai rendering is principled. The Pauline-pun-on-name reading (b) is rare in modern scholarship and would require a transliteration-plus-gloss approach.

**DECIDE flag — Confirm with Ben + external AI:** The current rendering is correct per evangelical-mainstream. But because PHP 4:3 also includes Εὐοδία (4:2), Συντύχη (4:2), Κλήμης (4:3) — three definite proper names — the σύζυγος common-noun reading creates a slight rhetorical-discontinuity (a list of names interrupted by a generic-vocative). Some readers may notice. Worth Ben's explicit confirmation that **เพื่อนร่วมแอกที่แท้จริง** is the corpus-default vs (b) the Syzygus-as-name option.

**Recommend: STABLE if confirmed; verse-level KD already comprehensive.** No new doc needed — the per-verse rationale is sufficient.

---

## 15. σκύβαλον at 3:8 — register choice — **DECIDE**

> ἡγοῦμαι **σκύβαλα** ἵνα Χριστὸν κερδήσω
> ข้าพเจ้าถือว่าสิ่งเหล่านั้นเป็น**เศษขยะ** เพื่อข้าพเจ้าจะได้พระคริสต์เป็นกำไร

NT-HAPAX. The Greek lexeme in Paul's day meant either (1) "excrement, dung" (vulgar register) or (2) "garbage, refuse, rubbish" (general dismissive register). The two register-options:

| Translation tradition | Rendering | Register |
|---|---|---|
| **KJV / NKJV** | "dung" | crude / vulgar |
| **NIV / NASB / CSB / NLT / ESV / BSB** | "rubbish / garbage / refuse" | dismissive / general |
| **Current Thai** | **เศษขยะ** ("garbage scraps / refuse") | dismissive / general — matches mainstream-evangelical English-Bible practice |

The KD acknowledges the choice explicitly:
> Render 'เศษขยะ' — captures the worthless-discarded sense for the Thai reader without forcing the more vulgar excrement-reading.

**Editorial assessment:** The choice aligns with mainstream-evangelical-English-Bible practice and respects Thai-Christian readerly register-expectations. Some scholarly translations (e.g., Bauer's BDAG; Wallace's argument that "dung" preserves the shock-value of Paul's rhetoric) would prefer a stronger rendering.

**DECIDE flag — Confirm with Ben:** Is the **เศษขยะ** ("garbage / refuse") register correct for the Thai-evangelical audience, or should the project use a stronger **มูลสัตว์** ("animal-dung") or **อุจจาระ** ("excrement, vulgar register") rendering to preserve the LXX-period crude force that Paul deliberately deployed? The verse-level KD acknowledges both options. Worth Ben's explicit register-choice — this is the **most-shocking word in the chapter**, and the editorial register-call here may set precedent for any future similarly-loaded Pauline rhetoric (e.g., Gal 5:12 ἀποκόψονται, Phil 3:2 κύνες which is already in PHP and rendered plain **สุนัข**).

**Recommend: STABLE if confirmed; no new doc needed.** Verse-level KD already captures the full reasoning; Ben's confirmation closes the editorial-question.

---

## Mechanical (§1) — **all green**

- 4/4 chapters: `output/check_reports/philippians_NN_review.md` ✓ (all chapter reports show ✅ clean status across all checks)
- 4/4 chapters: `output/back_translations/philippians_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-123-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --book philippians --strict`: **PASS** — 1 candidate (4:23 final-ἀμήν) resolved via `output/textual_variants/_resolved/philippians_04_final_amen.md` (silent-omission per RULES §5)
- `python3 scripts/export_to_usfm.py --book PHP`: **clean** — `output/paratext/PHP.SFM` regenerated with no errors
- `git status output/`: clean (only the new `_resolved/philippians_04_final_amen.md` file untracked, which is part of this audit branch)

---

## Pre-existing docs affirmed / unchanged

All 31 docs in `docs/translator_decisions/` reviewed. Compliance summary in §12 above. The **Lukan-Acts narrator-κύριος doc** flagged for amendment (already noted in JHN + GAL + 1TH audits) — PHP provides a fourth independent Pauline-corpus confirmation; the doc's "Lukan signature" framing should be renamed/extended to acknowledge corpus-wide narrator-κύριος usage in JHN + GAL + 1TH + PHP (and forward-Pauline). The **psyche_vs_pneuma_anthropological doc** flagged in 1TH audit for sub-section amendment to handle 1TH 5:23 tripartite-listing exception — PHP raises no new amendment-need (PHP's πνεῦμα / ψυχή uses are all compliant with the existing lock).

---

## Flagged for Ben's attention

### A. Christ-Hymn (2:5–11) vocabulary cluster — **STABLE, lift to corpus doc** (§1)
The single most theologically-load-bearing cluster in PHP. The kenosis-vocabulary (μορφή / σχῆμα / κενόω / ὑπερυψόω / κύριος Ἰησοῦς Χριστός) is rendered with principled, evangelical-orthodox Thai. Lift to corpus doc `christ_hymn_kenosis_2026-05.md` before Col 1:15–20 + 1 Tim 3:16 + Heb 1:1–4 + Eph 1:20–23 + 1 Pet 3:18–22 + Rev 5:9–14 ship.

### B. φρονέω cluster — **STABLE, lift to corpus doc** (§2)
The Philippians-signature lemma (10× in 4 chapters; densest in NT). The principled three-way semantic split (think / mindset / concern-for) is doctrinally rich. Lift to corpus doc `phroneo_pauline_2026-05.md` before Romans 8:5–7 (the densest Pauline cluster after PHP) and Col 3:2 (the Pauline imperative-mirror of PHP 3:19).

### C. χαρά / χαίρω joy-cluster — **STABLE, brief doc optional** (§3)
The joy-saturated PHP signature. Brief corpus doc `chara_pauline_joy_2026-05.md` would lock the **ชื่นชมยินดี** rendering as Pauline-corpus default. Lower priority than §A + §B.

### D. ἁρπαγμός 2:6 rendering — **REVIEW** (§4)
The classical-theological crux. Current **สิ่งที่ต้องยึดไว้** (res-rapta reading) is doctrinally orthodox per evangelical-Protestant majority. Worth one external-AI sanity-check that the rendering preserves reading (a) cleanly. Should also be locked into the new `christ_hymn_kenosis_2026-05.md` doc.

### E. πραιτώριον 1:13 bilingual gloss — **REVIEW** (§5)
The gloss **กองทหารองครักษ์ปรีทอเรียม** combines transliteration + Thai-explanatory. Defensible per RULES §5 contextual-variant. Worth Ben's confirmation that the bilingual-gloss-pattern is the right register here vs transliteration-only with verse-level note.

### F. παρουσία 1:26 non-eschatological-visit — **REVIEW** (§6)
**การกลับไป** (plain register) for Paul's own apostolic-visit, distinct from the eschatological-Christ **การเสด็จมา** locked in 1TH. Worth Ben's confirmation that PHP 1:26 should be carved out as the principled exception in any future `parousia_christou_2026-04.md` doc — the doc should specify Christ-eschatological-subject vs apostolic-or-non-divine-subject register split.

### G. πίστις Χριστοῦ 3:9 — **DECIDE** (§13)
Objective-vs-subjective genitive. Currently rendered as objective genitive (**ความเชื่อในพระคริสต์**, the mainstream evangelical reading). Worth Ben's explicit decision before book-philippians-v1 tag, since Romans 3:22 + 3:26 will compound the corpus-weight when they ship. **Recommend lock in `pistis_christou_2026-05.md` after Ben confirms** + cross-check with how GAL 2:16 + 2:20 were rendered in the already-shipped GAL audit.

### H. σύζυγος 4:3 common-noun vs proper-name — **DECIDE** (§14)
Currently rendered as common noun **เพื่อนร่วมแอกที่แท้จริง** (mainstream view). Worth Ben's confirmation that this is the corpus-default vs option (b) "Syzygus-as-name". Verse-level KD already captures the choice; no new doc needed if confirmed.

### I. σκύβαλον 3:8 register choice — **DECIDE** (§15)
Currently rendered as **เศษขยะ** ("garbage / refuse") — mainstream evangelical register. Worth Ben's explicit register-choice between mainstream (**เศษขยะ**) vs the cruder LXX-period **มูลสัตว์ / อุจจาระ** rendering. Sets precedent for any future similarly-loaded Pauline rhetoric.

### J. ἅγιος → ธรรมิกชน vs 1TH's วิสุทธิชน — **CORPUS-CLEANUP separate from PHP v1 tag** (§12 note)
PHP fully compliant with the Matthew/Acts/Romans/Philemon corpus-default **ธรรมิกชน**. **1 Thessalonians is the sole shipped-Pauline outlier** using **วิสุทธิชน** (4 occurrences). Recommend Ben decide separately whether to (a) normalize 1TH or (b) document it as a contextual-variant. **Not blocking for PHP v1 tag.**

### K. New corpus docs to write (before forward-Pauline books)
1. **`docs/translator_decisions/christ_hymn_kenosis_2026-05.md`** (§1) — locks the kenosis-vocabulary cluster + flags ἁρπαγμός / σύζυγος / σκύβαλον review-questions
2. **`docs/translator_decisions/phroneo_pauline_2026-05.md`** (§2) — locks φρονέω three-way semantic split
3. **`docs/translator_decisions/pistis_christou_2026-05.md`** (§13) — IF Ben confirms objective-genitive default
4. **(Optional)** `chara_pauline_joy_2026-05.md` (§3) — brief; locks **ชื่นชมยินดี** rendering
5. **(Future, after Romans ships)** `sarx_polysemy_2026-05.md` (§7) — full three-sense Pauline σάρξ doc

### L. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (Galatians + 1TH + PHP)." Already noted in JHN + GAL + 1TH audits; PHP provides the fourth confirmation.
- **(After 1TH-vs-corpus ἅγιος-rendering decision)** corpus-wide ἅγιος doc — TBD pending Ben's resolution per §12 note above.

### M. External AI review (§3 of checklist) — **packet built in this branch**
Recommended before `book-philippians-v1` tag. The external review packet is sized for free-tier AI ceilings (~20K chars). Use Grok + ChatGPT in parallel per the JHN/GAL/1TH pattern. Suggested 4-cluster external AI focus:
1. **PHP 2:5–11** — the Christ-hymn, μορφή/σχῆμα/κενόω/ὑπερυψόω cluster + ἁρπαγμός crux + Isa 45:23 echo
2. **PHP 3:2–11** — the Judaizers polemic + κατατομή/περιτομή pun + δικαιοσύνη contrast + πίστις Χριστοῦ + σκύβαλον register
3. **PHP 4:1–9 + 4:10–13** — Euodia/Syntyche unity + the σύζυγος/Σύζυγος question + ἐπιεικές gentleness + virtue-list (4:8) + αὐτάρκης Stoic-Christianized contentment
4. **PHP 1:13 + 1:26** — πραιτώριον bilingual-gloss + παρουσία non-eschatological visit + Roman-imperial-administration cluster

---

## Recommendation

**Philippians ships in strong corpus-hygiene shape — and provides the project's first major Christological-hymn rendering, the densest HAPAX-cluster in the corpus, and the joy-saturated Pauline-pastoral signature.** The translator made consistent, principled, evangelical-orthodox choices on the most theologically load-bearing passages (the Christ-hymn 2:5–11; the πίστις Χριστοῦ crux 3:9; the σάρξ polysemy split 1:22 vs 3:3; the κατατομή/περιτομή pun 3:2–3; the αὐτάρκης Stoic-Christianized contentment 4:11–13). The two cross-cutting-Pauline-vocabulary docs that should be lifted (§A Christ-hymn-kenosis; §B φρονέω) are MAJOR forward-pertinent locks — write before Col 1:15–20 + Romans 8 ship.

Tag `book-philippians-v1` after:
1. Ben's decisions on **§G + §H + §I** (DECIDE items: πίστις Χριστοῦ objective-vs-subjective genitive; σύζυγος common-noun-vs-name; σκύβαλον register choice)
2. Ben's confirmation on **§D + §E + §F** (REVIEW items: ἁρπαγμός rendering; πραιτώριον bilingual-gloss; παρουσία non-eschatological-visit)
3. Two-to-three new translator_decisions docs written (§K items 1–3; optionally 4)
4. One existing doc amended (`kyrios_narrator_voice_luke_acts_2026-04.md` — corpus-extension)
5. External AI sanity-check (§M)

The 1TH-audit-recommended `parousia_christou`, `hagiasmos_hagiosune`, and `hemera_kyriou` docs (still pending) should be written concurrently — PHP 1:26's non-eschatological παρουσία provides additional precedent for the παρουσία doc's contextual-register split.

The Pauline letters ahead (2 Thess in flight, then Rom, 1–2 Cor, Eph, Col, Pastorals) will compound the editorial weight of every PHP-introduced lemma. Writing the **Christ-hymn doc and the φρονέω doc** before the Captivity-Letter cluster (Col + Eph + Phlm) ships will avoid forward-drift in the Christological-vocabulary that those letters will further develop.
