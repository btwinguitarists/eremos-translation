# Ruth — External AI Review Response

**Date:** 2026-05-05
**Reviewers:** ChatGPT (independent review); Gemini 2.5 Pro (independent review)
**Audit doc:** `RUT_END_OF_BOOK_REVIEW_2026-05-05.md`
**Packet sent:** `external_review_packet_RUT_2026-05-05.md`

This doc records both reviewers' verdicts on the 9 items surfaced by the §2 audit, plus their cross-cutting flags. Where they converged, disposition is straightforward. Where they disagreed, the question is escalated to Ben.

---

## Item A — RUT 1:13 ทรง- on body-part rule (`yad-YHWH` anthropomorphism)

**ChatGPT:** FINE. Lock as-is. Write `divine_anthropomorphism_thai_grammar_2026-05.md` before Exod / Pss / Isaiah where the construction multiplies.

**Gemini:** FINE. The distinction between YHWH-as-direct-subject (takes ทรง-) and divine-body-part-as-subject (plain verb) is precise and linguistically accurate.

**Disposition:** **LOCK + write corpus doc.** Both AIs converge. Recommend Ben write `docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md` before next OT book ships.

---

## Item B — RUT 3:9 כָּנָף wordplay flatness (wing/cloak echo across 2:12 → 3:9)

**ChatGPT:** FINE. "Forcing it into Thai likely damages the receptor text more than it helps." Keep ปีก at 2:12, ชายผ้าคลุม at 3:9; preserve the echo in `thai_summary` only.

**Gemini:** FINE. "Forcing a morphological echo in Thai by using unnatural phrasing would severely disrupt the reading experience and compromise the optimal equivalence philosophy."

**Disposition:** **LOCK as-is** (option (a) — surface preservation with `thai_summary` unpacking). Both AIs strongly converge against options (b) and (c). No code change.

---

## Item C — RUT 4:19 רָם / MAT 1:3-4 อารัม cross-corpus name-form normalization

**ChatGPT:** CONCERN. Recommends path **(b)** — normalize Ruth 4:19 to อารัม. *"Reader recognition of the same canonical person wins when the person appears in both Testaments, unless the Hebrew and Greek forms represent genuinely distinct names or traditions."*

**Gemini:** CONCERN. Recommends path **(c)** — tolerate divergence with explicit policy doc. *"Retaining source-fidelity (ราม for Hebrew, อารัม for Greek) is technically accurate, but leaving it undocumented at the corpus level creates the appearance of error rather than deliberate methodology."* Draft `shared_names_normalization_2026-05.md`.

**The two AIs disagree.** ChatGPT prioritizes reader recognition (one Thai form across testaments). Gemini prioritizes source-fidelity preserved transparently (two forms, with policy doc).

**Disposition:** **DECIDE — Ben to choose (b) or (c).** Recurring question — affects Solomon, Jezebel, Elijah, Noah, etc. across Phase 6D. Escalated below.

---

## Item D — RUT 1:6 פָקַד pastoral-care register — **RESOLVED 2026-05-05 (Tier-A Thai reviewer)**

**ChatGPT:** CONCERN. Keep `ทรงเยี่ยมเยียน` for 1:6 (preserves visitation idiom + NT echo at Lk 1:68). Write 4-sense `paqad` corpus doc before 1 Sam 2.

**Gemini:** CONCERN. **Spot-revise** to `ทรงเหลียวแล` — captures covenantal-care without the spatial "physical visiting" baggage. Then write the 4-sense doc.

**The two AIs disagree on the verse-level rendering** (keep-vs-revise) but agree on the need for a corpus-level paqad sense-table.

**Tier-A native-Thai reviewer (2026-05-05):** "ทรงเหลียวแล is better." Confirms Gemini's call. Question framed as: *"There has been a long famine, and God is finally showing care for His people by bringing them food. Which of these two words sounds more natural for this specific situation — ทรงเยี่ยมเยียน or ทรงเหลียวแล?"* → Tier-A picked **ทรงเหลียวแล**.

**Disposition:** **APPLIED.** Ruth 1:6 spot-revise lands as `ทรงเหลียวแล`. Lk 1:68 (NT) ships unchanged as `เสด็จมาเยี่ยมเยียน` — different register (incarnational-arrival blessing, heavier royal-procession imagery), intentionally not cross-corpus-normalized. The forthcoming `paqad_visit_attend_2026-05.md` corpus doc will lock the four-sense table (pastoral-care → ทรงเหลียวแล; numbering / appointment / judgment-visitation rendered separately).

---

## Item E — RUT 1:9 מְנוּחָה / RUT 3:1 מָנוֹחַ contextual rendering split

**ChatGPT:** FINE, with caution. Lock the verse-level renderings (`ความสงบมั่นคง` at 1:9, `ที่พักพิง` at 3:1). State the rule as "context, not grammatical gender" so future books don't inherit a feminine/masculine hard rule.

**Gemini:** FINE. Same caveat — lock the contextual renderings, but document the principle as contextual rather than morphological so it scales correctly.

**Disposition:** **LOCK as-is** + when the chesed/manoach corpus doc is written, frame the principle as contextual not gendered. No code change.

---

## Item F — RUT 1:19 הוּם → แตกตื่น vs ฮือฮา

**ChatGPT:** CONCERN. `แตกตื่น` may "over-read alarm or panic into the village's reaction." Suggests: `ทั้งเมืองก็เกิดความฮือฮาเพราะพวกนาง` (or `ทั้งเมืองก็วุ่นวายฮือฮา`). Final call: native Thai review.

**Gemini:** CONCERN. **Spot-revise** to `ต่างพากันฮือฮา`. *"แตกตื่น leans too heavily toward physical panic, alarm, or a stampede. ฮือฮา captures public buzz."*

**The two AIs converge on the direction (ฮือฮา is closer than แตกตื่น) but propose slightly different phrasings.** Both want a revision.

**Disposition:** **DECIDE — Ben to pick a final phrase.** Two candidates:
  - `ทั้งเมืองก็ฮือฮาเพราะพวกนาง` (minimal change — drop "แตกตื่น" → "ฮือฮา")
  - `ทั้งเมืองก็เกิดความฮือฮาเพราะพวกนาง` (ChatGPT's compound)
  - `ต่างพากันฮือฮา` (Gemini's collective form, would require slight restructure)

Escalated below.

---

## Item G — RUT 4 levirate-redemption legal-vocabulary cluster

**ChatGPT:** FINE. Write `goel_kinsman_redeemer_2026-05.md` now. **Critical:** explicitly distinguish three usage tiers:
  1. Ruth/Lev 25 legal kinship → `ญาติผู้ไถ่`
  2. YHWH-as-Redeemer / theological → `พระผู้ไถ่` / `องค์พระผู้ไถ่` (no kinship prefix)
  3. NT redemption (Christological) → don't force `ญาติผู้ไถ่` unless kinship/legal-family imagery is explicitly active

**Gemini:** FINE. Same recommendation. *"The shift to the broader theological ผู้ไถ่ (Redeemer) for YHWH/Christ in later books will naturally drop the ญาติ (kinsman) prefix while maintaining the core ไถ่ root."*

**Disposition:** **LOCK + write corpus doc with explicit usage-tier distinction.** Both AIs strongly converge. Recommend Ben write `docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` before Phase 6C (Lev 25) ships.

---

## Item H — RUT 1:6 + 4:13 divine-action attribution language

**ChatGPT:** FINE. The Thai correctly preserves narrator restraint (direct divine action only at 1:6 + 4:13). Variation between `ทรงเยี่ยมเยียน` and `ทรงประทาน` reflects two different Hebrew verbs and two different divine acts — do not flatten.

**Gemini:** FINE. The structural variation is a faithful reflection of the Hebrew narrative strategy. The formal `ทรงประทานให้นางตั้งครรภ์` register fits explicit divine agency.

**Disposition:** **LOCK as-is.** Both AIs converge. No code change.

---

## Item I — Pronoun escalation: RUT 1:16-17 covenant oath vs RUT 3:9 marriage proposal

**ChatGPT:** FINE. `ข้าพเจ้า` for oath/prayer/covenant-formal; `ดิฉัน` where female humble-petitioner speech (אֲמָה / handmaid framing) is socially foregrounded. Do not escalate 3:9.

**Gemini:** FINE. *"A masterclass in utilizing Thai sociolinguistics to convey biblical posture."* Locks the social-posture distinction — formal-oath vs humble-petition — explicitly.

**Disposition:** **LOCK as-is.** Both AIs strongly converge. No code change.

---

## §Z — Cross-cutting metadata flags (ChatGPT only)

**§Z.1 Packet metadata bug.** ChatGPT noted the `external_review_packet_RUT_2026-05-05.md` header reads *"translated directly from SBLGNT (Greek)"* — wrong for an OT book. The hardcoded SBLGNT-Greek prompt-header in `scripts/build_external_review_packet.py` (lines 187, 191, 192, 193, 201) does not branch on testament. **Real bug; fix.**

**§Z.2 Hezron variance.** ChatGPT flagged `เฮศรอน / เฮสโรน` as a possible variance to bundle with the Ram/Aram pass. **Unfounded** — `grep -r "เฮศ"` returns zero matches; both Mt 1:3 and Ruth 4:18 already use `เฮสโรน` (Hebrew nun-final form). The audit doc's "final ม vs น" note refers to the Greek-form Ἑσρώμ vs Hebrew-form חֶצְרוֹן difference at the source-language level only — the Thai output is already aligned. No action.

---

## Items requiring Ben's decision (3)

| # | Item | Decision needed |
|---|---|---|
| C | Ram/Aram | (b) normalize Ruth → อารัม (ChatGPT) **or** (c) tolerate w/ policy doc (Gemini) |
| D | RUT 1:6 פָקַד | Keep `ทรงเยี่ยมเยียน` (ChatGPT) **or** revise to `ทรงเหลียวแล` (Gemini) |
| F | RUT 1:19 הוּם | Pick from `ฮือฮา` / `เกิดความฮือฮา` / `ต่างพากันฮือฮา` |

## Items recommending new corpus docs (2)

| # | Doc | Trigger book |
|---|---|---|
| A | `divine_anthropomorphism_thai_grammar_2026-05.md` | Before Exod 7 / Pss / Isaiah |
| G | `goel_kinsman_redeemer_2026-05.md` (with three-tier usage distinction) | Before Phase 6C (Lev 25) |

## Pure LOCK-as-is items (4)

B (כָּנָף wordplay), E (מְנוּחָה contextual), H (divine-action attribution), I (pronoun escalation).

## Tooling fix (1)

§Z.1 — `scripts/build_external_review_packet.py` SBLGNT/Greek hardcoding for OT books.

---

## Recommended next steps

1. Ben answers the three DECIDE items (C, D, F).
2. Open a single revision PR applying the agreed changes:
   - Item F spot-revise (Ben picks the phrase).
   - Item D spot-revise (only if Ben chooses Gemini's `ทรงเหลียวแล`).
   - Item C either (b) Mt + Lk backfill or (c) policy doc.
   - §Z.1 packet-builder fix.
3. Optionally bundle the recommended corpus docs (A and G) into a separate decision-docs PR before tagging.
4. Tag `book-ruth-v1`.
5. Resume `/loop eremos translation: next` → Jonah 1.
