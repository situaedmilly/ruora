# 06_RUNTIME_FLOW

**Suite status:** CANDIDATE — not ratified, not runtime-enforced.
**Protocol version:** `ourself.agent-selfrealization.v1`

## Purpose

Chamber II. Executed only once a `selfrealization_record` with verdict
`REALIZED` exists and a `05_RUNTIME_AUTHORIZATION_PACKET.md` instance has
bound it to a specific gate.

## Authority granted by this document

Only whatever `05_RUNTIME_AUTHORIZATION_PACKET.md`'s instance for this
session explicitly states. This document does not itself grant anything.

## Required output

An execution witness (`07_EXECUTION_WITNESS_SCHEMA.yaml`) and a handoff
(`08_HANDOFF_SCHEMA.yaml`).

## Canonical prompt text

```
OURSELF · AGENT RUNTIME FLOW · v1.0

Your SELFREALIZATION RECORD has been accepted.
You are authorized only for the attached runtime gate.

Execute the following lifecycle exactly:

────────────────────────────────────────
09_RUNTIME_BOOT
────────────────────────────────────────
Bind:
SELFREALIZATION_RECORD
RUNTIME_AUTHORIZATION
CURRENT_GATE
CURRENT_ENVIRONMENT

Confirm that no field contradicts the witnessed environment.
If contradiction exists, stop with RUNTIME_BOOT_CONFLICT.

────────────────────────────────────────
10_SYNCHRONIZATION
────────────────────────────────────────
Freshly witness all volatile state required for the gate.

Verify:
repository
branch
HEAD
working tree
target files
dependencies
existing tests
current task lineage
authorization boundary

Do not mutate during synchronization unless explicitly permitted.

────────────────────────────────────────
11_GATE_SELECTION
────────────────────────────────────────
Confirm that the authorized gate is:
1. The next lawful gate
2. Not already completed
3. Not superseded
4. Not blocked by unresolved prior work
5. Fully inside the granted jurisdiction

Return:
GATE_ADMITTED
GATE_REJECTED
GATE_BLOCKED

Only GATE_ADMITTED may proceed.

────────────────────────────────────────
12_PLAN
────────────────────────────────────────
Produce the smallest sufficient execution plan.

Every planned action must include:
purpose
target
authority
expected state transition
verification
rollback

No speculative improvements.
No neighboring cleanup.
No architecture drift.

────────────────────────────────────────
13_EXECUTION
────────────────────────────────────────
Execute only admitted actions.

Before each mutation, confirm:
target is writable
change is necessary
change is bounded
rollback exists
evidence can be produced

Record actual actions, not intended actions.

────────────────────────────────────────
14_VERIFICATION
────────────────────────────────────────
Run fresh verification after mutation.

Verification must distinguish:
syntax
structure
behavior
security
containment
regression
lineage
working-tree state

A passing command without relevant coverage is not sufficient evidence.

────────────────────────────────────────
15_SEAL_OR_HOLD
────────────────────────────────────────
Return one:
SEALED
READY_FOR_FOUNDER_SEAL
HOLD
FAILED
ROLLED_BACK

Never self-seal unless seal authority was explicitly granted.

────────────────────────────────────────
16_MEMORY_COMMIT
────────────────────────────────────────
Produce a durable execution witness containing:
timestamp
session
agent
repository
branch
pre-HEAD
post-HEAD
authorized gate
files read
files changed
commands run
verification results
commit
seal state
remaining contradictions
next lawful gate

────────────────────────────────────────
17_HANDOFF
────────────────────────────────────────
End with:
CURRENT STATE
PROVEN STATE
UNPROVEN STATE
OUTSTANDING RISK
NEXT LAWFUL GATE
AUTHORITY REQUIRED
```

## Refusal / HOLD conditions

- Any field bound in `09_RUNTIME_BOOT` contradicts witnessed environment →
  `RUNTIME_BOOT_CONFLICT`; do not proceed past boot.
- `11_GATE_SELECTION` returns anything other than `GATE_ADMITTED` → stop;
  do not proceed to `12_PLAN`.
- `13_EXECUTION` would require a target, authority, or scope not present in
  the Runtime Authorization Packet → refuse that specific action; do not
  substitute a "close enough" action.
- `15_SEAL_OR_HOLD` self-seal is attempted without explicit seal authority
  in the packet → refuse; downgrade to `READY_FOR_FOUNDER_SEAL`.

## Launch-state footer

`17_HANDOFF`'s `NEXT LAWFUL GATE` and `AUTHORITY REQUIRED` fields are the
live analogue of `governance/agentbridge/workflow/07_LAUNCH_ROADMAP.md`'s
trailing footer — but this suite's handoff is per-agent-session, not a
single global roadmap. See `00_MANIFEST.md` for the unresolved question of
how (or whether) these two ever merge.
