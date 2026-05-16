# Deuteronomy — End-of-Book Review

**Date:** 2026-05-16
**Scope:** All 34 chapters of Deuteronomy (~959 verses); `glossary.json`; existing `docs/translator_decisions/` (84 docs incl. the OT-corpus additions through `ot_warfare_ethics_2026-05.md`, `sacrificial_vocabulary_2026-05.md`, `goel_kinsman_redeemer_2026-05.md`, `i_am_yhwh_holiness_formula_2026-05.md`).
**Trigger:** DEU 34 shipped (commit `2f24b50`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Sixth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers) and the **fourth Pentateuch book — completing the Torah**. DEU is the most-NT-quoted OT book (Jesus' three Matt-4 temptation responses + DEU 6:5 Shema as "greatest commandment" + DEU 18:15 prophet-like-Moses + Paul's Romans citations + the entire Hebrews 10:30 / 12:29 cluster). It is also the **third recitation of the Sinai-attribute-formula** after EXO 34 and NUM 14:18 — a direct downstream test of the two outstanding DECIDE items from those audits.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **20 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 34/34 chapters have green per-chapter reports + back-translations + textual_variants files; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the 294-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `git status output/` clean. The divine_names script reports 1 [C-soft] false-positive on DEU 23:16 (אֲדֹנָיו = "his master" of a human slave-master, not divine Adonai); zero hard fails.
- **Deuteronomy exercises every OT-corpus lock landed by the 2026-05-15 LEV audit** and is the FIRST downstream OT-book test of (a) the **Sinai attribute-formula** in a Decalogue-context (DEU 5:9-10 is the THIRD OT recitation after Exod 34:6-7 and Num 14:18 — and the first to embed the formula directly in the second-Decalogue paqad-clause); (b) **`ot_warfare_ethics_2026-05.md`** (DEU is THE ḥerem book — 2:34, 3:6, 7:2+16+26, 13:16-18, 20:17, 25:17-19 — far more dense than NUM); (c) **`i_am_yhwh_holiness_formula_2026-05.md`** at DEU 5:6 + 32:39; (d) **`hebrew_oath_formulas_2026-05.md`** under the DEU 6:13 / Matt 5:33-37 NT-tension. mal'akh-YHWH has zero DEU occurrences (sustained Mosaic-speech book).
- **Data integrity nearly clean.** Hebrew word-spacing correct in all 34 chapters; `thai_literal` is Thai in all chapters EXCEPT **DEU 15:19** which contains the English token "**YHWH**" instead of "พระยาห์เวห์" in the literal field — single instance, surface `thai` field is correct (§20).
- **17 inherited locks verified compliant** in DEU across the divine-name family, OT-register policy, Hebrew-grammar-transfer, Hebrew-idioms, verse-schema, proper-names (with 2 within-DEU drifts), proper-noun-wordplay, chesed-corpus-doc, paqad-corpus-doc, hebrew-oath, divine-anthropomorphism, mt_vs_lxx-textual-variant-handling, divine-object-praise, narrator-vs-character-voice, leitwort, pagan_deities, ot_polytheistic_register. **N/A for DEU:** mal'akh_yhwh (no occurrences); kapporet (no occurrences); kareth_penalty (no occurrences); manah.
- **6 Deuteronomy-distinctive patterns are STABLE-and-locked** at corpus level (the Shema 6:4-9 + 11:13-21 + the love-formula recitations; the Decalogue-with-DEU-variations 5:6-21; the twelve-curse chant 27:14-26; the covenant-curse cluster 28:15-68; the Song of Moses 32 with rich Layer-2 footers including the 32:8 sons-of-God text-critical decision; the Blessing of Moses 33; the postmosaic coda 34).
- **3 items flagged STABLE-but-undocumented** (recommend new corpus docs): the **Shema canonical six-element form** (6:4-9 is THE most-recited OT-corpus text after Aaronic Blessing — needs a corpus-doc lock alongside the recommended `aaronic_blessing_2026-05.md` from NUM-audit §5); the **centralization-of-worship name-theology formula** ("สถานที่ซึ่งองค์พระผู้เป็นเจ้า...จะทรงเลือก เพื่อตั้งเป็นที่พำนักของพระนามของพระองค์", 6× in DEU 12; forward-protects 1 Kgs 8 + Solomon's temple-dedication); the **DEU-quoted-by-Jesus cluster** (DEU 6:13, 6:16, 8:3 — Matt 4 temptation; reader will encounter Thai surface in OT before NT).
- **5 items flagged REVIEW** (defensible-but-worth-Ben's confirmation): the **two within-DEU place-name drifts** (Pisgah พิสกาห์/ปิสกาห์ at ch.34 vs chs.3-4 — §6a; Seven-Nations ethnonym + prefix drift between DEU 7:1 and 20:17 — §6b); the **Adonai-in-prayer-context vocative at DEU 3:24 + 9:26** (same outstanding REVIEW from NUM 14:17); the **ḥerem 5-way Thai-surface drift within DEU** despite a single rich Layer-2 doctrinal footer at DEU 20:17 (§7); the **DEU 15:19 thai_literal English-token leakage** (single-word mechanical fix — §20).
- **4 items flagged DECIDE** (Ben choice needed before tagging `book-deuteronomy-v1`):
  - **DEU 5:9-10 Sinai-formula recitation DRIFT from `exod_34_attribute_formula_2026-05.md`** — the THIRD OT recitation of the formula drifts in the same component-by-component way as Exod 34:6-7 and Num 14:18. See §2. **CRITICAL.**
  - **Decalogue parallel-text drift between EXO 20 and DEU 5** — syntactic and lexical surface drift between two parallel passages where the Hebrew is identical (esp. גָּנַב 8th commandment: ลักทรัพย์ EXO / ขโมย DEU; and prohibitive "อย่า" EXO / "เจ้าจะต้องไม่" DEU throughout). See §3.
  - **NT-cross-corpus DEU-quote drift cluster** — DEU 18:15 prophet (ผู้พยากรณ์ OT / ผู้เผยพระวจนะ NT), DEU 25:4 muzzle-ox (three different Thai forms across DEU + 1Cor + 1Tim), DEU 32:21 jealousy (หึง OT / ริษยา NT), DEU 6:5 nephesh-as-psyche (สุดจิตวิญญาณ OT vs สุดจิต/สุดจิตวิญญาณ NT mix), DEU 6:13/6:16/8:3 Matt-4-temptation lexical drift. See §17. **HIGH severity** — DEU is the most-quoted OT book in NT.
  - **DEU 32:43 LXX/Heb 1:6 expansion handling** — currently the MT shorter form ships with a Layer-2 footer naming the Heb 1:6 LXX quote. Worth confirming the chosen text-critical disposition before tag. See §10.
- **External AI review (§3) pending.** Suggested 6-item packet (§2/§3/§17/§7 DECIDE items + §6 REVIEW items).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + Deuteronomy first-occurrence footnote — **LOCKED**

**550 YHWH occurrences across all 34 chapters** (every chapter contains YHWH — DEU is the OT-corpus's third-densest YHWH book after Numbers and the Psalter). Layer-2 first-occurrence footers present at all 34 `output/textual_variants/deuteronomy_NN.json` files; reference the `divine_names_table_2026-05.md` doc and identify the verses-of-occurrence within each chapter.

All 550 occurrences render as **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` ✓. No drift of the Tetragrammaton itself. Corpus-total YHWH count after DEU: ~1,470+ occurrences across 294 chapters, all uniformly rendered.

**Footnote-template wording.** DEU **adopted the post-NUM-14 shorter chapter-footer template** (omits the "ยาห์เวห์ Yahweh" romanization phrase as the going-forward standard); 23 of 34 DEU chapters use the bare short template; 11 chapters (4, 6, 10, 24, 28, 29, 31, 32, 34) retain the older "ยาห์เวห์" Thai marker. The post-NUM `check_divine_names.py` pattern-set must already recognize both forms (the script's `check_reports/divine_names.md` shows 0 DEU [D] warnings) — confirming the NUM-audit §3 resolution landed. **LOCKED.**

---

## 2. DEU 5:9-10 Sinai attribute-formula recitation — **DECIDE before tagging (CRITICAL — third downstream DRIFT)**

**The single most consequential finding of this audit.** DEU 5:9-10 is the **Decalogue-embedded** form of the Sinai attribute-formula — the same paqad-clause + chesed-clause that recur from Exod 34:6-7 (→ NUM 14:18). This is the THIRD OT occurrence of the formula and the FIRST in a Decalogue context. The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` does NOT yet name DEU 5:9-10 in its locked-recitations list, but the cross-corpus principle is identical to NUM 14:18: each formula-component must land at the doc-canonical Thai surface to preserve the recitation-thread.

> **5:9 Hebrew:** ...אֵל קַנָּא פֹּקֵד עֲוֺן אָבוֹת עַל־בָּנִים וְעַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים לְשֹׂנְאָי
>
> **5:9 Thai (as shipped):** เพราะเรา องค์พระผู้เป็นเจ้าพระเจ้าของเจ้า เป็นพระเจ้าผู้ทรงหวงแหน **ผู้ลงโทษ**ความผิดของบิดา**บน**บุตรถึงสามและสี่ชั่วอายุของผู้เกลียดเรา
>
> **5:10 Hebrew:** וְעֹשֶׂה חֶסֶד לַאֲלָפִים לְאֹהֲבַי וּלְשֹׁמְרֵי מִצְוֺתָי
>
> **5:10 Thai (as shipped):** แต่**ทรงสำแดง**ความรักมั่นคงต่อ**หนึ่งพัน**ชั่วอายุของผู้ที่รักเราและรักษาบัญญัติของเรา

Component-by-component drift table (comparing DEU 5:9-10 to doc-canonical Thai locked in `exod_34_attribute_formula_2026-05.md`):

| Hebrew (DEU 5:9-10) | Doc-locked Thai | DEU 5:9-10 as shipped | Drift? |
|---|---|---|---|
| פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **ผู้ลงโทษความผิดของบิดาบนบุตร** | ✗ ทรง- prefix dropped (divine-volitional register slip); ความชั่ว doc → ความผิด actual; บรรพบุรุษ doc → บิดา actual; "ต่อ" doc → "บน" actual; missing หลานเหลน |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **ถึงสามและสี่ชั่วอายุ** | partial drift (acceptable variant) |
| וְעֹשֶׂה חֶסֶד לַאֲלָפִים | **และทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ** (doc-canonical Decalogue form) | **ทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ** | ✓ (matches; minor — doc-canonical "พัน" without classifier "หนึ่ง", but acceptable) |

**The cross-corpus tangle.** The same Decalogue text appears at three places — EXO 20:5, DEU 5:9, and the formula proper at EXO 34:7 + NUM 14:18 — and each has different Thai. Comparing:

- **EXO 20:5 Thai:** "ลงโทษความบาปของบิดาที่ผ่านไปยังบุตรชั่วอายุที่สามและที่สี่ของผู้ที่เกลียดชังเรา"
- **DEU 5:9 Thai (this audit):** "ผู้ลงโทษความผิดของบิดาบนบุตรถึงสามและสี่ชั่วอายุของผู้เกลียดเรา"
- **NUM 14:18 Thai (NUM-audit §2):** "ทรงให้ความผิดของบิดาตกถึงบุตรหลานจนถึงสามและสี่ชั่วอายุ"
- **EXO 34:7 Thai (EXO-audit Item A):** various component drifts
- **Doc-canonical Thai:** "ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน"

**Five different Thai surfaces for the same paqad-clause across the OT corpus.** This is the most concentrated single-clause cross-corpus drift in the OT-pilot to date.

**Editorial assessment.** This is the **third-major instance of the same Sinai-formula drift** Ben encountered in the Exodus + Numbers audits. The pattern is identical: each formula-component is rendered with its own Thai vocabulary, drawing on the verse's local sense rather than the locked-corpus form. Because DEU 5 is the Decalogue + DEU 5:9 is one of the **most-known OT verses** (it's how Westerners learned "the sins of the fathers visited unto the third and fourth generation"), the drift here is high-visibility. Forward-compounding: every Decalogue-recitation in liturgy + every formula-echo in Pss + the Prophets + the Mishnah-quoted form all break the cross-corpus thread.

**This audit lands in the SAME ship-window as the EXO 34 + NUM 14:18 decisions.** Whatever resolution Ben chooses must apply identically to DEU 5:9-10. If EXO 34 + NUM 14:18 are normalized to the doc but DEU 5:9-10 is left as-is, the Decalogue context — arguably the formula's primary OT setting — breaks the thread.

**Forward-compounding (the rest of the formula recitations across the OT corpus):** Ps 86:15, 103:8, 145:8 ship with Psalms; Joel 2:13, Nah 1:3, Mic 7:18 ship with the Twelve; Neh 9:17, 2 Chr 30:9 ship with the Histories. Each downstream recitation will diverge ad-hoc unless the corpus-doc Thai is locked and applied retroactively to the four Pentateuchal anchors.

**DECIDE before tagging — recommend retroactive normalization in tandem with EXO 34 + NUM 14:18 normalization.** Three paths:

**(a) Strict normalization in tandem with EXO 34 + NUM 14:18** — re-render DEU 5:9-10 to match the doc's canonical Thai (including the dropped ทรง- prefix at "ลงโทษ"). The verse-level surgical edit is straightforward. Strongest cross-corpus protection; preserves the doc-lock at its Decalogue-context primary OT setting.

**(b) Doc-revision in tandem** — if Ben endorses the as-shipped surfaces collectively, the doc must be amended and Exod 34:6-7 + Num 14:18 + DEU 5:9-10 amended in lockstep. Cost: doc + 3 verse rewrites + the Jonah 4:2 retroactive de-normalization. NOT recommended (re-opens the 2026-05-09 cross-AI consensus).

**(c) Leave as-is, accept doc-divergence across all three Pentateuchal anchors** — worst path; breaks cross-corpus traceability and amounts to abandoning the doc.

**Recommend (a).** This is now the **third direct downstream test** of the Exodus-audit decision. If Ben chooses (a) for Exodus, the same edit is required at NUM 14:18 + DEU 5:9-10. **Severity: CRITICAL** — paired with the EXO 34 + NUM 14:18 findings.

**Followup:** the doc's Implementation Checklist (§3 item 2 in `exod_34_attribute_formula_2026-05.md`) calls for `check_phrase_consistency.py` extension to HARD FAIL when 3+ formula-components co-occur. DEU 5:9-10 is one of the verses the extension would catch.

---

## 3. Decalogue parallel-text drift EXO 20 vs DEU 5 — **DECIDE before tagging**

The two Decalogues (Exod 20:2-17 and DEU 5:6-21) are word-identical in MT for the majority of the prohibitives — yet the Thai surface drifts systematically. Sample drifts:

| Cmd | EXO 20 (Hebrew identical) | DEU 5 (Hebrew identical) | Drift |
|---|---|---|---|
| Slave-house formula | "เรือนทาส" (20:2) | "บ้านแห่งความเป็นทาส" (5:6) | ✗ different idiom |
| Prohibitive frame | "อย่า + verb" throughout | "เจ้าจะต้องไม่ + verb" throughout | ✗ syntactic register |
| 6th (לֹא תִּרְצָח) | "อย่าฆ่าคน" (20:13) | "เจ้าจะต้องไม่ฆ่าคน" (5:17) | ✗ syntax only |
| 7th (לֹא תִּנְאָף) | "อย่าล่วงประเวณี" (20:14) | "เจ้าจะต้องไม่ล่วงประเวณี" (5:18) | ✗ syntax only |
| **8th (לֹא תִּגְנֹב)** | "อย่า**ลักทรัพย์**" (20:15) | "เจ้าจะต้องไม่**ขโมย**" (5:19) | ✗ **different verb lemma** for גָּנַב |
| 9th (לֹא תַעֲנֶה) | "อย่าเป็นพยานเท็จ" | "เจ้าจะต้องไม่เป็นพยานเท็จ" | ✗ syntax |
| 10th (לֹא תַחְמֹד) | order: house→wife→servants (20:17) | order: **wife→house+field**→servants (5:21) | ✓ correctly preserves Hebrew DEU reorder |
| 5th honor-parents | "เพื่อวันของเจ้าจะ**ยาวนาน**" (20:12) | "เพื่อวันของเจ้าจะ**ยืนยาว**" (5:16) | ✗ Hebrew יַאֲרִכוּן = יַאֲרִכֻן same lemma |
| Sabbath rationale | creation (20:11) | exodus (5:15) | ✓ correctly preserves Hebrew divergence |

**The Hebrew-text variations** (Sabbath-rationale, coveting-order, the DEU "well-with-you" expansion at 5:16 v 20:12) **are correctly preserved**. But the **Thai surface for the syntactically-parallel commands diverges between EXO 20 and DEU 5** in a way the Hebrew does not justify. Most commands are word-identical in MT yet rendered with different Thai verbs ("อย่า"/"เจ้าจะต้องไม่") and different lemma-mappings (most concretely, גָּנַב 8th commandment: ลักทรัพย์ EXO / ขโมย DEU).

**Cross-corpus compound:** the NT Decalogue-quotations land further apart still. Rom 13:9 + Matt 19:18 + Mark 10:19 + Luke 18:20 + Jas 2:11 each quote subsets of the Decalogue; the Thai surface there will be third-and-fourth forms.

**Editorial assessment.** The principled position is: where the **Hebrew is identical, the Thai should be identical**. EXO 20 // DEU 5 is the canonical parallel-text exercise in the OT corpus. The DEU 5 shipped form should match EXO 20's "อย่า + verb" syntactic frame and the EXO 20 "ลักทรัพย์" 8th-commandment lemma (or the doc could decide for the reverse normalization).

**Three resolution paths:**

(a) **Normalize DEU 5 to EXO 20 surface** — change DEU 5:17, 5:18, 5:19, 5:20, 5:21 to EXO 20 syntactic frame; change ขโมย → ลักทรัพย์; change ยืนยาว → ยาวนาน at 5:16; change บ้านแห่งความเป็นทาส → เรือนทาส at 5:6. Cost: ~5-8 surgical verse-edits.

(b) **Normalize EXO 20 to DEU 5 surface** — symmetric edit but in EXO. Cost: same; less defensible since EXO is older corpus.

(c) **Lock the principle in a corpus-doc + normalize both to a third canonical form** — write `decalogue_parallel_text_2026-05.md` that locks Thai for the Ten Commandments + the NT cross-quotations. Cost: doc + ~10 verse-edits; strongest forward-protection.

**Recommend (c).** This is the cleanest forward-protection. The doc would also lock the EXO 20 / DEU 5 / NT-citation form for **all five distinct OT-corpus Decalogue-citations** (EXO 20, DEU 5, Lev 19's holiness-code echoes, Hos 4:2 catalog, Jer 7:9 catalog) + the **eight distinct NT-corpus citations** (Matt 5:21+27, Matt 19:18-19 // Mark 10:19 // Luke 18:20, Rom 7:7, Rom 13:9, Eph 6:2-3, Jas 2:11). **Severity: HIGH** — Decalogue is the most-quoted OT-corpus text after the Shema. **DECIDE before tagging.**

---

## 4. Shema (DEU 6:4-9 + 11:13-21) — **STABLE-with-internal-nephesh-drift-flag (recommend corpus-doc)**

**DEU 6:4-9 (primary Shema):**

> **6:4** จงฟังเถิด โอ อิสราเอล: องค์พระผู้เป็นเจ้าพระเจ้าของเรา องค์พระผู้เป็นเจ้าทรงเป็นหนึ่ง
> **6:5** และเจ้าจะรักองค์พระผู้เป็นเจ้าพระเจ้าของเจ้าด้วยสุดใจ สุด**จิตวิญญาณ** และสุดกำลังของเจ้า
> **6:6-9** [pedagogy formula sit-walk-lie-rise; tefillin "เครื่องเตือนใจบนมือ / มัดไว้บนหน้าผาก"; mezuzah "เขียนสิ่งเหล่านี้บนวงกบประตูบ้านของเจ้า"] ✓ all preserved literally

**DEU 11:13-21 (secondary Shema):**

> **11:13** [you shall love YHWH] ด้วยสุดใจของพวกเจ้าและด้วยสุด**จิต**ของพวกเจ้า

**Within-DEU DRIFT.** DEU 6:5 uses "สุดจิตวิญญาณ" while DEU 11:13 uses "สุดจิต" — same Hebrew נֶפֶשׁ rendered two ways in two Shema passages 5 chapters apart. (DEU 11:13 also omits the third clause "สุดกำลัง" — though the Hebrew of 11:13 omits מאד, so this is principled to the source.)

**NT cross-corpus consistency on Shema love-formula** (ψυχή for נֶפֶשׁ):

| Verse | Thai surface |
|---|---|
| DEU 6:5 | สุดใจ / สุด**จิตวิญญาณ** / สุดกำลัง |
| DEU 11:13 | สุดใจ / สุด**จิต** |
| Mark 12:30 | สุดใจ / สุด**จิต** / สุดความคิด / สุดกำลัง (4 clauses) |
| Matt 22:37 | สุดใจ / สุด**จิต** / สุดความคิด (3 clauses) |
| Luke 10:27 | สุดใจ / สุด**จิตวิญญาณ** / สุดกำลัง / สุดความคิด (4 clauses) |

**Pattern.** The נֶפֶשׁ/ψυχή lemma renders as **สุดจิตวิญญาณ** in DEU 6:5 + Luke 10:27, but **สุดจิต** in Mark 12:30 + Matt 22:37 + DEU 11:13. **Cross-corpus DRIFT in nephesh/psyche surface** — folded into §17 below.

**Editorial assessment.** The DEU 6:4-9 surface itself is faithful and the doc-canonical form for the Shema. The DEU 11:13 internal drift (สุดจิต) is the more visible problem within DEU; cross-corpus the nephesh→ψυχή→Thai thread is the bigger problem.

**STABLE** ✓ for 6:4-9; **REVIEW for 11:13 internal drift; DECIDE under §17 for the cross-corpus nephesh-thread.**

**Recommend new doc:** `docs/translator_decisions/shema_canonical_six_element_2026-05.md` — locks (a) the 6:4-5 six-element form ("จงฟัง / องค์พระผู้เป็นเจ้า / พระเจ้าของเรา / องค์พระผู้เป็นเจ้า / หนึ่ง / และเจ้าจะรัก ... สุดใจ สุดจิตวิญญาณ และสุดกำลัง"), (b) the Decalogue-style EXO 20 // DEU 5 parallel-text principle applied to the second-Shema 11:13 (same Thai when Hebrew is identical), and (c) the cross-corpus NT-quotation Thai-lock for the nephesh/ψυχή lemma. Pair with the NUM-audit-recommended `aaronic_blessing_2026-05.md`; together these two docs would lock the two most-recited Hebrew Bible liturgical texts in Jewish + Christian usage. **NEW.**

---

## 5. DEU 12 centralization-of-worship name-theology — **STABLE (recommend corpus-doc)**

The "place where YHWH will choose" formula appears 6 times in DEU 12 (vv. 5, 11, 14, 18, 21, 26) + recurs at 14:23-25, 15:20, 16:2-16, 17:8-10, 18:6, 26:2, 31:11. The Thai form is uniform:

> **สถานที่ซึ่งองค์พระผู้เป็นเจ้า ... จะทรงเลือก เพื่อตั้งเป็นที่พำนักของพระนามของพระองค์**

This preserves the שָׁכַן שְׁמוֹ "place his name" Hebrew Deuteronomic name-theology — forward-protects to 1 Kgs 8:29 (Solomon's temple-dedication: "my name shall be there"), 2 Kgs 23:27, Jer 7:11-12 (Shiloh), and the NT-corpus "name of Jesus" cluster (John 17:6, 11, 12, 26; Phil 2:9-10; Acts 4:12).

**Editorial assessment.** The Deuteronomic name-theology is the **single most-influential OT-corpus theological formula** for the Solomonic temple, Josiah's reform, the Deuteronomic-history evaluation framework, and the NT's "name of YHWH/Jesus" cluster. Uniform Thai surface across 14 DEU occurrences is a corpus-wide achievement.

**STABLE** ✓. **Recommend new doc:** `docs/translator_decisions/deuteronomic_name_theology_2026-05.md` — locks the "สถานที่ซึ่ง...จะทรงเลือก เพื่อตั้งเป็นที่พำนักของพระนามของพระองค์" Thai form and names the forward-protection to 1 Kgs 8 + the NT "name of Jesus" cluster. **NEW.**

---

## 6. Place-name within-DEU drifts — **REVIEW**

Two within-DEU place-name drifts (both mechanical fixes):

### 6a. Pisgah פִּסְגָּה — **REVIEW**

| Verse | Thai |
|---|---|
| 3:17 | พิสกาห์ |
| 3:27 | พิสกาห์ |
| 4:49 | พิสกาห์ |
| **34:1** | **ปิสกาห์** |

The same Hebrew פִּסְגָּה renders four different times in DEU with one drift at the final chapter (single-character drop: **พ → ป** at the head). The NUM-audit §6 noted the parallel Sinai = ซีนาย/สีนาย within-NUM drift; this is the same class of within-book drift. Cost: 1 surgical edit at DEU 34:1. **Severity: LOW.**

### 6b. Seven-Nations ethnonym + prefix drift between DEU 7:1 and 20:17 — **REVIEW**

| Position | DEU 7:1 (7-nation list) | DEU 20:17 (6-nation list) |
|---|---|---|
| Prefix | **ชาว**ฮิตไทต์ / ชาวเกอร์กาชี / ชาวอาโมไรต์ / ชาวคานาอัน / **ชาวเปริซซี** / **ชาวฮีไว** / **ชาวเยบุส** | **คน**ฮิตไทต์ / [no Girgashites] / คนอาโมไรต์ / คนคานาอัน / **คนเปริสซีต** / **คนฮีไวต์** / **คนเยบุสีต** |

**The drifts.** (1) Prefix "ชาว" (7:1) vs "คน" (20:17); (2) ethnonym spelling: เปริซซี/เปริสซีต, ฮีไว/ฮีไวต์, เยบุส/เยบุสีต. Both passages use the same Hebrew lemma set (פְּרִזִּי, חִוִּי, יְבוּסִי). The lengths differ in 20:17 by omission of Girgashites — but that is principled to the source.

**Editorial assessment.** The 7:1 form (ชาว- prefix; bare ethnonym) is the more frequent corpus form (matches NUM + JOS forward-quotation likelihood). DEU 20:17's drift introduces a -ต suffix on three of the six names (the Hebrew is the bare lemma; the -ต suffix appears to be a Thai-language plural-marker that the rest of the corpus does not apply). Cost: ~6 surgical edits at DEU 20:17. **Severity: MEDIUM** — direct proper-name lock-violation within the same book.

**Recommend:** normalize DEU 20:17 to match DEU 7:1's surface for the six shared ethnonyms. **Glossary-entry recommendation:** lock these seven ethnonyms in `glossary.json` (currently absent — the glossary covers most proper nouns but not the seven-nations cluster).

---

## 7. Ḥerem חרם / OT warfare ethics — **DECIDE (recommend corpus-doc-lift + Thai-surface lock)**

DEU is THE ḥerem book. **Five distinct Thai surface forms** for the same Hebrew lemma חרם across DEU:

| Verse | Hebrew form | Thai surface |
|---|---|---|
| 2:34 | וַנַּחֲרֵם | "(เรา)ถวายเฮเรม" — transliterated |
| 3:6 | וַנַּחֲרֵם | "ถวายเฮเรม" — transliterated |
| 7:2 | הַחֲרֵם תַּחֲרִים | "ถวายเฮเรม … ทำลายอย่างสิ้นเชิง" — translit + gloss |
| 7:26 | חֵרֶם | "แยกถวายเฉพาะเพื่อการทำลาย" |
| 13:16 | הַחֲרֵם | "ทุ่มถวายเพื่อทำลายอย่างสมบูรณ์" |
| 13:18 | חֵרֶם | "สิ่งที่ทุ่มถวาย" |
| 20:17 | הַחֲרֵם תַּחֲרִימֵם | "ทุ่มถวายพวกเขาเพื่อทำลายอย่างสมบูรณ์" |
| 25:17-19 (Amalek erasure) | מָחֹה תִּמְחֶה אֶת־זֵכֶר עֲמָלֵק | "ลบความทรงจำของอามาเลค" — no ḥerem-verb |

**Layer-2 doctrinal footers:**
- **DEU 20:17 has a single rich Layer-2 doctrinal footer** in `output/textual_variants/deuteronomy_20.json` — names the ot_warfare_ethics interpretive frame, Canaan-judgment-historicism, Rahab/Gibeonites exceptions, Eph 6:12 spiritual-warfare typology, Rev 19-20 final-judgment typology. **Excellent anchor footer.**
- **No ḥerem footers at chs 2-3, 7, 13, 25** despite these being the other major ḥerem cluster locations. The cluster is under-footed; readers will encounter four chs of ḥerem command without doctrinal-frame footer until ch.20.

**Editorial assessment.** The existing `docs/translator_decisions/ot_warfare_ethics_2026-05.md` doc (landed 2026-05 per NUM-audit §17 recommendation) names the historicist-conditioning interpretive frame Ben endorsed. The DEU corpus is the first major downstream test of that doc — and the Thai-surface for חרם itself is NOT locked there. Five forms is too many for a single Hebrew lemma in a single book.

**DECIDE before tagging — three paths:**

**(a) Normalize all DEU ḥerem occurrences to one canonical Thai surface.** Recommend **"ทุ่มถวายเพื่อทำลาย"** (the 13:16, 20:17 form) as canonical — most-frequent + theologically transparent (preserves the "devote/ban" sense without transliteration). Cost: ~5 surgical verse-edits across chs 2-3, 7, 13. Optionally keep the transliterated "เฮเรม" as a parenthetical at the first occurrence (DEU 2:34) with a chapter-footer.

**(b) Keep the five forms, amend `ot_warfare_ethics_2026-05.md` to acknowledge the surface-flexibility.** Defensible — preserves the as-shipped richness; argues that the multiple Thai forms reflect the different functional registers of חרם (volitional "we-devoted" vs categorical "ban" vs gloss). Cost: doc amendment + back-pointer Layer-2 footers in chs 2-3, 7, 13, 25 pointing to the DEU 20:17 anchor footer.

**(c) Leave as-is.** Defensible-but-unprotected — the next ḥerem corpus (Joshua 6-11; 1 Sam 15) will diverge further. NOT recommended.

**Recommend (a) + amend doc to name the canonical Thai surface.** The anchor Layer-2 footer at DEU 20:17 stays; the chs 2-3, 7, 13, 25 receive back-pointer footers. The DEU 25:17-19 Amalek-erasure use of מָחֹה (not חרם) is principled — different Hebrew lemma; the "ลบความทรงจำ" Thai is correct and should remain. **Severity: HIGH** (reader-experience + corpus-protection).

---

## 8. Curses (DEU 27-28) — **LOCKED**

**DEU 27:14-26 twelve-curse chant:** all 12 curses preserved in the uniform locked form **"ผู้ถูกสาปแช่งคือผู้ที่... และให้ประชาชนทั้งหมดกล่าวว่า 'อาเมน!'"**. The ארור→ผู้ถูกสาปแช่ง lock is consistent across all 12. The אָמֵן rendered as "อาเมน!" with exclamation. Liturgically beautiful.

**DEU 28:15-68 covenant curses:** descending curses preserved literally including the explicit siege-cannibalism passages (28:53-57: "เจ้าจะกินผลของท้องของเจ้า เนื้อของบุตรชายและบุตรหญิง..."). No sanitization. Siege-context preserved.

**Cross-corpus:** the DEU 27:26 "Cursed is anyone who does not uphold the words of this law" is quoted by Gal 3:10 — see §17 for the cross-corpus Thai-surface drift on this verse.

**LOCKED** ✓.

---

## 9. Song of Moses (DEU 32) — **LOCKED-with-rich-Layer-2-handling**

Outstanding text-critical handling. All major DEU 32 verses Layer-2-footnoted:

- **32:1-2:** poetic register preserved ("ฟ้าสวรรค์เอ๋ย จงเงี่ยหูฟัง...") ✓
- **32:4:** "ทรงเป็นศิลา" + "พระเจ้าแห่งความสัตย์ซื่อ" ✓
- **32:8-9 sons-of-God textual variant:** Eremos **follows the DSS (4QDeut^j) + LXX reading** ("ตามจำนวนของบุตรของพระเจ้า") rather than MT (בני ישראל). **Layer-2 footer present** with detailed explanation citing 4QDeut^j, MT, LXX, sons-of-God-divine-council theology, and the 1Cor 10:20 NT echo. **Exemplary text-critical decision.**
- **32:17:** "พวกเขาบูชาแก่ผีปีศาจ ไม่ใช่แก่พระเจ้า" — Layer-2 footer cites 1Cor 10:20.
- **32:21:** "เราจะทำให้พวกเขาหึงด้วยผู้ที่ไม่ใช่ชนชาติ" — Layer-2 footer cites Rom 10:19, 11:11, 11:14. (Cross-corpus קנא vs ζῆλος Thai-surface drift — see §17.)
- **32:35:** "การแก้แค้นเป็นของเรา เราจะตอบแทน" — Layer-2 footer cites Rom 12:19, Heb 10:30.
- **32:39:** "เราเป็นพระองค์" — Layer-2 footer cites Jn 8:24/58, Isa 41:4 i_am_yhwh thread.
- **32:43:** **DECIDE flag** — see §10.

**LOCKED** ✓ for all DEU 32 verses except 32:43 — see §10.

---

## 10. DEU 32:43 LXX/Heb 1:6 expansion handling — **DECIDE before tagging**

DEU 32:43 in MT reads roughly: "Rejoice, O nations, with his people, for he avenges the blood of his servants…" — short form.

DEU 32:43 in LXX + 4QDeut^q reads: "Let the heavens rejoice with him, and let all the sons of God / angels of God worship him…" — long form. The "all God's angels worship him" clause is the line **Heb 1:6 quotes** as proof of Christ's superiority over angels.

**Eremos shipped form** (DEU 32:43):

> "ชนชาติทั้งหลายเอ๋ย จงยินดีกับประชาชนของพระองค์... ทรงชำระแผ่นดินและประชาชนของพระองค์"

— **MT shorter form.** Layer-2 footer at `output/textual_variants/deuteronomy_32.json` names the LXX expansion + cites Heb 1:6.

**Editorial assessment.** This is a defensible choice — the corpus's stated text-base is MT/SBLGNT, and the Layer-2 footer transparently signals the divergence. **However**, the related DEU 32:8 verse follows the DSS/LXX reading (sons-of-God), not MT. The two adjacent text-critical decisions in the same chapter diverge in disposition: 32:8 → follows DSS/LXX; 32:43 → follows MT.

**The principled question.** Should Pentateuchal-corpus text-critical decisions consistently favor (a) MT-with-Layer-2-for-LXX-expansions, or (b) DSS/LXX-where-Greek-evidence-is-corroborated-by-DSS? Currently DEU 32 splits — 32:8 path (b), 32:43 path (a). Ben should confirm whether this split is principled or accidental.

**Three resolution paths:**

(a) **Keep current** — MT 32:43 + DSS/LXX 32:8 split is correct because 32:8 has 4QDeut^j Hebrew-witness corroboration while 32:43 has only 4QDeut^q (later). Defensible; needs Layer-2 footer wording-amendment naming the asymmetric-witness rationale.

(b) **Lift 32:43 to LXX form** to match 32:8 — adopt the long form including "let all God's angels worship him" since Heb 1:6 directly quotes it. Layer-2 footer notes the MT shorter form. Stronger NT-quotation continuity.

(c) **Lower 32:8 to MT form** — adopt MT "sons of Israel" with Layer-2 footer noting the DSS/LXX reading. Stronger MT-base consistency. NOT recommended — would lose the 32:8 divine-council theology evidence.

**Recommend (a) with footer wording-amendment.** The asymmetry is defensible because the textual evidence is asymmetric (32:8 has Hebrew witness; 32:43 does not). The Layer-2 footer at DEU 32:43 should be amended to explicitly name this asymmetric-witness rationale so future readers and reviewers see the principle. **Severity: MEDIUM** — text-critical, low reader-impact but high editorial-coherence value. **DECIDE** flag preserved for Ben's confirmation.

---

## 11. Blessing of Moses (DEU 33) — **LOCKED**

- **33:2:** "องค์พระผู้เป็นเจ้าเสด็จมาจาก**ซีนาย**" — matches the EXO/NUM Sinai lock (ซีนาย, not สีนาย) ✓. Theophany-imagery preserved literally ("เสอีร์ … ภูเขาปาราน … ฝูงผู้บริสุทธิ์นับหมื่น พร้อมไฟลุกที่พระหัตถ์ขวา").
- **33:12:** "พระอังสาของพระองค์" — divine anatomical anthropomorphism preserved ✓
- **33:26:** "ผู้ทรงขี่ฟ้าสวรรค์มาช่วยเจ้า … ทรงขี่เมฆในพระสง่าราศี" — "rider of heavens" preserved ✓
- **33:27:** "พระเจ้านิรันดร์ทรงเป็นที่พำนักของเจ้า และข้างใต้คือ**พระกรนิรันดร์**" — "everlasting arms" → "พระกรนิรันดร์" ✓ (preserves the classic OT anthropomorphism + matches `divine_anthropomorphism_thai_grammar_2026-05.md`)
- **33:29:** "ผู้ได้รับการช่วยให้รอดโดยองค์พระผู้เป็นเจ้า … โล่ที่ปกป้องเจ้า ดาบที่เจ้าโอ้อวด" — military-imagery preserved ✓

Tribal blessings render with poetic register. **LOCKED** ✓.

---

## 12. Death of Moses (DEU 34) — **LOCKED-with-rich-Layer-2-handling**

Outstanding Layer-2 footer density at DEU 34:

- **34:1:** Pisgah within-DEU drift — see §6a (ปิสกาห์ vs chs.3-4 พิสกาห์).
- **34:5 "ตามพระดำรัสขององค์พระผู้เป็นเจ้า"** (עַל־פִּי יְהוָה) — Layer-2 footer cites Talmud Bava Batra 17a + Sifre Deut 357 "kiss of God" tradition + the ordinary "by his command" reading. Excellent rabbinic-tradition disclosure.
- **34:6 "พระองค์ทรงฝังท่าน"** (3rd-singular יִקְבֹּר subject-ambiguous, MT לֹא־יָדַע) — Layer-2 footer cites Mishnah Sotah 14a "God buried Moses", LXX plural reading (= angels), Jude 9 / Assumption of Moses tradition. **Outstanding divine-anthropomorphism handling.**
- **34:7 לֵחֹה** hapax — Layer-2 footer naming hapax-legomenon, lexical sense, theological reading.
- **34:9 Joshua-succession** preserved (ויקרא יהוה — "and YHWH appointed Joshua spirit-of-wisdom by laying-on-of-hands of Moses").
- **34:10 "ไม่มีผู้พยากรณ์คนใดในอิสราเอลที่ลุกขึ้นมาเหมือนโมเสส"** + **34:11-12 signs-and-wonders coda** — Layer-2 footers cite Acts 3:22 (prophet-like-Moses), Acts 7:37, Heb 3:1-6, 2Cor 3-4, the Transfiguration, John 4:48 signs-wonders. **Excellent NT-cross-corpus footers.**

**One enhancement noted:** there is no standalone "postmosaic-authorship" Layer-2 footer — the prophetic-coda framing is covered by the prophet-like-Moses footer at 34:10, but a reader-edition would benefit from an explicit Mosaic-authorship Layer-2 note (either at DEU 31:9 — "Moses wrote this law" — or at the head of DEU 34). Not blocking; STABLE.

**LOCKED** ✓ with optional enhancement.

---

## 13. Decalogue 5th commandment honor-parents — **STABLE-with-EXO-drift-flag**

DEU 5:16 vs EXO 20:12 vs Eph 6:2-3 — see §3 above for the parallel-text drift discussion. The DEU 5:16 + Eph 6:2-3 surface match each other ("ยืนยาว") and diverge from EXO 20:12 ("ยาวนาน"). Paul is quoting the DEU 5 expanded form ("เพื่อจะเป็นการดีกับเจ้า"), so this is defensible.

**Folded into §3 Decalogue-DECIDE.** Subordinate. Not a separate item.

---

## 14. Divine names (besides YHWH) — **LOCKED-with-Adonai-in-prayer-flag**

- **Elohim → พระเจ้า**: uniform across DEU ✓
- **El → พระเจ้า**: e.g. DEU 4:31 אֵל רַחוּם → "พระเจ้าผู้ทรงพระเมตตา" ✓
- **El Elyon → องค์ผู้สูงสุด**: DEU 32:8 ✓ matches `divine_names_table_2026-05.md`
- **El Shaddai / Shaddai**: not present in DEU.
- **Adonai:**
  - **DEU 3:24, 9:26** `אֲדֹנָי יְהוִה` → "ข้าแต่องค์พระผู้เป็นเจ้า" — collapses Adonai-YHWH compound into single YHWH-form. Same pattern as **NUM 14:17** (Adonai-vocative-in-prayer-context). **Defensible but doc-divergent.**
  - **DEU 10:17** וַאֲדֹנֵי הָאֲדֹנִים → "**องค์เจ้านายของบรรดาเจ้านาย**" ✓ matches `divine_names_table_2026-05.md` standalone-Adonai lock. Also "אֱלֹהֵי הָאֱלֹהִים" → "**พระเจ้าของบรรดาพระ**" ✓.

**The Adonai-in-prayer flag.** DEU 3:24 + 9:26 are the **second + third instances** of the same Adonai-in-prayer pattern flagged at NUM 14:17 (the NUM-audit recommended doc-amendment to `divine_names_table_2026-05.md` adding a sub-rule). DEU strengthens the case for the doc-amendment: this is now a 3-verse cross-Pentateuch pattern, not a single-verse anomaly.

**Status:** LOCKED for divine_names_table where the lemma is explicit; **REVIEW** for the Adonai-in-prayer sub-rule (folded into the NUM-audit §8 REVIEW — recommend doc-amendment to `divine_names_table_2026-05.md` to lock the principle that **standalone Adonai-as-prayer-vocative-in-YHWH-context renders as "ข้าแต่องค์พระผู้เป็นเจ้า"** distinct from standalone Adonai-as-title rendering "องค์เจ้านาย"). The DEU 3:24 + 9:26 forms become the locking precedent.

---

## 15. Divine-passive / divine-volitional register (ทรง-) — **LOCKED with one register-slip noted**

- **ทรง- prefix** maintained for divine actions throughout (spot-checks at chs 1, 5, 6, 7, 12, 28, 32) ✓
- **One register-slip:** DEU 5:9 "**ผู้ลงโทษ**ความผิด…" — should be "**ทรงลงโทษ**" per OT-register policy for divine-volitional. The ผู้-prefix functions as participle/agentive but loses the ทรง- royal-Thai register. **Folded into §2 Sinai-formula DECIDE — same fix.**
- **Moses-as-prophet narrator-vs-character voice**: Moses speaks in first-person (ข้าพเจ้า) plain register to humans ✓; uses humble ข้าพระองค์ when addressing YHWH (DEU 3:24, 9:26, 26:5-10 etc.) ✓. Consistent with `narrator_vs_character_voice_2026-04.md` and `ot_register_policy_2026-05.md`.

**LOCKED** ✓ (register-slip at 5:9 resolved by §2 fix).

---

## 16. Hebrew oath formulas — **LOCKED**

- DEU 1:34-35: YHWH's oath against wilderness-generation — "พระองค์ทรงพระพิโรธและทรง**ปฏิญาณ**" ✓
- DEU 4:21, 4:26: Moses' oath + heaven-and-earth witnesses ✓
- **DEU 6:13** "וּבִשְׁמוֹ תִּשָּׁבֵעַ" → "**สาบาน**ในพระนามของพระองค์" ✓ — contrasts directly with Matt 5:33-37 in NT where Jesus contradicts: "อย่าสาบานเลย". The cross-corpus OT-mandate / NT-contradiction tension is preserved in Thai surface (สาบาน in both). **Reader-experience consideration:** a Layer-2 footer at DEU 6:13 (or at Matt 5:33-37) flagging the Jesus-contradicts-DEU thread would protect the reader from confusion — but no footer is currently present. Not a DEU-blocking issue; logged here as a forward-flag for the next Sermon-on-the-Mount audit (already done) to consider Matt 5:33-37 footer.
- DEU 8:18, 29:12-14: covenant-oath ("พันธสัญญานี้และคำปฏิญาณนี้") ✓

**LOCKED** ✓ per `hebrew_oath_formulas_2026-05.md`.

---

## 17. NT-cross-corpus DEU-quote drift cluster — **DECIDE before tagging (HIGH severity)**

DEU is **the most-quoted OT book in the NT corpus** (esp. by Jesus in the Matt-4 temptation + Paul in Romans + Hebrews). The cross-corpus Thai-surface drifts are widespread and systematic.

| OT (DEU) | NT echo | Match? | Notes |
|---|---|---|---|
| **6:5 love-formula** | Matt 22:37 / Mark 12:30 / Luke 10:27 | partial | psyche/nephesh DRIFT: DEU + Luke = **สุดจิตวิญญาณ**; Mark + Matt = **สุดจิต**. DEU 11:13 internally uses สุดจิต — see §4. |
| **6:13 fear/serve** | Matt 4:10 | partial | DEU "เกรงกลัว…รับใช้พระองค์เท่านั้น…สาบาน" vs Matt "นมัสการ…ปรนนิบัติพระองค์แต่ผู้เดียว" — defensible (Matt 4:10 quotes LXX προσκυνέω form of יָרֵא); no Layer-2 footer noting the LXX-vs-MT divergence. |
| **6:16 do-not-test** | Matt 4:7 | partial | DEU "อย่า**ทดสอบ**" vs Matt "อย่า**ทดลอง**" — verb-lemma drift on נסה/πειράζω |
| **8:3 bread-alone** | Matt 4:4 | partial | DEU "มนุษย์ไม่ได้**มีชีวิตอยู่**ด้วยขนมปังเพียงอย่างเดียว" vs Matt "มนุษย์มิได้**ดำรงชีวิต**ด้วยขนมปังอย่างเดียว" — verb drift on חיה/ζάω |
| **18:15 prophet-like-Moses** | Acts 3:22 / 7:37 | **MAJOR DRIFT** | DEU "**ผู้พยากรณ์**" vs Acts "**ผู้เผยพระวจนะ**" — cross-corpus DRIFT for נביא/προφήτης. DEU 18:15-22 uses ผู้พยากรณ์ consistently (vv.15, 18, 19, 20, 22), so the drift is OT→NT systemic. **Affects entire OT-prophets vocabulary forward.** |
| **21:23 hung-on-tree-cursed** | Gal 3:13 | partial | DEU "ผู้ใดที่ถูกแขวนบนต้นไม้อยู่ภายใต้คำสาปแช่งของพระเจ้า" vs Gal "ทุกคนที่ถูกแขวนไว้ที่ต้นไม้ ย่อมถูกสาปแช่ง" — partial (the "ของพระเจ้า" qualifier omitted in Gal quotation, matching the Greek text Paul uses). |
| **25:4 muzzle-ox** | 1Cor 9:9 / 1Tim 5:18 | **THREE DIFFERENT THAI FORMS** | DEU "อย่า**ผูกปาก**วัวขณะที่มันกำลังเหยียบนวดข้าว" / 1Cor "อย่าเอา**ผ้าผูกปาก**วัวขณะมันกำลังนวดข้าว" / 1Tim "อย่าเอา**ตะกร้อครอบปาก**วัว" — three different Thai surfaces for the same Greek text Paul quotes twice. **Worst single-verse cross-corpus drift in DEU's NT quotation set.** |
| **27:26 cursed-not-uphold** | Gal 3:10 | partial | DEU "ผู้ถูกสาปแช่งคือผู้ที่ไม่ปฏิบัติตามถ้อยคำของบัญญัตินี้" vs Gal "ทุกคนที่ไม่ได้ยึดมั่นในการประพฤติตามทุกข้อที่เขียนไว้ในหนังสือธรรมบัญญัติย่อมถูกสาปแช่ง" — different syntactic frames (note: Gal quotes the LXX expanded form, so partial-divergence is principled). |
| **30:12-14 word-near-you** | Rom 10:6-8 | partial | DEU "อยู่ใกล้เจ้ามาก อยู่ในปากของเจ้าและใน**ใจ**ของเจ้า" vs Rom "อยู่ใกล้ท่าน — อยู่ในปากของท่านและใน**จิตใจ**ของท่าน" — ใจ vs จิตใจ |
| **32:21 jealousy-by-non-nation** | Rom 10:19 | partial | DEU "เราจะทำให้พวกเขา**หึง**ด้วยผู้ที่ไม่ใช่ชนชาติ" vs Rom "เราจะทำให้พวกเจ้า**ริษยา**โดยผู้ที่ไม่ใช่ชนชาติ" — different verb-lemma for קנא/παραζηλόω (หึง vs ริษยา) |
| **32:35 vengeance-is-mine** | Rom 12:19 / Heb 10:30 | partial | DEU "การแก้แค้นเป็นของเรา เราจะ**ตอบแทน**" / Rom "เราเองจะ**ตอบแทน**" ✓ / Heb 10:30 "เราจะ**ตอบสนอง**" — Heb diverges. |
| **32:43 nations-rejoice-with-people** | Heb 1:6 (LXX form) | text-critical | See §10 — DEU 32:43 ships MT shorter form + Layer-2 footer for the Heb 1:6 LXX expansion. |
| **5:16 honor-parents** | Eph 6:2-3 | partial | DEU 5:16 + Eph 6:2-3 match each other (ยืนยาว) and diverge from EXO 20:12 (ยาวนาน) — see §3. |
| **17:6 / 19:15 two-or-three-witnesses** | Matt 18:16 / 2Cor 13:1 / 1Tim 5:19 | partial | DEU 19:15 "พยานสองหรือสามคน" / Matt + 2Cor "พยานสองหรือสามคน" ✓; DEU 17:6 slightly different form "พยานสองคนหรือสามคน" — minor intra-DEU drift. |

**Pattern.** The most-systemic issues are:

1. **נביא → ผู้พยากรณ์ (OT) vs προφήτης → ผู้เผยพระวจนะ (NT)** — affects every NT quote of DEU 18:15 (Acts 3:22, 7:37, Heb 3:1-6 backdrop) AND **dozens of forward Prophets-corpus occurrences** (Isaiah, Jeremiah, Ezekiel, the Twelve — all currently un-shipped). This is the single biggest forward-protection issue.
2. **נֶפֶשׁ → สุดจิตวิญญาณ (OT poetic) vs ψυχή → สุดจิต (NT majority)** — affects Shema NT quotations + the entire psyche/nephesh anthropological-vocabulary cluster.
3. **קנא → หึง (OT poetry) vs ζῆλος/ζηλόω → ริษยา (NT)** — affects the divine-jealousy + Pauline-jealousy thread.
4. **DEU 25:4 quote** has **three different Thai renderings** across DEU, 1 Cor 9:9, 1 Tim 5:18 — the single most-fragmented OT-quote in the NT corpus.

**Editorial assessment.** The OT-NT cross-quotation Thai-thread is currently broken for the most-quoted OT book. The pattern is: OT-side renders the Hebrew lemma in its own context; NT-side renders the Greek lemma in its own context; the Thai-reader cannot recognize the quotation-relationship across the gap.

**Three resolution paths:**

(a) **Status-quo + accept drift.** Defensible — each side reads with internal-corpus coherence. But the cross-corpus thread is lost; reader experience breaks at every Pauline OT-quote.

(b) **Write a corpus-doc `ot_nt_cross_quotation_thread_2026-05.md`** that locks the OT→NT Thai-thread for the major lemma-pairs (נביא/προφήτης; נֶפֶשׁ/ψυχή; קנא/ζῆλος; the DEU 25:4 cluster). Cost: 1 new doc + ~20-30 surgical verse-edits across DEU + NT-citation verses + the script `check_phrase_consistency.py` extension. Strongest cross-corpus protection.

(c) **Selective normalization for the highest-impact drifts only** — normalize **DEU 18:15 + the entire DEU 18:9-22 prophet-cluster to ผู้เผยพระวจนะ** (matches NT), normalize the DEU 25:4 muzzle-ox surface to match 1 Cor 9:9, leave the others. Cost: ~5-8 surgical verse-edits.

**Recommend (b).** The OT-prophets corpus (Isa-Mal, ~16 books, ~250 chapters) is the largest single forward-cover for the נביא thread. Locking the lemma now — at the DEU 18:15 + Acts 3:22 thread anchor — protects the entire Major + Minor Prophets ship. The doc would also lock the foundational OT-corpus anthropological-vocabulary thread (nephesh, ruach, basar, leb) → NT counterparts (psyche, pneuma, sarx, kardia). **Severity: HIGH** (forward-protection magnitude). **DECIDE before tagging.**

---

## 18. Distinctive DEU vocabulary clusters — **STABLE**

| Cluster | Verses | Thai surface | Status |
|---|---|---|---|
| Levirate marriage | 25:5-10 | "พี่น้องเขย" for יָבָם ✓; "ถอดรองเท้า ถ่มน้ำลายใส่หน้า"; "บ้านของผู้ที่ถูกถอดรองเท้า" preserved as Hebrew etymological name | LOCKED |
| Tithing | 14:22-29, 26:1-15 | "หนึ่งในสิบ" / "สิบลด" — both used (minor intra-DEU drift for מַעֲשֵׂר) | STABLE-with-flag |
| Sabbatical year (shemittah) | 15:1-11 | "การยกเว้นหนี้" for שמטה; "ปีที่เจ็ด ปีแห่งการยกเว้น" ✓ (no Jubilee in DEU — that's LEV 25) | LOCKED |
| Centralization of worship | 12:5-26, 14-26 | "สถานที่ซึ่งองค์พระผู้เป็นเจ้า...จะทรงเลือก เพื่อตั้งเป็นที่พำนักของพระนามของพระองค์" — uniform across 14 occurrences ✓ | LOCKED — see §5 (recommend new corpus-doc) |
| Three pilgrim feasts | 16:1-17 | "เทศกาลปัสกา / เทศกาลขนมปังไร้เชื้อ / เทศกาลสัปดาห์ / เทศกาลอยู่เพิง" ✓ | LOCKED |
| King-law | 17:14-20 | "กษัตริย์" ✓; "ม้วนหนังสือ" for the Torah-copy ✓ | LOCKED |
| Prophet-law | 18:9-22 | "ผู้พยากรณ์" throughout (see §17 NT-drift); divinatory-vocabulary cluster ("ผู้ทำการดูดวง / ผู้ทำคาถา / ผู้ตีความลาง / ผู้ทำเวทมนตร์ / ผู้ร่ายมนตร์ / ผู้ปรึกษากับคนทรงหรือคนนำวิญญาณ / ผู้สอบถามคนตาย") preserved literally | LOCKED-with-§17-flag |
| Witnesses requirement | 17:6, 19:15 | "พยานสองหรือสามคน" ✓ (minor 17:6 drift "สองคนหรือสามคน") | STABLE |
| Cities of refuge | 19:1-13 (parallel to NUM 35) | "เมืองลี้ภัย" ✓ matches NUM lock | LOCKED |
| Asylum-altar / first-fruits liturgy | 26:1-15 | "ขนมปังของบรรพบุรุษ" + the famous "บรรพบุรุษของข้าพระองค์เป็นชาวอาราเมียนผู้กำลังพินาศ" (26:5) | LOCKED |

**STABLE** ✓.

---

## 19. Inherited corpus locks — **all compliant except where flagged**

| Doc | DEU evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | See §1, §14. Tetragrammaton-as-องค์พระผู้เป็นเจ้า uniform (550/550); El → พระเจ้า; Elyon → ผู้สูงสุด at 32:8; Adonai-of-Adonais → องค์เจ้านายของบรรดาเจ้านาย at 10:17. **EXCEPTION: DEU 3:24 + 9:26 Adonai-in-prayer renders YHWH-form (§14, folded into NUM-audit §8 REVIEW).** | **LOCKED-with-§14-flag** |
| `ot_register_policy_2026-05.md` | Moses-as-prophet/narrator with humble ข้าพระองค์ to YHWH; plain register to Israel; YHWH-speech uses ทรง- divine-volitional throughout. **EXCEPTION: DEU 5:9 ผู้ลงโทษ register-slip — folded into §2.** | **LOCKED-with-§2-flag** |
| `chesed_covenant_love_2026-05.md` | DEU 5:10, 7:9, 7:12 — all render ความรักมั่นคง ✓ | **LOCKED** |
| `exod_34_attribute_formula_2026-05.md` | **MAJOR DRIFT at DEU 5:9-10 — see §2.** Cross-corpus traceability is broken at the THIRD downstream witness (Decalogue context). | **DRIFT (DECIDE)** |
| `nicham_divine_relenting_2026-05.md` | DEU has no formal naham occurrences. N/A. | **LOCKED (N/A)** |
| `hebrew_oath_formulas_2026-05.md` | DEU 1:34-35, 4:21+26, 6:13, 8:18, 29:12-14 — see §16. Compliant. | **LOCKED** |
| `paqad_visit_attend_2026-05.md` | DEU 5:9 פֹּקֵד עֲוֹן clause — judgment-paqad form. **DRIFT in surrounding formula-cluster — see §2.** | **LOCKED-with-§2-flag** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Strong hand and outstretched arm" cluster pervasive (DEU 4:34, 5:15, 6:21, 7:8+19, 9:26+29, 11:2, 26:8) — uniform "พระหัตถ์อันทรงฤทธิ์และพระกรที่เหยียดออก" ✓; "everlasting arms" 33:27 → พระกรนิรันดร์ ✓; "face of YHWH" 5:4, 34:10 → พระพักตร์ ✓ | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains pervasive in narrative sections (chs 1-3, 9, 31); cognate-accusatives at DEU 6:17 (שָׁמוֹר תִּשְׁמְרוּן "keeping you shall keep"); imperative-of-prohibition pattern in Decalogue ch.5. Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "land flowing with milk and honey" 6:3, 11:9, 26:9+15, 27:3, 31:20 → uniform "แผ่นดินที่ไหลด้วยน้ำนมและน้ำผึ้ง" ✓; "by the hand of Moses" pattern at 34:9; "fire-from-heaven" theophany 4:11-12+24, 5:22-26, 9:3+10 → uniform "ไฟ" + divine-context "ไฟไหม้" ✓. Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | DEU has the famous **MT-vs-English boundary at 12:32/13:1** (MT 13:1 = English 12:32; the chapter-break shifts). Also at 22:30/23:1, 28:69/29:1, 29:28/29:29 (Masoretic puncta extraordinaria). All Layer-2-footnoted at `output/textual_variants/deuteronomy_{13,23,29}.json`. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | 800+ proper-noun renderings spot-checked: Moses **โมเสส**, Joshua **โยชูวา**, Aaron **อาโรน**, Caleb **คาเลบ**, Sihon **สิโหน**, Og **โอก**, Balaam **บาลาอัม** (recap at 23:4-5), Balak **บาลาค**; place-names Sinai **ซีนาย** at 33:2 ✓, Horeb **โฮเรบ** (9× — DEU-distinctive), Kadesh-Barnea **คาเดชบารเนีย**, Pisgah **พิสกาห์/ปิสกาห์** mixed — see §6a, Nebo **เนโบ**, Mt Gerizim **เกริซิม**, Mt Ebal **เอบาล**, Seven-Nations ethnonyms mixed — see §6b. Mostly consistent, two within-DEU drifts flagged. | **LOCKED-with-§6a/§6b-flag** |
| `proper_noun_wordplay_2026-05.md` | DEU has the **"house-of-the-one-with-shoe-removed"** etymology at 25:10 (preserved literally — "บ้านของผู้ที่ถูกถอดรองเท้า"); **"Massah and Meribah"** recap at 6:16, 9:22, 33:8 (matches EXO/NUM precedent). | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | **MAJOR test:** DEU 32:8 (sons-of-God 4QDeut^j+LXX vs MT) — Layer-2 footer present ✓; DEU 32:43 (LXX expansion + Heb 1:6 quote) — Layer-2 footer present, MT form shipped — see §10 DECIDE; DEU 5:21 (coveting-order MT vs Sam Pent variant) — MT shipped without footer (low-impact). | **LOCKED-with-§10-flag** |
| `manah_divine_appointment_2026-05.md` | DEU has no מָנָה occurrences. N/A. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | "other gods" cluster pervasive (DEU 6:14, 7:4+16, 8:19, 11:16+28, 13:2+6+13, 17:3, 18:20, 28:14+36+64, 29:25, 30:17, 31:18+20) → uniform "พระอื่นๆ" / "พระอื่นใด" ✓; "Baal-Peor" recap at 4:3 → "บาอัลแห่งเปโอร์" ✓. Compliant. | **LOCKED** |
| `ot_polytheistic_register_2026-05.md` | DEU 5:7 (Decalogue first commandment "no other gods"); 32:17 (demons-not-God); 32:21 (a not-people made-them-jealous-by-no-god); 32:43 (LXX form: "all sons of God worship him" — handled in 32:43 Layer-2). All polytheistic-register vocabulary preserves Hebrew lemma-distinctions ✓ | **LOCKED** |
| `ot_warfare_ethics_2026-05.md` | See §7 — DEU is THE downstream test of the doc. Doc landed; DEU has rich Layer-2 anchor footer at 20:17 + 5-way Thai-surface drift across חרם — **DECIDE on doc-amendment + surface-normalization**. | **DRIFT-on-surface (DECIDE)** |
| `i_am_yhwh_holiness_formula_2026-05.md` | DEU 5:6 (אָנֹכִי יהוה אֱלֹהֶיךָ Decalogue-introduction) ✓ matches doc; DEU 32:39 (אֲנִי הוּא "I am he") — Layer-2 footer cites Jn 8:24, 8:58, 13:19; Isa 41:4, 43:10+13 cross-corpus thread. **LOCKED** ✓ — DEU 32:39 is a major i_am_yhwh-thread anchor in the OT corpus. | **LOCKED** |
| `kareth_penalty_formula_2026-05.md` | DEU has no formal kareth/וְנִכְרְתָה occurrences (verified by regex). Covenant-curse vocabulary is the broader 28:15-68 cluster, not the priestly-Levitical kareth form. N/A. | **LOCKED (N/A)** |
| `uncover_nakedness_euphemism_2026-05.md` | DEU 22:30 + 27:20+22+23 (the "uncovering the father's garment" curse-cluster + the Decalogue-coveting context) → preserves "ผ้าคลุมของบิดา" Hebrew literal + Layer-2 footer references levitical סקפ levirate ban. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator: ch.1-4 introduction + ch.27 ritual-cere remote-narrator + ch.31-34 deathbed-narrator; Mosaic-speech occupies most of the book (chs.5-30) with internal narrator-frame at ch.27. Plain-register Moses-to-Israel; humble ข้าพระองค์ Moses-to-YHWH ✓. Compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | DEU 6:5 (Shema love-formula) ✓; DEU 10:12 ("what does YHWH require of you" — fear/walk/love/serve compound) ✓; DEU 32 (the entire Song-of-Moses praise-context) ✓. Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative; Greek-NT-specific. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | N/A — NT-specific. OT-side handled by `mt_vs_lxx_textual_variant_handling_2026-05.md`. | **LOCKED (N/A)** |
| `malak_yhwh_2026-05.md` | **Zero DEU occurrences** (DEU is sustained Mosaic-speech; no divine-messenger narrative). N/A. | **LOCKED (N/A)** |
| `kapporet_atonement_cover_2026-05.md` | **Zero DEU occurrences.** N/A. | **LOCKED (N/A)** |
| `sacrificial_vocabulary_2026-05.md` | DEU is light on Levitical-sacrifice ritual (centralization-of-worship 12 displaces the Levitical detail); but DEU 12:6+11+27, 15:21, 18:1-8 + ch.16 feasts use the doc-canonical vocabulary (เครื่องบูชาเผา burnt-offering, เครื่องบูชามิตรภาพ peace-offering, ทศางค์ tithe, ของถวาย freewill-offering, บุตรหัวปี firstborn). Compliant. | **LOCKED** |
| `goel_kinsman_redeemer_2026-05.md` | DEU 19:6+12 (גָּאֵל הַדָּם blood-avenger in the cities-of-refuge context) → "**ผู้แก้แค้นเลือด**" ✓ matches doc; **DEU 25:5-10 levirate ger** uses יָבָם not גָּאֵל so technically a different lemma — Thai "พี่น้องเขย" preserves the levirate-specific term. Compliant. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | DEU's massive **שמע "hear/listen" leitwort** (DEU 4:1+10+33+36, 5:1+23+24+25+26+27, 6:3+4, 7:12, 8:20, 9:1+23, 10:10, 11:13+27+28, 12:28, 13:1+3+9+12, 15:5+9, 17:12+13, 18:14+15+19, 19:20, 20:3, 21:18+19+20+21, 23:6, 25:8, 26:7+14+17, 27:9+10+14, 28:1+2+13+15+45+62, 29:4+19, 30:2+8+10+12+13+17+20, 31:11+12+13+28, 32:1+44, 33:7) — **210+ occurrences**, the most-concentrated single-lemma leitwort in OT-corpus pilot. Thai uniformly "ฟัง" ✓. Outstanding leitwort handling. | **LOCKED** |
| `shared_names_normalization_2026-05.md` | Tribal-name spellings + ancestor-names (Abraham, Isaac, Jacob — pervasive in chs.1-9 historical-recap) — all match prior-book locks. Compliant. | **LOCKED** |

---

## 20. Mechanical (§1) — **all green except DEU 15:19 thai_literal English-leakage**

- 34/34 chapters: `output/check_reports/deuteronomy_NN_review.md` + sub-reports ✓
- 34/34 chapters: `output/back_translations/deuteronomy_NN.json` ✓
- 34/34 chapters: `output/textual_variants/deuteronomy_NN.json` present (every chapter contains YHWH; matches NUM precedent for YHWH-dense books)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 294-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `python3 scripts/check_divine_names.py`: **1 [C-soft] DEU warning** at DEU 23:16 — false-positive (אֲדֹנָיו = "his master" of a human slave-master, not divine Adonai). **0 hard fails.**
- `git status output/`: clean (post-2026-04-19 ship gate auto-commits)
- Hebrew word-spacing **clean for all 34 chapters** ✓
- `thai_literal` is **Thai for 33 of 34 chapters** ✓; **EXCEPTION: DEU 15:19** contains the English token "**YHWH พระเจ้าของเจ้า**" (should be "พระยาห์เวห์ พระเจ้าของเจ้า" matching the literal-Hebrew form used in DEU 6:1, 6:2, etc.). **Single instance** — surface `thai` field is correct; the literal field needs the bare-word fix.

**Severity: LOW** — REVIEW for a 1-token mechanical fix.

---

## 21. Flagged for Ben's attention

### A. DEU 5:9-10 Sinai-formula DRIFT from corpus-doc — **DECIDE before tagging** (§2)
Retroactively normalize DEU 5:9-10 to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md`. **Critical** — must be done in tandem with the EXO 34 + NUM 14:18 normalization (Exodus-audit Item A + NUM-audit Item A). The same Sinai-formula recitation drifts at all three verses; all three restore in one paired commit. This is the third downstream test of the unresolved formula-lock decision.

### B. Decalogue parallel-text drift EXO 20 vs DEU 5 — **DECIDE before tagging** (§3)
Write `decalogue_parallel_text_2026-05.md` doc locking the principle that EXO 20 // DEU 5 Thai must match where Hebrew matches. Normalize the 8th commandment (ลักทรัพย์ both), 5:16 honor-parents (match EXO + NT echo), syntactic frame, and DEU 5:6 slave-house formula. Cost: ~5-8 surgical verse-edits + 1 new corpus-doc.

### C. NT-cross-corpus DEU-quote drift cluster — **DECIDE before tagging** (§17)
Write `ot_nt_cross_quotation_thread_2026-05.md` doc locking the OT→NT Thai-thread for נביא/προφήτης (DEU 18:15 + Acts 3:22 anchor), נֶפֶשׁ/ψυχή (Shema-quotation thread), קנא/ζῆλος (DEU 32:21 + Rom 10:19), DEU 25:4 muzzle-ox (3-way drift across DEU + 1Cor 9:9 + 1Tim 5:18). Cost: 1 new corpus-doc + ~20-30 surgical verse-edits across DEU + NT-citation verses + a `check_phrase_consistency.py` extension. **The single biggest forward-protection issue** before the Major Prophets ship.

### D. ḥerem 5-way Thai-surface drift within DEU — **DECIDE before tagging** (§7)
Amend `ot_warfare_ethics_2026-05.md` to lock the canonical Thai surface for חרם (recommend "ทุ่มถวายเพื่อทำลาย"). Normalize the 5 DEU verses (2:34, 3:6, 7:2+26, 13:16+18) to canonical form; keep the DEU 20:17 anchor Layer-2 footer; add back-pointer Layer-2 footers in chs 2-3, 7, 13, 25. Cost: ~5 surgical verse-edits + doc-amendment + ~4 back-pointer footers.

### E. DEU 32:43 LXX/Heb 1:6 expansion handling — **DECIDE before tagging** (§10)
Confirm the asymmetric text-critical disposition is principled (32:8 → DSS/LXX, 32:43 → MT). Amend the DEU 32:43 Layer-2 footer wording to explicitly name the asymmetric-witness rationale (32:8 has 4QDeut^j Hebrew witness; 32:43 has only 4QDeut^q). Cost: 1 Layer-2 footer wording-edit.

### F. Pisgah within-DEU drift (ปิสกาห์ at 34:1 vs พิสกาห์ at chs 3-4) — **REVIEW** (§6a)
Normalize DEU 34:1 ปิสกาห์ → พิสกาห์ to match chs 3-4. 1-character mechanical fix.

### G. Seven-Nations within-DEU drift (DEU 7:1 vs 20:17) — **REVIEW** (§6b)
Normalize DEU 20:17 ethnonyms (เปริสซีต → เปริซซี, ฮีไวต์ → ฮีไว, เยบุสีต → เยบุส; "คน" prefix → "ชาว") to match DEU 7:1. Add `glossary.json` entries for the seven-nations cluster as the corpus-lock.

### H. DEU 11:13 internal Shema-drift (สุดจิต vs DEU 6:5 สุดจิตวิญญาณ) — **REVIEW** (§4)
Normalize DEU 11:13 to "สุดจิตวิญญาณ" to match DEU 6:5. Folded with §17 cross-corpus nephesh-thread.

### I. Adonai-in-prayer at DEU 3:24 + 9:26 (compounds NUM 14:17 outstanding REVIEW) — **REVIEW** (§14)
Amend `divine_names_table_2026-05.md` with a sub-rule for "standalone Adonai-as-prayer-vocative-in-YHWH-context renders as ข้าแต่องค์พระผู้เป็นเจ้า". DEU 3:24 + 9:26 (matching NUM 14:17) become the locking precedent. Carries forward to Pss + Prophets.

### J. DEU 15:19 thai_literal English-token leakage ("YHWH" → "พระยาห์เวห์") — **REVIEW** (§20)
Single 1-token mechanical fix.

### K. Shema canonical doc-lift — **STABLE** (§4)
Write `shema_canonical_six_element_2026-05.md` locking the DEU 6:4-5 + 11:13 surface + cross-corpus NT-quotation Thai-lock (alongside the NUM-audit-recommended `aaronic_blessing_2026-05.md`).

### L. Deuteronomic name-theology doc-lift — **STABLE** (§5)
Write `deuteronomic_name_theology_2026-05.md` locking the "สถานที่ซึ่ง...จะทรงเลือก เพื่อตั้งเป็นที่พำนักของพระนามของพระองค์" Thai form and the forward-protection to 1 Kgs 8 + the NT "name of Jesus" cluster.

---

## External AI review (§3 of checklist)

Suggested 6-cluster packet — one cluster per major editorial-decision area:

1. **Sinai-formula cross-corpus cluster** — §2 (DEU 5:9-10 vs corpus-doc; paired with EXO-audit Item A + NUM-audit Item A as the THIRD downstream witness)
2. **Decalogue parallel-text EXO 20 vs DEU 5** — §3 (syntactic + lexical surface drift)
3. **NT-cross-corpus DEU-quote drift cluster** — §17 (DEU 18:15, 25:4, 32:21, 6:5 + Matt-4 temptation drifts)
4. **Ḥerem Thai-surface normalization** — §7 (5-way drift; doc-amendment + verse-edits)
5. **Within-DEU place-name drift cluster** — §6a + §6b (Pisgah + Seven-Nations)
6. **DEU 32:43 LXX/Heb 1:6 asymmetric text-critical disposition** — §10

Sized for ~20K-char free-tier AI ceilings per `scripts/build_external_review_packet.py`.

---

## Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1 YHWH, §8 curses, §9 Song of Moses, §11 Blessing of Moses, §12 Death of Moses, §15 register, §16 oaths, §18 distinctive vocab, §19 inherited locks-compliant subset, §20 mechanical except 15:19, plus locked-N/A: mal'akh, kapporet, kareth, manah)
- **STABLE (recommend new doc):** 3 items (§4 Shema, §5 centralization-name-theology, partial §18 tithing)
- **REVIEW:** 5 items (§6a Pisgah within-DEU, §6b Seven-Nations within-DEU, §14 Adonai-in-prayer compounds NUM 14:17, §20 DEU 15:19 thai_literal English-leakage, §4 DEU 11:13 internal Shema-drift)
- **DECIDE:** 4 items (§2 Sinai-formula CRITICAL, §3 Decalogue parallel-text HIGH, §17 NT-cross-corpus DEU-quote cluster HIGH, §7 ḥerem 5-way surface HIGH, §10 DEU 32:43 text-critical MEDIUM — §10 promoted from REVIEW to DECIDE because it codifies the principled text-critical disposition before further Pentateuch + Prophets ship)

**4 DECIDE items block the `book-deuteronomy-v1` tag.** (§2, §3, §7, §17; §10 is MEDIUM-severity DECIDE and can be deferred if Ben prefers — but recommend resolving in tandem.)

**3 new translator_decisions docs recommended** (shema_canonical_six_element, deuteronomic_name_theology, ot_nt_cross_quotation_thread) **+ 1 existing doc to amend** (`ot_warfare_ethics_2026-05.md` for ḥerem Thai-surface lock; `divine_names_table_2026-05.md` for Adonai-in-prayer sub-rule per NUM-audit §8 + DEU §14 compound; `exod_34_attribute_formula_2026-05.md` for DEU 5:9-10 addition to the locked-recitations list) **+ optional 1 new doc** (`decalogue_parallel_text_2026-05.md`) if Ben prefers the principle-doc path for §3.
