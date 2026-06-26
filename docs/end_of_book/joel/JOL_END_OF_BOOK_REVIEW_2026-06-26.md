# Joel — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 4 chapters of Joel (73 verses, MT versification); `glossary.json`; `docs/translator_decisions/` corpus. **The second Book-of-the-Twelve title in the corpus** (after Hosea) and the OT's foundational *Day-of-the-LORD* book — the יוֹם יְהוָה leitwort that Amos, Obadiah, Zephaniah, and the NT (Acts 2; 1 Thess 5; 2 Pet 3) all inherit. Joel is also one of the most densely NT-quoted Minor Prophets: **2:28–32 (MT 3:1–5) "I will pour out my Spirit"** → the centrepiece of Peter's Pentecost sermon (Acts 2:17–21); **2:32 (MT 3:5) "everyone who calls on the name of the LORD"** → Acts 2:21 **and** Rom 10:13; **3:13 (MT 4:13) sickle-and-winepress** → Rev 14:15–20. **All of the NT it cross-quotes is already shipped.**
**Trigger:** JOL 4 shipped (last chapter, commit `29c6a93b`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **12 cross-cutting items reviewed.** Mechanical gates (§1) pass: 4/4 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks); `audit_inclusion_variants.py --book joel --strict` = **0 candidates, exit 0**; `check_versification_anchor.py --book JOL` = exit 0 (the two MT-vs-English divergence zones — the whole of chs **3 and 4** — are fully registered in `data/versification_map.json` as `JOL-3-1…5` + `JOL-4-1…21`, **already committed**, so Joel does **not** reproduce the Ezekiel/Hosea "versification-map sitting uncommitted" gotcha); `git status output/` clean. `check_divine_names.py --book JOL` = exit 0 with **one warning** (ch.3 — see §10). All four `output/textual_variants/joel_NN.json` files carry the Exod-34 grace-formula footnote (ch.2), the locust-lexicon note (ch.1), the versification-divergence footnotes (chs 3, 4), and the Acts/Romans NT-citation footnote (ch.3). **Mechanically Joel is among the cleanest OT book states in the corpus** — comparable to Hosea, with the one ch.3 footnote-type gap as the sole non-green checker line.

- **1 item flagged DECIDE** (Ben choice needed before tagging `book-joel-v1`):
  - **§12 — 2:23 הַמּוֹרֶה לִצְדָקָה: "early rain for vindication" vs the messianic "Teacher of Righteousness."** This is Joel's single genuine interpretive fork. מוֹרֶה is a real double-entendre: "early/autumn rain" **and** "teacher." The translation follows the **rain reading** → **ฝนต้นฤดู…ด้วยความชอบธรรม** (justified by the immediately-following גֶּשֶׁם … וּמַלְקוֹשׁ "downpour … and latter rain," which fixes מוֹרֶה in its precipitation sense), and discloses the messianic "ผู้สอนแห่งความชอบธรรม" reading — held by Qumran (the *moreh ṣedeq*) and parts of the rabbinic/patristic tradition — in a Tier-2 footnote. This is the right restraint and is consistent with the **committal-messianic-surface policy ratified at the Isaiah audit** (translate the plain-sense surface; reserve the messianic reading for apparatus). But because it is the most contested verse in the book and touches messianic surfacing, **Ben should explicitly ratify "rain-reading primary, messianic-in-footnote"** before the tag, so it sets the precedent for the rest of the Twelve. See §12.

- **3 items flagged REVIEW** (worth Ben's confirmation):
  - **§9 — Joel → NT reception-history surfaces (Acts 2:17–21; Rom 10:13; Rev 14).** Joel's Spirit-outpouring oracle (3:1–5 MT = 2:28–32 Eng) is the longest OT block Peter quotes, and the Joel Thai legitimately **differs from the shipped Acts 2 Thai** at the points where Acts follows the LXX and Joel follows the MT: (a) **old-men/young-men order is swapped** (MT 3:1: old men dream → young men visions; Acts 2:17: young men visions → old men dreams); (b) **2:31/3:4 "great and *dreadful*" נוֹרָא → น่าสะพรึงกลัว** vs **Acts 2:20 "great and *glorious*" ἐπιφανῆ → รุ่งโรจน์**; (c) "all flesh" כָּל־בָּשָׂר → **มนุษย์ทั้งปวง** (Joel) vs **มนุษย์ทุกคน** (Acts). All three are correct source-driven divergences, and joel_03's `nt_citation_note` footnote already names the Acts/Romans citations. The "calls on the name" idiom **ร้องออกพระนาม…จะรอด** matches Rom 10:13 verbatim. **Confirm** the policy (translate each from its own base, footnote the citation) and whether the marquee 2:31 *dreadful*/*glorious* split clears the Tier-2-footer floor the way the Jeremiah 31:32 → Heb 8:9 case did. See §9.
  - **§10 — ch.3 YHWH first-occurrence footnote uses the wrong type.** chs 1, 2, 4 each carry a `tetragrammaton_convention_first_occurrence` footnote; **ch.3 does not** — its YHWH (3:4, 3:5 ×3) is disclosed inside the `nt_citation_note` instead, so `check_divine_names.py` warns (exit 0, non-fatal). The reader is **not** deprived of the information, but coverage is 3/4 by canonical type vs Hosea's clean 4/4. A one-line `tetragrammaton_convention_first_occurrence` entry in joel_03 would clear the warning. See §10.
  - **§11 — `export_to_usfm.py` still rejects `JOL`** ("Unknown book code: JOL"), the recurring OT book-code gotcha (same as the still-open ISA/EZK/LAM cases). Not a translation issue and not a tag blocker, but Paratext export of Joel is impossible until the code is registered. See §11.

- **STABLE-but-undocumented patterns recommending doc-lift / note:**
  - **§5 — the יוֹם יְהוָה "Day of the LORD" leitwort** (Joel's controlling theme, 5×: 1:15, 2:1, 2:11, 2:31/3:4, 3:14/4:14) → **วันแห่งองค์พระผู้เป็นเจ้า**, uniform and matching the `glossary.json` ἡμέρα κυρίου corpus entry — but with **no OT translator-decisions doc**. **Recommend `day_of_the_lord_leitwort_2026-06.md`** as the canonical reference the already-shipped Isaiah/Amos-bound NT surface (Acts 2:20; 1 Thess 5:2; 2 Pet 3:10) was derived against and that the rest of the Twelve will inherit.
  - **§6 — the four-locust lexicon** (1:4 + 2:25): גָּזָם/אַרְבֶּה/יֶלֶק/חָסִיל → a fixed 1:1 map **ตัด / ฝูง / วัยกระโดด / ทำลาย**, held across both verses despite their different Hebrew word-order. Footnoted at 1:4; **no corpus doc.** Recommend a short note (`joel_locust_lexicon_2026-06.md` or a paragraph in a leitwort-handling doc).
  - **§7 — the plowshares↔swords reversal** (4:10 vs the shipped Isaiah 2:4): the **same** Thai word-pair is reused in inverted position (Isa 2:4 ดาบ→ผาลไถนา, หอก→มีดลิดแขนง; Joel 4:10 ผาลไถนา→ดาบ, มีดลิดแขนง→หอก), so the deliberate eschatological inversion lands unmistakably. Already footnoted in joel_04. Confirm + optionally note.
  - **§8 — first-person divine possessives rendered plain** (my land אַרְצִי → แผ่นดินของเรา, my people עַמִּי → ประชากรของเรา, my holy mountain הַר קָדְשִׁי → ภูเขาบริสุทธิ์ของเรา) — uniform plain-possessive handling, consistent with the corpus practice for divine possession of land/people/mountain (distinct from body-part Rachasap).

- **External AI review (§3) pending.** Suggested 4-item packet: the 2:23 môreh rain/teacher fork (§12 DECIDE); the Joel→Acts/Romans MT/LXX reception surface + footer question (§9 REVIEW); the Day-of-the-LORD leitwort rendering + doc-lift (§5 STABLE — also tests consistency against the shipped Acts 2:20 / 1 Thess 5 surface); the four-locust lexicon (§6 STABLE — tests the "four species vs four stages" disambiguation).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. יְהוָה Tetragrammaton (Layer 1) + first-occurrence footnote coverage — **LOCKED**

YHWH → **องค์พระผู้เป็นเจ้า** in every occurrence (Layer 1), with each verse's KD citing `divine_names_table_2026-05`. The vocative "O LORD" (1:19 אֵלֶיךָ יְהוָה; 2:17 חוּסָה יְהוָה) correctly takes **ข้าแต่องค์พระผู้เป็นเจ้า** / **ขอทรงเมตตา…องค์พระผู้เป็นเจ้า**. The covenant self-declaration אֲנִי יְהוָה אֱלֹהֵיכֶם (2:27, 4:17) → **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า**. The divine word-formula כִּי יְהוָה דִּבֵּר (4:8) → **เพราะองค์พระผู้เป็นเจ้าได้ตรัสไว้แล้ว**. The compound יוֹם יְהוָה ("Day of the LORD," 5×) → **วันแห่งองค์พระผู้เป็นเจ้า** (→ §5). Three of four `output/textual_variants/joel_NN.json` files carry the `tetragrammaton_convention_first_occurrence` footnote (chs 1, 2, 4); **ch.3's YHWH is disclosed under a differently-typed footnote** — the canonical Layer-1 rendering is uniform and correct, but the footnote-type coverage gap is split out as **§10 (REVIEW)**. The Layer-1 rendering itself is **LOCKED** ✓ per `divine_names_table_2026-05.md`. **Severity: GREEN.**

---

## 2. שַׁדַּי Shaddai + divine titles (1:15) — **LOCKED**

The single Shaddai in the book — וּכְשֹׁד מִשַׁדַּי "like destruction from the Almighty" (1:15) — → **ความพินาศจากองค์ผู้ทรงมหิทธิฤทธิ์**, matching the corpus Shaddai form **ผู้ทรงมหิทธิฤทธิ์** (`divine_names_table_2026-05`; the wordplay שֹׁד/שַׁדַּי "šōḏ/šaday" is named in the KD per `wordplay_and_paronomasia_2026-05`). No other divine title-cluster (no Sabaoth, no standalone Adonai) occurs in Joel. **LOCKED** ✓. **Severity: GREEN.**

---

## 3. Exodus 34:6 grace-attribute formula (2:13) — **LOCKED**

Joel 2:13 is the theological heart of the book's repentance call, and it quotes the Exod-34:6 attribute-formula. All four clauses match the corpus lock (the shipped Jonah 4:2 / Ps 103:8 surface), and the rendering passes `check_phrase_consistency.py` (0 violations):

- חַנּוּן וְרַחוּם → **ทรงพระคุณและทรงพระเมตตา** ("gracious and compassionate")
- אֶרֶךְ אַפַּיִם → **ทรงกริ้วช้า** ("slow to anger")
- וְרַב־חֶסֶד → **ทรงบริบูรณ์ด้วยความรักมั่นคง** (חֶסֶד → ความรักมั่นคง, the corpus chesed-lock)
- וְנִחָם עַל־הָרָעָה → **ทรงเปลี่ยนพระทัยจากการลงโทษ** ("relents from disaster")

The formula is reader-disclosed in the joel_02 `tetragrammaton_and_formula_note` footnote, which explicitly cross-references Jonah 4:2 / Ps 103:8. The נִחָם "relent" root recurs at 2:14 (מִי יוֹדֵעַ יָשׁוּב וְנִחָם → ทรงหันกลับและทรงเปลี่ยนพระทัย), correctly held to the same royal-verb pattern. **LOCKED** ✓ per `exod_34_attribute_formula_2026-05.md`. **Severity: GREEN.**

---

## 4. Divine anthropomorphism / first-person register — **LOCKED (Joel adds no friction)**

The Hosea audit's loudest finding (§7 DECIDE) was the **codified first-person-plain rule** for divine body-parts (my hand → plain มือ, my heart → plain ใจ) and its internal inconsistency (face kept royal) — a drift the Isaiah, Jeremiah, and Ezekiel audits also flagged, **all still untagged and unreconciled.** **Joel does not reproduce this friction.** Its divine anthropomorphisms are uniformly **royal** and consistent:

- **my Spirit** רוּחִי (1st-person divine, 3:1, 3:2) → **พระวิญญาณ** (royal — the standard, not a body-part-to-plain case)
- **his voice** נָתַן קוֹלוֹ (2:11) / יִתֵּן קוֹלוֹ (4:16) → **ทรงเปล่งพระสุรเสียง** (royal)
- **God relents** וְנִחָם (2:13–14) → **ทรงเปลี่ยนพระทัย** (royal พระทัย for God's "heart/mind")

The only plain ใจ in the book is the **people's** heart — קִרְעוּ לְבַבְכֶם "rend *your* hearts" (2:13) → ฉีก**ใจ**ของเจ้า — correctly plain (human subject). So Joel is a clean, non-friction data point for the open corpus question: it shows the royal-register default working without strain when no first-person divine *body-part* (hand/eye/face) appears. **No new exception is introduced.** Compliant with `divine_anthropomorphism_thai_grammar_2026-05.md`. **The cross-corpus DECIDE remains open** (Isaiah/Jeremiah/Ezekiel/Hosea) but Joel does not move it. **LOCKED** ✓. **Severity: GREEN.**

---

## 5. יוֹם יְהוָה "Day of the LORD" leitwort — **STABLE (recommend corpus doc)**

The controlling theme of Joel, and the verse-cluster the rest of the Twelve and the NT build on. Rendered **uniformly** as **วันแห่งองค์พระผู้เป็นเจ้า** across all five occurrences:

| Ref (MT) | Hebrew | Thai |
|---|---|---|
| 1:15 | יוֹם יְהוָה | วันแห่งองค์พระผู้เป็นเจ้า (…ใกล้เข้ามาแล้ว) |
| 2:1 | יוֹם־יְהוָה | วันแห่งองค์พระผู้เป็นเจ้า (…กำลังมาถึง) |
| 2:11 | יוֹם־יְהוָה … גָדוֹל וְנוֹרָא | วันแห่งองค์พระผู้เป็นเจ้า…ยิ่งใหญ่และน่าสะพรึงกลัว |
| 3:4 (Eng 2:31) | יוֹם יְהוָה הַגָּדוֹל וְהַנּוֹרָא | วันแห่งองค์พระผู้เป็นเจ้าอันยิ่งใหญ่และน่าสะพรึงกลัว |
| 4:14 (Eng 3:14) | יוֹם יְהוָה | วันแห่งองค์พระผู้เป็นเจ้า |

The form matches the `glossary.json` ἡμέρα κυρίου corpus entry (so the already-shipped Acts 2:20, 1 Thess 5:2, 2 Pet 3:10 surfaces all read the same **วันแห่งองค์พระผู้เป็นเจ้า**). This is the project's single most cross-book-load-bearing prophetic phrase, yet it lives only in a glossary entry + per-verse KDs — **no `docs/translator_decisions/` doc.** **Recommend `day_of_the_lord_leitwort_2026-06.md`** consolidating the rendering, the anarthrous-technical rationale, and the OT↔NT consistency, as the canonical reference for Amos/Obadiah/Zephaniah/Malachi. **Severity: GREEN (consistency), but doc-lift recommended.**

---

## 6. The four-locust lexicon (1:4 / 2:25) — **STABLE (recommend note)**

Joel's four Hebrew locust-words are mapped to four fixed Thai terms, held across **both** occurrences despite the Hebrew word-order differing between them:

| Hebrew | Thai | 1:4 order | 2:25 order |
|---|---|---|---|
| גָּזָם gāzām | **ตั๊กแตนตัด** | 1st | 4th |
| אַרְבֶּה ʾarbeh | **ตั๊กแตนฝูง** | 2nd | 1st |
| יֶלֶק yeleq | **ตั๊กแตนวัยกระโดด** | 3rd | 2nd |
| חָסִיל ḥāsîl | **ตั๊กแตนทำลาย** | 4th | 3rd |

The 1:1 lemma→term map is preserved verbatim, so the "what one left, the next ate" cascade (1:4) and the "I will repay the years the *X* ate" restoration (2:25) line up word-for-word. The joel_01 footnote discloses the scholarly "four species vs four growth-stages" ambiguity and the Exod-10 Egyptian-plague echo of אַרְבֶּה. **STABLE** — well-handled and footnoted; **recommend a short corpus note** so Nahum 3:15–17 (אַרְבֶּה/יֶלֶק) inherits the same map. **Severity: GREEN.**

---

## 7. Plowshares ↔ swords reversal (4:10 vs Isaiah 2:4) — **STABLE**

Joel 4:10 (Eng 3:10) deliberately **inverts** the shipped Isaiah 2:4 / Micah 4:3 peace-oracle. The translation reuses the **same** four Thai nouns in swapped positions, so the inversion is unmistakable against the already-shipped Isaiah surface:

- **Isa 2:4** (shipped): כִּתְּתוּ חַרְבוֹתָם לְאִתִּים → ตี**ดาบ**…เป็น**ผาลไถนา**; וַחֲנִיתוֹתֵיהֶם לְמַזְמֵרוֹת → ตี**หอก**…เป็น**มีดลิดแขนง**
- **Joel 4:10**: כֹּתּוּ אִתֵּיכֶם לַחֲרָבוֹת → จงตี**ผาลไถนา**…ให้เป็น**ดาบ**; וּמַזְמְרֹתֵיכֶם לִרְמָחִים → ตี**มีดลิดแขนง**…ให้เป็น**หอก**

The lexical pair (ดาบ/ผาลไถนา, หอก/มีดลิดแขนง) is identical; only the direction flips. Footnoted in joel_04 (and in the verse summary). The hapax חַלָּשׁ "the weak" → คนอ่อนแอ. **STABLE** ✓ — confirm and optionally fold into a "prophetic-allusion inversion" note. **Severity: GREEN.**

---

## 8. First-person divine possessives rendered plain — **STABLE**

Where God speaks of *his land / his people / his holy mountain* in the first person, the possessive is rendered with the plain ของเรา (not a royal construct), consistent across the book and with corpus practice for divine possession of land/nation:

- אַרְצִי "my land" (1:6; 4:2) → **แผ่นดินของเรา**
- עַמִּי "my people" (2:26, 2:27; 4:2, 4:3) → **ประชากรของเรา**
- נַחֲלָתִי "my inheritance" (4:2) → **มรดกของเรา**
- הַר קָדְשִׁי "my holy mountain" (2:1; 4:17) → **ภูเขาบริสุทธิ์ของเรา**

This is distinct from the body-part Rachasap question (§4) — it concerns possession, not anatomy — and is uniform. **STABLE** ✓. **Severity: GREEN.**

---

## 9. Joel → NT reception-history surfaces (Acts 2; Rom 10:13; Rev 14) — **REVIEW**

Joel 3:1–5 (MT = Eng 2:28–32) is the longest OT passage Peter quotes (Acts 2:17–21), and the Joel Thai **legitimately diverges** from the shipped Acts 2 Thai exactly where Acts follows the LXX and Joel follows the MT. All three divergences below are correct source-driven choices — the question is purely whether the apparatus should flag them more sharply:

| Point | Joel (MT-based) | Acts 2 (LXX-based, shipped) |
|---|---|---|
| Order, 3:1/2:17 | **คนชรา…จะฝันเห็น** then **คนหนุ่ม…จะเห็นนิมิต** (old→young) | **คนหนุ่ม…จะเห็นนิมิต** then **คนชรา…จะฝันเห็น** (young→old) |
| "all flesh" כָּל־בָּשָׂר | **มนุษย์ทั้งปวง** | มนุษย์ทุกคน |
| 3:4/2:31 epithet | יוֹם…הַנּוֹרָא "dreadful" → **น่าสะพรึงกลัว** | ἐπιφανῆ "glorious" → **รุ่งโรจน์** |

The "calls on the name" climax matches the corpus idiom across all three witnesses: Joel 3:5 **ทุกคนที่ร้องออกพระนามขององค์พระผู้เป็นเจ้าจะรอด** = **Rom 10:13 verbatim**; Acts 2:21 reads จะ**ได้รับความรอด** (same idiom, fuller verb). joel_03 already carries an `nt_citation_note` footnote naming the Acts 2:17–21 and Rom 10:13 citations, and joel_04's harvest imagery (4:13) footnotes the Rev 14:15–20 reuse. **REVIEW questions:** (1) Confirm the policy — each text translated from its own base, NT citation disclosed in a footnote, no harmonizing of the OT surface to the NT quotation. (2) Does the **2:31 "dreadful" (MT) vs "glorious" (Acts/LXX)** split — a substantive tonal divergence on a marquee verse — clear the same Tier-2 reader-footer floor the **Jeremiah 31:32 → Heb 8:9** case was flagged for, or is the existing combined `nt_citation_note` sufficient? **Severity: YELLOW (apparatus/disclosure).**

---

## 10. ch.3 YHWH first-occurrence footnote — wrong type — **REVIEW**

`check_divine_names.py --book JOL` exits 0 but emits one warning:

```
[D] joel ch.3: contains YHWH but no first-occurrence footnote in output/textual_variants/joel_03.json
```

chs 1, 2, 4 each carry a `tetragrammaton_convention_first_occurrence` entry; **ch.3 does not.** Its YHWH (3:4, and 3:5 ×3 — "calls on the name of YHWH … as YHWH promised … whom YHWH calls") is disclosed instead inside the chapter's `nt_citation_note` ("พระนาม יהוה ปรากฏที่ข้อ 4 และ 5 (สามครั้ง)"). So the reader **is** told — the gap is one of footnote *type*, not of disclosure — but the checker (and the corpus's 4/4-coverage convention, which Hosea met) flags it. A one-line `tetragrammaton_convention_first_occurrence` entry added to joel_03 would clear the warning and bring Joel to full canonical coverage. **This is a textual_variants edit, not a translation edit** — appropriate to fix before the tag if Ben wants the clean checker line; the existing disclosure is not wrong. **Severity: YELLOW (mechanical).**

---

## 11. Infrastructure — `export_to_usfm.py` rejects `JOL` — **REVIEW**

`python3 scripts/export_to_usfm.py --book JOL` → `✗ Unknown book code: JOL` / `⚠ JOL: no translated chapters found`. This is the recurring OT book-code gotcha already noted for ISA, EZK, and LAM (the export script's internal code table lags the YAML/packet tables). It blocks Paratext (.SFM) export of Joel but is **not** a translation issue and **not** a v1-tag blocker. This audit has already registered JOL in `build_external_review_packet.py` (BOOKS) and `audit_items_to_yaml.py` (BOOK_SLUGS); `export_to_usfm.py` should be registered in the same pass when the maintainer next touches it. **Severity: YELLOW (infra, non-blocking).**

---

## 12. 2:23 הַמּוֹרֶה לִצְדָקָה — "early rain" vs the messianic "Teacher of Righteousness" — **DECIDE**

Joel's one genuine interpretive fork. The Hebrew הַמּוֹרֶה is a true double-entendre:

- **HEB:** `כִּי־נָתַן לָכֶם אֶת־הַמּוֹרֶה לִצְדָקָה וַיּוֹרֶד לָכֶם גֶּשֶׁם מוֹרֶה וּמַלְקוֹשׁ`
- **TH (rain reading):** `เพราะพระองค์ประทาน**ฝนต้นฤดู**ให้แก่พวกเจ้า**ด้วยความชอบธรรม** พระองค์ทรงเทฝนลงมา…ทั้ง**ฝนต้นฤดูและฝนปลายฤดู**`

מוֹרֶה means both **"early/autumn rain"** and **"teacher,"** so הַמּוֹרֶה לִצְדָקָה reads either "the early rain *for vindication/righteousness*" **or** "the *Teacher of Righteousness*." The translation takes the **rain reading**, decisively anchored by the same-verse pairing גֶּשֶׁם מוֹרֶה וּמַלְקוֹשׁ "downpour, early-rain, and latter-rain" (which uses מוֹרֶה unambiguously of precipitation). The **messianic** reading — the Qumran *moreh ṣedeq* / "Teacher of Righteousness," and the patristic christological gloss — is disclosed in the joel_02 Tier-2 footnote (`translation_ambiguity_note`).

This is the **correct** application of the **committal-messianic-surface policy ratified at the Isaiah audit** (translate the plain-sense surface; reserve a messianic/typological reading for the apparatus rather than baking it into the rendered text). It is internally well-argued and footnoted.

**Why DECIDE, not REVIEW:** it is the most contested verse in the book; it touches messianic surfacing directly; and its disposition sets the precedent for the rest of the Twelve (e.g., the messianic surfaces in Amos 9:11, Micah 5, Zechariah). Ben should **explicitly ratify "rain-reading primary, messianic-in-footnote"** so the choice is logged as a corpus precedent and not merely a per-verse default. **No translation change is proposed** — this is a ratification gate. **Severity: the one item blocking `book-joel-v1`.**

---

## Recommended new translator-decisions docs

1. **`day_of_the_lord_leitwort_2026-06.md`** (§5) — consolidate יוֹם יְהוָה → วันแห่งองค์พระผู้เป็นเจ้, the anarthrous-technical rationale, and OT↔NT consistency (Acts 2:20 / 1 Thess 5:2 / 2 Pet 3:10). The most cross-book-load-bearing prophetic phrase in the corpus; currently glossary-only.
2. **`joel_locust_lexicon_2026-06.md`** (§6) — the גָּזָם/אַרְבֶּה/יֶלֶק/חָסִיל → ตัด/ฝูง/วัยกระโดด/ทำลาย 1:1 map, the "species vs stages" note, and forward-protection for Nahum 3:15–17.

(Both are STABLE-confirm doc-lifts, not new decisions. They should be written **only if Ben confirms** the renderings at review — per the checklist, this audit recommends but does not author them.)

## Checklist for Ben before tagging `book-joel-v1`

- [ ] **§12 DECIDE** — ratify 2:23 "rain-reading primary, messianic Teacher-of-Righteousness in footnote."
- [ ] §9 REVIEW — confirm the Joel↔Acts/Romans MT/LXX divergence policy; decide whether 2:31 *dreadful/glorious* warrants a Tier-2 footer.
- [ ] §10 REVIEW — optionally add a `tetragrammaton_convention_first_occurrence` footnote to joel_03 to clear the `check_divine_names` warning.
- [ ] §11 REVIEW — register `JOL` in `export_to_usfm.py` (infra; non-blocking).
- [ ] §5 / §6 — approve (or decline) the two recommended translator-decisions docs.
- [ ] Then: `bash scripts/ship_book.sh JOL` (lock-the-book ship + tag).
