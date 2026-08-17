# ACTIMANIRUN-F3-B — EVALUATION PROVENANCE GENESIS AND FALSIFICATION

```yaml
record_class: SEMANTIC_GENESIS_AND_FALSIFICATION_RECORD
gate: ACTIMANIRUN-F3-B
authorization_token: AUTHORIZE_ACTIMANIRUN_F3_B_EVALUATION_PROVENANCE_GENESIS_AND_FALSIFICATION_ONLY
authority_source: MYSELF (Founder transmission act, 2026-08-17)
executed_by: CLAUDESELF (Claude Code session 1ed7a1da-0ad5-493f-9f62-03d5c85fd2a6)
lease_scope: >
  Bounded lease for gate F3-B only: read-only inspection of governed bytes and
  read-only out-of-tree invocation of the already-built compiler, plus custody
  of this single governance record. NO implementation mutation authorized or
  performed. Expires at STOP.
recorded_at_utc: 2026-08-17T22:25:37Z
prime_question: >
  What must be witnessed before ACTIMANIRUN may claim that a particular rule was
  mechanically evaluated under a declared evaluation regime?
custody_channel:
  branch: governance/actimanirun-000-custody
  governance_parent: 19529f882b0486165d26003f86e5ec60dc7d9b5a
  commit_hash: WITNESSED_IN_GATE_REPORT
  remote_publication: NOT_AUTHORIZED_THIS_GATE
observed_implementation:
  host_head: d1de631efcba5ed6718c19bdd368ad9625dc61ea
  executable_implementation: 5b78ed5d4dffc5875d3e6c6554ba29c8e80794a7
  compiler_version: actimanirun-derive/v0.3
  tests: 63 passed / 0 failed
  adapters: 0
  mutation_by_this_gate: NONE
necessity_test_result: NO_NEW_PRIMITIVE_SURVIVES
new_primitive_minted: NONE
verdict: F3_B_FOUNDER_DECISION_REQUIRED
```

---

## §1 — LIVE CUSTODY COORDINATES (observed, not installed)

| | expected | observed | |
|---|---|---|---|
| host HEAD | `d1de631e…61ea` | identical | MATCH |
| executable implementation | `5b78ed5d…94a7` | `git log -1 --format=%H -- src/` | MATCH |
| CompilerVersion | `actimanirun-derive/v0.3` | `src/derive.mjs:31` | MATCH |
| tests / adapters / remotes | 63-0 / 0 / — | 63-0 / 0 / 0 | MATCH |
| governance HEAD | `19529f88…9b5a` | identical, worktree clean | MATCH |

No drift. `STOP_REALITY_RECONCILIATION_REQUIRED` not triggered.

## §2 — GOVERNED CLAUSES INSPECTED (bytes, at HEAD)

`001 §0` · `001 §4` · `001 §10` · `001 §11` · `001C D-001C-01` · `D-001C-02.1/.2/.3` ·
`D-001C-04` · `D-001C-07` · `F3-A` (all) · `F3-A1` (all) · `F3-A1-R` (all) ·
`REVIEW-001` (all) · host `GOVERNANCE-BINDING.md` · host `LEDGER.md`.

**The single governing clause for the subject of this gate — 001 §4, verbatim:**

> *"`evaluation_route: <declared mechanical evaluation path>`"*
>
> *"DOCUMENTED_CONTRACT != EVALUATED_CONTRACT (empirical law of this estate:
> every hand cadence contract on record failed compliance). A contract without a
> declared `evaluation_route` is admissible as declaration, but its drift
> findings carry standing `NEVER_MECHANICALLY_EVALUATED`."*

That is the **entire** governed definition. There is no other occurrence of the
token in the corpus (F3-A §2 established this, and it re-verifies).

### 2.1 — F3-A-N3 IS LOAD-BEARING AND MUST BE STATED FIRST

**001 §4 is `CLOSED_UNRATIFIED`.** 001A's scope firewall expressly left §4–§13
unratified; D-001C-01 ratified the cadence contract's **canonical name only**
(`RATIFIED_NAME`), never its content.

```
ClauseSealed != ClauseRatified
```

Every conclusion below is therefore an analysis of an **unratified clause**. This
gate can establish what that clause *can* and *cannot* mean, and what the
machine can and cannot witness. It cannot ratify §4, and it does not.

### 2.2 — THE SEAM F3-A1 OPENED

001 §4's sole mechanical consequence assigns the value
`NEVER_MECHANICALLY_EVALUATED` to a *drift finding's standing*. F3-A1 §4.2
**removed that value from the FindingOutcomeStanding surface**, proving
mechanically that it varies with a declaration property while the outcome it
purports to describe is fixed:

```
OutcomeStanding      != EvaluationProvenance
DeclaredRouteAbsent  != MechanicalEvaluationAbsent
```

So 001 §4's only operative rule now points at a value with no lawful home on the
dimension §4 assigned it to. **That seam is this gate's subject.**

## §3 — CURRENT `evaluation_route` SEMANTICS, AS BUILT

Mechanically inventoried at `5b78ed5d` (static + dynamic, read-only):

```
occurrences in src/:      1   — src/derive.mjs :: cadenceDrift
occurrences in run.mjs:   0
occurrences in project.mjs: 0
occurrences in admit.mjs: 0
```

The sole site is a **truthiness test**:

```js
standing: contract.evaluation_route ? 'FINDING' : 'NEVER_MECHANICALLY_EVALUATED'
```

**The route is read once, used as a boolean, and discarded.** It is never
compared to anything, never resolved, and — verified by scanning the full
serialized output of a live run — **never appears in DERIVED_CONTENT, the
RunRecord, or the Projection**:

```json
{"route_in_output": false, "evaluator_field": false, "occurrence_field": false}
```

```
DeclaredValue != RetainedProvenance
```

## §4 — RUNRECORD PROVENANCE CAPABILITY (measured)

```
run_identity · observation_boundary · input_set_identity · source_snapshot_refs ·
source_health · evaluation_reference_time · evaluation_time · derivation_version ·
projection_digest · coverage_witness · run_status
```

Compiler-identity fields: exactly **one** (`derivation_version`) — the invariant
003A-X sealed and F3-A1-R preserved. What the RunRecord **does not** carry: any
route, any evaluator identity other than the derivation core's own version, any
per-rule attribution, any evaluation count, and **the admitted bytes themselves**
(it carries `input_set_identity`, a digest, plus snapshot refs).

```
DigestOfInputs != Inputs
```

## §5 — P1–P10 REPRESENTABILITY / ESTABLISHMENT MATRIX

Grades: **A** representable · **B** establishable · **C** derivable reproducibly ·
**D** inferable by convention only · **E** impossible.

| | Proposition | Internal evaluator (ACTIMANIRUN itself) | Foreign evaluator (what a route names) |
|---|---|---|---|
| P1 | which regime was declared | **A** — frozen in the admitted contract. **not B**: no schema, no resolution, no authority; §4 unratified | **A** identically — a declaration is a declaration regardless of who it names |
| P2 | which evaluator executed | **A+B** via `derivation_version` (003A-X: it identifies the logic that ran) | **E** — see §5.1 |
| P3 | which exact rule/predicate | **D only** — the finding's `rule` field is free prose (`"monotonic silence exceeds contract with no active hold exception"`), not a resolvable identifier | **E** |
| P4 | against which contract | **A** — `cadence_contract_ref` on the manifestation; on the finding itself only as prose inside `expected` | **A** (declaration) |
| P5 | against which admitted inputs | **A** by digest; **B** only if the inputs are re-obtainable | **A** by digest |
| P6 | inside which run | **A+B** — `run_identity` | **A+B** |
| P7 | at what evaluation time | **A+B** for the RUN. `EvaluationTime(run) != EvaluationTime(rule)` — no per-rule timestamp exists | **E** |
| P8 | **did evaluation actually occur** | **C, not A** — derivable by replay, represented nowhere. See §6 | **E** |
| P9 | what outcome | **A+B** when a finding is emitted; **ambiguous on absence** — see §7 | **E** |
| P10 | can another evaluator replay | **C, conditionally** — requires the AdmissionRecord, which the RunRecord does not carry | **E** |

### 5.1 — WHY THE FOREIGN COLUMN IS `E`, STRUCTURALLY

001 §10 makes the derivation phase a **pure function** — no I/O, no clock, no
network — and the implementation enforces this by function signature. Therefore
**ACTIMANIRUN cannot, from inside derivation, resolve, contact, or verify any
evaluator it does not itself execute.** Measured: a contract declaring
`evaluation_route: foreign-evaluator://some-other-organ/v2` produces standing
`FINDING`, byte-identical to a self-referential route, with no resolution
attempted.

This is not an implementation gap. It is a **consequence of a sealed law**.

```
PurityOfDerivation -> ForeignEvaluationOccurrence is UNWITNESSABLE from inside derivation
```

## §6 — CASE E · THE DECISIVE FALSIFICATION — **CONFIRMED**

Mandatory hostile specimen, run against the live v0.3 compiler. In every case
the declared route resolves, the evaluator is compatible, coverage is
sufficient, and the outcome is otherwise computable:

```
E1  route+evaluator compatible · rule NEVER RAN (hold suspends the clock)   -> NO FINDING
E2  route+evaluator compatible · rule RAN and was SATISFIED                 -> NO FINDING
E3  route+evaluator compatible · rule NEVER RAN (no lawful-silence limit)   -> NO FINDING

E1 == E3 derived-drift bytes: true
E2 == E3 derived-drift bytes: true
```

**ACTIMANIRUN cannot distinguish an evaluation that never happened from an
evaluation that happened and passed.** Both are represented by the same thing:
nothing.

```
RouteMatch      != EvaluationOccurred     — MECHANICALLY DEMONSTRATED
NoFindingEmitted != EvaluationOccurredAndPassed
```

**This is the same law F3-A1-R closed one level down, recurring one level up.**
There, `NoFindingEmitted != NothingToReport` was closed on the *outcome*
dimension for EVIDENCE_INTEGRITY. Here the identical ambiguity reappears on the
*provenance* dimension for cadence. Silence is overloaded twice in this compiler
for the same structural reason: **absence is being used to carry meaning.**

Not repaired. No execution witness invented. (WFC §7 honoured.)

## §7 — CASES A–L · FULL RESULTS

| Case | Specimen | Emitted standing | Reading |
|---|---|---|---|
| **A** | declared route **absent**, silence exceeded | `NEVER_MECHANICALLY_EVALUATED` | **the comparison DID execute** — the finding exists only because `silence > limit` was computed. Only the *declaration* was absent. See §9 |
| **B** | route `not-a-compiler-at-all` | `FINDING` | a syntactically valid, semantically nonexistent route is indistinguishable from a correct one |
| **B2** | route `actimanirun-derive/v9.9` (no such compiler) | `FINDING` | same |
| **C** | route names `v0.1`, evaluator **is** `v0.3` | `FINDING` | declared/actual mismatch is invisible. `DeclaredEvaluationRegime != ActualEvaluatorIdentity` confirmed unrepresented |
| **D** | route matches the running compiler exactly | `FINDING` | **identical output to B, B2, C** — only *presence* is tested |
| **E** | compatible, evaluation never executes | (see §6) | **decisive** |
| **F** | executes, outcome not establishable | `FINDING` | with no admitted claims the silence clock falls back to `contract.effective_from`; a finding is produced from a *default*, not from an observed movement |
| **G** | replay under a different CompilerVersion | `FINDING` | standing identical to the v0.3 run. Nothing binds an evaluation to the evaluator that performed it |
| **H** | same class evaluated 3× in one run | 3 findings | no evaluation count; findings separable only by `manifestation_ref` |
| **I** | one evaluator, 3 rules, one run | 3 findings | **zero per-rule evaluator attribution**; one `derivation_version` covers all |
| **J** | route `ANY-STRING-AT-ALL` | `FINDING` | no resolution mechanism exists, so any string satisfies the test. Two evaluators could claim one route; one evaluator could claim many; neither is representable |
| **K** | provenance completeness of a real finding | — | the finding carries `expected`/`observed`/`rule` as **prose**. `rule` is a sentence, not a reference. `PROSE != RESOLVABLE_REFERENCE` |
| **L** | **source declares "CADENCE_RULE_WAS_MECHANICALLY_EVALUATED_BY_US"** | admitted, **0 rejections** | **structural gap — see §7.1** |

### 7.1 — CASE L IS A REAL FINDING (F3-B-N1)

D-001C-07 rejects an envelope carrying any of five axis fields
(`movement_pulse`, `hold_context`, `attention_state`, `drift_standing`,
`institutional_standing`). **An evaluation-occurrence claim is not among them.**
A source asserting that an evaluation occurred is admitted without objection.

```
SourceClaimOfEvaluation != EvaluationOccurrence
```

That law currently holds **only because ACTIMANIRUN does not read such a field**
— not because admission forbids one. It is protected by silence, not by
structure. The exact species D-001C-07 exists to prevent
(`AdapterObservation != ProjectionConclusion`), one dimension over.

**Recorded, not repaired.** Whether the admission guard should be widened is a
D-001C-07 matter, not an F3-B matter — a different owning clause.

## §8 — `evaluation_route` CANDIDATE-MEANING ATTACK

For each candidate: what proposition does it assert, who declares it, how is it
resolved, what proves it was used, what happens when it is unresolved or wrong.

| # | Candidate meaning | Verdict |
|---|---|---|
| **A** | human-readable declaration only | **SURVIVES.** Asserts "a mechanical evaluation path is claimed to exist." Declared by the contract's `authority_ref`. Resolution: none needed. Nothing proves use — and under this reading nothing needs to. Consistent with the estate's empirical law `DOCUMENTED_CONTRACT != EVALUATED_CONTRACT`, and with the implementation, which uses it as a boolean. **The only candidate the built system actually implements.** |
| **B** | logical route identifier | **UNESTABLISHED.** Requires a namespace, a registry, and an identity law. None exists in the corpus. Would need genesis of a naming authority — outside F3-B's grant |
| **C** | executable evaluator identity | **FALSIFIED — structurally.** §5.1: derivation is pure; ACTIMANIRUN can never establish that a named executable ran. Would also collide with `derivation_version`, which already *is* the identity of the evaluator ACTIMANIRUN executes |
| **D** | evaluation method identifier | **UNESTABLISHED.** A method vocabulary exists nowhere. The nearest governed analogue, `effect_evaluation_rules.method: DECLARED_EVIDENCE_PREDICATE`, is contract-side, typed, and **already works** — evidence that when this corpus means "method" it says so, in a different field |
| **E** | dispatch / routing address | **FALSIFIED.** Dispatch implies I/O. 001 §10 forbids I/O in derivation. An address ACTIMANIRUN may never dial is not an address |
| **F** | versioned evaluation-regime reference | **UNESTABLISHED, and dangerous.** The historical fixture strings (`actimanirun-derive/v0.1`) *look* like CompilerVersion values. `LexicalEquality != SemanticIdentity`. 003A-X §8 already measured that nothing compares the two, and GOVERNANCE-BINDING records those strings as **evidence that must not be tidied**. Treating resemblance as identity would launder a coincidence into a law |

**Result: only candidate A survives on governed bytes.** Under A, `evaluation_route`
asserts nothing about occurrence at all — which makes 001 §4's consequence
clause (findings "carry standing `NEVER_MECHANICALLY_EVALUATED`") an
overstatement of what its own field can support.

```
CompilerVersion != EvaluationRoute
Declaration     != Execution
Configuration   != Witness
```

## §9 — CC-1 SEMANTIC DISPOSITION

**What was `NEVER_MECHANICALLY_EVALUATED` unsuccessfully trying to represent?**

CASE A settles it mechanically. When the route is absent, the cadence comparison
**still executes** — the finding exists *only* because `silence > limit` was
computed. The token therefore never described evaluation occurrence. It
described **the absence of a declared route on the contract**.

### Disposition: **DECLARATION PROVENANCE — and it is already represented.**

Of the six candidates the WFC named:

| Candidate | Verdict |
|---|---|
| **declaration provenance** | **YES — this is the referent** |
| evaluator provenance | no — the evaluator was ACTIMANIRUN in every branch |
| evaluation occurrence | **no — falsified by CASE A**: evaluation occurred in both branches |
| evaluation coverage | no — coverage is `CoverageWitness` (D-001C-08), a different, existing object |
| evaluation execution witness | no — nothing about execution varies between the branches |
| **unnecessary: existing facts suffice** | **YES, jointly** — see below |

The fact the token encodes is `contract.evaluation_route ∈ {present, absent}`.
That fact is **already in the admitted AdmissionRecord**, frozen, and reachable
by any consumer of the run. It needs no representation on the finding, and it
was never a property of the finding.

```
ContractDeclarationCompleteness != FindingOutcome
AbsenceOfDeclaration            != AbsenceOfEvaluation
```

**Semantic disposition returned; no implementation repair performed or
authorized.** The lawful implementation consequence — that the branch has no
home on the outcome surface — was already established at F3-A1 §8 (CC-1) and
remains open there.

## §10 — NECESSITY TEST · MODELS A → D

| Model | Attempt | Result |
|---|---|---|
| **A** — existing objects suffice | for P1, P2-internal, P4, P5, P6, P7-run, P9-emitted | **SURVIVES** for those propositions |
| **B** — bounded extension of an existing object | for P8-internal and P10: the missing capability is **input custody**, not a new concept. D-001C-02.3 already **ratifies** an append-only RunRecord store in the compiler host; it is simply **UNBUILT** (003A-X §6 established `NO_PERSISTED_LEGACY_ADMISSION_RECORD`, SCOPED_NULL). Given the AdmissionRecord, re-derivation is byte-identical to the original run — measured | **SURVIVES — and requires no new semantics, only construction of an already-ratified store** |
| **C** — a derived relation suffices | P8-internal is a *derived* property of `(AdmissionRecord, derivation_version)` under a pure function. Replay is the relation | **SURVIVES for the internal lane** |
| **D** — a genuinely new object is irreducibly necessary | reached only for the **foreign** lane (P2/P3/P7/P8/P9/P10 = `E`) | **NOT ESTABLISHED — because the foreign lane's jurisdiction is unresolved (§11). A primitive cannot be proven necessary for work that has not been established as ACTIMANIRUN's to do** |

### **NECESSITY TEST RESULT: `NO_NEW_PRIMITIVE_SURVIVES`.**

Nothing was minted. Not `ActualEvaluator`, not `EvaluationExecutionWitness`, not
`RouteCompatibility`, not `PULSE_ELIGIBLE`, not any evaluation-provenance object,
field, or standing value.

```
MissingRepresentation ⇏ PermissionToMintNewPrimitive
Convenience           != Necessity
```

### 10.1 — THE ANSWER TO THE PRIME QUESTION

> *What must be witnessed before ACTIMANIRUN may claim that a particular rule was
> mechanically evaluated under a declared evaluation regime?*

**The question has two answers, and 001 §4 conflates them into one field.**

```
IF the evaluator is ACTIMANIRUN itself:
    occurrence is not witnessed — it is REPLAYED.
    Required: the AdmissionRecord, the derivation_version, and the purity law.
    Two of the three exist and are ratified; the third (custody of the admitted
    bytes) is ratified at D-001C-02.3 and unbuilt.
    NOTHING NEW IS NEEDED. A witness object here would re-represent a fact the
    pure function already determines.

IF the evaluator is anyone else:
    occurrence CANNOT be witnessed from inside derivation, at all, by the sealed
    purity law. ACTIMANIRUN could only ADMIT A FOREIGN DECLARATION that an
    evaluation occurred — which is a declaration, not a witness, and CASE L shows
    admission currently accepts one unguarded.
```

**That bifurcation is the finding.** The reason evaluation provenance felt like a
missing object is that a single field has been carrying a foreign-evaluator
concept inside a compiler whose derivation law forbids ever meeting a foreign
evaluator.

## §11 — EXACT UNRESOLVED FOUNDER DECISIONS

**F3-B-D1 · Ratify, narrow, or withdraw 001 §4's `evaluation_route`.**
Its defining clause is `CLOSED_UNRATIFIED` (F3-A-N3). Only candidate meaning
**A** survives (§8). Under A, the clause's consequence sentence overstates what
the field can support. Options: ratify as declaration-only; narrow the
consequence clause; or withdraw the field. **ACTIMANIRUN cannot decide this — a
gate may not ratify the clause it is interpreting.**

**F3-B-D2 · Does ACTIMANIRUN's jurisdiction include FOREIGN evaluation provenance
at all?**
F3-A1's Founder ruling C-1 granted ACTIMANIRUN the per-finding **OUTCOME-STANDING**
vocabulary, scope "ACTIMANIRUN projection semantics only." F3-A1 §4.2 then
established that evaluation provenance is a **different dimension**, explicitly
undecided. C-1 does not reach it.

```
LocalOutcomeStandingAuthority != EvaluationProvenanceAuthority
```
If **NO** — the foreign lane closes permanently; F3-C/D/E are unnecessary; only
D1 and the CC-1 implementation consequence remain.
If **YES** — the foreign lane needs an admission-side design (D-001C-07's guard,
per §7.1), because derivation can never reach it.

**F3-B-D3 · Build the ratified RunRecord/AdmissionRecord store?**
D-001C-02.3 ratifies it; it does not exist. Without it, P8/P10 are derivable in
principle and unreplayable in practice, because `DigestOfInputs != Inputs`.

## §12 — RELATIONSHIPS PRESERVED

**To `derivation_version`:** it is the identity of the evaluator ACTIMANIRUN
executes — the *only* evaluator identity the system can establish. It is **not**
an evaluation route and must not absorb one. `LexicalEquality != SemanticIdentity`.

**To RunRecord:** the RunRecord is the record of the evaluation **ACT**, already
carrying run identity, input-set identity, version, and time. It is the correct
future home for any internal-lane provenance, because provenance of ACTIMANIRUN's
own derivation is derived-plane content and D-001C-02.3 forbids custodying it in
a declaration organ.

**To DriftFinding:** unchanged. `FindingOutcomeStanding` remains closed at three
(`FINDING` · `NOT_EVALUABLE(reason)` · `MISMATCH_OBSERVED`) and this gate adds
nothing to it. F3-A1's dimensional separation is reaffirmed, not revised:

```
FindingOutcomeStanding != ClaimStanding != FindingClassStanding
                       != InstitutionalStanding != GeneralEpistemicStanding
                       != EvaluationProvenance
```

**Failure states named, unminted:** route unresolved · route resolvable but
unused · declared ≠ actual evaluator · evaluation skipped by short-circuit ·
evaluation performed with a defaulted operand (CASE F) · foreign claim of
evaluation (CASE L). Each is a *state*; none is granted a representation here.
`RejectedToken ⇏ NonexistentState` (F3-A1 §4.1 idiom, carried).

**Authority ceiling:** this gate ratifies nothing, alters no Drift doctrine, mints
no external authority, repairs no source, and touches no foreign organ.
`MoreCognition != MoreAuthority` · `SemanticClosure != ImplementationAuthorization`.

## §13 — FUTURE IMPLEMENTATION SURFACE (returned, NOT performed)

If and only if D1/D2 authorize it, the **minimum** surface, in dependency order:

1. **Nothing at all** if D2 = NO and D1 = "declaration-only" — the internal lane
   already works; CC-1's disposition is then a §4 consequence-clause repair,
   which is governance text, not code.
2. **CC-1 implementation consequence** — one branch in
   `derive.mjs :: cadenceDrift` (the `evaluation_route ? … : …` ternary). It
   currently emits a value outside the closed outcome surface. Its lawful
   replacement follows from D1, not from this gate.
3. **RunRecord store** (D-001C-02.3, already ratified, unbuilt) — enables P8/P10
   replay. New host surface; no new semantics.
4. **Admission guard** for foreign evaluation claims (§7.1) — only under D2 = YES;
   owned by D-001C-07, not by this gate.

No file was named as a write target and no write set is declared, because none
is authorized.

## §14 — PROOFS

```yaml
implementation_mutation:  NONE — `git status --porcelain` empty at gate close;
                          host HEAD d1de631e unchanged; all analysis performed by
                          out-of-tree scripts importing the built modules read-only
adapters:                 0 files matching *adapter* (unchanged)
compiler_version:         actimanirun-derive/v0.3 — unchanged, not incremented
tests:                    63 passed / 0 failed — unchanged
N1_N2:                    UNTOUCHED — project.mjs byte-identical; no reason-field
                          retrofit; PresentationDebt != EvaluationProvenanceDebt
003B:                     CLOSED — no adapter, no acquisition, not opened
F3_C_D_E:                 NOT OPENED
push:                     NONE — host has 0 remotes; governance branch not pushed
predecessors:             no governed byte modified; this record is appended
```

## §15 — SUCCESSOR NECESSITY

| Gate | Necessary? |
|---|---|
| **F3-C** (`ActualEvaluator` representation) | **NOT ESTABLISHED.** For the internal lane `derivation_version` already is it. For the foreign lane it is unreachable by the purity law. **Contingent on D2 = YES**, and even then it belongs to admission, not derivation |
| **F3-D** (execution witness) | **NOT ESTABLISHED — and falsified for the internal lane.** Replay determines occurrence; a witness object would re-represent what the pure function already fixes. Contingent on D2 = YES |
| **F3-E** (route-mismatch standing) | **NOT ESTABLISHED.** It presupposes route resolution (candidate B/C/F), all unestablished or falsified. F3-A §9's bar — *"new standing design is NOT currently lawful"* — is not lifted by this gate |

`NecessityUnproven != Impossible` — each remains available if D1/D2 resolve
toward them. None is authorized now.

### VERDICT: **F3_B_FOUNDER_DECISION_REQUIRED**

The prime question is **answered** (§10.1) and the necessity test is **closed**
(`NO_NEW_PRIMITIVE_SURVIVES`). What cannot be closed here is the ratification of
the clause under analysis and the jurisdiction of the foreign lane — both
Founder acts. Recording that honestly rather than manufacturing closure is the
required behaviour under this gate's §15.

## §16 — NEXT LAWFUL GATE

The Founder decisions **F3-B-D1** and **F3-B-D2**. Nothing in F3-C/D/E or 003B is
decidable before them. `003B` remains BLOCKED.

## §17 — STOP

STOP after this semantic/falsification custody. Conclusion not implemented ·
F3-C/D/E not opened · 003B not opened · no adapter · CompilerVersion unchanged ·
CC-1 not repaired · N1/N2 not repaired · no push · no CODEXSELF contact · no
successor self-authorized. `ClaudeSELFRuntimeReality != CodexSELFRuntimeReality`.
