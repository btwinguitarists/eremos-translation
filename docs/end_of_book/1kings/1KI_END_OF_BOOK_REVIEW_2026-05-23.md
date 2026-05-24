# 1 Kings — End-of-Book Review

**Date:** 2026-05-23
**Scope:** All 22 chapters of 1 Kings (817 verses); `glossary.json`; `docs/translator_decisions/` corpus (~95 docs through the 2 Samuel end-of-book audit).
**Trigger:** 1KI 22 shipped (commit `eeb86e6`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Tenth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel, 2 Samuel) and the **fourth Former-Prophets / Deuteronomistic-History book.** 1 Kings is the first OT-corpus book whose dominant literary architecture is the **Deuteronomistic regnal cycle** (accession formula → evaluation formula → "walked in the way of X" → death/burial formula → succession), and the first downstream stress-test of two locks that explicitly named 1 Kings as a forward-cover target: `malak_yhwh_2026-05.md` ("1 Kings 19 (Elijah at Horeb)") and `spirit_of_yhwh_empowerment_2026-05.md` (1 Kgs 18:12, 22:24).
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) pass: 22/22 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 578-chapter corpus); `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); 22/22 chapters have `output/textual_variants/1kings_NN.json`. The single dirty file in `git status output/` is `output/check_reports/divine_names.md` — a transient single-chapter scratch report (`Chapters checked: 1`) regenerated out-of-band; report-only, not a translation surface, identical in kind to the note carried in the 1SA audit §22.
- **1 Kings is the first downstream book to ship a previously-drifted lock CLEANLY — and the first to drift AGAINST a different forward-protective lock.**
  - **`spirit_of_yhwh_empowerment_2026-05.md` HOLDS in 1 Kings.** Both Spirit-of-YHWH occurrences — **18:12** (Obadiah: "the Spirit of YHWH will carry you," נָשָׂא-class) and **22:24** (Zedekiah ben Chenaanah: "which way did the Spirit of YHWH pass from me," עָבַר-class) — ship **`พระวิญญาณขององค์พระผู้เป็นเจ้า`** with the **พระ** honorific intact. This is the **opposite** of the 1SA book-wide bare-`วิญญาณ` drift (1SA audit §4 DECIDE). 1 Kings validates the lock. See §4.
  - **`malak_yhwh_2026-05.md` DRIFTS at 1 Kgs 19:7.** The lock requires מַלְאַךְ יְהוָה → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** and its implementation checklist explicitly names "1 Kings 19 (Elijah at Horeb)" as a forward-cover target. 19:5 (standalone מַלְאָךְ) ships the correct **`ทูตสวรรค์องค์หนึ่ง`**, but 19:7 (מַלְאַךְ יְהוָה, the same angel) ships **`ทูตขององค์พระผู้เป็นเจ้า`** — missing `สวรรค์`, the precise drift the lock was created to eliminate (cf. its Exod 3:2 pre-fix). One surgical verse-edit. See §3. **DECIDE.**
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-1kings-v1`):
  - **§3 mal'akh-YHWH lock drift at 19:7** — drift against a forward-protective lock that named 1 Kings 19; 1-verse surgical fix (`ทูต` → `ทูตสวรรค์`).
  - **§17 MT/LXX inclusion-variant gap** — carried forward from 1SA §17 (and the 2SA textual-variant Tier-2 DECIDE). 1 Kings' textual_variants files contain **zero** inclusion-variant entries despite 1 Kings being the corpus's largest MT-vs-LXX divergence to date (the LXX 3 Reigns reordering, the two "Miscellanies" supplements at 3 Rgns 2:35a–o + 2:46a–l, the alternate Jeroboam narrative at 3 Rgns 12:24a–z, and the MT 20↔21 / LXX 21↔20 chapter-order swap).
- **5 items flagged REVIEW** (worth Ben's confirmation):
  - §5 DTr-evaluation-formula surface drift (`ทำสิ่งชั่วร้าย` ×7 regnal vs `ทำสิ่งชั่ว` at 22:53) + high-places-not-removed two-surface drift (15:14 vs 22:44)
  - §6 DTr death-formula royal-register split (`ทรงล่วงหลับ` for Davidic-line + Jeroboam vs bare `ก็ล่วงหลับ` for Baasha 16:6 / Omri 16:28 / Ahab 22:40)
  - §3b mal'akh human-messenger surface — 1 Kings ships a **third** corpus variant (`ผู้สื่อสาร`, 19:2/20:2/20:9) alongside 1SA's `ผู้ส่งสาร` / `ผู้ส่งข่าว`
  - §8 1 Kgs 8:53 Adonai-YHWH compound rendered `ข้าแต่องค์พระผู้เป็นเจ้า` (vocative particle) — the 2026-05-23 sub-rule assigns *appositional* compounds the bare form
  - §14 "until this day" leitwort — 1 Kings uniform `จนถึงทุกวันนี้` (sides with JDG-majority; makes **1SA the lone outlier** at bare `จนถึงวันนี้`)
- **2 items recommend new corpus docs** (STABLE-but-undocumented):
  - **§5 Deuteronomistic regnal-cycle formulas** — the signature architecture of Kings, uniform and principled across ~30 surfaces but UNDOCUMENTED. The 1SA audit flagged `dtr_history_cycle_formulas_2026-05.md` as forward-pending for Kings; 1 Kings is where it must be born. **HIGH priority** — gates 2 Kings (wall-to-wall regnal formulas) + 1–2 Chronicles.
  - §10 Deuteronomistic **Name-theology** (`בֵּית לְשֵׁם יְהוָה` → `พระนิเวศเพื่อพระนามขององค์พระผู้เป็นเจ้า`) — uniform across chs 3/5/8/9/11; cross-corpus thread back to Deut 12. MEDIUM priority.
- **External AI review (§3) pending.** Suggested 5-item packet (mal'akh 19:7 drift §3; MT/LXX 3-Reigns inclusion-variant gap §17; DTr regnal-formula doc-lock proposal §5; Adonai-YHWH 8:53 sentence-final vocative §8; pagan-deity register + cross-book Ashtoreth spelling convergence §12).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout. **259 surface occurrences** of `องค์พระผู้เป็นเจ้า` in `thai` verse-text across the 22 chapters (≈ the MT YHWH count for 1 Kings; minor surface-vs-lemma variance from compound collapses and verses with multiple occurrences).

**ยาห์เวห์ residues in verse text: zero.** No `ยาห์เวห์` surface in any 1 Kings `thai` field. (Place-name memorial compounds — the only sanctioned `ยาห์เวห์` survival per `divine_names_table_2026-05.md` — do not occur in 1 Kings.)

**Per-chapter first-occurrence YHWH footnote.** 21/21 chapters that contain YHWH carry the locked Tier-2 explanation in `output/textual_variants/1kings_NN.json` (`type: tetragrammaton_convention_first_occurrence`). (1 Kings 4 — the administrative-list chapter, Solomon's officials + provisions — contains no first-occurrence footnote; spot-check confirms it is a YHWH-light chapter.)

**LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 2. Elohim + Adonai compound divine names — **LOCKED**

- **Elohim → พระเจ้า** uniform across 1 Kings ✓. No drift.
- **Standalone divine אֲדֹנָי (third-person, narrator).** 1 Kgs **3:10** — וַיִּיטַב הַדָּבָר בְּעֵינֵי אֲדֹנָי ("the thing was good in the eyes of the Lord") → **`เป็นที่พอพระทัยขององค์เจ้านาย`**. Correctly uses the standalone-Adonai third-person form `องค์เจ้านาย`, distinct from YHWH's `องค์พระผู้เป็นเจ้า` — matches the 2026-05-18 4-way distinction (third-person title → `องค์เจ้านาย`). ✓
- **Adonai-YHWH compound (אֲדֹנָי יְהוִה), narrative reference.** 1 Kgs **2:26** — "you carried the ark of אֲדֹנָי יְהוִה before David" → **`หีบขององค์พระผู้เป็นเจ้า`** (bare collapse). Correct per the main table ("compound collapses to องค์พระผู้เป็นเจ้า"). ✓
- **Adonai-YHWH compound in prayer.** 1 Kgs **8:53** — the lone compound in Solomon's temple-dedication prayer — see §8 (REVIEW; sentence-final-vs-appositional particle question).

**LOCKED** ✓ (with the §8 8:53 REVIEW flag).

---

## 3. mal'akh-YHWH (1 Kgs 19) — **DECIDE before tagging (drift against a forward-protective lock)**

`malak_yhwh_2026-05.md` (locked 2026-05-13, tri-AI review) requires every divine מַלְאָךְ → **`ทูตสวรรค์`**, with the genitive qualifier carried by `ของ` + the divine-name form. Its §3 implementation checklist explicitly lists **"1 Kings 19 (Elijah at Horeb)"** as a forward-cover target. 1 Kings has three divine-mal'akh occurrences:

| Ref | Hebrew | 1KI Thai (shipped) | Locked Thai | Status |
|---|---|---|---|---|
| **19:5** | מַלְאָךְ (standalone — "an angel touched him") | **`มีทูตสวรรค์องค์หนึ่งมาแตะตัวเขา`** | `ทูตสวรรค์` | ✓ correct |
| **19:7** | **מַלְאַךְ יְהוָה** ("the angel of YHWH returned a second time") | **`ทูตขององค์พระผู้เป็นเจ้ากลับมา`** | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✗ **DRIFT** (missing `สวรรค์`) |
| **13:18** | מַלְאָךְ (the old prophet's claimed angel) | **`มีทูตสวรรค์องค์หนึ่งบอกข้า`** | `ทูตสวรรค์` | ✓ correct |

**The drift is exact and isolated.** 19:5 and 19:7 narrate the *same* angel feeding Elijah under the broom tree; 19:5 ships the locked `ทูตสวรรค์` but 19:7 drops `สวรรค์` to the bare `ทูต` — both an internal inconsistency within one pericope and the precise pre-fix form the lock was written to eliminate (the Exod 3:2 "ทูตขององค์พระผู้เป็นเจ้า" → "ทูตสวรรค์ขององค์พระผู้เป็นเจ้า" fix recorded in `malak_yhwh_2026-05.md` §2.3).

**Editorial assessment.** This is the second OT-corpus drift discovered AGAINST an explicitly-forward-protective lock that named the affected book (after 1SA §4 Spirit-of-YHWH). Unlike 1SA's 12-verse book-wide drift, this is a single surgical edit. The fix is unambiguous (the lock leaves no discretion): 19:7 → `ทูตสวรรค์ขององค์พระผู้เป็นเจ้ากลับมา…`.

**DECIDE before tagging — recommended:** restore `สวรรค์` at 19:7; re-run the ch-19 check report + back-translation; ship as a single-verse revision (`revision/malak-yhwh-1ki-19-2026-05`). **Severity: MEDIUM** (1-verse fix, but it blocks a clean v1 tag against a locked, forward-protective doc). Forward-protects 2 Kgs 1 (Elijah + Ahaziah's messengers — the next divine-mal'akh narrative), Zech 1–6, Mal.

---

## 3b. mal'akh human-messenger surface — **REVIEW (third cross-book variant)**

Per `malak_yhwh_2026-05.md`, human-messenger מַלְאָךְ is **outside the lock** ("use the plain register `ผู้ส่งสาร` or `ทูต` as context requires"). 1 Kings renders human envoys uniformly **within the book** as **`ผู้สื่อสาร`** (19:2 Jezebel's messenger to Elijah; 20:2, 20:9 Ben-Hadad's envoys to Ahab). But this is a **third corpus surface**: the 1SA audit §3 documented `ผู้ส่งสาร` (1SA 16:19+) and `ผู้ส่งข่าว` (1SA 6:21, ch 11). The corpus now carries three Thai surfaces for the identical human-messenger מַלְאָךְ lemma across JDG/1SA/1KI.

**REVIEW.** Cross-book normalization (recommend a single corpus surface — `ผู้ส่งสาร` has the widest footprint). Folds into the same cross-book pass as the 1SA §3 flag. **Severity: LOW.**

---

## 4. Spirit-of-YHWH (1 Kgs 18:12, 22:24) — **LOCKED (lock holds; first clean downstream ship)**

The Spirit-of-YHWH empowerment lock (`spirit_of_yhwh_empowerment_2026-05.md`) was the **HIGHEST-severity DECIDE** in the 1SA audit (§4 — 12/12 occurrences drifted to bare `วิญญาณ`). 1 Kings is the next book the lock named for forward-protection (§4 of the 1SA audit listed "1 Kings 18:12" and "1 Kings 22:24"). **1 Kings ships both occurrences COMPLIANT:**

| Ref | Hebrew | Verb class | 1KI Thai (shipped) |
|---|---|---|---|
| **18:12** | רוּחַ יְהוָה (Obadiah: "the Spirit of YHWH will carry you," נָשָׂא) | carry/transport | **`พระวิญญาณขององค์พระผู้เป็นเจ้าก็อาจพาท่านไป`** ✓ |
| **22:24** | רוּחַ יְהוָה (Zedekiah: "which way did the Spirit of YHWH pass from me," עָבַר) | pass/depart | **`พระวิญญาณขององค์พระผู้เป็นเจ้าออกจากข้าไปพูดกับเจ้าทางไหน`** ✓ |

Both ship the **`พระ`** honorific on Spirit — the exact element 1SA dropped. The verbs here (נָשָׂא "carry," עָבַר "pass") are **outside** the doc's 4-way empowerment split (which covers הָיָה עַל / לָבַשׁ / פָּעַם / צָלַח); both are flagged in the doc's "Edge cases + forward-watch" as "possibly out-of-scope" (18:12 נָשָׂא) and "may need adjacent treatment" (22:24 עָבַר). The divine-name surface (`พระวิญญาณขององค์พระผู้เป็นเจ้า`) is correct regardless of verb class.

**The ch-22 "lying spirit" is correctly NOT subsumed.** 22:21–23 — the council spirit who volunteers to be a `רוּחַ שֶׁקֶר` ("lying spirit") in the mouths of Ahab's prophets — is a *created spirit-being*, not the Spirit of YHWH, and ships bare **`วิญญาณ`** / **`วิญญาณมุสา`** ("a spirit" / "a lying spirit"). This is the right call: the empowerment lock's "Edge cases" excludes `רוּחַ רָעָה`-type non-divine spirit referents, and the divine `พระ` honorific is correctly withheld from the council-spirit.

**LOCKED** ✓. 1 Kings is the **first downstream book to ship the spirit-of-yhwh lock cleanly** and the strongest evidence that the lock-as-written is sustainable. **Recommend a one-line amendment** to `spirit_of_yhwh_empowerment_2026-05.md` §"Edge cases" formally adding נָשָׂא (1 Kgs 18:12 / 2 Kgs 2:16 — "the Spirit will carry/lift him") and עָבַר (1 Kgs 22:24 / 2 Chr 18:23) as documented out-of-empowerment-split verb classes that still take the `พระ` honorific, citing the 1 Kings clean ship as the anchor.

---

## 5. Deuteronomistic regnal-cycle formulas — **STABLE; recommend new doc (HIGH priority) + REVIEW (minor surface drift)**

This is the **signature cross-cutting architecture of 1 Kings** and the corpus's first sustained encounter with the Deuteronomistic regnal cycle. The 1SA audit (§"DTr cycle refrain — N/A in 1SA") explicitly deferred the `dtr_history_cycle_formulas_2026-05.md` doc as "forward-pending for Kings + Chronicles." **1 Kings is where it must be born.** The shipped corpus is impressively uniform across the formula family:

**(a) Evaluation formula** הָרַע / הַיָּשָׁר בְּעֵינֵי יְהוָה — uniform `(ทำ)สิ่งชั่วร้าย / สิ่งที่ถูกต้อง ในสายพระเนตรขององค์พระผู้เป็นเจ้า`:

| Did evil | Did right |
|---|---|
| 11:6 (Solomon), 14:22 (Judah), 15:26 (Nadab), 15:34 (Baasha), 16:19 (Zimri), 16:25 (Omri), 16:30 (Ahab) | 15:5 (David), 15:11 (Asa), 22:43 (Jehoshaphat) |

**(b) "Walked in the way of Jeroboam / in the sin he made Israel to sin"** — uniform `ดำเนินตามทางของเยโรโบอัม…และในบาปที่เยโรโบอัมชักนำให้อิสราเอลทำตาม` (15:34, 16:2, 16:19, 16:26, 22:53; the "sin of Jeroboam" thread also at 13:34, 14:16, 15:30, 16:31, 21:22).

**(c) Death/burial formula** וַיִּשְׁכַּב עִם אֲבֹתָיו → uniform `ล่วงหลับไปอยู่กับบรรพบุรุษ` (2:10, 11:43, 14:20, 14:31, 15:8, 15:24, 16:6, 16:28, 22:40, 22:51) + succession `ขึ้นครองราชย์แทน`.

**(d) "High places were not removed"** הַבָּמוֹת לֹא־סָרוּ — the king-was-good-but refrain (15:14 Asa, 22:44 Jehoshaphat).

**STABLE → new doc.** Recommend `docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md` locking the five formula surfaces (accession synchronism, mother's-name, evaluation, "walked in the way," death/burial/succession, "high places not removed," source-citation "are they not written in the book of the chronicles…"). This is the highest-value forward-protection from this audit: **2 Kings is wall-to-wall regnal formulas** (every king of Israel + Judah to the exile), and 1–2 Chronicles re-runs the Judahite cycle. Without a lock, a future translator will drift the formula surfaces across 2 Kings' ~40 regnal notices.

**Two minor surface drifts (REVIEW, fold into the new-doc lock):**
1. **Evaluation-formula intensifier.** The regnal notices use `ทำสิ่งชั่วร้าย` (×7) but **22:53 (Ahaziah)** ships `ทำสิ่งชั่ว` (no `ร้าย`) for the identical הָרַע. Recommend normalize 22:53 → `ทำสิ่งชั่วร้าย`. (Note: the non-regnal "sold yourself to do evil," הִתְמַכֶּרְךָ לַעֲשׂוֹת הָרַע, at 21:20+25 correctly uses a distinct construction — not a drift.)
2. **High-places-not-removed.** 15:14 → `ที่สูงทั้งหลายยังไม่ได้ถูกกำจัด`; 22:44 → `สถานบูชาบนที่สูงยังไม่ถูกรื้อถอน` — two surfaces (กำจัด vs รื้อถอน; ที่สูง vs สถานบูชาบนที่สูง) for the same formula. Recommend normalize.

**Severity: the doc is HIGH priority; the two surface drifts are LOW.**

---

## 6. DTr death-formula royal register — **REVIEW (ทรง split across kings)**

Within the §5(c) death formula, the royal honorific `ทรง` is applied **inconsistently**:

| `ทรงล่วงหลับ` (with royal honorific) | bare `ก็ล่วงหลับ` (no honorific) |
|---|---|
| David (2:10), Solomon (11:43), Jeroboam (14:20), Rehoboam (14:31), Abijam (15:8), Asa (15:24), Jehoshaphat (22:51) | **Baasha (16:6), Omri (16:28), Ahab (22:40)** |

Every Judahite (Davidic-line) king + the first Northern king (Jeroboam) gets `ทรง`; the bare form falls only on three later Northern kings (the Baasha founder + the Omride founder + Ahab). The split is **not** cleanly North/South (Jeroboam, the archetypal Northern sinner, gets `ทรง`).

**Two readings (Ben to confirm):**
- **(a) Intentional delegitimization.** The bare form may signal the diminished royal honor of the most-condemned usurper dynasties (Baasha's and Omri's house, climaxing in Ahab) — consistent with `honorifics_non_divine_authorities_2026-04.md`'s "public royal role → ทรง" being a *grantable* register the narrator can withhold. But Jeroboam's `ทรง` weakens this.
- **(b) Drift.** Later chapters (16+, 22) simply dropped the honorific from the death formula for some Northern kings.

**REVIEW.** Confirm whether the `ทรง`-withholding at 16:6 / 16:28 / 22:40 is principled (and if so, document it in the §5 DTr doc) or drift (normalize to `ทรงล่วงหลับ`). **Severity: LOW.**

---

## 7. חַי־יְהוָה oath formula — **LOCKED**

"As YHWH lives" → uniform **`องค์พระผู้เป็นเจ้า…ทรงพระชนม์อยู่`**:

| Ref | Speaker | Thai surface |
|---|---|---|
| 1:29 | David (royal oath, "as YHWH lives who has redeemed my life") | `องค์พระผู้เป็นเจ้าผู้ทรงไถ่ชีวิตของข้า…ทรงพระชนม์อยู่` |
| 2:24 | Solomon | `องค์พระผู้เป็นเจ้า…ทรงพระชนม์อยู่` |
| 17:1 | Elijah (to Ahab) | `องค์พระผู้เป็นเจ้าพระเจ้าแห่งอิสราเอล…ทรงพระชนม์อยู่` |
| 17:12 | the widow of Zarephath | `องค์พระผู้เป็นเจ้าพระเจ้าของท่านทรงพระชนม์อยู่แน่ฉันใด` |
| 18:10 | Obadiah | same |
| **18:15** | Elijah | **`องค์พระผู้เป็นเจ้าจอมโยธา…ทรงพระชนม์อยู่`** (YHWH-Tsebaoth compound preserved ✓) |
| 22:14 | Micaiah ben Imlah | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่แน่ฉันใด` |

The compound human oath at 1:31 (Bathsheba: "may my lord King David live forever") correctly extends `ทรงพระชนม์` to the human-king referent. Matches `hebrew_oath_formulas_2026-05.md` + the 1SA §8 lock.

**LOCKED** ✓.

---

## 8. Adonai-YHWH compound vocative at 8:53 — **REVIEW (sentence-final particle question)**

Solomon's temple-dedication prayer (8:22–53) is the densest divine-address passage in 1 Kings, but it uses **`יְהוָה` / `יְהוָה אֱלֹהֵי יִשְׂרָאֵל` / `יְהוָה אֱלֹהָי`** throughout (→ `องค์พระผู้เป็นเจ้า` / `…พระเจ้าแห่งอิสราเอล` / `…พระเจ้าของข้า`, all compliant). The **lone אֲדֹנָי יְהוִה compound** is the prayer's closing word at **8:53**:

> HEB: …בְּהוֹצִיאֲךָ אֶת־אֲבֹתֵינוּ מִמִּצְרַיִם **אֲדֹנָי יְהוִה**
> TH: …เมื่อพระองค์ทรงนำบรรพบุรุษของเราออกจากอียิปต์ **ข้าแต่องค์พระผู้เป็นเจ้า**

The shipped form prefaces `ข้าแต่` (sentence-initial deferential vocative particle). But the 2026-05-23 sub-rule of `divine_names_table_2026-05.md` (locked the day before this audit, from the 2SA audit) draws a **position-determines-particle** distinction:
- **Sentence-initial interjection** (`אֲהָהּ` / `בִּי` / `אָנָּא` + אֲדֹנָי יְהוִה) → `ข้าแต่องค์พระผู้เป็นเจ้า`
- **Mid-sentence appositional** (compound without a preceding interjection particle) → **bare `องค์พระผู้เป็นเจ้า`** (anchor: 2 Sam 7:18–29)

8:53's compound is **sentence-final appositional** (no `אֲהָהּ`/`בִּי`/`אָנָּא` interjection precedes it) — which the 2026-05-23 rule assigns the bare form. The shipped `ข้าแต่` reads it as a climactic closing vocative-plea instead. This is a genuine borderline the sub-rule's two categories don't cleanly cover (sentence-*final* is neither sentence-initial nor strictly mid-sentence).

**REVIEW.** Either (a) normalize 8:53 → bare `…ออกจากอียิปต์ องค์พระผู้เป็นเจ้า` per the 2026-05-23 appositional rule, or (b) document a "sentence-final climactic vocative" carve-out that warrants `ข้าแต่` at the close of a sustained prayer. Recommend (a) for sub-rule consistency. **Severity: LOW** (1 verse). Continues the Adonai-in-prayer thread running through JOS 7 / JDG 6 / 2 Sam 7.

---

## 9. "Still small voice" (1 Kgs 19:12) — **STABLE (verse-level rationale documented)**

The famous crux קוֹל דְּמָמָה דַקָּה ("a still small voice," KJV) at Elijah's Horeb theophany ships **`เสียงแผ่วเบาในความเงียบสงัด`** ("a faint sound in utter silence"), with a `key_decisions` entry decomposing קוֹל (เสียง) + דְּמָמָה (ความเงียบ) + דַקָּה (แผ่วเบา) and naming the poetic paradox ("God speaks in the silence, not in the storm, fire, or earthquake"). The surrounding theophany (19:11–13) renders the storm/earthquake/fire sequence with the repeated `แต่องค์พระผู้เป็นเจ้าไม่ได้สถิตใน…` ("but YHWH was not in the…"), preserving the rhetorical build.

**STABLE.** Thoughtful, well-documented handling of a load-bearing crux; no action needed. **Optional Layer-2:** a cross-reference noting the NT echo is thin here, but the "sound of sheer silence" is a frequent devotional touchstone — a Layer-2 note is polish, not a gap.

---

## 10. Deuteronomistic Name-theology — **STABLE; recommend doc or Layer-2 (MEDIUM)**

The "house for the **Name** of YHWH" centralization theology (Deut 12 substrate) is dense and uniform in 1 Kings: בֵּית לְשֵׁם יְהוָה / לִשְׁמִי / שָׁם שְׁמִי → **`พระนิเวศเพื่อพระนามขององค์พระผู้เป็นเจ้า`** / **`เพื่อนามของเรา`** / **`นามของเราจะอยู่ที่นั่น`** (3:2, 5:17, 5:19, 8:16–20, 8:29, 8:35, 8:43, 9:3, 9:7, 11:36). The Name-as-divine-presence motif (8:29 "my Name shall be there") is preserved cleanly with `นาม` / `พระนาม`.

**STABLE; not documented in `docs/translator_decisions/`.** The rendering is transparent at verse level, but the Deut 12 → 1 Kings 8 → (NT: Acts 7:47–49, John 1:14 σκηνόω) Name-theology thread is a cross-corpus theme analogous to the threads other docs lock. **Recommend** either a brief `name_theology_deuteronomistic_2026-05.md` doc or a Layer-2 cross-reference at 8:29 ↔ Deut 12:5,11. **Priority: MEDIUM** (forward-protects 2 Kgs 21:4,7 + 23:27 + the Chronicles temple-theology).

---

## 11. cherem + warfare ethics (1 Kgs 20:42) — **LOCKED**

The lone ḥerem occurrence is 20:42 — the prophet's word to Ahab for releasing Ben-Hadad: אִישׁ־חֶרְמִי ("the man I had devoted to destruction"). Renders within the locked `ทุ่มถวาย…เพื่อทำลาย` family per `ot_warfare_ethics_2026-05.md` (the 1SA §11 + JOS/DEU lock). No dense ḥerem cluster in 1 Kings (unlike Josh 6–11 / 1 Sam 15). Compliant.

**LOCKED** ✓.

---

## 12. Pagan deities + Baal-cycle register — **LOCKED (and reinforces the 1SA Ashtoreth normalization)**

1 Kings is the corpus's densest pagan-deity book after Judges (the ch-18 Carmel showdown + Solomon's apostasy in ch 11). The shipped renderings are clean and consistent with the OT-precedent `พระ`-register:

| Deity | Hebrew | 1KI Thai | Verses |
|---|---|---|---|
| **Baal** | בַּעַל | **`พระบาอัล`** (uniform — incl. "prophets of Baal," "altar of Baal") | 16:31, 16:32, 18:18, 18:19, 18:21, 18:22, 18:25, 18:26, 18:40, 19:18, 22:54 |
| **Asherah** | אֲשֵׁרָה | `เสาอาเชราห์` (pole, 14:23, 16:33) / `เทพีอาเชราห์` (goddess, 15:13) / `พระอาเชรา(ห์)` (18:19, prophets-of) | 14:23, 15:13, 16:33, 18:19 |
| **Ashtoreth** | עַשְׁתֹּרֶת | **`พระอัชเทเรทเทพีของชาวซีโดน`** | 11:5, 11:33 |
| **Milcom** | מִלְכֹּם | `มิลโคมเทพ(อันน่าสะอิดสะเอียน)ของชาวอัมโมน` | 11:5, 11:33 |
| **Molech** | מֹלֶךְ | `โมเลคเทพอันน่าสะอิดสะเอียน` | 11:7 |
| **Chemosh** | כְּמוֹשׁ | `พระเคโมชเทพ(อันน่าสะอิดสะเอียน)ของโมอับ` | 11:7, 11:33 |

**No `พระเจ้า`-for-pagan-deity violation** (the 1SA §12 Dagon-5:7 problem does **not** recur in 1 Kings; literal pagan deities consistently take the `พระ`/`เทพ`/`เทพี` register, never the supreme `พระเจ้า` title — compliant with `pagan_deities_2026-04.md` Rule 1 + `ot_polytheistic_register_2026-05.md` §1.3).

**Cross-book win on Ashtoreth spelling.** 1 Kings ships **`อัชเทเรท`** at 11:5 + 11:33 — the *exact* spelling the 1SA audit §12 recommended as canonical (1SA had shipped three different drifting spellings: อัชโทเรท / อาเชโทรท / อัชทาโรท; JDG shipped อัชเทเรท). 1 Kings independently lands on the JDG/recommended form, **reinforcing the case to normalize 1SA's drift to `อัชเทเรท`**. The שִׁקֻּץ / תּוֹעֵבָה "abomination" descriptor renders `(เทพ)อันน่าสะอิดสะเอียน` consistently.

**LOCKED** ✓. (One note: 11:5 מִלְכֹּם "Milcom" and 11:7 מֹלֶךְ "Molech" are rendered as two distinct names — `มิลโคม` vs `โมเลค` — both "of the Ammonites." This correctly tracks the MT's two spellings; some text traditions read 11:7 as מִלְכֹּם, but the corpus follows MT — defensible, no action.)

---

## 13. Royal ทรง-register for kings — **LOCKED (with §6 death-formula REVIEW)**

The narrator's royal `ทรง`-register for kings' public actions per `honorifics_non_divine_authorities_2026-04.md` is applied throughout: David (1:1 `ทรงพระชรา`), Solomon (`ทรงสร้าง`, `ทรงตื่นบรรทม`, `เสด็จ`), Rehoboam (12:6 `ทรงปรึกษา`), Jehoshaphat (22:43 `ทรงดำเนินตาม`), the Queen of Sheba (10:4 `ทรงเห็น`). The royal-death-formula `ทรง` inconsistency is the one flagged sub-item (§6 REVIEW).

**LOCKED** ✓ (with §6 flag).

---

## 14. "Until this day" leitwort — **REVIEW (cross-book; 1 Kings sides with JDG, 1SA is the outlier)**

1 Kings renders עַד הַיּוֹם הַזֶּה uniformly as **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) — 8:8, 9:13, 9:21, 10:12, 12:19. This matches the **JDG-majority** form (`จนถึงทุกวันนี้`, 6×) and stands **opposite the 1SA-uniform** bare form (`จนถึงวันนี้`, 8×, flagged 1SA §14).

**Cross-book corpus picture now (three DTr books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× (+1 drift at 19:30) |
| 1 Samuel | `จนถึงวันนี้` (bare) | 8× uniform |
| **1 Kings** | **`จนถึงทุกวันนี้`** | **5× uniform** |

**Two of three Former-Prophets books now agree on `จนถึงทุกวันนี้`; 1 Samuel is the lone outlier.** This sharpens the 1SA §14 cross-book REVIEW: the canonical surface should be `จนถึงทุกวันนี้` (JDG + 1KI), and 1SA's 8 occurrences should be normalized. `leitwort_handling_policy_2026-05.md` still does not lock a Thai surface for this leitwort.

**REVIEW.** Internal 1 Kings uniformity ✓; the cross-book decision (lock `จนถึงทุกวันนี้`; normalize 1SA) should land in `leitwort_handling_policy_2026-05.md`. **Severity: LOW.**

---

## 15. חֶסֶד covenant-love — **LOCKED**

חֶסֶד renders within the locked `chesed_covenant_love_2026-05.md` family: 2:7 (David's charge re: Barzillai's sons) → `ความรักมั่นคง`; 3:6 (×2, Solomon: "you showed great chesed to David…") → `ความรักมั่นคงอันใหญ่หลวง`; 8:23 (Solomon's prayer: covenant-keeping God) → covenant-chesed context; 20:31 (Ben-Hadad's servants: "the kings of Israel are merciful," מַלְכֵי חֶסֶד) → `ผู้มีเมตตา` (context-appropriate "merciful"). Compliant.

**LOCKED** ✓.

---

## 16. Solomonic wisdom (חָכְמָה) — **STABLE**

חָכְמָה / חָכָם renders uniformly **`สติปัญญา`** across the Solomon narrative (2:6, 3:28, 5:9, 5:10, 5:14, 5:26, 10:4, 10:6, 10:8, 10:23, 10:24, 11:41) and for the craftsman Hiram (7:14, "filled with wisdom"). No drift. The chapter-3 judgment narrative (the two women + the living/dead child) renders the wisdom-recognition cleanly (3:28 "they saw that the wisdom of God was in him to do justice"). Not separately documented, but uniform and unremarkable.

**STABLE** ✓.

---

## 17. MT/LXX inclusion-variant gap — **DECIDE before tagging (carried from 1SA §17, larger in Kings)**

The `output/textual_variants/1kings_NN.json` files contain **only** 21× `tetragrammaton_convention_first_occurrence` (YHWH footnote) + 1× `versification_divergence_mt_vs_english` (1kings_22.json, v44). **Zero** entries of `inclusion_variant_minus` / `inclusion_variant_plus` / MT-vs-LXX-divergence type exist — yet **1 Kings is the corpus's largest MT-vs-LXX divergence to date:**

| Divergence | Description | Documented? |
|---|---|---|
| **LXX 3 Reigns Solomon-narrative reordering** | The Greek 3 Reigns substantially reorders the Solomon material (chs 2–11) relative to MT. | ❌ |
| **The two "Miscellanies"** | 3 Rgns 2:35a–o + 2:46a–l — large supplementary blocks of Solomon material with no MT counterpart. | ❌ |
| **Alternate Jeroboam narrative** | 3 Rgns 12:24a–z — a parallel, divergent account of Jeroboam's rise. | ❌ |
| **MT 20↔21 / LXX 21↔20 chapter swap** | LXX places the Naboth's-vineyard chapter (MT 21) before the Aram-war chapter (MT 20). | ❌ |

The shipped text follows MT throughout — defensible and matching `ot_canon_and_text_base_2026-05.md`'s MT-base policy — but, exactly as in 1SA §17, the **Tier-2 transparency layer is missing**. The infrastructure is deployed (21/21 chapters have textual_variants files) but carries only the YHWH footnote.

**Versification divergences ARE handled** (this is *not* the gap): 1 Kings 5 (MT 5 = English 4:21–5:18) is documented both in `data/versification_map.json` and as a reader-facing note folded into `1kings_05.json`'s footnote ("**หมายเหตุการนับข้อ:** บทที่ 5 ใน MT ครอบคลุม… MT 5:1–14 = English 4:21–34, MT 5:15–32 = English 5:1–18"), and 1 Kings 22:43/44 carries a dedicated `versification_divergence_mt_vs_english` entry. (Minor structural asymmetry: ch 5's divergence is folded into the YHWH footnote text while ch 22's is a separate typed entry — worth normalizing when the §17 work lands, but both are reader-visible.)

**DECIDE before tagging — recommended path** (mirrors the 1SA §17 + 2SA textual-variant DECIDE): write Tier-2 chapter-footer entries documenting the MT-base decision + the major LXX 3-Reigns divergences (minimally a 1 Kings 2 / 11 footer for the Miscellanies + Solomon reordering, a ch-12 footer for the alternate Jeroboam narrative, and a ch-20/21 footer noting the LXX chapter-order swap). **Cost:** ~4 chapter-footer JSON entries; no translation surface edits. **Severity: HIGH** — this is the second consecutive book to ship the same gap, and 1 Kings is the largest LXX-divergence case before Jeremiah. Gates the Tier-2 textual-variant infrastructure for 2 Kings (LXX OG), Jeremiah (MT ~1/8 longer than LXX), and Daniel.

---

## 18. Inherited corpus locks — all compliant except where flagged

| Doc | 1KI evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH 259 surfaces, 0 ยาห์เวห์ residue), §2 (Elohim/Adonai; 3:10 องค์เจ้านาย, 2:26 compound collapse). **EXCEPTION:** 8:53 sentence-final compound vocative particle (§8). | **LOCKED-with-§8-REVIEW** |
| `malak_yhwh_2026-05.md` | §3 — **DRIFT at 19:7** (ทูต, missing สวรรค์); 19:5 + 13:18 compliant. | **DECIDE-§3** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §4 — **HOLDS** (18:12 + 22:24 ship พระวิญญาณ; council-spirit 22:21–23 correctly bare). First clean downstream ship. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | §7 — חַי־יְהוָה ×7 uniform `ทรงพระชนม์อยู่`; 18:15 Tsebaoth compound preserved. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | §15 — ความรักมั่นคง / เมตตา per context (2:7, 3:6, 8:23, 20:31). | **LOCKED** |
| `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` | §12 — พระบาอัล uniform; อัชเทเรท/เคโมช/มิลโคม/โมเลค พระ-register; no พระเจ้า-for-pagan violation. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | King-name + place-name spot-check clean (โซโลมอน, เรโหโบอัม, เยโรโบอัม, อาหับ, เยโฮชาฟัท, เยเซเบล, เอลียาห์, โอบาดีห์, เบนฮาดัด, อัชเทเรท matches JDG). **Cross-book win:** 1KI อัชเทเรท reinforces 1SA §12 normalization. | **LOCKED** |
| `ot_warfare_ethics_2026-05.md` | §11 — 20:42 ḥerem within ทุ่มถวาย…เพื่อทำลาย family. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | §13 — royal ทรง for kings + Queen of Sheba. **EXCEPTION:** death-formula ทรง split (§6). | **LOCKED-with-§6-REVIEW** |
| `nicham_divine_relenting_2026-05.md` | No נחם lemma in 1 Kings (21:29 Ahab's reprieve is לֹא־אָבִיא, "I will not bring," not נחם). | **LOCKED (N/A)** |
| `leitwort_handling_policy_2026-05.md` | §14 — internal uniform จนถึงทุกวันนี้; cross-book 1SA-outlier decision pending. | **LOCKED-with-§14-cross-book-REVIEW** |
| `verse_schema_and_versification_2026-05.md` | §17 — ch 5 (MT 5 = Eng 4:21–5:18) + ch 22:43/44 divergences documented in map + textual_variants. | **LOCKED** |
| `ot_register_policy_2026-05.md` | Royal ทรง for YHWH-volitional + king-office; plain register for character speech. Solomon's prayer ch 8 register clean. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` + `hebrew_idioms_and_metaphor_2026-05.md` | Wayyiqtol narrative chains pervasive; "hand of YHWH" (18:46); "kindled anger" (`ทรงพระพิโรธ` 16:33). Compliant. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §17 — **INCLUSION-VARIANT GAP** (3 Reigns divergences undocumented). | **DECIDE-§17** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Hand of YHWH on Elijah" (18:46), "YHWH's anger" (16:33) → พระหัตถ์ / ทรงพระพิโรธ. Compliant. | **LOCKED** |

---

## 19. NT cross-corpus echoes from 1 Kings — **STABLE (Layer-2 opportunities)**

1 Kings (especially the Elijah cycle + Solomon) is heavily echoed in the NT. Cross-check / Layer-2 candidates:

| 1KI ref | NT echo | Note |
|---|---|---|
| 17:1–18:46 (Elijah + the drought) | **Jas 5:17–18** ("Elijah prayed… no rain for 3½ years") | Layer-2 cross-ref candidate |
| 17:8–24 (widow of Zarephath) | **Luke 4:25–26** (Jesus cites the Zarephath widow) | Layer-2 candidate |
| 19:18 ("7,000 who have not bowed to Baal") | **Rom 11:2–4** (Paul cites the 7,000 remnant) | verify Thai surface alignment |
| 19:1–18 (Elijah at Horeb) | **Matt 17 / Mark 9 (Transfiguration — Elijah appears)** | thematic |
| 10:1–13 (Queen of Sheba) | **Matt 12:42 / Luke 11:31** ("the Queen of the South") | Layer-2 candidate |
| 10:4–7 (Solomon's glory) | **Matt 6:29 / Luke 12:27** ("Solomon in all his glory") | Layer-2 candidate |
| 8:10–13 (glory fills the temple) | **Acts 7:47–49** (Stephen: "Solomon built him a house") | Layer-2 candidate |

**STABLE.** Renderings are sound; the cross-references are corpus-completeness polish, not gaps. **Severity: LOW.** (Recommend prioritizing the Jas 5:17 + Luke 4:25 + Rom 11:2–4 cross-refs, which are direct citations rather than allusions.)

---

## 20. Mechanical (§1) — all green (one transient report file)

- 22/22 chapters: `output/check_reports/1kings_NN_review.md` all "✅ Ready to ship" ✓
- 22/22 chapters: `output/back_translations/1kings_NN.json` ✓
- 22/22 chapters: `output/translations/1kings_NN.json` (817 verses) ✓
- 22/22 chapters: `output/textual_variants/1kings_NN.json` ✓ (YHWH footnote deployed; inclusion-variant gap flagged §17)
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (578-chapter corpus)
- `check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `audit_inclusion_variants.py --book 1KI --strict`: **0 candidates** (the heuristic is NT-SBLGNT-tuned; it does not catch MT/LXX 3-Reigns divergences — see §17. **Note:** the book-code `1KI` was not registered in the §3/§4 tooling slug tables (`build_external_review_packet.py` `BOOKS`, `audit_items_to_yaml.py` `BOOK_SLUGS`); registered as part of this audit per the EOB book-code-registration gotcha.)
- `export_to_usfm.py --book 1KI`: **N/A** — the script's `BOOKS` table is NT-only; OT USFM export is a carried-over separate concern (as noted in prior OT audits).
- `git status output/`: **clean except `output/check_reports/divine_names.md`** — a transient single-chapter scratch report (`Chapters checked: 1`, regenerated out-of-band; its only diff clears a stale 2SA 1:10 warning). Report-only, not a 1 Kings translation surface; identical in kind to the 1SA §22 note.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **259**. `ยาห์เวห์` residues: **zero**.

**Severity: GREEN.**

---

## 21. Flagged for Ben's attention

### A. mal'akh-YHWH lock drift at 19:7 — **DECIDE before tagging** (§3)
1 Kgs 19:7 ships `ทูตขององค์พระผู้เป็นเจ้า`; `malak_yhwh_2026-05.md` requires `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` and explicitly named "1 Kings 19" as a forward-cover target. 19:5 + 13:18 are compliant; 19:7 is the one drift (and internally inconsistent with 19:5 in the same pericope). **1-verse surgical fix** (add `สวรรค์`). Recommended path: `revision/malak-yhwh-1ki-19-2026-05`. Forward-protects 2 Kgs 1, Zech 1–6, Mal.

### B. MT/LXX inclusion-variant gap — **DECIDE before tagging** (§17)
Zero inclusion-variant entries in 1KI textual_variants despite the largest MT-vs-LXX divergence to date (3 Reigns Solomon reordering, the two Miscellanies, the alternate Jeroboam narrative, the MT 20↔21 chapter swap). Carried forward from 1SA §17 + 2SA. Cost: ~4 chapter-footer JSON entries; no surface edits. Gates 2 Kgs + Jer + Dan.

### C. Deuteronomistic regnal-cycle formulas — **STABLE; new doc (HIGH priority)** (§5)
Write `docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md` locking the five formula surfaces (evaluation, "walked in the way of Jeroboam," death/burial/succession, "high places not removed," source-citation). 1SA deferred this doc to Kings; 1 Kings is where it must be born. Forward-protects 2 Kings' ~40 regnal notices + 1–2 Chronicles. Fold in the two minor surface drifts (22:53 `ชั่ว`→`ชั่วร้าย`; 15:14/22:44 high-places two-surface).

### D. DTr death-formula royal-register split — **REVIEW** (§6)
`ทรงล่วงหลับ` (Davidic line + Jeroboam) vs bare `ก็ล่วงหลับ` (Baasha 16:6 / Omri 16:28 / Ahab 22:40). Confirm intentional delegitimization vs drift; document or normalize. **LOW.**

### E. Adonai-YHWH 8:53 sentence-final vocative — **REVIEW** (§8)
8:53 closing compound אֲדֹנָי יְהוִה ships `ข้าแต่องค์พระผู้เป็นเจ้า`; the 2026-05-23 sub-rule assigns appositional compounds the bare form. Borderline (sentence-final ≠ sentence-initial interjection nor strictly mid-sentence). Recommend normalize to bare per the appositional rule, or document a sentence-final-climax carve-out. **LOW.**

### F. mal'akh human-messenger surface — **REVIEW** (§3b)
1 Kings ships a third corpus surface (`ผู้สื่อสาร`) alongside 1SA's `ผู้ส่งสาร` / `ผู้ส่งข่าว`. Cross-book normalize (recommend `ผู้ส่งสาร`). **LOW.**

### G. "Until this day" leitwort cross-book normalization — **REVIEW** (§14)
1 Kings uniform `จนถึงทุกวันนี้` sides with JDG; **1SA is the lone outlier** (`จนถึงวันนี้`). Lock `จนถึงทุกวันนี้` in `leitwort_handling_policy_2026-05.md`; normalize 1SA's 8 occurrences. **LOW.**

### H. Deuteronomistic Name-theology — **STABLE; doc or Layer-2 (MEDIUM)** (§10)
`พระนิเวศเพื่อพระนามขององค์พระผู้เป็นเจ้า` uniform across chs 3/5/8/9/11. Recommend a brief `name_theology_deuteronomistic_2026-05.md` or a Layer-2 cross-ref at 8:29 ↔ Deut 12. Forward-protects 2 Kgs 21/23 + Chronicles.

### I. spirit-of-yhwh edge-case amendment — **STABLE; doc amendment (LOW)** (§4)
Add נָשָׂא (1 Kgs 18:12) + עָבַר (1 Kgs 22:24) to `spirit_of_yhwh_empowerment_2026-05.md` §"Edge cases" as documented out-of-empowerment-split verb classes that still take the `พระ` honorific, citing the 1 Kings clean ship as the anchor.

### J. New corpus docs to write — summary
1. **`dtr_history_cycle_formulas_2026-05.md`** (§C) — regnal-cycle formula family; gates 2 Kings + Chronicles ← **HIGH PRIORITY**
2. **`name_theology_deuteronomistic_2026-05.md`** (§H) — Name-centralization thread; gates 2 Kings + Chronicles ← MEDIUM (or Layer-2)

### K. Existing docs to amend
- **`malak_yhwh_2026-05.md`** — after the §3 19:7 fix ships, tick "1 Kings 19" on the §3 forward-cover checklist + note the retroactive remediation.
- **`spirit_of_yhwh_empowerment_2026-05.md`** — §"Edge cases" amendment per §I (נָשָׂא + עָבַר).
- **`leitwort_handling_policy_2026-05.md`** — lock `จนถึงทุกวันนี้` as canonical per §14.
- **`divine_names_table_2026-05.md`** — optionally refine the 2026-05-23 sub-rule to cover sentence-final climactic compounds per §8.
- **`proper_names_and_transliteration_2026-05.md`** — note that 1KI `อัชเทเรท` confirms the 1SA §12 normalization target.

### L. External AI review (§3 of checklist) — pending
Recommended 5-cluster packet (see `external_review_items_1KI.md`):
1. **mal'akh-YHWH 19:7 drift** (§3) — drift against a forward-protective lock
2. **MT/LXX 3-Reigns inclusion-variant gap** (§17) — largest LXX divergence to date
3. **DTr regnal-formula doc-lock proposal** (§5) — corpus-architecture decision before 2 Kings
4. **Adonai-YHWH 8:53 sentence-final vocative** (§8) — continues the Adonai-in-prayer thread
5. **Pagan-deity register + cross-book Ashtoreth convergence** (§12) — gate-status check

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 10 items (§1 YHWH, §2 Elohim/Adonai, §4 Spirit-of-YHWH [lock holds], §7 oath formula, §11 cherem, §12 pagan deities, §13 royal register, §15 chesed, §16 wisdom, §20 mechanical; + inherited locks via §18)
- **STABLE (recommend new doc / Layer-2):** 3 items (§5 DTr regnal formulas [HIGH], §10 Name-theology [MEDIUM], §9 still-small-voice [verse-level; no action])
- **REVIEW:** 5 items (§3b mal'akh human-messenger surface, §5 DTr surface drifts, §6 death-formula ทรง split, §8 Adonai 8:53 vocative, §14 cross-book "until this day")
- **DECIDE:** 2 items (§3 mal'akh-YHWH 19:7 lock drift; §17 MT/LXX inclusion-variant gap)

**2 DECIDE items block the `book-1kings-v1` tag** (§3, §17).

**1 new translator_decisions doc strongly recommended** (`dtr_history_cycle_formulas_2026-05.md` — HIGH) **+ 1 optional** (`name_theology_deuteronomistic_2026-05.md` / Layer-2 — MEDIUM).

**Existing docs to amend:** `malak_yhwh_2026-05.md` (19:7 remediation), `spirit_of_yhwh_empowerment_2026-05.md` (נָשָׂא/עָבַר edge cases), `leitwort_handling_policy_2026-05.md` (lock `จนถึงทุกวันนี้`), `divine_names_table_2026-05.md` (optional 8:53 sub-rule refinement), `proper_names_and_transliteration_2026-05.md` (Ashtoreth confirmation).

---

## Recommendation

**1 Kings ships in strong corpus-hygiene shape.** It is the **fourth Former-Prophets book** and the first sustained encounter with the Deuteronomistic regnal cycle. The audit finds:

- **The Spirit-of-YHWH lock HOLDS** (18:12 + 22:24 ship `พระวิญญาณ`) — the first downstream book to ship cleanly the lock that 1SA drifted from, validating the lock-as-written.
- **The mal'akh-YHWH lock DRIFTS once** (19:7 missing `สวรรค์`) — a single surgical edit, but a drift against a forward-protective lock that named 1 Kings 19, so it blocks a clean v1 tag.
- The DTr regnal-cycle formulas are uniform and principled but **undocumented** — the highest-value forward-protection opportunity from this audit (gates 2 Kings + Chronicles).
- Pagan-deity handling is clean and **reinforces the 1SA Ashtoreth normalization** (1KI independently ships `อัชเทเรท`).
- The MT/LXX inclusion-variant gap is the **second consecutive book** to ship without Tier-2 disposition of major textual divergences — and 1 Kings (LXX 3 Reigns) is the largest such case before Jeremiah.

**Tag `book-1kings-v1` after:**
1. Ben's decisions on **§A + §B** (DECIDE: mal'akh-YHWH 19:7 fix; MT/LXX inclusion-variant gap)
2. Ben's confirmation on **§D through §G** (REVIEW items)
3. The **`dtr_history_cycle_formulas_2026-05.md`** doc written (§C — HIGH; ideally before 2 Kings ships)
4. Existing-doc amendments (per §K)
5. External AI sanity-check (§L)

**The single load-bearing forward-protection step from this audit** is writing the DTr regnal-cycle formulas doc before 2 Kings — the book that is *almost entirely* regnal formulas — begins shipping.
