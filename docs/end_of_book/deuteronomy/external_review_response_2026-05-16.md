# Deuteronomy external review — response + actions taken

**Date:** 2026-05-16
**Audit packet:** `external_review_items_DEU.md`
**Reviewers:** Gemini + ChatGPT (both consulted; verdicts converged on all six items)
**Status:** all DECIDE items resolved; book-deuteronomy-v1 unblocked

---

## Summary of actions

| Item | Verdict | Action |
|---|---|---|
| **A** — DEU 5:9–10 Sinai attribute formula | MAJOR CONCERN | Retroactively normalized DEU 5:9–10, EXO 20:5–6, NUM 14:18 to the canonical Thai paqad+chesed Decalogue surface. `exod_34_attribute_formula_2026-05.md` §1.4 added (Decalogue paqad/chesed lock) + Decalogue recitations added to locked-recitations list. |
| **B** — Decalogue EXO 20 // DEU 5 parallel-text drift | MAJOR CONCERN | New `decalogue_parallel_text_2026-05.md` written. DEU 5:6 (เรือนทาส), 5:7, 5:8, 5:11, 5:17–20, 5:21 prohibitive frame normalized to "อย่า + verb" (matching EXO 20). DEU 5:19 lemma normalized: ขโมย → ลักทรัพย์. DEU 5:16 ยืนยาว preserved (Eph 6:2–3 NT-quotation alignment with DEU's expanded Hebrew). Synoptic + Pauline + Jacobean Decalogue citations staged for NT-side reaudit. |
| **C** — NT-cross-corpus DEU-quote cluster | MAJOR CONCERN | New `ot_nt_cross_quotation_thread_2026-05.md` written. DEU 18:9–22 prophet-cluster (vv.15, 18, 19, 20, 22) normalized: ผู้พยากรณ์ → ผู้เผยพระวจนะ. DEU 25:4 normalized to canonical muzzle-ox surface "อย่าเอาผ้าผูกปากวัวขณะมันกำลังนวดข้าว" (Pauline NT-citation thread lock). DEU 11:13 within-DEU Shema drift fixed: สุดจิต → สุดจิตวิญญาณ. NT-side reaudits (Acts 3:22, 7:37; 1 Cor 9:9; 1 Tim 5:18; Synoptic Shema; Matt-4 temptation-quotes) staged. |
| **D** — Ḥerem 5-way Thai-surface drift | MAJOR/CONCERN | `ot_warfare_ethics_2026-05.md` §4.1 amended (Thai-surface lock added: canonical = ทุ่มถวายเพื่อทำลาย). DEU 2:34 retains transliterated เฮเรม at first occurrence + new Layer-2 first-occurrence footer. DEU 3:6, 7:2, 7:26 (×2) normalized to canonical surface. Layer-2 back-pointer footers added to chs 2, 3, 7, 13 pointing to DEU 20:17 anchor. |
| **E** — DEU 32:43 LXX/Heb 1:6 expansion | FINE WITH FOOTER AMENDMENT | DEU 32:43 Layer-2 footer amended to explicitly state the asymmetric-witness rationale (32:8 follows DSS/LXX with strong 4QDeut^j corroboration; 32:43 retains MT despite LXX/4QDeut^q expansion quoted in Heb 1:6 — weaker witness). Disposition stays MT-with-Layer-2; transparency added per both reviewers. |
| **F** — Pisgah + Seven-Nations drift | CONCERN | DEU 34:1 mechanical typo fixed: ปิสกาห์ → พิสกาห์. DEU 20:17 seven-nations normalized to match DEU 7:1 surface (ชาว- prefix + bare ethnonym): คนฮิตไทต์/คนอาโมไรต์/คนคานาอัน/คนเปริสซีต/คนฮีไวต์/คนเยบุสีต → ชาวฮิตไทต์/ชาวอาโมไรต์/ชาวคานาอัน/ชาวเปริซซี/ชาวฮีไว/ชาวเยบุส. Within-DEU follow-on drifts found by the new check (§Z below) fixed: DEU 11:30 (คนคานาอัน → ชาวคานาอัน), DEU 31:4 (คนอาโมไรต์ → ชาวอาโมไรต์). `proper_names_and_transliteration_2026-05.md` amended with seven-nations cluster lock + trans-Jordan place-names section. |
| **§Z** — Proper-noun glossary regex check | CONSIDER ADDING | New `data/proper_noun_locks.json` (lock data) + new `scripts/check_proper_nouns.py` (Thai-side rejected-surface auditor) written. Initial corpus run finds 26 rejected-surface violations across GEN/EXO/NUM/DEU; the 2 DEU-internal ones fixed in this pass. The other 24 (GEN/EXO/NUM cross-corpus surface drifts) are documented as forward-protection scope for the next per-book end-of-book audits. Wiring into `run_checks.py` is left as a follow-up step (script is invocable manually as `python3 scripts/check_proper_nouns.py --all --report`). |

---

## Verses edited

### DEU translations
- DEU 5:6, 5:7, 5:8, 5:9, 5:10, 5:11, 5:17, 5:18, 5:19, 5:20, 5:21 — Decalogue normalization (Items A + B)
- DEU 3:6, 7:2, 7:26 — ḥerem surface normalization (Item D)
- DEU 11:13 — within-DEU Shema drift fix (Item C)
- DEU 11:30 — ethnonym drift fix (§Z follow-on)
- DEU 18:15, 18:18, 18:19, 18:20, 18:22 — prophet-cluster normalization (Item C)
- DEU 20:17 — seven-nations normalization (Item F)
- DEU 25:4 — muzzle-ox canonical (Item C)
- DEU 31:4 — ethnonym drift fix (§Z follow-on)
- DEU 34:1 — Pisgah typo fix (Item F)

### Cross-Pentateuch (Item A tandem)
- EXO 20:5, 20:6 — Sinai-formula paqad+chesed normalized
- NUM 14:18 — Sinai-formula full-form normalized

### DEU textual_variants (Layer-2 footers)
- DEU 2:34 — new ḥerem first-occurrence footer (introduces เฮเรม + back-points to 20:17)
- DEU 3:6 — new ḥerem back-pointer footer
- DEU 7:2 — new ḥerem back-pointer footer
- DEU 13:16 — new ḥerem back-pointer footer
- DEU 32:43 — amended witness-asymmetry rationale

### Docs created / amended
- `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` — amended (§1.4 added; locked-recitations list expanded; change log v0.2)
- `docs/translator_decisions/decalogue_parallel_text_2026-05.md` — **new**
- `docs/translator_decisions/ot_nt_cross_quotation_thread_2026-05.md` — **new**
- `docs/translator_decisions/ot_warfare_ethics_2026-05.md` — amended (§4.1 Thai-surface lock added)
- `docs/translator_decisions/proper_names_and_transliteration_2026-05.md` — amended (seven-nations cluster + trans-Jordan place-names sections added)

### Pipeline assets
- `data/proper_noun_locks.json` — **new**
- `scripts/check_proper_nouns.py` — **new**

---

## What's staged (not done in this pass)

- **Synoptic Decalogue / Shema / muzzle-ox reaudits** (NT-side): Matt 19:18–19, Mark 10:19, Luke 18:20, Matt 22:37, Mark 12:30, 1 Cor 9:9, 1 Tim 5:18, Rom 13:9, Eph 6:2–3, Jas 2:11. Per `decalogue_parallel_text_2026-05.md` §4 + `ot_nt_cross_quotation_thread_2026-05.md` §2.
- **Matt-4 temptation-quote reaudit**: DEU 6:13 / 6:16 / 8:3 NT-side surfaces (Matt 4:4, 4:7, 4:10) — MEDIUM-severity verb-lemma drift.
- **Cross-corpus seven-nations + Pisgah drift fixes** in EXO/GEN/NUM: 24 rejected-surface violations to be folded into the next per-book end-of-book audits (or batched as a one-off OT-pilot polish pass).
- **`check_phrase_consistency.py` Decalogue + ḥerem + cross-quotation lock extensions** — HARD-FAIL on the locks defined in the new docs.
- **`run_checks.py` wiring** for `check_proper_nouns.py` (currently standalone-invocable).

---

## Tag readiness

All four DECIDE items (A, D, E-footer, F) and the minimum-for-tag scope of MAJOR items B + C are resolved. **`book-deuteronomy-v1` is unblocked** by this audit-response pass.
