#!/usr/bin/env python3
"""
Translate Mark from Greek to Thai using Claude API.

Reads the structured verse data from extract_mark.py and generates Thai translations
with rationale for each verse. Uses an optimal-equivalence translation philosophy
(BSB-style) — balancing fidelity to the Greek with natural Thai readability.

Usage:
  # Translate one chapter (default: chapter 1)
  python3 scripts/translate_mark.py --chapter 1

  # Translate a single verse for testing
  python3 scripts/translate_mark.py --chapter 1 --verse 1

  # Translate the whole book
  python3 scripts/translate_mark.py --all
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic SDK not installed. Run: pip3 install anthropic --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
MARK_DIR = ROOT / "output" / "mark"
TRANSLATIONS_DIR = ROOT / "output" / "translations"

MODEL = "claude-opus-4-6"  # Highest-quality model — translation is the highest-stakes step.

SYSTEM_PROMPT = """You are a Bible translator producing a new Thai translation of the Gospel of Mark directly from the Koine Greek source text.

TRANSLATION PHILOSOPHY: Optimal equivalence (Berean Standard Bible style).
- Faithful to the Greek grammar, syntax, and semantic range
- Natural, readable Thai that a modern Thai speaker would find clear
- Preserve theological precision of key terms (e.g., εὐαγγέλιον = ข่าวประเสริฐ, χριστός = พระคริสต์, βασιλεία = อาณาจักร)
- Use respectful/religious register appropriate for Scripture in Thai (ราชาศัพท์ where applicable for divine subjects)

For each verse you translate:
1. Analyze the Greek grammatically using the provided morphological data
2. Identify the key semantic choices (especially for words with wide semantic range)
3. Produce a Thai translation that renders the meaning accurately and naturally
4. Provide brief rationale for any non-obvious word choices

IMPORTANT:
- Translate FROM the Greek, using the English gloss only as a sanity check, not as your source
- Be aware this is a CC0/public domain translation — do not mimic copyrighted Thai translations
- Flag any hapax legomena or textual variants where your choice involves interpretation
- Use natural Thai word order — do not slavishly follow Greek syntax

Output format: Valid JSON only, no prose outside JSON. Schema:
{
  "reference": "Mark X:Y",
  "thai": "...",
  "thai_literal": "... (more literal rendering if different from main)",
  "key_decisions": [
    {"greek": "...", "thai": "...", "rationale": "..."}
  ],
  "notes": "any translation challenges, variant issues, or hapax handling"
}"""


def build_user_prompt(verse: dict) -> str:
    """Build the user prompt for a single verse."""
    words_info = []
    for w in verse["words"]:
        morph = w["morphology"]
        morph_str = " ".join(
            f"{k}={v}" for k, v in morph.items() if v
        )
        freq = w["nt_frequency"]
        freq_marker = " [HAPAX]" if freq == 1 else f" [freq:{freq}]"
        words_info.append(
            f"  {w['greek']}\t→ lemma: {w['lemma']}\t"
            f"gloss: {w['english_gloss']}\t{w['class']}/{w['type']}\t"
            f"{morph_str}{freq_marker}"
        )

    hapax_note = ""
    if verse["hapax_legomena"]:
        hapax_note = f"\nHAPAX LEGOMENA in this verse (words appearing only once in NT, translate carefully): {', '.join(verse['hapax_legomena'])}"

    return f"""Translate {verse['reference']} to Thai.

GREEK (SBLGNT):
{verse['greek']}

WORD-BY-WORD MORPHOLOGY:
{chr(10).join(words_info)}

BSB ENGLISH (reference only — do NOT copy, translate from Greek):
{verse['bsb_english']}
{hapax_note}

Produce your JSON output now."""


def translate_verse(client, verse: dict, retries: int = 2) -> dict:
    """Translate a single verse via Claude API."""
    user_prompt = build_user_prompt(verse)

    for attempt in range(retries + 1):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
            )
            text = response.content[0].text.strip()

            # Strip markdown code fences if present
            if text.startswith("```"):
                text = text.split("\n", 1)[1]
                if text.endswith("```"):
                    text = text.rsplit("```", 1)[0]
                text = text.strip()

            result = json.loads(text)
            return {
                "reference": verse["reference"],
                "chapter": verse["chapter"],
                "verse": verse["verse"],
                "greek": verse["greek"],
                "bsb_english": verse["bsb_english"],
                "translation": result,
                "model": MODEL,
            }
        except json.JSONDecodeError as e:
            if attempt < retries:
                print(f"  JSON parse error (attempt {attempt + 1}), retrying: {e}")
                time.sleep(2)
                continue
            return {
                "reference": verse["reference"],
                "error": f"JSON parse failed: {e}",
                "raw_output": text,
            }
        except Exception as e:
            if attempt < retries:
                print(f"  API error (attempt {attempt + 1}), retrying: {e}")
                time.sleep(5)
                continue
            return {
                "reference": verse["reference"],
                "error": f"API error: {e}",
            }


def main():
    parser = argparse.ArgumentParser(description="Translate Mark from Greek to Thai")
    parser.add_argument("--chapter", type=int, default=1, help="Chapter to translate (default: 1)")
    parser.add_argument("--verse", type=int, help="Single verse to translate (for testing)")
    parser.add_argument("--all", action="store_true", help="Translate all 16 chapters")
    parser.add_argument("--limit", type=int, help="Limit number of verses (for testing)")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic()
    TRANSLATIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Load verses
    verses_path = MARK_DIR / "mark_verses.json"
    with open(verses_path, encoding="utf-8") as f:
        all_verses = json.load(f)

    # Filter
    if args.all:
        targets = all_verses
        out_name = "mark_full.json"
    elif args.verse is not None:
        targets = [v for v in all_verses if v["chapter"] == args.chapter and v["verse"] == args.verse]
        out_name = f"mark_{args.chapter:02d}_{args.verse:02d}.json"
    else:
        targets = [v for v in all_verses if v["chapter"] == args.chapter]
        out_name = f"mark_{args.chapter:02d}.json"

    if args.limit:
        targets = targets[:args.limit]

    print(f"Translating {len(targets)} verse(s) using {MODEL}...")
    print(f"Output: {TRANSLATIONS_DIR / out_name}")
    print()

    results = []
    start = time.time()
    for i, verse in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {verse['reference']}... ", end="", flush=True)
        t0 = time.time()
        result = translate_verse(client, verse)
        elapsed = time.time() - t0

        if "error" in result:
            print(f"ERROR ({elapsed:.1f}s): {result['error']}")
        else:
            thai = result["translation"].get("thai", "")
            print(f"{elapsed:.1f}s")
            print(f"    EN: {verse['bsb_english'][:80]}")
            print(f"    TH: {thai}")

        results.append(result)

        # Save incrementally
        out_path = TRANSLATIONS_DIR / out_name
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

    total = time.time() - start
    print(f"\nDone. {len(results)} verses in {total:.1f}s (avg {total/len(results):.1f}s/verse)")
    print(f"Saved to: {TRANSLATIONS_DIR / out_name}")


if __name__ == "__main__":
    main()
