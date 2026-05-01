# 1 Corinthians — End-of-Book Review

**Date:** 2026-05-01
**Scope:** All 16 chapters; `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** 1CO 16 shipped (commit `d5a006e` thai-bible-ai); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2) + handwritten External AI items packet (§3 — ready for Gemini/Grok/ChatGPT cross-review). No translation changes prescribed; surface only.

## Summary

- **8 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 16/16 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 violations) across the 149-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status` clean.
- **1 Corinthians is the FOURTH FULL Pauline epistle the project has shipped** (after Galatians, 1 Thess, 2 Thess), and the LARGEST-AND-DENSEST Pauline letter to date at 16 chapters. It introduces several MAJOR FIRST-OCCURRING corpus-cross-cutting clusters:
  - **Glossolalia / spiritual-gifts vocabulary** (chs 12–14): γλῶσσαι, προφητεία, διακρίσεις πνευμάτων, ἑρμηνεία γλωσσῶν, χάρισμα, πνευματικά
  - **Resurrection vocabulary** (ch 15): ἀνάστασις, ἀπαρχή (confirms 2 Th 2:13 lock → ผลแรก), σῶμα ψυχικόν / πνευματικόν, ἐγείρω + σπείρω body-grain metaphor, ψυχή/πνεῦμα contrast at 15:45 (Adam-typology)
  - **Lord's Supper vocabulary** (ch 11): δειπνον κυριακόν, ἄρτος + ποτήριον, ἀνάμνησις, εὐλογία (cup-of-blessing), κοινωνία (participation)
  - **Body-of-Christ ecclesiology** (ch 12): σῶμα Χριστοῦ + μέλη + βάπτισμα ἐν πνεύματι metaphor cluster
  - **Idol-meat / pagan-table polemic** (chs 8–10): εἰδωλόθυτα, εἴδωλον, τράπεζα δαιμονίων / κυρίου
  - **Marriage / celibacy vocabulary** (ch 7): γαμέω, παρθένος, ἁγία, ἄγαμος, χωρίζω + ἀφίημι divorce-vocabulary
- **Inherited locks verified compliant:** ἁγιασμός cluster from 1 Thess (1:30, 6:11); παρουσία (15:23, 16:17 — Christ-subject, royal เสด็จมα retained); σημεῖον = หมายสำคัญ (1:22 — corpus default, miracle-sense); ἀπαρχή = ผลแรก (15:20, 15:23, 16:15 — confirms 2 Th 2:13 lock); ἀπώλεια (1:18 → ความพินาศ); ἀδικία = อธรรม; πορνεία = การล่วงประเวณี (5–6 cluster); μυστήριον = ความล้ำลึก (2:1, 2:7, 4:1, 13:2, 14:2, 15:51).
- **Major textual variant treated:** 11:24 omits κλώμενον "broken" per SBLGNT/NA28 (vs TR/Byz/KJV which include) — followed; no chapter-footer note attached. 14:34–35 retained in-place per SBLGNT/NA28 (vs Western-MSS displacement) — no note attached.
- **External AI cross-review (§3) PENDING.** Items doc + packet ready: paste `docs/end_of_book/1corinthians/external_review_packet_1CO_2026-05-01.md` into Gemini / Grok / ChatGPT / Claude.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — defensible, worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. γλῶσσαι rendering (chs 12–14) — **REVIEW**

Uniform **ภาษา / ภาษาต่างๆ** ("languages") — preserves Greek literal-language sense; theologically-neutral on cessationist/continuationist + xenoglossy/ecstatic debates. Affects Acts 2 retroactively (already locked) and Mark 16:17 (long-ending). See **Item A** in items doc.

## 2. σῶμα ψυχικόν / πνευματικόν at 15:44 + ψυχή/πνεῦμα collapse at 15:45 — **REVIEW**

15:44 σῶμα ψυχικόν → **กายตามธรรมชาติ**; σῶμα πνευματικόν → **กายฝ่ายวิญญาณ**. The 15:45 ψυχή AND πνεῦμα BOTH → **วิญญาณ** — collapses the 1 Thess 5:23 tripartite-anthropology lock locally. **CROSS-CUTTING tension flagged.** See **Item B**.

## 3. Corinthian-slogan quotation marks at 7:1, 8:4, 10:23 — **REVIEW**

Translator marks Corinthian-slogans-Paul-quotes-then-refutes with curly quotes per modern critical consensus. Crosses light-commentary boundary; will recur in 1 Cor 6:12-13 plus 2 Cor and Romans diatribe sections. See **Item C**.

## 4. 1 Cor 11:24 textual variant + ἀνάμνησις — **STABLE**

SBLGNT followed (omits κλώμενον). ἀνάμνησις → **ระลึกถึง**. Mainstream-aligned. See **Item D**.

## 5. Women: 11:5 vs 14:34–35 + textual variant — **DECIDE**

11:5 (women may pray/prophesy) and 14:34-35 (women silent) translated straight, in-place. NO Tier-2 footer note for the Western-MSS displacement at 14:34-35. NO cross-reference notes acknowledging the apparent tension. Whether to add either (or both) is a project-policy call. See **Item E**.

## 6. εἰδωλόθυτα chs 8–10 — **STABLE**

**อาหารที่ถวายแก่รูปเคารพ** for εἰδωλόθυτος; **รูปเคารพ** for εἴδωλον. Thai-cultural resonance lands well. Will recur Rev 2:14, 20; Acts 15:29 + 21:25 retroactively-aligned. See **Item F**.

## 7. πορνεία family — **REVIEW**

**การล่วงประเวณี** for πορνεία; **คนล่วงประเวณี** for πόρνος. Thai-natural but slightly narrower than Greek (which is broader than μοιχεία = adultery-specifically). Cross-corpus consistency check. See **Item G**.

## 8. Marana tha at 16:22 — **STABLE**

Aramaic-embed treatment per RULES §10b: **มาราน-อาธา** transliterated + parenthetical Thai gloss "องค์พระผู้เป็นเจ้าของเราเอ๋ย ขอเสด็จมาเถิด" (royal-เสด็จมα consistent with παρουσία corpus-lock). See **Item H**.

---

## TODO — corpus decision docs (non-blocking; JIT before relevant downstream books)

Carrying forward from 2 Thessalonians audit, plus new from 1 Corinthians:

1. `docs/translator_decisions/parousia_register_2026-04.md` — Christ-เสด็จมา / adversary-มาถึง split. (Carried over.)
2. `docs/translator_decisions/anomia_lawlessness_2026-04.md` — ความอธρρม / คนอธρρม. (Carried over.)
3. `docs/translator_decisions/aparche_firstfruits_2026-04.md` — ผลแรก. **Confirmed by 1 Cor 15:20, 23, 16:15.** (Carried over; ready to write.)
4. `docs/translator_decisions/paradosis_synoptic_pauline_split_2026-04.md` — Synoptic ธρρมเนียม / Pauline คำสอนที่ส่งทอดมα + Col 2:8 caveat. (Carried over.)
5. `docs/translator_decisions/semeion_three_senses_2026-04.md` — miracle / authentication-mark / signal. **Confirmed by 1 Cor 1:22 (miracle sense locked).** (Carried over.)
6. **NEW** `docs/translator_decisions/glossolalia_languages_2026-05.md` — γλῶσσαι → ภาษา / ภาษาต่างๆ uniform rendering. **Trigger book:** any forward use; immediate.
7. **NEW** `docs/translator_decisions/eidolothyta_idol_meat_2026-05.md` — εἰδωλόθυτος → อาหารที่ถวายแก่รูปเคารพ; εἴδωλον → รูปเคารπ. **Trigger book:** Revelation 2.
8. **NEW** `docs/translator_decisions/corinthian_slogan_quotemarks_2026-05.md` — convention for marking Pauline-quotation of opponents/correspondents. **Trigger book:** 2 Corinthians (heavy diatribe); Romans 1-3.
9. **NEW** `docs/translator_decisions/anastasis_resurrection_cluster_2026-05.md` — resurrection vocabulary cluster from 1 Cor 15. **Trigger book:** 1 Thess 4-5 retro-check; Romans 6, 8.

---

## Tagging eligibility

§1 mechanical gates clean. §2 internal review complete. §3 external AI review **PENDING** (packet ready for paste). §4 native-speaker / theological reviewer feedback **PENDING** (no live form questions yet from 1 Cor; Item E's women/14:34 textual-variant question is the strongest candidate for new YAML).

**Tag `book-1corinthians-v1` is gated on §3 + §4** — paste packet into Gemini for §3 cross-check; consider adding 1-2 reviewer-form YAMLs for the most-pastoral-impact items (E + B are top candidates).
