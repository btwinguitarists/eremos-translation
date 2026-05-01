# Acts — End-of-Book Review

**Date:** 2026-04-26
**Scope:** All 28 chapters (1,002 verses); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** ACT 28 shipped (commit `e9ffbd7`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 28/28 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `git status output/` clean; main branch up to date with origin.
- **8 inherited Luke-era locks verified compliant** in Acts (ἐκκλησία, ἄφεσις, narrator-κύριος, βασιλεία, οὐρανός-Ascension, παρρησία, divine-praise default, vocative Κύριε).
- **3 cross-cutting patterns are STABLE-but-undocumented at corpus level** (ἔθνος contextual handling, Roman administrative titles, pagan-deity proper nouns). Verse-level rationale carries the full burden; recommend lifting to `docs/translator_decisions/` before Pauline epistles.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation).
- **1 item flagged DECIDE** (Acts 21 we-passage register elevation).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. ἔθνος — three-way contextual split — **STABLE (undocumented; recommend new doc)**

28 occurrences in Acts, principled three-way split that Thai readers parse cleanly:

| Sense | Thai | Count | Representative |
|---|---|---|---|
| Geopolitical "nations" (Psalmic / cosmic / universal scope) | **ประชาชาติ** | 2 | 4:25 (Psalm 2 quotation), 17:26 (every nation of mankind) |
| "Nation" as specific people-group (incl. Israel itself) | **ชนชาติ** | 8 | 7:7 (Stephen, OT context); 13:19 (seven nations of Canaan); 24:2, 24:10, 24:17 (Felix audience speaking of "this nation"); 26:4 (Paul's "nation"); 26:23a (λαός↔ἔθνος dichotomy "people [of Israel] and Gentiles") |
| "Gentiles" (non-Jewish mission target) | **คนต่างชาติ** | 16 | 10:45, 11:1, 11:18, 13:46, 13:48, 15:7, 15:12, 15:17, 18:6, 21:19, 21:21, 22:21, 26:20, 26:23b, 28:28, etc. |
| "Samaritan" people-collective | **ชาวสะมาเรีย** | 1 | 8:9 (τὸ ἔθνος τῆς Σαμαρείας) |
| **ANOMALY** — "Gentiles" rendered as **ชนต่างชาติ** | inconsistent variant | 2 | **4:27, 14:27** |

**Acts 26:23 is the cleanest exegetical proof of the rule** — the verse maps λาός→ชนชาติ (Israel-as-nation) against ἔธนεσιน→คนต่างชาติ (Gentiles) within a single doublet. Translator clearly distinguishes the two semantic fields.

### REVIEW flag — ชนต่างชาติ vs. คนต่างชาติ

ACT 4:27 and 14:27 render "Gentiles" as **ชนต่างชาติ** (ชน-prefix), where the other 16 mission-context occurrences use **คนต่างชาติ** (คน-prefix). Both are grammatical Thai for "Gentile-people"; ชน- is the more literary register, คน- the everyday register. Per-verse rationales do not flag the choice. **Recommend: normalize to คนต่างชาติ at 4:27 + 14:27 OR document the literary-elevation choice (4:27 is in a high-register congregational prayer; 14:27 reports to the Antiochene church — both formal-public contexts). Ben to decide.**

**→ Recommend new doc:** `docs/translator_decisions/ethnos_nations_vs_gentiles_2026-04.md` — locks the three-way split for Pauline forward-pass (Romans 9–11 + Galatians + Ephesians 2–3 will compound this).

---

## 2. Roman administrative titles — **STABLE (undocumented; recommend new doc)**

Acts is the NT corpus where Roman administrative vocabulary peaks. Findings:

| Greek | Thai | Count | Status |
|---|---|---|---|
| χιλίαρχος (Roman tribune, cohort commander) | **นายพัน** | 12 | ✓ uniform across 21:31–24:22 |
| ἑκατοντάρχης / ἑκατόνταρχος (centurion) | **นายร้อย** | 11 | ✓ uniform |
| ἡγεμών (governor — Felix, Festus) | **ผู้ว่าราชการ** | 6 | ✓ uniform |
| πολιτάρχης (Thessalonian city authority) | **เจ้าหน้าที่ปกครองเมือง** | 2 | ✓ uniform |
| στρατηγός (temple captain vs. Philippi magistrate) | **นายทหารรักษาพระวิหาร** (4:1, 5:24, 5:26) / **ผู้พิพากษาเมือง** (16:20, 22, 35, 36, 38) | 8 | ✓ principled split |
| γραμματεύς (Jewish scribes vs. Ephesus town clerk) | **ธรรมาจารย์** (4:5, 6:12, 23:9) / **เจ้าหน้าที่เลขานุการเมือง** (19:35) | 4 | ✓ principled split |
| Σεβαστός (Augustus title) | **องค์จักรพรรดิ** | 2 | ✓ documented at 25:21 (Σεβαστός ≠ Καῖσαρ) |
| Καῖσαρ (throne-name) | **ซีซาร์** | 9 | ✓ uniform; ἐπικαλέομαι Καίσαρα → ถวายฎีกา/อุทธรณ์ต่อซีซาร์ glossary-locked |
| πρῶτος τῆς νήσου (Publius, Malta) / πρῶτοι (leading men) | **หัวหน้าของเกาะ** / **หัวหน้า / ผู้นำ** | 3 | ✓ |

**Honorifics applied per `honorifics_non_divine_authorities_2026-04.md`** — Felix and Festus (governors) consistently get plain register (no ทรง). Agrippa II (king) consistently gets ราชาศัพท์ (ทรงเสด็จมา 25:13, ทรงทราบ/ทรงเชื่อ 26:26–27, เสด็จ 25:23). Herod Agrippa I in 12:1 also gets ทรง for kingly action. **The Markan default scales correctly to Acts.**

### REVIEW flag — ἀνθύπατος drift

Three occurrences with two Thai renderings:
- 13:8, 13:12 (Sergius Paulus, Cyprus): **ผู้สำเร็จราชการ**
- 19:38 (generic "the proconsuls exist"): **ผู้ว่าการ**

The split is defensible (specific named proconsul vs. abstract reference to the institution at Asia's assize courts), but **ผู้ว่าการ** at 19:38 is also lexically very close to **ผู้ว่าราชการ** (used elsewhere for ἡγεμών = governor), creating a potential reader confusion between two different Roman ranks. **Recommend: confirm ผู้สำเร็จราชการ as the standard render for ἀνθύπατος, and either normalize 19:38 OR document the generic-vs-specific split. Ben to decide.**

**→ Recommend new doc:** `docs/translator_decisions/roman_administrative_titles_2026-04.md` — locks the χιλίαρχος / ἑκατοντάρχης / ἡγεμών / ἀνθύπατος / πολιτάρχης / στρατηγός / Καῖσαρ / Σεβαστός vocabulary block. The Pauline corpus will revisit ἡγεμών (Rom 13:1–7 ἐξουσίαι) but the proper-noun titles are largely Acts-specific.

---

## 3. Pagan-deity proper nouns — **STABLE (undocumented; recommend new doc)**

Acts establishes the corpus pagan-deity policy. Strong verse-level rationale (the Acts 19:24 KD explicitly cross-references RULES §3 + ACT 14 polytheistic-lock + ACT 17:18 δαιμόνιον treatment), but no consolidated `docs/translator_decisions/` doc.

| Greek | Thai | Type | Reference |
|---|---|---|---|
| Ζεύς (Δία acc) | **ซีอุส** | transliteration | 14:12, 14:13 |
| Ἑρμῆς (Ἑρμῆν acc) | **เฮอร์เมส** | transliteration | 14:12 |
| Ἄρτεμις | **อารเทมิส** | transliteration | 19:24, 19:27, 19:28, 19:34, 19:35 |
| θεά (goddess feminine) | **เทพี** | register-marked feminine | 19:27, 19:37 |
| Διόσκουροι (Castor + Pollux) | **ฝาแฝดดิออสคูรี** | transliteration + descriptive (twin-pair) | 28:11 |
| ἡ Δίκη (Justice goddess) | **เทพีแห่งความยุติธรรม** | descriptive translation (NOT transliteration) | 28:4 |
| Μολόχ (Amos 5:26 LXX) | **โมเลค** | transliteration | 7:43 |
| Ῥαιφάν (Amos 5:26 LXX) | **เรฟาน** | transliteration | 7:43 |
| ἀγνώστῳ θεῷ ("to the unknown god") | **แด่พระเจ้าที่ไม่รู้จัก** | translated phrase (Athenian altar inscription) | 17:23 |
| οἱ θεοί (polytheistic plural) | **เหล่าทวยเทพ** | polytheistic-register plural | 14:11 |
| Θεοῦ φωνὴ (crowd to Herod) | **เสียงของเทพเจ้า** | "a god" register | 12:22 |
| ἔλεγον αὐτὸν εἶναι θεόν (Maltese natives on Paul) | **ท่านเป็นเทพเจ้าองค์หนึ่ง** | "one of the gods" register | 28:6 |

**Two principled rules already operating:**

1. **Pagan-deity register: เทพ / เทพี / เทพเจ้า / เหล่าทวยเทพ** — explicitly NOT พระเจ้า (which is reserved for the biblical God). Crowd at 12:22 (Herod's death) and Maltese natives at 28:6 (Paul not dying) say "เทพเจ้า" — Luke's own theology then corrects them in narrator voice.
2. **Transliteration-vs-translation split:** Personal proper-name deities (Zeus, Hermes, Artemis, Castor/Pollux, Moloch, Rephan) get **transliteration**; abstract/personified-attribute deities (Δίκη "Justice") get **descriptive translation** (เทพีแห่งความยุติธรรม). Reasonable; defensible; reader-comprehension-prioritized.

### Acts 28:11 Διόσκουροι — note

Renders as **ฝาแฝดดิออสคูรี** (twin-pair-Dioscuri) — uses the Greek collective form rather than the Latin Castor/Pollux pair-name. The user's question prompt mentioned "Castor/Pollux" — the Thai chose to follow Luke's Greek source over the more-recognizable Latin pair-name. Defensible (Luke wrote in Greek; Castor/Pollux is a Roman-mythology framing of the same deities). Confirm with Ben whether to keep this Greek-source-fidelity or pivot toward Thai-reader-recognition with คาสเตอร์และพอลลักซ์ as a footnote.

**→ Recommend new doc:** `docs/translator_decisions/pagan_deity_proper_nouns_2026-04.md` — locks the register policy + transliteration-vs-descriptive split before:
- 1 Cor 8:5–6 (πολλοὶ θεοί)
- 1 Cor 10:14 + 10:19–21 (εἰδωλόθυτα + δαιμόνια)
- Rom 1:18–25 (Gentile idolatry critique)
- Galatians 4:8–9 (φύσει μὴ οὖσιν θεοῖς)

---

## 4. σωτήριον τοῦ θεοῦ — Lukan two-volume inclusio — **STABLE**

Verified the Luke 2:30 + Luke 3:6 → Acts 28:28 inclusio renders cleanly:

- **LUK 2:30** (Simeon): τὸ σωτήριόν σου → **ความรอดของพระองค์**
- **LUK 3:6** (Baptist citing Isa 40:5): τὸ σωτήριον τοῦ θεοῦ → **ความรอดของพระเจ้า**
- **ACT 28:28** (Paul to Roman Jews): τοῦτο τὸ σωτήριον τοῦ θεοῦ → **ความรอดของพระเจ้านี้**

**Documented at verse level** — the ACT 28:28 KD explicitly cross-references LUK 2:30 + 3:6 and names the inclusio. The Lukan two-volume bookend (σωτήριον first announced at the Temple by Simeon, then proclaimed by Baptist at the Jordan, then declared as having reached the Gentiles in Rome) is preserved by uniform Thai rendering ความรอด + ของพระเจ้า/ของพระองค์.

**Recommendation: STABLE — no separate doc needed.** The verse-level rationale at 28:28 carries the full burden. Could be lifted to a doc later if Romans 11:11 or 11:14 (σωτηρία τοῖς ἔθνεσιν) needs corpus-level coordination.

---

## 5. Lukan "we"-passages — narrator voice register — **DECIDE (Acts 21 outlier)**

Four "we" blocks with consistent Greek 1pl markers (ἡμᾶς / ἡμῶν / ἡμεῖς / ἡμῖν + 1pl verbs):

| Block | Verses | Thai 1pl form | Status |
|---|---|---|---|
| 1. Troas → Philippi | 16:10–17 | **เรา / พวกเรา** (mixed, natural register) | ✓ |
| 2. Philippi → Troas | 20:5–15 | **พวกเรา** uniform | ✓ |
| 3. Miletus → Jerusalem | 21:1–18 | **ข้าพเจ้าทั้งหลาย** uniform (7 of 7) | **DECIDE** |
| 4. Caesarea → Rome | 27:1–28:16 | **พวกเรา** uniform | ✓ |

### DECIDE flag — Acts 21 register elevation

All 7 we-passage verses in chapter 21 (21:1, 5, 11, 12, 16, 17, 18) use **ข้าพเจ้าทั้งหลาย** ("I + the rest of us," formal-literary register). Every other we-passage chapter uses **พวกเรา** ("we", natural register). Within 21:5, the verse mixes ข้าพเจ้าทั้งหลาย AND พวกเรา in a single sentence — suggesting the elevation is partial/inconsistent.

**Verse-level key_decisions for 21:1, 21:5, 21:11 do NOT document the register choice.** The 21:1 KD only notes "ἡμᾶς exclusive 'we' = Luke + Paul + traveling-companions, not the readers" — addressing the inclusive/exclusive question, not the formality elevation.

**Two readings:**

(a) **Deliberate register elevation** — Chapter 21 is the most theologically/dramatically charged we-block: prophetic warning (21:11), tearful farewell (21:13), formal arrival in Jerusalem (21:17), audience with James and elders (21:18). The literary lift to ข้าพเจ้าทั้งหลาย honors the gravity. If so, **document in a we-passage doc + restore inner-verse consistency** (eliminate the พวกเรา mid-21:5).

(b) **Unmarked drift** — A single chapter's register slip when the rest of the corpus uses พวกเรา. If so, **normalize 21:1–18 to พวกเรา** for corpus-uniform we-passage handling.

**Ben to decide.** This is the one item I'd recommend resolving before `book-acts-v1` tag, because it lands a register-mark in Luke's most signature stylistic feature (the we-passages) — and Acts 27:1+ is the longest we-block, where any chapter-21 precedent will pull the much-longer voyage narrative.

**→ If decision is (a):** new doc `docs/translator_decisions/we_passage_register_2026-04.md`. **If (b):** spot-revise 7 verses in Acts 21 to พวกเรา.

---

## 6. Inherited Luke-era locks — **all compliant**

Verified Acts compliance against existing `docs/translator_decisions/`:

| Doc | Acts evidence | Status |
|---|---|---|
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 22 narrator-κύριος-as-Jesus verses sampled (8:25; 9:10, 11, 15, 17, 27, 42; 11:21, 24; 13:11, 12, 47, 48, 49; 14:23; 16:14, 32; 18:9; 19:10, 17, 20; 22:10) — **all องค์พระผู้เป็นเจ้า**. No drift. | **LOCKED** |
| `basileia_kingdom_rendering_2026-04.md` | All 7 βασιλεία τοῦ θεοῦ in Acts (1:3, 8:12, 14:22, 19:8, 20:25, 28:23, 28:31) → **อาณาจักรของพระเจ้า**. 1:6 (political "kingdom to Israel") → อาณาจักร. | **LOCKED** |
| `aphesis_forgiveness_of_sins_2026-04.md` | All 5 Acts sermons (2:38, 5:31, 10:43, 13:38, 26:18) → **การยกโทษบาป**. Lock A1 from LUK end-of-book holds. | **LOCKED** |
| `ekklesia_2026-04.md` | 16 Christian-community uses → **คริสตจักร** (5:11, 8:1, 8:3, 9:31, 11:22, 11:26, 12:1, 13:1, 14:23, 14:27, 15:3, 15:4, 15:22, 15:41, 16:5, 18:22, 20:17, 20:28). Civic-assembly carve-out at **19:32, 19:39, 19:40 → ที่ประชุม** per doc's exception. Stephen's LXX use at **7:38 → ที่ประชุมของอิสราเอล** per doc's OT-LXX exception. **Fully compliant**. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | **Ascension 1:10–11 → สวรรค์** (matches LUK 24:51 lock). 1:10 + 1:11 also use ท้องฟ้า for the literal "looking up at the sky" act — defensible (the disciples gaze meteorologically; Jesus ascends to heaven theologically). 7:42 ("host of heaven") → ฟ้าสวรรค์ per cosmic-emphatic exception. 7:55 (Stephen's vision) + 9:3 (Damascus light) — mixed render. Per doc's note about retrospective normalization being deferred until John-era sweep. | **LOCKED (doc anticipates sweep)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | Sample Κύριε vocatives (Ananias 9:10 → องค์พระผู้เป็นเจ้า; Cornelius 10:14 → องค์พระผู้เป็นเจ้า; Paul 22:10 → องค์พระผู้เป็นเจ้า) — disciples-and-confessing-believers route holds. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | See **§7 below** — partial drift flagged. | **REVIEW** |
| `narrator_vs_character_voice_2026-04.md` + `speech_verbs_adversaries_addressing_divine_2026-04.md` | Stephen's speech (ch.7); Peter's sermons (chs.2–4, 10–11); Paul's sermons (chs.13, 17, 22, 24, 26) — narrator royal register on apostles' divine subjects + character-voice register tracking speaker stance. ποτπότητός(?) verb: παρρησιάζομαι 100% uniform across Acts → **อย่างกล้าหาญ** (10/10). | **LOCKED** |

---

## 7. Praise-verb default — **REVIEW (mild δοξάζω drift)**

`divine_object_praise_verbs_2026-04.md` locks สรรเสริญ as the corpus default for δοξάζω + εὐλογέω + αἰνέω + αἶνον δίδωμι when God is the object.

**Acts findings:**

| Verse | Greek | Thai | Status |
|---|---|---|---|
| 2:47 | αἰνοῦντες τὸν θεόν | สรรเสริญพระเจ้า | ✓ default |
| 3:8 | αἰνῶν τὸν θεόν | สรรเสริญพระเจ้า | ✓ default |
| 3:9 | αἰνοῦντα τὸν θεόν | สรรเสริญพระเจ้า | ✓ default |
| 4:21 | ἐδόξαζον τὸν θεόν | **ถวายพระเกียรติแด่พระเจ้า** | non-default |
| 10:46 | μεγαλυνόντων τὸν θεόν | สรรเสริญพระเจ้า | ✓ default |
| 11:18 | ἐδόξαζον τὸν θεόν | **ถวายเกียรติแด่พระเจ้า** | non-default |
| 13:48 | ἐδόξαζον τὸν λόγον | **เทิดทูน(พระวจนะ)** | non-default; doxological |
| 19:17 | ἐμεγαλύνετο τὸ ὄνομα | **ได้รับการยกย่องสรรเสริญ** | mixed |
| 21:20 | ἐδόξαζον τὸν θεόν | **ถวายเกียรติแด่พระเจ้า** | non-default |

The 4:21 + 11:18 + 21:20 cluster systematically uses **ถวายเกียรติ** for δοξάζω in narrator-context "they glorified God." The doc says default = สรรเสริญ but allows ถวายพระเกียรติ for "doxological-formal contexts." All three verses are corporate-acclamation-after-salvific-event (Sanhedrin-released-apostles 4:21; Jerusalem-believers-on-Cornelius 11:18; James + elders on Paul's mission 21:20) — arguably doxological-formal, defensible.

**REVIEW: Confirm whether δοξάζω → ถวายเกียรติ for narrator-context "they glorified God" is the intended sub-pattern.** If so, amend `divine_object_praise_verbs_2026-04.md` to document the sub-rule. If not, normalize the three verses to สรรเสริญ.

---

## Mechanical (§1) — **all green**

- 28/28 chapters: `output/check_reports/acts_NN_review.md` + `_summary.json` ✓
- 28/28 chapters: per-chapter back-translations + check sub-reports (back_translation, claim_consistency, greek_field_integrity, key_term_consistency, ot_citations, tnbt_comparison) ✓
- `python3 scripts/check_key_term_consistency.py` clean — **0 rule violations, 0 undocumented multi-renderings** across the entire 4-book corpus
- `git status output/` clean (last commit `e9ffbd7`, ACT 28 source + checks + reader doc + bundle hashes)

---

## Pre-existing docs affirmed / unchanged

- `amen_saying_formula_2026-04.md` — applies as in Mark/Matthew/Luke; Acts has no Jesus ἀμήν λέγω formula (not Acts genre).
- `aramaic_transliterations_2026-04.md` — Aramaic mostly absent; Saulos/Saul Σαούλ at 9:4, 22:7, 26:14 → "เซาโล/ซาอูล" handled per-verse.
- `historic_present_2026-04.md` — applies; Lukan careful Greek minimizes historic presents (Acts is heavier on aorist + imperfect than Mark).
- `honorifics_non_divine_authorities_2026-04.md` — fully compliant (Felix, Festus = plain; Agrippa I+II = ราชาศัพท์ for kingly action). The doc's "Acts will stress-test this" note is now satisfied.
- `inclusion_variants_absent_verses_2026-04.md` — Path A applied. Acts 8:37 (Western "Eunuch's confession") and Acts 24:6b–8a (Western Lysias addition) handled per RULES §0; Tier 2 footers added for v.6b–8a (commit `66c8bd4`).
- `markan_euthys_immediately_2026-04.md` — Mark-specific; Acts uses εὐθέως conventionally (no signature-marker behavior).
- `metanoeo_vs_metamelomai_2026-04.md` — Acts μετανοέω uniform → กลับใจ (2:38, 3:19, 8:22, 17:30, 26:20). No μεταμέλομαι in Acts.
- `parabolic_god_figures_human_register_2026-04.md` — Acts has no parables (genre absence); doc not exercised.
- `psyche_vs_pneuma_anthropological_2026-04.md` — Acts 2:27, 2:31 (Hades/soul/flesh trichotomy from Ps 16) handled per Luke pattern.
- `son_of_man_disambiguation_2026-04.md` — Acts has only Stephen's vision at 7:56 (Son of Man); follows Luke pattern.

---

## Flagged for Ben's attention

### A. Acts 21 we-passage register — **DECIDE before tagging** (§5)
Ben to decide whether the seven-verse ข้าพเจ้าทั้งหลาย run is a deliberate elevation (then document) or unmarked drift (then normalize). The mid-21:5 inconsistency (ข้าพเจ้าทั้งหลาย → พวกเรา within one verse) is the strongest evidence for "drift."

### B. ἔธนος split — confirm + new doc (§1)
Confirm three-way split is correct as observed; resolve 4:27 + 14:27 ชนต่างชาติ inconsistency; if confirmed, write `ethnos_nations_vs_gentiles_2026-04.md`. **Highest Pauline-forward priority** — Romans 9–11 will compound this.

### C. Roman titles — confirm + new doc (§2)
Confirm ἀνθύπατος rendering (ผู้สำเร็จราชการ vs. ผู้ว่าการ at 19:38); if confirmed, write `roman_administrative_titles_2026-04.md`. Largely Acts-specific but Romans 13:1–7 + 1 Tim 2:1–2 use ἐξουσίαι generically.

### D. Pagan-deity register — new doc (§3)
The verse-level rationale is exceptionally strong (the 19:24 + 19:27 + 17:18 + 12:22 + 28:6 KDs cite each other and RULES §3). Lift to corpus-level doc before Pauline epistles. Confirm Διόσκουροι Greek-source choice over Latin Castor/Pollux pair-name (28:11).

### E. Praise-verb sub-rule — confirm or normalize (§7)
Three δοξάζω-narrator-context verses (4:21, 11:18, 21:20) use ถวายเกียรติ instead of the doc's สรรเสริญ default. Either amend doc to document the sub-rule or normalize.

### F. External AI review (§3 of checklist) — pending
Recommended before `book-acts-v1` tag. The Pauline-forward stakes (especially ἔθνος + pagan-deity policy + Roman titles) warrant at least one external AI sanity-check pass. Suggest Gemini 2.5 Pro on a 4-chapter packet (Acts 7 [Stephen's OT-citation density], Acts 17 [Areopagus + pagan-deity peak], Acts 21 [we-passage register flag], Acts 28 [σωτήριον inclusio + Δίκη + Διόσκουροι + closing prison-house]).

---

## External AI review outcomes (Gemini 2.5 Pro + ChatGPT, 2026-04-26)

Per checklist §3, submitted the focused 6-item packet (`~/Desktop/eremos-acts-external-ai-review-packet.md`) to **both Gemini 2.5 Pro and ChatGPT**. Both returned substantive verdicts. Cross-checked all claims against actual JSONs.

| Item | Gemini | ChatGPT | Resolution |
|---|---|---|---|
| A — Acts 21 we-register | CONCERN, normalize to พวกเรา | CONCERN, normalize | **Spot-revised** (20 occurrences in acts_21.json) |
| B — ἔθνος ชนต่างชาติ at 4:27 + 14:27 | CONCERN, normalize 14:27 + 4:27→ประชาชาติ | FINE, document as literary variant | **Spot-revised both to คนต่างชาติ** + new doc. Note: Gemini misread 4:27 (ἔθνεσιν there is Pauline-Gentiles in apposition with λαοῖς Ἰσραήλ, NOT cosmic-Psalmic; would have broken the deliberate λαός/ἔθνος contrast) |
| C — ἀνθύπατος drift | CONCERN, normalize to ผู้สำเร็จราชการ | CONCERN, normalize | **Spot-revised**. Audit also surfaced Acts 18:12 (Gallio) drift missed by initial review — also normalized. Total 6 occurrences in acts_18.json + 9 in acts_19.json (incl. KD rationales + thai_summary). |
| D — Διόσκουροι Greek vs. Latin | FINE, keep ดิออสคูรี | MINOR CONCERN, Ben to decide | **Locked as-is** — Ben confirmed Greek-source fidelity preference |
| E — δοξάζω → ถวายเกียรติ | FINE, log sub-rule | FINE, log sub-rule | **Amended `divine_object_praise_verbs_2026-04.md`** with narrator-doxological sub-rule |
| F — σωτήριον inclusio | FINE, lock | FINE, lock | **Locked as-is** |
| §Z — καταγγέλλω/εὐαγγελίζομαι distinctness | flagged as worth checking | flagged as worth checking | **Audited** — κηρύσσω + καταγγέλλω → ประกาศ uniformly (defensible Thai-naturalness collapse). εὐαγγελίζομαι → ประกาศข่าวประเสริฐ when intransitive; with explicit content-object (τὸν λόγον) parallels 15:35 + 13:32 pattern (ประกาศ + content-noun). Acts 16:21 καταγγέλλω → เผยแพร่ principled (negative-spreading accusation, documented). **No drift; no action.** |

## Spot-revisions executed (2026-04-26)

| File | Verses | Change | Verification |
|---|---|---|---|
| `output/translations/acts_04.json` | 4:27 + KD | ชนต่างชาติ → คนต่างชาติ (3 occurrences in file) | greek_field_integrity 0/0 |
| `output/translations/acts_14.json` | 14:27 (.thai + thai_summary + KD) | ชนต่างชาติ → คนต่างชาติ (3 line-targeted edits, leaving 14:2 + 14:16 thai_literal untouched) | greek_field_integrity 0/0 |
| `output/translations/acts_18.json` | 18:12 (.thai + thai_literal + thai_summary + KD ×2) | ผู้ว่าการ → ผู้สำเร็จราชการ (6 occurrences in file) | greek_field_integrity 0/0 |
| `output/translations/acts_19.json` | 19:38 + 19:40 thai_summary | ผู้ว่าการ → ผู้สำเร็จราชการ (9 occurrences in file) | greek_field_integrity 0/0 |
| `output/translations/acts_21.json` | 21:1, 5, 11, 12, 16, 17, 18 + earlier-audit-missed verses (21:2, 3, 4, 6, 7, 8, 10, 14, 15) — full chapter we-passage normalization | ข้าพเจ้าทั้งหลาย → พวกเรา (20 occurrences in file) | greek_field_integrity 0/0 |

**Corpus-wide post-revision checks:**
- `check_key_term_consistency.py`: 0 rule violations, 0 undocumented multi-renderings
- `check_phrase_consistency.py`: 7 phrase-locks audited, 0 violations
- `check_greek_field_integrity.py` (5 touched chapters): all 0/0 hard-fails/warnings

## New + amended documents

1. `docs/translator_decisions/ethnos_2026-04.md` — three-way split (ประชาชาติ / ชนชาติ / คนต่างชาติ); locks ชนต่างชาติ as deprecated variant
2. `docs/translator_decisions/roman_administrative_titles_2026-04.md` — full title-by-title lock; explicit ἀนธύπาτος → ผู้สำเร็จราชการ vs. ἡγεμών → ผู้ว่าราชการ distinction
3. `docs/translator_decisions/pagan_deities_2026-04.md` — register policy (เทพ/เทพี/เทพเจ้า; never พระเจ้า) + transliteration vs. descriptive split
4. `docs/translator_decisions/divine_object_praise_verbs_2026-04.md` — amended to log δοξάζω narrator-doxological sub-rule (ถวายเกียรติ for corporate-narrator acclamation)

## Recommendation

**Acts ships in strong corpus-hygiene shape with all flagged items resolved.**

Tag `book-acts-v1` after:
1. ✅ Ben's decisions (§A–F received 2026-04-26)
2. ✅ Spot-revisions executed + checks clean
3. ✅ External AI sanity-check (Gemini + ChatGPT)
4. ✅ Three new translator_decisions docs written
5. ✅ Praise-verbs doc amended

Romans (or whichever epistle is next per `data/production_order.json`) can begin in parallel.
