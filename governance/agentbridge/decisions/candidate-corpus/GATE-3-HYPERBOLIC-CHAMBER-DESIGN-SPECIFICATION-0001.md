# GATE 3 — HYPERBOLIC CHAMBER — DESIGN SPECIFICATION

STATUS: DISPOSITIONED (2026-07-30) — APPROVED. See
  decisions/ratified/FOUNDER-DISPOSITION-008-GATE-3-WITNESS.md for the
  constitutional record.
CLASSIFICATION: ARCHITECTURAL_DESIGN_CANDIDATE
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE
SCOPE: DESIGN_ONLY — no runtime behavior, no AgentBridge integration, no execution hooks

DEPENDENCY (both must resolve before this gate may become executable):
1. Founder ratification of the completed SELFREALIZATION F-01/F-02/F-04
   role-correspondence repair (DECISION_SIGNAL
   OURSELF_SELFREALIZATION_SCHEMA_ROLE_CORRESPONDENCE_FOUNDER_RATIFICATION).
2. SR-EXEC-001 (authority.execute ceiling amendment) executed and disposed
   by the Founder.

If either dependency is unresolved, this document may be read, edited, and
discussed, but nothing described in it may be implemented, bound, or invoked
by any runtime.

────────────────────────────────────────
WHY THIS GATE IS SEQUENCED THIRD, NOT FIRST
────────────────────────────────────────
SELFREALIZATION is still mid-ratification. Inserting a new governing layer
above it before its own ratification path completes would mean changing the
foundation while it is under review — a future reviewer would not be able to
tell whether a finding belongs to SELFREALIZATION or to this chamber
abstraction. This document exists to preserve the idea while it is fresh,
not to schedule its implementation. Discovery of an architectural layer does
not obligate its activation.

Lineage this gate must preserve:

    Doctrine
        -> SELFREALIZATION
        -> (HYPERBOLIC CHAMBER specification — this document, parked)
        -> Binding decision (future gate, not this one)
        -> Implementation (future gate, not this one)

────────────────────────────────────────
1. WHAT IS A CHAMBER
────────────────────────────────────────
A chamber is a reasoning-depth protocol, not a workflow. A workflow
specifies what to do (steps, targets, order). A chamber specifies how much
uncertainty must be eliminated, and by what structural means, before a
result produced by a workflow is trusted.

The two are orthogonal. The same workflow (e.g. "amend a schema file") can
be run under different chamber intensities, producing different amounts of
independent extraction, adversarial challenge, and cold review around the
same core steps.

────────────────────────────────────────
2. WHAT PROBLEM THIS SOLVES
────────────────────────────────────────
Today, rigor is set per-task, ad hoc, inside each amendment gate's own text
(e.g. SR-EXEC-001 hand-specifies precondition witness, independent
extraction, adversarial verification, cold review, Founder packet — all
authored inline, every time). That produces:

- inconsistent rigor across OURSELF systems (AgentBridge, SELFQuant, UREEL,
  FREED SELF, AEXIOM, Momentum each reinvent their own verification depth);
- no shared vocabulary for "how hard did we try to be wrong here";
- no way to dial rigor up or down without rewriting the gate's prose.

A chamber, invoked once per gate/mutation and referenced rather than
re-authored, would let any OURSELF system declare an intensity level and
inherit a known reasoning-density protocol.

────────────────────────────────────────
3. INPUTS AND OUTPUTS (per chamber stage)
────────────────────────────────────────
Common input contract, every stage:
- prior stage's output artifact (or, for Chamber 1, the raw task)
- COGNITIVE_PRESSURE level (see section 4) — governs stage parameters
- authorized mutation boundary (files/targets the whole chamber run may
  ever touch — set once, upstream, never widened mid-run)

Stage outputs (each a named, inspectable artifact — not a verdict alone):

  Chamber 1  Reality Synchronization   -> REALITY_LOCKED
  Chamber 2  Independent Extraction    -> CANONICAL_MODEL
  Chamber 3  Adversarial Chamber       -> SURVIVING_INVARIANTS
  Chamber 4  Synthesis Chamber         -> AMENDMENT_PLAN
  Chamber 5  Execution Chamber         -> PATCH
  Chamber 6  Verification Chamber      -> VERIFIED_PATCH
  Chamber 7  Cold Chamber              -> COLD_VERDICT
  Chamber 8  Founder Chamber           -> FOUNDER_PACKET

Each artifact must be independently re-derivable from disk state, not
carried forward as an assertion — a later stage does not get to say "trust
the earlier stage's conclusion," it re-reads.

────────────────────────────────────────
4. HOW CHAMBER INTENSITY AFFECTS WORKFLOW RIGOR
────────────────────────────────────────
COGNITIVE_PRESSURE is a single dial. It parameterizes the stages above; it
does not change their order or add/remove stages.

  LEVEL 0  Routine     1 extraction path, no adversarial pass, no cold review
  LEVEL 1  Focused      2 extraction paths, light adversarial pass
  LEVEL 2  Deep         independent extraction + full adversarial pass,
                         1 verification reviewer, no cold chamber
  LEVEL 3  Hyperbolic   full 8-chamber run, N independent extraction paths,
                         adversarial falsification across all listed
                         categories, 1 cold reviewer
  LEVEL 4  Cathedral    LEVEL 3 + multiple independent verification
                         reviewers + multiple cold reviewers, lower
                         acceptable-uncertainty threshold
  LEVEL 5  Founder      LEVEL 4 + mandatory Founder Chamber synthesis;
                         cannot self-ratify at any level below this one

Per-level parameters that must be pinned before this is implementable
(open questions, not yet answered by this document):
- exact reviewer counts and how disagreement among them resolves;
- what "acceptable uncertainty threshold" means numerically or structurally,
  and how a chamber run reports that it failed to clear its own threshold;
- whether level selection is fixed per gate class or chosen per-invocation,
  and by whom.

────────────────────────────────────────
5. UNIVERSAL VS IMPLEMENTATION-SPECIFIC
────────────────────────────────────────
Universal (belongs in the chamber protocol itself, reusable across every
OURSELF system):
- the 8-stage shape and its artifact contract;
- the COGNITIVE_PRESSURE level definitions and what each dials;
- the rule that later stages re-derive from disk rather than trust prior
  conclusions;
- the rule that Execution (Chamber 5) is always a single mutator, never
  concurrent;
- the rule that Founder Chamber never silently ratifies.

Implementation-specific (belongs to whatever system binds the chamber —
AgentBridge, SELFQuant, UREEL, etc. — and is explicitly out of scope for
this document):
- what "repository," "authority," and "writable boundary" resolve to in
  Chamber 1 for a given system;
- what counts as an "extraction path" for a given domain (schema fields for
  a governance amendment vs. price-state layers for SELFQuant);
- how PATCH is represented and applied (git diff, SQL migration, config
  write, trade order — domain-defined);
- how FOUNDER_PACKET is delivered (this repo's existing decision-brief /
  human-decision file pattern, a Slack message, etc.).

────────────────────────────────────────
6. CONSTITUTIONAL BOUNDARIES
────────────────────────────────────────
- This chamber protocol grants no authority. It is a reasoning-density
  contract, not an authorization mechanism. A chamber run at any level
  produces a recommendation/artifact chain; it does not itself authorize
  mutation. Mutation authority still comes from the role constitutions and
  SELFREALIZATION schema (and, once resolved, SR-EXEC-001's execute-ceiling
  rules).
- A chamber must not be able to grant itself a higher COGNITIVE_PRESSURE
  level's authority by claiming a lower one ran adequately — level
  escalation requires a fresh run at the higher level, not a relabeling of
  an existing artifact chain.
- Chamber 8 (Founder Chamber) can never be skipped for LEVEL 5 work and can
  never auto-approve; "never silently ratify" is a hard constraint on the
  protocol itself, not a per-implementation choice.
- Binding this chamber above SELFREALIZATION (per the lineage diagram in
  section "why this gate is sequenced third") is itself a future decision,
  not a conclusion of this document. This document only asserts that *if*
  bound, it sits above SELFREALIZATION and below nothing already ratified.

────────────────────────────────────────
7. EXPLICITLY OUT OF SCOPE FOR THIS GATE
────────────────────────────────────────
- No AgentBridge integration or code.
- No runtime execution hooks.
- No binding decision about whether SELFREALIZATION invokes this chamber.
- No concrete reviewer-count defaults, threshold math, or level-selection
  authority — flagged above as open questions for the future binding gate.
- No staging, commit beyond this document, push, or publication of anything
  other than this design-only file.

────────────────────────────────────────
8. NEXT GATE (NOT THIS ONE)
────────────────────────────────────────
Gate 4+ — "Evaluate whether SELFREALIZATION should invoke the chamber
before runtime" — is where binding, integration, and the open questions in
section 4/5 get resolved. It does not become eligible until both
dependencies listed at the top of this document are cleared by the Founder.
