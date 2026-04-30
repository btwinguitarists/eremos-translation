#!/bin/zsh
# ship_chapter.sh — fully-automated end-of-translation ship pipeline.
#
# After a chapter has been translated and passed all checks, this script:
#   1. Pulls latest main in EremosVercel2 (so we don't overwrite recent merges)
#   2. Rebuilds the eremos_translation.json bundle from all translated chapters
#   3. If bundle changed: branches, commits, pushes, opens PR, auto-merges
#   4. Bumps iOS CURRENT_PROJECT_VERSION (auto-detects next available number)
#   5. Builds web + cap syncs iOS
#   6. Archives, exports, uploads to TestFlight via altool
#   7. Commits version bump to main
#
# Usage:
#   ship_chapter.sh <BOOK_CODE> <CHAPTER>
#   ship_chapter.sh MRK 5
#   ship_chapter.sh 1TI 4
#
# Optional flags:
#   --skip-testflight     # ship to Vercel only; skip iOS build (~10x faster)
#   --skip-merge          # open PR but don't auto-merge (for manual review)
#
# Exit codes:
#   0 = success (or "nothing to ship")
#   1 = error (any step failed)

set -e

# --- Apple / App Store Connect credentials (env-driven for public-repo safety) ---
# These are sourced from the user's environment (Claude Code loads them from
# ~/.claude/settings.json via its `env` block). If you run this script outside
# Claude Code, export them in your shell or a local .env before invoking.
#
#   APP_STORE_CONNECT_KEY_ID         — e.g. ABC12345 (the 10-char key identifier)
#   APP_STORE_CONNECT_ISSUER_ID      — UUID issued by Apple to your team
#   APP_STORE_CONNECT_API_KEY_PATH   — absolute path to AuthKey_<KEY_ID>.p8
#   APPLE_DEVELOPMENT_TEAM           — 10-char Apple Developer Team ID
#
# These values were previously hardcoded; they were moved to env vars before
# this repo was made public (2026-04-17) to avoid exposing them in git history.
: "${APP_STORE_CONNECT_KEY_ID:?APP_STORE_CONNECT_KEY_ID not set — see settings.json or shell env}"
: "${APP_STORE_CONNECT_ISSUER_ID:?APP_STORE_CONNECT_ISSUER_ID not set}"
: "${APP_STORE_CONNECT_API_KEY_PATH:?APP_STORE_CONNECT_API_KEY_PATH not set}"
: "${APPLE_DEVELOPMENT_TEAM:?APPLE_DEVELOPMENT_TEAM not set}"

# --- args ---
SKIP_TESTFLIGHT=0
SKIP_MERGE=0
POSITIONAL=()
while [ $# -gt 0 ]; do
    case "$1" in
        --skip-testflight) SKIP_TESTFLIGHT=1; shift ;;
        --skip-merge) SKIP_MERGE=1; shift ;;
        *) POSITIONAL+=("$1"); shift ;;
    esac
done
set -- "${POSITIONAL[@]}"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <BOOK_CODE> <CHAPTER> [--skip-testflight] [--skip-merge]"
    echo "  e.g. $0 MRK 5"
    exit 1
fi

BOOK_CODE="$1"
CHAPTER="$2"
THAI_BIBLE_AI="$HOME/thai-bible-ai"
EREMOS_REPO="$HOME/EremosVercel2"

# Resolve book slug from extract_book.py BOOKS table
SLUG=$(python3 -c "
import sys
sys.path.insert(0, '$THAI_BIBLE_AI/scripts')
from extract_book import BOOKS
code = '$BOOK_CODE'.upper()
if code not in BOOKS:
    print(f'ERROR: unknown book code {code}', file=sys.stderr)
    sys.exit(1)
print(BOOKS[code][1])
") || exit 1

CHAPTER_PADDED=$(printf "%02d" "$CHAPTER")
BRANCH="feat/eremos-translation-${SLUG}-${CHAPTER}"
PR_TITLE="feat: Eremos Translation — ${BOOK_CODE} ${CHAPTER}"

# Per-ship-pipeline SHA tracking, used by assert_chapter_commits_on_origin_main
# to verify both repos' chapter commits actually reached origin/main. Empty
# when the ship is a no-op (e.g., bundle unchanged) or when commits are
# skipped — the assertion treats empty as "nothing to verify".
TBA_SOURCE_SHA=""        # thai-bible-ai source-artifact commit SHA
EREMOS_CHAPTER_SHA=""    # EremosVercel2 chapter-bundle commit SHA (PR-merged)
EREMOS_BUMP_SHA=""       # EremosVercel2 iOS-bump commit SHA (direct-to-main)

# Final pipeline assertion — added 2026-04-30 after the GAL+1TH incident
# where 20 chapter source commits silently piled up on a feature branch
# instead of landing on main per-chapter (PRs #60/#61 had to batch-merge
# them). Runs before any "ship complete" message so we fail loud rather
# than declaring success and continuing the loop on stale state.
assert_chapter_commits_on_origin_main() {
    local failed=0
    echo
    echo "[assert] Chapter commits on origin/main..."

    # Refresh remote refs to be sure origin/main is current.
    git -C "$THAI_BIBLE_AI" fetch origin main --quiet 2>/dev/null || true
    git -C "$EREMOS_REPO" fetch origin main --quiet 2>/dev/null || true

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

    if [ -n "$EREMOS_CHAPTER_SHA" ]; then
        if git -C "$EREMOS_REPO" merge-base --is-ancestor "$EREMOS_CHAPTER_SHA" origin/main 2>/dev/null; then
            echo "    ✓ EremosVercel2 chapter ${EREMOS_CHAPTER_SHA:0:7} reachable from origin/main"
        else
            echo "    ✗ EremosVercel2 chapter ${EREMOS_CHAPTER_SHA:0:7} NOT reachable from origin/main"
            echo "       origin/main: $(git -C "$EREMOS_REPO" rev-parse origin/main 2>/dev/null)"
            failed=1
        fi
    fi

    if [ -n "$EREMOS_BUMP_SHA" ]; then
        if git -C "$EREMOS_REPO" merge-base --is-ancestor "$EREMOS_BUMP_SHA" origin/main 2>/dev/null; then
            echo "    ✓ EremosVercel2 iOS bump ${EREMOS_BUMP_SHA:0:7} on origin/main"
        else
            echo "    ✗ EremosVercel2 iOS bump ${EREMOS_BUMP_SHA:0:7} NOT on origin/main"
            failed=1
        fi
    fi

    if [ $failed -ne 0 ]; then
        echo
        echo "✗✗✗ Chapter shipped but not on origin/main — investigate."
        echo "     PR #60/#61 incident pattern (2026-04-30): silent push to wrong branch."
        echo "     Likely causes: (a) wrong-branch checkout, (b) push rejected,"
        echo "     (c) merge skipped/squashed differently than expected."
        exit 1
    fi
}

echo "=== Ship pipeline: ${BOOK_CODE} ${CHAPTER} (slug=${SLUG}) ==="
echo

# --- Pre-flight: gate on check status ---
# Per RULES.md §7, all 5 automated checks must pass before shipping.
# This gate enforces it — no more "trust the chat" to have run checks.
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
    echo "    ⚠ No translation file found — skipping check (assuming bundle-only ship)."
fi

# Pre-flight: warn about other uncommitted source files from prior chapters.
# This script auto-commits THIS chapter's artifacts (see step after rebuild
# below), but pre-existing orphans need manual cleanup. Added 2026-04-19
# after discovering 14 orphaned chapters from past sessions that exited
# before committing.
if [ -d "$THAI_BIBLE_AI/output" ]; then
    other_orphans=$(cd "$THAI_BIBLE_AI" && git ls-files --others --exclude-standard output/ 2>/dev/null | grep -v "${SLUG}_${CHAPTER_PADDED}" | wc -l | tr -d ' ')
    if [ "$other_orphans" -gt 0 ]; then
        echo "[gate] ⚠ ${other_orphans} uncommitted source file(s) in thai-bible-ai/output/ from other chapters."
        echo "         Review with: (cd $THAI_BIBLE_AI && git status --short output/)"
    fi
fi

# Pre-flight: thai-bible-ai MUST be on main before we commit source artifacts.
# Added 2026-04-30 after the GAL+1TH incident: a prior Claude session left
# the repo on `end-of-book-review-galatians`, ship_chapter.sh dutifully
# committed source to that branch (no pre-check), and 20 accumulated commits
# had to be batch-merged via PRs #60/#61 instead of landing per-chapter on
# main. Hard-gate prevents recurrence.
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

# --- 1. Pull latest main ---
echo "[1/7] Pull latest main in EremosVercel2..."
cd "$EREMOS_REPO"
git checkout main >/dev/null 2>&1
git pull origin main 2>&1 | tail -1

# --- 2. Rebuild bundle + update verification hashes + regen reader doc ---
echo "[2/7] Rebuild bundle, update HASHES.md, regenerate reader doc..."
python3 "$THAI_BIBLE_AI/scripts/build_eremos_bundle.py" 2>&1 | tail -3
python3 "$THAI_BIBLE_AI/scripts/update_hashes.py" 2>&1 | tail -2
python3 "$THAI_BIBLE_AI/scripts/render_reader.py" --book "$BOOK_CODE" 2>&1 | tail -2

# Commit source artifacts + cumulative state in thai-bible-ai (separate
# from the Eremos bundle commit, which lands in EremosVercel2). Bundles
# everything for THIS chapter into one source commit so the audit trail
# is clean and atomic. Signed via configured GPG key.
#
# Added 2026-04-19 after discovering 14 chapters with orphaned source
# files (sessions exited before committing). The prior version of this
# block only committed HASHES.md + output/reader/, leaving translation
# JSON, back-translations, check reports, and uw_notes for the chat
# session to commit — which often did not happen. Now the ship is the
# source of truth: if it succeeded, the source is in git.
(
    cd "$THAI_BIBLE_AI"
    # Per-chapter source artifacts (each || true so set -e doesn't abort
    # on a missing file)
    git add "output/translations/${SLUG}_${CHAPTER_PADDED}.json" 2>/dev/null || true
    git add "output/back_translations/${SLUG}_${CHAPTER_PADDED}.json" 2>/dev/null || true
    git add "output/uw_notes/${SLUG}_${CHAPTER_PADDED}.md" 2>/dev/null || true
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
    # Cumulative state updated by checks (glossary growth, OT citation registry,
    # synoptic parallels regenerated across all books on every ship). output/plain/
    # and output/feedback/ are also regenerated derivatives — added 2026-04-30
    # after PR #66 had to clean up an orphaned 1TH 5 refresh.
    git add HASHES.md output/reader/ output/plain/ output/feedback/ glossary.json data/nt_ot_citations.json 2>/dev/null || true
    git add output/check_reports/parallel_passages.md 2>/dev/null || true

    if ! git diff --cached --quiet 2>/dev/null; then
        # Hard-fail on commit/push errors (was `|| true` pre-2026-04-30 — that
        # masked the GAL/1TH wrong-branch bug). The pre-flight gate above
        # ensures we're on main, so a commit-or-push failure now is real.
        if ! git commit -q -m "feat(${BOOK_CODE} ${CHAPTER}): source + checks + reader doc + bundle hashes"; then
            echo "✗ thai-bible-ai source commit failed for ${BOOK_CODE} ${CHAPTER}" >&2
            exit 1
        fi
        # Save the new SHA for the post-ship assertion
        git rev-parse HEAD > /tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha
        PUSH_OUT=$(git push origin main 2>&1)
        PUSH_EXIT=$?
        echo "$PUSH_OUT" | tail -1
        if [ $PUSH_EXIT -ne 0 ]; then
            echo "✗ thai-bible-ai push to origin/main failed (exit $PUSH_EXIT):" >&2
            echo "$PUSH_OUT" >&2
            exit 1
        fi
    fi
) || exit 1

# Pull the SHA back from the temp file (subshell var doesn't propagate)
if [ -f "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha" ]; then
    TBA_SOURCE_SHA=$(cat "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha")
    rm -f "/tmp/ship_${SLUG}_${CHAPTER_PADDED}_tba_sha"
fi

# Check if bundle changed
if git diff --quiet server/data/eremos_translation.json; then
    # Source-only ship (e.g., re-run after a bundle no-op); still verify the
    # thai-bible-ai source commit reached origin/main.
    assert_chapter_commits_on_origin_main
    echo
    echo "✓ Bundle has no changes — nothing to ship. Exiting."
    exit 0
fi

# --- 3. Branch, commit, push, PR, merge ---
echo "[3/7] Branch + commit + push..."
git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"
git add server/data/eremos_translation.json
git commit -q -m "feat: add ${BOOK_CODE} ${CHAPTER} to Eremos Translation bundle

Auto-shipped by ship_chapter.sh after translation + checks passed.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

# Save chapter-bundle SHA for the post-ship origin/main assertion
EREMOS_CHAPTER_SHA=$(git rev-parse HEAD)

PUSH_OUT=$(git push -u origin "$BRANCH" 2>&1)
PUSH_EXIT=$?
echo "$PUSH_OUT" | tail -1
if [ $PUSH_EXIT -ne 0 ]; then
    echo "✗ EremosVercel2 branch push failed (exit $PUSH_EXIT):"
    echo "$PUSH_OUT"
    exit 1
fi

PR_BODY="Adds ${BOOK_CODE} chapter ${CHAPTER} to the Eremos Translation bundle.

Translated and checked via the thai-bible-ai pipeline (RULES.md compliance: key-term consistency, TNBT structural, OT citations, synoptic parallels, back-translation — all green).

Auto-shipped via \`ship_chapter.sh\`."

PR_CREATE_OUT=$(gh pr create --title "$PR_TITLE" --body "$PR_BODY" --base main --head "$BRANCH" 2>&1)
PR_CREATE_EXIT=$?
PR_URL=$(echo "$PR_CREATE_OUT" | tail -1)
echo "    PR: $PR_URL"
if [ $PR_CREATE_EXIT -ne 0 ]; then
    echo "✗ gh pr create failed (exit $PR_CREATE_EXIT):"
    echo "$PR_CREATE_OUT"
    exit 1
fi

if [ $SKIP_MERGE -eq 1 ]; then
    # PR is open but not merged; chapter commit lives on $BRANCH only. Still
    # assert that the thai-bible-ai source push reached origin/main.
    EREMOS_CHAPTER_SHA=""  # unset — chapter commit is not on main yet
    assert_chapter_commits_on_origin_main
    echo "    --skip-merge set; PR open for manual review."
    echo
    echo "Stopped before TestFlight (--skip-merge implies --skip-testflight)."
    exit 0
fi

echo "[4/7] Auto-merge PR..."
sleep 3
PR_MERGE_OUT=$(gh pr merge "$BRANCH" --merge --delete-branch 2>&1)
PR_MERGE_EXIT=$?
echo "$PR_MERGE_OUT" | tail -2
if [ $PR_MERGE_EXIT -ne 0 ]; then
    echo "✗ gh pr merge failed (exit $PR_MERGE_EXIT) — PR remains open."
    echo "$PR_MERGE_OUT"
    echo "  Common causes: required-status-check pending, merge conflict,"
    echo "  branch protection blocking auto-merge."
    exit 1
fi

# Sync local main
git checkout main >/dev/null 2>&1
git pull origin main 2>&1 | tail -1

if [ $SKIP_TESTFLIGHT -eq 1 ]; then
    assert_chapter_commits_on_origin_main
    echo
    echo "✓ Vercel ship complete (${PR_URL}). --skip-testflight set; iOS build skipped."
    exit 0
fi

# --- 5. Bump iOS version ---
echo "[5/7] Bump iOS version..."
CURRENT_VERSION=$(grep -E "CURRENT_PROJECT_VERSION = [0-9]+;" ios/App/App.xcodeproj/project.pbxproj | head -1 | grep -oE "[0-9]+")
NEW_VERSION=$((CURRENT_VERSION + 1))
echo "    ${CURRENT_VERSION} → ${NEW_VERSION}"
sed -i '' "s/CURRENT_PROJECT_VERSION = ${CURRENT_VERSION};/CURRENT_PROJECT_VERSION = ${NEW_VERSION};/g" ios/App/App.xcodeproj/project.pbxproj

# --- 6. Build web + cap sync ---
echo "[6/7] Build web + cap sync iOS..."
npm run build 2>&1 | tail -3
npx cap sync ios 2>&1 | tail -2

# --- 7. Archive, export, upload TestFlight ---
echo "[7/7] Archive → export → upload TestFlight..."
echo "    (this takes 5-8 min total)"

xcodebuild archive -scheme Eremos -project ios/App/App.xcodeproj \
    -archivePath /tmp/Eremos.xcarchive \
    -allowProvisioningUpdates \
    CODE_SIGN_STYLE=Automatic DEVELOPMENT_TEAM="$APPLE_DEVELOPMENT_TEAM" 2>&1 | tail -3
echo "    ✓ archive built"

xcodebuild -exportArchive \
    -archivePath /tmp/Eremos.xcarchive \
    -exportOptionsPlist "$HOME/.appstoreconnect/ExportOptions.plist" \
    -exportPath /tmp/EremosExport \
    -allowProvisioningUpdates \
    -authenticationKeyPath "$APP_STORE_CONNECT_API_KEY_PATH" \
    -authenticationKeyID "$APP_STORE_CONNECT_KEY_ID" \
    -authenticationKeyIssuerID "$APP_STORE_CONNECT_ISSUER_ID" 2>&1 | tail -2
echo "    ✓ IPA exported"

xcrun altool --upload-app -f /tmp/EremosExport/Eremos.ipa -t ios \
    --apiKey "$APP_STORE_CONNECT_KEY_ID" \
    --apiIssuer "$APP_STORE_CONNECT_ISSUER_ID" 2>&1 | tail -3
echo "    ✓ uploaded to TestFlight as build ${NEW_VERSION}"

# Commit and push the version bump (precedent: direct to main for chore bumps)
git add ios/App/App.xcodeproj/project.pbxproj
git commit -q -m "chore: bump iOS build to ${NEW_VERSION}

Eremos Translation chapter ${BOOK_CODE} ${CHAPTER} added in PR ${PR_URL}.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
EREMOS_BUMP_SHA=$(git rev-parse HEAD)

PUSH_OUT=$(git push origin main 2>&1)
PUSH_EXIT=$?
echo "$PUSH_OUT" | tail -1
if [ $PUSH_EXIT -ne 0 ]; then
    echo "✗ EremosVercel2 iOS-bump push failed (exit $PUSH_EXIT):"
    echo "$PUSH_OUT"
    exit 1
fi

assert_chapter_commits_on_origin_main

echo
echo "=== Ship complete ==="
echo "  PR:        ${PR_URL} (merged)"
echo "  TestFlight: build ${NEW_VERSION} uploaded"
echo "  Vercel:     auto-deploys from main (~2 min)"
echo "  iOS:        TestFlight processing (~10-15 min)"

# --- 8. End-of-book detection ---
# If this chapter is the LAST in its book, halt with exit 1 so the /loop
# wrapper detects failure and stops before drafting the next chapter.
# Per docs/END_OF_BOOK_CHECKLIST.md, an editorial review must run before
# starting the next book — it produces translator_decisions docs that the
# next book's chapters will load at draft-time.
echo
echo "[end-of-book check] $BOOK_CODE $CHAPTER..."
set +e
python3 "$THAI_BIBLE_AI/scripts/detect_book_complete.py" "$BOOK_CODE" "$CHAPTER"
DETECT_EXIT=$?
set -e
if [ $DETECT_EXIT -eq 1 ]; then
    exit 1
fi
