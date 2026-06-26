# Nahum — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 3 chapters of Nahum (MT versification — Nahum carries a **whole-chapter MT/English divergence zone in chapter 2**: MT 2:1–14 = English 1:15–2:13, the English versification closing chapter 1 one verse later than the MT; chapters 1 and 3 align); `glossary.json`; `docs/translator_decisions/` corpus. Nahum is the **seventh Book-of-the-Twelve title** processed (after Hosea, Joel, Amos, Obadiah, Jonah, Micah). Three cross-cutting facts dominate the review and all point the same direction — *clean*: (1) Nahum's divine-name inventory is **only** the bare Tetragrammaton (יהוה) and the **YHWH-Sabaoth** compound (יְהוָה צְבָאוֹת) — it carries **no** אֲדֹנָי יְהוִה "Lord GOD" compound, so it sidesteps the open Amos §1 headline entirely, and its Sabaoth form matches the locked `องค์พระผู้เป็นเจ้าจอมโยธา`; (2) Nahum 1:3 deploys the **Exodus-34 attribute formula in deliberate inversion** — the judgment half only (`אֶרֶךְ אַפַּיִם` + `וְנַקֵּה לֹא יְנַקֶּה`), the mirror image of Jonah 4:2's mercy-recitation over the *same* city; (3) the prophet's name **Nahum = "comfort"** (`נַחַם`) frames a book-spanning wordplay that lands hard at 3:7 ("from where shall I seek **comforters** for you, [Nineveh]?").

**Trigger:** Final chapter of Nahum (NAM 3) shipped via `scripts/ship_chapter.sh`; `scripts/detect_book_complete.py` fired the end-of-book audit.

**Mandate:** §2 (Editorial review) + §3 (External AI packet) of `docs/END_OF_BOOK_CHECKLIST.md`. **Assessment only — no translation JSON was modified.**

## Summary

- **9 cross-cutting items reviewed.**
- **0 items flagged DECIDE.** Nahum adds **no** new Ben-blocker and **does not move** any open cross-book DECIDE (the §13 first-person-plain anthropomorphism question and the Amos §1 `אֲדֹנָי יְהוִה` headline remain open elsewhere — Nahum has **no instance forcing either**). Nahum is, with Obadiah, one of the **cleanest minor prophets** to date: it can be tagged `book-nahum-v1` once Ben confirms the four REVIEW items, none of which propose a translation change.
- **4 items flagged REVIEW** (worth Ben's confirmation; no change proposed):
  - **§3 — Exodus-34 attribute formula deployed in inversion at 1:3** (`ทรงกริ้วช้า` lemma compliant; the *Jonah↔Nahum* canonical pairing + a minor doc-sync are the actionable points).
  - **§4 — `הִנְנִי אֵלַיִךְ` "Behold, I am against you" → `เราเป็นปฏิปักษ์กับเจ้า`** (2:14, 3:5), aligning with the dominant Ezekiel/Jeremiah-oracle rendering; a one-file Jeremiah variant (`เราต่อสู้กับเจ้า`) means the formula is **not yet leitwort-documented**.
  - **§5 — the Nahum = "comfort" (`נַחַם`) wordplay/inclusio** (1:1 ↔ 1:12 ↔ 3:7), undocumented in `proper_noun_wordplay_2026-05` and a deliberate dark inverse of the Lamentations `אֵין מְנַחֵם` "no comforter" refrain.
  - **§9 — `export_to_usfm.py` rejects `NAM`** (infrastructure, non-blocking; the standing minor-prophet apparatus item).
- **4 items LOCKED** — §1 (Tetragrammaton Layer-1 + Layer-2 footnote), §2 (YHWH-Sabaoth), §6 (anthropomorphism), §7 (versification).
- **1 item STABLE** — §8 (NT-reception restraint at 2:1 ∥ Isa 52:7 → Rom 10:15).
- **Mechanical gate: fully GREEN.** `check_key_term_consistency` 0 violations; `check_phrase_consistency` 0 violations; `check_divine_names` **ZERO Nahum warnings** (no false-positive class); all 3 per-chapter `*_review.md` green; all 3 `back_translations/nahum_NN.json` present; all 3 `textual_variants/nahum_NN.json` present with the **correct** `tetragrammaton_convention_first_occurrence` footnote type in **every** chapter (no Joel-ch3 type-mismatch, no Micah-ch5 / Lamentations-ch2-3 missing-footnote gap); versification map `NAM-2-1…14` committed (f0c7955e).
- **External AI review (§3) packet:** focused **3-item** packet — the Exod-34 inversion + Jonah pairing (§3), the `הִנְנִי אֵלַיִךְ` formula rendering (§4), and the Nahum-name wordplay (§5). The infra item (§9) is not an externally-reviewable translation question and is excluded, matching the Amos/Obadiah/Micah packet scoping. All LOCKED/STABLE items are excluded.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Divine names — Tetragrammaton Layer-1 uniform + Layer-2 footnote present in every chapter — **LOCKED**

YHWH appears in all three chapters — **1:2** (×3), **1:3** (×2), **1:7, 1:9, 1:11, 1:12, 1:14; 2:3, 2:14; 3:5** — and is rendered **`องค์พระผู้เป็นเจ้า`** uniformly (Layer 1, `divine_names_table_2026-05`). The Layer-2 apparatus is **complete and correct**:

- `textual_variants/nahum_01.json` v2 — `tetragrammaton_convention_first_occurrence`, lists every YHWH verse in the chapter.
- `textual_variants/nahum_02.json` v3 — `tetragrammaton_convention_first_occurrence` (first YHWH of the chapter is at MT 2:3; flags the 2:14 `יְהוָה צְבָאוֹת`).
- `textual_variants/nahum_03.json` v5 — `tetragrammaton_convention_first_occurrence` (notes 3:5 `יְהוָה צְבָאוֹת`, and that the rest of the chapter is first-person divine speech / direct address).

`check_divine_names.py` reports **zero** Nahum entries in its 262-warning corpus list — Nahum has **no standalone `אֲדֹנָי`** (the `C-soft` class) and **no false-positive** human-subject verses. This is **cleanest-tier**: unlike Micah (Layer-2 footnote missing in ch.5), Lamentations (ch.2/ch.3 gap), or Joel (ch.3 wrong footnote type), Nahum's per-chapter first-occurrence footnote is present **and** correctly typed in all three chapters. **LOCKED** ✓ (`divine_names_table_2026-05`). **Severity: GREEN.**

---

## 2. YHWH-Sabaoth (`יְהוָה צְבָאוֹת`) → `องค์พระผู้เป็นเจ้าจอมโยธา` — **LOCKED**

The compound appears twice, both in the chapter-closing divine verdicts: **2:14** (MT; = English 2:13) and **3:5**, each `נְאֻם יְהוָה צְבָאוֹת` → **`องค์พระผู้เป็นเจ้าจอมโยธาตรัสว่า`**. This is **identical to the locked form** at `divine_names_table_2026-05` line 23 ("**องค์พระผู้เป็นเจ้าจอมโยธา** — Identical to already-shipped Jas 5:4; visual unity preserved across testaments") and matches the 31× Isaiah / 30× Jeremiah / 8× Psalms uses of the same Hebrew form.

This is **distinct** from the corpus's 562× `พระเจ้าจอมโยธา`, which renders the *different* Hebrew form `אֱלֹהֵי צְבָאוֹת` / `יהוה אלהי צבאות` ("**God** of hosts," used heavily in 1 Kings, Amos, Hosea, Jeremiah, Psalms). The two Thai forms correctly track two distinct Hebrew forms; Nahum uses only the `יְהוָה צְבָאוֹת` form and renders it correctly.

**Note for the record:** Nahum's *entire* divine-name inventory is the bare Tetragrammaton + YHWH-Sabaoth. It carries **no** `אֲדֹנָי יְהוִה` "Lord GOD" compound and **no** standalone `אֲדֹנָי`. It therefore **sidesteps the open Amos §1 headline DECIDE** (the `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` vs bare tension) entirely — there is no Adonai-YHWH datum here to vote either way. **LOCKED** ✓. **Severity: GREEN.**

---

## 3. Exodus-34 attribute formula deployed in **inversion** at 1:3 — lemma LOCKED; the canonical pairing + doc-sync — **REVIEW**

Nahum 1:3 opens `יְהוָה אֶרֶךְ אַפַּיִם וּגְדָל־כֹּחַ וְנַקֵּה לֹא יְנַקֶּה` → **`องค์พระผู้เป็นเจ้าทรงกริ้วช้าและทรงฤทธิ์อำนาจยิ่งใหญ่ และ…จะไม่ทรงปล่อยให้ผู้กระทำผิดลอยนวลพ้นโทษเลย`**. The locked Exod-34 lemma **`ทรงกริ้วช้า`** (`אֶרֶךְ אַפַּיִם` "slow to anger") is present and **matches** `exod_34_attribute_formula_2026-05` (which already lists Nahum 1:3 in its recitation table, line 48). `check_key_term_consistency` is clean.

What is theologically notable — and worth Ben's eye — is that Nahum recites **only the judgment half** of the formula. Where Exodus 34:6–7, Joel 2:13, Psalms 86/103/145, and Jonah 4:2 cite "gracious, compassionate, slow to anger, abounding in chesed," Nahum drops the mercy clauses and keeps `אֶרֶךְ אַפַּיִם` *plus* `וְנַקֵּה לֹא יְנַקֶּה` ("**will by no means clear the guilty**" — the Exod 34:7 reservation). This is a **deliberate inversion**: the formula Jonah quoted **for** Nineveh's mercy (Jonah 4:2) is the formula Nahum quotes **against** Nineveh's guilt — the two Nineveh books form a mercy/judgment frame around the same recitation.

**Two sub-points (no translation change proposed):**
- **(a)** Confirm whether a reader-facing cross-reference (Jonah 4:2; Exod 34:6–7) is desired at 1:3. The current `key_decisions` rationale names the Exod-34 echo but the rendered `notes` do not surface the Jonah pairing to the reader. Per the corpus pattern for canonical-thread allusions, a `messianic_reception_note`-style footnote (here a `formula_echo_note`) would be in keeping.
- **(b)** Minor doc-hygiene: the illustrative Nahum 1:3 row in `exod_34_attribute_formula_2026-05` quotes `…ยิ่งใหญ่ในพระเดช…ไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ`, whereas the shipped verse reads `…ทรงฤทธิ์อำนาจยิ่งใหญ่…ไม่ทรงปล่อยให้ผู้กระทำผิดลอยนวลพ้นโทษ`. The **locked lemma** (`ทรงกริ้วช้า`) is unaffected; only the non-formulaic free-rendering parts differ. Recommend syncing the doc's example row to the shipped wording.

**Why REVIEW, not LOCKED:** the lemma itself is locked and compliant; the actionable items are the optional cross-reference footnote and the doc-row sync, both of which want Ben's confirmation. **Severity: GREEN (compliant; flagged for the canonical-thread + doc-hygiene call).**

---

## 4. `הִנְנִי אֵלַיִךְ` "Behold, I am against you" → `เราเป็นปฏิปักษ์กับเจ้า` — **REVIEW**

The divine challenge-formula `הִנְנִי אֵלַיִךְ` opens both of Nahum's verdict oracles: **2:14** (`הִנְנִי אֵלַיִךְ נְאֻם יְהוָה צְבָאוֹת`) and **3:5** (same), each → **`ดูเถิด เราเป็นปฏิปักษ์กับเจ้า`**. This aligns with the **dominant** corpus rendering of the formula: `เราเป็นปฏิปักษ์กับเจ้า` also carries the formula at **Ezekiel 38–39** (against Gog) and **Jeremiah 50–51** (against Babylon). A **second** rendering, `เราต่อสู้กับเจ้า`, appears in the corpus but is confined to a **single Jeremiah file** (and may render a different underlying construction, e.g. `נִלְחַם בְּ־`, rather than the `הִנְנִי אֵל־` formula).

The formula is a recurring prophetic-oracle leitwort (the "challenge-to-a-doom" marker), but it is **not yet covered by a translator-decisions doc** — `leitwort_handling_policy_2026-05` does not name it. Nahum picks the majority rendering and is internally consistent (both occurrences identical).

**Why REVIEW:** the rendering is principled and consistent with the Ezekiel/Jeremiah oracular use, but the existence of a second corpus form means an external reader could ask whether `הִנְנִי אֵלַיִךְ` is meant to be a fixed formula. **Confirm** `เราเป็นปฏิปักษ์กับเจ้า` is the intended fixed rendering of `הִנְנִי אֵל־` (no change proposed), optionally folding it into the leitwort doc. **Severity: GREEN (consistent with the dominant rendering; flagged for the leitwort-documentation gap).**

---

## 5. Nahum = "comfort" (`נַחַם`) — the book-spanning name wordplay / inclusio — **REVIEW**

The prophet's name is glossed at **1:1** (`notes`: "นาฮูม (‘การปลอบโยน’)" — Nahum = "comfort/consolation," from `נָחַם`). The book then turns that name into structural irony:
- **1:12** — to Judah: `וְעִנִּתִךְ לֹא אֲעַנֵּךְ עוֹד` "though I afflicted you, I will afflict you **no more**" → comfort embodied (the `key_decisions` rationale explicitly notes "Nahum's name (‘comfort’) embodied").
- **3:7** — to Nineveh: `מֵאַיִן אֲבַקֵּשׁ מְנַחֲמִים לָךְ` "from where shall I seek **comforters** (`מְנַחֲמִים`, same root) for you?" → **`เราจะหาผู้ปลอบโยนเจ้าได้จากที่ไหน`**. The prophet *named* "Comfort" announces that for Nineveh there is **no comforter**.

This is a deliberate name-anchored inclusio (`נַחַם` at the head; the negated `מְנַחֲמִים` near the close), and it is the **dark inverse** of the Lamentations refrain `אֵין מְנַחֵם` "she has no comforter" (Lam 1) — there, Zion has no comforter under judgment; here, Nineveh has none, and that *is* Judah's comfort. The connection is currently **undocumented**: it is glossed only at 1:1, with no footnote tying the name to 3:7, and `proper_noun_wordplay_2026-05` has **no Nahum entry** (its Micah town-name paronomasia entry is the nearest analogue).

**Why REVIEW:** the wordplay is real, structural, and theologically load-bearing (it is the book's *raison d'être*), yet a reader who does not know Hebrew cannot see that "Nahum," "comfort you no more," and "no comforters" share a root. **Recommend** a `wordplay_note` at 3:7 cross-referencing the 1:1 name-gloss (and, if desired, the Lamentations `אֵין מְנַחֵם` inverse), and an entry for the Nahum name in `proper_noun_wordplay_2026-05`. **Severity: YELLOW (a reader-comprehension gap on the book's central pun; current state defensible because 1:1 carries the gloss).**

---

## 6. Divine anthropomorphism — **LOCKED**

Nahum's God-language splits cleanly along the established grammar (`divine_anthropomorphism_thai_grammar_2026-05`):
- **Third-person reference → honorific:** `אֲבַק רַגְלָיו` "dust of his feet" → **`ฝุ่นจากพระบาทของพระองค์`** (1:3); `מִפָּנָיו` / `לִפְנֵי` "before his face/presence" → **`ต่อพระพักตร์พระองค์`** (1:5, 1:6); wrath → **`พระพิโรธ`** (1:2, 1:6).
- **First-person divine speech → plain `เรา`:** "I will break their yoke" (1:13), "I am against you… I will burn your chariots… I will cut off" (2:14), "I will lift your skirts… pelt you with filth… make a spectacle of you" (3:5–7).

Critically, Nahum contains **no graphic first-person body-part-plain** case of the Isaiah 51:9 / Ezekiel "5:11-lock" class — its only divine body-parts (`רַגְלָיו`, `פָּנָיו`) appear in **third-person** reference and take the honorific. Nahum is therefore a **clean, non-friction data point** that **does not move** the open Isaiah/Jeremiah/Ezekiel/Hosea/Amos first-person-plain §13 DECIDE — exactly as Joel, Amos, and Micah were. **LOCKED** ✓. **Severity: GREEN.**

---

## 7. Versification — MT zone (ch.2: MT 2:1–14 = English 1:15–2:13) REGISTERED — **LOCKED**

Nahum's chapter 2 carries a whole-chapter MT/English offset: the English/KJV tradition closes chapter 1 one verse later than the MT, so **MT 2:1 = English 1:15** (the "feet of the herald" verse), and the offset runs through **MT 2:14 = English 2:13**; chapters 1 and 3 align. The Eremos text follows the **MT** numbering throughout. The zone is **fully registered**:
- Per-verse `versification` objects (`mt_ref` / `english_ref` / `bsb_ref` / `lxx_ref` / `diverges: true`) present on all 14 verses of chapter 2.
- Map entries **`NAM-2-1` … `NAM-2-14`** committed to `data/versification_map.json` (commit f0c7955e).
- A `versification_divergence` Layer-2 footnote at 2:1 explaining the offset and pointing to the map.

This is **cleanest-tier** — the zone was registered at ship time, not retrofitted at audit (contrast Daniel, Job, Ezekiel ch.21, which shipped with **unregistered** zones flagged at their audits). **LOCKED** ✓ (`verse_schema_and_versification_2026-05`). **Severity: GREEN.**

---

## 8. NT-reception restraint — 2:1 "feet of the herald" ∥ Isaiah 52:7 → Romans 10:15 — **STABLE**

Nahum 2:1 (= English 1:15), `הִנֵּה עַל־הֶהָרִים רַגְלֵי מְבַשֵּׂר מַשְׁמִיעַ שָׁלוֹם` → **`ดูเถิด บนภูเขาทั้งหลายมีเท้าของผู้นำข่าวดีมา ผู้ประกาศสันติสุข`**, is a near-doublet of Isaiah 52:7 that Paul lifts at Romans 10:15. The text handles this as **reception, not assertion**: a `parallel_passage_note` footnote records the Isaiah parallel and the Romans 10:15 application, and explicitly notes that "the wording in Nahum is not identical to Isaiah, so it is translated on Nahum's own terms" — the doublet is **kept independent** (not harmonized to Isaiah), consistent with the Obadiah ∥ Jeremiah-49 treatment and matching the criterion the Micah §2 doublet item raised (harmonize *verbatim-identical* shared text; keep *reworked* parallels independent — Nahum/Isaiah is the latter).

No bare `คือพระคริสต์` surface assertion appears anywhere in Nahum; the only NT bridge is the herald-feet reception note. This is clean of the Ezekiel §14 messianic-regression and consistent with the Isaiah committal-surface policy. **STABLE** ✓. **Severity: GREEN.**

---

## 9. Infrastructure — `export_to_usfm.py` rejects `NAM` — **REVIEW (infra, non-blocking)**

`scripts/export_to_usfm.py` does not yet accept the `NAM` book code (the standing minor-prophet apparatus gap — the same item flagged at Joel/Amos/Obadiah/Micah). `NAM` **is** now registered in `scripts/build_external_review_packet.py` (BOOKS list) and has been added to `scripts/audit_items_to_yaml.py` (BOOK_SLUGS + verse-ref regex) as part of this audit. This is a non-translation, non-blocking infrastructure item; it does not affect the v1 tag. **Severity: GREEN (infra; does not gate the tag).**

---

## Items reviewed that need no action

- **`בְּלִיַּעַל` "Belial/worthlessness"** — 1:11 (`יֹעֵץ בְּלִיָּעַל` "counselor of Belial" → `ที่ปรึกษาที่ชั่วช้าเลวทราม`) and 2:1 (`בְּלִיַּעַל` standalone "the wicked one" → `คนชั่วช้า`). Both render the term as a **common noun** on the `ชั่วช้า` root (not a proper name), which is principled and internally consistent; no proper-noun lock is implicated.
- **`מַלְאָכֵכֵה` "your messengers" (2:14)** → `ผู้ส่งสาร` — Nineveh's human envoys/heralds (the Rabshakeh class, cf. Isa 36). This is **not** `מַלְאַךְ יְהוָה` and does **not** implicate the `malak_yhwh_2026-05` lock.
- **`נֹא אָמוֹן` "No-Amon" = Thebes (3:8)** → `โนอามอน` with a historical Layer-2 footnote (the 663 BC fall to Ashurbanipal, the a-fortiori argument). Proper-noun transliteration + footnote, per `proper_names_and_transliteration_2026-05`. Clean.
- **Lion (2:12–14) and prostitute-sorceress (3:4) imagery** — Assyria's royal lion-emblem and the `בַּעֲלַת כְּשָׁפִים` "mistress of sorceries" → `เจ้าแม่แห่งวิทยาคม`; both carry explanatory `key_decisions`. Metaphor handled per `hebrew_idioms_and_metaphor_2026-05`. Clean.
- **"Uncover nakedness" exposure (3:5)** — `גִלֵּיתִי שׁוּלַיִךְ עַל־פָּנָיִךְ` "I will lift your skirts over your face" → `เราจะถลกกระโปรงของเจ้าขึ้นปกหน้าของเจ้า`. The shaming-of-the-harlot image is rendered directly (within the latitude of `uncover_nakedness_euphemism_2026-05`, which governs the `עֶרְוָה` euphemism class); no euphemism-lock conflict.
- **Nahum 2:4 looser back-translation match** — the verse's `key_decisions` self-notes the dense hapax-laden battle-tableau (`מְאָדָּם`, `מְתֻלָּעִים`, `פְּלָדוֹת`, `בְּרֹשִׁים`) accounts for a looser back-translation alignment; the per-chapter check report is **green**. No action.
- **Divine-names false-positive class** — `check_divine_names` produces **zero** Nahum warnings (no standalone-Adonai `C-soft` flags, no human-subject false positives such as Amos 4:1's). Cleanest possible state.

## Recommended new / amended translator-decisions docs

These are **recommendations only** — per the checklist, this audit recommends but does not author corpus docs, and none is *owed* (there is no DECIDE resolving into a lock). All are optional polish:

1. **`proper_noun_wordplay_2026-05` — add a Nahum-name entry** (§5): the `נַחַם`/`מְנַחֲמִים` name-inclusio (1:1 ↔ 1:12 ↔ 3:7), cross-referenced to the Lamentations `אֵין מְנַחֵם` inverse. Pairs with a `wordplay_note` footnote at 3:7.
2. **`leitwort_handling_policy_2026-05` — add the `הִנְנִי אֵל־` "I am against you" formula** (§4): fix `เราเป็นปฏิปักษ์กับเจ้า` as the rendering across Ezk 38–39 / Jer 50–51 / Nah 2:14, 3:5, and disambiguate it from the single-file Jeremiah `เราต่อสู้กับเจ้า`.
3. **`exod_34_attribute_formula_2026-05` — sync the Nahum 1:3 example row** to the shipped wording (§3, sub-point b), and optionally note the **Jonah 4:2 ↔ Nahum 1:3** mercy/judgment inversion as a canonical-thread cross-reference.

## Checklist for Ben before tagging `book-nahum-v1`

- [ ] **§3 REVIEW** — confirm whether a `formula_echo_note` footnote (Jonah 4:2 / Exod 34:6–7) is wanted at 1:3; approve the `exod_34_attribute_formula` example-row sync. No translation change proposed.
- [ ] **§4 REVIEW** — confirm `เราเป็นปฏิปักษ์กับเจ้า` is the intended fixed rendering of `הִנְנִי אֵל־` (optionally document the leitwort). No change proposed.
- [ ] **§5 REVIEW** — confirm whether to add a `wordplay_note` at 3:7 + a `proper_noun_wordplay` entry for the Nahum-name inclusio. No change proposed.
- [ ] **§9 REVIEW** — acknowledge the `export_to_usfm.py` `NAM` gap (infra; non-blocking).
- [ ] **No DECIDE items** — nothing blocks the v1 tag; the four REVIEWs are confirmations, not changes.
- [ ] Tag `book-nahum-v1` after confirming the above.

*Status counts: 4 LOCKED · 1 STABLE · 4 REVIEW · 0 DECIDE.*
