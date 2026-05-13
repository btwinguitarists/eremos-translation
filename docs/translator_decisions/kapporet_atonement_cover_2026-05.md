# כַּפֹּרֶת / kapporet — OT corpus-wide rendering lock

**Scope:** All OT instances of the Hebrew lemma כַּפֹּרֶת (kapporet, the gold cover of the ark of the covenant). Lock the Thai surface as a single corpus-wide rendering, and document the cross-corpus relationship with the NT Greek ἱλαστήριον (Rom 3:25; Heb 9:5).

**Decided:** 2026-05-13 (Ben + tri-AI review of Exodus end-of-book audit). The decision aligns the OT surface with the NT-corpus's existing distinction between (a) physical-tabernacle ἱλαστήριον (Heb 9:5) and (b) Christological-propitiation ἱλαστήριον (Rom 3:25).

**Companion docs:** `hilasterion_heb-rom_distinction_2026-05.md` (NT-side lock), `divine_names_table_2026-05.md`, `chesed_covenant_love_2026-05.md`.

---

## 1. The lock

**Hebrew lemma** כַּפֹּרֶת in all OT occurrences → **พระที่นั่งกรุณา** ("throne of grace" / "mercy seat").

This aligns the OT physical-tabernacle object with the Heb 9:5 NT rendering. The Christological-propitiation reading at Rom 3:25 (ἱλαστήριον = "เครื่องบูชาไถ่บาป") is a separate semantic layer — the NT corpus already distinguishes; the OT follows suit.

### 1.1 The triple-fold semantic field of ἱλαστήριον

The Greek noun ἱλαστήριον carries three semantic strands in Pauline usage:

| Strand | Reading | Lock |
|---|---|---|
| (a) Propitiation | wrath-averting sacrifice (Reformation default) | Subsumed in Rom 3:25's เครื่องบูชาไถ่บาป |
| (b) Expiation | sin-removing sacrifice (modernist-favored) | Subsumed in Rom 3:25's เครื่องบูชาไถ่บาป |
| (c) Mercy seat / cover-of-ark | LXX of OT kapporet | Heb 9:5 + OT lock: พระที่นั่งกรุณา |

Rom 3:25 fuses (a)+(b)+(c) into a single Christological term. The Eremos NT corpus renders Rom 3:25 as เครื่องบูชาไถ่บาป (a + b), with the (c) Levitical-mercy-seat layer carried by the thai_summary explanation (cross-references Lev 16, Yom Kippur).

### 1.2 The Hebrew etymological note

כַּפֹּרֶת derives from the root כפר ("to cover / atone / wipe away"). The same root produces:
- כִּפּוּר (kippur, "atonement" — as in יוֹם הַכִּפּוּרִים, Yom Kippur, "the Day of Atonements").
- כִּפֶּר (piel verb, "to atone / cover over sin").
- כֹּפֶר (kopher, "ransom / atonement payment").

The lock at พระที่นั่งกรุณา (mercy seat) does NOT erase the כפר-atonement etymology. The atonement layer is carried by:
- The Yom Kippur narrative at Lev 16 — the kapporet is where the high priest sprinkles blood once a year.
- The Rom 3:25 NT-side lock at เครื่องบูชาไถ่บาป — which carries the full atonement-cover semantics into the Pauline propitiation language.
- The Heb 9:5 NT-side lock at พระที่นั่งกรุณา — which retains the physical-object naming.

The OT Thai surface stays at พระที่นั่งกรุณา for consistency with Heb 9:5 + the 8-of-9 Exodus precedent at time of decision (40:20 the lone outlier).

---

## 2. Verse coverage

### 2.1 OT occurrences

The Hebrew kapporet appears ~27× in the OT, concentrated in:

| Cluster | References | Count |
|---|---|---|
| Exodus tabernacle blueprint + construction | Exod 25:17, 18, 19 (×2), 20 (×2), 21, 22; 26:34; 30:6; 31:7; 35:12; 37:6, 7, 8 (×2), 9 (×2); 39:35; 40:20 | 19 |
| Leviticus Yom Kippur ritual | Lev 16:2, 13, 14 (×2), 15 (×2) | 6 |
| Numbers narrative | Num 7:89 | 1 |
| Chronicles tabernacle reference | 1 Chr 28:11 | 1 |

All → พระที่นั่งกรุณา.

### 2.2 The Exodus 40:20 fix

End-of-book audit 2026-05-13 found EXO 40:20 shipped as "ที่ลบล้างบาป" (atonement-cover), creating an 8-to-1 within-book inconsistency. Normalized to พระที่นั่งกรุณา in the audit-revision commit.

### 2.3 NT cross-corpus references

| Verse | Greek | NT Thai lock | Sense |
|---|---|---|---|
| Rom 3:25 | ἱλαστήριον | เครื่องบูชาไถ่บาป | Christological propitiation (a + b) |
| Heb 9:5 | ἱλαστήριον | พระที่นั่งกรุณา | Physical tabernacle object (c) — same as OT kapporet |

---

## 3. Why this direction rather than the alternative

The audit-options included normalizing all 9 EXO occurrences to ที่ลบล้างบาป (the Geminian alternative — atonement-etymology surface). This was rejected for three reasons:

1. **NT alignment.** Heb 9:5 (the only NT explicit mention of the physical mercy-seat) locks to พระที่นั่งกรุณา, with explicit kd-rationale: "Thai distinguishes: tabernacle-cover = พระที่นั่งกรุณา; Christ-as-propitiation = เครื่องบูชาไถ่บาป (ROM 3:25 lock)". The OT side should follow the existing NT distinction.

2. **Existing corpus precedent.** 8 of 9 EXO occurrences (Exod 25:17 through 39:35) already shipped as พระที่นั่งกรุณา. Normalizing 8 to ที่ลบล้างบาป would be a 16-verse retroactive migration on top of the 1-verse fix — disproportionate to the corpus benefit.

3. **Thai church reception.** พระที่นั่งกรุณา is the classical Thai church term for the mercy seat; it carries the throne-above-the-cherubim imagery (cherubim with wings overshadowing → Heb 9:5's κατασκιάζοντα). ที่ลบล้างบาป is functional/descriptive but less anchored in Thai biblical-imagination tradition.

---

## 4. Implementation checklist

- [x] Exodus 40:20 normalized to พระที่นั่งกรุณา (verified 2026-05-13).
- [ ] Verify Leviticus 16 (the Yom Kippur narrative) uses the locked form at all 6 occurrences when Lev ships.
- [ ] Verify Num 7:89, 1 Chr 28:11 use the locked form when those books ship.
- [ ] Layer-2 footnote at first OT occurrence (Exod 25:17 / next book's first occurrence): brief survey of (a) the כפר etymology, (b) the Yom Kippur ritual context, (c) the Rom 3:25 + Heb 9:5 NT trajectory, (d) why Thai distinguishes the surface between OT/Heb-9:5 (physical object) and Rom 3:25 (Christological propitiation).

---

## 5. Change log

- **v0.1** (2026-05-13) — Initial lock, triggered by Exodus end-of-book audit on EXO 40:20. Tri-AI consensus: align with NT Heb 9:5 + the 8-of-9 EXO precedent. Distinct from the propitiation-Christology layer at Rom 3:25.
