# COPIES-AND-TWINS — the SARA family, receipted

*Assembled 2026-10-13; copy 1 re-cut 2026-10-29 with the two new ledger entries. Every copy verified byte-for-byte (sha256) against a fresh clone of its
source repository on the day it was placed. Re-verify any time with:*
`sha256sum <path>` — *no claim here is made from memory.*

## The six copies in this repository

| # | File here | Source path (repo) | Source rev | sha256 | Lines / words (`wc`) |
|---|---|---|---|---|---|
| 1 | `SARA.md` | `soul-land-universal-kit` → `SARA.md` (repo root) | `a7791db` → **re-cut 2026-10-29** | `d8b5c1f501e3680b209d12e60c2dec82e7ba8f23ec47043487319047527aebb2` | 688 / 14,293 |
| 2 | `editions/workspace-incarnation-2026-09-19.md` | `soul-land-universal-kit` → `SOUL_LAND_WORKSPACE/SARA.md` | `a7791db` | `5066f6cfbc330cdc9cbd5da76e38cf886cc52bdc257ddea664cfcada9ca7496a` | 799 / 13,180 |
| 3 | `editions/lan-shen-incarnation.md` | `soul-land-universal-kit` → `lan_shen/SARA.md` | `a7791db` | `171b23398f2a1e98ca178fe8864576862f6fc008e014f51f6e9d29c9cdc8bb18` | 323 / 3,369 |
| 4 | `editions/fire-phoenix/working-context.md` | `soul-land-universal-kit` → `soul_land_4_fire_phoenix/workshop/SARA_WORKING_CONTEXT.md` | `a7791db` | `38da926d93e0560c4732b7d584387ba743d9c998c91c4db799e5173347273697` | 29 / 473 |
| 5 | `editions/fire-phoenix/comprehension-ledger.md` | `soul-land-universal-kit` → `soul_land_4_fire_phoenix/workshop/SARA_COMPREHENSION_LEDGER.md` | `a7791db` | `0fc9fa57b458ed98c8bae1351b82a82009f53f6127a70c5cd684d4d8d5e5be2e` | 129 / 2,460 |
| 6 | `AGENT-OPERATING-PROFILE.md` | `soul-land-universal-kit` → `SOUL_LAND_WORKSPACE/AGENT_OPERATING_PROFILE.md` | `a7791db` | `eddfd2f04611244f0d415f9bf594d701b0695e43871003b74acea72bb688222b` | 151 / 2,302 |

Also carried (tooling, from the account's repositories): `tools/refresh-manifest.sh` (pattern from
`adaptation-talent`), `LICENSE` (`adaptation-talent` @ `389a824`, sha256
`c317d8d48606c85a9a1a244d20c72cfd57eefa3b2d57760f25e8efd2a1ee8102`). `tools/check.py` and
`tools/check_sara.py` were written for this repository.

## Twin analysis (hash-based, not name-based)

- **Within this repository:** the six copies are **6 distinct hashes — 0 byte-identical twins.**
  Each is a genuinely different document: the canonical self-file, the workspace edition, the
  serial edition, the workshop pair, and the profile.
- **Against the wider account:** the SARA family is distinct from the kit's other twin families
  (the master ×3, GENESIS ×2, blue_silver pairs the desk's item C tracks). No SARA file duplicates
  any of those.
- **Why hashes:** the account's rule, from the day a basename match produced ten "twins" of which
  zero were identical — *match by hash or do not claim a match.*

## The standing copies — nothing moved, nothing deleted

The six sources above **remain in their own repositories, unchanged.** This repository is the
reading home; the working copies stay where the work happens (the kit's `SARA.md` is what the
serials read and the session appends to; the workshop pair is what the Fire Phoenix room loads).
Consolidating such families is the author's call — the same call already standing for the
account's other family-files on [`the-authors-desk`](https://github.com/gm5206663-bit/the-authors-desk).
The SARA family is now listed there too; until a ruling, **copies stay recorded, not collected.**

## If a source changes

The self-file is a *living* document — it is appended to every session, by its own law. When a
source in the table above changes:

1. re-copy it here (keeping this repository the reading home),
2. update its sha256 and `wc` numbers in this table,
3. run `sh tools/refresh-manifest.sh`, then `python3 tools/check.py`,
4. commit the copy, this table, and the refreshed manifest **together**.

A divergent copy is a fork, and forks are how the account's register once drifted — the remedy is
always the same: re-copy, re-hash, re-verify, in the same turn.
