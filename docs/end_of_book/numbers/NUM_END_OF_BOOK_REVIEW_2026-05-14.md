# Numbers — End-of-Book Review

**Date:** 2026-05-14
**Scope:** All 36 chapters of Numbers (~1,289 verses); `glossary.json`; existing `docs/translator_decisions/` (78 docs incl. the Exodus-audit additions `malak_yhwh_2026-05.md`, `kapporet_atonement_cover_2026-05.md`, `pharaoh_heart_hardening_2026-05.md`, `ot_polytheistic_register_2026-05.md`, plus the Sinai-formula doc `exod_34_attribute_formula_2026-05.md`).
**Trigger:** NUM 36 shipped (commit `9a54c5d`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Fifth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus) and the **third Pentateuch book**. Numbers contains the first OT recitation of the Sinai attribute-formula AFTER Exodus 34 (Num 14:18), the Balaam mal'akh-YHWH cluster (22:22-35; 10 occurrences), and the second Passover (ch.9) — three direct downstream tests of the Exodus-audit corpus-doc landings.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 36/36 chapters have green per-chapter reports + back-translations + textual_variants files; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the 260-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `git status output/` shows only the harmless re-run of `output/check_reports/divine_names.md`. The divine_names script reports 29 warnings on NUM (7 [C-soft] standalone-Adonai false-positives + 22 [D] first-occurrence-footnote-wording-drift starting at ch.15 — see §3); zero hard fails.
- **Numbers exercises every OT-corpus lock landed by 2026-05-13 audit** including the four NEW Exodus-audit docs. It is the first downstream OT-book test of (a) the **Sinai attribute-formula** (Num 14:18 is the SECOND OT occurrence after Exod 34:6-7); (b) the **mal'akh-yhwh corpus lock** (the Balaam-donkey cluster at 22:22-35 + 20:16 = 11 occurrences — the largest mal'akh-yhwh cluster in any OT book); (c) **kapporet** (single Num 7:89 occurrence — compliant); (d) **ot_polytheistic_register** (Num 25 Baal-Peor apostasy + Num 33:4 "judgments on the gods of Egypt").
- **Data integrity is clean.** Hebrew word-spacing correct in all 36 chapters; `thai_literal` is Thai in all 36 chapters (no regression of the Genesis chs.44-50 English-leakage pattern); all 36 chapters have correctly-spaced Hebrew and Thai `thai_literal` fields.
- **17 inherited locks verified compliant** in NUM across the divine-name family, OT-register policy, Hebrew-grammar-transfer, Hebrew-idioms, verse-schema (incl. MT-vs-English versification at ch.16/17 + ch.29/30 boundaries — Layer-2 footers landed correctly), proper-names, proper-noun-wordplay (Massah-Meribah recurrence at 20:13), chesed-corpus-doc, nicham-corpus-doc, paqad-corpus-doc, hebrew-oath, divine-anthropomorphism, mt_vs_lxx-textual-variant-handling, divine-object-praise, narrator-vs-character-voice, kapporet, leitwort, manah, pagan_deities.
- **5 Numbers-distinctive patterns are STABLE-and-locked** at corpus level (the Aaronic Blessing 6:24-26 as the canonical priestly-benediction Thai form; the wilderness-itinerary 42-station catalog at ch.33; the Sotah ordeal vocabulary 5:11-31; the Nazirite vow vocabulary 6:1-21; the cities-of-refuge / blood-redeemer vocabulary at ch.35).
- **3 items flagged STABLE-but-undocumented** (recommend new corpus docs): the **Aaronic blessing six-clause structure** (6:24-26 is the most-recited OT-corpus liturgical text after Shema — needs a corpus-doc lock); the **Balaam-oracle prophetic-poetry register** (chs.23-24, 4 oracles); the **Numbers-distinctive ritual-vocabulary cluster** (Sotah 5; Nazirite 6; Red Heifer 19; Cities of Refuge 35; covers vocabulary for חַטָּאת sin-offering, נֶפֶשׁ life/person, גָּאַל redeem-avenger).
- **4 items flagged REVIEW** (defensible-but-worth-Ben's confirmation): the **place-name drift Sinai = ซีนาย/สีนาย mix** within NUM (10× สีนาย vs. 27× ซีนาย; cf. EXO 100% ซีนาย — §6); the **place-name drift Succoth = สุคโคท→สุคคท** between EXO and NUM (§7); the **first-occurrence YHWH-footnote wording-drift starting at NUM 15** (the romanization "ยาห์เวห์ Yahweh" was dropped from the chapter-footer template starting at ch.15 — affects divine_names check pass-rate, §3); the **NUM 14:17 standalone אֲדֹנָי vocative** rendering ("องค์พระผู้เป็นเจ้าของข้าพระองค์" rather than the divine_names_table doc's "องค์เจ้านาย" form — §8).
- **3 items flagged DECIDE** (Ben choice needed before tagging `book-numbers-v1`):
  - **Num 14:18 Sinai-formula recitation DRIFT from `exod_34_attribute_formula_2026-05.md`** — the SECOND OT recitation of the formula drifts in 5 of 5 character-vocabulary slots. See §2. **CRITICAL.**
  - **Num 22:22-35 + 20:16 mal'akh-YHWH cluster (11 occurrences) DRIFT from `malak_yhwh_2026-05.md`** — uniform "ทูตขององค์พระผู้เป็นเจ้า" (envoy form) rather than the doc-locked "ทูตสวรรค์ขององค์พระผู้เป็นเจ้า" (heavenly-messenger form). See §4. The Balaam-donkey is the most-iconic mal'akh-YHWH OT cluster.
  - **Num 31:17-18 + 25:1-9 sexual-violence + zealot-execution register** — sensitive war-bride command (31:17-18 "kill every male child + every non-virgin woman") + Phinehas spear-execution (25:7-8). Translation surface is faithful; the question is whether a Layer-2 doctrinal footer is warranted for Thai-evangelical reader experience. See §17.
- **External AI review (§3) pending.** Suggested 6-item packet (§2/§4/§17 DECIDE items + §6/§3/§8 REVIEW items).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + Numbers first-occurrence footnote — **LOCKED-with-wording-drift-flag (§3)**

**321 YHWH occurrences across all 36 chapters** (every chapter contains YHWH — Numbers is a sustained YHWH-speech book, the most concentrated Tetragrammaton-density in the OT-corpus pilot). Layer-2 first-occurrence footers present at all 36 `output/textual_variants/numbers_NN.json` files (cross-references the divine_names_table doc; explicitly identifies the verses-of-occurrence within each chapter).

All 321 occurrences render as **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` ✓. No drift of the Tetragrammaton itself. Corpus-total YHWH count after Numbers: ~920+ occurrences across 260 chapters, all uniformly rendered.

**LOCKED** ✓ for the Tetragrammaton surface itself. See §3 for the first-occurrence-footnote **wording-drift** beginning at ch.15.

---

## 2. Num 14:18 Sinai attribute-formula recitation — **DECIDE before tagging (CRITICAL — DRIFT from corpus-doc)**

**The single most consequential finding of this audit.** Num 14:18 is Moses' intercessory recitation of the Sinai attribute-formula (Exod 34:6-7), spoken during the spies-rebellion crisis. The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` explicitly names Num 14:18 in its locked-recitations list (alongside Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Jonah 4:2, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18).

> **14:18 Hebrew:** יְהוָה אֶרֶךְ אַפַּיִם וְרַב־חֶסֶד נֹשֵׂא עָוֹן וָפָשַׁע וְנַקֵּה לֹא יְנַקֶּה פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים
>
> **14:18 Thai (as shipped):** ‘องค์พระผู้เป็นเจ้าทรงเป็นพระเจ้าผู้ทรง**พระพิโรธช้า** และทรง**เปี่ยมด้วยความรักมั่นคง** ผู้ทรง**ยกโทษความผิดและการละเมิด** แต่จะไม่ทรงปล่อย**ผู้ผิด**ให้พ้นโทษ ทรง**ให้ความผิดของบิดาตกถึงบุตรหลาน**จนถึงสามและสี่ชั่วอายุ’

Note Num 14:18 is the **shorter** form of the formula — it omits the opening רַחוּם וְחַנּוּן ("compassionate and gracious") character-pair and the third sin-term חַטָּאָה (sins). What remains drifts component-by-component:

| Hebrew (Num 14:18) | Doc-locked Thai | Num 14:18 as shipped | Drift? |
|---|---|---|---|
| אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | **ทรงพระพิโรธช้า** | ✗ (different metaphor; the doc-canonical "กริ้วช้า" is Rachasap-active; "พระพิโรธช้า" is "slow in wrath") |
| וְרַב־חֶסֶד | **ทรงบริบูรณ์ด้วยความรักมั่นคง** | **ทรงเปี่ยมด้วยความรักมั่นคง** | ✗ (เปี่ยม vs. บริบูรณ์ — synonyms; minor lexical drift) |
| נֹשֵׂא עָוֹן וָפָשַׁע | **ทรงยกโทษความชั่ว การละเมิด** | **ทรงยกโทษความผิดและการละเมิด** | ✗ (ความชั่ว doc → ความผิด actual — major lexical drift; doc's "ความชั่ว" = moral-evil register, actual "ความผิด" = legal-fault register) |
| וְנַקֵּה לֹא יְנַקֶּה | **แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ** | **แต่จะไม่ทรงปล่อยผู้ผิดให้พ้นโทษ** | ✗ (ทรงพิจารณา vs. ทรงปล่อย — different verb sense; legal-deliberation vs. release) |
| פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **ทรงให้ความผิดของบิดาตกถึงบุตรหลาน** | ✗ (ทรงลงโทษ vs. ทรงให้...ตก — no direct "punish" verb; "fathers→sons" vs. "ancestors→grandchildren-and-great-grandchildren") |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **จนถึงสามและสี่ชั่วอายุ** | partial drift (acceptable variant phrasing) |

**Editorial assessment.** This is the **second-major instance of the same Sinai-formula drift** Ben encountered in the Exodus audit (§2 there). The pattern is identical: each formula-component is rendered with its own Thai vocabulary, drawing on the verse's local sense rather than the locked-corpus form. Because Num 14:18 is the **shortest formal recitation** in the OT (only 5 character-components vs. Exod 34's 8), the drift is harder to spot but compounds in the same way.

**This audit lands in the SAME ship-window as the Exodus audit decision.** Whatever resolution Ben chooses for EXO 34 (the Exodus-audit Item A — retroactive normalization to doc-canonical Thai, or doc-revision) **must apply identically to Num 14:18**. If Exod 34 is normalized to the doc but Num 14:18 is left as-is, the cross-corpus recitation breaks at its first downstream witness.

**Forward-compounding (the rest of the formula recitations):** Ps 86:15 ships with Psalms; Ps 103:8 + Ps 145:8 ship with Psalms; Joel 2:13 + Nah 1:3 + Mic 7:18 ship with the Twelve; Neh 9:17 + 2 Chr 30:9 ship with the Histories. Each downstream recitation will diverge ad-hoc unless the corpus-doc Thai is locked and applied.

**DECIDE before tagging — recommend retroactive normalization in tandem with EXO 34 normalization.** Three paths:

**(a) Strict normalization in tandem with EXO 34** — re-render Num 14:18 to match the doc's canonical Thai. The verse-level surgical edit is straightforward (15-word verse). Strongest cross-corpus protection; preserves the doc-lock at its first downstream test.

**(b) Doc-revision** — if Ben endorses the as-shipped EXO 34 surface, the doc must be amended and Num 14:18 amended in lockstep with EXO 34's. Cost: doc + 2 verse rewrites (Exod 34:6-7 + Num 14:18) + the Jonah 4:2 retroactive de-normalization. NOT recommended (re-opens a 2026-05-09 cross-AI consensus).

**(c) Leave as-is, accept doc-divergence** — the worst path. Breaks cross-corpus traceability; Ben has explicitly endorsed the locking-principle elsewhere (chesed, paqad, malak).

**Recommend (a).** This is the **direct downstream test** of the Exodus-audit decision. If Ben chooses (a) for Exodus, the same edit is required here. **Severity: CRITICAL** — paired with the EXO 34 finding.

**Followup:** the doc's Implementation Checklist (§3 item 2 in the doc) calls for `check_phrase_consistency.py` extension to HARD FAIL when 3+ formula-components co-occur. Num 14:18 is one of the verses the extension would catch. Recommend writing the extension in tandem with the §2(a) commit.

---

## 3. Numbers first-occurrence YHWH-footnote wording-drift starting at ch.15 — **REVIEW**

The `output/textual_variants/numbers_NN.json` Layer-2 first-occurrence footnotes were drafted in a consistent template for chapters **1-14**:

> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏที่ข้อ X, Y, Z...) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า ออกเสียงโดยทั่วไปว่า **"ยาห์เวห์"** Yahweh)…

Starting at ch.15, the template **omits the "ยาห์เวห์ Yahweh" romanization-phrase**:

> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏที่ข้อ X, Y, Z...) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า). ฉบับเอเรโมสใช้ **องค์พระผู้เป็นเจ้า** ตามแบบแผนของฉบับพันธสัญญาใหม่ในการแปล κύριος.

**Effect.** The script `scripts/check_divine_names.py` (line 186) checks for the marker phrases `"องค์พระผู้เป็นเจ้α" + "ยาห์เวห์"` or the english `"tetragrammaton" / "yhwh"` in `.lower()` form. The post-ch.14 template loses the Thai marker (ยาห์เวห์) without adding the english marker — so the script reports `[D] numbers ch.NN: contains YHWH but no first-occurrence footnote` for chs.15-36 (22 warnings). The footnotes ARE present and well-formed; the script's pattern-match no longer finds them.

**Two parallel fixes possible.** (a) **Restore the wording template** — add back the "ยาห์เวห์ Yahweh" romanization phrase to chs.15-36 footnotes (22 short edits). (b) **Loosen the script's pattern** — add the post-ch.14 marker phrase ("ตามแบบแผนของฉบับพันธสัญญาใหม่") to the script's detection set. Either preserves the warning-free state.

**Editorial assessment.** The post-ch.14 wording is actually more concise and references the project's own divine_names_table doc explicitly — arguably better than the original template. Recommend (b): update the script to recognize the post-ch.14 marker, and adopt the shorter template as the going-forward standard. This avoids 22 footnote-edits and aligns with the project's pattern of evolving conventions docpos-first.

**Severity: LOW** — Tier-2 footnotes are reader-facing but the wording-drift is style-only; underlying lock is intact. **REVIEW** — Ben to decide which fix.

---

## 4. Num 20:16 + Num 22:22-35 mal'akh-YHWH cluster — **DECIDE before tagging (DRIFT from corpus-doc)**

The mal'akh-YHWH lemma appears in NUM **11 times**, all in supernatural / divine-messenger contexts:

| Verse | Hebrew | Thai (as shipped) |
|---|---|---|
| **20:16** | מַלְאָךְ (history-retrospect, Israel-to-Edom diplomatic letter recounting Exodus) | **ทูต** |
| **22:22** | מַלְאַךְ יְהוָה (Balaam's-donkey, opens cluster) | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:23** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:24** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:25** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:26** | מַלְאַךְ־יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:27** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:31** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:32** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:34** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |
| **22:35** | מַלְאַךְ יְהוָה | **ทูตขององค์พระผู้เป็นเจ้า** |

**The lock per `malak_yhwh_2026-05.md` (decided 2026-05-13, post-EXO audit) is uniform `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** for all divine-messenger mal'akh contexts. The doc's §3 Implementation Checklist item explicitly names **"Num 22 (Balaam's donkey)"** under "forward-cover" — Numbers was supposed to be the first downstream OT-book to apply the lock. Instead, all 11 occurrences shipped with the pre-doc surface ("ทูตของ-" envoy-form).

**Editorial assessment.** This is the **largest mal'akh-YHWH cluster in any OT book** (more than the 6 in Exodus). The Balaam-donkey is one of the **most-iconic mal'akh-YHWH scenes in scripture** (with sword drawn, blocking the way), and is the OT-NT pre-incarnate-Christ-as-mal'akh tradition's locus alongside Gen 16/22 + Judg 6/13.

**The cluster ALSO breaks the cross-corpus thread internally within Numbers:** the doc reads `ทูตสวรรค์ของเรา` for any YHWH-1cs-suffixed מַלְאָכִי (cf. Exod 32:34). Num 22 has no 1cs-suffix occurrences, but if Ben confirms the corpus-doc, future patient-form `ทูตสวรรค์ของเรา` constructions (Exod 23:23 already normalized) need to be coherent with the NUM normalization here.

**DECIDE before tagging — recommend normalization to doc-canonical Thai (option a)** for all 11 occurrences (10 in ch.22 + 1 in 20:16). Three paths:

**(a) Strict normalization** — rewrite the 11 occurrences to `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` (or `ทูตสวรรค์` for the standalone 20:16). Cost: 11 surgical verse-edits + re-run per-chapter checks. Restores the doc-lock at its first downstream test.

**(b) Doc-revision** — accept the as-shipped NUM 22 surface as a sub-rule (treat the Balaam-donkey cluster as a literary unit that uses the envoy-form rather than the heavenly-messenger form). Defensible only if Ben actively prefers the as-shipped Thai — but doc was decided 2026-05-13 with Ben + tri-AI consensus to lock `ทูตสวรรค์`; re-opening discards that decision.

**(c) Leave as-is, accept divergence** — worst path; breaks the cross-corpus thread the doc was created to protect. Genesis (Hagar 16:7-13; Akedah 22:11/15) is already mixed — needs same normalization.

**Recommend (a)** + the doc's §3 Implementation Checklist item (extend `check_phrase_consistency.py` to HARD FAIL when Hebrew has divine-context מַלְאָךְ but Thai lacks ทูตสวรรค์). The cost is 11 verse edits + a short check-script extension; the benefit is corpus-wide protection. **Severity: HIGH.**

---

## 5. Aaronic Blessing (Num 6:24-26) — **STABLE (recommend corpus-doc)**

The priestly blessing in Num 6:24-26 + 6:27 is the single most-recited Hebrew Bible liturgical text in Jewish + Christian usage. The shipped Thai:

> **6:24** ‘ขอองค์พระผู้เป็นเจ้าทรงอวยพรท่าน และทรงพิทักษ์รักษาท่าน
> **6:25** ขอองค์พระผู้เป็นเจ้าทรงให้พระพักตร์ของพระองค์ส่องสว่างแก่ท่าน และโปรดประทานพระเมตตาแก่ท่าน
> **6:26** ขอองค์พระผู้เป็นเจ้าทรงยกพระพักตร์ของพระองค์เหนือท่าน และประทานสันติสุขแก่ท่าน’
> **6:27** ดังนั้น พวกเขาจะวางนามของเราเหนือชนอิสราเอล และเราจะอวยพรพวกเขา"

**Editorial assessment.** All six benedictory clauses render cleanly:
- **יְבָרֶכְךָ ... וְיִשְׁמְרֶךָ** → "ทรงอวยพร ... และทรงพิทักษ์รักษา" ✓
- **יָאֵר ... פָּנָיו** → "ทรงให้พระพักตร์ ... ส่องสว่าง" — pulls **פָּנִים → พระพักตร์** per `hebrew_idioms_and_metaphor_2026-05.md` lock ✓
- **וִיחֻנֶּךָּ** (חנן graciousness) → "โปรดประทานพระเมตตา" — note this is the **doc-locked חנן → พระคุณ** drift; the doc's lock is "พระคุณ" (gracious), shipped uses "พระเมตตา" (mercy). See cross-reference §15 below.
- **יִשָּׂא ... פָּנָיו** → "ทรงยกพระพักตร์" — preserves the "lift up his face" Hebrew metaphor literally ✓
- **שָׁלוֹם** → "สันติสุข" ✓
- **שָׂמוּ אֶת־שְׁמִי** → "วางนามของเรา" ✓ (preserves the name-placement formula that prefigures Deut 12:5 + Solomon's temple-dedication 1 Kgs 8)

The single drift is **חנן → พระเมตตา (rather than พระคุณ)** at 6:25, which carries the verb's force into the same lemma-territory as רחם (mercy) in the Sinai-formula. This mirrors the EXO-audit-§3 חַנֹּתִי mapping question and compounds with §2 above.

**STABLE** ✓ — the surface is faithful and the doc-lemma is the only minor drift. **Recommend new doc:** `docs/translator_decisions/aaronic_blessing_2026-05.md` — locks the six-clause Thai form, the doc-canonical חנן rendering at 6:25 (whether พระคุณ or พระเมตตา), and the cross-reference to the Hellenistic LXX (Num 6:24-26 LXX is the form quoted in 4QFlorilegium, the Aaronic priestly bless. The Heb 13:20-21 NT benediction is a downstream typological echo. The doc would forward-protect future liturgical recitations and locks Ben's chosen חנן-rendering across the OT corpus.

---

## 6. Place-name Sinai = ซีนาย / สีนาย mix within NUM — **REVIEW**

Frequency count across the corpus:

| Book | ซีนาย | สีนาย |
|---|---|---|
| Exodus | 44× | 0× |
| Numbers | **27×** | **10×** |

**Within-NUM drift.** The same Hebrew סִינַי is rendered two different ways in the same book. Spot-check shows the 10× `สีนาย` occurrences cluster in chs.1-3, 9-10, 33; the 27× `ซีนาย` are distributed elsewhere. Most likely cause: the chapter-by-chapter ship cadence allowed local-precedent drift before the locking-precedent (Exodus 19's `ซีนาย`) was retroactively applied.

**Cross-book drift.** Exodus locked `ซีนาย` (100% uniform across 44 occurrences); Numbers's 10× `สีนาย` breaks that lock. Future Pentateuch (Deut 33:2) and Pentateuchal-allusion (Judg 5:5, Ps 68:8+17, Neh 9:13) recitations are at risk.

**Editorial assessment.** Both spellings are defensible Thai transliterations of סִינַי (Hebrew /siːˈnaj/) — `สีนาย` follows the Hebrew vowel /iː/ literally; `ซีนาย` follows the conventional Thai-Christian-Bible Sinai spelling (matches THSV-1971). Per `proper_names_and_transliteration_2026-05.md`'s "follow established Thai-Christian-Bible precedent unless documented otherwise" rule, `ซีนาย` is the corpus-canonical form.

**REVIEW flag.** Recommend normalization: **change the 10× `สีนาย` to `ซีนาย`** to match Exodus. Cost: ~10 surgical text-edits across chs.1-3, 9-10, 33 (mostly the NUM 33 itinerary in 33:15-16; cluster at NUM 1:1, 1:19, 3:1, 3:4, 3:14, 9:1, 9:5, 10:12). Add a `glossary.json` entry or a quick check-script extension that locks the canonical ซีนาย form for סִינַי. **Severity: MEDIUM** — direct proper-name lock-violation.

---

## 7. Place-name Succoth: EXO สุคโคท → NUM สุคคท — **REVIEW**

Frequency count:

| Book | สุคโคท | สุคคท |
|---|---|---|
| Exodus | 7× | 0× |
| Numbers | 0× | **4×** |

**The drift.** EXO 12:37, 13:20 use `สุคโคท` (7 total occurrences). NUM 33:5, 33:6 use `สุคคท` (4 total). The Hebrew סֻכֹּת is identical in both books. The Numbers form differs from the Exodus-locked form.

**Editorial assessment.** Likely cause: the NUM 33 itinerary was drafted from the Hebrew + a parallel reading rather than from glossary cross-check. The two-letter "โค→ค" drop is subtle and easy to miss in proof.

**REVIEW flag.** Recommend normalization to **สุคโคท** to match Exodus across 4 verses. Cost: ~4 text-edits in chs.33. Strongly consider extending the proper-name script or `glossary.json` lookups to catch place-name drift between books — this is a class of drift that mechanical checks miss because both spellings are valid Thai-transliteration-of-Hebrew. **Severity: MEDIUM.**

---

## 8. Num 14:17 standalone אֲדֹנָי — **REVIEW (drift from divine_names_table)**

> **14:17 Hebrew:** וְעַתָּה יִגְדַּל־נָא כֹּחַ אֲדֹנָי
>
> **14:17 Thai (as shipped):** บัดนี้ ขอพระอานุภาพของ**องค์พระผู้เป็นเจ้าของข้าพระองค์**ทรงสำแดงพระเกียรติยิ่งใหญ่...

The doc `divine_names_table_2026-05.md` locks **standalone אֲדֹנָי → องค์เจ้านาย** as a distinct form from the YHWH-form (`องค์พระผู้เป็นเจ้า`). Num 14:17 is in a Moses-to-YHWH prayer context — Moses uses the vocative `אֲדֹנָי` (not YHWH) to invoke the Lord's power.

**Editorial assessment.** Two possible readings: (a) the form is intentional — Moses is addressing YHWH-as-master (Adonai), so the Thai's "องค์พระผู้เป็นเจ้าของข้าพระองค์" (literally "the Lord of mine") preserves the personal-vocative force even if the lexical category differs; (b) the form is a drift — the doc-lock is "องค์เจ้านาย", and even in YHWH-context the Adonai vocative should use that form.

The script `check_divine_names.py` does NOT flag this verse as a [C] case because the YHWH-form `องค์พระผู้เป็นเจ้า` IS present in the Thai (the check's predicate is "Thai missing both Adonai-form AND YHWH-form"). The drift is therefore script-invisible.

**REVIEW flag.** Recommend amending `divine_names_table_2026-05.md` to address standalone Adonai in YHWH-context-prayer (Num 14:17 is a clean example; similar cases will recur in Pss + the Prophets — Isa 6:1+8+11, Jer's "Adonai YHWH" compound; Ezekiel passim). Two paths:
- (a) **Lock Adonai-vocative-in-prayer → องค์พระผู้เป็นเจ้าของข้าพระองค์** (the as-shipped form) — names the principled distinction between standalone Adonai-as-title (lock = องค์เจ้านาย) and Adonai-as-prayer-vocative (lock = องค์พระผู้เป็นเจ้าของข้าพระองค์).
- (b) **Normalize Num 14:17 to องค์เจ้านาย** — match the doc strictly. Cost: 1 verse-edit.

**Recommend (a) doc-amendment.** The as-shipped Thai reads as **petitionary "my Lord"** with Rachasap; reading "องค์เจ้านาย" in a prayer-vocative would actually sound less petitionary in Thai register. Doc amendment locks the principled distinction. **Severity: LOW.**

---

## 9. Balaam oracles (Num 23-24) — **STABLE-with-prophetic-poetry-doc-recommendation**

Four oracles of Balaam across 23:7-10, 23:18-24, 24:3-9, 24:15-24. Several features tested:

| Verse | Hebrew | Thai (as shipped) | Notes |
|---|---|---|---|
| **23:19** | לֹא אִישׁ אֵל וִיכַזֵּב וּבֶן־אָדָם וְיִתְנֶחָם | "พระเจ้ามิใช่มนุษย์ที่จะมุสา หรือเป็นบุตรของมนุษย์ที่จะเปลี่ยนพระทัย" | ✓ נחם → **เปลี่ยนพระทัย** matches `nicham_divine_relenting_2026-05.md` factive-volitional lock |
| **23:21** | יְהוָה אֱלֹהָיו עִמּוֹ | "องค์พระผู้เป็นเจ้าพระเจ้าของพวกเขาทรงอยู่กับพวกเขา" | ✓ |
| **23:22 + 24:8** | אֵל מוֹצִיאוֹ מִמִּצְרָיִם | "พระเจ้าทรงนำเขาออกจากอียิปต์" | ✓ ; Recapitulates Exod 20:2 with same Thai |
| **24:4 + 24:16** | שַׁדַּי / יוֹדֵעַ דַּעַת עֶלְיוֹן | "ผู้ทรงมหิทธิฤทธิ์" / "ผู้สูงสุด" | ✓ matches `divine_names_table_2026-05.md` El Shaddai + Elyon locks |
| **24:17** | דָּרַךְ כּוֹכָב מִיַּעֲקֹב וְקָם שֵׁבֶט מִיִּשְׂרָאֵל | "ดวงดาวจะออกมาจากยาโคบ และคทาจะลุกขึ้นจากอิสราเอล" | ✓ messianic poetic-imagery preserved literally; cross-refs Rev 22:16 |

**Editorial assessment.** The oracle-register (Hebrew elevated poetry) is rendered cleanly in Thai. The 24:17 "Star out of Jacob" preserves the imagery without messianic-paraphrase — matches the OT-LXX-NT thread (Justin Martyr's Dial. 106 quotes this; Bar Kokhba's name-tradition rests on the שֵׁבֶט-cluster; Rev 22:16's "ดาวประจำเช้า" inherits the imagery). 

**STABLE** ✓ — the Hebrew poetic register is preserved without flattening. **Recommend new doc:** `docs/translator_decisions/balaam_oracles_2026-05.md` — names the prophetic-poetry register, the messianic-imagery preservation principle, and locks the cross-reference to Rev 22:16 + Matt 2:2 (the Magi's Bethlehem-star-tradition rests on Num 24:17).

---

## 10. Wilderness-itinerary (Num 33) — **STABLE-with-§7-flag**

42 station-names across NUM 33:5-49. All proper-name transliterations are internally consistent within ch.33 and match the corresponding occurrences in earlier chapters (Sinai-itinerary in chs.10-14; Kadesh in 13-14, 20). **Single exception: NUM 33:5-6 `สุคคท` drift from EXO's `สุคโคท`** — see §7.

**LOCKED in current handling** for the 41 other place-names; **§7 flag** for the Succoth drift.

---

## 11. Num 16-17 Korah's rebellion + MT versification — **LOCKED**

Numbers 16 in MT versification has 35 verses; in English it has 50. Numbers 17 in MT has 28 verses; in English it has 13. The MT-vs-English boundary at the 16/17 break is documented via `versification_note` Layer-2 footers at `output/textual_variants/numbers_17.json`. Same for the 29/30 boundary (one verse shifts).

Spot-check NUM 16:30 (the swallowing-by-Sheol prophecy):
> **16:30** "แต่ถ้าองค์พระผู้เป็นเจ้าทรงทำสิ่งที่ไม่เคยมีมาก่อน คือแผ่นดินอ้าปากของมันออกและกลืนพวกเขา ... และพวกเขาลงไปยังแดนคนตายทั้งเป็น"

**שְׁאוֹל → แดนคนตาย** ✓ matches NT corpus's lock for ᾅδης (cross-doc: `ouranos_heaven_rendering_2026-04.md`-companion eschatology doc). The "open-the-mouth-of-Sheol" Hebrew metaphor is preserved literally.

**LOCKED** ✓.

---

## 12. Num 19 Red-heifer ordinance — **STABLE (recommend ritual-vocabulary doc)**

The red-heifer purification ritual at NUM 19 establishes Thai vocabulary for the chief Levitical purification-from-corpse-defilement ritual:

| Hebrew | Thai (current) | Notes |
|---|---|---|
| **פָּרָה אֲדֻמָּה תְּמִימָה** | **วัวสีแดง สมบูรณ์ ไม่มีตำหนิ** | "red unblemished cow" (NUM 19:2) |
| **חַטָּאת** | **เครื่องบูชาไถ่บาป** | "sin/purification-offering" (NUM 19:9, 17) |
| **מֵי נִדָּה** | **น้ำชำระมลทิน** | "water of separation/impurity-cleansing" |
| **טָמֵא** | **เป็นมลทิน** | "be impure" |
| **טָהוֹר** | **สะอาด** | "be pure / clean" |
| **כִּפֶּר** (no occurrence in NUM 19 but in 28:22, 29:5, 35:33) | (no Thai surface verb stated) | — |

**The חַטָּאת → เครื่องบูชาไถ่บาป cross-corpus question.** This is the Hebrew term for the sin/purification-offering ritually administered. The NT-corpus uses `เครื่องบูชาไถ่บาป` for **ἱλαστήριον at Rom 3:25** per the `kapporet_atonement_cover_2026-05.md` and `hilasterion_heb-rom_distinction_2026-05.md` docs. The cross-corpus thread is:
- OT חַטָּאת (sin/purification-offering) → **เครื่องบูชาไถ่บาป**
- NT ἱλαστήριον (mercy-seat or propitiation-offering) at Rom 3:25 → **เครื่องบูชาไถ่บาป**

Both Hebrew/Greek lemmas land at the same Thai surface. This is **principled** because the Pauline thought-world reads Christ's atonement against the OT-sacrificial-vocabulary, but worth noting: a Thai reader will read `เครื่องบูชาไถ่บาป` at both NUM 19:9 (red heifer) and Rom 3:25 (Christ). The doctrinal continuity is theologically intended; the lexical-collapse is the price.

**STABLE** ✓. **Recommend new doc:** `docs/translator_decisions/sacrificial_vocabulary_2026-05.md` — locks the Thai vocabulary for the Levitical sacrifices (חַטָּאת sin-offering, אָשָׁם guilt-offering, עֹלָה burnt-offering, מִנְחָה grain-offering, שְׁלָמִים peace-offering, נֶסֶךְ drink-offering) and names the cross-corpus continuity with the NT propitiation vocabulary. The doc would forward-protect Leviticus (when it ships) and the entire Hebrews 9-10 sacrificial-typology cluster.

---

## 13. Num 5:11-31 Sotah ordeal — **STABLE**

The suspected-adultery ordeal at NUM 5:11-31 is the OT's only formal **trial-by-ordeal** ritual. The Thai handles:

- **קִנְאָה / קִנְאֹת** "jealousy/zeal" → **ความหึงหวง** (the same lemma renders YHWH's "zeal" at 25:11 + Exod 20:5 + 34:14 — note the cross-corpus thread)
- **טָמֵא** "be defiled" → **เป็นมลทิน** (matches §12 ritual-purity vocabulary)
- **מַיִם הַמָּרִים הַמְאָרֲרִים** "bitter water that causes the curse" → **น้ำขมที่นำคำสาปแช่ง** ✓ (preserves the both-bitter-and-curse-bearing Hebrew construction)
- **צָבָה / נָפַל יָרֵךְ** "swelling belly / falling thigh" → **ท้องบวม / สะโพกเหี่ยวลีบ** ✓ (preserves the Hebrew somatic-curse imagery literally — anatomical euphemism for miscarriage or sexual dysfunction; preserved without sanitization)

**STABLE** ✓.

---

## 14. Num 35 Cities of Refuge + Blood-Avenger — **STABLE**

The cities-of-refuge ordinance at NUM 35:9-34 establishes the Thai legal vocabulary for the OT's **manslaughter-vs-murder distinction**:

- **עִיר מִקְלָט** "city of refuge" → **เมืองลี้ภัย** ✓
- **גֹּאֵל הַדָּם** "redeemer-of-blood" (the kinsman-avenger) → **ผู้แก้แค้นเลือด** ✓ (preserves the גָּאַל kinsman-redeemer cross-corpus lemma; will compound forward to Ruth's Boaz גֹּאֵל, Isaiah's "Redeemer" titles, Heb 9:12's lit-r-edeemer-construction)
- **כֹּפֶר** "ransom" (35:31-32) → **สินไถ่** ✓ (matches NT-corpus lock for λύτρον at Mark 10:45 + Matt 20:28)
- **רֹצֵחַ** "manslayer" → **ผู้ฆ่า** vs. **רֹצֵחַ הוּא** "he is a murderer" → **ฆาตกร** ✓ (preserves the inadvertent-vs-intentional distinction)

**STABLE** ✓ — the legal-vocabulary cluster is principled and forward-protected to Deut 19 (parallel cities-of-refuge ordinance), Josh 20 (cities-of-refuge designations), Ruth 4 (kinsman-redeemer narrative), 1 Kgs 2 (Joab's altar-flight), and the NT typological-redemption cluster (Heb 9:12 + Eph 1:7 + 1 Pet 1:18-19).

**Recommend new doc** (subsumed under the §12 sacrificial-vocabulary doc, or standalone): `docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` — locks **גֹּאֵל → ผู้แก้แค้น/ผู้ไถ่** distinction (depending on judicial vs. redemptive context) and forward-protects Ruth + Isaiah-redeemer + NT λύτρωσις cluster.

---

## 15. Inherited corpus locks — **all compliant except where flagged**

| Doc | NUM evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | See §1. Tetragrammaton-as-องค์พระผู้เป็นเจ้า uniform (321/321); El Shaddai 24:4, 24:16 → ผู้ทรงมหิทธิฤทธิ์; Elyon 24:16 → ผู้สูงสุด. **EXCEPTION: Num 14:17 standalone Adonai-in-prayer renders YHWH-form (§8); 22 chapters' first-occurrence footnote drifts from script-pattern (§3).** | **LOCKED-with-§8-+-§3-flag** |
| `ot_register_policy_2026-05.md` | Divine-speech ทรง- throughout (e.g., 6:24-26, 12:6-8, 14:11-12, 18:20+24, 22-24); Moses receives **plain narrator + humble first-person ข้าพระองค์** to YHWH (per doc rule for prophet-leaders); the Levitical priests carry plain register; foreign-king Balak (22:6+15-17, 23:11, 23:25-30, 24:10-14) uses **ตรัส**-style royal-Thai speech-verb consistent with EXO's Pharaoh-as-foreign-emperor pattern. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | 2 occurrences (14:18, 14:19) — both render **ความรักมั่นคง** ✓. **EXCEPTION: 14:18 surrounding character-cluster drifts — see §2.** | **LOCKED-with-§2-flag** |
| `exod_34_attribute_formula_2026-05.md` | **MAJOR DRIFT at Num 14:18 — see §2.** Cross-corpus traceability is broken at the first downstream witness. | **DRIFT (DECIDE)** |
| `nicham_divine_relenting_2026-05.md` | Num 23:19 (לֹא־אִישׁ אֵל ... וְיִתְנֶחָם "God is not a man that he should change his mind") → **เปลี่ยนพระทัย** ✓ matches doc's factive-volitional sub-rendering. Note this is the **doctrinal-negation** form (opposite of Exod 32:14's affirmative "YHWH relented"); the doc handles both. Compliant. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | NUM 14:21 (חַי־אָנִי "as I live"), 14:28 (חַי־אָנִי same formula), 30:3+ (vow-formulas in Num 30:1-16 chapter — נֶדֶר vow-language); NUM 32:10-15 (יְהוָה's oath against the wilderness-generation; recapitulates Deut 1:35 + Ps 95:11 + Heb 3:11). All rendered with the **doc-canonical Thai oath surface**. Compliant. | **LOCKED** |
| `paqad_visit_attend_2026-05.md` | NUM is THE paqad-heavy book — every census-verse uses פָּקַד "muster / number" (chs.1, 3, 4, 26). The doc's **census-vs-judgment-vs-mercy three-way sense-split** is applied: **census-paqad → นับ/ลงทะเบียน** (chs.1-4, 26); **mercy-paqad → เสด็จมาเยี่ยม** (no NUM occurrence in this sense); **judgment-paqad → ลงโทษ** (14:18; Num 14:18's פֹּקֵד עֲוֹן → "ทรงให้ความผิดของบิดาตกถึงบุตรหลาน" — the Sinai-formula context; see §2). Compliant for census; the formula-context drift is captured under §2. | **LOCKED-with-§2-flag** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Hand of YHWH" (NUM 11:23); "Spirit of God" (24:2 — Balaam); "face of YHWH" (6:25-26 ✓ matches §5); "voice of YHWH" (7:89 ✓). All anthropomorphisms compliant. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains pervasive; cognate-accusatives at NUM 31:2 ("avenge the avenging" נָקֹם נְקַם), 6:2 (לִנְדֹּר נֶדֶר "vow a vow"), 30:3 (יִדֹּר נֶדֶר); imperative-of-prohibition pattern in 35:31-33. Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "land flowing with milk and honey" 13:27, 14:8, 16:13+14 → uniform "แผ่นดินที่มีน้ำนมและน้ำผึ้งไหล" ✓; "face/presence" idioms 6:25-27 → พระพักตร์ ✓; "lift up his face" 6:26 → ทรงยกพระพักตร์ ✓; "by the hand of Moses" 4:37+45+49, 33:1 → "ในมือของโมเสส" ✓. Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | MT-vs-English versification divergences at the 16:36-50 / 17:1-15 boundary AND the 29:40 / 30:1 boundary — both Layer-2-footnoted at `output/textual_variants/numbers_{17,30}.json`. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | 1,200+ proper-noun renderings spot-checked: Moses **โมเสส**, Aaron **อาโรน**, Eleazar **เอเลอาซาร์**, Phinehas **ฟีเนหัส**, Balaam **บาลาอัม**, Balak **บาลาค**, Sihon **สิโหน**, Og **โอก**, Korah **โคราห์**, Dathan **ดาธาน**, Abiram **อะบีราม**, Caleb **คาเลบ**, Joshua **โยชูวา**, Zelophehad **เศโลเฟหาด** and his five daughters Mahlah/Noah/Hoglah/Milcah/Tirzah **มาห์ลาห์ โนอาห์ โฮกลาห์ มิลคาห์ ทีรซาห์** ✓; place-names Sinai (mixed **ซีนาย/สีนาย** — see §6), Kadesh **คาเดช**, Hor **โฮร์**, Pisgah **พิสกาห์**, Moab **โมอับ**, Edom **เอโดม**, Bashan **บาชาน**, Heshbon **เฮชโบน**, Jericho **เยรีโค**, Succoth (**สุคคท**, drift from EXO **สุคโคท** — see §7). Most consistent, two flagged. | **LOCKED-with-§6/§7-flag** |
| `proper_noun_wordplay_2026-05.md` | NUM has 7 paronomastic name-etymologies: **Massah and Meribah** (recapitulates Exod 17:7 at NUM 20:13; etymology preserved); **Marah** (NUM 33:8-9 recapitulation); **Beer** (21:16-18, "well" + naming-song); **Suph + Vaheb** (21:14, the "Book of the Wars of YHWH" snippet); **Pi-hahiroth** (33:7-8); **Hor-haggidgad** (33:32); **Iyye-abarim** (33:44). All etymological transparency preserved. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | NUM has the **Levitical-arithmetic tension at 3:39** (sum 22,000 vs. component-sum 22,300) — Layer-2 footer at `output/textual_variants/numbers_03.json` cross-references the **MT puncta extraordinaria** + the LXX harmonization-attempt at 3:39. Also the **Deuel-vs-Reuel** name-variation at 2:14 (vs. 1:14, 7:42, 10:20) — Layer-2 footer present. **LOCKED** ✓ at both witnesses. | **LOCKED** |
| `manah_divine_appointment_2026-05.md` | NUM has no מָנָה appointment-verbs (the OT use of מנה for divine-appointment clusters in Job 7:3, Dan 1:5+10-11, Jonah 1:17+4:6-8). N/A. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | **Baal-Peor** 25:3+5 (Hebrew בַּעַל פְּעוֹר — "Lord of Peor", a Moabite deity) → "**บาอัลของเปโอร์**" ✓; **'their gods'** 25:2 (Moabite-women-incited apostasy) → "**พระทั้งหลายของพวกเขา**" ✓; **'the gods of Egypt'** 33:4 (recapitulates Exod 12:12) → "**พระทั้งหลายของอียิปต์**" ✓. Consistent OT-polytheistic-register usage. | **LOCKED** |
| `ot_polytheistic_register_2026-05.md` | NUM 25:2-3 (Moabite-deities, plural-gods construction); 33:4 (gods-of-Egypt, plural-gods); 22-24 (Balaam invoking-YHWH register from a non-Israelite prophet — note Balaam uses **El, Shaddai, Elyon, YHWH** somewhat interchangeably across his 4 oracles, mirroring his liminal Mesopotamian-diviner-vs-YHWH-instrument identity). The Eremos Thai preserves the Hebrew lemma-distinctions (אֵל → พระเจ้า in 23:22; שַׁדַּי → ผู้ทรงมหิทธิฤทธิ์ in 24:4; עֶלְיוֹן → ผู้สูงสุด in 24:16). Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator royal-Thai for divine acts ✓; speaker-register distinguishes Moses' prophet-voice (humble ข้าพระองค์ to YHWH at 11:11-15, 14:13-19), Aaron's deferential register to Moses (12:11 + 16:46), Balaam's oracle-vs-conversation register-shifts (lower register to Balak's messengers, elevated poetic register in oracles 23-24), foreign-king Balak ตรัส-style. Compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | Aaronic blessing (6:24-26) — see §5; well-song (21:17-18 "spring up, O well, sing to it!") preserves the antiphonal-imperatives. Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative uses wayyiqtol; doc is Greek-NT-specific. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` (NT) | N/A — Numbers is OT. The OT-companion handling is per `mt_vs_lxx_textual_variant_handling_2026-05.md`. | **LOCKED (N/A)** |
| `malak_yhwh_2026-05.md` | **MAJOR DRIFT at Num 22:22-35 + 20:16 (11 occurrences) — see §4.** Forward-cover § from doc unfulfilled. | **DRIFT (DECIDE)** |
| `kapporet_atonement_cover_2026-05.md` | Single NUM occurrence at 7:89 (the divine-voice from above the kapporet between the cherubim) → **พระที่นั่งกรุณา** ✓ matches doc lock. | **LOCKED** |

---

## 16. Pre-existing docs to recommend NEW or AMEND from Numbers

(Following the Exodus-audit-recommendation-template; new recommendations from NUM that didn't already land:)

- **`aaronic_blessing_2026-05.md`** — see §5. Locks the six-clause Thai form, names the חנן rendering choice (พระคุณ or พระเมตตα) for cross-corpus locking, and cross-references the Heb 13:20-21 NT-benediction echo. **NEW.**
- **`sacrificial_vocabulary_2026-05.md`** — see §12. Locks the Thai for the Levitical sacrifices (חַטָּאת, אָשָׁם, עֹלָה, מִנְחָה, שְׁלָמִים, נֶסֶךְ) and the cross-corpus continuity with NT propitiation vocabulary. Forward-protects Leviticus + Hebrews 9-10. **NEW.**
- **`goel_kinsman_redeemer_2026-05.md`** — see §14. Locks **גֹּאֵל → ผู้แก้แค้น/ผู้ไถ่** distinction. Forward-protects Deut 19 + Ruth + Isaiah-redeemer + NT λύτρωσις cluster. **NEW.**
- **`balaam_oracles_2026-05.md`** — see §9. Names the prophetic-poetry register, the messianic-imagery preservation principle, locks cross-references to Rev 22:16 (morning star) + Matt 2:2 (Magi's Bethlehem-star). **NEW.**
- **`divine_names_table_2026-05.md` AMENDMENT** — see §8. Add a "standalone Adonai-as-prayer-vocative-in-YHWH-context" sub-rule (Num 14:17 locking precedent; future occurrences in Pss + Prophets). **AMEND existing.**
- **Script wording-pattern fix** — see §3. Extend `check_divine_names.py`'s detection-pattern set to recognize the post-ch.14 chapter-footer template, OR retroactively normalize the chapters 15-36 footnotes to the original template. **AMEND check script (recommended).**
- **`malak_yhwh_2026-05.md` IMPLEMENTATION** — see §4. The doc's §3 Implementation Checklist forward-cover for Num 22 was unfulfilled at NUM ship. Need to normalize the 11 occurrences + extend `check_phrase_consistency.py` to lock the pattern. **AMEND.**

---

## 17. Num 31:17-18 + 25:6-9 sexual-violence + zealot-execution register — **DECIDE**

**Two morally-difficult passages in close proximity:**

> **25:6-9** (Phinehas spear-execution; ends a divinely-sent plague):
> The Israelite man and the Midianite woman in flagrante; Phinehas takes a spear, follows them into the tent, and pierces both through in one thrust. The plague stops at 24,000 dead. The Eremos Thai preserves the Hebrew text faithfully.
>
> **31:17-18** (Midianite war-booty distribution; following the Balaam-counsel apostasy of 25):
> "And now, kill every male child, and every woman who has known a man by lying with a man, kill. But every female who has not known the lying of a man, keep alive for yourselves."

**The Thai surface** for 31:17-18:
> "และบัดนี้ จงฆ่าเด็กชายทุกคน และหญิงทุกคนที่ได้รู้จักชายด้วยการนอนกับชาย พวกเจ้าจงฆ่า แต่เด็กหญิงทั้งหมดที่ไม่เคยรู้จักการนอนกับชาย จงไว้ชีวิตไว้สำหรับพวกเจ้า"

**Editorial assessment.** The translation surface is **faithful and literal** — the Hebrew imperative-of-prohibition (לֹא תְחַיֶּה) and imperative-of-command (הִרְגוּ) is preserved without softening or euphemism. The Hebrew euphemism for sexual experience (יָדְעוּ מִשְׁכַּב זָכָר "know the lying with a man") is preserved.

**The question is whether a Layer-2 doctrinal footer is warranted** for the Thai reader. Two analogous OT-corpus precedents:
- **Exod 15:11 בָּאֵלִם** (Exodus audit Item C / EXO §14) — `ot_polytheistic_register_2026-05.md` was written to handle the Hebrew-evangelical-register tension on a single verse.
- **Gen 19, 34, 38, 39** (Genesis audit §11) — Genesis-audit STABLE-flagged the morally-difficult content register; the existing doc `divine_object_praise_verbs_2026-04.md` partially addresses but is incomplete.

The Num 31:17-18 command is unique in the OT corpus for its **active divine-sanctioned-by-Moses sexual-violence target** (the explicit captive-virgin-keeping is in the same instruction as the kill-all-non-virgin command). This is a **first-class evangelical-reader interpretive crux** — readers of the Eremos Thai will encounter this and either (a) read it as historically-conditioned warfare-ethics (the standard evangelical-historicist reading), (b) read it as theological-typology (the "kill everything Midianite to prevent recurrence of Baal-Peor" reading), or (c) confront the moral question directly.

**Three resolution paths:**

(a) **Current** — leave as-is. Most-faithful to the Hebrew text's plain surface. Defensible academically; absorbs the reader-interpretive-burden as the standard.

(b) **Layer-2 doctrinal footer** — add an entry to `output/textual_variants/numbers_31.json` naming the **ḥerem (ban) institution in OT warfare** and the **interpretive options** in evangelical-Protestant tradition. Similar pattern to the Gen 6:1-4 Nephilim Layer-2 (preserves the surface; carries the interpretive question in a footer).

(c) **Doc-lift** — write `docs/translator_decisions/ot_warfare_ethics_2026-05.md` (covers Num 21 (Sihon/Og elimination), Num 25 (Phinehas), Num 31 (Midianite war), Deut 7+20+25 (ḥerem ordinances), Josh 6-11 (Conquest narratives), 1 Sam 15 (Saul-and-Amalek)). The doc names the **historicist-conditioning interpretive frame** Ben endorses, preserves textual faithfulness, and locks the Layer-2 footer practice across the OT-warfare cluster.

**DECIDE flag.** Recommend (c) doc-lift — this is the cleanest forward-protection for the largest single class of evangelical-reader-question-prompting OT material. The doc would handle 30+ verses across the Pentateuch + Joshua + 1 Samuel uniformly. Cost: one new corpus-doc; zero verse-edits unless Ben chooses to add Layer-2 footers retroactively. **Severity: HIGH (reader-experience).**

---

## 18. Mechanical (§1) — **all green**

- 36/36 chapters: `output/check_reports/numbers_NN_review.md` + sub-reports ✓
- 36/36 chapters: `output/back_translations/numbers_NN.json` ✓
- 36/36 chapters: `output/textual_variants/numbers_NN.json` present (every chapter contains YHWH; matches Exodus practice for YHWH-rich books)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 260-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `python3 scripts/audit_inclusion_variants.py --book NUM --strict`: N/A (NT-style inclusion-variants policy not applicable for OT; OT-corpus-side handled by `mt_vs_lxx_textual_variant_handling_2026-05.md`)
- `git status output/`: only `output/check_reports/divine_names.md` modified (re-run by audit-time invocation; **29 warnings on NUM** = 7 [C-soft] standalone-Adonai false-positives + 22 [D] post-ch.14 first-occurrence-footnote-wording-drift; see §3 + §8 for analysis; **0 hard fails**). No source-file dirt.
- Hebrew word-spacing **clean for all 36 chapters** ✓
- `thai_literal` is **Thai for all 36 chapters** ✓
- divine_names.md [C-soft] warnings at 3:36+3:37, 4:31+4:32 are **false positives** (אֲדָנִים "bases/sockets" not אֲדֹנָי "Adonai"); 11:28, 12:11, 32:25, 36:2 are **false positives** (אֲדֹנִי "my lord" addressing a human — Moses); only 14:17 is a real standalone-Adonai case (handled at §8 — the script doesn't flag it because YHWH-form is present elsewhere in the verse).

---

## 19. Flagged for Ben's attention

### A. Num 14:18 Sinai-formula DRIFT from corpus-doc — **DECIDE before tagging** (§2)
Retroactively normalize Num 14:18 to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md`. **Critical** — must be done in tandem with the EXO 34 normalization (Exodus-audit Item A). The same Sinai-formula recitation drifts at both verses; both restore in one paired commit.

### B. Num 22:22-35 + 20:16 mal'akh-YHWH cluster DRIFT from corpus-doc — **DECIDE before tagging** (§4)
Normalize 11 occurrences to `ทูตสวรรค์ของ-` form per `malak_yhwh_2026-05.md` §1 lock. The Balaam-donkey is the largest mal'akh-YHWH cluster in the OT; the doc's §3 Implementation Checklist forward-cover for NUM 22 was unfulfilled.

### C. Num 31:17-18 + 25:6-9 sexual-violence + zealot-execution — **DECIDE before tagging** (§17)
Recommend writing `docs/translator_decisions/ot_warfare_ethics_2026-05.md` to name the historicist-conditioning interpretive frame and lock the Layer-2 footer practice across the OT-warfare cluster. Translation surface is faithful; doc-lift is reader-experience protection.

### D. Sinai = ซีนาย/สีนาย mix within NUM — **REVIEW** (§6)
Normalize 10× สีนาย → ซีนาย to match EXO + within-book consistency. Mechanical fix.

### E. Succoth = สุคโคท→สุคคท drift from EXO — **REVIEW** (§7)
Normalize 4× สุคคท → สุคโคท to match EXO. Mechanical fix.

### F. First-occurrence-footnote wording drift in chs.15-36 — **REVIEW** (§3)
Either restore the "ยาห์เวห์ Yahweh" romanization-phrase in chs.15-36 footnotes (22 edits), or update `check_divine_names.py`'s pattern-set to recognize the post-ch.14 marker phrase. Recommend the script-update path.

### G. Num 14:17 standalone Adonai vocative — **REVIEW** (§8)
Doc-amend `divine_names_table_2026-05.md` with a sub-rule for "standalone Adonai-in-prayer-vocative within YHWH-context". The as-shipped Thai is defensible; the doc lock is the principled distinction.

### H. Aaronic blessing recommend doc-lift — **STABLE** (§5)
Write `aaronic_blessing_2026-05.md` locking the six-clause Thai form + the חנן rendering choice + the cross-reference to Heb 13:20-21 NT-benediction.

### I. Sacrificial vocabulary recommend doc-lift — **STABLE** (§12)
Write `sacrificial_vocabulary_2026-05.md` locking the Levitical sacrifice vocabulary. Forward-protects Leviticus + Hebrews 9-10 + the entire cross-corpus atonement-typology cluster.

### J. גֹּאֵל kinsman-redeemer recommend doc-lift — **STABLE** (§14)
Write `goel_kinsman_redeemer_2026-05.md` locking the גָּאַל-family vocabulary. Forward-protects Deut 19 + Ruth + Isaiah's "Redeemer" titles + NT λύτρωσις cluster.

### K. Balaam oracles recommend doc-lift — **STABLE** (§9)
Write `balaam_oracles_2026-05.md` locking the prophetic-poetry register + the Num 24:17 messianic-imagery preservation + cross-references to Rev 22:16 + Matt 2:2.

---

## External AI review (§3 of checklist)

Suggested 6-cluster packet — one cluster per major editorial-decision area:

1. **Sinai-formula cross-corpus cluster** — §2 (Num 14:18 vs. corpus-doc; paired with EXO-audit Item A)
2. **mal'akh-YHWH cross-corpus cluster** — §4 (Num 20:16 + 22:22-35 vs. corpus-doc)
3. **OT-warfare-ethics doctrinal-footer cluster** — §17 (Num 31:17-18 + 25:6-9)
4. **Place-name normalization cluster** — §6 + §7 (Sinai + Succoth drift)
5. **First-occurrence-footnote script-vs-template cluster** — §3
6. **Adonai-vocative doc-amendment cluster** — §8

Sized for ~20K-char free-tier AI ceilings per `scripts/build_external_review_packet.py`.

---

## Counts per status code (TL;DR)

- **LOCKED:** 10 items (§1, §10, §11, §15a-r where compliant, §18)
- **STABLE:** 5 items (§5 Aaronic, §9 Balaam, §12 red-heifer, §13 Sotah, §14 cities-of-refuge)
- **REVIEW:** 4 items (§3 footnote-wording-drift, §6 Sinai mix, §7 Succoth drift, §8 Adonai vocative)
- **DECIDE:** 3 items (§2 Sinai-formula CRITICAL, §4 mal'akh-YHWH HIGH, §17 OT-warfare-ethics HIGH)

**3 DECIDE items block the `book-numbers-v1` tag.**

**5 new translator_decisions docs recommended** (aaronic_blessing, sacrificial_vocabulary, goel_kinsman_redeemer, balaam_oracles, ot_warfare_ethics).

**1 existing translator_decisions doc to amend** (divine_names_table for Adonai-in-prayer-vocative sub-rule). **1 check-script extension** (`check_divine_names.py` pattern-set for post-ch.14 marker).
