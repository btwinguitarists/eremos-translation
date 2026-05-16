# OT-NT cross-quotation Thai-thread — lemma + quotation locks

**Status:** LOCKED 2026-05-16 (initial — OT-side DEU normalizations applied; NT-side reaudits staged)
**Triggered by:** Deuteronomy end-of-book audit (Item C). Cross-AI consensus Gemini + ChatGPT (both: path b).
**Scope:** Major lemma-pairs + multi-citation OT verses where the OT text is directly quoted in the NT; the Thai surface must thread through the OT→NT boundary for reader-recognition of the cross-canonical link.
**Companion docs:** `proper_names_and_transliteration_2026-05.md`, `decalogue_parallel_text_2026-05.md`, `psyche_vs_pneuma_anthropological_2026-04.md`.

---

## 1. The principle

When an OT verse is directly quoted in the NT, the Thai reader must be able to recognize the NT-side as the same text as the OT-side. Where the Hebrew lemma → LXX Greek lemma → NT-citation Greek lemma forms a thread (e.g., נביא → προφήτης → προφήτης), the Thai rendering must be **the same word** across the entire thread, unless context demands register-shift (rare, must be documented in Layer-2 footer).

Deuteronomy is **the most-quoted OT book in the NT** — the natural anchor for the lemma-thread locks.

---

## 2. Locked lemma-pairs

### 2.1 נביא / προφήτης → ผู้เผยพระวจนะ

**Lock:** Hebrew נביא (nabi') + Greek προφήτης → **ผู้เผยพระวจนะ** ("one who reveals the divine word"). Reject **ผู้พยากรณ์** ("foreteller/diviner") as a translation of either lemma — even though it appears in some Thai bibles, the pyākon/pyākạrn root collides semantically with divination (cf. DEU 18:10's "ผู้ทำการดูดวง" = the proscribed pagan diviner). The נביא is precisely the **anti-diviner** — the legitimate revealer of YHWH's word.

**Anchor verse:** DEU 18:15 — "องค์พระผู้เป็นเจ้าพระเจ้าของเจ้าจะทรงตั้งผู้เผยพระวจนะเหมือนข้าพเจ้าให้เจ้า" — quoted directly in:
- **Acts 3:22** (Peter's Solomon's-portico sermon)
- **Acts 7:37** (Stephen's defense)

Both NT citations should match the OT Thai surface "ผู้เผยพระวจนะ".

**Forward-protection:** the lock extends to:
- DEU 18:9–22 (entire prophet-cluster): vv.15, 18, 19, 20, 22 — ✓ normalized 2026-05-16.
- Isaiah, Jeremiah, Ezekiel, Daniel + the Twelve (~16 un-shipped OT books).
- Every NT προφήτης occurrence (~140+) — `check_phrase_consistency.py` should HARD-FAIL on ผู้พยากรณ์ as a translation of προφήτης.

**Exception:** the rare cases where the NT identifies a **false prophet** (ψευδοπροφήτης, e.g., Matt 7:15) use **ผู้เผยพระวจนะเท็จ** — same root + qualifier.

### 2.2 נֶפֶשׁ / ψυχή — the Shema-thread (DEU 6:5)

**Status:** DEU-side lock applied; NT-side reaudit staged.

The Shema (DEU 6:5) is quoted at **Matt 22:37 // Mark 12:30 // Luke 10:27**. The Hebrew נֶפֶשׁ = Greek ψυχή = "soul/life-force/whole-person".

Locked Thai: נֶפֶשׁ / ψυχή → **จิตวิญญาณ** (per `psyche_vs_pneuma_anthropological_2026-04.md`).

| Verse | Currently | Lock |
|---|---|---|
| DEU 6:5 | สุดจิตวิญญาณ | ✓ correct |
| DEU 11:13 | (was) สุดจิต — within-DEU drift | ✓ normalized 2026-05-16 → สุดจิตวิญญาณ |
| Luke 10:27 | สุดจิตวิญญาณ | ✓ matches DEU |
| Mark 12:30 | สุดจิต (within-NT drift) | — staged for NT-corpus reaudit |
| Matt 22:37 | สุดจิต (within-NT drift) | — staged for NT-corpus reaudit |

### 2.3 DEU 25:4 muzzle-ox — three-way quotation lock

**Lock:** DEU 25:4 // 1 Cor 9:9 // 1 Tim 5:18 — all three must use the same Thai surface for Paul's twice-quoted command.

**Canonical Thai:** **"อย่าเอาผ้าผูกปากวัวขณะมันกำลังนวดข้าว"**.

Cross-AI consensus: both Gemini and ChatGPT identified the 1 Cor 9:9 form as the canonical baseline. Natural Thai agricultural register, concrete object ("ผ้า" — cloth/material as the muzzle device), and works in Paul's argumentation context.

| Verse | Status |
|---|---|
| DEU 25:4 | ✓ normalized 2026-05-16 |
| 1 Cor 9:9 | — staged for NT-side reaudit; verify already-shipped Thai surface |
| 1 Tim 5:18 | — staged; currently uses "ตะกร้อครอบปาก" (basket-cover) — reject; normalize to canonical |

### 2.4 קנא / ζῆλος (divine-jealousy thread) — DEU 32:21 // Rom 10:19

**Status:** flagged; staged. Currently DEU uses **หึง** and Rom uses **ริษยา** — these are different Thai-affect words. Lock decision deferred pending review of the broader divine-jealousy thread across the Pentateuch + Romans.

### 2.5 Matt-4 temptation-quotations — DEU 6:13, 6:16, 8:3

**Status:** staged for NT-side reaudit. Each temptation-quote shows MEDIUM-severity verb-lemma drift between DEU and Matt:

| OT verse | NT quote | Drift |
|---|---|---|
| DEU 6:13 | Matt 4:10 | DEU "เกรงกลัว/รับใช้/สาบาน" vs Matt "นมัสการ/ปรนนิบัติ" (Matt follows LXX προσκυνέω form; defensible but document with Layer-2 footer) |
| DEU 6:16 | Matt 4:7 | DEU "ทดสอบ" vs Matt "ทดลอง" (verb-lemma drift on נסה/πειράζω; normalize at NT-side reaudit) |
| DEU 8:3 | Matt 4:4 | DEU "มีชีวิตอยู่" vs Matt "ดำรงชีวิต" (verb drift on חיה/ζάω; normalize at NT-side reaudit) |

These are all NT-side adjustments; the DEU surface stays as-is.

---

## 3. Layer-2 footer policy for cross-quotation threads

At each locked OT-side anchor verse (DEU 18:15, 25:4, 32:35, 32:43, etc.), the Layer-2 footer should:
1. Identify the NT citation(s).
2. Confirm the Thai surface is locked across the OT-NT thread.
3. Cross-reference this doc.

At each NT-side citation verse, the Layer-2 footer should:
1. Identify the OT source.
2. Note any LXX-vs-MT divergence relevant to the citation form.
3. Confirm Thai-surface alignment with the OT-side.

---

## 4. `check_phrase_consistency.py` HARD-FAIL extension

The cross-quotation lock should be machine-enforceable. The check should be extended to:

1. Build a known OT-NT citation pair table (DEU + every NT echo, expandable to Pss/Isa/Mal as those ship).
2. For each citation pair, verify the locked Thai surface (from §2 above) appears in **both** the OT-side and the NT-side verse.
3. HARD-FAIL when a citation pair diverges and no Layer-2 footer justifies the divergence.

Initial table to seed: DEU 18:15 → Acts 3:22, Acts 7:37; DEU 6:5 → Matt 22:37, Mark 12:30, Luke 10:27; DEU 25:4 → 1 Cor 9:9, 1 Tim 5:18; DEU 32:35 → Rom 12:19, Heb 10:30; DEU 32:43 → Rom 15:10 (+ Heb 1:6 with text-critical footer); DEU 21:23 → Gal 3:13; DEU 27:26 → Gal 3:10; DEU 30:12–14 → Rom 10:6–8.

---

## 5. Change log

- **v0.1** (2026-05-16) — Initial lock from DEU end-of-book audit. OT-side: DEU 18:15 + 18:18, 18:19, 18:20, 18:22 (prophet-cluster) normalized to ผู้เผยพระวจนะ; DEU 25:4 normalized to "อย่าเอาผ้าผูกปากวัวขณะมันกำลังนวดข้าว"; DEU 11:13 normalized to สุดจิตวิญญาณ. NT-side reaudits staged: Synoptic Shema (Matt 22:37, Mark 12:30), Pauline muzzle-ox (1 Cor 9:9, 1 Tim 5:18), Matt-4 temptation-quotes, Rom 10:19 jealousy thread. Path b chosen (doc + OT lock + staged NT reaudits) per cross-AI consensus.
