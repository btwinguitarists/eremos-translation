# Ezekiel — End-of-Book Review

**Date:** 2026-06-25
**Scope:** All 48 chapters of Ezekiel (1,273 verses); `glossary.json`; `docs/translator_decisions/` corpus (97 docs). Ezekiel is the OT's **densest divine-name book** — the compound אֲדֹנָי יְהוִה ("Lord GOD") occurs **217 times**, far more than any other book — and the densest concentration of three Ezekiel-signature refrains: the recognition formula *"you/they shall know that I am YHWH"* (אֲנִי יְהוָה, 84 verses), the address *"son of man"* (בֶּן־אָדָם, 93 verses), and the divine self-oath *"as I live"* (חַי־אָנִי, 16 verses). It is also the corpus's heaviest concentration of **first-person divine body-part theophany** ("I will stretch out my hand," "my eye will not pity") — the exact pressure point the Jeremiah audit (§13) named Ezekiel as carrying "the highest forward weight," and the great foreign-ruler oracle book (Tyre ch. 28, Pharaoh chs. 29–32, Nebuchadnezzar, Gog chs. 38–39), the second pressure point (Jeremiah §24). The temple vision (chs. 40–48) is the OT's densest cluster of measurement-textual cruxes, and the Davidic-shepherd material (ch. 34, 37:24–25) is cross-quoted into the NT (John 10; Rev 21–22). The project follows the MT surface throughout.
**Trigger:** EZK 48 shipped (commit `18485408`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **23 cross-cutting items reviewed.** Mechanical gates (§1) pass: 48/48 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks, 29,886 verses); `audit_inclusion_variants.py --book ezekiel --strict` = **0 candidates, exit 0**; `check_divine_names.py --book EZK` = exit 0 with **0 soft warnings** (the cleanest divine-name checker state of any major prophet — no human-address אֲדֹנִי false positives to adjudicate); `check_versification_anchor.py --book EZK` = exit 0 (but **false-clean** — see §19). **47/47** chapters that contain a divine name carry a `textual_variants` YHWH first-occurrence footnote (complete coverage; ch. 19, the princes' dirge, correctly has no divine name and no footnote). Two infrastructure items surfaced (§23): `export_to_usfm.py` still rejects `EZK` (the recurring OT book-code gotcha), and the EZK 21 MT/English versification offset is **not registered** in `versification_map.json` while a `key_decisions` note falsely claims it was (§19).
- **4 items flagged DECIDE** (Ben choice needed before tagging `book-ezekiel-v1`):
  - **§10 — divine-anthropomorphism register: the codified first-person-plain rule, now operationalized at scale.** The loudest finding, and the one the Jeremiah audit predicted would be heaviest here. `divine_anthropomorphism_thai_grammar_2026-05.md` locks God's body parts to royal register (ราชาศัพท์) with **no person-based exception**: hand יָד → **พระหัตถ์**, eye עֵינַי → **พระเนตร**, face פָּנִים → **พระพักตร์**, arm זְרוֹעַ → **พระกร**. In Ezekiel, first-person divine speech ("my hand / my eye / my face") systematically drops to **plain** register (มือ / ตา / หน้า), and — beyond Jeremiah, where the rule was merely codified once — Ezekiel **operationalizes it at scale** with a self-cross-referencing lock chain (5:11 "lock," "consistent with 5:11," "as 14:8") spanning ~22 verses, plus two named exceptions (the Exodus "mighty-hand-and-outstretched-arm" power-formula keeps royal at 20:33–34; hedged vision-body-parts like "the form of a hand" 8:3 stay plain). It produces **three same-idiom register splits** — sharpest at chapter 20, where "I withheld my **มือ**" (20:22) and "with strong **พระหัตถ์** and outstretched **พระกร**" (20:33) put the identical lemma יָד in two registers eleven verses apart. The 3rd-person narration "the hand of YHWH" stays correctly royal (พระหัตถ์: 1:3, 3:14, 8:1, 37:1, 40:1), confirming the split is deliberately person-conditioned, not noise. This is the same conflict as Isaiah §13 and Jeremiah §13 (both unresolved), now the **largest and most rigorously-codified instance in the corpus**, and the drift is **invisible to mechanical gates** (the KDs cite each other, so internal consistency is perfect). **Ben must ratify a documented first-person-plain exception (amending the anthropomorphism doc, formalizing the Exodus-formula + hedge carve-outs) OR reverse the ~22 verses to Rachasap — and reconcile with Isaiah §13 + Jeremiah §13** so three major prophets speak with one voice. See §10.
  - **§11 — foreign-monarch register: every ruler is plain, hardening the Jeremiah/Daniel conflict into a genre-level split.** Across all 48 chapters **every foreign and human ruler receives plain register** — no ราชาศัพท์ (ทรง / เสด็จ), no royal pronoun พระองค์, no royal verbs — including **narrator-voice siege-action verbs** for Nebuchadnezzar (26:8–9 ฆ่า/ตั้ง/ก่อ, all plain), the exact category `ot_register_policy §2.6` *upgraded to* ทรง for the Ezra block. `§2.2` grants foreign emperors full ราชาศัพท์ even if villainous; **Daniel gives all four emperors full ทรง**. Ezekiel therefore agrees with **Jeremiah** (§24, Nebuchadnezzar plain) **against** the Writings block (Daniel + the §2.6 Ezra lock) — and as the **third data point** it tips the corpus pattern into a genre split: *Latter-Prophets judgment oracles flatten the rulers; Writings court-narratives dignify them.* The choice is internally consistent (the translator consciously reasons to plain at 12:12 via the shame-downshift and at 38:3/39:1 via the §3 adversary rule) and rhetorically defensible (granting ทรง to the self-deifying king of Tyre, 28:2, or the "great monster" Pharaoh, 29:3, would undercut the oracles), but it is **not what §2.2/§2.6 as written require**, and the unifying `foreign_monarch_register` doc **owed since Ezra still does not exist**. **Ben must write that doc**, deciding whether to carve out a Latter-Prophets judgment-oracle exception (which retroactively blesses Jeremiah + Ezekiel and confines §2.6 to narrative books) or to declare both prophets non-conformant — and **resolve jointly with the still-untagged EZR/NEH/EST/DAN block + Jeremiah** so Nebuchadnezzar above all speaks with one voice. See §11.
  - **§14 — messianic/Davidic committal surface: the §0 line is crossed in the note layer.** The translation **surface is clean everywhere** (the verse text never asserts fulfillment), but Ezekiel's messianic `thai_summary` lines are **materially more doctrinally-forward than Isaiah's or Jeremiah's and regress past the §0 bar the Jeremiah audit drew**. Jeremiah's most-forward line (31:31, *"cited in Heb 8/10 as fulfilled in Christ"*) passed because it **reports what Hebrews does** (a citation-fact). Ezekiel instead **asserts the identification as bare fact in the translator's own voice**: 34:23 *"…หมายถึงเชื้อสายของดาวิด **คือพระคริสต์**"* ("means the seed of David, who **is the Christ**"); 17:22 *"กษัตริย์ในวงศ์ดาวิดที่แท้จริง**คือพระคริสต์**"* ("the true Davidic king **is the Christ**"); 21:32 *"จะได้รับการสถาปนาใหม่**ในพระคริสต์**"* ("will be re-established **in Christ**"). At least five summaries (34:23, 34:1, 21:32, 17:22, 17:23) plus the 37:24/37:25 + 34:23 KDs cross the line. A correct **report-form** template already exists *in the same book* (47:1 *"ภาพนี้สำเร็จในวิวรณ์ 22:1"*; 17:23b *"พระเยซูทรงนำภาพนี้ไปใช้ใน…มัทธิว 13:32"* — reporting what the NT does). **Ben must decide whether to down-tone the five+ assertive clauses to report-form or affirm them** — this is the natural external-AI item and tests messianic-policy continuity with Isaiah §6 / Jeremiah §6. See §14.
  - **§18 — MT/LXX temple-vision disclosure is incomplete and structurally fragile.** Surface correct (MT throughout). But Ezekiel is the OT's densest measurement-crux book and only **3 of 9 temple chapters** (40, 42, 45) surface an MT/LXX measurement note to the reader, and all three are **bundled inside the chapter's YHWH first-occurrence footnote** — a reader who doesn't open the divine-name footnote never sees them. Chapters 41, 43, 44, 46, 47, 48 disclose nothing; many cruxes (40:14, 42:16 reeds-vs-cubits, 45:12 mina) live only in `key_decisions` (never rendered). There is **no book-level or temple-section disclosure note**. The Jeremiah audit made MT/LXX macro-disclosure a DECIDE (§9) and the `mt_vs_lxx §2.3` floor applies here too. (Good precedent inside the book: ch. 7's footnote *does* disclose the famous MT/LXX verse-order difference at 7:3–9 — reader-facing.) **Ben must ratify a temple-vision disclosure standard** (minimally a §2.3 section-header note for 40–48: "Eremos = MT; English/BSB figures differ"; ideally a non-divine-name footer type so measurement cruxes don't depend on the YHWH footnote) **or affirm the current bundled-footnote state.** See §18.
- **6 items flagged REVIEW** (worth Ben's confirmation):
  - **§9 — "son of man" (בֶּן־אָדָם) doc reconciliation.** All 93/93 render the locked **บุตรแห่งมนุษย์เอ๋ย** (with connector แห่ง + vocative เอ๋ย), perfectly uniform and correctly distinct from the Christological title **บุตรมนุษย์** (no connector; Dan 7:13, NT) — a doctrinally load-bearing three-way system (title บุตรมนุษย์ / generic บุตรของมนุษย์ / mortal-address บุตรแห่งมนุษย์), harmonized with shipped Dan 8:17 + Ps 8:4. **But** `son_of_man_disambiguation_2026-04.md` is NT-scoped and its "alternatives considered" *explicitly rejected* แห่ง for the title — so the shipped OT mortal-address form superficially contradicts the doc. **Recommend amending the doc** to register the OT mortal-address แห่ง-form. Doc-debt, not a translation defect.
  - **§12 — רוּחַ "new spirit" lexeme split.** רוּחַ חֲדָשָׁה is **จิตใจใหม่** at 11:19 and 18:31 but **จิตวิญญาณใหม่** at 36:26 — and 11:19 ↔ 36:26 are the deliberate promise-doublet (36:26's own KD glosses "cf. 11:19"). Normalize (recommend จิตใจใหม่, the 2-vote majority + 11:19 anchor). Secondary: the indwelling Spirit is bare วิญญาณ(ของเรา) at 36:27/37:14 but พระวิญญาณ in the transport formulas + 39:29 — defensible (gift vs. agent), worth a conscious ratify-or-normalize alongside.
  - **§16 — covenant of peace בְּרִית שָׁלוֹם / בְּרִית עוֹלָם.** Uniform (พันธสัญญาแห่งสันติสุข 34:25/37:26; พันธสัญญานิรันดร์ 16:60/37:26), KD-cross-linked, but undocumented. **Recommend folding into the messianic-Branch/David doc** (below) or `ot_nt_cross_quotation_thread`.
  - **§19 — versification: EZK 21 offset unregistered + a false compliance claim.** Ezekiel ships pure MT numbering; ch. 21 runs MT 21:1–37 = English 20:45–21:32 (a full chapter-boundary shift; "until he comes whose right it is" sits at MT 21:32 = English 21:27). `versification_map.json` has **no EZK entry**, **zero** `versification` sub-objects exist across all 48 chapters, and `check_versification_anchor.py` default-passes (false-clean) — yet the **ch. 21:1 KD falsely states** *"(versification sub-objects added per verse)."* Worse than Jeremiah's 8/9 offset (which was REVIEW). **Register the EZK 21 zone + correct the false KD claim** (mind the "ship script doesn't stage the map" gotcha).
  - **§21 — חַי־אָנִי "as I live" — new-lock candidate, now overdue.** All **16/16** occurrences → **เรามีชีวิตอยู่แน่ฉันใด**, perfectly uniform — exactly the form the Jeremiah audit recommended formalizing into `hebrew_oath_formulas §1.5`. The doc still has no §1.5. Ezekiel's 16 uniform witnesses make formalization overdue. **Add §1.5.**
  - **§22 — uncover-nakedness euphemism (chs. 16, 23).** The OT's most graphic chapters are rendered faithfully (23:20 explicit: อวัยวะเพศ / น้ำกาม, KD "explicit but not gratuitous") per `uncover_nakedness_euphemism §6`. One deviation: **22:10** uses the euphemism เปิดสิ่งที่ควรปกปิดของบิดา where doc §6 lists 22:10 under "literal ความเปลือยเปล่า consistently." Reconcile (allow the ʿerwaṯ-ʾāḇ incest-idiom euphemism in the doc, or re-render literal). Optional: a reader-facing graphic-content note for chs. 16/23 (none exists; Ben's call).
- **STABLE-but-undocumented patterns recommending doc-lift / new locks:** the **Davidic-shepherd / "my servant David"** rendering (§14 — plain register, KD-only; recommend finally creating the twice-deferred `messianic_branch_tzemach_2026-06.md`, now widened to cover the Davidic-shepherd thread + cedar-shoot ↔ Isa 11:1/Jer 23:5 byte-link + brit-shalom lock + a **§0 phrasing template** so the down-toning decided in §14 is enforced by reference before Daniel + Zechariah); **חַי־אָנִי** (§21 — formalize into `hebrew_oath_formulas §1.5`); the **בֶּן־אָדָם** three-way system (§9 — amend `son_of_man_disambiguation`); **covenant of peace** (§16).
- **External AI review (§3) pending.** Suggested 4-item packet: the codified anthropomorphism rule (§10 DECIDE); the foreign-monarch genre-split (§11 DECIDE); the messianic-summary §0 regression (§14 DECIDE); the MT/LXX temple-disclosure question (§18 DECIDE).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. אֲדֹנָי יְהוִה — "Lord GOD" (the 217× signature compound) — **LOCKED**

Ezekiel's defining feature. **217 occurrences** of אֲדֹנָי יְהוִה, all rendered **องค์พระผู้เป็นเจ้า** (Adonai collapsed, per the `divine_names_table` mid-sentence sub-rule): 212 mid-sentence appositional → bare องค์พระผู้เป็นเจ้า; 5 sentence-initial vocative → **ข้าแต่องค์พระผู้เป็นเจ้า** (4:14, 9:8, 11:13, 21:5 — the prophet's אֲהָהּ אֲדֹנָי יְהוִה "Alas, O Lord GOD!" lament-interjection; + 37:3 אֲדֹנָי יְהוִה אַתָּה יָדָעְתָּ "O Lord GOD, you know," a direct vocative reply). Zero verses stack Adonai (องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย) and zero are missing the rendering. The compound-vocative position rule (2026-05-23) is applied correctly — only the interjection/vocative cases take ข้าแต่. **LOCKED** ✓ per `divine_names_table_2026-05.md`. **Severity: GREEN.**

---

## 2. כֹּה אָמַר אֲדֹנָי יְהוִה — "Thus says the Lord GOD" — **LOCKED**

122 occurrences. **113** → **องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า**; the other 9 are natural Thai re-orderings where the formula names an addressee (องค์พระผู้เป็นเจ้าตรัสแก่ X ดังนี้ว่า — to the mountains 6:3, Jerusalem 16:3, Tyre 26:15, the dry bones 37:5). Same vocabulary throughout; no lexical drift. **LOCKED** ✓. **Severity: GREEN.**

---

## 3. נְאֻם אֲדֹנָי יְהוִה — "declares the Lord GOD" — **LOCKED**

81 occurrences, **all 81** → **องค์พระผู้เป็นเจ้าตรัส…** (…ตรัสไว้ดังนี้ / …ตรัสว่า). Perfectly uniform. **LOCKED** ✓. **Severity: GREEN.**

---

## 4. Bare standalone אֲדֹנָי (non-compound) + plain יְהוָה — **LOCKED**

Only 5 standalone (non-compound) Adonai tokens, **all 3rd-person title references**, all → **องค์เจ้านาย** (correct per the 4-way table, 3rd-person-title row): the people's complaint דֶּרֶךְ אֲדֹנָי "the way of the Lord is not just" (18:25, 18:29, 33:17, 33:20) + the bare-Adonai messenger formula 21:14. No standalone prayer-vocative Adonai in Ezekiel (the laments use the *compound* אֲהָהּ אֲדֹנָי יְהוִה, §1). Plain non-compound יְהוָה (≈200 verses, mostly the recognition formula and דְּבַר־יְהוָה) → **องค์พระผู้เป็นเจ้า** with zero misses. **LOCKED** ✓. **Severity: GREEN.**

---

## 5. YHWH first-occurrence footnote coverage — **LOCKED (complete)**

All **47** chapters that contain a divine name carry the Layer-2 `tetragrammaton_convention_first_occurrence` footnote in `output/textual_variants/ezekiel_NN.json`. **Ch. 19** (the lament/dirge over Israel's princes) correctly has **no divine name** and therefore no footnote and no variant file — the lone no-YHWH chapter, parallel to the Daniel/Ecclesiastes no-name precedent. Ch. 42 uses unpointed יהוה at v. 13 (דְּבַר־יהוה) and carries its footnote. Several footnotes go further (ch. 7 documents the MT/LXX verse-order difference; chs. 40/42/45 carry measurement notes — §18). Complete coverage. **LOCKED** ✓. **Severity: GREEN.**

---

## 6. `check_divine_names.py --book EZK` — **LOCKED (cleanest checker state of any major prophet)**

`Divine names — checked 48 OT chapter(s); 47 contain YHWH` — exit 0, **0 hard fails, 0 soft warnings.** Unlike Jeremiah (2 single-yod אֲדֹנִי human-address false positives), Isaiah (6), and Daniel (1), Ezekiel triggers **no** warnings — there is no suffixed-human אֲדֹנִי "my lord" form in the sampled set to adjudicate. **LOCKED** ✓. **Severity: GREEN.**

---

## 7. Recognition formula — "you/they shall know that I am YHWH" (אֲנִי יְהוָה) — **LOCKED**

Ezekiel's leitwort. **84 verses** across chs. 5–39 contain אֲנִי יְהוָה; **all 84** render the divine-name core as the exact locked phrase **เราคือองค์พระผู้เป็นเจ้า** (zero drift to พระยาห์เวห์ or bare พระเจ้า). Sub-variants all keep the core intact:
- **Recognition proper** (ידע "know that," ~65 vv) → …จะรู้ว่าเราคือองค์พระผู้เป็นเจ้า (6:7, 6:14, …).
- **"I YHWH have spoken"** (אֲנִי יְהוָה דִּבַּרְתִּי, ~15 vv) → เราคือองค์พระผู้เป็นเจ้า เราได้ลั่นวาจาแล้ว (5:15, 5:17, 17:24).
- **Holiness variant** (כִּי אֲנִי יְהוָה מְקַדִּשְׁכֶם, the doc-named 20:12 + 37:28) → เราคือองค์พระผู้เป็นเจ้าผู้ทรงชำระ…ให้บริสุทธิ์ (relative clause unfolds verbally onto the core, matching the doc pattern; cf. 7:9 "…ผู้ลงโทษ").

Explicitly forward-locked in `i_am_yhwh_holiness_formula_2026-05.md §3`, which names Ezekiel's recognition formula by lemma. Execution complies exactly. **LOCKED** ✓. **Severity: GREEN.**

---

## 8. The merkabah / glory anthropomorphism (chs. 1, 8, 10) — **STABLE** (register detail → §10)

Ezekiel's unique visible-divine-form material is handled on a hedge/definiteness axis: the **divine figure and his actions stay royal** — throne כִּסֵּא → **พระที่นั่ง**, the enthroned figure → ประทับ + pronoun พระองค์, voice → พระสุรเสียง…ตรัส, glory → พระสิริ, and in 8:3 the divine actions are royal (ทรงยื่น, ทรงยก) — but **hedged vision-body-parts drop to plain** with explicit contrast: 8:3 תַּבְנִית יָד "the form of a hand" → สิ่งที่ดูเหมือนมือ, KD: *"deliberately indefinite (not the definite divine hand of 1:3) → plain มือ with the 'what looked like' hedge, reserving royal พระหัตถ์ for the unhedged divine hand."* This third (hedge-conditioned) register rule is principled and self-aware; its relationship to the first-person-plain rule is part of §10. **STABLE.** **Severity: GREEN** (the register-policy question rolls into §10).

---

## 9. "son of man" (בֶּן־אָדָם) — God's address to Ezekiel — **STABLE + REVIEW (doc reconciliation)**

**93 verses** (chs. 2–47), **all 93** → **บุตรแห่งมนุษย์เอ๋ย** (connector แห่ง + vocative เอ๋ย), perfectly uniform. The form is **deliberately distinct** from the Christological title **บุตรมนุษย์** (no connector; confirmed at Dan 7:13 + the NT) and consistent with the OT *mortal*-sense already shipped at **Dan 8:17** and **Ps 8:4** — a doctrinally load-bearing three-way system: title บุตรมนุษย์ / generic-plural บุตรของมนุษย์ / mortal-address บุตรแห่งมนุษย์. Rationale documented once, at the 2:1 KD.

**REVIEW — the policy doc owes an amendment.** `son_of_man_disambiguation_2026-04.md` is **NT-scoped** and its "alternatives considered" section **explicitly rejected บุตรแห่งมนุษย์** ("with แห่ง") — aimed at the *NT title*, but on its face the shipped Ezekiel mortal-address is the very form the doc rejects. **Recommend amending the doc** to register the three-way OT/NT system and authorize แห่ง for the prophetic mortal-address (Ezekiel ×93, Dan 8:17, Ps 8:4), keeping the บุตรมนุษย์-no-แห่ง rule for the NT title. Doc-debt, not a translation error. **Severity: LOW** (execution flawless; documentation lags).

---

## 10. Divine anthropomorphism — the codified first-person-plain rule, operationalized at scale — **DECIDE (the loudest finding)**

`divine_anthropomorphism_thai_grammar_2026-05.md §2.1` locks God's body parts to royal register with **no person-based exception**. Ezekiel honors that **only** for 3rd-person narration and the Exodus power-formula, and **systematically drops to plain for every first-person divine self-reference**, by stated, self-locking design — the same drift Isaiah §13 and Jeremiah §13 flagged (both unresolved), now the **largest, densest, most rigorously-codified instance in the corpus**.

**The core split (same idiom, two registers, decided by grammatical person):**

| Idiom | 3rd-person narration ("hand of YHWH") | 1st-person divine speech ("MY hand") |
|---|---|---|
| יָד / hand | **พระหัตถ์ (royal)** — 1:3, 3:14, 3:22, 8:1, 33:22, 37:1, 40:1 (7×) | **มือ (plain)** — 6:14, 13:9, 14:9, 14:13, 16:27, 20:22, 25:7, 25:13, 25:16, 35:3, 37:19, 39:21 (12×) |

**10a. "I will stretch out my hand against" (נטה יד, 1cs) — all plain มือ, drift CODIFIED.** Every occurrence renders มือ, never พระหัตถ์, with the rule spelled out and explicitly contrasted against the royal narration form — 6:14 KD: *"God's OWN hand in 1st-person speech → PLAIN มือ … contrast the narrator-voice royal พระหัตถ์ at 1:3."* (also 14:9, 14:13, 16:27, 25:7/13/16, 35:3; plus 1st-person non-stretch hands 13:9, 20:22, 37:19, 39:21).

**10b. "My eye(s) will not pity" (לֹא תָחוֹס עֵינִי) — Ezekiel's signature refrain, all plain ตา, named "5:11 lock."** 7/7 plain ตา: 5:11 (KD: *"God's OWN eye in 1st-person speech → PLAIN ตา (not royal พระเนตร)"* — the anchor), 7:4, 7:9 ("consistent with 5:11"), 8:18 (+ "my ears" בְאָזְנַי → plain หู), 9:10 ("lock, 5:11"), 20:17 (positive counterpart). The 2nd-person executioner form (9:5 "let not your eye spare") mirrors it.

**10c. "I will set my face against" (נָתַתִּי פָנַי) — all plain หน้า, codified.** 14:8 (KD: *"plain หน้า (1st-person convention)"*), 15:7 ("as 14:8").

**10d. The two named exceptions (a second, finer split).** The **Exodus power-formula** keeps royal even in 1st-person speech: 20:33–34 בְּיָד חֲזָקָה וּבִזְרוֹעַ נְטוּיָה → **พระหัตถ์**อันแข็งแกร่ง **พระกร**ที่เหยียดออก, KD: *"as a lexicalized epithet … keeps Rachasap even in 1st-person speech, distinct from the plain-hand convention."* So **within chapter 20**: "I withheld my **มือ**" (20:22) vs "with strong **พระหัตถ์** and outstretched **พระกร**" (20:33) — identical lemma יָד, same speaker, eleven verses apart. The **hedged vision-body-part** (8:3 "form of a hand" → plain มือ, §8) is the third exception.

**Quantified tally:** ~22 first-person divine body-part verses render **plain by stated rule**; **0** render royal. The doc's §2.1 royal mapping is followed only in 3rd-person narration (7×) + the Exodus epithet (2×).

**Why DECIDE, not REVIEW:** (1) it directly contradicts the governing doc, which states the mapping has "no person-based exception"; (2) it **compounds** Isaiah §13 + Jeremiah §13 rather than resolving them, and Ezekiel is the largest test case, so whatever is decided here sets the retroactive corpus precedent for three major prophets; (3) it is now self-justifying and self-locking — the KDs cite each other, so a mechanical check sees internal consistency and never flags it; (4) three same-idiom splits coexist (พระหัตถ์/มือ, พระเนตร/ตา, พระพักตร์/หน้า — plus the Exodus-epithet sub-split).

**DECIDE — Ben must choose one and apply it corpus-wide:**
(a) **Ratify** a documented "first-person divine self-reference → plain register" exception, amend `divine_anthropomorphism_thai_grammar_2026-05.md`, and formalize the Exodus-formula + hedge carve-outs (three books now lean this way with explicit rationale — this appears to be the de-facto corpus position, but the doc still wins on paper); **or**
(b) **Reverse** the ~22 Ezekiel verses to Rachasap (matching the Isaiah §13 recommendation), plus the Isaiah/Jeremiah cases.

Either way, **reconcile with Isaiah §13 + Jeremiah §13** so the corpus speaks with one voice. **Severity: HIGH** (corpus-lock conflict, codified, cross-book, load-bearing, invisible to gates).

---

## 11. Foreign-monarch register — every ruler plain, hardening the cross-book conflict into a genre split — **DECIDE**

`ot_register_policy §2.2` grants foreign emperors full ราชาศัพท์ *even if villainous*; `§2.6` (the Ezra lock) extends ทรง to narrator-voice emperor-action verbs; **Daniel gives all four emperors full ทรง**. **Ezekiel renders every foreign and human ruler in plain register** — a full-book scan for ทรง/พระองค์/เสด็จ on ruler verses returned **zero hits**.

| Ruler | Key verses | Rendering | Register | Status |
|---|---|---|---|---|
| **Nebuchadnezzar / Babylon** | 26:7–12; 29:18–19; 30:10 | เนบูคัดเนสซาร์กษัตริย์บาบิโลน; "king of kings" → จอมกษัตริย์; **siege verbs all plain** (26:8–9 ฆ่า/ตั้ง/ก่อ) | **PLAIN** | **DECIDE** |
| **Pharaoh / Egypt** | 29:2–3; 31:2; 32:2 | ฟาโรห์; 2nd-person เจ้า; mocking imagery intact (สัตว์ร้ายมหึมา, สิงห์หนุ่ม) | PLAIN | STABLE |
| **Prince/king of Tyre** | 28:2 (נְגִיד→เจ้านาย), 28:12 (מֶלֶךְ→กษัตริย์) | plain title-nouns; self-deification rebuked (เจ้าเป็นเพียงมนุษย์) | PLAIN | STABLE |
| **Prince of Israel / Zedekiah** | 12:10–12, 17:12–16, 21:25 | plain; **12:12 KD** invokes the Rachasap shame-downshift → plain แบก/คลุม | PLAIN (conscious §1.4/§2.2) | STABLE |
| **Gog** | 38:2–3, 39:1 | เจ้านายผู้เป็นประมุข; **39:1 KD**: "plain adversary register (§3)" | PLAIN | LOCKED |
| **King of Assyria (cedar)** | 31:3 | allegorized as a fallen cedar (มัน) | PLAIN / N-A | LOCKED |

Ezekiel is **internally fully consistent** (uniformly plain, no drift), and the choice is **considered** — 12:12 reasons to plain via the shame-downshift, 38:3/39:1 via the §3 adversary rule. There is a defensible theological logic (these are judgment oracles mocking the rulers; granting ทรง to the self-deifying king of Tyre or the "great monster" Pharaoh would undercut the rhetoric). **But it is not what §2.2/§2.6 as written require**, including the narrator-voice siege verbs the §2.6 Ezra lock specifically upgraded.

**The cross-book picture (the crux):** Ezekiel agrees with **Jeremiah** (§24, Nebuchadnezzar plain incl. siege verbs) **against** the Writings block (Daniel + the §2.6 Ezra lock). As the **third data point** Ezekiel tips the count — Nebuchadnezzar is now **plain in 2 books (Jer, Ezk), royal in 1 (Dan)** — and hardens the conflict into a **genre-level pattern**: *Latter-Prophets judgment oracles flatten the rulers; Writings court-narratives dignify them.* The unifying `foreign_monarch_register` doc **owed since Ezra still does not exist.**

**DECIDE:**
1. **Write `docs/translator_decisions/foreign_monarch_register_2026-05.md`** (still nonexistent), deciding whether to carve out a **Latter-Prophets judgment-oracle exception** (plain for condemned foreign rulers in oracle voice; royal only in court-narrative voice — retroactively blessing Jer + Ezk and confining §2.6 to narrative books) **or** declare Jeremiah + Ezekiel non-conformant and schedule an upgrade.
2. **Resolve jointly with the still-untagged EZR/NEH/EST/DAN block + Jeremiah** so Nebuchadnezzar above all speaks with one voice across books. Ezekiel cannot be tagged v1 until this genre-policy is written — it is now the deciding third data point.

(Pharaoh / Tyre / Zedekiah ride on the Nebuchadnezzar decision; Gog + Assyria-cedar are correctly plain under §3/allegory and out of scope.) **Severity: HIGH** (cross-book inconsistency on the OT's most prominent foreign king, now a genre split + a long-owed doc).

---

## 12. רוּחַ (Spirit / wind / breath) — the four-sense disambiguation — **LOCKED + REVIEW (new-spirit split)**

Ezekiel is the most רוּחַ-dense book in the OT (~52 occurrences across four senses), all hinging on one word. The disambiguation is principled and, at the key crux, **reader-flagged**:
- **Spirit transports/empowers the prophet** → uniform **พระวิญญาณ** + royal verb (เสด็จ/ทรงยก): enters (2:2, 3:24), lifts (3:12, 8:3, 11:1, 11:24, 43:5, 3:14). Sub-forms differentiated: רוּחַ אֱלֹהִים → พระวิญญาณของพระเจ้า (11:24), רוּחַ יְהוָה → พระวิญญาณขององค์พระผู้เป็นเจ้า (37:1). **LOCKED** per `spirit_of_yhwh_empowerment_2026-05.md`.
- **The ch. 37 dry-bones multi-sense play** (the signature OT pun: רוּחַ shifts between Spirit / breath / wind within a few verses) → **พระวิญญาณ** (37:1, 14) / **ลมหายใจ** (37:5, 6, 8, 9, 10) / **ลมทั้งสี่ทิศ** (37:9 four-winds), each context-driven with per-verse KDs **and** a **reader-facing disambiguation note** in `textual_variants/ezekiel_37.json` (attached to the 37:1 footnote): *"คำว่า רוּחַ ในบทนี้มีความหมายหลากหลายตามบริบท — 'พระวิญญาณ'…'ลมหายใจ'…'ลม'…"* The pun is both principled and transparently flagged. **LOCKED.**
- **Wind** → ลม (storm 1:4/13:11/13:13 ลมพายุ; east wind 17:10/19:12/27:26; scatter-to-the-winds 5:2/12:14/17:21). **LOCKED.**
- **Human/animating/created spirit** → วิญญาณ/จิตใจ (living-creatures' spirit 1:12/1:20/10:17; false-prophet spirit 13:3). **STABLE.**

**REVIEW — "new spirit" (רוּחַ חֲדָשָׁה) lexeme split.** 11:19 → **จิตใจใหม่**, 18:31 → **จิตใจใหม่**, but **36:26 → จิตวิญญาณใหม่** — for the identical phrase, and 11:19 ↔ 36:26 are the deliberate promise-doublet (36:26's KD glosses "cf. 11:19"). **Normalize** (recommend จิตใจใหม่, 2-vote majority + 11:19 anchor). Secondary: the indwelling Spirit is bare **วิญญาณ(ของเรา)** at 36:27/37:14 (KDs cite Acts 2 / Rom 8 / Joel 2) but **พระวิญญาณ** in transport + 39:29 — defensible (implanted gift vs. divine agent), worth a conscious ratify-or-normalize. Minor doc-scope note: the 11:5 רוּחַ יְהוָה uses the verb נָפַל "fell upon," outside the `spirit_of_yhwh_empowerment` 4-way verb lock (הָיָה עַל / לָבַשׁ / פָּעַם / צָלַח) — rendering is fine; optional one-line doc append. **Severity: LOW.**

---

## 13. כְּבוֹד יְהוָה — "the glory of YHWH" leitwort — **LOCKED**

Uniform **พระสิริ** across the book's structural arc — glory that fills, departs (chs. 8–11: 9:3 → 10:4 → 10:18 → 11:23, with KDs tracking the departure verbs), and returns (ch. 43: 43:2 "from the east — exactly reverses 11:23" → 43:4 → 43:5 → 44:4). Sub-forms differentiated (כְּבוֹד יְהוָה → พระสิริขององค์พระผู้เป็นเจ้า; כְּבוֹד אֱלֹהֵי יִשְׂרָאֵל → พระสิริของพระเจ้าแห่งอิสราเอล; כְּבוֹדִי → พระสิริของเรา). **Homonym discipline clean** — the non-glory כבד root is never พระสิริ (3:5 "heavy of tongue" → เข้าใจยาก; 21:26 "liver" → ตับ; 27:25 heavy cargo; 28:22 verb "be glorified" → ได้รับเกียรติ; 31:18 Pharaoh's secular glory → ศักดิ์ศรี). **LOCKED** ✓. **Severity: GREEN.**

---

## 14. Messianic / Davidic committal surface — the §0 line crossed in the note layer — **DECIDE**

The translation **surface is clean everywhere** — the verse text never asserts fulfillment, register is correct (**"my servant David"** uniformly **plain** ดาวิดผู้รับใช้ของเรา at 34:23–24 / 37:24–25, correct for a not-yet-reigning future figure per the Jer 30:9/30:21 precedent), and NT cross-quotes are harmonized (§17). **But the `thai_summary` note layer regresses past the §0 bar the Jeremiah audit drew.** Jeremiah's most-forward line (31:31, *"cited in Heb 8/10 as fulfilled in Christ"*) passed because it **reports what Hebrews does**; the Jeremiah audit praised the book as *"§0-cleaner than Isaiah."* Ezekiel instead **asserts the identification as bare fact in the translator's own voice:**

| Verse | Summary clause (verbatim) | Gloss | §0 |
|---|---|---|---|
| **34:23** | *"…หมายถึงเชื้อสายของดาวิด **คือพระคริสต์** ผู้เลี้ยงแกะที่ดี (ยอห์น 10:11)"* | "means the seed of David, **who is the Christ**, the Good Shepherd (John 10:11)" | **assertion** |
| **34:1** | *"…เป็นภาพล่วงหน้าของพระเยซู ผู้เลี้ยงแกะที่ดี"* | "a foreshadowing of Jesus" (as fact) | assertion |
| **17:22** | *"กษัตริย์ในวงศ์ดาวิดที่แท้จริง**คือพระคริสต์**"* | "the true Davidic king **is the Christ**" | **assertion** |
| **17:23** | *"สื่อถึงอาณาจักรของพระเมสสิยาห์ — พระเยซูทรงนำภาพนี้ไปใช้ใน…มัทธิว 13:32"* | mustard-seed half is **report-form (OK)**; "kingdom of the Messiah" is the assertive part | mixed |
| **21:32** | *"…จะได้รับการสถาปนาใหม่**ในพระคริสต์** ผู้ทรงเป็นกษัตริย์โดยชอบธรรม"* | "re-established **in Christ**" (Gen 49:10/Shiloh cross-ref sound) | **assertion** |

Plus the 34:23 / 37:24 / 37:25 KDs assert "fulfilled in Christ" / "the coming Davidic Messiah." A correct **report-form template already exists in the same book** — 47:1 *"ภาพนี้สำเร็จในวิวรณ์ 22:1"*, 39:17 *"สะท้อนในวิวรณ์ 19:17–18"*, 17:23b *"พระเยซูทรงนำภาพนี้ไปใช้ใน…"* — all reporting *what the NT text does*, which is §0-compliant.

**DECIDE — Ben must decide whether to down-tone the five+ assertive clauses to report-form** (e.g. "ในการตีความของคริสเตียน อ่านว่า… / พันธสัญญาใหม่นำข้อนี้ไปใช้กับพระคริสต์" — "in Christian interpretation, read as… / the NT applies this to Christ") **or affirm them.** The fix is mechanical and the template is in-book; surface, register, and harmonization need no change. This is the book's headline note-layer gate, the natural external-AI item, and tests messianic-policy continuity with Isaiah §6 / Jeremiah §6. **Severity: MEDIUM-HIGH** (theological, high reviewer-visibility, RULES §0; but confined to the unrendered-elsewhere… no — `thai_summary` **is** reader-rendered, which is why it matters).

---

## 15. "my servant David" register — **STABLE** (covered in §14)

Uniformly plain (ผู้รับใช้ของเรา, no ราชาศัพท์) across 34:23–24 / 37:24–25 — correct per the "royal-only-when-actively-reigning" rule (David here is future/not-yet-reigning, like Jer 30:9/30:21). **STABLE.** **Severity: LOW.**

---

## 16. Covenant of peace — בְּרִית שָׁלוֹם / בְּרִית עוֹלָם — **STABLE (recommend lock)**

Uniform: בְּרִית שָׁלוֹם → **พันธสัญญาแห่งสันติสุข** (34:25, 37:26); בְּרִית עוֹלָם → **พันธสัญญานิรันดร์** (16:60, 37:26). KD-cross-linked (34:25 ↔ 37:26), no drift, no §0 issue. Undocumented (KD-only). **Recommend folding into the messianic-Branch/David doc** (§14 recommendation) or `ot_nt_cross_quotation_thread`. **Severity: LOW.**

---

## 17. OT→NT cross-quotation thread — **LOCKED**

All shipped NT targets verified present and harmonized; the notes name them descriptively (report-form), which is the §0-correct model:

| Ezekiel | → NT | Verdict |
|---|---|---|
| 34:23 (one shepherd, David) | John 10:11 | byte-faithful (ผู้เลี้ยงแกะที่ดี); §0 note issue → §14 |
| 37:27 (my dwelling with them) | Rev 21:3; 2 Cor 6:16 | harmonized; 48:35 summary cites Rev 21:3 descriptively |
| 47:1 (river from the temple) | Rev 22:1 | summary "สำเร็จในวิวรณ์ 22:1" — report-form ✓ |
| 47:12 (leaves for healing) | Rev 22:2 | correctly *not* byte-identical (Heb vs Grk differ); summary accurate |
| 39:17 (sacrificial feast) | Rev 19:17–18 | descriptive ✓ |
| 38–39 (Gog) | Rev 20:8 | name-form consistent (กอกและมาโกก) |
| 36:25–27 (clean water / new heart) | echoes John 3 / Heb 10:22 | surface clean; no NT-assertion in summary (cleanest) |

**LOCKED** ✓. **Severity: GREEN** (the §14 note-layer issue is the one exception).

---

## 18. MT/LXX divergence + the temple-vision measurements (chs. 40–48) — **DECIDE (the textual headline)**

**Surface: correct** — MT throughout, per `ot_canon_and_text_base` + `mt_vs_lxx_textual_variant_handling`. **Disclosure: incomplete and structurally fragile.** Every chapter carries exactly one `textual_variants` entry (the YHWH footnote); Ezekiel has **zero stand-alone textual-variant footers** — every textual note is appended to the divine-name footnote.

Only **3 of 9** temple chapters surface a measurement note, all bundled inside the YHWH footnote:
- **ch. 40** (v. 49): MT "eleven cubits" / no steps vs LXX "twelve cubits" + "ten steps"; Eremos = MT.
- **ch. 42** (v. 4, 16–20): MT אַמָּה אֶחָת "one cubit" (likely scribal for מֵאָה "hundred") vs LXX/BSB "hundred cubits"; v. 16–20 MT "500 reeds" vs BSB "500 cubits"; Eremos splits (v. 4 by sense, v. 16–20 per MT).
- **ch. 45** (v. 1): MT "ten thousand" vs LXX/BSB "twenty thousand"; Eremos = MT.

Chapters **41, 43, 44, 46, 47, 48 disclose nothing.** Many cruxes live only in `key_decisions` (never rendered): 40:14, 42:16 reeds-vs-cubits, 45:12 mina. There is **no book-level or temple-section disclosure note.** (Good precedent inside the book: ch. 7's footnote *does* disclose the MT/LXX verse-order difference at 7:3–9 — reader-facing.) Ezekiel is the OT's densest measurement-crux book; per the `mt_vs_lxx §2.3` floor and the Jeremiah §9 precedent, the "3/9 + bundled in the YHWH footnote" state is a genuine disclosure gap.

**DECIDE — ratify a temple-vision disclosure standard or affirm the current state:**
1. Add a **temple-section (40–48) disclosure note** (minimally a §2.3-style header: "Eremos follows MT measurements throughout the temple vision; English/BSB figures, following LXX in places, differ").
2. Consider **decoupling measurement footers from the YHWH footnote type** (a non-divine-name `textual_variants` entry) so a reader who doesn't open the divine-name footnote still sees them, and promote the KD-only cruxes (40:14, 42:16, 45:12).

**No translation-surface edit is implied** — this is an apparatus decision, the Ezekiel analogue of Jeremiah §9. **Severity: MEDIUM** (the temple vision's defining textual character; strong external-AI candidate).

---

## 19. Versification (MT vs English) — **REVIEW (EZK 21 offset unregistered + a false compliance claim)**

Ezekiel ships **pure MT numbering.** The reader-affecting divergence is **ch. 21**: ch. 20 ends at v. 44, ch. 21 runs **MT 21:1–37 = English/BSB 20:45–21:32** (a full chapter-boundary shift; teraphim divination sits at MT 21:26, and "until he comes whose right it is" at MT 21:32 = English 21:27). **Gaps:** `grep EZK data/versification_map.json` = **none**; **zero** `versification` sub-objects exist across all 48 chapters; `check_versification_anchor.py --book EZK` exits 0 only because EZK is **absent from the map** (false-clean) — and the **ch. 21:1 KD falsely claims** *"(versification sub-objects added per verse)"* when none exist. This is **worse than Jeremiah's 8/9 offset** (flagged REVIEW): a whole-chapter offset, unregistered, with a false in-data compliance claim. **Recommend registering the EZK 21 zone in `versification_map.json` and correcting the ch. 21:1 KD** (mind the "ship script doesn't stage the map" gotcha — commit the map edit manually). **Severity: LOW-MEDIUM** (mechanical fix, but the false KD claim should not ship).

---

## 20. Idols / pagan deities / polytheistic register — **STABLE / LOCKED**

- **גִּלּוּלִים** (Ezekiel's signature contemptuous idol-word, ~36–39×) → uniformly **รูปเคารพ**, corpus-locked to Lev 26:30. The KDs acknowledge the likely "dung-pellets" contempt but **deliberately do not preserve it** (รูปเคารพ is neutral) — a conscious consistency-over-nuance lock for cross-book uniformity with Leviticus. **STABLE** (optional REVIEW: if Ben wants the contempt audible it would require a corpus-wide re-lock affecting Lev — likely keep as-is).
- **ch. 8 abomination tour — register-correct:** Tammuz 8:14 → **เทพทัมมุส** (เทพ- foreign-deity prefix, not พระ-); image of jealousy 8:3/5 → descriptive รูปเคารพแห่งความหึงหวง; sun-worship 8:16 → plain ดวงอาทิตย์ (no deification). Teraphim 21:26 → รูปเคารพประจำบ้าน; belomancy/hepatoscopy descriptive. All correct per `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`. **LOCKED.** **Severity: GREEN.**

---

## 21. חַי־אָנִי "as I live" (divine self-oath) — **STABLE (new-lock candidate, overdue)**

All **16/16** occurrences → **เรามีชีวิตอยู่แน่ฉันใด**, perfectly uniform (5:11; 14:16/18/20; 16:48; 17:16/19; 18:3; 20:3/31/33; 33:11/27; 34:8; 35:6/11) — exactly the form the Jeremiah audit recommended formalizing into `hebrew_oath_formulas §1.5`. The doc still has no §1.5. Ezekiel's 16 uniform witnesses make formalization overdue. **Recommend adding §1.5 חַי־אָנִי → เรามีชีวิตอยู่แน่ฉันใด** (noting the deliberate 1st-vs-3rd-person verb split, מีชีวิตอยู่ vs ทรงพระชนม์, so it isn't later "corrected" into false uniformity). **Severity: LOW.**

---

## 22. Uncover-nakedness euphemism (chs. 16, 23) — **STABLE + REVIEW (22:10 deviation)**

The OT's most sexually graphic chapters are rendered **faithfully, not euphemized**, per `uncover_nakedness_euphemism §6`: 16:8 (positive covenant metaphor) → ปกปิดความเปลือยเปล่า; 16:36, 23:10/18/29 → literal ความเปลือยเปล่า; **23:20** (the OT's most graphic verse) explicit — อวัยวะเพศ "genitals," น้ำกาม "emission," KD: *"explicit but not gratuitous."*

**REVIEW — 22:10 deviation.** Doc §6 lists 22:10 under "literal ความเปลือยเปล่า consistently," but shipped 22:10 (ʿerwaṯ-ʾāḇ "father's nakedness") uses the **euphemism** เปิดสิ่งที่ควรปกปิดของบิดา (KD justifies it as the father's-wife incest idiom per Lev 18:8). **Reconcile** — update doc §6 to allow the euphemism for the ʿerwaṯ-ʾāḇ incest idiom, or re-render 22:10 literal. Optional: a reader-facing graphic-content note for chs. 16/23 (none exists; the `textual_variants` there carry only the YHWH footnote — Ben's call). **Severity: LOW.**

---

## 23. Mechanical (§1) + infrastructure

- **48/48** chapters: `output/check_reports/ezekiel_NN_review.md` (green) + `output/back_translations/ezekiel_NN.json` + `output/translations/ezekiel_NN.json` ✓
- **47/47** chapters-with-a-divine-name: `output/textual_variants/ezekiel_NN.json` carrying the YHWH first-occurrence footnote — **complete coverage** (ch. 19 correctly none; §5).
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings.**
- `check_phrase_consistency.py`: **0 violations across 38 audited locks** (29,886 verses).
- `audit_inclusion_variants.py --book ezekiel --strict`: **0 candidates, exit 0** (correct — the inclusion-variant policy is NT-only; Ezekiel's MT/LXX issues route through §18).
- `check_divine_names.py --book EZK`: **exit 0, 0 hard fails, 0 soft warnings** (§6 — the cleanest checker state of any major prophet).
- `check_versification_anchor.py --book EZK`: **exit 0 — but false-clean** (EZK absent from the map; §19).
- `git status output/`: clean (the 3 modified files in `docs/end_of_book/_external_inbox/` are unrelated GEN/JON/JUD raw inbox files).
- **`export_to_usfm.py --book EZK`: FAILS — "Unknown book code: EZK."** The recurring OT-USFM book-code-registration gotcha (logged for LAM/SNG/ISA/JER in every prior OT audit). **Non-blocking infra gap** — flag for the maintainer to register `EZK` in the export script's book table; not a translation defect.

---

## Recommendation

**Ezekiel ships in strong corpus-hygiene shape** — mechanically among the cleanest major-prophet states to date (217× אֲדֹנָי יְהוִה rendered with total consistency; 84× recognition formula and 93× "son of man" and 16× "as I live" each perfectly uniform; complete divine-name footnote coverage; **zero** divine-name checker warnings; พระสิริ glory leitwort with no homonym leakage; the ch. 37 multi-sense רוּחַ pun both principled and reader-flagged). The four DECIDE items are all **policy-and-apparatus decisions, not surface-quality defects**, and **three of them are corpus-level questions Ezekiel inherited and sharpened** — the anthropomorphism rule (§10) and the foreign-monarch register (§11) were named by the Jeremiah audit as carrying their highest forward weight *into Ezekiel*, and Ezekiel is now the deciding instance of both; the messianic §0 regression (§14) is the one Ezekiel genuinely *worsens* relative to Isaiah/Jeremiah.

Tag `book-ezekiel-v1` after:
1. Ben's decisions on the **4 DECIDE** items: §10 anthropomorphism (ratify-the-exception-or-reverse + reconcile Isaiah §13 + Jeremiah §13), §11 foreign-monarch register (write the owed doc + reconcile Jeremiah + the EZR/NEH/EST/DAN block; Ezekiel is the third data point), §14 messianic §0 (down-tone the five+ assertive summaries to report-form, or affirm), §18 MT/LXX temple disclosure (apply the section-note apparatus, or affirm bundled-footnote).
2. Ben's decisions on the **6 REVIEW** items (§9 son-of-man doc, §12 new-spirit split, §16 covenant-of-peace lock, §19 versification registration + KD correction, §21 חַי־אָנִי §1.5, §22 22:10 reconciliation).
3. Any spot-revisions executed + checks re-run clean.
4. New docs written as decided: the twice-deferred **`messianic_branch_tzemach_2026-06.md`** (now widened to the Davidic-shepherd thread + cedar-shoot byte-link + brit-shalom lock + a **§0 phrasing template**, §14/§16), **`foreign_monarch_register_2026-05.md`** (§11); amendments to `hebrew_oath_formulas §1.5` (חַי־אָנִי, §21), `son_of_man_disambiguation` (the OT mortal-address แห่ง-form, §9), and `divine_anthropomorphism_thai_grammar` (§10, if ratifying the exception).
5. External AI sanity-check (§3 — the 4-item packet above).

The **anthropomorphism §10 + foreign-monarch §11** reconciliations are the two highest-value forward-protection actions — both are now three-book conflicts (Isa/Jer/Ezk; Jer/Ezk/Dan) that must be settled before they compound further into Daniel/the Twelve.
