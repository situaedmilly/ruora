# AUTHORITY APPLICABILITY PROVENANCE SUITE — Semantic Reconciliation 001 — Bounded Repair 002

~~~text
ARTIFACT_CLASS:
  BOUNDED_REPAIR_CANDIDATE

PRODUCING_RUNTIME:
  CODEXSELF / SELFIR

REPAIR_SESSION:
  FRESH
  DISTINCT_FROM_PRIOR_REVIEWER_SESSION

REPAIR_SCOPE:
  IHR-B01 THROUGH IHR-B10 ONLY

SOURCE_REVIEW_VERDICT:
  CHANGES_REQUIRED

REPAIR_STANDING:
  BOUNDED_REPAIR_CANDIDATE
  NONCANONICAL
  NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
  NOT_ADOPTED
  NOT_RATIFIED

GENE_AUTHORITY_BRANCH:
  HOLD

FOUNDATION_AUTHORITY_BRANCH:
  HOLD

SELFIR:
  ACTIVE_ON_UNRELATED_BRANCHES

NOTEPAD_INTEGRATION:
  DEFERRED

MUTATIONS_AUTHORIZED_BY_THIS_ARTIFACT:
  NONE
~~~

This artifact is a fresh repair-session response to the ten blocking findings
in the exact source review identified below. It does not inherit reviewer
confidence, repair-author confidence, Founder evaluation, standing, adoption,
ratification, or authority from any predecessor. It never reports an
independent PASS.

The artifact attempts to defeat IHR-B01 through IHR-B10 at the semantic-model
level only. It creates no implementation, schema, runtime, shared ontology,
Gene, Foundation IR, AgentBridge, DATASELF, Notepad, or ClaudeSELF mutation.

~~~text
RepairSession != PriorReviewerSession
AuthorClaim != IndependentReviewResult
RepairCandidate != CanonicalLaw
GitHubPresence != Standing
Commit != Adoption
Push != Ratification
~~~

## 1. EXACT SOURCE REVIEW INPUT WITNESS

The authoritative input was fetched from the connected GitHub repository and
then cross-checked against the same commit and Git blob in the local RUORA
object store. It was not reconstructed from memory, this command, or a prior
repair.

| Witness field | Exact verified value |
|---|---|
| Repository | situaedmilly/ruora |
| Connected GitHub repository ID | 1146440771 |
| Connected GitHub remote | git@github.com:situaedmilly/ruora.git |
| Source review commit | 4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f |
| Source review commit subject | authority: record provenance-suite repair 001 hostile review |
| Source review artifact | governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_INDEPENDENT_HOSTILE_REVIEW_001.md |
| Git blob | 12f0ba9e1ea582c1c4fd08b4b965232c9b999b67 |
| Line count | 945 |
| Byte size | 34,839 |
| SHA-256 | ee26c4cb4f3083b2a84ecdad3c3179d6e574aa56a26142cd97c8efc387d7d264 |
| Expected verdict | CHANGES_REQUIRED |
| Observed verdict | CHANGES_REQUIRED |
| UTF-8 terminal newline | Present |
| Integrity disposition | EXACT_MATCH |

The connected GitHub file response named the same repository, commit, path,
and blob. The local Git object resolved the same blob and produced the exact
line count, byte count, SHA-256, and verdict. The dirty primary worktree was
not used as input and was not modified.

Read-only verification commands:

~~~bash
git rev-parse \
  '4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f:governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_INDEPENDENT_HOSTILE_REVIEW_001.md'

git show \
  '4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f:governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_INDEPENDENT_HOSTILE_REVIEW_001.md' \
  | wc -l -c

git show \
  '4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f:governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_INDEPENDENT_HOSTILE_REVIEW_001.md' \
  | shasum -a 256

git show \
  '4dbeb3baeedcf60eb361ea1b6cd2e61a81a7950f:governance/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_INDEPENDENT_HOSTILE_REVIEW_001.md' \
  | rg -n -A1 '^TOP_LEVEL_VERDICT:'
~~~

No repair was written until every expected identity field matched.

## 2. EXACT EXTRACTED IHR-B01 THROUGH IHR-B10

The following finding text is extracted directly from the exact witnessed
source bytes.

### IHR-B01 — Discovery-law meta-closure is absent

Authority-query and discovery laws have no candidate discovery or closure over
the law set itself.

Countermodel:

~~~text
L1 is independently standing and names only C1.
C1 is empty.

L2 is independently standing and names C2.
C2 contains a valid permit basis.

Evaluation under L1:
  candidate set closed relative to L1
  → FALSE

Evaluation under the complete law set:
  permit exists
  → TRUE or conflict

No closure exists over {L1, L2}.
~~~

### IHR-B02 — Root and control-domain closure is absent

A root bundle reports known conflicts and independence from a named set, but
does not prove that the root set or named control/dependency domain is complete.

Countermodel:

~~~text
R1 reports:
  no known conflict
  independent from K = {suite}

R2 is another applicable root and prohibits q.
or:
an undisclosed actor controls R1 standing.

No RootCandidateSetClosureAssessment exists.
No IndependenceDomainClosureAssessment exists.
~~~

### IHR-B03 — The closed type-inventory claim is false

The graph uses untyped nodes and permits objects of one primary type to receive
assessment dispositions belonging to another.

### IHR-B04 — Policy-selection-law standing is not fully graphed

`PolicyCandidateDiscoveryAssessment` semantically depends on a selection law,
but the dependency is absent from the displayed proof DAG. Selection and
composition laws are consumed as standing without separate standing paths.

### IHR-B05 — Exhaustive negative proof performs an invalid cast

`ExhaustiveNegativeProof` is typed as `EVIDENCE_REFERENCE`, yet it may directly
establish query-level `FALSE`. A separate current assessment is required.

### IHR-B06 — Context binding is an unresolved authority input

`context_binding` has no typed object, authoritative source, currentness
assessment, or owning upstream interface.

Countermodel:

~~~text
actual environment = production
caller-provided context = sandbox
grant permits sandbox only

Caller-selected context changes the authority result.
~~~

### IHR-B07 — Query, snapshot, and graph identities are recursive

~~~text
q contains EvaluationSnapshotIdentity S
S binds exact q
S binds dependency graph identity G
G contains assessments over q and S
~~~

No construction order, pre-snapshot identity, structural graph identity, or
fixed-point law resolves the recursion.

### IHR-B08 — Revocation authority recursion and timing are incomplete

The model requires authority for `REVOKE_GRANT`, but does not fully represent
that subquery in the DAG or specify evaluation against immediate pre-state,
post-state, event time, or effective time.

### IHR-B09 — Replay and retry overlap

An admitted, unconsumed act redelivered after a processor crash satisfies both
definitions:

~~~text
Replay:
  reuse of the same admitted act

Retry:
  repeated delivery or processing attempt for one event identity
~~~

### IHR-B10 — Policy supersession leaks into grant currentness

Excluding a superseded policy from the current governing set does not establish
whether grants historically issued under that policy survive.

~~~text
PolicyCurrentExclusion
↛ GrantBasisFALSE
~~~

The exact source review also records Z1 through Z10. Those specimens are
replayed individually in section 20.

## 3. AUTHORIZED BOUNDARY AND NONCLAIMS

Authorized:

- repair the semantic mechanisms directly implicated by IHR-B01 through
  IHR-B10;
- add only the objects, relations, dependency edges, and outcome algebras
  necessary to make those repairs coherent;
- preserve stricter fail-closed laws that survived Repair 001;
- author this one noncanonical report artifact;
- publish only this artifact on the exact isolated branch.

Not authorized:

- creating or asserting a positive constitutional, Founder, human-origin, or
  institutional root;
- determining actual policy, root, context-source, time-source, event-identity,
  registry, corpus, or composition standing;
- defining a shared ontology beyond this candidate report;
- changing Gene, Foundation IR, AgentBridge, DATASELF, Notepad, ClaudeSELF,
  schema, implementation, runtime, deployment, or storage;
- adopting, ratifying, sealing, or canonizing this repair;
- independently reviewing this repair in the repair session.

~~~text
FoundNewProblem != AuthorityToRepairNewProblem
NamedDependency != StandingDependency
TypedObject != AdmittedObject
CompleteCandidateModel != PositiveRealWorldResult
~~~

## 4. SURVIVING REPAIR 001 LAW PRESERVED

The following surviving laws are retained without weakening:

~~~text
PathFALSE != QueryFALSE
PathTRUE != QueryTRUE

PolicyStanding != PolicyApplicability
HistoricalRecord != CurrentAssessment

AuthorityApplicability != MutationEligibility

Replay != LawfulReissuance
GrantUseState != AuthorizationActConsumption

NoFirstMatchAuthority
NoUnauthorizedMultiGrantUnion
NoInventedPositiveRoot
FailClosedOnUnresolvedComposition
~~~

Additional surviving non-collapse laws retained:

~~~text
Representation != HistoricalEvent
HistoricalEvent != StandingRecord
StandingRecord != CurrentAssessment
EvidenceReference != NegativePropositionAssessment

RootReference != RootStanding
RootStanding != RootApplicability
External != Independent
FounderLabeled != FounderOriginProven

SameText ↛ SameEvent
NewMessage ↛ NewAuthorization

AuthorityApplicabilityAssessment = TRUE
↛ MutationEligibilityDecision = ELIGIBLE
~~~

This repair narrows two Repair 001 phrasings that hostile review defeated:

~~~text
ExhaustiveNegativeProof
is replaced by
NegativeEvidenceSet
→ ExhaustivenessAssessment
→ NegativePropositionAssessment

q contains S
is replaced by
AuthorityQueryIdentity q
and separate EvaluationCoordinate(q, S, GraphBlueprintIdentity)
~~~

No surviving result is promoted to canonical law merely because it is
preserved here.

## 5. REPAIR-TIME SEMANTIC FOUNDATION

### 5.1 Primary semantic types

Bounded Repair 002 uses the same eight primary type classes as Repair 001. No
additional primary type class is needed:

~~~text
SOURCE_RECORD
HISTORICAL_EVENT
RESOLVED_BINDING
CURRENT_ASSESSMENT
STANDING_RECORD
POLICY_OR_RULE_RECORD
EVIDENCE_REFERENCE
DERIVED_VALUE
~~~

This is the minimum extension result:

~~~text
NEW_PRIMARY_TYPE_CLASSES = 0
NEW_OBJECTS_WITHIN_EXISTING_TYPES = REQUIRED
~~~

Every graph object has exactly one primary semantic type. A record, event,
binding, set, graph, or evidence reference never receives an assessment
disposition. Only a CURRENT_ASSESSMENT receives an outcome from its declared
outcome algebra.

### 5.2 Query and evaluation coordinates

The query identity no longer contains the snapshot or completed graph:

~~~text
AuthorityQueryIdentity q =
  identity(
    admitted_request_act_identity,
    principal_binding_identity,
    actor_binding_identity,
    governed_operation_binding_identity,
    governed_target_binding_identity,
    context_resolution_request_identity
  )

EvaluationCoordinate E =
  identity(
    q,
    EvaluationSnapshotIdentity S,
    DependencyGraphBlueprintIdentity G0
  )
~~~

The final evaluated graph identity G is attached to the result record after
evaluation. Neither q, S, G0, nor any assessment-node identity depends on G.

### 5.3 Outcome algebras

General proposition assessment:

~~~text
TRUE
FALSE
NOT_EVALUABLE
~~~

Applicability assessment:

~~~text
APPLICABLE
NOT_APPLICABLE
NOT_EVALUABLE
~~~

Closure assessment:

~~~text
CLOSED
NOT_CLOSED
NOT_EVALUABLE
~~~

Currentness assessment:

~~~text
CURRENT
NOT_CURRENT
NOT_EVALUABLE
~~~

Classification assessment:

~~~text
RETRY
REPLAY
LAWFUL_REISSUANCE
NEW_FIRST_DELIVERY
NOT_EVALUABLE
~~~

No result token is assigned to a set or binding. For example:

~~~text
GoverningPolicySet
does not become NOT_EVALUABLE.

GoverningPolicySetAssessment
may have disposition NOT_EVALUABLE.

EvaluationSnapshotIdentity
does not become NOT_EVALUABLE.

SnapshotConstructionAssessment
may have disposition NOT_EVALUABLE.
~~~

### 5.4 Fail-closed aggregation

At every semantic level:

~~~text
missing mandatory input
or stale mandatory input
or nonauthoritative mandatory input
or unresolved outcome-changing conflict
or incomplete required candidate domain
or relevant provenance cycle
→ affected assessment = NOT_EVALUABLE
~~~

FALSE requires a positively established negative proposition at the exact
semantic level. One path failure never becomes global absence. TRUE requires
all mandatory closure, standing, applicability, currentness, composition, and
acyclicity dependencies for the selected result.

## 6. IHR-B01 REPAIR — DISCOVERY-LAW META-CLOSURE

### FINDING

Discovery-law meta-closure is absent. A basis-candidate set can appear closed
relative to L1 while an independently standing L2 exposes an outcome-changing
permit.

### COUNTERMODEL

~~~text
L1 is standing and names C1.
C1 is empty.

L2 is standing and names C2.
C2 contains a valid permit.

L1-relative closure yields FALSE.
Complete-law evaluation yields TRUE or conflict.
~~~

### ROOT DEFECT

Repair 001 conflated five separate questions:

1. whether a discovery-law record exists;
2. whether the record has standing;
3. whether it applies to q;
4. whether the discovery-law candidate set is closed;
5. whether multiple applicable discovery laws compose or precede one another.

It also allowed basis closure relative to one chosen law without proving
closure over the admissible discovery-law set.

### REPAIR

The repair introduces a finite, explicit governance-boundary input:

~~~text
GovernanceBoundaryRecord B0
  identifies:
    governed authority class
    governed jurisdiction set
    admissible discovery-law registries
    admissible policy-selection-law registries
    admissible root registries
    corpus namespace domain
    effective interval
    registry epochs
    boundary digest

GovernanceBoundaryAdmissionAssessment(B0, S)
  establishes whether B0 may be relied upon.
~~~

B0 is not discovered or validated by any law contained inside B0. Its
admission must terminate through an independently standing predecessor or an
applicable RootResolutionBundle. This artifact supplies neither. If that
external path is absent or cyclic, the boundary admission assessment is
NOT_EVALUABLE and discovery stops.

This is the exact termination boundary:

~~~text
INSIDE_BOUNDARY:
  finite discovery-law enumeration
  standing assessment
  currentness assessment
  applicability assessment
  law-set closure
  law composition

AT_BOUNDARY:
  GovernanceBoundaryAdmissionAssessment

OUTSIDE_BOUNDARY:
  independently standing predecessor
  or applicable RootResolutionBundle

IF OUTSIDE PATH IS UNRESOLVED:
  do not search for another meta-law
  do not assert closure
  return NOT_EVALUABLE
~~~

The evaluator performs this finite construction:

~~~text
DiscoveryLawRegistrySnapshot(B0, S)
→ DiscoveryLawRegistryCurrentnessAssessment
→ DiscoveryLawCandidateSet
→ DiscoveryLawCandidateSetClosureAssessment

for each DiscoveryLawRecord L:
  DiscoveryLawStandingAssessment(L, S)
  DiscoveryLawCurrentnessAssessment(L, S)
  DiscoveryLawApplicabilityAssessment(L, q, S)

all standing + current + applicable laws
→ DiscoveryLawCompositionAssessment
→ combined AuthorityBasisCandidateSet
→ BasisSetClosureAssessment
~~~

The combined candidate set is not a first-match result. All standing,
applicable discovery laws contribute, subject only to a separately standing,
current, applicable DiscoveryLawCompositionRuleRecord. If discovery laws
conflict about exclusions, corpus ownership, or domain coverage and the
composition rule cannot resolve that conflict, the law composition assessment
is NOT_EVALUABLE.

Law-set closure and basis-set closure remain distinct:

~~~text
DiscoveryLawCandidateSetClosureAssessment
  asks whether every admissible discovery law was considered.

BasisSetClosureAssessment
  asks whether every outcome-changing authority basis was considered
  under the resolved discovery-law composition.
~~~

An empty basis result may participate in query FALSE only when both closures
are CLOSED and the negative-assessment chain in section 16 resolves.

### NEW OBJECTS / RELATIONS

New objects:

- GovernanceBoundaryRecord;
- GovernanceBoundaryAdmissionEvent;
- GovernanceBoundaryStandingRecord;
- GovernanceBoundaryStandingAssessment;
- GovernanceBoundaryCurrentnessAssessment;
- GovernanceBoundaryApplicabilityAssessment;
- GovernanceBoundaryAdmissionAssessment;
- DiscoveryLawRegistrySnapshot;
- DiscoveryLawRegistryCurrentnessAssessment;
- DiscoveryLawRecord;
- DiscoveryLawCandidateSet;
- DiscoveryLawCandidateSetClosureAssessment;
- DiscoveryLawStandingAssessment;
- DiscoveryLawCurrentnessAssessment;
- DiscoveryLawApplicabilityAssessment;
- DiscoveryLawIdentityResolutionAssessment;
- DiscoveryLawCompositionRuleRecord;
- DiscoveryLawCompositionRuleStandingAssessment;
- DiscoveryLawCompositionRuleCurrentnessAssessment;
- DiscoveryLawCompositionRuleApplicabilityAssessment;
- DiscoveryLawCompositionAssessment;
- AuthorityBasisIdentityResolutionAssessment.

New relations:

~~~text
boundary admits registry
registry enumerates candidate laws
candidate-set closure precedes law selection/composition
record standing is assessed separately
record applicability is assessed separately
all applicable laws contribute before basis closure
boundary standing cannot be supplied by an enclosed law
~~~

### NEW DEPENDENCIES

- exact governance-boundary identity and digest;
- independently standing boundary-admission path;
- current registry epoch and coverage statement;
- standing/current/applicable composition rule when multiple law effects
  require composition;
- explicit exclusion proof for any admissible law omitted as irrelevant.

These dependencies are not claimed resolved by this artifact.

### WHY COUNTERMODEL NOW FAILS

If B0 closes over both L1 and L2, both laws are evaluated. C2 and its permit
cannot be omitted merely because L1 produced an empty C1. The combined result
contains the permit or an explicit unresolved conflict; it cannot lawfully be
FALSE from L1 alone.

If L2 is omitted from the registry, the discovery-law set is not CLOSED unless
an independently standing boundary proves L2 outside the admissible domain or
irrelevant. Without that proof, the result is NOT_EVALUABLE.

If B0 itself lacks independent admission, evaluation terminates at the
declared boundary with NOT_EVALUABLE. It does not recurse indefinitely and
does not invent a positive meta-root.

### NEW ATTACK SURFACE

- a forged or stale GovernanceBoundaryRecord could falsely shrink the law
  universe;
- two independently standing boundaries could conflict;
- a composition law could depend on the law set it composes;
- registry aliasing could hide a distinct discovery law.

All four surfaces fail closed through boundary currentness, identity,
standing, closure, and cycle assessment. Cross-boundary federation remains an
unresolved root, not a repaired fact.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 7. IHR-B06 REPAIR — AUTHORITATIVE CONTEXT RESOLUTION

### FINDING

Caller-controlled context could change authority without a typed authoritative
context source, currentness assessment, applicability assessment, or semantic
owner.

### COUNTERMODEL

~~~text
actual environment = production
caller ContextClaim = sandbox
grant permits sandbox only

caller-selected context would yield a permit
~~~

### ROOT DEFECT

Repair 001 placed context_binding inside q without defining:

- whether the value was a claim or resolved binding;
- who semantically owned resolution;
- which source had standing;
- whether the source was current;
- whether it applied to the target/operation;
- how conflicts were resolved.

### REPAIR

The semantic owner is named:

~~~text
AUTHORITATIVE_CONTEXT_RESOLUTION_INTERFACE
~~~

This is an upstream semantic ownership boundary, not an implementation,
service, storage, network, or deployment choice. It supplies context facts and
bindings. It must not supply authority applicability.

The repair distinguishes:

~~~text
ContextClaim
  caller or source assertion
  SOURCE_RECORD

ContextSource
  exact source record from which context facts are obtained
  SOURCE_RECORD

ContextSourceStandingRecord
  recognized source standing
  STANDING_RECORD

ContextBinding
  resolved environment/jurisdiction/tenant/safety-domain identity
  RESOLVED_BINDING

ContextCurrentnessAssessment
  whether the bound facts remain current at S
  CURRENT_ASSESSMENT

ContextApplicabilityAssessment
  whether the source and binding apply to q
  CURRENT_ASSESSMENT
~~~

Context resolution proceeds:

~~~text
ContextResolutionRequest(q0)
+ all ContextClaim objects
+ ContextSourceCandidateSet
+ ContextSourceCandidateSetClosureAssessment
+ each ContextSourceStandingAssessment
+ each ContextSourceCurrentnessAssessment
+ each ContextSourceApplicabilityAssessment
+ standing ContextResolutionRuleRecord path
→ ContextResolutionAssessment
→ ContextBinding
~~~

A caller ContextClaim is evidence only. It can influence ContextBinding solely
when a standing, current, applicable context-resolution rule authorizes that
source for the exact dimension. A caller cannot select the rule or elevate its
own claim.

The authoritative source may differ by dimension. For example, environment,
tenant, jurisdiction, and target custody may come from distinct standing
sources. Composition requires a separately standing ContextCompositionRule.
Unresolved conflict is not resolved by source order, lexical specificity, or
caller preference.

The query identity uses the identity of the context-resolution request. The
resolved ContextBinding is added to ResolvedQueryCore before snapshot
construction. If no binding can be lawfully constructed,
ContextResolutionAssessment is NOT_EVALUABLE and q is not finalized.

### NEW OBJECTS / RELATIONS

New objects:

- ContextClaim;
- ContextSource;
- ContextSourceCandidateSet;
- ContextSourceIdentityResolutionAssessment;
- ContextSourceCandidateSetClosureAssessment;
- ContextSourceStandingRecord;
- ContextSourceStandingAssessment;
- ContextSourceCurrentnessAssessment;
- ContextSourceApplicabilityAssessment;
- ContextResolutionRuleRecord;
- ContextResolutionRuleStandingAssessment;
- ContextResolutionRuleCurrentnessAssessment;
- ContextResolutionRuleApplicabilityAssessment;
- ContextCompositionRuleRecord;
- ContextCompositionRuleStandingAssessment;
- ContextCompositionRuleCurrentnessAssessment;
- ContextCompositionRuleApplicabilityAssessment;
- ContextResolutionAssessment;
- ContextBinding;
- ContextCurrentnessAssessment;
- ContextApplicabilityAssessment.

New relations:

~~~text
caller claim is evidence only
standing source supplies candidate fact
source currentness and applicability precede binding
standing resolution/composition rules control conflicts
resolved binding participates in q
context never supplies authority by itself
~~~

### NEW DEPENDENCIES

- context-source candidate closure;
- independent source standing;
- source and binding currentness;
- query-relative applicability;
- standing resolution and composition rules;
- dimension-consistency and conflict resolution.

### WHY COUNTERMODEL NOW FAILS

The sandbox ContextClaim cannot become ContextBinding merely because the
caller supplied it. The standing authoritative production source is evaluated.
If it resolves production, the sandbox-only grant path is NOT_APPLICABLE or
FALSE according to its scope law. If source standing, closure, or conflict is
unresolved, the context assessment and query are NOT_EVALUABLE. The caller
cannot force a permit.

### NEW ATTACK SURFACE

- authoritative sources may disagree by observation time;
- a source may be standing for one context dimension but not another;
- target movement can stale a previously valid binding;
- a context-resolution rule may depend on the authority result.

The first three require current query-relative assessment. The fourth is a
relevant provenance cycle and yields NOT_EVALUABLE.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 8. IHR-B07 REPAIR — ACYCLIC q / S / G CONSTRUCTION

### FINDING

q contained S, S contained q and G, and G contained assessments over q and S.
No identity could be completed without its own completed identity.

### COUNTERMODEL

~~~text
q contains S
S contains q and G
G contains assessments over q@S

implementation A allocates q first
implementation B allocates G first
both appear permitted
~~~

### ROOT DEFECT

Repair 001 collapsed:

- query subject identity;
- evaluation coordinate;
- snapshot seed;
- graph structure;
- evaluated graph record.

It also used final graph identity as an input to identities that the graph
itself was required to evaluate.

### REPAIR

The construction is acyclic and phase-ordered.

#### Phase 0 — immutable input capture

Capture:

~~~text
InputCaptureBatch I0
  admitted request occurrence reference
  candidate source references
  observation boundary
  evaluation nonce
  B0 candidate reference
~~~

I0 does not contain q, S, G0, G, or any assessment result.

#### Phase 1 — pre-query coordinates

Construct:

~~~text
QueryDraft q0
  request-act candidate identity
  claimed actor/principal coordinates
  governed operation reference
  governed target reference
  context-resolution request identity
~~~

q0 has no snapshot or graph identity.

#### Phase 2 — binding resolution

Resolve:

~~~text
AdmittedRequestActIdentity
PrincipalBinding
ActorBinding
OperationBinding
TargetBinding
ContextBinding
~~~

The corresponding construction assessments receive dispositions. Successful
bindings form ResolvedQueryCore Q1.

#### Phase 3 — query identity

Construct:

~~~text
AuthorityQueryIdentity q =
  identity(Q1 exact binding identities)
~~~

q has no S, G0, G, or assessment result.

#### Phase 4 — snapshot seed

Construct:

~~~text
SnapshotSeed S0 =
  identity(
    q,
    B0 identity,
    source and registry epoch observations,
    time-evidence identities,
    observation boundary,
    freshness-policy references
  )
~~~

S0 does not contain G0, G, or evaluated node results.

#### Phase 5 — dependency graph blueprint

Using only q, S0, the frozen type table, standing dependency templates, and
candidate identity references, construct:

~~~text
DependencyGraphBlueprint GB
DependencyGraphBlueprintIdentity G0 = identity(canonical structure of GB)
~~~

GB contains node kinds, dependency edge kinds, and candidate references. It
does not contain completed assessment results or final graph identity G.

#### Phase 6 — snapshot identity

Construct:

~~~text
EvaluationSnapshotIdentity S =
  identity(
    S0,
    G0,
    reconciled time binding,
    exact bound source/registry epochs
  )
~~~

SnapshotConstructionAssessment decides whether S may be constructed. S itself
never receives NOT_EVALUABLE.

#### Phase 7 — assessment-node identities

For each blueprint node in topological order:

~~~text
AssessmentNodeIdentity N =
  identity(
    node kind,
    q,
    S,
    G0,
    subject identity,
    ordered dependency-node identities
  )
~~~

No node identity includes its own result or G.

Before evaluation:

- GraphTypeClosureAssessment confirms every node has one table type;
- GraphEdgeClosureAssessment confirms every mandatory edge exists;
- GraphAcyclicityAssessment detects strongly connected components;
- GraphCandidateCoverageAssessment confirms candidate branches are represented.

A relevant cycle prevents evaluation. Only an independently sufficient
selected acyclic subgraph may be called a proof DAG, and only after standing
composition proves every omitted cyclic candidate outcome-irrelevant.

#### Phase 8 — evaluation and final graph record

Evaluate nodes in dependency order. Then construct:

~~~text
AuthorityDependencyGraph G
AuthorityDependencyGraphIdentity =
  identity(
    G0,
    ordered node identities,
    ordered edge identities,
    assessment-result record identities
  )
~~~

Finally construct:

~~~text
AuthorityEvaluationRecord
  binds q
  binds S
  binds G
  binds AuthorityApplicabilityAssessment result
~~~

G is an output witness. It is not retroactively inserted into q or S.

#### Exact construction trace

~~~text
I0
→ q0
→ binding construction assessments
→ Q1
→ q
→ S0
→ GB
→ G0
→ SnapshotConstructionAssessment
→ S
→ assessment-node identities
→ graph closure + acyclicity assessments
→ ordered assessment results
→ G
→ AuthorityEvaluationRecord
~~~

There is no reverse identity edge.

### NEW OBJECTS / RELATIONS

New objects:

- InputCaptureBatch;
- QueryDraft;
- QueryBindingConstructionAssessment;
- ResolvedQueryCore;
- AuthorityQueryIdentity;
- SnapshotSeed;
- DependencyGraphBlueprint;
- DependencyGraphBlueprintIdentity;
- SnapshotConstructionAssessment;
- EvaluationSnapshotIdentity;
- AssessmentNodeIdentity;
- GraphTypeClosureAssessment;
- GraphEdgeClosureAssessment;
- GraphCandidateCoverageAssessment;
- GraphAcyclicityAssessment;
- SelectedAcyclicProofSubgraph;
- AuthorityDependencyGraph;
- AuthorityDependencyGraphIdentity;
- AuthorityEvaluationRecord.

New relations:

~~~text
identity phases are strictly ordered
blueprint precedes snapshot identity
snapshot precedes assessment-node identity
assessment results precede final graph identity
final graph is output-only for current evaluation
~~~

### NEW DEPENDENCIES

- deterministic identity function and canonical structural encoding;
- frozen type table and dependency templates;
- stable observation boundary and registry epochs;
- cycle detection before result use;
- selected-subgraph sufficiency under independently standing composition.

The identity algorithm and storage encoding are implementation questions and
are not selected here.

### WHY COUNTERMODEL NOW FAILS

Neither implementation may allocate q, S, or G in an arbitrary order. q is
complete before S0; G0 is structural and complete before S; G is constructed
only after all assessments. q and S never contain G, and G does not determine
their identities. Any implementation using the old recursive shape violates
the declared construction order and cannot produce an admitted evaluation
record.

### NEW ATTACK SURFACE

- nondeterministic canonical encoding could yield divergent G0 identities;
- a candidate discovered after GB freeze could stale S;
- a graph template could omit an outcome-changing node;
- a post-evaluation record could be confused with a pre-evaluation blueprint.

The semantic response is explicit identity separation and reconstruction on
staleness. Concrete canonicalization and runtime enforcement remain outside
this repair.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 9. IHR-B08 REPAIR — REVOCATION AUTHORITY AND TIME

### FINDING

The REVOKE_GRANT authority subquery was absent from the graph, and equal-time
self-revocation could be evaluated against incompatible pre-state or
post-state assumptions.

### COUNTERMODEL

~~~text
Grant G is A's only authority to revoke G.
Revocation R is issued and effective at the same instant.

pre-state:
  R authorized
  G revoked

post-state:
  A unauthorized
  R invalid
~~~

### ROOT DEFECT

Repair 001 distinguished several revocation objects but did not:

- represent RevocationAct as the admitted authority-bearing act;
- include the complete RevocationAuthorityAssessment subquery;
- bind effective time separately from observation time;
- identify the state against which revocation authority is evaluated;
- require a standing equal-time/pre-state law.

### REPAIR

The revocation chain is:

~~~text
RevocationRepresentation
→ RevocationActAdmissionAssessment
→ RevocationAct
→ RevocationStandingAssessment
→ RevocationStandingRecord
→ RevocationEffectiveTimeBinding
→ RevocationObservationTimeBinding
→ RevocationTemporalOrderingAssessment
→ RevocationAuthorityStateSelectionAssessment
→ RevocationAuthorityAssessment
→ CurrentRevocationAssessment
~~~

RevocationAct is a HISTORICAL_EVENT with its own semantic event identity,
actor attribution, exact target grant, revoked dimensions, asserted effective
time, and provenance. The representation does not prove the act or its
standing.

RevocationAuthorityAssessment is a complete authority subquery:

~~~text
operation:
  REVOKE_GRANT

actor:
  exact revocation actor binding

target:
  exact grant identity and exact portion

context:
  authoritative context binding

evaluation state:
  the state selected by
  RevocationAuthorityStateSelectionAssessment

snapshot:
  a historical snapshot bound to that selected state
~~~

State selection requires:

~~~text
RevocationStateSelectionRuleRecord
→ RevocationStateSelectionRuleStandingAssessment
→ RevocationStateSelectionRuleCurrentnessAssessment
→ RevocationStateSelectionRuleApplicabilityAssessment
→ RevocationAuthorityStateSelectionAssessment
~~~

Possible selected states are:

~~~text
IMMEDIATE_PRE_STATE
EVENT_STATE
IMMEDIATE_POST_STATE
OTHER_EXPLICITLY_DEFINED_STATE
NOT_EVALUABLE
~~~

No state is selected by intuition. In particular, equal event/effective times
do not imply pre-state evaluation.

RevocationTemporalOrderingAssessment separately compares:

- act occurrence time;
- asserted effective time;
- standing effective time;
- observation time;
- selected authority-state boundary;
- query snapshot time.

It consumes a standing temporal-order rule. Time-source disagreement crossing
any relevant boundary yields NOT_EVALUABLE.

CurrentRevocationAssessment may establish current effect only when:

- RevocationAct is admitted;
- RevocationStandingAssessment resolves;
- RevocationAuthorityAssessment is TRUE at the lawfully selected state;
- effective-time and observation-time bindings resolve;
- temporal ordering resolves;
- target and revoked dimensions resolve;
- current policy, conflict, and survivorship dependencies resolve.

Equal-time rule unresolved:

~~~text
RevocationAuthorityStateSelectionAssessment = NOT_EVALUABLE
→ RevocationAuthorityAssessment = NOT_EVALUABLE
→ CurrentRevocationAssessment = NOT_EVALUABLE
→ outcome-changing GrantCurrentnessAssessment = NOT_EVALUABLE
~~~

### NEW OBJECTS / RELATIONS

New objects:

- RevocationActAdmissionAssessment;
- RevocationAct;
- RevocationStandingAssessment;
- RevocationStandingRecord;
- RevocationEffectiveTimeBinding;
- RevocationObservationTimeBinding;
- RevocationTemporalOrderRuleRecord;
- RevocationTemporalOrderRuleStandingAssessment;
- RevocationTemporalOrderRuleCurrentnessAssessment;
- RevocationTemporalOrderRuleApplicabilityAssessment;
- RevocationTemporalOrderingAssessment;
- RevocationStateSelectionRuleRecord;
- RevocationStateSelectionRuleStandingAssessment;
- RevocationStateSelectionRuleCurrentnessAssessment;
- RevocationStateSelectionRuleApplicabilityAssessment;
- RevocationAuthorityStateSelectionAssessment;
- RevocationAuthorityAssessment;
- CurrentRevocationAssessment.

New relations:

~~~text
act admission precedes standing
state-selection law precedes revocation authority
revocation authority is a complete historical subquery
effective time differs from observation time
temporal ordering precedes current effect
~~~

### NEW DEPENDENCIES

- semantic event identity and source admission for RevocationAct;
- actor, operation, target, and context bindings;
- standing revocation state-selection law;
- standing temporal-order law;
- historical snapshot at the selected state;
- closed authority basis for REVOKE_GRANT;
- current revocation policy, conflict, and survivorship rules.

### WHY COUNTERMODEL NOW FAILS

The evaluator cannot choose pre-state or post-state by implementation
convenience. If an independently standing applicable state-selection law names
IMMEDIATE_PRE_STATE, the pre-state result is evaluated. If it names another
state, that state is evaluated. If the law or its standing path is unresolved,
the result is deterministically NOT_EVALUABLE. Both contradictory outcomes can
no longer be asserted from the same unresolved input.

### NEW ATTACK SURFACE

- retroactive effective time may precede act occurrence;
- two time sources may order equal-time boundaries differently;
- the state-selection rule may depend on the revocation it governs;
- a revocation may target the rule that establishes its own authority.

These require explicit temporal, standing, and cycle assessment. No default
retroactivity or self-revocation rule is introduced.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 10. IHR-B09 REPAIR — RETRY / REPLAY DISJOINTNESS

### FINDING

The same admitted, unconsumed act redelivered after a crash satisfied both the
Repair 001 replay and retry definitions.

### COUNTERMODEL

~~~text
Act A admitted.
Processing crashes before consumption.
Same event redelivered.

reuse of admitted act → Replay
repeated delivery of one event identity → Retry
~~~

### ROOT DEFECT

Repair 001 used admission status and redelivery alone. It did not distinguish:

- semantic event identity;
- delivery identity;
- processing-attempt identity;
- admission identity;
- terminal processing state;
- consumption state;
- intent to obtain an additional reliance.

### REPAIR

The event boundary uses five independent identities:

~~~text
SemanticEventIdentity E
  identity of the meaning-bearing occurrence

DeliveryIdentity D
  identity of one transport delivery carrying a representation of E

ProcessingAttemptIdentity P
  identity of one processing attempt over D/E

AdmissionIdentity A
  identity of one standing admission decision for E as an act

AuthorizationActConsumptionStateAssessment C
  current state of reliance consumption for A
~~~

Lexical equality is evidence only:

~~~text
SameText
↛ SameSemanticEvent

DifferentText
↛ DifferentSemanticEvent
~~~

Classification is deterministic when identities and state resolve.

Retry:

~~~text
same SemanticEventIdentity E
same AdmissionIdentity A
new DeliveryIdentity D or ProcessingAttemptIdentity P
no new admission claimed
prior processing state is NONTERMINAL
consumption state is UNCONSUMED
standing retry-admission law permits continuation
→ RETRY
~~~

Replay:

~~~text
same SemanticEventIdentity E
and same or aliased AdmissionIdentity A
and one of:
  terminal consumption already occurred
  terminal completion already occurred
  terminal rejection already occurred and re-admission is prohibited
  presentation seeks an additional authorization reliance
  presentation falsely claims a new admission for the same nonreissuable event
→ REPLAY
~~~

Replay is therefore narrower than redelivery. Redelivery before a known
terminal boundary is not replay.

Lawful reissuance:

~~~text
new SemanticEventIdentity E2
new historical authorization occurrence
new AdmissionIdentity A2
new actor attribution
new authority assessment
new policy and snapshot assessment
→ may classify as LAWFUL_REISSUANCE
~~~

A new delivery or new message alone cannot establish E2.

If E, A, terminal state, or consumption state is unresolved:

~~~text
EventReuseClassificationAssessment = NOT_EVALUABLE
~~~

It is never simultaneously RETRY and REPLAY.

Crash boundaries:

| Observed durable state | Classification |
|---|---|
| Admission durable; no terminal result; consumption durably UNCONSUMED | RETRY, if standing retry law permits |
| Consumption durable; acknowledgement absent | REPLAY on redelivery |
| Terminal state and consumption durability disagree | NOT_EVALUABLE |
| Admission identity unresolved | NOT_EVALUABLE |
| New event and admission independently established | LAWFUL_REISSUANCE candidate |

Grant intrinsic use remains separate:

~~~text
GrantUseStateAssessment
!= AuthorizationActConsumptionStateAssessment
~~~

### NEW OBJECTS / RELATIONS

New objects:

- SemanticEventIdentity;
- SemanticEventIdentityResolutionAssessment;
- DeliveryIdentity;
- ProcessingAttemptIdentity;
- AdmissionAct;
- AdmissionIdentity;
- AdmissionIdentityResolutionAssessment;
- AdmissionStandingRecord;
- AdmissionCurrentnessAssessment;
- ProcessingTerminalStateAssessment;
- AuthorizationActConsumptionRecord;
- AuthorizationActConsumptionStateAssessment;
- RetryAdmissionRuleRecord;
- RetryAdmissionRuleStandingAssessment;
- RetryAdmissionRuleCurrentnessAssessment;
- RetryAdmissionRuleApplicabilityAssessment;
- EventReuseClassificationAssessment.

New relations:

~~~text
delivery carries event representation
processing attempt consumes a delivery
admission binds semantic event
consumption state binds admission reliance
classification consumes all five identities/states
reissuance requires new event and new admission
~~~

### NEW DEPENDENCIES

- authoritative semantic event identity resolution;
- delivery and processing-attempt identity;
- authoritative admission identity;
- durable terminal and consumption-state assessment;
- standing retry-admission rule;
- alias resolution across representations and admissions.

### WHY COUNTERMODEL NOW FAILS

The crash occurs before terminal consumption. The same E and A are redelivered
under a new D/P while durable consumption is UNCONSUMED. Under a standing retry
law, the classification is RETRY and cannot be REPLAY. If durable state is
uncertain, the classification is NOT_EVALUABLE, not both.

### NEW ATTACK SURFACE

- a crash may occur between consumption persistence and acknowledgement;
- two stores may disagree on terminal state;
- an attacker may forge a new admission identity for the same E;
- semantic event aliasing may be unresolved.

These surfaces are exposed rather than guessed. Runtime atomicity and storage
design remain outside this semantic repair.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 11. COMPLETE REPAIR-TIME GRAPH NODE / TYPE TABLE

This table is closed over the graph in section 17 and the construction trace in
section 18. Every named graph node has exactly one row and one primary semantic
type. No alias is a second object.

Outcome algebra abbreviations apply only to CURRENT_ASSESSMENT rows:

| Code | Outcome algebra |
|---|---|
| PROP | TRUE, FALSE, NOT_EVALUABLE |
| APP | APPLICABLE, NOT_APPLICABLE, NOT_EVALUABLE |
| CLOSE | CLOSED, NOT_CLOSED, NOT_EVALUABLE |
| CURRENT | CURRENT, NOT_CURRENT, NOT_EVALUABLE |
| ADMIT | ADMITTED, REJECTED, NOT_EVALUABLE |
| RESOLVE | RESOLVED, CONFLICT_UNRESOLVED, NOT_EVALUABLE |
| EXHAUST | EXHAUSTIVE, NON_EXHAUSTIVE, NOT_EVALUABLE |
| PATH | TRUE, FALSE, NOT_EVALUABLE |
| QUERY | TRUE, FALSE, NOT_EVALUABLE |
| SPECIAL | Exact finite algebra named in the role column |

### 16.1 Construction, identity, time, and graph nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| InputCaptureBatch | DERIVED_VALUE | — | Immutable references captured before construction |
| QueryDraft | DERIVED_VALUE | — | Pre-binding query coordinates without S or G |
| AdmittedRequestAct | HISTORICAL_EVENT | — | Admitted request occurrence |
| AdmittedRequestActIdentity | RESOLVED_BINDING | — | Identity binding for the request occurrence |
| QueryBindingConstructionAssessment | CURRENT_ASSESSMENT | RESOLVE | Decides whether mandatory q bindings can be constructed |
| PrincipalBinding | RESOLVED_BINDING | — | Exact principal identity for q |
| ActorBinding | RESOLVED_BINDING | — | Exact event-specific actor identity for q |
| OperationBinding | RESOLVED_BINDING | — | Exact governed operation identity/version |
| TargetBinding | RESOLVED_BINDING | — | Exact governed target identity/revision |
| ResolvedQueryCore | DERIVED_VALUE | — | Complete successful binding tuple |
| AuthorityQueryIdentity | RESOLVED_BINDING | — | Identity of Q1, excluding S and G |
| EvaluationTimeEvidence | EVIDENCE_REFERENCE | — | Time observations used at the boundary |
| TimeSourceStandingRecord | STANDING_RECORD | — | Recognized time source |
| TimeSourceStandingAssessment | CURRENT_ASSESSMENT | PROP | Current standing of a time source |
| TimeReconciliationRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for reconciling standing time sources |
| TimeReconciliationRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of time reconciliation rule |
| TimeReconciliationRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of time reconciliation rule |
| TimeReconciliationRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of time reconciliation rule |
| FreshnessRuleRecord | POLICY_OR_RULE_RECORD | — | Rule defining freshness for an input class |
| FreshnessRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of freshness rule |
| FreshnessRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of freshness rule |
| FreshnessRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of freshness rule |
| TimeFreshnessAssessment | CURRENT_ASSESSMENT | CURRENT | Freshness of time evidence |
| TimeSourceReconciliationAssessment | CURRENT_ASSESSMENT | RESOLVE | Reconciles time sources under standing law |
| ReconciledEvaluationTimeBinding | RESOLVED_BINDING | — | Bound evaluation time and tolerance |
| SnapshotSeed | DERIVED_VALUE | — | Pre-graph snapshot seed S0 |
| DependencyGraphBlueprint | DERIVED_VALUE | — | Structural node/edge plan without results |
| DependencyGraphBlueprintIdentity | RESOLVED_BINDING | — | Identity G0 of the canonical blueprint |
| SnapshotConstructionAssessment | CURRENT_ASSESSMENT | RESOLVE | Decides whether S can be constructed |
| EvaluationSnapshotIdentity | RESOLVED_BINDING | — | Final snapshot identity S |
| AssessmentNodeIdentity | RESOLVED_BINDING | — | Identity of one assessment node |
| GraphTypeClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Confirms every node has one table type |
| GraphEdgeClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Confirms all mandatory dependencies exist |
| GraphCandidateCoverageAssessment | CURRENT_ASSESSMENT | CLOSE | Confirms all outcome-changing candidates are graphed |
| GraphAcyclicityAssessment | CURRENT_ASSESSMENT | SPECIAL | ACYCLIC, RELEVANT_CYCLE, NOT_EVALUABLE |
| SelectedAcyclicProofSubgraph | DERIVED_VALUE | — | Selected sufficient acyclic graph after relevance law |
| ProvenanceCycleAssessment | CURRENT_ASSESSMENT | SPECIAL | IRRELEVANT, RELEVANT, NOT_EVALUABLE |
| AuthorityDependencyGraph | DERIVED_VALUE | — | Completed evaluated graph G |
| AuthorityDependencyGraphIdentity | RESOLVED_BINDING | — | Post-evaluation identity of G |
| AuthorityApplicabilityAssessment | CURRENT_ASSESSMENT | QUERY | Final q-at-S authority disposition |
| AuthorityEvaluationRecord | SOURCE_RECORD | — | Output record binding q, S, G, and AA result reference |

### 16.2 Governance boundary and discovery-law nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| GovernanceBoundaryRecord | POLICY_OR_RULE_RECORD | — | Finite admissible governance boundary B0 |
| GovernanceBoundaryAdmissionEvent | HISTORICAL_EVENT | — | Historical admission occurrence for B0 |
| GovernanceBoundaryStandingRecord | STANDING_RECORD | — | Recognized standing record for B0 |
| GovernanceBoundaryStandingAssessment | CURRENT_ASSESSMENT | PROP | Current standing of B0 without self-validation |
| GovernanceBoundaryCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of B0 and its effective interval |
| GovernanceBoundaryApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of B0 to q authority class/jurisdiction |
| GovernanceBoundaryAdmissionAssessment | CURRENT_ASSESSMENT | ADMIT | Independent admission of B0 |
| DiscoveryLawRegistrySnapshot | DERIVED_VALUE | — | Bound discovery-law registry epoch |
| DiscoveryLawRegistryCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Registry epoch currentness |
| DiscoveryLawRecord | POLICY_OR_RULE_RECORD | — | One authority-basis discovery law |
| DiscoveryLawCandidateSet | DERIVED_VALUE | — | All admissible discovery-law identities |
| DiscoveryLawIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves law aliases without digest collapse |
| DiscoveryLawCandidateSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Closure over discovery laws |
| DiscoveryLawStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of one discovery law |
| DiscoveryLawCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of one discovery law |
| DiscoveryLawApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of one discovery law to q |
| DiscoveryLawCompositionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for composing applicable discovery laws |
| DiscoveryLawCompositionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of discovery-law composition rule |
| DiscoveryLawCompositionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of discovery-law composition rule |
| DiscoveryLawCompositionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of discovery-law composition rule |
| DiscoveryLawCompositionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves effects of all applicable discovery laws |
| AuthorityRecordCorpusSnapshot | DERIVED_VALUE | — | Bound authority-record corpus epochs |
| AuthorityRecordCorpusCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Corpus epoch currentness |
| AuthorityBasisDiscoveryAssessment | CURRENT_ASSESSMENT | RESOLVE | Discovers basis candidates under all resolved laws |
| AuthorityBasisCandidateSet | DERIVED_VALUE | — | Exact candidate basis identities |
| AuthorityBasisIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves basis aliases and distinct issuance events |
| BasisSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Closure over outcome-changing basis candidates |
| AuthorityBasisCandidate | DERIVED_VALUE | — | One typed basis reference |
| BasisPathAssessment | CURRENT_ASSESSMENT | PATH | Disposition of one exact basis path |
| AuthorityBasisCompositionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for query-level basis composition |
| AuthorityBasisCompositionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of basis composition rule |
| AuthorityBasisCompositionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of basis composition rule |
| AuthorityBasisCompositionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of basis composition rule |
| AuthorityBasisCompositionAssessment | CURRENT_ASSESSMENT | RESOLVE | Composes all evaluated basis effects |

### 16.3 Root nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| RootRegistrySnapshot | DERIVED_VALUE | — | Bound root-registry epochs |
| RootRegistryCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of root registry |
| RootReference | EVIDENCE_REFERENCE | — | Exact proposed root reference |
| RootAdmissionEvent | HISTORICAL_EVENT | — | Historical root-admission occurrence |
| RootStandingRecord | STANDING_RECORD | — | Recognized root-standing record |
| RootStandingAssessment | CURRENT_ASSESSMENT | PROP | Current root standing |
| RootCandidateDiscoveryAssessment | CURRENT_ASSESSMENT | RESOLVE | Discovers roots admissible under B0 |
| RootCandidateSet | DERIVED_VALUE | — | Exact root candidates for required edge |
| RootIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves root aliases and distinct admission events |
| RootCandidateSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Root-candidate-set closure |
| RootControlDomain | DERIVED_VALUE | — | Candidate controllers and dependencies of a root |
| RootControlEvidence | EVIDENCE_REFERENCE | — | Evidence of root control/dependency relations |
| RootControlDefinitionRuleRecord | POLICY_OR_RULE_RECORD | — | Defines controlling relations for the required edge |
| RootControlDefinitionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of control-definition rule |
| RootControlDefinitionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of control-definition rule |
| RootControlDefinitionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of control-definition rule |
| RootControlDomainDiscoveryAssessment | CURRENT_ASSESSMENT | RESOLVE | Discovers root control relations |
| IndependenceDomainClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Closure over the root control domain |
| RootIndependenceAssessment | CURRENT_ASSESSMENT | PROP | Independence after domain closure |
| RootApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Root applicability to exact required edge |
| RootConflictRuleRecord | POLICY_OR_RULE_RECORD | — | Root conflict precedence/composition rule |
| RootConflictRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of root conflict rule |
| RootConflictRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of root conflict rule |
| RootConflictRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of root conflict rule |
| RootConflictResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves all applicable root effects |
| RootResolutionBundle | DERIVED_VALUE | — | References to fully assessed root components |
| RootResolutionBundleAssemblyAssessment | CURRENT_ASSESSMENT | RESOLVE | Decides whether a root bundle can be assembled |

### 16.4 Policy-selection and governing-policy nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| PolicySelectionLawRegistrySnapshot | DERIVED_VALUE | — | Bound policy-selection-law registry epoch |
| PolicySelectionLawRegistryCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Registry currentness |
| PolicySelectionLawRecord | POLICY_OR_RULE_RECORD | — | One policy-candidate selection law |
| PolicySelectionLawCandidateSet | DERIVED_VALUE | — | All admissible selection-law identities |
| PolicySelectionLawIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves selector aliases without record collapse |
| PolicySelectionLawCandidateSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Closure over selection laws |
| PolicySelectionLawStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of one selection law |
| PolicySelectionLawCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of one selection law |
| PolicySelectionLawApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of one selection law |
| PolicySelectionLawCompositionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for composing selection laws |
| PolicySelectionLawCompositionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of selector-composition rule |
| PolicySelectionLawCompositionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of selector-composition rule |
| PolicySelectionLawCompositionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of selector-composition rule |
| PolicySelectionLawCompositionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves effects of all applicable selection laws |
| PolicyCorpusSnapshot | DERIVED_VALUE | — | Bound governed-policy corpus epochs |
| PolicyCorpusCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Policy corpus currentness |
| PolicyCandidateDiscoveryAssessment | CURRENT_ASSESSMENT | RESOLVE | Discovers policies under resolved selection laws |
| PolicyCandidateSet | DERIVED_VALUE | — | Exact policy candidates |
| PolicyIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves policy aliases and distinct adoption events |
| PolicyCandidateSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Closure over policy candidates |
| PolicyRecord | POLICY_OR_RULE_RECORD | — | Exact policy identity/version/content |
| PolicyAdoptionEvent | HISTORICAL_EVENT | — | Policy adoption/amendment/withdrawal occurrence |
| PolicyAdoptionStandingRecord | STANDING_RECORD | — | Recognized adoption standing |
| PolicyAdoptionStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of adoption record |
| PolicyAdoptionAuthorityAssessment | CURRENT_ASSESSMENT | PROP | Actor authority at adoption snapshot |
| PolicyStandingAssessment | CURRENT_ASSESSMENT | PROP | Current governance standing, not q applicability |
| PolicyCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Current policy state |
| PolicyApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Query-relative policy applicability |
| PolicyCompositionRuleRecord | POLICY_OR_RULE_RECORD | — | Governing policy precedence/composition rule |
| PolicyCompositionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of policy composition rule |
| PolicyCompositionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of policy composition rule |
| PolicyCompositionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of policy composition rule |
| PolicyCompositionAssessment | CURRENT_ASSESSMENT | RESOLVE | Composes all standing applicable policies |
| GoverningPolicySet | DERIVED_VALUE | — | Resolved policy identities and composition |
| GoverningPolicySetAssessment | CURRENT_ASSESSMENT | RESOLVE | Decides whether the governing set is usable |

### 16.5 Context nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| ContextResolutionRequest | RESOLVED_BINDING | — | Identity of requested context dimensions |
| ContextClaim | SOURCE_RECORD | — | Caller or source context assertion |
| ContextSource | SOURCE_RECORD | — | Exact upstream context-source record |
| ContextSourceCandidateSet | DERIVED_VALUE | — | Candidate context-source identities |
| ContextSourceIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves source aliases and distinct observations |
| ContextSourceCandidateSetClosureAssessment | CURRENT_ASSESSMENT | CLOSE | Context-source closure |
| ContextSourceStandingRecord | STANDING_RECORD | — | Recognized source standing |
| ContextSourceStandingAssessment | CURRENT_ASSESSMENT | PROP | Current source standing |
| ContextSourceCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Source record currentness |
| ContextSourceApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Source applicability to q dimension |
| ContextResolutionRuleRecord | POLICY_OR_RULE_RECORD | — | Context-source selection/resolution rule |
| ContextResolutionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of context resolution rule |
| ContextResolutionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of context resolution rule |
| ContextResolutionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of context resolution rule |
| ContextCompositionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for composing context dimensions/sources |
| ContextCompositionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of context composition rule |
| ContextCompositionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of context composition rule |
| ContextCompositionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of context composition rule |
| ContextResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves source claims into a binding |
| ContextBinding | RESOLVED_BINDING | — | Authoritative resolved context identity |
| ContextCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of the resolved binding |
| ContextApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Binding applicability to q |

### 16.6 Negative-evidence nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| NegativeEvidenceReference | EVIDENCE_REFERENCE | — | One exact item supporting a negative proposition |
| PositiveCounterevidenceReference | EVIDENCE_REFERENCE | — | Exact evidence capable of defeating the negative proposition |
| NegativeEvidenceSet | DERIVED_VALUE | — | Set of negative-evidence references |
| NegativeEvidenceAdmissionAssessment | CURRENT_ASSESSMENT | ADMIT | Evidence source/provenance admission |
| NegativeEvidenceCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Evidence freshness and snapshot alignment |
| ExhaustivenessAssessment | CURRENT_ASSESSMENT | EXHAUST | Coverage of the exact negative domain |
| NegativePropositionAssessment | CURRENT_ASSESSMENT | PROP | Assesses the exact negative proposition |
| BasisAbsenceAssessment | CURRENT_ASSESSMENT | PROP | Binds established negative proposition to basis absence |

### 16.7 Grant, delegation, role, scope, and condition nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| GrantRepresentation | SOURCE_RECORD | — | Grant-shaped source bytes |
| GrantIssuanceEvent | HISTORICAL_EVENT | — | Historical grant issuance occurrence |
| GrantStandingRecord | STANDING_RECORD | — | Recognized grant-standing record |
| GrantStandingAssessment | CURRENT_ASSESSMENT | PROP | Current usability of grant standing |
| IssuerAuthorityAssessment | CURRENT_ASSESSMENT | PROP | ISSUE_GRANT authority at issuance snapshot |
| DelegationStandingRecord | STANDING_RECORD | — | Recognized child delegation |
| DelegationChainAssessment | CURRENT_ASSESSMENT | PATH | Parent-child current chain result |
| GrantUseStateRecord | STANDING_RECORD | — | Recognized intrinsic grant-use state |
| GrantUseStateAssessment | CURRENT_ASSESSMENT | CURRENT | Intrinsic grant-use currentness |
| GrantCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Aggregate current grant lifecycle state |
| RolePossessionRecord | STANDING_RECORD | — | Recognized role fact |
| RoleActivationEvent | HISTORICAL_EVENT | — | Historical role activation |
| RoleRequirementResolution | CURRENT_ASSESSMENT | RESOLVE | Whether selected basis requires role |
| RoleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Role satisfaction/applicability to q |
| ScopeRuleRecord | POLICY_OR_RULE_RECORD | — | Scope comparison semantics |
| ScopeRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of scope rule |
| ScopeRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of scope rule |
| ScopeRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of scope rule |
| ScopeApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Basis-scope relation to q |
| JurisdictionRuleRecord | POLICY_OR_RULE_RECORD | — | Jurisdiction comparison semantics |
| JurisdictionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of jurisdiction rule |
| JurisdictionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of jurisdiction rule |
| JurisdictionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of jurisdiction rule |
| JurisdictionAssessment | CURRENT_ASSESSMENT | APP | Basis jurisdiction relation to q |
| ConditionDefinitionRecord | POLICY_OR_RULE_RECORD | — | Exact normative condition definition |
| ConditionDefinitionStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of condition definition |
| ConditionDefinitionCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of condition definition |
| ConditionDefinitionApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of condition definition |
| ConditionStandingRecord | STANDING_RECORD | — | Recognized condition standing |
| ConditionEvidence | EVIDENCE_REFERENCE | — | Evidence used by the predicate evaluator |
| PredicateEvaluationAssessment | CURRENT_ASSESSMENT | PROP | Generic predicate truth at S |
| ConditionRelianceAssessment | CURRENT_ASSESSMENT | PATH | Authority-specific condition effect |

### 16.8 Revocation nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| RevocationRepresentation | SOURCE_RECORD | — | Revocation-shaped source bytes |
| RevocationActAdmissionAssessment | CURRENT_ASSESSMENT | ADMIT | Admission of exact revocation occurrence |
| RevocationAct | HISTORICAL_EVENT | — | Admitted revocation occurrence |
| RevocationStandingRecord | STANDING_RECORD | — | Recognized revocation standing |
| RevocationStandingAssessment | CURRENT_ASSESSMENT | PROP | Current reliance on revocation standing |
| RevocationEffectiveTimeBinding | RESOLVED_BINDING | — | Standing effective-time identity |
| RevocationObservationTimeBinding | RESOLVED_BINDING | — | Observation-time identity |
| RevocationTemporalOrderRuleRecord | POLICY_OR_RULE_RECORD | — | Rule for ordering revocation times/states |
| RevocationTemporalOrderRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of temporal-order rule |
| RevocationTemporalOrderRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of temporal-order rule |
| RevocationTemporalOrderRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of temporal-order rule |
| RevocationTemporalOrderingAssessment | CURRENT_ASSESSMENT | RESOLVE | Orders act/effective/observation/query times |
| RevocationStateSelectionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule selecting authority-evaluation state |
| RevocationStateSelectionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of state-selection rule |
| RevocationStateSelectionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of state-selection rule |
| RevocationStateSelectionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of state-selection rule |
| RevocationAuthorityStateSelectionAssessment | CURRENT_ASSESSMENT | SPECIAL | PRE, EVENT, POST, OTHER, NOT_EVALUABLE |
| RevocationAuthorityAssessment | CURRENT_ASSESSMENT | PROP | Complete REVOKE_GRANT authority subquery |
| CurrentRevocationAssessment | CURRENT_ASSESSMENT | SPECIAL | EFFECTIVE, NOT_EFFECTIVE, PARTIAL, NOT_EVALUABLE |

### 16.9 Semantic-event, delivery, admission, and consumption nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| SemanticEventIdentity | RESOLVED_BINDING | — | Identity of meaning-bearing occurrence E |
| SemanticEventIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves E across representations |
| DeliveryIdentity | RESOLVED_BINDING | — | Identity of transport delivery D |
| ProcessingAttemptIdentity | RESOLVED_BINDING | — | Identity of processing attempt P |
| AdmissionAct | HISTORICAL_EVENT | — | Admission decision occurrence |
| AdmissionIdentity | RESOLVED_BINDING | — | Identity A of admission for E |
| AdmissionIdentityResolutionAssessment | CURRENT_ASSESSMENT | RESOLVE | Resolves admission aliases and duplicate records |
| AdmissionStandingRecord | STANDING_RECORD | — | Recognized admission standing |
| AdmissionCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Current reliance on admission |
| ProcessingTerminalStateAssessment | CURRENT_ASSESSMENT | SPECIAL | NONTERMINAL, COMPLETED, REJECTED, NOT_EVALUABLE |
| AuthorizationActConsumptionRecord | STANDING_RECORD | — | Recognized consumption-state record |
| AuthorizationActConsumptionStateAssessment | CURRENT_ASSESSMENT | SPECIAL | UNCONSUMED, CONSUMED, CONFLICT, NOT_EVALUABLE |
| RetryAdmissionRuleRecord | POLICY_OR_RULE_RECORD | — | Rule permitting retry under same admission |
| RetryAdmissionRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of retry rule |
| RetryAdmissionRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of retry rule |
| RetryAdmissionRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of retry rule |
| EventReuseClassificationAssessment | CURRENT_ASSESSMENT | SPECIAL | RETRY, REPLAY, LAWFUL_REISSUANCE, NEW_FIRST_DELIVERY, NOT_EVALUABLE |

### 16.10 Policy supersession and grant-survival nodes

| Object | Primary semantic type | Outcome | Exact graph role |
|---|---|---|---|
| PolicySupersessionRelation | DERIVED_VALUE | — | Candidate P1-to-P2 relation |
| PolicySupersessionEvidence | EVIDENCE_REFERENCE | — | Evidence for identity, authority, and time of supersession |
| PolicySupersessionAssessment | CURRENT_ASSESSMENT | PROP | Establishes supersession identity/authority/time |
| GrantPolicyDependency | DERIVED_VALUE | — | Exact candidate dependency dimensions |
| GrantPolicyDependencyEvidence | EVIDENCE_REFERENCE | — | Issuance-policy dependency evidence |
| GrantPolicyDependencyAssessment | CURRENT_ASSESSMENT | RESOLVE | Establishes dependency classification |
| SupersessionSurvivalRuleRecord | POLICY_OR_RULE_RECORD | — | Rule governing grant survival |
| SupersessionSurvivalRuleStandingAssessment | CURRENT_ASSESSMENT | PROP | Standing of survival rule |
| SupersessionSurvivalRuleCurrentnessAssessment | CURRENT_ASSESSMENT | CURRENT | Currentness of survival rule |
| SupersessionSurvivalRuleApplicabilityAssessment | CURRENT_ASSESSMENT | APP | Applicability of survival rule |
| SurvivalAssessment | CURRENT_ASSESSMENT | SPECIAL | SURVIVES, DOES_NOT_SURVIVE, PARTIALLY_SURVIVES, NOT_EVALUABLE |

### 16.11 Exact alias and retirement map

These names do not introduce additional graph objects:

| Prior or informal name | Repair 002 treatment |
|---|---|
| AuthorityRecordQueryLaw | Alias retired in favor of DiscoveryLawRecord |
| PolicyPrecedenceRule | Alias retired in favor of PolicyCompositionRuleRecord |
| AdoptionActorAttribution | Uses the already typed ActorBinding |
| context_binding | Exact object name is ContextBinding |
| RevocationEvent | Exact object name is RevocationAct |
| ExhaustiveNegativeProof | Removed from graph; replaced by the three-assessment chain |
| dependency graph identity G in S | Removed; S binds only G0 |
| GoverningPolicySet = NOT_EVALUABLE | Forbidden; GoverningPolicySetAssessment receives the disposition |
| EvaluationSnapshotIdentity = NOT_EVALUABLE | Forbidden; SnapshotConstructionAssessment receives the disposition |

### 16.12 Type-closure invariants

~~~text
ObjectPrimaryTypeCount = 1

CURRENT_ASSESSMENT
  may receive only its declared outcome algebra

all other primary types
  receive no assessment disposition

UnknownGraphNode
→ GraphTypeClosureAssessment = NOT_EVALUABLE

DuplicateObjectWithDifferentPrimaryType
→ GraphTypeClosureAssessment = NOT_EVALUABLE

OutcomeTokenStoredAsRecordStanding
→ FORBIDDEN_CAST
→ affected graph = NOT_EVALUABLE
~~~

## 12. IHR-B10 REPAIR — POLICY SUPERSESSION AND GRANT SURVIVAL

### FINDING

Current exclusion of a superseded policy was allowed to make a historically
issued grant basis FALSE without a grant-survival law.

### COUNTERMODEL

~~~text
P1 validly issues perpetual grant G.
P2 supersedes P1.

P2 preserves existing grants
or:
P2 says nothing.

P1 current exclusion does not determine G currentness.
~~~

### ROOT DEFECT

Repair 001 collapsed policy-set currentness into grant currentness. It did not
represent the exact dependency a grant has on its issuing policy or the rule
governing survival across supersession.

### REPAIR

The repair introduces:

~~~text
GrantPolicyDependency
SupersessionSurvivalRuleRecord
SurvivalAssessment
~~~

GrantPolicyDependency is a DERIVED_VALUE established from the standing grant,
issuance policy, adoption lineage, and governing issuance law. It records the
candidate dependency dimensions without deciding currentness:

~~~text
issuance_validity_dependency
continuing_validity_dependency
interpretive_dependency
scope_definition_dependency
condition_definition_dependency
revocation_dependency
explicit_survival_clause_reference
~~~

The dependency classification is itself guarded by
GrantPolicyDependencyAssessment. Silence never selects a dependency kind.

Supersession survival proceeds:

~~~text
SupersessionSurvivalRuleRecord
→ SupersessionSurvivalRuleStandingAssessment
→ SupersessionSurvivalRuleCurrentnessAssessment
→ SupersessionSurvivalRuleApplicabilityAssessment
→ SurvivalAssessment(G, P1, P2, S)
→ GrantCurrentnessAssessment(G, S)
~~~

SurvivalAssessment outcomes:

~~~text
SURVIVES
DOES_NOT_SURVIVE
PARTIALLY_SURVIVES
NOT_EVALUABLE
~~~

The assessment binds:

- exact G identity and issuance event;
- exact P1 and P2 identities/versions;
- proven supersession relation and effective time;
- GrantPolicyDependency;
- explicit survival text, if any;
- standing survival rule;
- query operation, target, context, and snapshot;
- conflicts with other applicable policies or roots.

No defaults:

~~~text
PolicyCurrentExclusion
↛ GrantBasisFALSE

PolicySuperseded
↛ GrantSurvives

PolicySilence
↛ GrantSurvives

PolicySilence
↛ GrantInvalidated
~~~

Decision mapping:

| Survival result | Grant path effect |
|---|---|
| SURVIVES | Continue every other grant currentness and applicability check |
| DOES_NOT_SURVIVE | Exact grant path may be FALSE when every other required dependency and composition edge resolves |
| PARTIALLY_SURVIVES | Evaluate only dimensions explicitly preserved; incomparable remainder NOT_EVALUABLE |
| NOT_EVALUABLE | GrantCurrentnessAssessment NOT_EVALUABLE if outcome-changing |

Historical issuance standing remains historical in every case.

### NEW OBJECTS / RELATIONS

New objects:

- PolicySupersessionRelation;
- PolicySupersessionEvidence;
- PolicySupersessionAssessment;
- GrantPolicyDependency;
- GrantPolicyDependencyEvidence;
- GrantPolicyDependencyAssessment;
- SupersessionSurvivalRuleRecord;
- SupersessionSurvivalRuleStandingAssessment;
- SupersessionSurvivalRuleCurrentnessAssessment;
- SupersessionSurvivalRuleApplicabilityAssessment;
- SurvivalAssessment;
- GrantCurrentnessAssessment.

New relations:

~~~text
policy current exclusion triggers survival assessment
grant-policy dependency precedes survival
survival rule standing precedes survival result
survival result is one input to grant currentness
historical issuance remains distinct from current grant effect
~~~

### NEW DEPENDENCIES

- exact policy supersession identity, authority, and time;
- standing grant-policy dependency classification;
- independently standing/current/applicable survival rule;
- explicit dimension comparison for partial survival;
- conflict handling across policies and roots.

### WHY COUNTERMODEL NOW FAILS

If P2 expressly preserves G under a standing applicable survival rule,
SurvivalAssessment may return SURVIVES and P1 exclusion cannot make G false.
If P2 is silent and no standing default rule resolves silence,
SurvivalAssessment is NOT_EVALUABLE. If a standing rule invalidates G, the
exact grant path may be FALSE. The model no longer permits policy exclusion
alone to choose between survival and invalidation.

### NEW ATTACK SURFACE

- P2 may preserve only a grant class whose membership is unresolved;
- two successor policies may conflict about survival;
- the survival rule may be issued under P1 and superseded with it;
- grant dependency classification may itself depend on successor policy.

Each requires separate standing, applicability, currentness, conflict, and
cycle assessment. No default is introduced.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 13. IHR-B02 REPAIR — ROOT SET AND CONTROL-DOMAIN CLOSURE

### FINDING

Root independence was evaluated against a named known set without proving that
the root-candidate universe or control/dependency domain was complete.

### COUNTERMODEL

~~~text
R1:
  no known conflict
  independent from K = {suite}

R2:
  another applicable root
  prohibits q

or:
  an undisclosed actor controls R1 standing
~~~

### ROOT DEFECT

Repair 001 treated RootResolutionBundle as though recorded known conflicts and
independence from a named set could establish:

- root-candidate-set closure;
- jurisdiction closure;
- control-subject closure;
- dependency-relation closure;
- conflict absence;
- root applicability.

Those propositions are distinct. Independence from a known set is not
independence from a closed control domain.

### REPAIR

Root resolution is rebuilt as five ordered assessments:

~~~text
1. RootCandidateDiscoveryAssessment
2. RootCandidateSetClosureAssessment
3. RootControlDomainClosureAssessment
4. RootIndependenceAssessment
5. RootApplicabilityAssessment
   plus RootConflictResolutionAssessment
~~~

The objects are:

~~~text
RootCandidateSet RC
  finite root references admitted by B0 for the required edge

RootControlDomain(R)
  candidate controlling subjects, standing dependencies,
  admission dependencies, revocation dependencies,
  funding/custody dependencies when normatively controlling,
  and policy dependencies capable of changing R

IndependenceDomainClosureAssessment(R, S)
  determines whether RootControlDomain(R) is complete
  for the exact required edge and snapshot
~~~

RootCandidateSetClosureAssessment requires:

- B0 admission;
- all root registries named by B0 at their bound epochs;
- jurisdiction and authority-class coverage;
- alias resolution without collapsing distinct roots;
- explicit treatment of every omitted root capable of changing q.

IndependenceDomainClosureAssessment requires:

- a standing definition of control for the required authority edge;
- complete discovery of controlling subjects and dependency relations inside
  B0;
- currentness at S;
- no unresolved hidden-controller evidence;
- no self-certification by R or a component whose independence is at issue.

Only after both closure assessments are CLOSED may
RootIndependenceAssessment return TRUE or FALSE. Otherwise it returns
NOT_EVALUABLE.

Conflict and applicability remain separate:

~~~text
RootIndependenceAssessment = TRUE
↛ RootApplicabilityAssessment = APPLICABLE

RootApplicabilityAssessment = APPLICABLE
↛ RootConflictResolutionAssessment = RESOLVED
~~~

Root conflict resolution consumes all standing, current, applicable roots in
the closed RootCandidateSet and a separately standing root precedence or
composition rule. It never selects first, newest, local, external, or
Founder-labeled by default.

This artifact introduces no positive root and supplies no positive closure
assessment for a real root set.

### NEW OBJECTS / RELATIONS

New objects:

- RootRegistrySnapshot;
- RootRegistryCurrentnessAssessment;
- RootCandidateDiscoveryAssessment;
- RootCandidateSet;
- RootIdentityResolutionAssessment;
- RootCandidateSetClosureAssessment;
- RootControlDomain;
- RootControlEvidence;
- RootControlDefinitionRuleRecord;
- RootControlDefinitionRuleStandingAssessment;
- RootControlDefinitionRuleCurrentnessAssessment;
- RootControlDefinitionRuleApplicabilityAssessment;
- RootControlDomainDiscoveryAssessment;
- IndependenceDomainClosureAssessment;
- RootIndependenceAssessment;
- RootApplicabilityAssessment;
- RootConflictRuleRecord;
- RootConflictRuleStandingAssessment;
- RootConflictRuleCurrentnessAssessment;
- RootConflictRuleApplicabilityAssessment;
- RootConflictResolutionAssessment;
- RootResolutionBundleAssemblyAssessment.

New relations:

~~~text
root registry closure precedes root-set closure
root-set closure precedes conflict resolution
control-domain closure precedes independence
independence precedes admissible root termination use
applicability is query-relative
conflict resolution consumes all applicable roots
~~~

### NEW DEPENDENCIES

- admitted governance boundary B0;
- authoritative root-registry epochs;
- standing control-relation definition;
- current control-domain discovery;
- root alias and identity resolution;
- standing root conflict rule when multiple applicable roots disagree.

### WHY COUNTERMODEL NOW FAILS

R2 cannot be silently omitted when RootCandidateSetClosureAssessment is CLOSED.
If R2 is inside B0, it must appear and enter conflict resolution. If its
membership is unresolved, closure is NOT_EVALUABLE and R1 cannot terminate the
path.

The undisclosed controller prevents IndependenceDomainClosureAssessment from
being CLOSED. Therefore RootIndependenceAssessment cannot return TRUE.

~~~text
IndependentFromKnownSet
!= IndependenceEstablished
~~~

The only lawful results are complete conflict handling or fail-closed
NOT_EVALUABLE. No positive R1 is created by this repair.

### NEW ATTACK SURFACE

- control may be indirect, time-varying, or jurisdiction-specific;
- root registries may disagree about aliases;
- a root-conflict rule may be controlled by a disputed root;
- B0 may fail to cover a foreign root jurisdiction.

These remain explicit dependencies. An unresolved case produces
NOT_EVALUABLE.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 14. IHR-B03 REPAIR — COMPLETE REPAIR-TIME TYPE TABLE

### FINDING

Repair 001 used graph nodes absent from its inventory and allowed a binding or
derived value to receive an assessment disposition.

### COUNTERMODEL

~~~text
PolicyCandidateDiscoveryAssessment is used but untyped.
context_binding is used but untyped.
EvaluationSnapshotIdentity is a binding but receives NOT_EVALUABLE.
GoverningPolicySet is a derived value but receives NOT_EVALUABLE.
Rule records are consumed as standing without standing assessments.
~~~

### ROOT DEFECT

The object inventory was written separately from the dependency graph and was
not closed over the graph's actual node names. Record, standing, currentness,
applicability, set, binding, and result roles were not mechanically separated.

### REPAIR

Section 11 is the normative repair-time node registry for this artifact. Every
node in sections 17 and 18 appears exactly once in that table with:

- one object name;
- one primary semantic type;
- one exact role;
- an outcome algebra only when the type is CURRENT_ASSESSMENT.

The table uses the eight existing primary types and introduces zero new
primary type classes. It includes every object newly required by IHR-B01
through IHR-B10 and every retained graph node needed to connect them to the
final AuthorityApplicabilityAssessment.

The graph completeness rule is bidirectional:

~~~text
GraphNode → exactly one TypeTableRow
TypeTableNode marked IN_GRAPH → exactly one GraphNodeIdentity
~~~

The following casts are forbidden:

~~~text
SOURCE_RECORD ↛ HISTORICAL_EVENT
HISTORICAL_EVENT ↛ STANDING_RECORD
STANDING_RECORD ↛ CURRENT_ASSESSMENT
POLICY_OR_RULE_RECORD ↛ rule standing
EVIDENCE_REFERENCE ↛ negative proposition
DERIVED_VALUE ↛ assessment disposition
RESOLVED_BINDING ↛ assessment disposition
~~~

When construction of a binding, set, or graph fails, a separate construction,
closure, or assembly assessment receives NOT_EVALUABLE. The underlying object
is absent or remains a candidate; it is never relabeled as an assessment.

### NEW OBJECTS / RELATIONS

New objects are the typed nodes in section 11. The minimum new relations are:

~~~text
record → standing assessment
record → currentness assessment
record → applicability assessment
evidence set → exhaustiveness assessment
binding inputs → construction assessment → binding
set inputs → closure assessment → set use
graph blueprint → graph assessments → final graph record
~~~

### NEW DEPENDENCIES

- exact agreement between the type table and graph;
- named outcome algebra for each assessment;
- graph-construction rejection of untyped nodes;
- graph-construction rejection of cross-type disposition assignment.

### WHY COUNTERMODEL NOW FAILS

PolicyCandidateDiscoveryAssessment, ContextClaim, ContextSource,
ContextBinding, EvaluationSnapshotIdentity, GoverningPolicySet, and every
consumed rule-standing path now have explicit rows. EvaluationSnapshotIdentity
and GoverningPolicySet never receive NOT_EVALUABLE; their construction or set
assessment does.

An untyped node makes GraphTypeClosureAssessment NOT_EVALUABLE and prevents a
query result. A disposition attached to a non-assessment object is a forbidden
cast and likewise blocks graph admission.

### NEW ATTACK SURFACE

- prose could introduce a new graph node after the table is frozen;
- aliases could make one object appear under two types;
- a runtime could serialize a result token inside a record field.

This report addresses the semantic surface by freezing the node registry and
alias rules. Runtime enforcement remains out of scope and unresolved.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 15. IHR-B04 REPAIR — POLICY-SELECTION-LAW STANDING

### FINDING

PolicyCandidateDiscoveryAssessment depended on an ungraphed selection law, and
selection/composition rules were consumed as standing without independent
standing paths.

### COUNTERMODEL

~~~text
SL1 selects only Ppermit.
SL2 selects only Pprohibit.

or:
Policy P selects SL.
SL gives P standing.

or:
SL selects itself as the only standing selection law.
~~~

### ROOT DEFECT

Repair 001 modeled policy candidates but not a closed candidate set of
PolicySelectionLawRecord objects. It therefore could omit a selector, accept a
bare selector record as standing, or hide selection-law/policy-standing
recursion.

### REPAIR

Policy selection is split into two non-self-validating layers.

Layer A resolves selection laws:

~~~text
PolicySelectionLawRegistrySnapshot(B0, S)
→ PolicySelectionLawRegistryCurrentnessAssessment
→ PolicySelectionLawCandidateSet
→ PolicySelectionLawCandidateSetClosureAssessment

for each PolicySelectionLawRecord SL:
  PolicySelectionLawStandingAssessment
  PolicySelectionLawCurrentnessAssessment
  PolicySelectionLawApplicabilityAssessment

all standing + current + applicable SL
→ PolicySelectionLawCompositionAssessment
~~~

Layer B discovers policies:

~~~text
resolved PolicySelectionLawCompositionAssessment
+ q
+ S
+ governed policy corpus snapshots
→ PolicyCandidateDiscoveryAssessment
→ PolicyCandidateSet
→ PolicyCandidateSetClosureAssessment
~~~

The dependency is mandatory and explicit:

~~~text
PolicyCandidateDiscoveryAssessment
DEPENDS_ON
PolicySelectionLawCompositionAssessment
~~~

Every PolicySelectionLawRecord has a standing path independent of the policy
candidates it selects. Its standing may terminate only through:

- a predecessor rule whose own path is acyclic; or
- an applicable RootResolutionBundle resolved under section 13.

The law may not rely exclusively on:

- itself;
- the policy set it selects;
- a policy whose adoption standing depends on that law;
- the AuthorityApplicabilityAssessment that consumes its output.

The same record/assessment separation applies to policy precedence and
composition:

~~~text
PolicyCompositionRuleRecord
→ PolicyCompositionRuleStandingAssessment
→ PolicyCompositionRuleCurrentnessAssessment
→ PolicyCompositionRuleApplicabilityAssessment
→ PolicyCompositionAssessment
~~~

Selection-law candidate closure uses B0 as the finite termination boundary.
B0 cannot be admitted by an enclosed selection law. If the independent B0 path
is unresolved, selection-law closure and policy discovery are
NOT_EVALUABLE—there is no infinite self-selection regress.

### NEW OBJECTS / RELATIONS

New objects:

- PolicySelectionLawRegistrySnapshot;
- PolicySelectionLawRegistryCurrentnessAssessment;
- PolicySelectionLawRecord;
- PolicySelectionLawCandidateSet;
- PolicySelectionLawIdentityResolutionAssessment;
- PolicySelectionLawCandidateSetClosureAssessment;
- PolicySelectionLawStandingAssessment;
- PolicySelectionLawCurrentnessAssessment;
- PolicySelectionLawApplicabilityAssessment;
- PolicySelectionLawCompositionRuleRecord;
- PolicySelectionLawCompositionRuleStandingAssessment;
- PolicySelectionLawCompositionRuleCurrentnessAssessment;
- PolicySelectionLawCompositionRuleApplicabilityAssessment;
- PolicySelectionLawCompositionAssessment;
- PolicyCandidateDiscoveryAssessment;
- PolicyIdentityResolutionAssessment;
- PolicyCompositionRuleRecord;
- PolicyCompositionRuleStandingAssessment;
- PolicyCompositionRuleCurrentnessAssessment;
- PolicyCompositionRuleApplicabilityAssessment;
- PolicyCompositionAssessment.

New relations:

~~~text
selection-law closure precedes policy discovery
selection-law standing is independent of selected policies
policy discovery consumes resolved selection-law composition
policy standing remains separate from policy applicability
policy composition record never self-confers standing
~~~

### NEW DEPENDENCIES

- admitted B0;
- policy-selection-law registry identity, epoch, and closure;
- independent standing/currentness/applicability for every consumed selector;
- standing selector-composition law when multiple selectors differ;
- policy-corpus closure;
- independent standing/currentness/applicability for policy composition.

### WHY COUNTERMODEL NOW FAILS

SL1 and SL2 must both appear when the selection-law set is CLOSED. Ppermit and
Pprohibit both enter policy discovery, and their normative conflict requires
standing composition. If selector closure or composition is unresolved, the
governing-policy assessment is NOT_EVALUABLE. No selector can win by omission.

A self-selecting or policy-dependent standing path forms an explicit
POLICY_SELECTION_PROVENANCE_CYCLE. It cannot produce standing. Without an
acyclic predecessor or applicable root, policy discovery is NOT_EVALUABLE.

### NEW ATTACK SURFACE

- multiple selection-law registries may disagree;
- a predecessor chain may be finite but point to an inapplicable root;
- selector composition may exclude a selector whose exclusion changes policy
  discovery;
- a policy may indirectly control a selector through an alias.

All remain graph dependencies and fail closed when unresolved.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 16. IHR-B05 REPAIR — NEGATIVE-EVIDENCE ASSESSMENT CHAIN

### FINDING

An EVIDENCE_REFERENCE named ExhaustiveNegativeProof could directly establish
query FALSE.

### COUNTERMODEL

~~~text
stale evidence reference says no basis exists

direct evidence-to-FALSE cast:
  query FALSE

current assessment:
  NOT_EVALUABLE
~~~

### ROOT DEFECT

Repair 001 named evidence as a proof object and skipped the current assessment
steps that must establish authority, coverage, freshness, snapshot alignment,
conflict state, and noncircularity.

### REPAIR

The old ExhaustiveNegativeProof node is removed from the repaired graph. It is
replaced with:

~~~text
NegativeEvidenceSet
→ ExhaustivenessAssessment
→ NegativePropositionAssessment
→ BasisAbsenceAssessment
→ AuthorityBasisCompositionAssessment
→ AuthorityApplicabilityAssessment
~~~

NegativeEvidenceSet is a DERIVED_VALUE containing exact
EVIDENCE_REFERENCE identities. It does not assert absence and has no
disposition.

ExhaustivenessAssessment asks whether that set covers the exact negative
domain:

~~~text
negative proposition
q
S
B0
closed discovery-law set
closed authority-corpus set
all admissible basis kinds
all relevant aliases
current corpus epochs
source standing
source authority
freshness
snapshot consistency
conflicts
noncircularity
~~~

Its outcomes are:

~~~text
EXHAUSTIVE
NON_EXHAUSTIVE
NOT_EVALUABLE
~~~

NegativePropositionAssessment may return TRUE only when
ExhaustivenessAssessment is EXHAUSTIVE and every required input is current,
authoritative, aligned, and acyclic. It returns FALSE only if positive evidence
defeats the negative proposition. Otherwise it returns NOT_EVALUABLE.

BasisAbsenceAssessment binds the established negative proposition to the
authority-basis domain. Query FALSE additionally requires:

- DiscoveryLawCandidateSetClosureAssessment = CLOSED;
- BasisSetClosureAssessment = CLOSED;
- no non-grant or out-of-corpus basis kind remains admissible;
- governing policy and composition are resolved;
- no standing prohibition/permit interaction changes the result.

Mandatory failure mapping:

| Condition | ExhaustivenessAssessment | NegativePropositionAssessment | Query effect |
|---|---|---|---|
| Stale evidence | NOT_EVALUABLE | NOT_EVALUABLE | NOT_EVALUABLE |
| Incomplete domain | NON_EXHAUSTIVE | NOT_EVALUABLE | NOT_EVALUABLE |
| Nonauthoritative source | NOT_EVALUABLE | NOT_EVALUABLE | NOT_EVALUABLE |
| Snapshot mismatch | NOT_EVALUABLE | NOT_EVALUABLE | NOT_EVALUABLE |
| Unresolved source conflict | NOT_EVALUABLE | NOT_EVALUABLE | NOT_EVALUABLE |
| Current, authoritative, closed, conflict-free negative domain | EXHAUSTIVE | TRUE | Continue query-level composition |
| Positive counterevidence | EXHAUSTIVE or NOT_EVALUABLE as applicable | FALSE | Negative route cannot establish query FALSE |

~~~text
AbsenceObservation
!= ExhaustiveNegativeProof
!= NegativeAssessment
~~~

The middle name is retained only in this non-collapse statement. It is no
longer a graph-object type or a direct authority input.

### NEW OBJECTS / RELATIONS

New objects:

- NegativeEvidenceSet;
- PositiveCounterevidenceReference;
- NegativeEvidenceAdmissionAssessment;
- NegativeEvidenceCurrentnessAssessment;
- ExhaustivenessAssessment;
- NegativePropositionAssessment;
- BasisAbsenceAssessment.

New relations:

~~~text
evidence references form a set
set admission/currentness precede exhaustiveness
exhaustiveness precedes negative proposition
negative proposition precedes basis absence
basis absence remains one query-composition input
~~~

### NEW DEPENDENCIES

- source standing and authority;
- complete negative domain description;
- B0, discovery-law, corpus, basis-kind, and alias closure;
- snapshot alignment and currentness;
- conflict and noncircularity assessment;
- standing query-level composition.

### WHY COUNTERMODEL NOW FAILS

The stale reference cannot make ExhaustivenessAssessment EXHAUSTIVE.
NegativePropositionAssessment is therefore NOT_EVALUABLE, and no query-level
FALSE is available. The evidence remains evidence; it is never cast into an
assessment result.

### NEW ATTACK SURFACE

- a negative domain can be framed too narrowly;
- multiple evidence sources can use different epochs;
- a source may be authoritative for one corpus but not all basis kinds;
- circular absence evidence may depend on the query result.

Each is an explicit assessment dependency. Unresolved cases remain
NOT_EVALUABLE.

### STATUS

~~~text
AUTHOR_CLAIMS_CLOSED
NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
~~~

## 17. REPAIRED DEPENDENCY GRAPH

In every diagram below:

~~~text
A
  → B

means:
  positive or dispositive use of A depends on B
~~~

The candidate dependency graph may contain cycles. It is called a proof DAG
only after GraphAcyclicityAssessment and ProvenanceCycleAssessment establish a
selected sufficient acyclic subgraph under standing composition law.

Capitalized identifiers in the diagrams are exact graph objects from section
11. Lower-case phrases are edge annotations, parameter values, or fields of
the named object; they do not introduce hidden graph nodes.

### 17.1 Top-level authority graph

~~~text
AuthorityApplicabilityAssessment(q, S, G0)
|
+→ QueryBindingConstructionAssessment
|   +→ AdmittedRequestAct
|   +→ AdmittedRequestActIdentity
|   +→ PrincipalBinding
|   +→ ActorBinding
|   +→ OperationBinding
|   +→ TargetBinding
|   +→ ContextResolutionAssessment
|       +→ ContextBinding
|       +→ ContextCurrentnessAssessment
|       +→ ContextApplicabilityAssessment
|
+→ SnapshotConstructionAssessment
|   +→ SnapshotSeed
|   +→ DependencyGraphBlueprintIdentity
|   +→ ReconciledEvaluationTimeBinding
|   +→ TimeFreshnessAssessment
|   +→ TimeSourceReconciliationAssessment
|
+→ GovernanceBoundaryAdmissionAssessment
|
+→ GoverningPolicySetAssessment
|
+→ AuthorityBasisCompositionAssessment
|
+→ GraphTypeClosureAssessment
+→ GraphEdgeClosureAssessment
+→ GraphCandidateCoverageAssessment
+→ GraphAcyclicityAssessment
+→ ProvenanceCycleAssessment
~~~

The completed AuthorityDependencyGraph and its identity are output witnesses.
They are not dependencies of AuthorityApplicabilityAssessment in the same
evaluation.

### 17.2 Boundary-admission termination graph

~~~text
GovernanceBoundaryAdmissionAssessment(B0, S)
|
+→ GovernanceBoundaryRecord
+→ GovernanceBoundaryAdmissionEvent
+→ GovernanceBoundaryStandingRecord
+→ GovernanceBoundaryStandingAssessment
+→ GovernanceBoundaryCurrentnessAssessment
+→ GovernanceBoundaryApplicabilityAssessment
+→ RootResolutionBundleAssemblyAssessment
    or an independently supplied predecessor path
~~~

If RootResolutionBundleAssemblyAssessment depends on the same B0 whose
admission it is meant to prove, the cycle is explicit and relevant. Without an
independent acyclic predecessor/root path, boundary admission is
NOT_EVALUABLE.

### 17.3 Time and snapshot graph

~~~text
TimeSourceReconciliationAssessment
|
+→ EvaluationTimeEvidence
+→ TimeSourceStandingRecord
+→ TimeSourceStandingAssessment
+→ TimeReconciliationRuleRecord
+→ TimeReconciliationRuleStandingAssessment
+→ TimeReconciliationRuleCurrentnessAssessment
+→ TimeReconciliationRuleApplicabilityAssessment

TimeFreshnessAssessment
|
+→ EvaluationTimeEvidence
+→ FreshnessRuleRecord
+→ FreshnessRuleStandingAssessment
+→ FreshnessRuleCurrentnessAssessment
+→ FreshnessRuleApplicabilityAssessment

SnapshotConstructionAssessment
|
+→ AuthorityQueryIdentity
+→ SnapshotSeed
+→ DependencyGraphBlueprintIdentity
+→ TimeSourceReconciliationAssessment
+→ TimeFreshnessAssessment
+→ exact source and registry epoch identities
~~~

### 17.4 Discovery-law meta-closure graph

~~~text
DiscoveryLawCompositionAssessment(q, S)
|
+→ GovernanceBoundaryAdmissionAssessment
+→ DiscoveryLawRegistrySnapshot
+→ DiscoveryLawRegistryCurrentnessAssessment
+→ DiscoveryLawCandidateSet
+→ DiscoveryLawIdentityResolutionAssessment
+→ DiscoveryLawCandidateSetClosureAssessment
+→ for every DiscoveryLawRecord L:
|   +→ DiscoveryLawStandingAssessment(L, S)
|   +→ DiscoveryLawCurrentnessAssessment(L, S)
|   +→ DiscoveryLawApplicabilityAssessment(L, q, S)
+→ DiscoveryLawCompositionRuleRecord
+→ DiscoveryLawCompositionRuleStandingAssessment
+→ DiscoveryLawCompositionRuleCurrentnessAssessment
+→ DiscoveryLawCompositionRuleApplicabilityAssessment

AuthorityBasisDiscoveryAssessment
|
+→ DiscoveryLawCompositionAssessment
+→ AuthorityRecordCorpusSnapshot
+→ AuthorityRecordCorpusCurrentnessAssessment
+→ AuthorityQueryIdentity
+→ EvaluationSnapshotIdentity
+→ GoverningPolicySetAssessment

BasisSetClosureAssessment
|
+→ DiscoveryLawCandidateSetClosureAssessment
+→ DiscoveryLawCompositionAssessment
+→ AuthorityBasisDiscoveryAssessment
+→ AuthorityBasisCandidateSet
+→ AuthorityBasisIdentityResolutionAssessment
+→ AuthorityRecordCorpusCurrentnessAssessment
~~~

No AuthorityBasisCandidateSet can be declared closed relative to only one
selected L when another standing applicable L remains in the closed law set.

### 17.5 Policy-selection-law and governing-policy graph

~~~text
PolicySelectionLawCompositionAssessment(q, S)
|
+→ GovernanceBoundaryAdmissionAssessment
+→ PolicySelectionLawRegistrySnapshot
+→ PolicySelectionLawRegistryCurrentnessAssessment
+→ PolicySelectionLawCandidateSet
+→ PolicySelectionLawIdentityResolutionAssessment
+→ PolicySelectionLawCandidateSetClosureAssessment
+→ for every PolicySelectionLawRecord SL:
|   +→ PolicySelectionLawStandingAssessment(SL, S)
|   +→ PolicySelectionLawCurrentnessAssessment(SL, S)
|   +→ PolicySelectionLawApplicabilityAssessment(SL, q, S)
+→ PolicySelectionLawCompositionRuleRecord
+→ PolicySelectionLawCompositionRuleStandingAssessment
+→ PolicySelectionLawCompositionRuleCurrentnessAssessment
+→ PolicySelectionLawCompositionRuleApplicabilityAssessment

PolicyCandidateDiscoveryAssessment
|
+→ PolicySelectionLawCompositionAssessment
+→ PolicyCorpusSnapshot
+→ PolicyCorpusCurrentnessAssessment
+→ AuthorityQueryIdentity
+→ EvaluationSnapshotIdentity

PolicyCandidateSetClosureAssessment
|
+→ PolicyCandidateDiscoveryAssessment
+→ PolicyIdentityResolutionAssessment
+→ PolicySelectionLawCandidateSetClosureAssessment
+→ PolicyCorpusCurrentnessAssessment

PolicyStandingAssessment(P, S)
|
+→ PolicyRecord
+→ PolicyAdoptionStandingAssessment
|   +→ PolicyAdoptionStandingRecord
|   +→ PolicyAdoptionEvent
|   +→ PolicyAdoptionAuthorityAssessment
+→ PolicyCurrentnessAssessment
+→ ProvenanceCycleAssessment

PolicyApplicabilityAssessment(P, q, S)
|
+→ PolicyStandingAssessment
+→ AuthorityQueryIdentity
+→ ContextBinding
+→ EvaluationSnapshotIdentity

PolicyCompositionAssessment(q, S)
|
+→ PolicyCandidateSet
+→ PolicyCandidateSetClosureAssessment
+→ every PolicyStandingAssessment
+→ every PolicyApplicabilityAssessment
+→ PolicyCompositionRuleRecord
+→ PolicyCompositionRuleStandingAssessment
+→ PolicyCompositionRuleCurrentnessAssessment
+→ PolicyCompositionRuleApplicabilityAssessment

GoverningPolicySetAssessment
|
+→ PolicyCompositionAssessment
+→ GoverningPolicySet
~~~

PolicySelectionLawStandingAssessment may not depend exclusively on the
PolicyCandidateSet it causes to be discovered. PolicyAdoptionAuthorityAssessment
may not depend exclusively on the policy whose adoption it is assessing.

### 17.6 Root and control-domain graph

~~~text
RootCandidateDiscoveryAssessment(required_edge, S)
|
+→ GovernanceBoundaryAdmissionAssessment
+→ RootRegistrySnapshot
+→ RootRegistryCurrentnessAssessment
+→ every RootReference

RootCandidateSetClosureAssessment
|
+→ RootCandidateDiscoveryAssessment
+→ RootCandidateSet
+→ RootIdentityResolutionAssessment

RootControlDomainDiscoveryAssessment(R, S)
|
+→ RootReference
+→ RootStandingRecord
+→ GovernanceBoundaryAdmissionAssessment
+→ RootControlEvidence
+→ RootControlDefinitionRuleRecord
+→ RootControlDefinitionRuleStandingAssessment
+→ RootControlDefinitionRuleCurrentnessAssessment
+→ RootControlDefinitionRuleApplicabilityAssessment

IndependenceDomainClosureAssessment(R, S)
|
+→ RootControlDomainDiscoveryAssessment
+→ RootControlDomain
+→ standing control-definition dependencies

RootIndependenceAssessment(R, S)
|
+→ IndependenceDomainClosureAssessment
+→ RootControlDomain
+→ unresolved dependency component being terminated

RootApplicabilityAssessment(R, required_edge, S)
|
+→ RootStandingAssessment
+→ RootIndependenceAssessment
+→ AuthorityQueryIdentity
+→ EvaluationSnapshotIdentity

RootConflictResolutionAssessment
|
+→ RootCandidateSetClosureAssessment
+→ every applicable RootApplicabilityAssessment
+→ RootConflictRuleRecord
+→ RootConflictRuleStandingAssessment
+→ RootConflictRuleCurrentnessAssessment
+→ RootConflictRuleApplicabilityAssessment

RootResolutionBundleAssemblyAssessment
|
+→ RootReference
+→ RootAdmissionEvent
+→ RootStandingRecord
+→ RootStandingAssessment
+→ RootCandidateSetClosureAssessment
+→ IndependenceDomainClosureAssessment
+→ RootIndependenceAssessment
+→ RootApplicabilityAssessment
+→ RootConflictResolutionAssessment
+→ RootResolutionBundle
~~~

No positive RootResolutionBundle is instantiated by this report.

### 17.7 Context-resolution graph

~~~text
ContextResolutionAssessment
|
+→ ContextResolutionRequest
+→ every ContextClaim
+→ every ContextSource
+→ ContextSourceCandidateSet
+→ ContextSourceIdentityResolutionAssessment
+→ ContextSourceCandidateSetClosureAssessment
+→ every ContextSourceStandingRecord
+→ every ContextSourceStandingAssessment
+→ every ContextSourceCurrentnessAssessment
+→ every ContextSourceApplicabilityAssessment
+→ ContextResolutionRuleRecord
+→ ContextResolutionRuleStandingAssessment
+→ ContextResolutionRuleCurrentnessAssessment
+→ ContextResolutionRuleApplicabilityAssessment
+→ ContextCompositionRuleRecord
+→ ContextCompositionRuleStandingAssessment
+→ ContextCompositionRuleCurrentnessAssessment
+→ ContextCompositionRuleApplicabilityAssessment

ContextCurrentnessAssessment
|
+→ ContextBinding
+→ source observation epochs
+→ EvaluationSnapshotIdentity

ContextApplicabilityAssessment
|
+→ ContextBinding
+→ AuthorityQueryIdentity
+→ EvaluationSnapshotIdentity
~~~

The caller's ContextClaim is never a standing resolution rule or binding.

### 17.8 Negative-evidence graph

~~~text
NegativeEvidenceAdmissionAssessment
|
+→ every NegativeEvidenceReference
+→ exact source provenance and standing inputs

NegativeEvidenceCurrentnessAssessment
|
+→ NegativeEvidenceSet
+→ EvaluationSnapshotIdentity
+→ AuthorityRecordCorpusSnapshot
+→ PolicyCorpusSnapshot

ExhaustivenessAssessment
|
+→ NegativeEvidenceSet
+→ NegativeEvidenceAdmissionAssessment
+→ NegativeEvidenceCurrentnessAssessment
+→ GovernanceBoundaryAdmissionAssessment
+→ DiscoveryLawCandidateSetClosureAssessment
+→ DiscoveryLawCompositionAssessment
+→ BasisSetClosureAssessment
+→ AuthorityRecordCorpusCurrentnessAssessment

NegativePropositionAssessment
|
+→ ExhaustivenessAssessment
+→ PositiveCounterevidenceReference
+→ ProvenanceCycleAssessment

BasisAbsenceAssessment
|
+→ NegativePropositionAssessment
+→ AuthorityBasisCandidateSet
+→ BasisSetClosureAssessment
~~~

### 17.9 Exact grant-basis graph

~~~text
BasisPathAssessment(G, q, S)
|
+→ GrantStandingAssessment
|   +→ GrantRepresentation
|   +→ GrantIssuanceEvent
|   +→ GrantStandingRecord
|   +→ IssuerAuthorityAssessment
|       +→ complete ISSUE_GRANT historical authority subquery
+→ DelegationChainAssessment
|   +→ DelegationStandingRecord
+→ GrantCurrentnessAssessment
|   +→ GrantUseStateAssessment, if intrinsic-use constrained
|   +→ CurrentRevocationAssessment
|   +→ SurvivalAssessment, if issuing policy is superseded
+→ RoleRequirementResolution
+→ RoleApplicabilityAssessment, if required
+→ ScopeApplicabilityAssessment
|   +→ ScopeRuleRecord
|   +→ ScopeRuleStandingAssessment
|   +→ ScopeRuleCurrentnessAssessment
|   +→ ScopeRuleApplicabilityAssessment
+→ JurisdictionAssessment
|   +→ JurisdictionRuleRecord
|   +→ JurisdictionRuleStandingAssessment
|   +→ JurisdictionRuleCurrentnessAssessment
|   +→ JurisdictionRuleApplicabilityAssessment
+→ ConditionRelianceAssessment
|   +→ ConditionDefinitionRecord
|   +→ ConditionDefinitionStandingAssessment
|   +→ ConditionDefinitionCurrentnessAssessment
|   +→ ConditionDefinitionApplicabilityAssessment
|   +→ ConditionStandingRecord
|   +→ ConditionEvidence
|   +→ PredicateEvaluationAssessment
+→ GoverningPolicySetAssessment
+→ ProvenanceCycleAssessment
~~~

### 17.10 Revocation subgraph

~~~text
CurrentRevocationAssessment(R, G, S)
|
+→ RevocationActAdmissionAssessment
|   +→ RevocationRepresentation
|   +→ RevocationAct
+→ RevocationStandingAssessment
|   +→ RevocationStandingRecord
+→ RevocationEffectiveTimeBinding
+→ RevocationObservationTimeBinding
+→ RevocationTemporalOrderingAssessment
|   +→ RevocationTemporalOrderRuleRecord
|   +→ RevocationTemporalOrderRuleStandingAssessment
|   +→ RevocationTemporalOrderRuleCurrentnessAssessment
|   +→ RevocationTemporalOrderRuleApplicabilityAssessment
+→ RevocationAuthorityStateSelectionAssessment
|   +→ RevocationStateSelectionRuleRecord
|   +→ RevocationStateSelectionRuleStandingAssessment
|   +→ RevocationStateSelectionRuleCurrentnessAssessment
|   +→ RevocationStateSelectionRuleApplicabilityAssessment
+→ RevocationAuthorityAssessment
    +→ complete REVOKE_GRANT historical authority subquery
    +→ selected historical state and snapshot
    +→ ActorBinding
    +→ OperationBinding
    +→ TargetBinding
    +→ ContextBinding
~~~

The REVOKE_GRANT subquery is mandatory. A relevant self-revocation cycle is
not hidden as a leaf.

### 17.11 Retry/replay classification graph

~~~text
EventReuseClassificationAssessment
|
+→ SemanticEventIdentity
+→ SemanticEventIdentityResolutionAssessment
+→ DeliveryIdentity
+→ ProcessingAttemptIdentity
+→ AdmissionAct
+→ AdmissionIdentity
+→ AdmissionIdentityResolutionAssessment
+→ AdmissionStandingRecord
+→ AdmissionCurrentnessAssessment
+→ ProcessingTerminalStateAssessment
+→ AuthorizationActConsumptionRecord
+→ AuthorizationActConsumptionStateAssessment
+→ RetryAdmissionRuleRecord
+→ RetryAdmissionRuleStandingAssessment
+→ RetryAdmissionRuleCurrentnessAssessment
+→ RetryAdmissionRuleApplicabilityAssessment
~~~

When q relies on an asserted new authorization act,
QueryBindingConstructionAssessment depends on
EventReuseClassificationAssessment. A replay blocks that claimed new-act path.
It does not, by itself, rewrite intrinsic grant currentness.

### 17.12 Supersession-survival graph

~~~text
PolicySupersessionAssessment(P1, P2, S)
|
+→ PolicySupersessionRelation
+→ PolicySupersessionEvidence
+→ PolicyStandingAssessment(P1)
+→ PolicyStandingAssessment(P2)
+→ PolicyCurrentnessAssessment(P1)
+→ PolicyCurrentnessAssessment(P2)

GrantPolicyDependencyAssessment(G, P1, S)
|
+→ GrantStandingRecord
+→ GrantIssuanceEvent
+→ PolicyRecord(P1)
+→ GrantPolicyDependencyEvidence

SurvivalAssessment(G, P1, P2, S)
|
+→ PolicySupersessionAssessment
+→ GrantPolicyDependency
+→ GrantPolicyDependencyAssessment
+→ SupersessionSurvivalRuleRecord
+→ SupersessionSurvivalRuleStandingAssessment
+→ SupersessionSurvivalRuleCurrentnessAssessment
+→ SupersessionSurvivalRuleApplicabilityAssessment
+→ PolicyCompositionAssessment
+→ RootConflictResolutionAssessment
~~~

### 17.13 Basis composition and final disposition

~~~text
AuthorityBasisCompositionAssessment(q, S)
|
+→ AuthorityBasisCandidateSet
+→ BasisSetClosureAssessment
+→ every BasisPathAssessment
+→ BasisAbsenceAssessment, when negative route is asserted
+→ AuthorityBasisCompositionRuleRecord
+→ AuthorityBasisCompositionRuleStandingAssessment
+→ AuthorityBasisCompositionRuleCurrentnessAssessment
+→ AuthorityBasisCompositionRuleApplicabilityAssessment
+→ GoverningPolicySetAssessment
+→ RootConflictResolutionAssessment, when root paths participate
+→ no unresolved outcome-changing candidate
~~~

Final query outcomes:

| Preconditions | Query disposition |
|---|---|
| Any mandatory closure NOT_CLOSED or NOT_EVALUABLE | NOT_EVALUABLE |
| Any mandatory standing/currentness/applicability path NOT_EVALUABLE and outcome-changing | NOT_EVALUABLE |
| Relevant cycle without independently sufficient acyclic path | NOT_EVALUABLE |
| Closed set; all sufficient permit paths positively FALSE; composition resolved | FALSE |
| Closed empty set; negative chain positively establishes exact absence; composition resolved | FALSE |
| Closed set; at least one TRUE permit; every conflict/prohibition resolved in its favor by standing law | TRUE |
| TRUE permit and TRUE prohibition without standing resolution | NOT_EVALUABLE |
| Multiple permits requiring union without standing union law | Evaluate exact paths only; aggregate is NOT_EVALUABLE if q requires union |

## 18. EXACT ACYCLIC CONSTRUCTION ORDER

This section restates the construction as a complete executable semantic order,
not an implementation prescription.

| Step | Construct or assess | May depend on | Must not depend on |
|---|---|---|---|
| 0 | InputCaptureBatch I0 | Raw admitted references and observation boundary | q, S, G0, G, assessment results |
| 1 | QueryDraft q0 | I0 | S, G0, G |
| 2 | QueryBindingConstructionAssessment | q0 and upstream binding evidence | S, G |
| 3 | ResolvedQueryCore Q1 | Successful exact bindings | S, G0, G |
| 4 | AuthorityQueryIdentity q | Q1 identities | S, G0, G, query result |
| 5 | SnapshotSeed S0 | q, B0 reference, epochs, time-evidence identities | G0, G, assessment results |
| 6 | DependencyGraphBlueprint GB | q, S0, frozen table/templates, candidate references | S, G, results |
| 7 | DependencyGraphBlueprintIdentity G0 | Canonical GB structure | S, G, results |
| 8 | SnapshotConstructionAssessment | q, S0, G0, reconciled time and exact epochs | G, results |
| 9 | EvaluationSnapshotIdentity S | Successful step 8 inputs | G, results |
| 10 | AssessmentNodeIdentity values | q, S, G0, subject and dependency-node identities | Own result, G |
| 11 | Graph type/edge/candidate/acyclicity assessments | GB and node identities | G |
| 12 | Current assessment results | Dependency results in topological order | G |
| 13 | AuthorityDependencyGraph G | G0, ordered nodes/edges/result-record identities | Nothing in earlier identity depends back on G |
| 14 | AuthorityEvaluationRecord | q, S, G, AA result reference | No retroactive identity mutation |

Exact identity trace:

~~~text
I0
→ q0
→ Q1
→ q
→ S0
→ GB
→ G0
→ S
→ N1 ... Nn
→ assessment results
→ G
→ AuthorityEvaluationRecord
~~~

Forbidden traces:

~~~text
q → S → q
S → G → S
G → assessment result → G identity before evaluation
node identity → its own result
boundary admission → enclosed law → same boundary admission
~~~

If candidate discovery changes after GB or a bound epoch changes after S, the
current construction is stale. It remains historical and a new construction
starts at step 0 or the earliest lawfully reusable immutable step. No identity
is patched in place.

## 19. CLOSURE AND TERMINATION MODELS

### 19.1 Finite governance boundary

B0 identifies a finite evaluation universe:

~~~text
B0 = (
  authority_class_set,
  jurisdiction_set,
  discovery_law_registry_set,
  policy_selection_law_registry_set,
  root_registry_set,
  authority_corpus_namespace_set,
  policy_corpus_namespace_set,
  context_source_domain,
  effective_interval,
  registry_epoch_vector,
  boundary_digest
)
~~~

Closure is never universal metaphysical completeness. It is completeness over
the exact admissible domain of an independently standing, current, applicable
B0. Anything possibly outcome-changing outside an unresolved boundary makes
closure NOT_EVALUABLE.

### 19.2 Exact non-regress rule

~~~text
B0 cannot be admitted by:
  a DiscoveryLawRecord inside B0
  a PolicySelectionLawRecord inside B0
  a PolicyRecord selected under B0
  the AuthorityApplicabilityAssessment using B0

B0 admission requires:
  an acyclic predecessor standing path
  or an independently admitted applicable root bundle

if neither is available:
  GovernanceBoundaryAdmissionAssessment = NOT_EVALUABLE
  evaluator does not search for a new meta-law
  evaluator emits no FALSE or TRUE
~~~

The search terminates because:

1. each registry named by B0 is finite at its bound epoch;
2. no internal law can enlarge B0 during the same evaluation;
3. predecessor edges must move to an earlier admitted standing occurrence;
4. repeated identity indicates a cycle, not a new search level;
5. reaching an unresolved primitive boundary returns NOT_EVALUABLE.

The termination boundary is therefore explicit failure-capable input, not an
invented positive root.

### 19.3 Closure obligations by domain

| Domain | Candidate set | Closure assessment | Required before |
|---|---|---|---|
| Discovery laws | DiscoveryLawCandidateSet | DiscoveryLawCandidateSetClosureAssessment | DiscoveryLawCompositionAssessment |
| Policy-selection laws | PolicySelectionLawCandidateSet | PolicySelectionLawCandidateSetClosureAssessment | PolicySelectionLawCompositionAssessment |
| Policies | PolicyCandidateSet | PolicyCandidateSetClosureAssessment | PolicyCompositionAssessment |
| Roots | RootCandidateSet | RootCandidateSetClosureAssessment | RootConflictResolutionAssessment |
| Root controllers | RootControlDomain | IndependenceDomainClosureAssessment | RootIndependenceAssessment |
| Context sources | ContextSourceCandidateSet | ContextSourceCandidateSetClosureAssessment | ContextResolutionAssessment |
| Authority bases | AuthorityBasisCandidateSet | BasisSetClosureAssessment | AuthorityBasisCompositionAssessment |
| Negative evidence domain | NegativeEvidenceSet plus B0 domains | ExhaustivenessAssessment | NegativePropositionAssessment |

No closure assessment substitutes for another.

### 19.4 Discovery-law composition

For the closed applicable law set DL:

~~~text
CombinedCandidateDomain =
  standing composition of every effect from every L in DL
~~~

Possible results:

- union of nonconflicting corpus domains;
- standing precedence over conflicting domain definitions;
- explicit proof that one law is irrelevant to q;
- NOT_EVALUABLE.

First-match, source order, newest, most specific, local, root-labeled, and
permit-favoring defaults are forbidden.

### 19.5 Root-set and independence closure

Root closure asks whether all roots admissible for the required edge are
present. Independence closure asks whether every controlling subject and
dependency relation capable of changing R has been considered. These are
orthogonal:

~~~text
RootCandidateSetClosure = CLOSED
↛ IndependenceDomainClosure = CLOSED

IndependenceDomainClosure = CLOSED
↛ RootCandidateSetClosure = CLOSED
~~~

Only both closures, plus standing, applicability, currentness, and conflict
resolution, can make a root usable.

### 19.6 Policy-selection closure

Policy discovery is unavailable until selection-law closure and composition
resolve. Policy standing is unavailable until adoption standing and adoption
authority resolve through an acyclic predecessor/root path. Policy
applicability is evaluated only after standing.

~~~text
PolicySelectionLawRecord
↛ PolicySelectionLawStanding

PolicyStanding
↛ PolicyApplicability

PolicyApplicability
↛ PolicyCompositionResolution
~~~

### 19.7 Negative-domain closure

NegativeEvidenceSet coverage is evaluated over:

- all admissible discovery laws;
- all named authority corpora;
- every basis kind allowed by governing law;
- all aliases and event identities;
- exact q dimensions;
- exact S epochs.

An empty observed result in one corpus is an AbsenceObservation only. The
negative proposition remains NOT_EVALUABLE unless ExhaustivenessAssessment is
EXHAUSTIVE.

### 19.8 Decision completeness

A standing decision-completeness rule may prove unresolved candidates
irrelevant only when:

- its own record, standing, currentness, and applicability paths resolve;
- the candidate universe over which irrelevance is asserted is closed;
- the rule cannot be changed by an omitted candidate;
- every prohibition and conflict effect is included;
- the selected sufficient path is acyclic.

Decision completeness cannot bootstrap law-set closure.

### 19.9 Snapshot closure

Every closure assessment is snapshot-relative. A later registry, context,
policy, root, grant, revocation, or consumption-state epoch does not alter the
historical result; it invalidates current reliance and requires reconstruction.

~~~text
ClosedAt(S1)
↛ ClosedAt(S2)
~~~

## 20. REQUIRED Z1–Z10 COUNTERMODEL REPLAY

These are repair-author executions of the exact source-review specimens. They
are not an independent review.

### Z1 — Query-law split

**INPUT**

~~~text
L1 → C1(empty)
L2 → C2(valid permit)
~~~

**OLD FAILURE**

No closure existed over the discovery-law set. Evaluating only L1 allowed
query FALSE while evaluating L2 allowed TRUE or conflict.

**REPAIR PATH**

~~~text
B0 admission
→ DiscoveryLawRegistrySnapshot
→ DiscoveryLawCandidateSet {L1, L2}
→ DiscoveryLawCandidateSetClosureAssessment
→ standing/currentness/applicability for L1 and L2
→ DiscoveryLawCompositionAssessment
→ combined AuthorityBasisCandidateSet
→ BasisSetClosureAssessment
→ AuthorityBasisCompositionAssessment
~~~

**NEW RESULT**

- If B0 and the law set are closed, L1 and L2 are both evaluated. C2 is not
  omitted. The query result is the standing composition result over the permit
  and every other effect.
- If L2 membership, boundary admission, or law composition is unresolved, the
  query is NOT_EVALUABLE.
- L1-relative emptiness alone cannot produce FALSE.

**COUNTERMODEL DEFEATED? YES**

**WHY**

The two derivations no longer arise from the same admitted input. A closed law
set includes both laws; an unclosed law set fails closed. The explicit B0
boundary terminates the search without inventing a positive meta-law.

### Z2 — Policy-selector split

**INPUT**

~~~text
SL1 selects only Ppermit.
SL2 selects only Pprohibit.
~~~

**OLD FAILURE**

No selector-candidate closure or selector precedence/composition law existed.
Either policy could be omitted.

**REPAIR PATH**

~~~text
B0 admission
→ PolicySelectionLawRegistrySnapshot
→ PolicySelectionLawCandidateSet {SL1, SL2}
→ PolicySelectionLawCandidateSetClosureAssessment
→ independent standing/currentness/applicability for each SL
→ PolicySelectionLawCompositionAssessment
→ PolicyCandidateDiscoveryAssessment
→ PolicyCandidateSet {Ppermit, Pprohibit}
→ policy standing/applicability/composition
~~~

**NEW RESULT**

- With closure, both selectors contribute and both policies are evaluated.
- Without standing selector composition or policy composition, the governing
  policy assessment and query are NOT_EVALUABLE.
- Neither selector is accepted merely because it is encountered first.

**COUNTERMODEL DEFEATED? YES**

**WHY**

Policy candidate discovery has an explicit dependency on a closed,
independently standing selector-law layer. Omission and self-selection cannot
produce a positive result.

### Z3 — Root/control omission

**INPUT**

R1 is declared independent from named K while an omitted controller in K'
controls its standing.

**OLD FAILURE**

The named independence set was treated as complete. No
IndependenceDomainClosureAssessment existed.

**REPAIR PATH**

~~~text
RootCandidateDiscoveryAssessment
→ RootCandidateSetClosureAssessment
→ RootControlDomainDiscoveryAssessment
→ IndependenceDomainClosureAssessment
→ RootIndependenceAssessment
→ RootApplicabilityAssessment
→ RootConflictResolutionAssessment
~~~

**NEW RESULT**

The omitted controller prevents domain closure. RootIndependenceAssessment is
NOT_EVALUABLE, and R1 cannot terminate the authority path.

**COUNTERMODEL DEFEATED? YES**

**WHY**

Independence can no longer be TRUE relative only to a known set. Root-set
closure and control-domain closure are separate mandatory prerequisites.

### Z4 — Rule-record oracle

**INPUT**

A bare AuthorityBasisCompositionRule claims first permit wins, with no
adoption, currentness, standing, or applicability assessment.

**OLD FAILURE**

Consuming the record as standing yielded TRUE; enforcing record/standing
separation yielded NOT_EVALUABLE.

**REPAIR PATH**

~~~text
AuthorityBasisCompositionRuleRecord
→ AuthorityBasisCompositionRuleStandingAssessment
→ AuthorityBasisCompositionRuleCurrentnessAssessment
→ AuthorityBasisCompositionRuleApplicabilityAssessment
→ AuthorityBasisCompositionAssessment
~~~

**NEW RESULT**

The record alone produces no composition result. Missing assessments make
AuthorityBasisCompositionAssessment NOT_EVALUABLE. First-match authority
remains forbidden.

**COUNTERMODEL DEFEATED? YES**

**WHY**

The type table and graph make the record-to-standing cast invalid. Every
consumed rule class has its own assessment path.

### Z5 — Negative-proof cast

**INPUT**

A stale evidence reference claims no basis exists.

**OLD FAILURE**

Direct consumption yielded FALSE, while current evaluation yielded
NOT_EVALUABLE.

**REPAIR PATH**

~~~text
NegativeEvidenceReference
→ NegativeEvidenceSet
→ NegativeEvidenceAdmissionAssessment
→ NegativeEvidenceCurrentnessAssessment
→ ExhaustivenessAssessment
→ NegativePropositionAssessment
→ BasisAbsenceAssessment
→ query composition
~~~

**NEW RESULT**

The stale evidence makes NegativeEvidenceCurrentnessAssessment NOT_CURRENT or
NOT_EVALUABLE. Exhaustiveness and the negative proposition are
NOT_EVALUABLE. Query FALSE is unavailable.

**COUNTERMODEL DEFEATED? YES**

**WHY**

Evidence never receives or directly supplies a proposition disposition.
Stale, incomplete, or nonauthoritative evidence deterministically fails
closed.

### Z6 — Context injection

**INPUT**

~~~text
actual environment = production
caller ContextClaim = sandbox
only sandbox is permitted
~~~

**OLD FAILURE**

No authoritative context interface prevented the caller's false binding.

**REPAIR PATH**

~~~text
ContextClaim
+ closed ContextSourceCandidateSet
+ source standing/currentness/applicability
+ standing ContextResolutionRuleRecord path
+ standing ContextCompositionRuleRecord path
→ ContextResolutionAssessment
→ ContextBinding
→ ContextCurrentnessAssessment
→ ContextApplicabilityAssessment
~~~

**NEW RESULT**

- If the standing authoritative source resolves production, the sandbox-only
  permit path is defeated under its standing scope/context law.
- If source closure, standing, or conflict is unresolved, the query is
  NOT_EVALUABLE.
- The caller claim cannot bind sandbox by itself.

**COUNTERMODEL DEFEATED? YES**

**WHY**

ContextClaim and ContextBinding are distinct types, and the upstream semantic
owner plus current assessment path controls binding.

### Z7 — Snapshot recursion

**INPUT**

~~~text
q contains S.
S contains q and G.
G contains assessments over q@S.
~~~

**OLD FAILURE**

Two implementations could allocate identities in different recursive orders.

**REPAIR PATH**

~~~text
I0 → q0 → Q1 → q → S0 → GB → G0 → S
→ node identities → assessment results → G
→ AuthorityEvaluationRecord
~~~

**NEW RESULT**

q excludes S and G. S binds q and G0, not G. G is an output constructed after
assessment. The same frozen inputs and canonical structural encoding have one
declared order.

**COUNTERMODEL DEFEATED? YES**

**WHY**

No object's identity requires its own completed identity. Any implementation
using the old cyclic shape violates the construction contract and produces no
admitted evaluation record.

### Z8 — Immediate self-revocation

**INPUT**

Grant G is A's only authority to revoke G. Revocation R is issued and effective
at the same instant.

**OLD FAILURE**

Pre-state evaluation made R valid and G revoked. Post-state evaluation made A
unauthorized and R invalid. No equal-time law selected a state.

**REPAIR PATH**

~~~text
RevocationAct
→ standing/effective/observation bindings
→ RevocationTemporalOrderingAssessment
→ standing RevocationStateSelectionRule path
→ RevocationAuthorityStateSelectionAssessment
→ complete RevocationAuthorityAssessment
→ CurrentRevocationAssessment
~~~

**NEW RESULT**

If an independently standing applicable rule selects a state, the authority
subquery is evaluated at exactly that state. If no such rule resolves,
RevocationAuthorityStateSelectionAssessment, RevocationAuthorityAssessment,
and CurrentRevocationAssessment are NOT_EVALUABLE. No intuitive pre-state or
post-state default is applied.

**COUNTERMODEL DEFEATED? YES**

**WHY**

The divergence is converted into an explicit missing-law dependency with one
fail-closed result. The repair does not choose which state is normatively
correct.

### Z9 — Retry/replay collision

**INPUT**

Act A is admitted. Processing crashes before consumption. The same semantic
event is redelivered.

**OLD FAILURE**

The redelivery was both reuse of an admitted act and retry of one event
identity.

**REPAIR PATH**

~~~text
SemanticEventIdentity E
+ DeliveryIdentity D
+ ProcessingAttemptIdentity P
+ AdmissionIdentity A
+ ProcessingTerminalStateAssessment
+ AuthorizationActConsumptionStateAssessment
+ standing RetryAdmissionRule path
→ EventReuseClassificationAssessment
~~~

**NEW RESULT**

When durable state establishes NONTERMINAL and UNCONSUMED for the same E and A,
the redelivery is RETRY if the standing retry law permits. It is not REPLAY.
If durable state is unresolved, classification is NOT_EVALUABLE. Redelivery
after durable terminal consumption is REPLAY.

**COUNTERMODEL DEFEATED? YES**

**WHY**

Replay is narrower than redelivery and is separated from retry by terminal and
consumption state. The classifications are disjoint outcomes of one assessment.

### Z10 — Supersession survival

**INPUT**

P1 validly issues perpetual G. P2 supersedes P1 and either preserves existing
grants or says nothing.

**OLD FAILURE**

Policy current exclusion was allowed to make the grant basis FALSE even though
survival was unresolved.

**REPAIR PATH**

~~~text
PolicySupersessionAssessment
+ GrantPolicyDependencyAssessment
+ standing/current/applicable SupersessionSurvivalRule path
→ SurvivalAssessment
→ GrantCurrentnessAssessment
→ BasisPathAssessment
~~~

**NEW RESULT**

- Express preservation under standing law may yield SURVIVES.
- Express invalidation under standing law may yield DOES_NOT_SURVIVE.
- Silence without a standing default yields NOT_EVALUABLE.
- P1 exclusion alone never yields GrantBasisFALSE.

**COUNTERMODEL DEFEATED? YES**

**WHY**

Grant-policy dependency and survival are assessed separately from policy-set
currentness. No default survival or invalidation is invented.

### Z1–Z10 replay summary

| Case | New repair-session result | Countermodel defeated? |
|---|---|---|
| Z1 | Both laws evaluated or NOT_EVALUABLE | YES |
| Z2 | Both selectors/policies evaluated or NOT_EVALUABLE | YES |
| Z3 | Omitted controller prevents independence | YES |
| Z4 | Bare rule record cannot compose | YES |
| Z5 | Stale evidence cannot establish FALSE | YES |
| Z6 | Caller claim cannot bind authoritative context | YES |
| Z7 | Fixed acyclic construction order | YES |
| Z8 | Standing state-selection law or NOT_EVALUABLE | YES |
| Z9 | RETRY / REPLAY disjoint; uncertainty NOT_EVALUABLE | YES |
| Z10 | Survival rule required; no default | YES |

~~~text
Z_REPLAY_AUTHOR_CLAIM != INDEPENDENT_REVIEW
COUNTERMODEL_DEFEATED_AUTHOR_CLAIM != PASS
~~~

## 21. ADDITIONAL HOSTILE SPECIMENS

These specimens were generated because the repair creates new explicit
boundaries. They do not expand repair authority.

### H2-01 — Boundary self-admission

**INPUT:** B0 names L0; L0 says B0 is standing; no predecessor or root exists.

**REQUIRED RESULT:** A relevant boundary-provenance cycle.
GovernanceBoundaryAdmissionAssessment is NOT_EVALUABLE.

**NEW DEFECT EXPOSED:** None beyond IHR-B01/IHR-B04. The explicit cycle is the
intended fail-closed result.

### H2-02 — Two boundary bundles disagree

**INPUT:** Independently presented B0 and B1 name disjoint discovery-law
registries for the same authority class and jurisdiction; no boundary
precedence law is standing.

**REQUIRED RESULT:** Boundary admission/composition is NOT_EVALUABLE; neither
boundary is selected by order.

**NEW DEFECT EXPOSED:** Cross-boundary federation and precedence remain an
unresolved root. No cross-organ doctrine repair is authorized here.

### H2-03 — Discovery-law alias collision

**INPUT:** Two records have equal content digests but distinct adoption events
and standing paths.

**REQUIRED RESULT:** Do not alias by digest. Law-set closure is
NOT_EVALUABLE until identity relation resolves.

**NEW DEFECT EXPOSED:** Canonical cross-registry alias adjudication remains
unresolved.

### H2-04 — Root controller discovered after S

**INPUT:** RootControlDomain closed at S1; a new controlling relation is
observed before consequence snapshot S2.

**REQUIRED RESULT:** S1 remains historical. Current independence at S2 is not
established; reconstruct and reassess.

**NEW DEFECT EXPOSED:** None. This exercises currentness rather than widening
root authority.

### H2-05 — Context source conflict

**INPUT:** A standing deployment source reports production while a standing
test-harness source reports sandbox for the same dimension and epoch.

**REQUIRED RESULT:** Without a standing applicable ContextCompositionRule,
ContextResolutionAssessment is NOT_EVALUABLE.

**NEW DEFECT EXPOSED:** Actual context-source precedence remains unresolved.
No implementation owner is selected.

### H2-06 — Negative evidence over the wrong context

**INPUT:** A current exhaustive sandbox registry proves no basis, while q is
authoritatively bound to production.

**REQUIRED RESULT:** ExhaustivenessAssessment is NON_EXHAUSTIVE or
NOT_EVALUABLE for q. No query FALSE.

**NEW DEFECT EXPOSED:** None. Exact context binding is part of the negative
domain.

### H2-07 — Blueprint mutation after snapshot

**INPUT:** GB omits L2; L2 is discovered after G0 and S are constructed.

**REQUIRED RESULT:** GraphCandidateCoverageAssessment fails for current use.
The old record remains historical; construction restarts before GB.

**NEW DEFECT EXPOSED:** Runtime invalidation signaling is not specified and
remains implementation work outside scope.

### H2-08 — Consumption committed, acknowledgement lost

**INPUT:** Consumption is durably recorded, then the processor crashes before
acknowledgement. The same E/A is redelivered.

**REQUIRED RESULT:** REPLAY, not RETRY, because durable consumption is terminal
for reliance.

**NEW DEFECT EXPOSED:** Crash-consistent persistence and atomicity are runtime
questions not repaired here.

### H2-09 — Consumption stores disagree

**INPUT:** One standing source reports CONSUMED; another reports UNCONSUMED; no
standing reconciliation rule applies.

**REQUIRED RESULT:** AuthorizationActConsumptionStateAssessment and
EventReuseClassificationAssessment are NOT_EVALUABLE.

**NEW DEFECT EXPOSED:** Consumption-state source reconciliation remains an
unresolved downstream root.

### H2-10 — Partial policy survival

**INPUT:** P2 preserves READ grants issued under P1 but is silent on WRITE; G
contains READ and WRITE.

**REQUIRED RESULT:** READ may continue only if membership and every other
dependency resolve. WRITE is NOT_EVALUABLE absent a standing silence rule.
No whole-grant default.

**NEW DEFECT EXPOSED:** Dimension-specific survival comparison remains
dependent on standing law.

### H2-11 — Survival rule supersedes itself

**INPUT:** The only rule preserving P1 grants is inside P1 and is claimed
excluded by P2; no independent survival rule decides whether it survives.

**REQUIRED RESULT:** SurvivalAssessment is NOT_EVALUABLE due to a rule
currentness/provenance dependency.

**NEW DEFECT EXPOSED:** None beyond IHR-B10; self-preserving survival rules are
now visible.

### H2-12 — Revocation effective before occurrence

**INPUT:** R asserts an effective time before its admitted occurrence. No
standing retroactivity rule exists.

**REQUIRED RESULT:** RevocationTemporalOrderingAssessment and
CurrentRevocationAssessment are NOT_EVALUABLE. The bytes do not create
retroactivity.

**NEW DEFECT EXPOSED:** Actual retroactivity law remains unresolved.

### New-risk register

| ID | Risk exposed by repair | Standing in this artifact |
|---|---|---|
| NR-01 | Cross-boundary federation/composition | RECORDED, NOT_REPAIRED, unresolved root |
| NR-02 | Canonical identity encoding and digest algorithm | RECORDED, implementation out of scope |
| NR-03 | Runtime graph invalidation signaling | RECORDED, runtime out of scope |
| NR-04 | Crash-consistent consumption-state persistence | RECORDED, runtime out of scope |
| NR-05 | Cross-source consumption-state reconciliation | RECORDED, downstream semantic root unresolved |
| NR-06 | Cross-registry law/root/event alias adjudication | RECORDED, shared ontology not authorized |

~~~text
NewRiskRecorded != NewRiskRepaired
NewRiskRecorded != ScopeExpansion
~~~

## 22. IHR-B01–IHR-B10 CLOSURE MATRIX

Every status below is the repair author's claim. None is an independent
disposition.

| Finding | Root defect repaired | Principal repair path | Exact hostile result | Repair-session status |
|---|---|---|---|---|
| IHR-B01 | Discovery-law record/standing/applicability/set-closure/composition collapse | B0 → closed DiscoveryLawCandidateSet → law assessments → law composition → basis closure | L1 cannot hide L2; incomplete boundary/law set returns NOT_EVALUABLE | AUTHOR_CLAIMS_CLOSED |
| IHR-B02 | Known root/control set treated as complete | closed RootCandidateSet + closed RootControlDomain before independence/conflict/applicability | R2/controller omission blocks root use | AUTHOR_CLAIMS_CLOSED |
| IHR-B03 | Graph/type inventory divergence and forbidden dispositions | Frozen table with one type per node; assessment-only outcome algebras | Untyped node or cross-type disposition blocks graph | AUTHOR_CLAIMS_CLOSED |
| IHR-B04 | Ungraphed selection-law dependency and self-validation | closed PolicySelectionLawCandidateSet + independent selector standing + explicit discovery edge | Selector split/self-selection returns composed result or NOT_EVALUABLE | AUTHOR_CLAIMS_CLOSED |
| IHR-B05 | Evidence-to-FALSE cast | NegativeEvidenceSet → ExhaustivenessAssessment → NegativePropositionAssessment → BasisAbsenceAssessment | Stale/incomplete/nonauthoritative evidence returns NOT_EVALUABLE | AUTHOR_CLAIMS_CLOSED |
| IHR-B06 | Caller-owned untyped context | ContextClaim/source/binding/currentness/applicability under AUTHORITATIVE_CONTEXT_RESOLUTION_INTERFACE | Caller sandbox claim cannot override production binding | AUTHOR_CLAIMS_CLOSED |
| IHR-B07 | q/S/G recursive identities | q → S0 → GB/G0 → S → nodes/results → G | No identity requires its own completion | AUTHOR_CLAIMS_CLOSED |
| IHR-B08 | Hidden revocation-authority subquery and intuitive state choice | RevocationAct + time bindings + standing state-selection law + complete REVOKE_GRANT assessment | Equal-time unresolved law returns NOT_EVALUABLE | AUTHOR_CLAIMS_CLOSED |
| IHR-B09 | Redelivery defined as both retry and replay | E/D/P/A identities + terminal/consumption state + one classification assessment | Pre-consumption redelivery is RETRY or NOT_EVALUABLE, never both | AUTHOR_CLAIMS_CLOSED |
| IHR-B10 | Policy exclusion cast into grant invalidity | GrantPolicyDependency + standing SupersessionSurvivalRule + SurvivalAssessment | Preservation/invalidation/silence have distinct results | AUTHOR_CLAIMS_CLOSED |

Closure claim conditions:

~~~text
AUTHOR_CLAIMS_CLOSED
!= INDEPENDENTLY_CLOSED

AUTHOR_CLAIMS_CLOSED
!= PASS

AUTHOR_CLAIMS_CLOSED
!= ADOPTED

AUTHOR_CLAIMS_CLOSED
!= RATIFIED
~~~

## 23. SURVIVING UNRESOLVED ROOTS

The following predecessor roots remain unresolved and unchanged:

- human or Founder-origin proof;
- a positive constitutional root;
- root-admission authority;
- root independence adjudication;
- root conflict precedence and cross-jurisdiction recognition;
- principal, actor, role, operation, target, context, and custody registries;
- role self-activation;
- standing time sources and time-source reconciliation;
- policy-corpus authority and closure;
- policy adoption authority and first predecessor;
- policy precedence and composition;
- authority-record corpus ownership and completeness;
- grant aliases and cross-corpus identity;
- multi-basis composition;
- revocation comparison, conflict, retroactivity, and survivorship;
- arbitrary predicate implication and evaluator standing;
- authorization-act taxonomy;
- intrinsic-use and consumption mapping;
- downstream mutation-eligibility policy.

The following roots exposed by the exact source review remain unresolved as
positive facts even though their dependency shapes are repaired:

- governance-boundary admission standing;
- discovery and closure of discovery/query laws;
- discovery-law composition;
- policy-selection-law candidate closure;
- policy-selection-law composition;
- root-candidate-set closure;
- root-control-domain closure;
- standing assessments for every consumed rule class;
- authoritative context-source standing and composition;
- negative-evidence source authority and exhaustive domain coverage;
- canonical acyclic identity encoding;
- revocation authority-state and equal-time law;
- retry-admission and consumption-state reconciliation law;
- policy-supersession-to-grant-survival law.

Newly explicit unresolved roots:

- cross-boundary federation and boundary precedence;
- cross-registry law/root/event alias adjudication;
- context-source precedence across standing sources;
- semantic event identity authority;
- delivery, attempt, admission, and consumption-state source authority;
- canonical graph serialization and digest algorithm;
- runtime snapshot invalidation signaling;
- crash-consistent consumption persistence.

No unresolved root is treated as false, true, standing, or applicable merely
because it is named.

~~~text
UnresolvedRoot != FalseRoot
UnresolvedRoot != ValidRoot
NamedInterface != StandingInterface
TypedBoundary != AdmittedBoundary
NoPositiveRootInvented
~~~

This report supplies no positive RootResolutionBundle and no positive
GovernanceBoundaryAdmissionAssessment for a real-world query. Real queries
that require either remain NOT_EVALUABLE until separately established.

## 24. CARRY-FORWARD A–W TRACE REPLAY

These traces verify that the new repair mechanisms do not weaken surviving
Repair 001 results.

| Trace | Input pressure | Repair 002 path | Repair-session authority result |
|---|---|---|---|
| A | Founder-like packet self-claims ROOT/FULL/GLOBAL | Boundary/root/basis/policy/context closure absent | NOT_EVALUABLE |
| B | Required role mismatches one basis | Exact BasisPathAssessment FALSE; alternate basis closure absent | Query NOT_EVALUABLE |
| C | Direct grant text says no role | Grant/policy/selector/basis standing and closure unresolved | NOT_EVALUABLE |
| D | Target outside one grant | ScopeApplicabilityAssessment defeats exact path; alternatives unclosed | Query NOT_EVALUABLE |
| E | Issuer proven unauthorized | GrantStandingAssessment path FALSE; alternatives unclosed | Query NOT_EVALUABLE |
| F | One grant expired | GrantCurrentnessAssessment NOT_CURRENT for exact path; alternatives unclosed | Query NOT_EVALUABLE |
| G | Standing effective revocation defeats one grant | CurrentRevocationAssessment defeats exact path; alternatives unclosed | Query NOT_EVALUABLE |
| H | Parent revoked; child survivorship absent | Delegation and survival dependencies unresolved | NOT_EVALUABLE |
| I | Child wider/disjoint from parent | Proven outside portion FALSE; severable remainder requires standing law | Query aggregate NOT_EVALUABLE |
| J | Grant applies only in foreign jurisdiction | Exact jurisdiction path NOT_APPLICABLE/FALSE under standing rule; alternatives unclosed | Query NOT_EVALUABLE |
| K | Grant issued under superseded policy | SurvivalAssessment required; no default false | NOT_EVALUABLE unless standing survival rule resolves |
| L | Historical act predates amendment | S1 remains history; reconstruct policy/basis at S2 | Current query NOT_EVALUABLE pending reassessment |
| M | Quote substitutes for authorization act | Event/admission identity not established; no closed basis | NOT_EVALUABLE |
| N | One-use act consumed and redelivered | Consumption durable → REPLAY; grant authority assessed separately | Claimed reliance blocked; authority separately TRUE/FALSE/NOT_EVALUABLE |
| O | Distinct lawful reissuance; every authority dependency stipulated resolved | New E/A; closed policies/bases; acyclic graph stipulated | TRUE as authority prerequisite only |
| P | Session basis used for repository operation | Operation/target scope mismatch on exact path; alternatives unclosed | Query NOT_EVALUABLE |
| Q | Subject issues and validates own grant | Relevant authority provenance cycle | NOT_EVALUABLE |
| R | Same runtime has independently rooted roles | Role facts do not close authority basis/root domains | NOT_EVALUABLE |
| S | Condition true at t1, false at t2 | Exact path FALSE at S2; alternatives unclosed | Query NOT_EVALUABLE |
| T | Operation exact; target unresolved | QueryBindingConstructionAssessment cannot resolve Q1 | NOT_EVALUABLE |
| U | Authority fully stipulated TRUE; safety false | Downstream firewall preserves authority result | Authority TRUE; mutation ineligible |
| V | Policy self-claims ratification | Adoption/selector provenance cycle | NOT_EVALUABLE |
| W | Request says CURRENT/NOW | Standing time, B0, selector, policy, and basis closure unresolved | NOT_EVALUABLE |

Carry-forward invariants:

~~~text
ExactPathFailure
↛ GlobalQueryFALSE

HistoricalAuthorityAtS1
↛ CurrentAuthorityAtS2

AuthorityTRUE
↛ MutationEligible

ConsumedAuthorizationAct
↛ GrantExhausted
~~~

## 25. CARRY-FORWARD X1–X15 ATTACK REPLAY

| Case | Pressure input | Repair 002 path and result |
|---|---|---|
| X1 | Valid permit and prohibition both apply | Closed basis set plus standing basis composition required; absent resolution, query NOT_EVALUABLE |
| X2 | P1 requires role, P2 says role not required | Closed selector/policy sets plus standing policy composition required; absent resolution, NOT_EVALUABLE |
| X3 | Target revision changes during evaluation | S becomes stale for current use; preserve history and reconstruct q/S/G0 |
| X4 | Revocation races the query snapshot | Effective/observation/query ordering plus state-selection law required; unresolved result NOT_EVALUABLE |
| X5 | P2 becomes effective before consequence snapshot | S1 remains historical; rebuild selection/policy/basis graph at S2 |
| X6 | Actor attribution corrected from A to B | Old binding remains historical; new Q1/q/S required for B |
| X7 | Standing time sources disagree across expiry boundary | Standing TimeReconciliationRule required; absent resolution, snapshot/query NOT_EVALUABLE |
| X8 | Partial revocation removes WRITE from READ/WRITE parent | WRITE child path may be FALSE; READ needs standing survivorship law; aggregate remains NOT_EVALUABLE when unresolved |
| X9 | Two applicable roots conflict | Closed RootCandidateSet plus standing RootConflictRule required; absent resolution, NOT_EVALUABLE |
| X10 | AA at S1 is stale before consequence gate | S1 remains historical; downstream eligibility requires refreshed authority |
| X11 | Registry claims exhaustive absence | NegativeEvidenceSet chain plus B0/law/basis closure required; only a positive NegativePropositionAssessment can support FALSE |
| X12 | Child permission is nonempty and disjoint from parent | Exact child path FALSE under standing comparison law; query still aggregates other bases |
| X13 | Role neutrality comes from unresolved grant/policy | RoleRequirementResolution cannot resolve before grant/policy standing and selector closure; NOT_EVALUABLE |
| X14 | Parent/child predicate implication undecidable | Delegation path NOT_EVALUABLE; no silent NARROWER cast |
| X15 | P recognizes G and G authorizes P | Explicit adoption and issuance edges expose relevant policy/authority cycles; NOT_EVALUABLE |

No X result introduces first-match, implicit union, positive root, intuitive
time ordering, or downstream mutation authority.

## 26. CARRY-FORWARD Y1–Y15 ATTACK REPLAY

| Case | Pressure input | Repair 002 path and result |
|---|---|---|
| Y1 | Discovery/query law expired before S | DiscoveryLawCurrentnessAssessment blocks use; law composition and query NOT_EVALUABLE |
| Y2 | Equal grant digest, distinct issuance events | Do not alias by payload; basis closure NOT_EVALUABLE until identity relation resolves |
| Y3 | Newest-wins selector depends on newest selected policy | Policy-selection provenance cycle; selector standing NOT_EVALUABLE |
| Y4 | Earlier nonexhaustive empty search precedes later permit | Earlier NegativePropositionAssessment was NOT_EVALUABLE, never lawful FALSE |
| Y5 | Negative evidence from old corpus epoch reused | NegativeEvidenceCurrentnessAssessment NOT_CURRENT; query NOT_EVALUABLE |
| Y6 | Actor epoch and grant-index epoch incompatible | SnapshotConstructionAssessment or graph coverage NOT_EVALUABLE; reconstruct or block |
| Y7 | Undisclosed actor controls candidate root | IndependenceDomainClosureAssessment not CLOSED; independence NOT_EVALUABLE |
| Y8 | Unauthorized union exceeds issuer ceilings | Evaluate exact paths only; no union without standing composition |
| Y9 | Production prohibition may apply; caller context unresolved | Authoritative context resolution required; query NOT_EVALUABLE until bound |
| Y10 | Revocation bytes self-assert retroactivity | Standing temporal/state-selection rule required; current/historical effect NOT_EVALUABLE |
| Y11 | Required predicate evaluator unavailable | Predicate/condition path NOT_EVALUABLE; policy standing remains separate |
| Y12 | Two incomparable maximal policies | Apply independently standing partial-order composition or return NOT_EVALUABLE |
| Y13 | Direct path sufficient; delegated cycle claimed irrelevant | TRUE only with closed candidates and standing law proving direct path sufficient and cycle outcome-irrelevant |
| Y14 | Oral grants lawful outside queried corpus | If B0 admits oral domain but discovery omits it, law/basis closure fails and query is NOT_EVALUABLE |
| Y15 | One authorization act consumed | Consumption blocks that reliance; GrantUseStateAssessment remains separate |

~~~text
X_Y_REPLAY = REPAIR_AUTHOR_PRESSURE_TEST
X_Y_REPLAY != INDEPENDENT_REVIEW
~~~

## 27. EXACT REPAIR CLAIMS, NONCLAIMS, AND HOLDS

### Repair claims

This repair author claims only:

- every exact IHR-B01 through IHR-B10 countermodel now has a typed repair path;
- each path produces one declared result or fail-closed NOT_EVALUABLE;
- every graph node has one primary semantic type;
- the q/S/G identity construction is acyclic;
- no positive root is invented;
- surviving Repair 001 non-collapse laws remain;
- Z1 through Z10 are defeated under the candidate model as an author claim.

### Nonclaims

This artifact does not claim:

- independent PASS;
- independent closure of any finding;
- canonical standing;
- constitutional standing;
- adoption;
- ratification;
- seal;
- Founder approval;
- human-origin proof;
- actual root admission;
- actual B0 standing;
- actual discovery-law or selector-law closure;
- actual policy, root, context, time, corpus, event, admission, or survival
  standing;
- implementation completeness;
- schema validity;
- runtime correctness;
- storage durability;
- deployment readiness;
- mutation eligibility;
- execution authority.

~~~text
ModelCanRepresent(TRUE)
!= TRUEEstablished

AuthorClaimsCountermodelDefeated
!= IndependentCountermodelDefeated

SemanticRepairCandidate
!= ExecutableAuthoritySystem
~~~

### Exact branch holds

~~~text
GENE_AUTHORITY_BRANCH = HOLD
GENE_STANDING = UNCHANGED
GENE_FILE_MUTATION = NOT_AUTHORIZED

FOUNDATION_AUTHORITY_BRANCH = HOLD
FOUNDATION_STANDING = UNCHANGED
FOUNDATION_FILE_MUTATION = NOT_AUTHORIZED

SELFIR = ACTIVE_ON_UNRELATED_BRANCHES
NOTEPAD_INTEGRATION = DEFERRED
~~~

Unrelated SELFIR work may continue only under its own authority. It must not
consume this candidate as standing authority, repair Gene or Foundation IR,
resolve Notepad semantics, or project this report into another source organ.

### Exact out-of-scope mutation statement

This repair does not modify:

- Gene;
- Foundation IR;
- AgentBridge;
- DATASELF;
- Notepad;
- ClaudeSELF;
- shared ontology;
- implementation;
- schema;
- runtime;
- deployment;
- any predecessor artifact.

The authorized publication boundary is exactly one new report path:

~~~text
governance/
AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_
SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_002.md
~~~

### Downstream firewall

~~~text
AuthorityApplicabilityAssessment = TRUE
↛ MutationEligibilityDecision = ELIGIBLE

RepairArtifactPublished
↛ AuthorityApplicabilityAssessment = TRUE

RepairArtifactPublished
↛ AnyMutationAuthorized
~~~

## 28. EXACT NEXT GATE ONLY

The only next gate named by this repair is:

~~~text
FRESH INDEPENDENT HOSTILE REVIEW OF BOUNDED REPAIR 002
~~~

Required review posture:

~~~text
ReviewerSession != ThisRepairSession
Review = READ_ONLY
Review != Repair
Review != Adoption
Review != Ratification
Review != Seal
~~~

Required exact input witness:

- connected GitHub repository identifier;
- exact published branch;
- exact full commit SHA;
- exact artifact path;
- exact Git blob;
- exact line count;
- exact byte count;
- exact SHA-256;
- exact one-path commit boundary.

Required hostile pressure:

- independently re-extract IHR-B01 through IHR-B10 from the source review;
- independently test every author-claimed closure;
- rerun Z1 through Z10;
- attack H2-01 through H2-12;
- verify the complete type table against every graph node;
- verify q/S/G construction has no hidden identity recursion;
- verify all rule records have standing/currentness/applicability paths;
- verify no closure assessment bootstraps B0;
- verify no evidence reference casts directly to FALSE;
- verify retry/replay disjointness under crash boundaries;
- verify policy exclusion never defaults grant survival or invalidation;
- return PASS, CHANGES_REQUIRED, or NOT_EVALUABLE without repair.

This artifact does not open, perform, or prejudge that review.

~~~text
POST_AUTHORING_STANDING:
  BOUNDED_REPAIR_CANDIDATE
  NONCANONICAL
  NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
  NOT_ADOPTED
  NOT_RATIFIED

NEXT_GATE:
  FRESH INDEPENDENT HOSTILE REVIEW OF BOUNDED REPAIR 002

STOP_AFTER_PUBLICATION_SIGNAL:
  REQUIRED
~~~
