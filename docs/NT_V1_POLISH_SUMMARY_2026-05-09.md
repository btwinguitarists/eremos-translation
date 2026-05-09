# NT v1.0 — Polish Proposals (Decision Doc)

**Generated:** 2026-05-09
**Total proposals:** 223

**This is the single decision doc.** For each proposal below, change 
`**Decision:** pending` to `**Decision:** approve` or `**Decision:** reject`. 
Save the file. Then run:

```
python3 scripts/apply_polish_deltas.py --all
```

Per-chapter files under `output/polish_proposals/<book>/` are auto-generated 
reference copies — you do NOT need to edit them.

---

## Counts by issue type

| Issue type | Count |
|---|---:|
| awkward_phonetic | 7 |
| conjunction_overload | 59 |
| literal_idiom | 8 |
| redundant_directional | 1 |
| register_drift | 107 |
| title_collision | 2 |
| wooden_passive | 39 |
| **Total** | **223** |

## Counts by book

| Book | Proposals | File |
|---|---:|---|
| matthew | 18 | `output/polish_proposals/matthew/matthew_02.md`, `output/polish_proposals/matthew/matthew_06.md`, `output/polish_proposals/matthew/matthew_10.md`, `output/polish_proposals/matthew/matthew_11.md`, `output/polish_proposals/matthew/matthew_12.md`, `output/polish_proposals/matthew/matthew_13.md`, `output/polish_proposals/matthew/matthew_15.md`, `output/polish_proposals/matthew/matthew_20.md`, `output/polish_proposals/matthew/matthew_24.md`, `output/polish_proposals/matthew/matthew_26.md`, `output/polish_proposals/matthew/matthew_27.md`, `output/polish_proposals/matthew/matthew_28.md` |
| mark | 13 | `output/polish_proposals/mark/mark_01.md`, `output/polish_proposals/mark/mark_02.md`, `output/polish_proposals/mark/mark_03.md`, `output/polish_proposals/mark/mark_06.md`, `output/polish_proposals/mark/mark_08.md`, `output/polish_proposals/mark/mark_10.md`, `output/polish_proposals/mark/mark_11.md`, `output/polish_proposals/mark/mark_12.md`, `output/polish_proposals/mark/mark_15.md` |
| luke | 15 | `output/polish_proposals/luke/luke_01.md`, `output/polish_proposals/luke/luke_04.md`, `output/polish_proposals/luke/luke_07.md`, `output/polish_proposals/luke/luke_10.md`, `output/polish_proposals/luke/luke_11.md`, `output/polish_proposals/luke/luke_12.md`, `output/polish_proposals/luke/luke_16.md`, `output/polish_proposals/luke/luke_17.md`, `output/polish_proposals/luke/luke_18.md`, `output/polish_proposals/luke/luke_19.md`, `output/polish_proposals/luke/luke_22.md`, `output/polish_proposals/luke/luke_24.md` |
| john | 27 | `output/polish_proposals/john/john_01.md`, `output/polish_proposals/john/john_02.md`, `output/polish_proposals/john/john_05.md`, `output/polish_proposals/john/john_07.md`, `output/polish_proposals/john/john_08.md`, `output/polish_proposals/john/john_09.md`, `output/polish_proposals/john/john_10.md`, `output/polish_proposals/john/john_11.md`, `output/polish_proposals/john/john_12.md`, `output/polish_proposals/john/john_13.md`, `output/polish_proposals/john/john_14.md`, `output/polish_proposals/john/john_15.md`, `output/polish_proposals/john/john_20.md`, `output/polish_proposals/john/john_21.md` |
| acts | 21 | `output/polish_proposals/acts/acts_01.md`, `output/polish_proposals/acts/acts_03.md`, `output/polish_proposals/acts/acts_04.md`, `output/polish_proposals/acts/acts_06.md`, `output/polish_proposals/acts/acts_07.md`, `output/polish_proposals/acts/acts_08.md`, `output/polish_proposals/acts/acts_09.md`, `output/polish_proposals/acts/acts_14.md`, `output/polish_proposals/acts/acts_15.md`, `output/polish_proposals/acts/acts_17.md`, `output/polish_proposals/acts/acts_18.md`, `output/polish_proposals/acts/acts_19.md`, `output/polish_proposals/acts/acts_20.md`, `output/polish_proposals/acts/acts_21.md`, `output/polish_proposals/acts/acts_25.md`, `output/polish_proposals/acts/acts_26.md`, `output/polish_proposals/acts/acts_28.md` |
| romans | 25 | `output/polish_proposals/romans/romans_02.md`, `output/polish_proposals/romans/romans_03.md`, `output/polish_proposals/romans/romans_04.md`, `output/polish_proposals/romans/romans_05.md`, `output/polish_proposals/romans/romans_06.md`, `output/polish_proposals/romans/romans_07.md`, `output/polish_proposals/romans/romans_08.md`, `output/polish_proposals/romans/romans_09.md`, `output/polish_proposals/romans/romans_10.md`, `output/polish_proposals/romans/romans_11.md`, `output/polish_proposals/romans/romans_12.md`, `output/polish_proposals/romans/romans_13.md`, `output/polish_proposals/romans/romans_14.md`, `output/polish_proposals/romans/romans_15.md`, `output/polish_proposals/romans/romans_16.md` |
| 1corinthians | 22 | `output/polish_proposals/1corinthians/1corinthians_03.md`, `output/polish_proposals/1corinthians/1corinthians_04.md`, `output/polish_proposals/1corinthians/1corinthians_05.md`, `output/polish_proposals/1corinthians/1corinthians_06.md`, `output/polish_proposals/1corinthians/1corinthians_07.md`, `output/polish_proposals/1corinthians/1corinthians_08.md`, `output/polish_proposals/1corinthians/1corinthians_09.md`, `output/polish_proposals/1corinthians/1corinthians_10.md`, `output/polish_proposals/1corinthians/1corinthians_11.md`, `output/polish_proposals/1corinthians/1corinthians_12.md`, `output/polish_proposals/1corinthians/1corinthians_13.md`, `output/polish_proposals/1corinthians/1corinthians_14.md`, `output/polish_proposals/1corinthians/1corinthians_15.md`, `output/polish_proposals/1corinthians/1corinthians_16.md` |
| 2corinthians | 17 | `output/polish_proposals/2corinthians/2corinthians_01.md`, `output/polish_proposals/2corinthians/2corinthians_03.md`, `output/polish_proposals/2corinthians/2corinthians_04.md`, `output/polish_proposals/2corinthians/2corinthians_05.md`, `output/polish_proposals/2corinthians/2corinthians_07.md`, `output/polish_proposals/2corinthians/2corinthians_08.md`, `output/polish_proposals/2corinthians/2corinthians_09.md`, `output/polish_proposals/2corinthians/2corinthians_10.md`, `output/polish_proposals/2corinthians/2corinthians_11.md`, `output/polish_proposals/2corinthians/2corinthians_12.md`, `output/polish_proposals/2corinthians/2corinthians_13.md` |
| ephesians | 5 | `output/polish_proposals/ephesians/ephesians_04.md`, `output/polish_proposals/ephesians/ephesians_05.md`, `output/polish_proposals/ephesians/ephesians_06.md` |
| philippians | 4 | `output/polish_proposals/philippians/philippians_01.md`, `output/polish_proposals/philippians/philippians_03.md` |
| colossians | 2 | `output/polish_proposals/colossians/colossians_03.md`, `output/polish_proposals/colossians/colossians_04.md` |
| 1timothy | 4 | `output/polish_proposals/1timothy/1timothy_01.md`, `output/polish_proposals/1timothy/1timothy_04.md`, `output/polish_proposals/1timothy/1timothy_06.md` |
| philemon | 1 | `output/polish_proposals/philemon/philemon_01.md` |
| hebrews | 8 | `output/polish_proposals/hebrews/hebrews_01.md`, `output/polish_proposals/hebrews/hebrews_02.md`, `output/polish_proposals/hebrews/hebrews_04.md` |
| 1john | 3 | `output/polish_proposals/1john/1john_03.md`, `output/polish_proposals/1john/1john_04.md` |
| revelation | 38 | `output/polish_proposals/revelation/revelation_01.md`, `output/polish_proposals/revelation/revelation_02.md`, `output/polish_proposals/revelation/revelation_03.md`, `output/polish_proposals/revelation/revelation_04.md`, `output/polish_proposals/revelation/revelation_05.md`, `output/polish_proposals/revelation/revelation_06.md`, `output/polish_proposals/revelation/revelation_07.md`, `output/polish_proposals/revelation/revelation_08.md`, `output/polish_proposals/revelation/revelation_09.md`, `output/polish_proposals/revelation/revelation_10.md`, `output/polish_proposals/revelation/revelation_11.md`, `output/polish_proposals/revelation/revelation_12.md`, `output/polish_proposals/revelation/revelation_13.md`, `output/polish_proposals/revelation/revelation_14.md`, `output/polish_proposals/revelation/revelation_16.md`, `output/polish_proposals/revelation/revelation_18.md`, `output/polish_proposals/revelation/revelation_19.md`, `output/polish_proposals/revelation/revelation_20.md`, `output/polish_proposals/revelation/revelation_22.md` |

---

## awkward_phonetic (7)

<!-- POLISH_PROPOSAL id=mark_03_002 -->
### Mark 3:11

**Current:**

> พระพักตร์พระองค์

**Proposed:**

> พระพักตร์ของพระองค์

**Why:** พระ- repeats back-to-back in พระพักตร์พระองค์, which can stumble aloud. Inserting ของ separates the two royal terms without changing the referent.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_15_001 -->
### John 15:12

**Current:**

> นี่คือพระบัญญัติของเรา คือ ให้พวกท่านรักกันและกัน เหมือนที่เราได้รักพวกท่าน

**Proposed:**

> นี่คือพระบัญญัติของเรา ได้แก่ ให้พวกท่านรักกันและกัน เหมือนที่เราได้รักพวกท่าน

**Why:** The verse uses คือ twice in one compact explanatory construction. Replacing the second คือ with ได้แก่ keeps the explanation function but removes the audible echo.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_15_002 -->
### John 15:19

**Current:**

> แต่เพราะพวกท่านไม่ได้เป็นของโลก แต่เราได้เลือกพวกท่านออกมาจากโลกแล้ว

**Proposed:**

> แต่เพราะพวกท่านไม่ได้เป็นของโลก เราได้เลือกพวกท่านออกมาจากโลกแล้ว

**Why:** แต่ appears twice in close succession, creating a repeated-conjunction stumble. The opening แต่เพราะ already carries the contrast, so the second แต่ can be dropped without changing the relation.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_15_003 -->
### John 15:21

**Current:**

> เพราะพระนามของเรา เพราะพวกเขาไม่รู้จักผู้ทรงใช้เรามา

**Proposed:**

> เพราะพระนามของเรา เนื่องจากพวกเขาไม่รู้จักผู้ทรงใช้เรามา

**Why:** เพราะ closes one causal phrase and immediately opens the next. Replacing the second เพราะ with เนื่องจาก breaks the echo while preserving the causal meaning.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_03_001 -->
### Romans 3:20

**Current:**

> พระพักตร์พระองค์

**Proposed:**

> พระพักตร์ของพระองค์

**Why:** พระ- repeats back-to-back in พระพักตร์พระองค์, which can stumble aloud. Inserting ของ separates the two royal terms without changing the referent.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1john_03_001 -->
### 1 John 3:11

**Current:**

> นี่คือถ้อยแถลงที่ท่านได้ยินมาตั้งแต่ปฐมกาล คือ ให้เรารักซึ่งกันและกัน

**Proposed:**

> นี่คือถ้อยแถลงที่ท่านได้ยินมาตั้งแต่ปฐมกาล ได้แก่ ให้เรารักซึ่งกันและกัน

**Why:** The verse uses คือ twice in one compact explanatory construction. Replacing the second คือ with ได้แก่ keeps the explanation function but removes the audible echo.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1john_03_002 -->
### 1 John 3:23

**Current:**

> นี่คือพระบัญญัติของพระองค์ คือ ให้เราเชื่อในพระนามของพระบุตรของพระองค์ คือพระเยซูคริสต์ และให้เรารักซึ่งกันและกัน เหมือนที่พระองค์ทรงบัญญัติไว้แก่เรา

**Proposed:**

> นี่คือพระบัญญัติของพระองค์ ได้แก่ ให้เราเชื่อในพระนามของพระบุตรของพระองค์ คือพระเยซูคริสต์ และให้เรารักซึ่งกันและกัน เหมือนที่พระองค์ทรงบัญญัติไว้แก่เรา

**Why:** The verse uses คือ twice in one compact explanatory construction. Replacing the second คือ with ได้แก่ keeps the explanation function but removes the audible echo.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## conjunction_overload (59)

<!-- POLISH_PROPOSAL id=matthew_02_optimal_002 -->
### Matthew 2:16

**Current:**

> แล้วเมื่อเฮโรดรู้ว่าตนถูกพวกโหราจารย์หลอก ก็โกรธจัด

**Proposed:**

> เมื่อเฮโรดรู้ว่าตนถูกพวกโหราจารย์หลอก ก็โกรธจัด

**Why:** The verse opens with τότε rendered as แล้ว (then/at that time), immediately followed by เมื่อ from the locked construction เมื่อ…รู้ว่าตนถูก…หลอก — producing แล้วเมื่อ, a back-to-back pairing of two temporal markers at sentence-start that is not idiomatic in Thai narrative prose. The เมื่อ clause itself already anchors the temporal sequence; dropping แล้ว yields เมื่อเฮโรดรู้ว่าตนถูกพวกโหราจารย์หลอก ก็โกรธจัด, which reads more cleanly while the narrative anchoring of τότε (linking the massacre to the Magi's non-return) is preserved by context following the Jeremiah citation in v.17. Flagged fyi rather than defer_to_native because whether τότε warrants an overt Thai marker is a recurring pattern across Matthew (cf. 2:7, 2:17, etc.) and a normalisation decision may be more appropriate at corpus level than verse by verse. Locked term เมื่อ…รู้ว่าตนถูก…หลอก and โกรธจัด both preserved verbatim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_02_optimal_001 -->
### Matthew 2:22

**Current:**

> แต่เมื่อได้ยินว่า

**Proposed:**

> ครั้นได้ยินว่า

**Why:** The current rendering splits δέ → แต่ and the participial ἀκούσας → เมื่อ, producing the compound connector แต่เมื่อ (adversative + temporal stacked) at verse-start. Because the second half of the same verse contains the locked clause เมื่อพระเจ้าทรงเตือนในความฝัน, the full verse runs แต่เมื่อ…ก็…และเมื่อ…จึง with two เมื่อ-clauses in sequence, creating a mild rhythmic and logical pile-up. Thai formal narrative particle ครั้น handles both the δέ transitional function and the participial ἀκούσας in a single elegant word — ครั้นได้ยินว่า (upon hearing that) is the established register-appropriate Thai construction for this participial clause type. The adversarial force of δέ (homecoming of v.21 contrasted with a new obstacle) is fully recoverable from narrative context. All locked terms preserved verbatim; the only change is the opening connector.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_06_optimal_001 -->
### Matthew 6:7

**Current:**

> เพราะเขาคิดว่าจะได้รับคำตอบเพราะการพูดมากของเขา

**Proposed:**

> เพราะเขาคิดว่าจะได้รับคำตอบด้วยการพูดมากของเขา

**Why:** The first เพราะ correctly renders the discourse marker γάρ ('for they think…'); the second เพราะ, however, is rendering ἐν τῇ πολυλογίᾳ, a dative of means — 'by means of their many words' — not a causal clause. Mapping a Greek instrumental ἐν onto a Thai causal connector produces two identical connectors in immediate succession ('เพราะ…เพราะ'), creating an awkward pile-up that also obscures the logical distinction between the framing reason and the means clause. Replacing the second เพราะ with ด้วย (by/through) resolves the pile-up and is more faithful to the Greek instrumental construction; a Thai reader will immediately parse ด้วยการพูดมาก as 'by means of much talking.' Both locked terms จะได้รับคำตอบ and การพูดมากของเขา are preserved verbatim, and the theological content — that pagans expect divine attention in proportion to verbal volume — is unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_10_optimal_001 -->
### Matthew 10:10

**Current:**

> หรือเสื้อสองตัว หรือรองเท้า หรือไม้เท้า

**Proposed:**

> เสื้อสองตัว รองเท้า หรือไม้เท้า

**Why:** The Greek uses μηδέ three times in unbroken sequence (μηδὲ δύο χιτῶνας μηδὲ ὑποδήματα μηδὲ ῥάβδον), and the Thai renders each occurrence as 'หรือ,' producing three identical connectors in a row — a textbook conjunction pile-up. In idiomatic Thai, a list of co-prohibited items is more naturally rendered with comma-style juxtaposition, reserving 'หรือ' for the final item only; the prohibitive force of 'อย่านำ' at the head of the clause already negates the entire list without requiring an 'or' before every member. The proposed text removes the two medial 'หรือ' while leaving all four locked terms (อย่านำย่ามในการเดินทาง, เสื้อสองตัว, รองเท้า, ไม้เท้า) verbatim and unchanged; the prohibition on every item remains fully unambiguous. No theological alteration of any kind; this is purely a connector-frequency adjustment. Routing to Tier-A Thai reviewer to confirm that the list-enumeration pattern is the more natural Thai register here.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_12_optimal_001 -->
### Matthew 12:15

**Current:**

> และมีคนมากมายตามเสด็จพระองค์ และพระองค์ทรงรักษาเขาทุกคน

**Proposed:**

> มีคนมากมายตามเสด็จพระองค์ และพระองค์ทรงรักษาเขาทุกคน

**Why:** The two consecutive καί linking three sequential clauses are both rendered as 'และ,' producing 'และมีคนมากมายตามเสด็จพระองค์ และพระองค์ทรงรักษาเขาทุกคน' — a mild connector pile-up within a single verse. The first 'และ' is dispensable: 'มีคนมากมายตามเสด็จพระองค์' reads naturally as a circumstantial consequence of 'เสด็จหลบออกไปจากที่นั่น' without requiring an explicit connective, while the second 'และ' more purposefully binds the healing action to the crowd-following context. Dropping the first 'และ' yields a smoother Thai narrative cadence — Jesus withdrew / crowds followed (resultant) / and he healed them all — without altering the logical sequence or touching any locked term (มีคนมากมายตามเสด็จพระองค์ and ทรงรักษาเขาทุกคน both preserved verbatim). No KD entry addresses the conjunction rendering for this verse; the KDs cover only the individual clause-content choices. A native Thai-language reviewer should confirm preferred rhythm, since this is a cadence judgment rather than a meaning correction.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_02_optimal_001 -->
### Mark 2:12

**Current:**

> เขาก็ลุกขึ้น และทันใดนั้นก็ยกแคร่เดินออกไปต่อหน้าทุกคน

**Proposed:**

> เขาก็ลุกขึ้น ทันใดนั้นก็ยกแคร่เดินออกไปต่อหน้าทุกคน

**Why:** The Greek καὶ εὐθύς ('and immediately') is currently rendered as 'และทันใดนั้น,' prepending an explicit 'และ' to the temporal adverb. In Thai narrative, 'ทันใดนั้น' (at once / immediately) already serves as a discourse bridge; it links the preceding clause to the next and carries the immediacy signal without needing a co-ordinating 'และ' in front of it. The sentence as a whole already accumulates five discourse particles — ก็, และ, ก็, จน, and a second และ — so the first 'และ' before 'ทันใดนั้น' adds to that pile-up without contributing logical information. Dropping it lets 'ทันใดนั้น' headline the dramatic speed of the healed man's obedience, exactly as a Thai narrator would deploy it, while fully preserving the Greek meaning of immediate response; no locked terms are altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_10_optimal_002 -->
### MRK 10:21

**Current:**

> แล้วท่านจะมีทรัพย์สมบัติในสวรรค์ แล้วจงมาติดตามเรา

**Proposed:**

> แล้วท่านจะมีทรัพย์สมบัติในสวรรค์ และจงมาติดตามเรา

**Why:** The verse's final two Greek clauses are both introduced by καί: 'καὶ ἕξεις θησαυρὸν ἐν οὐρανῷ' (and you will have treasure in heaven) and 'καὶ δεῦρο ἀκολούθει μοι' (and come follow me). Rendering both with 'แล้ว' imposes a temporal-sequential reading ('then… then…') on the second καί, which in context is climactic-additive rather than sequential: Jesus issues the discipleship summons as the culminating co-ordinate call, not as something contingent on the treasure being received first. Two consecutive 'แล้ว' also creates a rhythmically awkward pile-up at the verse's climax. Replacing the second 'แล้ว' with 'และ' removes the false sequentiality, breaks the pile-up, and aligns with the coordinating (not temporal) force of καί before δεῦρο. The key decisions rationale documents the discipleship formula 'จงมาติดตามเรา' (locked and preserved verbatim) but does not address the preceding connector; all other locked terms are untouched; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_10_optimal_001 -->
### MRK 10:43

**Current:**

> แต่ในพวกท่านจะไม่เป็นเช่นนั้น แต่ผู้ใดต้องการเป็นใหญ่ในพวกท่าน ผู้นั้นจะต้องเป็นผู้รับใช้ของท่านทั้งหลาย

**Proposed:**

> แต่ในพวกท่านจะไม่เป็นเช่นนั้น ผู้ใดต้องการเป็นใหญ่ในพวกท่าน ผู้นั้นจะต้องเป็นผู้รับใช้ของท่านทั้งหลาย

**Why:** The Greek opens with the discourse particle δέ (topic-contrast) and then pivots to the counter-rule with ἀλλά (strong adversative). Mapping both onto 'แต่' produces the jarring adjacent pair 'แต่ในพวกท่านจะไม่เป็นเช่นนั้น แต่ผู้ใดต้องการเป็นใหญ่…' — two identical connectors in consecutive clauses that Thai readers naturally stumble over. Dropping the second 'แต่' lets the positive counter-rule ('ผู้ใดต้องการเป็นใหญ่…ผู้นั้นจะต้องเป็นผู้รับใช้') follow the negated premise asyndetically, which is the natural Thai rhetorical pattern for this kind of antithetical rule-pair. The key decisions rationale for this verse documents the rendering of οὐχ οὕτως and διάκονος but does not address the connector choice, leaving this open for polish. All locked terms ('ในพวกท่านจะไม่เป็นเช่นนั้น', 'เป็นใหญ่', 'ผู้รับใช้') are preserved verbatim; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_11_optimal_001 -->
### Mark 11:4

**Current:**

> เขาทั้งสองก็ไป และพบลูกลาตัวหนึ่งผูกไว้ที่ประตูด้านนอกบนถนน และแก้มันออก

**Proposed:**

> เขาทั้งสองก็ไป พบลูกลาตัวหนึ่งผูกไว้ที่ประตูด้านนอกบนถนน และแก้มันออก

**Why:** Three consecutive καί clauses are rendered as 'ก็ไป และพบ … และแก้มัน,' producing a double-'และ' pile-up that is unnatural in Thai narrative prose. In Thai, rapid sequential actions (went → found → untied) conventionally chain without a connector before the second verb; 'และ' is most naturally reserved to flag the final completing action. Dropping 'และ' before 'พบ' yields the idiomatic Thai narrative sequence 'ก็ไป พบ … และแก้มันออก,' which fully preserves the logical relation and temporal order of all three events. Neither KD1 nor KD2 addresses the conjunction-handling here; locked terms ถนน and แก้ remain verbatim; no theological content is affected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_12_optimal_001 -->
### Mark 12:28

**Current:**

> ได้ยินพวกเขาโต้เถียงกัน และเห็นว่าพระองค์ตรัสตอบได้ดี

**Proposed:**

> ได้ยินพวกเขาโต้เถียงกัน เห็นว่าพระองค์ตรัสตอบได้ดี

**Why:** The Greek presents two sequential aorist participles—ἀκούσας ('having heard') and ἰδών ('having perceived')—flowing without an explicit conjunction into the main verb ἐπηρώτησεν; no καί or δέ stands between them. The Thai rendering inserts 'และ' before 'เห็น,' producing the three-connector chain 'ได้ยิน…และเห็น…จึง,' which reads as a list of parallel events rather than a natural participial build-up. Thai participial sequences of this type (perception → assessment → resulting action) idiomatically drop the coordinator between the first two members, letting 'ได้ยิน…เห็น…จึงเข้ามา' read as a single unbroken mental progression. Removing 'และ' is the minimal fix; both locked terms 'ได้ยินพวกเขาโต้เถียงกัน' and 'เห็นว่าพระองค์ตรัสตอบได้ดี' are preserved verbatim, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_04_optimal_001 -->
### Luke 4:22

**Current:**

> และพูดกันว่า

**Proposed:**

> พลางพูดกันว่า

**Why:** The verse chains three καί clauses: the first is absorbed into 'ต่างก็', the second surfaces as 'และ' before 'อัศจรรย์ใจ', and the third produces a second 'และ' immediately before 'พูดกันว่า', yielding an 'และ…และ' pile-up across one sentence. The Greek imperfect ἔλεγον is concurrent with ἐθาύมαζον — the crowd was saying this while they were marveling, not after — so Thai 'พลาง' (doing X simultaneously while doing Y) carries that concurrence more precisely and naturally breaks the repeated conjunction. All four locked terms (ทุกคนต่างก็พูดชมเชยพระองค์, อัศจรรย์ใจในถ้อยคำแห่งพระคุณ, จากพระโอษฐ์ของพระองค์, คนนี้ไม่ใช่บุตรของโยเซฟหรือ) are preserved verbatim; only the single connector particle changes, and whether 'พลาง' lands as more natural than 'และ' here warrants a native-speaker ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_07_optimal_001 -->
### Luke 7:34

**Current:**

> มาและกินและดื่ม

**Proposed:**

> มา ทั้งกินทั้งดื่ม

**Why:** The Greek contains exactly one καί, binding the two present participles ἐσθίων καὶ πίνων into a manner-of-coming phrase that modifies ἐλήλυθεν; there is no connector in Greek between the main verb and the first participle. The Thai 'มา-และ-กิน-และ-ดื่ม' adds a second 'และ' without Greek warrant, flattening the participial manner clause into three co-ordinated main verbs that read as sequential events ('came, then ate, then drank') rather than a single arrival characterised by eating-and-drinking. The Thai correlative ทั้ง…ทั้ง ('both…and') is the natural paired-activity construction for concurrent actions and restores the participial manner sense: 'the Son of Man came, both eating and drinking.' The locked title 'บุตรมนุษย์' and the locked accusation-quote (ดูสิ ชายผู้นี้เป็นคนตะกละและคนขี้เมา / เป็นเพื่อนของพวกคนเก็บภาษีและคนบาป) are preserved verbatim; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_12_optimal_001 -->
### Luke 12:58

**Current:**

> แล้วเจ้าพนักงานก็จะใส่ท่านลงในคุก

**Proposed:**

> เจ้าพนักงานก็จะใส่ท่านลงในคุก

**Why:** The Greek presents three coordinated καί clauses: lest the opponent drag you, καὶ ὁ κριτής hand you over, καὶ ὁ πράκτωρ throw you in prison. The Thai renders the second with 'และ' alone but the third with 'แล้ว...ก็' — a double consecutive marker for a single καί, creating a connector pile-up absent from the source. No KD entry addresses this chain; KD5 covers only the lexical choice πράκτωρ → เจ้าพนักงาน. Dropping 'แล้ว' while retaining 'ก็' is sufficient to mark the sequential result; 'เจ้าพนักงานก็จะ' follows naturally from the preceding 'และผู้พิพากษาจะ...' All locked terms (เจ้าพนักงาน, ฉุดลาก, คู่ความ, ต่อหน้าผู้มีอำนาจ, พยายามตกลงกับเขา) are preserved; no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_17_optimal_001 -->
### Luke 17:14

**Current:**

> และต่อมาขณะที่พวกเขาเดินไป

**Proposed:**

> และขณะที่พวกเขาเดินไปนั้น

**Why:** The rendering lexicalises both elements of Luke's narrative formula separately: ἐγένετο → 'ต่อมา' (subsequently/later) and ἐν τῷ ὑπάγειν → 'ขณะที่...เดินไป' (while going), stacking two temporal connectives that carry contradictory directional force in Thai — 'ต่อมา' marks sequential-after while 'ขณะที่' marks simultaneity, creating a mild logical tension. Luke's ἐγένετο here functions as a pure narrative-progression marker and carries no semantic content that Thai requires a separate lexeme to render; dropping 'ต่อมา' and retaining 'ขณะที่...นั้น' alone renders ἐν τῷ ὑπάγειν accurately and more naturally. No KD rationale documents the choice of 'ต่อมา,' and the locked phrase 'พวกเขาก็หายสะอาดจากโรคเรื้อน' is fully preserved unchanged. This is not a theological alteration.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_18_optimal_001 -->
### Luke 18:43

**Current:**

> เขาก็กลับมองเห็น และเขาติดตามพระองค์ไปพร้อมกับสรรเสริญพระเจ้า และประชาชน

**Proposed:**

> เขาก็กลับมองเห็น เขาติดตามพระองค์ไปพร้อมกับสรรเสริญพระเจ้า และประชาชน

**Why:** The three καί's yield ก็…และ…และ in the current text: the first καί is naturally absorbed into ก็ (tied to ทันใดนั้น), but both the second and third καί are rendered as และ, producing back-to-back connectors of the same form. In Thai narrative, rapid sequential actions by the same subject (heal → follow) typically read more naturally in asyndeton, reserving และ for the shift to a new subject (the crowd). Dropping the และ before เขาติดตาม creates that distinction — 'recovered sight / followed him glorifying God — and all the people…' — without altering meaning or any locked term. Whether native-speaker intuition prefers the current flowing-and or the asyndeton is the judgment call; the KD rationale for this verse does not address conjunction handling, so no corpus lock applies.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_19_optimal_001 -->
### Luke 19:11

**Current:**

> และเพราะพวกเขาคิดว่าอาณาจักรของพระเจ้าจะปรากฏโดยพลัน

**Proposed:**

> และพวกเขาคิดว่าอาณาจักรของพระเจ้าจะปรากฏโดยพลัน

**Why:** The Greek has a single διά + τό governing two coordinated infinitives (εἶναι καὶ δοκεῖν), expressing both reasons as one compound causal construction rather than two independently signalled causes. The Thai expands this into two parallel เพราะ-clauses ('เพราะ … และเพราะ …'), adding a second causal marker that the Greek source does not independently supply. Dropping the second เพราะ to yield 'เพราะ … และ …' preserves both reasons under the frame already established by the first เพราะ, reduces connector weight to match the single-διά construction, and marginally improves sentence rhythm. All locked terms are preserved verbatim: 'เพราะพระองค์ใกล้กรุงเยรูซาเล็มเข้าไปแล้ว' is untouched, and 'จะปรากฏโดยพลัน' is retained intact. This is not a theological change; the parable's two motivations remain fully present. Whether formal evangelical Thai prose prefers the balanced double-เพราะ for rhetorical parallelism or the leaner single-เพราะ for natural flow is a judgment that a Tier-A native reviewer should adjudicate.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_01_optimal_001 -->
### John 1:34

**Current:**

> และข้าพเจ้าได้เห็นแล้ว และได้เป็นพยานยืนยันว่า

**Proposed:**

> ข้าพเจ้าเองได้เห็นแล้ว และได้เป็นพยานยืนยันว่า

**Why:** κἀγώ is an emphatic compound in which the rhetorical weight falls on ἐγώ ('I myself'), not on the connective καί; the identical κἀγώ in v.31 is rendered within this same corpus as 'ข้าพเจ้าเองก็' — with no leading 'และ' — establishing the preferred pattern. The current v.34 form 'และข้าพเจ้า … และได้เป็นพยาน' places two consecutive 'และ' connectors back-to-back, producing a translationese pile-up that reads awkwardly in Thai. Replacing the first 'และ' with the emphatic particle 'เอง' breaks the pile-up, restores the κἀγώ-emphasis ('I myself have seen'), and restores corpus-internal consistency with v.31. The KD1 rationale for v.34 addresses only the textual variant (ἐκλεκτός vs υἱός) and does not document the leading 'และ' as a deliberate choice; this is therefore an undocumented literal carry-over, not a locked decision. The locked term 'ผู้ที่พระเจ้าทรงเลือกสรร' is preserved verbatim, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_02_optimal_003 -->
### John 2:14

**Current:**

> และคนรับแลกเงินนั่งอยู่

**Proposed:**

> กับคนรับแลกเงินนั่งอยู่

**Why:** All four καί connectors in the verse are mapped to 'และ', including the one that appends the money-changers as a distinct category after the list of animal-sellers. This produces 'คนขายวัว แกะ และนกพิราบ และคนรับแลกเงิน' — a list-final 'และ' immediately followed by another 'และ' for a new category, which is mildly awkward in Thai list prose. Thai idiom conventionally uses 'กับ' to attach an additional item or subgroup after a closed list ('... และนกพิราบ กับคนรับแลกเงินนั่งอยู่'), breaking the pile-up while preserving the additive logic of καί. Both locked terms 'คนขายวัว แกะ และนกพิราบ' and 'คนรับแลกเงิน' appear verbatim in the proposal. Whether 'กับ' vs. 'และ' is the more natural connector at this specific list-junction requires a native Thai stylistic judgment, hence defer_to_native.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_09_optimal_001 -->
### John 9:22

**Current:**

> เพราะกลัวผู้นำชาวยิว เพราะผู้นำชาวยิวได้ตกลงกันแล้วว่า

**Proposed:**

> เพราะกลัวผู้นำชาวยิว เนื่องจากผู้นำชาวยิวได้ตกลงกันแล้วว่า

**Why:** The Greek deploys two structurally distinct connectors: ὅτι introduces the primary-cause clause ('that they feared the leaders') and γάρ introduces its explanatory ground ('for the leaders had already agreed'). The Thai renders both identically as เพราะ, producing the pile-up ก็เพราะ...เพราะ within a single sentence, which flattens the ὅτι/γάρ distinction and reads slightly heavy in modern formal prose. Replacing the second instance with เนื่องจาก — a standard modern formal-register causal connector that does not overlap with the first เพราะ — breaks the pile-up and signals the γάρ shift from direct cause to explanatory elaboration, matching THSV2011 register. Both locked terms (ถูกขับออกจากธรรมศาลา, ยอมรับว่าพระเยซูเป็นพระคริสต์) fall after the changed span and are wholly preserved; no theological content is altered. Confidence is defer_to_native because the choice between เพราะ and เนื่องจาก in a complex subordinate chain is a naturalness judgment that requires a Tier-A Thai ear to confirm.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_10_optimal_002 -->
### John 10:33

**Current:**

> เราไม่ได้ขว้างหินใส่ท่านเพราะการดี แต่เพราะการหมิ่นประมาท เพราะท่านเป็นเพียงมนุษย์ แต่ตั้งตัวเองเป็นพระเจ้า

**Proposed:**

> เราไม่ได้ขว้างหินใส่ท่านเพราะการดี แต่เพราะการหมิ่นประมาท ที่ท่านเป็นเพียงมนุษย์ แต่ตั้งตัวเองเป็นพระเจ้า

**Why:** The Greek ὅτι introducing the content of the charge (ὅτι σὺ ἄνθρωπος ὢν ποιεῖς σεαυτὸν θεόν) is rendered by a second 'เพราะ,' producing a 'เพราะ … เพราะ' pile-up where both connectives are given equal causal weight. The second ὅτι here is content-appositional — it unpacks what the blasphemy consists of, not an independent additional cause — and Thai relative 'ที่' (of the kind that / in that) expresses this appositive-explanatory relationship more precisely without repeating the causal particle. Both locked phrases 'การหมิ่นประมาท' and 'ท่านเป็นเพียงมนุษย์ แต่ตั้งตัวเองเป็นพระเจ้า' appear verbatim in the proposal; no theological meaning is altered. Routing to Tier-A Thai-language reviewer because the choice between 'เพราะ' and 'ที่' in this particular appositive context is a subtle native-register judgment.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_13_optimal_001 -->
### John 13:11

**Current:**

> เพราะพระองค์ทรงทราบว่าใครจะเป็นผู้ทรยศพระองค์ เพราะเหตุนี้พระองค์จึงตรัสว่า

**Proposed:**

> เพราะพระองค์ทรงทราบว่าใครจะเป็นผู้ทรยศพระองค์ พระองค์จึงตรัสว่า

**Why:** γάρ (background-explanatory) is rendered เพราะ, then διὰ τοῦτο (consequential 'for this reason') is rendered เพราะเหตุนี้, producing a three-marker stack: เพราะ … เพราะเหตุนี้ … จึง. Standard Thai cause-result discourse uses the เพราะ … จึง pair as a clean binary; the middle เพราะเหตุนี้ is redundant because จึง already signals the consequence in full. Dropping เพราะเหตุนี้ preserves both the causal background (γάρ → เพราะ) and the consequential force (διὰ τοῦτο → จึง) without stacking. The locked term ผู้ทรยศพระองค์ is preserved verbatim; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_06_optimal_001 -->
### Acts 6:7

**Current:**

> พระวจนะของพระเจ้าก็จำเริญขึ้น และจำนวนสาวกในกรุงเยรูซาเล็มก็ทวีมากยิ่งขึ้น และปุโรหิตจำนวนมากก็มาเชื่อฟังในความเชื่อ

**Proposed:**

> พระวจนะของพระเจ้าก็จำเริญขึ้น จำนวนสาวกในกรุงเยรูซาเล็มก็ทวีมากยิ่งขึ้น และปุโรหิตจำนวนมากก็มาเชื่อฟังในความเชื่อ

**Why:** The Greek coordinates three clauses with καί + καί + τε; the Thai gives each clause a ก็ particle that already carries connective force equivalent to καί, but additionally inserts 'และ' before both clauses 2 and 3, producing a doubled-connector pattern (และ + ก็) in each. Clause 2's ก็ is sufficient to bear the second καί unaided; placing 'และ' before it creates a minor pile-up (และจำนวน...ก็...และปุโรหิต...ก็) not present in the Greek. Reserving 'และ' for clause 3 alone better mirrors the Greek's distinct shift from καί to τε and yields a cleaner Thai progression (ก็ … ก็ … และ…ก็). The proposed text removes only the unlocked 'และ' before clause 2; all three locked key-decision terms (พระวจนะของพระเจ้าก็จำเริญขึ้น, จำนวนสาวกในกรุงเยรูซาเล็มก็ทวีมากยิ่งขึ้น, and และปุโรหิตจำนวนมากก็มาเชื่อฟังในความเชื่อ) are preserved verbatim, and no theological content is altered; the question is purely whether omitting the first 'และ' reads more naturally to a native ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_08_optimal_001 -->
### Acts 8:13

**Current:**

> อย่างใกล้ชิด และเมื่อเห็นหมายสำคัญ

**Proposed:**

> อย่างใกล้ชิด เมื่อเห็นหมายสำคัญ

**Why:** The Greek θεωρῶν τε is a participial clause joined by τε (a softer, subordinating-connective particle) to the preceding action, expressing circumstance-leading-to-result ('seeing signs and great works, he was amazed'), not a fully coordinate clause. Thai renders it with a leading 'และเมื่อ,' which promotes it to a coordinate clause syntactically parallel with the earlier 'และเมื่อรับบัพติศมา...' clause, creating a mechanical pile-up of the pattern 'และเมื่อ...ก็... และเมื่อ...ก็.' Dropping 'และ' before the second 'เมื่อเห็น' allows the temporal-circumstantial clause to stand naturally in Thai narrative prose without forced coordination, matching the THSV2011 register for participial circumstance and better reflecting the lighter τε connector. All three locked phrases ('แม้แต่ซีโมนเองก็เชื่อด้วย,' 'เมื่อรับบัพติศมาแล้วเขาก็ติดตามฟีลิปอย่างใกล้ชิด,' 'เมื่อเห็นหมายสำคัญกับการอัศจรรย์อันยิ่งใหญ่ที่เกิดขึ้น เขาก็ตะลึงงัน') are preserved verbatim; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_09_optimal_001 -->
### Acts 9:38

**Current:**

> พวกสาวกจึงได้ยินว่าเปโตรอยู่ที่นั่น จึงส่งชายสองคนไปหาท่าน

**Proposed:**

> เมื่อพวกสาวกได้ยินว่าเปโตรอยู่ที่นั่น ก็ส่งชายสองคนไปหาท่าน

**Why:** The Greek presents two structurally distinct elements after the causal genitive-absolute: a circumstantial aorist participle ἀκούσαντες ('having heard') and the main-clause verb ἀπέστειλαν ('they sent'). The current Thai renders both transitions with 'จึง,' producing a 'จึง...จึง' chain that reads as two sequential causal results of the nearness — nearness caused hearing, and then hearing caused sending. The Greek instead treats hearing as a temporal circumstance ('when they heard') and sending as the principal consequence. A 'เมื่อ...ก็' pattern for the hearing clause more accurately captures the circumstantial force of the participle and dissolves the pile-up, without altering the meaning. Neither KD1 (which documents only 'เนื่องจาก' for the genitive-absolute) nor KD2 (which documents 'ทูลว่า' for παρακαλοῦντες) addresses the double 'จึง' connector; the locked phrases 'เนื่องจากเมืองลิดดาอยู่ใกล้เมืองยัฟฟา' and 'ส่งชายสองคนไปหาท่าน' are preserved verbatim in the proposal.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_18_optimal_002 -->
### Acts 18:10

**Current:**

> เพราะในเมืองนี้เรามีประชากรจำนวนมาก

**Proposed:**

> ด้วยว่าในเมืองนี้เรามีประชากรจำนวนมาก

**Why:** Greek uses διότι twice in this verse; both are rendered 'เพราะ,' placing the same causal connector at the opening and the close of a short divine-speech unit ('เพราะเราอยู่กับเจ้า … เพราะในเมืองนี้'). The first 'เพราะ' is locked as part of 'เพราะเราอยู่กับเจ้า' and cannot change. The second διότι, however, introduces an elaborating sub-ground for the safety promise — a logically downstream role that Thai 'ด้วยว่า' (formal explanatory/elaborating particle) captures more precisely while breaking the double-เพราะ pile-up. The locked phrase 'ในเมืองนี้เรามีประชากรจำนวนมาก' is preserved verbatim; only the unlocked connector is touched; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_20_optimal_001 -->
### Acts 20:13

**Current:**

> เพราะท่านได้จัดการไว้เช่นนั้น เนื่องจากท่านตั้งใจเดินเท้าไปเอง

**Proposed:**

> เพราะท่านได้จัดการไว้เช่นนั้น โดยที่ท่านตั้งใจเดินเท้าไปเอง

**Why:** The Greek presents a single γάρ-explanatory clause ('for he had arranged it thus') followed by the circumstantial participle μέλλων αὐτὸς πεζεύειν ('intending to go on foot himself'); the participle expresses attendant circumstance or manner, not a second independent cause. The Thai renders this as two sequential causal conjunctions — เพราะ (because) immediately followed by เนื่องจาก (since/because) — producing a causal-marker pile-up that is heavier than the source structure and risks reading as two symmetrically weighted causes. Replacing เนื่องจาก with โดยที่ reframes the second clause as a circumstantial or modal adverb, more faithfully mirroring the Greek participial function and relieving the double-causal accumulation. Neither KD entry for v.13 addresses the connector choice for the μέλλων clause, so the เนื่องจาก is not rationale-justified. The locked phrase 'ท่านตั้งใจเดินเท้าไปเอง' is preserved verbatim in the proposed text; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_28_optimal_001 -->
### Acts 28:20

**Current:**

> ดังนั้น เพราะเหตุนี้ ข้าพเจ้าจึงเชิญพวกท่านมาพบและสนทนากัน

**Proposed:**

> เพราะเหตุนี้ ข้าพเจ้าจึงเชิญพวกท่านมาพบและสนทนากัน

**Why:** The Greek 'διὰ ταύτην οὖν τὴν αἰτίαν' is a single emphatic prepositional phrase in which οὖν is embedded as an inferential intensifier — 'for this very reason, therefore.' The Thai rendering splits the phrase into two discrete connectors ('ดังนั้น' for οὖν and 'เพราะเหตุนี้' for διά) and then adds a third resultative marker 'จึง' inside the main clause, producing a three-connector pile-up ('therefore…because of this…so I') that reads as translationese rather than natural formal Thai. Dropping 'ดังนั้น' and retaining the idiomatic Thai pairing 'เพราะเหตุนี้…จึง' captures both the causal sense of διά and the inferential weight of οὖν in a single natural construction. The locked phrase 'เชิญพวกท่านมาพบและสนทนากัน' is preserved verbatim, and no theological content is affected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_04_optimal_001 -->
### Romans 4:6

**Current:**

> โดยปราศจากการประพฤติเช่นเดียวกัน

**Proposed:**

> โดยปราศจากการประพฤติ

**Why:** The comparison signalled by καθάπερ καί is already fully expressed by the opening 'ดังที่...ก็'; adding 'เช่นเดียวกัน' at the close of the verse creates a third comparison marker for a single Greek construction, producing a connector pile-up. More critically, its placement immediately after 'โดยปราศจากการประพฤติ' risks being parsed as modifying that clause ('apart from works — in the same manner') rather than echoing the David-introduction, causing syntactic ambiguity for Thai readers. Dropping it leaves the locked phrase 'ความสุขของคนที่พระเจ้าทรงนับว่าเป็นผู้ชอบธรรม โดยปราศจากการประพฤติ' fully intact, the Greek meaning unchanged, and the verse's comparative logic cleaner.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_05_optimal_001 -->
### Romans 5:2

**Current:**

> และเรายืนหยัดอยู่ในพระคุณนี้ และเราชื่นชมยินดีในความหวังแห่งพระเกียรติของพระเจ้า

**Proposed:**

> ซึ่งเรายืนหยัดอยู่ในพระคุณนั้น และเราชื่นชมยินดีในความหวังแห่งพระเกียรติของพระเจ้า

**Why:** The Greek ἐν ᾗ ἑστήκαμεν is a relative clause grammatically embedded inside the main clause, modifying χάριν ταύτην ('this grace in which we stand'), and carries no καί of its own; the one genuine καί in this half of the verse introduces καυχώμεθα. The current Thai promotes this relative clause into a full independent clause opened with 'และ,' creating two consecutive 'และ' where the Greek has one relative pronoun plus one καί — a coordinator pile-up without Greek warrant. Replacing the first 'และ' with the relative pronoun 'ซึ่ง' (and using 'นั้น' as anaphoric back-reference to 'พระคุณนี้' already named in the preceding clause) restores the embedded-clause structure of the Greek while removing the spurious connector. Both locked terms are fully preserved verbatim: 'เราได้เข้าถึง' remains intact in the preceding clause and 'เราชื่นชมยินดีในความหวังแห่งพระเกียรติของพระเจ้า' is retained unchanged; no theological content is altered. Flagged defer_to_native because whether the ซึ่ง-relative construction reads more naturally than the double-'และ' coordination in THSV2011 evangelical-formal register is a nuanced judgment best confirmed by a Tier-A Thai-language reviewer.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_06_optimal_001 -->
### Romans 6:19

**Current:**

> — เพราะเช่นเดียวกับที่

**Proposed:**

> — เช่นเดียวกับที่

**Why:** The verse opens with the KD1-locked clause ending in เพราะความอ่อนแอของเนื้อหนังของพวกท่าน (rendering διά), then immediately after the dash introduces a second เพราะ (rendering γάρ) before เช่นเดียวกับที่, producing a double-เพราะ echo that reads as stacked connectives in Thai. The ὥσπερ…οὕτως correlative already carries inherent explanatory force — เช่นเดียวกับที่…บัดนี้จงมอบ is self-explicating and does not require an additional causal marker to convey γάρ's discourse function. Dropping the second เพราะ lets the correlative pair do the work unimpeded, which is how formal Thai comparison clauses typically run. Both locked terms — KD1 (ข้าพเจ้ากล่าวอย่างมนุษย์เพราะความอ่อนแอของเนื้อหนังของพวกท่าน) and KD2 (ทาสของความชอบธรรม สู่ความบริสุทธิ์) — are entirely untouched, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_07_optimal_002 -->
### Romans 7:10

**Current:**

> และข้าพเจ้าก็ตาย — และข้าพเจ้าพบว่า

**Proposed:**

> ข้าพเจ้าก็ตาย — และพบว่า

**Why:** The opening 'และข้าพเจ้าก็ตาย' renders ἐγὼ δέ with both 'และ' and 'ก็,' creating doubled connective weight; 'ก็' already carries the contrastive δέ sense (sin revived in v.9 while I died), making the preceding 'และ' redundant. The immediately following 'และข้าพเจ้าพบว่า' (for καί) then repeats both 'และ' and the explicit subject 'ข้าพเจ้า,' producing an 'และ … และ / ข้าพเจ้า … ข้าพเจ้า' cluster across the em-dash. Dropping the opening 'และ' and contracting to 'และพบว่า' (subject already established) breaks the cluster while preserving the δέ contrast (via ก็) and the καί consequence (via the retained 'และพบว่า'). The locked term 'พระบัญญัติที่ตั้งใจมาเพื่อชีวิต กลับนำมาซึ่งความตาย' follows unchanged and no theological change is introduced. Marked defer_to_native because opening a new verse with bare 'ข้าพเจ้าก็ตาย' (no initial connector linking to v.9) is a stylistic judgment that turns on Thai narrative-continuity conventions best confirmed by a Tier-A native reviewer.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_07_optimal_001 -->
### Romans 7:15

**Current:**

> ไม่เข้าใจสิ่งที่ตนกระทำ — เพราะสิ่งที่ข้าพเจ้าปรารถนา ข้าพเจ้าก็ไม่ทำ

**Proposed:**

> ไม่เข้าใจสิ่งที่ตนกระทำ — สิ่งที่ข้าพเจ้าปรารถนา ข้าพเจ้าก็ไม่ทำ

**Why:** The verse opens with 'เพราะข้าพเจ้าไม่เข้าใจสิ่งที่ตนกระทำ' (first γάρ, linking back to v.14's 'sold under sin') and then a second 'เพราะ' immediately after the em-dash for the elaborating second γάρ, producing a 'เพราะ — เพราะ' pile-up that reads stilted in Thai. In Thai discourse an em-dash already signals explanatory elaboration, making the second 'เพราะ' redundant; the evidence-clause flows naturally without a repeated causal connector. Dropping the second 'เพราะ' preserves the Greek explanatory logic — the second γάρ's evidence function is fully carried by the em-dash — while breaking the connector pile-up. The locked term 'สิ่งที่ข้าพเจ้าปรารถนา ข้าพเจ้าก็ไม่ทำ แต่สิ่งที่ข้าพเจ้าเกลียดชัง ข้าพเจ้ากลับทำ' is preserved verbatim and no theological change is introduced.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_13_optimal_002 -->
### Romans 13:4

**Current:**

> เพราะเขาไม่ได้ถือดาบไว้เปล่าๆ เพราะเขาเป็นผู้รับใช้ของพระเจ้า — เป็นผู้แก้แค้นเพื่อนำพระพิโรธมาสู่ผู้กระทำชั่ว

**Proposed:**

> เพราะเขาไม่ได้ถือดาบไว้เปล่าๆ — เขาเป็นผู้รับใช้ของพระเจ้า เป็นผู้แก้แค้นเพื่อนำพระพิโรธมาสู่ผู้กระทำชั่ว

**Why:** The verse carries three γάρ clauses all rendered เพราะ; two land consecutively ('เพราะเขาไม่ได้ถือดาบไว้เปล่าๆ เพราะเขาเป็นผู้รับใช้…') and stall the reading rhythm. Replacing the second back-to-back เพราะ with an em-dash — the connective already used once in this same clause — converts the resumptive γάρ into a natural Thai appositive ('not in vain — he is God's servant'), a common formal-prose move. Both locked terms (เป็นผู้รับใช้ของพระเจ้า and เป็นผู้แก้แค้นเพื่อนำพระพิโรธมาสู่ผู้กระทำชั่ว) are preserved verbatim. Deferred to Tier-A native review because the em-dash must be confirmed to carry adequate causal force in place of the explicit เพราะ in this theologically freighted context.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_03_optimal_001 -->
### 1 Corinthians 3:19

**Current:**

> เพราะมีคำเขียนไว้ว่า

**Proposed:**

> ดังที่เขียนไว้ว่า

**Why:** The verse opens with a causal γάρ rendered 'เพราะปัญญาของโลกนี้เป็นความโง่เขลา…' and immediately follows with a second γάρ (γέγραπται γάρ) also rendered 'เพราะ,' stacking two consecutive causal connectors where the second one performs a functionally distinct role: introducing a Scripture citation as evidential support, not a causal chain-link. In THSV2011-register Thai evangelical usage, γέγραπται γάρ introducing a proof-text is naturally rendered 'ดังที่เขียนไว้ว่า' or 'ตามที่เขียนไว้ว่า,' which is the standard citation-reference marker rather than a repeated causal เพราะ. Changing 'เพราะมีคำเขียนไว้ว่า' to 'ดังที่เขียนไว้ว่า' breaks the pile-up and restores the correct discourse signal (Scripture corroborates the preceding claim) while leaving all locked terms verbatim: 'ในสายพระเนตรของพระเจ้า' and the citation quote 'พระองค์ทรงจับคนมีปัญญาในความเจ้าเล่ห์ของพวกเขาเอง' are untouched. This is purely a connector-register fix, not a theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_05_optimal_001 -->
### 1 Corinthians 5:11

**Current:**

> แต่เป็นคนล่วงประเวณี

**Proposed:**

> กลับเป็นคนล่วงประเวณี

**Why:** The verse already opens with 'แต่บัดนี้' rendering δέ, and the translator added a second 'แต่' to make explicit the implicit Greek contrast between ὀνομαζόμενος (being named a brother) and ᾖ πόρνος (being in fact immoral). The two 'แต่' tokens appearing within the same sentence create an inelegant pile-up that a Thai editor would automatically resolve. 'กลับเป็น' (lit. 'turns out / reversal-is') is a standard formal Thai construction that carries precisely this reversal contrast — someone who carries the name of a brother yet lives in flagrant sin — without any register loss and without any pile-up. All locked terms ('ผู้ใดที่ได้ชื่อว่าเป็นพี่น้อง', 'คนล่วงประเวณี…คนปล้นชิง', 'อย่าแม้กระทั่งกินด้วยกันกับคนเช่นนั้น') remain verbatim unchanged, and no theological meaning shifts.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_05_optimal_002 -->
### 1 Corinthians 5:3

**Current:**

> เพราะส่วนข้าพเจ้านั้น

**Proposed:**

> เพราะข้าพเจ้า

**Why:** Ἐγὼ μὲν γάρ stacks two Greek discourse markers — γάρ (explanatory-causal) and μέν (contrastive particle setting up the body/spirit antithesis). Thai renders both simultaneously: เพราะ (γάρ) + ส่วน…นั้น (μέν), yielding the three-word opener 'เพราะส่วนข้าพเจ้านั้น' — a combination that sits awkwardly in Thai prose. Crucially, the μέν antithesis is already handled by the locked 'แม้ไม่ได้อยู่ด้วยทางกาย แต่อยู่ด้วยทางใจ' that follows immediately, making ส่วน…นั้น structurally redundant; retaining only เพราะ preserves γάρ's causal link to v.2 while lightening the opener. All locked terms remain verbatim unchanged. Confidence is defer_to_native because whether 'เพราะส่วนข้าพเจ้านั้น' reads as appropriately weighty or as an awkward stack is ultimately a native-register judgment the Tier-A Thai reviewer should confirm.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_06_optimal_001 -->
### 1 Corinthians 6:16

**Current:**

> หรือพวกท่านไม่รู้หรือว่า

**Proposed:**

> หรือพวกท่านไม่รู้ว่า

**Why:** The Greek ἢ οὐκ οἴδατε ὅτι carries exactly one disjunctive marker (ἢ) and one subordinating conjunction (ὅτι); there is no second interrogative particle in the Greek. The current Thai 'หรือพวกท่านไม่รู้หรือว่า' stacks two instances of หรือ in immediate succession — the opening หรือ rendering ἢ, then a second หรือ embedded in 'ไม่รู้หรือว่า' — producing a pile-up that the source lacks. Every other occurrence of the identical Greek formula ἢ οὐκ οἴδατε ὅτι in this chapter (vv. 2, 9, 19) is rendered 'หรือพวกท่านไม่รู้ว่า' with a single หรือ; v.16 is the sole outlier. Dropping the embedded second หรือ normalises v.16 to the intra-chapter pattern, eliminates the redundant stacking, and carries zero theological implication. Both locked terms for this verse (ผู้ที่ผูกพันกับหญิงโสเภณีก็เป็นกายเดียวกันกับนาง and เพราะมีคำเขียนไว้ว่า 'ทั้งสองจะเป็นเนื้อเดียวกัน') are fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_07_optimal_002 -->
### 1 Corinthians 7:7

**Current:**

> แต่แต่ละคนก็มีของประทานเฉพาะของตนจากพระเจ้า

**Proposed:**

> ทว่าแต่ละคนก็มีของประทานเฉพาะของตนจากพระเจ้า

**Why:** The adversative ἀλλά is rendered as 'แต่,' which immediately precedes the Thai distributive determiner 'แต่ละคน' (each person), producing a double-แต่ cluster — 'แต่ แต่ละคน' — where the conjunction and the distributive share the same syllable. These are two entirely distinct Thai lexemes (adversative connector vs. distributive quantifier), but the sonic and visual collision is unnatural and a native reader would notice the pile-up. Replacing the conjunction with 'ทว่า' (a formal-register synonym for 'however/but,' standard in evangelical THSV2011 prose) dissolves the collision without weakening the adversative logic of ἀλλά. The locked phrase 'แต่ละคนก็มีของประทานเฉพาะของตนจากพระเจ้า' is preserved verbatim, and no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_09_optimal_001 -->
### 1 Corinthians 9:8

**Current:**

> หรือว่าธรรมบัญญัติก็กล่าวเช่นเดียวกันด้วยไม่ใช่หรือ?

**Proposed:**

> หรือว่าธรรมบัญญัติก็ไม่ได้กล่าวสิ่งเหล่านี้ด้วยหรือ?

**Why:** The current clause compounds 'เช่นเดียวกัน' (a loose rendering of ταῦตา as 'in the same way') with 'ด้วย' (rendering καί, 'also'), producing two near-synonymous discourse markers in rapid succession, then caps the whole phrase with a further 'ไม่ใช่หรือ?' flip — three stacked layers where the Greek has one conjunction (καί) and one negative (οὐ). Dropping the redundant 'เช่นเดียวกัน' and restoring ταῦτα precisely as 'สิ่งเหล่านี้' leaves a single clean connector 'ด้วย' for καί; repositioning the negative as 'ไม่ได้กล่าว...หรือ?' converts the question to the standard Thai rhetorical-negative form naturally expecting an affirmative answer ('yes, it does say these things'). The locked first clause is unchanged, no theological nuance is altered, and the Greek lemmas are each rendered once rather than twice.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_03_optimal_001 -->
### 2 Corinthians 3:12

**Current:**

> เนื่องจากเรามีความหวังเช่นนี้ เราจึงประกาศด้วยความกล้าหาญอย่างยิ่ง

**Proposed:**

> เมื่อเรามีความหวังเช่นนี้ เราจึงประกาศด้วยความกล้าหาญอย่างยิ่ง

**Why:** เนื่องจาก...จึง is a grammatically correct Thai causal construction, but when prefixed by ดังนั้น the sentence front-loads three successive logical connectors—'therefore / because / therefore'—that stammer against each other in Thai prose. Thai เมื่อ...จึง renders the Greek circumstantial participle ἔχοντες as a lighter temporal-circumstantial clause ('when/since we have such hope, we therefore…'), allowing ดังนั้น to carry the discourse-level οὖν without redundancy. The locked phrase เราจึงประกาศด้วยความกล้าหาญอย่างยิ่ง is preserved exactly, and Paul's meaning—apostolic boldness flowing from Spirit-grounded hope—is fully intact. No theological shift occurs.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_03_optimal_002 -->
### 2 Corinthians 3:14

**Current:**

> เพราะจนถึงทุกวันนี้ ผ้าคลุมเดียวกันนั้นก็ยังคงอยู่ในขณะอ่านพันธสัญญาเดิม

**Proposed:**

> จนถึงทุกวันนี้ ผ้าคลุมเดียวกันนั้นก็ยังคงอยู่ในขณะอ่านพันธสัญญาเดิม

**Why:** The verse's locked end-clause already deploys เพราะ to render ὅτι ('เพราะในพระคริสต์เท่านั้นที่ผ้าคลุมจะถูกขจัดออกไป'); rendering the earlier γάρ with a second เพราะ produces a เพราะ…เพราะ echo within a single complex sentence that reads clumsily in Thai. Dropping the first เพราะ lets the evidential γάρ clause flow naturally as an unmarked elaboration on the hardening claim—Thai readers will parse 'until this day the veil remains' as self-evident continuation without needing a formal causal particle. All locked phrases (จิตใจของพวกเขาแข็งกระด้าง, ในขณะอ่านพันธสัญญาเดิม, and the full ก็ยังคงอยู่…ถูกขจัดออกไป clause) are preserved verbatim; the logical and theological content is identical.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_04_optimal_001 -->
### 2 Corinthians 4:11

**Current:**

> เพราะเห็นแก่พระเยซู

**Proposed:**

> โดยเห็นแก่พระเยซู

**Why:** The verse opens with γάρ rendered เพราะ to introduce the causal clause; then the same clause ends with διὰ Ἰησοῦν rendered เพราะเห็นแก่พระเยซู, creating a double-เพราะ pattern within one clause ('เพราะเราซึ่งยังมีชีวิตอยู่นั้น ถูกมอบไว้แก่ความตายเสมอเพราะเห็นแก่'). Replacing เพราะเห็นแก่ with โดยเห็นแก่ breaks the pile-up while preserving the full causal-motivational sense of διά + accusative ('on account of / for the sake of'). Critically, the identical Greek phrase διὰ Ἰησοῦν at 4:5 is corpus-locked as 'โดยเห็นแก่พระเยซู,' so this change simultaneously achieves cross-verse consistency with that locked term; all other locked terms in the verse are untouched and no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_04_optimal_002 -->
### 2 Corinthians 4:15

**Current:**

> เพื่อพระคุณที่ทวีขึ้นโดยทางคนเป็นจำนวนมาก จะทำให้

**Proposed:**

> ให้พระคุณที่ทวีขึ้นโดยทางคนเป็นจำนวนมาก ทำให้

**Why:** The verse accumulates three เพื่อ markers from three distinct Greek elements: δι' ὑμᾶς → เพื่อพวกท่าน, ἵνα → เพื่อพระคุณ..., and εἰς τὴν δόξαν → เพื่อพระเกียรติ (this last within the locked term). Swapping the ἵνα-introduction from เพื่อ to ให้—a fully standard Thai purpose-clause marker also equivalent to ἵνα—reduces the triple-เพื่อ stack to two while preserving both locked terms ('พระคุณที่ทวีขึ้น' and 'การขอบพระคุณล้นเหลือไปเพื่อพระเกียรติของพระเจ้า'); removing จะ before ทำให้ is consistent with Thai ให้-purpose-clause grammar, which does not require the future marker. Flagged defer_to_native because the specific naturalness of ให้ versus เพื่อ as the ἵνα carrier in this noun-subject purpose clause warrants Tier-A native reviewer confirmation before applying.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_05_optimal_001 -->
### 2 Corinthians 5:4

**Current:**

> เพราะเราไม่ปรารถนาที่จะถูกถอดออก

**Proposed:**

> โดยที่เราไม่ปรารถนาที่จะถูกถอดออก

**Why:** The verse opens with 'เพราะ' rendering γάρ and then repeats 'เพราะ' for ἐφ' ᾧ (ἐπί + relative pronoun dative), flattening two structurally distinct Greek connectors into the same Thai word and producing a 'เพราะ…เพราะ' pile-up within a single sentence. 'โดยที่' (= 'in that / by the fact that') more precisely captures ἐφ' ᾧ as a ground-specifying relative clause — 'we groan with heaviness, in that we do not wish to be stripped' — giving it a different grammatical register from the causal γάρ that opens the verse and clarifying that the second clause specifies the basis of the heaviness rather than adding a parallel reason. All three locked terms (คร่ำครวญด้วยความหนักอึ้ง; ไม่ปรารถนาที่จะถูกถอดออก แต่ปรารถนาที่จะได้สวมเพิ่มเข้าไป; ให้สิ่งที่ตายได้ถูกชีวิตกลืนเสีย) are preserved verbatim; only the single connector word changes. This is a surface-level stylistic refinement with no theological implication, and whether 'โดยที่' sounds more natural than a second 'เพราะ' in this exact context is best confirmed by a native Thai reviewer.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_07_optimal_002 -->
### 2 Corinthians 7:13

**Current:**

> เพราะจิตวิญญาณของเขาได้รับการพักพิงจากพวกท่านทุกคน

**Proposed:**

> เนื่องจากจิตวิญญาณของเขาได้รับการพักพิงจากพวกท่านทุกคน

**Why:** The clause 'เราชื่นชมยินดียิ่งกว่านั้นเพราะความปีติยินดีของทิตัส' renders ἐχάρημεν ἐπὶ τῇ χαρᾷ Τίτου using 'เพราะ' for the prepositional ἐπί+dative construction, and the following ὅτι clause explaining the grounds of Titus's joy is also rendered 'เพราะ', stacking two เพราะ in consecutive clauses with different grammatical origins (preposition vs. subordinating conjunction). Replacing the ὅตι-connector with 'เนื่องจาก' distinguishes the explanatory sub-clause and makes the logical layering (Titus was joyful → because his spirit had been refreshed) more transparent to Thai readers. The KD rationale for 7:13 documents the passive choices for παρακαλέω and ἀναπαύω (both corpus-locked) but does not address the connector selected for ὅτι. The corpus-locked phrase 'จิตวิญญาณของเขาได้รับการพักพิงจากพวกท่านทุกคน' is preserved verbatim inside the proposed text, as are all other locked phrases for the verse. No theological change is involved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_07_optimal_001 -->
### 2 Corinthians 7:9

**Current:**

> เพราะพวกท่านได้รับความโศกใจตามพระประสงค์ของพระเจ้า

**Proposed:**

> เนื่องจากพวกท่านได้รับความโศกใจตามพระประสงค์ของพระเจ้า

**Why:** The preceding ἀλλ' ὅτι clause is already rendered with 'แต่เพราะ' (= 'but because'), and the immediately following γάρ clause is also rendered 'เพราะ', producing two adjacent เพราะ clauses — 'แต่เพราะความโศกใจได้นำพวกท่านสู่การกลับใจ เพราะพวกท่านได้รับความโศกใจตามพระประสงค์ของพระเจ้า' — where the connectors serve distinct logical roles (content-of-rejoicing vs. explanatory-causal). γάρ carries a 'for / since' explanatory nuance that เนื่องจาก captures more precisely while breaking the pile-up. The KD1 rationale for 7:9 justifies the lexical choices for λυπέω, μετάνοια, κατὰ θεόν, and ζημιόω but does not address the specific connector selected for γάρ. All locked Thai phrases — 'พวกท่านได้รับความโศกใจตามพระประสงค์ของพระเจ้า', 'ความโศกใจได้นำพวกท่านสู่การกลับใจ', and 'เพื่อพวกท่านจะไม่เสียหายในเรื่องใดเพราะเรา' — are preserved verbatim. This is a surface connector polish only; no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_12_optimal_001 -->
### 2 Corinthians 12:6

**Current:**

> เพราะถ้าข้าพเจ้าอยากภาคภูมิใจ

**Proposed:**

> ถ้าข้าพเจ้าอยากภาคภูมิใจ

**Why:** Greek ἐὰν γάρ encodes a discourse-level γάρ within a conditional protasis; the translator has rendered both components literally, producing the Thai compound 'เพราะถ้า' (because-if), which is not a natural Thai conjunctive pair — Thai ordinarily uses either 'เพราะ' or 'ถ้า' alone for their respective functions, not stacked. Here γάρ operates as an explanatory connector to v.5, a function that the discourse context already supplies without lexical encoding; dropping 'เพราะ' and retaining standalone 'ถ้า' preserves the conditional meaning fully and lets the second, genuinely causal γάρ ('เพราะข้าพเจ้าจะพูดความจริง' — locked) carry its causal force unimpeded. No locked terms are touched and no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1timothy_04_optimal_001 -->
### 1 Timothy 4:10

**Current:**

> เพราะเราได้วางใจในพระเจ้าผู้ทรงพระชนม์

**Proposed:**

> เนื่องจากเราได้วางใจในพระเจ้าผู้ทรงพระชนม์

**Why:** The Greek εἰς τοῦτο γάρ … ὅτι construction causes both γάρ (embedded inside the locked phrase 'เพราะเหตุนี้เอง') and ὅτι to surface as เพราะ in Thai, producing back-to-back เพราะ-phrases: 'เพราะเหตุนี้เองที่เราทำงานหนักและทุ่มเท เพราะเราได้วางใจ …' — a mild but noticeable pile-up in formal written Thai. No KD rationale addresses the ὅตι connector, so the choice is undocumented. Replacing the second เพราะ with เนื่องจาก varies the connector while preserving the identical causal-explanatory relation (ὅตι after a forward-pointing εἰς τοῦτο introduces the content/reason of 'this very end,' which เนื่องจาก carries precisely). The locked term 'วางใจในพระเจ้าผู้ทรงพระชนม์' is retained verbatim, and no theological meaning is affected. Routing to a Tier-A Thai-language reviewer to confirm whether the double-เพราะ cadence actually registers as awkward to a native ear in this register.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=philemon_01_optimal_001 -->
### Philemon 1:7

**Current:**

> เพราะข้าพเจ้ามีความชื่นชมยินดีอย่างยิ่งและการหนุนใจในความรักของท่าน เพราะใจของธรรมิกชนได้รับการทำให้สดชื่นโดยท่าน พี่น้องเอ๋ย

**Proposed:**

> ข้าพเจ้ามีความชื่นชมยินดีอย่างยิ่งและการหนุนใจในความรักของท่าน เพราะใจของธรรมิกชนได้รับการทำให้สดชื่นโดยท่าน พี่น้องเอ๋ย

**Why:** Both γάρ and ὅτι are rendered เพราะ, producing a Thai เพราะ…เพราะ sequence within a single verse that no key-decision rationale addresses. γάร here is a post-positive elaborating particle connecting v.7 back to the thanksgiving of vv.4–6; in Thai discourse this explanatory link can be carried implicitly when the sentence is a natural continuation of what precedes, making the leading เพราะ redundant rather than clarifying. Dropping the initial เพราะ (γάร) allows the main clause to open assertively—'I had much joy and comfort'—while the retained second เพราะ (ὅτι) delivers its direct causal force, giving the reason for that joy. All four locked terms (การหนุนใจ, ใจของธรรมิกชน, ได้รับการทำให้สดชื่น, พี่น้องเอ๋ย) are preserved verbatim; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_02_optimal_004 -->
### Hebrews 2:14

**Current:**

> เพราะฉะนั้น เนื่องจากบุตรทั้งหลายมีเลือดและเนื้อ

**Proposed:**

> เพราะฉะนั้น เมื่อบุตรทั้งหลายมีเลือดและเนื้อ

**Why:** The Greek compound connector Ἐπεὶ οὖν ('since therefore') is mirrored by two heavy Thai causal markers back-to-back (เพราะฉะนั้น + เนื่องจาก), producing an opening that a Thai reader would likely perceive as stilted. Swapping เนื่องจาก for the lighter conditional-causal เมื่อ ('given that / since') reduces the pile-up while preserving the logical relationship between the children's shared humanity and Christ's participation in it. No locked terms are affected. Surfaced as fyi because the double connector may be a conscious choice to mirror the Greek rhetorical texture, in which case no change is needed.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_04_optimal_001 -->
### Hebrews 4:6

**Current:**

> และเนื่องจากผู้ที่ได้รับพระกิตติคุณก่อนหน้าไม่ได้เข้าเพราะการขัดขืน

**Proposed:**

> และผู้ที่ได้รับพระกิตติคุณก่อนหน้าไม่ได้เข้าเพราะการขัดขืน

**Why:** The conjunction introducing the second clause is a simple coordinate καί subordinate to the opening ἐπεὶ οὖν that anchors the verse's single causal structure. Repeating 'เนื่องจาก' for this second καί promotes a coordinate link into a second independent causal clause, producing a 'เนื่องจาก…เนื่องจาก' pile-up where the Greek has only one causal hinge (ἐπεὶ) followed by a coordinate extension (καί). Dropping the redundant 'เนื่องจาก' preserves the identical logical relation — both clauses jointly ground the conclusion drawn in v.7 — while eliminating the stacked-connector effect. The locked phrase 'ยังเหลือสำหรับบางคนที่จะเข้าสู่การพักสงบนั้น' is untouched and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_03_optimal_002 -->
### Revelation 3:16

**Current:**

> เพราะฉะนั้น เนื่องจากเจ้าเป็นน้ำอุ่น

**Proposed:**

> เพราะฉะนั้น เมื่อเจ้าเป็นน้ำอุ่น

**Why:** The Greek has two discourse markers in sequence — οὕτως (consequential 'so/thus') and ὅτι (causal 'because') — which the Thai renders as the stacked connectives เพราะฉะนั้น + เนื่องจาก immediately adjacent; in Thai, stacking a result-marker directly before a reason-marker in this way creates an awkward double-load that no native speaker would write. The KDs for this verse cover only the two HAPAX lexemes (χλιαρός → น้ำอุ่น and ἐμέω → อาเจียน); neither addresses the connective cluster. Substituting เมื่อ ('since/given that') for เนื่องจาก retains the causal-circumstantial logic of ὅτι while letting เพราะฉะนั้น carry the consequential force of οὕτως, breaking the pile-up without dropping any semantic content; both locked fragments (เป็นน้ำอุ่น and เรากำลังจะอาเจียนเจ้าออกจากปากของเรา) are preserved verbatim. Routed to defer_to_native because the pragmatic weight of เมื่อ vs เนื่องจาก in this rhetorical context calls for a native Thai ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_04_optimal_001 -->
### Revelation 4:8

**Current:**

> แต่ละตนมีปีกหกปีก และทั้งภายนอกและภายในเต็มไปด้วยดวงตา

**Proposed:**

> แต่ละตนมีปีกหกปีก ทั้งภายนอกและภายในเต็มไปด้วยดวงตา

**Why:** The Greek has a single καί connecting κυκλόθεν (all around) and ἔσωθεν (inside); crucially, there is no explicit connector between the wings participial phrase (ἔχων ἀνὰ πτέρυγας ἕξ) and the following eyes clause — only a comma. The Thai correctly renders the internal καί as ทั้ง...และ... but then adds a further 'และ' before 'ทั้งภายนอก' to bridge the wings and eyes clauses, producing 'และทั้งภายนอกและภายใน' — three and-connectors in rapid succession where the Greek supplies one. Dropping the bridging 'และ' lets the eyes clause stand as a natural appositive description flowing directly from the subject, matches the Greek participial clause architecture (no explicit connector), and eliminates the triple-and echo without altering any meaning. The locked term 'แต่ละตนมีปีกหกปีก' appears verbatim in the proposed text; no theological content is changed.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_08_optimal_001 -->
### Revelation 8:13

**Current:**

> และข้าพเจ้าได้เห็น และได้ยินนกอินทรีตัวหนึ่ง

**Proposed:**

> และข้าพเจ้าได้เห็นและได้ยินนกอินทรีตัวหนึ่ง

**Why:** The Greek Καὶ εἶδον, καὶ ἤκουσα presents two καί-clauses that the Thai renders as two separate 'และ' phrases — leaving 'และข้าพเจ้าได้เห็น' as a dangling clause without an explicit object, then resuming with 'และได้ยินนกอินทรีตัวหนึ่ง.' In Thai narrative prose, an objectless 'ได้เห็น' clause mid-sentence is jarring; native readers instinctively ask 'เห็นอะไร?' and the answer arrives only through the following clause. Merging both verbs into a single compound predicate 'ได้เห็นและได้ยินนกอินทรีตัวหนึ่ง' gives both sensory verbs one shared object (the eagle), which is the natural Thai way to express concurrent visionary perception. The Greek meaning — John both saw and heard the eagle — is fully preserved; the downstream locked woe-formula '"วิบัติ วิบัติ วิบัติแก่ผู้ที่อาศัยอยู่บนแผ่นดินโลก' is untouched; and no theological content is altered. A native Tier-A reviewer should confirm whether the two-beat Greek structure (sight announced separately, then hearing specified) carries deliberate rhetorical weight worth preserving even at the cost of the dangling clause.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_11_optimal_002 -->
### Revelation 11:7

**Current:**

> จะทำสงครามกับพวกเขา และจะเอาชนะพวกเขา และจะฆ่าพวกเขา

**Proposed:**

> จะทำสงครามกับพวกเขา เอาชนะพวกเขา และฆ่าพวกเขา

**Why:** The key_decisions entry for 11:7 covers only the identity of the Beast (θηρίον, Dan 7 allusion); the three-verb sequential clause is not addressed. Flattening the three Greek καί-linked future verbs into three repeated 'และจะ + verb' constructions creates a stilted, monotonous cadence in Thai. The natural Thai strategy for a rapid narrative sequence (make-war → conquer → kill) is to lead with the first verbal phrase in full, then continue with bare verbs, reserving 'และ' for the final item only: 'จะทำสงครามกับพวกเขา เอาชนะพวกเขา และฆ่าพวกเขา.' All three actions are preserved in the same order; the locked term 'สัตว์ร้ายที่ขึ้นมาจากเหวลึก' is untouched. Routed to defer_to_native because the exact rhythm of the verbal sequence benefits from a native ear to confirm the drop of the second 'และจะ' reads as gain rather than loss.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_16_optimal_001 -->
### Revelation 16:11

**Current:**

> เพราะความเจ็บปวดของพวกเขาและเพราะฝีของพวกเขา

**Proposed:**

> เพราะความเจ็บปวดและฝีของพวกเขา

**Why:** The Greek presents two parallel prepositional phrases (ἐκ τῶν πόνων αὐτῶν καὶ ἐκ τῶν ἑλκῶν αὐτῶν) that share the same pronominal referent αὐτῶν. The current Thai renders each as a fully independent เพราะ clause with its own ของพวกเขา, producing 'เพราะ A ของพวกเขา และเพราะ B ของพวกเขา.' Standard Thai grammar contracts coordinated noun phrases under a single shared pronoun: 'เพราะ A และ B ของ X' is the idiomatic form, and the doubled เพราะ with doubled ของพวกเขา registers as translationese stiffness to a Thai reader. The proposed form drops the repeated connector and pronoun tail while preserving both causal items and the full logical relation. No locked terms ('พวกเขาก็หมิ่นประมาทพระเจ้าแห่งสวรรค์' and 'พวกเขาก็ไม่กลับใจจากการกระทำของพวกเขา') are touched, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_16_optimal_002 -->
### Revelation 16:21

**Current:**

> เพราะภัยพิบัติแห่งลูกเห็บนั้น เพราะภัยพิบัตินั้นรุนแรงเหลือเกิน

**Proposed:**

> เพราะภัยพิบัติแห่งลูกเห็บนั้นรุนแรงเหลือเกิน

**Why:** The Greek appends an explanatory ὅτι clause (ὅτι μεγάλη ἐστὶν ἡ πληγὴ αὐτῆς σφόδρα) to the prior instrumental phrase ἐκ τῆς πληγῆς τῆς χαλάζης. Both are rendered as Thai เพราะ, producing a double-เพราะ sequence where 'ภัยพิบัติ' is repeated verbatim in back-to-back clauses, creating an awkward echo. Natural Thai prose absorbs an explanatory ὅτι as a predicate of the antecedent noun: 'เพราะภัยพิบัติแห่งลูกเห็บนั้นรุนแรงเหลือเกิน' ('because the hailstorm plague was exceedingly severe') subsumes both the causal agent and its magnitude in one clean clause, losing nothing of the Greek's meaning. The locked term 'มนุษย์ทั้งหลายก็หมิ่นประมาทพระเจ้า' is fully preserved. Confidence is defer_to_native because collapsing two Greek clauses into one Thai predicate is a naturalness judgment that benefits from a Tier-A native-ear review.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_20_optimal_001 -->
### Revelation 20:4

**Current:**

> และข้าพเจ้าได้เห็นวิญญาณของผู้ที่ถูกตัดศีรษะ

**Proposed:**

> ข้าพเจ้ายังได้เห็นวิญญาณของผู้ที่ถูกตัดศีรษะ

**Why:** The verse contains at least seven consecutive 'และ' clauses tracking the Greek καί-chain; the translator's second 'ข้าพเจ้าได้เห็น' (not in the Greek, which has only one εἶδον governing both accusatives) was added for structural clarity, but prefixing it with 'และ' extends rather than resolves the pile-up ('และ…และ…และข้าพเจ้าได้เห็น…และข้าพเจ้าได้เห็น…'). Replacing the leading 'และ' with 'ยัง' ('ข้าพเจ้ายังได้เห็น' = 'I also saw') varies the connector while fully preserving the additive, vision-report relationship—the soul-martyrs remain an extension of the same divine scene but the rhythmic pile-up is broken. All locked phrases ('วิญญาณของผู้ที่ถูกตัดศีรษะ เพราะคำพยานของพระเยซู และเพราะพระวจนะของพระเจ้า,' 'บัลลังก์ทั้งหลาย และผู้ที่นั่งบนนั้น และทรงประทานอำนาจการพิพากษาแก่พวกเขา,' and 'พวกเขาได้มีชีวิตอยู่ และครอบครองเป็นกษัตริย์กับพระคริสต์เป็นเวลาพันปี') are entirely untouched; this is a surface connector choice, not a theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_22_optimal_001 -->
### Revelation 22:9

**Current:**

> และเป็นเพื่อนผู้รับใช้กับพี่น้องผู้เผยพระวจนะของท่าน และเป็นเพื่อนผู้รับใช้กับผู้ที่รักษาถ้อยคำของหนังสือเล่มนี้

**Proposed:**

> กับพี่น้องผู้เผยพระวจนะของท่าน และกับผู้ที่รักษาถ้อยคำของหนังสือเล่มนี้

**Why:** The Greek constructs a single predicate σύνδουλός σού εἰμι ('I am your fellow-servant') with three genitive complements chained by καί—not three separate predicate clauses. The current Thai mechanically re-states the full predicate 'เป็นเพื่อนผู้รับใช้กับ' for each of the second and third complements, producing a stacked, repetitive rhythm that no Thai speaker would use for an enumerated list. Dropping the repeated predicate and continuing with bare 'กับ + noun phrase' for the continuation members is the natural Thai list structure, reading the three parties as coordinate objects of the same relationship. The locked phrase 'อย่าทำเช่นนั้นเลย เราเป็นเพื่อนผู้รับใช้กับท่าน' is preserved verbatim; no theological meaning is altered and no other locked terms are touched.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## literal_idiom (8)

<!-- POLISH_PROPOSAL id=john_02_optimal_001 -->
### John 2:18

**Current:**

> ตอบและกล่าวกับพระองค์ว่า

**Proposed:**

> ตอบพระองค์ว่า

**Why:** ἀπεκρίθησαν καὶ εἶπαν is a Hebraistic verbal doublet (LXX formula ἀπεκρίθη καὶ εἶπεν ← וַיַּעַן וַיֹּאמֶר) whose idiomatic force is simply 'replied' — the two verbs form a fixed formulaic unit, not two discrete speech-acts. Rendering it word-for-word as 'ตอบและกล่าวกับพระองค์ว่า' creates a redundant Thai surface ('both answered AND said to him') that a Thai reader reads as awkward co-ordination rather than as a natural response formula. Standard Thai uses 'ตอบพระองค์ว่า' for this idiom, which already contains the speech-reporting function. The locked phrase 'เพราะเหตุการณ์นี้ ... จึงตอบ' is preserved verbatim as a substring of the revised sentence; 'ชาวยิว' and all other locked terms are unchanged. No theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_11_optimal_001 -->
### Romans 11:2

**Current:**

> ที่ท่านได้ทูลขอต่อพระเจ้าตำหนิอิสราเอล?

**Proposed:**

> ที่ท่านได้ทูลกล่าวหาอิสราเอลต่อพระเจ้า?

**Why:** ἐντυγχάνω κατά is a fixed Greek forensic idiom meaning to lodge a formal complaint or stand as accuser against a party before a higher authority (cf. Acts 25:24; Rom 8:27, 34 for the same verb in intercessory register); here Elijah himself functions as Israel's accuser before God's tribunal, not merely as a petitioner asking God to perform a rebuking action. The current 'ทูลขอต่อพระเจ้าตำหนิอิสราเอล' fractures the unified idiom into two sequential acts — 'petition God' then 'rebuke Israel' — so a Thai reader naturally understands Elijah as requesting God to do something to Israel, erasing the adversarial κατά dimension in which Elijah is the one bringing the charge. The proposed 'ทูลกล่าวหาอิสราเอลต่อพระเจ้า' (humbly brought charges against Israel before God) encodes the κατά-accusation in the verb กล่าวหา and places 'พระเจ้า' as the authority before whom the charge is brought, rendering the idiom-meaning rather than the surface words. Neither locked term for this verse ('ที่ทรงรู้จักล่วงหน้า' and 'พระคัมภีร์กล่าวอย่างไรเกี่ยวกับเอลียาห์') appears in the affected clause; อิสราเอล and พระเจ้า are preserved verbatim; this is a surface-rendering improvement only and introduces no theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_11_optimal_001 -->
### 1 Corinthians 11:29

**Current:**

> ก็กินและดื่มการพิพากษาเข้าใส่ตัวเอง

**Proposed:**

> ก็กินและดื่มโดยนำการพิพากษามาสู่ตนเอง

**Why:** The Greek 'κρίμα ἑαυτῷ ἐσθίει καὶ πίνει' deploys a dative of result: the unworthy partaker eats and drinks [the Supper] to/for his own judgment — judgment is the incurred consequence landing upon him, not the grammatical object of the eating and drinking. The Thai 'กินและดื่มการพิพากษาเข้าใส่ตัวเอง' treats 'การพิพากษา' as the direct object of กิน/ดื่ม, a construction Thai does not naturally license for abstract nouns; a Thai reader is likely to pause at the phrasing rather than catch the intended sense. The proposed 'กินและดื่มโดยนำการพิพากษามาสู่ตนเอง' retains both กิน and ดื่ม (preserving the deliberate repetition that mirrors the Eucharistic eating-and-drinking of vv. 26–28) while expressing judgment as a resultant consequence via the Thai instrumental 'โดย', which maps naturally onto the Greek dative-of-result. No theological change is made; the locked phrase 'โดยไม่หยั่งรู้ถึงพระกาย' is in a separate clause and is left untouched. Flagged fyi rather than apply because the KD documents the crux of τὸ σῶμα but is silent on this clause specifically, and the Eucharistic context may have led the translator to a deliberate literalism whose force a Tier-A Thai-language reviewer is better placed to assess.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_15_optimal_001 -->
### 1 Corinthians 15:41

**Current:**

> เพราะแม้แต่ดาวต่อดาวก็มีสง่าราศีต่างกัน

**Proposed:**

> เพราะดาวแต่ละดวงก็มีสง่าราศีต่างกัน

**Why:** The Greek uses a genitive-of-comparison construction — ἀστήρ ἀστέρος, 'star from star' — to convey that each star differs from every other. Thai 'ดาวต่อดาว' is a word-for-word calque: ต่อ in Thai carries senses of 'per,' 'against,' or 'toward' but does not idiomatically signal mutual comparison, so the phrase is opaque or simply odd to a Thai reader. 'ดาวแต่ละดวงก็มีสง่าราศีต่างกัน' (each individual star has different glory) conveys the same distributive meaning — stars are not uniform in their glory — in natural Thai without importing the Greek genitive grammar. No locked terms are present in this verse; no theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=ephesians_05_optimal_002 -->
### Ephesians 5:32

**Current:**

> แต่ข้าพเจ้ากล่าวถึงพระคริสต์และคริสตจักร

**Proposed:**

> แต่ข้าพเจ้าหมายถึงพระคริสต์และคริสตจักร

**Why:** Paul's λέγω εἰς in this meta-commentary clause carries applicatory-interpretive force — 'I am speaking with reference to / I mean [this mystery to apply to]' — not merely 'I am mentioning.' The εἰς specifies the referent toward which the Gen 2:24 quotation is being redirected (typological move), which is the entire point of the verse. 'กล่าวถึง' (speak of, mention) renders the literal surface but can leave a Thai reader wondering what Paul is actually asserting about Christ and the church; 'หมายถึง' (mean, refer to) signals the clarifying-identification move that a native Thai reader expects in a meta-statement of this type. The locked phrase 'ความลึกลับนี้ยิ่งใหญ่' is untouched, and no theological interpretation changes — Paul's typological claim that Gen 2:24 points to Christ-and-church stands unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=ephesians_06_optimal_001 -->
### Ephesians 6:15

**Current:**

> สวมรองเท้าที่เท้าด้วยความพร้อมแห่งข่าวประเสริฐของสันติสุข

**Proposed:**

> สวมรองเท้าด้วยความพร้อมแห่งข่าวประเสริฐของสันติสุข

**Why:** The Greek ὑποδησάμενοι τοὺς πόδας ('having shod your feet') is rendered word-for-word as 'สวมรองเท้าที่เท้า,' making 'ที่เท้า' entirely redundant in Thai: 'สวมรองเท้า' already encodes the foot-location with full idiomatic force—no native Thai speaker would say 'put shoes on at the feet.' No KD rationale documents or justifies the retention of 'ที่เท้า.' Removing it yields the natural Thai action phrase 'สวมรองเท้า' while preserving the full Greek meaning; the locked term 'ความพร้อมแห่งข่าวประเสริฐของสันติสุข' is unchanged, and no theological content is affected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_02_optimal_002 -->
### Revelation 2:23

**Current:**

> เราจะประหารบุตรของนางด้วยความตาย

**Proposed:**

> เราจะประหารชีวิตบุตรของนาง

**Why:** The Greek ἀποκτενῶ ἐν θανάτῳ is a LXX Hebraism (from Heb. בַּדֶּבֶר, 'by pestilence'; cf. Ezek. 33:27; Rev. 6:8 same phrase) rendered word-for-word as ประหาร…ด้วยความตาย, producing a Thai surface tautology—'execute by means of death' collapses to 'kill by the act of dying'—where Thai readers hear redundancy rather than apocalyptic idiom. The natural Thai ประหารชีวิต (judicial execution) conveys the same divine lethal judgment in an idiomatic, register-consistent form; the locked term เรานี่แหละคือผู้ที่ตรวจดูใจและจิตใจ is preserved verbatim and no theological meaning is altered. Because the KD for this verse does not document whether ด้วยความตาย is intentionally retained as a deliberate inter-corpus echo linking to the identical Greek phrase at Rev. 6:8, a native-speaker reviewer should confirm the change before it is applied.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_11_optimal_003 -->
### Revelation 11:16

**Current:**

> กราบลงบนใบหน้าของตน

**Proposed:**

> ก้มหน้าลงกราบถึงพื้น

**Why:** No key_decisions entry exists for 11:16. The Greek 'fell upon their faces' is a Semitic idiom for total prostration in worship; the Thai 'กราบลงบนใบหน้าของตน' renders it word-for-word, producing a phrase that Thai readers would parse as 'bowed down on their faces' — 'บนใบหน้าของตน' is a direct calque because กราบลง already implies a downward bowing motion, and Thai does not naturally describe prostration by naming the face as a landing surface. 'ก้มหน้าลงกราบถึงพื้น' (bend the face downward and bow to the ground) is the idiomatic Thai for full, face-floor prostration and carries the same meaning — the twenty-four elders are fully prostrate in worship before God. No theological change; the intensity of the act is preserved. Routed to defer_to_native because Thai prostration-language has register-specific conventions that warrant native-reviewer confirmation.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## redundant_directional (1)

<!-- POLISH_PROPOSAL id=mark_03_001 -->
### Mark 3:7

**Current:**

> เสด็จออกไปกับบรรดาสาวกของพระองค์ไปยัง

**Proposed:**

> เสด็จออกไปกับบรรดาสาวกของพระองค์ยัง

**Why:** The direction particle ไป occurs once in เสด็จออกไป and again in ไปยัง, creating an audible repeated-motion stumble. Dropping the second ไป keeps the destination marker ยัง and preserves the movement.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## register_drift (107)

<!-- POLISH_PROPOSAL id=matthew_10_optimal_002 -->
### Matthew 10:18

**Current:**

> และเพราะเราพวกท่านจะถูกนำไปอยู่ต่อหน้าบรรดาผู้ว่าราชการและกษัตริย์ทั้งหลาย เพื่อเป็นคำพยานแก่พวกเขาและแก่คนต่างชาติด้วย

**Proposed:**

> และพวกท่านจะถูกนำไปอยู่ต่อหน้าบรรดาผู้ว่าราชการและกษัตริย์ทั้งหลายเพราะเรา เพื่อเป็นคำพยานแก่พวกเขาและแก่คนต่างชาติด้วย

**Why:** The current Thai inserts 'เพราะเรา' between the clause-coordinating 'และ' and the subject 'พวกท่าน' — a word-order pattern that reads as translationese-stiff (register drifting toward literal-academic) and creates a secondary parsing risk, since a non-specialist reader may momentarily parse 'เพราะเรา' as 'because we' before the ราชาศัพท์ context resolves the royal pronoun. In natural Thai discourse, a short causal phrase like ἕนεκεν ἐมоῦ idiomatically follows the main predicate rather than wedging itself between a conjunction and the subject; the proposed reordering also happens to track the Greek itself more faithfully, where ἕνεκεν ἐμοῦ appears after ἀχθήσεσθε. All three locked phrases ('เพราะเรา,' 'พวกท่านจะถูกนำไปอยู่ต่อหน้าบรรดาผู้ว่าราชการและกษัตริย์ทั้งหลาย,' 'เพื่อเป็นคำพยานแก่พวกเขาและแก่คนต่างชาติด้วย') are preserved character-for-character; only their sequence within the verse changes. No theological content is altered. Routing to Tier-A Thai reviewer to confirm whether the reordered clause feels more natural in evangelical-formal Thai prose.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_11_optimal_001 -->
### Matthew 11:2

**Current:**

> เมื่อได้ยินในคุกถึงพระราชกิจของพระคริสต์

**Proposed:**

> ขณะที่อยู่ในคุก ได้ยินถึงพระราชกิจของพระคริสต์

**Why:** The current Thai places the locative 'ในคุก' between 'ได้ยิน' and its complement particle 'ถึง,' interrupting the standard Thai compound 'ได้ยินถึง' (heard about); this mirrors the Greek participial word order rather than Thai-native clause sequencing. The KD documents the lexical choices ('คุก,' 'พระราชกิจของพระคริสต์') but does not address the syntactic position of the locative. Thai natively fronts circumstantial states before the main predicate, so 'ขณะที่อยู่ในคุก ได้ยินถึง…' (while-being-in-prison, heard-about…) reads as natural Thai participial sequencing. All four locked terms ('ฝ่ายยอห์น,' 'ในคุก,' 'พระราชกิจของพระคริสต์,' 'จึงใช้สาวกของตนไป') are preserved verbatim; no theological change is introduced.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_13_optimal_001 -->
### Matthew 13:17

**Current:**

> เราบอกความจริงแก่พวกท่านว่า

**Proposed:**

> เราบอกพวกท่านตามจริงว่า

**Why:** The ἀμήν+λέγω solemn formula is corpus-established as 'เราบอกพวกท่านตามจริง' (KD1 cites Mark 3:28 as the formula anchor and lists 'เราบอกพวกท่านตามจริง' as the locked KD Thai term). The current text instead renders ἀμήν as a nominal object ('ความจริง', 'the truth') and restructures the indirect object as 'แก่พวกท่าน', yielding 'เราบอกความจริงแก่พวกท่านว่า' — a grammatically sound construction but one that breaks the established corpus formula and loses the adverbial register of ἀμήν as a solemn oath-particle. The proposed 'เราบอกพวกท่านตามจริงว่า' restores the locked formula verbatim ('ตามจริง' = adverbially 'in truth/truly', matching ἀมήν's function as a solemn-assertion intensifier rather than a referential noun), then appends 'ว่า' to introduce the ὅτι content-clause. This is a corpus-consistency correction, not a theological change; both renderings carry the same meaning. Because ἀมήน+λέγω occurs multiple times across Matthew, application should be preceded by a full formula-consistency audit of all occurrences before this verse is individually patched.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_15_optimal_001 -->
### Matthew 15:6

**Current:**

> โดยนัยนี้

**Proposed:**

> ด้วยเหตุนี้

**Why:** The Greek connecting particle here is a plain καί with no inferential-implication vocabulary — Jesus moves directly from the Corban illustration to his accusation. 'โดยนัยนี้' (lit. 'by this implication') introduces the abstract noun 'นัย' (connotation/implication), which sits in academic-commentary register rather than the optimal-evangelical-formal THSV2011 target; it reads more like a theological essay than narrative rebuke speech. 'ด้วยเหตุนี้' (for this reason / therefore) conveys the same causal-logical bridge in register-appropriate Thai without the abstract vocabulary. None of the locked KD terms for this verse (ผู้นั้นก็ไม่ต้องให้เกียรติบิดา [หรือมารดา] ของตน / พวกท่านได้ทำให้พระวจนะของพระเจ้าเป็นโมฆะ / เพราะเห็นแก่ธรรมเนียมของพวกท่าน) is affected, and the theological accusation is unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_24_optimal_003 -->
### Matthew 24:24

**Current:**

> เพื่อจะชักจูงแม้ผู้ที่ทรงเลือกให้หลงไป หากเป็นไปได้

**Proposed:**

> เพื่อจะนำแม้ผู้ที่ทรงเลือกให้หลงผิด หากเป็นไปได้

**Why:** KD1 for Matt 24:4 explicitly marks πλανάω as thematic across vv. 4, 5, 11, and 24, with the chapter-wide rendering 'นำ...ให้หลงผิด.' Verse 24 alone departs from this pattern with 'ชักจูง' (coax/entice), which is softer and lacks the directional going-astray image of πλανάω; 'นำให้หลงผิด' restores both the Greek sense and the established chapter idiom. All locked terms—'พระคริสต์เทียมและผู้พยากรณ์เทียม,' 'หมายสำคัญและการอัศจรรย์อันยิ่งใหญ่,' and the split lock 'แม้ผู้ที่ทรงเลือก...หากเป็นไปได้'—are fully preserved in the resulting verse. Flagged fyi because the variation may be deliberate (miraculous signs 'entice' in a way ordinary false teaching does not), and a corpus-wide πλανάω harmony audit is recommended before committing.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_24_optimal_002 -->
### Matthew 24:50

**Current:**

> ในวันที่เขาไม่คาดหวัง และในชั่วโมงที่เขาไม่รู้

**Proposed:**

> ในวันที่เขาไม่คาดคิด และในชั่วโมงที่เขาไม่รู้

**Why:** Thai 'คาดหวัง' carries a positive-expectation or hopeful-longing nuance ('was hoping for'), subtly misaligned with the neutral watchful-anticipation sense of προσδοκάω. In the bad-slave scenario the word invites a reading of 'wasn't looking forward to it'—technically true but with emotional colouring absent from the Greek. 'ไม่คาดคิด' (not having foreseen/anticipated) is semantically neutral and matches the identical eschatological-surprise phrase in v.44 ('ในชั่วโมงที่พวกท่านไม่คาดคิด'), restoring chapter-level consistency. The locked parallelism frame 'ในวัน...ในชั่วโมง' is preserved verbatim in the proposed text; no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_27_optimal_002 -->
### Matthew 27:39

**Current:**

> ส่ายศีรษะของพวกเขา

**Proposed:**

> ส่ายศีรษะ

**Why:** The Greek κινοῦντες τὰς κεφαλὰς αὐτῶν carries the explicit possessive αὐτῶν, which the Thai mirrors literally as 'ของพวกเขา.' In natural Thai narrative, when the established subject performs an action on their own body part, the possessive pronoun is characteristically omitted—'ส่ายศีรษะ' alone is the idiomatic form and precisely the term locked in KD2. The suffix 'ของพวกเขา' tips the phrase toward translationese-stiff, slightly disrupting the THSV2011 register. Dropping only that suffix preserves both the locked term ส่ายศีรษะ and the LXX Psalm 22:7 allusion the translator explicitly notes, with no theological change; however, whether the possessive is natural enough in this specific context is a fine call best confirmed by a Tier-A Thai-language reviewer.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_28_optimal_001 -->
### Matthew 28:14

**Current:**

> และพวกเราจะทำให้พวกท่านไม่ต้องกังวล

**Proposed:**

> และจะทำให้พวกท่านไม่ต้องกังวล

**Why:** The Greek second clause carries no explicit ἡμεῖς — the subject is implicit, continuing from the first clause's πείσομεν. KD2 documents ἡμεῖς as emphatic only for the first clause (with เอง added to reinforce it); no KD entry motivates repeating พวกเรา before ποιήσομεν. Thai discourse regularly elides a co-referent subject in conjoined verb phrases when the reference is unambiguous, and spelling it out again across two แล้ว-adjacent clauses produces a faintly mechanical, word-for-word rhythm that tilts toward translationese-stiff. Dropping พวกเรา before จะทำให้ tightens the pair into a single flowing promise without altering meaning or theology; the locked phrase จะทำให้พวกท่านไม่ต้องกังวล is preserved verbatim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_01_optimal_002 -->
### Mark 1:28

**Current:**

> ทั่วทุกแห่งในเขตทั่วทั้งแคว้นกาลิลี

**Proposed:**

> ทั่วบริเวณแคว้นกาลิลีทุกแห่ง

**Why:** The current phrase stacks two instances of ทั่ว (ทั่วทุกแห่ง rendering πανταχοῦ and ทั่วทั้ง rendering ὅλην) with เขต sandwiched between them for περίχωρον, producing the ungainly chain 'everywhere in the zone throughout all of Galilee' — a literal Greek word-order transfer that does not sit naturally in Thai prose. The proposed ทั่วบริเวณแคว้นกาลิลีทุกแห่ง uses บริเวณ for περίχωρον ('surrounding area') and ทุกแห่ง to carry the combined scope of πανταχοῦ + ὅลην, collapsing the redundant double-ทั่ว without dropping semantic content. The locked term กิตติศัพท์ is unaffected and no theological content changes. Deferring to Tier-A Thai reviewer to confirm that the single-ทั่ว restructuring reads as equally emphatic to a native ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_01_optimal_001 -->
### Mark 1:6

**Current:**

> สายคาดเอวทำด้วยหนังรัดรอบเอว

**Proposed:**

> สายคาดเอวหนัง

**Why:** The current Thai renders three discrete Greek elements word-for-word — ζώνην (สายคาดเอว) + δερματίνην (ทำด้วยหนัง) + περὶ τὴν ὀσφύν (รัดรอบเอว) — causing เอว to appear twice in close succession, a textbook translationese artifact. Thai natively compounds the concept as สายคาดเอวหนัง ('leather waist-belt'), in which the wrapping-around-the-waist function is already entailed by the compound สายคาดเอว; the modifier หนัง carries δερματίνην cleanly. All three Greek semantic components (leather, belt, worn at the waist) are preserved; neither locked term (แต่งกายด้วย, กิน) is affected; no theological meaning changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_06_optimal_001 -->
### Mark 6:2

**Current:**

> ก็เป็นเช่นนี้ได้อย่างไร?

**Proposed:**

> ก็เกิดขึ้นได้อย่างไร?

**Why:** Thai 'เป็นเช่นนี้' renders γίνομαι (γινόμεναι, 'happening/coming about') as a static state-verb ('be like this'), whereas γίνομαι denotes occurrence or arising — not a condition of resemblance. Thai 'เกิดขึ้น' (to arise, come to pass) maps the occurrence-sense of γίνομαι precisely and is the standard Thai verb in questions of the form 'how can X happen/come about?' The demonstrative 'เช่นนี้' (like this) is also redundant: the locked phrase 'ฤทธิ์อำนาจอันยิ่งใหญ่' already absorbs the τοιαῦται (such/of this kind) force, making 'เป็นเช่นนี้' circular and translationese-stiff. The proposed 'ก็เกิดขึ้นได้อย่างไร?' (and how do they come about?) is natural Thai interrogative phrasing that preserves the rhetorical-question register and the logical parallel with the two preceding questions. No KD rationale addresses or justifies 'เป็นเช่นนี้' specifically; all six locked terms for this verse are preserved verbatim; the theological content — how are such mighty works performed through his hands? — is unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_08_optimal_001 -->
### Mark 8:14

**Current:**

> พวกเขามีขนมปังอยู่กับพวกเขาในเรือเพียงก้อนเดียวเท่านั้น

**Proposed:**

> พวกเขามีขนมปังอยู่ในเรือเพียงก้อนเดียวเท่านั้น

**Why:** The phrase 'อยู่กับพวกเขา' word-mirrors the Greek reflexive μεθ' ἑαυτῶν, but in Thai 'พวกเขา' is already the grammatical subject of the very same clause, so restating it as the complement of 'กับ' produces an unnatural loop ('they had bread with them') that no fluent Thai writer would generate; Thai expresses the same sense of on-board possession simply through subject + 'มี' + locative. Dropping 'กับพวกเขา' removes this translationese-stiff artifact without losing any information: location ('ในเรือ') and subject ('พวกเขามี') together fully render 'they had [it] with them in the boat.' All locked terms ('เพียงก้อนเดียวเท่านั้น,' 'ขนมปัง…ก้อนเดียว,' and 'ลืม' in the first clause) are preserved verbatim, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_11_optimal_002 -->
### Mark 11:13

**Current:**

> แต่เมื่อเสด็จถึงก็ไม่พบสิ่งใดเลยนอกจากใบ

**Proposed:**

> แต่เมื่อเสด็จถึงก็ไม่ทรงพบสิ่งใดเลยนอกจากใบ

**Why:** The main-clause verb εὗρεν has Jesus as its subject yet is rendered ไม่พบ without the ราชาศัพท์ prefix ทรง-, while every other Jesus-subject action verb in the same verse carries ราชาศัพท์ (ทอดพระเนตร, เสด็จไป, เสด็จถึง). No key_decision documents an intentional exception here. Adding ทรง- restores the ราชาศัพท์ consistency expected at the THSV2011 register for a Jesus-subject main-clause verb. Whether Thai stylistic convention permits dropping ทรง- on a result-clause verb that immediately follows a ราชาศัพท์ motion verb in the same breath-unit is a register judgment best confirmed by the Tier-A Thai reviewer. The meaning is identical; all locked terms (ต้นมะเดื่อ, ทอดพระเนตรเห็น…แต่ไกล, เพราะยังไม่ถึงฤดูมะเดื่อ) lie outside the changed substring and are unaffected; no theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=mark_15_optimal_001 -->
### Mark 15:16

**Current:**

> เรียกทหารทั้งกองมาประชุมกัน

**Proposed:**

> เรียกทหารทั้งกองมาพร้อมกัน

**Why:** συγκαλέω in a military context denotes a muster or assembly call — soldiers being summoned to action — not a committee or deliberative gathering. Modern Thai 'ประชุมกัน' primarily evokes a formal meeting or conference session (boardroom, committee), creating a subtle bureaucratic register drift that is mismatched to the Roman Praetorium military setting. KD3 for this verse documents only the ทหารทั้งกอง rendering (σπεῖρα → cohort) and does not address the verb of assembly; the 'ประชุมกัน' rendering is therefore not covered by an existing rationale lock. Replacing 'ประชุมกัน' with 'มาพร้อมกัน' ('assembled/came together') fits the military-muster register, preserves the locked term ทหารทั้งกอง verbatim, and introduces no theological change — the whole cohort still converges, but in the register of troops being mustered rather than officials being convened.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_01_optimal_001 -->
### Luke 1:78

**Current:**

> ด้วยพระเมตตาอันอ่อนโยนของพระเจ้าของเรา ซึ่งโดยพระเมตตานั้น ดวงรุ่งอรุณจากเบื้องสูงจะเสด็จมาเยี่ยมเยียนเรา

**Proposed:**

> ด้วยพระเมตตาอันอ่อนโยนของพระเจ้าของเรา ดวงรุ่งอรุณจากเบื้องสูงจะเสด็จมาเยี่ยมเยียนเรา

**Why:** The connector phrase 'ซึ่งโดยพระเมตตานั้น' stacks three distinct connective elements — relative pronoun (ซึ่ง), instrumental preposition (โดย), and resumptive demonstrative noun phrase (พระเมตตานั้น) — to render the single Greek relative clause ἐν οἷς, producing a stilted, translationese-heavy phrase that drifts below the THSV2011 register of respectful-modern-accessible prose. No key_decision rationale documents or justifies this three-way stack: KD1 covers the locked term 'ด้วยพระเมตตาอันอ่อนโยนของพระเจ้าของเรา' and KD2 covers 'ดวงรุ่งอรุณจากเบื้องสูงจะเสด็จมาเยี่ยมเยียนเรา', but neither addresses the connector between them. In natural modern Thai the causal-instrumental relationship is already established by the opening ด้วย; the relative resumption is therefore redundant and creates an unnatural doubling of the mercy-reference that a native Thai ear would register as bookish. The proposed text eliminates 'ซึ่งโดยพระเมตตานั้น' entirely, preserves both locked terms verbatim in their documented forms, and maintains the full theological content — the tender mercy of God remains the means by which the dawn from on high visits us. This is a surface-register polish, not a theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_10_optimal_001 -->
### Luke 10:13

**Current:**

> การอัศจรรย์ทั้งหลายที่ได้กระทำในเจ้าได้กระทำในเมืองไทระและไซดอน

**Proposed:**

> การอัศจรรย์ทั้งหลายที่เกิดขึ้นในเจ้าได้เกิดขึ้นในเมืองไทระและไซดอน

**Why:** The Greek verb γίνομαι (happen, occur, come to pass) appears twice in this clause — once as a participle modifying the miracles ('that happened/occurred among you') and once as the conditional aorist ('if they had occurred in Tyre and Sidon') — yet both instances are rendered 'กระทำ' (to perform/do), which belongs to the semantic field of deliberate action (ποιέω/πράσσω) rather than occurrence. The back-to-back 'ที่ได้กระทำในเจ้าได้กระทำ' reads translationese-stiff, with the near-identical strings colliding in a single conditional clause. Replacing both with 'เกิดขึ้น' (happen, come about) is more faithful to γίνομαι's core sense and breaks the mechanical repetition without changing the meaning; the locked term 'การอัศจรรย์ทั้งหลาย' is preserved verbatim and 'เมืองไทระและไซดอน' is unchanged. No theological shift is involved — the miracles still occurred under the same implied divine agency.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_11_optimal_001 -->
### Luke 11:46

**Current:**

> วิบัติแก่พวกเจ้าผู้เชี่ยวชาญทางบัญญัติด้วย เพราะพวกเจ้าวางภาระหนักเกินจะแบกไว้บนผู้คน แต่พวกเจ้าเองไม่แตะต้องภาระเหล่านั้นแม้ด้วยปลายนิ้วเดียว

**Proposed:**

> วิบัติแก่พวกท่านผู้เชี่ยวชาญทางบัญญัติด้วย เพราะพวกท่านวางภาระหนักเกินจะแบกไว้บนผู้คน แต่พวกท่านเองไม่แตะต้องภาระเหล่านั้นแม้ด้วยปลายนิ้วเดียว

**Why:** The Pharisee woes (vv. 42–44) address their audience as พวกท่าน (formal-respectful ท่าน), which is corpus-locked at v. 42 (วิบัติแก่พวกท่านฟาริสี). The lawyer woes (vv. 46–52) shift wholesale to พวกเจ้า — a distinct second-person form that in Thai carries a mildly superior-to-inferior or archaic coloring — without any KD documentation explaining the change. The Greek uses the identical pronoun ὑμεῖς/ὑμῖν for both groups throughout; the parallel prophetic-woe formula argues for consistent register treatment. In THSV2011-register biblical Thai, ท่าน is the standard formal second-person address in prophetic-denunciation contexts, while เจ้า can read as either archaic-formal or subtly condescending, and the unexplained asymmetry risks register inconsistency within a tightly structured pericope. Flagged FYI rather than apply because: (a) correcting it requires a mini-corpus pass spanning vv. 46, 47, 48, and 52; (b) the translator may have deliberately differentiated the two groups after the lawyer's direct challenge in v. 45 — a rhetorical rationale that is plausible but undocumented and should be captured in the KD ledger regardless of which pronoun is retained; and (c) no theological meaning is altered either way.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_12_optimal_003 -->
### Luke 12:25

**Current:**

> สามารถเพิ่มอายุของตนให้ยืนยาวออกไปแม้สักชั่วโมงได้

**Proposed:**

> สามารถเพิ่มอายุของตนแม้สักชั่วโมงได้

**Why:** The Greek is simply προσθεῖναι ἐπὶ τὴν ἡλικίαν αὐτοῦ πῆχυν — 'add a single cubit to his lifespan.' KD1 locks อายุ and KD2 locks สักชั่วโมง; both are preserved verbatim in the proposal. The complement 'ให้ยืนยาวออกไป' (make it stretch further) is redundant after 'เพิ่มอายุ', whose meaning already entails lengthening; no KD entry documents this verbose expansion. Removing it brings the clause to the compact, accessible THSV2011 register without altering meaning, theology, or any locked term.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_16_optimal_001 -->
### Luke 16:3

**Current:**

> นายของเรากำลังริบหน้าที่พ่อบ้านไปจากเราแล้ว

**Proposed:**

> นายของเรากำลังปลดเราออกจากหน้าที่พ่อบ้านแล้ว

**Why:** ἀφαιρέω means 'take away / remove' with no connotation of forcible confiscation; Thai 'ริบ' characteristically collocates with tangible assets (ริบทรัพย์สิน — seize property) rather than with an office or duty, making 'ริบหน้าที่' an unusual and slightly stiff collocation that signals translationese rather than natural internal-monologue register. Independently, v.4's locked term establishes 'ปลดออกจากหน้าที่พ่อบ้าน' for the identical dismissal-from-office concept; adopting 'ปลด' in the manager's subjective v.3 monologue normalises the intra-chapter lexical pattern without any shift in meaning. The proposed rendering 'กำลังปลดเราออกจากหน้าที่พ่อบ้านแล้ว' preserves the locked term 'นายของเรา' verbatim, carries the same dismissal sense as the Greek, and introduces no theological change whatsoever.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_22_optimal_001 -->
### Luke 22:24

**Current:**

> การโต้เถียงกันเกิดขึ้นในหมู่พวกเขา

**Proposed:**

> เกิดการโต้เถียงกันขึ้นในหมู่พวกเขา

**Why:** The current rendering mirrors Greek word order (nominal subject φιλονεικία fronted before existential verb Ἐγένετο), producing a translationese-stiff construction in Thai. Standard Thai existential/inchoative clauses front the emergence verb เกิด before the noun, yielding the natural pattern เกิด[noun]ขึ้น (cf. เกิดปัญหาขึ้น, เกิดการทะเลาะกันขึ้น, เกิดเหตุขึ้น). The proposed reordering 'เกิดการโต้เถียงกันขึ้นในหมู่พวกเขา' preserves the locked key-term 'การโต้เถียง' verbatim and carries identical meaning ('a dispute arose among them'); no theological content is altered. A Tier-A Thai reviewer should confirm whether the THSV2011 formal-literary register consistently favours the noun-fronted or verb-fronted pattern in narrative discourse before applying.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_24_optimal_002 -->
### Luke 24:19

**Current:**

> ผู้เป็นผู้เผยพระวจนะทรงฤทธิ์

**Proposed:**

> ซึ่งเป็นผู้เผยพระวจนะทรงฤทธิ์

**Why:** The current text uses ผู้ simultaneously as a relative pronoun ('the one who') and as the nominalizer prefix of ผู้เผยพระวจนะ, producing a double-ผู้ sequence ('ผู้เป็นผู้เผย…') that is mildly clunky in modern Thai prose; the relative pronoun ซึ่ง is the more natural choice when the predicate noun already carries ผู้ as a built-in prefix. The proposed rendering preserves the locked substring 'ผู้เผยพระวจนะทรงฤทธิ์ทั้งในด้านการกระทำและถ้อยคำ' verbatim and conveys the identical relative-clause meaning of ὃς ἐγένετο. No KD for this verse documents or justifies the ผู้เป็น construction specifically; this is purely a surface-fluency normalization that may benefit from a corpus-wide check of how ὃς/ἥ/ὅ ἐγένετο preceding ผู้-nouns is handled across the translation.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_24_optimal_001 -->
### Luke 24:25

**Current:**

> โอ คนโง่เขลาและเชื่อช้าในใจต่อทุกสิ่งที่พวกผู้เผยพระวจนะได้กล่าวเอ๋ย

**Proposed:**

> โอ คนโง่เขลาเอ๋ย และเชื่อช้าในใจต่อทุกสิ่งที่พวกผู้เผยพระวจนะได้กล่าว

**Why:** In standard Thai, the vocative particle เอ๋ย must immediately follow the noun it addresses (e.g., คนโง่เขลาเอ๋ย), not trail at the end of a long relative-clause modifier; current placement after '...ที่พวกผู้เผยพระวจนะได้กล่าว' is non-standard and reads as translationese-stiff rather than THSV2011 natural register. Moving เอ๋ย to directly after คนโง่เขลา restores the idiomatic Thai vocative pattern while keeping the coordinate conjunction และ intact and all three locked terms verbatim — 'โอ คนโง่เขลา' appears as a substring, 'เชื่อช้าในใจ' and 'ต่อทุกสิ่งที่พวกผู้เผยพระวจนะได้กล่าว' are unchanged. The KD1 rationale addresses Ὦ → โอ but does not document or justify the trailing เอ๋ย placement; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_02_optimal_002 -->
### John 2:21

**Current:**

> ทรงตรัสถึง

**Proposed:**

> ตรัสถึง

**Why:** Thai 'ตรัส' is itself the corpus-standard royal speech verb for Jesus; it already encodes the honorific grade that 'ทรง-' would supply. Prefixing it with 'ทรง-' produces a double-honorific ('ทรงตรัส') that is inconsistent with the rest of John 2, where the same Greek speech lemmas (λέγω / εἶπεν / ἔλεγεν referring to Jesus) are rendered with bare 'ตรัส' throughout (vv. 4, 8, 16, 19). This isolated double-honorific constitutes register drift toward translationese-stiff relative to the surrounding corpus. Dropping 'ทรง-' restores intra-chapter consistency without altering meaning, theology, or either locked term ('พระองค์' and 'พระวิหารแห่งพระกายของพระองค์เอง', both preserved verbatim).

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_02_optimal_004 -->
### John 2:22

**Current:**

> ทรงเคยตรัสเช่นนี้

**Proposed:**

> เคยตรัสเช่นนี้

**Why:** Same double-honorific pattern flagged in v.21 — 'ทรงตรัส' appears twice in this verse ('ทรงเคยตรัสเช่นนี้' and 'พระเยซูทรงตรัสไว้'), both inconsistent with the corpus norm of bare 'ตรัส' for Jesus' speech. Surfaced as fyi rather than apply because correcting both instances here in tandem with v.21 constitutes a mini corpus-normalization pass that should be reviewed as a set rather than verse-by-verse. Locked term 'เชื่อพระคัมภีร์และพระดำรัส' and 'ทรงเป็นขึ้นจากความตาย' (where 'ทรง-' is required because 'เป็นขึ้น' is not itself a royal verb) are unaffected by either instance of the proposed change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_05_optimal_001 -->
### John 5:42

**Current:**

> เรารู้จักพวกท่าน — พวกท่านไม่มีความรักต่อพระเจ้าในตนเอง

**Proposed:**

> เรารู้จักพวกท่านว่า พวกท่านไม่มีความรักต่อพระเจ้าในตนเอง

**Why:** The Greek ὅτι functions here as a standard indirect-content subordinator, introducing what Jesus knows: 'I have known you that you do not have the love of God in yourselves.' The Thai renders this clause-link with an em-dash (—) rather than the native ว่า connector. In THSV2011-register formal biblical prose, ว่า is the unmarked, natural choice for ὅτι-content clauses after verbs of knowing; the em-dash is more typical of literary or journalistic Thai typography and risks reading as a dramatic-pause interjection rather than a logical subordination. No KD rationale documents a specific reason for the dash over ว่า. The proposed ว่า preserves both locked terms verbatim (เรารู้จักพวกท่าน and พวกท่านไม่มีความรักต่อพระเจ้าในตนเอง), accurately maps the ὅτι structure, and aligns with standard Thai biblical register. This is a surface connector adjustment with no theological implication whatsoever.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_07_optimal_001 -->
### John 7:45

**Current:**

> ซึ่งพวกนั้นถามว่า

**Proposed:**

> แล้วพวกนั้นก็ถามว่า

**Why:** The construction 'ซึ่งพวกนั้นถามว่า' pairs a relative pronoun (ซึ่ง) with a resumptive subject pronoun (พวกนั้น) within the same clause — a pattern that does not occur in natural Thai narrative prose and produces translationese-stiff register. Standard Thai connects consecutive narrative events (officers-arrive → leaders-speak) with the coordinate sequence marker 'แล้ว...ก็' rather than a relative clause with a gap-filling resumptive. The proposed 'แล้วพวกนั้นก็ถามว่า' converts the awkward relative structure into a fluent sequential clause, matching the THSV2011 register target of respectful, modern, accessible prose. Both locked terms ('พวกเจ้าหน้าที่' and 'ทำไมพวกเจ้าจึงไม่จับเขามา') are preserved verbatim, and no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_08_optimal_001 -->
### John 8:44

**Current:**

> พวกท่านปรารถนาจะทำตามความปรารถนาของบิดาของพวกท่าน

**Proposed:**

> พวกท่านต้องการทำตามความปรารถนาของบิดาของพวกท่าน

**Why:** The verb 'ปรารถนา' (to earnestly wish/desire) used for θέλετε creates an immediate root-collision with 'ความปรารถนา' used for ἐπιθυμίαις two words later — 'ปรารถนาจะทำตามความปรารถนา' is noticeably stilted repetition in Thai. The natural formal-register Thai equivalent for θέλω is 'ต้องการ' (to want/need), which also restores the Greek's deliberate lexical distinction: θέλω (volitional willing) vs. ἐπιθυμίαι (strong desires/lusts). Using two different Thai roots to render two different Greek lemmas improves both readability and semantic precision without altering the theological charge of either term. All locked terms in the verse — มาร, ผู้ฆ่ามนุษย์, ผู้พูดเท็จ, บิดาของการมุสา — remain verbatim; no theological meaning changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_11_optimal_001 -->
### John 11:4

**Current:**

> ความป่วยนี้จะไม่จบลงด้วยความตาย แต่เป็นไปเพื่อพระสิริของพระเจ้า เพื่อพระบุตรของพระเจ้าจะได้รับพระสิริผ่านความป่วยนี้

**Proposed:**

> ความเจ็บป่วยนี้จะไม่จบลงด้วยความตาย แต่เป็นไปเพื่อพระสิริของพระเจ้า เพื่อพระบุตรของพระเจ้าจะได้รับพระสิริผ่านความเจ็บป่วยนี้

**Why:** The nominalization 'ความป่วย' (used twice in the verse) is grammatically possible but statistically uncommon as a standalone Thai noun; the standard formal Thai compound is 'ความเจ็บป่วย,' which is the normal THSV2011-register rendering for illness as an abstract noun. No KD locks 'ความป่วย' as a term; the two KD-locked items for this verse — 'เพื่อพระสิริของพระเจ้า' and 'พระบุตรของพระเจ้า' — are preserved verbatim in the proposal. The change is purely a surface-form normalization with zero theological effect. Flagged FYI rather than apply or defer_to_native because the translator may have deliberately chosen 'ความป่วย' to create a lexical-root echo of v.1's 'กำลังป่วย' (same ป่วย stem), a legitimate cohesion device; if that echo is intentional, the current form should stand and this proposal should be dismissed.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_13_optimal_002 -->
### John 13:10

**Current:**

> ก็ไม่จำเป็นต้องล้างใดๆ อีก เว้นแต่เพียงเท้าเท่านั้น

**Proposed:**

> ก็ไม่จำเป็นต้องล้างอีก เว้นแต่เท้าเท่านั้น

**Why:** The Greek οὐκ ἔχει χρείαν εἰ μὴ τοὺς πόδας νίψασθαι ('has no need except to wash the feet') is rendered with five stacked limiting words: ใดๆ (any), อีก (more), เว้นแต่ (except), เพียง (only), and เท่านั้น (alone). The clusters ใดๆ อีก and เพียง … เท่านั้น each independently cap the exception, creating translationese-stiff double qualification; เว้นแต่ … เท่านั้น already fully expresses 'only the feet.' Removing ใดๆ and เพียง yields natural THSV-register Thai without semantic loss. Locked phrases ผู้ที่อาบน้ำแล้ว (before) and ก็สะอาดทั้งกาย (after) are unaffected; a Tier-A Thai reviewer should confirm whether the qualifiers feel naturally emphatic or merely wordy in this context.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_13_optimal_003 -->
### John 13:19

**Current:**

> เพื่อเมื่อมันเกิดขึ้น

**Proposed:**

> เพื่อเมื่อสิ่งนั้นเกิดขึ้น

**Why:** The pronoun มัน back-references เหตุการณ์ from the preceding clause; while มัน is standard in modern colloquial Thai for inanimate or abstract referents, it carries a mildly casual register signature that can sit below the THSV2011 formal-evangelical target. สิ่งนั้น (that thing/event) is the register-appropriate formal alternative for a back-reference to an abstract prophetic occurrence. The locked absolute I-AM formula เราเป็น is preserved unchanged; no theological content is altered. A Tier-A Thai reviewer should confirm whether มัน is within acceptable THSV register range for a solemn predictive utterance of Jesus.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_14_optimal_001 -->
### John 14:11

**Current:**

> จงเชื่อเราเถิดที่ว่า

**Proposed:**

> จงเชื่อเราเถิดว่า

**Why:** Greek ὅτι after πιστεύετέ μοι is a plain content-clause complementizer ('that'); in Thai it attaches most naturally to a verb of belief as bare 'ว่า' (เชื่อ [object] ว่า). The current 'ที่ว่า' relativizes the complement into a nominal structure ('believe us in that-which-says…'), producing a mildly stiff, translationese construction that jars against the surrounding imperative register. Removing 'ที่' yields 'จงเชื่อเราเถิดว่า', the standard pattern used throughout modern Christian Thai literature and consistent with the THSV2011 target register. The semantic content is unchanged, no theological shift is introduced, and the locked phrase 'ก็จงเชื่อเพราะพระราชกิจเหล่านั้นเอง' in the following clause is unaffected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_14_optimal_002 -->
### John 14:29

**Current:**

> เมื่อมันเกิดขึ้น

**Proposed:**

> เมื่อสิ่งนั้นเกิดขึ้น

**Why:** The Greek ὅταν γένηται ('when it happens') requires an anaphoric pronoun referring to the foretold events. Thai 'มัน' is the colloquial default for inanimate referents in everyday speech; however, in the optimal-evangelical-formal register targeting THSV2011, formal written Thai uses 'สิ่งนั้น' (that thing) or 'เหตุการณ์นั้น' (those events) for solemn prophetic discourse. The slip is mild but consistent with a register standard the rest of chapter 14 upholds. Replacing 'มัน' with 'สิ่งนั้น' is a surface register correction with no semantic or theological change; there are no locked terms in this verse.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_15_optimal_001 -->
### John 15:4

**Current:**

> พวกท่านก็เช่นกัน ถ้าไม่คงอยู่ในเรา พวกท่านก็เกิดผลไม่ได้

**Proposed:**

> พวกท่านก็เช่นกัน ถ้าไม่คงอยู่ในเรา ก็เกิดผลไม่ได้

**Why:** The subject pronoun 'พวกท่าน' appears twice within the same short clause ('พวกท่านก็เช่นกัน … พวกท่านก็เกิดผลไม่ได้'), re-stating a referent established only four words earlier. In idiomatic Thai, pronoun drop when the subject is immediately clear is the unmarked norm; retaining it reads as translationese-stiff, mirroring English/Greek subject-marking rather than Thai discourse rhythm. The Greek itself places ὑμεῖς only once in this clause (οὕτως οὐδὲ ὑμεῖς ἐὰν μὴ ἐν ἐμοὶ μένητε), so the second 'พวกท่าน' has no Greek counterpart. Dropping it leaves 'ก็เกิดผลไม่ได้' as a natural Thai conditional apodosis with subject implied from immediate context; neither KD1 nor KD2 locks or documents this half of the verse, all locked terms (คงอยู่, เกิดผลไม่ได้) are preserved verbatim, and no theological meaning changes. Flagged defer_to_native because whether the repetition is intended to carry rhetorical contrast-emphasis ('you—specifically you—cannot bear fruit') versus simply being redundant is a judgment requiring a native Thai ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_21_optimal_001 -->
### John 21:15

**Current:**

> เมื่อพวกเขาทานอาหารเช้าเสร็จแล้ว

**Proposed:**

> เมื่อพวกเขารับประทานอาหารเช้าเสร็จแล้ว

**Why:** The narrative verb ทาน sits one register below the consistently formal-elevated THSV2011 level maintained throughout this scene. The v.12 key decision locks รับประทานอาหารเช้า as Christ's direct-speech invitation (มาเถิด มารับประทานอาหารเช้ากัน); carrying the same lexeme into the immediately following narrative clause preserves intra-episode lexical consistency and avoids a perceptible formality dip. The Greek ἠρίστησαν carries no colloquial nuance, so ทาน represents a surface register slip rather than a meaning choice. No locked terms are affected and no theological content is involved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_21_optimal_002 -->
### John 21:20

**Current:**

> ซึ่งเป็นผู้ที่ได้พิงพระองค์ในมื้ออาหาร

**Proposed:**

> ผู้ซึ่งได้พิงพระองค์ในมื้ออาหาร

**Why:** The construction ซึ่งเป็นผู้ที่ is a translationese artifact of rendering the Greek relative pronoun ὃς with an explicit copula (เป็น) and classifier (ผู้); Thai achieves the identical relative-clause sense more naturally with ผู้ซึ่ง, shedding the redundant เป็นผู้ that adds stiffness without semantic contribution. The locked phrase ได้พิงพระองค์ในมื้ออาหาร is preserved verbatim. The change is purely syntactic-surface and carries no theological implication; the reference to the Beloved Disciple's position at the Last Supper remains fully intact.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_04_optimal_001 -->
### Acts 4:22

**Current:**

> ชายผู้เกิดเหตุหมายสำคัญแห่งการรักษาครั้งนี้นั้น

**Proposed:**

> ชายที่หมายสำคัญแห่งการรักษาครั้งนี้เกิดขึ้นกับเขา

**Why:** The agentive nominal 'ผู้เกิดเหตุ' attempts to render ἐφ᾽ ὃν γεγόνει ('upon whom the sign had occurred'), but in contemporary Thai 'เกิดเหตุ' and its nominalization 'ผู้เกิดเหตุ' carry a police-report / news-broadcast register connotation — the person involved in an accident or crime incident — that sits incongruously against a miracle-healing context and drifts below the optimal THSV2011 evangelical-formal register. The proposed full relative-clause 'ชายที่หมายสำคัญแห่งการรักษาครั้งนี้เกิดขึ้นกับเขา' renders the identical Greek construction naturally in formal literary Thai, preserves the locked term 'หมายสำคัญแห่งการรักษา' verbatim, and leaves both other locked terms ('มีอายุกว่าสี่สิบปี' and 'หมายสำคัญแห่งการรักษา') intact. No theological content is altered; this is a surface-register adjustment to the descriptive relative clause identifying the formerly-lame man. A Tier-A native Thai reviewer should confirm whether 'ผู้เกิดเหตุ' reads as markedly journalistic to a modern audience before applying.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_07_optimal_001 -->
### Acts 7:55

**Current:**

> เห็นพระสิริของพระเจ้าและเห็นพระเยซูทรงยืนอยู่

**Proposed:**

> เห็นพระสิริของพระเจ้าและพระเยซูทรงยืนอยู่

**Why:** The Greek has a single aorist εἶδεν governing two coordinate objects joined by καί ('saw the glory of God and Jesus standing'), yet the Thai repeats เห็น before the second object, a doubling absent from the Greek and undocumented in any KD rationale. In Thai narrative prose, the เห็น X และเห็น Y pattern reads slightly translationese-stiff compared with the natural single-verb-two-object structure (เห็น X และ Y). Dropping the second เห็น restores that natural flow, leaves the locked phrase พระเยซูทรงยืนอยู่ ณ เบื้องขวาพระหัตถ์ของพระเจ้า fully intact, and alters no theological content. Whether the translator intended the repetition to mark two distinct revelatory moments (glory versus the person of Jesus) is a register judgment that requires a native-ear sign-off before committing.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_14_optimal_001 -->
### Acts 14:18

**Current:**

> แม้พูดเช่นนี้แล้ว

**Proposed:**

> แม้กล่าวเช่นนี้แล้ว

**Why:** ταῦτα λέγοντες ('while saying these things') is rendered with the everyday verb พูด, yet every other narrative speech-act verb in Acts 14 uses กล่าว (vv. 3, 10, 15), which sits squarely at the THSV2011 register — respectful, literary, one register step above unmarked daily speech. พูด is the colloquially neutral Thai default and reads slightly below the formal-evangelical target register in this narrative frame. Replacing it with กล่าว is a surface-only change: identical lexical meaning, identical referent (the speech just delivered in vv. 15–17), and no locked terms are affected — both locked phrases in v.18 (ยากที่จะห้าม and ไม่ให้ถวายเครื่องบูชาแก่พวกเขา) remain verbatim. A native Tier-A Thai-language reviewer should confirm whether พูด carries a colloquial tinge here or reads as register-neutral in this particular narrative clause.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_15_optimal_001 -->
### Acts 15:22

**Current:**

> เห็นสมควรว่าควรเลือกชายบางคนในพวกเขาส่งไปยังเมืองอันทิโอก

**Proposed:**

> เห็นสมควรที่จะเลือกชายบางคนในพวกเขาส่งไปยังเมืองอันทิโอก

**Why:** The complement construction 'เห็นสมควรว่าควรเลือก' is translationese-stiff: 'ว่าควร' (that one should) is functionally redundant after 'เห็นสมควร' (deemed appropriate/fitting), since both words carry the propriety-sense and the stacking of the two creates an English-shaped embedded-clause pattern foreign to natural Thai. The identical verb phrase recurs six verses later in v.28 as 'เห็นสมควรที่จะไม่วางภาระ', where the more natural Thai infinitival complement 'ที่จะ + verb' is already in place — showing the translator knows the idiomatic construction. Harmonising v.22 to 'เห็นสมควรที่จะเลือก' removes the stiffness and brings the council-decision language into register-consistency with v.28 within the same letter. The locked term 'บรรดาอัครทูต ผู้ปกครองคริสตจักร พร้อมทั้งคริสตจักรทั้งหมดเห็นสมควร' is preserved verbatim; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_17_optimal_002 -->
### Acts 17:18

**Current:**

> กำลังจะพูดอะไร?

**Proposed:**

> อยากจะพูดอะไรกัน?

**Why:** The Greek uses ἄν + potential optative of θέλω (τί ἂν θέλοι ὁ σπερμολόγος οὗτος λέγειν), a construction that in Athenian rhetorical-pejorative speech encodes contemptuous incredulity — 'what could this babbler possibly want to say?' Thai กำลังจะพูดอะไร? is a neutral future-progressive that drops both θέλω (want/wish) and the deliberative-contemptuous modal force of the optative-with-ἄν, flattening the philosophers' intellectual sneer into a plain information-seeking question. อยากจะ restores the θέลω nuance, while the particle กัน? adds rhetorical-dismissive force appropriate to the deliberative optative without slipping into colloquial-loose register. The KD3 rationale addresses only σπερμολόγος → คนช่างเก็บเล็กผสมน้อยคนนี้; the verb clause is undocumented. Because the optimal Thai formulation for Athenian philosophical contempt turns on register feel, a Tier-A native reviewer should confirm; the locked term คนช่างเก็บเล็กผสมน้อยคนนี้ is unaffected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_17_optimal_001 -->
### Acts 17:5

**Current:**

> หวังจะนำเปาโลกับสิลาสออกมามอบให้ฝูงชน

**Proposed:**

> พยายามจะนำเปาโลกับสิลาสออกมามอบให้ฝูงชน

**Why:** ἐζήτουν is the imperfect of ζητέω (seek, strive, try), signaling sustained, purposive mob-effort — a semantic range that belongs to active volitional striving, not to passive expectation. Thai หวัง (hope, expect) maps onto the ἐλπίζω/ἐλπίς field; in a riot-and-raid context the imperfect ζητέω requires a volitional, action-oriented rendering. พยายามจะ (were attempting to, tried to) matches the Greek's determined-effort nuance and the violent register of the surrounding narrative. None of the five KD entries for this verse address ζητέω → หวัง, confirming the choice is undocumented; the correction involves no theological change and preserves the locked term ให้ฝูงชน verbatim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_18_optimal_003 -->
### Acts 18:14

**Current:**

> กัลลิโอก็พูดกับพวกชาวยิวว่า

**Proposed:**

> กัลลิโอก็กล่าวกับพวกชาวยิวว่า

**Why:** Gallio here delivers an official judicial ruling as Roman proconsul in open court — the highest-formality speech context in the chapter; εἶπεν in this setting warrants 'กล่าว' (formal literary-narrative register) rather than 'พูด' (everyday conversational). The register mismatch is sharpened by contrast with v.21, where the same εἶπεν narrative frame is rendered 'กล่าวว่า,' and by the stiff official content that immediately follows ('ท่านชาวยิวทั้งหลาย … เราก็คงจะอดทนรับฟัง'). No locked term in the narrative frame is affected; all speech-content locked phrases ('ท่านชาวยิวทั้งหลาย,' 'การกระทำที่อยุติธรรมหรือเป็นอาชญากรรมร้ายแรง,' 'เราก็คงจะอดทนรับฟังพวกท่านตามสมเหตุสมผล') remain verbatim; this is a surface register correction with no impact on theological meaning.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_18_optimal_001 -->
### Acts 18:6

**Current:**

> เปาโลสะบัดเสื้อผ้าและพูดกับพวกเขาว่า

**Proposed:**

> เปาโลสะบัดเสื้อผ้าและกล่าวกับพวกเขาว่า

**Why:** Thai 'พูด' is the everyday conversational speech-verb and pulls the register toward the colloquial; 'กล่าว' is the formal literary-narrative register that THSV2011 uses for εἶπεν in solemn narrative contexts. The immediate dramatic context — symbolic garment-shaking followed by a prophetic OT blood-guilt formula — calls squarely for the elevated register marker 'กล่าว.' The register inconsistency is confirmed within the same chapter: the parallel εἶ πεν-introduction formula at v.21 is rendered 'กล่าวว่า,' whereas v.6 breaks that pattern with 'พูด.' The proposed 'กล่าวกับพวกเขาว่า' preserves the locked term 'สะบัดเสื้อผ้า' and leaves all speech-content locked phrases entirely unchanged; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_21_optimal_001 -->
### Acts 21:9

**Current:**

> หญิงพรหมจารีและทุกคนกล่าวพยากรณ์

**Proposed:**

> หญิงพรหมจารี ทุกคนกล่าวพยากรณ์

**Why:** In the Greek, παρθένοι and προφητεύουσαι are parallel predicative attributes of θυγατέρες with no καί between them — the two qualities are asyndetically juxtaposed. The Thai relative clause ที่ยังเป็นหญิงพรหมจารี closes naturally at พรหมจารี, but immediately appending และทุกคนกล่าวพยากรณ์ creates a structural tension: the ที่ has opened a relative clause modifying บุตรสาวสี่คน, so readers must resolve whether ทุกคนกล่าวพยากรณ์ is still inside that relative clause or is a new main clause with ทุกคน as a redundant re-stated subject. Dropping และ and letting ทุกคนกล่าวพยากรณ์ stand as an asyndetic parallel descriptor mirrors the Greek's zero-conjunction structure and follows a common Thai prose pattern for juxtaposed nominal and verbal predicates. Both locked terms (บุตรสาวสี่คนที่ยังเป็นหญิงพรหมจารี and กล่าวพยากรณ์) are preserved verbatim; the KD justifies ทุกคน and กล่าวพยากรณ์ individually but does not address the และ connector, making this a legitimate surface-level proposal with no theological content affected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_25_optimal_001 -->
### Acts 25:21

**Current:**

> ขอให้กักตัวท่านไว้รอการวินิจฉัยขององค์จักรพรรดิ ข้าพเจ้าจึงสั่งให้กักตัวท่านไว้จนกว่าจะส่งท่านไปยังซีซาร์

**Proposed:**

> ขอให้กักตัวเขาไว้รอการวินิจฉัยขององค์จักรพรรดิ ข้าพเจ้าจึงสั่งให้กักตัวเขาไว้จนกว่าจะส่งเขาไปยังซีซาร์

**Why:** ท่าน is a Thai honorific pronoun that carries an implicit elevation of social status for its referent; applying it three times to Paul — a prisoner — in Festus's report to King Agrippa sits one register-step too high for the narrative context. Every other pronoun reference to Paul in Festus's sustained narrative speech (vv. 15–20) uses เขา or a neutral nominal such as ชายผู้นั้น (v.17), and Agrippa himself in v.22 immediately afterwards refers to Paul as ชายผู้นี้, not ท่าน — meaning even the king does not apply an honorific to him. The switch to เขา throughout v.21 restores consistency with the surrounding verses and removes an inadvertent social elevation of a prisoner that no other character in the passage performs; it carries no theological implication. Both locked terms (การวินิจฉัย, องค์จักรพรรดิ) are preserved verbatim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_26_optimal_001 -->
### Acts 26:11

**Current:**

> มักลงโทษพวกเขาบ่อยๆ

**Proposed:**

> ลงโทษพวกเขาบ่อยครั้ง

**Why:** The Greek πολλάκις τιμωρῶν ('often punishing them') is rendered with two frequency markers stacked: มัก (habitual-aspect particle) and บ่อยๆ (informal repetition intensifier). Both convey 'repeatedly/often,' so the pairing is redundant. บ่อยๆ additionally carries a slightly colloquial register via the informal -ๆ reduplication suffix, which sits below the optimal-evangelical-formal register of Paul's high-court oration before King Agrippa. The proposed ลงโทษพวกเขาบ่อยครั้ง ('punished them on many occasions') eliminates the redundancy, substitutes the more formal term บ่อยครั้ง, and preserves the full Greek sense of πολλάκις. None of the four locked phrases for this verse (ด้วยความเดือดดาลอย่างยิ่ง, ถึงเมืองต่างประเทศ, พยายามบีบให้พวกเขาหมิ่นประมาท, ในธรรมศาลาทุกแห่ง) is affected, and no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_26_optimal_002 -->
### Acts 26:4

**Current:**

> ซึ่งเป็นมาแต่แรก

**Proposed:**

> ซึ่งมีมาตั้งแต่ต้น

**Why:** The Greek τὴν ἀπ'ἀρχῆς γενομένην ('that which came about from the beginning') is rendered as ซึ่งเป็นมาแต่แรก. The phrase is comprehensible but mildly wooden: เป็นมา is a strained fit for the aorist participle γενομένην, and แต่แรก without the idiomatic ตั้งแต่- prefix sounds clipped. Thai ซึ่งมีมาตั้งแต่ต้น ('which has existed from the outset') renders the same temporal-origin meaning more idiomatically and flows more naturally into the following locked phrase ท่ามกลางชนชาติของข้าพเจ้า. No KD rationale covers this participial phrase, so it is not corpus-locked. All three locked terms for this verse (ความเป็นอยู่, ตั้งแต่วัยหนุ่ม, ท่ามกลางชนชาติของข้าพเจ้า) are preserved verbatim; no theological change is involved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_03_optimal_001 -->
### Romans 3:2

**Current:**

> มาก ในทุกประการ ประการแรก

**Proposed:**

> มาก ในทุกประการ ประการแรกก็คือ

**Why:** The γάρ in πρῶτον μὲν γάρ functions as an explanatory bridge ('for — the first reason being that...'), connecting the emphatic πολύ-affirmation to the list that follows. Dropping γάρ entirely produces a paratactic Thai text — 'มาก ในทุกประการ ประการแรก...' — that jumps without cohesive glue, landing on the stiff-translationese side of the THSV2011 register target. In natural Thai formal prose, 'ประการแรกก็คือ' is the standard idiomatic frame for introducing a first enumerated reason, absorbing the explanatory γάρ without loading in a heavy 'เพราะ' connector that would over-translate. The change is a single particle addition with no theological implication; neither locked phrase is touched ('มาก ในทุกประการ' and 'พวกเขาได้รับมอบฝากให้ถือพระวจนะของพระเจ้า' both appear verbatim in the proposed text). Routes to a Tier-A Thai reviewer because the naturalness differential between 'ประการแรก' and 'ประการแรกก็คือ' at this register level is a native-ear judgment.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_04_optimal_002 -->
### Romans 4:24

**Current:**

> ผู้ที่จะทรงนับว่าชอบธรรมให้เป็น

**Proposed:**

> ผู้ที่จะทรงนับว่าชอบธรรม

**Why:** 'ทรงนับว่าชอบธรรม' already carries the full sense of λογίζεσθαι in its forensic-declarative register; appending 'ให้เป็น' is semantically redundant ('reckon-as-righteous to-become') and produces a clunky word cluster that reads as translationese-stiff rather than THSV2011-register. The Greek at this point (οἷς μέλλει λογίζεσθαι) does not include an explicit εἰς δικαιοσύνην object, so 'ให้เป็น' over-renders implied content. Removing it aligns the phrasing with the register of the surrounding narrative prose while preserving the locked resurrection-formula that follows and making no theological change; routed to Tier-A Thai reviewer because the original 'ให้เป็น' may reflect a deliberate stylistic choice to echo the εἰς δικαιοσύνην formula of vv. 3/9/22.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_09_optimal_002 -->
### Romans 9:22

**Current:**

> ทรงอดทนด้วยความอดกลั้นพระทัยอันยิ่งใหญ่

**Proposed:**

> ทรงอดทนด้วยความอดกลั้นอันยิ่งใหญ่

**Why:** The compound 'ความอดกลั้นพระทัย' (restraint of the royal heart) is an unusual Thai rendering of μακροθυμία (long-suffering/forbearance); the standard corpus form is 'ความอดกลั้น' or 'ความอดทนนาน' without an explicit 'พระทัย' qualifier, which adds little meaning and produces a slightly stiff noun phrase. Dropping 'พระทัย' yields 'ความอดกลั้นอันยิ่งใหญ่,' preserving the full sense of ἐν πολλῇ μακροθυμίᾳ with no theological change and no locked terms affected. Flagged as fyi because normalising μακροθυμία renderings across the NT corpus is a wider editorial decision best addressed in a dedicated consistency pass rather than a single-verse fix.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_09_optimal_001 -->
### Romans 9:5

**Current:**

> ของพวกเขาเป็นบรรพบุรุษ

**Proposed:**

> บรรพบุรุษเป็นของพวกเขา

**Why:** The Thai 'ของพวกเขาเป็นบรรพบุรุษ' mirrors the Greek genitive ὧν οἱ πατέρες word-for-word, producing an unusual subject–predicate inversion ('their-thing is patriarchs') not idiomatic in Thai possessive expression. Thai naturally places the possessed noun first: 'บรรพบุรุษเป็นของพวกเขา' (the patriarchs are theirs) conveys the same heritage-claim in natural word order with no theological change. No locked terms are affected and the doxology later in the verse is untouched. Deferred because the translator may have intentionally front-loaded 'ของพวกเขา' to sustain the ὧν-catalog rhythm carried from v.4, a judgment requiring a native-ear check.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_10_optimal_002 -->
### Romans 10:4

**Current:**

> สู่ความชอบธรรมแก่ทุกคนที่เชื่อ

**Proposed:**

> เป็นความชอบธรรมสำหรับทุกคนที่เชื่อ

**Why:** The sequence สู่ (rendering εἰς, 'toward/to') immediately followed by แก่ ('for/to [recipient]') produces a two-preposition phrase 'สู่ความชอบธรรมแก่ทุกคนที่เชื่อ' that reads as translationese-stiff. Thai 'เป็นความชอบธรรมสำหรับทุกคนที่เชื่อ' ('constituting/as righteousness for every believer') collapses to a single predicate and renders the resultative force of εἰς δικαιοσύνην more naturally as the apodosis of τέλος γὰρ νόμου Χριστός. The locked phrase 'พระคริสต์ทรงเป็นจุดสิ้นสุดของธรรมบัญญัติ' is entirely untouched; only the trailing εἰς-phrase is modified. This is not a theological proposal and does not re-open the τέλος (end vs. goal) crux documented in KD1. Flagged as fyi rather than defer_to_native because committing to 'เป็น' here should first be checked against how εἰς δικαιοσύνην is rendered in 1:17 and 3:22 to avoid creating a cross-corpus inconsistency.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_12_optimal_001 -->
### Romans 12:17

**Current:**

> จงพิจารณาสิ่งที่ดีต่อหน้ามนุษย์ทุกคน

**Proposed:**

> จงคำนึงถึงสิ่งที่ดีงามต่อหน้ามนุษย์ทุกคน

**Why:** พิจารณา carries a formal-deliberative register in Thai that tilts toward judicial or legislative contexts (พิจารณาคดี, พิจารณาร่างกฎหมาย), making it translationese-stiff for Pauline practical ethics. Greek προνοέω means 'give forethought to / take care to provide' — an active, forward-looking moral intention — and the THSV2011 register calls for a warmer, everyday expression of that intentionality. คำนึงถึง (be mindful of / give thought to) conveys the proactive-care nuance of προνοέω more naturally without the judicial weight. Substituting ดีงาม for ดี also marginally improves the rendering of καλά, which connotes honorable-nobility rather than bare goodness. This is surface-register polish; the doctrinal content — give thought to what is honorable in the sight of all people — is fully preserved, and the locked clause อย่าตอบแทนความชั่วด้วยความชั่วแก่ผู้ใด in the verse's first half is untouched.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_12_optimal_002 -->
### Romans 12:5

**Current:**

> เราที่เป็นจำนวนมาก

**Proposed:**

> เราหลายคน

**Why:** The relative-clause construction เราที่เป็นจำนวนมาก (we who are of large number) reads with a slight census-bureaucratic stiffness in Thai; the simpler เราหลายคน (we, the many) renders οἱ πολλοί more fluently while preserving the deliberate 'many' emphasis Paul intends. This is flagged as fyi rather than a firm recommendation because οἱ πολλοί carries Pauline theological freight across Romans (5:15, 19; 12:5), so any change to its surface rendering should ideally be a corpus-wide normalization decision rather than a single-verse tweak. The locked predicate เป็นร่างกายเดียวในพระคริสต์ และแต่ละคนเป็นอวัยวะของกันและกัน is entirely untouched by this proposal.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_13_optimal_001 -->
### Romans 13:11

**Current:**

> และให้ทำเช่นนี้ — เพราะรู้ถึงเวลานี้ — ว่าถึงเวลาแล้วที่พวกท่านจะตื่นขึ้นจากการหลับ

**Proposed:**

> และให้ทำเช่นนี้ เพราะรู้ถึงเวลานี้ว่าถึงเวลาแล้วที่พวกท่านจะตื่นขึ้นจากการหลับ

**Why:** The double em-dash strands ว่า after a full pause ('— เพราะรู้ถึงเวลานี้ — ว่า…'), severing the Thai complementizer from its governing verb; standard Thai prose requires รู้ว่า to connect without interruption. Collapsing the two em-dashes and placing ว่า immediately after เวลานี้ restores the natural construction while preserving εἰδότες (เพราะรู้ถึงเวลานี้) and the ὅτι-content clause (ว่าถึงเวลาแล้ว…) intact. The locked term ถึงเวลาแล้วที่พวกท่านจะตื่นขึ้นจากการหลับ appears verbatim in the proposed text. This is a punctuation-structure repair only; no vocabulary or theological meaning changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_15_optimal_002 -->
### Romans 15:4

**Current:**

> เพื่อโดยความเพียรและการหนุนใจของพระคัมภีร์ เราจะมีความหวัง

**Proposed:**

> เพื่อเราจะมีความหวัง โดยอาศัยความเพียรและการหนุนใจของพระคัมภีร์

**Why:** The current rendering stacks the purpose marker เพื่อ directly before the instrumental marker โดย at the head of the clause, mechanically following the Greek ἵνα...διά sequence. In natural Thai prose the main verb of the purpose clause comes first and the instrumental phrase trails after it; opening a clause with 'เพื่อโดย' is translationese-stiff. Reordering to 'เพื่อเราจะมีความหวัง โดยอาศัย…' untangles the two connectives without dropping either logical relation and without altering the theology (Scripture's endurance and encouragement sustain hope). The locked phrase 'สิ่งทั้งหลายที่ได้เขียนไว้ก่อน ก็เขียนไว้เพื่อสอนเรา' is untouched. Marked defer_to_native because the exact weight and register of อาศัย in evangelical-formal Thai, and the preferred clause-order rhythm, benefit from a Tier-A native reader's judgment.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_16_optimal_001 -->
### Romans 16:1

**Current:**

> ผู้เป็นผู้รับใช้ของคริสตจักรที่เมืองเคนเครีย

**Proposed:**

> ผู้รับใช้ของคริสตจักรที่เมืองเคนเครีย

**Why:** The Greek participial οὖσαν (being/who is) coupled with διάκονον produces the Thai double-marker construction ผู้เป็นผู้รับใช้, stacking two relative/nominal markers in sequence. In Thai, the ผู้ prefix of ผู้รับใช้ already functions as a relative clause head, making ผู้เป็น superfluous and registering as translationese-stiff; compare all other appositive noun phrases in this chapter (เพื่อนร่วมงาน, เหรัญญิก, ผู้ต้อนรับ) which carry no intervening เป็น. Dropping ผู้เป็น yields a clean appositive structure natural to modern Thai and fully consistent with the THSV2011 register. The locked term ผู้รับใช้ของคริสตจักร is preserved verbatim; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_16_optimal_002 -->
### Romans 16:7

**Current:**

> เพื่อนร่วมเป็นเชลยของข้าพเจ้า

**Proposed:**

> เพื่อนร่วมเชลยของข้าพเจ้า

**Why:** The Greek compound συναιχμάλωτος (fellow-captive) is rendered เพื่อนร่วมเป็นเชลย, inserting the copula เป็น between ร่วม and เชลย in a pattern that does not match standard Thai compound formation. Thai builds 'fellow + noun' compounds directly — เพื่อนร่วมงาน, เพื่อนร่วมห้อง, เพื่อนร่วมชั้น — without an intervening copula; the เป็น here is a Greek-calque particle that reads as mildly awkward. เชลย stands alone as a well-established Thai noun (captive/prisoner), so เพื่อนร่วมเชลย is both more compact and more idiomatic. The captivity sense of αἰχμάλωτος is fully preserved; this is a surface-level polish with no theological implication. Neither of the locked terms for this verse is affected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_04_optimal_001 -->
### 1 Corinthians 4:17

**Current:**

> เขาจะระลึกพวกท่านถึงทางของข้าพเจ้าในพระเยซูคริสต์

**Proposed:**

> เขาจะเตือนความจำพวกท่านถึงทางของข้าพเจ้าในพระเยซูคริสต์

**Why:** In modern standard Thai, ระลึก is an intransitive verb meaning 'to recall/remember' and cannot take a person as its direct object; the construction ระลึกพวกท่านถึง is syntactically un-Thai and produces translationese-stiff output that a Thai reader must re-parse before comprehending. The causative verb เตือนความจำ ('to remind'), which naturally governs a person object followed by ถึง + content-recalled, is the THSV-register equivalent of ἀναμιμνήσκω in its causative meaning 'cause to remember, bring to mind.' No key-decision rationale documents the ระลึก choice for this verb (KD2 justifies only the rendering of ὁδοί → ทางของข้าพเจ้า; KD3 covers the doublet πανταχοῦ/ἐν πάσῃ ἐκκλησίᾳ). The locked term ทางของข้าพเจ้าในพระเยซูคริสต์ is preserved verbatim, and no theological content is affected — the change is a pure verb-selection correction restoring grammatical naturalness to the Greek's causative force.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_07_optimal_001 -->
### 1 Corinthians 7:6

**Current:**

> ที่ข้าพเจ้ากล่าวเช่นนี้ก็โดยเป็นการอนุญาต ไม่ใช่เป็นคำสั่ง

**Proposed:**

> ที่ข้าพเจ้ากล่าวเช่นนี้ก็เป็นการอนุญาต ไม่ใช่เป็นคำสั่ง

**Why:** The Greek prepositional phrase κατὰ συγγνώμην is rendered with Thai 'โดยเป็นการอนุญาต,' inserting 'โดย' as a preposition-proxy for κατά. In Thai the predicate 'เป็นการอนุญาต' already carries the relational/identificatory sense inherently; the 'โดย' is syntactically redundant and shifts the register toward translationese-stiff ('by-means-of-being-permission' rather than the simpler copulative 'is permission'). Dropping 'โดย' yields 'ก็เป็นการอนุญาต ไม่ใช่เป็นคำสั่ง,' which sits at natural THSV2011 register for concessive clarifications. The locked phrase 'เป็นการอนุญาต ไม่ใช่เป็นคำสั่ง' is preserved verbatim, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_08_optimal_001 -->
### 1 Corinthians 8:7

**Current:**

> ในฐานะที่เป็นของถวายแก่รูปเคารพ

**Proposed:**

> โดยถือว่าเป็นของถวายแก่รูปเคารพ

**Why:** Thai 'ในฐานะที่เป็น' ('in the capacity/status of being') carries a legalistic-formal register typical of contracts and official documents, pulling the verse above the accessible evangelical register the corpus targets. The Greek ὡς εἰδωλόθυτον is a plain comparator — 'eating it as [i.e., treating it as] idol-sacrificed food' — not a formal designation of legal status. 'โดยถือว่าเป็น' ('by regarding/treating it as') conveys the identical semantic content — the weak believer psychologically perceives and treats the food as ceremonially idol-associated — while sitting comfortably in natural modern Thai at the THSV2011 register. All three locked terms for this verse (ความคุ้นเคยกับรูปเคารพมาจนถึงปัจจุบัน; มโนธรรมของพวกเขาที่อ่อนแอก็เป็นมลทินไป; ไม่ใช่ทุกคนที่มีความรู้นี้) are entirely unaffected. No theological meaning is altered — the concern remains the weak believer's habituated perception of the food's sacrificial significance, not any change in what that significance is.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_12_optimal_001 -->
### 1 Corinthians 12:15

**Current:**

> ก็มิได้ทำให้เท้านั้นไม่เป็นส่วนของร่างกายเลย

**Proposed:**

> เท้านั้นก็ยังคงเป็นส่วนของร่างกายอยู่นั่นเอง

**Why:** The current Thai contains a pragmatically heavy double negative (มิได้ … ไม่เป็น) that requires the reader to parse 'did not make it not be a part,' which reads as translationese-stiff rather than natural evangelical prose; the Greek's own double-negative rhetorical question is a Greek-rhetoric device that does not translate naturally into statement-form Thai with the same doubly-negated structure. The proposed 'เท้านั้นก็ยังคงเป็นส่วนของร่างกายอยู่นั่นเอง' ('the foot still remains part of the body all the same') conveys the identical affirmation — the foot is and remains a body-member despite its self-deprecating claim — without parsing overhead, and sits squarely in the THSV-evangelical register. No locked key_decisions terms fall within the proposed span; the foot-quote inside the quotation marks is entirely outside the current_text substring and is preserved verbatim. No theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_12_optimal_002 -->
### 1 Corinthians 12:16

**Current:**

> ก็มิได้ทำให้หูนั้นไม่เป็นส่วนของร่างกายเลย

**Proposed:**

> หูนั้นก็ยังคงเป็นส่วนของร่างกายอยู่นั่นเอง

**Why:** Exact parallel to v.15: the identical double-negative conclusion formula (ก็มิได้ทำให้ … ไม่เป็นส่วนของร่างกายเลย) recurs for the ear/eye pair and carries the same translationese-stiff awkwardness; because the Greek formula is word-for-word repeated, the same surface rigidity migrated into both verses identically. The proposed 'หูนั้นก็ยังคงเป็นส่วนของร่างกายอยู่นั่นเอง' mirrors the v.15 fix and maintains exact verbal parallelism across the two personification scenarios, affirming the ear's body-membership in natural Thai without a double negative. The locked KD term 'ถ้าหูจะพูดว่า "เพราะข้าพเจ้าไม่ใช่ตา"' is outside the proposed span and remains verbatim. Should the native reviewer approve the v.15 change, this verse should be updated in the same pass to preserve internal parallelism.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_14_optimal_001 -->
### 1 Corinthians 14:35

**Current:**

> เพราะเป็นการน่าอับอายสำหรับผู้หญิงที่จะพูดในคริสตจักร

**Proposed:**

> เพราะเป็นเรื่องน่าอับอายสำหรับผู้หญิงที่จะพูดในคริสตจักร

**Why:** In Thai grammar, 'เป็นการ' is a pre-verbal particle that nominali­ses action-verb phrases (เป็นการกระทำ, เป็นการฝ่าฝืน, เป็นการละเมิด); it does not precede predicate adjectives. 'น่าอับอาย' is a predicate adjective, so the standard THSV2011-register construction for the Greek predicate αἰσχρόν ἐστιν ('it is shameful') is 'เป็นเรื่องน่าอับอาย' (it is a shameful matter) or 'เป็นสิ่งน่าอับอาย', not 'เป็นการน่าอับอาย'. The KD for this verse addresses only the interpretive crux of ἄνδρας/husbands and does not document the 'เป็นการ' choice, so no translator rationale locks it. The single-word substitution เรื่อง for การ is a pure surface-grammatical correction: the lexical rendering น่าอับอาย for αἰσχρός is kept intact, no theological sense is altered, and the locked phrase in the first half of the verse is entirely outside the edited span and is unaffected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_14_optimal_002 -->
### 1 Corinthians 14:9

**Current:**

> ถ้าพวกท่านไม่ได้พูดถ้อยคำที่เข้าใจได้ผ่านปาก

**Proposed:**

> ถ้าพวกท่านไม่ได้พูดถ้อยคำที่เข้าใจได้

**Why:** 'ผ่านปาก' (through the mouth) was appended beyond the locked phrase to render the instrumental διὰ τῆς γλώσσης (through the tongue), evidently to avoid confusing γλῶσσα-the-organ with γλῶσσα-the-gift that dominates the chapter. However, 'พูดถ้อยคำ...ผ่านปาก' is tautological in Thai—speech already entails use of the mouth, so specifying the organ reads as translationese-stiff. The KD discusses εὔσημον and ἀέρα for this verse but is silent on 'ผ่านปาก', leaving the addition undocumented. Dropping it yields the fully natural Thai 'ถ้าพวกท่านไม่ได้พูดถ้อยคำที่เข้าใจได้', preserves the locked substring verbatim, and loses no semantic content since the instrument is implicit in 'พูด'. Marked fyi rather than apply because the translator may have added 'ผ่านปาก' as a deliberate intra-chapter glossolalia-disambiguation strategy that warrants a corpus-wide review of how διὰ τῆς γλώσσης is handled elsewhere before any removal is authorised.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_15_optimal_003 -->
### 1 Corinthians 15:19

**Current:**

> ถ้าความหวังของเราในพระคริสต์มีไว้เพียงสำหรับชีวิตนี้เท่านั้น

**Proposed:**

> ถ้าเราหวังในพระคริสต์เพียงสำหรับชีวิตนี้เท่านั้น

**Why:** The Greek ἠλπικότες ἐσμέν is a periphrastic perfect-participial construction that is verbal and personal in force — 'we are [people who have] hoped.' The Thai nominalizes this as 'ความหวัง...มีไว้' ('hope…is kept/held'), a noun-heavy construction that mutes the active personal-commitment sense Paul intends. 'ถ้าเราหวังในพระคริสต์เพียงสำหรับชีวิตนี้เท่านั้น' shifts to the natural Thai verbal form used in conditional clauses of this type. The locked apodosis 'เราก็เป็นคนที่น่าสมเพชยิ่งกว่ามนุษย์ทุกคน' is preserved verbatim in the verse and is not touched by this replacement. No theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_15_optimal_002 -->
### 1 Corinthians 15:6

**Current:**

> ซึ่งส่วนใหญ่ของพวกเขายังมีชีวิตอยู่จนถึงปัจจุบัน

**Proposed:**

> โดยส่วนใหญ่ยังมีชีวิตอยู่จนถึงปัจจุบัน

**Why:** ἐξ ὧν ('of whom,' partitive) is rendered as ซึ่ง (relative pronoun, already encoding the antecedent) plus ของพวกเขา (of them), creating a doubled back-reference that is a signature feature of translationese-stiff register. Natural Thai handles the partitive-circumstantial relation with a participial or adverbial clause opener such as โดย, which drops the redundant pronoun while preserving the meaning that the majority of the 500 witnesses were still alive at the time of writing. The locked term 'พี่น้องกว่าห้าร้อยคนในคราวเดียว' is entirely untouched; only the subsequent relative clause is smoothed. No theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_16_optimal_002 -->
### 1 Corinthians 16:18

**Current:**

> ได้ทำให้จิตใจของข้าพเจ้าและจิตใจของพวกท่านได้รับการพักพิง

**Proposed:**

> ได้ทำให้จิตใจของข้าพเจ้าและของพวกท่านสดชื่นขึ้น

**Why:** The Greek ἀνέπαυσαν is an aorist active verb meaning 'they refreshed / gave rest to,' yet the Thai renders it with the heavy nominalized-passive construction 'ได้รับการพักพิง' (received sheltering), which is translationese-stiff and also imports the shelter/dependency nuance of 'พักพิง' rather than the active spirit-refreshment of ἀναπαύω (cf. Phlm 1:7, 20 for the same word in relational contexts). The redundant second 'จิตใจ' further weighs the phrase down. Replacing with 'สดชื่นขึ้น' (became refreshed/revived) restores the active sense and lands at natural THSV2011 register; routed defer_to_native because the choice among 'สดชื่น,' 'ได้พักผ่อน,' or another near-equivalent turns on a native-speaker register call. The locked phrase 'จงรู้คุณคนเช่นนั้น' lies outside the changed span and is preserved unchanged; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_16_optimal_001 -->
### 1 Corinthians 16:2

**Current:**

> ตั้งไว้ที่ตนเอง สะสมไว้

**Proposed:**

> แยกเก็บสะสมไว้เอง

**Why:** The phrase 'ตั้งไว้ที่ตนเอง' is a wooden calque of παρ᾽ ἑαυτῷ—Thai speakers do not say 'วางไว้ที่ตนเอง' for the idea of setting something aside privately at home; the natural register is 'เก็บไว้เอง' or 'แยกเก็บไว้.' The immediately following 'สะสมไว้' (θησαυρίζω) then creates a clumsy doublet alongside 'ตั้งไว้,' stacking two near-synonymous verbs in translationese sequence. Collapsing both into 'แยกเก็บสะสมไว้เอง' renders the private setting-aside (παρ᾽ ἑαυτῷ) and the accumulation (θησαυρίζω) in a single, idiomatic Thai phrase that sits at natural THSV2011 register. The locked phrase 'ตามที่ตนเจริญรุ่งเรือง' follows immediately after the changed span and is untouched; no theological meaning is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_01_optimal_001 -->
### 2 Corinthians 1:12

**Current:**

> สิ่งที่เราภาคภูมิใจคือสิ่งนี้ คือคำพยานของมโนธรรมของเรา

**Proposed:**

> สิ่งที่เราภาคภูมิใจคือสิ่งนี้ ได้แก่คำพยานของมโนธรรมของเรา

**Why:** The Greek places the predicate-nominative αὕτη ἐστίν and then a bare appositive noun phrase (τὸ μαρτύριον τῆς συνειδήσεως ἡμῶν) with no additional connector. The Thai renders this as two consecutive 'คือ' markers — 'คือสิ่งนี้ คือคำพยาน...' — which is grammatically valid but drifts toward translationese-stiff: a native Thai writer specifying what 'สิ่งนี้' refers to would normally reach for 'ได้แก่' (the standard modern-Thai discourse marker for clarifying apposition, equivalent to 'namely / that is') rather than repeating 'คือ'. The THSV2011 register favours 'ได้แก่' in exactly this appositive role. Replacing only the second 'คือ' with 'ได้แก่' eliminates the back-to-back repetition while preserving both locked terms ('สิ่งที่เราภาคภูมิใจ' and 'คำพยานของมโนธรรมของเรา') verbatim and making no change to theological content.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_08_optimal_001 -->
### 2 Corinthians 8:11

**Current:**

> จะเข้ากับการทำให้สำเร็จตามกำลังที่ท่านมี

**Proposed:**

> จะสอดคล้องกับการทำให้สำเร็จตามกำลังที่ท่านมี

**Why:** เข้ากับ (= 'go with / suit / match in style') is most at home in everyday Thai contexts such as matching colours or flavours, giving it a colloquial register that sits below the optimal-evangelical-formal target. The Greek καθάπερ...οὕτως is a formal proportionality marker ('just as…so also'), expressing purposive correspondence between willing and completing; THSV2011-register Thai normally reaches for สอดคล้องกับ (= 'be in accord with / be consistent with') to carry that formal theological correspondence. All locked terms — ความตั้งใจที่จะกระทำ and การทำให้สำเร็จตามกำลังที่ท่านมี — are preserved verbatim, and no theological content is altered. This is surfaced as a possible corpus-wide normalization candidate rather than a single-verse change; a Tier-A native reviewer should confirm whether เข้ากับ appears in parallel constructions elsewhere before acting.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_09_optimal_001 -->
### 2 Corinthians 9:12

**Current:**

> จากคนเป็นจำนวนมาก

**Proposed:**

> จากผู้คนมากมาย

**Why:** วลี 'คนเป็นจำนวนมาก' แทรกกริยาสภาวะ 'เป็น' ระหว่างคำนาม 'คน' กับวลีปริมาณ 'จำนวนมาก' ทำให้โครงสร้างอ่านเสมือนแปลกลับจาก 'people being in large numbers' ซึ่งไม่เป็นธรรมชาติในภาษาไทยเขียน ระดับ THSV2011; ภาษาไทยทั่วไปใช้ 'ผู้คนมากมาย' หรือ 'คนมากมาย' โดยไม่ต้องมีกริยาคั่น; ข้อเสนอ 'จากผู้คนมากมาย' ถ่ายทอด πολλῶν (many) ครบถ้วน และไม่กระทบคำล็อกใดในบทนี้ ('การรับใช้ในพันธกิจนี้' และ 'เพิ่มเติมให้เต็มในความขัดสนของธรรมิกชน'); เป็นการปรับระดับภาษาเพื่อความเป็นธรรมชาติเท่านั้น ไม่มีผลต่อความหมายเชิงเทววิทยา.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_10_optimal_001 -->
### 2 Corinthians 10:7

**Current:**

> ระลึกในตัวเองอีกครั้งหนึ่ง

**Proposed:**

> คิดทบทวนในใจอีกครั้ง

**Why:** λογίζομαι (imperative λογιζέσθω) carries a deliberative-reckoning sense — 'consider / think through / reckon' — not the recall-oriented sense that is primary for ระลึก ('remember / recollect'); the current rendering is translationese-stiff, mapping each Greek element woodenly (ἐφ' ἑαυτοῦ → ในตัวเอง, πάλιน → อีกครั้งหนึ่ง) rather than producing natural Thai. The same imperative λογιζέσθω recurs in v.11, where the translation more naturally uses คิดดู, creating an intra-chapter inconsistency a Thai reader would notice. คิดทบทวนในใจอีกครั้ง ('think it over within himself once more') captures the deliberative-reconsideration force, matches the THSV2011 register, and leaves both locked phrases (พวกท่านมองสิ่งที่ปรากฏภายนอก; ถ้าผู้ใดมั่นใจในตัวเองว่าเป็นของพระคริสต์) completely untouched; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_11_optimal_002 -->
### 2 Corinthians 11:6

**Current:**

> เราได้สำแดงสิ่งนี้แก่พวกท่านอย่างชัดเจนในทุกเรื่องและในทุกประการ

**Proposed:**

> ข้าพเจ้าได้สำแดงสิ่งนี้แก่พวกท่านอย่างชัดเจนในทุกประการ

**Why:** The verse sustains first-person singular ข้าพเจ้า across both KD-locked clauses, then shifts abruptly to เรา in the concluding φανερώσαντες clause; no KD entry documents an intentional epistolary-plural shift here, and the abrupt change risks reading as a subject change for a Thai audience. The φανερώσαντες clause is part of Paul's personal self-defense argument, so ข้าพเจ้า maintains consistency. Additionally, 'ในทุกเรื่องและในทุกประการ' renders two cognate Greek phrases (ἐν παντὶ … ἐν πᾶσιν) in a Thai near-tautology; collapsing to ในทุกประการ preserves the rhetorical emphasis without the pile-up. Flagged fyi only: if the translator deliberately chose เรา as an authorial plural the KD should document it and no change is warranted.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_13_optimal_001 -->
### 2 Corinthians 13:4

**Current:**

> ในการมีต่อพวกท่าน

**Proposed:**

> ต่อพวกท่าน

**Why:** The phrase 'ในการมีต่อพวกท่าน' (literally 'in the having toward you') is a wooden nominalisation of the bare directional εἰς ὑμᾶς; no KD documents a deliberate choice for this second clause — the only locked element in v.4 covers the first Christ-clause. In natural Thai the directional εἰς ὑμᾶς appended to an active clause is simply 'ต่อพวกท่าน' (toward you), which sits cleanly at sentence-end without the artificial 'ในการมี-' wrapper. The proposed trim does not alter Paul's meaning — that his apostolic life exercised in resurrection-power is directed toward the Corinthians — nor does it touch any locked term.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_13_optimal_002 -->
### 2 Corinthians 13:5

**Current:**

> หรือพวกท่านไม่เข้าใจตัวเองหรือว่า

**Proposed:**

> หรือพวกท่านไม่ตระหนักหรือว่า

**Why:** ἐπιγινώσκω denotes perceptual recognition or discernment rather than cognitive understanding (เข้าใจ); Paul's rhetorical thrust is that the Corinthians should have already perceived — as a present, lived reality — that Christ indwells them. 'ตระหนัก' (to be aware of / to register a reality) maps more precisely onto that perceptual-recognition force than 'เข้าใจ.' Additionally, the current 'ไม่เข้าใจตัวเองหรือว่า' risks a dual parse where 'ตัวเอง' reads as object of 'เข้าใจ' ('don't understand themselves') before the reader reaches 'หรือว่า,' creating momentary ambiguity; dropping 'ตัวเอง' and using 'ตระหนักหรือว่า' resolves the parse cleanly. No locked KD term is affected; this is a surface-register adjustment only. Routing to native reviewer because the choice between 'เข้าใจ' and 'ตระหนัก' in formal-evangelical register may carry connotations that require a native Thai ear to confirm.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=ephesians_04_optimal_001 -->
### Ephesians 4:23

**Current:**

> จิตวิญญาณแห่งจิตใจของพวกท่าน

**Proposed:**

> วิญญาณแห่งจิตใจของพวกท่าน

**Why:** The current Thai compound 'จิตวิญญาณแห่งจิตใจ' places two lexemes that share the 'จิต' root immediately adjacent — 'จิตวิญญาณ' (spirit/soul) and 'จิตใจ' (mind/heart) — creating an unintentional near-redundancy that sounds translationese-stiff to Thai ears rather than natural evangelical-formal. Replacing 'จิตวิญญาณ' with the simpler 'วิญญาณ' (spirit) recovers the Greek πνεῦμα/νοῦς distinction cleanly: 'วิญญาณ' maps unambiguously to πνεῦμα while 'จิตใจ' retains νοῦς, eliminating the จิต-จิต collision without any theological change. However, if the translation corpus has locked 'จิตวิญญาณ' as its standard rendering for human-spirit πνεῦμα (distinct from 'พระวิญญาณ' for the Holy Spirit), a single-verse substitution would break corpus consistency and the fix would require a corpus-wide normalization pass — hence fyi rather than apply. The KD rationale for this verse addresses only ἀνανεοῦσθαι (the HAPAX renewal verb) and does not document the specific Thai choice for τῷ πνεύματι τοῦ νοὸς, leaving this sub-phrase unprotected by a corpus-lock rationale. The locked terms 'ให้ทรงฟื้นฟู' and 'ขึ้นใหม่' are preserved verbatim in the proposed rendering.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=ephesians_05_optimal_001 -->
### Ephesians 5:15

**Current:**

> จงระวังอย่างถี่ถ้วนถึงวิธีที่พวกท่านดำเนินชีวิต

**Proposed:**

> จงระวังอย่างถี่ถ้วนว่าพวกท่านดำเนินชีวิตอย่างไร

**Why:** The current 'ถึงวิธีที่พวกท่านดำเนินชีวิต' is a calque of the Greek πῶς-clause that nominalized the indirect question into a prepositional phrase ('about the way/manner that you live') — a translationese-stiff construction. Thai idiom embeds indirect manner-questions with 'ว่า…อย่างไร' (that…how), not 'ถึงวิธีที่…' (about the way that…), which is the pattern a THSV2011-register writer would naturally reach for. The locked term 'อย่างถี่ถ้วน' is preserved verbatim, and the surrounding locked antithesis 'คนเขลา … คนมีปัญญา' is unaffected. No theological content shifts — the call to careful discernment in the conduct of life remains fully intact.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=ephesians_06_optimal_002 -->
### Ephesians 6:18

**Current:**

> จงอธิษฐานในทุกเวลาในพระวิญญาณ

**Proposed:**

> จงอธิษฐานในพระวิญญาณทุกเวลา

**Why:** The Greek adverbial sequence ἐν παντὶ καιρῷ ἐν πνεύματι ('in every time, in the Spirit') is preserved in Greek word-order as 'ในทุกเวลาในพระวิญญาณ,' producing two back-to-back 'ใน-' prepositional phrases that feel translationese-stiff; Thai naturally prefers the theologically weightier element closer to its governing verb. No KD documents this adverbial ordering as a deliberate choice. Reordering to 'จงอธิษฐานในพระวิญญาณทุกเวลา' resolves the awkward double-'ใน' adjacency, follows Thai informational-focus patterns, and preserves the corpus-locked term 'ในพระวิญญาณ' verbatim; 'ทุกเวลา' is the natural Thai compression of 'ในทุกเวลา' (ἐν παντὶ καιρῷ = at all times). A Tier-A native reviewer should confirm the reordering does not inadvertently shift emphasis away from the temporal or pneumatological claim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=philippians_01_optimal_002 -->
### Philippians 1:1

**Current:**

> บรรดาผู้ปกครองดูแลและบรรดาผู้รับใช้

**Proposed:**

> บรรดาผู้ปกครองดูแลและผู้รับใช้

**Why:** The SBLGNT text is σύν ἐπισκόποις καὶ διακόνοις — a single preposition governing both offices with no repeated article-equivalent; the double 'บรรดา' therefore has no direct Greek basis. In natural Thai, 'บรรดา X และ Y' (one บรรดา scoping both noun groups joined by 'และ') is the idiomatic pattern; repeating 'บรรดา' before each member of the pair is translationese-stiff. Both corpus-locked terms — ผู้ปกครองดูแล and ผู้รับใช้ — appear verbatim in the proposed text. Flagged fyi rather than apply because the doubling may have been intentional to underscore two distinct offices, a choice that warrants a corpus-wide review of how บรรดา is applied to paired office-nouns throughout Acts and the Pastorals before normalising here.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=philippians_01_optimal_001 -->
### Philippians 1:20

**Current:**

> เช่นเดียวกับที่เป็นเสมอมา ทั้งบัดนี้ก็เช่นเดียวกัน

**Proposed:**

> เช่นเดียวกับที่เป็นเสมอมา ทั้งบัดนี้ด้วย

**Why:** ὡς πάντοτε καὶ νῦν ('as always and now') is rendered faithfully in content, but the Thai mirrors the ὡς-particle twice by repeating the เช่นเดียวกัน root in close succession ('เช่นเดียวกับที่เป็นเสมอมา … เช่นเดียวกัน'), producing a stilted same-root echo that has no structural parallel in the Greek. Replacing the trailing 'เช่นเดียวกัน' with 'ด้วย' (also/as well) conveys καὶ νῦν without the redundant echo and sits naturally at the THSV2011 evangelical-formal register. All four locked terms for v.20 (ความกล้าหาญ, ความเฝ้ารออย่างใจจดใจจ่อและความหวัง, พระคริสต์จะทรงได้รับการเทิดทูน, ในร่างกายของข้าพเจ้า) fall outside this substring and are untouched. No theological change — the affirmation that Christ will be magnified as always and also now is fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=philippians_01_optimal_003 -->
### Philippians 1:26

**Current:**

> ความภูมิใจของพวกท่านในพระเยซูคริสต์เกี่ยวกับข้าพเจ้าจะทวียิ่งขึ้น

**Proposed:**

> ความภูมิใจของพวกท่านในพระเยซูคริสต์จะทวียิ่งขึ้น เนื่องด้วยข้าพเจ้า

**Why:** The Greek stacks two ἐν-phrases on the same noun (ἐν Χριστῷ Ἰησοῦ and ἐν ἐμοί), and the Thai carries both as pre-verbal modifiers, producing a three-layer noun cluster (ของพวกท่าน + ในพระเยซูคริสต์ + เกี่ยวกับข้าพเจ้า) that is translationese-dense by Thai standards. Moving ἐν ἐμοί to a trailing explanatory clause ('เนื่องด้วยข้าพเจ้า') follows Thai's preference for a lighter noun phrase succeeded by its modifier, making the subject and main verb immediately accessible to the reader. The locked term ความภูมิใจ is preserved verbatim; การกลับไป appears in the preceding clause and is untouched. Flagged fyi because the restructuring is syntactic and warrants checking for consistency with how doubly-modified καύχημα constructions are rendered elsewhere in the corpus (e.g., Rom 5:2, 2 Co 10:17) before applying here.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=philippians_03_optimal_001 -->
### Philippians 3:6

**Current:**

> ตามความกระตือรือร้น

**Proposed:**

> ตามความร้อนรน

**Why:** ζῆλος in this credential-list context denotes Paul's pre-conversion religious-political fervor — a fanaticism intense enough to drive active persecution of the church. 'ความกระตือรือร้น' (general enthusiasm/diligence) is a register-neutral word applicable to any domain (work, studies, hobbies) and understates the specifically religious intensity of ζῆλος, gently shifting the verse toward the secular-neutral end of the evangelical-formal register. 'ความร้อนรน' is the established Thai Christian corpus term for ζῆλος and ζηλωτής (cf. standard Thai renderings of Acts 21:20, Rom 10:2) and carries the expected religious-fervor charge without altering the meaning: Paul still presents zealous-religiosity as a pre-conversion credential. No KD documents a rationale for preferring 'ความกระตือรือร้น' over 'ความร้อนรน' here; no locked terms are touched; no theological change results.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=colossians_03_optimal_001 -->
### Colossians 3:7

**Current:**

> ในยามที่พวกท่านยังใช้ชีวิตอยู่ในสิ่งเหล่านี้

**Proposed:**

> ในยามที่พวกท่านยังอยู่ในสิ่งเหล่านั้น

**Why:** The subordinate clause renders ζάω (ἐζῆτε ἐν τούτοις) as ใช้ชีวิตอยู่ — a distinctly modern-colloquial Thai phrase common in everyday spoken Thai — while the same verse's main clause renders περιπατέω as ดำเนินชีวิต, the formal-biblical register term corpus-locked throughout the Pauline corpus; the intra-verse collision of colloquial and formal registers for two adjacent 'life' concepts reads as translationese inconsistency against the THSV2011 target register. This ἐζῆτε rendering is undocumented in the KD, which covers only περιπατήσατέ and ποτε. Proposed ยังอยู่ (to be in / dwell among) naturally covers ζάω ἐν in context, matches the formal register of the surrounding verse, and removes the doubled ชีวิต vocabulary within the single sentence; adjusting เหล่านี้ → เหล่านั้น also aligns the anaphoric pronoun with the verse-opening ในวิถีเหล่านั้น, which already treats the pre-conversion vices as temporally and referentially distal. The locked term เคยดำเนินชีวิต is preserved verbatim, and no theological content is altered: the sense 'when you were still living in those things' is fully retained.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1timothy_01_optimal_001 -->
### 1 Timothy 1:3

**Current:**

> ให้พักอยู่ที่เมืองเอเฟซัส

**Proposed:**

> ให้คงอยู่ที่เมืองเอเฟซัส

**Why:** In contemporary Thai, "พักอยู่" typically connotes temporary lodging or stopping to rest (e.g., พักอยู่ที่โรงแรม), which undersells the force of Paul's apostolic instruction for Timothy to remain at his active ministry post. The Greek προσμένω (remain on, continue staying, abide further) denotes sustained, purposeful presence rather than a temporary pause. "คงอยู่" (remain, abide, stay on) is the standard formal-register Thai equivalent for this continuative sense and fits the optimal-evangelical-formal target register better. No locked terms are touched; the KD rationale for v.3 addresses only the two charge-verbs (ได้กำชับ / กำชับ) and ἑτεροδιδασκαλεῖν, leaving προσμένω unaddressed and therefore open to polish.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1timothy_01_optimal_002 -->
### 1 Timothy 1:4

**Current:**

> ซึ่งสิ่งเหล่านี้ส่งเสริมการถกเถียงค้นหา

**Proposed:**

> สิ่งเหล่านี้ก่อให้เกิดการถกเถียงค้นหา

**Why:** Two overlapping register issues appear in this substring. First, "ซึ่งสิ่งเหล่านี้" is a relative-pronoun-plus-resumptive-pronoun construction (ซึ่ง + สิ่งเหล่านี้) — a hallmark of Thai translationese; natural Thai prose either starts a new clause with the noun directly or uses a clause-initial connector, not both. Second, "ส่งเสริม" (promote, actively support, encourage growth) carries a positive/helpful connotation that is ironic and slightly misleading in context: the Greek παρέχουσι (provide, produce, give rise to) is neutral-to-negative — the myths and genealogies generate/produce speculative debates as a byproduct, they do not helpfully champion them. Replacing with "ก่อให้เกิด" (give rise to, generate) removes both the translationese ซึ่ง and the positive-connotation drift, and is fully natural in formal Thai prose. All three locked terms (การถกเถียงค้นหา, ตำนานและลำดับวงศ์ตระกูลที่ไม่จบสิ้น, ภารกิจของพระเจ้าซึ่งดำเนินไปโดยความเชื่อ) are preserved verbatim; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_01_optimal_002 -->
### Hebrews 1:14

**Current:**

> ไม่ใช่หรือ

**Proposed:**

> มิใช่หรือ

**Why:** The Greek rhetorical particle οὐχί expects a formal negative question in the register target (THSV2011-level: respectful, modern, accessible). ไม่ใช่หรือ is serviceable but sits at the everyday-speech end of the Thai register dial; in formal biblical and liturgical prose, มิใช่ (literary negative) is the conventional marker for rhetorical questions addressed to readers. This is a one-word substitution that neither alters meaning nor touches any locked terms, but whether มิใช่ is clearly more natural than ไม่ใช่ in a modern evangelical readership context requires a native Tier-A reviewer's ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_04_optimal_002 -->
### Hebrews 4:1

**Current:**

> จงเกรงเถิด

**Proposed:**

> ขอให้เราเกรง

**Why:** Φοβηθῶμεν is a hortatory subjunctive first-person plural ('let us fear'), the same grammatical form as σπουδάσωμεν (v.11 → 'ขอให้เราพยายามอย่างยิ่ง'), κρατῶμεν (v.14 → 'ขอให้เรายึดมั่น'), and προσερχώμεθα (v.16 → 'ขอให้เราเข้ามา'). Rendering only v.1's hortatory subjunctive as 'จงเกรงเถิด' — an archaic-formal second-person imperative pattern characteristic of older Thai translation registers (TKV-era) rather than THSV2011 — while every other hortatory subjunctive in the chapter uses 'ขอให้เรา…' creates an intra-chapter register inconsistency. The proposed 'ขอให้เราเกรง' aligns with modern evangelical-formal Thai, restores the inclusive pastoral first-person plural the Greek author intends (he includes himself in the warning), and preserves the natural rhetorical echo 'เกรง…เกรงว่า' within the verse. The locked phrase 'ขณะที่พระสัญญาแห่งการเข้าสู่การพักสงบของพระเจ้ายังคงอยู่' is entirely unaffected, and the change carries no theological consequence.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1john_04_optimal_001 -->
### 1 John 4:10

**Current:**

> ความรักนั้นอยู่ในสิ่งนี้

**Proposed:**

> ความรักนั้นอยู่ที่สิ่งนี้

**Why:** The Greek ἐν τούτῳ ἐστίν expresses abstract 'consists in / lies in' containment rather than spatial presence. Thai natively uses อยู่ที่ for this abstract sense — compare standard Thai collocations ปัญหาอยู่ที่..., คำตอบอยู่ที่..., ความสำเร็จอยู่ที่... — whereas อยู่ใน carries a spatial 'inside a container' connotation that reads as translationese-stiff at the THSV2011 register. A single-preposition refinement (ใน → ที่) fully preserves the Greek meaning of ἐν τούτῳ, leaves both locked phrases intact (มิใช่ที่เรารักพระเจ้า แต่เป็นที่พระองค์ทรงรักเรา; ทรงใช้พระบุตรของพระองค์มาเป็นเครื่องบูชาไถ่บาปของเรา), and involves no theological change whatsoever; native-speaker adjudication is recommended because the อยู่ใน / อยู่ที่ boundary for abstract constructions can be register-sensitive.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_01_optimal_001 -->
### Revelation 1:12

**Current:**

> เสียงที่กำลังพูดกับข้าพเจ้า

**Proposed:**

> เสียงที่กำลังกล่าวกับข้าพเจ้า

**Why:** λαλέω (ἐλάλει, imperfect active) → พูด is rendered at a conversational register that creates an intra-chapter inconsistency: v.11 (unlocked) already uses กล่าวว่า for the same unidentified voice's speech, while v.12 drops to พูดกับ for the same voice's ongoing speech. กล่าว is the THSV2011-standard formal verb for narrative speech attribution and sustains the prophetic-vision register that prevails throughout the chapter (ตรัสว่า v.17, กล่าวว่า v.11). Substituting กล่าว for พูด carries the identical semantic content of λαλέω and harmonizes register without touching the locked term เชิงตะเกียงทองคำเจ็ดอัน or any theological content. Routed defer_to_native because the imperfective relative-clause position (กำลัง + verb + กับ) may have a subtlety that the Tier-A Thai reviewer should confirm.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_02_optimal_001 -->
### Revelation 2:22

**Current:**

> พวกที่เล่นชู้กับนาง

**Proposed:**

> พวกที่ล่วงประเวณีกับนาง

**Why:** เล่นชู้ is a colloquial Thai expression for sexual infidelity that sits well below the formal-evangelical register the letter sustains throughout; it reads as chat-speak rather than solemn judicial speech. Within the same Jezebel-judgment passage (vv.20–23), the locked text of v.20 already renders the cognate sin (πορνεύω) as ล่วงประเวณี (formal), so rendering μοιχεύω with เล่นชู้ just two verses later introduces a conspicuous intra-letter register gap. Substituting ล่วงประเวณีกับนาง restores consistency with the established register and preserves the gravity of the divine-judgment context; no theological meaning changes, and the locked term เราจะโยนนางลงบนเตียง is entirely unaffected.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_05_optimal_003 -->
### Revelation 5:11

**Current:**

> ได้มองดู

**Proposed:**

> ได้เห็น

**Why:** Within Revelation 5, the Johannine vision-formula εἶδον (aorist of ὁράω) is rendered 'ได้เห็น' / 'เห็น' at vv. 1, 2, and 6; in v.11 the identical Greek verb shifts to 'ได้มองดู' ('gazed upon / looked') without any KD rationale documenting the switch. While 'มองดู' is not erroneous in isolation, the inconsistency within a single chapter creates subtle register unevenness in the visionary-formula refrain. Normalizing to 'ได้เห็น' would align v.11 with the chapter-wide pattern. Raised as fyi because the change may require a corpus-wide audit of εἶดον rendering before any single instance is altered, and because no translator rationale was present to rule out a deliberate stylistic variation at this verse.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_05_optimal_002 -->
### Revelation 5:3

**Current:**

> ที่จะสามารถเปิดหนังสือม้วนนั้นหรือดูในนั้นได้

**Proposed:**

> ที่สามารถเปิดหนังสือม้วนนั้นหรือดูในนั้นได้

**Why:** The Greek ἐδύνατο (imperfect of δύναμαι, 'was able to') is a single ability modal; the Thai renders it 'ที่จะสามารถ…ได้,' stacking ที่จะ (relativizer + potential marker) and สามารถ (ability auxiliary) where one suffices. In standard Thai, 'ที่สามารถ…ได้' carries identical meaning with less redundancy and fits the formal-evangelical register more naturally. The locked phrase 'ไม่มีใครในสวรรค์ บนแผ่นดินโลก หรือใต้แผ่นดินโลก' is wholly unaffected. The proposal is routed defer_to_native because a native Tier-A reviewer should confirm whether 'ที่จะสามารถ' was deliberately chosen here to heighten the emphasis of cosmic impossibility — if so, the current form should stand.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_05_optimal_001 -->
### Revelation 5:8

**Current:**

> ถือพิณและถือชามทองคำที่เต็มไปด้วยเครื่องหอม ซึ่งเป็นคำอธิษฐานของธรรมิกชน

**Proposed:**

> ถือพิณและชามทองคำที่เต็มไปด้วยเครื่องหอม ซึ่งเป็นคำอธิษฐานของธรรมิกชน

**Why:** The Greek ἔχοντες is a single participle governing a compound direct object — κιθάραν καὶ φιάλας χρυσᾶς — with no verb repeated for the second object. The Thai mirrors a Semitic/Greek verbal-repetition pattern by writing 'ถือพิณและถือชาม,' but Thai does not require or expect the governing verb to reappear before each item in a compound object list; 'ถือพิณและชาม' is the idiomatic form. Dropping the second 'ถือ' removes the translationese stiffness without any loss of meaning and without touching any locked term: 'ชามทองคำที่เต็มไปด้วยเครื่องหอม ซึ่งเป็นคำอธิษฐานของธรรมิกชน' is preserved verbatim in the proposed text. No theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_06_optimal_003 -->
### Revelation 6:11

**Current:**

> พักอีกชั่วคราวหนึ่ง

**Proposed:**

> พักอีกระยะหนึ่ง

**Why:** The Greek χρόνον μικρόν (a little while / a short span of time) is rendered ชั่วคราวหนึ่ง, but in contemporary Thai ชั่วคราว primarily functions as an adjective or adverb meaning 'temporary/provisional' (งานชั่วคราว, a temporary job; ที่พักชั่วคราว, temporary lodging) rather than a measurable short duration. Using it as a count noun (ชั่วคราวหนึ่ง = 'one temporary period') is mildly awkward and risks ambiguity for modern readers who may read พักชั่วคราว as 'rest on a provisional basis' rather than 'rest for a short while.' Thai ระยะหนึ่ง (a while / a brief stretch) renders the sense of χρόνον μικρόν more naturally and without ambiguity. Both locked terms (พวกเขาแต่ละคนได้รับเสื้อคลุมขาว and จนกว่าจำนวนของเพื่อนทาส…จะครบบริบูรณ์) are fully preserved and no theological content shifts. Routing defer_to_native because older Thai biblical usage may treat ชั่วคราว in the sense of ชั่วขณะ and a native reader should confirm whether the current form still reads naturally in this register.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_06_optimal_002 -->
### Revelation 6:12

**Current:**

> แผ่นดินไหวอย่างรุนแรงเกิดขึ้น

**Proposed:**

> เกิดแผ่นดินไหวอย่างรุนแรง

**Why:** The current rendering mirrors the Greek noun-first word order (σεισμὸς μέγας ἐγένετο → แผ่นดินไหวอย่างรุนแรง เกิดขึ้น), which is syntactically valid Thai but leans translationese. Thai existential and eventive clauses characteristically front the event verb: เกิดแผ่นดินไหวอย่างรุนแรง (lit. 'there occurred a violent earthquake') is the normal Thai idiom for seismic events — compare how news broadcasts and everyday speech universally use เกิดแผ่นดินไหว — and sits comfortably in the THSV2011 register. The locked sun-and-moon imagery in the remainder of the verse is entirely unaffected, and no meaning or theological content changes. Routing defer_to_native because formal-register biblical Thai occasionally accepts the more literal subject-first order in this tradition.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_07_optimal_001 -->
### Revelation 7:4

**Current:**

> เป็นผู้ที่ถูกประทับตราจากทุกเผ่าของบรรดาบุตรอิสราเอล

**Proposed:**

> จากทุกเผ่าของบรรดาบุตรอิสราเอล

**Why:** The Greek resumptive/appositional participle ἐσφραγισμένοι (nom. pl.) after the 144,000 figure is a Hellenistic anacoluthon — the clause restarts with the same participle to attach 'from every tribe of Israel' as a complement. Rendered literally, the Thai repeats 'ผู้ที่ถูกประทับตรา' twice in the same sentence (once at the head of the clause, again in 'เป็นผู้ที่ถูกประทับตราจากทุกเผ่า'), producing translationese-stiff redundancy that a Thai reader experiences as noise. Dropping 'เป็นผู้ที่ถูกประทับตรา' and attaching 'จากทุกเผ่าของบรรดาบุตรอิสราเอล' directly after the count is the natural Thai structure: the sealed referent is fully established by the head noun 'ผู้ที่ถูกประทับตรา' earlier in the same clause. The locked term 'หนึ่งแสนสี่หมื่นสี่พันคน' is preserved verbatim; no theological content is altered — the full meaning (144,000 sealed persons drawn from every tribe of Israel) is retained without change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_09_optimal_002 -->
### Revelation 9:4

**Current:**

> และได้มีคำสั่งกับพวกมันว่า

**Proposed:**

> และมีคำสั่งมาถึงพวกมันว่า

**Why:** The Greek ἐρρέθη αὐταῖς (it was said/commanded to them, divine passive) is rendered as ได้มีคำสั่งกับพวกมัน, which combines the completive marker ได้ with the existential verb มี in a collocation — ได้มีคำสั่ง — that is grammatically non-standard: มี does not naturally take ได้ as a completive in this idiom in Thai. The cleaner construction มีคำสั่งมาถึงพวกมัน ('a command reached them') conveys the divine-passive sense with no named agent and sits within THSV2011 register. The locked phrase 'คนที่ไม่มีตราของพระเจ้าบนหน้าผาก' later in the verse is wholly untouched. Routed to native reviewer because the distinction between ได้มีคำสั่งกับ and มีคำสั่งมาถึง in formal-religious Thai register is subtle enough to require a native ear.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_10_optimal_001 -->
### Revelation 10:8

**Current:**

> ได้พูดกับข้าพเจ้าอีก กล่าวว่า

**Proposed:**

> ได้กล่าวกับข้าพเจ้าอีกว่า

**Why:** The current Thai mechanically mirrors the two Greek participles (λαλοῦσαν + λέγουσαν) with two near-synonymous verbs, producing 'พูด...กล่าวว่า' — a register-inconsistent pairing where พูด sits in the colloquial register while กล่าวว่า is formal-literary, and both verbs convey the same speech act. Optimal-evangelical-formal register (THSV2011 level) calls for a single formal verb throughout. The proposed กล่าวกับ...อีกว่า collapses the redundancy, resolves the register mismatch, and fully preserves the πάλιν nuance (อีก = again) along with the temporal logic of the verse. The locked direct-speech phrase 'จงไปรับหนังสือม้วนที่เปิดอยู่' is untouched, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_10_optimal_002 -->
### Revelation 10:9

**Current:**

> ขอให้เขาให้หนังสือม้วนเล็กแก่ข้าพเจ้า

**Proposed:**

> ขอให้เขามอบหนังสือม้วนเล็กแก่ข้าพเจ้า

**Why:** The current Thai produces a double ให้ ('ขอให้เขาให้') — grammatically valid but phonetically awkward and below the formal-literary register of the passage. Replacing the second ให้ with มอบ (to present/hand over) removes the stutter and elevates register to match the vision-narrative tone without altering the semantic content of δοῦναί μοι ('give to me'). The locked key term หนังสือม้วนเล็ก is preserved verbatim, and the locked direct-speech block is entirely unaffected. A Tier-A Thai reviewer should confirm whether มอบ, ยื่น, or another formal-register verb of transfer feels most natural here.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_11_optimal_004 -->
### Revelation 11:10

**Current:**

> ดีใจและสนุกสนานต่อพวกเขา

**Proposed:**

> ยินดีและร่าเริงต่อพวกเขา

**Why:** The key_decisions entry for 11:10 covers only the gift-exchange (Esther echo in 'และจะส่งของขวัญให้กันและกัน'); the verbs of rejoicing are not addressed. 'ดีใจ' (personally glad, colloquial) and especially 'สนุกสนาน' (have fun / be merry in an everyday casual sense) sit in a register below the THSV2011 optimal-evangelical-formal target. In standard Thai-biblical usage χαίρω is rendered 'ยินดี' and εὐφραίνομαι 'ร่าเริง' or 'รื่นเริง'; 'สนุกสนาน' carries a marked casual-entertainment connotation. Proposed 'ยินดีและร่าเริง' matches THSV register while conveying the same ironic, wicked celebration; the locked phrase 'และจะส่งของขวัญให้กันและกัน' is untouched and no theological meaning changes. Marked fyi because a corpus-wide normalization of χαίρω/εὐφραίνομαι rendering may be in scope elsewhere in Revelation and should be handled in a single pass.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_13_optimal_001 -->
### Revelation 13:14

**Current:**

> ผู้ที่อาศัยอยู่บนแผ่นดินโลก ด้วยการอัศจรรย์ที่ได้รับอนุญาตให้ทำต่อหน้าสัตว์ร้าย และบอกให้ผู้ที่อาศัยอยู่บนแผ่นดินโลกสร้างรูปจำลองให้แก่สัตว์ร้าย

**Proposed:**

> ผู้ที่อาศัยอยู่บนแผ่นดินโลก ด้วยการอัศจรรย์ที่ได้รับอนุญาตให้ทำต่อหน้าสัตว์ร้าย และบอกให้พวกเขาสร้างรูปจำลองให้แก่สัตว์ร้าย

**Why:** The Greek repeats τοὺς κατοικοῦντας ἐπὶ τῆς γῆς twice in this verse — first as the object of πλανᾷ, then as the indirect object of λέγων — and the Thai mirrors both occurrences with the full formula ผู้ที่อาศัยอยู่บนแผ่นดินโลก within a single sentence, producing translationese-stiff prose. In natural THSV2011-register Thai, the second co-referential mention in the same sentence would be pronominalized to พวกเขา; the referent is unambiguous at that point, so no meaning is lost. The locked term สร้างรูปจำลองให้แก่สัตว์ร้าย is preserved verbatim and no theological content is altered. Deferred to native review because ผู้ที่อาศัยอยู่บนแผ่นดินโลก is a corpus-spanning formula throughout Revelation (κατοικοῦντες ἐπὶ τῆς γῆς), and the corpus-wide consistency policy should govern whether local pronominalization within a single verse is acceptable practice.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_14_optimal_002 -->
### Revelation 14:12

**Current:**

> ในที่นี้เป็นความอดทนของบรรดาธรรมิกชน

**Proposed:**

> นี่คือความอดทนของบรรดาธรรมิกชน

**Why:** Ὧδε in Revelation's recurring call-to-attention formula (cf. 13:10 Ὧδε ἡ ὑπομονή; 13:18 Ὧδε ἡ σοφία ἐστίν) functions as a logical-rhetorical pointer — 'herein lies / this is the...' — calling the hearer to moral attention, not identifying a physical location. The Thai ในที่นี้เป็น reads as 'in this place is', introducing an unintended spatial-locative concreteness that blunts the exhortatory rhetorical force of the formula. นี่คือ is the natural THSV2011-register rendering for such identification-clause discourse markers and more accurately captures the pragmatic thrust. Deferred to native reviewer to verify corpus consistency: if Rev 13:10 and 13:18 already render Ὧดε with a different formula in this translation, a uniform normalization pass across all three occurrences would be preferable to a single-verse change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_14_optimal_001 -->
### Revelation 14:20

**Current:**

> และบ่อย่ำองุ่นถูกย่ำนอกเมือง

**Proposed:**

> และบ่อย่ำองุ่นถูกเหยียบนอกเมือง

**Why:** The Thai verb ย่ำ (to tread/press with the feet) is already embedded in the established compound noun บ่อย่ำองุ่น (grape-treading-vat), so the passive ถูกย่ำ produces a jarring lexical collision — 'the grape-treading-vat was grape-trodden' — that reads as awkward, almost tautological Thai. Replacing the passive verb with เหยียบ (to tread/trample underfoot) renders πατέω with equal semantic fidelity — both words denote pressing down with the foot — while eliminating the surface repetition. เหยียบ additionally carries a slightly more visceral 'trample underfoot' force that suits the Isa 63 divine-warrior winepress-judgment imagery underlying this passage. The locked compound noun บ่อย่ำองุ่น is preserved verbatim, and no theological meaning is changed.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_18_optimal_001 -->
### Revelation 18:22

**Current:**

> จะไม่มีให้ได้ยินในเจ้าอีกต่อไป

**Proposed:**

> จะไม่ได้ยินในเจ้าอีกต่อไป

**Why:** The same Greek form οὐ μὴ ἀκουσθῇ ἐν σοὶ ἔτι appears twice in this verse; KD2 locks the second occurrence's predicate as 'จะไม่ได้ยินในเจ้าอีกต่อไป' — the translator's own preferred, clean construction. The first occurrence's predicate 'จะไม่มีให้ได้ยิน' is an existential-impersonal circumlocution ('there will be nothing for [anyone] to hear') that reads as translationese-stiff against the THSV2011 target register. Harmonizing to 'จะไม่ได้ยินในเจ้าอีกต่อไป' removes the awkward impersonal layer, achieves internal consistency within the same verse, and introduces zero theological change. All KD1-locked musical-group terms remain verbatim.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_19_optimal_001 -->
### Revelation 19:10

**Current:**

> เราเป็นเพื่อนผู้รับใช้กับท่าน และเป็นเพื่อนผู้รับใช้กับพี่น้องของท่าน ผู้ซึ่งมีคำพยานของพระเยซู

**Proposed:**

> เราเป็นเพื่อนผู้รับใช้กับท่าน และกับพี่น้องของท่าน ผู้ซึ่งมีคำพยานของพระเยซู

**Why:** The Greek σύνδουλός σού εἰμι καὶ τῶν ἀδελφῶν σου has a single predicate nominative (σύνδουλος) that governs two genitive objects joined by καί — there is no second predicate in the source. The current Thai expands this into two full parallel predicate-clauses, each carrying its own 'เป็นเพื่อนผู้รับใช้กับ,' a syntactic mirroring of Greek nominal government that Thai does not require and that produces a translationese-stiff rhythm in the angel's urgent rebuke. Dropping the repeated predicate in the second clause — leaving 'และกับพี่น้องของท่าน' — preserves the KD-locked phrase 'เราเป็นเพื่อนผู้รับใช้กับท่าน' verbatim, retains the full theological force (the angel is fellow-servant of both John and his brothers who hold the testimony of Jesus), and yields more natural, compressed Thai without altering meaning. Routed defer_to_native because a native reviewer should confirm whether the parallel-clause rhetorical weight carries appropriate solemnity in this rebuke context or whether the compressed form reads as underweight.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_20_optimal_002 -->
### Revelation 20:3

**Current:**

> ชั่วระยะเวลาหนึ่ง

**Proposed:**

> ชั่วระยะเวลาอันสั้น

**Why:** The Greek μικρὸν χρόνον means 'a short / little time'—the μικρόν qualifier carries eschatological weight, explicitly marking Satan's post-millennial release as deliberately brief before his final defeat. The current 'ชั่วระยะเวลาหนึ่ง' renders only 'for a period of time,' silently dropping μικρόν entirely, while the formal-bureaucratic compound ระยะเวลา tips the phrase toward translationese-stiff rather than optimal-evangelical-formal. 'ชั่วระยะเวลาอันสั้น' restores the 'short' qualifier in natural Thai at the THSV2011 register level without adding theological content. The KD2 rationale focuses exclusively on δεῖ (divine necessity) and does not address μικρόν, so the omission appears undocumented rather than intentional; flagged as fyi because the translator may hold a readability rationale not captured in the ledger. Both locked phrases ('แล้วปิดและประทับตราเหนือมันไว้' and 'เพื่อมันจะไม่หลอกลวงประชาชาติทั้งหลายอีก จนกว่าพันปีนั้นจะสำเร็จ') are fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## title_collision (2)

<!-- POLISH_PROPOSAL id=acts_03_001 -->
### Acts 3:22

**Current:**

> องค์พระผู้เป็นเจ้าพระเจ้า

**Proposed:**

> องค์พระผู้เป็นเจ้า พระเจ้า

**Why:** The divine titles run together as องค์พระผู้เป็นเจ้า + พระเจ้า without a visible grammatical break. Adding a space separates the titles for oral reading while leaving the title words unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_16_001 -->
### Revelation 16:7

**Current:**

> องค์พระผู้เป็นเจ้าพระเจ้า

**Proposed:**

> องค์พระผู้เป็นเจ้า พระเจ้า

**Why:** The divine titles run together as องค์พระผู้เป็นเจ้า + พระเจ้า without a visible grammatical break. Adding a space separates the titles for oral reading while leaving the title words unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

## wooden_passive (39)

<!-- POLISH_PROPOSAL id=matthew_20_optimal_001 -->
### Matthew 20:10

**Current:**

> คนที่ถูกว่าจ้างเป็นพวกแรก

**Proposed:**

> คนพวกแรก

**Why:** Greek οἱ πρῶτοι is a bare substantival adjective ('the first ones') carrying no verb; the Thai supplies ถูกว่าจ้าง ('were-hired', ถูก- passive) for reader clarity, a construction absent from the source text and undocumented in either KD entry for this verse. 'คนพวกแรก' removes the unwarranted passive and is consistent with the simpler noun-phrase pattern already established in v.8 (คนสุดท้าย / คนแรก), which renders the same ἔσχατοι / πρῶτοι pair without any added verb. However, v.9's locked phrase 'คนที่ถูกว่าจ้างเมื่อประมาณห้าโมงเย็น' uses the identical ถูก-ว่าจ้าง construction as a structural parallel to v.10; correcting v.10 in isolation would break intra-chapter symmetry, so any normalization must address both verses simultaneously and lies beyond the scope of a single-verse polish pass.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_24_optimal_001 -->
### Matthew 24:9

**Current:**

> พวกท่านจะถูกชนทุกชาติเกลียดชังเพราะนามของเรา

**Proposed:**

> ชนทุกชาติจะเกลียดชังพวกท่านเพราะนามของเรา

**Why:** Greek ἔσεσθε μισούμενοι is a future passive with an explicit prominent agent (ὑπὸ πάντων τῶν ἐθνῶν). When the agent is stated, Thai natively prefers an agent-fronted active construction over ถูก- passive. The KD addresses only 'เพราะนามของเรา' and the dynamic rendering of παραδίδωμι; the passive choice for μισούμενοι is undocumented. Fronting the agent preserves the Greek sense of universal persecution while reading more naturally. Locked term 'เพราะนามของเรา' is verbatim-preserved; no theological content changes. Flagged defer_to_native because ถูก- is not wrong—it may be deliberately foregrounding the disciples as sufferers—and a Tier-A native reviewer should adjudicate.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_26_optimal_002 -->
### Matthew 26:13

**Current:**

> จะถูกเล่าขาน

**Proposed:**

> จะได้รับการเล่าขาน

**Why:** Thai ถูก- passive carries a negative semantic valence—events that befall the subject adversely—whereas λαληθήσεται here describes a positive memorial proclamation honoring a woman's deed. The ได้รับการ- construction is the standard Thai pattern for positive or neutral passives (cf. ได้รับการยกย่อง, ได้รับการกล่าวถึง) and sits more naturally in an honorific context. The locked term เป็นที่ระลึกถึงนาง is unaffected by the change. No KD rationale in v.13 specifically justifies the ถูก- choice (KD3 addresses only เป็นที่ระลึกถึงนาง). The confidence is defer_to_native because whether จะถูกเล่าขาน has sufficiently neutralized its negative valence with the verb เล่าขาน in this register is a judgment that benefits from a Tier-A Thai-language reviewer. No theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_26_optimal_001 -->
### Matthew 26:24

**Current:**

> ผู้ที่บุตรมนุษย์จะถูกมอบไว้โดยการกระทำของเขา

**Proposed:**

> ผู้ที่มอบบุตรมนุษย์ไว้

**Why:** The Greek δι᾽οὗ...παραδίδοται identifies the betrayer as instrument ('through whom the Son of Man is handed over'), but the Thai ผู้ที่...จะถูกมอบไว้โดยการกระทำของเขา is circular: the relative pronoun ผู้ที่ already establishes the agent, making the appended โดยการกระทำของเขา redundant and heavy. Thai natively prefers active voice in such agent-relative clauses, and the same passive-to-active shift is already attested within the chapter's own KD apparatus (v.31 KD5: 'Passive → Thai active-idiom'). The proposed ผู้ที่มอบบุตรมนุษย์ไว้ preserves both the locked term บุตรมนุษย์ and the consistent παραδίδωμι → มอบ...ไว้ rendering used throughout the chapter (vv.15, 16, 21, 23, 45, 46). No theological change: the same betrayer-handing-over-Jesus meaning is carried, simply without the circumlocutory passive frame.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=matthew_27_optimal_001 -->
### Matthew 27:8

**Current:**

> จึงถูกเรียกว่าทุ่งโลหิต

**Proposed:**

> จึงเรียกกันว่าทุ่งโลหิต

**Why:** The aorist passive ἐκλήθη is rendered with the heavy ถูก- construction (ถูกเรียกว่า), yet neither KD1 nor KD2 documents a reason to prefer the formal Thai passive over the impersonal active. In THSV2011-register narrative, เรียกกันว่า ('people call it' / 'it is known as') is the standard idiom for place-name assignments and narrator-asides—it carries the same passive semantic without the ถูก- weight that normally signals affliction or an unwilling recipient. Both locked terms (ทุ่งโลหิต and จนถึงทุกวันนี้) are fully preserved, and the meaning (this field bears the name Blood Field to this day) is unchanged; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=luke_12_optimal_002 -->
### Luke 12:3

**Current:**

> จะถูกได้ยินในความสว่าง

**Proposed:**

> จะได้ยินกันในความสว่าง

**Why:** ἀκουσθήσεται (future passive of ἀκούω, 'will be heard') is rendered ถูก + ได้ยิน — an awkward double-passive stack, since ได้ยิน already carries a receptive reading in Thai and does not typically collocate with ถูก in natural speech. No KD entry addresses this construction; the three rationales for v.3 cover เพราะฉะนั้น, ห้องชั้นใน, and ดาดฟ้า only. The impersonal form จะได้ยินกัน renders the passive sense more naturally and echoes v.2's own 'เป็นที่รู้กัน' pattern for a parallel divine-passive. All three locked terms for this verse (ดาดฟ้า, ห้องชั้นใน, เพราะฉะนั้น) fall outside the changed substring and are untouched; the eschatological sense that God will cause hidden speech to be made public is fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_10_optimal_001 -->
### John 10:21

**Current:**

> ถ้อยคำเหล่านี้ไม่ใช่คำของคนที่ถูกผีสิง

**Proposed:**

> ถ้อยคำเหล่านี้ไม่ใช่คำของคนที่มีผีเข้าสิง

**Why:** The Greek δαιμονιζομένου (present passive participle of δαιμονίζω) is rendered in v.21 with the ถูก- passive marker ('ถูกผีสิง'), yet the corpus-locked rendering at v.20 for the semantically equivalent expression δαιμόνιον ἔχει is the active-existential construction 'มีผีเข้าสิง.' Thai natively prefers the active-existential 'มีผีเข้าสิง' over the ถูก- passive in demonic-possession contexts, as ถูก- carries a slightly clinical-victim connotation absent from the Greek participle. Replacing 'ถูกผีสิง' with 'มีผีเข้าสิง' restores intra-chapter consistency with v.20's corpus lock, removes the wooden passive, and faithfully represents δαιμονιζομένου; the only locked phrase in this verse, 'ผีจะเปิดดวงตาคนตาบอดได้หรือ?', is entirely untouched and no theological meaning changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_12_optimal_001 -->
### John 12:16

**Current:**

> สิ่งเหล่านี้ได้มีเขียนเกี่ยวกับพระองค์

**Proposed:**

> สิ่งเหล่านี้มีเขียนไว้เกี่ยวกับพระองค์

**Why:** The Greek γεγραμμένα (perfect passive participle, 'had been written about him') is rendered as 'ได้มีเขียน' — an unusual Thai construction that stacks the aspect marker ได้ onto the existential verb มี without the standard preservation-result marker ไว้. This produces a stilted phrase, compounded by the fact that ระลึกได้ earlier in the same clause means two ได้ land in close succession within the reported-speech frame. John 12:14 of the same chapter already uses 'ตามที่มีเขียนไว้ว่า' as the established corpus formula for γεγραμμένον; aligning v.16 to 'มีเขียนไว้เกี่ยวกับพระองค์' removes the doubled-ได้ awkwardness, matches that intra-chapter pattern, and better captures the Greek perfect's 'written-and-still-on-record' nuance via ไว้. The locked phrase เมื่อพระเยซูได้รับพระสิริ is entirely untouched; no theological change is involved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_14_optimal_003 -->
### John 14:21

**Current:**

> ผู้ที่รักเราจะได้รับความรักจากพระบิดาของเรา

**Proposed:**

> พระบิดาของเราจะทรงรักผู้ที่รักเรา

**Why:** The Greek future passive states the divine agent explicitly (ὑπὸ τοῦ πατρός μου); Thai idiom and the corpus rule (ทรง- on all divine actions) both strongly favour fronting the Father as active grammatical subject. The current ได้รับความรัก receive-passive keeps the human disciple as syntactic subject, muting the Father's initiative that the Greek foregrounds. The proposed agent-fronted form 'พระบิดาของเราจะทรงรักผู้ที่รักเรา' also creates a tight parallel with the immediately following active clause 'เราเองก็จะรักเขา', giving the two divine-love statements symmetrical syntax. Confidence is defer_to_native because the micro-level discourse rhythm of subject-fronting at this point is best verified by a Tier-A Thai reviewer; the locked term 'จะสำแดงตนเองให้เขาเห็น' later in the verse is preserved unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_20_optimal_001 -->
### John 20:30

**Current:**

> ซึ่งไม่ได้ถูกบันทึกไว้ในหนังสือเล่มนี้

**Proposed:**

> ซึ่งไม่ได้บันทึกไว้ในหนังสือเล่มนี้

**Why:** The Greek γεγραμμένα (perfect passive 'have been written/recorded') is rendered with the ถูก- passive marker, producing ไม่ได้ถูกบันทึกไว้ — a stacked ไม่ได้ + ถูก construction that is noticeably stiff in Thai. The ถูก marker typically signals an adversarial or unintended action done to a subject, which is tonally incongruous for a calm authorial note about the scope of the record. Dropping ถูก to yield ไม่ได้บันทึกไว้ produces natural Thai resultative-stative phrasing ('have not been recorded') in formal-evangelical register. No KD rationale justifies the ถูก construction here, and the corpus-locked phrase ในหนังสือเล่มนี้ is preserved verbatim. The theological content is unchanged.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=john_20_optimal_002 -->
### John 20:31

**Current:**

> สิ่งเหล่านี้ถูกบันทึกไว้

**Proposed:**

> สิ่งเหล่านี้บันทึกไว้

**Why:** The Gospel's climactic purpose declaration — 'these things have been written so that you may believe' — carries a deliberate, purposeful tone that the ถูก- passive undercuts in Thai: ถูก implies something happening to a subject without or against intent, whereas this is a triumphant authorial statement. Thai formal prose naturally uses the bare resultative form บันทึกไว้ (is recorded / stands written) in declarative-purpose constructions; สิ่งเหล่านี้บันทึกไว้เพื่อพวกท่านจะเชื่อ is idiomatic THSV2011-register Thai. No KD rationale locks the ถูก construction; the corpus-locked clauses เพื่อพวกท่านจะเชื่อว่าพระเยซูทรงเป็นพระคริสต์ พระบุตรของพระเจ้า and มีชีวิตในพระนามของพระองค์ are entirely untouched. The theological content and Greek meaning are fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_01_optimal_001 -->
### Acts 1:19

**Current:**

> จนที่ดินผืนนั้นถูกเรียกในภาษาของพวกเขาเองว่า

**Proposed:**

> จนที่ดินผืนนั้นมีชื่อในภาษาของพวกเขาเองว่า

**Why:** The Greek result-clause ὥστε κληθῆναι τὸ χωρίον (aorist passive infinitive of καλέω, 'so that the field was called') is mapped word-for-word onto the ถูก- passive 'ถูกเรียก.' For a place acquiring a proper name, Thai narrative convention gravitates toward active or stative constructions — most naturally 'มีชื่อว่า' ('bears the name') or impersonal active 'เรียกว่า' — rather than the ถูก- passive, which introduces a faint adversarial/agentive undertone foreign to simple naming. The locked phrase 'ในภาษาของพวกเขาเอง' is preserved verbatim in the proposal; the locked terms 'อาเคลดามา' and 'ทุ่งโลหิต' remain unchanged in the wider verse. No KD entry addresses or justifies the choice of the passive construction here. Whether 'มีชื่อ' is clearly preferable to 'ถูกเรียก' in formal Bible-register Thai turns on a fine register judgment that warrants a Tier-A native reviewer's ear before committing.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=acts_19_optimal_001 -->
### Acts 19:12

**Current:**

> ผ้าเช็ดหน้าและผ้ากันเปื้อนที่ได้สัมผัสร่างกายของเปาโลถูกนำไปวางบนคนป่วย

**Proposed:**

> มีการนำผ้าเช็ดหน้าและผ้ากันเปื้อนที่ได้สัมผัสร่างกายของเปาโลไปวางบนคนป่วย

**Why:** The Greek ἀποφέρεσθαι is an agent-neutral passive infinitive inside the ὥστε result clause; no agent is specified. The Thai ถูกนำไปวาง uses the ถูก- passive, whose adversarial connotation — implying something negative happening to the grammatical subject — is tonally mismatched for the beneficent miracle context of healing cloths being brought to the sick. None of the three key_decisions for this verse documents or justifies the ถูก- construction (KD1 addresses χρώς, KD2 the cloth types, KD3 the dual healing outcomes). The impersonal construction มีการนำ…ไปวางบนคนป่วย mirrors the Greek agent-neutral passive without the adversarial tinge, preserves both locked terms verbatim (ผ้าเช็ดหน้าและผ้ากันเปื้อน and ที่ได้สัมผัสร่างกายของเปาโล), and changes no theological meaning; whether this precise construction sounds optimal requires a native Tier-A reviewer to confirm register fit within the THSV2011 style.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_02_optimal_001 -->
### Romans 2:13

**Current:**

> จะทรงถูกประกาศว่าชอบธรรม

**Proposed:**

> จะทรงนับว่าชอบธรรม

**Why:** The current rendering fuses the royal-agent prefix ทรง- (which Thai grammar reserves for a divine or royal subject acting) with the patient-passive marker ถูก-, producing the anomalous cluster ทรงถูกประกาศ; Thai cannot coherently combine an agentive-subject honorific with a patient-passive marker on the same verbal complex, making the phrase feel both grammatically strained and register-contradictory. The KD2 ledger entry for this verse already records the translator's documented choice as 'จะทรงนับว่าชอบธรรม' (= 'royally-reckon-as-righteous'), an active-divine construction that renders the Greek divine passive δικαιωθήσονται cleanly and sustains Paul's imputational-justification theology without the ทรง/ถูก collision. The proposed text restores the KD2-locked term verbatim and preserves all other locked terms in the verse (ผู้ฟังธรรมบัญญัติ, ผู้ประพฤติตามธรรมบัญญัติ) unchanged; no theological alteration is involved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_08_optimal_001 -->
### Romans 8:21

**Current:**

> จะถูกปลดปล่อยจากการเป็นทาสของความเสื่อมสลาย

**Proposed:**

> จะได้รับการปลดปล่อยจากการเป็นทาสของความเสื่อมสลาย

**Why:** ἐλευθερωθήσεται is the future passive of ἐλευθερόω ('will be set free / will be liberated'), here rendered with the Thai ถูก-passive. In Thai, ถูก- prototypically marks an action that is adverse or unwelcome to the grammatical subject, so 'จะถูกปลดปล่อย' carries an unintended negative valence—as if liberation were something unpleasant happening to creation. Because Paul's point is entirely beneficent (creation will be emancipated into the glorious freedom of God's children), 'จะได้รับการปลดปล่อย' ('will receive liberation') aligns the passive construction with the positive character of the divine act. The Greek meaning, the theological content, and the locked phrase 'จากการเป็นทาสของความเสื่อมสลาย' are all preserved without alteration.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_10_optimal_001 -->
### Romans 10:15

**Current:**

> ถ้าไม่ได้รับการส่งไป

**Proposed:**

> ถ้าไม่มีผู้ส่งพวกเขาไป

**Why:** ἀποσταλῶσιν (aorist passive subjunctive of ἀποστέλλω, 'be sent / be commissioned') is rendered as ได้รับการส่งไป, the heavy ได้รับการ- passive frame. Embedded in Paul's four-link rhetorical chain where each clause is terse and parallel, Thai naturally favours a shorter agent-fronted conditional: 'ถ้าไม่มีผู้ส่งพวกเขาไป' ('if there is no one to send them') — one predicate instead of two, removing the bureaucratic ได้รับการ- feel. The KD documents only the OT quotation in this verse and offers no justification for the passive construction itself. The commissioning sense of ἀποστέλλω is fully preserved; the unnamed agent (God or the sending church) remains equally implied by context. Routed to native review because the choice between impersonal passive and agent-fronted construction may carry subtle evangelical-register weight that a Tier-A Thai reviewer should confirm.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_14_optimal_001 -->
### Romans 14:21

**Current:**

> ถูกกีดกั้น

**Proposed:**

> ล้มลง

**Why:** σκανδαλίζεται is the passive of σκανδαλίζω ('be caused to stumble / be led into sin'), a word rooted in σκάνδαλον ('trap-spring / stumbling-snare'); it does not mean 'be blocked or obstructed.' The Thai ถูกกีดกั้น both imposes the heavy ถูก- passive marker—out of register with the two flanking predicates สะดุด ('stumble,' causative-active frame) and อ่อนแอ ('weak,' stative)—and imports กีดกั้น ('hindered / barred'), which replaces the falling image with an obstruction image foreign to the Greek. ล้มลง ('fall down') restores the σκάνδαλον stumble-and-fall metaphor, matches the pattern of the other two verbs that avoid ถูก-, and produces the natural three-part list 'สะดุด หรือล้มลง หรืออ่อนแอ' that escalates from the initial trip to the resulting collapse to sustained weakness. No theological content changes: the verse still warns against any act that causes a brother to stumble, fall, or be weakened in faith.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_15_optimal_001 -->
### Romans 15:15

**Current:**

> ที่ทรงประทานแก่ข้าพเจ้าโดยพระเจ้า

**Proposed:**

> ที่พระเจ้าทรงประทานแก่ข้าพเจ้า

**Why:** The Greek δοθεῖσάν is an aorist passive participle with explicit agent ὑπὸ τοῦ θεοῦ; the current Thai mirrors the Greek passive-then-agent word order by appending โดยพระเจ้า after the ทรง-prefixed verb. This is doubly awkward in Thai: ทรง- already signals a royal/divine subject, making the postpositive โดยพระเจ้า both redundant and structurally unusual, since Thai relative clauses natively front the agent before the verb. Rewriting to 'ที่พระเจ้าทรงประทานแก่ข้าพเจ้า' (agent-fronted) is the unmarked Thai pattern. Both locked terms ('อย่างกล้าหาญ' and 'เพื่อเตือนพวกท่านให้ระลึก') survive verbatim; theology is unchanged — the grace is still God's gift to Paul.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=romans_15_optimal_003 -->
### Romans 15:16

**Current:**

> ทรงชำระให้บริสุทธิ์โดยพระวิญญาณบริสุทธิ์

**Proposed:**

> ที่พระวิญญาณบริสุทธิ์ทรงชำระให้บริสุทธิ์

**Why:** Structurally identical to the 15:15 wooden-passive pattern: ทรง-prefix verb followed by a postpositive agent phrase (โดยพระวิญญาณบริสุทธิ์) in a Thai participial modifier where natural Thai would front the agent as a relative clause. Flagged fyi rather than apply for two reasons: (1) the Greek uses instrumental ἐν — not agent ὑπό — so the decision to read the Spirit as explicit agent versus sphere/means may already be a deliberate interpretive corpus choice the translator should adjudicate; (2) the same ทรง…โดย pattern recurs in v.15, suggesting a systemic convention that warrants a single corpus-wide normalisation pass rather than a piecemeal single-verse patch. Both locked phrases ('ปรนนิบัติในฐานะปุโรหิตด้วยข่าวประเสริฐของพระเจ้า' and 'เครื่องบูชาคือคนต่างชาติ') are preserved verbatim in the substituted verse.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_10_optimal_001 -->
### 1 Corinthians 10:11

**Current:**

> และได้รับการเขียนไว้เพื่อเป็นข้อตักเตือนสำหรับเรา

**Proposed:**

> และเขียนไว้เพื่อเป็นข้อตักเตือนสำหรับเรา

**Why:** The aorist passive ἐγράφη ('was written') is rendered as 'ได้รับการเขียนไว้' — the heavy ได้รับการ- passive construction, which in Thai is ordinarily reserved for a human beneficiary receiving an action done to them (e.g., ได้รับการรักษา, ได้รับการศึกษา) and sounds stiff and translationese when applied to the recording of scripture. In the THSV2011 register, agentless 'เขียนไว้' is the long-established natural Thai form for describing scripture as written down, as confirmed by the standard NT citation formula 'ตามที่เขียนไว้ว่า' (as it is written…) used throughout the Thai NT. The proposed 'และเขียนไว้เพื่อเป็นข้อตักเตือนสำหรับเรา' fully preserves the meaning of ἐγράφη πρὸς νουθεσίαν ἡμῶν, reads naturally to a modern Thai audience, and does not alter any theological content or any locked term; both 'สิ่งเหล่านี้เกิดขึ้นกับพวกเขาเป็นแบบอย่าง' and 'ผู้ที่อยู่ในยุคสุดท้ายของยุคทั้งหลาย' are preserved verbatim. The key_decisions rationale for v.11 addresses τυπικῶς and τὰ τέλη τῶν αἰώνων but provides no documented justification for the ได้รับการ- passive over the agentless form.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_13_optimal_001 -->
### 1 Corinthians 13:8

**Current:**

> ก็จะถูกทำให้สิ้นสภาพ

**Proposed:**

> ก็จะสิ้นสุดลง

**Why:** Both prophecy (καταργηθήσονται) and knowledge (καταργηθήσεται) translate the same καταργέω future passive, yet the Thai treats them asymmetrically within the same verse: prophecy receives the lighter intransitive 'ก็จะสิ้นสุดลง' while knowledge receives the heavier double-passive chain 'ก็จะถูกทำให้สิ้นสภาพ' (ถูก- + ทำให้ + สิ้นสภาพ). KD2 documents the theologically significant tense-distinction between καταργέω passive (prophecy + knowledge) and παύω middle (tongues), but does not justify the split rendering within the καταργέω pair itself — so the current asymmetry is undocumented. Complicating a single-verse fix: the locked v.13:10 phrase independently uses 'ถูกทำให้สิ้นสภาพ' for the same verb, creating cross-verse pressure in both directions — either (a) harmonise both v.8 καταργέω instances upward to the heavier form to honour the v.10 lock and restore the καταργέω-vs-παύω contrast, or (b) simplify knowledge to match prophecy's lighter 'ก็จะสิ้นสุดลง' for natural intra-verse parallelism and accept a divergence from v.10. Because the correct resolution is a corpus-level consistency decision rather than a single-verse polish, this is raised as fyi only; no change is recommended without a cross-chapter normalization review.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1corinthians_15_optimal_004 -->
### 1 Corinthians 15:9

**Current:**

> ถูกเรียกว่าเป็นอัครทูต

**Proposed:**

> ถูกเรียกว่าอัครทูต

**Why:** καλεῖσθαι ἀπόστολος is 'to be called apostle' — a passive infinitive with a bare predicate noun and no copula. Standard Thai quotative-verb constructions place ว่า immediately before the predicate noun: 'ถูกเรียกว่าอัครทูต' is the natural form; inserting เป็น after ว่า adds a redundant copula not required by Thai grammar and not present in the Greek. The ถูก- passive is retained and is appropriate here — its slight negative connotation in Thai aligns with Paul's self-deprecating claim that he does not deserve the designation. This is a one-element reduction with no doctrinal implication; surfaced as fyi in case a corpus-wide normalization pass is warranted.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_11_optimal_001 -->
### 2 Corinthians 11:12

**Current:**

> พวกเขาจะถูกพบว่าเหมือนเราเช่นกัน

**Proposed:**

> จะพบว่าพวกเขาก็เหมือนกับเราด้วย

**Why:** The aorist passive subjunctive εὑρεθῶσιν carries an evaluative sense — 'may turn out / prove to be' — not a physical act of discovery by a named agent. Thai ถูก- marks a concrete-agent passive; ถูกพบ primarily reads as 'to be caught/discovered,' not 'to prove to be,' so the construction is wooden in this credentialing context. An impersonal active จะพบว่า ('one will find that' / 'it will turn out that') is the standard Thai equivalent for evaluative εὑρίσκω and reads more naturally here. The locked phrase ตัดโอกาสของบรรดาผู้ที่ต้องการโอกาสจะอวด is untouched; no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=2corinthians_12_optimal_002 -->
### 2 Corinthians 12:15

**Current:**

> ข้าพเจ้าจะถูกรักน้อยลงหรือ?

**Proposed:**

> ข้าพเจ้าจะเป็นที่รักน้อยลงหรือ?

**Why:** Greek ἀγαπῶμαι is a stative present passive ('I am loved'); Thai 'ถูก-' passive is pragmatically marked for undesirable or adversarial events visited upon the subject, making 'ถูกรัก' sound incongruous when the predicate is a positive emotion — a native Thai reader would sense a slight register clash where the construction implies love as something happening against Paul. The standard Thai idiom for the stative passive of positive emotional predicates is 'เป็นที่รัก' (lit. 'to be in a state of being loved'), which is used consistently in literary and religious Thai including the THSV2011 tradition. The proposed rendering carries identical passive meaning and preserves Pauline rhetorical irony intact; the locked phrase 'ใช้จ่ายและถูกใช้จนหมดด้วยใจยินดียิ่งเพื่อชีวิตของพวกท่าน' in the preceding sentence is untouched, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=colossians_04_optimal_001 -->
### Colossians 4:16

**Current:**

> จดหมายฉบับนี้ได้รับการอ่านในหมู่พวกท่านแล้ว

**Proposed:**

> มีการอ่านจดหมายฉบับนี้ในหมู่พวกท่านแล้ว

**Why:** The current text renders the aorist passive subjunctive ἀναγνωσθῇ with a ได้รับการ- construction ('จดหมายฉบับนี้ได้รับการอ่าน'), which positions the letter as the experiencer of an action and reads as legalistic/bureaucratic formal Thai. Thai idiom strongly prefers the impersonal event construction 'มีการ + verb phrase' for communal public-action contexts — precisely the church-assembly reading Paul is describing. The proposed 'มีการอ่านจดหมายฉบับนี้ในหมู่พวกท่านแล้ว' carries the identical meaning and temporal sense of the Greek ὅταν-clause while sounding natural in modern evangelical Thai. Neither the KD1 nor KD2 rationale for this verse addresses the passive construction; both locked terms — ชาวเลาดีเซีย and จดหมายจากเมืองเลาดีเซีย — remain verbatim in the unchanged surrounding text, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=1timothy_06_optimal_001 -->
### 1 Timothy 6:5

**Current:**

> ถูกพรากจากความจริง

**Proposed:**

> ปราศจากความจริง

**Why:** The Greek ἀπεστερημένων (perfect passive participle of ἀποστερέω, 'having been deprived of') is rendered via the ถูก-passive construction 'ถูกพรากจากความจริง.' Sitting immediately after the locked participial phrase ending in 'จิตใจถูกทำลาย,' this creates a back-to-back double ถูก-passive ('ถูกทำลาย...ถูกพราก') that can feel labored in a Thai relative clause. KD1 documents the rationale for 'การเสียดสีกันอย่างต่อเนื่อง' and 'จิตใจถูกทำลาย' but does not supply a specific justification for retaining ถูกพราก over an alternative construction. The Thai prepositional idiom ปราศจาก ('devoid of / without') conveys the same resultant state of being without truth that ἀπεστερημένων τῆς ἀληθείας denotes, reads more naturally in flowing Thai, and dissolves the double-passive rhythm while preserving the locked phrase 'จิตใจถูกทำลาย' verbatim and leaving 'ถือว่าความเคร่งในพระเจ้าเป็นเครื่องมือหากิน' untouched. Whether ปราศจาก fully captures the passive-deprivation nuance (someone stripped them of truth) versus mere absence (they simply lack it) is a register call that warrants confirmation from a Tier-A Thai-language reviewer before applying.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_01_optimal_001 -->
### Hebrews 1:12

**Current:**

> จะถูกเปลี่ยนไปดุจเสื้อผ้า

**Proposed:**

> จะเปลี่ยนแปลงไปดุจเสื้อผ้า

**Why:** The future passive ἀλλαγήσονται is rendered with a ถูก- passive construction, which in Thai carries a connotation of external imposition or adversarial action and reads stiffly in this cosmological context. The parallel passive παλαιωθήσονται in the immediately preceding v.11 was correctly rendered as เก่าไป (intransitive process, no ถูก-), creating a visible inconsistency within the same unbroken psalm citation; applying the same pattern here yields จะเปลี่ยนแปลงไป. The proposed intransitive form treats the transformation of the heavens as a natural cosmic process, which is idiomatic Thai and fully preserves the Greek meaning — the created order will be transformed/exchanged. No locked terms are touched.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_02_optimal_003 -->
### Hebrews 2:17

**Current:**

> ต้องถูกทำให้เหมือนพี่น้องในทุกประการ

**Proposed:**

> ต้องเป็นเหมือนพี่น้องในทุกประการ

**Why:** The ถูก- passive prefix in Thai typically carries an implication of unpleasant or unwanted imposition, which introduces a theologically awkward tone when applied to the incarnation; ถูกทำให้เหมือน subtly frames the Son's becoming-human as something done to him against his character. The stative ต้องเป็นเหมือน ('was obligated to be like') already conveys divine necessity through ต้อง — reflecting ὤφειλεν — without the negatively-toned ถูก-. The KD rationale for v.17 documents the choices for ἀρχιερεύς, ἐλεήμων, πιστός, and ἱλάσκομαι but does not address the passive rendering of ὁμοιωθῆναι. Deferred to a native Thai theologian because the passive may be important to some readers as a signal of divine agency in the incarnation that the stative reading leaves implicit.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_02_optimal_001 -->
### Hebrews 2:3

**Current:**

> และได้รับการยืนยันแก่เราโดยผู้ที่ได้ฟังพระองค์

**Proposed:**

> และผู้ที่ได้ฟังพระองค์ก็ยืนยันแก่เรา

**Why:** ἐβεβαιώθη is an aorist passive with an explicit agent phrase (ὑπὸ τῶν ἀκουσάντων, 'by those who heard'), precisely the syntactic condition under which Thai strongly prefers agent-fronted active construction. The heavy ได้รับการยืนยัน reads as translationese; ผู้ที่ได้ฟังพระองค์ก็ยืนยันแก่เรา carries identical witness-confirmation meaning with natural Thai word order. The KD rationale addresses ἀρχὴν λαβοῦσα and the author's second-generation status but does not document a rationale for the passive rendering of ἐβεβαιώθη. No locked terms are touched and no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=hebrews_02_optimal_002 -->
### Hebrews 2:9

**Current:**

> ทรงได้รับการสวมมงกุฎด้วยพระสิริและเกียรติ

**Proposed:**

> ทรงสวมมงกุฎด้วยพระสิริและเกียรติ

**Why:** ἐστεφανωμένον is a Greek perfect passive, but the intended sense is a resultant exalted state ('wearing/crowned with glory') rather than an ongoing passive event, and Thai renders such resultant states naturally with the bare stative verb. The heavy ทรงได้รับการ- prefix foregrounds the receiving-process rather than the glorified state the perfect tense signals. The shorter form also echoes the v.7 vocabulary (ทรงสวมมงกุฎให้เขา from the same στεφανόω root), providing cross-verse lexical coherence. No KD rationale justifies the heavy passive construction here, no locked terms are affected, and the theology of post-passion glorification is fully preserved.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_03_optimal_001 -->
### Revelation 3:5

**Current:**

> จะได้รับการสวมในเสื้อผ้าขาวเช่นเดียวกัน

**Proposed:**

> จะสวมเสื้อผ้าขาวเช่นเดียวกัน

**Why:** The Greek περιβαλεῖται is a future middle-passive form of περιβάλλω; neither KD1 nor KD2 addresses its voice or justifies a passive rendering. The Thai ได้รับการสวมใน is an unusually heavy three-layer passive ('receive the being-clothed-in') that sounds stilted and is not natural in any Thai register. The simple active จะสวมเสื้อผ้าขาวเช่นเดียวกัน ('will wear white garments likewise') is semantically equivalent — whether read as a Greek middle ('will clothe himself') or divine passive ('will be clothed'), the conferred-honor meaning is unchanged. Both locked phrases (หนังสือแห่งชีวิต clause and ὁμολογέω clause) are untouched, and no theological content shifts.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_06_optimal_001 -->
### Revelation 6:14

**Current:**

> ถูกย้ายออกจากที่ของมัน

**Proposed:**

> เคลื่อนออกจากที่ของมัน

**Why:** Thai ถูกย้าย (passive: was moved/relocated) carries a strong connotation of deliberate administrative transfer — moving furniture, reassigning staff — which reads as mundanely bureaucratic for the cosmic displacement of mountains and islands on the Day of the Lord. The Greek ἐκινήθησαν (aor. pass. of κινέω, to be set in motion / displaced) simply denotes physical dislocation without implying a purposeful human-like agent. Thai เคลื่อนออก (to shift out of place, to be displaced) is the natural idiom for geological and cosmic upheaval and preserves the implicit passive sense that these massive features were set in motion by the cataclysm. The locked term ท้องฟ้าหดถอยไปดุจหนังสือม้วนที่ถูกม้วน is entirely untouched, and no theological content is altered.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_09_optimal_001 -->
### Revelation 9:18

**Current:**

> หนึ่งในสามของคนได้ถูกฆ่าจากสามภัยพิบัตินี้

**Proposed:**

> หนึ่งในสามของคนเสียชีวิตจากสามภัยพิบัตินี้

**Why:** The Greek ἀπεκτάνθησαν (aorist passive, 'were killed') is rendered as ได้ถูกฆ่า, stacking both the Thai completive particle ได้ and the adversative passive marker ถูก- in a construction that is heavier than necessary. Thai naturally prefers an intransitive verb when expressing death-by-cause: เสียชีวิตจาก ('perished from / died from') carries identical semantic weight — one third of the people died as a result of the three plagues — without the double-passive awkwardness. No KD rationale exists for this verse to justify the passive form. The agent (the three plagues, named in the following clause) and the scale of death (one third) are unchanged, so this is not a theological alteration.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_09_optimal_003 -->
### Revelation 9:20

**Current:**

> ที่ไม่ได้ถูกฆ่าจากภัยพิบัติเหล่านี้

**Proposed:**

> ที่ไม่ได้เสียชีวิตจากภัยพิบัติเหล่านี้

**Why:** The same Greek aorist passive ἀπεκτάνθησαν recurs here within a restrictive relative clause (οἳ οὐκ ἀπεκτάνθησαν ἐν ταῖς πληγαῖς ταύταις, 'who were not killed in these plagues'). The ถูก- passive marker in ไม่ได้ถูกฆ่า inside a relative clause produces slightly heavy syntax; ไม่ได้เสียชีวิตจากภัยพิบัติเหล่านี้ ('who did not die from these plagues') is the more natural Thai equivalent and preserves the Greek negative framing (οὐκ ἀπεκτάνθησαν) without the passive marker. The long locked idol-list phrase is fully preserved. Routed to native reviewer because ถูกฆ่า is not unacceptable in Thai relative clauses and the improvement is subtle enough to warrant a native-ear adjudication before applying.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_11_optimal_001 -->
### Revelation 11:2

**Current:**

> เพราะได้ถูกมอบให้แก่คนต่างชาติ

**Proposed:**

> เพราะถูกมอบให้แก่คนต่างชาติ

**Why:** The key_decisions entry for 11:2 addresses only πατέω (เหยียบ) and the forty-two-month eschatological period; the passive ἐดόθη is not discussed. The current Thai 'ได้ถูกมอบ' double-stacks the perfect-aspect marker ได้ with the passive marker ถูก, producing a redundant, heavy construction that no modern Thai speaker would choose naturally. Dropping ได้ yields 'ถูกมอบให้แก่คนต่างชาติ,' a clean standard passive that preserves the divine-passive force of ἐδόθη (God gave the outer court to the nations) without introducing an explicit agent. The locked phrase 'พวกเขาจะเหยียบเมืองบริสุทธิ์เป็นเวลาสี่สิบสองเดือน' is entirely untouched; no theological meaning changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_12_optimal_001 -->
### Revelation 12:14

**Current:**

> นางจะถูกเลี้ยงดูที่นั่น

**Proposed:**

> นางจะได้รับการเลี้ยงดูที่นั่น

**Why:** Thai ถูก- is the adversative/negative passive morpheme reserved for actions that are unwanted or harmful to the subject (ถูกตี, ถูกจับ, ถูกปรับ); using it here frames the wilderness nourishing — an explicit act of divine protection and provision — as something afflictive, which is the opposite of the Greek's sense. For benefactive or neutral passives, Thai natively uses ได้รับการ- (received / was given), making ได้รับการเลี้ยงดู the register-correct rendering of τρέφεται. This instinct is already present in the corpus: the cognate active form (τρέφωσιν) at v.6 is rendered with the benevolent framing เพื่อพวกเขาจะเลี้ยงดูนาง; the proposed change aligns v.14 with that same pastoral tone. The Greek passive voice (τρέφεται) is fully preserved — only the Thai passive morpheme shifts from negative (ถูก-) to benefactive (ได้รับการ-) — so no locked term is disturbed and no theological content changes.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_14_optimal_003 -->
### Revelation 14:16

**Current:**

> และแผ่นดินโลกก็ถูกเก็บเกี่ยว

**Proposed:**

> และพระองค์ทรงเก็บเกี่ยวแผ่นดินโลก

**Why:** The Greek aorist passive ἐθερίσθη is rendered with a ถูก-passive, but the agent พระองค์ผู้ประทับบนเมฆ (the one sitting on the cloud) was named explicitly in the immediately preceding clause of the same verse. In Thai narrative, when the referential agent is this proximate, the active construction with a pronominal subject is the natural discourse-consecutive form; พระองค์ทรงเก็บเกี่ยวแผ่นดินโลก flows naturally as a parallel active pair after พระองค์...ทรงเหวี่ยงเคียว, and ทรง- correctly marks the divine Christological agent per corpus ราชาศัพท์ conventions. Deferred to native reviewer because the Greek agentless passive may be rhetorically deliberate — echoing the divine-passive of Isa 63 where the warrior-God's agency in the harvest-judgment is left intentionally implicit — a subtlety that a Tier-A Thai reviewer should weigh.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_18_optimal_002 -->
### Revelation 18:17

**Current:**

> ความมั่งคั่งมากมายเช่นนี้ก็ถูกทำให้รกร้างไป

**Proposed:**

> ความมั่งคั่งมากมายเช่นนี้ก็กลายเป็นที่รกร้างไป

**Why:** ἠρημώθη ('was made desolate') is rendered with the stacked ถูก + causative ทำให้ + adjective chain 'ถูกทำให้รกร้าง,' a translationese passive pattern heavier than natural Thai requires. Thai natively expresses a transformative state of becoming with กลายเป็น, so 'กลายเป็นที่รกร้างไป' preserves the full desolation image of ἐρημόω — the city that was teeming is now waste — without the periphrastic double-layer. Divine agency as cause is already established by v.8; it need not be foregrounded here via the passive frame. No theological content is altered, and the proposal must be applied together with v.19 for the three-refrain pattern (vv.10, 17, 19) to remain parallel. Routing to native reviewer to confirm กลายเป็นที่รกร้าง lands naturally at evangelical-formal register.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---

<!-- POLISH_PROPOSAL id=revelation_18_optimal_003 -->
### Revelation 18:19

**Current:**

> นางก็ถูกทำให้รกร้างไป

**Proposed:**

> นางก็กลายเป็นที่รกร้างไป

**Why:** Identical verb and identical heavy ถูก+ทำให้+adj construction as v.17. 'นางก็กลายเป็นที่รกร้างไป' expresses Babylon's desolation naturally with กลายเป็น while preserving ἐρημόω's waste-land image in full. The mariners' woe-cry refrain (vv.10, 17, 19 one-hour formula) will be internally consistent only if both v.17 and v.19 are normalized together; either change alone creates an intra-chapter inconsistency. All KD1-locked (dust-on-heads gesture) and KD2-locked (shipper-wealth phrase) terms remain verbatim. No theological change.

**Decision:** pending

<!-- /POLISH_PROPOSAL -->

---
