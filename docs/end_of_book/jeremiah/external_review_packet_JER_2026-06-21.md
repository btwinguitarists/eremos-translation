# Jeremiah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Jeremiah** (52 chapters, 1,364 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah complete (not yet tagged). Jeremiah 52/52 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Jeremiah (JER) — end-of-book external-review items

_Hand-curated from the JER end-of-book editorial review (`JER_END_OF_BOOK_REVIEW_2026-06-21.md`). One block per REVIEW/DECIDE item worth an independent second opinion. (Supersedes the auto-derived generic stub.) The project follows the **Masoretic Text** surface, renders the Tetragrammaton יהוה → **องค์พระผู้เป็นเจ้า**, uses Thai royal register (**ราชาศัพท์**, the ทรง/พระ- prefixes) for divine and royal referents, and per RULES §0 takes the evangelical-consensus reading in the main text while keeping notes descriptive (not pastorally endorsing)._

---

## Item A — A *codified* first-person-plain rule for God's body-parts (arm / hand / eyes)

**The pattern:** The translation locks God's body-part anthropomorphisms to Thai royal register: divine arm זְרוֹעַ → **พระกร**, divine hand יָד → **พระหัตถ์**, divine eyes עֵינַי → **พระเนตร** (the doc `divine_anthropomorphism_thai_grammar_2026-05.md` states no person-based exception). In Jeremiah, **first-person divine speech ("my arm / my hand / my eyes") systematically drops to plain register** — and unlike Isaiah (where this was undocumented drift), the lapse is **argued into the `key_decisions` as a deliberate rule**:
- 21:5 KD: *"คำพูดบุรุษที่ 1 ของพระเจ้า … ใช้คำส่วนร่างกายแบบ 'ธรรมดา' (มือ/แขน) ไม่ใช่ราชาศัพท์ … ราชาศัพท์สงวนไว้สำหรับการพรรณนาบุรุษที่ 3."*

**Arm — same idiom, opposite register, split on grammatical person:**
- 32:17 (2nd-person, to God) HE `בִּזְרֹעֲךָ הַנְּטוּיָה` → TH `ด้วย**พระกร**ที่เหยียดออกของพระองค์` ✓ royal
- 32:21 (2nd-person) HE `וּבִזְרוֹעַ נְטוּיָה` → TH `**พระหัตถ์**อันเข้มแข็งและ**พระกร**ที่เหยียดออก` ✓ royal
- **21:5 (1st-person, drift)** HE `בְּיָד נְטוּיָה וּבִזְרוֹעַ חֲזָקָה` → TH `ด้วย**มือ**ที่เหยียดออกและ**แขน**อันแข็งแกร่ง`
- **27:5 (1st-person, drift)** HE `וּבִזְרוֹעִי הַנְּטוּיָה` → TH `และ**แขน**ที่เหยียดออกของเรา`

**Hand — not even internally consistent under the stated rule:**
- 15:6 (1st-person, yet royal) HE `וָאַט אֶת־יָדִי עָלַיִךְ` → TH `เราจึงเหยียด**พระหัตถ์**ออกต่อสู้เจ้า`
- **6:12 (1st-person, drift)** HE `כִּי־אַטֶּה אֶת־יָדִי` → TH `เราจะเหยียด**มือ**ของเราออก`
- **51:25 (1st-person, drift)** HE `וְנָטִיתִי אֶת־יָדִי עָלֶיךָ` → TH `เราจะเหยียด**มือ**ของเราออกต่อสู้เจ้า`

The *exact same idiom* "I stretch out my hand against you" is **พระหัตถ์** at 15:6 but **มือ** at 6:12 / 51:25.

**Eyes:** 24:6 `וְשַׂמְתִּי עֵינִי עֲלֵיהֶם` ("I will set my eyes on them") → `เราจะ**จับตาดู**พวกเขา` (idiom flattened); "evil in my eyes" split **สายตา** (7:30, 32:30, 34:15) vs **สายพระเนตร** (18:10).

The identical drift was flagged in the Isaiah audit (ISA §13), which recommended **reversal**; Jeremiah has since argued it into the KDs as intentional, producing same-idiom register splits that are internally inconsistent.

**Two questions:**
1. Should God's first-person self-reference to his own arm/hand/eyes ("my arm / my hand / my eyes") take **plain** Thai register, or the **royal** register (ราชาศัพท์) the corpus locks for divine body-parts? Is there a sound Thai-grammar or theological basis for a *grammatical-person* exception (1st-person plain, 2nd/3rd-person royal), or does that produce an incoherent surface (พระหัตถ์ at 15:6 but มือ at 6:12 for the identical clause)?
2. If a first-person-plain rule is adopted, how should the internal inconsistencies (15:6 พระหัตถ์, 18:10 สายพระเนตร) be resolved — and should it be applied retroactively to Isaiah (51:5/51:9/63:5 arm; 42:1/44:3/59:21 Spirit) so the whole corpus is consistent before Ezekiel (which is saturated with first-person divine body-part speech)?

---

## Item B — Foreign-monarch register: Nebuchadnezzar in plain register (vs Daniel's royal register for the same king)

**The pattern:** The project's policy (`ot_register_policy §2.2`) gives foreign emperors full Thai royal register (ราชาศัพท์: ทรง/พระองค์/เสด็จ/ตรัส) **even if villainous**, and the already-audited **Daniel applies this to all four of its foreign emperors**. **Jeremiah does not:** across chapters 1–51 the king of Babylon, Nebuchadnezzar, receives **plain** register, codified as an "invader → plain" rule:
- 21:2 KD: *"กษัตริย์บาบิโลนผู้รุกราน → ทะเบียนธรรมดา (ผู้รุกราน ไม่ใช่บริบทราชกิจที่ผู้เล่าเชิดชู)."*
- 39:1 TH `เนบูคัดเนสซาร์ … ยกมาสู้รบ … และล้อมเมืองไว้` (plain) — contrast Daniel 1:1 `ทรงยกทัพ … ทรงล้อม` for the same action.

**The same king is therefore plain in Jeremiah but royal in Daniel.** And Jeremiah contradicts itself:
- **39:11** (Nebuchadnezzar protecting Jeremiah) TH `เนบูคัดเนสซาร์ … ได้**ทรง**บัญชา` — royal, KD: *"แม้ผู้พิชิตยังให้เกียรติ"* (royal register granted because the scene frames him favorably).
- **52:31–32** (the 2 Kings 25 appendix) — full royal for the Babylonian king Evil-merodach: `ได้**ทรงพระกรุณา**ปล่อย … ปีที่**พระองค์**ขึ้นครองราชย์ … **พระองค์ตรัส** … ด้วย**พระเมตตา** และ**ทรงตั้งบัลลังก์**.`

The theological tension of YHWH calling a pagan king **"my servant" (עַבְדִּי)** — 25:9, 27:6, 43:10, all → **ผู้รับใช้ของเรา**, the same word used for prophets/Israel — is handled well and *descriptively* (KD names him "เครื่องมือพิพากษาในพระหัตถ์พระเจ้า," God's instrument of judgment). But the translator cites the "servant = mere instrument, not honored" framing as part of the *rationale for withholding the royal register* — which is the crux of the divergence from §2.2.

The governing doc `foreign_monarch_register` does not yet exist (deferred since the Ezra audit).

**Two questions:**
1. Should a hostile conqueror-emperor (Nebuchadnezzar, Pharaoh Hophra) receive full Thai royal register (ราชาศัพท์) in narrator voice — matching Daniel and §2.2's "even if villainous" rule — or is a documented "hostile-invader downshift" to plain register defensible? Note the same king Nebuchadnezzar currently reads plain in Jeremiah but royal in Daniel.
2. Does YHWH's calling Nebuchadnezzar "my servant" (עַבְדִּי, 25:9/27:6/43:10 → ผู้รับใช้ของเรา) legitimately *lower* his royal register, or are the two questions independent (instrument-theology in the notes, royal register in the narrator voice regardless)? And how should Jeremiah's internal split — plain in chs 1–51 vs royal at 39:11 and in ch.52 — be reconciled?

---

## Item C — MT-vs-LXX: the OT's largest textual divergence is documented only in internal (non-reader-facing) notes

**The pattern:** Jeremiah's Masoretic Text is ~1/8 *longer* than the Septuagint, which also relocates the Oracles Against the Nations (chs 46–51 in MT) to after 25:13. The project correctly translates the MT surface throughout. But the divergence is documented **only in `key_decisions` and `notes`, which are never shown to readers** — every one of the 52 reader-facing `textual_variants` files carries only the Tetragrammaton footnote, there is no book-level prefatory note, and there are no chapter-footer anchors for the reorder or the MT-plus passages:
- **33:14–26** — the longest MT plus (the Branch + Davidic/Levitical-covenant oracle), entirely absent from the LXX; reader sees only one inline summary line on v.14, no footer; vv.15–26 silent.
- **10:11, 29:16–20, 39:4–13, 52:28–30** — MT material absent from LXX; KD/notes only (52:28–30 is KD-only, not even in notes).

**The sharpest single case — 31:32, where the NT itself follows the LXX against the MT surface the project ships:**
- 31:32 HE `אֲשֶׁר־הֵמָּה הֵפֵרוּ אֶת־בְּרִיתִי וְאָנֹכִי בָּעַלְתִּי בָם` ("…though **I was a husband** to them") → TH (MT) `แม้เราเป็นเหมือน**สามี**ของพวกเขา`
- Hebrews 8:9 (shipped) quotes the LXX `κἀγὼ ἠμέλησα αὐτῶν` ("and **I disregarded** them") → TH `และเราก็**มิได้เอาใจใส่**พวกเขา`

A reader comparing Jeremiah 31:32 with the shipped Hebrews 8:9 hits a flat contradiction (husband vs disregarded). The 31:32 KD identifies this but it is not in a reader-facing footer. Under the project's own `mt_vs_lxx §2.3` disclosure floor (an NT-cited LXX variant is "canonically visible"), this is the one footer the policy obligates.

**Two questions:**
1. For a Masoretic-base translation, is it sufficient to keep Jeremiah's macro LXX-divergence (the shorter LXX, the OAN reorder, the absent passages 33:14–26 etc.) in internal translator notes only — or should there be a reader-facing book-level prefatory note plus chapter-footer anchors at the key divergence points (25, 33, 39, 52, the OAN head 46)?
2. Specifically at 31:32, should a reader-facing footnote record that Hebrews 8:9 quotes the LXX reading ("I disregarded them") against the Masoretic "I was a husband to them" that the main text follows — given that a reader comparing the two shipped passages will otherwise see a contradiction?

---

## Item D — Messianic "Branch" oracles: committal surface, register, and the YHWH-our-Righteousness name-title

**The pattern:** Jeremiah's Davidic-messianic oracles take the evangelical-consensus reading in the main text while keeping notes descriptive (the same policy the Isaiah audit examined). The "Righteous Branch" צֶמַח is rendered **หน่ออันชอบธรรม** (byte-consistent with the locked Isaiah 11:1 Branch), and the name-title יְהוָה צִדְקֵנוּ is rendered as a transliterated proper name + gloss:
- 23:6 HE `יְהוָה צִדְקֵנוּ` → TH `**ยาห์เวห์ซิดเคนู** (องค์พระผู้เป็นเจ้าทรงเป็นความชอบธรรมของเรา)` ("Yahweh-Tsidkenu (the LORD is our righteousness)")
- 33:16 — byte-identical title, correctly noting the subject shifts from the *king* (23:6) to the *city* Jerusalem (33:16, feminine).

**A register asymmetry in the byte-parallel pair:**
- 23:5 HE has `וּמָלַךְ מֶלֶךְ` ("he will **reign as king**") → TH gives the Branch full **royal** register: `**พระองค์**จะ**ทรงครองราชย์**เป็นกษัตริย์`
- 33:15 omits the kingship verb → TH keeps **plain** register: `และ**ท่าน**จะให้ความยุติธรรม`

The split is Hebrew-anchored (kingship verb present vs absent) and mirrors Isaiah's birth-frame/reign-frame gradation, but the 33:15 KD does not explain the downshift.

**A summary line to confirm:** the new-covenant `thai_summary` at 31:31 reads *"…อ้างอิงเต็มใน ฮีบรู 8:8–12 และ 10:16–17 ว่า**สำเร็จในพระคริสต์**"* ("cited in full in Heb 8/10 as **fulfilled in Christ**") — framed as a report of what Hebrews does, but the closest Jeremiah comes to a doctrinally-forward summary (parallel to the line the Isaiah audit flagged at Isa 9:6).

**Two questions:**
1. Is the Branch handling sound — צֶמַח → หน่ออันชอบธรรม (byte-shared with Isaiah 11), the name יְהוָה צִדְקֵנוּ transliterated + glossed rather than translated, and full royal register only where the Hebrew explicitly says "he will reign" (23:5) vs plain register where it does not (33:15)? Should the 23:5/33:15 register difference be documented so the byte-parallel pair doesn't read as an inconsistency?
2. Does the 31:31 summary's *"fulfilled in Christ"* clause stay within "describe, don't endorse" (it reports the use Hebrews makes of the text), or does it cross into pastoral endorsement that belongs only in a footnote?

---

## Item E — "Lord GOD of hosts" (אֲדֹנָי יְהוִה צְבָאוֹת): inconsistent Adonai-marking

**The pattern:** The bare compound אֲדֹנָי יְהוִה ("Lord GOD") collapses mid-sentence to a single **องค์พระผู้เป็นเจ้า** (Adonai dropped) — the project's locked rule. For the triple-stack אֲדֹנָי יְהוִה צְבָאוֹת ("Lord GOD of hosts") Jeremiah is split:
- **Drops Adonai → องค์พระผู้เป็นเจ้าจอมโยธา:** 2:19
- **Marks Adonai → องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านายจอมโยธา:** 46:10 (×2), 49:5, 50:25, 50:31

Since 5 mark and only 1 drops, the doc-conformant 2:19 is the outlier; the consistent pattern is that the Oracles-Against-the-Nations climactic-judgment formulas mark Adonai (possibly an intentional emphasis convention). Separately, the oath at **44:26** HE `חַי־אֲדֹנָי יְהוִה` → TH `**องค์เจ้านายพระผู้เป็นเจ้า**ทรงพระชนม์อยู่แน่ฉันใด` marks Adonai where the bare compound elsewhere drops it — defensible as an audible distinction from the bare oath חַי־יְהוָה (องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่), but inconsistent with the drop-Adonai rule.

**Question:** Should the "Lord GOD of hosts" triple-stack drop Adonai everywhere (normalize 46:10/49:5/50:25/50:31 to องค์พระผู้เป็นเจ้าจอมโยธา, matching 2:19 and the mid-sentence rule) — or is marking Adonai (ผู้ทรงเป็นเจ้านาย) a justified emphasis in the Oracles-Against-the-Nations judgment formulas, in which case 2:19 should be normalized to match and the split documented? And should the 44:26 oath compound (องค์เจ้านายพระผู้เป็นเจ้า) follow the same decision?

---

## Item F — Jeremiah 31:22 crux ("a woman shall encompass a man") — interpretive note not reader-facing

**The pattern:** The famously obscure crux נְקֵבָה תְּסוֹבֵב גָּבֶר is rendered literally and its polysemy preserved, with the historic readings named *descriptively* in the internal `key_decisions`:
- 31:22 HE `כִּי־בָרָא יְהוָה חֲדָשָׁה בָּאָרֶץ נְקֵבָה תְּסוֹבֵב גָּבֶר` → TH `เพราะองค์พระผู้เป็นเจ้าได้ทรงสร้างสิ่งใหม่ขึ้นในแผ่นดิน คือ**ผู้หญิงจะโอบล้อมผู้ชาย**`
- KD: *"…ความหมายไม่แน่ชัด (การกลับด้านบทบาท / อิสราเอลปกป้อง / **การตีความเชิงเมสสิยาห์ในบางจารีต**) แปลตามอักษรฮีบรู คงความกำกวมไว้ มิได้บังคับการตีความเดียว"* (names the role-reversal, Israel-protects, and the messianic/Marian reading-families, foreclosing none).

The handling matches the project's crux policy *in substance*, but the note lives only in the (reader-invisible) `key_decisions`. The comparable Genesis cruxes (Gen 3:15 protoevangelium, Gen 3:16) each received a reader-facing Layer-2 footnote (`textual_variants`); `textual_variants/jeremiah_31.json` carries only divine-name boilerplate.

**Question:** Should Jeremiah 31:22 carry a reader-facing footnote presenting the crux and its main reading-families (role-reversal / Israel-encompasses-warrior / the historic messianic-Marian reading) — consistent with the Layer-2 footers given to the Genesis 3:15/3:16 cruxes — or is internal-notes-only documentation sufficient for an interpretive (non-textual) crux of this kind?

---

## Item G — "den of robbers" (Jer 7:11): the shipped Matthew disagrees with Jeremiah/Mark/Luke

**The pattern:** Jesus quotes Jeremiah 7:11 at the temple cleansing in all three Synoptics with identical Greek (σπήλαιον λῃστῶν). Jeremiah was rendered to match the shipped Mark/Luke, but Matthew shipped a different word:
- Jer 7:11 → **ถ้ำของโจร** (KD: "rendered to match shipped Mark 11:17")
- Mark 11:17 → **ถ้ำของโจร** ✓ — Luke 19:46 → **ถ้ำของโจร** ✓
- **Matthew 21:13 → ซ่องของพวกโจร** ✗ (lone outlier; ซ่อง "den/lair" + พวกโจร)

A reader comparing Jeremiah 7:11 → Matthew 21:13 sees ถ้ำ vs ซ่อง for the same quoted clause. This is a within-NT inconsistency the Jeremiah ship surfaced rather than caused (the Jeremiah analogue of Isaiah's 53:1 retro-candidate).

**Question:** Should the shipped Matthew 21:13 be normalized from ซ่องของพวกโจร to ถ้ำของโจร to match Jeremiah 7:11 / Mark 11:17 / Luke 19:46 (an NT-side fix via a staged re-audit), or is Matthew's distinct wording defensible — and if normalized, which surface should be canonical across all four loci?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
