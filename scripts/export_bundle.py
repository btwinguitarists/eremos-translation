#!/usr/bin/env python3
"""
Export the whole Eremos Translation as one JSON file, for developers and AI tools.

    output/bundle/eremos-thai.json   every book, chapter and verse, English (BSB)
                                     numbering, psalm titles as `title`
    output/bundle/SHA256SUMS         SHA-256 fingerprint of the JSON (and of the
                                     USFM/projection files), so anyone can check
                                     they hold the genuine text

Verse numbers and text come from versification_english.to_english_rows, the
function behind the reader edition, bible.eremosapp.com, the USFM files and the
app, so all of them agree verse for verse.

The file is deterministic (no timestamps): the same text always gives the same
bytes, so a signature stays valid until the text itself changes.

Signing (Ben's key) and the OpenTimestamps proof are separate steps, run after
this script; see output/bundle/README.md.

Stdlib only:  python3 scripts/export_bundle.py
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from versification_english import load_versification_map, to_english_rows  # noqa: E402
from export_projection import BOOKS as CANON  # noqa: E402  (slug, English name, OSIS id)
from export_to_usfm import BOOKS as USFM_BOOKS  # noqa: E402  code → (slug, long_th, short_th, abbr_th, mt, en)

TRANSLATIONS = ROOT / "output" / "translations"
OUT = ROOT / "output" / "bundle"
SLUG_TO_CODE = {v[0]: code for code, v in USFM_BOOKS.items()}


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main() -> int:
    vmap = load_versification_map()
    books, total = [], 0
    for slug, en, osis in CANON:
        code = SLUG_TO_CODE[slug]
        files = sorted(
            (p for p in TRANSLATIONS.glob(f"{slug}_*.json") if p.stem.rsplit("_", 1)[1].isdigit()),
            key=lambda p: int(p.stem.rsplit("_", 1)[1]),
        )
        mt = [v for f in files for v in json.loads(f.read_text(encoding="utf-8"))]
        rows, titles = to_english_rows(code, mt, vmap)
        chapters: dict[int, dict] = {}
        for r in rows:
            ch = chapters.setdefault(r["chapter"], {"chapter": r["chapter"], "verses": []})
            ch["verses"].append({"verse": r["verse"], "text": r["thai"]})
        for c, t in titles.items():
            if c in chapters and t:
                chapters[c]["title"] = t
        ordered = [dict(sorted(chapters[c].items(), key=lambda kv: ["chapter", "title", "verses"].index(kv[0]))) for c in sorted(chapters)]
        total += sum(len(c["verses"]) for c in ordered)
        books.append({
            "osis": osis, "usfm": code, "name_en": en, "name_th": USFM_BOOKS[code][1],
            "chapters": ordered,
        })

    bundle = {
        "name": "Eremos Translation (Thai)",
        "name_th": "พระคัมภีร์ไทย ฉบับแปลเอเรโมส",
        "language": "th",
        "license": "CC0-1.0",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "status": "Complete draft, drafted with AI from the Hebrew and Greek, machine-checked; Thai review is beginning.",
        "sources": {
            "hebrew": "Westminster Leningrad Codex (via OSHB / MACULA Hebrew)",
            "greek": "SBL Greek New Testament (via MACULA Greek)",
        },
        "versification": "English (BSB) numbering; psalm superscriptions are unnumbered `title` fields.",
        "decision_records": "Per-verse translation decisions (Hebrew/Greek, rationale) are in output/translations/*.json in the source repo.",
        "home": "https://bible.eremosapp.com",
        "source_repo": "https://github.com/btwinguitarists/eremos-translation",
        "counts": {"books": len(books), "verses": total},
        "books": books,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    data = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n"
    (OUT / "eremos-thai.json").write_text(data, encoding="utf-8")

    # Fingerprints of every distributable file, in `sha256sum -c` format.
    targets = [OUT / "eremos-thai.json"]
    targets += sorted((ROOT / "output" / "paratext").glob("*.SFM"))
    targets += sorted((ROOT / "output" / "projection").glob("*.xml"))
    lines = []
    for p in targets:
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        lines.append(f"{h}  {p.relative_to(ROOT).as_posix()}")
    (OUT / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{len(books)} books, {total} verses → {(OUT / 'eremos-thai.json').relative_to(ROOT)} "
          f"({len(data.encode()) / 1e6:.1f} MB); {len(lines)} fingerprints → output/bundle/SHA256SUMS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
