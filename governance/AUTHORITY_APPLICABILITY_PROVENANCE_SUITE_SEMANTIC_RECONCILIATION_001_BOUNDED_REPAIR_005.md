# AUTHORITY APPLICABILITY PROVENANCE SUITE
# SEMANTIC RECONCILIATION 001 · BOUNDED REPAIR 005

AUTHORIZE: AUTHORIZE_SELFIR_CAUSAL_NONBOOTSTRAP_AND_TERMINAL_STANDING_REPAIR_005_ONLY

RUNTIME: CODEXSELF / SELFIR

SESSION CLASS: BOUNDED_SEMANTIC_REPAIR

SESSION REQUIREMENT: Fresh Repair Session

PREDECESSOR: BOUNDED_REPAIR_004

SOURCE REVIEW: BOUNDED_REPAIR_004_INDEPENDENT_HOSTILE_REVIEW_001

WORKING TREE: `/Users/millysituated/RUORA-worktrees/authority-applicability-provenance-suite-bounded-repair-003`

CURRENT BRANCH: `agent/authority-provenance-bounded-repair-003`

CURRENT HEAD PRE-COMMIT: `9d134dd4e678b1d209ee002b30e7faadf40c2b92`

## 1) TARGET INTEGRITY WITNESS

Target artifact to repair: `AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_004.md`

Authoritative source review artifact:
- `governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_004_INDEPENDENT_HOSTILE_REVIEW_001.md`

Source review commit:
- `9d134dd4e678b1d209ee002b30e7faadf40c2b92`

Source review SHA-256:
- `3b8f82058dd712b68ac9d8bc429516939b6d573090d1eb0f8407f847549f5ceb`

Predecessor repair commit:
- `f7fc4a307e492878dcfb991e970065d35dca2df0`

Predecessor artifact SHA-256:
- `7d146da25b7f66555668a61943e4e66e68d2893e984cced04f7ee71f5bbde01b`

Predecessor artifact witness (observed):
- path: `governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_004.md`
- lines: 526
- bytes: 24545

Source review witness (observed):
- path: `governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_004_INDEPENDENT_HOSTILE_REVIEW_001.md`
- lines: 337
- bytes: 15498

Integrity checks passed:
- `Review input SHA-256 matches expected`
- target and source path are exact
- no path overwrite attempt

## 2) INPUT REVIEW VERDICT AND SESSION CONTINUITY

Source review top-level verdict:
- `CHANGES_REQUIRED`

Residual openings from source review:
- `R5-01`: Boundary-control terminal standing unresolved
- `R5-02`: Conformance-authority terminal standing unresolved
- `R5-03`: Basis-domain merge-policy terminal standing unresolved

Session and governance constraints enforced:
- `RepairSession != PriorReviewerSession`
- `IHR-B01 … IHR-B10` not reopened
- `Gene` branch remains HOLD
- `Foundation IR` branch remains HOLD
- no implementation/schema/runtime/shared ontology edits
- no Notepad semantics
- no ClaudeSELF projection

## 3) PRIMES OF AUTHORIZED SCOPE

Authorized repair domain (only):
1. R5-01 — Boundary-control source terminal standing
2. R5-02 — Conformance-authority terminal standing
3. R5-03 — Basis-domain merge-policy terminal standing

Excluded from this repair:
- IHR-B01 … IHR-B10
- previous Repair 001/002/003 internal subject surfaces
- Gene mutation
- Foundation IR mutation
- DATASELF/AgentBridge/Notepad/implementation/schema

## 4) PRIME LAW FOR REPAIR 005

The repair constrains authority transfer by preventing standing from terminating in a source that depends on the very proposition/domain/registry/policy/control system it is grounding.

Core non-collapse requirements:

- `Standing cannot terminate in a source whose own standing depends directly or transitively on the proposition under which it is used to ground.`
- `DifferentRecord != IndependentStanding`
- `DifferentNamespace != IndependentStanding`
- `DifferentRuntime != IndependentStanding`
- `GraphDisjointness != CausalIndependence`
- `LocalAcyclicity != GlobalNonCircularGrounding`

Conclusion law:

`ConclusionScope <= GroundingScope`

If no lawful terminal standing can be established:

`STANDING_TERMINATION_UNRESOLVED -> NOT_EVALUABLE`

No authority is minted by this repair.

## 5) REPAIR 005 CANDIDATE SEMANTIC OBJECTS

Candidate terminology introduced only as repair-scoped constructs:

- `StandingDependencyGraph`
- `StandingDependencyPath`
- `GroundingDependencyPath`
- `TerminalStandingSource`
- `TerminalSourceAdmissibilityAssessment`
- `StandingTerminationAssessment`
- `GroundingIndependenceAssessment`
- `CausalBootstrapCycleAssessment`
- `TerminalStandingScope`

No standing to be granted for these names as institutional entities in this pass.

## 6) FOUNDATIONAL MODEL (REPAIRED)

### 6.1 StandingDependencyPath

`StandingDependencyPath(X)` is complete when it enumerates every standing-bearing dependency used by the conclusion about `X`.

For each candidate path node:
- `StandingRecordNode`: has primary class
- `StandingDerivationEdge`: typed as admissible dependency (`requires`, `adoptedBy`, `derivedFrom`)
- `ClosureBoundaryGuard`: scoped boundary at which traversal may stop

### 6.2 TerminalStandingSource

`TerminalStandingSource(S)` is admissible only when:

1. `S` has a standing-bearing source record that is itself independently grounded outside `S`’s own candidate/control universe.
2. every dependency in `StandingDependencyPath` for `S` is traversable and lawful.
3. no node in the dependency ancestry includes the proposition/domain/registry/policy/control system that `S` is grounding.

### 6.3 StandingTerminationAssessment

`StandingTerminationAssessment(X)` requires:

1. explicit standing dependency graph extracted for `X`
2. `GroundingIndependenceAssessment(X, TerminalStandingSource)` holds
3. either:
   - lawful admissible terminal source reached, or
   - unresolved (then `NOT_EVALUABLE`)

### 6.4 Conformance authority boundary

`CrossRuntimeAgreement` is treated as convergence evidence only and never as constitutional correctness.

`ConformanceAuthority` is lawful only with standing-independent terminal grounding.

## 7) R5-01 FINDING: BOUNDARY-CONTROL SOURCE TERMINAL STANDING

**FINDING**: `R5-01`

**COUNTERMODEL ADDRESSED**: Mutually certifying boundary roots where local disjoint subgraphs each appear self-contained but jointly form a bootstrap cycle:

- `B0 -> Root_A`
- `B1 -> Root_B`
- `Root_A -> validates(B1)`
- `Root_B -> validates(B0)`

**ROOT DEFECT**: no lawful terminal standing boundary source is guaranteed when root nodes certify each other.

**PROPOSAL REPAIR**:

- `BoundaryStanding(B)` is valid only if `StandingDependencyPath(B)` has a resolved lawful `TerminalStandingSource`.
- terminal source must satisfy `GroundingIndependenceAssessment(source, B)` where independence is causal, not structural.
- local acyclicity and namespace/runtime disjointness are insufficient.

**NEW OBJECTS / RELATIONS**
- `BoundaryStandingDependencyPath(B)`
- `BoundaryStandingTerminationAssessment`
- `BoundarySourceIndependenceAssessment`

**NEW DEPENDENCIES**
- `BoundaryCandidateSet` now depends on lawful resolution of `BoundaryControlSourceStandingAssessment`.
- `BoundaryStanding` depends on admissibility of every path node before claiming complete.

**WHY COUNTERMODEL NOW FAILS**

The proposed terminal-termination test rejects cyclic support when boundary source proof reduces to the very control domain being grounded (`BoundaryStanding` cannot bootstrap itself via mutually validating roots).

**NEW ATTACK SURFACE**
- Multi-source bootstrap cycles with bounded partial admission (still unresolved without explicit jurisdictional terminal admission).

**STATUS**: `AUTHOR_CLAIMS_REPAIRED` (UNRESOLVED)

## 8) R5-02 FINDING: CONFORMANCE-AUTHORITY TERMINAL STANDING

**FINDING**: `R5-02`

**COUNTERMODEL ADDRESSED**:

- Registry/contract authority is derived from an authority relation that is itself determined by that same registry/contract lineage.
- Ten runtimes converge on one result without legitimizing constitutional authority.

**ROOT DEFECT**: conformance machinery had result-legitimacy and authority-legitimacy confounded.

**PROPOSAL REPAIR**:

- `ConformanceAuthorityStanding(C)` must resolve through `StandingDependencyPath(C)` to an admissible terminal source unrelated causally to `C`’s claimed governance outcome.
- `ConformanceAuthorityStanding` cannot be established by mere `ConformanceRule` existence, registry existence, or agreement convergence.
- Introduce explicit separation:
  - `ConformanceRule` (semantic mapping result)
  - `ConformanceRuleStanding` (authority to govern identity)
  - `ConformanceRuleStanding` itself requires independent termination.

**NEW OBJECTS / RELATIONS**
- `ConformanceAuthorityStandingAssessment`
- `ConformanceAuthorityTerminationPath`
- `ConformancePolicyControlBoundary` (scoped to actor/jurisdiction/policy epoch)

**NEW DEPENDENCIES**
- `RepresentationTypeRegistry`/`CanonicalSerializationContract` now require lawful terminal grounding for standing claims.
- `CrossRuntimeConformanceAssessment` contributes only to convergence score, not authority.

**WHY COUNTERMODEL NOW FAILS**

Because terminal sourcing is traced to nodes outside the conformance domain being adjudicated; consensus-only conclusions are downgraded to `NOT_ENOUGH_FOR_AUTHORITY` unless a lawful independent terminal is established.

**NEW ATTACK SURFACE**
- Hidden governance chain where external trust boundary itself is sourced from the governed contract.

**STATUS**: `AUTHOR_CLAIMS_REPAIRED` (UNRESOLVED)

## 9) R5-03 FINDING: BASIS-DOMAIN MERGE-POLICY TERMINAL STANDING

**FINDING**: `R5-03`

**COUNTERMODEL ADDRESSED**:

- Every fragment is independently standing and deterministic merge is lawful, but merge policy is derived from the same constrained domain it certifies.
- Deterministically merged fragments do not guarantee lawful closed-domain completeness.

**ROOT DEFECT**: merged domain standing can inherit from a closure policy whose own standing is unresolved.

**PROPOSAL REPAIR**:

- `BasisDomainClosureStanding(D)` requires explicit grounding of:
  1. `BasisKindCandidateSet` standing
  2. merge/composition rule standing
  3. applicability rule standing
  4. terminal source admissibility checks
  5. bounded conclusion ceiling
- If terminal grounding unresolved -> `BASIS_DOMAIN_BOOTSTRAP_OR_UNRESOLVED` and query class becomes `NOT_EVALUABLE`.

**NEW OBJECTS / RELATIONS**
- `BasisDomainMergeAuthoritySource`
- `BasisDomainMergeTerminationPath`
- `BasisDomainTerminalSourceAdmissibility`

**NEW DEPENDENCIES**
- `BasisDomainClosureAssessment` no longer depends only on admissible fragments; it depends on merge-policy terminal validity.

**WHY COUNTERMODEL NOW FAILS**

Because domain completeness in this proposal is a scoped inference only after merge policy and composition authorities are independently admissible and non-self-referential.

**NEW ATTACK SURFACE**
- Time-skewed merge-policy authority where jurisdiction or epoch changes after a fragment merge.

**STATUS**: `AUTHOR_CLAIMS_REPAIRED` (UNRESOLVED)

## 10) CLOSURE LAW THAT PREVENTS INFINITE RECURSION

The repair introduces a hard stop in dependency resolution:

`StandingTermination(X)` is true only if one of:

1. Admissible terminal source is in-scope and legally distinct from `X`’s governance system.
2. Or unresolved with explicit `NOT_EVALUABLE` outcome.

Forbidden forms:
- inventing a root by default
- inferring trusted roots from incomplete candidate sets
- standing-standing records without independent terminal source provenance

## 11) HOSTILE PRESSURE TRACES (TSG-01 … TSG-12)

Trace format used:
- INPUT
- DEPENDENCY GRAPH
- ATTACK
- EXPECTED FAILURE
- REPAIR RULE
- RESULT
- COUNTERMODEL DEFEATED?
- NEW ATTACK SURFACE

### TSG-01
- INPUT: Two boundary roots certify each other
- DEPENDENCY GRAPH: `RootA -> validates(B1)` and `RootB -> validates(B0)`
- ATTACK: local disjointness accepted as lawful termination
- EXPECTED FAILURE: boundary standing loops at roots
- REPAIR RULE: `BoundaryStandingTerminationAssessment` + terminal non-bootstrap scan
- RESULT: rejected unless a terminal source outside {B0,B1} control scope is reached
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: cross-branch but temporally bounded certification chains

### TSG-02
- INPUT: Three root nodes across runtimes form a transitive dependency cycle
- DEPENDENCY GRAPH: Runtime1.RootA -> Runtime2.RootB -> Runtime3.RootC -> Runtime1.RootA
- ATTACK: runtime separation mistaken for independence
- EXPECTED FAILURE: false terminalization on namespace boundary
- REPAIR RULE: causal ancestry check on combined standing graph, not runtime-local graph
- RESULT: unresolved unless explicit terminal boundary source exists
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: asynchronous admission drift across runtimes

### TSG-03
- INPUT: distinct object IDs and namespaces from same causal root lineage
- DEPENDENCY GRAPH: SourceX and SourceY share hidden provenance path to same admissible claim source
- ATTACK: identity disjointness mistaken as independence
- EXPECTED FAILURE: root appears duplicated but not independent
- REPAIR RULE: Causal standing ancestry deduplication before terminal acceptance
- RESULT: terminal path rejects both if lineage loops through same controlling source
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: provenance hash collision in standing lineage indexes

### TSG-04
- INPUT: conformance registry authority inferred from registry entry classification it controls
- DEPENDENCY GRAPH: `Registry -> AuthorityRecord -> Registry`
- ATTACK: authority circularity
- EXPECTED FAILURE: self-authorizing conformance governance
- REPAIR RULE: `ConformanceAuthorityStanding` requires terminal source not depending on same conformance claim domain
- RESULT: no standing; outcome set to `CONFORMANCE_AUTHORITY_BOOTSTRAP`
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: hidden policy-control recursion between contract and registry schema

### TSG-05
- INPUT: canonical serialization authority chain depends on policy identity derived by itself
- DEPENDENCY GRAPH: `PolicyIdentity -> CanonicalContract -> PolicyIdentity`
- ATTACK: canonical identity bootstrapping
- EXPECTED FAILURE: spurious identity certainty
- REPAIR RULE: separate `ConformanceRule` from `ConformanceRuleStanding`; terminal admissibility for the latter
- RESULT: classification remains convergent but not authoritative until terminal source proven
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: stale contract snapshots in boundary-scoped governance epochs

### TSG-06
- INPUT: ten runtime implementations produce identical conformance outputs on unauthorized rule
- DEPENDENCY GRAPH: many implementations -> same conformance map
- ATTACK: equating consensus with correctness
- EXPECTED FAILURE: unauthorized authority minted from agreement
- REPAIR RULE: cross-runtime convergence only feeds equivalence score; terminal authority still required
- RESULT: remains `NOT_EVALUABLE` for authority, only semantically equivalent behavior claim
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: runtime-specific canonicalization fallback divergence under load

### TSG-07
- INPUT: basis fragments all have standing; merged set declared complete by deterministic union
- DEPENDENCY GRAPH: `Union -> ClosedDomainClaim` with no merge-root grounding
- ATTACK: inferred completeness without admissible merge authority
- EXPECTED FAILURE: false negative handling from under-closed domain
- REPAIR RULE: `BasisDomainMergeAuthority` requires terminal admissible merge policy source
- RESULT: closure claim blocked; result downgraded to scoped negative
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: competing lawful merge authorities with partial overlap

### TSG-08
- INPUT: merge policy standing derived from the same domain it certifies
- DEPENDENCY GRAPH: `Domain D` depends on `MergePolicy M`; `M` depends on claims over D
- ATTACK: circular domain certification
- EXPECTED FAILURE: global completeness false claim
- REPAIR RULE: dependency graph requires admissible external terminal source for merge policy
- RESULT: `BASIS_DOMAIN_BOOTSTRAP_CYCLE` -> `NOT_EVALUABLE`
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: staged epoch supersession of merge policy source

### TSG-09
- INPUT: terminal source is historically valid but currently revoked/superseded
- DEPENDENCY GRAPH: TerminalSource@t0 -> used at t1 after revocation at t2
- ATTACK: using stale terminal grounding
- EXPECTED FAILURE: stale authority over current assessment
- REPAIR RULE: terminal source must satisfy `CurrentStandingAt(query_snapshot)` and revocation-aware applicability
- RESULT: terminal unresolved if revocation boundary makes source non-current
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: jurisdictional retroactive changes affecting terminal status

### TSG-10
- INPUT: terminal source exists but outside governing jurisdiction
- DEPENDENCY GRAPH: `TerminalSource(scope=A)` grounding `subject(scope=B)` with no cross-scope authority link
- ATTACK: jurisdiction bleed
- EXPECTED FAILURE: unauthorized cross-jurisdiction grounding
- REPAIR RULE: `GroundingIndependenceAssessment` includes jurisdiction compatibility
- RESULT: rejected as `JURISDICTIONAL_NON_COMPARABLE`
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: federated governance domains with overlapping control boundaries

### TSG-11
- INPUT: evaluator treats `NOT_EVALUABLE` as permissive continuation
- ATTACK: replacing standing unknowns with default permissive outcomes
- EXPECTED FAILURE: false positive applicability
- REPAIR RULE: explicit `NOT_EVALUABLE` terminal is absorbing for dependent authority claims
- RESULT: no continuation unless separate downstream session resolves standing source
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: policy engines that silently coerce unknown to FALSE/TRUE

### TSG-12
- INPUT: evaluation result scope exceeds grounding scope that supported terminal source
- ATTACK: scope overreach / conclusion leakage
- EXPECTED FAILURE: claims with larger epistemic reach than lawful boundary
- REPAIR RULE: `GroundedSemanticConclusion` function computes strict scope envelope
- RESULT: result tagged `ConclusionScope=GroundingScope` and reduced to bounded context
- COUNTERMODEL DEFEATED? `YES`
- NEW ATTACK SURFACE: boundary composition across independent authorities with incompatible epochs

## 12) ROOT / STANDING TERMINATION ASSESSMENT SUMMARY

- `RootRecord != TerminalStandingSource`
- `RootTermination` is lawful only if path ancestry reaches admissible non-dependent source.
- `No lawful terminal source` -> `NOT_EVALUABLE` (explicit, no fallback inference).
- `ConformanceAgreement`, `BoundaryAgreement`, and `BasisMergeAgreement` are convergence signals only; they are not standing sources.

## 13) CLOSURE CEILING ENFORCEMENT

Every authority conclusion now carries explicit ceilings:

- `scope`
- `jurisdiction`
- `policy_epoch`
- `standing_version`

No proposal outcome may exceed these ceilings.

## 14) BOUNDARY / ROOTING OF AUTHORITATIVE ASSERTIONS

Not minted:
- New repository
- New SELF
- New institution
- universal trust root

Allowed:
- A lawful, explicit, boundary-scoped terminal source set declared by previously established governance surfaces.

## 15) REPAIR LIMITATION MATRIX

R5-01: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

R5-02: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

R5-03: `AUTHOR_CLAIMS_REPAIRED / UNRESOLVED`

No closure claim is claimed as final in this repair artifact.

## 16) NEXT LAWFUL EDGE

Authorized next edge is review-only:

`FRESH_INDEPENDENT_HOSTILE_REVIEW_OF_BOUNDED_REPAIR_005`

This repair artifact is a candidate and not yet independently adjudicated.

## 17) STANDING OF THIS REPAIR ARTIFACT

- `BOUNDED_REPAIR_CANDIDATE`
- `NONCANONICAL`
- `NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR`
- `NOT_ADOPTED`
- `NOT_RATIFIED`

GENE Branch: `HOLD`
Foundation Branch: `HOLD`

## 18) WITNESS AND HANDOFF

- No mutation to GitHub policy, no ratification, no seal, no implementation.
- Candidate artifact is intended for exact downstream inspection and hostile review.
- ReviewerSession and RepairSession are distinct by construction.
- This repair does not consume, execute, or supersede any prior review.
