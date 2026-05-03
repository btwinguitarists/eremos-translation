# James — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 5 chapters (108 verses; 277 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (43 docs).
**Trigger:** JAS 5 shipped (commit `5bde9a4`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 + §3 of checklist). Surface only — no translation changes in this PR.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 5/5 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` clean apart from the verification re-run artifact.
- **James is the FIRST General/Catholic epistle the project has shipped** — distinct from the Synoptic-narrative, Johannine, Acts, and Pauline corpora that came before. James is wisdom-genre (closest NT analogue to Proverbs), pre-Pauline in date for those who hold the early-James view, and addresses the διασπορά rather than a named church. The audit confirms strong CONTINUITY with the inherited Synoptic + Pauline corpus on the locked-vocabulary set (ἐκκλησία, ἀδελφοί, πατήρ register split, narrator-κύριος, παρουσία, ψυχή, γέεννα, ἁμαρτία, ταπεινός cluster, ὑπομονή) AND surfaces three distinctive James-only clusters that need maintainer attention: **(a) δικαιόω in James 2:21/24/25 vs. the locked Pauline forensic-declarative rendering**, **(b) νόμος uniformly rendered as ธรรมบัญญัติ across all senses including James-distinctive "νόμος-of-X" constructions** ("perfect law of liberty," "royal law"), and **(c) the 4:5 πνεῦμα crux** (one of the most contested verses in the NT).
- **8 inherited corpus-locks verified compliant** in JAS (παρουσία, ἐκκλησία, narrator-κύριος, ταπεινός, ψυχή, ὑπομονή, πρόσωπολημψία, divine-passive δίδωμι/ἐγείρω with royal-prefix).
- **5 cross-cutting James-distinctive patterns are STABLE-but-undocumented at corpus level** (σοφία ἄνωθεν cluster + 7-fold list at 3:17; κύριος Σαβαώθ at 5:4; χαίρειν-χαρά keyword bridge in 1:1–2; the τέλειος-cluster at 1:4, 1:17, 1:25, 3:2; the πειρασμός lemma-ambiguity preserved across testing/temptation senses). Three of these are first-occurring in JAS and need corpus-doc lift before 1 Peter / 2 Peter / Jude (the remaining General Epistles, where overlapping vocabulary will recur).
- **5 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: πειρασμός deliberate lemma-ambiguity 1:2–15; βασιλικὸς νόμος rendering 2:8; the μοιχαλίδες explicit "พระเจ้า" disambiguation at 4:4; anointing-with-oil interpretive ambiguity at 5:14; δίκαιος at 5:6 generic-vs-Christological).
- **2 items flagged DECIDE** (1: δικαιόω in James 2:21/24/25 currently uses **ทรงนับว่าชอบธรรม** which the locked `dikaioo_dikaiosyne_family_2026-05.md` doc explicitly **rejected** as the Pauline rendering — does the lock apply to non-Pauline James?; 2: νόμος uniformly rendered as ธรรมบัญญัติ across all 12 JAS occurrences including the "law of liberty" / "royal law" / "law of freedom" Pauline-style genitive-of-X constructions — does the `nomos_pauline_2026-05.md` two-rendering split apply to James?).
- **External AI review (§3) packet built and ready** for paste into Grok / ChatGPT / Gemini.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. δικαιόω at JAS 2:21, 2:24, 2:25 vs. the locked Pauline forensic-declarative rendering — **DECIDE**

JAS 2:14–26 is the famous faith-and-works passage. The δικαιόω lemma occurs **3× in this passage** (2:21, 2:24, 2:25) plus 1× in the OT-citation at 2:23 via cognate λογίζομαι. The current Thai rendering uses **ทรงนับว่าชอบธรรม / ได้รับการนับว่าชอบธรรม** (the **นับ** verb-stem) for δικαιόω:

| Verse | Greek | Thai (current) |
|---|---|---|
| 2:21 | οὐκ ἐξ ἔργων ἐδικαιώθη | **ทรงได้รับการนับว่าชอบธรรมโดยการกระทำ ... มิใช่หรือ** |
| 2:23 | ἐλογίσθη αὐτῷ εἰς δικαιοσύνην (Gen 15:6 LXX) | **ทรงนับให้เป็นความชอบธรรมแก่ท่าน** |
| 2:24 | ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον | **คนเราได้รับการนับว่าชอบธรรมโดยการกระทำ และไม่ใช่โดยความเชื่ออย่างเดียว** |
| 2:25 | οὐκ ἐξ ἔργων ἐδικαιώθη | **ก็ได้รับการนับว่าชอบธรรมโดยการกระทำของนาง ... มิใช่หรือ** |

The locked `docs/translator_decisions/dikaioo_dikaiosyne_family_2026-05.md` (decided 2026-05-01 after the Romans 1–5 audit, reaffirmed by the Galatians external AI review) specifies for **all Pauline forensic-declarative δικαιόω**:

> **Default rendering:** passive δικαιόω → **ทรงถูกประกาศว่าชอบธรรม** (royal divine-passive)
>
> **Critical: do NOT use นับ (count/reckon) for δικαιόω.** `นับ` is reserved for **λογίζομαι** (Pauline-bookkeeping-vocabulary) ... Collapsing δικαιόω into the same Thai verb destroys Paul's deliberate two-step argument structure.

The James 2:21 KD explicitly cites:

> "δικαιόω → ทรงได้รับการนับว่าชอบธรรม corpus-precedent ACT 13:38 + GAL 2:16 + Tit 3:7 same lemma."

But ACT 13:38, GAL 2:16, and Tit 3:7 have **all been re-locked to ทรงประกาศว่า/ถูกประกาศว่า** under the Pauline forensic-declarative doc. The James KD is citing pre-2026-05-01 corpus-precedents that no longer hold.

**The crux:** James is **non-Pauline** (a separate authorship, addressing different theological concerns). The Pauline lock says δικαιόω = forensic-courtroom-declaration. James 2:24's claim "**ἐξ ἔργων δικαιοῦται ἄνθρωπος καὶ οὐκ ἐκ πίστεως μόνον**" — "a person is justified by works and not by faith alone" — is the most-debated single sentence in the NT for the Paul-vs-James faith-and-works tension. Two possible James-corpus stances:

**Option A — Apply the Pauline lock to James** (relock 2:21, 2:24, 2:25 to **ทรงถูกประกาศว่าชอบธรรม / ประกาศว่า ... ชอบธรรม**)

- **Pro:** Pauline-forensic-declarative is the lexically-precise reading of δικαιόω across the entire Greek NT. The same Greek lemma should produce the same Thai verb wherever it occurs in identical syntax (passive divine-subject, soteriological frame).
- **Pro:** Preserves the JAS 2:23 (λογίζομαι → นับ) vs. 2:24 (δικαιόω → ประกาศ) lexical distinction across the same paragraph — exactly the structure the Pauline lock protects in Romans 4.
- **Con:** Makes the Paul/James apparent-tension MORE acute for the lay Thai reader. Both Paul (e.g., Rom 3:28) and James (2:24) become "ประกาศว่าชอบธรรม" with opposite predicates — the reader sees a direct theological clash.
- **Con:** Most modern English translations (NIV, ESV, NLT, CSB) DO render δικαιόω uniformly as "justify" across both Paul and James — the Pauline lock matches that English-evangelical pattern. The Pauline-James tension is in the GREEK and is preserved by uniform-rendering.

**Option B — Keep James as ทรงนับว่าชอบธรรม** (current); document as principled non-Pauline exception

- **Pro:** James's δικαιόω is doing different lexical-rhetorical work than Paul's — it is closer to the OT/Jewish-wisdom "be vindicated / be reckoned-righteous" sense (cf. James 2:23 immediately quoting Gen 15:6 with λογίζομαι). The JAS 2:21/24/25 + 2:23 cluster are deliberately echoing the Genesis-15 ἐλογίσθη — the Thai นับ-stem unifies that echo.
- **Pro:** Preserves the historic Reformation harmonization-strategy: Paul's δικαιόω = forensic-declarative; James's δικαιόω = demonstrative-vindication ("shown-to-be-righteous"). Different Thai verbs map to that interpretive distinction.
- **Con:** Two Thai verbs for one Greek lemma based on book-of-origin is a hermeneutical commitment, not a lexical distinction. It pre-decides the Paul/James harmonization for the reader rather than letting the Greek tension stand.
- **Con:** James's Gen 15:6 OT-citation at 2:23 ALSO uses **นับ** (for λογίζομαι) — so within JAS 2:21–25, both lemmas collapse into the same Thai verb. Loses the structural distinction the Pauline lock preserves in Romans 4.

**Option C — Hybrid**: Render JAS 2:21, 2:24, 2:25 as **ถูกประกาศว่าชอบธรรม** (per Pauline lock) AND add a verse-level Note flagging the Paul/James tension as a feature-not-bug; let `thai_summary` carry the harmonization rather than the lexical choice.

**Recommend: DECIDE.** This is the single highest-stakes editorial question raised by the James audit. The corpus-doc `dikaioo_dikaiosyne_family_2026-05.md` does NOT name James in its scope ("All **Pauline** δικαιόω-verb"), so the silent default is currently Option B, but the question of whether to extend the lock to James warrants explicit Ben-decision before `book-james-v1`. The external AI review packet (§3) carries this as Item A.

---

## 2. νόμος uniformly rendered as ธรรมบัญญัติ across all senses — **DECIDE**

JAS has **12 νόμος occurrences** spanning multiple semantic registers, all uniformly rendered as **ธรรมบัญญัติ**:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:25 | νόμον τέλειον τὸν τῆς ἐλευθερίας | **ธรรมบัญญัติอันสมบูรณ์ คือธรรมบัญญัติแห่งเสรีภาพ** | "perfect law of liberty" — James-distinctive |
| 2:8 | νόμον ... βασιλικόν | **ธรรมบัญญัติแห่งพระมหากษัตริย์** | "royal law" / "law of the king" |
| 2:9 | ὑπὸ τοῦ νόμου ὡς παραβάται | **ถูกธรรมบัญญัติพิพากษาว่าเป็นผู้ละเมิด** | Mosaic Torah |
| 2:10 | πάντα τὸν νόμον τηρήσῃ | **รักษาธรรมบัญญัติทั้งหมด** | Mosaic Torah |
| 2:11 | παραβάτης νόμου | **ผู้ละเมิดธรรมบัญญัติ** | Mosaic Torah |
| 2:12 | διὰ νόμου ἐλευθερίας | **โดยธรรมบัญญัติแห่งเสรีภาพ** | "law of freedom" |
| 4:11 | καταλαλεῖ νόμου καὶ κρίνει νόμον (×4 in this verse) | **พูดใส่ร้ายธรรมบัญญัติ ... พิพากษาธรรมบัญญัติ ... ผู้ปฏิบัติตามธรรมบัญญัติ** | the law-as-norm |

Note: I have excluded 1:6, 1:12, 3:4, 5:10, 5:14 from the table — those greek hits matched on partial-stem patterns but do not contain the νόμος lemma.

The locked `docs/translator_decisions/nomos_pauline_2026-05.md` (decided 2026-05-02 after Romans audit + external AI review) implements a **two-rendering policy**:

> ธρρρμ for Mosaic-Torah / Pentateuch / law-as-canonical-text; **กฎ** for Pauline-rhetorical νόμος-of-X principle / governing-pattern / inner-norm.
>
> "**νόμος-of-X-genitive constructions where X is NOT God-as-covenant-giver** (νόμος ἁμαρτίας / θανάτου / πνεύματος τῆς ζωῆς / νοός / Χριστοῦ — the 'law of Christ' being the pivotal case)" → **กฎ**

Three of the 12 JAS νόμος occurrences are precisely Pauline-style "νόμος-of-X-genitive" constructions where X is an abstract quality:

- **1:25 + 2:12: νόμος (τῆς) ἐλευθερίας** ("law of freedom") — by Pauline-lock criterion would be **กฎแห่งเสรีภาพ**
- **2:8 νόμος βασιλικός** ("royal law") — adjectival not genitive, but the same Pauline-style "law-characterized-by-X" semantics

The current James rendering (uniform **ธรรมบัญญัติ** everywhere) is a **monolithic-Mosaic stance**: James's "law of liberty" is read as **the Torah viewed under the New Covenant freedom-aspect** — i.e., James is talking about **the actual Mosaic Torah** with an attributive-modifier ("the perfect Torah, namely the Torah-of-liberty"), not an abstract Pauline-style principle.

**Two possible James-corpus stances:**

**Option A — Apply the Pauline two-rendering split to James** (relock 1:25, 2:8, 2:12 to use **กฎ**)

- **Pro:** Lexical consistency with the Pauline lock. "Law of X-genitive-quality" → กฎ across the entire NT regardless of book-of-origin.
- **Pro:** The "perfect law of LIBERTY" (1:25) is rhetorically very close to Paul's "law of the SPIRIT of LIFE" (Rom 8:2) — both are "law-as-internalized-principle" rather than "Torah-as-text."
- **Con:** James is Jewish-Christian wisdom-genre that addresses Diaspora Jews (1:1) and presupposes Mosaic-Torah-validity (2:8–12 explicitly works through commands of the Decalogue). Reading "law of liberty" as **กฎ** ("principle / governing-norm") rather than **ธρρρμ** ("Torah / law-code") may cut against James's Jewish-Torah-positive register.
- **Con:** James's νόμος is consistently the Torah throughout the letter — even at 4:11 where "law" is the norm-being-judged, it is still the actual Mosaic-Torah-as-norm, not an abstract Pauline-principle. Splitting only 1:25/2:8/2:12 to **กฎ** introduces an inconsistency the reader will feel.

**Option B — Keep James as uniform ธρρρμ** (current); document as principled non-Pauline exception

- **Pro:** Reflects James's wisdom-genre stance: the Torah IS the perfect-law-of-liberty for the Jewish-Christian community living-under-grace. There is one law, with attributive modifiers, not multiple "laws."
- **Pro:** Preserves the corpus distinction: Paul's "νόμος" is rhetorical-multivalent (code-vs-principle); James's νόμος is monovalent (always-the-Torah). Different Thai renderings reflect different theological registers across the corpora.
- **Con:** The "νόμος βασιλικός" at 2:8 is grammatically an adjective-modifier; "law of the king" reads as "the King's law" in Thai (ธρρρμแห่งพระมหากษัตริย์) which is pleonastic if "the King" = God-the-divine-king (any law of God's is by-definition a "King's law"). The rendering is workable but worth confirmation.

**Option C — Hybrid**: Keep `νόμος-of-X` constructions in James as **ธρρρμ-แห่ง-X** (preserving the perfect-Torah-with-attribute reading) BUT document the principle in a new corpus-doc `nomos_jacobean_2026-05.md` that explicitly distinguishes James's monolithic-Mosaic νόμος from Paul's rhetorical-multivalent νόμος. This forecloses confusion when the General Epistles ship (1 Pet, 2 Pet, Jude all use νόμος sparsely; HEB will be the next major νόμος-cluster and will need its own decision).

**Recommend: DECIDE.** This is closely tied to Item 1 (both are "do the Pauline-corpus locks extend to James?" questions). The external AI review packet (§3) carries this as Item B. **Pre-recommendation: Option C (hybrid).** James's monolithic-ธρρρμ pattern is a feature, not a drift, but it deserves an explicit lock so that future translators understand it is principled.

---

## 3. σοφία ἄνωθεν + the 7-fold list at 3:17 — **STABLE (undocumented; recommend new doc — high General-Epistle-forward priority)**

σοφία occurs **4× in James** (1:5; 3:13; 3:15; 3:17), making James the most σοφία-dense NT book per chapter. The wisdom-from-above doctrine in 3:13–18 is the densest single passage on σοφία in the NT outside 1 Cor 1–2. The lock-worthy elements:

**The basic rendering: σοφία → ปัญญา** (corpus-precedent 1 Cor 1:19, 1:20). Uniform across all 4 occurrences. ✓ matches glossary.

**The earthly-vs-heavenly contrast (3:15–17):**

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 3:15 | ἐπίγειος, ψυχική, δαιμονιώδης | **ฝ่ายโลก ฝ่ายธรรมชาติ ฝ่ายผีปีศาจ** | downward triad |
| 3:17 | ἁγνή, εἰρηνική, ἐπιεικής, εὐπειθής, μεστὴ ἐλέους καὶ καρπῶν ἀγαθῶν, ἀδιάκριτος, ἀνυπόκριτος | **บริสุทธิ์, แห่งสันติ, สุภาพอ่อนโยน, ยอมเชื่อฟังโดยง่าย, เปี่ยมด้วยความเมตตาและผลดีทั้งหลาย, ไม่ลำเอียง, ไม่หน้าซื่อใจคด** | upward 8-fold (counting μεστὴ ... καρπῶν as one item) |

Five hapaxes in this passage alone (ἐπιστήμων, δαιμονιώδης, εὐπειθής, ἀδιάκριτος, plus the 1:5 ἁπλῶς). The 3:17 list is **Eremos's first major translation-decision on a NT virtue-list of this length** outside GAL 5:22–23 (fruit-of-the-Spirit) — the rendering quality is high (preserves both the ordering ("first-pure, THEN ...") and the doublet rhythm of the seven-virtues-following-purity).

**Editorial assessment:** The σοφία-from-above pattern is forward-pertinent. The General Epistles (1 Pet, 2 Pet, Jude) use σοφία sparsely; HEB and the Pastorals will recur with related virtue-lists. James's "wisdom-from-above" — divine-source-wisdom that contrasts with earthly-pseudo-wisdom — is a load-bearing biblical-theology category. Worth a brief corpus-doc.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/sophia_anothen_2026-05.md`. The doc should:
1. Lock σοφία → **ปัญญา** (continuity with Pauline)
2. Note the James-distinctive "from above" (ἄνωθεν → จากเบื้องบน) — same Thai as JHN 3:3, 3:7 (ἄνωθεν → "born from above") — preserving the divine-source idiom
3. Document the JAS 3:15 downward triad (earthly / soulish / demonic) and JAS 3:17 upward 7-fold list as the locking precedents
4. Cross-reference 1 Cor 2:6–7 ("σοφία τοῦ θεοῦ ἐν μυστηρίῳ") and the Pauline pseudo-wisdom critique for related-but-distinct contexts

---

## 4. κύριος Σαβαώθ at 5:4 — **STABLE (undocumented; recommend new doc)**

JAS 5:4 contains the **first NT explicit Σαβαώθ** transliteration outside Rom 9:29 (which is itself an Isa 1:9 OT-quote):

> Greek: εἰς τὰ ὦτα **Κυρίου Σαβαὼθ** εἰσεληλύθασιν
>
> Thai: ดังขึ้นถึง**พระกรรณขององค์พระผู้เป็นเจ้าจอมโยธา**แล้ว

**Σαβαώθ** is the LXX-loanword form of Hebrew **יהוה צבאות** ("YHWH of armies / LORD of Hosts"). The OT-divine-title preserves the Hebrew transliteration in Greek; Thai-Christian convention is to descriptively render it as **องค์พระผู้เป็นเจ้าจอมโยธา** ("Lord of the Heavenly Armies") rather than transliterate as **ซาบาโอธ**.

The 5:4 KD names the principle:

> "Hebrew-untranslated-loanword 'military-forces / heavenly-armies.' Render 'องค์พระผู้เป็นเจ้าจอมโยธา' — established Thai-Christian rendering of YHWH-Sabaoth (LORD-of-Hosts) preserving the divine-warrior title; transliterates the Hebrew-Sabaoth concept rather than the loanword."

The phrase carries the OT-prophetic imprecation register — JAS 5:1–6 is a prophetic-style invective against rich oppressors, deliberately echoing Isa 5:9 LXX (where κύριος Σαβαώθ is the divine-judge of the wealthy oppressors). The triple-OT-allusion in 5:4 (DEU 24:14–15 wages-cry-out + LEV 19:13 + MAL 3:5) is logged in `data/nt_ot_citations.json`.

Also in 5:4: the use of **พระกรรณ** ("[royal] ears") — the ราชาศัพท์ royal-honorific noun for divine ears — preserves the divine-anthropomorphic register. Compare JAS 5:11 **พระเมตตาและพระกรุณา** (royal-honorific divine-mercy + divine-compassion).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/kyrios_sabaoth_2026-05.md` before Rom 9:29 (next ship of Romans 9–16) and Heb 12:21–22 (where the divine-army imagery recurs). The doc should:
1. Lock κύριος Σαβαώθ → **องค์พระผู้เป็นเจ้าจอมโยธา** (descriptive-Thai not transliteration)
2. Cross-reference the Isa 5:9 LXX echo at JAS 5:4 + Rom 9:29
3. Document the divine-anthropomorphic ราชาศัพท์ pattern (พระกรรณ "[royal] ears") as parallel to the established narrator-κύριος divine-honorific register
4. Cite JAS 5:4 as the locking precedent

---

## 5. πειρασμός — deliberate lemma-ambiguity preserved across testing/temptation senses — **REVIEW**

JAS 1:2–15 contains the most-concentrated πειρασμ-stem cluster in the NT — the lemma occurs **6×** in 14 verses (1:2 πειρασμοῖς, 1:12 πειρασμόν, 1:13 πειραζόμενος, 1:13 πειράζομαι, 1:13 ἀπείραστος [hapax], 1:14 πειράζεται). Critical: the lemma SHIFTS senses between v.2–3 (TEST/TRIAL) and v.13–14 (TEMPTATION).

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:2 | πειρασμοῖς ποικίλοις περιπέσητε | **เผชิญการทดลองต่าง ๆ** | trials (external test of faith) |
| 1:3 | τὸ δοκίμιον ὑμῶν τῆς πίστεως | **การทดสอบความเชื่อของท่าน** | testing-process |
| 1:12 | μακάριος ἀνὴρ ὃς ὑπομένει πειρασμόν | **คนที่อดทนต่อการทดลอง** | trial endurance |
| 1:13 | μηδεὶς πειραζόμενος λεγέτω ὅτι Ἀπὸ θεοῦ πειράζομαι | **เมื่อถูกทดลอง อย่าให้ผู้ใดกล่าวว่า "พระเจ้ากำลังทดลองข้าพเจ้า"** | temptation (NOT trial) |
| 1:13 | ὁ θεὸς ἀπείραστός ἐστιν κακῶν, πειράζει δὲ αὐτὸς οὐδένα | **พระเจ้าไม่อาจถูกทดลองให้ทำชั่ว และพระองค์เองก็ไม่ทรงทดลองผู้ใดเลย** | God-untemptable, untempting |
| 1:14 | ὑπὸ τῆς ἰδίας ἐπιθυμίας πειράζεται | **ถูกตัณหาของตนเองชักออกไป** | desire-tempts |

The 1:13 KD names the principle:

> "πειρασμός lemma starts at the trial/test-of-faith sense (will shift to temptation-by-desire sense at v.13 — same Greek lemma, same Thai 'การทดลอง,' context disambiguates)."

**Editorial assessment:** Single Thai rendering **การทดลอง / ทดลอง** preserves the lemma-link that James deliberately constructs (vv.2–3 trials produce endurance + v.12 trial-endurance is rewarded → v.13 don't blame God for the same πειρασμός — for HE is not the source of the inward-temptation-form of the πειρασμός). The conscious wordplay is rare-but-theologically-load-bearing: James uses the polyseme to argue that **the same EVENT can be a trial-of-faith from God's perspective and a temptation-toward-sin from the desire's perspective; the moral responsibility lies with the desire, not with God**. Single Thai rendering preserves this argumentative-structure.

The English-translation tradition is split:
- **NIV / NLT / CSB:** "trials" (vv. 2–3, 12) + "tempt / temptation" (vv. 13–14) — different English words.
- **ESV / NRSV:** "trials" (vv. 2–3, 12) + "tempted" (vv. 13–14) — different English words but cognate.
- **NASB / KJV:** uniform "tempt / temptation" — preserves the lemma-link English-side.

The Thai single-rendering tracks the NASB/KJV approach (single Thai term with context-disambiguation) rather than the NIV/CSB approach (two English terms reflecting two senses).

**REVIEW flag:** Confirm with Ben that the deliberate lemma-ambiguity preservation is the right register call. Two questions:
1. Is the single-Thai-term policy (preserving the πειρασμός-cluster wordplay) preferable to a two-rendering split (e.g., **การทดสอบ** for trials/test-of-faith senses + **การล่อลวง** or **การประจญ** for temptation senses)?
2. Should JAS 1:13 add an explicit **thai_summary** clarifying the lemma-shift for Thai readers who may not catch the wordplay without exegetical-help? (Currently no thai_summary on 1:13.)

---

## 6. βασιλικὸς νόμος at 2:8 — **REVIEW**

The phrase **νόμον τελεῖτε βασιλικόν** at JAS 2:8 is rendered:

> Thai: **ปฏิบัติตามธรรมบัญญัติแห่งพระมหากษัตริย์**

The 2:8 KD names the principle:

> "Per uW figs-metonymy on βασιλικός: dual-possible-meaning (1) law-of-the-king's-kingdom, (2) law-given-by-the-divine-king. Render 'ธρρρμบัญญัติแห่งพระมหากษัตริย์' — preserves the king-divine-law-source sense, leaving the kingdom-of-God interpretation accessible without forcing it."

**Editorial assessment:** The phrase has at least three competing readings:
- (a) **"royal law"** = the Torah given by the divine-King (current Thai; preserves source-attribution)
- (b) **"the king's law"** = the law of the kingdom-of-God / the kingdom-ethic (eschatological-kingdom reading)
- (c) **"the supreme/preeminent law"** = the law that takes-precedence-over-all-others (intensifier reading; see e.g., NIV "royal law")
- (d) **"the law of the King"** = the law given by Jesus-as-King (Christological reading; cf. Jesus's "love your neighbor" teaching at MAT 22:39)

The Greek βασιλικός is genuinely ambiguous between these. Most modern English translations preserve the ambiguity with "royal law" (NIV/ESV/NASB/CSB). **ธρρρμบัญญัติแห่งพระมหากษัตริย์** ("law of the divine-king") commits to reading (a) + (d) (the law SOURCED FROM the divine-king), and forecloses (c) (the supreme/preeminent reading).

**Alternatives considered:**
- **กฎอันสูงส่ง** ("supreme/exalted law") — preserves reading (c)
- **ธρρρμบัญญัติของกษัตริย์** ("law of the king") — slightly more neutral; doesn't resolve King = God or = Christ
- **ธρρρμบัญญัติแห่งราชา** — register-issue (ราชา is poetic-archaic; less natural than พระมหากษัตริย์)

**REVIEW flag:** Confirm with Ben that the **ธρρρμบัญญัติแห่งพระมหากษัตริย์** rendering is the right interpretive commitment. Worth aligning with βασιλεία-rendering at JAS 2:5 (κληρονόμους τῆς βασιλείας → **ทายาทแห่งอาณาจักร**) — i.e., the divine-king who gives the law (2:8) is the same divine-king whose kingdom believers inherit (2:5). The current rendering aligns with that internal-frame.

---

## 7. φιλία τοῦ κόσμου + μοιχαλίδες at 4:4 — **REVIEW**

JAS 4:4 contains the strongest single condemnation-of-worldliness in the NT:

> Greek: **μοιχαλίδες**, οὐκ οἴδατε ὅτι ἡ φιλία τοῦ κόσμου ἔχθρα τοῦ θεοῦ ἐστιν
>
> Thai: ท่านทั้งหลาย**ผู้นอกใจพระเจ้า**เอ๋ย ท่านไม่รู้หรือว่า การเป็นมิตรกับโลกย่อมเป็นการเป็นศัตรูกับพระเจ้า

The translator has made **two distinctive interpretive moves**:

**(1) μοιχαλίδες → ผู้นอกใจพระเจ้า** ("those-unfaithful-to-God") — adds explicit "พระเจ้า" to disambiguate the OT-prophetic-marriage-metaphor.

The KD names the rationale:

> "μοιχαλίς 'adulteress' as OT-prophetic-metaphor for unfaithfulness-to-God (HOS, JER 3:8, EZK 16, etc.). Render 'ผู้นอกใจพระเจ้า' — preserves the spiritual-unfaithfulness sense; explicit 'พระเจ้า' added to disambiguate the metaphor (Thai readers may not immediately catch the OT-prophetic-marriage-metaphor without it)."

This is a deliberate **metaphor-explanation** (not flattening): preserves the "unfaithfulness" semantic but supplies the explicit "to-God" complement that the Greek leaves implicit. Compare flat alternatives:
- **ผู้ล่วงประเวณีทั้งหลาย** ("adulterers/adulteresses") — preserves literal but loses the OT-prophetic figurative-unfaithfulness sense; readers without OT-background may take it as literal sexual-immorality
- **คนเหลาะแหละ** ("faithless ones") — losses the marital-covenant register entirely

**(2) HAPAX φιλία → การเป็นมิตร** ("being-a-friend / friendship") — straightforward.

Combined effect: the rendering makes James's anti-worldliness rhetoric clearer to Thai readers BUT commits to a specific interpretive stance (the μοιχαλίδες are the same group later named in v.8 as "double-minded" + "sinners" — Christian believers compromised with worldly values). Some commentators read μοιχαλίδες more narrowly (literal-female-adulterers in James's audience) — the explicit "พระเจ้า" closes that reading.

**REVIEW flag:** Confirm with Ben that the explicit "พระเจ้า" disambiguation at 4:4 is the right call. The Hebraic OT-prophetic-marriage-metaphor (HOS 1–3; JER 3:8; EZK 16, 23) is theological-load-bearing; collapsing it into a plain "unfaithful" + explicit "to-God" may lose the marital-covenant intimacy. The trade-off is access for Thai readers without OT-background.

---

## 8. πνεῦμα at 4:5 — the difficult-verse ambiguity — **REVIEW**

JAS 4:5 is among the most difficult-to-translate verses in the entire NT:

> Greek: ἢ δοκεῖτε ὅτι κενῶς ἡ γραφὴ λέγει· **Πρὸς φθόνον ἐπιποθεῖ τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν;**
>
> Thai: หรือท่านคิดว่าพระคัมภีร์กล่าวอย่างเปล่าประโยชน์หรือว่า "**วิญญาณที่พระองค์ทรงให้สถิตในเราโหยหาด้วยความริษยา**"

The 4:5 KD names the difficulty explicitly:

> "DIFFICULT VERSE — multiple-interpretations per uW. The Spirit-as-subject reading (option 1) renders most-naturally: 'the Spirit [that God caused-to-dwell-in-us] yearns [with envy / jealousy].' ... πνεῦμα ambiguous — either Holy-Spirit or human-spirit; render 'วิญญาณ' preserves the same-Greek-ambiguity (Thai 'วิญญาณ' used for both Holy-Spirit and human-spirit contextually)."

**The interpretive cube** (per major commentaries):

1. **Subject of ἐπιποθεῖ:**
   - (i) τὸ πνεῦμα (the Spirit) — "the Spirit yearns ..."
   - (ii) God (with πνεῦμα as object) — "[God] yearns toward the spirit ..."

2. **Identity of πνεῦμα:**
   - (a) Holy Spirit (divine-Spirit dwelling-in-us)
   - (b) human-spirit (the human spirit-that-God-caused-to-dwell-in-us at creation)

3. **Sense of πρὸς φθόνον:**
   - (α) negative-jealousy (the human-spirit yearns-with-evil-envy → vice critique)
   - (β) positive-divine-jealousy (the divine-Spirit longs-jealously for our complete devotion → divine-jealousy parallel to OT)

The Thai **วิญญาณที่พระองค์ทรงให้สถิตในเรา** is a natural-reading rendering of **τὸ πνεῦμα ὃ κατῴκισεν ἐν ἡμῖν** that:
- Treats πνεῦμα as the **subject** (option (i))
- Uses **วิญญาณ** (without royal **พระ-** prefix) — leaves the divine-vs-human-spirit reading **open** (Thai **วิญญาณ** is used for both human-spirit and divine-Spirit contextually; the absence of royal-pระ is a slight leaning toward (b) human-spirit)
- Renders **πρὸς φθόνον → ด้วยความริษยา** with negative connotation (option (α))

This combines into reading (i)+(b)+(α): "**the human-spirit-that-God-caused-to-dwell-in-us yearns with [evil] envy**." Most modern English translations split:
- **NIV:** "the spirit he caused to dwell in us envies intensely" — reading (i)+(b)+(α) ✓ matches Thai
- **ESV:** "He yearns jealously over the spirit that he has made to dwell in us" — reading (ii)+(b)+(β); footnote acknowledges (i)
- **NASB:** "He jealously desires the Spirit which He has made to dwell in us" — reading (ii)+(a)+(β)

**REVIEW flag:** The current Thai locks reading (i)+(b)+(α). This is the **NIV-aligned** reading and is defensible. But it is one of three+ live readings, and the Greek itself is genuinely ambiguous. Alternatives:
- Accept the lock (current); keep the verse-Notes referencing the multiple readings
- Add a verse-footer-note (Tier 2) acknowledging that ESV/NASB take a different reading
- Re-render to preserve more ambiguity (e.g., **วิญญาณซึ่งพระองค์ทรงให้สถิตในเรานั้น โหยหาด้วยความหึงหวง** — using **หึงหวง** "jealousy-as-zeal" rather than **ริษยา** "envy-as-vice"; this preserves the (β) positive-divine-jealousy reading)

This is a verse where the per-chapter automated check passed (single rendering decision, BT-clean), but the editorial-stance is high-stakes given the verse's interpretive density.

---

## 9. anointing-with-oil at 5:14 — sacramental-vs-medicinal ambiguity preserved — **REVIEW**

JAS 5:14 is the **locus classicus** for the sacrament of anointing-the-sick (Catholic Extreme-Unction / Eastern Orthodox Holy-Unction) AND for charismatic / Pentecostal healing-prayer practice:

> Greek: ἀσθενεῖ τις ἐν ὑμῖν; προσκαλεσάσθω τοὺς πρεσβυτέρους τῆς ἐκκλησίας, καὶ προσευξάσθωσαν ἐπ' αὐτὸν **ἀλείψαντες αὐτὸν ἐλαίῳ** ἐν τῷ ὀνόματι τοῦ κυρίου
>
> Thai: ในพวกท่านมีใครป่วยหรือ ผู้นั้นจงเชิญผู้ปกครองของคริสตจักรมา ให้เขาทั้งหลายอธิษฐานเผื่อเขา และ**เจิมด้วยน้ำมัน**ในพระนามขององค์พระผู้เป็นเจ้า

**Key choices:**

1. **πρεσβυτέρους τῆς ἐκκลησίας → ผู้ปกครองของคริสตจักร** ("elders of the church") — corpus-locked from 1 Tim 5:19 + Tit 1:5. ✓ matches `ekklesia_2026-04.md`.
2. **ἀλείψαντες αὐτὸν ἐλαίῳ → เจิมด้วยน้ำมัน** ("anoint with oil") — literal-rendering. **No interpretive commitment** to sacramental-vs-medicinal reading.
3. **ἐν τῷ ὀνόματι τοῦ κυρίου → ในพระนามขององค์พระผู้เป็นเจ้า** — corpus-standard divine-name rendering.

The 5:14 KD acknowledges the dual-function:

> "Per uW translate-unknown: oil-anointing dual-function: medical + consecration. Render 'ด้วยน้ำมัน' — preserves the oil-anointing practice (transfers naturally to Thai-Christian practice)."

**Editorial assessment:** **เจิมด้วยน้ำมัน** ("anoint with oil") preserves both readings — the medicinal reading (oil as 1st-century antibiotic; cf. Mark 6:13) and the sacramental reading (oil as consecrated-instrument-of-divine-grace). Thai **เจิม** ("anoint") is the established Christian-vocabulary verb (used for OT-priestly-anointing, prophetic-anointing, kingly-anointing); applying it to JAS 5:14 produces a register-consistent-rendering that does NOT pre-decide the sacramental question.

**REVIEW flag:** This is principled but worth Ben's confirmation. Three sub-questions:
1. Is **เจิมด้วยน้ำมัน** the right rendering for ἀλείψαντες ἐλαίῳ? It is theologically-neutral and the established Thai-Christian standard. Alternative: **ทาน้ำมัน** ("apply oil") — more medicinal-leaning but loses the consecration-register.
2. Should the verse have a footer-note acknowledging the sacramental-vs-medicinal interpretive divide? The English-language CSB / NLT precedent is to leave the rendering bare and let the reader (or commentary) resolve.
3. The 5:15 σώσει τὸν κάμνοντα is rendered **ช่วยผู้ป่วยให้หาย** ("heal the sick") — uses physical-healing **ให้หาย** rather than the soteriological **ให้รอด**. This is interpretive (σῴζω here = heal-from-sickness, not save-from-sin) and well-handled, but it commits to the physical-healing reading. Worth confirmation.

---

## 10. δίκαιος at 5:6 — generic-righteous-person vs Christological — **REVIEW**

JAS 5:6 contains the climax of the prophetic-imprecation-against-rich-oppressors:

> Greek: κατεδικάσατε, ἐφονεύσατε **τὸν δίκαιον**, οὐκ ἀντιτάσσεται ὑμῖν
>
> Thai: ท่านได้ตัดสินลงโทษและฆ่า**ผู้ชอบธรรม** เขามิได้ต่อต้านท่านเลย

The current rendering **ผู้ชอบธรรม** is a **generic** "righteous person" (singular-collective in Thai, like Greek τὸν δίκαιον). This is the modern-majority reading: the rich oppress and condemn-to-death poor-just-people (legal-injustice and economic-violence pattern of 5:1–6).

**Alternative reading: Christological "the Righteous One" (Christ).** ACT 3:14, 7:52, 22:14 use **τὸν δίκαιον** as a Messianic title for the crucified-Jesus. If JAS 5:6 is read Christologically, the verse becomes "you condemned and murdered **THE RIGHTEOUS ONE [= Jesus]**" — a startling shift from socio-economic invective to Christological accusation against the rich.

The current Thai **ผู้ชอบธรรม** without honorifics or definite-article-strengthening leans **generic**. To render Christologically would require **องค์ผู้ชอบธรรม** ("THE Righteous One") with the **องค์**-honorific that the corpus uses for Christ-as-Messianic-title (cf. ACT 3:14 corpus rendering).

**REVIEW flag:** Confirm with Ben that the generic-reading is the corpus-default for JAS 5:6. The modern-commentary-majority leans generic (the verse is the climax of the social-justice invective, not Christological); but the Christological reading has patristic support and is a live minority-reading in evangelical commentary.

---

## 11. παρουσία at 5:7, 5:8 — **LOCKED ✓**

JAS 5:7 + 5:8 contain the **only παρουσία** occurrences in James:

| Verse | Greek | Thai |
|---|---|---|
| 5:7 | ἕως τῆς παρουσίας τοῦ κυρίου | **จนกว่าจะถึงการเสด็จมาขององค์พระผู้เป็นเจ้า** |
| 5:8 | ἡ παρουσία τοῦ κυρίου ἤγγικεν | **การเสด็จมาขององค์พระผู้เป็นเจ้าใกล้เข้ามาแล้ว** |

The 5:7 KD explicitly cites the corpus-lock:

> "CORPUS-LOCKED παρουσία (Christ-eschatological) → การเสด็จมา per parousia_christou_2026-05.md."

**Both occurrences comply** with `docs/translator_decisions/parousia_christou_2026-05.md` ✓ (Christ-subject → royal **เสด็จ** register). The 5:8 ἤγγικεν → **ใกล้เข้ามาแล้ว** is a perfect-tense-with-present-state rendering matching corpus pattern.

**LOCKED** ✓ — second General-Epistle confirmation of the παρουσία-lock (after 1 Thess + 2 Thess + Phil established it for Pauline corpus). The James farmer-and-rains analogy (5:7) is distinctively Jewish-agricultural (πρόϊμον "early/autumn rain" + ὄψιμον "late/spring rain" — both NT hapaxes, rendered **ฝนต้นฤดู + ฝนปลายฤดู** with the explicit-rain disambiguation per uW figs-explicit).

---

## 12. πρόσωπολημψία cluster (2:1, 2:9) — **LOCKED ✓**

| Verse | Greek | Thai |
|---|---|---|
| 2:1 | μὴ ἐν προσωπολημψίαις ἔχετε τὴν πίστιν | **ท่านอย่าถือความเชื่อ ... ด้วยการเลือกหน้าผู้คน** |
| 2:9 | προσωπολημπτεῖτε | **ถ้าท่านเลือกหน้าผู้คน** |

The 2:1 KD cites the Pauline corpus-precedents:

> "Render การเลือกหน้าผู้คน corpus-precedent COL 3:25 ('ไม่ทรงเลือกหน้าผู้ใด') + EPH 6:9 ('การเลือกหน้า') same lemma."

**LOCKED** ✓ — uniform-Thai across Pauline + James occurrences. The plural προσωπολημψίαις (2:1) → **การเลือกหน้าผู้คน** preserves the general-practice plural; the verb προσωπολημπτεῖτε (2:9) → **เลือกหน้าผู้คน** drops to the verb-form. Internally-consistent.

---

## 13. χαίρειν → χαρά keyword bridge at 1:1 → 1:2 — **STABLE (James-distinctive rhetorical structure)**

JAS 1:1's epistolary-greeting **χαίρειν** is rendered **ขอความชื่นชมยินดีจงมีแก่ท่าน** (literal "rejoice-greeting" preserved rather than collapsed to a generic "สวัสดี" or "เรียนสมาชิกใน...").

The 1:1 KD names the rationale:

> "Render preserves the literal-rejoice content rather than collapsing to a generic 'สวัสดี' — the χαρ-stem will recur immediately in v.2 πᾶσαν χαρὰν as the keyword-link James uses to bridge greeting + main-content (per uW Translation Issues note on key-word transitions)."

The bridge to 1:2 **πᾶσαν χαρὰν ἡγήσασθε → จงถือว่าเป็นความชื่นชมยินดีอย่างยิ่ง** preserves the keyword-link **ความชื่นชมยินดี** across the χαίρειν → χαρά shift. James's distinctive rhetorical-construction (greet-with-joy → consider-trials-as-joy) reads cleanly in Thai.

**Editorial assessment:** This is a James-distinctive feature — the χαίρειν epistolary-greeting is rare in the NT (only also at ACT 15:23 + ACT 23:26). The Thai **ขอความชื่นชมยินดีจงมีแก่ท่าน** is principled and cross-references the same lemma at ACT 15:23 (which is itself a letter-quote from James-the-Jerusalem-leader, suggesting authorial-fingerprint consistency). The rhetorical-bridge preservation is a translation-craft achievement worth flagging — and worth a brief corpus-doc lift IF 1 Pet 1:6+ joy-cluster reactivates the χαρ-stem at scale.

**STABLE — recommend optional brief doc** `docs/translator_decisions/jacobean_chairein_chara_bridge_2026-05.md` (low priority; one-line cross-reference would suffice).

---

## 14. τέλειος cluster (1:4, 1:17, 1:25, 3:2) — **STABLE**

τέλειος occurs **5×** in James (most-dense per chapter in the NT), spanning:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:4 | ἔργον τέλειον ἐχέτω, ἵνα ἦτε τέλειοι καὶ ὁλόκληροι | **ทำงานของตนให้สมบูรณ์ ... ผู้เติบโตเต็มที่และครบบริบูรณ์** | mature/complete |
| 1:17 | πᾶσα δόσις ἀγαθὴ καὶ πᾶν δώρημα τέλειον | **ของขวัญอันสมบูรณ์ทุกประการ** | perfect (gift) |
| 1:25 | νόμον τέλειον τὸν τῆς ἐλευθερίας | **ธρρρμบัญญัติอันสมบูρρณ์** | perfect (law) |
| 3:2 | οὗτος τέλειος ἀνήρ | **ผู้นั้นก็เป็นคนสมบูรณ์** | mature/perfect (person) |

**Editorial assessment:** Single-rendering **สมบูรณ์ / ครบบริบูรณ์** across the τέลειος cluster. The 1:4 doublet τέลειοι καὶ ὁλόκληροι is rendered with a complementary-pair (**ผู้เติบโตเต็มที่ + ครบบριบูรณ์**) that preserves the doublet-rhythm. James's wisdom-vocabulary "perfect/complete/mature" thread — closer to Stoic/Hellenistic-Jewish wisdom than to Pauline-eschatological τέลειος (cf. 1 Cor 13:10 the eschatological-τέลειος).

**STABLE** — verse-level rationale comprehensive. No new doc needed; future reference for the General Epistles (Heb 5:14, 1 Pet 5:10).

---

## 15. ταπεινός / ταπεινόω cluster (1:9, 1:10, 4:6, 4:10) — **STABLE / LOCKED**

| Verse | Greek | Thai |
|---|---|---|
| 1:9 | ὁ ἀδελφὸς ὁ ταπεινός | **พี่น้องที่ตกต่ำ** |
| 1:10 | ὁ δὲ πλούσιος ἐν τῇ ταπεινώσει αὐτοῦ | **ส่วนคนรวย ... ในฐานะอันต่ำต้อยของตน** |
| 4:6 | ταπεινοῖς δὲ δίδωσιν χάριν | **ทรงประทานพระคุณแก่คนถ่อมใจ** |
| 4:10 | ταπεινώθητε ἐνώπιον κυρίου, καὶ ὑψώσει ὑμᾶς | **จงถ่อมตนเฉพาะพระพักตร์ขององค์พระผู้เป็นเจ้า และพระองค์จะทรงยกท่านขึ้น** |

**Editorial assessment:** Three-fold semantic-distinction preserved in Thai:
- **ตกต่ำ / ต่ำต้อย** (status-low: socially-low position; 1:9–10)
- **ถ่อมใจ** (humble-disposition: the inner-virtue; 4:6 quoting Prov 3:34 LXX)
- **ถ่อมตน** (humble-action: the imperative-action; 4:10)

The 4:6 **ทรงประทานพระคุณแก่คนถ่อมใจ** matches **1 Pet 5:5** exactly — both letters cite Prov 3:34 LXX with **θεός** substituted for κύριος. Strong corpus-internal consistency for the locked-formula. **STABLE — no new doc needed.**

---

## 16. Inherited corpus-locks — **all compliant**

| Doc | JAS evidence | Status |
|---|---|---|
| `parousia_christou_2026-05.md` | 5:7, 5:8 → **การเสด็จมา** uniform (Christ-subject, royal). | **LOCKED** (see §11) |
| `ekklesia_2026-04.md` | 5:14 (πρεσβυτέρους τῆς ἐκκλησίας → **ผู้ปกครองของคริสตจักร**) — uniform with Pastorals. | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | JAS has **12 narrator/character κύριος references** (1:1, 1:7, 2:1, 3:9, 4:10, 4:15, 5:7, 5:8, 5:10, 5:11, 5:14, 5:15) — all → **องค์พระผู้เป็นเจ้า** with the κύριος Σαβαώθ (5:4) extension to **องค์พระผู้เป็นเจ้าจอมโยธา** (see §4). Compliant with the lock. **Doc-amendment-needed** (already noted in JHN + GAL + 1TH audits) — this is the FIFTH independent corpus confirming the pattern beyond Lukan-Acts. | **LOCKED-with-amendment-needed** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | ψυχή at 1:21 (σῶσαι τὰς ψυχὰς → **ช่วยจิตวิญญาณ ... ให้รอด**); 5:20 (σώσει ψυχὴν αὐτοῦ ἐκ θανάτου → **ช่วยจิตวิญญาณของเขาจากความตาย**) → **จิตวิญญาณ** uniform per the lock. πνεῦμα at 4:5 — see §8 for the contested rendering (the locked **จิต** is NOT used because the verse's πνεῦμα is the Spirit-causing-to-dwell, not the anthropological lemma). The 2:26 σῶμα χωρὶς πνεύματος → **ร่างกายที่ปราศจากวิญญาณ** uses **วิญญาณ** for human-spirit-as-life-principle (sense (b) of the doc — the human-spirit). Compliant. | **LOCKED** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in James (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | N/A — no doxological praise-verb-with-God-object constructions. (3:9 εὐλογοῦμεν τὸν κύριον "we bless the Lord" → **เราอวยพรองค์พระผู้เป็นเจ้า** uses **อวยพร** which matches the EUL-with-God-object Synoptic pattern; flagged as worth-verifying.) | **LOCKED-with-verification** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for human authorities + the apostle's-self-portrait (1:1 ยากอบ ผู้รับใช้). Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A** — no Aramaic embeds in James. (The Σαβαώθ at 5:4 is Hebrew-loanword, not Aramaic; covered by the recommended new κύριος Σαβαώθ doc — see §4.) | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** — no Tier 1/2/3 inclusion variants in James (no `output/textual_variants/james*` files; full text-scan confirmed). One verse-level **micro-variant** at 4:5 (different LXX-source-text proposals) noted in KD; followed SBLGNT per RULES §0; not requiring inclusion-bracket policy. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — James is wisdom-genre + paraenetic-imperative, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in James. The 1:6 wave-tossed-by-wind simile, 1:10–11 grass-flower simile, 3:3 horse-bridle simile, 3:4 ship-rudder simile, 3:5 forest-fire simile, and 5:7 farmer-waiting-for-rain are similes (transparent-vehicle-imagery), not parables-with-divine-figures. Compliant. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from James. The 4:8–10 turning-language uses ἁγιάζω (4:8 ἁγνίσατε καρδίας → **จงชำระใจ ... ให้บริสุทธิ์**) + ταπεινόω (4:10) — neither is the metanoia-lemma. | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | 5:15 ἀφεθήσεται αὐτῷ → **บาปนั้นก็จะได้รับการอภัย** — uses divine-passive ทำให้ + การอภัย; matches the corpus-locked ἀφίημι/ἄφεσις ρenrenderings. **Note:** glance-check vs. the existing doc — the divine-passive form at JAS 5:15 may be slightly different from the Synoptic ἀφέωνταί σοι αἱ ἁμαρτίαι pattern. Worth verifying alignment. | **LOCKED-with-verification** |
| `pagan_deities_2026-04.md` | N/A — no pagan-deity references in James. The 4:7 "διάβολος" → **มาร** uses the corpus-standard satanic-adversary rendering. | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman titles in James. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from James. | **LOCKED (N/A)** |
| `ethnos_2026-04.md` | N/A — ἔθνος / ἔθνη absent from James. | **LOCKED (N/A)** |
| `johannine_doubled_amen_2026-04.md` | N/A — Johannine-specific. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-adversary-speech-verbs-addressing-divine in James. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | 2:5 (κληρονόμους τῆς βασιλείας → **ทายาทแห่งอาณาจักร**) — consistent with the Synoptic-Acts-Pauline lock. 1 verse only; compliant. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | 5:12 (μήτε τὸν οὐρανὸν → **อ้างฟ้าสวรรค์**) — theological-default ฟ้าสวรรค์; 5:18 (ὁ οὐρανὸς ὑετὸν ἔδωκεν → **ฟ้าสวรรค์ก็ประทานฝน**) — same ฟ้าสวรรค์ for the rain-source. Both compliant. | **LOCKED** |
| `nomos_pauline_2026-05.md` | All 12 JAS occurrences uniform-ธρρρμบัญญัติ. **DECIDE-flag**: the doc's two-rendering split for νόμος-of-X-genitive constructions (→ กฎ) is NOT applied to James. See §2 above. | **DECIDE** |
| `dikaioo_dikaiosyne_family_2026-05.md` | 2:21, 2:24, 2:25 use **นับว่าชอบธรรม** (per pre-2026-05-01 corpus-precedent); the 2026-05-01 lock to **ประกาศว่าชอบธรรม** is NOT applied to James. **DECIDE-flag**: see §1 above. The cognate δίκαιος at 5:6 is rendered **ผู้ชอบธรรม** which IS the corpus-standard for δίκαιος-as-noun (REVIEW; see §10). The δικαιοσύνη at 1:20 + 3:18 → **ความชอบธรรม** matches the lock. | **DECIDE** |
| `epiphaneia_christou_2026-05.md` | N/A — ἐπιφάνεια absent from James. | **LOCKED (N/A)** |
| (All other Pauline-corpus docs: `huiothesia_adoption`, `christ_hymn_kenosis`, `pistis_christou`, `prototokos_pauline`, `phroneo_pauline`, `pastoral_corpus_locks`, `hygiaino_sound_doctrine`, `diakonos_pauline`, `sarx_pauline`, `stoicheia_tou_kosmou`, `telos_paidagogos_christ`, `spiritual_beings_hierarchy`, `huiothesia_adoption`, `parousia_christou`, `proper_noun_wordplay`, `porneia_vs_moicheia_DEFERRED`, `adversary_speech_register`, `honorifics_non_divine_authorities`, `ekklesia_2026-04`) | All N/A or compliant in James — see verse-level checks above. | **LOCKED (N/A)** |

---

## 17. OT echoes / allusions — Pauline-style density (3 explicit citations + ~6 echoes)

| JAS | OT source | Status |
|---|---|---|
| 2:8 | LEV 19:18 LXX (Ἀγαπήσεις τὸν πλησίον σου ὡς σεαυτόν) | **LOGGED** — direct citation; DB entry in `data/nt_ot_citations.json` |
| 2:11 | EXO 20:13–14 / DEU 5:17–18 (Decalogue: do-not-murder + do-not-commit-adultery) | **LOGGED** — direct citation |
| 2:23 | GEN 15:6 LXX (Ἀβραὰμ ἐπίστευσεν τῷ θεῷ καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην) | **LOGGED** — direct citation |
| 4:6 | PROV 3:34 LXX (κύριος ὑπερηφάνοις ἀντιτάσσεται, ταπεινοῖς δὲ δίδωσιν χάριν) — James + 1 Pet 5:5 both substitute θεός for κύριος | **LOGGED** — direct citation |

**Additional unflagged echoes:**

| JAS | Echoed text | Notes |
|---|---|---|
| 2:21 | GEN 22:1–19 (Aqedah / binding-of-Isaac) | KD acknowledges the OT-allusion; DB entry recommended |
| 2:25 | JOS 2:1–21 (Rahab-and-the-spies) | KD acknowledges; DB entry recommended |
| 4:5 | OT-prophetic-jealousy general (cf. EXO 20:5, DEU 4:24) | KD: "James paraphrases the general OT-Scripture-teaching about God's jealousy"; not a single-source quote |
| 5:4 | DEU 24:14–15 + LEV 19:13 + MAL 3:5 + ISA 5:9 LXX (κύριος Σαβαώθ context) | Composite echo logged in KD + DB |
| 5:11 | Job (entire-book) + EXO 34:6 / PSA 102:8 LXX (compassionate-and-merciful divine-attribute formula) | DB entries recorded |
| 5:17 | 1 KGS 17:1 + 18:1 (Elijah's three-and-a-half-year drought) | Implicit OT-narrative reference; not formally cited |
| 5:20 | PROV 10:12 LXX (love-covers-sins) — same OT echo at 1 Pet 4:8 | KD acknowledges; DB entry recorded |
| 1:10–11 | ISA 40:6–8 LXX (grass-and-flower wither imagery) | KD acknowledges; not formally cited |
| 5:5 | JER 12:3 / 25:34 LXX (slaughter-day imagery for the wicked) | KD acknowledges; not formally cited |

**Recommend (low priority):** Add the 5 unflagged echoes (Aqedah, Rahab, Isa 40:6–8, Jer 12:3 / 25:34, 1 Kgs 17–18) to `data/nt_ot_citations.json` as `type: "allusion"` or `type: "thematic_echo"` entries. Not blocking; verse-level KDs already capture the rationale.

---

## 18. Mechanical (§1) — **all green**

- 5/5 chapters: `output/check_reports/james_NN_review.md` ✓ (all 9 sub-checks clean — key-term consistency, TNBT structural, OT citations, Synoptic parallels, BT, summary coverage, claim consistency, Greek-field integrity, phrase consistency)
- 5/5 chapters: `output/back_translations/james_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only the verification re-run artifact (`key_term_consistency_all.md` modified by my §1 verification re-run). No JAS source-file dirt. Untracked SFM files in `output/paratext/` are pre-existing for prior books (1CO, 1TH, 2CO, 2TH, ACT, COL, EPH, GAL, TIT) — unrelated to JAS.

---

## Pre-existing docs affirmed / unchanged

All 43 docs in `docs/translator_decisions/` reviewed. Compliance summary in §16 above. The **Lukan-Acts narrator-κύριος doc** flagged for amendment — JHN, GAL, 1TH, 2TH, PHP audits already noted; James provides the FIFTH independent confirmation; the doc's "Lukan signature" framing should be renamed/extended to acknowledge corpus-wide narrator-κύριος usage. The **dikaioo + nomos Pauline locks** are flagged DECIDE for non-Pauline-James-application (§1, §2).

---

## Flagged for Ben's attention

### A. δικαιόω in James 2:21/24/25 — **DECIDE** (§1)
The current Thai (**ทรงนับว่าชอบธรรม / ได้รับการนับว่าชอบธรรม**) does NOT match the locked Pauline forensic-declarative rendering (**ทรงถูกประกาศว่าชอบธรรม**). Three options: apply the Pauline lock to James (Option A); document non-Pauline-James as principled exception (Option B); or hybrid relock with verse-Notes (Option C). **External AI review packet carries this as Item A.**

### B. νόμος uniform-ธρρρμ across all 12 JAS occurrences — **DECIDE** (§2)
The current uniform **ธρρρμบัญญัติ** rendering does NOT split per the locked Pauline two-rendering policy (ธρρρμ for Mosaic-Torah / กฎ for νόμος-of-X-principle). Three options: apply Pauline split to James (Option A); document James-monolithic as principled exception (Option B); or hybrid with new corpus-doc `nomos_jacobean_2026-05.md` (Option C — pre-recommended). **External AI review packet carries this as Item B.**

### C. πειρασμός lemma-ambiguity preserved — **REVIEW** (§5)
Confirm with Ben that the deliberate single-Thai-rendering policy (ทดลอง / การทดลอง for both trial and temptation senses across JAS 1:2–15) is the right call vs. a two-rendering split. The wordplay is theologically-load-bearing.

### D. βασιλικὸς νόμος at 2:8 — **REVIEW** (§6)
Confirm **ธρρρμบัญญัติแห่งพระมหากษัตริย์** is the right interpretive commitment. The current rendering picks the "law-given-by-the-divine-king" reading; alternatives include "supreme/preeminent law" or "kingdom-of-God's law" (Christological).

### E. φιλία τοῦ κόσμου + μοιχαλίδες explicit "พระเจ้า" disambiguation — **REVIEW** (§7)
Confirm the explicit "ผู้นอกใจ**พระเจ้า**" disambiguation at 4:4 is the right call (the OT-prophetic-marriage-metaphor for unfaithfulness-to-God). Trade-off: Thai-reader access vs. metaphor-richness.

### F. πνεῦμα at 4:5 — **REVIEW** (§8)
Confirm the current Thai locks reading (i)+(b)+(α) — "the human-spirit-that-God-caused-to-dwell-in-us yearns with [evil] envy" (NIV-aligned). Alternatives: ESV (ii)+(b)+(β) "He yearns jealously over the spirit ..."; NASB (ii)+(a)+(β) "He jealously desires the [Holy] Spirit ..."

### G. anointing-with-oil at 5:14 — **REVIEW** (§9)
Confirm **เจิมด้วยน้ำมัน** preserves both sacramental and medicinal readings (which it does well). Sub-question: should σώσει τὸν κάμνοντα (5:15) → **ช่วยผู้ป่วยให้หาย** (physical-healing) be paired with a verse-level clarification that the spiritual-healing reading is also live?

### H. δίκαιος at 5:6 — **REVIEW** (§10)
Confirm the generic-righteous-person reading (**ผู้ชอบธรรม**) vs. the Christological "Righteous One" reading (**องค์ผู้ชอบธรรม** — would parallel the corpus pattern at ACT 3:14, 7:52, 22:14).

### I. New corpus docs to write (before 1 Peter / 2 Peter / Jude / Hebrews)
1. **`docs/translator_decisions/sophia_anothen_2026-05.md`** (§3) — locks σοφία ἄνωθεν cluster + JAS 3:17 7-fold list
2. **`docs/translator_decisions/kyrios_sabaoth_2026-05.md`** (§4) — locks κύριος Σαβαώθ → **องค์พระผู้เป็นเจ้าจอมโยθา** before Rom 9:29 + Heb 12:21–22
3. **(Conditional on Item B Option C)** `docs/translator_decisions/nomos_jacobean_2026-05.md` — explicitly distinguishes James's monolithic-Mosaic νόμος from Paul's rhetorical-multivalent νόμος
4. **(Optional)** `docs/translator_decisions/jacobean_chairein_chara_bridge_2026-05.md` (§13) — locks the χαίρειν → χαρά keyword-bridge rendering policy

### J. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to acknowledge corpus-wide narrator/character-κύριος usage (Lukan-Acts + Johannine + Pauline + General-Epistle confirmation; James is the fifth independent confirmation).
- **`dikaioo_dikaiosyne_family_2026-05.md`** — add an explicit James-scope sub-section based on Item A's resolution. Either: extends the lock to include James (Option A), or documents the principled non-Pauline-James exception (Option B).
- **`nomos_pauline_2026-05.md`** — add an explicit James-scope sub-section based on Item B's resolution. Either: extends the two-rendering split to include James (Option A), or documents the James-monolithic-Mosaic principled exception (Option B), or cross-references the new `nomos_jacobean_2026-05.md` (Option C).

### K. External AI review (§3 of checklist) — **ready**
Packet built at `docs/end_of_book/james/external_review_packet_JAS_2026-05-03.md`. Items: A (δικαιόω/James), B (νόμος/James), C (πειρασμός lemma-ambiguity), D (βασιλικὸς νόμος), E (φιλία+μοιχαλίδες), F (πνεῦμα 4:5), G (anointing-oil), H (δίκαιος 5:6). Use Grok + ChatGPT in parallel per the JHN/GAL/PHP/1TH pattern; cross-check verse-claims against the JSONs (AIs occasionally hallucinate verse content).

---

## Recommendation

**James ships in strong corpus-hygiene shape — and is the corpus's first major test of whether Pauline-corpus locks should extend to non-Pauline epistles.** The translator made consistent, principled choices on the James-distinctive lemma-clusters (σοφία ἄνωθεν, κύριος Σαβαώθ, πειρασμός lemma-ambiguity, χαίρειν-χαρά bridge, τέλειος cluster, ταπεινός cluster) — none of which has a corpus-doc yet. The two DECIDE items (δικαιόω scope, νόμος scope) are **bookkeeping questions about lock-application boundaries**, not translation-quality questions: the current James renderings are defensible; the question is whether they should match the Pauline corpus or be principled exceptions.

Tag `book-james-v1` after:
1. Ben's decisions on **§A + §B** (DECIDE items: δικαιόω scope; νόμος scope) — these are the only blocking items
2. Ben's confirmation on **§C–§H** (REVIEW items: πειρασμός lemma-ambiguity; βασιλικὸς νόμος; μοιχαλίδες disambiguation; πνεῦμα 4:5; anointing-oil; δίκαιος 5:6)
3. Two new translator_decisions docs written (§I items 1–2 minimum: σοφία ἄνωθεν + κύριος Σαβαώθ); optionally items 3–4
4. Existing docs amended (§J: narrator-κύριος doc; dikaioo doc; nomos doc per the §A + §B resolutions)
5. External AI sanity-check (§K)

The General Epistles forward-queue (1 Pet, 2 Pet, Jude — and then Hebrews + Revelation) will benefit from the σοφία-ἄνωθεν + κύριος-Σαβαώθ docs and from the explicit James-scope-resolutions on the dikaioo and nomos locks. Better to make these decisions before James ships v1 than to incur drift across four more General Epistles.
