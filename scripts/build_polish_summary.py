#!/usr/bin/env python3
"""
Aggregate all per-chapter polish proposals into a single batch-review doc.

Reads:  output/polish_proposals/<book>/<book>_NN.json (sidecars from polish_review)
Writes: docs/NT_V1_POLISH_SUMMARY_<date>.md

The summary groups proposals by issue type for batch review. The reviewer
edits Decision lines in EITHER the per-chapter md files or this summary —
the apply step reads from per-chapter md files (the source of truth for
decisions), so this summary is a navigation aid.
"""
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPOSALS = ROOT / "output" / "polish_proposals"


def book_order_key(slug: str) -> int:
    order = [
        "matthew", "mark", "luke", "john", "acts", "romans", "1corinthians",
        "2corinthians", "galatians", "ephesians", "philippians", "colossians",
        "1thessalonians", "2thessalonians", "1timothy", "2timothy", "titus",
        "philemon", "hebrews", "james", "1peter", "2peter", "1john", "2john",
        "3john", "jude", "revelation",
    ]
    try:
        return order.index(slug)
    except ValueError:
        return 999


def main() -> None:
    if not PROPOSALS.exists():
        print("No proposals directory; run polish_review.py first.")
        return

    by_type = defaultdict(list)
    by_book = defaultdict(list)
    total = 0

    # Match both heuristic sidecars (`<book>_NN.json`) and optimal-equivalence
    # sidecars (`<book>_NN_optimal.json`) so both proposal sets land in the
    # same decision doc.
    sidecars = sorted(set(
        list(PROPOSALS.rglob("*_[0-9][0-9].json"))
        + list(PROPOSALS.rglob("*_[0-9][0-9]_optimal.json"))
    ))
    for sidecar in sidecars:
        try:
            data = json.loads(sidecar.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        slug = data.get("slug", sidecar.parent.name)
        # parse chapter from filename if not in data
        m = re.match(r"^.+_(\d{2})(?:_optimal)?\.json$", sidecar.name)
        chapter = data.get("chapter", int(m.group(1)) if m else 0)
        chapter_ref = data.get("chapter_ref", f"{slug} {chapter}")
        # is_optimal: optimal-equivalence proposals have a `confidence` field;
        # heuristic proposals don't. Used to namespace ids so the two sets
        # don't collide.
        suffix = "_optimal" if "_optimal.json" in sidecar.name else ""
        for i, p in enumerate(data.get("proposals", []), start=1):
            pid = f"{slug}_{chapter:02d}{suffix}_{i:03d}"
            entry = {
                "id": pid,
                "slug": slug,
                "chapter": chapter,
                "chapter_ref": chapter_ref,
                "verse_ref": p["verse_ref"],
                "issue_type": p["issue_type"],
                "confidence": p.get("confidence"),  # optimal-equivalence only
                "current_text": p["current_text"],
                "proposed_text": p["proposed_text"],
                "rationale": p["rationale"],
            }
            by_type[p["issue_type"]].append(entry)
            by_book[slug].append(entry)
            total += 1

    today = date.today().isoformat()
    out_path = ROOT / "docs" / f"NT_V1_POLISH_SUMMARY_{today}.md"

    lines = []
    lines.append(f"# NT v1.0 — Polish Proposals (Decision Doc)")
    lines.append("")
    lines.append(f"**Generated:** {today}")
    lines.append(f"**Total proposals:** {total}")
    lines.append("")
    lines.append("**This is the single decision doc.** For each proposal below, change ")
    lines.append("`**Decision:** pending` to `**Decision:** approve` or `**Decision:** reject`. ")
    lines.append("Save the file. Then run:")
    lines.append("")
    lines.append("```")
    lines.append("python3 scripts/apply_polish_deltas.py --all")
    lines.append("```")
    lines.append("")
    lines.append("Per-chapter files under `output/polish_proposals/<book>/` are auto-generated ")
    lines.append("reference copies — you do NOT need to edit them.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Counts by issue type
    lines.append("## Counts by issue type")
    lines.append("")
    lines.append("| Issue type | Count |")
    lines.append("|---|---:|")
    for itype in sorted(by_type.keys()):
        lines.append(f"| {itype} | {len(by_type[itype])} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")

    # Counts by book
    lines.append("## Counts by book")
    lines.append("")
    lines.append("| Book | Proposals | File |")
    lines.append("|---|---:|---|")
    for slug in sorted(by_book.keys(), key=book_order_key):
        items = by_book[slug]
        chapters = sorted({e["chapter"] for e in items})
        lines.append(
            f"| {slug} | {len(items)} | "
            f"{', '.join(f'`output/polish_proposals/{slug}/{slug}_{c:02d}.md`' for c in chapters)} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # Group by issue type, then list proposals — each with a Decision marker
    for itype in sorted(by_type.keys()):
        lines.append(f"## {itype} ({len(by_type[itype])})")
        lines.append("")
        # Sort by canonical book order, then chapter
        for entry in sorted(by_type[itype], key=lambda e: (book_order_key(e["slug"]),
                                                            e["chapter"], e["verse_ref"])):
            lines.append(f"<!-- POLISH_PROPOSAL id={entry['id']} -->")
            lines.append(f"### {entry['verse_ref']}")
            lines.append("")
            lines.append("**Current:**")
            lines.append("")
            lines.append("> " + entry["current_text"])
            lines.append("")
            lines.append("**Proposed:**")
            lines.append("")
            lines.append("> " + entry["proposed_text"])
            lines.append("")
            lines.append(f"**Why:** {entry['rationale']}")
            lines.append("")
            lines.append("**Decision:** pending")
            lines.append("")
            lines.append("<!-- /POLISH_PROPOSAL -->")
            lines.append("")
            lines.append("---")
            lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} ({out_path.stat().st_size} bytes, {total} proposals)")


if __name__ == "__main__":
    main()
