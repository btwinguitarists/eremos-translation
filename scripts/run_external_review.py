#!/usr/bin/env python3
"""
Run an external AI sanity-check review for a single chapter via Gemini API.

Combines the per-chapter review prompt template (`docs/CHAPTER_REVIEW_PROMPT.md`)
with the chapter's translation JSON (`output/translations/<slug>_NN.json`) and
sends to Gemini. Saves the AI's findings to
`output/check_reports/<slug>_<NN>_external_review.md`.

Usage:
  GEMINI_API_KEY=... python3 scripts/run_external_review.py BOOK CHAPTER [options]

  BOOK     three-letter book code (MAT, MRK, LUK, JHN, ACT, ...)
  CHAPTER  chapter number (e.g., 1)

Options:
  --model NAME       Gemini model (default: gemini-2.5-pro)
  --out PATH         output path; default output/check_reports/<slug>_NN_external_review.md
  --show             also print response to stdout
  --dry-run          assemble prompt + chapter, print size, do not call API

Requires:
  - GEMINI_API_KEY env var (get from https://aistudio.google.com/app/apikey)
  - No external Python packages — uses stdlib urllib

Free tier (Gemini 2.5 Pro): 15 RPM, 1500 RPD, 250K TPM.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
CHECK_REPORTS = ROOT / "output" / "check_reports"
PROMPT_TEMPLATE = ROOT / "docs" / "CHAPTER_REVIEW_PROMPT.md"

BOOKS = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
    "ACT": "acts", "ROM": "romans", "1CO": "1corinthians", "2CO": "2corinthians",
    "GAL": "galatians", "EPH": "ephesians", "PHP": "philippians", "COL": "colossians",
    "1TH": "1thessalonians", "2TH": "2thessalonians", "1TI": "1timothy",
    "2TI": "2timothy", "TIT": "titus", "PHM": "philemon", "HEB": "hebrews",
    "JAS": "james", "1PE": "1peter", "2PE": "2peter", "1JN": "1john",
    "2JN": "2john", "3JN": "3john", "JUD": "jude", "REV": "revelation",
}


def assemble_prompt(book_code, chapter):
    """Build the full prompt: template + chapter JSON appended."""
    if book_code not in BOOKS:
        sys.exit(f"Unknown book code: {book_code}. Known: {sorted(BOOKS)}")
    slug = BOOKS[book_code]
    chapter_path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not chapter_path.is_file():
        sys.exit(f"Chapter file not found: {chapter_path}")

    if not PROMPT_TEMPLATE.is_file():
        sys.exit(f"Prompt template not found: {PROMPT_TEMPLATE}")

    template = PROMPT_TEMPLATE.read_text()
    # Strip the "How to use" front-matter (everything before the first --- divider).
    if "\n---\n" in template:
        prompt_only = template.split("\n---\n", 1)[1].lstrip()
    else:
        prompt_only = template

    chapter_json = chapter_path.read_text()

    full_prompt = (
        prompt_only.rstrip()
        + "\n\n---\n\n"
        + f"## Chapter under review: {book_code} {chapter}\n\n"
        + "```json\n"
        + chapter_json.rstrip()
        + "\n```\n"
    )
    return slug, chapter_path, full_prompt


def call_gemini(prompt, model, api_key, timeout=180):
    """POST the prompt to Gemini API; return the assistant's text response."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
        f":generateContent?key={api_key}"
    )
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            # Gemini 2.5 models use "thinking tokens" that count against the
            # output budget; keep this generous so visible output isn't
            # truncated. Free-tier daily quota covers this comfortably.
            "maxOutputTokens": 32768,
        },
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"Gemini API HTTP {e.code}: {body[:1000]}")
    except urllib.error.URLError as e:
        sys.exit(f"Gemini API connection error: {e}")

    candidates = payload.get("candidates", [])
    if not candidates:
        sys.exit(f"Gemini API returned no candidates. Full payload:\n{json.dumps(payload, indent=2)[:1000]}")
    parts = candidates[0].get("content", {}).get("parts", [])
    finish = candidates[0].get("finishReason", "?")
    if not parts:
        sys.exit(f"Gemini API returned no content parts (finishReason={finish}). Payload: {json.dumps(payload)[:500]}")
    text = parts[0].get("text", "")
    if finish != "STOP":
        print(f"  WARNING: finishReason={finish} (response may be truncated or filtered)", file=sys.stderr)
    return text


def main():
    parser = argparse.ArgumentParser(description="Run external AI review for one chapter via Gemini.")
    parser.add_argument("book", help="three-letter book code")
    parser.add_argument("chapter", type=int, help="chapter number")
    parser.add_argument("--model", default="gemini-2.5-pro", help="Gemini model (default: gemini-2.5-pro)")
    parser.add_argument("--out", help="output path")
    parser.add_argument("--show", action="store_true", help="also print response to stdout")
    parser.add_argument("--dry-run", action="store_true", help="assemble + print sizes, do not call API")
    args = parser.parse_args()

    book_code = args.book.upper()
    slug, chapter_path, prompt = assemble_prompt(book_code, args.chapter)

    print(f"Chapter: {chapter_path.name}")
    print(f"Prompt size: {len(prompt):,} chars")

    if args.dry_run:
        print("--dry-run: not calling API. First 500 chars of prompt:\n")
        print(prompt[:500])
        return

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY env var not set. Get a key at https://aistudio.google.com/app/apikey")

    print(f"Calling {args.model} ...")
    response_text = call_gemini(prompt, args.model, api_key)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = CHECK_REPORTS / f"{slug}_{args.chapter:02d}_external_review.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    header = (
        f"# External review — {book_code} {args.chapter}\n\n"
        f"**Reviewer:** {args.model}\n"
        f"**Run at:** {datetime.now().isoformat(timespec='seconds')}\n"
        f"**Source:** `output/translations/{slug}_{args.chapter:02d}.json` "
        f"(via `docs/CHAPTER_REVIEW_PROMPT.md`)\n\n"
        f"---\n\n"
    )
    out_path.write_text(header + response_text.rstrip() + "\n")

    print(f"Wrote {out_path}")
    print(f"Response: {len(response_text):,} chars")
    if args.show:
        print("\n" + "=" * 70)
        print(response_text)


if __name__ == "__main__":
    main()
