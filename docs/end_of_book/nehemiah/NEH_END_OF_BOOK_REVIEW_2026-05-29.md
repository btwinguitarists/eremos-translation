# Nehemiah — End-of-Book Review

**Date:** 2026-05-29
**Scope:** All 13 chapters of Nehemiah (405 verses); `glossary.json`; `docs/translator_decisions/` corpus (~98 docs through the Ezra end-of-book audit).
**Trigger:** NEH 13 shipped (commit `29ee8ef`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Fifteenth OT book in the corpus** and **the second post-exilic / Persian-period book**, immediately following Ezra. Nehemiah inherits Ezra's locks and the Chronicler's locks intact, and it re-exercises every Persian-period surface Ezra introduced — but with one decisive difference: where Ezra's Persian kings appear mostly *inside reported letters*, **Nehemiah opens with the cupbearer standing before Artaxerxes in direct narrated audience (NEH 2:1–9)**, so the foreign-monarch register question Ezra *deferred to its own audit* is here exercised at full intensity in narrator voice — and, as shipped, **Nehemiah resolves it the opposite way Ezra did.** Unlike Ezra, Nehemiah is entirely Hebrew (no Aramaic sections), so the `biblical_aramaic` surface is N/A here.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) substantively pass: 13/13 chapters have green per-chapter reports + back-translations + translations (405 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 691-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (20,630 verses). Two `git`-dirty files are housekeeping, not translation surfaces: `data/versification_map.json` (the NEH divergence entries the ship script does not auto-stage — the known versification-map gotcha; committed with this audit branch) and a regenerated `output/check_reports/divine_names.md` aggregate report. **One real mechanical gap surfaced: `output/textual_variants/nehemiah_10.json` is missing** though ch 10 contains YHWH ×3 (see §16).
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-nehemiah-v1`):
  - **§6 — the foreign-monarch register now diverges across two adjacent, both-shipped Persian-court books.** Nehemiah grants Artaxerxes **full ราชาศัพท์ in narrator voice** (`ทรงส่ง` 2:9, `ทรงแต่งตั้ง` 5:14, `ตรัส` 2:2/2:4/2:6, `พระพักตร์`/`พระทัย`/`พระกรรณ`/`พระองค์` throughout), each verse citing `ot_register_policy_2026-05.md §2.2` ("foreign emperors get ราชาศัพท์"). **Ezra, still shipped and still untagged, withholds `ทรง` from the very same king** (EZR 1:7 `กษัตริย์ไซรัสยังได้นำ…ออกมา`; 6:1 `กษัตริย์ดาริอัสจึงสั่ง…` — plain, commoner register, matching 2 Chr 36:23) — Ezra's audit flagged this as its single DECIDE and *deliberately deferred the corpus decision to "Ezra–Nehemiah–Esther–Daniel" together.* The two books now render **the same emperor (Artaxerxes) inconsistently.** This is the headline: it must be resolved **once, for both books**, before either is tagged. See §6.
  - **§4 — the Exod-34 attribute-formula leitwort drifts at NEH 9:17 (+ 9:31).** The shipped 9:17 reads `…พระเจ้าผู้อภัย ผู้ทรงพระคุณและทรง**เมตตา** ทรง**พระพิโรธ**ช้า และ**เปี่ยม**ด้วยความรักมั่นคง`, but `exod_34_attribute_formula_2026-05.md` **explicitly lists NEH 9:17** with the locked canonical surface `พระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรง**พระเมตตา** ทรง**กริ้ว**ช้า ทรง**บริบูรณ์**ด้วยความรักมั่นคง`. The shipped form breaks the locked thread on two substantive components (`ทรงกริ้วช้า`→`ทรงพระพิโรธช้า`; `ทรงบริบูรณ์ด้วย`→`เปี่ยมด้วย`) plus the forgiveness clause. `check_phrase_consistency.py` missed it because only the embedded chesed token `ความรักมั่นคง` is in its audited locks — not the full formula. This is the same class of drift the formula doc was created to prevent (cf. the Jonah 4:2 `רַב־חֶסֶד` MAJOR-CONCERN flag). See §4.
- **4 items flagged REVIEW** (worth Ben's confirmation; not all tag blockers):
  - **§9 — Persian governor-title is rendered three ways and diverges from Ezra.** `פֶּחָה` (governor) → `เจ้าเมือง` (5:14, 5:18, 2:7, 2:9, 3:7) but `ผู้ว่าราชการ` at 12:26; `תִּרְשָׁתָא` (Tirshatha, the Persian gubernatorial title for Nehemiah) → `ผู้ว่าราชการ` (7:65, 7:69, 8:9, 10:2); **Ezra rendered the satrap Tattenai's `פֶּחָה` as `ผู้ว่าราชการแคว้น`.** Possibly a principled tier (`เจ้าเมือง` = governor of the Judah sub-province vs `ผู้ว่าราชการแคว้น` = satrap of the whole Trans-Euphrates), but 12:26 breaks even the internal pattern. Cross-book harmonization question. See §9.
  - **§15 — MT/LXX (Esdras B) disposition.** Like Ezra, the `textual_variants` files are YHWH-footnote-only (0 inclusion variants); the one MT-vs-parallel decision (the Ezra 2:66 horses+mules line absent in MT NEH 7:68) is documented inline. Below the `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 floor → non-gap, but recommend adding a Nehemiah row recording the Esdras B / 1 Esdras (which carries NEH 7:73–8:12) disposition. See §15.
  - **§16 — missing `textual_variants/nehemiah_10.json`.** Ch 10 has YHWH ×3 (first at 10:30) and renders `องค์พระผู้เป็นเจ้า` ×3, but carries **no** per-chapter first-occurrence Tetragrammaton footnote (chapters 1/5/8/9 all do). The 10:30 `key_decision` documents the convention, but the Layer-2 reader footnote is absent. Mechanical/infra gap — recommend the maintainer add the file. See §16.
  - **§17 — NEH 2:3 `key_decision.rendering` field mismatch.** The shipped verse body uses plain `ข้าพเจ้า` (policy-correct), and the rationale states `ข้าพเจ้า` was chosen over `ข้าพระบาท`, but the `key_decision`'s quoted `rendering` snippet reads `…สีหน้าของข้าพระบาท…`. Stale/mislabeled metadata field, not a translation defect. See §17.
- **Four new corpus docs recommended.** Three are carry-forwards from the Ezra audit that remain **unwritten** (`foreign_monarch_register_2026-05.md` [gated on §6 DECIDE], `god_of_heaven_persian_title_2026-05.md`, `persian_achaemenid_administrative_titles_2026-05.md` [now also covering the §9 governor-title tiers]); one is new and Nehemiah-distinctive (`nehemiah_remember_me_formula_2026-05.md`, §8).
- **External AI review (§3) pending.** Suggested 4-item packet: foreign-monarch register cross-book conflict (§6 DECIDE); Exod-34 formula drift at 9:17 (§4 DECIDE); Persian governor-title harmonization (§9 REVIEW); MT/LXX / Esdras B disposition (§15 REVIEW).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED** (with §16 footnote gap)

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout. **17 surface occurrences** in the verse text across 15 verses, in the 5 chapters whose Hebrew contains יהוה:

| Chapter | `องค์พระผู้เป็นเจ้า` in verse text | YHWH in Hebrew |
|---:|:--:|:--:|
| 1 | 1 (v5) | yes |
| 5 | 1 (v13) | yes |
| 8 | 6 (1, 6×2, 9, 10, 14) | yes |
| 9 | 6 (3×2, 4, 5, 6, 7) | yes |
| 10 | 3 (30, 35, 36) | yes |
| (all others) | 0 | no |
| **Total** | **17** | |

Every Hebrew יהוה is rendered; no over- or under-rendering. **`ยาห์เวห์` residues in verse text: zero** (the one whole-corpus hit is a benign etymological gloss of the personal name *Tobiah* in the 2:10 translator note — `'โทบียาห์' = 'ยาห์เวห์ทรงประเสริฐ'` — not a divine-name residue in rendered Scripture). The monotheism statement at **9:6** `אַתָּה־הוּא יְהוָה לְבַדֶּךָ` → `พระองค์เองทรงเป็นองค์พระผู้เป็นเจ้าผู้เดียว` correctly carries the Shema thread (KD cross-refs Deut 6:4).

**Per-chapter first-occurrence footnote — 4/5, and the gap is real:** chapters 1/5/8/9 each carry the locked `tetragrammaton_convention_first_occurrence` footnote in `output/textual_variants/nehemiah_NN.json`. **Chapter 10 is missing its file** (§16). This is **not** the Ezra-5 case (Ezra 5 was all-Aramaic with zero YHWH and was correctly owed none); ch 10 *has* YHWH and *is* owed a footnote.

**LOCKED** ✓ per `divine_names_table_2026-05.md` — modulo the §16 mechanical gap.

---

## 2. Elohim + standalone Adonai + pagan register — **LOCKED**

- **Elohim → พระเจ้า** uniform (4:9, 5:15, 6:12, 7:2; `אִישׁ הָאֱלֹהִים` 12:24 → `ดาวิดมนุษย์ของพระเจ้า`; `קְהַל הָאֱלֹהִים` 13:1 → `ชุมชนของพระเจ้า`). YHWH+Elohim compounds preserve both elements (8:9 `יְהוָה אֱלֹהֵיכֶם` → `องค์พระผู้เป็นเจ้าพระเจ้าของท่านทั้งหลาย`; 9:7 `יְהוָה הָאֱלֹהִים` → `องค์พระผู้เป็นเจ้า พระเจ้า`).
- **Standalone divine אֲדֹנָי → องค์เจ้านาย** (the form reserved to distinguish standalone Adonai from YHWH per `divine_names_table_2026-05.md`): **1:11** `אָנָּא אֲדֹנָי` → `ข้าแต่องค์เจ้านาย`; **4:8** `אֶת־אֲדֹנָי הַגָּדוֹל וְהַנּוֹרָא זְכֹרוּ` → `จงระลึกถึงองค์เจ้านายผู้ทรงยิ่งใหญ่และน่าเกรงขาม`; **8:10** `לַאֲדֹנֵינוּ` → `แด่องค์เจ้านายของเรา`. The **10:30 compound** `מִצְוֺת יְהוָה אֲדֹנֵינוּ` renders both elements: `องค์พระผู้เป็นเจ้าองค์เจ้านายของข้าพระองค์ทั้งหลาย`. **Note:** ch 9 (the great penitential prayer) contains **no standalone divine Adonai** — its divine name throughout is YHWH (→ `องค์พระผู้เป็นเจ้า`). Human/name false positives correctly *not* treated as divine Adonai: 3:5 `אֲדֹנֵיהֶם` (human "masters" → `นาย`); 7:18 Adonikam; 10:17 Adonijah.
- **Pagan-deity (`เทพเจ้า`) register: none in verse text** — Nehemiah is a wall-rebuilding + covenant-renewal book with no idol-polemic narrative, so the register simply doesn't fire (the only `เทพเจ้า` mention is in the 1:4 KD describing God as supreme over the gods of the Persian empire — commentary, not a rendered title).

**LOCKED** ✓ per `divine_names_table_2026-05.md` + `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` (the last two are N/A-by-content here).

---

## 3. חֶסֶד covenant-love — **LOCKED**

חֶסֶד renders uniformly as `ความรักมั่นคง` (the locked chesed surface) at every occurrence: **1:5** `וָחֶסֶד` → `ความรักมั่นคง`; **9:17** (within the Exod-34 formula, §4) `וְרַב־חֶסֶד` → `…ด้วยความรักมั่นคง`; **9:32** `שׁוֹמֵר הַבְּרִית וְהַחֶסֶד` → `ผู้ทรงรักษาพันธสัญญาและความรักมั่นคง` (KD names the lock + flags it as the leitwort matching Neh 1:5 and Deut 7:9); **13:14** `חֲסָדַי` → `การกระทำแห่งความรักมั่นคง`; **13:22** `כְּרֹב חַסְדֶּךָ` → `ความรักมั่นคงอันยิ่งใหญ่`.

**LOCKED** ✓ per `chesed_covenant_love_2026-05.md`. (The chesed *token* is correct everywhere; the **surrounding Exod-34 formula** at 9:17 nonetheless drifts — see §4.)

---

## 4. Exod-34 attribute formula at NEH 9:17 + 9:31 — **DECIDE (locked-leitwort drift)**

`exod_34_attribute_formula_2026-05.md` locks the Sinai self-revelation formula across all its OT anchors "so the Decalogue formula and the Sinai-revelation formula read as the same canonical text-thread," and its table **explicitly lists NEH 9:17** with the locked surface:

> **Locked (per the doc):** `พระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง`

The **shipped** NEH 9:17 reads:

> **Shipped:** `…แต่พระองค์ทรงเป็นพระเจ้าผู้อภัย ผู้ทรงพระคุณและทรงเมตตา ทรงพระพิโรธช้า และเปี่ยมด้วยความรักมั่นคง พระองค์มิได้ทรงทอดทิ้งพวกเขา`
> (Heb: `אֱלוֹהַּ סְלִיחוֹת חַנּוּן וְרַחוּם אֶרֶךְ אַפַּיִם וְרַב־חֶסֶד`)

The shipped form diverges from the lock on four points, two of them substantive:

| Component | Hebrew | Locked surface | Shipped surface | Severity |
|---|---|---|---|---|
| "God of forgiveness" | אֱלוֹהַּ סְלִיחוֹת | พระเจ้าผู้ทรง**ประทานการ**อภัย | พระเจ้าผู้อภัย | minor |
| "compassionate" | רַחוּם | ทรง**พระ**เมตตา | ทรงเมตตา | minor (missing พระ) |
| **"slow to anger"** | אֶרֶךְ אַפַּיִם | ทรง**กริ้ว**ช้า | ทรง**พระพิโรธ**ช้า | **substantive** |
| **"abounding in chesed"** | רַב־חֶסֶד | ทรง**บริบูรณ์**ด้วยความรักมั่นคง | **เปี่ยม**ด้วยความรักมั่นคง | **substantive** |

**9:31** (the short form `אֵל־חַנּוּן וְרַחוּם`) shipped as `เพราะพระองค์ทรงเป็นพระเจ้าผู้ทรงพระคุณและทรงเมตตา` — `חַנּוּן` → `ทรงพระคุณ` ✓ locked, but `רַחוּם` → `ทรงเมตตา` again drops the `พระ` (locked `ทรงพระเมตตา`). 9:17 and 9:31 are internally consistent with *each other*, but both deviate from the corpus lock.

**Why `check_phrase_consistency.py` passed it:** the checker's audited locks include the chesed token `ความรักมั่นคง` (present and correct here) but **not the full Exod-34 attribute-formula string**, so the `ทรงกริ้วช้า`→`ทรงพระพิโรธช้า` and `ทรงบริบูรณ์ด้วย`→`เปี่ยมด้วย` deviations are invisible to it. This is exactly the gap the Jonah 4:2 `רַב־חֶסֶד` episode (flagged MAJOR CONCERN by external AI, then normalized) warned about.

**DECIDE.** Recommend (a) **normalize NEH 9:17 + 9:31 to the locked canonical surface** so the leitwort thread holds across Exod 34:6 / Num 14:18 / Pss 86:15·103:8·145:8 / Joel 2:13 / Jonah 4:2 / 2 Chr 30:9 / Neh 9:17; and (b) **extend `check_phrase_consistency.py`** to audit the full Exod-34 attribute formula (not just the embedded chesed token) so this category of drift is caught mechanically in future books (Psalms especially). **Severity: MEDIUM** — a real surface defect against a LOCKED doc, but cleanly fixable; the chesed lock itself is intact.

---

## 5. "God of heaven" (אֱלֹהֵי הַשָּׁמַיִם) — **STABLE → recommend `god_of_heaven_persian_title_2026-05.md`** (carry-forward from Ezra §3, still unwritten)

The Persian-period divine self-presentation, here in Nehemiah's opening prayer + the Artaxerxes audience, renders **uniformly `พระเจ้าแห่งฟ้าสวรรค์`**:

| Ref | Source | Thai |
|---|---|---|
| 1:4 | `אֱלֹהֵי הַשָּׁמָיִם` (Nehemiah's prayer) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 1:5 | `יְהוָה אֱלֹהֵי הַשָּׁמַיִם` | `องค์พระผู้เป็นเจ้า พระเจ้าแห่งฟ้าสวรรค์` (both elements rendered) |
| 2:4 | `אֱלֹהֵי הַשָּׁמָיִם` (silent prayer before the king) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 2:20 | `אֱלֹהֵי הַשָּׁמַיִם הוּא יַצְלִיחַ` | `พระเจ้าแห่งฟ้าสวรรค์เองทรงเป็นผู้ที่จะให้เราประสบความสำเร็จ` |

The 1:4 KD documents the post-exilic title rationale. (Other `ฟ้าสวรรค์` hits in ch 9 — 9:6, 9:13, 9:15, 9:23, 9:27, 9:28 — are ordinary "heaven(s)," correctly *not* treated as the divine title.) This is the Ezra audit's §3 recommendation, **still unwritten** — Nehemiah is the second book confirming the uniform surface; the doc should be written now (it forward-covers Daniel 2:18–19, 2:37, 2:44; 5:23).

**STABLE** — no surface defect; documentation/forward-protection. **Severity: LOW.**

---

## 6. Foreign-monarch register (Artaxerxes) — **DECIDE (the headline; cross-book conflict with Ezra)**

This is the register question Ezra **explicitly parked for the Ezra–Nehemiah–Esther–Daniel block.** As shipped, the two books resolve it in **opposite directions for the same emperor**:

| | **Ezra (shipped, untagged)** | **Nehemiah (shipped, this audit)** |
|---|---|---|
| Persian king as **narrator-voice subject** | **No `ทรง`** — commoner register, matching 2 Chr 36:23. EZR 1:7 `กษัตริย์ไซรัสยังได้นำ…ออกมา`; 6:1 `กษัตริย์ดาริอัสจึงสั่งให้ค้น` | **Full ราชาศัพท์** — `ทรงส่ง` (2:9), `ทรงแต่งตั้ง` (5:14), `ตรัส` (2:2/2:4/2:6), `ประทาน` (2:8), royal nouns `พระพักตร์`/`พระทัย`/`พระเนตร`/`พระกรรณ`/`พระองค์`/`พระราชสาส์น` throughout |
| Stated rationale | "deferred to the Ezra end-of-book review" (1:2 note) | every verse cites **`ot_register_policy §2.2`** ("foreign emperors get ราชาศัพท์ in narrator voice") |
| Queen | (no queen scene) | 2:6 `הַשֵּׁגַל` → `พระมเหสี…ประทับ` (full royal) |

**Both books are shipped, neither is tagged** (`git tag` shows no `book-ezra-v1` / `book-nehemiah-v1`), and **Ezra has not been normalized** (EZR 1:7/6:1 still plain). So a reader moving from Ezra 7 (Artaxerxes commissioning Ezra, plain register) to Nehemiah 2 (Artaxerxes commissioning Nehemiah, full `ทรง`) meets the *same king* rendered two different ways across a book boundary.

The tension is real at the policy level too: **`ot_register_policy §2.2` actually supports Nehemiah** — its table row says "Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, Darius, Xerxes) → ราชาศัพท์ (ทรง)… even if villainous." Ezra's shipped surface is the one that *contradicts* the written table (it followed the 2 Chr 36:23 commoner-register precedent instead). So the cleanest reading is: **Nehemiah is policy-compliant; Ezra is the outlier** — but that is precisely the corpus decision Ezra deferred, and it has never been ratified.

**One part is already clean and consistent across both books:** **Nehemiah himself** (cupbearer + governor) is held in **plain register** in narrator voice exactly as `ot_register_policy §2.5` (the Joseph-vizier sub-rule, which names Nehemiah explicitly) requires — `ข้าพเจ้า` + plain verbs as governor (5:14–19) and reformer (13:8 `ขุ่นเคือง`/`เหวี่ยง`; 13:25 `ทุบตี`/`ดึงผม`); elevated `ข้าพระองค์` appears only when he addresses **God** in prayer (the correct humble-before-deity register, not self-elevation). The 1:11 note states the rule verbatim: imperial ราชาศัพท์ for Artaxerxes does **not** extend to the Hebrew servant-official. **§2.5 compliance is LOCKED;** the DECIDE is only about the *emperor's* register.

**DECIDE.** The audit changes nothing and recommends Ben **ratify one rule for the whole Persian-court block** and then **normalize whichever book diverges**:
- **Option A (recommended): ratify §2.2 as written — foreign emperors get full ราชาศัพท์ in narrator voice.** Keep Nehemiah as-is; **normalize Ezra's Persian-king narrator verbs to `ทรง`** (a bounded set: EZR 1:7, 3:7, 6:1, and the handful of other narrator-subject king verbs). This is the smaller edit and aligns the corpus with the written policy.
- **Option B: ratify the Ezra two-tier split (narrator-no-`ทรง` / in-address-deferential).** Then **normalize Nehemiah's narrator king-verbs** (2:2/2:4/2:6/2:9, 5:14, plus the royal nouns) and **amend §2.2** to reflect the commoner-register choice for Gentile emperors.

Either way: **write `foreign_monarch_register_2026-05.md`** (or amend `ot_register_policy §2.2`) so Esther (Ahasuerus, *the* central royal figure) and Daniel (Nebuchadnezzar/Belshazzar/Darius/Cyrus) inherit a single written rule. **Severity: MEDIUM-HIGH** — no theological stakes, but it is a now-*visible* cross-book inconsistency on a shared character, and it gates the register handling of every remaining Persian/Babylonian-court book. This decision should be made jointly with the Ezra tag.

---

## 7. Nehemiah-as-cupbearer/governor plain register — **LOCKED**

Covered under §6: per `ot_register_policy §2.5`, the narrator never grants Nehemiah `ทรง` or royal forms; he is plain throughout (1:11, 2:1, 5:14–19, 13). His humble first-person `ข้าพระองค์` + vocative `ข้าแต่…` + self-designation `ผู้รับใช้ของพระองค์` are reserved for addressing God (1:5–11; 5:19; 6:9; 13:14/22/31). No over-elevation found. **LOCKED** ✓ per `ot_register_policy_2026-05.md §2.5` + `honorifics_non_divine_authorities_2026-04.md`.

---

## 8. The "Remember me, O my God" memoir formula — **STABLE → recommend `nehemiah_remember_me_formula_2026-05.md`** (new, NEH-distinctive)

Nehemiah's first-person signature — `זָכְרָה־לִּי אֱלֹהַי` ("Remember me, O my God") — is the book's distinctive editorial fingerprint, recurring 6× with a **uniform Thai frame** `ข้าแต่พระเจ้าของข้าพระองค์ ขอทรงระลึกถึง [object]`:

| Ref | Hebrew | Object | Thai tail |
|---|---|---|---|
| 5:19 | זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה | me | `…ระลึกถึงข้าพระองค์ในทางที่ดี` |
| 6:14 (imprecatory) | זָכְרָה אֱלֹהַי לְטוֹבִיָּה וּלְסַנְבַלַּט | the enemies | `…ระลึกถึงโทบียาห์และสันบาลลัท ตามการกระทำเหล่านี้` |
| 13:14 | זָכְרָה־לִּי אֱלֹהַי עַל־זֹאת | me | `…ระลึกถึงข้าพระองค์ในเรื่องนี้` |
| 13:22 | גַּם־זֹאת זָכְרָה־לִּי אֱלֹהַי וְחוּסָה עָלַי | me | `…ระลึกถึงข้าพระองค์ในเรื่องนี้ด้วย และโปรดเมตตาข้าพระองค์` |
| 13:29 (imprecatory) | זָכְרָה לָהֶם אֱלֹהָי | the priests | `…ระลึกถึงพวกเขา` |
| 13:31 | זָכְרָה־לִּי אֱלֹהַי לְטוֹבָה | me | `…ระลึกถึงข้าพระองค์ในทางที่ดี` |

The frame is invariant; the Thai **fronts the vocative** ahead of the petition (Hebrew is `zokrah-li Elohai`, petition-first); the `לְטוֹבָה` tail renders identically at the 5:19 / 13:31 inclusio bookends as `ในทางที่ดี`; and the positive/imprecatory object-swap (`ข้าพระองค์` → the named enemies / `พวกเขา`) is handled cleanly where the Hebrew drops the `-li` suffix. The pronoun is consistently the humble `ข้าพระองค์`.

The one gap is documentation: **3 of 6 instances (6:14, 13:22, 13:29) carry no `key_decision` on the formula** (13:22's KD is chesed-only), so the lock currently lives as uneven inline prose. This clears the bar for a dedicated doc capturing the frame, the vocative-fronting rule, the `ข้าพระองค์` register, and the favorable/imprecatory object-swap. The formula is unique to Nehemiah in the OT (it has no forward-compounding worry), so the doc is lower-priority than the Persian-block docs — but it is the cleanest "uniform-but-undocumented" item in the book.

**STABLE** — uniform and principled; recommend the doc as polish. **Severity: LOW.**

---

## 9. Persian administrative titles + "Beyond the River" — **STABLE (Beyond-the-River) + REVIEW (governor-title tier)** → recommend `persian_achaemenid_administrative_titles_2026-05.md` (carry-forward from Ezra §6)

**Compliant / uniform:**
- **"Beyond the River" (עֵבֶר הַנָּהָר) → `(แคว้น)ฟากตะวันตกของแม่น้ำยูเฟรติส`** — uniform across 2:7, 2:9, 3:7, matching Ezra's descriptive policy exactly. The 2:7 KD documents the descriptive expansion (cites ESV/NIV/CSB). ✓
- **King's letters אִגְּרוֹת → `พระราชสาส์น`** (2:7–9); **the king's forest פַּרְדֵּס → `พระอุทยานของกษัตริย์`** (2:8, KD notes the Persian *paridaida* → "paradise" etymology); **daric דַּרְכְּמֹנִים → `ดาริค`**, **mina מָנִים → `มินา`** (transliterated units). ✓

**REVIEW — governor-title is rendered three ways:**

| Hebrew | Thai | Refs |
|---|---|---|
| פֶּחָה (governor, of Nehemiah) | **เจ้าเมือง** | 5:14, 5:18, 2:7, 2:9, 3:7 |
| פֶּחָה (governor, of Nehemiah) | **ผู้ว่าราชการ** | 12:26 |
| תִּרְשָׁתָא (Tirshatha, Nehemiah's Persian title) | **ผู้ว่าราชการ** | 7:65, 7:69, 8:9, 10:2 |
| פֶּחָה (satrap Tattenai) — **Ezra** | **ผู้ว่าราชการแคว้น** | EZR 5:3, 5:6, 6:6, 6:13 |

There may be a defensible tier here (`เจ้าเมือง` = governor of the Judah sub-province; `ผู้ว่าราชการแคว้น` = satrap of the whole Trans-Euphrates), in which case Nehemiah's default `เจ้าเมือง` is correct and *Ezra* sets the satrap level — but **12:26 calls Nehemiah `ผู้ว่าราชการ` (not `เจ้าเมือง`)**, breaking even the internal pattern, and `תִּרְשָׁתָא` is silently collapsed into `ผู้ว่าราชการ` with no KD on the transliterate-vs-translate choice. `check_key_term_consistency.py` is clean, which means `פֶּחָה`/`תִּרְשָׁתָא` are not registered key terms — so this variance is invisible to the mechanical gate. Recommend Ben confirm the intended tier and normalize 12:26 (and decide whether Tirshatha warrants a distinct surface), then capture the full Persian-title set in the recommended doc (which also forward-covers Esther/Daniel).

**STABLE** (Beyond-the-River) / **REVIEW** (governor-title tier). **Severity: LOW-MEDIUM.**

---

## 10. "Hand of God" anthropomorphism (יַד אֱלֹהַי הַטּוֹבָה) — **LOCKED**

The Ezra–Nehemiah providence leitwort "the good hand of my God upon me" renders within `divine_anthropomorphism_thai_grammar_2026-05.md`'s body-part rule — royal noun `พระหัตถ์`, **verb without `ทรง`** because the grammatical subject is the body-part: **2:8** `כְּיַד־אֱלֹהַי הַטּוֹבָה עָלַי` → `พระหัตถ์อันโอบเอื้อของพระเจ้าของข้าพเจ้าที่อยู่กับข้าพเจ้า` (and 2:18, same form). The 2:8 NOTE explicitly tracks the chain across both books (EZR 7:6, 7:9, 7:28, 8:18, 8:22, 8:31 → NEH 2:8, 2:18). (The 2:9 NOTE also documents the deliberate contrast — Nehemiah *accepts* a royal military escort, where Ezra 8:22 refused one.)

**LOCKED** ✓ per `divine_anthropomorphism_thai_grammar_2026-05.md` + `honorifics_non_divine_authorities_2026-04.md`. This is the body-part-before-`ทรง` rule recorded in the 2 Kings honorifics work, holding here as in Ezra §7.

---

## 11. Chapter 7 returnee list ≈ Ezra 2 — **STABLE**

The independent-MT discipline holds, with the synoptic relationship documented: **7:5** NOTE ("the same list as Ezra 2:1–70, with minor numeric differences"); **7:7** NOTE (cross-ref Ezra 2:2; distinguishes the Nehemiah-in-the-list from the author); **7:68** (MT; = English 7:69) KD+NOTE document that the Ezra 2:66 "horses 736 + mules 245" line is **absent in MT NEH 7** and that Eremos follows MT (MT NEH 7 = 72 verses vs English 73) rather than re-importing it from Ezra. **One small documentation gap:** the grand total **7:66 = 42,360** is preserved per MT (correct) but the well-known internal discrepancy (the listed group sums fall short of 42,360 — a tension shared with Ezra 2:64) is **not** flagged in any KD/note, where Ezra's audit found the parallel Ezra 2:64 *was* annotated. Minor — recommend a one-line note at 7:66 for parity with Ezra.

**STABLE** ✓ per `synoptic_parallel_passages_2026-05.md`. (The Cyrus≈Ezra duplication watch is an Ezra matter; Nehemiah's parallel is the returnee roster.)

---

## 12. "Until this day" leitwort — **LOCKED**

The etiological/temporal "this day" idiom occurs twice, both rendered with the locked **`จนถึงทุกวันนี้`**: **9:10** `וַתַּעַשׂ־לְךָ שֵׁם כְּהַיּוֹם הַזֶּה` → `…ทรงทำให้พระนามของพระองค์เป็นที่รู้จักจนถึงทุกวันนี้`; **9:32** `…מִימֵי מַלְכֵי אַשּׁוּר עַד הַיּוֹם הַזֶּה` → `…ตั้งแต่สมัยของกษัตริย์อัสซีเรียจนถึงทุกวันนี้`. Both comply with the corpus rendering established when the 2 Kings audit reversed the 1 Samuel outlier to `จนถึงทุกวันนี้`.

**LOCKED** ✓ per `leitwort_handling_policy_2026-05.md`.

---

## 13. Divine Spirit (רוּחַ) — **STABLE**

The two divine-Spirit references in the ch 9 prayer render with the elevated `พระวิญญาณ` register: **9:20** `וְרוּחֲךָ הַטּוֹבָה` → `พระวิญญาณอันดีของพระองค์` (KD: one of the OT texts naming the Holy Spirit directly); **9:30** `וַתָּעַד בָּם בְּרוּחֲךָ בְּיַד־נְבִיאֶיךָ` → `พระวิญญาณของพระองค์ทรงตักเตือนพวกเขาผ่านทางบรรดาผู้พยากรณ์ของพระองค์` (royal `ทรง` on the verb, God being the subject). Consistent and theologically apt. **STABLE** — no doc needed unless `spirit_of_yhwh_empowerment_2026-05.md` wants the post-exilic instruction-Spirit datapoints added.

---

## 14. Versification divergences (MT numbering) — **STABLE**

All translation files use **MT numbering**, and the divergences are mapped:

| Ch | File range | MT-expected | English equivalent |
|---|---|---|---|
| 3 | 1–38 | MT ends 3:38 | = English 4:1–6 |
| 4 | 1–17 | MT 4:1–17 | = English 4:7–23 |
| 7 | 1–72 | MT 7:1–72 (one fewer verse) | = English 7:1–73 |
| 9 | 1–37 | MT ends 9:37 | English 9:38 = MT 10:1 |
| 10 | 1–40 | MT 10:1–40 | = English 9:38 + 10:1–39 |

The seam chapters 7 and 9→10 carry per-verse NOTEs ("this is NEH 7:70/…/10:1 in the English/BSB"); the **3/4 seam relies only on `data/versification_map.json`** (no per-verse note), a minor annotation asymmetry. The map and the files are mutually consistent. **Housekeeping:** `data/versification_map.json` (`_total_entries` 1122 → 1190; +68 NEH `diverges:true` entries with `lxx_ref` = Esdras B offsets) was **uncommitted** at audit start — the known ship-script gotcha (`ship_chapter.sh` doesn't stage the map); **committed with this audit branch.**

**STABLE** ✓ per `verse_schema_and_versification_2026-05.md`. (Optional polish: add a 3:33 / 4:1 per-verse divergence note for parity with the 7 and 9→10 seams.)

---

## 15. MT/LXX disposition (Esdras B) — **REVIEW (non-gap; add doc row)**

The `output/textual_variants/nehemiah_*.json` files (1, 5, 8, 9 only) contain **exclusively** the per-chapter YHWH first-occurrence footnote — **zero** inclusion-variant / MT-vs-LXX entries — and there is no `audit_inclusion_variants` candidate. For verse-level MT/LXX divergence this is correct and matches the §2.3-floor disposition Ezra settled. The one MT-vs-parallel decision (the Ezra 2:66 horses+mules line absent in MT NEH 7:68) is documented inline (§11), not as a textual-variant entry. The LXX situation (Esdras B = Greek Ezra–Nehemiah, close to MT; **1 Esdras** carries only NEH 7:73–8:12, the Ezra-reads-the-Law scene) is recorded structurally in the versification map's `lxx_ref` fields. Like Ezra, Nehemiah sits below the disclosure floor → non-gap.

**REVIEW.** Recommend adding a **Nehemiah row** to `mt_vs_lxx_textual_variant_handling_2026-05.md` recording the Esdras B / 1 Esdras disposition (a parallel recension, not an MT variant; no per-verse disclosure owed). No surface change. **Severity: LOW.** Good external-AI item.

---

## 16. Missing `textual_variants/nehemiah_10.json` (YHWH footnote gap) — **REVIEW (mechanical/infra)**

Chapter 10 contains YHWH in 3 verses (10:30, 10:35, 10:36 — first occurrence 10:30, which is also the `יְהוָה אֲדֹנֵינוּ` compound) and renders `องค์พระผู้เป็นเจ้า` ×3, but **no `output/textual_variants/nehemiah_10.json` exists**, so the Layer-2 per-chapter first-occurrence Tetragrammaton footnote that chapters 1/5/8/9 all carry is absent. The 10:30 `key_decision` documents the convention at verse level, so a scholar reading for the underlying Hebrew is not stranded — but the reader-facing footnote is missing. The per-chapter automated check is green (it does not enforce footnote presence), which is why this slipped through.

**REVIEW.** Recommend the maintainer add `nehemiah_10.json` with a `tetragrammaton_convention_first_occurrence` footnote at v30 (mirroring chapters 1/5/8/9) **before the v1 tag**. This is infrastructure, not a translation surface, so it is outside the audit's no-edit mandate to write, but it should be closed before tagging. **Severity: LOW.**

---

## 17. NEH 2:3 `key_decision` rendering-field mismatch — **REVIEW (data integrity)**

At the pivotal audience verse 2:3, the **shipped `thai` body** reads `…สีหน้าของข้าพเจ้าจะไม่เศร้าหมอง` (plain `ข้าพเจ้า` — policy-correct per §6/§2.5), and the KD **rationale** states `ข้าพเจ้า` was deliberately chosen over the deferential `ข้าพระบาท`. But the same KD's quoted **`rendering` field** reads `…สีหน้าของข้าพระบาท…` — i.e., the snippet contradicts both the rationale and the shipped text. This is a stale/mislabeled metadata field, **not** a translation defect (the verse ships correctly). Worth a cleanup pass since 2:3 is the verse external reviewers will scrutinize for the §6 register question.

**REVIEW.** Recommend correcting the 2:3 KD `rendering` snippet to match the shipped `ข้าพเจ้า` form. **Severity: LOW.**

---

## 18. Inherited corpus locks — all compliant except where flagged

| Doc | NEH evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH 17 surfaces, 0 ยาห์เวห์, footnotes 1/5/8/9 — **ch 10 gap §16**); §2 (Elohim, standalone Adonai → องค์เจ้านาย, 10:30 compound). | **LOCKED** (modulo §16) |
| `chesed_covenant_love_2026-05.md` | §3 — ความรักมั่นคง at 1:5, 9:17, 9:32, 13:14, 13:22. | **LOCKED** |
| `exod_34_attribute_formula_2026-05.md` | §4 — 9:17 + 9:31 drift from the locked surface (`ทรงพระพิโรธช้า`/`เปี่ยมด้วย` vs locked `ทรงกริ้วช้า`/`ทรงบริบูรณ์ด้วย`). | **DECIDE-§4** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | §10 — "hand of God" body-part rule held at 2:8/2:18 (พระหัตถ์ + verb without ทรง). | **LOCKED** |
| `ot_register_policy_2026-05.md` §2.2 / `honorifics_non_divine_authorities_2026-04.md` | §6 — foreign-emperor register: NEH grants full ราชาศัพท์ (per §2.2); **Ezra withholds it** → cross-book conflict. | **DECIDE-§6** |
| `ot_register_policy_2026-05.md` §2.5 | §7 — Nehemiah-as-cupbearer/governor held plain throughout; ข้าพระองค์ only toward God. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | §12 — "until this day" → จนถึงทุกวันนี้ (9:10, 9:32). | **LOCKED** |
| `synoptic_parallel_passages_2026-05.md` | §11 — NEH 7 ≈ Ezra 2, MT preserved, divergence documented (7:5/7:7/7:68); minor 7:66 sum gap. | **LOCKED** (minor note) |
| `proper_names_and_transliteration_2026-05.md` | Persian royal/official names + the wall-builder (ch 3) and returnee (ch 7) rosters; `check_key_term_consistency.py` clean across the 691-chapter corpus. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §15 — §2.3 floor → non-gap; add Esdras B / 1 Esdras row → REVIEW. | **LOCKED-with-§15-REVIEW** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §13 — divine Spirit 9:20/9:30 → พระวิญญาณ (instruction/warning, not empowerment-idiom). | **STABLE / N/A** |
| `dtr_history_cycle_formulas_2026-05.md` | **N/A** — post-exilic; no regnal-evaluation cycle. The 2CH "did evil" drift does not recur. | **N/A** |
| `malak_yhwh_2026-05.md` | **N/A** — no מַלְאָךְ (divine or human) in Nehemiah. | **N/A** |
| `hebrew_oath_formulas_2026-05.md` | חַי־יְהוָה absent; the covenant-oath (ch 10) uses אָלָה/שְׁבוּעָה (10:30 → curse-oath to walk in the Law), not the חַי־יְהוָה formula. | **N/A** |
| `biblical_aramaic` (Ezra-recommended, unwritten) | **N/A** — Nehemiah is entirely Hebrew; no language switch. | **N/A** |

---

## 19. Mechanical (§1) — green with two housekeeping items + one infra gap

- 13/13 chapters: `output/check_reports/nehemiah_NN_review.md` — all "✅ Ready to ship" ✓
- 13/13 chapters: `output/back_translations/nehemiah_NN.json` ✓
- 13/13 chapters: `output/translations/nehemiah_NN.json` (405 verses) ✓
- 4 chapters: `output/textual_variants/nehemiah_NN.json` (YHWH first-occurrence footnote: 1, 5, 8, 9). **Chapter 10 missing though it has YHWH ×3 — §16.**
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (691-chapter corpus). *(Note: `פֶּחָה`/`תִּרְשָׁתָא` are not registered key terms, so the §9 governor-title variance is invisible to this check.)*
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (20,630 verses). *(Note: the full Exod-34 attribute formula is **not** an audited lock — only the embedded chesed token — which is why the §4 drift was not caught; recommend extending the checker.)*
- `export_to_usfm.py --book NEH`: **N/A** — the script's `BOOKS` table is NT-only; OT USFM export remains the carried-over separate concern noted in every prior OT audit.
- **Book-code registration:** confirm `NEH` is present in the §3/§4 tooling slug tables (`build_external_review_packet.py` `BOOKS`; `audit_items_to_yaml.py` `BOOK_SLUGS`) before running them — per the EOB book-code-registration gotcha (Ezra had to be registered during its audit).
- `git status output/`: clean **except `output/check_reports/divine_names.md`** — an aggregate report whose only diff is the YHWH-chapter counters (report-only, not a translation surface; identical in kind to the note carried in every prior OT audit). `data/versification_map.json` (the NEH divergence entries) is the other dirty file — housekeeping, committed with this branch.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **17**. `ยาห์เวห์` residues: **zero**. Aramaic verses: **zero** (Nehemiah is all-Hebrew).

**Severity: GREEN** (substantive checks clean; the §4 drift and §16 gap are real but were below the mechanical-gate's coverage, hence this audit).

---

## 20. Flagged for Ben's attention

### DECIDE (block the `book-nehemiah-v1` tag until resolved)

**A. Foreign-monarch register cross-book conflict (§6).** Nehemiah grants Artaxerxes full ราชาศัพท์ in narrator voice (per `ot_register_policy §2.2`); **Ezra (still shipped, still untagged) withholds it from the same king.** Ratify **one** rule for the Persian-court block and normalize whichever book diverges. **Recommended: Option A** — keep Nehemiah (it follows the written §2.2), normalize Ezra's Persian-king narrator verbs to `ทรง`, and write `foreign_monarch_register_2026-05.md`. Decide **jointly with the Ezra tag.** Nehemiah-the-cupbearer's own plain register (§2.5) is clean and not in question. **MEDIUM-HIGH.**

**B. Exod-34 attribute-formula drift at NEH 9:17 + 9:31 (§4).** Shipped 9:17 (`ทรงพระพิโรธช้า` / `เปี่ยมด้วยความรักมั่นคง` / `พระเจ้าผู้อภัย`) deviates from the LOCKED `exod_34_attribute_formula_2026-05.md` surface (`ทรงกริ้วช้า` / `ทรงบริบูรณ์ด้วยความรักมั่นคง` / `พระเจ้าผู้ทรงประทานการอภัย`), breaking the canonical leitwort thread. **Recommend: normalize 9:17 + 9:31 to the locked form + extend `check_phrase_consistency.py` to audit the full formula.** **MEDIUM.**

### REVIEW (worth Ben's confirmation; §9/§16 close before tag, §15/§17 optional)

**C. Persian governor-title harmonization (§9).** `פֶּחָה` → `เจ้าเมือง` (5×) vs `ผู้ว่าราชการ` (12:26); `תִּרְשָׁתָא` → `ผู้ว่าราชการ`; Ezra used `ผู้ว่าราชการแคว้น` for the satrap. Confirm the intended tier, normalize 12:26, decide Tirshatha's surface; capture in `persian_achaemenid_administrative_titles_2026-05.md`. **LOW-MEDIUM.**

**D. MT/LXX (Esdras B) disposition (§15).** Add a Nehemiah row to `mt_vs_lxx_textual_variant_handling_2026-05.md` (parallel recension, non-gap). **LOW.**

**E. Missing `textual_variants/nehemiah_10.json` (§16).** Add the ch-10 YHWH first-occurrence footnote (ch 10 has YHWH ×3, first at 10:30) before the tag. **LOW.**

**F. NEH 2:3 KD `rendering`-field mismatch (§17).** Correct the stale snippet (`ข้าพระบาท` → shipped `ข้าพเจ้า`). **LOW.**

### New translator_decisions docs recommended

1. **`foreign_monarch_register_2026-05.md`** (§6) — gated on the DECIDE; carry-forward from the Ezra audit (still unwritten). The single highest-value forward-protection doc — Esther + Daniel inherit it.
2. **`god_of_heaven_persian_title_2026-05.md`** (§5) — carry-forward from Ezra §3; lock `พระเจ้าแห่งฟ้าสวรรค์`. Forward-covers Daniel.
3. **`persian_achaemenid_administrative_titles_2026-05.md`** (§9) — carry-forward from Ezra §6; the title set + "Beyond the River" + the §9 governor-tier resolution.
4. **`nehemiah_remember_me_formula_2026-05.md`** (§8) — new; locks the `ขอทรงระลึกถึง` memoir frame. Lower priority (no forward-compounding).

### Existing docs to amend (optional, no tag block)
- **`ot_register_policy_2026-05.md §2.2`** — fold in / point to the §6 foreign-monarch decision.
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the Nehemiah Esdras B row (§15).
- **`synoptic_parallel_passages_2026-05.md`** — record NEH 7 ≈ Ezra 2 (§11) as the downstream test of the independent-MT principle.
- **`exod_34_attribute_formula_2026-05.md`** — once 9:17/9:31 are normalized, mark NEH 9:17 verified in the `## Corpus-verified shipped forms` section.

### External AI review (§3 of checklist) — pending
Recommended 4-item packet (see `external_review_items_NEH.md`):
1. **Foreign-monarch register cross-book conflict** (§6-A, DECIDE)
2. **Exod-34 attribute-formula drift at 9:17** (§4-B, DECIDE)
3. **Persian governor-title harmonization** (§9-C, REVIEW)
4. **MT/LXX / Esdras B disposition** (§15-D, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI/1CH/2CH/EZR pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 7 items (§1 YHWH, §2 Elohim/Adonai, §3 chesed, §7 Nehemiah-plain-register, §10 hand-of-God, §11 NEH 7≈Ezra 2, §12 until-this-day; + inherited locks via §18)
- **STABLE:** 4 items (§5 "God of heaven" [→ recommend doc], §8 Remember-me formula [→ recommend doc], §9 Beyond-the-River, §13 divine Spirit, §14 versification)
- **REVIEW:** 4 items (§9 governor-title, §15 MT/LXX row, §16 ch-10 footnote gap, §17 2:3 KD mismatch)
- **DECIDE:** 2 items (§6 foreign-monarch register cross-book conflict; §4 Exod-34 formula drift)

**Two DECIDE items block the `book-nehemiah-v1` tag.** Unlike Ezra's single clean policy-ratification DECIDE, **Nehemiah's two DECIDEs are both surface-actionable**: §6 is a now-visible cross-book inconsistency (and is best resolved jointly with the Ezra tag, since Ezra deferred the same question); §4 is a concrete drift from a LOCKED corpus doc.

**Four new translator_decisions docs recommended** (three carry-forward from Ezra, one new). **Four optional existing-doc amendments.**

---

## Recommendation

**Nehemiah ships in good shape — its inherited locks hold (YHWH, Elohim/Adonai, chesed, hand-of-God anthropomorphism, until-this-day leitwort, Nehemiah's own plain register, transliteration all LOCKED), and its Persian-period surfaces (God of heaven, Beyond the River, the returnee roster) are uniform and verse-documented.** But it carries **two real DECIDEs** that the per-chapter checks could not see:

- **§6 is the headline and is bigger than a single-book question.** Ezra deliberately deferred the Gentile-emperor register decision to be settled across "Ezra–Nehemiah–Esther–Daniel," and Nehemiah has now answered it (full ราชาศัพท์, per the written §2.2) in the opposite direction from Ezra's shipped surface (no `ทรง`). Both books are shipped and untagged. **The decision must be made once, applied to both, and written down before either is tagged.** The recommended resolution (ratify §2.2, normalize Ezra, write the doc) is the smaller edit and aligns the corpus with its own policy.
- **§4 is a clean, fixable drift** from the LOCKED Exod-34 attribute formula at the single most theologically weighty verse of Nehemiah's penitential prayer — exactly the leitwort-thread break that doc exists to prevent, missed only because the phrase-checker audits the chesed token but not the full formula.

**The remaining work is light:** the §9 governor-title tier and the §16 ch-10 footnote should be closed before the tag; §15 and §17 are optional; and the three carry-forward Persian-block docs (foreign-monarch, God-of-heaven, Persian-titles) should be written now — they are overdue from Ezra and forward-protect Esther and Daniel.

**Tag `book-nehemiah-v1` after:**
1. Ben's decision on the **§6 foreign-monarch register** (ratify + doc + normalize the diverging book) — **jointly with the Ezra tag.**
2. Ben's decision on the **§4 Exod-34 formula** (normalize 9:17 + 9:31 + extend the phrase checker).
3. The **§9 governor-title** confirmation/normalization and the **§16 ch-10 footnote** addition.
4. External AI sanity-check (the 4-item packet).
5. The three carry-forward Persian-block docs written (the Nehemiah Remember-me doc is optional polish).

**The single highest-value forward-protection step is the §6 register decision** — it has been open since Ezra, it is now a visible cross-book inconsistency, and it governs every remaining book of the Persian/Babylonian court.
