# Matthew — End-of-Book Review

**Date:** 2026-04-19
**Scope:** All 28 chapters (1,069 verses); `glossary.json`; `RULES.md`; `docs/translator_decisions/`.

## Summary

- **16 cross-cutting items reviewed.**
- **6 flagged** for Ben's attention: ἐκκλησία, μεταμέλομαι vs. μετανοέω, amen-formula drift, Σὺ λέγεις micro-drift, inclusion-variant treatment of 17:21/18:11, and `thai_summary` coverage variance.
- **10 items stable/locked** — no corpus-level change needed.
- **3 new decision docs recommended** (see final section).

Status codes below: **LOCKED** (stable + corpus-doc or unambiguous), **STABLE/UNDOCUMENTED** (no drift, no corpus-doc), **DRIFT** (varies without rationale), **REVIEW** (documented but Ben should confirm).

---

## 1. ἐκκλησία → คริสตจักร — **REVIEW / HIGH-PRIORITY LOCK**

Two occurrences: `output/translations/matthew_16.json:321` (16:18) and `matthew_18.json:294` (18:17). Both render **คริสตจักร**, not the more neutral **ที่ประชุม**. Per-verse rationale present; no corpus-level doc. This is the trigger case for the End-of-Book Checklist itself (`docs/END_OF_BOOK_CHECKLIST.md:48`).

**Precedent weight:** massive — Acts 23×, Pauline 60×, Hebrews/James/Peter/Revelation. Determines ἐκκλησία θεοῦ (1 Cor 1:2), αἱ ἐκκλησίαι τῶν ἐθνῶν (Rom 16:4), Rev 2–3 letters.

**Counter-argument** (Grok): คริสตจักร carries post-Pentecost institutional connotations; Jesus at 16:18/18:17 speaks proleptically; ที่ประชุม/ชุมนุม better preserves pre-institutional semantic range.

**Recommendation:** LOCK to คริสตจักร, but write `docs/translator_decisions/ekklesia_2026-04.md` explicitly so Acts + epistles translators don't re-litigate.

---

## 2. βασιλεία τῶν οὐρανῶν vs. τοῦ θεοῦ — **LOCKED**

53 occurrences. Stable split:
- **τῶν οὐρανῶν → อาณาจักรสวรรค์** (51×) — Matthean signature reverential periphrasis.
- **τοῦ θεοῦ → อาณาจักรของพระเจ้า** (2×: 12:28, 21:43).

The Greek variation is faithfully preserved rather than flattened. Matches RULES.md §4.

**Recommendation:** STABLE. No doc needed unless Ben wants an explicit one-line lock.

---

## 3. μετανοέω vs. μεταμέλομαι — **DRIFT / HIGH-PRIORITY**

Biggest editorial-coherence issue in Matthew.

| Verse | Greek | Thai | Distinct from μετανοέω? |
|-------|-------|------|-------------------------|
| 3:2, 4:17, 11:20–21, 12:41 (×5) | μετανοέω | กลับใจ(ใหม่) | (canonical) |
| 21:29 (son changes mind) | μεταμέλομαι | **กลับใจ** | NO |
| 21:32 (priests/elders) | μεταμέλομαι | **ไม่กลับใจ** | NO |
| 27:3 (Judas) | μεταμέλομαι | **เสียใจ** | YES |

The 21:29 rationale admits: "μεταμέλομαι narrower 'remorse/reconsidering' **but Thai does not distinguish readily**." Yet 27:3 makes the deliberate distinction: "CRUCIAL: this is NOT μετανοέω … preserves the Matthean theological distinction."

**Both cannot be right** — 21:29 and 27:3 use the same Greek verb.

**Precedent weight:** 2 Cor 7:10 (godly grief → μετάνοιαν vs. worldly grief → death) is the locus classicus. Hebrews 7:21, 12:17 also. If Matthew's corpus is inconsistent, those anchors drift.

**Recommendation:** **REVISE**. Preferred: change 21:29 and 21:32 to **เปลี่ยนใจ** (change-of-mind, non-salvific) to match 27:3's distinction. Write `docs/translator_decisions/metanoeo_vs_metamelomai_2026-04.md`.

---

## 4. ἀμὴν λέγω ὑμῖν formula — **MINOR DRIFT**

20 occurrences; 17 match the Markan lock "เราบอกความจริงแก่พวกท่าน" (per `amen_saying_formula_2026-04.md`). Anomalies:

- **5:18, 13:17**: "เราบอกพวกท่านตามจริง" (word order inverted, adverbial).
- **5:26**: "เราบอกท่านตามจริง" (σοι singular — the ตามจริง adverbial carries over).

**Recommendation:** **REVISE** these 3 verses to the locked form before `book-matthew-v1`. 3-line edit. Or update Mark's decision doc to permit the ตามจริง variant — but inconsistent with the rationale there.

---

## 5. Σὺ λέγεις / Σὺ εἶπας idiom — **STABLE (micro-variation)**

3 occurrences:
- **26:25** (Judas), **26:64** (Caiaphas): Σὺ εἶπας (aor) → "ท่านได้พูดเองแล้ว"
- **27:11** (Pilate): Σὺ λέγεις (pres) → "ท่านพูดเองแล้ว" (no ได้)

Greek tense difference justifies the Thai aspect-particle difference. The 27:11 rationale overstates by claiming "consistent rendering across all three"; in fact the form tracks Greek tense.

**Recommendation:** LEAVE AS-IS. No doc needed beyond existing verse notes.

---

## 6. γέεννα → นรก — **LOCKED**

7 occurrences (5:22, 5:29, 5:30, 10:28, 18:9, 23:15, 23:33). All **นรก** / **ไฟนรก** / **บุตรแห่งนรก**. No transliteration (เกเฮนนา) used. Matches Mark glossary. Locks for James 3:6.

---

## 7. παρουσία → การเสด็จมา — **LOCKED**

4 Matthean occurrences (24:3, 24:27, 24:37, 24:39), all **การเสด็จมา** (royal-register เสด็จ, since Son of Man is subject).

**Precedent weight:** huge for 1–2 Thess + 2 Peter. But: Paul also uses παρουσία for human visitors (1 Cor 16:17, 2 Cor 7:6–7, Phil 1:26) — การเสด็จมา would over-honorific Stephanas/Titus.

**Recommendation:** LOCK for Christological use. Write `docs/translator_decisions/parousia_2026-04.md` and flag the human-παρουσία ambiguity for the Paulines translator.

---

## 8. εὐνοῦχος (Matt 19:12) — **LOCKED**

Single occurrence (used 3× in the verse). **ขันที** — standard Thai Christian. Locks for Acts 8:27–39 (Ethiopian eunuch).

---

## 9. Pilate honorifics — **LOCKED**

12 Matt 27 verses. Narrator uses plain verbs (กล่าว, ถาม, ปล่อย, มอบ, สั่ง). Third-person เขา. Pilate→Jesus: ท่าน (27:13, 27:17). Pilate's self-reference: ข้าพเจ้า/เรา. Matches `docs/translator_decisions/honorifics_non_divine_authorities_2026-04.md` verbatim.

---

## 10. Herod honorifics — **LOCKED**

- **Herod the Great (Matt 2):** ทรง in narrator-voice at 2:3, 2:12, 2:22 (public-king role); plain at 2:7, 2:16, 2:19 (deceptions and massacre — register-downshift echoing Mark 6:16's guilty-king-speech).
- **Herod Antipas (Matt 14):** plain throughout. Daughter's court-speech 14:8 uses หม่อมฉัน/ประทาน per Mark 6:22–25 lock.

**Recommendation:** STABLE. Optionally append a "Matthew 2" evidence stanza to the existing honorifics doc.

---

## 11. Caiaphas / High Priest — **LOCKED**

Matt 26:57–68: plain verbs, เขา third-person, ท่าน to Jesus (26:62). Rationale at 26:62 explicitly cites Mark 14:60 lock.

---

## 12. Narrator-vs-character voice for Jesus — **LOCKED**

Narrator: always royal (ทรง, ตรัส, เสด็จ, พระองค์). Disciples: ข้าพระองค์/พระองค์. Crowds speculating, mockers, Pilate: เขา/ท่าน. Judas: **รับบี** at 26:25, 26:49 — the Markan "inadequate-confession" register. Matches `narrator_vs_character_voice_2026-04.md`.

---

## 13. Aramaic transliteration — **LOCKED**

Matthean extensions of the Markan "transliterate + gloss" pattern:
- **1:23 Ἐμμανουήλ → อิมมานูเอล** + gloss
- **5:22 Ῥακά → ‹ราคา›** (HAPAX, single-guillemet marks foreign)
- **6:24 μαμωνᾷ → เงินทอง** (not transliterated — rendered semantically)
- **27:33 Γολγοθᾶ → กลโกธา** + gloss
- **27:46 Ἠλὶ ἠλὶ λεμὰ σαβαχθάνι → เอλี เอλี เลมา ซาบัคทานี** + gloss

The existing `aramaic_transliterations_2026-04.md` specifically anticipated Matt 5:22 and 27:46; the calls made match the prediction.

**Recommendation:** STABLE. Optionally append a "Matthew confirms" stanza.

---

## 14. Inclusion-variant bracketing — **PARTIAL INCONSISTENCY / REVIEW**

RULES.md §5: single-brackets `[...]` for inclusion variants where mainstream traditions include but SBLGNT omits.

Bracketed (correctly): 5:22 [โดยไม่มีเหตุ], 5:44 [longer love-enemies], 6:13 [doxology], 6:15, 6:33, 15:6, 23:14 (whole verse), 25:14.

**Inconsistent cases:**

| Verse | Treatment | Issue |
|-------|-----------|-------|
| 17:21 (fasting) | **verse absent** (no JSON key) | No reader-visible marker |
| 18:11 (Son of Man came to save) | **verse absent** | Same |
| 23:14 (woe — widows' houses) | bracketed as whole verse | Reader-visible |
| 16:2b–3 (red sky) | included unmarked | Note says "omitted in earliest witnesses" |
| 21:44 (stone grinds) | included unmarked | Note flags SBLGNT inclusion, D/OL omit |

The 17:21/18:11 silent-skip vs. 23:14 bracketed-include is the core inconsistency. Per RULES.md §5 rationale ("silent omission reads as editorial overreach"), 17:21/18:11 should either appear as bracketed-included verses (consistent with 23:14) OR 23:14 should also be silently skipped.

**Precedent weight:** sets template for Mark 16:9–20 (already done), Acts 8:37, Acts 15:34, Rom 16:24, 1 John 5:7–8 (Johannine Comma).

**Recommendation:** **REVIEW**. Preferred: add 17:21 and 18:11 as bracketed-included verses; reconsider whether 16:2b–3 and 21:44 warrant brackets (both have recognized-but-not-fatal inclusion-doubt). Write `docs/translator_decisions/inclusion_variants_absent_verses_2026-04.md`.

---

## 15. τότε discourse marker — **STABLE**

89 occurrences, rendered in 5 forms (context-sensitive per Markan-εὐθύς precedent):
- แล้ว (39), ครั้งนั้น (15), เมื่อนั้น (11), ในเวลานั้น (10), ขณะนั้น (3), **NONE (11)**.

The 11 silent-drops deserve a spot-check (Matt 9:15, 9:37, 12:45, 13:26, etc.) — Markan εὐθύς was always rendered; Matthean τότε occasionally isn't. If any of the 11 structurally needs τότε for discourse clarity, add it.

**Recommendation:** STABLE. Optionally append a "Matthean τότε" stanza to `markan_euthys_immediately_2026-04.md`.

---

## 16. `thai_summary` coverage — **VARIABLE (product decision)**

Coverage bimodal by chapter:
- **100%**: 4, 5, 6, 10, 11, 13, 17, 18
- **50–80%**: 1, 2, 7, 12, 14–16, 23, 24, 27
- **30–50%**: 8, 20, 21, 22, 25, 26

Passion narrative (26, 27) and parable chapters (25) have lowest coverage — defensible per RULES.md §6 ("Skip simple narrative without interpretive payload"). Product-layer decision, not translation-correctness.

**Recommendation:** No action unless Ben wants to upscale passion chapters for Eremos app.

---

## Proper nouns & Son of Man (spot-checked) — **LOCKED**

All sampled proper nouns have exactly one Thai rendering (Ἰωάννης→ยอห์น, Δαυίδ→ดาวิด, Ἡρῴδης→เฮโรด, Πιλᾶτος→ปีลาต, Ἰούδας→ยูดาส, Μωϋσῆς→โมเสส, Ἀβραάμ→อับราฮัม, Ἠλίας→เอลียาห์, Βηθλέεμ→เบธเลเฮม, Ναζαρέτ→นาซาเร็ธ, Ζαβουλών→เศบูลุน, Νεφθαλίμ→นัฟทาลี, Γολγοθᾶ→กลโกธา, Βαραββᾶς→บารับบัส). Son of Man: all Matthean title occurrences use **บุตรมนุษย์** (no ของ) per `son_of_man_disambiguation_2026-04.md`.

---

## New decision documents recommended

Ranked by precedent weight:

1. **`docs/translator_decisions/ekklesia_2026-04.md`** — lock คริสตจักร vs. ที่ประชุม/ชุมนุม before Acts + epistles.
2. **`docs/translator_decisions/metanoeo_vs_metamelomai_2026-04.md`** — resolve 21:29/21:32 vs. 27:3 drift before 2 Cor 7:10.
3. **`docs/translator_decisions/inclusion_variants_absent_verses_2026-04.md`** — policy on whole-verse omissions (17:21/18:11 silent-skip vs. 23:14 bracket) before Acts 8:37 / Rom 16:24 / Johannine Comma.

Optional:
4. **`parousia_2026-04.md`** — lock การเสด็จมา for Christological use; flag human-παρουσία ambiguity for Paulines.
5. Appendix stanzas on existing docs (aramaic_transliterations / honorifics_non_divine_authorities / markan_euthys_immediately).

---

## Pre-tag action items (before `git tag book-matthew-v1`)

Must-do:
- [ ] Resolve μετανοέω / μεταμέλομαι; revise 21:29, 21:32 (or 27:3).
- [ ] Decide inclusion-variant policy for 17:21, 18:11 (and 16:2b–3, 21:44 consistency).
- [ ] Write `ekklesia_2026-04.md`.

Nice-to-have:
- [ ] Normalize amen-formula at 5:18, 5:26, 13:17 (3 edits).
- [ ] Spot-check 11 τότε NONE cases.
- [ ] Write `metanoeo_vs_metamelomai_2026-04.md`, `inclusion_variants_absent_verses_2026-04.md`.
