# Zechariah — End-of-Book Review

**Date:** 2026-06-27
**Scope:** All 14 chapters; `glossary.json`; existing `docs/translator_decisions/` (locked corpus decisions).
**Trigger:** ZEC 14 shipped (commit `0658ce1b`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 14/14 chapters have green per-chapter review reports + `output/back_translations/zechariah_NN.json` + `output/textual_variants/zechariah_NN.json`; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 locks); `check_divine_names.py` returns **ZERO Zechariah warnings**; `git status output/` clean (only re-ran check-report artifacts). The ZEC-2 versification zone is **registered AND committed** (commit `16721b9e`).
- **Status counts: 7 LOCKED · 4 STABLE · 2 REVIEW · 1 DECIDE.**
- **Zechariah is the densest NT-cited book in the OT** (the Branch, the donkey-king 9:9, the thirty pieces of silver 11:12–13, the pierced one 12:10, the struck shepherd 13:7). The audit confirms the project handles this maximal-density messianic surface with **exemplary reception discipline** — natural non-committal body text, `nt_citation_note` Layer-2 footnotes, and summaries that credit the NT (`พันธสัญญาใหม่อ้างถึง…`) rather than asserting `คือพระคริสต์` as bare fact. This is the **strongest reception-restraint witness in the corpus**, clean of the Ezekiel §14 regression, and the strongest possible anchor for the recommended `committal_messianic_surface` doc (forecast in the Haggai audit).
- **The single DECIDE (§1) is mechanically invisible and conflicts with a LOCKED doc:** the compound מַלְאַךְ יְהוָה ("angel of YHWH") is rendered **ทูตขององค์พระผู้เป็นเจ้า** (dropping **สวรรค์**) at 1:11, 1:12, 3:1, 3:5, 3:6, 12:8, while standalone/interpreting angels keep **ทูตสวรรค์** — a deliberate internal theophanic distinction that **inverts** the `malak_yhwh_2026-05` lock (which mandates מַלְאַךְ יהוה → ทูตสวรรค์ขององค์พระผู้เป็นเจ้า, *keeping* สวรรค์, as enforced through 2 Kings). Ben must ratify the Zechariah distinction (and amend the doc) or normalize.
- **Two REVIEW items:** (§5) the `satan_accuser_corpus_mapping_2026-05` doc mandates a Layer-2 first-occurrence footnote at Zech 3:1 noting the article + role-sense `ผู้กล่าวหา / ปฏิปักษ์` (mirror of Job 1:6); the ch3 footnotes carry the Jude-9 rebuke note but **not** that article-role note — a mechanically-invisible gap of the Micah-ch5 / Joel-ch3 class. (§14) `export_to_usfm.py` still rejects ZEC (infra, non-blocking).
- **Two new corpus docs recommended:** `committal_messianic_surface_2026-06.md` (Zechariah = strongest anchor) and `day_of_the_lord_leitwort_2026-06.md` (ch14 = densest Day-of-YHWH cluster among the Twelve, joining Joel/Amos/Obadiah/Zephaniah). Plus, contingent on §1, a `malak_yhwh_2026-05` amendment.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging `book-zechariah-v1`.

---

## 1. מַלְאַךְ יְהוָה → ทูตขององค์พระผู้เป็นเจ้า (drops สวรรค์) — **DECIDE** (headline; conflicts with `malak_yhwh_2026-05`)

Zechariah's vision cycle (chs 1–6) and the 12:8 oracle distinguish **two angelic classes** with two different Thai surfaces:

| Hebrew | Thai | Verses | สวรรค์? |
|---|---|---|---|
| מַלְאַךְ יְהוָה (the **angel/messenger of YHWH** — the theophanic figure) | **ทูตขององค์พระผู้เป็นเจ้า** | 1:11, 1:12, 3:1, 3:5, 3:6, 12:8 | **WITHOUT** |
| הַמַּלְאָךְ הַדֹּבֵר בִּי (the **interpreting angel**) / standalone הַמַּלְאָךְ | **ทูตสวรรค์** (…ที่สนทนาอยู่กับข้าพเจ้า) | 1:9, 1:13, 1:14, 2:2, 2:7 (+ מַלְאָךְ אַחֵר → ทูตสวรรค์อีกองค์หนึ่ง), 4:1, 6:4, 6:5 | **WITH** |

The split is **deliberate and self-aware**. The 1:11 KD states it explicitly:

> מַלְאַךְ יְהוָה 'the angel of YHWH' = the rider among the myrtles (the patrol's leader), distinct from 'the angel speaking with me' (the interpreting angel, vv.9,13,14) — both rendered ทูต…/ทูตสวรรค์, distinguished in the footnote.

The translator is marking the **theophanic angel-of-YHWH** (who in 3:1–2 is so closely identified with YHWH that "YHWH said" follows seamlessly; who at 12:8 is the measure of the house of David being "like God") as a near-divine *envoy of the LORD* (**ทูตขององค์พระผู้เป็นเจ้า**), distinct from ordinary *heaven-messengers* (**ทูตสวรรค์**). Internally this is principled and reads cleanly.

**The conflict:** `docs/translator_decisions/malak_yhwh_2026-05.md` locks the **opposite** mapping for the corpus:

> | מַלְאַךְ יהוה | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |

i.e. the compound *keeps* สวรรค์ and the qualifier rides on ของ + the divine name; the head-noun ทูตสวรรค์ never varies. That lock was decided 2026-05-13 (tri-AI Exodus review) precisely to stop the single Hebrew lemma fragmenting into multiple Thai surfaces, and it was enforced verse-by-verse through 2 Kings (the `mal'akh-YHWH locked rendering` reference: "keep สวรรค์"). Zechariah's compound thus **drops** the very morpheme the lock protects — and does so *systematically*, across six verses, in the corpus's most concentrated angel-of-YHWH passage.

This is **mechanically invisible**: `check_key_term_consistency.py`, `check_phrase_consistency.py`, and `check_divine_names.py` are all green because none of them tracks the ทูตสวรรค์ vs ทูต distinction.

**Two coherent resolutions — Ben's call:**
- **(a) Ratify the Zechariah theophanic distinction** and amend `malak_yhwh_2026-05.md` with a carve-out: the *theophanic* מַלְאַךְ יְהוָה (Zech, and arguably the Genesis/Exodus/Judges Christophany scenes) → **ทูตขององค์พระผู้เป็นเจ้า** (no สวรรค์, marking the near-divine envoy), while ordinary divine-messenger מַלְאָךְ → **ทูตสวรรค์**. This preserves Zechariah's reading but **re-opens the closed Exodus/2 Kings lock** and would need a back-sweep for consistency.
- **(b) Normalize to the lock** — restore **สวรรค์** to all six Zechariah compounds (ทูตสวรรค์ขององค์พระผู้เป็นเจ้า), keeping a footnote for the theophanic identification. Preserves the corpus lock; loses the translator's surface distinction.

**Blocks `book-zechariah-v1`.** No change made — assessment only.

---

## 2. Tetragrammaton — Layer-1 rendering + Layer-2 footnotes — **LOCKED** (`divine_names_table_2026-05`)

יהוה → **องค์พระผู้เป็นเจ้า** at every occurrence (Layer 1). Every one of the **14 chapters** carries a correctly-typed `tetragrammaton_convention_first_occurrence` Layer-2 footnote (verified across `output/textual_variants/zechariah_01..14.json`). **No Micah-ch5 / Joel-ch3 / Lamentations-ch2-3 missing-footnote gap** — Zechariah is cleanest-tier on divine-name architecture. `check_divine_names.py` emits **zero** Zechariah warnings.

---

## 3. יהוה צְבָאוֹת → องค์พระผู้เป็นเจ้าจอมโยธา — **LOCKED** (`divine_names_table_2026-05`)

YHWH-Sabaoth is **Zechariah's signature title — 46 verses** (the densest minor-prophet concentration alongside Haggai). Uniform **องค์พระผู้เป็นเจ้าจอมโยธา**, consistent with the corpus lock and James 5:4 (`องค์พระผู้เป็นเจ้าจอมโยธา`). The intercession at 1:12 (`ข้าแต่องค์พระผู้เป็นเจ้าจอมโยธา`) and the closing universal-worship oracle (14:16–21, "the King, the LORD of Hosts") both comply.

---

## 4. Bare אֲדֹנָי (9:4) → องค์เจ้านาย; **no אֲדֹנָי יְהוִה compound** — **LOCKED**

Standalone אֲדֹנָי occurs **once** (9:4, Tyre oracle) → **องค์เจ้านาย** per corpus convention, with 3rd-person royal register (ทรงยึด / ทรงเหวี่ยง). **There is no אֲדֹנָי יְהוִה compound anywhere in Zechariah (0 occurrences).** Zechariah therefore **sidesteps the open Amos §1 question entirely** (like Nahum and Haggai) — it offers no data point for the `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` vs bare-`องค์พระผู้เป็นเจ้า` dispute.

---

## 5. הַשָּׂטָן (Zech 3:1–2) → ซาตาน — **LOCKED rendering / REVIEW** (doc-mandated article-role footnote appears absent)

This is the forward reference the **Job audit** explicitly flagged (`satan_accuser_corpus_mapping_2026-05.md`, decided 2026-05-30 on the Job external review). The doc mandates, for Zech 3:1–2:

> render הַשָּׂטָן → **ซาตาน**; add the Layer-2 **first-occurrence role footnote** (mirror Job 1:6) noting the article + role-sense `ผู้กล่าวหา / ปฏิปักษ์`. The wordplay in Zech 3:2 … should preserve the rebuke-of-the-accuser sense.

**Rendering complies:** הַשָּׂטָן → **ซาตาน** (3:1, 3:2); the article role-sense is captured in the 3:1 KD ("the accuser/adversary in his prosecutorial role"); the wordplay הַשָּׂטָן … לְשִׂטְנוֹ is kept (`ซาตาน … เพื่อกล่าวโทษท่าน`); the Jude-9 rebuke echo is footnoted at 3:2.

**The gap (REVIEW):** the ch3 reader-facing footnotes (`output/textual_variants/zechariah_03.json`) carry the **Jude-9 rebuke** `nt_citation_note` at v2 but **not** the doc-mandated **article + role-sense first-occurrence footnote** at 3:1. The article-role rationale lives only in the (non-reader-facing) translator KD. This is the same mechanically-invisible missing-footnote class as Micah ch5 / Joel ch3. **Worth Ben's confirmation** that the doc's footnote requirement is satisfied or that a `ผู้กล่าวหา / ปฏิปักษ์` role-note should be added at 3:1.

---

## 6. Messianic / NT-citation surface — **STABLE** (strongest reception-restraint witness in the corpus; lift to `committal_messianic_surface_2026-06`)

Zechariah is the **densest NT-cited OT book**, and the translation handles every flagship verse the same principled way: **natural, non-committal Thai body text + a `nt_citation_note` Layer-2 footnote + a summary that credits the NT** (`พันธสัญญาใหม่อ้างถึง…`). There is **no `คือพระคริสต์` / `นี่คือพระเมสสิยาห์` asserted as bare fact in any body text** (full 14-chapter scan) — clean of the Ezekiel §14 regression that asserted "คือพระคริสต์" as flat statement.

| Verse | Hebrew | Thai (body) | NT reception (footnoted, not asserted) |
|---|---|---|---|
| 3:8 / 6:12 | צֶמַח "Branch" | **หน่อ** (matches Jer 23:5; 33:15 lock) | Davidic-messianic title; framed in §14 footnote |
| 6:11–13 | king + priest in one | ชายผู้หนึ่ง…ปุโรหิตอยู่บนบัลลังก์ (**plain** verbs — the Branch is a man, **not** addressed with divine ทรง) | Ps 110; Heb 7, footnoted |
| 9:9 | מַלְכֵּךְ … רֹכֵב עַל־חֲמוֹר | กษัตริย์ของเจ้าเสด็จมา…เสด็จมาประทับบนหลังลา | Matt 21:5; John 12:15 |
| 11:12–13 | שְׁלֹשִׁים כָּסֶף → הַיּוֹצֵר | เงินสามสิบเหรียญ → ช่างปั้นหม้อ | Matt 27:9-10 (`nt_citation_note` present) |
| 12:10 | הִבִּיטוּ אֵלַי אֵת אֲשֶׁר־דָּקָרוּ | **มองดูเรา ผู้ที่พวกเขาได้แทง** … คร่ำครวญถึง**เขา** | John 19:37; Rev 1:7 (`nt_citation_note` present; me/him crux preserved) |
| 13:7 | הַךְ אֶת־הָרֹעֶה | จงฟันผู้เลี้ยงแกะ และฝูงแกะจะกระจัดกระจายไป | Matt 26:31; Mark 14:27 |

The 12:10 case is the strongest test: the body **faithfully preserves the MT's me/him shift** (`มองดูเรา` … `ถึงเขา`, matching אֵלַי + עָלָיו) without resolving the crux toward Christ, and routes the John 19:37 / Rev 1:7 reading to the footnote. Likewise the Branch is rendered as a *man* (`ชายผู้หนึ่ง`) with **plain** (non-`ทรง`) verbs — the committal-restraint policy applied at the lexical/register level.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/committal_messianic_surface_2026-06.md`, anchoring on Zechariah as the **maximal-density** case (denser than the Haggai anchor the prior audit proposed). The policy — *natural body, reception-framed footnote, no bare `คือพระคริสต์`* — is now uniform across Isaiah/Haggai/Habakkuk/Micah and ratified at scale here; it deserves a standalone doc before the corpus tackles Malachi 3:1 / 4:5–6 (the messenger + Elijah) and the remaining NT-citation-dense books.

---

## 7. Anthropomorphism — first-person-plain divine body parts — **LOCKED** (`divine_anthropomorphism_thai_grammar_2026-05`)

Zechariah is a **live first-person-plain §13 witness** (like Zephaniah 1:4 / Haggai). At 2:13 (Eng 2:9) מֵנִיף אֶת־יָדִי "I will wave my hand" → **กวัดแกว่งมือของเรา** — God's own hand in God's own speech stays **plain มือ**, not royal พระหัตถ์ (KD explicit). Third-person narration of God takes royal register (1:13 ตรัสตอบ; 12:8 ทรงปกป้อง). At 2:17 / 8:21 the idiom פְּנֵי יְהוָה "the face of YHWH" is rendered plain (`ต่อหน้า` / `ทูลวิงวอนขอความโปรดปราน`, no royal body-part). **No friction** — Zechariah does **not** move the open Isaiah/Jeremiah/Ezekiel §13 DECIDE; it simply confirms the codified rule.

---

## 8. Covenant-jealousy קִנְאָה (1:14; 8:2) → หวงแหน — **STABLE**

God's zealous covenant-love for Zion, first-person (เรา): 1:14 קִנֵּאתִי … קִנְאָה גְדוֹלָה → **หวงแหน…อันยิ่งใหญ่**; 8:2 קִנְאָה + חֵמָה → **ความหวงแหน / ความเร่าร้อน**. Uniform, principled, rationale at verse level. No corpus doc owed (the gloss is glossary-indexed). Worth a one-line cross-reference if a divine-emotion doc is ever lifted.

---

## 9. Versification — ZEC-2 MT/English zone — **LOCKED**

Zechariah's one divergence zone: **MT 2:1–4 = Eng/BSB 1:18–21** and **MT 2:5–17 = Eng/BSB 2:1–13**. All 17 ZEC-2 entries are in `data/versification_map.json` **and committed** (commit `16721b9e`, "data(ZEC): versification map for Zechariah 2"). Confirmed present in `git show HEAD`. This avoids the `versification map ship gotcha` (ship_chapter.sh doesn't stage the map) — the zone was committed manually. Cleanest-tier: zone registered before the audit.

---

## 10. Day of YHWH (ch14) — **STABLE** (reinforces `day_of_the_lord_leitwort` doc rec)

Chapter 14 opens `הִנֵּה יוֹם־בָּא לַיהוָה` → **ดูเถิด วันแห่งองค์พระผู้เป็นเจ้ากำลังจะมาถึง** and runs the eschatological בַּיּוֹם הַהוּא "in that day" refrain **7×** across 21 verses — the densest Day-of-YHWH cluster among the Twelve after Joel/Zephaniah. The closing theophany (14:5 כָּל־קְדֹשִׁים "all the holy ones" → **บรรดาผู้บริสุทธิ์**, the angelic host; cf. Deut 33:2, Jude 14) and the universal-worship finale (14:9 "YHWH will be king over all the earth"; 14:16 nations keeping Sukkot) all comply with the locked narrator-divine register. **Reinforces** the recommended `day_of_the_lord_leitwort_2026-06.md` doc (joint with Joel §, Amos, Obadiah, Zephaniah) — Zechariah 14 is its eschatological capstone.

---

## 11. Foreign monarch (Darius, 1:1; 7:1) — **LOCKED (N/A)**

דָּרְיָוֶשׁ appears **only in date formulas** — 1:1 (`ปีที่สองแห่งรัชกาลดาริอัส`), 7:1 (`ปีที่สี่แห่งรัชกาลกษัตริย์ดาริอัส`). Like Haggai, the foreign-monarch register thread (the open Ezra/Nehemiah/Esther/Daniel `ทรง`-or-plain question) is **not implicated** — there is no foreign-king speech or action requiring register, only chronology.

---

## 12. Textual variants — 11:13 potter/treasury + 12:10 me/him — **STABLE** (`mt_vs_lxx_textual_variant_handling_2026-05`)

Two one-/few-letter MT forks, both handled MT-primary with the alternative footnoted:
- **11:13** הַיּוֹצֵר "the potter" (vs הָאוֹצָר "the treasury") → **ช่างปั้นหม้อ**; MT-primary, the treasury variant noted; the Matt 27:9-10 reception in the `nt_citation_note`.
- **12:10** אֵלַי "look on **me**" (vs the conjectural/some-witness אֵלָיו "on **him**") → body keeps **เรา** (me) + **เขา** (him for the mourning), faithful to MT's striking shift; the John 19:37 / Rev 1:7 reading footnoted. Per §2.3 these are **non-gap** (no inclusion-bracket owed). Clean.

---

## 13. The Branch + the shepherd allegory (ch11) — **LOCKED / STABLE**

- צֶמַח "Branch" → **หน่อ** uniform (3:8, 6:12), matching the Jeremiah lock (Jer 23:5; 33:15 `หน่ออันชอบธรรม`) — LOCKED key-term continuity. The 6:12 wordplay צֶמַח שְׁמוֹ … יִצְמָח → `มีนามว่า หน่อ … จะงอกขึ้น` is preserved.
- The two-staffs sign-act (11:7) נֹעַם / חֹבְלִים → **ความโปรดปราน / ความผูกพัน**; the worthless/foolish shepherd (11:15–17, רֹעֶה אֱוִלִי → **ผู้เลี้ยงแกะที่โง่เขลา**) is rendered as straightforward judgment allegory with no Christological over-reach. STABLE narrative handling of "the hardest chapter in Zechariah" (per its own summary).

---

## 14. Infrastructure — `export_to_usfm.py` rejects ZEC — **REVIEW** (non-blocking)

As with every minor-prophet audit (Joel/Amos/…/Haggai), `scripts/export_to_usfm.py` does not yet whitelist ZEC. Non-blocking for the v1 tag; flagged for the eventual USFM-export sweep. **Registered ZEC this audit** in `build_external_review_packet.py` (BOOKS dict — was only in OT_CODES, same Micah/Zephaniah/Haggai gap) and `audit_items_to_yaml.py` (BOOK_SLUGS — was absent).

---

## Mechanical (§1) — **all green**

- 14/14 chapters: `output/check_reports/zechariah_NN_review.md` + `output/back_translations/zechariah_NN.json` + `output/textual_variants/zechariah_NN.json` ✓
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** ✓
- `check_phrase_consistency.py`: **0 violations across 38 locks** ✓
- `check_divine_names.py`: **0 Zechariah warnings** ✓
- ZEC-2 versification zone registered + committed (`16721b9e`) ✓
- `git status output/`: clean (only re-ran-check artifacts: `divine_names.md`, `phrase_consistency.md`) ✓

---

## Flagged for Ben's attention

### A. מַלְאַךְ יְהוָה drops สวรรค์ — **DECIDE** (§1, blocks v1)
The compound angel-of-YHWH is rendered **ทูตขององค์พระผู้เป็นเจ้า** (no สวรรค์) across 1:11/1:12/3:1/3:5/3:6/12:8 — a deliberate theophanic distinction that **inverts** the `malak_yhwh_2026-05` lock (which keeps สวรรค์ and was enforced through 2 Kings). Mechanically invisible. Ratify-and-amend-the-doc (option a) or normalize-to-the-lock (option b).

### B. Satan article-role footnote at 3:1 — **REVIEW** (§5)
`satan_accuser_corpus_mapping_2026-05` mandates a first-occurrence article + role-sense (`ผู้กล่าวหา / ปฏิปักษ์`) footnote at Zech 3:1; the ch3 footnotes carry the Jude-9 note but not that one. Confirm satisfied or add at 3:1.

### C. Messianic/NT-citation policy ratification — **STABLE → lift to doc** (§6)
Zechariah ratifies the committal-restraint policy at maximal density (Branch, 9:9, 11:13, 12:10, 13:7) with zero bare-`คือพระคริสต์`. Lift to `committal_messianic_surface_2026-06.md` (Zechariah as anchor, superseding the Haggai-anchor proposal).

### D. New corpus docs recommended
1. **`committal_messianic_surface_2026-06.md`** (§6) — anchor Zechariah; the Isaiah-§0 / Ezk-§14 policy still has no standalone doc.
2. **`day_of_the_lord_leitwort_2026-06.md`** (§10) — Zechariah 14 is the eschatological capstone joining Joel/Amos/Obadiah/Zephaniah.
3. **(contingent on §1a)** `malak_yhwh_2026-05.md` amendment — theophanic-vs-ordinary מַלְאָךְ carve-out.

### E. External AI review (§3) — packet built
See `external_review_items_ZEC.md` + `external_review_packet_ZEC_2026-06-27.md`. Four items: mal'akh-YHWH สวรรค์ drop (A); messianic reception ratification + 12:10 me/him crux (B); satan article-role footnote gap (C); 11:13 potter/treasury + 12:10 MT-primary textual choices (D).

---

## Recommendation

**Zechariah ships in excellent corpus-hygiene shape** — cleanest-tier divine-name architecture (L1+L2 footnotes all 14 chapters, zero divine-name warnings), versification zone committed, no Adonai-YHWH compound to re-open Amos §1, and the **strongest messianic-reception-discipline witness in the entire corpus** at the densest NT-citation surface in the OT.

The one thing that blocks `book-zechariah-v1` is **§1**: the systematic, self-aware, but lock-violating **ทูตขององค์พระผู้เป็นเจ้า** (no สวรรค์) rendering of מַלְאַךְ יְהוָה. It is the corpus's first real test of whether the theophanic angel-of-YHWH should be surfaced distinctly from ordinary heaven-messengers — a question the Exodus-era `malak_yhwh_2026-05` lock answered "no, keep them uniform." Ben should decide before tagging.

Tag `book-zechariah-v1` after: (1) Ben's decision on **§A** (mal'akh สวรรค์); (2) Ben's confirmation on **§B** (satan footnote) and **§C** (messianic-policy lift); (3) the two recommended docs written (+ the malak amendment if §A resolves to ratify); (4) the external AI sanity-check returned.
