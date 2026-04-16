# Thai Bible AI

An AI-assisted, fully open-source (CC0) Thai translation of the Bible, built directly from Hebrew, Aramaic, and Koine Greek manuscripts. Every translation decision is traceable from source text through morphological analysis to final rendering.

## Status

Phase 1 (pilot) — Gospel of Mark from SBLGNT Greek + MACULA morphology + BSB reference.

## Stack

- **Greek source:** SBLGNT (CC BY 4.0) — `sources/SBLGNT/`
- **Morphology/syntax:** MACULA Greek (CC BY 4.0) — `sources/macula-greek/`
- **English reference:** BSB (CC0) — `sources/bsb-text/bsb.txt`
- **Translation AI:** Claude API (Sonnet 4.5, configurable)

## Setup

```bash
# Install dependencies
pip3 install anthropic --break-system-packages

# Set API key (get from console.anthropic.com)
export ANTHROPIC_API_KEY=sk-ant-...
```

## Scripts

### 1. Extract verse data

```bash
python3 scripts/extract_mark.py
```

Produces `output/mark/mark_verses.json` — 673 verses with word-by-word morphology, lemma, English gloss, Louw-Nida semantic domain, and NT-wide frequency (hapax flagging). Per-chapter files also written.

### 2. Translate to Thai

```bash
# Single verse (testing)
python3 scripts/translate_mark.py --chapter 1 --verse 1

# Whole chapter
python3 scripts/translate_mark.py --chapter 1

# Entire book
python3 scripts/translate_mark.py --all

# Limit for testing
python3 scripts/translate_mark.py --chapter 1 --limit 5
```

Output format per verse:
- Greek text (SBLGNT)
- Thai translation (optimal equivalence)
- Thai literal (where it differs)
- Key translation decisions with rationale
- Notes on textual variants, hapax legomena, theological choices

## Translation Philosophy

**Optimal equivalence** (BSB-style): faithful to Greek grammar/syntax while natural to Thai readers.

- Translate FROM the Greek using morphological data
- BSB English is a sanity check only, not a source
- Do not mimic copyrighted Thai translations (independent creation)
- Flag hapax legomena and manuscript variants transparently
- Respectful Thai religious register (ราชาศัพท์ for divine subjects)

## License

All translation output is CC0 (public domain). Source texts retain their original licenses.

## See Also

Full feasibility study and plan: `~/.claude/plans/delightful-chasing-mist.md`
