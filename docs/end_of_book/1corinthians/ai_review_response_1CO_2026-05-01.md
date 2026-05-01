# 1 Corinthians — External AI Review Response

**Date:** 2026-05-01
**Reviewers:** ChatGPT (detailed independent review with citations); Gemini (endorsed ChatGPT's review with light reformatting — effectively a sanity-check rather than a fully-independent third opinion)
**Author of this response:** Ben + Claude (in-session)
**Audit doc:** `1CO_END_OF_BOOK_REVIEW_2026-05-01.md`
**Items doc:** `external_review_items_1CO.md`

This doc records the disposition of each of the 8 items (A–H) and §Z. Items rendered with strong AI-reasoning consensus were spot-revised; items needing native-Thai-speaker input were deferred with a stub corpus-doc.

---

## Item A — γλῶσσαι (chs 12–14) → ภาษา / ภาษาต่างๆ

**Verdict:** FINE. Lock as-is.

**Reasoning (ChatGPT, endorsed by Gemini):** γλῶσσα has a real "language/tongue" semantic range. 1 Cor 12:10's pairing of γένη γλωσσῶν with ἑρμηνεία γλωσσῶν supports "languages needing interpretation." "ภาษา" remains broader than ecstatic-utterance-specific options (กลอสซาเลีย / ลิ้น) and works for 13:1's "languages of humans and angels." Locks γλῶσσαι uniformly; no charismatic/cessationist forcing.

**No revision.** Forward implication: same lock applies to Acts 2:4ff (already shipped), Mark 16:17.

---

## Item B — 15:44–45 σῶμα ψυχικόν / πνευματικόν + ψυχή/πνεῦμα

**Verdict (15:44):** FINE. Lock as-is — `กายตามธรรมชาติ / กายฝ่ายวิญญาณ` matches mainstream English-translation tradition.

**Verdict (15:45):** CONCERN — both AIs flag the prior collapse of ψυχή + πνεῦμα to `วิญญาณ` as obscuring the Adam/Christ typology. Mainstream translations preserve "living being / living soul / living person" for ψυχήν ζῶσαν, distinct from "life-giving spirit" for πνεῦμα ζῳοποιοῦν.

**Disposition:** **REVISED.** Spot-revised 1 Cor 15:45:
- ψυχήν ζῶσαν: `วิญญาณที่มีชีวิต` → **`สิ่งมีชีวิต`** (preserves Hebrew nephesh-chayyah / LXX ψυχὴ ζῶσα tradition)
- πνεῦμα ζῳοποιοῦν: `วิญญาณที่ให้ชีวิต` → **`วิญญาณผู้ให้ชีวิต`** (substantival agent — emphasizes Christ as ACTIVE life-giver vs Adam as passive recipient)

This resolves the ψυχή/πνεῦμα collapse flagged in the audit doc Item B (and the YAML B_1CO15_pneumatikon_psychikon at EremosVercel2). The typological-distinction now reads cleanly. Local-divergence from 1 Th 5:23 tripartite-anthropology lock is preserved as a deliberate context-distinguished decision (per RULES §4 multi-sense, here typological-Genesis-2:7-context vs anthropological-context-1Th).

**YAML closure:** B_1CO15_pneumatikon_psychikon.yml in EremosVercel2/shared/review-questions/ is now answered by AI consensus and can be deleted on next reviewer-form maintenance pass.

---

## Item C — Corinthian-slogan curly quotes at 7:1, 8:4, 10:23

**Verdict:** FINE. Lock as-is.

**Reasoning:** NET, ESV, CSB, NIV all use quotation-mark strategies for Pauline-Corinthian-slogan-citation; this is mainstream translation practice, not fringe commentary. The audit's choice aligns with consensus.

**No revision.** Doc action: write a corpus rule "Use curly quotes for Corinthian slogans where modern critical translation consensus identifies a quotation; avoid where consensus is weak" — queued in `docs/translator_decisions/sarcasm_quotation_convention_2026-05.md` (forward, not blocking tag).

---

## Item D — 11:24 textual variant + ἀνάμνησις

**Verdict:** FINE. Lock as-is.

**Reasoning:** SBLGNT-omission of κλώμενον "broken" is the eclectic-text consensus; modern translations follow. Thai `ซึ่งให้ไว้เพื่อพวกท่าน / เพื่อระลึกถึงเรา` is stable and standard.

**No revision.** ChatGPT explicitly says no Tier-2 note needed unless project has TR/KJV-legacy-reading policy.

---

## Item E — 11:5 vs 14:34–35 (women praying/silent + Western-MSS displacement)

**Verdict:** CONCERN — both AIs recommend neutral textual-note + cross-references between 11:5 and 14:34. Explicitly **NO bracketing** (verses present in all manuscripts; this is a DISPLACEMENT problem, not a standard inclusion-omission variant — Tier-2 footer treatment per RULES §5b does not apply).

**Disposition:** **REVISED.** Updates:
- 1 Cor 14:34 `notes` strengthened: explicit "SEE 11:5" cross-reference, manuscript displacement note (Codex Bezae D, F, G, old Latin and Vulgate place after v.40; Alexandrian uncials place here), explicit acknowledgement that displacement ≠ inclusion-omission and does not warrant bracketing.
- 1 Cor 11:5 `thai_summary` added (Thai-language reader-facing note): pointer to 14:34-35 + summary of mainstream interpretation that the two passages address different speech-situations.

No textual-variant JSON file added (per ChatGPT: "do **not** bracket the verses").

**YAML closure:** B_1CO_women_silence_variant.yml at EremosVercel2 was offering 4 options — option (c) "textual + xref" matches the implementation. YAML can be deleted on next reviewer-form maintenance pass.

---

## Item F — εἰδωλόθυτα → อาหารที่ถวายแก่รูปเคารพ

**Verdict:** FINE. Lock as corpus default.

**Reasoning:** Accurate, transparent, Thai-religious-culture-appropriate. รูปเคารพ already locked for εἴδωλον.

**No revision.** Forward: 1 Cor 8–10 (locked), Acts 15:29 + 21:25 (already shipped), Rev 2:14 + 2:20 (forward).

---

## Item G — πορνεία / πόρνος → การล่วงประเวณี / คนล่วงประเวณี

**Verdict:** CONCERN — but ChatGPT explicitly says "Ben to decide after a focused native-speaker check. The decision should not be verse-by-verse. Write a corpus rule for πορνεία vs μοιχεία."

**Disposition:** **DEFERRED to native-speaker review.** No verse revision. Reasoning: the recommendation requires native-Thai semantic judgment about whether `การล่วงประเวณี` reads broadly enough in Thai-Bible register, OR whether πορνεία needs a more general rendering (`การผิดศีลธรรมทางเพศ` / `คนผิดศีลธรรมทางเพศ`) reserving `การล่วงประเวณี` for μοιχεία. This is a corpus-wide call across Mark, Matthew, Acts, Paul, Revelation — too big to make verse-by-verse without native-speaker validation.

**Doc action:** Stub `docs/translator_decisions/porneia_vs_moicheia_DEFERRED_2026-05.md` capturing the question for future review. Adding a B-tier YAML at EremosVercel2 for native-speaker input on next reviewer-form pass.

---

## Item H — Marana tha + Aramaic-embed + parenthetical gloss

**Verdict:** FINE. Lock as standard pattern.

**Reasoning:** Preserves Aramaic-liturgical-formula visibility while glossing for Thai readers. Pattern: Thai-script transliteration + parenthetical Thai gloss for original-text-without-internal-explanation.

**No revision.** Forward: same pattern for Mark 5:41 (already shipped — ทาลิธา คูม), Mark 7:34 (Ephphatha — already shipped), Aramaic prayers in liturgical contexts (forward).

---

## §Z — Anything else?

ChatGPT: "No additional corpus-level concerns beyond B, E, and G." Gemini concurs.

---

## Summary table

| Item | Verdict | Action | Status |
|---|---|---|---|
| A γλῶσσαι | FINE | Lock as-is | ✅ no revision |
| B 15:44 σῶμα ψυχικόν | FINE | Lock as-is | ✅ no revision |
| B 15:45 ψυχή/πνεῦμα | CONCERN | **Revised** (สิ่งมีชีวิต / วิญญาณผู้ให้ชีวิต) | ✅ done |
| C Corinthian-slogan quotes | FINE | Lock; doc queued | ✅ no revision |
| D 11:24 variant | FINE | Lock as-is | ✅ no revision |
| E 14:34-35 textual + xref | CONCERN | **Strengthened cross-references + textual note** | ✅ done |
| F εἰδωλόθυτα | FINE | Lock as corpus default | ✅ no revision |
| G πορνεία vs μοιχεία | CONCERN | **Deferred to native-speaker** + stub doc | 🟡 pending |
| H Marana tha | FINE | Lock as pattern | ✅ no revision |

---

## Tagging eligibility

- §1 mechanical gates: ✅ clean (verified 2026-05-01)
- §2 audit doc: ✅ done (2026-05-01)
- §3 external AI review: ✅ done (this doc; ChatGPT independent + Gemini endorsement)
- §4 reviewer hand-off: 🟡 ongoing (B + G items now have native-speaker YAMLs queued for EremosVercel2). NOT blocking tag.
- §5 lock the book: ready after this revision lands.

**Tag `book-1corinthians-v1` is GO.** Item G is the only deferred-CONCERN, and it's explicitly flagged for native-speaker review (cannot be resolved by AI alone), with a stub doc capturing the question.
