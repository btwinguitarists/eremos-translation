# Malachi — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-27**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Malachi** (3 chapters, 55 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Malachi 3/3 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
- Tetragrammaton יהוה → องค์พระผู้เป็นเจ้า (NT-aligned per divine_names_table_2026-05.md); אֱלֹהִים → พระเจ้า; שַׁדַּי → ผู้ทรงมหิทธิฤทธิ์
- First-occurrence-per-chapter Tetragrammaton convention footer note in output/textual_variants/<book>_<chapter>.json (Layer 2)
- OT register: ราชาศัพท์ ทรง- on verbs whose subject is the divine person; plain verb when subject is a divine body part (e.g., יַד יהוה)
- Pagan deities (foreign אֱלֹהִים, plural-of-Moabite-gods, Baal/Asherah/etc.) → พระทั้งหลาย / เทพ — NEVER พระเจ้า (reserved for YHWH/true God)
- חֶסֶด (covenant loyal-love, Ruth 1:8 lock) → ความรักมั่นคง
- גֹּאֵל (kinsman-redeemer) → ญาติผู้ไถ่; גָּאַל / גְּאֻלָּה family verbs → ไถ่ / สิทธิ์ในการไถ่
- Hebrew oath formulas: כֹּה יַעֲשֶׂה יהוה ... וְכֹה יֹסִיף → ขอองค์พระผู้เป็นเจ้าทรงลงโทษ ... และให้หนักยิ่งกว่านั้นอีก; חַי־יהוה → ตราบใดที่องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่
- Hebrew anthropomorphism for YHWH's body parts: royal-Thai พระหัตถ์ / พระเนตร / พระโอษฐ์ / พระบาท (matches Rachasap when divine possessor)
- אֵשֶׁת חַיִל / אִישׁ גִּבּוֹר חַיִל (Ruth 2:1 + 3:11 mirrored pair) → ชายผู้มีฐานะมั่งคั่งและทรงเกียรติ / หญิงผู้ทรงคุณธรรมและทรงเกียรติ
- Hebrew jussive prayer-blessings (יְבָרֶכְךָ יהוה, יִתֵּן יהוה, etc.) → Thai ขอ-...ทรง- + verb (royal-honorific for divine subject)
- Hebrew narrative-opening וַיְהִי → idiomatic Thai (drop or use temporal-marker like 'วันหนึ่ง'); waw-consecutive chains do not require mechanical และ rendering

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Hebrew + Thai shown.

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
## Item A — The מַלְאָךְ "messenger" leitwort: should a human priest / forerunner read as ทูตสวรรค์ ("angel")?

Malachi is named for the word **מַלְאָכִי** ("my messenger," 1:1), and the lemma מַלְאָךְ is the structural hinge of the book. Every occurrence ships the corpus-locked head-noun **ทูตสวรรค์** — literally "heaven-messenger," i.e. **angel**:

| Verse | Hebrew | Referent | Thai (shipped) | English (BSB) |
|---|---|---|---|---|
| 2:7 | כִּ֛י מַלְאַ֥ךְ יְהוָֽה־צְבָא֖וֹת הֽוּא | **the human Levitical priest** | เพราะเขาเป็น**ทูตสวรรค์**ขององค์พระผู้เป็นเจ้าจอมโยธา | "because he is the messenger of the LORD of Hosts" |
| 3:1a | הִנְנִ֤י שֹׁלֵחַ֙ מַלְאָכִ֔י | **the human forerunner** (→ John the Baptist) | ดูเถิด เราจะส่ง**ทูตสวรรค์**ของเราไป | "Behold, I will send My messenger" |
| 3:1b | וּמַלְאַ֨ךְ הַבְּרִ֜ית | the Messenger of the covenant (divine/messianic) | คือ**ทูตสวรรค์**แห่งพันธสัญญา | "the Messenger of the covenant" |

**The rendering is deliberate and documented.** The project's lock `malak_yhwh_2026-05` §4.3 names Malachi explicitly — *"the book whose Hebrew title IS מַלְאָכִי"* — and rules that **the body-text lemma retains the lock** (uniform ทูตสวรรค์), so the single Hebrew lemma reads as the single Greek-NT lemma ἄγγελος (Matt 11:10 / Mark 1:2 / Luke 7:27 all cite 3:1 as ἄγγελός μου). The human-messenger nuance is carried in a footnote, not in the surface word.

**The tension.** ทูตสวรรค์ contains สวรรค์ = "heaven"; it is the standard Thai word for an **angel**. The *same* lock doc (§1, §4.4) carves out *"purely human messengers in non-supernatural narrative → use the plain register ผู้ส่งสาร or ทูต … outside this lock."* Malachi sits astride that line: 2:7 is a flesh-and-blood priest and 3:1a is a human prophet-herald, yet both read in Thai as "angel of the LORD of hosts." §4.3 was written anticipating the *name-form* and the forerunner — it never separately adjudicated the **human priest of 2:7**, which is the corpus's only instance of מַלְאַךְ יְהוָה applied to a human.

This is also **entangled with the open Zechariah §1 decision**, which proposes the *opposite* move — dropping สวรรค์ for the *theophanic* angel-of-YHWH (→ ทูตขององค์พระผู้เป็นเจ้า) while keeping ทูตสวรรค์ for ordinary angels. If Zechariah §1a is adopted, Malachi becomes maximally inconsistent: the *divine* angel loses สวรรค์ while the *human* priest keeps it. The two should be decided together.

Three candidate end-states:
1. **Hold as shipped** — all מַלְאָךְ → ทูตสวรรค์, human nuance in footnote (preserves the OT→NT lemma thread; accepts "angel" for a human).
2. **Human/divine split** — 2:7 + 3:1a → plain ทูต / ผู้ส่งสาร (human register); 3:1b keeps ทูตสวรรค์ (divine Messenger of the covenant). Faithful to the human/supernatural distinction; breaks the 1:1↔3:1 surface echo.
3. **Joint resolution with Zechariah** — corpus-wide ทูต-without-สวรรค์ default, สวรรค์ reserved for explicitly-angelic beings; requires the malak-doc amendment + Zechariah back-sweep.

**Two questions:** (1) For the **human** messengers of Malachi — the priest (2:7) and the forerunner (3:1a) — is **ทูตสวรรค์** ("angel of the LORD of hosts" / "my angel") the right Thai surface, or should they take the plainer human register (ทูต / ผู้ส่งสาร), with ทูตสวรรค์ reserved for the divine Messenger of the covenant in 3:1b? (2) Should this be ratified jointly with the open Zechariah angel-of-YHWH decision, and the resolution written back into `malak_yhwh_2026-05` §4.3 as an explicit Malachi human-messenger rule?

---

## Item B — Malachi 2:16: "I hate divorce" (MT/traditional) vs "he who divorces out of hate" (critical)

> כִּֽי־שָׂנֵ֣א שַׁלַּ֗ח אָמַ֤ר יְהוָה֙ אֱלֹהֵ֣י יִשְׂרָאֵ֔ל וְכִסָּ֤ה חָמָס֙ עַל־לְבוּשׁ֔וֹ … (MT)
> **Shipped Thai:** "‘เพราะเราเกลียดการหย่าร้าง’ องค์พระผู้เป็นเจ้าพระเจ้าแห่งอิสราเอลตรัสดังนี้ ‘และผู้ที่หย่าภรรยาก็เท่ากับเอาความทารุณคลุมเสื้อผ้าของตน’ …"
> **BSB:** "'For I hate divorce,' says the LORD, the God of Israel. 'He who divorces his wife covers his garment with violence,' says the LORD of Hosts."

The opening שָׂנֵא שַׁלַּח is grammatically ambiguous and the versions split two ways:
- **(a) God as speaker — "I hate divorce"** (KJV / NASB / BSB / NIV-1984). The Thai takes this: เราเกลียดการหย่าร้าง, framed by אָמַר יְהוָה אֱלֹהֵי יִשְׂרָאֵל.
- **(b) 3rd-person — "the man who divorces [his wife] out of hate covers his garment with violence"** (ESV / NRSV / NIV-2011). This reads שָׂנֵא as the participle "the one hating."

The translation ships (a) with (b) disclosed in a footnote, matching the project's source-of-record (BSB). The clause וְכִסָּה חָמָס עַל־לְבוּשׁוֹ is rendered เอาความทารุณคลุมเสื้อผ้าของตน ("covers his garment with violence" — the wrong stains the man like a garment).

The reading is MT-defensible and BSB-aligned, and the alternative is on the page. But it is a real exegetical fork with pastoral weight in Thai church usage, and modern critical consensus has moved toward (b).

**Question:** Should Malachi 2:16 keep the traditional God-as-speaker reading **"เราเกลียดการหย่าร้าง" ("I hate divorce")** as the in-body text with the "he-who-divorces-out-of-hate" reading footnoted (current state, MT-/BSB-faithful), or should the body adopt the 3rd-person critical reading? If the current reading stands, is the footnote's framing of the alternative clear enough for a Thai reader?

---

## Item C — Malachi 2:15: the supplied subject in an elliptical crux

> וְלֹא־אֶחָ֣ד עָשָׂ֗ה וּשְׁאָ֥ר ר֨וּחַ֙ ל֔וֹ וּמָה֙ הָֽאֶחָ֔ד מְבַקֵּ֖שׁ זֶ֣רַע אֱלֹהִ֑ים … (MT)
> **Shipped Thai:** "พระองค์มิได้ทรงสร้างเขาทั้งสองให้เป็นหนึ่งเดียว ทั้งเนื้อและจิตวิญญาณหรือ? และเหตุใดจึงเป็นหนึ่งเดียว? ก็เพื่อทรงแสวงหาเชื้อสายที่ชอบธรรม …"
> **BSB:** "Has not the LORD made them one, having a portion of the Spirit? And why one? Because He seeks godly offspring. …"

The MT here is among the most opaque verses in the prophets — literally "and-not one he-made, and-remnant-of spirit to-him; and-what the-one seeking seed-of God." It has no explicit subject and no explicit object. Essentially every modern version supplies both; BSB supplies "**the LORD** made **them** one." The Thai follows that path: พระองค์ (God) as subject, เขาทั้งสอง (the couple) as object, with เนื้อและจิตวิญญาณ ("flesh and spirit") glossing the difficult ושאר רוח, and เชื้อสายที่ชอบธรรม for זֶרַע אֱלֹהִים ("godly offspring").

The result is a smooth, BSB-aligned reading whose marriage-fidelity thrust is not in doubt — but the supplied subject/object reaches beyond the bare MT surface, and the gloss of ושאר רוח as "flesh and spirit" is interpretive.

**Question:** Is the interpretive, BSB-aligned rendering of 2:15 — supplying พระองค์ as subject and เขาทั้งสอง as object, and glossing ושאר רוח as ทั้งเนื้อและจิตวิญญาณ — acceptable for this acknowledged crux, or should the verse be rendered more cautiously / carry a footnote flagging that the subject and object are supplied?

---

## Item D — Malachi 3:1: הָאָדוֹן ("the Lord" who comes to his temple) → องค์เจ้านาย

> וּפִתְאֹם֩ יָב֨וֹא אֶל־הֵיכָל֜וֹ הָאָד֣וֹן ׀ אֲשֶׁר־אַתֶּ֣ם מְבַקְשִׁ֗ים … (MT)
> **Shipped Thai:** "และ**องค์เจ้านาย**ที่พวกเจ้าแสวงหาจะเสด็จมายังพระวิหารของพระองค์โดยฉับพลัน …"
> **BSB:** "Then the Lord whom you seek will suddenly come to His temple …"

הָאָדוֹן here is the **article-marked title** "the Lord/Master," and in this verse it denotes a clearly **divine / messianic** figure — the one who comes *to his own temple*. The translation renders it **องค์เจ้านาย**, the corpus's standard rendering for the bare/non-Tetragrammaton אֲדֹנָי title (also used in this same chapter-range for the more generic 1:12 "table of the Lord" and 1:14 "to the Lord"). The Tetragrammaton in the same verse (the closing אָמַר יְהוָה צְבָאוֹת) is kept distinct as องค์พระผู้เป็นเจ้าจอมโยธา.

The choice is consistent with the corpus bare-Adonai line and correctly avoids using the Tetragrammaton rendering for a non-YHWH title. The question is only whether องค์เจ้านาย — the same word used for the more generic 1:12/1:14 "Lord" — adequately carries the **divine/temple-owning** weight of הָאָדוֹן at 3:1, or whether the messianic referent here warrants a more elevated surface or a footnote distinguishing it.

**Question:** At Malachi 3:1, is **องค์เจ้านาย** the right rendering for הָאָדוֹן — "the Lord who comes to his temple" — given that the same word renders the more generic "Lord" of 1:12/1:14, or should the divine/messianic referent here be marked more strongly (elevated surface or a distinguishing footnote)?
</content>

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
