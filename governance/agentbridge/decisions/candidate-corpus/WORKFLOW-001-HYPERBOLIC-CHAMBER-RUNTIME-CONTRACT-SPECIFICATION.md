# WORKFLOW-001 — HYPERBOLIC CHAMBER RUNTIME CONTRACT
## Canonical Specification

STATUS: PARKED
CLASSIFICATION: ARCHITECTURAL_DESIGN_CANDIDATE (Design stage only, per
  `governance/agentbridge/workflow/04_GATE_EXECUTION.md`'s lifecycle:
  Design → Implementation → Regression → Production Proof → Cold
  Verification → Stabilization → Authority Expansion)
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE
SCOPE: SPECIFICATION_ONLY — no runtime behavior, no AgentBridge
  integration, no execution hooks, no code.

DEPENDENCY: Workflow 002 (or any implementation of what this document
  specifies) cannot begin until this document receives its own Founder
  disposition. That disposition, if granted, ratifies this contract's
  *content* — it does not, by itself or as a side effect, decide whether
  any system (AgentBridge or otherwise) invokes the Hyperbolic Chamber.
  That is a separate, still-open, still-undecided question. See
  "What this document does not decide," below.

────────────────────────────────────────
WHAT THIS DOCUMENT DOES NOT DECIDE
────────────────────────────────────────
Gate 3 (`GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md`) drew an
explicit line between two future decisions: *whether* SELFREALIZATION or
any other system should invoke the chamber at all, and *how* it would be
invoked if so (§8: "Gate 4+ ... 'Evaluate whether SELFREALIZATION should
invoke the chamber before runtime' — is where binding, integration, and
the open questions... get resolved"). That "whether" question has not
been decided. It is not decided by this document either.

What this document does: continues Gate 3's own already-acknowledged
open work — the "per-level parameters that must be pinned before this is
implementable" it named in its §4, and a fuller elaboration of the
"common input contract" and stage-output artifacts it sketched in its §3
— at the same UNIVERSAL, domain-agnostic level Gate 3 itself operated at
(§5: "Universal... belongs in the chamber protocol itself, reusable
across every OURSELF system"). It does not bind this contract to
AgentBridge, SELFREALIZATION, or any other specific system. Per
`04_GATE_EXECUTION.md`'s already-ratified rule, "Completing Design does
not authorize Implementation" — producing this Design-stage artifact,
even if later disposed as APPROVED, authorizes nothing beyond itself.

────────────────────────────────────────
A. RUNTIME CONTRACT — PACKET DEFINITIONS
────────────────────────────────────────
Every packet below is a data shape only — field names, types, and
meaning. None of these fields are populated, transmitted, or acted upon
by this document; there is no code here, only a contract a future,
separately-authorized Implementation stage could conform to.

**invocation_packet** (what starts a chamber run):
  - `chamber_id`: string — which chamber protocol version is invoked.
  - `cognitive_pressure`: enum [0,1,2,3,4,5] — per Gate 3 §4's LEVEL
    definitions (Routine..Founder).
  - `raw_task`: string — the task text, for Chamber 1 only.
  - `authorized_mutation_boundary`: string_list — files/targets the
    whole run may ever touch. Set once here; per Gate 3 §3, "never
    widened mid-run."
  - `requesting_identity`: string — who/what invoked this run. Per Gate
    3 §6, invocation itself grants no authority — this field is
    provenance, not a grant.

**context_packet** (carried into Chamber 1, Reality Synchronization):
  - `witnessed_environment`: object — repository, branch, HEAD, working
    tree state, as actually observed, not recalled.
  - `witnessed_at`: string (date-time) — per this repo's existing
    `unknown_or_string`/`witnessed_at` convention in
    `03_SELFREALIZATION_SCHEMA.yaml`, timestamp of live witness, not of
    memory recall.

**authority_packet** (what the run is and is not permitted to do):
  - `granted_dimensions`: object — explicit, per this repo's existing
    `authority_grant` convention (GRANTED/DENIED, no implicit default,
    absence is invalid not a silent denial).
  - `source_of_grant`: string — which role constitution / disposition
    record the grant traces to. A chamber run cannot self-grant; per
    Gate 3 §6, "This chamber protocol grants no authority... Mutation
    authority still comes from the role constitutions and SELFREALIZATION
    schema."

**writable_boundary** / **repository_boundary**:
  - Both `string_list`, identical in shape to
    `environment.writable_boundaries` / `environment.read_only_boundaries`
    already defined in `03_SELFREALIZATION_SCHEMA.yaml` — this contract
    reuses that existing vocabulary rather than inventing a parallel one.

**evidence_packet** (per-stage, emitted by every chamber stage):
  - `stage`: enum [1..8] matching Gate 3 §3's eight named stages.
  - `output_artifact_ref`: string — pointer to the actual disk artifact
    (REALITY_LOCKED, CANONICAL_MODEL, ... FOUNDER_PACKET). Per Gate 3
    §3, "independently re-derivable from disk state, not carried forward
    as an assertion."
  - `reviewer_identities`: string_list — populated only at
    COGNITIVE_PRESSURE levels that require independent review (Gate 3
    §4, Levels 2+).

**failure_packet** (emitted when a stage cannot produce its output):
  - `stage`: enum [1..8].
  - `reason`: string.
  - `classification`: enum [BLOCKING, NOT_SATISFIED, HOLD] — reusing
    this repo's existing disposition vocabulary
    (`READY_FOR_FOUNDER_RATIFICATION_REVIEW` / `CHANGES_REQUIRED` /
    `HOLD` / `FAILED` from SR-EXEC-001's own required-output section)
    rather than inventing new terms.
  - Per Gate 3's own rule, a stage stopping honestly is a lawful outcome:
    a failure_packet is not itself an error condition to be suppressed.

**completion_packet**:
  - `final_stage_reached`: enum [1..8].
  - `verdict`: enum matching this repo's existing verdict vocabulary.
  - `founder_packet_ref`: string, required only if stage 8 was reached.

────────────────────────────────────────
B. EXECUTION CONTRACT
────────────────────────────────────────
Inputs: invocation_packet + context_packet, per stage 1.
Outputs: one evidence_packet per completed stage, or one failure_packet
  at the stage where the run stopped, plus one completion_packet.

Required invariants (carried forward from Gate 3 §3/§6, not modified):
  - Later stages re-derive from disk; they do not trust a prior stage's
    assertion.
  - Chamber 5 (Execution) is always a single mutator; concurrent
    execution within one run is a forbidden state (below).
  - Chamber 8 (Founder) never auto-approves; a completion_packet with
    `final_stage_reached: 8` and no human-attributable
    `founder_packet_ref` is invalid by construction.
  - A chamber run cannot grant itself a higher `cognitive_pressure`
    level's authority retroactively — level escalation requires a fresh
    invocation_packet at the higher level.

Forbidden states:
  - Two evidence_packets for the same `stage` value within one run
    (re-running a stage silently, rather than a fresh invocation).
  - A completion_packet with `verdict: REALIZED`-equivalent and any
    open failure_packet in the same run.
  - `authorized_mutation_boundary` widened after invocation_packet is
    issued (Gate 3 §3's "never widened mid-run," now stated as a
    machine-checkable forbidden state rather than prose only).

Required witness: every run must produce a durable record containing, at
  minimum, the full sequence of evidence_packets/failure_packets and the
  completion_packet — the same "no orphaned assertions" standard already
  applied throughout this repo's other witness documents this session.

────────────────────────────────────────
C. BOUNDARY CONTRACT — WHAT A FUTURE WORKFLOW 002 MAY / MAY NOT DO
────────────────────────────────────────
IF a future Workflow 002 is separately authorized, it may:
  - Bind the packet shapes above to one specific system's concrete
    values (e.g., what `witnessed_environment` resolves to for
    AgentBridge specifically, what `output_artifact_ref` means in
    AgentBridge's own storage).
  - Define that system's own invocation point, timeout, retry, and
    escalation behavior.

A future Workflow 002 may NOT, as a consequence of this document or its
disposition alone:
  - Decide that the bound system in fact invokes the chamber — that
    "whether" decision must be separately, explicitly made before
    Workflow 002 opens, exactly as this document's DEPENDENCY section
    states.
  - Implement runtime code, routing changes, or activation — per
    `04_GATE_EXECUTION.md`'s existing rule, Design does not authorize
    Implementation regardless of how detailed the Design is.
  - Treat this document's disposition as also disposing Gate 3 itself,
    GOV-LINEAGE-001, or any other candidate artifact.

────────────────────────────────────────
D. DEPENDENCY CONTRACT
────────────────────────────────────────
Workflow 002 cannot begin until this document (Workflow 001) receives its
own Founder disposition. Disposition of this document is necessary but
not sufficient for Workflow 002 to begin — the separate binding ("whether
AgentBridge invokes the chamber") decision is an independent precondition
that this document's disposition does not satisfy, regardless of outcome.

────────────────────────────────────────
EXPLICITLY OUT OF SCOPE FOR THIS DOCUMENT
────────────────────────────────────────
- No AgentBridge routing, no runtime hooks, no code, no planner changes,
  no execution engine, no workflow dispatcher changes, no integration,
  no production activation.
- No rewrite of Gate 3 or any other existing candidate/ratified artifact.
- No doctrine edits.
- No decision on whether any system binds to this chamber.
