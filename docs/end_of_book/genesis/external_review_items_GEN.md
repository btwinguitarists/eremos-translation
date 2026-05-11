## Item A — GEN חֶסֶד (chesed) cross-corpus drift across 5 verses vs. the freshly-locked corpus-doc

**The drift:** The corpus-doc `docs/translator_decisions/chesed_covenant_love_2026-05.md` (decided 2026-05-09, Ben + cross-AI consensus, post-Jonah audit) locks **ความรักมั่นคง** as the corpus-default for חֶסֶד across the entire OT. Genesis was translated mostly BEFORE the doc was written, so 5 of 11 occurrences use older drafting renderings:

| Verse | Hebrew | Thai (current) | Compliant with `chesed_covenant_love_2026-05.md`? |
|---|---|---|---|
| **GEN 19:19** | וַתַּגְדֵּל חַסְדְּךָ | **ทรงสำแดงพระกรุณาอันยิ่งใหญ่** | ✗ DRIFT (uses พระกรุณา) |
| GEN 20:13 | חַסְדֵּךְ אֲשֶׁר תַּעֲשִׂי | **ความรักมั่นคงที่เจ้าจะกระทำ** | ✓ |
| **GEN 21:23** | כַּחֶסֶד אֲשֶׁר־עָשִׂיתִי | **ความเมตตา** | ✗ DRIFT (uses ความเมตตา) |
| GEN 24:12 | וַעֲשֵׂה־חֶסֶד עִם אֲדֹנִי | **ความรักมั่นคง** | ✓ |
| GEN 24:14 | עָשִׂיתָ חֶסֶד עִם־אֲדֹנִי | **ความรักมั่นคง** | ✓ |
| GEN 24:27 | חַסְדּוֹ וַאֲמִתּוֹ | **ความรักมั่นคงและความซื่อสัตย์** | ✓ (matches doc's word-pair lock exactly) |
| GEN 24:49 | חֶסֶד וֶאֱמֶת | **ความรักมั่นคงและความซื่อสัตย์** | ✓ |
| **GEN 32:11** | מִכֹּל הַחֲסָדִים וּמִכָּל־הָאֱמֶת | **พระคุณทั้งสิ้นและความซื่อสัตย์ทั้งสิ้น** | ✗ DRIFT (uses พระคุณ — a fourth Thai rendering of the lemma) |
| **GEN 39:21** | וַיֵּט אֵלָיו חָסֶד | **ทรงสำแดงความเมตตาต่อเขา** | ✗ DRIFT |
| **GEN 40:14** | וְעָשִׂיתָ־נָּא עִמָּדִי חָסֶד | **แสดงความเมตตาต่อข้าพเจ้า** | ✗ DRIFT |
| GEN 47:29 | חֶסֶד וֶאֱמֶת | **ความรักมั่นคงและความซื่อสัตย์** | ✓ |

**Cross-corpus context:** The Ruth lock (RUT 1:8, 2:20, 3:10) is **ความรักมั่นคง**; Jonah was retroactively normalized after its end-of-book audit (the Jonah audit's Item A — JON 2:9 + 4:2 — was the trigger that produced the corpus-doc); now Genesis exhibits the same drift Jonah had, only at five times the scale. The Pentateuch will recite Exod 34:6's רַב־חֶסֶד (≈ 9 OT recurrences) — without normalizing Genesis the cross-corpus thread is broken before Exodus 34 ships.

**Why the drift is consequential:** Without normalization, a typical Thai reader following חֶסֶד across Genesis 19 → 21 → 24 → 32 → 39 → 40 → 47 sees four different Thai phrases (ความรักมั่นคง / ความเมตตา / พระกรุณา / พระคุณ) for the same Hebrew lemma — the surface lemma-recognition fails. The 24-cluster (24:12, 14, 27, 49) and the 47:29 deathbed-oath are correctly locked; the 19, 21, 32, 39, 40 are not.

**Recommended retroactive normalization:**

| Verse | Drift Thai | Recommended Thai |
|---|---|---|
| 19:19 | …ทรงสำแดง**พระกรุณาอันยิ่งใหญ่**แก่ข้าพระองค์… | …ทรงสำแดง**ความรักมั่นคงอันยิ่งใหญ่**แก่ข้าพระองค์… (preserve the וַתַּגְדֵּל intensifier) |
| 21:23 | แสดง**ความเมตตา** | แสดง**ความรักมั่นคง** |
| 32:11 | **พระคุณทั้งสิ้น**และความซื่อสัตย์ทั้งสิ้น | **บรรดาความรักมั่นคง**และความซื่อสัตย์ทั้งปวง (matches doc row-3 חֲסָדִים-plural) |
| 39:21 | ทรงสำแดง**ความเมตตา**ต่อเขา | ทรงสำแดง**ความรักมั่นคง**ต่อเขา |
| 40:14 | แสดง**ความเมตตา**ต่อข้าพเจ้า | แสดง**ความรักมั่นคง**ต่อข้าพเจ้า |

**Two questions:**
1. Should Genesis 19:19, 21:23, 32:11, 39:21, 40:14 be retroactively normalized to **ความรักมั่นคง** per the corpus-doc lock, before tagging `book-genesis-v1`? The cost is 5 surgical verse-edits + re-running per-chapter checks; the benefit is restoring the cross-corpus lemma-thread before Exodus 34 ships.
2. Should `chesed` be added to the rules table in `scripts/check_key_term_consistency.py` after the §A normalization commits, so future OT-book ships are auto-protected? Currently the per-chapter checker did not flag this drift (the lemma is not in its rules table).

---

## Item B — GEN 3:16 תְּשׁוּקָה reading: polysemy preserved, Gen 4:7 parallel undocumented at surface

**The textual question:** The Eden-curse on the woman ends with אֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ וְהוּא יִמְשָׁל־בָּךְ — Eremos: **"ความปรารถนาของเจ้าจะอยู่ที่สามีของเจ้า และเขาจะปกครองเจ้า"** ("your desire will be toward your husband, and he will rule over you").

The lemma תְּשׁוּקָה occurs only **3× in the entire OT**:

| Verse | Hebrew | Sense | Thai (current Eremos) |
|---|---|---|---|
| **GEN 3:16** | אֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ | woman's desire toward husband (Eden-curse) | **ความปรารถนา** |
| **GEN 4:7** | אֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ | sin's desire toward Cain (controlling, predatory) | **ความปรารถนา** (sin-personified-as-predator) |
| Song 7:11 | אֲנִי לְדוֹדִי וְעָלַי תְּשׁוּקָתוֹ | beloved's desire (sexual / romantic) | (NT-corpus shipped, but the OT Song-corpus has not yet shipped) |

**The exegetical lock:** The 3:16 → 4:7 verbal-echo is **identical in structure** (`אֶל-X תְּשׁוּקַת-Y וְ-X יִמְשָׁל בְּ-Y` — "X's desire is for Y, and Y will rule over X"). At 4:7 the meaning is unambiguous — sin is a personified predator-power that desires-to-control Cain, who must master it. The lemma carries the same controlling/predatory weight at 3:16 by exact-construction parallel; this is the strongest exegetical lock in the chapter. ESV (post-2016 update) renders 3:16 explicitly as "Your desire shall be **contrary to** your husband, but he shall rule over you" — controlling-reading committed to the surface.

**The Eremos position:** **ความปรารถนา** is polysemous in Thai (covers (1) sexual / affectionate, (2) controlling / predatory, (3) general yearning). The verse-level KD preserves the polysemy without committing the rendering to one reading. This is principled and matches the project's "preserve dual-sense" stance at JON 4:11 — but it leaves modern Thai-evangelical readers (and theological reviewers) without an editorial signal on the most-disputed verse in modern Christian gender discourse. The 4:7 parallel's verbal-echo is dim in Thai because **ความปรารถนา** at both verses reads as plain "desire" without the predatory weight.

**Three resolution paths:**

(a) **Current** — preserve polysemy with **ความปรารถนา**; let the 4:7 parallel + the verse notes carry the controlling-reading signal. Lowest-risk.

(b) **Lift the controlling-reading into the surface** — render 3:16 as e.g. **"ความปรารถนาของเจ้าจะมุ่งครอบครองสามี และเขาจะปกครองเจ้า"** (your desire will seek-to-control your husband...). Locks the 4:7 parallel; matches ESV-2016 + complementarian readings.

(c) **Inline parenthetical / Layer-2 footer** — keep current Thai + add a Layer-2 entry to `output/textual_variants/genesis_03.json` (currently the chapter has only the tetragrammaton-first-occurrence entry) explicitly documenting the 3:16 → 4:7 verbal-echo + the three-reading question + the ESV-2016 / NIV / NRSV split.

**Why this matters forward:** The decision compounds into the related verses 1:27–28 (image-of-God / male-and-female), 2:18 (עֵזֶר helper), 2:24 (one-flesh marriage), Eph 5:21–33, 1 Cor 11, 1 Tim 2 — a multi-corpus thread that will be the focus of every Thai theological reviewer. The project's `gender_passages_thai_register_2026-05.md` doc has not yet been written; locking 3:16 first is the precedent-setting step.

**Two questions:**
1. Should Genesis 3:16 commit the surface rendering to one of the three readings (option a, b, or c above), or remain at polysemy-preserving **ความปรารถนา** with the choice explicitly named in a Layer-2 footer? Modern Thai-evangelical readers will likely default to a sexual-affection reading (the most-common Thai sense of ปรารถนา in romantic register) without explicit signal.
2. Should the project write `docs/translator_decisions/gender_passages_thai_register_2026-05.md` now (locking-precedent: this verse), to coordinate the editorial stance across Gen 1:27 + 2:18 + 2:24 + Eph 5:21–33 + 1 Cor 11 + 1 Tim 2 before the Pauline-epistles' gender-passage references compound? The doc would name the three readings + the ESV-2016 / NIV / NRSV split + the project's chosen surface-stance + the rationale.

---

## Item C — GEN 3:15 protoevangelium: ผู้นั้น singular vs. corporate-or-singular ambiguity

**The textual question:** Hebrew at 3:15: וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה וּבֵין זַרְעֲךָ וּבֵין זַרְעָהּ **הוּא** יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב.

Three exegetical decisions stack at this verse (the "first gospel"):

1. **זֶרַע "seed"** — singular morphology, corporate syntax. Eremos: **พงศ์พันธุ์** (singular Thai noun, corporate-allowable by context).
2. **הוּא pronoun** — referent-ambiguous (corporate-seed vs. individual-Christological-seed). Eremos: **ผู้นั้น** (singular-individual masculine) — commits the rendering to the **individual-seed Christological reading**.
3. **שׁוּף verb** — same root for both head-strike and heel-strike (asymmetric weight via context). Eremos: **ทำให้…ฟกช้ำ** preserved on both sides.

**The editorial decision:** Eremos's **ผู้นั้น** matches the LXX αὐτὸς (singular masculine) + Vulgate ipse + Targum messianic readings + Rom 16:20 ("the God of peace will crush Satan under your feet") + Heb 2:14 + Rev 12:17 NT trajectory. The rendering is **defensible** — it makes the protoevangelium reading visible to a typical Thai-evangelical reader without requiring access to the verse notes — but it is **stronger than the Hebrew alone justifies**. THSV has **เขา** (he, ambiguous singular-or-corporate); NIV / ESV use "he" (English's singular pronoun masks the corporate-or-individual question).

**Two readings:**
(a) **Individual-Christological** (Eremos's current reading; LXX + Vulgate + classical Christian) — the seed-of-the-woman is a singular descendant who will bruise the serpent's head; protoevangelium reading.
(b) **Corporate-or-individual** (modern critical, some evangelical) — the seed-of-the-woman is the entire human-line in conflict with the serpent-line; the singular-pronoun is a Hebrew-syntactic choice not a referential commitment.

**Question:** Should the project endorse the Christological-individual reading explicitly via the **ผู้นั้น** rendering + a Layer-2 footer that names the LXX αὐτός / Vulgate ipse / Rom 16:20 NT trajectory; OR move to the more-neutral **เขา** with extended `notes` documenting the Christological reading's manuscript + tradition support? The current rendering forecloses the corporate-or-collective reading without explicit editorial signal.

---

## Item D — GEN 6:1–4 בְּנֵי הָאֱלֹהִים + Nephilim: literal-rendering preserves polysemy, but reader-default

**The textual question:** Genesis 6:1–4 has the cryptic verse-pair: וַיִּרְאוּ בְנֵי־הָאֱלֹהִים אֶת־בְּנוֹת הָאָדָם כִּי טֹבֹת הֵנָּה ("the sons of God saw that the daughters of men were beautiful…"). Three Christian-tradition readings:

| Reading | Source | Implication |
|---|---|---|
| **Sethite-line** | Augustine + Reformed mainstream | Godly-line of Seth marrying Cainite women; "sons of God" = covenant-line members |
| **Royal / aristocratic** | Rabbinic minority | Kings / nobles marrying commoners |
| **Angelic / supernatural** | 1 Enoch + 2 Pet 2:4 + Jude 6 + most pre-Augustinian church | Divine-council members crossing the boundary with humans |

**The exegetical lock at Job:** The exact phrase **בְּנֵי הָאֱלֹהִים** appears 3 more times in the Hebrew Bible — Job 1:6, 2:1, 38:7 — all unambiguously referring to **divine-council members** (heavenly beings before YHWH's throne). Combined with Pss 29:1 + 89:6 (the parallel בְּנֵי אֵלִים), the lemma's primary OT sense is angelic / divine-council. The 2 Pet 2:4 + Jude 6 NT cross-references unambiguously read Gen 6 as the angelic-rebellion source.

**Eremos rendering:** Literal **บุตรของพระเจ้า** ("sons of God"). Polysemy preserved at the surface; readers can resolve via the verse-level KD or via the Layer-2 textual-variants footer.

**The reader-default concern:** A typical Thai-evangelical reader of **บุตรของพระเจ้า** alone will likely default to the **Sethite reading** (the dominant Reformed reading; matches THSV1971 expository tradition), because the angelic-reading is **counter-intuitive in Thai-evangelical theology** (the church's default is conservative-Augustinian). The Layer-2 entry in `output/textual_variants/genesis_06.json` does not currently expand on the three-reading question (only `tetragrammaton_convention_first_occurrence` is present).

**Question:** Should the project add an `interpretive_crux_footnote` Layer-2 entry to `output/textual_variants/genesis_06.json` that names the three readings + the Job 1:6 / 38:7 + Pss 29:1 / 89:6 OT parallels + the 2 Pet 2:4 / Jude 6 NT trajectory, so readers default-to-Sethite have explicit access to the manuscript-supported angelic reading? The decision compounds into the existing `spiritual_beings_hierarchy_2026-05.md` doc (which currently anchors the Daniel / Apocalyptic angelology — Genesis 6 needs a forward-anchor).

---

## Item E — GEN 49:10 שִׁילֹה: transliteration vs. messianic-paraphrase

**The textual question:** Jacob's deathbed blessing of Judah includes the famous crux: לֹא־יָסוּר שֵׁבֶט מִיהוּדָה וּמְחֹקֵק מִבֵּין רַגְלָיו עַד כִּי־יָבֹא **שִׁילֹה** וְלוֹ יִקְהַת עַמִּים. Eremos: **"…จนกว่า ชีโลห์ จะมา และความเชื่อฟังของชนชาติทั้งหลายจะเป็นของเขา"** ("…until Shiloh comes, and the obedience of the nations shall be his").

Three interpretive camps:

| Reading | Source | Thai surface |
|---|---|---|
| (1) **Place-name** "Shiloh" the city where the Ark rested (post-conquest; Joshua 18:1 etc.) | Modern critical, some Jewish | "until [the tribe] comes to Shiloh" |
| (2) **שֶׁלּוֹ "he-to-whom-it-belongs"** = the Messianic-king | Targum Onkelos (מְשִׁיחָא); LXX (τὰ ἀποκείμενα αὐτῷ "the things laid up for him"); Vulgate (qui mittendus est); classical Christian | "until he comes to whom it belongs" |
| (3) **Lectio difficilior** (unknown) | Modern critical agnosticism | preserves ambiguity |

**The Eremos position:** **`ชีโลห์`** transliteration. The 49:10 verse-level notes outline all three readings; the Layer-2 entry in `output/textual_variants/genesis_49.json` (type `translation_difficulty`) names the question.

**The reader-experience concern:** Transliteration **forecloses messianic-recognition** for typical Thai readers. **`ชีโลห์`** parses as either an unfamiliar place-name or an unfamiliar person-name; the Targum / LXX / Vulgate / classical Christian reading (where Shiloh = "the one to whom [the kingdom] belongs" = Messiah) is invisible at the surface. The 49:10 verse compounds into Rev 5:5 (Lion-of-the-tribe-of-Judah), Heb 7:14 (Christ from Judah), Mt 1:1–17 (Davidic genealogy) — all NT trajectories that read Jacob's-blessing-of-Judah Christologically.

**Three options:**

(a) **Current** — `ชีโลห์` transliteration; messianic reading lives in the notes. Defensible academic-stance.

(b) **Inline messianic** — render the second clause to disambiguate: **"…จนกว่า ผู้ที่สิทธิ์เป็นของเขา จะมา…"** (until he-to-whom-the-right-belongs comes). Locks the שֶׁלּוֹ reading; matches Targum + Vulgate + classical Christian tradition.

(c) **Footnote-elevated** — current Thai + a Layer-2 inline-marker at שִׁילֹה that more prominently surfaces the three-reading question for the reader, especially the שֶׁלּוֹ reading.

**Question:** Which option best serves the Thai reader's awareness of the 49:10 messianic-reading tradition? The verse is the OT's most-disputed messianic verse; the project's current stance (transliteration) is academically-honest but evangelical-readers will not see the protoevangelium-trajectory continuation that 3:15 + 22:18 ↔ 49:10 ↔ Mic 5:2 ↔ Mt 1:1–17 establishes.

---

## Item F — GEN 4:8 / 46:27 / 47:31: three different MT-vs-LXX-handling mechanisms; principle is implicit

**The pattern:** Three of the most-cited MT-vs-LXX divergences in Hebrew Bible scholarship appear in Genesis. Eremos handles each with a **different mechanism**, and the principle that distinguishes them is **nowhere documented at corpus level** — only at scattered verse-level KDs.

| Verse | MT reading | LXX reading | NT cross-reference | Eremos surface | Eremos Layer-2 |
|---|---|---|---|---|---|
| **GEN 4:8** | Cain's words to Abel are **silently absent** ("And Cain said to Abel his brother — [silence] — when they were in the field…") | LXX + SP + Syriac + Vulgate + Targums all add **"Let us go out to the field"** | n/a | **Inline brackets** in main text: `[**"ให้เราออกไปที่ทุ่งนากัน"**]` | Layer-2 entry type `textual_variant_lxx_addition` |
| **GEN 46:27** | **70 persons** descended into Egypt | **75 persons** (LXX adds 5 descendants of Joseph) | **Acts 7:14** cites LXX 75 | MT (**เจ็ดสิบคน**) | Layer-2 entry type `lxx_variant` documenting Acts 7:14 cross-ref |
| **GEN 47:31** | "Israel bowed at the head of the **bed**" (mittāh, מִטָּה) | "Israel bowed upon the top of his **staff**" (matteh, מַטֶּה) — same consonants, different vocalization | **Heb 11:21** cites LXX (πpoσεκύνησεν ἐπὶ τὸ ἄκρον τῆς ῥάβδου αὐτοῦ) | MT (**บนหัวเตียง**) | Layer-2 entry type `lxx_variant` documenting Heb 11:21 cross-ref |

**Three different mechanisms, three different decisions:**
- **4:8: LXX-addition brought into the main text in square brackets** (most-permissive — manuscript-supported gap-filler).
- **46:27 + 47:31: LXX-divergence excluded from the main text; Layer-2 footer only** (MT-priority — the LXX form is a different textual tradition, not a supplemental gap-fill).

The principle is **implicit**: 4:8 represents a **gap that cross-tradition manuscripts uniformly fill** (LXX, SP, Syriac, Vulgate, Targums all agree); 46:27 and 47:31 represent **legitimate textual-tradition divergences** where MT and LXX preserve parallel readings + only one can be on the surface. But this principle is **not documented at corpus level** — only at scattered verse-level KDs. The principle will compound massively across the OT (Joshua 21 missing-verse, 1 Sam 13:1 numerical gap, 1 Sam 17 Goliath-narrative LXX truncation, Jeremiah's MT-vs-LXX text-form dispute, Esther's LXX-additions, Ezra-Nehemiah's manuscript-divergences).

**Why this matters forward:** Without a corpus-doc, future OT-book ships will likely apply different mechanisms ad-hoc — exactly the pattern that produced the chesed cross-corpus drift Item A flagged. The NT corpus has `inclusion_variants_absent_verses_2026-04.md` (Tier 1/2/3 for SBLGNT-omits / mainstream-includes) covering its mirror-image situation; the OT side of the policy is the present gap.

**Two questions:**
1. Should the project write a corpus-doc `docs/translator_decisions/mt_vs_lxx_textual_variant_handling_2026-05.md` that names the three Genesis precedents (4:8 inline-bracket; 46:27 + 47:31 footer-only) + the principle that distinguishes them, before Joshua / Samuel / Jeremiah / Esther / Ezra-Nehemiah ship? The doc should explicitly cross-reference `inclusion_variants_absent_verses_2026-04.md` (NT-side companion).
2. Independently — is the **inline-square-bracket mechanism at 4:8 the right call**, or should the LXX-addition be relegated to Layer-2-only (matching 46:27 + 47:31), making the surface text MT-only across the entire OT? The 4:8 bracket-mechanism is currently the only place in the shipped corpus where a non-MT word-string appears in the main Thai text — a unique precedent whose principle deserves explicit naming.

---

## Item G — GEN 6:6–7 נָחַם divine-grief vs. divine-relenting subtype split

**The textual question:** Genesis 6:6–7 has the OT's first occurrence of the verb נָחַם (Niph'al) with God as subject:

- **Gen 6:6 (Hebrew):** וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם בָּאָרֶץ ("YHWH was sorry/relented that he had made man on the earth")
- **Gen 6:7 (Hebrew):** ...כִּי נִחַמְתִּי כִּי עֲשִׂיתִם ("for I am sorry/I relent that I have made them")

**The two senses of Niph'al-נָחַם:**

| Sense | Hebrew context | Thai rendering | Locked precedent |
|---|---|---|---|
| **Divine-grief** (reflexive-emotional, internal sorrow over creation/people-state) | Gen 6:6–7: God grieves over what creation has become; **no announced-decision-being-reversed** | **ทรงเสียพระทัย** | Gen 6:6 (proposed locking precedent) |
| **Divine-relenting** (factive-volitional, change of intended action away from announced judgment) | Jonah 3:9, 3:10, 4:2: God relents from announced destruction of Nineveh | **ทรงเปลี่ยนพระทัย** | Jon 3:10 (per `nicham_divine_relenting_2026-05.md`, locked 2026-05-09) |

**The Eremos rendering at Gen 6:6–7:** **ทรงเสียพระทัย** ("be-sorrowful in royal-Thai"). This is the **divine-grief sub-rendering** — distinct from the Jonah-locked **ทรงเปลี่ยนพระทัย** ("change [royal] mind"). The Gen 6 narrative-context unambiguously supports the divine-grief sense (the lament-frame of vv.5–7; the absence of any prior-announcement-of-judgment that would be reversed; the parallel `וַיִּתְעַצֵּב אֶל־לִבּוֹ` "and he was grieved to his heart" in 6:6b which the Eremos rendering preserves).

**The doc gap:** `nicham_divine_relenting_2026-05.md` v0.1 (decided 2026-05-09 in the Jonah audit) locks **ทรงเปลี่ยนพระทัย** as the corpus-default for divine-נָחַם but does NOT distinguish the two sub-senses. **Gen 6:6 is the OT's first divine-נָחַם occurrence** and the locking precedent for the divine-grief sub-rendering. Without a doc-amendment that recognizes the split, future OT books with divine-נָחַם verses (Ex 32:14 — divine-relenting; 1 Sam 15:11+35 — both senses present in different verses; Ps 106:45 — divine-relenting; Jer 18:8+10 — divine-relenting; Joel 2:13–14 — divine-relenting; Amos 7:3+6 — divine-relenting) will likely default to ทรงเปลี่ยนพระทัย and miss the divine-grief contexts where Gen 6:6 sets the precedent.

**The Num 23:19 / 1 Sam 15:29 counter-formulae** (לֹא יִנָּחֵם "[God] does not change his mind") apply to the **factive-volitional** sub-sense; the divine-grief sub-sense is not contradicted by them. A reader reconciling Gen 6:6 with Num 23:19 needs to see the sub-sense distinction explicitly — otherwise the surface paradox is unresolvable.

**Two questions:**
1. Should `nicham_divine_relenting_2026-05.md` be amended to split the lemma into two sub-rules — **ทรงเสียพระทัย** for divine-grief (reflexive-emotional, no decision-reversal) and **ทรงเปลี่ยนพระทัย** for divine-relenting (factive-volitional, decision-reversal-from-announced-judgment) — with Gen 6:6 as the locking precedent for the divine-grief sub-rule?
2. Is **ทรงเสียพระทัย** the right Thai for the divine-grief sense, or would **ทรงโทมนัส** / **ทรงเศร้าพระทัย** / another rendering capture the sense better? The Hebrew also has the parallel verb **עָצַב** (Hithpael, "grieved") in 6:6b which Eremos renders **ทรงเสียพระทัยในส่วนลึกของพระหฤทัย** — locking ทรงเสียพระทัย at 6:6 keeps the verbal-pair (נָחַם / עָצַב) on the same Thai vocabulary which is principled.

---

## Item H — Joseph receives Rachasap (ทรง-) honorific in 4 verses: vizier-of-Egypt vs. patriarch register

**The textual question:** The honorifics-binding check (`scripts/check_honorifics_binding.py`) flags 3 warnings in GEN 50 + 1 in GEN 44 + 1 in GEN 45 where **Joseph is the grammatical subject of a verb prefixed with ทรง-** (the royal-Thai prefix reserved per `ot_register_policy_2026-05.md` §2.2 for divine subjects, foreign emperors, and Hebrew kings — explicitly NOT for patriarchs):

| Verse | Thai (current) | Joseph's role at this moment |
|---|---|---|
| GEN 44:1 | โยเซฟ**ทรงสั่ง**คนต้นเรือนของพระองค์ว่า | Vizier-of-Egypt: commanding household staff |
| GEN 45:1 | โยเซฟ**ทรงเปิดเผยพระองค์**ต่อพี่น้องของพระองค์ | Vizier-of-Egypt: revealing identity to brothers in his palace |
| GEN 50:1 | โยเซฟ**ทรงโผลง**บนหน้าของบิดา **ทรงร้องไห้**บนท่าน และจูบท่าน | Personal/family: grieving father's death |
| GEN 50:2 | โยเซฟ**ทรงสั่ง**ผู้รับใช้ของพระองค์ คือหมอ ให้รักษาศพบิดาของพระองค์ | Vizier-of-Egypt: commanding embalmers (state-resourced) |

**The policy-doc text** (`ot_register_policy_2026-05.md` §2.2):

| Subject | Narrator-voice |
|---|---|
| **Patriarchs (Abraham, Isaac, Jacob, Joseph)** | **Plain narrator** (treat as venerated-elders, not kings); Rachasap **inappropriate** for tribal-patriarch role |
| **Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, Darius, Xerxes)** | **Rachasap (ทรง)** — they are imperial sovereigns of their narratives, even if villainous |
| **Foreign vassal-rulers, governors (Pekah, Hazael, etc.)** | **Plain** (they are lower than the imperial level) |

Joseph is **explicitly classified as a patriarch** (plain) in the doc; his vizier-role at Pharaoh's court would also fall under "vassal-rulers, governors" (plain). Either way, the doc requires plain register. The current ทรง- treatment is therefore a **Rachasap-policy violation** by the letter of the doc.

**Why this drift may have happened:** The Joseph-vizier role at Pharaoh's court occupies the highest non-royal Egyptian office (per Gen 41:40–44 his investiture as second-only-to-Pharaoh, with signet ring + linen robes + gold chain + Pharaoh's chariot + the title `אַבְרֵךְ`). The narrator's careful dignification of Joseph's actions — commanding staff, revealing identity to brothers in formal court setting, weeping over father's death, ordering embalmers — may have triggered an instinctive Rachasap-elevation. But the current doc is unambiguous about patriarchs (plain) regardless of office held.

**Three resolution paths:**

(a) **Strict policy compliance** — strip ทรง- from the 4 verses; render `โยเซฟสั่ง...`, `โยเซฟเปิดเผยตัว...`, `โยเซฟโผลง...`, `โยเซฟสั่ง...`. Matches the doc's current letter. The narrative loses some dignification but the policy-thread holds across all patriarchs (Abraham + Isaac + Jacob never receive ทรง- either; only the Joseph-vizier verses drift).

(b) **Joseph-as-vizier policy amendment** — add a sub-rule to `ot_register_policy_2026-05.md` §2.2 that distinguishes patriarchal-narrative-Joseph (chs.37–41 + 50 personal/family contexts → plain) from vizier-of-Egypt-public-office-Joseph (chs.41:40+ public-office contexts → Rachasap). The 4 affected verses split: 50:1 is personal grief at father's death (would shift to plain under (b)); 44:1 + 45:1 + 50:2 are public-office actions (would stay ทรง- under (b)). Daniel-as-Babylonian/Persian-vizier (chs.2, 5, 6) is the obvious cross-corpus parallel that would also benefit from this clarification.

(c) **Defer to Thai-language-reviewer voice** — Joseph's register may be one of the cases where the Thai-natural reading benefits from a slight elevation that doesn't cleanly match the doc's binary patriarch-vs-emperor split. The current Thai may sound stilted-but-respectful in a way that Thai readers accept as fitting Joseph's narrative arc.

**Two questions:**
1. Should the project amend `ot_register_policy_2026-05.md` §2.2 to add the Joseph-as-vizier-public-office distinction (option b above), or strip the ทรง- from the 4 verses to comply with the current doc letter (option a)? The decision compounds into Daniel and to a lesser extent Mordecai (Esther 8–10).
2. Independent of (1): for the 50:1 personal-grief verse specifically — does the Joseph-weeping-over-father's-corpse moment warrant the Rachasap (which marks the gravity of the patriarchal-succession transition Joseph now embodies), or should it strictly take plain narrative as the personal-grief register?
