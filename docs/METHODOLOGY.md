# Eremos Translation — Methodology

A technical account of how this translation was produced, checked, and reviewed,
written for readers who evaluate translations professionally: consultants,
biblical-studies scholars, Bible society staff, and seminary-trained pastors.
A plain-language companion lives at [METHODOLOGY_PLAIN.md](METHODOLOGY_PLAIN.md).

**What this is:** a complete first-draft translation of the Protestant Bible
(66 books) from the original Hebrew and Greek into modern Thai, produced by one
maintainer working with a frontier AI model inside a mechanically-gated
pipeline, released into the public domain (CC0), and now in its human-review
phase. Every verse carries a documented audit trail. Nothing here claims the
work of a translation committee; the claim is different — that a disciplined
AI-assisted process with total provenance transparency can produce a serious
draft, and that the draft's openness (open license, open process, open audit
trail) is precisely what makes rigorous human review possible.

**Status in one sentence:** drafting and machine/AI review layers are complete;
native-speaker and theological review is the current phase, and the first Thai
reviewers are being recruited now. No book is called finished until Thai
reviewers have read it.

---

## 1. At a glance

| Dimension | Value |
|---|---|
| Canon | 66 books, 1,189 chapters (Protestant; 27-book NT, no deuterocanon) |
| Verses | 31,155 in source numbering (MT for OT, SBLGNT for NT); 31,086 in English numbering (app + reader site); the 69-verse delta is fully reconciled — see §7 |
| Source texts | SBLGNT + MACULA Greek (NT); Westminster Leningrad Codex via OSHB + MACULA Hebrew (OT) |
| Translation philosophy | Optimal equivalence (BSB-family), SIL/Larson four-pillars |
| License | CC0 1.0 Universal (public domain) — text, notes, tooling |
| Key-term ledger | 19,265 glossary entries (`glossary.json`) |
| NT→OT citation registry | 1,570 recorded links (`data/nt_ot_citations.json`) |
| Back-translations | 1,189 chapters — 100% coverage, ship-blocking |
| Textual-variant records | 843 per-chapter files (`output/textual_variants/`) |
| Mechanical checks | 18 per-chapter check scripts (9-step NT cadence, 7-step OT cadence) plus a corpus-audit, polish, and drift-discovery suite |
| Translator-decision documents | 97 (`docs/translator_decisions/`) |
| End-of-book audits | 66 of 66 books |
| External AI review responses | 66 of 66 books (independent models — see §6.3) |
| Corpus-wide audits | NT v1 (2026-05-04) · OT v1 (2026-06-27) · whole-Bible cross-book (2026-06-27, adjudication pending — see §8) |
| Distribution | Eremos app (iOS/Android/web) · bible.eremosapp.com · USFM 3 export, all 66 books · Google Docs reader sync |

Timeline, stated plainly because a professional reader will ask: the pilot
chapters (Mark 1; 1 Timothy 3) and the governing RULES.md date to mid-April
2026; the whole-Bible draft with per-book audits was complete by 27 June 2026;
the English-numbered edition shipped to the app on 1 July 2026. That speed is
the point of the method — the AI made the fast part fast so that the slow,
human part (§9) starts from a complete, fully-documented corpus rather than a
partial one.

---

## 2. Confessional position

Eremos Translation is **evangelical Protestant** (RULES.md §0). Text-critical
base: SBLGNT — the same Alexandrian-leaning critical-text family as the ESV,
NIV, NASB, CSB, and BSB. On contested verses the project follows the modern
evangelical critical-text consensus; where SBLGNT and NA28 disagree, SBLGNT is
followed and the divergence documented. CC0 licensing means anyone of any
tradition may use the text, but editorial decisions are not doctrinally
neutral, and verse notes describe textual, linguistic, and cultural facts
rather than endorsing frameworks of other traditions.

## 3. Translation philosophy

**Optimal equivalence** (RULES.md §1): faithful to the grammar, syntax, and
semantic range of the source AND natural in modern Thai — the BSB's approach,
applied to Thai. The four SIL/Larson pillars govern: accuracy, clarity,
naturalness, acceptability. When pillars conflict, accuracy wins and the
naturalness tradeoff is documented in the verse record.

Register follows Thai Scripture convention (RULES.md §3): divine subjects take
ราชาศัพท์ (royal register — ทรง/เสด็จ/ตรัส/พระหัตถ์); humans addressing God use
humble register; demons and adversaries never receive honorifics; inter-human
dialogue matches social relationship. The OT extends this with a five-register
voice policy and an explicit Rachasap policy for human kings
(`docs/translator_decisions/ot_register_policy_2026-05.md`) — e.g. the
foreign-monarch register question (Pharaoh, Nebuchadnezzar, Cyrus) is a live
cross-book adjudication item (§8).

## 4. Source texts, isolation discipline, and licensing

Full inventory with licenses: [ATTRIBUTIONS.md](../ATTRIBUTIONS.md). The
authoritative per-source policy is
[source_license_policy.md](source_license_policy.md), which assigns every
source one of five roles: `primary_text`, `morphology_data`, `consult_only`,
`do_not_copy`, `proprietary_reference`.

**Primary sources (verbatim use permitted):**

- NT: **SBLGNT** (CC BY 4.0) with **MACULA Greek** morphology, syntax trees,
  and Louw-Nida semantic domains (CC BY 4.0)
- OT: **Westminster Leningrad Codex** via OSHB/morphhb (CC BY 4.0; underlying
  WLC public domain) with **MACULA Hebrew** morphology and clausal syntax
  (CC BY 4.0)
- English sanity reference: **Berean Standard Bible** (CC0) — read as a check,
  never copied from

**The isolation rule** (RULES.md §2, §8, §10): during drafting the model may
read only the original-language text with morphology, the project's own rules
and glossary, its own prior output, and unfoldingWord's English scholarly notes
(CC-BY-SA, consulted but never copied). It may **never** read any Thai
translation during drafting — not copyrighted Thai versions, and not even the
open-licensed TNBT. This is the project's independent-creation discipline: the
Thai wording is produced by direct analysis of the public-domain originals, so
no other translation's wording can enter the draft. Post-draft, the TNBT
(CC-BY-SA) is compared **structurally and mechanically only**
(`check_against_tnbt.py`) — sentence-count and length signals, with vocabulary
divergence expected and unremarkable.

**License hygiene worth naming:** the Septuagint has no clean public-domain
digital encoding, so the project deliberately operates without an LXX text
source in the repo — LXX comparison flows through MACULA Hebrew's inline
lemma-level Greek equivalents, and LXX/MT divergences are hand-curated
(`source_license_policy.md` §3). GPL-encoded and ShareAlike-encoded datasets
are refused entry even when convenient. The stated legal test for
`consult_only` sources: a CC0 reuser replacing our Thai with their own reading
of the Hebrew should arrive at substantially different wording; if they would
arrive at ours because we tracked a source line by line, we have leaked.

**The CC0 promise** (§6 of the policy): downstream users may reuse the
translation with no attribution and no license propagation, and can trust that
no part of the Thai text was lifted from a re-encumbering source.

## 5. The drafting process (per chapter)

Documented end-to-end in [TRANSLATION_WORKFLOW.md](TRANSLATION_WORKFLOW.md).

1. **Extraction** — `extract_book.py` / `extract_book_hebrew.py` produce a
   per-chapter JSON with word-by-word morphology, hapax flags, semantic
   domains, and the BSB reference text.
2. **Scholarly context** — `enrich_with_uw.py` fetches unfoldingWord
   Translation Notes: the book introduction (read first — author, audience,
   themes, known translation issues; standard SIL practice) and the
   chapter-level notes on interpretive cruxes.
3. **Drafting** — a fresh maximum-capability Claude session per chapter (clean
   context; RULES.md and the glossary loaded; the nearest prior chapter read
   for stylistic continuity) translates from the Greek/Hebrew. Every verse
   must record its interpretive surface (RULES.md §6): the Thai rendering, an
   optional literal alternative, an optional reader-facing Thai summary,
   `key_decisions` (Greek/Hebrew phrase → Thai choice → rationale), and
   `notes` covering textual variants, hapax legomena, OT citations, and
   polysemy calls. Schema completeness is mechanically enforced.
4. **Back-translation** — the same session writes a literal English
   back-translation of every verse to a separate file. A chapter cannot ship
   without one (hard gate since 2026-04-19).

What must always be flagged per verse (RULES.md §5): hapax legomena with
rationale; textual variants where SBLGNT diverges from Byzantine/BSB choices;
polysemous sense selections; OT citations and allusions (each registered in
`data/nt_ot_citations.json` — the checker fails ship if a note claims a
citation the registry lacks); gendered or scholarly-contested language;
technical and cultural terms without direct Thai equivalents.

## 6. Quality assurance

### 6.1 Per-chapter mechanical cadence

`run_checks.py` runs a language-routed cadence — 9 steps NT, 7 steps OT —
producing an aggregate report per chapter; `ship_chapter.sh` refuses to commit
on any failure. The gate is mechanical, not honor-system. Highlights:

| Check | What it catches |
|---|---|
| Back-translation diff | Undocumented divergence between the Thai (via literal back-translation) and the BSB rendering of the same source |
| Key-term consistency | A Greek lemma drifting across multiple Thai renderings without documented contextual rationale |
| Phrase consistency | Multi-word locked phrases (e.g. ἄφεσις ἁμαρτιῶν) rendered inconsistently — added after a drift the per-lemma check could not see |
| OT-citation acknowledgment | NT verses that quote the OT without registry entry, and note-vs-registry drift |
| Synoptic parallels | The same saying rendered differently across Gospels without cause (`data/synoptic_parallels.json`) |
| TNBT structural comparison | Sentence-count/length anomalies against the only open-licensed Thai NT (structure only; vocabulary divergence expected) |
| Greek/Hebrew field integrity | Fabricated or script-polluted source-language tokens in the decision records (a failure mode all other checks passed green on when it first occurred) |
| Claim consistency | "Pipeline hypocrisy": a note claiming a side-effect ("added to glossary", "registered citation") whose artifact doesn't exist |
| Divine names (OT) | Any deviation from the Tetragrammaton policy (§7 below) |
| Honorifics binding (OT) | Royal-register noun and verb layers applied incorrectly to divine subjects |
| Versification anchor (OT) | Verse-numbering drift at the ~23 MT/English seams |
| Proper-noun locks | Known-rejected transliteration surface forms (hard-fail) |
| Sacrificial vocabulary (OT) | Drift across the five Levitical offering-type nouns |
| Ketib/Qere · LXX/MT | Masoretic variant sites surfaced for review (policy: translate the Qere; translate MT, document LXX-only material) |

A deliberate design fact a professional reader should note: **several checks
were written in response to caught incidents**, and the incident reports are in
the repo (e.g. `docs/LUKE_DRIFT_2026-04-21.md`;
`docs/end_of_book/inclusion_variant_gap_2026-05-02.md`). The QA suite is not a
static checklist but a ratchet — each observed failure mode became a permanent
mechanical gate. A three-iteration revision loop (`revise_chapter.py`)
escalates any chapter that cannot pass its checks to human review.

### 6.2 End-of-book audit

When a book's last chapter ships, an audit runs before the book may be tagged
([END_OF_BOOK_CHECKLIST.md](END_OF_BOOK_CHECKLIST.md)): the mechanical gate
book-wide (including the strict inclusion-variant audit, §7), an editorial
review by a fresh AI session producing a per-book audit document with a
LOCKED / STABLE / REVIEW / DECIDE status per translation decision, and the
external review packet (§6.3). Corpus-level rollup across the 66 per-book
audits: 1,756 decisions LOCKED, 1,020 STABLE, 947 REVIEW, 781 DECIDE (counts
are heuristic; the per-book documents in `docs/end_of_book/` are the
decision-grade record). REVIEW and DECIDE items are exactly the material now
being routed to human reviewers.

### 6.3 Independent AI cross-examination

Every book's audit produces a review packet that is put to **AI models from
other vendors** (Gemini, ChatGPT/Grok) — deliberately not Claude, because
Claude reviewing Claude shares the same blind spots. Responses are then
verified claim-by-claim against the actual verse files (external models
hallucinate; the cross-check catches it), and surviving findings become
dispositions: keep-with-documentation, new decision doc, or a flagged edit for
the maintainer's sign-off. All 66 books have external responses on file. This
layer has caught real corpus-level questions per-chapter checks structurally
cannot see (the ἐκκλησία rendering question across Matthew 16/18 and Acts is
the canonical example — it triggered the creation of the end-of-book audit
itself).

### 6.4 Corpus-wide audits and the polish layer

Three consolidation audits sit above the per-book layer: **NT v1**
(2026-05-04), **OT v1** (2026-06-27), and the **whole-Bible cross-book audit**
(2026-06-27) — the layer that looks for what no per-book process can see
(§8). A separate polish suite (`polish_review.py`,
`polish_optimal_equivalence.py`) scans for micro-readability and
semantic-rigidity issues; it proposes, never auto-applies — edits require an
explicit approval decision per proposal, and approved deltas re-run the
corpus regression checks.

## 7. Text-critical and versification policy

**Inclusion variants** (RULES.md §5): where SBLGNT's main text omits material
that other manuscript traditions include, a three-tier policy matches
mainstream critical-text English practice (BSB/ESV/NIV/CSB): short contested
phrases print in single brackets […] in the main text; whole verses SBLGNT
omits move to a chapter-footer manuscript note (with witnesses and a Thai
explanation); the two large blocks (Mark 16:9–20; John 7:53–8:11) print in
⟦double brackets⟧ with extended notes. Every candidate surfaced by
`audit_inclusion_variants.py --strict` must carry an explicit disposition
before a book locks — a gate added after two early silent omissions (Romans
16:25–27; John 5:4) were caught, written up, and made structurally impossible
to repeat. The Luke 24 Western non-interpolations are enumerated and
dispositioned individually (RULES.md §5).

**Divine names (OT):** locked policy
(`docs/translator_decisions/divine_names_table_2026-05.md`): יהוה →
องค์พระผู้เป็นเจ้า (aligning with the NT's κύριος rendering); YHWH Ṣebaoth →
องค์พระผู้เป็นเจ้าจอมโยธา; standalone Adonai distinguished; place-name
compounds transliterate ยาห์เวห์-X. Mechanically enforced by
`check_divine_names.py` on every OT chapter.

**Versification:** the source corpus is anchored to the original-language
numbering (MT for OT — Joel has 4 chapters, Malachi 3, Psalm superscriptions
are verses); the app and reader site present standard English/BSB numbering.
A single conversion module (`versification_english.py`) owns the mapping so
the two surfaces cannot drift. The 69-verse count difference between the two
numbering schemes is item-by-item reconciled in
[PARATEXT_EXPORT_2026-08-02.md](PARATEXT_EXPORT_2026-08-02.md) — 66 verses of
Psalm superscriptions plus six MT/SBLGNT one-verse offsets, minus three
English-side merges — and content equality between surfaces was verified
character-for-character on 2026-08-02.

**Typeset structure** (headings, paragraphing, poetry indentation, Selah,
Psalm 119's acrostic letters) is a purely additive layer derived from the
public-domain BSB section apparatus ([STRUCTURE_LAYER.md](STRUCTURE_LAYER.md));
Thai headings are the project's own editorial translation and are explicitly
marked draft pending native review. No copyrighted heading set is used.

## 8. Known limitations and open work

Stated here because a serious reader will find them anyway, and should find
them stated by us first:

1. **Native-speaker review coverage is the project's current gap and current
   phase.** The review corpus (§9) is machine- and AI-verified, not yet
   naturalness-verified by a body of Thai readers. Recruiting is active;
   review tooling is live.
2. **Eight cross-book consistency themes await maintainer adjudication**
   ([WHOLE_BIBLE_CROSSBOOK_AUDIT_2026-06-27.md](WHOLE_BIBLE_CROSSBOOK_AUDIT_2026-06-27.md)):
   divine-anthropomorphism register; מַלְאָךְ messenger/angel renderings;
   the Adonai-YHWH compound's uniform application; reader-facing footnotes
   for MT/LXX and Ketib/Qere divergences; OT↔NT quotation seams (e.g. "den
   of robbers" in Jeremiah 7:11 vs Matthew 21:13); foreign-monarch register;
   parallel-passage harmonization policy; notes voice. Decisions will be
   recorded, then enforced by checks written for the purpose (decide → check
   → apply → ship).
3. **A Hebrew-lemma consistency checker does not yet exist** — the key-term
   checker is Greek-keyed; OT lemma-level drift is currently covered only by
   the Thai-surface phrase checker, the decision-doc verification workflow,
   and the audits.
4. **Some versification-seam verses carry null metadata sub-objects**
   (pre-dating the schema) — non-blocking, hand-patch backfill planned.
5. **Community comprehension testing** (the third social step RULES.md §9
   names) has not begun; it follows reviewer recruitment.
6. **One maintainer.** The bus-factor mitigation is the repo itself: rules,
   decisions, audit trail, and tooling are all public and reproducible.

## 9. Human review — who and how

The division of labor is documented in [WHO_DOES_WHAT.md](../WHO_DOES_WHAT.md):
one maintainer runs the pipeline; reviewers review. Reviewer roles: native
speakers (naturalness — "the single most valuable thing this project needs"),
careful readers, pastors/teachers, theological reviewers with original-language
competence, and editors. Review happens through a purpose-built bilingual web
form (eremosapp.com/review) whose question bank is generated from each book's
actual audit findings — reviewers answer real editorial questions, at their own
pace, and answers flow into the editorial record. Reading-based feedback
("here's where it stumbled across a whole book") is equally welcomed through
the app and reader site.

Honestly stated: this project is one missionary maintainer plus an AI pipeline,
with the first Thai reviewers now being recruited. Early feedback from Thai
friends who have read portions has been encouraging; that is not the same
thing as systematic review, which is why the recruiting matters. The gate
framing is the commitment: no book is called finished until Thai reviewers
have read it.

## 10. Integrity and provenance

Git history records every revision to every verse since the pilot.
`HASHES.md` maintains a SHA-256 manifest of all translation files. 97
translator-decision documents record corpus-level policies with their
rationale, each grep-verified against the shipped corpus before locking
([CORPUS_VERIFICATION_WORKFLOW.md](CORPUS_VERIFICATION_WORKFLOW.md)). Every
verse's interpretive reasoning ships with the verse — in the app's scholarly
notes, in this repository, and in the exports.

## 11. Distribution

- **Eremos app** (iOS / Android / web) — daily-use reader with the per-verse
  decision records behind a scholarly-notes toggle
- **bible.eremosapp.com** — typeset reader edition, Thai-first, with the
  structure layer
- **USFM 3** — all 66 books plus `booknames.xml`, Paratext-compatible
  (`output/paratext/`), the channel for eBible.org / DBL-style distribution
- **Google Docs** — reader edition auto-synced for low-friction sharing
- **This repository** — the entire pipeline, checks, decisions, and audit
  trail

Everything is CC0. No permission is needed for any use, including commercial
print. An attribution line is appreciated and never required.
