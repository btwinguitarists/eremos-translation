#!/usr/bin/env python3
"""
Hallucination / pipeline-hypocrisy check.

Scans translation notes for phrases that claim a pipeline action was taken
(e.g., "Added to nt_ot_citations.json", "Updated glossary", "Wrote HASHES.md")
and verifies the named artifact actually contains the expected evidence. Fails
ship when the translator claims a side-effect that didn't happen.

Background:
  The Opus 4.6→4.7 update introduced a pattern where the model's notes would
  claim to have updated auxiliary files (nt_ot_citations.json, etc.) without
  actually performing the update. The drift check in check_ot_citations.py
  catches this for OT citations. This script generalizes the pattern to
  other claimed pipeline actions.

Claims currently detected:
  - "added to nt_ot_citations" / "adding to nt_ot_citations"
        → verified by check_ot_citations.py's drift detector (pointer only)
  - "glossary established" / "glossary entry established" / "adding to glossary"
        → verified against glossary.json
  - "added to HASHES.md" / "updated HASHES.md"
        → verified by checking HASHES.md contains the chapter

Usage:
  python3 scripts/check_claim_consistency.py --book mark --chapter 15
  python3 scripts/check_claim_consistency.py --book mark --chapter 15 --stdout

Exit codes:
  0 = all claims verified
  1 = at least one claim unverified (ship blocked)
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
GLOSSARY_PATH = ROOT / "glossary.json"
HASHES_PATH = ROOT / "HASHES.md"
CITATIONS_PATH = ROOT / "data" / "nt_ot_citations.json"
REPORTS = ROOT / "output" / "check_reports"

SLUG_TO_CODE = {
    "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN",
    "acts": "ACT", "romans": "ROM", "1corinthians": "1CO", "2corinthians": "2CO",
    "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
    "1thessalonians": "1TH", "2thessalonians": "2TH", "1timothy": "1TI", "2timothy": "2TI",
    "titus": "TIT", "philemon": "PHM", "hebrews": "HEB", "james": "JAS",
    "1peter": "1PE", "2peter": "2PE", "1john": "1JN", "2john": "2JN",
    "3john": "3JN", "jude": "JUD", "revelation": "REV",
}


# Claim patterns — each is a (label, regex, verifier) tuple.
# Verifiers take (verse, match_text, book_code, chapter) and return
# (is_verified, message) tuples.

GLOSSARY_CLAIM_RE = re.compile(
    r"glossary\s+(?:established|entry\s+established|continuous\s+usage|reaffirmed|glossary-established)",
    re.IGNORECASE,
)
GLOSSARY_ADD_RE = re.compile(r"adding\s+to\s+glossary", re.IGNORECASE)
HASHES_CLAIM_RE = re.compile(r"(?:added|updated|written)\s+to\s+HASHES\.md", re.IGNORECASE)
CITATIONS_CLAIM_RE = re.compile(
    r"(?:added|adding|updated)\s+(?:to\s+)?nt_ot_citations(?:\.json)?",
    re.IGNORECASE,
)


def load_glossary():
    """Load the glossary — the actual entries live under data['entries']."""
    try:
        data = json.loads(GLOSSARY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    if isinstance(data, dict):
        for k in ("entries", "terms"):
            if k in data and isinstance(data[k], dict):
                return data[k]
    return data if isinstance(data, dict) else {}


def load_citations():
    try:
        return json.loads(CITATIONS_PATH.read_text(encoding="utf-8"))["citations"]
    except Exception:
        return {}


_WORD_RE = re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]+")  # Greek chars


def verify_glossary_claim(verse, match_text, book_code, chapter, glossary):
    """A 'glossary established' claim should correspond to at least one key
    decision on this verse whose Greek phrase contains a token that matches
    a glossary entry (exact or substring). Phrases are tokenized so that a
    key_decision like 'ἔθνος ἐπ' ἔθνος καὶ βασιλεία' still verifies when
    only individual lemmas (ἔθνος, βασιλεία) are in the glossary."""
    keydecs = (verse.get("translation", {}) or {}).get("key_decisions", []) or []
    if not keydecs:
        return False, "claim made but verse has no key_decisions entries"
    gloss_keys = list(glossary.keys())
    # Also tokenize glossary keys — they may themselves be phrases
    gloss_tokens = {
        t for k in gloss_keys for t in _WORD_RE.findall(k)
    } | {k for k in gloss_keys if _WORD_RE.fullmatch(k or "")}
    for d in keydecs:
        phrase = d.get("greek", "") or ""
        for tok in _WORD_RE.findall(phrase):
            if tok in gloss_tokens:
                return True, f"glossary contains token {tok!r}"
            # Also match as substring of any glossary key
            for gk in gloss_keys:
                if tok in gk or gk in tok:
                    return True, f"glossary key matches token {tok!r}"
    return False, f"no key_decision Greek token found in glossary"


def verify_hashes_claim(verse, match_text, book_code, chapter):
    """A HASHES.md claim should correspond to the chapter's translation file
    being listed in HASHES.md."""
    if not HASHES_PATH.exists():
        return False, "HASHES.md does not exist"
    text = HASHES_PATH.read_text(encoding="utf-8")
    slug_pattern = f"_{chapter:02d}.json"
    if slug_pattern not in text:
        return False, f"HASHES.md has no entry for *{slug_pattern}"
    return True, "HASHES.md contains chapter entry"


def verify_citations_claim(verse, match_text, book_code, chapter, citations):
    """A 'added to nt_ot_citations' claim requires an entry for this verse."""
    ref_key = f"{book_code} {chapter}:{verse['verse']}"
    if ref_key in citations:
        return True, f"DB has entry for {ref_key}"
    return False, f"no entry for {ref_key} in data/nt_ot_citations.json"


def check(book_code: str, chapter: int, translation_file: Path):
    verses = json.loads(translation_file.read_text(encoding="utf-8"))
    glossary = load_glossary()
    citations = load_citations()

    failures = []  # list of {verse, claim, reason}
    verified = []
    total_claims = 0
    seen = set()  # dedupe repeated claims on the same verse

    for v in verses:
        trans = v.get("translation", {}) or {}
        notes = trans.get("notes", "") or ""
        rats = " ".join((d.get("rationale") or "") for d in trans.get("key_decisions", []) or [])
        combined = notes + "\n" + rats

        # Glossary claims (both "established" and "adding to")
        for m in list(GLOSSARY_CLAIM_RE.finditer(combined)) + list(GLOSSARY_ADD_RE.finditer(combined)):
            key = (v["reference"], m.group(0).lower().strip())
            if key in seen:
                continue
            seen.add(key)
            total_claims += 1
            ok, msg = verify_glossary_claim(v, m.group(0), book_code, chapter, glossary)
            entry = {"verse": v["reference"], "claim": m.group(0), "reason": msg}
            (verified if ok else failures).append(entry)

        # HASHES.md claims
        for m in HASHES_CLAIM_RE.finditer(combined):
            key = (v["reference"], m.group(0).lower().strip())
            if key in seen:
                continue
            seen.add(key)
            total_claims += 1
            ok, msg = verify_hashes_claim(v, m.group(0), book_code, chapter)
            entry = {"verse": v["reference"], "claim": m.group(0), "reason": msg}
            (verified if ok else failures).append(entry)

        # nt_ot_citations claims (check_ot_citations.py has a dedicated drift
        # detector for this too — we keep a pointer check here so a claim
        # without a DB entry fails the consistency check independently).
        for m in CITATIONS_CLAIM_RE.finditer(combined):
            key = (v["reference"], m.group(0).lower().strip())
            if key in seen:
                continue
            seen.add(key)
            total_claims += 1
            ok, msg = verify_citations_claim(v, m.group(0), book_code, chapter, citations)
            entry = {"verse": v["reference"], "claim": m.group(0), "reason": msg}
            (verified if ok else failures).append(entry)

    return total_claims, verified, failures


def render_markdown(scope, total_claims, verified, failures):
    lines = [
        f"# Claim-consistency check — {scope}",
        "",
        f"Pipeline-action claims in notes: **{total_claims}**",
        f"- Verified: **{len(verified)}**",
        f"- Unverified (hallucinated or drifted): **{len(failures)}**",
        "",
    ]
    if failures:
        lines.append("## 🚨 UNVERIFIED CLAIMS")
        lines.append("")
        lines.append("The translator's notes claim these pipeline actions, but the")
        lines.append("named artifact has no corresponding evidence. Either make the")
        lines.append("claim true (update the file), or rephrase the note.")
        lines.append("")
        for f in failures:
            lines.append(f"- **{f['verse']}** — claim: `{f['claim']}` · reason: {f['reason']}")
        lines.append("")
    if verified and not failures:
        lines.append("All claims verified.")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    slug = args.book.lower()
    code = SLUG_TO_CODE.get(slug)
    if not code:
        print(f"Unknown book slug: {slug}")
        return 1

    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"No translation file at {translation_file}")
        return 1

    total, verified, failures = check(code, args.chapter, translation_file)
    md = render_markdown(f"{slug} ch. {args.chapter}", total, verified, failures)

    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / f"claim_consistency_{slug}_{args.chapter:02d}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")

    if failures:
        print(f"  🚨 {len(failures)} unverified claim(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
