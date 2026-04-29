"""Sync output/reader/*.md to a Google Drive folder as Google Docs.

Idempotent: re-running updates existing Docs in place rather than duplicating.
Mirrors the local folder structure under the configured root Drive folder.

Auth:
- GitHub Actions: reads OAUTH_TOKEN_JSON env var (the contents of oauth_token.json).
- Local dev: reads ~/.eremos-translation/oauth_token.json directly.

Config (env vars or defaults):
- DRIVE_FOLDER_ID: the parent folder in Drive (required)
- SOURCE_ROOTS: comma-separated repo-relative dirs to sync (default: output/reader)

Run from repo root:
    python3 scripts/sync_to_gdocs.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

GDOC_MIME = "application/vnd.google-apps.document"
FOLDER_MIME = "application/vnd.google-apps.folder"
MD_MIME = "text/markdown"


def load_credentials() -> Credentials:
    raw = os.environ.get("OAUTH_TOKEN_JSON")
    if raw:
        t = json.loads(raw)
    else:
        local = Path.home() / ".eremos-translation" / "oauth_token.json"
        if not local.exists():
            sys.exit(f"No OAUTH_TOKEN_JSON env var and no token at {local}")
        t = json.loads(local.read_text())
    return Credentials(
        token=None,
        refresh_token=t["refresh_token"],
        client_id=t["client_id"],
        client_secret=t["client_secret"],
        token_uri=t["token_uri"],
        scopes=t["scopes"],
    )


def find_child(drive, parent_id: str, name: str, mime: str | None = None) -> dict | None:
    """Return the first non-trashed child with the given name (and optional mime), or None."""
    safe_name = name.replace("'", "\\'")
    q = f"'{parent_id}' in parents and name = '{safe_name}' and trashed = false"
    if mime:
        q += f" and mimeType = '{mime}'"
    result = drive.files().list(q=q, fields="files(id,name,mimeType)", pageSize=2).execute()
    files = result.get("files", [])
    return files[0] if files else None


def get_or_create_folder(drive, parent_id: str, name: str) -> str:
    existing = find_child(drive, parent_id, name, FOLDER_MIME)
    if existing:
        return existing["id"]
    created = drive.files().create(
        body={"name": name, "parents": [parent_id], "mimeType": FOLDER_MIME},
        fields="id",
    ).execute()
    return created["id"]


def upsert_doc(drive, parent_id: str, doc_name: str, source_path: Path) -> tuple[str, str]:
    """Create or update a Google Doc from a markdown source. Returns (file_id, action)."""
    media = MediaFileUpload(str(source_path), mimetype=MD_MIME, resumable=False)
    existing = find_child(drive, parent_id, doc_name, GDOC_MIME)
    if existing:
        drive.files().update(fileId=existing["id"], media_body=media).execute()
        return existing["id"], "updated"
    created = drive.files().create(
        body={"name": doc_name, "parents": [parent_id], "mimeType": GDOC_MIME},
        media_body=media,
        fields="id",
    ).execute()
    return created["id"], "created"


def sync_directory(drive, repo_root: Path, source_rel: Path, drive_root_id: str, skip_files: set[str]) -> list[str]:
    """Walk repo_root/source_rel, mirror folder structure under drive_root_id, upsert .md files."""
    log: list[str] = []
    src = repo_root / source_rel

    if not src.exists():
        log.append(f"skip: {source_rel} does not exist")
        return log

    # Mirror each path segment of source_rel as a Drive folder under drive_root_id
    parent_id = drive_root_id
    for part in source_rel.parts:
        parent_id = get_or_create_folder(drive, parent_id, part)

    # For each .md file in source_rel (recursive), mirror its directory and upsert the doc
    for md in sorted(src.rglob("*.md")):
        rel_to_repo = md.relative_to(repo_root).as_posix()
        if rel_to_repo in skip_files:
            log.append(f"  skipped (in SKIP_FILES): {rel_to_repo}")
            continue
        rel_to_src = md.relative_to(src)
        # Walk subdirectories within source_rel
        sub_parent = parent_id
        for sub_part in rel_to_src.parent.parts:
            sub_parent = get_or_create_folder(drive, sub_parent, sub_part)
        doc_name = md.stem  # strip .md, becomes Doc title
        try:
            file_id, action = upsert_doc(drive, sub_parent, doc_name, md)
            log.append(f"  {action}: {source_rel}/{rel_to_src} -> {file_id}")
        except Exception as e:
            log.append(f"  ERROR: {source_rel}/{rel_to_src}: {e}")
    return log


def main() -> int:
    folder_id = os.environ.get("DRIVE_FOLDER_ID")
    if not folder_id:
        sys.exit("DRIVE_FOLDER_ID env var is required")

    source_roots = os.environ.get("SOURCE_ROOTS", "output/reader").split(",")
    source_roots = [s.strip() for s in source_roots if s.strip()]

    skip_files = {s.strip() for s in os.environ.get("SKIP_FILES", "").split(",") if s.strip()}

    repo_root = Path(__file__).resolve().parent.parent
    creds = load_credentials()
    drive = build("drive", "v3", credentials=creds)

    # Sanity-check the root folder is reachable
    folder = drive.files().get(fileId=folder_id, fields="id,name").execute()
    print(f"Syncing into Drive folder: {folder['name']} ({folder['id']})")
    if skip_files:
        print(f"Skipping: {sorted(skip_files)}")

    all_log: list[str] = []
    for sr in source_roots:
        print(f"\nSource: {sr}")
        log = sync_directory(drive, repo_root, Path(sr), folder_id, skip_files)
        for line in log:
            print(line)
        all_log.extend(log)

    print(f"\nDone. {len(all_log)} files processed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
