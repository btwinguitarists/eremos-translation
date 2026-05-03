# Titus — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Titus** (3 chapters, 46 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged. Titus 3/3 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — Tit 1:5 + 1:7 πρεσβύτερος = ἐπίσκοπος equivalence: distinct Thai lemmas (ผู้ปกครอง vs ผู้ปกครองดูแล)

**The pattern:** Titus 1:5-7 contains the corpus's clearest Pastoral elder-overseer terminological interchange. The Greek explicitly equates the two terms within one paragraph:

> 1:5 GK: καὶ καταστήσῃς κατὰ πόλιν **πρεσβυτέρους**
> TH: และตั้ง**ผู้ปกครอง**ในแต่ละเมือง

> 1:7 GK: δεῖ **γὰρ** τὸν **ἐπίσκοπον** ἀνέγκλητον εἶναι ὡς θεοῦ οἰκονόμον
> TH: เพราะ**ผู้ปกครองดูแล**ต้องเป็นคนไม่มีข้อตำหนิ ในฐานะเป็นผู้ดูแลของพระเจ้า

The **γάρ** ("for") at v.7 connects v.7's qualification list back to v.5's office-introduction — making the equivalence grammatically explicit. The 1:7 KD names this:

> Per uW translate-unknown: 'overseer' is alternate name for the same office Paul called πρεσβύτερος at v.5 — function-of-the-elder being-an-overseer.

**Editorial assessment:** The Thai uses **two distinct lexical items sharing a stem**: **ผู้ปกครอง** ("ruler / one-who-presides") + **ผู้ปกครองดูแล** ("ruling-overseer"). The shared **ผู้ปกครอง** stem preserves the structural-equivalence; the **ดูแล** suffix differentiates the ἐπίσκοπος-instance.

Compare mainstream English:
- **BSB / ESV / NIV / CSB / NASB**: "elders" (1:5) / "overseer" (1:7) — distinct lexemes, same office (English parallel structure)
- **NLT**: "elders" / "an elder" (collapses the distinction at 1:7 into "elder must be")
- **NRSV**: "elders" / "bishop" (preserves distinction, with "bishop" raising ecclesiological questions)

**Forward-applicability** — Acts 20:17+28 (Paul calls the same Ephesian leaders both πρεσβυτέρους and ἐπισκόπους in one paragraph) + 1 Pet 5:1-2 (πρεσβυτέρους + ἐπισκοποῦντες same-office equivalence) + Acts 14:23 (Pauline-elder-establishment narrative) — all forthcoming books require the same equivalence-handling.

**Two questions:**
1. Is the Thai stem-shared / suffix-differentiated approach (**ผู้ปกครอง** vs **ผู้ปกครองดูแล**) **sufficient** to convey the πρεσβύτερος = ἐπίσκοπος equivalence the Greek deliberately makes? Or should the Thai use **identical rendering** for both (e.g., **ผู้ปกครองดูแล** at both 1:5 and 1:7) — which would force the equivalence at the cost of the Greek's lexical-pair distinctness, but match how Acts 20:17+28 will eventually need to read?
2. Should the Tit 1:7 thai_summary (currently absent) be added to **explicitly surface the πρεσβύτερος = ἐπίσκοπος equivalence** for Thai readers? Without a thai_summary, Thai readers may perceive two distinct offices where the Greek deliberately shows one office under two names. A brief thai_summary noting the equivalence (e.g., **"คำว่า 'ผู้ปกครองดูแล' (ἐπίσκοπος) เป็นชื่อทางการอีกแบบหนึ่งของ 'ผู้ปกครอง' (πρεσβύτερος) ที่กล่าวถึงในข้อ 5 — เป็นตำแหน่งเดียวกัน เน้นหน้าที่การดูแลฝูงแกะของพระเจ้า"**) would surface the structural-equivalence.

---

## Item B — Tit 1:11 ἐπιστομίζω + 1:13 ἀποτόμως + 1:12 γαστέρες + 2:3 ἱεροπρεπής: §J metaphor-flattening cluster

**The pattern:** Titus 1-2 contains the corpus's **densest §J metaphor-flattening application** — four distinct Greek metaphor-vehicles flattened to Thai-natural target-sense renderings within 32 verses:

| Verse | Greek | Vehicle (literal Greek imagery) | Thai (target sense) | §J-test result |
|---|---|---|---|---|
| 1:11 | ἐπιστομίζειν (HAPAX) | "muzzle / put-mouth-on" | **ห้ามไม่ให้พูด** ("forbid from speaking") | vehicle-fails (physical-restraint reads incongruous in Thai for human-teachers) |
| 1:13 | ἀποτόμως | "by-cutting-off" (severance imagery) | **อย่างเคร่งครัด** ("strictly") | vehicle-fails (cutting reads as physical-violence in Thai) |
| 1:12 | γαστέρες ἀργαί | "lazy bellies" (synecdoche; whole-by-part) | **คนตะกละและเกียจคร้าน** ("gluttonous and lazy") | vehicle-fails (belly-synecdoche reads as vulgar/cartoonish in Thai for character) |
| 2:3 | ἱεροπρεπεῖς (HAPAX) | "sacred-fitting / priestly-suitable" | **กิริยาที่สมศักดิ์ศรี** ("dignified bearing") | vehicle-fails (clerical-sacral frame too narrow for daily-life-comportment in Thai) |

**Counter-example (vehicle PRESERVED because determinative):** Titus 3:11 ἐκστρέφομαι ("turn-out / pervert") → **ได้หันเหไปผิดทาง** ("has-turned-aside-on-wrong-path") — the path-imagery transfers cleanly to Thai AND the metaphor IS determinative for the verse's argument (the divisive person has "turned" off the right way), so vehicle is preserved per §J working test #2 (clean Thai cognate-domain).

**Editorial assessment:** Each of the four flattening cases passes the §J working test (vehicle-not-determinative + no-clean-Thai-cognate-domain). The §J principle is now **stress-tested across all three Pastoral letters** with consistent application — `pastoral_corpus_locks_2026-05.md` §J locked the principle at 2TI end-of-book; Titus exercises it most densely.

The 1:11 KD explicitly cites the §J principle:

> Per pastoral_corpus_locks_2026-05.md §J metaphor-flattening principle: vehicle (muzzle-imagery) does not transfer cleanly to Thai for human-teachers; target sense (silence-from-teaching) preserved.

**Two questions:**
1. Are all four flattenings (1:11 muzzle / 1:13 cutting / 1:12 belly / 2:3 sacral) appropriate per the §J working test? Or should any be revisited as **vehicle-determinative** (i.e., the imagery itself does work the verse depends on)? Specifically: 1:11 ἐπιστομίζω ("muzzle") at the false-teacher silencing context echoes a livestock-management vehicle that some patristic commentators read as theologically-loaded (false-teachers as wild-beasts requiring restraint, paralleling 1:12's κακὰ θηρία "evil beasts"). Is that vehicle-link worth preserving (e.g., **ปิดปาก** "shut-the-mouth" — closer to the muzzle-imagery without being physically-restraint-coded) over the current target-only **ห้ามไม่ให้พูด**?
2. The 1:12 γαστέρες ἀργαί ("lazy bellies") flattening is particularly aggressive — the synecdoche is one of the famous Cretan-stereotype Epimenides-fragments. The current **คนตะกละและเกียจคร้าน** preserves the trait-pair structure but loses the bodily-synecdoche-based vulgarity that gives the line its Greek-rhetorical force. Is the flattening too aggressive, or is the §J test correctly applied (Thai readers would find belly-synecdoche jarring/cartoonish)?

---

## Item C — Tit 2:11-14 + 3:4-7 doxological-hymn-pair: parallel ἐπεφάνη-grace + Granville-Sharp Christology + λουτροῦ παλιγγενεσίας construction

**The pattern:** Titus contains TWO parallel doxological-hymn-fragments, each opening with **ἐπεφάνη** ("appeared") + a divine-attribute as subject, both anchoring the surrounding ethical instruction in the gospel-event:

> 2:11-14 GK opening: **Ἐπεφάνη** γὰρ **ἡ χάρις τοῦ θεοῦ** σωτήριος πᾶσιν ἀνθρώποις
> TH: เพราะ**พระคุณของพระเจ้า**ได้**ทรงปรากฏ**แล้ว นำความรอดมาให้แก่มนุษย์ทุกคน

> 3:4-7 GK opening: ὅτε δὲ **ἡ χρηστότης καὶ ἡ φιλανθρωπία** **ἐπεφάνη** τοῦ σωτῆρος ἡμῶν θεοῦ
> TH: แต่เมื่อ**ความเมตตาและความรัก**ที่พระเจ้าพระผู้ช่วยให้รอดของเราทรงมีต่อมนุษย์ ได้**ทรงปรากฏ**แล้ว

The pair is structurally parallel (γάρ-/ὅτε-δέ-grounding clause + divine-attribute-subject + ἐπιφαίνω + soteriological-result + Christological-naming + ἐθική-application). Three editorial decisions are load-bearing:

### (a) ἐπιφάνεια / ἐπιφαίνω lemma-lock corpus-wide → **(การ)ทรงปรากฏ**

Per the new 2026-05-03 corpus doc `epiphaneia_christou_2026-05.md`. Titus exhibits the corpus's **clearest dual-sense ἐπιφάνεια application** — first-coming (2:11 + 3:4) + second-coming (2:13) within a single letter, all using the same root-rendering **ทรงปรากฏ**.

### (b) 2:13 Granville-Sharp single-person Christological reading → **พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา**

Per `pastoral_corpus_locks_2026-05.md` §C pre-decision (locked at 1TI end-of-book; ratified by all three external reviewers Grok / Gemini / ChatGPT). The 2:13 verse is **the highest-Christological verse in the Pastorals** and one of the strongest NT-witness verses to the deity-of-Christ.

> 2:13 GK: τὴν μακαρίαν ἐλπίδα καὶ ἐπιφάνειαν τῆς δόξης **τοῦ μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ**
> TH: ความหวังอันเปี่ยมพร และการทรงปรากฏแห่งพระสิริของ**พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา**

The Thai apposition (subject-name first, then descriptive titles) reads naturally in Thai sequence-of-identification without forcing the Granville-Sharp grammatical pattern onto Thai syntax.

### (c) 3:5 λουτροῦ παλιγγενεσίας + ἀνακαινώσεως πνεύματος ἁγίου — single-vs-dual washing-event reading

The NT's most-debated baptismal-regeneration / sacramental-soteriology crux:

> 3:5 GK: ἔσωσεν ἡμᾶς διὰ **λουτροῦ παλιγγενεσίας** καὶ **ἀνακαινώσεως πνεύματος ἁγίου**
> TH: พระองค์ทรงช่วยเราให้รอด ... โดยทาง**การชำระล้างแห่งการบังเกิดใหม่** และ**การสร้างใหม่โดยพระวิญญาณบริสุทธิ์**

Two competing grammatical readings:
- **(i) One event with two characterizations**: "the washing-of-rebirth-AND-of-renewal-by-the-Spirit" — single-genitive-construction with both παλιγγενεσίας + ἀνακαινώσεως modifying λουτροῦ (sacramental-baptismal-regeneration interpretation; favored by patristic + Roman Catholic + some Reformed)
- **(ii) Two events / two means**: "washing-of-rebirth AND renewal-by-the-Spirit" — two coordinate-genitives expressing distinct-yet-paired soteriological moments (most modern evangelical: justification-and-sanctification frame)

The Thai construction with **และ** ("and") + **โดย** ("by-means-of") + Spirit-as-explicit-agent leans slightly toward reading (ii) without committing entirely. Compare mainstream English:
- **BSB / NIV / CSB / NASB**: "washing of regeneration and renewal by the Holy Spirit" (similar (ii)-leaning)
- **ESV**: "the washing of regeneration and renewal of the Holy Spirit" (more (i)-preserving)
- **KJV / NKJV**: "the washing of regeneration, and renewing of the Holy Ghost" (preserves single-vs-dual ambiguity)

The 3:5 thai_summary explicitly embraces interpretation (i) for the **first** half: *"'การชำระล้างแห่งการบังเกิดใหม่' มักถูกเข้าใจว่าหมายถึงประสบการณ์การรับบัพติศมาในฐานะสัญลักษณ์ภายนอกของการบังเกิดใหม่ภายในโดยพระวิญญาณ"* — a baptismal-symbol commitment that the main text leaves grammatically open.

**Three questions:**
1. Is the slight (ii)-leaning **และ ... โดย** construction the right corpus-default for the 3:5 baptismal-regeneration crux? Or should the Thai preserve more (i)-style ambiguity (e.g., **การชำระล้างแห่งการบังเกิดใหม่และการสร้างใหม่โดยพระวิญญาณบริสุทธิ์** without the explicit event-separator, leaning toward "the washing-of-rebirth-and-renewal-by-the-Spirit" as a single complex genitive)?
2. Should the 3:5 thai_summary's baptismal-symbol commitment soften to **neutral interpretation-presentation** (e.g., *"หลายคนเข้าใจว่า ... แต่บางคนเข้าใจว่า"*) to match the main text's grammatical-openness? The current commitment is principled-as-mainstream-evangelical but commits beyond what the Greek requires.
3. The 2:13 Granville-Sharp + 3:6 σωτήρ-Christ pair forms a **trinitarian-soteriological architecture** within Titus 2-3 (Father-saves-vv.4 + Spirit-poured-vv.5-6 + Son-the-channel-vv.6). Is the **trinitarian-shape preserved adequately** by the current Thai, or worth surfacing in a thai_summary at 3:6 that explicitly names the trinitarian framing (analogous to how 1 Pet 1:2 + Eph 1's trinitarian doxologies are typically annotated)?

---

## Item D — Tit 2:14 περιούσιος LXX-echo + Tit 3:10 αἱρετικός relational-divisive: corpus-distinctive HAPAX renderings

**The pattern:** Titus contains two distinctive HAPAX renderings worth surfacing for confirmation — both editorial moves with corpus-forward implications.

### (a) Tit 2:14 περιούσιος HAPAX + LXX-Exod 19:5 covenant-vocabulary echo

The HAPAX περιούσιος (only here NT) carries direct lexical-echo of LXX Exod 19:5 + Deut 7:6 + 14:2 + 26:18 — the OT covenant-people-of-special-possession formula:

> 2:14 GK: καθαρίσῃ ἑαυτῷ **λαὸν περιούσιον**
> TH: ทรงชำระ**ประชากรเป็นของพระองค์เอง**ให้บริสุทธิ์

The 2:14 KD documents the LXX-echo:

> HAPAX περιούσιος (only here NT) — though present in LXX Exod 19:5 + Deut 7:6 + Deut 14:2 + Deut 26:18 (covenant-people-of-special-possession). Render 'ประชากรเป็นของพระองค์เอง' — preserves the possessive-special-property sense without forcing the wooden 'ทรัพย์สมบัติพิเศษ' (which would commodify-the-people image). LXX ECHO of Exod 19:5 — see notes.

The thai_summary contextualizes the covenant-extension theology:

> วลี 'ประชากรเป็นของพระองค์เอง' (กรีก λαὸς περιούσιος) ยืมจากพันธสัญญาเดิม ... การใช้คำนี้กับคริสเตียนของเปาโลที่นี่ และในเปโตรฉบับที่หนึ่ง 2:9 บ่งบอกว่าคริสตจักรเป็นผู้ที่สืบทอดพันธสัญญาของอิสราเอลในความหมายเชิงเทววิทยา — ไม่ใช่แทนที่อิสราเอล แต่ขยายชนชาติของพระเจ้าให้รวมทั้งคนต่างชาติด้วย

**Editorial assessment:** **Editorially-mature handling** — render preserves the possessive-special-property sense without forcing wooden Thai; thai_summary surfaces the OT-covenant linkage AND the supersessionism-guardrail (per RULES §0). The non-supersessionist guardrail is the right pastoral move for Thai-evangelical readers shaped by replacement-theology preaching traditions.

### (b) Tit 3:10 αἱρετικός HAPAX → relational-divisive (not doctrinal-heretic)

> 3:10 GK: **αἱρετικὸν** ἄνθρωπον μετὰ μίαν καὶ δευτέραν νουθεσίαν παραιτοῦ
> TH: จงปฏิเสธ**คนที่ก่อให้เกิดการแตกแยก** หลังจากตักเตือนเขาครั้งที่หนึ่งและครั้งที่สองแล้ว

The HAPAX αἱρετικός (only here NT) is rendered **คนที่ก่อให้เกิดการแตกแยก** ("divisive person"). The 3:10 KD names the editorial choice:

> HAPAX αἱρετικός (only here NT) — adjectival from αἵρεσις 'faction / sect.' Per uW figs-explicit: implication is divisive-in-the-church (causing-faction-formation). Render 'คนที่ก่อให้เกิดการแตกแยก' — preserves the divisive-in-community sense without forcing the modern 'heretic' register (which would import doctrinal-deviation as primary, when the early-church αἱρετικός sense is closer to 'schism-causing'). The rendering captures both the doctrinal-divergence and the relational-faction-formation aspects.

**Editorial assessment:** The Greek αἱρετικός in 1st-c. usage is closer to **schism-causing** ("forming-a-faction") than to the modern technical-theological **heretic** ("holding-condemned-doctrine"). The Eremos rendering aligns with mainstream English (BSB/ESV/NIV/CSB/NASB all "divisive person" / "factious person"; KJV "heretick").

**Forward-applicability:** The αἵρεσις-family appears at 1 Cor 11:19 (factions in worship), Gal 5:20 (vice-list), 2 Pet 2:1 αἱρέσεις ἀπωλείας (the verse where doctrinal-content is more foregrounded), Acts 24:14 (sectarian sense for "the Way"). A future Pauline-corpus αἵρεσις-family doc could lock the relational-default + flag 2 Pet 2:1 as the doctrinal-content exception.

**Two questions:**
1. **(a) περιούσιος LXX-echo handling**: Is the **ประชากรเป็นของพระองค์เอง** rendering + thai_summary explicit covenant-extension framing principled? The thai_summary explicitly names the supersessionism-guardrail (per RULES §0). Is the guardrail **necessary** for Thai-evangelical readers (who may be shaped by replacement-theology preaching) or **excessive editorial commitment** (committing to a non-supersessionist reading that the verse itself doesn't litigate)?
2. **(b) αἱρετικός relational-vs-doctrinal rendering**: Is **คนที่ก่อให้เกิดการแตกแยก** the right αἵρεσις-family corpus-default? Forward-application: 1 Cor 11:19 + Gal 5:20 will use the same relational-rendering; 2 Pet 2:1 αἱρέσεις ἀπωλείας ("destructive heresies") may need a **doctrinal-content-foregrounded** rendering instead. Should the corpus pre-commit to the relational-default + flag 2 Pet 2:1 as the doctrinal-content exception, or evaluate verse-by-verse at translation-time?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
