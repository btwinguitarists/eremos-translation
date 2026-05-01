# 2 Thessalonians — End-of-Book Review

**Date:** 2026-04-30
**Scope:** All 3 chapters (47 verses; verse-level `key_decisions` throughout); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** 2TH 3 shipped (commit `dcdcb5d` thai-bible-ai / `81b55ef` EremosVercel2 bundle); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2) + External AI cross-review (§3 — Gemini, response logged 2026-04-30). No translation changes prescribed beyond one spot-revision at 2:9 (applied in commit `17b5dcb`).

## Summary

- **8 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 3/3 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 violations) across the now-134-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status` clean.
- **2 Thessalonians is the THIRD FULL Pauline epistle the project has shipped** (after Galatians and 1 Thessalonians; all 2026-04). Composed shortly after 1 Thess (~AD 51) to the same audience to correct eschatological misunderstanding. The audit confirms strong CONTINUITY with 1 Thess on inherited Pauline-vocabulary set (παρουσία, ἐκκλησία, ἀδελφοί, εὐχαριστέω, πατήρ register split, ἁγιασμός, ὑπομονή, πίστις/πιστός pun) and **introduces several FIRST-OCCURRING corpus-cross-cutting items**: παρουσία applied to a NON-Christ subject (the lawless one) at 2:9; ἀνομία/ἄνομος cluster as the densest in the corpus; ἀποστασία (rare-NT, only here + Acts 21:21); the "restrainer" gender-shift at 2:6-7; the famous work-or-don't-eat dictum at 3:10; Paul's hand-signature anti-forgery at 3:17.
- **External AI cross-review (§3) complete.** Gemini reviewed all 8 items and returned **8 / 8 FINE** with one concrete spot-revision recommended at 2:9 (`การมา` → `การมาถึง`, applied). Verbatim response at `external_review_response_GEMINI_2026-04-30.md`.
- **5 corpus-level patterns flagged STABLE-but-undocumented**, with translator-decision docs recommended (non-blocking; can write JIT before relevant downstream books). All 5 are listed at the bottom of this doc.
- **2 spot-revisions to ALREADY-SHIPPED 1 Thess chapters applied during this audit cycle** (cross-book grooming triggered by the 2TH end-of-book review):
  - 1 Th 3:13 ἁγίων: `วิสุทธิชนทุกคน` → `บรรดาผู้บริสุทธิ์ทุกคน` (preserves angels-vs-saints ambiguity)
  - 1 Th 4:17 ἀπάντησις: `เพื่อพบกับ` → `เพื่อต้อนรับ` (restores Hellenistic civic-reception sense)
- **3 reviewer-form questions queued at eremosapp.com/review:** `B_GAL_pistis_christou` (already in pipeline), `B_GAL_stoicheia_principles` (already in pipeline), and **`B_1TH4_skeuos_body_or_wife`** (new — added during this audit cycle for the body-vs-wife crux at 1 Th 4:4).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — defensible, worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. παρουσία register split — Christ (royal) vs lawless one (plain) — **STABLE (corpus-doc recommended)**

First Pauline-corpus instance of παρουσία applied to a NON-Christ subject (2 Th 2:9 παρουσία τοῦ ἀνόμου). The translator preserves the Christ→**การเสด็จมา** (royal เสด็จ) lock from 1 Thess and uses NEUTRAL **การมาถึง** (revised 2026-04-30 from `การมา` per Gemini Item A) for the lawless-one's parousia.

| Verse | Subject | Greek | Thai |
|---|---|---|---|
| 2:1 | Christ | παρουσία τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ | **การเสด็จมา**ของพระเยซูคริสต์... |
| 2:8 | Christ | τῇ ἐπιφανείᾳ τῆς παρουσίας αὐτοῦ | **การปรากฏแห่งการเสด็จมา**ของพระองค์ |
| 2:9 | lawless one | οὗ ἐστιν ἡ παρουσία | **การมาถึง**ของเขา |

**Gemini Item A:** FINE. **Recommend STABLE → corpus doc** `docs/translator_decisions/parousia_register_2026-04.md` to formalize the Christ-เสด็จมา / adversary-มาถึง split, citing 2 Th 2:9 as the locking precedent. Will recur for 1 Cor 15:23, 16:17; 2 Cor 7:6-7; 10:10; Phil 1:26, 2:12; 1 Th 2:19, 3:13, 4:15, 5:23.

## 2. ἀνομία / ἄνομος / ἄνθρωπος τῆς ἀνομίας — densest "lawlessness" cluster in the corpus — **STABLE**

The translator's renderings: ἀνομία → ความอธรรม; ἄνομος (substantival) → คนอธรรม; ἄνθρωπος τῆς ἀνομίας → คนแห่งความอธรรม. Consistent with corpus precedent at Acts 2:23 (ἀνόμων → คนอธรรม) and Luke 22:37 (ἀνόμων → ผู้ล่วงละเมิดกฎ).

**TEXTUAL VARIANT at 2:3** (ἀνομίας vs ἁμαρτίας): SBLGNT/NA28 read ἀνομίας; TR/Byz/KJV read ἁμαρτίας. Following SBLGNT per RULES §0. ESV/NIV/CSB/BSB all align.

**Gemini Item B:** FINE. Lock as corpus default. Will recur in Rom 4:7 (LXX Ps 32 quotation); 6:19; 2 Cor 6:14; 1 Tim 1:9; Tit 2:14; Heb 1:9, 8:12, 10:17; 1 John 3:4 (the Johannine ἀνομία = ἁμαρτία identification verse).

## 3. ἀποστασία at 2:3 — religious-apostasy reading locked — **STABLE**

Rare NT term (only here + Acts 21:21). Translator chose **การละทิ้งความเชื่อ** ("abandonment of faith") committing to the religious-apostasy reading over political-rebellion or cosmic-rebellion alternatives.

**Gemini Item C:** FINE. Lock for religious-apostasy contexts. The article ἡ ἀποστασία ("THE apostasy") supports specific-eschatological-event reading consistent with Pauline-Thessalonian prior teaching (cf. v.5).

## 4. The restrainer (τὸ κατέχον / ὁ κατέχων) at 2:6-7 — gender-shift preservation — **STABLE**

Translator preserves the Greek MASCULINE/NEUTER shift in Thai: NEUTER **สิ่งใด** (v.6, "what-thing restrains") + MASCULINE **ผู้ที่** (v.7, "the one-who restrains"). Identity left ambiguous (Roman empire / Holy Spirit / archangel / gospel mission / personal restrainer) per patristic + modern divergent readings.

**Gemini Item D:** FINE. Lock the gender-split preservation.

## 5. εἵλατο + ἀπαρχήν at 2:13 — rare-verb + textual variant — **STABLE**

εἵλατο (αἱρέω middle, 3× in NT) translated as **ทรงเลือก** (royal divine-election verb). Textual variant: SBLGNT ἀπαρχήν (firstfruits) vs TR/Byz ἀπ' ἀρχῆς (from the beginning). Following SBLGNT → **ผลแรก** (firstfruits).

**Gemini Item E:** FINE. **Recommend lock ผลแรก for ἀπαρχή corpus-wide.** Will recur at Rom 8:23, 11:16, 16:5; 1 Cor 15:20, 23, 16:15; Jas 1:18; Rev 14:4. Recommend corpus doc `docs/translator_decisions/aparche_firstfruits_2026-04.md`.

## 6. παράδοσις — Synoptic-vs-Pauline split — **STABLE (corpus-doc recommended)**

Translator splits παράδοσις by Pauline-positive (apostolic teaching → **คำสอนที่ส่งทอดมา**) vs Synoptic-negative (Pharisaic tradition → **ธรรมเนียม**). 2 Th 2:15, 3:6 use the Pauline-positive form.

**Gemini Item F:** FINE — with explicit caveat that **Col 2:8** (negative — pagan-philosophical-tradition) should use **ธรรมเนียม**. Recommend corpus doc `docs/translator_decisions/paradosis_synoptic_pauline_split_2026-04.md` capturing the Col 2:8 caveat.

## 7. σημεῖον at 3:17 — contextual variant from corpus default — **STABLE (corpus-doc recommended)**

Corpus default is σημεῖον → **หมายสำคัญ** (miraculous-sign sense, locked across the gospels + Acts). At 2 Th 3:17 the verse uses σημεῖον in the AUTHENTICATING-MARK sense (Paul's hand-signature). Translator rendered **เครื่องหมาย** as a documented contextual variant per RULES §4.

**Gemini Item G:** FINE. **Specifically requested:** corpus doc disambiguating the THREE σημεῖον senses (miracle-sign / authentication-mark / signal). Recommend `docs/translator_decisions/semeion_three_senses_2026-04.md`. Affects future 1 Cor 1:22, 14:22; Rev's frequent σημεῖον; Heb 2:4.

## 8. κύριος τῆς εἰρήνης at 3:16 — unique non-Pauline formula — **STABLE**

Standard Pauline formula is **θεὸς τῆς εἰρήνης** ("God of peace"). 2 Th 3:16 is THE ONLY use of **κύριος τῆς εἰρήνης** ("Lord of peace") — applying the Father-formula-form to Christ. High-Christology. Translator: **องค์พระผู้เป็นเจ้าแห่งสันติสุข** preserves the formula-shape.

**Gemini Item H:** FINE. Lock as formulaic.

---

## Cross-book applied during this audit cycle

Two spot-revisions to already-shipped 1 Thessalonians chapters (triggered by the corpus-wide nature of the issues raised):

### 1 Th 3:13 ἁγίων — preserve angels-vs-saints ambiguity

Old: `พร้อมกับวิสุทธิชนทุกคนของพระองค์` (วิสุทธิชน in modern Thai narrows to "human saints/believers")
New: `พร้อมกับบรรดาผู้บริสุทธิ์ทุกคนของพระองค์` (more literal "his holy ones," preserves the angels-OR-believers ambiguity Greek ἅγιοι has)

### 1 Th 4:17 ἀπάντησις — restore civic-reception sense

Old: `เพื่อพบกับองค์พระผู้เป็นเจ้า` ("to meet with the Lord" — flat)
New: `เพื่อต้อนรับองค์พระผู้เป็นเจ้า` ("to welcome the Lord" — restores the Hellenistic-technical civic-reception "go-out-to-welcome-the-arriving-king" sense)

Both shipped via PR #408 (commit `5ec4cc1` on EremosVercel2/main); source commits `de0f124` + `d1691c0` on thai-bible-ai/main.

---

## Reviewer-form pipeline state

3 questions live at eremosapp.com/review (waiting for native-speaker / pastoral / theological reviewers to weigh in):

| YAML | Topic | Status |
|---|---|---|
| `B_GAL_pistis_christou.yml` | πίστις Χριστοῦ objective vs subjective genitive | Pre-existing |
| `B_GAL_stoicheia_principles.yml` | στοιχεῖα at Gal 4:3, 4:9 = principles vs spirits | Pre-existing |
| `B_1TH4_skeuos_body_or_wife.yml` | σκεῦος at 1 Th 4:4 = body vs wife | **Added during 2TH audit cycle** (PR #409) |

---

## TODO — corpus decision docs (non-blocking, JIT before relevant books)

Gemini specifically called for the following 5 docs to formalize the locked decisions surfaced in this audit:

1. `docs/translator_decisions/parousia_register_2026-04.md` — Christ-เสด็จมา / adversary-มาถึง split. **Trigger book:** any (active in 2TH 2:9 already; will recur).
2. `docs/translator_decisions/anomia_lawlessness_2026-04.md` — ἀนοมίา/ἄνομος cluster lock. **Trigger book:** Romans 4:7+ (LXX Ps 32 quotation), 6:19.
3. `docs/translator_decisions/aparche_firstfruits_2026-04.md` — ἀπαρχή → ผลแรก lock. **Trigger book:** Romans 8:23 / 11:16, 1 Corinthians 15:20.
4. `docs/translator_decisions/paradosis_synoptic_pauline_split_2026-04.md` — Synoptic-vs-Pauline split + **Col 2:8 → ธรรมเนียม caveat**. **Trigger book:** Colossians.
5. `docs/translator_decisions/semeion_three_senses_2026-04.md` — miracle / authentication-mark / signal disambiguation. **Trigger book:** 1 Corinthians 1:22, 14:22.

---

## Tagging eligibility

All §1 mechanical gates clean. §2 internal review complete. §3 external AI review complete (Gemini, all FINE). §4 native-speaker / theological reviewer feedback **pending** (3 questions live on review form).

**Tag `book-2thessalonians-v1` is gated on §4** — recommend awaiting at least one native-speaker reviewer's pass on the 3 form questions before tagging. None of the 3 questions block immediate downstream translation work; tagging can proceed-with-revisable-promise once §4 returns input.
