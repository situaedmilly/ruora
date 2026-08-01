# 02_SYNCHRONIZATION

**Document identifier:** `governance/agentbridge/workflow/02_SYNCHRONIZATION.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

Fresh, read-only synchronization between what the session currently believes
(from `SESSION_CONTEXT` and memory) and what live evidence actually shows.
Produces `SynchronizationContext`. This document never repairs anything it
finds — repair requires a separately authorized `MUTATION_SIGNAL` gate under
`04_GATE_EXECUTION.md`.

## Authority granted

- Read FOUNDATION documents (doctrine, prior seals, prior roadmap state).
- Perform live INSPECTION of repository and runtime-evidence state.
- Perform independent VERIFICATION of claims found in FOUNDATION against
  live INSPECTION.
- Classify the session as an inaugural baseline establishment or a
  steady-state drift comparison.
- Produce `SynchronizationContext` as output.

## Authority explicitly not granted

- No repair of detected drift, conflict, or missing evidence.
- No mutation of runtime evidence, kernel, or control-plane source.
- No silent reconciliation — every discrepancy found is reported, not
  resolved, by this document.

## Required inputs

- `SESSION_CONTEXT` from `01_SESSION_BOOTSTRAP.md`.
- FOUNDATION: prior doctrine, prior seal records, prior
  `07_LAUNCH_ROADMAP.md` state.
- Live repository and runtime-evidence state.

## Required procedure

1. Load FOUNDATION: the last known-sealed state (prior roadmap, prior seal
   witnesses, prior `SynchronizationContext` if one exists).
2. Perform live INSPECTION: re-read the repositories and runtime-evidence
   store as they exist right now. Do not accept FOUNDATION's description of
   current state as current — treat it as a claim to be checked.
3. Perform independent VERIFICATION: for each material claim in FOUNDATION,
   confirm or refute it against live INSPECTION.
4. Classify:
   - **Inaugural baseline establishment** — no prior `SynchronizationContext`
     exists; this session's output becomes the first baseline.
   - **Steady-state drift comparison** — a prior baseline exists; this
     session compares live state against it and reports delta only.
5. Produce `SynchronizationContext` with the required fields below.
6. Assign exactly one verdict from the allowed list. Never repair based on
   the verdict within this document.

## Required output — `SynchronizationContext`

```
SynchronizationContext
  Repository revisions:                 <HEAD per canonical repo root>
  Evidence-store hashes:                <content hash(es) of runtime
                                          evidence root, if applicable>
  Proof-chain count:                    <n>
  Non-chain governance-record count:    <n>
  Event-ledger count and validity:      <n, VALID|INVALID|UNVERIFIABLE>
  Proof Chain Integrity Matrix:         <per-chain status table>
  Active governance-publication count:  <n>
  Current authority surface:            <as read live from
                                          07_LAUNCH_ROADMAP.md, not memory>
  T-034 quarantine state:               <QUARANTINED|ACTIVE|UNKNOWN>
  Known schema drift:                   <list, or NONE>
  Human_TURN limitation:                <explicit note on what this session
                                          could not independently verify
                                          without a human-performed step>
  Classification:                       <INAUGURAL_BASELINE|DRIFT_COMPARISON>
  Verdict:                              <see allowed list>
```

## Allowed verdicts

- `FOUNDATION_BASELINE_BOOTSTRAPPED`
- `FOUNDATION_BASELINE_VERIFIED`
- `FOUNDATION_BASELINE_DRIFT_DETECTED`
- `FOUNDATION_BASELINE_CONFLICTED`
- `FOUNDATION_BASELINE_UNAVAILABLE`
- `HOLD`
- `FAILED`

Exactly one verdict per synchronization run. Verdicts are never combined.

## Refusal / HOLD conditions

- FOUNDATION is unavailable or unreadable → `FOUNDATION_BASELINE_UNAVAILABLE`.
- Live inspection contradicts FOUNDATION on a material fact (authority
  surface, proof-chain count, quarantine state) → `FOUNDATION_BASELINE_CONFLICTED`
  or `FOUNDATION_BASELINE_DRIFT_DETECTED`, whichever fits; never silently
  pick the more convenient reading.
- Any attempt to repair a finding inside this document → refuse; redirect
  to `03_GATE_SELECTION.md` for a properly authorized repair gate.

## Launch-state footer

`SynchronizationContext.Current authority surface` and
`Steps Until SELFLaunch` (carried from `07_LAUNCH_ROADMAP.md`) are restated
at the end of this document's output, sourced live, not from memory.
