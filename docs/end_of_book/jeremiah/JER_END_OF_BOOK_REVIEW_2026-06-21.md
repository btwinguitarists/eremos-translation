# Jeremiah — End-of-Book Review

**Date:** 2026-06-21
**Scope:** All 52 chapters of Jeremiah (1,364 verses); `glossary.json`; `docs/translator_decisions/` corpus (97 docs). **The second-largest book in the corpus after Isaiah, and the OT's single largest MT-vs-LXX divergence** — the LXX of Jeremiah is ~1/8 (≈2,700 words) shorter than the MT and relocates the Oracles Against the Nations (chs 46–51 in MT) to after 25:13 with a different internal order. The project follows the MT surface throughout. Jeremiah is also the source of the new-covenant oracle (31:31–34, quoted at the greatest length of any OT passage in the NT, Heb 8:8–12 + 10:16–17), the Rachel-weeping oracle (31:15 → Matt 2:18), the "den of robbers" (7:11 → the Synoptic temple cleansing), and the "boast in the LORD" oracle (9:23–24 → 1 Cor 1:31 / 2 Cor 10:17). All of the NT it cross-quotes is **already shipped**.
**Trigger:** JER 52 shipped (commit `9f9e05d9`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **28 cross-cutting items reviewed.** Mechanical gates (§1) pass: 52/52 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks, 28,613 verses); `audit_inclusion_variants.py --book jeremiah --strict` = **0 candidates, exit 0**; `check_divine_names.py --book JER` = exit 0 with **2 soft warnings, both confirmed false positives** (human "my lord the king," §3); `check_versification_anchor.py --book JER` = exit 0. **52/52** chapters carry a `textual_variants` YHWH first-occurrence footnote (complete coverage — the cleanest footnote state of any major OT book). Two infrastructure items surfaced (§28): `export_to_usfm.py` still rejects `JER` (the recurring OT book-code gotcha), and the JER 8/9 MT/English versification offset is **not yet registered** in `versification_map.json` (translator self-flagged; §12).
- **3 items flagged DECIDE** (Ben choice needed before tagging `book-jeremiah-v1`):
  - **§13 — divine-anthropomorphism register: a *codified* first-person-plain rule.** The loudest finding, and a step beyond Isaiah. `divine_anthropomorphism_thai_grammar_2026-05.md` locks God's body-parts to royal register (ราชาศัพท์): arm זְרוֹעַ → **พระกร**, hand יָד → **พระหัตถ์**, eyes עֵינַי → **พระเนตร**. In Jeremiah, first-person divine speech ("my arm / my hand / my eyes") systematically drops to **plain** register, and — unlike Isaiah, where it was undocumented drift — the lapse is **argued into the `key_decisions` as an intentional rule** (21:5 KD: *"คำพูดบุรุษที่ 1 ของพระเจ้า … ใช้คำส่วนร่างกายแบบ 'ธรรมดา' … ราชาศัพท์สงวนไว้สำหรับการพรรณนาบุรุษที่ 3"*; 27:5 KD: *"ใช้ 'แขน' คำสามัญ ไม่ใช่ราชาศัพท์ พระกร; สม่ำเสมอกับ 21:5"*). It produces a **same-idiom split**: "I stretch out my hand against you" is **พระหัตถ์** at 15:6 but **มือ** at 6:12 and 51:25; "outstretched arm" is **พระกร** at 32:17/32:21 (2nd-person address to God) but **แขน** at 21:5/27:5 (1st-person divine speech). It is not even internally consistent (15:6 keeps พระหัตถ์ in a first-person clause). This conflicts with the anthropomorphism doc, which has no person-based exception, and with the Isaiah audit's §13, which recommended **reversal** of the identical drift. **Ben must ratify a documented first-person-plain exception OR reverse the ~7–9 verses to Rachasap — and reconcile the decision with Isaiah §13** (heaviest forward weight: Ezekiel, with its dense outstretched-arm + body-part theophany). See §13.
  - **§24 — foreign-monarch register: Nebuchadnezzar is plain, contradicting Daniel and §2.2.** Across chs 1–51 the king of Babylon receives **plain register**, codified at 21:2 (*"กษัตริย์บาบิโลนผู้รุกราน → ทะเบียนธรรมดา"*) — an "invader → plain" rule with no basis in `ot_register_policy §2.2`, which grants foreign emperors full ราชาศัพท์ *even if villainous*. The already-audited **Daniel gives all four foreign emperors full ทรง**; the **same king Nebuchadnezzar** is therefore plain in Jeremiah but royal in Daniel. Jeremiah also contradicts **itself**: 39:11 gives Nebuchadnezzar **ทรง** (where he protects Jeremiah), and ch.52 (the 2 Kings 25 appendix) gives the Babylonian king Evil-merodach **full royal register** (52:31–32). The `foreign_monarch_register` doc **still does not exist** (deferred since Ezra; flagged in the Ezra/Neh/Esther/Daniel audits as "owed"). **Ben must decide the register, write the doc, reconcile Jeremiah chs 1–51 / ch.52 / 39:11, and resolve jointly with the still-untagged EZR/NEH/EST/DAN block** so shared kings speak with one voice. The "my servant Nebuchadnezzar" עַבְדִּי tension (25:9/27:6/43:10 → ผู้รับใช้ของเรา) is handled well descriptively — but the translator used the servant-instrument framing to *justify* the downshift, which is the crux of the conflict. See §24.
  - **§9 — MT/LXX macro-divergence disclosure is buried in `key_decisions` (not reader-facing).** The MT surface is correctly followed everywhere, but Jeremiah is the OT's largest LXX divergence and **none of it reaches the reader.** Every one of the 52 `textual_variants` files carries **only** the YHWH footnote; there is **no book-level prefatory note** (the §2.2 macro-structural model built for 1 Kings was never applied here) and **zero** chapter-footer anchors for the OAN reorder or the MT-plus passages (10:11, 29:16–20, **33:14–26** — the longest MT plus, the Branch/Davidic-covenant oracle entirely absent from LXX — 39:4–13, 52:28–30). Only 33:14 carries a reader-visible note, via a single inline `thai_summary` line. The sharpest single instance is **31:32**, where Heb 8:9 quotes the **LXX** ("disregarded them") against the MT surface Jeremiah ships ("I was a husband to them") — a flat contradiction for a reader comparing Jer 31:32 ↔ Heb 8:9, and the one NT-cited divergence the `mt_vs_lxx §2.3` floor actually **obligates** a Tier-2 footer for; it is currently KD-only. **Ben must decide whether to apply the policy's own prescribed remedy** (book-level prefatory note at `jeremiah_01` + chapter-footer anchors at 25, 33, 39, 52, and the OAN head 46 + the 31:32 footer) **or formally affirm KD-only disclosure for this book.** See §9.
- **8 items flagged REVIEW** (worth Ben's confirmation):
  - **§3 — אֲדֹנָי יְהוִה צְבָאוֹת + the lone compound drift.** The triple-stack "Lord GOD of hosts" is rendered two ways: **2:19** drops Adonai (→ องค์พระผู้เป็นเจ้าจอมโยธา, the doc-conformant mid-sentence form) but **46:10 (×2), 49:5, 50:25, 50:31** mark it (→ องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านายจอมโยธา). 5 mark, 1 drops — so the outlier is actually the doc-conformant 2:19, which suggests a (possibly intentional) OAN-emphasis convention. Separately, the **חַי־אֲדֹנָי יְהוִה** oath at **44:26** → องค์เจ้านายพระผู้เป็นเจ้า marks Adonai where the bare compound elsewhere drops it. Normalize or document.
  - **§12 — versification: JER 8/9 boundary unregistered.** MT 8:23 = English/BSB 9:1, and all of MT ch.9 = English 9:N+1. The `versification_map.json` has only `JER-10-11`; the offset zone is documented in KDs and **translator-self-flagged** but not in the map. Register it (mind the "ship script doesn't stage the map" gotcha).
  - **§7 — 31:22 crux (נְקֵבָה תְּסוֹבֵב גָּבֶר) has no Layer-2 reader footer.** The "a woman shall encompass a man" crux is handled well in the KD (the historic Marian/messianic reading is named *descriptively*, polysemy preserved per `gender_passages`), but the interpretive note lives only in the KD — inconsistent with the Gen 3:15/3:16 precedent, where each crux earned a reader-facing footer.
  - **§10 — retro-candidate: Matt 21:13 ซ่องของพวกโจร vs Jer 7:11 / Mark 11:17 / Luke 19:46 ถ้ำของโจร.** Jeremiah harmonized "den of robbers" to Mark/Luke; Matthew is the lone Synoptic outlier. NT-side fix (the Jeremiah analogue of Isaiah's 53:1 retro-candidate).
  - **§6 — 23:5 vs 33:15 Branch register asymmetry.** 23:5 gives the Branch full royal (พระองค์/ทรง, where the Hebrew has מָלַךְ מֶלֶךְ "he will reign as king"); 33:15 keeps plain ท่าน (the Hebrew omits the kingship verb). Hebrew-anchored and defensible, but the 33:15 KD does not explain the downshift in the byte-parallel pair.
  - **§6 — confirm the 31:31 "สำเร็จในพระคริสต์" summary.** The new-covenant `thai_summary` reads the oracle as "cited in full in Heb 8 / 10 *as fulfilled in Christ*" — the closest Jeremiah comes to the Isaiah-9:6-flagged endorsement line. Framed as a report of what Hebrews does (descriptive), judged §0-compliant — confirm it stands (parallel to the Isaiah §6 ratification request). Jeremiah is otherwise **cleaner on §0 than Isaiah**.
  - **§20 — בִּי נִשְׁבַּעְתִּי "by myself I have sworn" at 49:13.** 22:5 matches the lock (เราสาบานในตัวของเราเอง); 49:13 drifts to a synonym (เราได้ปฏิญาณด้วยตัวเราเอง). Normalize.
  - **§21 — balm צֳרִי lexical drift.** The "balm in Gilead" leitwort is rendered three ways: ยาสมานแผล (8:22) / ยางรักษาโรค (46:11) / ยาสมาน (51:8). Normalize to one for traceability.
- **STABLE-but-undocumented patterns recommending doc-lift / new locks:** the **Branch/צֶמַח** rendering (§6 — no corpus doc; KD-only; หน่ออันชอบธรรม byte-shares Isaiah 11; **recommend `messianic_branch_tzemach_2026-06.md` before Zechariah 3:8 / 6:12**); **חַי־אָנִי "as I live"** divine self-oath (§20 — the Isaiah-flagged new-lock candidate, now internally consistent in Jeremiah at 22:24/46:18; **formalize into `hebrew_oath_formulas` §1.5**, noting the 1st-vs-3rd-person verb split ทรงพระชนม์ / มีชีวิตอยู่); the **Queen of Heaven** מְלֶכֶת הַשָּׁמַיִם → เจ้าแม่แห่งฟ้าสวรรค์ (§23 — first in the corpus; add to the `pagan_deities` OT table).
- **External AI review (§3) pending.** Suggested 4-item packet: the codified anthropomorphism rule (§13 DECIDE); the Nebuchadnezzar/foreign-monarch register conflict (§24 DECIDE); the MT/LXX disclosure question incl. 31:32 (§9 DECIDE); the new-covenant/Branch committal-surface confirmation (§6/§9 — also tests messianic policy continuity with Isaiah).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. יְהוָה צְבָאוֹת — "LORD of hosts" (Sabaoth) + the Jeremiah-signature expansion — **LOCKED**

Jeremiah is one of the corpus's densest Sabaoth books. **77 occurrences** of base יְהוָה צְבָאוֹת → **องค์พระผู้เป็นเจ้าจอมโยธา** in every one (zero mismatches), identical to the shipped NT form (Jas 5:4 σαβαώθ). The Jeremiah-signature expansion **יְהוָה צְבָאוֹת אֱלֹהֵי יִשְׂרָאֵל ("LORD of hosts, the God of Israel," 32×)** → uniformly **องค์พระผู้เป็นเจ้าจอมโยธาพระเจ้าแห่งอิสราเอล**. Only cosmetic variance: 4 verses write an interior space before พระเจ้า (7:3, 7:21, 9:14, 51:33) — same lemma string, whitespace only. **LOCKED** ✓ per `divine_names_table_2026-05.md`. **Severity: GREEN.**

---

## 2. נְאֻם־יְהוָה / כֹּה אָמַר — the prophetic-formula refrains — **LOCKED**

נְאֻם־יְהוָה ("declares the LORD"), the most frequent formula in the book (~159 verses), → **องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้** with effectively 100% uniformity (a handful carry ตรัสดังนี้ without ไว้ — cosmetic). The four apparent outliers (2:19, 46:18, 49:5, 50:31) correctly carry the epithet the Hebrew itself adds (נְאֻם־יְהוָה צְבָאוֹת → องค์พระผู้เป็นเจ้าจอมโยธาตรัสไว้ดังนี้; נְאֻם־אֲדֹנָי יְהוִה צְבָאוֹת → องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านายจอมโยธาตรัสไว้ดังนี้ — see §3). **LOCKED** ✓. **Severity: GREEN.**

---

## 3. אֲדֹנָי יְהוִה compound + the Sabaoth-stack split — **LOCKED (bare compound) + REVIEW (Sabaoth-stack + 44:26)**

- **Sentence-initial interjection vocatives → ข้าแต่องค์พระผู้เป็นเจ้า** (correct, per the 2026-05-23 vocative sub-rule): 1:6, 4:10, 14:13, 32:17.
- **Mid-sentence appositional bare compound → องค์พระผู้เป็นเจ้า** (Adonai dropped, correct): 2:22, 7:20, 32:25, 44:26(first instance).
- **REVIEW — אֲדֹנָי יְהוִה צְבָאוֹת ("Lord GOD of hosts") rendered two ways.** **2:19** drops Adonai → **องค์พระผู้เป็นเจ้าจอมโยธา** (the doc-conformant mid-sentence form per the Amos `divine_names_table` sub-rule); **46:10 (×2), 49:5, 50:25, 50:31** mark it → **องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านายจอมโยธา**. Since 5 mark and 1 drops, the *outlier is the doc-conformant 2:19* — the consistent pattern is that the Oracles-Against-the-Nations climactic-judgment formulas mark Adonai. This may be an intentional OAN-emphasis convention. **Normalize to one form, or document the OAN split.**
- **REVIEW — 44:26 חַי־אֲדֹנָי יְהוִה oath compound marks Adonai.** The oath "as the Lord GOD lives" → **องค์เจ้านายพระผู้เป็นเจ้า**ทรงพระชนม์อยู่แน่ฉันใด, prepending องค์เจ้านาย where the bare compound elsewhere drops Adonai. Defensible as an audible distinction from the bare חַי־יְהוָה oath (องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่, §20), but it is the one bare-compound occurrence that marks Adonai. Normalize to องค์พระผู้เป็นเจ้า or document the oath-distinction.

**Severity: LOW-MEDIUM** (internal inconsistency visible only to a reader tracking the title-stacks).

---

## 4. Bare divine אֲדֹנָי + the 2 soft warnings — **LOCKED (both warnings false positives)**

No standalone *divine* אֲדֹנָי (outside a compound) occurs in Jeremiah; the divine vocative ข้าแต่องค์เจ้านาย correctly appears nowhere. The 2 `check_divine_names` soft warnings are **both human address, both correct:**
- **37:20** — single-yod `אֲדֹנִי הַמֶּלֶךְ` ("my lord the king"), Jeremiah pleading to King Zedekiah → **ข้าแต่กษัตริย์เจ้านายของข้าพระองค์** — human, correct.
- **38:9** — `אֲדֹנִי הַמֶּלֶךְ`, Ebed-melech to the king → **ข้าแต่กษัตริย์เจ้านายของข้าพระองค์** — human, correct.

Both can be whitelisted. **LOCKED** ✓. *(Same single-yod אֲדֹנִי false-positive class noted at Daniel 12:8 / Isaiah's 6 warnings — the check still conflates suffixed-human forms with standalone divine Adonai; a corpus-wide check-teaching backlog item, not a translation defect.)* **Severity: GREEN.**

---

## 5. YHWH first-occurrence footnote coverage — **LOCKED (complete)**

All **52/52** `output/textual_variants/jeremiah_NN.json` files exist and **all 52 carry the Layer-2 Tetragrammaton first-occurrence footnote** (`type: tetragrammaton_convention_first_occurrence`). Several go further — e.g. `jeremiah_02` documents the אֲדֹנָי יְהוִה compound and the נְאֻם־יְהוָה formula in the same footnote. This is the **cleanest divine-name footnote state of any major OT book** (contrast the Lamentations ch2/ch3 Adonai-footnote gap). **LOCKED** ✓. **Severity: GREEN.**

---

## 6. Messianic / committal surface: the Branch (23:5–6, 33:14–16), 30:9/30:21, 31:22 — **STABLE + REVIEW (register asymmetry; recommend a Branch doc; confirm the 31:31 summary)**

Jeremiah follows the **same committal evangelical-consensus surface + descriptive-notes policy** Isaiah established (ISA §6/§7), and is **cleaner on RULES §0** than Isaiah (no summary carries an Isaiah-9:6-style endorsement clause).

| Crux | Hebrew | Thai (main) | Register | Disposition |
|---|---|---|---|---|
| **23:5** | צֶמַח צַדִּיק | **หน่ออันชอบธรรม** | full royal (พระองค์/ทรงครองราชย์) — Hebrew has וּמָלַךְ מֶלֶךְ | byte-shares หน่อ with the locked Isaiah 11:1; KD cross-refs 33:15; Zech 3:8/6:12; Isa 4:2/11:1 |
| **23:6** | יְהוָה צִדְקֵנוּ | **ยาห์เวห์ซิดเคนู** (องค์พระผู้เป็นเจ้าทรงเป็นความชอบธรรมของเรา) | name-title | exactly the `divine_names_table` lock (translit + gloss) |
| **33:15** | צֶמַח צְדָקָה | **หน่ออันชอบธรรม** | **plain ท่าน** — Hebrew omits מָלַךְ מֶלֶךְ | byte-consistent title; **register downshift unexplained in KD** (REVIEW) |
| **33:16** | יְהוָה צִדְקֵנוּ | ยาห์เวห์ซิดเคนู (same gloss) | name of the *city* (fem. יִקְרָא־לָהּ) | subject-shift correctly flagged in KD |
| **30:9** | דָּוִד מַלְכָּם | …และดาวิดกษัตริย์ของพวกเขา | plain (object) | descriptively names พระเมสสิยาห์; cross-refs Ezek 34:23-24 |
| **30:21** | אַדִּירוֹ / מֹשְׁלוֹ | ผู้นำของเขา / ผู้ครอบครองของเขา | plain | not-yet-reigning future leader — correct per §2.2 |
| **31:22** | נְקֵבָה תְּסוֹבֵב גָּבֶר | ผู้หญิงจะโอบล้อมผู้ชาย | — | polysemy preserved; Marian/messianic reading named **descriptively** in KD; **no Layer-2 reader footer** (REVIEW, §7) |

- **REVIEW — 23:5 vs 33:15 register asymmetry.** The byte-parallel Branch pair differs (royal พระองค์ vs plain ท่าน). The split is **Hebrew-anchored** (kingship verb present in 23:5, absent in 33:15) and mirrors Isaiah's birth-frame/reign-frame gradation, but the 33:15 KD does not explain the downshift; a reviewer comparing the pair will notice. One-line KD note recommended.
- **REVIEW — confirm the 31:31 new-covenant summary.** *"…อ้างอิงเต็มใน ฮีบรู 8:8–12 และ 10:16–17 ว่าสำเร็จในพระคริสต์"* ("cited in full in Heb 8/10 as fulfilled in Christ"). Framed as a report of what Hebrews does (descriptive citation-fact, matching the Gen 3:15 construction), so judged **§0-compliant** — but it is the single most doctrinally-forward summary in the book. Confirm it stands (parallel to the Isaiah §6 ratification).
- **DECIDE-adjacent / recommend doc — the Branch/צֶמַח rendering has no corpus doc.** A `docs/` sweep finds the lock living **entirely in per-verse KDs** (Isa 11:1, Jer 23:5, Jer 33:15), each manually cross-referencing the others. צֶמַח recurs as a messianic title in **Zechariah 3:8 and 6:12** (still ahead). **Recommend `docs/translator_decisions/messianic_branch_tzemach_2026-06.md`** locking หน่ออันชอบธรรม + the royal-when-reigning register rule before Zechariah ships, so byte-consistency is enforced by reference rather than re-derived.

**Severity: MEDIUM** (theological, high reviewer-visibility; but the surface itself is sound and §0-cleaner than Isaiah).

---

## 7. 31:22 crux — Layer-2 reader-footer gap — **REVIEW**

The נְקֵבָה תְּסוֹבֵב גָּבֶר crux ("a woman shall encompass a man") is handled per policy *in substance*: the KD renders literally (ผู้หญิงจะโอบล้อมผู้ชาย), preserves the polysemy, and names the role-reversal + the historic Marian/messianic reading **descriptively** (*"การตีความเชิงเมสสิยาห์ในบางจารีต"*). But per `gender_passages_thai_register_2026-05.md §2`, interpretive cruxes of this weight belong in a **Layer-2 reader footnote** (`textual_variants`) — exactly as Gen 3:15 and 3:16 each received. `textual_variants/jeremiah_31.json` carries only the divine-name boilerplate; the crux is invisible to readers. **Recommend adding a 31:22 Layer-2 footer modeled on Gen 3:16.** **Severity: LOW-MEDIUM.**

---

## 8. New covenant 31:31–34 → Hebrews 8 / 10 — **LOCKED (substantially harmonized; one footer owed → §9)**

The longest OT quotation in the NT, and the quoted core is **substantially harmonized** with the shipped Hebrews:

| Element | Jer 31 | Heb 8/10 | Verdict |
|---|---|---|---|
| "new covenant" | พันธสัญญาใหม่ (31:31) | พันธสัญญาใหม่ (8:8) | byte-shared |
| "I will be their God / they my people" | เราจะเป็นพระเจ้าของพวกเขา และพวกเขาจะเป็นประชากรของเรา (31:33) | identical (8:10) | **byte-identical** |
| "they shall all know me" | ทุกคนจะรู้จักเรา (31:34) | ทุกคนจะรู้จักเรา (8:11) | byte-shared core |
| "remember sins no more" | ไม่จดจำบาป…อีกต่อไป (31:34) | ไม่จดจำบาป…อีกเลย (8:12 / 10:17) | byte-shared core |
| "house of Israel/Judah" | วงศ์วาน (31:31) | พงศ์พันธุ์ (8:8) | synonym (low-jar) |
| "law within / on hearts" | ธรรมบัญญัติ…ภายใน…จารึก…ดวงใจ (31:33) | บัญญัติ…ความคิด…จารึก…ใจ (8:10) | synonym; shared verb จารึก |
| "forgive iniquity" | อภัย (31:34, MT sālaḥ) | ทรงเมตตา (8:12, LXX ἵλεως) | **MT/LXX divergence — defensible** |

The covenant-formula clause is byte-identical; the divergences track genuine MT-vs-LXX wording and are individually defensible. The one outright contradiction — **31:32** "I was a husband to them" (MT) vs Heb 8:9 "I disregarded them" (LXX) — is the footer the policy obligates (§9). **LOCKED** on the thread; the footer gap rolls into the §9 DECIDE. **Severity: GREEN** (here; §9 carries the disclosure question).

---

## 9. MT-vs-LXX macro-divergence + the textual-footer apparatus — **DECIDE (the textual headline)**

**Surface: correct.** Jeremiah translates the MT (longer) text throughout, follows MT order for the OAN (chs 46–51), and excludes LXX-only material — exactly per `ot_canon_and_text_base` exception #4 and `mt_vs_lxx_textual_variant_handling`.

**Disclosure: the problem.** The reader sees Thai verses + `thai_summary` + `textual_variants` footers + `translator_notes` footers; **`key_decisions` and `notes` are never rendered** (confirmed in `render_reader.py`). Every one of the 52 `textual_variants` files carries **only** the YHWH footnote. So Jeremiah's defining textual feature — the OT's largest MT/LXX divergence — reaches the reader almost nowhere:

| Divergence | Documented where | Reader-facing? |
|---|---|---|
| OAN reorder (LXX after 25:13; different internal order) | 1:3 note + 25:13 KD/note | **No** (KD/note only) |
| 10:11 (single verse absent from LXX) | 10:11 note | **No** |
| 29:16–20 (absent from LXX) | 29:16 KD/note | **No** |
| 30:10–11 (relocated in LXX) | 30:10 KD/note | **No** |
| **33:14–26** (the longest MT plus — Branch + Davidic/Levitical covenant, absent from LXX) | 33:14 KD + note + **`thai_summary`** | **Partial** (one inline summary on v.14; vv.15–26 silent; no footer) |
| 39:4–13 (absent from LXX) | 39:4 KD/note | **No** |
| 52:28–30 (absent from LXX) | 52:28 KD only | **No** (not even in notes/summary) |
| **31:32** (MT "husband" vs LXX "disregarded," **cited at Heb 8:9**) | 31:32 KD/note | **No** |

There is **no book-level prefatory note** — the `mt_vs_lxx §2.2` macro-structural model (built for 1 Kings) and the §2.3 disclosure floor were written partly *for* a book like this, yet neither was applied. Jeremiah's divergences clearly clear the §2.3 floor (macro-structural reorder + reader-affecting absent passages + an NT-cited variant), so the "zero footers" state is **not** the compliant-silence case 2 Kings was — it is a genuine disclosure gap.

**31:32 is the single footer the policy actually obligates:** the LXX reading is *cited in the NT* (Heb 8:9), and a reader comparing Jer 31:32 ↔ Heb 8:9 hits "husband" vs "disregarded" — a flat contradiction. The KD correctly identifies it (*"ฉบับ LXX (อ้างใน ฮบ 8:9) อ่านต่างเป็น 'เราจึงทอดทิ้งพวกเขา' … ยึด MT"*) but it is KD-only.

**DECIDE — apply the policy's prescribed remedy, or formally affirm KD-only for this book:**
1. Add a **book-level prefatory note** at `jeremiah_01` (`textual_variants`) describing the LXX shorter-text + OAN reorder.
2. Add **chapter-footer anchors** (`textual_variants` entries) at chs **25** (OAN insertion point), **33** (33:14–26 absence — promote the v.14 summary to a footer), **39**, **52**, and the **OAN head (46)**.
3. Add the **31:32** Tier-2 footer (MT husband / LXX disregarded → Heb 8:9). Optionally an anchor footer at 31:31 flagging the Heb 8/10 cross-quote weight.

Affirmatively: every *other* cross-quote divergence (1 Cor 1:31, Matt 2:18, Rev 18, etc.) is synonym-level or intrinsic MT/LXX and falls **below** the §2.3 floor — KD-only is compliant there. **Severity: MEDIUM-HIGH** (the book's defining textual feature; strongest external-AI question after §13/§24). **No translation-surface edit is implied** — this is an apparatus decision.

---

## 10. OT→NT cross-quotation thread — **LOCKED (one retro-candidate)**

The entire NT Jeremiah cross-quotes is shipped, and the thread holds:

| Jer | NT | Verdict |
|---|---|---|
| 31:31–34 | Heb 8:8–12; 10:16–17 | harmonized core (§8); 31:32 footer owed (§9) |
| 31:15 | Matt 2:18 | harmonized (synonym-level; Matt follows LXX-B doublet, documented) |
| 7:11 | Mark 11:17 / Luke 19:46 | **byte-shared** (ถ้ำของโจร) |
| 7:11 | **Matt 21:13** | **RETRO-CANDIDATE** — Matt = ซ่องของพวกโจร (lone Synoptic outlier) |
| 9:23–24 | 1 Cor 1:31 | harmonized (อวด); 2 Cor 10:17 documented variant (ภาคภูมิใจ) |
| 22:24/30 (Coniah) | Matt 1:11–12 | name-form split โคนิยาห์/เยโคนิยาห์ (documented standard) |
| 31:33 | 2 Cor 3:3 | allusion, harmonized (จารึก + ใจ) |
| 10:7 | Rev 15:4 | echo, harmonized (ยำเกรง + ประชาชาติ) |
| 51:45 (+50:8) | Rev 18:4 | harmonized core (ประชากรของเรา…จงออกมา) |
| 51:7–8 | Rev 17:4 / 18:3 | **byte-shared** (ถ้วยทองคำ) |
| 51:63–64 | Rev 18:21 | defensible (stone vs millstone — source texts differ) |
| 32:6–9 | Matt 27:9–10 | non-quote (Matt = Zech 11 misattributed; 17 vs 30 shekels) |

**RETRO-CANDIDATE — Matt 21:13.** The Greek is identical across the three Synoptics (σπήλαιον λῃστῶν); Jeremiah harmonized to Mark/Luke (ถ้ำของโจร) but Matthew shipped ซ่องของพวกโจร. A reader comparing Jer 7:11 → Matt 21:13 sees ถ้ำ vs ซ่อง. **Recommend normalizing Matt 21:13 → ถ้ำของโจร** (NT-side fix, staged-re-audit path). **LOCKED** on the thread. **Severity: LOW-MEDIUM.**

---

## 11. פקד paqad "visit/punish" — **LOCKED (exemplary)**

49 occurrences; the most uniform book-level paqad performance in the corpus. Sense-4 judgment → **ลงโทษ / ทรงลงโทษ** in ~31 verses (5:9, 5:29, 6:6, 6:15, 8:12, 9:8, 9:24, 11:22-23, 14:10, 21:14, 23:34, 25:12, 27:8, 29:32, 30:20, 36:31, 44:13, 44:29, 46:21, 48:44, 49:8, 50:18, 50:31, 51:44, 51:47, 51:52, …); sense-1 visit/attend → ทรงเยี่ยมเยียน/มาดูแล (15:15, 27:22, 29:10); sense-3 appoint → แต่งตั้ง/กำหนด (1:10, 15:3, 49:19, 50:44). The 23:1–4 shepherd-paqad wordplay (negligent shepherds "not attended" / God "will attend") is rendered with the เลี้ยงดู/ดูแล split — defensible; the lemma-pun is unavoidably muted. **LOCKED** ✓ per `paqad_visit_attend_2026-05.md`. **Severity: GREEN.**

---

## 12. נחם nicham "relent" — **LOCKED (one first-person slip → §13)**

All divine-relenting Niph'al → the lock **ทรงเปลี่ยนพระทัย / เปลี่ยนพระทัย**: 15:6, 18:8, 18:10, 20:16, 26:3, 26:13, 26:19, 42:10. Correct non-fires: 31:19 is **human** repentance (Ephraim → สำนึกผิด). **One first-person slip: 4:28** `וְלֹא נִחַמְתִּי` → เราจะไม่**เปลี่ยนใจ** (plain), where 15:6's first-person clause kept เปลี่ยนพระทัย — the same first-person register lapse as §13, leaking into the nicham lemma. **LOCKED** ✓ per `nicham_divine_relenting_2026-05.md` (4:28 rolls into the §13 DECIDE). **Severity: GREEN.**

---

## 12b. Versification (MT vs English) — **REVIEW (JER 8/9 offset unregistered)**

MT numbering throughout; verse counts match standard MT for all 52 chapters; the lone Aramaic verse 10:11 is registered (`JER-10-11`, `diverges:false`). **Gap:** the **JER 8/9 MT-vs-English boundary** is not registered — MT 8:23 = English/BSB 9:1, and all of MT ch.9 = English 9:N+1. The offset is documented in KDs (8:23, 9:1–19) and **translator-self-flagged** (*"Flag for the versification_map maintainer: JER 8/9 boundary divergence is not yet in data/versification_map.json"*), but `versification_map.json` has only `JER-10-11`. `check_versification_anchor.py` default-passes because there is no map entry. **Recommend registering the JER 8:23 / ch.9 zone** — and note the "versification map ship gotcha" (`ship_chapter.sh` doesn't stage the map; commit manually). **Severity: LOW.**

---

## 13. Divine anthropomorphism — a *codified* first-person-plain rule — **DECIDE (the loudest finding)**

`divine_anthropomorphism_thai_grammar_2026-05.md` locks God's body-parts to royal register with **no person-based exception**: arm זְרוֹעַ → **พระกร**, hand יָד → **พระหัตถ์**, eyes עֵינַי → **พระเนตร**, mouth פֶּה → **พระโอษฐ์**. In Jeremiah, first-person divine speech ("my arm / my hand / my eyes") **systematically drops to plain register**, and — beyond Isaiah, where this was undocumented drift — the lapse is **written into the `key_decisions` as a deliberate rule**:

> 21:5 KD: *"คำพูดบุรุษที่ 1 ของพระเจ้า (เรา) ใช้คำส่วนร่างกายแบบ 'ธรรมดา' (มือ/แขน) ไม่ใช่ราชาศัพท์ … ราชาศัพท์สงวนไว้สำหรับการพรรณนาบุรุษที่ 3."*
> 27:5 KD: *"ใช้ 'แขน' คำสามัญ ไม่ใช่ราชาศัพท์ พระกร; สม่ำเสมอกับ 21:5."*

**13a. Arm זְרוֹעַ (the signature "outstretched arm" idiom):**
- **พระกร (correct, 2nd-person address to God):** 32:17, 32:21.
- **แขน (DRIFT, 1st-person divine speech):** **21:5** (`בְּיָד נְטוּיָה וּבִזְרוֹעַ חֲזָקָה` → "ด้วยมือที่เหยียดออกและแขนอันแข็งแกร่ง"), **27:5** (`וּבִזְרוֹעִי הַנְּטוּיָה` → "และแขนที่เหยียดออกของเรา"). Same idiom, opposite register, split on grammatical person.

**13b. Hand יָד ("I will stretch out my hand," idiom נטה יד) — not even internally consistent:**
- **พระหัตถ์:** 15:6 (`וָאַט אֶת־יָדִי עָלַיִךְ` → "เราจึงเหยียดพระหัตถ์ออกต่อสู้เจ้า") — **first-person, yet Rachasap.**
- **มือ (DRIFT):** 6:12 (`כִּי־אַטֶּה אֶת־יָדִי` → "เราจะเหยียดมือของเราออก"), 51:25 (`וְנָטִיתִי אֶת־יָדִי עָלֶיךָ` → "เราจะเหยียดมือของเราออกต่อสู้เจ้า"). The *exact same idiom* is พระหัตถ์ at 15:6 but มือ at 6:12/51:25 — the first-person rule isn't even applied uniformly.
- (Compliant non-finding: cup "from the hand of YHWH" → พระหัตถ์ at 25:17, 51:7.)

**13c. Eyes עֵינַי:**
- **พระเนตร / สายพระเนตร:** 16:17 (first-person, correct).
- **DRIFT / flattened:** 24:6 (`וְשַׂמְתִּי עֵינִי עֲלֵיהֶם לְטוֹבָה` "I will set my eyes on them" → "เราจะจับตาดูพวกเขา" — idiom dropped, no พระเนตร). The "evil in my eyes" idiom is **split**: สายตา (7:30, 32:30, 34:15) vs สายพระเนตร (18:10).

**13d. Mouth פֶּה — STABLE** (9:11 `פִּי־יְהוָה` → พระโอษฐ์; no drift). **13e. nicham** 4:28 first-person plain (§12).

The pattern is **systematic and codified**, not scattered typos, and produces same-idiom register splits (พระหัตถ์/มือ; พระกร/แขน; สายพระเนตร/สายตา) that are internally inconsistent. This is the identical drift the Isaiah audit flagged (ISA §13, which recommended **reversal**), now argued into Jeremiah's KDs as intentional.

**DECIDE — Ben must choose one and apply it corpus-wide:**
(a) **Ratify** a documented "first-person divine self-reference → plain register" exception, amend `divine_anthropomorphism_thai_grammar_2026-05.md`, and fix the *internal* inconsistencies (15:6, 18:10 → plain to match; or define when 1st-person still takes Rachasap); **or**
(b) **Reverse** the ~7–9 verses to Rachasap (21:5, 27:5 → พระกร; 6:12, 51:25 → พระหัตถ์; 24:6, 7:30, 32:30, 34:15 → พระเนตร; 4:28 → เปลี่ยนพระทัย), matching the Isaiah §13 recommendation.

Either way, **reconcile with Isaiah §13** (which is unresolved) so the corpus speaks with one voice — **highest forward weight: Ezekiel**, saturated with first-person divine body-part theophany ("I stretched out my hand," "my eyes will not spare"). **Severity: HIGH** (corpus-lock conflict, codified, cross-book, load-bearing).

---

## 14. חֶסֶד covenant-love — **LOCKED**

All 6 occurrences → **ความรักมั่นคง**: 2:2 (ḥesed of youth), 9:24 (the חֶסֶד מִשְׁפָּט וּצְדָקָה triad), 16:5, 31:3 (distinguished from אהבת עולם "ความรักนิรันดร์"), 32:18, 33:11. No mis-fires. **LOCKED** ✓ per `chesed_covenant_love_2026-05.md`. **Severity: GREEN.**

---

## 15. Exod-34 attribute formula — **N/A (correct)**

A whole-book scan for the character-cluster (חַנּוּן / רַחוּם / אֶרֶךְ אַפַּיִם / רַב־חֶסֶד) returns zero hits — the Sinai grace-formula is never recited in Jeremiah. The one partial echo, **32:18** (`עֹשֶׂה חֶסֶד לַאֲלָפִים … עֲוֹן אָבוֹת`, the Decalogue/Exod-34:7 tail), correctly renders the chesed-clause (ทรงสำแดงความรักมั่นคงต่อคนเป็นพันชั่วอายุ) without triggering the formula lock. **N/A (correct)** per `exod_34_attribute_formula_2026-05.md`. **Severity: GREEN.**

---

## 16. רוּחַ / Spirit — **N/A (correct)**

No Spirit-of-YHWH empowerment use in Jeremiah. Every רוּחַ is "wind" → ลม (2:24, 4:11-12, 5:13, 10:13, 13:24, 18:17, 22:22, 49:36, 51:16); the two God-as-subject cases stir a *human/agent* spirit, correctly **not** พระวิญญาณ (51:1 רוּחַ מַשְׁחִית → วิญญาณของผู้ทำลายล้าง; 51:11 `הֵעִיר יְהוָה אֶת־רוּחַ מַלְכֵי מָדַי` → ทรงเร้าจิตใจของบรรดากษัตริย์แห่งมีเดีย). The empowerment lock correctly stays dormant. **N/A (correct)** per `spirit_of_yhwh_empowerment_2026-05.md`. **Severity: GREEN.**

---

## 17. שׁוּב shuv "return / repent / turn" — **STABLE**

Jeremiah's central wordplay, handled with discourse-awareness and a traceable **กลับ** root: imperative "Return!" → จงกลับมา (3:12/14/22, 4:1, 31:21); the fall/turn wordplay (8:4–5) → หันเห…หันกลับมา; the double-shuv "if you return / I will restore you" (15:19) → ถ้าเจ้าหันกลับมา เราก็จะให้เจ้ากลับคืนมา; שׁוֹבָב "faithless" → กลับกลอก (3:14/22, 31:22); מְשׁוּבָה "backsliding" → ความกลับกลอก. The กลับ morpheme stays visible across the family. **STABLE** ✓ per `leitwort_handling_policy_2026-05.md`. **Severity: GREEN.**

---

## 18. Signature judgment leitwörter — **LOCKED / STABLE**

- **"sword, famine, pestilence" (חֶרֶב רָעָב דֶּבֶר)** → **ดาบ การกันดารอาหาร โรคระบาด**, uniform across ~12 (14:12, 21:9, 24:10, 27:8, 29:17-18, 32:24, 38:2, 42:17/22, 44:13); 34:17 reorders to track the Hebrew's own reordering. **LOCKED.**
- **"terror on every side" (מָגוֹר מִסָּבִיב)** → ความสยดสยอง(อยู่)รอบด้าน (6:25, 20:10, 46:5, 49:29); the Pashhur **name** at 20:3 correctly transliterated มาโกร์มิสซาบิบ. **STABLE** (cosmetic อยู่/no-อยู่ wobble).
- **Call-verbs "uproot/tear-down/destroy/overthrow // build/plant"** — core pairs locked: สร้าง / ปลูก / ถอน(ราก) / รื้อ(ทำลาย) (1:10, 18:7-9, 24:6, 31:28, 42:10, 45:4); the destructive verbs vary because the Hebrew verb-count varies per verse. **STABLE.**
- **שָׁמַע בְּקוֹל "obey/listen to (the) voice"** → เชื่อฟังเสียง (human) / เชื่อฟังพระสุรเสียง (divine) — the register split is the correct honorific application. **STABLE.**

**Severity: GREEN.**

---

## 19. Idol / false-god polemic — **LOCKED (excellent)**

- **Pagan deities all carry the OT พระ- proper-name register, zero bare:** Baal הַבַּעַל → **พระบาอัล** (13×: 2:8/23, 7:9, 9:13[pl], 11:13/17, 12:16, 19:5, 23:13/27, 32:29/35); Chemosh → พระเคโมช (48:7/13/46); Milcom → พระมิลโคม (49:1/3); Bel → พระเบล, Merodach → พระเมโรดัก (50:2, 51:44); Molech → พระโมเลค (32:35). Topheth → โทเฟท, Ben-Hinnom → หุบเขาเบนฮินโนม (translit). Pagan-deity pronoun consistently **มัน**, never elevated.
- **"other gods" אֱלֹהִים אֲחֵרִים → พระอื่น** in all 18 occurrences (`ot_polytheistic_register §1.1`).
- **Idol-fabrication satire (ch 10:1–16)** — contempt register fully intact, matching the Isaiah 44 approach: 10:5 "หุ่นไล่กาในไร่แตงกวา … เดินไม่ได้" (scarecrow), 10:8 "เป็นเพียงท่อนไม้," 10:14 "ไม่มีลมหายใจอยู่ในนั้นเลย," 10:15 "ของไร้ค่า … ผลงานที่น่าหัวเราะเยาะ."

**LOCKED** ✓ per `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`. *(Note: Jeremiah has **no** rhetorical-incomparable "who is like you among the gods" form — verified — so no polytheistic-register Layer-2 footnote is owed; the polemic is carried lexically. This resolves the Isaiah §27 reader-footnote question negatively for Jeremiah.)* **Severity: GREEN.**

---

## 20. Hebrew oath formulas — **LOCKED + REVIEW (49:13) + new-lock candidate (חַי־אָנִי)**

- **חַי־יְהוָה "as the LORD lives"** → **องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่(แน่ฉันใด)**, uniform across 9 (4:2, 5:2, 12:16, 16:14-15, 23:7-8, 38:16, 44:26). **LOCKED.**
- **בִּי נִשְׁבַּעְתִּי "by myself I have sworn"** — **22:5** matches the lock (เราสาบานในตัวของเราเอง); **49:13 REVIEW** drifts to a synonym (เราได้ปฏิญาณด้วยตัวเราเอง — ปฏิญาณ vs locked สาบาน). 51:14 is the 3rd-person construction, correctly ทรงปฏิญาณโดยพระองค์เอง. Normalize 49:13.
- **חַי־אָנִי "as I live" (divine self-oath)** → **เรามีชีวิตอยู่แน่ฉันใด** (22:24, 46:18), internally consistent; the 22:24 KD already cross-refs Isa 49:18. This is the **Isaiah-flagged new-lock candidate**, now demonstrated consistent in Jeremiah. **Recommend formalizing into `hebrew_oath_formulas_2026-05.md §1.5`**, noting the deliberate 1st-vs-3rd-person verb split (มีชีวิตอยู่ vs ทรงพระชนม์ for the same √חי) so it isn't later "corrected" into false uniformity.

**Severity: LOW** per `hebrew_oath_formulas_2026-05.md`.

---

## 21. balm צֳרִי "balm in Gilead" — **REVIEW (lexical drift)**

The recognized Jeremiah leitwort is rendered three ways: **ยาสมานแผล** (8:22) / **ยางรักษาโรค** (46:11) / **ยาสมาน** (51:8). Book-specific, not corpus-locked, so soft. **Recommend normalizing to one form (e.g. ยาสมาน)** for traceability of the motif. **Severity: LOW.**

---

## 22. עַבְדִּי "my servant" Nebuchadnezzar — **STABLE (theology handled well; register consequence → §24)**

All three occurrences render the Hebrew plain עֶבֶד → **ผู้รับใช้ของเรา** (the same lexeme used for prophets/Israel) — appropriate, with the descriptive notes carrying the "instrument, not covenant-servant" nuance: 25:9, 27:6, 43:10, each with a cross-referencing KD + summary naming the pagan-king-as-YHWH's-instrument tension (*"เครื่องมือพิพากษาในพระหัตถ์พระเจ้า"*). The עַבְדִּי rendering itself is **STABLE** and the theological tension is handled exactly right. Its register *consequence* — the translator cites "my servant = instrument-role" as part of the rationale for withholding ทรง — is the linchpin of §24. **Severity: GREEN** (here; §24 carries the register decision).

---

## 23. Queen of Heaven מְלֶכֶת הַשָּׁמַיִם — **STABLE (new-lock candidate)**

→ **เจ้าแม่แห่งฟ้าสวรรค์** (female pronoun นาง), uniform across 5 (7:18, 44:17-19, 44:25). As a *title-epithet* ("lady/mother-goddess") rather than a proper name, the descriptive title is the right call and the พระ- proper-name rule doesn't apply. First appearance in the corpus and **undocumented**. **Recommend adding to the `pagan_deities_2026-04.md` OT table** as a new-lock candidate. **Severity: LOW.**

---

## 24. Foreign-monarch register: Nebuchadnezzar plain, contradicting Daniel + §2.2 — **DECIDE**

`ot_register_policy §2.2` grants foreign emperors full ราชาศัพท์ *even if villainous*; the Ezra/Neh/Esther/Daniel block exercised this (Daniel gives all four emperors full ทรง). **Jeremiah diverges:** across chs 1–51 the king of Babylon receives **plain register**, codified as an "invader → plain" rule with no policy basis:

> 21:2 KD: *"กษัตริย์บาบิโลนผู้รุกราน → ทะเบียนธรรมดา (ผู้รุกราน ไม่ใช่บริบทราชกิจที่ผู้เล่าเชิดชู)."*

Evidence (narrator-voice, all plain): 34:1 (กำลังสู้รบ), 39:1 (ยกมา/ล้อม — contrast Dan 1:1 ทรงยกทัพ/ทรงล้อม for the same action), 39:5 (พิพากษา), 37:1 (ตั้ง). Plus the cross-book clash: the **same king Nebuchadnezzar** is plain in Jeremiah but full ทรง in Daniel.

**Two internal contradictions inside Jeremiah:**
1. **39:11** — *"เนบูคัดเนสซาร์…ได้ทรงบัญชา"* — ทรง granted, KD: *"แม้ผู้พิชิตยังให้เกียรติ"* (he gets royal register specifically where he protects Jeremiah — a content-sensitive register §2.2 rejects).
2. **Ch.52** (= 2 Kings 25 appendix) — full royal for the Babylonian king Evil-merodach: 52:31 *"…ได้ทรงพระกรุณาปล่อย … ปีที่พระองค์ขึ้นครองราชย์"*; 52:32 *"พระองค์ตรัส…ด้วยพระเมตตา และทรงตั้งบัลลังก์."* The book contradicts itself across the chs 1–51 / ch.52 seam.

(Pharaoh Hophra 44:30 and the OAN kings are likewise plain — internally consistent with the chs-1-51 philosophy but the same §2.2 deviation. The national deities Chemosh/Milcom/Amon are correctly พระ-prefixed, §19.)

**The kings of Judah are handled correctly (STABLE):** Zedekiah, Jehoiakim, Jehoiachin keep royal register, *held through condemnation* (52:11 ควักพระเนตร…สิ้นพระชนม์ while blinded and shackled), with principled shame-downshifts for specific humiliating actions (22:19 donkey-burial; 22:30 "this man childless"). One consistency note: the **same Zedekiah-capture scene is plain in ch.39 but royal in ch.52** — the ch.39/52 doublet split parallels the Nebuchadnezzar seam.

**Prophets/officials are correct (LOCKED):** Jeremiah plain + speaks ทูล up to the king (37:17); Hananiah the false prophet plain (28:1, death ก็ตาย not สิ้นชีวิต); Baruch, Ebed-melech, the princes all plain, per §2.2.

**DECIDE — this is the book's primary register decision and it has been deferred since Ezra:**
1. **Write `docs/translator_decisions/foreign_monarch_register_2026-05.md`** (still nonexistent), deciding explicitly whether hostile-conqueror emperors keep ทรง per §2.2 or get a documented "hostile-invader downshift."
2. **Reconcile Jeremiah internally** — chs 1–51 (plain) vs ch.52 (royal) vs 39:11 (ทรง); and the ch.39/52 Zedekiah doublet.
3. **Resolve jointly with the still-untagged EZR/NEH/EST/DAN block** so shared kings (Nebuchadnezzar above all) speak with one voice across books.

**Severity: HIGH** (cross-book inconsistency on the OT's most prominent foreign king + two within-book contradictions + a long-deferred owed doc). **The "my servant" theology (§22) is sound; the register downshift it was used to justify is the conflict.**

---

## 25. Kings of Judah register — **STABLE** (covered in §24)

Royal register maintained, even under judgment, with principled shame-action downshifts (22:19, 22:30). The ch.39/52 Zedekiah-capture register doublet is the one consistency note. **STABLE.** **Severity: LOW.**

---

## 26. Prophets / officials register — **LOCKED** (covered in §24)

Jeremiah, Baruch, Hananiah (false prophet), Ebed-melech, the princes all plain per `ot_register_policy §2.2`; Jeremiah speaks ทูล up to the king. No anomalies. **LOCKED** ✓. **Severity: GREEN.**

---

## 27. DSS / Qumran + inclusion variants — **STABLE (correct)**

No 4QJer readings adopted anywhere (Jeremiah is not on the `ot_canon` Tier-4 DSS-elevated list — only Samuel, Isaiah, Pentateuch — so the MT-priority policy correctly declines 4QJerᵇ's shorter LXX-type text). `audit_inclusion_variants.py --book jeremiah --strict` = **0 candidates, exit 0** — correct: the inclusion-variant policy is NT-only (SBLGNT/TR/Byz whole-verse omissions); Jeremiah's MT-plus passages are routed through the MT/LXX policy (§9), not the inclusion tiers. **STABLE** ✓. **Severity: GREEN.**

---

## 28. Mechanical (§1) + infrastructure

- **52/52** chapters: `output/check_reports/jeremiah_NN_review.md` (green) + `output/back_translations/jeremiah_NN.json` + `output/translations/jeremiah_NN.json` ✓
- **52/52** chapters: `output/textual_variants/jeremiah_NN.json` carrying the YHWH first-occurrence footnote — **complete coverage** (§5).
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings.**
- `check_phrase_consistency.py`: **0 violations across 38 audited locks** (28,613 verses).
- `audit_inclusion_variants.py --book jeremiah --strict`: **0 candidates, exit 0.**
- `check_divine_names.py --book JER`: **exit 0**; 2 soft warnings (37:20, 38:9) **both confirmed false positives** (human "my lord the king," §4).
- `check_versification_anchor.py --book JER`: **exit 0** (but the JER 8/9 offset zone is unregistered in the map — §12b).
- `git status output/`: only the re-ran-check artifact (`phrase_consistency.md`). No source-file dirt.
- **`export_to_usfm.py --book JER`: FAILS — "Unknown book code: JER."** The script's book table does not carry `JER` (the same OT-USFM book-code-registration gotcha logged for LAM/SNG/ISA in every prior OT audit). **Non-blocking infra gap** — flag for the maintainer to register `JER` in the export script's book table; not a translation defect.
- **Provenance note (surfaced for Ben):** during this audit, two commits (`b1dbb6e7` "clear external-AI backlog — auto-derive items + packets for 7 OT books," `72a40e0a`) landed on `main` from a separate automation and added a **machine-generated** `docs/end_of_book/jeremiah/external_review_items_JER.md` + `external_review_packet_JER_2026-06-21.md` (generic per-book second-opinion stubs). This audit **replaces those two files with the hand-curated versions** the §3 checklist calls for (specific REVIEW/DECIDE items from this editorial pass). The auto-derived content is superseded, not lost — it was a stopgap backlog-clearing artifact, and the hand-curated items doc is strictly more specific.

---

## Recommendation

**Jeremiah ships in strong corpus-hygiene shape** — mechanically the cleanest major-prophet state to date (full divine-name footnote coverage, zero bare pagan-deity names, near-perfect Sabaoth + נְאֻם־יְהוָה uniformity, exemplary paqad/nicham/chesed locks). The three DECIDE items are all **policy-and-apparatus decisions, not surface-quality defects**, and two of them (anthropomorphism §13, foreign-monarch §24) are **corpus-level questions Jeremiah inherited and sharpened** rather than created — both must be reconciled with prior books (Isaiah §13; the EZR/NEH/EST/DAN block) before they compound into Ezekiel.

Tag `book-jeremiah-v1` after:
1. Ben's decisions on the **3 DECIDE** items: §13 anthropomorphism (ratify-or-reverse + reconcile Isaiah), §24 foreign-monarch register (decide + write the owed doc + reconcile internally + with the EZR/NEH/EST/DAN block), §9 MT/LXX disclosure (apply the prefatory-note + footer apparatus, or affirm KD-only).
2. Ben's decisions on the **8 REVIEW** items (§3 Adonai-stack/44:26, §12b versification, §7 31:22 footer, §10 Matt 21:13 retro, §6 23:5/33:15 + 31:31 summary, §20 49:13, §21 balm).
3. Any spot-revisions executed + checks re-run clean.
4. New docs written as decided: `messianic_branch_tzemach_2026-06.md` (§6), `foreign_monarch_register_2026-05.md` (§24); amendments to `hebrew_oath_formulas` §1.5 (חַי־אָנִי, §20), `pagan_deities` (Queen of Heaven, §23), and `divine_anthropomorphism_thai_grammar` (§13, if ratifying the exception).
5. External AI sanity-check (§3 — the 4-item packet above).

The `foreign_monarch_register` + Isaiah-§13 reconciliations are the two highest-value forward-protection actions — both should land **before** Ezekiel.
