# Jude — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 1 chapter (25 verses; 64 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (47 docs).
**Trigger:** JUD 1 shipped (commit `dd8164e`); per `docs/END_OF_BOOK_CHECKLIST.md`. (Jude is single-chapter; the chapter and the book are coterminous.)
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **13 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 1/1 chapter has a green per-chapter `*_review.md` report + back-translation; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-228-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows no JUD source-file dirt (only unrelated paratext exports + 1JN textual_variants file from earlier audits).
- **Jude is one of the most lexically-distinctive books in the NT corpus.** 25 verses contain **~13 NT-hapax legomena** (one every two verses): ἐπαγωνίζομαι (v.3), παρεισδύω (v.4), ἐκπορνεύω + δεῖγμα + ὑπέχω (v.7), φυσικῶς (v.10), Κόρε (v.11), σπιλάς + φθινοπωρινός (v.12), ἐπαφρίζω + πλανήτης (v.13), ἀσεβέω (v.15), γογγυστής + μεμψίμοιρος (v.16), ἀποδιορίζω (v.19), ἄπταιστος (v.24). Per-verse hapax-density is the second-highest in the NT after 3 JN. Each is flagged in the verse-level `notes` per RULES §5; verse-level handling is adequate (no corpus doc needed) — but the cluster-density itself merits a noting-summary (§3 below).
- **Jude makes TWO direct citations of NON-CANONICAL Jewish pseudepigrapha** — UNIQUE in the NT corpus:
  - **JUD 1:9** — `Ἐπιτιμήσαι σοι κύριος` ("the Lord rebuke you") referencing the lost **Assumption of Moses** (also called *Testament of Moses*) tradition where Michael disputes with the devil over Moses's body.
  - **JUD 1:14–15** — direct quotation of **1 Enoch 1:9** introduced as `Προεφήτευσεν ... Ἑνώχ` ("Enoch prophesied").
  Both already have `thai_summary` entries explaining the source and the Protestant interpretive frame (citation does NOT entail canonical-status; cf. Pauline citation of Greek poets at ACT 17:28 + TIT 1:12). This is the **single biggest editorial decision in Jude** and warrants a NEW corpus doc — see §2 below.
- **Jude has the most-charged TEXTUAL VARIANT in the NT corpus** at JUD 1:5: SBLGNT prints `Ἰησοῦς` (Jesus); Byzantine + later mss read `κύριος` (Lord). Per RULES §0 the project follows SBLGNT — `พระเยซู` (Christ-pre-incarnate-Exodus-deliverer reading; cf. 1 COR 10:4 corpus-internal-link). The verse already carries a substantial `thai_summary` explaining the variant + Christological-significance. See §1 below.
- **Strong synoptic-parallel with 2 PET 2:1–3:3.** Approximately TWO-THIRDS of Jude shares-vocabulary-or-imagery with 2 Peter (the relationship is debated — most modern scholars hold Jude → 2 Peter, but the Eremos translation does not commit to a direction). The cross-corpus rendering of shared vocabulary (δεσπότης, ζόφος, σαρκός μιαίνουσιν, κυριότης + δόξας, ἐμπαῖκται, etc.) is uniformly compliant with the 2 Peter 2 KDs. See §11 below.
- **1 NEW corpus-doc lift emerges from JUD-distinctive content**:
  - **`pseudepigrapha_citations_2026-05.md`** (§2) — locks the surfacing-strategy for direct citations of non-canonical Jewish-tradition (JUD 9 Assumption-of-Moses + JUD 14–15 1-Enoch). Both passages already use `thai_summary` to surface the citation-context for Thai-Protestant readers; the corpus doc would formalize the strategy + the Protestant interpretive frame as the project's standard for any future analogous case (e.g., the 2 PET 2:4 fallen-angels-tradition reference, which the existing chapter handles compatibly).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): (a) **ἐπαγωνίζομαι v.3 → ต่อสู้อย่างเข้มแข็ง** (Jude's famous programmatic-statement "contend earnestly for the faith"); (b) **πληθυνθείη Catholic-Epistle greeting verb cross-corpus split** — 1 PET 1:2 → ทวียิ่งขึ้น vs JUD 1:2 + 2 PET 1:2 → ทวีคูณ (a Thai-corpus internal split worth confirming as principled or harmonizing); (c) **Pastoral triage at vv. 22–23** (the three-fold mercy-doubting / fire-rescue / fearful-mercy-with-clothing-hatred pattern — whether a v.23 thai_summary should explicate the priestly-defilement ZEC 3:3–4 + LEV 13:47 imagery).
- **2 items flagged DECIDE** (Ben choice needed before tagging): (a) the **Pseudepigrapha-citation surfacing strategy** at JUD 9 + JUD 14–15 — the two passages currently use thai_summary to bound the canonical-status reading; the DECIDE question is whether the surfacing is adequate or should be elevated/expanded (and whether to formalize as a new corpus doc); (b) the **Doxology v.25 Christological-mediation phrasing** `μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ` ("to the only God our Savior, through Jesus Christ our Lord") — the σωτῆρι-of-Father usage is theologically-charged (distinct from 2 PET 1:1 Granville-Sharp Christological-σωτῆρι); the KD already disambiguates against the Pastorals corpus, but the bare Thai surface may not preserve the trinitarian-mediation nuance for typical readers.
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Textual variant at v.5 — SBLGNT `Ἰησοῦς` vs Byzantine `κύριος` — **STABLE → LOCKED** (RULES §0 governs)

JUD 1:5 contains the single most Christologically-charged textual variant in Jude:

| Reading | Text | Modern critical-text |
|---|---|---|
| **SBLGNT (Eremos follows)** | `Ἰησοῦς λαὸν ἐκ γῆς Αἰγύπτου σώσας` | NA28, UBS5 (against earlier UBS4) — based on 𝔓72 (3rd-c.), Vaticanus, the Vulgate, and the Coptic |
| **Byzantine + later mss** | `κύριος` (Lord) | TR, KJV-tradition |
| **Older critical-texts** | `[ὁ] κύριος [ἅπαξ]` | UBS4 (now superseded) |

**Current rendering:** `พระเยซูได้ทรงช่วยประชากรของพระองค์ออกจากแผ่นดินอียิปต์` ("Jesus saved the people from the land of Egypt"). The verse carries a substantial **thai_summary** explaining:
1. SBLGNT prints `Ἰησοῦς`; later mss read `κύριος`.
2. Modern critical editions (NA28, UBS5) follow SBLGNT.
3. Eremos follows SBLGNT per RULES §0.
4. The Christological-significance: Christ-pre-incarnate as Exodus-deliverer (cf. 1 COR 10:4 "the rock was Christ").

**Editorial assessment.** This is the most-defensible call in Jude. RULES §0 commits the project to SBLGNT-strict alignment, so the textual choice is mechanical. The Christological consequence (pre-incarnate-Christ-as-Exodus-Lord) is significant and the thai_summary discloses it transparently. Major modern English versions (NIV, ESV, CSB) also follow SBLGNT here. THSV/THKJV follow the Byzantine `κύριος` reading — Eremos diverges from those Thai versions on principled-text-critical grounds.

The thai_summary is well-structured: it surfaces the variant, names the editorial choice, and articulates the Christological reading without polemic. A typical Thai-Protestant reader who encounters Eremos's `พระเยซู` and is familiar with THSV's `องค์พระผู้เป็นเจ้า` will find the explanation in-place at the chapter rather than having to consult an external commentary.

**Recommend: STABLE → LOCKED.** This is the project's flagship case for SBLGNT-strict-alignment with an interpretively-significant variant; documenting it formalizes the precedent for similar future cases (REV 22:14 etc.). The thai_summary is adequate as-is. **No corpus doc needed** — RULES §0 already governs; the verse-level thai_summary is the documentation-of-record. Keep verse-level.

---

## 2. Pseudepigrapha citations (vv. 9 + 14–15) — **DECIDE** (recommend new corpus doc `pseudepigrapha_citations_2026-05.md`)

Jude is the ONLY NT book that makes direct citations of NON-CANONICAL Jewish pseudepigrapha:

| Verse | Citation source | Greek formula | Thai_summary present? |
|---|---|---|---|
| **1:9** | **Assumption of Moses** (also: *Testament of Moses*; lost in full, fragments survive) — Michael-and-the-devil-disputing-over-Moses's-body tradition | `οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν· Ἐπιτιμήσαι σοι κύριος` | ✓ (substantial) |
| **1:14–15** | **1 Enoch 1:9** — direct verbatim quotation introduced with prophetic-formula | `Προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· Ἰδοὺ ἦλθεν κύριος ...` | ✓ (substantial) |

Both citations also include OT-DB cross-references (the Michael-rebuke at v.9 echoes ZEC 3:2 LXX, recorded in `data/nt_ot_citations.json`).

**Editorial assessment.** The two thai_summary entries handle the surfacing well. The v.9 summary names the Assumption-of-Moses, explains the disputing-over-Moses's-body tradition, and articulates the Protestant interpretive frame: "ยูดาสไม่ได้รับรองว่าเอกสารนี้เป็นพระคัมภีร์ แต่อ้างเป็นตัวอย่างที่ผู้อ่านชาวยิวรู้จัก" ("Jude does not endorse this document as Scripture, but cites it as an example his Jewish readers would recognize"). The v.14 summary explains the citation comes from 1 Enoch 1:9, names the document as pseudepigrapha (3rd-1st c. BC), and articulates the Protestant frame with the Pauline-poets-citation parallel (ACT 17:28 + TIT 1:12).

**The interpretive-bound is critical for Thai-Protestant readers.** Without the surfacing, a typical Thai reader could:
- (Misuse direction A) Assume Jude's citation entails the canonical-status of 1 Enoch / Assumption-of-Moses (the "if it's quoted in Scripture it must be Scripture" inference);
- (Misuse direction B) Treat the citation as evidence Jude is sub-canonical himself ("Jude quotes apocryphal books, so Jude shouldn't be in the NT");
- (Misuse direction C) Confuse Jude's citation-formula `Προεφήτευσεν` ("prophesied") at v.14 as endorsement of 1 Enoch's full prophetic-status.

The current thai_summary entries bound (A) and (C) explicitly. (B) is a meta-canonical question outside the translation's scope.

**The DECIDE question.** Is the two-verse-level thai_summary surfacing adequate, or should the project formalize a NEW corpus doc to:
1. Document the pseudepigrapha-citation surfacing-strategy as a project-wide standard;
2. Specify the Protestant interpretive frame (citation ≠ canonical-status);
3. Cross-reference the existing handling of 2 PET 2:4 (fallen-angels-tradition allusion to 1 Enoch 6–21 — same-tradition-stream, treated more allusively at the 2 PET level) for cross-corpus harmonization;
4. Specify that future analogous cases (none in NT outside Jude + arguably 2 Peter) should follow the same Protestant frame.

**Editorial recommendation.** **Option A (corpus doc):** create `docs/translator_decisions/pseudepigrapha_citations_2026-05.md` formalizing the surfacing strategy. Single-author, ~1 hour. The doc would close the corpus on this question (no further NT test cases — Revelation does not cite pseudepigrapha; the corpus closes here). **Option B (status quo):** keep the verse-level thai_summary entries; treat as STABLE per-verse handling.

**Recommendation lean: Option A.** The two-verse cluster is the entirety of NT direct-pseudepigrapha-citation; documenting closes the corpus and gives the project a referenceable standard if external reviewers raise the canonical-status question. The thai_summary entries are well-crafted but operate at the verse-level only — a corpus doc lifts them to the project-wide standard. **DECIDE** because Ben's input on the project's posture toward pseudepigrapha-citation is theologically-substantive and shouldn't be assumed.

---

## 3. HAPAX cluster — ~13 NT-hapaxes in 25 verses — **STABLE** (verse-level handling adequate; flag for §3 noting only)

Jude contains the most NT-hapaxes per verse-count in the NT corpus second only to 3 JN:

| Verse | Greek hapax | Sense | Thai rendering |
|---|---|---|---|
| 1:3 | ἐπαγωνίζομαι | "contend-strenuously" (intensified ἀγωνίζομαι) | **ต่อสู้อย่างเข้มแข็ง** |
| 1:4 | παρεισδύω | "creep-in-secretly" | **แอบเข้ามา ... โดยไม่ถูกสังเกต** |
| 1:7 | ἐκπορνεύω | "give-themselves-fully-to-fornication" | **ปล่อยตัวในการล่วงประเวณี** |
| 1:7 | δεῖγμα | "example / sample" | **ตัวอย่าง** |
| 1:7 | ὑπέχω | "undergo (punishment)" | (verbal-paraphrase) **การลงโทษ** |
| 1:10 | φυσικῶς | "by-instinct / naturally" | **ตามสัญชาตญาณ** |
| 1:11 | Κόρε | proper-noun "Korah" (only-NT) | **โคราห์** |
| 1:12 | σπιλάς | "hidden reef / submerged rock" | **โขดหินที่ซ่อนอยู่** |
| 1:12 | φθινοπωρινός | "autumnal" | **ในฤดูใบไม้ร่วง** |
| 1:13 | ἐπαφρίζω | "foam-up" | **พ่นฟอง** |
| 1:13 | πλανήτης | "wandering-star / planet" | **ดาวหลงทาง** |
| 1:15 | ἀσεβέω | "act-impiously" (verb) | (cognate-cluster paraphrase) |
| 1:16 | γογγυστής | "grumbler" | **คนบ่นพร่ำ** |
| 1:16 | μεμψίμοιρος | "complainer-about-fate" | **คนช่างตำหนิ** |
| 1:19 | ἀποδιορίζω | "set-apart-by-boundary / divide" | **ก่อความแตกแยก** |
| 1:24 | ἄπταιστος | "not-stumbling" | **ไม่ให้สะดุดล้ม** |

(16 entries — slightly more than the rough "~13" count because some clusters share a verse.)

Each is flagged in the verse-level `notes` per RULES §5. Verse-level handling is adequate.

**Editorial assessment.** The cluster-density is the most striking lexical feature of Jude. Some observations:

1. **σπιλάς (v.12) "hidden reef"** — the most-rendered-imagery hapax. The Thai **โขดหินที่ซ่อนอยู่** ("hidden rocky-outcropping") preserves the sea-going-vessel-danger imagery. Note: 2 PET 2:13 has variant readings σπίλοι (spots/blemishes) vs ἀπάταις (deceptions); KDs at v.12 mark this as corpus-internal-link rather than identical-rendering — principled.

2. **φθινοπωρινός (v.12) "autumnal"** — preserves the agricultural-imagery (autumn fruitless-trees). The Thai **ในฤดูใบไม้ร่วง** is direct. Some translators argue for "late-autumn" (i.e., past-fruit-bearing season) — Eremos's neutral "in-the-autumn-season" matches the lexicon and is principled.

3. **πλανήτης (v.13) "wandering-star"** — the technical-ancient-cosmology term (vs the predictable "fixed-stars"). The Thai **ดาวหลงทาง** ("astray-stars") preserves both the astronomical reference and the moral-metaphor (false-teachers astray-from-the-orbit-of-truth).

4. **ἐπαφρίζω (v.13) "foam-up"** — onomatopoeic Greek verb. Thai **พ่นฟอง** ("spew-foam") preserves the kinetic-imagery cleanly; the τὰς ἑαυτῶν αἰσχύνας ("their own shame") object is preserved as **ความน่าอายของตน**.

5. **γογγυστής + μεμψίμοιρος (v.16)** — the doublet "grumbler + complainer-about-fate" is preserved with the Thai doublet **คนบ่นพร่ำ + คนช่างตำหนิ**. The cognate-pair γογγυστής (γογγύζω/γογγυσμός noun) preserves the Hebraic-LXX wilderness-grumbling-tradition (cf. NUM 14:27, 1 COR 10:10) — Thai **บ่นพร่ำ** reads naturally for that tradition.

6. **ἀποδιορίζω (v.19) "divide"** — the only NT use of this compound. Thai **ก่อความแตกแยก** ("create-division") preserves the schismatic sense; the boundary-setting connotation is implicit in **ก่อ ... แตกแยก**.

7. **ἄπταιστος (v.24) "not-stumbling"** — the doxological-opening hapax. Thai **ไม่ให้สะดุดล้ม** ("not-cause-to-stumble-and-fall") preserves the imagery of divine-preservation against spiritual-stumbling.

**Recommend: STABLE.** No corpus doc needed; verse-level notes carry each hapax. The cluster itself is worth flagging in the project README as a documentation-of-Jude's-distinctiveness (low priority; this is a description of the source, not a translation decision).

---

## 4. ἐπαγωνίζομαι at v.3 → ต่อสู้อย่างเข้มแข็ง — Jude's programmatic statement — **REVIEW**

JUD 1:3 contains the famous programmatic statement of the entire letter — the verse-of-record for the project's standard of "the faith once-for-all delivered":

> Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν **ἐπαγωνίζεσθαι** τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
> ท่านที่รัก เมื่อข้าพเจ้าได้พยายามอย่างเต็มที่ที่จะเขียนถึงท่านเรื่องความรอดที่เรามีร่วมกัน ข้าพเจ้าเห็นว่าจำเป็นต้องเขียนถึงท่าน เพื่อขอวิงวอนท่านให้**ต่อสู้อย่างเข้มแข็ง**เพื่อความเชื่อที่ทรงมอบแก่ธรรมิกชนทั้งหลายครั้งเดียวสำหรับทุกยุคทุกสมัย

The 1:3 KD names the agonistic-imagery:

> HAPAX ἐπαγωνίζομαι (only here NT, 'contend-strenuously' — intensified ἀγωνίζομαι) → ต่อสู้อย่างเข้มแข็ง. The agonistic-imagery (cf. 1 TIM 6:12 ἀγωνίζου τὸν καλὸν ἀγῶνα same lemma).

**Editorial assessment.** The lemma is a rare-Koine intensified-form of ἀγωνίζομαι. In the simple form, ἀγωνίζομαι appears in:
- 1 COR 9:25 — ἀγωνιζόμενος (athletic-training)
- COL 1:29; 4:12 — Paul's striving in prayer/proclamation
- 1 TIM 6:12 — `ἀγωνίζου τὸν καλὸν ἀγῶνα τῆς πίστεως` ("fight the good fight of faith") — the most-direct conceptual parallel to Jude's ἐπαγωνίζομαι
- 2 TIM 4:7 — `τὸν καλὸν ἀγῶνα ἠγώνισμαι` (Paul's farewell)

The intensified ἐπ-prefix marks an "additional" or "for-something" sense — *contend on-behalf-of* rather than just "struggle." Jude's grammatical structure (`ἐπαγωνίζεσθαι τῇ ... πίστει`, dative-of-cause-or-defense) makes the on-behalf-of sense explicit: contend FOR the faith.

The Thai **ต่อสู้อย่างเข้มแข็ง** ("strive-fight strongly") preserves the intensified force. Other Thai versions:
- THSV: **ต่อสู้เพื่อความเชื่อ** ("fight for the faith" — adverb dropped)
- THKJV: **ต่อสู้เพื่อความเชื่อ** (same simplification)
- a Thai NLT-equivalent: **ป้องกันความเชื่อ** ("defend the faith")

**The current rendering preserves the intensifier** (อย่างเข้มแข็ง = "with-vigor"), which the simpler Thai versions drop. This is principled — the ἐπ-prefix is morphologically marked in Greek; preserving an adverbial-marker in Thai is the natural-equivalent strategy.

**REVIEW question for Ben.** Is **ต่อสู้อย่างเข้มแข็ง** the right rendering, or should it be elevated to **ต่อสู้อย่างหนักแน่น** ("fight steadfastly," more theologically-loaded register) or **ต่อสู้อย่างไม่ลดละ** ("fight unrelentingly," matches the agonistic-Pauline register more closely)? This is the verse-of-record for the project's stance on contending-for-the-faith, so the rendering is theologically-resonant. Current rendering is principled and natural; the alternatives are more theologically-elevated.

---

## 5. πληθυνθείη Catholic-Epistle greeting verb — cross-corpus split (1 PET 1:2 vs 2 PET 1:2 + JUD 1:2) — **REVIEW**

The optative-passive `πληθυνθείη` ("may-X-be-multiplied") is the distinctive Catholic-Epistle opening-greeting verb. It appears in three NT openings:

| Verse | Greek | Thai (current) |
|---|---|---|
| 1 PET 1:2 | χάρις ὑμῖν καὶ εἰρήνη **πληθυνθείη** | ขอพระคุณและสันติสุขจง**ทวียิ่งขึ้น**แก่ท่านทั้งหลาย |
| 2 PET 1:2 | χάρις ὑμῖν καὶ εἰρήνη **πληθυνθείη** ἐν ἐπιγνώσει ... | ขอพระคุณและสันติสุขจง**ทวีคูณ**แก่ท่านทั้งหลาย |
| JUD 1:2 | ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη **πληθυνθείη** | ขอพระเมตตา สันติสุข และความรัก จง**ทวีคูณ**แก่ท่านทั้งหลาย |

**The cross-corpus inconsistency.** 1 PET 1:2 uses **ทวียิ่งขึ้น** ("be more abundant" / "increase further"); 2 PET 1:2 + JUD 1:2 use **ทวีคูณ** ("multiply"). Both are valid Thai renderings of πληθυνθείη; the verb does not have a fixed Thai-corpus lock per `glossary.json` or any existing translator-decisions doc, and the phrase-consistency check tolerates this split (it is not a phrase-lock).

**Editorial assessment.** The split is small but structural — it appears at the corpus-internal-linking level. The 1 PET 1:2 KD (already shipped) does not name a corpus-link; the 2 PET 1:2 KD ("Same opening-formula as 1 PET 1:2 (πληθυνθείη → จงทวีคูณ)") asserts the formula identity but renders differently from the actual 1 PET. The JUD 1:2 KD names the corpus-internal-link with 1 PET 1:2 + 2 PET 1:2 ("Catholic-Epistle-openers") and uses ทวีคูณ.

**Two options:**

**Option A.** Harmonize: change 1 PET 1:2 to **ทวีคูณ** to match 2 PET + JUD. (Or change 2 PET + JUD to **ทวียิ่งขึ้น** to match 1 PET.)

**Option B.** Leave as-is (current state). Both are defensible Thai-equivalents; the split has no semantic consequence.

**Editorial recommendation.** This is a minor cross-corpus consistency issue that surfaced only because the JUD audit examines πληθυνθείη in context of all three Catholic-Epistle openings. The split does not violate any hard-rule (no phrase-lock; no glossary entry). Given the no-translation-changes mandate of this audit, this is best surfaced for Ben's note as a STABLE-with-cross-corpus-split. If Ben wants to harmonize, the change is one-token-in-one-verse (1 PET 1:2 ทวียิ่งขึ้น → ทวีคูณ).

**REVIEW question for Ben.** Harmonize 1 PET 1:2 → ทวีคูณ to match 2 PET + JUD (Option A), or leave as-is (Option B)? Recommendation: lean toward Option A for cross-Catholic-Epistle consistency; the change is minimal and improves the corpus-internal-linking the JUD 1:2 KD already cites.

---

## 6. Triple-greeting v.2 (ἔλεος + εἰρήνη + ἀγάπη) — Jude's distinctive triad — **STABLE** (corpus-precedent affirmed)

JUD 1:2 contains a three-element greeting unique among the Catholic Epistles:

> **ἔλεος** ὑμῖν καὶ **εἰρήνη** καὶ **ἀγάπη** πληθυνθείη.
> ขอ**พระเมตตา สันติสุข** และ**ความรัก** จงทวีคูณแก่ท่านทั้งหลาย

| Element | Greek | Thai | Other Catholic Epistles |
|---|---|---|---|
| Mercy | ἔλεος | **พระเมตตา** (royal-prefix) | 1 PET 1:3 (ἔλεος in body, not greeting) |
| Peace | εἰρήνη | **สันติสุข** | corpus-locked across NT |
| Love | ἀγάπη | **ความรัก** | corpus-locked Johannine + Pauline |

Distinct from:
- **1 PET 1:2 + 2 PET 1:2:** χάρις + εἰρήνη (two-element)
- **JAS 1:1:** χαίρειν (greeting-formula only, no triad)
- **1/2/3 JN:** Johannine letters open without a Pauline-style greeting

**Editorial assessment.** The triad is Jude-distinctive. The royal-prefix on **พระเมตตา** marks divine-mercy correctly. The order (mercy → peace → love) escalates naturally and matches the Greek. The KD names the corpus-internal-link with 1 PET 1:2 / 2 PET 1:2 (πληθυνθείη verb-shared) while preserving the lexical-distinctiveness of the Jude-triad (mercy + love added). **Compliant.**

**Recommend: STABLE.** No corpus-doc lift needed; the triad is unique to Jude (no further test cases). The royal-prefix application on ἔλεος matches `divine_object_praise_verbs_2026-04.md` style for divine-attributes (royal-prefix on the divine-attribute, not on the verb).

---

## 7. OT-archetype triad at v.11 (Cain + Balaam + Korah) — **STABLE** (corpus-precedent + one hapax-name)

JUD 1:11 lists three OT-archetypes-of-rebellion in escalating order:

| Archetype | Greek | Thai (current) | OT reference | Cross-NT corpus |
|---|---|---|---|---|
| Cain | Κάϊν | **คาอิน** | GEN 4 | 1 JN 3:12 (corpus-locked) + HEB 11:4 |
| Balaam | Βαλαὰμ + μισθοῦ | **บาลาอัม + สินจ้าง** | NUM 22–24 | 2 PET 2:15 (corpus-locked) + REV 2:14 |
| Korah | Κόρε (HAPAX) | **โคราห์** | NUM 16 | only here in NT |

**Editorial assessment.** Each transliteration matches its OT-Thai-Christian standard (the LXX-via-Hebrew-via-Thai-OT chain). Cain matches 1 JN 3:12 corpus-precedent. Balaam matches 2 PET 2:15 corpus-precedent (verified — 2 PET 2:15 reads `บาลาอัมบุตรของเบโอร์`, identical Balaam-rendering). Korah is the NT-hapax-proper-noun; the Thai **โคราห์** matches the Hebrew קֹרַח via the standard Thai-OT form.

The triad-structure (jealous-violence + greed-corrupted-prophecy + religious-rebellion) is preserved by the parallel-syntax of the Greek (each headed by a dative-of-cause: τῇ ὁδῷ + τῇ πλάνῃ + τῇ ἀντιλογίᾳ) — the Thai uses three matched preposition-phrases (**ตามทาง ... ของ + เข้าสู่ความผิด ... ของ + ใน...ของ**) which preserves the parallelism.

**Recommend: STABLE.** No corpus-doc lift needed; standard OT-name transliterations + verse-level KDs cover the analysis. The three-archetypes pattern is unique to Jude.

---

## 8. Doxology vv. 24–25 — `μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ` — **DECIDE**

JUD 1:24–25 contains the famous closing doxology:

> Τῷ δὲ δυναμένῳ φυλάξαι ὑμᾶς ἀπταίστους καὶ στῆσαι κατενώπιον τῆς δόξης αὐτοῦ ἀμώμους ἐν ἀγαλλιάσει, **μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.**

> ขอพระเกียรติจงมีแด่พระองค์ ผู้ทรงสามารถปกป้องท่านไม่ให้สะดุดล้ม และทรงนำท่านมายืนต่อหน้าพระสิริของพระองค์อย่างปราศจากตำหนิด้วยความปีติยินดี **แด่พระเจ้าผู้ทรงเป็นพระผู้ช่วยให้รอดของเราแต่องค์เดียว โดยทางพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** ขอพระสิริ พระบารมี ฤทธานุภาพ และสิทธิอำนาจ จงมีแด่พระองค์ก่อนกาลทั้งสิ้น ทั้งบัดนี้และตลอดทุกยุคทุกสมัย อาเมน

**The interpretive question.** The phrase `μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν` ("to the only God our Savior, through Jesus Christ our Lord") admits two readings:

| Reading | Construal | Theological consequence |
|---|---|---|
| **Trinitarian-mediation (Eremos current)** | "the only God [the Father, the] Savior of-us, [acting] through Jesus Christ our Lord" | God-the-Father is Savior; salvation-mediated through Christ |
| **Subordinationist-flat** | "the only God [is] our Savior; [we know him] through Jesus Christ our Lord" | (compatible with #1; some early-modern critics read this as flat-monotheist anti-Christ-divinity, but mainstream Protestant reads it #1) |

The KD already disambiguates against the subordinationist-flat reading:

> Per uW: 'the only God' here = the Father (the qualifier emphasizes monotheism while preserving the Christological-mediation 'through Jesus Christ'). σωτήρ-of-Father → พระผู้ช่วยให้รอด (matches 1 TIM 1:1, 2:3, 4:10 'God-our-Savior' context — distinct from Granville-Sharp Christological-σωτήρ at 2 PET 1:1 + 1:11 + TIT 2:13).

**The translation surface.** The Thai uses the ordinary structure **แด่พระเจ้า ผู้ทรงเป็นพระผู้ช่วยให้รอดของเราแต่องค์เดียว โดยทางพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** ("to God, who is our Savior alone, through-the-way-of Jesus Christ our Lord"). The **โดยทาง** ("through-the-way-of," instrumental-mediation) preserves the Christological-mediation reading clearly. The **แต่องค์เดียว** ("alone, only one") preserves the monotheism-emphasis (μόνῳ).

**Editorial assessment.** The Thai is principled. The σωτῆρι-of-Father at v.25 is theologically-charged because it stands in deliberate-contrast to the Granville-Sharp σωτῆρ-of-Christ pattern at 2 PET 1:1, 1:11 + TIT 2:13 (where the SAME Greek-style construction `τοῦ θεοῦ ἡμῶν καὶ σωτῆρος` reads as "of-our-God-and-Savior" applying both titles to Christ). Jude's syntax DELIBERATELY avoids the Granville-Sharp pattern: `μόνῳ θεῷ σωτῆρι ... διὰ Ἰησοῦ Χριστοῦ` (God + Savior = Father; through Christ) — the Pastorals-aligned reading. The KD names this distinction explicitly.

**The DECIDE question.** Is the verse-level surfacing adequate, or should v.25 receive a `thai_summary` (currently null) explicating the Trinitarian-mediation construal + the deliberate-contrast with the Granville-Sharp pattern at 2 PET 1:1 + TIT 2:13? A typical Thai-Protestant reader who encounters the Eremos `แด่พระเจ้า ... โดยทางพระเยซูคริสต์` will likely read it correctly (the **โดยทาง** mediation-marker is unambiguous), BUT will not see the deliberate-contrast with the Granville-Sharp pattern unless the thai_summary names it.

**Two options:**

**Option A (current).** Bare doxology; verse-level KD carries the analysis; no thai_summary at v.25.

**Option B (proposed).** Add a `thai_summary` at v.25 noting:
1. "พระเจ้า" ในข้อนี้ = พระบิดา; "พระผู้ช่วยให้รอด" = บทบาทของพระบิดา; "โดยทางพระเยซูคริสต์" = บทบาทของพระบุตรในการช่วยให้รอด
2. โครงสร้างของยูดาสในที่นี้แตกต่างจาก 2 เปโตร 1:1 และทิตัส 2:13 ที่ทั้ง "พระเจ้า" และ "พระผู้ช่วยให้รอด" ระบุถึงพระคริสต์ (Granville-Sharp)
3. คำสรรเสริญสี่องค์ประกอบ (พระสิริ + พระบารมี + ฤทธานุภาพ + สิทธิอำนาจ) ครอบคลุมกาลเวลาสามมิติ (ก่อนกาลทั้งสิ้น + บัดนี้ + ตลอดทุกยุคทุกสมัย)

**Editorial recommendation lean.** Option B is more conservative for Thai-Protestant theological-clarity. The doxology is the climax of the letter and the single most-frequently-quoted Jude passage in liturgical contexts; a thai_summary that names the trinitarian-mediation reading bounds future misreading and harmonizes with the existing Pastorals-corpus surfacing.

**This is DECIDE** because the practical-pastoral-implications of the verse are substantive (closing doxology, frequently used in Thai-Christian liturgy) and the surfacing-strategy is the kind of judgment Ben should weigh, not the audit. (It is NOT, however, a code/translation change — the main `thai` field at vv. 24–25 stays as-is regardless.)

---

## 9. Pastoral triage at vv. 22–23 — three-fold mercy + ZEC 3 + LEV 13 imagery — **REVIEW**

JUD 1:22–23 closes the letter's body with a three-fold pastoral-triage of-doubting-believers:

| Category | Greek | Thai (current) |
|---|---|---|
| (a) doubting-mercy | οὓς μὲν ἐλεᾶτε διακρινομένους | จงเมตตาบางคนที่ยังไม่แน่ใจ |
| (b) fire-rescue | οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες | จงช่วยบางคนให้รอดโดยฉุดเขาออกจากไฟ |
| (c) fearful-mercy with-clothing-hatred | οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα | จงเมตตาบางคนด้วยความเกรงกลัว เกลียดชังแม้แต่เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง |

**The three-fold structure.** SBLGNT prints the three-fold reading; some-mss collapse to two clauses. Eremos correctly follows SBLGNT (RULES §0).

**The OT-imagery layer.** Two OT-imagery threads:
- **ZEC 3:2** ("a brand-plucked-from-the-fire") — same Joshua-the-high-priest scene as the JUD 1:9 Michael-rebuke citation (`Ἐπιτιμήσαι σοι κύριος`). The (b) fire-rescue clause echoes ZEC 3:2 thematically; corpus-internal-link with v.9's ZEC-citation.
- **ZEC 3:3–4 + LEV 13:47** — the priestly-defilement clothing-hatred imagery. The "stained-tunic" (`χιτῶνα ἐσπιλωμένον ἀπὸ τῆς σαρκός`) recalls Joshua's filthy-garments in Zechariah 3 + the leprous-cloth contagion-purity laws in Leviticus 13.

The (c) clause's σπίλος cognate (`ἐσπιλωμένον`) shares root-family with 2 PET 2:13 σπίλοι ("blots/stains") — corpus-internal-link.

**Editorial assessment.** The Thai preserves the three-fold structure cleanly. The **ฉุดเขาออกจากไฟ** ("snatch-them-out-of-fire") preserves the urgent-rescue imagery. The **เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง** ("garment stained-by-flesh") preserves the priestly-defilement imagery literally; this is a deliberately-startling Thai phrasing that mirrors the deliberately-startling Greek.

**The interpretive question.** A typical Thai reader encountering **เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง** at v.23 may not immediately decode the priestly-defilement reference (ZEC 3:3–4 + LEV 13:47). The verse `notes` carries the analysis but is invisible to typical readers. The Thai preserves the literal-imagery faithfully, but the OT-imagery-load is heavy and possibly cryptic without the cross-references.

**REVIEW question for Ben.** Should v.23 receive a `thai_summary` explicating:
1. The three-fold pastoral-triage structure (doubting + fire-rescue + fearful-mercy);
2. The OT-imagery layer (ZEC 3:3–4 priestly-defilement + LEV 13:47 leprous-cloth-purity);
3. The σπίλος cognate cross-corpus link with 2 PET 2:13.

— or is the bare-translation + verse-level KD adequate? The current rendering preserves the imagery faithfully; the question is whether the OT-cross-references should be surfaced for typical Thai-Protestant readers.

---

## 10. ψυχικοί at v.19 → คนฝ่ายโลก — **LOCKED ✓** (`psyche_vs_pneuma_anthropological_2026-04.md`)

JUD 1:19 contains a key NT-pneumatological-test verse:

> οὗτοί εἰσιν οἱ ἀποδιορίζοντες, **ψυχικοί**, πνεῦμα μὴ ἔχοντες.
> คนเหล่านี้เป็นผู้ที่ก่อความแตกแยก เป็น**คนฝ่ายโลก** ไม่มีพระวิญญาณ

The 1:19 KD names the corpus-lock:

> Per psyche_vs_pneuma_anthropological_2026-04.md: ψυχικός vs πνευματικός distinction. ψυχικός here-context = worldly-soulish (not-spiritual) → คนฝ่ายโลก. πνεῦμα-of-God → พระวิญญาณ (royal-prefix).

**Editorial assessment.** The lock is `psyche_vs_pneuma_anthropological_2026-04.md` (the broader anthropological doc) — applies cleanly. The Thai **คนฝ่ายโลก** ("worldly-soulish-persons") matches the corpus-precedent at 1 COR 2:14, 15:44, 46 and JAS 3:15 (the only NT occurrences of ψυχικός). The pneumatological-counterpoint at v.20 (build-up-in-faith + pray-in-Spirit) reinforces the structural-contrast.

**Recommend: LOCKED ✓.** Compliant.

---

## 11. 2 Peter cross-corpus parallel — verbal/imagery sharing — **LOCKED** (verified compliance)

Approximately TWO-THIRDS of Jude shares-vocabulary-or-imagery with 2 Peter 2–3. Verified cross-corpus compliance:

| JUD verse | Greek | Thai (JUD) | 2 PET parallel | 2 PET Thai | Cross-corpus status |
|---|---|---|---|---|---|
| 1:4 | δεσπότης | **องค์เจ้านาย** | 2 PET 2:1 same | **องค์เจ้านาย** | ✓ matched |
| 1:4 | ἀσέλγεια | **ความเสเพล** | 2 PET 2:2, 7, 18 same | **ความเสเพล** | ✓ matched |
| 1:6 | ζόφος | **ความมืด** | 2 PET 2:4, 17 same | **ความมืด** | ✓ matched |
| 1:7 | Σόδομα + Γόμορρα | **โสโดมและโกโมราห์** | 2 PET 2:6 same | **โสโดมและโกโมราห์** | ✓ matched |
| 1:8 | κυριότης + δόξας | **อำนาจ + เหล่าผู้ทรงสง่าราศี** | 2 PET 2:10 same | (same registers) | ✓ matched |
| 1:10 | ἄλογα ζῷα | **สัตว์ป่าที่ปราศจากเหตุผล** | 2 PET 2:12 same | (same) | ✓ matched |
| 1:11 | Βαλαὰμ + μισθοῦ | **บาลาอัม + สินจ้าง** | 2 PET 2:15 + 2:13 | **บาลาอัม + ค่าจ้าง** | ✓ same-name; μισθός vs μισθός variant |
| 1:12 | συνευωχέομαι | **ร่วมรับประทานอาหาร** | 2 PET 2:13 same | (same) | ✓ matched |
| 1:13 | ζόφος + σκότος | **ความมืดมิดที่ดำสนิท** | 2 PET 2:17 same | **ความมืดมิดที่ดำสนิท** | ✓ matched (phrase-locked) |
| 1:16 | ὑπέρογκος | **อวดโอ่** | 2 PET 2:18 same | **อวดโอ่** | ✓ matched |
| 1:18 | ἐμπαῖκται | **คนเย้ยหยัน** | 2 PET 3:3 same | (same) | ✓ matched |

**Editorial assessment.** Cross-corpus compliance is exact for all shared-vocabulary. The phrase-consistency check (8 audited locks) passes. No drift. The KDs at each Jude verse explicitly cite the 2 PET corpus-internal-link, making the relationship transparent.

The single minor split: JUD 1:11 μισθοῦ → **สินจ้าง** vs 2 PET 2:15 (where the Greek reads μισθὸν ἀδικίας → **ค่าจ้างแห่งความอธรรม**, "wages of unrighteousness"). The Greek is identical-lemma but in different syntactic constructions; the Thai split (สินจ้าง vs ค่าจ้าง) is principled — สินจ้าง is the Hebraic-Balaam-reward register; ค่าจ้าง is the more-generic Pauline-wages register. Defensible at the verse-level.

**Recommend: LOCKED.** No corpus-doc lift needed — the cross-corpus consistency is verifiable per-verse, and the cross-corpus-link is documented in each KD. The Jude → 2 Peter direction-of-dependence question is debated in scholarship; the translation does not commit to a direction (correctly).

---

## 12. Inherited locks — all compliant

| Lock | JUD evidence | Status |
|---|---|---|
| `psyche_vs_pneuma_anthropological_2026-04.md` | v.19 → **คนฝ่ายโลก**. See §10. | **LOCKED ✓** |
| `spiritual_beings_hierarchy_2026-05.md` | v.6 (ἀγγέλους + ἀρχήν → **ทูตสวรรค์** + **ตำแหน่ง**); v.8 (κυριότης + δόξας → **อำนาจ** + **เหล่าผู้ทรงสง่าราศี**); v.9 (Μιχαὴλ ἀρχάγγελος → **อัครเทวดามีคาเอล**); v.14 (ἁγίαι μυριάδες → **ผู้บริสุทธิ์มากมาย**). All compliant. | **LOCKED ✓** |
| `pastoral_corpus_locks_2026-05.md` (πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์) | v.20 → **พระวิญญาณบริสุทธิ์**. Compliant. | **LOCKED ✓** |
| `divine_object_praise_verbs_2026-04.md` (royal-prefix on divine-objects) | v.2 พระเมตตา; v.21 พระเมตตาของพระเยซูคริสต์; v.24 พระเกียรติ + พระสิริ; v.25 พระเจ้า + พระสิริ + พระบารมี + ฤทธานุภาพ + สิทธิอำนาจ. All royal-prefixed. | **LOCKED ✓** |
| ἀγάπη → ความรัก / ἀγαπητοί → ท่านที่รัก | v.1 (ἠγαπημένοις → ทรงเป็นที่รัก); v.2 (ἀγάπη → ความรัก); v.3, 17, 20 (Ἀγαπητοί → ท่านที่รัก). Uniform. | **LOCKED** (corpus precedent) |
| ζωὴ αἰώνιος → ชีวิตนิรันดร์ | v.21 → **ชีวิตนิรันดร์**. Compliant. | **LOCKED** (corpus precedent) |
| ἄγγελος → ทูตสวรรค์ | v.6 → **ทูตสวรรค์**. Compliant. | **LOCKED** (corpus precedent) |
| διάβολος → มาร | v.9 → **มาร**. Compliant. | **LOCKED** (corpus precedent) |
| οὐαί → วิบัติ (Synoptic woe-formula) | v.11 → **วิบัติ**. Compliant with MAT/MRK/LUK + REV woe-passages. | **STABLE** (corpus precedent) |
| εἰρήνη → สันติสุข | v.2 → **สันติสุข**. Compliant. | **LOCKED** (corpus precedent) |
| πίστις → ความเชื่อ | v.3 (ἅπαξ παραδοθείσῃ ... πίστει → ความเชื่อที่ทรงมอบ ... ครั้งเดียวสำหรับทุกยุคทุกสมัย); v.20 (ἁγιωτάτῃ ὑμῶν πίστει → ความเชื่ออันบริสุทธิ์ที่สุด). | **LOCKED** (corpus precedent) |
| σωτηρία → ความรอด | v.3 (κοινῆς ἡμῶν σωτηρίας → ความรอดที่เรามีร่วมกัน). Compliant. | **LOCKED** (corpus precedent) |
| ἁμαρτωλός / ἁμαρτία → คนบาป / ความบาป | v.15 → **คนบาป**. Compliant. | **LOCKED** (corpus precedent) |
| ἅγιος (substantive) → ธรรมิกชน / ผู้บริสุทธิ์ | v.3 (ἁγίοις → ธรรมิกชนทั้งหลาย); v.14 (ἁγίαι μυριάδες → ผู้บริสุทธิ์มากมาย). Two registers correctly distinguished (saints-as-people vs holy-ones-angelic-army-or-saints). | **STABLE** (corpus precedent) |
| ἀσέβεια / ἀσεβής → ความอธรรม / คนอธรรม | vv.4, 15 (×3), 18 → **ความอธรรม + คนอธรรม** uniform. | **STABLE** (corpus precedent) |
| ἀσέλγεια → ความเสเพล | v.4 → **ความเสเพล**. Compliant with 2 PET 2:2, 7, 18. | **LOCKED** (corpus precedent) |
| κρίσις → การพิพากษา | v.6, 9, 15 → **การพิพากษา**. Compliant. | **LOCKED** (corpus precedent) |
| ἀρχάγγελος → อัครเทวดา | v.9 → **อัครเทวดา**. Compliant with 1 TH 4:16. | **STABLE** (corpus precedent) |
| Sodom + Gomorrah / proper-noun OT-place transliterations | v.7 → **โสโดมและโกโมราห์**. Compliant with 2 PET 2:6 + ROM 9:29 + MAT 10:15. | **LOCKED** (corpus precedent) |
| Cain transliteration | v.11 → **คาอิน**. Compliant with 1 JN 3:12 + HEB 11:4. | **STABLE** (corpus precedent) |
| ἀΐδιος → นิรันดร์ | v.6 → **นิรันดร์**. Compliant. | **STABLE** (corpus precedent) |
| αἰώνιος → นิรันดร์ | v.7 → **นิรันดร์**. Compliant. | **LOCKED** (corpus precedent) |
| ἔλεος → พระเมตตา (royal-prefix divine-mercy) | v.2 → **พระเมตตา**; v.21 → **พระเมตตาของพระเยซูคริสต์**. Compliant. | **LOCKED** (corpus precedent) |
| ἐπιθυμία → ตัณหา | vv. 16, 18 → **ตัณหา**. Compliant. | **LOCKED** (corpus precedent) |
| ποιμαίνω → เลี้ยงดู | v.12 → **เลี้ยงดู** (ironic-self-feeding). Compliant. | **STABLE** (corpus precedent) |
| ἐποικοδομέω → เสริมสร้าง | v.20 → **เสริมสร้าง**. Compliant with EPH 2:20. | **LOCKED** (corpus precedent) |
| πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ | v.20 → **พระวิญญาณบริสุทธิ์**. Compliant. | **LOCKED** (corpus precedent) |
| Pre-eternity + present + eternal-future temporal-doxology | v.25 → **ก่อนกาลทั้งสิ้น + บัดนี้ + ตลอดทุกยุคทุกสมัย**. Three-fold-temporal preserved. | **STABLE** (corpus precedent) |
| ἀμήν → อาเมน | v.25 → **อาเมน**. Compliant. | **LOCKED** (corpus precedent) |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** — Jude has no SBLGNT-omits-mainstream-includes variants. The v.5 textual variant (Ἰησοῦς vs κύριος) is a word-substitution, not an inclusion-omission. The vv. 22–23 variants are SBLGNT-three-fold vs Byzantine-two-fold, also a structural-variant not an absence. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — Jude is an epistle, not narrative. | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in Jude. | **LOCKED (N/A)** |
| `narrator_vs_character_voice_2026-04.md` | N/A — Jude has no extended dialogue requiring narrator-vs-character distinction. The two direct-citations (v.9 Michael-quote; vv.14–15 Enoch-quote) are quoted-speech rather than character-voice in narrative. | **LOCKED (N/A)** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic in Jude. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — no Son-of-Man title. | **LOCKED (N/A)** |
| `parousia_christou_2026-05.md` | v.21 (προσδεχόμενοι τὸ ἔλεος τοῦ κυρίου ... εἰς ζωὴν αἰώνιον) — eschatological-mercy-of-Christ awaiting; verbal-link to παρουσία expectation but no παρουσία-lemma occurs. | **LOCKED (N/A; thematic-only)** |
| `epiphaneia_christou_2026-05.md` | N/A — no ἐπιφάνεια-lemma. | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman-titles in Jude. | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | N/A — no non-divine honorific-bearer. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | N/A. | **LOCKED (N/A)** |
| OT citations (`data/nt_ot_citations.json`) | v.9 ZEC 3:2 LXX (recorded as DB entry). v.7 Sodom-Gomorrah is allusion, not citation. v.11 Cain/Balaam/Korah are allusions, not citations. | **STABLE** (one DB entry) |

---

## 13. v.5 NUM 14 wilderness-destruction tradition + v.6 Genesis 6 fallen-angels tradition + v.7 Sodom — three OT-judgment archetypes — **STABLE**

JUD 1:5–7 lists three OT-judgment-archetypes in escalating order:

| Verse | Archetype | OT reference | Pseudepigrapha-tradition support |
|---|---|---|---|
| 1:5 | Wilderness-unbelievers-destroyed | NUM 14 | (none specifically) |
| 1:6 | Fallen-angels-bound | GEN 6:1–4 (the "sons of God" tradition) | 1 Enoch 6–21 |
| 1:7 | Sodom-Gomorrah-fire | GEN 19 | (cf. Wisdom 10:6–7) |

This serves as a structural-parallel to the v.11 OT-archetype-triad (Cain + Balaam + Korah) — Jude bookends his polemic with two OT-archetype clusters. The vv. 5–7 cluster targets **judgment-already-executed** (past-tense OT-judgments); the v.11 cluster targets **archetypal-figures-of-rebellion** (Cain + Balaam + Korah as patterns).

**Editorial assessment.** Each archetype-rendering is compliant with corpus-precedent (verified via grep). The vv. 6–7 fallen-angels-pursuing-strange-flesh tradition (`σαρκὸς ἑτέρας` → **เนื้อหนังที่ผิดธรรมชาติ**) preserves the angelic-human boundary-violation reading per the Genesis 6 + 1 Enoch tradition, with the verse-level KD naming the source. This is the most-interpretively-charged reading in the cluster (some commentators read v.7 σαρκὸς ἑτέρας as homosexuality-only, others as angel-human boundary-violation; Eremos's **เนื้อหนังที่ผิดธรรมชาติ** is the broader "unnatural-flesh" rendering, defensible either way and not narrowing). Compliant.

**Recommend: STABLE.** No corpus-doc lift; the verse-level analysis is adequate. The v.6 fallen-angels-tradition allusion to 1 Enoch 6–21 dovetails with the v.14–15 direct-citation of 1 Enoch 1:9 — both should be cross-referenced if the recommended `pseudepigrapha_citations_2026-05.md` doc is created (§2 above). The v.6 allusion is more allusive than the v.14 citation; treating them differentially in the corpus doc is the principled approach.

---

## Mechanical (§1) — **all green**

- 1/1 chapter: `output/check_reports/jude_01_review.md` ✓
- 1/1 chapter: `output/back_translations/jude_01.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-228-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only unrelated paratext exports + 1JN textual_variants file from earlier audits; no JUD source-file dirt

---

## Pre-existing docs affirmed / unchanged

All 47 docs in `docs/translator_decisions/` are unchanged by Jude. The audit confirms compliance with the Pastoral + Catholic-Epistle + Petrine + Johannine + general locks. Inherited recommendations from earlier audits remain valid.

JUD-distinctive new corpus-doc recommendation:

1. **NEW `docs/translator_decisions/pseudepigrapha_citations_2026-05.md`** (§2) — formalizes the surfacing-strategy for direct citations of non-canonical Jewish-tradition (JUD 9 Assumption-of-Moses + JUD 14–15 1-Enoch). Cross-references the 2 PET 2:4 fallen-angels-tradition allusion. Closes the NT corpus on this question (no further test cases).

---

## Flagged for Ben's attention

### A. Pseudepigrapha-citation surfacing strategy (JUD 9 + JUD 14–15) — **DECIDE** (§2)
Both verses already carry substantial thai_summary entries explaining the source + the Protestant interpretive frame. The DECIDE question is whether to formalize the strategy as a new corpus doc (`pseudepigrapha_citations_2026-05.md`) — this is the single biggest editorial question of Jude and the reason this audit recommends Ben's input rather than the audit deciding. Lean: yes, write the corpus doc.

### B. Doxology v.25 Christological-mediation surfacing — **DECIDE** (§8)
The σωτῆρι-of-Father reading is theologically-charged (deliberate-contrast with 2 PET 1:1 + TIT 2:13 Granville-Sharp Christological-σωτῆρι). Should v.25 receive a thai_summary explicating the trinitarian-mediation construal + the deliberate-contrast pattern? Lean: yes, given the doxology's liturgical-frequency.

### C. Textual variant JUD 5 Ἰησοῦς vs κύριος — **STABLE → LOCKED** (§1)
The most-charged textual variant in the NT. RULES §0 governs (SBLGNT-strict). The thai_summary is well-crafted and adequate. **No change required.**

### D. ἐπαγωνίζομαι v.3 → ต่อสู้อย่างเข้มแข็ง — **REVIEW** (§4)
Jude's famous programmatic-statement. Current rendering preserves the intensifier (อย่างเข้มแข็ง) which simpler Thai versions drop. Defensible as-is; alternatives **ต่อสู้อย่างหนักแน่น** / **ต่อสู้อย่างไม่ลดละ** are more theologically-elevated.

### E. πληθυนθείη Catholic-Epistle greeting verb cross-corpus split — **REVIEW** (§5)
1 PET 1:2 → **ทวียิ่งขึ้น** vs 2 PET 1:2 + JUD 1:2 → **ทวีคูณ**. Minor cross-corpus inconsistency; principled either way; tolerated by phrase-consistency check. Recommendation: harmonize 1 PET 1:2 → ทวีคูณ to match 2 PET + JUD (one-token change in one verse).

### F. Pastoral triage at vv. 22–23 — **REVIEW** (§9)
Should v.23 receive a thai_summary explicating the three-fold structure + the OT-imagery layer (ZEC 3:3–4 + LEV 13:47 priestly-defilement)? The Thai preserves the literal-imagery faithfully; the question is whether the OT-cross-references should be surfaced for typical readers.

### G. New corpus-doc lifts (in priority order)
1. **NEW `pseudepigrapha_citations_2026-05.md`** (§2) — write FIRST; closes the NT corpus on this question. Single-author, ~1 hour.

(Inherited from prior audits — not Jude-driven but listed for completeness:)
2. **Brief amendment to `poimen_episkopos_register_split_2026-05.md`** for the Johannine-letter `Ὁ πρεσβύτερος` self-designation (overdue from 2JN/3JN audits) — N/A in Jude, still pending.
3. **Brief amendment to `hygiaino_sound_doctrine_2026-05.md`** for the 3 JN 1:2 literal-physical-health sub-case — N/A in Jude, still pending.
4. **NEW `propempo_missionary_sending_2026-05.md`** (recommended by 3JN audit) — N/A in Jude, still pending.

### H. External AI review (§3 of checklist) — **pending**
Recommended before `book-jude-v1` tag. Suggested 2-cluster external AI packet:
1. **JUD 1–11** — opening + greeting-triad + programmatic-statement (ἐπαγωνίζομαι) + textual-variant v.5 + OT-judgment-archetypes (vv.5–7) + libertine-pattern (v.8) + Michael-rebuke (v.9 + Assumption-of-Moses citation) + animal-parallel (v.10) + Cain-Balaam-Korah triad (v.11)
2. **JUD 12–25** — love-feast intrusion (v.12) + waterless-cloud + autumn-tree + foam-waves + wandering-stars (vv.12–13) + 1-Enoch-citation (vv.14–15) + grumblers + scoffers (vv.16, 18) + soulish-without-Spirit (v.19) + pneumatological-positive (vv.20–21) + pastoral-triage (vv.22–23) + closing-doxology (vv.24–25)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/1TH/1JN/2JN/3JN pattern. Foreground items A (pseudepigrapha-citations), B (doxology v.25), F (pastoral-triage v.23) — the rest of Jude is corpus-derivative or RULES §0-determined and well-locked.

---

## Recommendation

**Jude ships in strong corpus-hygiene shape.** The translator handled the lexically-distinctive material with discipline: the ~16 NT-hapaxes (highest per-verse density in the NT after 3 JN) all received verse-level KDs per RULES §5; the most-charged textual variant in the NT (v.5 Ἰησοῦς vs κύριος) received transparent thai_summary surfacing per RULES §0; the two NON-CANONICAL pseudepigrapha-citations (v.9 + vv.14–15) received substantial thai_summary entries with the Protestant interpretive frame (citation ≠ canonical-status); the 2-Peter cross-corpus parallel material (~two-thirds of the letter) is uniformly compliant with the 2 Peter 2 KDs.

The DECIDE items (A — pseudepigrapha-strategy formalization; B — doxology v.25 surfacing) are not translation changes — they are corpus-doc / thai_summary-additions. The verse-level translations stand as principled regardless of how Ben resolves them.

Tag `book-jude-v1` after:
1. Ben's decision on **A** (pseudepigrapha-citations corpus doc — new lock or status quo) and **B** (doxology v.25 thai_summary — added or status quo); both resolve without code/translation change.
2. Ben's confirmation on **D, E, F** (REVIEW items).
3. **Item G.1** (new `pseudepigrapha_citations_2026-05.md` corpus doc) — ~1 hour; can be batched with the 2JN/3JN-pending corpus-doc lifts in a single `docs/translator_decisions/` PR.
4. External AI sanity-check (§H) via Grok / ChatGPT / Gemini.

Jude is the LAST OF THE CATHOLIC EPISTLES (after 1 PET, 2 PET, 1 JN, 2 JN, 3 JN, JAS); the Catholic-Epistle corpus closes here. Revelation is downstream and inherits the now-fully-ratified Catholic-Epistle lock-set. The audit confirms Jude is the SINGLE NT BOOK with direct-pseudepigrapha-citations (closes the corpus); the only NT book with the v.5 Ἰησοῦς-as-Exodus-deliverer Christological reading at the textual-variant level (closes the corpus); a major contributor to the spiritual-beings-hierarchy lock (vv.6 + 8 + 9 + 14, ratifying `spiritual_beings_hierarchy_2026-05.md`).
