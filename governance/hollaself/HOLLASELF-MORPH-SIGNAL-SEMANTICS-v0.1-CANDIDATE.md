# HOLLASELF MORPH Signal Semantics v0.1 Candidate

```yaml
artifact_class: SEMANTIC_CANDIDATE
subject: HOLLASELF_MORPH_SIGNAL_SEMANTICS
standing:
  - SEMANTIC_CANDIDATE
  - NONCANONICAL
  - NOT_RATIFIED
  - NOT_IMPLEMENTED
runtime_identity: CODEXMOBILESELF
created_at: 2026-08-17T10:00:55-0400
host: RUORA governance candidate surface
control_effect: NONE
ratification_effect: NONE
implementation_effect: NONE
publication_effect: NONE
```

## 1. Source Binding

This candidate binds the current MORPH reality input:

```text
path: /Users/millysituated/.codex/attachments/5ba3692c-fcdf-4609-8252-8b7d6e3eb635/pasted-text.txt
line_count: 445
sha256: 47415810723160f1ff3acd1bfee6e39894b596f6094b567a14f190922b640ffa
```

And the HOLLASELF abstraction-boundary input:

```text
path: /Users/millysituated/.codex/attachments/e2358aba-b5a6-4a9a-b9b1-4ef1fa9ce95a/pasted-text.txt
line_count: 326
sha256: 90d6f4231c5ead899eb6484248586f58989cdb8b142c1390cb5ce230841de111
```

And the OTHERSELF transmission-layer sideglitch:

```text
path: /Users/millysituated/.codex/attachments/b736e091-c4aa-4446-9842-4f27c33fb0fe/pasted-text.txt
line_count: 577
sha256: 9b46fbd8cecf3883fe90834c3c7dad815fbf815736dea46e8b49c1bd097836a2
sideglitch_record: governance/hollaself/sideglitches/OTHERSELF-MORPH-TRANSMISSION-LAYER-SIDEGLITCH-001.md
standing: Founder-supplied cross-session context; not independent evidence
```

Predecessor candidate:

```text
GOCHECKIT-COMPLETE-CONTEXT-AND-REFERENCE-SIGNAL-PROTOCOL-v0.1-CANDIDATE
commit: 78261e4c00e90b32ebbb4f94fb8bd935cf8bc5fc
standing: SEMANTIC_CANDIDATE / NONCANONICAL / NOT_RATIFIED / NOT_IMPLEMENTED
```

## 2. Prime Correction

The current GOCHECKIT candidate successfully separates `GOCHECKIT` from
`HOLLASELF`, but the new reality input sharpens the decomposition.

Corrected architecture:

```text
HOLLASELF = signal / speech act
HOLLASIG  = identity of a specific signal emission
NODEFIELD = intended receiving SELF-set
SUBJECT_REFS = typed references to source Reality identities
MORPH = invariant-preserving projection from source Reality into target form
GOCHECK = one possible treatment workflow
```

Non-collapse:

```text
HOLLASELF != GOCHECK
HOLLASELF != Transport
HOLLASELF != Artifact
HOLLASELF != Review
HOLLASELF != Authority
HOLLASIG != ArtifactID
HOLLASIG != SessionID
HOLLASIG != ManifestationID
NODEFIELD != DeliveryProof
NODEFIELD != ReceiptProof
NODEFIELD != Obligation
GOCHECK != HOLLASELF
```

## 3. MORPH Operator

Candidate pre-formal operator:

```text
MORPH(S, P, I) -> S'
```

Where:

```text
S  = source Reality or source Reality subgraph
P  = target projection/profile
I  = invariants that must survive
S' = morphed representation
```

For HOLLASELF:

```text
MORPH(
  RealitySubgraph,
  HollaSignalProfile,
  ReferenceIntegrity
) -> HOLLASELF_SIGNAL
```

MORPH is not immediately minted as a new SELF, engine, IR, or universal
mathematical primitive. It is first held as an operator verb.

```yaml
morph:
  source:
  target_form:
  invariant_contract:
  allowed_loss:
  prohibited_loss:
  authority:
  output:
  witness:
```

Completion law:

```text
MORPH_COMPLETED iff InvariantContractSatisfied
MORPH(S, P, I) -> S'
Verify_I(S, S') = PASS
```

Failure states:

```text
MORPH_LOSS_EXCEEDED
MORPH_IDENTITY_BROKEN
MORPH_RELATION_BROKEN
MORPH_PROVENANCE_BROKEN
MORPH_STANDING_ESCALATION
MORPH_AUTHORITY_VIOLATION
MORPH_TARGET_UNRESOLVED
```

PRESERVE-AS kernel:

```text
source
-> declare preservation contract
-> transform
-> verify preserved relations
-> emit target representation
```

A projection is not a lawful morph unless the declared preservation contract
passes verification.

## 4. HOLLASELF Morph Invariants

The HOLLASELF signal morph must preserve at minimum:

```text
identity
relation
provenance
standing
custody
authority_ceiling
targeting
subject_scope
context_sufficiency
```

Loss contract:

```text
LossyProjection != InvalidProjection
```

Some signal projections intentionally omit full source prose, redundant
formatting, or unrelated history. Lawfulness depends on the declared
`allowed_loss` and `prohibited_loss` contract, not on total losslessness.

Candidate loss boundary:

```yaml
invariant_contract:
  preserve:
    - identity
    - standing
    - authority
    - provenance
    - source references
  allowed_loss:
    - full prose
    - redundant formatting
    - unrelated history
  prohibited_loss:
    - subject identity
    - custody binding
    - unresolved status
    - authority ceiling
```

Core laws:

```text
Morph != Rename
Morph != Replace
Morph != Merge
Morph != DeleteIdentity
Morph != CompressByInformationLoss
MorphResult != SourceReality
```

The result is a projection of source Reality, not source Reality itself.

## 5. HOLLASIG Identity

`HOLLASIG` identifies a specific signal morph event.

Candidate shape:

```yaml
hollasig:
  id: HOL-...
  source_graph_digest:
  morph_profile: HOLLASELF_SIGNAL_v0.1
  projection_digest:
  emitted_at:
  emitting_self:
  nodefield:
  subject_refs:
  custody_ref:
  standing:
  context_sufficiency:
  intended_treatment:
```

Identity law:

```text
SameSubjectRefs != SameHOLLASIG
```

Two HOLLASELF emissions concerning the same artifact are distinct if emitted at
different times, under different nodefields, standing, treatment, source state,
custody, or morph profile.

## 6. NODEFIELD

`NODEFIELD` is the intended receiving SELF-set.

Candidate modes:

```text
TARGETED -> explicit SELF/node identities
ALL      -> every admissible receiver in governed scope
NULL     -> no receiver designated; signal exists without directed delivery
```

Laws:

```text
NODEFIELD != AuthorityGrant
NODEFIELD != DeliveryProof
NODEFIELD != ReceiptProof
NODEFIELD != Obligation
```

Targeting `CHATGPTSELF` or `ClaudeSELF` does not prove delivery, receipt,
inspection, review, or authorization.

## 7. SUBJECT_REFS

Every referenced identity inside a HOLLASELF signal must preserve its source
identity domain and declare its relation to the signal.

Forbidden:

```text
MAN-0042 -> HOL-0091
ART-00881 -> HOL-0091
GLITCH-0019 -> HOL-0091
```

Required:

```yaml
hollasig: HOL-0091
subject_refs:
  - type: manifestation
    id: MAN-0042
    relation: ABOUT
  - type: artifact
    id: sha256:...
    relation: MANIFESTED_AS
  - type: finding
    id: GLITCH-0019
    relation: REPORTS_FINDING
  - type: note
    id: NOTE-0044
    relation: CONTEXTUALIZED_BY
```

Law:

```text
HOLLASIG != SubjectID
HOLLASIG -> {ID_1, ID_2, ..., ID_n}
AttachedReference != IdentityReplacement
```

Without typed reference roles, HOLLASELF degrades into a bag of IDs.

## 8. GOCHECK Disposition

`GOCHECKIT` remains the historical proto-protocol candidate that discovered a
bundle of concerns:

```text
COMPLETE_CONTEXT_MANIFESTATION
-> CUSTODY
-> REFERENCE_PACKAGING
-> HOLLASELF
-> RECEIVER_RESOLUTION
-> GOCHECK
```

Current disposition:

```text
GOCHECKIT = historical / proto-protocol candidate
HOLLASELF = signal primitive / speech act
GOCHECK = requested treatment workflow
```

Do not collapse them:

```text
HOLLASELF may carry GOCHECK
GOCHECK may be initiated from HOLLASELF
Receiving HOLLASELF != Authorized to perform GOCHECK
```

## 9. Signal Chain

Candidate operational chain:

```text
REALITY
-> MORPH
-> HOLLASELF / HOLLASIG
-> NODEFIELD
-> REQUESTED_TREATMENT
-> RECEIVING_SELF_AUTHORITY_CHECK
-> ACCEPT | REFUSE | HOLD
-> TREATMENT_WORKFLOW
-> RESULT
-> possible next HOLLASELF
```

Recursive law:

```text
HOLLASELF_1 -> GOCHECK -> Result -> HOLLASELF_2
```

This recursion does not create automatic authority or progress.

## 9A. DATASELF / HOLLASELF / DIGESELF / INSELFACTION Boundary

The OTHERSELF sideglitch adds a distributed-institution separation:

```text
DATASELF = memory/event fabric
HOLLASELF = signal transmission
DIGESELF = cognition/metabolism
INSELFACTION = governed handoff/custody transport
GO_CHECK = requested inspection treatment
```

Non-collapse:

```text
HOLLASELF != DATASELF
HOLLASELF != DIGESELF
HOLLASELF != INSELFACTION
HOLLASELF != GO_CHECK
```

Candidate relation:

```text
DATASELF supplies source refs
-> MORPH
-> HOLLASELF
-> receiving SELF
-> GO_CHECK / REVIEW / other treatment
-> result
-> new DATASELF
```

This keeps HOLLASELF as signal transmission rather than memory, cognition,
transport substrate, or treatment execution.

## 10. Speech / Transport / Treatment Separation

The durable doctrine:

```text
SIGNAL
!=
TRANSPORT
!=
REQUEST
!=
RECEPTION
!=
TREATMENT
!=
RESULT
```

Mapped:

```text
HOLLASELF = SIGNAL
HOLLASIG = SIGNAL IDENTITY
NODEFIELD = INTENDED RECEIVER FIELD
SUBJECT_REFS = IDENTIFIED REALITY ENCLOSED BY REFERENCE
GOCHECK = ONE POSSIBLE TREATMENT WORKFLOW
```

## 11. Relation To Compression And Compilation

Distinguish:

```text
COMPRESS = reduce representation size
COMPILE  = translate one representation into a target representation under explicit semantics
MORPH    = change form while preserving a declared invariant relation to source
```

Therefore:

```text
Compression != Compilation != Morphogenesis
```

They may compose:

```text
REALITY_GRAPH
-> SELECT_RELEVANT_SUBGRAPH
-> MORPH
-> COMPILE_TO_HOLLASELF_SIGNAL_IR
-> COMPRESS_REPRESENTATION
-> HOLLASIG
```

## 12. Premathematical Holding Pattern

Do not prematurely identify MORPH with one mathematical substrate.

Possible later mathematical realizations include:

```text
graph homomorphism
category-theoretic morphism
functor
state transition
topological deformation
linear interpolation
canonicalization
serialization
compiler lowering
lossy/lossless coding
```

Current status:

```text
SELFPREMSELFMATICS_PRECISE_HOLD
```

SELFMATH may later adjudicate which mathematical realization fits each subject.

Foundation IR relation:

```text
MORPH may consume Foundation IR preservation contracts.
MORPH does not own Foundation IR.
HOLLASELF does not become Foundation IR.
```

Foundation IR can specify invariants a representation transformation must
preserve; MORPH applies such a preservation/loss contract to a concrete
projection.

## 13. 2126 Law

Durable law:

```text
FORM MAY CHANGE WHILE IDENTITY AND REQUIRED RELATIONS REMAIN ADDRESSABLE.
```

OTHERSELF sideglitch sharpening:

```text
FORM MAY CHANGE WHILE REQUIRED IDENTITY, RELATION, PROVENANCE, STANDING,
AND AUTHORITY DISTINCTIONS REMAIN ADDRESSABLE.
```

Inverse:

```text
A REPRESENTATION TRANSFORMATION THAT BREAKS A REQUIRED INVARIANT IS NOT
A VALID MORPH OF THAT REALITY.
```

Corollaries:

```text
Representation may mutate; identity must not be silently replaced.
Compression may reduce bytes; meaning must not be silently destroyed.
Compilation may change form; authority must not be silently widened.
Morph may transform Reality; lineage must remain reconstructible.
```

Chess analogy:

```text
CompactSignal != CompressedMeaningByDeletion
```

The signal is small because identity and structure remain addressable elsewhere.

## 14. Non-Claims

This candidate does not:

- ratify MORPH as a universal primitive;
- create MORPHSELF;
- create MORPHENGINE;
- create MORPHIR;
- alter GOCHECKIT;
- alter HOLLASELF published candidate;
- implement signal routing;
- create receipt tracking;
- authorize GOCHECK;
- ratify NODEFIELD vocabulary;
- ratify HOLLASIG syntax;
- propagate into INSELFACTION, SELFLOGIC, ACTIMANIRUN, or SELF Protocol.

## 15. Next Lawful Gate

```text
HOLLASELF-MORPH-SIGNAL-SEMANTICS-INDEPENDENT-HOSTILE-REVIEW-001
```

No review, repair, adoption, commit, push, or propagation is authorized by this
candidate.
