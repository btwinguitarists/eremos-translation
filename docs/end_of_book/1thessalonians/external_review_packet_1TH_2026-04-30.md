# 1 Thessalonians — External AI Sanity-Check Review Packet
**Date assembled: 2026-04-30**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **1 Thessalonians** (5 chapters, 89 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** Mark, Matthew complete + tagged; Luke, John, Acts, Galatians complete (not yet tagged). 1 Thessalonians 5/5 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

### Already-locked corpus decisions — DO NOT re-litigate

- ἐκκλησία (Christian community) → คริสตจักร; secular/OT assembly → ที่ประชุม
- βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only)
- ἄφεσις ἁμαρτιῶν → การยกโทษบาป; ἄφεσις (release) at LUK 4:18 → ปลดปล่อย
- narrator-voice ὁ κύριος (= Jesus) → องค์พระผู้เป็นเจ้า (Luke-Acts signature)
- vocative Κύριε from disciples/believers → องค์พระผู้เป็นเจ้า; from outsiders → context
- παρρησιάζομαι → อย่างกล้าหาญ
- δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default)
- honorifics ราชาศัพท์ for divine subjects + kings (Herod, Agrippa); plain register for governors (Felix, Festus) + non-divine human authorities
- pagan deities → เทพ / เทพี / เทพเจ้า (NEVER พระเจ้า, reserved for the biblical God)
- μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering)
- οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after possessor); ท้องฟ้า (meteorological)
- ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์
- ὁ υἱὸς τοῦ ἀνθρώπου (Christological title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์
- Greek historic-present verbs → Thai past tense (do not preserve present morphology)
- ἀμὴν λέγω ὑμῖν (Synoptic single) → เราบอกความจริงแก่พวกท่าน(ว่า)
- ἀμὴν ἀμὴν λέγω ὑμῖν (Johannine doubled, 25× in John) → อาเมน อาเมน เราบอกแก่พวกท่านว่า — Aramaic-embed treatment
- μονογενὴς θεὸς (JHN 1:18) → พระบุตรองค์เดียวผู้ทรงเป็นพระเจ้าด้วย — exception to standard μονογενής → องค์เดียว lock for the compound
- Aramaic embeds (Talitha cumi, Ephphatha, Abba, etc.) → preserve Thai-script transliteration AND Mark's own Greek translation
- Inclusion-variant Path A (LOCKED): Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧` — matches BSB/ESV/NIV/CSB
- Parable characters representing God (fathers, kings, masters, judges) → human register, never ราชาศัพท์
- Narrator introducing adversary speech to Jesus → ทูล (preserves Jesus's divine status regardless of speaker)
- ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group, incl. Israel) / คนต่างชาติ (Gentiles, mission target)
- Roman titles: χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ
- Pagan-deity personal names → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม)

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Greek + Thai shown.

### What we are NOT asking for

- Don't propose stylistic alternatives "for variety." Consistency in key terms is a feature.
- Don't flag things from the locked-decisions list above. Those are settled.
- Don't suggest re-rendering specific verses for taste. Native Thai reviewers handle stylistic feedback.
- Don't comment on per-chapter automated-check coverage — those all pass.

### Output format

For each item below, return:

```
## [Item letter]: [Short title]
**Verdict:** FINE / CONCERN / MAJOR CONCERN
**Reasoning:** [1-3 sentences citing verses]
**Recommended action:** [specific — "lock as-is", "spot-revise verse X", "write doc Y", or "Ben to decide"]
```

Then a brief **§Z: Anything else?** section if you spot a corpus-level concern outside these items.

---
## Item A — παρουσία = การเสด็จมา: Pauline-corpus locking precedent

**The pattern:** 1 Thessalonians is the SECOND FULL Pauline epistle the project has shipped (after Galatians) and Paul's earliest extant letter (ca. AD 50–51). It contains **4 occurrences of παρουσία** — the densest distribution per chapter in the NT — establishing the Pauline rendering for Christ's eschatological return. All four use **การเสด็จมา** (the royal-divine **เสด็จ** verb-stem):

| Verse | Greek | Thai |
|---|---|---|
| 1TH 2:19 | ἔμπροσθεν τοῦ κυρίου ἡμῶν Ἰησοῦ ἐν τῇ αὐτοῦ παρουσίᾳ | **ต่อพระพักตร์พระเยซูองค์พระผู้เป็นเจ้าของเรา ในการเสด็จมาของพระองค์** |
| 1TH 3:13 | ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ μετὰ πάντων τῶν ἁγίων αὐτοῦ | **ในการเสด็จมาของพระเยซูองค์พระผู้เป็นเจ้าของเรา พร้อมกับวิสุทธิชนทุกคนของพระองค์** |
| 1TH 4:15 | εἰς τὴν παρουσίαν τοῦ κυρίου | **จนถึงการเสด็จมาขององค์พระผู้เป็นเจ้า** |
| 1TH 5:23 | ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ | **ในการเสด็จมาของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** |

**The CHALLENGE forward — 2 Thess 2:9 παρουσία τοῦ ἀνόμου:**
> 2 Thess 2:9 GK: `οὗ ἐστιν ἡ **παρουσία** κατ’ ἐνέργειαν τοῦ Σατανᾶ`

If the Thai uses **การเสด็จมา** (royal-เสด็จ) for both Christ AND the lawless one, the Pauline-rhetorical pun is preserved BUT the royal register is theologically inappropriate for the antichrist. Alternative: plain **การมาถึง** ("the arrival") for the lawless-one's parousia at 2 Thess 2:9.

**Two questions:**
1. Is **การเสด็จมา** (royal-เสด็จ) the right Pauline-corpus default for Christ's parousia? Does the royal-divine register correctly preserve the eschatological-glory weight?
2. How should the project handle 2 Thess 2:9 παρουσία τοῦ ἀνόμου — preserve the Pauline-rhetorical pun by using the same **การเสด็จมา** (theologically uncomfortable), or break the lemma-link with plain **การมาถึง** for the antichrist (preserves theological propriety but loses Paul's lexical-pivot)?

---

## Item B — ἁγιασμός / ἁγιωσύνη / ἀκαθαρσία: Pauline sanctification cluster

**The pattern:** 1 Thess 4:1–8 is the FIRST DENSE Pauline-sanctification passage in the corpus. The translator has implemented a principled lexical split that preserves the Greek-aspectual contrast (process vs state vs binary-opposite) — a contrast that English typically collapses into "sanctification" / "holiness":

| Greek | Thai | Sense | Verses |
|---|---|---|---|
| ἁγιασμός | **การชำระให้บริสุทธิ์** (process) | active-process | 4:3, 4:4, 4:7 |
| ἁγιωσύνη | **ความบริสุทธิ์** (state) | resulting-state | 3:13 |
| ἀκαθαρσία | **ความไม่บริสุทธิ์** (state) | binary-opposite | 4:7 |
| ἁγιάζω (verb, God-subject) | **ทรงชำระ ... ให้บริสุทธิ์** | divine action | 5:23 |
| ἅγιοι (substantive) | **วิสุทธิชน** | persons | 3:13 |

**Cleanest evidence — 1 Thess 4:7 binary contrast:**
- GK: `οὐ γὰρ ἐκάλεσεν ἡμᾶς ὁ θεὸς ἐπὶ **ἀκαθαρσίᾳ** ἀλλ’ ἐν **ἁγιασμῷ**`
- TH: `เพราะพระเจ้ามิได้ทรงเรียกเรามาเพื่อ**ความไม่บริสุทธิ์** แต่เพื่อ**การชำระให้บริสุทธิ์**`

The Thai SPECIFICALLY uses **ความ-** (state-noun-prefix) for ἀκαθαρσία and **การ-** (action-noun-prefix) for ἁγιασμός — a deliberate Thai morphological choice mirroring the Greek state-vs-process distinction.

**Process vs state — 3:13 vs 4:3:**
- 3:13 GK: `ἀμέμπτους ἐν **ἁγιωσύνῃ**` → TH: `ไม่มีตำหนิใน**ความบริสุทธิ์**` ([state of] holiness)
- 4:3 GK: `ὁ **ἁγιασμὸς** ὑμῶν` → TH: `**การชำระให้บริสุทธิ์**ของพวกท่าน` ([act of being] purified)

**Two questions:**
1. Is the Greek-aspectual lexical split (ἁγιασμός = **การชำระให้บริสุทธิ์** process / ἁγιωσύνη = **ความบริสุทธิ์** state) sound for a CC0 evangelical-Protestant Thai Bible? Or does it over-translate at the cost of natural Thai readability (the longer **การชำระให้บริสุทธิ์** is 5 syllables, vs THSV1971's compact **ความบริสุทธิ์** which collapses the distinction)?
2. Should this be lifted to a corpus doc before Rom 6:19, 22 + Heb 12:14 (where ἁγιασμός / ἁγιωσύνη recur in dense theological clusters)?

---

## Item C — ἁρπαγησόμεθα = ถูกรับขึ้นไป: theologically-neutral rendering of the rapture verb

**The textual question:** 1 Thess 4:17 is the most famous "rapture" verse — Latin Vulgate `rapio` (= ἁρπάζω) is the etymological source of the English term. The translator chose a **theologically-neutral, divine-passive rendering**:

- 1TH 4:17 GK: `ἔπειτα ἡμεῖς οἱ ζῶντες οἱ περιλειπόμενοι ἅμα σὺν αὐτοῖς **ἁρπαγησόμεθα** ἐν νεφέλαις εἰς ἀπάντησιν τοῦ κυρίου εἰς ἀέρα`
- TH: `หลังจากนั้น เราทั้งหลายที่ยังเป็นอยู่และเหลืออยู่ จะ**ถูกรับขึ้นไป**พร้อมกับพวกเขาในเมฆ เพื่อพบกับองค์พระผู้เป็นเจ้าในฟาκฟ้า`

The verse-level KD names the etymology while preserving theological neutrality on rapture-systems:

> ἁρπάζω future passive = 'will be snatched up.' The Latin VULGATE translates with rapio, source of English 'rapture.' The verse is foundational for various-Christian-eschatological-systems (pre-trib, mid-trib, post-trib, amillennial); the Greek text DOES NOT specify which system is correct — it specifies the EVENT but not its placement-within-eschatological-timeline.

**The accompanying 4:16 cluster — distinctive renderings:**
- κέλευσμα (NT hapax — "shout, military-command") → **เสียงคำสั่ง**
- ἀρχάγγελος ("archangel") → **หัวหน้าทูตสวรรค์** (descriptive, not transliterated)
- σάλπιγξ θεοῦ ("trumpet of God") → **เสียงแตรของพระเจ้า**
- ἀπάντησις (Hellenistic technical civic-reception term) → **พบกับ** (loses civic-formality)
- ἀέρ ("the air") → **ฟาκฟ้า** ("the firmament")

**Two questions:**
1. Is **ถูกรับขึ้นไป** ("will be received-up [divine-passive]") right for ἁρπαγησόμεθα? It is theologically-neutral and preserves the divine-passive. Alternative: **จะถูกฉวยเอาไป** ("will be snatched/grabbed up") preserves more of the literal ἁρπάζω semantic but sounds less divine-pastoral. Is the current softening defensible?
2. The 4:16 ἀπάντησις (formal civic-reception of an arriving-victorious-king who is then escorted-back-to-the-city — cf. Acts 28:15) is rendered with plain **พบกับ** ("meet"). Should it get a more technical Thai rendering like **เพื่อต้อนรับ** ("to welcome / receive in formal greeting") to preserve the civic-reception force?

---

## Item D — ἡμέρα κυρίου: OT-prophetic technical term, Pauline-corpus locking precedent

**The pattern:** 1 Thess 5:2 is the FIRST CLEAR Pauline use of the OT-prophetic technical term **יוֹם יְהוָה / ἡμέρα κυρίου**:

- 1TH 5:2 GK: `αὐτοὶ γὰρ ἀκριβῶς οἴδατε ὅτι **ἡμέρα κυρίου** ὡς κλέπτης ἐν νυκτὶ οὕτως ἔρχεται`
- TH: `เพราะพวกท่านเองทราบดีอยู่แล้วว่า **วันแห่งองค์พระผู้เป็นเจ้า**นั้นจะมาถึงเหมือนขโมยที่มาในเวลากลางคืน`

The construction **วันแห่งองค์พระผู้เป็นเจ้า** preserves both the genitive ("Day OF the Lord") and the divine-Christological force (κύριος = Christ in NT-application of the OT formula).

**Associated verses 5:4–5:**
- 5:4 GK: `ἵνα ἡ ἡμέρα ὑμᾶς ὡς κλέπτης καταλάβῃ` → TH: `เพื่อว่า**วันนั้น**จะมาถึงพวกท่าน` (anaphoric **วันนั้น**)
- 5:5 GK: `πάντες γὰρ ὑμεῖς υἱοὶ φωτός ἐστε καὶ **υἱοὶ ἡμέρας**` → TH: `เพราะพวกท่านทุกคนเป็น**บุตรแห่งความสว่าง**และ**บุตรแห่งวัน**` (preserves Hebraic "sons of X" idiom)

**The CHALLENGE forward — 2 Thess 2:2 textual variant:**
- SBLGNT: `ἡ ἡμέρα τοῦ κυρίου` ("day of the Lord")
- TR / Byz: `ἡ ἡμέρα τοῦ Χριστοῦ` ("day of Christ")

**Two questions:**
1. Is **วันแห่งองค์พระผู้เป็นเจ้า** the right Pauline-corpus default for ἡμέρα κυρίου? It preserves both the OT-prophetic technical-term force (translating יוֹם יְהוָה) and the NT-Christological-application. Alternative: a more compact **วันขององค์พระผู้เป็นเจ้า** (substituting แห่ง with ของ).
2. The related Pauline expression **ἡμέρα Χριστοῦ** (Phil 1:6, 1:10; 2:16) — should it use the same construction (**วันแห่งพระคริสต์**) to preserve Pauline parallelism, or a slightly-different register? Worth locking before 1 Cor 1:8 + Phil 1:6 ship.

---

## Item E — πνεῦμα + ψυχή + σῶμα tripartite anthropology at 1 Thess 5:23

**The textual question:** 1 Thess 5:23 is the ONLY canonical NT verse listing πνεῦμα + ψυχή + σῶμα together — the verse most-debated in tripartite-vs-dichotomous Christian anthropology:

- 1TH 5:23 GK: `Αὐτὸς δὲ ὁ θεὸς τῆς εἰρήνης ἁγιάσαι ὑμᾶς ὁλοτελεῖς, καὶ **ὁλόκληρον ὑμῶν τὸ πνεῦμα καὶ ἡ ψυχὴ καὶ τὸ σῶμα** ἀμέμπτως ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ τηρηθείη`
- TH: `ขอพระเจ้าแห่งสันติสุขเองทรงชำระพวกท่านให้บริสุทธิ์อย่างครบถ้วน และขอให้**วิญญาณ จิตใจ และร่างกาย**ของพวกท่านถูกสงวนรักษาไว้ครบถ้วนทุกส่วนอย่างไม่มีตำหนิ`

**Renderings:** πνεῦμα → **วิญญาณ**; ψυχή → **จิตใจ**; σῶμα → **ร่างกาย**

**The DEPARTURE from corpus-locked psyche/pneuma split:** The locked rule (`psyche_vs_pneuma_anthropological_2026-04.md` + `docs/CHAPTER_REVIEW_PROMPT.md`) is:
- ψυχή → **จิตวิญญาณ / ชีวิต** (context); πνεῦμα (anthropological) → **จิต**

But at 5:23, the corpus-locked **ψυχή → จิตวิญญาณ** + **πνεῦμα → จิต** would COLLAPSE in Thai (จิต and จิตวิญญาณ overlap heavily — จิตวิญญาณ literally is จิต + วิญญาณ compound). The translator therefore had to use a different tripartite Thai pairing (**วิญญาณ + จิตใจ + ร่างกาย**) to keep three lexically-distinct Thai nouns.

**Other 1TH ψυχή / πνεῦμα uses (compliant with the locked rule):**
- 2:8 ψυχή ("our [own] lives") → **ชีวิต** (locked sense)
- 5:14 ὀλιγόψυχος compound ("small-souled, faint-hearted") → **ใจฝ่อ**
- 5:19 πνεῦμα ("the Spirit" — divine, contextual) → **พระวิญญาณ** (royal-prefixed)

**Two questions:**
1. Is the 5:23 single-occurrence tripartite-listing exception (**วิญญาณ + จิตใจ + ร่างกาย**) the right call? It departs from the corpus-locked psyche/pneuma split. The alternative (using locked **จิตวิญญาณ / จิต**) would COLLAPSE the verse's distinctive 3-listing into "spirit-soul / spirit / body" which reads incoherently in Thai. Should the existing `psyche_vs_pneuma_anthropological` doc be amended with a 5:23 sub-section?
2. Looking forward to Hebrews 4:12 (`μερισμοῦ ψυχῆς καὶ πνεύματος` "division of soul and spirit") — should that verse use the same 5:23 pairing (**จิตใจและวิญญาณ**) or the locked split (**จิตวิญญาณ + จิต**)? The Heb 4:12 context is DIFFERENT (a separating action distinguishing 2 components, not a 3-listing).

---

## Item F — σκεῦος "vessel" at 1 Thess 4:4: BODY vs WIFE crux

**The textual question:** 1 Thess 4:4 — what does σκεῦος ("vessel, jar, instrument") refer to?

- 1TH 4:4 GK: `εἰδέναι ἕκαστον ὑμῶν τὸ ἑαυτοῦ **σκεῦος** κτᾶσθαι ἐν ἁγιασμῷ καὶ τιμῇ`
- TH (current — option A: BODY): `ให้ท่านแต่ละคนรู้จัก**ครอบครองร่างกายของตนเอง**ในความบริสุทธิ์และเกียรติ` ("control / possess one's own body in holiness and honor")
- Option B (WIFE): `ให้ท่านแต่ละคนรู้จัก**หาภรรยาของตนเอง**ในความบริสุทธิ์และเกียรติ` ("acquire one's own wife in holiness and honor")

**Two readings:**
- (a) **BODY** — modern majority (NIV, NLT, NRSV); supported by 2 Cor 4:7 ("treasure in earthen vessels"). Current Thai.
- (b) **WIFE** — older view (Augustine, Reformation-era commentators); supported by κτάομαι semantic ("acquire" — you don't "acquire" your own body); rabbinic-Greek κτᾶσθαι = "acquire-by-marriage."

The verse-level KD names both readings: "The verb κτάομαι = 'acquire, get for oneself' — favors (b) since you don't 'acquire' your own body. But the immediate context (sexual-ethics + the v.5 contrast with πάθει ἐπιθυμίας 'passion of lust') + the modern lexical-evidence weights toward (a)."

Modern English translations split: NIV/NLT/NRSV → body; ESV → body in main + wife in footnote; CSB → wife in main + body in footnote.

**Two questions:**
1. Is **option (a) BODY** (**ครอบครองร่างกายของตนเอง**) the right Pauline-corpus default? It is the modern-evangelical majority. The alternative (**หาภรรยาของตนเอง** "acquire one's own wife") fits κτάομαι better lexically AND would make the immediate context about anti-Greco-Roman-promiscuity-marriage-ethics rather than self-control over one's body.
2. Should the verse have a footer-note acknowledging the interpretive alternative? The English-language ESV / CSB precedent is to preserve both readings via footnote.

---

## Item G — πάντων τῶν ἁγίων αὐτοῦ at 1 Thess 3:13: ANGELS vs DEPARTED BELIEVERS

**The textual question:** 1 Thess 3:13's closing benediction — are the ἅγιοι **angels** or **departed believers**?

- 1TH 3:13 GK: `ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ μετὰ **πάντων τῶν ἁγίων αὐτοῦ**`
- TH: `ในการเสด็จมาของพระเยซูองค์พระผู้เป็นเจ้าของเรา พร้อมกับ**วิสุทธิชนทุกคนของพระองค์**`

**Three interpretations** (per the verse-level KD):
- (a) **ANGELS** (cf. Matt 25:31 "when the Son of Man comes in his glory, and all the angels with him"; 2 Thess 1:7; Jude 14 ἁγίαις μυριάσιν "with myriads of holy ones" — clearly angels). Older-traditional view.
- (b) **DEPARTED BELIEVERS** (cf. 1 Thess 4:14 "God will bring with him those who have fallen asleep in Jesus" — the "holy ones" = deceased Christians returning with Christ at the parousia). Most modern commentators.
- (c) **BOTH** (angels + saints together accompany Christ).

**Current Thai uses วิสุทธิชน** ("holy ones / saints") — the standard rendering for ἅγιοι. This **leans toward (b) DEPARTED BELIEVERS** since วิสุทธิชน in modern Thai usage strongly implies "Christian saints" rather than "angels" (which would more naturally be **ทูตสวรรค์**).

**The CHALLENGE forward — 2 Thess 1:7** uses the same μετ' ἀγγέλων / ἁγίων pattern; **Jude 14** quotes Enoch with **ἐν ἁγίαις μυριάσιν** = clearly angels.

**Two questions:**
1. Is **วิสุทธิชนทุกคน** the right rendering for τῶν ἁγίων αὐτοῦ at 3:13? It commits to interpretation (b) more than the Greek does. Alternatives: **บรรดาผู้บริสุทธิ์ของพระองค์** (more neutral "his holy ones," preserves more ambiguity); or paratactic **เหล่าทูตสวรรค์และวิสุทธิชน** (explicit (c) BOTH reading).
2. Should the Pauline ἅγιοι-with-Christ-at-parousia constructions be unified across 1 Thess 3:13, 2 Thess 1:7, 2 Thess 2:1 — and what about Jude 14 where Enoch's language is unambiguously angelic?

---

## Item H — 1 Thess 2:14–16 anti-Jewish polemic: SBLGNT-as-authentic vs interpolation question

**The textual question:** 1 Thess 2:14–16 is the most-contested passage in Pauline studies for the proposal that vv. 14–16 are a **post-AD-70 interpolation** by a later editor (the "wrath has come upon them εἰς τέλος" reading naturally as the AD-70 destruction of Jerusalem — which post-dates Paul, who died ca. AD 64–65).

- 1TH 2:14–16 GK (SBLGNT, retains as authentic): `ὑμεῖς γὰρ μιμηταὶ ἐγενήθητε, ἀδελφοί, τῶν ἐκκλησιῶν τοῦ θεοῦ τῶν οὐσῶν ἐν τῇ Ἰουδαίᾳ ἐν Χριστῷ Ἰησοῦ ... καθὼς καὶ αὐτοὶ ὑπὸ τῶν Ἰουδαίων τῶν καὶ τὸν κύριον ἀποκτεινάντων Ἰησοῦν καὶ τοὺς προφήτας καὶ ἡμᾶς ἐκδιωξάντων ... **ἔφθασεν δὲ ἐπ’ αὐτοὺς ἡ ὀργὴ εἰς τέλος**.`

**Key Thai rendering — 2:16 final clause:**
- TH: `และพระพิโรธก็ได้มาถึงพวกเขา**ในขั้นสุด**` ("and the wrath has come upon them **to the final/utmost extent**")

The verse-level KD acknowledges the interpolation-debate: "εἰς τέλος = 'to the end / to the utmost / completely / at last' (multiple readings). Modern majority: 'finally, at last.' This phrase is the basis for the proposed-post-AD-70-interpolation theory — IF read as referring to the destruction of Jerusalem (AD 70), it would post-date Paul (who died AD 64-65)."

**The 2:15 "killers of the Lord Jesus" — leadership-only reading?:**
- 2:15 TH: `ผู้ที่ได้ฆ่า**ทั้งพระเยซูองค์พระผู้เป็นเจ้าและบรรดาผู้เผยพระวจนะ**`

The Thai anchors **ผู้ที่** ("those who") to the immediately-preceding "Jews" of v.14, NOT to "the Jewish people" as a whole. The KD context is the persecutory leadership cohort that opposed the Judean churches — same kind of principled limitation as the JHN audit's οἱ Ἰουδαῖοι "leadership-only" reading. But the simpler **ชาวยิว** at v.14 doesn't carry the JHN-style **ผู้นำ** ("leaders") marker.

**Two questions:**
1. Is the SBLGNT-as-authentic stance (retaining vv. 14–16 + rendering naturally without flagging the interpolation-question) the right Pauline-corpus default? RULES §0 binds the project to SBLGNT, which retains the verses; this is the modern-evangelical-mainstream position.
2. Should the **ชาวยิว** at 2:14 be marked with a JHN-style **ผู้นำ** ("leaders") prefix to clarify the persecutory-leadership-cohort vs all-Israel question — or does the immediate context (v.14 συμφυλετῶν → Ἰουδαίων parallelism) make the leadership-cohort reading clear enough without explicit marking?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
