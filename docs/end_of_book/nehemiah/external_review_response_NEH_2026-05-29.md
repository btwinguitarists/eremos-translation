# Nehemiah external review — response + proposed actions

**Date:** 2026-05-29
**Reviewers:** Gemini 2.5 Pro + ChatGPT (web), via Cowork
**Audit packet:** `docs/end_of_book/nehemiah/external_review_packet_NEH_2026-05-29.md`
**Raw replies:** `docs/end_of_book/_external_inbox/NEH_raw.md`
**Status:** **NOT tag-clear.** Unlike Ezra (all lock-as-is), three of four items are verified-real:
- **Item B** — 2 proposed verse edits (NEH 9:17, 9:31) realigning shipped text to an **existing** lock.
- **Item A** — a corpus-level foreign-emperor register decision that **governs the imminent Esther + Daniel translations** and **reverses the Ezra review's Item A**. Needs Ben.
- **Item C** — a Persian-title consistency decision. Needs Ben.
- **Item D** — locks as-is.

> **Method note.** Per `_external_inbox/README.md`, Claude Code cross-checked **every** reviewer claim against `output/translations/*.json` and the cited lock/policy docs before promoting it to an action. No verse edits are auto-applied; everything below is **proposed** for Ben's sign-off (shipped/locked surfaces are sacred). Where the verification *changed* or *sharpened* a reviewer claim, that is called out explicitly.

---

## Convergence summary

| Item | Gemini | ChatGPT | Claude Code verification (vs JSON + locks) | Action |
|------|--------|---------|---------------------------------------------|--------|
| **A — Foreign-emperor honor register** | MAJOR CONCERN | MAJOR CONCERN | **CONFIRMED real + policy-decisive.** NEH narrator uses royal register for Artaxerxes (`ตรัส` 2:2/2:6, `ทรงส่ง` 2:9 — its key_decision *explicitly cites* `ot_register_policy §2.2`). EZR 1:7 uses plain `ได้นำ` for Cyrus (note says "plain register, deliberate"); 2 Chr 36:22 keeps Cyrus plain. **§2.2 sides with Nehemiah.** Added nuance: Ezra is *internally* mixed — 7:6/7:11 give Artaxerxes the royal give-verb `ประทาน`. | **DECISION — Ben.** Reconcile §2.2 ⇄ shipped Ezra ⇄ the Ezra review. **Governs Esther/Daniel.** |
| **B — NEH 9:17 / 9:31 Exod-34 formula drift** | CONCERN | MAJOR CONCERN | **CONFIRMED real.** Shipped 9:17 drifts on **all four** components vs the locked formula; 9:31 drifts (`ทรงเมตตา` vs locked `ทรงพระเมตตา`). The verse's own key_decision *falsely claims* it preserved the formula. The lock (`exod_34_attribute_formula_2026-05.md`, the Neh 9:17 row) already prescribes the exact target string. | **Propose 2 verse edits** (Ben sign-off) + add the full formula to hard-check enforcement. |
| **C — Persian governor title** | CONCERN | CONCERN | **CONFIRMED real.** `פֶּחָה` rendered `เจ้าเมือง` (5:14, 5:15, 5:18) but `ผู้ว่าราชการ` (12:26); `תִּרְשָׁתָא` rendered `ผู้ว่าราชการ` throughout (7:65, 7:70, 8:9, 10:1). No Persian-administrative-title lock exists (only `roman_administrative_titles_2026-04.md`). | **DECISION — Ben.** Pick one term; document `תִּרְשָׁתָא`; write a Persian-title doc. |
| **D — Greek tradition (1 Esdras / Esdras B) disclosure** | FINE | FINE | **Confirmed.** NEH 7:68 carries an inline key_decision documenting the MT-vs-Ezra 2:66 horses/mules difference; situation is below the `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 disclosure floor. | Lock as-is. Optional book-level note only. |

---

## Items in detail

### Item A — Foreign-emperor honor register (Artaxerxes / Cyrus)

- **Gemini — MAJOR CONCERN.** Ezra and Nehemiah feature the same historical king (Artaxerxes) but clash in register across the book boundary (plain `ได้นำ` EZR 1:7 vs. royal `ตรัส`/`ทรงส่ง` NEH 2:2, 2:9). Since `ot_register_policy §2.2` dictates that foreign emperors receive ราชาศัพท์, **Nehemiah is correct and Ezra is the outlier.** Recommends: lock Nehemiah's full-ราชาศัพท์ approach as the corpus standard; spot-revise Ezra (and 2 Chr 36) to elevate Cyrus/Darius/Artaxerxes; write a corpus doc so Esther + Daniel follow suit.
- **ChatGPT — MAJOR CONCERN.** Same diagnosis: the same king cannot be common-register in Ezra and royal in Nehemiah. The written policy already grants foreign emperors ราชาศัพท์, so Nehemiah is internally compliant and Ezra / 2 Chr 36:23 are the outliers. Recommends: Ben decides now, then write a corpus doc; normalize Ezra's emperors to Nehemiah's approach before tagging Ezra/Nehemiah/Esther/Daniel.

- **Claude Code verification — CONFIRMED, with a sharper picture than either AI gave:**
  - **NEH narrator = royal, by design.** NEH 2:2 `กษัตริย์ตรัสกับข้าพเจ้า`; 2:6 `กษัตริย์ตรัส…โดยมีพระมเหสีประทับ`; 2:9 `กษัตริย์ทรงส่ง`. The 2:2 key_decision states verbatim: *"ราชาศัพท์ 'ตรัส' สำหรับการพูดของกษัตริย์เปอร์เซีย ตาม ot_register_policy §2.2 — จักรพรรดิต่างชาติได้รับ ทรง-/พระ- ในเสียงผู้เล่า."* Nehemiah is consciously applying §2.2.
  - **EZR narrator = plain for Cyrus, by design.** EZR 1:7 `กษัตริย์ไซรัส…ได้นำ`; the verse note states: *"REGISTER: ไซรัสแปลด้วยภาษาสามัญ สอดคล้องกับการเลือกในข้อ 2."* 2 Chr 36:22 likewise keeps Cyrus plain (`ให้ออกประกาศ`; the `ทรง` there belongs to YHWH, who `ทรงเร้า` Cyrus).
  - **New finding — Ezra is *internally* inconsistent too.** EZR 7:6 and 7:11 give Artaxerxes the royal give-verb `ประทาน` ("the king `ประทาน`/granted"). So the drift is not a clean Ezra-plain / Nehemiah-royal split; Ezra mixes registers within itself. This *strengthens* the underlying point: there is no consistently-applied, documented rule.
  - **The policy is unambiguous.** `ot_register_policy_2026-05.md` §2.2 table row: **"Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, Darius, Xerxes) → Narrator-voice: ราชาศัพท์ (ทรง) — they are the imperial sovereigns of their narratives, even if villainous."** §2.5 confirms the split: the Hebrew-servant *viziers* (Joseph, Daniel, Mordecai, **Nehemiah**) do **not** receive `ทรง-`; only the emperors themselves do. Nehemiah's translation correctly gives `ทรง-` to **Artaxerxes the emperor**, not to Nehemiah-the-cupbearer — fully §2.2/§2.5 compliant.
  - **Therefore the Ezra review's Item A conclusion was wrong relative to the project's own §2.2.** That review (`docs/end_of_book/ezra/external_review_response_EZR_2026-05-28.md`) concluded "lock Ezra's plain register" and proposed a `foreign_monarch_register_2026-05.md` codifying *non*-royal default. **That doc was never written** (confirmed absent), so §2.2 still stands as the governing policy — and §2.2 favors Nehemiah.

- **Proposed action — DECISION REQUIRED (Ben).** This is the single highest-value output of this review. Reconcile three things now: (1) `§2.2` as written, (2) the shipped Ezra/2 Chr text, (3) the Ezra review's contrary Item A. Both external AIs *and* the standing policy converge on **royal register for foreign emperors**. If Ben affirms that:
  - Write `docs/translator_decisions/foreign_monarch_register_2026-05.md` codifying: *foreign imperial monarchs receive narrator-voice ราชาศัพท์ (Cyrus, Darius, Xerxes/Ahasuerus, Artaxerxes); their Hebrew-servant viziers do not (per §2.5).* This **supersedes the Ezra review's Item A**.
  - Schedule spot-revisions to Ezra (esp. 1:7 + any plain emperor-action verbs) and 2 Chr 36:22–23 — **shipped text, so itemize and sign off per verse** (candidate list deferred until the rule is fixed; see below).
  - Apply the rule to **Esther** (Ahasuerus = foreign emperor; Esther/queen → ราชาศัพท์ in royal-office context per §2.2) and **Daniel** (Nebuchadnezzar / Belshazzar / Darius) from the first chapter.

### Item B — NEH 9:17 / 9:31 drift from the locked Exodus-34 formula

- **Gemini — CONCERN.** 9:17 (`พระเจ้าผู้อภัย`, `ทรงเมตตา`, `ทรงพระพิโรธช้า`, `เปี่ยมด้วย…`) and 9:31 (`ทรงเมตตา`) violate the surface locked in `exod_34_attribute_formula_2026-05.md`, obscuring the Sinai (Exod 34:6) ↔ Nehemiah penitential-prayer echo. Recommends spot-revising to the locked formula.
- **ChatGPT — MAJOR CONCERN.** Same components flagged (`ทรงกริ้วช้า`→`ทรงพระพิโรธช้า`, `ทรงบริบูรณ์ด้วย…`→`เปี่ยมด้วย…`, `พระเจ้าผู้ทรงประทานการอภัย`→`พระเจ้าผู้อภัย`). Recommends revising 9:17 + 9:31 (`ทรงพระเมตตา`) **and adding the full formula to hard-check enforcement, not just the `ความรักมั่นคง` token.**

- **Claude Code verification — CONFIRMED real on both verses:**
  - **Locked target** (`exod_34_attribute_formula_2026-05.md`, the explicit Neh 9:17 row): `พระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง`.
  - **Shipped 9:17:** `…แต่พระองค์ทรงเป็นพระเจ้าผู้อภัย ผู้ทรงพระคุณและทรงเมตตา ทรงพระพิโรธช้า และเปี่ยมด้วยความรักมั่นคง…` — drifts on **all four** locked components.
  - **Shipped 9:31:** `…พระเจ้าผู้ทรงพระคุณและทรงเมตตา` — drifts (`ทรงเมตตา` vs locked `ทรงพระเมตตา`).
  - **Aggravating:** the 9:17 key_decision *asserts* it "preserves the same form as elsewhere" (`คงรูปเดียวกันกับการแปลในที่อื่น`) — but it does not. The leitwort lock + `ความรักมั่นคง` hard-check did not catch this because the drift is in the *other three* components.

- **Proposed action.** (1) Two verse edits below (Ben sign-off). (2) Adopt ChatGPT's systemic fix: extend the hard-check to the **full** Exod-34 formula surface, not just the `ความรักมั่นคง` token, so future recitations (Esther has none, but Psalms/Joel/Jonah recurrences do) cannot silently drift.

### Item C — Persian governor title (`פֶּחָה` / `תִּרְשָׁתָא`)

- **Gemini — CONCERN.** Internal inconsistency: Nehemiah is `เจ้าเมือง` in 5:14 but `ผู้ว่าราชการ` in 12:26; the Persian loanword `תִּרְשָׁתָא` is silently collapsed into a generic Thai title without a recorded rationale. Recommends: standardize Nehemiah's `פֶּחָה` to one term (prefers `ผู้ว่าราชการ`); either transliterate `תִּרְשָׁתָא` or document the collapse.
- **ChatGPT — CONCERN.** Same internal-inconsistency point; recommends a Persian-administration title doc; normalize 12:26; reader-first `เจ้าเมือง`/`ผู้ว่าราชการ` over transliteration, but **document** that it is Nehemiah's Persian office.

- **Claude Code verification — CONFIRMED real:**
  - `פֶּחָה` → `เจ้าเมือง` in 5:14 (`ทรงแต่งตั้งให้ข้าพเจ้าเป็นเจ้าเมือง`), 5:15 (`เจ้าเมืองคนก่อนๆ`), 5:18 (`อาหารที่ทางการจัดให้เจ้าเมือง`).
  - `פֶּחָה` → `ผู้ว่าราชการ` in 12:26 (`เนหะมีย์ผู้ว่าราชการ`).
  - `תִּרְשָׁתָא` → `ผู้ว่าราชการ` in 7:65, 7:70, 8:9 (`เนหะมีย์ผู้ว่าราชการ`), 10:1.
  - Net: **two Thai terms for Nehemiah's one office**, and the distinct loanword `תִּרְשָׁתָא` folded into `ผู้ว่าราชการ` with no documented decision. The reviewers diverge on the preferred term (Gemini → `ผู้ว่าราชการ`; ChatGPT → `เจ้าเมือง` for the Judah level) — a genuine fork for Ben.

- **Proposed action — DECISION (Ben).** Pick **one** Thai term for Nehemiah's `פֶּחָה`/`תִּרְשָׁתָא` office across the book; normalize the outliers (either lift 5:14/5:15/5:18 to match 12:26, or lower 12:26 to match ch. 5); record the `תִּרְשָׁתָא` handling. Capture it in a new `docs/translator_decisions/persian_administrative_titles_2026-05.md` (parallel to the existing Roman one) so Esther (Mordecai's offices, satraps) and Daniel (satraps/`אֲחַשְׁדַּרְפְּנִים`) inherit a fixed scheme.

### Item D — Greek tradition (1 Esdras / Esdras B) disclosure

- **Gemini — FINE.** Below the disclosure floor; 1 Esdras is a distinct recension (macro-structural), Esdras B tracks MT; the inline NEH 7:68 versification note is the correct approach. Lock as-is; maintain silence in the textual-variant files, mirroring Ezra.
- **ChatGPT — FINE.** MT-anchored; no macro reader-affecting divergence requiring per-verse treatment; 7:68 horses/mules already disclosed inline. Optional: one book-level internal audit note, but do not burden the reader text.

- **Claude Code verification — confirmed.** NEH 7:68 (`อูฐ 435 ตัว และลา 6,720 ตัว`) carries a key_decision documenting that the MT lacks the "736 horses, 245 mules" line present in Ezra 2:66, restored in English/BSB by comparison with Ezra 2 — exactly the inline handling both AIs endorse. Below `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3.

- **Proposed action.** Lock as-is. **Optional** (low priority): one book-level line in `mt_vs_lxx_textual_variant_handling_2026-05.md` or `ot_canon_and_text_base_2026-05.md` noting Nehemiah is MT-anchored and 1 Esdras/Esdras B is treated as a separate Greek book-form, mirroring the Ezra disposition. Reader text unchanged either way.

---

## Proposed verse edits — REQUIRES BEN SIGN-OFF

**Item B (high confidence — realigns shipped text to an existing lock):**

1. **Nehemiah 9:17** — align the attribute formula to the locked Exod-34 surface.
   - **Before:** `…แต่พระองค์ทรงเป็นพระเจ้าผู้อภัย ผู้ทรงพระคุณและทรงเมตตา ทรงพระพิโรธช้า และเปี่ยมด้วยความรักมั่นคง พระองค์มิได้ทรงทอดทิ้งพวกเขา`
   - **After:** `…แต่พระองค์ทรงเป็นพระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง พระองค์มิได้ทรงทอดทิ้งพวกเขา`
   - Also correct the verse's `key_decisions` rendering string to match, so the metadata stops asserting false compliance.

2. **Nehemiah 9:31** — restore the locked `רַחוּם` token.
   - **Before:** `…เพราะพระองค์ทรงเป็นพระเจ้าผู้ทรงพระคุณและทรงเมตตา`
   - **After:** `…เพราะพระองค์ทรงเป็นพระเจ้าผู้ทรงพระคุณและทรงพระเมตตา`

**Item A (deferred — contingent on the register decision):** if Ben affirms royal register for foreign emperors, a per-verse candidate list for Ezra (1:7 and other plain emperor-action verbs) and 2 Chr 36:22–23 will be drawn up for separate sign-off. Not itemized here because the target rule is not yet fixed, and both are **shipped** books.

**Item C:** no edit proposed until Ben picks the single term; then normalize the 2–3 outlier verses.

---

## Relationship to prior reviews

- **This review reverses Ezra review Item A.** The Ezra review locked plain register for foreign monarchs and proposed (never-written) `foreign_monarch_register_2026-05.md`. That conclusion contradicts `ot_register_policy §2.2` as written. The Nehemiah review — and the standing policy — favor royal register. Ben's Item A decision should explicitly settle which governs.
- **External-AI verdicts are context-bound, not authoritative.** The *same* two models called plain register "FINE" for Ezra and "MAJOR CONCERN" for Nehemiah. That flip is itself a signal: weight the project's own §2.2 as the anchor, not the per-book AI verdict.

---

## ⚠️ Should precede Esther

The user is starting **Esther** next (Phase 6E). Item A directly governs Esther's register: **Ahasuerus** is a foreign emperor (§2.2 → narrator-voice ราชาศัพท์) and **Esther/Vashti** are queens (§2.2 → ราชาศัพท์ in royal-office context). Deciding Item A **before or at the start of Esther** prevents a third book from being shipped on an undecided rule and then needing retroactive revision.

---

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/NEH_raw.md` (Cowork → Gemini 2.5 Pro + ChatGPT, 2026-05-29). Per `_external_inbox/README.md`, Claude Code cross-checked every claim against `output/translations/nehemiah_*.json`, `output/translations/ezra_*.json`, `output/translations/2chronicles_36.json`, and the cited lock/policy docs (`ot_register_policy_2026-05.md` §2.2/§2.5, `exod_34_attribute_formula_2026-05.md`). The reviewers' specific verse citations all checked out; the cross-check additionally found (a) Ezra's *internal* register inconsistency at 7:6/7:11, and (b) that the never-written `foreign_monarch_register` doc leaves §2.2 as the governing policy — both of which make Item A a clearer call than the raw replies alone. No verse edits applied; all actions await Ben's sign-off.
