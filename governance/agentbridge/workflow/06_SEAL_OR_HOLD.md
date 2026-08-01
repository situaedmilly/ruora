# 06_SEAL_OR_HOLD

**Document identifier:** `governance/agentbridge/workflow/06_SEAL_OR_HOLD.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

The canonical verdict protocol. Converts a Verification Report into exactly
one primary verdict and a completion witness. This is the only document in
the stack authorized to declare a gate closed.

## Authority granted

- Read the Verification Report and Gate Execution output.
- Issue exactly one primary verdict.
- Produce the required completion witness.
- Append-only recording of reviewer discoveries (findings are never erased,
  only ever added to or explicitly superseded by a later, separately dated
  finding).

## Authority explicitly not granted

- No mutation. This document only judges what `04_GATE_EXECUTION.md` did
  and `05_VERIFICATION.md` checked; it does not itself change anything.
- No commit/push authority — a `SEALED` or `READY_FOR_COMMIT` verdict is not
  itself a commit or push action; those remain separately authorized.
- No production-use authorization — sealing a gate does not authorize
  operating on production beyond what the gate itself already proved.
- No combining of verdicts (e.g. "SEALED, but also HOLD on the side").

## Required inputs

- Verification Report from `05_VERIFICATION.md`.
- Gate Selection and Gate Execution outputs.

## Allowed primary verdicts

- `SEALED`
- `READY_FOR_REVIEW`
- `READY_FOR_COMMIT`
- `HOLD`
- `CHANGES_REQUIRED`
- `FAILED`
- `AMEND`
- `REJECT`

Exactly one primary verdict is issued per gate. Never more than one.

## Verdict definitions

- **`SEALED`** — permitted only when: static containment is `CONTAINED`,
  targeted tests and full regression both pass, cold-process verification
  was actually performed (not skipped) and passed, ledger continuity is
  `CONTINUOUS`, and no `PROPOSITION_INFLATION` was detected. A narrative
  claim of success ("this works now") is never sufficient by itself — only
  the Verification Report's fields above can produce `SEALED`.
- **`HOLD`** — required whenever any material finding is unresolved:
  containment violation, regression failure, ledger gap, or an unmapped
  claim. `HOLD` is the default whenever `SEALED`'s conditions are not fully
  met and the gap is not narrow enough for `CHANGES_REQUIRED`.
- **`CHANGES_REQUIRED`** — narrower than `HOLD` or `REJECT`: the gate's
  direction is sound and its scope stays valid, but a specific, nameable
  defect must be fixed (as its own bounded-repair gate) before this gate
  can be re-submitted for a verdict. Use this only when the fix is fully
  specifiable now; if it is not, use `HOLD` instead.
- **`READY_FOR_REVIEW`** / **`READY_FOR_COMMIT`** — the gate is internally
  sound per verification but a human/Founder decision gate stands between
  here and `SEALED` (design or decision-only gates land here, not at
  `SEALED`, until that review actually happens).
- **`FAILED`** — the gate's approach itself is falsified by the evidence,
  not merely incomplete; per `04_GATE_EXECUTION.md`'s lifecycle rules, a
  lawful stop at Design because the design does not survive scrutiny is
  **not** `FAILED` — it is a successful use of the workflow and should be
  recorded as `HOLD` or `REJECT` on the specific design, not as a system
  failure.
- **`AMEND`** — the underlying design/decision needs a specific, named
  revision before re-attempting the gate.
- **`REJECT`** — the approach is not to be pursued; distinct from `FAILED`
  in that `REJECT` is a decision (this is not the direction to take) rather
  than a technical falsification.

Why a narrative success statement is not a seal: prose describing success
is not evidence: it is a claim about evidence. Only the Verification
Report's independently derived fields can ground `SEALED`.

Why reviewer discovery stays append-only: a finding that is quietly deleted
after being surfaced destroys the audit trail that makes any future
`SEALED` verdict trustworthy. Findings are superseded explicitly, dated, and
never erased.

Why commit/push and production use remain separately authorized: a seal
certifies that the verified work meets the bar for its own scope. It does
not, by itself, grant authority to act further (commit, push, or touch
production) — those require their own named `MUTATION_SIGNAL` per
`04_GATE_EXECUTION.md`.

## Required completion witness

```
UTC timestamp:              <ISO-8601 UTC>
Repositories:                <list, with paths>
Baseline HEAD:               <HEAD at gate start, per repo>
Resulting HEAD, if changed:  <HEAD at gate end, per repo, or UNCHANGED>
Files changed:                <exact list, or NONE>
Tests:                        <targeted + full regression summary>
Containment:                  <CONTAINED|VIOLATION>
Evidence artifacts:            <list produced by this gate>
Ledger/index effects:          <list, or NONE>
Commit/push status:            <NOT_PERFORMED|COMMITTED|PUSHED, with detail>
Production status:             <NOT_TOUCHED|PROVEN|N/A>
Final verdict:                 <exactly one, from the allowed list>
Next lawful gate:               <from 07_LAUNCH_ROADMAP.md>
Steps Until SELFLaunch:         <trailing count>
```

## Refusal / HOLD conditions

- More than one primary verdict is about to be issued → refuse; force a
  single verdict decision first.
- The Verification Report shows any containment violation → verdict cannot
  be `SEALED`; must be `HOLD`, `CHANGES_REQUIRED`, or `REJECT`.
- Cold-process verification was skipped or unavailable → verdict cannot be
  `SEALED`; treat as `HOLD` at minimum.

## Launch-state footer

Every completion witness restates `Next lawful gate` and
`Steps Until SELFLaunch`, both re-derived live from `07_LAUNCH_ROADMAP.md`
after this verdict is recorded there.
