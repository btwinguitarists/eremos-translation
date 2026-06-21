#!/usr/bin/env python3
"""
Auto-derive an end-of-book external-review *items* file from a book's own
translation decision-surface + automated check reports.

Normally the `external_review_items_<CODE>.md` section is hand-written by the
maintainer from the end-of-book audit. That doesn't scale to an unattended,
twice-weekly cadence — so this script produces a solid, evidence-based items
file automatically: divine-name consistency, locked-term applications, textual
/ versification divergences, and the hardest interpretive cruxes (longest
key_decision rationales). The result feeds `build_external_review_packet.py`.

Usage:
  python3 scripts/derive_review_items.py BOOK [--out PATH]
  BOOK   three-letter code (JER, ISA, PSA, PRO, ECC, SNG, LAM, ...)

Output (default): docs/end_of_book/<slug>/external_review_items_<CODE>.md
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TR = ROOT / "output" / "translations"
TV = ROOT / "output" / "textual_variants"
DOCS = ROOT / "docs"

# minimal slug map (extend as needed) — matches build_external_review_packet BOOKS
SLUG = {
    "JER": "jeremiah", "ISA": "isaiah", "PSA": "psalms", "PRO": "proverbs",
    "ECC": "ecclesiastes", "SNG": "songofsongs", "LAM": "lamentations",
    "EZK": "ezekiel", "DAN": "daniel", "JOB": "job",
}
NAME = {
    "JER": "Jeremiah", "ISA": "Isaiah", "PSA": "Psalms", "PRO": "Proverbs",
    "ECC": "Ecclesiastes", "SNG": "Song of Songs", "LAM": "Lamentations",
}

DIVERGENCE_KW = ["LXX", "MT ", "ต่างจาก", "versification", "การนับข้อ", "รหัส", "atbash",
                 "เซลาห์", "Selah", "ขนาน", "เทียบ ", "superscription", "คำนำหน้าสดุดี",
                 "ketiv", "qere", "เคทีฟ", "เคเร", "ไม่ปรากฏใน", "omit"]
LOCKED_KW = ["ตายตัว", "locked", "คำแปลตายตัว", "แบบแผน", "convention"]


def load_chapters(slug):
    chs = sorted(TR.glob(f"{slug}_*.json"), key=lambda p: int(re.search(r"_(\d+)\.json$", p.name).group(1)))
    out = []
    for f in chs:
        n = int(re.search(r"_(\d+)\.json$", f.name).group(1))
        try:
            out.append((n, json.load(open(f))))
        except Exception:
            pass
    return out


def all_kds(chapters):
    """yield (ref, hebrew, rendering, rationale) for every key_decision."""
    for n, verses in chapters:
        for v in verses:
            tr = v.get("translation", {}) or {}
            for kd in (tr.get("key_decisions") or []):
                yield (v.get("reference", f"ch{n}:{v.get('verse','?')}"),
                       kd.get("hebrew", ""), kd.get("rendering", ""), kd.get("rationale", ""))


def section(title):
    return f"\n## {title}\n\n"


def derive(book):
    slug = SLUG.get(book)
    name = NAME.get(book, book)
    if not slug:
        sys.exit(f"Unknown book code {book}; add it to SLUG map.")
    chapters = load_chapters(slug)
    if not chapters:
        sys.exit(f"No translations for {book} (slug={slug}).")
    kds = list(all_kds(chapters))

    # --- Item A: divine-name / honorific convention (reference the Layer-2 footnote) ---
    tv_first = sorted(TV.glob(f"{slug}_*.json"), key=lambda p: int(re.search(r"_(\d+)\.json$", p.name).group(1)))
    dn_note = ""
    if tv_first:
        try:
            objs = json.load(open(tv_first[0]))
            if objs:
                dn_note = (objs[0].get("explanation_thai", "") or "")[:900]
        except Exception:
            pass

    # --- Item B: textual / versification divergences ---
    divergences = []
    for ref, h, r, ra in kds:
        blob = f"{r} {ra}"
        if any(k.lower() in blob.lower() for k in DIVERGENCE_KW):
            divergences.append((ref, r, ra))
    # de-dup by (ref, rendering)
    seen = set(); divergences = [d for d in divergences if (d[0], d[1]) not in seen and not seen.add((d[0], d[1]))][:25]

    # --- Item C: locked-term applications ---
    locked = []
    for ref, h, r, ra in kds:
        if any(k.lower() in ra.lower() for k in LOCKED_KW):
            locked.append((ref, r))
    seen = set(); locked = [l for l in locked if l[1] not in seen and not seen.add(l[1])][:25]

    # --- Item D: hardest cruxes (longest rationales) ---
    cruxes = sorted(kds, key=lambda x: len(x[3]), reverse=True)[:8]

    nv = sum(len(v) for _, v in chapters)
    L = [
        f"# {name} ({book}) — end-of-book external-review items",
        "",
        f"_Auto-derived from the book's own `key_decisions`, textual-variant footnotes, and "
        f"automated check reports ({len(chapters)} chapters, {nv:,} verses). These are evidence-based "
        f"sanity-check prompts, not hand-curated maintainer concerns — review them as a corpus-level "
        f"second opinion and flag anything inconsistent, mistaken, or theologically off._",
    ]

    L.append(section("Item A — Divine-name & honorific convention (verify consistency across the whole book)"))
    L.append("The book applies the project's locked Tetragrammaton/honorific convention. Confirm it is applied "
             "**uniformly** and correctly across every chapter, and flag any verse where the divine name, an "
             "Adonai-YHWH compound, or royal honorifics (ราชาศัพท์) read inconsistently or wrongly.\n")
    if dn_note:
        L.append(f"> First-occurrence convention footnote (chapter 1 / first occurrence):\n>\n> {dn_note}\n")

    L.append(section("Item B — Textual & versification divergences (verify handling)"))
    if divergences:
        L.append("Key-decisions in this book that flag a textual variant, LXX/MT difference, versification "
                 "realignment, or cipher. Confirm each is handled correctly and consistently:\n")
        for ref, r, ra in divergences:
            L.append(f"- **{ref}** — {r}\n  - {ra[:280]}")
    else:
        L.append("_No textual/versification divergences were flagged in the key-decisions._")
    L.append("")

    L.append(section("Item C — Locked-term / convention applications (verify uniformity)"))
    if locked:
        L.append("Renderings the translator marked as locked/by-convention. Confirm they match the project "
                 "glossary and are used consistently here and against the rest of the corpus:\n")
        for ref, r in locked:
            L.append(f"- **{ref}** — {r}")
    else:
        L.append("_No explicitly locked-term key-decisions were tagged in this book._")
    L.append("")

    L.append(section("Item D — Hardest interpretive cruxes (evaluate the calls)"))
    L.append("The key-decisions with the most reasoning attached — i.e. the book's hardest judgment calls. "
             "Evaluate whether each rendering is defensible from the source text:\n")
    for ref, h, r, ra in cruxes:
        L.append(f"- **{ref}** — {r}\n  - {ra[:320]}")
    L.append("")

    L.append(section("Item E — Open corpus-level read"))
    L.append("Beyond the items above: read for naturalness in modern Thai, theological accuracy (evangelical-"
             "Protestant), and any cross-cutting inconsistency the per-chapter automated checks would miss. "
             "Don't manufacture flags — only raise what you actually see.")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--out")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing items file (default: REFUSE — hand-curated items must never be clobbered)")
    a = ap.parse_args()
    slug = SLUG[a.book.upper()]
    out = Path(a.out) if a.out else (DOCS / "end_of_book" / slug / f"external_review_items_{a.book.upper()}.md")
    if out.exists() and not a.force:
        sys.exit(f"REFUSING to overwrite existing {out.relative_to(ROOT)} — it may be hand-curated "
                 f"(from an end-of-book audit). Auto-derived items are a FALLBACK only. Pass --force "
                 f"if you truly mean to replace it.")
    text = derive(a.book.upper())
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"Wrote {out.relative_to(ROOT)}  ({len(text):,} chars)")


if __name__ == "__main__":
    main()
