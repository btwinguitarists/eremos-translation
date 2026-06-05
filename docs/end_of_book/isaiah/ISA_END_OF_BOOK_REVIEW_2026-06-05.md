# Isaiah — End-of-Book Review

**Date:** 2026-06-05
**Scope:** All 66 chapters of Isaiah (~1,292 verses); `glossary.json`; `docs/translator_decisions/` corpus (96 docs).
**Trigger:** ISA 66 shipped (commit `0d0e09da`); per `docs/END_OF_BOOK_CHECKLIST.md`. **The largest book in the corpus and the most NT-forward** — Isaiah is the single most-quoted OT book in the New Testament (~85 quotations/allusions), the source of the canon's central messianic surfaces (7:14 Immanuel, 9:5-6 throne-names, 11:1-10 the Branch, the four Servant Songs, 52:13–53:12), the densest OT cluster of divine self-declarations (the "I am YHWH / I am he" oracles of chs 40–48), the densest idol-polemic (chs 40–48), and the OT terminus of the "new heavens and new earth" hope (65:17, 66:22 → Rev 21:1, 2 Pet 3:13). All of the NT it cross-quotes is **already shipped**, so Isaiah is the first OT book whose harmonization can be checked against a complete NT.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **26 cross-cutting items reviewed.** Mechanical gates (§1) pass: 66/66 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the corpus); `check_phrase_consistency.py` clean (0 violations across 38 audited locks, 27,250 verses); `audit_inclusion_variants.py --book isaiah --strict` = **0 candidates, exit 0**; `check_divine_names.py --book ISA` = exit 0 with **6 soft warnings, all confirmed false positives** (human "lord/master," §4); `check_versification_anchor.py --book ISA` = exit 0, both divergence zones registered (§12). 64/66 chapters carry a `textual_variants` YHWH-footnote file; ch. **15 & 46 correctly have none** (neither contains the Tetragrammaton). Two infrastructure gaps surfaced (§25): `export_to_usfm.py` still rejects `ISA` (the LAM/SNG book-code gotcha), and the §3 packet tool's `BOOKS` table was missing `ISA` (**registered as part of this audit**).
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-isaiah-v1`):
  - **§6 — Ratify Isaiah's committal-messianic-surface policy, and reconcile it against Daniel 9:25.** Isaiah is *internally* exemplary and fully consistent: at every messianic fork it takes the **committal evangelical-consensus reading in the main text** (7:14 หญิงพรหมจารี "virgin"; 9:5 พระเจ้าผู้ทรงฤทธิ์ "Mighty God," locked identical to the undisputed-divine 10:21; 53:11 the DSS/LXX "light") while keeping **descriptive, non-endorsing notes** (Hebrew weight preserved, NT labeled "reception," no NT vocabulary spliced into the OT surface, the Servant kept in plain register). This obeys `RULES.md §0` and the shipped Gen 3:15 protoevangelium precedent. **Two things need Ben's eye before sealing the OT's most-scrutinized book:** (a) the 9:6 `thai_summary` line *"คริสตจักรอ่านพระนามเหล่านี้สำเร็จในพระเยซูคริสต์"* ("the church reads these names fulfilled in Jesus Christ") is the single most doctrinally-forward summary in the book and sits on the RULES §0 "describe-don't-endorse" line (defensible under the "the church reads…" reception framing, but it is the one line a strict-§0 reviewer would point at); and (b) the Daniel audit rendered מָשִׁיחַ **generically** (ผู้ถูกเจิม, non-committal) at Dan 9:25-26, which now reads as the **outlier** against Isaiah + Gen 3:15 — a reviewer comparing Isaiah 9/53 with Daniel 9 will see the asymmetry. **Bless the committal-surface policy for Isaiah and decide whether Daniel 9:25-26 is revisited toward it (or its difference articulated).** See §6.
- **8 items flagged REVIEW** (worth Ben's confirmation; the anthropomorphism drift, §13, is the one mechanical fix best done before tag):
  - **§13 — divine-anthropomorphism Rachasap drift (the loudest mechanical finding).** `divine_anthropomorphism_thai_grammar_2026-05.md` locks the divine **arm** זְרוֹעַ → **พระกร** and the divine **Spirit** רוּחַ → **พระวิญญาณ**. Both drift to plain register on divine referents: **arm = แขน** at 51:5, 51:9, 63:5 (vs พระกร at 40:10, 52:10, 53:1, 59:16 — note 51:9 แขน sits one column from 52:10 พระกร in the *same* "bared holy arm" thread, and 63:5 แขน is structurally identical to 59:16 พระกร); **Spirit = วิญญาณ** at 42:1, 44:3, 59:21 (vs พระวิญญาณ at 11:2, 61:1, 63:10). The pattern is systematic — 1st-person divine speech ("my arm/my Spirit") triggers the lapse. 42:1 is load-bearing (Servant Song quoted at Matt 12:18). **Mechanically fixable; recommend a block-tag normalization before v1.** See §13.
  - **§3 — אֲדֹנָי יְהוִה צְבָאוֹת ("Lord GOD of hosts") split.** 5 occurrences drop Adonai (→ องค์พระผู้เป็นเจ้าจอมโยธา: 3:15, 10:23, 22:5, 22:12, 28:22); **2 mark it** (→ องค์เจ้านาย องค์พระผู้เป็นเจ้าจอมโยธา: 22:14b, 22:15), both inside the ch.22 Shebna oracle. The bare אֲדֹנָי יְהוִה compound (17×) and bare divine Adonai (22×) are otherwise perfect. Normalize the 2 outliers per the `divine_names_table` mid-sentence sub-rule (drop Adonai), unless Ben prefers marking (then normalize the 5). See §3.
  - **§9 + §10 — NT cross-quotation: missing Category-B footnotes + retro-candidates.** The quoted cores are byte-shared and MT-vs-LXX divergences are correctly identified, but ~7 NT-cited MT/LXX divergences lack the policy-mandated `textual_variants` Layer-2 footer (9:1, 11:10, 25:8 [KD claims one that doesn't exist], 29:13-14, 42:1/42:4, 45:23, 65:1-2), and there are NT-side retro-candidates: **53:1 พระกร vs the shipped John 12:38 พระหัตถ์** (translator self-flagged), **56:7 นิเวศ vs the shipped Matthew 21:13 บ้าน**, and the 8:14/28:16 NT-internal Rom↔1Pet drift. See §9, §10.
  - **§11 — Qumran-footer asymmetry.** 33:8 + 53:11 (reader-affecting DSS adoptions) got Tier-2 footers; 21:8 (lion→lookout) + 19:18 (Destruction→Sun) are KD-only — and the 33:8 footer itself names "19:18; 21:8" as cluster practice. Add footers or affirm KD-level suffices.
  - **§24 — śāʿîr split.** The goat-demon שָׂעִיר is rendered demonic ผีปีศาจรูปแพะ at 13:21 but naturalized to แพะป่า ("wild goat") at 34:14 — where it sits *beside* Lilith and contradicts the Lev 17:7 goat-demon lock. Harmonize 34:14 or document the split.
  - **§27 — polytheistic-register reader footnote.** The idol-satire / lowercase-deity / cosmic-creature apparatus lives only in `key_decisions` (reader-invisible); none of Isaiah's `textual_variants` files carry a polytheistic-register first-occurrence footnote. Confirm whether `ot_polytheistic_register §3` mandates a reader-facing note (then add one; ch.46 Bel/Nebo has no host file) or whether KD-only is the established corpus practice.
  - **§1 (minor) — Holy-One connector 60:14.** The lone blemish on a 24× leitwort: "ศิโยน**แห่ง**องค์บริสุทธิ์**ของ**อิสราเอล" uses ของ where the other 23 use แห่ง. One-character spot-fix.
  - **§4 (minor) — goel พระ-prefix.** The personal divine-Redeemer doc-form is พระผู้ไถ่; Isaiah's apposition uses un-prefixed ผู้ไถ่ in 12/13 (only 63:16 carries พระ). Confirm the apposition-vs-standalone register is intended.
- **Several STABLE-but-undocumented patterns** recommend corpus-doc lift (§1 Holy One of Israel; §5 Rock/Mighty One/El Gibbor; §23 idol-fabrication satire; §24 Bel/Nebo + cosmic-creature table rows). Two **new-lock candidates** surfaced: **חַי־אָנִי "as I live"** divine oath (49:18; not in `hebrew_oath_formulas`; recurs in Num/Ezek) and **widening the `malak` + anthropomorphism check scopes to include Isaiah**.
- **External AI review (§3) pending.** Suggested 4-item packet: messianic committal-surface policy + Daniel reconciliation (§6 DECIDE); anthropomorphism Rachasap drift (§13); the śāʿîr demonic-register split (§24); the NT cross-quotation footnote/retro-candidate cleanup (§9/§10).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. קְדוֹשׁ יִשְׂרָאֵל — "Holy One of Israel" (Isaiah's signature title) — **STABLE (recommend table row) + minor REVIEW (60:14)**

Isaiah's defining divine title, rendered with near-perfect uniformity:

| Hebrew | Thai | Count | Representative refs |
|---|---|---|---|
| קְדוֹשׁ יִשְׂרָאֵל | **องค์บริสุทธิ์แห่งอิสราเอล** | 23 | 1:4, 5:19, 5:24, 10:20, 12:6, 17:7, 29:19, 30:11/12/15, 31:1, 37:23, 41:14/16/20, 43:3/14, 45:11, 47:4, 48:17, 54:5, 55:5, 60:9 |
| קְדוֹשׁ יַעֲקֹב | องค์บริสุทธิ์แห่งยาโคบ | 1 | 29:23 |
| קְדוֹשׁוֹ / קָדוֹשׁ standalone | องค์บริสุทธิ์ (40:25); ผู้ทรงพระนามว่าบริสุทธิ์ (57:15) | 3 | 10:17, 40:25, 49:7, 57:15 |
| קָדוֹשׁ ×3 (Trisagion) | บริสุทธิ์ บริสุทธิ์ บริสุทธิ์ | 1 | 6:3 |

**Drift candidate (1, cosmetic) — REVIEW:** **60:14** renders "ศิโยน**แห่ง**องค์บริสุทธิ์**ของ**อิสราเอล" — the title-internal connector is **ของ** where all 23 other "of Israel" occurrences use **แห่ง**. One-character inconsistency; the only blemish on the leitwort.

**Recommend:** lock **องค์บริสุทธิ์แห่งอิสราเอล** with a one-line row in `divine_names_table_2026-05.md` (the title is currently undocumented at corpus level despite being Isaiah's signature, ~25× — and it recurs in 2 Kings 19:22, Pss, Jer 50:29, 51:5). **Severity: LOW.**

---

## 2. יְהוָה צְבָאוֹת — "YHWH / LORD of hosts" (Sabaoth) — **LOCKED**

60 verses; **องค์พระผู้เป็นเจ้าจอมโยธา** in every one — programmatic check found **zero** mismatches (1:9, 2:12, 6:3, 6:5, 8:18, 9:6, 13:4, 18:7, 28:5, 37:16, 39:5, 44:6, 45:13, 47:4, 51:15, 54:5, …). Identical to the shipped NT form (Jas 5:4 σαβαώθ). No אֱלֹהֵי צְבָאוֹת variant occurs in Isaiah. **LOCKED** ✓ per `divine_names_table_2026-05.md`. **Severity: GREEN.**

---

## 3. אֲדֹנָי יְהוִה compound + the Sabaoth-compound split — **LOCKED (bare compound) + REVIEW (Sabaoth-compound)**

- **bare אֲדֹנָי יְהוִה ("Lord GOD," 17×)** → **องค์พระผู้เป็นเจ้า** (Adonai dropped) in every occurrence (7:7, 25:8, 28:16, 30:15, 40:10, 48:16, 49:22, 50:4/5/7/9, 52:4, 56:8, 61:1/11, 65:13/15) — exactly the 2026-05-23 mid-sentence appositional sub-rule, which forward-protects these very Isaiah verses by name. **LOCKED** ✓.
- **אֲדֹנָי יְהוִה צְבָאוֹת ("Lord GOD of hosts," 7×)** — **inconsistent.** 5 drop Adonai (→ องค์พระผู้เป็นเจ้าจอมโยธา: **3:15, 10:23, 22:5, 22:12, 28:22**); 2 mark it (→ **องค์เจ้านาย** องค์พระผู้เป็นเจ้าจอมโยธา: **22:14b, 22:15**), both in the ch.22 Shebna oracle. Verified against the Hebrew — all seven are the אֲדֹנָי יְהוִה צְבָאוֹת triple-stack (22:14 also opens with a *plain* יְהוָה צְבָאוֹת → องค์พระผู้เป็นเจ้าจอมโยธา, correctly distinguished within the verse).

**REVIEW:** Normalize the two ch.22 outliers (22:14b, 22:15) to **องค์พระผู้เป็นเจ้าจอมโยธา** for corpus-uniform mid-sentence rendering (the `divine_names_table` sub-rule drops Adonai in this position), **OR** — if the triple-stack should be preserved — prepend องค์เจ้านาย to the other five. Lean toward the former (matches the bare-compound 17× behavior and the table sub-rule). **Severity: LOW-MEDIUM** (visible only to a reader tracking the Shebna oracle, but an internal inconsistency).

---

## 4. Bare/standalone אֲדֹנָי (divine vs human) + the 6 soft warnings — **LOCKED (and all 6 warnings are false positives)**

- **Divine bare אֲדֹנָי (22×)** → **องค์เจ้านาย** (prayer-vocatives 6:11, 38:14, 38:16 → **ข้าแต่องค์เจ้านาย** per the 2026-05-18 vocative-interjection sub-rule). All correct (3:17/18, 4:4, 6:1/8/11, 7:14, 7:20, 8:7, 9:8, 9:16, 10:12, 11:11, 21:6/16, 28:2, 29:13, 30:20, 37:24, 38:14/16, 49:14).
- **Human "lord/master" (the 6 `check_divine_names` soft warnings)** — **all false positives, all correct.** Verified against Hebrew + BSB: **21:8** (the lookout's "my lord"), **22:18 / 24:2** (suffixed human "his master"), **36:8 / 36:9 / 36:12** (Rabshakeh's "my lord/master the king of Assyria"). All render นาย/เจ้านาย, never the divine องค์เจ้านาย. No genuine divine Adonai was flattened anywhere in the book.

**LOCKED** ✓ per `divine_names_table_2026-05.md` + the 05-15/18/23 sub-rules. *(Light follow-up, corpus-wide: the check conflates single-yodh אֲדֹנִי / suffixed human forms with standalone divine אֲדֹנָי — same false-positive class noted at Daniel 12:8. Worth teaching the check the distinction; it will keep firing in Psalms/Jeremiah.)* **Severity: GREEN.**

---

## 5. צוּר "Rock" / אֲבִיר "Mighty One" / אֵל גִּבּוֹר / הָאָדוֹן — **STABLE**

| Title | Hebrew | Thai | Refs |
|---|---|---|---|
| Rock (divine) | צוּר | (พระ)ศิลา | 8:14, 17:10, 26:4, 30:29, 44:8, 51:1 (non-divine צוּר/בְּצוּרָה at 2:10/15, 25:2, 27:10 correctly *not* ศิลา) |
| Mighty One of Israel | אֲבִיר יִשְׂרָאֵל | องค์ผู้ทรงอานุภาพแห่งอิสราเอล | 1:24 |
| Mighty God | אֵל גִּבּוֹר | พระเจ้าผู้ทรงฤทธิ์ | 9:5, 10:21 (identical surface at both — the lock that drives the §6 divine-child reading) |
| the Lord (article) | הָאָדוֹן | องค์เจ้านาย | 1:24, 3:1, 10:16, 10:33, 19:4 (human אֲדֹנִים קָשֶׁה at 19:4 correctly "นายผู้แข็งกร้าว") |

All uniform. None is named in a corpus doc; אֵל גִּבּוֹר/הָאָדוֹן could be folded into `divine_names_table`. **STABLE.** **Severity: LOW.**

---

## 6. Messianic / Christological surface policy (7:14, 9:5-6, 11:1-10, the Servant Songs, 53, 61:1-2) — **DECIDE (the headline; ratify the committal-surface stance + reconcile Daniel 9:25)**

This is the editorial heart of the book and the highest reviewer-visibility material in the OT. The finding: **Isaiah is internally exemplary and 100% consistent** — at every messianic fork it takes the **committal evangelical-consensus reading in the main text** and keeps **descriptive, non-endorsing notes**, exactly per `RULES.md §0` ("prefer the editorial choice that aligns with the modern evangelical critical-text consensus"; "notes should describe… not pastorally endorse") and the shipped **Gen 3:15** protoevangelium precedent (`gender_passages §2.5`: surface ผู้นั้น "intentional per the project's evangelical-Protestant canonical posture; the footer keeps the manuscript-level question visible").

| Crux | Hebrew | Thai (main text) | Register | Stance |
|---|---|---|---|---|
| **7:14** | עַלְמָה / עִמָּנוּ אֵל | **หญิงพรหมจารี** ("virgin") + อิมมานูเอล | child plain | committal surface; `thai_literal` keeps "หญิงสาว"; KD documents almah/παρθένος + Matt 1:23 + the MT "she"/LXX "they" person-split |
| **8:8, 8:10** | עִמָּנוּ אֵל | โอ้ อิมมานูเอล (8:8); เพราะพระเจ้าทรงสถิตกับเรา (8:10, = shipped Matt 1:23 gloss) | — | name→clause modulation, well-noted |
| **9:5-6** | פֶּלֶא יוֹעֵץ / **אֵל גִּבּוֹר** / אֲבִי־עַד / שַׂר־שָׁלוֹם | ที่ปรึกษามหัศจรรย์ / **พระเจ้าผู้ทรงฤทธิ์** / พระบิดานิรันดร์ / องค์สันติราช | ท่าน in birth-frame → full royal พระองค์/ทรง in reign-frame | committal; אֵל גִּבּוֹר **locked identical to the undisputed-divine 10:21**; summary names Christ (see flag) |
| **11:1-10** | חֹטֶר/נֵצֶר / שֹׁרֶשׁ יִשַׁי | หน่อ / แขนง / รากแห่งเจสซี (byte-harmonized to shipped Rom 15:12) | ท่าน → royal พระองค์ as office begins (mirrors 9:5→9:6) | sevenfold Spirit-rest נָחָה→จะสถิต per `spirit_of_yhwh` (rest, not the Judges' episodic rush); Matt 2:23 nēṣer pun noted as reception |
| **Servant Songs** (42, 49, 50, 52:13–53:12) | עֶבֶד | **ผู้รับใช้** (uniform) | **plain throughout** (ข้าพเจ้า / เขา; confessors' ท่าน = deference, not royalty) | Israel-servant (41:8-9, 44:1-2/21, 45:4, 49:3) and individual-servant (49:5-6, 53) share one surface; the riddle is **preserved** in the KDs, not flattened |
| **53** (incl. 53:11 light) | — | suffering figure plain ปาก/มือ (where the NT uses royal พระโอษฐ์/พระหัตถ์ for Christ, Isaiah keeps plain + documents the register difference) | plain | every crux LOCKED; **53:11 follows the DSS/LXX "light" reading** (เห็นแสงสว่างแห่งชีวิต) via BSB, fully footnoted (§8) |
| **61:1-2** | רוּחַ אֲדֹנָי יְהוִה / מָשַׁח | พระวิญญาณ…สถิตอยู่เหนือข้าพเจ้า / ทรงเจิม | first-person plain | best Luke-4 harmonization in the book: byte-shared where Luke follows the surface, `textual_variants` footer where Luke follows LXX (פְּקַח־קוֹחַ), even the Isa 58:6 splice in Luke's citation flagged |

**The register gradation is principled, not mechanical:** reigning-king figures get royal ทรง/พระองค์ (9:6, 11:3+, 32:1, 33:17); the Servant and David-as-witness (55:4, plain เขา) deliberately do **not** — the translation neither pre-royalizes the Servant nor flattens the Israel/individual ambiguity. This will withstand both evangelical and academic review.

**Why this is nonetheless a DECIDE (two things need Ben's explicit blessing before sealing the OT's most-scrutinized book):**

1. **The 9:6 `thai_summary` is the one line that pushes on RULES §0.** It reads *"พระนามสี่ชั้นเกินกว่ากษัตริย์มนุษย์คนใดจะแบกได้ … **คริสตจักรอ่านพระนามเหล่านี้สำเร็จในพระเยซูคริสต์**"* ("…the church reads these names fulfilled in Jesus Christ"). It is framed descriptively ("the church reads…"), matching the Gen 3:15 construction, so I judge it **compliant** — but it is the single most doctrinally-forward summary in the book, and a reviewer who wants strict §0 neutrality in `thai_summary` (vs `notes`) would point here. Confirm it stands.
2. **Cross-book asymmetry with Daniel 9:25-26.** The Daniel audit rendered מָשִׁיחַ **generically** (ผู้ถูกเจิม) with non-committal notes and flagged it REVIEW. Against Isaiah's committal surface + the Gen 3:15 precedent + RULES §0, **Daniel now looks like the under-committed outlier.** A Thai evangelical reviewer reading Isaiah 9/53 then Daniel 9 will see the gap. **Decide:** either revisit Dan 9:25-26 toward the committal surface, or articulate why Daniel's near-horizon מָשִׁיחַ is treated differently.

**Severity: MEDIUM-HIGH** (theological; highest reviewer-visibility in the OT). The strongest external-AI question. **No Isaiah edit is implied** — this is policy ratification + a Daniel-side decision.

---

## 7. Servant Songs / עֶבֶד — Israel-vs-individual identity — **LOCKED**

Covered in §6's table; recorded separately because it is the most argued question in Isaiah scholarship. **עֶבֶד is uniformly ผู้รับใช้**, plain register everywhere; the corporate-Israel servant (41:8-9; 44:1-2/21; 45:4) and the individuated servant (49:5-6; 53) carry the **same surface**, with the distinction held entirely in the `key_decisions` (49:3 KD: *"named Israel in v.3 yet SENT TO Israel in v.5 — the corporate-and-singular both held"*; 49:5 KD: *"the individuation undeniable here"*). This is the most defensible possible handling — no pre-royalizing, no flattening. **LOCKED** ✓ per `ot_register_policy §1.5`. **Severity: GREEN.**

---

## 8. Isaiah 53 + the 53:11 "light" textual variant — **LOCKED**

Every verse read. The suffering figure stays plain (ปาก/มือ); where the NT quotes a verse with royal Christ-honorifics, Isaiah keeps plain and documents the register difference. Cruxes all disposed correctly: 53:4 נָשָׂא → แบกรับ (KD: Matt 8:17 quotes the **Hebrew** not LXX); 53:5 מְחֹלָל → ถูกแทง; 53:7 lamb (MT שֶׂה/רָחֵל two-word distinction preserved vs LXX/Acts 8:32 single "lamb"); 53:8 MT followed with the Acts 8:33 LXX divergence in the footer; 53:10 אָשָׁם → เครื่องบูชาไถ่ความผิด (Lev-5 sacrificial lock); 53:12 → Luke 22:37 byte-shared (Mark 15:28 correctly noted as a later interpolation the project's Mark omits).

**53:11 "light" — confirmed (cross-validated by two independent agents):** the Thai follows the **DSS + LXX reading** (เห็นแสงสว่างแห่งชีวิต), via BSB, with a full `output/textual_variants/isaiah_53.json` v.11 entry naming **1QIsaᵃ, 1QIsaᵇ, 4QIsaᵈ + LXX** against the MT lacuna, plus the resurrection reading. This is the evangelical-consensus choice, correctly disposed as Tier-1 textual information and honoring the `mt_vs_lxx` Tier-4 DSS-elevation lock. **LOCKED** ✓. Carries one minor REVIEW (53:1 retro-candidate, §10). **Severity: GREEN.**

---

## 9. OT→NT cross-quotation harmonization (~85 quotations) — **STABLE → REVIEW (footnote-apparatus cleanup)**

Isaiah is the most-quoted OT book in the NT, and all of that NT is shipped. The **thread itself is essentially LOCKED**: lemma-locks hold across the NT loci, marquee verses (6:9-10, 40:3-5, 28:16, 45:23, 53 cluster, 61:1-2, 7:14) are **byte-shared on the quoted core**, and the `ot_nt_cross_quotation_thread` policy ("MT surface + shared vocabulary + documented Greek shift") is applied consistently. Footers are present and correct at 28:16, 40:3, 52:15, 53:8, 55:3, 59:20, 61:1, 64:3.

**What blocks a clean LOCK (REVIEW): ~7 NT-cited MT/LXX (Category-B) divergences lack the policy-mandated `textual_variants` Layer-2 footer**, even though the `key_decisions` assert the divergence:
- **25:8** (forever/victory; → 1 Cor 15:54 / Rev 7:17,21:4) — KD says "documented" but isaiah_25 carries only the YHWH entry — **a broken reference.**
- **9:1** (MT "walk in darkness" vs Matt 4:15-16); **11:10** (MT "seek" vs Rom 15:12 "hope"); **29:13-14** (→ Matt 15 / 1 Cor 1:19); **42:1/42:4** (uphold vs beloved; torah vs name → Matt 12:18-21); **45:23** (swear vs confess → Rom 14:11 / Phil 2:10-11); **65:1-2** (LXX reorder → Rom 10:20-21).

The main-text Thai is correct MT-adherence in every case — this is **apparatus, not translation defect** — but the policy requires a reader-facing footer for NT-cited divergences. **Recommend** adding the ~7 footers (and fixing the 25:8 broken reference) before sealing the book. **Severity: LOW-MEDIUM.**

---

## 10. NT-side retro-candidates — **REVIEW (staged NT re-audit)**

Places where the shipped OT and NT surfaces disagree and would jar a comparing reader (the project's "retro-candidate" path, already used for Deuteronomy):

- **RC-1 (translator self-flagged): 53:1 พระกร vs John 12:38 พระหัตถ์.** Same זְרוֹעַ/βραχίων "arm." Isaiah 53:1 = "และ**พระกร**ขององค์พระผู้เป็นเจ้า…"; shipped John 12:38 = "และ**พระหัตถ์**…". The 53:1 KD explicitly records this as a retro-candidate to align at the end-of-book check. (Secondary split in the same verse: Isaiah *เชื่อสิ่งที่เราได้ยินมา* = Rom 10:16, vs John 12:38 *เชื่อสารของเรา*.) **The NT-side fix is owed.** Note this also intersects §13 (the arm anthropomorphism).
- **RC-2: 56:7 นิเวศ vs Matthew 21:13 บ้าน.** "House of prayer": Isaiah / Mark 11:17 / Luke 19:46 = **นิเวศ**แห่งการอธิษฐาน (Mark byte-identical to Isaiah); shipped **Matthew 21:13 = บ้าน** (colloquial) — Matthew is the outlier. Plus "den": Matt ซ่อง vs Mark/Luke ถ้ำ. NT-internal.
- **RC-3: 8:14 / 28:16 NT-internal stone drift.** צוּר מִכְשׁוֹל / πέτρα σκανδάλου rendered three ways (Isa โขดหินแห่งการล้ม / Rom 9:33 หินแห่งการกีดกั้น / 1 Pet 2:8 หินแห่งเหตุสะดุด); 28:16 "not be shamed": Rom 9:33/10:11 ผิดหวัง vs 1 Pet 2:6 อับอาย. Both KD-flagged for the end-of-book audit. NT-side.

These are **NT-corpus edits, not Isaiah edits.** **Recommend** a staged NT re-audit pass (the Deuteronomy precedent) to reconcile RC-1/2/3. **Severity: LOW-MEDIUM.**

---

## 11. Textual variants / DSS — **LOCKED (minor footer-asymmetry REVIEW)**

MT is the surface base throughout; DSS adoptions name the witnesses; LXX/NT divergences get MT-surface + footer. Catalog (representative):

| Ref | Variant | Witnesses | Thai follows | Disposition |
|---|---|---|---|---|
| 53:11 | +"light" | MT vs 1QIsaᵃ/ᵇ + 4QIsaᵈ + LXX | DSS/LXX (แสงสว่างแห่งชีวิต) | Tier-2 footer ✓ |
| 33:8 | cities vs witnesses | MT vs 1QIsaᵃ | 1QIsaᵃ (พยาน) | Tier-2 footer ✓ (model entry; cross-refs 19:18/21:8) |
| 21:8 | lion vs lookout/seer | MT vs 1QIsaᵃ | 1QIsaᵃ (ผู้เฝ้ายาม) | **KD only** |
| 19:18 | City of Destruction vs City of the Sun | MT vs 1QIsaᵃ + Symmachus | 1QIsaᵃ (นครแห่งดวงอาทิตย์) | **KD only** |
| 52:15 | sprinkle vs startle | MT vs LXX | startle (ตะลึงพรึงเพริด) | Tier-2 footer ✓ |
| 53:8, 40:3, 28:16, 55:3, 59:20, 61:1, 64:3 | NT-cited MT/LXX | — | MT surface | Tier-2 footers ✓ |
| 42:8 | the Name surfaced *as a name* | MT | "นามของเราคือยาห์เวห์" | Layer-1 special ✓ (the one place the Name surfaces) |

Every `textual_variants` file carries the Layer-2 YHWH first-occurrence footnote; ch.15 & 46 correctly fileless (no Tetragrammaton). Fully compliant with `mt_vs_lxx_textual_variant_handling` + `ot_canon_and_text_base`.

**REVIEW (minor):** **footer asymmetry within the Qumran cluster** — 33:8 + 53:11 (reader-affecting DSS adoptions) earned Tier-2 footers; **21:8 + 19:18 are KD-only**, yet the 33:8 footer itself names "19:18; 21:8; 23:10" as established cluster practice. Both 21:8 and 19:18 change the reader-visible word (lookout not lion; Sun not Destruction). Add the two footers, or affirm KD-level suffices for this class. **Severity: LOW.**

**14:12 הֵילֵל "Day Star":** rendered **ดาวรุ่ง โอรสแห่งรุ่งอรุณ** (morning star), Babylon-king as primary referent, with the Luke 10:18 / Rev 12 Satan-fall tradition documented **descriptively** per RULES §0. Not a witness-variant (no MT-vs-DSS fork), so no footer owed — correctly handled. **STABLE.**

---

## 12. Versification (MT vs English/BSB) — **LOCKED**

The project uses MT numbering. Isaiah has exactly two divergence zones; **both are registered** in `versification_map.json` (33 ISA entries total) with `diverges:true` and the `check_versification_anchor.py --book ISA` anchor passes (exit 0, 1,371 map entries):

- **Zone 1 — 8:23 / ch.9 offset** (commit `6349827c`): `ISA-8-23` anchor (MT 8:23 = Eng 9:1) + `ISA-9-1…20` each MT n = Eng n+1.
- **Zone 2 — 63:19 / 64 offset** (commit `6c4e0e3b`): `ISA-63-19` anchor (MT 63:19 = Eng 63:19 + 64:1, "rend the heavens") + `ISA-64-1…11` each MT n = Eng n+1.

A verse-count sweep of all 66 chapters against standard English found **no unregistered divergence** — the only count differences (ch.8: MT 23/Eng 22; ch.9: MT 20/Eng 21; ch.64: MT 11/Eng 12) are all inside the two registered zones. Verse-level notes present at all four boundary verses (8:23, 9:1, 63:19, 64:1). Both map commits are in git history (the "versification map ship gotcha" — `ship_chapter.sh` doesn't stage the map — was handled manually). **LOCKED** ✓. **Severity: GREEN.** *(This is the cleanest major-prophet versification state to date — contrast Daniel, whose three zones were unregistered at audit.)*

---

## 13. Divine anthropomorphism — arm + Spirit Rachasap drift — **REVIEW / DRIFT (the one mechanical fix best done before tag)**

`divine_anthropomorphism_thai_grammar_2026-05.md` locks the divine **arm** זְרוֹעַ → **พระกร** and the divine **Spirit** רוּחַ → **พระวิญญาณ** (§2.1: "an established corpus-lock"). Most body-parts are clean (40:5 mouth → พระโอษฐ์; 59:1 hand → พระหัตถ์ + ear → พระกรรณ; 62:8 right hand → พระหัตถ์ขวา; 66:14 → พระหัตถ์). **Two locked terms drift to plain register on divine referents** — verified directly against the JSON:

**13a. Divine "arm" זְרוֹעַ:**
- **พระกร (correct):** 30:30, 40:10, 40:11, 52:10, 53:1, 59:16, 62:8, 63:12
- **แขน (DRIFT, plain, divine referent):**
  - **51:5** "…**แขน**ของเรา…หวังใน**แขน**ของเรา" (YHWH speaking; KD even names "the 40:10 ruling-arm theology")
  - **51:9** "…**แขน**แห่งองค์พระผู้เป็นเจ้าเอ๋ย…" — sits **one column from 52:10's พระกร** in the same "bared holy arm" Servant-thread
  - **63:5** "…**แขน**ของเราเองจึงนำความรอดมา…" — **structurally identical to 59:16's พระกร** ("his own arm brought salvation")

**13b. Divine "Spirit" רוּחַ:**
- **พระวิญญาณ (correct):** 11:2, 32:15, 61:1, 63:10, 63:11, 63:14
- **วิญญาณ (DRIFT, plain) for 1st-person "my Spirit" רוּחִי:** **42:1** ("เราได้วาง**วิญญาณ**ของเราไว้เหนือเขา" — and the Servant Song quoted at Matt 12:18), **44:3** ("เราจะเท**วิญญาณ**ของเรา"), **59:21** ("**วิญญาณ**ของเราซึ่งอยู่เหนือเจ้า")

**The pattern is systematic: 1st-person divine speech ("my arm/my Spirit") triggers the lapse to plain register** on a term the corpus has locked to Rachasap. This is the loudest mechanical finding in the audit and is mechanically fixable. **Recommend a block-tag normalization before v1:** arm 51:5/51:9/63:5 → พระกร; Spirit 42:1/44:3/59:21 → พระวิญญาณ. Forward-protect Jeremiah/Ezekiel (heavy outstretched-arm + Spirit). Note 51:9/53:1 also intersects RC-1 (§10). 66:1 "footstool" (הֲדֹם רַגְלַי → ที่รองเท้าของเรา) is acceptable (feet absorbed into furniture-idiom) — a soft note, not drift. **Severity: MEDIUM** (corpus-lock violation; load-bearing verses).

---

## 14. חֶסֶד covenant-love — **LOCKED**

חֶסֶד → **ความรักมั่นคง** fires correctly: 16:5, 54:8 (นิรันดร์), 54:10, 55:3 (Davidic), 63:7 (×2). The **40:6** case is a documented *non-fire*: MT ḥasdô = mortal flesh's loveliness (ironic), LXX/1 Pet 1:24 read δόξα → rendered **ความงามยั่งยืน** to harmonize with shipped 1 Pet 1:24; the chesed doc itself flags 40:6 as the "glory" crux, and the lock correctly does not fire on a non-divine-covenant use. **LOCKED** ✓. **Severity: GREEN.**

---

## 15. exod-34 attribute formula — **N/A (correct)**

Isaiah never recites the Sinai character-formula. At 63:7-9 only scattered attribute *vocabulary* appears (חֶסֶד, רַחֲמִים, טוּב) — none of the diagnostic 3+ cluster (חַנּוּן / רַחוּם / אֶרֶךְ אַפַּיִם / רַב־חֶסֶד together). Per `exod_34_attribute_formula_2026-05.md`'s hard-fail trigger, the formula lock should not fire — and it does not. **N/A (correct).** **Severity: GREEN.**

---

## 16. "I am YHWH / I am he" self-declaration (chs 40–48) — **LOCKED (minor apposition note)**

Isaiah is the OT's densest cluster of these. **אֲנִי יְהוָה → เราคือองค์พระผู้เป็นเจ้า** at 45:5, 45:6, 45:18. **אֲנִי הוּא "I am he" → เราคือผู้นั้น** uniformly at 41:4, 43:10, 43:13, 48:12, 52:6 (the formula `i_am_yhwh_holiness_formula` does not lexically lock "I am he," but it is internally uniform and echoes the Johannine ἐγώ εἰμι). **LOCKED** ✓. *Minor:* 41:4/45:7 use the no-copula apposition "เรา องค์พระผู้เป็นเจ้า" for plain אֲנִי יְהוָה; the doc's §5 sanctions the no-copula form only for a קָדוֹשׁ-fronted clause. Stylistically defensible (mid-sentence appositive) but worth a glance. **Severity: LOW.**

---

## 17. נחם "comfort" (chs 40–66) — **N/A for the relenting-lock (correct); comfort leitwort clean**

All Isaiah occurrences are Pi'el נחם "comfort/console" — which `nicham_divine_relenting_2026-05.md §1.4` explicitly excludes from the Niph'al relenting/grief lock. The relenting lock correctly does not fire; **ปลอบโยน** is sustained verbatim across 40:1, 49:13, 51:3 (×2), 51:12, 52:9, 57:18, 61:2, 66:13. No "relent" sense occurs in Isaiah. **N/A (correct); the comfort-leitwort is independently LOCKED-clean** per `leitwort_handling_policy`. **Severity: GREEN.**

---

## 18. רוּחַ YHWH empowerment — **LOCKED (verb-handling); see §13 for the Rachasap-form drift**

The Judges-era 4-way verb-split (הָיָה/לָבַשׁ/פָּעַם/צָלַח) is N/A — Isaiah uses different verbs (נוח "rest" 11:2, ערה/יצק "pour" 32:15/44:3, נתן "give" 42:1), all contextually apt. 11:2's נָחָה→**จะสถิต** (rest/permanent) is correctly distinguished from the Judges' episodic rush. The **63:10-11 "Holy Spirit"** (רוּחַ קָדְשׁוֹ) → **พระวิญญาณบริสุทธิ์ของพระองค์** — handled distinctively and well. **LOCKED** ✓ on verb-handling. *(The divine-name/Rachasap **form** of רוּחַ — พระวิญญาณ vs plain วิญญาณ — is the §13 drift.)* **Severity: GREEN** (here; §13 carries the drift).

---

## 19. מַלְאַךְ YHWH "angel of the LORD" — **LOCKED**

- **37:36** (the angel strikes 185,000 Assyrians) מַלְאַךְ יְהוָה → **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** ✓ exact lock.
- **63:9** "angel of his presence" מַלְאַךְ פָּנָיו → **ทูตสวรรค์เบื้องพระพักตร์ของพระองค์** ✓ (locked head-noun + presence qualifier per §4.1; no bare ทูต drift).

**LOCKED** ✓ per `malak_yhwh_2026-05.md` (the locked rendering matches `reference_malakh_yhwh_render`). *Note: Isaiah is not yet in the `check_phrase_consistency.py` `malak` enforcement scope — passes by convention; widening the scope to Isaiah is a backlog item.* **Severity: GREEN.**

---

## 20. Hebrew oath formulas — **LOCKED (45:23); new-lock candidate (49:18)**

- **45:23** בִּי נִשְׁבַּעְתִּי "by myself I have sworn" (the doc §1.3 lists Isa 45:23 by name) → **เราได้ปฏิญาณโดยตัวเราเอง** — the self-oath formula preserved (minor lexical: ปฏิญาณ vs the doc's สาบาน, both the oath register). ✓
- **49:18** חַי־אָנִי "as I live" → เรามีชีวิตอยู่แน่ฉันใด — **not one of the four formulae** catalogued in `hebrew_oath_formulas_2026-05.md` (raised-hand / hand-under-thigh / by-myself / cairn), so the doc is N/A; rendering is reasonable on its own.

**LOCKED** (45:23). **New-lock candidate:** חַי־אָנִי "as I live" is a recurring divine-oath formula (Num 14:21/28; Ezek ~14×) with no governing doc — flag for the backlog before Jeremiah/Ezekiel. **Severity: LOW.**

---

## 21. Leitwort policy — **LOCKED**

Signature Deutero-Isaiah threads hold: **"do not fear" אל־תירא → อย่ากลัวเลย** (41:10/13/14, 43:1/5, 44:2, 54:4); **Holy One of Israel** (§1); **"new things" חדשות → สิ่งใหม่** (42:9, 43:19, 48:6); **"comfort" → ปลอบโยน** (§17). "Former things" varies lexically (สิ่งที่แจ้งไว้ก่อน / สิ่งในอดีต) but that tracks two distinct Hebrew lemmas + context — within Rule 3 tolerance, not drift. **LOCKED** ✓ per `leitwort_handling_policy_2026-05.md`. **Severity: GREEN.**

---

## 22. פקד "visit/punish" — **LOCKED**

All checked occurrences are sense-4 judgment-visitation → **ทรงลงโทษ** (13:11, 24:21, 24:22, 26:14, 27:1), matching `paqad_visit_attend_2026-05.md`. 26:16 (seek in distress) → แสวงหา (the lemma's non-judgment edge, contextually correct); 27:3 = נצר guard, correctly not treated as paqad. **LOCKED** ✓. *Note: the paqad KDs don't always name the sense (1/2/3/4) the doc's §5 checklist asks for — a metadata/enforcement gap, not a surface drift.* **Severity: GREEN.**

---

## 23. Idol-fabrication polemic (chs 40–48, 44:9-20, 46:1-7) — **STABLE (recommend doc)**

The satire's contempt register is exact and doc-compliant: פֶּסֶל/עָצָב "idol" → **รูปเคารพ**; מַסֵּכָה "molten image" → **รูปหล่อ**; manufactured deity אֵל → **พระ** (lowercase, never พระเจ้า — 44:10/15/17, 45:20, 46:6); idolatrous worship verbs use the non-divine register (กราบไหว้/หมอบกราบ). The deadpan lands — the "won't topple" leitwort (40:20/41:7), the firewood-half/god-half satire (44:15-17), "he feeds on ashes" (44:20). 42:8 correctly contrasts YHWH's glory against the lowercase idols. **No drift.** Compliant with `ot_polytheistic_register` + `pagan_deities`, but the idol-fabrication satire is undocumented as a distinct surface — **recommend** a short doc (or amendment to `ot_polytheistic_register`) since Isaiah 40–48 is the corpus's locus classicus and it forward-compounds into Jeremiah 10 / Habakkuk 2 / Acts 17 / Rom 1. **STABLE.** **Severity: LOW.** *(See §27 for the reader-footnote question.)*

---

## 24. Pagan deities + cosmic/mythic beings — **STABLE + REVIEW (śāʿîr split)**

| Being | Hebrew | Thai | Refs |
|---|---|---|---|
| Bel / Nebo | בֵּל / נְבוֹ | **พระเบล / พระเนโบ** (พระ- prefix per OT pagan-deity rule) | 46:1 |
| Leviathan | לִוְיָתָן | เลวีอาธาน (harmonized to shipped Job 40:25) | 27:1 |
| fleeing/coiling serpent; sea-dragon | נָחָשׁ / תַּנִּין | งูที่เลื้อยหนี / งูที่ขดตัวเลื้อยคด / มังกรแห่งท้องทะเล (KD links Gen 1:21, Rev 12:9/20:2) | 27:1, 51:9 |
| Rahab | רַהַב | ราหับ (harmonized to shipped Job 9:13/26:12) | 30:7, 51:9 |
| Lilith | לִילִית | (นาง)ลีลิท + gloss "ผู้เพ่นพ่านยามราตรี" (transliterated, uncanny preserved) | 34:14 |

Bel/Nebo, Leviathan, Rahab, tannin, Lilith all clean and cross-corpus harmonized.

**REVIEW — שָׂעִיר (goat-demon) split between 13:21 and 34:14:** same demonic-desert lexeme rendered two ways — **13:21** "**ผีปีศาจรูปแพะ**จะโลดเต้น" (demonic; KD cites the Lev 17:7 goat-demon cult-ban + LXX δαιμόνια + Rev 18:2) vs **34:14** "**แพะป่า**ตัวหนึ่งจะร้องเรียกหาเพื่อน" (naturalized to "wild goat"; the 34:14 KD doesn't even flag śāʿîr). 34:14 is the *more* demonically-charged context — it sits in the very clause introducing **Lilith** (which the same verse keeps uncanny). Rendering the satyr beside Lilith as a mundane "wild goat" undercuts the register chosen 21 chapters earlier and contradicts the Lev 17:7 lock. **Recommend** harmonizing 34:14 to ผีปีศาจรูปแพะ, or documenting a deliberate context-split. **STABLE** overall; **REVIEW** on śāʿîr. *(Doc-maintenance: `pagan_deities_2026-04.md` could register Bel/Nebo — the corpus's first occurrence — though the rendering already conforms.)* **Severity: LOW.**

---

## 25. Nations / גּוֹיִם + the OT/NT vocabulary seam — **LOCKED**

**Every** גּוֹי/גּוֹיִם verse renders **ประชาชาติ** ("nations") — 52/52, zero use คนต่างชาติ. The 8 Isaiah verses with คนต่างชาติ all render a *different* lemma — נֵכָר/נָכְרִי/זָר "foreigner/stranger" (1:7, 2:6, 28:11, 56:3/6, 60:10, 61:5, 62:8). So the boundary is clean: **goyim → ประชาชาติ; nekar/zar → คนต่างชาติ.** This confirms the intended **OT ประชาชาติ vs NT คนต่างชาติ** seam relative to `ethnos_2026-04.md`: the Servant Songs' "light to the **nations**" verses are ประชาชาติ even though Acts/Luke re-aim them as คนต่างชาติ — and the KDs document the asymmetry intentionally (42:6 → Luke 2:32; 49:6 → Acts 13:47; 52:15 → Rom 15:21; 60:3 → Rev 21:24; 66:18 → Rev 7:9). This is a model of the intended cosmic-ἔθνη (ประชาชาติ) vs mission-ἔθνη (คนต่างชาติ) split. Nation-name transliterations spot-clean (บาบิโลน, etc.); key-term check confirms it. **LOCKED** ✓. **Severity: GREEN.**

---

## 26. Apocalyptic / eschatological imagery + "new heavens and new earth" — **LOCKED (exemplary forward-harmonization)**

The strongest forward-compounding in the book — the eschatological surface is deliberately byte-harmonized to the shipped NT:

| Isaiah | Thai | Shipped-NT link (KD-documented) |
|---|---|---|
| 25:8 בִּלַּע הַמָּוֶת | **ทรงกลืนความตายเสียเป็นนิตย์** | byte-shared with **1 Cor 15:54** |
| 25:8 wipe away tears | ทรงเช็ดน้ำตาจากทุกใบหน้า | harmonized to **Rev 7:17 / 21:4** |
| 26:19 resurrection | คนตายของพระองค์จะมีชีวิตขึ้น…ผู้อาศัยในผงคลีดิน | harmonized to **Dan 12:2** |
| 27:1 slay the dragon | ทรงประหารมังกรแห่งท้องทะเล | **Rev 12:9 / 20:2** |
| 65:17 / 66:22 new heavens + new earth | **ฟ้าสวรรค์ใหม่และแผ่นดินโลกใหม่** | byte-shared with **Rev 21:1 + 2 Pet 3:13** |
| 65:25 wolf/lamb | byte-identical to shipped 11:6-9 + Gen 3:14 | internal + Genesis |
| 66:24 worm/fire | **หนอน…ไม่รู้ตาย และไฟ…ไม่รู้ดับ** | byte-shared with **Mark 9:48** |

Both new-heavens-and-earth anchors are internally byte-identical and externally byte-shared with Rev 21:1 + 2 Pet 3:13; the dragon uses มังกร consistent with Revelation's δράκων. `therion_beast_apocalyptic_2026-05.md` satisfied (no heavenly-creature-register misuse). **LOCKED** ✓. **Severity: GREEN.**

---

## 27. Polytheistic-register / cosmic-creature reader footnote — **REVIEW**

`ot_polytheistic_register_2026-05.md §3` (per the idol-polemic agent's reading) calls for a per-book first-occurrence Layer-2 footnote explaining the lowercase-deity / rhetorical-incomparable convention. Isaiah's `textual_variants` files carry **only** the Tetragrammaton footnote — **none** carry the polytheistic-register, idol-satire, or cosmic-creature (Leviathan/Rahab/Lilith/Bel-Nebo) orientation; all of that lives in `key_decisions` (reader-invisible). Isaiah is the OT's densest idol-polemic (the doc itself cites "Isa 44–46"). Also ch.46 (Bel/Nebo) has **no** `textual_variants` file (no Tetragrammaton), so it currently has no host for such a note. **REVIEW — confirm the convention:** either (a) add the polytheistic-register + cosmic-creature first-occurrence footnotes (creating an `isaiah_46.json` stub), or (b) formally affirm that the corpus relies on `key_decisions`-only for this register and amend the doc's "once per book" expectation. *(Worth checking whether any prior OT book actually shipped such reader footnotes — if none did, KD-only is the de facto established practice and this is a doc-clarification, not a gap.)* **Severity: LOW-MEDIUM.**

---

## 28. Inherited corpus locks — compliance table

| Doc | ISA evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §2 Sabaoth 60/60; §3 bare Adonai-YHWH 17× + Sabaoth-compound split (REVIEW); §4 bare Adonai 22 divine + 6 human all correct | **LOCKED-with-§3-REVIEW** |
| `goel_kinsman_redeemer_2026-05.md` | §4 — root invariant held (13 title + 6 verb; 59:3 גאל-II → เปื้อน correct); minor พระ-prefix REVIEW | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | §14 — fires correctly; 40:6 documented "glory" non-fire | **LOCKED** |
| `exod_34_attribute_formula_2026-05.md` | §15 — vocabulary present (63:7) but not the formula → correctly does not fire | **N/A (correct)** |
| `i_am_yhwh_holiness_formula_2026-05.md` | §16 — chs 40-48 dense; เราคือองค์พระผู้เป็นเจ้า / เราคือผู้นั้น uniform; 41:4/45:7 apposition note | **LOCKED** |
| `nicham_divine_relenting_2026-05.md` | §17 — all Pi'el "comfort" → ปลอบโยน; relenting-lock correctly N/A | **N/A (correct)** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §18 — 11:2 rest vs Judges-rush; 63:10 Holy Spirit; (Rachasap-form drift → §13) | **LOCKED** |
| `malak_yhwh_2026-05.md` | §19 — 37:36, 63:9 exact lock | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | §13 — arm พระกร + Spirit พระวิญญาณ **drift** (51:5/51:9/63:5; 42:1/44:3/59:21) | **DRIFT (REVIEW)** |
| `hebrew_oath_formulas_2026-05.md` | §20 — 45:23 LOCKED; 49:18 חַי־אָנִי N/A (new-lock candidate) | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | §21 — do-not-fear / Holy One / new things / comfort all sustained | **LOCKED** |
| `paqad_visit_attend_2026-05.md` | §22 — sense-4 judgment consistent | **LOCKED** |
| `ot_register_policy_2026-05.md` | §6/§7 — messianic-figure register gradation principled; Servant plain (§1.5) | **LOCKED** |
| `ot_polytheistic_register_2026-05.md` | §23 idol-satire register exact; §24 lowercase pagan deities; §27 reader-footnote REVIEW | **LOCKED-with-§27-REVIEW** |
| `pagan_deities_2026-04.md` | §24 — Bel/Nebo พระ- correct (register Bel/Nebo in the table) | **LOCKED** |
| `ethnos_2026-04.md` | §25 — goyim→ประชาชาติ 52/52; OT/NT seam clean + documented | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling` + `ot_canon_and_text_base` | §11 — MT base + DSS-elevation + Category-B footers; §9 ~7 missing footers | **LOCKED-with-§9-REVIEW** |
| `ot_nt_cross_quotation_thread_2026-05.md` | §9/§10 — quoted cores byte-shared; footer gaps + retro-candidates | **STABLE→REVIEW** |
| `verse_schema_and_versification_2026-05.md` | §12 — both zones registered, anchor passes, no unregistered divergence | **LOCKED** |
| `therion_beast_apocalyptic_2026-05.md` | §26 — มังกร consistent with Rev δράκων | **LOCKED** |
| `son_of_man_disambiguation_2026-04.md` | N/A — no בֶּן־אָדָם title use in Isaiah (the generic 51:12, 56:2 "son of man" = mortal-man, plain) | **N/A** |

---

## 29. Mechanical (§1)

- **66/66** chapters: `output/check_reports/isaiah_NN_review.md` (green) + `output/back_translations/isaiah_NN.json` + `output/translations/isaiah_NN.json` ✓
- **64/66** chapters: `output/textual_variants/isaiah_NN.json` carrying the YHWH first-occurrence footnote; **ch. 15 & 46 correctly fileless** (neither contains the Tetragrammaton — verified). Divine-name footnote coverage is complete.
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings.**
- `check_phrase_consistency.py`: **0 violations across 38 audited locks** (27,250 verses).
- `audit_inclusion_variants.py --book isaiah --strict`: **0 candidates, exit 0.**
- `check_divine_names.py --book ISA`: **exit 0**; 6 soft warnings (21:8, 22:18, 24:2, 36:8/9/12) **all confirmed false positives** (human lords, §4).
- `check_versification_anchor.py --book ISA`: **exit 0**; both divergence zones registered (§12).
- `git status output/`: only re-ran-check artifacts (`phrase_consistency.md`). No source-file dirt. The `versification_map.json` is **not** dirty and **should not be** — both ISA zones already registered (contrast Daniel).
- **`export_to_usfm.py --book ISA`: FAILS — "Unknown book code: ISA."** The script's `BOOKS` table does not carry `ISA` (the same OT-USFM/book-code-registration gotcha logged for LAM/SNG and noted in every prior OT audit). **Non-blocking infra gap** — flagged for the maintainer to register `ISA` in the export script's book table; not a translation defect.
- **Book-code registration for §3 tooling:** `build_external_review_packet.py`'s `BOOKS` dict was **missing `ISA`** (it stopped at `JOB`) — **registered as part of this audit** (`"ISA": ("isaiah", "Isaiah")`), the same fix the Daniel audit applied for `DAN`. `audit_items_to_yaml.py` already carried `"ISA": "isaiah"`. **PSA/PRO/ECC/SNG/LAM are also still missing from that `BOOKS` dict** — a standing carry-forward the maintainer may want to backfill.

**Severity: GREEN on the consistency + versification + inclusion gates; two infra items (USFM export, packet `BOOKS` table) are tooling, not translation.**

---

## 30. Flagged for Ben's attention

### DECIDE (blocks the `book-isaiah-v1` tag until resolved)

**A. Messianic committal-surface policy + Daniel reconciliation (§6).** Isaiah is internally exemplary — committal evangelical-consensus surface (7:14 virgin; 9:5 Mighty God locked to the undisputed-divine 10:21; 53:11 DSS "light") + descriptive non-endorsing notes, per RULES §0 + the Gen 3:15 precedent; the Servant kept plain. **Two confirmations owed before sealing the OT's most-scrutinized book:** (1) the 9:6 `thai_summary` "the church reads these names fulfilled in Jesus Christ" — the most doctrinally-forward summary line in the book (defensible under the "the church reads…" reception framing, but the one line a strict-§0 reviewer flags); (2) the cross-book asymmetry with **Daniel 9:25-26** (generic ผู้ถูกเจิม, non-committal), which now reads as the outlier — decide whether Daniel is revisited toward the committal surface or its difference articulated. **No Isaiah edit implied.** **MEDIUM-HIGH.**

### REVIEW (worth Ben's confirmation; §13 ideally before tag)

**B. Divine-anthropomorphism Rachasap drift (§13) — the one mechanical fix best done before tag.** Divine **arm** rendered แขน at 51:5/51:9/63:5 (vs locked พระกร, incl. the adjacent 51:9-vs-52:10 and structurally-parallel 63:5-vs-59:16 splits); divine **"my Spirit"** render plain วิญญาณ at 42:1/44:3/59:21 (vs locked พระวิญญาณ). Systematic 1st-person-divine-speech lapse; mechanically fixable. **MEDIUM.**

**C. אֲדֹנָי יְהוִה צְבָאוֹת split (§3).** Normalize 22:14b/22:15 (องค์เจ้านาย-marked) to องค์พระผู้เป็นเจ้าจอมโยธา per the `divine_names_table` mid-sentence sub-rule (or mark the other 5). **LOW-MEDIUM.**

**D. NT cross-quotation footnote gaps + retro-candidates (§9/§10).** Add ~7 missing Category-B `textual_variants` footers (incl. fixing the 25:8 broken reference); schedule the NT-side staged re-audit for RC-1 (53:1 พระกร/พระหัตถ์, self-flagged), RC-2 (56:7 นิเวศ/บ้าน), RC-3 (8:14/28:16). **LOW-MEDIUM.**

**E. Qumran footer asymmetry (§11).** Add Tier-2 footers to 21:8 + 19:18 (KD-only; the 33:8 footer names them as cluster practice), or affirm KD-level suffices. **LOW.**

**F. śāʿîr demonic-register split (§24).** Harmonize 34:14 (แพะป่า, beside Lilith) to 13:21's ผีปีศาจรูปแพะ, or document the split. **LOW.**

**G. Polytheistic-register reader footnote (§27).** Confirm whether reader-facing footnotes are owed (then add; ch.46 needs a host file) or KD-only is the established practice. **LOW-MEDIUM.**

**H. Minor: Holy-One connector 60:14 (§1, ของ→แห่ง); goel พระ-prefix (§4); i_am apposition 41:4/45:7 (§16).** Spot-confirmations. **LOW.**

### New / carry-forward translator_decisions docs recommended

1. **Add `องค์บริสุทธิ์แห่งอิสราเอล` (Holy One of Israel) + `אֵל גִּבּוֹר`/`הָאָדוֹן` rows to `divine_names_table_2026-05.md`** (§1, §5) — Isaiah's signature title is undocumented at corpus level.
2. **Idol-fabrication satire doc** (or amend `ot_polytheistic_register`) (§23) — Isaiah 40–48 is the locus classicus; forward-compounds into Jer 10 / Hab 2 / Acts 17 / Rom 1.
3. **`hebrew_oath_formulas` — add חַי־אָנִי "as I live"** (§20) — recurs in Num/Ezek; owed before Jeremiah/Ezekiel.
4. **Register Bel/Nebo in `pagan_deities_2026-04.md`** (§24) — first corpus occurrence.

### Existing-tooling/scope items (maintainer)
- Register `ISA` in `export_to_usfm.py`'s `BOOKS` table (§29) — plus the standing LAM/SNG/PSA/PRO/ECC backlog.
- Widen `check_phrase_consistency.py` `malak` + the anthropomorphism check scopes to include Isaiah (§13, §19).
- Teach `check_divine_names.py` the single-yodh אֲדֹנִי / suffixed-human distinction (§4) — recurs Psalms/Jeremiah.

### External AI review (§3 of checklist) — pending
Recommended 4-item packet (see `external_review_items_ISA.md`):
1. **Messianic committal-surface policy + Daniel reconciliation** (§6-A, DECIDE)
2. **Divine-anthropomorphism Rachasap drift** (§13-B, REVIEW)
3. **śāʿîr demonic-register split** (§24-F, REVIEW)
4. **NT cross-quotation footnote/retro-candidate cleanup** (§9/§10-D, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/DAN pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 15 (§2 Sabaoth, §4 bare-Adonai, §7 Servant-identity, §8 ch.53/53:11, §12 versification, §14 chesed, §16 I-am-YHWH, §18 spirit-of-YHWH, §19 malak, §20 oath/45:23, §21 leitwort, §22 paqad, §25 nations, §26 apocalyptic, §11 textual-variants)
- **STABLE:** 4 (§1 Holy One of Israel [→ table row], §5 Rock/El-Gibbor/ha-Adon, §23 idol-fabrication satire [→ doc], §24 pagan-deities + cosmic beings)
- **N/A (correct):** 2 (§15 exod-34 formula, §17 nicham relenting)
- **REVIEW:** 8 (§3 Sabaoth-Adonai split, §9 NT footnote gaps, §10 NT retro-candidates, §11 Qumran footer asymmetry, §13 anthropomorphism drift, §24 śāʿîr split, §27 polytheistic-register footnote, §1 Holy-One 60:14 cosmetic)
- **DECIDE:** 1 (§6 messianic committal-surface policy + Daniel reconciliation)

**One DECIDE blocks the `book-isaiah-v1` tag** — and like the recent OT audits it is a **policy ratification + cross-book reconciliation, not a surface defect**: Isaiah's messianic material is internally exemplary; what is owed is Ben's blessing of the committal-surface stance (incl. the borderline 9:6 summary line) and a decision on the Daniel 9:25-26 asymmetry.

**The one mechanical item best fixed before tag is §13** (the arm/Spirit Rachasap drift) — a clean corpus-lock normalization across 6 verses.

**Four new/carry-forward docs recommended** (one is just table rows). **Three tooling/scope items** for the maintainer.

---

## Recommendation

**Isaiah ships in exceptionally strong corpus-hygiene shape — the cleanest major-prophet mechanical state to date.** Both versification zones are registered (contrast Daniel's three unregistered zones), the divine-name architecture is near-perfect (Sabaoth 60/60, bare-Adonai 22 divine + 6 human all correct, no flattened divine Adonai), the messianic/Servant material is the most disciplined theologically-charged corpus in the OT audit history (committal evangelical-consensus surface + rigorously descriptive notes, with the 53:11 DSS-"light" variant correctly followed and footnoted), the NT cross-quotation cores are byte-shared, the idol-polemic register is exact, the goyim/nekar seam is a model OT/NT boundary, and the eschatological "new heavens and new earth" surface is byte-harmonized to the shipped Revelation + 2 Peter.

**The work before v1 is overwhelmingly confirmation + apparatus, with one clean mechanical normalization:**

- **§6 (DECIDE) is the headline and is bigger than Isaiah:** ratify the committal-messianic-surface policy (bless the 9:6 summary line) and reconcile it against Daniel 9:25-26, which now reads as the under-committed outlier. **No Isaiah edit implied.**
- **§13 (REVIEW) is the one mechanical fix best done before tag:** normalize the divine arm (51:5/51:9/63:5 → พระกร) and Spirit (42:1/44:3/59:21 → พระวิญญาณ) to their existing locks — 6 verses, mechanically clean, and it forward-protects Jeremiah/Ezekiel.
- **§3 / §9 / §10 / §11 / §24 / §27 (REVIEW)** are apparatus + small normalizations (Sabaoth-Adonai, NT footers + retro-candidates, Qumran footers, śāʿîr, polytheistic footnote) — none theological, all bounded.
- **Four docs** (Holy-One table row, idol-satire, חַי־אָנִי oath, Bel/Nebo registration) and **three tooling items** (USFM book-code, malak/anthropomorphism check scope, divine-names single-yodh) close the corpus-hygiene loop.

**Tag `book-isaiah-v1` after:**
1. Ben's decision on **§6** (messianic-surface ratification + Daniel reconciliation).
2. **§13** anthropomorphism normalization (the one fix-before-tag) + re-run checks.
3. Ben's confirmation on **§3 / §9–11 / §24 / §27** (apparatus + small normalizations).
4. External AI sanity-check (the 4-item packet).
5. The recommended docs written / table rows added.

**The single highest-value step is §6** — Isaiah is the OT's messianic keystone, and blessing its committal-surface policy now both seals this book and resolves the Daniel asymmetry before Jeremiah/Ezekiel/the Twelve compound it.
