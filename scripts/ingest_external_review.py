#!/usr/bin/env python3
"""
Ingest Cowork-dropped external-AI raw replies into per-book response files.

Cowork (browser agent) saves one `<CODE>_raw.md` per reviewed book into
`docs/end_of_book/_external_inbox/`, with the model replies under `## GEMINI`,
`## GROK`, and `## CHATGPT` headings. This script:

  1. Splits each raw file on those headings.
  2. Writes `docs/end_of_book/<slug>/external_review_response_<CODE>_<DATE>.md`
     (the presence of a *response* file is what marks a book "done" for
     `external_review_status.py`).
  3. Moves the consumed raw into `_external_inbox/_processed/` (idempotent).
  4. Prints a short summary so the main session knows what landed.

Claude Code then reads the response files and decides what (if anything) to act
on — this script does NOT auto-apply any change to the translation.

Usage:
  python3 scripts/ingest_external_review.py [--date YYYY-MM-DD] [--keep-raw]
"""
import argparse, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "docs" / "end_of_book" / "_external_inbox"
PROCESSED = INBOX / "_processed"
EOB = ROOT / "docs" / "end_of_book"

# CODE -> slug, mirrors build_external_review_packet.BOOKS (kept local to avoid import cost)
try:
    sys.path.insert(0, str(ROOT / "scripts"))
    from build_external_review_packet import BOOKS  # type: ignore
    CODE2SLUG = {c: s for c, (s, _n) in BOOKS.items()}
except Exception:
    CODE2SLUG = {}

HEADING = re.compile(r"^##\s+(GEMINI|GROK|CHATGPT)\s*$", re.M)


def split_models(body: str):
    """Return {model: text} from a raw file body."""
    parts = {}
    matches = list(HEADING.finditer(body))
    for i, m in enumerate(matches):
        model = m.group(1).upper()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        parts[model] = body[start:end].strip()
    return parts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="date stamp for response files (YYYY-MM-DD); required for deterministic naming")
    ap.add_argument("--keep-raw", action="store_true", help="do not move raw into _processed/")
    a = ap.parse_args()
    if not a.date:
        sys.exit("Pass --date YYYY-MM-DD (the scheduled job supplies today's date).")

    raws = sorted(p for p in INBOX.glob("*_raw.md") if not p.name.startswith("_"))
    if not raws:
        print("No *_raw.md in inbox — nothing to ingest.")
        return
    PROCESSED.mkdir(exist_ok=True)
    ingested = []
    for raw in raws:
        code = raw.name[:-len("_raw.md")].upper()
        slug = CODE2SLUG.get(code)
        if not slug:
            print(f"  ! {raw.name}: unknown CODE '{code}' — skipping (add to BOOKS map).")
            continue
        body = raw.read_text()
        models = split_models(body)
        usable = {k: v for k, v in models.items() if v and "(skipped" not in v.lower() and "(no usable" not in v.lower()}
        book_dir = EOB / slug
        book_dir.mkdir(parents=True, exist_ok=True)
        out = book_dir / f"external_review_response_{code}_{a.date}.md"
        header = (
            f"# {code} — external AI review responses (ingested {a.date})\n\n"
            f"Source: Cowork web ({', '.join(models.keys()) or 'none'}). "
            f"Raw: `_external_inbox/{raw.name}`.\n\n"
            f"> Ingested verbatim. The main session reviews these and decides what to act on.\n\n"
        )
        sections = []
        for model in ("GEMINI", "GROK", "CHATGPT"):
            if model in models:
                sections.append(f"## {model}\n\n{models[model]}\n")
        out.write_text(header + "\n".join(sections))
        if not a.keep_raw:
            shutil.move(str(raw), str(PROCESSED / raw.name))
        ingested.append((code, list(models.keys()), len(usable)))
        print(f"  ✓ {code} → {out.relative_to(ROOT)}  (models: {', '.join(models.keys()) or 'none'}; usable: {len(usable)})")

    print(f"\nIngested {len(ingested)} book(s). Re-run external_review_status.py to refresh the queue.")


if __name__ == "__main__":
    main()
