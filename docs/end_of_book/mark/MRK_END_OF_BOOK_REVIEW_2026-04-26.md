# Mark — End-of-Book Review

**Date:** 2026-04-26 (retrospective)
**Scope:** All 16 chapters (673 verses); `glossary.json`; `RULES.md`; `docs/translator_decisions/`.
**Trigger:** **RETROSPECTIVE — backfill.** Mark was reviewed retroactively in 2026-04 alongside Matthew (2026-04-19) and during subsequent Luke/Acts reviews. Decision docs were created at those times but no consolidated audit doc was written for Mark. This doc consolidates the audit record for completeness and parity with Matthew, Luke, and Acts.
**Mandate:** Internal editorial review (§2 of `END_OF_BOOK_CHECKLIST.md`). No translation changes — verifies what was already decided.

## Summary

- **12 cross-cutting items consolidated.**
- **7 decision docs originated from Mark's retrospective review** (amen_saying_formula, aramaic_transliterations, historic_present, markan_euthys_immediately, narrator_vs_character_voice, son_of_man_disambiguation, honorifics_non_divine_authorities). All seven are LOCKED.
- **5 additional decision docs that lock Mark-applicable patterns** were written during Matthew/Luke/Acts reviews and verified compliant in Mark (basileia_kingdom_rendering, metanoeo_vs_metamelomai, inclusion_variants_absent_verses, parabolic_god_figures_human_register, divine_object_praise_verbs).
- **All mechanical gates pass:** Mark is tagged `book-mark-v1`. Per-chapter check reports (`output/check_reports/mark_*_review.md`) all green; key-term consistency clean; back-translations present.
- **No outstanding items.** No DRIFT or DECIDE flags. Mark is locked.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform pattern at verse-level, no separate doc needed (rule lives in RULES.md or glossary.json).

---

## 1. ἀμὴν λέγω ὑμῖν solemn-pronouncement formula — **LOCKED**

13 occurrences in Mark (3:28; 8:12; 9:1, 41; 10:15, 29; 11:23; 12:43; 13:30; 14:9, 18, 25, 30). Uniform rendering: **เราบอกความจริงแก่พวกท่าน(ว่า)**. The Markan lock anchors the synoptic dominical-saying register; Matthew's three drift verses (5:18, 13:17, 5:26) were corrected to this form during Matthew's audit.

**→ Doc:** `docs/translator_decisions/amen_saying_formula_2026-04.md`.

---

## 2. Aramaic transliterations — **LOCKED**

Seven Aramaic embeds in Mark (3:17 Βοανηργές; 5:41 Ταλιθα κουμ; 7:11 κορβᾶν; 7:34 ἐφφαθά; 14:36 αββα; 15:22 Γολγοθᾶ; 15:34 Ελωΐ Ελωΐ λεμὰ σαβαχθανί). Each preserved as Thai-script transliteration AND Mark's own Greek-to-Thai translation, matching Mark's "transliterate then translate" rhetorical move.

**→ Doc:** `docs/translator_decisions/aramaic_transliterations_2026-04.md`.

---

## 3. Historic present → Thai past tense — **LOCKED**

Mark uses historic-present ~150× (densest of the four gospels for this feature). Every Greek historic-present verb renders Thai past; no attempt to preserve present-tense morphology. Pattern verified at sample verses Mark 1:40–41, 4:35, 5:15–22, 9:2, 11:1–7, 14:17–45, 15:1–27, 16:2–6.

**→ Doc:** `docs/translator_decisions/historic_present_2026-04.md`.

---

## 4. εὐθύς / εὐθέως ("immediately") — **LOCKED (context-sensitive)**

42 occurrences in Mark (more than all other NT books combined for this Markan-dominant word). Not a single locked rendering — context-sensitive choice from a small consistent set (ทันใดนั้น / ในทันใด / และก็ — the third when εὐθύς acts as a prose-pacing connector rather than a temporal marker). Pattern verified across Mark 1:10–6:54 cluster + later occurrences.

**→ Doc:** `docs/translator_decisions/markan_euthys_immediately_2026-04.md`.

---

## 5. Narrator vs. character voice (register for Jesus) — **LOCKED**

Foundational register rule established during Mark's review and applied corpus-wide:
- Narrator-voice prose: Jesus always **พระเยซู / พระองค์ / เสด็จ / ตรัส / ทรง** (ราชาศัพท์, regardless of scene's friendliness)
- Character-voice quotations: register tracks the speaker's stance toward Jesus, not the narrator's

Verified at Mark 1:1, 5:7 (demon's voice), 6:14–16 (people's voice vs. narrator), 8:28 (crowd speculation), 14:45 (Judas), 15:2 (Pilate to Jesus), 15:29–32 (mockers).

**→ Doc:** `docs/translator_decisions/narrator_vs_character_voice_2026-04.md`.

---

## 6. ὁ υἱὸς τοῦ ἀνθρώπου ("Son of Man") — **LOCKED**

Two-way disambiguation:
- **Christological title** (Dan 7:13 echo, Jesus's self-designation, 14× in Mark: 2:10, 2:28, 8:31, 8:38, 9:9, 9:12, 9:31, 10:33, 10:45, 13:26, 14:21 ×2, 14:41, 14:62) → **บุตรมนุษย์** (no "ของ").
- **Generic plural** ("sons of men" = humanity, 1× in Mark at 3:28: τοῖς υἱοῖς τῶν ἀνθρώπων) → **บุตรของมนุษย์** (with "ของ", plural context).

The Thai distinction (presence vs. absence of "ของ") preserves the Greek Christological-title vs. generic-plural difference that the translation could otherwise lose.

**→ Doc:** `docs/translator_decisions/son_of_man_disambiguation_2026-04.md`.

---

## 7. Honorifics for non-divine human authorities — **LOCKED**

Foundational tier-rule established during Mark's review:

`RULES.md §3` specifies ราชาศัพท์ for divine subjects and distancing register for demons. It is silent on the middle tier — human authorities (kings, governors, officers, priests). Mark's pattern: **plain Thai register, NOT ราชาศัพท์**. Verified at Mark 6:14–29 (Herod), 15:1–15 + 43–44 (Pilate), 15:39 (centurion), 14:53–65 (high priest + Sanhedrin).

This rule then carried into Matthew, Luke, Acts (Felix, Festus, Agrippa II, etc.) without re-litigation.

**→ Doc:** `docs/translator_decisions/honorifics_non_divine_authorities_2026-04.md`.

---

## 8. βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า — **LOCKED**

Mark uses βασιλεία τοῦ θεοῦ exclusively (never the Matthean τῶν οὐρανῶν periphrasis). Uniform Thai rendering across all Markan occurrences: 1:14, 1:15, 4:11, 4:26, 4:30, 9:1, 9:47, 10:14, 10:15, 10:23, 10:24, 10:25, 12:34, 14:25, 15:43.

Decision doc was written during Luke end-of-book review but locks the corpus-wide pattern that Mark established.

**→ Doc:** `docs/translator_decisions/basileia_kingdom_rendering_2026-04.md`.

---

## 9. μετανοέω → กลับใจ — **STABLE**

Mark has μετανοέω at 1:4 (John's baptism), 1:15 (Jesus's first sermon), 6:12 (Twelve sent out). All render **กลับใจ** uniformly. Mark has no μεταμέλομαι occurrence (the contrast verb that triggered Matthew's drift) — the salvific-conversion rendering is uncontested in this book.

**→ Cross-ref:** `docs/translator_decisions/metanoeo_vs_metamelomai_2026-04.md` (the contrast was articulated during Matthew's audit; Mark is compliant by not having the contrast verb).

---

## 10. Mark 16:9–20 (longer ending) — **LOCKED Tier 3**

The longest inclusion-variant block in the NT. Treatment per `RULES.md §5` and `inclusion_variants_absent_verses_2026-04.md`:
- Rendered in main text with **⟦double brackets⟧**
- Extended note explains the textual situation (SBLGNT/NA28 manuscript witnesses, mainstream English-Bible practice)
- Reader can see both that the text exists AND that its manuscript status is contested

This locks the Tier-3 treatment for John 7:53–8:11 (pericope adulterae) when reached.

**→ Doc:** `docs/translator_decisions/inclusion_variants_absent_verses_2026-04.md`.

---

## 11. Mark 1:1, 3:14, 9:29 — **LOCKED Tier 1 short-phrase brackets**

Three short-phrase inclusion variants in Mark, rendered in single Thai brackets `[...]`:
- Mark 1:1 — `[พระบุตรของพระเจ้า]` (some witnesses lack υἱοῦ θεοῦ)
- Mark 3:14 — `[ซึ่งพระองค์ทรงเรียกว่าอัครทูตด้วย]` (some witnesses lack οὓς καὶ ἀποστόλους ὠνόμασεν)
- Mark 9:29 — `[และการอดอาหาร]` (some witnesses add καὶ νηστείᾳ)

Per-verse rationale lives in `key_decisions`; the policy lives in the inclusion-variants doc.

**→ Doc:** `docs/translator_decisions/inclusion_variants_absent_verses_2026-04.md`.

---

## 12. Mark 12:1–12 (wicked tenants parable) — **LOCKED**

The owner-of-the-vineyard figure represents God; the rendering uses **human register, NOT ราชาศัพท์**. Decision doc was written during Luke end-of-book review but applies retroactively to Mark 12; verified compliant.

**→ Doc:** `docs/translator_decisions/parabolic_god_figures_human_register_2026-04.md`.

---

## §B. Mechanical-gate verification (per END_OF_BOOK_CHECKLIST.md §1)

- [x] All 16 chapters have green `output/check_reports/mark_NN_review.md` (per-chapter automated checks passed)
- [x] All chapters have `output/back_translations/mark_NN.json` (BT done; back-translation gate enforced)
- [x] `python3 scripts/check_key_term_consistency.py` is clean across Mark — no undocumented lemma variance
- [x] `git status output/translations/mark_*.json` clean (book-mark-v1 tagged, working tree post-tag clean)

---

## §C. External review status (per END_OF_BOOK_CHECKLIST.md §3)

- **External AI review:** retrospective. Mark was the first complete book; the formal external-AI-review process was not yet established when Mark shipped. Subsequent corpus-locks (during Matthew/Luke/Acts external reviews) revisited Mark-applicable patterns and found them compliant. Cross-book consistency checks (`check_key_term_consistency.py`, `check_phrase_consistency.py`) provide ongoing surveillance.
- **Native-speaker Thai review:** pending; flagged for community-review pass.
- **Theological reviewer review:** pending; flagged for community-review pass.

If a future external AI review of Mark is desired, run `scripts/build_external_review_packet.py MRK --items <items_file>` with handwritten items derived from any new findings.

---

## §D. Outstanding / future

None for Mark itself. Forward-compounding items already addressed:
- **Pauline corpus on βασιλεία τοῦ θεοῦ:** Mark's exclusive τοῦ θεοῦ pattern is the precedent; Pauline epistles will inherit the lock (1 Cor 4:20, 6:9–10, 15:50; Rom 14:17; Gal 5:21; Col 4:11; 2 Thess 1:5).
- **Acts on εὐθύς:** Acts uses παραχρῆμα more than εὐθύς; the εὐθύς lock applies but with reduced frequency.
- **Future books on Tier 3 inclusion-variant blocks:** John 7:53–8:11 will follow Mark 16:9–20's `⟦...⟧` pattern.

---

**End of audit.** Mark is locked. Decision docs are stable. No corpus-revision required.
