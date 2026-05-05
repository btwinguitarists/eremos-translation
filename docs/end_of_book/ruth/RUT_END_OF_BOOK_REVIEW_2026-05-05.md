# Ruth — End-of-Book Review

**Date:** 2026-05-05
**Scope:** All 4 chapters (85 verses; ~250 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (52 docs incl. the 9 new OT-specific docs landed during W1).
**Trigger:** RUT 4 shipped (commit `b429230`); per `docs/END_OF_BOOK_CHECKLIST.md`. **First OT book in the corpus.**
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 4/4 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-130-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/`: untracked OT-extension check artifacts only (ot_citations / honorifics_binding / claim_consistency for ruth chapters — newly-added OT checks per W1 Day 9-11 PR #113; not run during NT-era ship for this book; not blockers for the audit itself).
- **Ruth is the FIRST OT book in the corpus** (after the 22-book NT pilot finished). The OT-specific lock-set landed in W1 (`divine_names_table_2026-05.md`, `ot_register_policy_2026-05.md`, `hebrew_grammar_transfer_2026-05.md`, `hebrew_idioms_and_metaphor_2026-05.md`, `ot_canon_and_text_base_2026-05.md`, `proper_names_and_transliteration_2026-05.md`, `pagan_deities_2026-04.md` reused, `adversary_speech_register_2026-05.md` reused, `honorifics_non_divine_authorities_2026-04.md` reused) was exercised here for the first time. The technical-vocabulary established in Ruth (chesed, go'el, Shaddai, Hebrew oath formulas, ḥayil-pair) propagates forward to Jonah → Genesis 1–11 → the rest of the Hebrew canon.
- **8 inherited NT-corpus locks verified compliant** in Ruth (Tetragrammaton-as-`องค์พระผู้เป็นเจ้า`, ἔθνος-style ชนชาติ, pagan-deity register, narrator-vs-character voice, OT-citation flagging-N/A, narrator-Adonai split, divine-object-praise-verbs precedent, honorifics for non-divine authority).
- **3 cross-cutting OT-distinctive patterns are STABLE-and-locked** at corpus level (Tetragrammaton convention with per-chapter footer note; chesed → ความรักมั่นคง; go'el → ญาติผู้ไถ่). All three propagate forward; locks are explicit + testable.
- **3 items flagged REVIEW** (defensible-but-worth-Ben-or-Thai-reviewer-confirmation: paqad → ทรงเยี่ยมเยียน register softness; mənuḥâ → ความสงบมั่นคง vs original ที่พักพิง; the narrator's collective-stir verb הוּם at 1:19 → แตกตื่น vs ฮือฮา).
- **3 items flagged DECIDE** (RUT 1:13 הַיָד יְהוָה anthropomorphism — ทรง- prefix-on-body-part principle; RUT 3:9 כָּנָף wordplay flatness in main text — wing-vs-cloak collapse; RUT 4:19 רָם / Mt 1:3 อารัม cross-corpus normalization).
- **External AI review (§3) pending.** This is the first OT-book external review; suggested 4-cluster packet at the end.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben-or-Thai-reviewer confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה — corpus-wide rendering + per-chapter footer convention — **LOCKED**

15 occurrences across the 4 chapters, all uniform **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` (Layer 1 vocabulary lock). Per-chapter Layer 2 footer note triggered at first occurrence (RUT 1:6 KD declares the convention; 2:4, 3:10, 4:11 are the chapter-anchor verses where YHWH first appears in chs.2-4 — tetragrammaton footer notes added per PR #118 `bbe78d2`).

| Chapter:Verse | Context | Thai rendering |
|---|---|---|
| 1:6 | Narrator: YHWH visited his people | ทรงเยี่ยมเยียน (royal-verb prefix) |
| 1:8, 1:9 | Naomi's jussive blessings | ขอองค์พระผู้เป็นเจ้าทรง- (jussive prayer-form) |
| 1:13 | Naomi's lament: hand of YHWH | พระหัตถ์ขององค์พระผู้เป็นเจ้า (possessive — see §4) |
| 1:17 | Ruth's oath formula | ขอ...ทรงลงโทษ |
| 1:21 | Naomi: YHWH brought me back | ทรงนำ...กลับมา |
| 2:4 (×2) | Boaz↔workers greeting + blessing exchange | ทรงสถิต / ทรงอวยพร |
| 2:12 | Boaz prays YHWH to repay Ruth | ทรงตอบแทน |
| 2:20 | Naomi: YHWH has not abandoned ḥesed | ผู้ไม่ทรงละทิ้ง |
| 3:10 | Boaz blessing Ruth | ทรงอวยพร |
| 3:13 | Boaz's oath חַי־יְהוָה | ตราบใดที่...ทรงพระชนม์อยู่ |
| 4:11, 4:12 | Elders' blessings | ทรงโปรด / ทรงประทาน |
| 4:13 | Narrator: YHWH gave conception | ทรงประทาน |
| 4:14 | Women's blessing-of-YHWH | ทรงเป็นที่สรรเสริญ |

**Editorial assessment:** The NT-aligned vocabulary lock (matching the 22 shipped NT books rendering κύριος-as-YHWH) holds without exception. The Hebrew-form transparency mechanism (Layer 1 KD per verse + Layer 2 first-occurrence footer per chapter) is exercised correctly in all four chapters. The reversibility clause in `divine_names_table_2026-05.md` (find-replace migration to `พระยาห์เวห์` if Thai reader feedback prefers historical-transliteration) remains open without any per-verse cost.

**LOCKED** ✓ — no action.

---

## 2. חֶסֶד (chesed, covenant loyal-love) — Ruth's central theological term — **LOCKED**

Three occurrences (1:8, 2:20, 3:10), all uniform **ความรักมั่นคง** ("steadfast love"). The 1:8 KD declares the OT-corpus key-term lock; 2:20 + 3:10 cite the lock by reference.

| Verse | Hebrew | Thai | Context |
|---|---|---|---|
| 1:8 | יַעַשׂ יְהוָה ... חֶסֶד | ขอองค์พระผู้เป็นเจ้าทรงสำแดงความรักมั่นคง | Naomi's jussive prayer-blessing for the daughters-in-law |
| 2:20 | (אֲשֶׁר) לֹא־עָזַב חַסְדּוֹ | ผู้ไม่ทรงละทิ้งความรักมั่นคงของพระองค์ | Naomi recognizes YHWH's ḥesed working through Boaz |
| 3:10 | הֵיטַבְתְּ חַסְדֵּךְ הָאַחֲרוֹן מִן־הָרִאשׁוֹן | ความรักมั่นคงของเจ้าในครั้งหลังนี้ยิ่งใหญ่กว่าครั้งก่อนเสียอีก | Boaz contrasts Ruth's later vs earlier ḥesed |

**Editorial assessment:** The single rendering carries the Hebrew Bible's signature covenant-faithfulness term forward into the Thai OT corpus. Distinguished from אַהֲבָה (general love → รัก, e.g. 4:15 of Ruth's love for Naomi) and from the Pauline-NT compound `divine_object_praise_verbs_2026-04.md` corpus-lock for δοξάζω/εὐλογέω/αἰνέω as praise. **The lock is theologically and lexically clean. Will compound massively into the Psalms (~127 occurrences of ḥesed alone) and the prophetic books.**

**Recommend: lift from in-place 1:8 lock to corpus doc** `docs/translator_decisions/chesed_covenant_love_2026-05.md` before Ps 23 ships (expected after Jonah). The doc should:
1. Lock חֶסֶד → ความรักมั่นคง
2. Cite Ruth 1:8 as the locking precedent
3. Document the distinction from אַהֲבָה (→ รัก) and the rare רַחֲמִים (→ พระเมตตา / ความเมตตาสงสาร — to be locked at first Ps occurrence)
4. Note compounds: חֶסֶד וֶאֱמֶת (Pss "steadfast-love and faithfulness"), חַסְדֵי יְהוָה (Pss 89:2 "the steadfast loves of YHWH"), אִישׁ חֶסֶד / אַנְשֵׁי חֶסֶד (Prov 11:17, Isa 57:1)

---

## 3. גֹּאֵל (go'el, kinsman-redeemer) — chapter 3-4 legal vocabulary — **LOCKED**

The book's central legal-theological term. ~14 occurrences across chs.3-4 (גֹּאֵל ~9×, גָּאַל verb ~5×, גְּאֻלָּה noun 2× at 4:6, 4:7), all consistent.

| Form | Thai | Sense |
|---|---|---|
| גֹּאֵל (noun, the redeemer-person) | **ญาติผู้ไถ่** | The kinsman with redemption-right |
| גָּאַל / גָּאֳלִי / יִגְאָל (verb) | **ไถ่** | To redeem (act-of-redemption) |
| גְּאֻלָּה (noun, the redemption-right) | **สิทธิ์ในการไถ่** | The legal claim/right to redeem |
| מוֹדָע / מֹדַעַת (rare kin-cluster nouns; 2:1, 3:2) | **ญาติ** | "One known" — pre-explicit kinsman framing |

Boaz's introduction at 2:1 uses the rare מוֹדָע "kinsman" (broad "one-who-is-known" sense) rather than the technical גֹּאֵל; the explicit go'el lemma surfaces at 2:20 (Naomi to Ruth) — the narrator's deliberate-disclosure pattern, preserved in Thai by the same ญาติ → ญาติผู้ไถ่ progression.

**Editorial assessment:** The Thai compound ญาติผู้ไถ่ ("relative-redeemer") combines the kinship-frame (ญาติ) with the redemption-act (ไถ่) — preserves the dual force of the Hebrew lemma without periphrasis. The verb-noun distinction (ไถ่ vs ญาติผู้ไถ่ vs สิทธิ์ในการไถ่) tracks the Hebrew's morphological derivations cleanly.

**Recommend: lift to corpus doc** `docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` before Job 19 ("I know that my Redeemer lives," גֹּאֲלִי), Isa 41:14 (Israel's Redeemer-YHWH), Pss 19:14 + 78:35 (YHWH-as-redeemer language), Prov 23:11 (the Redeemer-of-the-orphan). The Christological-typological NT cross-reference (Christ-as-redeemer language at Tit 2:14, Heb 9:12 ἀπολύτρωσιν, etc.) merits explicit cross-corpus link.

---

## 4. RUT 1:13 יַד־יְהוָה anthropomorphism — ทรง- prefix policy — **DECIDE**

The 1:13 KD documents an **explicit policy choice** that arose during ChatGPT review (2026-05-05): `יַד־יְהוָה יָצְאָה בִי` ("the hand of YHWH has gone out against me") rendered as **พระหัตถ์ขององค์พระผู้เป็นเจ้าได้ยื่นออกมาต่อสู้กับฉัน**. The verb ยื่นออกมา is **plain, no ทรง- prefix**, because the grammatical subject of the verb is `พระหัตถ์` (the hand), not YHWH directly. The KD frames this as a **Thai-grammar rule**: ทรง- attaches to verbs whose subject is the divine person, not to verbs whose subject is a body-part-of-the-divine-person.

**Editorial assessment:** This is principled and correct per Thai Rachasap grammar. The royal-Thai prefix พระ- still applies to the body-part itself (พระหัตถ์, not มือ); the verb downstream is plain. But: this is an **OT-frequent construction** (יַד יהוה occurs ~30× in OT in hostile-touch / mighty-act contexts; פִּי יהוה "mouth of YHWH" ~50×; עֵינֵי יהוה "eyes of YHWH" ~20×; פְּנֵי יהוה "face of YHWH" ~140×). The same ทรง-or-not question recurs everywhere.

The lock here in Ruth is implicit-at-verse-level. **Ben to decide:** elevate the Ruth 1:13 grammar-policy to an explicit corpus-doc rule. Suggested resolution:

**→ Recommend new doc:** `docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md` — locks the principle:
1. **YHWH-as-direct-subject of a verb** → ทรง- + verb (`พระเจ้าทรงตรัส`, `องค์พระผู้เป็นเจ้าทรงเสด็จ`)
2. **YHWH's body-part as grammatical subject of a verb** → royal-Thai prefix on the body-part (พระหัตถ์ / พระเนตร / พระโอษฐ์ / พระบาท / พระพักตร์), but verb stays **plain** (no ทรง-)
3. Cite Ruth 1:13 as the locking precedent
4. Document the contrast: when the body-part is in a possessor-position (e.g., "by the hand of YHWH" = an instrumental-by-phrase), the verb's subject is whoever/whatever performs the action — apply the rule consistently

This will compound into Exod 7:5 / 14:31 ("the great hand which YHWH did"); Deut 9:26; the Habakkuk theophanies; the eyes-of-YHWH idioms in 2 Chr 16:9 + Pss 33:18, 34:15; the face-of-YHWH idioms throughout the Pss; the mouth-of-YHWH formula in Isa-Jer.

---

## 5. RUT 1:6 פָקַד יהוה / RUT 1:9 מְנוּחָה — divine-action verb selection — **REVIEW**

The Ruth 1 KDs explicitly flag two verb-selection issues for end-of-book reviewer-validation, both adopted 2026-05-05 per ChatGPT review feedback:

### 5a. RUT 1:6 פָקַד → ทรงเยี่ยมเยียน (open question for Thai-language reviewer)

The 1:6 KD documents:
> "Render as 'ทรงเยี่ยมเยียน' (royal-Thai + visit) — adopted 2026-05-05 per ChatGPT review feedback to soften from earlier 'เสด็จมาเยี่ยมเยียน' which read as overly heavy royal-physical-visit register; the simpler ทรง-prefix preserves the divine-action register without implying a royal procession. **Open question for the Thai-language reviewer: is ทรงเยี่ยมเยียน too plain, or is ทรงเหลียวแล (look upon with care) more natural for paqad in pastoral-care contexts?**"

**Editorial assessment:** The verb פָּקַד is one of the OT's most frequent and contextually-ranged divine-action verbs (visit, attend to, intervene, muster, appoint, requite, hold accountable — ~300× OT). Locking the Ruth-1:6 covenantal-care sense alone is insufficient; the lemma needs a corpus-doc table. The ทรงเยี่ยมเยียน rendering is correct for the pastoral-care sense at 1:6 (matching Gen 21:1, Ex 4:31, 1 Sam 2:21, Lk 1:68 NT-echo); but other senses (פָּקַד as "hold accountable / requite," e.g. Ex 32:34 + the prophetic visitation-of-judgment idiom) need different Thai handling.

**Recommend: REVIEW + new doc** `docs/translator_decisions/paqad_visit_attend_2026-05.md` before 1 Samuel 2 (Hannah-Eli narrative is ยָקַד-dense). The doc should:
1. Lock contextual-rendering table: pastoral-care → ทรงเยี่ยมเยียน; numbering/mustering → ทรงทำสำมะโน; appointment → ทรงแต่งตั้ง; judgment-visitation → ทรงลงโทษ / ทรงทำการลงทัณฑ์
2. Cite Ruth 1:6 as the pastoral-care locking precedent
3. Surface the open question (ทรงเยี่ยมเยียน vs ทรงเหลียวแล) for Thai-language reviewer to settle

### 5b. RUT 1:9 מְנוּחָה → ความสงบมั่นคง (open question)

Same 2026-05-05 ChatGPT-review revision: from earlier ที่พักพิง (refuge/shelter — too physical-shelter-leaning) to ความสงบมั่นคง (settled-peace — better captures security-in-marriage nuance). 1:9 KD: "Open for Thai-language reviewer validation."

This is the same lemma as 3:1 מָנוֹחַ ("resting place"), there rendered ที่พักพิง — a deliberate contextual split: 1:9 = "may YHWH grant you מְנוּחָה" (abstract security in marriage) → ความสงบมั่นคง; 3:1 = "I will seek מָנוֹחַ for you" (concrete future-home with husband) → ที่พักพิง. **The split is principled** (the morphological feminine form מְנוּחָה carries the abstract sense; masculine מָנוֹחַ here carries the concrete-place sense per Naomi's 3:1 imagery), but the cross-lemma divergence (same root) is worth flagging for reviewer attention.

**Recommend: REVIEW;** if the split is endorsed, document in a brief doc (or in the chesed/ot-register doc as an aside) so it doesn't drift in Pss 95:11 / Heb 4:1ff (the canonical "rest" theme).

---

## 6. RUT 3:9 כָּנָף wordplay — wing/corner wordplay flatness in Thai — **DECIDE**

**The chapter 2-3 verbal echo:**
- 2:12 (Boaz to Ruth): `תַּחַת־כְּנָפָיו` ("under whose wings [of YHWH] you have come to take refuge") → **ใต้ปีกของพระองค์**
- 3:9 (Ruth to Boaz): `וּפָרַשְׂתָּ כְנָפֶךָ עַל־אֲמָתְךָ` ("spread your wing/corner-of-cloak over your handmaid") → **กางชายผ้าคลุมของท่านมาคลุมสาวรับใช้ของท่าน**

**The literary-theological pivot:** Hebrew uses the same noun כָּנָף for both (the noun's dual-sense "wing/edge-of-garment"). Boaz prays Ruth will take refuge under YHWH's wings (2:12); Ruth then asks Boaz to spread his wing/corner over her — Boaz becomes the human instrument by which YHWH answers Boaz's own prayer. **The Thai loses the verbal echo** because the two senses use different lexemes (ปีก = wing-of-bird; ชายผ้าคลุม = corner-of-cloak). The 3:9 thai_summary unpacks the wordplay; the main text presents the cultural-marriage-idiom but cannot transmit the verbal echo back to 2:12.

**Editorial assessment:** This is the chapter's most theologically-loaded literary device. Hebrew Bible scholars consistently flag the כָּנָף-wordplay as deliberate. Three options:

(a) **Surface preservation (current state)** — keep ปีก (2:12) + ชายผ้าคลุม (3:9); the verbal echo is unpacked in 3:9 thai_summary. The Thai surface reads naturally; the wordplay survives as scholarly footnote.

(b) **Force the echo at 3:9** — render 3:9 as **ขอท่านโปรดกางปีกแห่งผ้าคลุมของท่าน** (lit. "spread the wing-of-your-cloak") to import ปีก back into the 3:9 context. Preserves the verbal echo but adds Thai awkwardness — ปีก does not naturally apply to a garment in Thai, where it strictly means bird-wing.

(c) **Force the echo at 2:12** — render 2:12 as **ใต้ชายของปีกของพระองค์** (lit. "under the corner-of-the-wing of him") with footnote. Unusual Thai but makes the 3:9 echo visible.

**Ben to decide:** whether to accept the surface-flatness (option a) for natural Thai vs. preserve the verbal-echo at the cost of one site's awkwardness. The Pss compound this question (Ps 17:8, 36:7, 57:1, 91:4 all use כָּנָף "wings" of YHWH's protection); Mt 23:37 / Lk 13:34 NT-cross-reference also uses πτέρυγας. Recommend surfacing this with the external AI reviewers + the Thai-language reviewer; the choice between (a)/(b)/(c) compounds forward.

---

## 7. RUT 4:19 רָם vs Mt 1:3-4 อารัม — cross-corpus name-form normalization — **DECIDE**

**The divergence (already documented in the 4:19 KD):**
- Ruth 4:19 (OT, Hebrew רָם → THSV11 baseline) → **ราม**
- Matthew 1:3-4 (NT, Greek Ἀράμ with prosthetic alpha) → **อารัม**

Both refer to the same person — the OT figure between Hezron and Amminadab in the Davidic line. Same person, two Thai forms, due to the Greek-vs-Hebrew source-form difference (LXX adds prosthetic α, common in Greek transcription of Hebrew names beginning with /r/).

**Editorial assessment:** This is a generalizable issue across all OT-NT-shared genealogical names. Other Ruth-4 names (Hezron, Amminadab, Nahshon, Salmon, Boaz, Obed, Jesse, David) are already cross-corpus-locked to consistent Thai forms (per Mt 1:3-6 + Lk 3:32-33 verified compliant — see the agent-extracted scorecard). **Ram is the one drift** — and it's not Ruth's-fault (the Mt locking happened earlier from Greek; Ruth follows THSV11 from Hebrew).

The 4:19 KD already names this and recommends "future polish-pass." Three corpus-resolution paths:

(a) **OT Hebrew form wins** (ราม corpus-wide) — normalize Mt 1:3-4 in a future NT polish-pass to ราม. Hebrew-text fidelity argument; matches THSV11.

(b) **NT Greek form wins** (อารัม corpus-wide) — normalize Ruth 4:19 to อารัม. Cross-corpus consistency argument; matches the already-shipped Mt; aligns with mainstream evangelical Thai (NTV/THSV-Plus/ESV-Thai all carry over the Greek prosthetic).

(c) **Tolerate the divergence with a doc** — explicitly lock both forms with a translator-decision doc; readers see the same person in two valid Thai transliterations.

**Ben to decide.** The same question recurs for several other OT-Hebrew-vs-NT-Greek transliteration pairs: יִשַׁי / Ἰεσσαί (Jesse, currently both → เจสซี ✓), שְׁלֹמֹה / Σολομών (Solomon at 2 Sam 11ff vs Mt 1:6-7), אִיזֶבֶל / Ἰεζάβελ (Jezebel), and many others coming in Phase 6D (the Former Prophets). The Ram instance at Ruth 4:19 is the first concrete trigger; it warrants a rule, not a one-off polish.

**→ Recommend new doc:** `docs/translator_decisions/cross_corpus_name_normalization_2026-05.md` after Ben's decision (a/b/c). Document the rule + the migration plan (what Mt + Lk verses get normalized + when).

---

## 8. RUT 1:19 הוּם → แตกตื่น — Thai naturalness — **REVIEW**

The 1:19 KD documents:
> "Per ChatGPT review 2026-05-05: revised from earlier 'เกิดการตื่นเต้น' (which leans toward happy-excitement) to 'แตกตื่น' (be-startled/stirred-up) — captures the disturbed-reaction sense (the women's amazement is at how Naomi has been transformed by tragedy, not delighted excitement). **Open question for the Thai-language reviewer: is แตกตื่น appropriate here, or would ฮือฮา (buzzing/talking-up) be more natural Thai for the collective-vocal-stir?**"

**Editorial assessment:** The translator surfaces the open question explicitly. Both options are defensible:
- **แตกตื่น** (current) — disturbed/agitated, captures the negative-amazement (Naomi's tragic-changed appearance)
- **ฮือฮา** — collective-buzzing, more colloquial-natural Thai for "the whole town was talking"

The Hebrew הוּם itself spans both registers. The verse's force is the women's collective vocalization ("Is this Naomi?") + Naomi's response naming herself Mara. **REVIEW for Thai-language reviewer.**

---

## 9. RUT 1:13 הַפַקס תֵּעָגֵנָה + RUT 2:14 צָבַט + RUT 2:16 צֶבֶת + RUT 3:2 מֹדַעַת — hapax-legomena cluster — **STABLE (documented per-verse)**

Five hapax-or-near-hapax items in the book; all explicitly flagged in the relevant KD with **HAPAX** marker + etymology + lexicographic-resolution method:

| Verse | Hebrew | Thai | Resolution method |
|---|---|---|---|
| 1:13 | תֵּעָגֵנָה (ʿāgan, hapax) | งดแต่งงาน | Niphal context "shut up from marriage"; ChatGPT-revised from wordy "อยู่ในสภาพไม่แต่งงาน" |
| 2:1 + 3:2 | מוֹדַע / מֹדַעַת (2× / hapax-fem-form) | ญาติ | Cognate of יָדַע "know"; broad clan-relative |
| 2:14 | צָבַט (hapax verb) | ยื่น...ให้ | Cognate Arabic/Akkadian "grasp/seize"; modern English "reached out, offered" |
| 2:16 | צֶבֶת (hapax noun) | กอง | Connected to "bind/tie" root; "bundles" or "tied stalks" |
| 4:21 | שַׂלְמוֹן (hapax form variant of שַׂלְמָה v.20) | สัลโมน | Harmonized to single Thai form across 4:20 + 4:21 |

**Editorial assessment:** The translator's transparency-of-method here is exemplary — every hapax flagged, every uncertainty named, every resolution path documented. **STABLE — no action.** The hapax-handling becomes a template for the rest of the OT corpus where lexicographic uncertainty will compound (Job and the Psalms have ~80 OT-hapaxes between them).

---

## 10. Hebrew oath formulas — RUT 1:17 + RUT 3:13 — **STABLE (recommend lift to corpus doc)**

Two distinct OT oath-formulas surface in Ruth, both with Eremos-locked Thai renderings:

| Form | Hebrew | Thai | Verses |
|---|---|---|---|
| Self-imprecation (strongest) | כֹּה יַעֲשֶׂה יהוה לִי וְכֹה יֹסִיף | ขอองค์พระผู้เป็นเจ้าทรงลงโทษข้าพเจ้า และให้หนักยิ่งกว่านั้นอีก | 1:17 |
| Vow-by-divine-life | חַי־יְהוָה | ตราบใดที่องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ | 3:13 |

The 1:17 KD: "**Hebrew oath formula** ... the speaker invokes a self-curse if the oath is broken (cf. 1 Sam 3:17, 14:44, 20:13, 25:22; 2 Sam 3:9, 35; 19:14; 1 Kgs 2:23; 19:2; 20:10; 2 Kgs 6:31). The implicit curse is severe: 'may YHWH strike me dead and worse.'"

The 3:13 KD: "**ESTABLISHES OT OATH-FORMULA LOCK.** Per uW writing-oathformula: חַי־יְהוָה is the standard Hebrew most-binding oath, occurring 25× in Samuel-Kings alone."

**Editorial assessment:** Both are **STABLE in Ruth** (single occurrence each, principled rendering). The 25-occurrences-in-Sam-Kgs forward-load makes corpus-doc-lift critical before Phase 6D (Former Prophets). **Recommend new doc:** `docs/translator_decisions/hebrew_oath_formulas_2026-05.md` covering:
1. כֹּה יַעֲשֶׂה ... וְכֹה יֹסִיף — render Ruth 1:17 form
2. חַי־יְהוָה — render Ruth 3:13 form
3. חַי־אֲדֹנָי / חֵי נַפְשְׁךָ ("by the life of your soul") — Sam-Kgs variants
4. נִשְׁבַּע יהוה / שְׁבוּעָה — when YHWH is the swearer

Cite Ruth 1:17 + 3:13 as the locking precedents.

---

## 11. Hebrew narrative grammar — wayyiqtol chains, וַיְהִי, hendiadys, infinitive absolute — **STABLE (already documented in `hebrew_grammar_transfer_2026-05.md`)**

Ruth exercises the doc's full set of Hebrew-narrative-Thai-translation patterns:
- **Wayyiqtol-chain compression** (e.g., 1:6 "rose-up + returned"; 2:3 "went + came + gleaned" → Thai compress; 4:13 "took + became + entered + gave" → Thai connective-mix)
- **וַיְהִי opener** (1:1 "in the days of the judges"; 3:8 "at midnight"; 4:7 narrator-aside) — handled idiomatically per `hebrew_idioms_and_metaphor_2026-05.md` §5.1
- **Hendiadys** (1:9 lifted-voice + wept; 2:6 answered + said; 4:7 redemption + exchange) — collapsed appropriately
- **Infinitive absolute intensifying** (2:11 הֻגֵּד הֻגַּד; 2:16 שֹׁל־תָּשֹׁלּוּ) — encoded with totalizer + perfective Thai
- **Stative verbs** (1:12 זָקַנְתִּי "I am old") — adjectival rendering per doc §4
- **Cognate figura etymologica** (1:20 הֵמַר + מָרָא; 2:3 וַיִּקֶר מִקְרֶהָ) — preserved or unpacked in summary
- **הִנֵּה attention-marker** — uniformly ดูเถิด across 1:15, 2:4, 3:8, 4:1 per doc §5.2

**Editorial assessment:** The doc's coverage holds across Ruth without exception. **STABLE** ✓ — no action. The doc may want a "Ruth-as-template" annotation for future OT-translator orientation; that's a doc-meta-improvement, not a content change.

---

## 12. Hebrew idioms — wings, hand, eyes-of-favor, "spread the wing," etc. — **STABLE (already documented in `hebrew_idioms_and_metaphor_2026-05.md`)**

Major idiom-clusters exercised in Ruth:
- **חֵן בְּעֵינֵי X** ("favor in the eyes of") — 2:2, 2:10, 2:13 — rendered ความเมตตาในสายตาของ-
- **דִבֵּר עַל לֵב** ("speak upon the heart") — 2:13 — pragmatically rendered พูดด้วยความเมตตา (kind-speech)
- **נָשָׂא קוֹל** ("lift the voice") — 1:9, 1:14 — rendered ส่งเสียงร้องไห้
- **כָּנָף** ("wing / corner-of-garment") — 2:12, 3:9 — see §6 above
- **הַ בַּיִת = "to the city/courthouse" idiom** (gate/threshold) — 4:1 ประตูเมือง
- **לְהָקִים שֵׁם** ("raise up the name") — 4:5, 4:10 — สืบทอดชื่อ
- **רֵיקָם הֱשִׁיבַנִי** vs **אַל־תָּבוֹאִי רֵיקָם** ("empty-hand" verbal-thread 1:21 → 3:17) — preserved as มือเปล่า in both
- **תְּמוֹל שִׁלְשׁוֹם** ("yesterday + day-before-yesterday" = "previously") — 2:11 — rendered ก่อน...เลย
- **אִישׁ גִּבּוֹר חַיִל / אֵשֶׁת חַיִל** mirrored pair (2:1, 3:11) — ชายผู้มีฐานะมั่งคั่งและทรงเกียรติ / หญิงผู้ทรงคุณธรรมและทรงเกียรติ — see §13 below

**Editorial assessment:** The idiom-handling holds across the book. The 2:13 "speak upon the heart" pragmatically-rendered (vs literal-preserved) is the one editorial-judgment call worth confirming with reviewers; the heart-imagery is preserved in `thai_literal` per the project's two-tier approach.

**STABLE** ✓ — no action.

---

## 13. אִישׁ גִּבּוֹר חַיִל ↔ אֵשֶׁת חַיִל mirrored introduction pair — **LOCKED**

Ruth 2:1 introduces Boaz: אִישׁ גִּבּוֹר חַיִל → **ชายผู้มีฐานะมั่งคั่งและทรงเกียรติ** ("man of standing and honor"). Ruth 3:11 has the elders-of-the-town report their assessment of Ruth: אֵשֶׁת חַיִל → **หญิงผู้ทรงคุณธรรมและทรงเกียรติ** ("woman of virtue and honor"). The narrator's deliberate gender-pair sets Ruth as Boaz's character-equal despite the ethnic asymmetry.

The 3:11 KD declares: "**Project-wide lock established: אֵשֶׁת חַיִל = หญิงผู้ทรงคุณธรรมและทรงเกียรติ.**" Will compound into Pr 12:4, 31:10ff (the canonical "wife of valor" acrostic).

**Editorial assessment:** Both renderings are 4-syllable Thai compounds with parallel grammatical structure ("person-who-has X and Y"). The שׁוּב-rendering choice (ทรงคุณธรรมและทรงเกียรติ for אֵשֶׁת חַיִל) carries the moral-character emphasis the elders' speech requires; the parallel ผู้มีฐานะมั่งคั่งและทรงเกียรติ for אִישׁ גִּבּוֹר חַיִל carries the wealth-and-character force of Boaz's introduction. **LOCKED** ✓ — no action.

---

## 14. Inherited NT-corpus locks — **all compliant**

| Doc | Ruth evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | 15 YHWH occurrences, 2 Shaddai (1:20, 1:21 → ผู้ทรงมหิทธิฤทธิ์), 1 Adonai-pl-pagan (1:15 אֱלֹהֶיהָ → พระทั้งหลาย). Layer 1 + Layer 2 mechanisms exercised. | **LOCKED** |
| `ot_register_policy_2026-05.md` | Rachasap modulation: divine subject → ทรง- (uniform); Boaz as elder/landowner → plain (no royal); narrator-female-village register; pronoun-table at every register-juncture (Ruth's ดิฉัน-ข้าพเจ้า escalation; Naomi's ฉัน; Boaz's ฉัน when speaking-to-Ruth, etc.). | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | See §11 above. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | See §12 above. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | All 15+ personal names + 4 place names + 10 Davidic-genealogy names verified — 1 cross-corpus drift (RUT 4:19 רָם / Mt 1:3-4 อารัม), already flagged at §7. | **LOCKED-with-§7-DECIDE** |
| `pagan_deities_2026-04.md` (NT corpus) | RUT 1:15 אֱלֹהֶיהָ (Moabite gods) → พระทั้งหลาย — does not use the reserved-for-YHWH พระเจ้า. The lock holds in OT-foreign-deity-plural context. | **LOCKED** |
| `adversary_speech_register_2026-05.md` | N/A — no adversary characters in Ruth (no Satan, no serpent, no foreign deities-as-speakers). The closer-kinsman of 4:1-8 is not an adversary-figure; he's a foil with normal human-register. | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | The ten elders at 4:2 — plain register; the village-women narrative voice at 1:19 + 4:14-17 — plain register. Boaz as landowner/elder addressed by Ruth: นายของดิฉัน (humble-deferential). Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal narrator-voice on YHWH; plain narrator on all human characters incl. Boaz. Pronoun-track per character-relation matches the ot_register_policy table. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative tense-system is wayyiqtol-based, not historic-present. Doc is Greek-NT-specific. | **LOCKED (N/A)** |
| `ekklesia_2026-04.md` | N/A — Hebrew קָהָל / עֵדָה not exercised in Ruth (the 4:11 reference to "house of Israel" uses בֵּית, not קָהָל). | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — no תָּשׁוּב / נָחַם repentance-vocabulary in Ruth (Naomi's lament is not a repentance-speech-act). | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — no סָלַח / כִּפֶּר forgiveness-vocabulary in Ruth. | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | N/A — no שָׁמַיִם heaven references in Ruth. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — Christological NT title. | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative-of-deity in Ruth (no prayer-to-YHWH; Naomi's lament is to the village, not vocatively to YHWH). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | RUT 4:14 בָּרוּךְ יהוה ("blessed/praised be YHWH") → ทรงเป็นที่สรรเสริญ. Compliant per the doc's narrator-doxological pattern. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic embeds in Ruth. | **LOCKED (N/A)** |
| `johannine_doubled_amen_2026-04.md` | N/A — Johannine-Greek pattern. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | N/A — no Tier 1/2/3 inclusion variants in Ruth per RULES §0 OT text-base policy. The 3:15 וַיָּבֹא vs וַתָּבֹא variant is silently followed (MT-masculine, matching BSB/ESV/NIV) per the 3:15 KD; not a Tier 1/2/3 case under RULES §5. | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | RUT 1:15 — see above. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 4/4 chapters: `output/check_reports/ruth_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 4/4 chapters: `output/back_translations/ruth_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 130-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: untracked OT-extension check artifacts only:
  - `output/check_reports/claim_consistency_ruth_01.md`
  - `output/check_reports/honorifics_binding_ruth_01.md` + `ruth_04.md`
  - `output/check_reports/ot_citations_ruth_0[1-4].md`
  These are W1 Day 9-11 newly-added OT checks (PR #113 `15c9bc4`); they were not part of the per-chapter ship-script's auto-commit set when RUT 1-4 shipped. **Action:** include these in the audit branch's ship batch — they constitute the OT-specific check coverage for the audit's mechanical evidence.

---

## Pre-existing docs affirmed / unchanged

All 52 docs in `docs/translator_decisions/` reviewed. Compliance per §14 above. **No NT-corpus doc requires amendment from Ruth's data alone.** The 9 OT-specific docs landed in W1 are validated by Ruth's exercise — they hold without revision.

---

## Flagged for Ben's attention

### A. RUT 1:13 anthropomorphism — ทรง-on-body-part rule — **DECIDE before tagging** (§4)
Lock the implicit Ruth 1:13 rule (royal-Thai prefix on body-part; plain verb when subject is body-part-of-divine-person) into a corpus doc before Exod 7 + Pss + Isaiah's anthropomorphism-density. New doc recommended: `divine_anthropomorphism_thai_grammar_2026-05.md`.

### B. RUT 3:9 כָּנָף verbal-echo flatness — **DECIDE** (§6)
Choose between (a) accept surface-flatness with thai_summary unpacking; (b) force ปีก back into 3:9 main text; (c) restructure 2:12. Recommend (a) + flag for external AI reviewer attention. Theological literature is divided; Thai-language reviewer's voice critical.

### C. RUT 4:19 רָם / Mt 1:3-4 อารัม cross-corpus normalization — **DECIDE** (§7)
Pick (a) Hebrew-form wins (ราม corpus-wide); (b) Greek-form wins (อารัม corpus-wide); (c) tolerate divergence with doc. Compounds into the broader OT-Hebrew/NT-Greek transliteration question for shared genealogical names. New doc recommended: `cross_corpus_name_normalization_2026-05.md`.

### D. RUT 1:6 פָקַד pastoral-care vs other senses — **REVIEW + new doc** (§5a)
Confirm ทรงเยี่ยมเยียน vs ทรงเหลียวแล (Thai-language reviewer voice) + lift to corpus-doc with sense-table before 1 Samuel 2. New doc recommended: `paqad_visit_attend_2026-05.md`.

### E. RUT 1:9 מְנוּחָה vs RUT 3:1 מָנוֹחַ register split — **REVIEW** (§5b)
Confirm the gendered-form split (abstract-feminine מְנוּחָה → ความสงบมั่นคง vs concrete-masculine מָנוֹחַ → ที่พักพิง). Defensible; worth Thai-language-reviewer endorsement before the Pss "rest"-cluster.

### F. RUT 1:19 הוּם → แตกตื่น vs ฮือฮา — **REVIEW** (§8)
Thai-language reviewer choice. The translator surfaced this open in the KD — defer to reviewer.

### G. New corpus docs to write (before next OT book)
1. **`docs/translator_decisions/chesed_covenant_love_2026-05.md`** (§2) — locks ความรักมั่นคง before Pss
2. **`docs/translator_decisions/goel_kinsman_redeemer_2026-05.md`** (§3) — locks ญาติผู้ไถ่ before Job 19, Isa 41-43, Pss
3. **`docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md`** (§4) — Ben to decide; locks ทรง-on-body-part principle before Exod-Pss
4. **`docs/translator_decisions/hebrew_oath_formulas_2026-05.md`** (§10) — locks Ruth 1:17 + 3:13 forms before Sam-Kgs (25 חַי־יהוה occurrences in Sam-Kgs alone)
5. **`docs/translator_decisions/paqad_visit_attend_2026-05.md`** (§5a) — sense-table for the 300-occurrence lemma

### H. Existing docs to amend
- **`proper_names_and_transliteration_2026-05.md`** — add Ruth's full name-set (already covered by THSV11-baseline rule, but worth listing the Ruth-genealogy names + flagging the §7 Ram cross-corpus question for reviewer attention)
- (No NT-corpus doc requires amendment from Ruth alone)

### I. External AI review (§3 of checklist) — **pending**
Recommended before `book-ruth-v1` tag. Suggested 4-cluster external AI packet:
1. **RUT 1:6–18** — Ruth's covenant declaration + first OT YHWH convention + chesed first-occurrence + the death-oath formula + the kī-asseverative drift question
2. **RUT 1:19–22** — Naomi/Mara wordplay + Shaddai introduction + רֵיקָם empty-hand verbal thread setup + the הוּם stir-verb question
3. **RUT 2:8–17** — Boaz's protection-and-provision speech + 2:12 wings-of-YHWH + 2:13 nay-of-deshim + the chen-be'eney threefold favor-thread
4. **RUT 3:9–17 + 4:11–14** — the wings-wordplay pivot + the gō'ēl-and-marriage legal frame + the elders' Rachel-Leah-Tamar-Perez blessing + the Davidic genealogy resolution

Use Gemini 2.5 Pro + ChatGPT in parallel per the JHN/ACT pattern.

---

## Recommendation

**Ruth ships in strong corpus-hygiene shape — and the OT-specific lock-set landed in W1 (`divine_names_table`, `ot_register_policy`, `hebrew_grammar_transfer`, `hebrew_idioms_and_metaphor`, etc.) holds without revision after first-OT-book exercise.** Two structural improvements to lock in before Jonah ships:

1. **Five new OT corpus docs** (chesed, go'el, anthropomorphism, oath-formulas, paqad) — items §G1–§G5 above. Each has a high forward-load; locking now prevents drift across Pss/Sam-Kgs/Prophets/Job.

2. **Cross-corpus name-form policy** (§7) — Ben's call (a/b/c). The Ram instance is the first concrete trigger; the rule will recur dozens of times across Phase 6D (Former Prophets).

Tag `book-ruth-v1` after:
1. Ben's decisions on **§A + §B + §C** (DECIDE items: ทรง-on-body-part rule; כָּנָף wordplay; Ram normalization)
2. Ben's confirmations on **§D + §E + §F** (REVIEW items: paqad sense + מְנוּחָה split + הוּם verb — likely awaiting Thai-language reviewer voice)
3. Five new translator_decisions docs written (§G items 1-5; some may be deferred until after Jonah if scope-budget tight, but chesed + go'el are critical pre-Pss)
4. External AI sanity-check (§I)
5. The newly-added OT-extension check reports (output/check_reports/ot_citations_ruth_*, honorifics_binding_ruth_*, claim_consistency_ruth_01.md) committed alongside this audit

The book's central theological-narrative arc (foreigner-Moabite-Ruth's ḥesed → Davidic-line → NT-cross-reference Mt 1:5) is preserved with cross-corpus consistency. **Ruth is ready to be the OT-pilot template — pending the locks above.**
