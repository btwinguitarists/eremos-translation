# מַלְאָךְ / מַלְאַךְ יהוה — Corpus-wide rendering lock

**Scope:** OT instances of the Hebrew lemma מַלְאָךְ ("messenger / angel") in supernatural / divine-messenger contexts, including the compound מַלְאַךְ יהוה ("angel of YHWH") and the suffixed forms מַלְאָכִי ("my angel"), מַלְאַךְ הָאֱלֹהִים ("angel of God"), etc. This doc locks the Thai surface so the single Hebrew lemma reads as the single Greek-NT lemma ἄγγελος → ทูตสวรรค์ across the entire bilingual corpus.

**Decided:** 2026-05-13 (Ben + ChatGPT + Gemini + Claude tri-AI review of Exodus end-of-book audit). Triggered by Exodus 6-verse split across four different Thai phrasings.

**Companion docs:** `divine_names_table_2026-05.md`, `spiritual_beings_hierarchy_2026-05.md` (if exists), `hebrew_idioms_and_metaphor_2026-05.md`.

---

## 1. The lock

**Hebrew lemma** מַלְאָךְ in any divine-messenger context → **ทูตสวรรค์** (literally "heaven-messenger").

The genitive / possessive qualifier carries the variant: "of YHWH", "of God", "my (= YHWH's)", standalone. The qualifier is rendered with Thai ของ + the established divine-name form, NOT by varying the head-noun ทูตสวรรค์.

| Hebrew | Thai (locked) |
|---|---|
| מַלְאַךְ יהוה | ทูตสวรรค์ขององค์พระผู้เป็นเจ้า |
| מַלְאַךְ הָאֱלֹהִים | ทูตสวรรค์ของพระเจ้า |
| מַלְאָכִי (YHWH-speech, "my angel") | ทูตสวรรค์ของเรา |
| מַלְאָךְ (standalone, divine-messenger context) | ทูตสวรรค์ |

For purely human messengers in non-supernatural narrative (e.g., kings' envoys in Judg / 1 Sam / 1 Kings), use the plain register ผู้ส่งสาร or ทูต as context requires; that is outside this lock.

---

## 2. Why a corpus-wide lock

### 2.1 The Hebrew is uniform; the Greek NT is uniform

The Hebrew מַלְאָךְ is the same word in every divine-messenger occurrence — Exod 3:2's burning-bush "angel of YHWH", Gen 16's "angel of YHWH" to Hagar, Judg 13's "angel of YHWH" to Manoah, Zech's "angel of YHWH" in night visions. The qualifier varies; the head-noun does not.

The NT echoes this uniformity: ἄγγελος is the consistent rendering for divine messengers (Luke 1:11, 2:9-15; Acts 7:30 — explicitly quoting Exod 3:2 as ἄγγελος; Heb 1:14; the whole of Revelation). The Eremos NT corpus already locks ἄγγελος → ทูตสวรรค์.

If the OT Thai diverges into ทูตของ / ทูต / ทูตสวรรค์ depending on translator-feel, the OT-NT lemma-thread breaks at the most theologically loaded thread in the Bible.

### 2.2 The Christophany / pre-incarnate-Christ question

The "angel of YHWH" at the burning bush (Exod 3:2), at Gen 16/22, at Judg 6/13, is read in classical Christian tradition (Justin Martyr; Calvin; much of Reformed theology) as a pre-incarnate appearance of the Son. This is a theological reading layered onto the text — it is **not** a Hebrew lexical distinction.

The Hebrew offers no surface marker that says "this one is divine in a distinctive way." Acts 7:30 (Stephen's speech), citing Exod 3:2, uses the plain ἄγγελος — the same word the NT uses for any other angel. The church fathers and Reformers who read the Christophany made that read in *Greek*, with the same single word.

**Decision:** The Thai surface should NOT carve a separate lexical category for "angel-of-YHWH" vs. "regular angel." All divine מַלְאָךְ → ทูตสวรรค์. Where the theophanic complexity merits explanation, the verse-level Layer-2 footnote carries it (e.g., Exod 3:2; Gen 16:13; Judg 6:22-23; Judg 13:22).

### 2.3 The shipped Exodus drift

As of end-of-book audit 2026-05-13, Exodus 6 occurrences shipped as four different Thai phrasings:

| Verse | Hebrew | Shipped Thai (pre-fix) | Fixed (this doc) |
|---|---|---|---|
| 3:2 | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | ทูตสวรรค์ขององค์พระผู้เป็นเจ้า |
| 14:19 | מַלְאַךְ הָאֱלֹהִים | ทูตของพระเจ้า | ทูตสวรรค์ของพระเจ้า |
| 23:20 | מַלְאָךְ | ทูตสวรรค์ | ทูตสวรรค์ ✓ already correct |
| 23:23 | מַלְאָכִי | ทูตสวรรค์ของเรา | ทูตสวรรค์ของเรา ✓ already correct |
| 32:34 | מַלְאָכִי | ทูตของเรา | ทูตสวรรค์ของเรา |
| 33:2 | מַלְאָךְ | ทูตสวรรค์ | ทูตสวรรค์ ✓ already correct |

Normalized in commit landing this doc.

---

## 3. Implementation checklist

- [x] Exodus 3:2, 14:19, 32:34 normalized to ทูตสวรรค์ form (verified 2026-05-13).
- [~] **Lemma-binding check added (Kings-scoped) 2026-05-24; widened to Chronicles 2026-05-26** — `check_phrase_consistency.py` carries a `malak` lock (`hebrew_patterns` `מלאך\s*יהוה` / `מלאך\s*ה?אלהים` → expected `ทูตสวรรค์`), now `"books": ["1KI ", "2KI ", "1CH ", "2CH "]` (widened per 1 Chronicles EOB external review — ChatGPT + Gemini both CONCERN on "passed by convention, not enforcement"). The patterns key on `מלאך`+divine-name, so genealogies and human messengers (bare `מלאך`/`מלאכים`) never match — widening is false-positive-safe. Verified clean 2026-05-26: 1CH coverage = 21:12, 21:15, 21:16, 21:18, 21:30 all OK on `ทูตสวรรค์`. **Still widen corpus-wide (Gen/Judg/Sam/Zech) during the full-OT scan** (deferred backlog below).
- [ ] Forward-cover: Gen 16, 22 (Hagar + Abraham theophanies); Num 22 (Balaam's donkey); Judg 6 (Gideon), 13 (Samson's parents); 2 Sam 24 (David); **1 Chr 21 (David's census — the direct 2 Sam 24 synoptic parallel) — ✓ done + machine-enforced 2026-05-26** (21:12/15/16/18/30 all ship `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`; 1CH 21 is the checked-clean standard the deferred 2 Sam 24 retrofit should match); **1 Kings 19 (Elijah at Horeb) — ✓ done 2026-05-24** (19:5 `ทูตสวรรค์`, 19:7 `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`, 13:18 comply; 19:7 was the EOB-audit drift fix); 2 Kings 1 (Elijah + Ahaziah's messengers) — **✓ done 2026-05-25** (divine: 1:3, 1:15 ship `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`; human: 1:2, 1:3, 1:16 ship `ผู้ส่งสาร` per §4.4 hierarchy); Zech 1-6 (the angel-of-YHWH cycle); Mal — the book whose Hebrew title IS מַלְאָכִי.
- [ ] **⚠️ DEFERRED to a future full-OT scan — cross-book malak retrofit (Ben's decision 2026-05-24; do NOT forget):** older books were shipped before this lock and still render the divine messenger as bare `ทูต`. A 2026-05-24 corpus-wide run of the new `malak` lock (before it was scoped to Kings) flagged:
  - **Clear theophanies → retrofit to `ทูตสวรรค์`:** Genesis 16:7, 16:9, 16:10, 16:11, 21:17, 31:11.
  - **"like an angel of God" similes → review (may legitimately keep a plainer form):** 1 Samuel 29:9; 2 Samuel 14:17, 14:20, 19:28.
  - **Also re-check** the forward-cover list above (Gen 22, Num 22, Judg 6/13, 2 Sam 24) — the Kings-scoped run did not cover them.
  - **Method:** temporarily remove `"books"` from the `malak` lock in `check_phrase_consistency.py`, run it to regenerate the full flagged list, retrofit each, then widen the lock's permanent scope. **Not a 1 Kings tag blocker.**
- [ ] **⚠️ DEFERRED — human-messenger surface normalization (added 2026-05-25, 2 Kings EOB Item E):** the *human* מַלְאָךְ side (§4.4) drifted to `ผู้สื่อสาร` / `ผู้ส่งข่าว` in books shipped before the §4.4 hierarchy. Normalize toward the hierarchy (`ผู้ส่งสาร` default; `ทูต`/`คณะทูต` for diplomatic) in a cross-book pass, **per-verse** (do not blanket-replace — weigh royal-to-royal contexts for `ทูต`). Known queue in 2 Kings: `ผู้สื่อสาร` at 5:10, 6:32–33, 9:18, 10:8, 14:8, 19:9, 19:14 (2 Kings 1:2–3,16 + 19:23 already on `ผู้ส่งสาร`). Sweep other OT books for `ผู้สื่อสาร`/`ผู้ส่งข่าว` at the same time. **Not a 2 Kings tag blocker** (REVIEW item; MT-faithful either way).
- [ ] Layer-2 footnote template for Christophanic candidates (Exod 3:2, Gen 16/22, Judg 6/13): a short survey of the theophanic reading, anchored to the verse's narrative ambiguity without re-categorizing the Thai surface.

---

## 4. Edge cases

### 4.1 מַלְאָךְ + divine-name compound vs. standalone

If מַלְאָךְ is followed by a divine name (YHWH / Elohim), include the divine name in the Thai with ของ. If standalone (e.g., Exod 23:20 "I send a messenger"), use ทูตสวรรค์ without qualifier — narrative context (within YHWH speech) makes the divine source clear.

### 4.2 Suffixed forms (מַלְאָכִי, מַלְאָכָיו)

YHWH-speech suffix "my angel" → ทูตสวรรค์ของเรา.
YHWH-narrative suffix "his angels" → ทูตสวรรค์ทั้งหลายของพระองค์.

### 4.3 The book of Malachi

The book-name מַלְאָכִי is a personal name in tradition but is also the lemma "my-messenger" form. The book title is rendered "มาลาคี" (transliteration); the lemma in the body text retains the lock.

### 4.4 Plain human messengers

מַלְאָךְ in plain narrative for human envoys (e.g., 2 Sam 11:19-25 — David's military messenger; 2 Kings 1:2-3 — Ahaziah's messengers; Job 1:14-18 — the disaster-messengers) uses the plain register, not ทูตสวรรค์. Context (king's court / disaster narrative / non-supernatural) marks these. This doc covers only the divine / supernatural class.

**Human-messenger surface hierarchy (added 2026-05-25, 2 Kings EOB Item E).** The divine side is locked above; the *human* מַלְאָךְ side had drifted across an unconstrained set (`ผู้ส่งสาร` / `ผู้ส่งข่าว` / `ผู้สื่อสาร` / `ทูต` / `คณะทูต`). Both external reviewers (ChatGPT CONCERN; Gemini FINE-but-document) converged on **principled variation, not flattening** — Hebrew מַלְאָךְ spans a runner and a state delegation, and Thai marks that. The hierarchy:

| Sense | Thai (locked) | Example |
|---|---|---|
| 1. Default narrative messenger / runner | **`ผู้ส่งสาร`** | 2 Kings 1:2–3 (Ahaziah's messengers); the by-your-messengers taunt 2 Kings 19:23 |
| 2. Diplomatic envoy / formal state representative | **`ทูต`** | 2 Kings 17:4 (Hoshea → So of Egypt) |
| 3. Delegation / group of envoys | **`คณะทูต`** | 2 Kings 20:13 (Babylonian envoys to Hezekiah) |
| 4. Prophetic herald / God's spokesman-messenger | **`ผู้สื่อสารของพระเจ้า`** (licensed 2026-05-26, 2CH EOB Item E) | 2 Chr 36:15–16 (the prophets YHWH "sent again and again") — the herald/spokesperson weight is genuine and reads naturally in Thai; distinct from a mere courier |
| 5. Avoid | ~~`ผู้สื่อสาร`~~ (for ordinary couriers/envoys), ~~`ผู้ส่งข่าว`~~ | reclassify to (1)/(2)/(3); the sole licensed `ผู้สื่อสาร` use is the prophetic-herald sense (4), and it must be `ผู้สื่อสารของพระเจ้า` |

**2 Chronicles conformance (decided 2026-05-26, 2CH EOB Item E).** Both external reviewers (ChatGPT + Gemini) CONCERN'd that 2 Chronicles rendered every human/prophetic מַלְאָךְ as the avoid-form `ผู้สื่อสาร`. Resolution: the two **ordinary** cases were reclassified per the hierarchy — **18:12** (the court messenger fetching Micaiah) → `ผู้ส่งสาร`; **35:21** (Neco's royal envoys to Josiah) → `คณะทูต`. The two **prophetic-herald** cases — **36:15–16** (the prophets YHWH "sent again and again… but they mocked the messengers of God") — are **retained as `ผู้สื่อสารของพระเจ้า`** under the newly-licensed sense (4) above: here מַלְאָךְ denotes God's commissioned spokesmen, and the herald weight of `ผู้สื่อสาร` is apt. Ben's call, both reviewers' nuance honored.

`ผู้ส่งสาร` is the default; reserve `ทูต` / `คณะทูต` for genuinely diplomatic contexts. **19:23 fixed 2026-05-25** (`ผู้สื่อสาร` → `ผู้ส่งสาร`: בְּיַד מַלְאָכֶיךָ "by your messengers", an ordinary-messenger taunt). The remaining 2 Kings `ผู้สื่อสาร` occurrences (5:10, 6:32–33, 9:18, 10:8, 14:8, 19:9, 19:14) are queued for the deferred cross-book normalization pass (§3) — each classified per-verse (most → `ผู้ส่งสาร`; 14:8 / 19:9 royal-to-royal contexts to weigh for `ทูต`), not blanket-replaced. **Not a 2 Kings tag blocker** (REVIEW item; 2 Kings stays MT-faithful either way).

**1 Chronicles conformance (verified 2026-05-26, 1CH EOB Item C).** Both external reviewers revisited the scattered cross-book human-messenger set (ChatGPT CONCERN: license by register; Gemini FINE: just document it) — they converge on the table above, which already governs. 1 Chronicles itself **conforms with no drift and no normalization needed**: its only human-`מַלְאָךְ` (plural `מַלְאָכִים`, medial-kaf — never matches the divine lock) surfaces are `ทูต` at 14:1 (Hiram of Tyre's envoys to David) and 19:2 (David's condolence delegation to Hanun of Ammon) — both sense-2 royal/diplomatic — plus `ส่งคน` at 19:16 (Arameans sending for reinforcements; messenger role backgrounded — the licensed paraphrase). **Zero `ผู้สื่อสาร`/`ผู้ส่งข่าว` in 1CH.** This table is now the on-record register standard both reviewers asked for; the scattered back-catalogue surfaces (other books) remain the §3 deferred queue.

---

## 5. Change log

- **v0.1** (2026-05-13) — Initial lock, triggered by Exodus end-of-book audit. Tri-AI consensus (ChatGPT + Gemini + Claude separate session) agreed on ทูตสวรรค์ corpus-wide.
