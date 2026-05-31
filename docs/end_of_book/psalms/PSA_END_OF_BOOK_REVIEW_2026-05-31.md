# Psalms — End-of-Book Review

**Date:** 2026-05-31
**Scope:** All 150 chapters of Psalms (`output/translations/psalms_01.json` … `psalms_150.json`; 1–9 zero-padded, 10–150 unpadded); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** PSA 150 shipped (commit `eaf05e26`); per `docs/END_OF_BOOK_CHECKLIST.md` §2 + §3, fired by `scripts/detect_book_complete.py` (wrote `output/.book_complete_audit_prompt.md`).
**Mandate:** Internal editorial review (§2 of checklist). Surface only — **no translation changes made.**

## Summary

- **15 cross-cutting items reviewed.** Mechanical gates (§1): 150/150 chapters have green per-chapter 7-check reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `audit_inclusion_variants.py --book PSA --strict` exits 0 (**0 candidates** — the inclusion-variant gate is SBLGNT/NT-scoped; the Psalter's MT-vs-LXX/Qumran inclusion questions are handled as Tier-2 footnotes, see item 13). `check_phrase_consistency.py` reports **8 violations, all in Psalms**, on the Exod 34:6 compassion-formula — see item 11 (the one concrete pre-tag fix). `export_to_usfm.py` / `check_key_term_consistency.py --book PSA` are NT-book-code-scoped and do not yet know OT codes (tooling gap, not a corpus defect). `git status output/` clean except regenerated aggregate report files (`divine_names.md`, `phrase_consistency.md` — not Psalms source; left out of this branch).
- **8 items LOCKED** — compliant with an existing `translator_decisions/` doc (the divine-name family; the Rachasap honorific-binding rule; superscription versification; Selah/transliteration conventions; register).
- **4 items STABLE-but-undocumented** at corpus level (Hallelujah-frame transliteration; acrostic-marker mechanism; imprecatory-psalm footnote approach; NT-citation footnote pattern) — verse-level rationale sound; doc-lift recommended for the two that compound forward (imprecatory approach; Hallelujah frame).
- **2 items REVIEW** (defensible-but-worth-Ben's-confirmation).
- **1 item DECIDE** (item 11 — the רַחוּם lexeme split; blocks a clean `check_phrase_consistency` before tagging `book-psalms-v1`).
- **External AI review (§3) packet prepared** from the REVIEW/DECIDE items (see `external_review_items_PSA.md`).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging `book-psalms-v1`.

---

## 1. Divine-name family (YHWH / YAH / Adonai / Shaddai / Elyon / Tsevaot / El-Elohim) — **LOCKED** (`divine_names_table_2026-05.md`)

The Psalter is the most divine-name-dense book in the corpus, and every form resolves through the locked table with a per-verse Layer-1 `key_decisions` record:

| Hebrew | Rendering | Notes / loci |
|---|---|---|
| `יהוה` (Tetragrammaton) | องค์พระผู้เป็นเจ้า | the dominant form; per-chapter first-occurrence Tier-2 footnote present in every YHWH-bearing chapter |
| `יָהּ` (YAH, short form) | องค์พระผู้เป็นเจ้า | standalone (e.g. 68:5, 77:12, 94:7, 102:19, 115:17, 146:1, 150:6) **and** inside the `הַלְלוּ־יָהּ` frame (→ ฮาเลลูยาห์, item 5) |
| `אֲדֹנָי` (Adonai) | องค์เจ้านาย | lament/petition address; vocative ข้าแต่องค์เจ้านาย |
| `אֲדֹנֵינוּ` ("our Lord") | องค์เจ้านายของเรา | 8:1/9, 135:5, 147:5 |
| `יְהוִה אֲדֹנָי` / `אֲדֹנָי יְהוִה` combo | องค์พระผู้เป็นเจ้า + องค์เจ้านาย | 140:8, 141:8 — **both** the standalone-`יהוה` Layer-1 KD **and** the Adonai KD recorded per gotcha "combined-form ≠ standalone" |
| `שַׁדַּי` (Shaddai) | องค์ผู้ทรงมหิทธิฤทธิ์ | rare in Psalms — genuinely only **68:15** and **91:1** (the other `שדי` hits — 8:8, 50:11, 96:12, 104:11 etc. — are `שָׂדֶה` "field", not the divine name) |
| `עֶלְיוֹן` (Elyon) | องค์ผู้สูงสุด | frequent (e.g. 7, 9, 46, 47, 91) |
| `צְבָאוֹת` (Tsevaot) | จอมโยธา | 11 chapters (24, 44, 46, 48, 59, 60, 68, 69, 80, 84, 89); `יְהוָה צְבָאוֹת` → standalone-YK **plus** the จอมโยธา KD |
| `אֵל` / `אֱלֹהִים` | พระเจ้า | the generic word; vocative ข้าแต่พระเจ้า |
| `אֲבִיר יַעֲקֹב` (Mighty One of Jacob) | องค์ผู้ทรงอานุภาพแห่งยาโคบ | 132:2, 132:5 |

All conform. The `key_decisions` Layer-1 records and per-chapter first-occurrence footnotes are uniform across all 150 chapters. **LOCKED.**

## 2. The messianic crux at Psalm 110 — **STABLE** (handled with care)

110:1 `נְאֻם יְהוָה לַאדֹנִי` — YHWH (→ องค์พระผู้เป็นเจ้า) speaks **to** `אֲדֹנִי` "my Lord" (the Davidic/messianic king, rendered องค์เจ้านายของข้าพเจ้า), **not** the divine `אֲדֹנָי`; v5 `אֲדֹנָי` **is** the divine title. The distinction (human-addressed lord at v1 vs. divine Adonai at v5) is preserved and footnoted with the Matt 22:44 / Heb 1:13 citations. This is the single highest-stakes divine-name discrimination in the Psalter and it is correct. **STABLE — exemplary; no action.**

## 3. Rachasap honorific-binding (the ทรง + พระ-body-part rule) — **LOCKED** (`ot_register_policy_2026-05.md` §1.2/§1.4; `check_honorifics_binding.py`)

Every chapter passed `check_honorifics_binding` with 0 hard fails. The Psalter stress-tested this rule harder than any prior book (God's hand/arm/eyes/face/ear are everywhere). The operative discipline, applied corpus-wide:
- God's-own body-part as **object** of a ทรง-verb is safe (ทรงเหยียดพระหัตถ์); as **subject**, the verb stays plain (พระหัตถ์ขวาของพระองค์ช่วย…, not …ทรงช่วย).
- Perception verbs render as verbs (ทรงมองดู / ทรงสดับ), not body-part nouns (avoid ทอดพระเนตร / เงี่ยพระกรรณ when a ทรง follows).
- Idiom traps avoided: พอพระทัย / น้ำพระทัย / เข้าพระทัย (embed พระทัย) → ทรงโปรดปราน / ทรงประสงค์ / ทรงหยั่งรู้; พระกรุณา (embeds พระกร) → พระเมตตา.
- **Refinement discovered this run (Ps 144:7, fixed pre-ship):** even when a divine body-part is the *object* of a preceding ทรง-verb, a *following* ทรง-petition within ~60 chars still binds to it — so the next verb needs โปรด + plain form (proactively applied at Ps 145:16). Worth a one-line addendum to the policy doc's §1.4 examples.

**LOCKED** (recommend the §1.4 example addendum noted above).

## 4. Register: ข้าพระองค์ / ข้าพเจ้า / เรา / God's-speech เรา — **LOCKED** (`ot_register_policy §2`)

Uniform across 150 chapters: lament/petition-before-God first person → **ข้าพระองค์**; declarative/testimony → **ข้าพเจ้า**; communal → **เรา / ข้าพระองค์ทั้งหลาย**; God's own quoted speech → **เรา** with **plain** verbs (God does not self-honorific — e.g. the covenant oath Ps 132:11–12, the Zion-election speech 132:14–18, 50:7ff, 81:6ff, 91:14–16, 95:8–11). Human kings (Pharaoh in 105/135/136; the Davidic king in 72, 144) rendered **non-royally** (ของตน / ท่าน), reserving ทรง/พระองค์ for God. **LOCKED.**

## 5. The Hallelujah frame `הַלְלוּ־יָהּ` → ฮาเลลูยาห์ — **STABLE** (recommend doc-lift)

The frozen liturgical frame transliterates to **ฮาเลลูยาห์** at the open/close of the Hallel psalms (104:35, 105:45, 106:1/48, 111:1, 112:1, 113:1/9, 115:18, 116:19, 117:2, 135:1/21, 146:1/10, 147:1/20, 148:1/14, 149:1/9, 150:1/6), with a `הַלְלוּ־יָהּ` Layer-1 KD on each framing verse; mid-clause `הַלְלוּ יָהּ` ("praise YAH", e.g. 135:3) translates as the imperative จงสรรเสริญองค์พระผู้เป็นเจ้า. Distinct from the `הַלְלוּהוּ` ("praise Him", pronoun-object) imperatives in Ps 148/150 which carry **no** divine-name KD. Principled and uniform, but the ฮาเลลูยาห์-vs-translate decision lives only at verse level. **STABLE — recommend `docs/translator_decisions/hallelujah_frame_2026-05.md`** (compounds forward: the only other הַלְלוּ־יָהּ outside Psalms is rare, but the transliteration precedent matters for any liturgical reprint).

## 6. Superscription versification (offset psalms) — **LOCKED** (`verse_schema_and_versification_2026-05.md`; `data/versification_map.json`)

62 chapters carry top-level `versification` sub-objects where the MT counts the superscription as v1 (MT vN = English/BSB v(N-1)); `bsb_english` hand-realigned per MT verse; the superscription split from BSB's merged v1 at the content keyword. Short superscriptions integrated into v1 (e.g. "Of David", "A Psalm of Asaph") are MT=BSB aligned with no sub-objects. Back-translations keyed MT-numbered to match the realigned `bsb_english` (lesson locked after the Ps 108 mis-numbering). **LOCKED — see item 12 for the one known map gap (Ps 13).**

## 7. Selah / Maskil / Higgaion / Song-of-Ascents transliteration — **STABLE**

`סֶלָה` → **เซลาห์**, `מַשְׂכִּיל` → **มัสคิล**, `הִגָּיוֹן` → **ฮิกกาโยน**, `שִׁיר הַמַּעֲלוֹת` → **บทเพลงใช้แห่ขึ้น**, `מִכְתָּם` → มิคทาม. Uniform across all occurrences. The Songs of Ascents (120–134, the full 15) carry the consistent superscription rendering. **STABLE** (transliteration conventions; could fold into a single `psalm_genre_terms` note but low forward-compounding risk).

## 8. Acrostic-marker mechanism — **STABLE** (`ot_register_policy §5`)

Optional `acrostic_marker {letter, phonetic_thai, stanza_position}` on stanza-initial verses in the 9 acrostic chapters (9, 10, 25, 34, 37, 111, 112, 119, 145). The Thai poetry inside does **not** attempt Thai-alphabet equivalence (correct — Hebrew-form transparency only). Ps 119's 22-stanza structure and Ps 145's missing-נun (item 13) both handled. **STABLE.**

## 9. Imprecatory-psalm footnote approach — **STABLE** (recommend doc-lift — forward-compounding)

The Psalter's imprecatory passages (137:8–9, 139:19–22, 140:9–11, 149:6–9, plus 5, 35, 58, 69, 109 earlier) all carry a Tier-2 pastoral footnote with a consistent four-part frame: (1) faithful unsoftened rendering from the MT; (2) vengeance entrusted to God, not self-executed (Deut 32:35 / Rom 12:19); (3) lex talionis / God's righteous judgment; (4) the NT trajectory (Christ's love-of-enemies Matt 5:44; spiritual-warfare reading Eph 6:17 / Heb 4:12 / Rev 19:15). This is a genuine cross-cutting **editorial** stance, currently expressed only verse-by-verse. **STABLE — recommend `docs/translator_decisions/imprecatory_psalms_2026-05.md`** to lock the four-part frame as the corpus approach (it is the most pastorally sensitive recurring decision in the book and reviewers will ask about it).

## 10. NT-citation footnote pattern — **STABLE**

Rich Tier-2 cross-reference footnotes where the NT cites/alludes (110→Matt 22/Heb 1; 118 cornerstone→Matt 21:42 + Hosanna→Matt 21:9; 132:11→Acts 2:30; 132:17/148:14→Luke 1:69; 102:26→Heb 1:10–12; 109:8→Acts 1:20; 8/144:3→Heb 2:6; 145:8→Exod 34:6; 146:7–9→Luke 4:18; 143:2→Rom 3:20). Uniform tone and tier. **STABLE.**

## 11. Exod 34:6 compassion-formula `חַנּוּן וְרַחוּם` — **DECIDE** (one pre-tag fix clears `check_phrase_consistency`)

`check_phrase_consistency.py` flags 8 violations, all on this formula across Ps 86:5, 86:15, 103:8, 111:4, 112:4, 145:8. Disentangling them:
- **רַחוּם lexeme drift (the real fix):** רַחוּם renders **พระเมตตา** at 86:15, 103:8, 111:4, but **ความเมตตากรุณา** at **145:8** (the outlier — chosen to sidestep the พระกรุณา/พระกร trap, but พระเมตตา is itself trap-free and is the established form). **Recommend normalizing 145:8 רַחוּם → พระเมตตา** ("ทรงเปี่ยมด้วยพระคุณและพระเมตตา ทรงกริ้วช้า…"). One-word edit; re-ship PSA 145 via `ship_chapter.sh`; clears the lexeme inconsistency.
- **Word-order variation is legitimate** and tracks the MT: רַחוּם וְחַנּוּן (compassion-first) at 86:15/103:8 vs. חַנּוּן וְרַחוּם (grace-first) at 111:4/145:8/112:4. Preserve.
- **Ps 86:5 is a different formula** (טוֹב וְסַלָּח "good and forgiving", → ทรงดีและทรงพร้อมที่จะอภัย) — the phrase lock is over-matching; recommend tightening the lock pattern or documenting an exception.
- **Ps 112:4 is the righteous *man*** mirroring God's character (חַנּוּן וְרַחוּם וְצַדִּיק) — plain ความเมตตา (no พระ-) is correct there.

**DECIDE before `book-psalms-v1`:** approve the 145:8 normalization + decide whether to tighten the phrase-lock (exclude 86:5's סַלָּח) or add a documented exception.

## 12. Ps 13 versification-map content-shift gap — **REVIEW** (maintainer/tooling)

`build_psalm_entries` detects superscription offset by MT-vs-BSB verse *count*; Ps 13 has a superscription (+1 to MT) **and** English splitting 13:5–6, re-equalizing the count (MT 6 = Eng 6), so the map emits **no** entries though the content is shifted (MT v1=superscription; MT v6 = Eng 13:5–6 combined). Handled at translation time (hand-aligned `bsb_english`, `versification_verse_split` footnote, no spurious sub-objects), but the **generator should also detect content-shift, not just count-mismatch** (affects Ps 13 + any similar). Already flagged to Ben; logged here for the book record. **REVIEW (tooling).**

## 13. MT-vs-LXX/Qumran inclusion + difficult-text handling — **STABLE**

The Psalter's analog to the NT inclusion-variant gate is handled as Tier-2 text-critical footnotes, uniformly: **Ps 145:13 missing-נun verse** (absent in MT, supplied in 11QPsaᵃ Dead Sea Scrolls Hebrew + LXX + Syriac; the נun line quoted in the footnote; MT base retained, `bsb_english` truncated to the מ-line to match); **Ps 147** LXX/Vulgate two-psalm split noted; genuinely difficult Hebrew (Ps 138:2 name/word clause; 141:5–7) footnoted as such with the reading rationale. Consistent and transparent. **STABLE.**

## 14. Torah-synonym glossary (Ps 119) — **STABLE/LOCKED-adjacent**

The eight Torah synonyms locked in `psalter-translation-gotchas` and seeded at Ps 19:8 applied uniformly across Ps 119's 176 verses: תּוֹרָה=ธรรมบัญญัติ, עֵדוֹת=พระโอวาท, פִּקּוּדִים=ข้อบังคับ, מִצְוֹת=พระบัญญัติ, חֻקִּים=กฎเกณฑ์, מִשְׁפָּטִים=ข้อตัดสิน, דָּבָר=พระวจนะ, אִמְרָה=พระดำรัส. Recurs in 147:19 (กฎเกณฑ์/ข้อตัดสิน). **STABLE** — captured in the gotchas memory; could lift to a `torah_synonyms_2026-05.md` translator-decision doc if any future psalm/Torah-book needs the lock.

## 15. Divine-anthropomorphism preservation — **STABLE** (strength)

God's body-part imagery is preserved, not paraphrased away, per the standing guidance: "mighty hand and outstretched arm" (136:12 พระหัตถ์/พระกร), "the eyes of the LORD" (33:18, 34:16), "You open Your hand" (145:16), "Your right hand" (e.g. 138:7), "the light of Your face" — all rendered with the royal body-part where the Hebrew has the noun, while satisfying the Rachasap binding rule (item 3). The anthropomorphism is theological imagery the author intends; preserving it is correct. **STABLE — strength.**

---

## Recommended new translator-decisions docs (if Ben approves the doc-lifts)

- `docs/translator_decisions/imprecatory_psalms_2026-05.md` (item 9 — the four-part pastoral footnote frame)
- `docs/translator_decisions/hallelujah_frame_2026-05.md` (item 5 — ฮาเลลูยาห์ transliteration vs. translate)
- (optional) `torah_synonyms_2026-05.md` (item 14); §1.4 example addendum to `ot_register_policy` (item 3 refinement)

## DECIDE items blocking `book-psalms-v1`

- **Item 11** — approve the Ps 145:8 רַחוּם → พระเมตตา normalization + phrase-lock tightening for the Exod 34:6 formula. This is the only item that blocks a clean `check_phrase_consistency` run.

All other items are LOCKED/STABLE/REVIEW and do not block the tag.
