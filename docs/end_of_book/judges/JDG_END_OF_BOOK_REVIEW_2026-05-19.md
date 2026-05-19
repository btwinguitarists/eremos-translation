# Judges — End-of-Book Review

**Date:** 2026-05-19
**Scope:** All 21 chapters of Judges (618 verses; 913 verse-level `key_decisions`; 509 verses carrying notes); `glossary.json`; existing `docs/translator_decisions/` (87+ docs through the LEV / DEU / JOS end-of-book audits).
**Trigger:** JDG 21 shipped (commit `7844b37`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Eighth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua) and the **second Former-Prophets / Deuteronomistic-History book** — the first downstream test of every Joshua-era lock OUTSIDE Joshua itself.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 21/21 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `git status output/` clean; `output/textual_variants/judges_NN.json` present for all 21 chapters.
- **Judges is the first downstream stress-test of the JOS-audit findings.** Two of the three JOS-audit DECIDE / REVIEW items are implicitly resolved correctly in JDG:
  - **Seven-Nations ethnonyms — JDG matches JOS 3:10 / DEU 7:1 bare-suffix** (§4). The JOS 9:1+/24:11 -ต/-ไซต์ drift was NOT propagated forward. STABLE.
  - **mal'akh-YHWH compliant with the locked doc** (§3). All ~17 occurrences across 2:1+4, 5:23, 6:11–22 (Gideon), 13:3–21 (Manoah) uniformly render **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** / **ทูตสวรรค์ของพระเจ้า** (when Hebrew uses mal'akh-Elohim). LOCKED.
- **Judges introduces THREE major STABLE-but-undocumented patterns** that compound forward into 1–2 Sam + Heb 11:32:
  - **Spirit-of-YHWH 4-way principled split BY HEBREW VERB** (§5): תְּהִי עָלָיו → "มาเหนือ" (Othniel 3:10, Jephthah 11:29); לָבְשָׁה → "ทรงสวมทับ" (Gideon 6:34, lābash idiom); תָּחֶל לְפַעֲמוֹ → "เริ่มกระตุ้น" (Samson birth 13:25); תִּצְלַח עָלָיו → "มาเหนือเขาอย่างทรงพลัง" (Samson 14:6, 14:19, 15:14). Principled; not at corpus level. Will compound massively into 1 Sam 10:6, 10:10, 11:6, 16:13–14, 18:10, 19:9, 19:20, 19:23; 2 Sam 23:2.
  - **Judges cycle refrain + epilogue inclusio** (§6 + §7): the "did evil in the eyes of YHWH" formula (7×) and the "no king in Israel ... everyone did right in his own eyes" inclusio (4×) — uniform within JDG; STABLE.
  - **Spirit-clothing idiom (`lābash`) at JDG 6:34** — locks the Hebrew "clothed-with-the-Spirit" metaphor; recurs at 1 Chr 12:18, 2 Chr 24:20, and is the OT background for NT πληρόω-πνεύματος formula (Eph 5:18; cf. Luke 24:49).
- **3 items flagged REVIEW** (worth Ben's confirmation): the JDG 17:6 ↔ 21:25 inclusio surface-mismatch (§7); the JDG 19–21 annotation-architecture shift (§16); the JDG 19:30 "until this day" minor leitwort drift (§14).
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-judges-v1`):
  - **Adonai-in-prayer 5-form drift across JOS + JDG** (§8) — compounds NUM 14:17 + DEU 3:24+9:26 + JOS 7:7+8 → now JDG 6:15, 6:22, 13:8, 16:28 give FIVE different Thai surfaces for the same lemma-cluster. Highest-severity DECIDE; folds with the carried-forward JOS-audit §G.
  - **Heb 11:32 ↔ JDG name-spelling drift** (§9) — Gideon (Heb "กิเดโอน" vs JDG "กิดเอน") + Jephthah (Heb "เยฟธาห์" vs JDG "เยฟทาห์"). Cross-corpus NT/OT name-mismatch; first significant Heb 11 ↔ OT name drift surfaced. **DECIDE**.
- **External AI review (§3) pending.** Suggested 5-item packet (§5 Spirit-of-YHWH; §8 Adonai-prayer compound; §9 Heb 11:32 name drift; §11 Jephthah's vow; §13 Samson + NT-typology).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + divine-name compliance — **LOCKED**

YHWH occurs ~175× across the 21 chapters of Judges, uniformly rendered **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` ✓. Total surface occurrences of **องค์พระผู้เป็นเจ้า** across JDG = 715 (includes Elohim-compound, possessive, and prepositional forms). **8 "ยาห์เวห์" residues** were audited; all 8 are principled, not divine-name drift:

| Verse | Context | Disposition |
|---|---|---|
| JDG 6:24 (×5 across thai / thai_literal / key_decisions / notes / etc.) | Altar name **ยาห์เวห์ชาโลม** ("YHWH-Shalom") with parenthetical gloss "(องค์พระผู้เป็นเจ้าทรงเป็นสันติสุข)" | Compound altar-name; transliteration policy ✓ (see `divine_names_table_2026-05.md` exception for memorial proper-name compounds; same convention as El-Bethel / YHWH-Yireh in Genesis) |
| JDG 19:18 (key_decisions.note) | LXX-vs-MT textual discussion in commentary prose: "MT มี 'พระนิเวศของยาห์เวห์' แต่ LXX มี 'οἶκόν μου'" | Editorial prose-commentary, not Thai verse-text. Compliant. |

**LOCKED** ✓. Corpus-total YHWH count after JDG: ~1,870+ occurrences across 339 chapters, uniformly rendered.

---

## 2. Elohim + Adonai compound divine names — **LOCKED-with-§8-DECIDE**

- **Elohim → พระเจ้า** uniform across JDG ✓ (~50 occurrences).
- **mal'akh-Elohim** (instead of mal'akh-YHWH) at JDG 6:20, 13:6, 13:9 → **ทูตสวรรค์ของพระเจ้า** — preserves the Hebrew lemma-distinction (see §3).
- **Adonai standalone + compound — 4 distinct forms in JDG alone**: see §8 DECIDE. This is the highest-priority editorial item in the audit.

**LOCKED with §8 DECIDE flag.**

---

## 3. mal'akh-YHWH compliance — **LOCKED**

17 mal'akh occurrences verified across 4 narrative blocks; all uniformly compliant with `malak_yhwh_2026-05.md`:

| Block | Verses | Thai surface |
|---|---|---|
| Bokim address (covenant indictment) | 2:1, 2:4 | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** ✓ |
| Deborah's Song — curse on Meroz | 5:23 | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** ✓ |
| Gideon's call narrative | 6:11, 6:12, 6:20 (mal'akh-Elohim), 6:21, 6:22 | **ทูตสวรรค์ของ + [divine name]** ✓ |
| Manoah / Samson birth | 13:3, 13:6 (mal'akh-Elohim), 13:9 (mal'akh-Elohim), 13:13, 13:15, 13:16, 13:17, 13:18, 13:20, 13:21 | **ทูตสวรรค์ของ + [divine name]** ✓ |

The mal'akh-YHWH / mal'akh-Elohim lemma-distinction is preserved (6:20, 13:6, 13:9 use the Elohim form → "ทูตสวรรค์ของพระเจ้า"). The Manoah 13:22 "we shall die because we have seen God" is rendered: **"พวกเราจะต้องตาย เพราะพวกเราได้เห็นพระเจ้า"** — preserves Manoah's recognition that the figure was theophanic-grade.

**LOCKED** ✓ per `malak_yhwh_2026-05.md`. JDG is the densest-yet downstream test (4 narrative blocks; 17 occurrences) and confirms the lock holds.

**Note on §3 of JOS-audit's recommended new doc.** The JOS-audit §3 (Captain-of-host) recommended a new `captain_of_yhwh_host_2026-05.md` companion to `malak_yhwh_2026-05.md`. The Judges mal'akh occurrences re-test the Captain/mal'akh boundary (esp. Judges 6 + 13 = both classic Christophany-candidate passages). The JDG occurrences are CORRECTLY routed to mal'akh-YHWH (not captain-of-host) — the Hebrew lemma at JDG 6 + 13 is מַלְאַךְ, not שַׂר־צְבָא. The JOS captain-of-host doc, if/when written, should cross-reference JDG 6 + 13 as the mal'akh-side test cases and document the lemma boundary.

---

## 4. Seven-Nations ethnonyms — **LOCKED (JDG matches JOS 3:10 / DEU 7:1 bare-suffix)**

JDG cleanly inherits the JOS 3:10 / DEU 7:1 bare-suffix surface family for the Canaanite, Hittite, Amorite, Perizzite, Hivite, Jebusite cluster. **The JOS 9:1+/24:11 -ต / -ไซต์ drift was NOT propagated.**

| Lemma | JDG Thai surface | Occurrences |
|---|---|---|
| כְּנַעֲנִי (Canaanite) | **ชาวคานาอัน** | 1:1, 1:3, 1:4, 1:5, 1:9, 1:10, 1:17, 1:27, 1:28, 1:29, 1:30, 1:32, 1:33; 3:1, 3:3, 3:5; 4:2, 4:23, 4:24; 5:19; 21:12 (21 occurrences) |
| חִתִּי (Hittite) | **ชาวฮิตไทต์** | 1:26; 3:5 |
| אֱמֹרִי (Amorite) | **ชาวอาโมไรต์** | 1:34, 1:35, 1:36; 3:5; 6:10; 10:8, 10:11; 11:19, 11:21, 11:22, 11:23 |
| פְּרִזִּי (Perizzite) | **ชาวเปริซซี** | 1:4, 1:5; 3:5 |
| חִוִּי (Hivite) | **ชาวฮีไว** | 3:3, 3:5 |
| יְבוּסִי (Jebusite) | **ชาวเยบุส** | 1:21; 3:5; 19:10, 19:11 |
| צִידֹנִי (Sidonian) | **ชาวซีโดน** | 3:3 |

JDG 3:5 anchor verse: "และลูกหลานของอิสราเอลก็อาศัยอยู่ท่ามกลาง**ชาวคานาอัน ชาวฮิตไทต์ ชาวอาโมไรต์ ชาวเปริซซี ชาวฮีไว และชาวเยบุส**" — perfectly matches DEU 7:1's bare-suffix family.

**Editorial significance.** This is the FIRST downstream test of the JOS-audit §4 DECIDE (the JOS 3:10 family was the recommended canonical surface; the 9:1+/24:11 drift the recommended fix). JDG implicitly resolves the DECIDE in favor of path (a) — bare-suffix family. **Recommend the JOS-audit §4 DECIDE be normalized to JDG's surface family** (already the JOS 3:10 / DEU 7:1 form); JDG ships the canonical form natively. **LOCKED** ✓.

---

## 5. Spirit-of-YHWH formula — **STABLE (4-way principled split by Hebrew verb; recommend new corpus doc)**

The "Spirit of YHWH came upon X" judge-empowerment formula is the most theologically charged JDG signature — empowers each major judge for deliverance. JDG renders the formula with **four distinct Thai surfaces principled by the Hebrew verb chosen**:

| Verse | Judge | Hebrew verb | Thai surface |
|---|---|---|---|
| **3:10** | Othniel | וַתְּהִי עָלָיו | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขา** |
| **6:34** | Gideon | **לָבְשָׁה אֶת־** ("clothed") | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็ทรงสวมทับกิดเอน** |
| **11:29** | Jephthah | וַתְּהִי עַל־ | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเยฟทาห์** |
| **13:25** | Samson (prenatal) | **וַתָּחֶל ... לְפַעֲמוֹ** ("began to stir") | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็เริ่มกระตุ้นเขา** |
| **14:6** | Samson (lion) | **וַתִּצְלַח עָלָיו** ("rushed upon mightily") | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง** |
| **14:19** | Samson (Ashkelon) | וַתִּצְלַח עָלָיו | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง** |
| **15:14** | Samson (Lehi) | וַתִּצְלַח עָלָיו | **พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง** |

**Editorial assessment.** Principled four-way split by Hebrew verb:
- **תְּהִי עָלָיו** (basic "came upon") → "มาเหนือ" — Othniel + Jephthah
- **לָבְשָׁה** (literally "clothed itself with") → "ทรงสวมทับ" — Gideon's call; preserves the lābash idiom (Spirit-clothing the human)
- **תָּחֶל לְפַעֲמוֹ** (impersonal "began to stir/trouble") → "เริ่มกระตุ้น" — Samson's prenatal Nazirite stirring
- **תִּצְלַח עָלָיו** (cognate "rushed upon mightily / overpowered") → "มาเหนือเขาอย่างทรงพลัง" — uniform across 3 Samson empowerments

The lābash-Spirit metaphor at Gideon (6:34) is theologically distinctive — it is the OT background for NT πληρόω-πνεύματος formulations (Eph 5:18, Acts 2 fullness). The translator's "**ทรงสวมทับ**" preserves the Hebrew metaphor literally (Spirit clothes/envelops Gideon) without flattening to generic "came-upon."

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/spirit_of_yhwh_judges_empowerment_2026-05.md`. The doc should:
1. Lock the 4-way verb-principled Thai surface split documented above
2. Cite JDG 6:34 (lābash) as the locking precedent for the Spirit-clothing idiom — distinct from the standard "came upon"
3. Forward-protect 1 Sam 10:6, 10:10, 11:6 (Saul); 16:13–14 (David); 18:10, 19:9 (evil-spirit form); 19:20, 19:23 (Spirit-prophesying); 1 Chr 12:18 (Amasai — lābash-Spirit); 2 Chr 15:1 (Azariah), 2 Chr 20:14 (Jahaziel), 2 Chr 24:20 (Zechariah — lābash-Spirit)
4. Cross-reference NT pneumatology: Luke 1:35 ("Holy Spirit will come upon you"), Luke 4:18 (Spirit-anointing), Acts 1:8 (δύναμις cf. תִּצְלַח), Eph 5:18 (πληρόομαι), and the prophetic-Spirit thread

This is the third locking precedent (after JOS Captain-of-host and Jordan/Red-Sea typology) where the OT-side ships ahead of the corpus-doc. **Priority: HIGH** — gates 1–2 Samuel.

---

## 6. Judges cycle refrain "did evil in the eyes of YHWH" — **LOCKED-by-implication (uniform; recommend lift to doc)**

The signature Deuteronomistic-History formula opening each cycle: וַיַּעֲשׂוּ בְנֵי־יִשְׂרָאֵל הָרַע בְּעֵינֵי יְהוָה. **All 7 occurrences uniformly rendered** as:

> **"ลูกหลานของอิสราเอลก็ทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า"**

Locked at JDG 2:11, 3:7, 3:12, 4:1, 6:1, 10:6, 13:1. The phrase-consistency checker did not need to be primed for this formula; the 7-occurrence repetition is internally uniform.

**Editorial assessment.** The "**ในสายพระเนตร**" rendering (royal-anthropomorphic "eyes" of YHWH) is uniformly applied, distinct from the human-eye "ในตา" used in the inclusio refrain at JDG 17:6 + 21:25 (see §7). The split is principled: when YHWH is the subject of the seeing, royal "**สายพระเนตร**" applies (per `divine_anthropomorphism_thai_grammar_2026-05.md`); when humans are the implicit subject (the "everyone did right in his own eyes" idiom), plain "**ตา**" applies.

**STABLE — uniform within JDG; recommend lifting to corpus doc** `docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md` (or extending an existing DTr-history doc). The "did evil" formula recurs ~20× more across 1–2 Kgs (each Israelite king's evaluation; the "did evil ... like Jeroboam" subtype) and 4× in 2 Chr. The Judges form is the locking precedent.

---

## 7. "No king in Israel" inclusio (17:6 ↔ 21:25) — **STABLE-with-REVIEW (surface-mismatch on the second clause)**

The Judges epilogue inclusio (אֵין מֶלֶךְ בְּיִשְׂרָאֵל ... אִישׁ הַיָּשָׁר בְּעֵינָיו יַעֲשֶׂה) frames chs 17–21 and is the book's theological diagnosis. Occurrences:

| Verse | Thai surface |
|---|---|
| **17:6** | **"ในสมัยนั้นไม่มีกษัตริย์ในอิสราเอล ทุกคนทำในสิ่งที่ดูดีในสายตาของตัวเอง"** |
| **18:1** | **"ในสมัยนั้นไม่มีกษัตริย์ในอิสราเอล"** (truncated form — first clause only) |
| **19:1** | **"ในวันเหล่านั้นเมื่อยังไม่มีกษัตริย์ในอิสราเอล"** (truncated; "วันเหล่านั้น" instead of "สมัยนั้น") |
| **21:25** | **"ในวันเหล่านั้นไม่มีกษัตริย์ในอิสราเอล แต่ละคนทำสิ่งที่ถูกต้องในตาของตนเอง"** |

**Drift observations:**
- **Two surfaces for the temporal opener**: "ในสมัยนั้น" (17:6, 18:1) vs "ในวันเหล่านั้น" (19:1, 21:25). Hebrew בַּיָּמִים הָהֵם is identical at all four.
- **Two surfaces for the second clause** (17:6 vs 21:25 — the book-closing inclusio): "ทุกคนทำในสิ่งที่ดูดีในสายตาของตัวเอง" (17:6) vs "แต่ละคนทำสิ่งที่ถูกต้องในตาของตนเอง" (21:25). Hebrew אִישׁ הַיָּשָׁר בְּעֵינָיו יַעֲשֶׂה is identical at both.

**Editorial assessment.** The 17:6 ↔ 21:25 surface-mismatch on what is structurally the SAME inclusio frame is a small but visible drift. The Hebrew is verbatim-identical; the Thai uses two different relative-clause rendering choices (ดูดี vs ถูกต้อง for יָשָׁר; สายตา vs ตา for עֵינָיו; ทุกคน vs แต่ละคน for אִישׁ). Both renderings are defensible Thai for יָשָׁר בְּעֵינָיו (literally "right in his eyes"), but the **inclusio function** of 17:6 ↔ 21:25 is lost in the surface.

**REVIEW flag.** Recommend normalize 17:6 ↔ 21:25 to a single Thai surface for the second clause (Ben to pick: either "ทุกคนทำในสิ่งที่ดูดีในสายตาของตัวเอง" or "แต่ละคนทำสิ่งที่ถูกต้องในตาของตนเอง"). The 18:1 + 19:1 truncated occurrences can remain as-is. **Severity: LOW–MEDIUM** — inclusio framing.

---

## 8. Adonai-in-prayer — **DECIDE before tagging (5-form drift across JOS + JDG; HIGH severity)**

Standalone + compound Adonai-in-prayer surfaces have now drifted across **5 distinct Thai forms** between JOS and JDG, compounding the outstanding REVIEW from NUM 14:17 + DEU 3:24+9:26 + JOS 7:7+8 + JOS-audit §G:

| Verse | Hebrew | Thai | Class |
|---|---|---|---|
| **JOS 7:7** | אֲהָהּ ׀ אֲדֹנָי יְהוִה | **ข้าแต่องค์พระผู้เป็นเจ้า** | compound Adonai-YHWH (prayer) |
| **JOS 7:8** | בִּי אֲדֹנָי | **ข้าแต่องค์เจ้านาย** | standalone Adonai (prayer) |
| **JDG 6:15** | בִּי אֲדֹנָי | **ข้าแต่ท่านนายของข้าพเจ้า** | standalone Adonai (Gideon to mal'akh — pre-recognition) |
| **JDG 6:22** | אֲהָהּ אֲדֹנָי יְהוִה | **ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า** | compound Adonai-YHWH (Gideon post-recognition) |
| **JDG 13:8** | בִּי אֲדוֹנָי | **ข้าแต่องค์พระเจ้า** | standalone Adonai (Manoah's prayer) |
| **JDG 16:28** | אֲדֹנָי יֱהֹוִה | **ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า** | compound Adonai-YHWH (Samson's final prayer) |

**Five distinct surfaces:**
1. **ข้าแต่องค์พระผู้เป็นเจ้า** (JOS 7:7) — compound, NO trailing พระเจ้า
2. **ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า** (JDG 6:22 + JDG 16:28) — compound WITH trailing พระเจ้า (resolves the doubled Adonai-YHWH "Lord GOD" pattern explicitly)
3. **ข้าแต่องค์เจ้านาย** (JOS 7:8) — standalone Adonai (no Tetragrammaton)
4. **ข้าแต่ท่านนายของข้าพเจ้า** (JDG 6:15) — standalone Adonai BUT addressed to a then-unrecognized human/angel figure (pre-Christophany-recognition; matches the JOS 5:14 single-yodh אֲדֹנִי "my lord" pattern, NOT the prayer-Adonai pattern)
5. **ข้าแต่องค์พระเจ้า** (JDG 13:8) — standalone Adonai (Manoah's prayer; uniquely uses "พระเจ้า" alone)

The JDG 6:15 form ("ข้าแต่ท่านนายของข้าพเจ้า") is arguably defensible because Gideon addresses the figure as an unrecognized human/angel at that point in the narrative (the recognition lands at 6:22, after which the prayer-Adonai compound form kicks in). This is a **narrative-recognition arc principle** analogous to the JOS 5:14 Joshua-to-Captain-of-host single-yodh adoni address — i.e., before recognition, "my lord" register; after recognition, full prayer-Adonai register.

But **JDG 13:8 (Manoah) and JDG 16:28 (Samson) introduce two NEW surfaces** (ข้าแต่องค์พระเจ้า; ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า) not anticipated by the JOS-audit §G recommendation.

**Editorial assessment.** Five Thai surfaces for what is structurally **one cluster of lemma-compounds** (Adonai standalone + Adonai-YHWH compound + adoni single-yodh) is editorial fragmentation. The drift will compound massively into:
- 1 Sam 1:11+15 (Hannah's prayer — אֲדֹנָי)
- 1 Sam 3:9 (Samuel's "Speak, for your servant hears" — אֲדֹנָי)
- 2 Sam 7:18–29 (David's covenant prayer — אֲדֹנָי יְהוִה 7× in one prayer)
- 1 Kgs 8:23–53 (Solomon's temple-dedication prayer — אֲדֹנָי)
- Ezra 9:5–15 (Ezra's confession — אֲדֹנָי)
- Neh 1:5–11 (Nehemiah's prayer — אֲדֹנָי)
- Dan 9:4–19 (Daniel's confession — אֲדֹנָי 7× in one prayer)
- Habakkuk 3:19, Zeph 3:9, Amos passim
- NT cross-corpus: Romans 9:29 / Jas 5:4 (κύριος Σαβαώθ ← אֲדֹנָי צְבָאוֹת); Rev 6:10 / Rev 22:20 (δέσποτα / κύριε — Adonai-equivalent in apocalyptic prayer)

**DECIDE before tagging — recommended path:**

**(a) Lock a 4-way principled distinction** in `divine_names_table_2026-05.md`:

| Hebrew form | Class | Thai surface |
|---|---|---|
| אֲדֹנָי יְהוִה (compound; prayer) | compound Adonai-YHWH in prayer | **ข้าแต่องค์พระผู้เป็นเจ้า** (drop trailing พระเจ้า; conform JDG 6:22 + 16:28 to JOS 7:7 form) |
| אֲדֹנָי (standalone; prayer) | Adonai-alone in prayer | **ข้าแต่องค์เจ้านาย** (JOS 7:8 form; conform JDG 13:8 to it) |
| אֲדֹנָי (standalone; non-prayer title — e.g. "Adonai of Adonais") | Adonai-title | **องค์เจ้านาย / องค์เจ้านายของบรรดาเจ้านาย** (DEU 10:17 form) |
| אֲדֹנִי (single-yodh, "my lord" — human/angel address; or pre-recognition divine address) | adoni-vocative | **เจ้านายของข้าพเจ้า / ท่านนายของข้าพเจ้า** (JOS 5:14 + JDG 6:15 form) |

**Verses to normalize (path-a):** JDG 6:22 + JDG 16:28 → drop trailing "พระเจ้า" to conform to JOS 7:7. JDG 13:8 → change "ข้าแต่องค์พระเจ้า" → "ข้าแต่องค์เจ้านาย" to conform to JOS 7:8.

**Cost:** 3 surgical verse-edits in JDG + glossary entry + amend `divine_names_table_2026-05.md`. **Severity: HIGH** — forward-protects 8+ major OT prayer-passages and 4+ NT cross-corpus echoes.

**Note on JDG 6:22 + 16:28 trailing "พระเจ้า"**: the doubled form Adonai-YHWH (אֲדֹנָי יְהוִה or אֲדֹנָי יֱהֹוִה with the Adonai vowel-pointing) is conventionally read as "Adonai Elohim" in Jewish liturgical tradition (to avoid pronouncing the Tetragrammaton twice). The trailing "พระเจ้า" in JDG 6:22 + 16:28 captures the doubled reading; the JOS 7:7 form does not. This is a translatorial choice point — either keep the doubled-pronunciation reflection (JDG path) or use the unified-divine-name reflection (JOS path). Recommend the JOS path for corpus uniformity, but Ben should explicitly choose.

---

## 9. Heb 11:32 ↔ JDG name-spelling drift — **DECIDE before tagging (HIGH severity)**

Heb 11:32 explicitly names four JDG figures in the NT "faith-hall." Cross-checking `output/translations/hebrews_11.json` v.32:

> Heb 11:32 (Greek): Καὶ τί ἔτι λέγω; ἐπιλείψει με γὰρ διηγούμενον ὁ χρόνος περὶ **Γεδεών, Βαράκ, Σαμψών, Ἰεφθάε**, Δαυίδ τε καὶ Σαμουὴλ καὶ τῶν προφητῶν,
>
> Heb 11:32 (Thai, shipped): "และข้าพเจ้าจะกล่าวอะไรอีก? เพราะเวลาจะไม่พอที่ข้าพเจ้าจะเล่าเรื่องของ**กิเดโอน บาราค แซมสัน เยฟธาห์** ดาวิด ซามูเอล และบรรดาผู้เผยพระวจนะ"

| Figure | Heb 11:32 Thai | JDG Thai | Match? |
|---|---|---|---|
| Gideon (גִּדְעוֹן / Γεδεών) | **กิเดโอน** | **กิดเอน** (uniform across 6:11–8:35; ~50 occurrences) | ✗ DRIFT |
| Barak (בָּרָק / Βαράκ) | **บาราค** | **บาราค** (4:6 + 5:1 et al) | ✓ |
| Samson (שִׁמְשׁוֹן / Σαμψών) | **แซมสัน** | **แซมสัน** (13:24 + 14–16 passim) | ✓ |
| Jephthah (יִפְתָּח / Ἰεφθάε) | **เยฟธาห์** | **เยฟทาห์** (10:6 + 11–12 passim) | ✗ DRIFT (ธ vs ท) |

**Editorial assessment.** Two of four cross-corpus name-checks DRIFT between Heb 11:32 and JDG:
- **Gideon** — major drift: "กิเดโอน" (Heb, 3-syllable kee-DEH-on transliteration) vs "กิดเอน" (JDG, 2-syllable kid-ON transliteration). The Greek Γεδεών suggests a 3-syllable rendering, but the Hebrew גִּדְעוֹן is closer to 2-syllable (Gid-on). The JDG-side is more Hebrew-faithful; the Heb-side appears to have been transliterated from Greek without OT-corpus normalization.
- **Jephthah** — ธ vs ท drift. Greek Ἰεφθάε ends in -θε (with θ = "th"); Thai conventionally renders θ as ธ in scholarly transliteration. The Hebrew יִפְתָּח ends in -ח (with ח = guttural "ḥ"); Thai conventionally renders ח as ท. The cross-corpus mismatch reflects underlying Greek-vs-Hebrew transliteration policy.

**Forward-compounding.** The same cluster recurs in:
- 1 Sam 12:11 (Samuel's recap names Jerubbaal/Gideon + Barak + Jephthah + Samson)
- 2 Sam 11:21 (Joab's recap of Abimelech's death at Thebez — Gideon's son)
- Ps 83:9–11 (Sisera + Jabin + Oreb + Zeeb + Zebah + Zalmunna recap)
- NT: Heb 11:32 (already shipped — the drift point); James 5 patient-prophets allusion

**DECIDE before tagging — two paths:**

**(a) Normalize Heb 11:32 to the JDG-side spelling** (recommended). Edit `output/translations/hebrews_11.json` v.32: "กิเดโอน" → "กิดเอน"; "เยฟธาห์" → "เยฟทาห์". Forward-uniform with the OT name-corpus. Cost: 1 surgical verse-edit on the Hebrews side (already shipped; revision = "rev" commit + tag bump if Hebrews tag exists).

**(b) Normalize JDG to the Heb 11:32 spelling.** Edit ~50 JDG occurrences of "กิดเอน" → "กิเดโอน"; ~20 occurrences of "เยฟทาห์" → "เยฟธาห์". Far higher cost; reverses the more-Hebrew-faithful surface.

**(c) Document the Greek-vs-Hebrew transliteration-policy split** and accept both surfaces. Add a corpus doc explaining: OT figures rendered via Hebrew transliteration; NT cross-references via Greek transliteration. Defensible academically but creates Thai-reader friction.

**Recommend (a).** **Severity: HIGH** — direct NT/OT cross-corpus mismatch; 1 Sam 12:11 + Ps 83 will re-encounter the cluster. The proper-names doc (`proper_names_and_transliteration_2026-05.md`) should be amended to lock the Hebrew-faithful spelling and flag the Heb-side correction.

---

## 10. Jerub-baal (Gideon) name explanation — **STABLE**

JDG 6:32 introduces the Yerub-baal name with explicit Hebrew etymology preserved in the Thai surface:

> JDG 6:32 → "เรียกกิดเอนว่า **เยรุบบาอัล** นั่นคือ '**ขอให้บาอัลสู้คดีกับเขา**'"

11 subsequent occurrences (7:1, 8:29, 8:35, 9:1, 9:5, 9:16, 9:19, 9:24, 9:28, 9:57) uniformly render the alternate name as **เยรุบบาอัล** with paired-identification at JDG 7:1 ("เยรุบบาอัล (คือกิดเอน)") and JDG 8:35.

**Note on 2 Sam 11:21** — the alternate spelling יְרֻבֶּשֶׁת ("Yerubbesheth," replacing baʿal with bōsheth "shame") will appear there; the Judges-side לוק should lock "เยรุบบาอัล" as canonical with an explanatory cross-reference at 2 Sam 11:21 when that ships.

**STABLE** ✓.

---

## 11. Jephthah's vow + the sacrifice of his daughter (11:29–40) — **STABLE-with-recommendation-to-lift-to-doc**

The famous exegetical crux at JDG 11:29–40. The Thai translation preserves **deliberate ambiguity** between the two majority interpretations (literal sacrifice vs. perpetual virginity / Tabernacle dedication). The 11:31 notes field explicitly documents both readings:

> JDG 11:31 notes: "**ALTERNATE INTERPRETATION OF VOW**: นักวิชาการบางคน (Rabbinic + medieval Christian) เสนอว่า 'or' translation: 'จะเป็นของ YHWH OR ถวายเป็นเครื่องเผาบูชา'. ในการตีความนี้ Jephthah's daughter dedicated to lifelong celibacy ที่ Tabernacle — ไม่ใช่ killed. หลักฐาน: v.39 'she had never had relations with a man'. แต่ majority Hebrew interpretation: literal sacrifice. **MOSAIC PROHIBITION**: ลนต 18:21 ห้าม sacrifice เด็ก. แต่ Jephthah อาจไม่รู้ — outcast + grew up far from central worship."

> JDG 11:39 notes: "**TWO MAJOR INTERPRETATIONS — long debate**: (1) **Literal sacrifice** (= majority Jewish + early Christian) ... (2) **Lifelong celibacy/dedication** (= medieval Christian + some Jewish). ฉบับเอเรโมสคง ambiguity ของต้นฉบับ — ไม่บังคับการตีความ."

> JDG 11:34 notes: cross-references Gen 22 (Isaac parallel) — Jephthah parallels Abraham but "**NO DIVINE INTERVENTION**: ใน ปฐก 22 พระเจ้าทรงตอบที่จะหยุด — ที่นี่ silence."

**Editorial assessment.** The translation is exemplary: preserves Hebrew syntactic ambiguity (the vow's "shall be the LORD's AND/OR I will offer it as a burnt offering"); does NOT commit to either reading in the verse-text; cross-references Gen 22 Isaac-typology, Lev 18:21 child-sacrifice prohibition, and the medieval-vs-rabbinic interpretive history.

The translation is **STABLE** but the editorial decision (preserve ambiguity; document both readings; flag the Heb 11:32 faith-list paradox) is corpus-significant. Heb 11:32 lists Jephthah among the faith heroes — an interpretive choice point that Thai theological reviewers will press on.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/jephthah_vow_2026-05.md`. The doc should:
1. Lock the ambiguity-preserving stance at JDG 11:31 + 11:39
2. Document the two interpretive options + scholarly history (Rabbi David Kimhi's literal reading vs. medieval-Christian / Pseudo-Philo's virginity reading)
3. Cross-reference Gen 22 (Isaac binding), Lev 18:21 (child-sacrifice prohibition), 2 Kgs 3:27 (Moabite child sacrifice), Mic 6:7 (rhetorical question "Shall I give my firstborn for my transgression?")
4. Cross-reference Heb 11:32 NT-faith-list and the inclusion-without-endorsement principle
5. Cite JDG 11:29–40 as the locking precedent

Not blocking the v1 tag. **STABLE — preserved ambiguity is correctly applied.**

---

## 12. Levite-and-concubine + civil war (Judges 19–21) — **STABLE (explicit, restrained; recommend Layer-2 enhancement)**

Judges 19–21 (the Gibeah outrage + civil war + Benjaminite-wives) is the OT-corpus's darkest narrative cluster. The Thai translation handles the sensitive content with the right balance — explicit in moral force without descending to graphic detail.

| Verse | Thai surface (key fragments) |
|---|---|
| **19:22** (gang demand) | "**บุตรของเบลีอัล** ได้ล้อมบ้านไว้ ... 'จงนำชายผู้ที่เข้ามาในบ้านของเจ้าออกมา **เพื่อพวกเราจะรู้จักเขา**'" |
| **19:25** (abuse) | "พวกเขา**รู้จักนางและทารุณนาง**ตลอดคืนจนถึงรุ่งเช้า" |
| **19:29** (dismemberment) | "เขาก็จับมีด ยึดนางสนมของเขา และ**ตัดนางทีละข้อกระดูกเป็นสิบสองชิ้น**" |
| **20:6** (Israel's reaction) | "เขาได้กระทำเรื่อง**น่าเกลียดน่ารังเกียจ**ในอิสราเอล" |
| **20:10** | "...**ตามการกระทำความโง่เขลา**ทั้งหมด" |
| **21:25** (book-closing inclusio) | "ในวันเหล่านั้นไม่มีกษัตริย์ในอิสราเอล แต่ละคนทำสิ่งที่ถูกต้องในตาของตนเอง" |

**Editorial assessment.** Thai surface is **explicit but not pornographic**. The "**บุตรของเบลีอัล**" preserves the Hebrew בְּנֵי בְלִיַּעַל idiom (sons of Belial / worthlessness). The "**รู้จัก**" euphemism preserves the Hebrew יָדַע biblical-sex idiom without graphic expansion. The "**ตัด ... ทีละข้อกระดูก**" preserves the dismemberment shock without sanitization.

**Note on Sodom parallel (Gen 19) and Saul's ox-division (1 Sam 11:7).** The Hebrew narrative is a deliberate Sodom-allegory inversion (Gibeah hospitality fails where Sodom's did; the homeowner offers his daughter and the Levite's concubine — verbal echoes of Gen 19:5/8). The Levite's dismemberment-message to the 12 tribes also pre-figures Saul's ox-division at 1 Sam 11:7 (the same dismemberment-summons formula). These cross-corpus typologies are **NOT marked at verse level in JDG 19** (no notes field on chs 19–20; see §16).

**Recommend: STABLE; recommend Layer-2 enhancement.** Add chapter-footers (or verse-level notes) at JDG 19:22 (cross-reference Gen 19:4–11), JDG 19:29 (cross-reference 1 Sam 11:7), JDG 20:6 (cross-reference Hos 9:9 + 10:9 which name the Gibeah outrage as the paradigm of Israelite depravity). Cost: minimal — Layer-2 footer additions, no Thai-surface revision. Not blocking the v1 tag.

---

## 13. Samson cycle (chs 13–16) — **STABLE (rich verse-level rationale; recommend NT-typology Layer-2)**

The Samson narrative is one of the OT's most theologically textured judge-cycles. The Thai surface is uniformly compliant:

- **13:3–21 Manoah birth narrative** — mal'akh-YHWH lock applied (see §3); 13:18 angel's wonderful-name response → "ทำไมท่านถามชื่อของข้าพเจ้า"; 13:20 ascension-in-flame → "เสด็จขึ้นในเปลวไฟ"; 13:22 Manoah's "we shall die for we have seen God" → "พวกเราจะต้องตาย เพราะพวกเราได้เห็นพระเจ้า" ✓
- **14:6, 14:19, 15:14 Spirit-empowerment** — see §5 (Spirit-of-YHWH 4-way split)
- **14:14, 14:18 riddle** — "จากผู้กิน ออกมาเป็นสิ่งกิน และจากผู้แข็ง ออกมาเป็นสิ่งหวาน" / "พวกท่านไม่ได้ไถนาด้วยลูกวัวของข้าพเจ้า" — Hebrew riddle-logic preserved in Thai paraphrase
- **16:20** "the LORD had departed from him" → "เขาไม่รู้ว่าองค์พระผู้เป็นเจ้าได้ทรงจากเขาไปแล้ว" ✓ (preserves the tragic departure of Spirit-empowerment)
- **16:28** Samson's final prayer — see §8 Adonai-prayer drift; "**ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า**" needs §8-coordination
- **16:30** "let me die with the Philistines" → "ขอให้ข้าตายกับชาวฟีลิสตี" ✓

**Cross-corpus NT echoes** worth marking at Layer-2:
- **Heb 11:32** lists Samson among the faith heroes (see §9 name-drift)
- **Heb 11:34** "out of weakness were made strong" — Samson is the paradigm
- **Acts 13:20** "after that he gave them judges until Samuel the prophet" — places the Judges era in Pauline kerygma

**Recommend: STABLE; recommend Layer-2 enhancement** at JDG 13:1 (cycle opener), 13:5 (Nazirite vow lock — recurs at Num 6:1–21), 16:30 (Heb 11:32 cross-reference). Not blocking the v1 tag.

---

## 14. "Until this day" leitwort — **REVIEW (single-verse drift at 19:30)**

The עַד הַיּוֹם הַזֶּה leitwort ("until this day") is the Deuteronomistic-History etiological marker. JDG occurrences:

| Verse | Thai surface |
|---|---|
| 1:21 | **จนถึงทุกวันนี้** |
| 1:26 | **จนถึงทุกวันนี้** |
| 6:24 | **จนถึงทุกวันนี้** |
| 10:4 | **จนถึงทุกวันนี้** |
| 15:19 | **จนถึงทุกวันนี้** |
| 18:12 | **จนถึงทุกวันนี้** |
| **19:30** | **จนถึงวันนี้** (DRIFT — single-particle drop) |

**REVIEW flag.** The Hebrew is identical at all 7 occurrences; JDG 19:30 drops the "ทุก-" intensifier. Per `leitwort_handling_policy_2026-05.md`, the etiological-marker leitwort should be uniform across the corpus. Normalize 19:30 → **จนถึงทุกวันนี้** for corpus uniformity. **Severity: LOW.** (Mirrors the JOS audit's leitwort-thread; aligns with the JOS 4:9, 5:9, 6:25, etc. uniform rendering.)

---

## 15. Inherited corpus locks — **all compliant except where flagged**

| Doc | JDG evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1, §2, §8. Tetragrammaton uniform (~175/175). Elohim uniform. **EXCEPTION:** Adonai-in-prayer 5-form drift across JOS + JDG (§8 — DECIDE). | **LOCKED-with-§8-DECIDE** |
| `ot_register_policy_2026-05.md` | Royal ทรง- for YHWH-volitional throughout ✓; plain register for human judges + character speech ✓; Canaanite kings (Eglon JDG 3, Jabin JDG 4, Abimelech JDG 9 the king-claimant) plain register ✓. Compliant. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | חֶסֶד occurs at JDG 1:24 (spies + Joseph house at Bethel — "if you show us חֶסֶד") and JDG 8:35 (Israel "did not show חֶסֶד to Jerubbaal's house"). Both rendered via the doc-locked surface ✓. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator-omniscient stance throughout; royal register for YHWH-volitional; plain for judges. Compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "YHWH's hand" anthropomorphism ("ทรงมอบไว้ในมือของ ...") at 2:14, 2:15, 2:16, 2:18, 6:1, 13:1, etc. uniform ✓; "YHWH's anger kindled" (חָרָה אַף יְהוָה) at 2:14, 2:20, 3:8, 10:7 → "พระพิโรธ ... ทรงพระพิโรธ" uniform ✓; the "in the eyes of YHWH" royal-anthropomorphic eye (cycle refrain, §6) → **สายพระเนตร** ✓. Compliant. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol chains pervasive (esp. the Ehud assassination 3:15–25 — the textbook Hebrew narrative-pace chapter); cognate-accusatives preserved (e.g., 11:30 וַיִּדַּר ... נֶדֶר → "ปฏิญาณ ... คำปฏิญาณ"); imperative-of-prohibition forms. Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "Hand of YHWH" + "anger kindled" anthropomorphisms ✓; "until this day" leitwort (see §14 — single drift at 19:30); "in the eyes of YHWH / in his own eyes" inclusio (see §6 + §7). Compliant. | **LOCKED-with-§14-flag** |
| `hebrew_oath_formulas_2026-05.md` | חַי־יְהוָה ("as YHWH lives") at JDG 8:19 (Gideon to Zebah + Zalmunna). Other oath forms in 11:30 (Jephthah's vow — נֶדֶר construction) ✓; 21:1, 21:7, 21:18 (the Mizpah oath about Benjaminite wives). Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | No notable MT/English chapter-boundary divergences in JDG. The MT 13:1 vs LXX 13:2 minor verse-division difference handled. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | ~150 proper-noun renderings spot-checked. Judges: โอทนีเอล, เอฮูด, ชัมการ, เดโบราห์, บาราค, เยเอล, กิดเอน, เยฟทาห์, แซมสัน, อาบีเมเลค, โทลา, ยาอีร์, อิบซาน, เอโลน, อับโดน. Places: เบธเอล, โบคิม, มิสปาห์, ชีโลห์, โอฟราห์, ภูเขาทาบอร์, แม่น้ำคีโชน, ลำธารฮาโรด, มาหะเนห์-ดาน, เลฮี, ทิมนาห์, กิเบอาห์, อาเบล-ชิทธิม. Cross-corpus character matches verified: **คาเลบ** (JOS 14:6 + 15:13 ↔ JDG 1:12 + 3:9) ✓; **โอทนีเอล** (JOS 15:17 ↔ JDG 1:13 + 3:9) ✓. **EXCEPTIONS:** Heb 11:32 ↔ JDG name drift (Gideon + Jephthah — §9 DECIDE). | **LOCKED-with-§9-DECIDE** |
| `proper_noun_wordplay_2026-05.md` | JDG 6:32 Yerub-baal etymology preserved ("ขอให้บาอัลสู้คดีกับเขา") ✓; JDG 15:17 Ramath-lehi etymology ("Hill of the Jawbone"); JDG 15:19 En-hakkore ("Spring of the One Who Calls") ✓; JDG 18:29 Laish → Dan rename ✓; JDG 2:5 Bochim ("Weepers") etymology with explicit gloss ✓; JDG 5:6 "in the days of Jael" — proper-name preserved ✓. Compliant. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | 21/21 chapters have `output/textual_variants/judges_NN.json` files ✓. JDG 19:18 LXX-vs-MT note ("MT: 'house of YHWH' vs LXX: 'house of mine'") preserved at key_decisions level. Compliant. | **LOCKED** |
| `ot_warfare_ethics_2026-05.md` | Judges has scattered ḥerem-language passages (JDG 1:17 חָרַם uses; JDG 21:11 Mizpah-oath ban-language for Jabesh-Gilead). Same JOS-binyan-principled split observed: nominal cluster vs verbal cluster. Compliant with the JOS-audit §9 REVIEW (still pending coordination with DEU §7 DECIDE). | **LOCKED (carries JOS §9 REVIEW)** |
| `i_am_yhwh_holiness_formula_2026-05.md` | JDG 6:8–10 prophet oracle ("I am YHWH your God ... do not fear the gods of the Amorites") uniform with the Pentateuchal "I am YHWH" formula ✓. | **LOCKED** |
| `paqad_visit_attend_2026-05.md` | פָּקַד occurs at JDG 15:1 (Samson "visiting" his wife — semantic-context visiting-purpose) and 20:15 (mustering); semantic-context preserved. No drift. | **LOCKED** |
| `manah_divine_appointment_2026-05.md` | **Zero מָנָה occurrences in JDG.** N/A. | **LOCKED (N/A)** |
| `malak_yhwh_2026-05.md` | See §3 — fully compliant across 4 narrative blocks; 17 occurrences. | **LOCKED** |
| `kapporet_atonement_cover_2026-05.md` | **Zero כַּפֹּרֶת occurrences in JDG.** N/A. | **LOCKED (N/A)** |
| `kareth_penalty_formula_2026-05.md` | **Zero priestly-Levitical karet occurrences in JDG.** N/A. | **LOCKED (N/A)** |
| `hagiasmos_hagiosune_2026-05.md` | קֹדֶשׁ at JDG 17:3 (Micah's silver "dedicated to YHWH") — uniform with doc-locked surface ✓. The Nazirite consecration at JDG 13:5, 13:7, 16:17 → "ผู้ที่ถูกแยกไว้เพื่อพระเจ้า" ✓ doc-canonical. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | See §15-row above. Compliant. | **LOCKED** |
| `pagan_deities_2026-04.md` | Baal cluster at 2:11, 2:13, 3:7, 6:25–32 (Gideon-Baal showdown), 8:33, 9:4, 9:46 (Baal-berith / El-berith), 10:6, 10:10 → **พระบาอัล / พระบาอัล-เบรีธ / เอล-เบรีธ** ✓; Asherah cluster at 3:7, 6:25, 6:26, 6:28, 6:30 → **เสาอาเชราห์** (cultic object) / **บรรดาเสาอาเชราห์** ✓; Ashtaroth at 2:13, 10:6 → **บรรดาพระอัชเทเรท** ✓; "other gods" at 2:12, 2:17, 2:19, 10:13, 10:14 → **พระอื่น / พระอื่นๆ** ✓. No "พระเจ้า" used for pagan deities ✓. Compliant. | **LOCKED** |
| `ot_polytheistic_register_2026-05.md` | JDG 11:24 (Jephthah to Ammonite king: "will you not possess what Chemosh your god gives you?") — preserves the historical-polytheistic context without flattening to pagan-pejorative. JDG 16:23–24 (Dagon worship after Samson's capture) → **พระดาโกน** ✓. Compliant. | **LOCKED** |
| `goel_kinsman_redeemer_2026-05.md` | **Zero גָּאַל kinsman-redeemer occurrences in JDG** (the lemma is concentrated in Ruth + Lev 25). N/A. | **LOCKED (N/A)** |
| `leitwort_handling_policy_2026-05.md` | The "in the eyes of" leitwort (cycle refrain + book inclusio) — see §6 + §7. The "until this day" leitwort — see §14 (single-verse drift at 19:30). The "did evil / sold them into the hand" double-formula at every cycle opener — uniform. Compliant. | **LOCKED-with-§7-+-§14-flags** |
| `divine_object_praise_verbs_2026-04.md` | Limited JDG exposure: JDG 5:2 "Bless YHWH" (Deborah's Song) → **ขอจงสรรเสริญองค์พระผู้เป็นเจ้า** ✓ doc-canonical; JDG 5:9 + 5:11 similar. Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | `audit_inclusion_variants.py --book judges --strict` — no candidate inclusion-variants flagged. Compliant. | **LOCKED (N/A)** |
| `aramaic_transliterations_2026-04.md` | N/A — pre-Aramaic OT narrative. | **LOCKED (N/A)** |
| `nicham_divine_relenting_2026-05.md` | JDG 2:18 "the LORD was moved to pity" (נִחַם), JDG 21:6, 21:15 ("the Israelites repented / had compassion on Benjamin") — divine + human nicham mixed. Uniform with the doc's distinction (divine-relenting royal-marked; human-compassion plain). Compliant. | **LOCKED** |
| `uncover_nakedness_euphemism_2026-05.md` | JDG 19:22–25 (Gibeah outrage) does NOT use the technical "uncover nakedness" Leviticus-19 formula — uses יָדַע "know" + עָנָה "abuse" verbs instead. N/A for the technical formula. | **LOCKED (N/A)** |
| `shared_names_normalization_2026-05.md` | Tribal names compliant (Judah, Simeon, Ephraim, Manasseh, Dan, Benjamin, Naphtali, Asher, Zebulun, Issachar, Gad, Reuben — all match prior locks). Compliant. | **LOCKED** |
| `sacrificial_vocabulary_2026-05.md` | JDG 6:18–21 (Gideon's offering for the mal'akh-YHWH — מִנְחָה) → **เครื่องบูชา** ✓; JDG 11:31 + 11:39 (Jephthah's burnt-offering vow — עוֹלָה) → **เครื่องเผาบูชา** ✓ doc-canonical; JDG 13:15–20 (Manoah's burnt-offering — עוֹלָה + מִנְחָה) ✓; JDG 20:26 + 21:4 (Bethel assembly burnt + peace offerings — עוֹלָה + שְׁלָמִים) → **เครื่องเผาบูชาและเครื่องบูชามิตรภาพ** ✓. Compliant. | **LOCKED** |

---

## 16. JDG 19–21 annotation-architecture shift — **REVIEW**

Verified via per-chapter count:

| Chapter | verses | key_decisions | thai_summary | notes-field verses |
|---|---|---|---|---|
| JDG 17 | 13 | 17 | 6 | 13 |
| JDG 18 | 31 | 26 | 9 | 31 |
| **JDG 19** | **30** | **28** | **30** | **0** |
| **JDG 20** | **48** | **40** | **48** | **0** |
| **JDG 21** | **25** | **23** | **25** | **1** |
| (compare JDG 1) | 36 | 93 | 11 | 33 |
| (compare JDG 5) | 31 | 74 | 12 | 31 |
| (compare JDG 11) | 40 | 44 | 8 | 40 |

**Observation.** Across chs 1–18, JDG uses the standard annotation pattern: **notes field present on nearly every verse** (carries the Layer-2 cross-corpus references, theological/historical context, Hebrew grammar discussion) + sparse `thai_summary` (only on key verses). At JDG 19–21, the pattern **inverts completely**: `thai_summary` on every verse, `notes` field essentially empty (0 + 0 + 1).

**Editorial assessment — two possibilities:**

(a) **Intentional editorial decision.** The maintainer may have intentionally moved sensitive-content commentary out of the notes field (which renders prominently in the reader-edition or annotation UI) into thai_summary (which is verse-prose-style and lower-profile in display). Defensible for the Gibeah-outrage + civil-war + Benjaminite-wives content — keeps reader-facing commentary briefer and less intrusive.

(b) **Drift / different drafting pass.** The architectural shift may simply reflect a different drafting approach at the end of the book (perhaps a tighter cadence as the book closed; or a different prompt-template per chapter).

**REVIEW flag.** Ben to confirm whether the chs 19–21 shift is intentional. If yes, document the principle (sensitive-content chapters → thai_summary primary; notes empty) for future books with similar content (e.g., 2 Sam 11–13 David-Bathsheba-Amnon, Ezek 16/23 allegorical-zonah). If unintentional, consider retrofitting Layer-2 cross-corpus footers at JDG 19:22 (Gen 19 Sodom), 19:29 (1 Sam 11:7 dismemberment-summons), 20:6 (Hos 9:9 + 10:9 Gibeah-as-paradigm), 21:25 (book-closing inclusio with 17:6 — see §7). **Severity: LOW–MEDIUM.**

---

## 17. NT cross-corpus quotes from Judges — **REVIEW-with-§9-DECIDE-flag**

JDG is referenced 4 times in the NT, each rendering needs cross-corpus check:

| JDG ref | NT echo | Match? |
|---|---|---|
| Judges figures (Gideon + Barak + Samson + Jephthah) | **Heb 11:32** | ✗ DRIFT on Gideon + Jephthah — see §9 DECIDE |
| Samson's strength-from-weakness pattern | **Heb 11:34** | indirect allusion — no surface to verify |
| "After that he gave them judges until Samuel the prophet" | **Acts 13:20** | Paul's kerygma summary; no specific JDG-figure name verified |
| JDG 13:5/7/14 Nazirite vow | **Luke 1:15** (John the Baptist Nazirite-like) + Acts 21:23–26 (Paul + Jerusalem Nazirites) | typological — no surface to verify |

**Editorial assessment.** The Heb 11:32 surface-drift (§9) is the load-bearing cross-corpus item. The other three NT references are allusions/typology and don't require surface-uniformity.

**Recommend: REVIEW with §9-DECIDE-folded.** Resolving §9 (Heb 11:32 name normalization to JDG-side spelling) handles the only direct-quote drift. **Severity: HIGH** (folded into §9 DECIDE).

---

## 18. Mechanical (§1) — **all green**

- 21/21 chapters: `output/check_reports/judges_NN_review.md` + `_summary.json` + sub-reports ✓
- 21/21 chapters: `output/back_translations/judges_NN.json` ✓
- 21/21 chapters: `output/translations/judges_NN.json` ✓
- 21/21 chapters: `output/textual_variants/judges_NN.json` ✓ (FULL coverage — addresses the JOS-audit §H minor flag pattern; JDG has no equivalent missing-file)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 339-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `git status output/`: **clean** ✓
- YHWH "องค์พระผู้เป็นเจ้า" occurrences across JDG: **715** (counts include compound + possessive forms)
- "ยาห์เวห์" residues: **8 total**; all principled (Yahweh-Shalom altar at JDG 6:24 ×5; LXX-vs-MT commentary at JDG 19:18 ×1). See §1.

**Severity: GREEN.** Mechanical gate passes cleanly.

---

## 19. Flagged for Ben's attention

### A. Adonai-in-prayer 5-form drift across JOS + JDG — **DECIDE before tagging** (§8)
Compounds NUM 14:17 + DEU 3:24+9:26 + JOS 7:7+8 + JOS-audit §G. Normalize JDG 6:22 + 16:28 (drop trailing "พระเจ้า" → conform to JOS 7:7 form) + JDG 13:8 ("ข้าแต่องค์พระเจ้า" → "ข้าแต่องค์เจ้านาย" per JOS 7:8 form). JDG 6:15 ("ข้าแต่ท่านนายของข้าพเจ้า") is principled (pre-recognition adoni form) and remains. **HIGH severity** — forward-protects 8+ major OT prayer-passages + 4+ NT cross-corpus echoes.

### B. Heb 11:32 ↔ JDG name-spelling drift — **DECIDE before tagging** (§9)
Normalize Heb 11:32 Thai ("กิเดโอน" → "กิดเอน"; "เยฟธาห์" → "เยฟทาห์") to match the OT corpus surface. Cost: 1 surgical edit on Hebrews side (already-shipped revision). **HIGH severity** — first cross-corpus NT/OT name-drift surfaced; forward-protects 1 Sam 12:11 + Ps 83 recap clusters.

### C. Spirit-of-YHWH 4-way principled split — **STABLE; new doc** (§5)
Write `docs/translator_decisions/spirit_of_yhwh_judges_empowerment_2026-05.md` locking the verb-principled 4-way Thai surface split (תְּהִי עָלָיו → "มาเหนือ"; לָבְשָׁה → "ทรงสวมทับ"; תָּחֶל לְפַעֲמוֹ → "เริ่มกระตุ้น"; תִּצְלַח עָלָיו → "มาเหนือเขาอย่างทรงพลัง"). Forward-protects 1 Sam 10:6 / 10:10 / 11:6 / 16:13–14 / 18:10 / 19:9 / 19:20 / 19:23 + 1 Chr 12:18 + 2 Chr 15:1 / 20:14 / 24:20. **Priority: HIGH** — gates 1–2 Samuel.

### D. Judges cycle refrain + epilogue inclusio — **STABLE; new doc** (§6)
Write `docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md` locking:
1. The "did evil in the eyes of YHWH" formula → **"ลูกหลานของอิสราเอลก็ทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า"** (JDG 7-times occurrence as locking precedent)
2. The "in the eyes of YHWH" vs "in his own eyes" royal-vs-plain anthropomorphism split (per `divine_anthropomorphism_thai_grammar`)
3. The "YHWH raised up a judge / deliverer" formula — distinguishing shofet (judge) → "ผู้วินิจฉัย" from moshiyaʿ (deliverer) → "ผู้ช่วยกู้"
Forward-protects ~20 Kings + 4 Chronicles cycle-evaluation formulas.

### E. JDG 17:6 ↔ 21:25 inclusio surface-mismatch — **REVIEW** (§7)
Normalize the book-closing inclusio second clause to a single Thai surface. Ben to pick: either "ทุกคนทำในสิ่งที่ดูดีในสายตาของตัวเอง" (17:6 form) or "แต่ละคนทำสิ่งที่ถูกต้องในตาของตนเอง" (21:25 form). Cost: 1 surgical verse-edit + glossary note. **Severity: LOW–MEDIUM.**

### F. JDG 19:30 leitwort minor drift — **REVIEW** (§14)
Normalize "จนถึงวันนี้" → "จนถึงทุกวันนี้" for corpus uniformity per `leitwort_handling_policy_2026-05.md`. Cost: 1 surgical edit. **Severity: LOW.**

### G. JDG 19–21 annotation-architecture shift — **REVIEW** (§16)
Confirm whether the notes-empty / thai_summary-full pattern at chs 19–21 is intentional editorial decision (sensitive-content content-routing) or drift. If intentional, document the principle for future books; if drift, consider retrofitting Layer-2 cross-corpus footers at the key Gibeah-outrage / civil-war verses (Gen 19 / 1 Sam 11:7 / Hos 9:9–10:9 cross-references).

### H. Jephthah's vow corpus doc — **STABLE; new doc** (§11)
Write `docs/translator_decisions/jephthah_vow_2026-05.md` locking the ambiguity-preserving stance (literal-sacrifice vs perpetual-virginity readings preserved at notes-level; Thai verse-text does not commit). Cross-references Gen 22, Lev 18:21, Mic 6:7, Heb 11:32. Not blocking the v1 tag.

### I. Levite-and-concubine + civil war Layer-2 enhancement — **STABLE; optional** (§12)
Add Layer-2 cross-references at JDG 19:22 (Gen 19 Sodom inversion), 19:29 (1 Sam 11:7 dismemberment-summons), 20:6 (Hos 9:9 + 10:9 Gibeah-as-paradigm). Not blocking; optional polish.

### J. Samson cycle Layer-2 enhancement — **STABLE; optional** (§13)
Add Layer-2 footers at JDG 13:5 (Nazirite vow cross-reference to Num 6), 16:30 (Heb 11:32 NT-typology). Not blocking; optional polish.

### K. JOS-audit-§3 Captain-of-host doc — **carried forward**
JOS-audit recommended `captain_of_yhwh_host_2026-05.md`; this audit confirms JDG mal'akh-YHWH passages CORRECTLY routed to mal'akh (not captain). When the JOS doc is written, it should cross-reference JDG 6 + 13 as the mal'akh-side test cases and document the lemma boundary.

### L. New corpus docs to write — **summary**
1. **`spirit_of_yhwh_judges_empowerment_2026-05.md`** (§5 / §C) — 4-way verb-principled split; gates 1–2 Samuel ← HIGH PRIORITY
2. **`dtr_history_cycle_formulas_2026-05.md`** (§6 / §D) — cycle refrain + deliverer/judge formula; gates 1–2 Kings + 1–2 Chr
3. **(Optional)** `jephthah_vow_2026-05.md` (§11 / §H) — ambiguity-preserving stance; cross-references Heb 11:32

### M. Existing docs to amend
- **`divine_names_table_2026-05.md`** — 4-way Adonai distinction per §8 DECIDE (compounds NUM-audit §8 + DEU-audit §14 + JOS-audit §G + JDG §8) ← HIGH PRIORITY
- **`proper_names_and_transliteration_2026-05.md`** — lock JDG-Hebrew-faithful spellings for Gideon (กิดเอน) + Jephthah (เยฟทาห์); flag Heb 11:32-side correction per §9 DECIDE
- **`leitwort_handling_policy_2026-05.md`** — minor amendment: cite JDG 19:30 normalization as additional test case (§14)

### N. External AI review (§3 of checklist) — **pending**
Recommended 5-cluster external AI packet:
1. **Spirit-of-YHWH 4-way principled split** (§5) — Othniel / Gideon-lābash / Jephthah / Samson contrast
2. **Adonai-in-prayer 5-form drift JOS + JDG** (§8) — compounds NUM-audit §8 + DEU-audit §14 + JOS-audit §G
3. **Heb 11:32 ↔ JDG name-drift** (§9) — Gideon / Jephthah cross-corpus mismatch
4. **Jephthah's vow ambiguity-preservation** (§11) — interpretive options + Heb 11:32 faith-list paradox
5. **JDG 19–21 annotation-architecture shift** (§16) — sensitive-content content-routing principle question

Use Grok + ChatGPT in parallel per the JHN/GAL/DEU/JOS pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 9 items (§1 YHWH compliance, §3 mal'akh-YHWH, §4 ethnonyms, §10 Yerub-baal etymology, §15 inherited locks compliant subset, §18 mechanical, §2 Elohim/divine names, §17 NT cross-corpus base case, ${plus inherited locks via §15 row breakdown})
- **STABLE (recommend new doc):** 3 items (§5 Spirit-of-YHWH split, §6 cycle refrain, §11 Jephthah vow); + 2 optional Layer-2 enhancements (§12 Levite-civil-war, §13 Samson)
- **REVIEW:** 3 items (§7 17:6↔21:25 inclusio surface-mismatch, §14 19:30 leitwort drift, §16 chs 19–21 annotation shift)
- **DECIDE:** 2 items (§8 Adonai-prayer 5-form drift HIGH; §9 Heb 11:32 name drift HIGH)

**2 DECIDE items block the `book-judges-v1` tag.** (§8, §9)

**2 new translator_decisions docs recommended** (`spirit_of_yhwh_judges_empowerment_2026-05.md`, `dtr_history_cycle_formulas_2026-05.md`) + 1 optional (`jephthah_vow_2026-05.md`).

**2 existing docs to amend** (`divine_names_table_2026-05.md` Adonai 4-way distinction; `proper_names_and_transliteration_2026-05.md` Heb-OT name policy) + 1 minor (`leitwort_handling_policy_2026-05.md`).

---

## Recommendation

**Judges ships in strong corpus-hygiene shape.** It is the **second Former-Prophets book** and the FIRST DOWNSTREAM TEST of the JOS-era locks outside Joshua. The audit confirms:
- The Seven-Nations ethnonym JOS-audit §4 DECIDE is **implicitly resolved correctly** — JDG ships the JOS 3:10 / DEU 7:1 bare-suffix family natively (the JOS 9:1/24:11 drift was not propagated forward).
- The mal'akh-YHWH lock from `malak_yhwh_2026-05.md` holds across 4 narrative blocks + 17 occurrences — the densest downstream test of the doc to date.
- The OT-register policy, divine-anthropomorphism, Hebrew-grammar transfer, leitwort handling, oath formulas, pagan-deities + polytheistic-register, proper-noun wordplay, and sacrificial-vocabulary docs all carry cleanly.
- The cycle-refrain ("did evil") and the no-king-in-Israel inclusio are uniform internal markers.

However, **2 DECIDE items** must resolve before tagging `book-judges-v1`:
1. **§8 — Adonai-in-prayer 5-form drift across JOS + JDG.** Forward-protects 8+ major OT prayer-passages.
2. **§9 — Heb 11:32 ↔ JDG name-spelling drift.** First cross-corpus NT/OT name-mismatch surfaced; gates 1 Sam 12:11 + Ps 83 recap clusters.

The 2 STABLE-but-undocumented items (§5 Spirit-of-YHWH 4-way; §6 cycle refrain) should be lifted to corpus docs **before 1–2 Samuel ships** (Saul + David empowerment narratives will re-encounter the Spirit-of-YHWH cluster ~10 more times; the Kings-cycle evaluations will re-encounter the "did evil" formula ~20 more times).

Tag `book-judges-v1` after:
1. Ben's decisions on **§A + §B** (DECIDE: Adonai 5-form drift; Heb 11:32 name drift)
2. Ben's confirmation on **§E + §F + §G** (REVIEW: inclusio mismatch; leitwort 19:30; annotation-architecture shift)
3. Two new translator_decisions docs written (**§C + §D** — Spirit-of-YHWH; DTr cycle formulas)
4. Two existing docs amended (`divine_names_table_2026-05.md` Adonai 4-way; `proper_names_and_transliteration_2026-05.md` Heb-OT name policy)
5. External AI sanity-check (§N)

The Former-Prophets corpus (Ruth-already-shipped, 1–2 Sam, 1–2 Kgs) can be queued for next book — but writing `spirit_of_yhwh_judges_empowerment_2026-05.md` before 1 Sam 10 ships is the load-bearing forward-protection step.
