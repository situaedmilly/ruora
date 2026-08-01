# 04_GATE_EXECUTION

**Document identifier:** `governance/agentbridge/workflow/04_GATE_EXECUTION.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

Execute exactly the one gate named by `03_GATE_SELECTION.md`, using the
lifecycle proven by SL-008A. Encodes that lawful stopping at any stage is a
valid outcome, and that no stage's completion implies authority for the
next.

## Authority granted

Only the exact allowed actions named in the Gate Selection output for the
single named gate. Nothing beyond that scope, regardless of what would be
convenient or "obviously fine" to also do while here.

## Authority explicitly not granted

- No stage implies the next. Completing Design does not authorize
  Implementation. Completing Implementation does not authorize
  Production Proof. Each transition requires its own signal.
- No commit or push without a separately issued authorization for that
  specific commit/push, scoped to specific files.
- No production proof of any kind without separate authority for that
  proof.
- T-034 remains quarantined unless a separate, explicit activation signal
  admits it. Its quarantine is never lifted as a side effect of executing
  an unrelated gate.
- No mutation outside the exact file/path scope named for this gate.

## Required inputs

- Gate Selection output from `03_GATE_SELECTION.md`.

## The lifecycle

```
Design
  → Implementation
  → Regression
  → Production Proof
  → Cold Verification
  → Stabilization
  → Authority Expansion
```

Governing rules for this lifecycle:

1. Stages may stop lawfully at any point. A gate that stops at Design having
   found the design does not survive scrutiny is a **successful** exercise
   of governance, not a failure to complete something owed.
2. No later stage is implied by completing an earlier one. Each stage
   boundary requires a fresh, explicit signal to proceed.
3. Every mutation requires an exact file scope, stated before the mutation,
   not reconstructed afterward from what was touched.
4. Every production proof requires authority separate from the
   implementation authority that preceded it.
5. Every commit and every push requires authority separate from the
   implementation and from each other — a commit authorization is not a
   push authorization.
6. T-034 remains quarantined by default in every gate executed under this
   document, unless a distinct, explicitly named activation signal admits
   it for that gate alone.

## Required procedure

1. Confirm the gate identity, allowed actions, and forbidden actions match
   exactly what `03_GATE_SELECTION.md` produced. Any drift → `HOLD`, return
   to gate selection.
2. Execute only the stage(s) explicitly authorized. Stop at the first stage
   boundary that lacks its own explicit signal to continue.
3. At each stage, use the matching template below. Do not blend templates.
4. Record what was actually done (not what was planned) as the gate's
   output, to hand to `05_VERIFICATION.md`.

## Reusable gate templates

### Decision-only gate
- Input: a question requiring a Founder/human decision.
- Allowed: present options, tradeoffs, and a recommendation.
- Forbidden: implementing any option before the decision is made.
- Output: the decision recorded, or `HOLD` if undecided.

### Design-only gate
- Input: an objective requiring a design before any code/doc changes.
- Allowed: produce the design artifact (as a candidate-corpus document).
- Forbidden: implementation of the design.
- Output: design artifact + explicit statement that implementation is a
  separate, not-yet-authorized gate.

### Implementation gate
- Input: an already-reviewed design, explicit file scope.
- Allowed: mutation strictly within the named file scope.
- Forbidden: staging, committing, pushing, or touching files outside scope.
- Output: diff description, confined to the named scope.

### Bounded repair gate
- Input: a specific finding from `05_VERIFICATION.md` or
  `02_SYNCHRONIZATION.md`, explicitly authorized for repair.
- Allowed: the single named repair only.
- Forbidden: repairing any other finding discovered along the way without
  its own separate authorization.
- Output: the repair, plus an explicit list of any other findings noticed
  but *not* repaired under this gate.

### Commit-and-push gate
- Input: a completed, verified implementation with explicit commit/push
  authorization naming the exact files.
- Allowed: `git add` of only the named files, commit with an accurate
  message, push only if push is separately named in the authorization.
- Forbidden: `git add -A` / `git add .`, committing unrelated untracked
  files, force-push, push without explicit separate authorization.
- Output: resulting HEAD, files committed, push status.

### Production success proof
- Input: an implementation already verified in cold isolation.
- Allowed: execute the proof path in production and capture the witness.
- Forbidden: treating a successful proof as authorization for further,
  unrelated production actions.
- Output: witness record (what ran, what it touched, what it produced).

### Production refusal proof
- Input: a case that should be **refused** by the system under test.
- Allowed: execute the refusal path and capture that it was correctly
  refused.
- Forbidden: treating a refusal proof as equivalent to a success proof, or
  vice versa.
- Output: witness record showing the refusal occurred as designed.

### Replay / idempotency proof
- Input: a previously proven action, repeated under proof conditions.
- Allowed: re-execute and confirm at-most-once / idempotent behavior.
- Forbidden: assuming idempotency without an explicit replay witness.
- Output: witness record comparing first and repeat execution effects.

## Refusal / HOLD conditions

- The gate about to be executed does not exactly match
  `03_GATE_SELECTION.md`'s output → `HOLD`.
- A stage boundary is reached with no explicit signal to continue →
  stop lawfully; this is not a failure.
- Any action would exceed the named file/path scope → refuse the action,
  not the whole gate; report the boundary that was respected.
- T-034 activation is implied but not explicitly signaled → refuse;
  T-034 stays quarantined.

## Launch-state footer

Gate execution output feeds `05_VERIFICATION.md` directly and restates the
gate id, stage reached, and `Steps Until SELFLaunch` from
`07_LAUNCH_ROADMAP.md`.
