## Item A — Spirit-of-YHWH empowerment book-wide drift (HIGHEST severity; first lock-vs-shipped corpus divergence)

**The pattern:** A locked corpus doc (`docs/translator_decisions/spirit_of_yhwh_empowerment_2026-05.md`, finalized 2026-05-20 — two days before this audit, after the Judges end-of-book audit) requires every Spirit-of-YHWH empowerment occurrence to render as **`พระวิญญาณขององค์พระผู้เป็นเจ้า…`** (with the **พระ** honorific on Spirit). The צָלַח-verb class additionally requires the adverbial **`อย่างทรงพลัง`** (rushed-upon-with-power). The lock explicitly cites "forward-protect 1 SAM 10:6, 10:10, 11:6, 16:13 (Saul + David)" in its §1.1 row for צָלַח.

**1 Samuel ships 12 Spirit-occurrences that ALL drift from this lock.** All 12 use bare `วิญญาณ` (no พระ honorific); the 4 צָלַח-class verses drop the locked `อย่างทรงพลัง` and substitute `รุดมาเหนือ`.

| Verse | Hebrew verb | Sense | 1SA Thai (shipped) | Locked Thai (expected) |
|---|---|---|---|---|
| **10:6** | **צָלַח** | empowerment (Saul) | `วิญญาณขององค์พระผู้เป็นเจ้าจะรุดมาเหนือเจ้า` | `พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเจ้าอย่างทรงพลัง` |
| **10:10** | **צָלַח** | empowerment (Saul) | `วิญญาณของพระเจ้ารุดมาเหนือเขา` | `พระวิญญาณของพระเจ้าก็มาเหนือเขาอย่างทรงพลัง` |
| **11:6** | **צָלַח** | empowerment (Saul vs Nahash) | `วิญญาณของพระเจ้ารุดมาเหนือซาอูล` | `พระวิญญาณของพระเจ้าก็มาเหนือซาอูลอย่างทรงพลัง` |
| **16:13** | **צָלַח** | empowerment (David's anointing) | `วิญญาณขององค์พระผู้เป็นเจ้ารุดมาเหนือดาวิด…` | `พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือดาวิดอย่างทรงพลัง…` |
| **16:14** | סָרָה + רוּחַ רָעָה | departure + evil spirit | `วิญญาณขององค์พระผู้เป็นเจ้าจากซาอูลไปแล้ว…` | bare `วิญญาณ` — needs `พระ` |
| **16:15** | רוּחַ אֱלֹהִים רָעָה | evil spirit | `วิญญาณชั่วจากพระเจ้ากำลังทรมานท่าน` | same — needs `พระ` |
| **16:16** | רוּחַ אֱלֹהִים רָעָה | evil spirit | `เมื่อวิญญาณชั่วจากพระเจ้ามาเหนือท่าน` | same — needs `พระ` |
| **16:23** | רוּחַ אֱלֹהִים | evil-spirit oscillation | `วิญญาณจากพระเจ้ามาเหนือซาอูล…วิญญาณชั่วก็ออกไป` | same — needs `พระ` |
| **18:10** | **צָלַח** + evil-spirit | evil spirit (note: same verb as 10:6/16:13) | `วิญญาณชั่วจากพระเจ้าก็มาเหนือซาอูล` | (internal inconsistency: צָלַח good-spirit = `รุดมาเหนือ`; צָלַח evil-spirit = `มาเหนือ`) |
| **19:9** | תְּהִי + רוּחַ יְהוָה רָעָה | evil spirit | `วิญญาณชั่วจากองค์พระผู้เป็นเจ้ามาเหนือซาอูล` | needs `พระ` |
| **19:20** | תְּהִי | empowerment (Saul's messengers) | `วิญญาณของพระเจ้าก็มาเหนือผู้ส่งสารของซาอูล` | `พระวิญญาณของพระเจ้าก็มาเหนือ…` |
| **19:23** | תְּהִי | empowerment (Saul at Naioth) | `วิญญาณของพระเจ้าก็มาเหนือเขา` | `พระวิญญาณของพระเจ้าก็มาเหนือเขา` |

**For comparison, the shipped Judges corpus is 7/7 compliant** with the lock (all use `พระวิญญาณ` + `อย่างทรงพลัง` for צָלַח):

- **JDG 14:6** (צָלַח, Samson lion): "**พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง**"
- **JDG 14:19** (צָלַח, Ashkelon): "**พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง**"
- **JDG 15:14** (צָלַח, Lehi): "**พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง**"

**Editorial context:** The lock was written 2026-05-20 after JDG end-of-book audit, explicitly to forward-protect 1 Samuel before further shipment. But 1 Sam chs 10, 11, 16, 18, 19 had already shipped (between 2026-05-11 and 2026-05-20). The lock anticipated this exact risk; the drift was not caught by `check_key_term_consistency.py` because Spirit-of-YHWH is not a single-rendering lemma in the key-term registry. This is the **first OT-corpus drift discovered AGAINST an explicitly-forward-protective lock**.

**Forward-compounds to:** 2 Sam 23:2 (David's last words — תְּהִי), 1 Kgs 18:12 + 2 Kgs 2:16 (Spirit-of-YHWH-will-carry-you), 1 Chr 12:18 + 2 Chr 24:20 (לָבְשָׁה lābash — Spirit-clothing), 2 Chr 15:1 + 20:14 (הָיְתָה — Azariah, Jahaziel), Isa 11:2 / 42:1 / 61:1 (Messianic Spirit-anointing), and the NT-side Spirit-quotation passages (Acts 2:17–18 ← Joel 2; Luke 4:18 ← Isa 61; Eph 4:8 ← Ps 68).

**Two questions:**
1. Should the project ship a revision branch (`revision/spirit-of-yhwh-1sam-2026-05`) that retroactively normalizes all 12 1 Sam verses to the lock — restoring `พระ` honorific everywhere and adding `อย่างทรงพลัง` at the 4 צָלַח-good-spirit verses (10:6, 10:10, 11:6, 16:13)? This is the recommended path; cost ~12 surgical verse-edits + per-chapter check-report regeneration.
2. The 16:14–23 + 18:10 + 19:9 **evil-spirit cluster** is OUT-OF-SCOPE of the empowerment lock (per its §"Edge cases" exclusion of `רוּחַ רָעָה`). Should the corpus write a companion doc `docs/translator_decisions/evil_spirit_from_yhwh_1sam_2026-05.md` that explicitly locks a separate Thai surface for the troubling-spirit-from-YHWH narrative — and how should the 18:10 צָלַח-evil-spirit hybrid be treated (extend `อย่างทรงพลัง` or `อย่างรุนแรง` for verb-class consistency, OR split the evil-spirit family entirely)?

---

## Item B — MT/LXX inclusion-variant gap (HIGH severity; first major OT inclusion-variant cluster)

**The pattern:** 1 Samuel contains the corpus's first major MT/LXX/Qumran inclusion-variant cluster (Tier-2 textual-variants infrastructure first stress-test). The audit script `audit_inclusion_variants.py --book 1samuel --strict` reports **0 candidates** because its heuristic was tuned for NT SBLGNT-vs-mainstream variants and does not catch the MT-vs-LXX/Qumran clusters that dominate the OT-side. **None of the 4 major 1 Sam variants are documented** in `output/textual_variants/1samuel_NN.json` (29/31 chapter-variant files contain only the Tier-2 YHWH-first-occurrence footnote; 2/31 [chs 27 + 31] note the YHWH-absent chapter status; zero entries of `type: "inclusion_variant_minus"` exist):

| Variant | Description |
|---|---|
| **1 Sam 10:27b + 11:1** | 4QSamᵃ (Qumran Hebrew) preserves a longer reading naming Nahash's two-year campaign against Reuben + Gad **before** his siege of Jabesh-Gilead. The MT-shorter reading is followed by 1SA shipped text. NRSV + some modern translations include the plus. |
| **1 Sam 13:1** | The corrupt regnal-formula: MT reads "Saul was [missing] years old when he began to reign, and reigned [missing]-and-two years over Israel." The shipped 1SA text reflects the MT corruption ("ซาอูลทรงพระชนม์มายุ … ปี เมื่อพระองค์ขึ้นเป็นกษัตริย์ และทรงปกครองเหนืออิสราเอลสอง … ปี"). |
| **1 Sam 14:41** | MT short reading "הָבָה תָמִים" ("Give the perfect/truth"). LXX has a major expansion via Urim/Thummim: "If this iniquity is in me or in Jonathan my son, O LORD God of Israel, give Urim; but if the iniquity is in your people Israel, give Thummim." The LXX expansion clarifies the otherwise-obscure MT short reading. |
| **1 Sam 17:12–31** + **17:55–18:5** | The famous LXX-B (Vaticanus) **39-verse minus** in the David-Goliath cycle. LXX-B presents a substantially shorter David-introduction; MT (+ LXX-A) preserves the longer reading. The shipped 1SA follows MT throughout. (Note: the 17:4 Goliath-height MT-vs-LXX variant IS documented in the chapter footnote, but the major 39-verse minus is not flagged.) |

**Editorial context:** Per `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md`, every MT-vs-LXX/Qumran inclusion-variant with corpus-significance should be explicitly dispositioned (Tier 1 phrase brackets / Tier 2 chapter-footer file / Tier 3 ⟦double brackets⟧). 1 Samuel ships with the decisions silent — the maintainer followed MT throughout (defensible, matches `ot_canon_and_text_base_2026-05.md` MT-base policy), but the **transparency layer is missing**. The Tier-2 chapter-footer infrastructure is deployed (31/31 chapters have JSON files) but underutilized for the actual variant cluster.

**This sets the precedent** for 2 Sam (4QSamᵃ + LXX divergences), 1–2 Kings (LXX Old Greek), Jeremiah (the famous MT-vs-LXX shorter recension — LXX is ~12.5% shorter), and Daniel (Greek-vs-Aramaic plus-narratives).

**Two questions:**
1. The audit recommends writing 4 Tier-2 chapter-footer JSON entries (`output/textual_variants/1samuel_{11,13,14,17}.json`) documenting the MT-base decision + summarizing the LXX/Qumran alternative + Tier-2 marker (chapter-level footer per `inclusion_variants_absent_verses_2026-04.md` Tier-2 spec). Is this the right level of disclosure for the CC0 Thai Bible's target reader (Thai evangelical + theological-reviewer audience)? Or should the **1 Sam 17 LXX-B minus** (which is exceptionally well-known and substantial) receive a stronger Tier-1 disclosure (verse-level bracket or ⟦…⟧ markers around the LXX-omitted sections)?
2. The Hebrew MT 13:1 regnal-formula is **textually corrupt** — most scholars accept the MT preserves a damaged reading, not the original. Should the project follow the MT-corrupt form (current shipped behavior — preserving the textual difficulty as a witness to scribal-transmission history) OR interpolate plausible numbers (NRSV-style "[thirty]" + "[forty]-two") with explicit brackets and Tier-2 explanation OR adopt a third path (LXX has its own emendation of the verse)? The corpus's `ot_canon_and_text_base_2026-05.md` MT-base policy favors path 1 (preservation-of-difficulty), but the resulting Thai verse is opaque to Thai readers — is preserving the textual difficulty the right tradeoff?

---

## Item C — "Is Saul also among the prophets?" inclusio surface drift

**The pattern:** The Hebrew הֲגַם שָׁאוּל בַּנְּבִיאִם is the verbatim-identical proverb-inclusio closing two distinct prophetic-ecstasy narratives — one early (Saul's first Spirit-rush at Gibeah, 10:11–12) and one late (Saul's stripping at Naioth, 19:24). The inclusio is one of 1 Samuel's signature literary architectures (alongside the rise-of-David / fall-of-Saul axis). The Thai surfaces drift between the two narrative ends of the inclusio:

| Verse | Hebrew | Thai surface |
|---|---|---|
| **10:11** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ"** |
| **10:12** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ"** (identical to 10:11 — good internal consistency) |
| **19:24** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ซาอูลก็เป็นหนึ่งในผู้เผยพระวจนะด้วยหรือ?"** (DIFFERENT — subject-first reorder + "เป็นหนึ่งใน" insertion + explicit question mark) |

**Drift analysis.** The 10:11/12 form preserves Hebrew word-order + the rhetorical interrogative force of הֲגַם ("is also/even"). The 19:24 form reorders to a more-natural Thai prose construction. **Both are defensible Thai for the underlying proverb — but the inclusio's verbatim-function is lost in the surface.** This mirrors the JDG-audit §7 17:6 ↔ 21:25 "no king in Israel" inclusio drift (same literary-architecture issue, different book).

**Question:** Should the project normalize 19:24 to the 10:11/12 form ("ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ") to preserve the verbatim inclusio? Cost: 1 surgical verse-edit. (Or — does Thai-reader naturalness justify the variation, given that the 19:24 narrative-context is more dramatic — Saul stripped and lying naked all day at Naioth — and the question-mark form is more natural at the climactic moment?)

---

## Item D — Pagan-deity register + Ashtaroth spelling drift

**Two distinct sub-issues:**

### D1. 1 Sam 5:7 — Dagon called "พระเจ้า" in Philistine speech (Rule 1 violation)

The Philistines of Ashdod refer to Dagon as **"ดาโกนพระเจ้าของพวกเรา"** (1 Sam 5:7, וְעַל דָּגוֹן אֱלֹהֵינוּ). This applies the supreme Christian-divine title **`พระเจ้า`** to a literal pagan deity in pagan speech — explicitly forbidden by **two corpus docs**:

- `pagan_deities_2026-04.md` Rule 1: "Literal pagan deities, in any voice, never receive the divine register reserved for the biblical God."
- `ot_polytheistic_register_2026-05.md` §1.3: "Calling foreign deities **พระเจ้า** ("God") [is prohibited]. That term is reserved for the personal God of Israel + Christian Trinitarian usage. Foreign deities = พระ / พระทั้งหลาย / เทพ."

**Sample verse:**
- **1 Sam 5:7 HEB:** `כִּי־קָשְׁתָה יָדוֹ עָלֵינוּ וְעַל דָּגוֹן אֱלֹהֵינוּ` → **TH (shipped):** "เพราะมือของพระองค์หนักเหนือพวกเราและเหนือ**ดาโกนพระเจ้าของพวกเรา**"
- **Recommended fix:** "เหนือ**ดาโกนเทพเจ้าของพวกเรา**" (per pagan-deity Rule 1 register family — `เทพเจ้า` for "a god / one of the gods")

### D2. Ashtaroth (עַשְׁתָּרוֹת) 3-form spelling drift within 1SA; 4-form across JDG+1SA

| Ref | Hebrew | Thai |
|---|---|---|
| 1 Sam 7:3 | הָעַשְׁתָּרוֹת | "**พระอัชโทเรท**" |
| 1 Sam 7:4 | הָעַשְׁתָּרֹת | "**พระอัชโทเรท**" (matches 7:3) |
| 1 Sam 12:10 | הָעַשְׁתָּרוֹת | "**พระอาเชโทรททั้งหลาย**" |
| 1 Sam 31:10 | בֵּית עַשְׁתָּרוֹת | "**วิหารของเทพีอัชทาโรท**" |
| (cross-corpus) JDG 2:13, 10:6 | הָעַשְׁתָּרוֹת | "**บรรดาพระอัชเทเรท**" |

**Four distinct transliterations** for the same lemma: **อัชเทเรท** (JDG) / **อัชโทเรท** (1 Sam 7) / **อาเชโทรท** (1 Sam 12) / **อัชทาโรท** (1 Sam 31). Additionally, the 31:10 form is **register-divergent** from the JDG/early-1SA precedent: chs 7+12 use the OT-precedent `พระ`-prefix; 31:10 uses the pagan-deity-register `เทพี`-prefix (which is the form `pagan_deities_2026-04.md` Rule 1 actually requires).

**Editorial context:**
- The JDG-audit §15 row for `pagan_deities_2026-04.md` marked JDG-Baal/Ashtaroth **LOCKED + compliant** with `พระบาอัล / บรรดาพระอัชเทเรท` — treating the `พระ`-prefix as the OT-corpus convention (distinct from the NT-Acts pagan_deities rule that uses `เทพเจ้า`). So the question is whether the OT-corpus convention is the right exception, OR whether the corpus should retroactively shift to the NT-aligned `เทพ-`-register.
- A minor `พระ`-prefix internal drift also exists at 1 Sam 7:4 ("บาอัลทั้งหลาย" — no `พระ`) vs 12:10 ("พระบาอัลทั้งหลาย").

**Two questions:**
1. The 5:7 Dagon-as-`พระเจ้า` violation is unambiguous against **both** Rule 1 and ot_polytheistic_register §1.3. Should the recommended fix ("ดาโกนเทพเจ้าของพวกเรา") apply — OR is there a defensible reading where the Hebrew אֱלֹהֵינוּ ("our God/gods") gets a paraphrastic render like "ดาโกนพระของพวกเรา" (without the supreme `พระเจ้า`-title) for OT-corpus-register consistency with JDG?
2. For the Ashtaroth 4-form spelling drift: should the corpus (a) normalize to JDG's **อัชเทเรท** (which currently has 2 occurrences, the most across the corpus) keeping the OT-precedent `พระ`-register; OR (b) shift to the pagan_deities_2026-04 NT-aligned `เทพี`-register (which would require retroactive amendment to the JDG-audit §15 LOCKED entry); OR (c) accept a principled OT-vs-NT register-split documented in a new corpus doc?

---

## Item E — Witch of Endor + necromancy vocabulary lock (recommend new corpus doc)

**The pattern:** 1 Sam 28:3–25 is the OT's most theologically charged necromancy narrative. The Thai translation handles the אוֹב + יִדְּעֹנִי technical lemma cluster with **descriptive paraphrase** (not transliteration) — a defensible editorial choice that is currently undocumented in `docs/translator_decisions/`. The pattern forward-compounds to 5 other OT books + 1 NT passage.

**Sample verses showing the lock-candidate Thai surfaces:**

| Verse | Hebrew | Thai surface (shipped) |
|---|---|---|
| **28:3** | אֶת־הָאֹבוֹת וְאֶת־הַיִּדְּעֹנִים | "ผู้ที่ติดต่อกับวิญญาณและผู้ที่รู้สิ่งล้ำลับ" |
| **28:7** | אֵשֶׁת בַּעֲלַת־אוֹב | "ผู้หญิงที่เป็นแม่หมอ" |
| **28:8** | קָסֳמִי־נָא לִי בָּאוֹב וְהַעֲלִי לִי | "ขอจงเรียกวิญญาณให้ข้า และจงนำผู้ที่ข้าจะระบุแก่เจ้าขึ้นมาให้ข้า" |
| **28:13** | אֱלֹהִים רָאִיתִי עֹלִים מִן־הָאָרֶץ | **"ข้าเห็นพระเจ้า ขึ้นมาจากแผ่นดิน"** (Hebrew plural אֱלֹהִים + plural participle עֹלִים → Thai keeps `พระเจ้า` divine register; flattens plural participle to singular `ขึ้นมา`) |
| **28:14** | אִישׁ זָקֵן עֹלֶה וְהוּא עֹטֶה מְעִיל | "ชายแก่กำลังขึ้นมา และเขาสวมเสื้อคลุม" |
| **28:15** | וֵאלֹהִים סָר מֵעָלַי | "พระเจ้าทรงจากข้าไป" |
| **28:16** | וַיהוָה סָר מֵעָלֶיךָ | "องค์พระผู้เป็นเจ้าทรงจากเจ้าไป" |
| **28:19** | וּמָחָר אַתָּה וּבָנֶיךָ עִמִּי | "พรุ่งนี้ เจ้าและบุตรของเจ้าจะอยู่กับข้า" |

**Editorial assessment.**
- **Descriptive paraphrase** for אוֹב ("ผู้ที่ติดต่อกับวิญญาณ" = "one who contacts spirits") + יִדְּעֹנִי ("ผู้ที่รู้สิ่งล้ำลับ" = "one who knows hidden things") — preserves the prohibition's force without exoticizing the Hebrew technical lexicon, and avoids the THSV transliteration "หมอผีและคนทรง" (which sounds anachronistic Thai-folk-religion-coded).
- The 28:13 אֱלֹהִים-as-divine-being rendering is the load-bearing decision: the Hebrew uses plural אֱלֹהִים with plural participle עֹלִים (literally "I see *gods* ascending from the earth") — a grammatical curiosity that all major translations wrestle with. The Thai uses `พระเจ้า` (preserving the standard OT אֱלֹהִים → พระเจ้า convention from `divine_names_table_2026-05.md`) but flattens the plural participle to singular `ขึ้นมา`. Defensible per the OT-base lock — but loses the Hebrew literary curiosity.

**Forward-compounding cluster (the corpus doc would protect):**
- **Lev 19:31, 20:6, 20:27** — Mosaic prohibition (the legal background that 1 Sam 28:3 presupposes — "Saul had banished the mediums and the necromancers from the land")
- **Deut 18:9–14** — prohibition reaffirmed in the deuteronomic-law
- **2 Kgs 21:6 + 23:24** — Manasseh's revival + Josiah's purge (same lemma cluster)
- **Isa 8:19, 19:3, 29:4** — prophetic polemic against necromancy
- **1 Chr 10:13** — the Chronicler's death-notice for Saul explicitly cites the witch-of-Endor consultation as the proximate cause of his death (cross-corpus link)
- **NT: Acts 16:16–18** — the πνεῦμα πύθωνος (Pythian-slave-girl) exorcism, the closest NT analog

**Two questions:**
1. Is the **descriptive-paraphrase Thai surface** ("ผู้ที่ติดต่อกับวิญญาณ" / "ผู้ที่รู้สิ่งล้ำลับ") the right editorial choice for the אוֹב + יִדְּעֹנִי lemma cluster — vs the THSV/TNCV "หมอผี" / "คนทรง" alternative — for a CC0 Thai Bible whose Thai-evangelical readership is also navigating the Thai-folk-religion semantic field of spirit-mediumship? (The descriptive form is academically more neutral; the THSV-aligned form is more recognizable to Thai readers but risks importing Thai-folk-religion connotations into the OT cult-prohibition narrative.)
2. Should the project lock the 28:13 אֱלֹהִים-rendering choice (preserve `พระเจ้า` divine register; document the plural-participle flattening as an editorial choice rather than an oversight) in the new corpus doc? Or should the rendering instead use a paraphrastic form that captures the Hebrew plural ambiguity — e.g., "ข้าเห็น**สิ่งศักดิ์สิทธิ์** ขึ้นมาจากแผ่นดิน" (`สิ่งศักดิ์สิทธิ์` = "a divine/holy being"; matches `ot_polytheistic_register_2026-05.md` §1.1 vocabulary table for אֱלֹהִים in non-personal-divine contexts)?

---
