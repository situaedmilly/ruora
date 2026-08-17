# AUTHORITY APPLICABILITY PROVENANCE SUITE
# SEMANTIC RECONCILIATION 001 · BOUNDED REPAIR 007

AUTHORIZE: AUTHORIZE_SELFIR_VISIBILITY_STOP_RULE_PRECEDENCE_AND_TEMPORAL_REPAIR_007_ONLY

RUNTIME: CODEXSELF / SELFIR

SESSION CLASS: BOUNDED_SEMANTIC_REPAIR

SESSION REQUIREMENT:

Fresh Repair Session
RepairSession != PriorReviewerSession
Review != Repair
Repair != Adoption
Repair != Ratification

SOURCE INPUT CONTEXT (as provided into this repair gate):

- AUTHORITATIVE predecessor repair: `BOUNDED_REPAIR_006`
- SOURCE REVIEW: `BOUNDED_REPAIR_006_INDEPENDENT_HOSTILE_REVIEW_001` (session-level hostile review result used as residual input)
- Current SOURCE REVIEW outcome: `CHANGES_REQUIRED`
- Prior standing of this repair candidate: `BOUNDED_REPAIR_CANDIDATE / NONCANONICAL / NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR / NOT_ADOPTED / NOT_RATIFIED`
- SOURCE review residuals preserved at entry:
  - R5-01
  - R5-02
  - R5-03
- New residual compression for Repair 007:
  - `R7_01`: visibility-completeness + dependency-visibility meta-grounding
  - `R7_02`: stop-rule + terminal claim applicability
  - `R7_03`: precedence-policy conflict handling
  - `R7_04`: historical-vs-current standing lifecycle (non-retroactive)

## 1) TARGET INTEGRITY WITNESS (Pre-Repair)

Target branch/workspace:
- Repository root: `/Users/millysituated/RUORA-worktrees/authority-applicability-provenance-suite-bounded-repair-003`
- Branch: `agent/authority-provenance-bounded-repair-003`
- Pre-repair HEAD: `ddf4dc67a302f34e5c9df90ec33d9c345de4617e`
- Remote: `github` (`git@github.com:situaedmilly/ruora.git`)
- Artifact predecessor path: `governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_006.md`
- Branch already clean at invocation: verified

Authorized predecessor artifact:

- `AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_006.md`
- Commit expected in chain: `ddf4dc67a302f34e5c9df90ec33d9c345de4617e`

## 2) TOP-LEVEL REPAIR SCOPE (R7 only)

This repair is explicitly authorized only for:

- `R7_01 — DEPENDENCY_VISIBILITY_META_GROUNDING`
- `R7_02 — STOP_RULE_AND_TERMINAL_APPLICABILITY`
- `R7_03 — PRECEDENCE_POLICY_CONFLICT_RESOLUTION`
- `R7_04 — NON_RETROACTIVE_STANDING_LIFECYCLE`

No scope widening permitted toward:

- `R1` through `R6`
- `IHR-B01` … `IHR-B10`
- Gene / Foundation IR
- DATASELF
- AgentBridge
- Notepad
- implementation
- schema
- runtime

## 3) PRIME LAW OF REPAIR 007

Repair 007 targets the deeper theorem that bounded closure itself can be under-grounded.

Core non-collapse invariants:

1. `KnownEdgeVocabulary != CompleteApplicableEdgeClasses`
2. `VisibilityAssessment != VisibilityCompletenessProof`
3. `NoCycleFound != CycleAbsent`
4. `StopRuleExists != StopRuleAdmissible`
5. `TerminalSourceStanding != TerminalSourceApplicableToClaim`
6. `StandingPrecedencePolicyA + StandingPrecedencePolicyB != DeterminatePrecedence`
7. `ReauthorizationAt(t4) != RetroactiveValidationOf(t2,t3)`

Required distinction:

`DependencyVisibilityCompleteRelativeTo(claim_scope, governance_boundary, policy_epoch, registry_set)`
does **not** mean global, absolute visibility.

Allowed entailment:

`NO_CYCLE_WITHIN_GROUNDED_VISIBILITY`

does **not** entitle:

`GLOBAL_A_CYCLICITY`

Visibility failures produce bounded outcomes:

- `ANCESTRY_VISIBILITY_INCOMPLETE`
- `STOP_RULE_INADEQUATE`
- `TERMINAL_SCOPE_MISMATCH`

And any such unresolved state maps to `NOT_EVALUABLE`, not inferred global independence.

Conclusion ceiling law remains:

`ConclusionScope <= GroundingScope`

## 4) REPAIR SURFACE R7-01: DEPENDENCY VISIBILITY META-GROUNDING

### Source bundle

- ACR-06
- ACR-07
- ACR-09
- ACR-10
- ACR-20

### Finding

The dependency graph used for standing ancestry can be complete for observed edges but still miss lawful edge classes required for the claim scope.

### Root defect

Repair 006 introduced `CausalBootstrapNotEstablishedUnderGroundedVisibility`, but did not fully close the epistemic condition:

> what proves the dependency discovery mechanism has discovered all relevant edges.

This allows false confidence in graph exhaustiveness.

### Countermodels attacked

- F1: truncated edge set hides relevant standing edge.
- F4: separate local graphs appear acyclic while union is cyclic.

### Repair

Introduce explicit bounded meta-grounding of visibility:

- `DependencyVocabularyRecord(C, K)`
- `EdgeClassMap(C, K)`
- `EdgeDiscoveryBoundary(K)`
- `DependencyVisibilityCompletenessAssessment`
- `VisibilityCompletenessConfidence`
- `StandingDependencyCoverageAssessment`

where `C` is the claim class and `K = (jurisdiction, scope, policy_epoch, registry_set, governance_boundary, standing_version)`.

Require each standing ancestry check to include:

- `CandidateClaimScope` declaration
- `ApplicableEdgeVocabulary` declaration
- `CoverageEvidence` for edge classes relevant to that vocabulary
- `EdgeCompletenessDecision` explaining any omissions and the admissibility of the omission
- `InterRuntimeVisibilityUnion` for cross-runtime traces when applicable

`NoCycleFound` is only valid as `NO_CYCLE_WITHIN_GROUNDED_VISIBILITY` if `DependencyVisibilityCompletenessAssessment` is `COMPLETED`.

If completeness cannot be lawfully proven:

`ANCESTRY_VISIBILITY_INCOMPLETE`.

### New objects / relations

- `DependencyVisibilityBoundary`
- `DependencyVocabularyStandingAssessment`
- `EdgeClassCoverageRecord`
- `CrossRuntimeVisibilityConfluenceRecord`
- `VisibilityUnionProvenanceTrail`

### Why previous countermodel fails

Hidden edges now invalidate the claim that required edge classes are lawfully covered. A cyclic or open-chain that requires an undiscovered edge is no longer converted into local non-bootstrap; it remains unresolved until coverage is lawful.

### Status

`AUTHOR_CLAIMS_REPAIRED` / `UNRESOLVED` (candidate)

## 5) REPAIR SURFACE R7-02: STOP-RULE & TERMINAL APPLICABILITY

### Source bundle

- ACR-08
- ACR-11

### Finding

Terminal stopping is not just about having any standing source; it must be admissible for the exact claim context.

### Root defect

A `StopRule` may be standing in one context but irrelevant to the claim being grounded. Repair 006 still risks treating admissible stop rules as universally claim-applicable.

### Countermodel

- A standing stop rule for claim class `C1` is reused for claim class `C2` with no contextual compatibility check.

### Repair

Split terminal admissibility into explicit context:

- `StopRuleStandingValid(SR, K)`
- `StopRuleApplicableToClaim(SR, C, K)`
- `TerminalSourceStandingValid(S, K)`
- `TerminalSourceApplicableToClaim(S, C, K)`
- `StoppingRuleStandingSourceNonBootstrap(SR, C, K)`

Require terminal admission only under conjunction:

`TerminalSourceAdmissible(S, C, K) :=`
- `SourceStanding(S, K)=VALID`
- `StopRuleStandingValid(SR, K)=VALID`
- `StopRuleApplicableToClaim(SR, C, K)=TRUE`
- `TerminalSourceApplicableToClaim(S, C, K)=TRUE`
- `NoUnresolvedRequiredDependency(S, C, K)`
- `CausalBootstrapNotEstablishedUnderGroundedVisibility(S, C, K)=TRUE`
- `JurisdictionApplicable(S, C, K)=TRUE`
- `ScopeApplicable(S, C, K)=TRUE`
- `PolicyEpochCurrent(S, C, K)=TRUE`

If any conjunct cannot be lawfully shown:

- `STOP_RULE_APPLICABILITY_INDETERMINATE`
- `NOT_EVALUABLE`

### New objects / relations

- `TerminalAdmissionContext`
- `StopRuleJurisdictionAssessment`
- `StopRuleScopeAssessment`
- `ClaimScopedTerminalEligibilityRecord`
- `PolicyEpochAlignmentAssessment`

### Why previous countermodel fails

Countermodel now fails because admissibility is claim-specific and context-anchored, not reusable globally; a mismatch blocks terminal closure.

### Status

`AUTHOR_CLAIMS_REPAIRED` / `UNRESOLVED` (candidate)

## 6) REPAIR SURFACE R7-03: PRECEDENCE POLICY CONFLICT RESOLUTION

### Source bundle

- ACR-14

### Finding

Competing standing-precedence policies may both be valid while providing non-comparable orderings.

### Root defect

Repair 006 added precedence machinery but did not yet solve the case where precedence policies themselves conflict.

### Countermodel

- `P1: S1 > S2`, `P2: S2 > S1` both applicable, both standing.

### Repair

Introduce explicit conflict classes for policy-level composition:

- `OneStandingPolicyApplicable`
- `MultipleCompatiblePolicies`
- `ConflictingPrecedencePolicies`
- `NoApplicableHigherRule`

Define:

`StandingPolicyConflictResolution(SrcSet, C, K)` requires:
- all applicable composition policies enumerated
- pairwise precedence relation legality checks
- conflict-surface record if both directions occur
- lawful higher-order conflict-resolution policy that is pre-authorized independently

If only lexical/runtime orderability exists without standing authority:

`CONFLICTING_POLICY_ORDER -> NOT_EVALUABLE` (not synthetic ranking)

If no lawful higher-order conflict policy exists:

`CONFLICTING_POLICY_CONTEXT -> NOT_EVALUABLE`.

### New objects / relations

- `StandingPrecedencePolicyRecord`
- `PrecedencePolicyApplicabilityIndex`
- `PrecedenceConflictAssessment`
- `StandingConflictSet`
- `ConstrainedCompositionGate`

### Why previous countermodel fails

The two-direction cycle now remains in explicit conflict state unless a lawful higher-order policy applies. It is not resolved by non-deterministic tie-break.

### Status

`AUTHOR_CLAIMS_REPAIRED` / `UNRESOLVED` (candidate)

## 7) REPAIR SURFACE R7-04: NON-RETROACTIVE STANDING LIFECYCLE

### Source bundle

- ACR-18
- ACR-19

### Finding

Historical validity cannot be directly projected as current reliance.

### Root defect

Repair 006 retained a gap between:

- what was historically treated as valid
- what is currently re-validated after correction/revocation

### Countermodel

- `t0`: source considered valid
- `t1`: system relies on it
- `t2`: defect discovered
- `t4`: source reauthorized

Countermodel fails current inference if it uses historical `t0` status to authorize present conclusions at `t4` over changed evidence.

### Repair

Introduce explicit temporal-lane split:

- `HistoricalStandingRecord`
- `CurrentStandingRelianceRecord`
- `StandingTimelineEvidence`
- `RetroactiveRehabilitationProhibition`
- `HistoricalUseWindow`

Define for any current reliance:

`CurrentReliance(S, C, K, t) :=`
- current standing at `t` with applicable policy epoch
- no retroactive override from unbounded historical correction
- no erased historical decision validity unless separately admitted as forward-valid

Result classes:

- `HistoricalDecisionAt(t)` preserves provenance of what was once concluded
- `CurrentRelianceAt(t)` may differ and cannot infer invalid earlier states were true from reauthorization

Rule:

`ReauthorizationAt(t4) != RetroactiveValidationOf(t2,t3)`

`Rehabilitation != HistoricalErasure`

### New objects / relations

- `StandingTimeSlice`
- `StandingRevisionBoundary`
- `HistoricalVsCurrentStandingMatrix`
- `CorrectionEffectScopeRecord`
- `RetrospectiveClosureProhibitionAssessment`

### Why previous countermodel fails

Temporal correction no longer rewrites earlier conclusions by default; it changes current reliance windows only within lawful forward scopes.

### Status

`AUTHOR_CLAIMS_REPAIRED` / `UNRESOLVED` (candidate)

## 8) HOSTILE COUNTER TRACES FOR REPAIR 007

For each trace:
- INPUT
- DEPENDENCY GRAPH
- ATTACK
- EXPECTED FAILURE
- REPAIR RULE
- RESULT
- COUNTERMODEL DEFEATED?
- NEW ATTACK SURFACE

### R7-TSG-01 (R7-01)
- INPUT: `KnownEdgeVocabulary` declared as "all relevant edges" without provenance boundary.
- DEPENDENCY GRAPH: `B0 -> (edge class E_missing)`.
- ATTACK: `NoCycleFound` inferred from `KnownEdgeVocabulary` that omits `E_missing`.
- EXPECTED FAILURE: false `NO_CYCLE_WITHIN_GROUNDED_VISIBILITY`.
- REPAIR RULE: `DependencyVocabularyStandingAssessment` + `EdgeClassCoverageRecord`.
- RESULT: `DEPENDENCY_DISCOVERY_INCOMPLETE` / `ANCESTRY_VISIBILITY_INCOMPLETE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: unknown edge provenance channels with no coverage contract.

### R7-TSG-02 (R7-01)
- INPUT: local graph A and B each report acyclic; combined graph should include shared edge class.
- DEPENDENCY GRAPH: `A: RA→RB`, `B: RC→RA`, missing cross-link `RC↔RB`.
- ATTACK: local acyclicity accepted as global non-bootstrap.
- EXPECTED FAILURE: arbitrary terminal grounding.
- REPAIR RULE: `CrossRuntimeVisibilityConfluenceRecord` + `InterRuntimeStandingProjectionRecord`.
- RESULT: `ANCESTRY_VISIBILITY_INCOMPLETE` or `NO_CROSS_RUNTIME_CONVERGENCE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: cross-runtime visibility lag and delayed edge publication.

### R7-TSG-03 (R7-02)
- INPUT: stop-rule SR has standing but no proof of applicability to claim class C2.
- DEPENDENCY GRAPH: `SR ──(standing only)──> terminal-stop`
- ATTACK: terminal admissibility used by analogy from another claim class.
- EXPECTED FAILURE: claim-context misapplication.
- REPAIR RULE: `StopRuleApplicableToClaim` + `TerminalSourceApplicableToClaim`.
- RESULT: `TERMINAL_SCOPE_MISMATCH` → `NOT_EVALUABLE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: stale rule-scoped applicability tags.

### R7-TSG-04 (R7-02)
- INPUT: stopping rule itself depends on traversal result in same claim.
- DEPENDENCY GRAPH: `SR -> result -> SR`.
- ATTACK: bootstrap via stop-rule self-dependence.
- EXPECTED FAILURE: recursion disguised as admissibility.
- REPAIR RULE: `StoppingRuleStandingSourceNonBootstrap`.
- RESULT: `STOP_RULE_INADEQUATE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: stop-rule snapshot mismatch by epoch.

### R7-TSG-05 (R7-03)
- INPUT: two precedence policies mutually compare each other.
- DEPENDENCY GRAPH: `P1 > P2`, `P2 > P1` (both standing, both applicable).
- ATTACK: deterministic merge expects one winner.
- EXPECTED FAILURE: synthetic precedence.
- REPAIR RULE: `StandingPolicyConflictResolution`.
- RESULT: `CONFLICTING_PRECEDENCE_POLICIES` / `NOT_EVALUABLE` unless lawful higher policy exists.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: policy epoch collisions where both policies are simultaneously current.

### R7-TSG-06 (R7-03)
- INPUT: jurisdiction overlap with conflict in higher-rule selection.
- DEPENDENCY GRAPH: `S1 + S2 -> composed standing`, overlapping scopes.
- ATTACK: first-applicable heuristic.
- EXPECTED FAILURE: illegitimate global result.
- REPAIR RULE: `JurisdictionIntersection + PrecedenceApplicability Filter`.
- RESULT: `JURISDICTIONAL_PRECEDENCE_CONFLICT` / `NOT_EVALUABLE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: hidden jurisdiction precedence that appears only after claim scoping.

### R7-TSG-07 (R7-04)
- INPUT: historically valid source used as present proof after defect correction.
- DEPENDENCY GRAPH: `S@t0(V) -> rely@t1`, `S@t2(defect)`, `S@t4(reauthorized)`.
- ATTACK: historical fact treated as current lawful ground.
- EXPECTED FAILURE: retroactive authority.
- REPAIR RULE: `StandingTimelineAssessment` + `HistoricalVsCurrentStandingMatrix`.
- RESULT: `CURRENT_STANDING_INDETERMINATE` / `NOT_EVALUABLE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: mixed-epoch evidence caches.

### R7-TSG-08 (R7-04)
- INPUT: past defect correction used to erase noncompliant historical reliance.
- DEPENDENCY GRAPH: `HRecord@t0`, `Correction@t3`, `Current@t4`.
- ATTACK: history erased and rewritten.
- EXPECTED FAILURE: unauthorized temporal authority.
- REPAIR RULE: `CorrectionEffectScopeRecord` + `HistoricalDecisionAt`.
- RESULT: `HISTORICAL_PRESERVATION` + `CURRENT_REBIND_REQUIRED`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: audit replay and correction ordering edges.

### R7-TSG-09 (R7-01 / R7-02 composite)
- INPUT: visible ancestry is complete only within one governance boundary while claim requires broader boundary.
- DEPENDENCY GRAPH: `Boundary B1` complete, `Boundary B2` relevant but omitted.
- ATTACK: overconfident closure under narrower boundary.
- EXPECTED FAILURE: claim exceeds visibility envelope.
- REPAIR RULE: `DependencyVisibilityCompleteRelativeTo(C,K)` + `ConclusionScope<=GroundingScope`.
- RESULT: `DEPENDENCY_VISIBILITY_SCOPE_MISMATCH`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: boundary migration across policy epoch boundaries.

### R7-TSG-10 (R7-01 / R7-03 composite)
- INPUT: three standing policies with mutually non-total comparability.
- DEPENDENCY GRAPH: `S1`, `S2`, `S3` each mutually compatible pairwise and conflicting in triple.
- ATTACK: arbitrary selection.
- EXPECTED FAILURE: false determinism.
- REPAIR RULE: `StandingPolicyConflictResolution` + `ConformanceToHigherPolicy`.
- RESULT: `MULTIPLE_COMPATIBLE_POLICIES` or `CONFLICTING_POLICIES`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: non-transitive policy interaction edges.

### R7-TSG-11 (R7-02 / R7-04 composite)
- INPUT: stop rule valid at t1; claim issued at t3 under revoked policy.
- DEPENDENCY GRAPH: `StopRule@t1 -> terminal` with `Policy@t3(revoked)`.
- ATTACK: time-inappropriate reuse.
- EXPECTED FAILURE: temporal misapplication.
- REPAIR RULE: `PolicyEpochAlignmentAssessment`.
- RESULT: `STOP_RULE_APPLICABILITY_INDETERMINATE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: historical stop-rule snapshots reused without epoch checks.

### R7-TSG-12 (R7-02 / R7-04 composite)
- INPUT: historical standing of terminal source combined with current stale stop rule.
- DEPENDENCY GRAPH: `HistoricalStanding + StaleStop -> terminal`.
- ATTACK: retroactive fusion of two weak states.
- EXPECTED FAILURE: forged certainty.
- REPAIR RULE: `TerminalAdmissionContext` + `CurrentStandingRelianceRecord`.
- RESULT: `NOT_EVALUABLE`.
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: stale composite caches.

## 9) CLOSURE STANDING

R7_01: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

R7_02: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

R7_03: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

R7_04: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

No closure claim is asserted in this repair session. This artifact is candidate-only.

## 10) NON-COMPENSATION PRINCIPLES (In-force)

- Grounded terminal closure is **not** authority.
- A terminal source is lawful only relative to a specific claim, scope, jurisdiction, and policy epoch.
- `NO_CYCLE_WITHIN_GROUNDED_VISIBILITY` does not imply `GLOBAL_ACYCLICITY`.
- `Stopped` is not equal to `AuthoritativelySolved`.
- `NOT_EVALUABLE` is terminal on unresolved grounding, not a positive semantic claim.
- `CONFLICTING_POLICIES` do not downgrade to first-accepted or lexical precedence.
- `HISTORICAL_DECISION` is preserved, but does not erase the requirement for `CURRENT_STANDING`.

## 11) STANDING OF THIS REPAIR ARTIFACT

- `BOUNDED_REPAIR_CANDIDATE`
- `NONCANONICAL`
- `NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR`
- `NOT_ADOPTED`
- `NOT_RATIFIED`

Operational branches:

- Gene: `HOLD`
- Foundation IR: `HOLD`

## 12) NEXT AUTHORIZED LANE (post-Repair 007 candidate)

- `FRESH_INDEPENDENT_HOSTILE_REVIEW_OF_BOUNDED_REPAIR_007`
- Reviewer ownership and closure remain external to this repair.
- No adoption, ratification, or authority mutation is authorized here.
