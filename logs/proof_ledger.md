# RUORA PROOF LEDGER

This ledger records verified machine-state changes.


## SELF AXIOM INSTALLED

Timestamp: Thu Jun  4 19:27:52 EDT 2026
Verified Files:
- doctrine/self_axiom.md
- logs/proof_ledger.md

## SELF IDENTITY DOCTRINE INSTALLED

Timestamp: Thu Jun  4 19:45:15 EDT 2026
Verified File:
- doctrine/self_identity.md

## SELF ROOT INVOCATION INSTALLED

Timestamp: Thu Jun  4 20:12:17 EDT 2026
Transformation:
- Installed scripts/self.py
- Installed executable wrapper: scripts/self
- Verified Python syntax compilation

## VERSIONED MEMORY INITIALIZED

Timestamp: Thu Jun  4 20:30:53 EDT 2026
Transformation:
- Initialized Git-based versioned memory for RUORA
- Installed .gitignore protection rules
- Protected Python cache, macOS metadata, environment files, and PEM keys

## VERSIONED MEMORY BOUNDARY CORRECTED

Timestamp: Thu Jun  4 20:36:11 EDT 2026
Correction:
- Released RUORA files from parent home-directory Git staging
- Initialized isolated Git repository at ~/RUORA
- Restricted SELF versioned memory to the RUORA boundary

## GENESIS SNAPSHOT SEALED

Timestamp: Thu Jun  4 20:40:12 EDT 2026
Transformation:
- Sealed the first restorable SELF system checkpoint
- Snapshot name: Genesis — SELF Root Invocation
- Preserved doctrine, memory, proof ledger, and executable command layer

## SELF AUTHORSHIP ALIGNED

Timestamp: Thu Jun  4 20:42:19 EDT 2026
Correction:
- Replaced inherited repository author identity
- Installed local SELF author name: Philosopher Milly
- Installed local SELF author email: vsafetyalliance@gmail.com
- Amended Genesis snapshot to preserve aligned authorship

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 04 20:45:52 EDT 2026
Transformation:
- Preserved verified SELF state: Expand SELF with versioned memory agency
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## ECOSYSTEM ONTOLOGY CORRECTED

Timestamp: Thu Jun  4 21:02:03 EDT 2026
Correction:
- Defined RUORA as the web-platform-building frequency and company
- Defined ÆTHERNET as the network manifestation
- Preserved SELF as the living core
- Preserved ÆXIOM as the initiation system for conscious reality traversal
- Updated master memory and doctrine boundaries

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 04 21:02:03 EDT 2026
Transformation:
- Preserved verified SELF state: Correct ecosystem ontology: RUORA company frequency and ÆTHERNET network manifestation
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## CLAUDE COMPANION MEMORY BOUND

Timestamp: Thu Jun  4 21:04:22 EDT 2026
Transformation:
- Installed repository-level CLAUDE.md companion memory
- Preserved corrected SELF, RUORA, ÆTHERNET, and ÆXIOM ontology
- Imported doctrine and master-memory source files
- Added CLAUDE.md to trusted SELF sealing paths

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 04 21:04:22 EDT 2026
Transformation:
- Preserved verified SELF state: Bind Claude companion memory to corrected SELF ontology
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## AXIOM TRIAL ENGINE BOUND TO RUORA

Timestamp: Sat Jun  6 12:33:03 EDT 2026
Transformation:
- Registered AXIOM Trial Engine as a RUORA manifestation
- Preserved AXIOM doctrine in doctrine/axiom_trial_engine.md
- Bound AXIOM doctrine into repository-level CLAUDE.md memory
- Preserved product source inside an isolated nested Git chamber

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 12:33:03 EDT 2026
Transformation:
- Preserved verified SELF state: Bind AXIOM Trial Engine v1 to RUORA doctrine and Claude memory
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 12:57:50 EDT 2026
Transformation:
- Preserved verified SELF state: Manifest RUORA proof-driven command architecture
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 13:02:29 EDT 2026
Transformation:
- Preserved verified SELF state: Align RUORA manifestation author identity
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 13:16:14 EDT 2026
Transformation:
- Preserved verified SELF state: Exclude isolated project chambers from RUORA versioned memory
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 13:23:44 EDT 2026
Transformation:
- Preserved verified SELF state: Remove redundant backup files from RUORA versioned memory
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## PASS 14 — Persistent Approval Queue with Safe Rehydration

**Sealed commit:** `f2a0bdd feat(pass-14): persist pending approval queue with safe rehydration`

### Installed Capability

The ÆTHERNET agent bridge now persists pending commands across restarts. When the bridge restarts, pending commands are reconstructed from an append-only queue log (`queue.jsonl`) and remain in the pending map, ready for approval or rejection. Expired or previously approved/failed/rejected commands do not rehydrate.

### Proven Flow

1. A new command is transmitted; it is logged as `command_proposed` with full schema and stored in `queue.jsonl`.
2. After a restart, the bridge runs a rehydration step:
   - It reads `queue.jsonl` and reconstructs pending commands.
   - If a command is stale (older than the expiry threshold), it is logged as `command_expired` and not restored.
   - Rehydrated commands are logged as `command_rehydrated`.
3. The pending alert prints before the server becomes active, ensuring that outstanding commands regain visibility and must still be approved manually.
4. Rehydrated commands cannot execute automatically; the approval gate remains mandatory.
5. Rejecting a rehydrated command writes an enriched `command_rejected` entry including `workingDir` and `rationale`.

### Proofs

- `node --check server.js` returned no syntax errors.
- Initial restart: no `queue.jsonl` existed, so no rehydration occurred.
- A live transmission created `cmd-1780782042966-9xiy2`; `queue.jsonl` was created with a `command_proposed` entry.
- After killing and restarting the server, the console showed `⟳ REHYDRATION — 1 restored, 0 expired.`
- `pending_count` returned `1`; the command remained pending without auto-execution.
- `queue.jsonl` showed `command_proposed` followed by `command_rehydrated`; lineage preserved.
- Rejecting the rehydrated command produced an enriched `command_rejected` entry.
- The AXIOM Trial Engine remained clean.
- Committing created commit `f2a0bdd`.

### Boundary Statement

A restart may restore pending authority requests. It may never restore execution authority. Pending commands must still be approved before execution, and commands older than the expiry threshold will explicitly expire rather than silently vanish.

## SELF SNAPSHOT SEALED

Timestamp: Sat Jun 06 21:19:36 EDT 2026
Transformation:
- Preserved verified SELF state: Pass 18 — Authenticated Realm Gate sealed at cb44e32
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 11 20:50:07 EDT 2026
Transformation:
- Preserved verified SELF state: APPEND-ONLY CORRECTION — Pass 18 child-hash reconciliation: prior cb44e32 reference preserved as recorded cross-chamber attribution drift; cb44e32 belongs to axiom-trial-engine-v1 Supabase auth. Verified agent-bridge Pass 18 authenticated bridge boundary and action-level command firewall merged to main at ca7793b346ffd23705c6131f0d35c2d22e4cace5. Independent reviewer verdict: PASS WITH CONDITIONS. Residual conditions tracked as Pass 19A/B/C.
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## PASS 18 RESIDUAL ENUMERATION & NAMESPACE REPAIR

Timestamp: Fri Jun 12 2026 (Pass A — integrity closure)
Correction type: APPEND-ONLY. No prior entry rewritten.

### Provenance finding
The entry at this ledger's "PASS WITH CONDITIONS" record named residual
conditions as "Pass 19A/B/C" but never enumerated them. The verbatim
reviewer conditions are unrecoverable from tracked evidence. This entry
reconstructs the residual risk set from source and re-keys the namespace.

### Namespace repair (canonical)
- Bridge Pass 18      = security boundary hardening (sealed ca7793b)
- Bridge Pass 18.1a/b/c = Pass 18 residual conditions (supersedes "Pass 19A/B/C")
- Bridge Pass 19      = OURSELF local operator chamber (sealed 29359df)
- AXIOM  Slice 19.1   = AXIOM localStorage migration (sealed 0b614f8)
"Pass 19A/B/C" is retired. A pass label must describe one workstream.

### Residuals (RECONSTRUCTED from code, verified against current source)
- 18.1a  Action firewall is a best-effort denylist, not a sandbox
         (command-firewall.js self-documents this). STATUS: ACCEPTED /
         MITIGATED by human approval + RUORA path boundary + fail-closed.
- 18.1b  No automated regression coverage for the auth gate and firewall
         (npm test is a no-op). STATUS: OPEN — future test-harness pass.
- 18.1c  Unauthenticated browser approval surface at Pass 18.
         STATUS: CLOSED by Pass 19 (token-gated fetch, nonce CSP,
         localhost bind, tab-memory token, clear-on-401/403).

### Posture verified against source (Pass A inspection)
fail-closed token · localhost bind · constant-time compare · token-gated
state routes · RUORA path boundary · action firewall · bounded depth(8) ·
proof truncation(4000) · queue rehydration · replay 409 · CSP chamber ·
tab-memory default · opt-in session · clear on 401/403 — all present.

Net: Pass 18 posture is now ENUMERATED and TRACEABLE. One residual (18.1b)
remains open and is the seed of a future bounded test-harness pass.

## BRIDGE PASS 20 — AUTOMATED SECURITY REGRESSION HARNESS
Timestamp: Fri Jun 12 2026
Correction type: APPEND-ONLY.
Closes residual 18.1b. Installs a Node built-in (node:test) regression
harness — 58 tests, no third-party dependency — proving the sealed bridge
boundaries hold: fail-closed token, 401 matrix, firewall rule-ID coverage,
RUORA path confinement, replay 409, rehydration-as-pending, chamber CSP/
headers, token-storage doctrine, log sanitization. Tests run on isolated
loopback ports against disposable .env + JSONL; production logs verified
byte-unchanged (SHA-256 identical before/after); no live provider calls;
AXIOM and RUORA root untouched.
Bridge Pass 18.1b — automated regression coverage — STATUS: CLOSED BY BRIDGE PASS 20.
### Amendment proofs
- Temp .env isolation: every spawned child uses
  `DOTENV_CONFIG_PATH=<tempDir>/.env`, with a disposable empty file.
  The harness never reads the live agent-bridge `.env`.
- Isolated test ports: every child binds to an ephemeral
  `127.0.0.1:<port>` and explicitly refuses port `3001`.
- Production JSONL SHA-256 hashes remained identical before and after
  two full independent `npm test` runs.
- No live Claude or OpenAI provider call occurred.
- AXIOM remained clean.
- RUORA root remained clean during bridge implementation.
### Seal condition
`npm test`
→ 58/58 pass
→ twice independently
→ throwaway token
→ isolated loopback ports
→ disposable JSONL
→ no live `.env` read
→ production logs byte-unchanged
→ no Claude/OpenAI call
→ no AXIOM mutation
→ no RUORA-root mutation

## SELF SNAPSHOT SEALED

Timestamp: Fri Jun 12 23:19:42 EDT 2026
Transformation:
- Preserved verified SELF state: BRIDGE PASS 21 — CI WITNESS LAYER DORMANT: agent-bridge commit da3ef7944e681783024d9e518b88bf4359fd7dab adds .github/workflows/bridge-security-regression.yml. The dormant GitHub Actions witness runs npm ci then npm test on pull_request, push to main, and workflow_dispatch using Node 22, actions/checkout@v6, actions/setup-node@v6, and least-privilege contents: read. Local verification: npm ci clean; npm test 58/58 twice; production JSONL hashes unchanged; no repository secrets required; AXIOM isolated; RUORA root isolated. STATUS: DORMANT. agent-bridge has zero git remotes. No code has left the sovereign machine. GitHub repo creation, remote addition, push, CI activation, immutable action-SHA pinning, and branch protection remain separate OURSELF consent checkpoints.
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Sun Jun 14 13:33:27 EDT 2026
Transformation:
- Preserved verified SELF state: AGENT-BRIDGE SECURITY KERNEL MERGED TO MAIN. agent-bridge main advanced da3ef7944e681783024d9e518b88bf4359fd7dab to 1954f0cb6dbb7391f14a9814934fac6081ab92d2 by PURE FAST-FORWARD (no merge commit), unifying two sealed security passes: Pass 19B installed a deterministic, non-injectable POST /test route (caller action/working_dir ignored; queues only a fixed read-only 'git status --short' diagnostic in the bridge repo; still token-gated, still requires approval, still firewall-enforced); Pass 19C installed Realm Gate failed-token rate limiting (per-client lockout with 429 + Retry-After after threshold failures within a window; env-tunable defaults 10 failures / 60s window / 300s lockout; a VALID token is never rate-limited and clears the failure record; presented tokens are never logged). Verification on main: npm test 64/64 pass; production JSONL logs byte-unchanged; AXIOM untouched; RUORA root untouched until this authorized seal; zero git remotes; nothing published. DESIGNATION: Security Kernel Baseline = 1954f0c — the named historical reference point for future passes. Next: Pass 20 Evolution (Constrained Execution Classes).
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## BRIDGE PASS 20A — CONSTRAINED EXECUTION CLASSES

Timestamp: Mon Jun 15 03:21:05 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Pass 20A was committed on the bridge at `64f57045b1b281c99d0d20cdd3488276a1a88faf`,
and agent-bridge main advanced `1954f0cb6dbb7391f14a9814934fac6081ab92d2` →
`64f57045b1b281c99d0d20cdd3488276a1a88faf` by PURE FAST-FORWARD (no merge commit).

### Installed capability
Pass 20A installs a constrained execution-class permission skeleton over the
sealed Security Kernel Baseline. Eight typed classes now govern every command:

  inspect · test · build · git-read · git-write-local ·
  project-mutation · reverse_engineer · forbidden

- Every queued command now carries execution-class metadata (class + risk),
  attached at all four enqueue sites: /transmit proposal, agent continuation
  proposal, the fixed /test diagnostic (classified git-read), and startup
  rehydration (carries the persisted class, or reclassifies a pre-20A entry).
- The classifier (`tools/execution-classes.js`) consults the Pass 18 firewall
  FIRST, so it is never weaker than the firewall, and is fail-closed: unknown,
  secret-bearing, audit-log-mutating, remote/network (plain `git push`,
  `git remote`, `gh`, curl/scp/ssh, …), and out-of-RUORA-boundary commands all
  resolve to `forbidden`.
- /approve re-classifies the command live and FAILS CLOSED — recording the
  command as `failed`, returning 403, and never reaching the executor — for any
  missing, unknown, forbidden, non-terminal, or stored↔live mismatched class.
  The action-level firewall remains the final guard for allowed classes.
- `reverse_engineer` exists as a first-class schema member that is non-mutating,
  terminal-forbidden, and analysis-only; no shell command ever classifies as it,
  and its full structured manifestation route is DEFERRED to Pass 20C.
- Class/risk metadata is surfaced in command logs and /ourself/state and never
  contains secret values or presented tokens.

### Verification (on main after the fast-forward)
- npm test on main: 87/87 pass (and 87/87 twice in the pre-merge dry-run).
- Production JSONL logs byte-unchanged (SHA-256 identical before/after):
  transmissions.jsonl 7d88d1a6…051dae5a · queue.jsonl d02cc57a…05e08125.
- node --check clean on server.js, tools/execution-classes.js, and the new
  test/execution-classes.test.js.
- AXIOM untouched. RUORA root untouched until this authorized seal.
- Zero git remotes. Nothing published.

DESIGNATION: Execution Class Baseline = 64f5704 — the named reference point onto
which Pass 20B (firewall-by-class hardening) and Pass 20C (reverse_engineer
structured route) will attach.

## BRIDGE PASS 20B — FIREWALL-BY-CLASS HARDENING

Timestamp: Fri Jun 19 18:00:13 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Pass 20B was committed on the bridge at `e2a09bd751ad84c5f34611ec826f7506453e2bc4`,
and agent-bridge main advanced `64f57045b1b281c99d0d20cdd3488276a1a88faf` →
`e2a09bd751ad84c5f34611ec826f7506453e2bc4` by PURE FAST-FORWARD (no merge commit).

Preceded by a Root Hygiene Pass (RUORA root commit `542938d`) that added the
benign OURSELF preservation/quarantine directories (backups/, systems/,
quarantine/) to .gitignore — kept on disk, never tracked, no secrets — restoring
root cleanliness before this seal.

### Installed capability
Pass 20B turns the execution-class METADATA from 20A into ACTIVE per-class
enforcement at the point of execution — the muscle layer over the skeleton.

- `tools/command-firewall.js` gains `enforceClassPolicy(action, executionClass)`:
  per-class command-shape policy. inspect = read-only only; test = test/check
  runners only; build = local build/dependency only (no deploy/publish/upload);
  git-read = read-only git (+ branch/worktree listing), no writes/network;
  git-write-local = local git mutations only, still forbids push/remote/gh/
  publish; project-mutation = in-boundary writes only, never .env/secrets/*.pem/
  credentials/audit-logs or outside the RUORA boundary. forbidden and
  reverse_engineer are terminal-forbidden (never reach the shell). This is an
  INDEPENDENT second implementation of the shapes (no import of execution-classes)
  — defense in depth: classifier and policy must agree or the command is refused.
- `tools/terminal.js` enforces the class policy in executeCommand BEFORE the
  generic denylist, failing closed (classPolicyDenied) without spawning a shell.
  The Pass 18 denylist (inspectCommand) remains the always-on FINAL fail-closed
  backstop; class permissions are never weaker than it. Legacy no-class callers
  keep the prior firewall-only path unchanged.
- `server.js` /approve passes the already-validated cmd.executionClass into
  executeCommand, so the terminal re-verifies the class at execution time.

### Verification (on main after the fast-forward)
- npm test on main: 107/107 pass (and 107/107 twice in the pre-merge dry-run,
  with NO flake observed in the dry-run).
- Known caveat: one NON-REPRODUCIBLE environmental flake occurred once across 33
  pre-commit runs (never recurred in 32 retries), attributed to the pre-existing
  Realm Gate rate-limit wall-clock timing — to be made deterministic in Pass 20B.1.
- Production JSONL logs byte-unchanged (SHA-256 identical before/after):
  transmissions.jsonl 7d88d1a6…051dae5a · queue.jsonl d02cc57a…05e08125.
- node --check clean on all changed JS.
- Realm Gate / token gate / rate limiter / approval gate / RUORA boundary
  unchanged. AXIOM untouched. RUORA root clean (542938d) until this authorized
  seal. Zero git remotes. Nothing published.

DESIGNATION: Firewall-by-Class Baseline = e2a09bd — the named reference point onto
which Pass 20B.1 (deterministic rate-limit timing) and Pass 20C (reverse_engineer
structured route) will attach.

## SELF SNAPSHOT SEALED

Timestamp: Wed Jun 24 20:45:58 EDT 2026
Transformation:
- Preserved verified SELF state: Install OURSELF Master Command Doctrine — SELFControl
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Wed Jun 24 20:56:55 EDT 2026
Transformation:
- Preserved verified SELF state: Pass 21 — Doctrine Integrity Expansion: witness ourself_master_command.md
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 25 13:39:25 EDT 2026
Transformation:
- Preserved verified SELF state: OURSELF Witness Law ratified at ac2c113
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 25 14:01:48 EDT 2026
Transformation:
- Preserved verified SELF state: Witness Law refined: anchor sentence + observed reality
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 25 19:04:45 EDT 2026
Transformation:
- Preserved verified SELF state: Ledger 18:49 EDT: queue candidate runtime primitives (hypotheses)
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 25 19:22:46 EDT 2026
Transformation:
- Preserved verified SELF state: Ledger 19:12 EDT: queue Candidate Authority Architecture (not constitutionalized)
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## SELF SNAPSHOT SEALED

Timestamp: Thu Jun 25 20:47:14 EDT 2026
Transformation:
- Preserved verified SELF state: Ledger 20:44 EDT: queue Mutation Accounting + Economics axis (candidates)
- Staged trusted SELF paths only
- Rejected secret-bearing PEM files from versioned memory

## BRIDGE PASS 20B.1 — DETERMINISTIC RATE-LIMIT TIMING

Timestamp: Fri Jun 26 14:45:26 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Pass 20B.1 was committed on the bridge at `860a9a576b35d461dc92800f0e58f40da35f68f3`,
and agent-bridge main advanced `e2a09bd751ad84c5f34611ec826f7506453e2bc4` →
`860a9a576b35d461dc92800f0e58f40da35f68f3` by PURE FAST-FORWARD (no merge commit).

Sealed from branch `pass-20b1-deterministic-rate-limit-timing` (worktree
`agent-bridge-pass-20b1`).

### Installed capability
Pass 20B.1 makes the Realm Gate rate-limit timing DETERMINISTIC, resolving the
non-reproducible wall-clock timing flake recorded in Pass 20B (one flake across 33
pre-commit runs, attributed there to the pre-existing rate-limit wall-clock timing).

- New `tools/realm-gate.js` isolates the rate-limit/lockout primitive behind an
  injectable time source, so window expiry and lockout expiry are reached by
  ADVANCING INJECTED TIME, not by wall-clock waiting — making the gate's timing
  testable and deterministic.
- New `test/realm-gate.test.js` exercises the gate deterministically: a valid token
  is never rate-limited and clears the failure record; a valid token passes even
  while a key is locked out; lockout expiry is reached by advancing injected time;
  a fresh window starts after the window elapses; and the limiter never receives or
  stores a token value.
- `server.js` and `test/rate-limit.test.js` updated to consume the deterministic
  gate. Token secrecy preserved: presented tokens are never received, stored, or
  logged by the limiter.

### Verification
- npm test on branch `pass-20b1` before seal: 116/116 pass, 0 fail.
- npm test on main after the PURE FAST-FORWARD: 116/116 pass, 0 fail.
- Files changed (e2a09bd..860a9a5): server.js · test/rate-limit.test.js ·
  test/realm-gate.test.js (new) · tools/realm-gate.js (new) — 4 files, +233/-30.
- History shape: linear, no merge commit. Final git status: clean.
- Zero git remotes. Nothing pushed. Nothing published.

DESIGNATION: Security Kernel Baseline = 860a9a5 — the named reference point onto
which Pass 20C (reverse_engineer structured route) will attach.

## BRIDGE PASS 20C — REVERSE_ENGINEER ANALYSIS ORGAN

Timestamp: Fri Jun 26 15:20:00 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Pass 20C was committed on the bridge at `6564d70` (branch
`pass-20c-reverse-engineer-route`), and agent-bridge main advanced
`860a9a576b35d461dc92800f0e58f40da35f68f3` → `6564d70` by PURE FAST-FORWARD
(no merge commit). A dry-run ancestry check confirmed the fast-forward before
the merge.

### Installed capability
Pass 20C manifests the deferred `reverse_engineer` execution class as the
bridge's FIRST ANALYSIS ORGAN: a non-terminal, approval-gated, read-only
structural inspection route — perception of structure without the right to
alter it.

- New route `POST /reverse-engineer` (token-gated) enqueues a NON-TERMINAL
  analysis request (kind:'analysis', class:reverse_engineer). The target path is
  boundary-gated and secret-path-refused at enqueue, using the kernel's SINGLE
  SECRET_PATH source of truth (symlinks resolved via realpath first).
- Approval-gated: the request runs only after explicit `POST /approve/:id`. The
  /approve analysis branch dispatches to the in-process inspector and RETURNS
  before the Pass 20A execution-class gate (evaluateApproval) and before
  executeCommand — so analysis can never reach the shell.
- New `tools/reverse-engineer.js` performs in-process, read-only filesystem
  inspection (realpath/readdir/stat/lstat/readFile only) and returns a STRICT
  JSON artifact: request_id, class, analysis_only, mutation, terminal, target,
  summary, structure, signals (routes/schemas/workflows/dependencies), risks,
  non_actions. Bounded (depth/entry/scan caps). No shell, no spawn/child_process,
  no network, no writes. Secret-bearing files surface as risks and are NEVER read.

### Verification (on main after the fast-forward)
- npm test on main: 132/132 pass, 0 fail (116 prior baseline + 16 new).
- Changed files (860a9a5..6564d70): server.js · tools/reverse-engineer.js (new) ·
  tools/execution-classes.js · test/reverse-engineer.test.js (new) — 4 files.
- tools/terminal.js UNCHANGED. tools/command-firewall.js UNCHANGED.
- tools/execution-classes.js change was EXPORT-ONLY: `const SECRET_PATH` →
  `export const SECRET_PATH` (+ explanatory comment). The frozen class schema is
  untouched: reverse_engineer remains mutation:false, terminal:false,
  analysisOnly:true, requiresApproval:true.
- Shell guarantees preserved: classifyCommand never emits reverse_engineer;
  evaluateApproval('reverse_engineer', <shell>) still fails closed
  (non_terminal_class).
- History shape: linear, no merge commit. Final git status: clean.
- Zero git remotes. Nothing pushed. Nothing published. No deploy.

DESIGNATION: Reverse-Engineer Analysis Baseline = 6564d70 — the named reference
point onto which Pass 21A (OURSELF Mouth / SIA Router) will attach.

## CONTROL-PLANE PASS 21A.2 — FROZEN SIA REGISTRY SCHEMA

Timestamp: Fri Jun 26 15:35:00 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Repo: ~/RUORA/systems/ourself-agent-bridge (OURSELF control plane — distinct from
the agent-bridge kernel). Pass 21A.2 was committed on branch
`pass-21a2-sia-registry-schema` at `44aaa60`, and control-plane main advanced
`8bfebbb` → `44aaa60` by PURE FAST-FORWARD (no merge commit). A dry-run ancestry
check confirmed the fast-forward before the merge. Parent spec: `8bfebbb`
(doctrine: 21A Mouth/SIA Router spec, child of AECHO seal `10c5342`).

KERNEL UNTOUCHED: the agent-bridge kernel remains at `6564d70`. This is a
control-plane (symbolic/declaration) seal; the verified technical layer is not
modified.

### Installed capability
Pass 21A.2 establishes the FIRST OURSELF NOUN-SET: the frozen SELFIntelligence
Agent (SIA) registry — the recognized actor set the Router will route against.
Data + validation only; it never executes, routes, or mutates.

- New self-contained `router/` subsystem (sibling of `command-mouth/`),
  zero-dependency ESM, `node --test`.
- `router/sia-registry.js` declares seven SIAs — ChatSELF, ClaudeCodeSELF,
  CodexSELF, BubbleSELF, LedgerSELF, ObserverSELF, ReviewerSELF — each with:
  allowed_routes, forbidden_routes, can_mutate, approval_required,
  records_touched, handoff_rules, proof_required, notes.
- Invariants (validated at import, deep-frozen at runtime): unique ids; non-empty
  role; allowed/forbidden never overlap; no non-mutating SIA may hold a mutating
  route; every mutating SIA requires approval; ≥1 proof requirement each;
  unknown SIA and unknown route lookups FAIL CLOSED.
- Exports: SIA_REGISTRY, SIA_IDS, getSia, listSias, assertValidSiaRegistry,
  canSiaUseRoute, canSiaMutate, getSiasForRoute (+ KNOWN_ROUTES, MUTATING_ROUTES).

### Verification (on main after the fast-forward)
- npm --prefix router test on main: 19/19 pass, 0 fail.
- node --check clean on router/sia-registry.js and router/test/sia-registry.test.js.
- Changed files (8bfebbb..44aaa60): router/package.json · router/sia-registry.js ·
  router/test/sia-registry.test.js — 3 files.
- command-mouth runtime UNCHANGED. agent-bridge kernel UNCHANGED (`6564d70`).
- No route classifier created. No AEPACKET generator created. No API endpoint
  created. No Bubble implementation. No OURSELF doctrine file modified.
- Source-safety (tested): no shell/child_process/spawn/exec, no network, no
  file-write primitives; no import of the kernel or command-mouth; no AECHO/ledger
  writes.
- History shape: linear, no merge commit. Final git status: clean.
- Zero git remotes. Nothing pushed. Nothing published. No deploy.

DOCTRINE NOTE: 21A.2 seals the first OURSELF noun-set. 21A.3 (route classifier —
the first verb-set layer) will consume this registry as its recognized actor set.

DESIGNATION: SIA Registry Baseline = 44aaa60 — the named reference point onto
which Pass 21A.3 (route classifier) will attach.

## CONTROL-PLANE PASS 21A.3 — ROUTE CLASSIFIER / VERB-SET LAYER

Timestamp: Fri Jun 26 16:05:00 EDT 2026
Correction type: APPEND-ONLY. No prior entry rewritten.

Repo: ~/RUORA/systems/ourself-agent-bridge (OURSELF control plane — distinct from
the agent-bridge kernel). Pass 21A.3 was committed on branch
`pass-21a3-route-classifier` at `2613e6a`, and control-plane main advanced
`44aaa60` → `2613e6a` by PURE FAST-FORWARD (no merge commit). A dry-run ancestry
check confirmed the fast-forward before the merge. Parent noun-set: SIA Registry
Baseline `44aaa60` (RUORA ledger seal `abab6b0`).

KERNEL UNTOUCHED: the agent-bridge kernel remains at `6564d70`. This is a
control-plane (symbolic/declaration) seal; the verified technical layer is not
modified.

### Installed capability
Pass 21A.3 establishes the FIRST OURSELF VERB-SET LAYER: a pure, deterministic,
fail-closed route classifier that maps validated SELF language into a DRY-RUN
route plan. It consumes the sealed SIA registry (noun-set) and can never
contradict it. It never dispatches, executes, mutates, calls the kernel, writes
AECHO, writes the ledger, or creates an endpoint.

- `router/route-classifier.js` declares a 13-route taxonomy (per
  doctrine/21A-MOUTH-ROUTER-SPEC.md §6) whose allowed_sias are DERIVED from the
  registry, so the verb-set is automatically consistent with the noun-set.
- classifySelfCommand(input) returns a plan: route, sia, execution_class,
  mutation, requires_approval, proof_required, reason, status (planned|discarded).
- Fail-closed: unknown / empty / unsafe (publish/push/deploy/secret/.env) and any
  unmatched input resolve to `discard` — never a guessed route.
- Laws enforced + tested: cognition routes use execution_class null;
  project-mutation maps only to ClaudeCodeSELF (high approval + before/after
  proof); mutating routes require approval and map only to mutating SIAs;
  reverse_engineer → class reverse_engineer / mutation false / approval true;
  output carries NO kernel dispatch descriptor.
- Exports: ROUTE_TAXONOMY, ROUTE_IDS, classifySelfCommand, getRoute, listRoutes,
  assertValidRouteTaxonomy, isMutatingRoute, routeRequiresApproval,
  getAllowedSiasForRoute.

### Verification (on main after the fast-forward)
- npm --prefix router test on main: 45/45 pass, 0 fail (19 registry + 26 classifier).
- node --check clean on router/route-classifier.js and its test.
- Changed files (44aaa60..2613e6a): router/route-classifier.js ·
  router/test/route-classifier.test.js — 2 files.
- command-mouth runtime UNCHANGED. agent-bridge kernel UNCHANGED (`6564d70`).
- No AEPACKET generator created. No API endpoint created. No CLI mouth created.
  No Bubble implementation. No OURSELF doctrine file modified.
- Source-safety (tested): no shell/child_process/spawn/exec, no network, no
  file-write primitives; no import of the kernel or command-mouth; no AECHO/ledger
  writes.
- History shape: linear, no merge commit. Final git status: clean.
- Zero git remotes. Nothing pushed. Nothing published. No deploy.

DOCTRINE NOTE: 21A.3 seals the first OURSELF verb-set layer. 21A.4 (AEPACKET
generator) will consume the noun-set and verb-set to build the first sentence
layer.

DESIGNATION: Route Classifier Baseline = 2613e6a — the named reference point onto
which Pass 21A.4 (AEPACKET generator) will attach.
