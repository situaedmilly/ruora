BOUNDED REPAIR 003 CANDIDATE
=============================================================

ARTIFACT CLASS: BOUNDED_REPAIR_CANDIDATE
TARGET SUBJECT: AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001
RUNTIME: CODEXSELF / SELFIR
REPAIR SESSION: Fresh repair session over Repair 002 review residue
SESSION BOUNDARY: RepairSession != ReviewSession
REPAIR_SCOPE: R3-01, R3-02, R3-03 ONLY

REPAIR STANDING
--------------
REPAIR_SESS_STARTED: YES
REPAIR_SCOPE_BOUNDARY: R3-01..R3-03
AUTHOR: CODEXSELF / SELFIR
SOURCE_REVIEW_ARTIFACT: AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_002_INDEPENDENT_HOSTILE_REVIEW_002.md
SOURCE_REVIEW_COMMIT: e56e86d6fd6fb5616b89a22d5d4da2927a44d2ce
SOURCE_REVIEW_TOP_LEVEL_VERDICT: CHANGES_REQUIRED
TARGET_REVIEW_COMMIT_REFERENCED_BY_SCOPE: 4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f
Gene Authority Branch: HOLD
Foundation IR Branch: HOLD
SELFIR: ACTIVE_ON_UNRELATED_BRANCHES
NOTEPAD_INTEGRATION: DEFERRED
next_gate_authorized_only: AUTHORIZE_SELFIR_REPAIR_003_CLOSURE_CONFORMANCE_AND_NEGATIVE_DOMAIN_ONLY

INPUT VERIFICATION
------------------
Input review artifact path:
governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_002_INDEPENDENT_HOSTILE_REVIEW_002.md

Input review commit:
e56e86d6fd6fb5616b89a22d5d4da2927a44d2ce

Input artifact proof (local witness prior to this repair run):
lines=296
bytes=13021
sha256=c94f0a8c70f9665a67c0132f431f4d583518c864d716e847d3e164aff5913130

Validation of source linkage:
- target line: R3-01 R3-02 R3-03 are present in the input review and no earlier IHR-B01–IHR-B10 findings remain active in the scope gate.
- REVIEW gate lineage in input is AUTHORIZE_SELFIR_REPAIR_003_CLOSURE_CONFORMANCE_AND_NEGATIVE_DOMAIN_ONLY.

CRITICAL STABILITY RULE FOR THIS REPAIR
---------------------------------------
The previous review’s embedded status tags were advisory, not adjudicative.

Invariant:
- ReviewerProposesRepair != RepairOccurred
- CountermodelWouldFailUnder(ProposedRepair) != CountermodelFailedAgainst(ManifestedRepair)

Therefore all finding closures are represented as hypotheses until a future independent review.

FINDING MODEL (for R3-01..R3-03)
----------------------------------
Each finding must be captured with:
1) FINDING
2) COUNTERMODEL
3) ROOT DEFECT
4) REPAIR
5) NEW OBJECTS / RELATIONS
6) NEW DEPENDENCIES
7) WHY COUNTERMODEL NOW FAILS (under the proposed repair law)
8) NEW ATTACK SURFACE
9) STATUS

Global anti-collapse obligations:
- No invented positive root.
- No closure recursion by construction.
- AbsenceObservation != ExhaustiveNegativeProof.
- OPEN_WORLD_DOMAIN remains non-completable by absence.
- No `PathFALSE -> QueryFALSE`, `PathTRUE -> QueryTRUE`.
- No conflation of conformance with byte identity.

R3-01 — GOVERNANCE BOUNDARY META-CLOSURE
-----------------------------------------
FINDING:
Boundary selection can become complete in form but lacking independent lawful boundary-control closure, enabling hidden inflation by candidate reuse.

COUNTERMODEL:
An actor submits B1 as a boundary candidate set, and the closure assessment consumes B1 and marks B1 as complete by citing B1 as its own admissible boundary law and source.

ROOT DEFECT:
The closure mechanism has no separate boundary-control admissibility chain and no explicit source-of-control record, so boundary completion can become self-referential.

REPAIR:
Introduce a lawful boundary hierarchy that separates candidate collection from boundary admissibility:

1. `BoundaryCandidateSetRecord`
   - Inputs: candidate identifiers, discovered candidate sources, discovery context.

2. `BoundaryControlDomainRecord`
   - One of:
     - `OPEN_WORLD_DOMAIN`
     - `GOVERNED_CLOSED_DOMAIN`
     - `EXTERNALLY_BOUNDED_DOMAIN`

3. `BoundaryControlSourceRecord`
   - Admissible provenance for the control domain (cannot be inferred from candidate set).

4. `BoundarySelectionStandingAssessment`
   - Requires independent standing of `BoundaryControlSourceRecord`.

5. `BoundarySelectionLawRecord`
   - Must admit boundaries only if standing and control source are already resolved.

6. `BoundaryCandidateSetClosureAssessment`
   - Input set:
     - `BoundaryCandidateSetRecord`
     - `BoundaryControlDomainRecord`
     - `BoundarySelectionStandingAssessment`
     - `BoundarySelectionLawRecord`
   - Output: `BoundaryCandidateSetClosureResult`

7. `BoundaryApplicabilityToClosureContextAssessment`
   - Evaluates whether closure is attempted in open/closed/bounded mode.

8. `NoSelfAuthorshipConstraint`
   - Forbid any `BoundarySelectionLawRecord` from depending on unresolved boundary completion that uses the same candidate set.

9. `CompleteBoundaryAssessment`
   - Only if all above assessments are complete.
   - Output form:
     `CompleteBoundaryAssessment(boundary_ref, policy_epoch, control_domain, registry_set)`

This closes the regression:
- A boundary can be complete only relative to an explicitly controlled, independently standing source.
- Closure law candidates cannot be both the boundary source and the closure beneficiary in the same unresolved cycle.

NEW OBJECTS / RELATIONS:
- BoundaryCandidateSetRecord
- BoundaryControlDomainRecord
- BoundarySelectionLawRecord
- BoundaryControlSourceRecord
- BoundarySelectionStandingAssessment
- NoSelfAuthorshipConstraint
- BoundaryCandidateSetClosureAssessment
- BoundaryCandidateSetClosureResult

NEW DEPENDENCIES:
- `BoundarySelectionStandingAssessment` depends on `BoundaryControlSourceRecord`.
- `BoundarySelectionLawRecord` depends on `BoundarySelectionStandingAssessment`.
- `BoundaryCandidateSetClosureAssessment` depends on all of:
  - `BoundaryCandidateSetRecord`
  - `BoundarySelectionLawRecord`
  - `BoundarySelectionStandingAssessment`
  - `BoundaryControlDomainRecord`

WHY COUNTERMODEL NOW FAILS:
The self-referential loop now requires two independent prerequisites: control-source standing and non-self-authorship. A candidate cannot prove its own admissibility because dependency on `BoundarySelectionLawRecord` now requires resolved, independent standing.

NEW ATTACK SURFACE:
- Declaring `BoundaryControlDomainRecord` without corresponding control-source standing.
- Smuggling boundary laws through admissible-but-foreign registries with no cross-boundary control witness.

STATUS:
OPEN_FINDING

R3-02 — DETERMINISTIC CONFORMANCE
----------------------------------
FINDING:
Equivalent normative states can serialize differently; Repair 002 did not sufficiently constrain determinism class-by-class, allowing identity disputes in conformance-critical objects.

COUNTERMODEL:
Implementations I1 and I2 process the same normative inputs, same policy epoch, same snapshot, but emit different byte structures.
- I1 marks grant-path result object as identity-bearing and compares raw bytes.
- I2 emits equivalent semantics with diff bytes and gets rejected.
- A second normative query using the same inputs now diverges.

ROOT DEFECT:
Conformance law in Repair 002 used bytes as a weak proxy for identity across all object classes and did not enforce the identity class boundaries required to prevent this split.

REPAIR:
Define two orthogonal axes:

1. `NormativeIdentityClass`
   - `MANDATORY_IDENTITY`: representation identity must be deterministic and canonical.
   - `NON_MANDATORY_IDENTITY`: canonical equivalence may permit structural differences.

2. `CanonicalSerializationContract`
   - Includes: normative model version, contract dialect, canonicalization algorithm, canonical hash function.

3. `ConformanceDeterminismAssessment`
   - Validates that two independent implementations produce:
     - equal `NormativeIdentityClass` mapping,
     - equal canonicalized representation for `MANDATORY_IDENTITY`,
     - equivalent canonical structure for `NON_MANDATORY_IDENTITY`.

4. `RepresentationTypeRegistry`
   - Binds each semantic object to its identity class and mandated conformance level.

5. `CrossRuntimeConvergenceLaw`:
   `SameNormativeInputs + SameInputsEpoch + SameSnapshot + SameConformanceContract + IndependentConformingRuntime -> same_identity_result_for_mandatory, canonical_equiv_for_non_mandatory`

6. `RepresentationWitnessSet`
   - Contains the observed serialization profiles and their conformance verdict.
   - Must include `representation_version` and `runtime_profile`.

This introduces deterministic conformance without demanding universal byte identity for every object.

NEW OBJECTS / RELATIONS:
- NormativeIdentityClass
- CanonicalSerializationContract
- ConformanceDeterminismAssessment
- RepresentationTypeRegistry
- RepresentationWitnessSet
- CrossRuntimeConvergenceLaw

NEW DEPENDENCIES:
- `ConformanceDeterminismAssessment` depends on canonical version and dialect metadata in `CanonicalSerializationContract`.
- `CrossRuntimeConvergenceLaw` depends on `RepresentationTypeRegistry`.

WHY COUNTERMODEL NOW FAILS:
If an object is marked `MANDATORY_IDENTITY`, byte divergence itself becomes a conformance failure; if it is not, canonical equivalence is accepted. The previous loophole where bytes became the only source of disagreement is removed.

NEW ATTACK SURFACE:
- Oracle drift in `CanonicalSerializationContract` registry (malicious contract upgrades).
- Cross-runtime implementation that passes conformance for non-mandatory classes while mutating mandatory classes.

STATUS:
OPEN_FINDING

R3-03 — BASIS-KIND / NEGATIVE-DOMAIN CLOSURE
----------------------------------------------
FINDING:
Negative proof still risks incompleteness if applicable basis-kind universes are not closed relative to the same evaluation boundary.

COUNTERMODEL:
Known basis kinds set K1 is exhaustively searched and no grant basis is found.
However, hidden basis kind family K2 is in a different admissible domain and would alter the query result if closure were broader.

ROOT DEFECT:
`ExhaustiveSearchWithinKnownBasisKinds` can be mistaken for completion; no explicit domain-mode closure witness and no applicable basis-kind set proof were required for negative outcomes.

REPAIR:
Introduce a two-tier structure:

1. `BasisKindDomainRecord`
   - enumerates basis-kind families and their domain membership.

2. `BasisKindDomainStandingRecord`
   - requires standing for the domain record itself before using it for negative derivations.

3. `BasisKindApplicabilityRecord`
   - maps policy epoch + boundary candidate + basis kind set to an applicable-kind subset.

4. `BasisKindSetClosureAssessment`
   - computes closure of applicable basis kinds only after domain standing and control are resolved.

5. `NegativeOutcomeDomainMode`
   - one of:
     - `OPEN_WORLD_DOMAIN`
     - `GOVERNED_CLOSED_DOMAIN`
     - `EXTERNALLY_BOUNDED_DOMAIN`

6. `NegativeDomainDisposition`
   - For `OPEN_WORLD_DOMAIN`: negative remains `NOT_EVALUABLE` unless independently exhaustive external evidence exists.
   - For `GOVERNED_CLOSED_DOMAIN`: negative may become `FALSE` when:
     - `BasisKindSetClosureAssessment` proves closure
     - `NegativeEvidenceSet` is complete within that closed set.
   - For `EXTERNALLY_BOUNDED_DOMAIN`: negative becomes `FALSE` only with declared external boundary compliance.

7. `NegativePropositionAssessment`
   - Output:
     - `NOT_EVALUABLE` when closure witness missing,
     - `FALSE` only under bounded domain closure,
     - `TRUE` only under positive query proof.

This model avoids false negatives by binding negative proof to explicit domain and basis closure obligations.

NEW OBJECTS / RELATIONS:
- BasisKindDomainRecord
- BasisKindDomainStandingRecord
- BasisKindApplicabilityRecord
- BasisKindSetClosureAssessment
- BasisKindSetClosureResult
- BasisKindSetDependencyGraph
- NegativeOutcomeDomainMode
- NegativeDomainDisposition
- NegativePropositionAssessment

NEW DEPENDENCIES:
- `BasisKindSetClosureAssessment` depends on `BasisKindDomainStandingRecord` and `BasisKindApplicabilityRecord`.
- `NegativePropositionAssessment` depends on `NegativeOutcomeDomainMode` and `BasisKindSetClosureResult`.
- `NegativeDomainDisposition` depends on `NegativeOutcomeDomainMode`.

WHY COUNTERMODEL NOW FAILS:
K2 can only affect the result when the negative witness establishes it as an applicable basis kind in-domain. Under `OPEN_WORLD_DOMAIN`, absence in K1 cannot conclude false; therefore the countermodel does not generate false exclusion.

NEW ATTACK SURFACE:
- Declaring a `GOVERNED_CLOSED_DOMAIN` closure with a boundary that has not passed boundary standing.
- Incomplete basis-kind registry admitting only favorable kinds while excluding adversarial ones without a standing rule trace.

STATUS:
OPEN_FINDING

COUNTERMODEL RE-INTERACTION FOR THIS REPAIR
-------------------------------------------
The repair session replays the new residual countermodels in candidate form.

Z1 Query-law split
- Old failure: same query resolved by locally complete law but boundary mismatch at evaluation mode.
- Repair path: apply R3-01 and R3-03 before query-law closure.
- New result: unresolved until candidate boundary standing and closure witness is complete.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z2 Policy-selector split
- Old failure: selection law and authority law entangle via boundary reuse.
- Repair path: selection now depends on boundary control standing and no-self-authorship constraints.
- New result: loop blocked when selection requires independent boundary standing.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z3 Root/control omission
- Old failure: root closure treated as local claim.
- Repair path: boundary control domain requires explicit control source and closure dependency.
- New result: closed only relative to independent control source.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z4 Rule-record oracle
- Old failure: oracle-like rule record accepted for completion without admissibility.
- Repair path: rule record must be in representation conformance registry and boundary control chain.
- New result: becomes candidate-dependent and review-facing.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z5 Negative-proof cast
- Old failure: absence evidence interpreted as negative without closure across basis-kind domain.
- Repair path: negative domain mode + basis closure witness requirements.
- New result: negative requires governed-closed/external bounded closure.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z6 Context injection
- Old failure: caller-provided context could bias boundary selection.
- Repair path: boundary control source provenance required for completeness.
- New result: caller context remains an input only after control validation.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z7 Snapshot recursion
- Old failure: boundary closure and snapshot identities fed through unresolved closure-law cycle.
- Repair path: closure output is emitted as `CompleteBoundaryAssessment` with explicit policy epoch and registry-set witness.
- New result: recursion breaker added by separate standing/control chain.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z8 Immediate self-revocation
- Old failure: revocation proof depends on query closure without closure-mode witness.
- Repair path: not reopened by this gate; treated as dependent on `NoSelfAuthorshipConstraint` if closure path is reused.
- New result: no direct closure via self-revocation.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z9 Retry/replay collision
- Old failure: implementation-level retry and replay collision on identity-bearing outputs.
- Repair path: R3-02 identity class rule differentiates mandatory and non-mandatory identities.
- New result: replay remains deterministic only where identity is mandatory.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

Z10 Supersession survival
- Old failure: closure assumptions for negative proof omitted policy epoch interaction.
- Repair path: all negative closures include policy epoch in `CompleteBoundaryAssessment`.
- New result: supersession now externalized by epoch-vetted closure.
- COUNTERMODEL DEFEATED: PENDING_REVIEW

NEW SPECIMENS GENERATED DURING REPAIR 003
-----------------------------------------
R3-04 Boundary-Control Forgery
- Attempt: actor submits boundary source as a runtime artifact.
- Expected outcome: rejected by `BoundarySelectionStandingAssessment` (no independent control source standing).

R3-05 Conformance-Profile Drift
- Attempt: two dialects emit same non-mandatory object but incompatible mandatory hash.
- Expected outcome: non-mandatory accepted via canonical equivalence; mandatory rejected if hash mismatch.

R3-06 Hidden-Kind Admission
- Attempt: inject hidden basis-kind family K2 after K1 exhaustion.
- Expected outcome: no false negative under `OPEN_WORLD_DOMAIN`; must provide closure witness for closed-domain claim.

R3-07 Cross-Mode Boundary Migration
- Attempt: switch candidate boundary from GOVERNED_CLOSED to EXTERNALLY_BOUNDED mid-assessment.
- Expected outcome: denied until both control source standing and boundary mode closure are re-evaluated.

R3-08 Identity Class Ambiguity
- Attempt: classify an object lacking registry assignment.
- Expected outcome: default to non-mandatory identity class only if domain policy permits.

R3-09 Closure Witness Substitution
- Attempt: replace boundary completion witness with equivalent-looking witness of unknown provenance.
- Expected outcome: fails `BoundaryControlSourceRecord` and `NoSelfAuthorshipConstraint`.

R3-10 Registry Fragmentation
- Attempt: claim two independent registry fragments jointly close basis kinds.
- Expected outcome: fails until `BasisKindSetClosureAssessment` proves the merged registry is admissibly unified.

DERIVED COMPOSITION TABLE
-------------------------
R3-01, R3-02, R3-03 are all:
- Open findings (candidate hypotheses only)
- Repair hypotheses are explicit, bounded, and scoped
- Not adjudicated as closed by this artifact

No closure claim is inferred from this proposal alone.

GOVERNING POST-REPAIR STANDING
-------------------------------
After this repair session:
- standing remains: BOUNDED_REPAIR_CANDIDATE
- not independently reviewed yet
- not adopted
- not ratified

Gene and Foundation branches are unaffected.

METHODOLOGY BOUNDARIES
-----------------------
- No implementation code changes.
- No schema changes.
- No runtime changes.
- No foundation mutability.
- No Gene mutations.
- No Notepad semantics imported.
- This artifact records model and boundary law changes only.

NEXT_GATED_GATE
---------------
FRESH_INDEPENDENT_HOSTILE_REVIEW_OF_BOUNDED_REPAIR_003

AUTHORITY SEPARATION
--------------------
ReviewerSession != RepairSession
Review != Repair
Review != Adoption
Review != Ratification
