# 1 Samuel — End-of-Book Review

**Date:** 2026-05-22
**Scope:** All 31 chapters of 1 Samuel (811 verses); `glossary.json`; `docs/translator_decisions/` corpus (~90 docs through the JDG end-of-book audit).
**Trigger:** 1SA 31 shipped (commit `bd8dd88`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Ninth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges) and the **third Former-Prophets / Deuteronomistic-History book** — the first downstream stress-test of the JDG-audit locks (Spirit-of-YHWH, Adonai-prayer-cluster, Heb 11:32 name-corpus) outside Judges itself.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **20 cross-cutting items reviewed.** Mechanical gates (§1) pass: 31/31 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `check_divine_names.py` 0 hard fails (125 [C-soft] warnings — all human-addressee אֲדֹנִי, expected per §2); `audit_inclusion_variants.py --book 1samuel --strict` reports 0 candidates; 31/31 chapters have `output/textual_variants/1samuel_NN.json`.
- **1 Samuel is the first downstream stress-test of the JDG end-of-book audit locks.** Two of JDG's most-load-bearing new docs (`spirit_of_yhwh_empowerment_2026-05.md` lock; the forthcoming dtr-history-cycle-formulas doc recommended in JDG §6) face their first downstream encounter here.
  - **The `spirit_of_yhwh_empowerment_2026-05.md` lock FAILS in 1 Samuel.** All 12 Spirit-occurrences (10:6, 10:10, 11:6, 16:13, 16:14, 16:15, 16:16, 16:23, 18:10, 19:9, 19:20, 19:23) use bare **`วิญญาณ`** (no พระ honorific). The JDG corpus uses **`พระวิญญาณ`** uniformly. The lock — written 2026-05-20, two days before this audit, after the JDG audit — explicitly forward-protects 1 Sam 10:6, 10:10, 11:6, 16:13; yet 1 Sam shipped with the bare-form drift. The צָלַח-rush verses (10:6, 10:10, 11:6, 16:13) additionally drop the locked `อย่างทรงพลัง` adverbial. **HIGHEST-severity DECIDE.**
  - **DTr "did evil in the eyes of YHWH" cycle refrain — N/A in 1SA.** The Judges-era cycle ends at 1 Sam 7; the formula does not recur in 1SA. The recommended `dtr_history_cycle_formulas_2026-05.md` doc remains forward-pending for Kings + Chronicles.
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-1samuel-v1`):
  - **§4 Spirit-of-YHWH empowerment book-wide drift** — HIGHEST severity; contradicts a locked doc; ~12 surgical verse-edits required.
  - **§17 MT/LXX inclusion-variant gap** — the 1 Sam 17 LXX-B shortenings (and 11:1 4QSamᵃ, 13:1 regnal corruption, 14:41 LXX Urim/Thummim expansion) are not documented in `output/textual_variants/1samuel_NN.json`. First major-shortening corpus encounter; gates the Tier-2 textual-variants infrastructure.
- **6 items flagged REVIEW** (worth Ben's confirmation):
  - §5 "Is Saul also among the prophets?" inclusio surface drift (10:11+12 vs 19:24)
  - §12 Pagan-deity register drift at 1 Sam 5:7 (Dagon → พระเจ้า in pagan speech) + Ashtaroth 3-form spelling drift (อัชโทเรท / อาเชโทรท / อัชทาโรท)
  - §15 Sacrificial-vocabulary minor drift (מִנְחָה collapse + שְׁלָמִים 2 surfaces)
  - §3 mal'akh human-messenger surface split (ผู้ส่งสาร vs ผู้ส่งข่าว)
  - §6 Hannah's bare-form "นายของข้า" (vs standard "เจ้านายของข้า") — defensible humble-register, but undocumented
  - §19 Annotation-architecture undercoverage in chs 16+ (`thai_summary` < 50% verse coverage in chs 16, 17, 18, 19, 21, 25, 27, 29) — mirrors JDG-19-21 pattern in reverse direction
- **3 items recommend new corpus docs** (STABLE-but-undocumented):
  - §10 Witch of Endor + necromancy vocabulary lock (28:3–25) — forward-protects 1 Chr 10:13, 2 Kgs 21:6, 23:24, Isa 8:19, Lev 19:31 + 20:6/27 retroactive
  - §7 Hannah's Song ↔ Magnificat (Luke 1:46-55) NT cross-corpus thread — Layer-2 enhancement
  - §13 1 Sam 15 חרם + Saul-Amalek narrative — though `ot_warfare_ethics_2026-05.md` already covers the ḥerem lemma, 15:22 ("to obey is better than sacrifice") is a load-bearing prophetic-aphorism that warrants a corpus-level cross-reference to Hos 6:6 + Matt 9:13 + Matt 12:7 + Mark 12:33
- **External AI review (§3) pending.** Suggested 5-item packet (Spirit-of-YHWH drift §4 — HIGHEST priority; Adonai-cluster forward-projection §6; inclusion-variant gap §17; witch-of-Endor + theological-Christology §10+§7; "Saul among prophets" inclusio §5).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH occurs **320×** across the 31 chapters of 1 Samuel. Thai `องค์พระผู้เป็นเจ้า` in `thai` verse-text: **319 surface matches** (1:1 ratio — minor under-count is a single collapsed `לַיהוָה` at 1:28 where the immediate-preceding occurrence is absorbed into the Samuel/שָׁאוּל wordplay; not a drift).

**ยาห์เวห์ residues: zero in verse text.** One occurrence at 1SA 18:1 inside a `key_decisions.note` ("…เปรียบกับการอ้างของยาห์เวห์ในความสัมพันธ์พันธสัญญา…ฉธบ 11:1 'ผูกใจกับ YHWH'") — meta-discussion in editorial commentary, not the Thai surface; acceptable per `divine_names_table_2026-05.md` §"Layer 1 transparency" carve-out.

**YHWH-absent chapters.** 1SA 27 and 1SA 31 contain **zero יהוה occurrences** in the MT. Both are flagged in `output/textual_variants/1samuel_27.json` and `_31.json` with `type: "chapter_overview_note"` documenting the literary significance ("บทที่ไม่มี Tetragrammaton — โดดเด่นทางวรรณกรรม" — David in Philistine territory; Saul's death scene narrated from outside the YHWH-relational frame). Good editorial pattern.

**Per-chapter first-occurrence YHWH footnote.** 29/31 chapters (all that contain YHWH) carry the locked Tier-2 explanation in `output/textual_variants/1samuel_NN.json` per `divine_names_table_2026-05.md` §"Layer 2". `check_divine_names.py --report` shows 245/245 chapters with footnote across the corpus — clean.

Corpus-total YHWH count after 1SA: ~2,190+ occurrences across 370 chapters, uniformly rendered.

**LOCKED** ✓.

---

## 2. Elohim + Adonai compound divine names — **LOCKED (no divine-Adonai prayer in 1SA)**

- **Elohim → พระเจ้า** uniform across 1SA ✓ (~120 occurrences). No drift.
- **No Adonai-YHWH compound (אֲדֹנָי יְהוִה) occurs in 1SA.** The compound's first major recurrence after Joshua-Judges is at 2 Sam 7:18–29 (David's covenant prayer — 7× in one prayer). The JDG-audit §8 DECIDE on Adonai-prayer 5-form drift does NOT compound through 1SA — but is forward-deferred to 2 Sam 7.
- **No standalone divine-Adonai in prayer occurs in 1SA.** Hannah's prayer (1:11) addresses "יְהוָה צְבָאוֹת" (Lord of hosts) directly with the full Tetragrammaton-Tsebaoth compound — see §6. Samuel's "Speak, for your servant hears" (3:9–10) addresses "יְהוָה" without an Adonai vocative.
- **125 [C-soft] warnings from `check_divine_names.py`** — all are human-addressee אֲדֹנִי "my lord" → addressed to Eli (Hannah), to Saul (David, Ahimelech, Achish), to David (Abigail, Nabal's men), to Jonathan (his armor-bearer), to an Amalekite (the Egyptian slave at 30:13/15). All correct per category (c) of `divine_names_table_2026-05.md` §"4-way distinction" — non-divine "my lord" address. **The 125 [C-soft] count overestimates risk for 1SA** specifically because category (c) is dense in 1SA (David's interactions with Saul + Abigail-pericope + Achish dialogues). See §6 for the single intra-1SA register drift.

**LOCKED** ✓ (forward-defer to 2 Sam 7:18-29 for the divine-Adonai-prayer recurrence).

---

## 3. mal'akh — **STABLE (zero divine-mal'akh; human-messenger surface mildly split)**

**No מַלְאַךְ יְהוָה / מַלְאַךְ הָאֱלֹהִים in 1 Samuel.** The book is the first OT-narrative book without a mal'akh-YHWH narrative-block since Joshua (Genesis through JDG all carried major mal'akh-YHWH cycles; 1SA does not). The next major divine-mal'akh cycle is 2 Sam 24 (Davidic-census plague) + 1 Kings 19 (Elijah at Horeb) + 2 Kings 1 (Ahaziah's messengers).

**Every מַלְאָךְ in 1 Samuel is human messenger.** Total: 22 occurrences across 6:21, 11:3+4+7+9, 16:19, 19:11+14+15+16+20+21 (×2), 23:27, 25:14+42 (+ a few cross-refs).

| Hebrew | Thai surface | Verses |
|---|---|---|
| מַלְאָךְ (Israelite envoys) | **ผู้ส่งข่าว** | 6:21, 11:3, 11:4, 11:7, 11:9 |
| מַלְאָךְ (Saul's pursuers + David's envoys) | **ผู้ส่งสาร** | 16:19, 19:11–21, 23:27, 25:14, 25:42 |

**Minor drift.** Two Thai surfaces for the same Hebrew lemma in the same narrative function. The early chs (6:21 + ch 11) use `ผู้ส่งข่าว`; ch 16 forward uses `ผู้ส่งสาร`. Both are defensible Thai — but the inconsistency creates surface-noise. **REVIEW — recommend normalize to `ผู้ส่งสาร`** (matches the higher-count cluster + general OT-narrative usage).

**One mal'akh-Elohim simile.** 29:9 (Achish to David): כְּמַלְאַךְ אֱלֹהִים → **"เหมือนทูตของพระเจ้า"**. Distinctive use of `ทูต` (vs the human-messenger `ผู้ส่งสาร / ผู้ส่งข่าว`) — preserves the divine-comparative register; matches `malak_yhwh_2026-05.md` Layer-2 (`ทูต` reserved for actual or comparative angelic referents). ✓

**LOCKED-with-§3-REVIEW-flag** (human-messenger surface split).

---

## 4. Spirit-of-YHWH empowerment — **DECIDE before tagging (HIGHEST severity)**

**Book-wide drift from the locked `spirit_of_yhwh_empowerment_2026-05.md` doc.**

The Spirit-of-YHWH lock was finalized **2026-05-20**, two days before this audit, **specifically to forward-protect 1 Samuel** (the doc's §1.1 row for צָלַח explicitly cites "forward-protect 1 SAM 10:6, 10:10, 11:6, 16:13 (Saul + David)"). The locked corpus surface — verified compliant across all 7 JDG occurrences (3:10, 6:34, 11:29, 13:25, 14:6, 14:19, 15:14) — requires:

1. **`พระวิญญาณ`** (with the พระ honorific on Spirit)
2. **`มาเหนือ…อย่างทรงพลัง`** specifically for the צָלַח-verb (Spirit-rushes-on-with-power) class

**1 Samuel ships 12 Spirit-occurrences that ALL drift from this lock.** Surveyed surfaces (every verse uses bare **`วิญญาณ`** with no พระ; צָלַח-class verses drop the locked `อย่างทรงพลัง`):

| Ref | Hebrew verb | Sense | 1SA Thai (shipped) | Locked Thai (expected) |
|---|---|---|---|---|
| **10:6** | **צָלַח** | empowerment (Saul) | `วิญญาณขององค์พระผู้เป็นเจ้าจะรุดมาเหนือเจ้า` | `พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเจ้าอย่างทรงพลัง` |
| **10:10** | **צָלַח** | empowerment (Saul) | `วิญญาณของพระเจ้ารุดมาเหนือเขา` | `พระวิญญาณของพระเจ้าก็มาเหนือเขาอย่างทรงพลัง` |
| **11:6** | **צָלַח** | empowerment (Saul vs Nahash) | `วิญญาณของพระเจ้ารุดมาเหนือซาอูล` | `พระวิญญาณของพระเจ้าก็มาเหนือซาอูลอย่างทรงพลัง` |
| **16:13** | **צָלַח** | empowerment (David's anointing) | `วิญญาณขององค์พระผู้เป็นเจ้ารุดมาเหนือดาวิดตั้งแต่วันนั้น…` | `พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือดาวิดอย่างทรงพลังตั้งแต่วันนั้น…` |
| **16:14** | סָרָה + רוּחַ רָעָה | departure + evil spirit | `วิญญาณขององค์พระผู้เป็นเจ้าจากซาอูลไปแล้ว` | `พระวิญญาณขององค์พระผู้เป็นเจ้าจากซาอูลไปแล้ว` (departure idiom; out-of-scope of צָלַח adverbial — but `พระ` still required) |
| **16:15** | רוּחַ־אֱלֹהִים רָעָה (substantive) | evil spirit | `วิญญาณชั่วจากพระเจ้ากำลังทรมานท่าน` | (evil-spirit cluster — separate forthcoming lock per spirit-of-yhwh §"Edge cases") |
| **16:16** | בִּהְיוֹת + רוּחַ־אֱלֹהִים רָעָה | evil spirit | `เมื่อวิญญาณชั่วจากพระเจ้ามาเหนือท่าน` | (same evil-spirit-cluster) |
| **16:23** | בִּהְיוֹת + רוּחַ־אֱלֹהִים | evil-spirit oscillation | `วิญญาณจากพระเจ้ามาเหนือซาอูล … วิญญาณชั่วก็ออกไป` | (evil-spirit-cluster) |
| **18:10** | **צָלַח** + רוּחַ אֱלֹהִים רָעָה | evil spirit (note: same verb as 10:6/16:13!) | `วิญญาณชั่วจากพระเจ้าก็มาเหนือซาอูล` | (צָלַח-evil-spirit hybrid — internal inconsistency: 18:10 drops both `อย่างทรงพลัง` AND `รุด`, unlike 10:6/16:13 which kept `รุด`) |
| **19:9** | תְּהִי + רוּחַ יְהוָה רָעָה | evil spirit | `วิญญาณชั่วจากองค์พระผู้เป็นเจ้ามาเหนือซาอูล` | (evil-spirit-cluster) |
| **19:20** | תְּהִי | empowerment (Saul's messengers) | `วิญญาณของพระเจ้าก็มาเหนือผู้ส่งสารของซาอูล` | `พระวิญญาณของพระเจ้าก็มาเหนือผู้ส่งสารของซาอูล` (תְּהִי = locked "มาเหนือ" — adverb already absent in lock for this verb-class ✓; only the `พระ` is needed) |
| **19:23** | תְּהִי | empowerment (Saul) | `วิญญาณของพระเจ้าก็มาเหนือเขา` | `พระวิญญาณของพระเจ้าก็มาเหนือเขา` (same) |

**Three distinct sub-drifts:**

1. **Book-wide bare-`วิญญาณ` (12/12 verses).** The locked surface requires `พระวิญญาณ` (uniform across JDG 3:10 / 6:34 / 11:29 / 13:25 / 14:6 / 14:19 / 15:14). This is a clean break from the JDG-corpus convention. The bare `วิญญาณ` form might be a Saul-Spirit Christological-typology decision (Saul's experience of the Spirit is corrupted by his disobedience; bare form signals diminished theological honor) — but if so, the principle is undocumented, and the FOUR David-empowerment verses (10:6 is mediated to David in 10:1 context; 16:13 is David's anointing-Spirit) carry the diminution too.

2. **The locked `อย่างทรงพลัง` adverbial dropped at all 4 צָלַח-empowerment verses (10:6, 10:10, 11:6, 16:13).** Replaced with `รุดมาเหนือ` (literally "[Spirit] rushes-onto" — preserves the suddenness sense but loses the locked surface). The 18:10 צָלַח-evil-spirit verse drops both `อย่างทรงพลัง` AND the substitute `รุด`, creating an internal inconsistency (good-spirit-צָלַח = `รุดมาเหนือ`; evil-spirit-צָלַח = bare `มาเหนือ`). The Hebrew verb is identical at 10:6 + 16:13 + 18:10; the Thai surface should be uniform per verb-class.

3. **Internal inconsistency in the evil-spirit cluster (16:14–23, 18:10, 19:9).** "ทรมาน" used at 16:14+15 ("วิญญาณชั่ว…ทรมานเขา"); plain "มาเหนือ" used at 16:16+23, 18:10, 19:9. Multiple surface forms for the same evil-spirit-from-YHWH/Elohim narrative concept. This is OUT-OF-SCOPE of the empowerment lock (per §"Edge cases" of `spirit_of_yhwh_empowerment_2026-05.md`) — but warrants its own treatment in a forthcoming `evil_spirit_from_yhwh_1sam_2026-05.md` companion doc.

**Editorial assessment.** This is the highest-stakes drift surfaced in any OT end-of-book audit to date. The lock was written specifically to protect 1 Samuel before further shipment; 1 Samuel shipped with the precise drift the lock anticipated.

**Three possible explanations (Ben to confirm):**
- **(a) Drafting predates the lock.** 1 Sam 10 + 11 + 16 + 18 + 19 shipped between 2026-05-11 (Gen end-of-book) and 2026-05-20 (JDG end-of-book, when the spirit-of-yhwh doc was first written). The 1 Sam shipped surfaces never received the lock's forward-protection because the lock was finalized after this book's drafting was already in flight. **Most likely.** If true, the fix is a single revision pass + retroactive lock-enforcement.
- **(b) Intentional Saul-Spirit Christology.** Bare `วิญญาณ` for Saul's Spirit-experience signals his corrupted relationship to YHWH; David's verses (10:6 [via Saul-mediation], 16:13 [direct], 16:14 [departure]) carry the bare form by narrative-parallel polish. But this conflicts with the 14:6 / 14:19 / 15:14 Samson JDG-lock (Samson is a textbook corrupted-Spirit-bearer, yet the JDG corpus uses `พระวิญญาณ` uniformly). **Unlikely.**
- **(c) Spelling/keystroke drift.** Unlikely given the consistency across 12 verses + 3 distinct Hebrew verb-classes.

**DECIDE before tagging — recommended path (a):**

1. **Restore `พระ` honorific** at all 12 verses (10:6, 10:10, 11:6, 16:13, 16:14, 16:15, 16:16, 16:23, 18:10, 19:9, 19:20, 19:23) — wherever a רוּחַ-divine-name Hebrew NP is rendered, prefix the locked `พระวิญญาณ`.
2. **Add `อย่างทรงพลัง`** at the 4 צָלַח-good-spirit verses (10:6, 10:10, 11:6, 16:13) to match `spirit_of_yhwh_empowerment_2026-05.md` lock.
3. **Decide the 18:10 evil-spirit-צָלַח treatment.** Either: extend the `อย่างทรงพลัง` adverb to the evil-spirit cluster (preserving verb-class principle); or write a forthcoming `evil_spirit_from_yhwh_1sam_2026-05.md` doc that locks a separate evil-spirit Thai surface family (likely "พระวิญญาณชั่วจากองค์พระผู้เป็นเจ้า…มาเหนือ…อย่างรุนแรง" or similar).
4. **Re-ship affected chapters** as a `revision/spirit-of-yhwh-1sam-2026-05` branch with surgical 12-verse edits + per-chapter check-report regeneration + back-translation refresh. (Cost: 12 verse-edits across 8 chapters; ~1 day of work.)

**Severity: HIGHEST.** This is the first OT-corpus drift discovered AGAINST an explicitly-forward-protective lock that was written before the affected book completed. **Forward-protects:**
- 2 Sam 23:2 (David's last words: "the Spirit of YHWH spoke through me" — תְּהִי class)
- 1 Kings 18:12 (Obadiah on Elijah — "the Spirit of YHWH will carry you" — נָשָׂא class, possibly out-of-scope)
- 1 Kings 22:24 + 2 Chr 18:23 (Zedekiah ben Chenaanah: "Which way did the Spirit of YHWH go from me to speak to you?" — עָבַר class, may need adjacent treatment)
- 2 Kings 2:16 (sons of the prophets on Elijah — נָשָׂא)
- 1 Chr 12:18 (Amasai — לָבְשָׁה class; explicit forward-protection in the lock)
- 2 Chr 15:1 (Azariah — הָיְתָה)
- 2 Chr 20:14 (Jahaziel — הָיְתָה)
- 2 Chr 24:20 (Zechariah ben Jehoiada — לָבְשָׁה; explicit forward-protection in the lock)
- Isa 11:2, 42:1, 59:21, 61:1 (Messianic Spirit-anointing — distinct cluster but lock-adjacent)
- NT: Luke 4:18 (Spirit-anointing); Acts 1:8 (δύναμις cf. צָלַח); Eph 5:18 (πληρόομαι Spirit-clothing)

---

## 5. "Is Saul also among the prophets?" inclusio — **REVIEW (10:11+12 vs 19:24 surface mismatch)**

The Hebrew הֲגַם שָׁאוּל בַּנְּבִיאִם is the verbatim-identical inclusio that closes Saul's first prophetic ecstasy (1 Sam 10:11–12) and re-closes his last prophetic ecstasy in failure (1 Sam 19:24, naked at Naioth). The inclusio is one of the book's signature literary architectures (alongside the rise-of-David / fall-of-Saul double-axis). The Thai surfaces drift:

| Verse | Hebrew | Thai surface |
|---|---|---|
| **10:11** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ"** |
| **10:12** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ"** (identical to 10:11 — good) |
| **19:24** | הֲגַם שָׁאוּל בַּנְּבִיאִם | **"ซาอูลก็เป็นหนึ่งในผู้เผยพระวจนะด้วยหรือ?"** (DIFFERENT) |

**Drift analysis.** The 10:11/12 form ("ก็ซาอูลด้วย…") preserves the Hebrew word-order and the rhetorical interrogative (הֲגַם = "is also/even"). The 19:24 form ("ซาอูลก็เป็นหนึ่งใน…ด้วย…") reorders to subject-first with explicit "one of" insertion + question mark — more natural Thai prose but breaks the inclusio's verbatim function.

**REVIEW flag.** Recommend normalize 19:24 to the 10:11/12 form ("ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ") to preserve the inclusio. Mirrors the JDG-audit §7 17:6 ↔ 21:25 inclusio drift (same architectural issue, different book). **Severity: LOW–MEDIUM** — single-verse normalization.

---

## 6. Hannah's prayer + Song + the Adonai-humble register — **STABLE-with-REVIEW-flag**

**Hannah's prayer (1:11) — divine-name vocative.** 1:11 + 1:3 + 1:26 (×3 total) address YHWH-Tsebaoth: **`องค์พระผู้เป็นเจ้าจอมโยธา`** — matches `divine_names_table_2026-05.md` lock (consistent with Jas 5:4 NT YHWH-Sabaoth) ✓. **LOCKED.**

**Hannah's interaction with Eli — the humble-Adonai register drift.** 1:15 and 1:26 (×2) address Eli with the bare-form **`นายของข้า`**. Every OTHER human-addressee אֲדֹנִי in 1 Samuel uses **`เจ้านายของ___`** (e.g., 22:12 Ahimelech to Saul; 24:7+9+11 David to Saul; 25:24-31 Abigail to David; 26:15+17+18 David to Abner/Saul; 30:13 Egyptian slave). Hannah is the **only** speaker in 1SA who downshifts to bare `นายของข้า`.

| Ref | Speaker → Addressee | Thai surface |
|---|---|---|
| 1:15 | Hannah → Eli (defense — "I am a woman of sorrowful spirit") | **`นายของข้า`** |
| 1:26 (×2) | Hannah → Eli ("for this child I prayed") | **`นายของข้า`** |
| 22:12, 24:7, 24:9, 24:11, 25:14, 25:17, 25:24–31, 25:41, 26:15+17+18, 26:19, 29:4, 29:8, 29:10, 30:13, 30:15 | various → various | **`เจ้านายของ___`** |
| 20:38 | narrator (of the boy → Jonathan) | **`นายของเขา`** (third-person — bare form is correct for non-vocative narrator) |

**Editorial assessment.** Hannah's humble-Adonai is plausibly a deliberate Magnificat-foreshadowing — Hannah is presented as the OT-template for the *anawim* ("the lowly") who become the locus of YHWH's covenant action (cf. Luke 1:48 "he has regarded the humble estate of his maidservant"). The bare `นายของข้า` (vs the higher-register `เจ้านายของข้า` used by Abigail to David) signals Hannah's self-effacement at the moment of her vow + post-vow defense. **Defensible.**

But the **principle is undocumented** — neither `divine_names_table_2026-05.md` nor `honorifics_non_divine_authorities_2026-04.md` carves out a humble-Adonai-vocative register for the OT *anawim*. The exception is principled but invisible to a future translator drafting (e.g.) the Sons-of-Korah Psalms or Ruth-to-Boaz (Ruth 2:13 — אֲדֹנִי, "ขอจงโปรดเถิด นายของข้า"; need verification in shipped RUT corpus).

**REVIEW.** Two paths:
- **(a) Document and lock as a new principle.** Write a brief amendment to `divine_names_table_2026-05.md` adding category (c′): humble-Adonai *anawim*-vocative → `นายของข้า` (vs the standard `เจ้านายของ___`). Cross-reference Hannah, Ruth (if applicable), and forward-protect Magnificat-template OT female voices.
- **(b) Normalize Hannah's 3 occurrences** to `เจ้านายของข้า` for corpus uniformity. Lower theological texture; cleaner mechanical-check posture.

Recommend **(a)**. **Severity: LOW.** Not blocking the v1 tag.

**Song of Hannah (2:1–10).** Translation is theologically rich and preserves the Magnificat parallel structure. Verified renderings:

| Verse | Hebrew | Thai surface |
|---|---|---|
| 2:1 | עָלַץ לִבִּי בַּיהוָה רָמָה קַרְנִי בַּיהוָה | "หัวใจของข้ายินดีในองค์พระผู้เป็นเจ้า เขาของข้าได้ถูกชูในองค์พระผู้เป็นเจ้า" |
| 2:2 | אֵין־קָדוֹשׁ כַּיהוָה … וְאֵין צוּר כֵּאלֹהֵינוּ | "ไม่มีผู้บริสุทธิ์เหมือนองค์พระผู้เป็นเจ้า … ไม่มีศิลาเหมือนพระเจ้าของพวกเรา" |
| 2:6 | יְהוָה מֵמִית וּמְחַיֶּה מוֹרִיד שְׁאוֹל וַיָּעַל | "องค์พระผู้เป็นเจ้าทรงให้ตายและให้มีชีวิต ทรงนำลงสู่แดนคนตายและทรงนำขึ้น" |
| 2:7 | יְהוָה מוֹרִישׁ וּמַעֲשִׁיר מַשְׁפִּיל אַף־מְרוֹמֵם | "ทรงทำให้ยากจนและทรงทำให้รวย ทรงทำให้ต่ำและทรงยก" |
| 2:8 | מֵקִים מֵעָפָר דָּל מֵאַשְׁפֹּת יָרִים אֶבְיוֹן | "ทรงยกผู้ยากจนขึ้นจากผง ทรงยกผู้ขัดสนจากกองขี้เถ้า" |
| 2:10 | קֶרֶן מְשִׁיחוֹ | **"ทรงยกเขาของผู้ที่พระองค์ทรงเจิมไว้"** |

The 2:10 "horn of his anointed" preserves both קֶרֶן ("horn" → `เขา`) and the מָשִׁיחַ-link to the Davidic-Christology trajectory (this is the first occurrence of מָשִׁיחַ as title-of-king-Messiah in the OT — chronologically prophetic of Davidic Anointed; rendered via the same `ทรงเจิม` verb-phrase as the 6× Saul-anointed inclusio at 24:7/24:11/26:9/26:11/26:16/26:23). ✓

**Magnificat (Luke 1:46–55) NT cross-corpus echo — NOT marked at Layer-2 in 1 Sam 2.** No notes-field cross-reference at 2:1, 2:7, or 2:8 explicitly cites the Magnificat parallel. The shipped `notes` field at chapter 2 (1 entry — chapter-close summary) does mention Magnificat at the close, but the per-verse cross-corpus annotation is sparse.

**Recommend Layer-2 enhancement.** Add cross-reference at 2:7 ("ทรงทำให้ยากจนและทรงทำให้รวย ทรงทำให้ต่ำและทรงยก" ↔ Luke 1:52 "καθεῖλεν δυνάστας ἀπὸ θρόνων καὶ ὕψωσεν ταπεινούς"), at 2:8 (↔ Luke 1:52–53), and at 2:10 (↔ Luke 1:69 "κέρας σωτηρίας ἐν οἴκῳ Δαυίδ" — the explicit horn-of-salvation cross-reference at Zechariah's Benedictus). Forward-protects:
- Mary's Magnificat Greek text borrows the 2:1+8 structure
- Zechariah's Benedictus (Luke 1:67–79) borrows the 2:10 "horn" image
- The patristic-tradition rabbinic-Hannah-as-prototype reading

**STABLE-with-Layer-2-recommendation.** Not blocking the v1 tag.

---

## 7. Hannah's Song ↔ Magnificat NT cross-corpus thread — **STABLE; recommend new doc**

Building on §6: the Hannah-Magnificat cross-corpus thread is **not** documented in `docs/translator_decisions/`. This is the OT-prototype-for-NT theme analogous to the Genesis 22 / Lev 16 / Jer 31 / Isa 53 cross-corpus threads that drive NT Christology.

**Recommend new doc** `docs/translator_decisions/hannah_song_magnificat_thread_2026-05.md`:
1. Lock the OT-prototype reading: Hannah's Song is the literary template for Mary's Magnificat (verified via shared lexical thread: גָּדַל ↔ μεγαλύνει; הִתְפַּלֵּל ↔ προσευχή; "ทรงยกผู้ยากจน" ↔ "ταπεινούς"; "horn" ↔ "κέρας").
2. Cross-reference Zechariah's Benedictus (Luke 1:68–79) for the "horn of salvation" thread.
3. Lock the *anawim*-template reading of Hannah (cf. §6 humble-Adonai register) → forward-protects Ruth, the Hannah-template in the Psalms (Ps 113 hapax הָקֵם מֵעָפָר דָּל ↔ 1 Sam 2:8), and the Magnificat OT-substrate.
4. Cross-reference 2:35 ("a faithful priest … walking before my anointed forever") as the proto-Davidic-Messianic priestly thread that closes at 1 Sam 26:23 + 2 Sam 7:13–16 + Heb 5–7 (forward-protection: 2 Sam + Heb high-priest Christology).

**Priority: MEDIUM** — Magnificat is already shipped (Luke 1); the doc closes a loop rather than gating a forward shipment.

---

## 8. חַי־יְהוָה oath formula — **LOCKED**

The "as YHWH lives" oath occurs **11×** in 1 Samuel — concentrated in the David-cycle (Jonathan, David, Saul, Abishai, and Achish all swear). Survey uniformly renders **"องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่"** ✓:

| Verse | Speaker → Addressee | Thai surface |
|---|---|---|
| 14:39 | Saul (oath about Jonathan-honey) | "องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่" |
| 14:45 | the people (counter-oath to save Jonathan) | same |
| 19:6 | Saul (oath to Jonathan re: David) | same |
| 20:3 | David (compound: "as YHWH lives and your soul lives") | "**องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ และจิตวิญญาณของท่านทรงพระชนม์อยู่**" |
| 20:21 | Jonathan (compound oath formula) | same |
| 25:26 | Abigail to David (compound, parallel: "as YHWH lives and your soul lives") | same |
| 25:34 | David to Abigail | same |
| 26:10 | David to Abishai (about YHWH striking Saul) | "องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่" |
| 26:16 | David to Abner | same |
| 28:10 | Saul to the witch of Endor | same |
| 29:6 | Achish to David ("as YHWH lives, you are upright") | same |

**Compound forms** (חַי־יְהוָה וְחֵי נַפְשְׁךָ — "as YHWH lives and your soul lives") at 20:3, 25:26 uniformly extended to "**ทรงพระชนม์อยู่**" for both clauses — the same verb cleanly applied to both the divine "live" and the human "live," which preserves the Hebrew chiastic oath structure.

Compare JDG 8:19 lock (Gideon to Zebah + Zalmunna) — matches.

**LOCKED** ✓ per `hebrew_oath_formulas_2026-05.md`. 1 Samuel is the densest oath-formula book in the corpus to date.

---

## 9. מָשִׁיחַ יְהוָה ("YHWH's anointed") inclusio — **LOCKED**

The "do not stretch out your hand against YHWH's anointed" formula at 24:6/24:10 + 26:9/26:11/26:16/26:23 is one of 1 Samuel's signature literary architectures — the centerpiece of the David-Saul-cave + David-Saul-spear narrative pair. **All 6 occurrences uniformly render** the מָשִׁיחַ יְהוָה lemma as **"ผู้ที่องค์พระผู้เป็นเจ้าทรงเจิม"**.

Other מָשִׁיחַ occurrences in 1SA (non-formula):
- **2:10** קֶרֶן מְשִׁיחוֹ → "**เขาของผู้ที่พระองค์ทรงเจิมไว้**" (Hannah's Song — first occurrence; see §6)
- **2:35** בֵיתִי נֶאֱמָן … מְשִׁיחִי → "**ข้างหน้าผู้ที่เราเจิมไว้ตลอดไป**" (priestly-Messianic thread)
- **9:16, 10:1, 12:3, 12:5, 16:3, 16:6** — Saul/David-anointing-narrative — all rendered with `ทรงเจิม` / `เจิม` verb-phrase pattern ✓

**Editorial significance.** The Davidic-Christology thread (מָשִׁיחַ → χριστός → Christ) is fully traceable through 1 Sam 2:10 (Hannah) → 2:35 (priestly) → 16:13 (David anointed) → 24:6+ / 26:9+ (David's reverence-for-the-anointed inclusio). The uniform `ทรงเจิม` surface preserves the thread for the NT reader.

**LOCKED** ✓.

---

## 10. Witch of Endor + necromancy vocabulary (1 Sam 28) — **STABLE; recommend new doc**

1 Sam 28:3–25 is the OT's most theologically charged necromancy narrative. The Thai translation handles it with restraint + descriptive paraphrase (not transliteration) for the Hebrew אֹב + יִדְּעוֹנִי technical-necromancy lexicon:

| Verse | Hebrew | Thai surface |
|---|---|---|
| 28:3 | הָאֹבוֹת וְהַיִּדְּעֹנִים | **"ผู้ที่ติดต่อกับวิญญาณและผู้ที่รู้สิ่งล้ำลับ"** |
| 28:7 | אֵשֶׁת בַּעֲלַת־אוֹב | **"ผู้หญิงที่เป็นแม่หมอ"** |
| 28:8 | קָסֳמִי־נָא לִי בָּאוֹב וְהַעֲלִי לִי | "ขอจงเรียกวิญญาณให้ข้า และจงนำผู้ที่ข้าจะระบุแก่เจ้าขึ้นมาให้ข้า" |
| 28:9 | אֶת־הָאֹבוֹת וְאֶת־הַיִּדְּעֹנִי | "ผู้ที่ติดต่อกับวิญญาณและผู้ที่รู้สิ่งล้ำลับ" (uniform with 28:3) |
| 28:13 | אֱלֹהִים רָאִיתִי עֹלִים מִן־הָאָרֶץ | **"ข้าเห็นพระเจ้า ขึ้นมาจากแผ่นดิน"** (preserves the Hebrew אֱלֹהִים-as-divine-being ambiguity) |
| 28:14 | אִישׁ זָקֵן עֹלֶה וְהוּא עֹטֶה מְעִיל | "ชายแก่กำลังขึ้นมา และเขาสวมเสื้อคลุม" |
| 28:15 | וֵאלֹהִים סָר מֵעָלַי | "พระเจ้าทรงจากข้าไป" |
| 28:16 | וַיהוָה סָר מֵעָלֶיךָ | "องค์พระผู้เป็นเจ้าทรงจากเจ้าไป" |
| 28:18 | (catch-up reference to Amalek herem) | "ไม่ได้ทำตามความโกรธอันร้อนแรงของพระองค์ต่อชาวอามาเลก" |
| 28:19 | וּמָחָר אַתָּה וּבָנֶיךָ עִמִּי | "พรุ่งนี้ เจ้าและบุตรของเจ้าจะอยู่กับข้า" |

**The 28:13 אֱלֹהִים rendering is the load-bearing decision.** The Hebrew uses plural אֱלֹהִים with a plural participle עֹלִים (literally "I see gods ascending from the earth") — a grammatical curiosity that all major translations wrestle with (NRSV "I see a divine being"; ESV "I see a god"; NIV "I see a ghostly figure"). The 1SA Thai preserves the divine-register `พระเจ้า` (consistent with the doc-locked OT אֱלֹהִים → พระเจ้า convention) BUT flattens the plural participle עֹלִים to singular `ขึ้นมา`. Defensible but loses the Hebrew literary curiosity.

**Editorial assessment.** Translation is uniformly compliant — no transliteration drift, no theological intrusion, no register slip. The descriptive paraphrase ("ผู้ที่ติดต่อกับวิญญาณ / ผู้ที่รู้สิ่งล้ำลับ") preserves the prohibition's force without exoticizing the Hebrew technical vocabulary. The אֱלֹהִים at 28:13 is rendered with the standard `พระเจ้า` (acceptable but flattened).

**Recommend STABLE; lift to new doc** `docs/translator_decisions/necromancy_and_spiritism_vocabulary_2026-05.md`:
1. Lock the descriptive-paraphrase Thai surface for אֹב + יִדְּעֹנִי technical-necromancy lemmas
2. Forward-protect:
    - **Lev 19:31, 20:6, 20:27** (the Mosaic prohibition — retroactive; the 1 Sam text presupposes Lev as the legal background, "Saul had banished the mediums," 28:3)
    - **Deut 18:9–14** (the prohibition reaffirmed)
    - **2 Kgs 21:6, 23:24** (Manasseh's revival + Josiah's purge — same lemma cluster)
    - **Isa 8:19, 19:3, 29:4** (prophetic polemic against necromancy)
    - **1 Chr 10:13** (the Chronicler's death-notice for Saul explicitly cites the witch-of-Endor consultation as the proximate cause)
3. Lock the 28:13 אֱלֹהִים-rendering choice (preserve `พระเจ้า` for Hebrew-divine-register fidelity; document the plural-participle flattening as an editorial choice rather than an oversight)
4. Cross-reference NT: Acts 16:16–18 (the πνεῦμα πύθωνος Pythian-slave-girl exorcism — Greek-pagan necromancy/divination boundary)

**Priority: HIGH (forward-protects 2 Kings + Isaiah + Chronicles).** Not blocking the v1 tag.

---

## 11. cherem at 1 Sam 15 (Amalek) — **LOCKED**

The 1 Sam 15 Saul-Amalek narrative is the OT's third-densest ḥerem cluster (after Joshua 6–11 + Deut 7+20). All 7 חרם-root tokens in 1 Sam 15 render uniformly via the locked **"ทุ่มถวาย…เพื่อทำลาย"** family with **"เฮเรม"** transliteration anchored at first + re-anchored at 15:18:

| Verse | Hebrew | Thai surface |
|---|---|---|
| 15:3 | וְהַחֲרַמְתֶּם | "พวกเจ้าจงทุ่มถวายทุกสิ่งที่เป็นของเขาเพื่อทำลาย — **เป็นการเฮเรม**" |
| 15:8 | הֶחֱרִים לְפִי־חָרֶב | "ทุ่มถวายประชาชนทั้งหมดเพื่อทำลายด้วยคมดาบ" |
| 15:9 | וְלֹא אָבוּ הַחֲרִימָם … הֶחֱרִימוּ | "ไม่ยอมทุ่มถวายเพื่อทำลาย … พวกเขาก็ทุ่มถวายเพื่อทำลาย" |
| 15:15 | הֶחֱרַמְנוּ | "พวกเราได้ทุ่มถวายเพื่อทำลาย" |
| 15:18 | וְהַחֲרַמְתָּה | "จงไปและ**ทุ่มถวายเฮเรมต่อ**" (anchor re-introduced) |
| 15:20 | הֶחֱרַמְתִּי | "ทุ่มถวายชาวอามาเลกเพื่อทำลาย" |
| 15:21 | רֵאשִׁית הַחֵרֶם | "สิ่งที่ดีที่สุดของสิ่งที่ควรทุ่มถวายเพื่อทำลาย" |
| 28:18 | (catch-up; no חרם token) | "ไม่ได้ทำตามความโกรธอันร้อนแรงของพระองค์ต่อชาวอามาเลก" |

Matches `ot_warfare_ethics_2026-05.md` JOS/DEU lock and JDG-audit §"warfare ethics" carry. Uniform.

**1 Sam 15:22** ("to obey is better than sacrifice") — the load-bearing prophetic-aphorism — rendered: "**การฟังย่อมดีกว่าเครื่องบูชา และการใส่ใจดีกว่าไขมันของแกะตัวผู้**" — preserves both clauses cleanly. Recommend Layer-2 NT cross-reference at 15:22 to Hos 6:6 ("I desire mercy, not sacrifice"), Matt 9:13 + 12:7 (Jesus's twofold citation of Hos 6:6), Mark 12:33 (scribe's recognition that loving God + neighbor is "more than burnt offerings"), and 1 Cor 13:3 (love-supreme-over-sacrifice). Not currently in the 1 Sam 15:22 notes field.

**LOCKED** ✓. **Recommend Layer-2 enhancement at 15:22** (cross-corpus NT prophetic-aphorism thread).

---

## 12. Pagan deities + Philistine context — **REVIEW (3-form Ashtaroth spelling + Dagon-as-พระเจ้า at 5:7)**

**Dagon proper noun.** 11 occurrences across ch 5 (5:2, 5:3 ×2, 5:4 ×2, 5:5, 5:7, 16:23 [false hit; cross-ref check]). Uniformly **"ดาโกน"**. ✓

**Dagon "พระเจ้าของพวกเรา" at 5:7 — DRIFT.** The Philistines of Ashdod refer to Dagon as **"ดาโกนพระเจ้าของพวกเรา"** (וְעַל דָּגוֹן אֱלֹהֵינוּ). This applies the supreme divine title `พระเจ้า` to a literal pagan deity in pagan speech — **explicitly forbidden** by:
- `pagan_deities_2026-04.md` Rule 1 ("Literal pagan deities, in any voice, never receive the divine register reserved for the biblical God")
- `ot_polytheistic_register_2026-05.md` §1.3 ("Calling foreign deities **พระเจ้า** ("God"). That term is reserved for the personal God of Israel + Christian Trinitarian usage. Foreign deities = พระ / พระทั้งหลาย / เทพ")

**Recommended fix:** 5:7 → **"ดาโกนเทพเจ้าของพวกเรา"** (per pagan-deity Rule 1 register family). Compare Acts 12:22 Herod (`เทพเจ้า`), Acts 14:11 Lystra ("เหล่าทวยเทพ"). Cost: 1 surgical edit.

**Ashtaroth (עַשְׁתָּרוֹת / עַשְׁתָּרֹת) — 3-form spelling drift:**

| Ref | Hebrew | Thai |
|---|---|---|
| 7:3 | הָעַשְׁתָּרוֹת | "**พระอัชโทเรท**" |
| 7:4 | הָעַשְׁתָּרֹת | "**พระอัชโทเรท**" (matches 7:3) |
| 12:10 | הָעַשְׁתָּרוֹת | "**พระอาเชโทรททั้งหลาย**" (DRIFT) |
| 31:10 | בֵּית עַשְׁתָּרוֹת | "**วิหารของเทพีอัชทาโรท**" (DRIFT) |

Three different transliterations of the same lemma: **อัชโทเรท** (chs 7) / **อาเชโทรท** (12) / **อัชทาโรท** (31). Cross-corpus check: JDG-audit §15 reports JDG 2:13 + 10:6 use **"บรรดาพระอัชเทเรท"** — a FOURTH transliteration (อัชเทเรท). So the corpus now has 4 spellings for the same lemma across JDG + 1SA. **Normalize.**

**The 31:10 form is also register-divergent.** It uses `เทพี` (correctly pagan-deity-register per `pagan_deities_2026-04.md`) — but the prior chs 7 + 12 use `พระ` (matching JDG-precedent). The JDG-audit §15 row for `pagan_deities_2026-04.md` marks JDG-Baal/Ashtaroth (`พระบาอัล / บรรดาพระอัชเทเรท`) as LOCKED + compliant, treating the `พระ`-prefix as the OT-corpus convention (distinct from the NT-Acts `เทพเจ้า` register). So `พระอัชโทเรท / พระอัชเทเรท` is corpus-accepted; only the spelling-drift is the real issue.

**REVIEW recommendation:**
- **Normalize spelling** to one of {อัชเทเรท, อัชโทเรท, อาเชโทรท, อัชทาโรท}. JDG-audit precedent favors **อัชเทเรท** (used 2× across JDG); recommend extending that as the corpus surface.
- **Either:**
  - **(a) Keep the OT-precedent `พระ`-prefix register** (normalize 31:10 to `พระอัชเทเรท`)
  - **(b) Shift to the pagan_deities_2026-04 Rule 1 `เทพี`-register** (normalize 7:3+4, 12:10 to `เทพีอัชเทเรท`). This would also require revisiting the JDG-audit §15 LOCKED status for `พระบาอัล / บรรดาพระอัชเทเรท` — i.e., extending the §"7:3+4" register choice retroactively across JDG. **Higher cost.**

**Recommend (a):** keep the OT-precedent `พระ`-register (matches JDG); normalize the 4-form spelling drift to `อัชเทเรท`. Cost: ~4 verse-edits across 1SA + glossary note. **Severity: MEDIUM** — first cross-book proper-noun spelling drift surfaced in OT corpus.

**Baalim (הַבְּעָלִים):**
- 7:4 → "**บาอัลทั้งหลาย**" (no `พระ` prefix on the proper noun)
- 12:10 → "**พระบาอัลทั้งหลาย**" (with `พระ` prefix — matches JDG)

Minor internal-1SA drift on the `พระ`-prefix at 7:4. Recommend normalize to `พระบาอัลทั้งหลาย` per JDG precedent.

---

## 13. Saul-as-king register + the מָשִׁיחַ-thread — **LOCKED**

**Royal ทรง-register applied to King Saul.** The narrator's voice uses `ทรง` for Saul's kingly-office actions per `honorifics_non_divine_authorities_2026-04.md` (Mark 6:14 Herod model):

| Ref | Thai surface |
|---|---|
| 12:2 | "**กษัตริย์ทรงเดิน**" (Samuel referring to Saul-as-king) |
| 17:55 | "**องค์กษัตริย์ทรงพระชนม์อยู่**" (Abner's oath formula) |
| 18:25 | "**กษัตริย์ไม่ทรงประสงค์สินสอด**" (narrator on Saul) |
| 20:25 | "**กษัตริย์ทรงนั่งที่ที่นั่งของพระองค์**" |
| 21:3 (Eng 21:2) | "**กษัตริย์ทรงสั่งให้ข้าทำเรื่อง**" |

**Anticipatory ทรง for David at 25:28.** Abigail's prophetic speech to David ("the LORD will certainly make my lord a sure house"): **"เจ้านายของข้าทรงสู้สงคราม"** — applies ทรง to David BEFORE his coronation (1 Sam 25 precedes 2 Sam 5). The anticipatory royal register is theologically loaded (Abigail recognizes David's pre-anointed-but-yet-to-be-enthroned kingship); a single literary highlight, not a drift. Matches the `honorifics_non_divine_authorities_2026-04.md` "public royal role → ทรง" principle.

**LOCKED** ✓. The 6× "ผู้ที่องค์พระผู้เป็นเจ้าทรงเจิม" inclusio at 24:6+ / 26:9+ (see §9) is the densest single-book deployment of the מָשִׁיחַ-formula and the most-load-bearing forward-protection of the Davidic-Christology thread.

---

## 14. "until this day" leitwort — **LOCKED**

Survey of עַד הַיּוֹם הַזֶּה in 1 Samuel — 8 occurrences:

| Verse | Thai surface |
|---|---|
| 5:5 | **"จนถึงวันนี้"** |
| 6:18 | "จนถึงวันนี้" |
| 8:8 | "จนถึงวันนี้" |
| 12:2 | "จนถึงวันนี้" |
| 27:6 | "จนถึงวันนี้" |
| 29:3 | "จนถึงวันนี้" |
| 29:6 | "จนถึงวันนี้" |
| 30:25 | "จนถึงวันนี้" |

**All 8 occurrences uniformly render `จนถึงวันนี้`.**

**Cross-corpus check vs JDG-audit §14:** JDG used 6× **"จนถึงทุกวันนี้"** (with `ทุก-` intensifier) + 1 drift at 19:30 ("จนถึงวันนี้" without `ทุก-`). The JDG-audit §14 REVIEW recommended normalize 19:30 to `จนถึงทุกวันนี้`. **1 Samuel uniformly ships the bare-form `จนถึงวันนี้` — i.e., the JDG 19:30 form, NOT the JDG-majority `จนถึงทุกวันนี้` form.**

**Cross-corpus disposition.** Two paths:
- **(a)** JDG-majority is canonical (`จนถึงทุกวันนี้`); 1SA universally drifted. Fix: 8 surgical edits in 1SA + carry the JDG-19:30 normalization.
- **(b)** 1SA-uniform is canonical (`จนถึงวันนี้`); JDG-majority drifted. Fix: 6 surgical edits in JDG + the JDG-19:30 form is incidentally correct.

The Hebrew has no signal to prefer one over the other (עַד הַיּוֹם הַזֶּה is identical at every occurrence across the corpus). Path (a) preserves more intensification ("**every** day until now"); path (b) is leaner.

**Cross-reference to corpus-wide `leitwort_handling_policy_2026-05.md`:** the doc does not currently lock a specific Thai surface for the עַד הַיּוֹם הַזֶּה leitwort. Recommend doc amendment to lock the canonical surface.

**REVIEW.** Internal 1SA uniformity ✓; cross-book corpus normalization is the open question. **Severity: LOW.** Recommend resolve at the same time as the JDG-audit §14 normalization. Not blocking the 1SA v1 tag in isolation, but the cross-book decision should land first.

---

## 15. Sacrificial vocabulary — **REVIEW (minor drift: מִנְחָה collapse + שְׁלָמִים 2 surfaces)**

Survey of OT sacrificial lemmas across 1 Samuel:

| Hebrew | Thai (locked, per `sacrificial_vocabulary_2026-05.md`) | 1SA surface | Verses | Drift? |
|---|---|---|---|---|
| זֶבַח / זָבַח (sacrifice / to sacrifice) | "**บูชา / เครื่องบูชา / ถวายบูชา**" | uniform "ถวายบูชา / บูชา / เครื่องบูชา" | 1:3, 1:4, 1:21, 2:13, 2:15, 2:29, 15:15, 16:2, 16:3, 16:5 | ✓ uniform |
| עוֹלָה (burnt offering) | "**เครื่องเผาบูชา**" | uniform "เครื่องเผาบูชา" + "**เครื่องเผาบูชาทั้งตัว**" (for עוֹלָה כָּלִיל at 7:9) | 6:14, 7:9, 7:10, 10:8, 13:9, 13:10, 13:12, 15:22 | ✓ uniform |
| מִנְחָה (grain/tribute offering) | "**เครื่องธัญบูชา**" (or distinct surface from זֶבַח) | **"เครื่องบูชา"** (same as זֶבַח) | 2:17, 2:29 | ✗ **DRIFT** (collapse) |
| שְׁלָמִים (peace/fellowship offering) | "**เครื่องสันติบูชา**" or "**เครื่องบูชาสันติสุข**" | **two forms**: "เครื่องบูชาแห่งสันติสุข" (10:8) vs "เครื่องสันติบูชา" (13:9) | 10:8, 13:9 | ✗ **DRIFT** (2 surfaces) |
| אָשָׁם (guilt/trespass offering) | "**เครื่องบูชาไถ่ความผิด**" | uniform | 6:3, 6:4, 6:8, 6:17 | ✓ uniform |

**Two drift sub-items:**

1. **מִנְחָה collapses to "เครื่องบูชา" at 2:17, 2:29** — losing the lexical distinction from זֶבַח. The Hebrew מִנְחָה specifically denotes grain/cereal offering (or tribute-gift more broadly); the corpus-canonical surface per Lev/Num practice is **"เครื่องธัญบูชา"** (grain-bushel offering) or at minimum a distinct surface. The 2:17 reference is specifically about Eli's sons' contempt for "the offering of YHWH" (מִנְחַת יְהוָה) — flattening to `เครื่องบูชา` loses the cult-specific charge.
2. **שְׁלָמִים has two surfaces in 1 Samuel.** 10:8 (Samuel's instruction at Gilgal) → `เครื่องบูชาแห่งสันติสุข`; 13:9 (Saul's unauthorized offering) → `เครื่องสันติบูชา`. Hebrew is identical; Thai differs. Recommend normalize to `เครื่องสันติบูชา` per OT-corpus precedent (matches the locked Lev/Num surface).

**REVIEW.** Both are LOW-severity surgical drifts. **Recommend:**
- Normalize 2:17 + 2:29 מִנְחָה → "เครื่องธัญบูชา"
- Normalize 10:8 שְׁלָמִים → "เครื่องสันติบูชา"

Cost: 4 surgical verse-edits + glossary note. **Severity: LOW.**

---

## 16. נחם (divine relenting) at 15:11, 15:29, 15:35 — **LOCKED**

The 1 Sam 15 chapter's three-fold use of נחם is the OT's most theologically charged divine-relenting cluster. The principled distinction between anthropopathic-regret and cognitive-change-mind is preserved:

| Verse | Hebrew | Thai surface | Sense |
|---|---|---|---|
| **15:11** | נִחַמְתִּי כִּי־הִמְלַכְתִּי אֶת־שָׁאוּל | **"เราเสียพระทัยที่ได้ตั้งซาอูลให้เป็นกษัตริย์"** | anthropopathic divine sorrow (ทรงเสียพระทัย) |
| **15:29** | וְלֹא יִנָּחֵם כִּי לֹא אָדָם הוּא לְהִנָּחֵם | **"ไม่ทรงเปลี่ยนพระทัย เพราะพระองค์ไม่ใช่มนุษย์ที่จะเปลี่ยนพระทัย"** | cognitive reversal denied (ทรงเปลี่ยนพระทัย) |
| **15:35** | וַיהוָה נִחָם כִּי־הִמְלִיךְ אֶת־שָׁאוּל | **"องค์พระผู้เป็นเจ้าทรงเสียพระทัยที่ได้ตั้งซาอูลให้เป็นกษัตริย์"** | matches 15:11 |

The split — anthropopathic-regret (`ทรงเสียพระทัย` for נחם at 15:11 + 15:35) vs cognitive-change-mind (`ทรงเปลี่ยนพระทัย` for נחם at 15:29 — the explicit divine self-disclosure that YHWH is not the kind of being who can have his mind changed by external pressure) — matches `nicham_divine_relenting_2026-05.md` lock exactly. The verses' `key_decisions` explicitly capture both Hebrew forms + the apparent contradiction's resolution.

This is the corpus's load-bearing test case for the divine-relenting doc; it ships cleanly.

**LOCKED** ✓. Forward-protects 2 Sam 24:16 (the angel-of-pestilence נחם) + Jer 18:8+10, 26:3+13+19 + Amos 7:3+6 + Jon 3:9–10 + 4:2 (the Jonah-Nineveh נחם — the gentile-extension of the principle).

---

## 17. MT/LXX inclusion-variant gap — **DECIDE before tagging**

`audit_inclusion_variants.py --book 1samuel --strict` reports **0 candidates**. But the script's heuristic does NOT catch the major 1 Samuel MT/LXX variants, which are well-known and significant:

| Variant | Description | Currently documented in `output/textual_variants/1samuel_NN.json`? |
|---|---|---|
| **1 Sam 10:27b → 11:1** | 4QSamᵃ (Qumran scroll) preserves a longer reading naming Nahash's two-year campaign against Reuben + Gad before besieging Jabesh-Gilead. The shorter MT reading is followed by 1SA shipped text. | ❌ Not documented |
| **1 Sam 11:1** | The same 4QSamᵃ plus is also picked up by the NRSV + some modern translations. | ❌ Not documented |
| **1 Sam 13:1** | The corrupt regnal-formula: MT reads "Saul was [missing] years old when he became king, and reigned [missing-the-number]-two years over Israel." The shipped 1SA text reflects the MT corruption. | ❌ Not documented |
| **1 Sam 14:41** | MT has the short reading "Give the truth" (הָבָה תָמִים). LXX has a major expansion via Urim/Thummim ("If this iniquity be in me or in Jonathan my son, O LORD God of Israel, give Urim; but if you say it is in your people Israel, give Thummim"). The expansion clarifies the Hebrew obscurity. | ❌ Not documented |
| **1 Sam 17:12–31** + **17:55–18:5** | **The famous "minus" sections.** LXX-B (Vaticanus) omits these 39 verses of David-Goliath narrative, producing a substantially shorter David-introduction. The shipped 1SA follows MT (longer reading) at 17:12–31 + 17:55–18:5. | ❌ Not documented (the 17:4 Goliath-height MT-vs-LXX variant IS documented in the chapter footnote, but the major 39-verse minus is not flagged) |
| **1 Sam 13:1** age | Same as above. | — |

**Mechanism check.** Reviewed all 31 files in `output/textual_variants/1samuel_NN.json`. **29/31 are `type: "tetragrammaton_convention_first_occurrence"`** (the Tier-2 YHWH footnote). **2/31 are `type: "chapter_overview_note"`** (chs 27 + 31, both YHWH-absent). **Zero entries of `type: "inclusion_variant_minus"` or `"inclusion_variant_plus"` exist** in 1 Samuel's textual_variants files.

**Editorial assessment.** Per `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md`, every MT-vs-LXX/Qumran inclusion-variant with corpus-significance (Tier 1 = phrase brackets; Tier 2 = chapter-footer file; Tier 3 = ⟦double brackets⟧) should be explicitly dispositioned. 1 Samuel ships with these decisions silent — the maintainer followed MT throughout, but the choice is not visible to readers or future editors.

This is the **first major OT inclusion-variant cluster** the corpus has encountered (Genesis–Joshua have minor variants but no major-shortening like 1 Sam 17 LXX-B). The decision to follow MT is defensible (and matches `ot_canon_and_text_base_2026-05.md` MT-base policy), but the **transparency mechanism** (Tier-2 footers explaining the decision) was not deployed.

**DECIDE before tagging — recommended path:**

Write Tier-2 chapter-footer entries in `output/textual_variants/1samuel_NN.json` for the four major variants:
1. **1 Sam 11 chapter footer** — document the 4QSamᵃ 10:27b+ plus + the maintainer's MT-base decision
2. **1 Sam 13 chapter footer** — document the 13:1 regnal-formula corruption + the maintainer's preservation of the MT-corrupt form (vs the NRSV interpolation "[thirty]" + "[forty]-two")
3. **1 Sam 14 chapter footer** — document the 14:41 LXX Urim/Thummim expansion + maintainer's MT-base decision (and possibly Layer-2 note on the obscurity of the MT short reading)
4. **1 Sam 17 chapter footer** — document the LXX-B 17:12–31 + 17:55–18:5 minus + maintainer's MT-base decision (the height-of-Goliath 17:4 note already exists; this is an expansion)

**Cost:** 4 chapter-footer JSON entries (~30 minutes per entry, including scholarly summary). No translation surface edits — text is followed correctly per MT-base policy; the gap is the missing Tier-2 transparency layer.

**Severity: HIGH.** First major OT inclusion-variant cluster + textual-variants Tier-2 infrastructure forward-test. Sets the precedent for 2 Sam (4QSamᵃ + LXX divergences), Kings (LXX Old Greek), Jeremiah (the famous MT-vs-LXX shorter recension), and Daniel (Greek vs Aramaic plus-narratives). **Blocks `book-1samuel-v1` tag** without resolution.

---

## 18. Hebrew oath compound formulas (non-`חַי־יְהוָה`) — **LOCKED**

Beyond the `חַי־יְהוָה` survey (§8), 1 Sam contains additional Hebrew oath constructions surveyed for compliance with `hebrew_oath_formulas_2026-05.md`:

| Type | Hebrew | Verses | Thai surface |
|---|---|---|---|
| "May God do so to me and more also if …" | כֹּה־יַעֲשֶׂה־לִּי אֱלֹהִים וְכֹה יוֹסִיף כִּי… | 3:17 (Eli to Samuel), 14:44 (Saul re Jonathan), 20:13 (Jonathan to David), 25:22 (David re Nabal — note: MT "the enemies of David" emendation here for "David" — preserved + flagged in key_decisions ✓), 28:10 (Saul's oath to the witch) | "ขอพระเจ้าทรงกระทำเช่นนั้น…" uniform |
| "By the life of your soul" | חֵי נַפְשְׁךָ | 1:26 (Hannah to Eli), 17:55 (Abner) | "จิตวิญญาณของท่านทรงพระชนม์อยู่" (matches Job + JOS compound family) ✓ |
| "By God" (אֱלֹהִים swear-by) | — | (no standalone ב-אֱלֹהִים oaths in 1SA) | n/a |

**LOCKED** ✓. The 25:22 emendation (MT reads "the enemies of David"; many texts emend to "David" alone) is preserved as MT-reads + key_decisions note — exemplary handling.

---

## 19. Annotation-architecture pattern — **REVIEW (`thai_summary` undercoverage in chs 16+)**

Per-chapter annotation density (verses / `key_decisions` non-empty / `thai_summary` non-empty / `notes` non-empty):

| ch | verses | KD | summary | notes | summary % |
|---|---|---|---|---|---|
| 1 | 28 | 26 | 28 | 1 | 100% |
| 2 | 36 | 33 | 36 | 1 | 100% |
| 3 | 21 | 19 | 21 | 1 | 100% |
| 4 | 22 | 17 | 22 | 1 | 100% |
| 5 | 12 | 12 | 12 | 1 | 100% |
| 6 | 21 | 18 | 21 | 1 | 100% |
| 7 | 17 | 14 | 17 | 1 | 100% |
| 8 | 22 | 17 | 22 | 1 | 100% |
| 9 | 27 | 18 | 27 | 1 | 100% |
| 10 | 27 | 21 | 27 | 1 | 100% |
| 11 | 15 | 11 | 15 | 1 | 100% |
| 12 | 25 | 25 | 23 | 2 | 92% |
| 13 | 23 | 23 | 15 | 3 | 65% |
| 14 | 52 | 42 | 26 | 2 | 50% |
| 15 | 35 | 35 | 18 | 2 | 51% |
| **16** | **23** | **20** | **9** | **1** | **39%** |
| **17** | **58** | **17** | **16** | **4** | **28%** |
| **18** | **30** | **17** | **14** | **2** | **47%** |
| **19** | **24** | **11** | **11** | **1** | **46%** |
| 20 | 42 | 18 | 13 | 2 | 31% |
| 21 | 16 | 12 | 9 | 4 | 56% |
| 22 | 23 | 15 | 13 | 3 | 57% |
| 23 | 28 | 15 | 16 | 1 | 57% |
| 24 | 23 | 18 | 12 | 5 | 52% |
| 25 | 44 | 19 | 18 | 1 | 41% |
| 26 | 25 | 13 | 11 | 3 | 44% |
| 27 | 12 | 7 | 7 | 3 | 58% |
| 28 | 25 | 15 | 12 | 1 | 48% |
| 29 | 11 | 6 | 5 | 2 | 45% |
| 30 | 31 | 14 | 12 | 2 | 39% |
| 31 | 13 | 9 | 8 | 2 | 62% |

**Observation — sharp inflection at ch 12–13.** Chs 1–11 ship `thai_summary` at 100% verse-coverage. Chs 12 + 13 show first decline. **Chs 16–30 ship `thai_summary` at 28–58% per chapter.** Ch 17 (David-Goliath, 58 verses) is the most-undercovered at 28% (16/58 summarized).

**Mirrors the JDG-audit §16 pattern in REVERSE direction.** JDG 1–18 had notes-heavy / summary-sparse annotation; JDG 19–21 inverted to notes-empty / summary-full at the Gibeah-civil-war sensitive content. **1SA 1–11 ships summary-full** (matches JDG-19-21 sensitive-content pattern); **1SA 16–30 ships summary-sparse** (matches JDG-1-18 narrative-default pattern).

**Editorial assessment — two possibilities:**

(a) **Intentional editorial scaling.** The maintainer may have intentionally front-loaded annotation density in the Hannah/Eli/Samuel/early-Saul narratives (chs 1–11, the book's theological-setting chapters) and tapered as the David-narrative compounded (chs 16–30 are denser narrative-action with less per-verse theological texture). Defensible.

(b) **Drift / different drafting pass.** The architectural shift may simply reflect a different drafting approach across the book.

**REVIEW flag.** Ben to confirm whether the chs 16+ summary-undercoverage is intentional. If yes, document the principle for future books (action-narrative chapters → sparser per-verse summary; theological-foundation chapters → full summary). If unintentional, consider retrofit backfill on chs 16, 17, 20, 25, 26, 30 (the four <50% chapters that carry the most-cited David-narrative pericopes — Goliath, Jonathan-covenant, Nabal-Abigail, Saul-asleep-in-camp, Ziklag).

**Severity: LOW–MEDIUM.** Not blocking the v1 tag.

---

## 20. Inherited corpus locks — **all compliant except where flagged**

| Doc | 1SA evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1, §2, §6. Tetragrammaton uniform (319/320 — 1:1 ratio). Elohim uniform. **EXCEPTION**: humble-Adonai *anawim*-form `นายของข้า` at Hannah 1:15/26 (§6) — defensible but undocumented; recommend amendment. | **LOCKED-with-§6-REVIEW** |
| `spirit_of_yhwh_empowerment_2026-05.md` | **§4 BOOK-WIDE DRIFT.** 12/12 Spirit-occurrences use bare `วิญญาณ`; lock requires `พระวิญญาณ`. צָלַח-class drops the locked `อย่างทรงพลัง` adverbial. | **DECIDE-§4** |
| `ot_register_policy_2026-05.md` | Royal ทรง- for YHWH-volitional throughout ✓; plain register for narrator + character speech ✓; ทรง for King Saul + anticipatory ทรง for David at 25:28 (Abigail's prophetic speech) — matches `honorifics_non_divine_authorities_2026-04.md` Mark-Herod precedent. Compliant. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | §13. ทรง applied to Saul-as-king + Abigail's anticipatory ทรง for David. Compliant. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | חֶסֶד occurs at 1 Sam 20:8, 20:14 (×2), 20:15 (Jonathan-David covenant חֶסֶד thread), 1 Sam 15:6 (Kenites' חֶסֶד to Israel — Saul's protection of them), and 1 Sam 1:18 (Hannah seeks חֵן from Eli — adjacent but not the technical חֶסֶד). All rendered with the doc-locked `ความรักมั่นคง / ความเมตตา / ความกรุณา` family per context. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Narrator-omniscient throughout; royal register for YHWH-volitional + king-office; plain for character speech. Saul's confessional speeches (15:24+30, 24:17, 26:21) — plain register; David's reverence-speeches (24:6+ / 26:9+) — plain. Compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "YHWH's hand" anthropomorphism at 5:6, 5:7, 5:9, 5:11, 6:3, 6:5, 6:9 (ark-judgment-on-Philistines cluster) → "**พระหัตถ์ขององค์พระผู้เป็นเจ้า**" uniform ✓. "YHWH's anger kindled" (חָרָה אַף יְהוָה) at 11:6 (Saul-vs-Nahash empowerment), 28:18 — uniform "**พระพิโรธ**" / "**ทรงพระพิโรธ**" ✓. The "in the eyes of YHWH" anthropomorphism royal vs plain split — see §13. Compliant. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol chains pervasive (ark narrative 4–6; David-Goliath 17; Saul-Endor 28); cognate-accusatives preserved; imperative-of-prohibition forms ✓. Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "Hand of YHWH" (§ above); "anger kindled"; "until this day" leitwort (§14); the "uncircumcised Philistines" idiom at 14:6, 17:26+36, 31:4 → **"คนที่ไม่ได้รับสุหนัต"** uniform ✓. Compliant. | **LOCKED-with-§14-flag** |
| `hebrew_oath_formulas_2026-05.md` | §8 + §18. `חַי־יְהוָה` ×11 + `חֵי נַפְשְׁךָ` ×2 + `כֹּה־יַעֲשֶׂה־לִּי אֱלֹהִים` ×5 all uniform. 1SA is the densest oath-formula book in the corpus. Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | No notable MT/English chapter-boundary divergences (1 Sam 10/11 versification minor only). Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | ~40 proper-noun renderings spot-checked: ฮันนาห์, เอลคานาห์, เอลี, ซามูเอล, ซาอูล, โยนาธาน, ดาวิด, อาบีกายิล, นาบาล, อาคีช, มีคาล, ยูดาห์, ฟิลิสเตีย (153× — matches lock), ฟีเนหัส, โฮฟนี, เปนินนาห์, อาบีชัย, โยอาบ, เจสซี, อับเนอร์, ดาโกน, เอนโดร์, เอนเกดี, มาโอน, คาร์เมล, รามาห์, อามาเลก, โกลิยัท. **EXCEPTION:** Ashtaroth 3-form spelling drift across 7:3/7:4 / 12:10 / 31:10 (§12). **Cross-corpus discontinuity flag:** JDG ships ฟีลิสตี; 1SA ships ฟิลิสเตีย (1SA matches the lock — JDG drift unresolved). | **LOCKED-with-§12-REVIEW** |
| `proper_noun_wordplay_2026-05.md` | 1 Sam 1:28 שָׁאוּל / שָׁאַל wordplay (Samuel = "asked-for") preserved at "**เป็นผู้ที่ถูกขอแก่องค์พระผู้เป็นเจ้า**" + key_decisions note ✓. The "stone of Ebenezer" etymology at 7:12 ("up to here YHWH has helped us") preserved ✓. The Adonai-Bezek / Saul-coronation-Gilgal etymology threads preserved. Compliant. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | **§17 INCLUSION-VARIANT GAP.** 31/31 chapters have textual_variants files (Tier-2 footnote infrastructure deployed ✓), but the major MT/LXX/Qumran variants (1 Sam 10:27b+, 11:1, 13:1, 14:41, 17:12–31 + 17:55–18:5) are NOT documented. Tier-2 transparency layer missing on the first major-shortening cluster the OT-corpus has encountered. | **DECIDE-§17** |
| `ot_warfare_ethics_2026-05.md` | §11. cherem cluster at 1 Sam 15 (Amalek) uniform with `ทุ่มถวาย…เพื่อทำลาย` + `เฮเรม` anchor; 15:22 prophetic-aphorism preserved ✓. Compliant. | **LOCKED** |
| `i_am_yhwh_holiness_formula_2026-05.md` | The "I am YHWH" formula does not occur in 1 Samuel (it's concentrated in Lev + Ezek). The closest analog — Samuel's "the LORD is witness against you" at 12:5 — uses different formula; N/A for the technical "I am YHWH" lemma. | **LOCKED (N/A)** |
| `paqad_visit_attend_2026-05.md` | פָּקַד occurs at 1 Sam 2:21 (YHWH "visited" Hannah → conceived) → **"ทรงเยี่ยมเยียน"** ✓ doc-canonical; 1 Sam 13:15, 14:17, 15:4 (military mustering) → **"นับ / รวบรวม"** ✓ semantic-context-appropriate; 1 Sam 15:2 ("I will punish Amalek for what they did") → **"จะลงโทษ"** ✓ semantic-context shift. Compliant. | **LOCKED** |
| `manah_divine_appointment_2026-05.md` | **Zero מָנָה occurrences in 1SA.** N/A. | **LOCKED (N/A)** |
| `malak_yhwh_2026-05.md` | **§3 — Zero divine-mal'akh in 1 SA**; 22 human-messenger occurrences (mostly `ผู้ส่งสาร`, 5× `ผู้ส่งข่าว` at ch 6/11). 29:9 mal'akh-Elohim simile → `เหมือนทูตของพระเจ้า` ✓. Minor `ผู้ส่งสาร` / `ผู้ส่งข่าว` split flagged §3-REVIEW. | **LOCKED-with-§3-REVIEW** |
| `kapporet_atonement_cover_2026-05.md` | **Zero כַּפֹּרֶת occurrences in 1 SA** (the lemma is concentrated in Lev + Heb). The ark narrative (chs 4–6) refers to the ark as אֲרוֹן הָאֱלֹהִים / אֲרוֹן יְהוָה (without the כַּפֹּרֶת technical-term). N/A. | **LOCKED (N/A)** |
| `kareth_penalty_formula_2026-05.md` | **Zero priestly-Levitical karet occurrences in 1 SA.** N/A. | **LOCKED (N/A)** |
| `hagiasmos_hagiosune_2026-05.md` | קֹדֶשׁ at 1 Sam 7:1 ("they consecrated Eleazar"), 1 Sam 21:5–7 (David + the holy bread / Bread of the Presence — לֶחֶם הַפָּנִים) — uniform with doc-locked surface ✓. The Nazirite-like vow at 1:11 (Hannah's promise re: Samuel — "no razor shall touch his head") → "**ไม่เคยตัดเส้นผมของเขาเลย**" + key_decisions Nazirite-allusion ✓. Compliant. | **LOCKED** |
| `pagan_deities_2026-04.md` | §12. Dagon proper-noun uniform; **EXCEPTION** at 5:7 (Dagon-as-`พระเจ้า`-of-Philistines) — Rule 1 violation. Ashtaroth 3-form spelling drift. Baalim minor `พระ`-prefix split (7:4 vs 12:10). | **REVIEW-§12** |
| `ot_polytheistic_register_2026-05.md` | §12. The 5:7 Dagon-as-`พระเจ้า` violates §1.3 ("foreign deities = พระ / พระทั้งหลาย / เทพ, NOT พระเจ้า"). Else compliant. | **REVIEW-§12** |
| `goel_kinsman_redeemer_2026-05.md` | **Zero kinsman-redeemer גָּאַל occurrences in 1 SA** (the lemma is concentrated in Ruth + Lev 25 + Isa 40+). N/A. | **LOCKED (N/A)** |
| `leitwort_handling_policy_2026-05.md` | §14. "until this day" leitwort uniform within 1SA (`จนถึงวันนี้` ×8) — but cross-book inconsistency vs JDG's `จนถึงทุกวันนี้` majority. Cross-book normalization decision pending. | **LOCKED-with-§14-cross-book-REVIEW** |
| `divine_object_praise_verbs_2026-04.md` | Limited 1SA exposure: 2:1 "my heart exults in YHWH" → **"หัวใจของข้ายินดีในองค์พระผู้เป็นเจ้า"** ✓; 2:2 etc. Hannah's Song. Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | `audit_inclusion_variants.py --book 1samuel --strict` reports 0 candidates — but the script's heuristic misses the major 1 SAM-side variants (§17). Tier-2 footer infrastructure deployed (31/31 chapters) but underutilized for the actual variant cluster. | **DECIDE-§17** |
| `nicham_divine_relenting_2026-05.md` | §16. 1 Sam 15:11, 15:29, 15:35 — clean two-tier distinction. Doc-locked anchor (the densest 3-occurrence cluster in the OT corpus). | **LOCKED** |
| `uncover_nakedness_euphemism_2026-05.md` | **Zero technical "uncover nakedness" Leviticus-19 formula occurrences in 1 SA.** Saul's stripping at 19:24 uses a different idiom (פָּשַׁט "stripped off" — narrative-physical, not the Leviticus-incest legal-euphemism). N/A. | **LOCKED (N/A)** |
| `shared_names_normalization_2026-05.md` | Tribal names compliant (Judah, Benjamin, Ephraim, Manasseh, Naphtali, Reuben, Levi, Issachar, Zebulun, Dan, Gad, Asher, Simeon — all match prior locks). Compliant. | **LOCKED** |
| `sacrificial_vocabulary_2026-05.md` | §15. Drift on מִנְחָה (collapse to `เครื่องบูชา` at 2:17, 2:29) + שְׁלָמִים 2-surface drift (`เครื่องบูชาแห่งสันติสุข` 10:8 vs `เครื่องสันติบูชา` 13:9). Else uniform. | **REVIEW-§15** |
| `aramaic_transliterations_2026-04.md` | N/A — pre-Aramaic Hebrew narrative. | **LOCKED (N/A)** |

---

## 21. NT cross-corpus echoes from 1 Samuel — **STABLE-with-§4-DECIDE-flag**

1 Samuel is referenced or echoed across multiple NT books. Cross-checking shipped Thai:

| 1 SAM ref | NT echo | Surface check |
|---|---|---|
| 1 Sam 2:1–10 (Hannah's Song) | **Luke 1:46–55 (Magnificat)** | Structural parallel preserved (§6); Layer-2 cross-reference recommended (§7) |
| 1 Sam 2:10 (קֶרֶן מְשִׁיחוֹ) | **Luke 1:69 (κέρας σωτηρίας)** | "ทรงยกเขาของผู้ที่พระองค์ทรงเจิมไว้" ↔ Zechariah's Benedictus "horn of salvation" — both preserve the same Hebrew-derived `เขา` image |
| 1 Sam 9:1 + 9:21 (Kish, Benjamin, Saul) | **Acts 13:21 (Paul's kerygma)** | Thai ดาวิด/ซามูเอล/ซาอูล/คีช match — ✓ (§14 forward audit) |
| 1 Sam 13:14 ("man after his own heart") | **Acts 13:22 (David quote)** | "ข้าได้พบดาวิดบุตรของเจสซี เป็นชายตามใจของเรา" — needs spot-verification; ship-line referenced |
| 1 Sam 15:22 (obedience > sacrifice) | **Hos 6:6 → Matt 9:13 + 12:7 + Mark 12:33** | Cross-corpus prophetic-aphorism thread — Layer-2 enhancement recommended (§11) |
| 1 Sam 21:1–6 (David + showbread) | **Matt 12:3–4 + Mark 2:25–26 + Luke 6:3–4** | Jesus's "David ate the consecrated bread" controversy — cross-corpus rendering needs verification |
| 1 Sam 24:6+ / 26:9+ (anointed-of-YHWH) | **Acts 4:26 (LXX citation of Ps 2:2 χριστός); Heb 1:9; 9:11; throughout** | The OT-base for NT χριστός title; 6× uniform "ผู้ที่องค์พระผู้เป็นเจ้าทรงเจิม" preserves the thread (§9) |
| 1 Sam 25 (Abigail / Nabal) | **Luke 12:20 ("you fool") parable** | Indirect parallel; no surface to verify |
| 1 Sam 28 (Saul + necromancy) | **Acts 16:16–18 (Pythian slave-girl); 1 Tim 4:1 (doctrines of demons)** | NT echoes — Layer-2 cross-reference recommended (§10) |
| 1 Sam 31 (Saul's death) | **1 Chr 10:13 (Chronicler's death-notice citing 1 Sam 28 necromancy)** | Cross-corpus OT-corpus thread — captured in 1 Chr if/when it ships |

**Editorial assessment.** The corpus has shipped Heb 11:32 with David + Samuel matching the 1SA proper-name conventions (verified §14 — no Heb 11:32 name drift for 1SA-derived figures). The Acts 13:21–22 + Acts 7:46 surface checks pass.

**§4 Spirit-of-YHWH drift DOES NOT directly compound to NT side** — the NT Greek uses πνεῦμα (Acts 2 Pentecost; Luke 4:18) which is rendered via a separate Thai-NT decision (see `spiritual_beings_hierarchy_2026-05.md` if extant). But the OT-side `พระวิญญาณ` lock IS the conceptual base for the NT-side OT-quotation rendering at Acts 2:17–18 (Joel 2 citation), Luke 4:18 (Isa 61 citation), and Eph 4:8 (Ps 68 citation).

**REVIEW.** Layer-2 enhancements recommended at the following 1SA verses:
- **2:1, 2:7, 2:8, 2:10** — Magnificat cross-reference (§7)
- **15:22** — Hos 6:6 / Matt 9:13 / Mark 12:33 cross-reference (§11)
- **21:1–6** — Jesus's controversy (Matt 12 / Mark 2 / Luke 6) cross-reference
- **28:3–25** — Acts 16 / 1 Tim 4:1 necromancy / demonic-doctrines cross-reference (§10)

**Severity: LOW–MEDIUM.** Not blocking the v1 tag; corpus-completeness polish.

---

## 22. Mechanical (§1) — **all green**

- 31/31 chapters: `output/check_reports/1samuel_NN_review.md` + `_summary.json` + sub-reports ✓
- 31/31 chapters: `output/back_translations/1samuel_NN.json` ✓
- 31/31 chapters: `output/translations/1samuel_NN.json` ✓
- 31/31 chapters: `output/textual_variants/1samuel_NN.json` ✓ (Tier-2 YHWH-footnote infrastructure deployed; inclusion-variant-Tier-2 gap flagged §17)
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 370-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `python3 scripts/check_divine_names.py --all --report`: **0 hard fails, 125 [C-soft] warnings** (all human-addressee אֲדֹנִי "my lord" — expected; see §2)
- `python3 scripts/audit_inclusion_variants.py --book 1samuel --strict`: **0 candidates** (caveat: script heuristic does not catch the major MT/LXX 1 Sam clusters; see §17)
- `python3 scripts/export_to_usfm.py --book 1SA`: **N/A** — script's BOOKS table covers NT-only; OT export is a separate concern (carried over from prior OT audits)
- `git status output/`: **clean except for `output/check_reports/divine_names.md`** (regenerated by this audit's `--report` run; report-only, not a translation surface change)
- YHWH "องค์พระผู้เป็นเจ้า" occurrences across 1SA: **319** (matches 320 MT — 1:1 ratio, see §1)
- "ยาห์เวห์" residues in verse text: **zero**. One key_decisions meta-discussion at 18:1 ✓.

**Severity: GREEN.** Mechanical gate passes cleanly.

---

## 23. Flagged for Ben's attention

### A. Spirit-of-YHWH empowerment book-wide drift — **DECIDE before tagging** (§4)
**HIGHEST severity.** ~12 verses across 8 chapters (10, 11, 16, 18, 19) drift from `spirit_of_yhwh_empowerment_2026-05.md` lock: bare `วิญญาณ` instead of `พระวิญญาณ`; צָלַח-class drops `อย่างทรงพลัง` adverbial. Lock was written 2026-05-20, two days before this audit, explicitly forward-protecting 1 Sam 10:6, 10:10, 11:6, 16:13. **First corpus drift discovered AGAINST an explicitly-forward-protective lock.** Forward-protects 2 Sam 23:2 + 1 Kgs 18 + 1 Chr 12:18 + 2 Chr 24:20 + Isa 11/61. Cost: ~12 surgical verse-edits + per-chapter check-report regeneration + back-translation refresh. Recommended path: revision branch `revision/spirit-of-yhwh-1sam-2026-05`.

### B. MT/LXX inclusion-variant gap — **DECIDE before tagging** (§17)
**HIGH severity.** Major MT/LXX/Qumran variants at 1 Sam 10:27b+ (4QSamᵃ Nahash plus), 11:1, 13:1 (regnal-formula corruption), 14:41 (LXX Urim/Thummim expansion), 17:12–31 + 17:55–18:5 (LXX-B 39-verse minus) — none are documented in `output/textual_variants/1samuel_NN.json`. First major OT inclusion-variant cluster; gates the Tier-2 textual-variants transparency infrastructure. Cost: 4 chapter-footer JSON entries (~30 min/entry; no translation surface edits). Forward-protects 2 Sam (4QSamᵃ + LXX divergences), Kings (LXX OG), Jer (MT vs LXX shorter recension), Dan.

### C. "Is Saul also among the prophets?" inclusio drift — **REVIEW** (§5)
Normalize 19:24 → "ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ" (matching 10:11+12 form). Cost: 1 surgical verse-edit. **Severity: LOW–MEDIUM.**

### D. Pagan-deity register + Ashtaroth spelling drift — **REVIEW** (§12)
- 5:7 "Dagon-as-`พระเจ้า`-of-Philistines" violates `pagan_deities_2026-04.md` Rule 1 + `ot_polytheistic_register_2026-05.md` §1.3. Normalize → "ดาโกนเทพเจ้าของพวกเรา" (or "ดาโกนพระของพวกเรา" per OT-precedent register).
- Ashtaroth has 3 spellings in 1SA (อัชโทเรท / อาเชโทรท / อัชทาโรท); JDG adds a 4th (อัชเทเรท). Normalize. JDG-audit precedent favors **อัชเทเรท**.
- Baalim minor `พระ`-prefix drift (7:4 vs 12:10) — normalize to `พระบาอัลทั้งหลาย` per JDG precedent.
Cost: ~5 surgical verse-edits + glossary note. **Severity: MEDIUM.**

### E. Sacrificial-vocabulary minor drift — **REVIEW** (§15)
- מִנְחָה collapse to `เครื่องบูชา` at 2:17, 2:29 — normalize to `เครื่องธัญบูชา`.
- שְׁלָמִים 2-surface (10:8 vs 13:9) — normalize to `เครื่องสันติบูชา`.
Cost: 4 surgical verse-edits. **Severity: LOW.**

### F. mal'akh human-messenger surface split — **REVIEW** (§3)
`ผู้ส่งสาร` (ch 16+) vs `ผู้ส่งข่าว` (ch 6, 11). Normalize to `ผู้ส่งสาร` (matches higher-count cluster). Cost: ~5 surgical verse-edits. **Severity: LOW.**

### G. Hannah's humble-Adonai `นายของข้า` — **REVIEW; document or normalize** (§6)
Either: write a brief amendment to `divine_names_table_2026-05.md` adding category (c′) for OT *anawim*-vocative humble-Adonai; OR normalize Hannah's 3 occurrences (1:15, 1:26 ×2) to standard `เจ้านายของข้า`. Recommend documenting the principle (forward-protects Ruth 2:13 + Magnificat-template OT female voices). Cost: minimal doc work OR 3 verse-edits. **Severity: LOW.**

### H. Annotation undercoverage in chs 16+ — **REVIEW** (§19)
Confirm whether `thai_summary` undercoverage in chs 16–30 (28–58% verse coverage) is intentional editorial scaling (action-narrative chapters → sparser summary) or drift. If unintentional, consider retrofit backfill on chs 16, 17, 20, 25, 26, 30. **Severity: LOW–MEDIUM.**

### I. Witch of Endor + necromancy vocabulary lock — **STABLE; new doc** (§10)
Write `docs/translator_decisions/necromancy_and_spiritism_vocabulary_2026-05.md` locking the descriptive-paraphrase Thai surface for אֹב + יִדְּעֹנִי lemma cluster + the 28:13 אֱלֹהִים-as-`พระเจ้า` choice. Forward-protects Lev 19:31 + 20:6/27 (retroactive), Deut 18:9–14, 2 Kgs 21:6 + 23:24, Isa 8:19, 1 Chr 10:13, Acts 16:16–18. **Priority: HIGH** — forward-protects 5+ OT books + 1 NT passage.

### J. Hannah's Song ↔ Magnificat NT cross-corpus thread — **STABLE; new doc** (§7)
Write `docs/translator_decisions/hannah_song_magnificat_thread_2026-05.md` locking the OT-prototype-for-NT reading. Cross-references Magnificat (Luke 1:46–55) + Benedictus (Luke 1:67–79) + *anawim*-template. Cross-references Hannah's 2:35 priestly-Messianic thread to Heb 5–7. **Priority: MEDIUM.**

### K. 1 Sam 15:22 prophetic-aphorism cross-corpus Layer-2 — **STABLE; optional** (§11)
Add Layer-2 cross-reference at 15:22 ("obedience better than sacrifice") to Hos 6:6 + Matt 9:13 / 12:7 + Mark 12:33. Cost: minimal — Layer-2 footer addition. Not blocking; optional polish.

### L. "Until this day" leitwort cross-book normalization — **REVIEW** (§14)
1 SAM uniform `จนถึงวันนี้` ×8/8 ✓; cross-book inconsistency with JDG majority `จนถึงทุกวันนี้`. Recommend single corpus-wide decision in `leitwort_handling_policy_2026-05.md` to pick one canonical form. **Severity: LOW.**

### M. New corpus docs to write — **summary**
1. **`necromancy_and_spiritism_vocabulary_2026-05.md`** (§10 / §I) — descriptive-paraphrase lock; gates 2 Kgs, Isa, Chr ← HIGH PRIORITY
2. **`hannah_song_magnificat_thread_2026-05.md`** (§7 / §J) — OT-prototype-for-NT thread; closes a Magnificat loop ← MEDIUM
3. **(Optional)** `evil_spirit_from_yhwh_1sam_2026-05.md` — companion to spirit-of-yhwh-empowerment for the 16:14–23 + 18:10 + 19:9 evil-spirit cluster (defer until §4 DECIDE resolves)

### N. Existing docs to amend
- **`spirit_of_yhwh_empowerment_2026-05.md`** — add §"1 Sam 1-shipping retroactive remediation" subsection citing §4 DECIDE resolution (after Ben decides path-a)
- **`divine_names_table_2026-05.md`** — add category (c′) humble-Adonai *anawim*-vocative per §6
- **`proper_names_and_transliteration_2026-05.md`** — normalize Ashtaroth spelling (cross-corpus JDG + 1SA) per §12
- **`pagan_deities_2026-04.md`** + **`ot_polytheistic_register_2026-05.md`** — add 1 Sam 5:7 Dagon-as-`พระเจ้า` violation as test case (after §12 normalization)
- **`leitwort_handling_policy_2026-05.md`** — lock the canonical Thai surface for "until this day" leitwort per §14

### O. External AI review (§3 of checklist) — **pending**
Recommended 5-cluster external AI packet:
1. **Spirit-of-YHWH book-wide drift** (§4) — HIGHEST priority; first lock-vs-shipped corpus divergence
2. **MT/LXX inclusion-variant gap** (§17) — first major OT inclusion-variant cluster
3. **"Saul among the prophets" inclusio surface drift** (§5)
4. **Pagan-deity register Dagon-`พระเจ้า` at 5:7 + Ashtaroth spelling drift** (§12)
5. **Witch of Endor + necromancy vocabulary corpus doc** (§10) — gate-status check for the new doc

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1 YHWH, §2 Elohim/Adonai, §3 mal'akh-base-case, §8 oath formula, §9 משיח inclusio, §11 cherem, §13 royal register, §14 leitwort-internal, §16 nicham, §18 oath compounds, §22 mechanical; + inherited locks via §20 row breakdown)
- **STABLE (recommend new doc):** 2 items (§10 necromancy vocabulary, §7 Hannah-Magnificat thread); + 1 STABLE Layer-2 enhancement (§11 15:22 prophetic-aphorism)
- **REVIEW:** 6 items (§3 mal'akh-messenger-split, §5 Saul-prophets inclusio, §6 Hannah humble-Adonai, §12 pagan deities + Ashtaroth, §14 cross-book "until this day", §15 sacrificial vocab, §19 annotation undercoverage)
- **DECIDE:** 2 items (§4 Spirit-of-YHWH HIGHEST; §17 MT/LXX inclusion-variant gap HIGH)

**2 DECIDE items block the `book-1samuel-v1` tag.** (§4, §17)

**2 new translator_decisions docs recommended** (`necromancy_and_spiritism_vocabulary_2026-05.md`, `hannah_song_magnificat_thread_2026-05.md`) + 1 deferred (`evil_spirit_from_yhwh_1sam_2026-05.md` — defer until §4 resolves).

**5 existing docs to amend** (`spirit_of_yhwh_empowerment_2026-05.md` retroactive-remediation; `divine_names_table_2026-05.md` category c′; `proper_names_and_transliteration_2026-05.md` Ashtaroth normalization; `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` 5:7 test case; `leitwort_handling_policy_2026-05.md` "until this day" canonical lock).

---

## Recommendation

**1 Samuel ships in OVERALL strong corpus-hygiene shape — with one HIGHEST-severity exception.** It is the **third Former-Prophets book** and the FIRST DOWNSTREAM TEST of the JDG-audit-era locks outside Judges. The audit finds:

- The Adonai-cluster JDG-audit §8 DECIDE is implicitly **deferred** to 2 Sam 7 (no divine-Adonai-prayer occurs in 1SA).
- The Heb 11:32 ↔ JDG name-drift JDG-audit §9 DECIDE does NOT compound to 1SA (the Heb 11:32 ดาวิด + ซามูเอล surfaces match 1SA exactly; only the JDG-side กิดเอน / เยฟทาห์ remain pending).
- The mal'akh-YHWH lock holds — 1SA simply has no divine-mal'akh occurrences; the lock's first test in a non-mal'akh-rich narrative book is silent compliance ✓.
- The cherem, oath formula, nicham, royal register, divine anthropomorphism, Hebrew grammar transfer, leitwort handling, and proper-noun wordplay docs all carry cleanly.
- The 1 Sam 24:6+ / 26:9+ "ผู้ที่องค์พระผู้เป็นเจ้าทรงเจิม" inclusio is the densest single-book deployment of the מָשִׁיחַ-formula in the OT corpus — the load-bearing forward-protection of the Davidic-Christology thread.

However, **2 DECIDE items** must resolve before tagging `book-1samuel-v1`:

1. **§4 — Spirit-of-YHWH empowerment book-wide drift.** First-ever corpus drift discovered AGAINST an explicitly-forward-protective lock (the doc was written 2 days before this audit, specifically citing 1 Sam 10:6 / 10:10 / 11:6 / 16:13 in its forward-protection clause). Cost: ~12 surgical verse-edits + revision branch. **Forward-protects 2 Sam 23:2 + 1 Chr 12:18 + 2 Chr 24:20 + Isa Messianic-Spirit + NT pneumatology base.**
2. **§17 — MT/LXX inclusion-variant gap.** First major OT inclusion-variant cluster (4 known major variants undocumented). Cost: 4 chapter-footer JSON entries. **Gates the Tier-2 textual-variants infrastructure for 2 Sam + Kings + Jer + Dan.**

The 2 STABLE-but-undocumented items (§10 necromancy + §7 Hannah-Magnificat thread) should be lifted to corpus docs — necromancy is the higher priority (forward-protects 2 Kgs + Isa + Chr + Acts).

Tag `book-1samuel-v1` after:
1. Ben's decisions on **§A + §B** (DECIDE: Spirit-of-YHWH drift; MT/LXX inclusion-variant gap)
2. Ben's confirmation on **§C through §H** (6 REVIEW items)
3. Two new translator_decisions docs written (**§I + §J** — necromancy vocabulary; Hannah-Magnificat thread)
4. Five existing docs amended (per §N)
5. External AI sanity-check (§O)

**The Former-Prophets corpus** (Ruth-already-shipped, Genesis-Joshua-Judges-1Sam-now-pending-tag, 2 Sam, 1–2 Kgs) — writing `necromancy_and_spiritism_vocabulary_2026-05.md` before 2 Kgs 21+23 (Manasseh + Josiah) ships is the load-bearing forward-protection step from this audit.
