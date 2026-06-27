# Ecclesiastes — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Ecclesiastes** (12 chapters, 222 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job complete (not yet tagged). Ecclesiastes 12/12 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Ecclesiastes — External Review Items

Handwritten items for the external-AI review packet (consumed by
`scripts/build_external_review_packet.py ECC`). One block per REVIEW/DECIDE
item from `ECC_END_OF_BOOK_REVIEW_2026-06-04.md`. Each ends with a
`**Question:**` / `**Two questions:**` block that becomes a YAML reviewer question.

---

## Item A — הֶבֶל *hevel*, the book's leitwort: ไร้แก่นสาร vs อนิจจัง vs contextual (the single decision that defines the Thai Ecclesiastes)

**The pattern:** *hevel* ("vapor / breath / fleeting nothing") is the keyword of Ecclesiastes — it appears in **30 verses** (≈38 tokens with in-verse repeats), framing the whole book in an inclusio: 1:2 opens and 12:8 closes with the identical superlative הֲבֵל הֲבָלִים ("vanity of vanities"). The Thai renders all 30 verses with **one fixed word, ไร้แก่นสาร** ("without lasting core/substance"), to preserve that refrain. This shipped **PROVISIONAL** — a reader-panel verdict was still pending at book completion.

| Verse | Hebrew | Thai | English (BSB) |
|---|---|---|---|
| ECC 1:2 (inclusio open) | הֲבֵל הֲבָלִים ... הַכֹּל הָבֶל | "**ไร้แก่นสารที่สุด**" ... "ทุกสิ่งล้วน**ไร้แก่นสาร**" | "Vanity of vanities... everything is futile" |
| ECC 1:14 | הַכֹּל הֶבֶל וּרְעוּת רוּחַ | ทุกสิ่งล้วน**ไร้แก่นสาร** เป็นการไล่ตามลม | "all... futile, a pursuit of the wind" |
| ECC 2:11 | הַכֹּל הֶבֶל וּרְעוּת רוּחַ | ทุกสิ่งล้วน**ไร้แก่นสาร** เป็นการไล่ตามลม | "everything... futile, a pursuit of the wind" |
| ECC 6:12 | חַיֵּי הֶבְלוֹ | ชีวิตอัน**ไร้แก่นสาร**ของเขา | "his fleeting life" |
| ECC 12:8 (inclusio close) | הֲבֵל הֲבָלִים ... הַכֹּל הָבֶל | "**ไร้แก่นสารที่สุด**" ... "ทุกสิ่งล้วน**ไร้แก่นสาร**" | "Vanity of vanities... everything is futile" |

**Why ไร้แก่นสาร and not อนิจจัง:** The most familiar Thai word for "transience" is อนิจจัง — but that is the Buddhist term *anicca* (one of the three marks of existence), and importing it would re-frame Solomon's God-centered reflection inside a Buddhist doctrinal category. Across **33 prior *hevel* verses elsewhere in the corpus** (Psalms, Proverbs, Job), the project has *never once* used อนิจจัง, rendering contextually instead (ลมหายใจ Ps 144:4, ไอหมอก Prov 21:6, เปล่าประโยชน์ Job, ไร้สาระ Ps 94:11, ไม่จีรัง Prov 31:30, มายา Ps 62:10). ไร้แก่นสาร continues that avoidance **and** gains a single recognisable refrain the scattered renderings could not provide. The cost: ไร้แก่นสาร is a coined, slightly abstract compound ("core-less"), less immediately emotive than อนิจจัง or the older ฉบับแปลไทย อนิจจัง/อนิจจา.

**The three options on the table:**
1. **อนิจจัง** — traditional, instantly recognisable to Thai readers, but Buddhist-loaded (*anicca*).
2. **ไร้แก่นสาร** — non-Buddhist, preserves the 30-verse refrain (the shipped provisional).
3. **Contextual** per-verse (ลมหายใจ / ไอหมอก / เปล่าประโยชน์ ...) — natural locally, but destroys the inclusio and the book's signature repetition.

**Question:** For a Thai evangelical-Protestant Bible, which rendering best serves Ecclesiastes' *hevel* — (1) อนิจจัง (familiar but Buddhist-loaded), (2) ไร้แก่นสาร (non-Buddhist, preserves the 30-verse refrain), or (3) per-verse contextual rendering? Specifically: is the avoidance of อนิจจัง the right call for a God-centered Wisdom text, and is ไร้แก่นสาร natural enough to carry a refrain a Thai reader will hear 30 times?

---

## Item B — מִקְרֶה *miqreh* → เหตุอย่างเดียวกัน: avoiding ชะตากรรม (*karma*-freighted "fate")

**The pattern:** *miqreh* ("what befalls, fate, chance-event," 7×: 2:14-15, 3:19, 9:2-3) is rendered with the neutral **เหตุ(อย่างเดียวกัน)** — "the same thing happens to" — rather than **ชะตากรรม** ("fate/destiny"), the natural Thai word, which carries *karma* (กรรม) freight. This is a second, parallel anti-Buddhist register choice alongside *hevel* (Item A).

- ECC 3:19 HEB: `מִקְרֶה בְנֵי־הָאָדָם וּמִקְרֶה הַבְּהֵמָה וּמִקְרֶה אֶחָד לָהֶם` → TH: `เหตุที่เกิดแก่บุตรของมนุษย์ก็เกิดแก่สัตว์ เป็น**เหตุอย่างเดียวกัน**` (EN: "the fates of both men and beasts are the same")
- ECC 9:2 HEB: `מִקְרֶה אֶחָד לַצַּדִּיק וְלָרָשָׁע` → TH: `**เหตุอย่างเดียวกัน**เกิดแก่คนชอบธรรมและคนชั่วร้าย` (EN: "a common fate for the righteous and the wicked")
- ECC 9:3 HEB: `כִּי־מִקְרֶה אֶחָד לַכֹּל` → TH: `**เหตุอย่างเดียวกัน**เกิดแก่ทุกคน` (EN: "one fate for everyone")

**The tradeoff:** เหตุอย่างเดียวกัน is more neutral/flatter than the fatalistic weight of the Hebrew *miqreh*, but it refuses to import *karma*. ชะตากรรม would read more naturally and ominously but would smuggle a Buddhist/Hindu causation concept into a text whose whole point (12:14) is that God, not impersonal karma, judges every deed.

**Question:** Is rendering *miqreh* as the neutral เหตุอย่างเดียวกัน ("the same thing happens") — deliberately avoiding the natural-but-*karma*-freighted ชะตากรรม — the right register for a God-centered text, even though it loses some of the Hebrew's fatalistic force? Should this be locked as the same principle that governs the *hevel* / อนิจจัง avoidance (Item A)?

---

## Item C — ECC 3:11 הָעֹלָם → นิรันดร์กาล ("He has set eternity in their hearts"): a three-way lexical crux

**The pattern:** הָעֹלָם at 3:11 is one of the most debated single words in Ecclesiastes, read three ways: (a) "**eternity**" (a sense of the timeless / the everlasting), (b) "**the world**," or (c) "**what is hidden** / the hidden whole." The Thai chose (a), **นิรันดร์กาล** ("eternity / everlastingness"):

- ECC 3:11 HEB: `אֶת־הַכֹּל עָשָׂה יָפֶה בְעִתּוֹ גַּם אֶת־הָעֹלָם נָתַן בְּלִבָּם מִבְּלִי אֲשֶׁר לֹא־יִמְצָא הָאָדָם אֶת־הַמַּעֲשֶׂה אֲשֶׁר־עָשָׂה הָאֱלֹהִים מֵרֹאשׁ וְעַד־סוֹף`
- TH: `พระองค์ทรงทำให้ทุกสิ่งงดงามตามวาระของมัน ทั้งทรงตั้ง**นิรันดร์กาล**ไว้ในใจของพวกเขา แต่มนุษย์ก็ยังหยั่งไม่ถึงพระราชกิจที่พระเจ้าทรงกระทำตั้งแต่ต้นจนจบ`
- EN (BSB): "He has made everything beautiful in its time. He has also set **eternity** in the hearts of men, yet they cannot fathom the work that God has done from beginning to end."

**The case for "eternity":** the verse's own frame — מֵרֹאשׁ וְעַד־סוֹף "from beginning to end" (ต้นจนจบ) — is a temporal-totality phrase, and "eternity" matches NIV/ESV/CSB/standard Thai. **The case against:** the same consonants can mean "the world" (so some read "He has put a sense of the world/cosmos in their hearts"), and a minority emend to הֶעְלֵם "obscurity / the hidden." The Thai closes these options.

**Question:** Is rendering 3:11 הָעֹלָם as นิรันดร์กาล ("eternity") — over "the world" or "the hidden" — the right reading for an evangelical-Protestant Thai Bible, given the "from beginning to end" temporal frame in the same verse? Or should the rendering signal the crux (e.g. a footnote) rather than resolve it silently?

---

## Item D — ECC 7:26-28: the "snare-woman" passage — faithful rendering, trope-scoped notes

**The pattern:** Qoheleth's harshest lines about women — "more bitter than death is the woman who is a snare" (7:26) and "among all these I have not found one [upright] woman" (7:28) — are rendered **faithfully and unsoftened** in the Thai verse text, with the interpretive scoping (this is a wisdom-literature trope, not a universal verdict on women) placed **only in the translator notes**, cross-referenced to 9:9's positive marriage counterpart.

- ECC 7:26 HEB: `וּמוֹצֶא אֲנִי מַר מִמָּוֶת אֶת־הָאִשָּׁה אֲשֶׁר־הִיא מְצוֹדִים וַחֲרָמִים` → TH: `ข้าพเจ้าพบว่า สิ่งที่ขมขื่นยิ่งกว่าความตายคือ**ผู้หญิงที่ใจของนางเป็นบ่วงแร้วและตาข่าย**` (EN: "more bitter than death the woman who is a snare")
  - Note: *"ภาพ 'หญิงบ่วงแร้ว' ต่อสายวรรณกรรมปัญญา (เทียบ Prov 5, 7) — เป็นรูปจำเพาะ ไม่ใช่คำกล่าวรวมถึงสตรีทั้งปวง (ดู 9:9 คู่ตรงข้าม)."* ("the snare-woman image continues the wisdom-literature line, cf. Prov 5, 7 — a specific figure, not a statement about all women; see 9:9 for the counterpart")
- ECC 7:28 HEB: `אָדָם אֶחָד מֵאֶלֶף מָצָאתִי וְאִשָּׁה בְכָל־אֵלֶּה לֹא מָצָאתִי` → TH: `ในพันคนข้าพเจ้าพบชายเที่ยงตรงคนหนึ่ง แต่ในคนทั้งปวงเหล่านี้ ข้าพเจ้าไม่พบหญิงสักคน` (EN: "among a thousand I have found one upright man, but among all these not one [such] woman")
  - Note: scopes the claim to "the thousand" Qoheleth surveyed, not a universal pronouncement on women.
- ECC 9:9 (the intended balancing context) — "enjoy life with the wife whom you love" → rendered as a positive marriage counterpart.

**The architecture:** the rendered verse keeps the MT's force (no euphemism, no omission — the corpus's fidelity rule); the de-universalising interpretation lives in notes, not in the text. The risk: a lay Thai reader meeting 7:26-28 cold could read a misogynistic universal that the wisdom-genre context does not intend.

**Question:** Is the architecture correct — translate 7:26-28 faithfully and unsoftened, keeping the "this is a wisdom-trope, not a universal claim about women" scoping in translator notes plus the 9:9 cross-reference — or should something reader-facing (a footnote in the published text) accompany these verses so the trope-scope reaches the lay reader, not just the editor?

---

## Item E — MT-anchored word-variants at 2:25 and 8:10 (following the Masoretic Text against the BSB base)

**The pattern:** At two verses the Thai follows the **Masoretic Text** where the BSB English base reflects a different (LXX-ward or emended) reading. Both are **word-level** variants (a pronoun; a verb root) — not whole-verse inclusion variants — and both are documented in the verse's `key_decisions`.

| Verse | MT (→ Thai) | BSB base | Hebrew |
|---|---|---|---|
| ECC 2:25 | "apart from **me**" → นอกเหนือไปจาก**ข้าพเจ้า** | "apart from **Him**" (LXX/some MSS) | `חוּץ מִמֶּנִּי` (MT: *mimmenni* "from me") |
| ECC 8:10 | "they were **forgotten**" → **ถูกลืม** | "they were **praised**" (variant ישתבחו) | `וְיִשְׁתַּכְּחוּ` (MT: *yishtakkəḥu* "be forgotten") |

- ECC 2:25 TH: `เพราะใครเล่าจะกินได้ หรือใครเล่าจะหาความชื่นชมยินดีได้ **นอกเหนือไปจากข้าพเจ้า**` — KD: *"MT: 'นอกจากข้าพเจ้า' (ปัญญาจารย์ผู้มีทุกสิ่ง) — BSB แปลตามสาย LXX ว่า 'นอกจากพระองค์' (พระเจ้า)."*
- ECC 8:10 TH: `และพวกเขาก็**ถูกลืม**ไปในเมืองที่พวกเขาเคยทำเช่นนั้น นี่ก็ไร้แก่นสารเช่นกัน` — KD: *"MT: 'ถูกลืม' — BSB/บางฉบับอ่านตามสายแปรว่า 'ได้รับการสรรเสริญ'."*

**The policy question:** the corpus base text is the MT (per `ot_canon_and_text_base_2026-05.md`), and `mt_vs_lxx_textual_variant_handling_2026-05.md` governs these. Because they are word-level (not whole-verse absence/inclusion variants), the §2.3 inclusion-variant floor says **no `textual_variants/ecclesiastes_*.json` file is owed** — and none exists; the documentation lives in the verse KDs. This matches the 2 Kings / Daniel audit precedent where MT/LXX word-variants were ruled §2.3 non-gaps.

**Question:** Is MT-anchoring at 2:25 ("apart from me," not "apart from Him") and 8:10 ("forgotten," not "praised") correct for an MT-base Thai Bible, and is verse-level `key_decisions` documentation sufficient — i.e. confirm ECC owes **no** `textual_variants` JSON files, since these are word-level variants below the whole-verse inclusion-variant floor?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
