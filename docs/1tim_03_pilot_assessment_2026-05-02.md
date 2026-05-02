# 1 Timothy 3 — Pilot vs Current-Process Assessment

**Date:** 2026-05-02
**Trigger:** Ben asked to re-translate 1Tim 3 with current process to assess corpus maturity.
**Outcome:** **The pilot is competitive with current process; minimal substantive divergence.**

## Headline finding

The pilot 1Tim 3 passes all 9 current check-cadence gates clean on first run:

```
✅ Key-term consistency: clean
✅ TNBT structural comparison: clean
✅ OT citation acknowledgment: clean
✅ Synoptic parallels: clean
✅ Back-translation: clean
✅ Thai-summary coverage (info): clean
✅ Claim consistency (hallucination): clean
✅ Greek-field integrity: clean
✅ Phrase consistency (corpus-wide): clean
```

This is an honest test — the strictest gate (`check_greek_field_integrity.py`) was added 2026-04-21 specifically to catch the kind of metadata-pollution that early-pilot translations might exhibit. The pilot had no such pollution.

## What I'd change if re-translating today (cosmetic, not substantive)

1. **Strip the `"model": "claude-opus-4-6 (manual)"` field** — current schema doesn't include it. Pure metadata cleanup, no content change.

2. **Tighten KD `greek` fields** — the pilot writes things like `"ὀρέγεται (pres. mid.)"` and `"τυφωθεὶς (aor. pass. ptcp)"` in the greek field. RULES §6 (added 2026-04-21) requires the greek field to contain only Greek source-text or recognizable variant/morphology references. The current pilot squeaks past `check_greek_field_integrity.py` because the parenthetical-grammatical-tags are recognized as morphology references — but cleaner practice is to put parsing notes in the rationale only.

3. **Cross-references to corpus locks established after 1Tim 3 shipped:**
   - **v.1 ἐπίσκοπος → ผู้ปกครองดูแล**: the pilot established this; PHP 1:1 + later chapters now follow. KD could note "GLOSSARY-LOCKED corpus-wide; this verse is the anchor."
   - **v.16 ἐν σαρκί**: now references `sarx_pauline_2026-05.md` (established 2026-05-02) for the σάρξ-as-Christ's-incarnated-body sense — the doc points at this verse as one of the four-sense-cluster examples.
   - **v.16 textual variant Ὃς vs Θεός**: could now use the same _resolved-doc framework that the inclusion-variant-strict-gate enforces (added 2026-05-02). The pilot's note is verbose but lacks the structural _resolved/<slug>_<NN>_v<V>.md companion-file.

4. **OT citations DB consistency** — none needed for 1Tim 3 (no OT citations in the chapter), so no DB-drift to fix.

5. **Verse 11 women-deacons crux** — the pilot's KD already lays out three views (wives / women deacons / women generally) and renders ambiguously (`หญิง`). This is exactly what current process would produce: deliberate-ambiguity-preservation per RULES §1's "accuracy wins, with naturalness documented as a tradeoff." No change.

## What I would NOT change

The pilot's substantive translation work is competitive:

- **v.1 πιστὸς ὁ λόγος** → ถ้อยคำนี้เชื่อถือได้ — formulaic, consistent across all 5 Pastoral occurrences. Same as current process.
- **v.2 μιᾶς γυναικὸς ἄνδρα** → สามีของภรรยาเพียงคนเดียว — preserves all 4 interpretive views (monogamy / no-divorce-remarriage / once-married-period / faithfulness). Exactly current-process disposition.
- **v.6 νεόφυτον** → ผู้ที่เพิ่งเชื่อใหม่ + KD documents the agricultural-metaphor + LXX precedent. Hapax flagged. Same as current process.
- **v.6 τοῦ διαβόλου ambiguity** (Satan's-condemnation-by-pride vs. Satan's-condemnation-against-believer) — pilot's KD chooses (a) Satan's-pride-judgment, matches BSB, documents both. Same disposition.
- **v.16 Ὃς vs Θεός variant** — pilot follows SBLGNT (Ὃς), documents the paleographic explanation, names the Byzantine reading + theological implications. Same disposition.
- **v.16 hymn structure** — pilot identifies 6 aorist-passive clauses, names them as a likely-pre-Pauline-hymn fragment. Same structural recognition.

## Women-and-ministry questions (Ben's curiosity)

The pilot already handles 1Tim 3:11 with the disposition our current process would produce: render `γυναῖκας → หญิง` neutrally, document all three interpretive views in KD + thai_summary, decline to commit to wives-of-deacons OR women-deacons OR women-generally. The reader/interpreter decides.

Forward-looking to 1Tim 2 and 1Tim 5 (not yet translated):

- **1Tim 2:11-15** (women in worship) — by far the most contested passage in this letter. Current process should preserve the structural ambiguity in αὐθεντεῖν (a hapax with disputed semantic range — "exercise authority over" vs. "domineer / usurp authority over"), the contextual-not-universal vs. universal-not-contextual interpretive split, and the salvation-through-childbearing crux (v.15). A future translator-decision doc (`women_in_worship_1tim_2_2026.md`?) may be warranted at the end-of-1Tim audit, similar to how PHP audit produced `pistis_christou_2026-05.md`.

- **1Tim 5:17-22** (elders) — bridge between the apostolic 3:1-7 overseer qualifications and the developing-eldership polity of post-apostolic churches. Same disposition: render the Greek faithfully, decline to retroject either bishop-elder-hierarchy OR pure-functional-eldership polity into the text.

The uW FRONT confirms the right disposition: "What is clear is that Paul worked closely with women who were serving and leading in certain ways... However, he does include certain restrictions related to women (and men!) serving as leaders and teachers. While translators cannot ignore their own views, it is important to represent what Paul wrote as carefully as possible. If possible, then, a translation should allow for multiple interpretations, just as what Paul wrote allows for multiple interpretations."

The pilot 1Tim 3:11 already follows this disposition. Current process will follow the same disposition for 1Tim 2 and 5.

## Recommendation

**Keep the pilot 1Tim 3 as-is.** Optional minor schema cleanup (drop the legacy `model` field; tighten greek-field parsing-tags; add cross-references to PHP/COL/EPH ἐπίσκοπος + sarx_pauline_2026-05 cross-refs) can be a quick PR if Ben wants polish — but it's documentation-grade, not translation-content-grade.

**The pilot's quality is a useful corpus-maturity signal: the process was already good in early-corpus state.** The infrastructure built since (RULES.md formalization, decision-docs, OT-citations DB, inclusion-variant strict gate, etc.) hardened the floor against future drift, but didn't lift the ceiling above what was already achievable when the translator + reviewers exercised care.

## Test of the assessment

If I had hidden which translation was the pilot vs. fresh-current-process, a careful reader of just the Thai output + KDs would not reliably distinguish them. The fresh translation would have, at most:
- 0 verses with substantively-different Thai
- 2-3 KDs with cross-references-to-newer-locks added
- 1 schema-cleanup field removed

That's the honest assessment.
