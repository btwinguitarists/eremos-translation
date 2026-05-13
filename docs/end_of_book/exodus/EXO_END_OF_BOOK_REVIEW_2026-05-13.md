# Exodus — End-of-Book Review

**Date:** 2026-05-13
**Scope:** All 40 chapters of Exodus (~1,213 verses); `glossary.json`; existing `docs/translator_decisions/` (74 docs incl. the Genesis-audit doc additions and the Sinai-formula doc `exod_34_attribute_formula_2026-05.md` for which **Exodus 34 is the canonical locking-precedent**).
**Trigger:** EXO 40 shipped (commit `c6e5839`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Fourth OT book in the corpus** (after Ruth, Jonah, Genesis) and the **second Pentateuch book** — the first to recite the Sinai theophany its canonical doc was built around.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **20 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 40/40 chapters have green per-chapter reports + back-translations + textual_variants files (where chapter contains YHWH); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-224-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book EXO --strict` returns 0 candidates (NT-style inclusion-variants policy is N/A for Exodus); `git status output/` shows only a harmless re-run of `output/check_reports/divine_names.md` (one C-soft false positive at 40:18 where the script's consonant-pattern match cannot distinguish אֲדֹנָי "Adonai" from אֲדָנָיו "its bases/sockets" — the actual Hebrew at 40:18 is the latter, no divine-name handling required).
- **Exodus is the SECOND-LARGEST OT book yet** in the corpus (40 chapters / ~1,213 verses vs. GEN 50/1,533, JON 4, RUT 4). It exercises every OT-corpus lock landed by 2026-05-12 and is uniquely positioned because **Exod 34:6–7 is the corpus-locking precedent verse for `exod_34_attribute_formula_2026-05.md`** (decided 2026-05-09 after the Jonah audit). The same chapter has yielded the most consequential corpus-level drift in the audit.
- **Data integrity is clean.** No drift in Hebrew word-spacing (the Genesis chs.26–50 regression is absent here); no English-in-`thai_literal` drift (the Genesis chs.44–50 regression is absent here). All 40 chapters have correctly-spaced Hebrew and Thai `thai_literal` fields.
- **18 inherited locks verified compliant** in EXO across the divine-name family, OT-register policy, Hebrew-grammar-transfer, Hebrew-idioms, verse-schema, proper-names, proper-noun-wordplay, chesed-corpus-doc, nicham-corpus-doc, leitwort, manah, paqad, hebrew-oath, divine-anthropomorphism, mt_vs_lxx-textual-variant-handling, divine-object-praise, narrator-vs-character-voice, and historic-present.
- **6 Exodus-distinctive patterns are STABLE-and-locked** at corpus level (the Sinai-narrative `כְּבוֹד יְהוָה` recurrence; the Decalogue prohibition-formula 20:13–17; the Pharaoh heart-hardening triplet across חזק/קשה/כבד; the stiff-necked formula 32:9 + 33:3 + 33:5 + 34:9; the place-name-etymology cluster Marah 15:23 + Massah-Meribah 17:7 + Sinai 19; the Passover/Pesach + matzot transliteration thread).
- **2 items flagged STABLE-but-undocumented** (recommend new corpus docs): the **Tetragrammaton-self-titles family** in Exodus (יְהוָה רֹפְאֶךָ 15:26, יְהוָה נִסִּי 17:15, יְהוָה־קַנָּא 34:14, יְהוָה־צְבָאוֹת absent in EXO, etc. — needs a Tetragrammaton-self-titles sub-doc); and the **Pharaoh-heart-hardening cross-verb policy** (uniform Thai rendering across חזק/קשה/כבד, which is principled but corpus-implicit).
- **5 items flagged REVIEW** (defensible-but-worth-Ben's confirmation): the **חַנּוּן/רַחוּם vocabulary swap at Exod 33:19 + 34:6 vs. the corpus-doc's locked Thai**; the **מַלְאַךְ YHWH multi-rendering** (4+ distinct Thai phrases across 3:2, 14:19, 23:20, 23:23, 32:34, 33:2); the **כַּפֹּרֶת "atonement-cover" within-chapter drift** (พระที่นั่งกรุณา in chs.25/30/37 vs. ที่ลบล้างบาป at 40:20); the **YHWH-Nissi 17:15 paraphrase** vs. divine_names_table's transliteration principle for place-name-compounds (which Genesis followed at יהוה־יִרְאֶה 22:14); the **פָּנִים "face/presence" within-chapter drift** at 33:11/14/15/20/23.
- **3 items flagged DECIDE** (Ben choice needed before tagging `book-exodus-v1`):
  - **Exod 34:6–7 Sinai-formula DRIFT from its own canonical corpus-doc** — the locking-precedent verse does NOT use the doc's locked Thai vocabulary. See §2.
  - **Exod 33:19 חַנֹּתִי + רִחַמְתִּי verbal-form mapping** drifts from the doc's locked nominal-form mapping AND is swapped relative to Exod 34:6 within the same theophanic-cluster. See §3.
  - **Exod 15:11 בָּאֵלִם "among the gods"** rendering `ในหมู่พระทั้งหลาย` — a sensitive theological-register choice (preserves Hebrew polytheistic-mythopoetic surface vs. the Thai-evangelical default of monotheistic-comparative). See §14.
- **External AI review (§3) pending.** Suggested 8-item packet (§2/§3/§14 DECIDE items + §4/§7/§9/§13/§15 REVIEW items).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + Exodus first-occurrence footnote — **LOCKED**

**398 YHWH occurrences across 35 of 40 chapters** (chs.1, 2, 21, 26, 37 have none — by design; ch.1 + ch.2 are pre-burning-bush, ch.21 + ch.26 are casuistic/architectural pericopes, ch.37 is execution-narrative pure). Layer-2 first-occurrence footer present at `output/textual_variants/exodus_03.json` (the burning-bush + Ehyeh-self-disclosure node — locking precedent for the Tetragrammaton convention in the entire OT pilot, since Exod 3 is canonically the name's self-revelation). Footer cross-references the GEN 2:4 first-occurrence (where the OT corpus actually first encounters the Tetragrammaton via Eden's compound), Jn 8:24 ἐγὼ εἰμί NT trajectory, and the Ehyeh→Yahweh etymological link.

All 398 occurrences render as **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md`. The short form **יָהּ** (Yah) appears at 15:2 + 17:16 as part of Song-of-the-Sea + altar-name lyric register; both render as transliterated **ยาห์** per table.

**LOCKED** ✓ — the largest Tetragrammaton-bearing book in the OT pilot so far (398 in EXO vs. 156 in GEN). Total corpus YHWH count after Exodus: ~600+ occurrences across 224 chapters, all uniformly rendered.

---

## 2. Exod 34:6–7 Sinai attribute formula — **DECIDE before tagging (DRIFT from corpus-doc)**

**The most consequential finding of this audit.** The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` was decided 2026-05-09 (Ben + cross-AI review, post-Jonah) and **explicitly names Exod 34:6–7 as the canonical Sinai form** locking the Thai rendering across all ~10 OT recitations. The doc lists the canonical Thai:

```
องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า พระเจ้าผู้ทรงพระเมตตาและทรงพระคุณ ทรงกริ้วช้า
ทรงบริบูรณ์ด้วยความรักมั่นคงและความซื่อสัตย์
ทรงรักษาความรักมั่นคงไว้ถึงพันชั่วอายุ ทรงยกโทษความชั่ว การละเมิด และบาป
แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ — ทรงลงโทษความชั่วของบรรพบุรุษ
ต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน
```

**EXO 34:6–7 as shipped (commit `45938b8`, 2026-05-13):**

> **34:6** องค์พระผู้เป็นเจ้าทรงผ่านต่อหน้าโมเสสและทรงร้องเรียกว่า "องค์พระผู้เป็นเจ้า องค์พระผู้เป็นเจ้า **พระเจ้าผู้เปี่ยมด้วยความกรุณาและความเมตตา ช้าในการพิโรธ บริบูรณ์ด้วยความรักมั่นคงและความจริง**
>
> **34:7** **ทรงรักษาความรักมั่นคงไว้ตลอดพันชั่วอายุ ทรงให้อภัยความผิด การล่วงละเมิด และบาป แต่พระองค์จะไม่ทรงปล่อยให้คนผิดพ้นโทษ พระองค์จะลงโทษความผิดของบิดาต่อบุตรและหลานจนถึงชั่วอายุที่สามและที่สี่"**

**Drifts (six divergences, every component of the doc-locked vocabulary):**

| Hebrew | Doc-locked Thai | EXO 34 actual Thai | Drift? |
|---|---|---|---|
| חַנּוּן | **ทรงพระคุณ** | **ความกรุณา** (Sino-Thai gru-na) | ✗ |
| רַחוּם | **ทรงพระเมตตา** | **ความเมตตา** | ✗ (vocabulary differs; verbal-noun form lost) |
| אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | **ช้าในการพิโรธ** | ✗ (no royal ทรง-; different metaphor — "slow in anger" vs. "slow-to-anger-Rachasap") |
| רַב־חֶסֶד | **ทรงบริบูรณ์ด้วยความรักมั่นคง** | **บริบูรณ์ด้วยความรักมั่นคง** | ✗ (no ทรง-) |
| וֶאֱמֶת | **และความซื่อสัตย์** | **และความจริง** | ✗ (truth vs. faithfulness — major theological divergence on אֱמֶת) |
| נֹשֵׂא עָוֹן | **ทรงยกโทษความชั่ว** | **ทรงให้อภัยความผิด** | ✗ (ยกโทษ "lift away" vs. ให้อภัย "give forgiveness") |
| וְנַקֵּה לֹא יְנַקֶּה | **แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ** | **แต่พระองค์จะไม่ทรงปล่อยให้คนผิดพ้นโทษ** | partial drift |
| פֹּקֵד עֲוֹן אָבוֹת... | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **พระองค์จะลงโทษความผิดของบิดาต่อบุตรและหลาน** | ✗ (no royal ทรง-; "fathers→sons" vs. "ancestors→grandchildren-and-great-grandchildren") |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **จนถึงชั่วอายุที่สามและที่สี่** | partial drift (acceptable variant phrasing) |

**Editorial assessment.** This is the **single most consequential drift in the Exodus audit** because Exodus 34 is the *locking precedent* for the entire `exod_34_attribute_formula_2026-05.md` corpus doc. The doc was decided 2026-05-09 in the wake of Jonah 4:2's audit, and Jonah 4:2 has been retroactively normalized to use the doc's locked Thai. But **Exodus 34 — the doc's namesake — was shipped on 2026-05-13 without the lock applied**. The result is that the canonical Sinai formula and every prophetic / psalmist / post-exilic recitation downstream (Num 14:18, Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Jonah 4:2, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18) will diverge from the canonical recitation when read against the doc's locked Thai. The cross-corpus lemma-thread the doc was created to protect is **broken at the source verse**.

**Why this happened (hypothesis).** The chapter likely was drafted from a parallel reading of THSV / BSB / NIV rather than from the corpus-doc's Thai. The Decalogue parallel at Exod 20:5–6 (chesed-formula in negative-judgment + positive-mercy paired) was correctly rendered with **ความรักมั่นคง** for חֶסֶד — so the chesed sub-lock holds. But the surrounding character-cluster (חַנּוּן רַחוּם אֶרֶךְ אַפַּיִם … וֶאֱמֶת) was rendered freshly rather than from the doc. The doc's "Implementation checklist §3 item 2" explicitly anticipates this case and recommends `check_phrase_consistency.py` extension — that extension has not yet been written.

**DECIDE before tagging — recommend retroactive normalization.** Two paths:

**(a) Strict normalization** — re-render Exod 34:6–7 to match the doc's canonical Thai exactly. The cost is one surgical verse-pair edit + re-running per-chapter checks. The benefit is restoring the cross-corpus lemma-thread before any downstream OT-book ships the formula (Num 14:18 ships with Numbers; Ps 86:15 with Psalms; the formula is liturgically the most-recited Hebrew Bible text). This is the **recommended path**.

**(b) Doc-revision** — accept the EXO 34 surface as the new locking precedent and amend the doc to use the as-shipped vocabulary. Defensible if Ben prefers the as-shipped Thai (ความกรุณา/ความเมตตา rather than ทรงพระคุณ/ทรงพระเมตตา; ความจริง rather than ความซื่อสัตย์; the no-Rachasap surface). The cost is doc-rewrite + retroactive update of Jonah 4:2 (which was normalized to the now-being-revised doc) + a clear paper-trail of the change. NOT recommended — the doc was decided 2026-05-09 with Ben + cross-AI consensus; the doc's Thai was reasoned-through, and re-opening it discards that reasoning.

**Followup:** the doc's Implementation Checklist (§3 item 2 in the doc) calls for `check_phrase_consistency.py` extension to HARD FAIL when 3+ formula-components co-occur but the locked Thai is not present. **Recommend writing this check as part of the §2(a) normalization commit**, so future OT-book ships are auto-protected against this drift.

**Severity: CRITICAL.** This is the corpus-locking verse. If `book-exodus-v1` is tagged without normalization, every downstream formula-recitation will require an asterisk; the OT lock is broken at its source.

---

## 3. Exod 33:19 חַנֹּתִי + רִחַמְתִּי verbal-form mapping — **DECIDE before tagging**

The Exod 33:19 theophanic-promise verse is the structural precursor to 34:6 (the same divine self-revelation, in promise-form before the proclamation-form):

> **33:19 Hebrew:** וְקָרָאתִי בְשֵׁם יְהוָה לְפָנֶיךָ וְ**חַנֹּתִי אֶת־אֲשֶׁר אָחֹן וְרִחַמְתִּי אֶת־אֲשֶׁר אֲרַחֵם**
>
> **33:19 Thai (current):** …และเราจะประกาศชื่อของเรา — องค์พระผู้เป็นเจ้า — ต่อหน้าเจ้า **เราจะมีพระเมตตาต่อผู้ที่เราจะเมตตา และเราจะมีพระกรุณาต่อผู้ที่เราจะกรุณา**

**Two compounding drifts.** First, the verbal-noun mapping is **swapped relative to the corpus-doc**:

| Hebrew root | Doc-locked nominal Thai | 33:19 verbal Thai |
|---|---|---|
| חנן (חַנֹּתִי "I will be gracious") | **พระคุณ** (gracious) | **เมตตา** ✗ swapped |
| רחם (רִחַמְתִּי "I will be merciful") | **พระเมตตา** (compassionate/merciful) | **พระกรุณา** ✗ swapped |

Second, the 33:19 verbal mapping is **also swapped relative to the as-shipped Exod 34:6** (which uses רחום→กรุณา + חנון→เมตตา in the order the Hebrew has them):

| Verse | Hebrew | Thai |
|---|---|---|
| 33:19 | חַנֹּתִי + רִחַמְתִּי | **เมตตา + กรุณา** |
| 34:6 | רַחוּם + חַנּוּן | **กรุณา + เมตตา** |

Reading both verses, the cross-lemma assignment swaps within a single theophanic-cluster: 33:19 maps חנן→เมตตา and רחם→กรุณา; 34:6 maps רחום→กรุณา and חנון→เมตตา. Even on the as-shipped surface, the project's own internal lemma-Thai mapping is inconsistent between adjacent verses within the same theophanic-cluster.

The two-fold drift (vs. doc; vs. self) compounds when readers track the divine character through both verses.

**DECIDE before tagging — recommend normalization** in tandem with §2's Exod 34:6 normalization. The two verses should mirror each other lexically. Doc-aligned normalization:

| Verse | Hebrew | Doc-aligned Thai |
|---|---|---|
| 33:19 | חַנֹּתִי + רִחַמְתִּי | **เราจะทรงพระคุณต่อผู้ที่เราจะทรงพระคุณ และเราจะทรงพระเมตตาต่อผู้ที่เราจะทรงพระเมตตา** |
| 34:6 | רַחוּם + חַנּוּן | **พระเจ้าผู้ทรงพระเมตตาและทรงพระคุณ** |

(Note that Rom 9:15 quotes 33:19 in the NT; the Greek LXX renders חנן→ἐλεήσω and רחם→οἰκτιρήσω; the NT Pauline rendering compounds into Romans 9 election-discourse. The Thai mapping cascades into NT-side echo.)

---

## 4. Pharaoh's heart-hardening — three Hebrew roots, single Thai rendering — **STABLE (recommend corpus doc)**

The Exodus narrative deploys **three distinct Hebrew roots** for Pharaoh's heart-hardening across 19 occurrences (4:21, 7:3, 7:13, 7:14, 7:22, 8:15, 8:19, 8:32, 9:7, 9:12, 9:34, 9:35, 10:1, 10:20, 10:27, 11:10, 14:4, 14:8, 14:17):

| Hebrew root | Sense | Occurrences | Subject pattern |
|---|---|---|---|
| **חזק (Piel/Hiphil "strengthen / make-strong")** | strengthen-toward-defiance | 4:21, 7:13, 7:22, 8:19, 9:12, 9:35, 10:20, 10:27, 11:10, 14:4, 14:8, 14:17 (12×) | mostly YHWH-subject |
| **קשה (Hiphil "make-hard")** | make-stubborn | 7:3 (1×) | YHWH-subject |
| **כבד (Qal/Hiphil "be/make-heavy")** | weigh-down / be-burdened | 7:14, 8:15, 8:32, 9:7, 9:34, 10:1 (6×) | mixed: 8:15 + 8:32 + 9:34 Pharaoh-self; 10:1 YHWH-self |

**Thai (uniform across all 19):** **(ทำให้ใจ)ของฟาโรห์แข็งกระด้าง** — single Thai idiom for all three roots.

**Editorial assessment.** The Thai rendering is **principled but lexically collapsing**: the three Hebrew roots carry distinct biblical-theological weights (חזק "strengthen" connotes empowerment-toward-defiance; קשה "harden" connotes inner-stubbornness; כבד "make-heavy" connotes weight-of-judgment / burden-of-guilt). The Exodus narrator's careful alternation across these three roots is a **deliberate literary structure** (cf. Brevard Childs *Exodus* 170-175; Carol Meyers *Exodus* 78-79): YHWH starts with חזק (announcing), Pharaoh's self-hardening uses כבד, the final crescendo (chs.10–14) uses חזק exclusively. The Hebrew rhetorical structure tracks the increasing-divine-action arc.

The Thai's uniform **แข็งกระด้าง** flattens this distinction but matches THSV / BSB / NIV (all of which also use a single English/Thai phrase). The trade-off is well-understood in the translation literature: lexical-distinction-preservation requires three different Thai idioms, but Thai readers would then face the question "why three different words for what looks like the same action?" The Eremos choice is conservative and reader-friendly.

**Subject distinction is preserved in the Thai grammar.** When YHWH is subject ("เราจะทำให้ใจของฟาโรห์แข็งกระด้าง"), the Thai uses causative + 1st-person-divine; when Pharaoh is subject ("ใจของฟาโรห์ก็แข็งกระด้าง"), the Thai uses inchoative / stative; when "his heart became heavy" (the passive 7:13 etc.), the Thai uses the inchoative. So the subject-binding (the major exegetical question of who's hardening whom) is fully tracked, just at the syntactic rather than lexical level. **STABLE** ✓.

**→ Recommend new doc:** `docs/translator_decisions/pharaoh_heart_hardening_2026-05.md` — names the three-root pattern, the uniform Thai rendering, and the subject-tracking strategy. The doc would also lay groundwork for the **Isaiah 6:10 / Rom 9:18 / John 12:40 NT cross-reference cluster** (Pharaoh's hardening is the OT paradigm Paul builds on; the Eremos Thai should align across OT-and-NT for this cluster). Cost: 1 short doc + zero translation changes. Benefit: forward-protection for Deut 2:30, Josh 11:20, 1 Sam 6:6, Isa 6:10, Rom 9:18, Jn 12:40 — six future occurrences that will all benefit from the same locked Thai-strategy.

---

## 5. The Decalogue (Exod 20:1–17 and parallel Deut 5:6–21) — **LOCKED-with-Deut-5-deferred**

The Decalogue is rendered with high consistency:

| Verse | Thai opener / prohibition |
|---|---|
| **20:2 prologue** | "**เราคือองค์พระผู้เป็นเจ้าพระเจ้าของเจ้า** ผู้ทรงนำเจ้าออกจากแผ่นดินอียิปต์ ออกจากเรือนทาส" |
| **20:3 no other gods** | "**อย่ามีพระอื่นใดต่อหน้าเรา**" |
| **20:4 no graven image** | "**อย่าทำรูปเคารพหรือรูปจำลองสำหรับตนเอง**…" |
| **20:5 jealous-formula** | "…เป็น**พระเจ้าผู้หวงแหน** **ลงโทษความบาปของบิดาที่ผ่านไปยังบุตรชั่วอายุที่สามและที่สี่**…" |
| **20:6 chesed-formula** | "**แต่ทรงสำแดงความรักมั่นคงต่อพันชั่วอายุของผู้ที่รักเราและรักษาบัญญัติของเรา**" |
| **20:7 in vain** | "อย่ายกพระนามขององค์พระผู้เป็นเจ้าพระเจ้าของเจ้าโดยเปล่าประโยชน์" |
| **20:8 Sabbath** | "**จงระลึกถึงวันสะบาโต โดยรักษาให้บริสุทธิ์**" |
| **20:12 honor parents** | "จงให้เกียรติบิดามารดาของเจ้า…" |
| **20:13** | "**อย่าฆ่าคน**" (לֹא תִּרְצָח) |
| **20:14** | "**อย่าล่วงประเวณี**" |
| **20:15** | "**อย่าลักทรัพย์**" |
| **20:16** | "**อย่าเป็นพยานเท็จต่อเพื่อนบ้านของเจ้า**" |
| **20:17** | "**อย่าโลภบ้านของเพื่อนบ้านเจ้า** อย่าโลภภรรยา…" |

**Compliance.** The **chesed lock** at 20:6 uses the corpus-doc canonical **ความรักมั่นคง** ✓; this contrasts with the §2 finding at 34:6 (where the chesed sub-lock is also preserved but the surrounding character-cluster drifts). The **jealous-formula** at 20:5 uses **พระเจ้าผู้หวงแหน** for אֵל קַנָּא, consistent with 34:14 (the same lemma; same Thai) ✓. The **prohibition-formula** for the four short commandments (אַל / לֹא + imperfect) renders consistently as **อย่า + verb** ✓. The Sabbath imperative **זָכוֹר** ("remember") is preserved as **จงระลึกถึง** ✓.

**Cross-corpus consideration.** Deut 5:6–21 (the parallel Decalogue) will be the next major test of this Thai vocabulary. The differences between Exod 20 and Deut 5 (Sabbath rationale: Exod 20:11 cites creation; Deut 5:15 cites Exodus-from-Egypt) need their own locking precedent at Deut 5's ship-time. **Recommend a `decalogue_thai_lock_2026-05.md` doc** that names Exod 20:1–17 as the Thai-locking precedent, lists the 10 prohibitions in canonical-Thai form, and identifies the Exod-vs-Deut variant rationales for the Sabbath + 10th-commandment that will need handling at Deut 5 ship-time.

**LOCKED** ✓ in current handling; **DOC LIFT RECOMMENDED** before Deut 5 ships.

---

## 6. The Pesach + Matzot complex (chs.12–13) — **LOCKED**

The Passover-vocabulary at chs.12–13 establishes the Thai locking-precedent for the entire Passover thread (Lev 23, Num 9, Num 28, Deut 16, Josh 5, 2 Kgs 23, Ezra 6, 2 Chr 35, then the NT Last-Supper / Crucifixion-pesach trajectory in the four Gospels + 1 Cor 5:7):

| Hebrew | Thai (Exodus locked) | Notes |
|---|---|---|
| **פֶּסַח (Passover)** | **ปัสกา** | Transliterated. Note: NT corpus uses **เทศกาลปัสกา** ("Passover-festival") for Greek πάσχα — matches OT |
| **חַג הַמַּצּוֹת (Feast of Unleavened Bread)** | **เทศกาลขนมปังไร้เชื้อ** | 12:17, 23:15 |
| **מַצּוֹת (unleavened bread)** | **ขนมปังไร้เชื้อ** | 12:18, 13:6, 13:7 |
| **חָמֵץ (leaven / leavened)** | **เชื้อ** | 12:15, 12:19 |
| **מָרֹר (bitter herbs)** | **ผักขม** | 12:8 |
| **בְּכוֹר (firstborn)** | **บุตรหัวปี** | 11:5, 12:12, 12:29, 13:2, 13:13, 13:15 — consistent across the firstborn-thread |
| **גֵּר ger (sojourner)** | **คนต่างถิ่น** | 12:48–49, 22:21, 23:9 — consistent |
| **בֶּן־נֵכָר (foreign-born)** | **คนต่างชาติ** | 12:43 — distinguished from ger |

**12:38 עֵרֶב רַב "mixed multitude"** → **ฝูงชนหลากหลายเชื้อชาติ** (literally "crowd of various ethnicities"; neutral-demographic, not pejorative). Matches the Genesis-audit GEN finding pattern (preserve Hebrew register without sensationalism).

**12:40 בְּמִצְרַיִם שְׁלֹשִׁים שָׁנָה וְאַרְבַּע מֵאוֹת שָׁנָה** "430 years in Egypt" — rendered **เวลาที่บุตรอิสราเอลอาศัยอยู่ในอียิปต์เป็น 430 ปี**. The MT-vs-LXX-vs-SP divergence (SP + LXX read "in Egypt **and Canaan**", which Paul cites at Gal 3:17 as the 430-year-from-Abraham figure) is not currently surfaced in the textual_variants Layer-2 footer at `output/textual_variants/exodus_12.json` — recommend adding a Layer-2 entry naming the LXX/SP variant and the Gal 3:17 NT cross-reference, per the `mt_vs_lxx_textual_variant_handling_2026-05.md` precedent (Gen 4:8 / 46:27 / 47:31). The Gal 3:17 reference is the most-cited NT recapitulation of the 430-year figure, and the LXX/SP "in-Egypt-and-Canaan" reading reconciles it with the Gen 15:13 + Gen 12:4 + Acts 7:6 timeline. **Severity: LOW (textual-tradition footnote gap)** — translation surface is fine; reader-edition transparency would benefit from a Layer-2 lift.

**LOCKED** ✓.

---

## 7. כְּבוֹד יְהוָה "glory of YHWH" — **STABLE**

The כָּבוֹד-thread is the structural climax of Exodus (the book opens with Israel's affliction and closes with the כְּבוֹד filling the tabernacle 40:34–35). Six anchor verses:

| Verse | Hebrew | Thai |
|---|---|---|
| **14:4** | וְאִכָּבְדָה בְּפַרְעֹה | "เราจะได้รับเกียรติโดยผ่านฟาโรห์" |
| **16:7** | וּרְאִיתֶם אֶת־כְּבוֹד יְהוָה | "พวกเจ้าจะเห็นพระสิริขององค์พระผู้เป็นเจ้า" |
| **16:10** | כְּבוֹד יְהוָה נִרְאָה | "พระสิริขององค์พระผู้เป็นเจ้าก็ปรากฏ" |
| **24:16** | כְּבוֹד־יְהוָה | "พระสิริขององค์พระผู้เป็นเจ้า" |
| **24:17** | מַרְאֵה כְּבוֹד יְהוָה | "ภาพของพระสิริขององค์พระผู้เป็นเจ้า" |
| **29:43** | וְנִקְדַּשׁ בִּכְבֹדִי | "ที่นั้นจะได้รับการชำระให้บริสุทธิ์โดยพระสิริของเรา" |
| **33:18** | הַרְאֵנִי נָא אֶת־כְּבֹדֶךָ | "ขอทรงแสดงพระสิริของพระองค์แก่ข้าพระองค์เถิด" |
| **33:22** | בַּעֲבֹר כְּבֹדִי | "เมื่อพระสิริของเราผ่านไป" |
| **40:34–35** | כְּבוֹד יְהוָה מָלֵא אֶת־הַמִּשְׁכָּן | "พระสิริขององค์พระผู้เป็นเจ้าก็เต็มพลับพลา" |

**Compliance.** Uniform **พระสิริ** for כָּבוֹד as divine-glory across all 9 anchor verses ✓. At 14:4 + 14:17–18 where כָּבַד shifts to the Niphal verbal sense ("be glorified through/over"), the Thai shifts to **ได้รับเกียรติ** (be-honored / receive-glory) — this is the principled lexical pair that distinguishes the nominal-state ("glory") from the verbal-process ("be-glorified-over") within the Hebrew root. **STABLE** ✓.

**Forward-compounding.** The 40:34–35 capstone ("Moses could not enter…the glory filled") echoes 1 Kgs 8:10–11 (Solomon's-temple parallel) and Ezek 43:1–5 (return of the כָּבוֹד) and the NT trajectory at Lk 2:9 + Jn 1:14 (μονογενοῦς ... δόξαν) + Rev 21:23. The Thai **พระสิริ** holds across the entire OT-and-NT trajectory.

---

## 8. The Stiff-Necked Formula — **LOCKED**

| Verse | Hebrew | Thai |
|---|---|---|
| **32:9** | עַם־קְשֵׁה־עֹרֶף הוּא | "ชนชาติคอแข็ง" |
| **33:3** | עַם־קְשֵׁה־עֹרֶף אַתָּה | "ชนชาติคอแข็ง" |
| **33:5** | אַתֶּם עַם־קְשֵׁה־עֹרֶף | "ชนชาติคอแข็ง" |
| **34:9** | עַם־קְשֵׁה־עֹרֶף הוּא | "ชนชาติคอแข็ง" |

Uniform **ชนชาติคอแข็ง** for the post-golden-calf formula across all 4 occurrences ✓. The Acts 7:51 NT recapitulation (Stephen's speech: σκληροτράχηλοι "stiff-necked") will need the same Thai-lock at Acts ship — verify the NT-side compliance.

**LOCKED** ✓.

---

## 9. מַלְאַךְ YHWH / מַלְאָךְ — **REVIEW (cross-verse drift)**

Six "angel/messenger of YHWH" occurrences in Exodus render with **at least four distinct Thai variants**:

| Verse | Hebrew | Thai (current) |
|---|---|---|
| **3:2** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **14:19** | מַלְאַךְ הָאֱלֹהִים | **ทูตของพระเจ้า** |
| **23:20** | מַלְאָךְ (anarthrous) | **ทูตสวรรค์** |
| **23:23** | מַלְאָכִי (1cs pron suffix) | **ทูตสวรรค์ของเรา** |
| **32:34** | מַלְאָכִי | **ทูตของเรา** |
| **33:2** | מַלְאָךְ | **ทูตสวรรค์** |

**Editorial assessment.** The four variants ("ทูต" + qualifier vs. "ทูตสวรรค์") are not interchangeable in Thai. **ทูตสวรรค์** (literally "heavenly messenger") is the NT-corpus default for ἄγγελος (locked at numerous places in the Gospels + Acts + Revelation). **ทูต** alone (without สวรรค์) is plain "messenger / envoy / ambassador" — used in Thai diplomatic register without supernatural connotation. The current EXO mix reads as: 3:2 + 14:19 + 32:34 are **plain "envoy of YHWH/God"** (lower-supernatural-marking); 23:20 + 23:23 + 33:2 are **"heavenly messenger"** (full angelic-marking). The Hebrew text itself does not distinguish — the same lemma מַלְאָךְ appears in all 6.

A typical Thai-evangelical reader will read 3:2 ("ทูตขององค์พระผู้เป็นเจ้า") and 23:20 ("ทูตสวรรค์") as **different categories of being** — exactly the cross-corpus drift the project's term-consistency policy was created to prevent.

**REVIEW flag.** Confirm Ben endorses one of three resolution paths:
- (a) **Normalize to ทูตสวรรค์ throughout** for divine-מַלְאָךְ verses (lock the angelic-supernatural reading; matches NT-corpus default). Adjustments at 3:2 (→ "ทูตสวรรค์ขององค์พระผู้เป็นเจ้า"), 14:19 ("ทูตสวรรค์ของพระเจ้า"), 32:34 ("ทูตสวรรค์ของเรา").
- (b) **Normalize to ทูต throughout** for OT-corpus mal'akh-yhwh verses (lock the "messenger-of-YHWH as theophanic-agent" reading, which preserves Hebrew's underdetermined ontological status; the NT-corpus then independently uses ทูตสวรรค์ for ἄγγελος). Adjustments at 23:20, 23:23, 33:2.
- (c) **Doc-lift** — write `docs/translator_decisions/malak_yhwh_2026-05.md` naming the OT-corpus Thai-lock + the rationale + the cross-reference to NT angelology. Either (a) or (b) above should be the doc's choice; the doc names the principle.

The decision compounds across Genesis (Hagar 16:7, Sodom 19:1+15, Akedah 22:11+15, Jacob's-ladder 28:12, Mahanaim 32:1, Jacob-wrestling 32:24-30 indirectly), Numbers (22:22-35 Balaam), Judges (2:1+4, 6:11+12+21+22, 13:3-21 Manoah), Samuel (2 Sam 24:16), Kings (1 Kgs 19:5+7, 2 Kgs 1:3+15), Zechariah (1:9-19, 2:3-7, 3:1-7, 4:1-7, 5:5-10, 6:4-5), Daniel (3:28, 6:22), and Malachi (3:1 himself — the literary mal'akh-bookend). Without normalization the lemma-thread is broken in nearly every OT-corpus angelic-theophany.

**Recommend (a) + (c)** — normalize to ทูตสวรรค์ + write the doc. The normalization is mechanical (3 verse-edits), the doc is short (1 day of writing), and the forward-protection is corpus-wide.

---

## 10. כַּפֹּרֶת "atonement-cover / mercy-seat" — **REVIEW (within-book drift)**

The atonement-cover atop the Ark is named in chs. 25, 30, 37, 40:

| Verse | Hebrew | Thai (current) |
|---|---|---|
| **25:17** | וְעָשִׂיתָ כַפֹּרֶת | **พระที่นั่งกรุณา** (literally "throne of grace") |
| **25:18** | מִשְּׁנֵי קְצוֹת הַכַּפֹּרֶת | **พระที่นั่งกรุณา** |
| **25:22** | מֵעַל הַכַּפֹּרֶת | **พระที่นั่งกรุณา** |
| **30:6** | לִפְנֵי הַכַּפֹּרֶת אֲשֶׁר עַל־הָעֵדֻת | **พระที่นั่งกรุณาที่อยู่บนพระโอวาท** |
| **37:6** | וַיַּעַשׂ כַּפֹּרֶת | **พระที่นั่งกรุณา** |
| **37:7** | מִשְּׁנֵי קְצוֹת הַכַּפֹּרֶת | **พระที่นั่งกรุณา** |
| **37:8–9** | (כְּרוּב … עַל־הַכַּפֹּרֶת) | **พระที่นั่งกรุณา** |
| **40:20** | וַיִּתֵּן אֶת־הַכַּפֹּרֶת עַל־הָאָרוֹן | **ที่ลบล้างบาป** (literally "place that wipes-away sin") |

**Editorial assessment.** Eight occurrences across chs.25–37 use **พระที่นั่งกรุณา** (the THSV-style "throne of mercy/grace" rendering); the single 40:20 occurrence in the execution-narrative uses **ที่ลบล้างบาป** (the etymological/atonement-functional rendering, closer to the כפר root "cover/atone-for"). Both renderings are defensible — the Hebrew kapporet derives from kpr ("atone / cover"), and the LXX/Pauline tradition (ἱλαστήριον at Rom 3:25 + Heb 9:5) reads atonement-functionally — but they should not coexist in the same book.

**REVIEW flag.** Recommend normalization to a single Thai rendering. Two paths:
- (a) **Normalize 40:20 to พระที่นั่งกรุณา** — matches the 8 prior occurrences; preserves the throne-image (which is the rabbinic + classical-Christian reading: God's throne above the cherubim). Simpler, but loses the etymological-atonement signal.
- (b) **Normalize all 9 to ที่ลบล้างบาป** — recovers the kpr-atonement etymology; matches the NT-corpus's Rom 3:25 (where ἱλαστήριον recapitulates kapporet directly). Requires 8 verse edits.
- (c) **Doc-lift** — write a corpus-doc + choose. The decision compounds into Lev 16 (Yom Kippur, the kapporet-blood-application ritual) + Rom 3:25 + Heb 9:5. The doc would also handle the related lemma כָּפַר ("atone") which appears extensively in Lev + Num.

**Recommend (a) + doc-lift** — the throne-of-grace reading is the dominant Thai-evangelical tradition; the doc names the choice and cross-references Rom 3:25's NT-corpus handling.

---

## 11. YHWH-Nissi (Exod 17:15) — **REVIEW (paraphrase vs. table principle)**

| Verse | Hebrew | Thai |
|---|---|---|
| **17:15** | וַיִּקְרָא שְׁמוֹ יְהוָה נִסִּי | "(โมเสสสร้างแท่นบูชาและตั้งชื่อว่า) **'องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า'**" |

Compare the Genesis precedent (locked in `divine_names_table_2026-05.md` §"place-name compounds"):

| Verse | Hebrew | Thai (Genesis-locked) |
|---|---|---|
| GEN 22:14 | יְהוָה יִרְאֶה | **ยาห์เวห์ยีเรห์** (transliterated + parenthetical gloss) |

**Editorial assessment.** The Genesis convention for YHWH-compounded altar-names is to **transliterate** the Hebrew compound + add a parenthetical Thai gloss. Exodus 17:15 deviates from this convention: **the place-name is paraphrased rather than transliterated**. A consistent treatment would be:

> "(โมเสสสร้างแท่นบูชาและตั้งชื่อว่า) **'ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)'**"

The same question applies to **Exod 15:26 יְהוָה רֹפְאֶךָ** ("YHWH-your-Healer"; rendered "องค์พระผู้เป็นเจ้าผู้รักษาเจ้า" — paraphrased, not transliterated). This is a divine-self-title rather than a place-name, so the transliteration-or-paraphrase question is sharper here.

**REVIEW flag.** Confirm Ben endorses one of three resolution paths:
- (a) **Normalize Exod 17:15 to transliterated-place-name + gloss** ("ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)") to match Genesis 22:14's convention. Cost: 1 verse edit.
- (b) **Doc-amend** to recognize that Exodus has a category of YHWH-paraphrastic-self-titles (15:26 רֹפְאֶךָ "your healer"; 17:15 נִסִּי "my banner") distinct from the Genesis place-name-compound category (22:14 יִרְאֶה "will-see/provide" gave its name to the *place*; the Exod 17:15 and 15:26 phrases are altar-names / proclamations rather than place-names per se). Recommend explicit doc-amendment naming this sub-category + the Thai-paraphrase principle.
- (c) **Current** — leave as-is. The current rendering is reader-friendly (Thai readers can parse "ธงชัย" directly) but corpus-inconsistent.

**Recommend (b)** — doc-amend the divine_names_table to add a "YHWH-paraphrastic-self-title" sub-category that names this principled distinction, with Exod 15:26 + 17:15 + 17:16 ("כִּי־יָד עַל־כֵּס יָה") + 31:13 ("יְהוָה מְקַדִּשְׁכֶם") as Exodus's locking-precedent occurrences. The doc would clarify that future books should match this rule.

---

## 12. פָּנִים "face / presence" in Exodus 33 — **REVIEW (intra-chapter drift)**

The face/presence vocabulary in the Sinai-theophany cluster of Exodus 33–34 has FIVE occurrences with **two distinct Thai conceptual mappings within the same chapter**:

| Verse | Hebrew | Thai (current) | Mapping |
|---|---|---|---|
| **33:11** | פָּנִים אֶל־פָּנִים | "หน้าต่อหน้า" | "face-to-face" (literal) |
| **33:14** | פָּנַי יֵלֵכוּ | "การประทับของเรา" | "my presence" (paraphrase) |
| **33:15** | אִם־אֵין פָּנֶיךָ הֹלְכִים | "การประทับของพระองค์" | "your presence" (paraphrase) |
| **33:20** | לֹא תוּכַל לִרְאֹת אֶת־פָּנָי | "ใบหน้าของเรา" | "my face" (literal) |
| **33:23** | וּפָנַי לֹא יֵרָאוּ | "ใบหน้าของเรา" | "my face" (literal) |

**Editorial assessment.** This pattern follows the NIV / ESV / KJV English tradition: when פָּנִים has an agentive verbal-complement ("face will go / face is going"), translate as "presence"; when פָּנִים has a sensory verb ("see / not-see the face"), translate as literal "face." The split is principled at the English-level (English "presence" preserves the agentive-going sense without anthropomorphism) and Thai mirrors that.

But the **Hebrew lemma is uniform**: פָּנִים at 33:14–15 and פָּנִים at 33:20+23 are the same word. The intra-chapter rendering split makes the Thai reader experience the divine-face-question as if two different things were being discussed. The theological tension — Moses asks to see God's "face" but God says "my face will not be seen," while at the same time God says "my face will go with you" — is at the heart of Exodus 33, and the lexical-shift in the Thai dilutes it.

**REVIEW flag.** Three resolution paths:
- (a) **Current** — preserve NIV/ESV-style split (presence/face); preserve at the verse-level KD the lemma-uniformity at the Hebrew side. Reader-friendly; matches the dominant English-Bible tradition; loses the cross-verse lemma-thread.
- (b) **Normalize to "พระพักตร์" (royal-Thai for face) throughout** — restores the lemma-thread; reads as "my royal-face will go with you" at 33:14, which works in Thai royal-register (similar to Thai court usage of พระพักตร์ for kings and divine figures). Cost: 3 verse edits at 33:14, 33:15, 33:20+23 (last two are already "ใบหน้า" → would shift to "พระพักตร์" to match register).
- (c) **Doc-lift** — write a corpus-doc naming the split principle and the rationale. Per `hebrew_idioms_and_metaphor_2026-05.md`, "presence-of-YHWH / face-of-YHWH" should consistently render as **เบื้องพระพักตร์** / **พระพักตร์** in the Eremos OT corpus. So technically the current EXO 33 rendering DRIFTS from `hebrew_idioms_and_metaphor_2026-05.md` (which is explicit about פָּנִים → พระพักตร์ uniformly). The doc lift is therefore option (b).

**Recommend (b)** — normalize per the existing doc. The NIV/ESV "presence" tradition is principled but the project's corpus-doc explicitly chose otherwise; the drift here is a §15-style inherited-lock-violation rather than a new question.

---

## 13. Exod 3:14 אֶהְיֶה אֲשֶׁר אֶהְיֶה "I am that I am" — **REVIEW**

| Verse | Hebrew | Thai (current) |
|---|---|---|
| **3:14a** | אֶהְיֶה אֲשֶׁר אֶהְיֶה | "**เราเป็นผู้ที่เราเป็น**" |
| **3:14b** | אֶהְיֶה שְׁלָחַנִי אֲלֵיכֶם | "**'เราเป็น' ได้ส่งข้าพเจ้ามาหาพวกท่าน'**" |

**Editorial assessment.** The self-naming "**เราเป็น**" preserves the Hebrew אֶהְיֶה ("I am / I will be") as a divine-name, NOT as a copular verb. This is the ESV / NIV style (KJV "I AM THAT I AM"; NIV "I AM WHO I AM"). The Thai works idiomatically but two minor issues are worth surfacing:

1. **Punctuation drift at 3:14b.** The current Thai has an extra closing single-quote after "พวกท่าน": `"‘เราเป็น’ ได้ส่งข้าพเจ้ามาหาพวกท่าน'"` — should be `"‘เราเป็น’ ได้ส่งข้าพเจ้ามาหาพวกท่าน"` (close the outer double-quote, not a stray single-quote). Mechanical fix; not a content question.
2. **The אֶהְיֶה → יהוה etymological link** is documented in the textual_variants Layer-2 footer at `output/textual_variants/exodus_03.json` (the burning-bush + Ehyeh-self-disclosure node) — this is correctly handled. The Thai surface preserves the link by reading both Ex 3:14 ("เราเป็น") and Ex 3:15 ("องค์พระผู้เป็นเจ้า…") in the same divine speech.

**REVIEW flag (LOW severity).** Fix the punctuation; confirm Ben endorses the **เราเป็น** rendering (alternative: **เราคือผู้ทรงอยู่** — "I am the one who exists," matching the LXX ἐγὼ εἰμι ὁ ὤν).

---

## 14. Exod 15:11 בָּאֵלִם "among the gods" — **DECIDE**

The Song of the Sea includes a sensitive rhetorical question:

> **15:11 Hebrew:** מִי־כָמֹכָה בָּאֵלִם יְהוָה
>
> **15:11 Thai:** ใครในหมู่**พระทั้งหลาย**เหมือนพระองค์ ข้าแต่องค์พระผู้เป็นเจ้า

**Editorial assessment.** **ในหมู่พระทั้งหลาย** ("among the gods") preserves the Hebrew בָּאֵלִם plural-gods construction. This matches the literal LXX (ἐν θεοῖς) and is defensible — Exod 15 is the OT's oldest poetic stratum and contains traces of Yahweh-as-incomparable-among-other-gods register (cf. Ps 82:1, Ps 89:6, Ps 95:3; the rhetorical-comparative form in pre-monotheistic-development Hebrew). The Thai surface preserves this.

But: a typical Thai-evangelical reader of **ในหมู่พระทั้งหลาย** will read this as confirming **the existence of other gods** — which conflicts with the monotheistic frame the Thai-evangelical church understands as the OT's overall theology. THSV-1971 reads "เทพเจ้าทั้งหลาย" (similar register); some modern Thai translations paraphrase to "เทพเจ้าใดหรือที่จะเปรียบเทียบกับพระองค์ได้" ("which deities could compare with you") to preserve the rhetorical-question while neutralizing the polytheistic surface.

**DECIDE flag.** Confirm Ben endorses one of three resolution paths:
- (a) **Current** — preserve the Hebrew בָּאֵלִם as-is with **พระทั้งหลาย**. Most faithful to the Hebrew text's pre-monotheistic-development register. Defensible academically; risks reader-confusion in the Thai-evangelical context.
- (b) **Paraphrase to "เทพเจ้าใดเหมือนพระองค์"** — preserves the rhetorical-comparison; reads as "no deity is like you" rather than "no god among (the existing) gods is like you." Reader-friendly; muffles the Hebrew's mythopoetic surface.
- (c) **Doc-lift** — write a corpus-doc on **OT polytheistic-register vocabulary** (covering Exod 15:11, Deut 10:17 אֱלֹהֵי הָאֱלֹהִים, Pss 82 / 86 / 89 / 95 / 96 / 97 / 135 / 136 / 138, Job 1:6 בְּנֵי הָאֱלֹהִים, Isa 41–43 idol-polemic, etc.). The doc names the project's stance and lists locking-precedent occurrences.

**Recommend (c) + (a)** — preserve the Hebrew surface at Exod 15:11 (most-faithful) but lock the rationale in a corpus-doc to prevent ad-hoc drift in later books. The doc compounds into the existing `spiritual_beings_hierarchy_2026-05.md` (which currently covers angelology + Daniel-apocalyptic; would extend with an "OT-polytheistic-register" sub-section).

---

## 15. Inherited corpus locks — **all compliant except where flagged**

| Doc | EXO evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | See §1. Tetragrammaton-as-องค์พระผู้เป็นเจ้า uniform; standalone Adonai 4:10, 4:13, 15:17, 34:9 all render องค์เจ้านาย per table; El Shaddai 6:3 → พระเจ้าผู้ทรงมหิทธิฤทธิ์; Yah 15:2 + 17:16 → ยาห์. **EXCEPTION: YHWH-Nissi 17:15 paraphrased rather than transliterated — see §11.** | **LOCKED-with-§11-flag** |
| `ot_register_policy_2026-05.md` | Divine-speech ทรง- throughout (3:2+, 6:2+, 19, 20, 33, 34); Pharaoh receives Rachasap **ทรง- on action verbs** (1:22, 2:15, 5:6, 7:11, 7:23, 8:4+11+21, 9:7+27+34, 10:16+24, 12:30+31, 13:17, 14:6) and **royal Thai speech-verb ตรัส** elsewhere — 17 ทรง- + extensive ตรัส usage = Pharaoh-as-foreign-emperor register correctly applied per §2.2. Moses receives **plain narrator** throughout ✓ (matches doc rule for prophet-leaders). Hebrew midwives, Egyptian taskmasters, Jethro: plain register ✓. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | 4 occurrences (15:13, 20:6, 34:6, 34:7) — all render ความรักมั่นคง ✓. **EXCEPTION: 34:6+7 surrounding character-cluster drifts — see §2.** | **LOCKED-with-§2-flag** |
| `exod_34_attribute_formula_2026-05.md` | **MAJOR DRIFT at the doc's own locking precedent — see §2.** | **DRIFT (DECIDE)** |
| `nicham_divine_relenting_2026-05.md` | EXO 32:14 (וַיִּנָּחֶם יְהוָה עַל־הָרָעָה "YHWH relented from the disaster" — Moses-intercession context) — renders **ทรงเปลี่ยนพระทัย** ✓ matches doc's factive-volitional sub-rendering. Compliant. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | EXO 6:8 (וְהֵבֵאתִי ... אֲשֶׁר נָשָׂאתִי אֶת־יָדִי "the land I raised my hand to give") → "ที่เรายกมือสาบานว่าจะมอบให้" ✓; 13:5 oath ✓; 17:16 "(my) hand upon the throne of Yah" altar-oath ✓; 19:8 + 24:3 + 24:7 covenant-oaths ✓. Compliant. | **LOCKED** |
| `paqad_visit_attend_2026-05.md` | EXO 3:16 (פָּקֹד פָּקַדְתִּי "I have surely visited you" — Joseph's-prophecy fulfilled); 4:31 (paralleled); 13:19 (Joseph's-bones-claim per Gen 50:25 prophecy); 20:5 (פֹּקֵד עֲוֹן "visiting iniquity"); 32:34 (וּבְיוֹם פָּקְדִי וּפָקַדְתִּי). The dual-sense פָּקַד split is correctly handled: **mercy-visitation (3:16, 4:31, 13:19)** → "เสด็จมาเยี่ยม / มาเยือน"; **judgment-visitation (20:5, 32:34, 34:7)** → "ลงโทษ". Compliant per doc's sub-rule split. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Hand of YHWH" (9:3, 9:15, 13:9, 14:31, 15:6+12, 24:11, 31:18, 33:22-23) → **พระหัตถ์ / มือ** as anthropomorphism; "outstretched arm" (6:6, 15:16) → **พระกร**; "face" 33:11+20+23 → ใบหน้า / หน้า — **DRIFT at 33:14-15 — see §12.** Most-other anthropomorphisms compliant. | **LOCKED-with-§12-flag** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains throughout; cognate-accusatives at 32:31 (חָטָאוּ ... חֲטָאָה גְדֹלָה), 35:35 (חֹשְׁבֵי מַחֲשָׁבֹת), 39:1 (וְלַעֲשׂוֹת ... מַעֲשֶׂה); infinitive-absolute intensifiers at 3:16 (פָּקֹד פָּקַדְתִּי), 21:5 (אָהֵב אֹהֵב); imperative-of-prohibition (Decalogue 20:13-17). Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "presence/face-of-YHWH" → DRIFT at 33:14-15 — see §12; all other anthropomorphic-action idioms (e.g., "YHWH passes before face" 33:19+34:6) compliant; "land flowing with milk and honey" 3:8+17, 13:5, 33:3 → uniform "แผ่นดินที่มีน้ำนมและน้ำผึ้งไหล" ✓; "stiff-necked" — see §8. | **LOCKED-with-§12-flag** |
| `verse_schema_and_versification_2026-05.md` | EXO has minor MT-vs-English versification divergences at the 21:37/22:1 boundary (MT renumbers 22:1 as 21:37 — handled by following MT divisions throughout); 7:26 / 8:1 boundary (same). Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | 100+ proper-noun renderings spot-checked: Moses **โมเสส**, Aaron **อาโรน**, Miriam **มิเรียม**, Jethro/Reuel **เยโธร / เรอูเอล**, Zipporah **ศิปโปราห์**, Gershom **เกอร์โชม**, Eliezer **เอลีเอเซอร์**, Joshua **โยชูวา**, Hur **เฮอร์**, Bezalel **เบซาเลล**, Oholiab **อาโฮลีอาบ**, Pharaoh **ฟาโรห์**, Pithom/Raamses **พิธอม / รามเสส**, Goshen **โกเชน**, Succoth **สุคโคท**, Etham **เอธาม**, Pi-hahiroth **ปีฮาฮีโรท**, Migdol **มิกดอล**, Baal-Zephon **บาอัลเศโฟน**, Marah **มาราห์**, Elim **เอลิม**, Sin **ซีน**, Rephidim **เรฟีดิม**, Sinai/Horeb **ซีนาย / โฮเรบ**, Amalek **อามาเลข**, Massah/Meribah **มัสสาห์ / เมรีบาห์**. All consistent with corpus-doc rules. | **LOCKED** |
| `proper_noun_wordplay_2026-05.md` | EXO has 4 paronomastic-name etymologies: **Moses** (2:10 מָשָׁה "drawn-out") — KD documented; **Gershom** (2:22 גֵּר שָׁם "stranger there") — KD documented; **Marah** (15:23 מַר "bitter"); **Massah and Meribah** (17:7 נָסָה "test" + רִיב "quarrel"). All per doc principles. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | Major Exodus leitwortes preserved: **יָדַע "know-YHWH"** thread (6:7, 7:5, 7:17, 8:10, 8:22, 9:14, 9:29, 10:2, 11:7, 14:4, 14:18, 16:6, 16:12, 18:11, 29:46, 31:13, 33:13, 33:16-17) — uniform "**(พวกเขาจะ)รู้ว่าเราคือองค์พระผู้เป็นเจ้า**" ✓ corpus-doc compliant; **קָרָא "call / name"** thread (16:31, 17:7, 17:15, 33:7, 33:19, 34:5, 34:6) — uniform เรียก/ตั้งชื่อ ✓; **שָׁמַע "hear"** thread — uniform ฟัง ✓. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` (Genesis-locked) | EXO has fewer headline MT-vs-LXX divergences than Genesis. Notable: 12:40 (MT "in-Egypt-430" vs. LXX/SP "in-Egypt-AND-Canaan-430"; Gal 3:17 cites the LXX/SP timeline) — Layer-2 footer recommended but currently absent. See §6. | **LOCKED-with-§6-flag** |
| `manah_divine_appointment_2026-05.md` | מָנָה does not appear in Exodus with God-as-subject. N/A. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | Egyptian gods context: Pharaoh's חרטמים "magicians" (7:11, 7:22, 8:7, 8:18-19, 9:11) → "หมอผี" ✓; Egyptian gods 12:12 ("on all the gods of Egypt I will execute judgments") → "พระทั้งหลายของอียิปต์"; Baal-Zephon 14:2 + 14:9 (place-name with theophoric element) → "บาอัลเศโฟน" transliterated. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator royal-Thai for divine acts ✓; speaker-register distinguishes Moses' prophet-voice (humble ข้าพระองค์ to YHWH; authoritative narrator to Pharaoh) from YHWH's divine-1ps (เรา) ✓. Pharaoh's speech uses ตรัส (royal-Thai speech-verb) consistently. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | Song of the Sea (15:1-18) — anthemic praise vocabulary preserved per doc (อ้างเชิดชู, ยกย่อง, สรรเสริญ, สาธุการ); 18:10–11 (Jethro's blessing) → "สาธุการแด่องค์พระผู้เป็นเจ้า…". Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative uses wayyiqtol; doc is Greek-NT-specific. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` (NT) | N/A — Exodus is OT. The OT-companion handling is per `mt_vs_lxx_textual_variant_handling_2026-05.md`. | **LOCKED (N/A)** |

---

## 16. Pre-existing docs to recommend NEW or AMEND from Exodus

(Following the Genesis-audit-recommendation-template; only the NEW recommendations from Exodus that didn't already land:)

- **`pharaoh_heart_hardening_2026-05.md`** — see §4. Locks the three-Hebrew-roots-to-single-Thai principle; cross-references Isa 6:10 + Rom 9:18 + Jn 12:40. NEW.
- **`decalogue_thai_lock_2026-05.md`** — see §5. Locks the 10-prohibition Thai vocabulary; cross-references Deut 5 forthcoming. NEW.
- **`malak_yhwh_2026-05.md`** — see §9. Locks the OT-corpus mal'akh-yhwh Thai (recommend ทูตสวรรค์); cross-references NT corpus's ทูตสวรรค์-for-ἄγγελος lock. NEW.
- **`ot_polytheistic_register_2026-05.md`** — see §14. Locks the Hebrew-polytheistic-surface vocabulary (Pss 82, 86, 89, etc., bĕnê hāʾĕlōhîm at Job 1:6); decides between Hebrew-faithfulness and Thai-evangelical-default. NEW.
- **`kapporet_atonement_cover_2026-05.md`** — see §10. Locks the Thai rendering (recommend พระที่นั่งกรุณา) + cross-references Lev 16 + Rom 3:25 + Heb 9:5. NEW.
- **`divine_names_table_2026-05.md` AMENDMENT** — see §11. Add a "YHWH-paraphrastic-self-title" sub-category (Exod 15:26 + 17:15 + 31:13). AMEND existing.
- **`exod_34_attribute_formula_2026-05.md` IMPLEMENTATION** — see §2. The doc's §3 Implementation Checklist item 2 (check_phrase_consistency.py extension for the formula) has not yet been written. Recommend writing it in tandem with the §2 normalization commit. AMEND.

---

## 17. Mechanical (§1) — **all green**

- 40/40 chapters: `output/check_reports/exodus_NN_review.md` + sub-reports ✓
- 40/40 chapters: `output/back_translations/exodus_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 224-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (8 phrase-consistency rules audited 7,943 verses)
- `python3 scripts/audit_inclusion_variants.py --book EXO --strict`: **0 candidates** (NT-style inclusion-variants policy N/A for OT books; OT-corpus-side handled by `mt_vs_lxx_textual_variant_handling_2026-05.md`)
- `git status output/`: only `output/check_reports/divine_names.md` modified (re-run by audit-time invocation; the C-soft warning at 40:18 is a script-side false positive — אֲדָנָיו "its bases" is normalized to the same consonants אדני as Adonai; **the actual Hebrew at 40:18 is the tabernacle's bases/sockets, not Adonai**, so no key_decisions handling required). No source-file dirt.
- 38/40 chapters: `output/textual_variants/exodus_NN.json` present (ch.1 + ch.2 have no Tetragrammaton, so no first-occurrence footnote required — matches Gen 1 precedent). Recommend writing a `no_yhwh_in_chapter` placeholder for ch.1 + ch.2 + ch.26 + ch.37 + ch.21 for shape-consistency with Ruth/Jonah conventions.
- Hebrew word-spacing **clean for all 40 chapters** (no regression of the Gen-chs-26-50 pattern) ✓
- `thai_literal` is **Thai for all 40 chapters** (no regression of the Gen-chs-44-50 English-leakage pattern) ✓
- divine_names.md soft-warning at EXO 40:18 — **false positive** (אֲדָנָיו "its-bases" not אֲדֹנָי "Adonai") ✓

---

## 18. Flagged for Ben's attention

### A. Exod 34:6–7 Sinai formula DRIFT from corpus-doc — **DECIDE before tagging** (§2)
Retroactively normalize Exod 34:6–7 to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md`. **Critical before any downstream OT-formula recitation ships** (Num 14:18, Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18). Also recommend writing the `check_phrase_consistency.py` extension per the doc's Implementation Checklist §3 item 2.

### B. Exod 33:19 חַנֹּתִי + רִחַמְתִּי verbal-form mapping — **DECIDE before tagging** (§3)
Normalize 33:19 in tandem with §A's 34:6 normalization. Together restores the lemma-mapping at חנן + רחם across the theophanic-cluster (33:19 + 34:6).

### C. Exod 15:11 בָּאֵלִם "among the gods" register — **DECIDE before tagging** (§14)
Confirm Ben endorses the Hebrew-faithful **ในหมู่พระทั้งหลาย** or the Thai-evangelical-paraphrased **เทพเจ้าใดเหมือนพระองค์**. Recommend writing `ot_polytheistic_register_2026-05.md` either way.

### D. מַלְאַךְ YHWH multi-rendering — **REVIEW** (§9)
Recommend (a) normalize to ทูตสวรรค์ throughout + (c) write `malak_yhwh_2026-05.md`. Compounds across Genesis (Hagar, Sodom, Akedah, Mahanaim) + Numbers (Balaam) + Judges + Samuel + Kings + Zechariah + Daniel.

### E. כַּפֹּרֶת drift at 40:20 — **REVIEW** (§10)
Recommend normalize 40:20 to พระที่นั่งกรุณา to match chs.25/30/37; write `kapporet_atonement_cover_2026-05.md`.

### F. YHWH-Nissi 17:15 paraphrase vs. divine_names_table — **REVIEW** (§11)
Recommend doc-amend the table to add a YHWH-paraphrastic-self-title sub-category covering Exod 15:26 + 17:15 + 31:13.

### G. פָּנִים at Exod 33:14-15 vs. doc — **REVIEW** (§12)
Normalize per `hebrew_idioms_and_metaphor_2026-05.md` to พระพักตร์ uniformly across 33:11+14+15+20+23.

### H. Exod 3:14 punctuation drift — **REVIEW** (§13)
Mechanical fix: remove stray closing-quote at 3:14b.

### I. Pharaoh-heart-hardening pattern — **STABLE** (recommend doc-lift) (§4)
Write `pharaoh_heart_hardening_2026-05.md` naming the three-Hebrew-roots-to-single-Thai principle; cross-references the Pauline elections + Johannine Isaiah-citation NT trajectory.

### J. Decalogue locks — **STABLE** (recommend doc-lift) (§5)
Write `decalogue_thai_lock_2026-05.md` naming the canonical Thai for the 10 prohibitions + the Exod-20-vs-Deut-5 variant rationales for the Sabbath + 10th commandment.

### K. 12:40 LXX/SP-vs-MT variant — **STABLE** (recommend Layer-2 footer) (§6)
Add `mt_vs_lxx_textual_variant_handling`-compliant Layer-2 entry to `output/textual_variants/exodus_12.json` naming the LXX/SP "in-Egypt-and-Canaan" reading + the Gal 3:17 NT cross-reference.

---

## External AI review (§3 of checklist)

Suggested 5-cluster packet — one cluster per major editorial-decision area:

1. **Sinai-formula cluster** — §2 + §3 (Exod 33:19 + 34:6–7 vs. corpus-doc)
2. **OT polytheistic-register cluster** — §14 (Exod 15:11)
3. **Angel + divine-name multi-rendering cluster** — §9 + §11 (mal'akh-yhwh; YHWH-Nissi)
4. **Tabernacle vocabulary cluster** — §10 (kapporet); also touches the מִשְׁכָּן / אֹהֶל מוֹעֵד / סְפַר synonymy
5. **Anthropomorphism + face/presence cluster** — §12 (Exod 33:14-15)

Sized for ~20K-char free-tier AI ceilings per `scripts/build_external_review_packet.py`.

---

## Counts per status code (TL;DR)

- **LOCKED:** 13 items (§1, §5, §6, §7, §8, §15a-l)
- **STABLE:** 4 items (§4, §6-12:40-LXX, §17, §8-stiff-necked-cross-NT-followup)
- **REVIEW:** 5 items (§9 malak; §10 kapporet; §11 YHWH-Nissi; §12 panim-33; §13 Ehyeh-punctuation)
- **DECIDE:** 3 items (§2 Sinai-formula CRITICAL; §3 33:19 verbal-form; §14 בָּאֵלִם)

**3 DECIDE items block the `book-exodus-v1` tag.**

**5 new translator_decisions docs recommended** (pharaoh_heart_hardening, decalogue_thai_lock, malak_yhwh, ot_polytheistic_register, kapporet_atonement_cover).

**2 existing translator_decisions docs to amend** (divine_names_table for YHWH-paraphrastic-self-titles; exod_34_attribute_formula for the check-script extension).
