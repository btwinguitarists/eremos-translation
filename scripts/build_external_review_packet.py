#!/usr/bin/env python3
"""
Build an external AI sanity-check review packet for a completed NT book.

The packet is intended to be pasted into Grok / ChatGPT / Gemini / Claude for
end-of-book external review (per `docs/END_OF_BOOK_CHECKLIST.md` §3). Output
targets the ~20K-char ceiling that Grok and ChatGPT free tiers accept.

Boilerplate (prompt, project context, locked-decisions list, output format) is
auto-generated; the per-book "items" section is handwritten by the maintainer
from the end-of-book audit findings and passed in as a markdown file.

Usage:
  python3 scripts/build_external_review_packet.py BOOK --items PATH [--out PATH]

  BOOK     three-letter book code (MAT, MRK, LUK, ACT, 1TI, ...)
  --items  path to a markdown file containing the handwritten items section
           (one ## Item A — ... block per item, see existing packets for shape)
  --out    output path; default docs/external_review_packet_<BOOK>_<YYYY-MM-DD>.md

The handwritten items file should contain ONLY the items themselves — the script
wraps them with the title, paste-instructions, prompt, locked-decisions list,
output format, and footer.

Example:
  python3 scripts/build_external_review_packet.py ACT \\
    --items docs/external_review_items_ACT.md
"""
import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
DOCS = ROOT / "docs"

# ---------------------------------------------------------------------------
# Book registry — extend as books complete.
# ---------------------------------------------------------------------------
BOOKS = {
    "MAT": ("matthew", "Matthew"),
    "MRK": ("mark", "Mark"),
    "LUK": ("luke", "Luke"),
    "JHN": ("john", "John"),
    "ACT": ("acts", "Acts"),
    "ROM": ("romans", "Romans"),
    "1CO": ("1corinthians", "1 Corinthians"),
    "2CO": ("2corinthians", "2 Corinthians"),
    "GAL": ("galatians", "Galatians"),
    "EPH": ("ephesians", "Ephesians"),
    "PHP": ("philippians", "Philippians"),
    "COL": ("colossians", "Colossians"),
    "1TH": ("1thessalonians", "1 Thessalonians"),
    "2TH": ("2thessalonians", "2 Thessalonians"),
    "1TI": ("1timothy", "1 Timothy"),
    "2TI": ("2timothy", "2 Timothy"),
    "TIT": ("titus", "Titus"),
    "PHM": ("philemon", "Philemon"),
    "HEB": ("hebrews", "Hebrews"),
    "JAS": ("james", "James"),
    "1PE": ("1peter", "1 Peter"),
    "2PE": ("2peter", "2 Peter"),
    "1JN": ("1john", "1 John"),
    "2JN": ("2john", "2 John"),
    "3JN": ("3john", "3 John"),
    "JUD": ("jude", "Jude"),
    "REV": ("revelation", "Revelation"),
}

# ---------------------------------------------------------------------------
# Locked corpus-level decisions — compressed one-line summaries used in the
# packet's "don't re-litigate these" list. Keep in sync with
# docs/translator_decisions/README.md.
# ---------------------------------------------------------------------------
LOCKED_DECISIONS = [
    "ἐκκλησία (Christian community) → คริสตจักร; secular/OT assembly → ที่ประชุม",
    "βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only)",
    "ἄφεσις ἁμαρτιῶν → การยกโทษบาป; ἄφεσις (release) at LUK 4:18 → ปลดปล่อย",
    "narrator-voice ὁ κύριος (= Jesus) → องค์พระผู้เป็นเจ้า (Luke-Acts signature)",
    "vocative Κύριε from disciples/believers → องค์พระผู้เป็นเจ้า; from outsiders → context",
    "παρρησιάζομαι → อย่างกล้าหาญ",
    "δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default)",
    "honorifics ราชาศัพท์ for divine subjects + kings (Herod, Agrippa); plain register for governors (Felix, Festus) + non-divine human authorities",
    "pagan deities → เทพ / เทพี / เทพเจ้า (NEVER พระเจ้า, reserved for the biblical God)",
    "μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering)",
    "οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after possessor); ท้องฟ้า (meteorological)",
    "ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์",
    "ὁ υἱὸς τοῦ ἀνθρώπου (Christological title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์",
    "Greek historic-present verbs → Thai past tense (do not preserve present morphology)",
    "ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่พวกท่าน(ว่า) — uniform across all dominical solemn pronouncements",
    "Aramaic embeds (Talitha cumi, Ephphatha, Abba, etc.) → preserve Thai-script transliteration AND Mark's own Greek translation",
    "Inclusion-variant Path A (LOCKED): Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧` — matches BSB/ESV/NIV/CSB",
    "Parable characters representing God (fathers, kings, masters, judges) → human register, never ราชาศัพท์",
    "Narrator introducing adversary speech to Jesus → ทูล (preserves Jesus's divine status regardless of speaker)",
    "ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group, incl. Israel) / คนต่างชาติ (Gentiles, mission target)",
    "Roman titles: χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ",
    "Pagan-deity personal names → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม)",
]


def get_book_metadata(book_code):
    """Return (slug, full_name, chapter_count, verse_count) for a book."""
    if book_code not in BOOKS:
        sys.exit(f"Unknown book code: {book_code}. Known: {sorted(BOOKS)}")
    slug, name = BOOKS[book_code]
    chapters = sorted(TRANSLATIONS.glob(f"{slug}_*.json"))
    if not chapters:
        sys.exit(f"No translations found for {book_code} (slug={slug}). "
                 f"Looked in {TRANSLATIONS}.")
    verse_count = 0
    for chapter_file in chapters:
        with open(chapter_file) as f:
            data = json.load(f)
        verse_count += len(data)
    return slug, name, len(chapters), verse_count


def get_corpus_status(focus_slug):
    """One-sentence status of corpus excluding the book under review."""
    try:
        result = subprocess.run(
            ["git", "tag"],
            cwd=ROOT, capture_output=True, text=True, check=True
        )
        tags = result.stdout.strip().split("\n")
    except (subprocess.CalledProcessError, FileNotFoundError):
        tags = []

    tagged_books = []
    for tag in tags:
        if tag.startswith("book-") and tag.endswith("-v1"):
            tagged_slug = tag[5:-3]
            if tagged_slug == focus_slug:
                continue
            for code, (slug, name) in BOOKS.items():
                if slug == tagged_slug:
                    tagged_books.append(name)
                    break

    completed_untagged = []
    for code, (slug, name) in BOOKS.items():
        if slug == focus_slug:
            continue
        chapters = sorted(TRANSLATIONS.glob(f"{slug}_*.json"))
        if not chapters:
            continue
        if name in tagged_books:
            continue
        if len(chapters) >= 16 and slug != "1timothy":
            completed_untagged.append(name)

    parts = []
    if tagged_books:
        parts.append(f"{', '.join(tagged_books)} complete + tagged")
    if completed_untagged:
        parts.append(f"{', '.join(completed_untagged)} complete (not yet tagged)")
    return "; ".join(parts) if parts else "no other books shipped yet"


def build_packet(book_code, items_text):
    slug, name, chapter_count, verse_count = get_book_metadata(book_code)
    other_status = get_corpus_status(slug)
    today = date.today().isoformat()

    locked_lines = "\n".join(f"- {d}" for d in LOCKED_DECISIONS)

    header = f"""# {name} — External AI Sanity-Check Review Packet
**Date assembled: {today}**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **{name}** ({chapter_count} chapters, {verse_count:,} verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** {other_status}. {name} {chapter_count}/{chapter_count} just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

### Already-locked corpus decisions — DO NOT re-litigate

{locked_lines}

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Greek + Thai shown.

### What we are NOT asking for

- Don't propose stylistic alternatives "for variety." Consistency in key terms is a feature.
- Don't flag things from the locked-decisions list above. Those are settled.
- Don't suggest re-rendering specific verses for taste. Native Thai reviewers handle stylistic feedback.
- Don't comment on per-chapter automated-check coverage — those all pass.

### Output format

For each item below, return:

```
## [Item letter]: [Short title]
**Verdict:** FINE / CONCERN / MAJOR CONCERN
**Reasoning:** [1-3 sentences citing verses]
**Recommended action:** [specific — "lock as-is", "spot-revise verse X", "write doc Y", or "Ben to decide"]
```

Then a brief **§Z: Anything else?** section if you spot a corpus-level concern outside these items.

---
"""

    footer = f"""

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {{Verdict / Reasoning / Recommended action}} + optional §Z.
"""

    return header + items_text.strip() + footer


def main():
    parser = argparse.ArgumentParser(
        description="Build an external AI sanity-check review packet for a completed NT book."
    )
    parser.add_argument("book", help="three-letter book code (e.g., ACT, LUK)")
    parser.add_argument(
        "--items",
        required=True,
        help="path to handwritten markdown file with the per-book items section",
    )
    parser.add_argument(
        "--out",
        help="output path (default: docs/external_review_packet_<BOOK>_<DATE>.md)",
    )
    args = parser.parse_args()

    book_code = args.book.upper()
    items_path = Path(args.items)
    if not items_path.is_file():
        sys.exit(f"Items file not found: {items_path}")
    items_text = items_path.read_text()

    packet = build_packet(book_code, items_text)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = DOCS / f"external_review_packet_{book_code}_{date.today().isoformat()}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(packet)

    char_count = len(packet)
    line_count = packet.count("\n") + 1
    print(f"Wrote {out_path}")
    print(f"  {char_count:,} chars / {line_count:,} lines")
    if char_count > 25000:
        print(f"  WARNING: exceeds Grok free-tier ceiling (~25K). "
              f"Consider trimming items.")
    elif char_count > 20000:
        print(f"  Note: tight on Grok free tier (target ≤20K).")
    else:
        print(f"  Fits Grok / ChatGPT / Gemini free tiers.")


if __name__ == "__main__":
    main()
