# Numbers — 5 Decisions You Need to Make

**Date:** 2026-05-15
**Purpose:** Once you answer these 5 questions, I'll apply all revisions, run `ship_book.sh NUM`, tag `book-numbers-v1`, and the loop continues to Leviticus.

**Background:** Two external AIs (ChatGPT + Gemini) reviewed the 6 issues the end-of-book audit flagged. They **agreed** on items A, B (most of it), C, and D. They **disagreed** on E and F. There are also some doc-writing questions. That leaves you with 5 calls.

---

## ✅ Already settled (no action — I'll just do these)

- **Item A** (NUM 14:18 Sinai formula) — spot-revise to the doc-canonical Thai.
- **Item B — Balaam cluster** (NUM 22:22–35, 10 occurrences) — normalize ทูตขององค์พระผู้เป็นเจ้า → **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า**.
- **Item C** (NUM 25 + 31 warfare/zealot register) — don't change Thai surface; write `ot_warfare_ethics_2026-05.md` and add restrained Layer-2 footers at NUM 25:6–9 and 31:17–18.

---

## ❓ Decision 1 — NUM 20:16 (the *one* Balaam-cluster verse that's ambiguous)

### Context
This isn't Balaam seeing an angel with a sword. It's **Israel telling Edom**, "When we cried out, God *sent a מַלְאָךְ* and brought us out of Egypt." Could be a heavenly messenger OR an ordinary "messenger" in diplomatic language. The two AIs split:

- **ChatGPT:** "Mark for Thai/native-theology review — the standalone form is more ambiguous than the Balaam cluster."
- **Gemini:** "Apply the lock — `ทูตสวรรค์` for consistency."

### The verse
**Hebrew:** וַנִּצְעַק אֶל־יְהוָה … וַיִּשְׁלַח **מַלְאָךְ** וַיֹּצִאֵנוּ מִמִּצְרָיִם

**Currently shipped Thai:**
> และเมื่อเราร้องเรียกองค์พระผู้เป็นเจ้า … และทรง**ส่งทูต**และนำเราออกจากอียิปต์

### Your two options

**Option A — Lock it now to `ทูตสวรรค์`** (Gemini's call)
> และทรง**ส่งทูตสวรรค์**และนำเราออกจากอียิปต์
- Pro: Mechanical consistency. Same Hebrew word → same Thai everywhere in OT.
- Con: Theologically over-commits a verse where Israel is just summarizing the Exodus story to a foreign king.

**Option B — Hold for Thai-reviewer review** (ChatGPT's call)
- Leave `ทูต` as shipped for now, add a YAML question on the /review form, ship NUM with this single verse flagged.
- Pro: Doesn't force a theological call. Reviewer Benz or other Thai readers can weigh in.
- Con: Slightly inconsistent within the book until the review comes back.

### 📝 Your answer (circle one):
- [ ] **Option A — Lock to ทูตสวรรค์ now**
- [ ] **Option B — Hold for Thai reviewer**

---

## ❓ Decision 2 — Sinai spelling (and Succoth)

### Context
Exodus already locked **ซีนาย** (matches THSV-1971 — standard Thai Bible spelling). Numbers shipped **สีนาย** in 10 places. Same issue with **สุคโคท** (Exodus's locked form) vs **สุคคท** (what NUM 33 shipped).

Both AIs say: **normalize Numbers to match Exodus**. Add a glossary check so it can't drift again.

### 📝 Your answer (just confirm):
- [ ] **Yes — normalize all 10 NUM `สีนาย` → `ซีนาย`, and `สุคคท` → `สุคโคท`**
- [ ] **No / Other** (explain): _______________________

---

## ❓ Decision 3 — YHWH footnote wording (chapters 15–36)

### Context
The first-occurrence YHWH footnote was one wording in NUM 1–14, then drifted to a slightly shorter wording from NUM 15 onward (22 chapters). Footnote is conceptually correct in both versions. But the check script (`check_divine_names.py`) only recognizes the *old* wording and flags 22 false warnings.

### Your two options

**Option A — Restore the old wording across NUM 15–36** (ChatGPT's call)
- Add back the **ยาห์เวห์** romanization phrase to footnotes in chs.15–36.
- Pro: Uniform wording across all of Numbers and matches earlier OT books.
- Con: 22 footnote edits + leaves the script strict (good for future books).

**Option B — Loosen the check script** (Gemini's call)
- Update `check_divine_names.py` to accept *both* wordings; treat the newer shorter wording as the going-forward standard.
- Pro: Just one script change instead of 22 edits.
- Con: The newer wording becomes the OT default — once you do this, it should propagate backward to consolidate (or you live with mixed templates forever).

### 📝 Your answer:
- [ ] **Option A — Restore old wording across NUM 15–36**
- [ ] **Option B — Loosen check script, adopt new wording as OT default**

---

## ❓ Decision 4 — NUM 14:17 standalone אֲדֹנָי (Adonai) prayer-vocative

### Context
Adonai (אֲדֹנָי) is a Hebrew word meaning "my Lord" — used standalone as a respectful name for God, **especially in personal prayer**. The Divine Names policy mostly tells you what to do with YHWH (יהוה → องค์พระผู้เป็นเจ้า). But standalone Adonai *as a prayer vocative* never got a locked Thai form.

This matters because **standalone Adonai shows up everywhere in Psalms, Isaiah, Ezekiel, and Daniel.** Whatever you pick for NUM 14:17 becomes the precedent for those entire books.

### The verse
This is Moses interceding for Israel right after the spies-rebellion. He's praying:

**Hebrew:** וְעַתָּה יִגְדַּל־נָא כֹּחַ **אֲדֹנָי** כַּאֲשֶׁר דִּבַּרְתָּ לֵאמֹר

**Literal English:** "And now, please let the power of **Adonai (my Lord)** be great, as you have spoken, saying…"

**Currently shipped Thai:**
> บัดนี้ ขอพระอานุภาพ**ขององค์พระผู้เป็นเจ้าของข้าพระองค์**ทรงสำแดงพระเกียรติยิ่งใหญ่ …

(This already uses what Gemini wants, by accident — it just isn't documented yet.)

### Your two options

**Option A — Lock `องค์เจ้านาย`** (ChatGPT's call)
- Means "Lord/Master" — distinct from องค์พระผู้เป็นเจ้า (which is reserved for YHWH).
- Pro: Keeps the distinction Hebrew makes between יהוה and אֲדֹנָי visible in Thai.
- Con: Might feel formal/stiff in personal prayer (your Thai reviewers can confirm).
- NUM 14:17 would be revised to: ขอพระอานุภาพ**ขององค์เจ้านาย**ทรงสำแดงพระเกียรติยิ่งใหญ่ …

**Option B — Lock `องค์พระผู้เป็นเจ้าของข้าพระองค์`** (Gemini's call)
- "My Lord" — collapses standalone Adonai into the YHWH form.
- Pro: Natural petitionary register (it's already what's shipped); reads warmly in prayer.
- Con: Erases the Hebrew distinction between יהוה and אֲדֹנָי throughout Psalms/Prophets.
- NUM 14:17 stays as already shipped.

### 📝 Your answer:
- [ ] **Option A — Lock องค์เจ้านาย (preserves Hebrew distinction; revise NUM 14:17)**
- [ ] **Option B — Lock องค์พระผู้เป็นเจ้าของข้าพระองค์ (warmer prayer Thai; keep as shipped)**

---

## ❓ Decision 5 — New translator_decisions docs

### Context
The audit recommended writing **5 new docs** to lock translation choices that came up in Numbers and protect later books:

1. **`aaronic_blessing_2026-05.md`** — Locks the Thai for the Aaronic Blessing (NUM 6:24–26). The most-quoted OT passage; needs canonical Thai.
2. **`sacrificial_vocabulary_2026-05.md`** — Locks Thai for עֹלָה / מִנְחָה / חַטָּאת / שְׁלָמִים. Protects Leviticus + all sacrificial language.
3. **`goel_kinsman_redeemer_2026-05.md`** — Locks Thai for גֹּאֵל (kinsman-redeemer / avenger of blood). **Critical for Ruth + Boaz scene.**
4. **`balaam_oracles_2026-05.md`** — Locks Thai for the נְאֻם / מָשָׁל "oracle" formulae in Balaam's mashalim (NUM 23–24). Affects later prophet introductions.
5. **`ot_warfare_ethics_2026-05.md`** — The ḥerem/warfare ethics doc from Decision Item C. **I'll write this regardless** (already settled above).

### Your two options

**Option A — Write all 4 remaining docs now** (before LEV)
- Pro: Maximum forward protection. Ruth and Leviticus are next; #2 and #3 directly defend them.
- Con: ~2-3 hours of doc-writing before LEV 1 ships.

**Option B — Defer all 4 to "just-in-time"** (write each before the book that needs it)
- `goel` → before Ruth; `sacrificial_vocabulary` → before LEV 1; `aaronic_blessing` → backfill anytime; `balaam_oracles` → backfill anytime.
- Pro: Faster to LEV 1.
- Con: More risk that LEV/Ruth ship with drift before the doc lands.

**Option C — Hybrid (recommended): write the 2 that protect upcoming books**
- Write `sacrificial_vocabulary` (LEV is next) + `goel_kinsman_redeemer` (Ruth is in queue) now. Defer `aaronic_blessing` + `balaam_oracles`.
- Pro: ~30-45 min instead of 2-3 hours, protects what's next.
- Con: None — best balance.

### 📝 Your answer:
- [ ] **Option A — Write all 4 now**
- [ ] **Option B — Defer all 4**
- [ ] **Option C (recommended) — Write sacrificial_vocabulary + goel now, defer the other 2**

---

## After you answer

Drop the 5 answers into the next `/loop` prompt (e.g. `"1B, 2yes, 3A, 4B, 5C"`). I'll:

1. Apply the 4 settled items (A, B-cluster, C, D normalization) — script changes plus the 22 footnote edits if you chose 3A, or one script edit if you chose 3B
2. Apply your Decision 1 (NUM 20:16) and Decision 4 (Adonai vocative)
3. Write the docs per Decision 5
4. Re-run all 6 mechanical checks across the affected chapters
5. `bash scripts/ship_book.sh NUM` (bundle + tag `book-numbers-v1` + iOS bump + TestFlight + Play update)
6. Loop continues to **LEV 1**

Total wall time once you answer: 30-60 minutes depending on Decision 5 choice.

---

**Recommendation if you don't want to think about this:** `1B, 2yes, 3B, 4B, 5C`.
- 1B keeps NUM 20:16 flexible (reviewer-friendly)
- 2yes is uncontroversial
- 3B is one script edit instead of 22 doc edits
- 4B keeps what's already shipped (warmer Thai) and you can revisit before Psalms
- 5C protects the next two books without delaying LEV too long
