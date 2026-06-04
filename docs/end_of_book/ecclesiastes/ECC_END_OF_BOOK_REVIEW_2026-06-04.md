# Ecclesiastes — End-of-Book Review

**Date:** 2026-06-04
**Scope:** All 12 chapters (222 MT verses; verse-level `key_decisions` throughout); `glossary.json`; existing `docs/translator_decisions/` (97 docs).
**Trigger:** ECC 12 shipped (commit `7c729260`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **16 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 12/12 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-948-chapter corpus; `check_phrase_consistency.py` clean across all 38 audited locks. `git status output/` shows only the pre-existing `divine_names.md` counter drift (YHWH-chapters 1→0, which is *correct* for Ecclesiastes — see §12) and an untracked `.claude/`; no ECC-source dirt.
- **Ecclesiastes is the FIRST Wisdom book the project has shipped with a single dominant leitwort carried by a provisional rendering.** הֶבֶל (*hevel*) appears in **30 verses** (≈38 tokens with in-verse repeats) and is rendered uniformly **ไร้แก่นสาร** — but that rendering shipped **PROVISIONAL** pending a reader-panel verdict Ben solicited from two Thai friends (2026-06-03). This is the single item blocking the `book-ecclesiastes-v1` tag.
- **Ecclesiastes is also the FIRST OT book in the corpus with no Tetragrammaton at all** — God is named only by אֱלֹהִים / הָאֱלֹהִים → พระเจ้า. No first-occurrence YHWH footnote is owed, and the divine-names checker's "0 chapters with YHWH" is the correct state, not a regression (§12).
- **8 book-wide term locks are STABLE and uniform** across all 12 chapters (ภายใต้ดวงอาทิตย์ ×29, การไล่ตามลม ×9, ประโยชน์, ตรากตรำ, ส่วนแบ่ง, the carpe-diem refrain ×5, ข้าพเจ้า 1st-person, plain-กล่าว Qoheleth voice). Two of these (the **Qoheleth persona/register** and the **carpe-diem refrain shape**) carry no corpus doc and are recommended for lift.
- **6 inherited corpus locks verified compliant** in ECC (divine-names table; MT-anchored variant policy; inclusion-variant §2.3 floor; leitwort-handling policy; divine-anthropomorphism/honorifics; Hebrew idiom + wordplay handling — see §12-16).
- **4 items flagged REVIEW** (miqreh anti-*karma* register; 3:11 הָעֹלָם → นิรันดร์กาล crux; the 7:26-28 "snare-woman" register; the MT-anchored vs BSB word-variant renderings at 2:25 / 8:10).
- **1 item flagged DECIDE** (the *hevel* rendering itself — provisional, blocks the v1 tag).
- **2 new `docs/translator_decisions/` docs recommended:** `qoheleth_persona_register_2026-06.md` and (once the verdict lands) `hevel_leitwort_2026-06.md`.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. הֶבֶל *hevel* — the book's leitwort, shipped PROVISIONAL — **DECIDE before tagging (sole v1 blocker)**

The defining word of Ecclesiastes. *hevel* (lit. "vapor / breath") appears in **30 verses** across the book (with in-verse repeats at 1:2, 9:9 the token count is ≈38), framing the whole work in an inclusio: **1:2** opens it and **12:8** closes it with the identical superlative.

Every occurrence is rendered uniformly **ไร้แก่นสาร** ("without lasting substance / coreless"), with the construct superlative הֲבֵל הֲבָלִים → **ไร้แก่นสารที่สุด**:

| Verse | Hebrew | Thai | Note |
|---|---|---|---|
| ECC 1:2 (inclusio open) | הֲבֵל הֲבָלִים ... הַכֹּל הָבֶל | "ไร้แก่นสารที่สุด" ... "ทุกสิ่งล้วนไร้แก่นสาร" | superlative ×2 + summary |
| ECC 1:14 | הַכֹּל הֶבֶל וּרְעוּת רוּחַ | ทุกสิ่งล้วน**ไร้แก่นสาร** เป็นการไล่ตามลม | paired with re'ut-ruach |
| ECC 3:19 | כִּי הַכֹּל הָבֶל | เพราะทุกสิ่งล้วน**ไร้แก่นสาร** | man/beast same fate |
| ECC 6:12 | חַיֵּי הֶבְלוֹ | ชีวิตอัน**ไร้แก่นสาร**ของเขา | genitive construct |
| ECC 9:9 (×2) | חַיֵּי הֶבְלֶךָ ... יְמֵי הֶבְלֶךָ | วันคืนอัน**ไร้แก่นสาร**ของเจ้า | 2nd-person genitive |
| ECC 12:8 (inclusio close) | הֲבֵל הֲבָלִים ... הַכֹּל הָבֶל | "ไร้แก่นสารที่สุด" ... "ทุกสิ่งล้วนไร้แก่นสาร" | matches 1:2 |

The 1:2 KD states the choice and its provisional status explicitly:

> hevel leitwort (~38× ทั้งเล่ม) — เลือกคำเดียวคงที่เพื่อรักษา refrain; ไร้แก่นสาร = 'ไม่มีแก่นสารถาวร' ตรง uW gloss 'vapor that disappears, no lasting value'; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus (33 ข้อก่อนหน้าไม่เคยใช้). **PROVISIONAL** — รอคำยืนยันจากผู้อ่านไทยสองท่านของ Ben (2026-06-03); หากเปลี่ยนเป็น อนิจจัง ต้อง rev 1:2, 1:14

**Editorial assessment.** The rendering is principled, internally consistent (a single word carries the refrain across all 30 verses, preserving the leitwort that `leitwort_handling_policy_2026-05.md` exists to protect), and aligned with the corpus's standing avoidance of Buddhist-loaded vocabulary: across **33 prior *hevel* verses** outside Ecclesiastes the corpus has *never* used อนิจจัง (*anicca*), instead rendering contextually (ลมหายใจ Ps 144:4, ไอหมอก Prov 21:6, เปล่าประโยชน์ Job, ไร้สาระ Ps 94:11, ไม่จีรัง Prov 31:30, มายา Ps 62:10). ไร้แก่นสาร extends that avoidance while gaining what the scattered renderings could not: a recognisable book-wide refrain.

**Why it is DECIDE, not STABLE.** Ben explicitly opened this as a pending decision and authorized *ship-provisional* precisely so the translation loop would not stall: chapters shipped with ไร้แก่นสาร flagged PROVISIONAL, and the verdict from his two Thai readers (short EN+TH question texts sent 2026-06-03) was still outstanding at the time the book completed. Three options were on the table:
1. **อนิจจัง** consistent — traditional, THSV-familiar, but Buddhist-loaded (*anicca*);
2. **ไร้แก่นสาร** consistent — non-Buddhist, preserves the 30-verse refrain (the shipped provisional, translator's recommendation);
3. **contextual** per-verse — natural locally, loses the refrain.

**DECIDE before tagging.** Confirm the verdict from the reader panel.
- If **ไร้แก่นสาร confirmed** → strip the PROVISIONAL flags from the *hevel* KDs (mechanical) and lock via a new corpus doc.
- If **อนิจจัง** → mechanical swap across all 30 verses + re-render the *hevel*-ledger verses (established PSA re-rev pattern); the ledger is recorded per-chapter in auto-memory `project_ecclesiastes_start.md`.
- Either way, **→ recommend new doc** `docs/translator_decisions/hevel_leitwort_2026-06.md` locking the final rendering, the *anicca*-avoidance rationale, and the cross-corpus *hevel* policy (so Ps / Prov / Job retro-consistency and any future Isaiah/Jeremiah *hevel* are governed). This is the **only item blocking `book-ecclesiastes-v1`.**

---

## 2. קֹהֶלֶת Qoheleth → ปัญญาจารย์ + plain-voice register — **STABLE (undocumented; recommend new doc)**

The title-character's name is rendered with the traditional Thai title of the book, **ปัญญาจารย์** ("teacher of wisdom"), locked by Ben 2026-06-03, and the speech that introduces his words uses the **plain** speech verb กล่าว rather than royal register — even though 1:1 identifies him as "son of David, king in Jerusalem."

- ECC 1:1 GK/HEB: `דִּבְרֵי קֹהֶלֶת בֶּן־דָּוִד מֶלֶךְ בִּירוּשָׁלִָם` → TH: `ถ้อยคำของ**ปัญญาจารย์** โอรสของดาวิด กษัตริย์ในเยรูซาเล็ม`
- ECC 1:2 / 12:8: `אָמַר קֹהֶלֶת` → TH: `**ปัญญาจารย์กล่าว**` (plain กล่าว, both inclusio frames)

The 1:2 KD articulates the register choice: *"เสียงปัญญาจารย์ในฐานะครูปัญญา ใช้ register สามัญ (กล่าว) ไม่ใช่ราชาศัพท์ — ตามแนว wisdom-genre ของ corpus."* The persona is a wisdom-teacher addressing the reader, not an enthroned monarch in narrative; the plain register is the principled correlate of that genre read. Solomon-sonship at 1:1 follows the Prov 1:1 precedent (โอรสของดาวิด).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/qoheleth_persona_register_2026-06.md`, locking (a) קֹהֶלֶת → ปัญญาจารย์, (b) the plain-กล่าว wisdom-teacher voice, (c) the frame-narrator handling at 12:9-11 (§15). No book reuses קֹהֶלֶת, so forward-compounding is nil — but the doc closes the loop on a Ben-locked decision currently recorded only in working memory.

---

## 3. תַּחַת הַשֶּׁמֶשׁ → ภายใต้ดวงอาทิตย์ — **STABLE**

The book's signature spatial refrain, "under the sun," rendered uniformly **ภายใต้ดวงอาทิตย์** across **29 occurrences** (the count established at 1:3 and held through 12:2). Verified uniform — no drift to ใต้ดวงอาทิตย์ / บนโลก variants. Representative: 1:14, 2:11, 8:15 (twice in one verse), 9:3. Documented at verse level; uniformity is mechanical-checkable and clean.

---

## 4. רְעוּת / רַעְיוֹן רוּחַ → การไล่ตามลม — **STABLE**

"Chasing after wind," rendered uniformly **การไล่ตามลม** across **9 occurrences**, almost always paired with *hevel* (1:14, 2:11, 2:17, 2:26, 4:4, 4:6, 4:16, 6:9). The pairing reinforces the *hevel* refrain and is rendered as a fixed collocation. STABLE; will re-render only if §1 flips *hevel* to อนิจจัง (the pairing stays).

---

## 5. יִתְרוֹן → ประโยชน์ — **STABLE**

The "profit / gain / advantage" term that frames the book's opening question (1:3 "what profit?") — rendered **ประโยชน์** (ประโยชน์ appears 16× book-wide; the יִתְרוֹן-specific lock is ~10×, with the surplus carried by other gain-words rendered the same way for sense). Uniform, principled, mechanical-clean. STABLE.

---

## 6. Carpe-diem refrain (กิน-ดื่ม-ชื่นชมการตรากตรำ) — **STABLE (recommend doc note)**

Ecclesiastes' five "eat, drink, and find joy in your toil" refrains are rendered with a **fixed phrase skeleton** anchored at 2:24 and deliberately repeated:

| Verse | BSB | Thai (refrain core) |
|---|---|---|
| ECC 2:24 | eat and drink and enjoy his work | การกิน การดื่ม และการให้จิตใจชื่นชมกับสิ่งดีในการตรากตรำ |
| ECC 3:12-13 | rejoice... eat and drink and find satisfaction | ชื่นชมยินดี... จะกิน จะดื่ม และชื่นชมกับสิ่งดีในการตรากตรำ |
| ECC 3:22 | nothing better than to enjoy his work | ไม่มีสิ่งใดดีไปกว่าการที่มนุษย์จะชื่นชมยินดีในการงานของตน |
| ECC 5:18 | eat and drink and find satisfaction | (Eng 5:18 / MT 5:17 — divergence zone, §14) |
| ECC 8:15 | eat and drink and be merry | การกิน การดื่ม และการชื่นชมยินดี |

The 2:24 note flags the anchor explicitly: *"วรรคแรกของ refrain 'กิน-ดื่ม-ชื่นชมการตรากตรำ' (จะวนซ้ำ 3:12-13, 3:22, 5:18, 8:15) — ตรึงโครงวลีนี้."* The repetition is principled (these are the book's structural counterweight to the *hevel* refrain). STABLE; worth a one-line mention in the recommended Qoheleth doc (§2) rather than its own file.

---

## 7. מִקְרֶה *miqreh* → เหตุอย่างเดียวกัน (anti-*karma* register) — **REVIEW**

*miqreh* ("fate / what befalls / chance-event," 7× incl. 2:14-15, 3:19, 9:2-3) is uniformly rendered with the neutral **เหตุ(อย่างเดียวกัน)** ("the same event/occurrence befalls"), **deliberately avoiding ชะตากรรม** ("fate / destiny"), which in Thai carries *karma* freight. This parallels the §1 *hevel* avoidance of อนิจจัง — a second register-choice steering the Wisdom book away from Buddhist theological vocabulary.

- ECC 3:19 HEB: `מִקְרֶה בְנֵי־הָאָדָם וּמִקְרֶה הַבְּהֵמָה וּמִקְרֶה אֶחָד לָהֶם` → TH: `เหตุที่เกิดแก่บุตรของมนุษย์ก็เกิดแก่สัตว์ เป็น**เหตุอย่างเดียวกัน**`
- ECC 9:2 HEB: `מִקְרֶה אֶחָד לַצַּדִּיק וְלָרָשָׁע` → TH: `**เหตุอย่างเดียวกัน**เกิดแก่คนชอบธรรมและคนชั่วร้าย`
- ECC 9:3 HEB: `כִּי־מִקְרֶה אֶחָד לַכֹּל` → TH: `**เหตุอย่างเดียวกัน**เกิดแก่ทุกคน`

**REVIEW.** The choice is sound and consistent, but it is a *second* systematic anti-Buddhist register decision in the same book and deserves Ben's explicit confirmation alongside the *hevel* verdict — both are about the same theological-register boundary, and if a doc locks *hevel* (§1) it should name *miqreh* as a parallel application of the same principle. Tradeoff: เหตุอย่างเดียวกัน is slightly flatter than the fatalistic charge of the Hebrew, but it correctly refuses to import *karma*.

---

## 8. רוּחַ *ruach* — three-way contextual split (ลม / ลมหายใจ / วิญญาณ) — **STABLE**

*ruach* is rendered by sense, with the ambiguity-preserving cases flagged in-verse:

| Verse | Sense | Thai | Note |
|---|---|---|---|
| ECC 3:19 | breath (man/beast share) | ลมหายใจ | "all have the same breath" |
| ECC 3:21 | spirit (ascends/descends) | วิญญาณ | documented split vs 3:19 |
| ECC 11:5 | wind **or** spirit (deliberate ambiguity) | ลม | note: "ความกำกวมนี้อยู่ในต้นฉบับ" |
| ECC 12:7 | spirit (returns to God) | วิญญาณ | "the spirit returns to God who gave it" |

The 11:5 note keeps the Hebrew's wind/spirit double-reading open (paired both with 11:4's wind and with the womb-formation image) rather than forcing a choice. Principled, verse-documented, STABLE — consistent with `psyche_vs_pneuma_anthropological_2026-04.md`'s spirit-of-life handling.

---

## 9. ECC 3:11 הָעֹלָם → นิรันดร์กาล ("eternity in their hearts") — **REVIEW**

A genuine three-way lexical crux. הָעֹלָם at 3:11 is read by interpreters as (a) "eternity," (b) "the world," or (c) "what is hidden / the hidden whole." The translation chose **นิรันดร์กาล** ("eternity"):

- ECC 3:11 HEB: `גַּם אֶת־הָעֹלָם נָתַן בְּלִבָּם` → TH: `ทั้งทรงตั้ง**นิรันดร์กาล**ไว้ในใจของพวกเขา`
- Note: *"הָעֹלָם ตีความได้หลายทาง (นิรันดร์กาล/โลก/สิ่งที่ถูกซ่อน) — เลือก 'นิรันดร์กาล' ตามฉบับแปลหลักและบริบท 'ต้นจนจบ'."*

**REVIEW.** The choice aligns with NIV/ESV/CSB/THSV ("eternity") and the immediate context (מֵרֹאשׁ וְעַד־סוֹף, "from beginning to end" → ต้นจนจบ) supports a temporal-totality reading. Defensible and mainstream; flagged only because it is a contested crux where the alternatives are real and the rendering closes them. Worth Ben's confirmation that the temporal reading is the corpus default.

---

## 10. ECC 7:26-28 — the "snare-woman" passage register — **REVIEW**

The book's most pastorally sensitive verses. The translation renders the "woman who is a snare" (7:26) and "not one [upright] woman among all these" (7:28) faithfully, but **scopes them in-note to the wisdom-literature trope rather than a universal pronouncement on women**:

- ECC 7:26 HEB: `מַר מִמָּוֶת אֶת־הָאִשָּׁה אֲשֶׁר־הִיא מְצוֹדִים` → TH: `สิ่งที่ขมขื่นยิ่งกว่าความตายคือ**ผู้หญิงที่ใจของนางเป็นบ่วงแร้ว**` — note: *"ภาพ 'หญิงบ่วงแร้ว' ต่อสายวรรณกรรมปัญญา (เทียบ Prov 5, 7) — เป็นรูปจำเพาะ ไม่ใช่คำกล่าวรวมถึงสตรีทั้งปวง (ดู 9:9 คู่ตรงข้าม)."*
- ECC 7:28 HEB: `אִשָּׁה בְכָל־אֵלֶּה לֹא מָצָאתִי` → TH: `ในคนทั้งปวงเหล่านี้ ข้าพเจ้าไม่พบหญิงสักคน` — note scopes it to the "thousand" Qoheleth surveyed, not a universal claim, and cross-refs 9:9's positive counterpart (ชีวิตคู่ที่รัก).

**REVIEW.** The Thai text translates the MT without softening (no euphemising, no omission — correct per RULES §0 fidelity), and the interpretive scoping lives only in the translator notes, not the rendered verse. This is the right architecture. Flagged for Ben because (a) it is the one place in ECC where a faithful rendering risks a misogynistic-universal misreading by a lay Thai reader, and (b) the 9:9 cross-reference (positive marriage counterpart) is the intended balancing context — confirm whether anything beyond the note (e.g. a reader-facing footnote) is wanted before the v1 tag.

---

## 11. MT-anchored vs BSB word-variant renderings (2:25, 8:10) — **REVIEW**

Two verses where the Thai follows the **Masoretic Text** against the BSB base (which here reflects an LXX-ward or emended reading), each documented in-note per the `mt_vs_lxx_textual_variant_handling_2026-05.md` policy:

| Verse | MT reading (→ Thai) | BSB reading | Note |
|---|---|---|---|
| ECC 2:25 | מִמֶּנִּי "apart from **me**" → นอกเหนือไปจาก**ข้าพเจ้า** | "apart from **Him**" (LXX) | KD: MT = Qoheleth-who-has-everything |
| ECC 8:10 | יִשְׁתַּכְּחוּ "**forgotten**" → **ถูกลืม** | "**praised**" (variant ישתבחו) | KD: MT-anchored |

**REVIEW.** Both follow the corpus MT-floor policy correctly and are documented at verse level. The question for Ben: these are **word-level** variants (a pronoun, a verb root), not whole-verse inclusion variants, so under the §2.3 inclusion-variant floor **no `textual_variants/ecclesiastes_*.json` file is owed** — and indeed none exists. Confirm that verse-level KD documentation is sufficient here (matching the precedent set in 2KI / Daniel audits where MT/LXX word-variants were ruled §2.3 non-gaps), and that ECC owes no textual_variants files. (This mirrors the standing audit finding that books without whole-verse inclusion variants owe no such files — ECC has none.)

---

## 12. Divine names — Elohim-only, no Tetragrammaton — **LOCKED** (`divine_names_table_2026-05.md`)

Ecclesiastes is the **first OT book in the corpus with no YHWH at all** — God is named exclusively by אֱלֹהִים / הָאֱלֹהִים, rendered **พระเจ้า** throughout. Consequences, all correct:
- **No first-occurrence YHWH footnote is owed** (the footnote rule fires only on the Tetragrammaton).
- The `output/check_reports/divine_names.md` counter now reads "Chapters with YHWH: 0 / first-occurrence footnote: 0" — this is the **correct** state for ECC, not a regression. (The pre-existing modified-file noise predates this book; see auto-memory `project_ecclesiastes_start.md`.)
- Divine-name compliance is mechanically clean (0 hard fails, 0 warnings). **LOCKED.**

---

## 13. Divine anthropomorphism + honorifics — **LOCKED** (`divine_anthropomorphism_thai_grammar_2026-05.md`)

God consistently takes royal verbs (ประทาน "give," ทรงทำ/ทรงกระทำ "do/make," ทรงสถิต "dwell," พอพระทัย "be pleased") and พระหัตถ์ "hand," พระราชกิจ "work." Representative:
- ECC 3:11: `ทรงทำ...ทรงตั้ง...พระราชกิจที่พระเจ้าทรงกระทำ`
- ECC 5:1 (Eng): `พระเจ้าทรงสถิตในสวรรค์`
- ECC 12:14: `พระเจ้าจะทรงนำการกระทำทุกอย่างเข้าสู่การพิพากษา`

The **king** in ch. 8 (a human monarch) correctly receives full royal register (รachasap: พระบัญชา / พระดำรัส / พอพระทัย / ทรงกระทำ at 8:2-4), with the body-part-before-ทรง trap dodged via ที่ประทับ over พระพักตร์. The 6:10 oblique-God reference (תַּקִּיף) is kept plain to preserve the Hebrew's ambiguity. Honorific gates mechanically clean. **LOCKED.**

---

## 14. Versification divergence zone (MT 4:17 = Eng 5:1; MT 5 = Eng 5:2-20) — **STABLE**

Ecclesiastes 4-5 carries the standard MT/English one-verse offset (MT 4:17 = Eng 5:1, MT 5:1-19 = Eng 5:2-20). Every verse in the zone carries a versification sub-object and cross-filled BSB N+1 per the 1KI-5 precedent, and the entries are registered in `versification_map.json`. Per auto-memory, the map's builder is now merge-preserving (post-incident `7ab4bc6f`). **STABLE** — verify the map entries survived the final ship (`git status` shows no map dirt, so they did).

---

## 15. Epilogue frame-narrator voice shift (12:9-14) — **STABLE**

The book closes with a **third-person frame narrator** speaking *about* Qoheleth (12:9-11) before the final imperative (12:13-14) — a register shift from the first-person ข้าพเจ้า body of the book. Handled correctly:
- ECC 12:9: `נוסף שהיה קהלת חכם` → `นอกจาก**ปัญญาจารย์**เป็นคนมีปัญญาแล้ว **ท่าน**ยังสั่งสอน...` (3rd-person ท่าน, plain register)
- ECC 12:11: רֹעֶה אֶחָד "one Shepherd" → `**พระผู้เลี้ยง**เพียงผู้เดียว` (royal register for the divine Shepherd — correct elevation)
- ECC 12:13 (climax): `אֶת־הָאֱלֹהִים יְרָא` → `จง**ยำเกรง**พระเจ้า` (ยำเกรง fear-of-God, consistent with the book's earlier 3:14 / 5:7 usage)

The voice shift is principled and the divine-Shepherd elevation at 12:11 is correctly distinguished from the human-narrator plainness around it. STABLE; fold the frame-narrator handling into the recommended Qoheleth doc (§2).

---

## 16. Hebrew idiom, wordplay + hapax handling — **LOCKED** (`hebrew_idioms_and_metaphor_2026-05.md`, `wordplay_and_paronomasia_2026-05.md`)

Compliant throughout: the shem/shemen and sirim/sir puns (7:1, 7:6) are noted per the wordplay lock; the cheshbon/gulibai root-play (7:25-29) is flagged; the shacharut hapax (11:10) → วัยรุ่งอรุณแห่งชีวิต; nephesh sense-split (6:7 ความอยาก "appetite" vs elsewhere); the 12:1-7 allegory of aging is rendered image-faithfully with notes. No drift; verse-level rationale present. **LOCKED.**

---

## Recommended new translator_decisions docs

1. **`docs/translator_decisions/hevel_leitwort_2026-06.md`** — *create once §1 verdict lands.* Locks the final *hevel* rendering (ไร้แก่นสาร or อนิจจัง), the *anicca*-avoidance rationale, the 30-verse inclusio, and cross-corpus *hevel* policy (Ps/Prov/Job retro-consistency). Name *miqreh*/ชะตากรรม-avoidance (§7) as a parallel application.
2. **`docs/translator_decisions/qoheleth_persona_register_2026-06.md`** — locks קֹהֶלֶת → ปัญญาจารย์, the plain-กล่าว wisdom-teacher voice, the carpe-diem refrain skeleton (§6), and the 12:9-11 frame-narrator handling (§15).

## Checklist for Ben before tagging `book-ecclesiastes-v1`

- [ ] **DECIDE §1** — land the *hevel* reader-panel verdict. ไร้แก่นสาร confirmed → strip PROVISIONAL flags + write `hevel_leitwort_2026-06.md`. อนิจจัง → mechanical swap across 30 verses + re-rev the ledger.
- [ ] **REVIEW §7** — confirm *miqreh* → เหตุอย่างเดียวกัน (anti-*karma*) register.
- [ ] **REVIEW §9** — confirm 3:11 הָעֹלָם → นิรันดร์กาล (eternity) as corpus default.
- [ ] **REVIEW §10** — confirm the 7:26-28 snare-woman scoping (note-only, no reader footnote) is sufficient.
- [ ] **REVIEW §11** — confirm verse-level KD is sufficient for the 2:25 / 8:10 MT word-variants; ECC owes no `textual_variants` files.
- [ ] Write the two recommended translator_decisions docs.
- [ ] Tag `book-ecclesiastes-v1`.
