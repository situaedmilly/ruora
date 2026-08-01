# TRACK K — HISTORICAL VALIDITY — DESIGN CANDIDATE

AUTHORIZATION: TRACK_K_HISTORICAL_VALIDITY_DESIGN_CANDIDATE (Human_TURN,
  this session, 2026-07-30)
CLASS: Design only
STATUS: PARKED
MUTATION AUTHORITY: NONE
RUNTIME AUTHORITY: NONE
RATIFICATION STATUS: NOT DISPOSITIONED
CLASSIFICATION: DOCTRINE_CANDIDATE / DESIGN_CANDIDATE — proposes a new
  validity layer and its outcome vocabulary; is not itself doctrine,
  constitutional law, or implementation until separately dispositioned.
SCOPE: DESIGN_ONLY — defines vocabulary and a design surface; builds no
  checker, alters no existing law, touches no ratified document.

DEPENDENCY: Reads and does not modify `doctrine/self_axiom.md`,
  `doctrine/ourself_master_command.md`,
  `GATE-5-HYPERBOLIC-IMPLEMENTATION-CONTRACT.md`,
  `LINEAGE-DEFECT-PATTERN-DEFINITION.md`,
  `BCP-000001-PERSISTENCE-ENGINEERING-WITNESS.md`,
  `IMPLEMENTATION-TRACK-COORDINATION.md`, `GOV-LINEAGE-001-...md`, and
  `workflow/07_LAUNCH_ROADMAP.md`.

────────────────────────────────────────
0. WHY THIS DOCUMENT EXISTS, AND WHY IT SITS IN TRACK K
────────────────────────────────────────
Track K (Kernel/Control-Plane) is owned procedurally by
`07_LAUNCH_ROADMAP.md`, evidentiary-anchored by
`LIMITED_SELFLAUNCH_OPERATING_BOUNDARY.md`. Until this document, every
Track K artifact has been a roadmap item or an Implementation-class gate
attempt (`BCP-000001-PERSISTENCE-ENGINEERING-WITNESS.md`, GATE CLASS:
IMPLEMENTATION, refused pre-mutation). Track K has never produced a
Design-stage artifact of its own.

This document is that first Design-stage artifact. It does not import
Track C's lifecycle wholesale, and it does not merge the two tracks —
`IMPLEMENTATION-TRACK-COORDINATION.md` §4 found their substantive
dependency chains fully disjoint, and nothing here changes that finding.
What it borrows is narrower: the *documentation pattern* Track C
established (a parked, undispositioned, design-only candidate-corpus
document, distinct from an engineering witness) — a pattern that
belongs to the shared procedural layer per `IMPLEMENTATION-TRACK-
COORDINATION.md` §2 ("[the workflow lifecycle] ... Neither track owns
that procedural layer; both merely operate under it"), not to Track C
specifically.

This document introduces no gate number in either the `SL-00N` scheme
(Track K's own) or the `GATE-N`/`WORKFLOW-00N` schemes (Track C's,
already found to collide with each other in
`IMPLEMENTATION-TRACK-COORDINATION.md` §5). It is a standalone-named
artifact, the same class as `GOV-LINEAGE-001` and
`LINEAGE-DEFECT-PATTERN-DEFINITION.md` — not a numbered roadmap item. It
does not edit, and is not itself, `07_LAUNCH_ROADMAP.md`'s open-work
list.

────────────────────────────────────────
1. MISSION
────────────────────────────────────────
Define a reusable, machine-checkable validity layer answering:

    Does a present claim remain truthful when evaluated against the
    complete available lineage of the system?

────────────────────────────────────────
2. RELATIONSHIP TO EXISTING LAW — NOT REDISCOVERY
────────────────────────────────────────
Three prior instruments already occupy adjacent ground. This document
does not restate them; it locates the gap between them.

**a. `doctrine/self_axiom.md` / Reality Reconciliation Law.** States the
general law this document sharpens for one recurring case: *"No evidence
without memory"*; *"If memory says one thing and runtime says another,
freeze mutation and reconcile."* Historical Validity is a named,
procedural instance of that law, applied specifically to claims that
assert continuity with a lineage.

**b. `LINEAGE-DEFECT-PATTERN-DEFINITION.md`.** Defines Lineage Defect:
*"A required institutional artifact exists only in transient
conversational memory and cannot be reconstructed from repository state
alone."* This is adjacent but distinct. Lineage Defect is about an
artifact that was **never captured** to disk. Historical Validity is
about a claim that **has been captured** — cryptographically intact,
procedurally admitted, even individually honest — and asks whether it
still coheres with everything else already on record. A Lineage Defect,
once corrected (per that document's own remedy — a disclosed-fidelity
transcription), becomes exactly the kind of artifact Historical Validity
would then check going forward. The same document's three-artifact-class
table (Engineering Evidence / Founder Law / Lineage Record) is also
directly relevant: a Lineage Record's own truth claim is "this is the
institution's first durable reconstruction of the original," never "this
is the original" — Historical Validity is the check that would hold that
specific, narrower claim to account against the rest of the record.

**c. `GATE-5-HYPERBOLIC-IMPLEMENTATION-CONTRACT.md` §5, Evidence
Emission.** Already formalizes an epistemic pipeline: *artifact presence
→ interpretation validity → referent validity → temporal index*, with
`PROPOSITION_INFLATION` as the named failure when an artifact's claim
outruns what it can support. That pipeline is **local**: it checks
whether one artifact honestly supports its own proposition. Historical
Validity is **global**: it checks whether that proposition, once
locally honest, still agrees with the complete recorded lineage around
it. A claim can pass GATE-5 §5 in full and still be historically false —
see §3 below.

Historical Validity is not proposed as a replacement for any of the
above. It is the layer none of the three currently occupy.

────────────────────────────────────────
3. REQUIRED INVARIANT
────────────────────────────────────────
    Local truth does not establish historical truth.

An artifact may be internally honest and cryptographically intact while
still creating a false global history. Worked example, per this
document's own authorization:

    artifact genuinely exists
    + artifact accurately describes its own contents
    + artifact falsely claims continuity with an absent predecessor
    = historically invalid

No implementation of a check for this invariant exists anywhere in this
corpus as of this document.

────────────────────────────────────────
4. REQUIRED CANDIDATE SCOPE
────────────────────────────────────────
Design surface only — each item below names the question a future
binding/implementation gate must answer, not the answer itself.

- **Canonical inputs.** A checkable unit must be: the claim under test; its
  stated predecessor/successor references (if any); and the bounded set
  of accessible history it is checked against. What "complete available
  lineage" resolves to — the whole repository, or a designated store
  such as `runtime/agentbridge/events.jsonl` plus the candidate-corpus/
  ratified/ directories — is not fixed here (see §8).

- **Lineage traversal rules.** How a check walks backward and/or forward
  from a claim through its stated references; what terminates a
  traversal (a declared genesis, a declared boundary, or an unresolved
  referent); what happens when a reference points outside the accessible
  store.

- **Referent-resolution rules.** How a stated predecessor (e.g. "BCP-
  000001") resolves to an actual artifact — by identifier, by hash, by
  content address — and what distinguishes a resolved from an
  unresolved referent.

- **Temporal ordering.** How lawful precedence is established — via
  timestamp, hash-chain position, or event sequence number — and the
  distinction between a claimed order and a provable one.

- **Predecessor and successor consistency.** Whether a claim's stated
  predecessor's own content actually supports what the claim asserts
  about it — not merely that a predecessor exists, but that it says what
  the claim says it says.

- **Orphan detection.** Identifying artifacts that assert continuity with
  no discoverable predecessor, or that claim ongoing institutional
  relevance but are referenced by nothing after them.

- **Contradiction detection.** Identifying two or more discoverable
  artifacts making mutually exclusive claims about the same referent.

- **Replacement and supersession semantics.** How a later artifact may
  lawfully supersede an earlier one. Supersession must be its own
  lineage event, never a deletion — a `SUPERSEDED` verdict means "no
  longer authoritative," not "erased."

- **Declared gaps.** A gap already disclosed at the time it was found
  (e.g. BCP-000001's HOLD) is not the same defect class as a gap no one
  has yet noticed. The design must distinguish disclosed uncertainty
  from silent, undetected gaps.

- **Irrecoverable lineage.** What a check does when resolving a referent
  is determined, not merely currently unresolved but *permanently*
  unresolvable (source destroyed, never captured, refusal already
  recorded under `LINEAGE-DEFECT-PATTERN-DEFINITION.md`'s remedy) — must
  not force a false resolution to reach a tidy verdict.

- **Acceptable terminal outcomes.** A check must always halt at exactly
  one outcome from §5, never an ambiguous or partial state — the same
  "no automatic retry-and-suppress" discipline `GATE-5` §6 already
  requires of chamber stages.

- **Evidence requirements.** Every verdict must carry an inspectable
  trail of which lineage entries were traversed and how each resolved.
  A verdict asserted without a re-derivable trail is itself epistemically
  invalid by `GATE-5` §5's own standard — Historical Validity cannot
  exempt itself from the local-honesty layer it sits above.

- **Deterministic re-derivation from disk.** Same rule as `GATE-3` §3 and
  `GATE-5`: a verdict must be independently re-computable by a fresh
  process reading only the same disk state, never trusted from a prior
  run's claim.

────────────────────────────────────────
5. CANDIDATE OUTCOME VOCABULARY
────────────────────────────────────────
Names only. None ratified. None implemented. None binding on any
runtime, gate, or future document until a separate disposition adopts
them.

| Outcome | Candidate meaning |
|---|---|
| `HISTORICALLY_VALID` | The claim and its stated lineage references are fully consistent with everything currently discoverable in the accessible history store. |
| `HISTORICALLY_INVALID` | The claim is locally intact but demonstrably contradicts, or falsely asserts continuity with, something else in the recorded lineage. |
| `LINEAGE_GAP` | A referenced predecessor/successor cannot currently be located, but is not yet determined to be permanently unresolvable. |
| `LINEAGE_CONFLICT` | Two or more discoverable artifacts make mutually exclusive claims about the same referent. |
| `ORPHANED_CLAIM` | An artifact asserts continuity with no discoverable predecessor, and/or is never referenced by anything after it despite claiming ongoing relevance. |
| `SUPERSEDED` | A claim once (or once-would-have-been) valid, lawfully replaced by a later authoritative artifact; remains on record, no longer current. |
| `UNVERIFIABLE` | Resolution of a referent has been determined, by explicit disclosure, to be permanently unresolvable — the correct candidate outcome for a case like BCP-000001's absent content. |
| `INSUFFICIENT_EVIDENCE` | The check itself was not carried to completion, or the evidence needed to evaluate the claim was never gathered — a statement about the check's own incompleteness, not the lineage's. |

Open edge, disclosed rather than resolved: the boundary between
`LINEAGE_GAP`, `UNVERIFIABLE`, and `INSUFFICIENT_EVIDENCE` needs firming
up at binding stage — this document names the distinction it intends
(currently-missing vs. permanently-missing vs. check-incomplete) without
yet specifying the exact rule that decides which applies in a given
case.

────────────────────────────────────────
6. BCP-000001 — MOTIVATING CASE, NOT PROOF OF IMPLEMENTATION
────────────────────────────────────────
BCP-000001 motivates this document. It is not evidence that a Historical
Validity engine exists, and this document does not treat it as such.
Stated precisely, per `BCP-000001-PERSISTENCE-ENGINEERING-WITNESS.md`
(read in full, unmodified by this document):

- The persistence mechanism existed: `runtime/agentbridge/` already
  holds a mature evidence-store convention; a `baselines/` category was
  identified by direct analogy as where a persisted BCP-000001 would
  live.
- The baseline content was not recoverable: every file in the corpus
  naming BCP-000001 was read in full; none defines what the baseline
  actually asserted (state captured, timestamp, authorizing party,
  hash).
- Fabrication was refused: two possible mechanisms for "persisting"
  unknown content were named and both rejected — inventing plausible
  content, and silently widening read-scope beyond the gate's own token
  alchemy.
- HOLD exposed the need for Historical Validity: the witness's own
  refusal is a hand-reasoned instance of exactly the check this document
  proposes to formalize — a claim ("BCP-000001 = X") that would have
  been locally tidy but historically false, refused before it could be
  written.
- No reusable historical-validity engine currently exists. The refusal
  in that witness was performed by direct human/session reasoning, once,
  for one case. Nothing in this corpus generalizes it.

This document does not reinterpret BCP-000001's witness, does not alter
its `STATUS: BLOCKED`, and does not resolve `07_LAUNCH_ROADMAP.md` open-
work item 1. That item remains exactly as open as it was before this
document existed.

────────────────────────────────────────
7. EXPLICITLY FORBIDDEN — NON-GOALS OF THIS DOCUMENT
────────────────────────────────────────
This document does not, and no reader may treat it as if it does:

- ratify Historical Validity as doctrine or constitutional law;
- alter any existing Founder Disposition;
- change, bind, or touch any Track C document or artifact;
- implement a checker, in any language, anywhere;
- modify any runtime code or any file under `runtime/agentbridge/`;
- reinterpret, rewrite, or change the status of BCP-000001's witness;
- invent, assume, or reconstruct any missing lineage content;
- assign execution, mutation, or runtime authority to anything;
- claim that the five-layer validity model (cryptographic / procedural /
  constitutional / epistemic / historical), discussed in this session's
  conversation preceding this document, is already constitutional law —
  it is not; only this document's own narrow scope (Historical Validity
  as a named design candidate) is asserted here.

────────────────────────────────────────
8. OPEN DEPENDENCIES — NOT RESOLVED HERE
────────────────────────────────────────
1. Exact boundary of "complete available lineage" (§4, canonical
   inputs) — whole repository vs. a designated evidence store.
2. Reviewer/authority model for who may declare a verdict — parallel to
   Gate 3's own unresolved reviewer-count question, not resolved by
   analogy here.
3. Relationship to `COGNITIVE_PRESSURE` (Gate 3 §4) — whether historical-
   validity checking scales in depth the way chamber reasoning does, or
   is binary. Not decided by this document.
4. Whether Historical Validity remains Track-K-specific or becomes a
   shared procedural layer available to Track C and any future track —
   explicitly undecided; `IMPLEMENTATION-TRACK-COORDINATION.md`'s own
   "shared procedural law" category is the closest existing precedent
   for what that would mean, but adopting it is a future act.
5. Naming for any future binding or implementation-stage gate — this
   document deliberately claims no gate number in either existing
   scheme (§0).
6. Gate 3's own disposition remains open (`STATUS: PARKED`,
   undispositioned) — this document does not depend on Gate 3 for its
   own content, but any future attempt to route Historical Validity
   checking *through* the Hyperbolic Chamber (should §8 item 4 ever
   resolve toward "shared") would inherit that same open dependency
   `GATE-5` §9 item 1 already discloses.
7. `UNVERIFIABLE` (§5) collides with an existing use of the identical
   token in `workflow/02_SYNCHRONIZATION.md:66`, where it names a
   status value for whether an entire event-ledger scan's validity
   could be determined — related in spirit, not the same claim shape as
   a per-claim Historical Validity verdict. Found by the companion
   witness's post-write verification, not by this document's own
   drafting. Whether this is an acceptable overload, a term needing
   disambiguation (e.g. `HISTORICALLY_UNVERIFIABLE`), or a sign the two
   concepts should share one status vocabulary is not decided here.

────────────────────────────────────────
9. NEXT GATE (NOT THIS ONE)
────────────────────────────────────────
A future, separately authorized document would need to: resolve the
open dependencies in §8; produce a binding decision (Track-K-scoped or
shared, per §8 item 4); and only then become eligible for an
Implementation-stage gate, following the same "no stage implies the
next" discipline `04_GATE_EXECUTION.md` already applies everywhere else
in this corpus. None of that is performed, implied, or pre-authorized by
this document.
