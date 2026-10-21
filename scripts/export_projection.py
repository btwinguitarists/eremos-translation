#!/usr/bin/env python3
"""
Export the Eremos Translation as Bible files for church projection software.

Reads the verses-only edition (output/plain/<slug>.md, English/BSB verse
numbering: the numbering a congregation and a presenter expect) and writes
three whole-Bible files into output/projection/:

  eremos-thai.zefania.xml   Zefania XML   (OpenLP and many other projection apps)
  eremos-thai.osis.xml      OSIS 2.1.1    (OpenLP; SWORD tools)
  eremos-thai.opensong.xml  OpenSong XML  (OpenSong, OpenLP)

Psalm superscriptions (the italic line before verse 1) are kept as titles
where the format has one (Zefania CAPTION, OSIS psalm title) and left out of
OpenSong, which has no place for them. Nothing else is changed: no notes,
no context summaries, only the translated text.

Stdlib only. Run after any change to output/plain/:
    python3 scripts/export_projection.py
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

ROOT = Path(__file__).resolve().parent.parent
PLAIN = ROOT / "output" / "plain"
OUT = ROOT / "output" / "projection"

# Canonical Protestant order: (slug, English name, OSIS id)
BOOKS = [
    ("genesis", "Genesis", "Gen"), ("exodus", "Exodus", "Exod"), ("leviticus", "Leviticus", "Lev"),
    ("numbers", "Numbers", "Num"), ("deuteronomy", "Deuteronomy", "Deut"), ("joshua", "Joshua", "Josh"),
    ("judges", "Judges", "Judg"), ("ruth", "Ruth", "Ruth"), ("1samuel", "1 Samuel", "1Sam"),
    ("2samuel", "2 Samuel", "2Sam"), ("1kings", "1 Kings", "1Kgs"), ("2kings", "2 Kings", "2Kgs"),
    ("1chronicles", "1 Chronicles", "1Chr"), ("2chronicles", "2 Chronicles", "2Chr"),
    ("ezra", "Ezra", "Ezra"), ("nehemiah", "Nehemiah", "Neh"), ("esther", "Esther", "Esth"),
    ("job", "Job", "Job"), ("psalms", "Psalms", "Ps"), ("proverbs", "Proverbs", "Prov"),
    ("ecclesiastes", "Ecclesiastes", "Eccl"), ("songofsongs", "Song of Songs", "Song"),
    ("isaiah", "Isaiah", "Isa"), ("jeremiah", "Jeremiah", "Jer"), ("lamentations", "Lamentations", "Lam"),
    ("ezekiel", "Ezekiel", "Ezek"), ("daniel", "Daniel", "Dan"), ("hosea", "Hosea", "Hos"),
    ("joel", "Joel", "Joel"), ("amos", "Amos", "Amos"), ("obadiah", "Obadiah", "Obad"),
    ("jonah", "Jonah", "Jonah"), ("micah", "Micah", "Mic"), ("nahum", "Nahum", "Nah"),
    ("habakkuk", "Habakkuk", "Hab"), ("zephaniah", "Zephaniah", "Zeph"), ("haggai", "Haggai", "Hag"),
    ("zechariah", "Zechariah", "Zech"), ("malachi", "Malachi", "Mal"),
    ("matthew", "Matthew", "Matt"), ("mark", "Mark", "Mark"), ("luke", "Luke", "Luke"), ("john", "John", "John"),
    ("acts", "Acts", "Acts"), ("romans", "Romans", "Rom"), ("1corinthians", "1 Corinthians", "1Cor"),
    ("2corinthians", "2 Corinthians", "2Cor"), ("galatians", "Galatians", "Gal"),
    ("ephesians", "Ephesians", "Eph"), ("philippians", "Philippians", "Phil"),
    ("colossians", "Colossians", "Col"), ("1thessalonians", "1 Thessalonians", "1Thess"),
    ("2thessalonians", "2 Thessalonians", "2Thess"), ("1timothy", "1 Timothy", "1Tim"),
    ("2timothy", "2 Timothy", "2Tim"), ("titus", "Titus", "Titus"), ("philemon", "Philemon", "Phlm"),
    ("hebrews", "Hebrews", "Heb"), ("james", "James", "Jas"), ("1peter", "1 Peter", "1Pet"),
    ("2peter", "2 Peter", "2Pet"), ("1john", "1 John", "1John"), ("2john", "2 John", "2John"),
    ("3john", "3 John", "3John"), ("jude", "Jude", "Jude"), ("revelation", "Revelation", "Rev"),
]

TITLE = "พระคัมภีร์ไทย ฉบับแปลเอเรโมส (Eremos Translation)"
NOTE = ("Thai Bible drafted from the Hebrew (WLC) and Greek (SBLGNT). A draft: machine-checked, "
        "Thai review beginning. Dedicated to the public domain (CC0 1.0). bible.eremosapp.com")

CHAPTER_RE = re.compile(r"^## บทที่ (\d+)\s*$")
VERSE_RE = re.compile(r"^\*\*(\d+)\*\*\s+(.*\S)\s*$")
SUPER_RE = re.compile(r"^_(.+)_\s*$")


def parse(slug: str):
    """Thai book title and [(chapter, superscription or None, [(verse, text)])]."""
    lines = (PLAIN / f"{slug}.md").read_text(encoding="utf-8").splitlines()
    title = lines[0][2:].strip()
    chapters, cur = [], None
    for line in lines:
        m = CHAPTER_RE.match(line)
        if m:
            cur = [int(m.group(1)), None, []]
            chapters.append(cur)
            continue
        if cur is None:
            continue
        m = VERSE_RE.match(line)
        if m:
            cur[2].append((int(m.group(1)), m.group(2)))
            continue
        m = SUPER_RE.match(line)
        if m and not cur[2]:
            cur[1] = m.group(1).strip()
    return title, chapters


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    books = [(i + 1, slug, en, osis, *parse(slug)) for i, (slug, en, osis) in enumerate(BOOKS)]
    total = sum(len(vs) for *_, chs in books for _, _, vs in chs)

    # Zefania XML
    z = ['<?xml version="1.0" encoding="utf-8"?>',
         '<XMLBIBLE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
         'xsi:noNamespaceSchemaLocation="zef2005.xsd" biblename="Eremos Translation (Thai)" type="x-bible" status="v" version="1">',
         f'  <INFORMATION><title>{escape(TITLE)}</title><identifier>EREMOS-TH</identifier>'
         f'<language>THA</language><date>{date.today().isoformat()}</date>'
         f'<description>{escape(NOTE)}</description><rights>CC0 1.0 Universal (public domain)</rights></INFORMATION>']
    for n, slug, en, osis, th, chs in books:
        z.append(f'  <BIBLEBOOK bnumber="{n}" bname={quoteattr(th)} bsname={quoteattr(osis)}>')
        for c, sup, vs in chs:
            z.append(f'    <CHAPTER cnumber="{c}">')
            if sup:
                z.append(f'      <CAPTION vref="1">{escape(sup)}</CAPTION>')
            z.extend(f'      <VERS vnumber="{v}">{escape(t)}</VERS>' for v, t in vs)
            z.append('    </CHAPTER>')
        z.append('  </BIBLEBOOK>')
    z.append('</XMLBIBLE>')
    (OUT / "eremos-thai.zefania.xml").write_text("\n".join(z) + "\n", encoding="utf-8")

    # OSIS 2.1.1
    o = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<osis xmlns="http://www.bibletechnologies.net/2003/OSIS/namespace" '
         'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
         'xsi:schemaLocation="http://www.bibletechnologies.net/2003/OSIS/namespace '
         'http://www.bibletechnologies.net/osisCore.2.1.1.xsd">',
         '<osisText osisIDWork="EremosTH" osisRefWork="Bible" xml:lang="th">',
         f'<header><work osisWork="EremosTH"><title>{escape(TITLE)}</title><type type="OSIS">Bible</type>'
         f'<identifier type="OSIS">Bible.th.EremosTH</identifier><language type="IETF">th</language>'
         f'<rights type="x-copyright">{escape(NOTE)}</rights><refSystem>Bible.KJV</refSystem></work></header>']
    for n, slug, en, osis, th, chs in books:
        o.append(f'<div type="book" osisID="{osis}"><title type="main">{escape(th)}</title>')
        for c, sup, vs in chs:
            o.append(f'<chapter osisID="{osis}.{c}">')
            if sup:
                o.append(f'<title type="psalm" canonical="true">{escape(sup)}</title>')
            o.extend(f'<verse osisID="{osis}.{c}.{v}">{escape(t)}</verse>' for v, t in vs)
            o.append('</chapter>')
        o.append('</div>')
    o += ['</osisText>', '</osis>']
    (OUT / "eremos-thai.osis.xml").write_text("\n".join(o) + "\n", encoding="utf-8")

    # OpenSong
    s = ['<?xml version="1.0" encoding="UTF-8"?>', '<bible>']
    for n, slug, en, osis, th, chs in books:
        s.append(f'  <b n={quoteattr(th)}>')
        for c, sup, vs in chs:
            s.append(f'    <c n="{c}">')
            s.extend(f'      <v n="{v}">{escape(t)}</v>' for v, t in vs)
            s.append('    </c>')
        s.append('  </b>')
    s.append('</bible>')
    (OUT / "eremos-thai.opensong.xml").write_text("\n".join(s) + "\n", encoding="utf-8")

    print(f"{len(books)} books, {total} verses → {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
