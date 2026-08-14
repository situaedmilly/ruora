# F-05 — NORMALIZED OBSERVATION VOCABULARY
## Design Adjudication Packet v0.2 — Revision Pass

**STATUS** Design-only revision. Unratified. Unsealed. Not merged into the protocol.
**GOVERNING REPAIR SPECIFICATION** `OURSELF-RCP-F05-R02-FINDING-DISPOSITION-REPAIR-SPEC.md` (`8b8bd4de…c12d28d2`)
**SUPERSEDES (does not replace on disk)** `…ADJUDICATION-v0.1.md` (`b5c3a20e…c40e9`)
**AUTHORITY** Vocabulary and contract revision only. Not ratification, not sealing, not protocol revision, not implementation, not RC-0001 execution.

**LINEAGE**
```
RCP v0.1 draft         1aa3698c…38c776    UNCHANGED — not modified by this revision
Cold Review 001        082b6cb8…939fe9a   UNCHANGED
F-05 packet v0.1       b5c3a20e…c40e9     UNCHANGED — preserved, see §0.1
F05-R01                0420da3b…461a92ae  UNCHANGED
F05-R02                8b8bd4de…c12d28d2  UNCHANGED — governs this revision
HBC baseline           e350205            UNCHANGED — not read for mutation
```

---

## 0. Identity, lineage, and what this revision is

### 0.1 Why v0.1 was preserved rather than edited

v0.1 is bound by digest into two downstream records: F05-R01 declares it as its subject of record, and F05-R02 disposes fourteen findings against that exact text. Editing v0.1 in place would leave both records pointing at bytes that no longer exist, silently breaking the lineage chain they were written to establish.

This revision is therefore a **new artifact**. v0.1 remains on disk, byte-identical, as the object F05-R01 actually reviewed. Where this document changes something, the change is traceable in §15 to the finding that required it.

### 0.2 Authorship declaration — unchanged from v0.1

This revision is written by the same party that authored v0.1 and the protocol draft. It carries the same defect declared in v0.1 §0.1 and in F05-R01 §0: `SELF-DRAFTED ≠ INDEPENDENTLY ADJUDICATED`. Repairs written by the party whose defects were found are exactly the repairs most likely to preserve the assumption that produced the defect. Nothing here is ratified by having been written; F05-R03 re-review exists precisely because this document cannot certify itself.

### 0.3 The quality bar this revision was held to

F05-R02 transformed the task. The bar is not *improve the vocabulary*. It is:

> Remove every currently known way a normalized observation can acquire semantic, epistemic, provenance, authority, projection, or falsification meaning through an ungoverned channel.

Every section below is written against that bar. Where a channel remains open, it is named as open (§17), not left to be discovered.

### 0.4 What this revision does not do

It does not ratify the six-kind basis. It does not resolve NF-01, NF-02, or NF-03. It does not modify the base protocol, even where §7 and §17 identify a protocol-level gap. It does not decide whether `CANONICAL` is one dimension or two.

---

## 1. The observation-kind basis

### 1.1 The basis

```
PRIMITIVE KINDS (5)
  STATE                an entity's current classification
  TRANSITION_RESULT    the outcome of an attempted state transition
  COLLECTION           aggregate cardinality of a declared set
  PERSISTENCE          the durability tier an entity's value achieves
  ORDER                sequence position within a stimulus run

DERIVED KIND (1) — CONTESTED
  OBLIGATION           see §1.3
```

Six kinds. No seventh kind is added by this revision.

**INV-OBS-KIND-1.** `observable_kind` SHALL be drawn only from the six above. A target that emits any other value for this field has emitted an invalid observation, not a surplus one.

### 1.2 Orthogonal dimensions are not kinds

F05-R01 surfaced several concerns that could have been "solved" by adding observation kinds. Each is instead handled as a dimension orthogonal to kind:

| Dimension | Where it lives | Not a kind because |
|---|---|---|
| subject / identity | `entity_ref` (§4) | it names what an observation is *about* |
| observation presence | `observation_status` envelope (§2) | it is epistemic status, not semantic content |
| ancestry / provenance | Observation Projection Contract SSM output (§9) | it records where a reading came from |
| authority | **not owned by F-05** (§3) | see D-01 disposition, §3 |
| stimulus | stimulus obligations (§7) | it is what is *applied*, not what is observed |

```
                    NormalizedObservation
                            │
        ┌───────────┬───────┴───────┬───────────┐
        ▼           ▼               ▼           ▼
     SUBJECT     PRESENCE      OBSERVABLE    ANCESTRY
   entity_ref  observation_      KIND        (SSM, §9,
                 status       one of six    companion
                                  │          record)
                                  ▼
                                VALUE
                          legal only when
                          status = OBSERVED
```

### 1.3 OBLIGATION — explicit status, not silent retention

F05-R01 (F05R01-11) demonstrated that OBLIGATION's grounding case decomposes without loss into `COLLECTION.count` + a RealityIR-declared constant + `STATE`. F05-R02 required this revision to make an explicit either/or choice rather than retain OBLIGATION by inertia.

**Choice made: RETAIN, reclassified as DERIVED and marked CONTESTED.**

**INV-OBS-OBL-1.** OBLIGATION is a **derived** kind. It SHALL be defined as exactly:

```
OBLIGATION(e) ≡  met       = COLLECTION.count of the declared satisfying set
                 required  = a RealityIR-declared constant (not an observation)
                 satisfied = STATE ∈ {SATISFIED, UNSATISFIED}, where
                             SATISFIED ⟺ met ≥ required
```

**INV-OBS-OBL-2.** Because OBLIGATION is derived, a divergence in an OBLIGATION slot SHALL be reproducible as a divergence in its constituent `COLLECTION` and `STATE` slots. An OBLIGATION divergence that cannot be so reproduced indicates a defect in this definition, not a new semantic fact.

**INV-OBS-OBL-3.** OBLIGATION's value shape is `ordinal` (for `met`) plus `symbol` (for `satisfied`). The word *ratio*, used in v0.1 §1.2, is withdrawn: §3 admits no `ratio` form, and none is added.

**STATUS: CONTESTED.** Retention is on ergonomic grounds — a named, checkable category for a recurring pattern — not on grounds of semantic primitiveness, which F05R01-11 refuted and this revision does not attempt to re-establish. Whether the ergonomic argument justifies a derived kind at all is a founder adjudication this document does not pre-empt. Continued presence in this basis is **not** ratification.

---

## 2. The Normalized Observation structure

### 2.1 Structure

```
NormalizedObservation
    entity_ref            §4
    observable_kind       §1.1
    observation_status    §2.2
    value                 §3 — present only when observation_status = OBSERVED
```

**The `authority` field present in v0.1 §8.1 is removed.** See §3 for the disposition and §16 for why no replacement is introduced.

### 2.2 The presence envelope (D-02)

**INV-OBS-PRES-1.** `observation_status` SHALL be exactly one of `OBSERVED` or `NOT_OBSERVED`. It is a sibling of `value`, never a member of any value grammar, and never a member of any `observable_kind` enum.

**INV-OBS-PRES-2.** `OBSERVED` SHALL carry a `value` conforming to §3 for the selected `observable_kind`.

**INV-OBS-PRES-3.** `NOT_OBSERVED` SHALL carry no `value`. It asserts that no admissible observation of this slot was obtained — an epistemic absence, never a semantic one.

**INV-OBS-PRES-4 — the non-masquerade law.** `NOT_OBSERVED` SHALL NOT be represented by, conflated with, or substituted for any of:

```
boolean false            ordinal 0              symbol NONE
tier NONE                TRANSITION_RESULT.REJECTED
an empty COLLECTION      a declared default or initial value
an omitted slot
```

Each of the above is a positively observed fact about the target. `NOT_OBSERVED` is the absence of any such fact. This preserves `unknown ≠ false` and supplies the mechanism the base protocol's `INV-RC-VEC-4` requires and v0.1 did not provide.

**INV-OBS-PRES-5.** `NOT_OBSERVED` is meaningful only for a **declared, required** observable. Emitting `NOT_OBSERVED` for an undeclared slot is invalid — there is no obligation for it to be absent from.

**INV-OBS-PRES-6.** An omitted required slot is **not** equivalent to `NOT_OBSERVED` and SHALL be treated as a malformed conformance vector, not as an honest absence. Honest absence must be stated, not inferred from silence.

### 2.3 Invalid combinations — exhaustive for this structure

| Combination | Verdict |
|---|---|
| `OBSERVED` + no `value` | INVALID — malformed |
| `NOT_OBSERVED` + any `value` | INVALID — masquerade |
| `value` outside §3's forms for the declared kind | INVALID — undeclared value |
| `observable_kind` outside §1.1 | INVALID |
| required slot omitted entirely | INVALID — malformed vector (INV-OBS-PRES-6) |
| `NOT_OBSERVED` on an undeclared slot | INVALID (INV-OBS-PRES-5) |
| any field beyond the four in §2.1 | INVALID — ungoverned channel |

**INV-OBS-PRES-7.** The four fields in §2.1 are the complete structure. A field not enumerated there SHALL NOT appear. This closes, structurally, the class of defect F05R01-01 found — an undefined field cannot be introduced by diagram, by convention, or by inheritance from another document.

---

## 3. Authority — removed, not relocated (D-01)

F05R01-01 found `authority` present in v0.1's observation schema and defined nowhere: absent from the observable kinds, the value forms, the identity definition, and the adjudication table that claimed to record every term.

**Disposition applied, per F05-R02 D-01: classification (3) with immediate consequence (4).**

`authority` is a real construct already latent in the base protocol's own §2.4 candidate table ("Authority state", `LOCAL/PENDING/CANONICAL`), listed there as a peer of State, Intent, and Evidence state — each of which would require formal kernel admission before use. It was never admitted through that process, nor through F-05's extension law. It is therefore **not F-05's to own**, and F-05's schema SHALL NOT reference it.

**INV-OBS-AUTH-1.** No field named `authority`, and no field carrying authority semantics under another name, SHALL appear in the Normalized Observation structure.

**INV-OBS-AUTH-2.** No `observable_kind` SHALL be created to house authority. The six-kind basis is not extended for this purpose.

**INV-OBS-AUTH-3.** Ancestry (§9) SHALL NOT be read as authority. A record of where a reading came from confers no weight on whether that reading is confirmed. `traceability ≠ authority`.

**INV-OBS-AUTH-4.** Nothing in this section decides whether authority is later admitted, or by what mechanism. Future admission is a separate act requiring its own process, and this revision neither performs nor pre-empts it.

The standing law `meaning ≠ authority` is preserved by refusing authority a silent seat inside the meaning vocabulary — not by pretending the construct does not exist.

---

## 4. Observation identity

**INV-OBS-ID-1.** An observation is uniquely identified by the pair `(entity_ref, observable_kind)`. Two observations sharing this pair address the same slot and are comparable. Two observations with different pairs are never comparable; the oracle SHALL NOT attempt best-effort matching.

**INV-OBS-ID-2.** `entity_ref` SHALL be declared in RealityIR and carried unchanged through CapabilityDecision and TargetIR. A target SHALL NOT invent an `entity_ref` for anything RealityIR did not name.

**INV-OBS-ID-3 — corrected citation (F05R01-04).** INV-OBS-ID-2 establishes **stable cross-stage identity**: the subject of an observation is fixed before either target exists, so "the same slot" is an identity rather than a matching heuristic. It does **not**, by itself, satisfy the base protocol's `INV-RC-TGT-5`, which requires ancestry *"recoverable through the SSM by declaration, not by convention."* An unchanged opaque string is a convention. The declaration obligation that `INV-RC-TGT-5` actually requires is discharged by the Observation Projection Contract's SSM output (§9.5), not by identity stability. v0.1's claim to "directly satisfy" that invariant is withdrawn.

---

## 5. Ordering and trace semantics

### 5.1 Order is not time

**INV-OBS-ORD-1.** `ORDER` values SHALL be `sequence_token` — a monotonic integer scoped to one stimulus run, assigned by stimulus index. They SHALL NOT be derived from wall clock, thread scheduler, render loop, or any target-internal timing source.

**INV-OBS-ORD-2.** Wall-clock time SHALL NOT be used as an implicit total-order oracle. Where time is itself part of the SemanticProgram's meaning, it must be modelled as a declared observable in its own right, not inferred from observation timestamps.

### 5.2 The trace model

RC-0001 conformance SHALL NOT be reducible to terminal-state equality.

**INV-OBS-TRC-1.** A conformance run produces an ordered trace:

```
O₀ → s₁ → O₁ → s₂ → O₂ → … → sₙ → Oₙ
```

where each `Oᵢ` is the complete set of declared observations at that point and each `sᵢ` is a declared stimulus (§7).

**INV-OBS-TRC-2.** Comparison SHALL be performed over the full trace, step by step. Agreement at `Oₙ` alone is not conformance.

**INV-OBS-TRC-3 — no intra-step collapse.** If a slot's value changes more than once between two adjacent observation points, **every** intermediate value SHALL be retained as an ordered sub-sequence within that step. Collapsing intra-step changes to a last-write-wins value is forbidden.

*Rationale.* v0.1's `INV-OBS-ORD-1` specified last-write-wins for repeated intra-step writes. That permits a target to enter a state the reference forbids and self-correct before the next observation point, with the illegal excursion structurally invisible to step-by-step comparison. This revision removes that rule. The requirement is adopted from the F-05 revision mandate as a design obligation; it was not among F05-R01's fourteen findings, and no claim is made here that qualifying review established it.

**INV-OBS-TRC-4.** A transition SHALL NOT span an observation point. Every semantically significant state change produces an observation, so that ordering violations and forbidden intermediate states remain expressible in the trace rather than being smoothed away by sampling.

---

## 6. Persistence semantics

### 6.1 Discontinuity classes — substrate-neutral predicates (F05R01-12)

v0.1 defined tier boundaries by named events — "render", "reload", "tab lifetime", "device" — which are web-shaped and do not map onto iOS, server, batch, or non-interactive substrates. This revision defines boundaries by **discontinuity class**: a semantic category of interruption, stated without reference to any substrate's mechanics.

| Class | Predicate |
|---|---|
| `D-PRESENTATION` | The observable surface is recomputed from state still held by the same live runtime instance. |
| `D-RUNTIME` | The runtime instance holding the value is terminated; a new instance begins, same device, same actor. |
| `D-EPISODE` | The actor's bounded interaction episode ends, whether or not any runtime persists across it. |
| `D-STORAGE` | The local storage medium holding the value is lost, replaced, or reconstructed from empty. |
| `D-OBSERVER` | A different actor or observer attempts to observe the value. |

**INV-OBS-DISC-1.** Discontinuity classes are semantic. A substrate's concrete mechanism for inducing one (backgrounding, reload, reinstall, process kill, second device) is target-specific and belongs to the projection layer (§9), never to the class definition.

### 6.2 Tier predicates

```
NONE  <  LOCAL  <  SESSION  <  DURABLE_LOCAL  <  CANONICAL
```

| Tier | Survives | Does not survive |
|---|---|---|
| `NONE` | — | `D-PRESENTATION` |
| `LOCAL` | `D-PRESENTATION` | `D-RUNTIME` |
| `SESSION` | `D-RUNTIME` | `D-EPISODE` |
| `DURABLE_LOCAL` | `D-EPISODE` | `D-STORAGE` |
| `CANONICAL` | `D-STORAGE` **and** `D-OBSERVER` | — |

**INV-OBS-PER-1.** A RealityIR persistence requirement states a *required tier*; a target's observation states an *achieved tier*. The slot conforms iff `achieved ≥ required`, or the shortfall is covered by a declared CapabilityDecision (out of F-05's scope; reserved to R-04).

**INV-OBS-PER-2.** `CANONICAL` is a capability fact about a substrate, not a kernel fact. Nothing in this vocabulary asserts any substrate can reach it. A substrate that cannot SHALL say so at the named tier rather than satisfying the requirement at a lower tier silently.

### 6.3 NF-01 and NF-02 — recorded open, not resolved

**The `CANONICAL` row above carries two predicates.** Every other tier is distinguished from the one below it by exactly one discontinuity class. `CANONICAL` is distinguished by two: surviving `D-STORAGE` and being observable across `D-OBSERVER`. These are logically independent — a value can survive storage loss without being observable by another actor, and can be observable by another actor without surviving storage loss.

```
NF-01   Whether NONE < LOCAL < SESSION < DURABLE_LOCAL < CANONICAL is a
        coherent single semantic axis is UNTESTED.
        F05-R01 tested stimulus coverage (F05R01-03) and vocabulary
        substrate-neutrality (F05R01-12). Neither tested the order's
        internal coherence. No qualifying review has done so.

NF-02   Authority scope and durability may be two distinct dimensions,
        currently collapsed into one ladder at the CANONICAL rung.
        OPEN. Possibly the same missing dimension D-01 declined to admit
        (§3) — see F05-R02 §3.1.4.
```

**This revision deliberately neither splits nor defends the order.** Splitting without evidence would be as unfounded as retaining it by inertia. What the predicate form above accomplishes is making the two-dimensionality **visible in the table itself**, where v0.1's prose concealed it.

**What a future review must falsify.** Construct a value that is maximally authoritative on the `D-OBSERVER` axis and minimally durable on the `D-STORAGE` axis, or the converse, and determine whether `INV-OBS-PER-1`'s `achieved ≥ required` comparison produces a correct, an incorrect, or an undefined verdict for it. If undefined or incorrect, the ladder requires splitting into two independently-ordered dimensions.

---

## 7. Stimulus obligations (D-03) and the NF-03 dependency

### 7.1 The falsifiability law

**INV-OBS-STIM-1 — persistence coverage law.** A persistence tier SHALL NOT be claimed by RC-0001 unless the conformance suite contains at least one declared stimulus that induces the discontinuity class distinguishing that tier from the tier below it.

Applied to §6.2:

| Boundary | Required discontinuity | Covered by v0.1's `RESTART`? |
|---|---|---|
| `NONE → LOCAL` | `D-PRESENTATION` | possibly, if RESTART is read narrowly |
| `LOCAL → SESSION` | `D-RUNTIME` | plausibly — this is RESTART's natural reading |
| `SESSION → DURABLE_LOCAL` | `D-EPISODE` | **NO** |
| `DURABLE_LOCAL → CANONICAL` | `D-STORAGE` and `D-OBSERVER` | **NO** |

This is F05R01-03, made precise: one stimulus cannot discharge four boundaries, and the two upper boundaries are exactly the ones no declared stimulus reaches.

### 7.2 Stimulus contract shape — required, not populated

F-05 defines the **observation-side requirements** any stimulus must satisfy. It does not enumerate the stimuli.

```
STIMULUS (observation-side requirements)
  declared            named in RealityIR, applied identically to reference
                      and to every target; never incidental or emergent
  semantic identity   named by the semantic event it constitutes, never by a
                      substrate mechanism
  discontinuity class declares which of §6.1's classes it induces, if any
  observation point   induces exactly one observation point in the trace (§5.2)
  substrate mapping   how a given substrate realizes it is a projection
                      concern (§9), never part of the stimulus's identity
```

**INV-OBS-STIM-2.** A stimulus SHALL be identified semantically. `"app relaunch"` and `"page reload"` are substrate mechanics; `"a stimulus inducing D-RUNTIME"` is a stimulus identity. Two substrates realizing the same semantic stimulus by entirely different mechanisms have applied the same stimulus.

**INV-OBS-STIM-3.** `RESTART`, as defined in v0.1 §7, is withdrawn as a sufficient stimulus for persistence falsification. It may survive as one declared stimulus among several, mapped to a specific discontinuity class — but it SHALL NOT stand for all four boundaries.

**INV-OBS-STIM-4 — post-discontinuity re-observation.** Immediately following any stimulus inducing a discontinuity class, every persistence-bearing declared entity SHALL be re-observed, and:

```
required tier survives that class    →  observed value == value before
required tier does not survive it    →  observed value == declared initial value
                                        OR observation_status = NOT_OBSERVED,
                                        where the value is genuinely unobtainable
```

The `NOT_OBSERVED` branch matters: after `D-STORAGE`, a value at `DURABLE_LOCAL` is not merely reset — it may be genuinely unobservable, and §2.2 now permits saying so honestly.

### 7.3 NF-03 — the protocol-level gap, recorded not repaired

The base protocol defines stage contracts for every governed transformation (§1.1) but defines **no stimulus contract**, despite the Reference Operational Semantics being defined over *"a RealityIR + a stimulus sequence"* (protocol §4.2). Stimuli enter the pipeline ungoverned.

```
NF-03   The base protocol has no stimulus contract.
        F-05 may state observation-side requirements (§7.2) and does.
        F-05 may not create the protocol-level contract. It does not.
        DEPENDENCY: blocking on RC-0001 EXECUTION, not on F-05 coherence.
```

**Classification.** F-05 v0.2 remains internally coherent without the protocol-level contract: `INV-OBS-STIM-1` through `-4` are statable and checkable as written. What cannot proceed without it is RC-0001 actually *running* persistence falsification, because nothing would govern whether the applied stimuli are the declared ones. This is recorded as a downstream blocking dependency, not as a defect in this document, and **not** as authority to amend the protocol.

---

## 8. Transition and rejection semantics

### 8.1 Outcomes

**INV-OBS-TRN-1.** `TRANSITION_RESULT` SHALL be exactly one of:

```
APPLIED     the transition occurred; a new STATE observation is produced
REJECTED    the transition was declined; STATE is unchanged; a reason is carried
DEFERRED    the transition was recorded as intent, pending an authority this
            substrate may or may not possess
```

**INV-OBS-TRN-2.** `REJECTED` is a positively observed consequence. It SHALL NOT be conflated with `NOT_OBSERVED` (INV-OBS-PRES-4). A rejection is knowledge; an absence is the lack of it.

### 8.2 Rejection reasons

```
VALIDATION_FAILED     input did not satisfy a stated constraint
OBLIGATION_UNMET      a required obligation was not satisfied
AUTHORITY_ABSENT      the transition requires an authority this context lacks
OUT_OF_RANGE          a value fell outside a declared bound
```

**INV-OBS-TRN-3.** Closed for v0.2. New reasons enter only via §13's extension law, never by ad-hoc invention to explain an inconvenient rejection.

### 8.3 DEFERRED's effect on STATE (F05R01-13)

v0.1 stated the STATE effect for `APPLIED` and `REJECTED` and was silent for `DEFERRED` — permitting an optimistic target (STATE flips immediately) and a pessimistic reference (STATE holds) to agree at the `TRANSITION_RESULT` slot while diverging visibly to a user.

**INV-OBS-TRN-4.** Any entity whose RealityIR declares a `DEFERRED`-capable transition SHALL also declare a `STATE` observable. The divergence becomes visible in the trace regardless of which behaviour a target adopts.

**INV-OBS-TRN-5.** The optimistic/pessimistic choice SHALL be a declared per-requirement property in RealityIR, not a global default and not left to the target:

```
deferred_state_policy ∈ { HOLD_PRIOR, REFLECT_PENDING }
```

A target whose observed STATE after a `DEFERRED` outcome contradicts the declared policy has diverged, and the trace now shows it.

---

## 9. Observation Projection Contract (D-04)

F05R01-05, -06, -07 and -08 share one root cause: the projection boundary was drawn as a diagram box and given three narrow invariants, never instantiated as a governed transformation under the base protocol's §1.1 five-part discipline — so it inherited none of the obligations a properly-instantiated stage carries.

**Governance shape: a subordinate, cross-cutting contract — not a new top-level authority-bearing pipeline stage.** Precedent exists: the base protocol's SemanticSourceMap (§1.4) is fully governed without being a numbered box in the pipeline. The projection is specified the same way.

### 9.1 INPUT

A Target Observation — a reading of the live target expressed in target-local terms, produced from **declared target semantics** — together with a mandatory reference to the TargetIR node it is anchored to.

**INV-OPC-IN-1.** The anchoring TargetIR node reference is a typed, required input, not a documentation convention. A projection rule with no TargetIR node to anchor to is void and its output inadmissible.

### 9.2 OUTPUT

Exactly one Normalized Observation per declared observable, in the §2.1 structure, expressed only in F-05 vocabulary — plus the SSM record required by §9.5.

**INV-OPC-OUT-1.** The projection SHALL produce output for every declared required observable, using `observation_status = NOT_OBSERVED` where no admissible reading exists (§2.2). Producing nothing is not a lawful result.

### 9.3 INVARIANTS

**INV-OPC-1 — determinism.** The projection SHALL be a pure function of its declared input. Identical admissible input under the same declared projection SHALL yield identical normalized output.

**INV-OPC-2 — no permitted non-determinism.** RC-0001 requires none. Non-determinism in projection is therefore forbidden outright rather than bounded. (F05R01-07.)

**INV-OPC-3 — declared ancestry.** Every projection rule SHALL declare the ancestry relation it realizes, by declaration and not by naming convention.

**INV-OPC-4 — traceability.** Every Normalized Observation SHALL remain traceable to its originating target observation and to its semantic ancestry via §9.5.

**INV-OPC-5 — representation normalization only.** The projection MAY normalize *representation* — mapping a target-local encoding onto the declared vocabulary. This is its entire licensed function.

**INV-OPC-6 — coverage.** Every observable a TargetIR declares SHALL have a projection rule, and every rule's output form SHALL validate against §3. Coverage is checkable without understanding the substrate: count declared rules against declared observables, validate output shapes against a closed grammar.

**INV-OPC-7 — execution separation.** The projection SHALL NOT be executed by, nor derive its output from, the same process instance that produced the artifact under observation — unless every normalized observation is independently re-derived at witness time by a process that did not participate in emission.

*This closes the gap F05R01-08 identified.* v0.1's PROJ-3 required only that the rule's **author** differ from the verdict's computer. That is authorship separation. `INV-RC-WIT-4` guards against **execution-level** self-witnessing — the F-07 pattern — which authorship separation does not reach. Both are now required. The citation in v0.1 §8.2, which invoked `INV-RC-WIT-4` for a guarantee it does not provide, is withdrawn.

**INV-OPC-8 — authorship separation (retained).** The party authoring a projection rule SHALL NOT compute the pass/fail verdict for the slot that rule feeds.

### 9.4 FORBIDDEN AUTHORITY

The projection SHALL NOT:

```
invent semantic content not present in the target observation
weaken, reinterpret, or substitute for reference law
adjudicate conformance, or compute/influence any verdict
authorize adaptation
authorize correction
erase, omit, or suppress a required observation
convert NOT_OBSERVED into any semantic value (INV-OBS-PRES-4)
convert a semantic value into NOT_OBSERVED to avoid a divergence
consult reference observations
emit a value outside the closed vocabulary its anchored TargetIR node declares
introduce any field beyond §2.1's four
```

**INV-OPC-9 — the self-grading prohibition, stated as law.** A target emitter SHALL NOT be in a position to redefine its own observed behaviour during normalization. The constitutional separation required is: *the party or process that determines what the artifact does SHALL NOT be the sole party or process that determines what the artifact is recorded as having done.* No implementation technology is prescribed; the separation is a requirement on derivation independence, not on deployment topology.

### 9.5 SEMANTIC SOURCE MAP

**INV-OPC-SSM-1.** The projection SHALL emit, for every Normalized Observation, a resolvable reference to the target observation it derived from and to the TargetIR node anchoring the rule that produced it.

**INV-OPC-SSM-2.** This reference SHALL be a declaration, not a naming convention. Recoverability by matching strings, ordering, or similarity does not satisfy it. (This is the obligation `INV-RC-TGT-5` actually requires, and which §4's identity stability does not discharge — see INV-OBS-ID-3.)

**INV-OPC-SSM-3.** The SSM record is a companion to the observation, not a field within §2.1's four-field structure. Ancestry does not enter the comparison unit.

---

## 10. Semantic Source Map — authority boundary

Preserved from the governing lineage, unchanged.

**The SSM MAY:**
```
preserve semantic ancestry
identify divergence locus
connect a normalized observation to originating semantic constructs
support diagnostic reasoning
support bounded correction proposals
```

**The SSM MAY NOT:**
```
conclusively identify fault
mutate a target
authorize repair
adjudicate conformance
collapse locus into culpability
```

**INV-OBS-SSM-1 — mandatory causal discipline.**

```
divergence → locus → diagnostic reasoning → correction proposal
          → authority → governed execution → re-observation
```

**INV-OBS-SSM-2.** Any shortcut of the form `locus → fault → mutation` is forbidden, regardless of whether the resulting mutation would have been correct. Traceability informs authority; it never becomes authority.

---

## 11. Canonical value forms

| Form | Grammar | Used by |
|---|---|---|
| `symbol` | one member of a closed enum declared for that kind | STATE, TRANSITION_RESULT, OBLIGATION.satisfied |
| `boolean` | `true \| false` | declared boolean observables |
| `ordinal` | non-negative integer | COLLECTION.count, OBLIGATION.met |
| `entity_ref` | opaque string, RealityIR-declared | observations about another entity |
| `sequence_token` | monotonic integer, scoped to one stimulus run | ORDER |
| `tier` | one member of §6.2's ordered set | PERSISTENCE |

**INV-OBS-VAL-1.** No wall-clock form. No ISO timestamp, epoch value, or real-time-derived quantity. (Required by `INV-RC-REF-1`: two runs at different real times would otherwise produce different reference observations for identical programs.)

**INV-OBS-VAL-2.** The symbol set for a given `observable_kind` on a given entity type is declared once, upstream in RealityIR, and is closed. A target SHALL NOT introduce a symbol the reference never declared. Such a value is invalid, not surplus — see §12.

**INV-OBS-VAL-3.** No `ratio` form exists. v0.1's reference to one in OBLIGATION's shape is withdrawn (INV-OBS-OBL-3).

---

## 12. What is explicitly NOT observable

**INV-OBS-EXC-1.** The following SHALL NOT appear as normalized observations:

```
rendering and visual appearance     colour, layout, spacing, animation timing,
                                    typography — governed by target-local
                                    quality law, never by RC conformance
performance and timing              latency, frame rate, load time
implementation structure            DOM shape, class names, file layout,
                                    section-kind names — this is precisely what
                                    HBC's differentiation law measures; admitting
                                    it here would collapse Preservation into
                                    Distinction from the opposite direction
raw wall-clock values               forbidden at the value-form level, repeated
                                    here as the likeliest accidental leak
```

**INV-OBS-EXC-2 — surplus, stated as law rather than permission.** Comparison is defined only over declared `RequiredVectors`. An observation outside that set is never load-bearing for a verdict in either direction: a target earns no credit for volunteering it and incurs no penalty for withholding it.

*Drafting note.* v0.1 stated this as a permission ("a target may emit extra normalized observations") in §9 while `INV-OBS-VAL-2` simultaneously framed an undeclared value as a violation — the same act described two ways in two sections. This revision separates them: an **undeclared value on a declared slot** is invalid (INV-OBS-VAL-2); an **observation of an undeclared slot** is simply not load-bearing (INV-OBS-EXC-2). Converting the permission into a bounded invariant is required by the revision mandate's prose-permission law.

---

## 13. Extension law

**INV-OBS-EXT-1 — additive only.** A new observable kind, value form, rejection reason, discontinuity class, or persistence tier MAY be added. None SHALL be removed or redefined once a conformance vector has been recorded against it.

**INV-OBS-EXT-2 — admission burden, now including KERNEL-4 (F05R01-10).** An extension SHALL satisfy the base protocol's `INV-RC-KERNEL-1` (substrate independence), `INV-RC-KERNEL-3` (authority honesty), **and `INV-RC-KERNEL-4` (injective distinction)**.

`KERNEL-4` was omitted from v0.1's extension law with no stated reason. It is restored here, and — unlike `KERNEL-2` — it can be required directly without a bootstrap workaround: it tests a candidate against the already-admitted, fixed, enumerable set at extension time, and does not require the Reference Operational Semantics that made `KERNEL-2` circular.

**INV-OBS-EXT-3 — KERNEL-2 remains excluded, with the reason restated.** Admission is not conditioned on observability through the Reference Operational Semantics, because that semantics is defined over this vocabulary — the circularity Cold Review 001 recorded as R-01. Extensions are grounded instead in a demonstrated gap in an actual manifested artifact.

**INV-OBS-EXT-4 — semantic version immutability.** Adding a kind or form SHALL NOT retroactively change the meaning of any observation already valid under RC-0001. Every conformance record binds the vocabulary version under which it was produced, and SHALL be interpreted under that version. No migration framework is defined here; only the immutability obligation.

**INV-OBS-EXT-5 — founder ratification.** No extension self-seals. This applies to the contents of this document as much as to future proposals.

---

## 14. Term adjudication table — arithmetic corrected (F05R01-14)

v0.1's §11 claimed *"Twelve of twenty-four received terms were modified."* Direct recount refutes this. The table below is reproduced with verified counts.

| # | Term | Source | Verdict |
|---|---|---|---|
| 1 | entity state | Cold Review §4 | ACCEPT-MODIFIED |
| 2 | transition result | Cold Review §4 | ACCEPT |
| 3 | ordered collection state | Cold Review §4 | ACCEPT-MODIFIED |
| 4 | durable state | Cold Review §4 | ACCEPT-MODIFIED |
| 5 | relaunch/restoration state | Cold Review §4 | ACCEPT-MODIFIED |
| 6 | rejection/failure | Cold Review §4 | ACCEPT-MODIFIED |
| 7 | declared observable side effect | Cold Review §4 | REJECT |
| 8 | temporal/order relation | Cold Review §4 | ACCEPT-MODIFIED |
| 9 | `LOCAL` | Cold Review §4 | ACCEPT |
| 10 | `SESSION` | Cold Review §4 | ACCEPT |
| 11 | `DURABLE_LOCAL` | Cold Review §4 | ACCEPT |
| 12 | `CANONICAL` | Cold Review §4 | ACCEPT |
| 13 | `NONE` (persistence) | — | ADDED |
| 14 | `ENTITY` | founder message | REJECT as category |
| 15 | `STATE` | founder message | ACCEPT |
| 16 | `EVENT` | founder message | REJECT |
| 17 | `TRANSITION_RESULT` | founder message | ACCEPT |
| 18 | `COLLECTION` | founder message | ACCEPT |
| 19 | `PERSISTENCE` | founder message | ACCEPT |
| 20 | `ORDER` | founder message | ACCEPT |
| 21 | `REJECTION` | founder message | ACCEPT-MODIFIED |
| 22 | `RESTART` | founder message | ACCEPT-MODIFIED |
| 23 | `OBLIGATION` | — | ADDED |
| 24 | CapabilityDecision schema | founder message | DEFER |
| 25 | RC-0001 Semantic Basis | founder message | proposed path, not a term |

**Verified counts.** 25 rows. Row 25 is a proposed path, not a vocabulary term, leaving **24 term rows**. Of those 24: **8 ACCEPT-MODIFIED** (rows 1, 3, 4, 5, 6, 8, 21, 22) · **10 ACCEPT** (2, 9, 10, 11, 12, 15, 17, 18, 19, 20) · **3 REJECT-family** (7, 14, 16) · **2 ADDED** (13, 23) · **1 DEFER** (24). Sum: 8 + 10 + 3 + 2 + 1 = 24 ✓. Of the 24 term rows, **2 were ADDED** by the packet and **22 were received** from an upstream source.

The corrected claim: *eight* of twenty-two received terms were modified — not twelve of twenty-four.

---

## 15. Traceability — 14 findings → disposition → revised clause

| Finding | F05-R02 disposition | Revised clause in this document |
|---|---|---|
| F05R01-01 authority undefined | ACCEPT | §2.1 (field removed), §2.3, INV-OBS-PRES-7, §3 (INV-OBS-AUTH-1…4) |
| F05R01-02 no NOT_OBSERVED | ACCEPT | §2.2 (INV-OBS-PRES-1…6), §2.3, §7.2 INV-OBS-STIM-4 |
| F05R01-03 RESTART insufficient | ACCEPT_WITH_REFRAME | §6.1 (discontinuity classes), §7.1 (INV-OBS-STIM-1 + boundary table), INV-OBS-STIM-3 |
| F05R01-04 TGT-5 citation overclaim | ACCEPT | §4 INV-OBS-ID-3 (claim withdrawn), §9.5 INV-OPC-SSM-2 (obligation discharged where it belongs) |
| F05R01-05 no stage contract | ACCEPT | §9 in full — INPUT, OUTPUT, INVARIANTS, FORBIDDEN AUTHORITY, SSM |
| F05R01-06 no SSM ancestry | ACCEPT | §9.5 INV-OPC-SSM-1…3, §9.3 INV-OPC-3/-4 |
| F05R01-07 no determinism | ACCEPT | §9.3 INV-OPC-1, INV-OPC-2 |
| F05R01-08 WIT-4 authorship≠execution | ACCEPT_WITH_REFRAME | §9.3 INV-OPC-7 (execution separation added), INV-OPC-8 (authorship retained), citation withdrawn in situ |
| F05R01-09 COLLECTION membership | ACCEPT_WITH_REFRAME | §1.1 (scope narrowed to cardinality), §16 condition note |
| F05R01-10 EXT-2 drops KERNEL-4 | ACCEPT | §13 INV-OBS-EXT-2 |
| F05R01-11 OBLIGATION necessity | ACCEPT_WITH_REFRAME | §1.3 (INV-OBS-OBL-1…3, explicit RETAIN-as-DERIVED, CONTESTED), §11 INV-OBS-VAL-3 |
| F05R01-12 web-native tiers | ACCEPT | §6.1 (discontinuity predicates), §6.2 (tier table rewritten) |
| F05R01-13 DEFERRED silent on STATE | ACCEPT | §8.3 INV-OBS-TRN-4, INV-OBS-TRN-5 |
| F05R01-14 arithmetic defect | ACCEPT | §14 (recount, verified sum) |

**Count: 14 of 14 findings have a visible corresponding clause. 0 unaccounted.**

---

## 16. Five readiness conditions — disposition table

| # | Condition (from F05-R02 §10) | Revised section | Status | Unresolved dependency |
|---|---|---|---|---|
| 1 | OBLIGATION either/or must be an explicit stated choice | §1.3 | **SATISFIED** — RETAIN as DERIVED, marked CONTESTED, derivation stated normatively | Founder adjudication of whether a derived kind is warranted at all |
| 2 | DEFERRED STATE-effect resolved, not left silent | §8.3 | **SATISFIED** — per-requirement `deferred_state_policy` + mandatory STATE pairing | None |
| 3 | Persistence coherence must not be quietly assumed resolved | §6.3 | **SATISFIED** — NF-01/NF-02 recorded open; predicate form makes the two-dimensionality visible without deciding it; falsification target stated | NF-01 requires a dedicated review pass |
| 4 | `authority` removal immediate and unconditional | §2.1, §3 | **SATISFIED** — removed; INV-OBS-PRES-7 forecloses re-entry by any route; future admission explicitly not pre-empted | Future authority admission is a separate act |
| 5 | Every accepted finding's "review required after repair" is binding | §15 + this row | **SATISFIED** — all 14 carry a traceable clause; none is closed by this document | F05-R03 re-review must verify each |

**No condition required changing frozen doctrine or modifying the base protocol.** Condition 3's dependency (NF-01) and §7.3's dependency (NF-03) are downstream of this document, not blockers on its coherence.

---

## 17. Open questions carried forward

```
NF-01   Persistence-order coherence UNTESTED. No qualifying review has tested
        whether the five-tier ladder is one axis. §6.3 states the falsification
        target. OPEN.

NF-02   Authority scope may be a second dimension currently collapsed into the
        CANONICAL rung. Possibly the same construct D-01 declined to admit.
        OPEN.

NF-03   The base protocol has no stimulus contract. F-05 states observation-side
        requirements only (§7.2). Blocking on RC-0001 execution, not on F-05
        coherence. Requires a protocol-revision pass this document has no
        authority to perform. OPEN.

R-01    Kernel/reference circularity remains open in the general case. §13's
        INV-OBS-EXT-3 works around it for extensions; it does not resolve it.

R-03    RC-0001's proof predicate (target↔target vs target↔reference) untouched
        by this revision. OPEN, reserved to its own movement.

R-04    Capability decision bounds untouched. §6.2's tier order is what that
        schema will range over. OPEN, reserved to its own movement.

OBLIGATION status   Retained as DERIVED and CONTESTED (§1.3). Not ratified.
```

---

## 18. Non-mutation verification

```
FILES CREATED BY THIS REVISION    exactly one — this document
FILES MODIFIED                    none

F-05 packet v0.1     b5c3a20e…c40e9     UNCHANGED — preserved deliberately (§0.1)
F05-R01              0420da3b…461a92ae  UNCHANGED
F05-R02              8b8bd4de…c12d28d2  UNCHANGED
Cold Review 001      082b6cb8…939fe9a   UNCHANGED
RCP v0.1 draft       1aa3698c…38c776    UNCHANGED
HBC baseline         e350205            UNCHANGED, 30-file tree intact
```

Independent recomputation is reported in the response accompanying this document rather than duplicated here — a document should not be the sole evidence for its own correctness, consistent with `INV-RC-WIT-4`'s spirit.

---

## 19. Revision verdict

```
READY_FOR_F05_RE_REVIEW
```

All 14 findings have a traceable revised clause (§15). All 5 readiness conditions are satisfied (§16). D-01 through D-04 are each implemented as adjudicated. No repair required changing frozen doctrine, and none was attempted. Three open questions (NF-01, NF-02, NF-03) are carried forward explicitly rather than closed by assertion, and none of them blocks re-review of this document — NF-01 requires its own dedicated pass, NF-03 blocks RC-0001 execution downstream.

This verdict is a **readiness judgment only**. It is not ratification, not a seal, and not evidence that this vocabulary is correct. It asserts that the document is now in a state a re-reviewer can attack productively — nothing more.

The next lawful movement is **F05-R03 re-review**, which should be at minimum lineage-independent, and which will inherit this document's declared authorship defect (§0.2) as its reason for existing.

---

## Closing boundary

This revision repairs what F05-R02 accepted, in the form F05-R02 specified, and carries forward what remains open in the language of open questions rather than the language of resolution. It ratifies nothing, seals nothing, mutates no predecessor, touches no implementation, and executes no proof.

The vocabulary is no longer primarily a list of what can be observed. It is a specification of what OURSELF is legally permitted to claim it observed — and, more importantly, of every route by which such a claim could have entered ungoverned, now closed or named.

---

*An observation is not a value. It is a governed claim about what was seen, by whom, under what stimulus, with what standing — and a vocabulary that cannot say which of those it is missing has not finished being written.*
