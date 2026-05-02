# Inclusion-variant backfill — work order (2026-05-02)

**For Ben to execute through the pipeline.** This doc is a directive prompt: paste it into a `claude` session at `~/thai-bible-ai` (or run `claude < docs/end_of_book/backfill_workorder_2026-05-02.md`) to backfill the two genuine Tier 2/3 gaps surfaced by the inclusion-variant audit.

**Scope.** Two cases. Both are SBLGNT-omits-mainstream-includes where mainstream English/Thai readers will notice the absence:

1. **John 5:4** — angel troubling the Bethesda waters
2. **Romans 16:25-27** — the doxology

Other corpus-wide gaps (Mark 11:26, 15:28; Luke 17:36; ~30 other audit-flagged candidates) are handled by `_resolved/` dismissals or RULES §5 silent-omission notes phrasing — not by this work order.

**Constraints (read-only — do not improvise):**
- Follow `RULES.md` §5 strictly. Tier 2 → chapter-footer file at `output/textual_variants/<slug>_<NN>.json`. Tier 3 → `⟦…⟧` markers in main text + extended note.
- Use the existing Tier 2 file format. Compare to `output/textual_variants/matthew_17.json` (Tier 2 reference) and `output/translations/mark_16.json` v.9 (Tier 3 reference).
- Translate **from the TR/Byz Greek source** — it is the textual basis for these inclusion-variants. The English BSB equivalent is reference-only per RULES §1.
- Match the Thai register of the surrounding verses (formal liturgical for the doxology; narrative for John 5:4). Use `ราชาศัพท์` for divine subjects per RULES §3.
- Document witnesses on both sides honestly. Witness lists are in `docs/end_of_book/inclusion_variant_gap_2026-05-02.md` for both cases — do not re-research; copy verbatim.
- Every Greek term that involves a translation decision must have a `key_decisions` entry per RULES §6.

---

## Task 1 — John 5:4 (Tier 2 chapter-footer file)

**Output:** `output/textual_variants/john_05.json` (file does not currently exist; create it).

**Format:** array of one object, matching `output/textual_variants/matthew_17.json`'s shape.

**TR/Byz Greek (verbatim from Stephanus 1550 / Byzantine majority text):**
```
ἄγγελος γὰρ κατὰ καιρὸν κατέβαινεν ἐν τῇ κολυμβήθρᾳ, καὶ ἐτάρασσε τὸ ὕδωρ· ὁ οὖν πρῶτος ἐμβὰς μετὰ τὴν ταραχὴν τοῦ ὕδατος, ὑγιὴς ἐγίνετο, ᾧ δήποτε κατείχετο νοσήματι.
```

**BSB English equivalent (reference only):**
> "For an angel of the Lord went down at certain seasons into the pool, and stirred up the water; whoever then first, after the stirring up of the water, stepped in was made well from whatever disease he had."

**Witnesses (use these verbatim):**
- **Include:** Byzantine majority, A, C³, K, L, X, Δ, Θ, Ψ, 063, 078, f¹, f¹³, lat (most), sy^p, sy^h, KJV, THKJV
- **Omit:** 𝔓⁶⁶, 𝔓⁷⁵, ℵ, B, C*, D, T, W, 0125, 0141, sa, bo (most), most modern English (BSB, ESV, NIV, CSB), modern Thai THSV

**Notes for translator:**
- Note also that v.3b ("waiting for the moving of the water") is part of the same inclusion variant. Per `output/translations/john_05.json` v.3 notes, the existing translator intent was to bundle 5:3b and 5:4 as a single inclusion-variant unit in the Tier 2 footer — match that intent. Both pieces of contested text go into the same Tier 2 entry's `tr_byz_thai` (or as a single `verse: 4` entry whose explanation references the v.3b boundary).
- Cross-reference: the Bethesda narrative has parallel pool-of-Siloam imagery in John 9; mention briefly in `explanation_thai`.

**Required fields per `output/textual_variants/matthew_17.json` schema:**
- `verse`: 4
- `type`: `"inclusion_variant_absent"`
- `tr_byz_greek`: the verbatim Greek above
- `tr_byz_thai`: your Thai translation matching the surrounding chapter's register
- `bsb_english_equivalent`: the BSB-style English above
- `witnesses_include`: the Include list above
- `witnesses_omit`: the Omit list above
- `explanation_thai`: a Thai paragraph explaining the manuscript situation in the same plain-Thai register as the Matthew 17:21 example
- `cross_reference`: brief reference to John 5:3b (the bundled inclusion-variant), and to the John 9 Siloam-pool parallel

**After writing the file:**
1. Re-run the inclusion audit: `python3 scripts/audit_inclusion_variants.py --book john --strict` — John 5:3 should now show `✓ tier2`.
2. Re-export USFM: `python3 scripts/export_to_usfm.py --book JHN`.
3. Update v.3's notes in `output/translations/john_05.json` to remove the lie about "see output/textual_variants/john_05.json" being already-existent — replace with truthful "Tier 2 chapter-footer note (see output/textual_variants/john_05.json) added 2026-05-02 to remediate corpus-wide inclusion-variant audit gap; original v.3 translation unchanged."

---

## Task 2 — Romans 16:25-27 (Tier 3 large-block transmission)

**Decision required first.** The doxology is 3 verses long, ~80 Greek words. Per RULES §5 decision matrix:
- Tier 2 (chapter footer) is reasonable but pushes a large body of text into a footer block, which is unusual for footer-style (Matt 17:21 / Acts 8:37 are single short verses).
- Tier 3 (`⟦…⟧` in main text) parallels the Mark 16:9-20 longer-ending and John 7:53-8:11 pericope-adulterae treatments — both are large-block transmissions with significant theological content most readers expect.

**Recommendation: Tier 3.** Reasons:
- The doxology is the closing of Romans for almost every English Bible reader and a doctrinally-important passage (Pauline mystery / nations / faith-obedience / glory-Christology).
- Quantitatively closer to Mark 16:9-20 than to a single-verse Matthew 17:21.
- A reader of THSV / KJV / NKJV will absolutely look for it at the end of Romans.

**If Tier 3:** add three new entries to `output/translations/romans_16.json` (verses 25, 26, 27). Open `⟦` at start of v.25's `thai`, close `⟧` at end of v.27's `thai`. Match the bracketing pattern of `output/translations/mark_16.json` v.9 (open) and v.20 (close).

**If Tier 2:** create `output/textual_variants/romans_16.json` as a single entry covering vv.25-27 as one inclusion-variant block.

**TR/Byz Greek:**

```
v.25: Τῷ δὲ δυναμένῳ ὑμᾶς στηρίξαι κατὰ τὸ εὐαγγέλιόν μου καὶ τὸ κήρυγμα Ἰησοῦ Χριστοῦ, κατὰ ἀποκάλυψιν μυστηρίου χρόνοις αἰωνίοις σεσιγημένου,

v.26: φανερωθέντος δὲ νῦν διά τε γραφῶν προφητικῶν κατ᾽ ἐπιταγὴν τοῦ αἰωνίου θεοῦ εἰς ὑπακοὴν πίστεως εἰς πάντα τὰ ἔθνη γνωρισθέντος,

v.27: μόνῳ σοφῷ θεῷ, διὰ Ἰησοῦ Χριστοῦ, ᾧ ἡ δόξα εἰς τοὺς αἰῶνας τῶν αἰώνων· ἀμήν.
```

**BSB English (reference only):**
> v.25: "Now to Him who is able to strengthen you by my gospel and by the proclamation of Jesus Christ, according to the revelation of the mystery hidden for ages past
>
> v.26: but now revealed and made known through the writings of the prophets by the command of the eternal God, in order to lead all nations to the obedience that comes from faith—
>
> v.27: to the only wise God be glory forever through Jesus Christ! Amen."

**Witnesses:**
- **Include vv.25-27 at end of ch.16:** Byzantine majority, ℵ, B, C, D, 81, 1739, latt (most), sy^p, sy^h, sa, bo, KJV, THKJV, ESV, NIV, BSB, CSB, NASB
- **Place vv.25-27 at end of ch.14 instead:** L, Ψ, 0209^vid, 1881, Byzantine sub-tradition, lect (some)
- **Place at end of ch.15:** 𝔓⁴⁶, 1506, sa^mss, geo (some), Origen
- **Omit entirely:** F, G, 629, lat (some); marked as floating/inserted in some MSS witnesses to Marcion's Apostolikon (heretical, but textually significant)
- **SBLGNT** prints in main text but apparatus flags the floating-position evidence
- **NA28** prints in main text
- The variant is unique among NT inclusion variants for its **floating placement** (end of ch.14, 15, or 16 in different traditions) — strong evidence the doxology was a separate liturgical fragment that was incorporated into Romans by stages.

**Translator notes for the Tier 3 entry's `notes` field (or `thai_summary`):**
- Three theological motifs to preserve: (1) μυστήριον (the mystery hidden for ages, now revealed); (2) προφητικαὶ γραφαί (the prophetic writings); (3) εἰς ὑπακοὴν πίστεως εἰς πάντα τὰ ἔθνη (to all nations, for the obedience of faith — bookend to Rom 1:5).
- Cross-references: the v.27 doxological formula echoes Eph 3:20-21, 1 Tim 1:17, 6:16; the μυστήριον theme parallels Eph 3:3-9, Col 1:26-27.
- The "obedience of faith / all nations" formula is the rhetorical bookend with Rom 1:5 — even if the doxology is post-Pauline editorial, the editor preserved Paul's structural rhetoric.

**Required structure for vv.25-27 entries (Tier 3 — main verse list):**
Match the `output/translations/romans_16.json` v.24 entry's keys exactly:
- `reference`, `chapter`, `verse`
- `greek` (the TR/Byz Greek above for that verse)
- `bsb_english` (the BSB English above for that verse — note this is reference data, fine to populate even though SBLGNT omits)
- `translation.thai` — the Thai with `⟦` opening at v.25 and `⟧` closing at v.27
- `translation.thai_summary` — extensive Thai-language explanation of the textual situation, the floating-placement issue, and the doctrinal substance
- `translation.key_decisions` — every Greek choice that involved interpretation (μυστήριον, προφητικαὶ γραφαί, ὑπακοὴν πίστεως, μόνῳ σοφῷ θεῷ, etc.)
- `translation.notes` — extended notes including the floating-placement evidence, the cross-references, and a "TIER 3 large-block per RULES §5" header

**After writing the verses:**
1. Re-run the inclusion audit: `python3 scripts/audit_inclusion_variants.py --book romans --strict` — Romans 16:24 candidate should now resolve to `✓ tier3` (because v.25's thai contains `⟦`).
2. Re-export USFM: `python3 scripts/export_to_usfm.py --book ROM`.
3. Update v.24's notes to reflect the new state: replace "doxology omitted in SBLGNT — Romans ends here" with "doxology vv.25-27 added 2026-05-02 as Tier 3 large-block transmission (`⟦…⟧`) per RULES §5; remediation of inclusion-variant audit gap, see `docs/end_of_book/inclusion_variant_gap_2026-05-02.md`."

---

## Verification (run after both tasks complete)

```bash
cd ~/thai-bible-ai

# Should show Romans + John strict-pass (no UNRESOLVED inclusion candidates):
python3 scripts/audit_inclusion_variants.py --book romans --strict
python3 scripts/audit_inclusion_variants.py --book john --strict

# Should regenerate ROM.SFM (with Tier 3 verses) and JHN.SFM (with Tier 2 footer):
python3 scripts/export_to_usfm.py --book ROM
python3 scripts/export_to_usfm.py --book JHN

# All per-chapter checks should still pass:
python3 scripts/run_checks.py --book ROM
python3 scripts/run_checks.py --book JHN

# Sanity-check the new SFM has the chapter footer for John 5:
grep -A 3 "หมายเหตุด้านต้นฉบับ" output/paratext/JHN.SFM | head -10

# Sanity-check Romans 16 SFM has the doxology with double brackets:
grep -A 3 "⟦" output/paratext/ROM.SFM | head -8
```

## When done

- Open a PR titled "Backfill inclusion-variant gap: John 5:4 + Romans 16:25-27"
- Reference `docs/end_of_book/inclusion_variant_gap_2026-05-02.md` in the PR body
- Tag `book-romans-v1` only after this is merged (the Romans end-of-book audit gate will block tagging while the doxology is unresolved)
