# Ephesians — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 6 chapters (155 verses; ~395 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (40 docs).
**Trigger:** EPH 6 shipped (commit `1bcf1e6`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 6/6 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-193-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows only the re-ran-check artifact (`key_term_consistency_all.md`) plus the new-but-pre-shipped textual-variant resolved doc + paratext SFM artifacts — no EPH source-file dirt.
- **Ephesians is the THIRD CAPTIVITY-EPISTLE the project has shipped** (after PHP and COL; the cluster: PHP, COL, EPH, PHM). At 155 verses the letter is the longest of the four prison-epistles and carries a uniquely-condensed Pauline theological synthesis: doctrinal chs.1–3 (the eulogia + Gentile-inclusion-mystery + cosmic-Christology), ethical chs.4–6 (church-unity + put-off/put-on + Spirit-filling + the EXPANDED Haustafel + the armor-of-God spiritual-warfare). The letter introduces **two new-corpus clusters**: the EPH-distinctive **ἐπουρανίοις → สวรรคสถาน** (heavenly-realms — only here in NT, 5×), and the **κοσμοκράτωρ + πνευματικὰ τῆς πονηρίας** spiritual-warfare extension at 6:12.
- **The single most editorially-LOAD-BEARING new item is the EXPANDED Pauline Haustafel (5:22–6:9)** — vastly fuller than COL 3:18–4:1, with the Christ-and-church marriage-typology (5:22–33) at its core. Same ὑποτάσσω → **ยอมอยู่ใต้บังคับ** lock as COL is preserved, but the wife-husband section now triples in length and lays the typological foundation that subsequent NT marriage-discourse builds on.
- **The spiritual-beings hierarchy doc gets its FIRST FULL Pauline-letter confirmation** at EPH 1:21 (already revised on this branch to match the lock — see `spiritual_beings_hierarchy_2026-05.md`). EPH 3:10 + EPH 6:12 also compliant. EPH 6:12's κοσμοκράτωρ + πνευματικὰ τῆς πονηρίας extends the 4-tier hierarchy with two NT-HAPAX additions — recommend folding into the existing doc.
- **The σάρξ polysemy + RULES §5 flagging discipline COL exemplified** is preserved exactly across EPH (2:3, 2:11, 5:29, 6:5, 6:12 — all explicitly flagged). The recommended `sarx_pauline_2026-05.md` corpus doc is now a **two-letter-pattern** (COL + EPH) and should be written before Romans 7 ships.
- **9 inherited Pauline + Synoptic locks verified compliant** (πίστις-Χριστοῦ, υἱοθεσία, ἀφεσις, ἔθνος, narrator-κύριος, πατήρ register split, ἐκκλησία, ἀπόστολος, διάκονος — see §13).
- **3 items flagged DECIDE** (the EXPANDED Haustafel ὑποτάσσω + 5:21 mutual-submission framing; the EPH 1:23 πᾶν τὸ πλήρωμα τοῦ τὰ πάντα ἐν πᾶσιν πληρουμένου three-way ambiguity preserved; the EPH 4:8 Ps 68:18 Pauline-modification "received → gave" with Thai mirroring Paul not the LXX).
- **5 items flagged REVIEW** (the EPH 4:9 κατώτερα μέρη τῆς γῆς descent-to-earth vs descent-to-Hades; the EPH 5:14 unidentified citation handling; the EPH 5:26 λουτρόν+ῥῆμα baptism-and-word imagery; the EPH 4:11 πρὸς τὸν καταρτισμόν fivefold-vs-fourfold ministry-list; the πανοπλία τοῦ θεοῦ armor-vocabulary register at 6:11–17).
- **External AI review (§3) pending** — items doc + packet built in this branch.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. The EXPANDED Pauline Haustafel (5:22–6:9) — wife-husband Christ-church typology — **DECIDE before tagging**

The single most ethically load-bearing passage in the book + the most-debated NT-marriage-text in modern Christian-ethics discourse. EPH expands the COL Haustafel (COL 3:18–4:1, 6 verses) into a **22-verse Christological-typology** centered on the Christ-and-church-as-marriage-archetype:

| Verse | Greek | Thai |
|---|---|---|
| 5:21 | ὑποτασσόμενοι ἀλλήλοις ἐν φόβῳ Χριστοῦ | **ยอมอยู่ใต้บังคับซึ่งกันและกัน**ในความยำเกรงพระคริสต์ |
| 5:22 | Αἱ γυναῖκες τοῖς ἰδίοις ἀνδράσιν ὡς τῷ κυρίῳ | ภรรยาทั้งหลาย จง**ยอมอยู่ใต้บังคับ**สามีของตน เหมือนยอมอยู่ใต้บังคับองค์พระผู้เป็นเจ้า |
| 5:23 | ἀνήρ ἐστιν κεφαλὴ τῆς γυναικὸς ὡς καὶ ὁ Χριστὸς κεφαλὴ τῆς ἐκκλησίας, αὐτὸς σωτὴρ τοῦ σώματος | สามีเป็น**ศีรษะ**ของภรรยา เช่นเดียวกับที่พระคริสต์ทรงเป็นศีรษะของคริสตจักร พระองค์เองทรงเป็น**พระผู้ช่วยให้รอด**ของกายนั้น |
| 5:25 | οἱ ἄνδρες, ἀγαπᾶτε τὰς γυναῖκας, καθὼς καὶ ὁ Χριστὸς ἠγάπησεν τὴν ἐκκλησίαν καὶ ἑαυτὸν παρέδωκεν ὑπὲρ αὐτῆς | สามีทั้งหลาย จง**รัก**ภรรยา เช่นเดียวกับที่พระคริสต์ทรงรักคริสตจักรและทรงสละพระองค์เองเพื่อคริสตจักร |
| 5:31 | Gen 2:24 quotation | ‘ชายจะละบิดามารดาของตน และจะผูกพันอยู่กับภรรยาของตน และทั้งสองจะเป็นเนื้ออันเดียวกัน’ |
| 5:32 | τὸ μυστήριον τοῦτο μέγα ἐστίν, ἐγὼ δὲ λέγω εἰς Χριστὸν καὶ εἰς τὴν ἐκκλησίαν | **ความลึกลับ**นี้ยิ่งใหญ่ แต่ข้าพเจ้ากล่าวถึงพระคริสต์และคริสตจักร |
| 5:33 | ἡ δὲ γυνὴ ἵνα φοβῆται τὸν ἄνδρα | ภรรยาก็ต้อง**เคารพยำเกรง**สามี |

**Editorial assessment:** Three principled choices stand out:

1. **5:21 mutual-submission preserved as participle-bridge** between Spirit-filling (vv.18–20) and the household-code. The Thai **ซึ่งกันและกัน** (literal "to one another") preserves the egalitarian-frame that the Greek participle establishes. The 5:21 KD explicitly notes the household-relations are EXPRESSIONS of mutual-submission, not separate-from it. Egalitarian-vs-complementarian tension is preserved exactly as Greek leaves it.

2. **5:23 asymmetry deliberate**: husbands are **NOT** told to be saviour-of-wives (impossible-Christological-claim). The 5:23 KD names this: "The Christ-savior-of-the-body claim is NON-symmetrical." Husbands imitate Christ's-self-giving-cross-love, not Christ's-divine-status. **The asymmetry-prevents the Christ-church analogy from over-mapping into wife-as-needing-salvation-from-husband.**

3. **5:33 φοβέομαι → เคารพยำเกรง** (reverent-respect, not terror). Same lemma as v.21 φόβῳ Χριστοῦ — preserves the lexical-link without forcing fear-of-punishment register.

**DECIDE before tagging:**
1. Confirm Ben endorses **ยอมอยู่ใต้บังคับ** at 5:22, 5:24 — corpus-precedent-aligned with COL 3:18, GAL/Pauline-pattern. Same lock as COL audit §8 (which Ben presumably approved before EPH 5 shipped). The EPH-amplification (the v.21 mutual-frame + the v.23 Christ-savior-asymmetry + the v.31 Gen 2:24 typology) makes EPH the corpus-ANCHOR for the Pauline-marriage-doctrine — the lock cannot be revisited later without large back-incompatibility.
2. Confirm Ben endorses preserving the literal **ซึ่งกันและกัน** ("to one another") at 5:21 — keeps the egalitarian-frame visible to Thai readers — vs. softening to **ตามลำดับ** ("in order") which would force the complementarian reading. The CC0 evangelical-Protestant frame allows either, and the corpus-precedent for ὑποτάσσω + ἀλλήλοις at LUK 10:17 + 1Co 14:32 is mutual.
3. Confirm Ben endorses **เคารพยำเกรง** ("respect-with-reverence") at 5:33 — preserves the φόβος-of-Christ register from v.21 — vs. literal **เกรงกลัว** ("fear") which would import terror-connotation that the Pauline argument deliberately avoids.

**→ Recommend: STABLE on the locks themselves**, no new doc needed pre-tagging (the per-verse renderings are corpus-precedent-aligned with COL). But Ben's confirmation here is **load-bearing for 1 Pet 2:18–3:7 + 1 Tim 2:8–15 + Tit 2:1–10** — all upcoming Petrine + Pastoral Haustafels will inherit EPH's expanded-pattern, not just COL's brief one.

---

## 2. EPH 1:23 πᾶν τὸ πλήρωμα τοῦ τὰ πάντα ἐν πᾶσιν πληρουμένου — three-way ambiguity preserved — **DECIDE before tagging**

EPH 1:23 contains one of the most-debated single phrases in Pauline-theology — packed into the climax of the eulogia + cosmic-Christology section:

> ἥτις ἐστὶν τὸ σῶμα αὐτοῦ, **τὸ πλήρωμα τοῦ τὰ πάντα ἐν πᾶσιν πληρουμένου**
> ซึ่งคริสตจักรเป็น**กายของพระองค์** คือ **ความบริบูรณ์ของพระองค์ผู้ทรงเติมเต็มทุกสิ่งในทุกประการ**

Three readings hinge on the function of the participle πληρουμένου (middle vs passive) and the referent of πᾶν τὸ πλήρωμα:

| Reading | Claim |
|---|---|
| **(a) Christ-fills-all-things-in-all-people** (active middle) — *currently most-natural in Thai* | Christ as cosmic filler; the church = his fullness as the body that displays his cosmic-presence. |
| **(b) Christ-fills-all-aspects-of-all-things** (active middle, neuter) | Christ comprehensively-saturates every-aspect of all-creation. |
| **(c) The church is the fullness through whom Christ fills the cosmos** (passive sense) | The church is the agency-of-Christ's-cosmic-filling; church-as-Christ's-extension. |

The 1:23 KD explicitly names the three-way debate: "ambiguous between (1) Christ-fills-all-things-in-all-people, (2) Christ-fills-all-aspects-of-all-things, (3) the church is the fullness through whom Christ fills the cosmos. The translation preserves the ambiguity."

**Editorial assessment:** **ทรงเติมเต็มทุกสิ่งในทุกประการ** ("fills all-things in all-respects") is grammatically active-middle (Christ as subject-of-the-filling) and reads most-naturally as reading (a) or (b). Reading (c) — the church-as-instrument-of-Christ's-cosmic-filling — is grammatically possible if πληρουμένου is read as middle-permissive ("being-completed-by"), but is interpretively-stronger and less-natural in Thai. The current rendering thus preserves the (a)/(b) distinction while making (c) recede — defensible per the mainstream English translations (NIV, ESV, CSB, BSB all read this way).

**DECIDE before tagging:**
1. Confirm the (a)/(b)-favoring rendering as corpus-default — the church-as-Christ's-body-displaying-his-cosmic-presence reading. Compounds forward into EPH 3:19 (be-filled with-all-the-fullness-of-God) + EPH 4:10 (Christ ascended to fill all things) + EPH 4:13 (mature-to-fullness-of-Christ) — all four πλήρωμα verses in EPH form a tight Christological-cluster that this 1:23 reading anchors.
2. Alternative: shift to a more passive-friendly rendering (e.g., **คือความบริบูรณ์ของพระองค์ผู้ทรงเติมเต็มทุกสิ่งในทั้งสิ้น โดยทางคริสตจักรนั้น**) — would force the (c) ecclesiology-extension reading. Significantly more interpretive than the Greek itself.

The KD already names the ambiguity but the verse-level rationale doesn't lock a specific reading — Ben's confirmation closes the open question.

---

## 3. EPH 4:8 Ps 68:18 — Pauline-modification "received → gave" — **DECIDE before tagging**

EPH 4:8 is one of the **most-discussed citation-modifications in Paul** — the apostle changes the LXX's "received-gifts among-men" (ἔλαβες δόματα ἐν ἀνθρώπῳ) to "gave-gifts to-men" (ἔδωκεν δόματα τοῖς ἀνθρώποις):

> διὸ λέγει· Ἀναβὰς εἰς ὕψος ᾐχμαλώτευσεν αἰχμαλωσίαν, **ἔδωκεν δόματα τοῖς ἀνθρώποις**
> เพราะฉะนั้นจึงมีคำกล่าวว่า ‘เมื่อพระองค์เสด็จขึ้นสู่ที่สูง พระองค์ได้ทรงนำเชลยไปเป็นเชลย และ**ทรงประทานของประทานแก่มนุษย์**’

The Thai correctly mirrors **Paul's** modified-version, NOT the LXX original. The 4:8 KD explicitly walks through the issue: "the original-LXX has 'received-gifts among/from-men.' Paul changes RECEIVED-FROM (ἔλαβες) to GAVE-TO (ἔδωκεν) — fitting the Christ-ascended-and-gives pattern." The 4:8 thai_summary further explains the modification to Thai readers + cites the Targum-tradition that supports Paul's reading.

**Editorial assessment:** This is **principled** — the Thai must mirror Paul's quotation as Paul wrote it (with the modification), not LXX/MT-Hebrew. The thai-curly-quotes preserve the citation-form without forcing the reader to compare to Hebrew/Greek originals. The thai_summary handles the apparent-discrepancy explicitly. The Pauline-citation is added to `nt_ot_citations.json` with the modification noted.

But — a Thai-reader who consults a Thai OT translation (e.g., THSV1971 Ps 68:18) will see "received-gifts" and may wonder why Paul "changed" it. This is a **CC0 evangelical-Protestant-text-handling question**: should the apparent-modification be footnoted at EPH 4:8, or is the thai_summary disambiguation sufficient?

**DECIDE before tagging:**
1. Confirm the literal-mirror-of-Paul + thai_summary disambiguation strategy is the right approach for EPH 4:8 — keeping the Thai NT clean of footnotes.
2. Alternative: add a one-line footer-note at EPH 4:8 acknowledging the Pauline-modification + the Targum-tradition that supports it. More academically-honest but adds register-burden + sets a precedent for footnoting all citation-modifications across the NT.

This will recur for any Pauline-modified-citation downstream (Rom 9–11 Isaiah quotations; Heb 1 + 2 LXX-citations; etc.).

**→ Recommend: STABLE on the rendering (literal mirror of Paul)**; the question is whether to add a footer-note at this verse.

---

## 4. The eulogia (1:3–14) — Pauline single-period of 200+ words — **STABLE**

The longest single-Greek-period in the NT (vv.3–14, 202 words) — the project's most ambitious Pauline-rhetorical-unit handling to date. The Thai breaks the Greek period into multiple Thai sentences per the thai_summary at 1:3, but preserves:

- **The Trinitarian structure**: vv.3–6 Father's election; vv.7–12 Son's redemption; vv.13–14 Spirit's sealing
- **The threefold "to the praise of his glory" refrain** (vv.6, 12, 14) as structural-bookends, all rendered with **เพื่อสรรเสริญพระสิริ / เป็นที่สรรเสริญพระสิริของพระองค์**
- **The royal-ทรง prefix on every divine-action verb**: ทรงเลือกสรร (v.4), ทรงกำหนด (v.5), ทรงประทาน (v.6), ทรงประทานเทลงมา (v.8), ทรงให้เรารู้จัก (v.9), ทรงดำริ (v.9, v.11), ทรงรวบรวม (v.10) — exemplary `narrator_vs_character_voice_2026-04.md` compliance
- **The cognate-wordplay preserved**: εὐλογητός / εὐλογήσας / εὐλογίᾳ (v.3) → ขอถวายพระพร / ผู้ทรงอวยพร / ด้วยพระพร; χάριτος / ἐχαρίτωσεν (v.6) → ของพระคุณ / โดยพระคุณ; πληρωθῆτε / πλήρωμα (3:19) — all preserved as Pauline-rhetorical-density

**Editorial assessment:** The Thai handling of the eulogia is **the strongest extended-Pauline-prose handling in the corpus to date**. The trinitarian-structure is preserved without artificial-section-headers; the royal-ทรง is uniform; the cognate-pairs are preserved without flattening. **STABLE** ✓ — no action.

---

## 5. ἐπουρανίοις → สวรรคสถาน — EPH-distinctive heavenly-realms phrase — **STABLE-by-translator-lock**

ἐπουρανίοις occurs **only in Ephesians** in the Pauline-corpus (1:3, 1:20, 2:6, 3:10, 6:12 — 5×) and elsewhere only in scattered NT references. The translator chose **สวรรคสถาน** uniformly across all 5 EPH uses:

| Verse | Greek | Thai |
|---|---|---|
| 1:3 | ἐν τοῖς ἐπουρανίοις ἐν Χριστῷ | ในสวรรคสถาน |
| 1:20 | ἐν δεξιᾷ αὐτοῦ ἐν τοῖς ἐπουρανίοις | ที่พระหัตถ์ขวาของพระเจ้าในสวรรคสถาน |
| 2:6 | συνεκάθισεν ἐν τοῖς ἐπουρανίοις ἐν Χριστῷ Ἰησοῦ | ทรงให้เราประทับร่วมกับพระองค์ในสวรรคสถาน |
| 3:10 | ἐν τοῖς ἐπουρανίοις | ในสวรรคสถาน |
| 6:12 | πρὸς τὰ πνευματικὰ τῆς πονηρίας ἐν τοῖς ἐπουρανίοις | วิญญาณชั่วร้ายฝ่ายจิตวิญญาณในสวรรคสถาน |

The 1:3 KD anchors the lock: "Articular substantive 'the-heavenly-things/places.' Ephesians-distinctive phrase ... Refers to the heavenly-realm where Christ is enthroned + believers are 'seated with him.'"

**Editorial assessment:** สวรรคสถาน captures the heavenly-realm-as-place sense (vs. simple **สวรรค์** "heaven" which would lose the place-of-power register). The lexical-uniformity across all 5 uses preserves the Ephesian-distinctiveness — Thai readers see the same phrase recurring and pick up that this is a load-bearing Ephesian-vocabulary. **STABLE** ✓ — exemplary translator-discipline; no corpus doc needed (single-letter pattern).

---

## 6. The cosmic-Christology cluster (1:20–23 + 4:10) — extends `christ_hymn_kenosis_2026-05.md` — **STABLE (recommend amendment per COL audit §1)**

EPH contains the project's THIRD high-Christology cluster (after PHP 2:5–11 + COL 1:15–20). EPH 1:20–23 is the **cosmic-enthronement-and-headship** counterpart to COL 1:15–20's cosmic-creator-and-reconciler:

| Greek (verse) | Thai | Editorial principle |
|---|---|---|
| ἐνήργηκεν ἐν τῷ Χριστῷ ἐγείρας αὐτὸν ἐκ νεκρῶν (1:20a) | ทรงกระทำกิจในพระคริสต์ เมื่อทรงให้พระองค์เป็นขึ้นมาจากความตาย | resurrection-power demonstration |
| καθίσας ἐν δεξιᾷ αὐτοῦ ἐν τοῖς ἐπουρανίοις (1:20b) | ทรงให้พระองค์ประทับที่พระหัตถ์ขวาของพระเจ้าในสวรรคสถาน | Ps 110:1 enthronement (in DB) |
| ὑπεράνω πάσης ἀρχῆς καὶ ἐξουσίας καὶ δυνάμεως καὶ κυριότητος (1:21) | เหนือผู้ครอง ผู้ทรงอำนาจ ผู้ทรงสิทธิ และผู้ทรงเดชานุภาพทั้งปวง | spiritual-beings hierarchy lock — see §7 |
| πάντα ὑπέταξεν ὑπὸ τοὺς πόδας αὐτοῦ (1:22a) | ทรงปราบทุกสิ่งให้อยู่ใต้พระบาทของพระองค์ | Ps 8:6 universal-subjection (in DB) |
| αὐτὸν ἔδωκεν κεφαλὴν ὑπὲρ πάντα τῇ ἐκκλησίᾳ (1:22b) | ทรงประทานพระคริสต์ให้เป็นศีรษะเหนือทุกสิ่งเพื่อคริสตจักร | head-over-all-FOR-the-church |
| τὸ σῶμα αὐτοῦ, τὸ πλήρωμα τοῦ τὰ πάντα ἐν πᾶσιν πληρουμένου (1:23) | กายของพระองค์ คือ ความบริบูรณ์ของพระองค์ผู้ทรงเติมเต็มทุกสิ่งในทุกประการ | πλήρωμα cluster — see §2 |
| ὁ ἀναβὰς ὑπεράνω πάντων τῶν οὐρανῶν, ἵνα πληρώσῃ τὰ πάντα (4:10) | เสด็จขึ้นเหนือฟ้าสวรรค์ทั้งสิ้น เพื่อให้ทรงเติมเต็มทุกสิ่ง | Christ-as-cosmic-filler |
| πληρωθῆτε εἰς πᾶν τὸ πλήρωμα τοῦ θεοῦ (3:19) | เต็มเปี่ยมด้วยความบริบูรณ์ทั้งสิ้นของพระเจ้า | believer-fullness via Christ-fullness |

**Editorial assessment:** The EPH cluster confirms the COL audit's recommendation to lock πλήρωμα → **ความบริบูรณ์ทั้งสิ้น** (or context-shortened **ความบริบูรณ์**) and the cosmic-Christological vocabulary register. The royal-ทรง prefix is uniform on every Christ-action verb. The Ps 110:1 + Ps 8:6 OT-citations are flagged + added to the citations DB.

**Recommend: STABLE; the COL audit's §1 amendment to `christ_hymn_kenosis_2026-05.md`** should now include an **EPH 1:20–23 + 3:19 + 4:10 sub-section** as the THIRD-letter confirmation of the cosmic-Christology lock. EPH provides the "head-of-the-church-which-is-his-body" + "Christ-fills-all-things" Christological-vocabulary not present in PHP or COL.

---

## 7. EPH 1:21 spiritual-beings hierarchy — **LOCKED ✓ (first FULL Pauline-letter confirmation of `spiritual_beings_hierarchy_2026-05.md`)**

EPH 1:21 lists **four classes of spiritual-beings** + adds δύναμις (a fifth lemma not in COL 1:16). This was the trigger-verse for the spiritual-beings doc lock — and the EPH 1:21 rendering was revised on this branch (see `spiritual_beings_hierarchy_2026-05.md`'s "Verses revised this PR" section):

| Greek (1:21) | Thai (locked) | Per doc |
|---|---|---|
| ἀρχῆς | ผู้ครอง | ✓ |
| ἐξουσίας | ผู้ทรงอำนาจ | ✓ |
| δυνάμεως | ผู้ทรงสิทธิ | ✓ |
| κυριότητος | **ผู้ทรงเดชานุภาพ** | ✓ (revised — was previously **เทพผู้ครอง** which collided with `pagan_deities_2026-04.md`) |

EPH 3:10 (ταῖς ἀρχαῖς καὶ ταῖς ἐξουσίαις → **ผู้ครองและผู้ทรงอำนาจ**) ✓ — same lock.

EPH 6:12 extends the cluster with **two NT-HAPAX additions**:

| Greek (6:12) | Thai | Status |
|---|---|---|
| τὰς ἀρχάς | ผู้ครอง | LOCKED ✓ |
| τὰς ἐξουσίας | ผู้ทรงอำนาจ | LOCKED ✓ |
| τοὺς **κοσμοκράτορας** τοῦ σκότους τούτου | **เจ้าโลก**แห่งความมืดในยุคนี้ | NT-HAPAX; new |
| τὰ **πνευματικὰ τῆς πονηρίας** ἐν τοῖς ἐπουρανίοις | **วิญญาณชั่วร้ายฝ่ายจิตวิญญาณ**ในสวรรคสถาน | EPH-distinctive |

**Editorial assessment:** The 4-tier 1:21 cluster is **the cleanest test of the spiritual-beings-hierarchy lock yet** — same lemmas as COL 1:16 (3 of 4) + adds δύναμις, all rendered per the lock. The EPH 6:12 4-fold spiritual-warfare cluster is genuinely new — the κοσμοκράτωρ → **เจ้าโลก** is a clean Thai compound, and **วิญญาณชั่วร้ายฝ่ายจิตวิญญาณ** preserves the πνευματικά substantive without flattening to "evil spirits."

**Recommend: LOCKED ✓** for EPH 1:21 + 3:10. **STABLE** for EPH 6:12's two new lemmas — recommend extending `spiritual_beings_hierarchy_2026-05.md` with a brief **§ "Eph 6:12 expansion"** sub-section locking κοσμοκράτωρ → **เจ้าโลก** + πνευματικὰ τῆς πονηρίας → **วิญญาณชั่วร้ายฝ่ายจิตวิญญาณ** as the corpus-default for cosmic-warfare contexts. Important pre-Rev 12 + Rev 16:14 (where similar cosmic-warfare vocabulary recurs).

---

## 8. The armor-of-God (6:10–17) — military-metaphor cluster — **REVIEW (8 HAPAXES; register check)**

EPH 6:10–17 contains **eight NT-HAPAXES** in 8 verses, all rendered with reasonable Thai military-vocabulary equivalents:

| Verse | Greek (HAPAX) | Thai | Sense |
|---|---|---|---|
| 6:11 | πανοπλία | ยุทโธปกรณ์ครบชุด | full-armor / panoply |
| 6:12 | πάλη | การต่อสู้ | wrestling / struggle |
| 6:12 | κοσμοκράτωρ | เจ้าโลก | cosmic-ruler (see §7) |
| 6:14 | ζώννυμι (rare; not strictly HAPAX) | คาด | belt / gird |
| 6:15 | ἑτοιμασία | ความพร้อม | readiness / preparation |
| 6:16 | θυρεός | โล่ | large-shield (Roman scutum) |
| 6:16 | βέλος | ลูกศร | arrow / dart |
| 6:18 | προσκαρτέρησις | ความพากเพียร | perseverance |

Plus the OT-echo cluster: 6:14 (Isa 11:5 belt-of-righteousness; Isa 59:17 breastplate); 6:15 (Isa 52:7 feet-of-good-news-bringers); 6:17 (Isa 59:17 helmet-of-salvation) — all 4 added to `nt_ot_citations.json`.

**Editorial assessment:** The Thai military-vocabulary is principled — **ยุทโธปกรณ์** (military-equipment, Sanskrit-rooted compound) for πανοπλία preserves the full-equipment register; **โล่** for the large Roman scutum is the standard Thai for shield; **เสื้อเกราะ** (breastplate) for θώραξ is corpus-precedent. The Pauline-soldier-imagery is preserved without forcing modern-military or ancient-Roman-historical register.

**REVIEW flag:** The Thai military-register may sound either too-archaic (ยุทโธปกรณ์ + โซ่ตรวน at 6:20) or too-contemporary (ลูกศรไฟ "flame-arrow" — hard to make less-modern in Thai). Worth Ben's confirmation that the register matches the EPH-evangelical-Thai-reader-ear and doesn't drift into either fantasy-game or historical-documentary register.

**→ Recommend: STABLE** in principle; verse-level renderings are corpus-precedent-aligned where corpus exists. Not pre-tagging-blocking; worth a one-line note in any future review.

---

## 9. EPH 4:9 κατώτερα μέρη τῆς γῆς — descent-to-earth vs descent-to-Hades — **REVIEW**

EPH 4:9 is the most-debated single phrase in EPH-soteriology — bound up with the Apostles'-Creed "descended-into-hell" question:

> τὸ δὲ Ἀνέβη τί ἐστιν εἰ μὴ ὅτι καὶ κατέβη εἰς **τὰ κατώτερα μέρη τῆς γῆς**
> แต่คำว่า ‘เสด็จขึ้น’ นั้นหมายความอย่างไร นอกจากว่าพระองค์ก็ได้เสด็จลงไปสู่**ส่วนที่ต่ำกว่าของแผ่นดินโลก**ด้วย?

Two readings:

| Reading | Claim |
|---|---|
| **(a) Descent to-the-earth** ("the lower-region, i.e., the earth") — incarnation-descent | Christ descended TO the earth (genitive of apposition: "the earth itself, as the lower-region"). Lutheran / Reformed mainstream + most modern English Bibles. |
| **(b) Descent below-the-earth** ("the lower-parts of-the-earth, i.e., Sheol/Hades") — descent-to-the-dead | Christ descended INTO the underworld (cf. 1 Pet 3:19 "preached to spirits in prison"). Older patristic + Roman-Catholic + some-Reformed reading. |

The 4:9 KD acknowledges both: "Per uW: ambiguous — (1) 'the-earth-as-the-lower-region' (i.e., descent-to-the-earth in incarnation), (2) 'the-lower-parts-OF-the-earth' (i.e., descent-to-the-realm-of-the-dead/Sheol). Pauline-context favors (1) but (2) is theologically-traditional."

**Editorial assessment:** The Thai **ส่วนที่ต่ำกว่าของแผ่นดินโลก** ("the lower-parts of the earth") is **literally-bare** — it leaves both readings open in Thai exactly as in Greek. This is principled (genuine ambiguity preserved); it does mean Thai-readers without commentary will probably default to (b) "descent below-the-earth" because the literal preposition reads spatially.

**REVIEW:** Confirm the literal-ambiguity-preserving rendering is the right choice for the CC0 evangelical-Protestant Thai Bible. Alternative: shift to **ลงมาสู่แผ่นดินโลกซึ่งเป็นที่ต่ำกว่า** ("down to the earth, which is the lower-region") — would force reading (a), match NIV/ESV, and align with mainstream-evangelical reading.

**→ Recommend: STABLE** with the literal-ambiguity preserved; Ben's confirmation closes the open question.

---

## 10. EPH 5:14 unidentified citation — **REVIEW**

EPH 5:14 contains the only NT-citation **without an identified OT source** in the project so far:

> διὸ λέγει· **Ἔγειρε, ὁ καθεύδων, καὶ ἀνάστα ἐκ τῶν νεκρῶν, καὶ ἐπιφαύσει σοι ὁ Χριστός**
> เพราะฉะนั้นจึงมีคำกล่าวว่า ‘**จงตื่นเถิด ผู้ที่กำลังหลับ จงลุกขึ้นจากความตาย แล้วพระคริสต์จะทรงส่องแสงเหนือเจ้า**’

Likely sources: an early-Christian baptismal-hymn fragment, OR a Pauline-paraphrase of Isa 60:1 LXX (φωτίζου, φωτίζου, Ιερουσαλήμ ... ἥκει σου τὸ φῶς). The 5:14 KD acknowledges the source-uncertainty + the 5:14 thai_summary explains the early-Christian-hymn possibility to Thai readers.

**Editorial assessment:** The Thai-curly-quotes preserve the citation-form per RULES §5b; the thai_summary handles the source-uncertainty. The HAPAX ἐπιφαύσκω → **ทรงส่องแสง** (with royal-ทรง for Christ-as-divine-subject) is principled. The early-baptismal-hymn theory dovetails with v.26's λουτρόν+ῥῆμα (see §11) — both verses suggest baptismal-tradition material in EPH 5.

**REVIEW:** Confirm the citation-marked-without-identified-source approach is acceptable for the corpus. NOT in `nt_ot_citations.json` (no OT source to cite). The thai-curly-quote + thai_summary disambiguation is the only-handling-mechanism currently in place.

**→ Recommend: STABLE** (no action needed; thai_summary handles); Ben's confirmation closes.

---

## 11. EPH 5:26 λουτρόν+ῥῆμα — baptism-and-word imagery — **REVIEW**

EPH 5:26 contains the most-condensed baptismal-and-word formula in the Pauline-corpus:

> ἵνα αὐτὴν ἁγιάσῃ καθαρίσας **τῷ λουτρῷ τοῦ ὕδατος ἐν ῥήματι**
> เพื่อพระองค์จะทรงชำระคริสตจักรให้บริสุทธิ์ โดย**ทรงล้างด้วยการชะล้างน้ำผ่านพระวจนะ**

The Thai **การชะล้างน้ำผ่านพระวจนะ** preserves both: λουτρόν → **การชะล้าง** (washing — corpus-precedent at Tit 3:5 same lemma), ὕδατος → **น้ำ**, ἐν ῥήματι → **ผ่านพระวจนะ** (through-the-word). The 5:26 KD names the baptismal-allusion + the word-of-God-in-baptismal-instruction reading.

**Editorial assessment:** The Thai is principled and preserves both layers. Note ῥῆμα ("specific-spoken-word") is distinct from λόγος ("general-message") — the rendering **พระวจนะ** is the same as for λόγος (corpus-default), which slightly flattens the ῥῆμα distinction. EPH uses ῥῆμα four times (5:26; 6:17 "sword of the Spirit, which is ῥῆμα θεοῦ"; in both the rendering is **พระวจนะ**).

**REVIEW:** Should ῥῆμα be distinguished from λόγος in Thai (e.g., **ถ้อยพระดำรัส** for ῥῆμα at 5:26 + 6:17, vs. **พระวจนะ** for λόγος)? The translator chose to flatten; the alternative would distinguish but adds Thai-lexical-load that may not match the Greek's actual semantic-distance.

**→ Recommend: STABLE** with the flattened **พระวจνะ** rendering — preserves corpus-uniformity. Ben's confirmation closes.

---

## 12. EPH 4:11 fivefold ministry — pastor-and-teacher article-sharing — **REVIEW**

EPH 4:11 contains the famous **fivefold-or-fourfold-ministry-list**:

> καὶ αὐτὸς ἔδωκεν τοὺς μὲν ἀποστόλους, τοὺς δὲ προφήτας, τοὺς δὲ εὐαγγελιστάς, τοὺς δὲ **ποιμένας καὶ διδασκάλους**
> และพระองค์เองได้ทรงประทานบางคนให้เป็น**อัครทูต** บางคนเป็น**ผู้เผยพระวจνะ** บางคนเป็น**ผู้ประกาศข่าวประเสริฐ** และบางคนเป็น**ศิษยาภิบาลและอาจารย์**

The Greek **τοὺς δὲ ποιμένας καὶ διδασκάλους** uses a **single article** governing both ποιμένας and διδασκάλους (Granville-Sharp-style construction) — strongly suggesting a single combined office (pastor-teacher) rather than two-separate offices. The 4:11 notes flag this: "pastor and teacher share a single article in Greek ('the some-as pastors-and-teachers'), suggesting a combined-role rather than two-separate-offices."

**Editorial assessment:** The Thai **ศิษยาภิบาลและอาจารย์** preserves both nouns as if they were two-distinct-roles ("pastors and teachers") — which is the **most-common-evangelical-reading** but does flatten the Granville-Sharp-suggested combined-office reading. ποιμήν → **ศิษยาภิบาล** is the standard Thai-Christian rendering for the modern pastor-office (as opposed to **ผู้เลี้ยงแกะ** "shepherd" used at Mat 26:31 — context-disambiguated).

**REVIEW:** Confirm the four-nouns-rendering is right (vs. compounding the last-pair as **ศิษยาภิβาล-อาจารย์** "pastor-teacher" with hyphen, or **ศิษยาภิบาลผู้สั่งสอน** "teaching-pastor"). The fivefold-or-fourfold debate is theologically-load-bearing in modern church-polity discussions; the Thai handling tilts toward fivefold without explicitly excluding the combined-reading.

**→ Recommend: STABLE** with the fivefold-rendering — matches the most-common evangelical-Thai reading. Ben's confirmation closes.

---

## 13. πατήρ register split — **LOCKED ✓ (third Pauline-letter confirmation)**

EPH has 11 πατήρ-cluster occurrences with the same principled register-split as GAL + PHP + 1TH + COL:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:2 | θεοῦ πατρὸς ἡμῶν | **พระเจ้าพระบิดาของเรา** | divine (royal pระ-) |
| 1:3 | ὁ θεὸς καὶ πατὴρ τοῦ κυρίου ἡμῶν | **พระเจ้าและพระบิดา**แห่งพระเยซูคริสต์ | divine (Granville Sharp; royal) |
| 1:17 | ὁ πατὴρ τῆς δόξης | **พระบิดา**แห่งพระสิริ | divine (royal) |
| 2:18 | πρὸς τὸν πατέρα | **พระบิดา** | divine (royal — Trinitarian access formula) |
| 3:14 | πρὸς τὸν πατέρα | **พระบิดา** | divine (royal — prayer posture) |
| 3:15 | πᾶσα πατριά | **ทุกครอบครัว** | derived noun (family — context-distinct lemma) |
| 4:6 | εἷς θεὸς καὶ πατὴρ πάντων | **พระเจ้าและพระบิดา** | divine (royal — climactic of seven-fold-one) |
| 5:31 (Gen 2:24 quotation) | τὸν πατέρα καὶ τὴν μητέρα | **บิดามารดา** | human-paternal (plain — quoted OT) |
| 6:2 (Exod 20:12 quotation) | τὸν πατέρα σου | **บิดาของเจ้า** | human-paternal (plain — quoted OT 5th Commandment) |
| 6:4 | οἱ πατέρες | **บิดาทั้งหลาย** | human-paternal Haustafel address (plain — NOT royal) |
| 6:23 | θεοῦ πατρὸς | **พระเจ้าพระบิδา** | divine (royal — closing benediction) |

**Editorial assessment:** Perfect compliance with `narrator_vs_character_voice_2026-04.md`. The **8 divine-πατήρ → พระบิดา** (royal) + **3 human-paternal → บิดา** (plain) split is exact. The Haustafel-address **บิดาทั้งหลาย** at 6:4 is the plain-register parallel to COL 3:21's **บิดาทั้งหลาย** (per `narrator_vs_character_voice_2026-04.md` lock — confirmed at the COL audit §12). EPH gives the **third Pauline-letter confirmation** of the lock.

**LOCKED** ✓ — no action.

---

## 14. σάρξ polysemy with explicit RULES §5 flags — **STABLE (extends COL pattern; recommend `sarx_pauline_2026-05.md` doc)**

EPH has **9 σάρξ occurrences across 8 verses**, with the translator explicitly tagging each polysemy-instance with the RULES §5 flag — same exemplary discipline as COL audit §7:

| Sense | Verse | Greek context | Thai |
|---|---|---|---|
| **Hebraic idiom (flesh-and-blood = humans)** | 6:12 | πρὸς αἷμα καὶ σάρκα | **เลือดและเนื้อ** |
| **Neutral physical-body / earthly status** | 2:11 | τὰ ἔθνη ἐν σαρκί / ἐν σαρκὶ χειροποιήτου | **คนต่างชาติทางเนื้อหนัง / ทางเนื้อหนังโดยมือมนุษย์** |
| | 5:29 | οὐδεὶς γάρ ποτε τὴν ἑαυτοῦ σάρκα ἐμίσησεν | **ร่างกายของตน** |
| | 6:5 | τοῖς κατὰ σάρκα κυρίοις | **นายของตนตามฝ่ายเนื้อหนัง** |
| **Christ's earthly-physical body** | 2:14 | τὴν ἔχθραν ἐν τῇ σαρκὶ αὐτοῦ | **ในพระวรกายของพระองค์** (royal-pระ-) |
| **Mode-of-birth contrast** | 2:3 | ἐν ταῖς ἐπιθυμίαις τῆς σαρκὸς ἡμῶν / τὰ θελήματα τῆς σαρκὸς | **ในตัณหาของฝ่ายเนื้อหนังของเรา / ความปรารถνาของฝ่ายเนื้อหนัง** |
| **Christ-and-church one-flesh (Gen 2:24 quotation)** | 5:31 | ἔσονται οἱ δύο εἰς σάρκα μίαν | **เป็นเนื้ออันเดียวกัน** |

Every polysemous-σάρξ KD includes "POLYSEMOUS σάρξ flag (per RULES §5)" — exemplary discipline (matches COL). The 2:14 royal-prefixed **พระวรกาย** for Christ's-earthly-body extends the COL 1:22 sub-sense; the 5:31 **เนื้ออันเดียว** preserves the OT-quotation Hebraic idiom distinct from the Pauline-moral-σάρξ register.

**Editorial assessment:** EPH gives the **second-letter-pattern confirmation** for the σάρξ-handling COL exemplified. The recommended `sarx_pauline_2026-05.md` corpus doc (per GAL audit §6 + COL audit §7) is now overdue — both letters are shipped + compliant.

**Recommend: STABLE; finally lift to corpus doc** `docs/translator_decisions/sarx_pauline_2026-05.md` per the COL audit's recommendation. The doc should now cite **GAL + COL + EPH** as the three-letter-pattern locking precedents (EPH adds the Hebraic-flesh-and-blood idiom at 6:12 + the Gen-2:24-quotation one-flesh sense at 5:31 as additional sub-senses to lock).

---

## 15. Inherited locks — **all compliant**

| Doc | EPH evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 1:22, 3:10, 3:21, 5:23, 5:24, 5:25, 5:27, 5:29, 5:32 → **คริสตจักร** uniform (9 occurrences). | **LOCKED** |
| `ethnos_2026-04.md` | 2:11, 3:1, 3:6, 3:8, 4:17 → **คนต่างชาติ** uniform Pauline-mission contexts. | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 6+ narrator-κύριος uses (1:2, 1:3, 1:15, 1:17, 5:10, 5:17, 5:19, 5:20, 5:22, 6:1, 6:4, 6:7, 6:8, 6:10, 6:21, 6:23, 6:24) → **องค์พระผู้เป็นเจ้า** uniform. (Doc still flagged for amendment per JHN+GAL audits.) | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | πατήρ register split exact (§13). Royal ทรง- on every divine-action verb in chs.1–3 + every Christ-action in chs.4–6. **บิดา** plain-register at 5:31 (Gen 2:24) + 6:2 (Exod 20:12) + 6:4 (Haustafel). | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | EPH 1:6, 1:12, 1:14 (the threefold "to the praise of his glory" refrain) → **เพื่อสรรเสริญพระสิริ / เป็นที่สรรเสริญพระสิริของพระองค์** — ἔπαινος as praise-act of-praising rendered consistently. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic embeds in EPH. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | N/A in EPH; the **เทพ-class register** is correctly avoided in 1:21 / 3:10 / 6:12 spiritual-beings cluster (the trigger for the `spiritual_beings_hierarchy_2026-05.md` lock). | **LOCKED** |
| `inclusion_variants_absent_verses_2026-04.md` | N/A in main-text variants in EPH. The 1:1 ἐν Ἐφέσῳ omission-variant + the 5:30 "flesh and bones" extension are **silent-inclusion / silent-omission per RULES §5** (mainstream critical-text matches our practice). The 5:30 case has a resolved-variant doc at `output/textual_variants/_resolved/ephesians_05_v30_flesh_bones.md`. | **LOCKED (N/A — RULES §5 silent)** |
| `historic_present_2026-04.md` | N/A — Ephesians is a doctrinal-ethical letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in EPH. The 5:22–33 marriage-typology uses plain-register **บิดามารดา / สามี / ภรรยา** (correct — analogical, not transparent God-figures). | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω absent from EPH. | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | EPH 1:7 (τὴν ἄφεσιν τῶν παραπτωμάτων) → **การยกโทษการล่วงละเมิด**. Same lemma as COL 1:14 (ἁμαρτιῶν there); EPH uses παραπτώματα (transgressions) — slightly-distinct lemma, same Pauline-locked rendering of the ἄφεσις-phrase per the doc. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman titles in EPH. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from EPH. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (4:30 + 1:13 + 4:4 etc.) → **พระวิญญาณบริสุทธิ์ / พระวิญญาณ** uniform. ψυχή absent except at 6:6 (ἐκ ψυχῆς → **จากจิตวิญญาณ** — corpus-precedent at COL 3:23). | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — Pauline. The closing **ἀμήν** at 3:21 → **อาเมน**. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries in EPH. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | EPH 5:5 (ἐν τῇ βασιλείᾳ τοῦ Χριστοῦ καὶ θεοῦ) → **อาณาจักรของพระคริสต์และของพระเจ้า** — corpus-locked. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | EPH 1:10 (ἐν τοῖς οὐρανοῖς), 3:15, 4:10 (πάντων τῶν οὐρανῶν), 6:9 (ἐν οὐρανοῖς) → **สวรรค์** consistent. The EPH-distinctive ἐπουρανίοις → **สวรρคสถาν** (§5) is treated separately. | **LOCKED** |
| `pistis_christou_2026-05.md` | EPH 1:15 (πίστιν ἐν τῷ κυρίῳ Ἰησοῦ) → **ความเชื่อในพระเยซูองค์พระผู้เป็นเจ้า** (objective-genitive explicit per ἐν-construction); EPH 3:12 (πίστεως αὐτοῦ) → **ความเชื่อในพระองค์** (objective per the doc); EPH 2:8 (διὰ πίστεως) → **ผ่านทางความเชื่อ** (the climactic Pauline-soteriology summary). 1:15 + 3:12 KDs explicitly cite the doc. | **LOCKED** |
| `huiothesia_adoption_2026-05.md` | EPH 1:5 (εἰς υἱοθεσίαν) → **เพื่อให้ได้รับสิทธิ์การเป็นบุตร**. KD explicitly cites the doc. | **LOCKED** |
| `diakonos_pauline_2026-05.md` | EPH 3:7 (διάκονος of Paul) → **ผู้รับใช้**; EPH 6:21 (πιστὸς διάκονος of Tychicus) → **ผู้รับใช้ที่สัตย์ซื่อ** — both per the doc. | **LOCKED** |
| `dikaioo_dikaiosyne_family_2026-05.md` | EPH has no δικαιόω-justification verses (the doctrine-locus shifts to redemption + ἀπολύτρωσις in EPH). δικαιοσύνη appears only in ethical-virtue contexts (4:24, 5:9, 6:14) → **ความชอบธรรม** consistent with the abstract-noun rendering per the doc. | **LOCKED (verb absent; noun lemma compliant)** |
| `nomos_pauline_2026-05.md` | EPH has only ONE νόμος occurrence: 2:15 (τὸν νόμον τῶν ἐντολῶν ἐν δόγμασιν → **ธรรมบัญญัติแห่งข้อบัญญัติและข้อบังคับ**) — per the doc's single-rendering policy. The Mosaic-ceremonial-law sense is contextually clear. | **LOCKED** |
| `sarx_pauline_2026-05.md` | **DOC NOT YET WRITTEN.** EPH compliant per §14 above. Recommended write — see §14. | **(pending doc)** |
| `christ_hymn_kenosis_2026-05.md` | EPH 1:20–23 + 3:19 + 4:10 cosmic-Christology compliant per §6. **Recommend amendment** per COL audit §1 to include EPH cluster as third-letter-confirmation. | **LOCKED (recommend amendment)** |
| `prototokos_pauline_2026-05.md` | N/A in EPH (no πρωτότοκος uses). | **LOCKED (N/A; pending doc per COL recommendation)** |
| `parousia_christou_2026-05.md` | N/A in EPH (no παρουσία uses). | **LOCKED (N/A)** |
| `phroneo_pauline_2026-05.md` | N/A in EPH (no φρονέω uses). | **LOCKED (N/A)** |
| `proper_noun_wordplay_2026-05.md` | N/A — no Pauline-proper-noun-wordplay in EPH (PHM-specific Onesimus pun is the doc's anchor). | **LOCKED (N/A)** |
| `spiritual_beings_hierarchy_2026-05.md` | EPH 1:21 + 3:10 + 6:12 — **first FULL Pauline-letter confirmation** (§7). EPH 6:12 extends with κοσμοκράτωρ + πνευματικὰ τῆς πονηρίας — recommend doc-extension. | **LOCKED (recommend extension per §7)** |
| `stoicheia_tou_kosmou_2026-05.md` | **N/A in EPH** (no στοιχεῖα uses). The COL audit's deferred recommendation stands. | **LOCKED (N/A; doc still pending per COL recommendation)** |
| `honorifics_non_divine_authorities_2026-04.md` | N/A in EPH narrative; **บิดา / สามี / นาย** in the Haustafel are plain-register household-roles, correctly handled. | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in EPH (no vocative κύριε; doctrinal-ethical letter not narrative). | **LOCKED (N/A)** |
| `adversary_speech_register_2026-05.md` | N/A in EPH (no narrative). | **LOCKED (N/A)** |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | EPH 5:3 (πορνεία → **การล่วงประเวณี**) — corpus-default per the deferred doc; no μοιχεία in EPH. | **LOCKED (deferred-status preserved)** |
| `telos_paidagogos_christ_2026-05.md` | N/A in EPH (no τέλος-νόμου context, no παιδαγωγός). | **LOCKED (N/A)** |

---

## Mechanical (§1) — **all green**

- 6/6 chapters: `output/check_reports/ephesians_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 6/6 chapters: `output/back_translations/ephesians_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 193-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only the re-ran-check artifact (`key_term_consistency_all.md`) plus the resolved-variant doc + paratext SFM (untracked, generated-by-ship-script). No EPH source-file dirt.

---

## Pre-existing docs affirmed / unchanged

All 40 docs in `docs/translator_decisions/` reviewed. Compliance summary in §15 above. **`spiritual_beings_hierarchy_2026-05.md` recommended for extension** (κοσμοκράτωρ + πνευματικὰ τῆς πονηρίας from EPH 6:12). **`christ_hymn_kenosis_2026-05.md` recommended for amendment** (EPH 1:20–23 + 3:19 + 4:10 cosmic-Christology cluster — per COL audit §1's already-pending recommendation; EPH provides third-letter confirmation). **`sarx_pauline_2026-05.md` still-pending** (now overdue: GAL+COL+EPH three-letter-pattern compliant; should be written before Romans 7).

---

## Flagged for Ben's attention

### A. The EXPANDED Pauline Haustafel (5:22–6:9) — **DECIDE before tagging** (§1)
Confirm:
1. The **ยอมอยู่ใต้บังคับ** lock at 5:22, 5:24 — corpus-precedent-aligned with COL 3:18.
2. The literal **ซึ่งกันและกัน** ("to one another") preservation at 5:21 — keeps the egalitarian-mutual-submission frame visible.
3. The **เคารพยำเกรง** ("respect-with-reverence") at 5:33 — matches the φόβος-of-Christ register from v.21.

EPH is the corpus-ANCHOR for Pauline marriage-doctrine; the lock cannot be revisited later without back-incompatibility into 1 Pet 2:18–3:7 + 1 Tim 2:8–15 + Tit 2:1–10.

### B. EPH 1:23 πᾶν τὸ πλήρωμα τοῦ τὰ πάντα ἐν πᾶσιν πληρουμένου — **DECIDE** (§2)
Confirm the (a)/(b)-favoring rendering — Christ-fills-all-things-in-all-people / Christ-fills-all-aspects — vs. shifting to (c) the-church-as-instrument-of-Christ's-cosmic-filling. Compounds forward into EPH 3:19 + 4:10 + 4:13 (the 4-verse πλήρωμα cluster).

### C. EPH 4:8 Ps 68:18 Pauline-modification "received → gave" — **DECIDE** (§3)
Confirm the literal-mirror-of-Paul + thai_summary disambiguation strategy — vs. adding a one-line footer-note acknowledging the modification. Sets a precedent for all Pauline-modified-citations downstream.

### D. EPH 4:9 κατώτερα μέρη τῆς γῆς descent ambiguity — **REVIEW** (§9)
Confirm the literal-ambiguity-preserving rendering vs. forcing the (a) descent-to-earth incarnation reading.

### E. EPH 5:14 unidentified citation — **REVIEW** (§10)
Confirm the citation-marked-without-source approach + thai_summary explanation.

### F. EPH 5:26 λουτρόν+ῥῆμα baptism-and-word — **REVIEW** (§11)
Confirm flattening ῥῆμα → **พระวจνะ** (vs. distinguishing from λόγος).

### G. EPH 4:11 fivefold-ministry pastor-and-teacher — **REVIEW** (§12)
Confirm the four-distinct-nouns rendering (fivefold reading) vs. compounding the last pair (fourfold reading).

### H. EPH 6:10–17 armor-of-God military register — **REVIEW** (§8)
Confirm the **ยุทโธปกรณ์ครบชุด / โล่ / เสื้อเกราะ** military-vocabulary register matches the EPH-evangelical-Thai-reader-ear (not too-archaic, not too-fantasy-game).

### I. New corpus docs to write (already-pending from prior audits)
1. **`docs/translator_decisions/sarx_pauline_2026-05.md`** — overdue (GAL+COL+EPH compliant; before Rom 7)
2. **(Already pending)** `prototokos_pauline_2026-05.md` (per COL audit §2 — N/A in EPH)
3. **(Already pending)** `stoicheia_tou_kosmou_2026-05.md` (per GAL+COL audits — N/A in EPH)

### J. Existing docs to amend
- **`spiritual_beings_hierarchy_2026-05.md`** — extend with EPH 6:12 sub-section locking κοσμοκράτωρ → **เจ้าโลก** + πνευματικὰ τῆς πονηρίας → **วิญญาณชั่วร้ายฝ่ายจิตวิญญาณ** (§7)
- **`christ_hymn_kenosis_2026-05.md`** — per COL audit §1's pending amendment, fold in EPH 1:20–23 + 3:19 + 4:10 cosmic-Christology cluster as third-letter confirmation (§6)
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — already flagged-for-amendment in JHN+GAL audits; EPH provides further confirmation (16+ narrator-κύριος uses, all compliant)

### K. External AI review (§3 of checklist) — **pending**
Recommended before `book-ephesians-v1` tag. Suggested 4-cluster external AI packet:
1. **EPH 1:3–14** — the eulogia + Trinitarian structure + threefold-praise-refrain + cosmic-election
2. **EPH 1:20–23 + 2:11–22** — cosmic-Christology + Jew-Gentile unity-mystery
3. **EPH 4:7–13** — Ps 68:18 modification + descent-and-ascent + fivefold-ministry-list
4. **EPH 5:21–6:9** — the EXPANDED Pauline Haustafel + Christ-and-church-marriage-typology + slave-master code

Use Grok + ChatGPT in parallel per the JHN/COL/GAL pattern.

---

## Recommendation

**Ephesians ships in strong corpus-hygiene shape — and confirms two recently-locked corpus docs at corpus-scale** (`spiritual_beings_hierarchy_2026-05.md` first FULL Pauline confirmation; `huiothesia_adoption_2026-05.md` + `pistis_christou_2026-05.md` + `diakonos_pauline_2026-05.md` all explicitly cited at the verse-level). The single most editorially-load-bearing item is the EXPANDED Pauline Haustafel (5:22–6:9) — **22 verses anchoring the entire NT marriage-and-household-code tradition**. Three DECIDE items + five REVIEW items need Ben's confirmation before the tag.

Tag `book-ephesians-v1` after:
1. Ben's decisions on **§A + §B + §C** (DECIDE items: Haustafel locks; 1:23 πλήρωμα reading; 4:8 Ps 68:18 modification handling)
2. Ben's confirmations on **§D + §E + §F + §G + §H** (REVIEW items: 4:9 descent ambiguity; 5:14 citation; 5:26 ῥῆμα flattening; 4:11 fivefold; 6:10–17 armor register)
3. Existing docs amended (`spiritual_beings_hierarchy_2026-05.md` per §7; `christ_hymn_kenosis_2026-05.md` per §6 — the COL-audit-already-pending amendment now covers EPH too)
4. The overdue `sarx_pauline_2026-05.md` written (GAL+COL+EPH three-letter-pattern; before Romans 7)
5. External AI sanity-check (§K)

**The Captivity-Letters cluster (PHP, COL, EPH) is now complete.** PHM remains as the brief Captivity-coda. The Pauline corpus's biggest forward-load is now Romans (where δικαιόω + νόμος + σάρξ all compound massively). The EPH ship strengthens the Pauline-corpus's hygiene profile heading into Romans.
