# Ezra — End-of-Book Review

**Date:** 2026-05-27
**Scope:** All 10 chapters of Ezra (280 verses); `glossary.json`; `docs/translator_decisions/` corpus (~97 docs through the 2 Chronicles end-of-book audit).
**Trigger:** EZR 10 shipped (commit `afa31bab`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Fourteenth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles) and **the first post-exilic / Persian-period book**. Ezra opens on the exact words 2 Chronicles closed on (the Cyrus decree, 1:1–3a ≈ 2 Chr 36:22–23), so it inherits the Chronicler's locks — but it is also the corpus's **first sustained encounter with three brand-new stress-surfaces**: (a) **Biblical Aramaic** — roughly 4:8–6:18 and 7:12–26 (67 of 280 verses) are in Aramaic, not Hebrew, the first time the translation has had to carry a language switch mid-book; (b) **the foreign Persian monarch as a sympathetic actor** (Cyrus, Darius, Artaxerxes), which forces the register question the prior books never had to settle — do Gentile emperors get full Thai royal honorifics?; and (c) **the Persian-period administrative world** (satraps, governors, "Beyond the River," the imperial-archive memorandum) and the Persian-period divine title "the God of heaven."
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **13 cross-cutting items reviewed.** Mechanical gates (§1) pass: 10/10 chapters have green per-chapter reports + back-translations + translations (280 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 678-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (20,225 verses); `audit_inclusion_variants.py --book ezra --strict` = 0 candidates, exit 0. The single dirty file in `git status output/` is `output/check_reports/divine_names.md` — a transient aggregate report whose only diff adds one **C-soft** warning (Ezra 10:3 standalone אֲדֹנָי), which the 10:3 `key_decision` already documents as a deliberate false positive (§9); report-only, not a translation surface, identical in kind to the note carried in the 1SA/1KI/2KI/1CH/2CH audits.
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-ezra-v1`):
  - **§4 — the foreign-monarch register is a deliberately-deferred, precedent-setting choice that the translation parked *for this audit*.** The verse note at **1:2** states it verbatim: rendering the Gentile emperor in commoner register (`กล่าว`, not `ตรัส`) matches the already-shipped 2 Chr 36:23, but "whether to elevate foreign emperors to full royal honorifics per `ot_register_policy_2026-05.md` §2.2 is a corpus-level decision (affecting **Ezra–Nehemiah–Esther–Daniel**), to be considered at the Ezra end-of-book review." As shipped, Ezra runs a coherent **two-tier split**: in **narrator voice** the Persian kings take *no* `ทรง`-led verb (1:7 `กษัตริย์ไซรัสได้นำ…ออกมา`; 6:1 `กษัตริย์ดาริอัสจึงสั่งให้ค้น`), while **inside the reported letters/decrees** they receive in-world deferential forms (`พระองค์`, `กราบทูล`, `พระเกียรติ`, and even `ทรง` at 4:15 `พระองค์จะทรงพบ`, explicitly noted as courtly deference). The split is principled and documented per-verse, but it is **undocumented at corpus level and surface-mixed** (Persian kings carry `ทรง` in some verses, not others), and it is the precedent every later Persian-court book will inherit. **Needs Ben's ratification + a corpus doc before v1.** See §4.
- **4 items flagged REVIEW** (worth Ben's confirmation; not tag blockers):
  - **§3 / §6 — two new Persian-period surfaces are uniform and verse-documented but have no corpus doc.** (a) **"God of heaven"** (Hebrew אֱלֹהֵי הַשָּׁמַיִם, Aramaic אֱלָהּ שְׁמַיָּא) → uniformly **`พระเจ้าแห่งฟ้าสวรรค์`** (1:2; 5:11–12; 6:9–10; 7:12, 21, 23) across both languages — the signature divine self-presentation of the Persian period, recurring heavily in Nehemiah and Daniel. (b) The **Persian administrative-title set** — `เจ้าเมือง` (בְּעֵל־טְעֵם, commander), `อาลักษณ์` (סָפְרָא, scribe), `ผู้ว่าราชการแคว้น` (פֶּחָה, governor — Tattenai 5:3/6:6), `เหรัญญิก` (treasurer), the tax-triplet `ส่วย/บรรณาการ/ค่าธรรมเนียม` (4:13), and **"Beyond the River"** עֲבַר נַהֲרָה → descriptively `(แคว้น)ฟากตะวันตกของแม่น้ำ(ยูเฟรติส)` (12× in verse text, uniform). Recommend `god_of_heaven_persian_title_2026-05.md` and `persian_achaemenid_administrative_titles_2026-05.md` (both forward-cover Neh/Esth/Dan).
  - **§5 — the Hebrew↔Aramaic bilingual switch is handled at verse level but has no corpus doc or reader-facing footnote.** The `language` field correctly tags every verse (`hebrew`/`aramaic`); the switch is disclosed in the 4:7 + 4:8 verse notes ("from 4:8 to 6:18 the original is Aramaic"); and ch 5 — entirely Aramaic, containing **no** Tetragrammaton — correctly carries **no** YHWH first-occurrence footnote file (the 1CH-genealogy precedent). This is the corpus's first language switch and will recur in Daniel (2:4b–7:28); recommend a short `biblical_aramaic_sections_2026-05.md` capturing the policy.
  - **§9 — Ezra 10:3 אֲדֹנָי is read as the *human* "my lord" (= Ezra) and ships without `องค์เจ้านาย`.** The `key_decision` documents the choice (following BSB/ESV/NIV; context of v4 "Arise, this is your responsibility") and pre-empts the divine-names C-soft warning as a false positive. Defensible — but the **MT vocalizes it אֲדֹנָי (the form normally reserved for the divine title)**, not the human אֲדֹנִי, so a reviewer should confirm the human reading. Documented + defensible → REVIEW, not DECIDE.
  - **§12 — MT/LXX disposition: Ezra sits below the §2.3 disclosure floor, but its LXX situation (1 Esdras / Esdras A) is more prominent than the "Paraleipomena ≈ MT" cases.** All `textual_variants` files are YHWH-footnote-only (0 inclusion variants; `audit_inclusion_variants.py` clean). That is correct for verse-level MT/LXX divergence — but Ezra's distinctive textual feature is the **divergent Greek recension 1 Esdras** (Esdras A: reorders the material and adds the "contest of the three guardsmen," 1 Esd 3–4). Recommend confirming the §2.3-floor non-gap disposition explicitly given 1 Esdras's canonical visibility, and adding an Ezra row to `mt_vs_lxx_textual_variant_handling_2026-05.md`.
- **Three new corpus docs recommended:** `god_of_heaven_persian_title_2026-05.md` (§3), `persian_achaemenid_administrative_titles_2026-05.md` (§6), `biblical_aramaic_sections_2026-05.md` (§5). A fourth, the foreign-monarch register doc, is gated on the §4 DECIDE.
- **External AI review (§3) pending.** Suggested 4-item packet: foreign-monarch register (§4 DECIDE); 10:3 אֲדֹנָי (§9); 1 Esdras / MT-LXX (§12); "God of heaven" rendering (§3).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout the Hebrew sections. **~38 surface occurrences** of `องค์พระผู้เป็นเจ้า` across the 10 chapters (ch 1: 6; ch 2: 1; ch 3: 11; ch 4: 2; ch 5: 0; ch 6: 2; ch 7: 8; ch 8: 4; ch 9: 3; ch 10: 1). The density tracks the genre: ch 3 (altar + foundation worship) and ch 7–9 (Ezra's commission + confession) carry the most.

**ยาห์เวห์ residues in verse text: zero** across all 10 chapters. No sanctioned `ยาห์เวห์` survival (place-name memorial compounds) occurs in Ezra.

**Per-chapter first-occurrence YHWH footnote — 9/10, and the one gap is correct.** All chapters that contain YHWH carry the locked Tier-2 explanation in `output/textual_variants/ezra_NN.json` (`type: tetragrammaton_convention_first_occurrence`). **Ezra 5 is the sole chapter with no footnote file — and it is owed none: ch 5 is entirely Aramaic and contains zero Tetragrammaton** (the Aramaic uses אֱלָהּ "God", §2). This is exactly the 1 Chronicles precedent (genealogy chapters with no YHWH carried no footnote). Spot-checked and clean.

**LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 2. Elohim + Aramaic אֱלָהּ + pagan deities — **LOCKED**

- **Elohim → พระเจ้า** uniform across the Hebrew sections ✓.
- **Aramaic אֱלָהּ / אֱלָהָא ("God" / "the God") → พระเจ้า** uniform across the Aramaic sections (4:24; 5:1–2, 8, 11–17; 6:3–18; 7:12–26) ✓. The Aramaic divine vocabulary maps cleanly onto the same Thai surface as the Hebrew Elohim — no separate register leaks in.
- **אֱלָהָא רַבָּא ("the great God", 5:8) → พระเจ้าผู้ยิ่งใหญ่** ✓.
- **Pagan / foreign gods take the polytheistic `เทพเจ้า` register, never `พระเจ้า`.** 1:7 — the vessels Nebuchadnezzar placed `בֵּית אֱלֹהָיו` "in the house of his gods" → `วิหารแห่งเทพเจ้าของตน` (note explicitly: "`เทพเจ้า` not `พระเจ้า`"). Ezra has very little idolatry surface (it is a temple-rebuilding + covenant-purity book, not an apostasy narrative), so this is the principal pagan-deity datapoint and it complies. The "abominations of the peoples of the lands" in chs 9–10 are described as practices (`สิ่งน่าสะอิดสะเอียน`), not named deities.
- **No divine אֲדֹנָי in Ezra except the contested 10:3** (§9), which is read as human.

**LOCKED** ✓ per `divine_names_table_2026-05.md` + `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`.

---

## 3. "God of heaven" (אֱלֹהֵי הַשָּׁמַיִם / Aramaic אֱלָהּ שְׁמַיָּא) — **STABLE → recommend `god_of_heaven_persian_title_2026-05.md`**

The signature divine self-presentation of the Persian period — the title by which Israel's God is named to and by Gentile authorities — recurs across **both** languages of Ezra and renders **uniformly `พระเจ้าแห่งฟ้าสวรรค์`**:

| Ref | Lang | Source | Thai |
|---|---|---|---|
| 1:2 | Heb | אֱלֹהֵי הַשָּׁמָיִם (Cyrus' proclamation) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 5:11, 5:12 | Aram | אֱלָהּ שְׁמַיָּא (the elders' reply to Tattenai) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 6:9, 6:10 | Aram | אֱלָהּ שְׁמַיָּא (Darius' decree) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 7:12, 7:21, 7:23 | Aram | אֱלָהּ שְׁמַיָּא (Artaxerxes' rescript) | `พระเจ้าแห่งฟ้าสวรรค์` |

The 1:2 `key_decision` captures the rationale ("the title Cyrus uses to present YHWH to his subjects — the God who is over all / who rules the heavens"). The rendering is consistent and theologically apt, but it is **undocumented at corpus level** and recurs ~7× in Nehemiah and dominates Daniel (2:18–19, 2:37, 2:44; 5:23). This is the canonical end-of-book "lock it before it compounds" case.

**STABLE — recommend `god_of_heaven_persian_title_2026-05.md`** capturing: the Hebrew/Aramaic source forms, the locked Thai surface `พระเจ้าแห่งฟ้าสวรรค์`, and the forward-cover (Neh/Dan). No surface defect; documentation/forward-protection. **Severity: LOW.**

---

## 4. Foreign-monarch register (Persian emperors) — **DECIDE (the headline; deliberately deferred to this audit)**

This is the item the translation **explicitly parked for the Ezra end-of-book review**. The 1:2 verse note states it verbatim (translated): *"Cyrus, a foreign king, is rendered in commoner register (`กล่าว`) to match the already-shipped parallel 2 Chr 36:23; whether to elevate foreign emperors to full royal honorifics per `ot_register_policy_2026-05.md` §2.2 is a corpus-level decision (affecting Ezra–Nehemiah–Esther–Daniel) that should be considered together at the Ezra end-of-book review."* The same REGISTER note repeats at 1:7, 3:7, 4:8(area), and 6:1.

**What shipped is a coherent two-tier split:**

| Tier | Rule | Evidence |
|---|---|---|
| **Narrator voice** | Persian king takes **no `ทรง`-led verb**; polite nouns/pronouns allowed | 1:7 `กษัตริย์ไซรัสได้นำเครื่องใช้…ออกมา`; 6:1 `กษัตริย์ดาริอัสจึงสั่งให้ค้น…`; 3:7 `ให้` (not `ประทาน`) |
| **Inside reported letters / decrees** | King receives **in-world deferential forms** (`พระองค์`, `กราบทูล`, `พระเกียรติ`, occasionally `ทรง`) | 4:11 `ขอกราบทูลกษัตริย์อารทาเซอร์ซีส… ผู้รับใช้ของพระองค์`; 4:14 `เสื่อมเสียพระเกียรติ`; 4:15 `พระองค์จะทรงพบและทราบ` (note: "a polite form the writers use to address the king deferentially") |

The split is **principled and documented per-verse** — it mirrors the project's narrator-vs-character voice distinction and the §2.2 "register tracks the speaker's stance" logic. But:

1. It is **undocumented at corpus level** — no `docs/translator_decisions/` doc records the narrator-vs-address rule for Gentile monarchs, so the next book (Nehemiah, then Esther/Daniel, where Persian kings are *central*) has only the verse notes to go on.
2. It is **surface-mixed**: a reader scanning Ezra sees Persian kings sometimes with `ทรง`/`พระองค์` (inside letters) and sometimes without (narrator) — defensible by the rule, but it *looks* inconsistent without the rule stated.
3. It is **precedent-setting** for three more books and is the kind of editorial *whether* that the end-of-book checklist exists to catch (cf. the ἐκκλησία precedent that motivated the checklist).

**DECIDE.** The audit cannot change translations and recommends none here — the shipped surface is internally coherent. What is owed is **Ben's ratification of the two-tier convention** (most likely outcome: keep as-is) **and a corpus doc** (`foreign_monarch_register_2026-05.md` or an `ot_register_policy` §2.2 amendment) that states the narrator-no-`ทรง` / in-address-deferential split, so Nehemiah/Esther/Daniel inherit a written rule rather than re-deriving it. **Severity: MEDIUM** — no surface edit, but it is a corpus-precedent decision the translation deliberately deferred to this moment, and it gates the register handling of every later Persian-court book.

---

## 5. Hebrew↔Aramaic bilingual handling — **STABLE → recommend `biblical_aramaic_sections_2026-05.md`**

Ezra is the corpus's **first language switch mid-book**: ~4:8–6:18 and 7:12–26 (67 verses) are Biblical Aramaic, the rest Hebrew. The handling is mechanically sound:

- **The `language` field tags every verse** correctly (`hebrew` / `aramaic`) — verified across all 10 chapters (ch 4: 7 Heb + 17 Aram; ch 5: 17 Aram; ch 6: 18 Aram + 4 Heb [the 6:19–22 Passover, in Hebrew]; ch 7: 13 Heb + 15 Aram). The Aramaic verses carry the source in an `aramaic` field rather than `hebrew`.
- **The switch is disclosed at verse level.** 4:7 `key_decision` + note ("from 4:8 to 6:18 the original is Aramaic; Aramaic was the administrative language of the Persian empire"); 4:8 note ("the Aramaic original begins here").
- **Divine names map cleanly across the switch** (§2): Aramaic אֱלָהּ → `พระเจ้า`, no YHWH in the Aramaic, so the Tetragrammaton lock simply doesn't fire there — and ch 5 (all-Aramaic, no YHWH) correctly carries no first-occurrence footnote (§1).

The one gap is documentation/reader-facing: there is **no corpus doc** stating the bilingual policy and **no Tier-2/reader footnote** telling the Thai reader that this block was Aramaic in the original (the disclosure lives only in the translator-facing `notes`). This recurs immediately in Daniel (2:4b–7:28), so it is worth locking now.

**STABLE — recommend `biblical_aramaic_sections_2026-05.md`** capturing: the `language`-field convention, the Ezra + Daniel verse ranges, the no-YHWH-footnote-when-all-Aramaic rule, and a decision on whether a reader-facing note is owed. **Severity: LOW.**

---

## 6. Persian administrative titles + "Beyond the River" — **STABLE → recommend `persian_achaemenid_administrative_titles_2026-05.md`**

Ezra introduces the Persian imperial administrative world. The renderings are uniform and verse-documented, but there is **no OT-administrative-titles doc** (`roman_administrative_titles_2026-04.md` is NT-only):

| Source (Heb/Aram) | Thai | Ref |
|---|---|---|
| בְּעֵל־טְעֵם (commander / lord-of-decree) | `เจ้าเมือง` | 4:8, 4:9 |
| סָפְרָא (scribe / secretary) | `อาลักษณ์` | 4:8 |
| פֶּחָה (governor) — Tattenai | `ผู้ว่าราชการแคว้น` | 5:3, 5:6, 6:6, 6:13 |
| גִּזְבָּר (treasurer, Persian loanword) | `เหรัญญิก` | 1:8, 7:21 |
| מִנְדָּה־בְלוֹ וַהֲלָךְ (tax / tribute / toll) | `ส่วย บรรณาการ และค่าธรรมเนียม` | 4:13, 4:20, 7:24 |
| עֲבַר נַהֲרָה ("Beyond the River" / Trans-Euphrates) | `(แคว้น)ฟากตะวันตกของแม่น้ำ(ยูเฟรติส)` | 4:10–11, 4:16–17, 5:3, 6:6, 7:21, 8:36 |

**"Beyond the River" is the one to record explicitly.** It is rendered **descriptively** in verse text (`แคว้นฟากตะวันตกของแม่น้ำ` ×11; the first occurrence 4:10 adds the `ยูเฟรติส` gloss) — uniform, with the proper-name gloss `แคว้นทรานส์ยูเฟรติส` reserved for the explanatory `notes` (18×). This is a defensible reader-first choice (describe the satrapy rather than transliterate a Persian administrative name the Thai reader won't recognize), but it is a translation-policy decision worth locking, since the same term saturates Nehemiah.

**STABLE — recommend `persian_achaemenid_administrative_titles_2026-05.md`** capturing the title set above + the descriptive "Beyond the River" policy + forward-cover (Neh/Esth/Dan). The key-term-consistency check is clean for these (they are uniform), so this is documentation, not a defect. **Severity: LOW.**

---

## 7. "Hand of God" anthropomorphism (יַד אֱלֹהָיו) — **LOCKED**

The recurring Ezra leitmotif "the good hand of his God was upon him" (the providence formula tying the narrative together) renders within `divine_anthropomorphism_thai_grammar_2026-05.md`'s **body-part honorific rule**: the noun takes the royal `พระหัตถ์`, but the **verb does not take `ทรง`** because the grammatical subject is the body-part (the hand), not God directly:

| Ref | Source | Thai | Verb-honorific |
|---|---|---|---|
| 7:6 | יַד־יְהוָה אֱלֹהָיו עָלָיו | `พระหัตถ์ขององค์พระผู้เป็นเจ้าพระเจ้า…อยู่เหนือ` | no `ทรง` on `อยู่เหนือ` ✓ |
| 7:9, 8:18 | כְּיַד אֱלֹהָיו הַטּוֹבָה | `พระหัตถ์อันเปี่ยมด้วยพระกรุณาของพระเจ้า` | ✓ |
| 7:28, 8:22, 8:31 | יַד אֱלֹהָיו / יַד אֱלֹהֵינוּ | `พระหัตถ์ของพระเจ้า…อยู่เหนือ(และปกป้อง)` | ✓ |

The 8:31 `key_decision` cites the policy by name: *"the verb does not use `ทรง` because the subject is the hand (body-part) per the honorifics-binding policy (cf. Ruth 1:13); the hand is a figure for God's power."* This is exactly the body-part-before-`ทรง` rule recorded in the 2 Kings honorifics work, applied uniformly across all six occurrences. The divine-name half tracks the source correctly (YHWH→`องค์พระผู้เป็นเจ้า` where the Hebrew has the Tetragrammaton at 7:6; Elohim→`พระเจ้า` elsewhere).

**LOCKED** ✓ per `divine_anthropomorphism_thai_grammar_2026-05.md` + `honorifics_non_divine_authorities_2026-04.md`.

---

## 8. חֶסֶד covenant-love — **LOCKED**

חֶסֶד occurs in Ezra's confession-prayer context and renders within the `chesed_covenant_love_2026-05.md` family. **9:9** — `וַיַּט־עָלֵינוּ חֶסֶד לִפְנֵי מַלְכֵי פָרַס` "he extended to us steadfast love before the kings of Persia" → **`ทรงสำแดงความรักมั่นคง`** (the locked `ความรักมั่นคง` surface, with `ทรง` because God is the subject) ✓. The surrounding prayer vocabulary is clean: 9:8 "a remnant / a tent-peg in his holy place" → `ที่ยึดเหนี่ยวมั่นคงในสถานบริสุทธิ์`; 9:13 "you have punished us less than our iniquities deserved" → `ทรงลงโทษเราน้อยกว่าที่ความชั่วของเราสมควร`; 9:15 צַדִּיק אַתָּה → `พระองค์ทรงชอบธรรม`.

**LOCKED** ✓ per `chesed_covenant_love_2026-05.md`.

---

## 9. Ezra 10:3 אֲדֹנָי — **REVIEW (read as human "my lord"; MT points it as the divine form)**

In Shecaniah's proposal — `נַעֲשֶׂה כְּ… בַּעֲצַת אֲדֹנָי` "let it be done according to the counsel of *adonai*" — the shipped Thai reads it as the **human** "my lord" (= Ezra), and so does **not** apply the divine `องค์เจ้านาย`. The `key_decision` documents the choice fully:

> *"Here אֲדֹנָי means 'my lord/master' = Ezra (human), not God, per BSB/ESV/NIV (cf. the context of v4 'Arise, this matter is your responsibility'); so `องค์เจ้านาย`, reserved for God, is not used — note: the divine-names checker may raise a C-soft warning, which is a false positive in this case."*

The reading is **defensible and well-supported** (BSB/ESV/NIV all render "my lord"; the immediate context addresses Ezra). The one reason to flag it: the **MT vocalizes אֲדֹנָי (qam​ats) — the form normally reserved for the divine title** — rather than the expected human אֲדֹנִי (hiriq, "my lord"). The Masoretes' pointing is therefore (weak) evidence for a divine reading ("the counsel of the Lord"). This is precisely what the divine-names checker's C-soft warning (the one diff in the dirty `divine_names.md`) is detecting.

**REVIEW.** The rationale is documented at verse level and follows the major English versions, so this is not a tag blocker — but a Hebrew-competent reviewer should confirm the human reading against the MT pointing. Good external-AI item (a focused exegesis/grammar question). **Severity: LOW.**

---

## 10. Cyrus decree — dual version + the 2 Chronicles 36 duplication — **LOCKED / STABLE**

Ezra contains the Cyrus decree **twice**, and both are handled carefully:

- **1:1–4 (Hebrew proclamation)** ≈ **2 Chr 36:22–23**. The 1:1 note documents the near-verbatim overlap and the minor MT differences (Ezra מִפִּי "from the mouth of" vs Chronicles בְּפִי "by the mouth of"), and **1:3 preserves the MT difference** that Ezra reads `אֱלֹהָיו` "his God" *without* the Tetragrammaton where 2 Chr 36:23 reads `יְהוָה אֱלֹהָיו` — rendered `พระเจ้าของเขา` (not `องค์พระผู้เป็นเจ้า`), an explicit MT-faithful preservation. This closes the 2 Chronicles §16 forward-watch (which flagged the Cyrus≈Ezra duplication to be revisited when Ezra shipped) **cleanly** — the duplication is documented, the textual divergence preserved.
- **6:3–5 (Aramaic archival memorandum)** — the official version found at Ecbatana, which differs in content from the 1:2–4 proclamation (temple dimensions "60 cubits high, 60 wide"; royal financing; vessel return). Rendered per MT; the 6:3 dimensions are translated as-is without flagging the well-known missing-length crux or the contrast with Solomon's temple — defensible (MT-faithful, and the crux is below the disclosure floor).

The lexical variation between the two accounts (Hebrew ch 1 `เครื่องใช้`/`อ่าง`/`ชาม` for the vessels vs Aramaic ch 6 `ภาชนะ`) tracks the source-language difference (כְּלֵי vs מָאנֵי) and is not drift.

**LOCKED** (the 2 Chr 36 duplication + MT-divergence preservation) / **STABLE** (the dual-decree handling). No defect; an optional Layer-1 note linking 6:3–5 to 1:2–4 as the same decree in two forms would be polish, not a gap.

---

## 11. Numbers, lists, and the Nehemiah 7 parallel — **STABLE**

Ezra carries two list-heavy chapters (ch 2, the returnees; ch 8, Ezra's traveling company) and the inventory of ch 1. The internal-arithmetic and synoptic divergences are handled MT-faithfully, with notes, **no harmonizing** — the same discipline the 2 Chronicles audit found at its number cruxes:

- **1:9–11** — the itemized vessels (sum ≈ 2,499) vs the stated total 5,400. Note: "the total exceeds the listed items; uW recommends reporting per MT without reconciling; translated per MT."
- **2:1** — the returnee list "parallels Nehemiah 7 (where some group totals differ)" — documents the forward parallel (Neh not yet translated) under the independent-MT principle.
- **2:64** — the grand total 42,360 vs the sum of listed groups (≈ 29,818): "this discrepancy appears in *both* Ezra 2 and Neh 7 and has no clear explanation; translated per MT without reconciling." This is the Ezra analog of the documented 2 Chr number cruxes — MT preserved, divergence disclosed, no silent emendation.

Units (`ศอก` cubit, `ดาริค`/`มินา` where present, talents/minas of gold) and the hapax legomena (1:9 מַחֲלָפִים → `มีด` "knives"; 6:2 דִּכְרוֹן/אַחְמְתָא) are documented at verse level.

**STABLE** ✓. (Contrast the 2 Chr 36:9 DECIDE — an *undocumented* MT departure. Ezra has no analog: every number tension is preserved-with-note.)

---

## 12. MT/LXX disposition (incl. 1 Esdras) — **REVIEW (likely non-gap, but confirm given 1 Esdras's prominence)**

All `output/textual_variants/ezra_NN.json` files contain **only** the per-chapter YHWH first-occurrence footnote — **zero** inclusion-variant / MT-vs-LXX entries — and `audit_inclusion_variants.py --book ezra --strict` = 0 candidates, exit 0. For **verse-level** MT/LXX divergence this is correct and matches the §2.3 floor disposition the 1SA/1KI/2KI/1CH/2CH audits settled.

**The reason to flag (not a defect, a confirmation):** Ezra's distinctive textual feature is not verse-level variants but the **divergent Greek recension 1 Esdras (Esdras A)** — which reorders the Ezra material, omits/relocates blocks, and adds the famous "contest of the three guardsmen / the strength of truth" (1 Esd 3:1–5:6) with no Hebrew/Aramaic counterpart. The straight Greek translation (Esdras B = Ezra-Nehemiah) is close to MT; 1 Esdras is the macro-structural outlier. Under `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3, a macro-structural / canonically-visible divergence is exactly what the floor asks to be *disposed of explicitly*. 1 Esdras is canonically present (deuterocanon in the Orthodox tradition; appended in the Vulgate), so a one-line disposition ("the project translates MT Ezra; 1 Esdras is a separate recension, not a textual variant of MT, so no per-verse disclosure is owed") is worth recording.

**REVIEW.** Recommend adding an Ezra row to `mt_vs_lxx_textual_variant_handling_2026-05.md` §3 stating the 1 Esdras disposition (non-gap: a parallel recension, not an MT variant). No surface change. **Severity: LOW.** (Good external-AI item — a textual-criticism question the AIs can speak to.)

---

## 13. Proper-name transliteration — **STABLE**

Ezra is transliteration-dense: Persian royal names (`ไซรัส` Cyrus, `ดาริอัส` Darius, `อาหสุเอรัส` Ahasuerus/Xerxes, `อารทาเซอร์ซีส` Artaxerxes), Persian officials (`มิทเรดาท`, `เรฮูม`, `ชิมชัย`, `ทัทเธนัย`, `โอสนัปปาร์`/Ashurbanipal), place-names (`เอกบาทานา`, `แคว้นมีเดีย`), and the long returnee + mixed-marriage rosters (chs 2, 8, 10). The `key_decisions` consistently transliterate per `proper_names_and_transliteration_2026-05.md` and cite the parallel where one exists (e.g. `ไซรัส` "per the parallel 2 Chr 36:22"). Decisive evidence: `check_key_term_consistency.py` is clean (0 rule violations, 0 undocumented multi-renderings) across the 678-chapter corpus, which includes Ezra's heavy name load.

**STABLE** ✓.

---

## 14. Inherited corpus locks — all compliant except where flagged

| Doc | EZR evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH ~38 surfaces, 0 ยาห์เวห์, 9/10 footnoted; ch 5 correctly exempt — all-Aramaic, no YHWH); §2 (Elohim + Aramaic אֱלָהּ → พระเจ้า; pagan `เทพเจ้า` at 1:7). | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | §7 — "hand of God" body-part honorific rule held across 7:6/7:9/7:28/8:18/8:22/8:31 (พระหัตถ์ + verb without `ทรง`). | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | §8 — 9:9 `ทรงสำแดงความรักมั่นคง`. | **LOCKED** |
| `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` | §2 — Nebuchadnezzar's gods (1:7) `เทพเจ้า`; 0 `พระเจ้า`-for-pagan. | **LOCKED** |
| `ot_register_policy_2026-05.md` + `honorifics_non_divine_authorities_2026-04.md` | §4 — foreign-monarch register: narrator-no-`ทรง` / in-address-deferential split; **deliberately deferred → DECIDE**. | **DECIDE-§4** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §12 — §2.3 floor → non-gap; 1 Esdras disposition to be recorded → REVIEW. Inclusion audit 0 candidates. | **LOCKED-with-§12-REVIEW** |
| `synoptic_parallel_passages_2026-05.md` | §10 (Cyrus 1:1–4 ≈ 2 Chr 36:22–23, MT divergence preserved at 1:3) + §11 (Ezra 2 ≈ Neh 7, divergence noted at 2:64). Independent-MT principle held. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | §13 — Persian kings/officials/places + returnee rosters; key-term check clean. | **LOCKED** |
| `dtr_history_cycle_formulas_2026-05.md` | **N/A** — Ezra is post-exilic; no Israelite/Judahite regnal-evaluation cycle. The §4 2CH "did evil" drift does **not** recur (no formula to drift). | **N/A** |
| `malak_yhwh_2026-05.md` | **N/A** — no מַלְאָךְ (divine or human) in Ezra (Hebrew/Aramaic grep clean). The standing human-messenger `ผู้สื่อสาร` queue gains no Ezra entry. | **N/A** |
| `leitwort_handling_policy_2026-05.md` | **N/A** — the etiological "until this day" leitwort (עַד הַיּוֹם הַזֶּה) does not occur in Ezra. The cross-book 1SA-outlier decision is untouched. | **N/A** |
| `spirit_of_yhwh_empowerment_2026-05.md` | **N/A** — no Spirit-empowerment idiom in Ezra. | **N/A** |
| `hebrew_oath_formulas_2026-05.md` | **N/A** — חַי־יְהוָה does not occur in Ezra. | **N/A** |

---

## 15. Mechanical (§1) — all green (with the standing infra notes)

- 10/10 chapters: `output/check_reports/ezra_NN_review.md` — all six checks "✅ clean" / "Ready to ship" ✓
- 10/10 chapters: `output/back_translations/ezra_NN.json` ✓
- 10/10 chapters: `output/translations/ezra_NN.json` (280 verses) ✓
- 9/10 chapters: `output/textual_variants/ezra_NN.json` (YHWH first-occurrence footnote). **Ezra 5 correctly carries no file — all-Aramaic, no Tetragrammaton (§1).**
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (678-chapter corpus)
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (20,225 verses). (The DtrH evaluation/high-places/`malak` locks are out of scope for Ezra by design — Ezra has no regnal cycle and no מַלְאָךְ, §14 — so no DTr drift surface exists here, unlike 2CH §4.)
- `audit_inclusion_variants.py --book ezra --strict`: **0 candidates, exit 0** (NT-SBLGNT-tuned heuristic; the Ezra textual layer is the 1 Esdras recension question, §12, not verse-level inclusion).
- `export_to_usfm.py --book EZR`: **N/A** — the script's `BOOKS` table is NT-only; OT USFM export remains the carried-over separate concern noted in every prior OT audit.
- **Book-code registration:** `EZR` was present in `OT_CODES` (so the Hebrew/Aramaic-base packet branch was correct) but **missing from the §3/§4 tooling slug tables** (`build_external_review_packet.py` `BOOKS`; `audit_items_to_yaml.py` `BOOK_SLUGS`) — **registered as part of this audit** per the EOB book-code-registration gotcha.
- `git status output/`: **clean except `output/check_reports/divine_names.md`** — aggregate report whose only diff adds the Ezra 10:3 C-soft אֲדֹנָי warning, which the 10:3 `key_decision` documents as a deliberate false positive (§9); report-only, not a translation surface; identical in kind to the 1SA/1KI/2KI/1CH/2CH note.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **~38**. `ยาห์เวห์` residues: **zero**. Aramaic verses: **67** (correctly `language`-tagged).

**Severity: GREEN.**

---

## 16. Flagged for Ben's attention

### DECIDE (block the `book-ezra-v1` tag until resolved)

**A. Foreign-monarch register (§4).** The translation deliberately deferred the Gentile-emperor register question to this audit (1:2 note). As shipped: narrator voice → no `ทรง` for Persian kings; inside reported letters/decrees → in-world deferential forms (`พระองค์`/`กราบทูล`/`ทรง`). Coherent and verse-documented, but undocumented at corpus level, surface-mixed, and **precedent-setting for Nehemiah/Esther/Daniel**. **Recommend Ben ratify the two-tier convention (likely keep as-is) + write `foreign_monarch_register_2026-05.md` (or amend `ot_register_policy_2026-05.md` §2.2).** No surface edit expected. **MEDIUM.**

### REVIEW (worth Ben's confirmation; not tag blockers)

**B. "God of heaven" doc (§3).** Write `god_of_heaven_persian_title_2026-05.md` — lock `พระเจ้าแห่งฟ้าสวรรค์` for אֱלֹהֵי הַשָּׁמַיִם / אֱלָהּ שְׁמַיָּא (uniform across Ezra's Heb + Aram; heavy in Neh/Dan). **LOW.**

**C. Persian administrative-titles doc (§6).** Write `persian_achaemenid_administrative_titles_2026-05.md` — the title set (`เจ้าเมือง`/`อาลักษณ์`/`ผู้ว่าราชการแคว้น`/`เหรัญญิก`/tax-triplet) + the descriptive "Beyond the River" → `ฟากตะวันตกของแม่น้ำ` policy; forward-cover Neh/Esth/Dan. **LOW.**

**D. Biblical-Aramaic-sections doc (§5).** Write `biblical_aramaic_sections_2026-05.md` — the `language`-field convention, Ezra + Daniel verse ranges, no-YHWH-footnote-when-all-Aramaic rule, and the reader-facing-note question. **LOW.**

**E. 10:3 אֲדֹנָי human-vs-divine reading (§9).** Documented as human "my lord" (= Ezra) per BSB/ESV/NIV; MT points it as the divine form. Confirm the human reading. **LOW.**

**F. 1 Esdras / MT-LXX disposition (§12).** Add an Ezra row to `mt_vs_lxx_textual_variant_handling_2026-05.md` recording 1 Esdras as a separate recension (non-gap, no per-verse disclosure owed). **LOW.**

### Existing docs to amend (optional, no tag block)
- **`ot_register_policy_2026-05.md`** — fold in the §4 foreign-monarch decision (or point to the new doc).
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the Ezra §3-table row (MT Ezra; 1 Esdras separate recension → §2.3 floor non-gap).
- **`synoptic_parallel_passages_2026-05.md`** — record Ezra 1:1–4 ≈ 2 Chr 36:22–23 (with the 1:3 MT-divergence preservation) and Ezra 2 ≈ Neh 7 as downstream tests of the independent-MT principle.
- **`proper_names_and_transliteration_2026-05.md`** — note the Persian royal-name set as shipped.

### External AI review (§3 of checklist) — pending
Recommended 4-item packet (see `external_review_items_EZR.md`):
1. **Foreign-monarch register** (§4-A, DECIDE)
2. **10:3 אֲדֹנָי human-vs-divine** (§9-E, REVIEW)
3. **1 Esdras / MT-LXX disposition** (§12-F, REVIEW)
4. **"God of heaven" rendering** (§3-B, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI/1CH/2CH pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 6 items (§1 YHWH, §2 Elohim/Aramaic/pagan, §7 hand-of-God anthropomorphism, §8 chesed, §10 Cyrus/2 Chr-36 duplication, §13 transliteration; + inherited locks via §14)
- **STABLE:** 4 items (§3 "God of heaven" [→ recommend doc], §5 bilingual handling [→ recommend doc], §6 Persian admin titles [→ recommend doc], §11 numbers/Neh-7 parallel)
- **REVIEW:** 4 items (§3 God-of-heaven doc, §5 Aramaic doc, §6 Persian-titles doc, §9 10:3 אֲדֹנָי, §12 1 Esdras — note §3/§5/§6 carry both a STABLE rendering and a REVIEW doc-recommendation)
- **DECIDE:** 1 item (§4 foreign-monarch register — deliberately deferred to this audit)

**One DECIDE item blocks the `book-ezra-v1` tag** — and unlike the 2 Chronicles DECIDEs (which were lock-anchored surface *defects*), Ezra's single DECIDE is a **clean, deliberately-deferred policy ratification**: the shipped surface is internally coherent; what is owed is Ben's sign-off on the foreign-monarch register convention + a corpus doc so Nehemiah/Esther/Daniel inherit a written rule.

**Three new translator_decisions docs recommended:** `god_of_heaven_persian_title_2026-05.md` (§3), `persian_achaemenid_administrative_titles_2026-05.md` (§6), `biblical_aramaic_sections_2026-05.md` (§5). A fourth (foreign-monarch register) is gated on the §4 DECIDE. Four optional existing-doc amendments (§16).

---

## Recommendation

**Ezra ships in excellent shape — the cleanest OT narrative book since 1 Chronicles, with zero surface defects.** It inherits the Chronicler's locks intact (YHWH, Elohim, pagan register, chesed, anthropomorphism, transliteration all LOCKED/clean), opens by closing the 2 Chronicles §16 forward-watch cleanly (the Cyrus decree, with the 1:3 MT-divergence faithfully preserved), and handles its three genuinely-new surfaces — Biblical Aramaic, the Persian administrative world, and the "God of heaven" title — uniformly and with verse-level rationale. Its number/list cruxes are all preserved-with-note (no 2 Chr 36:9-style silent MT departure).

**The work to do before v1 is overwhelmingly documentation, not correction:**

- **The single DECIDE (§4 foreign-monarch register)** is a policy the translation explicitly *parked for this audit*. It is the corpus's first real test of how Gentile monarchs are honored in Thai, and it sets the precedent for three more Persian-court books. The shipped two-tier convention (narrator-no-`ทรง` / in-address-deferential) is coherent and defensible — the audit recommends ratifying it and writing it down, not changing it.
- **Three new docs** (§3 God-of-heaven, §5 Aramaic, §6 Persian titles) lock the new Persian-period surfaces before they compound into Nehemiah and Daniel — the canonical "lock it before it compounds" work.
- **Two light REVIEW confirmations** (§9 10:3 אֲדֹנָי; §12 1 Esdras) — both documented and defensible, both good external-AI questions.

**Tag `book-ezra-v1` after:**
1. Ben's decision on the **§4 foreign-monarch register** (ratify + doc).
2. Ben's confirmation on the **REVIEW items (§B–§F)** (all LOW).
3. External AI sanity-check (the 4-item packet).
4. Optionally, writing the **three new docs (§B/§C/§D)** and the existing-doc amendments — none gate the tag except the §4 register doc.

**The single highest-value forward-protection step here is the §4 register decision** — it is the rule Nehemiah (next), and then Esther and Daniel, will lean on most heavily, and Ezra is the right place to settle it.
