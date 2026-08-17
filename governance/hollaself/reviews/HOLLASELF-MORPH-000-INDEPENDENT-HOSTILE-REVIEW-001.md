# HOLLASELF/MORPH Independent Hostile Review 001

```yaml
artifact_class: INDEPENDENT_HOSTILE_REVIEW
review_session_id: REV-20260817T142144Z-HOLLASELF-MORPH-001
subject_commit: f8b112b940dc0038f65b4bfddfed8ea2d0666196
subject_candidate: governance/hollaself/HOLLASELF-MORPH-SIGNAL-SEMANTICS-v0.1-CANDIDATE.md
subject_sha256: 9746704cac9c1574dd6360a1affeaffddfbae5b3c8a7e758ccdbc180337b2226
runtime_identity: CODEXSELF / GPT-5 runtime projection
session_started_at: 2026-08-17T14:21:44Z
prior_authoring_participation: NONE
prior_subject_conclusions_loaded: NONE
final_verdict: CHANGES_REQUIRED
review_authority: ACTIVE
mutation_authority: REVIEW_CUSTODY_ONLY
repair_authority: NONE
ratification_authority: NONE
implementation_authority: NONE
publication_authority: NONE
hypedu_before_custody: 0
```

`AuthoringSession != ReviewerSession` is satisfied. No author-session conclusions
were used as verdicts.

## 1. Target integrity — SURVIVES

| Witness | Expected | Observed |
|---|---:|---:|
| HEAD | `f8b112b940dc0038f65b4bfddfed8ea2d0666196` | exact match |
| Parent | `78261e4c00e90b32ebbb4f94fb8bd935cf8bc5fc` | exact match |
| Candidate | 570 lines / 11,470 bytes / `9746704…b2226` | exact match |
| OTHERSELF sideglitch | 322 / 6,389 / `1778fe8…ec60` | exact match |
| Publication witness | 206 / 4,648 / `5f4fface…310be` | exact match |

The branch was one commit ahead of its configured GitHub tracking ref. No
unstaged, staged, or untracked changes were present.

## 2. Reviewer independence — SURVIVES

The review used:

- the three pinned HEAD blobs;
- the parent GOCHECKIT candidate and evidence;
- one directly named lineage record, `GLITCH-0017`;
- bounded searches for the asserted neighboring systems.

No mutation lease, repair authority, inherited verdict, or author-side
self-check was accepted as independent proof.

## 3. HOLLASELF necessity — CHANGES_REQUIRED

Classification:

```text
SPECIALIZED_SIGNAL_CLASS
```

The candidate establishes a useful specialization:

```text
addressable subject references
+ declared standing
+ intended receiver field
+ optional requested treatment
```

It does **not** establish that HOLLASELF is an irreducible primitive. The parent
already contains a `CONTEXT_SIGNAL`, and the current candidate supplies no
comparative countermodel showing why typed `SELFCOMMUNICATION` or another
existing signal/event envelope cannot express the same act.

Current defensible ceiling:

```text
HOLLASELF
=
candidate specialized inter-SELF signal class
```

Not yet defensible:

```text
HOLLASELF
=
new universal institutional speech primitive
```

## 4. HOLLASIG identity — CHANGES_REQUIRED

The candidate says HOLLASIG identifies a “specific signal morph event.” That
conflates two events:

```text
MorphEvent != EmissionOccurrence
```

A representation may be morphed once and emitted repeatedly. Conversely, a
failed morph may never emit.

Required identity model:

```text
HOLLASIG = identity of one emission occurrence
```

Unresolved and therefore blocking:

- creation identity;
- retry identity;
- replay identity;
- forward identity;
- supersession;
- cancellation;
- duplicate detection;
- producer-local counter collision;
- identity across migrated runtimes.

Likely lawful replay shape:

```text
new HOLLASIG
+ replay_of: prior HOLLASIG
```

This remains a repair candidate, not a ratified result.

## 5. NODEFIELD — CHANGES_REQUIRED

`TARGETED`, `ALL`, and `NULL` are not sufficiently typed.

`ALL` does not define:

- jurisdiction;
- admissible receiver class;
- present versus future membership;
- online versus offline membership;
- confidentiality eligibility;
- expansion time.

Therefore:

```text
ALL_SCOPE_UNRESOLVED
```

`NULL` collapses four different states:

```text
UNDIRECTED_PUBLICATION
RECEIVER_UNKNOWN
RECEIVER_INTENTIONALLY_ABSENT
BROADCAST_DISCOVERY
```

`TARGETED` also mixes SELF and node identities. Those are not interchangeable.

Surviving law:

```text
NODEFIELD
!= Delivery
!= Receipt
!= Attention
!= Obligation
!= AuthorityGrant
```

## 6. Subject-reference graph — CHANGES_REQUIRED

The typed-reference direction survives. `HOLLASIG != SubjectID` is explicitly
protected.

The current shape lacks:

- namespace or identity authority;
- immutable locator/version;
- relation direction;
- standing-at-emission;
- current standing distinction;
- disclosure classification;
- unresolved-reference state;
- per-reference custody;
- duplicate normalization;
- relation-vocabulary authority.

A bare `{type, id, relation}` cannot distinguish equal lexical IDs issued by
different namespaces.

Required minimum:

```yaml
subject_ref:
  identity_namespace:
  identity:
  relation:
  relation_direction:
  pinned_state:
  standing_at_emission:
  custody_refs:
  disclosure_class:
  resolution_state:
```

Deleted, private, forked, or subsequently promoted subjects must not
retroactively change what the emission claimed.

## 7. MORPH root semantics — CHANGES_REQUIRED

The constitutional insight survives:

```text
a form change is lawful only under an explicit preservation/loss contract
```

The operator does not yet survive as an independent operation.

Current `MORPH(S,P,I) -> S'` overloads:

- selection;
- transformation;
- projection;
- compilation;
- serialization;
- validation;
- loss adjudication.

The stronger decomposition is:

```text
T(S, P) -> S'
MORPH_VALID(T, S, S', I, L) iff Verify(I, L) = PASS
```

Under this model, MORPH is initially a **qualification/predicate over a
transformation**, not necessarily a separate universal opcode.

Standing remains:

```text
HOLLASELF_SEMANTIC_OPERATOR_CANDIDATE
```

## 8. Invariant contract — CHANGES_REQUIRED

The candidate lists useful invariant classes, but it does not define their
observable predicates.

Examples:

- “preserve identity” does not say whether addressability, equality, lineage,
  or namespace must survive;
- “preserve standing” conflicts with legitimate post-emission standing changes;
- “preserve custody” is unclear when custody becomes inaccessible;
- “preserve context sufficiency” cannot be proven merely by comparing two
  representations.

Each invariant requires:

```text
predicate
evidence source
evaluation time
failure class
permitted degradation
```

Authority should preserve an explicit **ceiling and jurisdictional basis**, not
an abstract authority value.

## 9. Loss semantics — CHANGES_REQUIRED

The core distinction survives:

```text
LossyProjection != InvalidProjection
```

The declared loss categories are not decidable. “Full prose,” “unrelated
history,” and “redundant formatting” may contain blockers, exceptions,
provenance, or scope restrictions.

Counterexample:

> A paragraph classified as “full prose” contains the only statement that
> ratification authority is absent.

Removing it satisfies the present vocabulary while laundering authority.

Required:

```text
DeclaredAllowedLoss
+ field-level loss map
+ relation-level loss map
+ proof that no prohibited proposition depended on omitted material
```

Therefore:

```text
UndeclaredLoss = MORPH_FAILURE
DeclaredButUnverifiableLoss = MORPH_FAILURE
```

## 10. MORPH / COMPRESS / COMPILE — CHANGES_REQUIRED

`COMPRESS` survives independently because its objective is representation-size
reduction.

`COMPILE` and current `MORPH` do not yet have a demonstrated independent
distinction. Both are described as semantics-constrained representation changes.

The proposed pipeline risks artificial duplication:

```text
Select -> Morph -> Compile
```

Better current model:

```text
Select source subgraph
-> Transform/compile into target representation
-> optionally compress encoding
-> verify preservation/loss contract
-> permit emission
```

MORPH may name the verified transformation relation, but recurrence evidence is
required before making it a separate execution stage.

## 11. Chess analogy — CHANGES_REQUIRED

`Nf3` is not independently resolvable without:

- a pinned board state;
- move number;
- side to move;
- rule set;
- legal-move context;
- notation convention.

The same notation can denote different move occurrences in different games.

Therefore:

```text
MoveNotation != MoveOccurrence
MoveOccurrence != BoardState
CompactNotation requires SharedPinnedContext
```

The analogy supports compact reference, but disproves self-sufficient
interpretation. HOLLASELF must bind resolvable state rather than assume a
synchronized global board.

## 12. Temporal model — CHANGES_REQUIRED

The candidate exposes only `emitted_at`. It requires at least:

```text
source_state_time
morph_time
emission_time
publication_time
```

Delivery, receipt, resolution, and inspection belong to separate downstream
evidence objects.

Required laws:

```text
EmissionTime != SourceRealityTime
FreshHOLLASELF != FreshSubjectReality
StandingAtEmission != StandingAtResolution
```

Without these, a fresh signal can launder stale subject reality.

## 13. Custody model — CHANGES_REQUIRED

A single opaque `custody_ref` is insufficient.

Required distinctions:

```text
SignalExists
!= SubjectResolvable
!= SubjectReadable
!= TreatmentAuthorized
```

The model must handle:

- multiple custody adapters;
- inaccessible custody;
- digest mismatch;
- mutable branch movement;
- lawful erasure;
- private targets;
- receivers lacking the named adapter;
- fallback custody without silently changing subject identity.

## 14. GOCHECK — CHANGES_REQUIRED

Current classification:

```text
receiver-local requested treatment workflow candidate
```

It is not yet shown to be an institution or protocol.

Required state separation:

```text
GOCHECK_REQUESTED
!= GOCHECK_ADMITTED
!= GOCHECK_AUTHORIZED
!= GOCHECK_EXECUTED
!= GOCHECK_RESULT_ACCEPTED
```

The candidate has an authority-check arrow, but not a typed state machine
defining who evaluates admission, under which jurisdiction, or how refusal is
recorded.

## 15. Speech acts — CHANGES_REQUIRED

The candidate alternates between describing HOLLASELF as a signal and as a
speech act. Those are different classification dimensions:

```text
SignalEnvelope != SpeechActType
```

A HOLLASELF envelope may carry:

```text
REPORT
REQUEST
QUESTION
PROPOSAL
WITNESS
```

`COMMAND`, `ADJUDICATION`, and `RATIFICATION` require stronger authority
bindings.

Required:

```text
LexicalForm != SpeechAct
ImperativeGrammar != Authority
```

Ownership of the shared speech-act vocabulary remains unresolved; the
HOLLASELF candidate must not silently claim it.

## 16. Recursion — CHANGES_REQUIRED

The candidate permits a result to produce another HOLLASELF but defines no
reference traversal law.

Required:

```text
visited_hollasigs
maximum_depth
maximum_expansion
cycle classification
```

Preserve:

```text
SignalCycle != AuthorityCycle
SignalReference != SignalAdoption
SelfReference != SelfAuthorization
```

## 17. Privacy — CHANGES_REQUIRED

The parent contains a general disclosure block, but the successor does not
attach disclosure law to NODEFIELD or each subject reference.

Required distinctions:

```text
CanSignalExistence != CanDiscloseSubjectMetadata
CanTargetReceiver != CanPubliclyDiscloseReceiver
CanReferenceSubject != CanRevealSubjectExistence
```

Until receiver eligibility, metadata disclosure, and public/targeted visibility
are explicit:

```text
UNIVERSAL_EMISSION_BLOCKED
```

## 18. Delivery and receipt — SURVIVES WITH REQUIRED SEPARATION

Separate objects are warranted:

```text
DeliveryAttempt
DeliveryWitness
Receipt
Acknowledgement
Refusal
```

They must not be forced into HOLLASIG.

```text
Emission != Delivery
Delivery != Receipt
Receipt != Acknowledgement
```

The candidate correctly avoids claiming delivery, but it needs stable relations
from those future objects back to the emission occurrence.

## 19. Replay — CHANGES_REQUIRED

No replay law exists.

A replay must not silently reuse the original occurrence identity.

Candidate repair model:

```yaml
new_hollasig:
  occurrence_kind: REPLAY
  replay_of: prior_hollasig
  emitted_at:
  emitter:
  nodefield:
```

Forwarding requires a separate `forward_of` relation because a forward changes
producer/custody lineage differently from replay.

## 20. Authority — CHANGES_REQUIRED

The high-level firewall survives:

```text
MORE_SIGNALING != MORE_AUTHORITY
```

The candidate correctly denies authority effects. However, enforceable authority
semantics are absent:

- jurisdiction is not a first-class field;
- sender provenance is not separated from authority basis;
- authority ceiling has no issuer or evaluation time;
- NODEFIELD admissibility is not jurisdiction-bound;
- requested treatment lacks an authorization decision reference.

Required:

```text
FounderProvenance != UniversalAuthority
SenderIdentity != AuthorityGrant
AuthorityAtEmission != AuthorityAtTreatment
```

## 21. Cross-SELF identity — CHANGES_REQUIRED

The current shape has `emitting_self` but fails to separate:

```text
SELFIdentity
RuntimeProjection
SessionIdentity
NodeIdentity
RoleIdentity
Jurisdiction
```

NODEFIELD explicitly allows “SELF/node identities,” recreating the collapse the
review was commissioned to prevent.

Every identity-bearing field needs a declared identity level and namespace.

## 22. Foreign-reality relations — UNRESOLVED

Current candidate relations remain hypotheses:

| Reality | Current defensible relation |
|---|---|
| DATASELF | possible source/event provider; not verified owner |
| DIGESELF | possible cognition consumer; not verified owner |
| INSELFACTION | related custody/handoff boundary; exact overlap unresolved |
| SELFCOMMUNICATION | likely shared signal/speech-act owner; corpus evidence absent |
| GOCHECKIT | established predecessor candidate |
| NOTEPAD | lineage/context surface, not signal authority |
| SELFIR/Foundation IR | possible invariant-contract supplier; no integration authority |
| ACTIMANIRUN | temporal resonance only; no imported jurisdiction |

No foreign system may be mutated or treated as integrated from these hypotheses.

## 23. 2126 substrate neutrality — CHANGES_REQUIRED

The conceptual nucleus survives removal of Git, GitHub, Markdown, SHA-256,
Claude, Codex, and ChatGPT:

```text
emission occurrence
receiver field
subject references
preservation contract
requested treatment
custody resolution
```

The concrete parent specimen remains Git-shaped. The successor improves
neutrality through `custody_ref`, but leaves the abstraction opaque.

A substrate-neutral contract must express capabilities:

```text
immutable subject resolution
integrity verification
read authorization
availability state
adapter identity
algorithm agility
```

SHA-256 may be one current integrity algorithm, not the ontology.

## 24. Kill-test matrix

| Kill test | Verdict | Reason |
|---|---|---|
| K1 HOLLASIG replaces subject identities | SURVIVES | Explicit typed-reference non-collapse |
| K2 NODEFIELD grants authority | SURVIVES | Explicitly denied |
| K3 ALL silently becomes universal broadcast | REJECTED | Governed scope is undefined |
| K4 MORPH permits undeclared loss | REJECTED | Loss categories are non-decidable |
| K5 MORPH changes authority standing | CHANGES_REQUIRED | Denied textually; verifier semantics absent |
| K6 Fresh signal launders stale Reality | REJECTED | No source-state time/freshness binding |
| K7 GOCHECK request auto-executes | CHANGES_REQUIRED | Authority check exists, state machine does not |
| K8 Signal cycle creates authority recursion | REJECTED | No cycle or traversal controls |
| K9 Private metadata leaks publicly | REJECTED | No per-reference/NODEFIELD disclosure contract |
| K10 Runtime projection mistaken for SELF | REJECTED | Identity levels are mixed |
| K11 Replay becomes original occurrence | REJECTED | Replay semantics absent |
| K12 MORPH promoted universally | SURVIVES | Explicit non-claim and standing ceiling |

Five mandatory kill tests fail outright. The candidate cannot pass.

## 25. Surviving laws

```text
HOLLASELF != HOLLASIG
HOLLASIG != SubjectIdentity
NODEFIELD != DeliveryProof
NODEFIELD != AuthorityGrant
Signal != Transport
Request != Authorization
Review != Ratification
LossyProjection != InvalidProjection
MorphResult != SourceReality
Custody != Truth
Publication != Ratification
MORE_SIGNALING != MORE_AUTHORITY
FreshHOLLASELF != FreshSubjectReality
RuntimeProjection != SELFIdentity
PressureDoesNotGrantStanding
```

## 26. Blocking findings

```text
HR-001 HOLLASIG_EVENT_COLLAPSE
Morph event and emission occurrence are conflated.

HR-002 NODEFIELD_SCOPE_UNDERDETERMINED
ALL, NULL, SELF, and node targeting lack distinct semantics.

HR-003 MORPH_OPERATOR_OVERLOAD
Transformation, compilation, projection, validation, and loss adjudication are collapsed.

HR-004 LOSS_CONTRACT_NONDECIDABLE
Allowed loss can remove load-bearing meaning without a detectable failure.

HR-005 TEMPORAL_FRESHNESS_GAP
No source-state time prevents stale-Reality laundering.

HR-006 RECURSION_AND_REPLAY_GAP
Cycles, replay, forwarding, supersession, and duplicate identity are undefined.

HR-007 PRIVACY_DISCLOSURE_GAP
Receiver targeting and subject-reference disclosure are not independently governed.

HR-008 CROSS_SELF_IDENTITY_COLLAPSE
SELF, runtime, session, node, role, and jurisdiction lack typed separation.

HR-009 PRIMITIVE_NECESSITY_UNPROVEN
HOLLASELF has not been falsified against existing communication/signal ownership.
```

## 27. Founder questions

1. Is HOLLASELF intended to identify an envelope class, a speech-act class, or
   the act of emission?
2. What exact governed population does `NODEFIELD=ALL` quantify over?
3. Should `NULL` mean undirected publication, deliberate absence, unknown target,
   or discovery broadcast?
4. Must HOLLASIG identify emission occurrence even when the same morph result is
   emitted repeatedly?
5. Is MORPH intended as an executable stage or as the validity relation applied
   to any transformation?
6. Which existing system owns shared speech-act typing?
7. Which identity level may NODEFIELD target: SELF, runtime projection, session,
   node, role, or an explicitly typed union?
8. May a public HOLLASELF reveal the existence of a private subject?
9. What authority decides whether omitted material is genuinely unrelated?
10. Is GOCHECK a request type, a receiver-local workflow, or a separately governed
    protocol candidate?

## 28. Final verdict

```text
CHANGES_REQUIRED
```

The signal architecture has a viable nucleus, but the current candidate cannot
block five mandatory failure classes and cannot yet justify HOLLASELF as an
irreducible primitive.

This verdict grants no repair, mutation, ratification, implementation,
publication, or integration authority.

```yaml
HYPEDU:
  current: 0
  pending: 1
  incremented: false
reason: Review computed in volatile session; no authorized custody act existed at review time.
```

## 29. Exact repair surface

If separately authorized, the minimum repair surface is the HOLLASELF/MORPH
candidate only:

1. Reclassify HOLLASELF provisionally as a specialized signal class.
2. Define HOLLASIG as emission-occurrence identity.
3. Add retry, replay, forward, supersession, cancellation, and duplication laws.
4. Replace ambiguous NODEFIELD modes with typed scope and identity-level semantics.
5. Add namespace, immutable state, disclosure, and resolution fields to subject
   references.
6. Recast MORPH as a preservation qualification over a transformation unless an
   independent operator distinction is demonstrated.
7. Define executable invariant predicates and field/relation-level loss maps.
8. Add source, morph, emission, and publication times.
9. Add recursion bounds and cycle classification.
10. Add privacy eligibility and metadata-disclosure gates.
11. Add GOCHECK admission/authorization/execution states.
12. Add explicit SELF/runtime/session/node/role/jurisdiction identities.
13. Add a lawful positive specimen and counterexamples for every surviving
    operation distinction.

Out of scope:

- sideglitch rewrite;
- parent GOCHECKIT rewrite;
- foreign-system mutation;
- compiler/runtime implementation;
- routing;
- publication;
- HOLLASIG allocation.

## 30. Next lawful gate only

```text
FOUNDER_DECISION:
AUTHORIZE_BOUNDED_HOLLASELF_MORPH_CANDIDATE_REPAIR_001
or
HOLD
```

At review-return time, no review artifact had been created and no files had been
edited, staged, committed, pushed, or published.

Review verification commands executed successfully:

```bash
git rev-parse HEAD
git rev-parse HEAD^
git status --short --branch
git diff-tree --no-commit-id --name-status -r HEAD
git show "HEAD:<path>" | wc -l
git cat-file -s "HEAD:<path>"
git show "HEAD:<path>" | shasum -a 256
git diff --stat
git diff --cached --stat
```

Review-return repository state was:

```text
HEAD: f8b112b940dc0038f65b4bfddfed8ea2d0666196
parent: 78261e4c00e90b32ebbb4f94fb8bd935cf8bc5fc
working tree mutation: NONE
index mutation: NONE
remote publication of HEAD: NOT PERFORMED
```

Custody of this review does not alter its verdict and does not grant repair
authority.

```text
ReviewCustody != RepairAuthority
HYPEDU1P != PASS
HYPEDU1P != VERIFIED
HYPEDU1P != RATIFIED
HYPEDU1P != CANONICAL
MORE_PRESSURE != MORE_AUTHORITY
```
