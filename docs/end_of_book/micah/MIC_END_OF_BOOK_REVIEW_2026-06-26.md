# Micah — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 7 chapters of Micah (MT versification — Micah carries the **MT/English divergence zone** MT 4:14 = English 5:1 and MT 5:1–14 = English 5:2–15); `glossary.json`; `docs/translator_decisions/` corpus. Micah is the **fifth Book-of-the-Twelve title** processed (after Hosea, Joel, Amos, Obadiah) and the first of the Twelve to carry a versification divergence zone. Three cross-cutting facts dominate the review: (1) Micah opens with the **אֲדֹנָי יְהוִה "Lord GOD"** compound (1:2) — the form whose *surfacing* in Amos is the open headline DECIDE — and Micah renders it **bare** `องค์พระผู้เป็นเจ้า` (plus the standalone אֲדֹנָי later in the same verse → `องค์เจ้านาย`), a clean path-(a) witness; (2) Micah 4:1–3 is a near-verbatim **doublet of Isaiah 2:2–4** that the Eremos text **harmonizes** to match Isaiah — the *opposite* surface treatment to Obadiah 1–9 ∥ Jeremiah 49 (translated independently), and the exact doublet the Obadiah audit forecast as "imminent in the Twelve"; and (3) Micah 5:1 is the corpus's highest-profile **messianic** verse (the Bethlehem oracle, Matt 2:6), handled with NT-**reception** framing rather than a bare "คือพระคริสต์" surface assertion.
**Trigger:** MIC 7 shipped (last chapter, commit `e5b9b895`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **10 cross-cutting items reviewed.** Mechanical gates (§1 of checklist) pass: all 7 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks, 30,428 verses scanned); per-chapter `check_divine_names` clean for Micah (**zero warnings** — no false positive of the Amos 4:1 / Daniel 12:8 class); all 7 `output/textual_variants/micah_NN.json` present; the versification-map entries `MIC-4-14` + `MIC-5-1…5-14` are committed (`eb9f2487`, `f5e40166`). `git status output/` for Micah files is clean (the four `*amos*` / `divine_names.md` entries in `git status` are pre-existing Amos-audit artifacts, untouched here).

- **1 item flagged DECIDE** (Ben choice needed before tagging `book-micah-v1`):
  - **§2 — Micah 4:1–3 ∥ Isaiah 2:2–4 is HARMONIZED** (rendered word-for-word to match the Isaiah surface), where Obadiah 1–9 ∥ Jeremiah 49:7–22 was translated **independently**. The corpus now visibly does **both**, and the Obadiah audit's own §2 table listed "Isa 2∥Mic 4" as an *independent*-translation example — which Micah's actual practice contradicts. There is no longer a single uniform doublet practice to "confirm"; Ben must **ratify the governing distinction** (harmonize verbatim-identical shared vision-text vs preserve independently-reworked oracles with genuine MT differences vs preserve deliberate inversions like Mic 4:3 ∥ Joel 4:10), which then unblocks the `parallel_passage_doublets_2026-06.md` doc recommended at Obadiah. See §2.

- **4 items flagged REVIEW** (worth Ben's confirmation):
  - **§1 — אֲדֹנָי יְהוִה "Lord GOD" at 1:2 rendered bare `องค์พระผู้เป็นเจ้า`** (and the standalone אֲדֹנָי in the same verse → `องค์เจ้านาย`). Micah is the **second minor-prophet datum after the bare-normalization commits** (after Obadiah) and it *complies* with the locked `divine_names_table_2026-05` rule and Amos's recommended path (a). Micah is uniquely **self-consistent** — it carries both the compound (bare) and a free-standing Adonai (→ `องค์เจ้านาย`) in one verse — and its KD cites the **real** locked doc, not the phantom `adonai_yhwh_2026-05` that Amos's KDs cite. Contingent on the open **Amos §1 DECIDE**. See §1.
  - **§5 — Micah 7:18–20 closing doxology echoes the Exodus 34:6–7 attribute formula** (`נֹשֵׂא עָוֺן` "bears iniquity," `לֹא־הֶחֱזִיק לָעַד אַפּוֹ` "does not keep his anger forever," `חָפֵץ חֶסֶד` "delights in steadfast love") but is rendered as an **independent doxology**, not conformed to the locked `exod_34_attribute_formula_2026-05` surface. Confirm this is held **off** the Exod-34 lock deliberately (cf. Lamentations §, where chesed 3:22 was held off the formula). See §5.
  - **§6 — the per-chapter Layer-2 Tetragrammaton footnote is MISSING in chapter 5.** Six of seven chapters carry the `tetragrammaton_convention_first_occurrence` footnote; chapter 5 (whose first YHWH is at MT 5:3 `בְּעֹז יְהוָה`) carries only `versification_divergence` + `messianic_reception_note` footnotes and **no** Tetragrammaton footnote. `check_divine_names` passes anyway — **mechanically invisible**, the same gap-class as the Lamentations ch2/ch3 and Joel ch3 Layer-2 issues. See §6.
  - **§10 — `export_to_usfm.py` still rejects `MIC`**, the recurring OT book-code gotcha (same open state as ISA/EZK/LAM/JOL/AMO/OBA). Not a translation issue and not a tag blocker; MIC **is** already registered in `build_external_review_packet.py` (line 113), and this audit registers it in `audit_items_to_yaml.py`. See §10.

- **STABLE / LOCKED items (no action needed; documented at verse level or corpus-locked):**
  - **§3 — messianic surface restraint (5:1 Bethlehem, 2:13 הַפֹּרֵץ the Breaker, 7:6 → Matt 10:35–36) — STABLE.** The highest-profile messianic test case in the corpus (5:1 → Matt 2:6) is handled with **reception framing** — `thai_summary` says "มัทธิวนำข้อนี้มาใช้กับ…พระเยซูพระเมสสิยาห์" ("Matthew applies this to…Jesus the Messiah") and a `messianic_reception_note` footnote, **not** a bare "คือพระคริสต์" assertion in the rendered text. This is clean of the **§0 messianic-regression** flagged at Ezekiel §14 and consistent with the committal-messianic-surface policy ratified at Isaiah — Micah is the **strongest data point yet** for that policy holding under maximal pressure.
  - **§4 — `חֶסֶד` chesed → `ความรักมั่นคง` (6:8, 7:18, 7:20) — LOCKED** (`chesed_covenant_love_2026-05`), three uniform occurrences incl. the famous 6:8 triad.
  - **§7 — divine anthropomorphism — LOCKED** (`divine_anthropomorphism_thai_grammar_2026-05`): Spirit → `พระวิญญาณ` (2:7, 3:8), divine mouth → `พระโอษฐ์` (4:4), treading iniquities underfoot → `พระบาท` (7:19); "hide his face" idiom plain `ซ่อนหน้า` (3:4); first-person divine speech plain (2:9, 6:3). Micah adds **no** graphic first-person body-part-plain of the Isaiah/Jeremiah/Ezekiel class and **does not move** the open cross-corpus §13 DECIDE.
  - **§8 — the Micah 1:10–15 town-name paronomasia — STABLE** (`proper_noun_wordplay_2026-05` / `wordplay_and_paronomasia_2026-05`): the densest pun-cluster in the OT, rendered place-name + action with the puns footnoted (`wordplay_note`). Minor reader-note coverage observation noted, non-blocking.
  - **§9 — versification MT zone (4:14 = Eng 5:1; 5:1–14 = Eng 5:2–15) REGISTERED — LOCKED.** Per-verse `versification` objects present, map entries committed, `versification_divergence` footnotes at 4:14 + 5:1, `check_versification_anchor` clean. Micah is **cleanest-tier** here — the zone is fully registered (unlike several prior books shipped with unregistered zones).

- **External AI review (§3) packet:** focused 3-item packet — the doublet-harmonization policy fork (§2 DECIDE, the load-bearing item), the אֲדֹנָי יְהוִה bare/marked corpus tension (§1, in deliberate contrast with the open Amos blocker), and the Exod-34 doxology-echo question (§5). The infra item (§10) and the apparatus gap (§6) are not externally reviewable translation questions and are excluded from the packet, matching the Amos/Obadiah packet scoping. The messianic item (§3) is compliant/LOCKED-adjacent and excluded.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. אֲדֹנָי יְהוִה "Lord GOD" at 1:2 — rendered BARE (+ standalone Adonai → `องค์เจ้านาย`), conforming to the locked rule — **REVIEW**

Micah's cosmic-courtroom summons (1:2) is the corpus's *next* occurrence of the divine compound after Obadiah, and it is unusually informative because it carries **both** divine forms in a single verse.

**The verse:**

- **HEB (1:2):** `שִׁמְעוּ עַמִּים כֻּלָּם … וִיהִי אֲדֹנָי יְהוִה בָּכֶם לְעֵד אֲדֹנָי מֵהֵיכַל קָדְשׁוֹ`
- **BSB:** "Hear, O peoples, all of you… May the **Lord GOD** bear witness against you, the **Lord** from His holy temple."
- **TH (Micah):** `ชนชาติทั้งหลายเอ๋ย จงฟังเถิด … ขอ**องค์พระผู้เป็นเจ้า**ทรงเป็นพยานปรักปรำพวกท่าน คือ**องค์เจ้านาย**จากพระวิหารบริสุทธิ์ของพระองค์`

The compound `אֲדֹנָי יְהוִה` is rendered **bare** `องค์พระผู้เป็นเจ้า` (Adonai collapsed), and the free-standing `אֲדֹנָי` later in the same verse is rendered **`องค์เจ้านาย`** — the locked surface for bare standalone Adonai. This is exactly **`divine_names_table_2026-05` row 22** ("compound collapses to single Thai rendering") plus the standalone-Adonai row, and it is what Ezekiel (217×), Isaiah (~30×), Jeremiah, and now Obadiah do. The `micah_01` KD records the compound and cites the **real** `divine_names_table_2026-05` — **not** the non-existent `adonai_yhwh_2026-05` that Amos's KDs cite.

**Why REVIEW, not LOCKED:** the rendering is correct under the current lock, but its standing is **contingent on the open Amos §1 DECIDE.** Amos surfaces the same compound as `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` in 20 verses; the Amos audit recommends **path (a)** — normalize Amos *down* to the bare form Micah and Obadiah already use. If Ben ratifies path (a), Micah needs **no change** and this item becomes LOCKED. Only an Amos **path (b)** (ratify the marked surface, write `adonai_yhwh_2026-06.md`, re-open the bare books) would force Micah's single occurrence to be re-marked. Micah is therefore a **second clean, self-consistent data point strengthening the case for path (a)**: it is, in fact, *more* informative than Obadiah, because it shows the translator correctly distinguishing the compound (→ bare `องค์พระผู้เป็นเจ้า`) from a standalone Adonai (→ `องค์เจ้านาย`) **in the same breath** — exactly the distinction the bare-collapse rule preserves in apparatus. **Confirm** the bare rendering stands; no translation change proposed. **Severity: GREEN (compliant; flagged only for the cross-book dependency).**

---

## 2. Micah 4:1–3 ∥ Isaiah 2:2–4 — the shared vision is HARMONIZED, where Obadiah ∥ Jeremiah-49 was kept independent — **DECIDE**

This is the load-bearing editorial item of the book, and the exact doublet the Obadiah audit named as "imminent in the Twelve."

**The situation.** Micah 4:1–3 ("In the last days the mountain of the house of the LORD…they will beat their swords into plowshares…") is a near-verbatim doublet of Isaiah 2:2–4. The Eremos text **harmonizes** it: the `micah_04` 4:1 note states outright *"มีคาห์ 4:1–3 ขนานเกือบทุกคำกับ อิสยาห์ 2:2–4 ฉบับเอเรโมสแปลให้สอดคล้องกัน"* ("Micah 4:1–3 parallels Isaiah 2:2–4 almost word-for-word; the Eremos edition translates them to match"), and 4:3's `וְכִתְּתוּ חַרְבֹתֵיהֶם לְאִתִּים` is rendered **verbatim** to the Isaiah 2:4 surface (`ตีดาบ…เป็นผาลไถนา`). A `parallel_passage_note` footnote discloses the relationship.

**The tension.** This is the **opposite** surface treatment to the immediately preceding book:

| Doublet | Treatment | Surface result |
|---|---|---|
| **Obadiah 1–9 ∥ Jeremiah 49:7–22** (OBA audit §2) | **Independent** per MT context | Incidental synonym-drift on identical-Hebrew phrases (`เย่อหยิ่ง`/`หยิ่งยโส`); genuine MT diff `שָׁמַעְנוּ`/`שָׁמַעְתִּי` preserved |
| **Micah 4:1–3 ∥ Isaiah 2:2–4** (this book) | **Harmonized** to match | Reader sees the two pilgrimage-of-the-nations visions in identical Thai |

And the Obadiah audit's **own §2 table** explicitly listed "Isa 2∥Mic 4" under its *independent*-translation examples — a stated expectation that Micah's actual practice **contradicts.** A third data point sharpens it further: Micah 4:3 (swords → plowshares) is the deliberate **inversion** of Joel 4:10 (plowshares → swords); the translator **preserved** that inversion (4:3 note flags it), correctly *not* harmonizing an intentional reversal.

**Why DECIDE, not REVIEW (unlike Obadiah's version).** At Obadiah the practice was *uniform* — every doublet had been independent — so "confirm the policy" was available. After Micah it is **not uniform**: the corpus now harmonizes one doublet and preserves another, and the just-written Obadiah audit documents an expectation Micah breaks. The recommended `parallel_passage_doublets_2026-06.md` doc **cannot be written** until Ben ratifies the governing distinction, because the doc would otherwise have to assert both "independent" and "harmonized" with no stated principle. The translator's *implicit* principle is coherent and defensible —

- **harmonize** verbatim-identical shared liturgical/vision text (Mic 4:1–3 ∥ Isa 2:2–4; cf. Ps 14 ∥ 53, 2 Kgs 18–20 ∥ Isa 36–39);
- **preserve independence** for reworked oracles carrying genuine MT differences (Oba 1–9 ∥ Jer 49:7–22, with its real `שָׁמַעְנוּ`/`שָׁמַעְתִּי`);
- **preserve** deliberate inversions (Mic 4:3 ∥ Joel 4:10)

— but it is **undocumented**, and the surface contradiction is reader-visible. Ben must choose: ratify this three-way distinction as the corpus policy (recommended; it matches actual practice and is the cleanest reading), or pick a single rule and request the conforming rev. **No translation change is proposed pending that choice.** **Severity: YELLOW (policy fork; current state defensible but no longer uniform).**

---

## 3. Messianic surface restraint — 5:1 Bethlehem, 2:13 הַפֹּרֵץ, 7:6 → Matt 10:35–36 — **STABLE (no §0 regression; strongest test case yet)**

Micah carries the corpus's single most-cited messianic verse, and the surface holds the committal-policy line under maximal pressure.

- **5:1 (MT) = 5:2 (Eng), the Bethlehem oracle** `מִמְּךָ לִי יֵצֵא לִהְיוֹת מוֹשֵׁל בְּיִשְׂרָאֵל וּמוֹצָאֹתָיו מִקֶּדֶם מִימֵי עוֹלָם`: the rendered Thai stays at the **plain text** — "ผู้หนึ่ง…ผู้ปกครอง…ต้นกำเนิดของท่านมีมาแต่โบราณกาล" — and the messianic identification is carried as **NT reception**, not surface assertion: the `thai_summary` reads "มัทธิวนำข้อนี้มาใช้กับการประสูติของพระเยซูพระเมสสิยาห์ที่เบธเลเฮม (มธ. 2:6)" ("Matthew **applies** this to the birth of Jesus the Messiah"), and `output/textual_variants/micah_05.json` carries a dedicated `messianic_reception_note`. **No bare "คือพระคริสต์."**
- **2:13 `הַפֹּרֵץ` "the Breaker"** → `ผู้เปิดทาง`, with the note "ประเพณีการตีความของชาวยิวเชื่อมโยงกับพระเมสสิยาห์" ("Jewish interpretive tradition connects this to the Messiah") — attributed to a tradition, descriptive, not asserted.
- **7:6** (family breakdown) → the `thai_summary` flags "พระเยซูทรงยกข้อนี้มาตรัส…(มธ. 10:35-36)" ("Jesus quotes this verse"), reception framing again; an `nt_citation_note` carries it.

This is clean of the **§0 messianic-regression** flagged at Ezekiel §14 (where 5+ summaries asserted "คือพระคริสต์" as bare fact) and consistent with the **committal-messianic-surface policy ratified at Isaiah** and applied at Joel/Amos/Obadiah. Because 5:1 is the corpus's highest-profile messianic verse, Micah is the **strongest evidence yet** that the reception-not-assertion policy holds where the temptation to over-commit is greatest. **STABLE** ✓ (LOCKED-adjacent; covered by the Isaiah committal-surface policy). **Severity: GREEN.**

---

## 4. `חֶסֶד` chesed → `ความรักมั่นคง` (6:8, 7:18, 7:20) — **LOCKED**

Three occurrences, all rendered with the corpus-locked `ความรักมั่นคง` (`chesed_covenant_love_2026-05`):

- **6:8 `וְאַהֲבַת חֶסֶד`** → `รักความรักมั่นคง`, inside the book's (and arguably the OT's) most famous summary of true religion — "do justice (`עֲשׂוֹת מִשְׁפָּט` → กระทำความยุติธรรม), love chesed, walk humbly (`הַצְנֵעַ לֶכֶת`, hapax → ดำเนินอย่างถ่อมตน) with your God." The 6:8 note explicitly cites the standard chesed rendering and the Hos 6:6 parallel.
- **7:18 `כִּי־חָפֵץ חֶסֶד הוּא`** → `ทรงพอพระทัยในความรักมั่นคง` (see also §5).
- **7:20 `חֶסֶד לְאַבְרָהָם`** → `ความรักมั่นคงแก่อับราฮัม`, paired with `אֱמֶת` "faithfulness" → `ความสัตย์จริง`.

Uniform with the lemma-thread across Ruth → Jonah → Psalms → Lamentations. **LOCKED** ✓. **Severity: GREEN.**

---

## 5. Micah 7:18–20 closing doxology — the Exodus-34 attribute echo, held OFF the formula lock — **REVIEW**

The crowning doxology (`מִי־אֵל כָּמוֹךָ` "Who is a God like you?", a pun on Micah's own name) clusters three attributes that **echo the Exodus 34:6–7 self-revelation formula** without quoting it:

- **7:18 `נֹשֵׂא עָוֺן וְעֹבֵר עַל־פֶּשַׁע`** "bearing iniquity and passing over transgression" → `ทรงยกโทษความชั่วช้า และทรงข้ามพ้นการล่วงละเมิด` (cf. Exod 34:7 `נֹשֵׂא עָוֺן וָפֶשַׁע`)
- **7:18 `לֹא־הֶחֱזִיק לָעַד אַפּוֹ`** "does not keep his anger forever" → `ไม่ทรงถือพระพิโรธไว้เป็นนิตย์` (cf. Exod 34:6 `אֶרֶךְ אַפַּיִם` "slow to anger")
- **7:18 `כִּי־חָפֵץ חֶסֶד הוּא`** "for he delights in steadfast love" → `เพราะพระองค์ทรงพอพระทัยในความรักมั่นคง` (the chesed lock, §4)

The locked `exod_34_attribute_formula_2026-05` mandates an *identical* Thai surface across the ~10 verbatim/near-verbatim recitations of the Sinai formula, so a reader recognizes the formula at each recurrence. Micah 7:18–20 is **not** one of those recitations — it is an *allusive* doxology that re-uses the attribute vocabulary in fresh syntax — and the Eremos text accordingly renders it **per local sense**, *not* conformed to the formula surface, with a `doxology_and_wordplay_note` footnote. This is the **same judgment** the Lamentations audit made when it held chesed 3:22 **off** the Exod-34 lock.

**Why REVIEW:** the decision (treat 7:18–20 as an independent doxology, not a formula recitation) is principled and consistent with the Lamentations precedent, but it is a **judgment call at the boundary** of the Exod-34 lock's scope, and the attribute overlap is strong enough that an external reader could expect formula-consistent wording. **Confirm** 7:18–20 is intentionally rendered as an allusive doxology outside the `exod_34_attribute_formula` identical-surface lock (no change proposed), or, if Ben prefers, request a targeted alignment of the overlapping phrases. **Severity: YELLOW (scope-of-lock confirmation; current state defensible).**

---

## 6. Divine names: Tetragrammaton Layer-1 uniform; Layer-2 footnote MISSING in chapter 5 — **REVIEW (mechanically invisible)**

- **Layer 1 — `יְהוָה` → `องค์พระผู้เป็นเจ้า` in every occurrence**, all 7 chapters (1:1, 1:3, 1:12, 2:3, 2:5, 2:7, 2:13, 3:4, 3:5, 3:8, 3:11, 4:1–13, 5:3–9, 6:1–9, 7:7–10, 7:17), each KD citing `divine_names_table_2026-05`. The `כֹּה אָמַר יְהוָה` / `נְאֻם־יְהוָה` / `פִי יְהוָה צְבָאוֹת` formulas are uniform; the Sabaoth form `יְהוָה צְבָאוֹת` → `องค์พระผู้เป็นเจ้าจอมโยธา` (4:4, bare — Micah carries no `אֱלֹהֵי`, so it does **not** hit the Amos §10 `พระเจ้า`-stack question). **The Micah divine-names check is clean, zero warnings.**
- **Layer 2 — the per-chapter first-occurrence footnote is present in 6 of 7 chapters, MISSING in chapter 5.** Chapters 1, 2, 3, 4, 6, 7 each carry a `tetragrammaton_convention_first_occurrence` footnote. **Chapter 5 does not** — its `output/textual_variants/micah_05.json` carries only a `versification_divergence` footnote (5:1) and the `messianic_reception_note` (5:1), even though chapter 5 contains YHWH at MT 5:3 (`בְּעֹז יְהוָה`, `שֵׁם יְהוָה`), 5:6 (`מֵאֵת יְהוָה`), and 5:9 (`נְאֻם־יְהוָה`). The first-occurrence footnote that every other chapter places at its opening YHWH is **absent** at 5:3.

`check_divine_names` passes regardless — the check does not enforce per-chapter Layer-2 footnote presence — so this is **mechanically invisible**, the same gap-class as the Lamentations ch2/ch3 Layer-2 gap and the Joel ch3 footnote-type mismatch. **Recommend adding the chapter-5 `tetragrammaton_convention_first_occurrence` footnote** (at 5:3, enumerating the chapter's YHWH verses) before the v1 tag, for parity with the other six chapters. Apparatus-only; not a rendered-text issue. **Severity: YELLOW (apparatus completeness; mechanically invisible).**

---

## 7. Divine anthropomorphism — **LOCKED**

Micah's God-language is handled per `divine_anthropomorphism_thai_grammar_2026-05`:

- **Third-person divine attributes → honorific (Rachasap):** Spirit of the LORD `רוּחַ יְהוָה` → `พระวิญญาณ` (2:7 "is the Spirit of the LORD impatient?", 3:8 "filled with the Spirit of the LORD"); mouth of the LORD `פִי יְהוָה` → `พระโอษฐ์` (4:4); treading iniquities underfoot `יִכְבֹּשׁ עֲוֺנֹתֵינוּ` → `ทรงเหยียบ…ไว้ใต้พระบาท` (7:19); coming forth / treading the heights (1:3) → `เสด็จ`/`ทรงเหยียบย่าง`.
- **The "hide the face" idiom → plain** `יַסְתֵּר פָּנָיו` → `ทรงซ่อนหน้า` (3:4), the set withdrawn-favour idiom, plain `หน้า` per the idiom convention.
- **First-person divine speech → plain:** `הֲדָרִי` "my splendour" → `ศักดิ์ศรีของเรา` (2:9), `מֶה־עָשִׂיתִי לְךָ` "what have I done to you?" → `เราได้ทำอะไรแก่เจ้า` (6:3).

Micah contains **no graphic first-person body-part-plain** case of the Isaiah 51:9 / Ezekiel-"5:11-lock" class that drives the open cross-corpus §13 DECIDE — its divine body-parts appear in third-person reference (honorific) or set idiom (plain). Micah is therefore a **clean, non-friction data point** that **does not move** the open Isaiah/Jeremiah/Ezekiel/Hosea/Amos first-person-plain DECIDE. **LOCKED** ✓. **Severity: GREEN.**

---

## 8. The Micah 1:10–15 town-name paronomasia — **STABLE**

The dirge over ~12 Judean towns (1:10–15) hangs on **untranslatable Hebrew puns** (Gath/`taggîdû` "tell"; Beth-leaphrah/`ʿāpār` "dust"; Maroth/`mār` "bitter"; Lachish/`rekesh` "steeds"; Achzib/`ʾakzāb` "deceptive"; Mareshah/`yōrēš` "conqueror"). The Eremos approach — **translate place-name + action, footnote the pun** — is per `proper_noun_wordplay_2026-05` / `wordplay_and_paronomasia_2026-05`: 1:10 carries a reader-facing strategy note + a `wordplay_note` in `textual_variants`; 1:12 (Maroth/bitter) and 1:13 (Lachish/steeds) carry per-verse rationale/notes. This is the **densest paronomasia cluster in the OT** and is handled consistently with the corpus wordplay policy.

**Minor observation (non-blocking):** reader-facing footnote coverage across the town-list is **uneven** — the puns at 1:11 (Shaphir/Zaanan), 1:14 (Achzib/deceptive), and 1:15 (Mareshah/conqueror, Adullam) are explained only in the translator-facing `key_decisions`, not in the reader `notes`. The 1:10 strategy-note tells the reader the whole list is built on puns, which mitigates this, so it is a polish item, not a defect. **STABLE** ✓. **Severity: GREEN.**

---

## 9. Versification — MT zone (4:14 = Eng 5:1; 5:1–14 = Eng 5:2–15) REGISTERED — **LOCKED**

Micah is the first Book-of-the-Twelve title to carry an MT/English divergence zone, and it is **fully registered** — the cleanest-tier handling:

- Per-verse `versification` objects are present on every divergent verse (`micah_04` 4:14; `micah_05` 5:1–5:14), each with `mt_ref` / `english_ref` / `bsb_ref` / `lxx_ref` / `diverges: true`.
- The map entries `MIC-4-14` and `MIC-5-1 … MIC-5-14` are committed to `data/versification_map.json` (`eb9f2487` for 4:14, `f5e40166` for chapter 5) — **manually staged**, per the `ship_chapter.sh`-doesn't-stage-the-map gotcha.
- `versification_divergence` footnotes are present at 4:14 and 5:1, each explaining "MT 4:14 = English 5:1" / "MT 5:N = English 5:N+1" to the reader and pointing to `data/versification_map.json`.
- `check_versification_anchor` clean for all 7 chapters.

This is a notable improvement over several prior books (Daniel, Job, Ezekiel ch21) that shipped with **unregistered** MT/English zones flagged at their audits. **LOCKED** ✓. **Severity: GREEN.**

---

## 10. Infrastructure — `export_to_usfm.py` rejects `MIC` — **REVIEW (infra, non-blocking)**

`python3 scripts/export_to_usfm.py … MIC` → unknown book code (the export script's internal code table lags the YAML/packet tables). The recurring OT book-code gotcha — same open state as ISA/EZK/LAM/JOL/AMO/OBA. It blocks Paratext (.SFM) export of Micah but is **not** a translation issue and **not** a v1-tag blocker. **MIC is already registered** in `build_external_review_packet.py` (BOOKS list, line 113), and this audit **registers MIC in `audit_items_to_yaml.py`** (BOOK_SLUGS + the verse-ref regex). `export_to_usfm.py` should be registered in the same pass when the maintainer next touches it. **Severity: YELLOW (infra, non-blocking).**

---

## Items reviewed that need no action

- **"In that day" / day-of-visitation thread (2:4, 4:6, 5:9, 7:4, 7:11–12).** Micah is **not** a Day-of-the-LORD book in the Joel/Amos/Obadiah sense — its `בַּיּוֹם הַהוּא` "in that day" is the eschatological-**restoration** register (re-gathering the lame, the reign in Zion), and 7:4 `יוֹם…פְּקֻדָּתְךָ` "day of your visitation" → `วันแห่งการลงโทษ` is the `paqad_visit_attend_2026-05` judgment sense. Micah therefore does **not** add a fourth witness to the dread-Day leitwort and does **not** further the `day_of_the_lord_leitwort_2026-06.md` recommendation (already triply owed by Joel/Amos/Obadiah). ✓.
- **MT/LXX — no inclusion-variant or macro-divergence candidate.** Micah carries no MT/LXX text-base fork of the Amos 9:11–12 (booth-of-David/Acts 15) or Jeremiah-scale kind; no `textual_variants` LXX/Septuagint note is present, and none is owed (§2.3 floor — non-gap). ✓.
- **Sabaoth `יְהוָה צְבָאוֹת` (4:4)** → `องค์พระผู้เป็นเจ้าจอมโยธา` (bare; no `אֱלֹהֵי`, so no `พระเจ้า`-stack) — consistent with `divine_names_table_2026-05` row 23 and **not** entangled with the open Amos §10 stack question. ✓.
- **Hapax legomena footnoted:** `רָתַם` (1:13), `צָנַע` (6:8), `עָבַת` (7:3), `מְסוּכָה` (7:4) — each glossed in `notes`. ✓.
- **`check_divine_names` false-positive class — none.** Unlike Amos 4:1 (human husbands flagged) or Daniel 12:8, Micah produces **zero** divine-names warnings; the human-subject "lords/husbands" trap does not appear. ✓.

---

## Recommended new translator-decisions docs

1. **`parallel_passage_doublets_2026-06.md`** (§2) — now **urgently owed** and **blocked on the §2 DECIDE.** The doc must encode the three-way distinction Micah forces into the open: **harmonize** verbatim-identical shared vision/liturgical text (Mic 4:1–3 ∥ Isa 2:2–4; cf. Ps 14 ∥ 53, 2 Kgs 18–20 ∥ Isa 36–39); **preserve independence** for reworked oracles carrying genuine MT differences (Oba 1–9 ∥ Jer 49:7–22, with `שָׁמַעְנוּ`/`שָׁמַעְתִּי`); **preserve** deliberate inversions (Mic 4:3 ∥ Joel 4:10). Recommended at Obadiah; Micah makes it the gating doc for the rest of the Twelve. **Author only after Ben ratifies the distinction (§2).**

(Per the checklist, this audit recommends but does not author the doc; it is blocked on the open DECIDE. The `day_of_the_lord_leitwort_2026-06.md` doc remains owed by Joel/Amos/Obadiah but is **not** further owed by Micah — see "Items reviewed that need no action.")

## Checklist for Ben before tagging `book-micah-v1`

- [ ] **§2 DECIDE** — ratify the doublet-handling distinction (harmonize verbatim-identical vision-text / preserve independent reworkings / preserve deliberate inversions), confirming Micah 4:1–3 ∥ Isaiah 2:2–4 is correctly **harmonized** while Obadiah ∥ Jeremiah-49 is correctly **independent**; this unblocks `parallel_passage_doublets_2026-06.md`. (Or pick a single rule and request the conforming rev.)
- [ ] **§1 REVIEW** — confirm the 1:2 `אֲדֹנָי יְהוִה` → bare `องค์พระผู้เป็นเจ้า` (+ standalone Adonai → `องค์เจ้านาย`) rendering stands (contingent on resolving the open **Amos §1 DECIDE** toward path (a); Micah is already correct under path (a)).
- [ ] **§5 REVIEW** — confirm Micah 7:18–20 is intentionally rendered as an allusive doxology **outside** the `exod_34_attribute_formula_2026-05` identical-surface lock (cf. the Lamentations chesed-3:22 precedent), or request targeted alignment.
- [ ] **§6 REVIEW** — add the missing chapter-5 `tetragrammaton_convention_first_occurrence` Layer-2 footnote (at 5:3) for parity with the other six chapters (mechanically invisible; apparatus-only).
- [ ] **§10 REVIEW** — register `MIC` in `export_to_usfm.py` (infra; non-blocking).
- [ ] Then: `bash scripts/ship_book.sh MIC` (lock-the-book ship + tag).
