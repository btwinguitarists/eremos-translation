# Source License Policy

**Status:** Authoritative. Approved 2026-05-04 as Gate 0 for the OT pipeline rollout (per `~/.claude/plans/i-want-you-to-synchronous-stardust.md` §3).

**Purpose.** The Eremos Translation's output is licensed CC0 1.0 Universal (public domain dedication). That commitment can be quietly compromised if (a) ShareAlike (CC-BY-SA) phrasing leaks into our Thai text, (b) we ingest a source whose license requires downstream attribution-with-license-propagation, or (c) we repackage a proprietary/commercial-restricted work without authorization. This policy keeps every external source explicitly classified by role so the curator (Ben) and any future maintainer can decide quickly: *can this material be copied verbatim into Eremos files? May it inform our Thai phrasing? Or is it consult-only?*

This policy supersedes the looser "scholarly sources consulted" section in `ATTRIBUTIONS.md`. `ATTRIBUTIONS.md` continues to record per-source attribution text for redistribution; this doc records the *role* that governs how each source is handled inside the pipeline.

---

## 1. The five license roles

Every external source is tagged with exactly one role.

| Role | Meaning | Permitted use in Eremos |
|---|---|---|
| `primary_text` | Public domain or CC0; can be reproduced verbatim in pipeline outputs | Source `hebrew` / `aramaic` / `greek` field; reader-rendered output; verbatim quotation OK |
| `morphology_data` | Open-license linguistic data, typically CC-BY 4.0; attribution required | Lemma / morph / clausal-alignment fields with attribution preserved in `ATTRIBUTIONS.md` |
| `consult_only` | Open license but ShareAlike (CC-BY-SA) or non-commercial; cannot leak into CC0 outputs | Read for context during drafting; **never copy phrasing** into the `thai` field; flag any incidental similarity for curator review |
| `do_not_copy` | Proprietary or commercial-restricted | Translator may consult mentally via legal access (purchased subscription, library); **nothing committed to repo files** |
| `proprietary_reference` | Paid scholarly tools (HALOT, BHQ, DCH) accessed via personal subscription | Live consult only via Logos/library; **not stored in repo**; cite by short reference in translator notes (academic fair use) |

**Hard rule for `consult_only` sources** (the most common license-leak failure mode): the curator may *learn from* the source, *paraphrase the insight*, and *cite the source by short reference*. The curator may not (a) copy phrases verbatim into a Thai rendering, (b) translate substantial chunks of a `consult_only` source's prose, (c) commit derived files where the wording is closely traceable to the source. The standard legal test: a CC0 reuser who replaces our Thai output with their own reading of the Hebrew should arrive at substantially different wording. If they would arrive at our exact wording because we tracked the `consult_only` source line by line, we have leaked.

---

## 2. Per-source role assignments

### 2.1 New Testament (already in production)

| Source | Role | Notes |
|---|---|---|
| **SBLGNT** | `primary_text` | CC-BY 4.0; published Greek NT base text |
| **MACULA Greek** | `morphology_data` | CC-BY 4.0; clause/morph/Louw-Nida annotations |
| **Berean Standard Bible (BSB) NT** | `primary_text` | CC0 1.0; English bridge translation |
| **uW Translation Notes (en_tn)** | `consult_only` | **CC-BY-SA 4.0; do not copy phrasing into Thai output** |
| **uW Translation Words (en_tw)** | `consult_only` | CC-BY-SA 4.0; same restriction |
| **TNBT (Thai New Buddhist Translation)** | `consult_only` | CC-BY-SA 4.0; structural comparator only via `check_against_tnbt.py` |
| **NA28 / UBS5 apparatus** | `proprietary_reference` | Cited; no text copied |
| **BDAG, Spicq, Lampe** | `proprietary_reference` | Logos library; live consult only |

### 2.2 Old Testament (W1 rollout)

| Source | Role | Notes |
|---|---|---|
| **Westminster Leningrad Codex (WLC) base text** | `primary_text` | Hebrew/Aramaic text is public domain; reproducible verbatim |
| **WLC morphology (WHM) layer** | `morphology_data` | CC-BY 4.0 via openscriptures/morphhb |
| **OSHB (openscriptures Hebrew Bible) lemmas** | `morphology_data` | CC-BY 4.0 |
| **MACULA Hebrew** | `morphology_data` | CC-BY 4.0 via Clear-Bible/macula-hebrew; clause-level discourse annotations |
| **openscriptures Rahlfs LXX (1935 base text only)** | **DEFERRED** — see §3 below | No clean PD digital encoding readily available; deferring to Phase 6 with translator-consult-only access via Logos |
| **BSB OT** | `primary_text` | CC0 1.0; English bridge for OT (already on disk via existing BSB clone) |
| **Strong's Hebrew dictionary (text content)** | `primary_text` (the dictionary content from 1890s is PD) | Strong's numbers H### and lemma forms are inline in MACULA Hebrew; we do not separately ingest the openscriptures `strongs` repo (which is GPL 3.0 encoded — incompatible with our CC0 monorepo). For full Hebrew gloss text, use BDB 1906 (PD) when needed in Phase 6 |
| **JPS 1917 Tanakh (English)** | `consult_only` | Public domain text but treated as English bridge for stylistic comparison only — its quotation register is generally not the model we want to copy |
| **Brenton's English LXX** | `consult_only` | Public domain bridge translation; comparative reading only |
| **uW Translation Notes (OT books)** | `consult_only` | CC-BY-SA 4.0; same hard rule as NT |
| **uW Translation Words (OT books)** | `consult_only` | CC-BY-SA 4.0; same hard rule |
| **uW UHB (Door43 unfoldingWord Hebrew Bible)** | `consult_only` | **CC-BY-SA 4.0 — NOT primary_text despite being a Hebrew text.** uW's publication is ShareAlike; the underlying Hebrew text is public domain via WLC, so we use WLC directly via `morphhb` and treat uW UHB as `consult_only` for any annotations or phrasing |
| **BDB (1906 ed.)** | `consult_only` | Public domain text; the one PD lexicon; we may quote glosses but should paraphrase |
| **HALOT, DCH, TDOT, BHS, BHQ apparatus** | `proprietary_reference` | Logos library; live consult only |
| **Targums, Vulgate, Peshitta, Samaritan Pentateuch** | `consult_only` | Mixed PD/edited; default to consult_only and elevate per-edition only after verifying the specific text used is PD |
| **Dead Sea Scrolls (Tov + Abegg eds.)** | `consult_only` (active comparator for 1–2 Sam, Isaiah, Pentateuch per plan §10) | The DSS text content is from antiquity, but most published editions carry editorial copyright; consult only via legitimate purchase/access |

---

## 3. LXX source decision (revised 2026-05-04 after probe)

**Original decision (in plan):** Use the openscriptures Rahlfs (1935) base text as the LXX `primary_text`.

**Probe finding (2026-05-04):** No clean PD digital encoding of the Rahlfs LXX is readily available on GitHub. The dominant candidates and their licenses:

| Candidate | License | Verdict |
|---|---|---|
| `eliranwong/LXX-Rahlfs-1935` | **CC-BY-NC-SA 4.0** (NonCommercial + ShareAlike, derivative of CCAT) | **Reject** — non-commercial restriction incompatible with CC0 |
| `openscriptures/GreekResources` | Effectively unavailable; explicitly says "the actual text of the Septuagint may be downloaded from the CCAT website" (CCAT EULA) | **Reject** — no LXX text in this repo |
| STEPBible Analytic LXX | Non-commercial / consent-required | **Reject** — incompatible with CC0 |
| Göttingen LXX (critical edition) | Active editorial copyright | `proprietary_reference` only via Logos |

The Rahlfs *text* itself (1935 + 70-year copyright term) **is** in the public domain in most jurisdictions, but every available digital encoding adds either CCAT-EULA, CC-BY-NC-SA, or active editorial copyright on top.

**Revised decision (2026-05-04).** Defer the LXX `primary_text` clone for W1. **Operate without an LXX text source in the repo for now.** Rely on:

- **MACULA Hebrew's `greek` and `greekstrong` inline attributes** (CC-BY 4.0) for word-level LXX equivalents at every Hebrew lemma. These are already cloned and cover the load-bearing case (NT-cited OT verses).
- **MACULA Greek's coverage** for NT-quoted LXX passages (already in the repo for NT use).
- **Translator consults LXX text per-verse via Logos** when the OT chapter being translated has a heavily NT-quoted verse. Notes are paraphrased.

**Open question for Ben (recorded for later resolution).** Two paths to recover an in-repo LXX `primary_text`, in increasing order of effort:

1. **Find / commission a community-encoded PD Rahlfs:** scan SacredTongues / openscriptures community for an unencumbered encoding. If one exists, it can be added later as `primary_text`.
2. **Make a curator-judgment call:** the underlying Rahlfs text is PD; the CCAT EULA may be a download-time access restriction rather than a copyright restriction binding downstream users. This is a legal-judgment call that should be made by the curator after consulting counsel, not by automation. Default for now: assume the EULA binds and reject.

**What this means in practice for W1:**

- No `sources/lxx/` directory created yet.
- LXX comparator data flows through MACULA Hebrew's `greek=` attributes inline.
- `check_lxx_mt_divergence.py` (planned in §9 of the plan) initially operates against MACULA Hebrew's inline LXX equivalents, not against an LXX text source.
- The `data/lxx_mt_divergences.json` file is hand-curated initially from translator notes during pilot; not auto-generated from a paired-text alignment.
- **No STEPBible LXX morphology files commit to the repo, ever.**
- **No Göttingen edition files commit to the repo, ever.**
- Translator consults Göttingen / Rahlfs (via Logos / personal copy) during chapter-level decisions; takes paraphrased notes; does not copy.

This is a *softening* of the plan's first-cut. The CC0-purity benefit (no LXX clone with restrictive licenses creeping into the repo) outweighs the loss of fully-automated MT-LXX comparator coverage. Most of the load-bearing NT-quoted OT verses are still covered via MACULA Hebrew's inline equivalents. The residual gap is a translator-consult task, not a pipeline blocker.

---

## 4. Attribution mechanics

Each new `morphology_data` source gets an entry in `ATTRIBUTIONS.md` with:

- Project name + editor
- License + version (commit hash at acquisition)
- Role assignment (`primary_text` / `morphology_data` / `consult_only` / `proprietary_reference`)
- Source URL
- Citation string suitable for redistribution

`consult_only` sources also get an entry, with an explicit **"phrasing not copied into translation outputs"** disclaimer (matching the existing uW TN pattern).

`proprietary_reference` sources are not enumerated individually in `ATTRIBUTIONS.md` (those are private translator tools), but the general fact that the translator uses Logos library + commercial lexicons is acknowledged in a single line.

---

## 5. Curator obligations (Ben)

When a new source is being considered:

1. Identify the publication's license. Read the actual license text, not the publisher's marketing.
2. Choose a role from the five-role table. If unsure between `morphology_data` and `consult_only`, default to `consult_only`.
3. Add the source to §2 of this doc + add an `ATTRIBUTIONS.md` entry.
4. Commit the source-clone + the policy update + the attribution update in a single PR. The PR description references this policy doc.

**Refusal triggers.** If a source's license is non-commercial, share-alike, or requires per-redistributor consent, it cannot enter the repo as `primary_text` or `morphology_data`. Reclassify as `consult_only` or refuse.

**Periodic re-verification.** Twice a year, or at every major OT phase boundary (6A → 6B, etc.), Ben re-reads the §2 table and confirms each source is still permissibly used at its assigned role. License terms can change at edition boundaries (a CC-BY 3.0 source becoming CC-BY-SA 4.0 in v3 is a real failure mode). This re-verification is logged in a brief commit comment.

---

## 6. The CC0 promise to downstream users

Anyone who uses the Eremos Thai output should be able to:

- Reuse our Thai text under CC0 (no attribution required, no license propagation)
- Trust that no part of our Thai text was lifted from a source that would re-encumber their downstream use
- Find clear pointers to the open-licensed sources we depended on, in case they want to verify or extend our work

This policy exists to make that promise structurally enforceable, not just aspirational.
