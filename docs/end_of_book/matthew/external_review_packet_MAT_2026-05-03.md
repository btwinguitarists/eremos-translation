# Matthew — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Matthew** (28 chapters, 1,068 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Philemon, Philippians, Romans complete + tagged. Matthew 28/28 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

### Already-locked corpus decisions — DO NOT re-litigate

- ἐκκλησία (Christian community) → คริสตจักร; secular/OT assembly → ที่ประชุม
- βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only)
- ἄφεσις ἁμαρτιῶν → การยกโทษบาป; ἄφεσις (release) at LUK 4:18 → ปลดปล่อย
- narrator-voice ὁ κύριος (= Jesus) → องค์พระผู้เป็นเจ้า (Luke-Acts signature)
- vocative Κύριε from disciples/believers → องค์พระผู้เป็นเจ้า; from outsiders → context
- παρρησιάζομαι → อย่างกล้าหาญ
- δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default)
- honorifics ราชาศัพท์ for divine subjects + kings (Herod, Agrippa); plain register for governors (Felix, Festus) + non-divine human authorities
- pagan deities → เทพ / เทพี / เทพเจ้า (NEVER พระเจ้า, reserved for the biblical God)
- μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering)
- οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after possessor); ท้องฟ้า (meteorological)
- ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์
- ὁ υἱὸς τοῦ ἀνθρώπου (Christological title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์
- Greek historic-present verbs → Thai past tense (do not preserve present morphology)
- ἀμὴν λέγω ὑμῖν (Synoptic single) → เราบอกความจริงแก่พวกท่าน(ว่า)
- ἀμὴν ἀμὴν λέγω ὑμῖν (Johannine doubled, 25× in John) → อาเมน อาเมน เราบอกแก่พวกท่านว่า — Aramaic-embed treatment
- μονογενὴς θεὸς (JHN 1:18) → พระบุตรองค์เดียวผู้ทรงเป็นพระเจ้าด้วย — exception to standard μονογενής → องค์เดียว lock for the compound
- Aramaic embeds (Talitha cumi, Ephphatha, Abba, etc.) → preserve Thai-script transliteration AND Mark's own Greek translation
- Inclusion-variant Path A (LOCKED): Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧` — matches BSB/ESV/NIV/CSB
- Parable characters representing God (fathers, kings, masters, judges) → human register, never ราชาศัพท์
- Narrator introducing adversary speech to Jesus → ทูล (preserves Jesus's divine status regardless of speaker)
- ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group, incl. Israel) / คนต่างชาติ (Gentiles, mission target)
- Roman titles: χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ
- Pagan-deity personal names → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม)

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Greek + Thai shown.

### What we are NOT asking for

- Don't propose stylistic alternatives "for variety." Consistency in key terms is a feature.
- Don't flag things from the locked-decisions list above. Those are settled.
- Don't suggest re-rendering specific verses for taste. Native Thai reviewers handle stylistic feedback.
- Don't comment on per-chapter automated-check coverage — those all pass.

### Output format

For each item below, return:

```
## [Item letter]: [Short title]
**Verdict:** FINE / CONCERN / MAJOR CONCERN
**Reasoning:** [1-3 sentences citing verses]
**Recommended action:** [specific — "lock as-is", "spot-revise verse X", "write doc Y", or "Ben to decide"]
```

Then a brief **§Z: Anything else?** section if you spot a corpus-level concern outside these items.

---
## Item A — ἐκκλησία → คริสตจักร: church-vs-assembly disposition (Matt 16:18; 18:17)

**The pattern.** Matthew has the only ἐκκλησία occurrences in the Gospels (16:18; 18:17). Eremos renders both **คริสตจักร** ("Christian-church"), not the more semantically-neutral **ที่ประชุม** / **ชุมนุม** ("assembly, gathering").

| Verse | Greek | Thai | Speech context |
|---|---|---|---|
| 16:18 | ἐπὶ ταύτῃ τῇ πέτρᾳ οἰκοδομήσω μου τὴν **ἐκκλησίαν** | บนศิลานี้เราจะสร้าง**คริสตจักร**ของเรา | Jesus to Peter at Caesarea Philippi |
| 18:17 | ἐὰν δὲ καὶ τῆς **ἐκκλησίας** παρακούσῃ … εἰπὲ τῇ **ἐκκลησίᾳ** | ถ้าเขาไม่ฟัง**คริสตจักร**ด้วย ก็จงบอก**คริสตจักร** | Jesus on church discipline |

**Counter-argument (raised during Matthew audit):** คริสตจักร carries post-Pentecost institutional connotations. Jesus at 16:18/18:17 speaks proleptically — the institutional Church didn't exist yet at the narrative-time of the saying. ที่ประชุม / ชุมนุม would better preserve the pre-institutional semantic range while remaining intelligible to Thai readers.

**Argument for the lock:** Thai-Christian readers expect **คริสตจักร** at 16:18 — it's the proof-text for ecclesiology in nearly every Thai Protestant and Catholic catechism. Choosing ที่ประชุม at 16:18 would read as Eremos editorially weakening a doctrinal anchor. The corpus-precedent weight is also massive: Acts 23×, Pauline 60×, Hebrews + General Epistles + Revelation. Forcing ที่ประชุม at the two Matthean Gospel-occurrences and then switching to คริสตจักร in Acts would be the worst of both worlds.

**Forward implication.** Determines the rendering of:
- ἐκκλησία θεοῦ (1 Cor 1:2; 10:32; 11:22; 15:9; Gal 1:13; 1 Thess 2:14)
- αἱ ἐκκλησίαι τῶν ἐθνῶν (Rom 16:4)
- The seven Rev 2–3 letter-recipients
- Acts 19:32, 39, 41 — the SECULAR ἐκκλησία (Ephesian civic-assembly, definitively NOT a Christian church)

The Acts 19 secular usages will need a non-Christian rendering (likely **ที่ประชุม**) — meaning the corpus carries a Christian-vs-secular semantic split for the same Greek lemma.

**Two questions:**
1. Is Matt 16:18 / 18:17 → คริสตจักร the right disposition for the Gospel-occurrences (where Jesus speaks proleptically), or does the proleptic-context warrant the more neutral ที่ประชุม / ชุมนุม even at the cost of breaking with Thai-Christian reader-expectation?
2. The Acts 19 secular ἐκκλησία occurrences will need a non-Christian rendering. Is a Christian-vs-secular split (คริสตจักร / ที่ประชุม) the principled disposition, or should the ENTIRE corpus default to ที่ประชุม with a `thai_summary` explanation that translates "Christian assembly" → "Christian church" interpretively?

---

## Item B — μετανοέω vs μεταμέλομαι: 21:29 / 21:32 vs 27:3 drift

**The drift.** Matthew has both μετανοέω (5×, salvific-conversion) and μεταμέλομαι (3×, narrower "remorse / change-of-mind"). The current Thai handling is internally inconsistent:

| Verse | Greek | Thai | Distinct from μετανοέω? |
|---|---|---|---|
| 3:2, 4:17, 11:20–21, 12:41 (5×) | μετανοέω | **กลับใจ(ใหม่)** | (canonical salvific) |
| 21:29 (the son who first refuses then changes mind) | μεταμέλομαι | **กลับใจ** | NO |
| 21:32 (priests/elders did not μεταμελήθητε) | μεταμέλομαι | **ไม่กลับใจ** | NO |
| 27:3 (Judas — μεταμεληθεὶς) | μεταμέλομαι | **เสียใจ** | YES |

The 21:29 per-verse rationale admits: "μεταμέλομαι narrower 'remorse/reconsidering' **but Thai does not distinguish readily**." Yet 27:3's rationale says: "CRUCIAL: this is NOT μετανοέω … preserves the Matthean theological distinction."

**Both rationales cannot be right** — 21:29 and 27:3 use the same Greek verb. Either Thai distinguishes (and 21:29/21:32 should be revised), or it doesn't (and 27:3 should match the others as กลับใจ).

**Doctrinal stakes.** 2 Cor 7:10 is the locus classicus for the μετάνοια vs μεταμέλεια contrast — "godly grief produces μετάνοιαν unto salvation," "worldly grief produces death." If Matthew's corpus is internally inconsistent, the 2 Cor 7:10 anchor (and the Heb 7:21 + 12:17 references) become harder to land cleanly.

**Recommendation from internal audit:** REVISE. Change 21:29 and 21:32 to **เปลี่ยนใจ** (change-of-mind, non-salvific) to match the 27:3 distinction. Write `metanoeo_vs_metamelomai_2026-04.md` documenting the rule.

**Two questions:**
1. Is the proposed 21:29/21:32 → **เปลี่ยนใจ** revision the right move, or does Thai's natural lexical inventory not support a clean three-way distinction (salvific-conversion / change-of-mind / regret-only) and the project should accept conflation between any two of the three?
2. Does the contrast actually carry across the entire Greek corpus consistently, or are there NT μεταμέλομαι occurrences (e.g., 2 Cor 7:8 — Paul's own non-salvific "regret" of having sent the letter) where the lexical distinction doesn't function in the same way and the Thai rendering should be context-sensitive rather than lemma-locked?

---

## Item C — βασιλεία τῶν οὐρανῶν vs τοῦ θεοῦ: Matthean signature

**The pattern.** Matthew uses βασιλεία τῶν οὐρανῶν 51× (the "kingdom of the heavens" — Matthean signature reverential periphrasis) but slips to βασιλεία τοῦ θεοῦ at 12:28 and 21:43 (2×). Eremos preserves the Greek variation rather than flattening it:

| Greek | Verses | Thai |
|---|---|---|
| τῶν οὐρανῶν | 51× across Matthew | **อาณาจักรสวรรค์** ("heavenly kingdom") |
| τοῦ θεοῦ | 12:28, 21:43 | **อาณาจักรของพระเจ้า** ("kingdom of God") |

The 51-vs-2 split is widely understood as Matthew's *kal vahomer* — when he wants the standard expression he uses τῶν οὐρανῶν (reverential periphrasis around the Tetragrammaton-substitute "heaven"); when he wants emphasis, he reaches for τοῦ θεοῦ. Eremos preserves both.

**The corpus-tension.** Mark uses τοῦ θεοῦ exclusively (15×). Luke uses τοῦ θεοῦ exclusively (32×). John uses τοῦ θεοῦ (3:3, 3:5) but it's relatively rare. The Pauline corpus uses τοῦ θεοῦ exclusively. So Matthew is the only NT book that has both, and the Eremos disposition treats his variation as load-bearing.

**The reader-experience question.** Thai readers cycling through Matthew → Mark → Luke will see:
- Matthew: dominant **อาณาจักรสวรรค์**, occasional **อาณาจักรของพระเจ้า**
- Mark + Luke: only **อาณาจักรของพระเจ้า**

For a Thai reader who memorizes Matt 12:28 ("if I cast out demons by the Spirit of God, then the kingdom of God has come upon you"), the variation appears at a load-bearing pneumatology / eschatology moment. Preserving the Greek's lexical signal here matters.

**Two questions:**
1. Is Matthew's 51-vs-2 distinction load-bearing enough to warrant the Thai preservation, or does Thai's Buddhist-Hindu-influenced cosmology of "สวรรค์" (heaven, plural devalokas) introduce semantic noise that flattens the periphrastic-reverence point Matthew is making? Would a single Thai default for all Synoptics + alone preserve the inter-Synoptic readability?
2. The Pauline corpus uses βασιλεία τοῦ θεοῦ exclusively (1 Cor 4:20; 6:9–10; 15:50; Rom 14:17; Gal 5:21; Col 4:11; 2 Thess 1:5). Does the Thai สวรรค์-vs-พระเจ้า distinction cause a discernible inter-corpus inconsistency for Thai readers (Matthew has both → Pauline has only one), and is that consistent with the Greek's own pattern or does it overstate the Greek-side variation?

---

## Item D — Inclusion-variant treatment: 17:21 / 18:11 silent-skip vs 23:14 bracketed

**The inconsistency.** RULES.md §5 specifies single-brackets `[...]` for inclusion variants where mainstream traditions include but SBLGNT omits. The general practice in Matthew is:

**Bracketed (correctly):** 5:22 [โดยไม่มีเหตุ], 5:44 [longer love-enemies clause], 6:13 [doxology — "for thine is the kingdom..."], 6:15, 6:33, 15:6, 25:14.

**Inconsistent cases:**

| Verse | Treatment | Issue |
|---|---|---|
| 17:21 (about prayer-and-fasting) | **verse absent** (no JSON key — silent-skip) | No reader-visible marker; Thai pastors expecting it find nothing |
| 18:11 ("Son of Man came to save the lost") | **verse absent** (silent-skip) | Same |
| 23:14 (woe to scribes — devouring widows' houses) | **bracketed as whole verse** | Reader-visible |
| 16:2b–3 (red-sky / weather-signs) | included unmarked | Note says "omitted in earliest witnesses" but no bracket |
| 21:44 ("on whom this stone falls, it grinds him to powder") | included unmarked | Note flags SBLGNT inclusion + D/Old-Latin omits |

**The 17:21 / 18:11 silent-skip vs 23:14 bracketed-include is the core inconsistency.** Per RULES.md §5 rationale ("silent omission reads as editorial overreach"), 17:21/18:11 should either (a) appear as bracketed-included verses (consistent with 23:14) OR (b) 23:14 should also be silently skipped (consistent with 17:21/18:11).

**Forward implication.** Sets the template for:
- Mark 16:9–20 (already done — Tier 3 ⟦double-brackets⟧)
- Acts 8:37 (Ethiopian eunuch's confession of faith, absent in earliest witnesses)
- Acts 15:34 (Silas remained at Antioch, absent in earliest witnesses)
- Rom 16:24 (grace-formula doublet)
- 1 John 5:7–8 (Johannine Comma)

Each of these will need a clear principled disposition.

**Two questions:**
1. Should the Matthew corpus revise 17:21 and 18:11 to bracketed-included verses (matching 23:14's treatment), or revise 23:14 to silent-skip (matching 17:21/18:11), or articulate a principled criterion for when each is appropriate (e.g., bracket when the variant content is doctrinally interesting; silent-skip when it's a duplication-by-harmonization with no independent content)?
2. The Johannine Comma (1 John 5:7–8) is the single most-disputed inclusion-variant in the entire NT and the Thai Trinitarian-doctrine landscape regards it as a load-bearing proof-text. Should Eremos pre-decide its treatment NOW (Tier 3 ⟦double-brackets⟧ with extended note? bracket + footer? silent-skip?) so the disposition is principled-by-policy rather than ad-hoc-by-the-time-1-John-ships?

---

## Item E — ἀμὴν λέγω ὑμῖν: minor drift at 5:18, 5:26, 13:17

**The Markan-anchor lock.** Per `amen_saying_formula_2026-04.md`, ἀμὴν λέγω ὑμῖν renders uniformly as **เราบอกความจริงแก่พวกท่าน(ว่า)** across all synoptic occurrences.

**Matthew's 20 occurrences include 17 that match the lock and 3 that drift:**

| Verse | Current Thai | Issue |
|---|---|---|
| 5:18 | "เราบอกพวกท่านตามจริง" | Word order inverted — adverbial **ตามจริง** instead of nominal **ความจริง** |
| 13:17 | "เราบอกพวกท่านตามจริง" | Same inversion |
| 5:26 | "เราบอกท่านตามจริง" | Same inversion + σοι singular variant ("ท่าน" not "พวกท่าน") |

The drift introduces a 3-form rather than 2-form ใช้-pattern (with the σοι singular), making the synoptic-lock not actually fully synoptic.

**Recommendation from audit:** REVISE 5:18, 13:17, 5:26 to the Markan-locked form before `book-matthew-v1` final tag. 3-line edit. Alternative: update Mark's decision-doc to permit the **ตามจริง** adverbial variant — but that's inconsistent with the rationale that lemmatized **ความจริง** for the Markan lock in the first place.

**Two questions:**
1. Should the 3 drift verses be revised to the Markan lock (mechanical alignment, low cost) or should the Markan decision-doc be relaxed to permit **ตามจริง** as an equally valid rendering (preserving any Matthean nuance the translator may have intended)?
2. The σοι singular at 5:26 (vs ὑμῖν plural at 5:18, 13:17, etc.) is a real Greek difference — Jesus addressing the singular "you" (the accused person at the courthouse step). Is "ท่าน" (singular) the right Thai marker, or should Thai distinguish more strongly (e.g., "ท่านผู้นี้") to preserve the Greek's number-shift?

---

## Item F — Aramaic / foreign-name transliterations: Matthean extensions of the Markan pattern

**The pattern.** Matthew extends the Markan "transliterate-then-gloss" rule (Item E in the Mark packet) with new occurrences:

| Verse | Greek | Thai | Treatment |
|---|---|---|---|
| 1:23 | Ἐμμανουήλ | **อิมมานูเอล** | + gloss "พระเจ้าทรงสถิตกับเรา" (Matthew's own translation) |
| 5:22 | Ῥακά (HAPAX) | **‹ราคา›** | Single-guillemet marks foreign-word-untranslated |
| 6:24 | μαμωνᾷ | **เงินทอง** | NOT transliterated — semantic rendering ("money / wealth") |
| 27:33 | Γολγοθᾶ | **กลโกธา** | + gloss "สถานที่กะโหลกศีรษะ" (Matthew's own translation) |
| 27:46 | Ἠλὶ ἠλὶ λεμὰ σαβαχθάνι | **เอลี เอลี เลมา ซาบัคทานี** | + gloss "พระเจ้าของข้าพระองค์ พระเจ้าของข้าพระองค์ ทำไมพระองค์ทรงทอดทิ้งข้าพระองค์?" |

**The 6:24 outlier.** μαμωνᾷ is the only Aramaic-loanword in Matthew rendered semantically (เงินทอง = "money/wealth") rather than transliterated. This is principled — μαμωνᾷ is a "personification of wealth" rhetorical device, not a foreign-place-name or proper-noun-of-Person; semantic rendering preserves the rhetorical force where transliteration would mystify Thai readers (compare KJV's "mammon" → Thai readers' incomprehension).

**The 5:22 ‹guillemet› device.** Ῥακά is a HAPAX (used only at 5:22 in the entire NT). The single-guillemet mark **‹ราคา›** is a special device that preserves the foreign-word-untranslated effect — the speaker's contemptuous foreign-curse retains its alienating force. The device doesn't appear elsewhere in Matthew; its single-use status makes its principled status uncertain.

**Two questions:**
1. Is the 6:24 μαμωνᾷ → semantic rendering (**เงินทอง**) the right principled exception to the transliterate-then-gloss default, or should μαμωνᾷ also be transliterated (**มัมโมนา**) to preserve the rhetorical-personification of wealth-as-rival-deity that Jesus is making? The Greek nuance is that μαμωνᾷ is treated AS A NAME — a personified rival to God — not just as the abstract noun "wealth."
2. The 5:22 ‹guillemet› device for Ῥακά is a one-off. Should Eremos pre-decide whether the device extends to other foreign-words-in-direct-speech (e.g., Acts has multiple) or treat ‹...› as Matthew-only and use a different convention elsewhere?

---

## Item G — παρουσία → การเสด็จมา: Christological lock + human-παρουσία forward implication

**The pattern.** Matthew uses παρουσία 4× (24:3, 24:27, 24:37, 24:39). All 4 render uniformly **การเสด็จมา** — using royal-register **เสด็จ** because Son of Man is the subject in every case.

| Verse | Greek context | Thai |
|---|---|---|
| 24:3 | τί τὸ σημεῖον τῆς σῆς **παρουσίας** | สัญญาณแห่ง**การเสด็จมา**ของพระองค์ |
| 24:27 | οὕτως ἔσται ἡ **παρουσία** τοῦ υἱοῦ τοῦ ἀνθρώπου | **การเสด็จมา**ของบุตรมนุษย์ก็จะเป็นเช่นนั้น |
| 24:37 | οὕτως ἔσται ἡ **παρουσία** τοῦ υἱοῦ τοῦ ἀνθρώπου | (same form) |
| 24:39 | οὕτως ἔσται ἡ **παρουσία** τοῦ υἱοῦ τοῦ ἀνθρώπου | (same form) |

The Christological-eschatological lock is principled — Son-of-Man's parousia is royal-arrival language; Thai's **การเสด็จมา** carries the same royal register that the Greek's idiom for divine-or-imperial advent carried.

**The forward problem.** The Pauline corpus uses παρουσία in BOTH senses:
- **Christ's parousia** (1 Thess 2:19; 3:13; 4:15; 5:23; 2 Thess 2:1, 8; 1 Cor 15:23) → should match Matt 24's **การเสด็จมา**
- **Human παρουσία** — non-eschatological visit/arrival of human persons (1 Cor 16:17 — Stephanas; 2 Cor 7:6–7 — Titus; Phil 1:26 — Paul himself; Phil 2:12) → **การเสด็จมา** would over-honorific the human visitors

PHP 1:26 in particular is a flagged corpus-issue: Paul calling his own future visit παρουσία doesn't carry royal/eschatological weight. Forcing **การเสด็จมา** there would over-translate; using **การมา** (plain "arrival") opens a wedge that may bleed into the Christological occurrences if not principled.

**Two questions:**
1. Should the corpus pre-decide a 2-way Thai split for παρουσία (royal **การเสด็จมา** for Christ-subject + plain **การมา** / **การมาเยี่ยม** for human-subject), or is the subject-driven split itself unprincipled (the Greek lemma is the same; subject-sensitivity is a Thai-side imposition)?
2. The PHP 2:12 παρουσίᾳ is borderline — Paul's "presence" (not arrival) with the Philippians, ablative-temporal. Does the Christ-vs-human split apply, and which Thai disposition handles "presence" rather than "arrival" semantics cleanly?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
