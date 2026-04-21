# Review Tools — community and scholarly review infrastructure

Our automated check cadence (see `RULES.md §7`) is SIL/Wycliffe-style enforcement at the machine level. For the manual steps that cannot be automated (native-speaker naturalness review, theological review, community comprehension testing), these are the free and/or sponsored tools that the Bible translation industry uses.

---

## 1. Paratext (SIL/UBS)

**What it is:** Industry-standard desktop app for Bible translation teams. Used by almost every formal translation project. Core features:
- Biblical Terms glossary enforcement (our `check_key_term_consistency.py` is a lightweight version of this)
- Parallel passage tool (synoptic + cross-testament)
- Consultant review workflow (remote consultants annotate and approve)
- Community testing tools
- Automated structural checks (verse count, quotation marks, etc.)

**Cost:** Paid subscription (~$100–200/year) OR **free for qualified missionary translators** via SIL sponsorship.

**Apply for free access:**  
https://paratext.org/request-access/  
You'll likely qualify. List your project (open-source CC0 Thai Bible), affiliation, and training. Response time: weeks.

**How it fits:**
- We can **import/export** between Paratext and our pipeline using USFM format
- Paratext would give you the **consultant-check workflow** that's currently absent from our pipeline
- Thai-speaking reviewers can annotate verses directly in Paratext rather than in JSON files

**Priority:** High. Apply now in the background even as you keep translating with our pipeline — it'll take weeks to get approved anyway, and Paratext becomes very useful once you have many chapters that need native-speaker review at scale.

---

## 2. Scripture Forge (SIL)

**What it is:** Free, open-source, web-based. Think "Paratext but in a browser with community features." Built by SIL on top of Paratext. Features:
- AI-assisted draft generation (their own models, not Claude — their quality is lower than Opus for our use case, but free)
- Community checking via web (reviewers don't need to install desktop software)
- Paratext integration (sync with Paratext projects)
- Text-to-speech for audio review

**Cost:** Free. Sign up at https://scriptureforge.org/.

**How it fits:**
- **Community review at scale.** If you want Thai Christians scattered around the country to review chapters, Scripture Forge is the path. They just need a web browser.
- Their AI-draft feature isn't what we want (lower quality than Opus + our pipeline), so **don't use it for drafting** — use it for **review workflow only**.
- Can sync with Paratext, so once you're set up there, reviewers feed back through Scripture Forge.

**Priority:** Medium. Once you have 5-10 chapters done, set up a Scripture Forge project and invite Thai-speaking reviewers. Free, web-based, low barrier.

---

## 3. unfoldingWord tools

**What it is:** Open ecosystem of Bible translation helps:
- **Translation Notes** (verse-by-verse scholarly commentary, CC-BY-SA) — we now auto-fetch these per chapter via `scripts/enrich_with_uw.py` → `output/uw_notes/<slug>_<NN>.md`. Claude reads them as scholarly context during translation.
- **Translation Words** (~1,000-term theological glossary, CC-BY-SA)
- **Translation Questions** (comprehension questions per chapter — good for community review testing)
- **tC Create** (web app) — where church-based translators collaborate on gateway language translations

**Cost:** Free. Content under CC-BY-SA 4.0.

**How it fits:**
- Already integrated into our pipeline for reference. Claude sees the uW notes when translating.
- **Copyright note:** we use them for reference only. Paraphrasing their notes into our own rationale is fine. Copying TN text verbatim into our translation output would make our output CC-BY-SA (we want CC0) — so we never copy.

**Priority:** Already integrated.

---

## 4. SIL AQuA (Augmented Quality Assessment)

**What it is:** SIL's AI quality-assessment tool. Runs translations through NLP models trained on expert translation consultant judgments. Produces "heat maps" of passages likely to have clarity/accuracy issues.

**Cost:** Part of SIL's tooling ecosystem; access usually via Paratext integration.

**How it fits:**
- **Complementary to our back-translation check.** AQuA detects a different class of issue than sequence-similarity does. Worth running as a second opinion on finished chapters.

**Priority:** Medium-low. Investigate once Paratext access is approved.

---

## 5. Avodah Connect

**What it is:** Proprietary AI Bible translation platform run by Avodah Inc.

**Cost:** Institutional partnerships only. Not accessible for individual projects.

**How it fits:** Doesn't. Noted here so future maintainers don't waste time chasing it.

**Priority:** None for this project.

---

## Recommended review workflow

Once we have meaningful chapter volume (post-Mark, post-Pauline corpus), the **manual review path**:

```
Chapter translated & passes automated checks (run_checks.py)
        ↓
Paratext import (USFM export from our pipeline)
        ↓
Native-speaker Thai reviewer opens in Paratext → flags issues with
comments (not direct edits)
        ↓
Ben addresses flags in our source output/translations/<slug>_<NN>.json
        ↓
Scripture Forge community review → wider circle of Thai believers
        ↓
Comprehension testing (uW Translation Questions)
        ↓
Re-run automated checks → bundle updated → Eremos app preview
        ↓
Chapter marked "v1.0 — reviewed & approved"
```

For the pilot phase (Mark 1, 1 Tim 3), Ben is the reviewer. Scale the workflow as the glossary and translation library grows.

---

## Current integration status

| Tool | Integration | Priority |
|------|-------------|----------|
| unfoldingWord TN | ✅ Auto-enriched per chapter (`enrich_with_uw.py`) | Done |
| unfoldingWord TW glossary | ⚠ Cloned at `sources/en_tw/`, not yet parsed into our glossary | Medium |
| Paratext | ✅ USFM export ready (`scripts/export_to_usfm.py`); registration code on file; install + first-run pending | **Install when reviewer is ready** |
| Scripture Forge | ❌ Not yet. Web-based companion; setup once Paratext project exists and is pushed to DBL. | Medium |
| SIL AQuA | ❌ Depends on Paratext access. | Low |
| Avodah Connect | N/A (inaccessible) | None |

### Paratext import procedure (when ready)

1. **Install Paratext 9** on the Mac from https://paratext.org/download. Enter the registration code on first run.
2. **Create a new Paratext project** — Language: Thai, License: CC0, Canon: NT (27 books), Project name: "Eremos Translation" (or similar).
3. **Regenerate the USFM export** from our pipeline:
   ```bash
   cd ~/thai-bible-ai
   python3 scripts/export_to_usfm.py --all
   ```
   Writes per-book `.SFM` files to `output/paratext/`. Includes Tier 2 textual-variant chapter footers (Matt 17:21, 18:11, 23:14, etc.) as `\rem` markers.
4. **Import into Paratext**: File → Import USFM → select `output/paratext/` → pick books to import.
5. **Enable Send/Receive** to push the project to DBL if you want consultants or Scripture Forge reviewers to access it remotely.

The export is deterministic — re-run anytime a chapter ships, re-import into Paratext to refresh. Paratext's built-in diff view will show what changed.

### What's exported vs. what stays in the source repo

**Exported to USFM** (reader-facing text): verse-by-verse Thai translation, chapter markers, textual-variant chapter footers, book metadata (Thai title, running header, TOC).

**Stays in `output/translations/*.json`** (translator/scholar apparatus): `key_decisions`, `notes`, `thai_summary`, `thai_literal`, `bsb_english`. These are not published Bible text — they're our translation audit trail — and live in the open-source GitHub repo for transparency.

---

## Action items for "autopilot" readiness

- [x] unfoldingWord TN auto-enrichment per chapter
- [ ] **Apply for Paratext sponsored access** (Ben's manual step: https://paratext.org/request-access/)
- [ ] Build `scripts/import_uw_tw.py` — parse uW Translation Words glossary and cross-reference with our `glossary.json`
- [ ] USFM export from our `output/translations/<slug>_<NN>.json` for Paratext import (script: `scripts/export_usfm.py` — TODO)
- [ ] Set up Scripture Forge project when ≥5 chapters translated
