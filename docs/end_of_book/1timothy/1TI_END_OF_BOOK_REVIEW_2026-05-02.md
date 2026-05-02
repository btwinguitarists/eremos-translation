# 1 Timothy — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 6 chapters (113 verses; ~135 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (39 docs).
**Trigger:** 1TI 6 shipped (commit `4cf4ccb`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 6/6 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book 1timothy --strict` PASSES (4 candidates: 2 silent per RULES §5, 2 with `_resolved/` docs at 4:12 and 6:21). Three additional textual variants (4:10 ἀγωνιζόμεθα/ὀνειδιζόμεθα, 5:16 πιστὴ vs πιστὸς ἢ πιστή, 6:19 ὄντως vs αἰώνιος ζωή) are dispositioned with `_resolved/` docs but did not match the inclusion-variant signal patterns. `git status output/` carries pre-existing 1TI-3-pilot-assessment artifacts and unrelated Eph/Col paratext stragglers; none affects translation content.
- **1 Timothy is the FIRST PASTORAL EPISTLE the project has shipped** and the entry-point for a distinctive Pauline sub-corpus (1 Tim, 2 Tim, Titus). The audit confirms strong CONTINUITY with GAL + 1TH on the inherited Pauline-vocabulary set (ἐκκλησία, ἀπόστολος, ἀδελφοί, πατήρ register split, εὐχαριστέω-cluster, εἰρήνη formula, βασιλεία, narrator-κύριος, divine-passive constructions) and **introduces five major NEW corpus-cross-cutting Pastoral-distinctive clusters: (1) πιστὸς ὁ λόγος "trustworthy saying" formula (3× in 1TI; 5× across the Pastorals), (2) εὐσέβεια / εὐσεβέω piety-virtue vocabulary (10× in 1-2Tim+Titus, 4× in 1TI alone), (3) ὑγιαίνω "sound" doctrine-metaphor (with διδασκαλία + λόγος), (4) σωτήρ applied to God-the-Father not Christ — the most-distinctive Pastoral Christological-shift, and (5) ἐπιφάνεια as Christ's-second-coming-vocabulary (alongside the inherited παρουσία from 1TH).** All five recur densely in 2 Tim + Tit, so corpus-doc lift is recommended before 2 Tim 1 ships.
- **1 Timothy also introduces the church-office vocabulary cluster** ἐπίσκοπος + πρεσβύτερος + διάκονος (3:1–13; 5:17–22) — partly covered by `diakonos_pauline_2026-05.md` but now warranting an extended Pastoral-offices doc. The pilot 1Tim 3 was retained verbatim (per Ben's 2026-05-02 pilot assessment doc); its qualifications language (`ผู้ปกครองดูแล / มัคนายก / ผู้ปกครองคริสตจักร`) is the corpus precedent for Tit 1:5–9 and beyond.
- **2 inherited locks confirmed compliant** (ekklesia, diakonos_pauline). **15 inherited Synoptic / John / Acts / Pauline locks compliant or N/A** in 1TI (see §16).
- **Inclusion-variant gate clean.** All 4 audit-flagged candidates have explicit dispositions; 7 `_resolved/` docs cover the broader textual-variant set (1:17, 2:7, 4:10, 4:12, 5:16, 6:19, 6:21). RULES §0 SBLGNT-strictness held throughout; no Tier 1/2/3 inclusion brackets needed.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: ἀρσενοκοίτης rendering at 1:10; μιᾶς γυναικὸς ἄνδρα formula at 3:2 / 5:9; 3:16 Ὃς vs Θεός Christ-hymn variant compliance).
- **3 items flagged DECIDE** (1 Tim 2:11–12 αὐθεντέω + women-in-worship interpretive-ambiguity-preservation strategy; 1 Tim 2:15 σωθήσεται διὰ τῆς τεκνογονίας; 1 Tim 3:11 γυναῖκας — wives-of-deacons vs women-deacons crux).
- **External AI review (§3) packet pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πιστὸς ὁ λόγος — "trustworthy saying" Pastoral formula — **STABLE (undocumented; recommend new doc — high Pastoral-forward priority)**

The Pastoral-distinctive citation-formula occurs **3× in 1 Timothy** (1:15; 3:1; 4:9) and **5× across the Pastorals** (adding 2 Tim 2:11; Tit 3:8). All three 1 Tim occurrences render uniformly **ถ้อยคำนี้เชื่อถือได้**:

| Verse | Greek | Thai | What follows |
|---|---|---|---|
| 1:15 | πιστὸς ὁ λόγος καὶ πάσης ἀποδοχῆς ἄξιος | **ถ้อยคำนี้เชื่อถือได้และสมควรแก่การยอมรับอย่างเต็มที่** | "Christ Jesus came into the world to save sinners" |
| 3:1 | πιστὸς ὁ λόγος | **ถ้อยคำนี้เชื่อถือได้** | "If anyone aspires to overseer-office..." (forward-pointing) |
| 4:9 | πιστὸς ὁ λόγος καὶ πάσης ἀποδοχῆς ἄξιος | **ถ้อยคำนี้เชื่อถือได้และสมควรแก่การยอมรับอย่างเต็มที่** | Ambiguous: back to v.8 OR forward to v.10 |

The 3:1 KD acknowledges the formula's role:

> Formulaic phrase appearing 5x in the Pastorals (1 Tim 1:15; 3:1; 4:9; 2 Tim 2:11; Tit 3:8). Establishing 'ถ้อยคำนี้เชื่อถือได้' as the consistent Thai rendering for all five occurrences.

**Editorial assessment:** **ถ้อยคำนี้เชื่อถือได้** is principled — preserves both the literal πιστός = "trustworthy" + λόγος = "saying / utterance" and reads naturally as a Thai citation-formula introducing a quoted maxim. The longer expansion **καὶ πάσης ἀποδοχῆς ἄξιος → สมควรแก่การยอมรับอย่างเต็มที่** is uniform across the two extended forms (1:15, 4:9). The 4:9 ambiguity (back-to-v.8 vs forward-to-v.10) is preserved by the standalone-sentence treatment per uW recommendation.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/pistos_ho_logos_pastoral_formula_2026-05.md` before 2 Tim 2:11 + Tit 3:8 (the remaining two occurrences). The doc should:
1. Lock πιστὸς ὁ λόγος → **ถ้อยคำนี้เชื่อถือได้**
2. Lock πάσης ἀποδοχῆς ἄξιος → **สมควรแก่การยอมรับอย่างเต็มที่** (matched extension)
3. Note the formula is **Pastoral-distinctive** (no occurrences outside 1-2 Tim + Titus); cite the 5-occurrence corpus inventory
4. Note the ambiguity-preservation principle for cases where the referent (back vs forward) is debated (1 Tim 4:9; arguably Tit 3:8)
5. Cite 1 Tim 1:15 as the locking precedent (densest first-occurrence; saves-sinners gospel-content)

---

## 2. εὐσέβεια / εὐσεβέω — Pastoral piety-virtue vocabulary — **STABLE (undocumented; recommend new doc — highest Pastoral-forward priority)**

The Pastoral-corpus's **single most-distinctive virtue-term**. εὐσέβεια + cognates occur **10× across 1-2 Tim + Titus**, with **4× in 1 Tim alone** (2:2; 4:7, 8; 6:5, 6, 11; plus θεοσέβεια at 2:10 — close cognate; plus the verb εὐσεβέω at 5:4):

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 2:2 | ἐν πάσῃ εὐσεβείᾳ καὶ σεμνότητι | **ความเคร่งในพระเจ้าและความสง่างามทุกประการ** | civic-life godliness |
| 2:10 | θεοσέβειαν (HAPAX cognate) | **ความเคารพยำเกรงพระเจ้า** | women's-adornment piety |
| 3:16 | τὸ τῆς εὐσεβείας μυστήριον | **ข้อล้ำลึกแห่งทางของพระเจ้า** | the gospel-as-godliness-mystery |
| 4:7 | γύμναζε δὲ σεαυτὸν πρὸς εὐσέβειαν | **ฝึกตัวเองในความเคร่งในพระเจ้า** | spiritual-formation goal |
| 4:8 | ἡ εὐσέβεια πρὸς πάντα ὠφέλιμός | **ความเคร่งในพระเจ้ามีประโยชน์ในทุกทาง** | comprehensive benefit |
| 5:4 | μανθανέτωσαν ... τὸν ἴδιον οἶκον εὐσεβεῖν | **แสดงความเคร่งในพระเจ้าต่อครอบครัวของตัวเอง** | family-honoring piety |
| 6:3 | τῇ κατ' εὐσέβειαν διδασκαλίᾳ | **คำสอนที่นำสู่ความเคร่งในพระเจ้า** | doctrine-as-piety |
| 6:5 | πορισμὸν εἶναι τὴν εὐσέβειαν | **ความเคร่งในพระเจ้าเป็นเครื่องมือหากิน** | merchant-religion (false) |
| 6:6 | ἡ εὐσέβεια μετὰ αὐταρκείας | **ความเคร่งในพระเจ้าพร้อมด้วยความพอใจ** | true-gain godliness |
| 6:11 | δίωκε ... εὐσέβειαν | **ไล่ตาม ... ความเคร่งในพระเจ้า** | virtue-list pursuit |

The 2:2 KD names the rendering choice:

> εὐσέβεια → ความเคร่งในพระเจ้า (corpus-precedent at Acts 3:12 same lemma). Pastoral-key-virtue (10x in 1-2Tim + Titus).

**Editorial assessment:** **ความเคร่งในพระเจ้า** is consistently locked — preserves both the *toward-God* directionality (เคร่งใน + พระเจ้า "strict-in + God") and the broad *embodied-piety* sense (วิถีชีวิต-แห่ง-ความเคารพยำเกรง) that εὐσέβεια carries in the Pastorals. The verbal εὐσεβέω at 5:4 takes the natural verbal form **แสดงความเคร่งในพระเจ้า** ("show / manifest εὐσέβεια"). The cognate **θεοσέβεια** (HAPAX, 2:10) gets a slightly-different **ความเคารพยำเกรงพระเจ้า** to preserve the lexical distinction (compound θεός + σέβομαι emphasizing reverence specifically toward God, not the broader Pastoral-piety semantic).

The most-substantive editorial choice is at **3:16** — the εὐσεβείας μυστήριον is rendered **ข้อล้ำลึกแห่งทางของพระเจ้า** ("the mystery of *the way-of-God*") rather than mechanical ความเคร่งในพระเจ้า. The 3:16 KD argues this captures both the devotional and practical dimensions of εὐσέβεια as the Pastorals' near-summary term for "authentic-Christian-life-and-faith" — a slight context-departure from the standard ความเคร่งในพระเจ้า lock but principled given the τὸ τῆς εὐσεβείας μυστήριον construction is functioning as a near-credal summary, not a virtue-naming.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/eusebeia_pastoral_piety_2026-05.md` **before 2 Tim 1 ships**. The doc should:
1. Lock εὐσέβεια → **ความเคร่งในพระเจ้า** (default Pastoral noun rendering)
2. Lock εὐσεβέω → **แสดงความเคร่งในพระเจ้า** (verbal; 5:4)
3. Lock θεοσέβεια (HAPAX, 2:10) → **ความเคารพยำเกรงพระเจ้า** (cognate distinguished)
4. Document the 3:16 εὐσεβείας μυστήριον → **ข้อล้ำลึกแห่งทางของพระเจ้า** principled-departure
5. Cite 1 Tim 2:2 as the locking precedent (first occurrence in the Pastorals)
6. Note the Synoptic-Acts precedent (Acts 3:12 only NT-non-Pastoral occurrence; same Thai rendering applies)

---

## 3. ὑγιαίνω + sound-doctrine metaphor cluster — **STABLE (undocumented; recommend new doc — high Pastoral-forward priority)**

The Pastoral-distinctive **medical metaphor** for orthodoxy. ὑγιαίνω + cognates occur **8× across the Pastorals** with **2× in 1 Tim** (1:10 ὑγιαίνουσα διδασκαλία; 6:3 ὑγιαίνοντες λόγοι):

| Verse | Greek | Thai | Construction |
|---|---|---|---|
| 1:10 | τῇ ὑγιαινούσῃ διδασκαλίᾳ | **คำสอนอันถูกต้อง** | "sound doctrine" — generic Pastoral standard |
| 6:3 | ὑγιαίνουσι λόγοις, τοῖς τοῦ κυρίου ἡμῶν | **ถ้อยคำอันถูกต้องของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** | "sound words" — Christ-tradition |

The 1:10 KD names the rendering:

> ὑγιαίνω → ถูกต้อง / ดีงาม (lit. be-healthy; Pauline-Pastoral-distinctive metaphor for sound-doctrine). διδασκαλία → คำสอน. Render 'คำสอนอันถูกต้อง' — preserves the doctrinal-soundness sense. Pastoral-recurring phrase (1Tim 6:3, 2Tim 1:13, 4:3, Tit 1:9, 1:13, 2:1, 2:2).

**Editorial assessment:** The literal Greek metaphor (medical "healthy / sound") is collapsed to **ถูกต้อง** ("correct, right") in Thai. This is a **principled metaphor-flattening** — Thai has no idiomatic equivalent of the body-health-as-doctrinal-correctness metaphor that the Pastoral-Greek deploys (the metaphor likely echoes Hellenistic-philosophical "healthy reason" tropes, esp. Stoic). The translator's rendering preserves the **functional force** (orthodoxy-as-correctness) while sacrificing the medical-imagery. An alternative **คำสอนที่ถูกหลัก** ("doctrine according to the standard") preserves a slightly-more-formal register; **คำสอนที่ถูกสุขภาพ** ("doctrine healthy-of-body") would preserve the literal metaphor at the cost of natural Thai readability.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/hygiaino_sound_doctrine_2026-05.md` before 2 Tim 1:13 + 4:3 + Tit 1:9, 1:13, 2:1, 2:2 (the densest cluster — Titus has 4 of the 8 corpus-occurrences). The doc should:
1. Lock ὑγιαίνω + διδασκαλία → **คำสอนอันถูกต้อง**
2. Lock ὑγιαίνω + λόγος → **ถ้อยคำอันถูกต้อง**
3. Document the metaphor-flattening rationale (Thai reader-cognition preserved; medical-Greek-imagery sacrificed)
4. Cite 1 Tim 1:10 as the locking precedent
5. Note the contrast-pair: ἑτεροδιδασκαλέω → **สอนผิดเพี้ยน** (1 Tim 1:3, 6:3) is the locked antonymic-rendering for the Pastoral false-teaching polemic

---

## 4. σωτήρ — Pastoral-distinctive God-as-Savior title — **STABLE (undocumented; recommend new doc — Pastoral-Christological cornerstone)**

The most-doctrinally-significant Pastoral-Christological-shift. The Pauline-corpus default applies σωτήρ predominantly to **Christ** (Eph 5:23; Phil 3:20; cf. Acts 13:23; Rom 11:26 implicit). The Pastorals invert this — **σωτήρ is applied 6× to God-the-Father and 4× to Christ** across 1-2 Tim + Tit. In **1 Timothy specifically, all 3 σωτήρ occurrences are God-the-Father, not Christ**:

| Verse | Greek | Thai | Subject |
|---|---|---|---|
| 1:1 | θεοῦ σωτῆρος ἡμῶν καὶ Χριστοῦ Ἰησοῦ τῆς ἐλπίδος ἡμῶν | **พระเจ้าพระผู้ช่วยให้รอดของเรา และของพระเยซูคริสต์ผู้ทรงเป็นความหวังของเรา** | God (Christ = "our hope," not Savior here) |
| 2:3 | ἐνώπιον τοῦ σωτῆρος ἡμῶν θεοῦ | **เฉพาะพระพักตร์ของพระเจ้าพระผู้ช่วยให้รอดของเรา** | God |
| 4:10 | ἠλπίκαμεν ἐπὶ θεῷ ζῶντι, ὅς ἐστιν σωτὴρ πάντων ἀνθρώπων | **วางใจในพระเจ้าผู้ทรงพระชนม์ ผู้ทรงเป็นพระผู้ช่วยให้รอดของทุกคน** | God |

The 1:1 KD names the principle:

> Distinctive Pastoral-title for God (NOT Christ): God-as-Savior. Recurs at 1Ti 2:3, 4:10, Tit 1:3, 2:10, 3:4. σωτήρ → พระผู้ช่วยให้รอด (corpus-locked, matches EPH 5:23 same lemma). The Pastoral-distinctive shifts the σωτήρ-attribution from Christ-only (typical Pauline) to Father-as-Savior in salvation-history's-broader-sense — fitting 1Tim's polemic-against-false-teachers.

**Editorial assessment:** **พระเจ้าพระผู้ช่วยให้รอดของเรา** is principled — uses the same Pauline-corpus-locked **พระผู้ช่วยให้รอด** rendering (matching Eph 5:23 of Christ) but applies it to God-the-Father in apposition (พระเจ้า + พระผู้ช่วยให้รอด). The royal-prefix construction is uniform across all three occurrences. This **preserves the Pastoral Christological-pattern** in Thai naturally without forcing a different lemma, and **leaves Christ-as-Savior available for occurrences in Titus** (Tit 1:4 χάρις καὶ εἰρήνη ἀπὸ θεοῦ πατρὸς καὶ Χριστοῦ Ἰησοῦ τοῦ σωτῆρος ἡμῶν "Christ Jesus our Savior" + Tit 2:13 + Tit 3:6) where Christ is named σωτήρ explicitly. The corpus needs to handle **Tit 2:13's** double-σωτήρ ambiguity (τοῦ μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ — Granville Sharp's Rule debate: "the great God and Savior" = Christ alone, or "the great God and-our-Savior Jesus Christ" = two persons) before Titus ships.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/soter_pastoral_god_christ_2026-05.md` **before 2 Tim 1:10 + Tit 1:3, 1:4, 2:10, 2:13, 3:4, 3:6 ship**. The doc should:
1. Lock σωτήρ-applied-to-God → **พระเจ้าพระผู้ช่วยให้รอด** (apposition)
2. Lock σωτήρ-applied-to-Christ → **พระผู้ช่วยให้รอด** (matches Eph 5:23 corpus-precedent)
3. Document the Pastoral Christological-distribution (6× God / 4× Christ across 1-2 Tim + Tit) as principled
4. **Pre-decide Tit 2:13 Granville-Sharp question** — recommend the unambiguous Trinitarian reading (Christ = "the great God and our Savior") since Greek grammar + Pauline-corpus-Christology favor it; render with a Thai construction that captures this without committing the verse to either reading definitively
5. Cite 1 Tim 1:1 as the locking precedent

---

## 5. ἐπίσκοπος / πρεσβύτερος / διάκονος — Pastoral church-office vocabulary — **STABLE (partly documented; recommend extending diakonos_pauline doc)**

The 1 Tim 3:1–13 + 5:17–22 office-qualification passages establish the Pastoral-corpus rendering pattern for church-leadership vocabulary:

| Lemma | 1 Tim verses | Thai | Sense |
|---|---|---|---|
| ἐπισκοπή | 3:1 | **ตำแหน่งผู้ปกครองดูแล** | the office (overseer-office) |
| ἐπίσκοπος | 3:2 | **ผู้ปกครองดูแล** | the person (overseer) |
| διάκονος | 3:8, 3:12 | **มัคนายก** | deacon (formal church-office) |
| διάκονος | 4:6 | **ผู้รับใช้** | servant (general — Timothy as Christ's servant) |
| διακονέω | 3:10, 3:13 | **รับใช้ในตำแหน่งมัคนายก / ปฏิบัติหน้าที่มัคนายก** | serve as deacon |
| πρεσβύτερος | 5:1 | **ผู้สูงอายุ** | older man (age-based) |
| πρεσβύτερος | 5:17, 5:19 | **ผู้ปกครองคริสตจักร** | elder (church-office) |
| πρεσβυτέριον | 4:14 | **คณะผู้ปกครอง** | the council-of-elders |
| πρεσβυτέρα | 5:2 | **หญิงสูงอายุ** | older woman (age-based) |

The diakonos_pauline_2026-05.md doc covers διάκονος / διακονέω. The **NEW Pastoral lemmas needing lock** are ἐπίσκοπος + πρεσβύτερος + the **same-lemma age-vs-office disambiguation** at 5:1 vs 5:17.

The 5:1 KD names the disambiguation principle:

> Per uW: πρεσβύτερος here = age-based 'older-man' (NOT church-office 'elder' as at v.17). Context (paired with πατήρ as analog) confirms age-meaning. Render 'ผู้สูงอายุ' — distinct from v.17's 'ผู้ปกครองคริสตจักร' (church-elder) lock. CRITICAL: same Greek word, two different Thai renderings depending on context-disambiguation.

**Editorial assessment:** The dual-rendering of πρεσβύτερος is **principled and contextually-decisive** — paired with πατήρ at 5:1, age-meaning is unambiguous; paired with προεστῶτες + κοπιῶντες ἐν λόγῳ καὶ διδασκαλίᾳ at 5:17, office-meaning is unambiguous. The corpus-precedent **ผู้ปกครองคริสตจักร** for the office-sense matches Acts 11:30, 14:23, etc.

The **ἐπίσκοπος → ผู้ปกครองดูแล** rendering is a deliberate pilot-decision per the 3:1 pilot KD: "ผู้ปกครองดูแล captures both governance and care — avoiding both bare transliteration (บิชอป) and reduction to mere 'pastor' (ศิษยาภิบาล, which is a different word)." This is **distinct from** the πρεσβύτερος-office rendering ผู้ปกครองคริสตจักร — the corpus principle is that ἐπίσκοπος + πρεσβύτερος, while functionally near-synonymous in the Pastorals, get **different Thai renderings** to preserve the Greek lexical distinction (a debate inside Christian-tradition: bishops + elders as one office or two — Ben's translation deliberately preserves both readings via the Thai lexical split).

**Recommend: STABLE; extend** `diakonos_pauline_2026-05.md` to a renamed/extended `pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md` (or write a parallel new doc), **before Tit 1:5–9 ships** (the densest qualification-cluster outside 1 Tim 3). The doc should:
1. Lock ἐπίσκοπος → **ผู้ปกครองดูแล** + ἐπισκοπή → **ตำแหน่งผู้ปกครองดูแล**
2. Lock πρεสβύτερος (office) → **ผู้ปกครองคริสตจักร** (already corpus-precedent from Acts)
3. Lock πρεสβύτερος (age) → **ผู้สูงอายุ** + πρεสβυτέρα → **หญิงสูงอายุ** + νεώτερος / νεωτέρα → **คนหนุ่ม / หญิงสาว**
4. Lock πρεสβυτέριον (collective elder-council) → **คณะผู้ปกครอง**
5. Document the **deliberate-lexical-split policy** — distinct Thai renderings for ἐπίσκοπος vs πρεσβύτερος-office to preserve the Greek lexical distinction without committing to a one-office or two-office ecclesiology
6. Cross-reference `diakonos_pauline_2026-05.md` for διάκονος / διακονέω
7. Cite 1 Tim 3:1–13 + 5:17–19 as the locking precedents

---

## 6. ἐπιφάνεια — Christ's appearing (Pastoral eschatological term) — **STABLE (undocumented; recommend brief new doc; intersects with parousia_christou)**

1 Tim 6:14 introduces the **Pastoral-distinctive eschatological lemma** ἐπιφάνεια ("appearing, manifestation"), which alongside the inherited παρουσία forms the Pastoral two-term-toolkit for Christ's-return language:

> 1 Tim 6:14 GK: μέχρι **τῆς ἐπιφανείας** τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ
> TH: จนกว่าจะถึง**การเสด็จมาปรากฏ**ของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา

The 6:14 KD names the rendering:

> ἐπιφάνεια → การเสด็จมาปรากฏ (appearing-manifestation — Pauline-eschatological-term, corpus-precedent at 2Th 2:8). Christ-return reference. Royal-prefix ทรงเสด็จ implied.

**Editorial assessment:** **การเสด็จมาปรากฏ** is principled — combines the royal-เสด็จ verb-stem (matching the locked παρουσία = **การเสด็จมา** from 1TH) with **ปรากฏ** ("manifest, appear") to capture ἐπιφάνεια's distinctive *visible-manifestation* force. The Thai compound **เสด็จมาปรากฏ** is heavier than the simple **การเสด็จมา** for παρουσία — the difference reflects the Greek lexical distinction (παρουσία = "presence, arrival"; ἐπιφάνεια = "manifestation, appearing"). This will recur 5× more in the Pastorals (2 Tim 1:10 — Christ's first ἐπιφάνεια, the incarnation; 2 Tim 4:1, 8 — the second ἐπιφάνεια; Tit 2:11 — first ἐπιφάνεια of grace; Tit 2:13 — second ἐπιφάνεια of glory).

**Recommend: STABLE; consider brief new doc** `docs/translator_decisions/epiphaneia_christou_2026-05.md` (or amend the still-to-be-written `parousia_christou_2026-04.md`), **before 2 Tim 1:10 ships**. The doc should:
1. Lock ἐπιφάνεια (Christ-eschatological subject) → **การเสด็จมาปรากฏ**
2. Note the **double application** in 2 Tim 1:10 + Tit 2:11 — ἐπιφάνεια referring to Christ's *first* coming (incarnation), not just the second; the Thai rendering should remain the same since both are royal-divine manifestations
3. Cross-reference with the παρουσία-doc-to-be-written (1TH precedent: παρουσία = **การเสด็จมา**)
4. Cite 1 Tim 6:14 as the first Pastoral-corpus occurrence + 2 Th 2:8 as the broader-Pauline precedent

---

## 7. δεσπότης vs κύριος — slave-master vocabulary — **STABLE (undocumented; consider doc later — recurs in 2 Tim 2:21, Tit 2:9, 1 Pet 2:18)**

1 Tim 6:1–2 establishes the Pauline-corpus disambiguation between δεσπότης (human master in slave-context) and κύριος (divine Lord):

> 1 Tim 6:1 GK: τοὺς ἰδίους **δεσπότας** πάσης τιμῆς ἀξίους
> TH: **นาย**ของตนสมควรได้รับเกียรติทุกประการ

| Lemma | 1 Tim verse | Thai | Sense |
|---|---|---|---|
| δεσπότης | 6:1, 6:2 | **นาย** | human master (no royal-prefix) |
| κύριος | 1:2, 1:12, 1:14, 6:3, 6:14, 6:15 | **องค์พระผู้เป็นเจ้า** | divine Lord (royal-prefix) |

The 6:1 KD names the disambiguation:

> δεσπότης → นาย (master — distinct from κύριος which Pauline-corpus reserves for divine-Lord). Pauline-pastoral-pragmatism: respect-as-witness, not endorsement-of-system.

**Editorial assessment:** The δεσπότης / κύριος split is **principled** — preserves the Pauline-corpus-locked κύριος → **องค์พระผู้เป็นเจ้า** for divine-Lord (per `kyrios_narrator_voice_luke_acts_2026-04.md`) while reserving plain **นาย** for the human-master category. The 6:1 thai_summary frames the historical-context carefully (Greco-Roman slavery as social-reality, not endorsement; cf. Gal 3:28; Phlm 1:16) — appropriate Pastoral-Pauline pastoral handling for a Thai reader who may not recognize 1st-century slavery's distinctive features.

**Recommend: STABLE; consider doc later** (after 2 Tim + Titus + 1 Peter ship — δεσπότης recurs in 2 Tim 2:21 of God; Tit 2:9 of human masters; 1 Pet 2:18 of human masters; 2 Pet 2:1 + Jude 4 of Christ; Acts 4:24 of God). The lemma's **inversion-pattern** (sometimes God/Christ, sometimes human masters) means the **Thai disambiguation has to be context-driven** — not a simple lemma-lock. For now, the verse-level rationale at 1 Tim 6:1 is comprehensive enough; revisit after the wider corpus is in.

---

## 8. ἀρσενοκοίτης rendering at 1 Tim 1:10 — **REVIEW (corpus-locked from 1Co 6:9; high doctrinal sensitivity)**

The Pauline-vice-list lemma ἀρσενοκοίτης occurs only **2× in the NT** — both Pauline (1 Cor 6:9; 1 Tim 1:10):

> 1 Tim 1:10 GK: πόρνοις, **ἀρσενοκοίταις**, ἀνδραποδισταῖς...
> TH: คนล่วงประเวณี **ผู้ชายที่ร่วมประเวณีกับผู้ชาย** คนค้าทาส...

The 1:10 KD names the corpus-precedent:

> ἀρσενοκοίτης → ผู้ชายที่ร่วมประเวณีกับผู้ชาย (corpus-precedent at 1Co 6:9 'ἀρσενοκοῖται'). Pauline-compound coined-from LXX Lev 18:22 + 20:13 (ἄρσην + κοιμάω). Render preserves the Levitical-derivation-and-clinical-description without modern-political-coloring.

**Editorial assessment:** The rendering **ผู้ชายที่ร่วมประเวณีกับผู้ชาย** ("a man who has sexual-relations with a man") is **principled and Levitically-derived** — Paul's compound is itself coined from LXX Lev 18:22 (ἄρσενος / ἄρσην + κοίτη) and Lev 20:13 (the same lexical-stem). The Thai rendering preserves both the **lexical compositionality** (ผู้ชาย "man" + ร่วมประเวณีกับผู้ชาย "has-sexual-relations-with-a-man") and the **clinical-descriptive register** (no modern-political-coloring; no transliteration of contemporary Thai LGBT terminology; no euphemism). This is **the most defensible scholarly choice** given the contested-modern-interpretive landscape (active-vs-passive-male-partner readings; pederasty-only vs all-male-male-relations readings; etc.) — the rendering does not commit to a narrower interpretive sub-question.

The **REVIEW flag** is not a request to change the rendering — it's a flag that **for a CC0 evangelical-Protestant Thai Bible deployed publicly via Eremos**, this is one of the rare verses where a public Thai Christian readership will scrutinize the lexical choice carefully. The current rendering is corpus-locked from 1 Cor 6:9 (already shipped) and matches the trajectory of mainstream English evangelical translations (BSB / NIV / ESV / CSB). Worth Ben's confirmation that the Thai rendering is the corpus-default before it is reused in 1 Cor 6:9 (pending re-translation if needed).

**Recommend: REVIEW** — confirm corpus-default with Ben. No new doc needed (the 1 Cor 6:9 audit, which is already shipped, should be the corpus-anchor — verify consistency).

---

## 9. μιᾶς γυναικὸς ἄνδρα / ἑνὸς ἀνδρὸς γυνή — Pastoral marital-faithfulness formula — **REVIEW (interpretive-ambiguity preserved literally)**

The famous Pastoral-crux occurs **3× in 1 Timothy** (3:2 overseer; 3:12 deacon; 5:9 enrolled-widow — feminine inversion) and recurs at Tit 1:6 (elder). All three 1 Tim occurrences render literally:

| Verse | Greek | Thai |
|---|---|---|
| 3:2 | μιᾶς γυναικὸς ἄνδρα | **เป็นสามีของภรรยาเพียงคนเดียว** |
| 3:12 | μιᾶς γυναικὸς ἄνδρες | **เป็นสามีของภรรยาเพียงคนเดียว** |
| 5:9 | ἑνὸς ἀνδρὸς γυνή | **เป็นภรรยาของสามีเพียงคนเดียว** |

The 3:2 KD names the four-way interpretive-ambiguity:

> FAMOUS CRUX. Literal: 'of one wife a husband.' Four main interpretations: (1) monogamous (not polygamous), (2) not divorced and remarried, (3) married only once (even after widowhood), (4) marital fidelity. Modern majority: (4) faithfulness to one's wife — but the literal Thai 'สามีของภรรยาเพียงคนเดียว' preserves the genuine ambiguity rather than committing to one reading.

**Editorial assessment:** The literal-rendering **สามีของภรรยาเพียงคนเดียว** is **principled per uW + RULES §1 (accuracy-with-ambiguity-preserved)**. It refuses to commit the verse to any of the four major interpretations — preserving the Greek ambiguity in Thai naturally. The 5:9 feminine inversion **ภรรยาของสามีเพียงคนเดียว** maintains structural-parallelism, which is editorially correct since the Greek 5:9 formula is the **deliberate feminine mirror-image** of 3:2 — Paul is aware of the cross-gender symmetry.

**Recommend: REVIEW** — confirm the literal-ambiguity-preservation strategy is the corpus-default before Tit 1:6 ships. The thai_summary at 3:2 already lists the four interpretations; this is comprehensive editorial handling. No corpus doc strictly needed if Ben confirms the strategy; but **a brief one-line cross-reference in `pastoral_offices_*` doc** noting the formula recurs 4× across the Pastorals and is uniformly rendered literally would aid forward-Pauline-corpus consistency.

---

## 10. 1 Tim 2:11–12 + 2:15 — women in worship + αὐθεντέω + σωθήσεται διὰ τῆς τεκνογονίας — **DECIDE (interpretive-ambiguity-preservation strategy under scrutiny)**

The most-contested cluster in 1 Timothy. The translation deploys an aggressive **interpretive-ambiguity-preservation strategy** — refusing to commit any of the three contested verses (2:11, 2:12, 2:15) to a single interpretation.

**1 Tim 2:11–12** — three preservation-points (per the 2:11 + 2:12 KDs):
1. **γυνή** — generic-women OR specifically-wives → rendered **หญิง** (ambiguous)
2. **ἡσυχία** — peaceful-disposition OR silence → rendered **ความสงบเงียบ** (compound preserves both: สงบ "calm" + เงียบ "silent")
3. **αὐθεντέω** (HAPAX, only here in NT) — neutral-authority OR domineering-authority → rendered **ใช้อำนาจเหนือ** (ambiguous in Thai)
4. **διδάσκειν** — teach-anyone OR teach-men-specifically → rendered literal **สอน** (ambiguous)

**1 Tim 2:15** — singular-to-plural pronoun shift preserved:
- σωθήσεται (sing.) → **นาง** ("she")
- μείνωσιν (pl.) → **พวกเขา** ("they")
- The **τεκνογονία** (HAPAX) is rendered **การคลอดบุตร** with διά rendered **ผ่าน** ("through") — preserving Mary-as-Messiah-bearer / women-saved-as-mothers / protected-during-childbirth / Eve-saved-by-Mary readings

The thai_summary unpacks the major-interpretations carefully without committing.

**Editorial assessment:** The strategy is **per uW + RULES §1** principled — uW explicitly recommends ambiguity-preservation at all four points, and the translator follows. **However**, this is the **single most-watched passage in the Pastoral letters for evangelical-Protestant Thai readers**, and the Eremos translation will be scrutinized closely on whether the Thai renderings genuinely preserve the ambiguity OR slip into a complementarian / egalitarian default. The ambiguity-preservation is **principled but high-stakes**.

**The DECIDE question:** Is the literal-ambiguity-preservation the right corpus-default for this passage, or should the translator commit to one interpretation (with thai_summary acknowledging the alternative)? The current strategy is more conservative than mainstream English Bibles — NIV / ESV / CSB / NLT all commit to **silence + authority** for ἡσυχία + αὐθεντέω (complementarian-leaning); only the NRSV / NRSVue lean closer to the Eremos-style ambiguity preservation. Worth Ben's confirmation, especially given the **Tit 2:3–5** + **2 Tim 3:6–7** female-focused passages will compound the editorial-decision-weight.

**Recommend: DECIDE** — Ben's confirmation needed before tagging `book-1timothy-v1`. If the literal-ambiguity-preservation is confirmed, write `docs/translator_decisions/women_in_worship_1tim_2_2026-05.md` to lock the strategy + flag forward-compounding cases (2 Tim 3:6–7; Tit 2:3–5).

---

## 11. 1 Tim 3:11 γυναῖκας — wives-of-deacons vs women-deacons — **DECIDE (interpretive crux)**

The verse **γυναῖκας ὡσαύτως σεμνάς** ("women / wives likewise [must be] dignified") is sandwiched between male-deacon qualifications (3:8–10) and male-deacon marital-status (3:12). The Greek lacks the possessive **αὐτῶν** ("their") that would unambiguously signal "wives."

> 1 Tim 3:11 GK: γυναῖκας ὡσαύτως σεμνάς, μὴ διαβόλους, νηφαλίους, πιστὰς ἐν πᾶσιν.
> TH: หญิงก็เช่นเดียวกัน ต้องเป็นผู้น่าเคารพ ไม่เป็นคนชอบใส่ร้าย รู้จักประมาณตน และซื่อสัตย์ในทุกเรื่อง

The 3:11 KD names the three-way crux:

> MAJOR INTERPRETIVE CRUX. γυνή can mean either (a) women, (b) wives. Three main views: (1) wives of deacons, (2) women deacons/deaconesses (parallel ὡσαύτως with v.8 suggests new category; Phoebe is διάκονος in Rom 16:1), (3) women in general in the congregation. The Greek lacks any possessive pronoun (αὐτῶν 'their') that would signal 'wives.'

**Editorial assessment:** The literal-rendering **หญิง** (no possessive) is **principled-ambiguity-preservation**. It refuses to commit to any of the three readings — matching SBLGNT's grammatical neutrality. The thai_summary at 3:11 frames the modern-scholarship-preference (women deacons, given (a) no αὐτῶν, (b) parallel ὡσαύτως pattern, (c) Rom 16:1 Phoebe-as-διάκονος) without committing.

**The DECIDE question:** Is the ambiguity-preservation correct for the corpus-default, OR should the verse explicitly commit to "women deacons" (modern-scholarly-majority + Rom 16:1 Phoebe-precedent) OR "wives [of deacons]" (older traditional-reading + sandwich-context favorable)? Mainstream English splits — BSB / NIV "the women" (ambiguous); ESV "their wives" (committed-to-1); NLT "the wives of deacons" (committed-to-1); CSB "the women" (ambiguous, with footnote noting deaconess interpretation). The Eremos-rendering aligns with BSB / NIV / CSB; the question is whether Ben prefers an **explicit Pauline-pastoral commitment to one reading** for a CC0 Thai Bible serving a missions-oriented audience.

**Recommend: DECIDE** — Ben's confirmation needed. If ambiguity-preservation is confirmed, fold into the proposed `women_in_worship_1tim_2_2026-05.md` doc as a separate sub-section. If a commitment to "women deacons" is preferred, the corpus also needs to handle Rom 16:1 (διάκονον τῆς ἐκκλησίας τῆς ἐν Κεγχρεαῖς) consistently before Romans ships.

---

## 12. 1 Tim 3:16 Ὃς vs Θεός — Christ-hymn textual variant + the hymn rendering — **REVIEW (SBLGNT-compliant; rendering principled)**

The famous Pastoral-Christological-hymn (3:16) opens with the contested relative pronoun:

> 1 Tim 3:16 GK (SBLGNT): καὶ ὁμολογουμένως μέγα ἐστὶν τὸ τῆς εὐσεβείας μυστήριον· **Ὃς** ἐφανερώθη ἐν σαρκί, ἐδικαιώθη ἐν πνεύματι, ὤφθη ἀγγέλοις, ἐκηρύχθη ἐν ἔθνεσιν, ἐπιστεύθη ἐν κόσμῳ, ἀνελήμφθη ἐν δόξῃ.

> TH: และตามที่ยอมรับร่วมกัน ข้อล้ำลึกแห่งทางของพระเจ้านั้นยิ่งใหญ่นัก คือ **พระองค์ทรงปรากฏในเนื้อหนัง** ทรงได้รับการพิสูจน์โดยพระวิญญาณ ทรงปรากฏแก่เหล่าทูตสวรรค์ ทรงได้รับการประกาศในหมู่ประชาชาติ ทรงเป็นที่เชื่อในโลก ทรงถูกรับขึ้นสู่พระสิริ

The 3:16 KD comprehensively names the SBLGNT-compliance + paleographic-rationale + theological-implication of the variant:

> External evidence strongly favors Ὃς (earliest and best mss). Paleographic explanation: ΟC (relative pronoun) → ΘC̄ (nomen sacrum abbreviation for θεός) is a plausible scribal addition of a horizontal bar; the reverse change is harder to motivate. Theologically: the Byzantine reading ('God was manifested in the flesh') makes an explicit high-Christology statement; the critical reading ('He who was manifested in the flesh') leaves the subject a relative pronoun that grammatically has no antecedent — best explained as the opening of a quoted hymn fragment about Christ. Following SBLGNT: Ὃς.

**Editorial assessment:** The Thai **พระองค์ทรง...** ("He / The-One-who...") is principled — preserves the Ὃς-relative-pronoun structure without committing to a Θεός high-Christological-anchor that would force **พระเจ้าทรง...** ("God..."). The royal-prefix ทรง is uniformly applied to all six aorist-passive verbs (the hymn's distinctive form), preserving the divine-passive structure. The hymn-fragment-recognition (per the ὁμολογουμένως HAPAX introduction) is acknowledged in the notes.

The **REVIEW flag** is not a request to change the rendering — it's a flag that this is **the most-watched textual-variant in 1 Timothy** for evangelical-Protestant readers, and the SBLGNT-compliance + literal preservation of the Ὃς-relative-pronoun structure is the modern-scholarly-consensus default. Worth Ben's confirmation that no footnote is needed (RULES §0 SBLGNT-strictness + RULES §5 silent-omission of the Byzantine Θεός variant).

**Recommend: REVIEW** — confirm with Ben. The current rendering is principled per RULES §0 + §5 + uW recommendation; the question is whether a footer-note (similar to JHN 1:18 μονογενὴς θεός handling, if any was applied) is warranted given the verse's prominence in confessional-Christian-tradition. Most likely **no footer-note** (per RULES §5 + the existing 7 `_resolved/` docs precedent: silent-omission unless surprise to mainstream readers) — but worth explicit confirmation.

---

## 13. πρεσβύτερος dual-meaning at 5:1 vs 5:17 — **STABLE (principled disambiguation; covered in §5)**

See §5. The same-lemma age-vs-office split is **fully principled and explicitly cross-referenced in the verse-level KD** at 5:1 and 5:17. The thai_summary at 5:17 explicitly addresses both this split AND the broader elder/overseer-debate (whether πρεσβύτερος-office and ἐπίσκοπος refer to the same office or two distinct ones — Eremos preserves both readings via the lexical-split). **STABLE — no further action needed beyond the §5 doc-extension recommendation.**

---

## 14. φιλαργυρία + greed/wealth instruction (6:6–10, 17–19) — **STABLE (verse-level rationale comprehensive; consider doc later)**

The Pastoral wealth-ethics-cluster — εὐσέβεια μετὰ αὐταρκείας (6:6) → ῥίζα πάντων τῶν κακῶν ἡ φιλαργυρία (6:10) → instruction to-the-rich (6:17–19). Key renderings:

| Greek | Thai |
|---|---|
| αὐτάρκεια | **ความพอใจในสิ่งที่มีอยู่** (corpus-locked from PHP 4:11 αὐτάρκης) |
| φιλαργυρία (HAPAX) | **การรักเงิน** |
| πορισμός | **เครื่องมือหากิน** (false-religion); **กำไรอันใหญ่หลวง** (true-godliness) |
| ὑψηλοφρονέω (HAPAX) | **หยิ่ง** |
| ἀπόλαυσις | **ใช้สอย** (enjoyment, neutral) |
| ἀποθησαυρίζω (HAPAX) | **สะสม** (echoes Matt 6:19–20 treasures-in-heaven) |

The thai_summary at 6:10 corrects the common-misquotation ("money is the root of all evil") and explicitly handles the πάντων τῶν κακῶν "all evils vs all kinds of evil" interpretive-question.

**Editorial assessment:** The cluster is **uniformly rendered with comprehensive verse-level rationale**. The αὐτάρκεια → **ความพอใจในสิ่งที่มีอยู่** rendering is corpus-locked from PHP 4:11. The vivid Pauline-imagery (drowning at 6:9 βυθίζω; self-impalement at 6:10 περιπείρω; storing-up-foundation-for-the-future at 6:19 ἀποθησαυρίζω) is preserved literally.

**Recommend: STABLE — no new doc needed.** Verse-level rationale is comprehensive. Worth a one-line cross-reference in any future Pastoral-ethics-doc.

---

## 15. πιστὸς + λόγος Christ-tradition citation at 5:18 — **STABLE (significant for canon-formation scholarship)**

1 Tim 5:18 cites *two* sources as **ἡ γραφή** ("Scripture"): Deut 25:4 (ox-treading) + Luke 10:7 (worker-worthy-of-wages). The 5:18 KD + thai_summary handle this carefully:

> Pauline cites Deuteronomy 25:4 LXX + Luke 10:7 (Jesus' own words) — the earliest-explicit-NT-citation-as-Scripture in NT itself. Significant for early-NT-canon-formation scholarship.

The Thai renders both quotations with **พระคัมภีร์กล่าวว่า** ("Scripture says") prefacing the dual quotation — preserving Paul's principled equation of Jesus-tradition with OT-Scripture.

**Editorial assessment:** The rendering is **principled and handles a nontrivial scholarly-question** (Pauline-equation-of-Christ-tradition-with-OT-Scripture; foundational for NT-canon-formation studies). The thai_summary unpacks this for Thai readers without anachronism.

**STABLE — no new doc needed.** Verse-level handling is comprehensive. Already in OT citations DB.

---

## 16. Inherited locks — **all compliant**

| Doc | 1 Tim evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 3:5 (ἐκκλησίας θεοῦ → **คริสตจักรของพระเจ้า**); 3:15 (ἐκκλησία θεοῦ ζῶντος → **คริสตจักรของพระเจ้าผู้ทรงพระชนม์**); 5:16 (μὴ βαρείσθω ἡ ἐκκλησία → **อย่าให้คริสตจักรต้องรับภาระ**). Three-occurrence uniform Pastoral-corpus compliance. | **LOCKED** |
| `diakonos_pauline_2026-05.md` | 3:8, 3:12 διάκονος (formal office) → **มัคนายก**; 4:6 διάκονος (general servant) → **ผู้รับใช้**; 3:10, 3:13 διακονέω → **รับใช้ในตำแหน่งมัคนายก / ปฏิบัติหน้าที่มัคนายก**; 1:12 διακονία → **งานรับใช้** (Pauline self-as-servant). Sense-disambiguation principled; recommend extension to `pastoral_offices_*` doc per §5. | **LOCKED-with-amendment-needed** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 1 Tim has **9+ narrator-κύριος references** (1:2, 1:12, 1:14, 5:21, 6:3, 6:14, 6:15, plus 6:1 δεσπότης-explicit-disambiguation showing the corpus rule is operating). All → **องค์พระผู้เป็นเจ้า** uniform. The Lukan-Acts-Johannine-Pauline-and-now-Pastoral signature is now confirmed across **5 corpus-streams** (LUK / ACT / JHN / GAL / 1TH / 1CO / 2CO / now 1TI). | **LOCKED-with-amendment-needed** (already noted across multiple prior audits) |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in 1TI — no vocative κύριε in this letter (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | N/A in 1TI — no doxological praise-verb-with-God-object constructions in narrative-form (the doxologies at 1:17 + 6:15–16 use formulaic-noun-phrase constructions, not praise-verbs-with-object). | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | 2:2 βασιλέων + ὑπεροχῇ → **กษัตริย์ + ตำแหน่งมีอำนาจ** (plain register, no royal-prefix; correct since civil-rulers-not-divine). 6:13 Ποντίος Πιλᾶτος → **ปอนทิอัสปีลาต** (transliteration, no royal-prefix). 1:20 Σατανᾶς + 5:15 Σατανᾶ → **ซาตาน** (plain — adversary not honored). Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register (ทรง / royal-vocabulary) on God + Christ throughout; plain register for Paul-as-author (1pl / 1sg ข้าพเจ้า), Timothy-as-recipient (ท่าน), human-authorities (กษัตริย์), human-paternal-and-maternal analogies (5:1 ὡς πατέρα → **ดุจบิดา** plain; 5:2 ὡς μητέρας → **เสมือนเป็นมารดา** plain). Pastoral-corpus extends the GAL + 1TH + 1CO + 2CO pattern. Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A in 1TI** — no Aramaic embeds in this letter (no Αββα, no Μαραναθα). | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | Audit script PASSES strict mode. 4 candidates dispositioned (2 silent-§5; 2 resolved-docs at 4:12 + 6:21). 3 additional textual-variants (4:10 ἀγωνιζόμεθα/ὀνειδιζόμεθα; 5:16 πιστὴ vs πιστὸς ἢ πιστή; 6:19 ὄντως vs αἰώνιος ζωή) carry `_resolved/` docs but do not match the inclusion-variant signal patterns. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — 1 Tim is a doctrinal-pastoral letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 1TI. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from 1TI. | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | **N/A** — ἄφεσις absent from 1TI (the Pastoral-letters use ἔλεος "mercy" + ἁμαρτωλούς σῶσαι "save sinners" formulae, not ἄφεσις). | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | N/A in 1TI — no pagan-idol references (closest is 4:1 πνεύμασι πλάνοις καὶ διδασκαλίαις δαιμονίων → **วิญญาณที่หลอกลวงและคำสอนของพวกผีปีศาจ** — demonic-doctrines, not pagan-deities-named). | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | 6:13 Ποντίος Πιλᾶτος → **ปอนทิอัสปีลาต** (corpus-locked transliteration). The reference is historical-anchor-for-Christ's-trial, not active Roman-administrator-title in narrative. Compliant. | **LOCKED** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 1 Tim. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (implied-divine — 4:1 τὸ πνεῦμα expressly-says: ambiguous between Holy-Spirit-OR-prophetic-Spirit; rendered **พระวิญญาณ** royal-prefix). No anthropological πνεῦμα + ψυχή pairings in 1 Tim (the 5:23 1TH-style tripartite is Pauline-corpus-unique). | **LOCKED (N/A on anthropology)** |
| `johannine_doubled_amen_2026-04.md` | N/A — Pastoral, not Johannine. ἀμήν at 1:17 + 6:16 (single doxology-amen) → **อาเมน** (corpus-locked transliteration). | **LOCKED (N/A on doubled)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in 1 Tim). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in 1 Tim. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A in 1 Tim — no βασιλεία references in this letter (the 6:15 βασιλεὺς τῶν βασιλευόντων is the divine-King-of-kings doxology, not βασιλεία-noun). | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | N/A in 1 Tim — no οὐρανός references (the 1Tim 6:14 ἐπιφάνεια covers Christ-return without οὐρανός; the 1:11 + 6:16 doxologies don't reference heaven specifically). | **LOCKED (N/A)** |
| Pauline locks confirmed in 1TI from prior books | παρουσία-style language is absent from 1 Tim (handled by ἐπιφάνεια instead per §6); ἁγιασμός absent; ἁρπάζω absent; ἡμέρα κυρίου absent (the 6:14 μέχρι τῆς ἐπιφανείας construction substitutes); ψυχή / πνεῦμα tripartite absent; πορνεία absent (1:10 πόρνοι is the noun-form of the lemma, rendered **คนล่วงประเวณี** per the corpus-locked porneia rendering); δικαιοσύνη at 6:11 → **ความชอบธรรม** (locked from `dikaioo_dikaiosyne_family_2026-05.md`); υἱοθεσία absent; νόμος at 1:8–9 → **ธรรมบัญญัติ** (locked from `nomos_pauline_2026-05.md`); σάρξ at 3:16 (ἐν σαρκί incarnation) → **เนื้อหนัง** (locked from `sarx_pauline_2026-05.md`); στοιχεῖα absent. | **LOCKED** ✓ |

---

## Mechanical (§1) — **all green**

- 6/6 chapters: `output/check_reports/1timothy_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 6/6 chapters: `output/back_translations/1timothy_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-125-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --book 1timothy --strict`: **PASS** (4 candidates: 2 silent + 2 resolved); 3 additional textual-variants resolved-doc-covered
- `git status output/`: pre-existing 1TI-3-pilot-assessment artifacts (`docs/1tim_03_pilot_assessment_2026-05-02.md`; modifications to `output/check_reports/1timothy_03_review.md` + `_summary.json`; `greek_field_integrity_1timothy_03.md`) + unrelated Eph/Col paratext stragglers + 7 untracked `output/textual_variants/_resolved/1timothy_*.md` files (created during chapter ships, all referenced from verse-level KDs). None affects translation content or audit conclusions.
- `python3 scripts/export_to_usfm.py --book 1TI`: not yet run as part of this audit (per §1 checklist; defer to ship-script gating).

---

## Pre-existing docs affirmed / unchanged

All 39 docs in `docs/translator_decisions/` reviewed. Compliance summary in §16 above.

**Two docs flagged for amendment** (already noted in JHN + GAL + 1TH + 1CO + 2CO audits):
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to acknowledge corpus-wide narrator-κύριος now confirmed across **8 corpus-streams** (LUK / ACT / JHN / GAL / 1TH / 1CO / 2CO / 1TI). The doc's "Lukan-Acts signature" framing should be renamed/extended to "Lukan-Acts + Johannine + Pauline + Pastoral" — no rendering change, only doc-text update.
- **`diakonos_pauline_2026-05.md`** — extend to cover the broader Pastoral-offices vocabulary cluster (ἐπίσκοπος + πρεσβύτερος + πρεσβυτέριον) per §5.

---

## Flagged for Ben's attention

### A. πιστὸς ὁ λόγος "trustworthy saying" Pastoral formula — **STABLE, lift to corpus doc** (§1)
3-occurrence-1TI + 5-occurrence-Pastoral-corpus density makes 1 Timothy the locking-precedent. Lift to corpus doc `pistos_ho_logos_pastoral_formula_2026-05.md` before 2 Tim 2:11 + Tit 3:8.

### B. εὐσέβεια Pastoral-piety vocabulary — **STABLE, lift to corpus doc** (§2)
Pastoral-distinctive virtue-cluster (10× across 1-2 Tim + Tit; 4× in 1 Tim alone). Lift to corpus doc `eusebeia_pastoral_piety_2026-05.md` **before 2 Tim 1 ships** (forward-compounding density).

### C. ὑγιαίνω sound-doctrine metaphor — **STABLE, lift to corpus doc** (§3)
Pastoral-distinctive medical-metaphor flattened to **ถูกต้อง**. Lift to corpus doc `hygiaino_sound_doctrine_2026-05.md` before 2 Tim 1:13 + 4:3 + Tit 1:9, 1:13, 2:1, 2:2 ship.

### D. σωτήρ-applied-to-God Pastoral-Christological-shift — **STABLE, lift to corpus doc** (§4)
The Pastoral-distinctive sub-corpus pattern (6× God / 4× Christ across 1-2 Tim + Tit). Lift to corpus doc `soter_pastoral_god_christ_2026-05.md` **before 2 Tim 1:10 + Tit ship** — and pre-decide Tit 2:13 Granville-Sharp question.

### E. ἐπίσκοπος / πρεσβύτερος / διάκονος / πρεσβυτέριον — **STABLE, extend `diakonos_pauline_2026-05.md`** (§5)
Pastoral-offices vocabulary cluster — including the same-lemma πρεσβύτερος age-vs-office disambiguation. Extend the existing doc into `pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md` before Tit 1:5–9 ships.

### F. ἐπιφάνεια Pastoral-eschatological-term — **STABLE, brief new doc** (§6)
1 Tim 6:14 establishes the rendering **การเสด็จมาปรากฏ**. Brief doc before 2 Tim 1:10 + 4:1, 8 + Tit 2:11, 2:13.

### G. ἀρσενοκοίτης rendering at 1:10 — **REVIEW** (§8)
Corpus-locked from 1 Cor 6:9 (already shipped). Worth Ben's confirmation that the Levitically-derived clinical-descriptive Thai rendering is the corpus-default for a CC0 evangelical-Protestant Thai Bible.

### H. μιᾶς γυναικὸς ἄνδρα formula at 3:2 / 3:12 / 5:9 — **REVIEW** (§9)
Literal-ambiguity-preservation strategy preserves all four Pauline-tradition interpretations. Worth Ben's confirmation before Tit 1:6.

### I. 2:11–12 + 2:15 women-in-worship cluster — **DECIDE** (§10)
Most-contested cluster in 1 Timothy. Aggressive ambiguity-preservation strategy at 4 points (γυνή / ἡσυχία / αὐθεντέω / διδάσκειν) plus singular-to-plural pronoun shift at 2:15. Worth Ben's confirmation **before tagging `book-1timothy-v1`** and before 2 Tim 3:6–7 + Tit 2:3–5 ship.

### J. 3:11 γυναῖκας (wives-of-deacons vs women-deacons) — **DECIDE** (§11)
Three-way crux — literal-ambiguity-preservation matches BSB / NIV / CSB but commits less than ESV / NLT. Worth Ben's confirmation that ambiguity-preservation is the corpus-default.

### K. 3:16 Christ-hymn + Ὃς vs Θεός variant — **REVIEW** (§12)
SBLGNT-compliant rendering (Ὃς-relative-pronoun preserved as **พระองค์ทรง**); no footer-note currently. Worth Ben's confirmation that no footer-note is needed (per RULES §0 + §5).

### L. New corpus docs to write (priority-ordered for forward-Pastoral-corpus compounding)

**Highest priority — write before 2 Tim 1 ships:**
1. **`docs/translator_decisions/eusebeia_pastoral_piety_2026-05.md`** (§B) — locks the Pastoral piety-virtue vocabulary
2. **`docs/translator_decisions/soter_pastoral_god_christ_2026-05.md`** (§D) — locks the Pastoral Christological-shift + pre-decides Tit 2:13 Granville-Sharp
3. **`docs/translator_decisions/hygiaino_sound_doctrine_2026-05.md`** (§C) — locks the sound-doctrine metaphor

**Medium priority — write before 2 Tim 1:10 / Tit 1:5–9 ships:**
4. **`docs/translator_decisions/pistos_ho_logos_pastoral_formula_2026-05.md`** (§A) — locks the trustworthy-saying formula
5. **`docs/translator_decisions/pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md`** (§E) — extends `diakonos_pauline_2026-05.md` to the full Pastoral-offices set
6. **`docs/translator_decisions/epiphaneia_christou_2026-05.md`** (§F) — locks ἐπιφάνεια Pastoral-eschatological-term

**Lower priority — write only after Ben's DECIDE confirmations:**
7. **(Conditional)** `docs/translator_decisions/women_in_worship_1tim_2_2026-05.md` (§I + §J) — only if ambiguity-preservation is confirmed for 2:11–15 + 3:11

### M. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend framing to "Lukan-Acts + Johannine + Pauline + Pastoral" (8-corpus-stream confirmation; already flagged across prior audits)
- **`diakonos_pauline_2026-05.md`** — extend or replace with `pastoral_offices_*` doc per §E

### N. External AI review (§3 of checklist) — **pending**
Recommended before `book-1timothy-v1` tag. Suggested 4-cluster external AI packet:
1. **1 Tim 1:10 + 1:15–17** — vice-list + ἀρσενοκοίτης + πιστὸς ὁ λόγος + Ὃς-style doxology
2. **1 Tim 2:1–15** — public-worship cluster (universal-prayer + male-prayer-posture + female-instruction + 2:11–15 women-in-worship + 2:15 σωθήσεται διὰ τῆς τεκνογονίας)
3. **1 Tim 3:1–16** — overseer-deacon qualifications + 3:11 γυναῖκας crux + μιᾶς γυναικός formula + 3:16 Christ-hymn (Ὃς-vs-Θεός)
4. **1 Tim 6:3–19 + 6:20–21** — wealth-ethics cluster + paradoxical πορισμός + Pastoral-offices + ψευδώνυμος-γνῶσις closing

Use Grok + ChatGPT (free-tier) per the JHN / GAL / 1TH / 1CO / 2CO pattern.

---

## Recommendation

**1 Timothy ships in strong corpus-hygiene shape — and provides the Pastoral-corpus entry-point for the Eremos translation.** The translator made consistent, principled choices on the **five most-significant Pastoral-introduced lemma-clusters** (πιστὸς ὁ λόγος; εὐσέβεια; ὑγιαίνω; σωτήρ-Pastoral-shift; ἐπιφάνεια) — and **none of these five has a corpus-level doc** yet. This is the moment to lock them in before 2 Tim compounds the editorial weight (esp. 2 Tim 1:1 σωτὴρ θεός; 2 Tim 1:10 ἐπιφάνεια incarnation; 2 Tim 1:13 ὑγιαίνοντες λόγοι; 2 Tim 2:11 πιστὸς ὁ λόγος; 2 Tim 3:5 εὐσέβεια). Titus then triples the editorial weight again (Tit 1:1 ἐπίγνωσιν ἀληθείας τῆς κατ' εὐσέβειαν; Tit 1:3 σωτὴρ θεός; Tit 2:13 the Granville-Sharp σωτήρ crux; Tit 1:9 + 2:1 ὑγιαίνουσα διδασκαλία densest; etc.).

The **6 contested verses** (2:11–15 + 3:11 + 3:16 + 1:10 + 3:2/5:9) all use **literal-ambiguity-preservation** strategies that match SBLGNT / uW / RULES §1 — but the strategy itself, as a corpus-default, deserves Ben's explicit confirmation before tagging `book-1timothy-v1`. The DECIDE items (§I + §J) compound forward into 2 Tim 3:6–7 + Tit 2:3–5; the §I confirmation, in particular, is **the single highest-value editorial-decision before the Pastoral sub-corpus is locked**.

Tag `book-1timothy-v1` after:
1. Ben's decisions on **§I + §J** (DECIDE items: 2:11–15 women-in-worship cluster; 3:11 γυναῖκας wives-vs-deacons)
2. Ben's confirmation on **§G + §H + §K** (REVIEW items: 1:10 ἀρσενοκοίτης; 3:2/5:9 μιᾶς γυναικός formula; 3:16 Ὃς-vs-Θεός variant + footer-note question)
3. Three-to-six new translator_decisions docs written (§L items 1–3 minimum before 2 Tim 1; ideally items 1–6 before 2 Tim 1:10 / Tit 1:5–9; conditional item 7 only if ambiguity-preservation is confirmed)
4. Two existing docs amended (`kyrios_narrator_voice_luke_acts_2026-04.md`; `diakonos_pauline_2026-05.md`)
5. External AI sanity-check (§N)

The next Pastoral letters (2 Tim, then Tit) should not ship until the Pastoral-corpus-locks listed above are written. The five Pastoral-distinctive clusters (πιστὸς ὁ λόγος / εὐσέβεια / ὑγιαίνω / σωτήρ-shift / ἐπιφάνεια) are the most-forward-compounding editorial-stakes the project has faced since the GAL + 1TH locks — and they are all **first-densely-occurring here**.
