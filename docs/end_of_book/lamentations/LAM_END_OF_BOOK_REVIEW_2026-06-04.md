# Lamentations — End-of-Book Review

**Date:** 2026-06-04
**Scope:** All 5 chapters of Lamentations (`output/translations/lamentations_01.json` … `lamentations_05.json`; 154 verses); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** LAM 5 shipped (commit `2c5ac67d`); per `docs/END_OF_BOOK_CHECKLIST.md` §2 + §3, fired by `scripts/detect_book_complete.py`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — **no translation changes made**.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 5/5 chapters have green per-chapter reports ("All checks passed") + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (38 locks, 0 violations across 25,959 verses — incl. the chesed and Exod-34 locks that the 3:22–23 cluster stress-tests); `audit_inclusion_variants.py --book lamentations --strict` exits 0 (**0 candidates** — LAM is MT poetry, no SBLGNT/LXX inclusion variants); `git status output/` clean.
- **10 items LOCKED** — compliant with an existing `translator_decisions/` doc (YHWH + Layer-1/Layer-2 architecture; bare-Adonai 4-way; chesed; goel; paqad; mashiach-YHWH; Elyon; divine anthropomorphism / rachasap body-part rule; hevel-contextual scope; inclusion-variants below the §2.3 floor).
- **4 items STABLE-but-undocumented** at corpus level (the אֵיכָה lament-opener `โอ้…เสียแล้ว`; the "no comforter" `אֵין מְנַחֵם` refrain; the city-as-woman epithet set; the deliberate divine↔enemy בלע "swallow" echo) — all are book-internal leitwort behavior already governed by `leitwort_handling_policy_2026-05.md`; verse-level rationale is sound. One optional doc recommended (אֵיכָה opener) for the Isaiah/Jeremiah-forward thread.
- **2 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): the Layer-2 bare-Adonai footnote is present only once in the book (ch.1) while ch.2/ch.3 use bare Adonai heavily with no in-chapter note; and the acrostic device is invisible in Thai with no reader-edition pointer.
- **1 item flagged DECIDE** (the **5:22 כִּי אִם book-ending crux** — the "unless you have utterly rejected us" reading sets the closing theology of the whole book; the choice + the synagogue v.21-reprise convention should be confirmed before the v1 tag).
- **External AI review (§3) packet prepared** from the REVIEW/DECIDE items (see `external_review_items_LAM.md`).

LAM is the cleanest mechanical state of any OT book in the pilot to date: it introduces **no new corpus-level lemma** requiring a fresh decision doc — it almost entirely *exercises* locks already established for Psalms/Proverbs/Ecclesiastes/Song. The audit is correspondingly light on doc-lift recommendations.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging `book-lamentations-v1`.

---

## 1. YHWH → องค์พระผู้เป็นเจ้า + Layer-1 `key_decisions` + Layer-2 first-occurrence footnotes — **LOCKED** (`divine_names_table_2026-05.md`)

After Ecclesiastes + Song of Songs (the two OT books with **no** Tetragrammaton), LAM brings the divine-name machinery back online, and it is handled with care. Every `יהוה` occurrence renders **องค์พระผู้เป็นเจ้า** with a Layer-1 `key_decisions` Hebrew-form record, and each chapter that contains YHWH carries a Layer-2 Tier-2 first-occurrence footnote in `output/textual_variants/lamentations_NN.json`:

| Chapter | YHWH verses | Layer-2 footnote (first occurrence) |
|---|---|---|
| 1 | 1:5, 9, 11, 12, 17, 18, 20 | v.5 ✓ |
| 2 | 2:6, 7, 8, 9, 17, 20, 22 | v.6 ✓ |
| 3 | 3:18, 22, 24, 25, 26, 40, 50, 55, 59, 61, 64, 66 | v.18 ✓ |
| 4 | 4:11, 16, 20 | v.11 ✓ |
| 5 | 5:1, 19, 21 | v.1 ✓ |

Vocative direct address (city/community to YHWH) uses the locked **ข้าแต่องค์พระผู้เป็นเจ้า** form (1:20; 2:20; 3:55, 59, 61, 64; 5:1, 19, 21). The check `[E]`/`[D]` gates (Layer-1 kd + Layer-2 footnote) pass on all five chapters. **LOCKED.** (See §16 for a footnote-*completeness* sub-flag concerning the bare-Adonai note.)

---

## 2. Bare Adonai אֲדֹנָי → องค์เจ้านาย / ข้าแต่องค์เจ้านาย — **LOCKED** (`divine_names_table_2026-05.md` 4-way sub-rule; LAM is named in the forward-protection list)

LAM uses standalone אֲדֹנָי (no YHWH compound) more densely than almost any OT book, and the 2026-05-18 four-way Adonai distinction — whose forward-protection section **explicitly names Lamentations** — governs it. Compliance:

| Hebrew context | Thai | Verses |
|---|---|---|
| Standalone Adonai, third-person reference (narrative/poetic) | **องค์เจ้านาย** | 1:14, 1:15; 2:1, 2:2, 2:5, 2:7, 2:18, 2:19, 2:20; 3:31, 3:36, 3:37 |
| Standalone Adonai, direct prayer-vocative | **ข้าแต่องค์เจ้านาย** | 3:58 |

The third-person uses are uniform and correct. The single vocative (3:58) is treated in §17 below as a minor REVIEW (it is a *bare appositional* vocative, not the interjection-prefaced form the ข้าแต่องค์เจ้านาย anchor was locked on). The lemma-distinction itself — YHWH (`องค์พระผู้เป็นเจ้า`) vs. standalone Adonai (`องค์เจ้านาย`) held apart so the Thai reader can feel the Hebrew register-alternation — is preserved exactly as the doc prescribes. **LOCKED.**

---

## 3. חֶסֶד (chesed) → ความรักมั่นคง — **LOCKED** (`chesed_covenant_love_2026-05.md`)

The theological hinge of the book, 3:22, is the stress-test: `חַסְדֵי יְהוָה` → **ความรักมั่นคงขององค์พระผู้เป็นเจ้า** ✓, and 3:32 `כְּרֹב חֲסָדָיו` → **ตามความรักมั่นคงอันอุดมของพระองค์** ✓. The lemma-thread is intact and matches the corpus form locked from Ruth/Jonah/Psalms.

Critically, the 3:22–23 cluster sits **adjacent to the Exod-34 attribute vocabulary** (chesed + rachamim + emunah), and the translator correctly held the rendering *off* the Exod-34 formula lock: רַחֲמָיו (3:22, plural) → **พระเมตตา** (noun, the distinct sibling lemma), אֱמוּנָתֶךָ (3:23) → **ความซื่อสัตย์** — neither triggers the `exod_34_attribute_formula` phrase lock, and `check_phrase_consistency.py` confirms 0 violations. The 3:22 `key_decisions` documents this explicitly. **LOCKED** — exemplary lemma-discipline at the one verse where drift would have been most costly.

---

## 4. Other inherited lemma locks — **LOCKED**

| Lemma / form | LAM evidence | Doc |
|---|---|---|
| goel "redeem" → **ทรงไถ่** | 3:58 גָּאַלְתָּ חַיָּי → ทรงไถ่ชีวิตของข้าพระองค์ | `goel_kinsman_redeemer_2026-05.md` |
| paqad "visit/punish" → **ทรงลงโทษ** | 4:22 פָּקַד עֲוֺנֵךְ (Edom) → จะทรงลงโทษความผิดบาปของเจ้า | `paqad_visit_attend_2026-05.md` |
| מְשִׁיחַ יְהוָה "the LORD's anointed" → **ผู้ที่องค์พระผู้เป็นเจ้าทรงเจิมไว้** | 4:20 (Zedekiah) | corpus form, 1SA 24:7 precedent (`proper_names_and_transliteration_2026-05.md` / divine-names family) |
| עֶלְיוֹן (Elyon) → **องค์ผู้สูงสุด** | 3:35, 3:38 | `divine_names_table_2026-05.md` |
| cheleq "portion" → **ส่วนแบ่ง** | 3:24 חֶלְקִי יְהוָה → องค์พระผู้เป็นเจ้าทรงเป็นส่วนแบ่งของข้าพเจ้า (the Eccl cheleq lock pays off — the LORD as true portion) | Ecclesiastes corpus lock |
| la'anah "wormwood" → **บอระเพ็ดพิษ** | 3:15, 3:19 | corpus term (Deut/Prov) |

All compliant. **LOCKED.**

---

## 5. Divine anthropomorphism / rachasap body-part rule — **LOCKED** (`hebrew_idioms_and_metaphor_2026-05.md`, `divine_anthropomorphism_thai_grammar_2026-05.md`, `ot_register_policy_2026-05.md`)

LAM ch.2 (the wrath chapter) is the densest divine-body-part text since the Psalter — pre-empted hand/arm/eyes/face/mouth imagery throughout — and the corpus rachasap rule (once any divine body-part token appears in a verse, no ทรง-verb may follow it anywhere in that verse) held through the whole catalog. The playbook is visible and consistently applied:

- **Body-part-as-subject takes a plain verb**: 1:14 พระหัตถ์…ถักร้อย; 2:4 พระหัตถ์ขวา…ตั้งมั่น; 4:16 พระพักตร์…ทำให้กระจัดกระจาย (+ passive follow-up ไม่ได้รับการเหลียวแล).
- **Front-load ทรง-verbs, body-part clause last** (2:4, 2:8 — note ทรงมุ่งหมาย substituted for ทรงตั้งพระทัย, with the literal kept in `thai_literal`).
- **Avoid the body-part in main text where it would poison a following ทรง-verb**: 1:18 פִיהוּ → พระดำรัส; 1:22 / 3:35 לְפָנֶיךָ → เฉพาะพระองค์ (พระพักตร์ kept in `thai_literal`); 3:3 "turn his hand" → main text reworded, literal พลิกพระหัตถ์ in `thai_literal`.
- **Human body-parts of suffering kept literal** per `hebrew_idioms`: 2:11 "my liver is poured out" → ตับ…ถูกเทลงบนดิน; 3:13 "kidneys" → ไต.

`check_phrase_consistency.py` and the per-chapter rachasap checker are green on all five chapters. **LOCKED** — strength.

---

## 6. הֶבֶל (hevel) at 4:17 → เปล่าประโยชน์ (contextual) — **LOCKED** (`leitwort_handling_policy_2026-05.md`; Ecclesiastes hevel scope)

LAM 4:17 `אֶל־עֶזְרָתֵנוּ הָבֶל` ("our help [was] vain") renders **เปล่าประโยชน์** — the general "futile/in-vain" sense — and the `key_decisions` explicitly notes that the Ecclesiastes leitwort rendering (ไร้แก่นสาร / the still-provisional hevel verdict) is **scoped to Qoheleth only** and does not apply here. This is the correct application of the leitwort-policy's "book-scoped leitwort vs. general lexical sense" distinction. **LOCKED.** (Forward note: when the standalone `hevel_leitwort` doc recommended by the Ecclesiastes audit is written, it should record this LAM 4:17 case as the model for non-Qoheleth hevel.)

---

## 7. Inclusion variants / MT–LXX divergence — **LOCKED (below the §2.3 floor)** (`mt_vs_lxx_textual_variant_handling_2026-05.md`, `inclusion_variants_absent_verses_2026-04.md`)

`audit_inclusion_variants.py --book lamentations --strict` → **0 candidates**. LAM is translated from the MT and carries no SBLGNT-omits / mainstream-includes verses; the well-known LXX paratext (the prefatory note ascribing the book to Jeremiah) and the MT/LXX ordering differences are paratextual, not verse-inclusion variants, and sit below the §2.3 textual-variant floor. **No `textual_variants` files are owed beyond the divine-name footnotes already present.** Consistent with every prior OT-book finding (1CH/2CH/2KI etc.: "MT/LXX = non-gap"). **LOCKED.**

---

## 8. אֵיכָה lament-opener → "โอ้ … เสียแล้ว" — **STABLE (undocumented; optional doc — low forward priority)**

The book's title-word and structural signature `אֵיכָה` ("How…!") opens three of the five chapters and is rendered with a uniform fixed frame **"โอ้ … เสียแล้ว"** (1:1, 2:1, 4:1). The choice wraps the Hebrew interjection's lament-force around the clause rather than translating it as a bare "อย่างไร" — principled, and uniform across all three occurrences. Documented only at the verse level (1:1 `key_decisions`).

`אֵיכָה` / `אֵיךְ` as a lament-or-taunt opener recurs outside LAM (Isa 1:21; 14:4, 12; Jer 48:17; Ezek 26:17; the dirge-genre marker), so there is mild forward-compounding. **Recommend (optional):** a short `docs/translator_decisions/ekhah_lament_opener_2026-06.md` locking the "โอ้ … เสียแล้ว" dirge-frame before Isaiah/Jeremiah, where the same interjection will need register-consistent handling. Low priority — STABLE as-is.

---

## 9. "No comforter" refrain אֵין מְנַחֵם → ไม่มีผู้ปลอบโยน — **STABLE** (`leitwort_handling_policy_2026-05.md`)

The ch.1 refrain (1:2, 1:9, 1:16-variant מְנַחֵם מֵשִׁיב נַפְשִׁי, 1:17, 1:21) is rendered uniformly **ไม่มีผู้ปลอบโยน / ผู้ปลอบโยน**, tied to the form already used at Eccl 4:1, preserving the leitwort's five-fold drumbeat. The 1:2 `key_decisions` records the refrain and its corpus tie. Principled and uniform. **STABLE** — governed by the leitwort policy; no separate doc needed.

---

## 10. City-as-woman epithet set — **STABLE** (`proper_names_and_transliteration_2026-05.md`; 2KI 19:21 corpus shape)

The personified-Zion epithets are rendered to a uniform corpus shape: בַּת־צִיּוֹן → **ธิดาแห่งศิโยน** (1:6; 2:1, 4, 8, 10, 13, 18); בְּתוּלַת בַּת־יְהוּדָה → **ธิดาพรหมจารีแห่งยูดาห์** (1:15; 2:13 Virgin Daughter of Zion); בַּת־יְהוּדָה → **ธิดาแห่งยูดาห์** (2:2, 2:5); and the recurring בַּת־עַמִּי → **ธิดาของประชาชนข้าพเจ้า** (2:11; 3:48; 4:3, 6, 10) — all matching the 2KI 19:21 form locked earlier. The personification (city as widow/weeping woman) is carried consistently with feminine address (นาง / เธอ). **STABLE.**

---

## 11. Deliberate divine↔enemy בלע "swallow" echo — **STABLE (strength; verse-level)**

The Hebrew binds God's judgment and the enemy's gloating with a shared verb בלע ("swallow up"): God בִּלַּע at 2:2, 2:5 (ทรงกลืน) and the enemy בִּלָּעְנוּ at 2:16 (พวกเรากลืนนางแล้ว). The translator preserved the same Thai verb **กลืน** across both subjects and flagged the intentional echo in the 2:16 `notes`. This is exactly the leitwort-preservation behavior the policy wants. **STABLE** — no action.

---

## 12. Register split (city/community: ข้าพเจ้า to humans, ข้าพระองค์ to YHWH) — **STABLE** (`ot_register_policy_2026-05.md`)

The first-person voice shifts register by addressee, applied consistently:
- City/poet speaking *to humans / about her plight* → **ข้าพเจ้า** (1:12, 1:16; 3:1–21 the geber; 3:48–54).
- City/poet/community *in direct prayer to YHWH* → **ข้าพระองค์** (1:9c, 1:11c, 1:20–22; 3:42–45 communal พวกข้าพระองค์; 3:55–66 ข้าพระองค์; all of ch.5 communal พวกข้าพระองค์).

The mid-verse switch points (e.g. 1:9, 1:11 where the last colon turns to address God) are flagged in `key_decisions`. ch.5's wholesale communal-prayer register (พวกข้าพระองค์ throughout) is documented at 5:1. Principled and uniform. **STABLE.**

---

## 13. The book's single divine speech (3:57) — **STABLE**

LAM contains exactly one direct divine utterance — 3:57 `אָמַרְתָּ אַל־תִּירָא` → **ตรัสว่า "อย่ากลัวเลย"** — rendered with the royal speech verb ตรัส and the corpus "อย่ากลัวเลย" reassurance form, and flagged in `notes` as the lone divine speech in the book. Correct. **STABLE.**

---

## 14. Acrostic structure (untranslatable) — **STABLE / see REVIEW §18**

Chapters 1, 2, 4 are 22-line alphabetic acrostics; ch.3 is a triple acrostic (66 lines, three per letter); ch.5 has 22 lines (matching the alphabet count) but is **not** acrostic. This architecture — the formal "A-to-Z completeness of grief" that is the book's defining literary feature — cannot survive into Thai, and the translator noted this honestly at the chapter-opening `key_decisions` (1:1, 3:1, 5:1). The handling is correct and transparent; the only open question is reader-facing (see §18). **STABLE** in the translation; **REVIEW** for the reader edition.

---

## 15. 5:21–22 the book ending — **see DECIDE §16-A below**

---

## 16. The bare-Adonai Layer-2 footnote is present only once — **REVIEW**

The bare-Adonai convention footnote (the Layer-2 note that tells a chapter-reader why standalone אֲדֹנָי is rendered **องค์เจ้านาย**, distinct from YHWH) appears **only in ch.1** (`lamentations_01.json`, v.14 note). But:

- **ch.2 opens with bare Adonai at 2:1** (before its first YHWH at 2:6) and uses it at 2:1, 2:2, 2:5, 2:7, 2:18, 2:19, 2:20 — yet `lamentations_02.json`'s textual-variants file carries only the YHWH footnote (v.6), no Adonai note.
- **ch.3 uses bare Adonai at 3:31, 3:36, 3:37, 3:58** — `lamentations_03.json` carries only the YHWH footnote (v.18), no Adonai note.

Compounding this: the LAM YHWH first-occurrence footnotes use a **shortened** form that drops the standard Adonai sentence the `divine_names_table` Layer-2 template prescribes ("…เมื่อข้อความฮีบรูใช้คำว่า אֲדֹנָי … ฉบับเอเรโมสจะแปลว่า 'องค์เจ้านาย'…"). So a reader who opens at ch.2 or ch.3 encounters องค์เจ้านาย with no in-chapter explanation at all.

This is a Layer-2 *completeness* gap, not a rendering error (the Layer-1 `key_decisions` are all present and correct). **Recommend:** either (a) add a per-chapter bare-Adonai note to `lamentations_02.json` (first occ. 2:1) and `lamentations_03.json` (first occ. 3:31), or (b) restore the full divine_names_table Layer-2 footnote text (which folds the Adonai sentence into the YHWH note) for every LAM chapter. Ben to confirm which mechanism. Note: this is moot once the Layer-3 reader-edition front-matter exists, per the doc's own plan — flag accordingly.

---

## 17. 3:58 standalone Adonai vocative without an interjection particle → ข้าแต่องค์เจ้านาย — **REVIEW**

3:58 `רַבְתָּ אֲדֹנָי רִיבֵי נַפְשִׁי` ("You have pleaded, O Lord, the causes of my soul") is a **bare appositional** prayer-vocative — standalone Adonai with no preceding interjection particle. It is rendered **ข้าแต่องค์เจ้านาย**.

The `divine_names_table` 4-way sub-rule (2026-05-18) anchored ข้าแต่องค์เจ้านาย on the *interjection-prefaced* form (בִּי אֲדֹנָי / אֲהָהּ אֲדֹנָי / אָנָּא אֲדֹנָי, JOS 7:8); and the 2026-05-23 sub-rule says **bare appositional** *compound* (אֲדֹנָי יְהוִה) vocatives drop the ข้าแต่ particle. By analogy, a bare appositional *standalone* Adonai vocative arguably should be **องค์เจ้านาย** (no ข้าแต่). The current rendering is defensible (3:58 is unambiguously direct address, and ข้าแต่ reads naturally) but sits in a gap the sub-rules don't explicitly cover. **Recommend:** confirm ข้าแต่องค์เจ้านาย at 3:58, OR drop to bare องค์เจ้านาย for consistency with the 2026-05-23 appositional principle — and add the standalone-bare-appositional case to the divine_names_table so Psalms/Isaiah/Ezekiel inherit it. Minor; Ben to decide.

---

## 18. Acrostic device is invisible in Thai with no reader pointer — **REVIEW**

Per §14, the alphabetic-acrostic architecture (and ch.5's deliberate *non*-acrostic 22-line foil) carries real meaning — completeness-of-grief, the measured containment of lament — that no Thai reader can perceive from the text. The translation notes it at the `key_decisions` level (translator-facing), but there is no reader-facing artifact. Most English editions add a one-line book or chapter note ("This chapter is an acrostic in Hebrew…"). **Recommend:** a single reader-edition / book front-matter line (or a per-chapter footer remark) explaining the acrostic, parallel to how the divine-name convention gets a front-matter note. Ben to decide whether this belongs in the reader edition or a chapter-footer `textual_variants` remark. Low-cost, high reader value.

---

## DECIDE — blocks the `book-lamentations-v1` tag

### A. LAM 5:22 — the כִּי אִם book-ending crux — **DECIDE**

The book ends on Hebrew's single most-debated conjunction. 5:21 pleads `הֲשִׁיבֵנוּ יְהוָה אֵלֶיךָ וְנָשׁוּבָה` ("Restore us… that we may return"); 5:22 then reads `כִּי אִם־מָאֹס מְאַסְתָּנוּ קָצַפְתָּ עָלֵינוּ עַד־מְאֹד`. The current rendering follows the BSB line:

> "เว้นเสียแต่ว่าพระองค์ทรงทอดทิ้งพวกข้าพระองค์อย่างสิ้นเชิงแล้ว และทรงพระพิโรธต่อพวกข้าพระองค์เกินประมาณ"
> ("**unless** You have utterly rejected us, and are angry with us beyond measure.")

The 5:22 `key_decisions` correctly flags the verse as open-ended (readable as "unless / except" *or* "even though") and notes the synagogue convention of re-reading v.21 after v.22 so the book does not close on darkness.

`כִּי אִם` here admits at least three classic construals, and the choice **sets the closing theology of the entire book**:
1. **"unless / except"** (BSB, current) — leaves open the dread possibility of final rejection. Bleakest, most text-literal.
2. **"for even though / although"** (concessive — NRSV-ish "Or have you utterly rejected us?") — softer, reads the rejection as a question/concession.
3. **"but instead / for [if]"** — conditional protasis.

This is exactly the kind of high-visibility, theology-bearing crux a textually-aware Thai reader (comparing THSV/NTV) will land on first. The rendering is defensible and documented, but **Ben should confirm**: (a) endorse the "เว้นเสียแต่ว่า / unless" reading, and (b) decide whether the reader edition should carry a footnote noting the v.21-reprise convention (so the book does not visually end in despair). **DECIDE before tagging.**

---

## Mechanical (§1) — all green

- 5/5 chapters: `output/check_reports/lamentations_NN_review.md` = "All checks passed" + back-translations `output/back_translations/lamentations_NN.json` present.
- `check_key_term_consistency.py`: 0 rule violations, 0 undocumented multi-renderings.
- `check_phrase_consistency.py`: 38 locks, 0 violations across 25,959 verses (chesed + Exod-34 locks clean at the 3:22–23 cluster).
- `audit_inclusion_variants.py --book lamentations --strict`: exit 0, 0 candidates.
- `git status output/`: clean.
- **Tooling note (book-code registration gotcha):** `export_to_usfm.py` still rejects `LAM` ("Unknown book code") — the USFM exporter's slug table lags (per `project_eob_book_code_registration` memory); not blocking for this audit but should be registered before the lock-the-book USFM regen. `audit_items_to_yaml.py`'s `BOOK_SLUGS` was also missing LAM (and PSA/PRO/ECC/SNG) — **fixed on this branch** so output #4 builds. `build_external_review_packet.py` already lists LAM.

---

## Pre-existing docs affirmed / unchanged

- `satan_accuser_corpus_mapping_2026-05.md` — N/A (no שָׂטָן in LAM).
- `exod_34_attribute_formula_2026-05.md` — affirmed by the 3:22–23 cluster *not* triggering it (see §3); the chesed/rachamim/emunah words appear adjacent but not as the formula.
- `ot_warfare_ethics_2026-05.md` / imprecation — the 3:64–66 + 1:21–22 + 4:21–22 imprecatory turns (pay-back to enemies / Edom) use the corpus pattern (ขอทรงตอบแทน / คำสาปแช่ง); no new lock needed.
- `nicham_divine_relenting_2026-05.md` — N/A (the מְנַחֵם "comforter" of §9 is the *human-comfort* root, not divine relenting).

---

## Recommendation

**Lamentations ships in the strongest corpus-hygiene shape of any OT book in the pilot.** It is a "consume the locks" book: the divine-name architecture, chesed, goel, paqad, anthropomorphism, leitwort, and register machinery all held under the stress of the wrath chapters and the 3:22 hinge, with zero mechanical violations and no new lemma requiring a fresh decision doc.

Tag `book-lamentations-v1` after:
1. Ben's decision on **§A (5:22 ending crux)** — the one DECIDE item.
2. Ben's calls on the two REVIEW items: **§16** (per-chapter bare-Adonai footnote completeness in ch.2/ch.3) and **§18** (reader-edition acrostic note); plus the minor **§17** (3:58 vocative particle).
3. (Optional) the `ekhah_lament_opener_2026-06.md` doc (§8) before Isaiah/Jeremiah.
4. Register `LAM` in `export_to_usfm.py` before the lock-the-book USFM regen (§1 tooling note).
5. External AI sanity-check (§3) on the packet built from `external_review_items_LAM.md`.
