# 1 John — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **1 John** (5 chapters, 105 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged. 1 John 5/5 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — ἀντίχριστος = ผู้ต่อต้านพระคริสต์: Johannine-corpus locking precedent

**The pattern:** ἀντίχριστος is **only-NT in 1+2 John** (1JN 2:18 ×2, 2:22, 4:3; 2JN 7). 1 John is the corpus-entry-point. All four 1JN occurrences render **ผู้ต่อต้านพระคริสต์** ("the-against-Christ"):

| Verse | Greek | Thai | Number |
|---|---|---|---|
| 1JN 2:18a | καθὼς ἠκούσατε ὅτι ἀντίχριστος ἔρχεται | **ผู้ต่อต้านพระคริสต์กำลังจะมา** | sing. (eschatological-future) |
| 1JN 2:18b | καὶ νῦν ἀντίχριστοι πολλοὶ γεγόνασιν | **ผู้ต่อต้านพระคริสต์มากมายเกิดขึ้นแล้ว** | pl. (current-many) |
| 1JN 2:22 | οὗτός ἐστιν ὁ ἀντίχριστος | **ผู้นั้นแหละเป็นผู้ต่อต้านพระคริสต์** | sing.-definitional |
| 1JN 4:3 | τοῦτό ἐστιν τὸ τοῦ ἀντιχρίστου | **วิญญาณของผู้ต่อต้านพระคริสต์** | gen. (the-spirit-of-anti-Christ) |

**The interpretive crux** — the singular-future-vs-plural-present ambiguity:

The 2:18 thai_summary documents both options:
> ในข้อ 18 คำนี้ใช้ในรูปพหูพจน์ — บ่งชี้ว่าในยุคของยอห์นมีคนหลายคนที่ต่อต้านพระคริสต์ ... นักวิชาการบางคนเข้าใจว่าหมายถึงผู้ต่อต้านพระคริสต์คนเดียวที่จะมาในยุคสุดท้าย (เช่น 2 เธสะโลนิกา 2:1-12 'ผู้ที่ไร้กฎหมาย') ส่วนคนอื่นมองว่าหมายถึงปฏิญาณการต่อต้านพระคริสต์ทุกประเภท — ทั้งสองมุมมองเข้ากันได้

Per `petrine_eschatological_disambiguation_2026-05.md`: preserve-ambiguity (both readings exegetically defensible).

**The CHALLENGE forward — 2 JN 7 + Revelation 13** Johannine ψευδόχριστος / ὁ ἄνομος cross-corpus:

The translator must lock ἀντίχριστος → **ผู้ต่อต้านพระคริสต์** distinctly from:
- ψευδόχριστος (Matt 24:24 + Mark 13:22) → **พระคริสต์เทียมเท็จ** ("false-Christ")
- ὁ ἄνομος / ὁ ἄνθρωπος τῆς ἀνομίας (2 Thess 2:3, 8) → **ผู้ที่ไร้กฎหมาย**
- The Revelation 13 "beast" complex (no ἀντίχριστος lemma)

**Two questions:**
1. Is **ผู้ต่อต้านพระคริสต์** the right Johannine-corpus default for ἀντίχριστος? It preserves the deliberate ἀντί- "against-and-instead-of" force AND avoids importing the dispensationalist English "Antichrist" framing as a name. The alternative would be transliterated **อันติคริสต์** (used in some popular Thai Christian materials but reads as a foreign-loanword, not a descriptive title).
2. Should the 2:18 thai_summary's framing be revised? It currently names "นักวิชาการบางคน ... ส่วนคนอื่น ..." (some-scholars ... others ...) — already neutral descriptive language. Worth confirming this neutrality holds for the corpus going forward (vs the 2:2 / 5:16 thai_summaries which name "ลัทธิ Calvinism / Arminianism" + "การละทิ้งความเชื่อ").

---

## Item B — ἱλασμός = เครื่องบูชาไถ่บาป: cognate-locking with ἱλαστήριον (ROM 3:25)

**The pattern:** ἱλασμός is **only-NT in 1 John 2:2 + 4:10**. The translator chose to render it identically to its cognate ἱλαστήριον at Rom 3:25:

| Verse | Greek | Thai |
|---|---|---|
| 1JN 2:2 | καὶ αὐτὸς ἱλασμός ἐστιν περὶ τῶν ἁμαρτιῶν ἡμῶν | **และพระองค์เองทรงเป็นเครื่องบูชาไถ่บาปของเราทั้งหลาย** |
| 1JN 4:10 | ἀπέστειλεν τὸν υἱὸν αὐτοῦ ἱλασμὸν περὶ τῶν ἁμαρτιῶν ἡμῶν | **ทรงใช้พระบุตรของพระองค์มาเป็นเครื่องบูชาไถ่บาปของเรา** |
| ROM 3:25 (locking precedent) | ὃν προέθετο ὁ θεὸς ἱλαστήριον διὰ τῆς πίστεως | **เครื่องบูชาไถ่บาป** (cognate-noun, same Thai) |

The 2:2 KD names the rationale:

> ἱλασμός → เครื่องบูชาไถ่บาป — same Thai as ἱλαστήριον at ROM 3:25 (corpus-precedent; cognate-noun in the same Levitical-atonement word-family). Per RULES §0 evangelical-Protestant default: propitiation + expiation + mercy-seat composite-sense preserved.

**The semantic-coverage question:** **เครื่องบูชาไถ่บาป** literally means "atonement-sacrifice / sin-redemption-instrument" — it preserves both the propitiation-sense (toward divine wrath) AND the expiation-sense (cleansing-from-sin) WITHOUT collapsing to one. The rendering is compatible with both substitutionary-atonement (Reformed) and Christus-Victor / participatory frameworks. English translations split here — ESV "propitiation" vs NIV "atoning sacrifice" vs CSB "atoning sacrifice" — the Thai matches the NIV/CSB neutral position.

**The CHALLENGE forward — Heb 9:5 ἱλαστήριον (mercy-seat) + Heb 2:17 ἱλάσκομαι (verbal):**

If **เครื่องบูชาไถ่บาป** locks for both ἱλασμός AND ἱλαστήριον, Heb 9:5 (the Levitical-tabernacle "mercy seat" itself, a physical-object) might need register-distinction (the throne-of-mercy at Heb 9:5 vs the Christ-as-atonement at Rom 3:25 + 1 JN 2:2 / 4:10).

**Two questions:**
1. Is **เครื่องบูชาไถ่บาป** the right cognate-locking rendering for ἱλασμός + ἱλαστήριον? It preserves the Levitical-cognate-thread across Pauline + Johannine + Hebrews corpora at the cost of slightly-less-naturalistic Thai (5 syllables; the alternative **การไถ่บาป** = "the redemption-of-sin" is 4 syllables but loses the sacrificial-instrument concrete force).
2. For Heb 9:5 (the Tabernacle's gold-covered ἱλαστήριον as a physical object on the Ark of the Covenant), should the rendering shift to a register-appropriate object-noun (e.g., **พระที่นั่งกรุณา** "the mercy-seat-throne") OR maintain the cognate-lock (**เครื่องบูชาไถ่บาป**) for word-family consistency? Different mainstream English translations also split here.

---

## Item C — ἱλασμός EXTENT at 2:2: Calvinist-Arminian crux preserve-ambiguity strategy

**The textual question:** 1 JN 2:2 is the canonical-evangelical-Protestant Calvinist-Arminian extent-of-the-atonement cleavage point:

> 1JN 2:2 GK: `καὶ αὐτὸς ἱλασμός ἐστιν περὶ τῶν ἁμαρτιῶν ἡμῶν, οὐ περὶ τῶν ἡμετέρων δὲ μόνον ἀλλὰ καὶ **περὶ ὅλου τοῦ κόσμου**`
> Thai: `และพระองค์เองทรงเป็นเครื่องบูชาไถ่บาปของเราทั้งหลาย และไม่เพียงเฉพาะของเราเท่านั้น แต่เป็นเครื่องบูชาไถ่บาปของ**คนทั้งโลก**ด้วย`

**The translator's strategy** — preserve-ambiguity per `petrine_eschatological_disambiguation_2026-05.md`:

Main text: literal **คนทั้งโลก** ("the whole-world / all-people-of-the-world") — readable for both Calvinist and Arminian readers.

thai_summary (current):
> ข้อนี้สามารถตีความได้ 2 แบบเกี่ยวกับขอบเขตของการไถ่บาป — (1) **ลัทธิ Calvinism** มองว่า 'คนทั้งโลก' หมายถึงผู้ที่ทรงเลือกสรรไว้จากทุกชนชาติ ... (2) **ลัทธิ Arminianism** มองว่า 'คนทั้งโลก' หมายถึงทุกคนทั่วโลกที่พระคริสต์ทรงไถ่บาปสำหรับทุกคน ...

**The framing concern** — same as 2 PET 3:9:

The 2 PET audit (2026-05-03) found that both Gemini + ChatGPT flagged the "ลัทธิ Calvinism / Arminianism" framing for tone-revision toward neutral descriptive language ("some interpret as the elect; others as all people"). The 1 JN 2:2 thai_summary uses identical-pattern framing.

**Two questions:**
1. Is **คนทั้งโลก** the right preserve-ambiguity main-text rendering? It is literal + both Calvinist and Arminian readers can affirm it. Alternative: more-explicit disambiguation (e.g., **"คนของคนทั้งโลก"** = "people-of-all-nations" — Calvinist-leaning) OR **"ทุกคนในโลก"** = "every-person-in-the-world" — Arminian-leaning) would foreclose one reading. Should the literal-ambiguity be confirmed as the corpus-default for atonement-extent passages?
2. Should the thai_summary be revised to drop the "ลัทธิ Calvinism / Arminianism" labels and adopt the same neutral framing the 2 PET audit recommended (e.g., "บางคนตีความว่า ... ส่วนคนอื่นตีความว่า ...")? This would remove polemical framing while preserving the substance of the interpretive options.

---

## Item D — μένω = คงอยู่: the Johannine-keyword "abide / remain"

**The pattern:** μένω is the Johannine signature verb par excellence — **24 occurrences in 1 John** (more than any lemma except ἀγάπη). All 24 render **คงอยู่**. The keyword bears the entire weight of the Johannine mutual-indwelling theology.

**Cleanest evidence — the 1 JN 4:13-16 triple-μένω structure:**

| Verse | Greek | Thai |
|---|---|---|
| 4:13 | ὅτι ἐν τῷ θεῷ μένει καὶ ὁ θεὸς ἐν αὐτῷ μένει | **เราคงอยู่ในพระองค์ และพระองค์คงอยู่ในเรา** |
| 4:15 | ὁ θεὸς ἐν αὐτῷ μένει καὶ αὐτὸς ἐν τῷ θεῷ | **พระเจ้าก็คงอยู่ในผู้นั้น และผู้นั้นก็คงอยู่ในพระเจ้า** |
| 4:16 | ὁ μένων ἐν τῇ ἀγάπῃ ἐν τῷ θεῷ μένει καὶ ὁ θεὸς ἐν αὐτῷ μένει | **ผู้ใดที่คงอยู่ในความรักก็คงอยู่ในพระเจ้า และพระเจ้าก็คงอยู่ในผู้นั้น** |

**The antithetical-extension at 3:14:** the same lemma covers the *opposite* state — **ผู้ที่ไม่รักก็คงอยู่ในความตาย** ("the one who does not love remains in death") — preserving the lexical-thread across both indwelling-life AND remaining-in-death.

**The CHALLENGE forward — 2 JN + 3 JN + Revelation:**

2 JN 9 has **πᾶς ὁ προάγων καὶ μὴ μένων ἐν τῇ διδαχῇ τοῦ Χριστοῦ** ("everyone who runs ahead and does not abide in the teaching of Christ") — same lemma, different referent (the doctrine, not God). 3 JN has μένω at 9 ("Diotrephes"). Revelation has 22+ μένω occurrences (e.g., Rev 17:10 the kings "remaining a little while").

**Two questions:**
1. Is **คงอยู่** the right uniform Johannine-keyword default for μένω? It preserves the theological-vocabulary thread that English collapses into "abide / remain / continue / dwell" depending on context. Should this be lifted to a corpus doc before 2 JN + 3 JN ship?
2. The future-extensions to Revelation may need register-distinction for non-theological-context occurrences (kings remaining; persons staying-in-place). Should the doc anticipate these or remain narrow to the Johannine-mutual-indwelling sense?

---

## Item E — γεγεννημένος ἐκ τοῦ θεοῦ vs γεννηθείς ἐκ τοῦ θεοῦ: the brilliant 5:18 perfect-vs-aorist distinction

**The textual question:** 1 JN 5:18 contains **two participles of γεννάω + ἐκ τοῦ θεοῦ within a single verse** — distinguishing the believer (perfect-passive participle) from Christ (aorist-passive participle):

> 1JN 5:18 GK: `οἴδαμεν ὅτι πᾶς **ὁ γεγεννημένος ἐκ τοῦ θεοῦ** οὐχ ἁμαρτάνει, ἀλλ' **ὁ γεννηθεὶς ἐκ τοῦ θεοῦ** τηρεῖ αὐτόν, καὶ ὁ πονηρὸς οὐχ ἅπτεται αὐτοῦ.`
> TH: `เรารู้ว่า**ทุกคนที่ได้บังเกิดจากพระเจ้า**ก็ไม่ได้ทำบาปต่อไป แต่**ผู้ที่ทรงบังเกิดจากพระเจ้า**ก็ทรงปกป้องเขาไว้ และมารร้ายก็แตะต้องเขาไม่ได้`

**The translator's brilliant Thai-grammatical solution:**

| Greek participle | Tense | Referent | Thai | Register |
|---|---|---|---|---|
| ὁ γεγεννημένος | perfect-pass. | the believer (permanent-result-of-having-been-born-of-God) | **ทุกคนที่ได้บังเกิดจากพระเจ้า** | plain |
| ὁ γεννηθείς | aorist-pass. | Christ (uniquely-born / divinely-begotten) | **ผู้ที่ทรงบังเกิดจากพระเจ้า** | royal-prefix ทรง- |

The 5:18 KD names the principle:
> Per uW: NB Greek-tense distinction — 'ὁ γεγεννημένος' (perfect-participle = the believer-with-permanent-result-of-having-been-born-of-God) vs 'ὁ γεννηθείς' (aorist-participle = the Christ-uniquely-born / the Begotten-One). Render preserves the distinction by using ทรง- (royal-prefix) ONLY for the second participle (Christ-as-divine-keeper-of-believer).

This is a Thai-grammatical solution to a Greek-tense-distinction that English typically loses (most English translations render both "born of God" identically; e.g., NIV does not distinguish; ESV footnotes the distinction).

**The CHALLENGE forward — JHN 1:13 + Revelation 12:5:**

JHN 1:13 has ἐκ θεοῦ ἐγεννήθησαν (aorist-passive plural for believers — "they were born of God"). Revelation 12:5 has ἔτεκεν υἱὸν ἄρρενα (different lemma τίκτω, but the begotten-Christ context).

**Two questions:**
1. Is the **royal-prefix-only-on-aorist-participle-for-Christ** rendering at 5:18 the right Johannine-corpus default? It is one of the most editorially-distinctive moves in the entire 1 JN translation — preserving a Greek-Aktionsart distinction via Thai-register. Should this be lifted to a corpus doc before 2 JN + 3 JN + Revelation?
2. The cognate JHN 1:14 μονογενής → **องค์เดียว** is a SEPARATE-but-related Christological-uniqueness rendering. Should the new doc tie γεννηθείς ἐκ θεοῦ → **ทรงบังเกิดจากพระเจ้า** + μονογενής → **องค์เดียว** + γεγεννημένος ἐκ θεοῦ → **ได้บังเกิดจากพระเจ้า** (plain) into a unified three-form doc?

---

## Item F — ἁμαρτία πρὸς θάνατον at 5:16: "sin unto death" 3-way ambiguity

**The textual question:** 1 JN 5:16 introduces the most-contested pastoral-ethical passage in the Johannine corpus — the "sin unto death" mentioned-but-not-defined:

> 1JN 5:16 GK: `... καὶ δώσει αὐτῷ ζωήν, τοῖς ἁμαρτάνουσιν μὴ πρὸς θάνατον. **ἔστιν ἁμαρτία πρὸς θάνατον**· οὐ περὶ ἐκείνης λέγω ἵνα ἐρωτήσῃ.`
> TH: `... และพระองค์จะทรงประทานชีวิตให้แก่ผู้ที่ทำบาปไม่ถึงตาย **มีบาปที่ถึงตาย** ข้าพเจ้าไม่ได้กล่าวว่าให้ทูลขอเกี่ยวกับบาปนั้น`

**The 3-way ambiguity preserved in thai_summary:**
> 'บาปที่ถึงตาย' มีการตีความหลายแบบ — (1) การละทิ้งความเชื่ออย่างถาวร (apostasy) เช่น ฮีบรู 6:4-6; 10:26-27 (2) การปฏิเสธพระเยซูคริสต์อย่างต่อเนื่อง — บาปต่อพระวิญญาณบริสุทธิ์ (มัทธิว 12:31) (3) บาปที่ทำให้ผู้กระทำสูญเสียชีวิตทางกายในการลงโทษของพระเจ้า (เช่น 1 โครินธ์ 11:30 ของอานันยาและสัปฟีรา กิจการ 5:1-11)

The 5:16 KD invokes `petrine_eschatological_disambiguation_2026-05.md`:
> Per petrine_eschatological_disambiguation_2026-05.md: PRESERVE-AMBIGUITY (multiple readings exegetically defensible).

**The translator's strategy:** Literal **บาปที่ถึงตาย** ("sin that-leads-to-death") in the main text — readable for all 3 interpretations. thai_summary documents all 3.

**The pastoral concern:** A Thai pastor preparing a sermon on 5:16 will need to commit to one reading. The current ambiguity-preservation explicitly DOES NOT help them choose; it only surfaces the options.

**Two questions:**
1. Is the **3-way ambiguity-preservation** strategy correct for ἁμαρτία πρὸς θάνατον? Or should the translator commit to one mainstream reading (most-evangelical-Protestant default = (1) apostasy, supported by Heb 6:4-6 + Heb 10:26-27 cross-references)? The Greek text genuinely under-determines the referent — but Thai readers may benefit from a more-actionable interpretation in the main text.
2. Should this 5:16 case be added as another anchor passage to the locked `petrine_eschatological_disambiguation_2026-05.md` doc (extending its scope from eschatology to broader-doctrinal-ambiguity)? Or written as a separate doc focused on Johannine pastoral-doctrinal ambiguities?

---

## Item G — οὗτός ἐστιν ὁ ἀληθινὸς θεὸς at 5:20: high-Christology commitment

**The textual question:** 1 JN 5:20 closes the entire epistle with a Christological-confession that has been variously read since the Patristic era:

> 1JN 5:20 GK: `οἴδαμεν δὲ ὅτι ὁ υἱὸς τοῦ θεοῦ ἥκει, καὶ δέδωκεν ἡμῖν διάνοιαν ἵνα γινώσκωμεν τὸν ἀληθινόν· καὶ ἐσμὲν ἐν τῷ ἀληθινῷ, ἐν τῷ υἱῷ αὐτοῦ Ἰησοῦ Χριστῷ. **οὗτός ἐστιν ὁ ἀληθινὸς θεὸς καὶ ζωὴ αἰώνιος**.`
> TH: `... คือในพระเยซูคริสต์พระบุตรของพระองค์ **ผู้นี้แหละเป็นพระเจ้าเที่ยงแท้และเป็นชีวิตนิรันดร์**`

**Two readings:**
- (a) **οὗτος = Jesus Christ** (immediate-antecedent grammar): "**Jesus** is the true God and eternal life." High-Christology reading; mainstream-evangelical-Protestant + scholarly-consensus (NIV, ESV, CSB, NASB, RSV/NRSV all read this).
- (b) **οὗτος = the Father** (broader-context): "**The Father** is the true God and eternal life" (the True-One earlier in the verse). Older-traditional + Patristic-divided reading; minority-modern.

The 5:20 KD explicitly commits to (a):
> Per pastoral_corpus_locks §C high-Christology + scholarly-consensus (NIV, ESV, CSB): οὗτος refers to-the-immediate-antecedent = Jesus Christ (Jesus = true-God + eternal-life).

The thai_summary explains both options:
> คำว่า 'ผู้นี้' ในประโยคสุดท้ายมีการตีความ 2 แบบ — (1) หมายถึงพระเยซูคริสต์ (สรรพนามใกล้ที่สุด) — เป็นการยืนยันความเป็นพระเจ้าของพระเยซูอย่างชัดเจน เปรียบเทียบกับ ยอห์น 1:1; 20:28 (2) หมายถึงพระบิดา (ตามบริบทกว้างของจดหมาย) นักวิชาการส่วนใหญ่และผู้แปลพระคัมภีร์อังกฤษสมัยใหม่ (NIV, ESV, CSB) เลือกการตีความที่ 1 ตามหลักไวยากรณ์กรีก (สรรพนามใกล้ที่สุด)

**The CHALLENGE — corpus-internal-consistency:** The choice of high-Christology here creates a **climactic-Christological-confession** at the end of 1 JN that ties cleanly to JHN 1:1 (the Word was God) + JHN 20:28 (Thomas's "my Lord and my God"). Reading (b) would leave the entire 5-chapter Johannine-letter without an explicit closing Christological-confession.

**Two questions:**
1. Is the **high-Christology commitment** (Jesus = the true God + eternal life) the right Johannine-corpus default at 5:20? It is mainstream-evangelical-Protestant + scholarly-consensus + grammatically-natural (immediate-antecedent), but it commits more-explicitly than the literal-Greek-reader would receive (where οὗτος is technically ambiguous between two preceding masculine-singular antecedents). Should the rendering preserve more ambiguity (e.g., **ผู้นั้นเป็นพระเจ้าเที่ยงแท้** with disambiguating distance from the Christ-anaphora)?
2. Should `pastoral_corpus_locks_2026-05.md` §C be amended to add 1 JN 5:20 as a Johannine-corpus confirming-precedent (extending its scope from Pastorals to Johannine), OR written as a brief new doc `houtos_ho_alethinos_theos_johannine_2026-05.md` focused on this specific passage?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
