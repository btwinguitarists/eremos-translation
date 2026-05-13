## Item A — EXO 34:6–7 Sinai attribute formula drifts from its own canonical corpus-doc

**The drift:** The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` (decided 2026-05-09, Ben + cross-AI consensus, post-Jonah audit) **explicitly names Exod 34:6–7 as the canonical Sinai form** locking the Thai across all ~10 OT recitations (Num 14:18, Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Jonah 4:2, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18). Jonah 4:2 was retroactively normalized after that doc landed. Exodus 34 — the doc's namesake locking-precedent — was shipped on 2026-05-13 **without the doc's lock applied**.

**The doc's canonical Thai (Exod 34:6–7):**

```
องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า พระเจ้าผู้ทรงพระเมตตาและทรงพระคุณ ทรงกริ้วช้า
ทรงบริบูรณ์ด้วยความรักมั่นคงและความซื่อสัตย์
ทรงรักษาความรักมั่นคงไว้ถึงพันชั่วอายุ ทรงยกโทษความชั่ว การละเมิด และบาป
แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ — ทรงลงโทษความชั่วของบรรพบุรุษ
ต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน
```

**EXO 34:6–7 as shipped:**

> **34:6** องค์พระผู้เป็นเจ้าทรงผ่านต่อหน้าโมเสสและทรงร้องเรียกว่า "องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า **พระเจ้าผู้เปี่ยมด้วยความกรุณาและความเมตตา ช้าในการพิโรธ บริบูรณ์ด้วยความรักมั่นคงและความจริง**
>
> **34:7** **ทรงรักษาความรักมั่นคงไว้ตลอดพันชั่วอายุ ทรงให้อภัยความผิด การล่วงละเมิด และบาป แต่พระองค์จะไม่ทรงปล่อยให้คนผิดพ้นโทษ พระองค์จะลงโทษความผิดของบิดาต่อบุตรและหลานจนถึงชั่วอายุที่สามและที่สี่"**

**Component-by-component drift** (every locked vocabulary item diverges):

| Hebrew | Doc-locked Thai | EXO 34 actual | Drift |
|---|---|---|---|
| חַנּוּן | **ทรงพระคุณ** | **ความกรุณา** | ✗ |
| רַחוּם | **ทรงพระเมตตา** | **ความเมตตา** | ✗ (vocabulary + verbal-noun form lost) |
| אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | **ช้าในการพิโรธ** | ✗ (no royal ทรง-; different metaphor) |
| רַב־חֶסֶד | **ทรงบริบูรณ์ด้วยความรักมั่นคง** | **บริบูรณ์ด้วยความรักมั่นคง** | ✗ (no ทรง-) |
| וֶאֱמֶת | **และความซื่อสัตย์** | **และความจริง** | ✗ (truth vs. faithfulness — major theological divergence) |
| נֹשֵׂא עָוֹן וָפֶשַׁע וְחַטָּאָה | **ทรงยกโทษความชั่ว การละเมิด และบาป** | **ทรงให้อภัยความผิด การล่วงละเมิด และบาป** | ✗ (ยกโทษ "lift away" vs. ให้อภัย "give forgiveness"; ความชั่ว vs. ความผิด) |
| וְנַקֵּה לֹא יְנַקֶּה | **แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ** | **แต่พระองค์จะไม่ทรงปล่อยให้คนผิดพ้นโทษ** | partial drift |
| פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים וְעַל־בְּנֵי בָנִים | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **พระองค์จะลงโทษความผิดของบิดาต่อบุตรและหลาน** | ✗ (no royal ทรง-; "fathers→sons" vs. "ancestors→grandchildren-and-great-grandchildren") |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **จนถึงชั่วอายุที่สามและที่สี่** | partial drift |

**Cross-corpus context:** The Jonah 4:2 audit (2026-05-09) was the trigger that produced the formula doc. After Jonah's normalization, the doc was the **canonical Thai** for the formula. Genesis didn't recite the formula (no occurrence in GEN). **Exodus 34:6–7 is the first OT recitation of the formula in Eremos's ship-order**. If `book-exodus-v1` ships without normalization, every downstream OT-book that recites the formula will diverge from the Exodus locking-precedent. The formula is the OT's most-recited divine-self-revelation — the cross-corpus thread is broken at its source.

**Why this is consequential:** Cross-corpus traceability is the formula's entire reason for the lock. The doc says "If the Thai rendering varies across recitations, the Thai reader cannot recognize the formula. The character-cluster becomes invisible." Currently the Thai reader will encounter Exod 34:6 → "พระเจ้าผู้เปี่ยมด้วยความกรุณา…ความเมตตา…ความจริง"; then at Jonah 4:2 → "พระองค์ทรงเป็นพระเจ้าผู้ทรงพระคุณ…ทรงพระเมตตา…ความรักมั่นคง"; then at Joel 2:13 (forthcoming) → presumably matching Jonah 4:2 via the doc. Cross-corpus recognition fails at the seam.

**Recommended retroactive normalization** (Exodus 34:6–7 → doc-canonical Thai):

| Verse | Drift Thai | Recommended Thai |
|---|---|---|
| 34:6 | …องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า **พระเจ้าผู้เปี่ยมด้วยความกรุณาและความเมตตา ช้าในการพิโรธ บริบูรณ์ด้วยความรักมั่นคงและความจริง** | …องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า **พระเจ้าผู้ทรงพระเมตตาและทรงพระคุณ ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคงและความซื่อสัตย์** |
| 34:7 | **ทรงรักษาความรักมั่นคงไว้ตลอดพันชั่วอายุ ทรงให้อภัยความผิด การล่วงละเมิด และบาป แต่พระองค์จะไม่ทรงปล่อยให้คนผิดพ้นโทษ พระองค์จะลงโทษความผิดของบิดาต่อบุตรและหลาน จนถึงชั่วอายุที่สามและที่สี่** | **ทรงรักษาความรักมั่นคงไว้ถึงพันชั่วอายุ ทรงยกโทษความชั่ว การละเมิด และบาป แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ — ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน** |

**Two questions:**

1. Should Exod 34:6–7 be retroactively normalized to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md` before tagging `book-exodus-v1`? The cost is one surgical verse-pair edit + re-running per-chapter checks; the benefit is restoring the cross-corpus lemma-thread before any downstream OT-book recites the formula (Num 14:18 ships with Numbers; Ps 86 / 103 / 145 with Psalms; Joel / Nah / Mic with the Twelve).

2. Should the doc's Implementation Checklist §3 item 2 (the `check_phrase_consistency.py` extension that would HARD FAIL when 3+ formula-components co-occur but the locked Thai is missing) be written in tandem with the normalization commit? This is the structural fix that prevents the same drift recurring at Num 14:18 / Ps 86 / etc.

---

## Item B — EXO 33:19 חַנֹּתִי + רִחַמְתִּי verbal-form mapping is swapped vs. corpus-doc AND vs. EXO 34:6 within the same theophanic-cluster

**The textual question:** Exod 33:19 is the structural precursor to 34:6 — the same divine self-revelation in promise-form before the proclamation-form. The two verses are the bookends of the Sinai-glory pericope (33:18-34:8).

> **33:19 Hebrew:** וְקָרָאתִי בְשֵׁם יְהוָה לְפָנֶיךָ וְ**חַנֹּתִי אֶת־אֲשֶׁר אָחֹן וְרִחַמְתִּי אֶת־אֲשֶׁר אֲרַחֵם**
>
> **33:19 Thai (current):** …และเราจะประกาศชื่อของเรา — องค์พระผู้เป็นเจ้า — ต่อหน้าเจ้า **เราจะมีพระเมตตาต่อผู้ที่เราจะเมตตา และเราจะมีพระกรุณาต่อผู้ที่เราจะกรุณา**

**Two compounding drifts:**

**First drift — verb mapping is swapped relative to corpus-doc:**

| Hebrew root | Doc-locked nominal Thai (`exod_34_attribute_formula_2026-05.md`) | 33:19 verbal Thai (current) |
|---|---|---|
| חנן (חַנֹּתִי "I will be gracious") | **พระคุณ** ("gracious") | **เมตตา** ✗ swapped |
| רחם (רִחַמְתִּי "I will be merciful") | **พระเมตตา** ("compassionate / merciful") | **พระกรุณา** ✗ swapped |

**Second drift — 33:19 verbal mapping is swapped relative to the as-shipped Exod 34:6:**

| Verse | Hebrew (in order) | Thai (in order) |
|---|---|---|
| 33:19 (promise-form) | חַנֹּתִי + רִחַמְתִּי | **เมตตา + กรุณา** |
| 34:6 (proclamation-form) | רַחוּם + חַנּוּן | **กรุณา + เมตตา** |

Reading both verses, the cross-lemma assignment swaps: 33:19 maps חנן→เมตตา and רחם→กรุณา; 34:6 maps רחום→กรุณา and חנון→เมตตา. **Even on the as-shipped surface, the project's own internal lemma-Thai mapping is inconsistent between adjacent verses within the same theophanic-cluster.**

**The Rom 9:15 NT cross-reference:** Paul quotes 33:19 in Romans 9:15 (`ἐλεήσω ὃν ἂν ἐλεῶ, καὶ οἰκτιρήσω ὃν ἂν οἰκτίρω`). The LXX renders חנן→ἐλεήσω (the same root the NT corpus has locked to a specific Thai) and רחם→οἰκτιρήσω. The Eremos NT renders Rom 9:15 with — whatever it renders. The OT side's swap means the OT-and-NT trajectory of חנן/רחם will fail at this seam unless both sides are normalized.

**Doc-aligned normalization recommendation:**

| Verse | Hebrew | Doc-aligned Thai |
|---|---|---|
| 33:19 | חַנֹּתִי + רִחַמְתִּי | **เราจะทรงพระคุณต่อผู้ที่เราจะทรงพระคุณ และเราจะทรงพระเมตตาต่อผู้ที่เราจะทรงพระเมตตา** |
| 34:6 | רַחוּם + חַנּוּן | (per Item A) **พระเจ้าผู้ทรงพระเมตตาและทรงพระคุณ** |

**Question:** Should Exod 33:19 be normalized to match the corpus-doc's locked nominal-form mapping (חנן → พระคุณ; רחם → พระเมตตา), in tandem with the Item A normalization at 34:6? The two verses are theologically paired in the Sinai-glory pericope; normalizing one without the other only fixes half the drift.

---

## Item C — EXO 15:11 בָּאֵלִם "among the gods" — Hebrew-polytheistic-surface vs. Thai-evangelical default register

**The textual question:** The Song of the Sea includes the rhetorical question:

> **15:11 Hebrew:** מִי־כָמֹכָה בָּאֵלִם יְהוָה
>
> **15:11 Thai (current):** ใครในหมู่**พระทั้งหลาย**เหมือนพระองค์ ข้าแต่องค์พระผู้เป็นเจ้า

**The exegetical question.** **ในหมู่พระทั้งหลาย** ("among the gods/deities") preserves the Hebrew בָּאֵלִם as a plural-gods construction. This matches the literal LXX (ἐν θεοῖς) and is **academically defensible** — Exod 15 is the OT's oldest poetic stratum and contains traces of Yahweh-as-incomparable-among-other-gods register (cf. Ps 82:1 בַּעֲדַת אֵל, Ps 89:6 בְּנֵי אֵלִים, Ps 95:3 עַל־כָּל־אֱלֹהִים, Ps 96:4 / 97:9 same idiom). The rhetorical-comparative form occurs throughout the Hebrew Bible's older poetic strata and reflects the pre-monotheistic-development Israelite religious-rhetorical convention (cf. Mark S. Smith, *The Early History of God*).

**The reader-experience concern.** A typical Thai-evangelical reader of **ในหมู่พระทั้งหลาย** will read this as **confirming the existence of other gods** — which conflicts with the monotheistic frame the Thai-evangelical church understands as the OT's overall theology. THSV-1971 reads **เทพเจ้าทั้งหลาย** (similar polytheistic-surface register); some modern Thai translations paraphrase to **เทพเจ้าใดเหมือนพระองค์** ("which deities could compare with you") to preserve the rhetorical-question form while neutralizing the polytheistic surface.

**Cross-corpus implications.** The decision compounds across:
- **Pss 82 / 86 / 89 / 95 / 96 / 97 / 135 / 136 / 138** (multiple "incomparable-among-gods" formulae)
- **Deut 10:17** אֱלֹהֵי הָאֱלֹהִים "God of gods"
- **Job 1:6 / 2:1 / 38:7** בְּנֵי הָאֱלֹהִים "sons of God" — Gen-audit-flagged
- **Isa 41–46** Yahweh-vs-the-idols polemic
- **Eph 6:12 / Col 2:15** "principalities-and-powers" NT compounding

Without a locked policy, future books will likely apply different conventions ad-hoc.

**Three resolution paths:**

(a) **Current** — preserve the Hebrew בָּאֵלִם as-is with **พระทั้งหลาย**. Most faithful to the Hebrew text's pre-monotheistic-development register. Defensible academically; risks Thai-reader-confusion in the evangelical context. Matches THSV-1971.

(b) **Paraphrase to "เทพเจ้าใดเหมือนพระองค์"** — preserves the rhetorical-comparison; reads as "no deity is like you" rather than "no god among (the existing) gods is like you." Reader-friendly; muffles the Hebrew's mythopoetic surface.

(c) **Doc-lift** — write `docs/translator_decisions/ot_polytheistic_register_2026-05.md` (or extend `spiritual_beings_hierarchy_2026-05.md`) naming the project's stance for Exod 15:11, the Psalms-cluster (82, 86, 89, etc.), Deut 10:17, Job 1:6, Isa 41–46, and the NT trajectory. The doc names the principle; either (a) or (b) above becomes the locked rendering.

**Question:** Which option best serves the Thai-evangelical reader's exegetical understanding of Exod 15:11 + the cross-corpus polytheistic-register thread? Should the project endorse the Hebrew-faithful **ในหมู่พระทั้งหลาย** + doc-lift (preserving academic-honesty), or the paraphrastic **เทพเจ้าใดเหมือนพระองค์** + doc-lift (preserving theological-clarity), with the doc naming the principle either way?

---

## Item D — מַלְאַךְ YHWH / מַלְאָךְ rendered four different ways in six occurrences

**The drift:** Across Exodus's six "angel/messenger of YHWH" occurrences, the Thai uses **at least four distinct phrases** for the same Hebrew lemma:

| Verse | Hebrew | Thai (current) | Variant |
|---|---|---|---|
| **3:2** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** | "envoy of YHWH" |
| **14:19** | מַלְאַךְ הָאֱלֹהִים | **ทูตของพระเจ้า** | "envoy of God" |
| **23:20** | מַלְאָךְ (anarthrous) | **ทูตสวรรค์** | "heavenly messenger" |
| **23:23** | מַלְאָכִי (1cs suffix) | **ทูตสวรรค์ของเรา** | "my heavenly messenger" |
| **32:34** | מַלְאָכִי | **ทูตของเรา** | "my envoy" |
| **33:2** | מַלְאָךְ | **ทูตสวรรค์** | "heavenly messenger" |

**The lexical distinction in Thai.** **ทูต** alone (without สวรรค์) is plain "messenger / envoy / ambassador" — used in Thai diplomatic register without supernatural connotation (the Thai foreign-affairs ministry calls its ambassadors **ทูต**). **ทูตสวรรค์** (literally "heavenly messenger") is the NT-corpus locked rendering for ἄγγελος (across all 4 Gospels + Acts + epistles + Revelation). **ทูต + qualifier** ("envoy of YHWH/God/me") reads as bureaucratic-divine-envoy register, while **ทูตสวรรค์** reads as angelic-supernatural.

**The reader-experience concern.** A Thai reader encountering 3:2 (burning bush — "ทูตขององค์พระผู้เป็นเจ้า") and then 23:20 ("ทูตสวรรค์") will read these as **different categories of being** — exactly the cross-corpus drift the project's term-consistency policy was created to prevent. The Hebrew has no such category-distinction; both are מַלְאָךְ.

**Cross-corpus implications.** The decision compounds across **nearly every OT theophanic narrative**:
- Genesis: Hagar (16:7-13), Sodom (19:1+15), Akedah (22:11+15), Jacob's-ladder (28:12), Mahanaim (32:1), Jacob-wrestling (32:24-30 indirectly), Joseph-dreams (mediated)
- Numbers: Balaam's-donkey (22:22-35)
- Judges: Bochim (2:1+4), Gideon's commissioning (6:11+12+21+22), Manoah / Samson's birth (13:3-21 — 11 occurrences!)
- Samuel: David's-census (2 Sam 24:16)
- Kings: Elijah's-flight (1 Kgs 19:5+7), Ahaziah (2 Kgs 1:3+15)
- Zechariah: 20+ occurrences across visions 1-6
- Daniel: fiery-furnace (3:28), lions' den (6:22)
- Malachi: 3:1 himself — the literary mal'akh-bookend ("my messenger")

Without normalization the lemma-thread is broken in nearly every OT-corpus angelic-theophany.

**Three resolution paths:**

(a) **Normalize to ทูตสวรรค์ throughout** for divine-מַלְאָךְ verses (lock the angelic-supernatural reading; matches NT-corpus default for ἄγγελος). Cost: 3 verse-edits at 3:2, 14:19, 32:34. Defensible because the NT trajectory (Heb 1:14 + 2:2 + 13:2 + Jude 6 + Rev) treats מַלְאָךְ/ἄγγελος as a single angelic category.

(b) **Normalize to ทูต throughout** for OT-corpus mal'akh-yhwh verses (preserve the Hebrew's underdetermined ontological status; the NT-corpus then independently uses ทูตสวรรค์ for ἄγγελος). Cost: 3 verse-edits at 23:20, 23:23, 33:2.

(c) **Doc-lift** — write `docs/translator_decisions/malak_yhwh_2026-05.md` naming the OT-corpus Thai-lock + rationale + the NT cross-reference. Either (a) or (b) becomes the doc's choice.

**Two questions:**

1. Should the project normalize the Exodus mal'akh-YHWH verses to a single Thai rendering (ทูตสวรรค์ or ทูต-with-qualifier), and write `malak_yhwh_2026-05.md` to lock the corpus-wide stance? The decision compounds across nearly every OT theophanic narrative and the entire NT corpus.

2. If normalizing to ทูตสวรรค์ (option a — recommended), is there theological concern about identifying the Exod 3:2 burning-bush מַלְאַךְ YHWH (often read in the church-tradition as the pre-incarnate Christ / 'angel-of-the-Lord' theophany) with ทูตสวรรค์ ("heavenly messenger" = generic angel)? Should the Thai distinguish the angel-of-YHWH theophany from generic angelic-mention via a doc-named sub-rule, or accept the lexical collapse and let the verse-level KD carry the theophany-distinction?

---

## Item E — EXO 17:15 יְהוָה נִסִּי "YHWH-Nissi" paraphrased, vs. divine_names_table's transliteration-plus-gloss convention for place-name compounds

**The textual question:** After defeating Amalek, Moses builds an altar and names it:

> **17:15 Hebrew:** וַיִּבֶן מֹשֶׁה מִזְבֵּחַ וַיִּקְרָא שְׁמוֹ יְהוָה נִסִּי
>
> **17:15 Thai (current):** โมเสสสร้างแท่นบูชาและตั้งชื่อว่า **'องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า'**

**The Genesis precedent** (locked in `divine_names_table_2026-05.md` §"place-name compounds"):

> GEN 22:14: יְהוָה יִרְאֶה → **ยาห์เวห์ยีเรห์** (transliterated + parenthetical gloss "องค์พระผู้เป็นเจ้าทรงจัดเตรียม")

The Genesis convention for YHWH-compounded altar-names is to **transliterate** the Hebrew compound + add a parenthetical Thai gloss. Exodus 17:15 deviates: **the altar-name is paraphrased** rather than transliterated.

A consistent treatment would be:

> โมเสสสร้างแท่นบูชาและตั้งชื่อว่า **'ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)'**

The same question applies to **EXO 15:26 יְהוָה רֹפְאֶךָ** ("YHWH-your-Healer"; rendered **องค์พระผู้เป็นเจ้าผู้รักษาเจ้า** — paraphrased, not transliterated) and **EXO 31:13 יְהוָה מְקַדִּשְׁכֶם** ("YHWH-who-sanctifies-you"). These are divine-self-titles rather than place-names per se, so the transliteration-or-paraphrase question is sharper here.

**The category distinction.** The Genesis compound יְהוָה יִרְאֶה became the *place-name* (the mountain itself is called by that name). The Exodus compounds are **altar-names** (17:15) and **divine-self-attribution titles** (15:26, 31:13) — they do not become place-names. This may be a defensible category-distinction (transliterate-place-names, paraphrase-self-titles). But the project doesn't currently document this distinction.

**Three resolution paths:**

(a) **Normalize Exod 17:15 to transliterated-altar-name + gloss** ("ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)") to match Genesis 22:14's convention. Same treatment for 15:26 + 31:13. Cost: 3 verse edits.

(b) **Doc-amend** — extend `divine_names_table_2026-05.md` with a "YHWH-paraphrastic-self-title" sub-category covering Exod 15:26 + 17:15 + 17:16 ("מִלְחָמָה לַיהוָה בַּעֲמָלֵק") + 31:13. The sub-category names the principle that **divine-self-titles** (paraphrase) are distinct from **place-name-compounds** (transliterate). Locking-precedent: Exod 15:26.

(c) **Current** — leave as-is; allow the precedent at Exod 17:15 to imply a (defensible-but-undocumented) category-distinction for future books.

**Question:** Should the divine_names_table doc be amended to add a "YHWH-paraphrastic-self-title" sub-category (option b above), naming Exodus 15:26 + 17:15 + 17:16 + 31:13 as locking precedents and the principle that distinguishes them from Genesis 22:14's place-name-compound transliteration? Or should Exodus 17:15 + 15:26 be retroactively normalized to transliterated-name + gloss (option a) to preserve the Genesis convention?

---

## Item F — Pharaoh's heart-hardening: three Hebrew roots collapse to single Thai idiom

**The pattern:** The Exodus narrative deploys **three distinct Hebrew roots** for Pharaoh's heart-hardening across 19 occurrences:

| Hebrew root | Sense | Occurrences | Subject pattern |
|---|---|---|---|
| **חזק (Piel/Hiphil "strengthen / make-strong")** | strengthen-toward-defiance | 4:21, 7:13, 7:22, 8:19, 9:12, 9:35, 10:20, 10:27, 11:10, 14:4, 14:8, 14:17 (12×) | mostly YHWH-subject |
| **קשה (Hiphil "make-hard")** | make-stubborn | 7:3 (1×) | YHWH-subject |
| **כבד (Qal/Hiphil "be/make-heavy")** | weigh-down / be-burdened | 7:14, 8:15, 8:32, 9:7, 9:34, 10:1 (6×) | mixed: Pharaoh-self + YHWH-self |

**Thai (uniform across all 19):** **(ทำให้ใจ)ของฟาโรห์แข็งกระด้าง**.

**Editorial assessment.** The Thai uniform rendering matches THSV / BSB / NIV but flattens the Hebrew literary-structural distinction:
- חזק "strengthen" connotes empowerment-toward-defiance
- קשה "harden" connotes inner-stubbornness
- כבד "make-heavy" connotes weight-of-judgment / burden-of-guilt

The Hebrew narrator's careful alternation across the three roots is a **deliberate literary structure** (cf. Brevard Childs, *Exodus*, 1974, pp. 170-175; Carol Meyers, *Exodus*, 2005, pp. 78-79): YHWH starts with חזק (announcing 4:21, 7:3), Pharaoh's self-hardening uses כבד (8:15 + 8:32 + 9:34), the final crescendo (chs. 10–14) uses חזק exclusively for YHWH's direct action.

**Subject-distinction IS preserved** at the syntactic level: When YHWH is subject ("เราจะทำให้ใจของฟาโรห์แข็งกระด้าง"), the Thai uses causative + 1st-person-divine; when Pharaoh is subject ("ใจของฟาโรห์ก็แข็งกระด้าง"), the Thai uses inchoative/stative. So the major exegetical question (who's hardening whom) is fully tracked.

**Why this matters forward:** Pharaoh's heart-hardening is the **OT paradigm for the Pauline elections theology** (Rom 9:14-23, anchored in 9:17-18 + the Exod 9:16 citation; and the Johannine Isaiah-citation at Jn 12:40 / Acts 28:27 / Rom 11:8). The Thai's uniform-flattening simplifies the OT-NT inheritance: the same Thai "แข็งกระด้าง" carries from the Exodus narrative to Paul's Romans to John's Isaiah-citation. This is **cross-corpus theological coherence** that the uniform rendering protects.

**Question:** Should the project write `docs/translator_decisions/pharaoh_heart_hardening_2026-05.md` naming the three-Hebrew-roots-to-single-Thai principle + the subject-tracking strategy + the Rom 9:18 + Jn 12:40 cross-references, to lock the precedent before Isa 6:10 + Deut 2:30 + Josh 11:20 + 1 Sam 6:6 (4 more OT occurrences) and the NT trajectory ship? The translation surface is fine; the doc-lift is purely forward-protection.

---

## Item G — EXO 33:14-15 "פָּנִים my face/presence" diverges from `hebrew_idioms_and_metaphor_2026-05.md` lock

**The textual question:** The Sinai-theophany cluster of Exodus 33–34 has five פָּנִים occurrences with two distinct Thai conceptual mappings within the same chapter:

| Verse | Hebrew | Thai (current) | Mapping |
|---|---|---|---|
| **33:11** | פָּנִים אֶל־פָּנִים | **หน้าต่อหน้า** | "face-to-face" (literal) |
| **33:14** | פָּנַי יֵלֵכוּ | **การประทับของเรา** | "my presence" (paraphrase) |
| **33:15** | אִם־אֵין פָּנֶיךָ הֹלְכִים | **การประทับของพระองค์** | "your presence" (paraphrase) |
| **33:20** | לֹא תוּכַל לִרְאֹת אֶת־פָּנָי | **ใบหน้าของเรา** | "my face" (literal) |
| **33:23** | וּפָנַי לֹא יֵרָאוּ | **ใบหน้าของเรา** | "my face" (literal) |

**The doc gap:** Per `hebrew_idioms_and_metaphor_2026-05.md`, "presence-of-YHWH / face-of-YHWH" should consistently render as **เบื้องพระพักตร์ / พระพักตร์** in the Eremos OT corpus (uniform royal-Thai for face-of-divine-figure). The Exod 33:14-15 paraphrase to **การประทับ** is the NIV/ESV English convention but **drifts from the project's own corpus-doc**.

**The exegetical stake:** The theological tension at Exod 33 is **Moses asks to see God's "face" but God says "my face will not be seen," while at the same time God says "my face will go with you"**. The Hebrew lemma is uniform — פָּנִים at 33:14-15 is the same word as פָּנִים at 33:20+23. The Thai lemma-shift (presence/face) dilutes the theological-paradox at the heart of the pericope.

**Two resolution paths:**

(a) **Normalize per the existing doc** — render all 5 occurrences with **พระพักตร์** (royal-Thai for face). 33:14 → "พระพักตร์ของเราจะไปกับเจ้า" / 33:15 → "ถ้าพระพักตร์ของพระองค์ไม่ไปกับพวกข้าพระองค์...". Reads as "my royal-face will go with you" — works in Thai royal-register (similar to Thai court usage of พระพักตร์ for kings + divine figures). Cost: 4 verse edits (33:14, 33:15, plus normalize 33:20+23 from ใบหน้า to พระพักตร์ to match the doc's full register-lock).

(b) **Doc-amend** — recognize that the NIV/ESV "presence" tradition is principled at 33:14-15 specifically (where the Hebrew has agentive-verb-complement "face will go") and amend `hebrew_idioms_and_metaphor_2026-05.md` with a sub-rule: when פָּנִים takes an agentive verbal-complement → "การประทับ" (presence); when פָּנִים takes a sensory verb → "พระพักตร์" (royal-face).

**Question:** Which option preserves the Exod 33 theological-paradox while serving Thai-reader experience? The current rendering follows the dominant English-Bible tradition (NIV/ESV-style face/presence split) but **drifts from the project's own corpus-doc**. Should the doc be amended to ratify the current rendering (option b), or should the verses be normalized to match the doc (option a)?

---

## Item H — EXO 40:20 כַּפֹּרֶת "atonement-cover" within-book drift: 8× พระที่นั่งกรุณา vs. 1× ที่ลบล้างบาป

**The drift:** The atonement-cover atop the Ark is named at 9 places in Exodus. Eight render as **พระที่นั่งกรุณา** ("throne of grace") — the single 40:20 occurrence renders as **ที่ลบล้างบาป** ("place that wipes-away sin"):

| Verse | Thai | Rendering |
|---|---|---|
| 25:17 — first occurrence (instruction) | **พระที่นั่งกรุณา** | throne-of-grace |
| 25:18, 25:22 (instruction) | **พระที่นั่งกรุณา** | (same) |
| 30:6 (incense altar placement) | **พระที่นั่งกรุณา** | (same) |
| 37:6, 37:7, 37:8-9 (execution) | **พระที่นั่งกรุณา** | (same) |
| **40:20** (final installation) | **ที่ลบล้างบาป** | atonement-cover (**DRIFT**) |

**The two readings** of kapporet:
- **Throne-of-grace / mercy-seat** (rabbinic + classical-Christian + KJV/THSV tradition): God's throne above the cherubim; the כפר etymology is "cover" understood as "covering-throne."
- **Atonement-cover** (modern critical + ESV/NRSV tradition; recovers the כפר root "atone / cover-for-sin"): the cover above the Ark where blood is applied for atonement (Lev 16). The LXX/Pauline tradition reads ἱλαστήριον at Rom 3:25 (where it recapitulates kapporet directly), and Heb 9:5 names "the kapporet" with the same etymological-atonement weight.

**Cross-corpus implications.** The decision compounds into:
- **Lev 16** (Yom Kippur — the kapporet-blood-application ritual; the central OT atonement-text)
- **Rom 3:25** (Christ presented as ἱλαστήριον — the locus classicus of Pauline atonement-theology)
- **Heb 9:5** (the only NT explicit mention of "the kapporet")

**Two resolution paths:**

(a) **Normalize 40:20 to พระที่นั่งกรุณา** — matches the 8 prior occurrences; preserves the throne-image (rabbinic + classical-Christian reading: God's throne above the cherubim); matches THSV. Cost: 1 verse edit. Simpler; loses the etymological-atonement signal at 40:20.

(b) **Normalize all 9 to ที่ลบล้างบาป** — recovers the כפר-atonement etymology; matches the NT-corpus's Rom 3:25 (ἱλαστήριον = kapporet directly); matches Heb 9:5 + modern critical translations. Cost: 8 verse edits. Lexically transparent on the כפר-atonement etymology.

(c) **Doc-lift** — write `docs/translator_decisions/kapporet_atonement_cover_2026-05.md` choosing between (a) and (b) and naming the cross-corpus rationale.

**Question:** Should the kapporet rendering be normalized to a single Thai across all 9 Exodus occurrences, and should the project write a corpus-doc locking the choice + the Rom 3:25 + Heb 9:5 NT cross-references? The decision is one of the most-consequential atonement-vocabulary choices in the OT corpus — it shapes the Thai reader's reception of Pauline propitiation-theology.

---
