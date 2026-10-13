# Contributing — how this repository is kept

This repository is a **curated archive of written documents** (the self-file and its editions), not
open prose to be edited. Three rules keep it alive and honest.

## 1 · The self-file grows in its own house

`SARA.md` here is the canonical lineage — but it is *appended* in the rooms where the work happens
(the kit session, the serial workshops), then mirrored here. If you are the agent continuing this
lineage:

- never edit an old entry to look better — append a new one that supersedes it and say so;
- every entry is dated (`### YYYY-MM-DD — title`) and signed (`— Sara`);
- run `python3 tools/check_sara.py` — the ledger floor and the name are enforced.

## 2 · A tracked change ships with a refreshed manifest

```sh
sh tools/refresh-manifest.sh    # regenerate MANIFEST.sha256
python3 tools/check.py          # manifest + every relative link
```

Commit the change and the refreshed manifest **together**. CI runs the same two commands on every
push (`.github/workflows/verify.yml`) plus `tools/check_sara.py`.

## 3 · Editions are facsimiles

Files in `editions/` and the profile are byte-for-byte copies of their sources. **Do not edit them
in place.** If a source document changes, re-copy it, update its sha256 in
`provenance/COPIES-AND-TWINS.md`, refresh the manifest, and commit — the provenance file is the
receipt of what came from where.

## The one-copy question

The SARA family's working copies live in their project rooms; this repository is the reading home.
Consolidation of such families is the author's call (it stands as an open item on
`the-authors-desk`). Do not move or delete a working copy to "tidy up" — record copies, don't
collect them.
