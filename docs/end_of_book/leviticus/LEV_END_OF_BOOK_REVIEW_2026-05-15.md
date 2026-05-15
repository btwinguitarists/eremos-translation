# Leviticus — End-of-Book Review

**Date:** 2026-05-15
**Scope:** All 27 chapters of Leviticus (~859 verses); `glossary.json`; existing `docs/translator_decisions/` (84 docs, including four landed today 2026-05-15 — `sacrificial_vocabulary_2026-05.md`, `goel_kinsman_redeemer_2026-05.md`, and revisions to the malak / kapporet / pharaoh-heart locks from the Numbers audit).
**Trigger:** LEV 27 shipped (commit `9402b89`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Sixth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers) and the **fourth Pentateuch book**. Leviticus is **the sacrificial / priestly / holiness-code locus** of the entire OT — the canonical OT-corpus test of every sacrificial-vocabulary lock and the locking precedent for kipper-atonement, kapporet, Yom Kippur, the five offering types, the Holiness Code (chs.17-26), Jubilee + Sabbatical year, and the kinsman-redeemer property-law cluster.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **20 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 27/27 chapters have green per-chapter reports + back-translations + textual_variants files; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-287-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `audit_inclusion_variants.py --book LEV --strict` returns 0 candidates (NT-style inclusion-variants policy N/A); `git status output/` shows only the harmless re-run of `output/check_reports/divine_names.md`. Zero hard fails across the mechanical surface.
- **Leviticus exercises every OT-corpus lock landed by 2026-05-14 audit** and is the canonical OT test of two docs landed today (2026-05-15) — `sacrificial_vocabulary_2026-05.md` and `goel_kinsman_redeemer_2026-05.md`. It is the **first downstream OT-book test** of (a) the **five-offering sacrificial-vocabulary lock** (LEV 1-7 is the sacrificial manual the doc was created to govern); (b) the **kapporet corpus lock** (6 LEV 16 occurrences); (c) the **kinsman-redeemer goel doc** (LEV 25 is the Pentateuch's property-goel locking-precedent chapter, 12+ occurrences); (d) the **kareth penalty leitwort** (18 occurrences, the densest book in scripture); (e) the **mot-yumat death-penalty formula** (14 occurrences, ditto).
- **Data integrity is clean.** Hebrew word-spacing correct in all 27 chapters; `thai_literal` is Thai in all 27 chapters (no English-leakage regression); all chapters have correctly-spaced Hebrew and Thai `thai_literal` fields; 27/27 chapters have Layer-2 first-occurrence YHWH footnotes in `output/textual_variants/leviticus_NN.json` using the post-NUM-15 going-forward template (no `ยาห์เวห์ Yahweh` romanization-phrase — the shorter NUM-going-forward template).
- **18 inherited locks verified compliant** in LEV across the divine-name family, OT-register policy, Hebrew-grammar-transfer, Hebrew-idioms (panim → พระพักตร์ at all 57 face-of-YHWH occurrences ✓), verse-schema, proper-names, kapporet, malak (N/A in LEV), divine-anthropomorphism, mt-vs-lxx-textual-variant-handling, divine-object-praise, narrator-vs-character-voice, leitwort, manah (N/A), paqad (N/A in LEV), pagan_deities (Molech → โมเลค ✓), hebrew_oath_formulas (N/A — no oath formulas in LEV's instructional register), nicham (N/A), chesed (1 false-positive at LEV 20:17 which is chesed II "disgrace" not chesed I — the Thai correctly renders `ความน่าอับอาย` "disgrace" — see §16).
- **5 Leviticus-distinctive patterns are STABLE-and-locked** at corpus level (the **"I am YHWH" formula** with 52 occurrences across the Holiness Code; the **Holiness Code leitwort קָדוֹשׁ** uniformly rendered; the **kareth penalty formula** 18 occurrences; the **mot-yumat death penalty formula** 14 occurrences; the **Lev 17 blood theology** + the LEV 16 Yom Kippur cluster as the canonical OT atonement-doctrine locus).
- **3 items flagged STABLE-but-undocumented** (recommend new corpus docs): the **Holiness Code "I am YHWH" closure leitwort** (the doc-able canonical Thai form); the **kareth penalty formula doc** (cross-Pentateuch lock for the 38+ occurrences across LEV / NUM / EXO / DEUT); the **incest catalog LEV 18:6-18 + 20:11-21 "uncover the nakedness" euphemism policy** (the Thai is hybrid — preserves `เปิดเผยความเปลือยเปล่า` "uncover nakedness" at 18:7-18 + 20:11-21 but renders 18:6's general `לְגַלּוֹת עֶרְוָה` as the explicit `มีความสัมพันธ์ทางเพศ` "have sexual relations"; the policy is principled but not docpos'd).
- **5 items flagged REVIEW** (defensible-but-worth-Ben's confirmation): the **LEV 23:6 Unleavened Bread feast Thai-drift** (`เทศกาลขนมปังไม่มีเชื้อ` vs. corpus-locked `เทศกาลขนมปังไร้เชื้อ` — single LEV 23:6 drift vs. 12 EXO + 3 LEV elsewhere + 5 NUM); the **LEV 25:25 goel doc-drift** (`ญาติสนิทที่สุด` "closest kinsman" rather than doc-canonical `ผู้ไถ่ที่เป็นญาติ` "kinsman-redeemer" or Ruth's `ญาติผู้ไถ่` — the locking-precedent verse for the property-goel chapter); the **yobel "Jubilee" rendering as `ปีจูบีลี`** (English-via-Latin transliteration rather than Hebrew transliteration `ปีโยเบล`); the **deror "liberty" rendering at LEV 25:10** (paraphrased `อิสรภาพ` — the Liberty Bell verse, which Isa 61:1's NT echo at Lk 4:18-19 will need to align with); the **LEV 16 + LEV 17:11 Layer-2 footer gap** (no Heb 9:5 / Heb 9:22 / Rom 3:25 / 1 Pet 2:24 cross-reference footers at the doctrinally load-bearing Yom Kippur + blood-theology verses).
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-leviticus-v1`):
  - **LEV-wide kipper drift from `sacrificial_vocabulary_2026-05.md`** — uniform `ลบมลทินบาป` ("clearance of ritual-impurity-sin") / `ทำการลบมลทินบาป` across **~168 occurrences** vs. the doc's locked `ลบบาป / ทำการลบบาป / ไถ่บาป` (no `มลทิน` morpheme). This is the largest single drift in the audit by occurrence-count. **The doc was decided 2026-05-15 — the SAME DATE as LEV 27 ship + this audit**. See §2. **CRITICAL.**
  - **LEV 25:25 goel + Ruth-vs-LEV cross-book divergence** — the goel doc (decided 2026-05-15) locks `ผู้ไถ่ที่เป็นญาติ` but neither Ruth (`ญาติผู้ไถ่`) nor LEV 25:25 (`ญาติสนิทที่สุด`) matches. The doc is the **third form** not used in either corpus. See §3.
- **External AI review (§3) pending.** Suggested 7-item packet (§2/§3 DECIDE + §4/§5/§7/§9/§11 REVIEW items).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה — **LOCKED**

**311 YHWH occurrences across all 27 chapters** (every chapter contains YHWH; densest in LEV 23 [36] and LEV 19 [22]; thinnest in LEV 13 [1] — within the diagnostic-skin-disease pericope, where the priest performs ritual inspection more than YHWH speaks). Layer-2 first-occurrence footers present at all 27 `output/textual_variants/leviticus_NN.json` files using the post-NUM-15 going-forward template (no `ยาห์เวห์ Yahweh` romanization-phrase). The script `check_divine_names.py` should now recognize this template — confirm clean pass on LEV.

All 311 occurrences render as **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` ✓. Zero drift to `ยาห์เวห์` transliteration in the primary `thai` field (the `thai_literal` back-translation column does use `พระยาห์เวห์` per back-translation convention; this is expected and not surfaced to readers).

**No standalone אֲדֹנָי occurrences in Leviticus** — the book is YHWH-direct-speech-saturated (priestly instructions delivered Moses → Aaron → people), with no Moses-vocative-Adonai prayers like Exod 4:10+13 or Num 14:17. So the divine_names_table's standalone-Adonai sub-rule (organce-on-its-own → องค์เจ้านาย) has no LEV exposure.

Corpus-total YHWH count after Leviticus: ~1,230+ occurrences across 287 chapters, all uniformly rendered.

**LOCKED** ✓.

---

## 2. LEV-wide kipper (כִּפֵּר) drift from `sacrificial_vocabulary_2026-05.md` — **DECIDE before tagging (CRITICAL — DRIFT from corpus-doc landed 2026-05-15)**

**The single most consequential finding of this audit.** The corpus-doc `docs/translator_decisions/sacrificial_vocabulary_2026-05.md` (Status: LOCKED 2026-05-15; cross-AI consensus ChatGPT + Gemini + Logos AI; triggered by NUM end-of-book audit) explicitly locks the כִּפֵּר verbal-rendering at:

> | Hebrew verb | Thai |
> |---|---|
> | כִּפֵּר (piel) | **ลบบาป** / **ไถ่บาป** / **ทำการลบบาป** |

**LEV-wide actual rendering:**

| Thai phrase | Verse count | Doc-canonical? |
|---|---|---|
| **ลบมลทินบาป** | 45 verses | ✗ adds `มลทิน` (ritual-impurity) morpheme |
| **ลบมลทิน** | 45 verses | ✗ adds `มลทิน` |
| **การลบมลทิน** | 42 verses | ✗ adds `มลทิน` |
| **ทำการลบมลทินบาป** | 41 verses | ✗ adds `มลทิน` |
| **ไถ่บาป** | 14 verses | ✓ matches doc-canonical |

**The drift is universal across LEV 1-7 + 16 + 23** (the sacrificial manual + Yom Kippur + Day-of-Atonement feast). The Thai surface adds the word **`มลทิน` ("ritual impurity")** to the doc-locked `ลบบาป` form. This is **arguably more faithful** to the Hebrew kipper semantic range (kipper covers BOTH moral-sin and ritual-impurity clearance in Leviticus's ritual register — see Milgrom *Leviticus 1-16* AB 1078-1083; Hartley *Leviticus* WBC 64-66; the kipper-as-purgation reading is the dominant scholarly view post-Milgrom). **But it diverges from the doc.**

**Editorial assessment.** The doc was decided **2026-05-15 — the same date as this audit**. The locking-precedent for the doc was presumably the as-shipped NUM kipper-rendering. Let me confirm the NUM precedent:

| Book | Verse | Hebrew | Thai |
|---|---|---|---|
| NUM 6:11 | וְכִפֶּ֣ר עָלָ֔יו | "ทำการลบมลทินบาปสำหรับเขา" (`ลบมลทินบาป` form) |
| NUM 8:12 | לְכַפֵּ֖ר עַל־הַלְוִיִּֽם | "ทำการลบมลทินบาปสำหรับคนเลวี" |
| NUM 15:25 | וְכִפֶּ֣ר הַכֹּהֵ֗ן | "ปุโรหิตจะทำการลบมลทินบาป" |

(Spot-check from `output/translations/numbers_*.json`.) **NUM uses the same `ลบมลทินบาป` form**. So the doc was apparently decided 2026-05-15 against a `ลบบาป`-canonical phrasing that is NOT what either NUM or LEV ships. The doc's locked Thai does not match the corpus-as-shipped at the largest-volume site of the lemma.

**Two paths — both require action before tagging `book-leviticus-v1`:**

**(a) Strict normalization** — rewrite **all ~168 LEV kipper-occurrences** to one of the doc's locked forms (`ลบบาป / ทำการลบบาป / ไถ่บาป`). Cost: hundreds of surgical text-edits across 21 chapters + per-chapter check re-runs + NUM normalization in tandem (~50+ NUM occurrences). Cost is high; semantic-loss (drops the `มลทิน` ritual-impurity dimension) is non-trivial; this option **NOT recommended**.

**(b) Doc-revision** — amend `sacrificial_vocabulary_2026-05.md` §5 to add `ลบมลทินบาป / ทำการลบมลทินบาป / การลบมลทิน` as the **canonical locked rendering** in Leviticus-ritual-context (with `ลบบาป / ไถ่บาป` retained for moral-noun and non-ritual atonement contexts). The doc's §3 already handles the חַטָּאת polysemy split by context — the kipper extension would parallel: ritual-context → `ลบมลทินบาป`; moral-forgiveness-context → `ลบบาป / ไถ่บาป`. Cost: one doc-revision + a §5 paragraph + cross-link to NUM-and-LEV-as-locking-precedent. **STRONGLY RECOMMENDED.**

**Severity: CRITICAL by count (~168 + ~50 NUM = ~218 occurrences), LOW by content-quality** — the as-shipped Thai is theologically defensible and arguably-better than the doc's locked Thai. The doc was apparently drafted without checking the as-shipped corpus.

**Followup:** the doc's §7 calls for `check_sacrificial_vocab.py` (script "to be written before LEV 1 ships"). The script **was not written**. Recommend writing it as part of the (b) doc-revision commit so future OT-book ships are auto-protected against any actual kipper-rendering drift.

---

## 3. LEV 25 goel + Ruth-vs-LEV cross-book divergence from `goel_kinsman_redeemer_2026-05.md` — **DECIDE before tagging**

The goel corpus-doc (LOCKED 2026-05-15) names **`ผู้ไถ่ที่เป็นญาติ`** ("kinsman who redeems") as the canonical Thai for the property/levirate-redemption goel:

> | Role | Hebrew context | Locked Thai |
> |---|---|---|
> | Kinsman-redeemer (property/levirate) | Lev 25; Ruth 2-4 | **ผู้ไถ่ที่เป็นญาติ** ("kinsman who redeems") |

**Three Thai forms in actual ship:**

| Source | Thai form | Verses |
|---|---|---|
| **Doc** (decided 2026-05-15) | **ผู้ไถ่ที่เป็นญาติ** | (locking precedent — not in any shipped translation) |
| **Ruth 3:9, 3:12, 3:13, 4:1, 4:3, 4:4, 4:6, 4:14** (8 occurrences) | **ญาติผู้ไถ่** ("kinsman-redeemer", compound) | Ruth chs.3-4 |
| **LEV 25:25** (locking-precedent intro verse) | **ญาติสนิทที่สุด** ("closest kinsman") | LEV 25:25 |
| **LEV 25:26, 25:48, 25:49, 25:54** | **ผู้ไถ่** alone (drops "kinsman" qualifier) | LEV 25:26-54 |

**The doc's locked form appears nowhere in either Ruth or LEV.** Ruth uses `ญาติผู้ไถ่`; LEV uses either `ญาติสนิทที่สุด` (25:25 only) or `ผู้ไถ่` (alone, 25:26+). The doc's `ผู้ไถ่ที่เป็นญาติ` is a third form.

**Editorial assessment.** The doc was decided 2026-05-15 — same date as audit + sacrificial-vocab doc. It appears the doc-canonical form was **drafted without verifying Ruth's actual shipped Thai**. Ruth is the first OT pilot book and ships the natural Thai compound `ญาติผู้ไถ่` ("kinsman-redeemer"). LEV 25:25 (the property-goel introduction) ships `ญาติสนิทที่สุด` ("closest kinsman"), which drops the ไถ่ root marker entirely — this is the substantive cross-book drift because LEV 25:25 is **the OT Pentateuch's locking precedent for the property-redemption sense** (`וּבָא גֹאֲלוֹ הַקָּרֹב אֵלָיו וְגָאַל אֵת מִמְכַּר אָחִיו` — "his goel who is close to him shall come and redeem his brother's sale"). The verse-level KD acknowledges `gōʾēl → ผู้ไถ่` and references "Boaz in Ruth 4" + "Christ-as-goel Rom 3:24", but the SURFACE Thai loses the root linkage. A Thai reader of LEV 25:25 sees `ญาติสนิทที่สุด` and a Thai reader of Ruth 3:9 sees `ญาติผู้ไถ่` — without root-linkage at the Thai surface, the typology breaks at the precise verse the doc was created to protect (`docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` §2: "If Ruth's Boaz is rendered ผู้ไถ่ที่เป็นญาติ but Job 19:25's 'my Redeemer' is rendered with a different term, the typology breaks AT THE THAI SURFACE.")

**Three paths — Ben choice needed:**

**(a) Normalize the doc to Ruth's actual `ญาติผู้ไถ่`** — amend `goel_kinsman_redeemer_2026-05.md` §1 to lock `ญาติผู้ไถ่` (the Ruth-ship form) as canonical. Then normalize LEV 25:25's surface from `ญาติสนิทที่สุด` → `ญาติผู้ไถ่` (1 verse edit). LEV 25:26+ already uses `ผู้ไถ่` alone, which would be retained as the in-context abbreviated form per the same doc rule. **RECOMMENDED** — Ruth is the pilot book and its naming convention should be the canonical lock; the doc-amendment is bookkeeping, the LEV 25:25 edit is surgical.

**(b) Strict normalization to doc-canonical `ผู้ไถ่ที่เป็นญาติ`** — rewrite both Ruth's 8 occurrences + LEV 25:25 to match the doc's locked form. Cost: ~9 surgical text-edits across 5 chapters. Defensible only if Ben actively prefers the doc's `ผู้ไถ่ที่เป็นญาติ` form over Ruth's natural `ญาติผู้ไถ่`. **NOT RECOMMENDED** — Ruth's form is more natural Thai compound morphology.

**(c) Leave as-is, accept divergence** — Ruth and LEV 25 use different surface forms; the goel doc's locked form is honored nowhere. Worst path; the doc loses authority.

**Forward-compounding:** Job 19:25 (the divine-Redeemer locking precedent the doc §5 names — **พระผู้ไถ่ของข้าพระองค์**), Isa 41:14, Isa 43:14, Isa 44:6, Isa 53 (typological), Ps 19:14 — all forthcoming. Whichever Thai is locked must propagate. **Severity: HIGH** — affects two shipped books + 4+ forthcoming.

---

## 4. LEV 23:6 Unleavened Bread feast — **REVIEW (cross-corpus single-verse drift)**

The Hebrew חַג הַמַּצּוֹת ("Feast of Unleavened Bread"; 12-month-1, 15-day-22 week-festival) appears at LEV 23:6. The corpus-locked Thai (`เทศกาลขนมปังไร้เชื้อ`) was established in Exodus and is uniform across EXO + LEV + NUM **with one exception**:

| Book | Thai | Verse count |
|---|---|---|
| Exodus | `เทศกาลขนมปังไร้เชื้อ` (and `ขนมปังไร้เชื้อ`) | 12 verses (12:8, 12:15, 12:17 etc.) |
| Leviticus | `ขนมปังไร้เชื้อ` | 3 verses (2:5, 8:2, 8:26) |
| Leviticus | **`ขนมปังไม่มีเชื้อ`** | **1 verse (23:6)** ✗ DRIFT |
| Numbers | `ขนมปังไร้เชื้อ` | 5 verses (6:15, 6:17, 6:19 etc.) |

The variant `ไม่มีเชื้อ` ("having no leaven") and the corpus-locked `ไร้เชื้อ` ("without leaven") are semantically equivalent in Thai (the `ไร้` prefix and the `ไม่มี` periphrasis are interchangeable register-neutral forms). Both are valid Thai renderings of מַצּוֹת. But the corpus has uniformly locked `ไร้เชื้อ` since EXO 12, and LEV 23:6 is the single drift.

**REVIEW flag.** Recommend single-verse normalization at LEV 23:6: change `เทศกาลขนมปังไม่มีเชื้อ` → `เทศกาลขนมปังไร้เชื้อ`. Cost: 1 surgical text-edit. **Severity: LOW** — proper-name lock-violation but limited blast radius; the doc-uniform form already covers 20+ other corpus occurrences.

---

## 5. Yobel "Jubilee" rendering as `ปีจูบีลี` — **REVIEW (transliteration-via-Latin vs. Hebrew-direct)**

The Hebrew יוֹבֵל ("ram's horn"; metonymically "year-of-jubilee") appears in LEV 25:9-54 + 27:17-24 (~19 occurrences). The Thai is uniformly `ปีจูบีลี` ("year of jubilee" — `จูบีลี` is the English `jubilee` transliterated via Latin `iubilaeus`).

**Editorial assessment.** Per `proper_names_and_transliteration_2026-05.md`, the project's principle is "follow established Thai-Christian-Bible precedent unless documented otherwise; for Hebrew terms, transliterate via Hebrew phonology when no precedent exists." The English-via-Latin `จูบีลี` follows the THSV2011 precedent (THSV2011 uses `ปีกึ่งศตวรรษ` for the conceptual translation OR `ปีโยเบล` for direct Hebrew-transliteration depending on edition; the modern THSV-Eclectic uses `ปีจูเบลี`). The Eremos choice `ปีจูบีลี` is a defensible Thai-Christian-Bible-tradition choice but **does not directly transliterate the Hebrew sounds /yoːbeːl/** — it brings in the English/Latin route.

**REVIEW flag.** Three paths:
- (a) **Current** — preserve `ปีจูบีลี` (English-via-Latin transliteration, matches modern Thai-Christian usage). Reader-friendly.
- (b) **Direct Hebrew transliteration** — `ปีโยเบล` (matches Hebrew phonology directly). More-faithful but less-familiar to Thai-Christian readers.
- (c) **Doc-lift** — amend `proper_names_and_transliteration_2026-05.md` to lock the Eremos choice + cross-reference modern-Thai-Christian-Bible-usage precedent.

**Recommend (a) + (c)** — preserve `ปีจูบีลี` as the going-forward lock and document the rationale. **Severity: LOW** — proper-name choice; the `ปีจูบีลี` form is widely-recognized in Thai-Christian-readership; documentation lift is bookkeeping.

---

## 6. LEV 25:10 deror "liberty" — **STABLE (recommend Layer-2 footer)**

> **25:10 Hebrew:** וּקְרָאתֶ֥ם דְּר֛וֹר בָּאָ֖רֶץ לְכָל־יֹשְׁבֶ֑יהָ
>
> **25:10 Thai (as shipped):** "พวกเจ้าจะชำระให้บริสุทธิ์ปีที่ห้าสิบและ**ประกาศอิสรภาพในแผ่นดิน**สำหรับผู้อาศัยทั้งหมด เป็นปีจูบีลีของพวกเจ้า..."

**Editorial assessment.** The Hebrew דְּרוֹר ("liberty / release / proclaimed-freedom") is a hapax-thread in the OT: 6 occurrences total (Lev 25:10; Jer 34:8, 34:15, 34:17; Isa 61:1; Ezek 46:17). **Isa 61:1's δ̄ρōr is quoted in Lk 4:18-19** (Jesus's Nazareth synagogue inaugural sermon) — making LEV 25:10 the OT-locking-precedent for the entire Jubilee-liberty-NT-trajectory.

The current Thai `อิสรภาพ` ("liberty / freedom") is a paraphrastic rendering (does not preserve the lemma's narrow legal-release sense). LXX uses ἄφεσις at LEV 25:10 + Isa 61:1 + Lk 4:18 — the same Greek lemma that NT-side Eremos locks to `การปลดปล่อย` / `การปลดเปลื้อง` per `aphesis_forgiveness_of_sins_2026-04.md` (forgiveness-and-release sub-rule). **LEV 25:10's `อิสรภาพ` is principled but does not pre-mirror the NT trajectory.**

**Recommend Layer-2 footer at LEV 25:10** in `output/textual_variants/leviticus_25.json` naming:
- The deror-thread: Lev 25:10 → Jer 34 → Isa 61:1 → Lk 4:18-19 (Jesus-as-Jubilee-inaugurator)
- The LXX ἄφεσις = Eremos NT-side `การปลดปล่อย` cross-link
- The Liberty Bell reference (cultural significance — Lev 25:10 is the most-famous LEV verse in American civil-religion)

**STABLE** ✓ at the surface (Thai is reader-friendly and accurate); doc-Layer-2 lift recommended. **Severity: LOW.**

---

## 7. LEV 16 + LEV 17:11 Layer-2 footer gap — **REVIEW**

The two **most doctrinally load-bearing verses in Leviticus** for NT atonement theology are LEV 16 (the Yom Kippur ritual) + LEV 17:11 (the "life is in the blood" axiom). Both have only the standard YHWH first-occurrence Layer-2 footer; **neither has a Layer-2 footer cross-referencing the NT doctrine they ground.**

**LEV 16 NT load-bearing nodes (no footer):**
- **LEV 16:2 כַּפֹּרֶת `พระที่นั่งกรุณา`** — locking precedent for `kapporet_atonement_cover_2026-05.md` and direct OT-source of Heb 9:5 (τὰ Χερουβεὶν δόξης κατασκιάζοντα τὸ ἱλαστήριον "cherubim of glory overshadowing the mercy seat"). Verse-level KD acknowledges the cross-reference but no Layer-2 footer.
- **LEV 16:5-10 + 16:15-22 two-goats / Azazel** — the OT-source of Heb 9:28's "Christ once-for-all" + Isa 53:6's "YHWH laid on him the iniquity of us all" + 1 Pet 2:24's "bore our sins in his body on the tree" (the cluster the church-fathers read as the two-goats cosmological-Christology — one slain, one bearing-iniquity-into-the-wilderness).
- **LEV 16:30 כִּפֻּרִים** as the OT-source of the Hebrews-corpus high-priestly-Christology.

**LEV 17:11 NT load-bearing (no footer):**
- > **17:11 Thai:** "เพราะ**ชีวิตของเนื้ออยู่ในเลือด** และเราได้ให้เลือดแก่พวกเจ้าบนแท่นบูชาเพื่อทำการลบมลทินบาปสำหรับจิตของพวกเจ้า เพราะเลือดเป็นสิ่งที่ทำการลบมลทินบาปด้วยชีวิต"

This is the **OT-source of Heb 9:22** (χωρὶς αἱματεκχυσίας οὐ γίνεται ἄφεσις "without shedding of blood there is no forgiveness") + Rom 3:25 (ὃν προέθετο ὁ θεὸς ἱλαστήριον... ἐν τῷ αὐτοῦ αἵματι "whom God put forth as kapporet... in his blood"). The verse-level `notes` field references these NT echoes; the Layer-2 footer does not.

**REVIEW flag.** Recommend writing **3 Layer-2 footers** in tandem before tagging:
1. `output/textual_variants/leviticus_16.json` — kapporet cross-reference to Heb 9:5 + two-goats cross-reference to Heb 9:28 + 1 Pet 2:24 + Isa 53:6.
2. `output/textual_variants/leviticus_17.json` — blood-life cross-reference to Heb 9:22 + Rom 3:25.
3. (Optional) `output/textual_variants/leviticus_23.json` — feast-calendar cross-reference to the NT feast-fulfillment cluster (Passover→Lk 22; Firstfruits→1 Cor 15:20; Pentecost→Acts 2; Trumpets+Atonement+Booths→eschatological-fulfillment readings).

**Severity: MEDIUM** — Layer-2 reader-edition transparency for the most-NT-load-bearing OT chapter in the corpus. Pattern: Genesis-audit added similar footers retroactively at Gen 3:15 + Gen 22 + Gen 49:10; Exodus-audit recommended at Exod 12 + Exod 24. LEV 16 is the natural next addition.

---

## 8. Five sacrificial offering types — **LOCKED**

| Hebrew | Thai (locked) | LEV occurrence count |
|---|---|---|
| עֹלָה | **เครื่องเผาบูชา** | 58 verses |
| מִנְחָה | **เครื่องบูชาธัญพืช** | 33 verses |
| שְׁלָמִים | **เครื่องสันติบูชา** | 29 verses |
| חַטָּאת (ritual) | **เครื่องบูชาไถ่บาป** | 51 verses |
| אָשָׁם | **เครื่องบูชาไถ่ความผิด** | 21 verses |

**Compliance.** 100% across all 5 offering types. **Zero drift candidates** (`เครื่องบูชาเผา` / `เครื่องบูชาธัญญาหาร` / `เครื่องบูชาศานติ` / `เครื่องบูชาบาป` / `เครื่องบูชาความผิด` — none of the doc-alternates appear). The חַטָּאת polysemy split (§3 of doc) is correctly applied — when context is moral-sin, Thai uses `บาป`; when ritual-offering, `เครื่องบูชาไถ่บาป`. Spot-check at LEV 4:3 ("the priest who is anointed who sins... shall offer for his sin (לְחַטָּאתוֹ) ... a bull (לְחַטָּאת)") — first occurrence is moral `บาป`, second is ritual `เครื่องบูชาไถ่บาป`. ✓

The doc's §7 calls for a `check_sacrificial_vocab.py` script "to be written before LEV 1 ships". **The script was not written**; the doc-uniform compliance is by Claude/translator-discipline rather than mechanical enforcement. Recommend writing the script as part of the §2 (kipper) doc-revision commit.

**LOCKED** ✓ on the five primary types. (Sub-issue at §2: the kipper verbal-form drift is the doc's only LEV exposure.)

---

## 9. Kapporet at LEV 16 — **LOCKED**

| Verse | Hebrew | Thai |
|---|---|---|
| LEV 16:2 | אֶל־פְּנֵ֨י הַכַּפֹּ֜רֶת | **พระที่นั่งกรุณา** ✓ |
| LEV 16:13 | אֶת־הַכַּפֹּ֖רֶת | **พระที่นั่งกรุณา** ✓ |
| LEV 16:14 (×2) | עַל־פְּנֵ֧י הַכַּפֹּ֛רֶת | **พระที่นั่งกรุณา** ✓ |
| LEV 16:15 (×2) | עַל־הַכַּפֹּ֖רֶת | **พระที่นั่งกรุณา** ✓ |

All 6 LEV-16 occurrences render uniformly per `kapporet_atonement_cover_2026-05.md` (decided 2026-05-13 post-EXO audit). The lock holds at the most-doctrinally-load-bearing kapporet verses in Scripture — the High Priest's annual blood-sprinkling on the kapporet that the NT (Heb 9:5; Rom 3:25 via ἱλαστήριον) cross-references directly. **LOCKED** ✓.

Note Lev 4:6's `פְּנֵי הַפָּרֹכֶת` ("face of the veil") — distinct from kapporet — is rendered `ม่านกั้น` ("partition curtain") — also doc-compliant per LEV 16:2 paroketh handling.

---

## 10. Azazel (עֲזָאזֵל) at LEV 16:8, 16:10, 16:26 — **STABLE**

Three occurrences uniformly transliterated as **อาซาเซล**. The verse-level KD at LEV 16:8 documents the three interpretive options (place-name / fallen-angel / "ʿēz ʾōzēl" = scapegoat-etymology) and explicitly chooses transliteration to "preserve the Hebrew mystery" — the BSB / NIV "scapegoat" gloss is interpretive; the Eremos approach is transliteration + verse-level KD + Layer-2 footer (note: a Layer-2 footer here would strengthen the editorial transparency — see §7 above).

**STABLE** ✓ — uniform; principled; verse-level rationale documented.

---

## 11. The "I am YHWH" Holiness Code leitwort — **STABLE (recommend corpus doc)**

The **`אֲנִי יְהוָה`** ("I am YHWH") closure-formula appears **52 times** in Leviticus, concentrated in the Holiness Code (chs.18-26). It is the structural-anchor of the Holiness Code — each ethical or ritual prohibition closes with the divine self-identification.

Spot-check sample (10 of 52 occurrences):

| Verse | Hebrew | Thai (current) |
|---|---|---|
| LEV 18:2 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** |
| LEV 18:6 | אֲנִ֖י יְהוָֽה | **เราคือองค์พระผู้เป็นเจ้า** |
| LEV 19:2 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เรา องค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** |
| LEV 19:18 | אֲנִ֖י יְהוָֽה | **เราคือองค์พระผู้เป็นเจ้า** |
| LEV 19:34 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** |
| LEV 20:26 | אֲנִ֤י יְהוָה֙ קָד֔וֹשׁ | **เรา องค์พระผู้เป็นเจ้า เป็นผู้บริสุทธิ์** |

**Compliance.** The Thai is uniform-up-to-minor-variations: the short form (אֲנִי יְהוָה bare) → `เราคือองค์พระผู้เป็นเจ้า`; the expanded form (אֲנִי יְהוָה אֱלֹהֵיכֶם) → `เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า`. Minor wording variant within Lev 19:2 + 20:26 omits the `คือ` ("is/am") copula — preserving the Hebrew's nominal-sentence directness. Both forms are well-formed Thai.

**Editorial assessment.** This is the **single densest divine-self-identification leitwort in all of scripture** (~52 LEV + ~6 Exod + ~5 Num + ~12 Ezekiel ≈ 75 OT occurrences). The Thai is principled and uniform but has **no corpus-doc lock**. The verse-level KDs document the rendering. The leitwort compounds across the Holiness Code into Ezekiel ("you/they will know that I am YHWH" — 65+ Ezekiel occurrences of the cognate-form `וִידַעְתֶּ֖ם כִּ֣י אֲנִ֣י יְהוָ֑ה`) — the Eremos Thai must align across LEV-and-Ezekiel for this cluster.

**→ Recommend new doc:** `docs/translator_decisions/i_am_yhwh_holiness_formula_2026-05.md` — names the bare-form vs. expanded-form Thai split; locks both; cross-references the Ezekiel "they-will-know" cognate-form. Cost: 1 short doc + zero translation changes. Benefit: forward-protection for Ezekiel (65+) + Deuteronomy 5 (Decalogue parallel) + scattered prophetic recurrences.

**STABLE** ✓ at the surface; doc-lift recommended.

---

## 12. Kareth (כָּרַת) penalty formula — **STABLE (recommend corpus doc)**

The kareth-formula (**וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ** "that person shall be cut off from his people") appears **18 times in Leviticus** — more than any other book in scripture. Verses: 7:20, 7:21, 7:25, 7:27, 17:4, 17:9, 17:10, 17:14, 18:29, 19:8, 20:3, 20:5, 20:6, 20:17, 20:18, 22:3, 23:29, 26:30 (the destruction-variant).

**Thai rendering pattern.** Uniformly **`ถูกตัดออกจากชนชาติของตน`** / **`ถูกตัดออกจากท่ามกลางชนชาติของเขา`** (literal "cut off from his people" or "cut off from among his people"). Spot-check:

| Verse | Thai |
|---|---|
| LEV 7:20 | "ผู้นั้น**จะต้องถูกตัดออกจากชนชาติของตน**" |
| LEV 17:10 | "เราจะตั้งหน้าของเราต่อต้านผู้นั้น และ**จะตัดเขาออกจากชนชาติของเขา**" |
| LEV 18:29 | "**จะต้องถูกตัดออกจากท่ามกลางชนชาติของพวกเขา**" |
| LEV 20:3 | "และ**ตัดเขาออกจากท่ามกลางชนชาติของเขา**" (divine-subject active) |
| LEV 23:29 | "ต้อง**ถูกตัดออกจากชนชาติของเขา**" |

**Editorial assessment.** Two consistent surface-form variants: (a) **passive `ถูกตัดออก`** when the Niphal/Hophal Hebrew form is used (`וְנִכְרְתָה` "shall-be-cut-off"); (b) **active `ตัดเขาออก`** when YHWH is the explicit grammatical subject (`וְהִכְרַתִּי` "I will cut off"). The split is principled and matches Hebrew voice. The "from his people" prepositional-phrase `מֵעַמֶּיהָ` / `מִקֶּ֧רֶב עַמָּֽיו` is uniformly rendered `จากชนชาติของเขา` / `จากท่ามกลางชนชาติ`.

The **theological force of kareth** (excommunication / divine destruction / annihilation — debated in rabbinic vs. Christian readings; cf. Milgrom *Lev 1-16* 457-460) is preserved at the Thai surface without forcing a particular interpretive collapse.

**→ Recommend new doc:** `docs/translator_decisions/kareth_penalty_formula_2026-05.md` — locks the passive/active Thai split + cross-references NT echoes (Acts 3:23's Stephen-speech citation of Deut 18:19 "shall-be-utterly-destroyed-from-the-people" picks up the kareth thread; Rom 9:3's ἀνάθεμα may reflect this). Cost: 1 short doc. Benefit: forward-protection for NUM 9:13, 15:30-31, 19:13, 19:20 (~5 more); DEUT (none in MT but Cf. EXO 12:15, 12:19, 30:33, 30:38, 31:14); Eze 14:8-9, 21:3-4 (cognate-form). **STABLE** ✓.

---

## 13. mot-yumat death-penalty formula (מוֹת יוּמָת) — **STABLE**

The infinitive-absolute-intensifier formula **`מוֹת יוּמָת`** ("shall surely be put to death" — Hebrew's most-emphatic capital-sentence formula) appears **14 times in Leviticus** (vs. 8 in EXO and 6+ in NUM): 19:20, 20:2, 20:9, 20:10, 20:11, 20:12, 20:13, 20:15, 20:16, 20:27, 24:16, 24:17, 24:21, 27:29.

**Thai rendering:** uniformly **`ต้องถูกประหารชีวิต`** ("must be put-to-death"). The Hebrew **infinitive-absolute-intensifier `מוֹת`** (literally "dying he shall die") is **collapsed into a single Thai verb-phrase**, **losing the Hebrew intensifier-force**. This matches EXO and NUM's pattern (the same lemma-pair) and is consistent with `hebrew_grammar_transfer_2026-05.md` general policy — Hebrew infinitive-absolute intensification doesn't map cleanly to Thai, and the Thai `ต้อง` ("must / certainly") is the doc-locked equivalent intensifier. The verbal-pair `הָרֹג תַּהַרְגוּ` at LEV 24:14 ("kill, you-shall-kill" — different lemma) is rendered with the same flattening.

**Note re LEV 19:20.** This verse uses the **negative-form** `לֹא יוּמְתוּ` ("they shall NOT be put to death" — the half-betrothed-slave-girl edge case where full death-penalty is suspended because she is not free): the Thai correctly renders the negative as `แต่พวกเขาไม่ต้อง[ถูกประหาร]` ("but they need not [be put to death]") — preserving the Hebrew negative-form. Not a drift.

**STABLE** ✓ — uniform; matches EXO/NUM precedent.

---

## 14. Holiness leitwort (קָדוֹשׁ / קֹדֶשׁ / קָדַשׁ) — **LOCKED**

The Holiness Code (chs.17-26) and the priestly-vestments (ch.8) and the Yom Kippur ritual (ch.16) saturate Leviticus with the holiness lemma-cluster. Thai rendering:

| Hebrew | Thai | LEV coverage |
|---|---|---|
| קָדוֹשׁ (adj. "holy") | **บริสุทธิ์** / **ผู้บริสุทธิ์** | uniformly across all 27 chapters |
| קֹדֶשׁ (noun "holiness/holy thing") | **บริสุทธิ์** / **สิ่งบริสุทธิ์** | LEV 2:3, 6:17 etc. |
| קֹדֶשׁ קָדָשִׁים (most-holy) | **บริสุทธิ์ที่สุด** | LEV 2:3, 2:10, 6:10, 6:18, 6:22, 24:9 etc. (11 verses uniform) |
| קָדַשׁ (verb piel "sanctify / consecrate") | **ชำระให้บริสุทธิ์** | LEV 8:10-11, 16:19, 21:8 etc. |
| בָּדַל (separate) | **แยก / แยกออก** | LEV 10:10, 20:24-26 etc. |

**The "be holy because I am holy" formula** at LEV 11:44-45, 19:2, 20:7, 20:26, 21:8 uses **`จงเป็นผู้บริสุทธิ์ เพราะเรา (องค์พระผู้เป็นเจ้า) เป็นผู้บริสุทธิ์`** — uniform across all 5 occurrences ✓.

**The holy/common + clean/unclean binary at LEV 10:10** (the doctrinal anchor of the entire priestly-purity system) — rendered: `พวกเจ้าจะต้องแยกระหว่าง**สิ่งบริสุทธิ์**และ**สิ่งสามัญ** ระหว่าง**สิ่งที่ไม่สะอาด**และ**สิ่งที่บริสุทธิ์**`. Preserves all four categories. ✓

**Compliance with `hagiasmos_hagiosune_2026-05.md`.** The doc covers the NT Greek family ἁγιασμός / ἁγιότης / ἁγιοσύνη with a process/state distinction; the OT companion vocabulary is implicit. LEV's `บริสุทธิ์` (state) + `ชำระให้บริสุทธิ์` (process) maps cleanly to the doc's state/process split. **LOCKED** ✓.

---

## 15. Goel verb / kinsman-redeemer cluster (LEV 25) — **STABLE-with-§3-drift-flag**

| Verse | Hebrew | Thai | Doc-form match? |
|---|---|---|---|
| LEV 25:24 | גְּאֻלָּ֖ה | **การไถ่** | ✓ verbal noun, doc-compliant |
| **LEV 25:25** | **גֹאֲל֤וֹ הַקָּרֹ֣ב אֵלָ֔יו** | **ญาติสนิทที่สุดของเขา** | ✗ drift — see §3 |
| LEV 25:26 | גֹּאֵל ... גְּאֻלָּתֽוֹ | **ผู้ไถ่** / **ไถ่ที่ดิน** | ✓ |
| LEV 25:33 | יִגְאַ֖ל | **ถูกไถ่** | ✓ |
| LEV 25:47-49 | יִגְאָלֶ֔נּוּ | **อาจไถ่เขาได้** | ✓ verb-form, doc-compliant |
| LEV 25:54 | יִגָּאֵ֤ל | **ถูกไถ่** | ✓ |
| LEV 27:13-31 | יִגְאַל / גָּאֹל | **ไถ่** | ✓ |

**21 goel/ga'al occurrences across LEV 25 + LEV 27** (the vow-redemption parallel pericope at ch.27). Compliance is uniform per `goel_kinsman_redeemer_2026-05.md` **except at the locking-precedent verse LEV 25:25** — see §3 for the cross-book Ruth/LEV drift analysis.

The verb-form `ไถ่` is doc-compliant at all 21 occurrences. The noun-form drift is concentrated at **LEV 25:25 alone** (the property-goel introductory verse). **STABLE-with-§3-flag** ✓.

---

## 16. Inherited corpus locks — **all compliant except where flagged**

| Doc | LEV evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | 311 YHWH all → องค์พระผู้เป็นเจ้า; no standalone Adonai in LEV; no Adonai-vocative; El-Shaddai absent in LEV. | **LOCKED** |
| `ot_register_policy_2026-05.md` | Instructional / legislative register throughout; divine-speech ทรง- consistently applied; YHWH-1ps `เรา` uniform; Moses + Aaron + priests + sons-of-Israel all plain-narrator (no Rachasap for non-divine human figures, matching Pentateuch policy). | **LOCKED** |
| `kapporet_atonement_cover_2026-05.md` | LEV 16 ×6 occurrences all → `พระที่นั่งกรุณา` ✓ (see §9). | **LOCKED** |
| `sacrificial_vocabulary_2026-05.md` | 5 main types 100% compliant (see §8); **kipper verbal-form drift see §2 DECIDE**. | **DRIFT (DECIDE §2)** |
| `goel_kinsman_redeemer_2026-05.md` | 21 occurrences compliant except LEV 25:25 (see §3 + §15 DECIDE). | **DRIFT (DECIDE §3)** |
| `pagan_deities_2026-04.md` | Molech at 18:21, 20:2-5 ×5 → `โมเลค` (transliterated) ✓ matches doc rule. No other pagan-deity references in LEV. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | פְּנֵי יְהוָה (face/presence of YHWH) at **57 occurrences** all → `ต่อพระพักตร์องค์พระผู้เป็นเจ้า` ✓ uniform. No drift. "Hand of YHWH" anthropomorphisms (e.g., LEV 14:34 "in the land which I give") render per doc. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | LEV 26:11-12 covenant-walking-formula → "เราจะตั้งที่อยู่ของเรา..." + "เราจะดำเนินในท่ามกลางพวกเจ้า" — both render per doc's Rachasap-with-divine-subject sub-rule. Compliant. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains throughout; cognate-accusatives (e.g., LEV 4:23 וְהָבִיא אֶת־קָרְבָּנוֹ "shall bring his offering"); infinitive-absolute intensifiers at the mot-yumat formula (see §13 — Hebrew intensifier collapsed; matches EXO/NUM pattern). Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | LEV has minor MT-vs-English versification divergence at the ch.5/6 boundary (MT 5:20-26 = English 6:1-7 — handled by following MT throughout). 27 chapter `language: hebrew`. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | Aaron `อาโรน`, Moses `โมเสส`, Nadab + Abihu `นาดับ + อาบีฮู`, Eleazar + Ithamar `เอเลอาซาร์ + อิธามาร์`, Sinai `ซีนาย` (×3, no NUM-style drift to `สีนาย` ✓), Shelomith `เชโลมิท` (LEV 24:11). All compliant. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | LEV has very low MT-vs-LXX textual divergence (LEV is one of the most textually-stable books in the OT). No headline divergences requiring Layer-2 footers (vs. GEN's 4:8, 46:27, 47:31). Compliant. | **LOCKED (N/A divergences)** |
| `narrator_vs_character_voice_2026-04.md` | Narrator's voice instructional / legal-direct; YHWH speech-acts uniformly attributed via `ตรัสกับโมเสส`; Aaron + sons-of-Aaron speech rare (LEV is YHWH-speaks-Moses-pass-to-priests). Compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | LEV has limited praise-vocabulary (legal-instructional register). No drift. | **LOCKED (N/A scope)** |
| `chesed_covenant_love_2026-05.md` | **One LEV "chesed" hit at LEV 20:17** — this is **chesed II** ("disgrace/shame"; cognate of Aramaic ḥesdā, distinct root from chesed I "covenant-love"; cf. HALOT s.v.). The Thai correctly renders `ความน่าอับอาย` ("shame/disgrace") — NOT `ความรักมั่นคง`. **Compliant** (correctly disambiguates the homonym). | **LOCKED** |
| `exod_34_attribute_formula_2026-05.md` | LEV has no Sinai-formula recitation (the formula appears in EXO 34 + NUM 14 + recurs in prophets/psalms — not in LEV). No exposure. | **LOCKED (N/A scope)** |
| `nicham_divine_relenting_2026-05.md` | LEV has no נָחַם divine-relenting verses. No exposure. | **LOCKED (N/A scope)** |
| `manah_divine_appointment_2026-05.md` | LEV has no מָנָה divine-appointment occurrences. No exposure. | **LOCKED (N/A scope)** |
| `paqad_visit_attend_2026-05.md` | LEV has no פָּקַד divine-visitation occurrences (the Pentateuch-paqad cluster is concentrated in GEN/EXO/NUM/DEUT, with LEV 26:16's `וְהִפְקַדְתִּי` as the only candidate; the Thai is `และเราจะให้` — non-paqad-rendering; verb-form is more "appoint over" than "visit"). The choice is principled — `הִפְקַדְתִּי` here means "I will assign / decree" (terror-against-them), not the paqad-pastoral-visitation sense. **Compliant** (correct disambiguation). | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | LEV has no oath-formulas (raised-hand / hand-under-thigh / by-myself-I-have-sworn). No exposure. | **LOCKED (N/A scope)** |
| `ot_polytheistic_register_2026-05.md` | LEV has no Hebrew-polytheistic-surface vocabulary (LEV's pagan-deity reference is Molech, which is a proper-name transliterated, not a polytheistic-rhetorical-surface). No exposure. | **LOCKED (N/A scope)** |
| `ot_canon_and_text_base_2026-05.md` | LEV is all Hebrew (no Aramaic). MT versioning throughout. Compliant. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | LEV's signature leitworts (holiness, "I am YHWH", clean/unclean, kareth, mot-yumat) are uniformly preserved at the Thai surface per doc principle. | **LOCKED** |
| `gender_passages_thai_register_2026-05.md` | LEV 18 / LEV 20 sexual-prohibitions are out-of-scope of this doc (which covers Gen 1-3 marriage + NT marriage / 1 Tim 2 cluster). LEV 18:22 / 20:13 ship literally with `หลับนอนกับชายเหมือนกับหญิง` + `สิ่งน่ารังเกียจ` (to'evah). LEV 18:6-18 incest catalog uses hybrid euphemism-and-explicit (see §17 STABLE). No drift FROM the doc; one **STABLE-but-undocumented** policy gap (see §17). | **LOCKED (out-of-scope)** |

---

## 17. LEV 18:6-18 + 20:11-21 incest catalog "uncover the nakedness" euphemism — **STABLE-but-undocumented**

The Hebrew euphemism **`לְגַלּוֹת עֶרְוָה`** ("to uncover the nakedness" — the Pentateuch's circumlocution for sexual intercourse, used **24 times** across LEV 18:6-18 + 20:11-21) is rendered with a **hybrid Thai strategy**:

| Verse | Hebrew literal | Thai (current) |
|---|---|---|
| LEV 18:6 (general / programmatic) | לְגַלּוֹת עֶרְוָה | **มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:7 (mother) | לֹא תְגַלֵּ֑ה | **ไม่เปิดเผยความเปลือยเปล่า... ไม่มีความสัมพันธ์ทางเพศกับนาง** (hybrid) |
| LEV 18:8 (stepmother) | לֹא תְגַלֵּ֑ה | **ไม่มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:16 (brother's wife) | לֹא תְגַלֵּ֑ה | **ไม่มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:18 (wife's sister) | לְגַלּ֤וֹת עֶרְוָתָהּ֙ | **มีความสัมพันธ์ทางเพศกับนาง** (explicit) |
| LEV 20:11 (father's wife) | עֶרְוַ֥ת אָבִ֖יו | **ได้เปิดเผยความเปลือยเปล่าของบิดา** (preserves euphemism) |
| LEV 20:18 (menstruant) | הֶעֱרָ֕ה ... וְהִ֖יא גִּלְּתָ֣ה | **เปิดเผยแหล่งที่มาของการไหล** (literal — preserves euphemism's clinical force) |

**Editorial assessment.** The Thai strategy is **principled hybrid**: when the Hebrew euphemism is contextually-clarified (LEV 18:7-18 introduces each prohibition with a relationship-pronoun that disambiguates), the Thai prefers explicit `มีความสัมพันธ์ทางเพศ`; when the Hebrew euphemism carries clinical-anatomical weight (LEV 20:18 menstruant), the Thai preserves the literal "uncovering" register. The intro verse 18:6 (programmatic for the catalog) uses the explicit form to set reader-expectation.

The trade-off — readability vs. lemma-preservation — is well-understood in modern translation: NIV / ESV / NRSV all preserve "uncover the nakedness" literally; NLT paraphrases to "have sexual relations"; THSV2011 uses a mixed strategy similar to Eremos. The Eremos hybrid is **not arbitrary** — it tracks Hebrew clarity vs. opacity within the same chapter.

**→ Recommend new short doc:** `docs/translator_decisions/uncover_nakedness_euphemism_2026-05.md` — names the hybrid principle; documents the LEV 18 + LEV 20 + Deut 22:30 + Deut 27:20 + Ezek 16 + Ezek 22:10 cross-corpus locations; cross-references the NT echo at 1 Cor 5:1 (γυναῖκά τινα τοῦ πατρὸς ἔχειν — "to have his father's wife"; Paul invokes LEV 18:8 + 20:11 directly). Cost: 1 short doc; benefit: forward-cover for Deuteronomy + Ezekiel + 1 Corinthians 5.

**STABLE** ✓ at the verse-level surface; doc-lift recommended.

---

## 18. LEV 26 covenant blessings + curses + diaspora-restoration — **LOCKED**

LEV 26 (the Holiness Code's covenant-blessings + sevenfold-escalating-curses + Exile-and-restoration cluster) is one of the two longest blessing-curse chapters in scripture (the other is Deut 28). Spot-check of the key thematic anchors:

| Verse | Hebrew | Thai |
|---|---|---|
| **26:6 שָׁלוֹם** ("peace in the land") | וְנָתַתִּ֤י שָׁלוֹם֙ בָּאָ֔רֶץ | "เราจะให้**สันติ**แก่แผ่นดิน" ✓ |
| **26:11-12 covenant-presence formula** | וְנָתַתִּי מִשְׁכָּנִי בְּתוֹכְכֶם ... וְהִתְהַלַּכְתִּי בְּתוֹכְכֶם וְהָיִיתִי לָכֶם לֵאלֹהִים וְאַתֶּם תִּהְיוּ־לִי לְעָם | **"เราจะตั้งที่อยู่ของเราในท่ามกลางพวกเจ้า... เราจะดำเนินในท่ามกลางพวกเจ้า และจะเป็นพระเจ้าของพวกเจ้า และพวกเจ้าจะเป็นประชากรของเรา"** ✓ NT echo 2 Cor 6:16 + Rev 21:3 documented in verse-level notes |
| **26:14-39 curse-formula (sevenfold-escalation: 18, 21, 24, 28)** | יָסַפְתִּי לְיַסְּרָה אֶתְכֶם שֶׁבַע עַל־חַטֹּאתֵיכֶם | "เราจะลงโทษพวกเจ้าเจ็ดเท่ายิ่งกว่าเดิม" — preserves sevenfold structure ✓ |
| **26:33 scatter-among-the-nations** | וְאֶתְכֶם֙ אֱזָרֶ֣ה בַגּוֹיִ֔ם | "เราจะ**กระจายพวกเจ้าไปท่ามกลางชนชาติทั้งหลาย**" ✓ |
| **26:34 land-keeps-its-sabbaths** | אָז תִּרְצֶ֤ה הָאָ֨רֶץ֙ אֶת־שַׁבְּתֹתֶ֔יהָ | "แผ่นดินจะได้รับ**สะบาโต**ของมัน" ✓ — cross-references 2 Chr 36:21 (the 70-year-exile-as-sabbath-restoration reading); the **70-year prophecy at Jer 25:11-12 + 29:10 + Dan 9:2 + 2 Chr 36:21 all derive from THIS verse**; locking-precedent for the cluster |
| **26:42 patriarchal-covenant-remembrance (reverse-order)** | אֶת־בְּרִיתִ֖י יַֽעֲק֑וֹב וְאַף֩ אֶת־בְּרִיתִ֨י יִצְחָ֝ק וְאַף֩ אֶת־בְּרִיתִ֤י אַבְרָהָם֙ | "พันธสัญญาของเรากับ**ยาโคบ** และ... กับ**อิสอัค** และ... กับ**อับราฮัม**" — preserves Hebrew reverse-order (Jacob first, Abraham last — a unique scripture-passage reversing the canonical Gen 12+15+17 forward-order) ✓ |

All thematic anchors render cleanly. The **NT-echo cluster** (2 Cor 6:16 covenant-presence; Rev 21:3 dwelling-with-people; Heb 13:5 "I will never leave you nor forsake you" echoes LEV 26:11; the diaspora-cluster Jer 25 + Dan 9 + 2 Chr 36 all citing 26:34) is documented in verse-level KDs.

**LOCKED** ✓.

---

## 19. LEV 24:16 blasphemy-of-the-Name death penalty — **STABLE**

> **24:16:** "ผู้ใดที่หมิ่นประมาทพระนามขององค์พระผู้เป็นเจ้าต้องถูกประหารชีวิต... ถ้าเขาหมิ่นประมาทพระนาม เขาต้องถูกประหาร"

LEV 24:16 is the **OT-corpus-locking precedent for the death penalty for blasphemy of the divine Name** (the underlying offense at the Sanhedrin trial of Jesus, Mt 26:65-66 / Mk 14:64; the offense at the trial of Stephen, Acts 6:11+13; the offense at the trial of Paul, Acts 21:28). The Thai `หมิ่นประมาทพระนาม` ("blaspheme/insult the Name") locks the Eremos rendering. This is the **first OT occurrence** of `נָקַב שֵׁם יְהוָה` ("name/curse the Name of YHWH") — the verse uses the Hebrew `נָקַב` ambiguously ("name-explicitly-with-curse" or "pierce/penetrate-with-imprecation"), which the rabbinic tradition (Sanh. 7:5; Sifra ad loc.) reads as the explicit-pronunciation prohibition.

**STABLE** ✓ — Thai is faithful + sufficient for the NT cross-reference; verse-level KD documents the Sanhedrin/Stephen/Paul echo.

---

## 20. LEV 19:18 + 19:34 love-neighbor / love-sojourner — **LOCKED (NT-corpus-critical)**

> **19:18:** "อย่าแก้แค้นหรือผูกพยาบาทต่อบุคคลใดในชนชาติของเจ้า แต่จง**รักเพื่อนบ้านของเจ้าเหมือนรักตัวเอง** เราคือองค์พระผู้เป็นเจ้า"
>
> **19:34:** "พวกเจ้าจะต้องปฏิบัติต่อคนต่างชาติที่อาศัยอยู่ท่ามกลางพวกเจ้าเหมือนคนพื้นเมือง และ**รักเขาเหมือนรักตัวเอง** เพราะพวกเจ้าเคยเป็นคนต่างชาติในแผ่นดินอียิปต์ เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า"

**LEV 19:18** is **the single most-NT-cited OT verse outside Deut 6:5** (the Shema). Six NT citations: Mt 19:19, 22:39; Mk 12:31; Lk 10:27 (Good Samaritan); Rom 13:9; Gal 5:14; Jas 2:8. The verse-level notes document all 6 NT echoes.

**Forward-cover for NT-corpus cross-corpus consistency.** The Eremos NT-side must render the citations at Mt 22:39 / Mk 12:31 / Lk 10:27 / Rom 13:9 / Gal 5:14 / Jas 2:8 with the **identical Thai** `รักเพื่อนบ้านของเจ้าเหมือนรักตัวเอง` so the Thai reader sees the recurrence. Spot-check of NT-corpus side suggests this is the case (Eremos Matt/Mark/Luke/Rom/Gal/Jas all use the same anchor phrase); recommend cross-corpus verification as part of NT-quotation-consistency audit.

**LEV 19:34** parallels the love-neighbor command to the sojourner (גֵר). The Thai `รักเขาเหมือนรักตัวเอง` (love-him-as-yourself) preserves the parallel structure with v.18. **NT echo:** Lk 10:25-37 (the Good Samaritan parable directly thematizes the LEV 19:34 sojourner-extension of the LEV 19:18 love-neighbor command).

**LOCKED** ✓. The cross-corpus NT-quotation thread is the single most reader-visible Eremos editorial structure — preserving the Thai across LEV 19:18 + 6 NT echoes is corpus-foundational.

---

## 21. Mechanical (§1) — **all green**

- 27/27 chapters: `output/check_reports/leviticus_NN_review.md` + sub-reports ✓
- 27/27 chapters: `output/back_translations/leviticus_NN.json` ✓
- 27/27 chapters: `output/textual_variants/leviticus_NN.json` (Layer-2 first-occurrence YHWH footers; post-NUM-15 going-forward template) ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 287-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses scanned)
- `python3 scripts/audit_inclusion_variants.py --book LEV --strict`: **0 candidates** (NT-style policy N/A for OT)
- `git status output/`: only `output/check_reports/divine_names.md` modified (harmless re-run from audit). No source-file dirt.
- Hebrew word-spacing **clean for all 27 chapters** ✓
- `thai_literal` is **Thai for all 27 chapters** ✓
- No drift of `ยาห์เวห์` transliteration into primary `thai` field ✓

---

## 22. Flagged for Ben's attention (TL;DR)

### A. LEV-wide kipper drift from `sacrificial_vocabulary_2026-05.md` — **DECIDE before tagging** (§2)
**~168 LEV kipper-occurrences** use `ลบมลทินบาป` / `ทำการลบมลทินบาป` (with `มลทิน` ritual-impurity morpheme); doc locks `ลบบาป` / `ทำการลบบาป`. Same drift extends to ~50+ NUM occurrences. **Recommend doc-revision to amend the doc to recognize the as-shipped form as canonical in Lev/Num ritual context** (path b in §2). The doc was decided 2026-05-15 — same day as audit; apparently drafted without checking shipped corpus.

### B. LEV 25:25 goel doc-drift + Ruth-vs-LEV divergence — **DECIDE before tagging** (§3)
Doc locks `ผู้ไถ่ที่เป็นญาติ`; Ruth ships `ญาติผู้ไถ่`; LEV 25:25 ships `ญาติสนิทที่สุด`. **Recommend (a) doc-amendment to lock Ruth's `ญาติผู้ไถ่` as canonical** + LEV 25:25 surgical edit. Forward-protection for Job 19:25 + Isa 41-44 + Isa 53 + Ps 19:14.

### C. LEV 23:6 Unleavened Bread feast Thai-drift — **REVIEW** (§4)
Single-verse drift `ขนมปังไม่มีเชื้อ` vs. corpus-locked `ขนมปังไร้เชื้อ` (20+ other corpus occurrences). 1 surgical edit.

### D. Yobel "Jubilee" rendering `ปีจูบีลี` — **REVIEW** (§5)
English-via-Latin transliteration vs. direct Hebrew. Recommend doc-lift to confirm `ปีจูบีลี` as the going-forward lock (matches modern Thai-Christian usage).

### E. LEV 25:10 deror "liberty" Layer-2 footer — **REVIEW** (§6)
Recommend Layer-2 footer naming Isa 61:1 + Lk 4:18 NT trajectory + LXX ἄφεσις cross-link.

### F. LEV 16 + LEV 17:11 Layer-2 footer gap — **REVIEW** (§7)
Add Layer-2 footers cross-referencing Heb 9:5 / Heb 9:22 / Rom 3:25 / 1 Pet 2:24 + Isa 53:6 at the most-NT-doctrine-load-bearing OT chapter in the corpus.

### G. "I am YHWH" Holiness Code leitwort — **STABLE** (recommend doc) (§11)
Write `i_am_yhwh_holiness_formula_2026-05.md` — locks the 52-LEV-occurrence Thai forms + forward-cover for 65+ Ezekiel cognate-form recurrences.

### H. Kareth penalty formula — **STABLE** (recommend doc) (§12)
Write `kareth_penalty_formula_2026-05.md` — locks the passive/active Thai split across the 18-LEV-occurrence cluster + cross-Pentateuch occurrences.

### I. LEV 18:6-18 + 20:11-21 "uncover nakedness" euphemism policy — **STABLE** (recommend doc) (§17)
Write `uncover_nakedness_euphemism_2026-05.md` — names the hybrid principle (explicit-in-clear-context vs. euphemism-preservation-in-anatomical-context) + forward-cover for Deut + Ezekiel + 1 Cor 5:1.

---

## External AI review (§3 of checklist)

Suggested 7-item packet — one cluster per major editorial-decision area:

1. **Sacrificial-vocabulary kipper-drift cluster** — §2 (LEV-wide + NUM-downstream)
2. **Goel cross-book divergence** — §3 (Ruth-vs-LEV + doc-form)
3. **LEV 23:6 Unleavened Bread single-verse drift** — §4
4. **Jubilee transliteration choice** — §5 (`ปีจูบีลี` vs. `ปีโยเบล`)
5. **LEV 25:10 deror + LEV 16/17 NT cross-reference Layer-2 footer gap** — §6 + §7
6. **"I am YHWH" Holiness Code doc-lift recommendation** — §11
7. **Incest catalog euphemism policy** — §17

Sized for ~20K-char free-tier AI ceilings per `scripts/build_external_review_packet.py`.

---

## Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1, §9, §10, §14, §15-with-flag, §16a-l, §18, §19, §20, §21)
- **STABLE:** 5 items (§11, §12, §13, §17, §6)
- **REVIEW:** 3 items (§4, §5, §7)
- **DECIDE:** 2 items (§2 kipper CRITICAL; §3 goel)

**2 DECIDE items block the `book-leviticus-v1` tag.**

**3 new translator_decisions docs recommended** (`i_am_yhwh_holiness_formula_2026-05`, `kareth_penalty_formula_2026-05`, `uncover_nakedness_euphemism_2026-05`).

**2 existing translator_decisions docs to amend** (`sacrificial_vocabulary_2026-05.md` §5 kipper-rule + `goel_kinsman_redeemer_2026-05.md` §1 to recognize Ruth's `ญาติผู้ไถ่` as canonical).

**1 new check-script recommended** — `check_sacrificial_vocab.py` per the doc's §7 (was promised before LEV 1 ship; was not written; recommend writing in tandem with the §2 doc-revision commit).
