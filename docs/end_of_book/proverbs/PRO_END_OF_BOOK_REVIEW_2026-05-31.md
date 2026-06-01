# Proverbs — End-of-Book Review

**Date:** 2026-05-31
**Scope:** All 31 chapters of Proverbs (`output/translations/proverbs_01.json` … `proverbs_31.json`); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** PRO 31 shipped (commit `0b61eff1`); per `docs/END_OF_BOOK_CHECKLIST.md` §2 + §3, fired by `scripts/detect_book_complete.py`.
**Mandate:** Internal editorial review (§2). Surface only — **no translation changes made.**

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1): 31/31 chapters have green per-chapter 7-check reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `audit_inclusion_variants.py --book PRO --strict` exits 0 (0 candidates — NT/SBLGNT-scoped, N/A for the Hebrew Wisdom text). `check_phrase_consistency.py` reports **4 Proverbs violations** (14:29, 15:18, 16:32, 25:15), all on the `אֶרֶךְ אַפַּיִם` "slow to anger / patient" idiom — see item 6 (the one concrete pre-tag fix). `git status` proverbs source clean. `export_to_usfm.py` / `build_external_review_packet.py` are NT/completed-book-code-scoped and do **not** yet know `PRO` (same tooling gap flagged for `PSA` in PR #188).
- **6 items LOCKED** — divine-name family; Rachasap honorific-binding (incl. the divine-eyes/hand reorderings); instruction register (בְּנִי → ลูกเอ๋ย); Selah-style transliteration N/A; superscription/heading versification (all aligned, no offsets); acrostic-marker mechanism (31:10–31).
- **5 items STABLE** — Lady-Wisdom personification + the 8:22 Christological crux; the rod-of-discipline pastoral frame; the honest-weights theme; NT-citation footnotes; the numerical-saying form (ch. 30).
- **2 items REVIEW** — the human-king non-royal register (item 2, the headline editorial decision); the Agur 30:4 "His Son" + 8:22 messianic-Wisdom reading.
- **1 item DECIDE** — item 6, the `אֶרֶךְ אַפַּיִם` rendering split; blocks a clean `check_phrase_consistency` before tagging `book-proverbs-v1`.
- **External AI review (§3) items prepared** (see `external_review_items_PRO.md`).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + verse-level rationale. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging `book-proverbs-v1`.

---

## 1. Divine-name family (YHWH / El-Elohim / Holy One / Adonai-construct / Maker / Redeemer) — **LOCKED** (`divine_names_table_2026-05.md`)

`יהוה` → **องค์พระผู้เป็นเจ้า** throughout, with a per-chapter first-occurrence Tier-2 footnote in every YHWH-bearing chapter, and the auto-YK Layer-1 `key_decisions` record per verse. The book's refrain **"the fear of the LORD"** (יִרְאַת יְהוָה) — the motto at 1:7, restated 9:10, and embodied at 31:30 — renders **ความยำเกรงองค์พระผู้เป็นเจ้า** uniformly. Other forms: `אֱלֹהִים`/`אֵל` → พระเจ้า; `קְדֹשִׁים` "the Holy One" (9:10; 30:3) → องค์บริสุทธิ์; `אֲדֹנֵי`-construct N/A here; `עֹשֵׂהוּ` "his Maker" (14:31; 17:5; 22:2) → พระผู้ทรงสร้าง; `גֹּאֵל` "Redeemer" (23:11) → พระผู้ไถ่. All conform. **LOCKED.**

## 2. Human-king register: non-royal — **REVIEW** (the headline editorial decision; recommend doc-lift)

Proverbs is dense with king/ruler proverbs (14:28,35; 16:10–15; 19:12; 20:2,8,26,28; 21:1; 22:11,29; 24:21; 25:2–7; 29:4,14,26; 31:1–9). The Eremos rendering keeps **human kings non-royal** — `กษัตริย์` as the repeated subject (not พระองค์), plain verbs (โปรดปราน, not ทรงโปรดปราน), `ความโกรธของกษัตริย์` (not พระพิโรธ), `สีหน้าของกษัตริย์` (not พระพักตร์), `ใจของกษัตริย์` (not the trap-prone royal forms) — **reserving the divine-royal register (ทรง / พระองค์ / พระพิโรธ / พระพักตร์ / พอพระทัย) for God alone.** This is consistent with the Psalms precedent (Pharaoh, the Davidic king of Ps 72/144 rendered non-royally) and keeps "พระองค์" unambiguously God across the whole corpus. The trade-off: Thai cultural norm *does* use ราชาศัพท์ for kings, so a Thai reader might expect light royal register for the king-proverbs. Footnoted once at 14:2. **REVIEW — confirm the non-royal policy and recommend `docs/translator_decisions/human_king_register_2026-05.md`** (compounds forward heavily into Kings/Chronicles/Esther/Daniel court narratives, and the Gospels' Herod/Pilate).

## 3. Rachasap honorific-binding + divine-eyes/hand reorderings — **LOCKED** (`ot_register_policy_2026-05.md`; `check_honorifics_binding.py`)

All 31 chapters cleared the honorifics check (0 hard fails after the build). Proverbs' recurring divine-body-part images were handled by the established reorder/verb techniques: **"the eyes of the LORD"** (5:21, 15:3, 22:12) reordered so พระเนตร is the subject of a *plain* verb (อยู่/เฝ้าดู/เฝ้าระวัง) or sits clause-final with no following ทรง; **"the king's heart in the hand of the LORD"** (21:1) reordered so ทรงหัน leads and พระหัตถ์ closes; **"His delight"** (רְצוֹנוֹ, 11:1,20; 12:22; 15:8; 16:7) → ทรงโปรดปราน, never พอพระทัย (avoids the พระทัย body-part); Agur's **"wind in His hands"** (30:4) kept อุ้งพระหัตถ์ clause-final. **LOCKED** (the Ps 144:7 "following-ทรง-verb" refinement applied throughout).

## 4. Instruction register: בְּנִי → ลูกเอ๋ย; the teacher's voice → เรา — **LOCKED-adjacent / STABLE**

The father-to-son address `בְּנִי` → **ลูกเอ๋ย** (plural בָּנִים → ลูกทั้งหลายเอ๋ย) uniformly across the lecture chapters (1–7, and the "my son" interjections through 19, 23, 24, 27). The instructor's first person ("my words / my teaching") → **เรา** (also used for Lady Wisdom and the Lemuel-mother). The mother's voice in 31:2 → แม่ + โอรส. Consistent and natural. **STABLE.**

## 5. Lady Wisdom personification + the 8:22 Christological crux — **STABLE / REVIEW**

`חָכְמָה` (feminine) personified as **ปัญญา / นาง / เรา** in chs. 1 (1:20–33), 8, 9 — the foil to the personified `אֵשֶׁת כְּסִילוּת` "Folly" (9:13–18) and the adulteress (ch. 7). The **8:22 crux** (`קָנָנִי`) was rendered **ทรงให้เราถือกำเนิด** "brought me forth" (matching the birth-language of 8:24–25), with a full Tier-2 footnote on the קנה range (possess/acquire/beget/create), the LXX `ἔκτισέν` "created" and the Arian controversy, and the NT Wisdom→Christ link (1 Cor 1:24,30; Col 1:15–17; John 1:1–3). The Agur **30:4 "what is the name of His Son?"** carries a parallel footnote (John 3:13). **REVIEW** — the messianic-Wisdom reading is doctrinally weighty; confirm the footnote framing is right for a Thai Buddhist-background readership.

## 6. `אֶרֶךְ אַפַּיִם` "slow to anger / patient" — **DECIDE** (clears `check_phrase_consistency`)

`check_phrase_consistency` flags 4 Proverbs violations on this idiom: rendered **โกรธช้า** at **15:18, 16:32** but **อดทน / ความอดทน** at **14:29, 25:15**. Both are faithful (slow-to-anger / patient), but the lock wants uniformity. Note 14:29 pairs it with its antonym `קְצַר־רוּחַ` "quick-tempered" (→ ใจร้อน), so a "slow/quick to anger" pairing reads most naturally there. **DECIDE:** approve a canonical rendering (recommend **ผู้ที่โกรธช้า** for the divine/proverbial "slow to anger," retaining อดทน only where the contrast is explicitly patience-vs-haste) and re-ship the affected chapters, OR document the two as accepted stylistic variants and tighten the lock. This is the only item blocking a clean phrase-consistency run. (Same idiom also appears in the Exod 34:6 formula — coordinate with the Psalms item in PR #188.)

## 7. Honest-weights / commercial-integrity theme — **STABLE**

`אֶבֶן וָאֶבֶן` / dishonest scales as an abomination to the LORD (11:1; 16:11; 20:10, 23) render uniformly (ตราชั่ง/ตุ้มน้ำหนักที่ไม่ซื่อตรง…เป็นที่น่ารังเกียจต่อองค์พระผู้เป็นเจ้า), with footnotes linking Lev 19:36 / Deut 25:13–16. **STABLE.**

## 8. The rod-of-discipline pastoral frame — **STABLE** (recommend doc-lift)

`שֵׁבֶט` "rod" of correction (13:24; 22:15; 23:13–14; 29:15) rendered **ไม้เรียว** with a consistent Tier-2 pastoral footnote framing it as *loving discipline/correction* (מוּסָר), explicitly not abuse, tied to God's loving discipline (3:11–12 / Heb 12:6). Given modern sensitivity, this recurring frame is worth locking. **STABLE — recommend `docs/translator_decisions/rod_of_discipline_2026-05.md`.**

## 9. NT-citation footnotes — **STABLE**

Uniform Tier-2 cross-references where the NT cites/echoes: 3:11–12→Heb 12:5–6; 3:34→Jas 4:6 / 1 Pet 5:5 (LXX form); 11:31→1 Pet 4:18 (LXX); 25:6–7→Luke 14:8–11; 25:21–22→Rom 12:20; 26:11→2 Pet 2:22; 27:1→Jas 4:13–14; 30:4→John 3:13; plus Lady Wisdom→Christ (item 5). **STABLE.**

## 10. Numerical sayings (Agur, ch. 30) — **STABLE**

The x/x+1 sayings ("three things… four", 30:15–31) and the leech/ants/locusts/lizard vignettes render naturally in Thai (มีสามสิ่ง…สี่สิ่ง). The 22:17–24:22 "Sayings of the Wise" and the Amenemope parallel footnoted at 22:17. **STABLE.**

## 11. The worthy-woman acrostic (31:10–31) — **LOCKED** (`ot_register_policy §5`)

22 `acrostic_marker` fields (א–ת) on the אֵשֶׁת חַיִל poem; Thai poetry natural (no Thai-alphabet equivalence attempted — Hebrew-form transparency only), footnoted as the embodiment of Lady Wisdom and the book's fear-of-the-LORD climax (31:30). Matches the Psalms acrostic mechanism (111, 112, 119, 145). **LOCKED.**

## 12. Collection-heading structure — **STABLE**

The seven section headings rendered + footnoted: 1:1 (Solomon, book title); 10:1 (Solomon, main collection); 22:17 + 24:23 (Sayings of the Wise + appendix); 25:1 (Hezekiah collection); 30:1 (Agur); 31:1 (Lemuel). All MT=BSB aligned (no versification offsets anywhere in Proverbs — confirmed). **STABLE.**

## 13. "Two ways" / righteous-vs-wicked antithetic frame — **STABLE** (strength)

The dominant antithetic-couplet form (10:1–15:33 esp.) rendered with consistent contrastive Thai (…แต่…), and the keyword pairs are uniform: צַדִּיק=คนชอบธรรม, רָשָׁע=คนชั่ว, חָכָם=คนมีปัญญา, כְּסִיל/אֱוִיל=คนโง่, פֶּתִי=คนรู้น้อย, לֵץ=คนชอบเยาะเย้ย. **STABLE — strength.**

## 14. Anthropomorphism preservation — **STABLE** (strength)

God's body-part imagery preserved where the Hebrew has it (the eyes of the LORD; the LORD's hand at 21:1; Agur's "wind in His hands" 30:4) rather than paraphrased away, while satisfying the binding rule (item 3). **STABLE — strength.**

---

## Recommended new translator-decisions docs (if Ben approves)

- `docs/translator_decisions/human_king_register_2026-05.md` (item 2 — non-royal human kings; high forward-compounding)
- `docs/translator_decisions/rod_of_discipline_2026-05.md` (item 8 — the pastoral ไม้เรียว frame)

## DECIDE item blocking `book-proverbs-v1`

- **Item 6** — approve a canonical `אֶרֶךְ אַפַּיִם` rendering (normalize 14:29/15:18/16:32/25:15) + phrase-lock tightening. Only item blocking a clean `check_phrase_consistency`. All others are LOCKED/STABLE/REVIEW and do not block the tag.
