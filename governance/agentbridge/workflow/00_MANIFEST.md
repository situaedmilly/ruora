# 00_MANIFEST

**Document identifier:** `governance/agentbridge/workflow/00_MANIFEST.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

This document is the single entry point for the OURSELF AgentBridge governance
workflow. It is never executed. It answers, before any session begins
executing anything:

- What is this workflow?
- Which documents in this stack are normative?
- Which are generated at session time?
- Which are candidate-only and not yet ratified?
- What is the current workflow schema version?

Every fresh terminal session that intends to act on AgentBridge (kernel,
control plane, or runtime evidence) SHALL load this manifest before loading
any other workflow document.

## Authority granted

None. This document confers no inspection, mutation, or decision authority
by itself. It is descriptive and routing-only.

## Authority explicitly not granted

- This document does not authorize any gate.
- This document does not ratify any constitution.
- This document does not expand the admitted authority surface defined in
  `07_LAUNCH_ROADMAP.md`.

## Required inputs

None. This is the fixed starting point of every session.

## Required procedure

State the following, verbatim in structure, at the start of every session
that touches AgentBridge:

1. **Workflow identity and version** — `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`,
   status `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`.
2. **Canonical entry point** — `01_SESSION_BOOTSTRAP.md`.
3. **Exact execution order**:

   ```
   01_SESSION_BOOTSTRAP
     → 02_SYNCHRONIZATION
     → 03_GATE_SELECTION
     → 04_GATE_EXECUTION
     → 05_VERIFICATION
     → 06_SEAL_OR_HOLD
     → 07_LAUNCH_ROADMAP
     → STOP
   ```

   No document in this order may be skipped. No document may be executed
   out of order. A session may stop at any document boundary; it may not
   jump ahead.

4. **Signal taxonomy** — every instruction issued to or by a session carries
   exactly one of the following signal classes:

   - `STOP_SIGNAL`
   - `AUTHORITY_SIGNAL`
   - `OPERATING_SIGNAL`
   - `OBJECTIVE_SIGNAL`
   - `INSPECTION_SIGNAL`
   - `MUTATION_SIGNAL`
   - `VERIFICATION_SIGNAL`
   - `SEAL_SIGNAL`
   - `FOUNDATION_SIGNAL`
   - `DECISION_SIGNAL`
   - `DESIGN_SIGNAL`
   - `SYNTHESIS_SIGNAL`
   - `PUBLICATION_SIGNAL`
   - `IMPLEMENTATION_SIGNAL`
   - `PRODUCTION_PROOF_SIGNAL`
   - `STABILIZATION_SIGNAL`

   A session must be able to name which signal class it is currently acting
   under at all times. An action taken under no identifiable signal class is
   a workflow violation and forces `HOLD`.

5. **Signal non-equivalence law** — the following are never interchangeable,
   regardless of how persuasive the surrounding narrative is:

   - Analysis ≠ authorization.
   - Design ≠ implementation.
   - Verification ≠ mutation.
   - Ratification ≠ publication.
   - Publication ≠ operational adoption.
   - Seal ≠ authority expansion.

6. **Authority precedence** — this workflow is subordinate to the
   controlling repository's existing `CLAUDE.md` and any pre-existing
   workflow-signal law in that repository. Where this workflow and a
   repository's own governing document conflict, the repository's own
   governing document controls, and the conflict itself is a `HOLD`
   condition until reconciled.

7. **Candidate corpus distinction**:

   ```
   Exploration → Candidate Corpus → Ratified Doctrine
   ```

   Nothing produced during a session is doctrine merely because it was
   produced. It is exploration until captured; candidate corpus once
   captured in `decisions/candidate-corpus/`; doctrine only once moved to
   `decisions/ratified/` through an explicit ratification gate.

8. **Core doctrine**:

   > A distinction does not become doctrine because it is persuasive.
   > It becomes doctrine only after it survives a formal decision process.

## Required output

A session that loads this manifest states, before proceeding to
`01_SESSION_BOOTSTRAP.md`, that it has read and adopted the execution order,
signal taxonomy, non-equivalence law, authority precedence, and core
doctrine above.

## Refusal / HOLD conditions

- The manifest is missing, unreadable, or its schema version does not match
  the version referenced by any other loaded workflow document → `HOLD`.
- A session cannot name its current signal class → `HOLD`.
- A repository's own `CLAUDE.md` or signal law conflicts with this manifest
  → `HOLD` pending reconciliation; this manifest does not override it.

## Launch-state footer

This document carries no live launch state. Live state is produced by
`01_SESSION_BOOTSTRAP.md` (`SESSION_CONTEXT`) and `07_LAUNCH_ROADMAP.md`
(trailing roadmap). See those documents.
