#!/usr/bin/env python3
"""Build the public reader site (bible.eremosapp.com) from the reader edition.

Reads output/reader/*.md (one file per book: `# <Thai title>`, chapters as
`## บทที่ N`, verses as `**N** text`, context notes as `> _บริบท: ..._`) and
generates a fully static site into site/dist/:

    /                     story + progress + book index + give/help/data doors
    /th/<slug>/           chapter grid for one book
    /th/<slug>/<n>.html   one chapter — reading flow (default), study view
                          (verse-by-verse + context notes, opt-in), and a
                          presentation mode (fullscreen slides; Chromecast via
                          the Presentation API; second-screen via the Window
                          Management API; AirPlay by screen mirroring)
    /data/                downloads: GitHub, per-book markdown, JSON, CC0

Stdlib only — runs anywhere (Vercel build: `python3 site/build_site.py`).
The generator never edits repo content; it is read-only over output/.

Formatting note: verses flow as continuous prose with superscript numbers,
and context notes are hidden by default (they are editorial, not text).
True typeset structure (section headings, paragraph breaks, poetry indents)
arrives as a separate data layer based on the BSB's public-domain apparatus —
that layer lives in the translation repo, not here.
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
    verses: list[tuple[str, str]] = field(default_factory=list)   # (num, text)
    notes: list[tuple[str, str]] = field(default_factory=list)    # (after_verse_num, text)


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
    th_title = ""
    book: Book | None = None
    chapter: Chapter | None = None
    pending: list[str] = []

    def flush(ch: Chapter | None) -> None:
        nonlocal pending
        if ch is not None and pending:
            last_v = ch.verses[-1][0] if ch.verses else "0"
            for note in pending:
                ch.notes.append((last_v, note))
        pending = []

    for line in text.splitlines():
        if line.startswith("# ") and not th_title:
            th_title = line[2:].strip()
            book = Book(slug=slug, en=en, th=th_title)
            continue
        m = CHAPTER_RE.match(line)
        if m:
            flush(chapter)
            chapter = Chapter(number=int(m.group(1)))
            assert book is not None
            book.chapters.append(chapter)
            continue
        if chapter is None:
            continue
        m = CONTEXT_RE.match(line)
        if m:
            pending.append(m.group(1).rstrip("_ "))
            continue
        if line.startswith(">"):
            cont = line.lstrip("> ").strip().strip("_")
            if cont and pending:
                pending[-1] += " " + cont
            continue
        m = VERSE_RE.match(line)
        if m:
            flush(chapter)
            chapter.verses.append((m.group(1), m.group(2).strip()))
    flush(chapter)
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

/* chapter toolbar */
.toolbar{display:flex;gap:.5rem;align-items:center;margin:1.2rem 0 1.8rem;flex-wrap:wrap}
.toolbar button{font:inherit;font-size:.82rem;padding:.42rem .85rem;border-radius:2rem;
border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.toolbar button:hover{border-color:var(--accent)}
.toolbar button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.toolbar .present-btn{margin-left:auto;background:var(--accent);border-color:var(--accent);color:#fff}

/* reading flow — continuous prose with superscript numbers */
.prose{font-size:1.24rem;line-height:2.05}
.prose .vn{font-size:.62em;color:var(--accent);vertical-align:super;margin:0 .3em 0 .55em;
font-variant-numeric:tabular-nums;user-select:none}
.prose .v:first-child .vn{margin-left:0}

/* study view — verse per line + notes */
.verse{margin:.85rem 0;line-height:1.9}
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
[hidden]{display:none !important}

/* ── presentation mode ─────────────────────────────────────────────── */
.present-root{position:fixed;inset:0;background:#0e0c09;color:#f3ead8;z-index:50;
display:flex;flex-direction:column;user-select:none}
.present-root .slide{flex:1;display:flex;align-items:center;justify-content:center;
padding:4vh 7vw;text-align:center;overflow:hidden}
.present-root .slide .vtext{font-weight:500;line-height:1.75;max-width:62ch;
font-family:-apple-system,'Sukhumvit Set','Noto Sans Thai',Thonburi,system-ui,sans-serif}
.present-root .ref{display:flex;justify-content:space-between;align-items:center;
padding:1.1rem 1.6rem;font-size:clamp(.9rem,1.6vw,1.25rem);color:#b9a888;
font-variant-numeric:tabular-nums}
.present-root .hud{position:absolute;top:.9rem;right:1rem;display:flex;gap:.5rem;z-index:2}
.present-root .hud button{font:inherit;font-size:.8rem;padding:.4rem .8rem;border-radius:2rem;
border:1px solid #4a4132;background:rgba(255,255,255,.06);color:#e8e0d0;cursor:pointer}
.present-root .hud button:hover{border-color:#b9a888}
.present-root .zone{position:absolute;top:0;bottom:4rem;width:30%;cursor:pointer;z-index:1}
.present-root .zone.prev{left:0}
.present-root .zone.next{right:0}
.present-root .hint{position:absolute;bottom:4.6rem;left:0;right:0;text-align:center;
font-size:.8rem;color:#8a7c62;opacity:.85}
body.receiver{background:#0e0c09}
"""

# Presentation logic — dependency-free. Three output paths:
#   1. Fullscreen on this display (works everywhere; AirPlay = mirror the
#      screen from Control Center, then present).
#   2. Chromecast via the Presentation API (Chrome): this same page acts as
#      the receiver (?present=receiver) — the controller sends verse indexes.
#   3. Second physical display via the Window Management API (Chrome): opens
#      a receiver window on the external screen, synced over BroadcastChannel.
PRESENT_JS = r"""
(function () {
  'use strict';
  var dataEl = document.getElementById('chapter-data');
  if (!dataEl) return;
  var DATA = JSON.parse(dataEl.textContent);
  var params = new URLSearchParams(location.search);
  var CHANNEL = 'eremos-present:' + DATA.slug + ':' + DATA.ch;
  var bc = ('BroadcastChannel' in window) ? new BroadcastChannel(CHANNEL) : null;

  var root = null, idx = 0, castConn = null, extWin = null;

  function build() {
    root = document.createElement('div');
    root.className = 'present-root';
    root.innerHTML =
      '<div class="hud">' +
      '<button data-act="cast" hidden>Cast</button>' +
      '<button data-act="ext" hidden>External display</button>' +
      '<button data-act="close">Esc</button></div>' +
      '<div class="zone prev" title="Previous"></div>' +
      '<div class="zone next" title="Next"></div>' +
      '<div class="slide"><div class="vtext"></div></div>' +
      '<div class="hint"></div>' +
      '<div class="ref"><span class="ref-book"></span><span class="ref-pos"></span></div>';
    document.body.appendChild(root);
    root.querySelector('.ref-book').textContent = DATA.th + ' · ' + DATA.en;
    root.querySelector('[data-act=close]').onclick = stop;
    root.querySelector('.zone.prev').onclick = function () { go(idx - 1); };
    root.querySelector('.zone.next').onclick = function () { go(idx + 1); };
    setupCast();
    setupExternal();
    if (!('PresentationRequest' in window) && /Safari/.test(navigator.userAgent) && !/Chrome/.test(navigator.userAgent)) {
      root.querySelector('.hint').textContent =
        'AirPlay: mirror this screen from Control Center, then present.';
      setTimeout(function () { var h = root && root.querySelector('.hint'); if (h) h.textContent = ''; }, 7000);
    }
  }

  function fit(el) {
    var size = Math.min(window.innerWidth, window.innerHeight) * 0.085;
    el.style.fontSize = size + 'px';
    var guard = 26;
    while (guard-- > 0 && el.scrollHeight > el.parentElement.clientHeight) {
      size *= 0.92;
      el.style.fontSize = size + 'px';
    }
  }

  function render() {
    if (!root) return;
    var v = DATA.verses[idx];
    var t = root.querySelector('.vtext');
    t.textContent = v.t;
    root.querySelector('.ref-pos').textContent =
      DATA.ch + ':' + v.n + '  ·  ' + (idx + 1) + '/' + DATA.verses.length;
    fit(t);
  }

  function broadcast() {
    var msg = { v: idx };
    if (bc) bc.postMessage(msg);
    if (castConn && castConn.state === 'connected') castConn.send(JSON.stringify(msg));
  }

  function go(n) {
    idx = Math.max(0, Math.min(DATA.verses.length - 1, n));
    render();
    broadcast();
  }

  function onKey(e) {
    if (!root) return;
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); go(idx + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(idx - 1); }
    else if (e.key === 'Escape') stop();
  }

  function start(at) {
    if (root) return;
    idx = at || 0;
    build();
    render();
    document.addEventListener('keydown', onKey);
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen().catch(function () {});
    }
    broadcast();
  }

  function stop() {
    if (!root) return;
    document.removeEventListener('keydown', onKey);
    root.remove(); root = null;
    if (document.fullscreenElement) document.exitFullscreen().catch(function () {});
    if (extWin && !extWin.closed) extWin.close();
    if (castConn) { try { castConn.terminate(); } catch (e) {} castConn = null; }
  }

  /* Chromecast (Presentation API) */
  function setupCast() {
    if (!('PresentationRequest' in window)) return;
    var btn = root.querySelector('[data-act=cast]');
    try {
      var req = new PresentationRequest([location.pathname + '?present=receiver']);
      req.getAvailability().then(function (avail) {
        btn.hidden = !avail.value;
        avail.onchange = function () { btn.hidden = !avail.value; };
      }).catch(function () {});
      btn.onclick = function () {
        req.start().then(function (conn) {
          castConn = conn;
          conn.onconnect = broadcast;
          setTimeout(broadcast, 800);
        }).catch(function () {});
      };
    } catch (e) {}
  }

  /* Second physical display (Window Management API) */
  function setupExternal() {
    var btn = root.querySelector('[data-act=ext]');
    if (!(window.screen && 'isExtended' in window.screen) || !window.getScreenDetails) return;
    btn.hidden = !window.screen.isExtended;
    btn.onclick = function () {
      window.getScreenDetails().then(function (details) {
        var other = null;
        for (var i = 0; i < details.screens.length; i++) {
          if (!details.screens[i].isPrimary) { other = details.screens[i]; break; }
        }
        other = other || details.screens[0];
        var feat = 'left=' + other.availLeft + ',top=' + other.availTop +
                   ',width=' + other.availWidth + ',height=' + other.availHeight;
        extWin = window.open(location.pathname + '?present=receiver', 'eremosPresent', feat);
        setTimeout(broadcast, 1200);
      }).catch(function () {});
    };
  }

  /* receiver mode — full-bleed slides driven by the controller */
  function receiver() {
    document.body.classList.add('receiver');
    var mains = document.querySelectorAll('main');
    for (var i = 0; i < mains.length; i++) mains[i].hidden = true;
    build();
    root.querySelector('.hud').hidden = true;
    root.querySelector('.hint').textContent = 'คลิกเพื่อเต็มจอ · click for fullscreen';
    root.addEventListener('click', function once() {
      if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(function () {});
      root.querySelector('.hint').textContent = '';
      root.removeEventListener('click', once);
    });
    render();
    function apply(m) { if (m && typeof m.v === 'number') { idx = m.v; render(); } }
    if (bc) bc.onmessage = function (e) { apply(e.data); };
    if (navigator.presentation && navigator.presentation.receiver) {
      navigator.presentation.receiver.connectionList.then(function (list) {
        function wire(conn) { conn.onmessage = function (e) { apply(JSON.parse(e.data)); }; }
        list.connections.forEach(wire);
        list.onconnectionavailable = function (e) { wire(e.connection); };
      });
    }
    window.addEventListener('resize', render);
  }

  if (params.get('present') === 'receiver') { receiver(); return; }

  var trigger = document.getElementById('present-start');
  if (trigger) trigger.onclick = function () { start(0); };
  window.addEventListener('resize', function () { if (root) render(); });

  /* reading/study view toggle (context notes live only in study view) */
  var btnRead = document.getElementById('view-reading');
  var btnStudy = document.getElementById('view-study');
  function setView(study) {
    document.getElementById('reading').hidden = study;
    document.getElementById('study').hidden = !study;
    btnRead.setAttribute('aria-pressed', String(!study));
    btnStudy.setAttribute('aria-pressed', String(study));
    try { localStorage.setItem('eremos.bible.view', study ? 'study' : 'reading'); } catch (e) {}
  }
  if (btnRead && btnStudy) {
    btnRead.onclick = function () { setView(false); };
    btnStudy.onclick = function () { setView(true); };
    try { if (localStorage.getItem('eremos.bible.view') === 'study') setView(true); } catch (e) {}
  }
})();
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


def build_chapter_body(book: Book, ch: Chapter, prev_link: str, next_link: str) -> str:
    reading = "".join(
        f'<span class="v" id="v{num}"><span class="vn">{num}</span>{html.escape(text)}</span> '
        for num, text in ch.verses
    )

    notes_by_verse: dict[str, list[str]] = {}
    for after_v, note in ch.notes:
        notes_by_verse.setdefault(after_v, []).append(note)
    study_parts: list[str] = []
    for num, text in ch.verses:
        study_parts.append(f'<p class="verse"><span class="vn">{num}</span>{html.escape(text)}</p>')
        for note in notes_by_verse.get(num, []):
            study_parts.append(f'<aside class="context">{html.escape(note)}</aside>')
    study = "\n".join(study_parts)

    chapter_data = json.dumps(
        {"slug": book.slug, "th": book.th, "en": book.en, "ch": ch.number,
         "verses": [{"n": n, "t": t} for n, t in ch.verses]},
        ensure_ascii=False, separators=(",", ":"),
    )

    note_count = len(ch.notes)
    study_label = f"ศึกษา · Study ({note_count})" if note_count else "ศึกษา · Study"

    return f"""<p class="eyebrow"><a href="index.html">{html.escape(book.th)} · {html.escape(book.en)}</a></p>
<h1>บทที่ {ch.number}</h1>
<div class="toolbar">
  <button id="view-reading" aria-pressed="true">อ่าน · Reading</button>
  <button id="view-study" aria-pressed="false">{study_label}</button>
  <button id="present-start" class="present-btn">▶ Present</button>
</div>
<div class="prose" id="reading">{reading}</div>
<div id="study" hidden>
{study}
<p class="note" style="margin-top:2rem">บริบท (context) notes are editorial commentary — not part of the biblical text.</p>
</div>
<div class="pager"><span>{prev_link}</span><span>{next_link}</span></div>
<script type="application/json" id="chapter-data">{chapter_data}</script>
<script src="../../present.js"></script>"""


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    (DIST / "style.css").write_text(CSS, encoding="utf-8")
    (DIST / "present.js").write_text(PRESENT_JS, encoding="utf-8")

    books = [parse_book(slug, en) for slug, en in CANON]
    total_chapters = sum(len(b.chapters) for b in books)
    total_verses = sum(len(ch.verses) for b in books for ch in b.chapters)
    total_notes = sum(len(ch.notes) for b in books for ch in b.chapters)

    for b in books:
        bdir = DIST / "th" / b.slug
        bdir.mkdir(parents=True)
        grid = "".join(f'<a href="{c.number}.html">{c.number}</a>' for c in b.chapters)
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
                     build_chapter_body(b, ch, prev_link, next_link), 2),
                encoding="utf-8",
            )

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
careful review with Thai readers. Every chapter has a <b>Present</b> mode for church screens —
fullscreen slides, Chromecast, or a second display.</p>
<div class="cards">
  <a class="card" href="{HELP_URL}"><b>Help review it</b><span>Read Thai? Join the review —
  native speakers, pastors, and careful readers all needed.</span></a>
  <a class="card" href="{GIVE_URL}"><b>Support the work</b><span>Tax-deductible gifts to Eremos
  sustain the translation and discipleship ministry.</span></a>
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

    print(f"built {total_chapters:,} chapters / {total_verses:,} verses / {total_notes:,} notes → {DIST}")


if __name__ == "__main__":
    main()
