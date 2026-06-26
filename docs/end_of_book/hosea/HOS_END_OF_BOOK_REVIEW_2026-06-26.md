# Hosea — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 14 chapters of Hosea (197 verses); `glossary.json`; `docs/translator_decisions/` corpus (97 docs). **The first of the Book of the Twelve (Minor Prophets) in the corpus, and the OT's foundational marriage-covenant book** — the spiritual-adultery metaphor (Gomer; זְנוּנִים / זָנָה) that Jeremiah 2–3 and Ezekiel 16/23 later develop at length. Hosea is also one of the most densely NT-quoted Minor Prophets: 11:1 "out of Egypt I called my son" (→ Matt 2:15), 6:6 "I desire mercy not sacrifice" (→ Matt 9:13; 12:7), 1:10 + 2:23 "Not-my-people → sons of the living God" (→ Rom 9:25–26; 1 Pet 2:10), 13:14 "O Death, where are your plagues" (→ 1 Cor 15:55), 10:8 "say to the mountains, cover us" (→ Luke 23:30; Rev 6:16), and 14:3 "fruit of our lips" (echoed Heb 13:15). **All of the NT it cross-quotes is already shipped.**
**Trigger:** HOS 14 shipped (commit `e1816641`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) pass: 14/14 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks); `audit_inclusion_variants.py --book hosea --strict` = **0 candidates, exit 0**; `check_divine_names.py --book HOS` = exit 0 with **zero warnings** (the cleanest divine-name checker state of any major OT book to date — cleaner than Jeremiah's 2 false positives); `check_versification_anchor.py --book HOS` = exit 0. **14/14** chapters carry a `textual_variants` YHWH first-occurrence footnote (complete coverage), and the three MT-vs-English divergence zones (chs **2, 12, 14**) each additionally carry a reader-facing `versification_divergence` footnote, while ch.13 carries a `reception_history_and_textual_note` footnote disclosing the 13:14 → 1 Cor 15:55 MT/LXX divergence. **Mechanically this is the cleanest book state in the corpus.** Two infrastructure items surfaced (§18): `export_to_usfm.py` still rejects `HOS` (the recurring OT book-code gotcha), and the **HOS-14 versification-map zone + a `build_versification_map.py` change are sitting uncommitted in the working tree** (the known "ship script doesn't stage the map" gotcha — they are present, so the check passes, but they need a manual commit before they are lost).

- **1 item flagged DECIDE** (Ben choice needed before tagging `book-hosea-v1`):
  - **§7 — divine-anthropomorphism register: the *codified* first-person-plain rule reappears, with the same internal inconsistency.** `divine_anthropomorphism_thai_grammar_2026-05.md` locks God's body-parts to royal register (ราชาศัพท์) with **no person-based exception**. In Hosea, first-person divine body-parts systematically drop to **plain** register, and — exactly as in Jeremiah §13 — the lapse is **argued into the `key_decisions` as an intentional "narrator-vs-speaker" rule**: 2:12 "my hand" מִיָּדִי → plain **มือ** (KD: *"in God's 1st-person speech rendered plain มือของเรา, not royal พระหัตถ์, per the narrator-vs-speaker distinction"*); 11:8 "my heart" לִבִּי → plain **ใจ** (KD: *"1st-person divine heart rendered plain ใจ, per the narrator-vs-speaker rule"*); 13:14 "my eyes" מֵעֵינָי → plain **สายตา**. But Hosea is **not internally consistent**: at **5:15** the first-person divine "seek my face" בִּקְשׁוּ פָנָי takes the **royal พระพักตร์** (KD: *"the worship-approach idiom takes the royal พระพักตร์, as in 2 Chr 7:14"*). So within one short book the same grammatical person splits: 1st-person hand/heart/eyes → plain, but 1st-person face → Rachasap. This is the identical drift the Isaiah audit (§13, recommended reversal), the Jeremiah audit (§13, codified), and the Ezekiel audit (§10, codified at scale) all flagged — **all three still untagged and unreconciled.** Hosea adds a clean new data point: the פָנִים "face" → พระพักตร์ exception. **Ben must ratify a documented first-person exception (and define where 1st-person still takes Rachasap, e.g. face) OR reverse the ~3 plain instances — and reconcile the decision corpus-wide with Isaiah/Jeremiah/Ezekiel** before it compounds into the rest of the Twelve (Joel, Amos, Micah). See §7.

- **4 items flagged REVIEW** (worth Ben's confirmation):
  - **§13 — 6:6 חֶסֶד vs the Matthew quotation: an NT-cited MT/LXX divergence with no reader footer.** Hosea 6:6 renders חֶסֶד → **ความรักมั่นคง** (the corpus chesed-lock); Jesus quotes the verse twice from the LXX (ἔλεος), and the shipped Matt 9:13 / 12:7 read **ความเมตตา** (also เครื่องสัตวบูชา vs เครื่องบูชา for "sacrifice"). A reader comparing Hos 6:6 ↔ Matt 9:13 hits ความรักมั่นคง vs ความเมตตา with **no footnote** — the same NT-cited MT/LXX gap the Jeremiah audit flagged for 31:32 (§9). The divergence is correctly noted in the 6:6 KD but is KD-only (not reader-facing). Confirm whether the `mt_vs_lxx §2.3` floor obligates a Tier-2 footer here (the contrasting 13:14 case **does** carry one — §12). See §13.
  - **§14 — 14:3 "fruit of our lips": the one verse where Hosea departs from its MT base.** The MT vocalizes פָּרִים "bulls (of our lips)"; the translation follows the LXX/Syriac reading פְּרִי "fruit," harmonizing with the shipped Heb 13:15 (**ผลแห่งริมฝีปาก**, byte-shared). This is defensible and well-attested, but it is the single place in the book where the MT-anchored text (`ot_canon_and_text_base`) follows a non-MT reading, and the decision lives only in the KD + `notes` (not reader-facing). Confirm + consider a Tier-2 footer. See §14.
  - **§15 — 4:7 tiqqun sopherim disclosure.** The verse renders the MT כְּבוֹדָם "their glory" and the `notes` correctly records the scribal tradition that the original may have read כְּבוֹדִי "My Glory." This is a reader-relevant text-critical point that lives only in the non-rendered `notes` field. Confirm KD/notes-only is acceptable, or promote to a Tier-2 footer. See §15.
  - **§18 — versification-map commit hygiene.** All three Hosea MT/English divergence zones (chs 2, 12, 14) are registered in `data/versification_map.json` and the check passes — but the **HOS-14 zone + a `scripts/build_versification_map.py` change are uncommitted in the working tree** (the documented ship-script gotcha). Commit them manually before tagging so they are not lost. See §18.

- **STABLE-but-undocumented patterns recommending doc-lift / note:** the **זָנָה / זְנוּנִים spiritual-harlotry leitwort** (§9 — the book's controlling metaphor, rendered with a principled זָנָה → **เล่นชู้** / נָאַף → **ล่วงประเวณี** split; no corpus doc; **recommend `spiritual_harlotry_metaphor_2026-06.md`** as the canonical reference the already-shipped Jeremiah 2–3 / Ezekiel 16/23 renderings were derived against); the **דַּעַת אֱלֹהִים "knowledge of God" leitwort** (§10 — Hosea's theme-word, רֵעַ → **ความรู้จักพระเจ้า / รู้จัก**, the daʿaṯ root traced through 2:22, 4:1, 4:6, 5:4, 6:3, 6:6, 13:5, 14:10; **recommend a one-paragraph note** in `leitwort_handling_policy`); the **symbolic-name-with-inline-gloss** method (§11 — Jezreel/Lo-Ruhamah/Lo-Ammi and their reversals, transliteration + parenthetical gloss; consistent with the Isaiah Maher-shalal / Immanuel approach).

- **External AI review (§3) pending.** Suggested 4-item packet: the codified first-person anthropomorphism rule (§7 DECIDE); the 6:6 חֶסֶד/ἔλεος NT-cited divergence + footer question (§13); the 14:3 MT-departure "fruit of lips" reading (§14); the spiritual-harlotry leitwort rendering (§9 — also tests the metaphor's consistency against the shipped Jeremiah/Ezekiel surface).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. יְהוָה Tetragrammaton (Layer 1) + first-occurrence footnote coverage — **LOCKED**

YHWH → **องค์พระผู้เป็นเจ้า** in every occurrence (Layer 1), with each verse's KD citing `divine_names_table_2026-05`. The vocative "O LORD" (9:14, 14:3) correctly takes **ข้าแต่องค์พระผู้เป็นเจ้า**. The Sabaoth title-cluster at **12:6** (יְהוָה אֱלֹהֵי הַצְּבָאוֹת) → **องค์พระผู้เป็นเจ้าพระเจ้าจอมโยธา**, matching the corpus jom-yotha lock. The covenant self-declaration אָנֹכִי יְהוָה אֱלֹהֶיךָ (12:10, 13:4) → **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของเจ้า** (Exod 20:2 form). All **14/14** `output/textual_variants/hosea_NN.json` files carry the `tetragrammaton_convention_first_occurrence` footnote — **complete coverage**, matching Jeremiah's clean state. `check_divine_names.py --book HOS` = exit 0 with **zero warnings**. **LOCKED** ✓. **Severity: GREEN.**

---

## 2. Standalone אֲדֹנָי (12:15) + the divine self-name echo (1:9) — **LOCKED**

The lone standalone third-person divine אֲדֹנָי at **12:15** (אֲדֹנָיו "his Lord/Master") → **องค์เจ้านายของเขา**, per the `divine_names_table` standalone-Adonai rule. The covenant-formula reversal at **1:9** (אָנֹכִי לֹא־אֶהְיֶה לָכֶם, echoing the divine self-name אֶהְיֶה of Exod 3:14) is handled descriptively in the KD and rendered "เราก็ไม่ใช่พระเจ้าของพวกเจ้า" — the אֶהְיֶה echo is named in the KD, not lexicalized. No other standalone divine Adonai occurs. **LOCKED** ✓. **Severity: GREEN.**

---

## 3. חֶסֶד covenant-love — **LOCKED**

All **6** occurrences → **ความรักมั่นคง**, zero mis-fires: 2:21 (the betrothal-virtue list), 4:1 (the missing-covenant triad), 6:4 ("your ḥesed is like the morning mist"), 6:6 (**the book's theological heart** — "I desire ḥesed not sacrifice"), 10:12 ("reap according to ḥesed"), 12:7 ("keep ḥesed and justice"). The 6:6 KD additionally flags the LXX ἔλεος rendering Jesus quotes (→ §13). **LOCKED** ✓ per `chesed_covenant_love_2026-05.md`. **Severity: GREEN.**

---

## 4. Baal / pagan-deity register — **LOCKED**

- **בַּעַל / הַבְּעָלִים all carry the OT proper-name register**, zero bare: Baal → **พระบาอัล** (2:10, 2:18, 11:2, 13:1), the plural "the Baals" → **พระบาอัลทั้งหลาย** (2:15, 2:19). The place-name **Baal-Peor** (9:10) correctly takes **no** พระ- (it is a toponym, not the deity) → บาอัลเปโอร์.
- The polemical substitute **בֹּשֶׁת "Shame"** (9:10, the contemptuous surrogate for "Baal") → **สิ่งที่น่าอับอาย**, descriptively handled in the KD.
- **Idol vocabulary** is uniformly contemptuous: עֲצַבִּים "idols" → รูปเคารพ (4:17, 8:4, 13:2, 14:9), the Bethel/Samaria **calf** (8:5–6, 10:5, 13:2) → รูปลูกวัว with the "a craftsman made it, it is not God" satire intact (8:6), and the household gods תְּרָפִים → รูปเคารพประจำบ้าน (3:4). Pagan-object pronouns stay **มัน**.

**LOCKED** ✓ per `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`. **Severity: GREEN.**

---

## 5. פקד paqad "visit / punish" — **LOCKED**

The judgment sense → **ลงโทษ / ทรงลงโทษ** consistently: 1:4 (the blood of Jezreel), 2:15 (the days of the Baals), 4:9 (priest and people alike), 4:14, 8:13, 9:9, 12:3 (the lawsuit against Jacob). The "days of reckoning" noun פְּקֻדָּה (9:7) → วันแห่งการลงโทษ. No sense-confusion with the visit/attend sense (which does not occur in a positive register here). **LOCKED** ✓ per `paqad_visit_attend_2026-05.md`. **Severity: GREEN.**

---

## 6. Hebrew oath חַי־יְהוָה (4:15) — **LOCKED**

The single oath formula in the book — חַי־יְהוָה "as the LORD lives" at **4:15** — → **องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่แน่ฉันใด**, exactly the corpus lock (and notably forbidden *here*: Israel is told not to swear it at the corrupt Gilgal/Beth-aven shrines). **LOCKED** ✓ per `hebrew_oath_formulas_2026-05.md`. **Severity: GREEN.**

---

## 7. Divine anthropomorphism — the codified first-person-plain rule + the face-exception — **DECIDE (the loudest finding)**

`divine_anthropomorphism_thai_grammar_2026-05.md` locks God's body-parts to royal register (ราชาศัพท์) with **no person-based exception**: hand יָד → **พระหัตถ์**, eyes עֵינַי → **พระเนตร**, face פָּנִים → **พระพักตร์**, heart לֵב → **พระทัย**. In Hosea, first-person divine body-parts **systematically drop to plain register**, and the lapse is **written into the `key_decisions` as a deliberate "narrator-vs-speaker" rule** — identical to the Jeremiah codification:

| Ref | Hebrew (1st-person divine) | Thai | Register | KD rationale |
|---|---|---|---|---|
| **2:12** | מִיָּדִי "from my hand" | **มือ** | **plain (DRIFT)** | *"in God's 1st-person speech rendered plain มือของเรา, not royal พระหัตถ์, per the narrator-vs-speaker distinction"* |
| **11:8** | לִבִּי "my heart" | **ใจ** | **plain (DRIFT)** | *"1st-person divine heart rendered plain ใจ, per the narrator-vs-speaker rule"* |
| **13:14** | מֵעֵינָי "from my eyes" | **สายตา** | **plain (DRIFT)** | (rendered plain; no explicit note) |
| **5:15** | בִּקְשׁוּ פָנָי "seek my face" | **พระพักตร์** | **royal (kept!)** | *"the worship-approach idiom takes the royal พระพักตร์, as in 2 Chr 7:14"* |

The third-person comparator is correct: **6:2** לְפָנָיו "before him" → royal **ต่อพระพักตร์พระองค์** ✓. The anger-anthropomorphisms (אַף) are noun-rendered and not at issue: 11:9 חֲרוֹן אַפִּי → ความพิโรธอันรุนแรง; 13:11 בְּאַפִּי / בְּעֶבְרָתִי → ด้วยความโกรธ/ความพิโรธ.

**The split is the problem.** Within one short book, the *same grammatical person* (1st-person divine speech) yields plain register for hand/heart/eyes but royal register for face — the translator codifies "1st-person → plain" yet carves an unstated face-exception for the "seek my face" worship-idiom. This is precisely the internal inconsistency the Jeremiah audit flagged (15:6 kept פระหัตถ์ in a 1st-person clause) and that Isaiah §13 recommended reversing.

**Hosea is now the fourth book** — after Isaiah (§13, undocumented drift, recommended reversal), Jeremiah (§13, codified rule), and Ezekiel (§10, codified at scale ~22 verses) — exhibiting this pattern, and **all three prior audits remain untagged and unreconciled.** Hosea's contribution is a clean, isolated demonstration of the **פָּנִים "face" → พระพักตร์ exception** that the rule needs to either absorb or reject.

**DECIDE — Ben must choose one and apply it corpus-wide:**
(a) **Ratify** a documented "first-person divine self-reference → plain register" exception, amend `divine_anthropomorphism_thai_grammar_2026-05.md`, and **state explicitly when 1st-person still takes Rachasap** (the 5:15 face-idiom shows the rule already has a carve-out); **or**
(b) **Reverse** the 3 plain instances to Rachasap (2:12 → พระหัตถ์; 11:8 → พระทัย; 13:14 → พระเนตร), matching the Isaiah §13 recommendation.

Either way, **reconcile with Isaiah/Jeremiah/Ezekiel §13** so the corpus speaks with one voice **before the rest of the Twelve** (Amos and Micah carry the same first-person divine-judgment idiom). **Severity: HIGH** (corpus-lock conflict, codified, cross-book, load-bearing — though *inherited and re-demonstrated*, not Hosea-created).

---

## 8. נחם / divine compassion (11:8, 13:14) — **STABLE (correctly does not fire the relent-lock)**

`nicham_divine_relenting_2026-05.md` locks the Niph'al "relent / change mind" sense → ทรงเปลี่ยนพระทัย / เปลี่ยนพระทัย. Hosea's two נחם occurrences are the **noun "compassion"** sense, not the relent-verb, and correctly do **not** fire the lock:
- **11:8** נִכְמְרוּ נִחוּמָי "my compassions grow warm" → **ความเมตตาสงสาร…ถูกจุดให้ร้อนรน** (the emotional summit of the book — God recoiling from Sodom-like annihilation).
- **13:14** נֹחַם יִסָּתֵר מֵעֵינָי "compassion is hidden from my eyes" (hapax) → **ความสงสารถูกซ่อนไว้**.

Both are rendered as the compassion-noun, leaving the relent-lemma lock dormant — correct. **STABLE** ✓. **Severity: GREEN.**

---

## 9. זָנָה / זְנוּנִים spiritual-harlotry leitwort — **STABLE (undocumented; recommend new doc)**

The book's controlling metaphor — Israel as YHWH's adulterous wife — is rendered with a **principled two-lemma split** that holds across all 14 chapters:

| Lemma | Sense | Thai | Representative |
|---|---|---|---|
| זָנָה (verb) / זְנוּנִים (noun) | "play the harlot / promiscuity" (spiritual adultery) | **เล่นชู้ / การเล่นชู้** | 1:2 (×3), 2:4, 2:7, 3:3, 4:10, 4:12 (×2), 4:13, 4:14, 4:15, 5:3, 6:10, 9:1 |
| נָאַף (verb) / נַאֲפוּפִים (noun) | "commit adultery" | **ล่วงประเวณี / การล่วงประเวณี** | 2:4, 3:1, 4:2, 4:13, 4:14, 7:4 |
| רוּחַ זְנוּנִים | "a spirit of harlotry" | **วิญญาณแห่งการเล่นชู้** | 4:12, 5:4 |
| אֶתְנָה / אֶתְנָן | "a harlot's hire/wages" | **ค่าจ้าง (ของหญิงโสเภณี)** | 2:14, 9:1 |
| זֹנוֹת / קְדֵשׁוֹת | "prostitutes / cult-prostitutes" | **หญิงโสเภณี / หญิงโสเภณีประจำสถานบูชา** | 4:14 |

The זָנָה (covenant-infidelity) vs נָאַף (literal adultery) distinction is maintained, and the literal-vs-figurative cult-prostitution of 4:13–14 is disambiguated lexically. This is the **OT root-system** that the already-shipped Jeremiah 2–3 and Ezekiel 16/23 elaborate. The rendering is consistent and principled but lives **entirely in per-verse KDs** — there is no corpus doc. **Recommend `docs/translator_decisions/spiritual_harlotry_metaphor_2026-06.md`** locking the זָנָה → เล่นชู้ / נָאַף → ล่วงประเวณี split as the canonical reference (retro-documenting the Jeremiah/Ezekiel surface against Hosea, the metaphor's source book; forward weight into the rest of the Twelve, esp. Nahum 3:4 and Micah 1:7). **Severity: LOW-MEDIUM** (surface is sound; the gap is corpus-doc-lift). The NT-side `porneia_vs_moicheia_DEFERRED_2026-05.md` is a separate (Greek) matter — note the cross-reference.

---

## 10. דַּעַת אֱלֹהִים "knowledge of God" leitwort — **STABLE (undocumented; recommend note)**

Hosea's theme-word — the relational covenant-knowledge whose absence is the indictment and whose restoration is the goal — is rendered with a traceable דַּעַת / יָדַע root: the noun phrase דַּעַת אֱלֹהִים → **ความรู้จักพระเจ้า** (4:1, 4:6, 6:6) and the verb יָדַע → **รู้จัก** (2:22 "you will know the LORD," 5:4 "they do not know the LORD," 6:3 "let us know, let us press on to know the LORD," 13:5 "I knew you in the wilderness," 14:10 the closing wisdom-colophon "the discerning will *know* them"). The morpheme รู้จัก stays visible across the family, and the 6:6 KD explicitly ties it to the 4:1/4:6 lack. This is principled leitwort handling per `leitwort_handling_policy_2026-05.md` but the daʿaṯ thread is nowhere consolidated. **Recommend a one-paragraph note** (in `leitwort_handling_policy` or a short Hosea-anchored doc) recording the דַּעַת → ความรู้จัก/รู้จัก thread. **Severity: LOW.**

---

## 11. Symbolic judgment-names + their reversal — **STABLE**

The three sign-act children's names and their great reversal are handled by a consistent **transliteration + inline parenthetical gloss** method (the names *are* the message), matching the Isaiah Maher-shalal-hash-baz / Immanuel approach:

| Name | Hebrew | Thai | Sense given |
|---|---|---|---|
| Jezreel | יִזְרְעֶאל | **ยิสเรเอล** | judgment (1:4) → "God sows," restoration (2:2, 2:24) — both senses surfaced in KD |
| Lo-ruhamah | לֹא רֻחָמָה | **โลรุหะมาห์** (ไม่ได้รับความเมตตา) | 1:6 |
| Lo-ammi | לֹא עַמִּי | **โลอัมมี** (ไม่ใช่ประชากรของเรา) | 1:9 |
| Ammi (reversal) | עַמִּי | **อัมมี** (ประชากรของเรา) | 2:3, 2:25 |
| Ruhamah (reversal) | רֻחָמָה | **รุหะมาห์** (ผู้ได้รับความเมตตา) | 2:3, 2:25 |

The scornful place-puns are likewise handled descriptively: **Beth-aven** בֵּית אָוֶן "house of iniquity" (4:15, 5:8, 10:5, 10:8) → เบธาเวน with the Bethel-pun named in the KD; **Achor** "trouble" → door of hope (2:17). The 2:25 climactic name-reversal is the verse Paul (Rom 9:25) and Peter (1 Pet 2:10) quote — see §12. **STABLE** ✓ per `proper_names_and_transliteration_2026-05.md` + `proper_noun_wordplay_2026-05.md`. **Severity: GREEN.**

---

## 12. OT→NT cross-quotation thread — **STABLE / LOCKED (two footer questions → §13, §14)**

Hosea is one of the most NT-quoted Minor Prophets, and **all of the NT it cites is shipped.** The thread holds at the core-phrase level; verified against the shipped NT:

| Hosea | NT | Hosea Thai | NT Thai | Verdict |
|---|---|---|---|---|
| **11:1** "out of Egypt I called my son" | Matt 2:15 | เราได้เรียกบุตรของเราออก**มา**จากอียิปต์ | เราได้เรียกบุตรของเราออกจากอียิปต์ | **near-byte** (cosmetic มา; minor — could normalize) |
| **2:1 (Eng 1:10)** "sons of the living God" | Rom 9:26 | บุตรของพระเจ้าผู้ทรงพระชนม์ | บุตรของพระเจ้าผู้ทรงพระชนม์**อยู่** | **near-byte** (cosmetic อยู่) |
| **2:25 (Eng 2:23)** "not-my-people → my people" | Rom 9:25; 1 Pet 2:10 | ประชากรของเรา / ไม่ใช่ประชากรของเรา | ประชากรของเรา / ไม่ใช่ประชากรของเรา | **byte-shared core** (Paul's "loved/ที่รัก" tracks his own Greek) |
| **6:6** "mercy not sacrifice" | Matt 9:13; 12:7 | ความรักมั่นคง (חֶסֶד) | ความเมตตา (ἔλεος) | **MT/LXX divergence — footer? → §13** |
| **13:14** "O Death, where are your plagues" | 1 Cor 15:55 | ภัยพิบัติ / พลังทำลายล้าง (MT) | ชัยชนะ / เหล็กใน (LXX) | **MT/LXX divergence — footer present** ✓ (reception_history note) |
| **10:8** "say to the mountains, cover us" | Luke 23:30; Rev 6:16 | จงปิดคลุมเราไว้ / จงทับถมเรา | จงล้มลงทับเราเถิด / จงปิดคลุมเราเถิด | **harmonized** (Luke reverses mountain/hill per its own Greek; ปิดคลุม shared; "fall on" varies ทับถม/ล้มลงทับ/ล้มทับ — minor) |
| **14:3** "fruit of our lips" | Heb 13:15 | ผลแห่งริมฝีปาก (LXX/Syriac reading) | ผลแห่งริมฝีปาก | **byte-shared — but MT-departure → §14** |

The two **near-byte cosmetic diffs** (11:1 ออกมาจาก vs Matt ออกจาก; 2:1 ผู้ทรงพระชนม์ vs Rom ผู้ทรงพระชนม์อยู่) are sub-§2.3-floor and KD-only-compliant; flag only if Ben wants byte-identity on the marquee Matt 2:15 quote. The **13:14** disclosure is the model case (a reader-facing `reception_history_and_textual_note` footnote in `textual_variants/hosea_13.json` explains the MT "plagues" vs LXX-Paul "victory/sting" split, and the KD notes "the Eremos text keeps the surface of the Hebrew and lets both horizons stand" — §0-compliant, restrained). The **6:6** (§13) and **14:3** (§14) divergences are the two that lack the same reader-facing treatment. **STABLE/LOCKED** on the thread itself. **Severity: GREEN** (here; §13/§14 carry the footer questions).

---

## 13. 6:6 חֶסֶד vs ἔλεος — NT-cited MT/LXX divergence, no reader footer — **REVIEW**

Hosea 6:6 is the book's theological heart and one of its most-quoted verses. The MT reads חֶסֶד (→ corpus-locked **ความรักมั่นคง**); the LXX reads ἔλεος "mercy," and **that** is the form Jesus quotes twice (Matt 9:13; 12:7), shipped as **ความเมตตา** (with "sacrifice" זֶבַח → เครื่องสัตวบูชา in Hosea vs θυσία → เครื่องบูชา in Matthew):

- **Hos 6:6** GK/MT: `כִּי חֶסֶד חָפַצְתִּי וְלֹא־זָבַח` → TH: `เพราะเราประสงค์**ความรักมั่นคง** ไม่ใช่**เครื่องสัตวบูชา**`
- **Matt 9:13 / 12:7** GK: `ἔλεος θέλω καὶ οὐ θυσίαν` → TH: `เราประสงค์**ความเมตตา** มิใช่**เครื่องบูชา**`

A reader cross-referencing Hos 6:6 ↔ Matt 9:13 sees ความรักมั่นคง vs ความเมตตา with **no footnote** — exactly the NT-cited MT/LXX gap the Jeremiah audit obligated a footer for at 31:32 (§9). The 6:6 KD correctly identifies the divergence (*"the LXX renders ἔλεος 'mercy,' which is how Jesus quotes it in Matt 9:13; 12:7"*), but it is KD-only and not reader-facing. The contrasting 13:14 case (§12) **does** carry a `reception_history` footer for the analogous divergence.

**REVIEW — confirm whether the `mt_vs_lxx §2.3` floor obligates a Tier-2 footer at 6:6** (modeled on the 13:14 reception-history note: "MT 'steadfast love' (חֶסֶד); the LXX 'mercy' (ἔλεος) is the form quoted in Matt 9:13; 12:7"). This is the highest-visibility cross-quote in the book after 11:1. **Severity: LOW-MEDIUM** (apparatus decision; no surface edit implied — the חֶסֶד lock is correct).

---

## 14. 14:3 "fruit of our lips" — the one MT-departure — **REVIEW**

`ot_canon_and_text_base` anchors the project to the MT. **Hosea 14:3 is the single verse in the book where the translation follows a non-MT reading.** The MT vocalizes פָּרִים "bulls (of our lips)"; the translation follows the LXX/Syriac פְּרִי "fruit," harmonizing with the shipped Heb 13:15:

- **Hos 14:3** MT: `וּנְשַׁלְּמָה פָרִים שְׂפָתֵינוּ` ("we will render the *bulls* of our lips") → TH: `เพื่อเราจะถวาย**ผลแห่งริมฝีปาก**ของเราต่างเครื่องบูชา` (the LXX/Syriac "fruit")
- **Heb 13:15** GK: `καρπὸν χειλέων` → TH: `**ผลแห่งริมฝีปาก**ที่ยอมรับพระนามของพระองค์` (byte-shared)

The choice is well-attested (BSB, NIV, ESV-mg all read "fruit"; the praise-replaces-sacrifice theology is the point) and the harmonization with Heb 13:15 is a genuine virtue. But it is the one place Hosea steps off its stated MT base, and the decision lives only in the KD + Thai `notes` (not reader-facing). The 14:3 `notes` correctly records the MT/LXX split and the Heb 13:15 echo.

**REVIEW — confirm the LXX/Syriac "fruit" reading against the MT base, and consider a Tier-2 footer** (the `mt_vs_lxx §2.3` floor is arguably met: an NT-echoed variant where the shipped surface follows the non-MT reading). If Ben wants strict MT-priority, this could rise to a re-render question; recommend **keep the reading** (it is the better-supported sense and harmonizes the NT) **+ add a reader footer**. **Severity: LOW-MEDIUM.**

---

## 15. 4:7 tiqqun sopherim — textual-tradition disclosure — **REVIEW**

Hosea 4:7 renders the MT כְּבוֹדָם "their glory" (they exchanged their glory for shame) and the `notes` records the Jewish scribal tradition (one of the *tiqqunê sopherim*, the reverent emendations) that the original may have read כְּבוֹדִי "**My** Glory" — i.e., they exchanged the LORD himself, their true Glory, for a shameful idol. The MT surface is correctly followed and the tradition correctly noted — but the note lives only in the non-rendered `notes` field. **REVIEW — confirm KD/notes-only disclosure is acceptable for a tiqqun-sopherim point, or promote to a Tier-2 footer.** This is the only tiqqun in Hosea; low forward weight, but a clean precedent-setting question (other tiqqunim occur in Zechariah 2:12, Malachi 1:13 ahead). **Severity: LOW.**

---

## 16. Foreign references (Assyria, Egypt; "the great king") — **STABLE (foreign_monarch doc unaffected)**

Hosea has **no foreign monarch as a narrative actor** — only references. The Assyrian title מֶלֶךְ יָרֵב (5:13, 10:6) → **มหากษัตริย์** "the great king" (following BSB; probably the Assyrian title *malki-rab* rather than a personal name "Jareb," correctly noted in the KD). Assyria → อัสซีเรีย and Egypt → อียิปต์ throughout (the "return to Egypt" un-Exodus motif, 8:13, 9:3, 11:5, 11:11). Because no foreign king receives narrator-elevated royal register here, **Hosea adds no new data to the still-owed `foreign_monarch_register` decision** (deferred since Ezra; flagged across the EZR/NEH/EST/DAN block and the Jeremiah §24 DECIDE). One-line note only. **STABLE** ✓. **Severity: GREEN.**

---

## 17. Messianic / committal surface — **STABLE (§0-compliant, restrained)**

Three forward-leaning surfaces, all handled with descriptive restraint that matches the Isaiah §6 / Jeremiah §6 committal-consensus policy:
- **3:5** "David their king" (דָּוִד מַלְכָּם) → **ดาวิดกษัตริย์ของพวกเขา** (plain), KD names the Davidic/messianic hope **descriptively** (cross-ref Ezek 34:23–24), no endorsement clause. Parallels Jeremiah 30:9.
- **6:2** "after two days… on the third day he will raise us up" → rendered literally (ในวันที่สามพระองค์จะทรงยกเราขึ้น); the KD calls it a "graded-numeral idiom for soon/surely" and does **not** impose an NT resurrection reading — restrained, §0-clean.
- **13:14** → the KD lets "both horizons stand" (immediate judgment vs the apostolic resurrection-victory reading of 1 Cor 15:55) without asserting fulfillment — the cleanest possible handling.

No summary carries an Isaiah-9:6-style "คือพระคริสต์" endorsement clause (the §0 regression the Ezekiel audit flagged is **absent** in Hosea). **STABLE** ✓. **Severity: GREEN.**

---

## 18. Mechanical (§1) + infrastructure

- **14/14** chapters: `output/check_reports/hosea_NN_review.md` (green) + `output/back_translations/hosea_NN.json` + `output/translations/hosea_NN.json` ✓
- **14/14** chapters: `output/textual_variants/hosea_NN.json` carrying the YHWH first-occurrence footnote — **complete coverage** (§1). Chs 2, 12, 14 additionally carry a reader-facing `versification_divergence` footnote; ch.13 carries a `reception_history_and_textual_note` (the 13:14 → 1 Cor 15:55 disclosure).
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings.**
- `check_phrase_consistency.py`: **0 violations across 38 audited locks.**
- `audit_inclusion_variants.py --book hosea --strict`: **0 candidates, exit 0** (correct — the inclusion-variant policy is NT-only; Hosea's MT/LXX matters route through the mt_vs_lxx policy, §13/§14).
- `check_divine_names.py --book HOS`: **exit 0, zero warnings** — the cleanest divine-name checker state of any major OT book.
- `check_versification_anchor.py --book HOS`: **exit 0** (1,421 map entries; all three Hosea divergence zones present).
- `git status output/`: only the re-ran-check artifact (`phrase_consistency.md`). No source-file dirt.
- **`export_to_usfm.py --book HOS`: FAILS — "Unknown book code: HOS."** The script's book table does not carry `HOS` (the same OT-USFM book-code-registration gotcha logged for JER/ISA/EZK/LAM/SNG in every prior OT audit). **Non-blocking infra gap** — flag for the maintainer to register `HOS`.
- **Versification-map commit hygiene (REVIEW).** All three Hosea MT/English divergence zones (chs **2, 12, 14**) are registered in `data/versification_map.json` — but the **HOS-14 zone entries + a `scripts/build_versification_map.py` change are uncommitted in the working tree** (present at session start as `M data/versification_map.json` + `M scripts/build_versification_map.py`). The check passes because the entries exist on disk, but per the documented "ship_chapter.sh doesn't stage the map" gotcha they need a **manual commit** before tagging or they will be lost. *(This audit branch deliberately does not touch them — it stages only `docs/end_of_book/hosea/`.)*

---

## Recommendation

**Hosea ships in the strongest corpus-hygiene shape of any book to date** — mechanically the cleanest divine-name state (zero checker warnings), full YHWH footnote coverage, all three MT/English versification zones registered + reader-footnoted, the 13:14 → 1 Cor 15:55 divergence disclosed exactly as the policy prescribes, and exemplary chesed / paqad / Baal / harlotry-leitwort locks. The single DECIDE is the **inherited, cross-book anthropomorphism question** Hosea re-demonstrates rather than creates.

Tag `book-hosea-v1` after:
1. Ben's decision on the **1 DECIDE** item: §7 anthropomorphism (ratify the first-person exception + define the face carve-out, OR reverse the 3 plain instances — and **reconcile with Isaiah/Jeremiah/Ezekiel §13**, the highest-value forward-protection action before the rest of the Twelve).
2. Ben's decisions on the **4 REVIEW** items: §13 (6:6 חֶסֶד/ἔλεος footer), §14 (14:3 "fruit of lips" MT-departure footer + reading confirmation), §15 (4:7 tiqqun disclosure), §18 (commit the HOS-14 map zone + build-script change).
3. Any spot-revisions executed + checks re-run clean.
4. New docs written as decided: **`spiritual_harlotry_metaphor_2026-06.md`** (§9), the **דַּעַת "knowledge of God" note** (§10); amendment to **`divine_anthropomorphism_thai_grammar_2026-05.md`** (§7, if ratifying the exception).
5. External AI sanity-check (§3 — the 4-item packet: §7, §13, §14, §9).
6. Infra (non-blocking): register `HOS` in `export_to_usfm.py`.
