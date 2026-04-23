#!/usr/bin/env python3
"""
Discover candidate parallelism-drift cases across the corpus.

This is a DISCOVERY TOOL, not a pass/fail check. It scans for recurring
Greek N-gram phrases (3-5 content words) and reports when their Thai
renderings diverge across verses. Output is a candidate list for human
review — add confirmed drift patterns to `scripts/check_phrase_consistency.py`
as new locks.

Motivated by Claude external-review (2026-04-23) catching the LUK 10:20/18:22
"in heaven" parallelism violation that the per-lemma and per-phrase checkers
both missed, because the Greek constructions were similar but not identical.

Pragmatic scope:
- Extract 3-to-5-word Greek phrases from each verse
- Filter out pure-function-word sequences (articles + particles only)
- For phrases appearing in 2-10 verses, collect Thai renderings
- Report phrases where Thai renderings differ substantially

Output is informational markdown. Human reviews and decides which
candidates are genuine drift vs. principled variation.

Usage:
  python3 scripts/discover_parallelism_drift.py
  python3 scripts/discover_parallelism_drift.py --min-n 4 --max-verses 5
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"


# Greek articles + particles + most common conjunctions/prepositions.
# A phrase containing ONLY these is usually not semantically interesting;
# we want phrases that include at least one content-bearing token.
GREEK_FUNCTION_TOKENS = {
    "ὁ", "ἡ", "τό", "οἱ", "αἱ", "τά", "τοῦ", "τῆς", "τῶν", "τῷ", "τῇ", "τόν", "τήν",
    "τούς", "τάς", "τοῖς", "ταῖς",
    "καί", "δέ", "γάρ", "οὖν", "ἀλλά", "ὅτι", "εἰ", "ἐάν", "ἵνα", "ὡς",
    "ἐν", "εἰς", "ἐκ", "ἀπό", "πρός", "διά", "κατά", "μετά", "ὑπό", "ὑπέρ", "περί",
    "ἐπί", "παρά", "σύν",
    "μή", "οὐ", "οὐκ", "οὐχ", "μηδέ", "οὐδέ",
    "ἐστιν", "εἰμί", "εἰσιν", "ἐστί",  # common copulas
    "τις", "τι", "τινι", "τινα",
    "γε", "μέν", "τε",
    "ἐγώ", "σύ", "ἡμεῖς", "ὑμεῖς", "αὐτός", "αὐτή", "αὐτό", "αὐτοῦ", "αὐτῆς",
    "αὐτοῖς", "αὐτούς", "αὐτάς", "αὐτῷ", "αὐτῇ", "αὐτόν", "αὐτήν",
    "ὅς", "ἥ", "ὅ", "ᾧ", "ᾗ",
    # Ultra-common narrative framing verbs — produce noise when indexed
    "εἶπεν", "λέγει", "ἔλεγεν", "ἔλεγον", "εἶπον", "ἀπεκρίθη", "λέγων", "λέγοντες",
    "ἦλθεν", "ἦλθον", "ἔρχεται", "ἦν",
}

# Thai function words — we want to see if the content-bearing renderings
# overlap, not just filler.
THAI_FUNCTION_TOKENS = {
    "ก็", "ที่", "ของ", "ว่า", "จะ", "ได้", "แล้ว", "และ", "หรือ", "แต่",
    "ใน", "กับ", "จาก", "ถึง", "เพื่อ", "ต่อ", "โดย", "ด้วย", "เพราะ", "แก่",
    "อย่าง", "เป็น", "มี", "ไม่", "เอง", "ให้", "อยู่", "เลย", "นั้น", "นี้",
    "ทั้ง", "หลาย", "เหล่า", "พวก", "บรรดา", "คน", "สิ่ง", "ผู้", "แห่ง",
    "พระ", "ทรง",  # filter honorifics since they attach to many words
    "ท่าน", "เรา", "เขา", "เจ้า",  # pronouns
}


def tokenize_greek(greek_text):
    """Split Greek text into word tokens (keep diacritics intact)."""
    # Remove punctuation but keep Greek letters + spaces
    clean = re.sub(r"[,.·;·\"'«»‹›()\[\]]", " ", greek_text)
    tokens = clean.split()
    return tokens


def tokenize_thai(thai_text):
    """Split Thai text by spaces + common punctuation."""
    clean = re.sub(r"[,.·;·\"'«»‹›()\[\]?!]", " ", thai_text)
    # Thai doesn't use spaces between words — but our pipeline does use
    # sentence-level spaces. Keep them as delimiters.
    tokens = [t for t in clean.split() if t]
    return tokens


def greek_phrase_is_contentful(tokens):
    """True if phrase has at least TWO tokens that aren't function words.
    Single-content-word phrases produce too many false positives."""
    lower_tokens = [t.lower() for t in tokens]
    content = sum(1 for t in lower_tokens if t not in GREEK_FUNCTION_TOKENS)
    return content >= 2


def extract_ngrams(tokens, n):
    """Yield n-grams as tuples."""
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i:i + n])


def thai_4gram_similarity(thai_a, thai_b):
    """
    Compute Jaccard similarity of 4-character substrings between two Thai
    strings. Returns float in [0, 1]. Thai doesn't use word spaces, so
    character-level n-grams approximate content-similarity.
    """
    a_4grams = set(thai_a[i:i + 4] for i in range(len(thai_a) - 3))
    b_4grams = set(thai_b[i:i + 4] for i in range(len(thai_b) - 3))
    if not a_4grams or not b_4grams:
        return 1.0
    shared = a_4grams & b_4grams
    total = a_4grams | b_4grams
    return len(shared) / len(total) if total else 0


def load_verses():
    """Yield (ref, greek, thai) for every shipped verse."""
    for f in sorted(TRANSLATIONS.glob("*.json")):
        try:
            data = json.load(open(f))
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(data, list):
            continue
        for v in data:
            if isinstance(v, dict) and "greek" in v and "translation" in v:
                ref = v.get("reference", "?")
                greek = v.get("greek", "")
                thai = v["translation"].get("thai", "") or ""
                if greek and thai:
                    yield ref, greek, thai


def discover_drift(min_n, max_n, min_verses, max_verses):
    """
    Build an index of Greek n-grams → verses containing them.
    Return list of candidate-drift cases.
    """
    # phrase → list of (ref, thai)
    index = defaultdict(list)
    for ref, greek, thai in load_verses():
        tokens = tokenize_greek(greek)
        for n in range(min_n, max_n + 1):
            for ngram in extract_ngrams(tokens, n):
                if not greek_phrase_is_contentful(ngram):
                    continue
                phrase = " ".join(ngram)
                index[phrase].append((ref, thai))

    # Find phrases appearing in 2-max_verses verses (ignore one-offs and
    # super-common constructions that are mostly noise)
    candidates = []
    for phrase, occurrences in index.items():
        refs = list(set(o[0] for o in occurrences))
        if not (min_verses <= len(refs) <= max_verses):
            continue
        # Compare Thai pairwise — find the MINIMUM similarity across all
        # pairs. A phrase with high min-similarity has consistent Thai
        # across all its verses. Low min-similarity means at least one
        # pair diverges — candidate for review.
        thai_by_ref = {}
        for ref, thai in occurrences:
            if ref not in thai_by_ref:
                thai_by_ref[ref] = thai
        verses = list(thai_by_ref.items())
        if len(verses) < 2:
            continue
        min_sim = 1.0
        for i in range(len(verses)):
            for j in range(i + 1, len(verses)):
                sim = thai_4gram_similarity(verses[i][1], verses[j][1])
                if sim < min_sim:
                    min_sim = sim
        # Only consider as drift-candidate if MIN similarity is very low
        # (< 0.15 — substantial divergence, not just surrounding context)
        if min_sim < 0.15:
            candidates.append({
                "phrase": phrase,
                "n_verses": len(verses),
                "min_similarity": min_sim,
                "occurrences": verses,
            })
    # Sort by severity (lowest Thai similarity = most suspicious)
    candidates.sort(key=lambda c: c["min_similarity"])
    return candidates


def write_report(candidates, out_path):
    lines = ["# Parallelism-drift discovery report", ""]
    lines.append("**Purpose:** auto-surface Greek phrases whose Thai renderings diverge across verses. Human review decides if each case is (a) genuine drift → add to `check_phrase_consistency.py`, (b) principled variation → document per-verse.")
    lines.append("")
    lines.append("**Scope:** 4-5-token Greek phrases with ≥2 content tokens; phrase appears in 2-5 verses; minimum pairwise Thai 4-gram similarity < 0.15 (substantial divergence).")
    lines.append("")
    lines.append("**Limitations:** this tool is imprecise by design. Many candidates will turn out to be principled variation (Greek sg/pl, different discourse contexts, etc.), not drift. Review top 30 and decide per-case.")
    lines.append("")
    lines.append(f"**Candidates found:** {len(candidates)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    if not candidates:
        lines.append("No drift candidates detected.")
    else:
        lines.append(f"Showing top 30 of {len(candidates)} total candidates (sorted by severity: lowest Thai similarity first).")
        lines.append("")
        for c in candidates[:30]:
            lines.append(f"## `{c['phrase']}`  —  min similarity {c['min_similarity']:.2f}")
            lines.append(f"**Verses:** {c['n_verses']}")
            lines.append("")
            for ref, thai in c["occurrences"]:
                lines.append(f"- **{ref}**: {thai[:140]}")
            lines.append("")
            lines.append("---")
            lines.append("")
    out_path.write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--min-n", type=int, default=3, help="min Greek phrase length (tokens)")
    ap.add_argument("--max-n", type=int, default=4, help="max Greek phrase length (tokens)")
    ap.add_argument("--min-verses", type=int, default=2, help="min verses phrase must appear in")
    ap.add_argument("--max-verses", type=int, default=10, help="max (filter out super-common phrases)")
    args = ap.parse_args()

    print(f"Scanning Greek phrases ({args.min_n}-{args.max_n} tokens)...")
    candidates = discover_drift(args.min_n, args.max_n, args.min_verses, args.max_verses)
    print(f"Found {len(candidates)} candidate-drift phrases.")

    REPORTS.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS / "parallelism_drift_discovery.md"
    write_report(candidates, out_path)
    print(f"Wrote {out_path}")
    print()
    print("This is a DISCOVERY tool — not a pass/fail check. Review the report")
    print("and decide: (a) genuine drift → add to check_phrase_consistency.py,")
    print("(b) principled variation → document per-verse.")


if __name__ == "__main__":
    main()
