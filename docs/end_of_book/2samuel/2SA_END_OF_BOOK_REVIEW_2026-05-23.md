# 2 Samuel — End-of-Book Review

**Date:** 2026-05-23
**Scope:** All 24 chapters of 2 Samuel (695 verses); `glossary.json`; `docs/translator_decisions/` corpus (~95 docs through the 1SA end-of-book audit).
**Trigger:** 2SA 24 shipped (commit `26b7618`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Tenth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel) and the **fourth Former-Prophets / Deuteronomistic-History book**. 2 Samuel is the **direct narrative continuation of 1 Samuel** and the first downstream test of several items the 1SA audit explicitly forward-deferred to this book: the Adonai-YHWH compound prayer cluster (2 Sam 7:18–29), the Spirit-of-YHWH lock at 23:2, the divine-mal'akh narrative at ch 24, and the nicham relenting at 24:16.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) pass: 24/24 chapters have green per-chapter reports + back-translations + textual-variant files; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `check_divine_names.py` 0 hard fails (162 corpus [C-soft] warnings, ~36 in 2SA — all human-addressee אֲדֹנִי "my lord", expected per §2); `audit_inclusion_variants.py --book 2samuel --strict` reports 0 candidates (exit 0); YHWH `องค์พระผู้เป็นเจ้า` surface = 152, `ยาห์เวห์` residues in verse text = **0**.
- **2 Samuel passes the items 1 Samuel failed.** The four 1SA-deferred items all ship in good shape here:
  - **The Spirit-of-YHWH lock HOLDS at 2 Sam 23:2.** David's last words `רוּחַ יְהוָה דִּבֶּר־בִּי` render `พระวิญญาณขององค์พระผู้เป็นเจ้าตรัสในข้า` — **with** the `พระ` honorific (the exact omission that drifted across all 12 1SA occurrences, §4 of the 1SA audit). 2 Samuel did **not** inherit the 1SA bare-`วิญญาณ` drift. The verse even carries the 2 Pet 1:21 NT-inspiration cross-reference at Layer 1. **LOCKED.**
  - **The Adonai-YHWH compound prayer cluster (7:18–29) is exemplary.** All 7 `אֲדֹנָי יְהוִה` occurrences render `องค์พระผู้เป็นเจ้า` per the `divine_names_table_2026-05.md` lock, each with a per-verse `key_decisions` entry recording the underlying compound (Layer-1 transparency). The JDG-audit §8 / 1SA §2 "Adonai-prayer drift" concern does **not** materialize — 2 Sam 7 is the corpus's densest compound-Adonai prayer and ships internally uniform. One register nuance flagged REVIEW (§2).
  - **The divine-mal'akh lock HOLDS at ch 24.** The census-plague destroying-angel renders `ทูตสวรรค์` and `מַלְאַךְ יְהוָה` → `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` per `malak_yhwh_2026-05.md` — the first divine-mal'akh narrative since the 1SA gap, shipping compliant. **LOCKED.**
  - **The nicham lock HOLDS at 24:16.** `וַיִּנָּחֶם יְהוָה` → `องค์พระผู้เป็นเจ้าทรงเปลี่ยนพระทัย` per `nicham_divine_relenting_2026-05.md`, the exact verse 1SA §16 forward-protected, with the Jer 18:7–10 cross-reference. **LOCKED.**
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-2samuel-v1`):
  - **§13 Textual-variant Tier-2 reader-footer gap.** 2 Samuel's significant MT cruxes (15:7 "forty"→"four" departure, 24:1 YHWH-incited vs 1 Chr 21:1 Satan, 24:9 census numbers, 24:13 seven-vs-three years, 21:19 Elhanan-Goliath) are **documented at Layer 1** (`key_decisions`/`notes`) — materially better than 1SA's silent variants — but **not lifted to the Layer-2 reader-facing chapter-footers** (`output/textual_variants/2samuel_NN.json`, which carry only the YHWH first-occurrence footnote). The canon policy (`ot_canon_and_text_base_2026-05.md` §"When to depart from MT", Trigger 1) **explicitly requires** the 15:7-type departure to carry a `[Tier 2]` verse-level footer note — currently absent. Inherits and parallels 1SA §17 (still pending Ben).
- **6 items flagged REVIEW** (worth Ben's confirmation):
  - §2 Adonai-YHWH compound **prayer-vocative `ข้าแต่`-omission** in 7:18–29 (vocabulary-compliant; the lock's vocative sub-form is `ข้าแต่องค์พระผู้เป็นเจ้า` but the cluster is mid-sentence appositional, not sentence-initial interjection — confirm the principle)
  - §13b 15:7 "four years" — confirm it clears the canon-policy Trigger-1 "semantically nonsensical" bar (MT reads `אַרְבָּעִים`, forty)
  - §11 "until this day" leitwort — 2SA uniformly `จนถึงวันนี้` (continues the 1SA bare-form; carries the unresolved 1SA §14 cross-book question vs JDG `จนถึงทุกวันนี้`)
  - §16 **22:11 doubled-`ทรง` copy-edit** — `พระองค์ทรงทรงเครูบ` (should be `ทรงเครูบ`); a surface typo, passes all checks because no script catches doubled-word artifacts
  - §15 Annotation-coverage variance (`thai_summary` 43–96%; ch 2/3/13 ~43–46%, ch 22 Psalm-18 song only 49%) — confirm intentional
  - §10 12:31 Rabbah "saws / brick-kilns" forced-labor reading (warfare-ethics) — confirm the labor interpretation
- **2 items recommend new corpus docs** (STABLE-but-undocumented):
  - §14 **Synoptic / parallel-passage handling** — 2 Sam 22 ≈ Psalm 18 (Davidic-appendix vs Psalter) **and** the Samuel ↔ Chronicles narrative-synoptic (1 Chr 11–21 ≈ 2 Sam 5–24). Excellent Layer-1+2 annotation ships, but no corpus doc locks the parallel-passage policy. Forward-protects the Psalter (Ps 18; 14//53; 40//70; 108=57+60), 2 Kgs 18–20//Isa 36–39, 2 Kgs 24–25//Jer 52, and the whole Chronicles synoptic. **Priority HIGH.**
  - §12 **Davidic-covenant Christology thread (2 Sam 7:12–16)** — the OT seedbed of messianic kingship; well-annotated at Layer 1 (Heb 1:5 at 7:14) and the NT side is shipped (Luke 1:32–33, Acts 2:30, Heb 1:5, Rev 22:16). A "closes-the-loop" doc analogous to the recommended 1SA Hannah-Magnificat thread. **Priority MEDIUM.**
- **External AI review (§3) pending.** Suggested 4-item packet (textual-variant Tier-2 gap §13 — highest; Adonai-YHWH prayer-vocative §2; synoptic-parallel doc §14; 15:7 four/forty + cross-book leitwort §13b/§11).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH `องค์พระผู้เป็นเจ้า` surface in `thai` verse-text: **152 occurrences** across the 24 chapters. **`ยาห์เวห์` residues in verse text: zero.** Concentrated in the Davidic-covenant prayer (ch 7), the ark-procession (ch 6), David's song (ch 22), and the census-plague (ch 24).

**Title-cluster compounds correctly differentiated within ch 7's prayer:**
- `יְהוָה צְבָאוֹת` (YHWH Tsebaoth) at 7:26, 7:27 → **`องค์พระผู้เป็นเจ้าจอมโยธา`** (matches Jas 5:4 NT lock) ✓
- `יְהוָה אֱלֹהִים` (YHWH Elohim) at 7:25 → **`องค์พระผู้เป็นเจ้าพระเจ้า`** ✓
- `אֲדֹנָי יְהוִה` (Adonai-YHWH compound) ×7 → **`องค์พระผู้เป็นเจ้า`** (see §2) ✓

**Per-chapter first-occurrence YHWH footnote.** 24/24 chapters carry the locked Tier-2 explanation in `output/textual_variants/2samuel_NN.json`. Chs 9 and 13 (which have no YHWH occurrence) carry a `chapter_overview_note` instead — good editorial pattern (mirrors 1SA's YHWH-absent chapter handling).

**LOCKED** ✓.

---

## 2. Elohim + Adonai-YHWH compound divine names (2 Sam 7:18–29) — **LOCKED (exemplary Layer-1); REVIEW on prayer-vocative `ข้าแต่`**

- **Elohim → พระเจ้า** uniform across 2SA ✓. No drift.
- **The Adonai-YHWH compound prayer (7:18–29) is the corpus's densest `אֲדֹנָי יְהוִה` cluster** — 7 occurrences in David's covenant prayer (7:18, 7:19 ×2, 7:20, 7:22, 7:28, 7:29). This is the verse-block JDG-audit §8 and 1SA §2 **explicitly forward-deferred** to 2 Sam 7 ("the compound's first major recurrence after Joshua-Judges is at 2 Sam 7:18–29 — 7× in one prayer").

All 7 render **`องค์พระผู้เป็นเจ้า`** per the `divine_names_table_2026-05.md` lock ("Compound collapses to single Thai rendering; `key_decisions` records the underlying Adonai-YHWH compound"). **The Layer-1 transparency is exemplary** — every compound verse carries a `key_decisions` entry naming `אֲדֹנָי יְהוִה` + the collapse rationale:

| Ref | Hebrew | Thai surface | Layer-1 `key_decisions`? |
|---|---|---|---|
| 7:18 | מִי אָנֹכִי **אֲדֹנָי יְהוִה** | `…“องค์พระผู้เป็นเจ้า ข้าพระองค์เป็นใคร…”` | ✓ + literary note (humility-formula cf. Gen 32:10, Exod 3:11, 1 Sam 18:18) |
| 7:19 (×2) | בְּעֵינֶיךָ **אֲדֹנָי יְהוִה** … תּוֹרַת הָאָדָם **אֲדֹנָי יְהוִה** | `…องค์พระผู้เป็นเจ้า … องค์พระผู้เป็นเจ้า?` | ✓ |
| 7:20 | יָדַעְתָּ אֶת־עַבְדְּךָ **אֲדֹנָי יְהוִה** | `…ข้ารับใช้ของพระองค์ องค์พระผู้เป็นเจ้า` | ✓ |
| 7:22 | עַל־כֵּן גָּדַלְתָּ **אֲדֹנָי יְהוִה** | `…พระองค์ยิ่งใหญ่ องค์พระผู้เป็นเจ้า` | ✓ |
| 7:28 | וְעַתָּה **אֲדֹנָי יְהוִה** אַתָּה־הוּא | `…องค์พระผู้เป็นเจ้า พระองค์ทรงเป็นพระเจ้า` | ✓ |
| 7:29 | כִּי־אַתָּה **אֲדֹנָי יְהוִה** דִּבַּרְתָּ | `…เพราะพระองค์ องค์พระผู้เป็นเจ้า ตรัส` | ✓ |

**Minor note (not a translation issue):** the 7:18 `key_decisions` summary states the compound "appears 6× (vv.18, 19 ×2, 20, 28, 29)" — it omits 7:22 from the enumeration. The actual count is **7** (7:22 is correctly rendered and carries its own `key_decisions` row). A one-character fix to the editorial note's count, not a surface change.

**REVIEW — the prayer-vocative `ข้าแต่` particle is absent.** The `divine_names_table_2026-05.md` lock table gives the compound's vocative sub-form as **`ข้าแต่องค์พระผู้เป็นเจ้า`** (anchor JOS 7:7, where `אֲהָהּ אֲדֹנָי יְהוִה` "Alas, Lord GOD!" is a sentence-initial interjection). 2 Sam 7:18–29 is a sustained prayer-vocative, yet renders the bare `องค์พระผู้เป็นเจ้า` (no `ข้าแต่`) at every occurrence. **This is defensible**: the 2 Sam 7 compounds are mid-sentence *appositional* address ("who am I, Lord GOD"; "you are great, Lord GOD"), where the Thai `ข้าแต่` sentence-initial vocative particle would read awkwardly — unlike JOS 7:7's sentence-initial interjection. But the principle (appositional compound-vocative omits `ข้าแต่`; interjection compound-vocative takes it) is **undocumented**. Recommend Ben confirm the principle and amend `divine_names_table_2026-05.md` to record it. **Severity: LOW.** Not blocking.

**LOCKED-with-§2-REVIEW** (forward-deferred 1SA §2 item resolves cleanly on vocabulary; only the vocative-particle principle wants documenting).

---

## 3. mal'akh — **LOCKED (human ผู้ส่งสาร; divine ทูตสวรรค์ at ch 24)**

**Human messengers → `ผู้ส่งสาร`** uniform: 3:26 (Joab's envoys recalling Abner), 5:11 (Hiram of Tyre's envoys), and the David/Absalom-war envoy clusters. **No `ผู้ส่งข่าว` drift** — 2SA ships the single form (resolving the 1SA §3 `ผู้ส่งสาร`/`ผู้ส่งข่าว` split in favor of the higher-count form).

**Divine mal'akh — the first since the 1SA gap.** The census-plague (ch 24) is the first divine-mal'akh narrative in the corpus since Joshua–Judges (1SA had zero). Renders per `malak_yhwh_2026-05.md` lock:
- 24:16 `הַמַּלְאָךְ` / `לַמַּלְאָךְ הַמַּשְׁחִית` (the destroying angel) → **`ทูตสวรรค์`** ✓
- 24:16 `מַלְאַךְ יְהוָה` → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** ✓
- 24:17 `הַמַּלְאָךְ הַמַּכֶּה בָעָם` → **`ทูตสวรรค์ที่ตีในประชาชน`** ✓

The head-noun `ทูตสวรรค์` is invariant; the qualifier carries the genitive — exactly the doc's prescription. The 24:17 verse additionally threads the David-as-shepherd-offering-himself typology to John 10:11 at Layer 1.

**LOCKED** ✓.

---

## 4. Spirit-of-YHWH at 23:2 — **LOCKED (the 1SA drift did NOT propagate)**

**This is the headline positive of the audit.** The 1SA audit §4 flagged a HIGHEST-severity book-wide drift: all 12 1 Samuel Spirit-occurrences shipped bare `วิญญาณ` (no `พระ` honorific), against the `spirit_of_yhwh_empowerment_2026-05.md` lock that explicitly forward-protects David. 1SA §4 listed **2 Sam 23:2** among the verses the unresolved drift could compound to.

**2 Sam 23:2 ships LOCK-COMPLIANT.** David's last words:

> `רוּחַ יְהוָה דִּבֶּר־בִּי וּמִלָּתוֹ עַל־לְשׁוֹנִי` → **`พระวิญญาณขององค์พระผู้เป็นเจ้าตรัสในข้า และพระวจนะของพระองค์อยู่บนลิ้นของข้า`**

The `พระ` honorific is **present** (`พระวิญญาณ`). This is a `דִּבֶּר`/declarative-class occurrence (Spirit *spoke through* me), not the `צָלַח`-rush empowerment class, so the locked `อย่างทรงพลัง` adverbial is correctly N/A. The `key_decisions` carries the 2 Pet 1:21 NT-inspiration cross-reference ("the basis of the doctrine of Scripture's inspiration").

**Other `רוּחַ` occurrences correctly disambiguated:** 22:11 `כַּנְפֵי־רוּחַ` (wings of the wind) → `ปีกของลม`; 22:16 `נִשְׁמַת רוּחַ אַפּוֹ` (breath of his nostrils) → `ลมหายใจของพระนาสิก`. The `วิญญาณ` Thai surfaces elsewhere (5:8, 13:39, 17:8) render `נֶפֶשׁ` "soul/life" (`จิตวิญญาณ`) — correct, not divine-Spirit.

**LOCKED** ✓. **Editorial significance:** 2 Samuel demonstrates the `spirit_of_yhwh_empowerment_2026-05.md` lock functioning as intended on the verse 1SA §4 specifically named as forward-at-risk. It also confirms the 1SA drift is **1SA-local** (a pre-lock drafting artifact), not a corpus-wide pattern — strengthening the 1SA §4 path-(a) "drafting predates the lock" diagnosis.

---

## 5. חַי־יְהוָה oath formula — **LOCKED**

The "as YHWH lives" oath renders uniformly **`องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่`**:

| Ref | Speaker | Thai surface |
|---|---|---|
| 4:9 | David (re: the Beerothite assassins) | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ ผู้ได้ทรงไถ่ชีวิตของข้า…` |
| 12:5 | David (Nathan's parable, self-condemning oath) | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ ชายผู้ที่ทำสิ่งนี้สมควรตาย` |
| 14:11 | David (oath to the Tekoite woman) | `…องค์พระผู้เป็นเจ้าพระเจ้าของท่าน…` (oath-by formula) |
| 15:21 | Ittai (compound: "as YHWH lives, and as my lord the king lives") | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ และเจ้านายของข้า กษัตริย์ ทรงพระชนม์อยู่` |
| 22:47 | David's song ("YHWH lives!") | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ และศิลาของข้าทรงได้รับการสรรเสริญ` |

**`חַי הָאֱלֹהִים` ("as God lives")** at 2:27 (Joab) → **`พระเจ้าทรงพระชนม์อยู่`** ✓ (the Elohim-variant correctly takes `พระเจ้า`). **Compound oaths** (`חַי־יְהוָה וְחֵי נַפְשְׁךָ`-type) at 14:19, 15:21 extend `ทรงพระชนม์อยู่` cleanly to both the divine and human "lives." Matches `hebrew_oath_formulas_2026-05.md` + the 1SA §8 lock.

**LOCKED** ✓.

---

## 6. חֶסֶד covenant-love — **LOCKED**

`חֶסֶד` is one of 2 Samuel's signature themes — the David-Jonathan covenant `חֶסֶד` extended to Mephibosheth (ch 9), the Jabesh-gilead loyalty (2:5), and the Hanun episode (ch 10). All render the doc-locked **`ความรักมั่นคง`** family per `chesed_covenant_love_2026-05.md`:

| Ref | Context | Thai surface |
|---|---|---|
| 2:5 | David blesses Jabesh-gilead for `חֶסֶד` to Saul | `ความรักมั่นคง` |
| 9:1 | "to whom I can show `חֶסֶד` for Jonathan's sake" | `ความรักมั่นคง` |
| 9:3 | `חֶסֶד אֱלֹהִים` ("the kindness of God") | `ความรักมั่นคงของพระเจ้า` |
| 9:7 | David to Mephibosheth | `ความรักมั่นคง` |
| 10:2 (×2) | David to Hanun, "as his father showed `חֶסֶד`" | `ความรักมั่นคง` |
| 16:17 | Absalom to Hushai ("is this your `חֶסֶד`?") | `ความรักมั่นคง` |

**LOCKED** ✓. The ch 9 David-Mephibosheth narrative — the climax of the David-Jonathan covenant-loyalty arc that 1SA established — ships uniformly.

---

## 7. נחם divine relenting (24:16) — **LOCKED**

`וַיִּנָּחֶם יְהוָה אֶל־הָרָעָה` (YHWH relented from the calamity) → **`องค์พระผู้เป็นเจ้าทรงเปลี่ยนพระทัยจากความหายนะ`** per `nicham_divine_relenting_2026-05.md`, with the Jer 18:7–10 cross-reference at Layer 1. This is the **exact verse 1SA §16 forward-protected** ("forward-protects 2 Sam 24:16 — the angel-of-pestilence נחם"). The relenting-from-judgment sense (change of planned course, cf. Jonah 3:10, Exod 32:14) correctly takes `ทรงเปลี่ยนพระทัย` rather than the anthropopathic-regret `ทรงเสียพระทัย` (1 Sam 15:11/35).

**LOCKED** ✓.

---

## 8. מָשִׁיחַ / anointing + Davidic royal register — **LOCKED**

**David's own anointings** render `מָשַׁח` → **`เจิม`** uniformly: 2:4 (anointed king over Judah), 5:3 (anointed king over Israel — `…และพวกเขาเจิมดาวิดเป็นกษัตริย์เหนืออิสราเอล`). The 1SA "do not touch YHWH's anointed" reverence-thread reaches its narrative payoff: David, the protected anointed of 1SA, is now the enthroned anointed.

**Royal Rachasap register for David-as-king** is pervasive and consistent, per `honorifics_non_divine_authorities_2026-04.md` + `ot_register_policy_2026-05.md`. The David-mourns-Absalom block (ch 19) is the densest deployment in the book: `กษัตริย์ทรงสะเทือนพระทัย` (19:1), `ทรงพระกันแสงและทรงไว้ทุกข์` (19:2), `ทรงคลุมพระพักตร์` (19:5), `เสด็จ` / `ประทับ` (19:9, 19:16). The "long live the king" acclamation at 16:16 (`ขอกษัตริย์ทรงพระชนม์ยืน`) and David-the-king verbs throughout use the royal register correctly. King-office actions of Saul's house, Absalom, and David all take `ทรง` per the Mark-6:14-Herod public-royal-role precedent.

**LOCKED** ✓.

---

## 9. "How the mighty have fallen" lament refrain — **LOCKED (uniform inclusio)**

David's lament over Saul and Jonathan (ch 1) turns on the threefold refrain `אֵיךְ נָפְלוּ גִבּוֹרִים`. **All three occurrences render uniformly** — a clean contrast to the 1SA §5 "Saul among the prophets" inclusio that drifted:

| Ref | Thai surface |
|---|---|
| 1:19 | `…ผู้ยิ่งใหญ่ทั้งหลายล้มลงเสียแล้ว!` |
| 1:25 | `ผู้ยิ่งใหญ่ทั้งหลายล้มลงเสียแล้วในกลางการรบ!` |
| 1:27 | `ผู้ยิ่งใหญ่ทั้งหลายล้มลงเสียแล้ว! และอาวุธของสงครามถูกทำลาย!` |

The signature literary refrain of one of the OT's most famous laments ships with verbatim consistency. **LOCKED** ✓.

---

## 10. Warfare ethics — **LOCKED (12:31 Rabbah forced-labor reading flagged REVIEW)**

2 Samuel's warfare narratives (ch 8 Davidic conquests, ch 10 Ammon-Aram, ch 12 Rabbah) carry no `חרם` (ḥerem) cluster — the ban is concentrated in Joshua/1 Sam 15. `ot_warfare_ethics_2026-05.md` is therefore largely N/A for the ban-lemma, with one crux:

**12:31 Rabbah** (`וַיָּשֶׂם בַּמְּגֵרָה…וְהֶעֱבִיר אוֹתָם בַּמַּלְבֵּן`) is rendered as **forced labor**: `…ตั้งให้พวกเขาที่เลื่อย และที่ลานเหล็ก และที่ขวานเหล็ก และนำพวกเขาผ่านเตาเผาอิฐ` ("set them to saws, iron picks, axes; brought them through the brick-kilns"). This takes the labor reading (`מַלְבֵּן` = brick-mold/kiln) over the older "tortured them with saws / made them pass through the brick-fire (Molech)" reading — matching modern scholarship and the BSB. **Defensible**, and the milder reading avoids importing a torture-narrative the Hebrew does not require. **REVIEW** (LOW): confirm the labor interpretation is the intended one; optionally a Layer-1 note recording the crux. Not blocking.

---

## 11. "until this day" leitwort — **LOCKED-internal; cross-book REVIEW (carries 1SA §14)**

`עַד הַיּוֹם הַזֶּה` renders uniformly **`จนถึงวันนี้`** in 2SA: 4:3 (Beerothites in Gittaim), 6:8 (Perez-uzzah), 7:6 (YHWH's tent-dwelling since the Exodus), 18:18 (Absalom's monument), and others. **Internally uniform** ✓.

**Cross-book question (unchanged from 1SA §14).** 2SA continues the 1SA bare-form `จนถึงวันนี้`, **not** the JDG-majority `จนถึงทุกวันนี้`. The corpus now has two Former-Prophets books (1SA + 2SA) on `จนถึงวันนี้` and JDG on `จนถึงทุกวันนี้`. The Hebrew is identical at every occurrence; `leitwort_handling_policy_2026-05.md` does not yet lock a canonical Thai surface. **REVIEW** (LOW): the corpus-wide normalization decision (deferred in 1SA §14) should land before more Former-Prophets ship. 2SA reinforces the case that `จนถึงวันนี้` is the de-facto majority (1SA + 2SA vs JDG alone).

---

## 12. Davidic-covenant Christology thread (2 Sam 7:12–16) — **STABLE; recommend new doc**

2 Sam 7:12–16 (the Davidic covenant) is the single most load-bearing OT messianic-kingship text — the seedbed of "Son of David" Christology. The shipped translation threads it well at Layer 1:

| Ref | Thai surface | Layer-1 NT cross-reference |
|---|---|---|
| 7:12 | `…เราจะตั้งเชื้อสายของเจ้าหลังจากเจ้า` | (seed/offspring → Acts 2:30, 13:23) |
| 7:13 | `…เราจะสถาปนาบัลลังก์ของราชอาณาจักรของเขาตลอดไป` | Solomon near-fulfillment (1 Kgs 5–8) + Christ far-fulfillment |
| 7:14 | `เราจะเป็นบิดาของเขา และเขาจะเป็นบุตรของเรา` | **Heb 1:5 cites this verse for Jesus** (explicit at Layer 1) |
| 7:16 | `…บัลลังก์ของเจ้าจะถูกสถาปนาตลอดไป` | `עוֹלָם` ×3 (vv.13,16) eternal-permanence note |

**Recommend new doc** `docs/translator_decisions/davidic_covenant_christology_thread_2026-05.md`:
1. Lock the 2 Sam 7:12–16 → NT messianic-kingship reading (Luke 1:32–33 "the throne of his father David"; Acts 2:30; Acts 13:22–23; Heb 1:5; Rev 22:16 "the Root and Offspring of David").
2. Cross-reference the Davidic-`חֶסֶד`-will-not-depart clause (7:15) to Ps 89 (the covenant-crisis lament) and Isa 55:3 ("the sure mercies of David," cited Acts 13:34).
3. Lock the "house/throne/kingdom forever" (`בַּיִת`/`כִּסֵּא`/`מַמְלָכָה` + `עוֹלָם`) cluster for forward-consistency with 1 Kgs 8, 1 Chr 17 (the Chronicles parallel), and the NT Davidic-throne citations.

**Priority: MEDIUM** — the NT side is already shipped; this closes a loop and forward-protects the 1 Chr 17 synoptic parallel + Kings. Analogous to the 1SA-audit-recommended Hannah-Magnificat thread doc (§7 / §J of that audit).

---

## 13. Textual-variant Tier-2 reader-footer gap — **DECIDE before tagging**

2 Samuel is the corpus's **first book with a full Samuel↔Chronicles synoptic partner** (1 Chr 11–21 ≈ 2 Sam 5–24), and it carries several of the OT's most-discussed cruxes. **The good news: every one is documented at Layer 1** (`key_decisions`/`notes`) — a material improvement over 1SA, whose §17 found the variants shipped *silent*. **The gap: none is lifted to the Layer-2 reader-facing chapter-footer** (`output/textual_variants/2samuel_NN.json` carries only the YHWH first-occurrence footnote — confirmed across all 24 files).

| Ref | Crux | Shipped Thai (MT-faithful unless noted) | Layer-1 doc'd? | Layer-2 footer? |
|---|---|---|---|---|
| **15:7** | MT `אַרְבָּעִים` (**forty** years) vs LXX/Syr/Vulg/Josephus + some MT mss "**four**" | **`สี่ปี`** (four — *departs* from MT) | ✓ thorough `key_decisions` | ❌ **required by policy, absent** |
| **24:1** | MT "**YHWH** incited David" vs 1 Chr 21:1 "**Satan** incited David" | `พระองค์ทรงยุยงดาวิด` (MT) | ✓ + Job 1–2 / 1 Kgs 22:19–22 framework | ❌ |
| **24:9** | census: MT 800k Israel / 500k Judah vs 1 Chr 21:5 (1.1M / 470k) | `แปดแสน / ห้าแสน` (MT) | partial | ❌ |
| **24:13** | MT "**seven** years" famine vs LXX/1 Chr 21:12 "**three**" | `เจ็ดปี` (MT) | ✓ `key_decisions` + `notes` | ❌ |
| **21:19** | MT "Elhanan killed **Goliath** the Gittite" vs 1 Chr 20:5 "Lahmi the **brother of** Goliath" | `…ได้ตีโกลิอัทชาวกัท` (MT — note: the Thai is *more* MT-faithful than the BSB English, which harmonizes to "the brother of") | not flagged | ❌ |

**Why this is DECIDE, not just REVIEW.** The canon policy `ot_canon_and_text_base_2026-05.md` §"When to depart from MT" specifies four exception triggers, and for **Trigger 1 (obvious copyist error preserved by MT)** it states: *"the divergence is recorded in the verse's `key_decisions` field **plus a `[Tier 2] verse-level footer note`** per RULES.md §5b."* **15:7 is a Trigger-1 departure** (the translator emended MT "forty" → "four"), so the Tier-2 footer is **mandatory** — and it is **absent**. As shipped, 15:7 is policy-noncompliant on the transparency requirement. This must be resolved before `book-2samuel-v1`.

**Recommended path** (parallels the 1SA §17 recommendation, still pending Ben):
1. Add Tier-2 chapter-footer entries (`type: "textual_variant"`) in `output/textual_variants/2samuel_{15,21,24}.json` for the five cruxes above — summarizing the MT reading, the alternative witness (LXX / 1 Chr / Qumran), and the project's disposition.
2. **15:7** specifically requires its footer (Trigger-1 mandate). The 24:1 YHWH/Satan and 21:19 Elhanan-Goliath cruxes are theologically/apologetically prominent enough that the reader-facing footer is high-value even though they preserve MT.
3. No translation-surface edits required for 24:1 / 24:9 / 24:13 / 21:19 (MT correctly followed). Only the Layer-2 transparency layer is missing.

**Cost:** 3 chapter-footer JSON entries (~30 min each; the scholarly content already exists at Layer 1 and can be lifted). **Severity: HIGH (DECIDE).** Gates the Samuel↔Chronicles synoptic-disclosure precedent for 1–2 Kings (LXX Old Greek), Jeremiah (the MT-vs-LXX shorter recension), Daniel, and the entire Chronicles synoptic. Blocks `book-2samuel-v1` without resolution.

### 13b. Sub-question (REVIEW): does 15:7 clear the Trigger-1 bar?

Trigger 1 requires MT to be "grammatically impossible, semantically nonsensical, or contradicts itself within a few verses." MT "forty years" for Absalom's pre-revolt interval is *historically awkward* (40 ≈ David's whole reign) but is not strictly "grammatically impossible" — it is the *lectio difficilior* with strong external support for the easier "four." The 15:7 `key_decisions` itself concedes "the project is normally MT-anchored — but in cases of clear scribal error, some editions choose the sensible reading." **REVIEW:** confirm (a) that 15:7 clears the Trigger-1 "nonsensical" threshold (vs. preserving MT "forty" + footer, the more conservative MT-base path), and (b) whether the policy doc should record 15:7 as the worked example of a Trigger-1 emendation (it currently cites only 1 Sam 13:1). Note the apparent — but ultimately principled — contrast with **24:13**, where MT "seven" is *preserved* against LXX/1 Chr "three": 24:13's MT reading is unusual but coherent (not "nonsensical"), so Trigger 1 does not fire and MT-preservation is the default. Documenting why 15:7 emends while 24:13 preserves would forestall the "inconsistent MT policy" critique.

---

## 14. Synoptic / parallel-passage handling (2 Sam 22 ≈ Ps 18; Samuel ↔ Chronicles) — **STABLE; recommend new doc (HIGH)**

2 Samuel introduces two parallel-passage relationships the corpus has not yet had to govern:

**(a) 2 Sam 22 ≈ Psalm 18.** David's song of deliverance appears near-verbatim in both the Davidic appendix and the Psalter. The shipped ch 22 handles it **well**: the chapter-overview `textual_variants` footer states `บทที่ 22 = สดด 18 — เพลงเดียวกันปรากฏใน 2 เล่ม (Davidic appendix … + Psalter)` and even flags the v.51 `magdol`(2 Sam)/`magdil`(Ps) variant; per-verse `notes` carry the Ps-18 verse-correspondence (e.g., 22:3 → Ps 18:2) and the NT echoes (22:50 → **Rom 15:9** cited directly; 22:28 → Magnificat Luke 1:51–52). Excellent Layer-1+2 work.

**(b) Samuel ↔ Chronicles.** 1 Chr 11–21 retells 2 Sam 5–24; the §13 cruxes (24:1, 24:9, 24:13, 21:19) are all Samuel↔Chronicles synoptic differences, handled at Layer 1.

**The gap:** there is **no corpus doc** locking the parallel-passage policy — i.e., when the *same* text appears in two books, which Thai surface governs, how variants between the parallels are disclosed, and how the reader is pointed to the partner passage. `decalogue_parallel_text_2026-05.md` exists for the Exod 20 // Deut 5 Decalogue but does not generalize.

**Recommend new doc** `docs/translator_decisions/synoptic_parallel_passages_2026-05.md`:
1. Lock the principle: each parallel passage is translated **independently from its own MT context** (so 2 Sam 22 follows 2 Sam 22's MT, Ps 18 will follow Ps 18's MT), with cross-reference notes and inter-parallel variants disclosed at Layer 1 + (where significant) Layer 2.
2. Lock the 2 Sam 22 ≈ Ps 18 correspondence + the `magdol`/`magdil` and other minor variants, so the Psalter ships consistent when Ps 18 is reached.
3. Lock the Samuel↔Chronicles synoptic-disclosure policy (ties directly to §13): which cruxes get Tier-2 footers, and the standard footer phrasing for "1 พศด อ่าน …".
4. Forward-protects: Ps 14//53, Ps 40:13–17//70, Ps 108 (=57:7–11 + 60:5–12), 2 Sam 22//Ps 18, 2 Kgs 18:13–20:19//Isa 36–39, 2 Kgs 24:18–25:30//Jer 52, and the entire 1–2 Chronicles synoptic.

**Priority: HIGH** — gates the Psalter *and* Chronicles, both major forthcoming books, and consolidates the §13 disclosure policy.

---

## 15. Annotation-architecture pattern — **REVIEW (coverage variance)**

Per-chapter `thai_summary` coverage:

| ch | verses | summary % | | ch | verses | summary % |
|---|---|---|---|---|---|---|
| 1 | 27 | 70% | | 13 | 39 | **46%** |
| 2 | 32 | **43%** | | 14 | 33 | 54% |
| 3 | 39 | **46%** | | 15 | 37 | 59% |
| 4 | 12 | 66% | | 16 | 23 | 60% |
| 5 | 25 | 60% | | 17 | 29 | 75% |
| 6 | 23 | 69% | | 18 | 32 | **96%** |
| 7 | 29 | 55% | | 19 | 44 | 79% |
| 8 | 18 | 55% | | 20 | 26 | 80% |
| 9 | 13 | 53% | | 21 | 22 | 81% |
| 10 | 19 | 68% | | 22 | 51 | **49%** |
| 11 | 27 | 62% | | 23 | 39 | 53% |
| 12 | 31 | 64% | | 24 | 25 | 68% |

**Pattern.** Unlike 1SA's sharp ch-12 inflection (100% → ~40%), 2SA's coverage is **more uniform but mid-band** (43–96%, no chapter at 100%). The lowest chapters are ch 2 (43%) + ch 3 (46%) + ch 13 (46%) — the Ish-bosheth/Abner political-maneuvering and the Amnon-Tamar chapters — and ch 22 (49%, the 51-verse Psalm-18 song, which is `notes`-heavy instead). The highest is ch 18 (96%, Absalom's death) and the chs 17–21 climax cluster (75–96%). **Note density** rises sharply in chs 17–24 (8–15 `notes`/chapter vs 1–6 earlier), consistent with the theologically dense appendix.

**REVIEW** (LOW): confirm the coverage variance is intentional editorial scaling (action/political-narrative chapters → sparser per-verse summary, theological-climax chapters → fuller). If unintentional, the candidates for backfill are ch 2, 3, 13, 22. **Not blocking.**

---

## 16. Surface copy-edit — **REVIEW (22:11 doubled `ทรง`)**

**22:11** ships **`พระองค์ทรงทรงเครูบและบินไป`** — a doubled `ทรง` (royal-honorific prefix repeated). The Hebrew `וַיִּרְכַּב עַל־כְּרוּב` ("he rode upon a cherub") should render `พระองค์ทรงเครูบ` (`ทรง` + vehicle = royal "rode"). This is a **copy-edit typo**, not a translation decision — it is the only `ทรงทรง` occurrence in 2SA. It passed all automated checks because no script catches doubled-word artifacts. **REVIEW** (trivial fix; flagging because it sits inside the high-visibility Psalm-18 song-text). Recommend a doubled-word lint be added to the per-chapter check suite (corpus-wide value).

---

## 17. Inherited corpus locks — **all compliant except where flagged**

| Doc | 2SA evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1, §2. YHWH 152 surfaces / 0 residue; Tsebaoth + YHWH-Elohim differentiated; Adonai-YHWH ×7 collapse with exemplary Layer-1. **EXCEPTION:** prayer-vocative `ข้าแต่`-omission (7:18–29) — defensible, undocumented (§2). | **LOCKED-with-§2-REVIEW** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §4. 23:2 `พระวิญญาณขององค์พระผู้เป็นเจ้า` — `พระ` honorific present. The 1SA drift did NOT propagate. | **LOCKED** |
| `malak_yhwh_2026-05.md` | §3. Human → `ผู้ส่งสาร` uniform; divine (ch 24) → `ทูตสวรรค์` / `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`. First divine-mal'akh since 1SA gap; compliant. | **LOCKED** |
| `nicham_divine_relenting_2026-05.md` | §7. 24:16 `ทรงเปลี่ยนพระทัย` + Jer 18 cross-ref. The verse 1SA §16 forward-protected. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | §6. `ความรักมั่นคง` uniform (David-Mephibosheth ch 9, Jabesh 2:5, Hanun 10:2). | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | §5. `חַי־יְהוָה` ×5 + `חַי הָאֱלֹהִים` 2:27 + compound oaths — uniform. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | §8. Royal Rachasap register for David-as-king pervasive (ch 19 mourning block densest). | **LOCKED** |
| `ot_register_policy_2026-05.md` | Royal `ทรง` for YHWH-volitional + king-office; plain for character speech. David's penitential speech (12:13) + Nathan parable (12:1–7) plain-register. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator-omniscient; character speech plain. Compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Hand of YHWH" 24:14 (`พระหัตถ์`); "anger of YHWH kindled" 6:7, 24:1 (`พระพิโรธ…เดือดดาล`); Uzzah-strike 6:7. Uniform. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol chains pervasive; ch 22 poetry preserves parallelism + hapax flags (`חַשְׁרָה` 22:12; `מִגְדּוֹל` 22:51). Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "Hand of YHWH" (above); "until this day" leitwort §11; "uncircumcised Philistines" 1:20 (`คนที่ไม่ได้รับสุหนัต`). Compliant. | **LOCKED-with-§11-flag** |
| `ot_canon_and_text_base_2026-05.md` | §13. MT-base correctly followed at 24:1/24:9/24:13/21:19; **15:7 Trigger-1 emendation present but missing the policy-required Tier-2 footer**. | **DECIDE-§13** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | §13. Significant cruxes documented at Layer 1; Tier-2 reader-footer infrastructure deployed (24/24 files) but underutilized for the actual variant cluster. | **DECIDE-§13** |
| `inclusion_variants_absent_verses_2026-04.md` | `audit_inclusion_variants.py --book 2samuel --strict` = 0 candidates / exit 0. (No SBLGNT-style omissions; the OT-side cruxes are MT/Chr/LXX recensional, caught at Layer 1 — see §13.) | **DECIDE-§13** |
| `decalogue_parallel_text_2026-05.md` | §14. Does not generalize to 2 Sam 22//Ps 18 or Samuel↔Chronicles — recommend new `synoptic_parallel_passages` doc. | **STABLE-§14-new-doc** |
| `leitwort_handling_policy_2026-05.md` | §11. `จนถึงวันนี้` uniform within 2SA; cross-book vs JDG `จนถึงทุกวันนี้` unresolved (carries 1SA §14). | **LOCKED-with-§11-cross-book-REVIEW** |
| `proper_names_and_transliteration_2026-05.md` | ~50 names spot-checked: ดาวิด, โยอาบ, อับเนอร์, อิชโบเชท, เมฟีโบเชท, อับซาโลม, อาหิโธเฟล, ฮูชัย, นาธาน, อุรียาห์, บัทเชบา, โยนาดับ, อัมโนน, ทามาร์, ชิเมอี, ชีบา, อมาสา, บารซิลลัย, อิททัย, ฟิลิสเตีย, อัมโมน, อารัม, ราฟา/Rephaim, อาราวนาห์. No spelling drift surfaced (contrast 1SA §12 Ashtaroth). | **LOCKED** |
| `proper_noun_wordplay_2026-05.md` | Place-etymologies preserved: Perez-uzzah 6:8 (`เปเรซ-อุสซาห์` + breach note), Baal-perazim 5:20 (`บาอัล-เปราซีม` + "bursting" wordplay), Nathan's "Jedidiah" 12:25. Compliant. | **LOCKED** |
| `pagan_deities_2026-04.md` / `ot_polytheistic_register_2026-05.md` | Philistine idols 5:21 → `รูปเคารพ`; no foreign-deity-as-`พระเจ้า` violation (contrast 1SA §12 Dagon-5:7). 12:30 `מַלְכָּם` rendered "their king" (vs Milcom-deity) — defensible MT vocalization. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | Ch 22 song: 22:4 `เรียก…ผู้สมควรแก่การสรรเสริญ`; 22:47 `ศิลาของข้าทรงได้รับการสรรเสริญ`. Compliant. | **LOCKED** |
| `shared_names_normalization_2026-05.md` | Tribal/place names match prior locks (Judah, Benjamin, Israel, Hebron, เยรูซาเล็ม, จอร์แดน). Compliant. | **LOCKED** |
| `sacrificial_vocabulary_2026-05.md` | `עוֹלָה`/`שְׁלָמִים` at 6:17–18 (ark-installation) + 24:25 (Araunah's altar) → `เครื่องเผาบูชา` / `เครื่องสันติบูชา`. Spot-check uniform (no 1SA §15-style drift surfaced). | **LOCKED** |
| `hebrew_idioms_and_metaphor` / `goel` / `kapporet` / `kareth` / `manah` / `i_am_yhwh` / `paqad` | `goel` blood-avenger 14:11 (`ผู้แก้แค้นเลือด`) ✓; the priestly-cult lemmas (kapporet/kareth/manah/i-am-YHWH) do not occur in 2SA narrative. | **LOCKED (mostly N/A)** |

---

## 18. NT cross-corpus echoes from 2 Samuel — **STABLE**

| 2SA ref | NT echo | Surface check |
|---|---|---|
| 7:12–16 (Davidic covenant) | Luke 1:32–33; Acts 2:30; **Heb 1:5** (7:14); Rev 22:16 | Heb 1:5 cited at Layer 1 (§12); recommend new thread doc |
| 7:14 ("I will be his father…") | Heb 1:5; 2 Cor 6:18 | ✓ Layer-1 |
| 22:3 / 22:50 (David's song) | **Rom 15:9** (22:50 cited directly by Paul) | ✓ Layer-1 notes |
| 22:28 ("you save the humble…") | Luke 1:51–52 (Magnificat) | ✓ Layer-1 note ("David's song is the root of Mary's song") |
| 22:31 ("the word of God is flawless") | Prov 30:5 | ✓ Layer-1 |
| 23:2 (Spirit spoke through me) | **2 Pet 1:21** (inspiration) | ✓ Layer-1 (§4) |
| 24:16–17 (David offers self for the people) | John 10:11 (good-shepherd) | ✓ Layer-1 typology note |
| 24:18–25 (Araunah's threshing-floor → Temple site) | (1 Chr 21:18–22:1; Calvary typology) | ✓ Layer-1 note (atonement-site typology) |

**STABLE.** The NT-echo annotation is rich and accurate; the §12 + §14 new docs would consolidate the threads. **Not blocking.**

---

## 19. Mechanical (§1) — **all green**

- 24/24 chapters: `output/check_reports/2samuel_NN_review.md` — all `✅ Ready to ship` ✓
- 24/24 chapters: `output/back_translations/2samuel_NN.json` ✓
- 24/24 chapters: `output/translations/2samuel_NN.json` ✓
- 24/24 chapters: `output/textual_variants/2samuel_NN.json` ✓ (YHWH-footnote / chapter-overview infrastructure deployed; inclusion-variant Tier-2 gap flagged §13)
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings**
- `check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `check_divine_names.py --all`: **0 hard fails**; 162 corpus [C-soft] warnings (~36 in 2SA — all human-addressee `אֲדֹנִי` "my lord": David to Joab, servants to David-as-king, Tekoite woman, Ziba, Mephibosheth, etc.; all expected per category, see §2)
- `audit_inclusion_variants.py --book 2samuel --strict`: **0 candidates, exit 0**
- YHWH `องค์พระผู้เป็นเจ้า`: **152**; `ยาห์เวห์` residues in verse text: **0**
- `git status output/`: clean except the transient `output/check_reports/divine_names.md` (a single-/all-chapter report regenerated on each ship + by this audit's `--report` run; report-only, not a translation surface — restored to HEAD by this audit). Not a gate failure (Hard fails: 0).

**Severity: GREEN.**

---

## 20. Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1 YHWH, §2 Elohim/Adonai-compound, §3 mal'akh, §4 Spirit-23:2, §5 oath, §6 chesed, §7 nicham, §8 mashiach/royal-register, §9 lament-refrain, §10 warfare-base, §19 mechanical) + inherited-lock table (§17)
- **STABLE (recommend new doc):** 2 items (§14 synoptic/parallel-passage — HIGH; §12 Davidic-covenant Christology thread — MEDIUM); + §18 NT-echo (STABLE, no doc)
- **REVIEW:** 6 items (§2 Adonai-YHWH prayer-vocative `ข้าแต่`; §13b 15:7 four/forty Trigger-1 confirmation; §11 cross-book "until this day"; §16 22:11 doubled-`ทรง` copy-edit; §15 annotation-coverage variance; §10 12:31 Rabbah forced-labor reading)
- **DECIDE:** 1 item (§13 textual-variant Tier-2 reader-footer gap — HIGH; inherits/parallels 1SA §17)

**1 DECIDE item blocks the `book-2samuel-v1` tag** (§13).

**2 new translator_decisions docs recommended:** `synoptic_parallel_passages_2026-05.md` (HIGH — gates Psalter + Chronicles + Kings//Isa//Jer), `davidic_covenant_christology_thread_2026-05.md` (MEDIUM).

**Existing docs to amend:**
- `divine_names_table_2026-05.md` — record the appositional-vs-interjection compound-vocative `ข้าแต่` principle (§2); cite 2 Sam 7:18–29 as the densest compound-Adonai prayer exemplar.
- `ot_canon_and_text_base_2026-05.md` — add 15:7 (and the 2 Sam 24 cruxes) as worked Trigger-1 / MT-preservation examples; clarify the Tier-2-footer mandate (§13).
- `leitwort_handling_policy_2026-05.md` — lock the canonical "until this day" surface (`จนถึงวันนี้` now 2:1 over JDG) — carries 1SA §14 (§11).

---

## 21. Recommendation

**2 Samuel ships in strong corpus-hygiene shape — notably stronger than 1 Samuel.** It is the fourth Former-Prophets book and the first downstream test of four 1SA-deferred items, **all of which pass**:

- The **Spirit-of-YHWH lock holds at 23:2** (`พระวิญญาณ` with the `พระ` honorific) — the precise verse the unresolved 1SA §4 drift threatened. This confirms the 1SA drift is a 1SA-local pre-lock drafting artifact, not a corpus pattern.
- The **Adonai-YHWH compound prayer (7:18–29)** — the corpus's densest, the verse-block JDG §8 / 1SA §2 forward-deferred — ships uniform with exemplary Layer-1 transparency.
- The **divine-mal'akh lock holds at ch 24** (first divine-mal'akh since the 1SA gap).
- The **nicham lock holds at 24:16** (the exact verse 1SA §16 forward-protected).

The chesed, oath, royal register, lament-refrain, divine-anthropomorphism, proper-noun, and pagan-deity locks all carry cleanly (no Ashtaroth-style spelling drift, no Dagon-as-`พระเจ้า` violation). The Davidic-covenant Christology (2 Sam 7) and the 2 Sam 22 // Ps 18 song are richly and accurately annotated.

**1 DECIDE item** must resolve before tagging `book-2samuel-v1`:

1. **§13 — Textual-variant Tier-2 reader-footer gap.** The major MT cruxes (15:7 forty/four, 24:1 YHWH/Satan, 24:9 census, 24:13 seven/three, 21:19 Elhanan-Goliath) are well-documented at Layer 1 but not lifted to the reader-facing Layer-2 chapter-footers; 15:7 in particular is a Trigger-1 MT-departure whose Tier-2 footer is **mandated by policy** and currently absent. Cost: 3 chapter-footer JSON entries (content already exists at Layer 1). Gates the Samuel↔Chronicles synoptic-disclosure precedent for Kings + Jeremiah + Daniel + the whole Chronicles parallel.

The 2 STABLE-but-undocumented items should be lifted to corpus docs — `synoptic_parallel_passages_2026-05.md` is the higher priority (it consolidates the §13 disclosure policy *and* forward-protects the Psalter + Chronicles, both major forthcoming books).

Tag `book-2samuel-v1` after:
1. Ben's decision on **§13** (DECIDE: textual-variant Tier-2 footers; 15:7 Trigger-1 confirmation).
2. Ben's confirmation on the **6 REVIEW items** (§2 prayer-vocative, §13b 15:7, §11 cross-book leitwort, §16 22:11 typo, §15 coverage, §10 Rabbah).
3. The 2 new translator_decisions docs written (§14 synoptic-parallel — HIGH; §12 Davidic-covenant thread — MEDIUM).
4. External AI sanity-check (§3).

**Forward note:** writing `synoptic_parallel_passages_2026-05.md` and settling the §13 Tier-2-disclosure policy before 1–2 Kings + Chronicles ship is the load-bearing forward-protection step from this audit — 2 Samuel is the corpus's first full Samuel↔Chronicles synoptic partner, and the disclosure precedent set here governs every parallel passage downstream.
