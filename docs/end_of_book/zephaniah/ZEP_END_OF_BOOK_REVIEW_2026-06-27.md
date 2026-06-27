# Zephaniah — End-of-Book Review

**Date:** 2026-06-27
**Scope:** All 3 chapters of Zephaniah (English versification = MT throughout — Zephaniah carries **no** MT/English divergence zone); `glossary.json`; `docs/translator_decisions/` corpus. Zephaniah is the **eleventh Book-of-the-Twelve title** processed (after Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk). The divine-name inventory is the bare Tetragrammaton (יהוה, dense across all three chapters), the **YHWH-Sabaoth** compound (יְהוָה צְבָאוֹת, 2:9, 2:10), and **one** Adonai-YHWH compound at 1:7 — all rendered uniformly on the `องค์พระผู้เป็นเจ้า` family, with the per-chapter Layer-2 footnote present and correctly typed in **all three** chapters. Two facts give the book editorial weight: **(1)** the Adonai-YHWH compound at **1:7** carries the **same word order** as Amos's headline compound (אֲדֹנָי יְהוִה) yet is rendered **bare** — the cleanest direct counter-witness yet to the open Amos §1; and **(2)** Zephaniah is **the** Day-of-YHWH book of the corpus (the locus classicus of 1:14–16, the *Dies Irae*), making it the keystone witness for the still-unauthored day-of-the-LORD leitwort doc.

**Trigger:** Final chapter of Zephaniah (ZEP 3) shipped via `scripts/ship_chapter.sh`; `scripts/detect_book_complete.py` fired the end-of-book audit.

**Mandate:** §2 (Editorial review) + §3 (External AI packet) of `docs/END_OF_BOOK_CHECKLIST.md`. **Assessment only — no translation JSON was modified.**

## Summary

- **10 cross-cutting items reviewed.**
- **0 items flagged DECIDE.** Zephaniah is **cleanest-tier** alongside Obadiah and Nahum: every mechanical gate is green, no versification zone is owed, the Layer-2 divine-name footnote is present and correctly typed in all three chapters, and no new lemma forces a fresh corpus decision. The two consequential editorial items are both **contingent/confirmatory** REVIEWs, not standalone Ben-blocks.
- **3 items flagged REVIEW** (worth Ben's confirmation; no change proposed):
  - **§3 — the lone Adonai-YHWH compound (אֲדֹנָי יְהוִה, 1:7) → bare `องค์พระผู้เป็นเจ้า`.** Complies with `divine_names_table_2026-05` **and** with the bare-path recommendation of the open Amos §1. Critically, Zephaniah's compound is the **identical word order** to Amos's (אֲדֹנָי יְהוִה, not the reversed Psalter-colophon form of Habakkuk 3:19) — so this is the **strongest path-a witness in the corpus**: the same Hebrew Amos rendered as the anomalous expanded `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`, Zephaniah renders bare. Contingent on the Amos §1 resolution; re-opens only under path-b.
  - **§9 — 3:17 יַחֲרִישׁ בְּאַהֲבָתוֹ ("he will quiet [you] in his love") → `จะทรงให้เจ้าสงบนิ่งด้วยความรัก`.** The book's tender climax; the MT reading is followed and the famous LXX variant (יְחַדֵּשׁ "he will **renew** you in his love") is footnoted. MT-primary per RULES §0; flagged because it is a beloved, much-translated verse worth an explicit confirmation.
  - **§10 — `export_to_usfm.py` rejects `ZEP`** (infrastructure, non-blocking; the standing minor-prophet apparatus gap).
- **4 items LOCKED** — §1 (Tetragrammaton Layer-1 + Layer-2 footnote), §2 (YHWH-Sabaoth), §5 (anthropomorphism minimal pair), §7 (versification — no zone).
- **3 items STABLE** — §4 (Day-of-YHWH leitwort), §6 (messianic restraint / YHWH-as-King), §8 (MT textual-variant disclosure + hapax handling).
- **Mechanical gate: fully GREEN.** `check_key_term_consistency` 0 violations; `check_phrase_consistency` 0 violations (38 locks audited, 30 584 verses); `check_divine_names` **ZERO Zephaniah warnings** (no standalone-Adonai `C-soft` flags, no human-subject false-positive class); `audit_inclusion_variants --book zephaniah --strict` **0 candidates**; all 3 per-chapter `*_review.md` green; all 3 `back_translations/zephaniah_NN.json` present; all 3 `textual_variants/zephaniah_NN.json` present with the **correct** `tetragrammaton_convention_first_occurrence` footnote type in **every** chapter (no Joel-ch3 type-mismatch, no Micah-ch5 / Lamentations-ch2-3 missing-footnote gap); no versification-map entries owed (Zephaniah has no MT divergence zone).
- **External AI review (§3) packet:** focused **2-item** packet — the Adonai-YHWH bare-collapse at 1:7 (§3, REVIEW) and the 3:17 quiet/renew crux (§9, REVIEW). The infra item (§10) is not an externally-reviewable translation question and is excluded, matching the Amos/Obadiah/Micah/Nahum/Habakkuk packet scoping. All LOCKED/STABLE items are excluded.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Divine names — Tetragrammaton Layer-1 uniform + Layer-2 footnote present in every chapter — **LOCKED**

YHWH appears densely in all three chapters and is rendered **`องค์พระผู้เป็นเจ้า`** uniformly (Layer 1, `divine_names_table_2026-05`):

- **Ch.1:** 1:1, 1:2, 1:3, 1:5, 1:6 (×2), 1:7 (the אֲדֹנָי יְהוִה compound + יוֹם יְהוָה), 1:8, 1:10, 1:12, 1:14 (×2), 1:17, 1:18 — first occurrence footnoted at 1:1.
- **Ch.2:** 2:2 (×2), 2:3 (×2), 2:5, 2:7, 2:9 (יְהוָה צְבָאוֹת), 2:10 (יְהוָה צְבָאוֹת), 2:11 — first occurrence footnoted at 2:2.
- **Ch.3:** 3:2, 3:5, 3:8, 3:9, 3:12, 3:15 (×2, incl. מֶלֶךְ יִשְׂרָאֵל יְהוָה), 3:17, 3:20 — first occurrence footnoted at 3:2.

The Layer-2 apparatus is **complete and correct**: each chapter's `textual_variants/zephaniah_NN.json` carries a `tetragrammaton_convention_first_occurrence` entry, with the ch.1 footnote explicitly flagging that **1:7 is the compound rendered bare**. `check_divine_names.py` reports **zero** Zephaniah entries in its corpus warning list — no false-positive human-subject verses (1:9 אֲדֹנֵיהֶם "their masters" is correctly read as the human-master plural and left plain `นาย`, the same true-negative class as Amos 4:1). This is **cleanest-tier**: unlike Micah (Layer-2 footnote missing in ch.5), Lamentations (ch.2/ch.3 gap), or Joel (ch.3 wrong footnote type), Zephaniah's per-chapter first-occurrence footnote is present **and** correctly typed in all three chapters. **LOCKED** ✓ (`divine_names_table_2026-05`). **Severity: GREEN.**

---

## 2. YHWH-Sabaoth (`יְהוָה צְבָאוֹת`) → `องค์พระผู้เป็นเจ้าจอมโยธา` — **LOCKED**

The compound appears twice, at **2:9** (`חַי־אָנִי נְאֻם יְהוָה צְבָאוֹת אֱלֹהֵי יִשְׂרָאֵל`) → **`องค์พระผู้เป็นเจ้าจอมโยธา พระเจ้าแห่งอิสราเอล`** and **2:10** (`עַל־עַם יְהוָה צְבָאוֹת`) → **`ประชากรขององค์พระผู้เป็นเจ้าจอมโยธา`**. Both are **identical to the locked form** at `divine_names_table_2026-05` ("**องค์พระผู้เป็นเจ้าจอมโยธา** — Identical to already-shipped Jas 5:4; visual unity preserved across testaments") and match the Habakkuk 2:13, Nahum 2:14 / 3:5, Isaiah, Jeremiah, and Psalms uses of the same Hebrew form. Correctly distinct from the corpus's `พระเจ้าจอมโยธา`, which renders the *different* form `אֱלֹהֵי צְבָאוֹת` ("**God** of hosts"). **LOCKED** ✓. **Severity: GREEN.**

---

## 3. The Adonai-YHWH compound at 1:7 (`אֲדֹנָי יְהוִה`) → bare `องค์พระผู้เป็นเจ้า` — **REVIEW** (the strongest witness for the open Amos §1)

Zephaniah's single Adonai-YHWH compound opens the Day-of-YHWH oracle: **1:7** `הַס מִפְּנֵי אֲדֹנָי יְהוִה` → **`จงเงียบสงบต่อหน้าองค์พระผู้เป็นเจ้า`**. The `key_decisions` explicitly records the underlying compound and renders it as the **single bare title** `องค์พระผู้เป็นเจ้า` "per the corpus standard for the Adonai-YHWH compound."

What makes this the **decisive data point** for the open Amos §1: Zephaniah's compound carries the **identical word order** to Amos's — אֲדֹנָי יְהוִה (Adonai *first*, then YHWH-vocalized-as-Elohim) — **not** the reversed Psalter-colophon form (יְהוִה אֲדֹנָי) that Habakkuk 3:19 used. So where Amos surfaced *exactly this Hebrew string* and rendered it as the **expanded** `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` (20×/19, anomalous against the entire rest of the corpus), Zephaniah renders **the same string bare**, the form Ezekiel (217×), Isaiah (30×), Jeremiah, Obadiah (1:1), Micah (1:2), and Habakkuk (3:19) all use. Zephaniah is therefore the cleanest possible **path-a witness** (normalize to bare): it removes the "different word order" hedge that softened the Habakkuk 3:19 comparison.

**Why REVIEW, not LOCKED:** the rendering is correct under the current table, but the table's treatment of the compound is exactly what Amos §1 placed under review. Zephaniah does not *open* a new question; it adds the strongest data point. **Confirm** the bare collapse at 1:7 is intended (no change proposed); this item re-opens only if Amos §1 resolves toward path-b (expanded), in which case 1:7 — and Obadiah/Micah/Habakkuk — would all need to follow. **Severity: GREEN (compliant; flagged as the lead contingent witness to the open Amos §1).**

---

## 4. Day-of-YHWH leitwort (`יוֹם יְהוָה`) → `วันแห่งองค์พระผู้เป็นเจ้า` — **STABLE** (recommend a corpus doc)

Zephaniah is **the** Day-of-the-LORD book — the densest concentration of the יוֹם יְהוָה motif in the corpus, and the source of the Western church's *Dies Irae*. The thread is rendered uniformly:

- **Plain "Day of YHWH":** 1:7 `קָרוֹב יוֹם יְהוָה` → `วันแห่งองค์พระผู้เป็นเจ้าใกล้เข้ามา`; 1:14 (×2) `יוֹם יְהוָה הַגָּדוֹל` → `วันแห่งองค์พระผู้เป็นเจ้าอันยิ่งใหญ่`.
- **Construct extensions, consistently chained:** 1:8 `יוֹם זֶבַח יְהוָה` → `วันแห่งเครื่องบูชาขององค์พระผู้เป็นเจ้า`; 2:2 (×2) / 2:3 `יוֹם אַף־יְהוָה` → `วันแห่งพระพิโรธขององค์พระผู้เป็นเจ้า`.
- **The "day of wrath" litany (1:15–16)** — `יוֹם עֶבְרָה … יוֹם צָרָה וּמְצוּקָה … יוֹם חֹשֶׁךְ וַאֲפֵלָה` → the anaphoric `วันแห่ง…` cascade, preserving the sixfold drumbeat that became the *Dies Irae*.
- **"On that day" / "at that time"** as the eschatological hinge in ch.3 (3:11, 3:16, 3:18–20) tying judgment to restoration.

This is `leitwort_handling_policy_2026-05` applied cleanly and at the highest density in the corpus. The Day-of-YHWH motif now spans Joel, Amos, Obadiah, and Zephaniah; each prior audit *recommended* a dedicated `day_of_the_lord_leitwort` doc but none has been authored. **Zephaniah is the keystone witness** — it should anchor that doc if Ben elects to lift it. **STABLE** ✓ (governed by `leitwort_handling_policy_2026-05`; no Zephaniah-specific lock owed). **Severity: GREEN.**

---

## 5. Divine anthropomorphism — the 1:4 / 2:13 minimal pair — **LOCKED**

Zephaniah supplies the cleanest **minimal pair** in the corpus for `divine_anthropomorphism_thai_grammar_2026-05`: the **same idiom** (נטה יד "stretch out the hand") appears once in first-person divine speech and once in third-person narration, and the grammar splits exactly as the doc prescribes:

- **1:4 — first-person divine speech → plain:** `וְנָטִיתִי יָדִי עַל־יְהוּדָה` "I will stretch out **my** hand against Judah" → **`เราจะเหยียดมือของเราออกต่อสู้ยูดาห์`** — plain `มือ`, no royal `พระหัตถ์`, because God speaks in the first person (`เรา`).
- **2:13 — third-person narration → royal:** `וְיֵט יָדוֹ עַל־צָפוֹן` "He will stretch out **his** hand against the north" → **`พระองค์จะทรงเหยียดพระหัตถ์ออกต่อสู้ดินแดนทางทิศเหนือ`** — royal `พระหัตถ์`, with the serial verbs after it left plain (ทำลาย, ทำให้) to avoid the body-part-then-`ทรง` honorifics trap (the KD explicitly cites HAB 3:6/3:12).

Two further first-person divine body-part / non-divine cases confirm the rule: **1:18** shifts mid-clause from first-person to third-person royal (`ของพระองค์`, `ทรงกระทำ`) tracking the Hebrew person-shift; **1:9 / 1:15** keep the human passer-by's hand plain. Note the contrast with **Habakkuk**, which had *no* first-person body-part-plain case: Zephaniah **does** exercise the contested first-person-plain sub-rule at **1:4**, so it is a **live compliance witness** to the open Isaiah/Jeremiah/Ezekiel §13 first-person-plain DECIDE — the codified KD rule (now standard since Jeremiah/Ezekiel) is applied correctly here, against the strongest possible test (a within-book minimal pair). Because the governing doc **exists** and Zephaniah follows it exactly, this is **LOCKED** ✓ (`divine_anthropomorphism_thai_grammar_2026-05`); the 1:4 instance reinforces, but does not re-open, §13. **Severity: GREEN.**

---

## 6. Messianic restraint / YHWH-as-King (3:15, 3:17) — **STABLE**

Zephaniah has **no** messianic figure — no מָשִׁיחַ, no Davidic ruler, no Branch. Its climactic kingship texts identify **YHWH himself** as Zion's king and savior:

- **3:15** `מֶלֶךְ יִשְׂרָאֵל יְהוָה בְּקִרְבֵּךְ` → **`องค์พระผู้เป็นเจ้าจอมกษัตริย์แห่งอิสราเอลสถิตอยู่ท่ามกลางเจ้า`** — YHWH as King-in-the-midst.
- **3:17** `יְהוָה אֱלֹהַיִךְ בְּקִרְבֵּךְ גִּבּוֹר יוֹשִׁיעַ` → **`องค์พระผู้เป็นเจ้า…ทรงเป็นวีรบุรุษผู้ประทานความรอด`** — "a warrior who saves," the book's tender climax (God rejoicing over his people).

These are rendered as straightforward statements about YHWH, with the "in-your-midst" refrain (`בְּקִרְבֵּךְ`, vv. 5/15/17 → `ท่ามกลางเจ้า`) carried consistently. No summary asserts a bare `คือพระคริสต์`; the Christian reading of God-dwelling-with-his-people (cf. John 1:14) is left implicit. This holds the **committal-messianic-surface policy** cleanly (Isaiah §0; the regression Ezekiel §14 flagged) — there is simply nothing here to over-claim, so restraint is trivially satisfied. **STABLE** ✓. **Severity: GREEN.**

---

## 7. Versification — no MT/English divergence zone — **LOCKED**

Zephaniah's three chapters follow a versification in which **MT = English throughout**; there is no offset zone (contrast Joel ch.3/4, Micah ch.4/5, and Nahum ch.2). `grep` confirms **zero** Zephaniah entries are owed in `data/versification_map.json`, and the per-chapter `versification_*` check reports are green for all three chapters. This is **cleanest-tier** alongside Amos, Obadiah, and Habakkuk — no zone to register, nothing retrofitted. **LOCKED** ✓ (`verse_schema_and_versification_2026-05`). **Severity: GREEN.**

---

## 8. MT textual-variant disclosure + hapax / crux handling — **STABLE**

Zephaniah carries several of the OT's harder clauses, and the apparatus handles them conservatively and transparently — MT in the body, the difficulty disclosed in the footnote (`audit_inclusion_variants` found **0** candidates, so no Tier-2 inclusion file is owed; these are §2.3 **non-gaps**):

- **1:3** `וְהַמַּכְשֵׁלוֹת אֶת־הָרְשָׁעִים` (broken syntax, "the stumbling-blocks/idols with the wicked") → `สิ่งที่ทำให้สะดุดพร้อมกับคนชั่ว`, difficulty flagged.
- **1:5** `מַלְכָּם` (MT-vocalized "Malkam") read as the Ammonite deity **Milcom** (`พระมิลโคม`) on the YHWH-contrast, footnoted.
- **2:1** `הַגּוֹי לֹא נִכְסָף` (root כסף ambiguous: "long for" / "be ashamed") → `ชนชาติที่ไม่รู้จักละอาย`, the repentance-context reading.
- **2:14** `כִּי אַרְזָה עֵרָה` (hapax אַרְזָה "cedar-work"; verb עֵרָה) read as stative passive "the cedar-work is laid bare" → `ไม้สนซีดาร์…ถูกรื้อจนเปลือยเปล่า`, with the alternative (God as subject) noted.
- **3:8** `לְיוֹם קוּמִי לְעַד` — the לְעַד crux ("as a witness" / "for prey" / "forever"); the LXX/BSB "witness" reading taken (`เป็นพยานปรักปรำ`), footnoted.
- **3:18** one of the most broken verses in the book (`נוּגֵי מִמּוֹעֵד…`) — rendered along the consensus reconstruction, difficulty flagged.

Sound-plays are preserved-in-sense and footnoted (2:4 `עַזָּה עֲזוּבָה` / `עֶקְרוֹן תֵּעָקֵר`, the Philistine-city pun), and the Sodom/Gomorrah and Babel-reversal (3:9) allusions are carried with cross-reference notes. **STABLE** ✓ (uniform and principled; `mt_vs_lxx_textual_variant_handling_2026-05` + `hebrew_idioms_and_metaphor_2026-05` govern the pattern; no Zephaniah-specific doc owed). **Severity: GREEN.**

---

## 9. The 3:17 climax — `יַחֲרִישׁ בְּאַהֲבָתוֹ` ("he will quiet you in his love") vs the LXX "renew" — **REVIEW**

Zephaniah 3:17b, `יַחֲרִישׁ בְּאַהֲבָתוֹ`, is the book's tender climax and one of the most beloved verses in the Twelve. The Eremos rendering follows the **MT** — **`จะทรงให้เจ้าสงบนิ่งด้วยความรักของพระองค์`** ("he will quiet you with his love") — and footnotes the famous variant: the **LXX read יְחַדֵּשׁ "he will renew you in his love"** (a one-consonant difference, ר/ד confusion), the reading many modern translations and worship settings prefer.

The translation decision is correct under RULES §0 (OT base = MT) and the variant is properly disclosed (`textual_variants/zephaniah_03.json`). It is flagged **REVIEW** — not because anything is wrong, but because this is a high-visibility verse where the MT/LXX fork produces two quite different devotional images ("God grows quiet in his love" vs. "God renews you in his love"), and a deliberate confirmation that the MT image is the intended Eremos surface is worth having on record before the v1 tag. **No change proposed.** **Severity: GREEN (MT-faithful and footnoted; confirmation wanted on a landmark verse).**

---

## 10. Infrastructure — `export_to_usfm.py` rejects `ZEP` — **REVIEW (infra, non-blocking)**

`scripts/export_to_usfm.py` does not yet accept the Zephaniah book code (`✗ Unknown book code: ZEPHANIAH` — the standing minor-prophet apparatus gap, the same item flagged at Joel/Amos/Obadiah/Micah/Nahum/Habakkuk). As part of this audit, `ZEP` **has been registered** in `scripts/build_external_review_packet.py` (the `BOOKS` slug dict — it was already in `OT_CODES`, the same Micah-class gap that fails the packet build until added) and in `scripts/audit_items_to_yaml.py` (`BOOK_SLUGS`). This is a non-translation, non-blocking infrastructure item; it does not affect the v1 tag. **Severity: GREEN (infra; does not gate the tag).**

---

## Items reviewed that need no action

- **The four-point compass of judgment (ch.2)** — Philistia (west, 2:4–7), Moab/Ammon (east, 2:8–11), Cush (south, 2:12), Assyria/Nineveh (north, 2:13–15). All proper nouns transliterated per `proper_names_and_transliteration_2026-05` (กาซา, อัชเคโลน, อัชโดด, เอโครน, เคเรธี, โมอับ, อัมโมน, คูช, อัสซีเรีย, นีนะเวห์). No named foreign **monarch** appears, so the open foreign-monarch-register thread (Ezra→Daniel; Jeremiah/Ezekiel) is **not** implicated.
- **Nineveh's boast (2:15)** `אֲנִי וְאַפְסִי עוֹד` "I am, and there is none besides me" → `มีแต่เราเท่านั้น ไม่มีผู้ใดอื่นอีก` — the usurpation of YHWH's self-predication (cf. Isa 45:5-6; 47:8) carried with a cross-reference note; `יָדוֹ` here is the human passer-by's hand (gesture of scorn) → plain `มือ`, correctly not royal.
- **The restoration formula `שׁוּב שְׁבוּת`** (2:7, 3:20) → `กลับสู่สภาพดีดังเดิม` — rendered uniformly at both the Philistia-remnant promise and the book's closing seal (`אָמַר יְהוָה`).
- **`פָּקַד` "visit" — punitive vs. positive sense** — punitive at 1:8, 1:9, 1:12 (`ลงโทษ`) and positive at 2:7 (`ทรงเยี่ยมเยียนดูแล`); the same lemma's two senses are correctly distinguished by context, `check_key_term_consistency`-clean.
- **The threefold `בַּקְּשׁוּ` "seek" (2:3)** — the book's theological center → `จงแสวงหา…จงแสวงหา…จงแสวงหา`, with `אוּלַי` "perhaps" (`บางที`) keeping grace genuinely open, not presumed.
- **Divine-names false-positive class** — `check_divine_names` produces **zero** Zephaniah warnings (the 1:9 human-master `אֲדֹנֵיהֶם` correctly left plain; no Amos-4:1-style flag). Cleanest possible state.

## Recommended new / amended translator-decisions docs

These are **recommendations only** — per the checklist, this audit recommends but does not author corpus docs. **None is *owed*** (no DECIDE resolved into a lock):

1. **`day_of_the_lord_leitwort_2026-06.md`** (§4) — the Day-of-YHWH motif now spans Joel, Amos, Obadiah, and Zephaniah, each prior audit recommending the doc. **Zephaniah is the keystone** (densest usage, the *Dies Irae* litany of 1:14–16) and should anchor the doc if Ben elects to lift it: record `יוֹם יְהוָה` → `วันแห่งองค์พระผู้เป็นเจ้า`, the construct-chain extensions (`יוֹם זֶבַח/אַף יְהוָה`), and the `วันแห่ง…` anaphora policy.
2. **`divine_names_table_2026-05` — note the bare collapse governs both compound word orders** (§3): Zephaniah 1:7 (`אֲדֹנָי יְהוִה`, Amos's order) and Habakkuk 3:19 (`יְהוִה אֲדֹנָי`, the reversed Psalter form) both collapse identically to bare `องค์พระผู้เป็นเจ้า`. Defer until Amos §1 resolves, since that decision governs the row.

## Checklist for Ben before tagging `book-zephaniah-v1`

- [ ] **§3 REVIEW** — confirm the bare collapse of `אֲדֹנָי יְהוִה` at 1:7 (the strongest path-a witness for the open Amos §1; same word order as Amos, rendered bare). No change proposed; re-opens only under an Amos path-b decision.
- [ ] **§9 REVIEW** — confirm the MT reading at 3:17 (`สงบนิ่ง` "quiet you in his love") over the LXX "renew" variant (footnoted). No change proposed.
- [ ] **§10 REVIEW** — acknowledge the `export_to_usfm.py` `ZEP` gap (infra; non-blocking; packet/YAML registration done in this audit).
- [ ] *(Optional)* greenlight the `day_of_the_lord_leitwort` doc (§4), anchored on Zephaniah.
- [ ] Tag `book-zephaniah-v1` after the three REVIEW confirmations. **No DECIDE blocks the tag.**

*Status counts: 4 LOCKED · 3 STABLE · 3 REVIEW · 0 DECIDE.*
