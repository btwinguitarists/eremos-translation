# Jonah — End-of-Book Review

**Date:** 2026-05-09
**Scope:** All 4 chapters (48 verses MT / 48 verses BSB; 130+ verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (60 docs incl. the OT-extension docs landed in W1 + the post-Ruth audit recommendations).
**Trigger:** JON 4 shipped (commit `c68b961`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Second OT book in the corpus** (after Ruth).
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 4/4 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-134-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/`: two newly-generated JON 4 OT-extension artifacts untracked (`output/check_reports/honorifics_binding_jonah_04.md` clean ✅; `output/textual_variants/jonah_04.json` containing 3 reader-edition entries) — these are produced by the JON 4 ship pass but were not picked up by the auto-commit in the `c68b961` ship; **action**: include both in the audit branch's commit batch.
- **Jonah is the SECOND OT book** (after Ruth) and the **first OT prophetic-narrative**. The OT-specific lock-set landed in W1 (`divine_names_table_2026-05`, `ot_register_policy_2026-05`, `hebrew_grammar_transfer_2026-05`, `hebrew_idioms_and_metaphor_2026-05`, `verse_schema_and_versification_2026-05`, `proper_names_and_transliteration_2026-05`) was exercised again here. The book also exercises five distinctively prophetic-narrative patterns not present in Ruth: divine-appointment leitmotiv (מָנָה ×4); divine relenting (נִחַם ×3); the Exod 34:6–7 attribute-formula echo (with Jonah-specific addendum); pagan-conversion register-arc (sailors, ch.1; Ninevites, ch.3); and the ירד-downward death-trajectory leitmotiv (chs.1–2).
- **9 inherited NT-corpus locks verified compliant** in JON (Tetragrammaton-as-`องค์พระผู้เป็นเจ้า`, OT-register policy, divine-object-praise verbs, narrator-vs-character voice, Hebrew-idiom transfer, narrator-Adonai split, honorifics, pagan-deities register, anthropomorphism rule from RUT 1:13).
- **3 cross-cutting OT-distinctive patterns are STABLE-and-locked** at corpus level (Tetragrammaton convention with per-chapter footer note — 4/4 chapters; OT-register policy on divine speech ทรง-/เรา/เจ้า; Hebrew-idiom-transfer applied to "presence-of-YHWH" + "before me" + cognate-accusative-fear).
- **5 items flagged STABLE-but-undocumented** (recommend new corpus docs): מָנָה divine-appointment lock (4 occurrences in JON alone, ~300 OT total); נִחַם divine-relenting theology (3 in JON, ~30 OT — the Numbers 23:19 ↔ Joel 2:13 ↔ Jonah 4:2 cluster); Exod-34:6–7 attribute-formula corpus tracker; verbal-leitwort handling policy (when a Hebrew lemma recurs deliberately); and a chesed corpus-doc lift from Ruth (now urgent — see §2).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-or-Thai-reviewer's confirmation: JON 1:4 טוּל-leitmotiv blunting via ทรงบันดาล vs โยน; JON 4:6 קִיקָיוֹן botanical identity = ต้นน้ำเต้า/gourd; JON 1:6 captain's אֱלֹהִים → พระเจ้า register-pre-conversion).
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-jonah-v1`: **JON 4:2 chesed cross-corpus drift** — ทรงบริบูรณ์ด้วยพระเมตตาเชิงพันธสัญญา vs Ruth's ความรักมั่นคง lock; **JON 4:11 right-hand/left-hand interpretive crux** — children-vs-morally-ignorant ambiguity preserved in main text + reader-edition footnote, but the population-arithmetic implication is not accessible to a typical Thai reader).
- **External AI review (§3) pending.** Suggested 4-cluster packet at the end.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's-or-Thai-reviewer's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה — corpus-wide rendering + per-chapter footer convention — **LOCKED**

19 occurrences across the 4 chapters, all uniform **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md`. Layer 1 (per-verse KD-citation) + Layer 2 (per-chapter first-occurrence footer note in `output/textual_variants/jonah_NN.json`) both exercised; PR #131 / #132 / #133 added the chapter-by-chapter footer notes.

| Chapter | Verses with יהוה | Count | Layer 2 footer |
|---|---|---|---|
| 1 | 1:1, 1:2, 1:3 (×2), 1:6, 1:9, 1:14, 1:16 | 8 | ✓ at 1:1 (PR #131) |
| 2 | 2:1, 2:2, 2:3 | 3 | ✓ at 2:1 (PR #132) — also versification-map note (MT 2:1 = BSB 1:17) |
| 3 | 3:1, 3:2, 3:3, 3:9 (×implied), 3:10 | 4 | ✓ at 3:1 (PR #133) — also divine-anthropomorphism note for נִחַם |
| 4 | 4:2, 4:4, 4:10 | 3 | ✓ at 4:2 (this audit branch) |
| **also: יְהוָה־אֱלֹהִים compound at 4:6** | (rare biblical compound; only in JON 4:6 within this book; see §11) | 1 | n/a |

**Editorial assessment:** The NT-aligned vocabulary lock (matching the 22 shipped NT books rendering κύριος-as-YHWH) holds without exception. The Hebrew-form transparency mechanism (Layer 1 KD per verse + Layer 2 first-occurrence footer per chapter) is exercised correctly in all four chapters. The reversibility clause in `divine_names_table_2026-05.md` (find-replace migration to `พระยาห์เวห์` if Thai reader feedback prefers historical-transliteration) remains open without any per-verse cost. Compound יְהוָה־אֱלֹהִים at 4:6 is rendered **องค์พระผู้เป็นเจ้าพระเจ้า** (concatenation) — a transparent join that preserves both lexemes and matches the doc's Genesis-2 echo treatment.

**LOCKED** ✓ — no action.

---

## 2. חֶסֶד (chesed) — Ruth-Jonah cross-corpus drift — **DECIDE before tagging**

Two חֶסֶד occurrences in Jonah, with **two different Thai renderings** — neither matching Ruth's lock:

| Verse | Hebrew | Thai (current) | Comment |
|---|---|---|---|
| JON 2:9 | חַסְדָּם יַעֲזֹבוּ | **พระเมตตาที่พวกเขาควรได้รับ** ("the mercy they should receive") | Ambiguous-suffix-resolved per BSB/ESV/NIV — unpacked into a relative clause; lemma flattened to plain พระเมตตา |
| JON 4:2 | וְרַב־חֶסֶד | **ทรงบริบูรณ์ด้วยพระเมตตาเชิงพันธสัญญา** ("abounding in covenant-mercy") | Compound rendering; "covenant-dimension" qualifier inserted to mark the technical sense |

**Compare Ruth's lock** (per RUT end-of-book audit §2, 2026-05-05):

| Verse | Hebrew | Thai (Ruth) |
|---|---|---|
| RUT 1:8 | יַעַשׂ יְהוָה ... חֶסֶד | **ขอองค์พระผู้เป็นเจ้าทรงสำแดงความรักมั่นคง** |
| RUT 2:20 | (אֲשֶׁר) לֹא־עָזַב חַסְדּוֹ | **ผู้ไม่ทรงละทิ้งความรักมั่นคงของพระองค์** |
| RUT 3:10 | הֵיטַבְתְּ חַסְדֵּךְ הָאַחֲרוֹן מִן־הָרִאשׁוֹן | **ความรักมั่นคงของเจ้า...** |

**Editorial assessment:** Ruth's audit recommended a corpus-doc lift (`docs/translator_decisions/chesed_covenant_love_2026-05.md`) "before Pss" but the doc was not yet written when Jonah shipped. Result: **Jonah drifted on the second OT-book exercise of the lemma**, splitting it into two new renderings (พระเมตตา at 2:9; พระเมตตาเชิงพันธสัญญา at 4:2). The 2:9 rendering is partially defensible — "their chesed" was unpacked into "the mercy they should receive" as an interpretive choice on the suffix-pronoun crux (option-1 reading per BSB/ESV/NIV), and the lemma's covenant-dimension is implicit in the divine-source. The 4:2 rendering is a single-verse compound (เชิงพันธสัญญา) that surfaces the technical sense for the Exod-34 attribute-formula context.

But: **the Ruth-Jonah cross-corpus consistency is broken.** A Thai reader working through Pss alongside Jonah will see three different chesed renderings (ความรักมั่นคง / พระเมตตา / พระเมตตาเชิงพันธสัญญา) with no transparent mapping back to the single Hebrew lemma.

**DECIDE before tagging:** Ben choice between four resolutions:

(a) **Ruth lock wins** (ความรักมั่นคง at JON 2:9 + 4:2). Re-translate JON 2:9 + 4:2 in this audit branch. Argument: cross-corpus consistency is the foundational OT-translation hygiene principle; Ruth shipped first, locked first, wins. The 4:2 attribute-formula is precedented at Pss 86:15, 103:8, 145:8 (~6 more occurrences) — locking ความรักมั่นคง now prevents drift across the formula.

(b) **Jonah-context wins** (Ruth's ความรักมั่นคง + Jonah's contextual π้องเมตตาเชิงพันธสัญญา preserved as principled-divergence). Argument: the 4:2 attribute-formula has a covenant-revelation force (Exod-34 echo) that ความรักมั่นคง alone may not signal to Thai readers; the contextual qualifier helps. But this means writing a corpus-doc that names BOTH renderings as legitimate, with verse-level guidance.

(c) **New unified rendering** that improves on both — e.g., **พระคุณมั่นคง** (royal-mercy + steadfast) or **ความเมตตาแห่งพันธสัญญา** (covenant-mercy noun-phrase). Recommend: only if Ben + Thai-language reviewer judge the existing options inadequate; cost is re-touching Ruth and re-translating JON.

(d) **Defer to a chesed corpus doc** (`docs/translator_decisions/chesed_covenant_love_2026-05.md`) and lock the chosen rendering there, then back-port to JON 2:9 + 4:2 if needed.

**Recommend (a) + new corpus doc** (option d as the implementation mechanism). The 4:2 attribute-formula will recur 6+ times across the Hebrew Bible (Exod 34:6, Num 14:18, Pss 86:15, 103:8, 145:8, Joel 2:13, Nah 1:3, Neh 9:17, 2 Chr 30:9 — see §3 below); locking now prevents 8-way drift later.

**→ Recommend new doc:** `docs/translator_decisions/chesed_covenant_love_2026-05.md` — locks ความรักมั่นคง as the corpus-default for חֶסֶד, names Jonah's two-rendering drift as a corrected precedent, cites RUT 1:8 + the JON 4:2 attribute-formula as joint locking-precedents for the corpus-wide rendering. Document the Pss-priority-list (Ps 23, Ps 86, Ps 103, Ps 136, Ps 145) and the Exod 34 mother-formula.

---

## 3. Exodus 34:6–7 attribute formula at JON 4:2 — **STABLE (recommend new doc)**

Jonah 4:2 contains the most compact **OT-internal echo of the Sinai self-revelation** (Exod 34:6–7) outside the Pentateuch itself, with a deliberate Jonah-specific addendum (וְנִחָם עַל־הָרָעָה — "one who relents from the calamity"). The formula is among the OT's most theologically-quoted verses — 7 OT cross-references catalogued in the textual_variants entry:

| Component | Hebrew | Thai (current) | Notes |
|---|---|---|---|
| God-formula | אֵל | **พระเจ้า** | Plain divine-noun (not the compound El-anything title) |
| Gracious | חַנּוּן | **ผู้ทรงพระคุณ** | Royal-Thai adj. ทรงพระคุณ |
| Compassionate | רַחוּם | **ทรงพระเมตตา** | Royal-Thai adj. (**See §2** — same rendering as the chesed lemma at 2:9; potential lemma-confusion) |
| Slow to anger | אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | Idiomatic Thai for "long-of-nostrils" — natural Thai idiom; preserves the slow-anger sense |
| Abounding in chesed | וְרַב־חֶסֶד | **ทรงบริบูรณ์ด้วยพระเมตตาเชิงพันธสัญญา** | See §2 — diverges from RUT lock |
| Relenting from calamity | וְנִחָם עַל־הָרָעָה | **ทรงเปลี่ยนพระทัยจากการลงโทษ** | **Jonah-specific addendum NOT in Exod 34** — preserves the prophet's protest-rhetoric |

**Editorial assessment:** The formula's Thai rendering is principled and theologically rich. Two corpus-level concerns:

1. **חַנּוּן vs רַחוּם — both surface as ทรงพระเมตตา/ทรงพระคุณ in Thai but the lemmata are distinct in Hebrew** (חַנּוּן ≈ "graciously favoring" → ทรงพระคุณ; רַחוּם ≈ "compassionately moved" → ทรงพระเมตตา). The Thai split (พระคุณ vs พระเมตตา) is reasonable but does not fully transfer the Hebrew etymological force (חנן = "stoop down to grant"; רחם = "womb-pity"). Future Pss occurrences (esp. Ps 86:15, 103:8 where the formula recurs verbatim) will need to align identically — the rendering established here becomes the corpus-default.

2. **רַחוּם → ทรงพระเมตตา + חֶסֶד → พระเมตตา (at 2:9) creates lemma-overlap.** A Thai reader cannot distinguish רַחוּם-mercy from חֶסֶד-mercy by surface lexeme; both surface as พระเมตตา. The Ruth-lock ความรักมั่นคง for חֶסֶด would resolve this overlap if applied here (see §2).

**→ Recommend new doc:** `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` — locks the 6-component formula's Thai rendering before its 7+ recurrences in Pss/Joel/Nah/Neh/2 Chr. Ruth+Jonah are the only OT books shipped that have any of the components; lock here. Cite JON 4:2 as the locking precedent for the full formula and the addendum.

---

## 4. נִחַם (divine relenting / "change of mind") — divine-repentance theology — **STABLE (recommend new doc)**

Three occurrences in Jonah; uniform Thai rendering **ทรงเปลี่ยนพระทัย** ("change [royal] mind") preserves the OT anthropomorphism literally per `hebrew_idioms_and_metaphor_2026-05.md` §1.4:

| Verse | Hebrew | Thai | Speaker | Theological force |
|---|---|---|---|---|
| JON 3:9 | יָשׁוּב וְנִחַם הָאֱלֹהִים | **พระเจ้าอาจจะทรงหันและเปลี่ยนพระทัย** | Ninevite king (cautious hope) | conditional-hope formula |
| JON 3:10 | וַיִּנָּחֶם הָאֱלֹהִים עַל־הָרָעָה | **พระเจ้าจึงทรงเปลี่ยนพระทัยเรื่องเหตุร้าย** | Narrator (factive) | divine-actual response |
| JON 4:2 | וְנִחָם עַל־הָרָעָה | **ทรงเปลี่ยนพระทัยจากการลงโทษ** | Jonah (citing Exod 34 + addendum, protest) | prophet's grievance-clause |

**Editorial assessment:** The literal-rendering policy holds — Thai readers face the same theological tension as Hebrew readers (vs. Num 23:19 לֹא אִישׁ אֵל וִיכַזֵּב וּבֶן־אָדָם וְיִתְנֶחָם "God is not a man that he should change his mind"; vs. 1 Sam 15:29 וְגַם נֵצַח יִשְׂרָאֵל לֹא יְשַׁקֵּר וְלֹא יִנָּחֵם). The mainstream evangelical reading (responsive-judgment is itself a stable covenant-feature, per Jer 18:7–10) is defensible; the Thai must preserve the surface-paradox to permit theological-explanation in a reader-edition footer.

PR #133 added a Layer-2 textual_variants note "divine-anthropomorphism note" at JON 3 — explicitly acknowledging the נִחַם anthropomorphism for reader-edition consumption. The mechanism is correct.

**→ Recommend new doc:** `docs/translator_decisions/nicham_divine_relenting_2026-05.md` — locks ทรงเปลี่ยนพระทัย as the corpus-rendering for divine-נִחַם before the prophetic books (Joel 2:13–14, Amos 7:3, 7:6, Jer 18:8, 18:10, 26:3, 26:13, 26:19, 42:10; cf. 1 Sam 15:29 + Num 23:19 counterpoints). The doc should:
1. Lock נִחַם (Niph'al, divine subject) → ทรงเปลี่ยนพระทัย
2. Distinguish from נִחַם applied to a human (= "console / be sorry") and from תָּשׁוּב (return/turn) — the JON 3:9 + 3:10 cluster shows שׁוּב + נִחַם as a hendiadys, not a distinct second action
3. Surface the apparent-paradox vs Num 23:19 / 1 Sam 15:29 explicitly + name the conditional-covenant resolution (Jer 18:7–10) as the mainstream evangelical reading
4. Cite JON 3:10 as the locking precedent (the only narrator-factive use in OT outside the Pentateuch's own counter-formulae)

---

## 5. מָנָה (divine appointment) — Jonah's signature leitmotiv — **STABLE (recommend new doc)**

Four divine-appointments in the book, all Pi'el of מָנָה ("appoint, prepare, ordain") with God as subject and a creature/object as direct object. Uniform Thai rendering **ทรงจัดเตรียม** ("royally prepare") at every occurrence:

| Verse | Subject | Object | Hebrew | Thai |
|---|---|---|---|---|
| JON 2:1 | יְהוָה | דָּג גָּדוֹל (great fish) | וַיְמַן יְהוָה דָּג גָּדוֹל | **องค์พระผู้เป็นเจ้าทรงจัดเตรียมปลาใหญ่** |
| JON 4:6 | יְהוָה־אֱלֹהִים | קִיקָיוֹן (qiqayon plant) | וַיְמַן יְהוָה־אֱלֹהִים קִיקָיוֹן | **องค์พระผู้เป็นเจ้าพระเจ้าทรงจัดเตรียมต้นน้ำเต้า** |
| JON 4:7 | הָאֱלֹהִים | תּוֹלַעַת (worm) | וַיְמַן הָאֱלֹהִים תּוֹלַעַת | **พระเจ้าทรงจัดเตรียมหนอนตัวหนึ่ง** |
| JON 4:8 | אֱלֹהִים | רוּחַ קָדִים (east wind) | וַיְמַן אֱלֹהִים רוּחַ קָדִים | **พระเจ้าทรงจัดเตรียมลมตะวันออก** |

**Editorial assessment:** The four-fold leitmotiv is the book's clearest narrative-design device. The Thai lock (ทรงจัดเตรียม at every occurrence) preserves the verbal echo perfectly — Thai readers can SURFACE-track the four divine appointments as Hebrew readers do. Note the **divine-name-shift across the four** (יהוה / יהוה־אלהים / האלהים / אלהים) — preserved transparently in the Thai (องค์พระผู้เป็นเจ้า / องค์พระผู้เป็นเจ้าพระเจ้า / พระเจ้า / พระเจ้า) without interpretive flattening; this is theologically significant (Jonah-as-Adam typology; Eden-Genesis-2 echo at 4:6 — see §11). 

**→ Recommend new doc:** `docs/translator_decisions/manah_divine_appointment_2026-05.md` (brief — single-Hebrew-lemma lock). The corpus-load for divine-מָנָה is moderate: Dan 1:5, 1:10, 1:11 (Daniel-court appointments); Job 7:3 (months of vanity); Ps 61:7 (appointed days). All can lock to ทรงจัดเตรียม at God-subject. Cite JON 2:1 as the locking precedent.

---

## 6. ירד "go down" — Jonah's death-trajectory leitmotiv — **STABLE**

Five "down" verbs across chapters 1–2 form a deliberate descending chain — the prophet's flight from God = downward motion toward death. Uniform Thai **ลง-** preserves the verbal echo:

| Verse | Hebrew | Thai | Direction-of-descent |
|---|---|---|---|
| JON 1:3a | וַיֵּרֶד יָפוֹ | **ท่านลงไปที่เมืองยัฟโฟ** | Galilean hills → coastal Joppa (geographic) |
| JON 1:3b | וַיֵּרֶד בָּהּ | **และลงเรือ** | dock → ship |
| JON 1:5 | יָרַד אֶל־יַרְכְּתֵי הַסְּפִינָה | **ได้ลงไปในส่วนล่างสุดของเรือ** | deck → hold |
| JON 2:7 | לְקִצְבֵי הָרִים יָרַדְתִּי | **ลงไปยังรากของภูเขาทั้งหลาย** | sea-surface → deep / mountain-roots (= cosmic underworld) |

Then v.7's וַתַּעַל ("but you brought up") reverses the descent — the divine rescue counter-verb. Thai **ทรงนำ...กลับมา** preserves the upward-counterpoint.

**Editorial assessment:** The KD at 1:3 explicitly names the leitmotiv and commits to **uniform ลง-** rendering. Compliance is total. **STABLE** ✓ — no action.

(N.B.: there are also two narrative-neutral "down" verbs that are NOT part of the theological leitmotiv: 3:6 the Ninevite king "rose" וַיָּקָם from his throne; 4:5 Jonah "went out" וַיֵּצֵא from the city. These are correctly rendered without ลง.)

---

## 7. טוּל "hurl" — chapter 1 hurling-chain leitmotiv — **REVIEW (verb-divergence in Thai)**

The Hebrew root טוּל (Hiph'il / passive forms) recurs four times in chapter 1:

| Verse | Subject | Object | Hebrew | Thai |
|---|---|---|---|---|
| JON 1:4 | יהוה | רוּחַ גְּדוֹלָה | הֵטִיל | **ทรงบันดาลให้...พัดมา** ("caused to blow") |
| JON 1:5 | sailors | כֵּלִים (cargo) | וַיָּטִלוּ | **โยน** ("throw") |
| JON 1:12 | Jonah → sailors (imperative) | אֹתִי / נַפְשִׁי | הֲטִילֻנִי | **จับ...โยน** ("seize and throw") |
| JON 1:15 | sailors | יוֹנָה | וַיָּטִלוּ | **โยน** ("throw") |

**Editorial assessment:** The Hebrew narrator deliberately reuses טוּל across vv.4–15 — God hurls wind → sailors hurl cargo → sailors hurl Jonah. The thematic point: God's hurling of the wind initiates a chain that terminates in the sailors hurling Jonah; the prophet becomes the cargo. **The Thai breaks the verbal echo at v.4** (ทรงบันดาลให้...พัดมา — a causation-verb, not a hurling-verb). The 1:4 KD names the trade-off explicitly:

> "The Thai rendering ทรงบันดาลให้...พัดมา preserves the divine causation while reading naturally; the harsher 'ทรงโยน' would sound non-Thai-idiomatic for wind."

The judgment is principled — Thai โยน lit. = "throw [a discrete object]" and does not naturally apply to wind in modern Thai. But the cost is the lost verbal echo.

**REVIEW flag:** Confirm Ben endorses the 1:4 verbal-blunting. Alternatives:
- (a) **Current** — ทรงบันดาลให้ลม...พัดมา at 1:4; โยน at 1:5/12/15. Verbal echo broken but Thai natural.
- (b) **Force the echo** — ทรงโยนลมพายุใหญ่ลงสู่ทะเล at 1:4 (literal "hurled a wind into the sea"). Preserves verbal echo at the cost of Thai naturalness; modern Thai readers may pause on "hurl-a-wind" as un-idiomatic.
- (c) **Compromise** — keep 1:4 as ทรงบันดาล but add a chapter-level reader-edition note that names the four-fold hurling-chain in Hebrew. Verbal echo not surface-preserved but reader awareness restored.

The thai_literal field at 1:4 already preserves option (b) reading ("ทรงโยนลมใหญ่ลงสู่ทะเล") — the literal layer carries the lemma-link. Recommend **(a) + extend the chapter-level note (option c)** unless Ben prefers (b). Future leitwort decisions of this kind will recur (see §8 for the chesed pattern; see Genesis 12 לֵךְ-לְךָ; see Pss-Lamentations cognate-accusative patterns) — establishing a "leitwort handling policy" doc would help.

**→ Recommend optional new doc:** `docs/translator_decisions/leitwort_handling_policy_2026-05.md` — names the trade-off (Thai naturalness vs Hebrew verbal-echo preservation) and lists the per-case decision pattern. Cite JON 1:4 (ทรงบันดาล) and JON 4:6/7/8 (ทรงจัดเตรียม) as the contrastive precedents (one breaks the echo for naturalness; the other preserves the echo because Thai tolerates it). The document is meta — for translator-discipline, not reader-facing.

---

## 8. גָּדוֹל "great" — chapter-spanning attributive Leitmotiv — **STABLE**

The adjective גָּדוֹל recurs ~14 times in Jonah, attached to: Nineveh (1:2, 3:2, 3:3, 4:11), wind (1:4), storm (1:4, 1:12), fear (1:10, 1:16 — both as cognate-accusative יִרְאָה גְדוֹלָה), fish (2:1), evil/calamity (4:1), joy (4:6). The adjective is the book's surface-design rhetoric — almost everything Jonah encounters is "great."

| Cluster | Hebrew | Thai |
|---|---|---|
| Nineveh-the-great-city (4×) | הָעִיר הַגְּדוֹלָה | **นครใหญ่** (1:2) / **นครใหญ่ยิ่ง** (3:2, 3:3 — intensified per "great to God" qualifier) / **นครใหญ่** (4:11) |
| Wind / storm | רוּחַ גְּדוֹלָה / סַעַר גָּדוֹל | **ลมพายุใหญ่ / พายุร้ายแรง / พายุใหญ่** |
| Fear (cognate accusative ×2) | וַיִּירְאוּ ... יִרְאָה גְדוֹלָה | **กลัว / เกรงกลัว ... อย่างยิ่ง** (collapsed into adverb) |
| Fish | דָּג גָּדוֹל | **ปลาใหญ่** |
| Calamity | רָעָה גְדוֹלָה | **เหตุร้ายอย่างยิ่ง** |
| Joy | שִׂמְחָה גְדוֹלָה | **ดีใจอย่างยิ่ง** (collapsed into adverb) |

**Editorial assessment:** Where Thai grammar tolerates a free adjective (city, wind, fish), the rendering is uniform **ใหญ่**. Where Hebrew uses a cognate-accusative or noun-adjective chunk that Thai naturally compresses to verb+adverb (great-fear, great-joy, great-evil), the Thai uses **อย่างยิ่ง** ("greatly") as the natural Thai equivalent. This follows `hebrew_grammar_transfer_2026-05.md` §3 (cognate-accusative compression). The result: ใหญ่/ยิ่ง surface-thread is partially preserved but the lemma's percussive recurrence (14× in 48 verses!) is muted in Thai.

**STABLE** ✓ — the trade-off is principled and follows the existing OT-grammar doc. Recommend mentioning in the future `leitwort_handling_policy_2026-05.md` (§7) as a contrastive case where the lemma-recurrence is acceptable to attenuate.

---

## 9. Sailor + Ninevite conversion register-arc — pagan-to-monotheistic vocabulary shift — **STABLE**

Two parallel conversion-arcs use a pagan-to-YHWH register-shift mechanism:

### 9a. Sailors (chapter 1)

| Verse | Hebrew lemma | Thai | Register |
|---|---|---|---|
| 1:5 | אִישׁ אֶל־אֱלֹהָיו ("each to his god") | **แต่ละคนต่อพระของตน** | **plain พระ-** (pagan; not the reserved พระเจ้า) |
| 1:6 | יִתְעַשֵּׁת הָאֱלֹהִים ("the god may consider") | **พระเจ้าจะทรงคำนึงถึง** | **พระเจ้า** + ทรง- (elevated; see REVIEW below) |
| 1:14 | אָנָּה יְהוָה אַל־נָא ("O YHWH, please not") | **ข้าแต่องค์พระผู้เป็นเจ้า ขออย่า** | **YHWH covenant-name + formal supplication** |
| 1:16 | וַיִּזְבְּחוּ־זֶבַח לַיהוָה ("offered a sacrifice to YHWH") | **ถวายเครื่องบูชาแด่องค์พระผู้เป็นเจ้า** | **YHWH + cultic-vocabulary** |

The shift from **"his god" (พระของตน, polytheistic) → "the god" (พระเจ้า, monotheistic) → "YHWH" (covenant-name, full conversion)** is preserved in Thai with reasonable fidelity. **STABLE** ✓.

### 9b. Ninevites (chapter 3)

| Verse | Hebrew | Thai | Register |
|---|---|---|---|
| 3:5 | וַיַּאֲמִינוּ אֱלֹהִים ("believed God") | **เชื่อพระเจ้า** | First Thai use of **พระเจ้า** for the Ninevites' object-of-faith — the conversion-pivot |
| 3:8 | וְיִקְרְאוּ אֶל־אֱלֹהִים ("cry to God") | **ร้องเรียกต่อพระเจ้า** | Continued **พระเจ้า** register |
| 3:9 | יִתְעַשֵּׁת הָאֱלֹהִים | **พระเจ้าอาจจะทรงหัน** | "the god" → พระเจ้า (matches 1:6 captain pattern) |
| 3:10 | וַיַּרְא הָאֱלֹהִים | **พระเจ้าทรงทอดพระเนตร** | Narrator-factive; God-subject ทรงทอดพระเนตร (royal-eye verb) |

The Ninevites do NOT progress to addressing YHWH by covenant-name (unlike the sailors at 1:14, 1:16) — they convert to monotheistic "the God" but not to covenant-Israel-faith. This nuance is preserved by the Thai's **พระเจ้า**-only rendering (no upgrade to องค์พระผู้เป็นเจ้า). The narrator at 3:10 uses אֱלֹהִים (not יהוה) for the same reason. **STABLE** ✓.

---

## 10. JON 1:6 captain's אֱלֹהִים → พระเจ้า — pre-conversion register choice — **REVIEW**

The Ninevite ship-captain at 1:6 says **אוּלַי יִתְעַשֵּׁת הָאֱלֹהִים לָנוּ** ("perhaps the God will consider us"). Thai renders **พระเจ้า** (the reserved-for-YHWH form), not the plain **พระ-** (which the sailors' own pagan-prayer at 1:5 uses).

**The captain is a Phoenician polytheist, not a monotheist.** The Hebrew הָאֱלֹהִים here ("the gods" or "the deity-in-question") is articular but does not commit the captain to monotheism. Most modern translations (BSB "this God"; ESV "the god"; NIV "the god") preserve the ambiguity. The 1:6 KD (per Explore-agent extraction) frames the captain's language as "an unconscious deferential elevation — the captain is ascending from polytheistic frame toward monotheistic recognition (fully realized in vv.14–16)."

**Editorial assessment:** Thai **พระเจ้า** here does double duty — for the Thai reader, it can read either as "the captain hopefully invokes the Hebrew God" (which fits the story's irony — the captain unwittingly speaks of YHWH) or "the captain elevates his pagan deity-in-the-moment with a generic high-register term" (the surface meaning). The choice is principled but represents a register elevation not licensed by the Hebrew alone — the 1:5 sailors just-prayed-to-their-gods (พระ-, plain) are the same characters as the 1:6 captain.

**REVIEW flag:** Confirm Ben endorses the 1:6 elevation. Alternatives:
- (a) **Current** — พระเจ้า at 1:6, with the captain framed as unconsciously-elevating. Reader-friendly + theologically loaded.
- (b) **Match the 1:5 plain register** — render 1:6 as "บางทีพระจะทรง..." (plain พระ-) to align with the same character's same-character-group pagan-frame at 1:5. The 1:14/1:16 conversion-arc still works without 1:6's pre-emptive elevation.
- (c) **Use a transitional word** — เทพเจ้า ("deity," the pagan-deity-register lemma per `pagan_deities_2026-04.md`) at 1:6 for the captain's אֱלֹהִים. Distinguishes from 1:5's individual pagan-gods (พระของตน) and from 1:14's covenant-name. Three-step register progression.

This is genuinely Thai-language-reviewer territory. Recommend surfacing for external AI sanity-check + Thai-language reviewer endorsement.

---

## 11. יְהוָה־אֱלֹהִים compound at JON 4:6 — Genesis-2 / Eden echo — **STABLE (interpretive note)**

JON 4:6 is the **only** verse in the book where the compound divine name יְהוָה־אֱלֹהִים appears (cf. Gen 2–3 Eden narrative — 20× in those two chapters; otherwise rare in the OT). The Thai renders **องค์พระผู้เป็นเจ้าพระเจ้า** — a transparent concatenation that mirrors the Hebrew compound visually.

The 4:6 KD names the Genesis-2 echo and the **Jonah-as-Adam typology** (the prophet-as-first-man being instructed by Yahweh-Elohim about creation-and-mercy via a plant). The verse-level decision is principled.

**Editorial assessment:** Defensible. The Thai concatenation reads slightly awkward but transparently preserves both lexemes. **STABLE** ✓ — no action. If the future `divine_names_table_2026-05.md` polish includes a "compound-divine-name handling" subsection, JON 4:6 + RUT 1:21 (Shaddai) + 1 Sam-Kgs (אֲדֹנָי יְהוִה / יְהוִה אֲדֹנָי) will be the corpus-tracker locks.

---

## 12. JON 4:6 קִיקָיוֹן (qiqayon plant) — botanical-identity crux — **REVIEW**

The plant Jonah sits under at 4:6 (and that is destroyed at 4:7) is **קִיקָיוֹן** — a Hebrew lemma that occurs ONLY in Jonah 4 (5×, vv.6/7/9/10 + indirectly v.10's "son-of-night-begotten plant"). Centuries-long botanical debate:

| Tradition | Identification | Notes |
|---|---|---|
| LXX | κολοκύνθη ("gourd") | Standard Greek tradition; influenced Latin & European versions |
| Jerome / Vulgate | hedera ("ivy") | Sparked the famous Augustine-Jerome dispute (Augustine objected to Jerome changing the LXX gourd) |
| Modern Hebrew lexicons (BDB, HALOT) | castor-bean (Ricinus communis) | Botanical match: rapid growth + large palmate leaves casting shade |
| Some modern English translations | "vine" / "leafy plant" / "bush" | Avoids the species-specificity question |

**Current Thai:** **ต้นน้ำเต้า** ("gourd plant"), uniform across all 5 occurrences. Aligns with the LXX tradition. The 4:6 KD (per Explore-agent extraction) names the LXX precedent, the bottle-gourd's rapid-growth + shade-casting properties, and the hedera/Ricinus alternatives.

**Editorial assessment:** The choice is principled (LXX precedent + botanical fit + Thai naturalness — น้ำเต้า is a familiar Thai plant). The cost: Thai readers do not see the centuries-old interpretive debate. The reader-edition footnote at JON 4:6 in `output/textual_variants/jonah_04.json` does NOT currently mention the botanical-crux (it covers the divine-name compound, not the plant identity).

**REVIEW flag:** Should the reader-edition footnote at JON 4:6 add a botanical-crux note (LXX-gourd vs Jerome-ivy vs modern-castor-bean)? Recommend yes — adds scholarly transparency without changing the main-text rendering.

---

## 13. JON 4:11 right-hand-from-left interpretive crux — **DECIDE before tagging**

The book's closing rhetorical question hinges on the phrase **לֹא־יָדְעוּ בֵין־יְמִינוּ לִשְׂמֹאלוֹ** ("who do not know between their right hand and their left"). Two well-attested readings:

| Reading | Implication |
|---|---|
| (1) **Literal — children too young to distinguish left from right** (≈ ages 3–4) | Nineveh has 120,000 small children → total population 600,000+ (matches archaeological estimates of greater-Nineveh) |
| (2) **Metaphorical — morally ignorant** (do not know good from evil) | The 120,000 = the entire morally-undiscerning Ninevite adult population |

**Current Thai:** **ผู้ไม่รู้จักแยกแยะมือขวาจากมือซ้ายของตน** — preserves the literal Hebrew + permits both interpretations. The reader-edition footnote in `output/textual_variants/jonah_04.json` at v.11 (`type: interpretive_crux_footnote`) **explicitly names both readings** and states "ฉบับเอเรโมสรักษาความเป็นสองนัยของต้นฉบับฮีบรูไว้โดยแปลตรง ผู้อ่านสามารถพิจารณาเลือกความหมายได้เอง" ("Eremos preserves the dual-sense of the Hebrew by direct translation; the reader may choose between the meanings").

**Editorial assessment:** The dual-sense preservation strategy is principled and matches Hebrew Bible scholarship's mainstream position (the ambiguity is deliberate). Two concerns:

1. **The "Are children meant?" question is the climactic theological hinge of the book.** If reading (1), YHWH's mercy is for the genuinely-innocent (small children) plus a remnant of contextually-discerning adults. If reading (2), YHWH's mercy is for the genuinely-guilty (morally-undiscerning adults who chose wrong). The two readings have very different theological force, and the book's closing line either lands as "mercy for innocents" or "mercy for the guilty" — these are not equivalent.

2. **The reader-edition footnote is currently buried in `output/textual_variants/jonah_04.json`** — a Layer-2 mechanism that may or may not surface in the final reader edition (depends on Eremos rendering layer). If it doesn't surface visibly, Thai readers will default to the literal-children reading (the surface Thai unambiguously says "people who don't know how to distinguish their right hand from their left" — which most Thai readers will read as a description of small children, not of moral-ignorance).

**DECIDE before tagging:** Three resolution paths:

(a) **Current** — surface-literal Thai + reader-edition footnote covering both readings. Defaults to children-reading for Thai readers; theological-reviewer or scholarly reader can use the footnote to access the moral-ignorance reading.

(b) **Lift the moral-ignorance reading into the main text** — render 4:11 with an interpretive paraphrase like "ผู้ที่ไม่รู้ผิดชอบดีชั่ว" ("who do not know right-from-wrong"). Locks the moral-ignorance reading into the main text; loses the surface dual-sense.

(c) **Surface-literal main text + an inline parenthetical note** — render as current Thai + add `(หมายถึงเด็กเล็ก หรือผู้เขลาทางศีลธรรม)` ("meaning either small children or the morally-ignorant") as an inline parenthetical. Surfaces the ambiguity directly to the reader without requiring them to find a footnote.

**Ben to decide.** Recommend (a) + ensure the textual_variants reader-edition footnote actually surfaces in the final Eremos rendering layer (this is an Eremos rendering verification, not a translation change). The 4:11 closing question's theological force depends on the reader being aware that BOTH readings are present in the Hebrew — without surfacing, the book's climax flattens into "mercy for innocents" (which is exactly the OT-cliché Jonah subverts).

---

## 14. Versification — MT 2:1 = English 1:17 — **LOCKED**

Hebrew MT places the great-fish verse at **2:1** (וַיְמַן יְהוָה דָּג גָּדוֹל); English versions (BSB/ESV/NIV) renumber it as **1:17** so the prayer-poem starts at chapter 2 verse 1 in English. The Thai follows MT (per `verse_schema_and_versification_2026-05.md` and the project's OT MT-baseline). 

PR #132 added the versification map note to `output/textual_variants/jonah_02.json` (Layer-2 entry, type `versification_map`) explicitly explaining the divergence to readers comparing with English Bibles.

**LOCKED** ✓ — the per-chapter Layer-2 reader-edition note is present and correct.

---

## 15. Inherited corpus locks — **all compliant**

| Doc | JON evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | 19 YHWH (§1) + 1 יְהוָה־אֱלֹהִים (4:6, §11) + ~10 אֱלֹהִים (3:5, 3:8, 3:10, 4:6, 4:7, 4:8, 4:9 — narrator/character voices distinguished). Layer 1 + Layer 2 mechanisms exercised in all 4 chapters. | **LOCKED** |
| `ot_register_policy_2026-05.md` | Divine-speech ทรง-/เรา/เจ้า throughout (1:2 YHWH-to-Jonah; 4:4, 4:9, 4:10–11 YHWH-to-Jonah diagnostic-questions). Foreign-emperor (Ninevite king at 3:6–7) takes ทรง- per §2.2 narrator-dignification rule. Pagan-sailors plain register; Jonah-to-pagan-sailors = ท่าน peer-respectful. Compliant. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol-chains (1:1, 1:3, 2:1, 3:1, 4:1) handled per doc; וַיְהִי opener at 1:1 (prophetic-formula preserved); cognate-accusative compressions at 1:10/16 fear-doublings (§8); infinitive-absolute intensifications at 4:9 (קָצַף הֵיטֵב "very angry / well-angry"). Compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | "לְפָנָי / מִלִּפְנֵי יהוה" → ต่อหน้าเรา / เบื้องพระพักตร์ (1:2, 1:3 ×2, 2:5); "yad-of-YHWH" not present; "raised-up evil came up before me" preserved as agriculture/altar-rising metaphor (1:2). Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | MT 2:1 = English 1:17 versification documented + Layer-2 footer note added (§14). Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | โยนาห์ (Jonah), อามิทัย (Amittai), นีนะเวห์ (Nineveh), ทารชิช (Tarshish), ยัฟโฟ (Joppa — note: NT Acts 9:36 etc. uses ยัฟปา; OT-NT divergence flagged at JON 1:3 KD; same class as RUT 4:19 רָם/Mt 1:3-4 อารัม cross-corpus normalization issue). | **LOCKED-with-cross-corpus-note** (see RUT audit §7) |
| `pagan_deities_2026-04.md` (NT-corpus, OT-extension) | Sailors' "his god" (1:5) → พระของตน (plain, not the reserved พระเจ้า). Compliant. The 1:6 captain's אֱלֹהִים → พระเจ้า is a register-elevation issue (see §10) — not a violation of the lock but worth Ben's review. | **LOCKED-with-§10-REVIEW** |
| `narrator_vs_character_voice_2026-04.md` | Narrator royal-Thai for YHWH/God-acts; characters' speech-register varies per character (sailors plain; Ninevite king dignified ทรง-; Jonah's first-person to YHWH is humble ข้าพระองค์ + addressing-YHWH-as-พระองค์/ทรง-). Compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | JON 1:16 וַיִּזְבְּחוּ־זֶבַח לַיהוָה ("offered sacrifice to YHWH") → ถวายเครื่องบูชา (formal-sacrificial verb, ถวาย royal). Compliant per the doc's altar-vocabulary pattern. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | The Ninevite king (3:6–7): ทรง- prefix on royal acts (rose from throne, took off robe, sat in ashes) — narrator dignifies office per Ruth-2:1+precedent. The ship-captain (1:6): plain register for the human role + the elevated speech-act addressed-to-deity uses พระเจ้า (see §10). Compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` (RUT-recommended; doc not yet written per Ruth audit §G3) | Body-part-of-divine-subject: "presence/face-of-YHWH" (1:2, 1:3 ×2, 2:5) → เบื้องพระพักตร์ / พระเนตร (royal-Thai noun) + plain verb. Anthropomorphic divine-actions: ทรงเปลี่ยนพระทัย (3:9, 3:10, 4:2 — body-part as object of verb, ทรง- on the action-verb). Compliant with the implicit Ruth-1:13 rule. **JON validates RUT's recommended principle for the second time; new doc still not written; recommend writing now (see §17).** | **LOCKED-pending-doc** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative tense is wayyiqtol; doc is Greek-NT-specific. | **LOCKED (N/A)** |
| `ekklesia_2026-04.md` / `ethnos_2026-04.md` | N/A — Greek vocabulary; not exercised in OT. | **LOCKED (N/A)** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic in Jonah. | **LOCKED (N/A)** |
| `johannine_doubled_amen_2026-04.md` / `son_of_man_disambiguation_2026-04.md` / `markan_euthys_immediately_2026-04.md` / etc. | N/A — Greek-NT-specific. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | N/A — no Tier 1/2/3 inclusion variants in Jonah per RULES §0 OT text-base policy. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — Greek lemmata. (The OT counterpart נִחַם is divine-relenting in Jonah; see §4. The human-repentance שׁוּב at 3:8/10 is rendered หันกลับ — does not collide with the Greek metanoeo lock.) | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — Greek lemma; OT counterparts סָלַח / כָּפַר not exercised in Jonah. | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | JON 1:9 אֱלֹהֵי הַשָּׁמַיִם ("God of heaven") → พระเจ้าแห่งฟ้าสวรรค์ — uses the Hebrew-OT compound noun ฟ้าสวรรค์, consistent with the doc's "compound heaven-noun" guidance. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 4/4 chapters: `output/check_reports/jonah_NN_review.md` + sub-reports ✓
- 4/4 chapters: `output/back_translations/jonah_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 134-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: 2 untracked files generated during the JON 4 ship pass:
  - `output/check_reports/honorifics_binding_jonah_04.md` (clean ✅, 0 violations)
  - `output/textual_variants/jonah_04.json` (3 reader-edition entries: tetragrammaton-first-occurrence + Exod-34 echo + 4:11 interpretive-crux)
  
  Both are produced by the JON 4 ship pass but were not picked up by the auto-commit in `c68b961`. **Action:** include both in the audit branch's commit batch (the equivalent of the Ruth-audit's OT-extension-artifact pickup at audit time).

---

## Pre-existing docs affirmed / unchanged

All 60 docs in `docs/translator_decisions/` reviewed. Compliance per §15 above. **No pre-existing doc requires amendment from Jonah's data.** Ruth's audit recommended writing 5 new corpus docs (chesed, go'el, anthropomorphism, hebrew-oath-formulas, paqad); of these, only **chesed** and **anthropomorphism** are exercised by Jonah — both validate the Ruth recommendations and are now urgent (see §17).

---

## Flagged for Ben's attention

### A. JON 4:2 chesed cross-corpus drift — **DECIDE before tagging** (§2)
Ruth-Jonah inconsistency: ความรักมั่นคง (RUT) vs พระเมตตา / พระเมตตาเชิงพันธสัญญา (JON). Recommend (a) Ruth-lock wins + (b) write the chesed corpus doc + (c) re-translate JON 2:9 + 4:2 in this audit branch. Critical before Pss/Joel/Nah etc. ship.

### B. JON 4:11 right-hand/left-hand interpretive crux — **DECIDE before tagging** (§13)
Confirm whether the dual-sense preservation strategy is theologically adequate, OR whether the closing climactic-line warrants an inline parenthetical that surfaces the children-vs-morally-ignorant ambiguity directly to the Thai reader. Verify the textual_variants reader-edition footnote actually surfaces in the final Eremos rendering layer.

### C. JON 1:4 טוּל-leitmotiv blunting — **REVIEW** (§7)
Confirm Ben endorses the ทรงบันดาล (causation) at 1:4 vs the verbal-echo-preserving ทรงโยน (literal hurling). Defensible; worth Thai-language reviewer voice. If accepted, recommend writing the meta-doc `leitwort_handling_policy_2026-05.md` to lock the trade-off principle for future leitwort decisions.

### D. JON 4:6 קִיקָיוֹน botanical-identity reader-edition note — **REVIEW** (§12)
Add a botanical-crux footnote at JON 4:6 in `output/textual_variants/jonah_04.json` (LXX-gourd vs Jerome-ivy vs modern-castor-bean). Adds scholarly transparency without changing main text. Editorial decision only — not a translation change.

### E. JON 1:6 captain's אֱלֹהִים → พระเจ้า register-elevation — **REVIEW** (§10)
Confirm the captain's pre-conversion elevation to พระเจ้า (vs matching 1:5 sailors' plain พระ-). Thai-language-reviewer territory.

### F. New corpus docs to write (before next OT book)
1. **`docs/translator_decisions/chesed_covenant_love_2026-05.md`** (§2) — locks ความรักมั่นคง; carries Ruth-Jonah cross-corpus consistency through Pss/Joel/Nah. **CRITICAL — depends on §A decision.**
2. **`docs/translator_decisions/exod_34_attribute_formula_2026-05.md`** (§3) — locks the 6-component formula's Thai before Pss 86/103/145, Joel 2:13, Nah 1:3, Neh 9:17, 2 Chr 30:9.
3. **`docs/translator_decisions/nicham_divine_relenting_2026-05.md`** (§4) — locks ทรงเปลี่ยนพระทัย before Joel 2:13, Amos 7:3+6, Jer 18:8/10, 26:3+13+19, 42:10; surfaces the Num 23:19 / 1 Sam 15:29 paradox + the Jer 18:7–10 conditional-covenant resolution.
4. **`docs/translator_decisions/manah_divine_appointment_2026-05.md`** (§5) — brief; locks ทรงจัดเตรียม. Lower-priority but cleanly resolvable now.
5. **(Optional)** `docs/translator_decisions/leitwort_handling_policy_2026-05.md` (§7) — meta-doc for translator-discipline; names the leitwort vs Thai-naturalness trade-off.
6. **(Carries forward from Ruth audit, still urgent)** `docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md` — Jonah validates the Ruth-1:13 implicit rule a second time; doc not yet written; lift now before Exod 7 / Pss / Isa.
7. **(Carries forward from Ruth audit, lower priority for Jonah)** `docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` — N/A in Jonah but still urgent before Job 19 / Isa 41-43.
8. **(Carries forward from Ruth audit, lower priority for Jonah)** `docs/translator_decisions/hebrew_oath_formulas_2026-05.md` — N/A in Jonah but still urgent before Sam-Kgs.
9. **(Carries forward from Ruth audit, lower priority for Jonah)** `docs/translator_decisions/paqad_visit_attend_2026-05.md` — N/A in Jonah but still urgent before 1 Sam 2.

### G. Existing docs to amend
- **`proper_names_and_transliteration_2026-05.md`** — add the Jonah names (Jonah, Amittai, Nineveh, Tarshish, Joppa-as-ยัฟโฟ); flag the OT-Joppa-ยัฟโฟ vs NT-Acts-ยัฟปา cross-corpus pair as the second known instance of the RUT-4:19-Ram-class issue.
- **(After §A decision)** Ruth's `chesed`-locking precedent will be cross-referenced in the new chesed corpus doc.

### H. External AI review (§3 of checklist) — **pending**
Recommended before `book-jonah-v1` tag. Suggested 4-cluster external AI packet:
1. **JON 1:1–16** — prophet-fleeing arc + ירד death-trajectory + טוּל hurling-chain + sailors' conversion-arc + 1:6 captain's elevation question + 1:9 Jonah's confession formula
2. **JON 2:1–11** — psalmist-prayer-from-the-fish + chesed first occurrence (2:9) + the divine-deliverance / underworld vocabulary + the prayer-poem's psalmic register
3. **JON 3:1–10** — Ninevite conversion + the divine-relenting (3:9, 3:10) + the king's edict + the Ninevite-vs-sailor-conversion contrast (אלהים-only vs YHWH-covenant-name)
4. **JON 4:1–11** — Jonah's protest + Exod-34 attribute formula + qiqayon plant lexical-crux + the four divine appointments + the closing right-hand/left-hand interpretive crux

Use Grok + ChatGPT in parallel per the prior pattern.

---

## Recommendation

**Jonah ships in strong corpus-hygiene shape — and validates the Ruth-audit's OT-corpus-doc roadmap by exercising several lemmata Ruth flagged for forward-load.** Five structural improvements to lock in before the next OT book ships:

1. **Resolve the Ruth-Jonah chesed drift** (§A) — write the chesed corpus doc + re-translate JON 2:9 + 4:2 if Ben endorses the Ruth-lock-wins resolution.
2. **Resolve the JON 4:11 right-hand/left-hand interpretive crux** (§B) — at minimum verify the textual_variants reader-edition footnote surfaces in the final Eremos rendering.
3. **Write the Exod-34 attribute-formula corpus doc** (§F2) — locks 6-component rendering before its 7+ recurrences in Pss/Joel/Nah/Neh/2 Chr.
4. **Write the נִחַם divine-relenting corpus doc** (§F3) — surfaces the apparent-paradox vs Num 23:19 + locks ทรงเปลี่ยนพระทัย before the prophetic-relenting cluster.
5. **Write the Ruth-recommended divine-anthropomorphism corpus doc** (§F6) — Jonah's second-validation makes this urgent before Exod 7 / Pss-corpus body-part-of-YHWH cluster.

Tag `book-jonah-v1` after:
1. Ben's decisions on **§A + §B** (DECIDE items: chesed cross-corpus drift; 4:11 interpretive crux)
2. Ben's confirmations on **§C + §D + §E** (REVIEW items: 1:4 hurl; 4:6 botanical footnote; 1:6 captain register)
3. Four new translator_decisions docs written (§F1–F4 — chesed + Exod-34 formula + נִחַם + מָנָה; F5/F6/F7/F8/F9 may be deferred or written in parallel)
4. External AI sanity-check (§H)
5. The two newly-generated JON 4 OT-extension artifacts (`output/check_reports/honorifics_binding_jonah_04.md` + `output/textual_variants/jonah_04.json`) committed alongside this audit

The book's central theological pivot (YHWH's mercy extends to the historic enemy + the prophet's protest at God's character) is preserved with cross-corpus consistency in everything except the chesed-lemma drift (§A). **Jonah is ready to be the second OT-pilot — pending the locks above.**
