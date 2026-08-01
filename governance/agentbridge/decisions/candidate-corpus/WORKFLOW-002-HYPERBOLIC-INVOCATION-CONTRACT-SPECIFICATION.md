# WORKFLOW-002 — HYPERBOLIC CHAMBER INVOCATION CONTRACT
## Canonical Specification

STATUS: PARKED
CLASSIFICATION: ARCHITECTURAL_DESIGN_CANDIDATE (Design stage only, per
  `04_GATE_EXECUTION.md`'s lifecycle — same stage as WORKFLOW-001)
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE
SCOPE: SPECIFICATION_ONLY — binds WORKFLOW-001's domain-agnostic packet
  contract to AgentBridge specifically. No routing implementation, no
  scheduler/planner implementation, no execution engine, no production
  activation, no code.

DEPENDENCY: WORKFLOW-003 (or any implementation) cannot begin until this
  document receives its own Founder disposition. As with WORKFLOW-001,
  disposition of this document is necessary but not sufficient for
  implementation — it specifies *how* AgentBridge would invoke the
  chamber, consistent with the architectural direction already stated;
  it does not itself route, schedule, or execute anything.

────────────────────────────────────────
0. INHERITED, NOT REPEATED
────────────────────────────────────────
This document assumes WORKFLOW-001's seven packet shapes, required
invariants, and forbidden states (FOUNDER-DISPOSITION-003, RATIFIED) as
given. It does not restate or re-derive them — see
`WORKFLOW-001-HYPERBOLIC-CHAMBER-RUNTIME-CONTRACT-SPECIFICATION.md`. Per
WORKFLOW-001 §C, this document is exactly the kind of binding it
anticipated: "what `witnessed_environment` resolves to for AgentBridge
specifically."

Existing AgentBridge doctrine reused here rather than duplicated:
  `04_GATE_EXECUTION.md` — lifecycle stages (Design → Implementation →
    Regression → Production Proof → Cold Verification → Stabilization →
    Authority Expansion); "no stage implies the next."
  `05_VERIFICATION.md` — cold-process verification (fresh process/
    session, not same context); the epistemic pipeline (artifact
    presence → interpretation validity → referent validity → temporal
    index); `PROPOSITION_INFLATION`.
  `06_SEAL_OR_HOLD.md` — the eight-verdict set (`SEALED`,
    `READY_FOR_REVIEW`, `READY_FOR_COMMIT`, `HOLD`, `CHANGES_REQUIRED`,
    `FAILED`, `AMEND`, `REJECT`); append-only reviewer-finding recording;
    "design or decision-only gates land at `READY_FOR_REVIEW`/
    `READY_FOR_COMMIT`, not `SEALED`, until that review actually
    happens."

────────────────────────────────────────
1. INVOCATION AUTHORITY
────────────────────────────────────────
This section specifies who/what MAY issue an `invocation_packet` for an
AgentBridge-bound chamber run, IF a run is ever invoked. It does not
itself invoke anything, and does not decide that AgentBridge invokes the
chamber by default or at all for any given gate.

- The issuer of an `invocation_packet` must supply
  `authority_packet.source_of_grant` (WORKFLOW-001 §A) pointing to a
  specific Gate Selection output (`03_GATE_SELECTION.md`) or a specific
  Founder disposition — never a self-declared grant. This mirrors
  `04_GATE_EXECUTION.md`'s existing rule: "Only the exact allowed actions
  named in the Gate Selection output for the single named gate."
- No AgentBridge role (Orchestrator, Planner, Executor, etc., per
  `04_ROLE_CONSTITUTIONS/`) may invoke a chamber run under authority it
  does not independently, verifiably hold — consistent with
  Orchestrator's own constitution ("No inherited mutation authority,
  ever... cannot aggregate authority from its children") and with
  SR-EXEC-001's now-ratified execute ceilings.
- Invocation authority is per-run, not standing. Each invocation
  requires its own fresh `invocation_packet`; no session or role
  retains authority to invoke a second run from a prior grant.

────────────────────────────────────────
2. INVOCATION PACKET (AgentBridge binding of WORKFLOW-001 §A)
────────────────────────────────────────
| WORKFLOW-001 field | AgentBridge-specific resolution |
|---|---|
| `chamber_id` | Fixed value for this binding: `hyperbolic-chamber-v1` |
| `cognitive_pressure` | Selected by whichever party holds the Gate Selection authority for the invoking gate — not by the chamber itself, and not by the role requesting invocation |
| `raw_task` | The exact task text from the relevant `03_GATE_SELECTION.md` output for the gate under consideration |
| `authorized_mutation_boundary` | The exact file/path scope `04_GATE_EXECUTION.md` would otherwise have granted that gate directly — invoking the chamber narrows or preserves this scope, never widens it |
| `requesting_identity` | The specific role-realized agent and its `selfrealization_record` reference (per `03_SELFREALIZATION_SCHEMA.yaml`), not a bare role name |

────────────────────────────────────────
3. INVOCATION LIFECYCLE
────────────────────────────────────────
Specification of where, IF bound, a chamber run would sit relative to
`04_GATE_EXECUTION.md`'s existing lifecycle — this section describes a
possible position, it does not wire it in:

```
Gate Selection (03_GATE_SELECTION.md)
  -> [optional] Hyperbolic Chamber invocation, scoped to Design stage only
  -> Gate Execution (04_GATE_EXECUTION.md) — proceeds with or without
     a prior chamber run; the chamber never replaces Gate Execution,
     it only front-loads reasoning-depth before Design begins
  -> Verification (05_VERIFICATION.md)
  -> Seal or Hold (06_SEAL_OR_HOLD.md)
```

A chamber run, if invoked, completes entirely within "Design" — it never
spans into or triggers Implementation, Regression, or Production Proof.
This preserves `04_GATE_EXECUTION.md`'s own rule unmodified: "No stage
implies the next."

────────────────────────────────────────
4. REVIEWER SELECTION INTERFACE
────────────────────────────────────────
Populates WORKFLOW-001's `evidence_packet.reviewer_identities`. Interface
only — no selection algorithm is implemented here.

- At `COGNITIVE_PRESSURE` levels requiring independent review (Gate 3
  §4, Level 2+), each reviewer must satisfy `05_VERIFICATION.md`'s
  existing cold-process standard: "a fresh process/session re-checking
  the claim, not the same context that produced it." A chamber run
  reusing its own Chamber 2/3 context for Chamber 6/7 review fails this
  interface by definition — this is a structural requirement, not a
  quality preference.
- The interface takes: `required_reviewer_count` (per level, values not
  fixed here — deferred, see §9 open items), `exclusion_set` (identities
  that produced the artifact under review, structurally barred from
  reviewing it — same rule as Verifier's own constitution: "Cannot
  verify work it produced itself").
- The interface returns: a list of reviewer identities plus, for each,
  a `source_of_grant` — no anonymous or unattributed reviewer is valid
  input to a `evidence_packet`.

────────────────────────────────────────
5. CONFIDENCE THRESHOLD INTERFACE
────────────────────────────────────────
Gate 3 §4 named this an unresolved open question ("what 'acceptable
uncertainty threshold' means numerically or structurally"). This section
defines the *interface shape* only — not the numbers:

- `threshold_input`: the `COGNITIVE_PRESSURE` level of the current run.
- `threshold_output`: one of `CLEARED` / `NOT_CLEARED` — reusing a
  binary shape consistent with this repo's existing `authority_grant`
  convention (no silent middle state).
- A run reporting `NOT_CLEARED` must produce a `failure_packet` (§8) —
  it may not silently downgrade its own `cognitive_pressure` level to
  manufacture a pass, per WORKFLOW-001's existing invariant: "A chamber
  run cannot grant itself a higher `cognitive_pressure` level's
  authority retroactively."
- The actual numeric/structural definition of `CLEARED` per level is
  explicitly NOT specified here — flagged as a genuine open item in §9,
  not silently resolved to keep this document appearing complete.

────────────────────────────────────────
6. DISAGREEMENT INTERFACE
────────────────────────────────────────
- Reviewer disagreement is recorded, not resolved by majority-override
  or silent discard — reusing `06_SEAL_OR_HOLD.md`'s existing rule:
  "append-only recording of reviewer discoveries (findings are never
  erased, only ever added to or explicitly superseded by a later,
  separately dated finding)."
- A `disagreement_log` entry: `{reviewer_identity, claim, agrees: bool,
  reasoning}` — one entry per reviewer per material claim.
- This interface does NOT define how disagreement is adjudicated (e.g.
  unanimous-required vs. majority vs. escalation) — that is a genuine
  open item (§9), because Gate 3 §4 explicitly deferred it: "exact
  reviewer counts and how disagreement among them resolves."

────────────────────────────────────────
7. CANCELLATION SEMANTICS
────────────────────────────────────────
- A chamber run may be cancelled only before Chamber 5 (Execution)
  begins. Per WORKFLOW-001's invariant, Chamber 5 is always a single
  mutator — cancellation mid-mutation is a forbidden state, not a
  supported transition, matching `04_GATE_EXECUTION.md`'s own rule that
  every mutation requires its exact scope stated before, not reconciled
  after.
- Cancellation produces a `failure_packet` with
  `classification: HOLD` (reusing `06_SEAL_OR_HOLD.md`'s definition:
  "required whenever any material finding is unresolved") — a
  cancelled run is not `FAILED` (which implies the run ran and did not
  succeed) and not silently discarded; it is witnessed as HOLD.
- Only the identity holding `source_of_grant` for the original
  `invocation_packet` may cancel it — not any reviewer, not the
  Orchestrator coordinating it (per Orchestrator's own "no inherited
  mutation authority" constitution).

────────────────────────────────────────
8. FAILURE SEMANTICS
────────────────────────────────────────
`failure_packet.classification` reuses `06_SEAL_OR_HOLD.md`'s existing
verdict set rather than inventing a parallel one:
  - `HOLD` — material finding unresolved (default, per existing
    definition).
  - `CHANGES_REQUIRED` — a specific, nameable defect in the chamber's
    own inputs (e.g., malformed `invocation_packet`), narrow enough to
    fix and re-invoke, not requiring a whole new binding decision.
  - `FAILED` — the run executed and did not produce a valid output at
    the stage it reached (distinct from cancellation, §7).
  - `REJECT` — reserved for Chamber 8 (Founder) explicitly declining to
    ratify, per Gate 3 §6: "Chamber 8 ... can never auto-approve."

────────────────────────────────────────
9. COMPLETION SEMANTICS
────────────────────────────────────────
`completion_packet.verdict` reuses `06_SEAL_OR_HOLD.md`'s distinction
directly: a chamber run — being a Design/decision-adjacent artifact, not
a mutation-and-proof gate — completes at `READY_FOR_REVIEW` or
`READY_FOR_COMMIT`, **never** `SEALED`, until Chamber 8's Founder review
actually happens. This is not a new rule invented for the chamber; it is
`06_SEAL_OR_HOLD.md`'s own existing text applied directly: "design or
decision-only gates land here, not at `SEALED`, until that review
actually happens."

A `completion_packet` with `final_stage_reached: 8` requires a
human-attributable `founder_packet_ref` (WORKFLOW-001 §B) before
`READY_FOR_COMMIT` may be reported — matching WORKFLOW-001's own
invariant that Chamber 8 "never auto-approves."

────────────────────────────────────────
10. EVIDENCE EMITTED
────────────────────────────────────────
Every chamber run, regardless of outcome, must emit evidence sufficient
to walk `05_VERIFICATION.md`'s existing epistemic pipeline for every
material claim the run makes:

```
Artifact presence -> interpretation validity -> referent validity ->
temporal index
```

Concretely: each `evidence_packet` (WORKFLOW-001 §A) must include enough
for an independent reader to check (a) the cited artifact exists, (b) it
is being read correctly, (c) it actually supports the claim attributed
to it, (d) it is current rather than stale evidence presented as
current. A claim that outruns this — `PROPOSITION_INFLATION`, per
`05_VERIFICATION.md`'s existing naming — invalidates that specific claim,
not silently rounds up to accepted.

────────────────────────────────────────
GENUINE OPEN ITEMS (not resolved here, disclosed rather than hidden)
────────────────────────────────────────
- Exact `required_reviewer_count` per `COGNITIVE_PRESSURE` level (§4).
- Numeric/structural definition of `CLEARED` per level (§5).
- Disagreement adjudication rule — unanimous, majority, or escalation
  (§6). Gate 3 §4 named this unresolved; this document does not resolve
  it either.
These remain NOT_SCHEMA_EXPRESSIBLE / NOT_YET_SPECIFIED, consistent with
this repo's existing practice (SR-EXEC-001) of naming a gap rather than
filling it with an unsupported assumption.

────────────────────────────────────────
EXPLICITLY FORBIDDEN FOR THIS DOCUMENT
────────────────────────────────────────
Runtime implementation. Routing implementation. Scheduler
implementation. Planner implementation. Execution engine. Production
activation. Doctrine edits. Gate 3 edits. WORKFLOW-001 edits. A decision
that AgentBridge invokes the chamber for any specific gate, by default
or otherwise — this document specifies mechanics only, contingent on a
per-invocation decision each time.
