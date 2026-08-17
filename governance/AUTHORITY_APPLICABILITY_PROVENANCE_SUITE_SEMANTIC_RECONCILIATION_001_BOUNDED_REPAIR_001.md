# AUTHORITY_APPLICABILITY_PROVENANCE_SUITE — Semantic Reconciliation 001 — Bounded Repair 001

~~~text
ARTIFACT_CLASS:
  BOUNDED_SEMANTIC_REPAIR_CANDIDATE

AUTHORING_RUNTIME:
  CODEXSELF

REPAIR_SCOPE:
  BLOCKING_FINDINGS_B1_THROUGH_B7_ONLY

SOURCE_STANDING:
  SEMANTIC_CANDIDATE
  NON_EXECUTABLE
  NONCANONICAL

REPAIR_STANDING:
  CANDIDATE
  NONCANONICAL
  NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
  NOT_ADOPTED
  NOT_RATIFIED

REVIEW_RESULT_CONSUMED:
  CHANGES_REQUIRED

REVIEWER_SESSION:
  DISTINCT_FROM_THIS_REPAIR_SESSION

GENE_AUTHORITY_BRANCH:
  HOLD

FOUNDATION_AUTHORITY_BRANCH:
  HOLD

SELFIR:
  ACTIVE_ON_UNRELATED_BRANCHES

NOTEPAD_INTEGRATION:
  DEFERRED

MUTATIONS_AUTHORIZED_BY_THIS ARTIFACT:
  NONE
~~~

This artifact repairs only the seven blocking findings identified by the exact
independent hostile-review response bound in section 2. It does not rewrite the
authoring target. It does not adopt the repaired vocabulary. It does not
establish a constitutional root. It does not decide that the repair passes
independent review.

The surviving non-collapse laws remain:

~~~text
Evidence != Authority
Occurrence != Standing
Standing != Applicability

GrantRepresentation
!= GrantIssuanceEvent
!= GrantStandingRecord
!= GrantCurrentnessAssessment

AuthorizationAct
!= CurrentAuthorizationReliance
!= MutationEligibilityDecision
!= MutationOccurrence

AuthorityApplicability
!= MutationEligibility

Replay
!= Retry
!= LawfulReissuance

SemanticRepair != GeneMutation
ReportArtifactCreation != ConstitutionalPromotion
AuthorityBranchBlocked != SELFIRBlocked
ClaudeSELFReality != CodexSELFReality
~~~

For this repair, let an authority query be:

~~~text
q = (
  actor_binding,
  governed_operation_binding,
  governed_target_binding,
  context_binding,
  evaluation_snapshot_identity
)
~~~

Every current assessment in this artifact is relative to the same exact query
and evaluation snapshot unless a historical snapshot is named explicitly.

## 1. TARGET INTEGRITY WITNESS

The actual authoring target bytes were read from:

~~~text
/Users/millysituated/
AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_
SEMANTIC_RECONCILIATION_001.md
~~~

| Witness field | Live value before repair |
|---|---|
| File type | Regular file |
| Line count | 1,242 |
| Byte size | 47,993 |
| SHA-256 | 3a62d0040b0d1041bdfdfd284549ed66e2e768c18b48f1eb66c962864c750a28 |
| Expected SHA-256 | 3a62d0040b0d1041bdfdfd284549ed66e2e768c18b48f1eb66c962864c750a28 |
| Integrity disposition | EXACT_MATCH |
| Git custody at source path | None; /Users/millysituated is not a Git worktree |

The target was not edited, copied over, normalized, or replaced. Its reported
digest is the input identity for this repair.

Read-only witness commands:

~~~bash
stat -f 'path=%N type=%HT bytes=%z inode=%i modified=%Sm' \
  -t '%Y-%m-%dT%H:%M:%S%z' \
  /Users/millysituated/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001.md

wc -l -c \
  /Users/millysituated/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001.md

shasum -a 256 \
  /Users/millysituated/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001.md

nl -ba \
  /Users/millysituated/AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_SEMANTIC_RECONCILIATION_001.md
~~~

## 2. REVIEW INPUT INTEGRITY WITNESS

The authoritative review input was not reconstructed from memory. The exact
assistant review response was recovered from the live Codex session artifact:

~~~text
SESSION_ARTIFACT:
  /Users/millysituated/.codex/sessions/2026/08/17/
  rollout-2026-08-17T07-58-05-
  01a00f96-06a2-7e71-9117-f7ed804dc031.jsonl

RESPONSE_MESSAGE_ID:
  msg_017c15a48b640c0e016a82f4fc2ed08194a43bb5af984582a3

RESPONSE_ROLE:
  assistant

RESPONSE_TITLE:
  CODEXSELF Independent Hostile Review 001

RESPONSE_VERDICT:
  CHANGES_REQUIRED

EXTRACTED_RESPONSE_NEWLINE_COUNT:
  567

EXTRACTED_RESPONSE_BYTE_SIZE:
  35,201

EXTRACTED_RESPONSE_SHA_256:
  03fa6ce4e0a574a4e503fd77cc96db3c8333135403bafb02a65a7586b95b60f2
~~~

The hash is over the exact output-text value selected by message identity,
without an added terminal newline. The whole JSONL file is append-only session
custody and may continue to grow; the message identity plus extracted message
digest is the stable review-input witness used here.

Extraction witness:

~~~bash
jq -jr \
  --arg message_id msg_017c15a48b640c0e016a82f4fc2ed08194a43bb5af984582a3 \
  'select(
     .type == "response_item"
     and .payload.type == "message"
     and .payload.id == $message_id
   )
   | .payload.content[]
   | select(.type == "output_text")
   | .text' \
  REVIEW_SESSION.jsonl
~~~

The review message itself reports the target integrity witness above and names
B1 through B7 exactly. No authoring-session confidence was substituted for the
review result.

## 3. EXACT B1-B7 INVENTORY

| ID | Exact blocking finding consumed |
|---|---|
| B1 | Authority-basis aggregation is absent. The target defines edge/path failures but not the complete set of candidate grants, policies, roots, or proof paths for an actor-operation-target query. One expired grant can produce FALSE while another valid grant produces TRUE. Both results are permitted by the current text. |
| B2 | The external root set is an untyped oracle. ExternallyAdoptedStandingRoots is used as successful recursion termination, but no upstream interface establishes root identity, adoption, provenance, independence, applicability, currentness, or set membership. External != Independent. |
| B3 | Policy standing and policy applicability are internally collapsed. The object table makes PolicyStandingAssessment include applicability while the policy section declares it distinct from PolicyApplicabilityAssessment. |
| B4 | The proof DAG omits policy-adoption authority and governing-policy selection. This admits the hidden cycle PolicyStanding(P) → AdoptionStanding(P) → AuthorityToAdopt(P) → PolicyStanding(P) when no predecessor policy or independent root exists. |
| B5 | The object/type inventory is incomplete. Objects used later but left untyped include IssuerAuthorityAssessment, DelegationChainAssessment, CurrentRevocationAssessment, PolicyApplicabilityAssessment, TimeFreshnessAssessment, CurrentSourceReliance, ActIdentityDisposition, and ActAdmissionAttempt. Cycle and lifecycle laws cannot be applied completely to an untyped graph. |
| B6 | The 7+5 decomposition is neither minimal nor complete. Actor attribution and predicate evaluation are generic upstream functions, while root admission, policy selection/precedence, proof-basis discovery/exhaustiveness, and time-source reconciliation are missing semantic surfaces. |
| B7 | FALSE and NOT_EVALUABLE are mapped at the wrong semantic level. Several entries establish only that one proof path failed, not that the entire authority query is false. GRANT_NOT_FOUND and POLICY_STALE are also treated unconditionally despite depending on whether negative evidence is complete and authoritative. |

The inventory is reproduced from the exact review response. It is not a
paraphrase used to alter scope.

## 4. B1 REPAIR

### FINDING

The target lacks a query-level authority-basis discovery, closure, and
aggregation model. It can evaluate an individual path but cannot determine
whether that path is the only relevant path or how multiple paths compose.

### COUNTERMODEL

~~~text
Query q has two candidate grant paths:

  G1:
    exact actor, operation, target
    expired at snapshot S
    BasisPathAssessment(G1) = FALSE

  G2:
    exact actor, operation, target
    current and otherwise satisfied at S
    BasisPathAssessment(G2) = TRUE

Old target:
  G1 permits query FALSE
  G2 permits query TRUE

No rule determines which path set is complete
or which query disposition follows.
~~~

### ROOT DEFECT

The old proof graph begins after a grant or root has already been selected. It
has no typed object for:

- discovering every candidate authority basis relevant to q;
- proving whether the discovery domain is complete;
- distinguishing a single path result from the query result;
- classifying each basis as permitting, prohibiting, or otherwise constraining;
- applying standing precedence or composition law;
- proving that an unresolved or undiscovered basis cannot change the result.

### REPAIR

Introduce these distinct current objects:

~~~text
AuthorityBasisDiscoveryAssessment(q, S)
AuthorityBasisCandidateSet(q, S)
BasisSetClosureAssessment(q, S)
BasisPathAssessment(basis, q, S)
AuthorityBasisCompositionAssessment(q, S)
AuthorityApplicabilityAssessment(q, S)
~~~

Authority basis is a set or dependency graph, never implicitly one grant.

AuthorityBasisDiscoveryAssessment must record:

- exact q and S;
- every governed corpus queried;
- the standing query law for each corpus;
- the returned basis identities;
- source epochs or revisions;
- unresolved corpora;
- whether the query domain is exhaustive for q;
- any authoritative negative proof;
- conflicts or aliases among returned identities.

BasisSetClosureAssessment has only:

~~~text
EXHAUSTIVE
DECISION_COMPLETE
NON_EXHAUSTIVE
NOT_EVALUABLE
~~~

EXHAUSTIVE means every source domain that a standing discovery law identifies
as capable of supplying a relevant basis was authoritatively queried at S.

DECISION_COMPLETE means a standing composition law proves that omitted bases
cannot change the disposition. It cannot be inferred from convenience, a
successful first match, or source ordering.

NON_EXHAUSTIVE means the search is known not to cover the complete relevant
domain.

NOT_EVALUABLE means coverage, source standing, epoch alignment, or the
discovery law cannot be established.

Each BasisPathAssessment carries:

~~~text
basis identity
basis kind
normative effect:
  PERMIT
  PROHIBIT
  REQUIRE
  NARROW
path disposition:
  TRUE
  FALSE
  NOT_EVALUABLE
dependency graph reference
root failures
evaluation snapshot
~~~

Query aggregation is lawful only after candidate-set closure and policy
composition resolve. The general law is:

~~~text
closed candidate basis set
+
every selected governing policy standing and applicable
+
every relevant basis path assessed
+
standing precedence/composition resolution
+
no outcome-changing unresolved basis
→ query-level disposition
~~~

For the countermodel:

~~~text
G1 = FALSE path
G2 = TRUE permit path

If a standing composition law says
any satisfied permit basis is sufficient
and G1 has no prohibitory effect:
  query = TRUE

If G1 is a standing prohibition:
  apply standing precedence/composition law

If no such law resolves the conflict:
  query = NOT_EVALUABLE

If candidate-set closure is not established:
  query = NOT_EVALUABLE
~~~

An individual FALSE path never suppresses another candidate basis. An
individual TRUE path never defeats a standing prohibition or unresolved basis
unless a standing composition law proves it irrelevant.

### WHY REPAIR CLOSES COUNTERMODEL

The two paths can no longer independently emit contradictory query results.
They emit path results into one closed candidate set. A separate composition
assessment resolves their normative effects or returns NOT_EVALUABLE. The
query result is therefore a function of the complete governed basis set, not
the first or last path encountered.

### NEW ASSUMPTIONS

- A standing discovery/query law can identify the authoritative corpora for q.
- Basis identities and aliases can be resolved across those corpora.
- A standing policy may define composition or precedence among multiple
  applicable bases.

These assumptions are requirements, not facts established by this artifact.

### NEW UNRESOLVED ROOTS

- authority over each grant or authority-record corpus;
- proof that the corpus set is exhaustive for q;
- cross-corpus identity and alias resolution;
- standing multi-basis composition law.

### REGRESSION RISK

The repaired calculus may return NOT_EVALUABLE more often than the old target.
That is intentional where basis closure is unproved. A future implementation
must not optimize by stopping at the first TRUE or FALSE path.

### STATUS

~~~text
CLOSED
~~~

This is an authoring disposition at the candidate-semantic level. It is not an
independent-review verdict.

## 5. B2 REPAIR

### FINDING

ExternallyAdoptedStandingRoots is an untyped successful terminus. Its name
asserts the very standing and external independence that the graph needs to
prove.

### COUNTERMODEL

~~~text
RootReference R contains:
  label = FOUNDER_ROOT
  status = VALID

The same record:
  claims Founder origin
  supplies its own adoption
  supplies its own independence
  supplies its own applicability

Old graph:
  incoming external record
  → successful authority termination
~~~

The record is external only relative to the suite. That does not prove
independence, adoption, provenance, currentness, or applicability.

### ROOT DEFECT

The old target has no typed boundary between:

~~~text
RootReference
RootAdmissionEvent
RootStandingRecord
RootStandingAssessment
RootIndependenceAssessment
RootApplicabilityAssessment
RootConflictResolution
~~~

It also lacks a rule that makes an unresolved root terminate fail-closed rather
than appear inside a prevalidated set.

### REPAIR

Replace ExternallyAdoptedStandingRoots with a required upstream interface:

~~~text
GOVERNANCE_ROOT_ADMISSION_AND_STANDING_INTERFACE
~~~

The interface may return a RootResolutionBundle. It may not return a bare
successful root label.

A RootResolutionBundle must identify:

- exact root identity, kind, version, and content digest;
- the root reference source and custody;
- the root-admission occurrence;
- the law or primitive trust-boundary declaration under which admission was
  performed;
- the actor and authority basis for admission, unless the law explicitly
  classifies the root as a primitive trust boundary;
- adoption standing and its provenance;
- effective interval and currentness;
- exact operations, targets, scope, and jurisdictions for which the root can
  terminate proof;
- the independence relation being claimed;
- the subjects, records, policies, or runtime controls from which independence
  is required;
- known conflicting roots and any standing precedence law;
- a RootStandingAssessment;
- a RootIndependenceAssessment;
- a RootApplicabilityAssessment;
- a RootConflictResolution.

Primitive trust-boundary declarations are not silently proven roots. They are
explicit boundary inputs whose own standing remains external to this suite.
The bundle must expose that fact:

~~~text
ROOT_BASIS_KIND:
  DERIVED_STANDING
  or
  EXPLICIT_PRIMITIVE_TRUST_BOUNDARY

EXTERNAL_STANDING_JURISDICTION:
  exact reference

SUITE_PROOF_CEILING:
  consumes result
  does not confer result
~~~

Successful root termination requires:

~~~text
RootStandingAssessment = TRUE
and RootIndependenceAssessment = TRUE
and RootApplicabilityAssessment = TRUE
and RootConflictResolution is resolved
and current at S
and exact to the required authority edge
~~~

Any missing or circular element yields:

~~~text
ROOT_RESOLUTION_UNAVAILABLE
or ROOT_STANDING_UNRESOLVED
or ROOT_INDEPENDENCE_UNRESOLVED
or ROOT_APPLICABILITY_UNRESOLVED
or ROOT_CONFLICT_UNRESOLVED

→ relied path = NOT_EVALUABLE
~~~

This artifact establishes no positive RootResolutionBundle.

### WHY REPAIR CLOSES COUNTERMODEL

The Founder-labeled record cannot occupy all root roles. Its label remains a
claim until distinct standing, independence, applicability, currentness, and
conflict assessments resolve. The suite cannot add the record to a trusted set
or use its own output to validate it. Without a lawful bundle, positive
termination is unavailable and the path returns NOT_EVALUABLE.

### NEW ASSUMPTIONS

- Some external governance jurisdiction may define root admission.
- Independence is a typed relation against named control/dependency domains,
  not a property inferred from source location.
- A primitive trust boundary, if one exists, can be named explicitly without
  pretending the suite proved it.

### NEW UNRESOLVED ROOTS

- the actual positive constitutional or governance root;
- authority for root admission;
- Founder-origin proof;
- cross-root conflict precedence;
- cross-jurisdiction root recognition;
- the exact independence adjudicator.

### REGRESSION RISK

No positive authority result may currently be reachable if no lawful root
bundle exists. That is an honest consequence, not a reason to reinstate an
oracle.

### STATUS

~~~text
CLOSED
~~~

The oracle defect is closed by typed fail-closed consumption. Positive root
standing remains unresolved.

## 6. B3 REPAIR

### FINDING

PolicyStandingAssessment both includes and excludes applicability in the old
target.

### COUNTERMODEL

~~~text
Policy P:
  lawfully adopted
  current
  not withdrawn
  jurisdiction J1

Query q:
  jurisdiction J2

If standing includes applicability:
  P standing = FALSE

If standing is distinct:
  P standing = TRUE
  P applicable to q = FALSE

The old object model permits both representations.
~~~

### ROOT DEFECT

One current assessment was assigned two questions:

1. Does the policy presently have recognized governance standing?
2. Does that standing policy govern this exact authority query?

The first is governance-relative and can exist without q. The second is
query-relative and must consume q.

### REPAIR

The repaired policy sequence is:

~~~text
PolicyRecord
→ PolicyAdoptionEvent
→ PolicyAdoptionStandingRecord
→ PolicyCurrentnessAssessment(S)
→ PolicyStandingAssessment(S)
→ PolicyApplicabilityAssessment(q, S)
→ PolicyPrecedenceResolution(q, S)
→ GoverningPolicySet(q, S)
~~~

PolicyStandingAssessment answers only:

- exact policy identity/version/content;
- whether a qualifying adoption standing record exists;
- whether adoption authority resolved;
- whether the adoption record is current;
- amendment, supersession, withdrawal, and expiry state;
- whether the standing jurisdiction recognizes the policy at S;
- provenance-cycle status.

It explicitly excludes:

- whether q falls within the policy operation or target domain;
- whether q meets role, context, or condition selectors;
- whether another applicable policy dominates or composes with it;
- whether the policy authorizes the actor.

PolicyApplicabilityAssessment consumes a standing policy and q. It answers
whether the policy's governed domain matches:

- actor or role selector;
- operation;
- target;
- scope;
- jurisdiction;
- context;
- evaluation snapshot.

PolicyPrecedenceResolution consumes every standing and applicable candidate
policy plus an independently standing precedence/composition law. It does not
change policy standing.

For the countermodel:

~~~text
PolicyStandingAssessment(P, S) = TRUE
PolicyApplicabilityAssessment(P, q@J2, S) = FALSE
~~~

No contradiction remains.

### WHY REPAIR CLOSES COUNTERMODEL

The same object can no longer mean both standing and query applicability.
Every downstream edge names which assessment it consumes. A nonapplicable
policy remains standing history and governance law in its own jurisdiction;
it simply does not enter the governing policy set for q.

### NEW ASSUMPTIONS

- The external governance interface can resolve policy adoption and
  currentness without using this query's final authority result.
- Query-specific applicability dimensions can be compared under standing
  definitions.

### NEW UNRESOLVED ROOTS

- policy adoption standing source;
- policy currentness and supersession authority;
- policy-domain comparison rules;
- precedence/composition law.

### REGRESSION RISK

A caller that previously treated PolicyStandingAssessment as a ready-to-use
governing-policy result would now be incomplete. No runtime migration is
authorized here.

### STATUS

~~~text
CLOSED
~~~

## 7. B4 REPAIR

### FINDING

The old proof DAG omits policy-adoption authority and governing-policy
selection, hiding a policy/authority recursion.

### COUNTERMODEL

~~~text
PolicyStanding(P)
  relies on AdoptionStanding(P)

AdoptionStanding(P)
  relies on AuthorityApplicability(
    actor,
    ADOPT_POLICY,
    P,
    adoption_time
  )

AuthorityApplicability(...)
  relies on PolicyStanding(P)

No predecessor policy.
No applicable independent root.
~~~

### ROOT DEFECT

The graph shows a policy standing node as if it were supplied directly by
external roots. It does not represent:

- the adoption act;
- adoption-actor attribution;
- authority to perform ADOPT_POLICY;
- the predecessor policy or root governing adoption;
- discovery of candidate policies;
- standing of the policy-selection rule;
- precedence or policy composition.

### REPAIR

The repaired graph explicitly contains two distinct policy law classes:

~~~text
governance-selection law:
  determines how candidate policies are discovered,
  compared, and composed

substantive authority policy:
  supplies requirements or constraints for q
~~~

The selection law must have standing through an earlier acyclic policy/root
path. A candidate policy may not select itself unless an independently
standing predecessor rule explicitly supplies that relationship.

Required policy-adoption path:

~~~text
PolicyRecord(P)
→ PolicyAdoptionEvent(A)
→ AdoptionActorAttribution(A)
→ AdoptionAuthorityAssessment(A, adoption_time)
→ predecessor governance policy or applicable root
→ PolicyAdoptionStandingRecord(P)
→ PolicyStandingAssessment(P, S)
~~~

Required policy-selection path:

~~~text
PolicyCandidateDiscoveryAssessment(q, S)
→ PolicyCandidateSet(q, S)
→ PolicyCandidateSetClosureAssessment(q, S)
→ standing selection/composition law
→ each PolicyStandingAssessment
→ each PolicyApplicabilityAssessment
→ PolicyPrecedenceResolution
→ GoverningPolicySet(q, S)
~~~

Required authority-basis path:

~~~text
GoverningPolicySet(q, S)
+
AuthorityBasisDiscoveryAssessment(q, S)
+
each BasisPathAssessment
→ AuthorityBasisCompositionAssessment(q, S)
→ AuthorityApplicabilityAssessment(q, S)
~~~

Every dependency edge carries:

- source node identity;
- destination node identity;
- dependency purpose;
- relevant operation and target;
- evaluation or historical time;
- policy version;
- snapshot identity;
- whether the edge is mandatory for the selected proof.

For the countermodel, the graph exposes:

~~~text
P standing
→ adoption authority for P
→ P standing
~~~

With no predecessor or independent root:

~~~text
POLICY_PROVENANCE_CYCLE
→ adoption path = NOT_EVALUABLE
→ PolicyStandingAssessment(P) = NOT_EVALUABLE
→ P cannot enter GoverningPolicySet
→ query = NOT_EVALUABLE when P is mandatory
~~~

### WHY REPAIR CLOSES COUNTERMODEL

The adoption-authority edge and policy-selection law are now first-class graph
nodes. The cycle cannot be hidden behind PolicyStandingAssessment. It is
detected before P can govern the same adoption that purportedly creates P's
standing.

### NEW ASSUMPTIONS

- Policy adoption is an authority-bearing operation unless an independently
  standing root law classifies a different adoption basis.
- Selection and precedence rules require their own standing.
- Historical adoption-time assessments remain distinct from current
  query-time assessments.

### NEW UNRESOLVED ROOTS

- predecessor policy for the first non-root policy;
- root authority for policy adoption;
- standing selection and precedence law;
- policy corpus completeness.

### REGRESSION RISK

Previously accepted policies may become NOT_EVALUABLE when their adoption
authority or selection-law lineage was implicit. That is the required
fail-closed result.

### STATUS

~~~text
CLOSED
~~~

## 8. B5 REPAIR

### FINDING

The old object inventory does not type every node used by its proof, lifecycle,
event, policy, time, and downstream boundaries.

### COUNTERMODEL

~~~text
CurrentRevocationAssessment is used to make GrantCurrentnessAssessment false,
but CurrentRevocationAssessment has no declared primary type.

The graph cannot determine whether it is:
  a historical occurrence,
  a standing record,
  a current conclusion,
  or an unverified source claim.

An untyped value can therefore cross occurrence, standing,
and applicability boundaries without a detectable cast.
~~~

### ROOT DEFECT

The old table is illustrative rather than closed over the proof graph. It also
uses StandingRecord as a label without stating what qualifies a record to
occupy that type.

### REPAIR

Section 12 supplies a closed inventory for every object used in the repaired
B1–B7 graph. Its rules are:

1. Every node has exactly one primary semantic type.
2. A record does not become standing because it is referenced by a current
   assessment.
3. A current assessment does not rewrite the historical object it assesses.
4. A derived set or graph contains references; it does not confer standing on
   them.
5. A resolved binding establishes identity correspondence only under its
   referenced standing rules.
6. Every cast between types is explicit and justified by a named standing
   rule.

StandingRecord is repaired to mean:

~~~text
an exact record whose recognized normative or institutional standing
was conferred by a distinct admitted occurrence under an independently
standing rule, with provenance, effective interval, jurisdiction,
currentness hooks, and no unresolved relied-upon conferment cycle
~~~

The following formerly omitted objects are explicitly typed:

~~~text
IssuerAuthorityAssessment
DelegationChainAssessment
CurrentRevocationAssessment
PolicyApplicabilityAssessment
TimeFreshnessAssessment
CurrentSourceReliance
ActIdentityDisposition
ActAdmissionAttempt
~~~

Additional nodes required by B1–B7 are also typed, including candidate sets,
closure assessments, root assessments, policy precedence, snapshot identity,
negative proof, and graph results.

### WHY REPAIR CLOSES COUNTERMODEL

CurrentRevocationAssessment is now a CURRENT_ASSESSMENT. It must point to a
RevocationStandingRecord, which is a STANDING_RECORD, and that record must
point to a RevocationEvent, which is a HISTORICAL_EVENT. Source bytes remain a
SOURCE_RECORD. The graph cannot lawfully use one as another without an
explicit invalid cast.

### NEW ASSUMPTIONS

- The enumerated primary types are sufficient for the B1–B7 semantic graph.
- External interfaces preserve the same type boundaries when supplying
  references.

### NEW UNRESOLVED ROOTS

- standing-conferral laws for each record domain;
- canonical cross-domain type registry;
- external interface conformance.

### REGRESSION RISK

Objects previously passed as generic GrantRecord, PolicyRecord, RootRecord, or
event may no longer satisfy a typed input. No schema or runtime migration is
selected in this pass.

### STATUS

~~~text
CLOSED
~~~

## 9. B6 REPAIR

### FINDING

The claimed seven authority-owned contracts plus five upstream interfaces are
neither proven minimal nor complete.

### COUNTERMODEL

~~~text
Actor attribution is implemented inside the authority suite.
The same event is attributed differently by another governance service.

Generic condition predicate evaluation is also implemented inside authority.
The authority suite can then select evidence semantics that make its own
condition pass.

Meanwhile:
  root admission,
  policy selection,
  basis-set closure,
  and time reconciliation
have no owned interface.
~~~

### ROOT DEFECT

Packaging count was treated as architectural truth before every semantic
surface and owner was known. Generic identity/event and predicate functions
were incorrectly authority-owned, while governance and completeness
dependencies were absent.

### REPAIR

The repair withdraws every minimum-count claim.

~~~text
PackagingCount != SemanticTruth
REPAIRED_DECOMPOSITION_MINIMALITY = NOT_CLAIMED
~~~

Section 11 defines semantic responsibilities before packaging. It routes:

- actor attribution upstream to event/identity semantics;
- role possession and activation facts upstream;
- generic predicate evaluation upstream;
- root admission and standing upstream to governance;
- policy adoption standing and precedence-law standing upstream to
  governance;
- time-source reconciliation and snapshot identity upstream;
- operation and target identity upstream;
- authority-record corpus access upstream.

It keeps authority-owned:

- query-specific basis discovery and closure reasoning;
- grant issuance/delegation/revocation/currentness resolution;
- role requirement and role-reliance effect for a selected authority basis;
- query-specific policy applicability and composition consumption;
- scope and jurisdiction boundary effects;
- final authority-basis composition and applicability assessment.

The repaired surfaces can later be packaged together or separately only if
their input/output and authority boundaries remain intact.

### WHY REPAIR CLOSES COUNTERMODEL

Actor attribution and generic predicates can no longer be selected by the
authority result they help establish. Missing root, policy, basis-completeness,
and time surfaces become explicit inputs. The model no longer asserts that a
document count is minimal.

### NEW ASSUMPTIONS

- Upstream identity/event, governance, time, predicate, and registry services
  can expose typed outputs.
- Authority-specific interpretation can consume but not mutate those outputs.

### NEW UNRESOLVED ROOTS

- ownership and standing of each upstream service;
- whether some semantic surfaces should share implementation;
- cross-service snapshot coordination;
- interface adoption.

### REGRESSION RISK

The repaired decomposition is more explicit and may require more interfaces
than a future implementation wants. Co-packaging is permitted; semantic
collapse is not.

### STATUS

~~~text
CLOSED
~~~

## 10. B7 REPAIR

### FINDING

The old failure table maps path failures directly to query-level FALSE or
NOT_EVALUABLE and treats missing observations as if they had one universal
meaning.

### COUNTERMODEL

~~~text
Search S1 is incomplete and finds no grant.
Search S2 is governed, authoritative, exhaustive, current,
and proves no grant exists for q.

Old mapping:
  GRANT_NOT_FOUND → NOT_EVALUABLE

Result:
  S1 and S2 collapse,
  even though S2 positively establishes a negative proposition.
~~~

Another countermodel:

~~~text
G1 path is expired → FALSE
G2 path is unresolved → NOT_EVALUABLE

Old target may emit query FALSE from G1
without proving G2 irrelevant.
~~~

### ROOT DEFECT

The target does not distinguish:

- observation-level absence;
- authoritative exhaustive negative proof;
- path-level disposition;
- query-level aggregation;
- a stale object proven stale;
- currentness that is merely unavailable.

### REPAIR

General negative-proof law:

~~~text
AbsenceObservation
!= ExhaustiveNegativeProof

MissingEvidence
!= ProvenNegativeProposition

PathDisposition
!= QueryDisposition
~~~

An ExhaustiveNegativeProof must bind:

- the exact negative proposition;
- q and S;
- the authoritative source domain;
- the standing law making that source authoritative for the proposition;
- the query used;
- source revision or epoch;
- coverage and completeness proof;
- result provenance;
- freshness;
- unresolved source domains;
- whether any admissible alternate source can change the conclusion.

Only a valid current ExhaustiveNegativeProof may establish a negative
proposition such as:

~~~text
no applicable grant exists
no standing revocation exists in the authoritative revocation domain
no applicable policy exists in the closed policy domain
no required role possession exists in the authoritative role domain
~~~

The law is not limited to grants. Its applicability depends on a standing
domain law that makes exhaustive negative proof possible for that proposition.
Open-world domains without such a law remain NOT_EVALUABLE.

Path-level rules:

~~~text
proven mismatch or invalidity on one path
→ that path = FALSE

unresolved mandatory dependency on one path
→ that path = NOT_EVALUABLE
~~~

Query-level rules:

~~~text
closed basis set
and every sufficient basis is positively FALSE
and no outcome-changing unresolved basis remains
→ query = FALSE

valid ExhaustiveNegativeProof(no applicable basis)
→ query = FALSE

at least one sufficient TRUE basis
and candidate-set closure is established
and all applicable prohibitions/constraints are resolved
and standing composition law yields permit
→ query = TRUE

mandatory discovery, standing, identity, time, comparison,
precedence, policy selection, or basis path unresolved
and it can change the result
→ query = NOT_EVALUABLE

conflicting TRUE effects without standing precedence/composition
→ query = NOT_EVALUABLE
~~~

Policy stale is split:

~~~text
POLICY_SUPERSEDED_PROVEN
  → that policy path = FALSE for current reliance

POLICY_CURRENTNESS_UNAVAILABLE
  → that policy path = NOT_EVALUABLE

POLICY_NOT_APPLICABLE_PROVEN
  → that policy is excluded from q
  → query disposition still depends on governing-policy-set closure
~~~

Grant not found is split:

~~~text
NO_GRANT_OBSERVED_IN_NON_EXHAUSTIVE_SEARCH
  → NOT_EVALUABLE

NO_APPLICABLE_GRANT_ESTABLISHED_BY_EXHAUSTIVE_NEGATIVE_PROOF
  → FALSE
~~~

Every disposition carries RootFailure entries scoped to:

~~~text
object
path
candidate set
or whole query
~~~

### WHY REPAIR CLOSES COUNTERMODEL

S1 remains NOT_EVALUABLE because it has no completeness proof. S2 can produce
query FALSE because its negative proposition is positively established under
a standing domain law. G1's expired path cannot make the entire query false
while G2 can still alter the result.

### NEW ASSUMPTIONS

- Some domains may lawfully support authoritative exhaustive queries.
- Completeness and freshness are themselves assessable.
- Root-failure scope is preserved through aggregation.

### NEW UNRESOLVED ROOTS

- authority of negative-proof sources;
- domain closure laws;
- cross-registry completeness;
- precedence when evidence sources conflict.

### REGRESSION RISK

Systems that equate empty query results with negative reality will now fail
closed. Systems that treat any single invalid path as global denial must adopt
query-level aggregation.

### STATUS

~~~text
CLOSED
~~~

## 11. REPAIRED DECOMPOSITION

The decomposition is responsibility-first. No count is asserted as minimal.

### Required upstream semantic interfaces

| Interface | Supplies | Must not supply |
|---|---|---|
| EVENT_IDENTITY_AND_SOURCE_ADMISSION_INTERFACE | admitted occurrence identity, event species, source provenance, current source reliance | authority or policy standing |
| PRINCIPAL_AND_ACTOR_ATTRIBUTION_INTERFACE | current principal binding and event-specific actor attribution | an authority grant |
| ROLE_FACT_INTERFACE | role-possession standing records and activation occurrences | authority applicability |
| GOVERNED_OPERATION_IDENTITY_INTERFACE | exact operation binding and semantic version | permission to perform the operation |
| GOVERNED_TARGET_IDENTITY_INTERFACE | exact target binding, revision, custody identity | permission over the target |
| TIME_RECONCILIATION_AND_SNAPSHOT_INTERFACE | evaluation time evidence, source reconciliation, freshness, snapshot identity | policy standing or authority |
| GENERIC_PREDICATE_EVALUATION_INTERFACE | evaluation of exact predicates against bound evidence | selection of which predicates have standing |
| GOVERNANCE_ROOT_ADMISSION_AND_STANDING_INTERFACE | typed root resolution bundles | self-declared root success |
| GOVERNED_POLICY_CORPUS_INTERFACE | policy records, adoption standing, currentness, selection-law standing, precedence-law standing, corpus coverage | query authority result |
| GOVERNED_AUTHORITY_RECORD_CORPUS_INTERFACE | grant, delegation, revocation, and other basis records plus authoritative query coverage | automatic basis applicability |

An implementation may combine upstream services. Combination does not erase
their semantic ownership or allow outputs to bootstrap their own standing.

### Authority-owned semantic surfaces

| Surface | Owns | Consumes |
|---|---|---|
| AUTHORITY_BASIS_DISCOVERY_AND_CLOSURE | relevant basis discovery, candidate-set identity, closure reasoning | governed authority corpora, q, S, policy selection |
| AUTHORITY_GRANT_LIFECYCLE_RESOLUTION | grant issuance authority, delegation, revocation, intrinsic currentness | typed records, historical assessments, policy, snapshot |
| AUTHORITY_ROLE_REQUIREMENT_AND_RELIANCE | whether a selected standing basis requires a role and whether upstream role facts satisfy it | role facts, selected basis, governing policy |
| AUTHORITY_POLICY_APPLICABILITY_AND_COMPOSITION | query-specific applicability of standing policies and their resolved composition | policy corpus outputs, q, S |
| AUTHORITY_BOUNDARY_RESOLUTION | scope and jurisdiction results as distinct typed outputs | basis envelopes, operation, target, context, policy |
| AUTHORITY_APPLICABILITY_AGGREGATION | path assessments, closure, policy composition, final TRUE/FALSE/NOT_EVALUABLE | every mandatory resolved input |

### Ownership laws

~~~text
ActorAttribution:
  upstream event and identity semantics

ActorAttributionBinding:
  consumed by authority
  not authored by authority

RolePossession and RoleActivation:
  upstream facts

RoleRequiredForBasis and RoleRelianceEffect:
  authority-owned query semantics

PredicateTruth:
  upstream generic evaluation

PredicateNormativeEffect:
  authority-owned only after its definition has standing

PolicyStanding:
  upstream governance

PolicyApplicabilityToAuthorityQuery:
  authority-owned composition input

RootStanding:
  upstream governance

AuthorityApplicabilityAssessment:
  authority-owned composition result
~~~

Scope and jurisdiction may share implementation plumbing, but they retain
different comparison algebras and separate assessment objects. If either
dimension is not comparable under a standing rule, that branch remains
NOT_EVALUABLE.

Grant issuance, delegation, revocation, and currentness may share lifecycle
packaging only while their distinct objects, historical times, authorities,
and current assessments remain explicit.

## 12. REPAIRED OBJECT/TYPE MODEL

Primary semantic types used here:

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

The slash spelling POLICY/RULE_RECORD in the source target is normalized here
to POLICY_OR_RULE_RECORD only as candidate notation. It carries no canonical
effect.

| Object | Primary semantic type | Exact role |
|---|---|---|
| AuthorityClaimRepresentation | SOURCE_RECORD | Claim-bearing source bytes |
| SourceAdmissionEnvelope | SOURCE_RECORD | Source-admission input bundle |
| RawOccurrenceEvent | HISTORICAL_EVENT | Admitted raw occurrence |
| AdmittedRequestAct | HISTORICAL_EVENT | Request occurrence bound to q |
| AuthorizationActCandidate | SOURCE_RECORD | Candidate interpretation of occurrence |
| ActIdentityDisposition | CURRENT_ASSESSMENT | Current species/identity disposition |
| ActAdmissionAttempt | HISTORICAL_EVENT | Admission attempt occurrence |
| AdmittedAuthorizationActIdentity | RESOLVED_BINDING | Exact admitted act identity |
| AuthorizationAct | HISTORICAL_EVENT | Admitted authorization occurrence |
| CurrentSourceReliance | CURRENT_ASSESSMENT | Current usability of admitted source |
| CredentialControlEvidence | EVIDENCE_REFERENCE | Credential-control support |
| PrincipalIdentitySourceRecord | SOURCE_RECORD | External identity source |
| CredentialPrincipalBindingRecord | STANDING_RECORD | Recognized credential-principal mapping |
| PrincipalBindingAssessment | CURRENT_ASSESSMENT | Current credential-to-principal resolution |
| ActorAttributionBinding | RESOLVED_BINDING | Event-specific actor identity binding |
| CurrentActorAttributionReliance | CURRENT_ASSESSMENT | Current reliance after corrections/conflicts |
| RolePossessionRecord | STANDING_RECORD | Recognized role possession |
| RoleActivationEvent | HISTORICAL_EVENT | Role activation occurrence |
| RoleApplicabilityAssessment | CURRENT_ASSESSMENT | Role relevance and satisfaction for q |
| RoleRequirementResolution | CURRENT_ASSESSMENT | Whether selected basis requires role evidence |
| GrantRepresentation | SOURCE_RECORD | Grant-shaped bytes or claims |
| GrantIssuanceEvent | HISTORICAL_EVENT | Issuance occurrence |
| GrantStandingRecord | STANDING_RECORD | Recognized grant under issuance law |
| IssuerAuthorityAssessment | CURRENT_ASSESSMENT | Issuer authority at exact issuance time |
| DelegationStandingRecord | STANDING_RECORD | Recognized bounded child grant |
| DelegationChainAssessment | CURRENT_ASSESSMENT | Current parent-child chain validity |
| DelegationDimensionComparison | DERIVED_VALUE | Typed comparison outcome per dimension |
| RevocationRepresentation | SOURCE_RECORD | Revocation-shaped bytes or claims |
| RevocationEvent | HISTORICAL_EVENT | Revocation occurrence |
| RevocationStandingRecord | STANDING_RECORD | Recognized revocation |
| CurrentRevocationAssessment | CURRENT_ASSESSMENT | Current revocation effect at S |
| PartialRevocationEnvelope | DERIVED_VALUE | Exact comparable portion removed |
| GrantIntrinsicUseConstraint | POLICY_OR_RULE_RECORD | Grant-level finite-use semantics |
| GrantUseStateRecord | STANDING_RECORD | Recognized grant-use state under its law |
| GrantUseStateAssessment | CURRENT_ASSESSMENT | Whether intrinsic grant use remains |
| GrantCurrentnessAssessment | CURRENT_ASSESSMENT | Expiry, revocation, delegation, intrinsic-use result |
| OperationDefinition | POLICY_OR_RULE_RECORD | Governed operation semantics |
| OperationBinding | RESOLVED_BINDING | Exact q operation identity |
| TargetIdentitySourceRecord | SOURCE_RECORD | External target identity/custody source |
| TargetBinding | RESOLVED_BINDING | Exact q target identity/revision |
| ScopeRule | POLICY_OR_RULE_RECORD | Scope dimension and comparison semantics |
| ScopeApplicabilityAssessment | CURRENT_ASSESSMENT | Basis envelope versus q |
| EffectiveScopeValue | DERIVED_VALUE | Scope value after lawful intersections/subtractions |
| JurisdictionRule | POLICY_OR_RULE_RECORD | Jurisdiction semantics |
| JurisdictionAssessment | CURRENT_ASSESSMENT | Jurisdiction result for q |
| ConditionDefinition | POLICY_OR_RULE_RECORD | Exact predicate inherited from standing basis |
| ConditionStandingBasis | STANDING_RECORD | Recognition of the predicate as normative |
| ConditionEvidence | EVIDENCE_REFERENCE | Predicate evidence |
| PredicateEvaluation | CURRENT_ASSESSMENT | Generic predicate truth result |
| ConditionRelianceAssessment | CURRENT_ASSESSMENT | Authority-specific effect of predicate result |
| PolicyRecord | POLICY_OR_RULE_RECORD | Exact policy identity/version/content |
| PolicyAdoptionEvent | HISTORICAL_EVENT | Adoption, amendment, or withdrawal occurrence |
| PolicyAdoptionStandingRecord | STANDING_RECORD | Recognized policy adoption |
| AdoptionAuthorityAssessment | CURRENT_ASSESSMENT | Actor authority for ADOPT_POLICY at adoption time |
| PolicyCurrentnessAssessment | CURRENT_ASSESSMENT | Amendment, supersession, withdrawal, expiry |
| PolicyStandingAssessment | CURRENT_ASSESSMENT | Governance standing, excluding q applicability |
| PolicyApplicabilityAssessment | CURRENT_ASSESSMENT | Standing policy applicability to q |
| PolicyCandidateSet | DERIVED_VALUE | Candidate policy references for q |
| PolicyCandidateSetClosureAssessment | CURRENT_ASSESSMENT | Policy corpus coverage |
| PolicyPrecedenceRule | POLICY_OR_RULE_RECORD | Standing comparison/composition rule |
| PolicyPrecedenceResolution | CURRENT_ASSESSMENT | Query-specific ordering/composition result |
| GoverningPolicySet | DERIVED_VALUE | Resolved policy set for q |
| RootReference | EVIDENCE_REFERENCE | Exact reference to proposed root |
| RootAdmissionEvent | HISTORICAL_EVENT | Root-admission occurrence |
| RootStandingRecord | STANDING_RECORD | Externally recognized root record |
| RootStandingAssessment | CURRENT_ASSESSMENT | Current root standing |
| RootIndependenceAssessment | CURRENT_ASSESSMENT | Independence against named dependency/control set |
| RootApplicabilityAssessment | CURRENT_ASSESSMENT | Root applicability to exact required edge |
| RootConflictResolution | CURRENT_ASSESSMENT | Conflict and precedence outcome |
| RootResolutionBundle | DERIVED_VALUE | References to all resolved root objects |
| EvaluationTimeEvidence | EVIDENCE_REFERENCE | Governed temporal observation |
| TimeSourceStandingRecord | STANDING_RECORD | Recognition of a time source |
| TimeFreshnessAssessment | CURRENT_ASSESSMENT | Freshness and tolerance at S |
| TimeSourceReconciliationAssessment | CURRENT_ASSESSMENT | Resolution among multiple time sources |
| EvaluationSnapshotIdentity | RESOLVED_BINDING | Exact identity of the assessment epoch |
| AuthorityRecordQueryLaw | POLICY_OR_RULE_RECORD | Defines searchable authority corpus/domain |
| AuthorityBasisDiscoveryAssessment | CURRENT_ASSESSMENT | Discovery result for q at S |
| AuthorityBasisCandidateSet | DERIVED_VALUE | Exact relevant basis references |
| BasisSetClosureAssessment | CURRENT_ASSESSMENT | Exhaustive or decision-complete coverage result |
| AuthorityBasisCandidate | DERIVED_VALUE | One typed candidate basis reference |
| BasisPathAssessment | CURRENT_ASSESSMENT | TRUE/FALSE/NOT_EVALUABLE for one path |
| AuthorityBasisCompositionRule | POLICY_OR_RULE_RECORD | Standing multi-basis composition law |
| AuthorityBasisCompositionAssessment | CURRENT_ASSESSMENT | Resolved effects over candidate set |
| ExhaustiveNegativeProof | EVIDENCE_REFERENCE | Positive evidence for exact negative proposition |
| AuthorityDependencyEdge | DERIVED_VALUE | Typed reliance edge |
| AuthorityDependencyGraph | DERIVED_VALUE | Complete selected and candidate proof graph |
| ProvenanceCycleAssessment | CURRENT_ASSESSMENT | Cycle relevance and acyclic path result |
| AuthorityApplicabilityAssessment | CURRENT_ASSESSMENT | Final q disposition |
| RootFailure | DERIVED_VALUE | Scoped cause attached to an assessment |
| AuthorizationActConsumptionEvent | HISTORICAL_EVENT | Particular reliance-consumption occurrence |
| AuthorizationActConsumptionRecord | STANDING_RECORD | Recognized consumption under downstream law |
| CurrentAuthorizationReliance | CURRENT_ASSESSMENT | Whether a particular act remains usable |
| MutationEligibilityDecision | CURRENT_ASSESSMENT | Downstream consequence decision |
| MutationOccurrence | HISTORICAL_EVENT | Actual mutation occurrence |

### Type invariants

~~~text
SOURCE_RECORD
↛ HISTORICAL_EVENT

HISTORICAL_EVENT
↛ STANDING_RECORD

STANDING_RECORD
↛ CURRENT_ASSESSMENT

CURRENT_ASSESSMENT(t1)
↛ CURRENT_ASSESSMENT(t2)

DERIVED_VALUE
↛ STANDING_RECORD

RESOLVED_BINDING
↛ AuthorityApplicability
~~~

StandingRecord is not an oracle. Its qualification requires a separate
standing-conferral occurrence, independently standing rule, exact provenance,
effective interval, jurisdiction, currentness hooks, and an acyclic relied
conferment path or explicit external primitive trust-boundary declaration.

The inventory is complete for every node named by the repaired B1–B7 graph. It
does not claim to be a canonical universal ontology.

## 13. REPAIRED PROOF DAG

The graph is not a linear pipeline. The following layout shows dependency
classes; arrows mean the positive resolution of the left node relies on the
right node.

~~~text
AuthorityApplicabilityAssessment(q, S)
|
+-- AuthorityBasisCompositionAssessment(q, S)
|   |
|   +-- AuthorityBasisCandidateSet(q, S)
|   |   |
|   |   +-- AuthorityBasisDiscoveryAssessment(q, S)
|   |       |
|   |       +-- governed authority corpora
|   |       +-- AuthorityRecordQueryLaw standing
|   |       +-- actor, operation, target bindings
|   |       +-- GoverningPolicySet(q, S)
|   |       +-- EvaluationSnapshotIdentity
|   |
|   +-- BasisSetClosureAssessment(q, S)
|   +-- each BasisPathAssessment(b, q, S)
|   +-- AuthorityBasisCompositionRule standing
|   +-- no outcome-changing unresolved basis
|
+-- GoverningPolicySet(q, S)
|   |
|   +-- PolicyCandidateDiscoveryAssessment
|   +-- PolicyCandidateSetClosureAssessment
|   +-- each PolicyStandingAssessment(P, S)
|   |   |
|   |   +-- PolicyAdoptionStandingRecord(P)
|   |   |   |
|   |   |   +-- PolicyAdoptionEvent(P)
|   |   |   +-- AdoptionActorAttribution
|   |   |   +-- AdoptionAuthorityAssessment@adoption
|   |   |       |
|   |   |       +-- predecessor policy
|   |   |       or applicable RootResolutionBundle
|   |   |
|   |   +-- PolicyCurrentnessAssessment(P, S)
|   |
|   +-- each PolicyApplicabilityAssessment(P, q, S)
|   +-- PolicyPrecedenceResolution(q, S)
|       |
|       +-- independently standing selection/composition law
|
+-- exact q bindings
|   |
|   +-- admitted request act
|   +-- PrincipalBindingAssessment
|   +-- CurrentActorAttributionReliance
|   +-- OperationBinding
|   +-- TargetBinding
|   +-- context binding
|
+-- EvaluationSnapshotIdentity
    |
    +-- EvaluationTimeEvidence
    +-- TimeSourceStandingRecord
    +-- TimeFreshnessAssessment
    +-- TimeSourceReconciliationAssessment
    +-- source/corpus epochs
~~~

Each grant basis path expands:

~~~text
BasisPathAssessment(grant G, q, S)
|
+-- GrantStandingRecord(G)
|   |
|   +-- GrantIssuanceEvent(G)
|   +-- issuer ActorAttributionBinding
|   +-- IssuerAuthorityAssessment@issuance
|   |   |
|   |   +-- complete authority subquery:
|   |       operation = ISSUE_GRANT
|   |       target = exact grant payload and subject
|   |       snapshot = issuance-time snapshot
|   |
|   +-- governing issuance policy at issuance
|
+-- DelegationChainAssessment(G, S)
+-- CurrentRevocationAssessment(G, S)
+-- GrantUseStateAssessment(G, S), only when intrinsic use-limited
+-- GrantCurrentnessAssessment(G, S)
+-- RoleRequirementResolution(G, q, S)
+-- RoleApplicabilityAssessment(q, S), when required
+-- ScopeApplicabilityAssessment(G, q, S)
+-- JurisdictionAssessment(G, q, S)
+-- ConditionRelianceAssessment(G, q, S)
+-- ProvenanceCycleAssessment(path)
~~~

Each root termination expands:

~~~text
RootResolutionBundle(R, required_edge, S)
|
+-- RootReference(R)
+-- RootAdmissionEvent(R)
+-- RootStandingRecord(R)
+-- RootStandingAssessment(R, S)
+-- RootIndependenceAssessment(R, named dependency set, S)
+-- RootApplicabilityAssessment(R, required_edge, S)
+-- RootConflictResolution(R, S)
~~~

### Graph completeness law

The proof DAG is evaluable only when:

- every object used by a selected path is typed;
- every mandatory dependency edge is represented;
- every candidate basis capable of changing the result is either evaluated or
  excluded by a standing closure law;
- every policy selection and precedence rule has its own standing path;
- historical assessments use their historical snapshot;
- current assessments use the current exact snapshot;
- no unresolved mandatory branch is ignored.

### Cycle law

~~~text
CycleInUnusedCandidatePath
and selected acyclic sufficient path exists
and standing composition law proves unused path irrelevant
→ unused cycle does not poison query

CycleInMandatoryOrOutcomeChangingPath
and no acyclic independently rooted alternative resolves
→ relevant path = NOT_EVALUABLE

Policy selects itself
or policy authorizes its own adoption
without predecessor/root
→ POLICY_PROVENANCE_CYCLE

Grant A authorizes Grant B
and Grant B authorizes Grant A
without independent applicable root
→ AUTHORITY_PROVENANCE_CYCLE
~~~

The graph never uses mutation eligibility, capability, safety, or execution
success to prove an upstream authority node.

## 14. ROOT TERMINATION MODEL

A root is a typed proof boundary, not a magic first node.

### Root admission requirements

The upstream governance interface must return:

~~~text
RootResolutionBundle {
  root_reference
  root_identity
  root_kind
  content_digest
  source_jurisdiction
  admission_event
  standing_record
  standing_assessment
  independence_assessment
  applicability_assessment
  conflict_resolution
  effective_interval
  evaluation_snapshot
  primitive_boundary_disclosure, if applicable
}
~~~

### Independence semantics

Independence is relational:

~~~text
Independent(
  root R,
  from dependency component C,
  from controlling subjects K,
  for required authority edge E,
  at snapshot S
)
~~~

It is not inferred from:

~~~text
different file
different repository
different runtime
different actor label
external transport
Founder label
recorded status
identity inequality
~~~

The independence assessment must show that R's standing and applicability do
not depend on the unresolved component it is terminating.

### Applicability semantics

RootStandingAssessment TRUE does not imply RootApplicabilityAssessment TRUE.
The latter binds exact operation, target, jurisdiction, scope, time, and
authority class.

### Conflict semantics

Multiple roots may coexist. If two applicable roots disagree:

~~~text
standing precedence/composition law resolves conflict
→ apply that result

no standing precedence/composition law
→ ROOT_CONFLICT_UNRESOLVED
→ affected path = NOT_EVALUABLE
~~~

### Current state

This artifact supplies no positive root bundle. Therefore any real query whose
positive path requires a root not established elsewhere remains
NOT_EVALUABLE.

~~~text
External != Independent
Recorded != Standing
RootReference != RootStanding
RootStanding != RootApplicability
FounderLabeled != FounderOriginProven
CandidateSuite != PolicyRoot
~~~

## 15. POLICY SELECTION / STANDING / APPLICABILITY MODEL

### Policy candidate discovery

PolicyCandidateDiscoveryAssessment binds q and S to every policy corpus that a
standing governance-selection law identifies. It returns PolicyCandidateSet
and PolicyCandidateSetClosureAssessment.

An empty candidate set means nothing without closure.

### Policy standing

PolicyStandingAssessment is true only when:

- exact policy identity/version/content resolves;
- adoption standing resolves;
- adoption authority resolves at adoption time;
- amendment and supersession lineage resolves;
- withdrawal and expiry do not defeat current standing;
- the recognizing governance jurisdiction is exact;
- no relied policy-standing cycle remains.

Policy standing is independent of whether the policy applies to q.

### Policy applicability

PolicyApplicabilityAssessment consumes a standing policy, q, and S. It compares
the policy's domain to exact query bindings.

Outcomes:

~~~text
APPLICABLE
NOT_APPLICABLE
NOT_EVALUABLE
~~~

NOT_APPLICABLE is a positive query-relative mismatch. It does not make the
policy nonstanding.

### Policy precedence and composition

PolicyPrecedenceResolution consumes all standing, applicable candidates and an
independently standing precedence/composition law.

Possible results:

~~~text
SINGLE_GOVERNING_POLICY
ORDERED_POLICY_SET
COMPOSED_POLICY_SET
CONFLICT_RESOLVED_BY_STANDING_RULE
CONFLICT_UNRESOLVED
PRECEDENCE_NOT_EVALUABLE
~~~

No default is selected for:

- newest policy wins;
- most specific policy wins;
- prohibition wins;
- root policy wins;
- local policy wins;
- Founder-labeled policy wins.

Each requires standing law.

### Anti-cycle law

~~~text
PolicySelectionLaw L
must have standing without relying exclusively on
the policy set L selects.

Policy P adoption authority
must terminate through predecessor policy or applicable root
without relying on P itself.
~~~

The hidden cycle:

~~~text
PolicySelection
→ PolicyStanding
→ AuthorityApplicability
→ PolicySelection
~~~

returns NOT_EVALUABLE unless a finite acyclic predecessor/root path breaks it.

### Role-not-required constraint

ROLE_NOT_REQUIRED_BY_GOVERNING_GRANT is valid only when:

- the exact grant basis is standing;
- the policy governing that basis is selected;
- the selected basis or governing policy explicitly states role neutrality;
- policy composition does not introduce another role requirement;
- basis and policy sets are closed or decision-complete.

Missing role evidence never produces role-not-required.

## 16. AUTHORITY BASIS DISCOVERY + AGGREGATION MODEL

### Candidate basis kinds

Candidate bases may include:

- direct grants;
- delegated grants;
- standing role-derived authority, if separately defined;
- standing institutional authority records;
- applicable root authority edges;
- standing prohibitions or constraints that alter a permit result.

The list is extensible only through a standing authority-record query law. A
source representation alone is not a candidate standing basis.

### Discovery

For each q:

1. Resolve q and S.
2. Resolve the standing policy-selection law.
3. Identify every authoritative basis corpus named by standing discovery law.
4. Query each corpus using exact actor, operation, target, context, and time
   semantics.
5. Resolve aliases and duplicates without collapsing distinct events or
   records.
6. Record unresolved corpora and epoch mismatch.
7. Produce the candidate set and closure assessment.

### Basis path evaluation

Every basis is evaluated independently before composition:

~~~text
BasisPathAssessment {
  basis_id
  normative_effect
  disposition
  exact_dependencies
  selected_policy_set
  snapshot
  root_failures
}
~~~

FALSE means that exact path is positively defeated. NOT_EVALUABLE means its
outcome cannot be established. TRUE means its own mandatory requirements are
positively satisfied; it does not yet mean the whole query is true.

### Aggregation

The aggregation order is semantic:

1. Require candidate-set closure or decision completeness.
2. Require governing-policy-set resolution.
3. Evaluate all outcome-changing basis paths.
4. Apply only a standing composition rule.
5. Preserve every scoped root failure.
6. Emit one query-level disposition.

### Decision table

| Candidate set | Basis path state | Composition state | Query disposition |
|---|---|---|---|
| Non-exhaustive or not evaluable | Any | Any | NOT_EVALUABLE unless standing decision-completeness proof excludes unknowns |
| Closed and empty with valid exhaustive negative proof | None | Resolved | FALSE |
| Closed | Every sufficient basis FALSE | Resolved | FALSE |
| Closed | At least one TRUE permit; all conflicts/constraints resolved | Resolves permit | TRUE |
| Closed | TRUE permit and TRUE prohibition | No precedence/composition | NOT_EVALUABLE |
| Closed | Any outcome-changing path NOT_EVALUABLE | Cannot prove irrelevance | NOT_EVALUABLE |
| Closed | Multiple TRUE permits | Standing union/choice rule resolves | Result of that rule |
| Closed | Multiple TRUE permits | No composition rule but effects identical and equivalence proven | TRUE only if standing law permits equivalence collapse |

### Direct plus delegated basis

A direct and delegated grant are distinct basis paths. A valid direct basis
does not repair a broken delegation path; a broken delegation path does not
defeat a valid direct basis unless a standing prohibition/composition law gives
it that effect.

### Conflicting roots

Root disagreement is not resolved by basis order. It enters the composition
assessment as ROOT_CONFLICT_UNRESOLVED and makes the affected query
NOT_EVALUABLE absent standing precedence.

## 17. FALSE / NOT_EVALUABLE ALGEBRA

### Semantic levels

~~~text
FACT_OR_EVIDENCE_RESULT
PATH_DISPOSITION
POLICY_SET_DISPOSITION
BASIS_SET_DISPOSITION
QUERY_DISPOSITION
DOWNSTREAM_ELIGIBILITY_RESULT
~~~

No level silently substitutes for another.

### General three-valued rule

For a proposition p:

~~~text
TRUE:
  p is positively established under standing evidence and comparison law

FALSE:
  not-p is positively established under standing evidence and comparison law

NOT_EVALUABLE:
  neither p nor not-p can presently be established,
  or mandatory inputs conflict without standing resolution
~~~

Unknown is not false. Failure to find is not proof of absence.

### Exhaustive negative proof

~~~text
AbsenceObservation(p, source_subset)
→ NOT_EVALUABLE for not-p

ExhaustiveNegativeProof(
  not-p,
  authoritative_domain,
  standing_query_law,
  complete_coverage,
  current_snapshot
)
→ not-p may be TRUE
→ p may therefore be FALSE
~~~

The proof must itself be current and noncircular.

### Repaired root-failure mapping

| Root failure | Local disposition | Query effect |
|---|---|---|
| PRINCIPAL_UNRESOLVED | Required path NOT_EVALUABLE | Query NOT_EVALUABLE |
| ACTOR_ATTRIBUTION_UNRESOLVED | Required path NOT_EVALUABLE | Query NOT_EVALUABLE |
| ROLE_MISMATCH_PROVEN | A role-required path FALSE | Aggregate across other bases |
| ROLE_STATUS_UNAVAILABLE | A role-required path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| NO_GRANT_OBSERVED_NON_EXHAUSTIVELY | Discovery NOT_EVALUABLE | Query NOT_EVALUABLE |
| NO_APPLICABLE_GRANT_EXHAUSTIVELY_PROVEN | Closed set empty | Query FALSE |
| GRANT_INVALIDLY_ISSUED | Exact grant path FALSE | Aggregate across other bases |
| GRANT_EXPIRED_PROVEN | Exact grant path FALSE | Aggregate across other bases |
| GRANT_CURRENTNESS_UNAVAILABLE | Exact grant path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| GRANT_REVOKED_PROVEN | Exact grant path FALSE | Aggregate across other bases |
| REVOCATION_STATUS_UNAVAILABLE | Exact grant path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| DELEGATION_WIDER_OR_DISJOINT_PROVEN | Exact child path FALSE | Aggregate across other bases |
| DELEGATION_COMPARISON_UNRESOLVED | Exact child path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| OPERATION_UNRESOLVED | Required binding NOT_EVALUABLE | Query NOT_EVALUABLE |
| TARGET_UNRESOLVED | Required binding NOT_EVALUABLE | Query NOT_EVALUABLE |
| SCOPE_MISMATCH_PROVEN | Exact basis path FALSE | Aggregate across other bases |
| SCOPE_COMPARISON_UNRESOLVED | Exact basis path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| JURISDICTION_MISMATCH_PROVEN | Exact basis path FALSE | Aggregate across other bases |
| JURISDICTION_UNRESOLVED | Exact basis path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| CONDITION_UNSATISFIED_PROVEN | Exact basis path FALSE | Aggregate across other bases |
| CONDITION_EVALUATION_UNAVAILABLE | Exact basis path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| POLICY_SUPERSEDED_OR_WITHDRAWN_PROVEN | Exact policy path FALSE/current exclusion | Recompute governing policy set |
| POLICY_CURRENTNESS_UNAVAILABLE | Policy path NOT_EVALUABLE | Query NOT_EVALUABLE if policy may govern |
| POLICY_NOT_APPLICABLE_PROVEN | Exclude that policy from q | Require policy-set closure |
| POLICY_SELECTION_UNRESOLVED | Policy set NOT_EVALUABLE | Query NOT_EVALUABLE |
| POLICY_CONFLICT_UNRESOLVED | Policy set NOT_EVALUABLE | Query NOT_EVALUABLE |
| TIME_SOURCE_UNRESOLVED | Snapshot NOT_EVALUABLE | Query NOT_EVALUABLE |
| TIME_SOURCE_CONFLICT_UNRESOLVED | Snapshot NOT_EVALUABLE | Query NOT_EVALUABLE |
| ROOT_STANDING_UNRESOLVED | Exact path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| ROOT_CONFLICT_UNRESOLVED | Exact path NOT_EVALUABLE | Query NOT_EVALUABLE if outcome-changing |
| AUTHORITY_PROVENANCE_CYCLE | Exact relied path NOT_EVALUABLE | Aggregate only if an acyclic alternative is lawfully sufficient |
| POLICY_PROVENANCE_CYCLE | Policy path NOT_EVALUABLE | Query NOT_EVALUABLE if policy may govern |
| REPLAY_DETECTED | No new authorization act | Downstream reliance blocked; actor authority assessed separately |
| AUTHORIZATION_CONSUMED | Particular reliance unavailable | Downstream eligibility blocked; grant authority may remain |

### Aggregation invariants

~~~text
PathFALSE != QueryFALSE
PathTRUE != QueryTRUE

OneResolvedBranch
↛ IgnoreUnresolvedMandatoryBranch

HistoricalTRUE@S1
↛ CurrentTRUE@S2

QueryTRUE
↛ MutationEligibilityELIGIBLE
~~~

Every NOT_EVALUABLE result retains all outcome-changing RootFailure values.
Every FALSE result identifies the positively established negative proposition
and the evidence/standing law that established it.

## 18. TEMPORAL / SNAPSHOT SEMANTICS

Time is not a caller-supplied indexical and a snapshot is not merely one clock
reading.

### Evaluation snapshot identity

EvaluationSnapshotIdentity binds:

- exact q;
- admitted request-act identity;
- principal and actor-attribution revisions;
- operation-definition identity and version;
- target identity and revision;
- role facts and activation state;
- policy corpus revision or epoch;
- authority-record corpus revision or epoch;
- grant, delegation, and revocation observation epochs;
- root bundle identities and assessment epochs;
- condition evidence revisions;
- time-source identities;
- reconciled evaluation time;
- uncertainty and tolerance;
- freshness bounds;
- dependency graph identity.

No storage format, transaction engine, clock service, or consensus technology
is selected.

### Snapshot consistency

~~~text
AssessmentInputObservedAtDifferentEpochs
and no standing reconciliation law proves consistency
→ SNAPSHOT_INCONSISTENT
→ affected assessment = NOT_EVALUABLE
~~~

A snapshot can be historically valid while no longer current:

~~~text
AuthorityApplicability(q, S1) = TRUE
and upstream basis changes before consequence gate at S2
→ S1 remains historical evidence
→ current authority at S2 is not established
→ consequence gate requires re-resolution
~~~

### Target change

If the target binding changes during assessment:

~~~text
TargetBinding(q, revision X)
!= TargetBinding(q, revision Y)

unresolved ordering or compatibility
→ TARGET_SNAPSHOT_STALE
→ current query = NOT_EVALUABLE
~~~

A standing grant may intentionally cover both revisions, but that scope must be
proven. Renaming, replacement, or successor identity never silently preserves
authority.

### Actor-attribution correction

An authorized correction does not rewrite the historical act. It invalidates
current reliance on the previous attribution:

~~~text
ActorAttributionBinding(A, act, S1)
corrected to
ActorAttributionBinding(B, act, S2)

AuthorityApplicability(A, q, S1)
remains historical

current reliance at S2
requires a new assessment for B
~~~

### Revocation race

For a revocation event R and snapshot S:

~~~text
R proven effective before S
→ affected grant path evaluated with revocation

R proven effective after S
→ assessment at S remains historical
→ later consequence gate must refresh

ordering between R and S unresolved
→ REVOCATION_ORDER_UNRESOLVED
→ affected grant path = NOT_EVALUABLE
~~~

Admission time, event occurrence time, effective time, and observation time
remain distinct.

### Policy amendment race

~~~text
Policy P1 governs S1
P2 becomes effective before consequence snapshot S2

AuthorityApplicability@S1
↛ CurrentAuthorityApplicability@S2
~~~

The policy candidate set, standing, applicability, and precedence must be
resolved again at S2.

### Time-source disagreement

Multiple time sources are not combined by averaging or source order. The
TimeSourceReconciliationAssessment requires standing reconciliation law.

If disagreement crosses an expiry, revocation, amendment, or condition
boundary and no standing resolution exists:

~~~text
TIME_SOURCE_CONFLICT_UNRESOLVED
→ EvaluationSnapshotIdentity = NOT_EVALUABLE
→ query = NOT_EVALUABLE
~~~

### Freshness

~~~text
TrustedTimeAt(t1)
↛ FreshTimeAt(t2)

CurrentAssessmentAt(S1)
↛ CurrentAssessmentAt(S2)
~~~

Freshness is evaluated against the rule governing each input, not one universal
duration.

## 19. MULTI-GRANT SEMANTICS

The repaired suite treats grants as candidate basis paths inside a closed
authority-basis set.

### Two permitting grants

Two applicable permit grants do not merge payloads by default.

~~~text
Permit(G1, operation READ, target A)
Permit(G2, operation WRITE, target B)
↛ Permit(READ + WRITE, targets A + B)
~~~

A standing composition law must authorize any union. Otherwise each grant can
support only the exact query it independently covers.

### Permit and prohibition

~~~text
G1:
  PERMIT WRITE on T

G2:
  PROHIBIT WRITE on T
~~~

Both may have true path assessments. The query is NOT_EVALUABLE unless a
standing policy resolves precedence or composition. No default deny-overrides,
permit-overrides, newest-wins, or root-wins rule is invented.

### Overlap with different conditions

If two grants overlap but use different conditions:

- each predicate is evaluated separately;
- each predicate's normative effect remains attached to its grant;
- satisfying one grant's conditions does not satisfy the other;
- a standing composition law decides whether one sufficient satisfied path is
  enough;
- unresolved conditions on an outcome-changing basis make the query
  NOT_EVALUABLE.

### Direct plus delegated grant

A direct grant and delegated grant retain distinct provenance.

~~~text
DirectGrantPath = TRUE
DelegatedGrantPath = FALSE
~~~

The query may be TRUE only if:

- the candidate set is closed or decision-complete;
- the direct grant is independently sufficient under standing composition law;
- the delegated path has no prohibitory or otherwise outcome-changing effect.

The valid direct path does not repair the invalid child record.

### Duplicate or aliased grants

Same text, same actor, or same payload does not prove one grant identity.
Identity resolution must distinguish:

- duplicate representations of one grant;
- two issuance events with identical payloads;
- lawful reissuance;
- retry of one issuance;
- forged or replayed representations.

Alias collapse without identity proof makes BasisSetClosureAssessment
NOT_EVALUABLE.

### Query-level FALSE

One invalid grant never establishes global absence of authority. Query FALSE
requires:

- exhaustive negative proof of no applicable grant or other basis; or
- a closed basis set in which every sufficient permit path is positively
  false and composition is resolved; or
- a standing prohibition whose composition law conclusively defeats every
  permit path.

## 20. MULTI-POLICY SEMANTICS

Multiple standing policies can be simultaneously applicable. Policy standing
does not guarantee compatibility.

### Candidate policy set

The policy corpus query must identify:

- all potentially applicable policy identities;
- their exact versions;
- adoption and currentness status;
- amendments, supersession, and withdrawals;
- jurisdictions and domains;
- the standing selection and composition law;
- corpus closure.

### Conflicting role semantics

~~~text
P1:
  role R required

P2:
  role R not required

both standing
both applicable to q
~~~

Possible lawful results require standing law:

~~~text
P1 precedes P2
P2 precedes P1
requirements compose and role is required
policy domains are proven disjoint
conflict remains unresolved
~~~

Without such law:

~~~text
POLICY_CONFLICT_UNRESOLVED
→ GoverningPolicySet = NOT_EVALUABLE
→ query = NOT_EVALUABLE
~~~

ROLE_NOT_REQUIRED cannot be selected merely because it produces fewer inputs.

### Amendment and supersession

The latest timestamp does not automatically define current policy. Amendment
identity, authority, effective interval, and supersession relation must be
standing and current.

If supersession is proven:

~~~text
superseded policy is excluded from current governing set
historical policy standing remains historical
~~~

If successor compatibility is unresolved:

~~~text
current policy selection = NOT_EVALUABLE
~~~

### Policy composition

Policies can be composed only over dimensions with a standing composition
algebra. Intersection is not universally valid.

For incomparable dimensions:

~~~text
POLICY_DIMENSION_NOT_COMPARABLE
→ PolicyPrecedenceResolution = NOT_EVALUABLE
~~~

### Policy-root conflict

If independently admitted roots recognize conflicting policy states, root
independence does not resolve normative conflict. A standing root-precedence
or composition law is still required.

## 21. REVOCATION / PARTIAL REVOCATION INTERSECTION

Revocation is an authority-bearing, temporally evaluated standing path.

### Required distinctions

~~~text
RevocationRepresentation
!= RevocationEvent
!= RevocationStandingRecord
!= CurrentRevocationAssessment
!= PartialRevocationEnvelope
~~~

### Revocation validity

A standing revocation requires:

- exact revocation event identity;
- actor attribution;
- authority for REVOKE_GRANT over the exact grant and portion;
- governing revocation policy at effective time;
- exact target grant identity;
- exact revoked dimensions;
- effective interval;
- provenance and custody;
- conflict and supersession handling.

An unresolved revocation claim cannot make a grant false. It can make grant
currentness NOT_EVALUABLE when outcome-changing.

### Partial revocation

Where a standing rule defines comparable set-like authority dimensions:

~~~text
EffectiveGrantEnvelope(S)
=
StandingGrantedEnvelope
minus
StandingEffectiveRevocationEnvelope(S)
~~~

This subtraction is lawful only when:

- both envelopes use the same typed dimension semantics;
- the revocation authority covers the removed portion;
- ordering and effective time resolve;
- the governing policy defines partial-removal behavior;
- no conflict or survivorship question remains.

For arbitrary predicates, subtraction or implication may be undecidable. The
result is NOT_EVALUABLE, never silently NARROWER.

### Parent and child

A child grant is evaluated against the effective parent envelope at the
relevant time, not the parent's original bytes alone.

~~~text
child permission within effective parent
→ continue other delegation checks

child permission wider than effective parent
→ child path FALSE for that permission

nonempty child permission DISJOINT from effective parent
→ DELEGATION_DISJOINT_FROM_PARENT
→ child path FALSE for that permission

comparison unavailable
→ child path NOT_EVALUABLE
~~~

### READ/WRITE partial-revocation case

~~~text
Parent initially permits:
  READ, WRITE

Standing partial revocation removes:
  WRITE

Child contains:
  READ, WRITE
~~~

Result:

- child's WRITE path is FALSE if revocation effect and parent-child law are
  established;
- child's READ path is not automatically surviving;
- READ can remain viable only if standing survivorship policy permits it and
  every other dependency resolves;
- absent survivorship law, READ is NOT_EVALUABLE;
- the whole query still aggregates alternate bases.

### Revocation conflict

Conflicting standing revocations require precedence/composition law. Neither
record order nor strongest restriction is selected by default.

### Parent expiry

Parent expiry and parent revocation are distinct. No cascade or survivorship
rule transfers automatically between them.

## 22. CONSUMPTION / USE-STATE BOUNDARY

The old phrase use state collapsed two different questions.

### Intrinsic grant use state

Some grants may themselves define a finite-use authority constraint. When that
constraint has standing, grant currentness may consume:

~~~text
GrantIntrinsicUseConstraint
GrantUseStateRecord
GrantUseStateAssessment
~~~

This asks:

~~~text
Does the grant itself still confer authority under its intrinsic use law?
~~~

It is part of GrantCurrentnessAssessment only when the standing grant or
governing policy explicitly defines such a constraint.

### Authorization-act consumption

AuthorizationActConsumptionEvent and CurrentAuthorizationReliance ask:

~~~text
May this particular admitted authorization act still be relied upon
for this downstream consequence?
~~~

That remains downstream from authority applicability.

### Non-collapse

~~~text
GrantUseExhausted
may make one grant basis path FALSE
under standing intrinsic-use law

AuthorizationActConsumed
blocks reliance on that act
but does not necessarily make actor authority FALSE

MutationOccurred
does not by itself prove either form of lawful consumption
~~~

The same historical occurrence may be evidence for both domains only when
separate standing laws admit it for each purpose. One assessment never
silently substitutes for the other.

### Replay, retry, and reissuance

~~~text
Replay:
  reuse of the same admitted act or consumed reliance

Retry:
  repeated delivery or processing attempt for one event identity

LawfulReissuance:
  distinct issuance event with its own identity, attribution,
  authority, policy, and snapshot
~~~

SameText does not prove SameEvent. NewMessage does not prove NewAuthorization.

### Downstream firewall

AuthorityApplicabilityAssessment excludes:

- particular authorization-act consumption;
- runtime capability;
- safety approval;
- environment readiness;
- human confirmation;
- review completion;
- locks and reservations;
- rollback readiness;
- mutation preconditions.

~~~text
AuthorityApplicabilityAssessment = TRUE
↛ MutationEligibilityDecision = ELIGIBLE
~~~

## 23. REPLAYED RELEVANT A-W TRACES

All A–W traces are replayed because B1–B7 alter the level at which path,
policy-set, basis-set, and query dispositions are calculated.

Unless the input facts establish candidate-set closure or a standing
decision-completeness law, one resolved path does not establish the query.

| Trace | Input facts and asserted claim | Repaired bindings and current assessments | Root failure | AA | Mutation eligibility effect | Repair-session disposition |
|---|---|---|---|---|---|---|
| A | Founder-like packet; claims ROOT/FULL/GLOBAL; no external refs | Request occurrence only; principal, actor, basis, policy, target, root, and snapshot unresolved | Multiple unresolved mandatory roots | NOT_EVALUABLE | Must not proceed | Labels cannot form a root bundle or closed basis set |
| B | Actor valid; required role mismatches | Selected role-required basis path is FALSE; alternate-basis closure absent | ROLE_MISMATCH_PROVEN on one path; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Path FALSE is not query FALSE |
| C | Actor valid; direct grant representation; policy text says no role | Grant standing, root bundle, policy selection, and basis closure are not established by representation/text | ROOT_STANDING_UNRESOLVED; POLICY_SELECTION_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Role-neutral result requires a selected standing basis and policy |
| D | Valid role; target outside one grant | Exact grant path has SCOPE_MISMATCH; alternate bases unclosed | SCOPE_MISMATCH_PROVEN on one path; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Scope path FALSE does not exhaust authority |
| E | Grant bytes; issuer proven unauthorized | Exact grant path FALSE at issuance; alternate bases unclosed | GRANT_INVALIDLY_ISSUED; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Invalid bytes remain invalid; global absence not proven |
| F | One otherwise valid grant expired | Exact grant path FALSE; alternate bases unclosed | GRANT_EXPIRED_PROVEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Expiry is path-relative |
| G | One grant has standing effective revocation | Exact grant path FALSE; alternate bases unclosed | GRANT_REVOKED_PROVEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Revocation does not erase another basis |
| H | Parent revoked; child exists; no survivorship law | Child path cannot resolve effective parent envelope | DELEGATION_SURVIVORSHIP_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Neither cascade nor survival is invented |
| I | Child provably wider than parent | Child path FALSE; alternate bases unclosed | DELEGATION_CHAIN_BROKEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Non-widening holds at path level |
| J | Grant valid elsewhere | Foreign-jurisdiction path FALSE; alternate bases unclosed | JURISDICTION_MISMATCH_PROVEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Jurisdiction mismatch does not prove no other basis |
| K | Grant tied to superseded policy | If supersession is proven, that policy/basis path is FALSE for current reliance; successor set unresolved | POLICY_SUPERSEDED_PROVEN; POLICY_SELECTION_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Proven staleness differs from unavailable currentness |
| L | Historical act predates amendment | Occurrence remains historical; current policy and reliance require S2 | POLICY_SNAPSHOT_STALE | NOT_EVALUABLE until re-resolved | Must not proceed | Historical occurrence does not preserve current reliance |
| M | Quote only | Quote event admitted; underlying authorization act and basis absent | AUTHORIZATION_ACT_NOT_ADMITTED; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Event species remain distinct |
| N | One-use act consumed; bytes replayed | No new act; underlying authority basis assessed separately | REPLAY_DETECTED and AUTHORIZATION_CONSUMED downstream | TRUE only if separately closed current authority query resolves; otherwise NOT_EVALUABLE | Replay/reliance blocked | Consumption does not negate actor authority by itself |
| O | Same language lawfully reissued as a distinct admitted act; issuer current; all authority inputs including closure stipulated resolved | New event identity; complete current basis and policy assessment stipulated | None under stated complete premise | TRUE | Authority prerequisite only | Same text does not collapse event identity |
| P | Session-response grant; repo mutation requested | Session path has scope mismatch; repository-basis set unclosed | SCOPE_MISMATCH_PROVEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Session authority cannot widen into repo authority |
| Q | Subject issues and validates own grant; no root | Cyclic basis path only | AUTHORITY_PROVENANCE_CYCLE | NOT_EVALUABLE | Must not proceed | No acyclic root termination |
| R | Same runtime has independently rooted roles; runtime equality asserted as authority | Role facts resolve; an authority root and closed basis set do not follow | AUTHORITY_ROOT_UNRESOLVED; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Same runtime is neither cycle nor authority |
| S | Condition true at t1 and false at t2 | Exact conditional basis path FALSE at S2; alternate bases unclosed | CONDITION_UNSATISFIED_PROVEN; BASIS_SET_CLOSURE_UNRESOLVED | NOT_EVALUABLE at query level | Must not proceed | Historical satisfaction is not current satisfaction |
| T | Operation exact; target unresolved | Required target binding absent | TARGET_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Lexeme is not target identity |
| U | AA fully TRUE by complete stipulated assessment; safety false | Authority result remains TRUE; safety remains downstream | No authority root failure | TRUE | Ineligible | Downstream failure does not rewrite AA |
| V | Policy bytes self-claim ratification | Adoption standing and adoption authority cycle unresolved | POLICY_PROVENANCE_CYCLE | NOT_EVALUABLE | Must not proceed | Policy cannot establish its own standing |
| W | Request says CURRENT and NOW | Policy candidate set and snapshot time unresolved | POLICY_SELECTION_UNRESOLVED; TIME_SOURCE_UNRESOLVED | NOT_EVALUABLE | Must not proceed | Indexicals are not governed evidence |

The changed B, D–G, I–K, P, and S outcomes are deliberate: their exact failing
paths are FALSE, while the whole query remains NOT_EVALUABLE until alternative
basis closure is established.

## 24. REPLAYED RELEVANT X1-X15 COUNTERMODELS

| Case | Pressure input | Repaired evaluation | Disposition under repair |
|---|---|---|---|
| X1 | Two valid grants; G1 permits WRITE and G2 prohibits WRITE | Both path assessments may be TRUE with opposing effects. Candidate set must be closed and composition law standing. | NOT_EVALUABLE absent precedence/composition; no convenience rule |
| X2 | Two applicable policies; P1 requires role R and P2 says role not required | Both policies retain standing and applicability. PolicyPrecedenceResolution must resolve the semantic conflict. | NOT_EVALUABLE absent standing policy composition |
| X3 | Target resolves to revision X and changes to Y during evaluation | EvaluationSnapshotIdentity no longer matches current target. | Historical result at X may remain; current query NOT_EVALUABLE until rebound at Y |
| X4 | Revocation races evaluation snapshot | Occurrence, effective, observation, and snapshot order must resolve. | NOT_EVALUABLE if order unresolved; path FALSE if revocation proven effective first |
| X5 | P1 supports AA at t1; amendment P2 becomes effective before execution | AA@S1 remains historical. Governing policy set must resolve at S2. | Current AA NOT_EVALUABLE until refreshed; eligibility blocked |
| X6 | Actor attribution corrected from A to B after authorization | Historical A attribution remains historical; current reliance invalidated. | New B-bound assessment required; current query NOT_EVALUABLE until resolved |
| X7 | Two standing time sources disagree across expiry boundary | No averaging or ordering by convenience. | NOT_EVALUABLE without standing time-source reconciliation |
| X8 | Parent READ/WRITE; partial revocation removes WRITE; child READ/WRITE | WRITE child path FALSE if revocation and comparison resolve. READ depends on standing survivorship law. | WRITE FALSE at path level; READ NOT_EVALUABLE absent survivorship; query aggregates other bases |
| X9 | Two independent roots conflict about P | RootIndependenceAssessment does not imply conflict resolution. | NOT_EVALUABLE absent standing root precedence/composition |
| X10 | AA TRUE at t1; grant stale before consequence gate | Snapshot S1 result remains historical; S2 freshness fails. | Authority must be reassessed; mutation eligibility blocked |
| X11 | Authoritative exhaustive registry proves no matching grant | ExhaustiveNegativeProof binds q, S, authoritative domain, coverage, and standing query law. | Query FALSE if the closed authority model requires a grant and no other basis kind can apply |
| X12 | Parent READ on A; child WRITE on B; comparison DISJOINT | Nonempty child authority lies outside effective parent envelope. | Child path FALSE with DELEGATION_DISJOINT_FROM_PARENT; query result still requires basis closure |
| X13 | ROLE_NOT_REQUIRED comes from G whose standing depends on unresolved P | Role neutrality cannot be consumed before G and P resolve. | NOT_EVALUABLE |
| X14 | Child predicate implication is undecidable | Generic evaluator cannot establish AllowedStates(child) subset of AllowedStates(parent). | Delegation path NOT_EVALUABLE, never NARROWER |
| X15 | P recognizes G; G authorizes adoption of P; no predecessor/root | Explicit adoption-authority and grant-standing edges form one required cycle. | POLICY_PROVENANCE_CYCLE and AUTHORITY_PROVENANCE_CYCLE; NOT_EVALUABLE |

These outcomes are candidate authoring results. They demonstrate how the
proposed repair addresses the review countermodels; they are not an
independent confirmation that the repair succeeds.

## 25. NEW COUNTERMODELS DISCOVERED DURING REPAIR

The repair was pressure-tested during authoring against additional cases. This
is falsification input, not self-review.

| ID | New hostile case | Required repaired result |
|---|---|---|
| Y1 | A basis registry says its query is exhaustive, but the law giving it that status expired before S. | Corpus coverage is NOT_EVALUABLE; the registry cannot produce ExhaustiveNegativeProof. |
| Y2 | Two corpora return the same grant digest but different issuance-event identities. | Do not alias by payload digest; identity resolution is NOT_EVALUABLE until event relation resolves. |
| Y3 | A policy precedence rule says newest wins, but its own adoption depends on the newest candidate policy. | POLICY_PROVENANCE_CYCLE; precedence is NOT_EVALUABLE. |
| Y4 | A valid permit basis is discovered after a FALSE query result from an earlier non-exhaustive search. | Earlier query was never lawfully FALSE; it must have been NOT_EVALUABLE. |
| Y5 | An exhaustive negative proof is current for S1 but reused after the corpus epoch advances to S2. | Proof is stale; current query NOT_EVALUABLE pending new proof. |
| Y6 | One snapshot uses actor attribution epoch A2 and grant registry epoch G1, but G1 was indexed only against actor epoch A1. | SNAPSHOT_INCONSISTENT; query NOT_EVALUABLE absent reconciliation. |
| Y7 | Root R is independent of grant cycle C but controlled by the actor whose authority is being assessed through an undisclosed control relation. | RootIndependenceAssessment cannot be TRUE until the named control domain is resolved. |
| Y8 | Two permit grants are individually narrower, but their unauthorized union would exceed both issuers' ceilings. | Never union without standing composition law; evaluate each path only for q. |
| Y9 | A standing prohibition applies only to production, while target environment identity is unresolved. | Prohibition applicability and permit result are outcome-changing; query NOT_EVALUABLE. |
| Y10 | A revocation is valid but retroactive effect is asserted only inside its own bytes. | Retroactivity is not established; current/historical effects NOT_EVALUABLE without standing revocation policy. |
| Y11 | Policy P is standing and applicable, but its required predicate evaluator version is unavailable. | Condition path NOT_EVALUABLE; policy standing remains TRUE. |
| Y12 | A policy set has two incomparable maximal policies and no total order is required by its standing law. | Use standing partial-order composition if defined; otherwise POLICY_CONFLICT_UNRESOLVED. |
| Y13 | A direct grant is TRUE and a delegated grant is cyclic but the composition law says direct grants are independently sufficient and delegated paths cannot prohibit. | If candidate-set closure and law standing resolve, select direct acyclic path; unused cycle is harmless. |
| Y14 | An empty grant result comes from an authoritative corpus, but standing law permits oral grants outside that corpus. | The domain is not exhaustive; absence observation yields NOT_EVALUABLE. |
| Y15 | One-use grant exhaustion is inferred solely because one authorization act was consumed. | No inference without standing mapping from act consumption to intrinsic grant use; grant currentness remains separately assessed. |

The new cases expose no authority to widen this pass into implementation,
schema, storage, Gene, Foundation, AgentBridge, DATASELF, or Notepad work.

## 26. B1-B7 CLOSURE MATRIX

Closure below is the repair author's candidate disposition. It is not PASS and
does not replace fresh independent hostile review.

| Finding | Repair mechanism | Countermodels exercised | Candidate status |
|---|---|---|---|
| B1 | Typed basis discovery, candidate-set closure, path assessment, and standing composition | Original expired-plus-valid basis; X1, X11, Y2, Y4, Y8, Y13, Y14 | CLOSED |
| B2 | RootResolutionBundle with separate standing, independence, applicability, currentness, and conflict assessments; no positive root invented | Founder-labeled self-proof; X9, Y7 | CLOSED |
| B3 | Distinct PolicyStandingAssessment and PolicyApplicabilityAssessment plus currentness and precedence | Cross-jurisdiction standing/applicability split; X2, Y11 | CLOSED |
| B4 | Explicit adoption-authority, predecessor/root, policy discovery, selection, and precedence edges in the DAG | Hidden policy cycle; X15, Y3 | CLOSED |
| B5 | Closed primary-type inventory for every B1–B7 graph node; StandingRecord qualification | Untyped revocation assessment; use-state and event intermediate pressure | CLOSED |
| B6 | Minimum-count claim withdrawn; generic actor attribution/predicate evaluation moved upstream; missing governance, discovery, and time surfaces added | Ownership countermodel; X3–X7 | CLOSED |
| B7 | General exhaustive-negative-proof law and separate path/set/query dispositions | X11; one FALSE plus unresolved alternative; Y1, Y4, Y5, Y14 | CLOSED |

Reasons these closures are more than added labels:

- B1 includes an aggregation decision table and closure obligations.
- B2 prevents positive root use unless every typed assessment resolves.
- B3 gives disjoint input/output questions for standing and applicability.
- B4 adds the exact missing graph edges and cycle result.
- B5 assigns every used node one primary type and supplies cast invariants.
- B6 changes semantic ownership and withdraws the unsupported minimum claim.
- B7 defines proof obligations for FALSE and quantification over the closed
  basis set.

Only a fresh reviewer may determine whether any repair is incomplete or creates
a new blocking countermodel.

## 27. SURVIVING UNRESOLVED ROOTS

The repair intentionally does not establish:

- positive human or Founder-origin proof;
- a positive constitutional root;
- authority for governance-root admission;
- exact root independence adjudication;
- cross-root conflict precedence;
- cross-jurisdiction root recognition;
- authority over principal and actor-attribution registries;
- standing of role-possession and activation sources;
- role self-activation law;
- operation registry ownership;
- target registry and custody ownership;
- standing time sources;
- time-source conflict reconciliation;
- policy corpus authority and closure;
- authority for policy adoption;
- the first predecessor policy or primitive governance boundary;
- policy precedence and composition law;
- authority-record corpus ownership;
- proof that all relevant authority corpora are known;
- grant alias and cross-corpus identity law;
- multi-basis composition law;
- partial-revocation comparison law;
- revocation conflict precedence;
- parent-expiry and parent-revocation survivorship;
- arbitrary predicate implication;
- condition evaluator standing;
- canonical event and authorization-act taxonomy;
- standing mapping between intrinsic grant use and recorded consumption;
- downstream mutation-eligibility policy.

Every unresolved root remains capable of producing NOT_EVALUABLE. None is
converted into TRUE by this report's existence, commit, or publication.

~~~text
UnresolvedRoot != FalseRoot
UnresolvedRoot != ValidRoot
NamedInterface != StandingInterface
CandidateClosure != IndependentReviewPass
~~~

## 28. WHAT WAS NOT REPAIRED

Out of scope and unchanged:

- material or advisory review findings not required for B1–B7 coherence;
- canonical lineage dispositions;
- target-organ adoption;
- source-admission generalization beyond the interfaces consumed here;
- a universal scope comparison algebra;
- a universal revocation cascade or survivorship law;
- a concrete clock, database, transaction, snapshot, or storage mechanism;
- schemas;
- runtime code;
- authorization consumption implementation;
- mutation eligibility implementation;
- AgentBridge doctrine or implementation;
- DATASELF doctrine or implementation;
- Gene candidate text;
- Foundation IR candidate text;
- Notepad semantics;
- ClaudeSELF projection;
- ratification;
- seal;
- constitutional promotion.

New unresolved observations encountered during authoring are recorded in
sections 25 and 27. They were not used to expand mutation scope.

The original target remains exact at its witnessed bytes. This repair artifact
is a distinct candidate:

~~~text
OriginalArtifactBytes != RepairArtifactBytes
RepairCandidate ↛ SourceTargetReplacement
RepairCandidate ↛ Adoption
~~~

## 29. EXACT GENE IMPLICATION

~~~text
GENE_AUTHORITY_BRANCH = HOLD
GENE_STANDING = UNCHANGED
GENE_FILE_MUTATION = NOT_AUTHORIZED
~~~

This repair does not establish:

~~~text
GenesisAuthority(...) = VALID
~~~

It supplies only a stronger candidate vocabulary for a later, separately
authorized Gene repair after independent review and Founder adjudication.

Any future Gene authority assessment would still require:

- exact CREATE_SELF or GENESIS operation binding;
- exact Genesis subject/target binding;
- actor and role context;
- closed authority-basis set;
- lawful root termination;
- governing-policy-set resolution;
- current evaluation snapshot;
- every independent Gene safety, necessity, forbidden-cast, evidence, and
  consequence gate.

~~~text
RepairCandidate
↛ GeneRepairAuthority

AuthorityApplicability = TRUE
↛ GenesisMutationEligible
~~~

No Gene file was read for mutation, edited, staged, or included in this
artifact commit.

## 30. EXACT FOUNDATION IR IMPLICATION

~~~text
FOUNDATION_AUTHORITY_BRANCH = HOLD
FOUNDATION_STANDING = UNCHANGED
FOUNDATION_FILE_MUTATION = NOT_AUTHORIZED
~~~

This repair does not replace:

~~~text
Authority(T) = VALID
~~~

inside any Foundation artifact. A later separately authorized repair may
consume a reviewed authority-applicability model, but it would still require:

- exact transmutation operation;
- exact source and target representations;
- exact Foundation IR boundary;
- actor and role;
- governing policy;
- current snapshot;
- invariant equivalence;
- preserved provenance;
- forbidden cast equal to zero;
- downstream safety and consequence gates.

~~~text
RepairCandidate
↛ FoundationRepairAuthority

AuthorityApplicability = TRUE
↛ FoundationSafeTransmutation
~~~

No Foundation IR file was edited, staged, or included in this artifact commit.

## 31. SELFIR CONTINUATION STATUS

~~~text
SELFIR = ACTIVE_ON_UNRELATED_BRANCHES
AuthorityBranchBlocked != SELFIRBlocked
NOTEPAD_INTEGRATION = DEFERRED
~~~

Unrelated, separately authorized SELFIR work may continue on:

- semantic invariants;
- representation identity;
- meaning preservation;
- semantic equivalence;
- directional conservation;
- semantic loss;
- contradiction and non-weakening;
- forbidden semantic casts;
- lineage and provenance preservation;
- representation-specific versus representation-neutral semantics;
- translation, transmutation, and amendment separation.

That work must stop at any transition that consumes:

- an unresolved authority root;
- Gene or Foundation mutation authority;
- Notepad semantics;
- foreign-runtime authority.

If a future authority repair actually requires Notepad live semantics:

~~~text
WAIT_FOR_NOTEPAD_LIVE_CONTRACT
~~~

That stop applies only to the dependent branch. It does not hold unrelated
SELFIR work.

## 32. REQUIRED NEXT LAWFUL GATE ONLY

~~~text
NOT_OPEN_AUTOMATICALLY

AUTHORIZE_AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_
SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001_
INDEPENDENT_HOSTILE_REVIEW_001_READ_ONLY

RUNTIME:
  FRESH CODEXSELF REVIEW CONTEXT

SESSION LAW:
  ReviewerSession != RepairSession
  Review != Repair
  Review != Adoption
  Review != Ratification

INPUT:
  exact GitHub repository identifier
  exact branch
  exact commit
  exact artifact path
  exact artifact SHA-256 from post-push witness

TARGET:
  AUTHORITY_APPLICABILITY_PROVENANCE_SUITE_
  SEMANTIC_RECONCILIATION_001_BOUNDED_REPAIR_001.md

REQUIRED:
  verify exact bytes
  attempt to falsify B1-B7 candidate closures
  rerun A-W
  rerun X1-X15
  attack Y1-Y15
  test all new root and composition assumptions
  return PASS, CHANGES_REQUIRED, or NOT_EVALUABLE

BOUNDARIES:
  READ ONLY
  NO REPAIR
  NO ADOPTION
  NO RATIFICATION
  NO SEAL
  NO GENE MUTATION
  NO FOUNDATION IR MUTATION
  NO AGENTBRIDGE MUTATION
  NO DATASELF MUTATION
  NO NOTEPAD SEMANTICS
  NO CLAUDESELF PROJECTION

STOP:
  immediately after the independent hostile-review report
~~~

Publication of this artifact establishes only that exact candidate bytes exist
in repository history.

~~~text
GitHubPresence != CanonicalStanding
Commit != Ratification
Push != Adoption
ArtifactExists != RepairPassed

POST_PUBLICATION_STANDING:
  CANDIDATE
  NONCANONICAL
  NOT_INDEPENDENTLY_REVIEWED_AFTER_REPAIR
  NOT_ADOPTED
  NOT_RATIFIED
~~~
