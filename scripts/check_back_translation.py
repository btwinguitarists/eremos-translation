#!/usr/bin/env python3
"""
Back-translation check: Thai → English via Claude, diffed against BSB.

The purpose is NOT to match BSB exactly (our Thai is independent). The purpose
is to catch:
  - Meaning loss (the back-translation says something different from the source Greek intent)
  - Unintended divergence (diverges from BSB but no documented rationale for why)
  - Added or missing content

For each verse, the script:
  1. Asks Claude to translate our Thai back to English, forbidding reference to any Bible text
  2. Computes a simple similarity score against BSB
  3. Flags verses where divergence is large AND no documented decision/note explains it

Requires: ANTHROPIC_API_KEY environment variable.

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 scripts/check_back_translation.py --book 1TI --chapter 3
  python3 scripts/check_back_translation.py --book mark --chapter 1 --limit 5
"""
import argparse
import difflib
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

MODEL = "claude-sonnet-4-5"

BACK_TRANS_SYSTEM = """You are a literal back-translator. Given a Thai sentence, produce its English meaning as literally as possible. Rules:

1. Do NOT consult the Bible, BSB, or any known Bible translation. Work only from the Thai input.
2. Do NOT paraphrase for style. Render the Thai sense directly in English.
3. Preserve the Thai's honorific register (e.g., ทรง → use passive or formal English for divine subjects).
4. Do NOT add theological interpretation — if the Thai is ambiguous, keep the English ambiguous.
5. Output ONLY the English back-translation, one line, no preamble, no commentary."""


def similarity(a: str, b: str) -> float:
    """Simple sequence-ratio similarity 0..1."""
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def back_translate_verse(client, thai: str, retries: int = 2) -> str:
    for attempt in range(retries + 1):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=500,
                system=BACK_TRANS_SYSTEM,
                messages=[{"role": "user", "content": f"Thai: {thai}\n\nEnglish back-translation (one line):"}],
            )
            return response.content[0].text.strip().split("\n")[0]
        except Exception as e:
            if attempt < retries:
                time.sleep(3)
                continue
            return f"[ERROR: {e}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--limit", type=int, help="Only process first N verses (testing)")
    parser.add_argument("--threshold", type=float, default=0.35,
                        help="Below this similarity, flag for review (default 0.35)")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set. Back-translation requires Claude API.")
        print("Skipping. To enable, export ANTHROPIC_API_KEY and re-run.")
        # Write a sentinel report so the orchestrator knows this step was skipped
        REPORTS.mkdir(parents=True, exist_ok=True)
        slug = args.book.lower()
        out_path = REPORTS / f"back_translation_{slug}_{args.chapter:02d}.md"
        out_path.write_text(
            f"# Back-translation check — {slug} ch. {args.chapter}\n\n"
            "⏭ **Skipped** — ANTHROPIC_API_KEY not set in environment.\n\n"
            "To run: `export ANTHROPIC_API_KEY=sk-ant-...` and rerun the check.\n",
            encoding="utf-8"
        )
        return 0

    try:
        import anthropic
    except ImportError:
        print("anthropic SDK missing. Install: pip3 install anthropic --break-system-packages")
        return 1

    slug = args.book.lower()
    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"No translation file at {translation_file}")
        return 1

    with open(translation_file, encoding="utf-8") as f:
        verses = json.load(f)

    if args.limit:
        verses = verses[: args.limit]

    client = anthropic.Anthropic()
    results = []

    print(f"Back-translating {len(verses)} verse(s)...")
    for i, v in enumerate(verses, 1):
        thai = (v.get("translation", {}) or {}).get("thai", "") or ""
        bsb = v.get("bsb_english", "") or ""
        if not thai:
            continue

        print(f"  [{i}/{len(verses)}] {v['reference']}...", end="", flush=True)
        t0 = time.time()
        bt = back_translate_verse(client, thai)
        sim = similarity(bt, bsb)
        print(f" sim={sim:.2f} ({time.time()-t0:.1f}s)")

        has_rationale = bool(
            (v.get("translation", {}) or {}).get("notes")
            or (v.get("translation", {}) or {}).get("key_decisions")
        )

        results.append({
            "verse": v["reference"],
            "thai": thai,
            "back_translation": bt,
            "bsb_english": bsb,
            "similarity": sim,
            "has_rationale": has_rationale,
            "flagged": sim < args.threshold and not has_rationale,
        })

    flagged = [r for r in results if r["flagged"]]
    low_sim_with_rationale = [r for r in results if r["similarity"] < args.threshold and r["has_rationale"]]

    md_lines = [
        f"# Back-translation check — {slug} ch. {args.chapter}",
        "",
        f"Model: `{MODEL}` | Threshold: {args.threshold}",
        "",
        f"- Verses checked: {len(results)}",
        f"- Flagged (low similarity AND no rationale): **{len(flagged)}**",
        f"- Low similarity but with rationale: {len(low_sim_with_rationale)}",
        f"- Acceptable similarity: {len(results) - len(flagged) - len(low_sim_with_rationale)}",
        "",
    ]

    if flagged:
        md_lines.append("## ⚠ Flagged verses")
        md_lines.append("")
        for r in flagged:
            md_lines.append(f"### {r['verse']}  (sim={r['similarity']:.2f})")
            md_lines.append(f"- **Thai**:    {r['thai']}")
            md_lines.append(f"- **Back-EN**: {r['back_translation']}")
            md_lines.append(f"- **BSB**:     {r['bsb_english']}")
            md_lines.append("")

    if low_sim_with_rationale:
        md_lines.append("## ℹ Low similarity — has documented rationale")
        md_lines.append("")
        for r in low_sim_with_rationale:
            md_lines.append(f"- **{r['verse']}** (sim={r['similarity']:.2f}) — rationale present, review if still appropriate")
            md_lines.append(f"  - Thai: {r['thai']}")
            md_lines.append(f"  - Back: {r['back_translation']}")
            md_lines.append(f"  - BSB:  {r['bsb_english']}")
        md_lines.append("")

    md = "\n".join(md_lines)
    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / f"back_translation_{slug}_{args.chapter:02d}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"\nWrote {out_path}")
        print(f"  Flagged: {len(flagged)}")

    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
