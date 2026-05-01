# John — End-of-Book Review

**Date:** 2026-04-30
**Scope:** All 21 chapters (878 verses; 1,934 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** JHN 21 shipped (commit `d50cea8`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **16 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 21/21 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks (incl. Johannine-doubled-amen plural form). `git status output/` shows only re-ran-check artifacts (no source-file dirt).
- **9 inherited Mark/Matthew/Luke/Acts locks verified compliant** in John (βασιλεία, οὐρανός, υἱὸς τοῦ ἀνθρώπου, πνεῦμα ἅγιον, μετανοέω-absent, parable-figures-N/A, Aramaic-transliterations, inclusion-variants Tier 3 + Tier 2, honorifics-non-divine).
- **4 cross-cutting patterns are STABLE-but-undocumented** at corpus level (οἱ Ἰουδαῖοι 4-way split; λόγος contextual rendering; Ἐγώ εἰμι absolute 4-way; παράκλητος corpus-lock declared in-place at 14:16 but no doc) — all four will compound forward (Pauline, Catholic Epistles, Revelation), so corpus-doc lift is recommended before next book.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation).
- **3 items flagged DECIDE** (JHN 3:11 amen-amen drift; JHN 7:8 textual-vs-Thai mismatch; JHN 1:34 ἐκλεκτός variant — confirm SBLGNT-against-evangelical-mainstream-evangelical-Thai expectation).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. οἱ Ἰουδαῖοι — four-way contextual split — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

64 narrator + character occurrences in John, principled four-way Thai split:

| Sense | Thai | Count | Representative |
|---|---|---|---|
| Religious-political leadership in adversarial action (Johannine signature use) | **ผู้นำชาวยิว** | 25 | 1:19; 6:41, 6:52; 7:1, 7:11, 7:13, 7:15, 7:35; 8:22, 8:48, 8:52, 8:57; 9:18, 9:22; 10:19, 10:24, 10:31, 10:33; 11:8, 11:54; 13:33 |
| Ethnic / festival / customs / believing / neutral | **ชาวยิว** | 27 | 2:6 (purification customs), 2:13 (Passover of the Jews), 3:1 (Nicodemus, "ruler of the Jews"), 4:9 (Samaritan-Jewish ethnic distinction), 4:22 ("salvation is from the Jews"), 5:1 (festival), 6:4 (festival), 7:2 (Tabernacles), 8:31 (believing Jews), 11:19/31/33/36/45 (Bethany mourners), 12:9, 12:11 (believing crowd), 18:20 (synagogue + temple-precincts), 18:33 (Pilate's question), 19:19/20/21 (titulus), 19:40, 19:42 (burial customs) |
| Passion-narrative compressed form (trial scenes, John 18–19) | **ยิว** (short) | 11 | 18:12, 18:14, 18:31, 18:36, 18:38; 19:7, 19:12, 19:14, 19:31, 19:38; 20:19 |
| **DRIFT VARIANT** — leader-marked, alternate phrase | **พวกผู้นำยิว** | 4 | 5:10, 5:15, 5:16, 5:18 (all in Bethesda-aftermath block) |

**Editorial significance:** This is the most contested editorial decision in modern English Bible translation (NIV-2011 added footnotes; NRSVue extensively renders "the Jewish authorities/leaders"). The translator's principled four-way split avoids both (a) flattening that loses Johannine semantic richness and (b) supersessionist-or-anti-Jewish framing. The choice is theologically careful and well-motivated, but it is **nowhere documented at corpus level** — only at scattered verse-level KDs (e.g., 1:19, 2:18, 5:10, 4:9). Will compound massively into Romans, 1 Thessalonians, the Catholic Epistles, and Revelation 2:9 + 3:9.

### REVIEW flag — พวกผู้นำยิว variant at 5:10–18

JHN 5:10, 5:15, 5:16, 5:18 use **พวกผู้นำยิว** instead of the dominant **ผู้นำชาวยิว**. All four verses are within one narrative block (post-Bethesda Sabbath conflict). Both are grammatical Thai for "the Jewish leaders"; ผู้นำชาวยิว is the established dominant form (25× elsewhere). The 5:10 KD does cross-reference the synecdoche but uses the variant phrasing. **Recommend: normalize 5:10/15/16/18 to ผู้นำชาวยิว for corpus-uniform leader-marked rendering, OR document the Bethesda-block intentional variant. Ben to decide.**

### REVIEW flag — Passion-narrative ยิว / ชาวยิว / ผู้นำชาวยิว oscillation

In John 18–20 the same lemma renders as **ยิว** (compressed), **ชาวยิว** (full), or **ผู้นำชาวยิว** (leader-marked) within consecutive verses. Defensible by context (e.g., 18:33 Pilate's question quotes the title "King of the **Jews**" → ชาวยิว; 18:31 "Take him yourselves" addressed to the prosecutorial leadership → ยิว). But **the principle is unstated** — the choice between ชาวยิว and ยิว especially is not flagged as register-vs-length in any KD. Worth either documenting or normalizing.

**→ Recommend new doc:** `docs/translator_decisions/ioudaioi_johannine_2026-04.md` — locks the four-way split (ผู้นำชาวยิว / ชาวยิว / ยิว / [retire พวกผู้นำยิว as deprecated variant]) before Romans (esp. Rom 9–11), Galatians, Thessalonians.

---

## 2. λόγος — multi-rendering by referent class — **STABLE-with-questions (undocumented; recommend new doc)**

35 verses; 7 distinct Thai renderings, principled by referent:

| Sense | Thai | Count | Verses |
|---|---|---|---|
| Christological Logos (Prologue doctrine) | **พระวาทะ** | 2 | 1:1 (×3), 1:14 |
| Father's word / scripture (royal-marked, written-revelation register) | **พระวจนะ** | 4 | 10:35, 17:6, 17:14, 17:17 |
| Jesus's spoken word (royal-marked, divine-utterance register) | **พระดำรัส** | 4 | 2:22, 4:41, 4:50, 5:38 |
| Jesus's word / saying (plain, most-frequent) | **คำ** | ~20 | 4:37; 5:24; 6:60; 7:36; 8:31, 8:37, 8:43, 8:51, 8:52, 8:55; 10:19; 12:38, 12:48; 14:23, 14:24; 15:3, 15:20, 15:25; 17:20; 18:9, 18:32; 19:8 |
| Testimony / witness (contextual) | **คำพยาน** | 1 | 4:39 |
| Teaching (contextual) | **คำสอน** | 1 | 6:60 |
| Rumor (contextual, narrator-distancing) | **คำเล่าลือ** | 1 | 21:23 |

**Three principled royal-marked renderings:**
- **พระวาทะ** — reserved exclusively for the Christological Logos in the Prologue. Excellent.
- **พระวจนะ** — reserved for written-scripture / Father's word (10:35 "scripture cannot be broken"; 17:6/14/17 "your word is truth"). Documented at 10:35 as scripture-register.
- **พระดำรัส** — reserved for Jesus's spoken word in narrator-emphasized contexts (2:22 "they remembered his word"; 4:41 "they believed because of his word"; 4:50 "the man believed the word Jesus spoke to him"; 5:38 "you do not have his word abiding in you").

### REVIEW flag — Farewell Discourse drift (พระดำรัส → คำ)

The Farewell Discourse (chs. 14–17) systematically uses **คำ** (plain) for Jesus's word/teaching, even where the rhetoric mirrors 2:22 / 4:41 / 4:50 / 5:38 patterns. Examples: 14:23 "if anyone loves me, he will keep my **word** (λόγον)"; 14:24 "the **word** (λόγος) which you hear is not mine"; 15:3 "you are clean because of the **word** (λόγον) I have spoken"; 15:20 "remember the **word** I said"; 15:25 "the **word** written in their law"; 17:20 "those who will believe through their **word**." Several of these carry the same divine-utterance weight as 2:22 / 4:50.

**Two readings:**
(a) **Principled register-collapse in Farewell Discourse** — Jesus is speaking intimately to disciples in the Upper Room; the διδακτική register prefers plain คำ over royal-marked พระดำรัส. If so, document as a Farewell-Discourse stylistic choice.
(b) **Drift** — should normalize critical instances (esp. 14:23–24, 15:3, 17:20) to พระดำรัส for consistency with 2:22 / 4:41 / 4:50 / 5:38 narrator-emphasis pattern.

**Ben to decide.** The corpus-lock for **พระวาทะ** (Logos) is unambiguous; the **พระดำรัส vs คำ** split needs explicit principle.

**→ Recommend new doc:** `docs/translator_decisions/logos_johannine_2026-04.md` — locks (1) พระวาทะ for Christological Logos (the Prologue title), (2) พระวจนะ for written-scripture / Father's word, (3) พระดำรัส for narrator-emphasized Jesus-speech, (4) คำ for general/dialogue. Also locks the contextual-class renderings (คำพยาน, คำสอน, คำเล่าลือ). Will compound into 1 John 1:1 ("the **Word** of life"), Hebrews 4:12, Revelation 19:13.

---

## 3. Vocative Κύριε — pre-recognition vs post-recognition arc — **STABLE-and-extends-existing-doc (recommend amendment)**

The existing `vocative_kyrie_didaskale_register_2026-04.md` (Luke-locked) classifies vocative Κύριε by speaker-class (disciples vs. crowds vs. adversaries). John adds a **narrative-recognition arc** axis specifically for human-to-Jesus encounters — uniformly applied across 14 verses:

| Recognition state | Thai | Count | Representative |
|---|---|---|---|
| **Pre-recognition** ("Sir / honored one," polite-not-divine) | **ท่านเจ้าข้า** | 9 | Samaritan woman 4:11, 4:15, 4:19; royal official 4:49; paralytic 5:7; bread-of-life crowd 6:34; pre-recognition blind man 9:36; Mary at the tomb (thinking Jesus is the gardener) 20:15; Greeks to Philip 12:21 |
| **Post-recognition** ("Lord," divine-recognition register) | **พระองค์เจ้าข้า** | 2 | blind man at recognition moment 9:38; Martha for Lazarus's sister Mary 11:3 |
| **Full Christological confession** ("the Lord," post-resurrection or OT-citation) | **องค์พระผู้เป็นเจ้า** | 4 | Peter 6:68; Thomas 20:28 (κύριος + θεός double); OT-citation Isa 53:1 LXX → JHN 12:38 |

**The blind-man pivot at JHN 9:36 → 9:38 is the cleanest exegetical proof of the arc.** Same speaker, same Greek vocative κύριε, but vv.36 (before the self-revelation in v.37) → ท่านเจ้าข้า; v.38 (after recognition + worship) → พระองค์เจ้าข้า. Translator's KD at 9:38 explicitly names the "REGISTER ESCALATION."

**Recommend: amend `vocative_kyrie_didaskale_register_2026-04.md`** to add the narrative-recognition arc axis (as a Johannine-specific extension), with the JHN 9:36→9:38 case as the locking precedent. The pattern will be revisited in John 21:15–17 (Peter post-restoration), Acts 9:5 (Saul on the road), Revelation 1:8 / 22:20.

---

## 4. ἀμὴν ἀμὴν λέγω — JHN 3:11 DRIFT — **DECIDE before tagging**

The locked Johannine doubled-amen formula is **อาเมน อาเมน** (per `johannine_doubled_amen_2026-04.md`). Verified compliant in all observed plural-form occurrences (`ὑμῖν`): 6:47, 8:51, 12:24, 13:16, 13:20, 14:12, 16:20, 16:23 — all use อาเมน อาเมน เราบอกแก่พวกท่านว่า. Singular-form (`σοι`): 13:38 (to Peter) + 21:18 (to Peter) — both use อาเมน อาเมน เราบอกแก่เจ้าว่า. **One verse violates the lock**:

- **JHN 3:11**: greek `ἀμὴν ἀμὴν λέγω σοι, ὃ οἴδαμεν λαλοῦμεν…` rendered as **"ความจริง ความจริง เราบอกท่านว่า…"** instead of the locked อาเมน อาเมน.

This is the only Johannine doubled-amen in JHN that uses the older Synoptic-style "ความจริง ความจริง" rendering. (The phrase_consistency checker missed this — its Greek-pattern variant list may not include `ἀμὴν ἀμὴν λέγω σοι` singular form.)

**Ben to decide:** normalize 3:11 to "อาเมน อาเมน เราบอกแก่ท่านว่า" (singular ท่าน, since Nicodemus is addressed individually, mirroring the 13:38 / 21:18 σοι pattern with เจ้า) for full corpus uniformity. Recommend yes — this is the only JHN ἀμὴν ἀμὴν that's not in the lock form, and the doc's stated 25× count assumes uniformity.

**Followup:** extend `scripts/check_phrase_consistency.py`'s Johannine-doubled-amen Greek-pattern variant list to include `ἀμὴν ἀμὴν λέγω σοι` (singular), so this category of drift is caught automatically in future books. Currently the check's "20 OK / 0 violations" report misses singular-σοι verses entirely.

---

## 5. JHN 7:8 — οὐκ vs οὔπω textual variant + Thai softening — **DECIDE**

**Famous textual variant:** SBLGNT/NA28/UBS5 read `ἐγὼ οὐκ ἀναβαίνω εἰς τὴν ἑορτὴν ταύτην` ("I am NOT going up to this feast") against TR/Byz `οὔπω` ("I am NOT YET going up"). RULES §0 binds the project to SBLGNT. The 7:8 verse-level `notes` correctly explains the variant + names Porphyry's "Jesus lied" critique that motivates the οὔπω reading historically.

**However, the Thai rendering is "เรา ยังไม่ ขึ้นไปยังเทศกาลนี้"** ("I am not yet going up to this feast") — which lexicalizes the οὔπω meaning the project explicitly chose against. The closer SBLGNT-faithful rendering would be **"เรา ไม่ ขึ้นไปยังเทศกาลนี้"** (plain "not"), which then requires the v.10 reader-resolution ("after his brothers had gone up, then he himself went up") to do the work the project's notes describe ("not going up [now, with you, publicly] vs. [later, alone, secretly]").

**Two readings:**
(a) **Deliberate Thai-naturalness softening** of a SBLGNT-faithful οὐκ. If so, document at 7:8 KD as principled exception ("Greek text-critically chosen οὐκ; Thai contextual rendering ยังไม่ to preserve ethical-coherence reading").
(b) **Drift** — Thai rendering effectively translates the rejected οὔπω textual choice. Should revise to plain "ไม่" (or restructure: "เราไม่ขึ้นไปยังเทศกาลนี้ [ในตอนนี้]" with bracketed clarifier).

**Ben to decide.** This is a high-visibility verse — first thing a textually-aware Thai reader who compares against KJV/THSV will notice ("why does THSV say ยัง but you say ยัง too — wait, didn't you choose SBLGNT?"). Recommend the project's editorial stance be made explicit either way.

---

## 6. JHN 1:34 — ἐκλεκτός variant — **REVIEW (confirm against evangelical-Thai reader-expectation)**

**Major textual variant:** SBLGNT (followed here) reads `ὁ ἐκλεκτὸς τοῦ θεοῦ` ("the Chosen One of God"); NA28, TR, Byzantine majority, KJV, BSB, NIV, ESV, CSB, THSV1971 all read `ὁ υἱὸς τοῦ θεοῦ` ("the Son of God"). The translator's choice follows SBLGNT (per RULES §0); rendering is **"ผู้ที่พระเจ้าทรงเลือกสรร"** with full textual-variant note at the verse-level.

**Editorial weight:** This is one of two verses in JHN where the SBLGNT reading diverges from the entire mainstream evangelical English-Bible tradition (the other being 1:18 μονογενὴς θεός, where SBLGNT diverges only from KJV/TR). The 1:34 divergence is more visible because **NA28 itself** sides with υἱός — meaning even the standard scholarly critical text disagrees with SBLGNT here.

**REVIEW flag:** Confirm Ben endorses the SBLGNT-strict choice at 1:34 against the unanimous Thai-evangelical reader expectation (THSV/NTV/ERV-Thai all use "พระบุตรของพระเจ้า"). The verse-level `notes` lay out the manuscript evidence comprehensively (P5 + ℵ* + Old Latin + Old Syriac for ἐκλεκτός vs. P66 + P75 + ℵ² + A + B + C + K + L for υἱός — overwhelming numerical advantage to υἱός). The rendering is defensible-and-well-documented, but **likely to be one of the most flagged verses by Thai theological reviewers**. Worth either (a) confirming + adding a footer-note for reader expectation management, or (b) revising to follow NA28 + the unanimous mainstream.

---

## 7. ἀρχιερεύς / ἀρχιερεῖς — JHN 7:32 + 7:45 plural-form drift — **REVIEW**

Verified across 20 occurrences. Singular ἀρχιερεύς (high priest in office, esp. Caiaphas) is consistently **มหาปุโรหิต**. Plural ἀρχιερεῖς (chief priests, the Sadducean priestly aristocracy / temple authorities) is consistently **พวกหัวหน้าปุโรหิต** — matching the Acts-locked rendering — at JHN 11:47, 11:57, 12:10, 18:3, 18:35, 19:6, 19:15, 19:21.

**Two outliers:** JHN 7:32 + 7:45 render plural ἀρχιερεῖς as **พวกมหาปุโรหิต** (พวก- + มหา-). Both are the same narrative block (Pharisees-and-chief-priests sending temple guards to arrest Jesus). Both are grammatical Thai for "the chief priests" (พวกมหา- pluralizes the singular form), but the Acts-corpus default is **พวกหัวหน้าปุโรหิต** (heads-of-priests).

**Recommend: normalize 7:32 + 7:45** to พวกหัวหน้าปุโรหิต for consistency with the JHN 11:47 → 19:21 corpus + the existing Acts lock. (Or, if the 7:32 + 7:45 form is intentional, document as a JHN 7-specific variant.)

---

## 8. ναός / ἱερόν — JHN 2:14–21 distinction collapse — **REVIEW**

The corpus principle (`ouranos_heaven_rendering`-style principled-distinction): `ἱερόν` = the Temple complex / outer precincts; `ναός` = the inner sanctuary / Holy of Holies. JHN 2:14–21 is the locus where John exploits the wordplay: the Jews think Jesus's "destroy this temple" refers to the building (`ἱερόν`-mental-image); Jesus means the inner sanctuary (`ναός`) of his own body.

**Current rendering:**
- 2:14, 2:15: ἐν τῷ ἱερῷ → **ในบริเวณพระวิหาร** (Temple precincts) ✓ matches existing lock
- 2:19, 2:20, 2:21: ναός / ναόν → **พระวิหาร** (Temple, plain)

**Distinction collapse:** Thai readers see "บริเวณพระวิหาร" (precincts) at 2:14–15 and "พระวิหาร" (Temple) at 2:19–21 — but without an explicit register marker for ναός as inner-sanctuary, the wordplay (Jews thinking *building*, Jesus meaning *holy place* / his own body), pivots only on the "บริเวณ" qualifier rather than on the distinct ναός vocabulary. The 2:19 KD does explain the wordplay, but the Thai surface doesn't carry it.

**Two options:**
(a) **Mark ναός distinctively** — e.g., "พระวิหารชั้นใน" (inner-sanctuary) at 2:19/20/21. Preserves the lemma distinction; risks awkward periphrasis ("Destroy this **inner-sanctuary**…").
(b) **Document the collapse** — note that the Thai relies on the 2:14–15 vs 2:19–21 phrasing-difference (precincts vs. plain) to carry the wordplay implicitly + the 2:21 narrator clarification ("but he was speaking of the temple of his body"). Defensible but loses surface-distinguishability for the lemma.

**Ben to decide.** Compounds into Matthew 26:61 + 27:5/40/51, Acts 6:13 + 7:48, 1 Cor 3:16–17 + 6:19, 2 Thess 2:4, Heb 9:11–24, Rev 7:15 + 11:19 + 21:22.

---

## 9. μένω — central Johannine verb — **STABLE (undocumented; consider doc later)**

78 verses; ~57× in distinctly-Johannine "abide/remain" senses (the rest are ordinary "stay/dwell"). Renderings observed:

| Context | Thai | Representative |
|---|---|---|
| Spirit-remaining-on-Christ (1:32) | **สถิต** (royal-rest) | 1:32 |
| Disciples staying with Jesus (1:38–39) | **ประทับอยู่** (royal-dwell) | 1:38, 1:39 |
| Water becoming wine still-being-water (2:9) | **ที่กลายเป็น…แล้ว** | 2:9 |
| Word of God abiding in believer (5:38) | **คงอยู่** (remain-permanent) | 5:38, 8:31, 8:35, 14:25, 15:4–10 (vine), 15:16 |
| Spirit's abiding presence (14:17) | **คงอยู่** | 14:17 |
| "If you abide in me" (15:4–7) — central Farewell motif | **จงคงอยู่** (imperative) | 15:4 (×2), 15:5, 15:6, 15:7, 15:9, 15:10 |
| Lazarus four days in tomb (11:6) | **ทรงคอยอยู่** | 11:6 |
| Bread that endures (6:27) | **ดำรงอยู่** (endure-eternally) | 6:27 |
| John 21:22–23 disciple "remaining until I come" | **คงอยู่** | 21:22, 21:23 |

The verb is rendered with deliberately-different Thai equivalents tracking the contextual nuance: คงอยู่ (the dominant abide), ประทับอยู่ (royal-dwelling), สถิต (Spirit's presence), ดำรงอยู่ (eternal-endurance), คอยอยู่ (await). The principled split is implicit in the per-verse `key_decisions` but is not consolidated.

**Recommend: STABLE; consider new doc** `docs/translator_decisions/meno_abide_johannine_2026-04.md` if 1 John 2:6/10/14/17/19/24/27/28 + 3:6/9/14/15/17/24 + 4:12/13/15/16 (the Catholic Epistles intensification) require corpus-coordination. If the Thai distinctions hold there too, no doc needed.

---

## 10. παράκλητος — **STABLE (in-place lock at 14:16; recommend lift to corpus doc)**

4 occurrences (14:16, 14:26, 15:26, 16:7), all uniformly **พระผู้ช่วย** (royal-helper) with consistent royal phrasing. The 14:16 KD declares "**NEW CORPUS-LOCK**: παράκλητος → พระผู้ช่วย"; subsequent occurrences (14:26, 15:26, 16:7) cite the lock by reference.

**Recommend: lift in-place corpus-lock to `docs/translator_decisions/parakletos_holy_spirit_2026-04.md`.** The doc can summarize: (1) the four Johannine occurrences (Spirit), (2) 1 John 2:1 (Christ as Παράκλητος → likely needs separate Christological treatment), (3) why "พระผู้ช่วย" was preferred over alternatives (พระวิญญาณผู้ช่วย, พระผู้ปลอบโยน, etc.). Important pre-1-John handoff.

---

## 11. Ἐγώ εἰμι — absolute (predicate-less) form — **STABLE (4-way principled split; undocumented)**

The distinctly Johannine "I AM" sayings split into two classes:
- **With predicate** (the seven famous "I am the X" — bread, light, gate, good shepherd, resurrection, way, vine): each rendered uniformly with **เราเป็น + [predicate]** (e.g., เราเป็นขนมปังแห่งชีวิต 6:35, 6:48; เราเป็นความสว่างของโลก 8:12, 9:5; เราเป็นประตูของแกะ 10:7; เราเป็นผู้เลี้ยงแกะที่ดี 10:11, 10:14; เราเป็นเถาองุ่น 15:1, 15:5). **STABLE** ✓
- **Absolute / predicate-less** (the climactic Ἐγώ εἰμι without complement, echoing Exod 3:14 LXX + Isa 43:10 LXX): **four distinct Thai forms by context.**

| Context | Thai | Verses |
|---|---|---|
| Self-identification to terrified disciples ("It's me") | **นี่เราเอง** | 6:20 |
| Dialogue self-disclosure to Samaritan woman (gloss-extended for clarity) | **เราที่กำลังพูดกับท่านอยู่นี้คือผู้นั้นเอง** | 4:26 |
| Climactic identification before arresting soldiers | **เราคือผู้นั้น** | 18:5, 18:6, 18:8 |
| Climactic Christological / YHWH-echo ("Before Abraham was, I AM") | **เราเป็น** (bare predicate) | 8:24, 8:28, 8:58, 13:19 |

Notice: 8:24 + 8:28 + 8:58 + 13:19 use bare **เราเป็น** to preserve the Exod 3:14 LXX echo (`ἐγώ εἰμι ὁ ὤν`). 18:5–8 use **เราคือผู้นั้น** because the soldiers ask for "Jesus of Nazareth" (so an answering self-identification). 6:20 is informal recognition. 4:26 is mid-dialogue with gloss. **The four-way split is principled and theologically articulate.**

**Recommend: STABLE; consider new doc** `docs/translator_decisions/ego_eimi_johannine_2026-04.md` to lock the contextual split (including the seven "I am + X" forms). The doc should explicitly state that **8:58 / 8:24 / 8:28 / 13:19 use bare "เราเป็น" specifically to preserve the YHWH self-name echo** — this is the most theologically charged Johannine signature, deserves explicit corpus-lock.

---

## 12. σάρξ — **STABLE (principled multi-rendering; documented at verse level)**

9 verses; principled three-way split:
- Anthropological "flesh" (= human nature, embodied desire) → **เนื้อหนัง**: 1:13 (will of the flesh), 3:6 (born of the flesh), 8:15 (judging according to the flesh) — and the Incarnation 1:14 ναός σὰρξ ἐγένετο → **ทรงรับสภาพเป็นมนุษย์** (took on human nature).
- Eucharistic (whole-body-as-offered) → **เนื้อ** (plain "flesh-as-meat" register): 6:51, 6:52, 6:53, 6:54, 6:55, 6:56 (eat my flesh).
- "According to the flesh" (assessment-by-mere-appearance) → **ตามมาตรฐานของเนื้อหนัง**: 8:15.

The 1:14 incarnation rendering is particularly note-worthy: **ทรงรับสภาพเป็นมนุษย์** ("took on the form of a human") rather than literal "พระวาทะกลายเป็นเนื้อหนัง." Defensible (Thai naturalness; theological-form-precision per Phil 2:7-style μορφή); worth confirming with Ben since this is the singular Christological verse where the σάρξ word-choice carries Chalcedonian weight. **STABLE — verse-level rationale carries; no doc needed unless 1 John 4:2 σάρκα ἐληλυθότα and 2 John 7 σαρκὶ make the σάρξ lemma do further Christological work.**

---

## 13. δοξάζω / δόξα — Father↔Son glorification idiom — **REVIEW (extends existing doc)**

`divine_object_praise_verbs_2026-04.md` (Acts-amended) locks **สรรเสริญ** as the corpus default for δοξάζω + εὐλογέω + αἰνέω + αἶνον δίδωμι when the *human* is the subject and *God* is the object (with a documented sub-rule for narrator-doxological **ถวายเกียรติ**).

JHN exhibits a **new pattern** the doc doesn't yet cover: **Father↔Son mutual glorification** (12:23, 12:28, 13:31–32, 14:13, 17:1–5, 17:10, 17:24). Where the subject is the Father glorifying the Son (or vice versa), the Thai uses **พระสิริ** (noun: glory) + variants like **ทำให้ … ได้รับพระสิริ** ("cause ... to receive glory") or **ถวายพระสิริแด่** ("give glory to"). Examples:
- 12:23 δοξασθῇ ὁ υἱὸς → **บุตรมนุษย์จะได้รับพระสิริ**
- 12:28 δόξασόν σου τὸ ὄνομα → **ขอทรงทำให้พระนามของพระองค์ได้รับพระสิริเถิด**
- 12:28b ἐδόξασα ... δοξάσω → **ได้ทำให้ได้รับพระสิริแล้ว ... จะทำให้ได้รับพระสิริอีก**
- 13:32 ὁ θεὸς δοξάσει αὐτὸν ἐν αὑτῷ → **พระเจ้าก็จะทรงให้พระองค์ได้รับพระสิริในพระองค์เอง**
- 17:5 δόξασόν με σύ → **ขอพระองค์ทรงให้เราได้รับพระสิริต่อพระพักตร์ของพระองค์**

The pattern is uniformly **พระสิริ + receive-causative** (not สรรเสริญ, which would be wrong here — it's not "praise" in the Acts-doxological sense, but the *transfer/manifestation of divine glory*). The 5:41 + 5:44 cluster correctly distinguishes — when humans seek **δόξα** from each other, it's **เกียรติ** (honor); when the Father glorifies the Son, it's **พระสิริ** (divine-glory-transfer).

**REVIEW: Confirm + amend `divine_object_praise_verbs_2026-04.md`** with a new sub-rule: "Father↔Son intra-Trinitarian glorification (esp. dense in JHN 12 + 17) → **พระสิริ (received/transferred)**, distinct from human-praise-of-God default **สรรเสริญ** and narrator-doxological **ถวายเกียรติ**." This is genuinely Johannine-distinctive and will recur in Romans 8:30, 9:23, 1 Cor 2:7–8, 2 Cor 3:18 (transformative-glory), Eph 1:6/12/14 (εἰς ἔπαινον τῆς δόξης), Phil 2:11, 1 Pet 1:8, 4:14 — and especially Revelation's massive doxological-glory vocabulary.

---

## 14. JHN 21:15–17 — ἀγαπάω / φιλέω flattening — **STABLE (explicit decision; recommend new doc)**

The famous Peter-restoration dialogue: Jesus uses **ἀγαπάω** twice (vv.15, 16), then switches to **φιλέω** in v.17; Peter answers all three with **φιλέω**. Thai renders **all six occurrences as รัก** ("love"). The 21:15 KD + thai_summary explicitly document: "The Greek ἀγαπάω/φιλέω alternation is preserved as-รัก-throughout in Thai (matching most-modern-English-versions which-translate-both as 'love' — the synonym-hypothesis is widely-held in modern-Greek-NT scholarship)."

This is an **explicit, principled, documented editorial decision** (the synonym-hypothesis position; matches NIV/ESV/CSB; differs from Amplified Bible / NASB-margin / older expository tradition). **STABLE — no action needed**, but I recommend lifting to a corpus doc for two reasons:
1. The decision isn't only about JHN 21:15–17. It applies corpus-wide: 5:20 (ὁ πατὴρ φιλεῖ τὸν υἱόν) and 3:35 (ὁ πατὴρ ἀγαπᾷ τὸν υἱόν) both render Father-loves-Son as **ทรงรัก** with no lexical distinction. The doctrine: ἀγαπάω + φιλέω are treated as Johannine synonyms in this translation.
2. It will be referenced repeatedly by Thai theological reviewers (the ἀγαπάω/φιλέω distinction is a perennial expository sermon-staple).

**→ Recommend new doc:** `docs/translator_decisions/agapao_phileo_johannine_synonym_2026-04.md`. Locks the synonym-hypothesis position; cites JHN 21:15–17 as the locking evidence; cross-references 3:35 + 5:20 + 11:3/5/36 + 16:27 + 20:2 + 21:7/20.

---

## 15. Aramaic embeds — **all compliant per `aramaic_transliterations_2026-04.md`**

Per the Mark-locked treatment (preserve Aramaic transliteration AND Greek translation):
- **Μεσσίας** → **เมสสิยาห์** (1:41 + 4:25; both with explanatory "ผู้ที่เรียกว่าพระคริสต์" gloss)
- **Ῥαββί** → **รับบี** (1:38, 1:49, 3:2, 3:26, 4:31, 6:25, 9:2, 11:8 — uniform)
- **Ῥαββουνί** → **รับโบนี** (20:16; Mary's recognition vocative; per Aramaic doc)
- **Σιλωάμ** → **สิโลอัม** (9:7, with "ซึ่งแปลว่า 'ผู้ถูกส่งไป'" gloss)
- **Γολγοθα** → **กลโกธา** (19:17, with "สถานที่กะโหลกศีรษะ" gloss)
- **Γαββαθα** → **กับบาธา** (19:13, with "ลานหินปู" gloss)
- **Βηθεσδά / Βηθζαθά** → **เบธซาธา** (5:2; SBLGNT reads Βηθζαθά)
- **Κηφᾶς** → **เคฟาส** (1:42, with "ซึ่งแปลว่าเปโตร" gloss)
- **Δίδυμος** → **ดิดิมัส** (Thomas's Greek-nickname; 11:16, 20:24, 21:2)

**Note on 4:25 abbreviation:** the term-extract showed truncated "พระเมษ์" — that's a `[:80]`-truncation artifact in my extraction tool, not a translation issue. Verified: full rendering is "เมสสิยาห์ (ผู้ที่เรียกว่าพระคริสต์)."

**LOCKED** ✓ — no action.

---

## 16. Inherited locks — **all compliant**

| Doc | JHN evidence | Status |
|---|---|---|
| `basileia_kingdom_rendering_2026-04.md` | 3:3, 3:5 → **อาณาจักรของพระเจ้า**; 18:36 → **อาณาจักรของเรา** (Christ's). Lock holds. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | 1:51 (heaven opened), 3:27 (given from heaven) → **ฟ้าสวรรค์** (default theological); 3:13, 6:31–58 (bread from heaven, chains of ἐκ τοῦ οὐρανοῦ), 12:28, 17:1 → **สวรรค์** (after preposition/possessor per doc rule). Compliant. | **LOCKED** |
| `son_of_man_disambiguation_2026-04.md` | 13× ὁ υἱὸς τοῦ ἀνθρώπου in JHN (1:51, 3:13, 3:14, 5:27, 6:27, 6:53, 6:62, 8:28, 9:35, 12:23, 12:34, 13:31) all uniform → **บุตรมนุษย์**. The 12:34 dialogue (people quote Jesus's title back) preserves the title. | **LOCKED** |
| `metanoeo_vs_metamelomai_2026-04.md` | **N/A — μετανοέω is striking absent from John (theologically significant)**. The Johannine equivalent is πιστεύω εἰς + the regeneration imagery (3:3–8, born ἄνωθεν). Worth a one-line note in next iteration of the doc explaining the JHN absence. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | 12:27 ἡ ψυχή μου → **จิตวิญญาณของเรา** (Christ's anguish; matches doc's "soul/inner-being" sense). 11:33 ἐνεβριμήσατο τῷ πνεύματι (Jesus moved in his spirit at Lazarus's tomb) → **ทรงสะเทือนพระทัย**. πνεῦμα ἅγιον (1:32–33, 7:39, 14:26, 20:22) → **พระวิญญาณบริสุทธิ์** uniform. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator royal register on Jesus throughout (พระองค์ทรง-, ตรัส, เสด็จ); adversary character speech tracks speaker stance. 8:39–44 fatherhood polemic — Jews call Abraham their **บิδา** (plain), then Jesus identifies their actual father as **มาร** (devil); Jews call God their **พระบิดา** (royal-divine) but Jesus rebuts. The plain/royal πατήρ split is principled per speaker. | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | The doc says "Lukan signature." JHN has 9 narrator-`ὁ κύριος` references (4:1, 6:23, 11:2, 20:2, 20:18, 20:20, 20:25, 21:7, 21:12). 7 of 9 follow the Lukan-Acts lock → **องค์พระผู้เป็นเจ้า**. **2 outliers:** **JHN 11:2** (Mary anointing the Lord) → **พระเยซูเจ้า**; the variant is also seen elsewhere. The doc's Lukan-only framing should be **amended** to acknowledge the JHN extension (the narrator-`ὁ κύριος` is also Johannine, especially post-resurrection). | **LOCKED-with-amendment-needed** |
| `vocative_kyrie_didaskale_register_2026-04.md` | See **§3 above** — JHN extends with pre/post-recognition arc. Amendment recommended. | **REVIEW** |
| `divine_object_praise_verbs_2026-04.md` | See **§13 above** — JHN's Father↔Son glorification idiom needs sub-rule amendment. | **REVIEW** |
| `historic_present_2026-04.md` | JHN is **the densest historic-present text in the NT** (~150+ occurrences; "λέγει" = "said" passim). All consistently rendered as Thai past tense per doc. Spot-checked 25 occurrences. | **LOCKED** |
| `parabolic_god_figures_human_register_2026-04.md` | JHN has the figurative ποιμήν (10:1–18) and ἀμπέλος (15:1–8) rather than Synoptic-style parables. The figures (Christ as shepherd, Father as vinedresser) get **royal register** because they're declared transparent identifications ("I AM the good shepherd"; "my Father is the vinedresser") — not parabolic-distance allegory. Doc's principle holds (parabolic distance → human register; transparent identification → royal). | **LOCKED** |
| `inclusion_variants_absent_verses_2026-04.md` | **PA (7:53–8:11)** Tier 3 ⟦…⟧ — fully bracketed across all 12 verses + chapter-footer reference to `output/textual_variants/john_08.json`. **JHN 5:3b–4** Tier 2 chapter-footer note (per RULES §5; reference to `output/textual_variants/john_05.json`). Compliant. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | See **§4 above** — 1 violation at 3:11. | **DRIFT (DECIDE)** |
| `aramaic_transliterations_2026-04.md` | See **§15 above**. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 21/21 chapters: `output/check_reports/john_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 21/21 chapters: `output/back_translations/john_NN.json` ✓
- 3 chapters have `output/check_reports/john_NN_external_review.md` (1, 6, 21 — past spot-reviews)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 5-book corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (incl. Johannine doubled-amen plural-form). **Note:** the singular-σοι form of ἀμὴν ἀμὴν is not in the lock pattern variants — this is why JHN 3:11 wasn't auto-caught (see §4).
- `git status output/`: only re-ran-check artifacts (john_21_review.md, key_term_consistency_all.md, phrase_consistency.md modified by my §1 verification re-runs; john_21_external_review.md exists). No source-file dirt.

---

## Pre-existing docs affirmed / unchanged

- `ekklesia_2026-04.md` — N/A in JHN (no occurrences of ἐκκλησία in the Johannine Gospel; the lemma debuts in 3 John).
- `aphesis_forgiveness_of_sins_2026-04.md` — JHN has no salvific ἄφεσις. The 20:23 ἀφῆτε / κρατῆτε passage uses verb-form ἀφίημι (forgive sins) → **ยกโทษ** uniform with the doc's root.
- `ethnos_2026-04.md` — minimal JHN exposure: 11:48 ("the Romans will come and take away our place and our **nation**" → ชนชาติ); 11:50–52 ("for the **nation**" → ชนชาติ); 18:35 (Pilate "your own **nation**" → ชนชาติ). All three correctly use **ชนชาติ** per the doc's "specific people-group" lock. The "Gentiles" (คนต่างชาติ) sense doesn't appear in JHN (the Gentile-mission framing is Acts/Paul). Compliant.
- `pagan_deities_2026-04.md` — N/A in JHN (no pagan deities named).
- `roman_administrative_titles_2026-04.md` — JHN has **χιλίαρχος** at 18:12 ("the Roman cohort and the tribune") → **นายพัน** ✓; **ἡγεμών**-type role for Pilate (named directly as Πιλᾶτος, not titled). Honorifics for Pilate: 16 occurrences across chs.18–19, all plain register (no royal ทรง- prefix on Pilate's actions); Jesus consistently royal-marked (ตรัส/พระองค์/ทรง-) when Pilate plain. Compliant per `honorifics_non_divine_authorities_2026-04.md`.
- `markan_euthys_immediately_2026-04.md` — Mark-specific; JHN doesn't use εὐθύς in Markan-signature mode.
- `amen_saying_formula_2026-04.md` — N/A (JHN uses doubled, not single, amen formula). See §4.
- `speech_verbs_adversaries_addressing_divine_2026-04.md` — Compliant. Adversary speech to Jesus uses **ทูล** (preserves Jesus's divine status) at e.g. 8:48 (Jews calling Jesus a Samaritan + demon-possessed → still "Ἀπεκρίθησαν αὐτῷ" rendered as **ตอบพระองค์ว่า**); 9:27 (formerly-blind man's adversaries → **ตอบ**); 18:30 (Jews to Pilate is Pilate-direction not Jesus-direction). The "even adversaries say ทูล when speaking to Jesus" pattern holds.

---

## Flagged for Ben's attention

### A. JHN 3:11 amen-amen drift — **DECIDE before tagging** (§4)
Normalize ความจริง ความจริง → อาเมน อาเมน? Recommend yes (only outlier; phrase-checker missed because single-σοι form not in lock variants — also extend the checker).

### B. JHN 7:8 Thai softening of SBLGNT οὐκ — **DECIDE** (§5)
Confirm whether "ยังไม่" is intentional contextual rendering (then document at KD as principled exception) or drift (then revise to plain "ไม่"). High visibility verse for textually-aware Thai readers.

### C. JHN 1:34 ἐκλεκτός — **REVIEW** (§6)
Confirm SBLGNT-strict choice against unanimous Thai-evangelical reader expectation. Verse-level rationale is comprehensive; question is reader-management (footer note? translator's-introduction explanation?).

### D. οἱ Ἰουδαῖοι 4-way split — **new doc + minor normalization** (§1)
**Highest Pauline-forward priority.** Lift the principle to corpus doc (`ioudaioi_johannine_2026-04.md`). Decide on 5:10–18 พวกผู้นำยิว variant (recommend normalize to ผู้นำชาวยิว) + Passion-narrative ยิว/ชาวยิว oscillation (recommend either document or normalize).

### E. λόγος multi-rendering — **new doc + Farewell-Discourse review** (§2)
Confirm the 7-way split (พระวาทะ / พระวจนะ / พระดำรัส / คำ / คำพยาน / คำสอน / คำเล่าลือ); decide whether Farewell-Discourse คำ should be lifted to พระดำรัส for major speech-emphasis verses (14:23–24, 15:3, 17:20). Then write `logos_johannine_2026-04.md`. Will compound into 1 John 1:1, Hebrews 4:12, Revelation 19:13.

### F. Vocative Κύριε — **amend existing doc** (§3)
Add the JHN narrative-recognition arc to `vocative_kyrie_didaskale_register_2026-04.md` (pre/post-recognition axis with JHN 9:36→9:38 as locking precedent).

### G. δοξάζω Father↔Son sub-rule — **amend existing doc** (§13)
Add Father↔Son intra-Trinitarian glorification sub-rule (พระสิริ-receive/transfer) to `divine_object_praise_verbs_2026-04.md`. Compounds into Romans 8:30, 2 Cor 3:18, Eph 1:6/12/14.

### H. Narrator-κύριος doc scope — **amend Lukan-Acts doc** (§16)
`kyrios_narrator_voice_luke_acts_2026-04.md` is currently framed as Lukan-only signature; JHN has 9 narrator-ὁ κύριος references (mostly post-resurrection). Either rename + extend the doc or write a JHN-specific companion. Outlier rendering at JHN 11:2 (พระเยซูเจ้า) needs confirmation or normalization to องค์พระผู้เป็นเจ้า.

### I. ἀρχιερεῖς (pl) at JHN 7:32 + 7:45 — **REVIEW** (§7)
Normalize พวกมหาปุโรหิต → พวกหัวหน้าปุโรหิต (Acts lock) for 2-verse drift, OR document as JHN 7-specific variant.

### J. ναός / ἱερόν distinction at 2:19–21 — **REVIEW** (§8)
Decide whether the wordplay-collapse (both → พระวิหาร with only the "บริเวณ" qualifier carrying ἱερόν vs. ναός) is acceptable, or mark ναός distinctively.

### K. New corpus docs to write (before next book)
1. `docs/translator_decisions/ioudaioi_johannine_2026-04.md` (§1)
2. `docs/translator_decisions/logos_johannine_2026-04.md` (§2)
3. `docs/translator_decisions/parakletos_holy_spirit_2026-04.md` (§10) — lift in-place 14:16 corpus-lock
4. `docs/translator_decisions/ego_eimi_johannine_2026-04.md` (§11) — optional but recommended; the bare-"เราเป็น" lock at 8:24/28/58/13:19 is too theologically charged to leave verse-level
5. `docs/translator_decisions/agapao_phileo_johannine_synonym_2026-04.md` (§14) — locks the synonym-hypothesis position before perennial expository pushback

### L. External AI review (§3 of checklist) — **pending**
Recommended before `book-john-v1` tag. Suggested 4-chapter packet: **JHN 1** (Prologue + Logos + Lamb of God + 1:18 + 1:34 ἐκλεκτός), **JHN 3** (Nicodemus + 3:11 amen drift + 3:14 ὑψόω + 3:16), **JHN 7–8** (PA tiering + 7:8 textual variant + Ἰουδαῖοι density + chief-priests drift + 8:58 climactic Ἐγώ εἰμι), **JHN 17** (high-priestly prayer; tests Father↔Son glorification + λόγος / πατήρ / unity vocabulary at peak density). Use Gemini 2.5 Pro + ChatGPT in parallel per the Acts pattern.

---

## Recommendation

**John ships in strong corpus-hygiene shape.** The JHN-distinct editorial decisions are well-documented at verse level; the gap is corpus-doc-lift before the editorial weight compounds into 1–3 John (which double down on μένω, ἀγάπη, παράκλητος, Logos, Ἰουδαῖοι), Hebrews (λόγος, ναός), and Revelation (Logos, glory-vocabulary, Ἰουδαῖοι at 2:9 + 3:9).

Tag `book-john-v1` after:
1. Ben's decisions on §A–C (DECIDE items)
2. Ben's decisions on §D–H (doc lifts + amendments)
3. Spot-revisions executed (3:11 amen, 5:10–18 variant, 7:32+45 chief priests, 11:2 narrator-κύριος if normalize) + checks clean
4. External AI sanity-check (§L)
5. Five new translator_decisions docs written (or four if ego_eimi is deferred)
6. Three existing docs amended (vocative_kyrie, divine_object_praise_verbs, kyrios_narrator_voice_luke_acts)

The Catholic Epistles (1–3 John especially) can be queued for next book — but writing `parakletos_holy_spirit_2026-04.md` + `ioudaioi_johannine_2026-04.md` + `logos_johannine_2026-04.md` should happen **before** 1 John 1:1 to avoid forward drift.
