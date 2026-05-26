# 2 Chronicles — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **2 Chronicles** (36 chapters, 822 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). 2 Chronicles 36/36 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
- Tetragrammaton יהוה → องค์พระผู้เป็นเจ้า (NT-aligned per divine_names_table_2026-05.md); אֱלֹהִים → พระเจ้า; שַׁדַּי → ผู้ทรงมหิทธิฤทธิ์
- First-occurrence-per-chapter Tetragrammaton convention footer note in output/textual_variants/<book>_<chapter>.json (Layer 2)
- OT register: ราชาศัพท์ ทรง- on verbs whose subject is the divine person; plain verb when subject is a divine body part (e.g., יַד יהוה)
- Pagan deities (foreign אֱלֹהִים, plural-of-Moabite-gods, Baal/Asherah/etc.) → พระทั้งหลาย / เทพ — NEVER พระเจ้า (reserved for YHWH/true God)
- חֶסֶด (covenant loyal-love, Ruth 1:8 lock) → ความรักมั่นคง
- גֹּאֵל (kinsman-redeemer) → ญาติผู้ไถ่; גָּאַל / גְּאֻלָּה family verbs → ไถ่ / สิทธิ์ในการไถ่
- Hebrew oath formulas: כֹּה יַעֲשֶׂה יהוה ... וְכֹה יֹסִיף → ขอองค์พระผู้เป็นเจ้าทรงลงโทษ ... และให้หนักยิ่งกว่านั้นอีก; חַי־יהוה → ตราบใดที่องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่
- Hebrew anthropomorphism for YHWH's body parts: royal-Thai พระหัตถ์ / พระเนตร / พระโอษฐ์ / พระบาท (matches Rachasap when divine possessor)
- אֵשֶׁת חַיִל / אִישׁ גִּבּוֹר חַיִל (Ruth 2:1 + 3:11 mirrored pair) → ชายผู้มีฐานะมั่งคั่งและทรงเกียรติ / หญิงผู้ทรงคุณธรรมและทรงเกียรติ
- Hebrew jussive prayer-blessings (יְבָרֶכְךָ יהוה, יִתֵּן יהוה, etc.) → Thai ขอ-...ทรง- + verb (royal-honorific for divine subject)
- Hebrew narrative-opening וַיְהִי → idiomatic Thai (drop or use temporal-marker like 'วันหนึ่ง'); waw-consecutive chains do not require mechanical และ rendering

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Hebrew + Thai shown.

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
## Item A — The "did evil in the eyes of YHWH" evaluation formula drifts in the six late apostate kings

**The pattern:** A locked corpus doc (`docs/translator_decisions/dtr_history_cycle_formulas_2026-05.md`, the Deuteronomistic regnal-cycle formulas, which it declares "Gates 2 Kings + **Chronicles**") locks the recurring evaluation formula וַיַּעַשׂ הָרַע בְּעֵינֵי יְהוָה ("he did evil in the eyes of YHWH") to a single Thai surface: **`ทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า`** — specifically *with* `ร้าย` (the 1 Kings end-of-book review normalized 1 Kgs 22:53 from bare `ชั่ว` to `ชั่วร้าย` precisely to enforce this). 2 Chronicles, narrating the full Judahite monarchy, runs this formula on every apostate king.

**A clean split: the two early apostates comply (and document the lock); the six late ones drift.**

| Ref | King | Thai evaluation clause | Compliant? |
|---|---|---|---|
| **21:6** | Jehoram | `ทรงทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✓ (+ key_decision citing the lock) |
| **22:4** | Ahaziah | `ทรงทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✓ (+ key_decision citing the lock) |
| **33:2** | Manasseh | `ทรงทำชั่วในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว`, no key_decision |
| **33:6** | Manasseh | `ทรงทำชั่วมากมายในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว` |
| **33:22** | Amon | `ทรงทำชั่วในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว` |
| **36:5** | Jehoiakim | `ทรงทำชั่วในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว` |
| **36:9** | Jehoiachin | `ทรงทำชั่วในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว` |
| **36:12** | Zedekiah | `ทรงทำชั่วในสายพระเนตรขององค์พระผู้เป็นเจ้า` | ✗ bare `ทำชั่ว` |

(Non-regnal, same surface: 29:6 "our fathers did evil" → bare `ทำชั่ว`, in Hezekiah's reform speech.)

**Sample verses:**
- **33:2 HEB:** `וַיַּעַשׂ הָרַע בְּעֵינֵי יְהוָה` → **TH:** "พระองค์**ทรงทำชั่ว**ในสายพระเนตรขององค์พระผู้เป็นเจ้า ตามอย่างกิจอันน่าสะอิดสะเอียนของบรรดาประชาชาติ…"
- **21:6 HEB:** same idiom → **TH:** "พระองค์**ทรงทำสิ่งชั่วร้าย**ในสายพระเนตรขององค์พระผู้เป็นเจ้า" (the locked form)

**Editorial context:** the Hebrew idiom is identical in all eight verses (הָרַע "the evil"). The split is exact — the two verses that carry an explicit `key_decision` ship the locked `ทำสิ่งชั่วร้าย`; the six that carry no `key_decision` ship the thinner bare `ทำชั่ว`. This shipped undetected because the `check_phrase_consistency.py` evaluation lock is scoped `"books": ["1KI ", "2KI "]` — **2 Chronicles was never machine-checked** for it (the `malak` lock was widened to 2CH on 2026-05-26, but the DTr-formula locks were not).

**Forward-compounds to:** the Prophets, where the same Deuteronomistic evaluation formula recurs; and the phrase-consistency enforcement, which should be widened to 2CH (and beyond) to lock this in.

**Question:** Should the project normalize the six late-king evaluations (33:2, 33:6, 33:22, 36:5, 36:9, 36:12 — plus the non-regnal 29:6) from bare `ทำชั่ว` to the locked `ทำสิ่งชั่วร้าย` (restoring the `ร้าย` the lock requires and the 1 Kgs 22:53 precedent enforced), and simultaneously widen the `check_phrase_consistency.py` evaluation lock's scope to include `"2CH "`? Or is bare `ทำชั่ว` an acceptable contextual variant when the surrounding clause already piles on the apostasy detail (33:2 "abominations of the nations", 33:6 "much evil"), such that the lock should be relaxed to accept `ทำชั่ว`/`ทำสิ่งชั่วร้าย` as equivalent rather than normalized?

---

## Item B — 2 Chr 24:20: the named לָבַשׁ-class Spirit forward-protect anchor ships missing the locked honorific ทรง

**The pattern:** `docs/translator_decisions/spirit_of_yhwh_empowerment_2026-05.md` locks a 4-way split of the Hebrew Spirit-empowerment idiom by verb class. The **לָבַשׁ ("clothed") class** — where the Spirit *envelops* a person like a garment — is locked to **`พระวิญญาณ…ทรงสวมทับ`**, with the royal verb-honorific **`ทรง`**. The doc explicitly names **"2 Chr 24:20 (forward-protect)"** as the downstream anchor of this class, alongside the corpus-verified JDG 6:34 (`พระวิญญาณขององค์พระผู้เป็นเจ้าก็ทรงสวมทับกิดเอน`) and the first downstream ship 1 Chr 12:18 (`พระวิญญาณก็เสด็จมาสวมทับอามาสัย`).

**The shipped verse drops `ทรง`:**

- **24:20 HEB:** `וְרוּחַ אֱלֹהִים לָבְשָׁה אֶת־זְכַרְיָה בֶּן־יְהוֹיָדָע` ("the Spirit of God clothed Zechariah son of Jehoiada")
- **24:20 TH (shipped):** "แล้ว**พระวิญญาณของพระเจ้าสวมทับ**เศคาริยาห์บุตรของเยโฮยาดาปุโรหิต…"
- **Locked form:** "…พระวิญญาณของพระเจ้า**ทรงสวมทับ**เศคาริยาห์…"

The divine-name half is correct (anarthrous רוּחַ אֱלֹהִים → `พระวิญญาณของพระเจ้า`, Elohim form). Only the honorific `ทรง` is missing, and no `key_decision` documents or justifies dropping it.

**Editorial context:** because the Spirit is the divine subject, the royal verb-honorific is owed — exactly as at JDG 6:34 and 1 Chr 12:18. This is the single verse the lock forward-protected *by name*, so the deviation is precisely the kind the end-of-book audit exists to catch. The verb-class itself is correctly identified (`สวมทับ` = the לָבַשׁ "clothed" surface, not the הָיָה עַל `มาเหนือ` surface used correctly at 15:1 and 20:14); only `ทรง` is absent.

**Forward-compounds to:** any further לָבַשׁ-Spirit occurrence (Isaiah, the prophetic-empowerment passages); the consistency of the divine-Spirit honorific across the corpus.

**Question:** Should 24:20 be corrected to `…พระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์…`, adding the locked `ทรง` to match JDG 6:34 and 1 Chr 12:18 and the named lock anchor? Is there any reading under which omitting `ทรง` here is defensible (e.g., a register choice for the Chronicler's narration), or is this an unambiguous lock deviation to fix before tagging?

---

## Item C — 2 Chr 36:9 silently departs from the MT base on Jehoiachin's age (8 → 18), with no disclosure footer

**The pattern:** the Eremos OT is **MT-anchored** (`ot_canon_and_text_base_2026-05.md`; `synoptic_parallel_passages_2026-05.md` §1: each book translated from its own MT). When a verse **emends away from MT**, the policy *mandates* a **Trigger-1 Layer-2 MT-departure footer** (the treatment given to 2 Sam 15:7, where MT "forty years" was emended to "four" with a footer). When MT is merely *different* from a parallel but coherent, MT is **preserved** with a synoptic-variant note (the treatment given to 2 Chr 22:2 below). 36:9 does neither.

**The verse:**

- **36:9 HEB (MT):** `בֶּן־שְׁמוֹנֶה שָׁנִים יְהוֹיָכִין בְּמָלְכוֹ` — "Jehoiachin was **eight** (שְׁמוֹנֶה) years old when he became king"
- **36:9 TH (shipped):** "เยโฮยาคีนมีพระชนมายุ**สิบแปดพรรษา** (18) เมื่อขึ้นครองราชย์…"
- **Parallel:** 2 Kings 24:8 = "eighteen"; many LXX mss + BSB = "eighteen"
- **`notes`:** *none.* **`key_decision` on the age:** *none* (the only key_decision is the boilerplate YHWH→องค์พระผู้เป็นเจ้า note).

**Contrast — 22:2, the equally-famous age crux, handled correctly:**
- **22:2 HEB (MT):** "Ahaziah was **forty-two** (אַרְבָּעִים וּשְׁתַּיִם) years old…" → **TH:** "…พระชนมายุ**สี่สิบสองพรรษา** (42)…" — **MT preserved**, with a key_decision flagging that 2 Kgs 8:26 + LXX/Syriac read "22", noting the chronological impossibility (his father Jehoram died at 40), and stating the project keeps the MT reading.

**Editorial context:** 36:9 is the one place in 2 Chronicles where the Thai **silently follows the parallel/LXX/BSB reading against MT** — exactly the Trigger-1 situation (MT's "8" is contextually difficult; 2 Kings/LXX preserve the coherent "18") that the policy says must be *either* preserved-with-note *or* emended-with-footer. As shipped it is an undocumented, unflagged MT departure, and it is internally inconsistent with how the book treats its twin crux at 22:2.

**Forward-compounds to:** Ezra/Nehemiah and the Prophets (further MT-vs-LXX age/number cruxes); the integrity of the MT-anchored claim in the reviewer-facing packet.

**Question:** For 36:9, which disposition does the project want — (a) **restore MT "8"** (שְׁמוֹנֶה) with a synoptic-variant footer disclosing the 2 Kgs 24:8 "18" reading (the MT-faithful path, matching 22:2), or (b) **keep "18"** with a Trigger-1 Layer-2 MT-departure footer documenting the emendation (the 2 Sam 15:7 path)? Either way the silent, undocumented departure should not stand — but which commitment (strict MT-anchoring vs the harmonized "18" most translations adopt) is the tie-breaker here?

---

## Item D — The Deuteronomistic-formula phrase-locks are still Kings-scoped; 2 Chronicles (the densest regnal book) is unenforced

**The pattern:** `dtr_history_cycle_formulas_2026-05.md` locks the evaluation, high-places, and death-formula surfaces and its Enforcement section says "Add these exact locked surfaces to `check_phrase_consistency.py` before 2 Kings ships." Those locks exist — but scoped **`"books": ["1KI ", "2KI "]`**. 2 Chronicles, which re-runs the *entire* Judahite regnal cycle (~20 kings) and exercises these formulas more densely than any book except 2 Kings, is **outside all of them**.

**Evidence the gap is load-bearing:** the Item-A "did evil" drift (six bare `ทำชั่ว` verses) is exactly what a 2CH-scoped evaluation lock would hard-catch. The clean `check_phrase_consistency.py` result for the DTr locks reflects 2 Chronicles being *out of scope*, not a passed check. The 1 Chronicles end-of-book audit named widening these locks "the single highest-value forward-protection step … before 2 Chronicles begins shipping" — the `malak` half was actioned (widened to `["1KI ","2KI ","1CH ","2CH "]` on 2026-05-26), but the DTr-formula half was not.

**What complies by convention (verified manually this audit):** high-places notice `สถานบูชาบนที่สูงยังไม่ถูกกำจัด` (15:17, 20:33) and the locked noun at 21:11; the death/succession kingdom-keyed `ทรง` across all Davidic kings (§6 of the audit). These are correct — but unenforced.

**Forward-compounds to:** the Prophets, where the Deuteronomistic evaluation/source-citation formulas echo; and the corpus-wide consistency the phrase-check is meant to guarantee.

**Question:** Should the project widen the `check_phrase_consistency.py` DTr-formula locks (evaluation `ชั่วร้าย` + `ถูกต้อง`, high-places `สถานบูชาบนที่สูง`) to include `"2CH "` (and add the death-formula register split as a fourth lock, keyed by kingdom), running it as part of resolving the Item-A drift? Is there any false-positive risk in 2 Chronicles that argues for leaving it convention-only (e.g., the active-removal `รื้อ`/`ชำระ`+`สถานสูง` narratives vs the locked `สถานบูชาบนที่สูง` notice — the two-surface system), or is the scope-widening clean?

---

## Item E — Human-messenger מַלְאָךְ ships uniformly as ผู้สื่อสาร — the form the lock says to avoid

**The pattern:** `malak_yhwh_2026-05.md` §4.4 places **human**-messenger מַלְאָךְ outside the divine `ทูตสวรรค์` lock and sets a hierarchy: default **`ผู้ส่งสาร`**; **`ทูต`/`คณะทูต`** for diplomatic/group envoys; and explicitly **avoid `ผู้สื่อสาร` / `ผู้ส่งข่าว`** (reclassify unless a documented contextual reason). 2 Chronicles renders **every** human/prophetic messenger as the avoid-form `ผู้สื่อสาร`:

| Ref | Hebrew | 2CH Thai | Sense |
|---|---|---|---|
| 18:12 | הַמַּלְאָךְ (envoy summoning Micaiah) | `ผู้สื่อสาร` | court runner |
| 35:21 | מַלְאָכִים (Pharaoh Neco's envoys to Josiah) | `ผู้สื่อสาร` | royal/foreign envoy |
| 36:15 | בְּיַד מַלְאָכָיו (YHWH's messengers = the prophets) | `ผู้สื่อสาร` | prophet-as-messenger |
| 36:16 | מַלְאֲכֵי הָאֱלֹהִים (the messengers of God = prophets) | `ผู้สื่อสารของพระเจ้า` | prophet-as-messenger |

**Sample:**
- **35:21 HEB:** `וַיִּשְׁלַח אֵלָיו מַלְאָכִים` → **TH:** "แต่เนโคส่ง**ผู้สื่อสาร**มาหาพระองค์ว่า…"
- **36:16 HEB:** `וַיִּהְיוּ מַלְעִבִים בְּמַלְאֲכֵי הָאֱלֹהִים` → **TH:** "แต่พวกเขากลับเยาะเย้ย**ผู้สื่อสารของพระเจ้า** ดูหมิ่นพระวจนะของพระองค์ และหัวเราะเยาะบรรดาผู้เผยพระวจนะ…"

**Editorial context:** the lemma-thread holds where it matters most — the divine angel (32:21 `ทูตสวรรค์องค์หนึ่ง`) and the prophets-as-messengers (`ผู้สื่อสาร`/`ผู้เผยพระวจนะ`) are cleanly separated, so `ทูตสวรรค์` never leaks into 36:15–16. The issue is only that 2 Chronicles uses the §4.4 *avoid*-form across the board rather than the `ผู้ส่งสาร` default. This continues the standing cross-book human-messenger normalization the 1 Kings §3b / 2 Kings §3b audits opened (the 2 Kings `ผู้สื่อสาร` backlog: 5:10, 6:32–33, 9:18, 10:8, 14:8, 19:9, 19:14). It is MT-faithful either way and is a deferred-queue item, not a tag blocker.

**Forward-compounds to:** the corpus-wide human-messenger normalization pass (already deferred); every later narrative book with royal/prophetic envoys.

**Question:** Should the project normalize 2 Chronicles' `ผู้สื่อสาร` toward the §4.4 hierarchy (18:12 court-runner → `ผู้ส่งสาร`; 35:21 Neco's foreign envoys → `ทูต`/`คณะทูต`; 36:15–16 prophets-as-messengers → keep a messenger word but per the default), folding it into the deferred cross-book pass — or is the *prophet-as-messenger* sense at 36:15–16 distinct enough that `ผู้สื่อสาร` ("communicator/herald") is actually the more natural Thai there, in which case the lock should license `ผู้สื่อสาร` for prophetic messengers and only normalize the ordinary-envoy cases (18:12, 35:21)?

---

## Item F — "Until this day" leitwort: 2 Chronicles makes it 5-of-6; 1 Samuel is the lone outlier

**The pattern:** עַד הַיּוֹם הַזֶּה ("until this day", the etiological leitwort) has two competing Thai surfaces across the corpus. 2 Chronicles ships it uniformly **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) at all six occurrences — **5:9, 8:8, 10:19, 20:26, 21:10, 35:25**.

**Cross-book corpus picture (six DtrH/Chronicler books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× (+1 drift) |
| **1 Samuel** | **`จนถึงวันนี้`** (bare) | **8× uniform** |
| 1 Kings | `จนถึงทุกวันนี้` | 5× |
| 2 Kings | `จนถึงทุกวันนี้` | 10× |
| 1 Chronicles | `จนถึงทุกวันนี้` | 2× |
| **2 Chronicles** | **`จนถึงทุกวันนี้`** | **6×** |

**Sample:** **35:25 TH:** "…บรรดานักร้องชายหญิงก็ขับบทคร่ำครวญถึงโยสิยาห์มา**จนถึงทุกวันนี้**…"

**Editorial context:** five of six books now agree on `จนถึงทุกวันนี้`; only 1 Samuel uses the bare `จนถึงวันนี้`. `leitwort_handling_policy_2026-05.md` still does not lock a Thai surface for this leitwort. This is the standing 1 Kings §14 / 2 Kings §11 / 1 Chronicles §13 cross-book REVIEW, now with a fifth concurring book — the majority is decisive.

**Question:** Should `leitwort_handling_policy_2026-05.md` now lock **`จนถึงทุกวันนี้`** as the canonical corpus surface (the 5-of-6 majority, the form 2 Chronicles independently uses 6×) and normalize 1 Samuel's 8 bare `จนถึงวันนี้` occurrences to match — or is the `ทุก-` intensifier (`ทุกวันนี้` "these very days / right up to now" vs `วันนี้` "this day") a meaningful nuance that could legitimately vary, leaving 1 Samuel's form defensible?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
