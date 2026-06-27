# Haggai — End-of-Book Review

**Date:** 2026-06-27
**Scope:** All 2 chapters of Haggai (English versification = MT throughout — Haggai carries **no** MT/English divergence zone); `glossary.json`; `docs/translator_decisions/` corpus. Haggai is the **twelfth Book-of-the-Twelve title** processed (after Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah). The divine-name inventory is **only** the bare Tetragrammaton (יהוה) and the **YHWH-Sabaoth** compound (יְהוָה צְבָאוֹת) — the latter is Haggai's *signature* title (≈14× across the two chapters, dense as in no other minor prophet) — both rendered uniformly on the `องค์พระผู้เป็นเจ้า` family with the per-chapter Layer-2 footnote present and correctly typed in **both** chapters. Two facts give the book editorial weight: **(1)** Haggai has **no** Adonai-YHWH compound and **no** standalone Adonai — so, like Nahum, it **sidesteps the open Amos §1 entirely**; and **(2)** Haggai is the corpus's **most messianically-dense minor prophet to date** — three footnotes invoke พระเมสสิยาห์ (the חֶמְדַּת כָּל־הַגּוֹיִם "Desire/treasure of nations" of 2:7, the "latter glory" of 2:9, and the Zerubbabel signet-ring of 2:23) — making the committal-messianic-surface discipline (Isaiah §0; the Ezekiel §14 regression) the live editorial axis here.

**Trigger:** Final chapter of Haggai (HAG 2) shipped via `scripts/ship_chapter.sh`; `scripts/detect_book_complete.py` fired the end-of-book audit.

**Mandate:** §2 (Editorial review) + §3 (External AI packet) of `docs/END_OF_BOOK_CHECKLIST.md`. **Assessment only — no translation JSON was modified.**

## Summary

- **9 cross-cutting items reviewed.**
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-haggai-v1`):
  - **§3 — the חֶמְדַּת כָּל־הַגּוֹיִם crux at 2:7** ("the **treasures** of all nations" vs. the traditional Christological "the **Desire** of [all] nations"). The Eremos body reads the **collective treasure** sense — keyed to the **plural** verb וּבָאוּ "they shall come," which matches a collective object, not a single figure — and footnotes the Vulgate/KJV singular-messianic reading. This is the book's signature interpretive fork: the MT itself is in grammatical tension (singular construct חֶמְדַּת against the plural verb), and the famous "Desire of Nations" reading (Handel's *Messiah*, "Come, Thou long-expected Jesus") makes this a high-visibility, ship-once-irreversible call. Like Joel's parallel messianic-vs-plain fork (2:23, the Teacher-of-Righteousness DECIDE), it warrants an **explicit Ben ratification** of the non-messianic surface before the v1 tag. The rendering is **correct and footnoted** under the project's MT-base + messianic-restraint policy; the DECIDE is for ratification, **not** because a change is proposed.
- **2 items flagged REVIEW** (worth Ben's confirmation; no change proposed):
  - **§5 — the messianic-reception surface cluster (2:9 "latter glory," 2:23 signet ring).** Haggai is the densest minor-prophet messianic-reception case; both are framed as **Christian reception** in the summaries (`คริสตชนเห็นว่า…`, `ปรากฏในลำดับพงศ์ของพระเมสสิยาห์ มัทธิว 1:12`) and footnoted, **not** asserted as bare fact — clean of the Ezekiel §14 regression. Flagged for confirmation that the reception-framing **level** is the intended Eremos surface.
  - **§9 — `export_to_usfm.py` rejects `HAG`** (infrastructure, non-blocking; the standing minor-prophet apparatus gap).
- **4 items LOCKED** — §1 (Tetragrammaton Layer-1 + Layer-2 footnote), §2 (YHWH-Sabaoth), §4 (anthropomorphism first-person-plain / third-person-royal), §8 (versification — no zone).
- **2 items STABLE** — §6 (OT→NT cross-quotation, 2:6 → Heb 12:26), §7 ("consider your ways" leitwort).
- **Mechanical gate: fully GREEN.** `check_key_term_consistency` 0 violations; `check_phrase_consistency` 0 violations (38 locks audited, 30 622 verses); `check_divine_names --all` shows **zero** Haggai entries in its warning list (no standalone-Adonai `C-soft` flags — Haggai has no Adonai at all — and no human-subject false-positive class); `audit_inclusion_variants --book haggai --strict` **0** candidates; both per-chapter `*_review.md` green; both `back_translations/haggai_NN.json` present; both `output/textual_variants/haggai_NN.json` present with the **correct** `tetragrammaton_convention_first_occurrence` footnote type in **both** chapters (no Joel-ch3 type-mismatch, no Micah-ch5 / Lamentations-ch2-3 missing-footnote gap); no versification-map entries owed (Haggai has no MT divergence zone).
- **External AI review (§3) packet:** focused **2-item** packet — the 2:7 חֶמְדַּת crux (§3, DECIDE) and the messianic-reception surface cluster (§5, REVIEW). The infra item (§9) is not an externally-reviewable translation question and is excluded, matching the Amos/Obadiah/Micah/Nahum/Habakkuk/Zephaniah packet scoping. All LOCKED/STABLE items are excluded.

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Divine names — Tetragrammaton Layer-1 uniform + Layer-2 footnote present in both chapters — **LOCKED**

YHWH appears densely in both chapters and is rendered **`องค์พระผู้เป็นเจ้า`** uniformly (Layer 1, `divine_names_table_2026-05`):

- **Ch.1:** 1:1, 1:2 (יְהוָה צְבָאוֹת), 1:3, 1:5 (יְהוָה צְבָאוֹת), 1:7 (יְהוָה צְבָאוֹת), 1:8, 1:9 (×2, incl. יְהוָה צְבָאוֹת), 1:12 (×2), 1:13 (×3, incl. מַלְאַךְ יְהוָה / נְאֻם־יְהוָה), 1:14 (יְהוָה צְבָאוֹת) — first occurrence footnoted at 1:1.
- **Ch.2:** 2:1, 2:4 (×3), 2:6 (יְהוָה צְבָאוֹת), 2:7 (יְהוָה צְבָאוֹת), 2:8 (יְהוָה צְבָאוֹת), 2:9 (×2, יְהוָה צְבָאוֹת), 2:10, 2:11 (יְהוָה צְבָאוֹת), 2:14, 2:15, 2:17, 2:18, 2:20, 2:23 (×3, incl. יְהוָה צְבָאוֹת ×2) — first occurrence footnoted at 2:1.

The Layer-2 apparatus is **complete and correct**: each chapter's `output/textual_variants/haggai_NN.json` carries a `tetragrammaton_convention_first_occurrence` entry that enumerates the YHWH verses and explicitly notes the dense יהוה צבאות → `องค์พระผู้เป็นเจ้าจอมโยธา` usage. `check_divine_names.py --all` reports **zero** Haggai entries in its corpus warning list. This is **cleanest-tier**: unlike Micah (Layer-2 footnote missing in ch.5), Lamentations (ch.2/ch.3 gap), or Joel (ch.3 wrong footnote type), Haggai's per-chapter first-occurrence footnote is present **and** correctly typed in both chapters. **LOCKED** ✓ (`divine_names_table_2026-05`). **Severity: GREEN.**

---

## 2. YHWH-Sabaoth (`יְהוָה צְבָאוֹת`) → `องค์พระผู้เป็นเจ้าจอมโยธา` — **LOCKED** (Haggai's signature title)

The compound is **Haggai's defining divine title** — it appears ≈14× across the two chapters (1:2, 1:5, 1:7, 1:9, 1:14; 2:6, 2:7, 2:8, 2:9 ×2, 2:11, 2:23 ×2), a density unmatched among the minor prophets and central to the book's rhetoric (the LORD-of-armies has the resources and the authority to rebuild his house). Every occurrence is rendered **`องค์พระผู้เป็นเจ้าจอมโยธา`**, **identical to the locked form** at `divine_names_table_2026-05` ("**องค์พระผู้เป็นเจ้าจอมโยธา** — Identical to already-shipped Jas 5:4; visual unity preserved across testaments") and matching the Zephaniah 2:9/2:10, Habakkuk 2:13, Nahum 2:14 / 3:5, Isaiah, Jeremiah, and Psalms uses of the same Hebrew form. Correctly distinct from the corpus's `พระเจ้าจอมโยธา`, which renders the *different* form `אֱלֹהֵי צְבָאוֹת` ("**God** of hosts"). The footnote glosses จอมโยธา = "commander of armies" for the reader. **LOCKED** ✓. **Severity: GREEN.**

---

## 3. The חֶמְדַּת כָּל־הַגּוֹיִם crux at 2:7 — "the treasures of all nations" vs. the Christological "Desire of Nations" — **DECIDE** (the v1 blocker)

Haggai 2:7 is the book's signature interpretive fork and one of the most famous Christological cruxes in the Twelve:

- **HEB (HAG 2:7):** `וְהִרְעַשְׁתִּי אֶת־כָּל־הַגּוֹיִם וּבָאוּ חֶמְדַּת כָּל־הַגּוֹיִם וּמִלֵּאתִי אֶת־הַבַּיִת הַזֶּה כָּבוֹד`
- **BSB:** "I will shake all the nations, and **they will come with all their treasures**, and I will fill this house with glory…"
- **TH (Haggai):** `เราจะเขย่าประชาชาติทั้งปวง และ**สิ่งล้ำค่าของประชาชาติทั้งหลายจะหลั่งไหลเข้ามา** และเราจะให้พระนิเวศนี้เต็มไปด้วยพระสิริ`

The Eremos body reads the **collective-treasure** sense (`สิ่งล้ำค่า`), and the `key_decisions` records the grammatical ground: the singular construct חֶמְדַּת is taken **collectively** because it governs the **plural** verb וּבָאוּ "they shall come" — a plural verb fits a collective object (the nations' treasures streaming in), not a single figure. The traditional reading — "the **Desire** / the **Desired-One** of all nations," a single messianic person (Vulgate *veniet desideratus cunctis gentibus*, KJV "the desire of all nations shall come") — is **footnoted**, not asserted in the body.

**Why DECIDE, not REVIEW.** Three things lift this above the routine MT-vs-variant confirmation:
1. **The MT is itself in grammatical tension** — singular construct noun, plural verb — which is precisely why the versions split. This is a genuine lexical-grammatical fork, not a settled reading the project is merely disclosing.
2. **It is among the highest-visibility Christological verses in the OT** — the "Desire of Nations" reading is embedded in Handel's *Messiah*, in "Come, Thou long-expected Jesus" ("Dear Desire of every nation"), and in centuries of Advent devotion. Shipping the collective reading is irreversible-once-public and deserves Ben's explicit eyes.
3. **Corpus precedent treats the parallel as DECIDE** — Joel 2:23 (the rain-vs-messianic-Teacher fork, הַמּוֹרֶה לִצְדָקָה) was flagged DECIDE and ratified (rain chosen, messianic footnoted, precedent-setting for the Twelve). Haggai 2:7 is the same shape: the natural/collective sense chosen in the body, the messianic sense footnoted.

The rendering is **correct and well-grounded** under RULES §0 (MT base) and the committal-messianic-surface restraint policy (don't surface a messianic figure as bare fact in the body). The DECIDE is a **ratification gate**, not a proposed change: confirm the collective "treasures" surface (messianic "Desire of Nations" footnoted) is the intended Eremos reading before `book-haggai-v1`. **Severity: AMBER (ratification wanted on the book's signature Christological crux before the tag).**

---

## 4. Divine anthropomorphism — first-person-plain vs. third-person-royal — **LOCKED**

Haggai exercises the contested first-person-plain sub-rule of `divine_anthropomorphism_thai_grammar_2026-05` repeatedly and correctly, and pairs it with the third-person-royal default:

- **First-person divine speech → plain `เรา`, no royal honorific:** 1:8 `וְאֶכָּבְדָה` "that I may be glorified" → `(เรา)จะได้รับเกียรติ`; 1:9 `וְנָפַחְתִּי בוֹ` "I blew on it" → `เราก็เป่ามันให้กระจายไป`; 1:13 / 2:4 `אֲנִי אִתְּכֶם` "I am with you" → `เราอยู่กับพวกเจ้า`; 2:6–7 `מַרְעִישׁ … וְהִרְעַשְׁתִּי … וּמִלֵּאתִי` "I am shaking / I will fill" → plain first-person; 2:14 `לְפָנַי` "before me" → plain `ต่อหน้าเรา` (the KD explicitly notes this is *not* a royal body-part); 2:17 `הִכֵּיתִי` "I struck" → `เราได้โบยตี`; 2:23 `אֶקָּחֲךָ … בָחַרְתִּי` "I will take you / I have chosen" → plain.
- **Third-person narration of God → royal `ทรง`:** 1:14 `וַיָּעַר יְהוָה אֶת־רוּחַ` "YHWH stirred up the spirit" → `องค์พระผู้เป็นเจ้าทรงเร้าจิตใจ` (royal `ทรงเร้า`; the KD notes רוּחַ here is the *people's* spirit, จิตใจ, so no divine-body-part question arises).

This is a **live first-person-plain compliance witness** to the open Isaiah/Jeremiah/Ezekiel §13 first-person-plain DECIDE — exactly the role Zephaniah 1:4 played — applied here at scale (six-plus first-person cases). The KDs at 1:12, 1:13, and 2:14 explicitly flag the "body-part-then-`ทรง` honorifics trap" and steer around it. Because the governing doc **exists** and Haggai follows it exactly, this is **LOCKED** ✓ (`divine_anthropomorphism_thai_grammar_2026-05`); the first-person cases reinforce, but do not re-open, §13. **Severity: GREEN.**

---

## 5. The messianic-reception surface cluster — 2:9 "latter glory" + 2:23 signet ring — **REVIEW**

Haggai is the corpus's **densest minor-prophet messianic-reception case**. Beyond the 2:7 crux (§3), two further texts carry a Christian-reception reading, and both are handled at the right altitude — reception framing in the summary + footnote, **not** bare assertion:

- **2:9** `גָּדוֹל יִהְיֶה כְּבוֹד הַבַּיִת הַזֶּה הָאַחֲרוֹן מִן־הָרִאשׁוֹן` "the latter glory of this house will be greater than the former" → `พระสิริยุคหลังของพระนิเวศนี้จะยิ่งใหญ่กว่าพระสิริยุคก่อน`. The thai_summary frames the Christian reading as **reception**: `คำพยากรณ์ที่**คริสตชนเห็นว่า**สำเร็จเมื่อพระเมสสิยาห์เสด็จเข้าสู่พระวิหารนี้` ("a prophecy that **Christians see as** fulfilled when the Messiah entered this temple"). The footnote likewise attributes the fulfilment reading to คริสตชน.
- **2:23** `וְשַׂמְתִּיךָ כַּחוֹתָם כִּי־בְךָ בָחַרְתִּי` "I will make you like my signet ring, for I have chosen you" → `เราจะทำให้เจ้าเป็นเหมือนแหวนตราของเรา เพราะเราได้เลือกเจ้าไว้แล้ว`. The summary + footnote note the **reversal of Jer 22:24** (Jehoiachin plucked off "like a signet ring") and that Zerubbabel `ปรากฏในลำดับพงศ์ของพระเมสสิยาห์ (มัทธิว 1:12)` ("appears in the Messiah's genealogy, Matt 1:12") — a genealogical-reception note, not a claim that Zerubbabel *is* the Messiah.

This holds the **committal-messianic-surface policy** cleanly (Isaiah §0; the regression Ezekiel §14 flagged, where 5+ summaries asserted bare `คือพระคริสต์` as fact): every Haggai messianic note is explicitly attributed to Christian reception or to the NT genealogy. Flagged **REVIEW** — not because anything is wrong, but because Haggai is the **densest** test of the restraint discipline so far (three messianic footnotes in one short book), and a deliberate confirmation that the reception-framing **level** is the intended Eremos surface is worth recording before the tag. **No change proposed.** This is the cluster most worth pairing with §3 for external eyes. **Severity: GREEN (reception-framed and footnoted; confirmation wanted on the densest messianic-reception book).**

---

## 6. OT→NT cross-quotation — 2:6 ("I will shake the heavens") → Hebrews 12:26 — **STABLE**

Haggai 2:6, `וַאֲנִי מַרְעִישׁ אֶת־הַשָּׁמַיִם וְאֶת־הָאָרֶץ` "I will shake the heavens and the earth," is directly quoted in **Hebrews 12:26** (ἔτι ἅπαξ ἐγὼ σείσω…) as a sign of the final judgment. The Eremos rendering — `เราจะเขย่าฟ้าสวรรค์และแผ่นดินโลก` — is footnoted with the Heb 12:26 citation (the v.7 `nt_citation_note` in `haggai_02.json`), so the cross-canonical link is available to the reader. The lemma `เขย่า` "shake" is carried consistently across 2:6, 2:7, and 2:21–22. This is `ot_nt_cross_quotation_thread_2026-05` applied at verse level; no Haggai-specific lock is owed (the thread doc governs the pattern). **STABLE** ✓. **Severity: GREEN.**

---

## 7. The "consider your ways" leitwort (`שִׂימוּ לְבַבְכֶם`) → `จงพิจารณา…ให้ดี` — **STABLE**

The summons שִׂימוּ לְבַבְכֶם "set your heart [on your ways]" is Haggai's structuring refrain, marking the pivots of the book — 1:5, 1:7 (diagnosis), and 2:15, 2:18 (the before/after line at the temple's refounding). It is rendered uniformly as `จงพิจารณาวิถีทางของพวกเจ้าให้ดี` / `จงพิจารณาให้ดี`, preserving the repetition that the reader is meant to hear as a drumbeat. This is `leitwort_handling_policy_2026-05` applied cleanly; no Haggai-specific doc is owed. **STABLE** ✓. **Severity: GREEN.**

---

## 8. Versification — no MT/English divergence zone — **LOCKED**

Haggai's two chapters follow a versification in which **MT = English throughout**; there is no offset zone (contrast Joel ch.3/4, Micah ch.4/5, Nahum ch.2). `grep` confirms **zero** Haggai entries are owed in `data/versification_map.json`, and the per-chapter `versification_*` check reports are green for both chapters. This is **cleanest-tier** alongside Amos, Obadiah, Habakkuk, and Zephaniah — no zone to register, nothing retrofitted. **LOCKED** ✓ (`verse_schema_and_versification_2026-05`). **Severity: GREEN.**

---

## 9. Infrastructure — `export_to_usfm.py` rejects `HAG` — **REVIEW (infra, non-blocking)**

`scripts/export_to_usfm.py` does not yet accept the Haggai book code (the standing minor-prophet apparatus gap, the same item flagged at Joel/Amos/Obadiah/Micah/Nahum/Habakkuk/Zephaniah). As part of this audit, `HAG` **has been registered** in `scripts/build_external_review_packet.py` (the `BOOKS` slug dict — it was already in `OT_CODES`, the same Micah/Zephaniah-class gap that fails the packet build until added) and in `scripts/audit_items_to_yaml.py` (`BOOK_SLUGS`). The `export_to_usfm.py` gap remains; it is a non-translation, non-blocking infrastructure item that does not affect the v1 tag. **Severity: GREEN (infra; does not gate the tag).**

---

## Items reviewed that need no action

- **No Adonai-YHWH compound and no standalone Adonai** — Haggai's divine-name inventory is *only* the bare Tetragrammaton and יהוה צבאות. Like **Nahum**, Haggai therefore **sidesteps the open Amos §1 entirely** — it offers neither a path-a nor a path-b witness, and `check_divine_names` produces **zero** Haggai warnings (no Amos-4:1-style standalone-Adonai false-positive class).
- **No named foreign monarch is addressed or quoted** — Darius appears **only** in the date formulas (1:1, 1:15, 2:10: `กษัตริย์ดาริอัส`), never spoken to or characterized, so the open foreign-monarch-register thread (Ezra→Daniel; Jeremiah/Ezekiel) is **not** implicated. Same true-negative class as Zephaniah.
- **The five-fold futility curse (1:6)** and the **covenant-curse triad** שִׁדָּפוֹן / יֵרָקוֹן / בָּרָד "blight / mildew / hail" (2:17, echoing Deut 28:22; 1 Kgs 8:37) → `โรคข้าวลีบ / ราข้าว / ลูกเห็บ` — the Deuteronomic curse vocabulary carried consistently and footnoted (the צְרוֹר נָקוּב "pierced bag" imagery note at 1:6).
- **The חֹרֶב / חָרֵב sound-play** (1:11 "drought" punning on 1:4/1:9 "ruins") — preserved-in-sense and footnoted at 1:11, the punishment (drought) mirroring the sin (the temple left in ruins).
- **The priestly-ruling object lesson (2:11–14)** — holiness is **not** contagious by contact but defilement **is** (טָמֵא) → the תּוֹרָה ruling rendered `คำวินิจฉัยทางธรรมบัญญัติ`, with the application footnoted; `check_key_term_consistency`-clean.
- **`מַלְאַךְ יְהוָה` at 1:13 = the prophet himself** → `ทูตขององค์พระผู้เป็นเจ้า` (Haggai *as messenger*, not the Angel of YHWH theophany) — correctly distinguished from the locked `malak_yhwh_2026-05` theophanic rendering, with the dual sense (ทูต / ทูตสวรรค์) and the hapax בְּמַלְאֲכוּת "commission" footnoted.
- **Inclusion variants** — `audit_inclusion_variants --book haggai --strict` found **0** candidates; no Tier-2 inclusion file is owed (§2.3 non-gap).

## Recommended new / amended translator-decisions docs

These are **recommendations only** — per the checklist, this audit recommends but does not author corpus docs. **None is *owed*** unless the §3 DECIDE resolves into a lock:

1. **`committal_messianic_surface_2026-06.md`** (§3, §5) — Haggai is the **densest minor-prophet messianic-reception case** (three footnotes: 2:7 Desire/treasure-of-nations, 2:9 latter-glory, 2:23 signet-ring/Matt 1:12), and the committal-messianic-surface discipline (ratified at Isaiah §0, regression-flagged at Ezekiel §14) is currently tracked only at audit level, **without a standalone corpus doc**. Haggai is the natural anchor: record the rule that messianic readings are surfaced as **reception** (`คริสตชนเห็นว่า…`) or via **NT-citation/genealogy footnote**, never as bare `คือพระคริสต์` in the body; and the policy that a contested messianic *lexeme* (חֶמְדַּת 2:7) takes its natural/collective sense in the body with the messianic reading footnoted (parallel to Joel 2:23). Author only if Ben elects to lift it (or as the resolution of the §3 DECIDE).

## Checklist for Ben before tagging `book-haggai-v1`

- [ ] **§3 DECIDE** — ratify the collective-treasure surface at 2:7 (`สิ่งล้ำค่าของประชาชาติ`, keyed to the plural verb וּבָאוּ), with the Christological "Desire of Nations" reading footnoted. **This blocks the tag.** No change proposed.
- [ ] **§5 REVIEW** — confirm the messianic-reception framing level at 2:9 (latter glory → Messiah entering the temple) and 2:23 (signet ring → Matt 1:12 genealogy) is the intended Eremos surface (reception-framed + footnoted; clean of Ezk §14). No change proposed.
- [ ] **§9 REVIEW** — acknowledge the `export_to_usfm.py` `HAG` gap (infra; non-blocking; packet/YAML registration done in this audit).
- [ ] *(Optional)* greenlight the `committal_messianic_surface` doc (§3/§5), anchored on Haggai.
- [ ] Tag `book-haggai-v1` after the §3 DECIDE is ratified and the two REVIEW confirmations are recorded.

*Status counts: 4 LOCKED · 2 STABLE · 2 REVIEW · 1 DECIDE.*
