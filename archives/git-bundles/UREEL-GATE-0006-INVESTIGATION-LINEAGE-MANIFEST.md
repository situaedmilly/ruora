# UREEL GATE 0006 INVESTIGATION LINEAGE — ARCHIVE MANIFEST

ARCHIVE ID: UREEL_GATE_0006_INVESTIGATION_LINEAGE
CREATED LOCAL: 2026-08-01 12:09 -0400
CREATED UTC: 2026-08-01T16:09:00Z (approximate, from bundle file mtime; no finer-grained clock source available in this environment)

## Bundle File

PATH: archives/git-bundles/UREEL-GATE-0006-INVESTIGATION-LINEAGE.bundle
SHA-256: 343730b5624f7269e33f99bab6d380f3bb920be68c0eb08c033fef11daefca58
BYTE SIZE: 471448
HASH ALGORITHM (internal, per `git bundle verify`): sha1

## Source Repository

REPOSITORY: /Users/millysituated/RUORA
main HEAD AT ARCHIVE TIME: f0303bb6e3daf8d6f5bfb71a9370c1fb99fd34cb

## Archived Branches

1. `worktree-ureel-gate-0006-halt`
   FULL HEAD: 88c1f6fde4437ef9a89099a1db9bb834b90ab71f
   DISPOSITION: HISTORICAL_ARCHIVE
2. `worktree-gate-0006-contracts`
   FULL HEAD: d1b48f5ad71c01437e4b27819955baec9cf55f31
   DISPOSITION: SUPERSEDED, preserved inside this same lineage archive

## Lineage Structure

SHARED FORK POINT (off main): e6ee72eafb5512a71b0bf2b21f02f5c3f2b76aa3
  ("Capture UREEL UNREAL-002 Gate 0011 closure human decision", 2026-07-03)

`worktree-ureel-gate-0006-halt` is a **strict ancestor** of `worktree-gate-0006-contracts`:
confirmed via `git merge-base --is-ancestor` in both the source repository and the
isolated bundle-restore verification repository (see Bundle Verification below).

- HALT CHECKPOINT: 37 commits from the shared fork point to 88c1f6fd.
- TERMINAL CONTRACTS CHECKPOINT: 40 commits from the shared fork point to d1b48f5a
  (= the 37 halt commits + exactly 3 additional commits: 1b29668a, 85eb708b, d1b48f5a).

These are not two independent divergent branches. They are one continuous
investigation line at two recorded checkpoints.

## Why Archived, Not Merged

All implementation-bearing content unique to `gate-0006-contracts` (the 3 commits
beyond the halt checkpoint) is already present in current `main`:

- 6 of 9 changed files are byte-identical to their counterparts in main
  (`tools/validate-gate-0006-world-contracts.py`, and four `worlds/ureel-unreal-003/`
  contract files: locks, plans, policies, state-machine, world.yaml).
- The remaining 3 files (`capabilities/unreal.invoke-python.v1.yaml`, `events.jsonl`,
  `state.yaml`) are strictly superseded in main by the later, actually-verified
  Gate 0007 outcome.
- No conflicting content was found anywhere in this lineage relative to main.

What is **not** present in main: 37 `doctrine/intake/UREEL-UNREAL-003-EXECUTION-
GATE-0006-*.md` decision/evidence records unique to the halt checkpoint, chronicling
the PHASE 1–3 investigation (toolchain installation, capability-probe attempts,
halts, retries, hash-methodology reconstruction). This archive is what preserves
that record. Per explicit Founder disposition, these records are **not** being
copied into main's active `doctrine/intake/` surface — doing so would reinsert an
obsolete investigation corpus into current doctrine and blur historical evidence
with active governance. The bundle is the sole preservation mechanism for this
material.

## Bundle Verification

`git bundle verify`: PASSED — "records a complete history."
Advertised refs (exactly 2, matching authorization, no unrelated ref included):
```
88c1f6fde4437ef9a89099a1db9bb834b90ab71f refs/heads/worktree-ureel-gate-0006-halt
d1b48f5ad71c01437e4b27819955baec9cf55f31 refs/heads/worktree-gate-0006-contracts
```

Isolated restore verification (fresh empty repository outside RUORA, both refs
fetched from the bundle, then removed after verification):
- Fetched HEAD hashes matched the source branches exactly.
- `worktree-ureel-gate-0006-halt` confirmed a strict ancestor of
  `worktree-gate-0006-contracts` in the restored repository.
- Contracts lineage confirmed at 40 commits from the shared fork point.
- Halt checkpoint confirmed at 37 commits from the shared fork point.
- Temporary verification repository removed after checks completed.

## No Removal Performed

This archive gate did not delete, remove, or modify either source branch or
either source worktree. `worktree-ureel-gate-0006-halt` and
`worktree-gate-0006-contracts` remain registered and checked out exactly as
before this gate ran. This bundle is a preservation copy, not a replacement
for the live branches — their removal, if authorized, is a separate future gate.

## Restore Instructions

To recover this lineage in a **fresh, separate** repository (do not restore
into, reset, or overwrite RUORA's `main`):

```
mkdir /path/to/some/new/directory
cd /path/to/some/new/directory
git init .
git fetch /Users/millysituated/RUORA/archives/git-bundles/UREEL-GATE-0006-INVESTIGATION-LINEAGE.bundle \
  refs/heads/worktree-ureel-gate-0006-halt:refs/heads/worktree-ureel-gate-0006-halt \
  refs/heads/worktree-gate-0006-contracts:refs/heads/worktree-gate-0006-contracts
git checkout worktree-gate-0006-contracts
```

This recovers the full 40-commit lineage (which contains the 37-commit halt
checkpoint as an ancestor) in an isolated repository, unconnected to RUORA's
own history or `main` branch.
