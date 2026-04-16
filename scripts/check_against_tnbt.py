#!/usr/bin/env python3
"""
Structural comparison against TNBT (Thai New Buddhist Translation, CC-BY-SA).

TNBT is a legitimately open-licensed Thai NT with a different target audience
(Thai Buddhists). Vocabulary divergence is EXPECTED — TNBT uses Buddhist
register (พระศรีอาริย์ instead of พระคริสต์, พิธีมุดน้ำ instead of บัพติศมา, etc.).
This check looks for STRUCTURAL signals, not vocabulary matching.

Signals flagged:
  - Sentence count mismatch (our verse has N sentences, TNBT has M; large delta → investigate)
  - Significant length delta (> ±60% of character count)
  - Missing verse on either side

Usage:
  python3 scripts/check_against_tnbt.py --book 1TI --chapter 3
  python3 scripts/check_against_tnbt.py --book mrk --chapter 1
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
TNBT_DIR = ROOT / "sources" / "TNBT" / "tx"
REPORTS = ROOT / "output" / "check_reports"

# Map book slug to TNBT 3-letter code
SLUG_TO_TNBT = {
    "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN",
    "acts": "ACT", "romans": "ROM", "1corinthians": "1CO", "2corinthians": "2CO",
    "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
    "1thessalonians": "1TH", "2thessalonians": "2TH", "1timothy": "1TI", "2timothy": "2TI",
    "titus": "TIT", "philemon": "PHM", "hebrews": "HEB", "james": "JAS",
    "1peter": "1PE", "2peter": "2PE", "1john": "1JN", "2john": "2JN",
    "3john": "3JN", "jude": "JUD", "revelation": "REV",
}


def parse_tnbt(book_code: str, target_chapter: int) -> dict[int, str]:
    """Parse TNBT .tx file, return {verse_num: text} for the target chapter.

    TNBT format:
      - First 3 lines: metadata
      - Lines with "_" prefix: section headings (skip)
      - Standalone numeric line = chapter marker
      - Body lines contain inline verse markers: "1 text... 2 text..."
    """
    tx_path = TNBT_DIR / f"{book_code}.tx"
    if not tx_path.exists():
        return {}

    verses = {}
    current_chapter = 0
    current_verse = 0
    current_text_parts: list[str] = []

    def flush():
        nonlocal current_verse, current_text_parts
        if current_chapter == target_chapter and current_verse > 0 and current_text_parts:
            text = " ".join(current_text_parts).strip()
            if current_verse not in verses:
                verses[current_verse] = text
            else:
                verses[current_verse] += " " + text
        current_text_parts = []

    with open(tx_path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[3:]:  # skip 3-line header
        line = line.rstrip("\n").strip()
        if not line:
            continue
        if line.startswith("_"):
            continue  # section heading
        # Standalone numeric line = chapter marker
        if re.fullmatch(r"\d+", line):
            flush()
            current_chapter = int(line)
            current_verse = 0
            continue
        if current_chapter != target_chapter:
            continue
        # Body line with inline verse markers: "1 text 2 text 3 text..."
        # Use finditer to locate each verse marker, then slice between them.
        # Marker = standalone integer preceded by start-of-string or whitespace,
        # followed by whitespace.
        pattern = re.compile(r"(?:^|\s)(\d+)(?=\s)")
        matches = list(pattern.finditer(line))
        if not matches:
            if current_verse > 0:
                current_text_parts.append(line)
            continue

        # Leading text (before first marker) belongs to previous verse
        first_start = matches[0].start()
        leading = line[:first_start].strip()
        if leading and current_verse > 0:
            current_text_parts.append(leading)

        for i, m in enumerate(matches):
            flush()
            current_verse = int(m.group(1))
            text_start = m.end()
            text_end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            current_text_parts.append(line[text_start:text_end].strip())

    flush()
    return verses


def sentence_count(s: str) -> int:
    """Rough sentence count using Thai and Western punctuation.

    Thai texts often don't use '.' but DO use quoted speech (ก่อน...ว่า), relative
    connectives, and paragraph boundaries. This is a rough estimate — good enough
    for "does the structure look similar" signaling.
    """
    if not s:
        return 0
    # Normalize quotes and count major clause-break punctuation.
    breaks = re.findall(r"[.!?]|[·]|[\u0e5a\u0e5b]|—|\"|'|“|”|‘|’", s)
    # Count breaks that look like sentence boundaries; minimum of 1 if any text
    return max(1, len([b for b in breaks if b in ".!?·"]) or 1)


def compare(eremos_verses: list[dict], tnbt_verses: dict[int, str]) -> list[dict]:
    flags = []
    for v in eremos_verses:
        verse_num = v["verse"]
        eremos_thai = (v.get("translation", {}) or {}).get("thai", "") or ""
        tnbt_thai = tnbt_verses.get(verse_num, "")

        entry = {
            "verse": v["reference"],
            "verse_num": verse_num,
            "eremos_thai": eremos_thai,
            "tnbt_thai": tnbt_thai,
            "signals": [],
        }

        if not eremos_thai:
            entry["signals"].append("Eremos Thai missing")
        if not tnbt_thai:
            entry["signals"].append("TNBT verse not found")

        if eremos_thai and tnbt_thai:
            e_len = len(eremos_thai)
            t_len = len(tnbt_thai)
            ratio = e_len / max(1, t_len)
            if ratio < 0.4 or ratio > 1.75:
                entry["signals"].append(
                    f"length ratio {ratio:.2f} (Eremos {e_len} vs TNBT {t_len} chars)"
                )

            e_sents = sentence_count(eremos_thai)
            t_sents = sentence_count(tnbt_thai)
            if abs(e_sents - t_sents) >= 2:
                entry["signals"].append(f"sentence count {e_sents} vs {t_sents}")

        if entry["signals"]:
            flags.append(entry)

    return flags


def render_markdown(flags: list[dict], scope: str, total_verses: int) -> str:
    lines = [
        f"# TNBT structural comparison — {scope}",
        "",
        "_TNBT uses Buddhist vocabulary register. Divergent wording is expected and NOT a flag._",
        "_Only structural signals (length ratio, sentence count, missing verses) are surfaced here._",
        "",
        f"Verses with structural signals: **{len(flags)} / {total_verses}**",
        "",
    ]

    if not flags:
        lines.append("✅ No structural divergences detected.")
        return "\n".join(lines)

    lines.append("## Flagged verses")
    lines.append("")
    for f in flags:
        lines.append(f"### {f['verse']}")
        lines.append("")
        lines.append(f"- **Signals**: {'; '.join(f['signals'])}")
        if f["eremos_thai"]:
            lines.append(f"- **Eremos**: {f['eremos_thai']}")
        if f["tnbt_thai"]:
            lines.append(f"- **TNBT**:   {f['tnbt_thai']}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True, help="Book slug (e.g., mark, 1timothy)")
    parser.add_argument("--chapter", type=int, required=True, help="Chapter number")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    slug = args.book.lower()
    tnbt_code = SLUG_TO_TNBT.get(slug)
    if not tnbt_code:
        print(f"No TNBT code known for book slug '{slug}'")
        return 1

    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"No translation file at {translation_file}")
        return 1

    with open(translation_file, encoding="utf-8") as f:
        eremos = json.load(f)

    tnbt = parse_tnbt(tnbt_code, args.chapter)
    if not tnbt:
        print(f"Warning: could not parse TNBT {tnbt_code} ch.{args.chapter}")

    flags = compare(eremos, tnbt)
    scope = f"{slug} ch. {args.chapter}"
    md = render_markdown(flags, scope, len(eremos))

    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / f"tnbt_comparison_{slug}_{args.chapter:02d}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")
        print(f"  Flagged: {len(flags)} / {len(eremos)} verses")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
