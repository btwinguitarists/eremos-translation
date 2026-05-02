# Romans — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 16 chapters (433 verses; ~1100+ verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (28 docs).
**Trigger:** ROM 16 shipped (commit `8403142`); per `docs/END_OF_BOOK_CHECKLIST.md`. Doxology vv.25–27 backfilled 2026-05-02 as Tier-3 ⟦…⟧ block (parallel to Mark 16:9–20) per the systemic inclusion-variant remediation; v.24 grace-formula retained per SBLGNT.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 16/16 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-178-chapter / 6198-verse corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` clean (post-doxology-backfill).
- **Romans is the project's THEOLOGICAL CENTER OF MASS** — 16 chapters that compound every Pauline-vocabulary lock the corpus has built since Galatians. The δικαιόω forensic-declarative lock (`dikaioo_dikaiosyne_family_2026-05.md`) was itself **born** mid-Romans (the 13-verse Rom 1–5 backfill on 2026-05-01 corrected the imputation-rendering drift inherited from THSV1971). That backfill held: every δικαιόω instance from Rom 2:13 through Rom 8:33 now uses the locked **ทรงถูกประกาศว่าชอบธรรม** (passive) / **ทรงประกาศว่าชอบธรรม** (active) construction, with the two principled exceptions (Rom 3:4 LXX-divine-vindication, Rom 6:7 ἀπό-discharge idiom) correctly applied.
- **Romans confirms continuity with the GAL + 1TH inherited Pauline locks.** The four cruxes flagged in the GAL audit as "lift to corpus doc before Romans 1" — πίστις-Χριστοῦ objective genitive; δικαιόω forensic-declarative; νόμος multi-sense single-rendering; στοιχεῖα — landed correctly in Romans (στοιχεῖα is N/A; the other three are uniformly applied). The 1TH audit's eschatology-vocabulary cluster (παρουσία, ἁγιασμός, ἡμέρα κυρίου, ὀργή) extends into Romans cleanly, with **ὀργή** the lemma that COMPOUNDS most dramatically here (6 occurrences vs. 3 in 1TH).
- **9 inherited Synoptic / John / Acts / GAL / 1TH locks verified compliant** in Romans (ἐκκλησία, ἔθνος, narrator-κύριος, vocative κύριε N/A, divine-object praise verbs implicitly N/A, narrator-vs-character voice, Aramaic transliterations [Rom 8:15 Αββα ὁ πατήρ], honorifics, OT-citation flagging — see §16–17).
- **3 cross-cutting Pauline patterns are STABLE-but-undocumented at corpus level** (νόμος Pauline two-rendering: ธรรมบัญญัติ for Mosaic Torah / กฎ for inner-principle, **first-systematized in Rom 7:21–8:2**; υἱοθεσία first-densely-occurring at Rom 8:15/23, 9:4 → **สิทธิ์การเป็นบุตร**; σάρξ Pauline ethical-negative dominant at Rom 7–8 → **เนื้อหนัง** uniform). All three need corpus-doc lift before 1–2 Corinthians; νόμος especially before 1 Cor 9:20–21.
- **5 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: σάρξ multi-sense single-rendering at Rom 7–8; υἱοθεσία rendering choice; the πνεῦμα/πνεύματι distribution at Rom 8:16; the παῖς-vs-υἱός register split for ἀδελφοί/τέκνα at Rom 8:14–17; λογικὴν λατρείαν at Rom 12:1).
- **5 items flagged DECIDE** (Rom 9:5 christological doxology — punctuation/syntax crux; Rom 10:4 τέλος terminal-vs-goal; Rom 11:26 "all Israel" three-way reading; Rom 16:1 Phoebe διάκονος generic-vs-office; Rom 16:7 Junia + ἐπίσημοι-ἐν-τοῖς-ἀποστόλοις).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. δικαιόω / δικαίωσις / δικαίωμα-as-verdict — forensic-declarative — **LOCKED ✓**

The lock-creating book. The Romans 1–5 backfill on 2026-05-01 (13 verses corrected from `ทรงนับว่าชอบธรรม` to `ทรงประกาศว่าชอบธรรม`) is documented in `docs/translator_decisions/dikaioo_dikaiosyne_family_2026-05.md`.

**Rom 6–16 compliance audit (post-lock):**

| Verse | Greek | Thai | Form |
|---|---|---|---|
| Rom 6:7 | δεδικαίωται ἀπό | **เพราะคนที่ตายแล้วก็พ้นจากบาป** | EXCEPTION 2 (ἀπό-discharge idiom — locked) ✓ |
| Rom 8:30 (×2) | ἐδικαίωσεν | **ทรงประกาศว่าชอบธรรม** | active aor — locked form ✓ |
| Rom 8:33 | δικαιῶν | **ทรงเป็นผู้ทรงประกาศว่าชอบธรรม** | active subst.ptc — locked form ✓ |

Plus the LOCK-DEFINING verses (Rom 2:13, 3:20, 3:24, 3:26, 3:28, 3:30 ×2, 4:2, 4:5, 4:25, 5:1, 5:9, 5:16, 5:18) all using the locked rendering.

**Rom 4 λογίζομαι separation preserved:** the 11 occurrences of λογίζομαι in Rom 4 (4:3, 4:4, 4:5, 4:6, 4:8, 4:9, 4:10, 4:11, 4:22, 4:23, 4:24) all use **นับ** ("count/reckon"); δικαιόω at Rom 4:2, 4:5 uses **ประกาศ**. The two-step Pauline argument (verdict-act vs accounting-act) is lexically distinct in Thai exactly per the lock's load-bearing test.

**STABLE: glossary.json** δικαιόω entry should reflect `primary_thai: ถูกประกาศว่าชอบธรรม` after this audit if not already.

**LOCKED** ✓ — no action.

---

## 2. πίστις Χριστοῦ — objective-genitive default — **STABLE (recommend new doc — high-priority before 1 Cor)**

Despite GAL audit §1 flagging this as DECIDE-before-tagging, no `pistis_christou_*.md` corpus doc was written. Romans makes the objective-genitive choice **even more dispositive** because Rom 3:21–4:25 is the doctrinal-load-bearing passage for justification-by-faith.

**Romans evidence — uniform objective genitive (ใน, "faith IN"):**

| Verse | Greek | Thai | Genitive |
|---|---|---|---|
| Rom 3:22 | διὰ πίστεως Ἰησοῦ Χριστοῦ | **ทางความเชื่อในพระเยซูคริสต์** | objective |
| Rom 3:26 | τὸν ἐκ πίστεως Ἰησοῦ | **ผู้ที่มีความเชื่อในพระเยซู** | objective |
| Rom 5:1 | δικαιωθέντες ἐκ πίστεως | **เมื่อเราทรงถูกประกาศว่าชอบธรรมโดยความเชื่อ** | objective (no Christou-genitive here; faith-act) |

Subjective-genitive constructions (Rom 1:8 πίστις ὑμῶν "your faith") use **ของ** correctly; no collision with the Christou-genitive lock.

**Editorial assessment:** The choice is uniform across Galatians + 1 Thess + Romans now. The GAL audit's recommended doc (`pistis_christou_2026-04.md`) was never written; Romans confirms the choice is corpus-stable. The principled alternative (subjective genitive — "the faithfulness OF Christ") is not represented in any verse — there is no ambiguous-rendering for the external AI to interrogate.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/pistis_christou_2026-05.md` after Ben's confirmation. The doc should:
1. Lock πίστις + Χριστοῦ-genitive → **ความเชื่อใน + พระเยซู / พระคริสต์** (objective-genitive default)
2. Cite Rom 3:22, 3:26 as the locking precedent (compounding GAL 2:16, 3:22 from `ai_review_response_GAL_2026-05-01.md`)
3. Reject the subjective-genitive alternative (Wright/Hays/Campbell) per RULES §0 evangelical-Protestant alignment
4. Note the rendering's interaction with Rom 4 πίστις-of-Abraham (subjective: ของอับราฮัม) — still ของ, no ambiguity
5. Forward-pertinent for Phil 3:9 (ἐκ θεοῦ δικαιοσύνην ἐπὶ τῇ πίστει — second-most-debated πίστις-Χριστοῦ-equivalent)

---

## 3. νόμος — Pauline two-rendering policy (ธรรมบัญญัติ vs กฎ) — **STABLE (undocumented; recommend new doc — HIGHEST forward priority)**

Romans has **74 occurrences of νόμος across 38 verses** — the densest νόμος-text in the entire NT, surpassing GAL (34 occurrences). The GAL audit §3 recommended `nomos_pauline_*.md` before Rom 7-8; the doc was never written. Romans 7:21–8:2 is exactly the cluster the GAL audit predicted: **5 νόμος in 4 verses, with 4 distinct senses.**

**Two-rendering policy (NEW pattern — distinct from GAL's single-rendering):**

| Sense | Thai | Romans evidence |
|---|---|---|
| Mosaic Torah / Pentateuch (the law-code or law-as-canonical-text) | **ธรรมบัญญัติ** | Rom 2:12, 13, 14, 17, 18, 20, 23, 25 (×2), 26, 27 (×2); 3:19 (×2), 20, 21, 27, 28, 31 (×2); 4:13, 14, 15 (×2), 16; 5:13, 20; 6:14, 15; 7:1 (×2), 2, 3, 4, 5, 6, 7 (×2), 8, 9, 12, 14, 16, 22, 25; 8:3, 4, 7; 9:31 (×2); 10:4, 5; 13:8, 10 — ~50 occurrences uniform |
| Inner-principle / governing-pattern (Pauline-rhetorical νόμος-of-X-genitive) | **กฎ** | Rom 7:21 (νόμος "the law" — "I find this law"); 7:23 (νόμος ἕτερος "another law", νόμος τοῦ νοός "law of the mind", νόμος τῆς ἁμαρτίας "law of sin"); 7:25 (νόμῳ ἁμαρτίας "law of sin"); 8:2 (νόμος τοῦ πνεύματος τῆς ζωῆς, νόμος τῆς ἁμαρτίας καὶ τοῦ θανάτου); 9:31 (the second occurrence — νόμον δικαιοσύνης "law of righteousness" — *check this — likely ธรรมบัญญัติ*) |
| Mosaic-Torah even when in a νόμος-of-X compound | **ธรรมบัญญัติ** | Rom 7:25b (νόμῳ θεοῦ "law of God" — Mosaic-Torah-affirmed-even-in-struggle) |

**The Rom 7:21–8:2 5-νόμος cluster — verse-by-verse:**

> Rom 7:21 (νόμος "this law/principle") → **กฎนี้** ("this law" = the principle-being-discovered, NOT Mosaic Torah)
> Rom 7:23 (νόμος ἕτερος / νόμος τοῦ νοός / νόμος τῆς ἁμαρτίας) → **กฎอีกอันหนึ่ง / กฎแห่งจิต / กฎแห่งบาป** (three principle-laws)
> Rom 7:25a (νόμος θεοῦ) → **ธรรมบัญญัติของพระเจ้า** (Mosaic-Torah; Paul's mind-aligned-with-God's-law)
> Rom 7:25b (νόμος ἁμαρτίας) → **กฎแห่งบาป** (principle-of-sin-in-the-flesh)
> Rom 8:2 (νόμος τοῦ πνεύματος τῆς ζωῆς ... νόμος τῆς ἁμαρτίας καὶ τοῦ θανάτου) → **กฎของพระวิญญาณแห่งชีวิต ... กฎแห่งบาปและความตาย** (two principle-laws)

The 7:25 KD makes the split explicit: **ธรรมบัญญัติของพระเจ้า** for the Mosaic-Torah νόμος + **กฎแห่งบาป** for the principle-νόμος, **in the same Greek sentence**.

**Editorial significance:** This is a **principled departure from GAL's single-rendering policy**. GAL §3 (audit) defended single-rendering ธรรมบัญญัติ across all 4 senses to preserve the Pauline punning. Romans introduces a NEW disambiguation: ธรรมบัญญัติ ↔ กฎ tracks the Mosaic-Torah-vs-inner-principle split. This is theologically sharper but loses the Greek's single-νόμος rhetorical force.

The two-rendering choice is **defensible** — Romans 7's "law of sin" / "law of God" / "law of mind" is so semantically diverse that flat ธรรมบัญญัติ everywhere would obscure that Paul means **different things** by νόμος in adjacent clauses. But this contradicts the GAL audit's recommendation; the discrepancy needs to be reconciled in the corpus doc.

**Recommend: STABLE; new doc** `docs/translator_decisions/nomos_pauline_2026-05.md` — **highest forward priority** before 1 Cor 9:20–21 (ὑπὸ νόμον / ἀνομοι / ἔννομος Χριστοῦ — the densest non-Romans νόμος cluster). The doc should:
1. Lock the two-rendering split: **ธรรมบัญญัติ** for Mosaic-Torah + Pentateuch-as-canon; **กฎ** for inner-principle / governing-pattern
2. Cite Rom 7:21–8:2 as the locking precedent (5 νόμος, 4 senses, 2 Thai renderings)
3. Document the SPLIT-FROM-GAL-PRECEDENT — GAL used single-rendering; Romans diverges. Resolve by amending GAL audit §3's recommendation, OR mark Romans as the principled-departure for inner-principle νόμος-of-X compounds while keeping single-rendering for νόμος-by-itself.
4. Forward-pertinent: 1 Cor 9:20–21 (νόμον ... ἔννομος Χριστοῦ "law of Christ" — gets **กฎของพระคริสต์** likely); Gal 6:2 (νόμον τοῦ Χριστοῦ — currently rendered ธรรมบัญญัติ; reconsider per the new lock); Heb 7:12, 7:16, 8:10 (Mosaic-vs-new-covenant νόμος).

---

## 4. σάρξ — Pauline ethical-negative dominant — **STABLE (undocumented; recommend new doc)**

Romans has **23+ σάρξ occurrences across 21 verses** — the densest σάρξ-text in the NT (surpassing GAL's 17). Rom 7–8 (esp. Rom 8:3–13) is the canonical "the flesh ↔ the Spirit" antagonism passage. The GAL audit §6 flagged sarx_pauline as STABLE-recommend-doc; that doc was never written.

**Romans evidence — uniform เนื้อหนัง across 5 senses:**

| Sense | Thai | Romans verses |
|---|---|---|
| Genealogical-physical (κατὰ σάρκα = "according to physical descent") | **ตามเนื้อหนัง** | Rom 1:3 (Christ from David's seed κατὰ σάρκα); 4:1 (Abraham κατὰ σάρκα); 9:3 (Paul's συγγενῶν κατὰ σάρκα); 9:5 (Christ κατὰ σάρκα); 9:8 (τέκνα τῆς σαρκός vs τέκνα τῆς ἐπαγγελίας) |
| Hebraic idiom "no flesh" (= no human being, OT-citation echo) | **เนื้อหนังใด** | Rom 3:20 (Ps 143:2 LXX — "no flesh will be justified") |
| Anthropological-neutral "weakness of the flesh" | **เนื้อหนัง** | Rom 6:19 (διὰ τὴν ἀσθένειαν τῆς σαρκός); 7:5 (ἐν τῇ σαρκί before-Christian-conversion); 7:18, 7:25 (ἐν τῇ σαρκί μου); 13:14 (τῆς σαρκὸς πρόνοιαν) |
| Ethical-negative "the flesh" = sinful nature | **เนื้อหนัง** | Rom 7:14 (ἐγὼ σάρκινός εἰμι); 7:25b (τῇ σαρκί νόμῳ ἁμαρτίας); 8:3 (×3 ἐν ὁμοιώματι σαρκὸς ἁμαρτίας ... ἐν τῇ σαρκί); 8:4–9 (×6 κατὰ σάρκα ↔ κατὰ πνεῦμα antagonism); 8:12, 8:13 (×2 κατὰ σάρκα living-vs-killing) |
| Outward-physical/circumcision marker | **เนื้อหนัง** | Rom 2:28 (ἐν σαρκὶ περιτομή — circumcision in the flesh) |

The Rom 8:5–9 ethical-antagonism cluster is the densest σάρξ-text in the NT. Thai uniformly **เนื้อหนัง** with the contrast borne by κατὰ σάρκα ↔ κατὰ πνεῦμα → **ตามเนื้อหนัง ↔ ตามพระวิญญาณ**.

**Editorial assessment:** Single-rendering uniform across all 5 senses, exactly per the GAL §6 policy. The Rom 1:3 + 9:5 (genealogical-Christ) and Rom 8:3 (ethical-Christ-in-likeness-of-sinful-flesh) co-occurrence in the same book is theologically loaded — Christ takes ON σάρξ in the genealogical sense without taking ON σάρξ in the ethical-sinful sense. The Thai uniform เนื้อหนัง forces the reader to disambiguate by context, exactly as the Greek does.

**Recommend: STABLE; new doc** `docs/translator_decisions/sarx_pauline_2026-05.md` (extending the JHN-only `psyche_vs_pneuma_anthropological_2026-04.md`). Lock single-rendering across all 5 senses; cite Rom 7–8 + Rom 1:3/9:5 as the locking precedent. Forward-pertinent: 1 Cor 1:26 (σοφοὶ κατὰ σάρκα); 2 Cor 5:16 (κατὰ σάρκα Χριστόν); Gal 5:13–24 (the GAL §6 cluster).

---

## 5. πνεῦμα — Pauline densest Spirit chapter (Rom 8) — **STABLE / extends inherited JHN+1TH lock**

Rom 8 has ~21 πνεῦμα-cluster occurrences — by a wide margin the densest Spirit chapter in the NT. All compliant with the inherited `psyche_vs_pneuma_anthropological_2026-04.md` lock plus the 1TH-amendment for tripartite-listing.

| Reference | Greek | Thai | Sense |
|---|---|---|---|
| Rom 8:2 | πνεύματος τῆς ζωῆς | **พระวิญญาณแห่งชีวิต** | divine Spirit + life-genitive |
| Rom 8:4, 5, 6, 9, 13, 14 | various πνεύματι / πνεῦμα + ἅγιον | **พระวิญญาณ** | uniform divine Spirit |
| Rom 8:9 | πνεῦμα Χριστοῦ | **พระวิญญาณของพระคริสต์** | Christ's-Spirit (= Holy Spirit by identity) |
| Rom 8:15 | πνεῦμα δουλείας / πνεῦμα υἱοθεσίας | **วิญญาณของการเป็นทาส / พระวิญญาณแห่งสิทธิ์การเป็นบุตร** | **REGISTER SPLIT** — non-divine "spirit" plain register; divine Spirit royal |
| Rom 8:16 | τὸ πνεῦμα ... τῷ πνεύματι ἡμῶν | **พระวิญญาณ ... จิตวิญญาณของเรา** | **REGISTER SPLIT** — divine Spirit royal; human spirit anthropological |
| Rom 8:23 | τὴν ἀπαρχὴν τοῦ πνεύματος | **ของแรกของพระวิญญาณ** | divine Spirit |
| Rom 8:26 (×2) | τὸ πνεῦμα συναντιλαμβάνεται ... αὐτὸ τὸ πνεῦμα ὑπερεντυγχάνει | **พระวิญญาณ ... พระวิญญาณเอง** | divine Spirit, intercessory |
| Rom 8:27 | τὸ φρόνημα τοῦ πνεύματος | **ความคิดของพระวิญญาณ** | divine Spirit |

**The Rom 8:15 / 8:16 register split is a principled exception to single-rendering πνεῦμα.** At 8:15 Paul contrasts **the spirit of slavery** (which we did NOT receive — non-divine, plain **วิญญาณ**) with **the Spirit of adoption** (which we DID receive — divine, royal **พระวิญญาณ**). At 8:16 Paul contrasts **the (Holy) Spirit himself** (royal **พระวิญญาณ**) with **our (human) spirit** (anthropological **จิตวิญญาณ**). Both register-splits exactly track the corpus-locked principle (`psyche_vs_pneuma_anthropological_2026-04.md`).

**Editorial assessment:** The Rom 8 Spirit-cluster is exemplary lock-compliance. The 8:15 contrastive-pair (slavery-spirit vs adoption-Spirit) is the load-bearing test for the doc's register-rule, and Romans nails it.

**STABLE — no new doc needed.** Existing JHN + 1TH locks fully cover. Worth a one-line cross-reference noting Pauline confirmation.

---

## 6. υἱοθεσία — adoption-as-sons (Pauline-corpus densest cluster) — **STABLE (undocumented; recommend new doc)**

Romans contains **3 of the 5 NT occurrences of υἱοθεσία** (8:15, 8:23, 9:4). The GAL audit §12 recommended `huiothesia_adoption_*.md` "before Rom 8 cluster"; the doc was never written.

| Verse | Greek | Thai |
|---|---|---|
| GAL 4:5 (precedent) | ἵνα τὴν υἱοθεσίαν ἀπολάβωμεν | **เพื่อเราจะได้รับการรับเป็นบุตร** |
| Rom 8:15 | ἐλάβετε πνεῦμα υἱοθεσίας | **พระวิญญาณแห่งสิทธิ์การเป็นบุตร** |
| Rom 8:23 | υἱοθεσίαν ἀπεκδεχόμενοι, τὴν ἀπολύτρωσιν τοῦ σώματος | **รอคอยสิทธิ์การเป็นบุตร — คือการไถ่ร่างกายของเรา** |
| Rom 9:4 | ὧν ἡ υἱοθεσία | **ผู้ที่ทรงประทานสิทธิ์การเป็นบุตร** |
| Eph 1:5 (forward) | προορίσας ἡμᾶς εἰς υἱοθεσίαν | (not yet translated) |

**Editorial flag — RENDERING DRIFT FROM GAL TO ROM:**
- **GAL 4:5: การรับเป็นบุตร** ("the receiving-as-son [act/status]")
- **ROM 8:15, 8:23, 9:4: สิทธิ์การเป็นบุตร** ("the right/privilege of being-a-son")

The two renderings are not synonymous. **การรับเป็นบุตร** emphasizes the act/status of being received as a son. **สิทธิ์การเป็นบุตร** adds the legal-rights-component (สิทธิ์ = right/privilege/legal-claim) — sharper emphasis on the Greco-Roman-legal-adoption force the GAL §12 KD names (legal-status, inheritance rights). The Romans rendering is **arguably more precise** for the legal-technical force, but it is a quiet **post-GAL revision** without a corresponding decision document.

**Recommend: REVIEW/STABLE; new doc** `docs/translator_decisions/huiothesia_adoption_2026-05.md` to lock ONE rendering for the Pauline-corpus. Two paths:
- (a) Standardize on **สิทธิ์การเป็นบุตร** (Romans pattern; preserves legal-rights force) and revise GAL 4:5 to match.
- (b) Standardize on **การรับเป็นบุตร** (GAL pattern; emphasizes the act-of-receiving) and revise Rom 8:15/8:23/9:4 to match.
- (c) Document both as principled-context-specific (GAL = redemption-context emphasizes the act; Rom = identity-context emphasizes the rights). Risky — corpus consistency-checker won't catch the split because the Thai isn't a single-locked-token.

**This is a STABLE-WITH-DRIFT-CANDIDATE flag** — Ben should pick the corpus-default before Eph 1:5 ships. Worth Ben's confirmation.

---

## 7. Rom 9:5 — christological doxology — **DECIDE before tagging (high-priority)**

The Greek at Rom 9:5 is **ambiguously punctuated** (the punctuation is editorial, NOT in the manuscripts):

> Greek: ὧν οἱ πατέρες, καὶ ἐξ ὧν ὁ χριστὸς τὸ κατὰ σάρκα, **ὁ ὢν ἐπὶ πάντων, θεὸς εὐλογητὸς εἰς τοὺς αἰῶνας· ἀμήν.**

**Two readings:**
- (a) **Christological:** "...from whom is Christ according to the flesh, **who is over all, God blessed forever. Amen.**" — Christ identified as "God-blessed-forever." One of the clearest Pauline-Christology proof-texts. BSB / NIV / ESV / CSB / NASB all chose this. Eremos current Thai: **ผู้ทรงเป็นพระเจ้าเหนือทุกสิ่ง ผู้ทรงเป็นที่ถวายสาธุการตลอดกาลเป็นนิตย์** (preserves Christ-IS-God-blessed-forever).
- (b) **Doxology-to-Father:** "...from whom is Christ according to the flesh. **God who is over all be blessed forever. Amen.**" — A separate doxology to the Father, syntactically detached from "Christ." NRSV (older), RSV-original-1946, NEB chose this.

The 9:5 KD is **explicit and principled** about following (a) per RULES §0:

> MAJOR INTERPRETIVE CRUX. Greek ambiguous-syntax: (a) referring-to-Christ ... (b) doxology-to-Father ... Following (a) per RULES §0 + BSB. ... The κατὰ σάρκα qualifier in 9:5a ('Christ according to flesh') would be POINTLESS without a complementary 'according to God-side' — supporting reading (a). Doxology-to-Father reading lacks this contextual-pointer.

**Editorial assessment:** The choice is RULES §0-aligned + BSB-aligned + the κατὰ-σάρκα-implies-complementary-divine-nature argument is exegetically strong. The Thai rendering **ผู้ทรงเป็นพระเจ้าเหนือทุกสิ่ง** is unambiguously Christological in Thai — there is no syntactic-ambiguity-preservation possible (Thai punctuation forces a choice).

**DECIDE before tagging:** Confirm Ben endorses the Christological reading as locked. Alternative: add a footer-note acknowledging the doxology-to-Father academic position (vanishingly minority among modern evangelical-Protestants, but the older RSV+NEB position is still cited in mainline scholarship). Critical for the external AI packet — both Grok and ChatGPT will likely affirm (a), but should be asked.

---

## 8. Rom 10:4 — τέλος νόμου Χριστὸς — **DECIDE before tagging**

> Greek: τέλος γὰρ νόμου Χριστὸς εἰς δικαιοσύνην παντὶ τῷ πιστεύοντι.
> Thai: เพราะพระคริสต์ทรงเป็นจุดสิ้นสุดของธรรมบัญญัติ สู่ความชอบธรรมแก่ทุกคนที่เชื่อ

τέλος carries two well-attested readings:
- (a) **Termination-end** ("Christ is the END of the Law as a means of righteousness"). Reformation-Lutheran-Reformed default. BSB / ESV / NIV / CSB. Eremos chose this — **จุดสิ้นสุด** ("end-point").
- (b) **Goal-fulfillment** ("Christ is the GOAL/aim that the Law was pointing to"). Increasingly favored in New-Perspective-Pauline scholarship (N.T. Wright, Dunn). Would be **เป้าหมาย** ("goal").

The 10:4 KD names the choice and follows (a) per RULES §0:

> FAMOUS-INTERPRETIVE-CRUX. τέλος ambiguous: (a) 'end / termination' (Reformation-Lutheran-Reformed default — Law-functionally-ended-as-means-of-righteousness); (b) 'goal / fulfillment' (some New-Perspective: Christ as the goal Law-was-pointing-to). RULES §0 evangelical-Protestant default favors (a). 'จุดสิ้นสุด' captures the termination-sense; could also be 'เป้าหมาย' for goal-sense. Following BSB.

**Editorial assessment:** Defensible per RULES §0. But the **GAL audit §7's παιδαγωγός εἰς Χριστόν crux is the parallel at GAL 3:24** (temporal-vs-directional reading). GAL 3:24 chose **temporal** ("until Christ"); Rom 10:4 chose **terminal** ("end of"). Both choices align — temporal-end and terminal-end form a coherent salvation-historical reading. But there is no corpus doc covering this pair.

**DECIDE before tagging:** Confirm Ben endorses the termination reading as the corpus default for τέλος-of-Law constructions. The alternative (goal-reading) would shift Rom 10:4 to **เป้าหมาย** + GAL 3:24 to **เพื่อนำเราไปถึงพระคริสต์**. Verse-level rationale at both is comprehensive. Worth combining into a single corpus doc covering paidagogos + telos as a paired Pauline-salvation-history-cluster.

**→ Recommend: new doc** `docs/translator_decisions/telos_paidagogos_christ_2026-05.md` to lock Pauline temporal-terminal-end-of-Law-at-Christ reading as the corpus default + cross-reference to GAL 3:24.

---

## 9. Rom 11:25–26 — "all Israel will be saved" — **DECIDE before tagging**

> Greek (11:26): καὶ οὕτως πᾶς Ἰσραὴλ σωθήσεται· καθὼς γέγραπται· Ἥξει ἐκ Σιὼν ὁ ῥυόμενος, ἀποστρέψει ἀσεβείας ἀπὸ Ἰακώβ.
> Thai: **และอย่างนี้อิสราเอลทั้งสิ้นจะได้รับความรอด** ดังที่เขียนไว้ว่า ‘ผู้ทรงช่วยให้พ้นจะเสด็จมาจากศิโยน — พระองค์จะทรงขจัดความอธรรมจากยาโคบ’

**Three competing readings of πᾶς Ἰσραήλ:**
- (a) **All-elect-of-ethnic-Israel** (Reformed-mainstream — the elect-remnant within ethnic Israel across history)
- (b) **Future end-time mass conversion of ethnic Israel** (Premillennial — a distinct future event tied to the parousia)
- (c) **Israel-AND-the-Church-together as the new-Israel** (some-Reformed / NT-Wright-school — typologically-redefined Israel)

The 11:26 KD:

> FAMOUS-INTERPRETIVE-CRUX. πᾶς Ἰσραήλ 'all Israel' — three-readings: (a) all-elect-of-ethnic-Israel (Reformed-mainstream); (b) corporate-Israel-as-a-future-end-time-mass-conversion (Premillennial); (c) Israel-and-the-Church-together as the new-Israel (some-Reformed). Eremos preserves 'อิสราเอลทั้งสิ้น' literally — leaving the reader to discern.

**Editorial assessment:** The Thai **อิสราเอลทั้งสิ้น** ("all Israel") is the most literal possible rendering and PRESERVES the ambiguity exactly as the Greek does. This is the right call — translation should not commit to (a)/(b)/(c) where the Greek itself is ambiguous. **Confirmation-needed** because Thai theological reviewers will read this through their Reformed-vs-Dispensational denominational frame and ask which reading is "right."

**DECIDE / REVIEW:** Confirm Ben endorses the ambiguity-preservation strategy. Alternatives:
- (a) Add a footer-note flagging the three readings (helps Thai reader distinguish from THSV1971-implicit reading).
- (b) Restrict the rendering to "อิสราเอลแท้" ("true Israel") — locks reading (c). Not recommended.
- (c) Restrict to "อิสราเอลทุกคน" ("every Israelite") — leans toward (b). Not recommended.

The current rendering is RIGHT but needs explicit endorsement.

---

## 10. Rom 16:1 — Phoebe διάκονον — **DECIDE before tagging**

> Greek: Συνίστημι δὲ ὑμῖν Φοίβην τὴν ἀδελφὴν ἡμῶν, οὖσαν καὶ διάκονον τῆς ἐκκλησίας τῆς ἐν Κεγχρεαῖς,
> Thai: ข้าพเจ้าขอฝากเฟบีพี่น้องหญิงของเรากับพวกท่าน ผู้เป็น**ผู้รับใช้**ของคริสตจักรที่เมืองเคนเครีย

**Two readings:**
- (a) **Generic servant** ("Phoebe, a servant of the church") — preserves NT-Pauline-διάκονος-fluidity (same word for Christ at Rom 15:8, apostles at 1 Cor 3:5). Conservative-evangelical-mainstream. Eremos current → **ผู้รับใช้**.
- (b) **Formal office (deaconess)** ("Phoebe, a deacon of the church") — formal church-office. Some-Reformed and progressive traditions. Would render as **ผู้ปกครอง** or transliterated **ดีคอน / มัคนายก**.

The 16:1 KD:

> διάκονος here-translation-debated: (a) 'servant' (generic; Eremos current); (b) 'deaconess' (formal-office). NT-Pauline-term-fluidity: same-word used of Christ (Rom 15:8) and apostles (1 Cor 3:5). Conservative-evangelical mainstream: 'servant' (preserves ambiguity); some-Reformed traditions read formal-office (= deacon). Eremos preserves the ambiguous-Greek by 'ผู้รับใช้.'

**Editorial assessment:** The choice (a) is RULES §0 evangelical-Protestant aligned + matches BSB / ESV / NIV / CSB. **ผู้รับใช้** preserves the fluidity. The Thai protestant-evangelical-mainstream is conservative on female-office; **ผู้รับใช้** does not pre-empt that conversation.

**DECIDE before tagging:** Confirm Ben endorses (a) the generic-servant reading. Critical because:
1. The same word appears in Rom 15:8 (Christ as διάκονος of the circumcision → **ผู้รับใช้**) — the Phoebe-rendering creates a Christ-Phoebe-parallel that may be theologically rich or problematic depending on view.
2. 1 Tim 3:8–13 (διακόνους + γυναῖκας) has the same crux for the female-deaconess question; the Romans-lock will propagate to 1 Tim.
3. Thai theological-reviewers will flag this question regardless.

**→ Recommend: external AI packet must include this item.** Both Grok and ChatGPT will likely affirm the conservative-evangelical reading; the question is whether Ben wants the Thai rendering to pre-commit on the female-deaconess question.

---

## 11. Rom 16:7 — Junia + ἐπίσημοι ἐν τοῖς ἀποστόλοις — **DECIDE before tagging**

> Greek: ἀσπάσασθε Ἀνδρόνικον καὶ **Ἰουνίαν** τοὺς συγγενεῖς μου ... οἵτινές εἰσιν **ἐπίσημοι ἐν τοῖς ἀποστόλοις**, οἳ καὶ πρὸ ἐμοῦ γέγοναν ἐν Χριστῷ.
> Thai: จงทักทายอันโดรนีคัสและ**ยูเนีย** ญาติของข้าพเจ้าและเพื่อนร่วมเป็นเชลยของข้าพเจ้า ทั้งสองคน**เป็นที่นับถือในหมู่อัครทูต** และทั้งสองได้อยู่ในพระคริสต์ก่อนข้าพเจ้า

**Two cruxes — gender + apostolic-status:**

**Crux 1 (Gender):** Ἰουνίαν (acc.) is grammatically ambiguous between Ἰουνία (fem. — "Junia") and the hypothetical Ἰουνίας (masc. — "Junias," not attested anywhere in Greek literature outside this debate). Modern scholarship overwhelmingly favors **feminine Junia** (Bauckham, Epp, Wallace). Eremos transliterates **ยูเนีย** — reads as feminine in Thai by phonetic-default but does not lexicalize the gender-marker.

**Crux 2 (Apostolic status):** ἐπίσημοι ἐν τοῖς ἀποστόλοις has two readings:
- (a) **"Outstanding among the apostles"** = they ARE apostles (broad-sense missionaries like Barnabas). Patristic-mainstream (Origen, Chrysostom — "what wisdom must this woman have had to be deemed worthy of the title of apostle!"); Bauckham, Epp.
- (b) **"Well-known to the apostles"** = they are NOT apostles, just esteemed by the apostles. Burer-Wallace; conservative-evangelical-mainstream.

Eremos current Thai **เป็นที่นับถือในหมู่อัครทูต** ("respected within / among the apostles") — preserves the ambiguity, but **ในหมู่** ("among / within") leans slightly toward (a).

The 16:7 NOTES:

> INTERPRETIVE CRUX: Junia (female) vs Junias (male hypothetical). Modern-scholarship overwhelmingly female. ἐπίσημοι ἐν τοῖς ἀποστόλοις: most-likely reads 'outstanding-among-the-apostles' (= they ARE-apostles, broad-sense missionaries like Barnabas). Eremos preserves slight-ambiguity in Thai while leaning-toward-inclusive.

**Editorial assessment:** The Notes acknowledge the inclusive lean (toward reading (a)). This is **arguably the most-debated single verse for female-leadership in the NT**. Thai protestant-evangelical reviewers will flag this; the inclusive lean is **not** RULES §0 evangelical-Protestant default (the conservative-evangelical-mainstream has shifted toward reading (b) since Burer-Wallace 2001).

**DECIDE before tagging:** Confirm Ben's preferred direction:
- **Inclusive (current): เป็นที่นับถือในหมู่อัครทูต** — leans toward (a), preserves ambiguity.
- **Conservative: เป็นที่รู้จักของอัครทูต** ("known to the apostles") — locks reading (b).
- **Strict-ambiguous: เป็นที่รู้จักโดดเด่นเกี่ยวข้องกับอัครทูต** — verbose ambiguity.

**Critical for the external AI packet** — both AIs will engage this question and likely give different answers (Grok-conservative; ChatGPT-inclusive).

---

## 12. Rom 12:1 — λογικὴν λατρείαν — **REVIEW**

> Greek: παραστῆσαι τὰ σώματα ὑμῶν θυσίαν ζῶσαν ἁγίαν εὐάρεστον τῷ θεῷ, **τὴν λογικὴν λατρείαν** ὑμῶν.
> Thai: ให้พวกท่านมอบร่างกายของพวกท่านเป็นเครื่องบูชา ... — นี่คือ**การปรนนิบัติบูชาตามความคิด**ของพวกท่าน

λογικός is interpretively-debated:
- (a) **Rational / mind-oriented** (cognate with λόγος "reason/word") — "your rational/reasonable worship" (your worship that befits a thinking creature). BSB / ESV / NASB.
- (b) **Spiritual** (in contrast to bodily/external) — "your spiritual worship" (LXX usage in Hellenistic-Jewish writers; some patristic). NIV ("true and proper worship"); CSB ("true worship"); 1 Pet 2:2 (λογικὸν γάλα) shows the meaning-fluidity.

Eremos current **ตามความคิด** ("according to thought / reason") — locks reading (a).

The 12:1 NOTES:

> 'Living-sacrifice' is the great-Pauline-paradox of new-covenant-worship. λογικός 'rational/reasonable' is interpretively-debated; Eremos preserves the rational-mind sense (cognate-with-λόγος).

**Editorial assessment:** The choice (a) is BSB-aligned + cognate-with-λόγος defensible. **ตามความคิด** is slightly awkward in Thai (could read as "according-to-your-opinion" — subjective overtones). The alternatives are **ฝ่ายจิตวิญญาณ** ("spiritual" — but collides with πνευματικός lock) or **ที่สมเหตุสมผล** ("reasonable") or **ที่ใช้ปัญญา** ("intellectual").

**REVIEW flag:** Confirm Ben endorses **ตามความคิด** as the lock + the rationale "rational-not-spiritual" is the corpus position. Worth Ben's confirmation; this is a small lemma but a famous-pulpit verse. Forward-pertinent: 1 Pet 2:2 (λογικὸν γάλα — same lemma, different referent).

---

## 13. ὀργή — divine wrath (Pauline-corpus densest cluster) — **STABLE / extends 1TH precedent**

Romans has **6 ὀργή occurrences** plus ~6 cognate orgizō-cluster instances. Uniform **พระพิโรธ** ("divine wrath" — royal-pระ-prefixed), exactly per the 1TH-§5 pattern.

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| Rom 1:18 | ἀποκαλύπτεται ... ὀργὴ θεοῦ ἀπ' οὐρανοῦ | **พระพิโรธของพระเจ้าได้รับการเปิดเผยจากสวรรค์** | revelatory-wrath (Rom thesis) |
| Rom 2:5 | θησαυρίζεις σεαυτῷ ὀργήν | **กำลังสะสมพระพิโรธ** | eschatological-day-of-wrath |
| Rom 2:8 | ὀργὴ καὶ θυμός | **พระพิโรธและความกริ้ว** | day-of-judgment doublet |
| Rom 3:5 | ὁ ἐπιφέρων τὴν ὀργήν | **ผู้ทรงนำพระพิโรธมา** | rhetorical-question wrath |
| Rom 4:15 | ὁ γὰρ νόμος ὀργὴν κατεργάζεται | **เพราะธรรมบัญญัติทำให้เกิดพระพิโรธ** | Law-effects-wrath |
| Rom 5:9 | σωθησόμεθα ... ἀπὸ τῆς ὀργῆς | **เราจะรอดพ้นจากพระพิโรธ** | eschatological-deliverance |
| Rom 9:22 | σκεύη ὀργῆς κατηρτισμένα εἰς ἀπώλειαν | **ภาชนะแห่งพระพิโรธที่จัดเตรียมไว้สำหรับความพินาศ** | election-theodicy |
| Rom 12:19 | δότε τόπον τῇ ὀργῇ ... ἐμοὶ ἐκδίκησις | **จงให้ที่แก่พระพิโรธ ... การแก้แค้นเป็นของเรา** | divine-prerogative + Deut 32:35 |
| Rom 13:4 | ἔκδικος εἰς ὀργὴν | **ผู้แก้แค้นเพื่อนำพระพิโรธมา** | civil-magistrate-as-instrument |
| Rom 13:5 | διὰ τὴν ὀργήν | **เพราะพระพิโรธ** | civic-obedience-motive |

**Editorial assessment:** Single-rendering **พระพิโรธ** uniform across all 10 instances. The pattern is principled and matches the 1TH §5 lock-precedent.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/orge_pauline_2026-05.md` (the 1TH audit deferred this; Romans 10-occurrence density makes Romans the natural locking-precedent). The doc should:
1. Lock ὀργή (divine-eschatological / civil-magistrate-instrumental) → **พระพิโรธ**
2. Lock orgizō-cluster cognates (orgilos, parorgizō) — likely → **ทำให้พระพิโรธ**
3. Cite Rom 1:18 (the letter-thesis-revelatory verse) as the locking precedent
4. Forward-pertinent: Eph 2:3 (τέκνα ὀργῆς), Eph 4:26 (ὀργίζεσθε), Eph 5:6, Col 3:6 (ὀργὴ θεοῦ), Rev 6:16 + 11:18 + 14:10 + 16:19 + 19:15 (eschatological-divine-wrath cluster)

---

## 14. Inclusion-variant disposition — **LOCKED ✓ (post-doxology-backfill)**

The 2026-05-02 systemic remediation (`docs/end_of_book/inclusion_variant_gap_2026-05-02.md`) and the strict-audit gate added to `scripts/audit_inclusion_variants.py` apply directly to Romans:

| Verse | SBLGNT status | Disposition |
|---|---|---|
| Rom 16:25–27 | SBLGNT includes (at end) | Tier-3 ⟦…⟧ large-block — backfilled 2026-05-02 ✓ |
| Rom 16:24 | NA28 omits; SBLGNT includes | Following SBLGNT — included as canonical text; flagged in v.24 NOTES |
| Rom 5:1 ἔχομεν vs ἔχωμεν | SBLGNT/NA28: indicative ἔχομεν | Following SBLGNT — verse-level NOTE explains the variant |
| Rom 8:1 (longer endings in Byz) | SBLGNT: shorter ending | Following SBLGNT — verse-level NOTE |
| Rom 14:23 (doxology-position) | SBLGNT: doxology at 16:25–27 only | No Tier-1/2/3 needed; addressed by 16:25 NOTES (floating-placement evidence: 𝔓⁴⁶ at end of ch.15; Byz-sub at end of ch.14; F/G omit) |

The 16:25 NOTES is **exemplary** — 600+ chars covering 𝔓⁴⁶ + Byz-sub + Marcion + every floating-placement witness, plus the explicit Tier-3 ⟦…⟧ self-marking. This is the pattern other books should imitate.

**LOCKED** ✓ — post-backfill, the `audit_inclusion_variants.py --strict` gate passes for Romans.

---

## 15. OT citations — Pauline-corpus densest book — **all LOCKED + LOGGED**

Romans is the **densest OT-citing book in the NT** — ~54 formal citations + ~30 allusions across 16 chapters. Special-density passages: Rom 3:10–18 (Pauline catena: Pss 14, 53, 5, 140, 10, 36 + Isa 59 + Eccl 7), Rom 4 (Gen 15:6 + Ps 32), Rom 9–11 (~24 citations covering Gen, Exod, Deut, 1 Kgs, Pss, Isa, Jer, Hos, Joel, Mal), Rom 15:9–12 (4 citations chained: Ps 18:49 + Deut 32:43 LXX + Ps 117:1 + Isa 11:10 — the "all the nations praise God" climactic-quartet).

All citations correctly flagged with **คำเขียน** ("it is written") + cross-referenced to source + appended to `data/nt_ot_citations.json` (verified by `output/check_reports/ot_citations_romans_NN.md` clean across all 16 chapters).

**Notable handling:**
- Rom 9:25–26 (Hos 2:23 + Hos 1:10) — chained quotation with the LXX-vs-MT-text-form variation flagged
- Rom 9:27–28 (Isa 10:22–23 LXX) — the σύντομον-LXX vs MT split flagged
- Rom 10:6–8 (Deut 30:12–14) — Pauline pesher-reframing of Deut acknowledged
- Rom 11:26–27 (Isa 59:20–21 LXX adaptation + Jer 31:34 echo) — the "ἥξει ἐκ Σιὼν" deliverer-formula correctly identified as Isa 59 with Pauline modification
- Rom 12:19 (Deut 32:35 LXX) — the divine-vengeance prerogative
- Rom 12:20 (Prov 25:21–22 LXX) — the heaping-coals-of-fire metaphor
- Rom 15:3 (Ps 69:9), 15:9 (Ps 18:49), 15:10 (Deut 32:43 LXX), 15:11 (Ps 117:1), 15:12 (Isa 11:10) — the climactic Gentile-praise catena

**LOCKED** ✓ — all citations flagged, sourced, and logged. The `check_phrase_consistency.py` audits 1 Romans-specific phrase ("καθὼς γέγραπται" → "ดังที่เขียนไว้") + the corpus formula list, all 0 violations.

---

## 16. Inherited locks — **all compliant**

| Doc | ROM evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | Rom 16:1 (ἐκκλησίας τῆς ἐν Κεγχρεαῖς → **คริสตจักรที่เมืองเคนเครีย**), 16:4 (αἱ ἐκκλησίαι πᾶσαι τῶν ἐθνῶν → **คริสตจักรของบรรดาชนชาติทั้งปวง**), 16:5 (κατ' οἶκον αὐτῶν ἐκκλησίαν → **คริสตจักรในบ้าน**), 16:16 (αἱ ἐκκλησίαι πᾶσαι τοῦ Χριστοῦ → **คริสตจักรทั้งสิ้นของพระคริสต์**), 16:23 (ὅλης τῆς ἐκκλησίας → **คริสตจักรทั้งหมด**) — **5 occurrences**, all → **คริสตจักร** uniform. | **LOCKED** |
| `ethnos_2026-04.md` | Rom 1:5, 1:13, 1:14 (Ἑλλησίν τε καὶ βαρβάροις → **ทั้งกรีกและคนป่าเถื่อน** — note this is NOT ἔθνος; barbarian-vs-Greek polarity), 2:14, 2:24, 3:29 (×2), 4:17, 4:18, 9:24, 9:30, 10:19, 11:11, 11:12, 11:13 (×2), 11:25, 15:9 (×2 — 9 + 11), 15:10, 15:11, 15:12, 15:16 (×2), 15:18, 15:27, 16:4, 16:26 — ~25 occurrences. **Two-rendering pattern** matches the doc: **ประชาชาติ** for cosmic-OT-Psalmic universal (1:5, 4:17–18, 15:11, 16:26); **ชนชาติ** for Israel's-people-among-other-peoples (10:19; 11:11–14 collective); **คนต่างชาติ** for Pauline-mission Gentile (1:5, 11:11, 11:12, 11:13, 11:25, 15:9, 15:16, 15:18, 15:27, 16:4). All three senses uniform per the doc's three-way rule. | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | Romans has **30+ narrator-κύριος references** (Rom 1:4, 1:7, 4:8, 4:24, 5:1, 5:11, 5:21, 6:11, 6:23, 7:25, 8:39, 9:28, 9:29, 10:9, 10:12, 10:13, 10:16, 11:3, 11:34, 12:11, 12:19, 13:14, 14:6, 14:8, 14:9, 14:11, 14:14, 15:6, 15:11, 15:30, 16:2, 16:8, 16:11, 16:12, 16:13, 16:18, 16:20, 16:22, 16:24) — all → **องค์พระผู้เป็นเจ้า**, perfectly compliant with the lock. The doc's "Lukan-Acts signature" framing now has **Pauline-confirmation across GAL + 1TH + ROM**; **amendment-needed** as already noted in JHN + GAL + 1TH audits. | **LOCKED-with-amendment-needed** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in Romans (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | Rom 1:21 (οὐχ ὡς θεὸν ἐδόξασαν → **ไม่ได้ทรงถวายพระเกียรติแด่พระเจ้า** — failure-to-glorify pagan-context; preserves divine-object praise verb pattern), 4:20 (δοὺς δόξαν τῷ θεῷ → **ถวายพระเกียรติแด่พระเจ้า** — Abraham giving-glory), 11:36 (αὐτῷ ἡ δόξα εἰς τοὺς αἰῶνας → **ขอพระเกียรติจงมีแด่พระองค์**), 15:6 (ἵνα ὁμοθυμαδὸν ... δοξάζητε τὸν θεόν → **เพื่อพร้อมกัน...ถวายพระเกียรติแด่พระเจ้า**), 15:9 (τὰ ἔθνη ὑπὲρ ἐλέους δοξάσαι τὸν θεόν → **คนต่างชาติ...ถวายพระเกียรติแด่พระเจ้า**), 16:27 (ᾧ ἡ δόξα → **ขอพระเกียรติจงมีแด่พระองค์**) — all uniform **ถวายพระเกียรติ** (Acts-amended doxological narrator-formal sub-rule). Compliant. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | Rom 13:1–7 ἐξουσίαις ὑπερεχούσαις → **อำนาจปกครองที่อยู่เหนือ** (plain register for civil authorities — correct: Pauline argument is that authorities-are-instruments-of-God-not-divine-themselves). 16:13 (Ῥοῦφον τὸν ἐκλεκτὸν ἐν κυρίῳ → **รูฟัสผู้ถูกเลือกในองค์พระผู้เป็นเจ้า**) — plain register for individual believer. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ + Spirit throughout (Rom 8:11 ἐγείραντος Χριστὸν → **ผู้ทรงให้พระคริสต์ทรงเป็นขึ้น**; royal compounds throughout Rom 1–11, 12–15 doxology, 16:25–27 doxology). Plain register for Phoebe (16:1), Prisca-Aquila (16:3), Junia (16:7), all human authority figures. The **πατήρ register split** at Rom 1:7 (θεοῦ πατρὸς ἡμῶν → **พระเจ้าพระบิดาของเรา** — divine, royal), Rom 4:1 (Ἀβραὰμ τὸν προπάτορα ἡμῶν κατὰ σάρκα → **อับราฮัมบรรพบุรุษของเราตามเนื้อหนัง** — human-genealogical-ancestor, plain — **เปรพบυรุς** lemma), Rom 4:11–12, 4:16–18 (Abraham-as-father-of-believers — plain register), Rom 8:15 (Αββα ὁ πατήρ → **อับบา พระบิดา** — divine, royal). Compliant — exact GAL-§5 + 1TH-§8 pattern. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | Rom 8:15 Αββα ὁ πατήρ → **อับบา พระบิดา** (Aramaic transliteration + Greek translation, exact GAL 4:6 pattern). Note the Mark 14:36 + GAL 4:6 + Rom 8:15 triple-occurrence locks the formula across Synoptics + GAL + Romans. | **LOCKED** |
| `inclusion_variants_absent_verses_2026-04.md` | Rom 16:25–27 Tier-3 ⟦…⟧ backfilled 2026-05-02 (see §14 above). 16:24 SBLGNT-included (NA28-omitted) — verse-level NOTE flags. **No other Tier-1/2/3 variants in Romans** (post-strict-audit confirms zero unresolved candidates). | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Romans is doctrinal-pastoral letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in Romans. The Rom 9:21 potter-clay analogy (κεραμεὺς τοῦ πηλοῦ → **ช่างปั้นหม้อ ... ดินเหนียว**) is an **analogy**, not a parable with transparent God-figure — the potter is the explicit-God-figure (κεραμεύς + θεοῦ in v.20), not a hidden one. Plain register for the potter-as-character; royal register for God-as-explicitly-named. Compliant. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | Rom 2:4 (τὸ χρηστὸν τοῦ θεοῦ εἰς μετάνοιάν σε ἄγει → **ความดีเลิศของพระเจ้านำท่านไปสู่การกลับใจ**), 11:29 (ἀμεταμέλητα γὰρ τὰ χαρίσματα — adjective-form αμεταμέλητος → **ไม่เปลี่ยนแปลง / ไม่ทรงเปลี่ยน**) — μετανοέω-cluster correctly rendered with **กลับใจ**; ἀμεταμέλητος (NOT-changeable, NOT-regretted, applied to GIFTS) correctly distinguished. Compliant per the doc's μετανοέω-vs-μεταμέλομαι split. | **LOCKED** |
| `aphesis_forgiveness_of_sins_2026-04.md` | Rom 4:7 (ἀφέθησαν αἱ ἀνομίαι → **ความอธรรมที่ทรงได้รับการอภัย** — Ps 32:1 LXX citation; ἀφίημι passive). The verb-form is ἀφίημι (the cognate verb, not the noun ἄφεσις) but the doc covers both noun and verb-form for the forgiveness-of-sins lemma. Uniform with the Synoptic pattern. | **LOCKED** |
| `pagan_deities_2026-04.md` | Rom 1:23 (ἤλλαξαν τὴν δόξαν τοῦ ἀφθάρτου θεοῦ ἐν ὁμοιώματι εἰκόνος φθαρτοῦ ἀνθρώπου → **เปลี่ยนพระเกียรติของพระเจ้าผู้ไม่เน่าเปื่อย เป็นรูปเคารพในรูปลักษณ์ของมนุษย์ที่เน่าเปื่อย**); 1:25 (μετήλλαξαν τὴν ἀλήθειαν τοῦ θεοῦ ἐν τῷ ψεύδει καὶ ἐσεβάσθησαν καὶ ἐλάτρευσαν τῇ κτίσει → **บูชาและปรนนิบัติสิ่งที่ทรงสร้าง**); 11:4 (Βάαλ → **บาอัล** — pagan-deity proper-name). Pagan deities consistently **รูปเคารพ / สิ่งที่ทรงสร้าง / บาอัล** — never พระเจ้า. Compliant per the doc. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman administrative titles in Romans (no procurator/centurion/proconsul named). The Rom 13:1–7 ἐξουσίαι "authorities" are abstract, not titled-individuals. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from Romans. The Rom 1:3 (γενομένου ἐκ σπέρματος Δαυὶδ κατὰ σάρκα — Davidic-descent-as-human) is the closest Christological-title-like construction here; renders with πรπะบุτร + κατὰ σάρκα + David-genealogy as locked elsewhere. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (~10 occurrences in Rom 5:5, 8:9, 8:11, 8:14, 8:16, 8:26, 9:1, 14:17, 15:13, 15:16, 15:19, 15:30) → **พระวิญญาณบริสุทธิ์** (full form) or **พระวิญญาณ** (anaphoric) — uniform. Anthropological πνεῦμα at Rom 1:9 (ἐν τῷ πνεύματί μου → **ด้วยจิตวิญญาณของข้าพเจ้า**), 8:16 (τῷ πνεύματι ἡμῶν → **จิตวิญญาณของเรา**) — **anthropological-human-spirit register** (จิตวิญญาณ, not จิต) per the 1TH-§6 amended-form. Worth noting Romans uses **จิตวิญญาณ** for human-πνεῦμα more frequently than the corpus-doc-implied **จิต**; this is consistent with the 1TH 5:23 tripartite-exception logic but extends the rendering to non-tripartite contexts. ψυχή at Rom 2:9 (πᾶσαν ψυχὴν ἀνθρώπου → **มนุษย์ทุกคน** — Hebraic idiom for "every human"), 11:3 (τὴν ψυχήν μου → **ชีวิตของข้าพเจ้า** — life-sense, OT echo of 1 Kgs 19:10), 13:1 (πᾶσα ψυχή → **ทุกคน** — every-person idiom), 16:4 (ὑπὲρ τῆς ψυχῆς μου → **เพื่อชีวิตของข้าพเจ้า** — life-risking sense). Uniform compliance with the locked rule's life-vs-personhood-vs-inner-self three-way distribution. | **LOCKED-with-amendment-noted** (1TH-§6 already flagged; Romans extends the **จิตวิญญาณ-for-anthropological-πνεῦμα** pattern beyond tripartite-only) |
| `johannine_doubled_amen_2026-04.md` | N/A — Romans is Pauline, not Johannine. Single ἀμήν at Rom 1:25, 9:5, 11:36, 15:33, 16:24, 16:27 — all chapter-or-doxology-closing acclamations → **อาเมน**. The 6-occurrence ἀμήν-density in Romans is the highest in the Pauline corpus (compared to GAL 1, 1TH 0); reflects Romans's doxological structure with each major argument-block ending in ἀμήν. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in Rom). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in Romans. | **LOCKED (N/A)** |
| `adversary_speech_register_2026-05.md` | N/A — no adversary speech register triggers in Romans (the Rom 9:14, 9:19, 11:1, 11:11 hypothetical-objector dialogues use first-person rhetorical voice, NOT distinct-adversary-register). | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | Rom 14:17 (ἡ βασιλεία τοῦ θεοῦ → **อาณาจักรของพระเจ้า**) — only βασιλεία-noun in Romans; consistent with the Synoptic-Acts-GAL-1TH lock. Compliant. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | Rom 1:18 (ἀπ' οὐρανοῦ → **จากสวรรค์** — directional-source); 10:6 (ἀναβήσεται εἰς τὸν οὐρανόν → **ขึ้นไปบนสวรรค์**); etc. Uniform **สวรรค์** for ouranos-as-source/destination. Compliant per the doc. | **LOCKED** |
| `dikaioo_dikaiosyne_family_2026-05.md` | The Romans-defining lock. See §1 above — full compliance. | **LOCKED** |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | N/A — Romans does NOT have porneia + moicheia in tension (Rom 13:9 has μοιχεύσεις only, in the Decalogue-citation; no πορνεία in Romans). The DEFERRED status is unaffected. | **LOCKED (N/A — DEFERRED)** |

---

## Mechanical (§1) — **all green**

- 16/16 chapters: `output/check_reports/romans_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 16/16 chapters: `output/back_translations/romans_NN.json` ✓ (back-translation files use `back_translation_romans_NN.md` naming + `output/back_translations/romans_NN.json` per the post-Acts-loop pipeline; both exist)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 178-chapter / 6198-verse corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --strict`: **passes** for Romans (post-doxology-backfill 2026-05-02)
- `git status output/`: clean (post-2026-04-19 ship script auto-commits)

---

## Pre-existing docs affirmed / unchanged

All 28 docs in `docs/translator_decisions/` reviewed. Compliance summary in §16 above. Three docs flagged for amendment (already noted in JHN + GAL + 1TH audits, now confirmed by Romans):

- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend "Lukan-Acts signature" framing to "Lukan-Acts + Johannine + Pauline (GAL + 1TH + ROM, 30+ narrator-κύριος references in Romans alone)." Fourth independent corpus-confirmation.
- **`psyche_vs_pneuma_anthropological_2026-04.md`** — Romans extends the **จิตวิญญาณ-for-anthropological-πνεῦμα** rendering beyond the 1TH 5:23 tripartite-exception to general anthropological-spirit contexts (Rom 1:9, 8:16). Worth a sub-section amendment naming Pauline anthropological-πνεῦμα → **จิตวิญญาณ** as the corpus default (not **จิต**).
- **`narrator_vs_character_voice_2026-04.md`** — Romans confirms the πατήρ register split (royal **พระบิดา** for divine; plain **บรรพบุรุษ** for ancestral / **บิดา** for analogical). Worth a one-line cross-reference to GAL §5 + 1TH §8 + ROM compliance.

---

## Flagged for Ben's attention

### A. πίστις Χριστοῦ — STABLE / lift to corpus doc — **(§2)**
Three-book-confirmed (GAL + 1TH-implicit + ROM). Lift to corpus doc `pistis_christou_2026-05.md` after Ben's confirmation that the objective-genitive (faith IN Christ → ความเชื่อในพระคริสต์) is the corpus-default.

### B. νόμος Pauline two-rendering policy — **STABLE / NEW lift to corpus doc — HIGHEST forward priority — (§3)**
Romans 7:21–8:2 introduces a **principled two-rendering split** (ธรรมบัญญัติ for Mosaic-Torah; กฎ for inner-principle / Pauline νόμος-of-X-genitive constructions) that is at apparent odds with the GAL §3 single-rendering recommendation. Reconcile in `nomos_pauline_2026-05.md`. Forward-pertinent: 1 Cor 9:20–21, GAL 6:2 (revisit), Heb 7-8.

### C. σάρξ Pauline single-rendering — **STABLE / lift to corpus doc — (§4)**
Romans 7-8 confirms the GAL §6 policy. Lift to corpus doc `sarx_pauline_2026-05.md`.

### D. υἱοθεσία rendering drift GAL→ROM — **REVIEW / lift to corpus doc — (§6)**
GAL uses **การรับเป็นบุตร**; Romans uses **สิทธิ์การเป็นบุตร**. Same lemma, two renderings, no documented decision. Pick a corpus default; revise the other to match.

### E. Rom 9:5 — christological doxology — **DECIDE before tagging — (§7)**
Confirm Ben endorses the Christological reading (BSB-aligned, RULES §0-aligned). The KD is principled; this is a confirmation-needed not a fix-needed.

### F. Rom 10:4 τέλος νόμου — **DECIDE before tagging — (§8)**
Confirm Ben endorses the termination-end reading (BSB-aligned, RULES §0-aligned). Recommend pairing with GAL 3:24 παιδαγωγός in a `telos_paidagogos_christ_2026-05.md` corpus doc.

### G. Rom 11:25–26 "all Israel" — **DECIDE before tagging — (§9)**
Confirm Ben endorses the ambiguity-preservation strategy (อิสราเอลทั้งสิ้น literal). Consider whether to add a footer-note for the three-readings.

### H. Rom 16:1 Phoebe διάκονον — **DECIDE before tagging — (§10)**
Confirm Ben endorses (a) the generic-servant reading **ผู้รับใช้** as the corpus default. Cross-pertinent for 1 Tim 3:8–13.

### I. Rom 16:7 Junia + apostolic status — **DECIDE before tagging — (§11)**
Confirm Ben endorses the inclusive lean (current: เป็นที่นับถือในหมู่อัครทูต) OR pivots to the Burer-Wallace conservative reading (เป็นที่รู้จักของอัครทูต). High-visibility female-leadership crux.

### J. Rom 12:1 λογικὴν λατρείαν — **REVIEW — (§12)**
Confirm Ben endorses **ตามความคิด** ("rational/mind-oriented") as the lock. Forward-pertinent for 1 Pet 2:2.

### K. ὀργή divine wrath — **STABLE / lift to corpus doc — (§13)**
10-occurrence Romans density makes Romans the locking precedent. `orge_pauline_2026-05.md`.

### L. New corpus docs to write (before 1–2 Corinthians)
1. **`docs/translator_decisions/pistis_christou_2026-05.md`** (§A) — locks objective-genitive default
2. **`docs/translator_decisions/nomos_pauline_2026-05.md`** (§B) — locks two-rendering policy ธรรมบัญญัติ/กฎ — **HIGHEST priority**
3. **`docs/translator_decisions/sarx_pauline_2026-05.md`** (§C) — locks single-rendering เนื้อหนัง
4. **`docs/translator_decisions/huiothesia_adoption_2026-05.md`** (§D) — locks one rendering (resolves drift); name the post-decision direction
5. **`docs/translator_decisions/telos_paidagogos_christ_2026-05.md`** (§F) — pairs Rom 10:4 + GAL 3:24
6. **`docs/translator_decisions/orge_pauline_2026-05.md`** (§K) — locks **พระพิโรธ** uniform
7. **(Optional)** `parousia_christou_2026-05.md` — promote 1TH-§1 doc-recommendation if not yet written

### M. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (GAL + 1TH + ROM)"
- **`psyche_vs_pneuma_anthropological_2026-04.md`** — add Pauline anthropological-πνεῦμα → **จิตวิญญาณ** sub-section
- **`narrator_vs_character_voice_2026-04.md`** — one-line cross-ref to GAL §5 + 1TH §8 + ROM πατήρ register split

### N. External AI review (§3 of checklist) — **pending**
Recommended before `book-romans-v1` tag. Suggested 5-cluster external AI packet:
1. **Rom 1:1–17** — opening + thesis + Hab 2:4 citation + revelation-of-wrath-of-God
2. **Rom 3:21–4:25** — justification-by-faith first-statement + πίστις-Χριστοῦ + δικαιόω + Abraham + λογίζομαι/imputation
3. **Rom 7:7–8:17** — the ἐγώ + νόμος-cluster + σάρξ vs πνεῦμα + Αββα ὁ πατήρ + υἱοθεσία
4. **Rom 9:1–11:36** — election + remnant + "all Israel" + Rom 9:5 christological doxology + 9:25 Hosea citation + 10:4 τέλος + 11:36 doxology
5. **Rom 16:1–16, 25–27** — Phoebe + Junia + greetings + Tier-3 doxology

Use Grok + ChatGPT in parallel per the JHN/GAL/1TH pattern. Both AIs must engage §G–§I (the controversial gender + Israel readings).

---

## Recommendation

**Romans ships in strong corpus-hygiene shape — and locks the project's heaviest theological-vocabulary load.** The translator made consistent, principled choices on the seven most-significant Romans-introduced or Romans-densified lemma-clusters (δικαιόω; πίστις-Χριστοῦ; νόμος two-rendering; σάρξ; υἱοθεσία; πνεῦμα; ὀργή). Six new translator_decisions docs are recommended (§L items 1–6); five DECIDE-items (§E–§I) need Ben's confirmation before tagging.

Tag `book-romans-v1` after:
1. Ben's decisions on **§E + §F + §G + §H + §I** (DECIDE items: Rom 9:5 christological doxology; Rom 10:4 τέλος; Rom 11:26 "all Israel"; Rom 16:1 Phoebe; Rom 16:7 Junia)
2. Ben's confirmations on **§A + §B + §C + §D + §J + §K** (REVIEW + STABLE items)
3. Six new translator_decisions docs written (§L items 1–6)
4. Three existing docs amended (§M)
5. External AI sanity-check (§N)
6. (Optional) Native-Thai-evangelical reviewer pass on Rom 9–11 (the most-visible doctrinal block) and Rom 16 (the gender-question block)

The remaining Pauline letters (1–2 Cor in flight; then Eph, Phil, Col, 2 Th, Pastorals, Phlm) can be queued for next book — but writing **`nomos_pauline_2026-05.md`** in particular should happen **before 1 Cor 9:20–21** to avoid forward drift. The eight Romans corpus-locks are now the **theological-vocabulary baseline** for the rest of the Pauline corpus + Hebrews + Catholic Epistles + Revelation.
