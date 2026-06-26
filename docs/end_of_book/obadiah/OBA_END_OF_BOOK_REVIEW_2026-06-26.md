# Obadiah — End-of-Book Review

**Date:** 2026-06-26
**Scope:** The single chapter of Obadiah (21 verses; standard versification — Obadiah has **no** MT/English divergence zone); `glossary.json`; `docs/translator_decisions/` corpus. **The shortest book in the Old Testament** and the fourth Book-of-the-Twelve title processed in the corpus (after Hosea, Joel, Amos). Two cross-cutting facts dominate the review: (1) Obadiah opens with the **אֲדֹנָי יְהוִה "Lord GOD"** compound (1:1) — the exact form whose *surfacing* in Amos is the headline DECIDE blocking `book-amos-v1` — and Obadiah renders it **bare** `องค์พระผู้เป็นเจ้า`, conforming to the locked rule and Amos's recommended path (a); and (2) Obadiah 1–9 is a **near-doublet of Jeremiah 49:7–22**, the corpus's other Edom oracle, which the two books translate **independently**.
**Trigger:** OBA 1 shipped (last/only chapter, commit `b5c1ec65`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **9 cross-cutting items reviewed.** Mechanical gates (§1 of checklist) pass: the single chapter has a green per-chapter report + back-translation + translation; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks, 30,323 verses scanned); per-chapter `check_divine_names` clean (zero warnings — no false positive of the Amos 4:1 / Daniel 12:8 class); `output/textual_variants/obadiah_01.json` present (Layer-2 YHWH first-occurrence footnote **and** a structure/summary footnote). `git status output/` for Obadiah files is clean (the four `*amos*`/`divine_names.md` entries in `git status` are pre-existing Amos-audit artifacts, untouched here).

- **0 items flagged DECIDE.** Nothing in Obadiah itself blocks `book-obadiah-v1`. The one item that *could* re-open — the אֲדֹנָי יְהוִה compound at 1:1 — is already rendered in the **locked bare form**, so its only exposure is downstream of the **open Amos §1 DECIDE** (see §1 below): if Ben resolves Amos toward path (a) "normalize to bare," Obadiah is already correct; only an Amos path-(b) ratification would force Obadiah back open. That is an Amos decision, not an Obadiah one.

- **3 items flagged REVIEW** (worth Ben's confirmation):
  - **§1 — אֲדֹנָי יְהוִה "Lord GOD" at 1:1 rendered bare `องค์พระผู้เป็นเจ้า`.** Obadiah is the **first minor-prophet datum after the Amos/Jeremiah bare-normalization commits** (`c25f2dc2`, `2118e3a6`) and it renders the compound bare — i.e. it *complies* with the locked `divine_names_table_2026-05` rule and Amos's recommended path (a), and the chapter footnote discloses the compound collapse explicitly. **Confirm** the bare rendering is the intended corpus surface (it is contingent on the still-open Amos §1 DECIDE). See §1.
  - **§2 — Obadiah 1–9 ∥ Jeremiah 49:7–22: the two Edom oracles are translated independently.** The Thai surfaces **correctly preserve** the real MT difference (`שָׁמַעְנוּ` "we have heard," Obad 1 → `เรา…ได้ยิน` vs `שָׁמַעְתִּי` "I have heard," Jer 49:14 → `ข้าพเจ้าได้ยิน`) but **drift incidentally** on phrases that are *identical* in Hebrew (`זְדוֹן לִבְּךָ הִשִּׁיאֶךָ` → Obad `ความเย่อหยิ่งในใจ` / Jer `ความหยิ่งยโสในใจ`; `שֹׁכְנִי בְחַגְוֵי־סֶלַע` → Obad `ซอกหินผา` / Jer `ซอกหิน`). Confirm the policy: parallel/doublet oracle material translated independently from each MT context (preserving genuine textual differences) rather than lexically harmonized. See §2.
  - **§9 — `export_to_usfm.py` still rejects `OBA`** ("Unknown book code: OBA → nothing exported"), the recurring OT book-code gotcha (same open state as ISA/EZK/LAM/JOL/AMO). Not a translation issue and not a tag blocker; OBA **is** already registered in `build_external_review_packet.py`, and this audit registers it in `audit_items_to_yaml.py`. See §9.

- **STABLE-but-undocumented pattern recommending doc-lift:**
  - **§3 — `יוֹם יְהוָה` "Day of the LORD" (1:15)** → **`วันแห่งองค์พระผู้เป็นเจ้า`**, identical to Joel and Amos. Obadiah is the **third OT witness** to the leitwort and **universalizes** it (`קָרוֹב יוֹם־יְהוָה עַל־כָּל־הַגּוֹיִם` "the Day of the LORD is near upon **all the nations**"). This **reinforces the `day_of_the_lord_leitwort_2026-06.md` doc** recommended at both the Joel and Amos audits — still un-written (Joel and Amos are also un-tagged). Write the doc once, covering Joel (institution), Amos (reversal), and Obadiah (universalization), as the canonical reference ahead of Zephaniah/Zechariah/Malachi.

- **External AI review (§3) packet:** focused 2-item packet — the אֲדֹנָי יְהוִה bare/marked corpus tension (§1, in deliberate contrast with the open Amos blocker) and the parallel-oracle harmonization question (§2). The infra item (§9) and the STABLE doc-lift (§3) are not externally reviewable translation questions and are excluded from the packet, matching the Amos packet's scoping.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. אֲדֹנָי יְהוִה "Lord GOD" at 1:1 — rendered BARE, conforming to the locked rule (in contrast with Amos) — **REVIEW**

Obadiah's superscription is the corpus's *next* occurrence of the divine compound after Amos, and it is the live test of whether the bare-collapse rule held once Amos surfaced the inconsistency.

**The verse:**

- **HEB (1:1):** `כֹּה־אָמַר אֲדֹנָי יְהוִה לֶאֱדוֹם … שְׁמוּעָה שָׁמַעְנוּ מֵאֵת יְהוָה`
- **BSB:** "This is what the Lord GOD says about Edom… We have heard a message from the LORD"
- **TH (Obadiah):** `องค์พระผู้เป็นเจ้าตรัสเกี่ยวกับเอโดมดังนี้ว่า … เราได้ยินข่าวจากองค์พระผู้เป็นเจ้า`

The first divine title is the compound `אֲדֹנָי יְהוִה`, rendered **bare** `องค์พระผู้เป็นเจ้า` (Adonai collapsed) — and the second, bare `יְהוָה` in the same verse, takes the identical surface. This is exactly the **locked `divine_names_table_2026-05` row 22** ("Compound collapses to single Thai rendering") and is what Ezekiel (217×), Isaiah (~30×), and Jeremiah do throughout. The `obadiah_01` KD records the underlying compound; `output/textual_variants/obadiah_01.json` v.1 footnote discloses it to the reader: *"ข้อ 1 ปรากฏรูป אֲדֹנָי יְהוִה … ซึ่งฉบับเอเรโมสแปลรวบเป็น 'องค์พระผู้เป็นเจ้า' เช่นเดียวกับ יהוה (ตามแบบแผนทั่วทั้งฉบับ)."*

**Why REVIEW, not LOCKED:** the rendering is correct under the current lock, but its standing is **contingent on the open Amos §1 DECIDE.** Amos surfaces the same compound as `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` in 20 verses; the Amos audit recommends **path (a)** — normalize Amos *down* to the bare form Obadiah already uses. If Ben ratifies path (a), Obadiah needs **no change** and this item becomes LOCKED. Only an Amos **path (b)** (ratify the marked surface, write `adonai_yhwh_2026-06.md`, re-open Ezekiel/Isaiah/Jeremiah) would force Obadiah's single occurrence to be re-marked too. So Obadiah is a **clean, conforming data point that strengthens the case for path (a)** — it shows the bare rule applying naturally at a fresh book boundary, with no phantom-doc citation (Obadiah's KD cites the real `divine_names_table_2026-05`, **not** the non-existent `adonai_yhwh_2026-05` that Amos's KDs cite). **Confirm** the bare rendering stands; no translation change proposed. **Severity: GREEN (compliant; flagged only for the cross-book dependency).**

---

## 2. Obadiah 1–9 ∥ Jeremiah 49:7–22 — the two Edom oracles translated independently — **REVIEW**

Obadiah's opening doom-section is a near-doublet of the Edom oracle in Jeremiah 49, the corpus's only other extended prophecy against Edom. Both ship; the question is whether the shared material should read identically in Thai or be translated independently from each MT context. **Current practice = independent translation**, which has a real upside and a real cost.

**The upside — genuine textual differences are preserved.** The MT itself differs between the two, and the Thai faithfully reflects it:

| | Obadiah (MT → TH) | Jeremiah 49 (MT → TH) |
|---|---|---|
| "heard a report" | 1:1 `שָׁמַעְנוּ` (1cp) → **เรา**ได้ยินข่าว | 49:14 `שָׁמַעְתִּי` (1cs) → **ข้าพเจ้า**ได้ยินข่าว |
| envoy sent | 1:1 "ท่ามกลางประชาชาติ … จงลุกขึ้นทำสงครามกับมัน" | 49:14 "ยังบรรดาประชาชาติ … จงรวมตัวกันยกไปต่อสู้เอโดม" |

The we/I (`שָׁמַעְנוּ`/`שָׁמַעְתִּי`) difference is a true MT variant and the independent renderings capture it — harmonizing would *erase* a real distinction.

**The cost — incidental lexical drift on phrases identical in Hebrew:**

| Hebrew (identical in both) | Obadiah TH | Jeremiah 49 TH |
|---|---|---|
| `זְדוֹן לִבְּךָ הִשִּׁיאֶךָ` (Obad 3 / Jer 49:16) | ความ**เย่อหยิ่ง**ในใจของเจ้าได้หลอกลวงเจ้า | ความ**หยิ่งยโส**ในใจของเจ้าได้หลอกลวงเจ้า |
| `שֹׁכְנִי בְחַגְוֵי־סֶלַע` (Obad 3 / Jer 49:16) | ผู้อาศัยอยู่ใน**ซอกหินผา** | ผู้อาศัยอยู่ตาม**ซอกหิน** |
| `מִשָּׁם אוֹרִידְךָ נְאֻם־יְהוָה` (Obad 4 / Jer 49:16) | เราก็จะดึงเจ้าลงมาจากที่นั่น องค์พระผู้เป็นเจ้า**ตรัสดังนี้** | เราก็จะดึงเจ้าลงมาจากที่นั่น องค์พระผู้เป็นเจ้า**ตรัสไว้ดังนี้** |

Here the Hebrew is word-for-word identical but the Thai diverges on synonyms (`เย่อหยิ่ง`/`หยิ่งยโส`, `ซอกหินผา`/`ซอกหิน`, `ตรัสดังนี้`/`ตรัสไว้ดังนี้`). No mechanical check catches this because the two passages are in different books and neither phrase is a registered phrase-lock. A reader cross-referencing the two Edom oracles sees gratuitous variation where the source is the same.

**Why REVIEW:** the independent-translation policy is **defensible** (it is how every doublet in the corpus has been handled — Ps 14∥53, Isa 2∥Mic 4, 2 Kgs 18–20∥Isa 36–39, Isa 37∥2 Kgs 19), and harmonizing carries its own risk (flattening the `שָׁמַעְנוּ`/`שָׁמַעְתִּי` distinction). But Obadiah∥Jeremiah-49 is the **tightest and most extended doublet yet** to cross an end-of-book boundary, so it is the natural place to **ratify the policy and decide whether a corpus doc is owed.** Confirm: parallel/doublet passages are translated independently from each MT context (textual differences preserved, incidental synonym-drift accepted), with **no retroactive harmonization** of Obadiah to Jeremiah 49. If Ben wants the *identical*-Hebrew phrases harmonized, that is a targeted Obadiah-or-Jeremiah rev, not a tag blocker. **Recommend a short `parallel_passage_doublets_2026-06.md` doc** to fix the policy for the doublets still ahead (Mic 4∥Isa 2 is imminent in the Twelve). **Severity: YELLOW (policy ratification; current state defensible).**

---

## 3. `יוֹם יְהוָה` "Day of the LORD" (1:15) — **STABLE (reinforces the Joel/Amos doc recommendation)**

Rendered **`วันแห่งองค์พระผู้เป็นเจ้า`** — identical to Joel and Amos — at the book's structural pivot (1:15), where the oracle turns from Edom to the nations. Obadiah is the **third OT witness** to the leitwort and contributes its **universalization**: `כִּי־קָרוֹב יוֹם־יְהוָה עַל־כָּל־הַגּוֹיִם` → `เพราะวันแห่งองค์พระผู้เป็นเจ้าใกล้เข้ามาแล้วเหนือประชาชาติทั้งปวง` ("…near **upon all the nations**"), paired with the lex-talionis principle `כַּאֲשֶׁר עָשִׂיתָ יֵעָשֶׂה לָּךְ` → `เจ้าได้กระทำสิ่งใด สิ่งนั้นก็จะถูกกระทำต่อเจ้า`. The form matches the `glossary.json` ἡμέρα κυρίου entry and the already-shipped Acts 2:20 / 1 Thess 5:2 / 2 Pet 3:10 surfaces. **This directly reinforces the `day_of_the_lord_leitwort_2026-06.md` doc recommended at the Joel audit (§5) and the Amos audit (§5) — still un-written.** The doc should now be authored once, covering Joel (institution), Amos (reversal to "darkness, not light"), and Obadiah (universalization to "all the nations"), before Zephaniah/Zechariah/Malachi. **Severity: GREEN (consistency); doc-lift recommended jointly with Joel + Amos.**

---

## 4. Divine first-person anthropomorphism (1:4, 1:16) — **LOCKED**

- **1:4 `מִשָּׁם אוֹרִידְךָ` "from there I will bring you down"** → `เราก็จะดึงเจ้าลงมาจากที่นั่น` — first-person divine action, plain register.
- **1:16 `הַר קָדְשִׁי` "my holy mountain"** → `ภูเขาบริสุทธิ์ของเรา` — first-person divine possessive, plain (no Rachasap honorific on the 1st-person form).

Both are **compliant with `divine_anthropomorphism_thai_grammar_2026-05.md`** (first-person divine speech → plain; the honorific/Rachasap layer attaches to third-person reference, of which Obadiah has none). Obadiah is a **clean, non-friction data point** for the open cross-corpus first-person-plain DECIDE (Isaiah/Jeremiah/Ezekiel/Hosea/Amos) — it adds another conforming instance but does **not** move the open item (no third-person body-part or siege-verb cases). **LOCKED** ✓. **Severity: GREEN.**

---

## 5. Divine names: Tetragrammaton + the Layer-2 footnote — **LOCKED**

- **`יְהוָה` Tetragrammaton → `องค์พระผู้เป็นเจ้า`** (Layer 1) in every occurrence — 1:1 (×2, incl. the compound), 1:4, 1:8, 1:15, 1:18, 1:21 — each KD citing `divine_names_table_2026-05`. The `נְאֻם־יְהוָה` "declares the LORD" (1:4, 1:8) and `כִּי יְהוָה דִּבֵּר` "for the LORD has spoken" (1:18) formulas are uniform, and the climactic `וְהָיְתָה לַיהוָה הַמְּלוּכָה` → `ราชอาณาจักรนั้นจะเป็นขององค์พระผู้เป็นเจ้า` (1:21) lands cleanly.
- **Layer 2 present and correct.** `output/textual_variants/obadiah_01.json` carries the per-chapter first-occurrence footnote (`tetragrammaton_convention_first_occurrence`), enumerating every YHWH verse and disclosing the 1:1 `אֲדֹנָי יְהוִה` compound collapse. This is the correct footnote **type** — Obadiah does **not** repeat the Joel ch.3 `nt_citation_note`-vs-`tetragrammaton` type mismatch that produced a `check_divine_names` WARN there. **The Obadiah divine-names check is clean with zero warnings.**

**LOCKED** ✓. **Severity: GREEN.**

---

## 6. Obadiah 21 — "the kingdom shall be the LORD's" + מוֹשִׁעִים "deliverers" — **LOCKED (no messianic over-commit)**

The book's triumphant close: `וְעָלוּ מוֹשִׁעִים בְּהַר צִיּוֹן … וְהָיְתָה לַיהוָה הַמְּלוּכָה`.

- **`מוֹשִׁעִים` "deliverers/saviors"** → `บรรดาผู้ช่วยให้รอด` — rendered as the **plural** human deliverers who ascend Zion (the šōphᵉṭîm/môšîaʿ "judges-deliverer" pattern, cf. `judges_shaphat_deliverer_cycle_2026-05.md`), not as a singular messianic title. Correct restraint — no over-reading toward Christ.
- **`וְהָיְתָה לַיהוָה הַמְּלוּכָה`** → `ราชอาณาจักรนั้นจะเป็นขององค์พระผู้เป็นเจ้า` — the kingdom belongs to YHWH, rendered **plainly**; the thematic NT link to Rev 11:15 ("the kingdom of the world has become…") is carried in the verse `thai_summary` and the structure footnote, **not** asserted in the rendered text. This is clean of the **§0 messianic-regression** flagged at Ezekiel §14 (no bare "คือพระคริสต์" assertion) and consistent with the committal-messianic-surface policy ratified at Isaiah and applied at Joel/Amos. **LOCKED** ✓. **Severity: GREEN.**

---

## 7. Proper names — Edom / Esau / Jacob / Teman / Sepharad / Zarephath — **LOCKED**

`אֱדוֹם` → เอโดม, `עֵשָׂו` → เอซาว, `יַעֲקֹב` → ยาโคบ, `תֵּימָן` → เทมาน, `הַר עֵשָׂו` → ภูเขาเอซาว, `הַנֶּגֶב` → เนเกบ, `הַשְּׁפֵלָה` → ที่ราบเชเฟลาห์, `צָרְפַת` → ศาเรฟัท, `סְפָרַד` → เสฟาราด — all per `proper_names_and_transliteration_2026-05.md`. The Esau/Jacob twin-brother frame (1:6, 1:10, 1:18) is consistently surfaced, anchoring the book's fratricide theme (Gen 25/36 cross-reference in the notes). **LOCKED** ✓. **Severity: GREEN.**

---

## 8. Hapax legomena (1:6, 1:9, 1:20) — **STABLE**

Obadiah's three notable rare words are each glossed in `notes`: `מַצְפֻּנָיו` "his hidden treasures" (1:6, hapax) → `ทรัพย์สมบัติที่ซ่อนไว้`; `קֶטֶל` "slaughter" (1:9, hapax) → `การเข่นฆ่า`; `סְפָרַד` "Sepharad" (1:20, hapax place-name of uncertain location, later Jewish usage = Spain) → `เสฟาราด` + note. Each is handled at verse level with the lexical uncertainty disclosed. No corpus-level issue. **STABLE** ✓. **Severity: GREEN.**

---

## 9. Infrastructure — `export_to_usfm.py` rejects `OBA` — **REVIEW (infra, non-blocking)**

`python3 scripts/export_to_usfm.py --book OBA` → `✗ Unknown book code: OBA` / `⚠ OBA: no translated chapters found — nothing exported`. The recurring OT book-code gotcha (same open state as ISA/EZK/LAM/JOL/AMO — the export script's internal code table lags the YAML/packet tables). It blocks Paratext (.SFM) export of Obadiah but is **not** a translation issue and **not** a v1-tag blocker. **OBA is already registered** in `build_external_review_packet.py` (BOOKS list, line 112), and this audit **registers OBA in `audit_items_to_yaml.py`** (BOOK_SLUGS + the verse-ref regex). `export_to_usfm.py` should be registered in the same pass when the maintainer next touches it. **Severity: YELLOW (infra, non-blocking).**

---

## Items reviewed that need no action

- **`חָמָס` "violence" against the brother (1:10)** → `ความรุนแรง` — the book's moral core (`מֵחֲמַס אָחִיךָ יַעֲקֹב`), rendered plainly and consistently with the corpus `חָמָס` surface. ✓.
- **The cup-of-wrath / drinking imagery (1:16)** `כַּאֲשֶׁר שְׁתִיתֶם … יִשְׁתּוּ כָל־הַגּוֹיִם תָּמִיד` → `พวกเจ้าได้ดื่ม … ประชาชาติทั้งปวงก็จะดื่มอยู่เรื่อยไป` — the talionic cup metaphor carried without explanatory intrusion; KD discloses the "cup of judgment" sense. ✓.
- **Versification** — Obadiah is a single 21-verse chapter with no MT/English divergence zone; `check_versification_anchor` clean. No versification-map entry owed. ✓.

---

## Recommended new translator-decisions docs

1. **`day_of_the_lord_leitwort_2026-06.md`** (§3) — the `יוֹם יְהוָה` → `วันแห่งองค์พระผู้เป็นเจ้า` lock, now covering **Joel** (institution), **Amos** (reversal), and **Obadiah** (universalization to "all the nations"). Recommended at the Joel and Amos audits; Obadiah makes it triply owed. Write once, before Zephaniah/Zechariah/Malachi.
2. **`parallel_passage_doublets_2026-06.md`** (§2) — the policy that doublet/parallel passages (Obad 1–9 ∥ Jer 49:7–22; Ps 14∥53; Isa 2∥Mic 4; 2 Kgs 18–20∥Isa 36–39) are translated **independently** from each MT context — genuine textual differences preserved, incidental synonym-drift on identical-Hebrew phrases accepted (or, if Ben prefers, harmonized by targeted rev). Forward-protects Mic 4∥Isa 2, imminent in the Twelve.

(Both are STABLE-confirm / policy-ratification doc-lifts; per the checklist, this audit recommends but does not author them.)

## Checklist for Ben before tagging `book-obadiah-v1`

- [ ] **§1 REVIEW** — confirm the 1:1 `אֲדֹנָי יְהוִה` → bare `องค์พระผู้เป็นเจ้า` rendering stands (contingent on resolving the open **Amos §1 DECIDE** toward path (a); Obadiah is already correct under path (a)).
- [ ] **§2 REVIEW** — ratify "doublet passages translated independently per MT context" for Obad 1–9 ∥ Jer 49:7–22 (or request targeted harmonization of the identical-Hebrew phrases); approve (or decline) `parallel_passage_doublets_2026-06.md`.
- [ ] **§9 REVIEW** — register `OBA` in `export_to_usfm.py` (infra; non-blocking).
- [ ] **§3** — approve (or decline) the `day_of_the_lord_leitwort_2026-06.md` doc (now owed jointly by Joel + Amos + Obadiah).
- [ ] Then: `bash scripts/ship_book.sh OBA` (lock-the-book ship + tag).
