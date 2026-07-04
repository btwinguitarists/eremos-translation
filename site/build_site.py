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
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READER = ROOT / "output" / "reader"
DIST = Path(__file__).resolve().parent / "dist"

SITE_ORIGIN = "https://bible.eremosapp.com"
SB_URL = os.environ.get("VITE_SUPABASE_URL", "")
SB_KEY = os.environ.get("VITE_SUPABASE_ANON_KEY", "")


def sb_config_script() -> str:
    """Baked Supabase config for the cross-device presenter (phone controls a
    TV/laptop over a realtime channel). Empty when creds absent → same-device only."""
    if SB_URL and SB_KEY:
        cfg = json.dumps({"url": SB_URL, "key": SB_KEY, "origin": SITE_ORIGIN})
        return f"<script>window.__EREMOS_SB={cfg};</script>"
    return ""

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
SUPERSCRIPT_RE = re.compile(r"^_(?!บริบท:)(.+?)_\s*$")  # unnumbered psalm superscription

STRUCTURE_DIR = ROOT / "data" / "structure"


@dataclass
class Chapter:
    number: int
    verses: list[tuple[str, str]] = field(default_factory=list)   # (num, text)
    notes: list[tuple[str, str]] = field(default_factory=list)    # (after_verse_num, text)
    superscription: str | None = None


def load_structure(slug: str) -> dict[tuple[int, int], dict]:
    """(chapter, verse) -> structure event (heading/start/selah/acrostic/…) from
    the BSB-aligned structure layer. Empty dict if the book has no file yet."""
    p = STRUCTURE_DIR / f"{slug}.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    return {(e["c"], e["v"]): e for e in data.get("structure", [])}


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
        # An italic line before the first verse of a chapter is the (unnumbered)
        # psalm superscription — "A Psalm of David. When he fled…".
        if chapter is not None and not chapter.verses and chapter.superscription is None:
            sm = SUPERSCRIPT_RE.match(line)
            if sm:
                chapter.superscription = sm.group(1).strip()
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
.wip{margin:1.6rem 0 .4rem;padding:1rem 1.2rem;background:var(--wash);border:1px solid var(--line);
border-left:3px solid var(--accent);border-radius:.6rem}
.wip-tag{display:inline-block;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;
font-weight:600;color:var(--accent);margin-bottom:.4rem}
.wip p{margin:0;font-size:.95rem;line-height:1.6;color:var(--ink);max-width:60rem}
.wip a{color:var(--accent)}
/* language switch — Thai default; toggle remembers choice */
[data-lang="th"] .only-en{display:none}
[data-lang="en"] .only-th{display:none}
.langtoggle{font:inherit;font-size:.78rem;padding:.22rem .7rem;border:1px solid var(--line);
border-radius:2rem;background:var(--card);color:var(--muted);cursor:pointer;vertical-align:middle}
.langtoggle:hover{border-color:var(--accent);color:var(--ink)}
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
.prose .prose-p{margin:0 0 1.15rem}
.prose .poetry{margin:.1rem 0 .1rem;padding-left:1.6rem;line-height:1.9;display:block}
.prose .poetry.q2{padding-left:3rem}
.prose .poetry.li1{padding-left:1.6rem}
.prose .poetry.li2{padding-left:3rem}
.prose .inscription{margin:.6rem 0;padding-left:1.6rem;font-style:italic}
.section-heading{font-family:Georgia,'Noto Serif Thai',serif;font-weight:600;line-height:1.3;
margin:2.2rem 0 .9rem}
h2.section-heading{font-size:1.35rem}
h3.section-heading{font-size:1.08rem;color:var(--muted);font-weight:500}
.section-heading.italic{font-style:italic}
.section-heading .heading-en{display:block;font-family:-apple-system,system-ui,sans-serif;
font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);
font-weight:500;margin-top:.25rem}
.book-divider{text-align:center;font-family:Georgia,serif;font-size:.8rem;letter-spacing:.2em;
text-transform:uppercase;color:var(--accent);margin:2.6rem 0 1.4rem;
padding-bottom:.7rem;border-bottom:1px solid var(--line)}
.acrostic{font-family:Georgia,serif;font-size:1.4rem;color:var(--accent);margin:1.6rem 0 .6rem}
.acrostic span{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
font-family:-apple-system,system-ui,sans-serif;vertical-align:middle;margin-left:.4rem}
.superscription{font-style:italic;color:var(--muted);font-size:.96rem;line-height:1.6;
margin:0 0 1.2rem;text-align:center}
.selah{float:right;font-style:italic;color:var(--muted);font-size:.8em}
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

/* ── presenter (control) + audience (second screen) ── */
.present-ctrl{position:fixed;inset:0;background:var(--bg);color:var(--ink);z-index:60;
display:flex;flex-direction:column;padding:.9rem 1.1rem 1.1rem;overflow:hidden}
.pc-bar{display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;
padding-bottom:.7rem;border-bottom:1px solid var(--line);flex:0 0 auto}
.pc-title{font-family:Georgia,serif;font-size:1rem}
.pc-actions{display:flex;gap:.5rem}
.pc-actions button,.pc-controls>button{font:inherit;font-size:.85rem;padding:.45rem .9rem;border-radius:2rem;
border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.pc-actions button:hover,.pc-controls>button:hover{border-color:var(--accent)}
.pc-primary{background:var(--accent)!important;border-color:var(--accent)!important;color:#fff!important}
.pc-remote{margin:.7rem 0 0;padding:.6rem .9rem;background:var(--wash);border-radius:.6rem;
font-size:.9rem;color:var(--muted);text-align:center;flex:0 0 auto}
.pc-code{font-family:Georgia,serif;font-size:1.15rem;letter-spacing:.22em;color:var(--accent);font-weight:600;margin:0 .2em}
.pc-look{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap;margin:.7rem 0 0;flex:0 0 auto}
.pc-look-lbl{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.pc-seg{display:inline-flex;border:1px solid var(--line);border-radius:2rem;overflow:hidden}
.pc-seg button{font:inherit;font-size:.8rem;padding:.35rem .8rem;border:none;background:var(--card);color:var(--muted);cursor:pointer}
.pc-seg button.on{background:var(--accent);color:#fff}
.pc-stage{flex:0 0 auto;border-radius:.7rem;margin:.8rem 0;padding:1.4rem 1.6rem;min-height:24vh;
display:flex;flex-direction:column;justify-content:center;transition:background .25s}
.pc-ref{text-align:center;font-size:.92rem;margin-bottom:.9rem;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.pc-preview{font-size:clamp(1.2rem,2.4vw,1.9rem);line-height:1.6;text-align:center;font-weight:500}
.pc-preview .pvn{font-size:.55em;vertical-align:super;margin:0 .3em 0 .5em}
.pc-controls{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex:0 0 auto}
.pc-span{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.55rem}
.pc-span b{min-width:1.3em;text-align:center;color:var(--ink);font-size:1.05rem}
.pc-span button{width:2rem;height:2rem;border-radius:50%;border:1px solid var(--line);background:var(--card);color:var(--ink);font-size:1.1rem;cursor:pointer;line-height:1}
.pc-hint{font-size:.78rem;color:var(--muted);margin:.6rem 0;text-align:center;flex:0 0 auto}
.pc-list{flex:1 1 auto;overflow-y:auto;border-top:1px solid var(--line);padding-top:.5rem;display:flex;flex-direction:column;gap:.1rem}
.pc-vitem{display:flex;gap:.6rem;align-items:baseline;text-align:left;font:inherit;font-size:1rem;line-height:1.5;
padding:.5rem .7rem;border:none;background:none;color:var(--ink);cursor:pointer;border-radius:.5rem;width:100%}
.pc-vitem:hover{background:var(--wash)}
.pc-vitem.on{background:var(--accent);color:#fff}
.pc-vn{flex:0 0 auto;min-width:1.8em;color:var(--accent);font-variant-numeric:tabular-nums;font-weight:600}
.pc-vitem.on .pc-vn{color:#fff}
.pc-vt{flex:1 1 auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}

/* audience — reference on top, brand bottom-left, hint fades when idle */
.present-audience{position:fixed;inset:0;background:#0e0c09;color:#f3ead8;z-index:50;
display:flex;flex-direction:column;user-select:none;transition:background .3s}
.present-audience .aud-ref{flex:0 0 auto;text-align:center;padding:2.6vh 4vw 0;
font-size:clamp(1rem,2vw,1.5rem);font-variant-numeric:tabular-nums;letter-spacing:.03em;
font-family:-apple-system,system-ui,sans-serif}
.present-audience .aud-slide{flex:1 1 auto;display:flex;align-items:center;justify-content:center;padding:2vh 7vw;overflow:hidden}
.present-audience .aud-body{font-weight:500;line-height:1.65;max-width:66ch;text-align:center;transition:opacity .3s ease}
.present-audience .aud-body.fade{opacity:0}
.present-audience .aud-body .pvn{font-size:.5em;vertical-align:super;margin:0 .3em 0 .5em}
.present-audience .aud-brand{position:absolute;left:2.2vw;bottom:2vh;font-size:clamp(.7rem,1.2vw,.95rem);
color:currentColor;opacity:.38;letter-spacing:.04em;font-family:-apple-system,system-ui,sans-serif}
.present-audience .aud-hint{position:absolute;bottom:2vh;left:0;right:0;text-align:center;font-size:.85rem;opacity:.5;transition:opacity .5s}
.present-audience.idle .aud-hint{opacity:0}
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
  var DATA = JSON.parse(dataEl.textContent); // {slug, th, en, ch, verses:[{n,t}]}
  var params = new URLSearchParams(location.search);
  var SB = window.__EREMOS_SB || null;
  var localCH = 'eremos-present:' + DATA.slug + ':' + DATA.ch;
  var bc = ('BroadcastChannel' in window) ? new BroadcastChannel(localCH) : null;

  // themes + fonts, shared by control preview + audience
  var THEMES = {
    night: { bg: '#0e0c09', fg: '#f3ead8', ref: '#c2ac86', vn: '#c9a978', brand: '#7d746c' },
    day:   { bg: '#f7f2e8', fg: '#2a241e', ref: '#7a6f5c', vn: '#b07d3b', brand: '#a99b83' },
    ink:   { bg: '#000000', fg: '#ffffff', ref: '#b7b7b7', vn: '#d8c39a', brand: '#8a8a8a' }
  };
  var FONTS = {
    trad:   '"Noto Serif Thai","Sarabun",Thonburi,"Angsana New",serif',
    modern: '"Sukhumvit Set","IBM Plex Sans Thai","Noto Sans Thai",system-ui,sans-serif'
  };
  function esc(t) { var d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  function realtimeConnect(code, onSlide, onHello) {
    if (!SB || !SB.url || !SB.key) return Promise.resolve(null);
    return import('https://esm.sh/@supabase/supabase-js@2').then(function (m) {
      var client = m.createClient(SB.url, SB.key, { realtime: { params: { eventsPerSecond: 10 } } });
      var ch = client.channel('bible-present:' + code, { config: { broadcast: { self: false } } });
      if (onSlide) ch.on('broadcast', { event: 'slide' }, function (e) { onSlide(e.payload); });
      if (onHello) ch.on('broadcast', { event: 'hello' }, function () { onHello(); });
      return new Promise(function (res) {
        ch.subscribe(function (s) { if (s === 'SUBSCRIBED') res({ client: client, channel: ch }); });
        setTimeout(function () { res({ client: client, channel: ch }); }, 4000);
      });
    }).catch(function () { return null; });
  }

  if (params.get('present') === 'receiver') { audience(); return; }

  var trig = document.getElementById('present-start');
  if (trig) trig.onclick = openControl;

  var ctrl = null, audWin = null, castConn = null, rt = null, CODE = null;
  var sel = 0, span = 1;
  var theme = 'night', font = 'trad';
  try { theme = localStorage.getItem('eremos.present.theme') || 'night'; font = localStorage.getItem('eremos.present.font') || 'trad'; } catch (e) {}

  function clampSel() { if (sel < 0) sel = 0; if (sel > DATA.verses.length - 1) sel = DATA.verses.length - 1; if (span < 1) span = 1; }
  function shown() { return Math.min(span, DATA.verses.length - sel); }  // never mutates span
  function roomCode() {
    try { var e = localStorage.getItem('eremos.present.code'); if (e && /^[A-Z0-9]{6}$/.test(e)) return e; } catch (x) {}
    var a = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', c = '';
    for (var i = 0; i < 6; i++) c += a[Math.floor(Math.random() * a.length)];
    try { localStorage.setItem('eremos.present.code', c); } catch (x) {}
    return c;
  }
  function slide() {
    clampSel();
    var n = shown(), body = '';
    for (var i = sel; i < sel + n; i++) body += '<span class="pv"><span class="pvn">' + DATA.verses[i].n + '</span>' + esc(DATA.verses[i].t) + '</span> ';
    var ref = DATA.th + ' ' + DATA.ch + ':' + DATA.verses[sel].n + (n > 1 ? '-' + DATA.verses[sel + n - 1].n : '');
    return { body: body, ref: ref, theme: theme, font: font };
  }
  function push() {
    var sl = slide();
    if (bc) bc.postMessage(sl);
    if (audWin && !audWin.closed) { try { audWin.postMessage({ __present: 1, p: sl }, '*'); } catch (e) {} }
    if (rt && rt.channel) { try { rt.channel.send({ type: 'broadcast', event: 'slide', payload: sl }); } catch (e) {} }
    if (castConn && castConn.state === 'connected') { try { castConn.send(JSON.stringify(sl)); } catch (e) {} }
  }

  function openControl() {
    if (ctrl) return;
    CODE = roomCode();
    var EN = document.documentElement.dataset.lang === 'en';
    function L(th, en) { return EN ? en : th; }
    ctrl = el('div', 'present-ctrl');
    ctrl.innerHTML =
      '<div class="pc-bar">' +
        '<span class="pc-title">' + esc(DATA.th) + ' ' + DATA.ch + L(' · ผู้นำเสนอ', ' · Presenter') + '</span>' +
        '<span class="pc-actions">' +
          '<button data-a="aud" class="pc-primary">' + L('เปิดหน้าจอผู้ชม', 'Open audience window') + '</button>' +
          '<button data-a="cast" hidden>' + L('แคสต์', 'Cast') + '</button>' +
          '<button data-a="close">' + L('Esc · ออก', 'Esc · exit') + '</button>' +
        '</span>' +
      '</div>' +
      (SB ? '<div class="pc-remote">' + L('บนทีวีหรือหน้าจออื่น เปิด ', 'On the TV / other screen, open ') +
            '<b>bible.eremosapp.com/present.html</b>' + L(' แล้วใส่รหัส ', ' and enter code ') +
            '<span class="pc-code">' + CODE + '</span> <span class="pc-status">' + L('· กำลังเชื่อมต่อ…', '· connecting…') + '</span></div>' : '') +
      '<div class="pc-look">' +
        '<span class="pc-look-lbl">' + L('รูปแบบ', 'Look') + '</span>' +
        '<span class="pc-seg" data-grp="theme">' +
          '<button data-theme="night">' + L('กลางคืน', 'Night') + '</button><button data-theme="day">' + L('กลางวัน', 'Day') + '</button><button data-theme="ink">' + L('ดำสนิท', 'Black') + '</button>' +
        '</span>' +
        '<span class="pc-seg" data-grp="font">' +
          '<button data-font="trad">' + L('ไทยดั้งเดิม', 'Traditional') + '</button><button data-font="modern">' + L('ไทยสมัยใหม่', 'Modern') + '</button>' +
        '</span>' +
      '</div>' +
      '<div class="pc-stage"><div class="pc-ref"></div><div class="pc-preview"></div></div>' +
      '<div class="pc-controls">' +
        '<button data-a="prev">' + L('← ก่อนหน้า', '← Prev') + '</button>' +
        '<div class="pc-span">' + L('ข้อต่อหน้าจอ', 'Verses per screen') + ' <button data-a="fewer">−</button><b class="pc-n">1</b><button data-a="more">+</button></div>' +
        '<button data-a="next">' + L('ถัดไป →', 'Next →') + '</button>' +
      '</div>' +
      '<div class="pc-hint">' + L('แตะข้อเพื่อเริ่มที่ข้อนั้น · −/+ กำหนดจำนวนข้อที่แสดง · ปุ่มถัดไปเลื่อนทีละจำนวนนั้น การควบคุมอยู่บนหน้าจอนี้', 'Tap a verse to start there · −/+ sets how many show · Next moves on by that many. Controls stay on this screen.') + '</div>' +
      '<div class="pc-list"></div>';
    document.body.appendChild(ctrl);

    var list = ctrl.querySelector('.pc-list');
    DATA.verses.forEach(function (v, i) {
      var b = el('button', 'pc-vitem');
      b.innerHTML = '<span class="pc-vn">' + v.n + '</span><span class="pc-vt">' + esc(v.t) + '</span>';
      b.onclick = function () { sel = i; span = 1; render(); push(); };
      list.appendChild(b);
    });
    ctrl.addEventListener('click', function (e) {
      var t = e.target, a = t.getAttribute && t.getAttribute('data-a');
      if (t.getAttribute && t.getAttribute('data-theme')) { theme = t.getAttribute('data-theme'); persistLook(); render(); push(); return; }
      if (t.getAttribute && t.getAttribute('data-font')) { font = t.getAttribute('data-font'); persistLook(); render(); push(); return; }
      if (!a) return;
      if (a === 'prev') go(-1);
      else if (a === 'next') go(1);
      else if (a === 'more') { span++; render(); push(); }
      else if (a === 'fewer') { if (span > 1) span--; render(); push(); }
      else if (a === 'aud') openAudience();
      else if (a === 'cast' && !castConn) startCast();
      else if (a === 'close') closeControl();
    });

    setupCast();
    document.addEventListener('keydown', onKey);
    render();
    realtimeConnect(CODE, null, function () { push(); }).then(function (r) {
      rt = r; var st = ctrl && ctrl.querySelector('.pc-status');
      if (st) st.textContent = r ? L('· พร้อมแล้ว — รอหน้าจอเข้าร่วม', '· ready — waiting for a screen to join') : L('· ออฟไลน์ (เฉพาะอุปกรณ์เดียวกัน)', '· offline (same-device only)');
      push();
    });
    push();
  }
  function persistLook() { try { localStorage.setItem('eremos.present.theme', theme); localStorage.setItem('eremos.present.font', font); } catch (e) {} }

  function render() {
    if (!ctrl) return;
    var s = slide();
    var stage = ctrl.querySelector('.pc-stage'), th = THEMES[theme];
    stage.style.background = th.bg;
    var prev = ctrl.querySelector('.pc-preview');
    prev.style.color = th.fg; prev.style.fontFamily = FONTS[font];
    prev.innerHTML = s.body;
    prev.querySelectorAll('.pvn').forEach(function (x) { x.style.color = th.vn; });
    var ref = ctrl.querySelector('.pc-ref'); ref.textContent = s.ref; ref.style.color = th.ref;
    ctrl.querySelector('.pc-n').textContent = String(span);
    ctrl.querySelectorAll('[data-theme]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-theme') === theme); });
    ctrl.querySelectorAll('[data-font]').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-font') === font); });
    var n = shown(), items = ctrl.querySelectorAll('.pc-vitem');
    for (var i = 0; i < items.length; i++) items[i].classList.toggle('on', i >= sel && i < sel + n);
    if (items[sel] && items[sel].scrollIntoView) items[sel].scrollIntoView({ block: 'nearest' });
  }
  function go(d) { clampSel(); sel = d > 0 ? sel + span : sel - span; if (sel < 0) sel = 0; if (sel > DATA.verses.length - 1) sel = DATA.verses.length - 1; render(); push(); }

  function openAudience() {
    var url = location.pathname + '?present=receiver';
    function popup(feat) { audWin = window.open(url, 'eremosAudience', feat); setTimeout(push, 900); }
    if (window.screen && window.screen.isExtended && window.getScreenDetails) {
      window.getScreenDetails().then(function (d) {
        var o = null; for (var i = 0; i < d.screens.length; i++) { if (!d.screens[i].isPrimary) { o = d.screens[i]; break; } }
        o = o || d.screens[0];
        popup('left=' + o.availLeft + ',top=' + o.availTop + ',width=' + o.availWidth + ',height=' + o.availHeight);
      }).catch(function () { popup('width=1280,height=720'); });
    } else { popup('width=1280,height=720'); }
  }
  function setupCast() {
    if (!('PresentationRequest' in window)) return;
    var btn = ctrl.querySelector('[data-a="cast"]');
    try {
      window.__castReq = new PresentationRequest([location.pathname + '?present=receiver']);
      window.__castReq.getAvailability().then(function (av) { btn.hidden = !av.value; av.onchange = function () { btn.hidden = !av.value; }; }).catch(function () {});
    } catch (e) {}
  }
  function startCast() { try { window.__castReq.start().then(function (c) { castConn = c; c.onconnect = push; setTimeout(push, 700); }).catch(function () {}); } catch (e) {} }
  function closeControl() {
    if (!ctrl) return;
    document.removeEventListener('keydown', onKey);
    ctrl.remove(); ctrl = null;
    if (audWin && !audWin.closed) audWin.close();
    if (castConn) { try { castConn.terminate(); } catch (e) {} castConn = null; }
    if (rt && rt.client) { try { rt.client.removeAllChannels(); } catch (e) {} rt = null; }
  }
  function onKey(e) {
    if (!ctrl) return;
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); go(1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(-1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); span++; render(); push(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); if (span > 1) span--; render(); push(); }
    else if (e.key === 'Escape') closeControl();
  }

  // ── AUDIENCE (chapter-page receiver window) ──
  function audience() { runAudience(document, THEMES, FONTS, bc); }
  if (bc) bc.addEventListener('message', function (e) { if (e.data && e.data.__hello && ctrl) push(); });

  // shared audience renderer (also used by present.html via window.__eremosAudience)
  window.__eremosAudience = function (doc, onReady) { runAudience(doc, THEMES, FONTS, null, onReady); };
  function runAudience(doc, themes, fonts, chan, viaExternal) {
    doc.body.classList.add('receiver');
    var mains = doc.querySelectorAll('main'); for (var i = 0; i < mains.length; i++) mains[i].hidden = true;
    var root = el('div', 'present-audience');
    root.innerHTML =
      '<div class="aud-ref"></div>' +
      '<div class="aud-slide"><div class="aud-body"></div></div>' +
      '<div class="aud-brand">bible.eremosapp.com</div>' +
      '<div class="aud-hint">แตะเพื่อเต็มจอ · tap for full screen</div>';
    doc.body.appendChild(root);
    var body = root.querySelector('.aud-body'), refEl = root.querySelector('.aud-ref'), hint = root.querySelector('.aud-hint');
    var idleTimer = null;
    function wake() { root.classList.remove('idle'); clearTimeout(idleTimer); idleTimer = setTimeout(function () { root.classList.add('idle'); }, 2600); }
    root.addEventListener('click', function () {
      if (doc.documentElement.requestFullscreen) doc.documentElement.requestFullscreen().catch(function () {});
      else if (doc.documentElement.webkitRequestFullscreen) doc.documentElement.webkitRequestFullscreen();
      hint.style.display = 'none'; wake();
    });
    doc.addEventListener('mousemove', wake); doc.addEventListener('touchstart', wake); wake();
    function fit() {
      var size = Math.min(root.clientWidth, root.clientHeight) * 0.078;
      body.style.fontSize = size + 'px';
      var g = 40; while (g-- > 0 && body.scrollHeight > body.parentElement.clientHeight && size > 12) { size *= 0.94; body.style.fontSize = size + 'px'; }
    }
    function apply(p) {
      if (!p || !p.body) return;
      var th = themes[p.theme] || themes.night;
      root.style.background = th.bg;
      refEl.style.color = th.ref; refEl.textContent = p.ref || '';
      body.style.fontFamily = fonts[p.font] || fonts.trad;
      body.style.color = th.fg;
      body.classList.add('fade');
      setTimeout(function () {
        body.innerHTML = p.body;
        body.querySelectorAll('.pvn').forEach(function (x) { x.style.color = th.vn; });
        body.classList.remove('fade'); fit();
      }, 150);
    }
    if (chan) chan.onmessage = function (e) { apply(e.data); };
    window.addEventListener('message', function (e) { if (e.data && e.data.__present) apply(e.data.p); });
    if (navigator.presentation && navigator.presentation.receiver) {
      navigator.presentation.receiver.connectionList.then(function (list) {
        function wire(c) { c.onmessage = function (e) { apply(JSON.parse(e.data)); }; }
        list.connections.forEach(wire); list.onconnectionavailable = function (e) { wire(e.connection); };
      });
    }
    window.addEventListener('resize', fit);
    if (chan) chan.postMessage({ __hello: 1 });
    if (viaExternal) viaExternal(apply);
  }

  // reading / study view toggle
  var btnRead = document.getElementById('view-reading'), btnStudy = document.getElementById('view-study');
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


def bi(th: str, en: str) -> str:
    """Inline bilingual span — CSS shows one per <html data-lang>. Thai is default."""
    return f'<span class="only-th">{th}</span><span class="only-en">{en}</span>'


# Set the language before first paint (no flash). Thai is the default for
# everyone — most Thai users run English-language phones, so browser-language
# detection would wrongly show them English; a remembered toggle handles the rest.
LANG_INIT = ("<script>(function(){try{var l=localStorage.getItem('eremos.lang');"
             "document.documentElement.dataset.lang=(l==='en'||l==='th')?l:'th';}"
             "catch(e){document.documentElement.dataset.lang='th';}})();</script>")
LANG_TOGGLE = ('<button class="langtoggle" aria-label="Thai / English" '
               "onclick=\"(function(){var d=document.documentElement.dataset;"
               "d.lang=d.lang==='en'?'th':'en';try{localStorage.setItem('eremos.lang',d.lang);}catch(e){}})()\">"
               '<span class="only-th">EN</span><span class="only-en">ไทย</span></button>')


def page(title: str, body: str, depth: int) -> str:
    rel = "../" * depth
    sb_head = sb_config_script()
    return f"""<!doctype html>
<html lang="th" data-lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{rel}style.css">
{LANG_INIT}
{sb_head}
<meta name="description" content="พระคัมภีร์ไทยฉบับเอเรโมส — a free, public-domain Thai Bible translated from the original Hebrew and Greek.">
</head>
<body>
<main>
<div class="top">
  <a class="brand" href="{rel}index.html">เอเรโมส · Eremos Thai Bible</a>
  <nav><a href="{rel}index.html#books">{bi('หนังสือ', 'Books')}</a> <a href="{rel}data/index.html">{bi('ข้อมูล', 'Data')}</a> <a href="{GIVE_URL}">{bi('ร่วมสมทบ', 'Give')}</a> {LANG_TOGGLE}</nav>
</div>
{body}
<footer>
  <p class="only-th">พระคัมภีร์ไทยฉบับเอเรโมส — มอบให้เป็นสมบัติสาธารณะภายใต้สัญญาอนุญาต
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a> ขอเชิญนำไปใช้ได้อย่างอิสระ
  ทั้งคัดลอก พิมพ์ หรือนำไปพัฒนาต่อ</p>
  <p class="only-en">The Eremos Thai Bible — released into the public domain under
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. You're warmly welcome to
  quote it, print it, and build on it.</p>
  <p style="margin-top:.5rem">{bi('ผลงานของ', 'A work of')} <a href="{APP_URL}">Eremos</a> ·
  <a href="{GITHUB}">{bi('ซอร์สโค้ดบน GitHub', 'source on GitHub')}</a> · <a href="{HELP_URL}">{bi('ช่วยตรวจทาน', 'help with the review')}</a> ·
  <a href="{GIVE_URL}">{bi('ร่วมสนับสนุน', 'support the work')}</a></p>
</footer>
</main>
</body>
</html>"""


_BLOCK_CSS = {"p": "prose-p", "q1": "poetry q1", "q2": "poetry q2",
              "li1": "poetry li1", "li2": "poetry li2", "inscription": "inscription"}


def _headings_html(ev: dict) -> str:
    """Section headings (Thai primary, English muted) + book dividers + acrostic
    letters that precede a verse."""
    out = []
    if ev.get("book_divider"):
        out.append(f'<div class="book-divider">BOOK {html.escape(ev["book_divider"])}</div>')
    for h in ev.get("heading", []):
        tag = "h2" if h["level"] == 2 else "h3"
        th = html.escape(h.get("th") or "")
        en = html.escape(h["en"])
        cls = "section-heading" + (" italic" if h.get("italic") else "")
        out.append(f'<{tag} class="{cls}">{th}<span class="heading-en">{en}</span></{tag}>')
    for ac in ev.get("acrostic", []):
        name = f' <span>{html.escape(ac["name"])}</span>' if ac.get("name") else ""
        out.append(f'<div class="acrostic">{html.escape(ac["letter"])}{name}</div>')
    return "".join(out)


def build_chapter_body(book: Book, ch: Chapter, prev_link: str, next_link: str, struct: dict) -> str:
    # Reading view: typeset with section headings, paragraphs, poetry indentation,
    # superscription, and Selah — driven by the BSB structure layer.
    reading_parts: list[str] = []
    if ch.superscription:
        reading_parts.append(f'<p class="superscription">{html.escape(ch.superscription)}</p>')
    block: tuple[str, list[str]] | None = None  # (css_class, [verse spans])

    def flush() -> None:
        nonlocal block
        if block:
            cls, items = block
            tag = "p" if cls == "prose-p" else "div"
            reading_parts.append(f'<{tag} class="{cls}">' + " ".join(items) + f"</{tag}>")
            block = None

    for num, text in ch.verses:
        ev = struct.get((ch.number, int(num))) if num.isdigit() else None
        if ev:
            head = _headings_html(ev)
            if head:
                flush()
                reading_parts.append(head)
            start = ev.get("start")
            if start:
                flush()
                block = (_BLOCK_CSS.get(start, "prose-p"), [])
        if block is None:
            block = ("prose-p", [])
        block[1].append(
            f'<span class="v" id="v{num}"><span class="vn">{num}</span>{html.escape(text)}</span>')
        if ev and ev.get("selah"):
            block[1].append('<span class="selah">เซลาห์</span>')
    flush()
    reading = "\n".join(reading_parts)

    notes_by_verse: dict[str, list[str]] = {}
    for after_v, note in ch.notes:
        notes_by_verse.setdefault(after_v, []).append(note)
    study_parts: list[str] = []
    if ch.superscription:
        study_parts.append(f'<p class="superscription">{html.escape(ch.superscription)}</p>')
    for num, text in ch.verses:
        ev = struct.get((ch.number, int(num))) if num.isdigit() else None
        if ev:
            head = _headings_html(ev)
            if head:
                study_parts.append(head)
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
    study_count = f" ({note_count})" if note_count else ""

    return f"""<p class="eyebrow"><a href="index.html">{html.escape(book.th)} · {html.escape(book.en)}</a></p>
<h1>{bi(f'บทที่ {ch.number}', f'Chapter {ch.number}')}</h1>
<div class="toolbar">
  <button id="view-reading" aria-pressed="true">{bi('อ่าน', 'Reading')}</button>
  <button id="view-study" aria-pressed="false">{bi('ศึกษา', 'Study')}{study_count}</button>
  <button id="present-start" class="present-btn">{bi('▶ นำเสนอ', '▶ Present')}</button>
</div>
<div class="prose" id="reading">{reading}</div>
<div id="study" hidden>
{study}
<p class="note" style="margin-top:2rem">{bi('หมายเหตุบริบทเป็นคำอธิบายเชิงบรรณาธิการ ไม่ใช่ส่วนหนึ่งของเนื้อความพระคัมภีร์', 'Context notes are editorial commentary — not part of the biblical text.')}</p>
</div>
<div class="pager"><span>{prev_link}</span><span>{next_link}</span></div>
<script type="application/json" id="chapter-data">{chapter_data}</script>
<script src="../../present.js"></script>"""


PRESENT_RECEIVER_HTML = r"""<!doctype html>
<html lang="th"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Audience · Eremos Thai Bible</title>
<link rel="stylesheet" href="style.css">
__SB__
</head><body class="receiver">
<div class="present-audience" id="root">
  <div class="aud-ref" id="ref"></div>
  <div class="aud-slide"><div class="aud-body" id="body"></div></div>
  <div class="aud-brand">bible.eremosapp.com</div>
  <div class="aud-hint" id="hint">แตะเพื่อเต็มจอ · tap for full screen</div>
</div>
<div id="join" style="position:fixed;inset:0;display:flex;flex-direction:column;align-items:center;
justify-content:center;gap:1rem;background:#0e0c09;color:#f3ead8;z-index:70;font-family:-apple-system,system-ui,sans-serif">
  <div style="font-family:Georgia,serif;font-size:1.3rem">เข้าร่วมการนำเสนอ · Join a presenter</div>
  <div style="color:#b9a888;font-size:.9rem">ใส่รหัส 6 หลักที่แสดงบนหน้าจอผู้นำเสนอ · Enter the 6-character code</div>
  <input id="code" maxlength="6" autocapitalize="characters" autocomplete="off"
   style="font:inherit;font-size:1.6rem;letter-spacing:.3em;text-align:center;text-transform:uppercase;
   width:9ch;padding:.6rem;border-radius:.5rem;border:1px solid #4a4132;background:rgba(255,255,255,.06);color:#f3ead8">
  <button id="go" style="font:inherit;font-size:1rem;padding:.55rem 1.4rem;border-radius:2rem;
   border:none;background:#d09a5b;color:#0e0c09;cursor:pointer">เชื่อมต่อ · Connect</button>
  <div id="err" style="color:#c98;font-size:.85rem;min-height:1.2em"></div>
</div>
<script>
(function(){
  var SB = window.__EREMOS_SB;
  var THEMES = {
    night:{bg:'#0e0c09',fg:'#f3ead8',ref:'#c2ac86',vn:'#c9a978'},
    day:{bg:'#f7f2e8',fg:'#2a241e',ref:'#7a6f5c',vn:'#b07d3b'},
    ink:{bg:'#000000',fg:'#ffffff',ref:'#b7b7b7',vn:'#d8c39a'}
  };
  var FONTS = {
    trad:'"Noto Serif Thai","Sarabun",Thonburi,"Angsana New",serif',
    modern:'"Sukhumvit Set","IBM Plex Sans Thai","Noto Sans Thai",system-ui,sans-serif'
  };
  var params = new URLSearchParams(location.search);
  var code = (params.get('code')||'').toUpperCase().replace(/[^A-Z0-9]/g,'');
  var join=document.getElementById('join'), input=document.getElementById('code');
  var root=document.getElementById('root'), body=document.getElementById('body'), refEl=document.getElementById('ref'), hint=document.getElementById('hint');
  var idle=null;
  function wake(){ root.classList.remove('idle'); clearTimeout(idle); idle=setTimeout(function(){root.classList.add('idle');},2600); }
  function fit(){
    var size=Math.min(root.clientWidth,root.clientHeight)*0.078; body.style.fontSize=size+'px';
    var g=40; while(g-->0 && body.scrollHeight>body.parentElement.clientHeight && size>12){size*=0.94;body.style.fontSize=size+'px';}
  }
  function apply(p){
    if(!p||!p.body) return;
    var th=THEMES[p.theme]||THEMES.night;
    root.style.background=th.bg; refEl.style.color=th.ref; refEl.textContent=p.ref||'';
    body.style.fontFamily=FONTS[p.font]||FONTS.trad; body.style.color=th.fg;
    body.classList.add('fade');
    setTimeout(function(){
      body.innerHTML=p.body;
      body.querySelectorAll('.pvn').forEach(function(x){x.style.color=th.vn;});
      body.classList.remove('fade'); fit();
    },150);
    hint.textContent='แตะเพื่อเต็มจอ · tap for full screen';
  }
  window.addEventListener('resize',fit);
  document.addEventListener('mousemove',wake); document.addEventListener('touchstart',wake);
  root.addEventListener('click',function(){
    if(document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(function(){});
    else if(document.documentElement.webkitRequestFullscreen) document.documentElement.webkitRequestFullscreen();
    hint.style.display='none'; wake();
  });
  function connect(c){
    if(!SB){ document.getElementById('err').textContent='Presenter sync is not configured on this site.'; return; }
    join.style.display='none'; wake();
    hint.textContent='รอผู้นำเสนอ · waiting for the presenter…';
    import('https://esm.sh/@supabase/supabase-js@2').then(function(m){
      var client=m.createClient(SB.url,SB.key,{realtime:{params:{eventsPerSecond:10}}});
      var ch=client.channel('bible-present:'+c,{config:{broadcast:{self:false}}});
      ch.on('broadcast',{event:'slide'},function(e){apply(e.payload);});
      ch.subscribe(function(s){ if(s==='SUBSCRIBED') ch.send({type:'broadcast',event:'hello',payload:{}}); });
    }).catch(function(){ document.getElementById('err').textContent='Could not load the realtime client.'; join.style.display='flex'; });
  }
  document.getElementById('go').onclick=function(){
    var c=(input.value||'').toUpperCase().replace(/[^A-Z0-9]/g,'');
    if(c.length!==6){ document.getElementById('err').textContent='Enter the 6-character code.'; return; }
    history.replaceState(null,'','?code='+c); connect(c);
  };
  input.addEventListener('keydown',function(e){ if(e.key==='Enter') document.getElementById('go').click(); });
  if(code && code.length===6){ input.value=code; connect(code); } else { input.focus(); }
})();
</script>
</body></html>
"""


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
        struct = load_structure(b.slug)
        grid = "".join(f'<a href="{c.number}.html">{c.number}</a>' for c in b.chapters)
        body = (
            f'<p class="eyebrow">{ bi("พันธสัญญาเดิม", "Old Testament") if b.testament == "ot" else bi("พันธสัญญาใหม่", "New Testament") }</p>'
            f"<h1>{html.escape(b.th)}</h1>"
            f'<p class="note">{html.escape(b.en)} · {len(b.chapters)} {bi("บท", "chapters")}</p>'
            f'<div class="chapters">{grid}</div>'
            f'<p class="note" style="margin-top:2rem"><a href="{GITHUB}/blob/main/output/reader/{b.slug}.md">'
            f'{bi("อ่านหนังสือเล่มนี้เป็น markdown บน GitHub →", "Read this book as markdown on GitHub →")}</a></p>'
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
                     build_chapter_body(b, ch, prev_link, next_link, struct), 2),
                encoding="utf-8",
            )

    def book_grid(subset: list[Book]) -> str:
        return '<div class="books">' + "".join(
            f'<a href="th/{b.slug}/index.html">{html.escape(b.th)}<em>{html.escape(b.en)}</em></a>'
            for b in subset
        ) + "</div>"

    index_body = f"""
<div class="hero">
  <p class="eyebrow">{bi('พระคัมภีร์ไทย แปลจากภาษาต้นฉบับ · มอบให้ด้วยใจ', 'A Thai Bible from the original languages — offered as a gift')}</p>
  <h1>พระคัมภีร์ไทยฉบับเอเรโมส</h1>
  <p class="only-th">พระคัมภีร์ไทยฉบับเอเรโมสเป็นฉบับแปลใหม่จากภาษาฮีบรูและกรีก มอบให้คริสตจักรไทยเป็นของขวัญ
  และวางไว้เป็นสมบัติสาธารณะ (CC0) เพื่อให้ทุกคริสตจักร แอปพลิเคชัน หรือผู้แปล นำไปใช้และต่อยอดได้อย่างอิสระ
  เราตั้งใจให้เป็นส่วนเสริมงานดีที่หลายองค์กรทุ่มเททำมานานในการแปลพระคัมภีร์ภาษาไทย ด้วยความขอบคุณ ไม่ใช่มาแทนที่</p>
  <p class="only-en">The Eremos Thai Bible is a new translation from the Hebrew and Greek, offered to the
  Thai church as a gift. It's placed in the public domain (CC0) so any church, app, or translator can
  freely use and build on it. We mean it to add to — and gratefully build on — the good work others
  have long done in Thai Scripture, not to compete with it.</p>
</div>
<div class="wip">
  <span class="wip-tag">{bi('ฉบับร่าง · กำลังตรวจทาน', 'Working draft, in review')}</span>
  <p class="only-th">นี่คือ<b>ฉบับร่างแรกที่ยังไม่เสร็จสมบูรณ์</b> ยังไม่ใช่ฉบับแปลสุดท้าย ร่างขึ้นจากภาษาฮีบรูและกรีก
  โดยมีปัญญาประดิษฐ์ (AI) ช่วย และขณะนี้ผู้อ่านชาวไทยกำลังตรวจทานทีละบรรทัดตามมาตรฐานการแปลพระคัมภีร์
  ทุกคำแปลพร้อมรับการแก้ไข <a href="{HELP_URL}"><b>ช่วยเราทำให้เสร็จสมบูรณ์ — มาเป็นผู้ตรวจทาน →</b></a></p>
  <p class="only-en">This is an <b>unfinished first draft</b> — not yet a final translation. It was drafted from the
  Hebrew and Greek with the help of AI, and Thai readers are now checking it line by line against
  established Bible-translation standards. Every rendering is open to correction.
  <a href="{HELP_URL}"><b>Help us finish it — become a reviewer →</b></a></p>
</div>
<div class="stats">
  <div><b>66</b><span>{bi('เล่ม', 'books')}</span></div>
  <div><b>{total_chapters:,}</b><span>{bi('บท', 'chapters')}</span></div>
  <div><b>{total_verses:,}</b><span>{bi('ข้อ', 'verses')}</span></div>
</div>
<p class="note only-th">ขณะนี้มีฉบับร่างครบทั้ง 66 เล่มแล้ว และกำลังตรวจทานอย่างรอบคอบทีละเล่มร่วมกับผู้อ่านชาวไทย —
ทั้งศิษยาภิบาล ผู้แปล และผู้อ่านทั่วไป — ก่อนที่ส่วนใดจะถือว่าเสร็จสมบูรณ์ ทุกบทยังมีโหมด <b>นำเสนอ</b>
สำหรับจอในคริสตจักรด้วย ทั้งแบบเต็มจอ จอที่สอง หรือ Chromecast</p>
<p class="note only-en">A first draft of all 66 books now exists and is moving, book by book, through careful
review with Thai speakers — pastors, translators, and everyday readers — before any part is
considered final. Every chapter also has a <b>Present</b> mode for church screens — fullscreen
slides, a second display, or Chromecast.</p>
<div class="cards">
  <a class="card" href="{HELP_URL}"><b>{bi('ช่วยตรวจทาน', 'Help review it')}</b><span>{bi('อ่านภาษาไทยได้ใช่ไหม? มาร่วมตรวจทาน — เราต้องการทั้งเจ้าของภาษา ศิษยาภิบาล และผู้อ่านที่ใส่ใจ', 'Read Thai? Join the review — native speakers, pastors, and careful readers all needed.')}</span></a>
  <a class="card" href="{GIVE_URL}"><b>{bi('ร่วมสนับสนุน', 'Support the work')}</b><span>{bi('การถวายช่วยสนับสนุนงานแปลและพันธกิจการสร้างสาวกของเอเรโมส', 'Tax-deductible gifts to Eremos sustain the translation and discipleship ministry.')}</span></a>
  <a class="card" href="data/index.html"><b>{bi('ใช้ข้อมูล', 'Use the data')}</b><span>{bi('ดาวน์โหลดได้ทุกเล่ม — CC0 ทั้งไฟล์ markdown และ JSON จากคลังข้อมูลเปิด', 'Download every book — CC0, markdown and JSON, straight from the open repository.')}</span></a>
</div>
<section id="books">
  <h2>{bi('พันธสัญญาเดิม', 'Old Testament')}</h2>
  {book_grid(books[:OT_COUNT])}
</section>
<section>
  <h2>{bi('พันธสัญญาใหม่', 'New Testament')}</h2>
  {book_grid(books[OT_COUNT:])}
</section>
<section>
  <h2>{bi('แปลอย่างไร และคืบหน้าแค่ไหน', "How it's made — and how far along it is")}</h2>
  <p class="note only-th">ทุกข้อร่างขึ้นจากต้นฉบับภาษาฮีบรู (Masoretic) และภาษากรีก (SBL Greek New Testament)
  โดยมี AI ช่วย จากนั้นตรวจสอบตามกฎที่วางเป็นชั้น ๆ ทั้งความสัตย์ซื่อต่อต้นฉบับ ความเป็นธรรมชาติของภาษาไทย
  และความสม่ำเสมอของพระนามพระเจ้าและคำราชาศัพท์ — แล้วจึงให้ผู้ตรวจทานชาวไทยอ่านก่อนจะถือว่าเล่มนั้นเสร็จ
  เรายึดหลักการแปลที่เป็นที่ยอมรับ และบันทึกทุกการตัดสินใจไว้อย่างเปิดเผยเพื่อให้ทุกคนตรวจสอบได้ นี่คืองานที่ตั้งใจ
  ให้อยู่ระหว่างดำเนินการ เรายินดีรับการแก้ไขมากกว่าจะผิดอยู่เงียบ ๆ และยินดีต้อนรับการตรวจสอบจากทั้งผู้แปลที่ผ่านการอบรม
  และเจ้าของภาษา แอปอ่านพระคัมภีร์ที่ <a href="{APP_URL}">eremosapp.com</a> ใช้ฉบับแปลนี้ควบคู่กับจังหวะการอ่านประจำวัน
  ทุกอย่าง — ทั้งเนื้อหา การตัดสินใจ และเครื่องมือ — อยู่ใน<a href="{GITHUB}">คลังข้อมูลสาธารณะ</a></p>
  <p class="note only-en">Every verse is drafted from the Masoretic Hebrew and the SBL Greek New Testament
  with the help of AI, then checked against layered rules for faithfulness to the original text,
  natural Thai, and consistent divine names and honorifics — and read by Thai reviewers before a
  book is called finished. We follow recognized translation principles and record every decision in
  the open, so anyone can weigh it. This is deliberately a work in progress: we would rather be
  corrected than be quietly wrong, and we welcome the scrutiny of trained translators and native
  speakers alike. The reading app at <a href="{APP_URL}">eremosapp.com</a> carries this translation
  alongside its daily Scripture rhythms; everything — text, decisions, tooling — lives in the
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
<h1>{bi('ใช้ข้อมูล', 'Use the data')}</h1>
<p class="only-th">ทุกอย่างเป็น <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a> —
สมบัติสาธารณะ ไม่ต้องให้เครดิต (แต่เรายินดีมากที่จะได้ยินว่าคุณนำไปสร้างอะไร)</p>
<p class="only-en">Everything is <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a> —
public domain, no attribution required (though we love hearing what you build).</p>
<section>
  <h2>{bi('รูปแบบไฟล์', 'Formats')}</h2>
  <ul class="plain">
    <li><b>{bi('Markdown สำหรับอ่าน', 'Reader markdown')}</b> — {bi('หนึ่งไฟล์ต่อหนึ่งเล่ม พร้อมหมายเหตุบริบท', 'one file per book with context notes')}:
        <a href="{GITHUB}/tree/main/output/reader">output/reader/</a></li>
    <li><b>{bi('Markdown ล้วน', 'Plain markdown')}</b> — {bi('เฉพาะข้อพระคัมภีร์ สำหรับตรวจทานและจัดพิมพ์', 'verses only, for review and typesetting')}:
        <a href="{GITHUB}/tree/main/output/plain">output/plain/</a></li>
    <li><b>{bi('JSON แบบมีโครงสร้าง', 'Structured JSON')}</b> — {bi('แยกตามบท พร้อมข้อความต้นฉบับและการตัดสินใจของผู้แปล', 'per-chapter, with source text and translator decisions')}:
        <a href="{GITHUB}/tree/main/output/translations">output/translations/</a></li>
    <li><b>{bi('ทั้งหมดในครั้งเดียว', 'Everything at once')}</b> — {bi('โคลนหรือ', 'clone or')}
        <a href="{GITHUB}/archive/refs/heads/main.zip">{bi('ดาวน์โหลดคลังข้อมูลเป็น ZIP', 'download the repository as a ZIP')}</a></li>
  </ul>
</section>
<section>
  <h2>{bi('ฉบับสำหรับอ่าน แยกตามเล่ม', 'Reader edition, book by book')}</h2>
  <ul class="plain">{book_links}</ul>
</section>
"""
    (DIST / "data").mkdir()
    (DIST / "data" / "index.html").write_text(
        page("Data · Eremos Thai Bible", data_body, 1), encoding="utf-8"
    )

    # Cross-device audience receiver — the URL a TV/laptop opens to join a
    # presenter by code (phone controls, this screen shows only the Bible).
    (DIST / "present.html").write_text(PRESENT_RECEIVER_HTML.replace("__SB__", sb_config_script()), encoding="utf-8")

    print(f"built {total_chapters:,} chapters / {total_verses:,} verses / {total_notes:,} notes → {DIST}")


if __name__ == "__main__":
    main()
