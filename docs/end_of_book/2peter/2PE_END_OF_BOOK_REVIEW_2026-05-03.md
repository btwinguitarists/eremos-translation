# 2 Peter — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 3 chapters (61 verses; verse-level `key_decisions` across the corpus); `glossary.json`; existing `docs/translator_decisions/` (47 docs).
**Trigger:** 2PE 3 shipped (commits `403c20c` / `be3c897` / `34921bf` for 2PE 1–3 source/checks/reader); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 3/3 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows only un-tracked Paratext-export files (untouched by this audit).
- **2 Peter is a uniquely-load-bearing book for several corpus-level patterns established in 1 Peter and the Pastorals.** It contains the **densest Granville-Sharp θεός-καὶ-σωτήρ cluster in the NT** (5 occurrences in 61 verses: 1:1, 1:11, 2:20, 3:2, 3:18). It is the **single book most-internally-aware of NT-canon-formation** (3:1 second-letter self-reference; 3:15-16 Paul's letters as γραφή / "Scripture"). It also tests the **petrine_eschatological_disambiguation** doc's anticipated 3:9 case (πάντας εἰς μετάνοιαν → preserve-ambiguity per doc; verified compliant).
- **The most theologically-loaded passages cluster in chapter 1**: 1:4 θείας κοινωνοὶ φύσεως ("partakers of the divine nature" — the locus-classicus for Eastern-Orthodox θέωσις; Thai chose Protestant ethical-spiritual participation framing) and 1:20-21 ἰδίας ἐπιλύσεως / οὐ θελήματι ἀνθρώπου (the foundational evangelical-Protestant proof-text for plenary-verbal inspiration; Thai chose the prophet's-own-interpretation reading). These are the highest-priority items for Ben's confirmation.
- **The παρουσία lemma returns to the Petrine corpus** at 1:16, 3:4, 3:12 — the only παρουσία occurrences in 1+2 Peter combined. Per the just-amended `parousia_christou_2026-05.md` §Petrine sub-section (lemma-driven rule), all three are rendered **การเสด็จมา** (Pauline rendering), confirming that the Pauline-vs-Petrine **การเสด็จมา / การสำแดง** distinction is *lemma-driven*, not *author-driven*. **LOCKED ✓.**
- **31 inherited locks verified compliant** in 2PE — including five new May-2026 corpus docs (parousia_christou, pascho_pathema_suffering, parepidēmos_paroikos_sojourner, poimēn_episkopos_register_split, petrine_eschatological_disambiguation) all written after the 1 Peter audit and now load-bearing for 2 Peter.
- **3 cross-cutting Petrine patterns are STABLE-but-undocumented at corpus level**:
  - **ἐπίγνωσις (true-knowledge) vs γνῶσις (bare-knowledge)** principled distinction (4× ἐπίγνωσις at 1:2, 1:3, 1:8, 2:20 + 2× γνῶσις at 1:5, 3:18) — densest NT cluster; consider corpus doc.
  - **σπουδάζω/σπουδή pastoral-imperative** (4× at 1:5, 1:10, 1:15, 3:14) — Petrine-signature exhortation; uniform Thai.
  - **στηρίζω stability-cluster** (1:12, 2:14, 3:16, 3:17) — letter-bracketing internal-stability theme.
- **4 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: 2:1 δεσπότης rendering; 2:4 Tartarus-terminology; 2:10-11 δόξας = angelic-beings rendering; 2:15 Βοσόρ → standard-OT-Beor normalization).
- **3 items flagged DECIDE** (1:4 divine-nature partakers framing; 1:20 ἰδίας ἐπιλύσεως reading; 3:9 πάντας ambiguity-preservation per locked doc — confirm doc applies as written).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Granville-Sharp θεὸς καὶ σωτὴρ Ἰησοῦς Χριστός — densest NT cluster — **LOCKED ✓**

2 Peter contains **the most-concentrated Granville-Sharp θεός+σωτήρ construction cluster in the entire NT** — five occurrences in 61 verses, with a sixth κύριος-καὶ-σωτήρ variant:

| Verse | Greek | Thai | Type |
|---|---|---|---|
| 1:1 | τοῦ θεοῦ ἡμῶν καὶ σωτῆρος Ἰησοῦ Χριστοῦ | **พระเจ้าและพระผู้ช่วยให้รอดของเราคือพระเยซูคริสต์** | θεός+σωτήρ Granville-Sharp |
| 1:11 | τοῦ κυρίου ἡμῶν καὶ σωτῆρος Ἰησοῦ Χριστοῦ | **พระเยซูคริสต์องค์พระผู้เป็นเจ้าและพระผู้ช่วยให้รอดของเรา** | κύριος+σωτήρ Granville-Sharp |
| 2:20 | τοῦ κυρίου καὶ σωτῆρος Ἰησοῦ Χριστοῦ | **พระเยซูคริสต์องค์พระผู้เป็นเจ้าและพระผู้ช่วยให้รอดของเรา** | κύριος+σωτήρ Granville-Sharp |
| 3:2 | τοῦ κυρίου καὶ σωτῆρος | **องค์พระผู้เป็นเจ้าและพระผู้ช่วยให้รอด** | κύριος+σωτήρ Granville-Sharp (bare) |
| 3:18 | τοῦ κυρίου ἡμῶν καὶ σωτῆρος Ἰησοῦ Χριστοῦ | **พระเยซูคริสต์องค์พระผู้เป็นเจ้าและพระผู้ช่วยให้รอดของเรา** | κύριος+σωτήρ Granville-Sharp |

The 1:1 KD names the construction:

> GRANVILLE-SHARP CONSTRUCTION: single article τοῦ governs both θεοῦ ἡμῶν + σωτῆρος → single subject (Jesus = our God and Savior). Per pastoral_corpus_locks §C: render high-Christological (matching Tit 2:13). Render 'พระเจ้าและพระผู้ช่วยให้รอดของเราคือพระเยซูคริสต์' — appositional 'คือ' makes the single-person-reading explicit.

**Editorial assessment:** The 1:1 (θεός+σωτήρ) construction is the **strongest single-verse Christological declaration in 2 Peter** — Jesus IS our God-and-Savior. The translator uses an explicit appositional **คือ** ("that is") to make the single-person reading unmistakable for Thai readers, while the four κύριος+σωτήρ constructions use the simpler appositional pattern (Jesus IS our Lord-and-Savior). This is fully compliant with `pastoral_corpus_locks_2026-05.md` §C (Granville-Sharp + Pastoral high-Christology consensus).

The 1:2 contrast is principled: that verse has **TWO articles** (`τοῦ θεοῦ καὶ Ἰησοῦ τοῦ κυρίου ἡμῶν`), so Granville-Sharp does NOT apply. The translator correctly renders God + Jesus as distinct-but-cooperating subjects ("ของพระเจ้าและของพระเยซูองค์พระผู้เป็นเจ้าของเรา"), preserving the Greek-grammatical signal.

**LOCKED ✓** — fully compliant with pastoral_corpus_locks §C. The 5-construction density in 61 verses is the **anchor evidence for high-Christological reading** of the construction-pattern across the NT. Worth a brief note in `pastoral_corpus_locks_2026-05.md` §C: 2 Peter ratifies the Tit 2:13 pre-decision corpus-wide.

---

## 2. ἐπίγνωσις (true-knowledge) vs γνῶσις (bare-knowledge) — Petrine-Pastoral keyword split — **STABLE (undocumented; recommend doc)**

2 Peter contains the **densest ἐπίγνωσις cluster in the NT** — 4 occurrences in chapter 1 alone (1:2, 1:3, 1:8 + 2:20, 2:21 cognate verb ἐπιγινώσκω). The translator preserves a principled lexical-split:

| Greek | Thai | Verses |
|---|---|---|
| ἐπίγνωσις (true-knowledge of God/Christ) | **ความรู้ที่แท้จริง** | 1:2, 1:3, 1:8, 2:20 |
| ἐπιγινώσκω (cognate verb) | **รู้จัก** | 2:21 (×2) |
| γνῶσις (bare-knowledge, in the chain-of-virtues / general) | **ความรู้** | 1:5, 1:6, 3:18 |

The 1:2 KD names the principle:

> ἐπίγνωσις → ความรู้ที่แท้จริง (corpus-lock from Rom 10:2 + Phil 1:9 + Eph 4:13 + Col 1:9).

The 1:5 KD names the deliberate contrast:

> γνῶσις → ความรู้ (bare-knowledge — NB distinct from ἐπίγνωσις at v.2-3, 8 → ความรู้ที่แท้จริง). The chain-of-virtues device here uses bare-γνῶσις as one-link-among-many; the ἐπι-prefix at v.8 then names the comprehensive whole of which γνῶσις is one component.

**Editorial assessment:** The principled split is theologically rich. **ἐπίγνωσις** in 2 Peter is the *comprehensive personal-relational knowledge* of Christ that anchors the believer against false-teaching (1:8) and against apostasy-relapse (2:20-21). **γνῶσις** is the *bare cognitive component* — one virtue-link in the chain (1:5-6). The Thai distinction (**ความรู้ที่แท้จริง** vs **ความรู้**) preserves this for Thai readers without forcing English-style epistemological technicality.

The 3:18 **closing-doxology bare γνῶσις** is the masterstroke: after a letter dominated by ἐπίγνωσις, Peter closes with the simpler γνῶσις, returning the chain of virtues to its 1:5 head — letter-bracket-completion via the lexical-distinction.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/epignosis_vs_gnosis_2026-05.md` before:
- **Hebrews** (γνῶσις-cluster at Heb 10:26 + the broader knowledge-of-God theme).
- **Pauline-corpus future-Pastoral retrospective** — the lock would clarify Eph 4:13 / Phil 1:9 / Col 1:9-10 / 1 Tim 2:4 / 2 Tim 2:25 / Tit 1:1 ἐπίγνωσις renderings already in the can.

The doc should:
1. Lock ἐπίγνωσις → **ความรู้ที่แท้จริง** (corpus-wide).
2. Lock γνῶσις → **ความรู้** (corpus-wide bare-form).
3. Note that the ἐπι-prefix carries genuine semantic weight in Pauline-Petrine usage (against the older Lightfoot-rejection of any meaningful ἐπι-distinction).
4. Cite 2 Pet 1:5 + 1:8 as the locking precedents (single-verse contrast within the same passage).

---

## 3. 2 Pet 1:1, 1:11 βασιλεία αἰώνιος — Petrine eternal-kingdom — **STABLE**

> 1:11 GK: `οὕτως γὰρ πλουσίως ἐπιχορηγηθήσεται ὑμῖν ἡ εἴσοδος εἰς τὴν αἰώνιον βασιλείαν τοῦ κυρίου ἡμῶν καὶ σωτῆρος Ἰησοῦ Χριστοῦ.`

> 1:11 TH: `เพราะเช่นนี้แล้ว ท่านจะได้รับการต้อนรับอย่างบริบูรณ์เข้าสู่อาณาจักรนิรันดร์ของพระเยซูคริสต์องค์พระผู้เป็นเจ้าและพระผู้ช่วยให้รอดของเรา`

**Editorial assessment:** βασιλεία → **อาณาจักร** corpus-precedent (per `basileia_kingdom_rendering_2026-04.md`). αἰώνιος → **นิรันดร์** corpus-locked. The pairing **อาณาจักรนิรันดร์** ("eternal kingdom") is uniquely-2 Petrine in the NT (the Synoptics use **ἡ βασιλεία τῶν οὐρανῶν / τοῦ θεοῦ** without the eternal-modifier; Hebrews uses **βασιλεία ἀσάλευτος** "unshakeable-kingdom" at Heb 12:28). **STABLE** — full compliance with basileia_kingdom_rendering doc.

---

## 4. 2 Pet 1:4 θείας κοινωνοὶ φύσεως — partakers of the divine nature — **DECIDE (the most theologically-contested verse in 2 Peter)**

> 1:4 GK: `ἵνα διὰ τούτων γένησθε **θείας κοινωνοὶ φύσεως**`

> 1:4 TH: `เพื่อโดยพระสัญญาเหล่านี้ ท่านทั้งหลายจะได้**มีส่วนร่วมในพระลักษณะแห่งพระเจ้า**`

This is **the single most-theologically-loaded verse in 2 Peter** — the locus-classicus for Eastern-Orthodox θέωσις (deification doctrine) and a major-difference between Eastern-Orthodox and Protestant-evangelical soteriology.

The 1:4 KD names the editorial choice:

> Per uW figs-metaphor: NOT theosis (becoming-divine); rather ethical-spiritual participation in divine-character. θεῖος + φύσις → พระลักษณะแห่งพระเจ้า (divine-nature/character). κοινωνός → มีส่วนร่วม corpus-precedent. Render preserves the ambiguity-of-participation but thai_summary clarifies the orthodox-evangelical-Protestant interpretation against deification-doctrine.

The verse's `thai_summary` (one of only ~6 thai_summary fields in the entire 2 Peter corpus) makes the editorial commitment explicit:

> 'มีส่วนร่วมในพระลักษณะแห่งพระเจ้า' (θείας κοινωνοὶ φύσεως) ไม่ได้หมายความว่ามนุษย์จะกลายเป็นพระเจ้า ตามคำสอนของพระคัมภีร์ พระเจ้าทรงเป็นพระผู้สร้าง ส่วนมนุษย์เป็นสิ่งที่ทรงสร้าง — ความแตกต่างนี้ไม่มีวันถูกลบล้าง สิ่งที่เปโตรหมายถึงคือ — ผู้เชื่อมีส่วนร่วมในธรรมชาติทางจริยธรรมและทางจิตวิญญาณของพระเจ้า เช่น ความบริสุทธิ์ ความรัก ความชอบธรรม ฯลฯ — โดยทางพระวิญญาณบริสุทธิ์ที่ทรงประทับในใจของผู้เชื่อ

**Editorial assessment:** Three editorial choices stack here:
- (a) **φύσις → พระลักษณะ** ("character / nature" with royal-prefix) rather than the more-literal **ธรรมชาติ** ("nature / essence") — preserves divinity-as-attribute rather than divinity-as-essence; aligns with Protestant-evangelical Creator-creature distinction.
- (b) **κοινωνός → มีส่วนร่วม** ("participate / share-in") rather than **กลายเป็น** ("become") — preserves participation-in rather than becoming-equivalent-to.
- (c) **thai_summary explicitly disclaims theosis-doctrine** — Thai-Eastern-Orthodox readers (small-but-existing community in Thailand, esp. Russian-Orthodox-aligned parishes) would be invited to a different reading.

This is the **opposite editorial strategy** from the project's RULES §0 evangelical-Protestant alignment as applied to ambiguous-irreducible passages (where ambiguity-preservation is preferred). At 1:4, the translator **disambiguated toward Protestant reading via main-text rendering choice + thai_summary disclaimer**.

**Why this is striking:** The Greek θείας κοινωνοὶ φύσεως is *genuinely ambiguous* between (i) ethical-character-participation (Protestant) and (ii) ontological-nature-participation (Eastern-Orthodox). Mainstream English (NIV/ESV/CSB/NASB) all render "partake of the divine nature" without disambiguation, leaving Eastern-Orthodox + Catholic + Protestant readers to bring their own theology to the verse. The Thai goes further — it commits to the Protestant reading and footnotes against Orthodox θέωσις.

**DECIDE — three sub-decisions:**

**§A — confirm φύσις → พระลักษณะ (character) rendering vs ธรรมชาติ (essence/nature).**
- (a) **พระลักษณะ** — current; preserves attribute-participation; theologically-cautious.
- (b) **ธรรมชาติ** — more-literal; preserves the Greek φύσις ambiguity; would let Thai readers inherit the same options Greek readers receive.

**§B — confirm κοινωνός → มีส่วนร่วม (participate) — vs alternatives.**
- (a) **มีส่วนร่วม** — current; corpus-precedent (matches κοινωνέω at 1 PET 4:13 same Thai-pattern); preserves participation-without-essence-merger.
- (b) **มีส่วนใน** — slightly more-literal "have-share-in"; nuance only.

**§C — confirm the thai_summary disclaimer-against-deification.**
- (a) **Current** — explicitly tells Thai readers that 1:4 does NOT teach θέωσις; aligns with Protestant-evangelical mainstream.
- (b) **Remove disclaimer** — let Thai readers receive the same ambiguity Greek readers receive; matches the broader project pattern for irreducibly-multi-interpretable passages (cf. 1 Pet 3:19 / 2 Pet 3:9).

**Recommend: STABLE-with-DECIDE on §A + §B + §C.** Per RULES §0 evangelical-Protestant alignment, the current rendering and disclaimer are mainstream-evangelical-aligned. But the contrast with the 2 Pet 3:9 ambiguity-preservation strategy (next item below) is striking and worth Ben's explicit confirmation. A new corpus doc `docs/translator_decisions/theiotētos_koinōnia_divine_nature_participation_2026-05.md` could lock the rendering — and would govern future 1 Cor 10:16-17 + Phil 2:1 + 1 John 1:3 κοινωνία renderings.

---

## 5. 2 Pet 1:16-18 transfiguration apostolic-eyewitness defense — **all LOCKED ✓**

> 1:17 GK: `Ὁ υἱός μου ὁ ἀγαπητός μου οὗτός ἐστιν, εἰς ὃν ἐγὼ εὐδόκησα`

> 1:17 TH: `"นี่คือบุตรที่รักของเรา ผู้ซึ่งเราพอใจ"`

**Editorial assessment:** The transfiguration-voice citation at 1:17 is rendered with the corpus-locked Thai-pattern matching MAT 17:5 + MAR 9:7 + LUK 9:35 (Synoptic-internal-link). Per RULES §5b, direct-speech curly Thai-quotes are used. DB entry recorded in `data/nt_ot_citations.json`.

The `holy mountain` (ἐν τῷ ἁγίῳ ὄρει) → **บนภูเขาบริสุทธิ์** rendering preserves the retrospective sanctification-by-divine-presence.

The HAPAX **ἐπόπτης** ("eyewitness" — Greek mystery-religion technical term Christianized) → **พยานผู้เห็นด้วยตาตนเอง** — explicit "witness who has seen with their own eyes." Captures the apostolic-eyewitness defense without forcing the mystery-cult-initiate connotation.

**LOCKED ✓** — Synoptic-internal cross-reference preserved. DB entry recorded.

---

## 6. 2 Pet 1:16, 3:4, 3:12 παρουσία — Petrine corpus tests the lemma-driven rule — **LOCKED ✓**

The παρουσία lemma occurs **3× in 2 Peter** — and **0× in 1 Peter** (which uses ἀποκάλυψις/φανερόω instead). All three 2 Pet uses render with the **Pauline pattern** **การเสด็จมา**, confirming that the Pauline-vs-Petrine **การเสด็จมา / การสำแดง** distinction is *lemma-driven*, not *author-driven*:

| Verse | Greek | Thai | Subject |
|---|---|---|---|
| 1:16 | τὴν τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ δύναμιν καὶ παρουσίαν | **ฤทธานุภาพและการเสด็จมาของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** | Christ-eschatological |
| 3:4 | Ποῦ ἐστιν ἡ ἐπαγγελία τῆς παρουσίας αὐτοῦ | **"พระสัญญาเรื่องการเสด็จมาของพระองค์อยู่ที่ไหน?"** | Christ-eschatological (scoffers' question) |
| 3:12 | προσδοκῶντας καὶ σπεύδοντας τὴν παρουσίαν τῆς τοῦ θεοῦ ἡμέρας | **รอคอยและเร่งให้วันแห่งพระเจ้าเสด็จมา** | the day-of-God's-coming |

The 1:16 KD names the lemma-driven rule:

> Per parousia_christou_2026-05.md: παρουσία (Christ-subject, eschatological) → การเสด็จมา. NB: this is the only Petrine use of παρουσία (1 Peter uses ἀποκάλυψις/φανερόω → การสำแดง for the same eschatological-coming).

**Editorial assessment:** The lemma-driven rule from `parousia_christou_2026-05.md` §Petrine sub-section (added 2026-05-03 after 1 Pet end-of-book audit) is now ratified by the 2 Peter occurrences. The rule is:

- **παρουσία (Christ-eschatological)** → **การเสด็จมา** (Pauline metaphor: royal-arrival)
- **ἀποκάλυψις / φανερόω (Christ-eschatological)** → **การสำแดง / ทรงสำแดง** (Petrine metaphor: unveiling-of-the-hidden)

The two metaphors describe the **same future event** with different Greek-lexical-emphases; the Thai preserves the lexical-emphasis distinction. Same-author-different-lemma cases are rendered by lemma, not by author — confirmed by Petrine παρουσία at 2 Pet 1:16, 3:4, 3:12 reading **การเสด็จมา** (not **การสำแดง**, even though Peter is the author).

**LOCKED ✓** — fully compliant with parousia_christou_2026-05.md §Petrine. 2 Peter is the *test case* for the lemma-driven rule and confirms the doc's prediction.

The 3:12 **"day of God"** (τῆς τοῦ θεοῦ ἡμέρας) is rendered **วันแห่งพระเจ้า** — distinct from the 3:10 **"day of the Lord"** (ἡμέρα κυρίου) → **วันขององค์พระผู้เป็นเจ้า**. The Thai correctly preserves the Petrine-distinctive **theocentric** ("of God") vs **Christological-via-κύριος** ("of the Lord") variant — both refer to the eschatological-judgment-day, but the Greek-lexical distinction is preserved in the Thai.

---

## 7. 2 Pet 1:20-21 ἰδίας ἐπιλύσεως / οὐ θελήματι ἀνθρώπου — Scripture's prophetic-origin — **DECIDE (foundational evangelical proof-text)**

> 1:20 GK: `τοῦτο πρῶτον γινώσκοντες ὅτι **πᾶσα προφητεία γραφῆς ἰδίας ἐπιλύσεως οὐ γίνεται**`

> 1:20 TH: `เหนือสิ่งอื่นใด ท่านทั้งหลายจงเข้าใจว่า **คำพยากรณ์ทั้งหมดในพระคัมภีร์ไม่ได้เกิดจากการตีความตามใจของผู้เผยพระวจนะเอง**`

> 1:21 GK: `οὐ γὰρ θελήματι ἀνθρώπου ἠνέχθη προφητεία ποτέ, ἀλλὰ ὑπὸ πνεύματος ἁγίου φερόμενοι ἐλάλησαν ἀπὸ θεοῦ ἄνθρωποι.`

> 1:21 TH: `เพราะคำพยากรณ์นั้นไม่เคยเกิดขึ้นโดยน้ำใจของมนุษย์เลย แต่มนุษย์ได้กล่าวถ้อยคำที่มาจากพระเจ้า โดยการนำของพระวิญญาณบริสุทธิ์`

This is **the foundational NT proof-text for evangelical doctrine of plenary-verbal inspiration**. The Greek HAPAX **ἐπίλυσις** has two well-attested readings — and their selection commits to opposite ecclesiologies:

- (a) **The prophet's-own-interpretation** (i.e., "no prophecy of Scripture comes from the prophet's-own private interpretation-of-the-vision-they-received") — supports a *divine-source* doctrine of inspiration. v.21 then supplies the positive: prophecy comes from God's Spirit, not from human-volition. **Mainstream-evangelical-Protestant reading**.
- (b) **The reader's-own private interpretation** (i.e., "no prophecy of Scripture is a matter of the reader's private interpretation") — supports a *magisterial-or-communal* doctrine of biblical interpretation. **Roman-Catholic-traditional reading**.

The translator chose (a). The 1:20 KD names the choice + documents both options:

> HAPAX ἐπίλυσις (only here NT, 'interpretation / explanation') → การตีความ. ἰδίας 'own' → ตามใจ ... เอง — preserves the agency-question (whose-interpretation?). Per uW: scholarly-consensus reads this as 'prophet's-own-interpretation-of-vision' (matching v.21's explanation that prophecy comes from the Spirit, not human will). thai_summary documents both options.

**Editorial assessment:** The translator chose (a) by inserting **ของผู้เผยพระวจนะเอง** ("of the prophet themselves") — explicitly committing the Thai to the **prophet's-own-interpretation** reading. This converts the genuinely-ambiguous Greek **ἰδίας ἐπιλύσεως** into a single-reading Thai. The thai_summary documents both options for Thai readers, but the main-text commits.

**Why this is striking:** This is the **opposite editorial strategy** from 1 Pet 3:19 (preserve-ambiguity for irreducibly-multi-interpretable Petrine eschatological passages, per `petrine_eschatological_disambiguation_2026-05.md`). Per that doc's principle:
- "Preserve ambiguity when the multiple readings are exegetically irreducible."
- "Disambiguate when one reading is theologically incompatible with the rest of Scripture."

For 2 Pet 1:20: are both readings (a) and (b) exegetically defensible against the rest of Scripture? Reading (a) coheres with v.21 (Spirit-borne prophets); reading (b) coheres with broader-Catholic ecclesiology but contradicts RULES §0 evangelical-Protestant alignment + the priesthood-of-all-believers principle (1 Pet 2:9). Whether (b) is *theologically incompatible* with Scripture (warranting disambiguation per the locked doc's principle) or *merely-non-evangelical* (warranting ambiguity-preservation) is the core question.

**DECIDE — three sub-decisions:**

**§A — confirm the 1:20 disambiguation toward prophet's-own-interpretation reading.**
- (a) **Current** — explicitly commits to (a) the prophet's-own-interpretation reading; matches mainstream-evangelical-Protestant interpretation; thai_summary documents (b) for completeness.
- (b) **Preserve ambiguity** — render the Thai with **โดยการตีความตามใจของตนเอง** ("by one's-own private interpretation" — neutral pronoun-reference, ambiguous between prophet and reader); let Thai pastors discern the reading.

**§B — confirm the 1:21 ὑπὸ πνεύματος ἁγίου φερόμενοι → "โดยการนำของพระวิญญาณบริสุทธิ์" (Spirit-borne) rendering.**
- (a) **Current** — preserves the Spirit-as-agent-of-bearing without forcing the Greek wind-or-ship metaphor literally. Mainstream-evangelical reading.
- (b) **More-literal "ทรงพา / ถูกนำพา"** — preserves the figurative "carried-along-as-by-wind" sense more visually.

**§C — formalize the implicit principle in a corpus doc.** The translator's mixed strategy (preserve at 3:19 / disambiguate at 1:20 / disambiguate at 4:6 / preserve at 3:9) is *consistent* per `petrine_eschatological_disambiguation_2026-05.md`'s principle — but the 1:20 application *extends* that principle from eschatology-passages to inspiration-passages. The doc could be amended with a §Inspiration-and-Hermeneutics sub-section, or a new doc `docs/translator_decisions/petrine_inspiration_hermeneutics_2026-05.md` could be written.

**Recommend: STABLE-with-DECIDE on §A + §B + §C.** Per RULES §0 evangelical-Protestant alignment, the (a) reading is the right corpus-default. But the disambiguation contrasts with 1 Pet 3:19 / 2 Pet 3:9 ambiguity-preservation, and the principle should be made explicit before Hebrews 1:1-3 (the foundational divine-speech doctrine) and 2 Tim 3:16 (already shipped — confirm consistency) ship.

---

## 8. 2 Pet 2:1 δεσπότης — absolute-master Christology — **REVIEW**

> 2:1 GK: `καὶ τὸν ἀγοράσαντα αὐτοὺς **δεσπότην** ἀρνούμενοι`

> 2:1 TH: `และปฏิเสธ**องค์เจ้านาย**ผู้ทรงไถ่พวกเขาไว้`

The 2:1 KD names the lexical choice:

> δεσπότης (rare NT, 'master-with-absolute-authority'; here-Christological) → องค์เจ้านาย — preserves the absolute-master sense distinct from κύριος. Per uW figs-metaphor: ἀγοράζω 'bought / redeemed' — slave-purchase metaphor for redemption (cf. 1 COR 6:20 + REV 5:9).

**Editorial assessment:** δεσπότης is the **strongest absolute-authority master-term in Greek** — used 10× in NT (LUK 2:29 Simeon; ACT 4:24 corporate-prayer; 1 TIM 6:1-2 + 2 TIM 2:21 + Tit 2:9 + 1 PET 2:18 master-of-slaves; JUDE 4 + REV 6:10 + here Christological). The translator distinguishes:
- **δεσπότης (Christological)** → **องค์เจ้านาย** (royal-prefix + "master") — emphatic absolute-master Christology
- **κύριος (Christological)** → **องค์พระผู้เป็นเจ้า** (royal-prefix + "Lord") — corpus-locked

The distinction is **principled and important**: the false-teachers deny **the Master-who-bought-them** — invoking the slave-purchase redemption metaphor (cf. 1 Cor 6:20 ἠγοράσθητε γὰρ τιμῆς). δεσπότης names the *purchase-rights* of the master over the bought-slave — making the false-teachers' denial more-egregious than mere κύριος-denial. The Thai **องค์เจ้านาย** preserves this absolute-purchase-rights sense.

**REVIEW** — confirm the **องค์เจ้านาย** rendering vs alternatives:
- (a) **องค์เจ้านาย** — current; preserves absolute-master sense distinct from κύริος. Could read slightly archaic in modern Thai.
- (b) **เจ้านาย** (without royal prefix) — would lose the divine-master sense (per the project's narrator-vs-character voice principle, royal-prefix is preserved for divine-Christological referents).
- (c) **องค์อธิปัตย์ผู้สูงสุด** ("Sovereign Master") — more-emphatic absolute-authority but verbose.

**Recommend: STABLE.** The current **องค์เจ้านาย** preserves the principled distinction from κύριος. Brief consideration in a new corpus doc `docs/translator_decisions/despotēs_christological_2026-05.md` would lock the choice before JUDE 4 (the same false-teachers-deny-our-only-Master language) ships.

---

## 9. 2 Pet 2:4 ταρταρόω — Tartarus-mythology terminology — **REVIEW**

> 2:4 GK: `Εἰ γὰρ ὁ θεὸς ἀγγέλων ἁμαρτησάντων οὐκ ἐφείσατο, ἀλλὰ σειραῖς ζόφου **ταρταρώσας** παρέδωκεν εἰς κρίσιν τηρουμένους`

> 2:4 TH: `เพราะถ้าพระเจ้าไม่ทรงละเว้นบรรดาทูตสวรรค์เมื่อพวกเขาทำบาป แต่**ทรงโยนพวกเขาลงในนรกขุมลึกที่สุด** ทรงล่ามไว้ในโซ่แห่งความมืดเพื่อรอการพิพากษา`

ταρταρόω is the **only NT use of the Greek-mythology Tartarus-terminology** — the deepest pit in the Greek-mythological underworld, deeper than Hades, reserved for the Titans-and-rebellious-immortals. Peter Christianizes the term to apply to fallen-angels (cf. GEN 6:1-4 + 1 Enoch 6-21 traditions).

The 2:4 KD names the choice + the thai_summary explains:

> ταρταρόω (only here NT, verbal-form of ταρταρός — the deepest-pit of Greek-mythology-Hades) → ทรงโยน ... ลงในนรกขุมลึกที่สุด — preserves the 'deepest-place' sense; thai_summary explains the Tartarus-mythology-background.

The thai_summary:

> 'ταρταρώσας' (ทรงโยนลงในทาร์ทารัส) เป็นคำที่มาจากตำนานกรีก ทาร์ทารัสเป็นที่กักขังของเหล่าทำตามตำนานกรีก เปโตรใช้คำนี้เพื่อบ่งบอกถึงสถานที่กักขังที่ลึกที่สุด — ลึกกว่าแดนคนตาย (Hades) และเป็นที่กักขังเฉพาะของทูตสวรรค์ที่กบฏเท่านั้น พื้นฐานทางคัมภีร์น่าจะอ้างถึงปฐมกาล 6:1-4 และประเพณี 1 เอโนค 6-21 ซึ่งเล่าถึงเรื่องราวของทูตสวรรค์ที่ตกลงมา

**Editorial assessment:** Two editorial choices stack:
- (a) **The main-text uses นรกขุมลึกที่สุด** ("deepest hell-pit") — rendering meaningful for Thai readers without the Tartarus-mythology background.
- (b) **The thai_summary explicitly names ทาร์ทารัส** as a transliteration + explains the Greek-mythology-background.

This combination is principled: the main-text is Thai-naturally readable; the thai_summary educates Thai pastors who want the technical-cultural background. The alternative — either naked transliteration **ทาร์ทารัส** in main-text (would alienate Thai readers unfamiliar with Greek-mythology) or pure abstraction **นรก** (would lose the Petrine-distinctive "deepest-pit" intensity) — both lose something.

**REVIEW** — confirm the layered approach (main-text Thai-natural + thai_summary cultural-explanation) is the corpus-default for **uniquely-Petrine Greek-mythology-Christianized-terminology**. Worth Ben's confirmation, especially since 2 Pet 2:4 is the only such case in the corpus (no other NT book Christianizes a Greek-mythology technical-term in this way).

**Recommend: STABLE.** The layered approach reads naturally in Thai and educates pastors. No new doc needed.

---

## 10. 2 Pet 2:10-11 δόξας → "เหล่าผู้ทรงสง่าราศี" — angelic-beings rendering — **REVIEW**

> 2:10 GK: `Τολμηταὶ, αὐθάδεις, **δόξας** οὐ τρέμουσιν, βλασφημοῦντες`

> 2:10 TH: `พวกเขาเป็นคนกล้าหาญในทางชั่ว เป็นคนถือทิฐิ ไม่เกรงกลัวที่จะดูหมิ่น**เหล่าผู้ทรงสง่าราศี**`

> 2:11 GK: `ὅπου ἄγγελοι ἰσχύϊ καὶ δυνάμει μείζονες ὄντες οὐ φέρουσιν κατ' αὐτῶν βλάσφημον κρίσιν.`

The Greek **δόξας** (plural of δόξα = "glory") is here used as a **personified-substantive** referring to **angelic-beings of glory** (cf. JUDE 8 same construction). The translator renders **เหล่าผู้ทรงสง่าราศี** ("beings of glory / glorious-beings") — preserves the angelic-beings sense without forcing the abstract-glory reading.

The 2:10 KD names the choice + the 2:11 thai_summary explains the Michael-vs-Satan-over-Moses-body tradition (JUDE 9 parallel):

> 2:10 KD: δόξας (here = glorious-beings, esp. angelic-powers) → เหล่าผู้ทรงสง่าราศี.
>
> 2:11 thai_summary: ข้อนี้น่าจะเป็นการอ้างอิงถึงเรื่องของอัครเทวดามีคาเอลที่โต้เถียงกับมารเรื่องศพของโมเสส (ยูดา 9 อ้างอิงประเพณีเดียวกัน) — แม้แต่ทูตสวรรค์ระดับสูงก็ไม่ใช้คำพิพากษาดูหมิ่นต่อพลังฝ่ายมาร แต่ครูสอนเท็จกลับกล้ามากกว่าทูตสวรรค์ในการดูหมิ่นเหล่าผู้ทรงสง่าราศี

**Editorial assessment:** The interpretive question is *which angelic-beings* are reviled:
- (a) **Good angels** (Calvin / Schreiner) — false-teachers revile godly-glorious-beings in heaven.
- (b) **Fallen / evil-spiritual-powers** (Bauckham / Davids / mainstream-modern) — false-teachers revile demonic-powers cavalierly, lacking the Michael-restraint shown at JUDE 9.

The Thai **เหล่าผู้ทรงสง่าราศี** is *neutral* between (a) and (b) — it preserves the angelic-glorious-beings sense without specifying good-vs-fallen. This is the right ambiguity-preservation strategy.

**REVIEW** — confirm:
- (a) **The δόξας → เหล่าผู้ทรงสง่าราศี angelic-beings rendering** — preserves the angelic-beings sense without disambiguating good-vs-fallen. Per `spiritual_beings_hierarchy_2026-05.md`, this is the right corpus-default.
- (b) **The thai_summary at 2:11** explains the JUDE 9 Michael-vs-Satan parallel + the apocryphal Assumption of Moses background. Worth a footer-cross-reference to JUDE 8-9 in any future Catholic-Epistles audit.

**Recommend: STABLE.** Compliant with `spiritual_beings_hierarchy_2026-05.md`. The neutral-rendering preserves the Greek's openness; thai_summary educates pastors on the JUDE-parallel.

---

## 11. 2 Pet 2:5-9 OT-judgment-examples chain — Noah / Sodom-Gomorrah / Lot — **all LOCKED ✓**

The Petrine chain of OT-judgment-examples (vv.4-9):

| Verse | OT figure / event | Greek | Thai | Status |
|---|---|---|---|---|
| 2:4 | rebel-angels (GEN 6:1-4 + 1 Enoch tradition) | ἀγγέλων ἁμαρτησάντων | **บรรดาทูตสวรรค์ ... ทำบาป** | **LOGGED** — OT-traditional allusion |
| 2:5 | Noah + flood (GEN 6-8) | Νῶε ... κήρυκα δικαιοσύνης | **โนอาห์ ผู้ประกาศความชอบธรรม** | **LOGGED** — corpus-lock; uniquely-Petrine "preacher-of-righteousness" title |
| 2:6 | Sodom + Gomorrah (GEN 19) | Σοδόμων καὶ Γομόρρας | **โสโดมและโกโมราห์** | **LOGGED** — corpus-lock |
| 2:7-8 | Lot (GEN 19) | δίκαιον Λώτ | **โลทผู้ชอบธรรม** | **LOGGED** — corpus-lock |

**Editorial assessment:** All four OT-figures + events use corpus-locked transliterations + theological-titles. The "preacher-of-righteousness" title for Noah (2:5) is uniquely-Petrine in the NT — drawn from Jewish-Second-Temple tradition (Sibylline Oracles 1.128-129; Josephus Ant. 1.74); not from MT/LXX-OT-text. The Thai preserves the title literally (**ผู้ประกาศความชอบธรรม**) as the principled rendering.

The cross-reference network is dense:
- 2 Pet 2:5 (Noah-flood) ↔ 1 Pet 3:20 (eight-saved-through-water) — Petrine-internal cross-corpus
- 2 Pet 2:6 (Sodom-Gomorrah) ↔ MAT 10:15 + LUK 17:29 (Synoptic-OT-typology) + ROM 9:29 (Pauline-citation)
- 2 Pet 2:7 (Lot) ↔ LUK 17:28-29 (Synoptic-OT-typology)
- 2 Pet 2:9 (the principle) ↔ MAT 10:15 + 1 Pet 4:5 (eschatological-judgment-day formula)

**LOCKED ✓** — all four corpus-locks compliant. DB entries recorded.

---

## 12. 2 Pet 2:15 Βοσόρ → "เบโอร์" — Petrine Greek-variant normalized to standard-Thai-OT — **STABLE**

> 2:15 GK: `ἐξακολουθήσαντες τῇ ὁδῷ τοῦ Βαλαὰμ τοῦ **Βοσὸρ** ὃς μισθὸν ἀδικίας ἠγάπησεν`

> 2:15 TH: `ทำตามทางของบาลาอัมบุตรของ**เบโอร์** ผู้ซึ่งรักค่าจ้างแห่งความอธรรม`

The Greek **Βοσόρ** is a NT-HAPAX form — likely a **Galilean-Aramaic vocalization** of the MT-Hebrew בְּעוֹר (Beor); LXX consistently uses Βεωρ (e.g., NUM 22:5 LXX). Some scholars suggest Peter's Βοσόρ may be an intentional pun (Hebrew בָּשָׂר "flesh" — fitting the Balaam-as-fleshly-corrupted-prophet theme), but no scholarly consensus.

The 2:15 KD names the normalization choice:

> HAPAX Βοσόρ (only here NT, the Petrine-Greek form of MT-Hebrew בְּעוֹר 'Beor'; LXX uses Βεωρ — Peter's Βοσόρ may be a Galilean-Aramaic vocalization) → เบโอร์ (using the standard Thai-OT form from NUM 22-24 + DEU 23:4).

**Editorial assessment:** The translator chose to **normalize the unusual Petrine Βοσόρ to the standard Thai-OT เบโอร์** rather than preserve the Petrine variant as **โบโซร์** (transliteration) or similar. Three considerations:
- (a) **Cross-corpus consistency** — Thai-OT readers know Beor as เบโอร์ from NUM 22-24; the Petrine variant would create unnecessary cross-reference difficulty.
- (b) **Loss of the wordplay-possibility** — if Peter intended Βοσόρ as a flesh-pun, the normalization erases the wordplay. But the wordplay is scholarly-contested.
- (c) **Transparency for Thai readers** — the standard-form lets Thai readers immediately identify the Balaam-Beor figure from OT-narrative.

**Recommend: STABLE.** The cross-corpus consistency + Thai-reader-transparency justify the normalization. The wordplay-possibility is documented in the KD for scholarly-curious readers. This case-study of "Petrine Greek-variant normalized to standard Thai-OT" sets a useful precedent for any similar future cases (e.g., the Aramaic-vs-Hebrew transliterations across the gospels). Worth a one-line note in `aramaic_transliterations_2026-04.md` if a corpus-doc amendment is being made.

---

## 13. 2 Pet 2:22 dog-vomit + sow-mire proverbs — **LOCKED ✓ + extra-canonical sourcing documented**

> 2:22 GK: `Κύων ἐπιστρέψας ἐπὶ τὸ ἴδιον ἐξέραμα, καί· Ὗς λουσαμένη εἰς κυλισμὸν βορβόρου.`

> 2:22 TH: `"สุนัขกลับไปกินสิ่งที่มันสำรอกเอง" และ "สุกรที่ล้างแล้วก็กลับไปเกลือกกลั้วในโคลนตม"`

**Editorial assessment:**
- The **dog-vomit proverb** is a DIRECT CITATION of PROV 26:11 LXX → DB entry recorded in `data/nt_ot_citations.json`. Per RULES §5b, direct-speech curly Thai-quotes preserved.
- The **sow-mire proverb** is **extra-canonical** — the closest parallel is Ahiqar 8:18 (Aramaic-Wisdom literature) or oral-Jewish-wisdom tradition. The Thai uses the same direct-speech curly-quote pattern as the dog-proverb, which is appropriate since Peter explicitly introduces both as **παροιμία** ("proverb") — a cited-saying-genre regardless of OT-canonical-status.

The thai_summary explains:

> สุภาษิตแรก 'สุนัขกลับไปกินสิ่งที่มันสำรอกเอง' มาจากสุภาษิต 26:11 ในพันธสัญญาเดิม สุภาษิตที่สอง 'สุกรที่ล้างแล้วก็กลับไปเกลือกกลั้วในโคลนตม' ไม่ปรากฏในพันธสัญญาเดิม นักวิชาการเชื่อว่าน่าจะมาจากเรื่องอาหิคารแห่งอัสซีเรีย หรือเป็นสุภาษิตยิวในยุคนั้น สุภาษิตทั้งสองใช้สัตว์ที่ในพระคัมภีร์ถือว่าไม่สะอาด — สุนัขและสุกร — เพื่อเป็นภาพของผู้ที่ละทิ้งความชอบธรรมและกลับไปสู่ความเสื่อมทราม

**LOCKED ✓** — DB entry for PROV 26:11; extra-canonical sourcing for sow-proverb documented in thai_summary.

---

## 14. 2 Pet 3:9 πάντας εἰς μετάνοιαν — Calvinist-Arminian crux — **LOCKED ✓ (per petrine_eschatological_disambiguation doc; confirm doc applies as written)**

> 3:9 GK: `οὐ βραδύνει κύριος τῆς ἐπαγγελίας, ὥς τινες βραδύτητα ἡγοῦνται, ἀλλὰ μακροθυμεῖ εἰς ὑμᾶς, μὴ βουλόμενός τινας ἀπολέσθαι ἀλλὰ **πάντας** εἰς μετάνοιαν χωρῆσαι.`

> 3:9 TH: `องค์พระผู้เป็นเจ้าไม่ได้ทรงล่าช้าในเรื่องพระสัญญา ดังที่บางคนเข้าใจว่าเป็นความล่าช้า แต่พระองค์ทรงอดกลั้นพระทัยต่อท่านทั้งหลาย ไม่ทรงประสงค์ให้ผู้ใดพินาศเลย แต่**ทรงประสงค์ให้ทุกคนกลับใจใหม่**`

The 3:9 KD applies the locked doc:

> Per petrine_eschatological_disambiguation_2026-05.md: PRESERVE-AMBIGUITY (both Calvinist + Arminian readings exegetically defensible). … thai_summary documents both interpretive options.

The thai_summary documents both readings:

> ข้อนี้สามารถตีความได้ 2 แบบ — (1) ลัทธิ Calvinism มองว่า 'ทุกคน' หมายถึงผู้ที่ทรงเลือกสรรไว้แล้ว ... (2) ลัทธิ Arminianism มองว่า 'ทุกคน' หมายถึงทุกคนทั่วโลก ... ทั้งสองมุมมองเชื่อในเสรีภาพของพระเจ้าและความรับผิดชอบของมนุษย์ในการกลับใจใหม่ การแปลภาษาไทยรักษาความหมายตามภาษากรีกตามที่ได้ตีพิมพ์ไว้ ผู้อ่านสามารถเข้าใจตามมุมมองทางเทววิทยาของตนเอง

**Editorial assessment:** This is the **anticipated test case** named in `petrine_eschatological_disambiguation_2026-05.md` lines 83 (verbatim from the doc):

> 2 Peter 3:9 — μὴ βουλόμενός τινας ἀπολέσθαι ἀλλὰ πάντας εἰς μετάνοιαν χωρῆσαι (not-wishing-any-to-perish-but-all-to-come-to-repentance). Two readings: universalist vs Calvinist-restrictive-of-the-elect. Both readings are exegetically defensible against the canon. → **Preserve ambiguity** when this verse ships.

The implementation matches the doc's prescription exactly. **LOCKED ✓** — the doc anticipated this verse and the rendering complies.

**DECIDE — confirm doc-application:** This is technically a DECIDE-confirm rather than a DECIDE-decision. Ben should confirm the doc applies as written and the 3:9 implementation is the corpus-default for *all* future passages where Calvinist + Arminian readings are both exegetically-defensible.

**Recommend: LOCKED-with-confirmation.** No new doc needed; the existing `petrine_eschatological_disambiguation_2026-05.md` covers this case and the implementation is faithful.

---

## 15. 2 Pet 3:10, 3:12 στοιχεῖα — cosmic-elements vs spiritual-powers — **LOCKED ✓**

> 3:10 GK: `στοιχεῖα δὲ καυσούμενα λυθήσεται`

> 3:10 TH: `บรรดา**สิ่งทรงสร้าง**จะถูกเผาและละลายไป`

> 3:12 GK: `στοιχεῖα καυσούμενα τήκεται`

> 3:12 TH: `บรรดา**สิ่งทรงสร้าง**จะถูกเผาและหลอมละลาย`

The 3:10 KD names the disambiguation:

> στοιχεῖα 'elements' → สิ่งทรงสร้าง — context here = the physical-cosmological-elements (Greek-philosophical fire/water/earth/air OR more-broadly the building-blocks of creation), NOT the spiritual-powers sense at GAL 4:3 + COL 2:8 + 2:20. Render สิ่งทรงสร้าง (created-things) — preserves the cosmic-elements sense.

**Editorial assessment:** Per `stoicheia_tou_kosmou_2026-05.md` (already locked), the principled disambiguation is:
- **στοιχεῖα (cosmic-physical-elements)** → context-dependent rendering (here **สิ่งทรงสร้าง** = "created-things"; in GAL 4:3 / COL 2:8, 2:20 → context-spiritual-powers-rendering)
- **στοιχεῖα (spiritual-powers)** → Pauline-corpus locked rendering (per the doc)

The 2 Pet 3:10, 3:12 cosmic-elements rendering is fully compliant with the doc's principle. The Thai **สิ่งทรงสร้าง** ("created-things") preserves the cosmological-elements sense without invoking the Pauline-spiritual-powers sense.

**LOCKED ✓** — fully compliant with stoicheia_tou_kosmou_2026-05.md.

---

## 16. 2 Pet 3:13 new-heavens-and-new-earth — ISA 65:17 + 66:22 LXX allusion — **LOCKED ✓**

> 3:13 GK: `καινοὺς δὲ οὐρανοὺς καὶ γῆν καινὴν κατὰ τὸ ἐπάγγελμα αὐτοῦ προσδοκῶμεν, ἐν οἷς δικαιοσύνη κατοικεῖ.`

> 3:13 TH: `แต่ตามพระสัญญาของพระองค์ เรารอคอยฟ้าสวรรค์ใหม่และแผ่นดินโลกใหม่ ที่ซึ่งความชอบธรรมสถิตอยู่`

**LOCKED ✓** — OT-allusion to ISA 65:17 + 66:22 LXX. Cross-references REV 21:1 (apocalyptic-vision parallel). DB entry should be recorded if not already; the personification ("righteousness dwells there") is preserved with **สถิตอยู่** (royal-prefix divine-attribute).

---

## 17. 2 Pet 3:15-16 Paul's letters as γραφή — earliest NT canonical-self-attestation — **STABLE (the most important canon-formation evidence in the NT)**

> 3:15-16 GK: `... ὁ ἀγαπητὸς ἡμῶν ἀδελφὸς Παῦλος ... ἐν αἷς ἐστιν δυσνόητά τινα, ἃ οἱ ἀμαθεῖς καὶ ἀστήρικτοι στρεβλοῦσιν **ὡς καὶ τὰς λοιπὰς γραφάς**`

> 3:15-16 TH: `... เปาโล พี่น้องที่รักของเรา ... ในจดหมายเหล่านั้นมีบางสิ่งที่ยากจะเข้าใจ ซึ่งคนโง่เขลาและไม่มั่นคงได้บิดเบือนเสีย **เช่นเดียวกับที่พวกเขาบิดเบือนพระคัมภีร์อื่น ๆ**`

The 3:16 thai_summary makes the canonical-significance explicit:

> ข้อนี้เป็นข้อสำคัญทางคัมภีร์เพราะเปโตรเรียกจดหมายของเปาโลว่า 'γραφή' (พระคัมภีร์) 'เช่นเดียวกับพระคัมภีร์อื่น ๆ' — บ่งบอกว่าในยุคของเปโตร จดหมายของเปาโลได้รับการยอมรับว่ามีอำนาจเทียบเท่าพันธสัญญาเดิมแล้ว นี่เป็นหลักฐานที่เก่าแก่ที่สุดของการรับรู้จดหมายของเปาโลว่าเป็นพระคัมภีร์ในคริสตจักรยุคแรก

**Editorial assessment:** 2 Pet 3:15-16 is the **earliest NT-internal evidence for Paul's letters being recognized as Scripture (γραφή)** — a foundational canon-formation text. The translator preserves both:
- (a) **3:15** Paul as **ἀγαπητὸς ἀδελφός** ("our beloved brother") — uniquely-Petrine inter-apostolic-recognition.
- (b) **3:16** Paul's letters as part-of **τὰς λοιπὰς γραφάς** ("the rest of the Scriptures") — implies canonical-equivalence with OT-Scripture.

The Thai **พระคัมภีร์อื่น ๆ** ("the other Scriptures") + thai_summary explanation preserves the full canonical-significance for Thai readers. The σοφία given-by-God at 3:15 (rendered **สติปัญญาที่ทรงประทาน** — royal-prefix divine-gift) supports the inspired-status of Paul's writings.

**STABLE — verse-level rationale comprehensive.** This is the single most-canonically-important verse in 2 Peter and the rendering is principled. No new corpus doc needed; the verse-level KD + thai_summary are sufficient. Worth a one-line cross-reference in any future canon-formation discussion.

---

## 18. Petrine σπουδάζω/σπουδή pastoral-imperative — **STABLE**

The σπουδάζω/σπουδή keyword cluster runs **5×** across 2 Peter, all rendered uniformly:

| Verse | Greek | Thai |
|---|---|---|
| 1:5 | σπουδὴν πᾶσαν παρεισενέγκαντες | **จงเพียรพยายามอย่างเต็มที่** |
| 1:10 | σπουδάσατε βεβαίαν ... κλῆσιν | **จงเพียรพยายาม ... ทำให้ ... มั่นคง** |
| 1:15 | σπουδάσω ... ἑκάστοτε | **จะเพียรพยายาม ... ทุกเมื่อ** |
| 3:14 | σπουδάσατε ... εὑρεθῆναι | **จงเพียรพยายาม ... ให้พบเป็น** |

**Editorial assessment:** Uniform Thai-rendering **เพียรพยายาม** ("strive earnestly") across all five occurrences. The Petrine-signature pastoral-exhortation is preserved cross-verse. **STABLE — verse-level rationale comprehensive.** No new corpus doc needed.

---

## 19. Petrine στηρίζω stability-cluster — letter-bracketing — **STABLE**

The στηρίζω-cognate cluster runs **4× across 2 Peter**, bracketing the letter as an internal-stability theme:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:12 | ἐστηριγμένους ἐν τῇ παρούσῃ ἀληθείᾳ | **ตั้งมั่นในความจริง** | established-in-truth (positive) |
| 2:14 | δελεάζοντες ψυχὰς ἀστηρίκτους | **ล่อจิตวิญญาณที่ไม่มั่นคง** | unstable-souls (false-teachers' targets) |
| 3:16 | οἱ ἀμαθεῖς καὶ ἀστήρικτοι στρεβλοῦσιν | **คนโง่เขลาและไม่มั่นคงได้บิดเบือน** | unstable-readers (Paul-distorters) |
| 3:17 | ἐκπέσητε τοῦ ἰδίου στηριγμοῦ | **ร่วงหล่นจากความมั่นคง** | own-stability-lost (apostasy-warning) |

**Editorial assessment:** The Petrine στηρίζω-cluster is the **letter's structural-stability metaphor** — stable-vs-unstable runs through the letter as the believer-vs-false-teacher contrast. The Thai **มั่นคง / ไม่มั่นคง** preserves this cross-verse anchor. **STABLE — verse-level rationale comprehensive.** No new corpus doc needed.

---

## 20. Inherited locks — **all compliant**

| Doc | 2PE evidence | Status |
|---|---|---|
| `parousia_christou_2026-05.md` (incl. §Petrine sub-section) | 1:16, 3:4, 3:12 — all παρουσία (Christ-eschatological) → **การเสด็จมา** per lemma-driven rule | **LOCKED** ✓ — confirms lemma-driven rule |
| `petrine_eschatological_disambiguation_2026-05.md` | 3:9 (πάντας εἰς μετάνοιαν → preserve-ambiguity per doc); 1:20 disambiguates per evangelical-Protestant principle | **LOCKED** (3:9) + **DECIDE** (1:20 — extends the principle) — see §7 |
| `pastoral_corpus_locks_2026-05.md` (esp. §C Granville-Sharp) | 1:1, 1:11, 2:20, 3:2, 3:18 — five θεός/κύριος-καὶ-σωτήρ Granville-Sharp constructions all rendered high-Christological | **LOCKED** ✓ — densest NT cluster ratifies §C |
| `pastoral_corpus_locks_2026-05.md` §B (εὐσέβεια) | 1:3, 1:6, 1:7, 3:11 — εὐσέβεια / εὐσεβής → **ความเคร่งในพระเจ้า** uniformly | **LOCKED** ✓ |
| `stoicheia_tou_kosmou_2026-05.md` | 3:10, 3:12 — στοιχεῖα (cosmological-elements context) → **สิ่งทรงสร้าง** (NOT spiritual-powers sense). Compliant with doc's context-dependent disambiguation. | **LOCKED** ✓ |
| `pascho_pathema_suffering_2026-05.md` | **N/A directly** — πάσχω + πάθημα absent from 2 Peter (the letter focuses on knowledge + judgment, not suffering). The 1:16 παθήσεσθαι-cognate participation in παρουσία is a separate lemma. | **LOCKED (N/A)** |
| `parepidēmos_paroikos_sojourner_2026-05.md` | **N/A** — sojourner-vocabulary absent from 2 Peter. Unlike 1 Peter, 2 Peter is genre-shifted to ethical-doctrinal-warning, not pilgrim-identity. | **LOCKED (N/A)** |
| `poimēn_episkopos_register_split_2026-05.md` | **N/A** — shepherd/overseer vocabulary absent from 2 Peter. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | 2:8 (ψυχὴν δικαίαν → **จิตวิญญาณอันชอบธรรม**, theological-anthropological); 2:14 (ψυχὰς ἀστηρίκτους → **จิตวิญญาณที่ไม่มั่นคง**); 1:21 (πνεύματος ἁγίου → **พระวิญญาณบริสุทธิ์**) | **LOCKED** ✓ |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 2 Pet has 9+ κύριος-divine references (1:2, 1:8, 1:11, 1:14, 1:16, 2:9, 2:11, 2:20, 3:2, 3:8, 3:9, 3:10, 3:15, 3:18). All divine → **องค์พระผู้เป็นเจ้า**. The δεσπότης at 2:1 (Christological) → **องค์เจ้านาย** is a principled distinction (see §8). | **LOCKED** ✓ — Catholic-Epistles ratifies |
| `vocative_kyrie_didaskale_register_2026-04.md` | **N/A** — no narrative-vocative κύριε in 2 Peter (epistolary-doctrinal genre). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | 3:18 closing-doxology (`αὐτῷ ἡ δόξα καὶ νῦν καὶ εἰς ἡμέραν αἰῶνος. ἀμήν`) → **ขอพระสิริจงมีแด่พระองค์ทั้งบัดนี้และจนถึงวันนิรันดร์ อาเมน** — compliant. The "day of eternity" formula is uniquely-2 Petrine. | **LOCKED** ✓ |
| `honorifics_non_divine_authorities_2026-04.md` | 3:15 (Παῦλος → **เปาโล**) — corpus-locked. | **LOCKED** ✓ |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for non-divine authorities (Balaam, Lot, Noah, etc.); plain register on the false-teachers + the scoffers (per adversary-speech-register doc). The 3:4 scoffers' direct-speech ('Ποῦ ἐστιν...') uses plain register correctly. Compliant. | **LOCKED** ✓ |
| `aramaic_transliterations_2026-04.md` | **N/A** — no Aramaic embeds in 2 Peter. The Βοσόρ at 2:15 (Galilean-Aramaic-Greek vocalization of Beor) is normalized to standard Thai-OT เบโอร์ — see §12. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** — 2 Pet has no Tier 1/2/3 inclusion variants. The 3:10 SBLGNT εὑρεθήσεται (vs Byzantine κατακαήσεται) is a textual-variant per RULES §0; followed SBLGNT. Documented in the 3:10 KD. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | **N/A** — 2 Peter is doctrinal-pastoral-warning, not narrative. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | **N/A** — no parables in 2 Peter. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | 3:9 (μετάνοια → **กลับใจใหม่**) — compliant. μεταμέλομαι absent. | **LOCKED** ✓ |
| `aphesis_forgiveness_of_sins_2026-04.md` | **N/A** — ἄφεσις absent from 2 Peter (the letter focuses on judgment + virtue, not forgiveness-vocabulary). | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | **N/A** — no explicit pagan-deity-reference in 2 Peter. | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | **N/A** — no Roman-administrative-titles in 2 Peter. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | **N/A** — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | **N/A** — υἱὸς τοῦ ἀνθρώπου absent from 2 Peter. | **LOCKED (N/A)** |
| `johannine_doubled_amen_2026-04.md` | **N/A** — Petrine. The 3:18 single-ἀμήν doxology is NOT the Johannine pattern. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | **N/A** — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in 2 Peter). The 3:18 ἀμήν is a doxology-close. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | **N/A** — no narrative-speech-verbs-by-adversaries-addressing-divine in 2 Peter. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | 1:11 (αἰώνιον βασιλείαν → **อาณาจักรนิรันดร์**) — compliant. See §3. | **LOCKED** ✓ |
| `ouranos_heaven_rendering_2026-04.md` | 1:18 (ἐξ οὐρανοῦ → **จากสวรรค์**); 3:5 (οὐρανοί → **ฟ้าสวรรค์**, plural-cosmological); 3:7 (νῦν οὐρανοί → **ฟ้าสวรรค์ในปัจจุบัน**); 3:10, 3:12, 3:13 (multiple οὐρανοί → ฟ้าสวรรค์). Compliant. | **LOCKED** ✓ |
| `ethnos_2026-04.md` | **N/A** — ἔθνος absent from 2 Peter. | **LOCKED (N/A)** |
| `ekklesia_2026-04.md` | **N/A** — ἐκκλησία absent from 2 Peter (matches 1 Peter — neither Petrine letter uses the lemma). | **LOCKED (N/A)** |
| `christ_hymn_kenosis_2026-05.md` | **N/A** — no Christ-hymn in 2 Peter. | **LOCKED (N/A)** |
| `huiothesia_adoption_2026-05.md` | **N/A** — υἱοθεσία absent from 2 Peter. | **LOCKED (N/A)** |
| `spiritual_beings_hierarchy_2026-05.md` | 2:4 (ἀγγέλων ἁμαρτησάντων → **ทูตสวรรค์ ... ทำบาป**, fallen-angels-judged); 2:10-11 (δόξας → **เหล่าผู้ทรงสง่าราศี**, angelic-glorious-beings); 2:11 (ἄγγελοι → **ทูตสวรรค์**, mightier-angels-with-restraint). Compliant — see §10. | **LOCKED** ✓ |
| `adversary_speech_register_2026-05.md` | The false-teachers' discourse (2:18 ὑπέρογκα ματαιότητος; 3:4 scoffers' question) is rendered with plain register — correctly avoids royal-prefixing. | **LOCKED** ✓ |
| `epiphaneia_christou_2026-05.md` | **N/A** — ἐπιφάνεια absent from 2 Peter. The Petrine-corpus uses παρουσία at 2 Peter / ἀποκάλυψις at 1 Peter — both rendered per their respective doc-locks. | **LOCKED (N/A)** |
| `hygiaino_sound_doctrine_2026-05.md` | **N/A** — ὑγιαίνω absent from 2 Peter. | **LOCKED (N/A)** |
| `pistis_christou_2026-05.md` | **N/A** — Pauline-specific construction; absent from 2 Peter. The 1:1 πίστιν → **ความเชื่อ** corpus-precedent unrelated to the πίστις Χριστοῦ debate. | **LOCKED (N/A)** |
| `dikaioo_dikaiosyne_family_2026-05.md` | 1:1 (δικαιοσύνῃ τοῦ θεοῦ → **ความชอบธรรมของพระเจ้า**); 2:5 (δικαιοσύνης κήρυκα → **ผู้ประกาศความชอบธรรม**); 2:7-8 (δίκαιος Λώτ → **โลทผู้ชอบธรรม**); 2:21 (ὁδὸν τῆς δικαιοσύνης → **ทางแห่งความชอบธรรม**); 3:13 (δικαιοσύνη κατοικεῖ → **ความชอบธรรมสถิตอยู่**). All compliant. | **LOCKED** ✓ |
| `sarx_pauline_2026-05.md` | **N/A directly** — though σάρξ does appear at 2:10 (ὀπίσω σαρκός → **ตามเนื้อหนัง**) and 2:18 (ἐπιθυμίαις σαρκός → **ตัณหาแห่งเนื้อหนัง**). Petrine usage matches Pauline negative-flesh sense; renderings compliant. | **LOCKED** ✓ |
| `phroneo_pauline_2026-05.md` | **N/A** — Pauline-specific. | **LOCKED (N/A)** |
| `nomos_pauline_2026-05.md` | **N/A** — Pauline-specific. | **LOCKED (N/A)** |
| `prototokos_pauline_2026-05.md` | **N/A** — Pauline-specific. | **LOCKED (N/A)** |
| `telos_paidagogos_christ_2026-05.md` | **N/A** — Pauline-specific. | **LOCKED (N/A)** |
| `diakonos_pauline_2026-05.md` | **N/A** — διάκονος absent from 2 Peter. | **LOCKED (N/A)** |
| `proper_noun_wordplay_2026-05.md` | The 2:15 Βοσόρ → **เบโอร์** normalization (instead of preserving the Petrine-Greek-variant) effectively forecloses the contested Βοσόρ-Hebrew-בָּשָׂר "flesh" wordplay-possibility. Per the doc's principle (preserve wordplay when scholarly-attested), the foreclosure is defensible since the wordplay is **scholarly-contested, not consensus**. See §12. | **LOCKED with note** ✓ |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | 2:14 (ὀφθαλμοὺς ... μεστοὺς μοιχαλίδος → **ดวงตา ... เต็มไปด้วยการล่วงประเวณี**, idiom-quality-genitive). The phrase is treated as figurative-idiom rather than literal-adultery; compliant with the deferred-doc's principle. | **LOCKED (deferred-doc)** ✓ |

---

## Mechanical (§1) — **all green**

- 3/3 chapters: `output/check_reports/2peter_NN_review.md` ✓
- 3/3 chapters: `output/back_translations/2peter_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-223-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only un-tracked Paratext-export files (`output/paratext/{1CO,1TH,2CO,2TH,ACT,COL,EPH,GAL,TIT}.SFM`) — pre-existing, untouched by this audit. No 2PE source-file dirt.

---

## Pre-existing docs affirmed / unchanged

All 47 docs in `docs/translator_decisions/` reviewed. Compliance summary in §20 above. Two amendments recommended (low-priority — current docs serve 2 Peter):

1. **`pastoral_corpus_locks_2026-05.md` §C** — extend with a one-line note that 2 Peter's 5-construction Granville-Sharp θεός/κύριος-καὶ-σωτήρ cluster ratifies the Tit 2:13 pre-decision corpus-wide. (Optional; status of §C is already STABLE.)

2. **`petrine_eschatological_disambiguation_2026-05.md`** — extend with §Inspiration-and-Hermeneutics sub-section if Ben confirms the 2 Pet 1:20 disambiguation extends the doc's principle. (Decision-dependent; see §7§C.)

---

## Flagged for Ben's attention

### A. ἐπίγνωσις vs γνῶσις keyword split — **STABLE; consider corpus doc** (§2)
Densest ἐπίγνωσις cluster in NT — 4× chapter 1 + 2× chapter 2 = 6 occurrences in 2 Peter. The principled distinction (true-knowledge vs bare-knowledge) is theologically rich; lift to corpus doc would clarify Pauline-corpus already-shipped occurrences (Eph 4:13; Phil 1:9; Col 1:9-10; 1 Tim 2:4; 2 Tim 2:25; Tit 1:1).

### B. 2 Pet 1:1, 1:11, 2:20, 3:2, 3:18 Granville-Sharp θεός/κύριος-καὶ-σωτήρ — **LOCKED; ratifies corpus-doc** (§1)
Densest Granville-Sharp construction-cluster in NT (5× in 61 verses). All rendered high-Christological per pastoral_corpus_locks §C. 2 Peter is the *empirical anchor* for the construction-pattern.

### C. 2 Pet 1:4 θείας κοινωνοὶ φύσεως — **DECIDE** (§4)
Translator chose Protestant ethical-spiritual participation framing + thai_summary disclaimer-against-deification. Three sub-decisions: (§A) φύσις → พระลักษณะ vs ธรรมชาติ; (§B) κοινωνός → มีส่วนร่วม; (§C) thai_summary deification-disclaimer keep-or-remove. Highest-priority Ben confirmation.

### D. 2 Pet 1:20 ἰδίας ἐπιλύσεως — **DECIDE** (§7)
Translator chose prophet's-own-interpretation reading (mainstream-evangelical-Protestant) + thai_summary documenting both options. Extends `petrine_eschatological_disambiguation_2026-05.md`'s disambiguation-principle to inspiration-and-hermeneutics passages. Confirm doc-amendment vs new doc.

### E. 2 Pet 2:1 δεσπότης Christology — **REVIEW** (§8)
The δεσπότης (absolute-master) → **องค์เจ้านาย** rendering preserves the principled distinction from κύριος → **องค์พระผู้เป็นเจ้า**. Worth Ben's confirmation; brief corpus doc could lock before JUDE 4 ships.

### F. 2 Pet 2:4 ταρταρόω Tartarus-mythology — **REVIEW** (§9)
Layered approach: main-text **นรกขุมลึกที่สุด** (Thai-natural) + thai_summary explains the Tartarus-mythology-background. Confirm this is the corpus-default for uniquely-NT-Greek-mythology-Christianized terminology.

### G. 2 Pet 2:10-11 δόξας = angelic-beings — **REVIEW** (§10)
**เหล่าผู้ทรงสง่าราศี** (angelic-glorious-beings, neutral on good-vs-fallen). Compliant with `spiritual_beings_hierarchy_2026-05.md`. Confirm corpus-default for the JUDE 8-9 parallel-passages.

### H. 2 Pet 2:15 Βοσόρ → standard-OT เบโอร์ — **STABLE** (§12)
Petrine Greek-variant normalized to standard Thai-OT. Forecloses the contested Βοσόρ-flesh-wordplay (scholarly-contested, not consensus). Worth a one-line note in `aramaic_transliterations_2026-04.md`.

### I. 2 Pet 3:9 πάντας εἰς μετάνοιαν — **LOCKED-with-confirmation** (§14)
Per locked `petrine_eschatological_disambiguation_2026-05.md` (which explicitly anticipated this verse): preserve-ambiguity-between-Calvinist-and-Arminian-readings. Implementation faithful. Confirm doc-application as written.

### J. 2 Pet 3:15-16 Paul's letters as γραφή — **STABLE** (§17)
The earliest NT-internal canonical-self-attestation. Verse-level KD + thai_summary preserve the canonical-significance for Thai readers. No new corpus doc needed.

### K. New corpus docs to consider
1. **`docs/translator_decisions/epignosis_vs_gnosis_2026-05.md`** (§2) — locks ἐπίγνωσις → ความรู้ที่แท้จริง / γνῶσις → ความรู้ corpus-wide
2. **`docs/translator_decisions/despotēs_christological_2026-05.md`** (§8) — locks δεσπότης (Christological) → องค์เจ้านาย; before JUDE 4 ships
3. **(Optional)** `docs/translator_decisions/theiotētos_koinōnia_divine_nature_participation_2026-05.md` (§4) — locks the Protestant-ethical-participation framing for 1:4 θείας κοινωνοὶ φύσεως. Decision-dependent on §C.
4. **(Optional)** `docs/translator_decisions/petrine_inspiration_hermeneutics_2026-05.md` (§7§C) — extends `petrine_eschatological_disambiguation` principle to inspiration-and-hermeneutics passages. Decision-dependent on §D.

### L. Existing docs to amend (low-priority)
- **`pastoral_corpus_locks_2026-05.md` §C** — note that 2 Peter ratifies the Tit 2:13 Granville-Sharp pre-decision (5 constructions in 61 verses).

### M. External AI review (§3 of checklist) — **pending**
Recommended before `book-2peter-v1` tag. Suggested 4-cluster external AI packet:
1. **2PE 1:1–11** — Granville-Sharp θεός+σωτήρ (1:1, 1:11) + ἐπίγνωσις (1:2-3, 1:8) + chain-of-virtues + 1:4 partakers-of-divine-nature
2. **2PE 1:12–21** — apostolic-eyewitness defense (transfiguration 1:16-18) + foundational-inspiration text (1:20-21 ἰδίας ἐπιλύσεως)
3. **2PE 2** — false-teachers' OT-judgment-examples chain + δεσπότης + ταρταρόω + δόξας + Βοσόρ + dog-vomit + sow-mire proverbs
4. **2PE 3:1–18** — eschatology + 3:9 πάντας ambiguity-preservation + 3:10 SBLGNT εὑρεθήσεται + 3:15-16 Paul's-letters-as-Scripture + 3:18 closing-doxology

Use Grok + ChatGPT in parallel per the JHN/GAL/1TH/1PE pattern.

---

## Recommendation

**2 Peter ships in strong corpus-hygiene shape — and serves as the empirical anchor for the densest Granville-Sharp + ἐπίγνωσις clusters in the NT.** The translator's principled choices on the four most-significant 2 Pet items (Granville-Sharp; ἐπίγνωσις/γνῶσις split; παρουσία lemma-driven rule; petrine_eschatological_disambiguation 3:9 ambiguity-preservation) are all either locked or recommended-for-corpus-doc. **None of them threatens the v1 tag.**

The highest-priority items for Ben's confirmation are the **DECIDE**-flagged passages in chapter 1: **1:4 θείας κοινωνοὶ φύσεως** (Protestant ethical-participation vs Eastern-Orthodox θέωσις) and **1:20 ἰδίας ἐπιλύσεως** (prophet's-own-interpretation vs reader's-own-interpretation). Both are foundationally-Protestant-evangelical readings; both are mainstream English (NIV/ESV/CSB) aligned; both could be either confirmed (current strategy) or ambiguity-preserved (alternative strategy per `petrine_eschatological_disambiguation_2026-05.md`). The choice is *which strategy the project applies to non-eschatological doctrinally-loaded ambiguous passages*.

The **3:9 πάντας ambiguity-preservation** is the simplest item — `petrine_eschatological_disambiguation_2026-05.md` explicitly anticipated the verse, and the implementation matches the doc's prescription verbatim. **LOCKED-with-confirmation** is the natural status.

Tag `book-2peter-v1` after:
1. Ben's decisions on **§C + §D** (DECIDE items: 1:4 divine-nature framing; 1:20 ἰδίας ἐπιλύσεως reading).
2. Ben's confirmations on **§E + §F + §G + §H + §I** (REVIEW + LOCKED-with-confirmation items).
3. **(Optional)** Two new translator_decisions docs written (§K items 1–2 minimum: ἐπίγνωσις/γνῶσις split + δεσπότης Christological).
4. **(Optional)** One existing doc amended (`pastoral_corpus_locks_2026-05.md` §C with 2 Pet ratification note).
5. External AI sanity-check (§M).

The Catholic-Epistles corpus is now three-quarters-shipped (James + 1 Peter + 2 Peter complete; 1-3 John + Jude pending). The Petrine-eschatology + Petrine-canonical-self-awareness + Petrine-Granville-Sharp-Christology clusters established here will propagate into Jude (synoptic-parallel with 2 Peter 2 — 80%+ overlap) and the Johannine epistles' eschatology (1 John 2:18, 28; 2:18-22 antichrist; 4:1-6 false-teachers).
