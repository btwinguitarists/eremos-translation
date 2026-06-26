# Amos — End-of-Book Review

**Date:** 2026-06-26
**Scope:** All 9 chapters of Amos (146 verses, standard versification — Amos has **no** MT/English divergence zone); `glossary.json`; `docs/translator_decisions/` corpus. **The third Book-of-the-Twelve title in the corpus** (after Hosea and Joel) and the earliest of the writing prophets. Amos inherits Joel's **יוֹם יְהוָה "Day of the LORD"** leitwort and famously **reverses** it (5:18–20: "darkness, not light"). Two of its passages are quoted in **already-shipped Acts**: **5:25–27 → Acts 7:42–43** (Stephen, Sakkuth/Kiyyun, LXX) and **9:11–12 → Acts 15:16–17** (James at the Jerusalem Council, the fallen booth of David, LXX). Amos is also the corpus's densest concentration of the **אֲדֹנָי יְהוִה "Lord GOD"** compound outside Ezekiel — and the audit's central finding is that Amos renders that compound **differently from the entire rest of the corpus.**
**Trigger:** AMO 9 shipped (last chapter, commit `d30a865f`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — **no translation changes made.**

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) pass: 9/9 chapters have green per-chapter reports + back-translations + translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks); `check_versification_anchor.py` clean (Amos has no divergence zone); `git status output/` clean. `check_divine_names.py --book AMO` exits 0 with **one soft warning** (4:1 — a **false positive**, see §6). **But the mechanical gate does not enforce the *surface form* of the Adonai-YHWH compound, and that is exactly where Amos drifts from the corpus** — see §1, the one item that genuinely blocks the tag.

- **2 items flagged DECIDE** (Ben choice needed before tagging `book-amos-v1`):
  - **§1 — אֲדֹנָי יְהוִה "Lord GOD" compound is SURFACED in Amos (`องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`) where the entire rest of the corpus COLLAPSES it to bare `องค์พระผู้เป็นเจ้า`.** This is a genuine cross-book divine-name inconsistency on the single most frequent divine title in the book (**20 verses**, 19 of them the *plain* mid-sentence compound). The locked rule (`divine_names_table_2026-05.md` row 22; confirmed by the Ezekiel, Isaiah, and Jeremiah audits) drops Adonai → bare `องค์พระผู้เป็นเจ้า`; Ezekiel renders all **217** occurrences bare, Isaiah ~30 bare, Jeremiah bare mid-sentence. Amos marks Adonai **everywhere.** The chapter `key_decisions` justify this by citing a doc, **`adonai_yhwh_2026-05`, that does not exist.** The mechanical checks cannot see this (divine-name *surface* forms aren't enforced). **This is the headline blocker.** See §1.
  - **§2 — 9:11–12 the fallen booth of David + the MT/LXX/Acts 15 fork.** Amos's great turn-to-hope (`סֻכַּת דָּוִיד הַנֹּפֶלֶת` → `พลับพลาของดาวิดที่ล้มลง`) is the verse James quotes (from the **LXX**) at the Jerusalem Council to authorize the Gentile mission (Acts 15:16–17). The MT/LXX divergence is a **one-letter** pair (`אֱדוֹם`/`אָדָם` "Edom"/"mankind"; `יִירְשׁוּ`/`יִדְרְשׁוּ` "possess"/"seek") that turns *conquest of Edom* into *conversion of mankind*. Eremos follows the **MT surface** ("possess the remnant of Edom") and footnotes the LXX/Acts reading — the correct application of the committal-messianic-surface policy ratified at Isaiah and applied at Joel 2:23. **Ben should explicitly ratify "MT-primary, LXX/Acts-in-footnote" for this marquee messianic surface** (it sets precedent for Micah 5, Zechariah, etc.), and confirm the `พลับพลา` rendering (see §2). **No translation change is proposed — this is a ratification gate.**

- **4 items flagged REVIEW** (worth Ben's confirmation):
  - **§7 — 5:25–27 → Acts 7:42–43 (Stephen's speech).** The astral-deity names `סִכּוּת`/`כִּיּוּן` (Sakkuth/Kiyyun) follow the **MT** (→ สิคูท/คิยยูน); Acts 7:43 quotes the **LXX** ("Moloch … Rephan," already shipped). The amos_05 footnote names the Acts citation. Confirm the policy (translate each from its own base, footnote the citation) and whether the substantive name-divergence clears the Tier-2 reader-footer floor — the same question raised at Joel §9 (2:31 *dreadful*/*glorious*) and Jeremiah §9 (31:32 → Heb 8:9).
  - **§9 — 7:14 `לֹא־נָבִיא אָנֹכִי` "I was/am no prophet."** The verbless clause is tense-ambiguous; the Thai reads present **`ข้าพเจ้าไม่ใช่ผู้เผยพระวจนะ`** ("I am not a prophet") while BSB reads past ("I *was* not"). A famous interpretive crux (denial-of-office vs denial-of-guild-membership). Confirm the present-tense reading and whether it warrants a reader note.
  - **§10 — the Sabaoth-stack rendering (`พระเจ้าจอมโยธา` with `พระเจ้า`).** Amos's `יְהוָה אֱלֹהֵי צְבָאוֹת` / `אֲדֹנָי יְהוִה אֱלֹהֵי הַצְּבָאוֹת` ("LORD God of Hosts") are rendered with `พระเจ้าจอมโยธא`, whereas `divine_names_table` row 23 locks bare `יְהוָה צְבָאוֹת` → `องค์พระผู้เป็นเจ้าจอมโยธา` (no `พระเจ้า`). Amos's forms legitimately carry `אֱלֹהֵי` "God of," so `พระเจ้า` is defensible — but it interacts with §1 (the `ผู้ทรงเป็นเจ้านาย` marking) and should be normalized together with it. See §10.
  - **§11 — `export_to_usfm.py` still rejects `AMO`** ("Unknown book code"), the recurring OT book-code gotcha (same open state as ISA/EZK/LAM/JOL). Not a translation issue and not a tag blocker; Paratext export of Amos is impossible until the code is registered. AMO **is** already registered in `build_external_review_packet.py`. See §11.

- **STABLE-but-undocumented patterns recommending doc-lift / note:**
  - **§3 — the `עַל־שְׁלֹשָׁה … וְעַל־אַרְבָּעָה` "for three transgressions, and for four" graduated-numerical formula** (8× in chs 1–2) → **`สามครั้ง หรือสี่ครั้ง เราจะไม่ยอมระงับการลงโทษ`**, held verbatim across all eight oracles. The book's structural signature; no corpus doc. **Recommend `graded_numerical_x_x_plus_one_2026-06.md`** (forward-protects Prov 6:16; 30:15–31; Job 5:19; Mic 5:4).
  - **§4 — the `וְלֹא־שַׁבְתֶּם עָדַי` "yet you did not return to Me" refrain** (5×: 4:6, 8, 9, 10, 11) → **`ถึงกระนั้น พวกเจ้าก็ไม่ได้กลับมาหาเรา`**, uniform. STABLE; verse-level rationale; optional note.
  - **§5 — `יוֹם יְהוָה` "Day of the LORD"** (5:18, 5:20; cosmic-darkness form 8:9) → **`วันแห่งองค์พระผู้เป็นเจ้า`**, matching Joel. **Reinforces the `day_of_the_lord_leitwort_2026-06.md` doc recommended at the Joel audit** (still un-written — Joel is also un-tagged). Amos is the leitwort's first OT inheritor and its first *reversal*. Write the doc once, covering both books.
  - **§8 — the three creation-doxologies** (4:13; 5:8–9; 9:5–6) → the `…שְׁמוֹ` "…is his name" colophons render uniformly (`พระนามของพระองค์คือ องค์พระผู้เป็นเจ้า` / `…พระเจ้าจอมโยธา`). STABLE; well-handled; optional hymn-fragment note.

- **External AI review (§3) pending.** Suggested 4-item packet: the Adonai-YHWH surfacing conflict (§1 DECIDE — the load-bearing item); the 9:11–12 booth-of-David MT/LXX/Acts-15 fork (§2 DECIDE); the 5:25–27 → Acts 7 reception surface (§7 REVIEW); the 7:14 "I was/am no prophet" tense (§9 REVIEW).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. אֲדֹנָי יְהוִה "Lord GOD" compound — SURFACED in Amos vs the LOCKED bare-collapse corpus rule — **DECIDE**

**This is the one item that genuinely blocks `book-amos-v1`.** It is invisible to every mechanical check (none of them enforce the *surface form* of the Adonai-YHWH compound), and it is a direct, visible conflict with the locked corpus rendering on the **single most frequent divine title in the book.**

### The locked rule

`docs/translator_decisions/divine_names_table_2026-05.md` row 22:

> | אֲדֹנָי יְהוִה (Adonai YHWH; "Lord GOD") | **องค์พระผู้เป็นเจ้า** | Compound collapses to single Thai rendering; `key_decisions` records the underlying Adonai-YHWH compound |

The same doc's §"Mid-sentence appositional" sub-rule (2026-05-23) and the **Jeremiah audit §3** confirm: the mid-sentence appositional compound `כֹּה אָמַר אֲדֹנָי יְהוִה` / `נְאֻם אֲדֹנָי יְהוִה` **drops Adonai** → bare **`องค์พระผู้เป็นเจ้า`**. The corpus has executed this consistently:

- **Ezekiel** — all **217** `אֲדֹנָי יְהוִה` occurrences → bare `องค์พระผู้เป็นเจ้า` (EZK audit; zero occurrences of the marked form in the Ezekiel translations).
- **Isaiah** — ~30 → bare (e.g. Isa 7:7 `อค์พระผู้เป็นเจ้าตรัสดังนี้`).
- **Jeremiah** — bare mid-sentence (e.g. Jer 5:7). The *only* Jeremiah departures are the **`אֲדֹנָי יְהוִה צְבָאוֹת` triple-stack** in 5 Oracles-Against-the-Nations climaxes (46:10×2, 49:5, 50:25, 50:31), which the JER audit §3 flagged as **REVIEW** ("possibly an intentional OAN-emphasis convention").

So across the corpus, the marked form `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` appears **only** in the Jeremiah OAN tsevaot-stack (already a flagged REVIEW) and a single Psalms verse.

### What Amos does

Amos renders the compound `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` ("the LORD who is the Lord/Master") in **20 verses** — and **19 of them are the *plain* `אֲדֹנָי יְהוִה`** (not the tsevaot-stack), i.e. exactly the mid-sentence appositional form the locked rule says to render bare:

| Verse | Hebrew form | Amos Thai | Locked-rule Thai |
|---|---|---|---|
| 1:8 | `אָמַר אֲדֹנָי יְהוִה` | องค์พระผู้เป็นเจ้า**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 3:7 | `אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 3:8 | `אֲדֹנָי יְהוִה דִּבֶּר` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 3:11 | `כֹּה אָמַר אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 3:13 | `אֲדֹנָי יְהוִה אֱלֹהֵי הַצְּבָאוֹת` | …**ผู้ทรงเป็นเจ้านาย** พระเจ้าจอมโยธา | (see §10) |
| 4:2 | `נִשְׁבַּע אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 4:5 | `נְאֻם אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 5:3 | `כֹּה אָמַר אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 6:8 | `נִשְׁבַּע אֲדֹנָי יְהוִה … אֱלֹהֵי צְבָאוֹת` | …**ผู้ทรงเป็นเจ้านาย** | (stack) |
| 7:1, 7:2, 7:4, 7:5, 7:6 | vision-formula `אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 8:1, 8:3, 8:9, 8:11 | `אֲדֹנָי יְהוִה` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |
| 9:5, 9:8 | `אֲדֹנָי יְהוִה (הַצְּבָאוֹת)` | …**ผู้ทรงเป็นเจ้านาย** | องค์พระผู้เป็นเจ้า |

Every one of these chapter `key_decisions` carries the same justification string:

> "Layer 1: אֲדֹנָי יְהוִה → องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย (contiguous, **adonai_yhwh_2026-05**); יהוה → องค์พระผู้เป็นเจ้า."

**The cited doc `adonai_yhwh_2026-05` does not exist** in `docs/translator_decisions/` (no file matches `*adonai_yhwh*`). The translator appears to have adopted a local Amos convention and back-referenced a phantom doc — so there is no audited corpus decision behind the departure.

### Why it matters / why DECIDE

- It is **visible in the rendered text** (not buried in `key_decisions`), so a reader comparing Amos to Ezekiel/Isaiah will see two different surfaces for the same Hebrew compound — the precise kind of forward-compounding drift the end-of-book gate exists to catch.
- It is the **dominant divine title of the book** (the vision cycle 7:1–9:8 is saturated with it), so the drift is not marginal.
- The corpus weight is overwhelmingly on the **bare** side (Ezekiel 217 + Isaiah 30 + Jeremiah, all locked + audited).

**Ben must decide between two paths:**

- **(a) Normalize Amos down to the locked bare form** — re-render all 19 plain `อค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` → `องค์พระผู้เป็นเจ้า` (and resolve the 3:13/6:8/9:5 stacks per §10). This conforms Amos to Ezekiel/Isaiah/Jeremiah and the divine_names_table. **Recommended**, as it touches the fewest other books and respects the existing lock. (A "rev" pass per the checklist's post-ship procedure, or before the v1 tag.)
- **(b) Ratify a deliberate marking convention** — accept that `אֲדֹנָי יְהוִה` should *surface* the doubled-lord, write the real `adonai_yhwh_2026-06.md` doc, and **also** revisit the Jeremiah OAN-split REVIEW (§3 there) and the 217 Ezekiel bare occurrences for consistency. This is the larger, more disruptive path and would reopen settled books.

**Either way, the phantom `adonai_yhwh_2026-05` citation must be resolved** (write the doc, or strike the citation when normalizing). **Severity: RED — the single blocker.**

---

## 2. 9:11–12 the fallen booth of David + the MT/LXX/Acts 15:16–17 fork — **DECIDE**

Amos's hinge from doom to hope, and the verse James cites at the Jerusalem Council to ground the Gentile mission. Two layers need Ben's ratification.

**(i) The MT/LXX divergence — handled correctly, ratify the policy.** The Hebrew/Thai:

- **9:12 HEB (MT):** `לְמַעַן יִירְשׁוּ אֶת־שְׁאֵרִית אֱדוֹם וְכָל־הַגּוֹיִם`
- **TH (MT surface):** `เพื่อพวกเขาจะได้ครอบครองชนเอโดมที่เหลืออยู่ และครอบครองประชาชาติทั้งปวงที่ถูกเรียกตามนามของเรา`

The **LXX** (which Acts 15:17 quotes) reads `ὅπως ἐκζητήσωσιν … τὸν κύριον` — "that **the remnant of mankind** (`אָדָם` for `אֱדוֹם`) may **seek** (`יִדְרְשׁוּ` for `יִירְשׁוּ`) the Lord." A **one-consonant** difference (ד/ר are near-identical in square script) turns Israel's *possession of Edom* into the nations' *seeking of God* — the textual basis for James's Gentile-inclusion argument. The amos_09 KD + `notes` already disclose the LXX/Acts reading explicitly. This is the **committal-messianic-surface policy** — translate the plain MT surface, footnote the messianic/NT reception — exactly as ratified at the **Isaiah audit** and applied at **Joel 2:23**.

**(ii) The messianic surface — restraint, ratify.** `סֻכַּת דָּוִיד הַנֹּפֶלֶת` is rendered plainly as the fallen Davidic dynasty (`พลับพลาของดาวิดที่ล้มลง`), with the christological/Acts fulfilment in apparatus, **not** baked into the rendered text (no "คือพระคริสต์" assertion — clean of the §0 regression flagged at Ezekiel §14). This is correct and consistent.

**Why DECIDE, not REVIEW:** it is the book's marquee messianic/NT-cited verse; its disposition sets precedent for the rest of the Twelve's messianic surfaces (Micah 5:2; Zechariah's Branch/booth imagery); and it is the natural place to **log the Davidic-restoration MT/LXX policy as a corpus precedent.** Ben should also **confirm the `พลับพลา` rendering** of `סֻכָּה`: `พลับพลา` connotes a royal pavilion/tabernacle, while `סֻכָּה` here is a humble "booth/hut" (the KD's own gloss) — `พลับพลา` may over-elevate the deliberately lowly image, though it reads naturally and carries the Davidic register. **No translation change is proposed pending Ben's call. Severity: the second tag-gating item (ratification).**

---

## 3. The `עַל־שְׁלֹשָׁה … וְעַל־אַרְבָּעָה` graded-numerical formula — **STABLE (recommend corpus doc)**

The structural signature of chs 1–2: eight oracles, each opening `כֹּה אָמַר יְהוָה עַל־שְׁלֹשָׁה פִּשְׁעֵי X וְעַל־אַרְבָּעָה לֹא אֲשִׁיבֶנּוּ` → **`องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า เพราะการล่วงละเมิดของ X สามครั้ง หรือสี่ครั้ง เราจะไม่ยอมระงับการลงโทษ`**, held **verbatim** across all eight (Damascus, Gaza, Tyre, Edom, Ammon, Moab, Judah, Israel). The "x / x+1" graded-numerical idiom (a full, overflowing measure of guilt) and `לֹא אֲשִׁיבֶנּוּ` "I will not turn it back" → `เราจะไม่ยอมระงับการลงโทษ` are rendered consistently and explained at 1:3. **STABLE** — uniform and principled, no corpus doc. **Recommend `graded_numerical_x_x_plus_one_2026-06.md`** to forward-protect Prov 6:16; 30:15–31; Job 5:19; Mic 5:4 (Sirach too if deuterocanon is ever in scope). **Severity: GREEN.**

---

## 4. The `וְלֹא־שַׁבְתֶּם עָדַי` "yet you did not return to Me" refrain — **STABLE**

The five-fold refrain sealing each discipline in 4:6–11 (famine, drought, blight, plague, Sodom-overthrow) → **`ถึงกระนั้น พวกเจ้าก็ไม่ได้กลับมาหาเรา`** (4:6, 8, 9, 10, 11), uniform. The escalating-discipline structure and the `שׁוּב` "return/repent" root land consistently. **STABLE** ✓ — verse-level rationale; optional note. **Severity: GREEN.**

---

## 5. `יוֹם יְהוָה` "Day of the LORD" — **STABLE (reinforces the Joel doc recommendation)**

Rendered **`วันแห่งองค์พระผู้เป็นเจ้า`** — identical to Joel — at 5:18 and 5:20, with the cosmic-darkness form (sun down at noon, 8:9) carrying the same theology without the lexical phrase. Amos is the **first OT inheritor** of Joel's leitwort and its **first reversal**: Israel longed for the Day as vindication; Amos declares it `חֹשֶׁךְ וְלֹא־אוֹר` "darkness, not light" → `ความมืด ไม่ใช่ความสว่าง`. The form matches the `glossary.json` ἡμέρα κυρίου entry and the already-shipped Acts 2:20 / 1 Thess 5:2 / 2 Pet 3:10 surfaces. **This directly reinforces the `day_of_the_lord_leitwort_2026-06.md` doc recommended at the Joel audit (§5) — still un-written (Joel is also un-tagged).** The doc should be authored once, covering Joel's institution and Amos's reversal, as the canonical reference for Obadiah/Zephaniah/Malachi. **Severity: GREEN (consistency); doc-lift recommended jointly with Joel.**

---

## 6. Divine names: Tetragrammaton, standalone Adonai, the 4:1 false positive — **LOCKED**

- **`יְהוָה` Tetragrammaton → `องค์พระผู้เป็นเจ้า`** (Layer 1) in every occurrence, each KD citing `divine_names_table_2026-05`. The thesis-verse roar (1:2, shared verbatim with Joel 4:16), the covenant seal (9:15 `יְהוָה אֱלֹהֶיךָ` → `องค์พระผู้เป็นเจ้าพระเจ้าของเจ้า`), the `נְאֻם־יְהוָה` / `אָמַר יְהוָה` formulas — all uniform. **LOCKED** ✓.
- **Standalone third-person `אֲדֹנָי` → `องค์เจ้านาย`** (the plumb-line and altar visions, 7:7, 7:8, 9:1; and within the title-cluster 5:16) — matches `divine_names_table` row "third-person reference → องค์เจ้านาย" exactly. **LOCKED** ✓. (Note: this is the *correct* handling of bare Adonai — and stands in deliberate contrast to the §1 problem, which is about the *compound* `אֲדֹנָי יְהוִה`, not bare Adonai.)
- **4:1 `check_divine_names` warning is a FALSE POSITIVE.** The checker flags 4:1 as possibly-missing `องค์เจ้านาย`, but the Hebrew is `הָאֹמְרֹת לַאֲדֹנֵיהֶם` — `אֲדֹנֵיהֶם` ("to **their** lords/husbands," 3mp suffix), the cows-of-Bashan women addressing their **human** husbands, correctly rendered `แก่สามีของตน` ("to their husbands"). No divine referent; no `องค์เจ้านาย` owed. Same false-positive class as the Daniel 12:8 case. **Severity: GREEN.**

---

## 7. 5:25–27 → Acts 7:42–43 (Stephen) — Sakkuth/Kiyyun MT vs Moloch/Rephan LXX — **REVIEW**

Stephen's speech (Acts 7:42–43) quotes Amos 5:25–27 from the **LXX**, which differs substantively from the MT Amos ships:

| Point | Amos (MT-based) | Acts 7 (LXX-based, shipped) |
|---|---|---|
| 5:26 deities | `סִכּוּת מַלְכְּכֶם … כִּיּוּן` → **สิคูทกษัตริย์… คิยยูน** (Sakkuth/Kiyyun, Assyrian astral gods) | "**Moloch** … **Rephan**" (LXX vocalization/substitution) |
| 5:27 exile | "beyond Damascus" → **ไกลออกไปเลยเมืองดามัสกัส** | "beyond **Babylon**" (Acts) |

The MT surface is correctly followed; the amos_05 KD + `notes` explicitly name the LXX/Acts 7:43 citation. This is the **same disclosure question** raised at Joel §9 and Jeremiah §9: (1) confirm the policy — each text translated from its own base, the NT citation footnoted, no harmonizing of the OT surface to the NT quotation; (2) decide whether the substantive **Sakkuth→Moloch / Damascus→Babylon** divergence clears the Tier-2 reader-footer floor, or whether the existing KD/`notes` disclosure suffices. (Amos 5:25–27 currently has the disclosure in the verse `notes`, not a dedicated `textual_variants` footer.) **Severity: YELLOW (apparatus/disclosure).**

---

## 8. The three creation-doxologies (4:13; 5:8–9; 9:5–6) — **STABLE**

Amos's hymnic fragments — the God who forms mountains and creates wind (4:13), made the Pleiades and Orion (5:8), builds his chambers in heaven (9:6) — each close with the `…שְׁמוֹ` "…is his name" colophon, rendered uniformly: `พระนามของพระองค์คือ องค์พระผู้เป็นเจ้า` (5:8; 9:6) / `…พระเจ้าจอมโยธา` (4:13). The astral terms `כִּימָה`/`כְּסִיל` → กลุ่มดาวลูกไก่/กลุ่มดาวนายพราน match the Job 9:9; 38:31 corpus surface. **STABLE** ✓ — well-handled, footnoted; optional "doxology-fragment" note. (The `אֱלֹהֵי צְבָאוֹת` element of 4:13's colophon ties into §10.) **Severity: GREEN.**

---

## 9. 7:14 `לֹא־נָבִיא אָנֹכִי` — "I was/am no prophet" — **REVIEW**

Amos's reply to Amaziah is a tense-ambiguous verbless clause. The Thai reads **present**: `ข้าพเจ้าไม่ใช่ผู้เผยพระวจนะ และไม่ใช่ลูกของผู้เผยพระวจนะ` ("I am not a prophet, nor a son of a prophet"). BSB reads **past** ("I *was* not a prophet"). The choice carries exegetical weight: the **present** reading makes Amos disclaim the *professional prophet-guild* (he is a layman `בּוֹקֵר`/`בּוֹלֵס שִׁקְמִים` called directly by YHWH, v.15) while still prophesying; the **past** reading makes it a biographical "I used to be no prophet — until God took me." The present reading is the majority modern view and is internally coherent with v.15's `וַיִּקָּחֵנִי יְהוָה` "the LORD *took* me." **Confirm** the present-tense rendering and whether the past/present ambiguity warrants a one-line reader note. **Severity: YELLOW (exegetical choice, well-defensible).**

---

## 10. The Sabaoth-stack rendering `พระเจ้าจอมโยธา` — **REVIEW (resolve with §1)**

`divine_names_table` row 23 locks **`יְהוָה צְבָאוֹת` → `องค์พระผู้เป็นเจ้าจอมโยธา`** (no `พระเจ้า`; identical to the shipped Jas 5:4). Amos's occurrences are the **fuller** `יְהוָה אֱלֹהֵי צְבָאוֹת` / `אֲדֹנָי יְהוִה אֱלֹהֵי הַצְּבָאוֹת` ("LORD **God** of Hosts"), and are rendered with `พระเจ้าจอมโยธא` (the `אֱלֹהֵי` "God of" → `พระเจ้า`):

| Verse | Hebrew | Amos Thai |
|---|---|---|
| 4:13 | `יְהוָה אֱלֹהֵי־צְבָאוֹת שְׁמוֹ` | องค์พระผู้เป็นเจ้า**พระเจ้าจอมโยธา** |
| 5:14, 5:15 | `יְהוָה אֱלֹהֵי צְבָאוֹת` | องค์พระผู้เป็นเจ้า**พระเจ้าจอมโยธา** |
| 5:16 | `יְהוָה אֱלֹהֵי צְבָאוֹת אֲדֹנָי` | องค์พระผู้เป็นเจ้าพระเจ้าจอมโยธา **องค์เจ้านาย** |
| 5:27 | `יְהוָה אֱלֹהֵי־צְבָאוֹת שְׁמוֹ` | องค์พระผู้เป็นเจ้า**ผู้ทรงพระนามว่าพระเจ้าจอมโยธา** |
| 3:13, 9:5 | `אֲדֹנָי יְהוִה (אֱלֹהֵי) (הַ)צְּבָאוֹת` | …ผู้ทรงเป็นเจ้านาย **(พระเจ้า)จอมโยธา** |

The `אֱלֹהֵי → พระเจ้า` expansion is **defensible** (the Hebrew genuinely adds "God of"), and `צְבָאוֹת → จอมโยธา` is the locked element. So this is **lower-severity than §1** — but the two interact (3:13, 6:8, 9:5 combine the §1 marking *and* the Sabaoth stack), so **normalize them together.** Confirm: `יְהוָה אֱלֹהֵי צְבָאוֹת` → `องค์พระผู้เป็นเจ้าพระเจ้าจอมโยธา` (Amos's current form) is the intended OT rendering of the fuller stack, distinct from the bare `יְהוָה צְבָאוֹת` → `องค์พระผู้เป็นเจ้าจอมโยธา`. **Severity: YELLOW (resolve in the same pass as §1).**

---

## 11. Infrastructure — `export_to_usfm.py` rejects `AMO` — **REVIEW (infra, non-blocking)**

`python3 scripts/export_to_usfm.py --book AMO` → `Unknown book code: AMO`. The recurring OT book-code gotcha (same open state as ISA/EZK/LAM/JOL — the export script's internal code table lags the YAML/packet tables). It blocks Paratext (.SFM) export of Amos but is **not** a translation issue and **not** a v1-tag blocker. **AMO is already registered** in `build_external_review_packet.py` (BOOKS list); `export_to_usfm.py` should be registered in the same pass when the maintainer next touches it. **Severity: YELLOW (infra, non-blocking).**

---

## Items reviewed that need no action

- **`נִחַם` divine relenting** (7:3, 7:6) → `ทรงเปลี่ยนพระทัย` — matches the Joel 2:13–14 surface and `nicham_divine_relenting_2026-05.md`. **LOCKED** ✓.
- **Divine first-person anthropomorphism** — "my hand" `יָדִי` (1:8 `หันมือของเรา`; 9:2 `มือของเรา`) → plain `มือ`; "my eyes" 1st-person `עֵינִי` (9:4 `จับตาดู`) plain vs 3rd-person `עֵינֵי אֲדֹנָי יְהוִה` (9:8 `ทอดพระเนตร`) royal; "my holy name" (2:7 `พระนามบริสุทธิ์ของเรา`). All **compliant with `divine_anthropomorphism_thai_grammar_2026-05.md`** (first-person body-part → plain; third-person with divine title → royal). Amos is a **clean, non-friction data point** for the open cross-corpus first-person-plain DECIDE (Isaiah/Jeremiah/Ezekiel/Hosea) — it does not move it. **LOCKED** ✓.
- **Paronomasia / wordplay** — `בֵּית־אֵל`/`אָוֶן` (5:5), `Lo-debar`/`Karnaim` (6:13), `קַיִץ`/`קֵץ` summer-fruit/end (8:1–2) — all footnoted per `wordplay_and_paronomasia_2026-05.md`. **LOCKED** ✓.
- **Hapax legomena** — Amos is hapax-dense (~20: `דּוּגָה`, `הַרְמוֹן`, `בָּשַׁס`, `מִרְזַח`, `כְּבָרָה`, etc.); each is glossed in `notes`. No corpus-level issue. ✓.

---

## Recommended new translator-decisions docs

1. **`day_of_the_lord_leitwort_2026-06.md`** (§5) — the `יוֹם יְהוָה` → `วันแห่งองค์พระผู้เป็นเจ้า` lock, now covering both **Joel** (institution) and **Amos** (reversal). Already recommended at the Joel audit; Amos makes it doubly owed. Write once, before Obadiah/Zephaniah/Malachi.
2. **`graded_numerical_x_x_plus_one_2026-06.md`** (§3) — the `שְׁלֹשָׁה … אַרְבָּעָה` "for three… and for four" formula → `สามครั้ง หรือสี่ครั้ง`, with forward-protection for Prov 30 / Job 5 / Mic 5.
3. **`adonai_yhwh_2026-06.md`** (§1) — **only if Ben chooses path (b)** (ratify the marking convention). If Ben chooses path (a) (normalize to bare), the phantom citation is struck instead and no doc is written. This doc must not be authored until that DECIDE is resolved.

(Docs 1–2 are STABLE-confirm doc-lifts; per the checklist, this audit recommends but does not author them. Doc 3 is contingent on the §1 DECIDE.)

## Checklist for Ben before tagging `book-amos-v1`

- [ ] **§1 DECIDE (BLOCKER)** — resolve the `אֲדֹנָי יְהוִה` compound surfacing: **(a)** normalize Amos's 19 plain `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` → bare `องค์พระผู้เป็นเจ้า` (conform to the locked corpus rule — **recommended**), or **(b)** ratify a deliberate Amos marking convention + write `adonai_yhwh_2026-06.md` + reconcile the Jeremiah OAN-split. Either way, resolve the phantom `adonai_yhwh_2026-05` citation.
- [ ] **§2 DECIDE** — ratify "MT-primary, LXX/Acts-in-footnote" for 9:11–12 (booth of David); confirm the `พลับพลา` rendering of `סֻכָּה`.
- [ ] §7 REVIEW — confirm the 5:25–27 → Acts 7 MT/LXX policy; decide whether Sakkuth→Moloch / Damascus→Babylon warrants a Tier-2 footer.
- [ ] §9 REVIEW — confirm the present-tense reading of 7:14 ("I am not a prophet").
- [ ] §10 REVIEW — confirm `יְהוָה אֱלֹהֵי צְבָאוֹת` → `องค์พระผู้เป็นเจ้าพระเจ้าจอมโยธา` (resolve with §1).
- [ ] §11 REVIEW — register `AMO` in `export_to_usfm.py` (infra; non-blocking).
- [ ] §3 / §5 — approve (or decline) the two recommended translator-decisions docs.
- [ ] Then: `bash scripts/ship_book.sh AMO` (lock-the-book ship + tag).
