## Item A — Textual-variant Tier-2 reader-footer gap (DECIDE; first Samuel↔Chronicles synoptic partner)

**The pattern:** 2 Samuel is the corpus's first book with a full Chronicles synoptic partner (1 Chr 11–21 ≈ 2 Sam 5–24) and carries several of the OT's most-discussed textual cruxes. **Every one is documented at Layer 1** (the per-verse `key_decisions` / `notes` fields) — a real improvement over 1 Samuel, whose end-of-book audit (§17) found the major variants shipped *silent*. **But none is lifted to the Layer-2 reader-facing chapter-footer** (`output/textual_variants/2samuel_NN.json`, which carries only the locked YHWH first-occurrence footnote — confirmed across all 24 files; zero `textual_variant`-type entries).

The corpus text-base policy (`ot_canon_and_text_base_2026-05.md`, §"When to depart from MT") lists four exception triggers. For **Trigger 1 — "obvious copyist error preserved by MT"** — it states the divergence must be recorded "in the verse's `key_decisions` field **plus a `[Tier 2]` verse-level footer note**." One 2 Sam verse (15:7) is a Trigger-1 *departure* from MT and is therefore policy-bound to carry the Tier-2 footer — which is absent.

**The five cruxes (shipped Thai follows MT unless noted):**

| Ref | Hebrew (MT) | Variant witness | Shipped Thai | English gloss |
|---|---|---|---|---|
| **15:7** | `מִקֵּץ אַרְבָּעִים שָׁנָה` (**forty** years) | LXX + Syriac + Vulgate + Josephus + some MT mss: "**four**" | **`เมื่อสี่ปีผ่านไป`** (four — *departs from MT*) | "After four years…" |
| **24:1** | `וַיָּסֶת אֶת־דָּוִד` (**YHWH** incited David) | 1 Chr 21:1: "**Satan** incited David" | `พระองค์ทรงยุยงดาวิด` (YHWH — MT) | "He [the LORD] stirred up David" |
| **24:9** | `שְׁמֹנֶה מֵאוֹת אֶלֶף … חֲמֵשׁ מֵאוֹת אֶלֶף` (800k / 500k) | 1 Chr 21:5: 1,100,000 / 470,000 | `แปดแสน … ห้าแสน` (MT) | "800,000 … 500,000" |
| **24:13** | `שֶׁבַע שָׁנִים רָעָב` (**seven** years famine) | LXX + 1 Chr 21:12: "**three**" | `การกันดารอาหารเจ็ดปี` (MT) | "seven years of famine" |
| **21:19** | `וַיַּךְ אֶלְחָנָן … אֵת גָּלְיָת הַגִּתִּי` (Elhanan killed **Goliath** the Gittite) | 1 Chr 20:5: "Lahmi the **brother of** Goliath" | `…ได้ตีโกลิอัทชาวกัท` (Goliath — MT) | "…killed Goliath the Gittite" |

Note that at 21:19 the shipped **Thai is more MT-faithful than the BSB English base**, which silently harmonizes to "the brother of Goliath." Likewise at 24:13 the BSB reads "three years" (following LXX/Chronicles) while the Thai keeps MT "seven." And at 15:7 the Thai has *adopted* the LXX/Syriac "four" against MT "forty." So the translation's textual-base decisions are real, deliberate, and visible only at Layer 1.

**15:7 `key_decisions` (shipped):** *"MT reads 'forty years' (אַרְבָּעִים שָׁנָה) — likely a copyist error. LXX + Syriac + Vulgate + Josephus + some MT mss read 'four years.' Rationale: 40 years = the whole length of David's reign. Most translators follow the older versions and read 'four years.' This project is normally MT-anchored — but in cases of clear scribal error, some editions choose the sensible reading. Here: preserve 'four years' per context + ancient versions + majority of translators."*

**24:1 `key_decisions` (shipped):** *"'sut' (Hiph'il, incited): contradicts 1 Chr 21:1, which says 'Satan incited David.' Scholarly explanation: God permits Satan to act (cf. Job 1–2; 1 Kgs 22:19–22) — the 2 Sam author views it from the angle of God's absolute sovereignty; the Chronicler from the angle of Satan as the agent. Eremos preserves the MT word — 'He incited' — understood within the framework of God's absolute sovereignty."*

**Two questions:**
1. The five cruxes are documented at Layer 1 but absent from the Layer-2 reader-facing chapter-footers. **15:7 in particular is a Trigger-1 MT-departure whose Tier-2 footer is mandated by the canon policy and is currently missing.** Should the project add Tier-2 chapter-footer entries (`output/textual_variants/2samuel_{15,21,24}.json`) for these five — summarizing the MT reading, the alternative witness (LXX / 1 Chr / Qumran), and the disposition — before tagging `book-2samuel-v1`? (No translation-surface edits are needed for 24:1 / 24:9 / 24:13 / 21:19; only the transparency layer.) Are all five worth reader-facing disclosure, or only the theologically/apologetically prominent ones (15:7, 24:1 YHWH/Satan, 21:19 Elhanan-Goliath)?
2. **15:7 specifically:** does MT "forty years" clear the Trigger-1 bar of "grammatically impossible, semantically nonsensical, or self-contradicting"? It is the *lectio difficilior* (harder reading) with strong external support for the easier "four" — but "forty" is *historically awkward*, not strictly nonsensical. Should the project keep the emended "four" (current behavior) + add the mandated footer, OR revert to the more conservative MT "forty" + footer? And how should the policy doc reconcile 15:7 (emends MT) with 24:13 (preserves MT "seven" against the same kind of LXX/Chronicles pressure) so the disposition does not read as an inconsistent MT policy?

---

## Item B — Adonai-YHWH compound prayer-vocative (2 Sam 7:18–29); the JDG/1SA forward-deferred cluster

**The pattern:** The Adonai-YHWH compound `אֲדֹנָי יְהוִה` ("Lord GOD" / "Sovereign LORD") was flagged in the Joshua and 1 Samuel end-of-book audits as a corpus-level register question and explicitly forward-deferred to **2 Sam 7:18–29 — David's covenant prayer, the densest compound-Adonai prayer in the OT (7 occurrences in 12 verses).** This is its first major recurrence after Joshua–Judges.

The locked policy (`divine_names_table_2026-05.md`) maps the compound to a single Thai surface: **`אֲדֹנָי יְהוִה` → `องค์พระผู้เป็นเจ้า`** (the compound collapses to avoid a "Lord Lord" reduplication; `key_decisions` records the underlying Hebrew). The lock's table row also gives a **vocative sub-form: `ข้าแต่องค์พระผู้เป็นเจ้า`**, anchored on JOS 7:7 (`אֲהָהּ אֲדֹנָי יְהוִה` "Alas, Lord GOD!" — a sentence-initial interjection).

**2 Sam 7 ships vocabulary-compliant with exemplary Layer-1 transparency** — all 7 occurrences render `องค์พระผู้เป็นเจ้า`, each with a `key_decisions` entry naming the compound:

| Ref | Hebrew | Shipped Thai | English gloss |
|---|---|---|---|
| 7:18 | `מִי אָנֹכִי אֲדֹנָי יְהוִה` | `…“องค์พระผู้เป็นเจ้า ข้าพระองค์เป็นใคร…”` | "Who am I, O Lord GOD…" |
| 7:19 | `…בְּעֵינֶיךָ אֲדֹנָי יְהוִה … תּוֹרַת הָאָדָם אֲדֹנָי יְהוִה` | `…องค์พระผู้เป็นเจ้า … องค์พระผู้เป็นเจ้า?` | "…in your eyes, O Lord GOD… is this your way with man, O Lord GOD?" |
| 7:22 | `עַל־כֵּן גָּדַלְתָּ אֲדֹנָי יְהוִה` | `เพราะเหตุนี้พระองค์ยิ่งใหญ่ องค์พระผู้เป็นเจ้า` | "Therefore you are great, O Lord GOD" |
| 7:28 | `וְעַתָּה אֲדֹנָי יְהוִה אַתָּה־הוּא הָאֱלֹהִים` | `และบัดนี้ องค์พระผู้เป็นเจ้า พระองค์ทรงเป็นพระเจ้า` | "And now, O Lord GOD, you are God" |
| 7:29 | `כִּי־אַתָּה אֲדֹנָי יְהוִה דִּבַּרְתָּ` | `เพราะพระองค์ องค์พระผู้เป็นเจ้า ตรัส` | "for you, O Lord GOD, have spoken" |

**The flag:** every occurrence omits the lock's vocative particle **`ข้าแต่`** — the prayer renders the bare `องค์พระผู้เป็นเจ้า`. This is **defensible**: the 2 Sam 7 compounds are mid-sentence *appositional* address ("who am I, **Lord GOD**"; "you are great, **Lord GOD**"), where Thai `ข้าแต่` (a sentence-initial deferential vocative particle) would read awkwardly — unlike JOS 7:7's sentence-initial interjection that naturally takes it. But the principle (appositional compound-vocative omits `ข้าแต่`; interjection compound-vocative takes it) is currently undocumented, and 2 Sam 7 is the corpus's defining test case for it.

**Question:** Is the bare `องค์พระผู้เป็นเจ้า` (no `ข้าแต่`) the right treatment for mid-sentence *appositional* compound-Adonai vocatives in sustained prayer — reserving `ข้าแต่องค์พระผู้เป็นเจ้า` for sentence-initial *interjection* vocatives (`אֲהָהּ`/`בִּי`/`אָנָּא` + Adonai-YHWH, per the JOS 7:7 anchor)? If so, should `divine_names_table_2026-05.md` be amended to record the appositional-vs-interjection distinction, with 2 Sam 7:18–29 cited as the appositional exemplar? Or should the densest compound-Adonai prayer in the OT carry the fuller `ข้าแต่` deferential register throughout to mark its theological weight?

---

## Item C — Synoptic / parallel-passage corpus doc (2 Sam 22 ≈ Ps 18; Samuel ↔ Chronicles)

**The pattern:** 2 Samuel introduces two parallel-passage relationships the corpus has not previously had to govern, and ships **excellent ad-hoc handling of both** — but with no corpus doc locking the policy for the many downstream parallels.

**(a) 2 Sam 22 ≈ Psalm 18.** David's song of deliverance appears near-verbatim in the Davidic appendix (2 Sam 22) and the Psalter (Ps 18). The shipped chapter-overview footer states: *"Chapter 22 = Ps 18 — the same song appears in two books (the Davidic appendix of 2 Sam + the Psalter). Eremos follows the 2 Sam 22 text — with minor variants vs Ps 18 (e.g., v.51 'magdol' in 2 Sam vs 'magdil' in Ps)."* Per-verse `notes` carry the Ps-18 correspondence and the NT echoes:
- **22:50** (`עַל־כֵּן אוֹדְךָ … בַּגּוֹיִם`) → cited directly by Paul at **Rom 15:9** (Layer-1 note).
- **22:28** (`עַם־עָנִי תּוֹשִׁיעַ` — "you save the humble people") → Magnificat **Luke 1:51–52** (Layer-1 note: "David's song is the root of Mary's song").

**(b) Samuel ↔ Chronicles.** 1 Chr 11–21 retells 2 Sam 5–24; the Item-A cruxes (24:1, 24:9, 24:13, 21:19) are all Samuel↔Chronicles synoptic differences, handled at Layer 1.

**The gap:** `decalogue_parallel_text_2026-05.md` exists for the Exod 20 // Deut 5 Decalogue but does not generalize. There is no doc locking: (i) that each parallel is translated independently from its own MT context; (ii) how inter-parallel variants are disclosed (Layer 1 vs Layer 2); (iii) the standard reader-footer phrasing for "Chronicles reads…". This forward-compounds to a large set: **Ps 14//53, Ps 40:13–17//70, Ps 108 (=57:7–11 + 60:5–12), 2 Sam 22//Ps 18, 2 Kgs 18:13–20:19//Isa 36–39, 2 Kgs 24:18–25:30//Jer 52, and the entire 1–2 Chronicles synoptic** — i.e., the Psalter and Chronicles, both major forthcoming books.

**Question:** Should the project write `synoptic_parallel_passages_2026-05.md` to lock the parallel-passage policy (independent translation from each book's own MT; Layer-1/Layer-2 disclosure of inter-parallel variants; standard footer phrasing) — and tie it to the Item-A Tier-2 disclosure decision so the Samuel↔Chronicles precedent set here governs Kings//Isaiah//Jeremiah and the Chronicles synoptic downstream? Is the 2 Sam 22 "follow this book's MT, footnote the Ps-18 variants" approach the right default for the Psalter when Ps 18 is reached?

---

## Item D — "Until this day" cross-book leitwort normalization

**The pattern:** The Deuteronomistic-History formula `עַד הַיּוֹם הַזֶּה` ("until this day") recurs across the Former Prophets. The corpus now ships **two competing Thai surfaces across three books**, with no locked canonical form in `leitwort_handling_policy_2026-05.md`:

| Book | Thai surface | Evidence |
|---|---|---|
| **Judges** | `จนถึงทุกวันนี้` (with `ทุก-` "every") | JDG audit §14 (6× majority) |
| **1 Samuel** | `จนถึงวันนี้` (bare) | 1SA audit §14 (8× uniform) |
| **2 Samuel** | `จนถึงวันนี้` (bare) | this audit §11 — 4:3, 6:8, 7:6, 18:18, … (uniform) |

**Sample (2SA):**
- **6:8** `וַיִּקְרָא לַמָּקוֹם הַהוּא פֶּרֶץ עֻזָּה עַד הַיּוֹם הַזֶּה` → `…เขาเรียกที่นั่นว่าเปเรซ-อุสซาห์ จนถึงวันนี้` ("…he called that place Perez-uzzah, to this day")
- **7:6** `לֹא יָשַׁבְתִּי בְּבַיִת לְמִיּוֹם הַעֲלֹתִי … עַד הַיּוֹם הַזֶּה` → `เพราะเราไม่ได้อาศัยอยู่ในบ้านตั้งแต่วันที่เรานำบุตรของอิสราเอลขึ้นจากอียิปต์จนถึงวันนี้` ("I have not dwelt in a house from the day I brought up Israel … to this day")

The Hebrew is identical at every occurrence corpus-wide; the variation is purely a Thai-surface choice. 2 Samuel reinforces the 1 Samuel bare-form, so the corpus is now **2 books (1SA + 2SA) on `จนถึงวันนี้` vs 1 book (JDG) on `จนถึงทุกวันนี้`**. The 1SA audit (§14) deferred the corpus-wide normalization decision; 2SA now makes the bare form the de-facto majority.

**Question:** Should `leitwort_handling_policy_2026-05.md` lock a single canonical Thai surface for `עַד הַיּוֹם הַזֶּה` — and is the bare **`จนถึงวันนี้`** (now the 1SA+2SA majority) the right choice, with JDG's `จนถึงทุกวันนี้` normalized to it? Or does the `ทุก-` ("every day until now") intensifier better capture the formula's etiological "and it remains so" force, arguing instead to normalize 1SA+2SA upward? This should be settled before more Former-Prophets ship (1–2 Kings recur the formula heavily).
