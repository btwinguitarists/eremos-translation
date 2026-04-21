#!/usr/bin/env python3
"""
Greek-field integrity check — catches schema drift in key_decisions[].greek.

Background:
  The LUK 13/14 drift of 2026-04-21 surfaced a class of metadata hallucination
  the other checks couldn't see: the `greek` field of key_decisions entries
  contained Thai characters (e.g., Thai pronouns stuffed into the Greek slot)
  or fabricated Greek-looking strings (e.g., "ἐσδέจ" — mixed Greek/Thai
  characters, not a real Greek word). All seven prior checks passed green.
  See docs/LUKE_DRIFT_2026-04-21.md for the remediation write-up.

What this enforces (per RULES.md §6 schema):

  The `greek` field of a key_decisions entry should contain the Greek source
  phrase as it appears in the verse, OR an explicit reference to a textual
  variant / classical usage / LXX reading / hapax etymology that the
  rationale itself identifies. Thai or mixed-script content is a schema
  violation.

Three checks:

  [A] HARD FAIL — `greek` field contains Thai characters (U+0E00–U+0E7F).
      There is no legitimate reason to have Thai in the Greek-source slot.

  [B] HARD FAIL — `greek` field contains only Greek letters, and the 3+ char
      Greek tokens don't appear in the verse's `greek` source text, AND the
      rationale doesn't mention any of the legitimate-exception keywords
      (variant, mss, manuscript, byzantine, tr, na28, nestle, classical,
      lxx, hapax, composite, apparatus, 2sg, 2pl, 3sg, 3pl). This catches
      fabricated Greek tokens.

  [C] WARN (non-blocking) — `greek` field is ASCII-only and holds a meta-label
      like "Speaker: X to Y" or "Punctuation ambiguity". Legitimate usage
      pattern in Mark, but noisy — surfaced for review, not blocking.

Usage:
  python3 scripts/check_greek_field_integrity.py --book LUK --chapter 14
  python3 scripts/check_greek_field_integrity.py --all

Exit codes:
  0 = clean (no hard fails)
  1 = at least one hard fail (ship blocked)
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
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

# Rationale keywords that excuse a Greek token not appearing in the verse.
# These indicate legitimate scholarly-reference contexts (variant readings,
# classical/LXX usage, grammatical annotations).
EXCUSE_KEYWORDS = re.compile(
    r"\b("
    r"variant|mss?\b|manuscript|witness|reading|byzantine|tr\b|na28|nestle|"
    r"classical|lxx|hapax|composite|apparatus|etymolog|"
    r"[123](?:sg|pl)|sing\.|plur\.|"
    r"lemma|louw-nida|bdag|bdf|morpholog|"
    r"switched\s+from|shift(?:ed)?\s+from|cf\.|compare\s+with|parallel|synoptic"
    r")",
    re.IGNORECASE,
)


def has_thai(s: str) -> bool:
    return any(0x0E00 <= ord(c) <= 0x0E7F for c in s)


def has_greek(s: str) -> bool:
    return any(0x0370 <= ord(c) <= 0x03FF or 0x1F00 <= ord(c) <= 0x1FFF for c in s)


def strip_punct(word: str) -> str:
    """Strip common Greek punctuation so token comparisons work."""
    return word.strip(" ,.·;:()[]{}⟦⟧«»…\"'")


def normalize_greek(s: str) -> str:
    """Lowercase + strip diacritics so accent variants (acute/grave/circumflex,
    smooth/rough breathing) don't cause spurious mismatches.

    NFD decomposes combined characters (e.g., ά → α + ́), then we drop the
    combining marks. This makes 'Ἄνθρωπε' ≡ 'ἄνθρωπε' ≡ 'ανθρωπε'.
    """
    decomposed = unicodedata.normalize("NFD", s)
    stripped = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    return stripped.casefold()


def extract_greek_tokens(s: str, min_len: int = 3) -> list[str]:
    """Pull Greek-letter tokens (>=min_len chars) from a string."""
    tokens = []
    current = []
    for c in s:
        if 0x0370 <= ord(c) <= 0x03FF or 0x1F00 <= ord(c) <= 0x1FFF:
            current.append(c)
        else:
            if current:
                t = strip_punct("".join(current))
                if len(t) >= min_len:
                    tokens.append(t)
                current = []
    if current:
        t = strip_punct("".join(current))
        if len(t) >= min_len:
            tokens.append(t)
    return tokens


def check_chapter(slug: str, chapter: int) -> tuple[list, list, list]:
    """Return (fails, warns, total_kd_count) for a single chapter."""
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return ([], [], 0)

    data = json.loads(path.read_text(encoding="utf-8"))
    fails = []
    warns = []
    total_kd = 0

    for v in data:
        verse_greek = v.get("greek", "") or ""
        for kd in (v.get("translation", {}).get("key_decisions") or []):
            total_kd += 1
            g = (kd.get("greek", "") or "").strip()
            rationale = kd.get("rationale", "") or ""
            if not g:
                continue

            if has_thai(g):
                fails.append({
                    "verse": v["reference"],
                    "kind": "THAI_IN_GREEK",
                    "greek_field": g,
                    "thai_field": kd.get("thai", ""),
                    "why": "Thai characters in the key_decisions[].greek slot — schema violation.",
                })
                continue

            if has_greek(g):
                tokens = extract_greek_tokens(g, min_len=3)
                verse_greek_norm = normalize_greek(verse_greek)
                if tokens and not any(normalize_greek(t) in verse_greek_norm for t in tokens):
                    if not EXCUSE_KEYWORDS.search(rationale):
                        fails.append({
                            "verse": v["reference"],
                            "kind": "GREEK_NOT_IN_VERSE",
                            "greek_field": g,
                            "thai_field": kd.get("thai", ""),
                            "tokens": tokens,
                            "why": "Greek token(s) not in the verse's source text (normalized for case/accents), and rationale doesn't flag it as variant/classical/LXX/hapax/morphological.",
                        })
                continue

            if not any(ord(c) > 127 for c in g):
                warns.append({
                    "verse": v["reference"],
                    "kind": "ASCII_LABEL",
                    "greek_field": g,
                    "thai_field": kd.get("thai", ""),
                    "why": "ASCII-only label in greek slot. Legitimate for decision-context tags (e.g., 'Speaker: X to Y') but noisy — worth eyeballing.",
                })

    return (fails, warns, total_kd)


def write_report(slug: str, chapter: int, fails: list, warns: list, total_kd: int) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / f"greek_field_integrity_{slug}_{chapter:02d}.md"

    lines = [
        f"# Greek-field integrity check — {slug} ch. {chapter}",
        "",
        f"- key_decisions entries scanned: **{total_kd}**",
        f"- Hard fails: **{len(fails)}**",
        f"- Warnings: {len(warns)}",
        "",
    ]

    if fails:
        lines.append("## ❌ Hard fails")
        lines.append("")
        for f in fails:
            lines.append(f"### {f['verse']}  ({f['kind']})")
            lines.append(f"- `greek` field: `{f['greek_field']}`")
            lines.append(f"- `thai` field: `{f['thai_field']}`")
            if "tokens" in f:
                lines.append(f"- Greek tokens checked: {f['tokens']}")
            lines.append(f"- Why flagged: {f['why']}")
            lines.append("")

    if warns:
        lines.append("## ⚠ Warnings (non-blocking)")
        lines.append("")
        for w in warns:
            lines.append(f"- **{w['verse']}** ({w['kind']}): `{w['greek_field']}` → `{w['thai_field']}`")
        lines.append("")

    if not fails and not warns:
        lines.append("✅ No integrity issues found.")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def resolve_slug(arg: str) -> str:
    up = arg.upper()
    for slug, code in SLUG_TO_CODE.items():
        if code == up:
            return slug
    return arg.lower()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Book code (LUK) or slug (luke)")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true", help="Scan every chapter of every book")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.all:
        total_fails = 0
        total_warns = 0
        for path in sorted(TRANSLATIONS.glob("*.json")):
            name = path.stem
            if "_" not in name:
                continue
            slug, num = name.rsplit("_", 1)
            try:
                chapter = int(num)
            except ValueError:
                continue
            fails, warns, total_kd = check_chapter(slug, chapter)
            if fails or warns:
                marker = "❌" if fails else "⚠"
                print(f"{marker} {slug}_{chapter:02d}: {len(fails)} fails, {len(warns)} warns (of {total_kd} kd)")
            total_fails += len(fails)
            total_warns += len(warns)
        print()
        print(f"Total hard fails: {total_fails}")
        print(f"Total warnings: {total_warns}")
        return 1 if total_fails else 0

    if not args.book or args.chapter is None:
        parser.error("--book and --chapter required (or use --all)")

    slug = resolve_slug(args.book)
    fails, warns, total_kd = check_chapter(slug, args.chapter)
    report_path = write_report(slug, args.chapter, fails, warns, total_kd)

    if not args.quiet:
        print(f"Wrote {report_path}")
        print(f"  Scanned: {total_kd} key_decisions entries")
        print(f"  Hard fails: {len(fails)}")
        print(f"  Warnings: {len(warns)}")
        for f in fails:
            print(f"  ❌ {f['verse']}: {f['kind']} → {f['greek_field']!r}")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
