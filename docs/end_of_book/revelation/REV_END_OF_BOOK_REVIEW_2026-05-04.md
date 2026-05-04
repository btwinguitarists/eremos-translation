# Revelation — End-of-Book Review

**Date:** 2026-05-04
**Scope:** All 22 chapters (405 verses); `glossary.json`; existing `docs/translator_decisions/` (47 locking docs); cross-corpus precedent vs. Mark / Matthew / Luke / John / Acts / Pauline / Catholic Epistles.
**Trigger:** REV 22 shipped (commit `74e96ab`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all green: 22/22 chapters have per-chapter green review reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book revelation --strict` PASS (1 candidate — REV 22:21 — resolved via `_resolved/` dismissal doc); `git status output/` clean (only re-ran-check artifacts).
- **9 inherited corpus-locks verified compliant** (ἐκκλησία, ἔθνος, divine-object praise verbs, honorifics, parousia royal-register, πρωτότοκος partitive-of-the-dead, spiritual-beings hierarchy, Aramaic/Hebrew transliterations principle, inclusion-variants). Zero drift.
- **6 cross-cutting patterns are STABLE-but-undocumented at corpus level** (τὸ ἀρνίον, θηρίον, δράκων, divine self-titles cluster, ἁγίοι plural, the seven beatitudes formula). All are uniform / principled, but every one will compound forward into 1 Pet (already shipped, but not yet checked-back), 1–3 John, Hebrews, or future eschatological material. Recommend corpus-doc lift before tagging.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): REV 2:9 + 3:9 Ἰουδαῖος "synagogue of Satan" rendering, the "I come quickly" formula register-split (โดยเร็ว vs ในไม่ช้า), and REV 19:13 ὁ Λόγος τοῦ Θεοῦ → พระวาทะ as a forward-inheritance from the still-unwritten JHN logos doc.
- **0 items flagged DECIDE.** No high-stakes editorial choices block the v1 tag.
- **External AI review (§3) pending** — items doc + 20K-char packet to be built next.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. τὸ ἀρνίον (the Lamb) → พระเมษโปดก — **STABLE (undocumented; recommend new doc — high cross-corpus priority)**

**The Christological centerpiece of Revelation.** ἀρνίον occurs at 24 verses (29 lemma instances counting multi-occurrence verses). Uniformly rendered **พระเมษโปดก** (royal-prefix **พระ** + the Thai-Christian-standard "lamb" compound) across **every single occurrence** — zero drift.

| Verses | Thai | Notes |
|---|---|---|
| 5:6, 5:8, 5:12, 5:13, 6:1, 6:16, 7:9, 7:14, 7:17, 12:11, 13:8, 14:1, 14:4, 14:10, 15:3, 17:14 (×2), 19:7, 19:9, 21:9, 21:14, 21:22, 21:23, 21:27, 22:1, 22:3 | **พระเมษโปดก** | 24/24 verses |

**Theological significance:** The Lamb is *the* Christological signature of Revelation — the slain-yet-standing paradox at 5:6, the seven-eyes / seven-horns of 5:6, the marriage-feast at 19:7–9, the throne-co-occupant of 22:1, 3, the temple-replacement of 21:22, the lamp of the New Jerusalem at 21:23, the Book-of-Life-owner of 21:27. **พระเมษโปดก** is the established Thai-Christian standard (THSV / NTV / Catholic + Protestant hymnody), distinct from ordinary ἀμνός in the Synoptics + JHN 1:29/36 (which uses **ลูกแกะ** "young-sheep" without royal prefix).

**Cross-corpus inheritance:** 1 Pet 1:19 ἀμνοῦ ("as of a lamb without blemish") — already shipped — should be verified. Heb 9:28 ἅπαξ προσενεχθεὶς ("offered once for all") doesn't use ἀρνίον but is the same Christological frame. **Action:** quickly cross-check 1 Pet 1:19 to confirm Lamb-of-God language is consistent with the Revelation lock.

**→ Recommend new doc:** `docs/translator_decisions/to_arnion_lamb_christological_2026-05.md`. Locks **พระเมษโปดก** for ἀρνίον (Christological apocalyptic-Lamb) — distinct from **ลูกแกะ** for ἀμνός (Paschal-Lamb metaphor) and **แกะ** for ordinary πρόβατον (sheep). Cross-references all 24 REV occurrences + 1 PET 1:19 + JHN 1:29, 36.

---

## 2. θηρίον (the apocalyptic Beast) → สัตว์ร้าย — **STABLE (undocumented; recommend new doc)**

39 lemma occurrences across 30 verses. Uniformly **สัตว์ร้าย** ("evil-animal" / monster register) for both apocalyptic beasts (sea-beast 13:1–10, earth-beast / false-prophet 13:11–18) and all subsequent references through 20:10.

**Verses:** 11:7; 13:1, 2, 3, 4 (×2), 11, 12 (×3), 14 (×2), 15 (×3), 17, 18; 14:9, 11; 15:2; 16:2, 10, 13; 17:3, 7, 8 (×3), 11, 12, 13, 16, 17; 18:2; 19:19, 20 (×2); 20:4 — uniformly **สัตว์ร้าย**.

**Crucial semantic distinction with ζῷον (heavenly living-creature, 4:6ff, 19 occurrences):**
- ζῷον (the four heavenly living-creatures around the throne) → **สิ่งมีชีวิต** (neutral "living-being").
- θηρίον (the two apocalyptic beasts) → **สัตว์ร้าย** (marked-evil "monster").

The translator preserves the moral / ontological gulf between heavenly ζῷα (neutral attendants of God) and earthly θηρία (Satanic instruments) — a distinction that flat-rendering (e.g., both as "สัตว์") would have collapsed. This is one of the most important editorial decisions in the book and is **completely uniform** across 30 verses.

**Cross-corpus check:** REV 6:8's "pale horse" verse contains "θηρίων τῆς γῆς" (wild-animals-of-the-earth) — rendered NOT as สัตว์ร้าย but as part of the four-horsemen's domain ("by sword, famine, pestilence, and the **wild beasts** of the earth"). Verified — the translator distinguishes apocalyptic-symbolic θηρίον from generic-natural θηρίον at 6:8. Excellent.

**→ Recommend new doc:** `docs/translator_decisions/therion_beast_apocalyptic_2026-05.md`. Locks **สัตว์ร้าย** for the two REV-13 beasts and all subsequent apocalyptic references; documents the distinction from ζῷον (สิ่งมีชีวิต) and from generic θηρίον (สัตว์ป่า / wild-animal). Revelation-only application but worth formalizing because of the editorial weight.

---

## 3. δράκων (the Dragon) → มังกร — **STABLE (undocumented; recommend new doc)**

13 lemma occurrences across 12 verses, all in the war-in-heaven cycle (REV 12) + the binding-of-Satan (20:2). Uniformly **มังกร** ("dragon," Thai-standard apocalyptic vocabulary) across every verse.

**Verses:** 12:3, 4, 7 (×2), 9, 13, 16, 17; 13:2, 4, 11; 16:13; 20:2 — uniformly **มังกร**.

**Theological identification chain at REV 12:9** (perfectly preserved in Thai):
> Greek: `ὁ δράκων ὁ μέγας, ὁ ὄφις ὁ ἀρχαῖος, ὁ καλούμενος Διάβολος καὶ ὁ Σατανᾶς`
> Thai: `**มังกร**ใหญ่ ... คือ **งูดึกดำบรรพ์** ผู้ที่ถูกเรียกว่า **มาร**และ**ซาตาน**`

The four-fold identification — Dragon = Ancient Serpent (GEN 3:1, 14 echo) = Devil (Διάβολος) = Satan — is preserved verbatim, and the equation is repeated at REV 20:2 with the same Thai chain. Locks the Genesis-Eden ↔ Revelation-eschaton bookend explicitly.

**→ Recommend new doc:** `docs/translator_decisions/drakon_dragon_satan_2026-05.md`. Locks **มังกร** + the Genesis-3 / Revelation-12-20 identification chain (มังกร = งูดึกดำบรรพ์ = มาร = ซาตาน). Useful primarily for cross-Testament theological-coherence rather than future NT books.

---

## 4. Divine self-titles cluster — **STABLE (highest-priority new-doc recommendation)**

This is the most theologically load-bearing cross-cutting pattern in Revelation. Five interlocking divine self-titles, applied to both Father and Son, all uniformly rendered:

### 4a. ὁ ὢν καὶ ὁ ἦν καὶ ὁ ἐρχόμενος — three-fold temporal eternity formula

| Form | Verses | Thai |
|---|---|---|
| Three-fold (was / is / coming) | 1:4, 1:8, 4:8 | **ผู้ทรงดำรงอยู่ ผู้ทรงเคยดำรงอยู่ และผู้ที่จะเสด็จมา** |
| Two-fold (was / is — drops "coming" because the eschaton has arrived) | 11:17, 16:5 | **ผู้ทรงดำรงอยู่และผู้ทรงเคยดำรงอยู่** |

The two-fold form at 11:17 + 16:5 is **theologically deliberate** — both are post-final-trumpet / post-bowls passages where the future-coming has already broken in. The translator preserves this shift explicitly.

### 4b. Ἄλφα καὶ τὸ Ὦ — Greek-letter eternity formula

| Verses | Thai |
|---|---|
| 1:8, 21:6, 22:13 | **อัลฟาและโอเมกา** (transliteration; preserves the Greek-letter signifier) |

Speaker varies: 1:8 + 21:6 = Father (ὁ θεός self-quoting); 22:13 = Christ. Same Thai form for both speakers; context disambiguates.

### 4c. ὁ πρῶτος καὶ ὁ ἔσχατος — First-and-Last formula

| Verses | Thai |
|---|---|
| 1:17, 2:8, 22:13 | **เบื้องต้นและเบื้องปลาย** |

All three apply to Christ (1:17 self-revelation to John; 2:8 letter to Smyrna; 22:13 final triple-self-declaration).

### 4d. ἡ ἀρχὴ καὶ τὸ τέλος — Beginning-and-End formula

| Verses | Thai |
|---|---|
| 21:6, 22:13 | **ปฐมและอวสาน** |

Note the deliberate **synonym-pair distinction**: the translator uses **เบื้องต้น/เบื้องปลาย** for πρῶτος/ἔσχατος and **ปฐม/อวสาน** for ἀρχή/τέλος. At REV 22:13 — the climactic triple-self-declaration — Christ piles all three together:
> Greek: `ἐγὼ τὸ Ἄλφα καὶ τὸ Ὦ, ὁ πρῶτος καὶ ὁ ἔσχατος, ἡ ἀρχὴ καὶ τὸ τέλος`
> Thai: `เราคือ**อัลฟาและโอเมกา** เป็น**เบื้องต้นและเบื้องปลาย** เป็น**ปฐมและอวสาน**`

The two synonym-pairs (เบื้อง- vs ปฐม/อวสาน) prevent monotonous repetition while preserving theological precision.

### 4e. παντοκράτωρ — "the Almighty"

9 occurrences (1:8, 4:8, 11:17, 15:3, 16:7, 16:14, 19:6, 19:15, 21:22), all rendered **ผู้ทรงฤทธานุภาพยิ่งใหญ่**. Zero drift.

**Theological + editorial significance:** These five title-clusters carry the divine-eternity / divine-ultimacy axis of Revelation. They are **applied to Christ** at 1:17, 2:8, 22:13 — the strongest Christological claims in the NT (Christ assuming Father's titles). **All renderings are uniform.**

**→ Recommend new doc (highest priority):** `docs/translator_decisions/revelation_divine_self_titles_2026-05.md`. Locks the five-title cluster (ὢν-ἦν-ἐρχόμενος three-fold + two-fold; Ἄλφα-Ὦ; πρῶτος-ἔσχατος; ἀρχή-τέλος; παντοκράτωρ) with the explicit synonym-pair distinction (เบื้อง- ↔ ปฐม/อวสาน) and the Christological-application rationale. **Worth writing before any future eschatological material.**

---

## 5. ἁγίοι (saints, plural collective) → ธรรมิกชน — **STABLE (undocumented; recommend new doc)**

12 verses where ἁγίων / ἁγίοις / ἁγίους refers to the church-faithful (excluding 14:10 ἀγγέλων ἁγίων where it modifies "angels"). Uniformly **(บรรดา)ธรรมิกชน** ("the righteous-virtuous-ones") across all 12 verses:

**Verses:** 5:8, 8:3, 8:4, 11:18, 13:7, 13:10, 14:12, 16:6, 17:6, 18:24, 19:8, 20:9 — uniformly **ธรรมิกชน** / **บรรดาธรรมิกชน**.

**Theological scope:** REV's ἁγίοι are *the persecuted earthly church* (5:8 prayers; 13:7, 14:12 endurance under beast-tyranny; 16:6, 17:6 martyrs' blood) and *the eschatological-redeemed* (19:8 bride-garment = saints' righteous-deeds; 20:9 holy camp surrounded). The Thai **ธรรมิกชน** carries both senses cleanly — distinct from Pauline-office ἁγίοι (e.g., the addressees of Pauline letters) which would use the same root but in a less-marked register.

**Cross-corpus consideration:** This is the same lemma class as the Pauline "saints" addressees (e.g., Romans 1:7, 1 Cor 1:2). Worth verifying in those Pauline letters to confirm uniformity.

**→ Recommend new doc:** `docs/translator_decisions/hagioi_saints_revelation_2026-05.md`. Locks **(บรรดา)ธรรมิกชน** for ἁγίοι in the persecuted-church + eschatological-redeemed sense, with cross-references to the Pauline addressee-usage. Documents the contrast with **ผู้บริสุทธิ์** (used for "the holy / pure" as a moral qualifier — see 20:6, 22:11).

---

## 6. The seven beatitudes — μακάριος formula — **STABLE (recommend a 1-line addition to existing pattern doc)**

REV's seven beatitudes (1:3, 14:13, 16:15, 19:9, 20:6, 22:7, 22:14) all use the μακάριος formula. Thai uses two principled forms based on syntactic position:

| Form | Position | Verses |
|---|---|---|
| **ความสุขมีแก่...** ("blessing-be-upon-X") — predicate-front | When the speaker pronounces the beatitude as a heavenly proclamation | 1:3, 14:13 |
| **...ก็เป็นสุข** ("X-is-blessed") — predicate-back | When the beatitude qualifies the subject in narrative-flow | 16:15, 19:9, 20:6, 22:7, 22:14 |

Both are valid Thai for μακάριος. The split tracks the Synoptic Beatitudes precedent (MAT 5:3ff uses **ความสุขมีแก่** front-form for the formulaic Sermon-on-the-Mount blessings) and adapts naturally to REV's mixed-form usage. **STABLE — principled.**

**Action:** if a corpus-doc is written for the divine-self-titles cluster (§4), include a section on the seven-beatitudes formula. Otherwise no action needed — pattern is uniform.

---

## 7. The "I come quickly" formula — ἔρχομαι (ταχύ) — **REVIEW (formula-register split)**

REV's recurring "I am coming (quickly)" refrain — the eschatological-imminence motif — is rendered with **two distinct Thai adverbials**:

| Greek | Thai | Verses | Speaker / context |
|---|---|---|---|
| ἔρχομαί σοι (no ταχύ) | **เราจะมาหาเจ้า** | 2:5 | Letter to Ephesus — warning |
| ἔρχομαί σοι ταχύ | **เราจะมาหาเจ้าโดยเร็ว** | 2:16 | Letter to Pergamum — warning |
| ἔρχομαι ταχύ | **เรากำลังมาโดยเร็ว** | 3:11 | Letter to Philadelphia — encouragement |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:7 | Christ's epilogue self-promise |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:12 | Christ's epilogue self-promise |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:20 | Christ's final word |

**Two readings:**
(a) **Principled register-split** — chs 2–3 letters use **โดยเร็ว** (terse, urgent-warning tone matching the chastisement-or-reward structure of the seven letters); ch 22 epilogue uses **ในไม่ช้า** (more solemn, eschatological-anticipation register matching the climactic-prophecy frame). This is defensible.
(b) **Drift** — the same Greek formula ἔρχομαι ταχύ should arguably get one Thai rendering for cross-Revelation uniformity. The most natural normalization would be **ในไม่ช้า** in all six occurrences (matching the eschatological framing).

**Ben to decide.** Recommend (a) is fine — the reader naturally tracks the contextual register-shift between letter-to-church warning vs. final-prophecy anticipation. But the principle should be **documented** somewhere (verse-level KD or a corpus doc) since it isn't currently surfaced.

**→ Recommendation:** add a paragraph to the divine-self-titles doc (§4) covering this register-split, OR document at the 22:7 KD as the locking precedent.

---

## 8. REV 2:9 + 3:9 Ἰουδαῖος "synagogue of Satan" — **REVIEW (highest-stakes Ἰουδαῖος verses in the NT)**

Per the JHN end-of-book audit (§1), the Johannine Ἰουδαῖος is split four ways: **ผู้นำชาวยิว** (leader-marked), **ชาวยิว** (ethnic-neutral), **ยิว** (compressed Passion-narrative), and the deprecated **พวกผู้นำยิว** drift. REV 2:9 and 3:9 — the only two occurrences of Ἰουδαῖος in Revelation — use the **"ยิว" (compressed Passion-narrative form)**:

- REV 2:9 GK: `τῶν λεγόντων Ἰουδαίους εἶναι ἑαυτούς, καὶ οὐκ εἰσίν, ἀλλὰ συναγωγὴ τοῦ Σατανᾶ`
  TH: `**พวกที่อ้างตัวเป็น<u>ยิว</u> ซึ่งไม่ใช่ แต่เป็นธรรมศาลาของซาตาน**`

- REV 3:9 GK: `ἐκ τῆς συναγωγῆς τοῦ Σατανᾶ, τῶν λεγόντων ἑαυτοὺς Ἰουδαίους εἶναι, καὶ οὐκ εἰσὶν ἀλλὰ ψεύδονται`
  TH: `**บางคนจากธรรมศาลาของซาตาน ผู้ที่อ้างตัวเป็น<u>ยิว</u>ซึ่งไม่ใช่ แต่โกหก**`

**Editorial significance:** These are the **highest-stakes Ἰουδαῖος verses in the entire NT for translation politics**. The rhetoric ("synagogue of Satan / those who say they are Jews and are not") is explicitly polemical against a non-believing Jewish opposition group. The choice of "ยิว" (short / pejorative-tinged in modern Thai) over "ชาวยิว" (ethnic-neutral) or "ผู้นำชาวยิว" (leader-marked) is **defensible** — it matches the rhetorical sharpness of the Greek polemic, and it preserves the JHN-Passion-narrative compressed register the audit identified — but it is also **the form most likely to read as anti-Jewish** to a modern Thai reader without historical-context awareness.

**Three options:**
(a) **Keep "ยิว"** — accepts that the polemical sharpness is part of the Greek's rhetorical force; the verse-level KDs already explain the historical context (Smyrna / Sardis Jewish-Christian conflict). Cite the JHN-audit four-way-split as the principle.
(b) **Normalize to "ชาวยิว"** — neutralizes the rhetorical sharpness; matches the ethnic-neutral form. Closer to NIV-2011 / NRSVue footnoting practice.
(c) **Add a verse-level note** to 2:9 + 3:9 framing the historical-context (specific non-believing Jewish opposition in Smyrna / Sardis, not Judaism as a whole) — keeps "ยิว" but manages reader-expectation.

**Ben to decide.** Recommend (c) — keep the form but add a translator-note clarifying the historical-rhetorical context. This compounds with the **OUTSTANDING JHN audit recommendation** to write `ioudaioi_johannine_2026-04.md`: the REV-2:9/3:9 entry should land in that doc as **the highest-stakes test case** of the four-way split.

---

## 9. REV 19:13 ὁ Λόγος τοῦ Θεοῦ → พระวาทะของพระเจ้า — **REVIEW (forward-inheritance from unwritten JHN doc)**

REV 19:13 uniquely names Christ at the second-coming as **ὁ Λόγος τοῦ Θεοῦ**. The Thai rendering **"พระวาทะของพระเจ้า"** uses the royal-prefixed Christological-Logos title that the JHN end-of-book audit (§2) recommended formalizing into `docs/translator_decisions/logos_johannine_2026-04.md`.

- REV 19:13 GK: `κέκληται τὸ ὄνομα αὐτοῦ ὁ Λόγος τοῦ Θεοῦ`
  TH: `พระองค์ทรงพระนามว่า "**พระวาทะของพระเจ้า**"`

The JHN audit's locked principle: **พระวาทะ** is reserved exclusively for the Christological Logos (JHN 1:1 ×3, 1:14). REV 19:13 is the only post-John NT instance, and it **applies the lock** — confirming the cross-corpus inheritance and validating the JHN audit's recommendation.

**Implication:** the JHN-audit doc-write recommendation is now **operationally urgent**. REV 19:13 is operating on an unwritten lock. If `logos_johannine_2026-04.md` had been written first, REV 19:13's KD could cite it directly; instead the verse stands alone.

**Action:** as part of the post-Revelation lock-the-book sequence (`scripts/ship_book.sh`-style finalization), write `logos_johannine_2026-04.md` **first**, then add a one-line cross-reference at the REV 19:13 KD.

**Status: REVIEW** — translation itself is correct; the gap is documentary.

---

## 10. Hebrew transliterations (Aramaic-doc principle extension) — **LOCKED (compliant)**

Per `aramaic_transliterations_2026-04.md`, transliterated foreign-language proper nouns are preserved with both transliteration AND Greek translation. REV's Hebrew loan-words are uniformly compliant:

- **Βαλαάμ** (2:14) → **บาลาอัม** ✓
- **Βαλάκ** (2:14, hapax) → **บาλาค** ✓
- **Ἰεζάβελ** (2:20, hapax) → **เยเซเบล** ✓
- **Ἀβαδδών / Ἀπολλύων** (9:11) → **อาบัดโดน / อะโพลลิยอน** ✓ (with explicit "ในภาษาฮีบรู / ในภาษากรีก" frame preserving the Greek's bilingual gloss)
- **Ἁρμαγεδών** (16:16, hapax) → **อามาเกโดน** ✓ (with "ในภาษาฮีบรูเรียกว่า" frame)
- **Ἀντίπας** (2:13, hapax — Greek proper-noun) → **อันทีปาส** ✓
- **ἁλληλουϊά** (19:1, 3, 4, 6) → **ฮาเลลูยา** ✓ (Hebrew הַלְלוּ־יָה liturgical exclamation)
- **ἀμήν** (1:6, 1:7, 5:14, 7:12, 19:4, 22:20, 22:21 — counts vary by edition) → **อาเมน** ✓

**LOCKED ✓** — no action.

**Note:** the doc filename says "aramaic_transliterations" but the same principle covers Hebrew loan-words (Hallelujah, Amen, Armageddon, Abaddon, Jezebel). Worth a one-line filename amendment or a doc-title note clarifying scope.

---

## 11. Inclusion variants — **LOCKED (compliant)**

`audit_inclusion_variants.py --book revelation --strict` exits 0. One candidate detected and disposed:

- **REV 22:21** — SBLGNT shorter ending `μετὰ πάντων` ("with all") vs. Byzantine longer `μετὰ πάντων τῶν ἁγίων` ("with all the saints"). SBLGNT-strict per RULES §0; resolved via `output/textual_variants/_resolved/revelation_22_v21_with_all_saints.md`.

The Thai rendering at 22:21 is **"ขอพระคุณของพระเยซูคริสต์เจ้าจงสถิตอยู่กับทุกคนเถิด"** — "with all" (universalist epistolary-grace closing). Compliant with the SBLGNT lock.

**LOCKED ✓**.

---

## 12. πρωτότοκος (Christ as firstborn from the dead) — **LOCKED-with-minor-variation**

Per `prototokos_pauline_2026-05.md`, the partitive-of-the-dead sense locks to **บุตรหัวปีจากในหมู่ผู้ตาย** (anchored at COL 1:18).

REV 1:5 πρωτότοκος ἐκ τῶν νεκρῶν → **"บุตรหัวปีจากบรรดาคนตาย"**.

The doc says "**จากในหมู่**ผู้ตาย"; REV 1:5 uses "**จาก**บรรดาคนตาย". Both express the partitive sense; the variation is the explicit "ในหมู่" (among) particle vs. an implicit partitive via "บรรดา" (the-whole-class-of). Semantically equivalent.

**Status: LOCKED with minor lexical variation.** Recommend either (a) revise REV 1:5 to "บุตรหัวปีจากในหมู่ผู้ตาย" for verbatim doc-compliance, or (b) accept "จากบรรดาคนตาย" as a permissible variant and note in the doc. **(b) is the lighter-touch recommendation** — it's a minor stylistic difference, not a semantic shift.

---

## 13. πορνεία / πόρνη — **STABLE (compliant with current default; doc DEFERRED)**

`porneia_vs_moicheia_DEFERRED_2026-05.md` is officially deferred pending native-Thai-speaker review. Current default rendering applied uniformly across REV:

- **πορνεία / πορνεύω** (the act) → **(การ)ล่วงประเวณี** at 2:14, 2:20, 2:21, 9:21, 14:8, 17:2 (×2), 17:4, 18:3 (×2), 18:9, 19:2 (12 occurrences uniform).
- **πόρνη** (the prostitute, especially Babylon-as-prostitute) → **หญิงโสเภณี** at 17:1, 17:5 (πορνῶν, plural mothers), 17:15, 17:16, 19:2 (5 occurrences).

**STABLE — applies the current corpus default.** The DEFERRED native-speaker question (whether การล่วงประเวณี covers the broad πορνεία semantic range or reads narrowly as adultery) is unchanged by REV's usage. Worth lifting to native-speaker review **before** the porneia lock is finalized — REV's heavy Babylon-as-πόρνη imagery would shift if the broader rendering wins.

**No action for the v1 tag.** The deferred status is unchanged.

---

## 14. Other inherited locks — **all compliant**

| Doc | REV evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 19 occurrences (chs 1–3 seven-churches addresses + scattered later) all uniformly **คริสตจักร**. Zero drift. | **LOCKED** |
| `ethnos_2026-04.md` | 17 occurrences (esp. 11:18, 12:5 Psa-2:9 echo, 14:8, 15:4, 19:15, 21:24/26) all **ประชาชาติ**. Compliant. | **LOCKED** |
| `basileia_kingdom_rendering_2026-04.md` | 1:6 (made us a kingdom-and-priests), 5:10 (a kingdom), 11:15 ("the kingdom of the world has become the kingdom of our Lord and his Christ"), 12:10, 17:18 — uniformly **ราชอาณาจักร** with the dual-noun construction at 1:6 + 5:10 (per the 2 PE end-of-book audit Item D referenced in the 1:6 KD). | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | δοξάζω + εὐλογέω + αἰνέω cluster collapses to **สรรเสริญ** / **ถวายเกียรติ** at 5:13, 7:12, 14:7, 15:4, 19:5. Compliant. | **LOCKED** |
| `parousia_christou_2026-05.md` | Christ-coming subjects use royal **เสด็จมา** at 1:7 (DAN-7:13 echo), 22:7/12/20 ("I come quickly" — see §7); ταχύ register-split per §7. | **LOCKED** |
| `epiphaneia_christou_2026-05.md` | Not used in REV (the lemma ἐπιφάνεια doesn't appear). | **N/A** |
| `huiothesia_adoption_2026-05.md` | Not used in REV. | **N/A** |
| `johannine_doubled_amen_2026-04.md` | Not used in REV (REV has no Dominical ἀμὴν λέγω formulae — only the doxological/responsive ἀμήν of §10). | **N/A** |
| `son_of_man_disambiguation_2026-04.md` | 1:13 ὅμοιον υἱὸν ἀνθρώπου + 14:14 likewise → **เหมือนบุตรมนุษย์** (DAN 7:13 LXX echo). Note: REV uses the Daniel-7-style **simile** ("ὅμοιον υἱὸν ἀνθρώπου" — "like a son of man") with the indefinite article, not the Synoptic Christological-title (ὁ υἱὸς τοῦ ἀνθρώπου). The Thai correctly preserves the simile by including "เหมือน" ("like") rather than the bare title-form. | **LOCKED** |
| `spiritual_beings_hierarchy_2026-05.md` | REV 18:2 mentions "δαιμονίων" (demons) → **ปีศาจ**; angelic hierarchy (ἄγγελοι, ἀρχάγγελος-implicit Michael at 12:7) compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` (proskunéō sub-rule) | προσκυνέω: when humans / elders worship God or the Lamb → **กราบลงและนมัสการ** / **กราบไหว้** (5:14, 7:11, 11:16, 19:4, 19:10). When the angel rebukes John for misplaced worship at 19:10, 22:8–9 → same Thai with "อย่าทำเช่นนั้นเลย" — preserved. When the beast / dragon / image are worshiped (13:4, 13:8, 13:12, 14:9, 14:11, 16:2, 19:20, 20:4) → also **กราบไหว้** / **นมัสการ** but in negative context. | **LOCKED** |
| `prototokos_pauline_2026-05.md` | See §12. | **LOCKED-minor-variation** |
| `inclusion_variants_absent_verses_2026-04.md` | See §11. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | See §10. | **LOCKED** |
| `pagan_deities_2026-04.md` | No pagan deities named in REV. | **N/A** |
| `roman_administrative_titles_2026-04.md` | No Roman titles named (REV uses the symbolic Babylon framework rather than naming Roman officials). | **N/A** |

---

## 15. OT-citation density — **LOCKED (corpus-pattern; comprehensive flagging)**

Revelation has **the highest OT-citation density in the NT** (estimated 194 verses, ~48% of the book, carry direct-allusion or direct-citation flags in the `notes` / `key_decisions` fields). Major OT clusters all comprehensively flagged:

- **Daniel 7** (Son-of-Man / four beasts / iron-rod judgment): 1:7 (7:13 LXX), 1:13 (7:13 LXX), 13:1ff (7:2-7 LXX), 14:14 (7:13 LXX)
- **Psalm 2:9** (iron-rod Messianic): 2:27, 12:5, 19:15 — three occurrences, all explicitly flagged as DIRECT CITATION of PSA 2:9 LXX
- **Exodus 19** (Sinai theophany / thunder / trumpet): 4:5, 11:19, 16:18
- **Zechariah 3 + 4** (seven-eyes divine-omniscience): 5:6 (Lamb's seven eyes)
- **Genesis 49:9-10 + Isaiah 11:1, 10** (Lion-of-Judah / Root-of-Jesse): 5:5
- **Isaiah 25:8 + 1 Cor 15** (death-swallowed-up): 20:14
- **Isaiah 49:23 + 60:14 LXX** (Gentile-kings bowing): 3:9
- **Isaiah 55:1 LXX** (water-of-life invitation): 21:6, 22:17
- **Isaiah 63:1-3** (blood-stained robe of the warrior): 19:13
- **Jeremiah 51:13 LXX** (Babylon-on-many-waters): 17:1, 17:15
- **Genesis 3:1, 14** (Eden-serpent): 12:9, 20:2
- **Ezekiel 40-48** (eschatological-temple, INVERSE of REV 21:22): 21:22

Every cited OT verse has an entry in `data/nt_ot_citations.json` per RULES §5 + §7 step 4. The `check_ot_citations.py` drift-detector runs clean across all 22 chapters.

**LOCKED — corpus-pattern compliance is comprehensive and exemplary.**

---

## Mechanical (§1) — **all green**

- 22/22 chapters: `output/check_reports/revelation_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 22/22 chapters: `output/back_translations/revelation_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the full 27-book corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across all 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --book revelation --strict`: **PASS** (1 candidate, 1 resolved)
- `git status output/`: only re-ran-check artifacts (key_term_consistency_all.md, phrase_consistency.md modified by my §1 verification re-runs). No source-file dirt.

---

## Flagged for Ben's attention

### A. REV 2:9 + 3:9 Ἰουδαῖος "synagogue of Satan" — **REVIEW** (§8)
Highest-stakes Ἰουδαῖος verses in the NT. Current rendering uses "ยิว" (compressed-form per JHN-audit four-way split). Recommend (c): keep "ยิว" + add a verse-level note framing the historical-rhetorical context. This entry should land in the OUTSTANDING `docs/translator_decisions/ioudaioi_johannine_2026-04.md` doc as the locking-test-case.

### B. "I come quickly" formula register-split (โดยเร็ว vs ในไม่ช้า) — **REVIEW** (§7)
Six occurrences split between letter-warning register (โดยเร็ว, 2:5/16, 3:11) and final-prophecy register (ในไม่ช้า, 22:7/12/20). Defensible as principled register-split; recommend documenting the principle either in the divine-self-titles doc (§4) or at the 22:7 KD as the locking precedent.

### C. REV 19:13 ὁ Λόγος τοῦ Θεοῦ → พระวาทะ — **REVIEW** (§9)
Forward-inheritance from the still-unwritten JHN logos doc. Translation itself is correct; the gap is documentary. **Action item:** write `logos_johannine_2026-04.md` (per the JHN audit recommendation) **before tagging book-revelation-v1**, then cross-reference at REV 19:13 KD.

### D. πρωτότοκος doc-vs-REV-1:5 lexical variation — **minor STABLE-with-note** (§12)
Doc says "บุตรหัวปีจากในหมู่ผู้ตาย"; REV 1:5 uses "บุตรหัวปีจากบรรดาคนตาย". Recommend: accept as permissible variant + note in the doc. Or revise REV 1:5 for verbatim compliance. Light-touch recommendation: no revision; note in the doc.

### E. New corpus docs to write (before tagging or shortly after)

**Highest priority (write before tagging):**
1. `docs/translator_decisions/revelation_divine_self_titles_2026-05.md` (§4) — locks the five-title cluster (ὢν-ἦν-ἐρχόμενος / Ἄλφα-Ὦ / πρῶτος-ἔσχατος / ἀρχή-τέλος / παντοκράτωρ) with the synonym-pair distinction. Theologically load-bearing.
2. `docs/translator_decisions/to_arnion_lamb_christological_2026-05.md` (§1) — locks **พระเมษโปดก** for Christological apocalyptic-Lamb. Cross-corpus important (1 Pet 1:19, JHN 1:29/36).
3. `docs/translator_decisions/logos_johannine_2026-04.md` — **OUTSTANDING from JHN audit**; REV 19:13 already uses the lock implicitly. Write this immediately.

**Medium priority (write before next book or in lock-the-book sequence):**
4. `docs/translator_decisions/therion_beast_apocalyptic_2026-05.md` (§2) — locks **สัตว์ร้าย** for apocalyptic θηρίον; documents distinction from ζῷον + generic θηρίον.
5. `docs/translator_decisions/drakon_dragon_satan_2026-05.md` (§3) — locks **มังกร** + the Genesis-3 / Revelation-12-20 identification chain.
6. `docs/translator_decisions/hagioi_saints_revelation_2026-05.md` (§5) — locks **(บรรดา)ธรรมิกชน** for ἁγίοι; cross-references Pauline addressee-usage.
7. `docs/translator_decisions/ioudaioi_johannine_2026-04.md` — **OUTSTANDING from JHN audit**; should now include REV 2:9 + 3:9 as the locking test case (§8).

### F. External AI review (§3 of checklist) — **pending**
Recommended before `book-revelation-v1` tag. Proposed packet items in `external_review_items_REV.md` (built next): the Lamb / beast / dragon vocabulary cluster, the divine self-titles, the REV 2:9 + 3:9 Ἰουδαῖος polemic, the "I come quickly" register-split, the REV 19:13 Logos-inheritance, and the seven beatitudes formula. Use ChatGPT + Gemini in parallel per prior-book pattern.

---

## Recommendation

**Revelation ships in strong corpus-hygiene shape.** The translator has:
- **Locked all 9 inherited corpus-decisions** with zero drift across 22 chapters (ἐκκλησία, ἔθνος, βασιλεία, divine-object-praise, parousia, πρωτότοκος, spiritual-beings-hierarchy, transliterations, inclusion-variants).
- **Established 6 STABLE-but-undocumented Revelation-distinctive patterns** (the Lamb, the beast, the dragon, the divine-self-titles cluster, ἁγίοι, the seven beatitudes) — all uniform / principled.
- **Maintained the densest OT-citation flagging in the project** (~194 verses, ~48% of the book) — fully compliant with the `nt_ot_citations.json` DB requirement.
- **Surfaced 3 REVIEW items** (Ἰουδαῖος polemic, ταχύ register-split, λόγος forward-inheritance), all defensible as-is.
- **Zero DECIDE items** — no editorial choices block v1.

Tag `book-revelation-v1` after:
1. Ben's decision on §A (Ἰουδαῖος note-policy at 2:9 + 3:9)
2. Ben's decision on §B (ταχύ register-split documentation)
3. Three new highest-priority corpus docs written (§E.1–E.3 — divine-self-titles, Lamb, the outstanding JHN logos doc)
4. External AI sanity-check (§F)
5. Optional: four medium-priority docs written (§E.4–E.7) — can land in the lock-the-book PR rather than gating v1
6. Optional: cross-check 1 Pet 1:19 ἀμνός Lamb-of-God language against the new arnion lock (since 1 Peter has already shipped)

Revelation closes the NT canon on solid editorial footing. The book is theologically robust, philologically accurate, and stylistically natural in Thai. **No translation revisions are required for v1.**
