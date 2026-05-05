#!/bin/zsh
# ship_chapter.sh — source-only chapter ship.
#
# After a chapter has been translated and passed all checks, this script:
#   1. Verifies all 9 automated checks pass for the chapter
#   2. Verifies thai-bible-ai is on main (PR #60/#61 incident guard)
#   3. Commits the chapter source artifacts to thai-bible-ai/main
#      (translation JSON, back-translation, check reports, uW notes,
#      glossary growth, OT-citation registry, etc.)
#   4. Detects "is this the last chapter of the book?" via
#      detect_book_complete.py
#      → If yes: auto-launches end-of-book audit via run_end_of_book_audit.sh,
#        which produces the §2 editorial review + §3 external AI packet on a
#        new PR branch. /loop halts after the audit so Ben can do the external
#        AI review and decide on revisions.
#      → If no: exit 0; /loop can continue to next chapter.
#
# Bundle / Vercel / iOS / Android shipping is DEFERRED to ship_book.sh —
# it runs once at book-boundary after the audit (and any revisions) merge.
# This consolidates ~16 EremosVercel2 PRs + ~16 iOS bumps per Romans-sized
# book into 1 of each, and makes "what users see in the app" atomic with
# the audited + tagged book content.
#
# Usage:
#   ship_chapter.sh <BOOK_CODE> <CHAPTER>
#   ship_chapter.sh MRK 5
#   ship_chapter.sh 1TI 4
#
# Optional flags:
#   --skip-audit          # at end-of-book, skip the auto-audit (manual review later)
#
# Exit codes:
#   0 = success (loop can continue)
#   1 = error OR end-of-book reached (loop must halt)

set -e

# --- args ---
SKIP_AUDIT=0
POSITIONAL=()
while [ $# -gt 0 ]; do
    case "$1" in
        --skip-audit) SKIP_AUDIT=1; shift ;;
        --skip-testflight|--skip-merge)
            # Compatibility no-ops — these flags only made sense in the
            # per-chapter ship era. Now ship_chapter.sh is source-only;
            # bundle/iOS work moved to ship_book.sh. Accept silently for
            # backward-compatible /loop wrappers; print one-line note.
            echo "[compat] $1 is a no-op — ship_chapter.sh is source-only as of 2026-05-02."
            shift ;;
        *) POSITIONAL+=("$1"); shift ;;
    esac
done
set -- "${POSITIONAL[@]}"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <BOOK_CODE> <CHAPTER> [--skip-audit]"
    echo "  e.g. $0 MRK 5"
    exit 1
fi

BOOK_CODE="$1"
CHAPTER="$2"
THAI_BIBLE_AI="$HOME/thai-bible-ai"

# Resolve book slug — check NT BOOKS first, then OT (extract_book_hebrew).
# Loop kickoff invokes ship_chapter.sh with the same code regardless of testament;
# the dispatcher transparently picks the right slug source.
SLUG=$(python3 -c "
import sys
sys.path.insert(0, '$THAI_BIBLE_AI/scripts')
from extract_book import BOOKS as NT_BOOKS
try:
    from extract_book_hebrew import BOOKS as OT_BOOKS
except ImportError:
    OT_BOOKS = {}
code = '$BOOK_CODE'.upper()
if code in NT_BOOKS:
    print(NT_BOOKS[code][1])
elif code in OT_BOOKS:
    print(OT_BOOKS[code][1])
else:
    print(f'ERROR: unknown book code {code}', file=sys.stderr)
    sys.exit(1)
") || exit 1

CHAPTER_PADDED=$(printf "%02d" "$CHAPTER")

# Source-commit SHA tracking, used by assert_source_commit_on_origin_main
# to verify the chapter source actually reached origin/main. Empty when
# the commit is a no-op (re-run on already-shipped chapter).
TBA_SOURCE_SHA=""

# Final pipeline assertion — added 2026-04-30 after the GAL+1TH incident.
# Now scoped to thai-bible-ai only (Eremos-side work moved to ship_book.sh).
assert_source_commit_on_origin_main() {
    local failed=0
    echo
    echo "[assert] Source commit on origin/main..."
    git -C "$THAI_BIBLE_AI" fetch origin main --quiet 2>/dev/null || true
    if [ -n "$TBA_SOURCE_SHA" ]; then
        if git -C "$THAI_BIBLE_AI" merge-base --is-ancestor "$TBA_SOURCE_SHA" origin/main 2>/dev/null; then
            echo "    ✓ thai-bible-ai source ${TBA_SOURCE_SHA:0:7} on origin/main"
        else
            echo "    ✗ thai-bible-ai source ${TBA_SOURCE_SHA:0:7} NOT on origin/main"
            echo "       origin/main: $(git -C "$THAI_BIBLE_AI" rev-parse origin/main 2>/dev/null)"
            echo "       branch:      $(git -C "$THAI_BIBLE_AI" branch --show-current 2>/dev/null)"
            failed=1
        fi
    fi
    if [ $failed -ne 0 ]; then
        echo
        echo "✗✗✗ Chapter source committed but not on origin/main — investigate."
        echo "     PR #60/#61 incident pattern (2026-04-30): silent push to wrong branch."
        exit 1
    fi
}

echo "=== Source-only chapter ship: ${BOOK_CODE} ${CHAPTER} (slug=${SLUG}) ==="
echo

# --- Pre-flight: gate on check status ---
echo "[gate] Verifying check status..."
if [ -f "$THAI_BIBLE_AI/output/translations/${SLUG}_${CHAPTER_PADDED}.json" ]; then
    if ! python3 "$THAI_BIBLE_AI/scripts/run_checks.py" --book "$BOOK_CODE" --chapter "$CHAPTER" >/dev/null 2>&1; then
        echo
        echo "✗ SHIP BLOCKED — automated checks failed for ${BOOK_CODE} ${CHAPTER}."
        echo "  See: $THAI_BIBLE_AI/output/check_reports/${SLUG}_${CHAPTER_PADDED}_review.md"
        echo "  Run: python3 scripts/revise_chapter.py --book ${BOOK_CODE} --chapter ${CHAPTER}"
        echo "  Then re-run ship_chapter.sh once revisions are clean."
        exit 1
    fi
    echo "    ✓ All checks pass."
else
    echo "    ⚠ No translation file found — nothing to ship."
    exit 0
fi

# --- Post-checks polish: optimal-equivalence semantic-rigidity scan ---
# Runs a lightweight Claude-Code review for register/idiom/wooden-passive
# rigidity. Output goes to output/polish_proposals/<slug>/<slug>_<NN>_optimal.md
# for human review at end-of-book audit time. Does NOT block ship — failures
# here are non-fatal (the script's own validation already filters
# hallucinations; on transient claude-CLI failure we just skip and log).
# Skipped if the SKIP_OPTIMAL_EQUIVALENCE env var is set (e.g., during loop
# runs where one sweep at end-of-book is preferred over per-chapter calls).
if [ -z "${SKIP_OPTIMAL_EQUIVALENCE:-}" ]; then
    echo "[post-checks] Optimal-equivalence polish scan (Claude; ~30-60s)..."
    if python3 "$THAI_BIBLE_AI/scripts/polish_optimal_equivalence.py" \
        --book "$SLUG" --chapter "$CHAPTER" --resume \
        >"/tmp/optimal_${SLUG}_${CHAPTER_PADDED}.log" 2>&1; then
        proposal_path="$THAI_BIBLE_AI/output/polish_proposals/${SLUG}/${SLUG}_${CHAPTER_PADDED}_optimal.md"
        if [ -f "$proposal_path" ]; then
            apply_count=$(grep -c "^**Decision:** pending" "$proposal_path" 2>/dev/null || echo 0)
            defer_count=$(grep -c "^**Decision:** defer-to-thai-reviewer" "$proposal_path" 2>/dev/null || echo 0)
            echo "    ✓ wrote $proposal_path (apply: $apply_count, defer: $defer_count)"
        else
            echo "    ✓ no rigidity flagged."
        fi
    else
        echo "    ⚠ optimal-equivalence scan failed (non-fatal); see /tmp/optimal_${SLUG}_${CHAPTER_PADDED}.log"
    fi
fi

# Pre-flight: warn about other uncommitted source files from prior chapters.
if [ -d "$THAI_BIBLE_AI/output" ]; then
    other_orphans=$(cd "$THAI_BIBLE_AI" && git ls-files --others --exclude-standard output/ 2>/dev/null | grep -v "${SLUG}_${CHAPTER_PADDED}" | wc -l | tr -d ' ')
    if [ "$other_orphans" -gt 0 ]; then
        echo "[gate] ⚠ ${other_orphans} uncommitted source file(s) in thai-bible-ai/output/ from other chapters."
        echo "         Review with: (cd $THAI_BIBLE_AI && git status --short output/)"
    fi
fi

# Pre-flight: thai-bible-ai MUST be on main before we commit source artifacts.
echo "[gate] Verifying thai-bible-ai is on main..."
TBA_BRANCH=$(git -C "$THAI_BIBLE_AI" branch --show-current 2>/dev/null || echo "")
if [ "$TBA_BRANCH" != "main" ]; then
    echo
    echo "✗ SHIP BLOCKED — thai-bible-ai is on '$TBA_BRANCH', not main."
    echo "  Source commits would land on the wrong branch (PR #60/#61 incident, 2026-04-30)."
    echo "  Fix:"
    echo "    cd $THAI_BIBLE_AI && git status   # confirm tree is clean"
    echo "    git checkout main && git pull"
    echo "  Then re-run this script."
    exit 1
fi
git -C "$THAI_BIBLE_AI" pull origin main 2>&1 | tail -1
echo "    ✓ thai-bible-ai on main, synced."
echo

# --- Regenerate corpus-wide derivatives so the source commit is self-consistent ---
# update_hashes.py and render_reader.py update files that downstream readers
# (Google Doc sync per reference_gdocs_sync.md, Paratext export) consume.
# build_eremos_bundle.py + iOS work moved to ship_book.sh; we don't run it here.
echo "[regen] Update HASHES.md + reader doc..."
python3 "$THAI_BIBLE_AI/scripts/update_hashes.py" 2>&1 | tail -2
python3 "$THAI_BIBLE_AI/scripts/render_reader.py" --book "$BOOK_CODE" 2>&1 | tail -2

# --- Commit source artifacts ---
# Bundles everything for THIS chapter into one source commit so the audit
# trail is clean and atomic. Per RULES §6 schema requirements.
(
    cd "$THAI_BIBLE_AI"
    git add "output/translations/${SLUG}_${CHAPTER_PADDED}.json" 2>/dev/null || true
    git add "output/back_translations/${SLUG}_${CHAPTER_PADDED}.json" 2>/dev/null || true
    git add "output/uw_notes/${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/uw_notes/${SLUG}_FRONT.md" 2>/dev/null || true
    git add "output/check_reports/${SLUG}_${CHAPTER_PADDED}_review.md" 2>/dev/null || true
    git add "output/check_reports/${SLUG}_${CHAPTER_PADDED}_summary.json" 2>/dev/null || true
    git add "output/check_reports/${SLUG}_${CHAPTER_PADDED}_iterations.txt" 2>/dev/null || true
    git add "output/check_reports/${SLUG}_${CHAPTER_PADDED}_REVISIONS_NEEDED.md" 2>/dev/null || true
    git add "output/check_reports/back_translation_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/claim_consistency_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/key_term_consistency_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/ot_citations_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/tnbt_comparison_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/summary_coverage_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    git add "output/check_reports/greek_field_integrity_${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
    # Cumulative state regenerated by checks + render
    git add HASHES.md output/reader/ output/plain/ output/feedback/ glossary.json data/nt_ot_citations.json 2>/dev/null || true
    git add output/check_reports/parallel_passages.md 2>/dev/null || true
    git add output/check_reports/phrase_consistency.md 2>/dev/null || true
    git add output/check_reports/key_term_consistency_all.md 2>/dev/null || true

    if ! git diff --cached --quiet 2>/dev/null; then
        if ! git commit -q -m "feat(${BOOK_CODE} ${CHAPTER}): source + checks + reader doc"; then
            echo "✗ thai-bible-ai source commit failed for ${BOOK_CODE} ${CHAPTER}" >&2
            exit 1
        fi
        git rev-parse HEAD > /tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha
        PUSH_OUT=$(git push origin main 2>&1)
        PUSH_EXIT=$?
        echo "$PUSH_OUT" | tail -1
        if [ $PUSH_EXIT -ne 0 ]; then
            echo "✗ thai-bible-ai push to origin/main failed (exit $PUSH_EXIT):" >&2
            echo "$PUSH_OUT" >&2
            exit 1
        fi
    else
        echo "    (no source changes — chapter already committed)"
    fi
) || exit 1

if [ -f "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha" ]; then
    TBA_SOURCE_SHA=$(cat "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha")
    rm -f "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha"
fi

assert_source_commit_on_origin_main

echo
echo "✓ Source ship complete for ${BOOK_CODE} ${CHAPTER}."
echo "  Bundle / Vercel / iOS / Android deferred to ship_book.sh at book-boundary."

# --- End-of-book detection ---
# If this chapter is the LAST in its book:
#   1. detect_book_complete.py writes the audit prompt + signal file, exits 1
#   2. We auto-launch run_end_of_book_audit.sh --print, which spawns a fresh
#      Claude session that produces §2 audit doc + §3 external AI packet on
#      a new PR branch
#   3. /loop halts (we exit 1) so Ben can do external AI review + decide
#      revisions before lock-the-book ship
echo
echo "[end-of-book check] $BOOK_CODE $CHAPTER..."
set +e
python3 "$THAI_BIBLE_AI/scripts/detect_book_complete.py" "$BOOK_CODE" "$CHAPTER"
DETECT_EXIT=$?
set -e

if [ $DETECT_EXIT -ne 1 ]; then
    # Not the last chapter — /loop can continue to next chapter.
    exit 0
fi

# Last chapter of the book.
if [ $SKIP_AUDIT -eq 1 ]; then
    echo
    echo "[--skip-audit set] End-of-book audit not auto-launched."
    echo "  Run manually when ready: bash scripts/run_end_of_book_audit.sh $BOOK_CODE"
    exit 1
fi

echo
echo "[end-of-book audit] Auto-launching for $BOOK_CODE..."
echo "  Spawns a fresh Claude session via 'claude --print < audit_prompt.md'."
echo "  The subagent produces §1 mechanical-gate verification, §2 editorial"
echo "  audit doc, and §3 external AI packet on a new PR branch."
echo "  Expected duration: 5-15 min."
echo
set +e
bash "$THAI_BIBLE_AI/scripts/run_end_of_book_audit.sh" "$BOOK_CODE" --print
AUDIT_EXIT=$?
set -e

echo
if [ $AUDIT_EXIT -eq 0 ]; then
    echo "✓ End-of-book audit complete."
    echo "  Review the audit PR + external AI packet at:"
    echo "    docs/end_of_book/$(echo "$SLUG")/"
    echo "  Halting /loop here for external AI review."
    echo "  After revisions (if any) merge, run:"
    echo "    bash scripts/ship_book.sh $BOOK_CODE"
    echo "  to ship bundle / Vercel / iOS / tag book-${SLUG}-v1."
elif [ $AUDIT_EXIT -eq 3 ]; then
    echo "✗ End-of-book audit BLOCKED by inclusion-variant gate."
    echo "  See output above for unresolved candidates."
    echo "  Halting /loop."
else
    echo "⚠ End-of-book audit exited $AUDIT_EXIT — manual recovery needed."
    echo "  Halting /loop."
fi

# Halt /loop regardless — book-boundary is the natural stop point
exit 1
