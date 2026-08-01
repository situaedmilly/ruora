# GATE 5 — HYPERBOLIC CHAMBER IMPLEMENTATION CONTRACT
## Canonical Specification

STATUS: PARKED
CLASSIFICATION: IMPLEMENTATION_DESIGN_CANDIDATE (Design stage, per
  `04_GATE_EXECUTION.md`'s lifecycle — same stage as Gate 3/WORKFLOW-001/
  WORKFLOW-002, one level more concrete)
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE — no runtime code, no routing code, no
  scheduler, no planner, no execution engine, no implementation, no
  activation.
SCOPE: SPECIFICATION_ONLY. This document specifies what an
  Implementation-stage gate would build; it does not build it.

DEPENDENCY: Binds `WORKFLOW-001`'s domain-agnostic packet contract and
  `WORKFLOW-002`'s AgentBridge-specific invocation mechanics to concrete
  interface, persistence, and test shapes. Requires its own Founder
  disposition before any Implementation-stage gate may cite it as
  authorized ground, exactly as `WORKFLOW-001`/`WORKFLOW-002` each
  required before the next document in this lineage could proceed.

────────────────────────────────────────
0. INHERITED, NOT REPEATED — AND ONE CARRIED-FORWARD CAVEAT
────────────────────────────────────────
This document assumes, without restating: Gate 3's 8-stage chamber shape
and `COGNITIVE_PRESSURE` levels 0–5; `WORKFLOW-001`'s seven packet shapes,
execution contract, and forbidden states (`FOUNDER-DISPOSITION-003`,
RATIFIED); `WORKFLOW-002`'s AgentBridge-specific invocation authority,
lifecycle position, reviewer/confidence/disagreement interfaces, and
failure/completion semantics (`FOUNDER-DISPOSITION-004`, RATIFIED);
`GATE-4`'s architectural binding decision (`FOUNDER-DISPOSITION-006`,
RATIFIED: BOUND, per-invocation, Design-stage only, never standing).

**Carried forward from `GATE-4` §4, unchanged by this document**: Gate
3's own chamber-protocol content remains `STATUS: PARKED` —
un-dispositioned. This is the third Design-stage document in Track C
built on that un-ratified content without ratifying it, following the
exact same precedent `WORKFLOW-001` and `WORKFLOW-002` already set
(both written and later ratified while Gate 3 itself stayed un-disposed).
This document does not change that precedent's risk profile beyond what
`WORKFLOW-001`/`WORKFLOW-002` already accepted — but it is one layer
deeper, and is stated here rather than left implicit: **implementation
against this contract still requires Gate 3's own disposition first**,
per `GATE-4` §4 item 1, restated as this document's own §9 item 1 below.

────────────────────────────────────────
1. IMPLEMENTATION BOUNDARY
────────────────────────────────────────
Per `LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md`'s own "Governs:" line,
two repository roots exist for AgentBridge: the kernel
(`projects/agent-bridge`) and the control-plane
(`systems/ourself-agent-bridge`). Neither this document nor any prior
Track C document has inspected either repository's actual code — per
this gate's own token-alchemy constraint ("no rediscovery"), it does not
do so now either.

Proposed boundary, to be confirmed against the actual control-plane
layout at Implementation-stage time (§9 item 4), not assumed here:
implementation lives entirely within a new, clearly separated module
under the control-plane repository — e.g.
`systems/ourself-agent-bridge/hyperbolic-chamber/` — never inside
`governance/` (doctrine/markdown only), never inside the kernel root
(`projects/agent-bridge`, which `LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md`
governs under its own separate, narrower admitted-operations set), and
never touching any file this session's governance work has produced.
This boundary is a recommendation for the Implementation-stage gate to
adopt or correct, not a mutation performed here.

────────────────────────────────────────
2. RUNTIME INTERFACE
────────────────────────────────────────
Language-agnostic, pseudocode form — no programming language is assumed,
since no control-plane source was inspected under this gate's read
restriction. One function per chamber stage, each taking the prior
stage's output artifact plus the run's fixed `authorized_mutation_
boundary` and `cognitive_pressure` (Gate 3 §3's "common input contract"),
returning one `evidence_packet` or one `failure_packet`
(`WORKFLOW-001` §A):

```
runChamber1_RealitySynchronization(invocation_packet, context_packet)
  -> evidence_packet(REALITY_LOCKED) | failure_packet

runChamber2_IndependentExtraction(REALITY_LOCKED)
  -> evidence_packet(CANONICAL_MODEL) | failure_packet

runChamber3_AdversarialChamber(CANONICAL_MODEL)
  -> evidence_packet(SURVIVING_INVARIANTS) | failure_packet

runChamber4_SynthesisChamber(SURVIVING_INVARIANTS)
  -> evidence_packet(AMENDMENT_PLAN) | failure_packet

runChamber5_ExecutionChamber(AMENDMENT_PLAN)
  -> evidence_packet(PATCH) | failure_packet
  # single mutator only — WORKFLOW-001 §B forbidden-state: no concurrent
  # execution within one run

runChamber6_VerificationChamber(PATCH)
  -> evidence_packet(VERIFIED_PATCH) | failure_packet

runChamber7_ColdChamber(VERIFIED_PATCH)
  -> evidence_packet(COLD_VERDICT) | failure_packet
  # reviewer_identities required, exclusion_set enforced per
  # WORKFLOW-002 §4 — cold reviewer must not be an identity that
  # produced any upstream artifact in this same run

runChamber8_FounderChamber(COLD_VERDICT)
  -> evidence_packet(FOUNDER_PACKET) | failure_packet
  # never auto-approves — WORKFLOW-001 §B: a completion_packet with
  # final_stage_reached=8 and no human-attributable founder_packet_ref
  # is invalid by construction
```

Each function re-derives its inputs from disk state at call time (Gate 3
§3: "independently re-derivable from disk state, not carried forward as
an assertion") — it does not accept a trusted in-memory object from the
prior stage without re-reading the artifact the prior stage claims to
have written.

────────────────────────────────────────
3. INVOCATION API
────────────────────────────────────────
Single entry point, matching `WORKFLOW-002` §2's AgentBridge binding of
the `invocation_packet`:

```
invokeChamber(invocation_packet) -> completion_packet
  where invocation_packet.chamber_id == "hyperbolic-chamber-v1"
    (WORKFLOW-002 §2, fixed value for this binding)
```

Synchronous from the caller's perspective per run (a run does not return
control to the invoking gate until it reaches a stage boundary requiring
external input — e.g. Chamber 8's Founder review — at which point it
returns a `completion_packet` with `final_stage_reached` at the last
completed stage and `verdict` reflecting the pending state, never a
partial/ambiguous return). No polling API is specified — none is needed,
since `WORKFLOW-002` §7 already establishes a run may only be cancelled
before Chamber 5, and every other stage boundary either completes or
halts with a `failure_packet`.

Precondition, enforced at the API boundary, not inside chamber logic:
`authority_packet.source_of_grant` must resolve to an actual, inspectable
`03_GATE_SELECTION.md` output or Founder disposition record
(`WORKFLOW-002` §1) — the invocation API rejects any call lacking this,
before Chamber 1 ever runs.

────────────────────────────────────────
4. PERSISTENCE REQUIREMENTS
────────────────────────────────────────
Reuses, rather than duplicates, the durable-evidence-store convention
`runtime/agentbridge/` already established for the kernel track (PC-
000001 through PC-000005): `events.jsonl` (append-only), `proof-chain-
index.jsonl`, `witnesses/`, `executions/`, `proposals/`,
`reconciliations/`. Proposed, separated location — kept distinct from
kernel-track evidence to preserve Track K/Track C independence (per
`IMPLEMENTATION-TRACK-COORDINATION.md` §3–§4):

```
runtime/agentbridge/hyperbolic-chamber/
  events.jsonl                 (append-only, one line per evidence_packet
                                 or failure_packet emitted)
  proof-chain-index.jsonl      (one entry per completed chamber run)
  witnesses/<run_id>.lock
  executions/<run_id>.lock
  proposals/<run_id>.json      (the invocation_packet as submitted)
  reconciliations/<run_id>.lock
```

`<run_id>` format and generation rule are an Implementation-stage
decision (§9 item 4), not fixed here — this section specifies the
directory shape and append-only/durability requirement, not the ID
scheme.

Required invariant, restated from `WORKFLOW-001` §B: "every run must
produce a durable record containing, at minimum, the full sequence of
evidence_packets/failure_packets and the completion_packet" — no
in-memory-only run is a lawful run.

────────────────────────────────────────
5. EVIDENCE EMISSION
────────────────────────────────────────
Every `evidence_packet` must satisfy `05_VERIFICATION.md`'s existing
epistemic pipeline before being accepted as emitted, not merely produced:

```
Artifact presence -> interpretation validity -> referent validity ->
temporal index
```

Concretely: `output_artifact_ref` (`WORKFLOW-001` §A) must point to a
file that (a) exists at emission time, (b) is parsed using the schema
its own stage declares, (c) actually supports the claim the stage makes
about it, (d) carries a `witnessed_at` timestamp current to this run, not
reused from a prior run. A packet failing any of these is
`PROPOSITION_INFLATION` (`05_VERIFICATION.md`'s own naming) and must be
rejected at emission, not accepted and flagged later.

────────────────────────────────────────
6. FAILURE SEMANTICS
────────────────────────────────────────
Implements `WORKFLOW-002` §8 directly — no new vocabulary:
`failure_packet.classification` is exactly one of `HOLD`,
`CHANGES_REQUIRED`, `FAILED`, `REJECT` (the last reserved for Chamber 8
only). The invocation API surfaces a `failure_packet` to the caller
verbatim; it does not translate, retry, or reinterpret it. A stage that
emits `failure_packet` halts the run at that stage — per Gate 3's own
"lawful stopping" rule, this is a valid outcome, not an implementation
defect, and the implementation must not treat it as one (e.g., no
automatic retry-and-suppress logic).

────────────────────────────────────────
7. RECOVERY SEMANTICS
────────────────────────────────────────
A run that stops without reaching a `completion_packet` — process crash,
environment interruption — is neither `FAILED` nor silently resumable.
Per `02_SYNCHRONIZATION.md`'s own reality-reconciliation method, applied
here rather than inventing a parallel one: recovery re-derives the run's
actual last-completed stage from `runtime/agentbridge/hyperbolic-
chamber/events.jsonl` directly (never from an in-memory or claimed
state), and:
- if the last durable event is a completed `evidence_packet` with no
  following `failure_packet` or `completion_packet`, the run is
  `INCOMPLETE` — a fresh invocation may resume from the next stage only
  if a fresh `invocation_packet` is issued citing the same
  `authorized_mutation_boundary` (no widening, per `WORKFLOW-001` §B);
- Chamber 5 (Execution) recovery is stricter: per `WORKFLOW-001` §B,
  concurrent execution is a forbidden state — an `INCOMPLETE` run halted
  mid-Chamber-5 must not be silently resumed; it requires fresh
  `02_SYNCHRONIZATION.md`-style inspection of whatever partial `PATCH`
  state exists on disk before any further mutation is attempted, exactly
  as this repository already requires for any other mid-flight mutation.

────────────────────────────────────────
8. TEST ACCEPTANCE CRITERIA
────────────────────────────────────────
Reuses `SR-EXEC-001`'s own established adversarial-test shape (positive
+ negative + cold review) rather than inventing a new test philosophy:
- **Positive**: one full 8-stage run at each `COGNITIVE_PRESSURE` level
  0–5 (per Gate 3 §4), each producing a valid `completion_packet`; one
  run per forbidden-state category (§6/§7 above) confirming correct
  `failure_packet`/`HOLD` production instead of silent success.
- **Negative**: invocation missing `authority_packet.source_of_grant`
  (rejected before Chamber 1); two concurrent Chamber-5 executions
  attempted within one run (rejected, forbidden state); a stage re-run
  attempted for a `stage` value already present in the run's evidence
  sequence (rejected, forbidden state — `WORKFLOW-001` §B); a Chamber
  8 completion claiming `READY_FOR_COMMIT` with no
  `founder_packet_ref` (rejected by construction).
- **Cold-process verification**: per `05_VERIFICATION.md`'s own
  standard, a fresh process/session, not the implementing session,
  re-checks a completed run's evidence trail end-to-end before this
  contract's own implementation may be considered verified.
- **Regression**: re-run of every positive/negative case above after
  any subsequent change to this module, per `05_VERIFICATION.md`'s
  "targeted tests, then full regression suite" requirement.

────────────────────────────────────────
9. IMPLEMENTATION PREREQUISITES
────────────────────────────────────────
Carried forward from `GATE-4` §4, restated precisely for this document,
none satisfied by producing this specification:
1. **Gate 3's own disposition** — still open (readiness assessment B4;
   `GATE-4` §4 item 1). Implementation against an un-ratified design
   remains a disclosed, accepted-so-far risk (§0), not a resolved one.
2. **Resolution of Gate 3/WORKFLOW-002's genuinely open parameters**
   (reviewer counts, `CLEARED` thresholds, disagreement-adjudication
   rule) — required before Chamber 7 (Cold Chamber) can be implemented
   at any `COGNITIVE_PRESSURE` level requiring more than one reviewer.
3. **This document's own Founder disposition** — required before any
   Implementation-stage gate may cite it as authorized ground, per
   `04_GATE_EXECUTION.md`'s "no stage implies the next."
4. **Inspection of the actual control-plane repository**
   (`systems/ourself-agent-bridge`) — this document's §1 boundary and
   §2's language-agnostic interface are proposals; confirming or
   correcting them against real code requires reading that repository,
   explicitly not performed under this gate's read restriction.
5. **The Implementation-stage gate itself** — per
   `04_GATE_EXECUTION.md`'s lifecycle, this document completes Design;
   Implementation, Regression, Production Proof, Cold Verification,
   Stabilization, and Authority Expansion each require their own
   separate, explicit signal.

────────────────────────────────────────
10. EXPLICIT NON-GOALS
────────────────────────────────────────
- No runtime code, in any language, is written by this document.
- No routing, scheduler, or planner integration is specified beyond the
  invocation API's own boundary (§3) — how any specific AgentBridge gate
  decides to call `invokeChamber` is that gate's own concern, out of
  scope here.
- No execution engine is built or selected.
- No activation of any kind occurs.
- No resolution of Gate 3's own open parameters (§9 item 2) is attempted
  — naming them as prerequisites is not the same as resolving them, and
  this document does not conflate the two.
- No change to `WORKFLOW-001`, `WORKFLOW-002`, `GATE-4`, or Gate 3's own
  content.
- No claim that this contract, once ratified, makes implementation
  eligible to begin immediately — §9 lists what remains, precisely so
  that ratifying this document is never mistaken for satisfying items
  1, 2, 4, or 5 above.
