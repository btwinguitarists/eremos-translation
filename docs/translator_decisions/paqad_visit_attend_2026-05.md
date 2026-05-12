# פָּקַד (paqad) — four-sense corpus table

**Scope:** The Hebrew verb פָּקַד (~300 OT occurrences) — one of the most frequent and contextually-ranged divine-action verbs in the OT. The lemma carries four distinct senses that require four different Thai renderings; one Thai verb cannot serve all four contexts.

**Decided:** 2026-05-12 (Genesis end-of-book audit §J3 + Ruth-audit carry-forward open-question resolution). **CRITICAL** before Exodus 3:16 ships (which is the locking-precedent for sense (1) divine-pastoral-care visit).

**Companion docs:** `divine_names_table_2026-05.md`, `hebrew_idioms_and_metaphor_2026-05.md`, `ot_register_policy_2026-05.md`.

---

## 1. The four senses + Thai locks

| Sense | Hebrew context | Thai lock | Locking precedents |
|---|---|---|---|
| **(1) Pastoral-care visit** | God "visits" his people in mercy/care — typically introducing salvation-act or covenant-fulfillment | **ทรงเยี่ยมเยียน** | **Gen 21:1**, **Gen 50:24–25**, Ex 3:16, Ex 4:31, Ex 13:19, 1 Sam 2:21, Ruth 1:6 (already locked); Lk 1:68 NT-echo (ἐπεσκέψατο) |
| **(2) Numbering / mustering** | Census-taking; military-roster compiling | **ทรงทำสำมะโน / ทำสำมะโน** | Num 1:3 + 1:19, Num 26 throughout, 1 Sam 11:8, 1 Sam 13:15, 1 Sam 14:17, 1 Sam 15:4 |
| **(3) Appointment / commissioning** | Setting someone over a task / office | **ทรงแต่งตั้ง / แต่งตั้ง** | Num 27:16, Jer 1:10, Jer 49:19, 2 Kgs 25:22, 2 Chr 12:10 |
| **(4) Judgment-visitation (punitive)** | God "visits" in the sense of bringing judgment / calling-to-account | **ทรงลงโทษ / ทรงพิพากษา** | Ex 32:34 ("when I visit, I will visit their sin upon them"), Hos 4:9, Amos 3:14, Jer 5:9, Jer 5:29, Jer 6:15, Jer 9:25, Jer 27:22 |

The four senses are **lexically distinct** in Thai (different rendering for each), but **all derive from the same Hebrew lemma** — the verse-level KD should name the Hebrew lemma + classify the sense so readers can trace lemma-recurrence across the four-rendering-cluster.

---

## 2. Sense-classification heuristics

When a translator encounters פָּקַד in a new context, apply this decision-tree:

1. **Is the subject God + the object God's people + the discourse-frame benevolent (salvation/covenant-fulfillment)?** → Sense (1) ทรงเยี่ยมเยียน
2. **Is the construction a numerical-counting or military-roster?** → Sense (2) ทรงทำสำมะโน
3. **Is the construction a הִפְקִיד עַל ("appoint over") or similar X-over-Y syntax?** → Sense (3) ทรงแต่งตั้ง
4. **Is the subject God + the object sin/wickedness/wrongdoing + the discourse-frame punitive (judgment-frame)?** → Sense (4) ทรงลงโทษ

The four senses are mutually exclusive in practice — a single occurrence falls cleanly into one of the four. Edge cases (e.g., God "visiting" in a context that is **simultaneously** benevolent-to-Israel and punitive-to-Egypt, as in Ex 32:34) are flagged at the verse-level KD and resolved by the dominant discourse-direction.

---

## 3. Senses A vs. D — the pastoral/judgment polarity

Senses (1) and (4) are the most theologically-loaded pair because they form a polarity: God-visits-in-mercy vs. God-visits-in-judgment. The **same Hebrew lemma** is doing both kinds of work.

This polarity is the OT's clearest example of a lemma carrying both positive and negative theological weight depending on context. A few high-stakes verses:

| Verse | Hebrew | Sense | Note |
|---|---|---|---|
| Gen 21:1 | וַיהוָה פָּקַד אֶת־שָׂרָה | (1) pastoral-care | "And YHWH visited Sarah" — Isaac's birth |
| Gen 50:24–25 | פָּקֹד יִפְקֹד אֱלֹהִים אֶתְכֶם | (1) pastoral-care | Joseph's last words: "God will surely visit you" |
| Ex 3:16 | פָּקֹד פָּקַדְתִּי אֶתְכֶם | (1) pastoral-care | YHWH at the burning bush: "I have surely visited you" — fulfillment of Gen 50:24 |
| Ex 32:34 | בְּיוֹם פָּקְדִי וּפָקַדְתִּי | (4) judgment | "In the day of my visiting, I will visit their sin upon them" — Golden Calf aftermath |
| Hos 4:9 | וּפָקַדְתִּי עָלָיו דְּרָכָיו | (4) judgment | "I will visit upon him his ways" |

The Ex 3:16 verse intentionally echoes Gen 50:24 — same lemma, same intensifying infinitive-absolute construction (פָּקֹד פָּקַדְתִּי). Thai readers should be able to see this echo: **ทรงเยี่ยมเยียน...อย่างแน่นอน** at both verses preserves the structural-recognition.

---

## 4. Cross-corpus thread (forward-look)

- **Exodus 3:16 + 4:31 + 13:19** — locking-trio for the Pentateuch sense (1) usage
- **1 Sam 2:21** — YHWH visits Hannah (gives her additional children) — sense (1)
- **Ruth 1:6** — already shipped with ทรงเยี่ยมเยียน (per `Ruth audit 2026-04 open question, resolved here`)
- **Psalms** — Pss 8:4, 65:9, 80:14, 89:32, 106:4 — mix of sense (1) and sense (4)
- **Jeremiah** — heavy on sense (4) judgment-visitation; ~30 occurrences across Jer
- **Lk 1:68 NT-echo** — Zechariah's Benedictus: ἐπεσκέψατο ὁ Θεός / **พระเจ้าทรงเยี่ยมเยียน** (cross-corpus into NT)

---

## 5. Implementation checklist

- [x] Ruth 1:6: ทรงเยี่ยมเยียน (sense 1) — already shipped 2026-04
- [x] Genesis 21:1, 50:24–25: locking-precedents documented in this doc
- [ ] Extend `check_key_term_consistency.py` with a paqad multi-rendering rule: per-sense Thai rendering must match the catalogue; verse-level KD must explicitly name the sense (1/2/3/4)
- [ ] At Ex 3:16 ship-time: confirm ทรงเยี่ยมเยียน + the Gen 50:24 echo is visible in Thai
- [ ] At Ex 32:34 ship-time: confirm ทรงลงโทษ (sense 4) + verse-level KD names the sense-1-vs-sense-4 distinction within the chapter (32:34 is the polarity-pivot)

---

## 6. Change log

- **v0.1** (2026-05-12) — Initial policy, triggered by Genesis end-of-book audit §J3 + Ruth-audit carry-forward (Ruth 1:6 ทรงเยี่ยมเยียน was the per-verse precedent; Genesis adds 21:1 + 50:24–25 as corpus-locking precedents). Resolves the open question in the Ruth audit on whether ทรงเยี่ยมเยียน or ทรงเหลียวแล is the better Thai — locked to **ทรงเยี่ยมเยียน** with cross-OT corpus consistency.
