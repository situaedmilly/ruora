# OURSELF REALITY COMPILATION PROTOCOL v0.1

**STATUS** DRAFT · design-only authorship · not sealed · not ratified
**AUTHORITY** Design/documentation only. No implementation authorized.
**PRECONDITION** HBC custody witnessed at `e350205`, tree digest `98fb73e3…cfded7`.

---

## Preamble — what this document is

The strategic doctrine and protocol topology of OURSELF Age III were frozen in
deliberation and, until this document, had no repository body. This artifact is
the first durable embodiment of that frozen law. It authors what was frozen; it
does not extend it.

Where authorship encountered a question the frozen doctrine does not answer, the
question is recorded in **§13 Findings Register** and left open. No finding has
been silently resolved by inventing law. That register is the honest output of
this pass and should be read before any section is treated as settled.

This protocol governs **one claim**: that a single intended reality can be
projected onto more than one substrate without its meaning changing. Everything
else here exists to make that claim falsifiable.

---

## 0. Identity + Scope

### 0.1 Identity

The Reality Compilation Protocol (**RCP**) is the constitution of the OURSELF
compilation organism. It defines the stages by which a **SemanticProgram**
becomes a running reality on a target substrate, and the conditions under which
two such realities may be called **the same reality**.

RCP is not a framework, not a runtime, and not a code generator. It is the law
that a compilation organ must submit to in order to be called conformant.

### 0.2 The governed pipeline

```
SemanticProgram
      │  authorship
      ▼
RealityIR ─────────────────► Reference Operational Semantics
      │  canonical form              │  evaluation
      │                              ▼
      │                       Reference Observations
      ▼
CapabilityDecision                   │
      │  substrate resolution        │
      ▼                              │
TargetIR                             │
      │  adaptation                  │
      ▼                              ▼
Emitter ──► Target Artifact ──► Target Observations
                                     │
                                     ▼
                            ConformanceOracle
                                     │
                                     ▼
                              DIVERGENCE / CONFORMANCE
```

`SemanticSourceMap` runs orthogonally across every arrow. It is defined once in
§1.4 and carried as an obligation by every stage.

### 0.3 The two axes — and why they must not be confused

RCP governs exactly one of two orthogonal integrity axes.

| | Question | Governed by |
|---|---|---|
| **Preservation** | Does *one* meaning survive *different* embodiments? | **RCP. This document.** |
| **Distinction** | Do *different* meanings resist collapsing into interchangeable artifacts within *one* substrate? | Target-local quality law. Not RCP. |

```
        PRESERVATION                          DISTINCTION
  one meaning, many substrates          many meanings, one substrate

     SemanticProgram                    Reality A        Reality B
            │                               │                │
      ┌─────┴─────┐                         ▼                ▼
      ▼           ▼                    embodiment       embodiment
    WEB         iOS                         └───── must NOT ─────┘
      └──── must ────┘                            collapse
         be equivalent

    RC CONFORMANCE                    TARGET-LOCAL QUALITY LAW
```

**§0.3 LAW.** A target-local distinction law is never evidence of RC
conformance, and RC conformance is never evidence of distinction. A target may
pass one and fail the other. Any document, oracle, or report that treats one as
the other is in violation of this protocol.

*Rationale — HBC as found.* HBC v0.1 implements a differentiation law
(`compiler/differentiate.js`) measuring whether distinct packets produce
non-interchangeable artifacts. Inspection confirms the law takes N realms and
compares them pairwise across **different** packets; it has no representation of
one program across two substrates. The preservation axis is therefore not merely
unimplemented in HBC — it is unexpressible in HBC's current type signature. HBC
cannot accidentally claim RC conformance. This is a favourable structural
property and is recorded, not credited.

### 0.4 Scope

**RCP governs:** the stage contracts; the canonical form of RealityIR; the
authority permitted at each stage; the vocabulary of capability decisions; the
obligations of an emitter; what constitutes an observation, a conformance
vector, and drift; who may adjudicate; and the specification of RC-0001.

**RCP does not govern:** the authorship of any particular SemanticProgram; the
aesthetic or commercial quality of any target artifact; the internal
implementation of any emitter, provided its contract holds; hosting, deployment,
or distribution; or any target-local quality law.

### 0.5 Explicit non-goals

RCP v0.1 does not seal the membership of the Semantic Kernel (§2.2), does not
authorize any implementation, and does not adjudicate any existing organ into
conformance. Candidate status is not conformance.

### 0.6 Versioning

RCP v0.1 is a draft. A sealed RCP requires separate adjudication under §11. No
stage contract in this document may be treated as binding law until sealed.

---

## 1. Stage Contracts

### 1.1 The universal stage form

Every stage in §0.2 is a contract. Every applicable stage contract in this
document declares, without exception:

```
INPUT                     what the stage is permitted to receive
OUTPUT                    what the stage is obligated to produce
INVARIANTS                what must hold across the transformation
FORBIDDEN AUTHORITY       what the stage may never do, decide, or claim
SEMANTIC SOURCE MAP       what ancestry the stage must preserve
```

A stage that cannot declare all five is not a stage. It is an unaudited
transformation and has no place in the pipeline.

### 1.2 The authority narrowing law

**INV-RC-STAGE-1.** Authority is monotonically non-increasing along the
pipeline. No stage may hold authority its input did not already carry, and no
stage may grant itself authority by producing output that asserts more than its
input permitted.

**INV-RC-STAGE-2.** A stage may **narrow** meaning only by an explicitly
recorded decision (§5). Silent narrowing is drift (§10), not adaptation.

**INV-RC-STAGE-3.** No stage may **widen** meaning. A stage that produces an
output asserting something its input did not is in violation regardless of
whether the assertion is true.

### 1.3 Totality

**INV-RC-STAGE-4.** Every stage is a partial function that either produces a
declared OUTPUT or **refuses** with a stated reason. No stage may produce a
degraded output silently. Refusal is a lawful result; silent degradation is not.

### 1.4 The Semantic Source Map — cross-stage traceability contract

The Semantic Source Map (**SSM**) is a cross-stage traceability structure
carried by every arrow in §0.2. It exists so that a divergence can be *located*
without anyone being authorized to *act* on the location.

**SSM MAY:**

- preserve semantic ancestry from any downstream node to its upstream origin;
- identify divergence loci;
- support bounded correction proposals.

**SSM MAY NOT:**

- conclusively diagnose root cause;
- mutate targets;
- authorize correction;
- adjudicate conformance.

**INV-RC-SSM-1.** Every node in every stage OUTPUT carries a resolvable
reference to the node(s) in that stage's INPUT from which it derives.

**INV-RC-SSM-2.** Ancestry is declared by the producing stage, never inferred by
a consumer. Ancestry recoverable only by convention — position, ordering, naming
similarity — does not satisfy this invariant.

**INV-RC-SSM-3.** The SSM is evidence-bearing and never authority-bearing. The
lawful chain is:

```
ConformanceOracle → DIVERGENCE → SemanticSourceMap → LOCUS / PROVENANCE
      → diagnostic reasoning → CorrectionProposal → Authority
      → governed execution → re-observation
```

Any path that shortens this chain — most dangerously *locus therefore fault
therefore automatic mutation* — is a violation of RCP regardless of correctness
of outcome. Traceability informs authority. It never becomes authority.

**HBC v0.1 AS FOUND.** Inspection of the emitted artifact shows target-local
structural ancestry attributes: `data-section`, `data-primitive`, `data-realm`,
`data-voice`, plus deterministic collision-free element ids and a packet digest.
No emitted node carries a declared reference to its originating packet path; the
mapping from `hierarchy[i]` to emitted DOM is recoverable only by kind-and-order
convention. Under INV-RC-SSM-2 as drafted, convention-recoverable ancestry does
not satisfy the invariant. **This is recorded as Finding F-01 and is not
repaired.** HBC must be graded as found; an artifact coached to pass the
examination proves nothing about the examination.

---

## 2. Semantic Kernel

### 2.1 Purpose

The Semantic Kernel is the closed set of meaning-bearing constructs that
RealityIR is able to express. It is the answer to: *what, exactly, is being
preserved?*

### 2.2 Membership is NOT sealed in v0.1

**RCP v0.1 does not seal kernel membership.** Sealing the kernel is a
constitutional act requiring adjudication under §11 and is outside design-only
authority. What v0.1 seals is the set of **obligations** any construct must
satisfy to be admitted.

### 2.3 Admission obligations

A construct may be admitted to the Semantic Kernel only if it satisfies all of:

**INV-RC-KERNEL-1 — Substrate independence.** The construct is expressible
without reference to any particular substrate's mechanics. A construct that can
only be stated in terms of DOM, UIKit, HTTP, or any concrete technology is not a
kernel construct.

**INV-RC-KERNEL-2 — Observable consequence.** The construct has at least one
consequence observable through the Reference Operational Semantics (§4). A
construct with no observable consequence cannot be preserved, cannot be
violated, and cannot be tested; it is decoration in the sense of
SELF-VISUAL-DIMENSION Law 1 and is refused.

**INV-RC-KERNEL-3 — Authority honesty.** The construct is able to represent its
own authority state, including the state *unknown* and the state *not
confirmed*. A construct that can only represent confirmed states cannot express
the honesty law and is refused.

**INV-RC-KERNEL-4 — Injective distinction.** No admitted construct may encode a
distinction already encoded by another admitted construct. Two constructs that
collapse to one meaning encode neither.

### 2.4 Candidate constructs already manifested

The following are recorded as **candidates** because they exist in already-
manifested ecosystem artifacts, not because RCP invents them. Recording is not
admission.

| Candidate | Manifested in | Note |
|---|---|---|
| Actor | ClientPortal, HBC packets | who acts |
| Intent | ClientPortal `client_intent_recorded`, HBC ECHO | a proposed, unconfirmed act |
| Authority state | ClientPortal `LOCAL/PENDING/CANONICAL`, HBC `LOCAL/PENDING/NONE` | see §2.5 |
| Evidence state | ClientPortal `MISSING/SUBMITTED/VERIFIED/FAILED` | `SUBMITTED ≠ VERIFIED` |
| Obligation | HBC `required` / outstanding selections | something owed before a transition |
| State transition | ClientPortal stage thread, HBC week state | with declared from/to |
| Boundary | HBC `boundary_statement`, `truth.unknown` | a declared absence of capability |
| Causal relation | ClientPortal THREAD, HBC `process_thread` | ordered consequence |

### 2.5 A structural observation on authority vocabulary

HBC v0.1 makes `CANONICAL` unreachable: its emitted runtime contains no
transport whatsoever (no `fetch`, `XMLHttpRequest`, WebSocket, EventSource,
`localStorage`, `sessionStorage`, `document.cookie`, or form action — asserted
by its own test suite), so no compiled realm can claim a system accepted
anything.

Under RCP this is correctly read **not** as a kernel truth but as a **capability
decision of the static-HTML substrate** (§5). The kernel authority vocabulary
must span substrates where `CANONICAL` *is* reachable; HBC's restriction is the
substrate answering the capability question, not the kernel lacking the concept.

Recorded as **Finding F-04**. Whether the kernel authority vocabulary is exactly
ClientPortal's three states, or a superset, is not decided here.

### 2.6 Contract

```
INPUT                 candidate construct proposal
OUTPUT                admission or refusal, with stated reason
INVARIANTS            INV-RC-KERNEL-1 … 4
FORBIDDEN AUTHORITY   may not admit a construct by usage; may not seal
                      membership; may not define substrate mechanics
SEMANTIC SOURCE MAP   every admitted construct records the artifact in which
                      it was first manifested
```

---

## 3. RealityIR Canonical Form

### 3.1 Purpose

RealityIR is the substrate-independent representation of an intended reality. Its
canonical form exists so that **identity of meaning is decidable by bytes**.

### 3.2 Contract

```
INPUT                 SemanticProgram
OUTPUT                RealityIR in canonical form, with a canonical digest
INVARIANTS            INV-RC-IR-1 … 5
FORBIDDEN AUTHORITY   may not resolve capabilities; may not consult any
                      substrate; may not choose an emitter; may not
                      evaluate; may not observe
SEMANTIC SOURCE MAP   every RealityIR node references its SemanticProgram origin
```

### 3.3 Invariants

**INV-RC-IR-1 — Canonicality.** Two RealityIR values with identical meaning have
identical canonical serializations. Key order, whitespace, and construction
order are normalized away.

**INV-RC-IR-2 — Digest identity.** The canonical digest is a function of the
canonical serialization alone. Two programs share a digest if and only if they
share a meaning.

**INV-RC-IR-3 — No ambient state.** No wall clock, randomness, environment
variable, filesystem state, locale, or network result may reach a canonical
form. A RealityIR that cannot be reproduced is not canonical.

**INV-RC-IR-4 — Substrate silence.** RealityIR contains no substrate mechanics.
A RealityIR referencing a DOM node, a view controller, an HTTP verb, or a CSS
token is malformed.

**INV-RC-IR-5 — Total declaration.** Everything the program asserts is present
in the RealityIR. Nothing is carried out-of-band into a later stage.

### 3.4 Prior art — recorded, not adopted

HBC v0.1 independently demonstrates a working instance of the INV-RC-IR-1/2/3
discipline: key-sorted JSON serialization, `sha256` over sorted
`path:sha256(content)` lines, artifact digest a function of file names and bytes
alone, and a test asserting no wall clock reaches an artifact. Its determinism
is verified by compiling every fixture twice and comparing digests.

**This is prior art, not a claim that HBC's Realm Packet is RealityIR.** The
Realm Packet is substrate-shaped: it names HTML section kinds, CSS-bound
frequency dimensions, and a `static_html` target. Under INV-RC-IR-4 it is
therefore **not** a RealityIR. Whether it is a TargetIR, or derives from one, is
**Finding F-02** and is not decided here.

---

## 4. Reference Operational Semantics

### 4.1 Purpose

The Reference Operational Semantics defines what a RealityIR *means* by defining
how it is evaluated. It is the sole authority on meaning. No target substrate,
however elegant or however widely deployed, may define meaning.

### 4.2 Contract

```
INPUT                 RealityIR in canonical form + a stimulus sequence
OUTPUT                an ordered set of Reference Observations
INVARIANTS            INV-RC-REF-1 … 4
FORBIDDEN AUTHORITY   may not emit; may not adapt; may not consult a target;
                      may not judge conformance; may not repair
SEMANTIC SOURCE MAP   every observation references the RealityIR node(s)
                      whose evaluation produced it
```

### 4.3 Invariants

**INV-RC-REF-1 — Determinism.** The same RealityIR under the same stimulus
sequence produces the same observations, always.

**INV-RC-REF-2 — Substrate blindness.** The reference interpreter has no
knowledge of any target. It cannot be tuned to make a target pass.

**INV-RC-REF-3 — Observational completeness.** Every kernel construct with an
observable consequence (INV-RC-KERNEL-2) produces at least one observation.

**INV-RC-REF-4 — Non-authority over targets.** A reference observation is the
statement of what *should* be observed. It is never itself evidence that a
target *did* observe it.

### 4.4 The observation

An observation is a normalized, substrate-neutral record of a consequence. Its
vocabulary is **not** sealed in v0.1 — see **Finding F-05**. What is sealed is
that observations from the reference interpreter and from any target must be
expressed in the *same* vocabulary, or the Conformance Oracle (§8) is comparing
nothing.

---

## 5. Capability Decision Vocabulary

### 5.1 Purpose

Substrates differ. A capability decision records — explicitly, and in a closed
vocabulary — what a given substrate can do with a given semantic requirement.
Its purpose is to make substrate limitation **declared** rather than silently
absorbed.

### 5.2 Contract

```
INPUT                 RealityIR + a substrate capability profile
OUTPUT                a CapabilityDecision per semantic requirement
INVARIANTS            INV-RC-CAP-1 … 4
FORBIDDEN AUTHORITY   may not alter RealityIR; may not emit; may not decide
                      that a requirement is unimportant; may not resolve a
                      requirement by omission
SEMANTIC SOURCE MAP   every decision references the RealityIR requirement it
                      answers and the capability profile entry it consulted
```

### 5.3 The closed decision vocabulary

| Decision | Meaning |
|---|---|
| `SUPPORTED` | The substrate realizes the requirement directly. |
| `SUBSTITUTED` | Realized by different mechanics with equivalent observable consequence. Equivalence must be demonstrable, not asserted. |
| `DEGRADED` | Realized with reduced fidelity, with the reduction stated and bounded. Observable consequence is preserved; richness is not. |
| `ABSENT` | Not realizable on this substrate. The absence must be **declared in the artifact**, never hidden. |
| `REFUSED` | The substrate could realize it, but doing so would violate an invariant. Compilation stops. |

**INV-RC-CAP-1 — Totality.** Every semantic requirement receives exactly one
decision. A requirement with no decision is a compilation error, not a default.

**INV-RC-CAP-2 — Declared absence.** An `ABSENT` decision obligates the emitter
to make the absence visible in the target artifact. Absence hidden from the
actor is a false claim about reality.

**INV-RC-CAP-3 — Substitution burden.** `SUBSTITUTED` requires demonstrable
observational equivalence. Assertion of equivalence is not equivalence.

**INV-RC-CAP-4 — No silent downgrade.** A decision may never be weakened after
the fact to make a conformance run pass. Decisions are inputs to conformance,
never outputs of it.

### 5.4 HBC v0.1 AS FOUND

HBC embodies the spirit of INV-RC-CAP-2 unusually well without naming it. Its
pattern is already:

```
unknown       ≠ false
unobserved    ≠ passed
local         ≠ canonical
generated     ≠ verified
artifact      ≠ evidence
```

Concretely: `truth.unknown` and `authority_contract.may_never_claim` are
compiled into a visible `boundary_statement` rather than omitted; a missing
photograph becomes a declared evidence slot rather than a stock substitute; and
an unavailable browser yields `NOT WITNESSED` rather than `PASS`.

This is recorded as favourable structural compatibility. It is **not** a
capability decision vocabulary: HBC declares absences it was told about in its
packet, and has no capability *profile* and no per-requirement decision record.
Recorded as **Finding F-03**.

---

## 6. TargetIR Adaptation Law

### 6.1 Purpose

TargetIR is the substrate-shaped representation produced by applying capability
decisions to RealityIR. It is where substrate mechanics first become lawful.

### 6.2 Contract

```
INPUT                 RealityIR (canonical) + complete CapabilityDecision set
OUTPUT                TargetIR for exactly one named substrate
INVARIANTS            INV-RC-TGT-1 … 5
FORBIDDEN AUTHORITY   may not add semantics; may not drop a declared
                      obligation; may not consult observations; may not
                      judge; may not re-decide capabilities
SEMANTIC SOURCE MAP   every TargetIR node references its RealityIR ancestor
                      and the CapabilityDecision that shaped it
```

### 6.3 Invariants

**INV-RC-TGT-1 — No semantic addition.** TargetIR asserts nothing the RealityIR
did not. Substrate affordance is not permission to mean more.

**INV-RC-TGT-2 — Obligation preservation.** Every obligation in the RealityIR
appears in the TargetIR or is accounted for by an `ABSENT` / `DEGRADED` decision
whose declaration obligation is carried forward.

**INV-RC-TGT-3 — Decision fidelity.** Adaptation implements the decisions it was
given. It may not silently choose `DEGRADED` where it was handed `SUPPORTED`.

**INV-RC-TGT-4 — Single substrate.** One TargetIR names exactly one substrate.
A TargetIR spanning substrates is malformed.

**INV-RC-TGT-5 — Reversible ancestry.** For every TargetIR node, the RealityIR
node it derives from is recoverable through the SSM by declaration, not by
convention.

---

## 7. Emitter Contract

### 7.1 Purpose

The emitter turns TargetIR into a running artifact. This is the stage where a
compilation organ most easily begins to lie, because it is the first stage that
produces something a human will look at and believe.

### 7.2 Contract

```
INPUT                 TargetIR for the emitter's declared substrate
OUTPUT                a target artifact + an emission record
INVARIANTS            INV-RC-EMIT-1 … 7
FORBIDDEN AUTHORITY   may not add semantics; may not claim authority the
                      TargetIR did not carry; may not repair its input;
                      may not adjudicate its own conformance; may not
                      deploy, publish, or distribute
SEMANTIC SOURCE MAP   every emitted node references its TargetIR ancestor
```

### 7.3 Invariants

**INV-RC-EMIT-1 — Determinism.** The same TargetIR emits byte-identical
artifacts. No wall clock, randomness, or environment state may reach output.

**INV-RC-EMIT-2 — Declared substrate.** An emitter serves exactly one substrate
and declares it.

**INV-RC-EMIT-3 — No undeclared authority.** The artifact may not assert, imply,
or stage any authority its TargetIR did not carry. Structural impossibility is
preferred to policy: an emitter that *cannot* reach a transport cannot lie about
one.

**INV-RC-EMIT-4 — Declared absence carried through.** Every `ABSENT` and
`DEGRADED` decision surfaces in the artifact as a visible declaration.

**INV-RC-EMIT-5 — Refusal over degradation.** An emitter that cannot satisfy its
TargetIR refuses with a stated reason. It never ships a partial artifact
silently.

**INV-RC-EMIT-6 — Source map emission.** The emitter produces an SSM segment
satisfying INV-RC-SSM-1 and INV-RC-SSM-2.

**INV-RC-EMIT-7 — Boundary of authority.** Emission ends at a sealed artifact
candidate. Deployment authority is separate and is never held by an emitter.

### 7.4 HBC v0.1 AS FOUND — evaluated, not graded

Evaluated against §7.3 as the artifact stands at `e350205`. This is an
observation table, **not** a conformance verdict; conformance requires the
Oracle (§8), which does not exist.

| Invariant | HBC v0.1 as found |
|---|---|
| EMIT-1 Determinism | Present. Byte-identical recompilation asserted by test and by `hbc prove`, which compiles every fixture twice and compares digests. |
| EMIT-2 Declared substrate | Present. `output_contract.target: static_html`. |
| EMIT-3 No undeclared authority | Present, and structurally enforced. Emitted runtime contains no transport primitive of any kind. |
| EMIT-4 Declared absence | Present in effect. Boundary statement compiled from `truth.unknown` + `may_never_claim`; evidence slots rather than substituted imagery. Not driven by a capability decision record (F-03). |
| EMIT-5 Refusal over degradation | Present. Blueprint stage refuses on unbound primitive, undeclared primitive, missing required content, out-of-vocabulary glyph, and portal cardinality violation. |
| EMIT-6 Source map emission | **Not satisfied as drafted.** Ancestry is convention-recoverable only (F-01). |
| EMIT-7 Deployment boundary | Present. Writes refused outside `output/`; artifacts stop at `SEALED_REALM_CANDIDATE`; witness records `NOT DEPLOYED`. |

Six of seven invariants have a corresponding property already present. The
single gap is declarative ancestry. **No repair is authorized, proposed, or
implied by this table.**

---

## 8. Conformance Vector Contract

### 8.1 Purpose

A conformance vector is the normalized observation set produced by exercising an
artifact. It is the only thing the Oracle is permitted to compare.

### 8.2 Contract

```
INPUT                 a target artifact + the stimulus sequence used for the
                      reference evaluation
OUTPUT                a ConformanceVector in the shared observation vocabulary
INVARIANTS            INV-RC-VEC-1 … 4
FORBIDDEN AUTHORITY   may not consult RealityIR; may not consult reference
                      observations; may not judge; may not adapt the artifact
SEMANTIC SOURCE MAP   every observation references the emitted node that
                      produced it
```

### 8.3 Invariants

**INV-RC-VEC-1 — Shared vocabulary.** Target observations use the same
vocabulary as reference observations (§4.4). Comparison across vocabularies is
not comparison.

**INV-RC-VEC-2 — Blind extraction.** The extractor does not know the expected
answer. An extractor with access to reference observations can manufacture
agreement.

**INV-RC-VEC-3 — Identical stimulus.** Both vectors arise from the same stimulus
sequence. Different stimuli produce incomparable vectors.

**INV-RC-VEC-4 — Unobserved is a value.** An observation that could not be made
is recorded as `NOT OBSERVED`, never as absence and never as agreement.

### 8.4 Equivalence, not identity

**INV-RC-VEC-5.** Conformance is *observational equivalence*, not artifact
identity. Two substrates producing byte-identical artifacts would prove nothing
except that they are the same substrate. What must match is consequence.

### 8.5 HBC v0.1 AS FOUND

HBC emits a `witness.json` containing check ids, statuses in a
`pass / fail / not_witnessed` trichotomy, bound primitives, realized
interactions, and digests. The trichotomy independently anticipates INV-RC-VEC-4.

However these are **target-local check results**, not normalized observations:
the ids (`glyphs_labelled`, `no_rigid_widths`, `contrast_floor`) are HTML/CSS
specific and have no meaning on another substrate. HBC has no normalized
observation vocabulary and cannot currently produce a ConformanceVector.
Recorded as **Finding F-06**.

---

## 9. Witness + Evidence Contract

### 9.1 The evidence law

**INV-RC-WIT-1 — Artifact is not evidence.** An artifact is a claim. Evidence is
an observation of that artifact made by something other than the thing that
produced it.

**INV-RC-WIT-2 — Unobserved is never passed.** A property that could not be
checked is reported `NOT WITNESSED` with the reason it could not be checked. It
is never reported as a pass, and never silently omitted.

**INV-RC-WIT-3 — Human judgment is not machine evidence.** Design quality,
premium atmosphere, and appropriateness are not witnessable. A witness that
claims them is lying about its own nature.

**INV-RC-WIT-4 — Witness independence.** A witness may not be produced by the
stage it witnesses in a way that lets the stage choose its own verdict.

**INV-RC-WIT-5 — Stated scope.** A green witness asserts only the specific
properties it checked, and enumerates what it did not.

### 9.2 Contract

```
INPUT                 an artifact + a witness specification
OUTPUT                a witness record: per-property pass / fail / not-witnessed,
                      each with detail
INVARIANTS            INV-RC-WIT-1 … 5
FORBIDDEN AUTHORITY   may not repair; may not adjudicate conformance; may not
                      promote; may not suppress a not-witnessed result
SEMANTIC SOURCE MAP   every witness result references the artifact node(s)
                      inspected
```

### 9.3 HBC v0.1 AS FOUND

HBC satisfies the *spirit* of INV-RC-WIT-2, -3 and -5 as found: 16 checks pass,
3 are reported `NOT WITNESSED` with stated reasons (no browser runtime; reflow
requires a layout engine; human design judgment is not machine evidence), and
`WITNESS.md` enumerates the unwitnessed gaps rather than burying them.

INV-RC-WIT-4 is **not** satisfied: HBC witnesses its own emission within the same
process. Recorded as **Finding F-07**. Note this is a structural observation
about independence, not an allegation of inaccuracy — the checks are real and
several were verified to fail correctly under deliberate corruption.

---

## 10. Semantic Drift Law

### 10.1 Definition

**Drift** is any difference between the reference conformance vector and a
target conformance vector that is not accounted for by a declared
CapabilityDecision.

```
difference + declared decision   →  ADAPTATION   (lawful)
difference + no decision         →  DRIFT        (violation)
```

### 10.2 Invariants

**INV-RC-DRIFT-1 — Decision accounting.** Every difference is either matched to a
`SUBSTITUTED` / `DEGRADED` / `ABSENT` decision, or it is drift.

**INV-RC-DRIFT-2 — Drift is not a defect report.** Drift names a divergence. It
does not name a cause, a culprit stage, or a fix.

**INV-RC-DRIFT-3 — Detection never authorizes repair.** Discovering drift confers
no authority to change anything. The chain of INV-RC-SSM-3 is mandatory.

**INV-RC-DRIFT-4 — Tolerance must be declared in advance.** Any tolerance class
is declared before the run. Tolerance widened after observing a failure is
falsification of the proof, not adjustment of it.

**INV-RC-DRIFT-5 — Drift is symmetric.** Drift is a property of a *pair* of
vectors. It does not identify which side is wrong. The reference is the
authority on meaning (§4), but a reference interpreter may itself be defective,
and RCP does not presume otherwise.

---

## 11. Adjudication + Promotion Boundary

### 11.1 The promotion ladder

```
UNCLASSIFIED  →  CANDIDATE  →  CONFORMANT  →  SEALED
```

| Status | Meaning | Requires |
|---|---|---|
| `UNCLASSIFIED` | Exists; unassessed against RCP. | — |
| `CANDIDATE` | Executable, custody established, submitted to RCP jurisdiction. | Custody witness |
| `CONFORMANT` | Passed a conformance run under a sealed RCP. | Oracle result + adjudication |
| `SEALED` | Conformance recorded as durable law. | Founder authority |

### 11.2 Invariants

**INV-RC-ADJ-1 — Execution is not conformance.** That an organ works, is well
tested, and is deterministic promotes it no further than `CANDIDATE`. HBC's
75/75 tests and proven determinism are not conformance evidence.

**INV-RC-ADJ-2 — No self-promotion.** No organ, oracle, or document may promote
its own status.

**INV-RC-ADJ-3 — Custody precedes judgment.** An organ must have an immutable
recorded baseline before it can be judged, or the judgment has no fixed subject.

**INV-RC-ADJ-4 — No retroactive redefinition.** The protocol may not be edited to
make an existing organ conform. An organ is evaluated as found.

**INV-RC-ADJ-5 — Promotion is a founder act.** Adjudication and promotion are
never automatic consequences of an oracle result.

### 11.3 Current register

```
OURSELF RCP v0.1                          DRAFT · NOT SEALED
Semantic Kernel                           MEMBERSHIP NOT SEALED
RealityIR                                 CANONICAL FORM DRAFTED · NOT SEALED
Reference Interpreter                     NOT IMPLEMENTED
Capability Resolver                       VOCABULARY DRAFTED · NOT IMPLEMENTED
Conformance Oracle                        NOT IMPLEMENTED
Semantic Source Map                       CONTRACT DRAFTED · NON-AUTHORITY-BEARING

TARGET SUBSTRATES
  WEB — HBC HTML Realm Compiler v0.1
        STATUS            CANDIDATE
        CUSTODY           WITNESSED · e350205 · 98fb73e3…cfded7
        EXECUTABLE        YES · 75/75 tests · deterministic
        DIFFERENTIATION   PROVEN (target-local quality law, §0.3)
        RC CONFORMANCE    NOT ESTABLISHED
  iOS
        STATUS            NOT IMPLEMENTED · NOT AUTHORIZED

RC-0001                                   SPECIFICATION FROZEN
                                          EXECUTION NOT AUTHORIZED
REALITY COMPILER                          NOT YET PROVEN
```

---

## 12. RC-0001 Proof Specification

### 12.1 The claim under test

> One SemanticProgram, compiled onto two substrates through the governed
> pipeline, produces two artifacts whose observable consequences are equivalent
> under the declared capability decisions.

### 12.2 Falsification condition

RC-0001 **fails** if any observable difference exists that is not accounted for
by a declared CapabilityDecision — that is, if any drift is found (§10.1).

Stating the falsification condition first is deliberate. A proof specification
that cannot say in advance what would refute it is not a proof specification.

### 12.3 Required components

RC-0001 cannot execute until all of the following exist and are sealed:

1. Sealed Semantic Kernel membership (§2.2 — currently open)
2. Sealed observation vocabulary (§4.4 — currently open, Finding F-05)
3. An implemented Reference Interpreter (§4)
4. An implemented Capability Resolver (§5)
5. Two conformant emitters (§7)
6. An implemented Conformance Oracle (§8)
7. Declared tolerance classes (INV-RC-DRIFT-4)

**None of these exist.** RC-0001 is specified, not runnable.

### 12.4 The asymmetric structure — recorded

The existence of HBC changes the shape of RC-0001 favourably:

```
              RCP v0.1
                 │
        ┌────────┴────────┐
        ▼                 ▼
   ADAPT EXISTING      CREATE NEW
       (HBC)              (iOS)
        │                 │
        └────────┬────────┘
                 ▼
              RC-0001
```

This tests something stronger than two purpose-built emitters would: whether a
**pre-existing organ, built before the constitution and without knowledge of
it**, can submit to that constitution without being rewritten into a fake proof.
An organ built to pass proves the builder's intent. An organ built earlier and
independently, then submitted, proves the constitution's reach.

This is why INV-RC-ADJ-4 and Finding F-01's no-repair posture matter more than
they appear to: the value of HBC as an RC-0001 subject is a direct function of
its having been built in ignorance of RCP. Every pre-conformance edit to HBC
reduces the scientific value of the eventual result.

### 12.5 Contract

```
INPUT                 one SemanticProgram + two sealed substrate profiles
OUTPUT                a proof record: conformance or drift, with vectors and
                      SSM segments
INVARIANTS            all invariants of §§1–11
FORBIDDEN AUTHORITY   may not modify any organ under test; may not widen
                      tolerance after observation; may not promote; may not
                      repair
SEMANTIC SOURCE MAP   full chain retained from SemanticProgram to every
                      observation on both substrates
```

---

## 13. Findings Register

Recorded, not resolved. Each requires adjudication outside design-only
authority. No finding has been repaired, and no frozen law has been changed to
accommodate one.

| ID | Finding | Bears on |
|---|---|---|
| **F-01** | HBC exposes target-local ancestry (`data-section`, `data-primitive`, `data-realm`, `data-voice`) but no declared packet-path ancestry. Under INV-RC-SSM-2 as drafted, convention-recoverable ancestry is insufficient. Explicitly **not repaired** — repairing it would coach the specimen before the examination. | §1.4, §7.3 |
| **F-02** | HBC's Realm Packet is substrate-shaped and so cannot be a RealityIR under INV-RC-IR-4. Whether it *is* a TargetIR, or should *derive* from one, is undecided. This determines whether HBC is adapted or fronted by a new adaptation stage. | §3, §6 |
| **F-03** | HBC declares absences it was told about in its packet; it has no capability *profile* and no per-requirement decision record. Its honesty is authored, not resolved. | §5 |
| **F-04** | HBC's unreachable `CANONICAL` is a capability decision of the static-HTML substrate, not a kernel truth. Whether the kernel authority vocabulary is ClientPortal's three states or a superset is undecided. | §2.5 |
| **F-05** | The normalized observation vocabulary is unsealed. Without it, §4, §8 and §10 cannot be implemented and RC-0001 cannot run. This is the tightest dependency in the protocol. | §4.4, §8 |
| **F-06** | HBC's `witness.json` carries HTML/CSS-specific check ids, not normalized observations. It cannot currently produce a ConformanceVector. | §8.5 |
| **F-07** | HBC witnesses its own emission in-process, so INV-RC-WIT-4 (witness independence) is unsatisfied. A structural observation about independence, not an allegation of inaccuracy. | §9.3 |
| **F-08** | The strategic freeze existed only in conversation until this document. This artifact is now its first durable body. Whether the freeze requires its own separate record, or is adequately embodied here, is undecided. | Preamble |

### 13.1 Contradictions requiring doctrine change

**None encountered.** Authorship did not require altering any frozen law. Where
the frozen doctrine was silent, the silence is recorded above as an open
finding rather than filled.

---

## Closing boundary

This document is **design only**. It authorizes no implementation, no HBC
mutation, no Swift, no React, no interpreter, no oracle, no emitter adaptation,
and no RC-0001 execution.

It evaluates HBC v0.1 **as found at `e350205`** and does not redefine it
retroactively to make it conform. Six of seven emitter invariants already have
a corresponding property in HBC; the gaps are named and deliberately left open.

The specimen is in the archive. The law that will judge whether it belongs to
the species is now drafted, unsealed, and awaiting adjudication.

---

*Preservation and distinction together: same must remain same, different must
remain different. Either alone is a weaker claim than both.*
