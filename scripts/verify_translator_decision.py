#!/usr/bin/env python3
"""
Corpus-verification for translator-decisions docs.

Added 2026-05-16 after the Leviticus end-of-book audit surfaced two doc-vs-corpus
drift incidents (sacrificial_vocabulary §5 locked `ลบบาป` while 144 occurrences
of `ลบมลทินบาป` had already shipped; goel_kinsman_redeemer locked
`ผู้ไถ่ที่เป็นญาติ` while neither Ruth nor Leviticus uses that form).

Rule: before any translator-decisions doc is marked LOCKED, run this script
against the doc and paste the output as a "Corpus-verified shipped forms"
section. This prevents docs from locking forms that the shipped text does not
use.

Two modes:

  --doc <path-to-md>
      Parse the doc for tables under headings matching /lock|locked|thai/i.
      Extract Thai locked forms from those tables. Grep shipped corpus.
      Report per-form: occurrences, books covered, sibling forms found.

  --form <thai-string> [--form <other> ...]
      Quick ad-hoc lookup. Greps shipped translations for the given Thai
      string(s) and reports per-book counts. Useful when drafting a doc
      before the lock table is finalized.

Output: a markdown section ready to paste into the doc, plus a
machine-readable JSON summary on stderr (one line, for tooling).

Usage:

  python3 scripts/verify_translator_decision.py --doc docs/translator_decisions/sacrificial_vocabulary_2026-05.md
  python3 scripts/verify_translator_decision.py --form 'ลบมลทินบาป' --form 'ลบบาป'
  python3 scripts/verify_translator_decision.py --form 'ญาติผู้ไถ่' --form 'ผู้ไถ่ที่เป็นญาติ'

Exit code: 0 always (this is informational; reviewer decides how to act).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS_DIR = REPO_ROOT / "output" / "translations"


def list_translation_files() -> list[Path]:
    if not TRANSLATIONS_DIR.exists():
        return []
    return sorted(TRANSLATIONS_DIR.glob("*.json"))


def book_slug_from_filename(p: Path) -> str:
    # e.g. leviticus_25.json -> leviticus
    stem = p.stem
    return stem.rsplit("_", 1)[0] if "_" in stem else stem


def search_form_in_corpus(form: str) -> dict:
    """Return {'total': N, 'by_book': {slug: count}, 'sample_refs': [...]}"""
    by_book: dict[str, int] = defaultdict(int)
    sample_refs: list[str] = []
    total = 0
    for p in list_translation_files():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        book = book_slug_from_filename(p)
        for v in data:
            if not isinstance(v, dict):
                continue
            thai = (v.get("translation") or {}).get("thai") or ""
            if form in thai:
                total += 1
                by_book[book] += 1
                if len(sample_refs) < 5:
                    sample_refs.append(v.get("reference") or f"{book} ?:?")
    return {
        "form": form,
        "total": total,
        "by_book": dict(by_book),
        "sample_refs": sample_refs,
    }


def extract_thai_locks_from_doc(doc_path: Path) -> list[str]:
    """
    Heuristic: walk the doc, find markdown tables, and pull Thai-script cells.
    Returns a deduplicated list of Thai locked forms found in tables.

    A 'Thai cell' is any pipe-delimited cell that contains at least one Thai
    character (U+0E00-U+0E7F) and isn't a header/separator row. We don't try
    to be perfect — the goal is to surface candidates for the reviewer to
    paste into --form runs if the heuristic misses something.
    """
    if not doc_path.exists():
        return []
    text = doc_path.read_text(encoding="utf-8")
    thai_re = re.compile(r"[฀-๿]")
    bold_strip = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
    forms: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if "|" not in line:
            continue
        if re.fullmatch(r"\s*\|?(\s*:?-+:?\s*\|)+\s*", line):
            continue  # separator row
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        for cell in cells:
            cell = bold_strip.sub(r"\1", cell).strip()
            # Strip leading/trailing punctuation likely from markdown
            cell = cell.strip("` *")
            if not cell:
                continue
            # Require Thai chars + skip obvious English-only cells
            if not thai_re.search(cell):
                continue
            # Skip cells that are mostly Latin (e.g. "ekklesia / ที่ประชุม" — keep both)
            # Split on common dividers and keep each Thai sub-cell
            for sub in re.split(r"\s*[/;,]\s*", cell):
                sub = sub.strip("()` *").strip()
                if sub and thai_re.search(sub) and sub not in seen:
                    seen.add(sub)
                    forms.append(sub)
    return forms


def render_markdown_section(results: list[dict], heading: str | None = None) -> str:
    lines = []
    if heading:
        lines.append(f"## {heading}")
        lines.append("")
    lines.append("Auto-generated by `scripts/verify_translator_decision.py`. Re-run before locking.")
    lines.append("")
    lines.append("| Locked Thai | Total occurrences | Books | Sample refs |")
    lines.append("|---|---:|---|---|")
    for r in results:
        books = ", ".join(f"{k} ({v})" for k, v in sorted(r["by_book"].items(), key=lambda kv: -kv[1]))
        if not books:
            books = "—"
        refs = "; ".join(r["sample_refs"]) if r["sample_refs"] else "—"
        lines.append(f"| `{r['form']}` | {r['total']} | {books} | {refs} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--doc", type=Path, help="Path to a translator-decisions markdown doc")
    ap.add_argument("--form", action="append", default=[], help="Ad-hoc Thai form to grep (repeatable)")
    ap.add_argument("--heading", default="Corpus-verified shipped forms (2026-05-16 pre-lock rule)",
                    help="Heading for the rendered markdown section")
    ap.add_argument("--json", action="store_true", help="Emit JSON to stdout instead of markdown")
    args = ap.parse_args()

    forms: list[str] = list(args.form)
    if args.doc:
        extracted = extract_thai_locks_from_doc(args.doc)
        if extracted:
            print(f"[verify] extracted {len(extracted)} candidate Thai form(s) from {args.doc.name}", file=sys.stderr)
        forms.extend(f for f in extracted if f not in forms)

    if not forms:
        print("usage: --doc <path.md> OR --form <thai> [--form ...]", file=sys.stderr)
        return 2

    results = [search_form_in_corpus(f) for f in forms]

    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        print(render_markdown_section(results, heading=args.heading))

    # one-line machine-readable summary on stderr
    summary = {r["form"]: r["total"] for r in results}
    print(f"[verify] summary: {json.dumps(summary, ensure_ascii=False)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
