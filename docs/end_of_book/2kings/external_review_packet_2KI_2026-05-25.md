# 2 Kings — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-25**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **2 Kings** (25 chapters, 719 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). 2 Kings 25/25 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Baal-zebub `พระ`-register: the lone foreign-deity exception in 2 Kings

**The pattern:** `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` apply an OT `พระ`/`เทพ`/`เทพี` register to literal pagan deities (proper-noun gods take the `พระ` prefix; `เทพ`/`เทพี` carry the descriptor; the supreme `พระเจ้า` is reserved for YHWH/Elohim). 2 Kings applies this **uniformly to every foreign deity — except one.** `บาอัลเซบูบ` of Ekron ships *bare* (no `พระ`):

| Deity | Hebrew | 2KI Thai | `พระ`? |
|---|---|---|---|
| Baal (Israelite cult) | בַּעַל | **`พระบาอัล`** | ✓ |
| Succoth-benoth, Nergal, Ashima | (ch 17) | `พระสุคโคทเบโนท`, `พระเนอร์กัล`, `พระอาชิมา` | ✓ |
| Nibhaz, Tartak, Adrammelech, Anammelech | (ch 17) | `พระนิบหัส`, `พระทารทัก`, `พระอัดรัมเมเลค`, `พระอานัมเมเลค` | ✓ |
| Nisroch | נִסְרֹךְ | `พระนิสรอค` | ✓ |
| Molech | מֹלֶךְ | `พระโมเลค` | ✓ |
| Ashtoreth / Chemosh | עַשְׁתֹּרֶת / כְּמוֹשׁ | `พระอัชเทเรท…` / `พระเคโมช…` | ✓ |
| **Baal-zebub** | **בַּעַל זְבוּב** | **`บาอัลเซบูบ เทพเจ้าแห่งเอโครน`** | **✗** |

**Sample verses:**
- **1:2 HEB:** `דִּרְשׁוּ בְּבַעַל זְבוּב אֱלֹהֵי עֶקְרוֹן` → **TH:** "จงไปสอบถาม**บาอัลเซบูบ เทพเจ้าแห่งเอโครน** ว่าเราจะหายจากอาการบาดเจ็บนี้หรือไม่"
- **1:3 HEB:** `הֲמִבְּלִי אֵין־אֱלֹהִים בְּיִשְׂרָאֵל אַתֶּם הֹלְכִים לִדְרֹשׁ בְּבַעַל זְבוּב` → **TH:** "เพราะในอิสราเอลไม่มี**พระเจ้า**หรือ พวกเจ้าจึงจะไปสอบถาม**บาอัลเซบูบ เทพเจ้าแห่งเอโครน**?"
- **17:31 HEB (contrast):** the Sepharvites *burned their children in the fire* to → **TH:** "เผาบุตรของตนในไฟบูชา**พระอัดรัมเมเลคและพระอานัมเมเลค**" — the child-sacrifice gods keep `พระ`.

**Editorial context:** The bare form **does** carry a verse-level rationale (1:2 `key_decisions`): the deliberate `אֱלֹהֵי` → **`เทพเจ้า`** (not `พระเจ้า`, "reserved for YHWH") is "the heart of the chapter" — the YHWH-vs-Baal-zebub polemic of "is there no God in Israel?" (vv 3, 6, 16) — and the consultation verb is deliberately plain `สอบถาม` (not the deferential `ทูลถาม` used for inquiring of YHWH). That `เทพเจ้า`-vs-`พระเจ้า` contrast is principled and well-documented. **What is *not* explained is the `พระ`-drop on the proper noun itself**: the rationale even cites `เทียบ พระบาอัล 1 พงศ์กษัตริย์ 16:31` (it knew the `พระบาอัล` form) yet rendered `บาอัลเซบูบ` bare. So Baal-zebub is the lone exception to an otherwise-exceptionless `พระ`+proper-noun register across the whole book — including gods (Adrammelech/Anammelech) every bit as contemptible as the Ekron oracle.

**Question:** Is the bare `บาอัลเซบูบ` (a) a *deliberate further deprecation* of the Ekron oracle-god — distinct from the established Israelite-apostasy cult `พระบาอัล` — that should be **documented** as an intentional carve-out in `pagan_deities_2026-04.md`? Or (b) an inadvertent `พระ`-drop that rode along with the (correct) `เทพเจ้า` decision, and should **normalize** to `พระบาอัลเซบูบ` for register consistency with `พระบาอัล` and every other foreign deity in 2 Kings? If a deprecation carve-out is intended, what principled boundary distinguishes Baal-zebub from Adrammelech/Anammelech/Nisroch (who keep `พระ`) — foreign-oracle-being-consulted vs. foreign-god-being-worshipped?

---

## Item B — Adversary-speech register for a human imperial blasphemer (Rabshakeh, 2 Kings 18–19)

**The pattern:** `adversary_speech_register_2026-05.md` (LOCKED 2026-05-01) requires *neutral* speech-verbs for adversaries — never the deferential `ทูล` — and preserves divine honorifics *as content* even in an adversary's mouth (the demon at Mark 5:7 still gets `ร้องเสียงดังว่า` for its speech-stance, while `พระเยซูบุตรของพระเจ้า` is preserved as the quoted content). But the doc was written for **NT demons / the devil / false prophets**; its edge-cases name OT הַשָּׂטָן but **no human imperial blasphemer**. 2 Kings 18–19 (Rabshakeh / Sennacherib) is the corpus's **first sustained human imperial blasphemer taunting YHWH directly** — and it triggers a three-way register interaction:

| Speaker / referent | 2KI Thai register | Sample |
|---|---|---|
| **Rabshakeh** (envoy/official) → neutral speech-verbs | `กล่าวแก่` (18:19), `ตอบว่า` (18:27), `ร้องเสียงดัง` (18:28) | — |
| **The Assyrian "great king"** (a foreign monarch) → foreign-royal register | 18:19 "มหาราชา…**ตรัส**ดังนี้"; 18:28 "**พระดำรัส**ของมหาราชา"; 19:9 Sennacherib "**ทรง**ส่ง" | — |
| **YHWH** (mocked, inside the taunt) → divine honorific preserved as content | 18:35 "แล้ว**องค์พระผู้เป็นเจ้าจะทรงช่วยกู้**กรุงเยรูซาเล็ม…ได้อย่างไร?" | — |
| **Pagan "gods" of the nations** (in the taunt) → pagan register | 18:33 "มี**พระ**ของชนชาติใด…"; 18:34 "ไหนล่ะ**พระ**ของเมืองฮามัท…" | — |

- **18:35 HEB:** `מִי בְּכָל־אֱלֹהֵי הָאֲרָצוֹת … כִּי־יַצִּיל יְהוָה אֶת־יְרוּשָׁלִַם מִיָּדִי` → **TH:** "ในบรรดา**พระ**ของแผ่นดินทั้งหลาย…มีองค์ใดเคยช่วยกู้…บ้าง? แล้ว**องค์พระผู้เป็นเจ้าจะทรงช่วยกู้**กรุงเยรูซาเล็ม…ได้อย่างไร?" — the mocked YHWH keeps both the full divine name `องค์พระผู้เป็นเจ้า` and the royal-divine `ทรง`, while the pagan gods get `พระ`.
- **19:22 (YHWH's reply via Isaiah) HEB:** `אֶת־מִי חֵרַפְתָּ וְגִדַּפְתָּ … עַל־קְדוֹשׁ יִשְׂרָאֵל` → **TH:** "เจ้า**เย้ยหยันและหมิ่นประมาท**ผู้ใด?…ต่อ**องค์บริสุทธิ์แห่งอิสราเอล**น่ะสิ!"

**Editorial context:** The handling is consistent with the doc's *principle* — the adversary's *speech-stance* is neutral (envoy verbs `กล่าว`/`ตอบ`/`ร้อง`), while the divine referent keeps its honorific *as content*. It also correctly layers in the *separate* foreign-monarch royal register (`honorifics_non_divine_authorities_2026-04.md`): the Assyrian "great king" gets `ตรัส`/`พระดำรัส` as a head of state, while his envoy Rabshakeh does not. The configuration looks right — but it is **undocumented** for this class, and the interaction of three registers in one passage (envoy-neutral × foreign-king-royal × mocked-divine-honorific-as-content) has not been written down anywhere.

**Two questions:**
1. Is the within-quote handling correct for a *human* blasphemer — i.e., should the mocked YHWH retain the royal-divine `ทรง` (`องค์พระผู้เป็นเจ้าจะทรงช่วยกู้`, 18:35) even when the verb is voiced by a sneering Assyrian field commander, exactly as the corpus preserves `พระเยซูบุตรของพระเจ้า` in a demon's mouth? Or does a *human* mocker's stance argue for withholding `ทรง` from the hypothetical-deliverance verb inside the taunt (while keeping the divine name)?
2. Should `adversary_speech_register_2026-05.md` (or `ot_register_policy_2026-05.md`) gain a short **OT human-imperial-blasphemer** extension note documenting this three-way pattern, to forward-protect Sennacherib/the Chaldeans in Isaiah + Jeremiah and Belshazzar in Daniel — distinguishing the *royal* foreign king (royal speech-verbs) from his *envoy/official* (neutral speech-verbs) from the *mocked divine referent* (honorific-as-content)?

---

## Item C — MT/LXX inclusion-variant gap: a recurring DECIDE now in its third consecutive DtrH book

**The pattern:** Per `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md`, every corpus-significant MT-vs-LXX divergence should be explicitly dispositioned (Tier 1 phrase brackets / Tier 2 chapter-footer / Tier 3 ⟦double brackets⟧ / silent-omission per RULES §5). The 1SA audit (§17) and 1KI audit (§17) both flagged a **DECIDE**: the OT `output/textual_variants/<book>_NN.json` files carry only the YHWH first-occurrence footnote and **zero** textual-divergence entries. **2 Kings is the third consecutive DtrH book with the identical gap** — all 25 files contain only `tetragrammaton_convention_first_occurrence`.

**Honest sizing — 2 Kings is the low-acuteness end of this gap:**

| Book | MT/LXX divergence character | Tier-2 need |
|---|---|---|
| 1 Kings (3 Reigns) | **Macro-structural**: the two Miscellanies (3 Rgns 2:35a–o, 2:46a–l), the alternate Jeroboam narrative (12:24a–z), the MT 20↔21 chapter swap | HIGH (1KI §17 DECIDE) |
| **2 Kings (kaige section)** | **Translation-character** (kaige recension) + scattered verse-level pluses/minuses + the regnal-synchronism chronology crux (reign-lengths/co-regencies don't arithmetically reconcile) | LOW — *no* Miscellanies, *no* reordering |
| Jeremiah | LXX ~⅛ shorter; oracles-against-the-nations reordered | VERY HIGH (forthcoming) |
| Daniel | the Greek additions (Susanna, Bel, Prayer of Azariah) | HIGH (forthcoming) |

**Editorial context:** The shipped 2 Kings text follows MT throughout — defensible, matching `ot_canon_and_text_base_2026-05.md`'s MT-base policy — and 2 Kings has no macro-structural divergence demanding a reader note the way 1 Kings did. Re-flagging the identical DECIDE for a third straight book is itself the signal: the missing decision is not "write 2 Kings footers," it is a **one-time corpus policy** for when the Tier-2 obligation triggers.

**Two questions:**
1. Should the project adopt a standing corpus policy that the Tier-2 MT/LXX-divergence disclosure obligation triggers **only on macro-structural divergence** (1 Kings 3 Reigns; Jeremiah; Daniel) — formally accepting *silent MT-base adherence per RULES §5* for kaige-character / routine verse-level variants (2 Kings, much of Samuel) and **ending the per-book re-flagging**? Or should every MT-base OT book carry at least a brief book-level prefatory note ("follows MT; LXX differs in …"), in which case 2 Kings needs one short note (kaige character + the synchronism chronology crux)?
2. If the policy is "macro-structural only," is the regnal-**synchronism chronology** (the famously non-reconciling reign-length data in 2 Kings — a content feature, not a textual variant) worth a *separate* reader-facing note, given Thai evangelical + theological reviewers will notice the numbers don't add up? Or is that a study-Bible concern outside the CC0 translation's Tier-2 remit?

---

## Item D — "Until this day" leitwort: 2 Kings makes 1 Samuel the lone corpus outlier

**The pattern:** `leitwort_handling_policy_2026-05.md` does not yet lock a Thai surface for the Deuteronomistic refrain עַד הַיּוֹם הַזֶּה ("until this day"). The 1KI audit (§14) flagged a cross-book split. 2 Kings now renders it **uniformly `จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) — **10 occurrences**: 2:22, 8:22, 10:27, 14:7, 16:6, 17:23, 17:34, 17:41, 20:17, 21:15. That is the largest single-book witness in the corpus.

**Cross-book corpus picture (four DtrH books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× |
| **1 Samuel** | **`จนถึงวันนี้`** (bare) | 8× uniform — **outlier** |
| 1 Kings | `จนถึงทุกวันนี้` | 5× uniform |
| **2 Kings** | **`จนถึงทุกวันนี้`** | **10× uniform** |

- **17:23 sample HEB:** `וַיִּגֶל יִשְׂרָאֵל מֵעַל אַדְמָתוֹ אַשּׁוּרָה עַד הַיּוֹם הַזֶּה` → **TH:** "ชนอิสราเอลจึงถูกกวาดต้อน…ไปเป็นเชลยยังอัสซีเรียมา**จนถึงทุกวันนี้**"

**Editorial context:** Three of four Former-Prophets books now agree on `จนถึงทุกวันนี้`, and 2 Kings (10×) is the heaviest witness. 1 Samuel's 8× bare `จนถึงวันนี้` is now clearly the lone outlier. Internal 2 Kings uniformity is clean; the only open question is the cross-book lock + the 1 Samuel normalization.

**Question:** Should `leitwort_handling_policy_2026-05.md` now lock **`จนถึงทุกวันนี้`** as the canonical Former-Prophets surface for עַד הַיּוֹם הַזֶּה (on the JDG + 1KI + 2KI majority, 21 occurrences vs 1SA's 8), and schedule 1 Samuel's 8 bare `จนถึงวันนี้` occurrences for normalization in a cross-book pass? Or is the bare `จนถึงวันนี้` an acceptable free variant that does not warrant a corpus-wide surface lock?

---

## Item E — mal'akh human-messenger surface: cross-book convergence and within-book variance

**The pattern:** `malak_yhwh_2026-05.md` §4.4 places *human-messenger* מַלְאָךְ **outside** the divine-angel lock ("use the plain register `ผู้ส่งสาร` or `ทูต` as context requires"). The divine angel is locked (`ทูตสวรรค์`; 2 Kings ships 1:3/1:15/19:35 clean — not at issue here). The *human-messenger* surface, however, has drifted across books, and 2 Kings adds new data points:

| Ref | Context | 2KI Thai |
|---|---|---|
| **1:2, 1:3** | Ahaziah's messengers / "messengers of the king of Samaria" | **`ผู้ส่งสาร`** |
| **17:4** | Hoshea's envoys to So of Egypt | **`ทูต`** |
| **20:13** | the Babylonian envoys (Merodach-baladan) | **`คณะทูต`** |

- **1:3 sample:** "…ไปพบ**ผู้ส่งสาร**ของกษัตริย์แห่งสะมาเรีย…"
- **17:4 sample:** "…คือส่ง**ทูต**ไปหาโสกษัตริย์แห่งอียิปต์…"

**Editorial context:** Encouragingly, 2 Kings 1:2/1:3 ships **`ผู้ส่งสาร`** — the exact surface the 1KI §3b audit recommended as the canonical cross-book form (over 1SA's `ผู้ส่งสาร`/`ผู้ส่งข่าว` and 1KI's `ผู้สื่อสาร`). But 2 Kings then uses `ทูต` (17:4) and `คณะทูต` (20:13) for other human envoys, and `ผู้สื่อสาร` reappears at 19:23 (inside Sennacherib's quoted poetic taunt). Across JDG/1SA/1KI/2KI the corpus now carries **`ผู้ส่งสาร` / `ผู้ส่งข่าว` / `ผู้สื่อสาร` / `ทูต` / `คณะทูต`** for the identical human-messenger lemma. None is *wrong* (the lemma is outside the lock), but the surface is unstable.

**Question:** Should the corpus standardize a single narrative surface for human-messenger מַלְאָךְ — recommend **`ผู้ส่งสาร`** (widest footprint; already used at 2 Kgs 1:2/1:3, and the 1KI-recommended form) — folding 17:4 `ทูต` / 20:13 `คณะทูต` and the cross-book JDG/1SA/1KI variants into one normalization pass? Or is human-messenger surface variation acceptable as context-sensitive (e.g., `คณะทูต` legitimately marks a *diplomatic delegation* at 20:13, vs. a single `ผู้ส่งสาร` runner at 1:2), in which case the variation should be *documented as principled* rather than normalized away?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
