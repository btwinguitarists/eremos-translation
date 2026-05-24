## Item A — mal'akh-YHWH lock drift at 1 Kgs 19:7 (drift against a forward-protective lock)

**The pattern:** A locked corpus doc (`docs/translator_decisions/malak_yhwh_2026-05.md`, finalized 2026-05-13 via tri-AI review) requires every divine מַלְאָךְ to render as **`ทูตสวรรค์`** ("heaven-messenger"), with the genitive qualifier carried by `ของ` + the established divine-name form — so מַלְאַךְ יְהוָה → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`**. The lock's §3 implementation checklist explicitly names **"1 Kings 19 (Elijah at Horeb)"** as a forward-cover target. The lock exists precisely to eliminate the bare-`ทูต` drift (its §2.3 records the Exod 3:2 pre-fix `ทูตขององค์พระผู้เป็นเจ้า` → fixed `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`).

**1 Kings has three divine-mal'akh occurrences; one drifts:**

| Ref | Hebrew | Thai (shipped) | Locked Thai | Status |
|---|---|---|---|---|
| **19:5** | מַלְאָךְ (standalone — "an angel touched him") | `มีทูตสวรรค์องค์หนึ่งมาแตะตัวเขา` | `ทูตสวรรค์` | ✓ |
| **19:7** | **מַלְאַךְ יְהוָה** ("the angel of YHWH returned a second time") | **`ทูตขององค์พระผู้เป็นเจ้ากลับมา`** | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✗ **DRIFT** |
| **13:18** | מַלְאָךְ (the old prophet's claimed angel) | `มีทูตสวรรค์องค์หนึ่งบอกข้า` | `ทูตสวรรค์` | ✓ |

**Sample verses:**
- **19:5 HEB:** `וְהִנֵּה־זֶה מַלְאָךְ נֹגֵעַ בּוֹ` → **TH:** "ทันใดนั้นมี**ทูตสวรรค์**องค์หนึ่งมาแตะตัวเขา"
- **19:7 HEB:** `וַיָּשָׁב מַלְאַךְ יְהוָה שֵׁנִית` → **TH (shipped):** "**ทูต**ขององค์พระผู้เป็นเจ้ากลับมาแตะตัวเขาเป็นครั้งที่สอง"
- **Recommended fix:** "**ทูตสวรรค์**ขององค์พระผู้เป็นเจ้ากลับมา…"

**Editorial context:** 19:5 and 19:7 narrate the *same* angel feeding Elijah under the broom tree — so the drift is both a lock violation and an internal inconsistency within a single pericope (19:5 has `ทูตสวรรค์`, 19:7 drops `สวรรค์`). The drift was not caught by `check_key_term_consistency.py` because the malak_yhwh binding-check (a planned `check_phrase_consistency.py` extension, per the lock's §3 checklist) is not yet implemented. This is the **second OT-corpus drift discovered against an explicitly-forward-protective lock that named the affected book** (after 1SA §4 Spirit-of-YHWH), though unlike 1SA's 12-verse drift this is a single surgical edit.

**Forward-compounds to:** 2 Kgs 1:3,15 (the angel of YHWH to Elijah re: Ahaziah's messengers — the next divine-mal'akh narrative), Zech 1–6 (the angel-of-YHWH night-vision cycle), Malachi (the book whose Hebrew title *is* מַלְאָכִי).

**Question:** Should the project ship a single-verse revision (`revision/malak-yhwh-1ki-19-2026-05`) normalizing 19:7 to `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` per the lock, then tick "1 Kings 19" on the `malak_yhwh_2026-05.md` §3 forward-cover checklist? (The fix is mechanically unambiguous — the lock leaves no discretion for the divine compound מַלְאַךְ יְהוָה — so this is really a confirm-and-ship rather than an open editorial choice. Is there any reading under which the bare `ทูต` at 19:7 is defensible — e.g., as a stylistic variation within a single narrative — that would argue against normalization?)

---

## Item B — MT/LXX (3 Reigns) inclusion-variant gap (largest LXX divergence in the corpus to date)

**The pattern:** Per `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md`, every MT-vs-LXX divergence with corpus-significance should be explicitly dispositioned (Tier 1 phrase brackets / Tier 2 chapter-footer file / Tier 3 ⟦double brackets⟧). The 1SA audit (§17) flagged this as a **DECIDE** for the first major OT inclusion-variant cluster; the same gap recurs in 1 Kings — and **1 Kings is the corpus's largest MT-vs-LXX divergence to date.** The `output/textual_variants/1kings_NN.json` files contain only the Tier-2 YHWH footnote (21 chapters) + one versification note (ch 22:44); **zero** entries disposition the LXX 3 Reigns divergences:

| Divergence | Description |
|---|---|
| **LXX 3 Reigns Solomon-narrative reordering** | The Greek 3 Reigns substantially reorders the Solomon material (chs 2–11) relative to the MT sequence. |
| **The two "Miscellanies"** | 3 Rgns 2:35a–o + 2:46a–l — large supplementary blocks of Solomon material with no MT counterpart (drawn partly from material MT places elsewhere). |
| **Alternate Jeroboam narrative** | 3 Rgns 12:24a–z — a parallel, divergent account of Jeroboam's rise, distinct from the MT account in chs 11–14. |
| **MT 20↔21 / LXX 21↔20 chapter swap** | LXX places the Naboth's-vineyard chapter (MT 21) *before* the Ben-Hadad / Aram-war chapter (MT 20). |

**Editorial context:** The shipped 1 Kings text follows MT throughout — defensible and matching `ot_canon_and_text_base_2026-05.md`'s MT-base policy. The Tier-2 *infrastructure* is deployed (21/21 chapters have textual_variants files), but it carries only the YHWH footnote; the **transparency layer for the textual divergences is missing**, exactly as in 1SA. (Versification divergences, by contrast, ARE handled: 1 Kings 5 = MT 5 / English 4:21–5:18 is documented in `versification_map.json` + a reader note folded into `1kings_05.json`; 1 Kings 22:43/44 carries a dedicated `versification_divergence_mt_vs_english` entry.)

**This sets the precedent** for 2 Kings (LXX Old Greek + the kaige recension), Jeremiah (the famous shorter LXX — MT is ~1/8 longer, with reordered oracles-against-the-nations), and Daniel (the Greek additions).

**Two questions:**
1. The audit recommends ~4 Tier-2 chapter-footer JSON entries documenting the MT-base decision + summarizing the major 3 Reigns divergences (minimally: a ch-2/ch-11 footer for the Solomon reordering + the two Miscellanies; a ch-12 footer for the alternate Jeroboam narrative; a ch-20/21 footer for the LXX chapter-order swap). Is chapter-footer Tier-2 the right disclosure level for the CC0 Thai Bible's audience (Thai evangelical + theological reviewer) — or are the 3 Reigns divergences (which involve *reordering* and *large pluses*, not just verse-level minuses) better served by a single book-level prefatory note explaining that 1 Kings follows MT and that the Greek 3 Reigns presents the Solomon/Jeroboam material in a substantially different order and shape?
2. The LXX divergences in 1 Kings are primarily *structural* (reordering + supplementary blocks) rather than the verse-level *minus/plus* pattern the Tier-1/2/3 scheme was designed around (e.g., the John 5:4 / Romans doxology cases). Does the existing tiered-disposition framework need an explicit fourth category for **macro-structural** MT/LXX divergence (whole-narrative reordering, alternate parallel accounts), or can it be adequately captured by a chapter-footer that points to the structural difference without enumerating every shifted verse?

---

## Item C — Deuteronomistic regnal-cycle formulas: recommend a new corpus doc before 2 Kings

**The pattern:** 1 Kings is the corpus's first sustained encounter with the **Deuteronomistic regnal cycle** — the formulaic frame the Deuteronomistic Historian wraps around each king (accession synchronism → mother's name → evaluation → "walked in the way of X" → death/burial → succession → source-citation). The shipped 1 Kings corpus is impressively uniform across the formula family, but the pattern is **undocumented** in `docs/translator_decisions/`. The 1SA audit explicitly deferred a `dtr_history_cycle_formulas_2026-05.md` doc as "forward-pending for Kings + Chronicles." 1 Kings is where the formulas first appear in force, and **2 Kings is almost entirely regnal formulas** (every king of Israel + Judah down to the exile).

**Shipped formula surfaces (uniform unless flagged):**

| Formula | Hebrew | 1KI Thai (locked-candidate) | Verses |
|---|---|---|---|
| **Evaluation (evil)** | (וַיַּעַשׂ) הָרַע בְּעֵינֵי יְהוָה | `ทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า` | 11:6, 14:22, 15:26, 15:34, 16:19, 16:25, 16:30 |
| **Evaluation (right)** | (וַיַּעַשׂ) הַיָּשָׁר בְּעֵינֵי יְהוָה | `ทำสิ่งที่ถูกต้องในสายพระเนตรขององค์พระผู้เป็นเจ้า` | 15:5, 15:11, 22:43 |
| **"Walked in the way of Jeroboam / in his sin"** | וַיֵּלֶךְ בְּדֶרֶךְ יָרָבְעָם וּבְחַטָּאתוֹ | `ดำเนินตามทางของเยโรโบอัม…และในบาปที่เยโรโบอัมชักนำให้อิสราเอลทำตาม` | 15:34, 16:2, 16:19, 16:26, 22:53 |
| **Death / burial / succession** | וַיִּשְׁכַּב עִם אֲבֹתָיו | `ล่วงหลับไปอยู่กับบรรพบุรุษ … ขึ้นครองราชย์แทน` | 2:10, 11:43, 14:20, 14:31, 15:8, 15:24, 16:6, 16:28, 22:40, 22:51 |
| **"High places not removed"** | הַבָּמוֹת לֹא־סָרוּ | (two surfaces — see below) | 15:14, 22:44 |

**Two minor surface drifts within the family (would be normalized by the lock):**
- **Evaluation intensifier:** 7 regnal notices use `ทำสิ่งชั่วร้าย`, but **22:53 (Ahaziah)** ships `ทำสิ่งชั่ว` (no `ร้าย`) for identical הָרַע.
- **High-places-not-removed:** 15:14 → `ที่สูงทั้งหลายยังไม่ได้ถูกกำจัด`; 22:44 → `สถานบูชาบนที่สูงยังไม่ถูกรื้อถอน` (กำจัด vs รื้อถอน; ที่สูง vs สถานบูชาบนที่สูง).
- **Death-formula royal register:** `ทรงล่วงหลับ` falls on every Davidic-line king + Jeroboam, but the bare `ก็ล่วงหลับ` (no `ทรง`) falls on Baasha (16:6), Omri (16:28), Ahab (22:40) — possibly intentional delegitimization of the worst Northern usurper dynasties, possibly drift (Jeroboam, the archetypal Northern sinner, keeps `ทรง`, which weakens the "intentional" reading).

**Question:** Should the project write `docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md` now (locking the five formula surfaces above) so the pattern is forward-protected before 2 Kings — the book that is *almost entirely* regnal formulas — ships? And within that lock: (a) normalize the two minor surface drifts (22:53 `ชั่ว`→`ชั่วร้าย`; the high-places two-surface) to single canonical forms; and (b) is the death-formula `ทรง` split (withheld from Baasha/Omri/Ahab) a *principled* narrator's-honorific decision worth documenting as a register tool, or drift to be normalized to uniform `ทรงล่วงหลับ`?

---

## Item D — Adonai-YHWH compound at 1 Kgs 8:53: sentence-final vocative particle

**The pattern:** `divine_names_table_2026-05.md` carries a 2026-05-23 sub-rule (locked the day before this audit, from the 2SA audit) that makes the vocative particle for the אֲדֹנָי יְהוִה compound **position-dependent**:
- **Sentence-initial interjection** (`אֲהָהּ` / `בִּי` / `אָנָּא` + אֲדֹנָי יְהוִה) → **`ข้าแต่องค์พระผู้เป็นเจ้า`**
- **Mid-sentence appositional** (compound without a preceding interjection particle) → **bare `องค์พระผู้เป็นเจ้า`** (anchor: 2 Sam 7:18–29, David's covenant prayer)

Solomon's temple-dedication prayer (1 Kgs 8:22–53) uses `יְהוָה` / `יְהוָה אֱלֹהֵי יִשְׂרָאֵל` / `יְהוָה אֱלֹהָי` throughout (all compliant → `องค์พระผู้เป็นเจ้า` family). The **lone אֲדֹנָי יְהוִה compound** is the prayer's **closing word** at 8:53:

- **8:53 HEB:** `…בְּהוֹצִיאֲךָ אֶת־אֲבֹתֵינוּ מִמִּצְרַיִם **אֲדֹנָי יְהוִה**`
- **8:53 TH (shipped):** "…เมื่อพระองค์ทรงนำบรรพบุรุษของเราออกจากอียิปต์ **ข้าแต่องค์พระผู้เป็นเจ้า**"

The shipped form uses `ข้าแต่` (sentence-initial deferential vocative particle). But 8:53's compound is **sentence-final appositional** — there is no preceding `אֲהָהּ`/`בִּי`/`אָנָּא` interjection. Per the 2026-05-23 rule's two categories, an appositional compound (no interjection particle) takes the **bare** `องค์พระผู้เป็นเจ้า`. The shipped `ข้าแต่` instead reads 8:53 as a climactic closing vocative-plea. The case is genuinely borderline: sentence-*final* is neither sentence-*initial* interjection nor strictly mid-sentence appositional (the 2 Sam 7 anchor), and the 2026-05-23 rule's two categories don't explicitly name the sentence-final-climax position.

**This continues the Adonai-in-prayer thread** that has run through every Former-Prophets audit: JOS 7:7–8 (the 4-way distinction anchor), JDG 6:15→6:22 (the recognition-arc), 2 Sam 7:18–29 (the appositional-bare anchor). 1 Kgs 8:53 is the next single-occurrence test.

**Two questions:**
1. Should 8:53 normalize to the **bare** `…ออกจากอียิปต์ องค์พระผู้เป็นเจ้า` per the 2026-05-23 appositional rule (treating the sentence-final compound as appositional, like the 2 Sam 7 mid-sentence cases)? Or does a compound that *closes* a sustained prayer warrant a distinct "sentence-final climactic vocative" treatment with `ข้าแต่` — and if so, should that be documented as a third position-category in the sub-rule?
2. More broadly: the corpus has now accreted four Adonai sub-rules (2026-05-15 possessive, 2026-05-18 4-way, 2026-05-20 recognition-arc, 2026-05-23 position). Is the framework converging, or is each new prayer surfacing a new edge that suggests the rule-set is over-fitting to anchors rather than capturing a generalizable principle a Thai reader actually perceives?

---

## Item E — Pagan-deity register + cross-book Ashtoreth spelling convergence

**The pattern:** 1 Kings is the corpus's densest pagan-deity book after Judges (the ch-18 Carmel showdown vs the prophets of Baal + Solomon's apostasy to the Sidonian/Moabite/Ammonite gods in ch 11). The shipped renderings are clean and consistent with the OT-precedent `พระ`-register (`pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`):

| Deity | Hebrew | 1KI Thai |
|---|---|---|
| Baal | בַּעַל | **`พระบาอัล`** (uniform, 11 occurrences across chs 16/18/19/22) |
| Ashtoreth | עַשְׁתֹּרֶת | **`พระอัชเทเรทเทพีของชาวซีโดน`** (11:5, 11:33) |
| Chemosh | כְּמוֹשׁ | `พระเคโมชเทพ(อันน่าสะอิดสะเอียน)ของโมอับ` (11:7, 11:33) |
| Milcom | מִלְכֹּם | `มิลโคมเทพของชาวอัมโมน` (11:5, 11:33) |
| Molech | מֹלֶךְ | `โมเลคเทพอันน่าสะอิดสะเอียน` (11:7) |
| Asherah | אֲשֵׁרָה | `เสาอาเชราห์` (pole) / `เทพีอาเชราห์` (goddess) |

**Two positive findings worth a sanity-check:**
- **No `พระเจ้า`-for-pagan-deity violation.** The 1SA §12 problem (Dagon called `ดาโกนพระเจ้าของพวกเรา` at 1 Sam 5:7, applying the supreme Christian-divine title to a pagan god) does **not** recur in 1 Kings. Every literal pagan deity takes `พระ` / `เทพ` / `เทพี`, never `พระเจ้า`.
- **Cross-book Ashtoreth spelling convergence.** The 1SA audit §12 flagged a 3-form drift (อัชโทเรท / อาเชโทรท / อัชทาโรท) and recommended normalizing to **`อัชเทเรท`** (the form JDG 2:13 + 10:6 used). **1 Kings independently ships `อัชเทเรท` at 11:5 + 11:33** — reinforcing the recommended canonical spelling and strengthening the case to normalize 1SA's drift.

**Question:** 1 Kings confirms the OT-precedent `พระ`-register for pagan deities (`พระบาอัล`, `พระอัชเทเรท`, `พระเคโมช`) — distinct from the NT-Acts `เทพเจ้า` register (Acts 12:22, 14:11). With three Former-Prophets books now consistently using the `พระ`-prefix for proper-noun pagan deities + `เทพ`/`เทพี` descriptors, is the OT/NT register-split (`พระ`-prefix OT proper-noun deities vs `เทพเจ้า` NT generic-god references) stable enough to document as a deliberate principle in `pagan_deities_2026-04.md` / `ot_polytheistic_register_2026-05.md` — and does the `อัชเทเรท` spelling (now used in JDG + 1KI, drifting only in 1SA) become the locked corpus form, with the 1SA occurrences normalized to match?
