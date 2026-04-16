#!/usr/bin/env python3
"""
Render a translated chapter as readable markdown for human review.

Output: docs/mark_XX_review.md with parallel Greek / BSB English / Thai,
plus translator notes and key decisions inline.

Usage:
  python3 scripts/render_markdown.py --chapter 1
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS_DIR = ROOT / "output" / "translations"
DOCS_DIR = ROOT / "docs"


def render_chapter(chapter: int) -> str:
    in_path = TRANSLATIONS_DIR / f"mark_{chapter:02d}.json"
    if not in_path.exists():
        raise SystemExit(f"No translation file at {in_path}. Run translate_mark.py first.")
    with open(in_path, encoding="utf-8") as f:
        verses = json.load(f)

    lines = []
    lines.append(f"# Mark {chapter} — AI Translation Draft (Eremos Translation)")
    lines.append("")
    lines.append("Open-source (CC0) Thai Bible translation from SBLGNT Greek, via MACULA morphological analysis, with BSB English as reference.")
    lines.append("")
    lines.append("---")
    lines.append("")

    total_variants = 0
    total_hapax = 0

    for v in verses:
        ref = v["reference"]
        greek = v.get("greek", "")
        english = v.get("bsb_english", "")
        t = v.get("translation", {})
        thai = t.get("thai", "")
        literal = t.get("thai_literal", "")
        decisions = t.get("key_decisions", [])
        notes = t.get("notes", "")

        if notes:
            if "VARIANT" in notes.upper():
                total_variants += 1
            if "HAPAX" in notes.upper():
                total_hapax += 1

        lines.append(f"## {ref}")
        lines.append("")
        lines.append(f"**GK:** {greek}")
        lines.append("")
        lines.append(f"**EN (BSB):** {english}")
        lines.append("")
        lines.append(f"**TH:** {thai}")
        lines.append("")
        if literal and literal != thai:
            lines.append(f"*Literal:* {literal}")
            lines.append("")

        if decisions:
            lines.append("<details>")
            lines.append("<summary>Translation decisions</summary>")
            lines.append("")
            for d in decisions:
                g = d.get("greek", "")
                th = d.get("thai", "")
                r = d.get("rationale", "")
                lines.append(f"- **{g}** → **{th}** — {r}")
            lines.append("")
            lines.append("</details>")
            lines.append("")

        if notes:
            lines.append(f"> **Notes:** {notes}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Summary at top
    header_summary = [
        f"**Summary:** {len(verses)} verses · {total_variants} textual variants flagged · {total_hapax} hapax-containing verses",
        "",
    ]
    lines = lines[:3] + header_summary + lines[3:]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", type=int, default=1)
    args = parser.parse_args()

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    out = DOCS_DIR / f"mark_{args.chapter:02d}_review.md"
    content = render_chapter(args.chapter)
    out.write_text(content, encoding="utf-8")
    print(f"Rendered: {out}")
    print(f"  Size: {len(content):,} chars")


if __name__ == "__main__":
    main()
