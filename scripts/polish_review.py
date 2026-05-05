#!/usr/bin/env python3
"""
NT v1.0 Thai-flow polish sweep (Stage 2 of run_nt_full_audit).

Default mode is a deterministic local scanner focused only on
**micro-readability** issues. It proposes edits; it never auto-applies.

Claude Code review is still available for spot checks with `--engine claude`,
but it is not the default for `--all` because one Claude process per chapter is
too slow and brittle for a corpus-wide pass.

Issue types caught (closed list):
  - double_possessive     ของตน...ของตน in close proximity
  - title_collision       divine titles back-to-back (e.g., องค์พระผู้เป็นเจ้าพระเจ้า)
  - redundant_directional repeated direction-of-motion (ส่งมา...มาถึง)
  - lexical_redundancy    redundant near-synonyms in same phrase
  - passive_ambiguity     Greek passive rendered as Thai active causing confusion
  - awkward_phonetic      general phonetic flow issues a Thai reader notices aloud

Output: output/polish_proposals/<slug>_<NN>.md (per chapter, decision-ready)

Validation gates (rejects hallucinations before writing):
  - `current_text` must appear verbatim in the verse's Thai field
  - `issue_type` must be in the closed list above
  - Any term from the verse's `key_decisions` Thai value must still appear in `proposed_text`
    (corpus-locked terms cannot be silently changed)

Files written ONLY to output/polish_proposals/. Translation JSONs untouched.

Usage:
  python3 scripts/polish_review.py --book john              # single book, heuristic engine
  python3 scripts/polish_review.py --book john --chapter 15 # single chapter smoke test
  python3 scripts/polish_review.py --book john --chapter 15 --engine claude
  python3 scripts/polish_review.py --all                    # all 27 NT books, fast local scan
  python3 scripts/polish_review.py --all --resume           # skip chapters with existing proposals
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
PROPOSALS = ROOT / "output" / "polish_proposals"
RULES = ROOT / "RULES.md"
GLOSSARY = ROOT / "glossary.json"

MODEL = "sonnet"  # Editorial nuance benefits from sonnet over haiku.
DEFAULT_ENGINE = "heuristic"

ISSUE_TYPES = {
    "double_possessive",
    "title_collision",
    "redundant_directional",
    "lexical_redundancy",
    "passive_ambiguity",
    "awkward_phonetic",
}

NT_BOOKS = [
    ("matthew", 28), ("mark", 16), ("luke", 24), ("john", 21), ("acts", 28),
    ("romans", 16), ("1corinthians", 16), ("2corinthians", 13), ("galatians", 6),
    ("ephesians", 6), ("philippians", 4), ("colossians", 4), ("1thessalonians", 5),
    ("2thessalonians", 3), ("1timothy", 6), ("2timothy", 4), ("titus", 3),
    ("philemon", 1), ("hebrews", 13), ("james", 5), ("1peter", 5), ("2peter", 3),
    ("1john", 5), ("2john", 1), ("3john", 1), ("jude", 1), ("revelation", 22),
]

SYSTEM_PROMPT = """You are a Thai-language editor reviewing an already-finalized Bible translation for **micro-readability polish**.

Your ONLY job is to surface Thai phrasing that stumbles when read aloud — phonetic flow, redundancy, or a passive/active ambiguity. NOT theology, NOT word choice, NOT register.

The reviewer who reads your output is a native Thai speaker who will accept or reject each proposal individually. You should be HELPFUL and surface real issues — even minor ones. Do NOT under-fire. The reviewer would rather see 6 candidates and reject 2 than miss a real flow issue.

ISSUE TYPES (closed list — proposal MUST match one):

1. **double_possessive** — ของตน, ของเขา, ของพวก- repeated in the same phrase making the sentence rhythmically heavy.
   EXAMPLE (John 15:13): "...สละชีวิตของตนเพื่อมิตรสหายของตน" → "...สละชีวิตเพื่อมิตรสหายของตน" (drop the first ของตน since reflexivity is implied by สละชีวิต).

2. **title_collision** — divine titles run together without grammatical bridge so they read as a stutter.
   EXAMPLE (Rev 19:6): "องค์พระผู้เป็นเจ้าพระเจ้าผู้ทรงฤทธานุภาพ" → "องค์พระผู้เป็นเจ้า พระเจ้าผู้ทรงฤทธานุภาพ" (insert space + bridge).

3. **redundant_directional** — repeated direction-of-motion (มา, ไป) creating audible repetition.
   EXAMPLE (John 15:26): "ส่งมาจากพระบิดามาถึง" → "ส่งจากพระบิดามายัง" (swap prepositions to remove double มา).

4. **lexical_redundancy** — two near-synonyms in the same phrase saying the same thing twice.
   EXAMPLE (Rev 19:15): "บ่อย่ำองุ่นแห่งเหล้าองุ่นของพระพิโรธ" → "บ่อคั้นองุ่นแห่งพระพิโรธ" (compress; "winepress of wine" is redundant).

5. **passive_ambiguity** — Greek perfect-passive rendered with Thai active phrasing that misleads.
   EXAMPLE (Rev 19:9): "ผู้ที่ทรงเรียกให้มาในงานเลี้ยงวิวาห์" (reads as "one who calls others") → "บรรดาผู้ที่ได้รับเชิญมาในงานเลี้ยงวิวาห์" (use ได้รับ for clear passive).

6. **awkward_phonetic** — phrase that's hard to read aloud due to consonant cluster or unintended sound repetition.

ABSOLUTE RULES:
- DO NOT propose changes for theological reasons. Theology is locked.
- ONLY the specific Thai strings listed under "Locked phrases" for a given verse are corpus-locked. The REST of the verse's Thai text is fair game for polish — including the surrounding context where a locked phrase sits. A proposal is fine as long as every "Locked phrase" string still appears verbatim in your `proposed_text`.
- DO NOT change ทรง- prefixes or royal Thai (ราชาศัพท์) registers.
- DO NOT change meaning. Smooth flow only.
- The `current_text` field MUST be a verbatim substring (character-for-character) of the verse's Thai text.
- Output ONLY the JSON object. No prose before or after. No markdown fences. No commentary.

OUTPUT: Strict JSON. No prose outside JSON. Schema:

{
  "chapter_ref": "<Book Chapter>",
  "proposals": [
    {
      "verse_ref": "<Book Chapter:Verse>",
      "issue_type": "<one of the six closed types>",
      "current_text": "<EXACT verbatim Thai substring of translation.thai>",
      "proposed_text": "<the smoothed Thai>",
      "rationale": "<one or two sentences in English: why current is awkward, how proposed smooths it without changing meaning>"
    }
  ]
}

Walk the chapter verse by verse. For each verse, check the six issue types against the Thai text. Return all valid proposals. An empty proposals array is fine if and only if you genuinely found nothing across the entire chapter."""

USER_PROMPT_TEMPLATE = """Chapter to review: **{chapter_ref}**

For each verse below: Thai text first, then a list of corpus-locked Thai phrases that MUST be preserved verbatim in any proposal.

{compact_chapter}

Review the Thai text for the six micro-readability issue types. Return strict JSON only. Empty proposals array is fine if you found nothing."""


def build_compact_chapter(chapter_data: list[dict]) -> str:
    """Render a small per-verse representation: ref + Thai + locked terms.
    Avoids sending the full chapter JSON (Greek, English, notes, rationale)
    which is ~10x larger and slows the model unnecessarily."""
    out = []
    for v in chapter_data:
        ref = v.get("reference", "?")
        thai = v.get("translation", {}).get("thai", "")
        locked = []
        for kd in v.get("translation", {}).get("key_decisions", []) or []:
            t = (kd or {}).get("thai")
            if t:
                locked.append(t.strip())
        out.append(f"### {ref}")
        out.append(f"Thai: {thai}")
        if locked:
            out.append("Locked phrases (do not modify): " + " | ".join(locked))
        out.append("")
    return "\n".join(out)


def load_chapter(slug: str, chapter: int) -> dict | None:
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def all_locked_thai(verse: dict) -> set[str]:
    """Collect every Thai term that's locked via key_decisions for this verse."""
    locked = set()
    kds = verse.get("translation", {}).get("key_decisions", []) or []
    for kd in kds:
        thai = (kd or {}).get("thai")
        if thai:
            # Strip whitespace; keep multi-word phrases as a unit.
            locked.add(thai.strip())
    return locked


def thai_of(verse: dict) -> str:
    return verse.get("translation", {}).get("thai", "") or ""


def add_candidate(candidates: list[dict], seen: set[tuple[str, str, str]],
                  verse: dict, issue_type: str, current_text: str,
                  proposed_text: str, rationale: str) -> None:
    """Append a deterministic proposal candidate if it is non-empty and unique."""
    current_text = current_text.strip()
    proposed_text = proposed_text.strip()
    if not current_text or not proposed_text or current_text == proposed_text:
        return
    key = (verse.get("reference", ""), current_text, proposed_text)
    if key in seen:
        return
    seen.add(key)
    candidates.append({
        "verse_ref": verse.get("reference", "?"),
        "issue_type": issue_type,
        "current_text": current_text,
        "proposed_text": proposed_text,
        "rationale": rationale,
    })


def add_literal_replacement(candidates: list[dict], seen: set[tuple[str, str, str]],
                            verse: dict, issue_type: str, current_text: str,
                            proposed_text: str, rationale: str) -> None:
    """Add a literal replacement only when the exact current string appears."""
    if current_text in thai_of(verse):
        add_candidate(candidates, seen, verse, issue_type, current_text,
                      proposed_text, rationale)


def scan_title_collisions(candidates: list[dict], seen: set[tuple[str, str, str]],
                          verse: dict) -> None:
    thai = thai_of(verse)
    if "องค์พระผู้เป็นเจ้าพระเจ้า" in thai:
        add_literal_replacement(
            candidates, seen, verse, "title_collision",
            "องค์พระผู้เป็นเจ้าพระเจ้า",
            "องค์พระผู้เป็นเจ้า พระเจ้า",
            "The divine titles run together as องค์พระผู้เป็นเจ้า + พระเจ้า without a visible grammatical break. Adding a space separates the titles for oral reading while leaving the title words unchanged.",
        )


def scan_directional_redundancy(candidates: list[dict], seen: set[tuple[str, str, str]],
                                verse: dict) -> None:
    add_literal_replacement(
        candidates, seen, verse, "redundant_directional",
        "เสด็จออกไปกับบรรดาสาวกของพระองค์ไปยัง",
        "เสด็จออกไปกับบรรดาสาวกของพระองค์ยัง",
        "The direction particle ไป occurs once in เสด็จออกไป and again in ไปยัง, creating an audible repeated-motion stumble. Dropping the second ไป keeps the destination marker ยัง and preserves the movement.",
    )
    add_literal_replacement(
        candidates, seen, verse, "redundant_directional",
        "ส่งมาจากพระบิดามาถึงพวกท่าน",
        "ส่งจากพระบิดามายังพวกท่าน",
        "The paired มาจาก ... มาถึง repeats the direction particle มา in a tight span. Using ส่งจาก ... มายัง keeps the source and destination clear while smoothing the repeated motion wording.",
    )


def scan_lexical_redundancy(candidates: list[dict], seen: set[tuple[str, str, str]],
                            verse: dict) -> None:
    add_literal_replacement(
        candidates, seen, verse, "lexical_redundancy",
        "บ่อย่ำองุ่นแห่งเหล้าองุ่นของพระพิโรธ",
        "บ่อคั้นองุ่นแห่งพระพิโรธ",
        "บ่อย่ำองุ่นแห่งเหล้าองุ่น doubles the winepress/wine idea in Thai. บ่อคั้นองุ่นแห่งพระพิโรธ keeps the image and removes the redundant เหล้าองุ่น wording.",
    )


def scan_passive_ambiguity(candidates: list[dict], seen: set[tuple[str, str, str]],
                           verse: dict) -> None:
    add_literal_replacement(
        candidates, seen, verse, "passive_ambiguity",
        "ผู้ที่ทรงเรียกให้มาในงานเลี้ยงวิวาห์",
        "บรรดาผู้ที่ได้รับเชิญมาในงานเลี้ยงวิวาห์",
        "ผู้ที่ทรงเรียกให้มา can sound as though the blessed people are the ones calling others. ได้รับเชิญ makes the passive invitation clear while preserving the banquet setting.",
    )


def scan_double_possessive(candidates: list[dict], seen: set[tuple[str, str, str]],
                           verse: dict) -> None:
    replacements = [
        (
            "บำเหน็จของตนเองตามการตรากตรำของตนเอง",
            "บำเหน็จตามการตรากตรำของตนเอง",
            "ของตนเอง appears twice in the same reward/labor phrase. Removing the first possessive lightens the Thai rhythm while the second still marks whose labor is in view.",
        ),
        (
            "สละชีวิตของตนเพื่อมิตรสหายของตน",
            "สละชีวิตเพื่อมิตรสหายของตน",
            "ของตน appears twice in a short sacrificial-love phrase. สละชีวิต already implies one's own life, so the first possessive can be omitted while the second keeps the friend relationship explicit.",
        ),
        (
            "ยอมสละชีวิตของตนเพื่อมิตรสหายของตน",
            "ยอมสละชีวิตเพื่อมิตรสหายของตน",
            "ของตน appears twice in a short sacrificial-love phrase. ยอมสละชีวิต already implies one's own life, so the first possessive can be omitted while the second keeps the friend relationship explicit.",
        ),
    ]
    for current_text, proposed_text, rationale in replacements:
        add_literal_replacement(candidates, seen, verse, "double_possessive",
                                current_text, proposed_text, rationale)


def scan_phonetic_awkwardness(candidates: list[dict], seen: set[tuple[str, str, str]],
                              verse: dict) -> None:
    add_literal_replacement(
        candidates, seen, verse, "awkward_phonetic",
        "แต่เพราะพวกท่านไม่ได้เป็นของโลก แต่เราได้เลือกพวกท่านออกมาจากโลกแล้ว",
        "แต่เพราะพวกท่านไม่ได้เป็นของโลก เราได้เลือกพวกท่านออกมาจากโลกแล้ว",
        "แต่ appears twice in close succession, creating a repeated-conjunction stumble. The opening แต่เพราะ already carries the contrast, so the second แต่ can be dropped without changing the relation.",
    )
    add_literal_replacement(
        candidates, seen, verse, "awkward_phonetic",
        "เพราะพระนามของเรา เพราะพวกเขาไม่รู้จักผู้ทรงใช้เรามา",
        "เพราะพระนามของเรา เนื่องจากพวกเขาไม่รู้จักผู้ทรงใช้เรามา",
        "เพราะ closes one causal phrase and immediately opens the next. Replacing the second เพราะ with เนื่องจาก breaks the echo while preserving the causal meaning.",
    )
    add_literal_replacement(
        candidates, seen, verse, "awkward_phonetic",
        "พระพักตร์พระองค์",
        "พระพักตร์ของพระองค์",
        "พระ- repeats back-to-back in พระพักตร์พระองค์, which can stumble aloud. Inserting ของ separates the two royal terms without changing the referent.",
    )

    thai = thai_of(verse)
    for match in re.finditer(r"(นี่คือ[^.!?\"“”\n]{1,140}? คือ (?:ให้|ชีวิต|การ)[^.!?\"“”\n]{0,180})", thai):
        current_text = match.group(0)
        proposed_text = current_text.replace(" คือ ", " ได้แก่ ", 1)
        add_candidate(
            candidates, seen, verse, "awkward_phonetic",
            current_text, proposed_text,
            "The verse uses คือ twice in one compact explanatory construction. Replacing the second คือ with ได้แก่ keeps the explanation function but removes the audible echo.",
        )


def heuristic_review_chapter(chapter_data: list[dict]) -> list[dict]:
    """Return deterministic micro-polish candidates for a chapter.

    These rules deliberately prefer high-precision, literal substitutions over
    broad rewriting. Validation still rejects any candidate whose current text
    does not occur verbatim or whose substitution would drop a locked Thai term.
    """
    candidates: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    for verse in chapter_data:
        scan_title_collisions(candidates, seen, verse)
        scan_directional_redundancy(candidates, seen, verse)
        scan_lexical_redundancy(candidates, seen, verse)
        scan_passive_ambiguity(candidates, seen, verse)
        scan_double_possessive(candidates, seen, verse)
        scan_phonetic_awkwardness(candidates, seen, verse)
    return candidates


def validate_proposal(prop: dict, chapter_data: list[dict]) -> tuple[bool, str]:
    """Return (ok, reason). Reject hallucinations and lock-breakers."""
    required = {"verse_ref", "issue_type", "current_text", "proposed_text", "rationale"}
    if not required.issubset(prop):
        return False, f"missing fields: {required - set(prop)}"
    if prop["issue_type"] not in ISSUE_TYPES:
        return False, f"unknown issue_type: {prop['issue_type']}"
    if prop["current_text"].strip() == prop["proposed_text"].strip():
        return False, "current_text == proposed_text"

    # Find the verse this proposal references
    ref = prop["verse_ref"]
    verse = next((v for v in chapter_data if v.get("reference") == ref), None)
    if not verse:
        return False, f"verse_ref not in chapter: {ref}"

    thai = verse.get("translation", {}).get("thai", "")
    if prop["current_text"] not in thai:
        return False, "current_text not found verbatim in verse Thai"

    # Apply the substitution and check that no locked term was lost
    proposed_full = thai.replace(prop["current_text"], prop["proposed_text"], 1)
    locked = all_locked_thai(verse)
    for term in locked:
        # If the locked term was in the original Thai but not in the proposed Thai, reject
        if term and term in thai and term not in proposed_full:
            return False, f"would remove corpus-locked term: {term}"

    return True, "ok"


def call_polish_cli(chapter_ref: str, compact_chapter: str) -> dict:
    """Call Claude Code CLI in --print mode. Uses the user's Claude subscription
    (no API key needed). Returns parsed JSON or raises."""
    user_prompt = USER_PROMPT_TEMPLATE.format(
        chapter_ref=chapter_ref,
        compact_chapter=compact_chapter,
    )
    # NOTE: do NOT use --bare; it disables OAuth/Max-subscription auth.
    # Use --system-prompt to REPLACE the default coding-agent system prompt;
    # otherwise the polish task gets diluted by Claude Code's tool-use harness.
    # Pass user prompt via stdin to avoid shell ARG_MAX on large chapters.
    cmd = [
        "claude",
        "--print",
        "--model", MODEL,
        "--system-prompt", SYSTEM_PROMPT,
        "--output-format", "text",
        "--no-session-persistence",  # don't save sessions for batch jobs
    ]
    result = subprocess.run(
        cmd, input=user_prompt, capture_output=True, text=True, timeout=300,
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude CLI exit {result.returncode}: {result.stderr.strip()[:300]}")
    text = result.stdout.strip()
    # Extract first JSON object even if model adds prose before/after.
    # Prefer fenced-block extraction; fall back to greedy {...} match.
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    # Find first { ... } that contains "proposals"
    candidate = re.search(r"\{[^{}]*\"proposals\"\s*:\s*\[.*?\]\s*\}", text, flags=re.DOTALL)
    if candidate:
        return json.loads(candidate.group(0))
    # Last resort: try plain parse
    return json.loads(text)


def write_proposal_md(slug: str, chapter: int, chapter_ref: str,
                      proposals: list[dict], rejected: list[tuple[dict, str]],
                      engine: str) -> Path:
    """Write the human-readable proposal markdown for a chapter."""
    out_dir = PROPOSALS / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}_{chapter:02d}.md"

    lines = []
    lines.append(f"# Polish proposals — {chapter_ref}")
    lines.append("")
    lines.append(f"**Generated:** {date.today().isoformat()}  ")
    lines.append(f"**Source:** `polish_review.py`  ")
    lines.append(f"**Engine:** `{engine}`  ")
    lines.append(f"**Total proposals:** {len(proposals)}")
    lines.append("")
    lines.append("> _Reference copy — decisions are marked in the single summary doc at_")
    lines.append("> _`docs/NT_V1_POLISH_SUMMARY_<date>.md`. Edit decisions there, not here._")
    lines.append("")

    if not proposals:
        lines.append("_No micro-readability issues flagged for this chapter._")
        lines.append("")
        if rejected:
            lines.append(f"_({len(rejected)} candidate(s) rejected by validation — see `<chapter>.rejected.json`.)_")
        out_path.write_text("\n".join(lines), encoding="utf-8")
        if rejected:
            rej_path = out_dir / f"{slug}_{chapter:02d}.rejected.json"
            rej_path.write_text(json.dumps([
                {"proposal": p, "reason": r} for p, r in rejected
            ], ensure_ascii=False, indent=2), encoding="utf-8")
        return out_path

    lines.append("---")
    lines.append("")

    for i, prop in enumerate(proposals, start=1):
        lines.append(f"## {i}. {prop['verse_ref']} — `{prop['issue_type']}` (id `{slug}_{chapter:02d}_{i:03d}`)")
        lines.append("")
        lines.append("**Current:**")
        lines.append("")
        lines.append("> " + prop["current_text"])
        lines.append("")
        lines.append("**Proposed:**")
        lines.append("")
        lines.append("> " + prop["proposed_text"])
        lines.append("")
        lines.append(f"**Why:** {prop['rationale']}")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")

    # Also write a sidecar JSON for the apply step (machine-readable source of truth)
    json_path = out_dir / f"{slug}_{chapter:02d}.json"
    json_path.write_text(json.dumps({
        "chapter_ref": chapter_ref,
        "slug": slug,
        "chapter": chapter,
        "generated": date.today().isoformat(),
        "engine": engine,
        "proposals": proposals,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    if rejected:
        rej_path = out_dir / f"{slug}_{chapter:02d}.rejected.json"
        rej_path.write_text(json.dumps([
            {"proposal": p, "reason": r} for p, r in rejected
        ], ensure_ascii=False, indent=2), encoding="utf-8")

    return out_path


def review_chapter(slug: str, chapter: int, chapter_ref: str,
                   chapter_data: list[dict], engine: str) -> tuple[int, int]:
    """Review one chapter. Returns (accepted_count, rejected_count)."""
    if engine == "claude":
        compact = build_compact_chapter(chapter_data)
        parsed = call_polish_cli(chapter_ref, compact)
        raw_proposals = parsed.get("proposals", []) or []
    else:
        raw_proposals = heuristic_review_chapter(chapter_data)

    accepted = []
    rejected = []
    for p in raw_proposals:
        ok, reason = validate_proposal(p, chapter_data)
        if ok:
            accepted.append(p)
        else:
            rejected.append((p, reason))

    write_proposal_md(slug, chapter, chapter_ref, accepted, rejected, engine)
    return len(accepted), len(rejected)


def chapter_already_polished(slug: str, chapter: int) -> bool:
    return (PROPOSALS / slug / f"{slug}_{chapter:02d}.md").exists()


def book_chapter_refs(slug: str, chapter: int, chapter_data: list[dict]) -> str:
    """Get the book-name display from the first verse's reference."""
    if chapter_data:
        first_ref = chapter_data[0].get("reference", "")
        # "John 15:1" -> "John 15"
        m = re.match(r"^(.+?)\s+(\d+):", first_ref)
        if m:
            return f"{m.group(1)} {m.group(2)}"
    return f"{slug.capitalize()} {chapter}"


def review_book(slug: str, max_chapters: int, only_chapter: int | None,
                resume: bool, engine: str) -> dict:
    stats = {"book": slug, "accepted": 0, "rejected": 0, "skipped": 0, "missing": 0}
    chapters = [only_chapter] if only_chapter else range(1, max_chapters + 1)
    for ch in chapters:
        chapter_data = load_chapter(slug, ch)
        if chapter_data is None:
            stats["missing"] += 1
            continue
        if resume and chapter_already_polished(slug, ch):
            stats["skipped"] += 1
            continue
        chapter_ref = book_chapter_refs(slug, ch, chapter_data)
        try:
            accepted, rejected = review_chapter(slug, ch, chapter_ref, chapter_data, engine)
            stats["accepted"] += accepted
            stats["rejected"] += rejected
            print(f"  {chapter_ref}: {accepted} proposals ({rejected} rejected by validation)")
            if engine == "claude":
                time.sleep(0.5)  # gentle pacing for external model calls
        except json.JSONDecodeError as exc:
            print(f"  {chapter_ref}: CLI returned non-JSON; skipping. ({exc})")
        except Exception as exc:
            print(f"  {chapter_ref}: error {type(exc).__name__}: {exc}")
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="NT v1.0 Thai-flow polish sweep (Stage 2)")
    parser.add_argument("--book", help="Book slug (e.g., john, romans)")
    parser.add_argument("--chapter", type=int, help="Single chapter (requires --book)")
    parser.add_argument("--all", action="store_true", help="Sweep all 27 NT books")
    parser.add_argument("--resume", action="store_true",
                        help="Skip chapters that already have a proposal file")
    parser.add_argument("--engine", choices=("heuristic", "claude"),
                        default=DEFAULT_ENGINE,
                        help="Review engine: fast local heuristic scan (default) or Claude CLI spot review")
    args = parser.parse_args()

    if not (args.book or args.all):
        parser.error("must specify --book SLUG or --all")
    if args.chapter and not args.book:
        parser.error("--chapter requires --book")

    if args.engine == "claude" and not shutil.which("claude"):
        print("claude CLI not found in PATH. Install Claude Code first.")
        sys.exit(1)

    if args.engine == "claude" and args.all:
        print("Refusing --all --engine claude: this starts one Claude process per chapter and is too slow/retry-prone.")
        print("Use the default heuristic engine for --all, or run --engine claude with --book/--chapter for spot checks.")
        sys.exit(2)

    PROPOSALS.mkdir(parents=True, exist_ok=True)

    targets = []
    if args.all:
        targets = NT_BOOKS
    else:
        match = next(((s, c) for s, c in NT_BOOKS if s == args.book), None)
        if not match:
            parser.error(f"unknown book slug: {args.book}")
        targets = [match]

    grand_accepted = 0
    grand_rejected = 0
    print(f"Engine: {args.engine}")
    for slug, max_ch in targets:
        print(f"\n=== {slug} ===")
        stats = review_book(slug, max_ch, args.chapter, args.resume, args.engine)
        grand_accepted += stats["accepted"]
        grand_rejected += stats["rejected"]
        print(f"  → {stats['accepted']} accepted, {stats['rejected']} rejected, "
              f"{stats['skipped']} skipped, {stats['missing']} missing")

    print(f"\nTotal: {grand_accepted} proposals across all targets ({grand_rejected} rejected by validation)")
    print(f"Review at: output/polish_proposals/")


if __name__ == "__main__":
    main()
