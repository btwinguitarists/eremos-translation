#!/usr/bin/env python3
"""
audit_items_to_yaml — convert end-of-book audit items to per-question YAML.

Parses `docs/end_of_book/<slug>/external_review_items_<BOOK>.md` (the
handwritten / agent-generated items doc — one `## Item A — ...` block per
review-worthy editorial decision) and emits one YAML file per item matching
the format of `EremosVercel2/shared/review-questions/<id>.yml`.

This eliminates the manual TS-file-edit step that landed in PR #403 ("add 16
review questions from JHN+GAL audits") — the audit agent now produces the
items doc, runs this script, and opens a PR adding the YAMLs to the form.

Usage:
    python3 scripts/audit_items_to_yaml.py BOOK [--items PATH] [--out DIR]

    BOOK     three-letter book code (JHN, GAL, 1TH, ...)
    --items  path to the items doc; default
             docs/end_of_book/<slug>/external_review_items_<BOOK>.md
    --out    output directory; default
             output/review_questions_<slug>/

Each emitted YAML has:
    id          — heuristic from book + verse refs in the title or item letter
    tier        — B by default (theological items); A for items the title flags
                  as "register" / "naturalness" / "Thai-ear"
    roles       — derived from tier (per shared/translation-review-questions.ts)
    kind        — "text" (open-ended; the audit items rarely have enumerable
                  answer options out of the box — reviewers respond in prose)
    topic       — first sentence of the title block
    body        — full item content (the analysis paragraphs + verse evidence)
                  with the trailing `**Question(s):**` block stripped
    question    — extracted from `**Question:**` / `**Two questions:**` block

The script emits English content only — `th:` fields contain a placeholder
("__TODO_TH__") that the audit agent (or a Thai-translation pass) fills in
before the PR is opened. The YAML loads at build time via
`EremosVercel2/script/build-review-questions.ts` only after the placeholders
are replaced.

Exit codes:
    0 — items doc parsed; YAML files written
    1 — items doc missing or unreadable
    2 — invalid arguments
"""
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Slug map (mirrors detect_book_complete.py / build_external_review_packet.py)
BOOK_SLUGS = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
    "ACT": "acts", "ROM": "romans", "1CO": "1corinthians", "2CO": "2corinthians",
    "GAL": "galatians", "EPH": "ephesians", "PHP": "philippians", "COL": "colossians",
    "1TH": "1thessalonians", "2TH": "2thessalonians", "1TI": "1timothy",
    "2TI": "2timothy", "TIT": "titus", "PHM": "philemon", "HEB": "hebrews",
    "JAS": "james", "1PE": "1peter", "2PE": "2peter", "1JN": "1john",
    "2JN": "2john", "3JN": "3john", "JUD": "jude", "REV": "revelation",
    # OT books — added as the OT pilot ships
    "RUT": "ruth",
    "JON": "jonah",
    "GEN": "genesis",
}

TODO_TH = "__TODO_TH__"

# Tier-A topic-word hints (reader-naturalness / register questions; everything
# else defaults to tier B = theological).
TIER_A_HINTS = (
    "naturalness", "register", "honorific", "rhythm", "read aloud",
    "read-aloud", "intimate-dialogue", "thai-ear", "thai ear",
)

ITEM_HEADING_RE = re.compile(r"^##\s+Item\s+([A-Z])\s+—\s+(.+?)$", re.MULTILINE)
# Matches the `**Question:**` / `**Two questions:**` / `**Three questions:**`
# trailing markers used by every items doc to date. The colon is INSIDE the
# bold markup in every existing example, so the regex requires it.
QUESTION_BLOCK_RE = re.compile(
    r"\n\*\*(?:Question|Two\s+questions|Three\s+questions|Questions)\s*:\*\*\s*",
    re.IGNORECASE,
)
ITEM_SEPARATOR_RE = re.compile(r"\n+---\s*\n*$")
VERSE_REF_RE = re.compile(
    r"(?:JHN|MAT|MRK|LUK|ACT|ROM|1CO|2CO|GAL|EPH|PHP|COL|1TH|2TH|1TI|2TI|"
    r"TIT|PHM|HEB|JAS|1PE|2PE|1JN|2JN|3JN|JUD|REV|RUT|JON|GEN)\s*(\d+):(\d+)"
)


@dataclass
class Item:
    letter: str          # "A", "B", ...
    title: str           # text after "## Item X — "
    body: str            # full content minus the trailing question block
    question: str        # everything after the question marker
    book: str            # uppercase book code, from CLI


def parse_items(text: str, book: str) -> list[Item]:
    items: list[Item] = []
    matches = list(ITEM_HEADING_RE.finditer(text))
    if not matches:
        return items

    for i, m in enumerate(matches):
        letter = m.group(1)
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        # Strip trailing `---` separator (between items) before parsing
        block = ITEM_SEPARATOR_RE.sub("", block).rstrip()

        q_match = QUESTION_BLOCK_RE.search(block)
        if q_match:
            body = block[:q_match.start()].strip()
            question = block[q_match.end():].strip()
            # Strip any trailing `---` left in the question text
            question = ITEM_SEPARATOR_RE.sub("", question).strip()
        else:
            body = block.strip()
            question = ""
        items.append(Item(letter=letter, title=title, body=body,
                          question=question, book=book))
    return items


def derive_id(item: Item) -> str:
    """Derive a YAML filename / id for an item.

    Heuristic:
      - tier letter (A or B; from infer_tier)
      - book code (uppercase, no zero-pad)
      - first verse reference in the title or first 200 chars of body
        (e.g., "JHN3_11"); if no specific verse, use letter as suffix
      - topic slug — take the most distinctive word from the title
    """
    tier = infer_tier(item)
    haystack = item.title + "\n" + item.body[:300]
    vm = VERSE_REF_RE.search(haystack)
    if vm:
        loc = f"{item.book}{vm.group(1)}_{vm.group(2)}"
    else:
        loc = f"{item.book}_{item.letter}"

    # Topic slug — take the first non-trivial ASCII word from the title.
    # Greek letters are intentionally excluded so the slug stays filename-safe.
    title_words = re.findall(r"[A-Za-z]{3,}", item.title)
    skip = {
        "the", "and", "with", "from", "into", "for", "vs", "on", "of",
        "—", "but", "drift", "variant", "split", "rendering", "reading",
        "John", "Mark", "Matthew", "Luke", "Acts", "Galatians", "Thessalonians",
        "Romans", "Corinthians", "Ephesians", "Philippians", "Colossians",
        "Timothy", "Titus", "Hebrews", "James", "Peter", "Jude", "Revelation",
        "Item", "SBLGNT", "Ruth",
    }
    # Also skip book codes (JHN, MAT, etc.) so a title like
    # "JHN 3:11 ἀμὴν ἀμὴν drift" picks "drift" rather than "JHN".
    skip_codes = set(BOOK_SLUGS.keys())
    topic = next(
        (
            w.lower() for w in title_words
            if w not in skip and w.upper() not in skip_codes and not w.isdigit()
        ),
        f"item{item.letter.lower()}",
    )
    # Strip diacritics / non-ASCII for filenames (keep Greek-letter source words
    # only as the origin; the slug is ASCII-only)
    topic = re.sub(r"[^a-z0-9]", "", topic)
    if not topic:
        topic = f"item{item.letter.lower()}"

    return f"{tier}_{loc}_{topic}"


def infer_tier(item: Item) -> str:
    text = (item.title + " " + item.body[:500]).lower()
    if any(hint in text for hint in TIER_A_HINTS):
        return "A"
    return "B"


def roles_for_tier(tier: str) -> list[str]:
    if tier == "A":
        return ["native_speaker", "lay_person", "pastor"]
    return ["theological", "pastor"]


def yaml_quote(s: str) -> str:
    """Quote a single-line string for YAML scalar emission."""
    if not s:
        return '""'
    if any(ch in s for ch in ":#&*!|>%@`'\"") or s.startswith(("- ", "? ", "[ ", "{ ")):
        # Use double-quoted style with backslash escapes
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return s


def yaml_block(s: str, indent: int = 4) -> str:
    """Emit a YAML literal block (`|`) for multi-line content."""
    pad = " " * indent
    if not s:
        return "|"
    lines = s.splitlines() or [""]
    body = "\n".join((pad + ln) if ln else "" for ln in lines)
    return f"|\n{body}"


def emit_yaml(item: Item) -> str:
    qid = derive_id(item)
    tier = infer_tier(item)
    roles = roles_for_tier(tier)
    topic_en = item.title
    body_en = item.body
    question_en = item.question or "(See body — this item lacked an explicit Question block.)"

    # If the question is short and single-line, inline-quote; otherwise emit
    # as a literal block to preserve full content (audit questions often
    # span multiple sentences with embedded code/Greek).
    use_block_for_question = len(question_en) > 200 or "\n" in question_en
    question_field = (
        f"  en: {yaml_block(question_en)}" if use_block_for_question
        else f"  en: {yaml_quote(question_en)}"
    )

    return (
        f"id: {qid}\n"
        f"tier: {tier}\n"
        f"roles: [{', '.join(roles)}]\n"
        f"kind: text\n"
        f"topic:\n"
        f"  en: {yaml_quote(topic_en)}\n"
        f"  th: {TODO_TH}\n"
        f"question:\n"
        f"{question_field}\n"
        f"  th: {TODO_TH}\n"
        f"text_prompt:\n"
        f'  en: "Notes / reasoning:"\n'
        f'  th: "{TODO_TH}"\n'
        f"body:\n"
        f"  en: {yaml_block(body_en)}\n"
        f"  th: {yaml_block(TODO_TH)}\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("book", help="Three-letter book code (JHN, GAL, ...)")
    ap.add_argument("--items", help="Path to items doc")
    ap.add_argument("--out", help="Output directory")
    args = ap.parse_args()

    book = args.book.upper()
    if book not in BOOK_SLUGS:
        print(f"unknown book code: {book}", file=sys.stderr)
        return 2
    slug = BOOK_SLUGS[book]

    items_path = Path(args.items) if args.items else (
        ROOT / "docs" / "end_of_book" / slug / f"external_review_items_{book}.md"
    )
    if not items_path.exists():
        print(f"items doc not found: {items_path}", file=sys.stderr)
        return 1

    out_dir = Path(args.out) if args.out else (
        ROOT / "output" / f"review_questions_{slug}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    text = items_path.read_text(encoding="utf-8")
    items = parse_items(text, book)
    if not items:
        print(f"no `## Item X — ...` blocks found in {items_path}", file=sys.stderr)
        return 1

    written: list[Path] = []
    for item in items:
        yaml_text = emit_yaml(item)
        out_path = out_dir / f"{derive_id(item)}.yml"
        out_path.write_text(yaml_text, encoding="utf-8")
        written.append(out_path)

    rel_out = out_dir.relative_to(ROOT) if out_dir.is_relative_to(ROOT) else out_dir
    print(f"Wrote {len(written)} YAML files to {rel_out}/")
    for p in written:
        print(f"  - {p.name}")
    print()
    print("Next steps:")
    print(f"  1. Review {rel_out}/ — replace every {TODO_TH} with Thai content")
    print( "     (verse-evidence chunks in body can stay as-is; the audit agent")
    print( "     should translate topic/question/text_prompt + the prose body)")
    print(f"  2. Copy approved YAMLs to ~/EremosVercel2/shared/review-questions/")
    print(f"  3. From ~/EremosVercel2 main: `git checkout -b feat/review-questions-{slug}-audit`")
    print(f"  4. `npm run build:review-questions` (regenerates shared/review-questions-generated.ts)")
    print(f"  5. Commit + push + `gh pr create --title \"feat: add {len(written)} review questions from {book} end-of-book audit\"`")
    return 0


if __name__ == "__main__":
    sys.exit(main())
