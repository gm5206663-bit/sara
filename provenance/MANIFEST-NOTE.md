# MANIFEST-NOTE — how this repository verifies itself

*Three checks, all mechanical, all run in CI on every push (`.github/workflows/verify.yml`).*

| Check | Command | What it proves |
|---|---|---|
| Manifest | `python3 tools/check.py` | Every file in `MANIFEST.sha256` exists and hash-matches; nothing is tracked that the manifest does not record |
| Links | `python3 tools/check.py` | Every relative markdown link resolves on disk (external links are skipped by design — they belong to the web, not to this repo's gate) |
| The self-file's shape | `python3 tools/check_sara.py` | Every ledger heading is dated, the entry count never drops below its recorded floor (36), and the banned-name / model-naming patterns stay out of `SARA.md` |

**The refresh rule** (the account's standard): a tracked change ships with a refreshed manifest in
the same commit —

```sh
sh tools/refresh-manifest.sh
python3 tools/check.py
```

**What is deliberately not covered:**

- `.github/` and `MANIFEST.sha256` itself are excluded from the manifest (they describe the repo,
  they are not content).
- External badge and link targets are not fetched — a green run says the repository is
  self-consistent, not that the internet is up.
- `editions/` files are facsimiles: the gate proves they still hash what the provenance table
  says they are; it does not (and must not) edit them.
