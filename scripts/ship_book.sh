#!/bin/zsh
# ship_book.sh — book-boundary deferred ship.
#
# Companion to ship_chapter.sh (which is now source-only as of 2026-05-02).
# Run once per book after:
#   1. All chapters of the book have shipped to thai-bible-ai/main via
#      ship_chapter.sh
#   2. End-of-book audit has run (auto-launched at last chapter ship) and
#      its PR has merged
#   3. Any AI-review revisions have been implemented and merged
#
# What this script does, in order:
#   1. Pull latest main in EremosVercel2
#   2. Rebuild eremos_translation.json bundle (book-agnostic; picks up every
#      translated chapter, not just BOOK_CODE)
#   3. If bundle changed:
#        - Branch: feat/book-ship-<slug>
#        - Commit + push + PR + auto-merge to EremosVercel2/main
#        - Vercel auto-deploys from main
#   4. Bump iOS CURRENT_PROJECT_VERSION (auto-detects next available number)
#   5. npm run build && npx cap sync ios
#   6. xcodebuild archive → exportArchive → xcrun altool --upload-app
#   7. Commit version bump to EremosVercel2/main
#   8. Tag book-<slug>-v1 in thai-bible-ai + push tag
#
# Android (Play Console) is a separate manual step; see
# reference_eremos_ship_recipe.md for the gradle bundleRelease + play_upload.py
# command sequence. Plumbing it here as --android is tracked but not
# implemented in this iteration (the Android script lives in ~/.appstoreconnect/,
# not in this repo).
#
# Usage:
#   ship_book.sh <BOOK_CODE>
#   ship_book.sh PHM
#   ship_book.sh ROM --skip-tag    # ship bundle/iOS but defer the v1 tag
#
# Optional flags:
#   --skip-testflight   ship to Vercel only; skip iOS build/upload
#   --skip-tag          ship bundle + iOS but don't tag book-<slug>-v1
#   --skip-merge        open PR but don't auto-merge (manual review)
#
# Exit codes:
#   0 = success (or "nothing to ship" if bundle unchanged)
#   1 = error (any step failed)

set -e

# --- Apple credentials (env-driven) ---
: "${APP_STORE_CONNECT_KEY_ID:?APP_STORE_CONNECT_KEY_ID not set — see settings.json or shell env}"
: "${APP_STORE_CONNECT_ISSUER_ID:?APP_STORE_CONNECT_ISSUER_ID not set}"
: "${APP_STORE_CONNECT_API_KEY_PATH:?APP_STORE_CONNECT_API_KEY_PATH not set}"
: "${APPLE_DEVELOPMENT_TEAM:?APPLE_DEVELOPMENT_TEAM not set}"

# --- args ---
SKIP_TESTFLIGHT=0
SKIP_TAG=0
SKIP_MERGE=0
POSITIONAL=()
while [ $# -gt 0 ]; do
    case "$1" in
        --skip-testflight) SKIP_TESTFLIGHT=1; shift ;;
        --skip-tag) SKIP_TAG=1; shift ;;
        --skip-merge) SKIP_MERGE=1; shift ;;
        *) POSITIONAL+=("$1"); shift ;;
    esac
done
set -- "${POSITIONAL[@]}"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <BOOK_CODE> [--skip-testflight] [--skip-tag] [--skip-merge]"
    echo "  e.g. $0 PHM"
    exit 1
fi

BOOK_CODE="$1"
THAI_BIBLE_AI="$HOME/thai-bible-ai"
EREMOS_REPO="$HOME/EremosVercel2"

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

BRANCH="feat/book-ship-${SLUG}"
PR_TITLE="feat: ship Eremos Translation book — ${BOOK_CODE}"
TAG="book-${SLUG}-v1"

EREMOS_BUNDLE_SHA=""
EREMOS_BUMP_SHA=""

assert_book_commits_on_origin_main() {
    local failed=0
    echo
    echo "[assert] Book-ship commits on origin/main..."
    git -C "$EREMOS_REPO" fetch origin main --quiet 2>/dev/null || true
    if [ -n "$EREMOS_BUNDLE_SHA" ]; then
        if git -C "$EREMOS_REPO" merge-base --is-ancestor "$EREMOS_BUNDLE_SHA" origin/main 2>/dev/null; then
            echo "    ✓ EremosVercel2 bundle ${EREMOS_BUNDLE_SHA:0:7} reachable from origin/main"
        else
            echo "    ✗ EremosVercel2 bundle ${EREMOS_BUNDLE_SHA:0:7} NOT reachable from origin/main"
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
        echo "✗✗✗ Book-ship commits not on origin/main — investigate."
        exit 1
    fi
}

echo "=== Book ship: ${BOOK_CODE} (slug=${SLUG}) ==="
echo

# --- Pre-flight: verify book is actually ready for ship ---
# All chapters of BOOK_CODE must be in output/translations/.
echo "[gate] Verifying all chapters of ${BOOK_CODE} are translated..."
python3 - <<PY || exit 1
import json, sys
from pathlib import Path
ROOT = Path("$THAI_BIBLE_AI")
order = json.loads((ROOT / "data" / "production_order.json").read_text())
chapters = sorted(e["chapter"] for e in order["order"] if e["book"] == "$BOOK_CODE".upper())
if not chapters:
    print("    ✗ $BOOK_CODE not in production_order.json", file=sys.stderr); sys.exit(1)
slug = "$SLUG"
missing = [n for n in chapters if not (ROOT / "output" / "translations" / f"{slug}_{n:02d}.json").exists()]
if missing:
    print(f"    ✗ $BOOK_CODE missing chapters: {missing}", file=sys.stderr); sys.exit(1)
print(f"    ✓ All {len(chapters)} chapters of $BOOK_CODE translated.")
PY

# Inclusion-variant strict gate — same gate that run_end_of_book_audit enforces.
# Catches SBLGNT-omits-mainstream-includes candidates lacking disposition.
echo "[gate] Inclusion-variant strict gate..."
if ! python3 "$THAI_BIBLE_AI/scripts/audit_inclusion_variants.py" --book "$SLUG" --strict >/dev/null 2>&1; then
    echo "    ✗ Inclusion-variant gate FAILED for ${BOOK_CODE}."
    echo "    Run: python3 scripts/audit_inclusion_variants.py --book ${SLUG} --strict"
    echo "    See docs/end_of_book/inclusion_variant_gap_2026-05-02.md."
    exit 1
fi
echo "    ✓ Inclusion-variant gate clean."

# Verify thai-bible-ai is on main (so any in-flight branch work is intentional)
echo "[gate] Verifying thai-bible-ai is on main..."
TBA_BRANCH=$(git -C "$THAI_BIBLE_AI" branch --show-current 2>/dev/null || echo "")
if [ "$TBA_BRANCH" != "main" ]; then
    echo "✗ thai-bible-ai is on '$TBA_BRANCH', not main."
    echo "  cd $THAI_BIBLE_AI && git checkout main && git pull"
    exit 1
fi
git -C "$THAI_BIBLE_AI" pull origin main 2>&1 | tail -1
echo "    ✓ thai-bible-ai on main, synced."
echo

# --- 1. Pull latest main in EremosVercel2 ---
echo "[1/8] Pull latest main in EremosVercel2..."
cd "$EREMOS_REPO"
git checkout main >/dev/null 2>&1
git pull origin main 2>&1 | tail -1

# --- 2. Rebuild bundle ---
echo "[2/8] Rebuild bundle (book-agnostic; all translated chapters)..."
python3 "$THAI_BIBLE_AI/scripts/build_eremos_bundle.py" 2>&1 | tail -3

# --- 3. Branch + commit + push + PR + auto-merge ---
if git diff --quiet server/data/eremos_translation.json; then
    echo
    echo "✓ Bundle has no changes — bundle is already in sync."
    BUNDLE_NOOP=1
else
    BUNDLE_NOOP=0
fi

if [ $BUNDLE_NOOP -eq 0 ]; then
    echo "[3/8] Branch + commit + push + PR..."
    git checkout -b "$BRANCH" 2>/dev/null || git checkout "$BRANCH"
    git add server/data/eremos_translation.json
    git commit -q -m "feat: ship Eremos Translation book — ${BOOK_CODE}

Lock-the-book deferred ship after end-of-book audit + revisions merged.
Bundle picks up all currently-translated chapters in the corpus.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

    EREMOS_BUNDLE_SHA=$(git rev-parse HEAD)

    PUSH_OUT=$(git push -u origin "$BRANCH" 2>&1)
    PUSH_EXIT=$?
    echo "$PUSH_OUT" | tail -1
    if [ $PUSH_EXIT -ne 0 ]; then
        echo "✗ EremosVercel2 branch push failed (exit $PUSH_EXIT):"
        echo "$PUSH_OUT"
        exit 1
    fi

    PR_BODY="Locks ${BOOK_CODE} for production after end-of-book audit + revisions merged.

This bundle includes every currently-translated chapter in the corpus (book-agnostic walker). Triggers Vercel deploy.

Auto-shipped via \`scripts/ship_book.sh\`."

    PR_CREATE_OUT=$(gh pr create --title "$PR_TITLE" --body "$PR_BODY" --base main --head "$BRANCH" 2>&1)
    PR_CREATE_EXIT=$?
    PR_URL=$(echo "$PR_CREATE_OUT" | tail -1)
    echo "    PR: $PR_URL"
    if [ $PR_CREATE_EXIT -ne 0 ]; then
        echo "✗ gh pr create failed (exit $PR_CREATE_EXIT)"
        echo "$PR_CREATE_OUT"
        exit 1
    fi

    if [ $SKIP_MERGE -eq 1 ]; then
        echo "    --skip-merge set; PR open for manual review."
        echo
        echo "Stopped before iOS bump (--skip-merge implies --skip-testflight)."
        exit 0
    fi

    echo "[4/8] Auto-merge PR..."
    sleep 3
    PR_MERGE_OUT=$(gh pr merge "$BRANCH" --merge --delete-branch 2>&1)
    PR_MERGE_EXIT=$?
    echo "$PR_MERGE_OUT" | tail -2
    if [ $PR_MERGE_EXIT -ne 0 ]; then
        echo "✗ gh pr merge failed (exit $PR_MERGE_EXIT)"
        echo "$PR_MERGE_OUT"
        exit 1
    fi

    git checkout main >/dev/null 2>&1
    git pull origin main 2>&1 | tail -1
fi

if [ $SKIP_TESTFLIGHT -eq 1 ]; then
    if [ $BUNDLE_NOOP -eq 0 ]; then
        assert_book_commits_on_origin_main
    fi
    echo
    echo "✓ Bundle ship complete${BUNDLE_NOOP:+ (no-op)}. --skip-testflight set; iOS build skipped."
    if [ $SKIP_TAG -eq 0 ]; then
        echo "  Tagging book-${SLUG}-v1..."
        cd "$THAI_BIBLE_AI"
        git tag -a "$TAG" -m "${BOOK_CODE} v1 — book-boundary ship complete (Vercel only)"
        git push origin "$TAG" 2>&1 | tail -1
        echo "    ✓ Tagged $TAG"
    fi
    exit 0
fi

# --- 5. Bump iOS version ---
cd "$EREMOS_REPO"
echo "[5/8] Bump iOS version..."
CURRENT_VERSION=$(grep -E "CURRENT_PROJECT_VERSION = [0-9]+;" ios/App/App.xcodeproj/project.pbxproj | head -1 | grep -oE "[0-9]+")
NEW_VERSION=$((CURRENT_VERSION + 1))
echo "    ${CURRENT_VERSION} → ${NEW_VERSION}"
sed -i '' "s/CURRENT_PROJECT_VERSION = ${CURRENT_VERSION};/CURRENT_PROJECT_VERSION = ${NEW_VERSION};/g" ios/App/App.xcodeproj/project.pbxproj

# --- 6. Build web + cap sync ---
echo "[6/8] Build web + cap sync iOS..."
npm run build 2>&1 | tail -3
npx cap sync ios 2>&1 | tail -2

# --- 7. Archive, export, upload TestFlight ---
echo "[7/8] Archive → export → upload TestFlight..."
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

git add ios/App/App.xcodeproj/project.pbxproj
git commit -q -m "chore: bump iOS build to ${NEW_VERSION} for ${BOOK_CODE} v1

Lock-the-book ship for ${BOOK_CODE} via scripts/ship_book.sh.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
EREMOS_BUMP_SHA=$(git rev-parse HEAD)

PUSH_OUT=$(git push origin main 2>&1)
PUSH_EXIT=$?
echo "$PUSH_OUT" | tail -1
if [ $PUSH_EXIT -ne 0 ]; then
    echo "✗ iOS-bump push failed (exit $PUSH_EXIT)"
    echo "$PUSH_OUT"
    exit 1
fi

assert_book_commits_on_origin_main

# --- 8. Tag book-<slug>-v1 ---
if [ $SKIP_TAG -eq 0 ]; then
    echo
    echo "[8/8] Tag book-${SLUG}-v1..."
    cd "$THAI_BIBLE_AI"
    git tag -a "$TAG" -m "${BOOK_CODE} v1 — end-of-book ship complete

Bundle: PR ${PR_URL} merged
TestFlight build: ${NEW_VERSION}
"
    git push origin "$TAG" 2>&1 | tail -1
    echo "    ✓ Tagged $TAG"
fi

echo
echo "=== Book ship complete ==="
echo "  Bundle PR:  ${PR_URL} (merged)"
echo "  TestFlight: build ${NEW_VERSION} uploaded"
echo "  Vercel:     auto-deploys from main (~2 min)"
echo "  iOS:        TestFlight processing (~10-15 min)"
if [ $SKIP_TAG -eq 0 ]; then
    echo "  Tag:        $TAG pushed"
fi
echo
echo "Android (Play Console) is a separate manual step:"
echo "  See: ~/EremosVercel2/android/ + ~/.appstoreconnect/play_upload.py"
echo "  Per: reference_eremos_ship_recipe.md (auto-memory)"
