# Spiritual-beings hierarchy — corpus-consistent Pauline cosmology terms

**Decision date:** 2026-05-02 (formalized after COL end-of-book external AI review)
**Anchor passages:** Colossians 1:16, 2:10, 2:15; Ephesians 1:21
**Forward applicability:** Eph 3:10, 6:12; 1 Pet 3:22; Rom 8:38–39; Titus 3:1
**Status:** LOCK. Two verses revised in this PR (COL 1:16 + EPH 1:21) to fix a เทพ-collision and an ἀρχαί inconsistency.

## The problem caught by the audit

COL 1:16 originally read:

> ไม่ว่าจะเป็น**บัลลังก์**หรือ**เทพผู้ครอง** หรือ**ทูตสวรรค์ผู้มีอำนาจ**หรือ**ผู้ทรงสิทธิ**

Two issues, both flagged independently by all three external AI reviewers:

1. **`เทพผู้ครอง` for κυριότητες** collides with the locked `pagan_deities_2026-04.md` rule. The เทพ / เทพี / เทพเจ้า register is reserved for **pagan deities** (Zeus, Artemis, Athena, etc.). Christ's CREATURES — even at the highest spiritual-power tier — must not be rendered with deity-class register. Doing so would lexically undercut Paul's central polemical move in 1:16 ("by him all things were created … whether thrones or dominions or rulers or authorities — all things were created through him and for him").

2. **`ทูตสวρρค์ผู้มีอำนาจ` for ἀρχαί at 1:16** but **`ผู้ครอง`** at 2:10 and 2:15 — undocumented inconsistency for the same Greek lemma within the same chapter block. Forward-compounding into Eph 1:21 (now revised), Eph 6:12, 1 Pet 3:22, Rom 8:38–39.

## Locked corpus mapping

| Greek | Thai | Sense | Locking precedent |
|---|---|---|---|
| **θρόνοι / θρόνος** | บัลลังก์ | thrones (highest cosmological tier; rare) | COL 1:16 |
| **κυριότητες / κυριότης** | **ผู้ทรงเดชานุภาพ** | dominions / lordships (royal register; not เทพ) | COL 1:16; EPH 1:21 |
| **ἀρχαί / ἀρχή** | **ผู้ครอง** | rulers (cosmological power, not human-political) | COL 2:10, 2:15; EPH 1:21 |
| **ἐξουσίαι / ἐξουσία** (cosmic-power sense) | **ผู้ทρρอำนาจ** | authorities | COL 1:16, 2:10, 2:15; EPH 1:21 |
| **δυνάμεις / δύναμις** (cosmic-power sense) | ผู้ทρρสิทธิ | powers | EPH 1:21 |

Note: ἐξουσία in human-political contexts (Rom 13:1–7, Titus 3:1 first occurrence, etc.) renders differently per ordinary-civic-rendering rules — see verse-level KDs there. The cosmic-power register is the lock here.

## Why ผู้ทรงเดชานุภาพ for κυριότητες

Three candidates considered (Claude's suggestion list):

1. **ผู้ทρρเดชานุภาพ** ("those who possess sovereign power") — chosen.
2. อำนาจครอบครอง — works but reads as abstract noun, not personal-class beings.
3. ผู้มีฐานะเป็นเจ้านาย — accurate but verbose; the "lord-status" framing is more lexical-explanation than translation.

ผู้ทρρเดชานุภาพ:
- Uses **ทρρ-** royal verbal prefix (consistent with cosmological-tier register without crossing into deity-class).
- เดชานุภาพ ("majestic-sovereign-power") is a Pali-Sanskrit-rooted compound common in Thai religious-historical register; reads as elevated authority, not as a deity.
- Distinct from ผู้ทρρอำนาจ (ἐξουσίαι, "authorities") and ผู้ทρρสิทธิ (δυνάμεις, "powers") — the three terms remain lexically separable.

## Verses revised this PR

**COL 1:16:**
- κυριότητες: เทพผู้ครอง → **ผู้ทρρเดชานุภาพ**
- ἀρχαί: ทูตสวρρค์ผู้มีอำนาจ → **ผู้ครอง**
- ἐξουσίαι: ผู้ทρρสิทธิ → **ผู้ทρρอำนาจ**

**EPH 1:21:**
- κυριότητος: เทพผู้ครอง → **ผู้ทρρเดชานุภาพ**

(EPH 1:21 was shipped earlier today on this branch with the same problematic rendering — caught and fixed before broader Ephesians ships.)

## Forward applicability

When these verses ship, validate against this doc's lock:

- **Eph 3:10:** ταῖς ἀρχαῖς καὶ ταῖς ἐξουσίαις ἐν τοῖς ἐπουρανίοις → ผู้ครองและผู้ทρρอำนาจ
- **Eph 6:12:** πρὸς τὰς ἀρχάς, πρὸς τὰς ἐξουσίας, πρὸς τοὺς κοσμοκράτορας τοῦ σκότους τούτου, πρὸς τὰ πνευματικὰ τῆς πονηρίας → 4-tier; the κοσμοκράτωρ is its own NT-HAPAX needing separate treatment, not in this lock
- **1 Pet 3:22:** ἀγγέλων καὶ ἐξουσιῶν καὶ δυνάμεων → ทูตสวρρค์ + ผู้ทρρอำนาจ + ผู้ทρρสิทธิ
- **Rom 8:38–39:** οὔτε ἄγγελοι οὔτε ἀρχαί … οὔτε δυνάμεις → ทูตสวρρค์ + ผู้ครอง + ผู้ทρρสิทธิ
- **Titus 3:1:** ἀρχαῖς ἐξουσίαις (here civic, not cosmic) — different rendering; document at the verse-level KD

## OT extension: Gen 6:1–4 בְּנֵי הָאֱלֹהִים (sons-of-God) anchor (added 2026-05-12)

Added per Genesis end-of-book audit §D + external AI review (ChatGPT + Gemini both CONCERN — both recommend surface-text preservation + Layer-2 interpretive-crux footer).

**The Hebrew phrase** בְּנֵי הָאֱלֹהִים *bĕnê hāʾĕlōhîm* ("sons of God") appears in Gen 6:1–4 and again in Job 1:6, 2:1, 38:7 in the same morphological form. The Eremos OT-side rendering preserves the literal phrase **บุตรของพระเจ้า** ("sons of God") at all four occurrences.

**Three competing interpretations:**

1. **Sethite-line** (Augustine + Reformed mainstream): godly Sethite line marrying Cainite women
2. **Royal/aristocratic** (rabbinic minority): rulers/nobles marrying commoners
3. **Angelic / divine-council** (1 Enoch + 2 Pet 2:4 + Jude 6 + most pre-Augustinian church): heavenly-council members crossing the boundary with humans — the Job 1:6 / 2:1 / 38:7 parallels use the **identical phrase** unambiguously for divine-council members

**Surface-text policy:** preserve the literal phrase **บุตรของพระเจ้า** to retain Hebrew polysemy. Do NOT inline-paraphrase to "เชื้อสายของเซธ" (Sethite reading) or "ทูตสวรรค์" (angelic reading) — both would foreclose the question. The Job parallels (rendered the same way) carry the structural-recognition load that the Hebrew makes possible.

**Layer-2 interpretive-crux footnote** required at Gen 6:2 + 6:4 (added 2026-05-12 to `output/textual_variants/genesis_06.json`) — names the three readings + the Job 1:6 / 2:1 / 38:7 + Ps 29:1 + 89:6 parallels + the 2 Pet 2:4 / Jude 6 NT trajectory.

**Nephilim** (נְפִילִים) at Gen 6:4 transliterated as **เนฟิลิม** + Num 13:33 cross-reference (the only other OT occurrence; LXX γίγαντες).

**Forward applicability:**

- **Job 1:6, 2:1, 38:7** — same phrase, same rendering บุตรของพระเจ้า; the Job context makes the divine-council reading harder to escape, providing a natural cross-reference for readers wrestling with the Gen 6 question
- **Ps 29:1, 89:6** — בְּנֵי אֵלִים ("sons of gods/mighty ones") — related phrase; render with similar literal-preservation + interpretive-crux footer; do NOT collapse to "ทูตสวรรค์" or to "เทพ-class" (would collide with `pagan_deities_2026-04.md`)
- **Dan 3:25** ("the appearance of a son of the gods") — separate construction (Aramaic בַּר־אֱלָהִין); document at verse-level KD

## Cross-references

- Verse-level KDs: COL 1:16 (revised, with note); EPH 1:21 (revised, with note); COL 2:10, 2:15 (unchanged, corpus-consistent).
- Companion / blocked-by doc: `pagan_deities_2026-04.md` — the locked เทพ-class register is what this doc avoids colliding with.
- Audit: `docs/end_of_book/colossians/COL_END_OF_BOOK_REVIEW_2026-05-02.md` Item F; `docs/end_of_book/genesis/GEN_END_OF_BOOK_REVIEW_2026-05-11.md` §D.
- AI review: `docs/end_of_book/colossians/ai_review_response_COL_2026-05-02.md` Item F; Genesis external AI review (ChatGPT + Gemini, 2026-05-12).

## Change log

- **v0.2** (2026-05-12) — added OT extension: Gen 6:1–4 + Job 1:6/2:1/38:7 בְּנֵי הָאֱלֹהִים anchor with surface-text policy + Layer-2 interpretive-crux footer requirement.
- **v0.1** (2026-05-02) — initial NT Pauline-cosmology lock (COL 1:16, 2:10, 2:15; EPH 1:21).
