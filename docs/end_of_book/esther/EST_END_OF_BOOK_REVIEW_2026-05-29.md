# Esther — End-of-Book Review

**Date:** 2026-05-29
**Scope:** All 10 chapters of Esther (167 verses); `glossary.json`; `docs/translator_decisions/` corpus (~98 docs through the Nehemiah end-of-book audit).
**Trigger:** EST 10 shipped (commit `ac16d1c9`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Sixteenth OT book in the corpus** and **the third post-exilic / Persian-court book**, immediately following Ezra and Nehemiah. Esther inherits both books' locks and re-exercises every Persian-court surface — but at maximum intensity: where Ezra met the Persian king mostly *inside reported letters* and Nehemiah met him in a single audience scene, **Esther's entire plot unfolds inside the court of Ahasuerus (Xerxes), who is the central royal figure of the book.** So the foreign-monarch register question that Ezra *deferred to a corpus decision* and Nehemiah *answered (full ราชาศัพท์)* is here exercised continuously across 10 chapters — and Esther resolves it the **same way Nehemiah did**, against Ezra. Esther is also unique in two ways no prior book has been: it is the **only book in the Hebrew Bible that never names God** (no Tetragrammaton, no Elohim, no Adonai anywhere in the rendered text), and it is the corpus's first encounter with a **named human arch-villain** (Haman) and a **festival-institution etiology** (Purim).
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) pass cleanly: 10/10 chapters have green per-chapter reports + back-translations + translations (167 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 701-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (20,797 verses); `audit_inclusion_variants.py --book esther --strict` = 0 candidates, exit 0. **`git status output/` is fully clean** (no dirty `divine_names.md` aggregate — see below). Esther carries **no `output/textual_variants/esther_NN.json` files at all**, and that is correct: the whole book contains zero Tetragrammaton, so no chapter is owed a YHWH first-occurrence footnote (the Ezra-5 / all-Aramaic precedent, applied here to the whole book). There is **no versification divergence** — MT and English Esther align chapter-and-verse (`data/versification_map.json` carries 0 Esther entries), the deuterocanonical Additions being the only material the LXX numbers differently, and those are excluded (§12).
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-esther-v1`):
  - **§2 — the foreign-monarch register, now the third book of the Persian-court block, and Esther casts the deciding vote for the Nehemiah / written-`§2.2` reading.** Esther grants Ahasuerus **full ราชาศัพท์ in narrator voice** wherever the king acts — `ผู้ทรงครอบครอง` (1:1), `ทรงจัดงานเลี้ยง` (1:3), `บรรทม` (6:1), `เสด็จ`/`ทอดพระเนตร`/`ทรงลุกขึ้นด้วยพระพิโรธ` (7:7–8), `ทรงถอดพระธำมรงค์`/`พระราชทาน` (8:1–2), `ทรงเรียกเก็บส่วย`/`ทรงเลื่อนยศ` (10:1–2), and royal nouns `พระทัย`/`พระพักตร์`/`พระเนตร`/`พระธำมรงค์`/`พระพิโรธ` throughout — every verse citing `ot_register_policy_2026-05.md §2.2` ("foreign emperors get ราชาศัพท์… even if villainous"). The 1:10 `key_decision` explicitly **declines to downshift** the register in the satirical drunk scene and **names Nehemiah's Artaxerxes as the precedent** ("สอดคล้องกับการคงราชาศัพท์ให้อารทาเซอร์ซีสในเนหะมีย์"). This is the same king-class as Ezra and **the very same king as Ezra 4:6** (Ahasuerus/Xerxes), whom Ezra renders in commoner register. So the cross-book inconsistency Nehemiah surfaced (Artaxerxes rendered two ways) now extends to **Ahasuerus rendered two ways** (Ezra plain / Esther full `ทรง`). Both Ezra and Nehemiah remain shipped and **untagged** (`git tag` shows no `book-ezra-v1` / `book-nehemiah-v1`); the decision Ezra deferred for "Ezra–Nehemiah–Esther–Daniel" is still open and now spans three shipped books. **Esther is itself policy-compliant — no edit to Esther is expected** — but its tag is gated on the same corpus ratification. See §2.
- **3 items flagged REVIEW** (worth Ben's confirmation; not all tag blockers):
  - **§9 — `דָּת` ("law / royal decree," the Persian-court leitwort and the engine of the plot) is rendered five+ ways.** `พระราชโองการ` (1:8), `กฎหมาย` (1:15, 1:19, 8:13), `พระบัญชา`/`พระราชกำหนด` (2:8), `ระเบียบ` (2:12, the women's-regimen rule), `พระราชสาส์น` (3:12–13, 8:9), `พระราชกฤษฎีกา` (9:1). The "irrevocable law of the Medes and Persians" motif (1:19 `เปลี่ยนแปลงไม่ได้` ↔ 8:8 `เพิกถอนไม่ได้`) — a structural hinge of the book — is itself worded two ways. The tiering is *probably* principled (general statute `กฎหมาย` vs specific written edict `พระราชสาส์น`/`พระราชโองการ` vs court regulation `ระเบียบ`), and `check_key_term_consistency.py` is clean because `דָּת` is not a registered key term (the §9-Nehemiah `פֶּחָה` situation), but it is worth Ben confirming the tier and the irrevocability wording. See §9.
  - **§12 — MT/LXX disposition: the Additions to Esther, the most prominent deuterocanonical expansion in any book the corpus has shipped.** The LXX Esther carries **six large Additions (A–F, ~107 verses)** — Mordecai's dream, the two royal decree-texts, the prayers of Mordecai and Esther, Esther's audience, the dream's interpretation — which insert the explicit divine-name and prayer language the Hebrew pointedly withholds, and which Catholic/Orthodox canons include. Eremos translates **MT only** and excludes them, documented in a **single** note at 1:1 (`ไม่รวม 'ส่วนเพิ่มเติมของเอสเธอร์' ในฉบับ LXX… ตาม RULES §0`). Like Ezra's 1 Esdras and Nehemiah's Esdras B, this sits below the `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 disclosure floor → non-gap — but the Additions are *more* canonically visible than 1 Esdras and **directly bear on the book's defining feature** (they supply the God Esther omits), so the disposition is worth recording explicitly. See §12.
  - **§13 — the hidden-acrostic Tetragrammaton (a Masoretic scribal feature unique to Esther) is not mentioned anywhere.** The MT of Esther famously encodes the divine name YHWH in four acrostics (1:20, 5:4, 5:13, 7:7) and the divine self-designation EHYH once (7:5) — the one place the Hebrew "smuggles in" the name the book otherwise refuses to speak, a feature several MT manuscripts mark with enlarged/majuscule letters. No `key_decision` or `note` across the 10 chapters mentions it. This is below the disclosure floor and translating the acrostic into Thai is impossible — but given that Esther's no-divine-name silence is itself a flagged feature (§1), Ben may want a single reader-facing note acknowledging the scribal tradition. See §13.
- **Three new corpus docs recommended,** two of them **overdue carry-forwards** from Ezra and Nehemiah:
  - **`persian_achaemenid_administrative_titles_2026-05.md`** (§10) — carry-forward from Ezra §6 + Nehemiah §9, **still unwritten**. Esther adds the satrap/governor/official tier (`สมุหเทศาภิบาล`/`ผู้ว่าราชการ`/`เจ้านายของมณฑล`, 3:12 = 8:9 = 9:3) and the `דָּת` tier (§9).
  - **`esther_divine_absence_2026-05.md`** (§1) — new, Esther-unique. Captures the no-divine-name fact, the resulting no-textual-variant-files convention, the silent-providence translation stance, and (per §13) the disposition on the hidden-acrostic feature.
  - **`purim_pur_etiology_2026-05.md`** (§8) — new, Esther-distinctive. Locks the `ปูร์ (คือสลาก)` + `ปูริม` rendering and the pur→Purim wordplay etiology. Lower priority (no forward-compounding — Purim appears only here).
  - (The Ezra/Nehemiah `foreign_monarch_register_2026-05.md` and `god_of_heaven_persian_title_2026-05.md` carry-forwards remain — the first gated on the §2 DECIDE; the second N/A to Esther, which has no divine title at all.)
- **External AI review (§3) pending.** Suggested 4-item packet: foreign-monarch register, now three-book (§2 DECIDE); `דָּת` decree-rendering tiers + irrevocability motif (§9 REVIEW); Additions-to-Esther / MT disposition (§12 REVIEW); hidden-acrostic Tetragrammaton reader-note question (§13 REVIEW).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Divine-name **absence** — **STABLE → recommend `esther_divine_absence_2026-05.md`** (Esther-unique)

Esther is the only book in the Hebrew Bible that never mentions God, and the translation faithfully preserves the silence. A whole-book search of the rendered `thai` verse text confirms **zero** occurrences of `องค์พระผู้เป็นเจ้า` (YHWH), `พระเจ้า` (Elohim), `ยาห์เวห์`, or `องค์เจ้านาย` (Adonai). The only four whole-file hits for `พระเจ้า` are **all in translator-facing commentary, never in Scripture text**:

| Ref | Field | Content |
|---|---|---|
| 1:1 | `thai_summary` + `notes` | "เอสเธอร์เป็นหนังสือเดียวในพันธสัญญาเดิมที่ไม่เอ่ยพระนามของพระเจ้าเลยแม้แต่ครั้งเดียว… พระหัตถ์ที่ทรงปกปักรักษาทรงทำงานอยู่เบื้องหลังฉากอย่างเงียบ ๆ" |
| 2:9 | `key_decision` rationale | commentary on חֶסֶד/favor (§14) |
| 3:2 | `key_decision` rationale | commentary on why Mordecai refuses to bow |
| 10:3 | `notes` | "เอสเธอร์จบลงโดยไม่เอ่ยพระนามพระเจ้าตลอดทั้งเล่ม… สื่อถึงการทรงนำเบื้องหลังฉากอย่างเงียบ ๆ โดยให้ผู้อ่านเป็นผู้สังเกตเอง" |

**Two consequences flow from the absence, both handled correctly:**

1. **No divine register decisions in the book.** The 1:1 note states it: "จึงไม่มีการตัดสินใจเรื่องราชาศัพท์ของพระเจ้าในเล่มนี้." The divine-name table, the `god_of_heaven` Persian title, the Spirit-empowerment idiom, the chesed-as-covenant-love lock, the Exod-34 attribute formula — none of them fire, because there is no divine subject anywhere. (The §10/§13/§14 inherited-lock checks below are all "N/A by content.")
2. **No `textual_variants` files.** Every prior OT book carried per-chapter YHWH first-occurrence footnotes; **Esther carries none, and is owed none** — the whole book is the Ezra-5 case (no Tetragrammaton → no footnote) extended to all 10 chapters. The mechanical gate is correct to be silent here.

The **silent-providence translation stance** is exercised most visibly at the book's theological hinges, all rendered without naming a deliverer:
- **4:14** `יַעֲמוֹד… מִמָּקוֹם אַחֵר` → `ความบรรเทาและการช่วยกู้สำหรับชาวยิวก็จะมาจากที่อื่น`, with the `key_decision`: "'จากที่อื่น'… เป็นการพาดพิงอย่างอ้อม ๆ โดยไม่ระบุชัดว่าผู้ใดจะช่วยกู้ — คงความกำกวมไว้ตามต้นฉบับ" — the ambiguity is deliberately preserved.
- **4:14b** `אִם־לְעֵת כָּזֹאת` → `บางทีเจ้าอาจได้มาถึงตำแหน่งราชินีก็เพื่อยามเช่นนี้ก็เป็นได้`.
- **4:16** `וְכַאֲשֶׁר אָבַדְתִּי אָבָדְתִּי` → `หากข้าพเจ้าจะต้องพินาศ ข้าพเจ้าก็ยอมพินาศ`.
- **9:1** `נַהֲפוֹךְ הוּא` → `กลับพลิกผัน` (the reversal leitwort, §6).

This is uniform, principled, and richly documented at verse level — but it is **undocumented at corpus level**, and it is the single most distinctive editorial fact about the book. **Recommend `esther_divine_absence_2026-05.md`** capturing: the no-divine-name fact, the no-textual-variant-files convention (and *why* it differs from every other OT book), the silent-providence rendering stance (`จากที่อื่น` ambiguity preserved), and the §13 hidden-acrostic disposition.

**STABLE** — no surface defect; documentation of a unique feature. **Severity: LOW** (forward-compounding is nil — Esther is unique — but explanatory value is high).

---

## 2. Foreign-monarch register (Ahasuerus) — **DECIDE (the headline; third book of the Persian-court block; Esther votes with Nehemiah against Ezra)**

This is the register question Ezra **explicitly parked for the "Ezra–Nehemiah–Esther–Daniel" block** and Nehemiah answered (full ราชาศัพท์, per the written §2.2). Esther — where Ahasuerus is the central figure and on stage for the whole book — answers it the **same way as Nehemiah**, and does so with an explicit cross-reference to the Nehemiah precedent.

**As shipped, Esther grants Ahasuerus full ราชาศัพท์ in narrator voice wherever he acts:**

| Ref | Hebrew | Thai (narrator voice) | Royal marker |
|---|---|---|---|
| 1:1 | הַמֹּלֵךְ | `ผู้**ทรง**ครอบครอง` | `ทรง` |
| 1:3 | עָשָׂה מִשְׁתֶּה | `**ทรง**จัดงานเลี้ยง` | `ทรง` |
| 1:4 | בְּהַרְאֹתוֹ | `**ทรง**สำแดง` | `ทรง` |
| 6:1 | נָדְדָה שְׁנַת הַמֶּלֶךְ | `กษัตริย์**บรรทม**ไม่หลับ` | royal verb (sleep) |
| 6:3 ff | וַיֹּאמֶר הַמֶּלֶךְ | `กษัตริย์**ตรัส**` | royal speech verb |
| 7:7 | קָם בַּחֲמָתוֹ | `**ทรง**ลุกขึ้นด้วย**พระพิโรธ** … **เสด็จ**จากงานเลี้ยง` | `ทรง` + royal noun + `เสด็จ` |
| 7:8 | וְהַמֶּלֶךְ שָׁב … | `กษัตริย์**เสด็จ**กลับ … **ทอดพระเนตร**เห็น` | `เสด็จ` + `พระเนตร` |
| 8:2 | וַיָּסַר הַמֶּלֶךְ אֶת־טַבַּעְתּוֹ | `**ทรง**ถอด**พระธำมรงค์** … **พระราชทาน**` | `ทรง` + royal noun + royal verb |
| 8:4 | וַיּוֹשֶׁט הַמֶּלֶךְ | `**ทรง**ยื่นคทาทองคำ` | `ทรง` |
| 10:1 | וַיָּשֶׂם … מַס | `**ทรง**เรียกเก็บส่วย` | `ทรง` |
| 10:2 | גִּדְּלוֹ הַמֶּלֶךְ | `กษัตริย์**ทรง**เลื่อนยศ` | `ทรง` |

The register is **applied uniformly per §2.2, not unevenly** — the chapters with little king-`ทรง` (4, 9) are simply the chapters where the king barely acts (the action is Esther's, Mordecai's, or the battle's); every narrator-voice verb whose subject *is* the king carries a royal form. The book's foundational `key_decision` is at **1:1**: "จักรพรรดิต่างชาติ (ฟาโรห์ เนบูคัดเนสซาร์ ไซรัส ดาริอัส เซอร์ซีส) ได้รับ ทรง- ในเสียงผู้เล่า แม้เป็นคนนอกพันธสัญญา … ตาม ot_register_policy §2.2."

**The decisive datapoint is 1:10** — the satirical scene where the king, drunk, issues the impulsive command that triggers the plot. The `key_decision` explicitly **declines to downshift** the honorific and **anchors the choice to Nehemiah's Artaxerxes**:

> "แม้ฉากนี้ออกเชิงเสียดสี (ทรงมึนเมา) ก็ยังคงราชาศัพท์ของจักรพรรดิตาม §2.2 'แม้เป็นตัวร้าย' — สงวนการลดทอนไว้สำหรับความผิดศีลธรรมร้ายแรง (เทียบดาวิด 2 ซมอ 11) ฉากนี้ยังไม่ถึงระดับนั้น (สอดคล้องกับการคงราชาศัพท์ให้อารทาเซอร์ซีสในเนหะมีย์)."

So Esther knows about, and aligns with, the Nehemiah resolution — and against Ezra. The cross-book inconsistency is now sharper than at the Nehemiah audit: **the conflict is no longer only on Artaxerxes (Ezra 7 / Neh 2) but on Ahasuerus/Xerxes himself** — Ezra 4:6 mentions Ahasuerus in narrator voice in commoner register, while Esther renders the same king with full `ทรง` for 10 chapters. A reader moving from Ezra to Esther meets the identical Persian emperor honored two different ways.

**The §2.5 Hebrew-servant side is clean and not in question.** Mordecai (cupbearer-class → vizier) is held in plain register throughout, exactly as Nehemiah was — see §3. Esther-the-queen's register (§4) is a separate, correctly-handled axis. **Only the *emperor's* register is the DECIDE.**

**DECIDE.** The audit changes nothing in Esther — Esther follows the written §2.2 and is internally uniform. What is owed is the **corpus-wide ratification Ezra deferred**, now over three shipped, untagged books:
- **Option A (recommended, and now strongly favored by the corpus): ratify §2.2 as written** — foreign emperors get full ราชาศัพท์ in narrator voice. Keep Nehemiah and Esther as-is (both already comply); **normalize Ezra's Persian-king narrator verbs to `ทรง`** (the bounded set EZR 1:7, 3:7, 4:6, 6:1, etc.). Two of three books, and the written policy, already point this way; Esther — the book where the Gentile emperor matters most — makes it three.
- **Option B: ratify the Ezra commoner-register split.** Then normalize **both** Nehemiah and Esther's narrator king-verbs (a much larger edit, against the written §2.2) and amend §2.2.

Either way: **write `foreign_monarch_register_2026-05.md`** (or amend `ot_register_policy §2.2`) before any of the three books is tagged, so Daniel (Nebuchadnezzar/Belshazzar/Darius/Cyrus) inherits a single written rule, and **tag Ezra, Nehemiah, and Esther together** once the diverging book is normalized. **Severity: MEDIUM-HIGH** — no theological stakes, but a now-three-book visible inconsistency on shared kings, gating every remaining Babylonian/Persian-court book. **Decide jointly with the Ezra and Nehemiah tags.**

---

## 3. Mordecai-as-vizier plain register (§2.5) — **LOCKED ("the supreme case")**

Per `ot_register_policy_2026-05.md §2.5` (the Joseph-vizier sub-rule, which names Mordecai explicitly), the narrator never grants the Hebrew court-official royal honorifics, even at the height of office. Esther holds this perfectly, and the **10:3** `key_decision` calls it out as the rule's strongest instance:

> `מִשְׁנֶה לַמֶּלֶךְ` → `อุปราชรองจากกษัตริย์`; "แม้โมรเดคัยจะเป็นผู้มีอำนาจรองจากจักรพรรดิ ก็ยังคงใช้ภาษาสามัญในเสียงผู้เล่า ไม่ได้รับราชาศัพท์ ทรง- ตาม ot_register_policy §2.5 (เทียบโยเซฟ 'รองจากฟาโรห์', ดาเนียล, เนหะมีย์) — ราชาศัพท์สงวนไว้สำหรับจักรพรรดิเท่านั้น **นี่คือกรณีสุดยอดของหลัก §2.5 ในเล่มเอสเธอร์**."

Mordecai's elevation chapters use plain verbs throughout — 8:2 he receives the signet (the *king* acts with `ทรง`; Mordecai is the recipient), 8:9–10 `เขียน`/`ส่ง` (plain) for issuing the counter-decree, 9:4 `เป็นใหญ่` (plain), 10:3 `เป็นอุปราช`/`แสวงหา`/`กล่าว` (plain). The contrast with the king in the same verses (8:2 `ทรงถอด`/`พระราชทาน` vs Mordecai plain) is exactly the §2.2/§2.5 boundary working as designed. This is the third consecutive book (Ezra-the-scribe, Nehemiah-the-governor, Mordecai-the-vizier) to confirm the Hebrew-servant plain register.

**LOCKED** ✓ per `ot_register_policy_2026-05.md §2.5` + `honorifics_non_divine_authorities_2026-04.md`.

---

## 4. Esther-as-queen register shift — **LOCKED**

The narrator tracks Esther's status with a clean register **shift at her coronation**, exactly as `ot_register_policy §2.2` (queens row) + §1.4 (royal voice) prescribe:

- **Before crowning (ch 2, a Jewish orphan):** plain register. 2:7 `นางไม่มีบิดามารดา`; 2:8 `เอสเธอร์ก็ถูกนำเข้าไป`; 2:10 `เอสเธอร์ไม่ได้บอก`. The **2:8** `key_decision` states the rule: "ยังไม่ได้เป็นราชินี จึงใช้ภาษาสามัญในเสียงผู้เล่า — ราชาศัพท์ของเอสเธอร์ในฐานะพระราชินีจะเริ่มเมื่อนางได้รับการสถาปนาในข้อ 17."
- **After crowning (chs 4–9, the queen):** full ราชาศัพท์. 4:4 `พระราชินีก็**ทรง**เป็นทุกข์`; 4:5 `พระนางเอสเธอร์จึง**ทรง**เรียก`; 5:1 `**ทรง**ฉลอง**พระองค์**`.
- **Speech-register modulation toward the king:** when the queen petitions her husband-sovereign she correctly downshifts to deferential first-person — 7:3 `พระนางเอสเธอร์… **ทูล**ตอบ`, `ข้าแต่กษัตริย์ หาก**หม่อมฉัน**…` (humble `หม่อมฉัน` + vocative `ข้าแต่`), reserving royal forms for the narrator's description of her and for her commands to inferiors. This is the §1.4 / pronoun-table register working on a queen-to-king axis.

The shift is principled, documented at the seam (2:8/2:17), and consistent thereafter.

**LOCKED** ✓ per `ot_register_policy_2026-05.md §2.2`/§1.4.

---

## 5. Haman — villain / adversary plain register — **LOCKED**

Esther is the corpus's first named human arch-villain, and the narrator holds him in **plain register throughout** — no `ทรง`, no royal speech verbs — exactly as the adversary policy prescribes, even though the king "set his seat above all the princes" (3:1). The **3:5** `key_decision` states the rule: "ฮามานเป็นขุนนาง (ต่ำกว่าระดับจักรพรรดิ) จึงใช้ภาษาสามัญตาม §2.2." Evidence:

| Ref | Hebrew | Thai | Register |
|---|---|---|---|
| 3:1 | וַיְגַדֵּל… אֶת־הָמָן | king `ทรง`เลื่อนยศ; Haman the object | plain (recipient) |
| 3:5 | וַיִּמָּלֵא הָמָן חֵמָה | `ฮามาน**เดือดดาล**ยิ่งนัก` (not royal `พระพิโรธ`) | plain |
| 3:8 | וַיֹּאמֶר הָמָן לַמֶּלֶךְ | `ฮามานจึง**ทูล**กษัตริย์` (deferential up, not `ตรัส`) | plain/deferential |
| 5:9 | יָצָא הָמָן… שָׂמֵחַ | `ฮามานออกไปด้วย**ใจ**ชื่นบาน` (not royal `พระทัย`) | plain |
| 5:12 | וַיֹּאמֶר הָמָן | first-person `**ข้าพเจ้า**` (not royal `เรา`) | plain |
| 7:6 | אִישׁ צַר וְאוֹיֵב | `ศัตรูและปฏิปักษ์ก็คือฮามาน**คนชั่วร้าย**ผู้นี้` | plain + villain label |
| 7:7 ff | (begging Esther) | `ฮามาน… **ทูลขอ**ชีวิต` (plain `ขอ`) | plain/deferential |

The plain-but-deferential-upward treatment (Haman uses `ทูล`/`ข้าพเจ้า` toward the king, never the royal `เรา`/`ตรัส` that the king himself takes) is precisely the noble-below-emperor register, and the `คนชั่วร้าย` (`רָע`) label tracks the locked `ชั่วร้าย` rendering. No honorific leakage anywhere.

**LOCKED** ✓ per `adversary_speech_register_2026-05.md` + `ot_register_policy §2.2` (foreign vassal/noble = plain).

---

## 6. The "Agagite / Amalek" intertext + the reversal (נַהֲפוֹךְ) leitwort — **STABLE**

Two Esther-distinctive editorial threads, both documented at verse level:

- **Haman the Agagite → Agag/Amalek.** The **3:1** `key_decision` makes the OT-internal allusion explicit: `הָאֲגָגִי` = "เชื้อสายอากากกษัตริย์ชาวอามาเลข (1 ซมอ 15) — ศัตรูของอิสราเอลตั้งแต่อพยพ (อพย 17) สะท้อนความขัดแย้งกับโมรเดคัยชาวเบนยามิน" — tying Haman to Agag king of Amalek (1 Sam 15) and the Saul-Agag backstory (Mordecai is a Benjamite, Saul's tribe). The epithet is rendered uniformly `คนอากาก` at 3:1, 8:3, 9:24. This is a genuine canonical-thread datapoint (the kind `proper_noun_wordplay_2026-05.md` / `ot_nt_cross_quotation_thread_2026-05.md` track).
- **The reversal leitwort `נַהֲפוֹךְ` (9:1)** → `กลับพลิกผัน`, with the `key_decision`: "נַהֲפוֹךְ (พลิกกลับ) เป็นคำสำคัญที่สรุปแก่นของทั้งเล่ม — สถานการณ์กลับตาลปัตร." The peripeteia that organizes the whole book (Haman's gallows, his decree, his honors all turned back on him) is captured at its hinge verse.

**STABLE** — both uniform and verse-documented. The Agagite thread could optionally be added as a datapoint to `proper_noun_wordplay`/cross-quotation docs; no defect. **Severity: LOW.**

---

## 7. מִשְׁתֶּה "feast" leitwort → งานเลี้ยง — **LOCKED**

The book's structural leitwort — Esther is built on a sequence of ten banquets — renders uniformly as `งานเลี้ยง` at every occurrence (1:3 `ทรงจัดงานเลี้ยง`, 1:5, 1:9, 2:18, 5:4–8, 6:14, 7:1–8 `งานเลี้ยงเหล้าองุ่น` for `מִשְׁתֵּה הַיַּיִן`, 9:17–18 `วันเลี้ยงฉลองและความยินดี` for `מִשְׁתֶּה וְשִׂמְחָה`). The **1:3** `key_decision` flags the intent ("מִשְׁתֶּה แปลคงที่ว่า 'งานเลี้ยง' ตลอด… คำนี้เป็นคำสำคัญประจำเล่ม"). No variant. Consistent with `leitwort_handling_policy_2026-05.md`.

**LOCKED** ✓ per `leitwort_handling_policy_2026-05.md`.

---

## 8. פּוּר / Purim etiology — **STABLE → recommend `purim_pur_etiology_2026-05.md`** (new, Esther-distinctive)

Esther is the etiology of a Jewish festival, and the pur→Purim wordplay is the book's naming-payoff. The translation handles it with a **dual transliterate-plus-gloss** strategy, introduced at the casting of the lot and resolved at the festival-naming:

| Ref | Hebrew | Thai | Note |
|---|---|---|---|
| 3:7 | הִפִּיל פּוּר הוּא הַגּוֹרָל | `ทอด**ปูร์** (คือ**สลาก**)` | KD: "ผู้เล่าให้ทั้งชื่อเปอร์เซีย 'ปูร์' และคำฮีบรู 'สลาก' (גּוֹרָל) เพราะเป็นที่มาของชื่อเทศกาลปูริม" |
| 9:24 | וְהִפִּל פּוּר הוּא הַגּוֹרָל | `ทอด**ปูร์** (คือ**สลาก**)` | same dual frame |
| 9:26 | קָרְאוּ… פוּרִים עַל־שֵׁם הַפּוּר | `เรียกว่า **ปูริม** ตามคำว่า **ปูร์**` | etymology: "'ปูริม' (พหูพจน์ของ 'ปูร์')" |
| 9:28–32 | (the days of) הַפּוּרִים | `วันปูริม` / `เรื่องปูริม` | consistent festival surface |

The festival's institutions are also rendered cleanly: `מִשְׁלוֹחַ מָנוֹת` → `ส่งของขวัญแก่กันและกัน`, `מַתָּנוֹת לָאֶבְיוֹנִים` → `ของกำนัลแก่คนยากจน` (9:22). The transliterate-the-Persian-name + gloss-the-Hebrew-equivalent pattern is the right reader-first call (it preserves the loanword the festival is named for while making the "lot" meaning transparent), and it is exactly the kind of festival-institution decision worth locking — even though Purim does not forward-compound (it appears only here).

**STABLE — recommend `purim_pur_etiology_2026-05.md`** capturing the `ปูร์ (คือสลาก)` dual frame, the `ปูริม` festival surface, and the wordplay etiology. **Severity: LOW.**

---

## 9. דָּת "law / royal decree" — multi-rendering + irrevocability motif — **REVIEW**

`דָּת` (a Persian loanword, ~20× in Esther) is the legal engine of the plot — the irrevocable edict that condemns the Jews and the counter-edict that saves them. It is rendered **five-plus ways**:

| Thai | Refs | Apparent role |
|---|---|---|
| `พระราชโองการ` | 1:8 | king's standing ordinance |
| `กฎหมาย` | 1:15, 1:19, 8:13, 9:1(adj.) | general statute / "the law" |
| `พระบัญชา` / `พระราชกำหนด` | 2:8 | royal command + regulation |
| `ระเบียบ` | 2:12 | the women's beauty-regimen rule |
| `พระราชสาส์น` | 3:12–13, 8:9 | a specific written/sealed edict |
| `พระราชกฤษฎีกา` | 9:1 | the decree taking effect |

The **"law of the Medes and Persians that cannot be repealed"** motif — a structural hinge (the king cannot undo Haman's decree, only counter it) — is itself worded two ways: **1:19** `…ในกฎหมายของชาวเปอร์เซียและมีเดียเพื่อจะ**เปลี่ยนแปลงไม่ได้**` vs **8:8** `…**เพิกถอนไม่ได้**` (the 8:8 KD explicitly cross-refs 1:19: "กฎเปอร์เซีย เทียบ 1:19").

The tiering is **probably principled** — `กฎหมาย` for the abstract statute, `พระราชสาส์น`/`พระราชโองการ` for a specific issued edict, `ระเบียบ` for a court regulation — and `check_key_term_consistency.py` is clean because `דָּת` is not a registered key term (exactly the Nehemiah §9 `פֶּחָה`/`תִּרְשָׁתָא` situation, invisible to the mechanical gate). But the variation is wide enough, and the irrevocability motif structural enough, that Ben should confirm: (a) is the contextual tier intended (and should it be recorded in the recommended Persian-titles doc), and (b) should the irrevocability wording (`เปลี่ยนแปลงไม่ได้` / `เพิกถอนไม่ได้`) be harmonized so the motif reads as one thread across 1:19 and 8:8?

**REVIEW.** No tag block, but a good harmonization question and a good external-AI item. **Severity: LOW-MEDIUM.**

---

## 10. Persian administrative titles — **STABLE → recommend `persian_achaemenid_administrative_titles_2026-05.md`** (overdue carry-forward from Ezra §6 + Nehemiah §9)

Esther re-exercises and extends the Persian imperial administrative vocabulary. Renderings are uniform across the book's three parallel decree-distribution lists (3:12 = 8:9 = 9:3):

| Source | Thai | Refs |
|---|---|---|
| אֲחַשְׁדַּרְפְּנִים (satraps) | `สมุหเทศาภิบาล` | 3:12, 8:9, 9:3 |
| פַּחוֹת (governors) | `ผู้ว่าราชการ` | 3:12, 8:9, 9:3 |
| שָׂרֵי הַמְּדִינוֹת (provincial officials) | `เจ้านายของมณฑล` | 3:12, 8:9, 9:3 |
| פַּרְתְּמִים (nobles, Persian loanword) | `(เหล่า)ขุนนางผู้สูงศักดิ์` | 1:3, 6:9 |
| בִּיתָן / גִּנַּת הַבִּיתָן (palace/pavilion) | `(ลาน)อุทยานแห่งพระราชวัง` | 1:5, 7:7–8 |
| כֶּתֶר (crown) | `ราชมงกุฎ` | 1:11, 2:17, 6:8 |
| מְדִינָה (province) | `มณฑล` | throughout |

This is the **third book** to introduce uniform-but-undocumented Persian administrative surfaces, and the recommended `persian_achaemenid_administrative_titles_2026-05.md` (carry-forward from both Ezra §6 and Nehemiah §9, **still unwritten**) should now be written, folding in: Ezra's set (`เจ้าเมือง`/`อาลักษณ์`/`ผู้ว่าราชการแคว้น`/`เหรัญญิก`/tax-triplet/"Beyond the River"), Nehemiah's governor-tier resolution (§9 there), Esther's satrap/governor/official tier here, and the §9 `דָּת` decree-tier. It forward-covers Daniel.

**STABLE** — uniform; documentation/forward-protection. **Severity: LOW** (but the doc is overdue across three books).

---

## 11. Proper-name transliteration (incl. the ten sons of Haman) — **LOCKED**

Esther is transliteration-dense — Persian royal names, seven eunuchs (1:10), seven princes (1:14), and the **ten sons of Haman** (9:7–9, all hapax) — and the `key_decisions` transliterate per `proper_names_and_transliteration_2026-05.md` (THSV11 base). Decisive evidence: `check_key_term_consistency.py` is clean (0 rule violations, 0 undocumented multi-renderings) across the 701-chapter corpus, which includes Esther's heavy name load. The ten sons (9:7–9): `ปารชันดาธา / ดาลโฟน / อัสปาธา / โปราธา / อาดัลยา / อารีดาธา / ปารมัชทา / อารีสัย / อารีดัย / ไวซาธา`, with the KD noting "ล้วนเป็น hapax ทับศัพท์ตามฐาน THSV11." Core characters are stable throughout: `อาหสุเอรัส` (Ahasuerus/Xerxes), `วัชที` (Vashti), `เอสเธอร์` (Esther), `โมรเดคัย` (Mordecai), `ฮามาน` (Haman), `เฮกัย` (Hegai), `เศเรช` (Zeresh). The Harbona spelling variant (חַרְבוֹנָא 1:10 / חַרְבוֹנָה 7:9) is rendered uniformly `ฮารโบนา`, with the MT variance noted.

*(Optional polish, not a gap: several MT manuscripts set the ten sons' names in a distinctive vertical-column layout. Whether to mirror that scribal feature in the reader app is a layout question, not a translation defect — could be folded into the §1 / §13 disposition if Ben wants it captured.)*

**LOCKED** ✓ per `proper_names_and_transliteration_2026-05.md`.

---

## 12. MT/LXX disposition — the Additions to Esther — **REVIEW (non-gap; add doc row)**

Esther's textual situation is the most prominent deuterocanonical-expansion case the corpus has shipped. The Greek (LXX) Esther carries **six large Additions (A–F, ~107 verses)**: (A) Mordecai's apocalyptic dream + the eunuchs' plot; (B) the text of Artaxerxes' pogrom edict; (C) the prayers of Mordecai and Esther; (D) Esther's unsummoned audience before the king; (E) the text of the counter-edict; (F) the interpretation of Mordecai's dream + the Purim colophon. The Additions famously **supply the explicit God-language the Hebrew withholds** (prayers, providence named outright), and Catholic/Orthodox canons include them. Eremos translates **MT Esther only**, per `RULES §0` and `ot_canon_and_text_base_2026-05.md`, and the exclusion is documented in a single note at **1:1**: "ฐานต้นฉบับ: MT (เอสเธอร์ภาษาฮีบรู) — ไม่รวม 'ส่วนเพิ่มเติมของเอสเธอร์' ในฉบับ LXX ซึ่งเป็นหนังสือนอกสารบบของนิกายโปรเตสแตนต์ (ตาม RULES §0)."

For **verse-level** MT-vs-LXX divergence this is correct: `audit_inclusion_variants.py --book esther --strict` = 0 candidates, no `textual_variants` files (and none owed — no YHWH, §1). Under `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3, the Additions are a **separate recension / canonical-block question**, not a per-verse MT variant, so the disposition is **non-gap** — the same call Ezra reached for 1 Esdras and Nehemiah for Esdras B. The reason to flag it: the Additions are *more* canonically visible than 1 Esdras **and** they bear directly on the book's flagged defining feature (§1 — they are precisely where the LXX "fixes" the missing God). A one-line book-level disposition is worth recording.

**REVIEW.** Recommend adding an **Esther row** to `mt_vs_lxx_textual_variant_handling_2026-05.md` §3 recording the Additions-to-Esther disposition ("MT Esther is the base; the six LXX Additions A–F are deuterocanonical expansions excluded per RULES §0, not MT textual variants → no per-verse disclosure owed"). No surface change. **Severity: LOW.** Strong external-AI item.

---

## 13. Hidden-acrostic Tetragrammaton (Masoretic feature) — **REVIEW (reader-note question)**

The MT of Esther encodes the divine name in **four acrostics** — the initial or final letters of four consecutive words spell יהוה at 1:20, 5:4, 5:13, and 7:7 — and the divine self-designation אהיה ("I AM") once at 7:5, the single place the Hebrew text "smuggles in" the name the book otherwise refuses to speak. Several MT manuscripts mark these with enlarged/majuscule letters. A whole-book search of all `key_decisions` and `notes` finds **no mention** of the feature anywhere.

This is genuinely below the disclosure floor — the acrostic is untranslatable into Thai (it is a property of the Hebrew consonantal sequence), and most English versions are likewise silent. But Esther's no-divine-name silence is itself a *flagged* feature of this audit (§1), and the hidden acrostics are the scribal tradition's own theological commentary on that silence — "the name is present though unspoken." So unlike (say) an ordinary Masoretic enlarged-letter, this one is thematically load-bearing for the very thing the §1 doc will document.

**REVIEW.** Recommend Ben decide whether a **single reader-facing note** (one occurrence, e.g. at 1:20 or in the book introduction) acknowledging the acrostic tradition is owed — and fold the decision into `esther_divine_absence_2026-05.md` (§1) either way (whether "we note it once" or "deliberately silent, consistent with the book's own reticence"). No translation surface changes regardless. **Severity: LOW.** Good external-AI item (a textual/Masoretic question the AIs can speak to).

---

## 14. חֶסֶד as **human favor** (not covenant-love) — **LOCKED (disambiguation correct)**

Esther is the rare book where every `חֶסֶד` is **human**, not divine covenant-love — fitting the no-God theme. The locked `ความรักมั่นคง` (the divine-covenant-love surface) correctly **does not fire**; the human-favor sense renders as `ความโปรดปราน`: **2:9** `וַתִּשָּׂא חֶסֶד לְפָנָיו` → `ได้รับความโปรดปรานจากเขา` (Esther winning Hegai's favor); likewise 2:17. This is exactly the human-vs-divine disambiguation `chesed_covenant_love_2026-05.md` exists to protect, and the phrase-checker is clean (the `ความรักมั่นคง` lock is not misapplied to a human-favor context). The `חֵן`/`חֶסֶד` "favor and kindness" pairing toward Esther is the relational engine of her rise, rendered in ordinary register.

**LOCKED** ✓ per `chesed_covenant_love_2026-05.md` (the lock correctly N/A by sense — there is no divine chesed in Esther).

---

## 15. Versification — **STABLE (no divergence)**

MT and English Esther align chapter-and-verse; `data/versification_map.json` carries **0 Esther entries**, and that is correct — the only material the traditions number differently is the deuterocanonical Additions (which Catholic Bibles interleave with letter-versification, e.g. 11:2–12:6), and those are excluded (§12). No seam chapters, no per-verse divergence notes needed. (Contrast Nehemiah's five divergence chapters; Esther needs none.)

**STABLE** ✓ per `verse_schema_and_versification_2026-05.md`.

---

## 16. Inherited corpus locks — all compliant or correctly N/A

| Doc | EST evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 — **N/A by content**: zero YHWH/Elohim/Adonai in the rendered text; no textual-variant files owed. | **N/A (correct)** |
| `chesed_covenant_love_2026-05.md` | §14 — every חֶסֶד is human favor → `ความโปรดปราน`; the `ความรักมั่นคง` lock correctly does not fire. | **LOCKED** |
| `ot_register_policy_2026-05.md §2.2` | §2 — Ahasuerus full ราชาศัพท์ (per written §2.2); cross-book conflict with Ezra (incl. Ahasuerus at Ezra 4:6) → DECIDE. §4 — Esther-queen register shift. §5 — Haman noble-plain. | **DECIDE-§2** / **LOCKED-§4/§5** |
| `ot_register_policy_2026-05.md §2.5` | §3 — Mordecai-as-vizier plain throughout ("the supreme case of §2.5", 10:3). | **LOCKED** |
| `adversary_speech_register_2026-05.md` | §5 — Haman plain + deferential-upward; `คนชั่วร้าย` label. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | §7 — מִשְׁתֶּה → งานเลี้ยง uniform; §6 — נַהֲפוֹךְ → พลิกผัน (9:1). | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | §11 — Persian royal/eunuch/prince names + 10 sons of Haman; key-term check clean (701-chapter corpus). | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §12 — §2.3 floor → non-gap; add Additions-to-Esther row → REVIEW. Inclusion audit 0 candidates, exit 0. | **LOCKED-with-§12-REVIEW** |
| `proper_noun_wordplay_2026-05.md` / `ot_nt_cross_quotation_thread_2026-05.md` | §6 — Haman-the-Agagite → Agag/Amalek (1 Sam 15) thread documented at 3:1. | **STABLE** |
| `god_of_heaven_persian_title` (Ezra/Neh-recommended, unwritten) | **N/A** — no divine title of any kind in Esther (§1). | **N/A** |
| `exod_34_attribute_formula_2026-05.md` | **N/A** — no divine-attribute formula (no divine subject). | **N/A** |
| `dtr_history_cycle_formulas_2026-05.md` | **N/A** — post-exilic court narrative; no regnal-evaluation cycle. | **N/A** |
| `malak_yhwh_2026-05.md` | **N/A** — no מַלְאָךְ (divine or human) in Esther. | **N/A** |
| `hebrew_oath_formulas_2026-05.md` | **N/A** — no חַי־יְהוָה (there is no YHWH to swear by); the fast (4:16) uses צוּם, not an oath formula. | **N/A** |
| `spirit_of_yhwh_empowerment_2026-05.md` | **N/A** — no Spirit reference. | **N/A** |
| `biblical_aramaic` (Ezra-recommended, unwritten) | **N/A** — Esther is entirely Hebrew; no language switch. | **N/A** |

---

## 17. Mechanical (§1) — fully green

- 10/10 chapters: `output/check_reports/esther_NN_review.md` — all "✅ Ready to ship" ✓
- 10/10 chapters: `output/back_translations/esther_NN.json` ✓
- 10/10 chapters: `output/translations/esther_NN.json` (167 verses) ✓
- 0 chapters: `output/textual_variants/esther_NN.json` — **correct, none owed** (zero Tetragrammaton in the whole book; §1).
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (701-chapter corpus). *(Note: `דָּת` is not a registered key term, so the §9 decree-rendering variance is invisible to this check — the same gate-blind-spot as Nehemiah's `פֶּחָה`.)*
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (20,797 verses).
- `audit_inclusion_variants.py --book esther --strict`: **0 candidates, exit 0** (the Esther textual layer is the Additions-recension question, §12, not verse-level inclusion).
- `export_to_usfm.py --book EST`: **N/A** — the script's `BOOKS` table is NT-only ("Unknown book code: EST"); OT USFM export remains the carried-over separate concern noted in every prior OT audit.
- **Book-code registration:** `EST` was present in `OT_CODES` but **missing from the §3/§4 tooling slug tables** (`build_external_review_packet.py` `BOOKS`; `audit_items_to_yaml.py` `BOOK_SLUGS`) — **registered as part of this audit** per the EOB book-code-registration gotcha (Ezra and Nehemiah each hit this).
- `git status output/`: **fully clean** — no dirty `divine_names.md` aggregate (Esther adds no YHWH rows), no versification-map edits (Esther has no divergence, §15). The cleanest mechanical state of any OT book audited.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **zero** (by design, §1). Aramaic verses: **zero** (Esther is all-Hebrew).

**Severity: GREEN** — the cleanest mechanical gate in the OT pilot.

---

## 18. Flagged for Ben's attention

### DECIDE (block the `book-esther-v1` tag until resolved)

**A. Foreign-monarch register — now a three-book corpus decision (§2).** Esther grants Ahasuerus full ราชาศัพท์ in narrator voice (per the written `ot_register_policy §2.2`), aligning with Nehemiah and against Ezra — and it explicitly cites the Nehemiah/Artaxerxes precedent at 1:10. The cross-book inconsistency now spans the same king (Ahasuerus: Ezra 4:6 plain / Esther full `ทรง`). All three books are shipped and untagged. **Ratify one rule for the Persian/Babylonian court, normalize the diverging book (recommended: keep Nehemiah + Esther, normalize Ezra to `ทรง`), write `foreign_monarch_register_2026-05.md`, and tag Ezra + Nehemiah + Esther together.** Esther itself needs no edit. **MEDIUM-HIGH.**

### REVIEW (worth Ben's confirmation; §9 ideally before tag, §12/§13 optional)

**B. `דָּת` decree-rendering tiers + irrevocability motif (§9).** `דָּת` rendered 5+ ways (`กฎหมาย`/`พระราชโองการ`/`พระราชสาส์น`/`ระเบียบ`/`พระราชกฤษฎีกา`); the "cannot be repealed" motif worded two ways (1:19 `เปลี่ยนแปลงไม่ได้` / 8:8 `เพิกถอนไม่ได้`). Confirm the contextual tier is intended; consider harmonizing the irrevocability wording; capture in the recommended Persian-titles doc. **LOW-MEDIUM.**

**C. Additions-to-Esther / MT disposition (§12).** Add an Esther row to `mt_vs_lxx_textual_variant_handling_2026-05.md` recording the six LXX Additions (A–F) as excluded deuterocanonical expansions (non-gap). **LOW.**

**D. Hidden-acrostic Tetragrammaton (§13).** Decide whether a single reader-facing note acknowledging the MT acrostic tradition (1:20/5:4/5:13/7:7; EHYH 7:5) is owed, given §1's flagged no-divine-name feature; fold the decision into `esther_divine_absence_2026-05.md`. **LOW.**

### New translator_decisions docs recommended

1. **`foreign_monarch_register_2026-05.md`** (§2) — gated on the DECIDE; carry-forward from Ezra + Nehemiah (still unwritten). The single highest-value forward-protection doc — Daniel inherits it.
2. **`persian_achaemenid_administrative_titles_2026-05.md`** (§10) — overdue carry-forward from Ezra §6 + Nehemiah §9; now also covering Esther's satrap/governor/official tier + the §9 `דָּת` decree-tier. Forward-covers Daniel.
3. **`esther_divine_absence_2026-05.md`** (§1) — new, Esther-unique; the no-divine-name fact, the no-textual-variant-files convention, the silent-providence stance, and the §13 acrostic disposition.
4. **`purim_pur_etiology_2026-05.md`** (§8) — new, Esther-distinctive; the `ปูร์ (คือสลาก)` + `ปูริม` frame. Lower priority (no forward-compounding).

### Existing docs to amend (optional, no tag block)
- **`ot_register_policy_2026-05.md §2.2`** — fold in / point to the §2 foreign-monarch decision once ratified.
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the Esther Additions row (§12).
- **`proper_noun_wordplay_2026-05.md`** / **`ot_nt_cross_quotation_thread_2026-05.md`** — record the Haman-Agagite → Agag/Amalek thread (§6).
- **`chesed_covenant_love_2026-05.md`** — note Esther as the human-favor-only datapoint (§14).

### External AI review (§3 of checklist) — pending
Recommended 4-item packet (see `external_review_items_EST.md`):
1. **Foreign-monarch register — three-book corpus decision** (§2-A, DECIDE)
2. **`דָּת` decree-rendering tiers + irrevocability motif** (§9-B, REVIEW)
3. **Additions-to-Esther / MT disposition** (§12-C, REVIEW)
4. **Hidden-acrostic Tetragrammaton reader-note** (§13-D, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI/1CH/2CH/EZR/NEH pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 7 items (§3 Mordecai-§2.5, §4 Esther-queen, §5 Haman-adversary, §7 feast leitwort, §11 transliteration, §14 chesed-as-human-favor; + inherited locks via §16)
- **STABLE:** 4 items (§1 divine-name absence [→ recommend doc], §6 Agagite/Amalek + reversal leitwort, §8 Purim/Pur etiology [→ recommend doc], §10 Persian admin titles [→ recommend doc], §15 versification)
- **REVIEW:** 3 items (§9 `דָּת` decree-rendering, §12 Additions-to-Esther row, §13 hidden-acrostic note)
- **DECIDE:** 1 item (§2 foreign-monarch register — now a three-book corpus decision)

**One DECIDE item blocks the `book-esther-v1` tag** — and like Ezra's, it is a **clean, deliberately-deferred policy ratification, not a surface defect**: Esther follows the written §2.2 and is internally uniform; what is owed is the corpus-wide ratification (now over three shipped books) + the `foreign_monarch_register` doc, after which the diverging book (Ezra) is normalized and all three are tagged together.

**Three new translator_decisions docs recommended** (two overdue carry-forwards from Ezra/Nehemiah, one Esther-unique; a fourth is optional polish). **Four optional existing-doc amendments.**

---

## Recommendation

**Esther ships in excellent shape — the cleanest mechanical state of any OT book in the pilot** (fully clean `git status`, no dirty aggregate, no versification map edits, no textual-variant files owed). Its inherited locks all hold or are correctly N/A: Mordecai's §2.5 plain register is "the supreme case," Haman's adversary register is clean, Esther's queen-register shift is principled, the feast leitwort and transliteration are LOCKED, and the chesed lock correctly stays dormant in a book whose every חֶסֶד is human. Its three genuinely-new surfaces — the **absence of the divine name**, the **named human villain**, and the **Purim etiology** — are handled uniformly and with verse-level rationale.

**The work to do before v1 is, as with Ezra and Nehemiah, overwhelmingly documentation and one corpus decision, not correction:**

- **§2 is the headline and is bigger than Esther.** Esther is the third Persian-court book and casts the deciding vote: with the written `§2.2`, Nehemiah, and now Esther all on the full-ราชาศัพท์ side, Ezra is the lone outlier on a question it itself deferred to this very block. The decision must be made once, applied to all three, written into `foreign_monarch_register_2026-05.md`, and the three books tagged together. **Esther needs no edit** — only the corpus ratification it is gated on.
- **§9 (`דָּת` tiers + irrevocability motif)** is the one internal item worth confirming before the tag — a Nehemiah-§9-style key-term variance invisible to the mechanical gate.
- **§12 (Additions to Esther)** and **§13 (hidden acrostic)** are light, documented dispositions — both excellent external-AI questions and both bearing on the book's defining no-God feature.
- **The two overdue carry-forward docs** (`foreign_monarch_register`, `persian_achaemenid_administrative_titles`) should finally be written now — they have been owed since Ezra, span three books, and forward-protect Daniel; plus the two Esther-unique docs (`esther_divine_absence`, `purim_pur_etiology`).

**Tag `book-esther-v1` after:**
1. Ben's decision on the **§2 foreign-monarch register** (ratify + doc + normalize Ezra) — **jointly with the Ezra and Nehemiah tags.**
2. Ben's confirmation on **§9** (`דָּת` tier + irrevocability wording).
3. External AI sanity-check (the 4-item packet).
4. The two carry-forward Persian-block docs + the two Esther-unique docs written (the Purim doc is optional polish).

**The single highest-value forward-protection step remains the §2 register decision** — open since Ezra, now a visible three-book inconsistency on shared Persian kings, and the rule Daniel will lean on most heavily. Esther is the natural place to close it, because Esther is the book where the Gentile emperor matters most.
