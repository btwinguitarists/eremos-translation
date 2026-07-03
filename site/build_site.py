#!/usr/bin/env python3
"""Build the public reader site (bible.eremosapp.com) from the reader edition.

Reads output/reader/*.md (one file per book: `# <Thai title>`, chapters as
`## บทที่ N`, verses as `**N** text`, context notes as `> _บริบท: ..._`) and
generates a fully static site into site/dist/:

    /                     story + progress + book index + give/help/data doors
    /th/<slug>/           chapter grid for one book
    /th/<slug>/<n>.html   one chapter (verses + context asides + prev/next)
    /data/                downloads: GitHub, per-book markdown, JSON, CC0

Stdlib only — runs anywhere (Vercel build: `python3 site/build_site.py`).
The generator never edits repo content; it is read-only over output/.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READER = ROOT / "output" / "reader"
DIST = Path(__file__).resolve().parent / "dist"

GITHUB = "https://github.com/btwinguitarists/eremos-translation"
GIVE_URL = "https://eremosapp.com/give"
HELP_URL = "https://eremosapp.com/help-translate"
APP_URL = "https://eremosapp.com"

# Canonical Protestant order; slugs match output/reader filenames.
CANON: list[tuple[str, str]] = [
    # (slug, English display name) — Thai titles come from each file's H1.
    ("genesis", "Genesis"), ("exodus", "Exodus"), ("leviticus", "Leviticus"),
    ("numbers", "Numbers"), ("deuteronomy", "Deuteronomy"), ("joshua", "Joshua"),
    ("judges", "Judges"), ("ruth", "Ruth"), ("1samuel", "1 Samuel"),
    ("2samuel", "2 Samuel"), ("1kings", "1 Kings"), ("2kings", "2 Kings"),
    ("1chronicles", "1 Chronicles"), ("2chronicles", "2 Chronicles"),
    ("ezra", "Ezra"), ("nehemiah", "Nehemiah"), ("esther", "Esther"),
    ("job", "Job"), ("psalms", "Psalms"), ("proverbs", "Proverbs"),
    ("ecclesiastes", "Ecclesiastes"), ("songofsongs", "Song of Songs"),
    ("isaiah", "Isaiah"), ("jeremiah", "Jeremiah"), ("lamentations", "Lamentations"),
    ("ezekiel", "Ezekiel"), ("daniel", "Daniel"), ("hosea", "Hosea"),
    ("joel", "Joel"), ("amos", "Amos"), ("obadiah", "Obadiah"),
    ("jonah", "Jonah"), ("micah", "Micah"), ("nahum", "Nahum"),
    ("habakkuk", "Habakkuk"), ("zephaniah", "Zephaniah"), ("haggai", "Haggai"),
    ("zechariah", "Zechariah"), ("malachi", "Malachi"),
    ("matthew", "Matthew"), ("mark", "Mark"), ("luke", "Luke"), ("john", "John"),
    ("acts", "Acts"), ("romans", "Romans"), ("1corinthians", "1 Corinthians"),
    ("2corinthians", "2 Corinthians"), ("galatians", "Galatians"),
    ("ephesians", "Ephesians"), ("philippians", "Philippians"),
    ("colossians", "Colossians"), ("1thessalonians", "1 Thessalonians"),
    ("2thessalonians", "2 Thessalonians"), ("1timothy", "1 Timothy"),
    ("2timothy", "2 Timothy"), ("titus", "Titus"), ("philemon", "Philemon"),
    ("hebrews", "Hebrews"), ("james", "James"), ("1peter", "1 Peter"),
    ("2peter", "2 Peter"), ("1john", "1 John"), ("2john", "2 John"),
    ("3john", "3 John"), ("jude", "Jude"), ("revelation", "Revelation"),
]
OT_COUNT = 39

CHAPTER_RE = re.compile(r"^## บทที่ (\d+)\s*$")
VERSE_RE = re.compile(r"^\*\*(\d+(?:-\d+)?)\*\*\s*(.*)$")
CONTEXT_RE = re.compile(r"^>\s*_(บริบท:.*?)_?\s*$")


@dataclass
class Chapter:
    number: int
    # Ordered blocks: ("verse", num, text) | ("context", text)
    blocks: list[tuple] = field(default_factory=list)


@dataclass
class Book:
    slug: str
    en: str
    th: str
    chapters: list[Chapter] = field(default_factory=list)

    @property
    def testament(self) -> str:
        idx = next(i for i, (s, _) in enumerate(CANON) if s == self.slug)
        return "ot" if idx < OT_COUNT else "nt"


def parse_book(slug: str, en: str) -> Book:
    text = (READER / f"{slug}.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    th_title = ""
    book = None
    chapter: Chapter | None = None
    pending_context: list[str] = []

    for line in lines:
        if line.startswith("# ") and not th_title:
            th_title = line[2:].strip()
            book = Book(slug=slug, en=en, th=th_title)
            continue
        m = CHAPTER_RE.match(line)
        if m:
            chapter = Chapter(number=int(m.group(1)))
            assert book is not None
            book.chapters.append(chapter)
            continue
        if chapter is None:
            continue
        m = CONTEXT_RE.match(line)
        if m:
            pending_context.append(m.group(1).rstrip("_ "))
            continue
        if line.startswith(">"):
            # continuation of a context blockquote
            cont = line.lstrip("> ").strip().strip("_")
            if cont and pending_context:
                pending_context[-1] += " " + cont
            continue
        if pending_context and line.strip() == "":
            for note in pending_context:
                chapter.blocks.append(("context", note))
            pending_context = []
            continue
        m = VERSE_RE.match(line)
        if m:
            chapter.blocks.append(("verse", m.group(1), m.group(2).strip()))
    if chapter is not None and pending_context:
        for note in pending_context:
            chapter.blocks.append(("context", note))
    assert book is not None, f"no title found in {slug}.md"
    return book


CSS = """
:root{--bg:#faf7f0;--ink:#2b2620;--muted:#7a715f;--line:#e6dfd0;--accent:#8a5a2b;
--card:#ffffff;--wash:#f3eee1}
@media (prefers-color-scheme:dark){:root{--bg:#191511;--ink:#e8e0d0;--muted:#9a8f7a;
--line:#31291f;--accent:#d09a5b;--card:#211c15;--wash:#211c15}}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);color:var(--ink);font:17px/1.65 -apple-system,'Sukhumvit Set',
'Noto Sans Thai',Thonburi,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:44rem;margin:0 auto;padding:2.5rem 1.25rem 5rem}
h1,h2,h3{font-family:Georgia,'Noto Serif Thai',serif;font-weight:500;line-height:1.25}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.eyebrow{font-size:.72rem;letter-spacing:.17em;text-transform:uppercase;color:var(--muted)}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;
padding-bottom:1.5rem;border-bottom:1px solid var(--line);margin-bottom:2rem}
.top .brand{font-family:Georgia,serif;font-size:1.05rem;color:var(--ink)}
.top nav{display:flex;gap:1rem;font-size:.85rem}
.hero h1{font-size:2.1rem;margin:.4rem 0 1rem}
.hero p{color:var(--muted);max-width:36rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.8rem;margin:2rem 0}
.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:.7rem;
padding:1rem 1.1rem;color:var(--ink)}
.card:hover{border-color:var(--accent);text-decoration:none}
.card b{display:block;font-family:Georgia,serif;font-weight:500;margin-bottom:.25rem}
.card span{font-size:.85rem;color:var(--muted)}
.stats{display:flex;gap:2.2rem;margin:1.8rem 0;flex-wrap:wrap}
.stats div b{display:block;font-family:Georgia,serif;font-size:1.7rem;font-weight:500}
.stats div span{font-size:.8rem;color:var(--muted)}
section{margin-top:3rem}
section>h2{font-size:1.25rem;margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--line)}
.books{display:grid;grid-template-columns:repeat(auto-fill,minmax(11.5rem,1fr));gap:.45rem}
.books a{display:block;padding:.5rem .7rem;border-radius:.5rem;color:var(--ink);line-height:1.35}
.books a:hover{background:var(--wash);text-decoration:none}
.books a em{display:block;font-style:normal;font-size:.72rem;color:var(--muted)}
.chapters{display:grid;grid-template-columns:repeat(auto-fill,minmax(3.2rem,1fr));gap:.4rem;margin-top:1.4rem}
.chapters a{display:block;text-align:center;padding:.55rem 0;border:1px solid var(--line);
border-radius:.5rem;color:var(--ink);font-variant-numeric:tabular-nums}
.chapters a:hover{border-color:var(--accent);text-decoration:none}
.verse{margin:.85rem 0}
.verse .vn{font-size:.7rem;color:var(--accent);vertical-align:super;margin-right:.35rem;
font-variant-numeric:tabular-nums}
.context{margin:1.1rem 0;padding:.7rem .95rem;background:var(--wash);border-radius:.55rem;
font-size:.86rem;color:var(--muted)}
.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:2.8rem;
padding-top:1.4rem;border-top:1px solid var(--line);font-size:.9rem}
footer{margin-top:4rem;padding-top:1.4rem;border-top:1px solid var(--line);
font-size:.8rem;color:var(--muted)}
footer a{color:var(--muted);text-decoration:underline}
.note{font-size:.85rem;color:var(--muted)}
ul.plain{list-style:none;padding:0}
ul.plain li{margin:.45rem 0}
"""


def page(title: str, body: str, depth: int) -> str:
    rel = "../" * depth
    return f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{rel}style.css">
<meta name="description" content="พระคัมภีร์ไทยฉบับเอเรโมส — a free, public-domain Thai Bible translated from the original Hebrew and Greek.">
</head>
<body>
<main>
<div class="top">
  <a class="brand" href="{rel}index.html">เอเรโมส · Eremos Thai Bible</a>
  <nav><a href="{rel}index.html#books">Books</a> <a href="{rel}data/index.html">Data</a> <a href="{GIVE_URL}">Give</a></nav>
</div>
{body}
<footer>
  <p>พระคัมภีร์ไทยฉบับเอเรโมส · The Eremos Thai Bible — released into the public domain under
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. Use it freely: quote it, print it,
  build with it — no permission, no price.</p>
  <p style="margin-top:.5rem">A work of <a href="{APP_URL}">Eremos</a> ·
  <a href="{GITHUB}">source on GitHub</a> · <a href="{HELP_URL}">help with the review</a> ·
  <a href="{GIVE_URL}">support the work</a></p>
</footer>
</main>
</body>
</html>"""


def build_chapter(book: Book, ch: Chapter, prev_link: str, next_link: str) -> str:
    parts = [f'<p class="eyebrow"><a href="index.html">{html.escape(book.th)} · {html.escape(book.en)}</a></p>']
    parts.append(f"<h1>บทที่ {ch.number}</h1>")
    for block in ch.blocks:
        if block[0] == "verse":
            _, num, text = block
            parts.append(f'<p class="verse"><span class="vn">{num}</span>{html.escape(text)}</p>')
        else:
            parts.append(f'<aside class="context">{html.escape(block[1])}</aside>')
    parts.append('<p class="note" style="margin-top:2rem">บริบท (context) notes are editorial commentary — not part of the biblical text.</p>')
    parts.append(f'<div class="pager"><span>{prev_link}</span><span>{next_link}</span></div>')
    return "\n".join(parts)


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    (DIST / "style.css").write_text(CSS, encoding="utf-8")

    books = [parse_book(slug, en) for slug, en in CANON]
    total_chapters = sum(len(b.chapters) for b in books)
    total_verses = sum(
        sum(1 for bl in ch.blocks if bl[0] == "verse") for b in books for ch in b.chapters
    )

    # Book + chapter pages
    for b in books:
        bdir = DIST / "th" / b.slug
        bdir.mkdir(parents=True)
        grid = "".join(
            f'<a href="{c.number}.html">{c.number}</a>' for c in b.chapters
        )
        body = (
            f'<p class="eyebrow">{ "พันธสัญญาเดิม · Old Testament" if b.testament == "ot" else "พันธสัญญาใหม่ · New Testament" }</p>'
            f"<h1>{html.escape(b.th)}</h1>"
            f'<p class="note">{html.escape(b.en)} · {len(b.chapters)} บท</p>'
            f'<div class="chapters">{grid}</div>'
            f'<p class="note" style="margin-top:2rem"><a href="{GITHUB}/blob/main/output/reader/{b.slug}.md">'
            f"Read this book as markdown on GitHub →</a></p>"
        )
        (bdir / "index.html").write_text(
            page(f"{b.th} · Eremos Thai Bible", body, 2), encoding="utf-8"
        )
        for i, ch in enumerate(b.chapters):
            prev_link = (
                f'<a href="{b.chapters[i-1].number}.html">← บทที่ {b.chapters[i-1].number}</a>'
                if i > 0 else f'<a href="index.html">← {html.escape(b.th)}</a>'
            )
            next_link = (
                f'<a href="{b.chapters[i+1].number}.html">บทที่ {b.chapters[i+1].number} →</a>'
                if i < len(b.chapters) - 1 else f'<a href="index.html">{html.escape(b.th)} →</a>'
            )
            (bdir / f"{ch.number}.html").write_text(
                page(f"{b.th} {ch.number} · Eremos Thai Bible",
                     build_chapter(b, ch, prev_link, next_link), 2),
                encoding="utf-8",
            )

    # Index
    def book_grid(subset: list[Book]) -> str:
        return '<div class="books">' + "".join(
            f'<a href="th/{b.slug}/index.html">{html.escape(b.th)}<em>{html.escape(b.en)}</em></a>'
            for b in subset
        ) + "</div>"

    index_body = f"""
<div class="hero">
  <p class="eyebrow">A free Thai Bible from the original languages</p>
  <h1>พระคัมภีร์ไทยฉบับเอเรโมส</h1>
  <p>God's Word belongs to everyone. The Eremos Thai Bible is translated afresh from the
  Hebrew and Greek and released into the public domain — every verse free for any church,
  app, or translator in Thailand to use. No permission. No price. Forever.</p>
</div>
<div class="stats">
  <div><b>66</b><span>books · เล่ม</span></div>
  <div><b>{total_chapters:,}</b><span>chapters · บท</span></div>
  <div><b>{total_verses:,}</b><span>verses · ข้อ</span></div>
</div>
<p class="note">A complete first translation of all 66 books now exists and is moving through
careful review with Thai readers. Context notes and remaining rough edges are being refined
in the open — you can watch, and help, as it happens.</p>
<div class="cards">
  <a class="card" href="{HELP_URL}"><b>Help review it</b><span>Read Thai? Join the review —
  native speakers, pastors, and careful readers all needed.</span></a>
  <a class="card" href="{GIVE_URL}"><b>Support the work</b><span>Tax-deductible gifts through
  Axia International sustain translation and review.</span></a>
  <a class="card" href="data/index.html"><b>Use the data</b><span>Download every book — CC0,
  markdown and JSON, straight from the open repository.</span></a>
</div>
<section id="books">
  <h2>พันธสัญญาเดิม · Old Testament</h2>
  {book_grid(books[:OT_COUNT])}
</section>
<section>
  <h2>พันธสัญญาใหม่ · New Testament</h2>
  {book_grid(books[OT_COUNT:])}
</section>
<section>
  <h2>How it's made</h2>
  <p class="note">Each verse is translated from the Masoretic Hebrew text and the SBL Greek
  New Testament, checked against layered honorific, divine-name, and consistency rules, and
  recorded with its translator decisions in the open. The reading app at
  <a href="{APP_URL}">eremosapp.com</a> carries this translation alongside its daily
  Scripture rhythms. Everything — text, decisions, tooling — lives in the
  <a href="{GITHUB}">public repository</a>.</p>
</section>
"""
    (DIST / "index.html").write_text(
        page("Eremos Thai Bible · พระคัมภีร์ไทยฉบับเอเรโมส", index_body, 0), encoding="utf-8"
    )

    # Data page
    book_links = "".join(
        f'<li><a href="{GITHUB}/blob/main/output/reader/{b.slug}.md">{html.escape(b.th)} · {html.escape(b.en)}</a></li>'
        for b in books
    )
    data_body = f"""
<h1>Use the data</h1>
<p>Everything is <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a> —
public domain, no attribution required (though we love hearing what you build).</p>
<section>
  <h2>Formats</h2>
  <ul class="plain">
    <li><b>Reader markdown</b> — one file per book with context notes:
        <a href="{GITHUB}/tree/main/output/reader">output/reader/</a></li>
    <li><b>Plain markdown</b> — verses only, for review and typesetting:
        <a href="{GITHUB}/tree/main/output/plain">output/plain/</a></li>
    <li><b>Structured JSON</b> — per-chapter, with source text and translator decisions:
        <a href="{GITHUB}/tree/main/output/translations">output/translations/</a></li>
    <li><b>Everything at once</b> — clone or
        <a href="{GITHUB}/archive/refs/heads/main.zip">download the repository as a ZIP</a>.</li>
  </ul>
</section>
<section>
  <h2>Reader edition, book by book</h2>
  <ul class="plain">{book_links}</ul>
</section>
"""
    (DIST / "data").mkdir()
    (DIST / "data" / "index.html").write_text(
        page("Data · Eremos Thai Bible", data_body, 1), encoding="utf-8"
    )

    print(f"built {total_chapters:,} chapters / {total_verses:,} verses across {len(books)} books → {DIST}")


if __name__ == "__main__":
    main()
