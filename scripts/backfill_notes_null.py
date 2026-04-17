#!/usr/bin/env python3
"""
Schema fix: every verse's translation object must contain a 'notes' key.

Gemini's 2026-04-17 review flagged that 69 verses had the 'notes' key
entirely absent rather than set to null — a fragility that would crash
any check script using direct bracket access.

This script normalizes every verse across every shipped chapter so that
'notes' is always present (null when no meaningful notes exist). Run once
as a one-time cleanup; going forward, RULES.md §6 requires the key to
always be written.

No translation text, rationale, or existing note is touched — this only
adds `"notes": null` where the key was missing.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANS_DIR = ROOT / "output" / "translations"


def main():
    total_fixed = 0
    for chapter_file in sorted(TRANS_DIR.glob("*.json")):
        if "demo" in chapter_file.name:
            continue
        verses = json.loads(chapter_file.read_text(encoding="utf-8"))
        fixed = 0
        for v in verses:
            trans = v.get("translation")
            if not isinstance(trans, dict):
                continue
            for key, default in (
                ("notes", None),
                ("thai_literal", None),
                ("key_decisions", []),
                ("thai_summary", None),
            ):
                if key not in trans:
                    trans[key] = default
                    fixed += 1
        if fixed:
            chapter_file.write_text(json.dumps(verses, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  {chapter_file.name}: fixed {fixed} key-slots")
            total_fixed += fixed
    print(f"\nTotal: {total_fixed} verses normalized. `notes: null` now universally present.")


if __name__ == "__main__":
    main()
