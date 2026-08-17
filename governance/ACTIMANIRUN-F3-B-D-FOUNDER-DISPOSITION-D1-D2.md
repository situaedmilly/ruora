# ACTIMANIRUN-F3-B-D — FOUNDER DISPOSITION OF D1 AND D2

```yaml
record_class: FOUNDER_DISPOSITION_CUSTODY_RECORD
gate: ACTIMANIRUN-F3-B-D
authorization_token: AUTHORIZE_ACTIMANIRUN_F3_B_FOUNDER_DISPOSITION_D1_D2_ONLY
authority_source: MYSELF (Founder transmission act, 2026-08-17)
executed_by: CLAUDESELF (Claude Code session 1ed7a1da-0ad5-493f-9f62-03d5c85fd2a6)
custodian_role: SCRIBE — CLAUDESELF custodies a Founder act; it authored neither ruling
lease_scope: >
  Bounded lease for gate F3-B-D only: custody of this single governance record.
  NO implementation mutation. NO D3 build. NO CC-1 repair. NO F3-C/D/E. NO 003B.
  NO push. Expires at STOP.
recorded_at_utc: 2026-08-17T22:39:48Z
subject:
  gate: ACTIMANIRUN-F3-B
  artifact: governance/ACTIMANIRUN-F3-B-EVALUATION-PROVENANCE-GENESIS-AND-FALSIFICATION.md
  governance_commit: 356b089dec134539afb53a7442fffc943511ac77
  lines: 483
  bytes: 26395
  sha256: 1bdb1a5828d230f3059c69b3705f27c5f8d22d712c2ba87b2b4154bf2c5f8a94
  verdict_disposed: F3_B_FOUNDER_DECISION_REQUIRED
observed_implementation:
  host_head: d1de631efcba5ed6718c19bdd368ad9625dc61ea
  executable_implementation: 5b78ed5d4dffc5875d3e6c6554ba29c8e80794a7
  compiler_version: actimanirun-derive/v0.3
  tests: 63 passed / 0 failed
  mutation_by_this_gate: NONE
d1: NARROW_AND_RATIFY_REMAINDER
d2: NO_FOREIGN_EVALUATION_PROVENANCE_JURISDICTION
verdict: F3_B_D_FOUNDER_DISPOSITION_CUSTODIED
```

---

## §0 — SUBJECT VERIFICATION (performed before any byte was written)

The bound artifact was re-read from custody at `356b089d` and recomputed:

```
observed:  483 lines · 26395 bytes · sha256 1bdb1a5828d230f3059c69b3705f27c5f8d22d712c2ba87b2b4154bf2c5f8a94
expected:  483 lines · 26395 bytes · sha256 1bdb1a5828d230f3059c69b3705f27c5f8d22d712c2ba87b2b4154bf2c5f8a94
```

**MATCH.** The rulings below are bound to *these exact bytes*, not to a gate
name. `RatificationBindsEvidenceState` — a disposition signs an evidence
lineage, never a title.

```
LaterFounderDisposition != EarlierGateAuthorship
```

**F3-B is not rewritten.** It returned `F3_B_FOUNDER_DECISION_REQUIRED` and it
still says exactly that. This record is appended; it does not retro-fit F3-B to
appear as though it had contained these answers.

## §1 — D1 · 001 §4 `evaluation_route` — **`NARROW_AND_RATIFY_REMAINDER`**

Neither `RATIFY_AS_IS` nor `WITHDRAW_COMPLETELY`. The field survives; the
implication it carried does not.

### 1.1 The narrowed, ratified meaning

```
evaluation_route = DeclaredEvaluationRegime
```

It declares **which evaluation regime is intended or applicable.** That is the
whole of its ratified content — and it is exactly the one candidate meaning
F3-B §8 found survivable on governed bytes (candidate **A**,
*human-readable declaration only*).

### 1.2 Ratified permanently — what it does NOT establish

```
DeclaredEvaluationRegime != ActualEvaluatorIdentity
DeclaredEvaluationRegime != EvaluationOccurrence
Declaration              != Execution
RoutePresence            != MechanicalEvaluationOccurrence
```

and correspondingly `evaluation_route` establishes none of:
`ActualEvaluatorIdentity` · `EvaluationOccurrence` ·
`EvaluationExecutionWitness` · `EvaluationOutcome` · `FindingOutcomeStanding`.

### 1.3 The removed implication

**WITHDRAWN:**

> *"A contract without a declared `evaluation_route` is admissible as
> declaration, but its drift findings carry standing
> `NEVER_MECHANICALLY_EVALUATED`."* — 001 §4

Two **independent** grounds, either sufficient:

1. `NEVER_MECHANICALLY_EVALUATED` was expelled from the FindingOutcomeStanding
   surface at **F3-A1 §4.2**, mechanically — the value varied with a declaration
   property while the outcome it purported to describe stayed fixed. The
   implication's consequent has had no lawful home since.
2. **F3-B §9 / CASE A** established that declaration presence or absence cannot
   witness whether execution occurred. With the route absent, the cadence
   comparison **still executes**; the finding exists only because
   `silence > limit` was computed. The implication's antecedent never had the
   evidential force the consequent required.

**No replacement standing is minted by this act.** The three-value
FindingOutcomeStanding surface closed at F3-A1 §3 is untouched:
`FINDING` · `NOT_EVALUABLE(reason)` · `MISMATCH_OBSERVED`.

### 1.4 Ratification scope, stated exactly

001 §4 was `CLOSED_UNRATIFIED` (F3-A-N3). This act ratifies **the remainder** of
its `evaluation_route` content under the narrowing above. It does **not** ratify
001 §4 wholesale, and it touches no other §4 clause — cadence class, lawful
silence, hold exceptions, `pause_semantics: CLOCK_STOP`, freshness, evaluation
clock and the `NO CONTRACT → NOT_EVALUABLE` law all retain the standing they
already had. `NarrowRatification != WholesaleRatification`.

001 itself remains **byte-identical** at `c648f2f7…9384`. The narrowing lives
here.

## §2 — D2 · FOREIGN EVALUATION PROVENANCE — **`NO_FOREIGN_EVALUATION_PROVENANCE_JURISDICTION`**

For **current** ACTIMANIRUN.

### 2.1 What ACTIMANIRUN MAY do

Admit — as ordinary source material, at whatever evidence ceiling their
admission contract earns them — foreign evaluator **declarations**, foreign
evaluator **claims**, and foreign evaluation **artifacts**.

### 2.2 What ACTIMANIRUN MAY NOT do

Infer from any of that material: foreign evaluation **occurrence** · foreign
evaluator **identity as observed fact** · foreign **execution witness** ·
any **mechanically-evaluated standing**.

Unless a future, separately governed organ or protocol supplies admissible
evidence of those facts.

```
ForeignEvaluationDeclaration != ForeignEvaluationOccurrence
ForeignEvaluationClaim       != ForeignEvaluationWitness
SourceAdmission              != OccurrenceEstablishment
```

### 2.3 The purity boundary is the reason, and it is not to be widened

**ACTIMANIRUN's derivation purity must not be widened in order to observe
foreign evaluators.** F3-B §5.1 established that the impossibility is a
*consequence of sealed law* (001 §10 — no I/O in derivation), not an
implementation gap. Widening it to reach a foreign runtime would convert this
organ into an orchestrator, dispatcher, remote verifier, or foreign-runtime
witness system — none of which it is.

```
PurityOfDerivation is a JURISDICTION BOUNDARY, not a limitation to engineer around
```

### 2.4 Scope of the denial

This is a jurisdiction boundary **for this organ, in this generation.** It is
not a statement about OURSELF, and it does not deny that foreign evaluation
provenance is knowable by some future organ properly constituted for it.

```
OutOfJurisdiction != Unknowable
NotThisOrgan      != NotEver
```

## §3 — THE RATIFIED INTERNAL/FOREIGN SPLIT

This is the architecture the two rulings jointly establish.

```
                     EVALUATION PROVENANCE
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
      INTERNAL DERIVATION              FOREIGN EVALUATOR
              │                               │
     InputSetIdentity                 declaration admitted
   + CompilerVersion                          │
   + deterministic derivation                 ▼
   + reproducible replay              CLAIM / SOURCE DATA
   + durable RunRecord custody                │
              │                               ╳
              ▼                               │
      EvaluationOccurrence            NOT ACTIMANIRUN-ESTABLISHED
        ESTABLISHABLE                       OCCURRENCE
              │
              ▼
        RunRecord custody
```

**Internal lane — ratified as sufficient.** For ACTIMANIRUN's own deterministic
derivation, the five existing structures above **may establish internal
derivation occurrence within ACTIMANIRUN's own jurisdiction.** Four of the five
already exist and are ratified; the fifth (durable RunRecord custody) is
ratified at D-001C-02.3 and unbuilt.

**Do not mint a new `EvaluationExecutionWitness` primitive** unless future
falsification proves these existing structures insufficient.

```
MissingRepresentation ⇏ PermissionToMintNewPrimitive
```

**Foreign lane — closed.** Admission is permitted; conversion of admitted claims
into established occurrence is not.

## §4 — SUCCESSOR DISPOSITIONS

| Gate | Disposition under D1 + D2 |
|---|---|
| **F3-C** — `ActualEvaluator` representation | **`NOT_REQUIRED`** unless later evidence establishes a new necessity. Internally `derivation_version` already is the evaluator identity; externally it is out of jurisdiction |
| **F3-D** — evaluation execution witness | **`NOT_REQUIRED`** for internal derivation (replay determines occurrence) · **`OUT_OF_CURRENT_JURISDICTION`** for foreign evaluation |
| **F3-E** — route-mismatch standing | **`NOT_REQUIRED`** under the current foreign-provenance boundary. It presupposed that a declared route asserts something about the evaluator; D1 rules that it does not, so a mismatch has nothing to be a mismatch *of* |

**Three prospective gates dissolved — not deferred, not deleted by fiat.** Each
was an artifact of a jurisdiction assumption that D2 has now denied.

```
DeeperAnalysis -> LessArchitecture
NecessityUnproven != Impossible
```

They remain available if future falsification re-establishes necessity.

## §5 — D3 · RUNRECORD DURABLE CUSTODY

```
RunRecordStore = ALREADY_GOVERNED (D-001C-02.3) = UNBUILT
```

**Materially different from `NEW_PRIMITIVE_CANDIDATE`.** No further Genesis
debate is required for it: D-001C-02.3 already ratified the append-only
RunRecord store, co-located with the bounded compiler host and forbidden from
OMR/OSM. What is missing is **physical, not ontological.**

**D3 is NOT authorized by this token.** Its standing is
`ALREADY_RATIFIED_IMPLEMENTATION_OBLIGATION, UNBUILT, UNAUTHORIZED`.

**Founder sequencing ruling recorded:** D3 precedes 003B. Reason recorded as
given — once ACTIMANIRUN begins mechanically acquiring live sources, the first
mechanically acquired run must not exist only ephemerally, when the system has
already established that RunRecord custody is how internal evaluation occurrence
becomes reconstructible.

```
AcquiredReality without PreservedRun = the acquisition disproves itself
```

## §6 — CC-1 STANDING — **SEMANTIC CONSEQUENCE NOW DETERMINATE**

CC-1 (`cadenceDrift` emits `NEVER_MECHANICALLY_EVALUATED`, outside the closed
outcome surface) **remains OPEN as an implementation matter and is NOT repaired
here.**

But its disposition is no longer an open question. With D1 withdrawing the
implication, the ternary's false branch has **no governing clause at all**, and
the lawful outcome follows from bytes already ratified at **F3-A1 §6**, whose
applicability matrix gives MOVEMENT_CADENCE exactly two members:

| class | FINDING | NOT_EVALUABLE(reason) | MISMATCH_OBSERVED |
|---|---|---|---|
| MOVEMENT_CADENCE | silence exceeds contract, no active hold exception | `NO_APPLICABLE_CONTRACT` | n/a |

Route presence appears **nowhere** in that ratified matrix as a discriminator.
A cadence finding is produced only when the comparison was performed and the
norm violated — which is precisely F3-A1 §3.1's definition of `FINDING`.

```
CC-1 repair is now DETERMINED BY ALREADY-RATIFIED LAW, not by a pending decision.
What remains is the ACT, not the ANSWER.
```

No new standing is introduced to replace the withdrawn value, and none is
needed. **The repair itself requires its own authorization.**

## §7 — CONSEQUENCE FOR 003A-F3 (recorded, not acted on)

003A-F3 — *"a non-empty `evaluation_route` confers mechanical-evaluation standing
without proving the declared route corresponds to the evaluator that actually
ran"* — is **`DISSOLVED_BY_NARROWING`**, not repaired.

Under D1 the route no longer confers mechanical-evaluation standing on anything,
so the mismatch it identified has lost the significance that made it a defect.
`DefectDissolvedByLawChange != DefectRepairedInCode`.

**Consequence flagged, deliberately not acted on:** GOVERNANCE-BINDING.md records
the two stale `actimanirun-derive/v0.1` route strings in fixtures as *"evidence
in that adjudication and must not be tidied."* That adjudication has now
concluded. Whether those strings retain evidentiary status is a **separate
bounded act** on the host's own declaration surface, and this gate does not
touch it. `EvidenceOfMismatch != PermissionToRepairMismatch` still governs until
that act occurs.

## §8 — 003B STANDING

**`BLOCKED`.** Unchanged by this act. Under §5's sequencing, D3 stands between
it and authorization.

## §9 — FIREWALLS HONOURED

```yaml
implementation_mutation: NONE — host d1de631e clean, tree e162ee89 unchanged
compiler_version:        actimanirun-derive/v0.3 — unchanged
tests:                   63 passed / 0 failed — unchanged
adapters:                0
D3_build:                NOT PERFORMED, NOT AUTHORIZED
CC-1_repair:             NOT PERFORMED, NOT AUTHORIZED
F3-C / F3-D / F3-E:      NOT OPENED (dispositioned as NOT_REQUIRED / OUT_OF_JURISDICTION)
003B:                    NOT OPENED
N1 / N2:                 UNTOUCHED
push:                    NONE
predecessors:            F3-B, F3-A1, F3-A, 001 all byte-identical; this record is appended
```

Nothing minted: no `ActualEvaluator`, no `EvaluationExecutionWitness`, no
`RouteCompatibility`, no replacement standing value, no new drift class, no new
authority.

### VERDICT: **F3_B_D_FOUNDER_DISPOSITION_CUSTODIED**

## §10 — NEXT LAWFUL GATE

```
ACTIMANIRUN-D3 — RUNRECORD DURABLE CUSTODY IMPLEMENTATION
```

Eligible to be proposed; **not authorized** by this token; requires its own
Founder act. It is an implementation obligation under already-ratified
D-001C-02.3, not a Genesis question.

Thereafter, in the sequence the Founder fixed: CC-1 implementation conformance,
then 003B mechanical Git acquisition.

## §11 — STOP

STOP after D1/D2 custody. No implementation · no D3 build · no CC-1 repair ·
no N1/N2 repair · no F3-C/D/E · no 003B · no adapter · no CompilerVersion change ·
no push · no CODEXSELF contact · no successor self-authorized.
`ClaudeSELFRuntimeReality != CodexSELFRuntimeReality`.
