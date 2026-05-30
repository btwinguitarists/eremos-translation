# Job — End-of-Book Review

**Date:** 2026-05-30
**Scope:** All 42 chapters of Job (`output/translations/job_01.json` … `job_42.json`); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** JOB 42 shipped (commit `163b26e3`); per `docs/END_OF_BOOK_CHECKLIST.md` §2 + §3, fired by `scripts/detect_book_complete.py`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — **no translation changes made**.

## Summary

- **16 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 42/42 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (38 locks, 0 violations across 22,024 verses); `audit_inclusion_variants.py --book job --strict` exits 0 (**0 candidates** — Job carries no SBLGNT/LXX inclusion variants). `git status output/` clean except a pre-existing single-chapter-scoped regen of `divine_names.md` (not a Job source change; left untouched, out of this branch).
- **9 items LOCKED** — compliant with an existing `translator_decisions/` doc (divine-name family, goel, sons-of-God, Adonai-28:28, nicham, qere/ketiv handling, register, inclusion-variants below-floor).
- **5 items STABLE-but-undocumented** at corpus level (mediator/arbiter thread; barak/curse euphemism; Sheol/Abaddon underworld vocabulary; Behemoth/Leviathan transliteration; the divine-name *architecture* itself) — verse-level rationale is sound; doc-lift recommended for the two that compound forward.
- **5 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation).
- **1 item flagged DECIDE** (the `הַשָּׂטָן` → ซาตาน rendering — the article-marked council role flattened to the proper name; undocumented; forward-compounds to Zech 3 + Ps 109:6).
- **External AI review (§3) packet prepared** from the REVIEW/DECIDE items (see `external_review_items_JOB.md`).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging `book-job-v1`.

---

## 1. Divine-name *architecture* (YHWH-frame vs. El/Eloah/Shaddai-dialogue) — **STABLE (strength; preserved as Hebrew-form transparency)**

Job's signature literary feature is its divine-name distribution: the Tetragrammaton `יהוה` is almost entirely confined to the **prose frame** (prologue chs. 1–2; epilogue ch. 42) and the **divine-speech headers** (38, 40), while the **poetic dialogue** (chs. 3–37) overwhelmingly uses `אֵל` / `אֱלוֹהַּ` (Eloah) / `שַׁדַּי` (Shaddai). The shipped corpus reproduces this exactly:

| Zone | YHWH (`יהוה`) occurrences | Dialogue names |
|---|---|---|
| Prologue (ch. 1–2) | 18 | — |
| Dialogue (ch. 3–37) | **1** (only 12:9) | Eloah ×41, Shaddai ×31, El frequent |
| Divine speeches (ch. 38, 40) | 4 | — |
| Epilogue (ch. 42) | 9 | — |

The lone dialogue YHWH at **12:9** (a long-noted textual curiosity — many witnesses read Eloah; widely held to echo Isa 41:20) is explicitly flagged in `output/textual_variants/job_12.json`: *"ข้อ 12:9 เป็นการปรากฏของ יהוה เพียงแห่งเดียวในบทกวีโต้วาทีของโยบ."* The 38:1 `key_decision` likewise names the architecture: *"เป็นการกลับมาของพระนาม יהוה ในบทกวี (38-42) หลังจากใช้ אֵל/אֱלוֹהַּ/שַׁדַּי ตลอดบทโต้วาที."*

Because the Thai collapses YHWH / Eloah / Shaddai / El into the `องค์พระผู้เป็นเจ้า` / `พระเจ้า` / `ผู้ทรงมหิทธิฤทธิ์` family (per `divine_names_table_2026-05.md`), the *vocabulary distinction* the Hebrew author exploits is not visible on the Thai surface — but it is preserved as **Hebrew-form transparency** in the per-verse `key_decisions`, exactly as the divine-names doc's Layer-1 mechanism prescribes. This is the intended behavior and is handled with unusual care. **No action — STABLE strength.**

---

## 2. YHWH → องค์พระผู้เป็นเจ้า + first-occurrence footnotes — **LOCKED** (`divine_names_table_2026-05.md`)

All 32 `יהוה` occurrences render `องค์พระผู้เป็นเจ้า`. Per-chapter first-occurrence Tier-2 footnotes present in `output/textual_variants/` for the YHWH-bearing chapters (job_01, _02, _12, _38, _40, _42). Vocative (`ข้าแต่องค์พระผู้เป็นเจ้า`) and `key_decisions` Hebrew-form records all conform. **LOCKED.**

---

## 3. El / Eloah → พระเจ้า — **LOCKED** (`divine_names_table_2026-05.md` rows 26–27)

`אֱלוֹהַּ` (Eloah, 41×; the divine-names doc already anticipates "Job-frequent ~41×") and standalone `אֵל` both render **พระเจ้า**, uniform across the dialogue. Spot-checks (6:14, 16:21, 19:26, 27:2 etc.) all conform. **LOCKED.**

---

## 4. Shaddai → ผู้ทรงมหิทธิฤทธิ์ — **LOCKED**, but **องค์-prefix within-book drift — REVIEW**

All 31 real `שַׁדַּי` occurrences render the locked lexeme **ผู้ทรงมหิทธิฤทธิ์** (`divine_names_table_2026-05.md` row 29). Compliant. **However**, the standalone-title form drifts by chapter:

- **Bare `ผู้ทรงมหิทธิฤทธิ์`** — 5:17, 6:4, 6:14, 8:3, 8:5, 11:7 (the six earliest occurrences, chs. 5–11)
- **`องค์ผู้ทรงมหิทธิฤทธิ์`** (with the honorific classifier `องค์-`) — all 25 occurrences from 13:3 onward (13, 15, 21, 22, 23, 24, 27, 29, 31, 32, 33, 34, 35, 37, 40)

Both are correct Thai; `องค์-` reads more naturally as a standalone divine title. But the divine-names table locks the bare form `ผู้ทรงมหิทธิฤทธิ์`, and the split is a chapter-progression drift (bare 5–11, `องค์-` 13+), not a positional/grammatical distinction (8:3 is bare-as-subject; 21:15 is `องค์-`-as-subject). **REVIEW: normalize to the dominant `องค์ผู้ทรงมหิทธิฤทธิ์` (25/31) and update the divine-names-table row to record `องค์ผู้ทรงมหิทธิฤทธิ์` as the standalone-title form, OR normalize the six early occurrences to add `องค์-`.** Recommend the former (document `องค์-` as the standalone-title form; bare form retained only inside `ของ`-genitive constructions if a principle is wanted). Compounds forward into Ruth 1:20–21 (Naomi's Shaddai pun), Gen-patriarchal Shaddai, Isa 13:6, Joel 1:15, Ezek 1:24.

---

## 5. `הַשָּׂטָן` → ซาตาน — **DECIDE before tagging**

`הַשָּׂטָן` appears 11× in the prologue (1:6, 1:7, 1:8, 1:9, 1:12 [×2], 2:1, 2:2, 2:3, 2:4, 2:6, 2:7), **always with the definite article** — i.e., a **title/role** ("*the* accuser / *the* adversary," a function in the divine council), not yet the proper personal name "Satan" of later Second-Temple and NT theology. The shipped rendering is the proper name **ซาตาน** at every occurrence. The 1:6 `key_decision`/`notes` correctly *identify* the issue — *"הַשָּׂטָן มีคำนำหน้านามชี้เฉพาะ (‘ผู้กล่าวหา’) เป็นบทบาทในที่ประชุมสวรรค์"* — then render the proper name anyway *"ตามสำนวนพระคัมภีร์ที่รู้จัก"* (by familiar biblical convention).

**Why this is a DECIDE, not just a note:**
1. **The Hebrew article carries the role meaning that the Thai surface erases.** A Thai reader sees the proper-name antagonist of NT theology; the Hebrew presents a prosecutorial office-holder in YHWH's court. Modern scholarly translations diverge sharply here (NRSV "Satan" + footnote "the Accuser"; CEB / NABRE "the Adversary" / "the satan"; ESV/NIV keep "Satan"). The evangelical-conventional choice is defensible but interpretively committed.
2. **It is undocumented at corpus level.** No `translator_decisions/` doc governs the satan/accuser rendering (only an incidental mention in `synoptic_parallel_passages_2026-05.md`, NT context).
3. **It is already a de-facto corpus convention — but unflagged.** `1 Chronicles 21:1` (shipped) renders the *article-less* `שָׂטָן` ("an adversary stood up against Israel") as **ซาตาน** too, and the 1CH audit did not flag it. So the corpus has flattened *both* the article-marked council-role (Job) *and* the article-less form (1 Chr) to the same proper name — a coherent convention, but one made by default rather than by decision.
4. **It compounds forward.** `Zechariah 3:1–2` (הַשָּׂטָן, article-marked, the cleanest "the accuser" courtroom scene) and `Psalm 109:6` (שָׂטָן at the accused's right hand) are the next occurrences. Locking this now prevents drift.

**Ben to decide:** (a) keep **ซาตาน** corpus-wide (recommend a 1-line doc + a Layer-2 interpretive footnote at Job 1:6 explaining the article-marked "ผู้กล่าวหา" role, parallel to the sons-of-God crux footnote); or (b) render the article-marked role as **ผู้กล่าวหา** ("the accuser") in Job + Zech, reserving ซาตาน for article-less/NT uses. Recommend (a) — preserves corpus consistency with 1 Chr 21:1 while giving the scholar the role-nuance via footnote. Either way, **write `docs/translator_decisions/ha_satan_accuser_2026-05.md`** to lock the choice before Zechariah ships.

---

## 6. `בְּנֵי הָאֱלֹהִים` "sons of God" → บุตรของพระเจ้า — **LOCKED** (`spiritual_beings_hierarchy_2026-05.md` §71–87)

1:6, 2:1, 38:7 all render **(บรรดา)บุตรของพระเจ้า** — literal-preservation per the doc's surface-text policy (do NOT collapse to ทูตสวรรค์ / เชื้อสายของเซธ). The 1:6 `key_decision` cites `spiritual_beings_hierarchy`. Compliant. **Minor note:** the doc mandates the Layer-2 interpretive-crux footnote only at Gen 6:2/6:4; the Job parallels are cited there as cross-references. Optional: a one-line cross-reference footnote at Job 1:6 would help a reader who arrives at Job first, but it is **not owed**. **LOCKED.**

---

## 7. `גֹּאֵל` "my Redeemer" (19:25) → พระผู้ไถ่ของข้าพระองค์ — **LOCKED** (`goel_kinsman_redeemer_2026-05.md` §5)

19:25 ships **ส่วนข้าพระองค์ ข้าพระองค์รู้ว่าพระผู้ไถ่ของข้าพระองค์ทรงพระชนม์อยู่** — character-for-character the doc's locked form. The divine register (royal `พระ-` + `ทรงพระชนม์` / `ทรงยืน`) deliberately encodes the Christological-typological reading and preserves the single-root identity with Ruth's `ญาติผู้ไถ่` (Boaz) → Isa 43/53. Compliant. **Housekeeping:** the goel doc's "Corpus-verified shipped forms" table still lists `พระผู้ไถ่` as **"0 — forward-lock for Job 19:25 … not yet shipped."** Job has now shipped it; per `docs/CORPUS_VERIFICATION_WORKFLOW.md` the doc's verification table should be refreshed to "1 (Job 19:25)" at tag time. **LOCKED (doc table needs a one-line refresh).**

---

## 8. The mediator / arbiter / witness thread (9:33; 16:19–21; 33:23–24) — **STABLE-undocumented + messianic-marking asymmetry vs. 19:25 — REVIEW**

Job's distinctive theological cry for an intermediary between man and God runs as a coherent thread, rendered consistently and with cross-referencing `key_decisions`:

| Verse | Hebrew | Thai | Register |
|---|---|---|---|
| 9:33 | `מוֹכִיחַ` (umpire/arbiter) | **คนกลาง** | plain |
| 16:19 | `עֵד` / `שָׂהֵד` (witness in heaven) | **พยาน / ผู้รับรอง** | plain |
| 16:21 | arbiter "between man and God" | **วิงวอนต่อพระเจ้า** (periphrastic) | plain |
| 33:23–24 | `מַלְאָךְ מֵלִיץ` (mediating angel) + `כֹּפֶר` (ransom) | **ทูตสวรรค์ … คนกลาง … ค่าไถ่** | plain |

The 9:33 `key_decision` explicitly cross-references **1 Tim 2:5** ("one mediator between God and men"); 16:19's KD cross-references 19:25 ("เทียบ ‘ผู้ไถ่’ 19:25"). The thread is principled and well-glossed at verse level — **STABLE** — but it is **not consolidated in any corpus doc**, and it carries a genuine editorial tension worth Ben's eye:

**The messianic-marking asymmetry.** 19:25's `גֹּאֵל` is marked **divine/royal** (พระผู้ไถ่ + ทรง-), committing to the Christological reading. But 9:33 / 16:19 / 33:23 — the *same* longing-for-an-intermediary thread, which Christian tradition reads as the *same* Christ-foreshadowing — are rendered **plain human register** (คนกลาง / พยาน / ทูตสวรรค์, no royal marking). Is the asymmetry principled (19:25 alone is a confession of certainty — "I *know* my Redeemer *lives*"; 9:33's arbiter is explicitly *absent* — "there is no umpire between us"), or is it an inconsistency in how far the translation pre-loads the mediator thread with messianic register? **REVIEW: confirm the asymmetry is intentional** (recommend: yes — keep 9:33/16:19/33:23 plain, since marking a *hypothesized/absent* arbiter as divine would over-read the Hebrew, whereas 19:25 is a positive confession), **and recommend a short `translator_decisions/job_mediator_arbiter_thread_2026-05.md`** tying 9:33 → 16:19–21 → 19:25 → 33:23–24 together with the register principle, since the thread is Job-distinctive and the 1 Tim 2:5 / Heb cross-references make it a perennial reviewer touchpoint.

---

## 9. `אֲדֹנָי` standalone (28:28) → องค์เจ้านาย — **LOCKED** (`divine_names_table_2026-05.md`, 4-way Adonai sub-rule)

28:28 is the **only** standalone `אֲדֹנָי` in Job (MT `יִרְאַת אֲדֹנָי`, "the fear of the Lord is wisdom"). Third-person title, not a prayer-vocative → **องค์เจ้านาย** per the 2026-05-18 4-way sub-rule (third-person reference row). The `key_decision` and the `job_28` note both record that MT reads `אֲדֹנָי` here, not `יהוה`. Compliant. **LOCKED.**

---

## 10. `נִחַם` (42:6) → กลับใจ — **LOCKED** (`nicham_divine_relenting_2026-05.md`)

42:6 (`אֶמְאַס וְנִחַמְתִּי`, Job's response from the whirlwind) renders **ข้าพระองค์จึงเกลียดตนเอง และกลับใจ** — *human* repentance (กลับใจ/สำนึกผิด), correctly distinguished from *divine* relenting per the doc; the KD names the distinction explicitly. (Note: 42:6 `אֶמְאַס` is itself objectless in Hebrew and a known crux — the rendering supplies "ตนเอง" / "myself," the mainstream reading matching most English versions. Defensible; no action.) **LOCKED.**

---

## 11. Behemoth / Leviathan → เบเฮโมท / เลวีอาธาน — **STABLE (transliteration; principled)**

`בְּהֵמוֹת` (40:15) → **เบเฮโมท** and `לִוְיָתָן` (3:8, 40:25 [MT]) → **เลวีอาธาน**, both transliterated with `key_decisions` glossing them as primeval/chaos creatures (rather than domesticating to "ฮิปโป" / "จระเข้"). Consistent with the proper-noun/transliteration policy and the right call for these mythopoetic names. **STABLE — no doc owed** (covered by general transliteration policy); worth a one-line mention in `proper_names_and_transliteration_2026-05.md` if a canonical list is maintained.

---

## 12. Sheol / Abaddon / the Pit underworld vocabulary — **STABLE (uniform)**

`שְׁאוֹל` (Sheol) → **แดนคนตาย** uniformly (7:9, 11:8, 14:13, 17:13, 21:13, 24:19, 26:6); `אֲבַדּוֹן` (Abaddon) → **แดนพินาศ** (26:6, 28:22, 31:12, with a transliteration gloss "อาบัดโดน" at 31:12); `שַׁחַת` (the Pit) → **หลุมมรณา** (33:24). Principled and consistent. **STABLE** — consider folding into an OT-wide underworld-vocabulary note when Psalms/Proverbs ship (Sheol density spikes there).

---

## 13. The `בָּרַךְ` "bless"/curse euphemism (1:5, 1:11, 2:5, 2:9) — **STABLE (recommend small doc)**

Four prologue verses use `בֵּרֵךְ`/`בָּרֵךְ` ("bless") as the scribal **euphemism for "curse" God** (the antiphrastic *tiqqun*-style usage). All four render the *meaning* **แช่งด่า** ("curse"), with each `key_decision` explicitly naming the euphemism: *"בֵּרֵךְ แท้จริงแปลว่า ‘อวยพร’ แต่ในที่นี้เป็นสำนวนเลี่ยง (euphemism) … → แปลตามความหมายว่า ‘แช่งด่า.’"* This is the mainstream scholarly approach (matches all major English versions) and is well-documented at verse level. **STABLE.** **Recommend `docs/translator_decisions/barak_curse_euphemism_2026-05.md`** because the device recurs at **1 Kgs 21:10, 21:13** (Naboth — "you have *blessed* God and the king"), **Ps 10:3**, and is a known reviewer flag ("why does your Job say *curse* when the Hebrew says *bless*?"). A small lock + the four Job anchors would settle it before Kings-revisits and Psalms.

---

## 14. Textual cruxes (13:15 qere/ketiv; 23:2 MT-departure; 24:18–24, 30:18 hard-text) — **REVIEW (footer disposition + §2.3-floor affirmation)**

Job is the OT's most textually difficult book; the translation handles its cruxes at `key_decisions`/`notes` level, following MT-or-BSB and recording the choice:

- **13:15** — the famous `כְּתִיב לֹא` ("I have *no* hope") vs. `קְרֵי לוֹ` ("yet will I hope *in him*"). Follows the **qere** (= BSB; the faith-reading). Note present. ✓ The single most reader-visible crux in Job.
- **23:2** — MT `יָדִי` ("*my* hand") vs. ancient versions + BSB `יָדוֹ` ("*his* [God's] hand is heavy"). **Follows BSB against MT** — an exception-(1)-type departure (`ot_canon_and_text_base_2026-05.md` §104). Recorded in the verse `notes` only.
- **24:18–24, 30:18** — notoriously corrupt Hebrew; notes flag "ตีความยาก … แปลตาม MT/BSB."

Under `mt_vs_lxx_textual_variant_handling_2026-05.md` **§2.3 disclosure-threshold floor**, routine minor cruxes need **no** Tier-2 reader-facing footer — surface = the chosen reading, silent, per RULES §5. Most of Job's cruxes sit below that floor. **But two questions for Ben:**

1. **Does 13:15 rise above the floor?** It is *canonically visible* and *materially reader-affecting* — the ketiv/qere difference is the gap between despair ("I have no hope") and the book's most-quoted confession of faith ("though he slay me, yet will I hope in him"). A Thai reader comparing against THSV (which also follows qere) won't be surprised, but the §2.3 criteria ("materially reader-affecting") are arguably met. **Recommend a Tier-2 footer at 13:15** (`output/textual_variants/job_13.json`) noting the ketiv reading — it is the one Job crux worth surfacing.
2. **Is the 23:2 BSB-over-MT departure adequately dispositioned?** Per `ot_canon` §113, exception-(1) departures take "key_decisions + a [Tier 2] verse-level footer note … when the divergence is theologically significant." 23:2 is *not* theologically significant (Job's groaning is heavy / God's hand is heavy), so a footer is likely **not** owed — but confirm the verse-note disposition is the intended floor treatment, and that the audit may **affirmatively state** "all other Job MT/LXX/MT-internal divergences are below the §2.3 disclosure floor; no footers required" (per the 2 Kings precedent). **REVIEW.**

---

## 15. Versification map — MT 40:25–41:34 zone under-registered — **REVIEW (mechanical)**

Job's Behemoth/Leviathan section diverges in chapter/verse numbering: **MT Job 40:25–32 = English/BSB 41:1–8**, and **MT 41:1–26 = English 41:9–34**. The translation correctly uses **MT numbering** (notes at 40:25 + 41:1 explain the divergence to the reader). However, `data/versification_map.json` contains **only one** Job entry — `JOB-41-1` (with a prose note describing the whole zone). The per-verse mappings for **MT 40:25–32** and **MT 41:2–26** are **not individually registered.**

This matches the recurring gap pattern flagged in the Daniel audit ("3 MT/Eng zones unregistered") and the known ship-script gotcha (`ship_chapter.sh` does not stage `versification_map.json`; map edits are committed manually). **REVIEW: backfill the per-verse Job 40:25–32 + 41:2–26 entries into `data/versification_map.json` before tagging**, so downstream cross-reference / USFM export resolves Job 41 correctly against English-numbered references. Low risk to the text; matters for tooling + reader cross-referencing.

---

## 16. Inherited locks, register, and proper nouns — **all compliant (LOCKED)**

| Item | JOB evidence | Status |
|---|---|---|
| `narrator_vs_character_voice` / honorifics | Divine speech (38–41) full royal register (`ตรัส`, `ราชาศัพท์`, `เรา`); Elihu (32–37) and the three friends kept in **human register** (`ความโกรธ` not `พระพิโรธ` at 32:2); narrator royal-marks God, plain for humans. 42:7 God names Job `ผู้รับใช้ของเรา`. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar` | God's "hand" in satan's challenge (1:11, 2:5) → `พระหัตถ์` (royal); creaturely body-parts plain (38:3 `เอว`, 40:15). | **LOCKED** |
| `proper_names_and_transliteration` | Friends + places uniform: เอลีฟัส (6×), บิลดัด (5×), โศฟาร์ (4×), เอลีฮู (7×), เทมาน, ชูอาห์, นาอามาห์, บูซ, อูส (1:1); daughters เยมีมาห์ / เคเรนหัปปุค (42:14). No spelling drift. | **LOCKED** |
| `inclusion_variants_absent_verses` / `audit_inclusion_variants` | **0 candidates** — Job has no SBLGNT/LXX inclusion variants; nothing owed. | **LOCKED (N/A)** |
| `mt_vs_lxx_textual_variant_handling` §2.3 | All Job MT/LXX divergences below the disclosure floor except the 13:15 question (§14). | **LOCKED-with-§14-review** |
| `spirit_of_yhwh_empowerment` / `psyche_vs_pneuma` | 32:8, 33:4 `רוּחַ`/`נְשָׁמָה` ("breath/spirit of Shaddai gives understanding/life") → `วิญญาณ`/`ลมปราณ` — anthropological, not the empowerment-Spirit formula; correct. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 42/42 chapters: `output/check_reports/job_NN_review.md` + `output/back_translations/job_NN.json` ✓
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** ✓
- `check_phrase_consistency.py`: **0 violations / 38 locks / 22,024 verses** ✓
- `audit_inclusion_variants.py --book job --strict`: **exit 0, 0 candidates** ✓
- `git status output/`: clean except a pre-existing single-chapter regen of `output/check_reports/divine_names.md` (present in the start-of-session snapshot; **not** a Job source change — left untouched and excluded from this audit branch).

---

## Flagged for Ben's attention

### DECIDE (blocks `book-job-v1` tag)
- **§5 — `הַשָּׂטָן` → ซาตาน.** Article-marked council role ("the accuser") flattened to the proper name; undocumented; consistent with shipped 1 Chr 21:1 but unflagged; forward-compounds to Zech 3 + Ps 109:6. Recommend: keep ซาตาน + add a Layer-2 footnote at Job 1:6 + write `ha_satan_accuser_2026-05.md`.

### REVIEW (confirm; non-blocking but recommended before tag)
- **§4 — Shaddai `องค์-` prefix drift** (bare in chs. 5–11, `องค์ผู้ทรงมหิทธิฤทธิ์` from 13 on). Normalize + update divine-names-table row.
- **§8 — mediator/arbiter thread messianic-marking asymmetry** (19:25 divine-marked vs. 9:33/16:19/33:23 plain). Confirm intentional; recommend a short thread doc.
- **§14 — textual-crux footer disposition** (esp. 13:15 ketiv/qere — recommend a Tier-2 footer; confirm 23:2 BSB-over-MT floor treatment + affirm §2.3 floor for the rest).
- **§15 — versification map** backfill for MT 40:25–32 + 41:2–26.

### STABLE — recommended new docs (housekeeping; not blocking)
1. `docs/translator_decisions/ha_satan_accuser_2026-05.md` (§5 — also the DECIDE resolution)
2. `docs/translator_decisions/job_mediator_arbiter_thread_2026-05.md` (§8)
3. `docs/translator_decisions/barak_curse_euphemism_2026-05.md` (§13)
- Refresh the `goel_kinsman_redeemer_2026-05.md` corpus-verified table (§7 — Job 19:25 now shipped).

---

## Recommendation

**Job ships in excellent corpus-hygiene shape** — arguably the cleanest mechanical state of any poetic OT book so far (0 inclusion-variant candidates, 0 consistency violations, sophisticated handling of the divine-name architecture and the 12:9 anomaly). The editorial gaps are doc-lift, not translation defects: every flagged item is either a documented-at-verse-level decision awaiting corpus consolidation, or a single genuine DECIDE (the satan/accuser rendering) that needs Ben's call before a doc can lock it.

Tag `book-job-v1` after:
1. Ben's decision on §5 (`הַשָּׂטָן`) — the one DECIDE.
2. Ben's confirmation on §4, §8, §14, §15 (REVIEW).
3. Any spot-revisions executed (Shaddai `องค์-` normalization; 13:15 footer; versification backfill) + checks re-run clean.
4. External AI sanity-check (§3 — packet prepared from the four lead items).
5. Recommended docs written (`ha_satan_accuser`, `job_mediator_arbiter_thread`, `barak_curse_euphemism`) + goel-table refresh.
