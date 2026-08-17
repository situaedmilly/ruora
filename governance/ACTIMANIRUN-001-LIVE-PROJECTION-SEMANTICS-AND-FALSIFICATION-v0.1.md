# ACTIMANIRUN-001 — LIVE PROJECTION SEMANTICS AND FALSIFICATION v0.1

```yaml
artifact_class: SEMANTIC_CLOSURE_AND_FALSIFICATION_RECORD
gate: ACTIMANIRUN-001
authorization_token: AUTHORIZE_ACTIMANIRUN_001_LIVE_PROJECTION_SEMANTICS_AND_FALSIFICATION_ONLY
authority_source: MYSELF (Founder disposition, 2026-08-17, relayed with Milasophahr commentary)
authored_by: CLAUDESELF (Claude Code session c23de3d6-1255-4dec-b130-d9eb8f625122)
created_at_utc: 2026-08-17T07:40:43Z
created_at_local: 2026-08-17T03:40:43-04:00
standing: >
  SEMANTIC_CANDIDATE_CLOSURE · FALSIFIED_AGAINST_SPECIMENS · NOT_IMPLEMENTED ·
  NOT_RATIFIED — closure of a semantic model is not ratification of law.
  RECORDED_CLOSURE != FOUNDER_RATIFICATION.
lineage:
  parent_gate: ACTIMANIRUN-000A
  parent_commit: 65e5f9dab179c890dbb502f6d7bb51bb3cd41234
  branch: governance/actimanirun-000-custody
  founding_artifact_sha256: ab75649afc4773c5a679c7396df076906ee608254cbf8c5b54f32d146c5d444b
  evidence_record_sha256: 9dbf36e8f364110112a90b22c03aac8a57fa42edeeb09baa9127ec23739cc2ec
  ratification_record_sha256: 6fdc15b5bb6dab64e369319bf24e1382dc5fe9af0a2fbe9730a61599d7426bc5
  historical_law: LaterRatification != OriginalAuthorship — no parent bytes mutated
lease:
  holder: CLAUDESELF session c23de3d6-1255-4dec-b130-d9eb8f625122
  subject: (GOVERNANCE-CANDIDATE:ACTIMANIRUN, gate ACTIMANIRUN-001)
  scope: creation of this artifact + its evidence record + their custody commit ONLY
  granted_by: Founder token above (fresh grant; the expired 000/000A leases were NOT revived)
  expires: at gate STOP; non-transferable; not inherited by successor sessions
  concurrent_front_note: >
    Codex estate session 01a00e62 was LIVE during this gate (rollout mtime
    2026-08-17T03:34:22-04:00, 43 conceptual ACTIMANIRUN references, ZERO
    references to this custody worktree). ParallelAnalysis != ParallelAuthority;
    no Codex contact issued.
authority_effect: NONE_UNLESS_SEPARATELY_RATIFIED
mutation_authority_of_this_artifact: NONE
evidence_record: governance/evidence/ACTIMANIRUN-001/SEMANTIC-GATE-EVIDENCE-RECORD-001.md
```

---

## §0 — PRIME NON-COLLAPSE LAWS (BINDING FRAME OF THIS GATE)

Ratified frame carried from D-000A-01:

```
InstitutionalState != MovementPulse != HoldContext != AttentionState != SourceHealth
```

Frozen for attack in this gate (and surviving it — see §16):

```
SourceEventTime != ObservationTime != AdmissionTime != EvaluationTime != InstitutionalTime
FreshRun != FreshSource
```

A projection compiled now from stale evidence is a fresh projection of stale
evidence. It must never masquerade as current source reality.

---

## §1 — 001A · MOVEMENTPULSE — FINAL DISPOSITION: **CLOSED, TRI-STATE**

### 1.1 Final vocabulary

```
WITNESSED_MOVING
NO_CURRENT_MOVEMENT_WITNESS
UNKNOWN(unknown_reason)
```

### 1.2 Closed semantics

**WITNESSED_MOVING** — emitted iff at least one MovementClaim (§8) with
standing `ESTABLISHED` exists whose `event_time` falls inside the evaluation
window of the applicable MovementCadenceContract (§4), derived from an
admitted, integrity-verified witness of an accepted movement event class.

**NO_CURRENT_MOVEMENT_WITNESS** — an existential negative over the admitted
evidence set: *no admissible, sufficiently-fresh movement witness currently
establishes movement.* It MUST NOT be read as inactive, blocked, abandoned,
failed, stale, drifting, or waiting. It carries one additional obligation,
closed in this gate:

```
SILENCE REQUIRES COVERAGE:
NO_CURRENT_MOVEMENT_WITNESS may be emitted only when admitted sources
whose declared coverage spans the accepted movement event classes were
OBSERVED inside the freshness requirement (observation_time witnessed).
Silence from an unobserved or uncovered channel is not evaluated silence.
```

Absence of witness is not witness of absence — but a lawful negative claim
still requires proof that someone looked.

**UNKNOWN(unknown_reason)** — evaluation preconditions failed. One enum value
with a mandatory typed reason (structure, not a fourth scalar):

```
unknown_reason ∈ { NO_ADMITTED_SOURCE_COVERAGE, TIME_SEMANTICS_UNRESOLVED,
                   IDENTITY_UNRESOLVED, ADMISSION_UNRESOLVED, WINDOW_UNRESOLVED }
```

### 1.3 Fourth-value attack — RESULT: **NO FOURTH VALUE**

Attacked candidates:

| Candidate 4th value | Verdict | Reason |
|---|---|---|
| `STALE_WITNESS` | REJECTED | staleness of the channel is SourceHealth (§6); a witness too old to satisfy freshness simply fails to establish → the tri-state already answers truthfully |
| `NOT_EVALUABLE` as separate from `UNKNOWN` | REJECTED | no surviving case where evaluation runs AND yields indeterminate: inadmissible witnesses are excluded at admission; contradictory admissible witnesses route to drift (§11), pulse evaluates over the surviving set. One value + typed reason suffices |
| `PARTIAL` | REJECTED | partial coverage either still yields an ESTABLISHED claim (→ WITNESSED_MOVING) or fails coverage (→ UNKNOWN:NO_ADMITTED_SOURCE_COVERAGE); no third truth-value exists between them |

Source staleness is represented entirely by SourceHealth; it stays out of
MovementPulse. A stale source with admissible cached witnesses still evaluates
(Specimen I); a source so stale that no admissible evidence survives its
evidence ceiling produces UNKNOWN(NO_ADMITTED_SOURCE_COVERAGE) — through the
coverage predicate, never through a health→pulse inference.

### 1.4 Required falsification — PASS

The pulse derivation function is, by construction:

```
pulse = f(admitted_movement_evidence_set, window, freshness_rule, coverage_proof)
```

HoldContext, AttentionState, Founder priority, and institutional lifecycle
labels are not inputs. Demonstrated mechanically across Specimens A–I (§15) —
no specimen required reading a prohibited axis to produce its pulse value.

---

## §2 — 001B · HOLDCONTEXT — FINAL DISPOSITION: **CLOSED**

### 2.1 Definition

HoldContext = the presently **declared** reason or lawful context explaining
why movement may be absent or intentionally suspended. Declared-plane only:
every non-NONE value requires a declaration act with provenance (who, on what
evidence) and a review/expiry condition. HoldContext is a property of the
manifestation, never of an observer.

### 2.2 Final vocabulary

```
NONE_DECLARED                — no hold is declared (a declaration-plane fact,
                               NOT a claim that no reason exists)
WAITING_FOUNDER(ref)         — movement awaits a named Founder act
WAITING_EXTERNAL(ref)        — movement awaits a named external party/event
WAITING_DEPENDENCY(ref)      — movement awaits another named estate object
                               (manifestation, gate, or MUTATION LEASE —
                               000 §5's LEASE_HELD_ELSEWHERE is narrowed in
                               here: a lease is an estate object)
LAWFUL_QUIET(contract_ref)   — the cadence contract declares silence lawful now
UNKNOWN                      — the declaration store could not be read
```

### 2.3 BLOCKED_CONTEXT adjudication — **REJECTED (duplication confirmed)**

The gate's question — does BLOCKED_CONTEXT improperly duplicate an existing
institutional BLOCKED status — is answered YES, three ways:

1. **Name collision:** BLOCKED is live institutional-status vocabulary (OSM
   board status set includes BLOCKED). A same-name hold value invites the
   prohibited laundering `InstitutionalClaim → HoldContext` — a stale board
   BLOCKED becoming a "declared" hold with no declarer.
2. **Decomposition:** every concrete blocked case names a blocker, and every
   nameable blocker is a Founder act, an external party, or an estate object —
   exactly WAITING_FOUNDER / WAITING_EXTERNAL / WAITING_DEPENDENCY.
3. **The residue is not a hold:** a "blocked" with no nameable ref is an
   undiagnosed condition — a drift/attention matter, not a declarable reason.
   Admitting it as a hold would let vagueness suspend silence clocks.

### 2.4 Laws (carried + closed)

```
ReasonForNoMovement != MovementObservation                     (D-000A-03)
HoldContext does not change MovementPulse unless an independent
  movement observation changes                                  (by construction: §1.4)
pulse=NO_CURRENT_MOVEMENT_WITNESS + hold=WAITING_EXTERNAL is a
  VALID, non-contradictory pair                                 (Specimen A)
Holds named in the contract's hold_exceptions suspend the silence
  clock (§4 pause_semantics); an expired unreviewed hold is itself
  a drift-evaluable fact                                        (§11 DEPENDENCY_DRIFT)
```

---

## §3 — 001C · ATTENTIONSTATE — DISPOSITION: **AXIS IRREDUCIBLE (re-proven) · VOCABULARY CLOSED AT 3+UNKNOWN**

### 3.1 Irreducibility

Re-affirmed from 000 §6 with this gate's specimens: attention diverges from
pulse in both directions (Specimen B: WITNESSED_MOVING + no attention due;
an escalated blocked item: no pulse + maximal attention), from institutional
state (24 board-ACTIVE vs a handful attended), from hold (a held item may be
foreground while the blocker is worked), and from priority (allocation is not
an ordering). The axis answers only: *what institutional attention should this
manifestation receive now?*

### 3.2 ESCALATED attack — **REJECTED AS A STATE VALUE**

Both available readings fail:

- As an allocation level above FOREGROUND it encodes an ordering among
  attended items — that is priority, which this axis MUST NOT encode.
- As "attention was demanded" it is a **transition act** (actor + reason ref +
  timestamp), i.e. a request/decision record, not a state of allocation.

Ruling: escalation survives as an **ACT** whose lawful effect is a transition
to FOREGROUND, with the escalation act reference retained as provenance of
the resulting FOREGROUND declaration. ACTIMANIRUN may derive the finding
"escalation act present, attention still BACKGROUND" as reconciliation
evidence (§11), never as a fourth state.

### 3.3 DORMANT_BY_LAW placement attack — **STAYS IN ATTENTIONSTATE**

LAWFUL_QUIET (hold) answers "why is movement absent"; DORMANT_BY_LAW answers
"what attention is lawful." They separate on live estate evidence:
`com.selfquant.spy24hobserver` moves autonomously (WITNESSED_MOVING) while
lawfully requiring no attention — a hold value cannot express that, because
nothing is held. Conversely a LAWFUL_QUIET manifestation may be FOREGROUND
(under review — review is attention without movement). Distinct dimensions.

### 3.4 Final vocabulary (each value a unique dimension)

```
FOREGROUND                 — attended now (scarce declared allocation)
BACKGROUND                 — in the attention rotation, not attended now (DEFAULT)
DORMANT_BY_LAW(law_ref)    — excluded from the rotation by an explicit law;
                             waking requires a lawful transition, not focus drift
UNKNOWN                    — attention declaration unreadable
```

---

## §4 — 001D · MOVEMENT_CADENCE_CONTRACT — DISPOSITION: **CLOSED (working term retained; canonical name = Founder decision)**

Declared-plane, founder-declared institutional fact, append-only supersession
(inherits OMR supersession law). No MANIFREQ terminology (Ruling 5 carried).

```yaml
movement_cadence_contract:
  manifestation_ref: <namespaced: OMR:MAN-NNNNNN | source-native | GOVERNANCE-CANDIDATE:*>
  authority_ref: <who declared, under what authority>          # declaration provenance
  effective_from: <institutional time — founder-declared>
  effective_until: <institutional time | OPEN>
  supersession_ref: <prior contract | NONE>                    # append-only chain
  cadence_class: BURST | STEADY | EVENT_DRIVEN | LONG_HORIZON | NO_EXPECTED_MOVEMENT
  accepted_movement_event_classes: [...]                       # what counts as movement (§8)
  accepted_witness_classes: [...]                              # what may witness those events
  expected_movement_window: <duration>                         # basis for derivation ONLY
  maximum_lawful_silence: <duration>                           # monotonic evaluation (timeself law)
  hold_exceptions: [<HoldContext kinds that suspend the silence clock>]
  pause_semantics: CLOCK_STOP                                  # closed this gate — see below
  freshness_requirements: <max admissible observation age for coverage>
  evaluation_clock: <named time type + clock domain, per §5>
  evaluation_route: <declared mechanical evaluation path>      # see empirical law below
```

**Closed laws:**

```
CadenceContract != ObservedMovement
  — declaring/superseding a contract is movement of the CONTRACT record,
    never movement of the subject manifestation.
ExpectedNextMovement is DERIVED, never contract source truth,
  unless explicitly Founder-declared as an institutional commitment.
NO CONTRACT → cadence-silence is NOT_EVALUABLE for cadence drift. NEVER STALE.
  A run-declared default window may support pulse evaluation only when
  flagged NON_CONTRACTUAL (000 §4 law 1 carried); it can never ground drift.
PAUSE_SEMANTICS = CLOCK_STOP: an active hold named in hold_exceptions stops
  silence accrual; accrual resumes at hold release; the hold interval is
  recorded, never deleted.
DOCUMENTED_CONTRACT != EVALUATED_CONTRACT (empirical law of this estate:
  every hand cadence contract on record failed compliance). A contract
  without a declared evaluation_route is admissible as declaration, but its
  drift findings carry standing NEVER_MECHANICALLY_EVALUATED.
```

---

## §5 — 001E · TYPED TIME MODEL — DISPOSITION: **CLOSED**

### 5.1 The six time types

```yaml
SOURCE_EVENT_TIME   (t_event): when the claimed effect occurred in the target
                               reality, per the source's own record. MAY BE ABSENT.
OBSERVATION_TIME    (t_obs):   when an admitted instrument read the source.
RECEIVED_TIME       (t_recv):  when evidence arrived at the estate boundary
                               (push-delivered evidence; distinct from a poll's t_obs).
ADMISSION_TIME      (t_adm):   when evidence passed the admission contract into
                               a run's frozen boundary.
EVALUATION_TIME     (t_eval):  when the compiler evaluated (run clock).
INSTITUTIONAL_TIME  (t_inst):  founder-declared effective coordinates —
                               "never a wall-clock read" (OMR-008 law carried).
```

### 5.2 Laws (all held under attack)

```
EvaluationTime != EventTime
ObservationTime != InstitutionalTime
WallClockRead != FounderDeclaration
TemporalPrecedence != Causation
MissingTime != InventedTime
AdmissionTime != EventTime  →  NewAdmission != NewMovement          (Specimen H)
LaterEvidence != PriorRunDefect — a run is judged against its own frozen
  boundary; later-admitted evidence may SUPERSEDE a projection, never
  retroactively falsify the run that lawfully lacked it.
```

Machine time is authorized for bounded runtime evaluation only (t_obs,
t_eval); it may never be reinterpreted as Founder-declared institutional
history (t_inst).

### 5.3 Degenerate-case evaluation (typed outputs, no guessing)

| Condition | Typed result |
|---|---|
| t_event missing on a witness | that witness cannot satisfy the freshness predicate → cannot produce WITNESSED_MOVING; it establishes movement-at-unknown-time only. If ALL coverage lacks time typing → pulse UNKNOWN(TIME_SEMANTICS_UNRESOLVED) |
| t_obs missing on a channel | coverage unprovable for that channel (SILENCE REQUIRES COVERAGE, §1.2); if no covered channel remains → UNKNOWN(NO_ADMITTED_SOURCE_COVERAGE) |
| clock domains disagree, no declared mapping | cross-domain freshness comparison NOT_EVALUABLE; contract's evaluation_clock names the governing domain; unmapped witnesses fall out of the establishing set |
| evidence arrives late (t_recv >> t_event) | currency judged by t_event only; the late arrival is admission-plane history |
| old evidence newly admitted (t_adm = now, t_event = old) | Specimen H — the run may now KNOW about old movement; it may never REPORT new movement |

---

## §6 — 001F · SOURCEHEALTH — DISPOSITION: **STRUCTURED OBJECT (scalar REJECTED)**

The four mandated attacks each vary one dimension while holding the others —
no single scalar can carry them without lying:

| Attack case | availability | freshness | integrity | coverage |
|---|---|---|---|---|
| available but stale | AVAILABLE | STALE(age) | VERIFIED | FULL |
| fresh but partial | AVAILABLE | FRESH | VERIFIED | PARTIAL(missing) |
| unavailable, cached witness valid | UNAVAILABLE | STALE(cache_age) | VERIFIED | per cache |
| digest valid, coverage incomplete | AVAILABLE | FRESH | VERIFIED | PARTIAL(missing) |

Closed object (per source, per run; observation-plane; derived from the run's
own read attempts, never declared):

```yaml
source_health:
  availability: AVAILABLE | PARTIAL | UNAVAILABLE | UNKNOWN
  freshness:    FRESH | STALE(age) | UNKNOWN          # t_obs vs freshness_requirements
  integrity:    VERIFIED | FAILED | UNVERIFIED        # digests/signatures
  coverage:     FULL | PARTIAL(missing) | NONE | UNKNOWN
```

Laws: a derived scalar summary is permitted for display only —
`DerivedSummary != SourceTruth` — and may never feed pulse derivation; cached
witnesses from an UNAVAILABLE source remain admissible per their evidence
ceiling (unavailability of the channel does not retroactively invalidate
verified custody of prior reads).

---

## §7 — 001G · SOURCE ADMISSION CONTRACT — DISPOSITION: **CLOSED (no adapters authorized)**

Per-source admission envelope, frozen per run:

```yaml
source_admission:
  source_identity: <stable ref>          # source-native identifiers retained
  source_class: TRUTH_SOURCE | CLAIM_SOURCE | PULSE_SIGNAL     # 000 §11 carried
  jurisdiction: <owning organ/system>
  authority_context: <under what law this read occurs; READ-ONLY always>
  identity_namespace: <how its refs map to OMR/candidate namespaces — no silent minting>
  snapshot_identity: <head/version at read>
  snapshot_digest: <digest where computable>
  coverage: [<accepted movement event classes this source CAN witness>]
  event_time_semantics: <clock domain; whether t_event is carried; mapping ref>
  observation_time: t_obs
  admission_time: t_adm
  freshness_contract: <max admissible age for this source's reads>
  evidence_ceiling: <maximum evidential force — see ceiling law>
  movement_claim_capability: CAN_ESTABLISH | CORROBORATE_ONLY | CLAIM_ONLY
  failure_state: <typed; a failed source is recorded, never silently dropped>
```

**Ceiling laws (closed):**

```
SourceAdmitted != SourceTrustedForEveryClaim — trust is per claim class,
  bounded by evidence_ceiling.
CLAIM_SOURCE (boards, registries, memory organs) → movement_claim_capability
  = CLAIM_ONLY: can NEVER produce WITNESSED_MOVING at any freshness; its
  assertions route to drift comparison (§11 STATE_ALIGNMENT_DRIFT).
PULSE_SIGNAL (mtimes, process tables, rosters) → CORROBORATE_ONLY by
  default: establishes ActivityObserved, not movement, unless the applicable
  contract explicitly elevates a named signal class to an accepted movement
  event class.
GitActivity != ManifestationMovement — a commit is movement evidence ONLY
  when the contract lists its class (e.g. commit-to-declared-repo with
  target-effect binding) in accepted_movement_event_classes.  (Specimen F)
```

Candidate source classes (UNRATIFIED EXAMPLES, no adapters created): OMR ·
OSM · local Git · GitHub · SELFPI · runtime process/daemon · INSELFACTION ·
external infrastructure witness · future DATASELF source.

---

## §8 — 001H · MOVEMENTCLAIM — DISPOSITION: **NECESSARY — DERIVED, RUN-SCOPED**

Without a typed unit, every run re-improvises the witness→effect→manifestation
binding and WITNESSED_MOVING becomes machine taste. MovementClaim is admitted
as ACTIMANIRUN's internal derived object — persisted only inside run records,
NOT a new canonical estate primitive.

```yaml
movement_claim:
  manifestation_ref: <namespaced>
  movement_event_class: <from the applicable contract>
  effect_claim: <what effect is claimed>
  target_reality: <where the effect is claimed to hold>
  source_refs: [...]
  witness_refs: [...]                    # existing governed evidence semantics; no minting
  event_time: t_event                    # may be ABSENT — see §5.3
  observation_time: t_obs
  standing: ESTABLISHED | INSUFFICIENT(typed_failure) | CLAIM_ONLY
  freshness: <derived vs window>
  derived_by: <run_id>
```

It answers: WHAT MOVED · WHAT EFFECT · IN WHICH TARGET REALITY · WITNESSED BY
WHAT · WHEN THE EFFECT OCCURRED. Pulse derivation becomes mechanical:

```
WITNESSED_MOVING  ⇔  ∃ MovementClaim(standing=ESTABLISHED, t_event ∈ window)
```

**Activity law (closed):** `Activity != Movement`. A SELF thinking, reviewing,
reading, or coding counts as manifestation movement ONLY if the applicable
contract defines that activity as a required target effect AND evidence
establishes the effect (Specimen D). Non-identities: MovementClaim != EVD
(references evidence, never mints it); MovementClaim != FOOTWORK (derived
observation vs declared work).

---

## §9 — 001I · FOOTWORK NECESSITY TEST — RESULT: **GENERALIZE_EXISTING**

Formal test — can existing structures express

```
WorkObject W --ADVANCES(effect=A)--> MAN-1
           W --ADVANCES(effect=B)--> MAN-2
           W --ADVANCES(effect=C)--> MAN-3
```

without duplicating W, lying about ownership, losing per-edge effect, or
mutating existing object semantics?

- **INHERIT_EXISTING — ELIMINATED.** All five candidates fail as-is (000 §9
  table re-verified against sealed bytes): T-objects are single-project with
  no advances[] relation; Æ dispatch packets are single-target transport;
  OMR founder questions bind one candidate_state_id; quads are occurrence
  records; MIG objects are single-subject registry mutations.
- **NEW_PRIMITIVE_NECESSARY — NOT ESTABLISHED.** Nothing in the T-object's
  shape structurally prevents a many-to-many `advances[]` edge set (per-edge
  effect_class + witness binding + per-edge completion). A wholly new
  primitive would duplicate the bounded-work-object semantics the T-object
  already carries and create a SECOND task-identity space — the same
  collision species as MANI-/MAN- (one letter from an existing namespace),
  which gate 000 existed to prevent.
- **GENERALIZE_EXISTING — RETURNED.** The lawful path is a generalized
  T-object carrying `advances[]: [{manifestation_ref, effect_class,
  witness_binding, edge_completion}]`. CONDITION: this requires a Founder
  cross-jurisdiction charter act with AgentBridge (000 §14.4, still open).
  Until that act: FOOTWORK remains `FOUNDATIONAL_CANDIDATE ·
  CANDIDATE_JUSTIFIED_NOT_MINTED` (D-000A-05 unchanged).

No mint. No migration. No renaming. Specimen G (§15) demonstrates the edge
grammar abstractly and proves no duplication laundering is required.

---

## §10 — 001J · RUN IDENTITY — DISPOSITION: **CLOSED**

Inherited grammar (HBC transit, 000 §11 carried):

```
run_id = <ISO8601-compact-UTC>Z-actimanirun-<12hex>
  <12hex> = sha256 prefix over canonical serialization of
            (admitted source boundary + per-source heads/digests + derivation version)
```

Distinct identities (none collapsible):

```
RunIdentity          — the evaluation ACT (run_id)
InputSetIdentity     — digest of the frozen admitted boundary
CompilerVersion      — derivation logic version
ProjectionIdentity   — identity of the output artifact lineage
ProjectionDigest     — content digest of DERIVED_CONTENT (see below)
EvaluationTime       — t_eval, run metadata
```

**Determinism boundary (exact, not weakened):** a run has two phases.

```
OBSERVATION PHASE  — reads live sources, produces admitted snapshots.
                     Inherently nondeterministic. Never claims determinism.
DERIVATION PHASE   — pure function: (InputSetIdentity, CompilerVersion) →
                     DERIVED_CONTENT. MUST be byte-deterministic under
                     canonical serialization.
ObservationPhase != DerivationPhase
```

The projection separates `DERIVED_CONTENT` (deterministic) from
`RUN_METADATA` (run_id, t_eval, per-read t_obs — necessarily varies).
ProjectionDigest is computed over DERIVED_CONTENT ONLY. Hence the laws:

```
Run1 != Run2  may coexist with  ProjectionDigest1 = ProjectionDigest2
SameInputSetIdentity + SameCompilerVersion → SameProjectionDigest
```

Nondeterministic observations are excluded from the digest by construction —
by phase membership, not by ad-hoc exemption lists.

---

## §11 — 001K · DRIFT SEMANTICS — DISPOSITION: **8 SURVIVORS, 2 REJECTED/DEFERRED**

ACTIMANIRUN owns no root Drift doctrine; all findings are DERIVED under the
sealed parent loop (which contains an explicit Classify Drift step). Prime
laws: `DerivedDriftFinding != SourceTruthMutation` — ACTIMANIRUN may DETECT,
never REPAIR. Standing of every subclass: DERIVED_FINDING_CANDIDATE —
admission under parent doctrine remains a Founder decision.

| Subclass | Expected object | Observed object | Comparison rule | Resolution requirement |
|---|---|---|---|---|
| STATE_ALIGNMENT_DRIFT (subsumes CLAIM_WITHOUT_WITNESS) | claim-source institutional assertion | witness-derived standing | claim vs accepted-witness compatibility | source-owner reconciliation |
| MOVEMENT_CADENCE_DRIFT | contract (max_lawful_silence, hold_exceptions) | latest ESTABLISHED claim t_event | monotonic silence > contract, no active exception, evaluable | movement, hold declaration, or contract supersession |
| EVIDENCE_INTEGRITY_DRIFT | recorded digest in a governed record | recomputed digest | equality | custody investigation (never repair) |
| LINEAGE_DRIFT | append-only single-current supersession law | actual chain | graph check (missing parent / two currents) | Founder adjudication (SFC-005 fork species) |
| DEPENDENCY_DRIFT (incl. expired unreviewed holds) | hold's dependency/review condition | referenced object's state / review clock | satisfaction & expiry check | hold review act |
| TARGET_REALITY_DRIFT | effect_claim of an ESTABLISHED claim or completion record | target-reality probe witness | effect-specific verification class | source-owner reconciliation (estate proof: deploy-witness vs Cloudflare 522) |
| PROJECTION_STALENESS_DRIFT (narrows SOURCE_FRESHNESS_DRIFT) | projection covering latest witnessed state | projection input boundary vs newest admitted witness | boundary older than witness | re-run/recompile by projection owner |
| DECISION_RECONCILIATION_DRIFT (bounded) | a decision record's OWN declared successor act + window | absence of that act past window | only evaluable where the decision declares both; else NOT_EVALUABLE | the declared successor act |

**Rejected/deferred:**

- `AUTHORITY_DRIFT` — OUT_OF_JURISDICTION: authority adjudication belongs to
  the authority organs. ACTIMANIRUN may surface raw observations (mutation
  witnessed + no lease record found) as evidence FOR those organs — never as
  a typed drift verdict of its own.
- `NOTE_CONTEXT_DRIFT` — DEFERRED_UNTIL_NOTEPAD_GENESIS: no drift may be
  typed against a primitive that does not exist (D-000A-06); the 000 §10
  interface reservation stands.
- Channel staleness per se is SourceHealth (§6), not drift — drift requires
  an expected/observed pair, and a slow source violates no expectation unless
  a contract declares one.

---

## §12 — 001L · HOST NECESSITY TEST — DISPOSITION: **C CLOSED (bounded cross-organ projection compiler)**

Adjudicated against A/B/C/D/E on jurisdiction/coupling evidence only:

- **A (OSM extension) — REJECTED.** OSM's sealed jurisdiction is compiled
  institutional standing from authored organ files. ACTIMANIRUN's closed
  semantics now REQUIRE machinery OSM lacks and must not grow: typed
  six-time model, two-phase runs with frozen boundaries, per-source
  admission/ceilings, live truth/pulse adapters. Grafting distorts OSM's
  sealed scope (prohibited coupling).
- **B (OMR subsystem) — REJECTED.** OMR is the constitutional identity and
  canonical-state registry. Coupling live pulse machinery into the identity
  organ distorts its jurisdiction; OMR retains manifestation identity
  untouched (constraint honored).
- **D (new organ) — REJECTED.** Necessity Test: a new organ is lawful only
  if A–C necessarily cause ownership distortion. C causes none — it owns
  ONLY derivation logic, run records, and projections; it owns no upstream
  truth. D therefore fails necessity.
- **E (unresolved) — NOT TAKEN.** The evidence adjudicates.

**New boundary law closed this gate** (resolving the one live collision risk):

```
ACTIMANIRUN MUST NOT PROJECT INSTITUTIONAL STANDING.
OSM remains the sole institutional-standing projector; ACTIMANIRUN consumes
OSM output as CLAIM_SOURCE and quotes institutional state source-natively,
verbatim, never re-derived. The two projectors project ORTHOGONAL AXES —
this is D-000A-01 applied to jurisdiction.
```

C binds the SHAPE only. The custody address (which repo hosts the compiler)
remains a Founder decision. The host is NOT created.

---

## §13 — 001M · MINIMUM IMPLEMENTATION TOPOLOGY (DERIVED, NOT BUILT)

**Byte-verification note (evidence-scope discipline):** the authorization
packet states "Gate 000 referenced a four-object topology." The string
"topology" and any four-object enumeration appear NOWHERE in the sealed 000
artifact or its evidence record (verified against `ab75649a…` / `9dbf36e8…`).
Sealed §13 names three owned surfaces (derivation logic, run records,
projections); sealed §11 defines source admission as a fourth functional
surface. The packet's count is therefore a MEMORY CLAIM that fails byte
verification as a citation — while the topology reconstructed from sealed
bytes below happens to contain four objects. Reconstructed from bytes, not
from the packet:

| Object | Purpose | Input | Output | Authority | Mutation rights | Persistence | Failure behavior | Non-identity |
|---|---|---|---|---|---|---|---|---|
| **AdmissionRecord** | freeze the per-run source boundary (§7) | source reads + admission contracts | admitted snapshot set + InputSetIdentity | READ-ONLY over all sources | appends its own record only | append-only run store | typed failure_state per source; dropped coverage LOGGED never silent | != evidence ledger; != source truth |
| **DerivationCore** | pure derivation (§10 derivation phase) | admitted set + cadence contracts + CompilerVersion | MovementClaims + five-axis values + drift findings | NONE over sources | none (pure function) | versioned code artifact | typed NOT_EVALUABLE / UNKNOWN outputs; never guesses | != status authority; != repair engine |
| **RunRecord** | bind the act (§10) | run_id, t_eval, InputSetIdentity, CompilerVersion, per-source health | the run's durable witness | none | appends itself once | append-only | a failed run is recorded as failed | RunRecord != Projection |
| **Projection** | queryable derived output | DERIVED_CONTENT + RUN_METADATA | board-class rendering + ProjectionDigest | none | replaced per run; NEVER edits sources | overwrite-class under LAUNCH_BOARD law ("this board is never truth") | absent projection != absent manifestation | Projection != SourceTruth |

Implementation becomes mechanical from §§1–12 + this table: every field is
semantically typed, every degenerate case has a typed output, and no step
requires machine taste. **NOTHING IS IMPLEMENTED IN THIS GATE.**

---

## §14 — CROSS-AXIS FALSIFICATION — ALL 10 PROHIBITED DERIVATIONS FAIL (PASS)

Each prohibited inference is broken by a live estate counterexample:

| Prohibited derivation | Killing counterexample | Mechanism that blocks it |
|---|---|---|
| InstitutionalState → MovementPulse | 24 OSM-board ACTIVE records vs witnessed silence (Specimen C) | pulse function takes no institutional input (§1.4) |
| MovementPulse → HoldContext | silence with NONE_DECLARED — pulse cannot invent a declarer | hold is declared-plane only (§2.1) |
| HoldContext → AttentionState | WAITING_EXTERNAL item worked FOREGROUND | axes proven divergent (§3.1) |
| AttentionState → Priority | FOREGROUND set has no internal ordering | allocation != ordering (§3.2) |
| SourceHealth → MovementPulse | stale source, valid cached witness (Specimen I) | pulse reads evidence set, not channel state (§1.3) |
| GitActivity → MovementPulse | 2026-07-15 chore-sweep across 11 repos (Specimen F) | event-class predicate (§7 ceiling law) |
| AgentActivity → MovementPulse | SPY observer runtime; this session's own tokens (Specimens B, D) | Activity != Movement (§8) |
| CadenceSilence → Drift without contract | any uncontracted quiet manifestation | NOT_EVALUABLE law (§4) |
| FreshRun → FreshSource | this gate compiling over 10-day-stale boards (Specimen I) | two-phase run; SourceHealth carried per source (§10, §6) |
| AdmissionTime → EventTime | old witness admitted today (Specimen H) | currency predicate reads t_event only (§5.3) |

---

## §15 — ADVERSARIAL SPECIMENS A–I — ALL REPRESENTABLE WITHOUT COLLAPSE (PASS)

**A — SELFOURCLOUD** (SFC-001 sealed; SFC-002 blocked on edge VPS):
`institutional_state: ACTIVE(source-native) · movement_pulse:
NO_CURRENT_MOVEMENT_WITNESS · hold_context: WAITING_EXTERNAL(edge VPS
provisioning) · attention_state: BACKGROUND · source_health: per channel`.
No drift: hold_exceptions suspend the silence clock. VALID, no contradiction.

**B — SPY OBSERVER** (`com.selfquant.spy24hobserver`, 60s tick):
`movement_pulse: WITNESSED_MOVING` (contract accepts daemon-tick event class
with target effect = observation capture) while interactive SELF projection
activity = NONE and `attention_state: DORMANT_BY_LAW(stoppability
amendment)`. AgentActivity != ManifestationActivity holds in BOTH directions:
the daemon moves its manifestation with no agent attending; an agent may
churn with no manifestation moving.

**C — STALE BOARD** (OSM board compiled 2026-08-07, claims ACTIVE):
institutional_state remains source-native ACTIVE (quoted verbatim, §12
boundary law); movement_pulse does NOT become WITNESSED_MOVING (board is
CLAIM_SOURCE → CLAIM_ONLY, §7); source_health.freshness = STALE(10d) exposes
the input. If the board asserts movement: STATE_ALIGNMENT_DRIFT finding, not
pulse.

**D — THIS GATE ITSELF:** ClaudeSELF's analysis tokens, tool calls, and
elapsed runtime establish NOTHING. Movement of GOVERNANCE-CANDIDATE:ACTIMANIRUN
exists iff the authorized target effect (durable custodied semantic record)
occurs and is witnessed — i.e., at the custody commit of this artifact, and
only then. At gate STOP the pulse lawfully returns to
NO_CURRENT_MOVEMENT_WITNESS while the manifestation remains alive — the
exact distinction this system exists to preserve.

**E — LOCAL/GITHUB DIVERGENCE** (~/RUORA main 151 commits unpushed): local
commits to the declared repo are admissible movement witnesses (TRUTH_SOURCE,
accepted class); GitHub silence is one source's health
(`availability: AVAILABLE, coverage: PARTIAL` for local-only lineages), and
under SILENCE REQUIRES COVERAGE a silent GitHub channel can never overrule an
established local witness. GitHub silence does NOT suppress valid local
witnessed movement.

**F — CHORE SWEEP** (2026-07-15 cluster, 11 repos): many commits, no
target-reality advancement. Commits fail the accepted_movement_event_class
predicate (no target-effect binding) → remain GitActivity; MovementClaims
derive as INSUFFICIENT(no_target_effect); pulse unmoved. GitActivity !=
ManifestationProgress, mechanically.

**G — ONE FOOTWORK / THREE MANIFESTATIONS:** under §9's returned disposition,
one generalized work object W carries
`advances[] = [{MAN-1, effect:A, witness:w1}, {MAN-2, effect:B, witness:w2},
{MAN-3, effect:C, witness:w3}]` — single W identity (no duplication), owner
on W (no ownership lie), per-edge effect and witness (nothing lost), and each
edge derives an independent MovementClaim for its manifestation. Expressible.
NOT minted.

**H — NEWLY ADMITTED OLD WITNESS (mandatory attack) — HELD:** t_adm = now,
t_event = old. The freshness predicate reads t_event ONLY (§5.3). The run's
knowledge changed; the manifestation's movement did not.
`OldEvent + NewAdmission != NewMovement.` The projection may report "old
movement newly admitted" as admission-plane history — it may never report
current movement.

**I — STALE SOURCE + FRESH RUN (mandatory attack) — HELD:** run at t_now over
a stale snapshot: RunFreshness = fresh (RUN_METADATA), source_health.freshness
= STALE(age), movement_pulse derived only from admissible movement evidence
(§1.3). ProjectionDigest covers DERIVED_CONTENT only (§10), so a fresh run
cannot launder stale evidence into fresh reality even at the byte level.
`FreshProjection + StaleSource != FreshReality.`

---

## §16 — PASS ADJUDICATION

| Criterion | Result |
|---|---|
| MovementPulse semantics close | CLOSED (§1) |
| HoldContext semantics close | CLOSED (§2) |
| AttentionState necessity adjudicated | IRREDUCIBLE; vocabulary closed (§3) |
| MovementCadenceContract closes | CLOSED (§4) |
| Time semantics close | CLOSED (§5) |
| SourceHealth closes | CLOSED, structured (§6) |
| SourceAdmission closes | CLOSED (§7) |
| MovementClaim disposition | NECESSARY, derived/run-scoped (§8) |
| Footwork necessity disposition | GENERALIZE_EXISTING (§9) |
| Run identity closes | CLOSED, exact determinism boundary (§10) |
| Drift inheritance boundary closes | CLOSED, 8 candidates typed (§11) |
| Host disposition closes | C CLOSED (§12) |
| Topology derivable without machine taste | YES (§13) |
| Specimens A–I representable without collapse | ALL PASS (§15) |
| No implementation mechanism required to define the law | HELD — all laws stated over typed semantics only |

### GATE RESULT: **PASS**

```
ACTIMANIRUN-001 = SEMANTICS_CLOSED + FALSIFICATION_SURVIVED + RUNTIME_ABSENT
```

ACTIMANIRUN is now **semantically safe for an implementation gate** — every
compiler decision is mechanical over this artifact — SUBJECT TO the Founder
decisions below. SEMANTICALLY_SAFE != IMPLEMENTATION_AUTHORIZED.

---

## §17 — UNRESOLVED FOUNDER DECISIONS (EXACT)

1. Ratify the closed MovementPulse vocabulary + unknown_reason set (§1).
2. Ratify the closed HoldContext vocabulary, including the BLOCKED_CONTEXT
   rejection and the WAITING_DEPENDENCY narrowing of LEASE_HELD_ELSEWHERE (§2).
3. Ratify the closed AttentionState vocabulary, including the ESCALATED
   removal (escalation = act, not state) (§3).
4. Canonical name for MOVEMENT_CADENCE_CONTRACT (working term retained) (§4).
5. FOOTWORK: authorize (or decline) the cross-jurisdiction charter act with
   AgentBridge implementing the GENERALIZE_EXISTING disposition (§9).
6. Custody address of the projection compiler (host SHAPE closed as C;
   address open) (§12).
7. Admission of the eight drift subclasses under parent drift doctrine (§11).
8. Whether OMR's first real founder decision should precede the first
   canonical ACTIMANIRUN projection (000 §14.8, carried unresolved).
9. Remote publication of the custody branch (still NOT authorized).
10. Opening ACTIMANIRUN-002 (implementation) — PROHIBITED until granted.

## §18 — ABSOLUTE STOP (EXECUTED)

STOP after semantics + falsification + bounded custody of this artifact and
its evidence record. NO implementation · NO ACTIMANIRUN-002 · NO projection
compiler · NO source adapters · NO FOOTWORK creation · NO NOTEPAD · NO
CodexSELF contact · NO Foundation IR · NO departure from ACTIMANIRUN reality.
