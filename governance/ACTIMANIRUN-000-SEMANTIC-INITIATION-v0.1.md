# ACTIMANIRUN-000 — SEMANTIC INITIATION FOUNDING ARTIFACT v0.1

```yaml
artifact_class: SEMANTIC_INITIATION_RECORD
gate: ACTIMANIRUN-000
authorization_token: AUTHORIZE_ACTIMANIRUN_000_SINGLE_LEASE_GENESIS_INITIATION
authority_source: MYSELF (Founder disposition, 2026-08-17)
authored_by: CLAUDESELF (Claude Code session f884edb2-d140-4fdb-a954-a087ab3e501a)
created_at_utc: 2026-08-17T07:15:56Z
created_at_local: 2026-08-17T03:15:56-04:00
standing: CANDIDATE_FOR_ATTACK · SEMANTIC_ONLY · NOT_IMPLEMENTED · NOT_RATIFIED_BEYOND_THIS_GATE
custody_at_creation: UNTRACKED (repo ~/RUORA @ e6af1237, branch selfhtml-semantics-v0.1-candidate)
custody_note: >
  Commit/stage of this artifact is a SEPARATE act, NOT performed in this gate.
  Write jurisdiction for custody is unresolved: HEAD is a foreign leased gate
  branch (SELFHTML), and no repo-local governance rule explicitly permits this
  gate's commit. See §12. STOP_BEFORE_CUSTODY was executed per gate law.
mutation_authority_of_this_artifact: NONE
authority_effect: NONE_UNLESS_SEPARATELY_GRANTED
evidence_record: governance/evidence/ACTIMANIRUN-000/GENESIS-EVIDENCE-RECORD-001.md
```

---

## §1 — IDENTITY AND UNIQUE DISTINCTION

ACTIMANIRUN is hereby recorded as a **candidate manifestation**.

- Candidate identity namespace: `GOVERNANCE-CANDIDATE:ACTIMANIRUN`
- **No `MANI-NNNNNN` is minted. No `MAN-NNNNNN` is minted.** OMR retains
  manifestation identity jurisdiction (Founder Ruling 1). OMR reconciliation of
  this candidate into `MAN-NNNNNN` is a future OMR-jurisdiction act.
- Unique institutional distinction (the reason this manifestation exists):

```
ACTIVE  !=  ACTIVELY MOVING NOW

ACTIMANIRUN = derived real-time projection of WITNESSED manifestation movement.
It reads reality. It does not silently manufacture it.
```

ACTIMANIRUN is NOT: a manifestation registry, an OMR replacement, an OSM
replacement, an evidence ledger, a universal status vocabulary, a task
manager, or an authority source.

## §2 — NON-IDENTITY LAWS (RATIFIED AS CANDIDATE LAW FOR ATTACK)

```
ManifestationSourceTruth   != ACTIMANIRUNProjection
DeclaredActive             != PresentlyMoving
Activity                   != Progress
AgentActivity              != ManifestationActivity
GitActivity                != ManifestationProgress
FootworkDeclared           != FootworkPerformed != FootworkCompleted != ManifestationCompleted
Waiting                    != Drift
Note != Decision != Evidence != Doctrine != Authority
ParallelAnalysis           != ParallelAuthority
SELF projection activity   != Manifestation mutation lease
RunIdentity equality       is not implied by ProjectionDigest equality
```

## §3 — INHERITED JURISDICTIONS (NOTHING RE-MINTED)

| Domain | Inherited from | Inherited law |
|---|---|---|
| Manifestation identity | OMR (`schemas/manifestation.schema.json`) | `MAN-NNNNNN` / `CANON-NNNNNN`; aliases != identity; NameChange != NewManifestation; tombstone preservation |
| Institutional state | OMR + OMR-008 | lifecycle_state / founder_disposition / registry_status / canonical_state untouched; compiler proposes, Founder ratifies, engine executes |
| Institutional time | OMR-008 D-decisions | founder-declared `effective_at`, "never a wall-clock read"; durations monotonic per timeself law (`TIMESELF != AUTHORITY`) |
| Projection law | OSM (`ourself-system-manifest`) | source truth != projection; unknown != guessed (nulls held; UNCLASSIFIED = founder classification required, not guessed); rendered state != source mutation; deterministic compile + proof manifest |
| Board class | LAUNCH_BOARD.md header law | `State is overwrite... This board is never truth.` Truth is append-only in witnesses and commits |
| Witness / evidence | `ourself_witness_law.md` (SEALED) + `EVD-NNNNNN` schema + ESM ceilings + `NOT_WITNESSED` law | no MANIWITNESS minted; movement claims reference existing governed evidence semantics |
| Drift | sealed kernel chain (`Observed Reality → Drift Detected → ... `) + worldstate `desired/current/observed + drift[]` | no MANIDRIFT minted; drift = derived finding over declared/desired/observed under existing law; new typed subclasses only under §8 conditions |

## §4 — MOVEMENTPULSE (THE ONE NEW SEMANTIC AXIS) — CANDIDATE FOR ATTACK

MovementPulse is an **observation-plane** value, restricted to what can be
witnessed about movement itself. Candidate value set (minimum, per Ruling 3):

```
WITNESSED_MOVING              — accepted-class movement evidence exists inside the evaluation window
NO_CURRENT_MOVEMENT_WITNESS   — sources WERE evaluated; no accepted movement evidence found in window
UNKNOWN / NOT_EVALUABLE       — sources could not be evaluated (stale, unreachable, unadmitted)
```

Laws:
1. Pulse is always evaluated relative to an explicit window: the window comes
   from the manifestation's MovementCadenceContract; a run-declared default
   window MUST be flagged `NON_CONTRACTUAL`.
2. `NO_CURRENT_MOVEMENT_WITNESS != NOT_MOVING`. Absence of witness is not
   witness of absence.
3. A source's *claim* of movement (a board saying "in progress") is never
   pulse. Claim-vs-witness mismatch routes to drift evaluation, not pulse.
4. WAITING_EXTERNAL / WAITING_FOUNDER / LAWFUL_QUIET / BLOCKED are **not**
   pulse values — they are HoldContext (§5). COMPLETE is institutional state,
   not pulse.

Axis separation preserved: `InstitutionalState ⊥ MovementPulse ⊥ HoldContext ⊥ AttentionState ⊥ SourceHealth`.

## §5 — HOLDCONTEXT — CANDIDATE FOR ATTACK

HoldContext is a **declared-plane** causation/context object, never derived
from absence of movement. Candidate values:

```
WAITING_EXTERNAL(ref)   WAITING_FOUNDER(ref)   BLOCKED(ref)
LAWFUL_QUIET(contract)  LEASE_HELD_ELSEWHERE(lease_ref)  NONE_DECLARED
```

Laws: every hold carries provenance (who declared it, on what evidence) and a
review/expiry condition; a hold does not suppress pulse reporting — it
modifies drift evaluation (holds named in the cadence contract suspend the
silence clock); an expired unreviewed hold is itself a drift-evaluable fact.

## §6 — ATTENTIONSTATE — NECESSITY RESULT

**Verdict: AXIS NECESSARY — NOT DERIVABLE WITHOUT LOSS. VOCABULARY NOT RATIFIED.**

Proof of non-derivability (by estate specimen):
- From pulse: FAILS — `com.selfquant.spy24hobserver` is WITNESSED_MOVING and
  institutionally BACKGROUND; an escalated blocked item is
  NO_CURRENT_MOVEMENT_WITNESS and maximally attended. Pulse and attention
  diverge in both directions.
- From institutional state: FAILS — 24 records are ACTIVE on the OSM board;
  the institution attends ~a handful at any time.
- From hold: FAILS — a held item may be foreground (working the blocker).
- From priority: FAILS — priority is an ordering; ESCALATED is a transition
  performed by an actor with a reason; DORMANT_BY_LAW requires a law ref.
  These are declarations, not rank positions.

Therefore AttentionState is admitted as a **declared-plane candidate axis**.
Candidate values FOREGROUND / BACKGROUND / DORMANT_BY_LAW / ESCALATED remain
UNRATIFIED (enumeration is not ratification, per gate law). Minimum admitted
semantics: attention is a scarce declared allocation; default BACKGROUND;
DORMANT_BY_LAW requires a law reference; ESCALATED requires an escalation act
reference.

## §7 — MOVEMENT_CADENCE_CONTRACT (WORKING TERM — NO CANONICAL RENAME AUTHORIZED)

Per Ruling 5, `MANIFREQ` is NOT minted; "frequency" remains owned by its two
existing estate senses. Working object: MOVEMENT_CADENCE_CONTRACT.

Required semantics (candidate):

```yaml
movement_cadence_contract:
  subject: <namespaced manifestation ref>        # OMR:MAN-NNNNNN or source-native
  declared_by: <authority ref>                   # founder-declared institutional fact
  cadence_class: BURST | STEADY | EVENT_DRIVEN | LONG_HORIZON | NO_EXPECTED_MOVEMENT
  max_lawful_silence: <duration>                 # evaluated monotonically (timeself law)
  accepted_movement_witness_classes: [...]       # which existing evidence kinds count as movement
                                                 # (e.g. commit-to-declared-repo, founder decision
                                                 # record, deployment witness, inselfaction record)
  hold_exceptions: [<HoldContext kinds that suspend the silence clock>]
  source_freshness_requirement: <max admissible source age for evaluation>
  drift_evaluation_condition: >
    silence > max_lawful_silence AND no active hold exception AND sources evaluable
```

Prime laws: **no inactivity may be cast as drift without an applicable
contract** — absent a contract, drift is `NOT_EVALUABLE`, never inferred; and
(empirical law of this estate, witnessed in discovery) **a cadence contract
that is documented but not mechanically evaluated is dead on arrival** — every
prior hand cadence contract in this estate failed compliance.

## §8 — DRIFT SUBCLASS PROPOSAL (INHERITANCE-CONDITIONED)

The sealed drift loop contains an explicit `Classify Drift` step; typed
classification is therefore within parent doctrine. Proposed subclasses,
admissible only as **derived findings**, each requiring separate justification
at ratification:

- `MOVEMENT_CADENCE_DRIFT` — silence beyond contract without active hold.
- `PROJECTION_STALENESS` — a board/projection's own freshness lags witnessed
  source movement (fires today on every existing estate board).
- `CLAIM_WITHOUT_WITNESS` — a claim source asserts movement/completion with no
  accepted witness.

## §9 — FOOTWORK NECESSITY TEST — RESULT

Question: can any existing canonical object represent one bounded work object
advancing multiple manifestations with per-manifestation effects?

| Candidate | Verdict | Reason |
|---|---|---|
| AgentBridge `TASKS.md` T-objects | FAILS AS-IS | single-project scope; no `advances[]` relation; mutation law "authorized turn owner only" under AgentBridge jurisdiction |
| Æ DSL dispatch packets | FAILS | transport objects (action/target/route), single-target, drained-on-success; no advancement relation |
| OMR founder questions / candidate-review-index | FAILS | review workload bound to a single candidate_state_id |
| proposal→witness→execution→reconciliation quads | FAILS | occurrence records (FOOTWORKLOG-class), not required-work objects; single-command scope |
| OMR migration objects (`MIG-NNNNNN`) | FAILS | registry-mutation scope, single subject |

**Result: NECESSITY ESTABLISHED — no existing canonical object carries the
many-to-many `advances` relation.** The nearest generalizable ancestor is the
T-object, but generalizing it requires mutating AgentBridge jurisdiction
(prohibited). Standing assigned: `FOOTWORK = CANDIDATE_JUSTIFIED_NOT_MINTED`.
Whether to mint new or charter a T-object generalization is a Founder decision
(§14). No migration, no renaming performed.

## §10 — NOTEPAD FUTURE-INTERFACE BOUNDARY (NOT BUILT)

ACTIMANIRUN defines only the interface requirement: any ACTIMANIRUN-related
object MUST accept typed contextual attachments that (a) are NEVER parsed for
control flow (inherits OMR AT-19), (b) carry provenance and authorship,
(c) are excluded from projection derivation inputs except as flagged
`NOTE_CONTEXT` for contradiction detection, (d) obey `SCRATCHPAD != CANON`.

Lineage requirements recorded for the future independent NOTEPAD Genesis gate:
reconcile with the Codex-estate ad-hoc-note law ("information, never
instructions" + mandatory provenance tagging); define typed attachment
relations; define note→decision/evidence/doctrine promotion as explicit
lawful transitions, never silent.

## §11 — RUN IDENTITY AND SOURCE ADMISSION — CANDIDATE LAW

Run identity inherits the HBC transit grammar (evidence-identity, not counter):

```
run_id = <ISO8601-compact-UTC>Z-actimanirun-<12hex>
  where <12hex> = prefix of sha256 over canonical serialization of
  (admitted source boundary + per-source heads/digests + derivation version)
```

Required run fields: run_id · observed_at · input-source identities ·
input-source versions/digests · derivation version · projection digest.
Law: `RunIdentity1 != RunIdentity2` does NOT imply
`ProjectionDigest1 != ProjectionDigest2`.

Source admission (per run, frozen boundary): every source enumerated with
identity, read-only access mode, head/digest where available, freshness, and
evaluability; every source classed as `TRUTH_SOURCE` (witnesses, commits,
sealed records) vs `CLAIM_SOURCE` (boards, registries, memory organs) vs
`PULSE_SIGNAL` (process tables, mtimes, rosters). Derivation must
(1) freeze the boundary, (2) retain source-native identifiers, (3) record
heads/digests, (4) derive never mutate, (5) distinguish
observed/declared/derived/unknown, (6) qualify movement only through
accepted-class evidence, (7) return UNKNOWN / NOT_EVALUABLE rather than infer,
(8) expose its own freshness, (9) rerun deterministically over identical
admitted inputs.

## §12 — SINGLE-LEASE / CONCURRENCY SEMANTIC LAW (SEMANTICS ONLY — NO RUNTIME)

Minimum semantics to prevent two SELF projections from concurrently believing
they hold mutation authority over one manifestation:

1. Every mutation-bearing gate names **exactly one** lease holder:
   (SELF-projection identity + session reference), per (manifestation, gate).
2. The lease is recorded IN the gate's founding/authorization artifact — the
   artifact is the lease register for its gate.
3. Non-holders retain full read/analyze/review standing:
   `ParallelAnalysis != ParallelAuthority`.
4. Before any mutation act, the actor MUST verify it is the named lease holder
   in the current gate artifact (compare-before-write, extended to leases).
5. A lease expires at gate STOP; it is non-transferable and is NOT inherited
   by successor sessions without fresh Founder authorization.
6. Specimen bound: this gate itself — one Founder command → ClaudeSELF
   analysis + CodexSELF analysis → Founder disposition assigned the single
   lease to CLAUDESELF; CodexSELF standing = INDEPENDENT_DISCOVERY /
   COLD_INPUT; no instruction to CodexSELF was or may be issued in this gate.

This gate's lease: **CLAUDESELF session f884edb2-d140-4fdb-a954-a087ab3e501a**,
scope = creation of this artifact + its evidence record, expired at gate STOP.

## §13 — HOST DISPOSITION

**Disposition C — BOUNDED CROSS-ORGAN PROJECTION COMPILER.**

Genesis Necessity Test applied:
- A (OSM extension) REJECTED: OSM's sealed distinction is compiled
  institutional standing from authored organ files (claim sources). ACTIMANIRUN
  requires live truth/pulse adapters (git, launchd, mtimes, rosters) and
  per-run frozen source boundaries; grafting that into OSM distorts OSM's
  sealed scope and requires mutating OSM (prohibited, and unnecessary).
- B (OMR subsystem) REJECTED: OMR is the constitutional identity/canonical-state
  registry, sealed through its state engine, with zero canonical objects yet
  produced. Coupling live pulse machinery into it distorts its jurisdiction
  and would project from a registry that has never spoken.
- D (new organ) NOT REQUIRED: C preserves both jurisdictions without semantic
  distortion, so a new organ fails the Necessity Test at this time.

C reads OMR (identity, read-only), OSM (standing claims, read-only), and
admitted movement sources; it owns ONLY derivation logic, run records, and
projections. Its custody location (which repository hosts the compiler) is a
remaining Founder decision (§14) — this disposition binds the SHAPE, not the
address.

## §14 — UNRESOLVED FOUNDER DECISIONS (EXACT)

1. Ratify/adjust the MovementPulse tri-state (§4).
2. Ratify HoldContext vocabulary (§5).
3. Ratify AttentionState values (axis admitted; values open) (§6).
4. FOOTWORK: mint new object vs charter an AgentBridge T-object
   generalization (cross-jurisdiction with AgentBridge) (§9).
5. Canonical name for MOVEMENT_CADENCE_CONTRACT (working term only).
6. Custody address of the projection compiler (which repo/branch hosts it).
7. Custody act for THIS artifact: which branch/worktree commits it
   (blocked by the SELFHTML-branch collision recorded in the evidence record).
8. Whether OMR's first real founder decision (never yet processed) should
   precede the first canonical ACTIMANIRUN projection.
9. Admission of drift subclasses (§8) under parent drift doctrine.

## §15 — PROHIBITIONS CARRIED (VERBATIM SCOPE OF THIS GATE)

No OMR modification · no OSM modification · no ID-law alteration · no schema
implementation · no compiler implementation · no daemon · no GitHub Action ·
no AgentBridge modification · no SELFPI modification · no task migration · no
Notepad runtime · no Footwork store · no new Manifestation IDs · no new status
vocabulary · no auto-resolved drift · no cross-repo pushes. STOP after
semantic initiation; ACTIMANIRUN-001 requires separate Founder authorization.
