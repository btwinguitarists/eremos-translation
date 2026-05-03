# 2 Timothy — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 4 chapters (83 verses; ~95 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (40 docs, including the new `pastoral_corpus_locks_2026-05.md`).
**Trigger:** 2TI 4 shipped (commit `00a387a`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 4/4 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the now-129-chapter corpus); `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book 2timothy --strict` PASSES (1 candidate at 1:11 dispositioned silent per RULES §5). `git status output/` carries only the two `_resolved/` variant docs (1:11 + 2:14, both filed 2026-05-02) plus unrelated paratext stragglers; none affects translation content.
- **2 Timothy is the SECOND PASTORAL EPISTLE shipped** and inherits the bulk of its corpus-level discipline from `pastoral_corpus_locks_2026-05.md` (locked 2026-05-02 at 1TI end-of-book). All five Pastoral-distinctive clusters identified at 1TI re-occur and **all comply with the 1TI locks**: πιστὸς ὁ λόγος (2:11), εὐσέβεια family (3:5; 3:12), ὑγιαίνω (1:13; 4:3), σωτήρ (1:10 — first Christ-application in the Pastorals), ἐπιφάνεια (1:10 first-coming + 4:1, 4:8 second-coming).
- **2 Timothy introduces several NEW corpus-cross-cutting items** that did not surface densely in 1TI: (1) **παραθήκη** "deposit" cluster (1:12, 14; cf. 1 Tim 6:20) — Pastoral-distinctive entrustment-vocabulary; (2) **ἐπιφάνεια bidirectionality** — incarnation-sense at 1:10 vs. second-coming-sense at 4:1/4:8 within a single letter; (3) **3:16 θεόπνευστος + πᾶσα γραφή** — the most-cited evangelical inspiration prooftext, with three HAPAX (θεόπνευστος + ἐλεγμός + ἐπανόρθωσις) and a load-bearing πᾶσα-distributive-vs-collective ambiguity; (4) **2:11–13 conditional-couplet hymn** — a creedal hymn following the πιστὸς ὁ λόγος formula, with a deliberate climactic asymmetry at v.13b; (5) **2:15 ὀρθοτομέω HAPAX** — the famous "rightly-handling-the-word-of-truth" verse with a metaphor-debate (woodworking vs. road-building vs. sacrificial); (6) **3:8 Ἰάννης + Ἰαμβρῆς** — extra-canonical Jewish-tradition names appearing in canonical Scripture; (7) **3:6–7 γυναικάρια** — the diminutive "weak-women" lemma that 1TI's pastoral_corpus_locks §E flagged forward.
- **5 inherited Pastoral-corpus locks confirmed compliant** (πιστὸς ὁ λόγος formula; εὐσέβεια family; σωτήρ Pastoral-shift; ὑγιαίνω sound-doctrine; women-in-worship ambiguity-preservation). **Plus the broader Pauline / corpus locks compliant** in 2TI (see §15).
- **Inclusion-variant gate clean.** 1 candidate at 1:11 (Byzantine harmonization to 1 Tim 2:7's ἐθνῶν) silent-omitted. Plus the 2:14 θεοῦ/κυρίου reading-variant resolved-doc (mainstream English follows θεοῦ; Eremos follows SBLGNT κυρίου per RULES §0). RULES §0 SBLGNT-strictness held throughout; no Tier 1/2/3 inclusion brackets needed (1TI's Tier-2 reading_variant precedent at 1 Tim 3:16 not invoked here).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: παραθήκη ambiguity-preservation strategy at 1:12; 2:15 ὀρθοτομέω metaphor-flattening to "จัดการ ... อย่างตรงเที่ยง"; 3:8 Ἰάννης + Ἰαμβρῆς extra-canonical-name handling).
- **1 item flagged DECIDE** (3:16 πᾶσα γραφὴ θεόπνευστος — the πᾶσα distributive-vs-collective ambiguity preserved + θεόπνευστος rendering "ได้รับการดลใจจากพระเจ้า" loses the etymological breath-image — both worth Ben's confirmation given the verse's centrality to evangelical-Protestant doctrine of Scripture).
- **External AI review (§3) packet pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πιστὸς ὁ λόγος formula at 2:11 — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §A)**

The fourth of five corpus occurrences of the Pastoral citation-formula (1 Tim 1:15; 3:1; 4:9; 2 Tim 2:11; Tit 3:8). Renders **ถ้อยคำนี้เชื่อถือได้** — exact match to the §A lock.

| Verse | Greek | Thai | Reference direction |
|---|---|---|---|
| 2:11 | πιστὸς ὁ λόγος (followed by hymn vv.11b–13) | **ถ้อยคำนี้เชื่อถือได้** | **Forward** (introduces the conditional-couplet hymn) |

The 2:11 KD names the locking precedent:

> GLOSSARY-LOCKED Pastoral-formula (per pastoral_corpus_locks_2026-05.md §A; corpus-locked across all 5 Pastoral occurrences). Reference-direction here is FORWARD (the saying introduced by πιστὸς ὁ λόγος is the conditional-couplet hymn that follows in vv.11b–13).

**Editorial assessment:** Compliant. The §A lock anticipates this exact unambiguous-forward case (1 Tim 4:9 was the ambiguous one). The Thai introduction reads naturally as a Christian-creedal-citation marker followed by the four-clause conditional hymn.

**LOCKED** — no action.

---

## 2. εὐσέβεια family at 3:5 + 3:12 — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §B)**

| Verse | Greek | Thai | Form |
|---|---|---|---|
| 3:5 | ἔχοντες μόρφωσιν εὐσεβείας ... τὴν δὲ δύναμιν αὐτῆς ἠρνημένοι | **มีรูปแบบของความเคร่งในพระเจ้า แต่ปฏิเสธฤทธิ์อำนาจของความเคร่งนั้น** | noun |
| 3:12 | ζῆν εὐσεβῶς ἐν Χριστῷ Ἰησοῦ | **ดำเนินชีวิตอย่างเคร่งในพระเจ้าในพระเยซูคริสต์** | adverb |

The §B "when-to-revisit" clause flagged 3:5 specifically: *"If 2 Tim 3:5 (ἔχοντες μόρφωσιν εὐσεβείας) reads awkwardly with ความเคร่งในพระเจ้า, consider whether a paired noun handles the μόρφωσις contrast better than literal nesting."* The 3:5 KD addresses this directly:

> Per uW figs-explicit: μόρφωσις = outward-form/appearance (vs. inner-substance). Distinct from μορφή (essence/intrinsic-nature, PHP 2:6 christ_hymn_kenosis_2026-05.md lock). Render 'รูปแบบ' (form/format/outward-appearance) — preserves the surface-vs-substance contrast.

**Editorial assessment:** The Thai **มีรูปแบบของความเคร่งในพระเจ้า ... แต่ปฏิเสธฤทธิ์อำนาจของความเคร่งนั้น** reads cleanly — the "ของความเคร่งในพระเจ้า ... ของความเคร่งนั้น" anaphora carries the form-vs-power contrast naturally without needing a paired noun reformulation. The §B revisit-trigger is therefore not engaged. The adverb form εὐσεβῶς at 3:12 takes the natural derivation **อย่างเคร่งในพระเจ้า** matching §B's verbal-form pattern.

The 3:5 KD also explicitly preserves the **μόρφωσις vs. μορφή** lexical distinction with the existing `christ_hymn_kenosis_2026-05.md` lock — the Pauline-corpus disambiguation operates correctly across both Pastoral and Pauline-Christological domains.

**LOCKED** — no action.

---

## 3. σωτήρ at 1:10 — Pastoral Christological-shift confirmed bidirectional (Father AND Christ) — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §C)**

This is **the FIRST σωτήρ-applied-to-Christ occurrence in the Pastorals** (after 1 Tim 1:1, 2:3, 4:10 all to God-the-Father). Confirms §C's bidirectional Christological-pattern.

> 2 Tim 1:10 GK: φανερωθεῖσαν δὲ νῦν διὰ τῆς ἐπιφανείας **τοῦ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ**
> TH: บัดนี้ พระคุณนั้นได้ทรงปรากฏแจ้งแล้วโดยการทรงปรากฏของ**พระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา**

**Editorial assessment:** **พระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา** uses the same **พระผู้ช่วยให้รอด** lemma as God-applications (per §C uniform-rendering rule), in apposition to **พระเยซูคริสต์** rather than **พระเจ้า**. This is exactly what §C anticipates — the lemma is preserved across both referents; only the apposition-noun shifts (God vs. Christ). The corpus pattern (6× Father-Savior + 4× Christ-Savior across the Pastorals) is confirmed operating correctly here.

The 1:10 verse sits inside the credal-hymn fragment vv.9–10 — making this the densest single-verse Pastoral Christology in 2 Timothy: σωτήρ-as-Christ + ἐπιφάνεια-as-incarnation + θάνατος-καταργέω + ζωὴ-καὶ-ἀφθαρσία through the gospel.

**LOCKED** — no action. (Sets corpus-precedent for Tit 1:4 χάρις καὶ εἰρήνη ἀπὸ θεοῦ πατρὸς καὶ Χριστοῦ Ἰησοῦ τοῦ σωτῆρος ἡμῶν, where the Pauline-letter-opening pattern would apply directly.)

---

## 4. ἐπιφάνεια bidirectional (incarnation 1:10; second-coming 4:1, 4:8) — **STABLE (undocumented; recommend brief new doc — high Pastoral-forward priority)**

The §L#6 follow-up doc flagged at 1TI end-of-book (`epiphaneia_christou_2026-05.md`) was deferred pending ship of 2 Tim 1. With 2 Tim 1, 4 now shipped, this is the moment to write it. The corpus evidence is now densest:

| Verse | Greek context | Thai | Sense |
|---|---|---|---|
| 1 Tim 6:14 | μέχρι τῆς ἐπιφανείας τοῦ κυρίου | **การเสด็จมาปรากฏของพระเยซูคริสต์องค์พระผู้เป็นเจ้า** | second-coming |
| 2 Tim 1:10 | διὰ τῆς ἐπιφανείας τοῦ σωτῆρος ἡμῶν | **โดยการทรงปรากฏของพระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา** | **first-coming (incarnation)** |
| 2 Tim 4:1 | καὶ τὴν ἐπιφάνειαν αὐτοῦ καὶ τὴν βασιλείαν αὐτοῦ | **และ ... การทรงปรากฏของพระองค์ และอาณาจักรของพระองค์** | second-coming |
| 2 Tim 4:8 | πᾶσιν τοῖς ἠγαπηκόσι τὴν ἐπιφάνειαν αὐτοῦ | **ทุกคนที่ได้รักการทรงปรากฏของพระองค์** | second-coming |

**Editorial observation — the Thai rendering shifts subtly between 1 Tim 6:14 and 2 Tim 1:10:** 1 Tim 6:14 uses the heavier compound **การเสด็จมาปรากฏ** (เสด็จ-มา-ปรากฏ); 2 Tim 1:10, 4:1, 4:8 all use the simpler **การทรงปรากฏ** (ทรง-ปรากฏ). The 2 Tim 1:10 KD names the principled difference:

> ἐπιφάνεια → การทรงปรากฏ (royal-prefix appearance). Per uW figs-explicit: ἐπιφάνεια here = the Incarnation/first-coming (encompassing Christ's becoming-human, life, death, resurrection) — distinct from 1 Tim 6:14 + 2 Tim 4:1, 4:8 + TIT 2:13 where ἐπιφάνεια = second-coming. Both senses preserved by single Thai lemma.

The 4:1 KD confirms the second-coming-context returns to **การทรงปรากฏ** (not **การเสด็จมาปรากฏ**) — meaning the lighter Thai compound is now the de facto 2 Tim default for ἐπιφάνεια regardless of first-vs-second-coming. The 1 Tim 6:14 heavier compound was the only outlier.

**Editorial assessment:** This is a **principled and elegant solution** — using one Thai lemma (**การทรงปรากฏ**) for the Greek lemma (ἐπιφάνεια), with context disambiguating first-vs-second-coming exactly as the Greek does. However, the **1 Tim 6:14 vs 2 Tim 1:10 surface mismatch** (เสด็จมาปรากฏ vs. ทรงปรากฏ) is mild lemma-drift across two letters within the same Pastoral-corpus and within a 5-occurrence corpus-set. **Worth surfacing for Ben's confirmation: should the 1 Tim 6:14 occurrence be retroactively conformed to การทรงปรากฏ for full corpus-uniformity, or is the 1 Tim 6:14 second-coming-context warrant for the heavier compound?** (Both readings defensible — 1 Tim 6:14 is the densest παρουσία-style "until-his-appearing" eschatological summary in the Pastorals; the 4:1 + 4:8 occurrences in 2 Tim are arguably similar in eschatological-intensity, yet take the lighter compound.)

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/epiphaneia_christou_2026-05.md` **before Tit 2:11 + 2:13 ship**. The doc should:
1. Lock ἐπιφάνεια → **การทรงปรากฏ** (single Thai lemma; context disambiguates first-vs-second-coming)
2. Note the dual application (incarnation 2 Tim 1:10 + Tit 2:11; second-coming 1 Tim 6:14 + 2 Tim 4:1, 4:8 + Tit 2:13)
3. **Decide the 1 Tim 6:14 conformation question** — either (a) retroactive harmonization to **การทรงปรากฏ** for full corpus-uniformity, or (b) preserve **การเสด็จมาปรากฏ** there as a context-specific eschatological-intensifier
4. Cross-reference `parousia_christou_2026-05.md` for the παρουσία complementary-lemma
5. Cite 2 Tim 1:10 as the densest Pastoral-corpus-Christological-summary occurrence

---

## 5. ὑγιαίνω sound-doctrine metaphor at 1:13 + 4:3 — **STABLE (undocumented; recommend new doc — same as 1TI §L#3)**

| Verse | Greek | Thai | Construction |
|---|---|---|---|
| 1:13 | ὑποτύπωσιν ἔχε ὑγιαινόντων λόγων | **จงยึดถือแบบอย่างของถ้อยคำอันถูกต้อง** | "sound words" — apostolic tradition |
| 4:3 | τῆς ὑγιαινούσης διδασκαλίας οὐκ ἀνέξονται | **คนจะทนคำสอนอันถูกต้องไม่ได้** | "sound doctrine" — eschatological apostasy |

The 1:13 KD names the corpus-lock:

> ὑγιαίνω → ถูกต้อง (CORPUS-LOCKED from 1 Tim 1:10 ὑγιαίνουσα διδασκαλία; recurs 1 Tim 6:3, 2 Tim 1:13, 4:3, TIT 1:9, 1:13, 2:1, 2:2). Per uW figs-metaphor: ὑγιαίνω = 'healthy / sound / not-corrupted' — words-like-healthy-food metaphor. Thai 'ถูกต้อง' preserves the doctrinal-soundness sense.

**Editorial assessment:** Both 2 Tim occurrences comply with the de-facto corpus default established at 1 Tim 1:10. The metaphor-flattening rationale (Thai has no idiomatic equivalent of body-health-as-doctrinal-correctness) is preserved. The **doc-lift remains pending** — `hygiaino_sound_doctrine_2026-05.md` was 1TI §L#3 priority but not yet written. With 2 Tim shipped, **4 of the 8 corpus-occurrences are now in scope** (1 Tim 1:10 + 6:3 + 2 Tim 1:13 + 4:3); Titus adds 4 more (1:9; 1:13; 2:1; 2:2 — densest single-letter cluster).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/hygiaino_sound_doctrine_2026-05.md` **before Tit 1 ships**. The doc should:
1. Lock ὑγιαίνω + διδασκαλία → **คำสอนอันถูกต้อง**
2. Lock ὑγιαίνω + λόγος → **ถ้อยคำอันถูกต้อง**
3. Document the metaphor-flattening rationale (Thai reader-cognition preserved; medical-Greek-imagery sacrificed)
4. Cite 1 Tim 1:10 as the locking precedent + 2 Tim 1:13 as the densest "preserve-pattern-of-sound-words" pastoral-charge
5. Note the contrast-pair: ἑτεροδιδασκαλέω (1 Tim 1:3, 6:3) — false-teaching antonym

---

## 6. παραθήκη "deposit" cluster at 1:12, 1:14 — **STABLE (undocumented; brief doc would aid Pastoral-corpus consistency)**

The Pastoral-distinctive **entrustment-vocabulary** appears 3× across the Pastorals (1 Tim 6:20; 2 Tim 1:12, 14). All three uniformly render **สิ่งที่ฝากไว้**.

| Verse | Greek | Thai | Direction |
|---|---|---|---|
| 1 Tim 6:20 | τὴν παραθήκην φύλαξον | **จงรักษาสิ่งที่ฝากไว้** | God→Timothy |
| 2 Tim 1:12 | τὴν παραθήκην μου φυλάξαι | **รักษาสิ่งที่ฝากไว้นั้น** | **AMBIGUOUS** (Paul→God or God→Paul) |
| 2 Tim 1:14 | τὴν καλὴν παραθήκην φύλαξον | **จงรักษาสิ่งที่ฝากไว้อันดีงาม** | God→Timothy |

The 1:12 KD names the **deliberate ambiguity-preservation** at the central occurrence:

> παραθήκη → สิ่งที่ฝากไว้ (corpus-precedent 1 Tim 6:20). Per uW figs-possession + figs-metaphor: μου (genitive) ambiguous between (1) deposit-from-me (Paul deposited with God — his life/eternal-rewards) or (2) deposit-given-to-me (God deposited gospel/ministry with Paul). Render 'สิ่งที่ฝากไว้นั้น' (preserves both directions).

**Editorial assessment:** The Thai **สิ่งที่ฝากไว้** is a **structurally-elegant solution** — Thai's flexible "ที่ฝากไว้" passive-relative leaves the deposit-direction grammatically open (can read as "what-was-deposited" without specifying who-deposited or who-received). The 1:12 vs 1:14 pair (ambiguous + clear God→Timothy) bookends the appeal-to-faithful-preservation theme. The corpus-pattern is **principled and uniform**.

The lemma is **corpus-distinctive** to the Pastorals (no NT occurrences outside these three) — making this a candidate for a brief corpus doc that locks the Thai rendering + documents the 1:12 ambiguity-preservation principle.

**Recommend: STABLE; consider brief new doc** `docs/translator_decisions/paratheke_pastoral_deposit_2026-05.md` (low priority — only 3 corpus-occurrences and no further Pastoral-letter occurrences expected; Tit doesn't use the lemma). Alternative: include as a §I sub-section in `pastoral_corpus_locks_2026-05.md` (since the corpus-set is closed at 3 occurrences).

---

## 7. 2 Tim 2:11–13 conditional-couplet hymn — **STABLE (verse-level rationale comprehensive; significant for early-Christian-creed scholarship)**

The four-clause hymn introduced by πιστὸς ὁ λόγος (v.11):

> εἰ συναπεθάνομεν, καὶ συζήσομεν (a)
> εἰ ὑπομένομεν, καὶ συμβασιλεύσομεν (b)
> εἰ ἀρνησόμεθα, κἀκεῖνος ἀρνήσεται ἡμᾶς (c)
> εἰ ἀπιστοῦμεν, ἐκεῖνος πιστὸς μένει· ἀρνήσασθαι ἑαυτὸν οὐ δύναται (d — climactic asymmetry)

Thai rendering preserves the four-clause structure with conditional-couplet parallelism for a/b/c, then **breaks the parallel pattern at d** (πιστὸς μένει + the negative grounded in God's-being) exactly as the Greek does:

> ถ้าเราตายกับพระองค์ เราจะมีชีวิตอยู่กับพระองค์ด้วย / ถ้าเราอดทน เราจะครองราชย์ร่วมกับพระองค์ด้วย / ถ้าเราปฏิเสธพระองค์ พระองค์ก็จะทรงปฏิเสธเราด้วย / ถ้าเราไม่ซื่อสัตย์ พระองค์ก็ยังคงสัตย์ซื่อ พระองค์ทรงปฏิเสธพระองค์เองไม่ได้

The 2:13 KD names the climactic-asymmetry handling:

> Important to NOT translate δύναμαι as 'not powerful enough' — the negation here is constitutive, not power-based: God's-very-being is faithful, so denial-of-self is impossibility-by-nature.

**Editorial assessment:** **Principled and theologically-precise.** The σύν-Χριστῷ Pauline-pattern (συναποθνῄσκω + συζάω + συμβασιλεύω) is preserved through the Thai **กับพระองค์ / ร่วมกับพระองค์** repetition. The asymmetry at v.13b — God's-faithfulness grounded in his own-being, not contingent on human-faithfulness — is a **load-bearing-theological-claim** for Pauline assurance + perseverance doctrine, and the Thai construction (พระองค์ทรงปฏิเสธพระองค์เองไม่ได้, "he-cannot-deny-himself") preserves the constitutive-impossibility correctly without flattening into a power-based modality.

**Recommend: STABLE — no new doc needed.** Verse-level rationale is comprehensive. Significant for early-Christian-creed scholarship (resembles other credal-fragments at 1 Tim 3:16, Phil 2:6–11, Col 1:15–20) but uniquely-Pastoral in its conditional-couplet form.

---

## 8. 2 Tim 2:15 ὀρθοτομέω + ἀνεπαίσχυντος HAPAX cluster — **REVIEW (metaphor-flattening high-stakes)**

The famous "rightly-handling-the-word-of-truth" verse with two HAPAX:

> 2 Tim 2:15 GK: σπούδασον σεαυτὸν δόκιμον παραστῆσαι τῷ θεῷ, ἐργάτην **ἀνεπαίσχυντον**, **ὀρθοτομοῦντα** τὸν λόγον τῆς ἀληθείας.
> TH: จงเพียรพยายามที่จะถวายตัวเองต่อพระเจ้าในฐานะผู้ที่ทรงรับรอง เป็นคนทำงาน**ที่ไม่ต้องอับอาย** ผู้ที่**จัดการพระวจนะแห่งความจริงอย่างตรงเที่ยง**

The 2:15 KD names the metaphor-debate:

> HAPAX ὀρθοτομέω (only here NT, compound ὀρθός + τέμνω) → จัดการ ... อย่างตรงเที่ยง (handle-rightly / cut-straight). The metaphor's precise image is debated — woodworking (cutting-straight), road-building (laying-straight-path), or sacrificial-cutting (proper-priestly-handling). Render 'จัดการ ... อย่างตรงเที่ยง' — flatter than the literal Greek but preserves the orthopraxy-of-handling-truth functional sense.

**Editorial assessment:** The Thai **จัดการ ... อย่างตรงเที่ยง** is a **principled metaphor-flattening** — Thai has no single-word-equivalent of the τέμνω-based imagery (cut-straight). The Greek itself does not unambiguously commit to a single metaphor (the three options are scholarly debate). The Thai render preserves the functional force (orthopraxy + uprightness in handling-truth) without forcing a metaphor-choice.

**The REVIEW flag:** This is one of the **most-cited verses in evangelical-Protestant Bible-handling discourse** (KJV "rightly dividing the word of truth" became the slogan of early-20th-century-American dispensational-hermeneutics + Scofield Reference Bible tradition). Modern English translations diverge:
- **BSB / NIV / CSB**: "correctly handling the word of truth" / "rightly handling" (function-based, like Eremos)
- **ESV**: "rightly handling the word of truth" (function-based)
- **KJV / NKJV**: "rightly dividing the word of truth" (metaphor-preserving, woodworking-flavor)
- **NLT**: "correctly explains the word of truth" (interpretive expansion)

The Eremos rendering aligns with BSB/NIV/CSB/ESV (mainstream evangelical-modern-critical translations). Worth Ben's confirmation that the metaphor-flattening is the corpus-default for HAPAX-with-debated-metaphor cases (compare 1 Tim 1:10's ὑγιαίνω metaphor-flattening; pattern is consistent — Thai prefers function over surface-image when the Greek metaphor has no idiomatic Thai equivalent).

**Recommend: REVIEW** — confirm the metaphor-flattening principle with Ben. No new doc needed.

---

## 9. 2 Tim 3:16 πᾶσα γραφὴ θεόπνευστος — **DECIDE (πᾶσα distributive-vs-collective ambiguity preserved + θεόπνευστος etymological-image flattened)**

The single most-cited evangelical-Protestant inspiration prooftext in the NT, with **three HAPAX** (θεόπνευστος + ἐλεγμός + ἐπανόρθωσις) and a load-bearing grammatical ambiguity:

> 2 Tim 3:16 GK: πᾶσα γραφὴ θεόπνευστος καὶ ὠφέλιμος πρὸς διδασκαλίαν, πρὸς ἐλεγμόν, πρὸς ἐπανόρθωσιν, πρὸς παιδείαν τὴν ἐν δικαιοσύνῃ
> TH: **พระคัมภีร์ทุกตอน**ได้รับการดลใจจากพระเจ้า และมีประโยชน์สำหรับการสอน สำหรับการตักเตือน สำหรับการแก้ไข และสำหรับการอบรมในเรื่องความชอบธรรม

The 3:16 KD names the πᾶσα ambiguity:

> Per uW figs-explicit + grammar: πᾶσα ambiguous — 'every / all of'; γραφή anarthrous so could be (1) 'every-passage-of-Scripture' (distributive) or (2) 'all-Scripture-as-a-whole' (collective). Render 'ทุกตอน' — Thai's distributive-collective 'ทุก-' preserves both readings.

And the θεόπνευστος etymology:

> HAPAX θεόπνευστος (only here NT, compound θεός + πνέω) → ได้รับการดลใจจากพระเจ้า (be-divinely-inspired). Per uW figs-metaphor: 'breathed-out-by-God' — Scripture as divine-utterance, not merely human-document-blessed-by-God. Thai 'ได้รับการดลใจ' is the established-Thai-Christian theological term.

**Editorial assessment:** **Both choices are defensible but principled-departures from the Greek surface.**

(a) **πᾶσα γραφή → พระคัมภีร์ทุกตอน** — the distributive **ทุก-** in Thai naturally reads "every passage" but functionally encompasses "all-of" as well; this matches how mainstream English handles the same ambiguity (BSB/NIV/CSB/ESV all default to "all Scripture" but support "every Scripture" as the alternative). The Eremos rendering is **principled per uW figs-explicit**.

(b) **θεόπνευστος → ได้รับการดลใจจากพระเจ้า** — flattens the compound's etymological **breath-image** (θεός "God" + πνέω "breathe-out") into the established-Thai-Christian theological term **การดลใจ** ("inspiration / inspired-utterance"). The Thai **การดลใจ** does NOT carry the breathing-imagery — it's closer to "infused-by-divine-spirit" with no respiratory metaphor. The literal-etymological rendering would be **ลมหายใจของพระเจ้า** ("the breath of God") or **ที่พระเจ้าทรงเป่าออก** ("which God breathed-out") — both heavier and less idiomatic in Thai-Christian register.

**The DECIDE question:** This verse is **the load-bearing prooftext** for evangelical-Protestant doctrine of biblical inspiration (cited in confessional documents, statements of faith, seminary curricula across Thai evangelical churches and missions seminaries). The Eremos rendering aligns with mainstream Thai-evangelical translations (TNCV, THSV) which similarly use **การดลใจ** — but a CC0 Bible whose stated value is preserving Greek-imagery (per the ὑγιαίνω + Pastoral-corpus pattern, the project usually avoids flattening when a literal-Thai rendering exists) **could** opt for **ลมหายใจของพระเจ้า** here to honor the etymological breath-metaphor that θεόπνευστος uniquely carries.

The **πᾶσα-distributive question** is a separate strand: should the corpus commit to **distributive** (ทุกตอน, "every passage") or **collective** (ทั้งสิ้น, "all of Scripture as a whole")? Modern Greek grammar slightly favors distributive (anarthrous πᾶσα + singular noun = "every" without article; cf. Eph 2:21 πᾶσα οἰκοδομή). Thai **ทุกตอน** preserves this — but a Thai reader with a high-view-of-Scripture-as-corpus may default-read it as "all of Scripture" (the collective sense). Both readings are theologically-equivalent (every-passage ⊂ all-of-Scripture-as-whole).

**Recommend: DECIDE** — Ben's confirmation needed. Two sub-questions:
1. Should θεόπνευστος render with the literal **breath-image** (ลมหายใจของพระเจ้า / ที่พระเจ้าทรงเป่าออก) or the established-Thai-Christian **inspiration** term (การดลใจ as currently)? The breath-image preserves more of the Greek but breaks Thai-evangelical-register consistency with TNCV / THSV.
2. Should πᾶσα γραφή commit to **distributive** (ทุกตอน, current) or **collective** (ทั้งสิ้น), or is the current Thai's distributive-collective dual-reading sufficient?

Worth surfacing to external AI reviewers given the verse's prominence + the etymological-vs-idiomatic trade-off.

---

## 10. 2 Tim 3:8 Ἰάννης + Ἰαμβρῆς extra-canonical names — **REVIEW (transliteration choice + thai_summary handling)**

The two HAPAX names appearing in canonical Scripture but drawn from extra-canonical Jewish-tradition (Targum Pseudo-Jonathan; Damascus Document CD 5:18-19; Pliny NH 30.11):

> 2 Tim 3:8 GK: ὃν τρόπον δὲ **Ἰάννης καὶ Ἰαμβρῆς** ἀντέστησαν Μωϋσεῖ
> TH: ฉันเดียวกันกับที่**ยันเนสและยัมเบรส**ได้ต่อต้านโมเสส

The 3:8 KD names the transliteration choice:

> Per uW translate-names: HAPAX names Ἰάννης + Ἰαμβρῆς (only here NT) — extra-canonical-Jewish-tradition names for the magicians of Pharaoh in Exod 7-9. Render Thai Christian transliteration ('ยันเนส' + 'ยัมเบรส' following Greek-pronunciation pattern).

And the thai_summary frames the extra-canonical-source openly for Thai readers:

> ยันเนส (Ἰάννης) และยัมเบรส (Ἰαμβρῆς) เป็นชื่อที่ปรากฏในคำสอนของชาวยิวนอกคัมภีร์ (เช่น Targum Pseudo-Jonathan และเอกสารคัมภีร์ทะเลตาย) — ระบุว่าเป็นนักเวทมนตร์สองคนของฟาโรห์ที่ต่อต้านโมเสสตามที่บันทึกไว้ในอพยพ 7-9

**Editorial assessment:** The **Thai-Christian transliteration** is principled — follows Greek-pronunciation (Ἰά → ยา; -ννης → -นเนส) producing **ยันเนส** rather than English-Anglicized "Jannes." Likewise **ยัมเบรส** for Ἰαμβρῆς. The transliteration matches typical Thai-evangelical conventions for extra-canonical NT names (compare ALEXANDER ὁ χαλκεύς → อเล็กซานเดอร์ at 4:14, where the same letter has another Alexander known from extra-Pauline sources).

The **thai_summary's open-acknowledgment of the extra-canonical source** is editorially noteworthy — frames "in Jewish-tradition outside Scripture" without dismissing the Pauline citation as unreliable. This is the **right scholarly handling** for a CC0 evangelical-Protestant Thai Bible — Thai readers benefit from understanding why these names are NOT in their OT (Exodus 7-9 names neither magician), preserving Pauline-typology authority while showing Paul-as-rhetor drawing on broadly-known Jewish-haggadic tradition.

**The REVIEW flag** is not a request to change the rendering or summary — it's a flag that **for a CC0 Thai Bible serving missions-context Thai readers**, an explicit thai_summary that surfaces an extra-canonical source is **rare in Thai Bible editions** (TNCV / THSV typically transliterate without explanation; only NRSV / NRSVue / CEB tend toward this open-handling in English). Worth Ben's confirmation that the open-acknowledgment is the corpus-default for canonical-citations-of-extra-canonical-tradition.

**Recommend: REVIEW** — confirm with Ben. No new doc needed (verse-level handling is comprehensive). If confirmed as corpus-default, this approach should propagate forward to Jude 14-15 (1 Enoch 1:9 citation) and any other extra-canonical-citation cases.

---

## 11. 2 Tim 3:6–7 γυναικάρια — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §E forward-applicability clause)**

The diminutive lemma γυναικάριον (HAPAX) — the feminine-pejorative-or-sympathetic noun the 1TI lock §E forward-flagged:

> 2 Tim 3:6 GK: αἰχμαλωτίζοντες **γυναικάρια** σεσωρευμένα ἁμαρτίαις
> TH: จับ**ผู้หญิงอ่อนแอ**ที่แบกภาระบาปจำนวนมากไว้เป็นเชลย

The §E forward-applicability clause says:

> 2 Tim 3:6–7 (silly women / γυναικάρια): preserve the rhetorical force without commenting on whether women-in-general are characterized; the diminutive γυναικάριον is the abusive term, not γυνή.

The 3:6 KD aligns:

> HAPAX γυναικάριον (only here NT, diminutive of γυνή) → ผู้หญิงอ่อนแอ (vulnerable-woman). Per pastoral_corpus_locks_2026-05.md §E (women-in-worship ambiguity strategy carrying forward to 2 Tim 3:6-7) ... render preserves the vulnerability-of-the-victims (not contempt-for-women); the abusive register attaches to the false-teachers, not the women they prey upon.

**Editorial assessment:** **Compliant with §E.** The Thai **ผู้หญิงอ่อนแอ** ("vulnerable woman") preserves the diminutive's connotation-of-vulnerability without inflating it into general-feminine-pejorative ("silly women" — the KJV / older-English option). The thai_summary unpacks the diminutive carefully ("คำเล็กน้อย ... เน้นว่าผู้สอนเท็จเลือกเฉพาะผู้ที่อ่อนแอ ... เป็นเหยื่อง่าย"), placing the abusive-rhetorical-force on the false-teachers' predatory targeting, not on the women themselves. This is the editorially-correct handling per modern feminist-attentive-evangelical scholarship.

**LOCKED** — no action.

---

## 12. 2 Tim 1:11 διδάσκαλος textual variant + 2 Tim 2:14 θεοῦ/κυρίου textual variant — **LOCKED (silent-omission per RULES §5)**

Both variants are dispositioned in `output/textual_variants/_resolved/`:

| Variant | SBLGNT | Byzantine/some | Eremos | Disposition |
|---|---|---|---|---|
| 1:11 διδάσκαλος | shorter (no ἐθνῶν) | διδάσκαλος ἐθνῶν (1 Tim 2:7 harmonization) | shorter | silent-omission (BSB/ESV/NIV/CSB consensus) |
| 2:14 θεοῦ/κυρίου | κυρίου | θεοῦ (Byzantine) | κυρίου per SBLGNT → องค์พระผู้เป็นเจ้า | silent-omission (mainstream English ironically reads θεοῦ but theological force preserved either way) |

The 2:14 variant is **interesting** — modern English Bibles (BSB/ESV/NIV/CSB/NASB) all read "before God" (θεοῦ) while the SBLGNT critical-text apparatus actually reads κυρίου. The resolved-doc explains this as either (a) older NA editions had θεοῦ, or (b) the rhetorical-equivalence is treated as exegetical-non-difference. The Eremos translation correctly follows SBLGNT (RULES §0) → **องค์พระผู้เป็นเจ้า** (corpus-locked κύριος rendering); silent-omission is principled because both readings serve the same divine-witness-charge function.

**Editorial assessment:** Both resolved-docs are **comprehensive and well-reasoned**. The 1:11 variant is textbook-scribal-harmonization (filling out the parallel to 1 Tim 2:7's triple-office with ἐθνῶν); the 2:14 variant illustrates SBLGNT-strict-compliance even when mainstream English translations diverge due to older NA editions. Neither warrants Tier-2 footer-note treatment (no entrenched-confessional-prooftext function like 1 Tim 3:16 had).

**LOCKED** — no action.

---

## 13. δεσπότης at 2 Tim 2:21 — household-master register — **STABLE (compliant with 1TI §7 disambiguation)**

The 2 Tim 2:21 occurrence is **household-master**, not the Christological σωτήρ-shift, fitting the οἰκία (great-house) frame from v.20:

> 2 Tim 2:21 GK: εὔχρηστον **τῷ δεσπότῃ** εἰς πᾶν ἔργον ἀγαθὸν ἡτοιμασμένον.
> TH: มีประโยชน์แก่**นาย** และพร้อมสำหรับการดีทุกอย่าง

Render **นาย** ("master") matches 1 Tim 6:1, 6:2 (human-master register, no royal-prefix). The 2:21 KD explicitly notes:

> δεσπότης (master) here is the household-master, fitting the οἰκία frame; NOT the Christological σωτήρ shift.

**Editorial assessment:** **Compliant with 1TI §7 δεσπότης / κύριος disambiguation.** The Pastoral-corpus disambiguation principle holds — δεσπότης gets plain **นาย** (no royal-prefix) when the context is household / human-master imagery; the divine-Lord κύριος retains **องค์พระผู้เป็นเจ้า**. This is one of the inversion-pattern occurrences (sometimes God/Christ, sometimes human-master); the verse-level rationale is comprehensive enough.

**STABLE** — no action; the eventual `despotes_pauline_general_2026-XX.md` doc-when-2-Pet-and-Jude-are-shipped (per 1TI §7) remains pending.

---

## 14. ἐκείνη ἡ ἡμέρα Pastoral-eschatological idiom (1:12, 1:18, 4:8) — **STABLE (uniform; consider corpus-doc later)**

The "that day" Pastoral-idiom occurs **3× in 2 Timothy alone** (1:12, 1:18, 4:8) plus **1 Tim** doesn't use it. All three render uniformly **วันนั้น** ("that day") with eschatological-context cues making the future-judgment-day reference clear:

| Verse | Context | Thai |
|---|---|---|
| 1:12 | δυνατός ἐστιν ... φυλάξαι εἰς ἐκείνην τὴν ἡμέραν | **จนกระทั่งถึงวันนั้น** |
| 1:18 | δῴη αὐτῷ ὁ κύριος εὑρεῖν ἔλεος ... ἐν ἐκείνῃ τῇ ἡμέρᾳ | **ในวันนั้น** |
| 4:8 | ὃν ἀποδώσει μοι ὁ κύριος ἐν ἐκείνῃ τῇ ἡμέρᾳ | **ในวันนั้น** |

**Editorial assessment:** The Thai **วันนั้น** preserves the Pastoral-distinctive idiom literally — distinct from the broader Pauline ἡμέρα-Χριστοῦ / ἡμέρα-κυρίου constructions (which would translate as **วันแห่งพระคริสต์ / วันขององค์พระผู้เป็นเจ้า** per Pauline-corpus precedent). The minimal **วันนั้น** preserves Pastoral-corpus distinctiveness. Worth a brief note in any future Pastoral-eschatology doc, but not gating.

**STABLE — no new doc needed** (low-priority candidate for a future Pastoral-eschatological-vocabulary doc combining ἐπιφάνεια + ἐκείνη ἡ ἡμέρα + Pastoral βασιλεία-ἐπουράνιος).

---

## 15. Inherited locks — **all compliant**

| Doc | 2 Tim evidence | Status |
|---|---|---|
| `pastoral_corpus_locks_2026-05.md` §A (πιστὸς ὁ λόγος) | 2:11 — exact match **ถ้อยคำนี้เชื่อถือได้** | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §B (εὐσέβεια family) | 3:5 noun **ความเคร่งในพระเจ้า**; 3:12 adverb **อย่างเคร่งในพระเจ้า** | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §C (σωτήρ Pastoral-shift) | 1:10 first σωτήρ-applied-to-Christ in Pastorals → **พระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา** (uniform-lemma rule) | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §E (women-in-worship) | 3:6–7 γυναικάρια → **ผู้หญิงอ่อนแอ** (preserves diminutive vulnerability without inflation) | **LOCKED** |
| `ekklesia_2026-04.md` | **N/A in 2TI** — no ἐκκλησία occurrences in this letter | **LOCKED (N/A)** |
| `diakonos_pauline_2026-05.md` | 1:18 διηκόνησεν → **ปรนนิบัติ** (general service); 4:5 διακονίαν → **พันธกิจ** (Timothy's ministry); 4:11 διακονίαν → **งานพันธกิจ** (Mark's usefulness for ministry); 2:24 δοῦλον κυρίου → **ผู้รับใช้ขององค์พระผู้เป็นเจ้า** (general service); no formal-deacon ἐπίσκοπος/πρεσβύτερος occurrences | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 2 Tim has **17+ narrator-κύριος references** (1:2, 1:8, 1:16, 1:18, 2:7, 2:14, 2:19 ×2, 2:22, 2:24, 3:11, 4:8, 4:14, 4:17, 4:18, 4:22) all → **องค์พระผู้เป็นเจ้า** uniform. The 9-corpus-stream confirmation now extends across LUK/ACT/JHN/GAL/1TH/1CO/2CO/1TI/2TI. | **LOCKED-with-amendment-noted** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in 2TI — epistolary, no narrative-vocatives | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | 4:18 ᾧ ἡ δόξα → **ขอพระสิริมีแด่พระองค์** (doxological-formula, not narrative-praise-verb-with-object); compliant | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | 2:3 στρατιώτης → **ทหาร** (plain register, soldier-metaphor); 2:21 δεσπότῃ → **นาย** (household-master, plain register, see §13); 2:26 διάβολος → **มาร** (plain — adversary not honored); compliant | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for Paul-as-author (ข้าพเจ้า), Timothy (ท่าน), human-figures (เดมาส, ลูกา, ทิตัส, etc.); compliant | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | N/A in 2TI — no Aramaic embeds | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | Audit script PASSES strict mode. 1 candidate at 1:11 dispositioned silent-§5; plus 2:14 reading-variant resolved-doc (not an inclusion variant). | **LOCKED** |
| `historic_present_2026-04.md` | N/A — epistolary, not narrative | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 2TI | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | 2:25 μετάνοιαν → **การกลับใจ** (corpus-locked); compliant | **LOCKED** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — ἄφεσις absent from 2TI | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | N/A in 2TI — no pagan-idol references | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | N/A in 2TI — no Roman-administrative occurrences | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 2TI | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον at 1:14 → **พระวิญญาณบริสุทธิ์** (RULES §4 standard); 4:22 πνεῦμα-of-Timothy → **จิตวิญญาณ** (psyche/pneuma anthropological — appropriate plain-register); 1:7 πνεῦμα-of-character (δειλίας / δυνάμεως / ἀγάπης / σωφρονισμοῦ) → **วิญญาณ** (figurative-disposition); compliant | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — Pastoral. ἀμήν at 4:18 (single doxology-amen) → **อาเมน** (corpus-locked transliteration). | **LOCKED (N/A on doubled)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs in 2TI | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | 4:1 βασιλείαν → **อาณาจักร**; 4:18 βασιλείαν τὴν ἐπουράνιον → **อาณาจักรสวรรค์**; corpus-locked compliance. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | 4:18 ἐπουράνιος (adjective) → **สวรรค์** in compound **อาณาจักรสวรรค์** — adjectival use, no standalone οὐρανός noun in 2TI; compliant | **LOCKED** |
| `parousia_christou_2026-05.md` | N/A direct (no παρουσία noun in 2TI), but the complementary ἐπιφάνεια Pastoral-eschatological lemma is governed by the §4 follow-up doc-to-write | **LOCKED (N/A on παρουσία; ἐπιφάνεια-doc pending)** |
| `christ_hymn_kenosis_2026-05.md` | 3:5 μόρφωσις vs μορφή lexical distinction preserved (μόρφωσις → **รูปแบบ**, distinct from PHP 2:6 μορφή → **สภาพ**); compliant | **LOCKED** |
| `dikaioo_dikaiosyne_family_2026-05.md` | 2:22 δικαιοσύνην → **ความชอบธรรม**; 3:16 παιδείαν τὴν ἐν δικαιοσύνῃ → **การอบรมในเรื่องความชอบธรรม**; 4:8 ὁ τῆς δικαιοσύνης στέφανος → **มงกุฎแห่งความชอบธรรม**; 4:8 δίκαιος κριτής → **ผู้พิพากษาที่ทรงธรรม**; corpus-locked compliance | **LOCKED** |
| `nomos_pauline_2026-05.md` | N/A — νόμος absent from 2TI | **LOCKED (N/A)** |
| `sarx_pauline_2026-05.md` | N/A — σάρξ absent from 2TI | **LOCKED (N/A)** |
| `phroneo_pauline_2026-05.md` | N/A — φρονέω family absent from 2TI | **LOCKED (N/A)** |
| `pistis_christou_2026-05.md` | 1:13 ἐν πίστει + ἀγάπῃ τῇ ἐν Χριστῷ Ἰησοῦ → **ด้วยความเชื่อและความรักที่อยู่ในพระเยซูคริสต์**; 3:15 διὰ πίστεως τῆς ἐν Χριστῷ Ἰησοῦ → **โดยทางความเชื่อในพระเยซูคริสต์**; subjective-vs-objective-genitive ambiguity preserved per the doc | **LOCKED** |
| `prototokos_pauline_2026-05.md` | N/A — πρωτότοκος absent from 2TI | **LOCKED (N/A)** |
| `huiothesia_adoption_2026-05.md` | N/A — υἱοθεσία absent from 2TI | **LOCKED (N/A)** |
| `proper_noun_wordplay_2026-04.md` | N/A — no proper-noun-wordplay in 2TI | **LOCKED (N/A)** |
| `spiritual_beings_hierarchy_2026-05.md` | 2:26 διάβολος → **มาร** (corpus-locked adversary-rendering; compliant) | **LOCKED** |
| `stoicheia_tou_kosmou_2026-05.md` | N/A — στοιχεῖα absent from 2TI | **LOCKED (N/A)** |
| `telos_paidagogos_christ_2026-05.md` | N/A — παιδαγωγός absent; 3:16 παιδεία → **การอบรม** is the cognate-noun (general formative-discipline), distinct rendering from παιδαγωγός | **LOCKED (N/A)** |
| `adversary_speech_register_2026-05.md` | N/A — no adversary-direct-speech in 2TI | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in 2TI | **LOCKED (N/A)** |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | N/A — neither lemma in 2TI | **LOCKED (DEFERRED, N/A)** |
| Pauline locks confirmed in 2TI from prior books | δοξα at 2:10 + 4:18 → **พระสิริ / ศักดิ์ศรี** (doxological standard); χάρις at 1:2 + 1:9 + 2:1 + 4:22 → **พระคุณ** (corpus-locked); εἰρήνη at 1:2 + 2:22 → **สันติสุข** (corpus-locked); εὐαγγέλιον throughout → **ข่าวประเสริฐ** (RULES §4); 2:8 ἐκ νεκρῶν → **จากตาย** (resurrection-formula); 2:8 ἐκ σπέρματος Δαυίδ → **เชื้อสายของดาวิด** (corpus-locked from ROM 1:3); 4:7 τὸν καλὸν ἀγῶνα → **การต่อสู้อย่างดี** (corpus-precedent 1 Tim 6:12); 4:13 βιβλία/μεμβράνας → **หนังสือต่าง ๆ / หนังสือม้วนหนัง** (technical-distinction preserved); ψυχή/πνεῦμα anthropological at 4:22 → **จิตวิญญาณ** (compound preserves both; appropriate for closing-blessing context). | **LOCKED** ✓ |

---

## Mechanical (§1) — **all green**

- 4/4 chapters: `output/check_reports/2timothy_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 4/4 chapters: `output/back_translations/2timothy_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-129-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --book 2timothy --strict`: **PASS** (1 candidate at 1:11 silent-§5)
- `git status output/`: 2 `_resolved/` variant docs (1:11 + 2:14, both filed 2026-05-02 as part of 2 Tim 1 + 2 chapter ships); 1 modified `key_term_consistency_all.md` (regenerated by gate script); plus unrelated paratext stragglers (1CO/1TH/2CO/2TH/ACT/COL/EPH/GAL SFM files from prior book-ships). None affects translation content.
- `python3 scripts/export_to_usfm.py --book 2TI`: not yet run as part of this audit (per §1 checklist; defer to ship-script gating).

---

## Pre-existing docs affirmed / unchanged

All 40 docs in `docs/translator_decisions/` reviewed. Compliance summary in §15 above.

**One doc flagged for amendment** (extending 1TI's prior recommendation):
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend framing to "Lukan-Acts + Johannine + Pauline + Pastoral" (now confirmed across **9 corpus-streams**: LUK / ACT / JHN / GAL / 1TH / 1CO / 2CO / 1TI / 2TI). No rendering change, only doc-text update. Already flagged at 1TI §M; remains pending.

---

## Flagged for Ben's attention

### A. ἐπιφάνεια Pastoral-Christological-eschatological-lemma — **STABLE, lift to corpus doc** (§4)
2 Timothy now provides the densest 4-occurrence in-letter cluster (1:10 incarnation + 4:1 + 4:8 second-coming). Lift to corpus doc `epiphaneia_christou_2026-05.md` **before Tit 2:11, 2:13 ship**. Includes the 1 Tim 6:14 conformation-question (heavier **การเสด็จมาปรากฏ** there vs. **การทรงปรากฏ** elsewhere) — Ben to decide retroactive harmonization vs. context-specific intensifier preservation.

### B. ὑγιαίνω sound-doctrine metaphor — **STABLE, lift to corpus doc** (§5)
Pending from 1TI §L#3. 2 Tim adds 2 more occurrences (1:13 + 4:3); 4 of 8 corpus-occurrences now in scope. Lift to `hygiaino_sound_doctrine_2026-05.md` before Tit 1:9, 1:13, 2:1, 2:2 ship.

### C. παραθήκη "deposit" cluster — **STABLE, brief new doc OR fold into pastoral_corpus_locks** (§6)
3 corpus occurrences (1 Tim 6:20; 2 Tim 1:12, 14) — closed corpus-set with the 1:12 ambiguity-preservation principle worth documenting. Low priority; could be added as a §I sub-section in `pastoral_corpus_locks_2026-05.md` rather than a separate doc.

### D. 2:15 ὀρθοτομέω metaphor-flattening — **REVIEW** (§8)
Famous KJV "rightly dividing" verse. Eremos renders **จัดการ ... อย่างตรงเที่ยง** (function-based; matches BSB / NIV / CSB / ESV against KJV / NKJV). Worth Ben's confirmation that the metaphor-flattening principle is the corpus-default for HAPAX-with-debated-metaphor cases.

### E. 3:8 Ἰάννης + Ἰαμβρῆς extra-canonical-name handling — **REVIEW** (§10)
Thai-Christian transliteration **ยันเนส + ยัมเบรส**; thai_summary openly acknowledges Targum / Damascus-Document / Pliny extra-canonical sources. Worth Ben's confirmation that the open-acknowledgment is the corpus-default for canonical-citations-of-extra-canonical-tradition (carries forward to Jude 14-15).

### F. 1:12 παραθήκη ambiguity-preservation — **REVIEW** (§6)
Direction-of-deposit (Paul→God vs. God→Paul) preserved literally via **สิ่งที่ฝากไว้นั้น**. Bookended by the unambiguous 1:14 **สิ่งที่ฝากไว้อันดีงาม**. Worth Ben's confirmation that ambiguity-preservation is principled here (vs. committing to one direction with thai_summary acknowledging the alternative).

### G. 3:16 πᾶσα γραφὴ θεόπνευστος — **DECIDE** (§9)
Two sub-questions:
1. **θεόπνευστος** rendering choice — etymological breath-image (**ลมหายใจของพระเจ้า / ที่พระเจ้าทรงเป่าออก**) vs. established-Thai-Christian inspiration-term (**การดลใจ** as currently). The breath-image preserves more Greek but breaks Thai-evangelical-register consistency with TNCV / THSV.
2. **πᾶσα γραφή** ambiguity — distributive (**ทุกตอน**, current) vs. collective (**ทั้งสิ้น**) commitment, or current Thai's distributive-collective dual-reading sufficient.
Worth Ben's confirmation **before tagging `book-2timothy-v1`** given verse's centrality to evangelical-Protestant doctrine of Scripture.

### H. New corpus docs to write (priority-ordered for forward-Pastoral-corpus compounding)

**Highest priority — write before Tit 1 ships:**
1. **`docs/translator_decisions/hygiaino_sound_doctrine_2026-05.md`** (§B) — locks the sound-doctrine metaphor (4 corpus-occurrences shipped, 4 more in Titus)
2. **`docs/translator_decisions/epiphaneia_christou_2026-05.md`** (§A) — locks ἐπιφάνεια Pastoral-eschatological-term + decides 1 Tim 6:14 conformation-question

**Medium priority — write before or alongside Tit:**
3. **(Conditional)** Brief `paratheke_pastoral_deposit_2026-05.md` (§C) OR fold into `pastoral_corpus_locks_2026-05.md` as §I — locks παραθήκη-cluster + 1:12 ambiguity-preservation (only 3 corpus-occurrences total; closed-set; low priority)

**Lower priority (1TI §L#5 inheritance):**
4. **`docs/translator_decisions/pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md`** (1TI §L#5) — Tit 1:5–9 dense overseer-elder qualification cluster makes this gating before Titus ships

### I. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend framing to "Lukan-Acts + Johannine + Pauline + Pastoral" (9-corpus-stream confirmation; pending from 1TI §M)

### J. External AI review (§3 of checklist) — **pending**
Recommended before `book-2timothy-v1` tag. Suggested 4-cluster external AI packet (smaller than 1TI's 8-item; 2 Tim is shorter):
1. **2 Tim 1:9–10** — gospel-summary credal-fragment (σωτήρ-Christ + ἐπιφάνεια-incarnation + θάνατος-καταργέω + ζωὴ-καὶ-ἀφθαρσία + πρὸ χρόνων αἰωνίων)
2. **2 Tim 2:11–13** — πιστὸς ὁ λόγος + conditional-couplet hymn + climactic-asymmetry at v.13
3. **2 Tim 2:15 + 3:8** — ὀρθοτομέω HAPAX metaphor-flattening + Ἰάννης-Ἰαμβρῆς extra-canonical-handling
4. **2 Tim 3:15–17** — ἱερὰ γράμματα + πᾶσα γραφὴ θεόπνευστος + 4-fold-Scripture-utility + ἄρτιος HAPAX

Use Grok + ChatGPT + Gemini (free-tier) per the JHN / GAL / 1TH / 1CO / 2CO / 1TI pattern.

---

## Recommendation

**2 Timothy ships in strong corpus-hygiene shape** — with all five major Pastoral-distinctive clusters from `pastoral_corpus_locks_2026-05.md` confirmed compliant (πιστὸς ὁ λόγος; εὐσέβεια family; σωτήρ Pastoral-shift confirmed bidirectional with first Christ-Savior occurrence at 1:10; women-in-worship ambiguity-preservation at γυναικάρια; ὑγιαίνω implicit lock). **The translator made consistent, principled choices on the new lemma-clusters that 2 Timothy introduces** — παραθήκη ambiguity-preservation, ἐπιφάνεια bidirectional handling, the 2:11–13 hymn-fragment, the 2:15 metaphor-flattening, and the 3:16 inspiration-prooftext.

**The single highest-stakes editorial item is §G — the 2 Tim 3:16 θεόπνευστος + πᾶσα γραφή pair** — given the verse's centrality to evangelical-Protestant doctrine of Scripture. The current Thai rendering aligns with mainstream Thai-evangelical translations (TNCV / THSV) but **could** opt for a more etymologically-faithful breath-image rendering. Worth surfacing to external AI reviewers and confirming with Ben before tagging.

**The other contested items** (§D ὀρθοτομέω; §E Ἰάννης-Ἰαμβρῆς; §F 1:12 παραθήκη ambiguity) are all REVIEW-not-DECIDE — defensible-as-shipped, just worth Ben's explicit confirmation. None compound forward to Titus with high editorial-weight (§D ὀρθοτομέω has no Tit recurrence; §E Ἰάννης-Ἰαμβρῆς Jewish-haggadic-citation pattern is unique to 2 Tim 3:8; §F παραθήκη is 2-Tim-distinctive within the Pastorals).

**Tag `book-2timothy-v1` after:**
1. Ben's decision on **§G** (DECIDE: 3:16 θεόπνευστος + πᾶσα γραφή)
2. Ben's confirmation on **§D + §E + §F** (REVIEW items)
3. Two new translator_decisions docs written (§H items 1–2 minimum before Titus ships)
4. One existing doc amended (`kyrios_narrator_voice_luke_acts_2026-04.md`)
5. External AI sanity-check (§J)

The forward-Pastoral pipeline (Titus) inherits **all** of `pastoral_corpus_locks_2026-05.md` plus the new §H ἐπιφάνεια + ὑγιαίνω docs. The Pastoral-corpus is now **2 of 3 letters complete**, and the editorial-stakes for Titus are concentrated in three specific clusters: (a) Tit 1:5–9 elder-overseer qualifications (the §H#4 `pastoral_offices_*` doc-to-write); (b) Tit 2:13 Granville-Sharp σωτήρ-double-name (already pre-decided in `pastoral_corpus_locks_2026-05.md` §C); (c) Tit 1:9 + 1:13 + 2:1 + 2:2 ὑγιαίνω-densest-letter (§H#1 doc-to-write). With those three covered, Titus should ship with editorial-weight comparable to 2 Timothy.
