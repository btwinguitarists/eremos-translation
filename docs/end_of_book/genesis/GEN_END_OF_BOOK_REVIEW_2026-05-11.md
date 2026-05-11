# Genesis — End-of-Book Review

**Date:** 2026-05-11
**Scope:** All 50 chapters (1,533 verses); `glossary.json`; existing `docs/translator_decisions/` (66 docs incl. the chesed/Exod-34/nicham/manah/leitwort docs landed via the post-Jonah commit `0344376`).
**Trigger:** GEN 50 shipped (commit `515121a`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Third OT book in the corpus** (after Ruth + Jonah) and **first OT book of substantial length / first Pentateuch book**.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **22 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 50/50 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-184-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks; `git status output/` clean except a harmless re-run of `output/check_reports/divine_names.md`.
- **Genesis is the LARGEST OT book yet** in the corpus by an order of magnitude (50 chapters / 1,533 verses vs. RUT 4 + JON 4). It exercises every OT-corpus lock landed during W1 OT-extension work and the post-Ruth/post-Jonah corpus-doc additions, plus several Genesis-distinctive patterns (toledot-genealogies; patriarchal-narrative cycles; Eden + Flood + Babel + Akedah cruxes; the famous LXX-vs-MT divergence cluster at 4:8 / 46:27 / 47:31 with their NT cross-references).
- **15 inherited locks + new OT-corpus docs verified compliant** in GEN (Tetragrammaton-as-`องค์พระผู้เป็นเจ้า` + Layer 2 first-occurrence footers; OT-register policy; divine-name table family — El Shaddai, El Elyon, El Olam, El Roi, יהוה־יִרְאֶה all per-table-locked; covenant-language; bara-as-`ทรงสร้าง`; proper-names + transliteration; proper-noun-wordplay; pagan-deities; honorifics; narrator/character voice; Hebrew-grammar-transfer; Hebrew-idioms-and-metaphor; verse-schema; Exod-34-attribute-formula sub-component; manah / leitwort handling).
- **8 cross-cutting Genesis-distinctive patterns are STABLE-and-locked** at corpus level (the 12-sons name-etymology cluster Gen 29:32–30:24; the patriarchal-name-changes Abram→Abraham 17:5, Sarai→Sarah 17:15, Jacob→Israel 32:28+35:10; Babel-counter-etymology 11:9; the Eden compound יהוה־אֱלֹהִים → `องค์พระผู้เป็นเจ้าพระเจ้า` 19×; the Joseph-narrative ירד-down + עלה-up trajectory; the Akedah μονογενής-typology hook at 22:2; the Eden-creation Logos hook at 1:1 echoed in Jn 1:1; the Joseph providence-arc capstone at 50:20).
- **2 items flagged STABLE-but-undocumented** (recommend new corpus docs): the LXX-textual-addition bracket convention (Gen 4:8 + the broader MT-vs-LXX policy needs a corpus-doc lift); the protoevangelium / messianic-reading register (Gen 3:15 ผู้นั้น singular + Gen 49:10 Shiloh + how messianic readings interact with the textual-variants Layer-2 footnote layer).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's confirmation): the Gen 3:15 ผู้นั้น singular reading (LXX αὐτός / Vulgate ipsa→ipse tradition vs. NIV/ESV "he"); the Gen 6:1–4 בְּנֵי הָאֱלֹהִים literal `บุตรของพระเจ้า` (preserves polysemy but Thai-evangelical-default reading is angelic-beings via 2 Pet 2:4 / Jude 6); the Gen 49:10 שִׁילֹה transliteration as `ชีโลห์` (vs. messianic-paraphrase per Targum-Onkelos / classical Christian reading).
- **4 items flagged DECIDE** (Ben choice needed before tagging `book-genesis-v1`):
  - **chesed cross-corpus drift across 5 Genesis verses** (19:19, 21:23, 32:11, 39:21, 40:14) that diverge from the freshly-locked `chesed_covenant_love_2026-05.md` — see §2.
  - **Gen 3:16 תְּשׁוּקָה reading** — see §8.
  - **Hebrew-source word-spacing absent in 25 of 50 chapters (GEN 26–50, ~766 verses).** The `hebrew` field of every verse in chapters 26 through 50 was extracted *without word-spaces* (a stripped concatenation of word-tokens with cantillation marks intact); chapters 1–25 are correctly spaced. This is a **data-integrity drift** in the verse JSON files that the existing checks did not flag (the `hebrew_field_integrity` check only catches Thai-character leakage and fabricated tokens). Reader-edition Hebrew-display + any downstream consumer of the `hebrew` field will read these chapters as run-on character strings. **Severity: MEDIUM** — does not affect the Thai translation surface but degrades reader-edition Hebrew transparency for half the book. **Recommend extraction-script audit + re-extraction of the 25 affected chapters.** See §16.
  - **`thai_literal` field is in ENGLISH (not Thai) for all 198 verses of GEN 44–50.** The Joseph-denouement + Jacob's-blessing + Joseph's-death narratives (chapters 44 through 50, the entire end of Genesis) have the `thai_literal` layer populated with English-language literal-translations rather than Thai. The main `thai` field is correctly Thai across all 50 chapters; only the literal-transparency layer drifted. **Severity: MEDIUM** — this is the field that scholarly readers + theological reviewers depend on for word-by-word transparency; English in this slot is unusable for Thai readers. **Recommend retroactive Thai re-rendering of the 198 affected `thai_literal` fields.** See §17.
- **External AI review (§3) pending.** Suggested 5-cluster packet at the end (one cluster per major narrative block).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + Eden compound + divine-name table family — **LOCKED**

156 occurrences of standalone יהוה (first at GEN 2:4 within the Eden compound; first standalone at GEN 4:1) across 31 chapters; uniform **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md`. Layer 2 first-occurrence footer notes present in 33 chapters. Genesis 1 has no Tetragrammaton (אֱלֹהִים-only chapter, by design); `output/textual_variants/genesis_01.json` is absent — a gap relative to the Ruth/Jonah convention but defensible because there is no first-occurrence to footnote. Recommend a one-line acknowledgement-stub if reader-edition layer expects per-chapter files; otherwise leave as-is.

The Eden-narrative compound **יהוה־אֱלֹהִים** (19× in Gen 2–3 + at 4:1) is uniformly **องค์พระผู้เป็นเจ้าพระเจ้า** (transparent concatenation), matching the Jonah 4:6 lock-precedent for the only other OT compound occurrence. Per-verse `key_decisions` records the underlying Hebrew at each occurrence.

The full divine-name family from the table is exercised correctly:

| Hebrew | Verses | Thai (current) | Lock status |
|---|---|---|---|
| יהוה | 156 (first 4:1) | **องค์พระผู้เป็นเจ้า** | LOCKED ✓ |
| יהוה־אֱלֹהִים | 19 (Gen 2–3 + 4:1) | **องค์พระผู้เป็นเจ้าพระเจ้า** | LOCKED ✓ |
| אֵל שַׁדַּי | 17:1, 28:3, 35:11, 43:14, 48:3, 49:25 | **พระเจ้าผู้ทรงมหิทธิฤทธิ์** | LOCKED ✓ |
| אֵל עֶלְיוֹן | 14:18, 14:19, 14:20, 14:22 (Melchizedek scene) | **พระเจ้าผู้สูงสุด** | LOCKED ✓ |
| אֵל עוֹלָם | 21:33 | **พระเจ้านิรันดร์** (in compound) | LOCKED ✓ |
| אֵל רֳאִי | 16:13 (Hagar) | **เอลโรอี (พระเจ้าผู้ทรงเห็นข้าพเจ้า)** — transliterated + parenthetical gloss | LOCKED ✓ |
| יהוה־יִרְאֶה | 22:14 | **ยาห์เวห์ยีเรห์** (place-name compound; transliterated per table §"place-name compounds") | LOCKED ✓ |
| אֱלֹהִים | 167 across 33 chapters | **พระเจ้า** | LOCKED ✓ |
| אֱלוֹהַּ | (rare in GEN) | n/a | — |
| יָהּ | (none in GEN) | n/a | — |

**LOCKED** ✓ — the divine-name family is the single most extensively-exercised lock in this book, and compliance is total. The table successfully scales from 4-chapter Ruth/Jonah to 50-chapter Genesis without any inconsistency.

---

## 2. חֶסֶד (chesed) — pre-lock-era Genesis drift across 5 verses — **DECIDE before tagging**

Eleven חֶסֶד occurrences across Genesis. **6 are compliant with the freshly-locked `chesed_covenant_love_2026-05.md`** (rendering: **ความรักมั่นคง**); **5 diverge with three different older renderings**:

| Verse | Hebrew | Thai (current) | Compliant? | Notes |
|---|---|---|---|---|
| 19:19 | וַתַּגְדֵּל חַסְדְּךָ | **พระกรุณาอันยิ่งใหญ่** | ✗ DRIFT | Lot to angels; intensifier וַתַּגְדֵּל compounded into adjective "อันยิ่งใหญ่" |
| 20:13 | חַסְדֵּךְ אֲשֶׁר תַּעֲשִׂי | **ความรักมั่นคงที่เจ้าจะกระทำ** | ✓ | Abraham to Sarah |
| 21:23 | כַּחֶסֶד אֲשֶׁר־עָשִׂיתִי | **ความเมตตา** | ✗ DRIFT | Abimelech-Abraham covenant |
| 24:12 | וַעֲשֵׂה־חֶסֶד עִם אֲדֹנִי | **ความรักมั่นคง** | ✓ | Servant's prayer; covenant register |
| 24:14 | עָשִׂיתָ חֶסֶד עִם־אֲדֹנִי | **ความรักมั่นคง** | ✓ | Same prayer |
| 24:27 | חַסְדּוֹ וַאֲמִתּוֹ | **ความรักมั่นคงและความซื่อสัตย์** | ✓ | Word-pair (chesed wĕ-ʾemet); matches table `chesed_covenant_love_2026-05.md` row 5 exactly |
| 24:49 | חֶסֶד וֶאֱמֶת | **ความรักมั่นคงและความซื่อสัตย์** | ✓ | Same word-pair |
| 32:11 | מִכֹּל הַחֲסָדִים וּמִכָּל־הָאֱמֶת | **พระคุณทั้งสิ้นและความซื่อสัตย์ทั้งสิ้น** | ✗ DRIFT | Jacob's prayer at the Jabbok crossing; uses **พระคุณ** (a fourth Thai rendering of chesed) |
| 39:21 | וַיֵּט אֵלָיו חָסֶד | **ความเมตตา** | ✗ DRIFT | Joseph in prison |
| 40:14 | וְעָשִׂיתָ־נָּא עִמָּדִי חָסֶד | **ความเมตตา** | ✗ DRIFT | Joseph to cupbearer |
| 47:29 | וְעָשִׂיתָ עִמָּדִי חֶסֶד וֶאֱמֶת | **ความรักมั่นคงและความซื่อสัตย์** | ✓ | Jacob's deathbed-oath to Joseph; word-pair |

**Editorial assessment:** The lock at `chesed_covenant_love_2026-05.md` was decided 2026-05-09, in the wake of the Jonah audit. Most of Genesis was translated BEFORE that date, so the 5 drift verses use the project's older drafting vocabulary (the same vocabulary the Jonah audit flagged as "two new renderings, neither matching Ruth"). The 6 compliant verses are mostly the late-Genesis word-pair instances (24:27/49, 47:29) plus the recently-touched-up 20:13 + 24:12/14. A typical Thai reader following חֶסֶד across Genesis sees four different Thai phrases (ความรักมั่นคง / ความเมตตา / พระกรุณา / พระคุณ) for the same Hebrew lemma — exactly the cross-corpus drift the corpus-doc was written to prevent.

**DECIDE before tagging — recommend retroactive normalization.** Five surgical edits:

| Verse | Drift Thai | Recommended Thai (per `chesed_covenant_love_2026-05.md`) |
|---|---|---|
| 19:19 | …ทรงสำแดง**พระกรุณาอันยิ่งใหญ่**แก่ข้าพระองค์… | …ทรงสำแดง**ความรักมั่นคงอันยิ่งใหญ่**แก่ข้าพระองค์… (preserve the וַתַּגְדֵּל intensifier) |
| 21:23 | แสดง**ความเมตตา**แก่ข้าพเจ้า | แสดง**ความรักมั่นคง**แก่ข้าพเจ้า |
| 32:11 | **พระคุณทั้งสิ้น**และความซื่อสัตย์ทั้งสิ้น | **บรรดาความรักมั่นคง**และความซื่อสัตย์ทั้งปวง (matches doc row 3 חֲסָדִים plural) |
| 39:21 | ทรงสำแดง**ความเมตตา**ต่อเขา | ทรงสำแดง**ความรักมั่นคง**ต่อเขา |
| 40:14 | แสดง**ความเมตตา**ต่อข้าพเจ้า | แสดง**ความรักมั่นคง**ต่อข้าพเจ้า |

After these revisions all 11 Genesis chesed-occurrences map cleanly to the doc; the cross-corpus thread (Ruth → Genesis → Jonah → Pss → Joel → Nah → Neh) is restored before Exodus 34:6 ships in the Pentateuch sequence.

**Followup:** the per-chapter check `check_key_term_consistency.py` did not flag this drift because **chesed is not in the `key_term_consistency` rules table yet** (it's a lemma-multi-rendering type that the consistency checker doesn't track). Recommend adding chesed to the rules table after the §A normalization commits, so future books are auto-protected.

---

## 3. Patriarchal name-changes (Abram→Abraham, Sarai→Sarah, Jacob→Israel) — **LOCKED**

Three covenant-renamings, all handled with explicit transition + per-verse documentation:

| Original | Renamed | Renaming verse | Pre-rename Thai | Post-rename Thai | Note |
|---|---|---|---|---|---|
| אַבְרָם | אַבְרָהָם | 17:5 | **อับราม** | **อับราฮัม** | Etymology "father-of-multitude" surfaced in 17:5 KD |
| שָׂרַי | שָׂרָה | 17:15 | **ซาราย** | **ซาราห์** | Both forms = "princess"; theological-shift documented |
| יַעֲקֹב | יִשְׂרָאֵל | 32:28 (+35:10 reaffirmation) | **ยาโคบ** | **อิสราเอล** | Wordplay שָׂרָה (wrestle) + אֵל (God); `proper_noun_wordplay` doc applied |

After the 32:28 renaming, both **ยาโคบ** and **อิสราเอล** are used in narrative — preserving the Hebrew text's free alternation (יַעֲקֹב 36×, יִשְׂרָאֵל 35× post-32:28). The narrator's choice of name often signals register (Israel = covenant-mode; Jacob = household / Joseph-cycle informal). **STABLE** ✓.

**Rachel's death-naming Benjamin** (Gen 35:18: בֶּן־אוֹנִי → בִּנְיָמִין) is the fourth name-change in Genesis: rendered **เบนโอนี** → **เบนยามิน** with the Rachel-grief vs. Jacob-blessing theological inversion documented at the verse-level. **LOCKED** ✓ per `proper_noun_wordplay_2026-05.md`.

---

## 4. The 12 sons' name-etymology cluster (Gen 29:32–30:24, 35:18) — **LOCKED**

Twelve consecutive paronomastic name-etymologies in two compressed narrative spans — Hebrew Bible's densest concentration of wordplay-naming. All 12 documented per `proper_noun_wordplay_2026-05.md`:

| # | Name | Hebrew root + paronomastic clause | Thai treatment |
|---|---|---|---|
| 1 | **Reuben** רְאוּבֵן | רָאָה ("see" — "YHWH has seen my affliction") | **รูเบน** + KD |
| 2 | **Simeon** שִׁמְעוֹן | שָׁמַע ("hear" — "YHWH heard I am unloved") | **สิเมโอน** + KD |
| 3 | **Levi** לֵוִי | לָוָה ("join" — "now my husband will be joined to me") | **เลวี** + KD |
| 4 | **Judah** יְהוּדָה | וָדָה ("praise" — "this time I will praise YHWH") | **ยูดาห์** + KD |
| 5 | **Dan** דָּן | דִּין ("judge" — "God has judged me") | **ดาน** + KD |
| 6 | **Naphtali** נַפְתָּלִי | פתל ("wrestle" — "I have wrestled wrestlings of God") | **นัฟทาลี** + KD |
| 7 | **Gad** גָּד | גַּד ("fortune" — "good fortune!") | **กาด** + KD |
| 8 | **Asher** אָשֵׁר | אָשֶׁר ("happy" — "women will call me happy") | **อาเชอร์** + KD |
| 9 | **Issachar** יִשָּׂשכָר | שָׂכָר ("wages" — "God has given me my wages") | **อิสสาคาร์** + KD |
| 10 | **Zebulun** זְבֻלוּן | זָבַד / זֶבֶד / זָבַל triple-play | **เศบูลุน** + KD (triple-hapax noted) |
| 11 | **Joseph** יוֹסֵף | אָסַף + יָסַף double-play (gather away [shame] + add [another son]) | **โยเซฟ** + KD (double wordplay) |
| 12 | **Benjamin** בִּנְיָמִין (vs. בֶּן־אוֹנִי) | יָמִין ("right hand / favor") vs. אוֹן ("sorrow") | **เบนยามิน** + KD (counter-etymological renaming) |

Each rendering follows the doc's principle: transliterate the name; surface the etymology in the verse-level KD + thai_summary; do NOT inline-paraphrase the name into the running Thai. **LOCKED** ✓.

Same pattern for **Cain** (Gen 4:1: קָנָה "acquire"), **Eve** (3:20: חַי "living"), **Noah** (5:29: נָחַם "comfort"), **Isaac** (17:17 / 18:12 / 21:6: צָחַק "laugh"), **Manasseh + Ephraim** (41:51–52: שָׁכַח "forget" / פָּרָה "fruitful"), and the place-names **Beersheba** (21:31, 26:33: dual שִׁבְעָה "seven" / שָׁבוּעַ "oath" wordplay), **Bethel** (28:19), **Mahanaim** (32:2), **Peniel** (32:30), **Beer-lahai-roi** (16:14), and the **Babel** counter-etymology (11:9: בָּלַל "confuse" defying Babylonian בָּב־אִלוּ "gate-of-god"). **LOCKED** ✓.

---

## 5. Anachronistic designations (Philistines, Dan, Ur of Chaldeans) — **STABLE (Layer-2 footers)**

Three corpus-acknowledged anachronisms in Genesis, all handled with MT-fidelity in the main text + Layer-2 reader-edition footnotes that surface the historical-chronology issue:

- **"Philistines"** (Gen 21:32, 26:1, 26:8, 26:14–15, 26:18) — Philistines proper settle coastal Canaan ~1200 BCE, several centuries after the patriarchal era. Rendered **ฟิลิสเตีย / คนฟิลิสเตีย** (THSV-aligned). Layer-2 footer notes the ANE-chronology question.
- **"Dan"** (Gen 14:14, "as far as Dan") — the tribe-name and the geographic-location named for the tribe both postdate Judges 18:29. Rendered **ดาน**. Layer-2 footer notes the post-conquest editorial provenance.
- **"Ur of the Chaldeans"** (Gen 11:28, 11:31, 15:7) — Chaldeans (Kaldu) not politically-dominant in southern Mesopotamia until ~1000 BCE. Rendered **อูร์ของชาวเคลเดีย** (or variants). Layer-2 footer notes the ANE-chronology issue.

The treatment is principled and consistent. **STABLE** ✓ — no action.

---

## 6. Famous textual divergences — Gen 4:8 (LXX-addition), 46:27 (70 vs. 75), 47:31 (bed vs. staff) — **STABLE-but-recommend-corpus-doc**

Three of the most-cited MT-vs-LXX divergences in Hebrew Bible scholarship, each handled with a different mechanism. There is no corpus-doc yet that names the principle behind the choice of mechanism.

### 6a. Gen 4:8 — LXX-addition "Let us go out to the field"

MT silently lacks Cain's words to Abel ("And Cain said to Abel his brother — [silence] — when they were in the field, Cain rose up against Abel..."); LXX, SP, Syriac, Vulgate, and Targums all add **εἴπωμεν εἰς τὸ πεδίον** ("Let us go out to the field"). Eremos's main Thai text **includes the addition in square brackets**:

> คาอินพูดกับอาเบลน้องชายว่า [**"ให้เราออกไปที่ทุ่งนากัน"**] เมื่อพวกเขาอยู่ในทุ่งนา…

The `thai_literal` layer preserves MT-only; the `output/textual_variants/genesis_04.json` Layer-2 entry (type `textual_variant_lxx_addition`) documents the manuscript evidence. This is the **first** LXX-textual-addition the OT-pilot has ingested via square-bracket inline-display rather than via Tier 3 ⟦double-bracket⟧ omission per RULES §5 inclusion-variants.

### 6b. Gen 46:27 — MT 70 vs. LXX 75 persons (cited in Acts 7:14)

MT: **70 persons** descended into Egypt. LXX: **75 persons** (adds 5 descendants of Joseph). Acts 7:14 (Stephen's speech) cites the LXX number. Eremos main Thai text uses **เจ็ดสิบคน** (MT 70); Layer-2 entry (type `lxx_variant`) documents the LXX divergence + the Acts 7:14 NT cross-reference.

### 6c. Gen 47:31 — MT "head of bed" vs. LXX "top of staff" (cited in Heb 11:21)

MT: וַיִּשְׁתַּחוּ יִשְׂרָאֵל עַל־רֹאשׁ הַמִּטָּה ("Israel bowed at the head of the **bed**"). LXX: ἐπὶ τὸ ἄκρον τῆς ῥάβδου ("upon the head of his **staff**") — same consonants (מטה), different vocalization (mittāh "bed" vs. matteh "staff"). Heb 11:21 cites LXX. Eremos main Thai text uses **บนหัวเตียง** (MT "head of bed"); Layer-2 entry (type `lxx_variant`) documents the LXX divergence + Heb 11:21 NT cross-reference.

**Three different mechanisms, three different decisions:**
- 4:8: LXX-addition **brought into main text** in square brackets (most-permissive).
- 46:27: LXX-divergence **excluded** from main text; Layer-2 footer only.
- 47:31: LXX-divergence **excluded** from main text; Layer-2 footer only.

The principle is implicit (4:8 is a manuscript-supported gap-filler with broad cross-tradition support; 46:27 and 47:31 are vocalization / counting differences where LXX preserves a different but parallel tradition rather than an MT-omission). **But the principle is nowhere documented at corpus level** — only at scattered verse-level KDs. This will compound massively across the OT (Joshua 21 missing-verse, 1 Sam 13:1 numerical gap, 1 Sam 17 Goliath-narrative LXX truncation, Jeremiah's MT-vs-LXX text-form dispute, Esther's LXX-additions, Ezra-Nehemiah's manuscript-divergences).

**→ Recommend new doc:** `docs/translator_decisions/mt_vs_lxx_textual_variant_handling_2026-05.md` — names the three Genesis precedents (4:8 inline-bracket; 46:27 + 47:31 footer-only) and the principle that distinguishes them. Should also cover the hapax יְהוָה־יִרְאֶה place-name compound (which is its own micro-decision: LXX has Κύριος εἶδεν "the Lord saw"). The doc should explicitly cross-reference the existing NT-corpus `inclusion_variants_absent_verses_2026-04.md` (Tier 1/2/3 for SBLGNT-omits / mainstream-includes) — the OT side of that policy is the present gap.

**STABLE** ✓ in current handling; **DOC LIFT RECOMMENDED** before Joshua / Samuel ship.

---

## 7. Gen 3:15 protoevangelium — **REVIEW (singular ผู้นั้น reading)**

Hebrew: וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה וּבֵין זַרְעֲךָ וּבֵין זַרְעָהּ **הוּא** יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב.

Three exegetical decisions stack at this verse:

1. **זֶרַע "seed"** singular vs. corporate. The Hebrew lemma is morphologically singular but syntactically often collective. Eremos: **พงศ์พันธุ์** (singular Thai noun; preserves Hebrew-singular-form, allows the corporate reading by context).
2. **הוּא pronoun** referent — corporate-seed (his offspring will war with hers) vs. individual-seed (a singular descendant will conquer the serpent). Eremos: **ผู้นั้น** ("that-one," singular-individual masculine). This commits the rendering to the **individual-seed Christological reading** (LXX αὐτὸς preserves singular; Vulgate famously has *ipsa* / *ipse* depending on edition; Rom 16:20 + Heb 2:14 + Rev 12:17 NT trajectory all read individually).
3. **שׁוּף verb** — Eremos: **ทำให้…ฟกช้ำ** ("bruise / cause-to-be-bruised"), preserving the same verb both directions of the asymmetric strike.

**Editorial assessment:** The **ผู้นั้น** singular-individual reading is theologically rich and matches the dominant NT-citation tradition, but it is **stronger than the Hebrew alone justifies**. The translator's verse-level KD names the protoevangelium tradition explicitly, but the Thai surface text is editorially loaded. THSV uses **เขา** (he, ambiguous singular-or-corporate); NIV / ESV use "he" (individual-leaning); some modern translations use a corporate "they."

**REVIEW flag:** Confirm Ben endorses **ผู้นั้น** (individual-Christological) over the more-neutral **เขา** (gender-marked but reference-ambiguous singular). The current rendering is defensible — it makes the protoevangelium reading visible to a typical Thai-evangelical reader without requiring access to the verse notes — but it does foreclose the corporate reading. Recommend either (a) confirm + add an explicit Layer-2 footer documenting the editorial choice, or (b) move to **เขา** with extended `notes` documenting the Christological reading's manuscript + tradition support.

---

## 8. Gen 3:16 תְּשׁוּקָה — **DECIDE (controlling-desire vs. polysemy preserved)**

Hebrew: וְאֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ וְהוּא יִמְשָׁל־בָּךְ. Eremos: **ความปรารถนาของเจ้าจะอยู่ที่สามีของเจ้า และเขาจะปกครองเจ้า** ("your desire will be toward your husband, and he will rule over you").

Two well-attested readings of תְּשׁוּקָה:
- (1) **Sexual / affectionate desire** — Song 7:10 parallel (the only other OT occurrence of the lemma).
- (2) **Controlling / predatory desire** — Gen 4:7 parallel (the third and final OT occurrence: sin's desire toward Cain), where the construction is **identical** (אֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ "its desire is for you, but you must rule over it"). The 4:7 sense is unambiguously controlling; the verbal echo at 3:16 → 4:7 is the strongest exegetical lock.

**Editorial assessment:** Eremos's **ความปรารถนา** is polysemous in Thai — it covers (1) and (2) and a great deal more (general yearning, craving, longing). The 3:16 KD preserves the polysemy without committing the rendering to one reading. This is principled, but it leaves modern Thai-evangelical readers (and theological reviewers) without an editorial signal on how to resolve the most-disputed verse in modern Christian gender discourse.

**Three resolution paths:**

(a) **Current** — preserve polysemy with **ความปรารถนา**; let the 4:7 parallel + the verse notes carry the controlling-reading signal. Lowest-risk; matches the project's "preserve dual-sense" stance at JON 4:11. But: the 4:7 parallel's verbal-echo is dim in Thai because **ความปรารถนา** at both 3:16 + 4:7 reads as plain "desire" without the predatory weight.

(b) **Lift the controlling-reading into the surface** — render 3:16 as **"ความปรารถนาของเจ้าจะมุ่งครอบครองสามี และเขาจะปกครองเจ้า"** (your desire will seek-to-control your husband...). Locks the 4:7 parallel to the surface; commits the rendering to the ESV-style controlling-reading.

(c) **Inline parenthetical** — render as current Thai + add an inline parenthetical at the second-half **(เปรียบ ปฐก. 4:7)** that triggers the reader's cross-reference to the next chapter's identical construction. Surfaces the parallel without overruling either reading.

**Ben to decide.** Recommend (a) + add a Layer-2 footer note in `output/textual_variants/genesis_03.json` (currently the chapter has only the tetragrammaton-first-occurrence entry) that names the 4:7 parallel as the exegetical-lock-toward-controlling-reading. Adds scholarly transparency without changing main text. The decision compounds into the doc-recommendation `gender_passages_thai_register_2026-05.md` (alongside Gen 1:27–28; 2:18 עֵזֶר; 2:24 marriage; Eph 5:21–33; 1 Cor 11; 1 Tim 2 — a multi-corpus thread).

---

## 9. Gen 6:1–4 בְּנֵי הָאֱלֹהִים + Nephilim — **REVIEW (literal `บุตรของพระเจ้า` preserves polysemy)**

Three readings in Christian tradition:
1. **Sethite-line** (Augustine + Reformed mainstream) — godly-line of Seth marrying Cainite women.
2. **Royal / aristocratic** (rabbinic minority) — kings / nobles marrying commoners.
3. **Angelic / supernatural** (1 Enoch + 2 Pet 2:4 + Jude 6 + most of pre-Augustinian church) — divine-council members crossing the boundary with humans. Job 1:6 / 2:1 / 38:7 use the **identical phrase** בְּנֵי הָאֱלֹהִים unambiguously for divine-council members.

Eremos: **บุตรของพระเจ้า** (literal "sons of God"; preserves polysemy). Layer-2 entry in `output/textual_variants/genesis_06.json` does not currently expand on the three-reading question (the type listed is `tetragrammaton_convention_first_occurrence`, not `interpretive_crux_footnote`).

**REVIEW flag:** Confirm Ben endorses the polysemy-preserving rendering. Two minor adjustments worth considering:
- (a) Add an `interpretive_crux_footnote` Layer-2 entry to `output/textual_variants/genesis_06.json` naming the three readings + the Job 1:6 / 38:7 parallel + the 2 Pet 2:4 / Jude 6 NT trajectory.
- (b) Confirm the Nephilim transliteration (currently **เนฟิลิม** per chapter-text spot-check) and its cross-reference to Num 13:33 (the only other OT occurrence).

The compound expression בְּנֵי הָאֱלֹהִים compounds forward into Job, Pss 29:1 + 89:6 (likewise rendered with `บุตรของพระเจ้า`?), and the angelological vocabulary of Daniel + Zechariah. Recommend the corpus-doc `spiritual_beings_hierarchy_2026-05.md` (which exists) be amended with a Genesis-6 sub-entry.

---

## 10. Gen 49:10 שִׁילֹה — **REVIEW (transliteration vs. messianic-paraphrase)**

Hebrew: לֹא־יָסוּר שֵׁבֶט מִיהוּדָה וּמְחֹקֵק מִבֵּין רַגְלָיו עַד כִּי־יָבֹא **שִׁילֹה** וְלוֹ יִקְהַת עַמִּים. Eremos: **"…จนกว่า ชีโลห์ จะมา และความเชื่อฟังของชนชาติทั้งหลายจะเป็นของเขา."**

Three interpretive camps:
- (1) **Place-name** — "Shiloh" the city where the Ark rested (post-conquest). Reading: "until [the tribe] comes to Shiloh."
- (2) **שֶׁלּוֹ "he-to-whom-it-belongs"** = the Messianic-king. Reading: "until he comes to whom it belongs." Targum Onkelos has מְשִׁיחָא ("the Messiah") here; Vulgate has *qui mittendus est*; classical Christian + LXX (τὰ ἀποκείμενα αὐτῷ) preserve the messianic reading.
- (3) **Unknown / lectio difficilior** — modern critical agnosticism.

Eremos's **transliteration `ชีโลห์`** preserves the term-ambiguity. The 49:10 verse-notes outline all three readings (per Layer-2 entry type `translation_difficulty`). The choice is **defensible** — it matches the modern-scholarly ambiguity-stance — but it **forecloses messianic-recognition** for typical Thai readers (who will not parse `ชีโลห์` as a messianic-name title).

**REVIEW flag:** Confirm Ben endorses the transliteration. Three options:
- (a) **Current** — `ชีโลห์` transliteration; messianic reading lives in the notes. Defensible academic-stance.
- (b) **Inline messianic** — render the second clause to disambiguate: "**…จนกว่าผู้ที่สิทธิ์เป็นของเขาจะมา…**" (until he-to-whom-the-right-belongs comes). Locks the שֶׁלּוֹ reading; matches Targum + Vulgate + classical Christian tradition.
- (c) **Footnote-elevated** — current Thai + a prominently-rendered Layer-2 inline-marker at שִׁילֹה pointing to the three readings. Surfaces the messianic-reading without overruling either.

The 49:10 verse compounds into Rev 5:5 (Lion-of-the-tribe-of-Judah) + Heb 7:14 + Mt 1:1–17 (Davidic genealogy). Recommend either (a) confirm + Layer-2 elevation, or (b) consider inline-paraphrase on the 49:10 weight alone.

---

## 11. Sexual + morally-difficult content register (Gen 19, 34, 38, 39) — **STABLE**

Four episodes with sexual / sexual-violence content:

| Passage | Hebrew register | Thai register | Sensitivity |
|---|---|---|---|
| Gen 19:5 (Sodom mob) | יָדַע ("know" = sexual-violence) | **รู้จัก** + contextual cues | Euphemistic-but-clear; matches biblical-Thai convention |
| Gen 34 (Dinah's violation) | עָנָה Pi'el ("humble/violate") | **ทำให้เสียสติ** / **นอนกับ** | Preserves assault-fact without exploitative detail |
| Gen 38 (Tamar / Judah) | יָדַע + שָׁכַב עִם | **รู้จัก** / **นอน** | Tamar's righteousness-defense (38:26 "צָדְקָה מִמֶּנִּי" → "นางชอบธรรมยิ่งกว่าเรา") preserves moral-frame |
| Gen 39 (Joseph + Potiphar's wife) | שָׁכַב עִם | **นอนกับ** | Joseph's resistance + chastity preserved as virtue-template |

Across all four, the project preserves Hebrew-clarity without sensationalism — the moral-weight lives in the surrounding narrative-frame, not in the sexual-vocabulary. **STABLE** ✓ — register-choice is principled and consistent.

---

## 12. Cosmogonic decisions — Gen 1:1–2 — **STABLE-and-locked**

- **Gen 1:1** "In the beginning" — independent-clause reading: **"ในปฐมกาล พระเจ้าทรงสร้าง..."** preserves the Hebrew-title-as-incipit convention (the book's Hebrew title בְּרֵאשִׁית is also its first word). Defensible against the dependent-clause reading ("when God began to create..."); matches mainstream English (ESV/NIV/CSB) + THSV convention.
- **Gen 1:2** רוּחַ אֱלֹהִים — Eremos: **พระวิญญาณของพระเจ้า** (Spirit of God), following LXX πνεῦμα τοῦ θεοῦ + mainstream evangelical reading. Documented at verse-level; the alternative ("wind from God") is preserved in the verse-notes for scholarly access.
- **Gen 1:26–27** "Let us make" plural-deliberation — Eremos: **ให้เราสร้างมนุษย์ตามฉายาของเรา ตามอย่างของเรา** (preserves the plural). Layer-2 entry references the three readings (royal-plural / heavenly-court / Trinitarian foreshadowing) without forcing one.
- **Gen 1:27** "in the image of God" — Eremos: **ตามพระฉายาของพระเจ้า**. The female-image clause (`וַיִּבְרָא אֹתָם זָכָר וּנְקֵבָה בָּרָא אֹתָם` "male and female he created them") is preserved with full-rendering, no-collapse. **STABLE** ✓.

**STABLE** ✓ — cosmogonic decisions are theologically careful and well-documented.

---

## 13. Akedah typology + μονογενής hook (Gen 22:2) — **LOCKED**

Hebrew: יְחִידְךָ ("your only-one"). Eremos: **บุตรคนเดียวของเจ้า** ("your only son"). LXX: μονογενής. NT inheritance: Jn 1:14, 1:18, 3:16, 3:18; 1 Jn 4:9 (Christ as μονογενής υἱός).

The Akedah-typology hook is preserved at the lexical level (the Thai **บุตรคนเดียว** mirrors the LXX μονογενής → NT μονογενής path). The verse-level KD names the staircase-narrowing rhetoric ("your son, your only-one, whom you love, Isaac") and the inclusio with Gen 12:1 (לֶךְ־לְךָ "go-yourself"), and surfaces Heb 11:19 (Isaac as "figuratively raised from dead"). **LOCKED** ✓ — the typological lemma-thread is Thai-traceable from Genesis to John.

---

## 14. Joseph providence-arc capstone (Gen 50:20) — **STABLE**

Hebrew: וְאַתֶּם חֲשַׁבְתֶּם עָלַי רָעָה אֱלֹהִים חֲשָׁבָהּ לְטֹבָה. Eremos: **"พวกท่านคิดร้ายต่อข้าพเจ้า แต่พระเจ้าทรงคิดให้กลายเป็นความดี…"** The verb חָשַׁב ("to plan / reckon / intend") is rendered consistently with the Gen 15:6 חָשַׁב (faith-reckoned-as-righteousness; → **ทรงนับ**), but in 50:20's context the planning sense yields **คิด** rather than the forensic-reckoning **นับ**. This is the only place in Genesis where חָשַׁב carries narrative-providence weight rather than forensic-imputation weight — the contextual split is principled.

**STABLE** ✓ — Joseph's closing-providence frame is the OT's cleanest articulation of compatibilist-providence. The Thai rendering preserves the vocabulary distinction between *human plotting* (`คิดร้าย`) and *divine planning* (`ทรงคิดให้กลายเป็น`) — the chiasm carries.

---

## 15. Inherited corpus locks — **all compliant except chesed (§2) + nicham subtype (§18)**

| Doc | GEN evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | See §1 above | **LOCKED** |
| `ot_register_policy_2026-05.md` | Divine-speech ทรง- + เรา/เจ้า throughout the book; Pharaoh + foreign kings (Abimelech, Hittites at Machpelah negotiation Gen 23) take dignified ทรง- per §2.2; pagan-prayer-vocabulary at Gen 31:30 (Laban's Teraphim) takes plain register; humans-to-divine takes humble ข้าพระองค์ throughout. **EXCEPTION: Joseph receives ทรง- in 4 verses (44:1, 45:1, 50:1, 50:2) — see §19.** | **DRIFT-Joseph (REVIEW)** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains throughout the toledot frame; וַיְהִי opener at 1:3, 4:8, 11:1, 12:10, 14:1, 22:1 (etc.) preserved as narrative-frame markers; cognate-accusative compressions at 27:33 (חָרַד חֲרָדָה גְדֹלָה "trembled a great trembling") + 29:11 (וַיִּשָּׂא קֹלוֹ וַיֵּבְךְּ "lifted his voice and wept") + 49:9 (גּוּר אַרְיֵה "lion-cub") handled per doc. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "presence/face-of-YHWH" (Gen 4:14, 16; 27:7; 32:30 Peniel) → **เบื้องพระพักตร์** / **พระพักตร์**; "yad-of-YHWH" (Gen 19:16 angelic hand-grasp) → **พระหัตถ์**; anthropomorphic divine-actions (3:8 walking-in-the-garden; 11:5 came-down-to-see; 18:21 will-go-down-and-see) → ทรง- on action verbs. Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | Genesis has no major MT-vs-English versification divergences (all 50 chapters align across MT/LXX/SP/English). One passage (Gen 32:1–32 → English 31:55–32:32 in some Bibles) is handled at the chapter-boundary by following the MT divisions; chapter-boundary split-verses are minor. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | All 200+ proper-noun renderings spot-checked against THSV baseline; name-changes (17:5, 17:15, 32:28) explicitly tracked; place-names (Eden, Babel, Ur, Haran, Shechem, Bethel, Hebron, Mamre, Sodom-Gomorrah, Zoar, Beersheba, Padan-Aram, Gerar, Goshen, etc.) all per-table. | **LOCKED** |
| `proper_noun_wordplay_2026-05.md` | See §3, §4 above. 30+ wordplay-name etymologies documented across Genesis. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | See §2 above — **5-verse drift**. | **DRIFT (DECIDE)** |
| `exod_34_attribute_formula_2026-05.md` | N/A in Genesis (Exod 34 not yet shipped); but `רַחוּם` / `חַנּוּן` precursor vocabulary is absent in Genesis. The Sinai-formula's chesed-component is the cross-corpus thread chesed-doc covers. | **LOCKED (N/A)** |
| `nicham_divine_relenting_2026-05.md` | Gen 6:6–7 (וַיִּנָּחֶם יהוה) "YHWH was sorry he had made man" — Eremos renders **เสียพระทัย** (be-sorrowful) rather than the JON-3:9–4:2 lock **ทรงเปลี่ยนพระทัย**. **The split is principled** (Gen 6:6 is divine-grief over creation-state, reflexive-emotional sense; not divine-relenting-from-judgment, factive-volitional sense as in Jonah). The doc's principle holds, but the doc itself does not currently distinguish the two senses — recommend amendment. See §18. | **LOCKED-with-Genesis-6-sub-rule (REVIEW)** |
| `manah_divine_appointment_2026-05.md` | The verb מָנָה does not appear in Genesis with God-as-subject (Genesis uses the cognate verb עָשָׂה or the יְהוָה־יִרְאֶה place-name compound for divine-provision). N/A. | **LOCKED (N/A)** |
| `leitwort_handling_policy_2026-05.md` | Genesis exercises this policy at: (a) the שֶׁבַע / שָׁבוּעַ Beersheba dual-wordplay (21:31 + 26:33) — leitmotiv preserved; (b) the יָרַד "go down" / עָלָה "go up" Joseph-narrative trajectory (Joseph "down" to Egypt 39:1; Israel "up" out of Egypt 50:25 prefigured) — preserved; (c) the recurrent עֶזְרָה / עֵזֶר "help" word-family (2:18 helper; 49:25 the Father's help) — preserved; (d) the כָּסַף "covet/silver" wordplay at 31:30 (Laban) + 37:28 (Joseph sold for 20 of-silver) + 42:25 / 43:15 (returned-silver) + 44:2 (silver-cup planted) — partially preserved as `เงิน` (silver). | **LOCKED** |
| `divine_names_table_2026-05.md` (place-name compounds) | יהוה־יִרְאֶה at 22:14 → **ยาห์เวห์ยีเรห์** + parenthetical gloss; אֵל רֳאִי at 16:13 → **เอลโรอี** + parenthetical gloss. Compliant per table §"place-name compounds." | **LOCKED** |
| `pagan_deities_2026-04.md` (NT-corpus, OT-extension) | Laban's teraphim (Gen 31:19, 31:34, 31:35) → **เทราฟิม** transliterated with descriptive-frame ("รูปเคารพ" household-idols). Foreign-religion vocabulary distinguished from יהוה-vocabulary throughout. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator royal-Thai for divine acts; speaker-register distinguishes patriarchal-elder voice (royal ทรง-) from younger-character voice (plain); foreign-king speech (Pharaoh, Abimelech) gets dignified ทรง-. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | Genesis has limited praise-vocabulary; Gen 14:20's "Blessed be God Most High" → **สาธุการแด่พระเจ้าผู้สูงสุด**; Gen 24:48's Eliezer-bowing-and-praising → **ก้มกราบและสรรเสริญ**. Compliant per the doc's altar-vocabulary pattern. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative tense is wayyiqtol; Greek-NT-specific. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | NT-inclusion-variants policy. The OT-side (Gen 4:8 / 46:27 / 47:31 — see §6) is currently handled per-verse without a corresponding doc. | **LOCKED-pending-OT-companion-doc** |

---

## 16. Hebrew-source word-spacing absent in Gen 26–50 — **DECIDE before tagging (data-integrity)**

**The finding:** Of 1,533 Genesis verses across 50 chapters, **766 verses (50% of the book) have the `hebrew` source field stored as a continuous run-on string with cantillation marks intact but word-spaces stripped.** The split is sharp and chapter-aligned:

| Chapter range | Verses with-spaces | Verses without-spaces | Status |
|---|---:|---:|---|
| GEN 01–25 | 767 | 0 | ✓ correctly spaced |
| GEN 26–50 | 1 | 766 | ✗ word-spaces stripped |

(Chapters 26–50 each have 0–14 with-spaces verses scattered through, but the dominant pattern is no-space.)

**Example — GEN 26:1:**
- **Correct (Gen 25:1 style):** `וַיֹּ֧סֶף אַבְרָהָ֛ם וַיִּקַּ֥ח אִשָּׁ֖ה`
- **Stripped (Gen 26:1 style):** `וַיְהִ֤ירָעָב֙בָּאָ֔רֶץמִלְּבַד֙הָרָעָ֣ב`

The MACULA Hebrew source has correct word-spacing for all 50 Genesis chapters; this drift is in the verse-extraction step somewhere between MACULA and `output/translations/genesis_NN.json`. The chapter-26-onward pattern strongly suggests a regression in `scripts/extract_book_hebrew.py` (or whichever extraction script handles Genesis) that affected an extraction-batch covering chs.26–50.

**Why the existing checks did not catch this:** `scripts/check_hebrew_field_integrity.py` enforces three rules: (A) HARD FAIL on Thai-character leakage in `hebrew` field; (B) HARD FAIL on `key_decisions[].hebrew` containing fabricated tokens; (C) WARN on ASCII-only meta-labels in `key_decisions[].hebrew`. **Whitespace-integrity is not in the rule-set.** The extraction quality regression was therefore invisible to ship-time checks.

**Reader-edition impact:** Any consumer that displays the `hebrew` field directly (the Eremos reader-edition Hebrew-pane; future scholarly export to USFM with parallel Hebrew; reverse-lookup tools) will show chapters 26–50 as continuous Hebrew character-strings — illegible in their current form for parallel-reading. **The Thai translation surface is not affected** (the `thai`, `thai_literal`, `thai_summary`, `key_decisions`, `notes` fields in chapters 26–50 are correctly populated, with the separate `thai_literal` issue noted in §17).

**DECIDE before tagging:** Two resolution paths:

(a) **Re-extract chapters 26–50** from MACULA Hebrew with a corrected extraction script. The verse-text content is identical (just whitespace); a clean re-extraction + diff-only-the-spaces commit + re-running per-chapter checks restores the data integrity without touching any translation content. Recommend this path. Estimated effort: 1 ship-cycle (extraction-script audit + 25-chapter mechanical re-extraction + check re-run).

(b) **Defer to post-tag follow-up** if the reader-edition Hebrew-pane is not yet rendering for OT books. Would mean tagging `book-genesis-v1` with a known data-integrity asterisk on chapters 26–50 + opening a tracking issue.

**→ Recommend extending `scripts/check_hebrew_field_integrity.py`** to add a HARD FAIL on `hebrew` field that contains zero word-space characters (` ` U+0020) over a length threshold (e.g., 30+ characters of Hebrew). This is the structural fix that prevents future books from shipping with the same regression.

**→ Recommend (a) + check-extension.** The data-integrity restoration is mechanical (extraction-script audit), and the ship-time check extension prevents recurrence — both are clean wins. **MEDIUM severity** (does not affect Thai translation surface; does affect reader-edition Hebrew-display).

---

## 17. `thai_literal` field is in ENGLISH for all of GEN 44–50 — **DECIDE before tagging (data-integrity)**

**The finding:** Of 1,533 Genesis verses, **198 verses across the last 7 chapters (44, 45, 46, 47, 48, 49, 50) have the `thai_literal` field populated with English-language literal-translations rather than Thai.** The main `thai` field is correctly Thai across all 50 chapters; only the literal-transparency layer drifted in chapters 44–50.

| Chapter | Verses with English `thai_literal` |
|---|---:|
| GEN 44 | 34/34 (100%) |
| GEN 45 | 28/28 (100%) |
| GEN 46 | 34/34 (100%) |
| GEN 47 | 31/31 (100%) |
| GEN 48 | 22/22 (100%) |
| GEN 49 | 33/33 (100%) |
| GEN 50 | 26/26 (100%) |
| **Total** | **198 verses (12.9% of Genesis)** |

**Example — GEN 49:1:**
- `thai`: `ยาโคบเรียกบุตรชายของท่านและตรัสว่า "จงมารวมกัน เราจะบอกพวกเจ้าถึงสิ่งที่จะเกิดแก่พวกเจ้าในวันสุดท้าย`
- `thai_literal`: `And Jacob called to his sons, and he said, 'Gather yourselves and I will tell you what shall meet you in the last of the days.`

The `thai_literal` field's purpose (per `RULES.md` §6) is the **literal Thai alternative** to the natural `thai` rendering — a word-by-word transparency layer for scholarly reviewers. Populating it with English defeats the purpose for Thai-speaking reviewers and breaks the project's two-tier (literal + natural) Thai-only convention.

**Why this affects only chapters 44–50:** These chapters constitute the entire Joseph-denouement / Jacob's-blessings / Joseph's-death narrative — likely a single drafting batch where the thai_literal-generation step regressed. Chapters 1–43 have Thai-language `thai_literal` correctly. The drift is chapter-aligned and 100%-of-batch, suggesting a script-side regression rather than per-verse drafting drift.

**Reader-edition impact:** The Eremos reader-edition's literal-tier display for chapters 44–50 will show English text — unusable for the intended Thai-reviewer audience. **The main `thai` Thai translation is unaffected** and reads naturally for all 50 chapters.

**DECIDE before tagging:** Two resolution paths:

(a) **Retroactively re-render the 198 affected `thai_literal` fields in Thai.** Surgical edit of 7 chapter JSON files; the `thai_literal` text is intentionally close to the source-Hebrew-syntax so the re-render is a translate-from-English-back-to-Thai-literal pass. Estimated effort: 1–2 hours of Thai re-rendering. Could be batched in a single PR. Recommend this path.

(b) **Defer to post-tag follow-up** if the reader-edition literal-pane is not yet rendering for OT books in production. Would mean tagging `book-genesis-v1` with a known `thai_literal` gap on the last 7 chapters + opening a tracking issue.

**→ Recommend extending `scripts/check_back_translation.py` or adding a sibling check** that flags `thai_literal` fields containing >50% ASCII letters (U+0041–U+007A) as a HARD FAIL. The convention is that `thai_literal` is **always Thai** (with optional Hebrew transliteration in parens for hapax-words), never English.

**→ Recommend (a) + check-extension.** Lower-effort than §16's Hebrew-source restoration; could be combined into a single ship-cycle PR.

---

## 18. נָחַם at Gen 6:6–7: divine-grief vs. divine-relenting subtype split — **REVIEW (recommend doc amendment)**

Genesis 6:6–7 has the OT's first occurrence of the verb נָחַם (Niph'al) with God as subject:

- **Gen 6:6:** וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם בָּאָרֶץ ("YHWH was sorry he had made man on the earth")
- **Gen 6:7:** ...כִּי נִחַמְתִּי כִּי עֲשִׂיתִם ("for I am sorry that I have made them")

Eremos renders both as **ทรงเสียพระทัย** ("be-sorrowful in royal-Thai") — distinct from the lock at `nicham_divine_relenting_2026-05.md` which establishes **ทรงเปลี่ยนพระทัย** ("change [royal] mind") as the corpus-rendering for divine-נָחַם.

**Editorial assessment:** The split is **principled and correct** — the Hebrew lemma carries two distinct senses:

| Sense | Hebrew context | Thai rendering | Locked precedent |
|---|---|---|---|
| **Divine-grief** (reflexive-emotional, internal sorrow) | Gen 6:6–7: God grieves over what creation has become | **ทรงเสียพระทัย** | Gen 6:6 (this verse) |
| **Divine-relenting** (factive-volitional, change of intended action) | Jonah 3:9, 3:10, 4:2: God relents from announced judgment | **ทรงเปลี่ยนพระทัย** | Jon 3:10 (`nicham_divine_relenting_2026-05.md`) |

The two senses are well-attested in BDB / HALOT and align with the contextual distinction (Gen 6:6 has no announced-decision-being-reversed; Jon 3:10 explicitly does). The lemma's polysemy is the cleanest exegetical case in the OT for the Niph'al's two senses.

**The doc gap:** `nicham_divine_relenting_2026-05.md` v0.1 (decided 2026-05-09) locks **ทรงเปลี่ยนพระทัย** as the corpus-default without distinguishing the divine-grief sub-sense. Gen 6:6–7 is the OT's locking precedent for the divine-grief sub-rendering. The doc should be amended:

| Sub-sense | Hebrew tell | Thai lock | Locking precedent |
|---|---|---|---|
| Reflexive-emotional (divine-grief, no-decision-reversal) | context: lament over creation/people-state | **ทรงเสียพระทัย** | **Gen 6:6** (corpus-locking precedent) |
| Factive-volitional (divine-relenting, decision-reversal-from-announced-judgment) | context: explicit prior-announcement-of-judgment + the relenting | **ทรงเปลี่ยนพระทัย** | Jon 3:10 (locked) |

Other OT divine-נָחַם verses (Ex 32:14, 1 Sam 15:11+35, Ps 106:45, Jer 18:8+10, etc.) need to be classified by sub-sense at first occurrence. The Num 23:19 + 1 Sam 15:29 counter-formulae (לֹא יִנָּחֵם "[God] does not change his mind") apply to the **factive-volitional** sub-sense; the divine-grief sub-sense is not contradicted by them.

**REVIEW flag:** Confirm Ben endorses the Gen 6:6 **ทรงเสียพระทัย** rendering AND the doc-amendment splitting the lemma into two sub-senses. Recommended amendment to `nicham_divine_relenting_2026-05.md` (single new section in the existing doc; not a new doc).

---

## 19. Joseph receives Rachasap (ทรง-) honorific in 4 verses — **REVIEW (Rachasap policy clarification)**

The honorifics-binding check (`scripts/check_honorifics_binding.py`) flags 3 warnings in GEN 50 + 1 in GEN 44 + 1 in GEN 45 where **Joseph is the grammatical subject of a verb prefixed with ทรง-** (the royal-Thai prefix reserved per `ot_register_policy_2026-05.md` §2.2 for divine subjects, foreign emperors, and Hebrew kings — explicitly NOT for patriarchs):

| Verse | Thai (current) |
|---|---|
| GEN 44:1 | โยเซฟ**ทรงสั่ง**คนต้นเรือนของพระองค์ว่า ("Joseph commanded the steward of his house") |
| GEN 45:1 | โยเซฟ**ทรงเปิดเผยพระองค์**ต่อพี่น้องของพระองค์ ("Joseph revealed himself to his brothers") |
| GEN 50:1 | โยเซฟ**ทรงโผลง**บนหน้าของบิดา **ทรงร้องไห้**บนท่าน และจูบท่าน ("Joseph fell on his father's face, wept on him, and kissed him") |
| GEN 50:2 | โยเซฟ**ทรงสั่ง**ผู้รับใช้ของพระองค์ คือหมอ ให้รักษาศพบิดาของพระองค์ ("Joseph commanded his servants the physicians to embalm his father") |
| GEN 50:24 | (the `ทรงสาบานไว้กับเอบราฮัม...` is YHWH-subject, not Joseph; check flag is a false positive at 50:24) |

**Editorial assessment:** This is a **register-policy ambiguity**. Per `ot_register_policy_2026-05.md` §2.2:
- **Patriarchs (Abraham, Isaac, Jacob, Joseph)** — *plain narrator* (treat as venerated-elders, not kings); Rachasap **inappropriate** for tribal-patriarch role.
- **Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, ...)** — Rachasap (ทรง) — they are imperial sovereigns of their narratives.
- **Foreign vassal-rulers, governors** — Plain.

Joseph in chapters 44–50 is **vizier of Egypt under Pharaoh** (per Gen 41:40–44 his investiture as second-only-to-Pharaoh). The doc explicitly classifies him as a **patriarch** (plain register) but also has a "vassal-ruler" category (also plain). Either way, the doc says plain. The current ทรง- treatment in the 4 verses is therefore **a Rachasap-policy violation** at the surface.

**Why this drift may have happened:** The Joseph-vizier role at Pharaoh's court occupies the highest non-royal Egyptian office; the narrator's careful dignification of Joseph's actions (commanding, revealing-himself, weeping) may have triggered an instinctive Rachasap-elevation. But the doc is unambiguous: patriarchs do not receive ทรง- regardless of office held.

**REVIEW flag:** Confirm Ben endorses one of three resolution paths:
- (a) **Strict policy compliance** — strip ทรง- from the 4 verses; render `โยเซฟสั่ง...`, `โยเซฟเปิดเผยตัว...`, `โยเซฟโผลง...`, `โยเซฟสั่ง...`. Matches the doc's current letter.
- (b) **Joseph-as-vizier policy amendment** — add a sub-rule to `ot_register_policy_2026-05.md` §2.2 that distinguishes patriarchal-narrative-Joseph (chs.37–41 + 50 personal contexts → plain) from vizier-of-Egypt-narrative-Joseph (chs.41:40+ public-office contexts → Rachasap). The 4 affected verses are a mix: 44:1 + 45:1 + 50:2 are public-office actions; 50:1 is personal grief at father's death. Under (b), 50:1 would shift back to plain; 44:1 + 45:1 + 50:2 stay ทรง-.
- (c) **Defer to Thai-language-reviewer voice** — Joseph's register may be one of the cases where the Thai-natural reading benefits from a slight elevation that doesn't cleanly match the doc's binary patriarch-vs-emperor split.

**Recommend (b) — a doc amendment that captures the Joseph-vizier-public-office distinction**, with the 4 verses surveyed as the locking-precedent corpus. The amendment should also clarify the Daniel parallel (Daniel-as-Babylonian/Persian-vizier in the courts of Nebuchadnezzar / Belshazzar / Darius — same role, similar narrative).

---

## 20. Toledoth formula minor drift — **STABLE**

The אֵלֶּה תוֹלְדוֹת ("these are the generations of") formula structurally divides Genesis into 11 sections. Eremos renders it consistently as **"นี่คือเรื่องราว..."** at 9 of 11 occurrences, with two minor variations:

| Verse | Thai opener | Notes |
|---|---|---|
| 2:4 | นี่คือเรื่องราวของฟ้าสวรรค์... | Locked rendering |
| 5:1 | นี่คือหนังสือเรื่องราวของวงศ์อาดัม | Adds "หนังสือ" — matches Hebrew סֵפֶר תּוֹלְדוֹת ("book of generations"); justified |
| 6:9 | นี่คือเรื่องราวของโนอาห์ | Locked rendering |
| 10:1 | นี่คือเรื่องราววงศ์ของบุตรชาย... | Adds "วงศ์" — small drift |
| 10:32 | เหล่านี้คือตระกูลของลูกหลาน... | Closing-formula variant; uses "ตระกูล" not "เรื่องราว" |
| 11:10 | นี่คือเรื่องราววงศ์ของเชม | Adds "วงศ์" — small drift |
| 11:27 | นี่คือเรื่องราววงศ์ของเทราห์ | Adds "วงศ์" — small drift |
| **25:12** | **นี่เป็นเรื่องราวเชื้อสายของอิชมาเอล** | **DRIFT**: uses `เป็น` not `คือ` + adds `เชื้อสาย` |
| **25:19** | **นี่เป็นเรื่องราวเชื้อสายของอิสอัค** | **DRIFT**: same |
| 36:1 | นี่คือเรื่องราวของเอซาว (คือเอโดม) | Locked |
| 36:9 | นี่คือเรื่องราวของเอซาว บิดาของชาวเอโดม | Locked |
| 37:2 | นี่คือเรื่องราวของยาโคบ | Locked |

The 25:12 + 25:19 pair is a small drift (two ad-jacent verses; possibly drafted in one pass with the same chosen variant). The cross-formula thread is mostly intact — readers tracking the toledoth-frame will recognize all 11 occurrences as variants of the same formula. **STABLE** ✓ — no surgical action required, but the 25:12 + 25:19 pair could be normalized to `นี่คือเรื่องราว...` if a future polish-pass touches Gen 25.

---

## Mechanical (§1) — **all green**

- 50/50 chapters: `output/check_reports/genesis_NN_review.md` + sub-reports ✓
- 50/50 chapters: `output/back_translations/genesis_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 184-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (8 phrase-consistency rules audited 7,943 verses)
- `git status output/`: only `output/check_reports/divine_names.md` modified (re-run by audit-time `key_term_consistency.py` invocation; reflects the YHWH-counter run-state — diff is harmless count-update). No source-file dirt.
- 49/50 chapters: `output/textual_variants/genesis_NN.json` present (Gen 1 has no Tetragrammaton; the missing file is per-design but the convention from Ruth/Jonah was to write a `no_yhwh_in_chapter` placeholder — recommend writing one for Gen 1 for shape-consistency).
- **Hebrew word-spacing is missing in 766 of 1,533 verses (chapters 26–50) — see §16. This is not currently caught by any check.**
- **`thai_literal` is in ENGLISH for 198 verses (chapters 44–50) — see §17. This is not currently caught by any check.**

---

## Pre-existing docs affirmed / unchanged

All 66 docs in `docs/translator_decisions/` reviewed. Compliance per §15 above. The Jonah audit's recommendations landed (chesed-doc + Exod-34-formula doc + nicham-doc + manah-doc + leitwort-doc — all live in `0344376`). Genesis exercises three of those five (chesed, nicham, leitwort); the other two (Exod-34-formula, manah) are exercised in the next-priority OT books.

The post-Ruth-and-Jonah recommendations still NOT yet written:
- `divine_anthropomorphism_thai_grammar_2026-05.md` — implicit Ruth-1:13 rule + Jonah `נִחַם` validation; **Genesis validates it a third time** (Gen 6:6 grief-anthropomorphism; 11:5 came-down-to-see; 18:20–21 went-down-to-see; 1:2 hovering-Spirit).
- `goel_kinsman_redeemer_2026-05.md` — N/A in Genesis but still urgent before Job 19 / Isa 41–43.
- `hebrew_oath_formulas_2026-05.md` — Genesis exercises this **extensively** (Gen 14:22–23 "raised-hand oath"; 21:23–32 Beersheba oath; 22:16 "by myself I have sworn"; 24:2–9 "place hand under thigh" oath; 26:28–31; 31:44–53 Mizpah-cairn oath; 47:29–31; 50:5–6, 50:25). Recommend lifting NOW as a Genesis-locking-precedent doc, before 1 Sam 14, 2 Sam 21, etc.
- `paqad_visit_attend_2026-05.md` — Gen 21:1 (וַיהוָה פָּקַד אֶת־שָׂרָה "YHWH visited Sarah") + 50:24–25 ("God will surely visit you" Joseph's last words). **Genesis is the locking-precedent for the doc** — write before Exodus 3:16 + 4:31 + 13:19 + 1 Sam 2:21.

---

## Flagged for Ben's attention

### A. Chesed cross-corpus drift across 5 GEN verses — **DECIDE before tagging** (§2)
Retroactively normalize 19:19, 21:23, 32:11, 39:21, 40:14 to **ความรักมั่นคง** per `chesed_covenant_love_2026-05.md`. Critical before Exodus 34 + Pss/Joel/Nah/Neh ship.

### B. Gen 3:16 תְּשׁוּקָה reading — **DECIDE before tagging** (§8)
Confirm whether to (a) preserve polysemy + add Layer-2 footer naming the 4:7 parallel, (b) lift the controlling-reading into the surface, or (c) inline-parenthetical the 4:7 cross-reference. High-visibility verse for modern Thai-evangelical gender discourse + theological reviewers.

### C. Gen 3:15 ผู้นั้น singular protoevangelium reading — **REVIEW** (§7)
Confirm Ben endorses the Christological-individual reading vs. the more-neutral **เขา** singular-or-corporate. If endorsed, recommend Layer-2 footer documenting the editorial choice + LXX αὐτός / Vulgate ipse / Rom 16:20 NT trajectory.

### D. Gen 6:1–4 בְּנֵי הָאֱלֹהִים — **REVIEW** (§9)
Confirm polysemy-preserving rendering; recommend adding `interpretive_crux_footnote` Layer-2 entry to `output/textual_variants/genesis_06.json` naming the three readings + Job 1:6 / 38:7 + 2 Pet 2:4 / Jude 6 NT trajectory. Confirm Nephilim transliteration for Num 13:33 cross-reference.

### E. Gen 49:10 שִׁילֹה — **REVIEW** (§10)
Confirm Ben endorses the **ชีโลห์** transliteration vs. messianic-paraphrase. The 49:10 verse is the OT's most-disputed messianic verse; the project's current stance forecloses messianic-recognition for typical readers. Recommend either (a) confirm + Layer-2 elevation, or (b) inline messianic paraphrase.

### F. Hebrew-source word-spacing absent in GEN 26–50 (766 verses) — **DECIDE before tagging** (§16)
Re-extract the 25 affected chapters from MACULA Hebrew with a corrected extraction script + extend `check_hebrew_field_integrity.py` to add a HARD FAIL on missing-word-spaces. Mechanical fix; data integrity restoration only — does not affect the Thai translation surface.

### G. `thai_literal` is ENGLISH for GEN 44–50 (198 verses) — **DECIDE before tagging** (§17)
Retroactively re-render the 198 affected `thai_literal` fields in Thai + extend `check_back_translation.py` (or sibling) to add a HARD FAIL on `thai_literal` containing >50% ASCII letters. Lower-effort than §16.

### H. Joseph receives Rachasap (ทรง-) in 4 verses — **REVIEW** (§19)
Confirm one of three resolution paths: (a) strict policy compliance (strip ทรง- from 44:1, 45:1, 50:1, 50:2); (b) Joseph-as-vizier policy amendment to `ot_register_policy_2026-05.md` (recommend); or (c) defer to Thai-language-reviewer.

### I. Gen 6:6–7 nicham divine-grief sub-rendering — **REVIEW** (§18)
Confirm Ben endorses the `ทรงเสียพระทัย` rendering at 6:6 + 6:7 + the doc amendment splitting `nicham_divine_relenting_2026-05.md` into two sub-senses (divine-grief / divine-relenting). The Gen 6:6 precedent locks the divine-grief sub-rendering for the corpus.

### J. New corpus docs to write (before Exodus / Samuel ship)
1. **`docs/translator_decisions/mt_vs_lxx_textual_variant_handling_2026-05.md`** (§6) — locks the three Genesis precedents (4:8 inline-bracket; 46:27 + 47:31 footer-only). **CRITICAL** before Joshua / Samuel / Jeremiah / Esther / Ezra-Nehemiah ship.
2. **`docs/translator_decisions/hebrew_oath_formulas_2026-05.md`** (carry-forward from Ruth audit; Genesis is the locking-precedent — see §15) — locks the four oath-formulae exercised in Genesis (raised-hand 14:22; place-hand-under-thigh 24:2; "by myself I have sworn" 22:16; cairn-oath 31:44–53). **CRITICAL** before 1 Sam 14 + 2 Sam 21 ship.
3. **`docs/translator_decisions/paqad_visit_attend_2026-05.md`** (carry-forward from Ruth audit; Gen 21:1 + 50:24–25 are the locking-precedents) — **CRITICAL** before Exodus 3:16 ships.
4. **`docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md`** (carry-forward from Ruth audit; Genesis validates Ruth-1:13 + Jonah-נִחַם a third time) — write before Exodus 7 (plagues) + Pss-corpus body-part-of-YHWH cluster.
5. **(Optional)** `docs/translator_decisions/protoevangelium_messianic_reading_register_2026-05.md` (§7 + §10) — meta-doc for translator-discipline; names the Gen 3:15 ผู้นั้น + Gen 49:10 ชีโลห์ pair as the corpus's editorial stance on messianic-reading-visibility. Cross-reference with Isa 7:14 + 9:6 + 53 (forward); Pss 2 + 110 (forward); Mt 1:23 + Jn 19:36–37 + Heb 7:14 (NT-side).

### K. Existing docs to amend
- **`spiritual_beings_hierarchy_2026-05.md`** — add Gen 6:1–4 sub-entry (with the three-reading question + Job 1:6 / 38:7 parallel). The doc currently exists for the Daniel / Apocalyptic side; Genesis 6 needs a forward-anchor.
- **`nicham_divine_relenting_2026-05.md`** — add Gen 6:6 grief-anthropomorphism sub-rule (distinct from the JON-3:9–4:2 factive-relenting sense): Hebrew נִחַם reflexive-emotional → **เสียพระทัย**; factive-volitional → **ทรงเปลี่ยนพระทัย**. The split is the cleanest exegetical proof of the lemma's polysemy. See §18.
- **`leitwort_handling_policy_2026-05.md`** — add Genesis-locking-precedents sub-section listing the four major leitwort-cases handled (Beersheba dual-wordplay; Joseph ירד / עלה; עזר help-family; כסף silver-recursion).
- **`ot_register_policy_2026-05.md`** — add Joseph-as-vizier-of-Egypt sub-rule (per §19) clarifying public-office vs personal-narrative register split.

### L. External AI review (§3 of checklist) — **pending**
Recommended before `book-genesis-v1` tag. Suggested **5-cluster external AI packet** (Genesis is too large for one packet; chunk by major narrative-block):

1. **Gen 1–11 Primeval History** — creation cosmogony + 1:26–27 image-of-God + 3:15 protoevangelium + 3:16 desire + 4:8 LXX-addition + 6:1–4 sons-of-God + 6:6–7 divine-grief + 9:6 image-of-God + 11:9 Babel counter-etymology + the toledot-frame versification.
2. **Gen 12–25 Abraham cycle** — 12:3 blessing-formula + 14:18–22 Melchizedek + 15:6 faith-righteousness + 16:13 El Roi + 17:1 El Shaddai + 17:5 Abram-renaming + 21:33 El Olam + 22:2 Akedah μονογενής + 22:14 YHWH-Yireh + 24 chesed-cluster.
3. **Gen 26–36 Jacob cycle** — 25:23 two-nations-oracle + Beersheba dual-wordplay (26:33) + Bethel (28:19) + Mahanaim (32:2) + Peniel (32:30) + Israel-renaming (32:28+35:10) + the 12-sons name-etymologies (29:32–30:24, 35:18) + chesed at 32:11 (drift) + tribal-violence at Gen 34.
4. **Gen 37–45 Joseph descent + reunion** — 37 Joseph-sold + 38 Tamar interlude + 39 Potiphar's wife + 41:51–52 Manasseh / Ephraim wordplay + 39:21 + 40:14 chesed (drift) + the providence-arc setup.
5. **Gen 46–50 Joseph in Egypt + closure** — 46:27 70-vs-75 LXX-variant + 47:31 head-of-bed-vs-staff LXX-variant + 47:29 chesed compliant + 48:14 cross-handed blessing + 49:10 שִׁילֹה + 49:24–25 the divine-titles cluster (אֲבִיר יַעֲקֹב + רֹעֶה + אֵל שַׁדַּי) + 50:20 providence-capstone.

Use Grok + ChatGPT + Gemini in parallel per the prior pattern. Genesis-1 + Genesis-3 + Genesis-22 + Genesis-49 are the highest-yield clusters.

---

## Recommendation

**Genesis ships in strong corpus-hygiene shape on the translation surface — and exercises the W1 OT-extension lock-set + the post-Ruth + post-Jonah corpus-doc additions at unprecedented scale (50 chapters / 1,533 verses).** But two **data-integrity issues** affect 25–50% of the book at the source / literal-layer level (NOT the main Thai translation), and the chesed lock acquired post-Genesis-drafting requires retroactive normalization. Five structural improvements to lock in before Exodus / Samuel ship:

1. **Resolve the GEN chesed drift** (§A) — 5 surgical edits at 19:19 / 21:23 / 32:11 / 39:21 / 40:14 to align with the (Ben-decided 2026-05-09) `chesed_covenant_love_2026-05.md` lock.
2. **Re-extract the Hebrew source for chs.26–50** (§F) — restore word-spacing data integrity for half the book. Mechanical fix.
3. **Re-render `thai_literal` for chs.44–50** (§G) — restore the Thai literal-layer for 198 verses currently in English. Lower-effort.
4. **Resolve the Gen 3:16 תְּשׁוּקָה reading** (§B) — high-visibility for theological-reviewer + modern-evangelical-reader expectation.
5. **Write the four pending OT-corpus docs** (§J1–J4 — MT-vs-LXX-textual-variant-handling, hebrew-oath-formulas, paqad, divine-anthropomorphism — all locking-precedents within Genesis).

Tag `book-genesis-v1` after:
1. Ben's decisions on **§A + §B + §F + §G** (DECIDE items: chesed drift; Gen 3:16 desire reading; Hebrew word-spacing; English thai_literal)
2. Ben's confirmations on **§C + §D + §E + §H + §I** (REVIEW items: 3:15 protoevangelium; 6:1–4 בני האלהים; 49:10 Shiloh; Joseph Rachasap; Gen 6:6 nicham subtype)
3. Four new translator_decisions docs written (§J1–J4 — J5 protoevangelium-meta-doc may be deferred or written in parallel)
4. Four existing docs amended (§K — spiritual_beings_hierarchy, nicham, leitwort, ot_register_policy)
5. External AI sanity-check (§L) across the 5 packet-clusters
6. Two ship-time check extensions: `check_hebrew_field_integrity.py` for whitespace HARD FAIL; sibling check for ASCII-in-thai_literal HARD FAIL
7. Optional: write a `no_yhwh_in_chapter` placeholder for `output/textual_variants/genesis_01.json` to match Ruth/Jonah convention

Genesis is the **first OT book of substantial length to ship** — its successful completion validates the entire OT-pilot lock-set + workflow at scale. The remaining OT-corpus docs (oath-formulas, paqad, anthropomorphism, MT-vs-LXX-variant-handling) are now urgent because they have Genesis-locking-precedents that need to compound forward without drift, exactly the pattern the chesed Ruth→Jonah→Genesis arc has just demonstrated. The two data-integrity findings (§F + §G) are the first time the audit-process has surfaced source-file drift that ship-time checks did not catch — the recommended check extensions (§F + §G) close those gaps for future books.
