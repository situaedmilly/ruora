# GATE 4 — HYPERBOLIC CHAMBER BINDING DECISION

STATUS: DISPOSITIONED (2026-07-30) — BOUND. See
  decisions/ratified/FOUNDER-DISPOSITION-006-GATE-4-WITNESS.md for the
  constitutional record.
CLASSIFICATION: ARCHITECTURAL_BINDING_DECISION (per
  `GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md` §8: "Gate 4+ —
  'Evaluate whether SELFREALIZATION should invoke the chamber before
  runtime' — is where binding, integration, and the open questions...
  get resolved.")
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE — no runtime implementation, no routing change,
  no chamber activation authorized by this document.
NAMING: `GATE-4`, per
  `IMPLEMENTATION-TRACK-COORDINATION.md` §6 — continuing Gate 3's own
  forward reference ("Gate 4+"), not `WORKFLOW-003` (WORKFLOW-002's
  independently-introduced, now cross-collided identifier). This is the
  first document in Track C to use the resolved naming.

DEPENDENCY: Gate 3's two stated preconditions (Founder ratification of
  F-01/F-02/F-04; SR-EXEC-001 executed and disposed) were both satisfied
  before this gate opened — `FOUNDER-DISPOSITION-001` and
  `FOUNDER-DISPOSITION-002` respectively. `WORKFLOW-001` and
  `WORKFLOW-002` (the Design-stage packet/invocation contracts this
  binding decision activates) are both independently ratified —
  `FOUNDER-DISPOSITION-003` and `FOUNDER-DISPOSITION-004`.

────────────────────────────────────────
1. THE CONSTITUTIONAL BINDING DECISION
────────────────────────────────────────
**AgentBridge SHALL bind to the Hyperbolic Chamber as an architectural
component.**

This decision was made directly by the Founder, in this conversation,
via an explicit, unhedged, single selection among three stated
alternatives (YES — bind / NO — do not bind / DEFER), each alternative's
exact consequence stated in advance before the selection was made — the
same authentication mechanism disclosed for
`FOUNDER-DISPOSITION-005`. See §Authentication Disclosure in the
accompanying Founder Disposition record for the full disclosure.

This decision resolves the "whether" question `GATE-3` §8 named as
belonging to "Gate 4+" and that `WORKFLOW-001`/`WORKFLOW-002` both
independently held open pending "its own explicit, unhedged Founder
statement." It is made now, for the first time, as a file-anchored
constitutional act. A prior, informal indication is recorded in
`FOUNDER-DISPOSITION-003`'s own text ("Binding Decision: Yes [as
architectural direction, not implementation authorization]," attributed
to an earlier conversation) — that record explicitly declined to treat
its own mention as a constitutional act ("not restated as law here since
it is a direction, not itself a constitutional act on any file"). This
document does not rely on that prior mention as its own evidentiary
basis; it stands on the fresh, direct statement obtained in this
conversation.

────────────────────────────────────────
2. SCOPE OF THE BINDING
────────────────────────────────────────
The binding is exactly, and only, what `WORKFLOW-001` and `WORKFLOW-002`
already specify — this decision activates their already-ratified
contracts; it does not add to, narrow, or reinterpret them:

- **Per-invocation, never standing.** Per `WORKFLOW-002` §1: "Invocation
  authority is per-run, not standing. Each invocation requires its own
  fresh `invocation_packet`; no session or role retains authority to
  invoke a second run from a prior grant." Binding AgentBridge to the
  chamber architecturally does not grant any specific future gate
  authority to invoke it — each invocation remains its own, separately
  authorized act.
- **Design-stage only.** Per `WORKFLOW-002` §3: a chamber run, if
  invoked, "completes entirely within 'Design' — it never spans into or
  triggers Implementation, Regression, or Production Proof." This
  binding does not extend the chamber's reach beyond that.
- **Selected, not defaulted.** `cognitive_pressure` level and the
  decision to invoke at all are selected "by whichever party holds the
  Gate Selection authority for the invoking gate — not by the chamber
  itself, and not by the role requesting invocation" (`WORKFLOW-002` §2).
  No gate is bound to use the chamber by default as a consequence of
  this decision.
- **Authority is never self-granted.** Per `WORKFLOW-002` §1, any future
  invocation's `authority_packet.source_of_grant` must point to "a
  specific Gate Selection output ... or a specific Founder disposition —
  never a self-declared grant." This decision does not itself function
  as a standing source of grant for any specific future invocation.

────────────────────────────────────────
3. EXPLICIT EXCLUSIONS
────────────────────────────────────────
This decision does NOT:
- ratify `GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md`'s own
  chamber-protocol content (the 8-stage shape, `COGNITIVE_PRESSURE`
  level definitions). Gate 3 itself remains `STATUS: PARKED`,
  un-dispositioned, exactly as before — every prior Founder Disposition
  in this corpus (FD-001, -002, -003, -004) explicitly excluded
  ratifying Gate 3, and this one does too. Binding AgentBridge to "the
  chamber" as an architectural direction is a distinct act from
  certifying the chamber's own internal design as constitutional law;
  the latter remains open (readiness assessment B4).
- implement any runtime code, routing change, scheduler/planner change,
  or execution engine work;
- activate the chamber for any specific gate, present or future — no
  invocation occurs as a result of this decision;
- resolve Gate 3's own genuinely open items, restated as open by
  `WORKFLOW-002`'s own "GENUINE OPEN ITEMS" section: exact
  `required_reviewer_count` per `COGNITIVE_PRESSURE` level, the
  numeric/structural definition of `CLEARED` per level, or the
  disagreement-adjudication rule (unanimous / majority / escalation).
  These remain `NOT_YET_SPECIFIED`, unchanged by this act;
- authorize `WORKFLOW-003`-in-the-Track-C-sense (the implementation-
  stage gate `WORKFLOW-002`'s own text once anticipated under that
  name) — per `IMPLEMENTATION-TRACK-COORDINATION.md` §6, that
  identifier is retired for Track C; any future implementation-stage
  gate in this track uses the `GATE-N` scheme (the next being `GATE-5`,
  if and when opened);
- edit any doctrine file, any file in `governance/agentbridge/workflow/`,
  or any schema;
- authorize staging, commit, push, publication, deployment, or release.

────────────────────────────────────────
4. IMPLEMENTATION PREREQUISITES (what must still happen before any
   chamber code exists)
────────────────────────────────────────
In dependency order, all still open after this decision:
1. **Gate 3's own disposition** (readiness assessment B4) — the
   chamber-protocol design itself should receive its own Founder
   Disposition before implementation proceeds against it, since no
   existing ratification covers its content, only documents built on top
   of it.
2. **Resolution of the three genuinely open items** named in §3 above
   (reviewer counts, `CLEARED` thresholds, disagreement adjudication) —
   required before any `COGNITIVE_PRESSURE` Level 2+ run could actually
   execute with reviewers, per `WORKFLOW-002` §4–§6's own interface
   definitions (interfaces only; no values specified).
3. **A new, `GATE-N`-named Implementation-stage gate** (per
   `04_GATE_EXECUTION.md`'s lifecycle: Design → **Implementation** →
   Regression → Production Proof → Cold Verification → Stabilization →
   Authority Expansion) — this decision only completes Track C's Design
   stage; per `04_GATE_EXECUTION.md`'s own rule, "Completing Design does
   not authorize Implementation," restated here rather than assumed
   overridden by this binding decision's own significance.
4. **A per-invocation authorization** for whichever specific future gate
   first actually invokes the chamber — this binding decision is not
   that authorization; §2 above states this precisely.

────────────────────────────────────────
EXPLICITLY OUT OF SCOPE FOR THIS DOCUMENT
────────────────────────────────────────
No implementation of any kind. No runtime change. No doctrine edit. No
ratification of Gate 3's own content. No resolution of Gate 3's open
parameters. No specific gate's chamber invocation.
