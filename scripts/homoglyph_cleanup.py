#!/usr/bin/env python3
"""Clean Greek-letter homoglyphs from Thai-mixed text.

Distinguishes legitimate Greek source-text references (all-Greek tokens like
"κλητός" or "δικαιόω aorist-passive") from accidental homoglyph contamination
(Greek letters typed in place of visually-similar Thai letters within Thai
words, e.g. "ทρง" should be "ทรง" — ρ U+03C1 → ร U+0E23).

Tokenization rule: A "word" is a run of non-whitespace, non-punctuation chars.
A token mixing Thai chars with Greek/Cyrillic chars has the Greek/Cyrillic
chars replaced. Pure-Greek tokens are preserved.

Mapping covers the six confusable lowercase letters observed in the corpus:
α β θ μ ν ρ → า บ ธ ม น ร.

Other Greek letters (κ γ χ η ω λ τ etc.) are left alone — they appear only
in legitimate Greek-word contexts in this corpus.

Usage:
  python3 scripts/homoglyph_cleanup.py            # dry-run report
  python3 scripts/homoglyph_cleanup.py --apply    # apply fixes
"""
import argparse
import glob
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HOMOGLYPH_MAP = {
    'α': 'า',  # α → า
    'β': 'บ',  # β → บ
    'θ': 'ธ',  # θ → ธ
    'μ': 'ม',  # μ → ม
    'ν': 'น',  # ν → น
    'ρ': 'ร',  # ρ → ร
}

PUNCT = set('()[]{}.,;:!?"\'""“”‘’«»—–-/\\<>|~`@#$%^&*+=…•')


def is_thai(c: str) -> bool:
    return 0x0E00 <= ord(c) <= 0x0E7F


def is_greek_or_cyrillic(c: str) -> bool:
    cp = ord(c)
    return (0x0370 <= cp <= 0x03FF) or (0x0400 <= cp <= 0x04FF)


def is_word_char(c: str) -> bool:
    return not (c.isspace() or c in PUNCT)


def clean_text(text: str):
    """Return (cleaned_text, num_fixes, sample_fixes).

    sample_fixes: list of (before, after) tuples for the first few fixes (for reporting).
    """
    if not text:
        return text, 0, []

    n = len(text)
    # Compute word boundaries
    word_id = [-1] * n
    cur_word = -1
    in_word = False
    for i, c in enumerate(text):
        if is_word_char(c):
            if not in_word:
                cur_word += 1
                in_word = True
            word_id[i] = cur_word
        else:
            in_word = False

    # Mark words that contain any Thai char
    word_has_thai = set()
    for i, c in enumerate(text):
        if word_id[i] >= 0 and is_thai(c):
            word_has_thai.add(word_id[i])

    # Build cleaned text
    out = []
    fixes = 0
    sample_fixes = []
    for i, c in enumerate(text):
        if (
            is_greek_or_cyrillic(c)
            and word_id[i] in word_has_thai
            and c in HOMOGLYPH_MAP
        ):
            out.append(HOMOGLYPH_MAP[c])
            fixes += 1
            if len(sample_fixes) < 3:
                ctx_before = text[max(0, i - 8): i + 8]
                # Approximate the after-context by replacing this single char
                ctx_after = ctx_before.replace(c, HOMOGLYPH_MAP[c], 1)
                sample_fixes.append((ctx_before, ctx_after))
        else:
            out.append(c)

    return ''.join(out), fixes, sample_fixes


def clean_json_file(path: Path, apply: bool):
    """Process a JSON file. Returns (total_fixes, per_field_fixes_dict, examples)."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    per_field = defaultdict(int)
    examples = []

    def fix_field(parent: dict, key: str, field_label: str):
        val = parent.get(key)
        if not isinstance(val, str):
            return
        cleaned, n, samples = clean_text(val)
        if n > 0:
            per_field[field_label] += n
            parent[key] = cleaned
            for s in samples[:1]:
                examples.append((field_label, s[0], s[1]))

    if isinstance(data, list):
        for v in data:
            if not isinstance(v, dict):
                continue
            tr = v.get('translation') if 'translation' in v else v
            if not isinstance(tr, dict):
                tr = v
            for fk in ('thai', 'thai_literal', 'thai_summary', 'notes'):
                fix_field(tr, fk, fk)
            kds = tr.get('key_decisions') if isinstance(tr, dict) else None
            if isinstance(kds, list):
                for kd in kds:
                    if isinstance(kd, dict):
                        fix_field(kd, 'thai', 'kd_thai')
                        fix_field(kd, 'rationale', 'kd_rationale')
            # back-translation single-field
            if 'back_translation' in v:
                fix_field(v, 'back_translation', 'back_translation')

    total = sum(per_field.values())
    if apply and total > 0:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    return total, dict(per_field), examples


def clean_text_file(path: Path, apply: bool):
    """Process a markdown / plain-text file. Returns (total_fixes, examples)."""
    with open(path, encoding='utf-8') as f:
        original = f.read()
    cleaned, n, samples = clean_text(original)
    if apply and n > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
    return n, samples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Write changes (default: dry run)')
    ap.add_argument('--scope', choices=['all', 'translations', 'back_translations', 'docs'],
                    default='all', help='Which file groups to process')
    args = ap.parse_args()

    targets = []
    if args.scope in ('all', 'translations'):
        targets += [(p, 'json') for p in sorted(glob.glob(str(ROOT / 'output/translations/*.json')))]
    if args.scope in ('all', 'back_translations'):
        targets += [(p, 'json') for p in sorted(glob.glob(str(ROOT / 'output/back_translations/*.json')))]
    if args.scope in ('all', 'docs'):
        # markdown decision docs + end-of-book reviews
        for pat in ('docs/translator_decisions/*.md', 'docs/end_of_book/**/*.md', 'RULES.md'):
            targets += [(p, 'md') for p in sorted(glob.glob(str(ROOT / pat), recursive=True))]

    grand_total = 0
    files_changed = 0
    field_totals = defaultdict(int)

    print(f"{'Mode:':<8}{'APPLY' if args.apply else 'DRY RUN'}")
    print(f"{'Scope:':<8}{args.scope}")
    print(f"{'Files:':<8}{len(targets)}")
    print()

    per_file_changed = []

    for path_str, kind in targets:
        path = Path(path_str)
        rel = path.relative_to(ROOT)
        try:
            if kind == 'json':
                n, per_field, examples = clean_json_file(path, args.apply)
                if n > 0:
                    files_changed += 1
                    grand_total += n
                    for k, v in per_field.items():
                        field_totals[k] += v
                    per_file_changed.append((str(rel), n, per_field, examples))
            else:  # md
                n, samples = clean_text_file(path, args.apply)
                if n > 0:
                    files_changed += 1
                    grand_total += n
                    field_totals['md_text'] += n
                    per_file_changed.append((str(rel), n, {'md_text': n}, [('md_text', s[0], s[1]) for s in samples]))
        except Exception as e:
            print(f"  ERROR on {rel}: {e}", file=sys.stderr)

    print(f"=== Summary ===")
    print(f"Files changed:   {files_changed} / {len(targets)}")
    print(f"Total fixes:     {grand_total}")
    print()
    print("Fixes by field:")
    for fname, count in sorted(field_totals.items(), key=lambda kv: -kv[1]):
        print(f"  {fname:<20}: {count}")

    print()
    print(f"=== Top 15 files by fix count ===")
    per_file_changed.sort(key=lambda t: -t[1])
    for rel, n, per_field, examples in per_file_changed[:15]:
        bd = ', '.join(f"{k}={v}" for k, v in sorted(per_field.items(), key=lambda kv: -kv[1]) if v > 0)
        print(f"  {rel}: {n} [{bd}]")
        for fld, before, after in examples[:1]:
            print(f"    e.g. {fld}: '{before}' -> '{after}'")

    if not args.apply:
        print()
        print("(Dry run — no files modified. Re-run with --apply to write changes.)")


if __name__ == '__main__':
    main()
