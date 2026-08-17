# NOTEPAD-000 GENESIS, CUSTODY, AND CONTEXT ATTACHMENT CONTRACT v0.2

```yaml
artifact_id: NOTEPAD-000
artifact_class: SEMANTIC_REPAIR_SUCCESSOR_CANDIDATE
version: v0.2
status: AUTHORED_CANDIDATE
standing: UNRATIFIED
sealed: false
implemented: false
jurisdiction: BOUNDED_CROSS_ORGAN_NOTEPAD_CONTRACT
custody_repository: situaedmilly/ruora
custody_branch: governance/notepad-000-genesis-contract
predecessor_commit: f47becbe5c99ca6634d756d5fec47389ac229211
predecessor_contract_sha256: d5aca8c7f6377bde217a4711b800905c819564fec17ef04b608897f54cd8370e
predecessor_evidence_sha256: d8d3a7cea47d2ec865b6c56292ebf2482c3846e8bf7366b88102c5f6c05da1a2
repair_review_session: 01a00f71-70aa-7613-8f52-1873f7bc8afc
repair_review_verdict: CHANGES_REQUIRED
repair_authority: AUTHORIZE_NOTEPAD_000_R01_BOUNDED_SEMANTIC_REPAIR_001
control_effect: NONE
ratification_effect: NONE
runtime_effect: NONE
implementation_authority: NONE
```

## 0. Successor standing and byte-history law

This artifact is a semantic repair successor to the immutable v0.1 reviewed
subject. It does not rewrite, replace in Git history, ratify, implement, or
silently supersede v0.1.

```text
ReviewedSubject != RepairedSubject
Repair != Review
Repair != Ratification
SuccessorCustody != PredecessorErasure
```

The repair commission is limited to findings returned by
`AUTHORIZE_NOTEPAD_000_INDEPENDENT_HOSTILE_REVIEW_001`. Stable references for
those findings in this successor are `IHR-R01` through `IHR-R20`, corresponding
to review chambers R1 through R20. These identifiers organize repair provenance;
they do not rewrite the review return.

This candidate creates no runtime, database, API, mobile application, central
registry, SELF identity, ACTIMANIRUN dependency, SELFIR implementation, or
NOTEPAD-001 lease.

## 1. Retained prime law

```text
NOTE
!= NOTEPAD
!= SOURCE_TRUTH
!= EVIDENCE
!= DECISION
!= DOCTRINE
!= STANDING
!= AUTHORITY
```

```text
ContextMayInform != ContextMayControl
ContainerStanding != ContainedMeaningStanding
RecordStanding != PropositionStanding
Publication != Ratification
Publication != ImplementationAuthorization
```

A note is attributed context. No property of its container, custody, author,
attachment, publication, or governing surface promotes the propositions inside
it.

## 2. Root ontology repair [IHR-R01]

### 2.1 Shared primitive

The shared primitive is the representation-neutral `NotepadContract`. It
defines the minimum semantics required for contextual note handling across
otherwise sovereign jurisdictions.

The v0.1 `NotepadRole` is removed as an independent primitive. The behavior it
attempted to name is fully derived from three separate assessments:

```text
InterfaceConformance
!= SurfaceCapability
!= JurisdictionAdmission
```

### 2.2 Surface capability

`SurfaceCapabilityAssessment(S,t)` records whether surface `S` can perform a
candidate operation at time `t`, such as preserve, present, attach, redact, or
export context.

Capability is descriptive. It grants no conformance, admission, standing, or
authority.

```text
SurfaceCapable != ContractConformant
SurfaceCapable != JurisdictionAdmitted
```

### 2.3 Contract conformance

`ContractConformanceDisposition(S,V,t)` determines whether surface `S`
conforms to contract version `V` at time `t` under a standing-bearing
conformance rule and authorized assessor.

The disposition must bind:

- surface identity and version;
- contract identity and version;
- mandatory-core test set;
- extension declarations;
- assessor authority reference;
- basis references;
- time and validity interval;
- result and failure state.

Self-declared conformance is a claim, not a disposition.

### 2.4 Jurisdictional admission

`JurisdictionAdmissionDecision(S,J,V,t)` is a jurisdiction-local decision that
admits, rejects, suspends, or revokes surface `S` for jurisdiction `J` under
contract version `V`.

Admission requires independently established authority in `J`. Conformance is
necessary but cannot self-admit the surface.

### 2.5 Derived admitted-surface state

```text
AdmittedNotepadSurface(S,J,V,t)
iff
SurfaceCapabilityAssessment(S,t) satisfies required operations
AND ContractConformanceDisposition(S,V,t) = CONFORMANT_CURRENT
AND JurisdictionAdmissionDecision(S,J,V,t) = ADMITTED_CURRENT
```

`AdmittedNotepadSurface` is a derived state, not a role identity and not an
institution.

Failure of any operand fails closed for governed use without erasing the
surface's independent identity or its historical records.

## 3. NOTE identity constitution [IHR-R02]

### 3.1 Three identity layers

```text
NOTE_LINEAGE_IDENTITY
!= NOTE_VERSION_IDENTITY
!= NOTE_CONTENT_IDENTITY
```

- `NOTE_LINEAGE_IDENTITY` identifies the continuing contextual record across
  lawful revisions.
- `NOTE_VERSION_IDENTITY` identifies one immutable admitted state of that
  lineage.
- `NOTE_CONTENT_IDENTITY` identifies content bytes or canonical content by an
  explicitly named digest or equivalent content-addressing method.

```text
SameLineage != SameVersion
SameVersion != SameContentAddress
SameContent != SameNote
FileIdentity != NoteIdentity
AttachmentIdentity != NoteIdentity
```

A path, row number, list position, UI card, or repository filename cannot be a
constitutional Note identity by itself.

### 3.2 Constitutive creation act

A new NOTE lineage exists when an accountable creation occurrence binds:

```yaml
NoteCreationOccurrence:
  lineage_identity:
  initial_version_identity:
  content_identity_or_inline_content:
  author_provenance:
  created_time:
  originating_jurisdiction:
  source_refs: []
  record_state:
```

Creation of an ephemeral Note occurrence does not require institutional custody
or T5. Admission to a governed surface separately requires current write and
admission authority.

### 3.3 Immutable admitted versions

Once a Note version is admitted, its content and constitutive provenance are
immutable. Correction creates a new version or successor; it never overwrites
the admitted version in place.

Every admitted Note version binds exactly one `NOTE_CONTENT_IDENTITY`. Inline
content without a content identity is permitted only before governed admission.

Mutable drafts may exist before admission, but:

```text
MutableDraft != AdmittedNoteVersion
DraftIdentity != GoverningRecordStanding
```

### 3.4 Transition matrix

| Transition | Lineage result | Version result | Required provenance | Authority boundary |
| --- | --- | --- | --- | --- |
| `CREATE` | new lineage | initial version | author, time, origin, content/source | creation may be personal; governed admission requires write authority |
| `REVISE` | same lineage | new immutable version | predecessor version, editor, reason | governed surface write authority |
| `SUCCESSOR` | new lineage | initial version | predecessor lineage, succession reason | admission and any supersession authority |
| `FORK` | new lineage | initial version | fork source version, actor, divergence point | fork creation plus local admission authority |
| `IMPORT` | new lineage by default | initial version | external source, importer, import method | import and local admission authority |
| `PROJECTION` | new lineage | initial version | source version, transform, projector | projection and local admission authority |
| `REPLICA` | source lineage retained | source version retained | source version proof, replica identity, custodian | replica custody authority; no content mutation authority |
| `MIRROR` | no Note lineage change by itself | no Note version change by itself | mirror agreement, source, replicas, sync policy | mirror establishment authority; no source authority |

Identity-preserving import is not `IMPORT`; it is a verified `REPLICA` operation.
A quotation always creates content in another Note lineage and never inherits the
quoted Note identity.

### 3.5 Successor and supersession

`REVISE` preserves lineage. `SUCCESSOR`, `FORK`, `IMPORT`, and `PROJECTION`
create new lineage. Supersession is an explicit relation with authority and
scope; a later timestamp alone cannot supersede a Note.

```text
LaterVersion != AutomaticCurrentVersion
LaterNote != AutomaticSuccessor
Successor != HistoricalErasure
```

## 4. NOTE semantic anatomy [IHR-R02, IHR-R08]

This remains a semantic shape, not an executable schema:

```yaml
NOTE:
  lineage_identity:
  version_identity:
  content_identity_or_content:
  author_provenance:
  runtime_projection:
  created_time:
  source_refs: []
  claim_atoms: []
  context_type:
  record_standing:
  visibility_policy_ref:
  retention_policy_ref:
  predecessor_version_ref:
  lineage_relation_refs: []
  custody_replica_refs: []
```

Attachments are referenced from independent `ContextAttachment` objects and do
not constitute Note identity.

## 5. Proposition-level attribution [IHR-R08]

### 5.1 Optional ClaimAtom

A Note may remain unstructured human context. A machine-consumable proposition
must be represented by an attributable `ClaimAtom`:

```yaml
ClaimAtom:
  claim_identity:
  note_version_ref:
  span_ref_or_content_ref:
  proposition_type:
  attribution:
  source_refs: []
  proposition_standing:
  assessed_at:
  assessment_authority_ref:
  applicability_or_time:
```

Candidate proposition types such as quotation, hypothesis, observation,
declaration, derivation, humor, and stale context are examples, not a closed
universal vocabulary.

### 5.2 Safe fallback

If no ClaimAtom exists, or a consumer cannot resolve the ClaimAtom:

```text
EntireNoteContent = ATTRIBUTED_UNASSESSED_CONTEXT
```

It may be displayed as context. It may not be consumed as established
proposition truth, evidence standing, authority, or machine-action input.

Any content span not covered by a valid ClaimAtom remains
`ATTRIBUTED_UNASSESSED_CONTEXT`. One assessed ClaimAtom cannot uplift the
standing of adjacent or otherwise uncovered content.

No system is required to parse every sentence. The requirement activates only
when a downstream system wants to consume a proposition independently of the
Note as contextual text.

```text
GovernedNote != GovernedPropositions
VerifiedClaimAtom != VerifiedWholeNote
FounderAuthorship != CurrentAuthority
```

## 6. ContextAttachment repair [IHR-R03]

### 6.1 First-class relation

```text
ATTACHES_CONTEXT_TO(note_version_identity, target_identity, relation_purpose)
```

Each attachment has independent identity, authority, visibility, provenance,
and lifecycle. One Note version may attach to many targets; one target may have
many attachments.

### 6.2 Relation purposes

| Relation | Meaning | Authority effect | Standing effect | Control-flow effect |
| --- | --- | --- | --- | --- |
| `CONTEXT_FOR` | General attributed context for a target | NONE | NONE | NONE |
| `QUESTION_ABOUT` | Records an unresolved question about a target | NONE | NONE | NONE |
| `FLAGS_POTENTIAL_CONTRADICTION_WITH` | Claims an apparent conflict requiring separate evaluation | NONE | NONE | NONE |
| `PROVIDES_HANDOFF_CONTEXT_FOR` | Supplies supplementary context around a handoff subject | NONE | NONE | NONE |

`CONTRADICTION_WITH` is removed because an attachment cannot establish logical
or institutional contradiction merely by naming it.

```text
ContradictionClaim != EstablishedContradiction
PotentialConflictFlag != ContradictionDisposition
```

An established contradiction requires a separate governed evaluation under the
relevant proposition and evidence law.

### 6.3 Handoff boundary

```text
HandoffContext
!= TransportAct
!= AdmissionAct
!= CustodyTransfer
!= LeaseTransfer
```

`PROVIDES_HANDOFF_CONTEXT_FOR` proves no packet creation, delivery, receipt,
acceptance, INSELFACTION admission, or authority transfer. Where a future
handoff depends on INSELFACTION, the dependency must be resolved by a separate
integration gate.

### 6.4 Vocabulary extension

Local relation purposes may extend the vocabulary only if they preserve the
mandatory zero-authority, zero-standing, and zero-control defaults. Unknown or
incompatible relation purposes fail closed for automated consumption.

## 7. Target resolution and privacy [IHR-R05, IHR-R09]

### 7.1 Four authority axes

```text
DISCOVERY_AUTHORITY
!= METADATA_DISCLOSURE_AUTHORITY
!= SELECTION_AUTHORITY
!= WRITE_AUTHORITY
```

Discovery may establish internally that candidates exist without authorizing
their identity, count, location, jurisdiction, or policy metadata to be shown to
the requester.

### 7.2 Privacy-safe result views

A resolver may produce an internal policy result and a requester-visible result.
The requester-visible result must be filtered by metadata-disclosure authority.

If existence itself is restricted, the requester-visible state is
`TARGET_UNRESOLVED`; it must be observationally indistinguishable from a scoped
null. `TARGET_HIDDEN_BY_POLICY` may appear only to a policy-authorized auditor.

### 7.3 Terminal states

- `EXACT_TARGET_RESOLVED`
- `FUNCTIONAL_CANDIDATES_RESOLVED`
- `TARGET_AMBIGUOUS`
- `TARGET_HIDDEN_BY_POLICY`
- `TARGET_UNRESOLVED`
- `TARGET_INACCESSIBLE`
- `TARGET_SELECTION_REQUIRED`

Renamed and superseded candidates return their current identity only when
lineage resolution and metadata disclosure are both authorized. Stale source
health cannot be normalized into a current target.

### 7.4 Authorized ambiguity resolution

Ambiguity may be resolved only by an actor or rule referenced by a current
`JurisdictionTargetSelectionAuthority` record in the request's jurisdiction.
If that authority cannot be resolved, return `TARGET_SELECTION_REQUIRED`.

No ranking score, lexical match, repository proximity, singular request label,
recency, popularity, or model preference may become institutional selection.

```text
Discovery != Selection
Selection != Authorization
OneCandidateFound != CandidateSelected
TargetSelected != WriteAuthorized
```

## 8. Privacy and attachment-graph visibility [IHR-R09]

### 8.1 Visibility axes

```text
CONTENT_VISIBILITY
!= ATTACHMENT_VISIBILITY
!= TARGET_METADATA_VISIBILITY
!= SOURCE_METADATA_VISIBILITY
```

```text
CanReadNote != CanSeeAttachmentGraph
CanSeeAttachmentGraph != CanResolveTargetIdentity
CanReferencePrivateTarget != CanDisclosePrivateTarget
CanReadNote != CanExportNote
CanWriteNote != CanAttachNote
```

### 8.2 Redacted attachment state

`ATTACHMENT_EXISTS_TARGET_REDACTED` may be disclosed only when the governing
policy permits disclosure of the relationship's existence. Otherwise neither
the edge, its count, its target class, nor its redaction state is discoverable.

### 8.3 Sensitive-source metadata

Repository identity, path, commit, digest, author, jurisdiction, and policy
identifiers are independently protected metadata. Public contract custody does
not declassify private source metadata.

This successor binds its public predecessor by public commit and digest only.
It does not repeat the predecessor's private-source metadata. The existing v0.1
publication history is immutable under this gate; whether its prior metadata
disclosure was authorized and what response is required remains a Founder
privacy disposition, not a permission to rewrite history.

### 8.4 Secrets and cache propagation

Secrets are prohibited from durable Notepad custody. On post-admission secret
discovery, access and export fail closed, affected replicas/caches receive an
authorized redaction or erasure directive, and the secret itself must not be
copied into the incident record.

Mobile cache, export, mirror, and projection policies must carry invalidation
and deletion propagation behavior before those capabilities can conform.

## 9. Multi-Notepad replica and mirror law [IHR-R06]

### 9.1 Separate identities

```text
NOTE_LINEAGE_IDENTITY
!= NOTE_VERSION_IDENTITY
!= REPLICA_IDENTITY
!= MIRROR_IDENTITY
!= CUSTODY_SURFACE_IDENTITY
```

- `REPLICA_IDENTITY` identifies one custody realization of a specific Note
  version.
- `MIRROR_IDENTITY` identifies a governed synchronization agreement, not a Note
  and not a source authority.
- `SOURCE_VERSION` identifies the immutable Note version expected by a sync
  epoch.
- `SYNC_EPOCH` identifies one bounded synchronization assessment.

```text
Replica != Source
Mirror != SourceAuthority
SameBytes != SameReplica
Divergence != AutomaticMerge
```

### 9.2 Mirror creation

A mirror agreement must bind source replica, destination replica, Note version,
surface identities, visibility ceilings, synchronization rule, divergence rule,
source-loss behavior, and mirror authority.

Mirror creation cannot elevate source standing or destination authority.

### 9.3 Synchronization and divergence

Each sync emits a new `SYNC_EPOCH` record. Content or constitutive-provenance
change outside the agreement marks:

```text
DIVERGENCE_REQUIRES_ADJUDICATION
```

No auto-merge is allowed. Authorized dispositions are:

- restore a conforming replica from source;
- recognize a new Note version under the source lineage;
- recognize an explicit fork with new lineage;
- retain divergent bytes as quarantined non-Note material;
- terminate the mirror.

### 9.4 Source loss and replica promotion

Source loss does not automatically promote a replica. Promotion requires a
standing-bearing decision by authority governing the affected jurisdiction and
must preserve source-loss uncertainty and last verified sync epoch.

```text
SourceUnavailable != ReplicaAuthoritative
ReplicaAvailable != SourceStandingTransferred
```

### 9.5 Cross-reference loops

Mirror topology and contextual attachment topology are distinct. A mirror loop
cannot recursively create replicas. Synchronization tracks visited mirror and
replica identities and fails closed on repeated identity within one operation.

## 10. Erasure, retention, and history [IHR-R10]

### 10.1 Competing lifecycle modes

- `SUPERSEDE`: preserve prior record and add an explicit current successor.
- `REDACT`: preserve permitted metadata while withholding specified content.
- `TOMBSTONE`: preserve only the minimum legally permitted historical marker.
- `ERASE`: remove content, identity, relationship, or existence metadata as the
  governing rule requires.
- `LEGAL_HOLD`: suspend otherwise available deletion under established legal
  authority and scope.

```text
AppendOnlyByDefault != NeverErasable
HistoricalAddressability = CONDITIONAL_ON_GOVERNING_PRIVACY_AND_RETENTION_LAW
```

### 10.2 Authority and unresolved priority

Each lifecycle act requires authority, jurisdiction, subject, scope, reason,
time, and propagation obligations. When the controlling legal priority cannot
be resolved:

```text
ERASURE_AUTHORITY_REQUIRED
LEGAL_PRIORITY_UNRESOLVED
```

The contract does not invent legal priority. Further ordinary processing fails
closed while emergency security containment may proceed only under separately
established authority.

### 10.3 Propagation

An authorized erasure or redaction disposition must address known replicas,
mirrors, projections, exports, search indexes, backups, and mobile caches.
Unknown destinations remain explicitly unresolved; completion cannot be claimed
from deletion of one path.

Restore after erasure is prohibited unless the governing disposition and law
explicitly authorize restoration. Target erasure may require erasure of the
attachment relationship itself, not merely redaction of the target label.

## 11. T3/T5 independence repair [IHR-R11]

### 11.1 Context-note occurrence

T3 observes a contextual Note occurrence. It does not assert institutional
custody.

```text
T3 CONTEXT_NOTE = PRESENT
iff
ContextualNoteOccurrenceIdentifiable
AND NotepadSemanticClassKnown
AND SourceObservationSufficientToEstablishOccurrence
```

The occurrence identity may be a bounded session-local observation identity. It
does not need an admitted surface, durable path, content digest, Git custody,
institutional lineage, or T5 binding.

```text
ContextNoteOccurrenceIdentity != GovernedNoteLineageIdentity
MinimalOccurrenceBinding != InstitutionalCustodyBinding
T3 CONTEXT_NOTE != T5 CUSTODY_BINDING
TraceClass != DurabilityRank
```

### 11.2 Required independence cases

| Specimen | T3 | T5 | Result |
| --- | --- | --- | --- |
| identifiable ephemeral contextual Note, no custody binding | PRESENT | ABSENT | VALID |
| admitted, custody-bound contextual Note | PRESENT | PRESENT | VALID |
| alleged Note with insufficient source observation | UNKNOWN | ABSENT | VALID |
| custody-bound non-Note governance artifact | ABSENT | PRESENT | VALID |

Neither axis is inferred from the other.

## 12. Trace-obligation matrix [IHR-R12]

Data minimization is the default. A Note is created or retained only for a
declared contextual purpose under applicable privacy and retention law.

| Work class | Required durable trace | Notepad disposition |
| --- | --- | --- |
| consequential mutation | execution, mutation, or evidence record REQUIRED | NOT_REQUIRED by default; PERMITTED for otherwise missing context |
| standing-bearing decision | decision record REQUIRED | NOT_REQUIRED; supplementary context PERMITTED |
| unresolved governed obligation | obligation or handoff record REQUIRED | REQUIRED only when governing action contract expressly selects T3; otherwise PERMITTED |
| handoff with obligation transfer | handoff/transport trace REQUIRED | PERMITTED supplement; cannot replace transport or admission |
| temporary computation | NOT_REQUIRED | NOT_REQUIRED; PROHIBITED when no retention purpose exists |
| debugging | contextual | PERMITTED; REQUIRED only for an unresolved consequential handoff selected by contract |
| ordinary brainstorming | NOT_REQUIRED | PERMITTED on an authorized surface; institutional custody not presumed |
| private scratch cognition | NOT_REQUIRED | PROHIBITED from institutional custody absent explicit purpose, consent, and private policy |
| secret-bearing material | redacted incident reference only where required | PROHIBITED |
| Founder informal context | NOT_REQUIRED solely by provenance | PERMITTED when explicitly selected and lawfully custodied |

```text
DurableTraceRequired != NotepadRequired
CanPreserve != ShouldPreserve
TraceVolume != InstitutionalProgress
```

## 13. Session-death recovery [IHR-R13]

### 13.1 Degraded state

When a consequential act occurs but its required trace is incomplete because a
session or runtime dies:

```text
MutationOccurred != TraceCompleted
LeaseEnded != TraceRecovered
institutional_state = TRACE_INCOMPLETE_DEGRADED
```

The physical occurrence is not erased. Its institutional conclusions, further
authority, completion standing, and dependent transitions fail closed until
recovery or authorized abandonment.

### 13.2 Detection

Detection may arise from a pre-existing lease journal, execution witness,
mutation record, event journal, run record, commit, evidence queue, or observed
state change lacking its required completion trace.

Detection does not require Notepad.

### 13.3 Recovery authority and sources

Recovery authority derives from the governing action jurisdiction, never from
the interrupted Note or runtime. Reconstruction may use immutable execution
witnesses, commits, run records, event journals, source state, recovery packets,
and independently attributable observations.

Another SELF may reconstruct observed effects and unresolved obligations. It
may not fabricate intent, authorship, command provenance, or authorization.

### 13.4 Recovery dispositions

- `TRACE_RECOVERED`: required trace reconstructed with sufficient provenance.
- `TRACE_PARTIALLY_RECOVERED`: bounded facts established; unresolved fields
  remain explicit and dependent transitions remain blocked where material.
- `TRACE_ABANDONED_BY_AUTHORITY`: recovery closed without claiming missing
  facts; consequences follow governing law.
- `TRACE_RECOVERY_UNRESOLVED`: no sufficient reconstruction or authority.

Recovery emits its own record through a pre-existing recovery-capable carrier.
It must not require the missing Note or a new trace mechanism whose existence
depends on successful completion of the failed trace.

If the recovery carrier also fails, the state remains
`TRACE_RECOVERY_UNRESOLVED`; no recursively generated carrier or success claim
is permitted.

```text
RecoveryCarrier != NotepadNecessarily
TraceFailure != RecursiveNotepadRequirement
```

## 14. Authority and source-truth firewall [IHR-R04, IHR-R07]

Notepad may capture, preserve, attach, cross-reference, flag potential conflict,
and support later review. It may not execute instructions, mutate source
objects, complete work, alter standing, grant authority, ratify doctrine,
rewrite evidence, change priority, open gates, revive leases, mint SELF identity,
or choose its own governing policy.

```text
ImperativeTextInNote != ExecutableInstruction
QuotedAuthority != CurrentAuthority
NoteAttachment != MutationLease
NoteConflict != SourceTruthMutation
FreshNote != FreshReality
NoteAboutMovement != MovementWitness
AttachedContext != MovementClaim
```

Any institutional consequence requires a separate lawful input-admission and
decision transition under the target system's authority.

## 15. Contract governance and host law [IHR-R17]

### 15.1 Custody separation

```text
RUORAHostsContract != RUORAOwnsAllNotepads
ContractCustody != ImplementationCustody
ContractConformance != InstitutionalSubordination
```

RUORA carries candidate bytes and lineage. This artifact grants RUORA no
automatic ratification, amendment, registry, surface-admission, or local Note
authority.

### 15.2 Contract authority

Ratification and amendment require explicit standing-bearing source records
naming `ContractRatificationAuthority` and `ContractAmendmentAuthority`, their
jurisdiction, scope, validity, and amendment procedure. Until resolved, this
candidate remains unratified and cannot self-promote.

### 15.3 Version adoption

Each jurisdiction may adopt, reject, defer, suspend, or supersede a contract
version through its own authorized decision. Publication or conformance does not
force adoption.

```text
ContractPublished != ContractAdopted
OneJurisdictionAdopts != AllJurisdictionsAdopt
NonAdoption != ContractViolation
```

### 15.4 Mandatory conformance core

The mandatory core consists of:

- NOTE, proposition, attachment, target, and custody identity separation;
- zero implicit authority, standing, evidence, and control effect;
- proposition-level safe fallback;
- privacy-safe discovery and graph visibility;
- T3/T5 independence;
- data-minimized trace obligations;
- erasure and retention policy resolution;
- finite traversal and no authority propagation through references;
- explicit version, extension, and jurisdiction reporting.

Local extensions may add stricter privacy, retention, identity, or workflow
constraints. They may not weaken the mandatory core or redefine a core failure
as success.

Unknown contract versions, unknown extensions affecting the core, or
incompatible extensions return `CONFORMANCE_NOT_EVALUABLE` or
`NONCONFORMANT`; they cannot be ignored.

### 15.5 Deprecation and supersession

Contract versions remain historically addressable where lawful. A superseding
version does not silently update jurisdictional adoption. Deprecation must state
effective time, affected versions, migration expectation, compatibility, and
authority. Local implementations retain sovereignty to remain unadopted, cease
Notepad operation, or adopt a lawful version.

## 16. Self-reference and cycle law [IHR-R20]

### 16.1 Classification

| Relation shape | Disposition | Law |
| --- | --- | --- |
| NOTE -> distinct NOTE | ALLOWED_BOUNDED | contextual relation only; finite traversal |
| NOTE -> exact self | PROHIBITED by default | dedicated reflexive relation would require future authority |
| NOTE -> OWN_ATTACHMENT | PROHIBITED | prevents construction and containment recursion |
| NOTE -> NOTEPAD_SURFACE | ALLOWED_BOUNDED | no surface authority or self-admission |
| NOTE -> CONTRACT | ALLOWED_BOUNDED | critique/context only; no amendment or ratification |
| NOTE -> CYCLIC_REFERENCE_GRAPH | ALLOWED_BOUNDED | cycle visible; traversal terminates |

### 16.2 Finite traversal

Every graph traversal must carry:

```yaml
TraversalContext:
  visited_identity_set: []
  current_depth:
  max_depth:
  cycle_detected:
```

`max_depth` must be finite and declared before traversal. Encountering an
already visited identity sets `cycle_detected = true`, reports the bounded edge,
and stops expansion along that path. Missing limits fail closed.

```text
ReferenceCycle != AuthorityCycle
SelfReference != SelfRatification
CyclicContext != InfiniteTraversal
```

No reference edge or traversal order may create authority, standing, selection
priority, dependency, execution, ownership, or conformance.

## 17. SELF-specific and cross-reality boundaries [IHR-R14, R15, R16]

```text
ReadableContext != AdoptedProtocol
ClaudeSELFBoot != CodexSELFBoot
ContextTransfer != ProtocolAdoption
NOTEPAD != ACTIMANIRUN
NOTEPAD != SELFIR
PotentialDependency != CurrentBlockingDependency
```

`SELFIR_DEPENDENCY_DETECTED` applies only to a future transition that represents
or transmutes NOTE or ContextAttachment objects. Notepad remains
representation-neutral. SELFIR would own representation and conservation law;
this contract does not define it.

ACTIMANIRUN may consume or route Note context only after a separate integration
gate establishes the exact input, authority, standing, and failure behavior.
This contract itself grants no contradiction-routing permission.

## 18. Substrate neutrality [IHR-R19]

Foundational semantics are identity, provenance, proposition attribution,
attachment, jurisdiction, privacy, retention, trace independence, finite
traversal, and zero implicit consequence.

GitHub, Markdown, paths, branches, commits, blobs, SHA-256, mobile caches, and
current runtimes are custody mechanisms. They are not Notepad ontology.

```text
SourceOrPathBound
```

is replaced at the foundational layer by:

```text
ResolvableSourceAddressOrObservationBinding
```

whose realization is substrate-specific.

## 19. Repair matrix

| Review chamber | v0.2 disposition | Repair location |
| --- | --- | --- |
| IHR-R01 root ontology | REPAIRED | section 2 |
| IHR-R02 NOTE identity | REPAIRED | sections 3-4 |
| IHR-R03 attachment vocabulary | REPAIRED | section 6 |
| IHR-R04 control flow | SURVIVOR_RETAINED | sections 1 and 14 |
| IHR-R05 target resolution | REPAIRED | section 7 |
| IHR-R06 multi-Notepad | REPAIRED | section 9 |
| IHR-R07 source truth | SURVIVOR_RETAINED | section 14 |
| IHR-R08 proposition standing | REPAIRED | section 5 |
| IHR-R09 privacy/access | REPAIRED_SEMANTICALLY | sections 7-8 |
| IHR-R10 deletion/history | REPAIRED_WITH_JURISDICTIONAL_PRIORITY_EXPLICITLY_UNRESOLVED | section 10 |
| IHR-R11 T3 independence | REPAIRED | section 11 |
| IHR-R12 trace obligation | REPAIRED | section 12 |
| IHR-R13 session death | REPAIRED | section 13 |
| IHR-R14 cross-SELF | SURVIVOR_RETAINED | section 17 |
| IHR-R15 SELFIR | DEPENDENCY_RECORDED_NOT_ACTIVATED | section 17 |
| IHR-R16 ACTIMANIRUN | SURVIVOR_CLARIFIED | sections 14 and 17 |
| IHR-R17 host governance | REPAIRED | section 15 |
| IHR-R18 publication | SURVIVOR_RETAINED | sections 0, 1, and 15 |
| IHR-R19 survivability | SURVIVOR_CLARIFIED | section 18 |
| IHR-R20 self-reference | REPAIRED | section 16 |

## 20. Required falsification traces

### F-01: T3 independent from T5

An observed, identifiable session-local contextual Note has no durable custody.
Result: `T3=PRESENT`, `T5=ABSENT`. No contradiction.

### F-02: custody does not confer proposition truth

A committed, published Note contains the claim `SELFPI is compromised` but no
ClaimAtom assessment. Result: record custody is established; proposition is
`ATTRIBUTED_UNASSESSED_CONTEXT` and cannot drive action.

### F-03: private attachment metadata does not leak

A public Note references a private target whose existence is non-disclosable.
Internal policy result may be hidden; requester receives `TARGET_UNRESOLVED`
with no count, type, redaction marker, path, or jurisdiction leak.

### F-04: session death recovers without recursion

A mutation witness exists but the session dies before the required run record.
State becomes `TRACE_INCOMPLETE_DEGRADED`; recovery uses the execution witness
and pre-existing event journal. No Note is required.

### F-05: self-reference terminates

Note A references Note B and B references A. Traversal marks A visited, then B,
detects A at the second edge, sets `cycle_detected`, and stops that path within a
finite declared depth. No standing or priority changes.

### F-06: contradiction relation does not claim truth

A Note flags a potential contradiction with an OMR assertion. The attachment
is `FLAGS_POTENTIAL_CONTRADICTION_WITH`; no contradiction standing exists until
a separate authorized evaluation.

### F-07: conformance without jurisdictional surrender

A local surface passes the mandatory core and is admitted by its local
jurisdiction. It retains implementation, content, access, and retention custody.
RUORA obtains no local authority.

### F-08: discovery cannot expose a private candidate

Resolver finds one private candidate but requester lacks metadata-disclosure
authority. Visible output is indistinguishable from scoped unresolved state;
selection and write remain unavailable.

### F-09: lawful erasure does not contradict history

Governing privacy law requires erasure of content and relationship metadata.
Authorized `ERASE` removes both and propagates directives. Historical
addressability is not claimed; unknown replicas remain explicit.

### F-10: publication does not imply readiness

This v0.2 candidate may be committed and remotely published while standing
remains `UNRATIFIED`, implementation safety remains false, and NOTEPAD-001
remains unauthorized.

## 21. Unresolved Founder decisions

1. Name contract ratification and amendment authority.
2. Decide whether RUORA remains physical custodian only or receives a bounded
   governance role through a separate standing-bearing act.
3. Select the exact identity grammar and canonicalization method for lineage,
   version, content, replica, mirror, attachment, and ClaimAtom identities.
4. Close or leave extensible proposition, relation-purpose, lifecycle, and
   failure-state vocabularies.
5. Name surface-conformance assessors, admission authorities, target-selection
   authorities, and metadata-disclosure authorities per jurisdiction.
6. Adjudicate whether v0.1's historical private-source metadata disclosure was
   authorized and what remediation, notification, or retention response applies.
7. Establish jurisdiction-specific privacy, erasure, legal-hold, backup, cache,
   export, and retention priority.
8. Select default finite traversal limits and any future authorized reflexive
   relation.
9. Select the pre-existing recovery-capable carriers for each mutation class.
10. Determine whether and when a future transition creates an actual SELFIR,
    ACTIMANIRUN, INSELFACTION, DATASELF, or other integration dependency.

## 22. Repair completion and next standing

All blocking findings are addressed at the semantic-contract level in this
successor. The historical v0.1 metadata-disclosure response and jurisdictional
legal priorities remain explicit Founder dispositions because this gate cannot
rewrite history or invent law.

```yaml
repair_status: COMPLETE_FOR_NEW_INDEPENDENT_REVIEW
ratification_status: NOT_AUTHORIZED
implementation_safety: FALSE
NOTEPAD_001: NOT_AUTHORIZED
eligible_for_new_independent_hostile_review: true
```

Eligibility for review is not a pass verdict. A new independent reviewer must
attack these exact bytes and may return `CHANGES_REQUIRED` again.

STOP. No ratification, implementation, merge, PR, default-branch mutation, or
cross-reality integration is authorized by this successor.
