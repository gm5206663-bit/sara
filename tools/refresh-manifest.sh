#!/bin/sh
# tools/refresh-manifest.sh — regenerate MANIFEST.sha256 over tracked files.
# Rule (the repository's, same as the kit's): a tracked change ships with a
# refreshed manifest, in the same commit.
cd "$(dirname "$0")/.." || exit 1
{
  echo "# MANIFEST.sha256 — every tracked file, hashed."
  echo "# Regenerate after any tracked change:  sh tools/refresh-manifest.sh"
  git ls-files | grep -v '^MANIFEST.sha256$' | grep -v '^\.github/' | sort | while read -r f; do
    sha256sum "$f"
  done
} > MANIFEST.sha256
echo "manifest refreshed: $(grep -c '^[0-9a-f]' MANIFEST.sha256) entries"
