# 03_GATE_SELECTION

**Document identifier:** `governance/agentbridge/workflow/03_GATE_SELECTION.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

Select exactly one active, executable gate from `07_LAUNCH_ROADMAP.md`'s
open work. This is the only document in the stack that names what happens
next; it does not perform it.

## Authority granted

- Read `SynchronizationContext` and `07_LAUNCH_ROADMAP.md`.
- Name exactly one gate as the session's current gate.
- Permit a synchronized, read-only decision or design track in parallel
  **only** when a separate, explicit authorization already admits it (e.g.
  the roadmap's "Parallel, non-blocking" track).
- Produce the Gate Selection output below.

## Authority explicitly not granted

- No execution of the selected gate — that begins only in
  `04_GATE_EXECUTION.md`.
- No selection of more than one **implementation** gate at a time.
- No inferred authorization: if the roadmap does not explicitly list a gate
  as open and its dependencies as met, it is not selectable.
- No resolution of ambiguous gate identity by guessing intent.

## Required inputs

- `SynchronizationContext` (verdict must not be `HOLD` or `FAILED`, or this
  document itself is blocked).
- `07_LAUNCH_ROADMAP.md`'s current "Open work, ordered" and "Parallel,
  non-blocking" lists.

## Required procedure

1. Confirm `SynchronizationContext` verdict permits proceeding
   (`FOUNDATION_BASELINE_VERIFIED` or `FOUNDATION_BASELINE_BOOTSTRAPPED`).
   Any other verdict → refuse gate selection, return to synchronization.
2. Read the roadmap's ordered open-work list. The next selectable gate is
   the first item whose dependencies are all satisfied.
3. If the objective under discussion does not map cleanly to exactly one
   roadmap item, refuse to select — name the ambiguity and stop. Do not
   invent a gate id, and do not silently select the "closest" one.
4. If two candidate gates appear simultaneously executable, select the one
   earlier in the ordered list; do not run both as implementation gates in
   the same session. A read-only decision/design track may run alongside an
   implementation gate only if the roadmap already separates them (see its
   "Parallel, non-blocking" track).
5. Produce the Gate Selection output.

## Required output — Gate Selection

```
Gate ID:                <exact roadmap item, e.g. "Persist BCP-000001">
Gate class:             <DECISION|DESIGN|IMPLEMENTATION|VERIFICATION|
                          BOUNDED_REPAIR|COMMIT_AND_PUSH|PRODUCTION_PROOF>
Controlling signal:     <signal class from 00_MANIFEST.md taxonomy>
Objective:              <one sentence, drawn from the roadmap item itself>
Evidence baseline:      <SynchronizationContext reference / timestamp>
Dependencies:           <roadmap items that must already be satisfied>
Allowed actions:        <exact list — nothing implied>
Forbidden actions:      <exact list, at minimum everything 07_LAUNCH_ROADMAP.md
                          marks "Not admitted">
Completion condition:   <what evidence must exist for this gate to be
                          considered complete>
Next possible gate:     <the following roadmap item, contingent on this
                          gate's outcome>
Steps Until SELFLaunch: <trailing count, from 07_LAUNCH_ROADMAP.md>
```

## Refusal / HOLD conditions

- `SynchronizationContext` verdict is `HOLD`, `FAILED`,
  `FOUNDATION_BASELINE_CONFLICTED`, or `FOUNDATION_BASELINE_UNAVAILABLE` →
  refuse gate selection entirely.
- The requested objective does not correspond to a single roadmap item →
  refuse; report the ambiguity instead of guessing.
- More than one **implementation** gate would need to run concurrently to
  satisfy the request → refuse; select the earlier one only.
- The named gate's dependencies are not all satisfied per
  `SynchronizationContext` → refuse; name the missing dependency.

## Launch-state footer

Gate Selection output always restates `Steps Until SELFLaunch` from the live
`07_LAUNCH_ROADMAP.md`, and the gate selected here becomes the `Current
gate` field the next `SESSION_CONTEXT` must report.
