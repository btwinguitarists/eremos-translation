# Philemon — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 1 chapter (25 verses; ~80 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (28+ docs).
**Trigger:** PHM 1 shipped (commit `8f3a14f`); per `docs/END_OF_BOOK_CHECKLIST.md`. (PHM is single-chapter; the chapter and the book are coterminous.)
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.
**Note on auto-launch:** PHM 1 shipped 2026-05-02 02:25Z, ~50 minutes BEFORE the auto-audit refactor (PR #76) merged at 03:18Z. This audit is a manual catch-up. Future end-of-book completions auto-launch via `ship_chapter.sh` → `run_end_of_book_audit.sh BOOK --print`.

## Summary

- **4 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 1/1 chapter has green per-chapter report + back-translation; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-178-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book PHM --strict` clean (0 candidates — PHM has no SBLGNT-omits-mainstream-includes variants apart from the closing-Amen at v.25, which is RULES §5b silent-omission per modern critical-text consensus). `git status output/` clean.
- **Philemon is the SHORTEST Pauline epistle** (25 verses, 1 chapter, ~330 Greek words). It is also the **most personal-rhetorical** — a single-recipient appeal letter built on classical *praeteritio* / paralipsis / polite-rhetorical devices rather than dense theological exposition. The translation surfaces these rhetorical devices in `key_decisions` and `thai_summary` rather than in the main `thai` field (which preserves Greek surface where natural in Thai). 7 NT-hapax legomena in 25 verses (Φιλήμων, Ἀπφία, ἄχρηστος, ἑκούσιος, ἀποτίνω, προσοφείλω, ὀνίνημι) — exceptional density driven by the legal-financial register Paul deploys for the IOU passage (vv.18-20).
- **Inherited Pauline corpus locks all verified** in PHM: δοῦλος → ทาส (v.16), δέσμιος → นักโทษ (vv.1, 9), οὖν → เพราะฉะนั้น (vv.8, 17), εὐαγγέλιον → ข่าวประเสริฐ (v.13), κύριος (Christ) → องค์พระผู้เป็นเจ้า, ἁγιοι → ธรรมิกชน (v.5), ἀδελφός → พี่น้อง, συνεργός → เพื่อนร่วมงาน, ἀσπάζομαι → ฝากความระลึกถึง / ทักทาย, εὐχαριστέω + θεός → ขอบพระคุณพระเจ้า. Pauline opening + closing formulae match 2 Cor 1:1-2 / Gal 6:18 precedents exactly.
- **2 items flagged STABLE-but-could-lift-to-corpus-doc**: σπλάγχνα theme-word handling (Pauline emotional-anatomy-metaphor; recurs in 2 Cor, Phil, Col); hapax-density handling in legal-financial Pauline register (precedent for Pastoral Epistles + Hebrews legal language).
- **2 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation): πρεσβύτης lexical at v.9 (minority MS πρεσβευτής "ambassador"); Onesimus name-wordplay surfacing strategy (thai_summary vs explicit Greek footnote).
- **0 items flagged DECIDE** — no item blocks the v1 tag.
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. σπλάγχνα — Pauline emotional-anatomy theme-word — **STABLE (undocumented; recommend brief corpus doc)**

Σπλάγχνα ("inward parts / bowels") is the **single most important theme-word in Philemon** — Paul deliberately repeats it 3× across the 25-verse letter to build the emotional-rhetorical arc:

| Verse | Greek | Thai |
|---|---|---|
| 1:7 | τὰ σπλάγχνα τῶν ἁγίων ἀναπέπαυται διὰ σοῦ | **ใจของธรรมิกชนได้รับการทำให้สดชื่นโดยท่าน** |
| 1:12 | τοῦτ᾽ ἔστιν τὰ ἐμὰ σπλάγχνα | **ผู้นี้คือใจของข้าพเจ้าเอง** |
| 1:20 | ἀνάπαυσόν μου τὰ σπλάγχνα ἐν Χριστῷ | **จงทำให้ใจของข้าพเจ้าสดชื่นในพระคริสต์** |

The 1:7 KD names the principle:

> σπλάγχνα literally = 'inward-parts/bowels' (the seat of emotion in Hellenistic anthropology). Modern Thai 'ใจ' = heart/inner-being is the natural cultural-equivalent. Matches 2 Cor 6:12 σπλάγχνοις → 'ใจ.' This is a key theme-word for Philemon (vv.7, 12, 20).

**Editorial assessment:** **ใจ** is principled — it preserves the seat-of-emotion semantic without the anatomical specificity that would confuse Thai readers (Thai cultural anthropology doesn't locate emotion in the bowels/intestines specifically). The single-rendering policy across all 3 occurrences holds the rhetorical-bookend pattern (v.7 = others' σπλάγχνα Philemon refreshed; v.20 = Paul's σπλάγχνα asking the same favor). The thai_summary at v.7 surfaces the theme-word arc explicitly for Thai readers ("ปรากฏ 3 ครั้ง ข้อ 7, 12, 20"). Verbal cognate ἀναπαύω → ทำให้สดชื่น also pairs across vv.7+20.

**Recurrence forward:** 2 Cor 6:12, 7:15 (already shipped, ใจ rendering); Phil 1:8, 2:1 (forthcoming); Col 3:12 (forthcoming); 1 John 3:17 (forthcoming).

**Recommend: STABLE; OPTIONAL lift to brief corpus doc** `docs/translator_decisions/splanchna_pauline_2026-05.md` if Ben judges the theme-word strategy worth corpus-locking before Phil/Col/1 John ship. Low priority — the existing 2CO precedent + per-verse rationale already covers it. Not a blocker for the v1 tag.

---

## 2. Hapax-density in the legal-financial register (vv.18-20) — **STABLE**

Three NT-hapax legomena cluster in the IOU passage (vv.18-20) where Paul deploys the formal commercial-accounting register:

| Verse | Greek | Thai | Rationale |
|---|---|---|---|
| 1:18 | ἐλλόγα (commercial-accounting; not strictly NT-hapax — also Rom 5:13) | **คิดเป็นบัญชี** | Imperative — formal IOU; preserves accounting-formality |
| 1:19 | ἀποτίσω (NT-hapax) | **จะใช้คืนให้** | Future — legal repayment commitment |
| 1:19 | προσοφείλεις (NT-hapax) | **เป็นหนี้ต่อข้าพเจ้าอยู่เกินไปกว่านั้น** | προσ- intensifier preserved ("over-and-above") |
| 1:20 | ὀναίμην (NT-hapax; optative) | **ขอให้ข้าพเจ้าได้รับประโยชน์** | Optative-wish; ALSO root-pun on Onesimus's name (see Item 4) |

Plus 4 more hapax across the rest of the letter:

| Verse | Greek | Thai | Notes |
|---|---|---|---|
| 1:1 | Φιλήμων (proper noun) | **ฟีเลโมน** | Established Thai Christian transliteration |
| 1:2 | Ἀπφία (proper noun) | **อัปเฟีย** | Established Thai Christian transliteration |
| 1:11 | ἄχρηστος | **ไม่มีประโยชน์** | Set up the v.11 pun on Onesimus (see Item 4) |
| 1:14 | ἑκούσιος | **ความสมัครใจ** | "Voluntary" — paired against ἀνάγκη "compulsion" |

**Editorial assessment:** All 7 hapax are flagged in their verse `notes` per RULES §5. The legal-financial cluster (vv.18-20) is a deliberate Pauline register-shift — matched in Thai by the corresponding accounting/legal vocabulary: บัญชี (account), ใช้คืน (repay), เป็นหนี้ (owe a debt), บังคับ (compulsion), สมัครใจ (voluntary). The register reads cleanly in Thai. The proper-nouns Φιλήμων/Ἀπφία follow Thai Christian Pauline-letter convention.

**Recommend: STABLE**, no corpus doc needed. Hapax-density in PHM 18-20 is unique to this letter's IOU passage; precedent for legal/financial Pauline register going forward (Pastoral Epistles, Hebrews 6:8, Heb 12:11). No action items.

---

## 3. πρεσβύτης (1:9) — **REVIEW** (lexical-variant minority reading)

> διὰ τὴν ἀγάπην μᾶλλον παρακαλῶ, τοιοῦτος ὢν ὡς Παῦλος **πρεσβύτης** νυνὶ δὲ καὶ δέσμιος Χριστοῦ Ἰησοῦ
> ข้าพเจ้าขอวิงวอนโดยอาศัยความรักมากกว่า — ในฐานะที่ข้าพเจ้าคือเปาโล **ผู้สูงอายุ** และบัดนี้ยังเป็นนักโทษของพระเยซูคริสต์ด้วย

**The textual situation.** SBLGNT/NA28/UBS5/WH all print **πρεσβύτης** (old man / aged person). A minority text-tradition + a few patristic citations have **πρεσβευτής** (envoy / ambassador) — the difference is one letter (ευ vs υ). Bentley conjectured πρεσβευτής in the 18th century; Lightfoot adopted it. ESV/NIV/NLT all go with πρεσβύτης ("aged"); NRSV-1989 had "ambassador" but NRSVue-2021 reverted to "old man." BSB has "aged."

**The current rendering: ผู้สูงอายุ (πρεσβύτης = aged-person, lexical default).**

The verse-level note acknowledges the variant:
> TEXTUAL VARIANT (lexical): πρεσβύτης ('old man') vs. πρεσβευτής ('ambassador'). Some early MSS and a few patristic citations have πρεσβευτής. SBLGNT/NA28/UBS5 print πρεσβύτης; the parallelism with δέσμιος (a physical-condition descriptor of Paul's present state) supports this reading. We follow SBLGNT silently — the variant has no manuscript-weight to surface to mainstream Thai readers (THSV/THKJV agree with πρεσβύτης). RULES §5b silent-omission applies.

**Why this is REVIEW rather than STABLE:** The case for πρεσβευτής ("ambassador") is rhetorically attractive — Paul as Christ's ambassador-in-chains rhymes with 2 Cor 5:20, Eph 6:20. But the parallelism with δέσμιος ("now also a prisoner") — both physical-condition descriptors of Paul's present-self — carries the day for πρεσβύτης on internal grounds. SBLGNT critical text + most modern English critical-text Bibles also concur. The current rendering is defensible.

**Question for Ben:** Is the silent-omission disposition (no footer note, no in-thai-field bracket) appropriate for this lexical variant, or do you want a brief verse-level note acknowledging the πρεσβευτής reading for Thai scholarly readers?

---

## 4. Onesimus name-wordplay surfacing — **REVIEW** (form rather than substance)

Greek Ὀνήσιμος = "useful / profitable" (from ὀνίνημι "to derive benefit"). Paul plays on the name THREE TIMES in 25 verses:

| Verse | Greek | Thai | Wordplay |
|---|---|---|---|
| 1:11 | τόν ποτέ σοι **ἄχρηστον** νυνὶ δὲ σοὶ καὶ ἐμοὶ **εὔχρηστον** | ครั้งหนึ่งเคย**ไม่มีประโยชน์**แก่ท่าน แต่บัดนี้กลับ**มีประโยชน์**ทั้งแก่ท่านและแก่ข้าพเจ้า | ἄ-χρηστος / εὔ-χρηστος pun (paronomasia) |
| 1:20 | ἐγώ σου **ὀναίμην** ἐν κυρίῳ | ขอให้ข้าพเจ้า**ได้รับประโยชน์**จากท่านในองค์พระผู้เป็นเจ้า | ὀναίμην (NT-hapax optative) is the etymological root of Ὀνήσιμος |

Plus the name itself at 1:10 (ὃν ἐγέννησα ... Ὀνήσιμον) — Paul reveals the name at sentence-end after building emotional connection ("my child"), maximizing the rhetorical reveal.

**Current strategy:** the wordplay is surfaced explicitly in `thai_summary` at vv.10, 11, 20 — Thai prose explanations of the Greek name's meaning + the pun mechanics. The `thai` field uses ประโยชน์ ("benefit/profit") consistently, which preserves the semantic field but loses the etymological tie to the name (Thai readers don't see "Onesimus = useful" without the thai_summary).

**Two options Ben should weigh:**

**Option A (current):** Wordplay surfaced ONLY in thai_summary. Thai readers see clean text + a 1-2 sentence cultural-context explanation. The Greek pun is preserved in the scholarly notes for translators/reviewers but not visible to ordinary readers without engaging the summary.

**Option B (alternative):** Add an explicit verse-level footer note at v.10 (the introduction of the name) explaining the etymology — something like a brief footnote `*ชื่อโอเนซิมัสในภาษากรีก หมายความว่า "ผู้มีประโยชน์"` ("The name Onesimus in Greek means 'useful'"). This would make the wordplay visible to all readers, not just thai_summary readers. But it adds a footnote-style apparatus that the rest of the corpus doesn't use (no other Pauline letter has etymology-of-name footnotes).

**Editorial assessment:** Option A (current) is consistent with the rest of the corpus — proper-noun etymology is generally surfaced through thai_summary or scholarly notes, not main-text footnotes. Adding a footer note for Onesimus would be an exception to the corpus-wide convention. But Onesimus is unusually pun-heavy for a single short letter (3 wordplays in 25 verses) — there's a reasonable case for the exception.

**Question for Ben:** Stay with Option A (thai_summary only) or move to Option B (add a v.10 verse-level etymology note)?

---

## Recurrence forward (informational; no action items)

Pauline letters not yet shipped that share PHM patterns:

- **Ephesians, Philippians, Colossians** — all share the imprisonment-context (Paul as δέσμιος; Pauline "captivity epistles"). The δέσμιος → นักโทษ lock from PHM holds.
- **Philippians 2:25** — second NT occurrence of συστρατιώτης (after PHM 1:2). Established rendering เพื่อนร่วมรบ should hold.
- **Colossians 1:7, 4:7-12** — Onesimus, Tychicus, Epaphras all reappear. PHM proper-noun establishments (Onesimus → โอเนซิมัส; Epaphras → เอปาฟราส) hold.
- **Pastoral Epistles (1 Tim, 2 Tim, Titus)** — Paul's most personal letters; they will draw on PHM precedents for vocative ἀδελφέ → พี่น้องเอ๋ย, διακονέω → ปรนนิบัติ, σπλάγχνα → ใจ.

---

## Constraints respected

- No translation JSON files modified.
- No `RULES.md` / `docs/TRANSLATION_WORKFLOW.md` / `docs/END_OF_BOOK_CHECKLIST.md` changes.
- No `docs/translator_decisions/` files written by this audit (Item 1's recommended doc is OPTIONAL; not a v1 tag blocker).
- PR opened on `end-of-book-review-philemon-audit` branch (not pushed to main directly).
