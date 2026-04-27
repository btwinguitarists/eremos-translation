#!/usr/bin/env python3
"""
Render per-book reader-friendly Markdown documents of the Eremos Translation.

Three outputs per book:
  - output/reader/<slug>.md   — Thai verses + thai_summary as inline italic
    context (the "บริบท" blockquotes). For end-users / app readers.
  - output/plain/<slug>.md    — Thai verses ONLY, no commentary, no Greek, no
    English. For Thai scholars and theological reviewers evaluating the
    translation on its own terms.
  - output/feedback/<slug>.md — same content as plain, but every verse has a
    `>` placeholder block underneath where reviewers type per-verse comments.
    For systematic verse-by-verse review by Thai pastors / scholars / lay
    readers. The reviewer fills in only verses they want to flag and sends
    the file back; we parse the `>` blocks under each verse to extract
    feedback.

All three files include the chapter-end textual-variant footer (since those
are translation decisions about what's IN the verse text, not commentary
about it) and a SHA-256 verification footer pointing at the source JSON.

Usage:
  python3 scripts/render_reader.py                  # render ALL three variants for every translated book
  python3 scripts/render_reader.py --book MRK       # render ALL three variants for one book
  python3 scripts/render_reader.py --book mark      # same, slug form
  python3 scripts/render_reader.py --mode plain     # only the plain variant
  python3 scripts/render_reader.py --mode reader    # only the annotated reader variant
  python3 scripts/render_reader.py --mode feedback  # only the per-verse feedback template

Designed to be safe to re-run: writes only to output/reader/, output/plain/,
and output/feedback/, never touches translation source. Wired into
ship_chapter.sh so all three files regenerate on every chapter ship.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
TEXTUAL_VARIANTS = ROOT / "output" / "textual_variants"
READER_DIR = ROOT / "output" / "reader"
PLAIN_DIR = ROOT / "output" / "plain"
FEEDBACK_DIR = ROOT / "output" / "feedback"

MODES = ("reader", "plain", "feedback")

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS  # noqa: E402

# Thai book titles. For each book, the on-page heading shown to readers.
# Canonical Thai Christian conventions: พระกิตติคุณ for the four Gospels,
# กิจการของอัครทูต for Acts, individual book names otherwise.
THAI_BOOK_TITLES = {
    "MAT": "พระกิตติคุณตามมัทธิว",
    "MRK": "พระกิตติคุณตามมาระโก",
    "LUK": "พระกิตติคุณตามลูกา",
    "JHN": "พระกิตติคุณตามยอห์น",
    "ACT": "กิจการของอัครทูต",
    "ROM": "โรม",
    "1CO": "1 โครินธ์", "2CO": "2 โครินธ์",
    "GAL": "กาลาเทีย", "EPH": "เอเฟซัส", "PHP": "ฟีลิปปี", "COL": "โคโลสี",
    "1TH": "1 เธสะโลนิกา", "2TH": "2 เธสะโลนิกา",
    "1TI": "1 ทิโมธี", "2TI": "2 ทิโมธี", "TIT": "ทิตัส", "PHM": "ฟีเลโมน",
    "HEB": "ฮีบรู", "JAS": "ยากอบ",
    "1PE": "1 เปโตร", "2PE": "2 เปโตร",
    "1JN": "1 ยอห์น", "2JN": "2 ยอห์น", "3JN": "3 ยอห์น",
    "JUD": "ยูดา", "REV": "วิวรณ์",
}

SLUG_TO_CODE = {slug: code for code, (_, slug) in BOOKS.items()}


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def chapter_files_for(slug: str) -> list[Path]:
    """All translated chapter files for a book, sorted by chapter number.
    Strict pattern match excludes demo / fragment files like mark_01_01_demo.json."""
    pattern = re.compile(rf"^{re.escape(slug)}_(\d+)\.json$")
    matched = [
        (int(m.group(1)), p)
        for p in TRANSLATIONS.glob(f"{slug}_*.json")
        if (m := pattern.match(p.name))
    ]
    return [p for _, p in sorted(matched)]


def render_chapter(verses: list[dict], chapter_num: int, variants: list[dict] | None = None, *, mode: str = "reader") -> str:
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}, got {mode!r}")
    lines = [f"## บทที่ {chapter_num}", ""]
    for v in verses:
        n = v["verse"]
        thai = (v.get("translation") or {}).get("thai", "").strip()
        # Bold verse number followed by the verse text on the same paragraph.
        # Thai Bibles use Arabic numerals conventionally; keep Arabic.
        lines.append(f"**{n}** {thai}")
        if mode == "reader":
            summary = (v.get("translation") or {}).get("thai_summary")
            if summary and summary.strip():
                lines.append("")
                # GitHub renders blockquote + italic cleanly. The "บริบท:" label
                # mirrors the in-app popup's "บริบท · Context" header.
                lines.append(f"> _บริบท: {summary.strip()}_")
        elif mode == "feedback":
            # Per-verse placeholder block. Reviewer types comments inside the
            # `>` block; empty `___` means no concerns. We parse `>` content
            # under each verse number when extracting feedback.
            lines.append("")
            lines.append("> ___")
        lines.append("")

    # Path A inclusion-variant footer (per RULES §5 + docs/translator_decisions/
    # inclusion_variants_absent_verses_2026-04.md). For each whole-verse
    # inclusion variant absent from the SBLGNT base text, surface the TR/Byz
    # Thai rendering + manuscript witnesses so readers cross-checking with
    # THSV/THKJV can see what those traditions read instead of seeing a
    # silent verse-number jump.
    if variants:
        lines.append("---")
        lines.append("")
        lines.append("### หมายเหตุด้านต้นฉบับ")
        lines.append("")
        for var in variants:
            verse_num = var.get("verse")
            tr_thai = var.get("tr_byz_thai", "")
            include = var.get("witnesses_include", "")
            omit = var.get("witnesses_omit", "")
            explanation = var.get("explanation_thai", "")
            lines.append(f"**ข้อ {verse_num}** — ขาดในต้นฉบับวิจารณ์ (SBLGNT)")
            lines.append("")
            if tr_thai:
                lines.append(f"> {tr_thai}")
                lines.append("")
            if explanation:
                lines.append(f"_{explanation}_")
                lines.append("")
            if include or omit:
                lines.append("ต้นฉบับที่รวมไว้: " + (include or "-"))
                lines.append("")
                lines.append("ต้นฉบับที่ละไว้: " + (omit or "-"))
                lines.append("")
        lines.append("")
    return "\n".join(lines)


def load_textual_variants(slug: str, chapter_num: int) -> list[dict]:
    """Load chapter-level inclusion-variant footer notes if present."""
    fp = TEXTUAL_VARIANTS / f"{slug}_{chapter_num:02d}.json"
    if not fp.exists():
        return []
    return json.loads(fp.read_text(encoding="utf-8"))


def _edition_blurb(mode: str, slug: str) -> str:
    if mode == "plain":
        return (
            "_This **plain edition** shows only the Thai translation — no commentary, "
            "no Greek, no English. Intended for Thai scholars and theological reviewers "
            f"evaluating the translation on its own terms. For the annotated edition with "
            f"contextual summaries (บริบท), see `output/reader/{slug}.md`. For the underlying "
            f"Greek, English (BSB) reference, and translator decisions per verse, see the "
            f"per-chapter review reports at `output/check_reports/{slug}_NN_review.md` "
            f"or the source JSON at `output/translations/`._"
        )
    if mode == "feedback":
        return (
            "_This **feedback edition** is the plain Thai translation with a `>` "
            "placeholder block under each verse for reviewer comments. **See the "
            "instructions immediately below before reading.** "
            f"For the annotated edition (with contextual summaries), see `output/reader/{slug}.md`; "
            f"for the verses-only edition (no comment blocks), see `output/plain/{slug}.md`._"
        )
    return (
        "_This reader edition shows the Thai translation and the contextual "
        "summary (บริบท) where one is provided. The contextual summaries are AI-generated "
        "editorial commentary, not part of the biblical text. For a plain "
        f"verses-only edition (recommended for scholarly review), see "
        f"`output/plain/{slug}.md`. For the underlying Greek, English (BSB) reference, "
        f"and translator decisions per verse, see the per-chapter review reports at "
        f"`output/check_reports/{slug}_NN_review.md` or the source JSON at "
        f"`output/translations/`._"
    )


FEEDBACK_INSTRUCTIONS = """## วิธีใช้ / How to use this file

**ภาษาไทย — สำหรับผู้ตรวจทาน**

1. เปิดไฟล์นี้ในโปรแกรมแก้ไขข้อความ (TextEdit, VS Code, Notepad) หรืออัปโหลดเข้า Google Docs
2. ใต้แต่ละข้อมีกล่อง `> ___` ว่างไว้สำหรับความเห็นของท่าน — พิมพ์ความเห็นแทน `___` หากท่านมีข้อเสนอแนะ ข้อสังเกต หรือคำถามเกี่ยวกับข้อนั้น
3. **ปล่อยกล่องที่เป็น `> ___` ไว้เหมือนเดิม หากไม่มีความเห็น** — ไม่ต้องเขียนทุกข้อ
4. ความเห็นของท่านอาจเป็น: ภาษาไทยที่ฟังไม่เป็นธรรมชาติ, การเลือกใช้คำที่ควรปรับ, ราชาศัพท์ที่ใช้ผิดบริบท, ความหมายที่คลุมเครือ, หรือสิ่งใดก็ตามที่ท่านสังเกตเห็น
5. บันทึกไฟล์ (หรือคัดลอกเอกสาร Google Docs) แล้วส่งกลับมาให้ผู้ดูแลโครงการ

**English — for the reviewer**

1. Open this file in any text editor (TextEdit, VS Code, Notepad) or upload to Google Docs.
2. Under each verse you'll find an empty `> ___` block. Replace `___` with your comments — suggestions, concerns, questions about that verse.
3. **Leave the `> ___` block unchanged for verses you have no comments on.** You don't need to comment on every verse.
4. Comments can be about: unnatural Thai, word choices to revisit, register issues (royal vs. plain Thai), unclear meaning, anything you notice.
5. Save the file (or share the Google Doc) and send it back to the maintainer.

ขอบคุณ / Thank you for your time."""


def render_book(book_code: str, *, mode: str = "reader") -> Path | None:
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}, got {mode!r}")
    if book_code not in BOOKS:
        print(f"  unknown book code: {book_code}", file=sys.stderr)
        return None
    title_en, slug = BOOKS[book_code]
    title_thai = THAI_BOOK_TITLES.get(book_code, title_en)

    chapters = chapter_files_for(slug)
    if not chapters:
        print(f"  {book_code}: no translated chapters yet — skipping")
        return None

    chapter_count = len(chapters)
    chapter_word = "chapter" if chapter_count == 1 else "chapters"
    one_line = (
        f"_The Gospel of {title_en} — {chapter_count} {chapter_word}, "
        f"translated from the SBLGNT Greek text into Thai by the Eremos Translation project._"
        if book_code in {"MAT", "MRK", "LUK", "JHN"}
        else f"_{title_en} — {chapter_count} {chapter_word}, translated from the SBLGNT Greek text into Thai by the Eremos Translation project._"
    )

    parts = [
        f"# {title_thai}",
        "",
        one_line,
        "",
        _edition_blurb(mode, slug),
        "",
        "---",
        "",
    ]

    if mode == "feedback":
        parts.append(FEEDBACK_INSTRUCTIONS)
        parts.append("")
        parts.append("---")
        parts.append("")

    chapter_hashes: list[tuple[str, str]] = []
    for chapter_path in chapters:
        chapter_num = int(re.search(r"_(\d+)\.json$", chapter_path.name).group(1))
        verses = json.loads(chapter_path.read_text(encoding="utf-8"))
        variants = load_textual_variants(slug, chapter_num)
        parts.append(render_chapter(verses, chapter_num, variants, mode=mode))
        parts.append("---")
        parts.append("")
        chapter_hashes.append((chapter_path.name, file_sha256(chapter_path)))

    parts.append("## Verification")
    parts.append("")
    parts.append(
        "Each chapter's source JSON has a SHA-256 fingerprint. Anyone can recompute "
        "and verify against the manifest at `HASHES.md` to confirm they have the "
        "canonical Eremos Translation of that chapter."
    )
    parts.append("")
    parts.append("| Chapter file | SHA-256 |")
    parts.append("|---|---|")
    for name, sha in chapter_hashes:
        parts.append(f"| `output/translations/{name}` | `{sha}` |")
    parts.append("")

    out_dir = {"reader": READER_DIR, "plain": PLAIN_DIR, "feedback": FEEDBACK_DIR}[mode]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.md"
    out_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return out_path


def _modes_to_run(mode_arg: str) -> list[str]:
    """Map a --mode flag to the list of mode names to render."""
    if mode_arg == "all":
        return list(MODES)
    return [mode_arg]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--book",
        help="Book code (MRK) or slug (mark). If omitted, render all books that have translated chapters.",
    )
    parser.add_argument(
        "--mode",
        choices=["all", *MODES],
        default="all",
        help="Which markdown variants to write. 'all' (default) writes output/reader/, output/plain/, and output/feedback/.",
    )
    args = parser.parse_args()
    modes = _modes_to_run(args.mode)

    if args.book:
        code = args.book.upper()
        if code not in BOOKS:
            code = SLUG_TO_CODE.get(args.book.lower())
        if not code:
            print(f"Unknown book: {args.book}", file=sys.stderr)
            return 1
        for mode in modes:
            out = render_book(code, mode=mode)
            if out:
                print(f"Wrote {out}")
        return 0

    # Render every book that has translated chapters.
    written: list[Path] = []
    for code, (_, slug) in BOOKS.items():
        if not any(TRANSLATIONS.glob(f"{slug}_*.json")):
            continue
        for mode in modes:
            out = render_book(code, mode=mode)
            if out:
                print(f"Wrote {out}")
                written.append(out)
    dirs = sorted({str(p.parent) for p in written})
    print(f"\nRendered {len(written)} file(s) to {', '.join(dirs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
