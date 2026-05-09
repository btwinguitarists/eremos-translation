# מָנָה (manah) — Divine appointment Leitwort lock

**Scope:** The Hebrew verb מָנָה (manah) — "appoint, prepare, designate" — when used of God appointing creatures or elements as agents of his sovereign will. Recurs as a deliberate Leitwort (keyword) in Jonah (4 occurrences across chs. 2–4: fish, plant, worm, wind), and is a candidate Leitwort lock for future books where divine-appointment patterns recur.

**Decided:** 2026-05-09 (Jonah end-of-book audit recommendation; cross-AI review concurs).

**Companion docs:** `leitwort_handling_policy_2026-05.md` (Rule 1 — corpus-lock list includes מָנָה), `ot_register_policy_2026-05.md` §1.1 (divine-action ราชาศัพท์).

---

## 1. The lock

| Hebrew form | Thai rendering | Notes |
|---|---|---|
| Pi'el of מָנָה (וַיְמַן) | **ทรงจัดเตรียม** | "(he) appointed/prepared" — the form used in all 4 Jonah occurrences |
| Other binyanim (Qal, Niph'al) | (decide per occurrence) | Less frequent; document on first encounter |

The lock applies to the **divine-subject Pi'el** form specifically (which is the form that occurs as a Leitwort).

---

## 2. The Jonah corpus

The 4 Jonah occurrences (chronological):

| Verse | Hebrew | Thai | Object |
|---|---|---|---|
| Jonah 2:1 (MT) | וַיְמַן יְהוָה דָּג גָּדוֹל | องค์พระผู้เป็นเจ้าทรงจัดเตรียมปลาใหญ่ตัวหนึ่ง | the great fish |
| Jonah 4:6 | וַיְמַן יְהוָה־אֱלֹהִים קִיקָיוֹן | องค์พระผู้เป็นเจ้าพระเจ้าทรงจัดเตรียมต้นน้ำเต้า | the qiqayon plant |
| Jonah 4:7 | וַיְמַן הָאֱלֹהִים תּוֹלַעַת | พระเจ้าทรงจัดเตรียมหนอนตัวหนึ่ง | the worm |
| Jonah 4:8 | וַיְמַן אֱלֹהִים רוּחַ קָדִים חֲרִישִׁית | พระเจ้าทรงจัดเตรียมลมตะวันออกอันร้อนแรง | the scorching east wind |

**The four-fold pattern is intentional.** All four creatures/elements are non-human agents through which YHWH teaches the prophet. The Leitwort `מָנָה` declares divine sovereignty over creation: nothing happens to Jonah by chance — even the gourd-pest worm and the desert sirocco are appointed.

The narrator varies the divine name across the four occurrences (יהוה → יהוה־אלהים → האלהים → אלהים) but keeps the same verb. This signals that the divine-subject's identity may shift in nuance but the appointment-act is the same God's continuous instruction.

---

## 3. Why ทรงจัดเตรียม

- **ทรง-** preserves the Rachasap (royal Thai) register required for divine subjects.
- **จัดเตรียม** ("prepare, arrange, designate, ready") captures both senses of מָנָה: (a) bring-into-being for a purpose; (b) appoint-with-task. The Pi'el intensification (vs Qal's "count, number") supports the "purposeful appointment" sense.
- The compound is established in Thai Christian vocabulary (THSV uses "ทรงเตรียม" for Jonah 1:17/2:1; we use the slightly stronger "ทรงจัดเตรียม" to capture the Pi'el-intensive force).

### 3.1 What we deliberately reject

- **ทรงสร้าง** ("created") — too strong; the fish, worm, and wind are not new creatures created ex nihilo at Jonah's moment. Reserved for Gen 1's בָּרָא.
- **ทรงส่ง** ("sent") — too directional; the appointment is broader than dispatching.
- **ทรงนำมา** ("brought") — too generic; loses the purposeful-appointment force.

---

## 4. Cross-corpus candidates for לpiece-lock extension

The Pi'el of מָנָה for divine-subject appointment also occurs in:

- **Daniel 1:5, 10, 11** — the king of Babylon "appoints" food and overseers for Daniel; the appointment-pattern carries from divine to royal sovereignty. Render as **กษัตริย์ทรงจัดเตรียม** for the royal-subject (Rachasap per `ot_register_policy §2.2` for foreign emperor).
- **Daniel 3:12** — the king "appoints" Shadrach, Meshach, Abednego over Babylonian provinces.
- **1 Chronicles 9:29** — Levitical-officials "appointed" over temple goods. Render with plain Thai (priestly appointments do not get Rachasap per `ot_register_policy §2.2`).

For non-Pi'el forms (Qal "count, number"; Niph'al "be counted"), the Thai rendering varies — those are not Leitwort-locked and are decided per-context.

---

## 5. Implementation checklist

- [x] All 4 Jonah occurrences (2:1, 4:6, 4:7, 4:8) use ทรงจัดเตรียม (verified 2026-05-09 ship).
- [ ] Pre-load `data/manah_corpus_thread.json` with all known divine/royal-subject Pi'el-מָנָה occurrences for cross-reference.
- [ ] `check_key_term_consistency.py` rule: any divine/royal Pi'el-מָנָה not rendered ทรงจัดเตรียม is a HARD FAIL.

---

## 6. Why this is a Leitwort lock, not a corpus lock

מָנָה is **not** as theologically loaded as חֶסֶד or יהוה or נָחַם — it doesn't carry covenant-vocabulary or divine-name weight. But within Jonah, it is a structural Leitwort: the four-fold appointment-pattern is the book's narrative architecture. Translation must preserve the lexical recurrence within the book to make the pattern visible.

For other books where מָנָה appears in an isolated context (not as a Leitwort), the same Thai rendering should still apply — for the same reason chesed has a corpus lock, mainah has a corpus lock — but the structural Leitwort role is Jonah-specific.

---

## 7. Change log

- **v0.1** (2026-05-09) — Initial lock, triggered by Jonah end-of-book audit. Locks ทรงจัดเตรียม uniformly for divine/royal-subject Pi'el-מָנָה occurrences across the OT corpus.
