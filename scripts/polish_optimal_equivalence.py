#!/usr/bin/env python3
"""
Optimal-Equivalence polish review (Stage 3 — semantic-rigidity scan).

Sibling to scripts/polish_review.py — same plumbing, different axis. Where
polish_review.py catches MICRO-readability stumbles (phonetic doublets,
redundant directionals, title collisions), THIS script catches SEMANTIC
rigidity: places where a literal rendering of the Greek lands woodenly in
Thai, and a more natural rendering would carry the same meaning + theology
without sacrificing accuracy.

Triggered by Gemini's 2026-05-05 Jn 15 review which scored Eremos lower than
THSV2011 on the μένω → คงอยู่ vs ติดสนิท axis. Hypothesis: Eremos has thousands
of locked decisions where the formal-vs-dynamic call was made deliberately,
but some literal renderings shipped without the corresponding `key_decisions`
entry justifying them — those are the catchable wins.

Engine: Claude Code subprocess (--print mode), uses the user's Claude Max
subscription. Same auth contract as polish_review.py's --engine claude path.
Reasonable for sample runs (3-10 chapters); not designed for --all (one
process per chapter is too slow / retry-prone).

Output: output/polish_proposals/<slug>/<slug>_<NN>_optimal.md
  Separate from the heuristic-pass <slug>_<NN>.md so issue-types don't
  collide. Both files are picked up by build_polish_summary.py.

Validation gates (rejects hallucinations before writing):
  - `current_text` must appear verbatim in the verse's Thai field
  - Any term from the verse's `key_decisions[].thai` value (corpus-locked)
    must still appear in `proposed_text`
  - Three confidence buckets: apply / defer_to_native / fyi
    Only `apply`-bucket proposals get written as full POLISH_PROPOSAL blocks
    that the apply-script would land. `defer_to_native` proposals get a
    DEFER block (decision-pending; routed through normal review). `fyi` are
    informational, not actionable.

Usage:
  python3 scripts/polish_optimal_equivalence.py --book john --chapter 15
  python3 scripts/polish_optimal_equivalence.py --book romans --chapter 8
  python3 scripts/polish_optimal_equivalence.py --book john          # whole book
  python3 scripts/polish_optimal_equivalence.py --book john --chapter 15 --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
PROPOSALS = ROOT / "output" / "polish_proposals"
DECISIONS_DIR = ROOT / "docs" / "translator_decisions"

MODEL = "claude-sonnet-4-6"  # cheaper + fast enough for polish work
TIMEOUT_SEC = 600

CONFIDENCE_BUCKETS = {"apply", "defer_to_native", "fyi"}


SYSTEM_PROMPT = """You are a Thai-language Bible-translation editor performing an **Optimal Equivalence** polish review on an already-finalized Eremos Thai NT translation.

The translation is shipped from SBLGNT Greek with deliberate philosophical stance: **optimal equivalence** (faithful to the Greek + natural in modern Thai). The corpus has a sibling translator-decisions ledger that locks hundreds of theological and lexical choices. Your scan looks for places where a literal Greek-shape rendering shipped without a documented justification AND where a more idiomatic Thai rendering would carry the same meaning more naturally.

What you are looking for (one closed list — proposal MUST match one):

1. **rigid_metaphor** — a Greek metaphor rendered word-for-word in Thai where Thai has a more vivid native equivalent that carries the SAME image. Canonical example: μένω in vine-and-branches ("abide" → คงอยู่ vs ติดสนิท "graft-attach"). Only flag if the proposed Thai is at least as faithful to the Greek meaning AND clearly more natural.

2. **conjunction_overload** — Greek discourse markers (καί, γάρ, δέ, οὖν, ὅτι, ἵνα) all flattened to Thai connectives that pile up. The proposal drops or varies one connector to break the pile-up while preserving logical relation.

3. **wooden_passive** — Greek perfect/aorist passive rendered as a heavy Thai passive (ถูก-, ได้รับ-) in a context where Thai natively prefers active voice or an agent-fronted construction.

4. **literal_idiom** — Greek idiomatic phrase rendered word-for-word, where the Thai surface carries no metaphor that a Thai reader would catch. Propose a Thai natural equivalent that renders the IDIOM-MEANING, not the words. Only flag clear cases (e.g., σπλάγχνα "bowels-as-emotion" → ใจ, NOT word-by-word "ลำไส้").

5. **register_drift** — a verse's register has slipped from optimal-evangelical-formal to either translationese-stiff (overly literal academic) or colloquial-loose (chat-speak). Optimal target is the THSV2011 register: respectful, modern, accessible.

ABSOLUTE RULES (read carefully — they prevent noisy proposals):

- **READ THE EXISTING `key_decisions` FIRST.** Every verse arrives with translator rationales. If the rationale already documents the literal-rendering choice (corpus-lock, theological reason, cross-corpus echo, hapax handling, key-term consistency, etc.), DO NOT propose a change. The translator already considered the alternative and chose the literal for reason. Trust the rationale.

- **PRESERVE LOCKED `key_decisions[].thai` TERMS VERBATIM.** Any Thai phrase appearing as `kd.thai` must appear unchanged in your `proposed_text`. The rest of the verse is fair game for polish.

- **DO NOT propose theological changes.** Theology is locked. Optimal equivalence improves the SURFACE rendering of meaning — never the meaning itself.

- **DO NOT change Tetragrammaton, divine names, ราชาศัพท์ (ทรง- prefixes, royal Thai vocabulary), or other corpus-locked vocabulary.** If you're tempted, you've drifted from polish into rewrite.

- **`current_text` must be a verbatim substring (character-for-character)** of the verse's `translation.thai`. If you can't find the exact substring, do not propose.

- **Three confidence buckets — be honest about which:**
  - `apply` — clearly natural improvement, no register/feel ambiguity, ready to ship if the translator approves.
  - `defer_to_native` — the change is plausibly better but turns on Thai naturalness/register that requires a native ear. The translator should route this to the Tier-A Thai-language reviewer.
  - `fyi` — surfacing a candidate the translator may want to consider but you do NOT recommend changing yet (e.g., would require a corpus-wide normalization pass beyond this single verse).

- **Bias toward fewer, higher-quality proposals.** A run that surfaces 3 strong proposals is better than a run that surfaces 30 mediocre ones. The translator's bandwidth is finite; respect it.

- **Skip the verse entirely** if it's already optimal. Empty proposals array is the right answer for chapters that are well-rendered.

OUTPUT: Strict JSON. No prose outside JSON. No markdown fences. No commentary. Schema:

{
  "chapter_ref": "<Book Chapter>",
  "proposals": [
    {
      "verse_ref": "<Book Chapter:Verse>",
      "issue_type": "<one of the five closed types>",
      "confidence": "<apply | defer_to_native | fyi>",
      "current_text": "<EXACT verbatim Thai substring of translation.thai>",
      "proposed_text": "<the more idiomatic Thai>",
      "greek_lemma_focus": "<the Greek word(s) at the root of the rigidity, e.g., μένω, σπλάγχνα>",
      "rationale": "<2-4 sentences: why current is rigid; how proposed reads more naturally; why proposed still preserves the Greek meaning + any locked terms; why this is NOT a theological change.>"
    }
  ]
}

Walk the chapter verse by verse. For each verse, FIRST read its `key_decisions` rationale; SKIP if the rationale already justifies the literal rendering. Then check the five issue types. Return all valid proposals in confidence-ranked order (`apply` first, then `defer_to_native`, then `fyi`). An empty proposals array is the right answer for chapters that are already optimal."""


USER_PROMPT_TEMPLATE = """Chapter to review: **{chapter_ref}**

For each verse below you have: ref + Thai + Greek + (compressed) key_decisions rationale + locked Thai phrases (must be preserved verbatim).

{compact_chapter}

Review the Thai text for the five Optimal-Equivalence issue types. **Read the key_decisions rationale FIRST** for every verse — if the literal rendering is already justified there, skip the verse. Return strict JSON only. Empty proposals array is fine if you found nothing."""


def load_chapter(slug: str, chapter: int) -> list[dict] | None:
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def thai_of(verse: dict) -> str:
    return verse.get("translation", {}).get("thai", "") or ""


def all_locked_thai(verse: dict) -> set[str]:
    locked = set()
    kds = verse.get("translation", {}).get("key_decisions", []) or []
    for kd in kds:
        thai = (kd or {}).get("thai")
        if thai:
            locked.add(thai.strip())
    return locked


def build_compact_chapter(chapter_data: list[dict]) -> str:
    """Per-verse compressed view: ref + Thai + Greek + key_decisions
    rationale + locked phrases. Bigger than polish_review's compact view
    because optimal-equivalence needs the rationale chain to avoid
    re-proposing what's already documented."""
    out = []
    for v in chapter_data:
        ref = v.get("reference", "?")
        thai = thai_of(v)
        greek = v.get("greek", "")
        out.append(f"### {ref}")
        out.append(f"Greek: {greek}")
        out.append(f"Thai:  {thai}")
        kds = v.get("translation", {}).get("key_decisions") or []
        for i, kd in enumerate(kds, start=1):
            g = (kd.get("greek") or "").strip()
            t = (kd.get("thai") or "").strip()
            r = (kd.get("rationale") or "").strip()
            # Compress rationale to first ~250 chars to keep the prompt lean
            r_short = (r[:250] + "…") if len(r) > 250 else r
            out.append(f"  KD{i}: greek={g!r} thai={t!r}")
            if r_short:
                out.append(f"        rationale: {r_short}")
        locked = sorted(all_locked_thai(v))
        if locked:
            out.append("Locked Thai (must preserve verbatim): " + " | ".join(locked))
        out.append("")
    return "\n".join(out)


def call_claude(chapter_ref: str, compact_chapter: str) -> dict:
    """Subprocess Claude Code in --print mode. Uses Max-subscription auth."""
    user_prompt = USER_PROMPT_TEMPLATE.format(
        chapter_ref=chapter_ref,
        compact_chapter=compact_chapter,
    )
    cmd = [
        "claude",
        "--print",
        "--model", MODEL,
        "--system-prompt", SYSTEM_PROMPT,
        "--output-format", "text",
        "--no-session-persistence",
    ]
    result = subprocess.run(
        cmd, input=user_prompt, capture_output=True, text=True,
        timeout=TIMEOUT_SEC,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"claude CLI exit {result.returncode}: "
            f"{result.stderr.strip()[:300]}"
        )
    text = result.stdout.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fence:
        return json.loads(fence.group(1))
    obj = re.search(r"\{[^{}]*\"proposals\"\s*:\s*\[.*?\]\s*\}", text, flags=re.DOTALL)
    if obj:
        return json.loads(obj.group(0))
    return json.loads(text)


REQUIRED_PROP_FIELDS = {
    "verse_ref", "issue_type", "confidence", "current_text",
    "proposed_text", "rationale",
}
ALLOWED_ISSUE_TYPES = {
    "rigid_metaphor", "conjunction_overload", "wooden_passive",
    "literal_idiom", "register_drift",
}


def validate_proposal(prop: dict, chapter_data: list[dict]) -> tuple[bool, str]:
    """Return (ok, reason). Mirrors polish_review.validate_proposal but
    extends with the confidence-bucket check."""
    if not isinstance(prop, dict):
        return False, "not a dict"
    missing = REQUIRED_PROP_FIELDS - set(prop.keys())
    if missing:
        return False, f"missing fields: {sorted(missing)}"
    if prop["issue_type"] not in ALLOWED_ISSUE_TYPES:
        return False, f"unknown issue_type: {prop['issue_type']}"
    if prop["confidence"] not in CONFIDENCE_BUCKETS:
        return False, f"unknown confidence: {prop['confidence']}"

    ref = prop["verse_ref"]
    verse = next((v for v in chapter_data if v.get("reference") == ref), None)
    if not verse:
        return False, f"verse_ref not in chapter: {ref}"

    thai = thai_of(verse)
    if prop["current_text"] not in thai:
        return False, "current_text not found verbatim in verse Thai"

    proposed_full = thai.replace(prop["current_text"], prop["proposed_text"], 1)
    locked = all_locked_thai(verse)
    for term in locked:
        if term and term in thai and term not in proposed_full:
            return False, f"would remove corpus-locked term: {term}"

    return True, "ok"


def write_proposal_md(slug: str, chapter: int, chapter_ref: str,
                      proposals: list[dict],
                      rejected: list[tuple[dict, str]]) -> Path:
    """Write the human-readable proposal markdown for a chapter, segregated
    by confidence bucket so the reviewer can scan high-confidence first."""
    out_dir = PROPOSALS / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}_{chapter:02d}_optimal.md"

    lines = []
    lines.append(f"# Optimal-Equivalence proposals — {chapter_ref}")
    lines.append("")
    lines.append(f"**Generated:** {date.today().isoformat()}  ")
    lines.append(f"**Source:** `polish_optimal_equivalence.py`  ")
    lines.append(f"**Engine:** `claude` ({MODEL})  ")
    lines.append(f"**Total proposals:** {len(proposals)}")
    if rejected:
        lines.append(f"**Rejected at validation:** {len(rejected)} (see `<chapter>_optimal.rejected.json`)")
    lines.append("")
    lines.append("> _Reference copy — decisions are marked in the single summary doc at_")
    lines.append("> _`docs/NT_V1_POLISH_SUMMARY_<date>.md` after running `build_polish_summary.py`._")
    lines.append("")

    if not proposals:
        lines.append("_No optimal-equivalence rigidity flagged for this chapter — already at target register / Greek-shape natural in Thai._")
        lines.append("")
        out_path.write_text("\n".join(lines), encoding="utf-8")
        if rejected:
            rej_path = out_dir / f"{slug}_{chapter:02d}_optimal.rejected.json"
            rej_path.write_text(json.dumps(
                [{"proposal": p, "reason": r} for p, r in rejected],
                ensure_ascii=False, indent=2,
            ), encoding="utf-8")
        return out_path

    # Group by confidence
    buckets = {"apply": [], "defer_to_native": [], "fyi": []}
    for p in proposals:
        buckets.setdefault(p.get("confidence", "fyi"), []).append(p)

    for bucket, label in [
        ("apply", "✅ APPLY — high-confidence, ready to land"),
        ("defer_to_native", "🇹🇭 DEFER TO NATIVE — needs Tier-A Thai-language reviewer"),
        ("fyi", "📋 FYI — informational, not recommended for application"),
    ]:
        bucket_props = buckets.get(bucket, [])
        if not bucket_props:
            continue
        lines.append(f"## {label} — {len(bucket_props)}")
        lines.append("")
        for i, prop in enumerate(bucket_props, start=1):
            pid = f"{slug}_{chapter:02d}_optimal_{i:03d}"
            lines.append(f"<!-- POLISH_PROPOSAL id={pid} -->")
            lines.append(f"### {prop['verse_ref']} — `{prop['issue_type']}` ({pid})")
            lines.append("")
            if prop.get("greek_lemma_focus"):
                lines.append(f"**Greek lemma:** `{prop['greek_lemma_focus']}`")
                lines.append("")
            lines.append("**Current:**")
            lines.append("")
            lines.append(f"> {prop['current_text']}")
            lines.append("")
            lines.append("**Proposed:**")
            lines.append("")
            lines.append(f"> {prop['proposed_text']}")
            lines.append("")
            lines.append(f"**Why:** {prop['rationale']}")
            lines.append("")
            if bucket == "apply":
                lines.append("**Decision:** pending")
            elif bucket == "defer_to_native":
                lines.append("**Decision:** defer-to-thai-reviewer")
            else:
                lines.append("**Decision:** fyi")
            lines.append("")
            lines.append("<!-- /POLISH_PROPOSAL -->")
            lines.append("")
            lines.append("---")
            lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")

    if rejected:
        rej_path = out_dir / f"{slug}_{chapter:02d}_optimal.rejected.json"
        rej_path.write_text(json.dumps(
            [{"proposal": p, "reason": r} for p, r in rejected],
            ensure_ascii=False, indent=2,
        ), encoding="utf-8")

    sidecar = out_dir / f"{slug}_{chapter:02d}_optimal.json"
    sidecar.write_text(json.dumps({
        "chapter_ref": chapter_ref,
        "engine": "claude",
        "model": MODEL,
        "generated_at": date.today().isoformat(),
        "proposals": proposals,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    return out_path


def review_chapter(slug: str, chapter: int, dry_run: bool, resume: bool = False) -> tuple[int, int, int]:
    # Resume support: skip chapters that already have an _optimal.md output.
    # Lets the NT-wide sweep restart cleanly across multiple sessions when
    # the Max-subscription rate-limit window forces a pause.
    out_path = PROPOSALS / slug / f"{slug}_{chapter:02d}_optimal.md"
    if resume and out_path.exists():
        print(f"\n--- skipping {slug} ch.{chapter} (resume: {out_path.name} exists) ---")
        return 0, 0, 0

    chapter_data = load_chapter(slug, chapter)
    if chapter_data is None:
        print(f"  no translation file for {slug} {chapter}; skipping")
        return 0, 0, 0

    chapter_ref = chapter_data[0].get("reference", f"{slug} {chapter}").rsplit(":", 1)[0]
    compact = build_compact_chapter(chapter_data)

    if dry_run:
        print(f"\n--- DRY RUN: {chapter_ref} ---")
        print(f"  Compact context: {len(compact):,} chars")
        print(f"  Verse count: {len(chapter_data)}")
        print(f"  Skipping Claude call.")
        return 0, 0, 0

    print(f"\n=== {chapter_ref} ===")
    print(f"  Compact context: {len(compact):,} chars / {len(chapter_data)} verses")
    print(f"  Calling claude --print (model={MODEL}, timeout={TIMEOUT_SEC}s)...")
    try:
        response = call_claude(chapter_ref, compact)
    except (RuntimeError, json.JSONDecodeError, subprocess.TimeoutExpired) as e:
        print(f"  ✗ Claude call failed: {type(e).__name__}: {str(e)[:200]}")
        return 0, 0, 0

    raw_proposals = response.get("proposals", [])
    accepted = []
    rejected = []
    for prop in raw_proposals:
        ok, reason = validate_proposal(prop, chapter_data)
        if ok:
            accepted.append(prop)
        else:
            rejected.append((prop, reason))

    out_path = write_proposal_md(slug, chapter, chapter_ref, accepted, rejected)
    apply_count = sum(1 for p in accepted if p.get("confidence") == "apply")
    defer_count = sum(1 for p in accepted if p.get("confidence") == "defer_to_native")
    fyi_count = sum(1 for p in accepted if p.get("confidence") == "fyi")
    print(f"  → wrote {out_path}")
    print(f"  proposals: {len(accepted)} accepted ({apply_count} apply, {defer_count} defer, {fyi_count} fyi), {len(rejected)} rejected")
    return apply_count, defer_count, fyi_count


def chapter_count_for_book(slug: str) -> int:
    nt = {
        "matthew": 28, "mark": 16, "luke": 24, "john": 21, "acts": 28,
        "romans": 16, "1corinthians": 16, "2corinthians": 13, "galatians": 6,
        "ephesians": 6, "philippians": 4, "colossians": 4, "1thessalonians": 5,
        "2thessalonians": 3, "1timothy": 6, "2timothy": 4, "titus": 3,
        "philemon": 1, "hebrews": 13, "james": 5, "1peter": 5, "2peter": 3,
        "1john": 5, "2john": 1, "3john": 1, "jude": 1, "revelation": 22,
    }
    return nt.get(slug, 0)


NT_SLUGS = [
    "matthew", "mark", "luke", "john", "acts",
    "romans", "1corinthians", "2corinthians", "galatians", "ephesians",
    "philippians", "colossians", "1thessalonians", "2thessalonians",
    "1timothy", "2timothy", "titus", "philemon", "hebrews",
    "james", "1peter", "2peter", "1john", "2john", "3john", "jude",
    "revelation",
]


def main():
    parser = argparse.ArgumentParser(
        description="Optimal-Equivalence semantic-rigidity polish review")
    book_group = parser.add_mutually_exclusive_group(required=True)
    book_group.add_argument("--book", help="Book slug (e.g., john)")
    book_group.add_argument("--all-nt", action="store_true",
                            help="Sweep all 27 NT books (resume-aware)")
    parser.add_argument("--chapter", type=int, help="Chapter number (whole book if omitted)")
    parser.add_argument("--dry-run", action="store_true", help="Build context but skip Claude call")
    parser.add_argument("--resume", action="store_true",
                        help="Skip chapters that already have an _optimal.md output (safe restart for sweeps)")
    args = parser.parse_args()

    if not args.dry_run and not shutil.which("claude"):
        print("claude CLI not found in PATH. Install Claude Code first.")
        return 1

    if args.all_nt:
        if args.chapter is not None:
            print("--all-nt and --chapter are mutually exclusive")
            return 1
        # Implicit --resume for sweeps so a re-run after rate-limit pause is safe.
        resume = True
        plan = []
        for slug in NT_SLUGS:
            for ch in range(1, chapter_count_for_book(slug) + 1):
                plan.append((slug, ch))
        print(f"=== NT sweep: {len(plan)} chapters across {len(NT_SLUGS)} books "
              f"(resume-aware; will skip chapters with existing _optimal.md) ===")
    else:
        slug = args.book.lower()
        chapters = ([args.chapter] if args.chapter else list(range(1, chapter_count_for_book(slug) + 1)))
        if not chapters:
            print(f"unknown book slug: {slug}")
            return 1
        plan = [(slug, ch) for ch in chapters]
        resume = args.resume

    totals = [0, 0, 0]
    for slug, ch in plan:
        a, d, f = review_chapter(slug, ch, args.dry_run, resume=resume)
        totals[0] += a
        totals[1] += d
        totals[2] += f

    print()
    label = "NT sweep" if args.all_nt else args.book
    print(f"=== {label} totals: {totals[0]} apply / {totals[1]} defer-to-native / {totals[2]} fyi ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
