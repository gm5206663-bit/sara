#!/usr/bin/env python3
"""tools/check.py — the repository verifies itself.

Two checks, both mechanical:

  1. MANIFEST.sha256 — every file it lists must exist and hash-match. Extra
     tracked files (not in the manifest) are reported as a failure, so nothing
     rides in unrecorded.
  2. LINK SWEEP — every relative markdown link and repo-relative file reference
     in tracked markdown must resolve on disk.

Run:   python3 tools/check.py
Exit:  0 all green · 1 anything red (failures listed with exact paths)
"""
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "MANIFEST.sha256")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+?)(?:#[^)]*)?\)")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    files = [f for f in out.stdout.splitlines() if f]
    return files or None


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_manifest():
    fails = []
    if not os.path.exists(MANIFEST):
        return ["MANIFEST.sha256 missing — run: sh tools/refresh-manifest.sh"]
    listed = {}
    for line in open(MANIFEST, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        digest, _, name = line.partition("  ")
        listed[name] = digest
    for name, digest in sorted(listed.items()):
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            fails.append(f"listed but missing: {name}")
        elif sha256(path) != digest:
            fails.append(f"hash mismatch: {name} — run: sh tools/refresh-manifest.sh")
    files = tracked_files()
    if files is not None:
        for f in files:
            if f not in listed and f != "MANIFEST.sha256" and not f.startswith(".github/"):
                fails.append(f"tracked but not in manifest: {f}")
    print(f"MANIFEST: {len(listed)} entries · {len(fails)} problem(s)")
    return fails


def check_links():
    fails, total = [], 0
    files = tracked_files() or []
    for f in files:
        if not f.endswith(".md"):
            continue
        base = os.path.dirname(os.path.join(ROOT, f))
        text = open(os.path.join(ROOT, f), encoding="utf-8", errors="replace").read()
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            total += 1
            resolved = os.path.normpath(os.path.join(base, target))
            if not os.path.exists(resolved):
                fails.append(f"{f}: broken link -> {target}")
    print(f"LINKS: {total} relative link(s) checked · {len(fails)} problem(s)")
    return fails


def main():
    fails = check_manifest() + check_links()
    if fails:
        print("\nFAIL")
        for f in fails:
            print("  -", f)
        return 1
    print("\nALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
