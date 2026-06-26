# Habakkuk — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 3 chapters of Habakkuk (English versification = MT throughout — Habakkuk carries **no** MT/English divergence zone); `glossary.json`; `docs/translator_decisions/` corpus. Habakkuk is the **eighth Book-of-the-Twelve title** processed (after Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum). One fact dominates the review and pulls it toward *clean*: Habakkuk's divine-name inventory is the bare Tetragrammaton (יהוה), the **YHWH-Sabaoth** compound (יְהוָה צְבָאוֹת, 2:13), the poetic **Eloah / Holy One** (אֱלוֹהַ / קָדוֹשׁ, 3:3), and **one** Adonai-YHWH compound at the closing colophon (יְהוִה אֲדֹנָי, 3:19) — all rendered uniformly on the `องค์พระผู้เป็นเจ้า` family, with the per-chapter Layer-2 footnote present and correctly typed in **all three** chapters. The two items that carry editorial weight are both reception/cross-testament questions, not mechanical defects: **(1)** the rendering of אֱמוּנָה at **2:4** ("the righteous shall live by his faith") — the corpus's single most NT-cited OT verse (Rom 1:17; Gal 3:11; Heb 10:38) and the Reformation cornerstone — as `ความเชื่ออันมั่นคง` "steadfast faith"; and **(2)** the bare collapse of the Adonai-YHWH compound at **3:19**, a witness for the open Amos §1 path.

**Trigger:** Final chapter of Habakkuk (HAB 3) shipped via `scripts/ship_chapter.sh`; `scripts/detect_book_complete.py` fired the end-of-book audit.

**Mandate:** §2 (Editorial review) + §3 (External AI packet) of `docs/END_OF_BOOK_CHECKLIST.md`. **Assessment only — no translation JSON was modified.**

## Summary

- **10 cross-cutting items reviewed.**
- **1 item flagged DECIDE:**
  - **§4 — אֱמוּנָה at 2:4 → `ความเชื่ออันมั่นคง` "steadfast faith."** The book's theological heart and the corpus's most NT-cited OT verse (Rom 1:17; Gal 3:11; Heb 10:38). The translation follows the **MT** (the righteous person's *own* faithfulness, suffix בֶּאֱמוּנָתוֹ) and footnotes the NT reception, which cites the **LXX** (ἐκ πίστεως, possessive dropped). The corpus-level *whether* — should the landmark OT verse read `ความเชื่ออันมั่นคง` while its three NT citations read the plain `โดยความเชื่อ`? — is exactly the cross-testament consistency call the EOB audit exists to surface. **Ben's ratification wanted before the v1 tag.**
- **2 items flagged REVIEW** (worth Ben's confirmation; no change proposed):
  - **§3 — the lone Adonai-YHWH compound (יְהוִה אֲדֹנָי, 3:19) → bare `องค์พระผู้เป็นเจ้า`.** Complies with `divine_names_table_2026-05` line 22 *and* with the **bare-path recommendation of the open Amos §1** — Habakkuk is a clean path-a witness, alongside Obadiah and Micah. Contingent on the Amos §1 resolution; re-opens only under path-b.
  - **§10 — `export_to_usfm.py` rejects `HAB`** (infrastructure, non-blocking; the standing minor-prophet apparatus gap).
- **4 items LOCKED** — §1 (Tetragrammaton Layer-1 + Layer-2 footnote), §2 (YHWH-Sabaoth), §7 (anthropomorphism), §8 (versification — no zone).
- **3 items STABLE** — §5 (NT-reception apparatus at 2:3 → Heb 10:37, MT-primary + footnoted), §6 (messianic restraint at 3:13), §9 (MT textual-variant disclosure + hapax handling).
- **Mechanical gate: fully GREEN.** `check_key_term_consistency` 0 violations; `check_phrase_consistency` 0 violations; `check_divine_names` **ZERO Habakkuk warnings** (no standalone-Adonai `C-soft` flags, no human-subject false-positive class); `audit_inclusion_variants --book habakkuk --strict` **0 candidates**; all 3 per-chapter `*_review.md` green; all 3 `back_translations/habakkuk_NN.json` present; all 3 `textual_variants/habakkuk_NN.json` present with the **correct** `tetragrammaton_convention_first_occurrence` footnote type in **every** chapter (no Joel-ch3 type-mismatch, no Micah-ch5 / Lamentations-ch2-3 missing-footnote gap); no versification-map entries owed (Habakkuk has no MT divergence zone).
- **External AI review (§3) packet:** focused **2-item** packet — the אֱמוּנָה rendering (§4, DECIDE) and the Adonai-YHWH bare-collapse at the colophon (§3, REVIEW). The infra item (§10) is not an externally-reviewable translation question and is excluded, matching the Amos/Obadiah/Micah/Nahum packet scoping. All LOCKED/STABLE items are excluded.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Divine names — Tetragrammaton Layer-1 uniform + Layer-2 footnote present in every chapter — **LOCKED**

YHWH appears in all three chapters — **1:2, 1:12** (ch.1); **2:2, 2:13** (יְהוָה צְבָאוֹת), **2:14, 2:16, 2:20** (ch.2); **3:2** (×2), **3:8, 3:18, 3:19** (the יְהוִה אֲדֹנָי compound; ch.3) — and is rendered **`องค์พระผู้เป็นเจ้า`** uniformly (Layer 1, `divine_names_table_2026-05`). The Layer-2 apparatus is **complete and correct**:

- `textual_variants/habakkuk_01.json` — `tetragrammaton_convention_first_occurrence`, first occurrence at 1:2, lists 1:2 and 1:12.
- `textual_variants/habakkuk_02.json` — `tetragrammaton_convention_first_occurrence`, first occurrence at 2:2, lists 2:2, 2:13 (the Sabaoth form), 2:14, 2:16, 2:20.
- `textual_variants/habakkuk_03.json` — `tetragrammaton_convention_first_occurrence`, first occurrence at 3:2, lists 3:2 (×2), 3:8, 3:18, 3:19 (and flags 3:19 as the compound).

`check_divine_names.py` reports **zero** Habakkuk entries in its corpus warning list — Habakkuk has **no false-positive** human-subject verses. This is **cleanest-tier**: unlike Micah (Layer-2 footnote missing in ch.5), Lamentations (ch.2/ch.3 gap), or Joel (ch.3 wrong footnote type), Habakkuk's per-chapter first-occurrence footnote is present **and** correctly typed in all three chapters. **LOCKED** ✓ (`divine_names_table_2026-05`). **Severity: GREEN.**

---

## 2. YHWH-Sabaoth (`יְהוָה צְבָאוֹת`) → `องค์พระผู้เป็นเจ้าจอมโยธา` — **LOCKED**

The compound appears once, at **2:13** (`הֲלוֹא הִנֵּה מֵאֵת יְהוָה צְבָאוֹת`) → **`ดูเถิด นี่มาจากองค์พระผู้เป็นเจ้าจอมโยธามิใช่หรือ`**. This is **identical to the locked form** at `divine_names_table_2026-05` line 23 ("**องค์พระผู้เป็นเจ้าจอมโยธา** — Identical to already-shipped Jas 5:4; visual unity preserved across testaments") and matches the Nahum 2:14 / 3:5, Isaiah, Jeremiah, and Psalms uses of the same Hebrew form. It is correctly distinct from the corpus's `พระเจ้าจอมโยธา`, which renders the *different* form `אֱלֹהֵי צְבָאוֹת` ("**God** of hosts"). **LOCKED** ✓. **Severity: GREEN.**

---

## 3. The lone Adonai-YHWH compound at the colophon (`יְהוִה אֲדֹנָי`, 3:19) → bare `องค์พระผู้เป็นเจ้า` — **REVIEW** (contingent on the open Amos §1)

Habakkuk's single Adonai-YHWH compound closes the book: **3:19** `יְהוִה אֲדֹנָי חֵילִי` → **`องค์พระผู้เป็นเจ้าทรงเป็นกำลังของข้าพเจ้า`**. Note this is the **reversed-order** form (YHWH-vocalized-as-Elohim *then* Adonai — the form standard in the Psalter colophons, e.g. Ps 68:21, 109:21, 140:8, 141:8), as distinct from Amos's word order אֲדֹנָי יְהוִה. The `key_decisions` explicitly records the underlying compound and renders it as the **single bare title** `องค์พระผู้เป็นเจ้า`, "per the corpus standard for the Adonai-YHWH compound (bare … not a doubled title)."

This is fully compliant with `divine_names_table_2026-05` line 22 (the compound collapses to a single Thai rendering; the `key_decisions` records the underlying form). More importantly, it is a **clean witness for the bare-rendering path of the still-open Amos §1 DECIDE**: where Amos surfaced אֲדֹנָי יְהוִה rendered as the *expanded* `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` (20×/19, anomalous against the rest of the corpus), Habakkuk — like Obadiah (1:1) and Micah (1:2) before it — renders the compound **bare**, the form Ezekiel (217×), Isaiah, and Jeremiah all use. Habakkuk thus **votes path-a** (normalize to bare).

**Why REVIEW, not LOCKED:** the rendering is correct under the current table, but the table's treatment of the compound is exactly what Amos §1 has placed under review. Habakkuk does not *open* a new question; it adds a data point. **Confirm** the bare collapse at 3:19 is the intended rendering of the climactic colophon title (no change proposed); this item re-opens only if Amos §1 resolves toward path-b (expanded). **Severity: GREEN (compliant; flagged as a contingent witness to the open Amos §1).**

---

## 4. "The righteous shall live by his faith" (אֱמוּנָה, 2:4) → `ความเชื่ออันมั่นคง` "steadfast faith" — **DECIDE**

Habakkuk 2:4b, `וְצַדִּיק בֶּאֱמוּנָתוֹ יִחְיֶה`, is the theological heart of the book and the single **most NT-cited OT verse in the corpus** — lifted at **Romans 1:17, Galatians 3:11, and Hebrews 10:38**, and the textual cornerstone of the Reformation. The Eremos rendering is **`ส่วนคนชอบธรรมจะดำรงชีวิตอยู่ด้วยความเชื่ออันมั่นคงของเขา`** — "but the righteous will live by his **steadfast faith**."

The translation decision (recorded in the `key_decisions` and the `habakkuk_02.json` v4 footnote) is principled and MT-faithful:
- **אֱמוּנָה holds two senses** — "faithfulness / steadfastness" (covenant loyalty) and "faith / trust." The rendering `ความเชื่ออันมั่นคง` ("steadfast/firm faith") was chosen to carry **both** — the firmness of the root *and* the trust dimension.
- **The MT suffix בֶּאֱמוּנָתוֹ = "by HIS [own] faithfulness"** — the righteous person's steadfast trust, *not* God's faithfulness. The translation preserves the possessive (`…ของเขา`). This is the correct MT reading per RULES §0 (OT base = MT).
- **The NT citations follow the LXX** (`ὁ δίκαιος ἐκ πίστεώς [μου] ζήσεται`), which renders אֱמוּנָה as πίστις and — in the form Paul quotes — **drops the possessive suffix entirely** ("the righteous shall live by faith"). The footnote discloses this MT/LXX/NT divergence and notes that the NT reads the verse "in the dimension of justifying faith," while the MT context "emphasizes living with steadfast faithfulness amid crisis."

**Why this is a DECIDE, not a STABLE/REVIEW:** every mechanical and verse-level box is checked — but the *corpus-level whether* is open and consequential. A Thai reader who cross-references Habakkuk 2:4 against its three NT citations (which, in the Eremos NT, render the Pauline/Hebrews quotations) will read **`ความเชื่ออันมั่นคง`** in the OT and **`โดยความเชื่อ`** (plain "by faith") in the NT. Is that intended divergence (faithful to MT-vs-LXX, with the footnote bridging) the corpus policy for its landmark cross-testament thread — or should the OT verse read the plainer `ความเชื่อ` to visually unify the four occurrences? This is precisely the kind of forward-compounding editorial choice (cf. the MAT 18 ἐκκλησία precedent that motivated this checklist) that should be ratified deliberately before `book-habakkuk-v1` locks the surface. **Severity: YELLOW (translation is defensible and well-footnoted; the cross-testament consistency call wants Ben's decision).**

---

## 5. NT-reception apparatus — 2:3 (LXX personal subject → Heb 10:37) — **STABLE**

Habakkuk 2:3, `כִּי בֹא יָבֹא לֹא יְאַחֵר` ("for it will surely come, it will not delay"), is rendered on the **MT** as an impersonal subject — the *vision* will come (`เพราะมันจะมาถึงอย่างแน่นอน และจะไม่ชักช้า`). The footnote (`habakkuk_02.json` v3, `nt_citation_note`) discloses that the **LXX** read an implied personal subject ("the coming one will come"), the form **Hebrews 10:37–38** cites — joined to 2:4 — to point to the coming of Christ. The text translates the MT and records the reception; it does **not** retrofit the LXX personalization into the Hebrew.

This is the same MT-primary-plus-reception-footnote discipline applied to Joel 2:31 → Acts 2 and Nahum 2:1 → Romans 10:15 — reception, not assertion. Paired with §4, the 2:3–4 pericope forms the Hebrews 10:37–38 citation cluster, handled uniformly: MT in the body, NT reception in the footnote. **STABLE** ✓ (the apparatus is principled and consistent; no corpus doc names the policy, but `mt_vs_lxx_textual_variant_handling_2026-05` + `ot_nt_cross_quotation_thread_2026-05` govern the pattern). **Severity: GREEN.**

---

## 6. Messianic restraint — 3:13 (מָשִׁיחַ "anointed" + head-crushing → Gen 3:15) — **STABLE**

Habakkuk 3:13, `יָצָאתָ לְיֵשַׁע עַמֶּךָ לְיֵשַׁע אֶת־מְשִׁיחֶךָ … מָחַצְתָּ רֹּאשׁ מִבֵּית רָשָׁע` → **`พระองค์เสด็จออกไปเพื่อช่วยประชากรของพระองค์ … เพื่อช่วยผู้ที่พระองค์ทรงเจิมไว้ … ทรงบดขยี้ศีรษะแห่งเรือนของคนชั่ว`**. The term מָשִׁיחֶךָ "your anointed" — parallel to עַמֶּךָ "your people" — is rendered **`ผู้ที่พระองค์ทรงเจิมไว้`** ("the one you have anointed"), correctly reading it in its OT sense as the anointed Davidic king / covenant people, **not** a bare "คือพระคริสต์" assertion. The head-crushing (`מָחַצְתָּ רֹּאשׁ`) echo of Genesis 3:15 and the Christian messianic reading are recorded **in the footnote** (`habakkuk_03.json` v5, `nt_citation_note` — "in the Christian reading … reflects the hope of the Messiah"), using reception language ("reflects / echoes / hope"), without flattening the Hebrew.

This is the **committal-messianic-surface policy** held cleanly (Isaiah §0; the policy whose regression Ezekiel §14 flagged — 5+ summaries asserting "คือพระคริสต์" as bare fact). Habakkuk 3:13 is the strongest committal test since Micah 5:1 (Bethlehem → Matt 2:6), and like Micah it stays on the right side of the line: reception in the footnote, restraint in the body. **STABLE** ✓. **Severity: GREEN.**

---

## 7. Divine anthropomorphism — the chapter-3 theophany — **LOCKED**

Habakkuk 3 is a dense theophany, and it is the book's stress-test of `divine_anthropomorphism_thai_grammar_2026-05`. The grammar splits cleanly:
- **God's body-parts, third-person reference → honorific/royal:** "rays from his hand" (3:4) → **`พระหัตถ์`**; "at his feet" (3:5) → **`เบื้องพระบาท`**; "you marched with fury / threshed in wrath" (3:12) → **`พระอาการกริ้ว / พระพิโรธ`**; "before his presence" (2:20) → **`ต่อพระพักตร์พระองค์`**; the eyes too pure to see evil (1:13) → **`พระเนตร`**.
- **Non-divine body-parts → plain:** the personified Deep lifting **its own** hands (3:10, יָדֵיהוּ) → plain **`มือ`**; the prophet's **own** feet (3:19, רַגְלַי) → plain **`เท้า`**; the prophet's lips and belly trembling (3:16) → plain.
- **The ทרง-trap correctly avoided at 2:16:** "the cup of YHWH's **right hand**" → `พระหัตถ์ขวา` (royal, because the hand is God's), but the verb's subject is the **cup** (`ถ้วย…จะเวียนมา`), not the hand — so no body-part-before-ทรง violation is triggered.

Critically, Habakkuk has **no first-person body-part-plain** case of the Isaiah 51:9 / Ezekiel "5:11-lock" class — God's body-parts all appear in the prophet's **third-person** theophanic description and take the honorific; God's first-person speech (1:5–11; 2:2ff) carries no body-part. Habakkuk is therefore a **clean, non-friction data point** that **does not move** the open Isaiah/Jeremiah/Ezekiel/Hosea/Amos first-person-plain §13 DECIDE — exactly as Joel, Amos, Micah, and Nahum were. **LOCKED** ✓. **Severity: GREEN.**

---

## 8. Versification — no MT/English divergence zone — **LOCKED**

Habakkuk's three chapters follow a versification in which **MT = English throughout**; there is no offset zone (contrast Joel ch.3/4, Micah ch.4/5, and Nahum ch.2). `grep` confirms **zero** Habakkuk entries are owed in `data/versification_map.json`, and the per-chapter `versification_*` check reports are green for all three chapters. This is **cleanest-tier** alongside Amos and Obadiah — no zone to register, nothing retrofitted. **LOCKED** ✓ (`verse_schema_and_versification_2026-05`). **Severity: GREEN.**

---

## 9. MT textual-variant disclosure + hapax handling — **STABLE**

Habakkuk is lexically among the hardest minor prophets (3:9 is one of the most obscure clauses in the OT), and the apparatus handles it conservatively and transparently:
- **MT-primary variants, disclosed not gapped:** **2:5** MT `הַיַּיִן` "wine" vs 1QpHab `הוֹן` "wealth" → MT followed, footnoted (`textual_variant`); **2:16** Ketiv `הֵעָרֵל` "expose your foreskin" vs Qere `הֵרָעֵל` "stagger" → Ketiv followed, footnoted (`Ketiv/Qere`); **3:9** the crux `שְׁבֻעוֹת מַטּוֹת אֹמֶר` → rendered conservatively, difficulty flagged (`textual_crux`). These are §2.3 **non-gaps** — translation follows MT, the variant is disclosed — not inclusion variants (`audit_inclusion_variants` found **0** candidates, so no Tier-2 file is owed).
- **Hapax legomena handled with notes:** עָקַל (1:4), מְגַמָּה (1:9), מִשְׂחַק (1:10), עַבְטִיט (2:6), כָּפִיס (2:11), קִיקָלוֹן (2:16), רוֹם (3:10) each carry a `notes`/`key_decisions` gloss. Lexical care is consistent and reader-serving.
- **Liturgical apparatus:** `סֶלָה` → transliterated **`เซลาห์`** (3:3, 9, 13, corpus convention); the Shigionoth superscription (3:1) and the choirmaster colophon (3:19) carry Psalter-style `liturgical_note` footnotes, correctly treating ch.3 as a psalm.

**STABLE** ✓ (uniform and principled; `mt_vs_lxx_textual_variant_handling_2026-05` + `hebrew_idioms_and_metaphor_2026-05` govern the pattern; no Habakkuk-specific doc owed). **Severity: GREEN.**

---

## 10. Infrastructure — `export_to_usfm.py` rejects `HAB` — **REVIEW (infra, non-blocking)**

`scripts/export_to_usfm.py` does not yet accept the `HAB` book code (`✗ Unknown book code: HAB` — the standing minor-prophet apparatus gap, the same item flagged at Joel/Amos/Obadiah/Micah/Nahum). As part of this audit, `HAB` **has been registered** in `scripts/build_external_review_packet.py` (the BOOKS slug dict — it was already in `OT_CODES`) and in `scripts/audit_items_to_yaml.py` (`BOOK_SLUGS`). This is a non-translation, non-blocking infrastructure item; it does not affect the v1 tag. **Severity: GREEN (infra; does not gate the tag).**

---

## Items reviewed that need no action

- **The five woe-oracles (`הוֹי`, 2:6, 9, 12, 15, 19) → `วิบัติ`** — uniform rendering across all five; the prophetic doom-announcement marker is consistent and `check_phrase_consistency`-clean.
- **3:2 "in wrath remember mercy" (`בְּרֹגֶז רַחֵם תִּזְכּוֹר`)** → `ในยามที่ทรงพระพิโรธ ขอทรงระลึกถึงพระเมตตา` — a mercy *petition*, **not** the Exodus-34 attribute-formula recitation (no gracious/compassionate/slow-to-anger string), so `exod_34_attribute_formula_2026-05` is **not** implicated; no lock conflict (contrast Nahum 1:3, which *does* recite the formula).
- **Eloah / the Holy One (3:3, `אֱלוֹהַ` / `קָדוֹשׁ`)** → `พระเจ้า` / `องค์บริสุทธิ์` — the poetic divine names of the theophany; rendered per `divine_names_table_2026-05` (El-family → พระเจ้า), no separate lock needed.
- **Chaldeans / proper nouns** — `כַּשְׂדִּים` → `ชาวเคลเดีย` (1:6), Teman/Paran/Cushan/Midian (3:3, 3:7) transliterated per `proper_names_and_transliteration_2026-05`. Clean.
- **Divine-names false-positive class** — `check_divine_names` produces **zero** Habakkuk warnings (no standalone-Adonai `C-soft` flags, no human-subject false positives such as Amos 4:1's). Cleanest possible state.

## Recommended new / amended translator-decisions docs

These are **recommendations only** — per the checklist, this audit recommends but does not author corpus docs. None is *owed* unless the §4 DECIDE resolves into a lock:

1. **If §4 resolves** — record the אֱמוּנָה / "righteous shall live by faith" decision (the MT `ความเชื่ออันมั่นคง` vs the NT-citation `โดยความเชื่อ` cross-testament policy) either as a new `habakkuk_2_4_faith_2026-06.md` or as an entry in `ot_nt_cross_quotation_thread_2026-05`. This is the only doc that would become *owed*, and only on a path-b decision.
2. **`divine_names_table_2026-05` — optional note on the reversed-order compound** (§3): the table's compound row cites the אֲדֹנָי יְהוִה word order; a one-line note that the reversed יְהוִה אֲדֹנָי (Psalter-colophon form, Hab 3:19) collapses identically would close a small documentation gap. Defer until Amos §1 resolves, since that decision governs the row.

## Checklist for Ben before tagging `book-habakkuk-v1`

- [ ] **§4 DECIDE** — ratify the אֱמוּנָה rendering at 2:4. Confirm whether the landmark OT verse should read `ความเชื่ออันมั่นคง` "steadfast faith" (MT-faithful, footnoted) while its three NT citations read the plain `โดยความเชื่อ`, or whether the OT verse should be unified to the plainer `ความเชื่อ`. **This blocks the v1 tag.**
- [ ] **§3 REVIEW** — confirm the bare collapse of יְהוִה אֲדֹנָי at 3:19 (contingent on the open Amos §1; re-opens only under path-b). No change proposed.
- [ ] **§10 REVIEW** — acknowledge the `export_to_usfm.py` `HAB` gap (infra; non-blocking).
- [ ] Tag `book-habakkuk-v1` after the §4 decision and the two REVIEW confirmations.

*Status counts: 4 LOCKED · 3 STABLE · 2 REVIEW · 1 DECIDE.*
