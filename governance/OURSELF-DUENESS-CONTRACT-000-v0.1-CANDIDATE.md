# OURSELF-DUENESS-CONTRACT-000 — v0.1 CANDIDATE

```
STATUS:            CANDIDATE — SEMANTIC DOCTRINE ONLY. Nothing herein is
                   ratified, nothing is implemented, nothing grants authority.
                   CandidateAuthored != CandidateReviewed != Ratified.
AUTHORED:          2026-08-20, on separate Founder authorization ("authorize
                   OURSELF-DUENESS-CONTRACT-000 semantic candidate authoring
                   against custodied DUE-01").
EVIDENCE BASIS:    REQUIRED ADJUDICATED BASIS — HBCSELF-DUE-01 @ b4c80e4
                   (return sha256 7db6119d…c382f4d). Every law herein either
                   restates a DUE-01 surviving law, seats a DUE-01-mandated
                   repair, or seats a Founder commissioning directive from the
                   authorizing transmission (marked FOUNDER-COMMISSIONED).
                   NEIGHBORING ESTABLISHED BOUNDARY LAW — ADJ-02 @ 055841c
                   (crossings-only witness law; WITNESS-CONSTITUTION-REQUIRED;
                   W-9 dueness machinery), consulted where basis admission
                   touches exposure; its bytes and vocabulary are UNTOUCHED.
                   PRESSURE LINEAGE ONLY — DUENESS-HBC-0001 @ 7c4486b, cited
                   nowhere as authority (PressureCustodied != PressureEstablished).
OPERATIONAL NOTE:  U-9 (third-register custody organ) is a NAMED OPERATIONAL
                   DEPENDENCY of any future evaluator. Its construction is NOT
                   authorized by this artifact and this artifact makes NO
                   housing decision for it (§9).
SCOPE CEILING:     dueness stratum ONLY. The second membrane
                   (disposition → jurisdiction → actor → authority →
                   transition) is a separate stratum and a separate future
                   artifact. MICROAUTO implementation is PROHIBITED here.
```

---

## §1 ROOT THEOREM

The entire contract exists to make this one property a conformance obligation
rather than a philosophical expectation:

> **T-1.** SameAdmittedClosedBasis + SameDuenessContractVersion
> ⇒ SameDuenessDisposition.

Deterministic, idempotent, fail-closed — with zero authority effect and zero
action. Any evaluator, any substrate, any restart, any number of repetitions.
An evaluation whose result can differ from another evaluation over the same
admitted closed basis under the same contract version is nonconformant, and
the difference is a defect in the evaluator or the basis admission — never a
lawful ambiguity of dueness.

Corollary (two-evaluator law, from DUE-01's extended replay): two evaluators
either receive the identical admitted basis and MUST return the identical
disposition, or they receive different admitted bases and are NOT evaluating
the same dueness instance. There is no third case.

## §2 THE DuenessContract (the single mint, ADJUDICATED_NECESSITY per DUE-01)

A DuenessContract is a standing, versioned, institutionally admitted rule that
derives obligation state from custodied evidence. It is the class-level
generalization of the per-relation authoring act already adjudicated in ADJ-02
W-9. Its schema (every field mandatory):

```
dueness_contract:
  contract_id:            stable identity, never reused
  version:                pinned; any change = new version, prior versions immutable
  admitting_jurisdiction_ref:  the seat that admitted this contract
                          (SEAT REGISTERED OPEN — see §13; this artifact
                          names the slot, never fills it)
  subject_scope:          mechanical pattern over typed custodied subjects —
                          never a prose description, never model-interpreted
  due_species:            the obligation species this contract can derive
  basis_ref_classes:      enumerated, closed list of the named custodied ref
                          classes the rule may consume; EACH class carries its
                          named witness constitution (§7) — an unwitnessable
                          class makes the contract INADMISSIBLE
  rule:                   total, computable, authored function over the
                          admitted basis; defined for every input in scope;
                          no model evaluation, no prose parsing, no clock
  activation_event_class: the witnessed event class that transitions a derived
                          obligation from latent to due (the bridging term, §8)
  missing_basis_disposition:  explicit fail-closed result when a named basis
                          ref is not establishable (default UNRESOLVED; a
                          contract MAY name NOTHING_DUE explicitly; silence
                          is not permitted)
```

**Contract admission is the institutional act** (DUE-01's S54 reconciliation):
admission of a contract at a version, by the admitting jurisdiction, is the
one-time authoring act that pre-pays institutional admission at the class
level. Mechanical derivation under an admitted contract thereafter requires no
per-disposition admission. `ContractAdmitted != AnyDispositionEstablished`.

## §3 CLOSED BASIS AND THE BASIS ADMISSION MEMBRANE

**Closed-basis law (DUE-01, ADJUDICATED_NECESSITY).** The basis of an
evaluation is a closed, ordered, enumerated set of named custodied refs — the
BasisRefSet. Contracts enumerate refs by class; they never quantify over "the
state." Anything outside the BasisRefSet cannot influence the result; an
evaluator observed consuming an unlisted input is nonconformant.
`EvaluationContext` does not exist in this stratum: everything lawful that was
ever imagined inside it is either a basis ref or the admitted-contract-set
ref; everything else is smuggled judgment. There is no Epoch input: time
enters only as witnessed, custodied events, and time-triggered dueness is
BLOCKED until a clock authority is seated (§13).

**Basis admission membrane (FOUNDER-COMMISSIONED; seam to ADJ-02).**

> **L-1.** InstitutionPossesses(X) ≠ XAdmittedToDuenessBasis.
> **L-2.** AvailableEvidence ≠ AdmissibleEvidenceForThisComputation.

Custody is not admission. Matter the institution holds — even at ESTABLISHED
standing — enters a BasisRefSet only through the basis admission membrane:
the ref belongs to a class the contract enumerates, the class's witness
constitution is satisfied for this ref, AND no exposure or independence
membrane (ADJ-02 stratum) protects the ref from this evaluator. An evaluator
may never reason "X exists in the repository, therefore I may consume X."
This is where ADJ-02 and DUE-01 meet without merging: ADJ-02 law governs what
crossing into the evaluator's surface would mean; this contract governs what
may lawfully cross. Consequently (DUE-01's evaluator non-cognition law): the
evaluator must be non-cognitive, or its own basis reads constitute exposure
crossings and can breach the very blinds its evaluation accounts for.

## §4 EVALUATION SEMANTICS AND RESULT VOCABULARY

```
D = Evaluate(BasisRefSet, AdmittedContract@Version)
D ∈ { NOTHING_DUE | DUE | UNRESOLVED }        — three values, per DUE-01
```

DUENESS_CONFLICT is not a species (DUE-01 kill 3). Two compatible applicable
contracts yield two independent dispositions; servicing order is
authority-stratum matter. A jointly incoherent applicable contract set is an
evaluability failure: UNRESOLVED with reason-class CONTRACT_SET_INCOHERENT.

**Fail-closed defaults (both mandatory, never conflated):**
- **F-1.** NoApplicableAdmittedContract ⇒ NOTHING_DUE. Never "ask a model
  what should happen next."
- **F-2.** ApplicableContract + named basis ref not establishable ⇒ the
  contract's explicit missing_basis_disposition (default UNRESOLVED).
  Missing evidence never silently extinguishes an obligation — and (two-strata
  correction, DUE-01) that sentence governs the DERIVATION stratum; on the
  LINEAGE stratum the parallel law is that evidence loss never deletes an
  established disposition (§6).

**Reason register.** UNRESOLVED always carries a typed reason-class (initial
vocabulary: CONTRACT_SET_INCOHERENT; BASIS_REF_UNESTABLISHABLE;
BASIS_MEDIA_UNKNOWN; SUBJECT_SEAT_TIER_UNADJUDICABLE). Reasons are typed
register entries, not prose.

**Uniform-UNRESOLVED anti-leak law (DUE-01, seatable now).**

> **L-3.** UNRESOLVED over held matter MUST be bytewise indistinguishable
> from UNRESOLVED over absent matter, to every reader not lawfully exposed
> to the held matter.

EvaluationFailureSemantics must not reveal protected basis state. Without
L-3 the dueness layer is an oracle over hidden Matter and every blind it
touches is breachable by asking about obligations.

**Zero-effect law.** DUE → zero authority effect. NOTHING_DUE → zero
authority effect. UNRESOLVED → zero authority effect. Every result value
carries AUTHORITY_EFFECT: NONE, structurally. The evaluator knows nothing
about authorization outcomes; DUE_NOT_AUTHORIZED is a second-membrane value
and MUST NOT appear in this vocabulary.

## §5 DISPOSITION IDENTITY, IDEMPOTENCE, SUCCESSION

> **L-4 (identity).** DuenessDispositionID = identity over
> (ContractVersion, Subject, DueSpecies, BasisRefSet).

No clock element; restart-preservation is thereby trivial. Any hash is
implementation detail; the tuple is the law.

> **L-5 (derivation idempotence).** SameBasisEvaluation ≠ NewObligation.
> Re-evaluation over the same tuple re-derives the same identity — a
> re-evaluation witness, never a new disposition. This law is also the
> termination guarantee of any mechanical accounting loop built above it.

> **L-6 (register idempotence).** Re-derivation of an existing identity
> appends a re-evaluation witness, never a duplicate entry — including
> across a crash between derivation and append.

> **L-7 (successor continuity).** A successor disposition (new basis, new
> contract version) MUST carry an explicit relation to its predecessor.
> Drifting state may never litter unlinked dispositions.

## §6 DISPOSITION LINEAGE — APPEND-ONLY, NEVER DELETION

`NotCurrentlyDue ≠ NeverWasDue. Satisfied ≠ Deleted.` (ESTABLISHED-BY-
DERIVATION from estate append-only discipline.) Disposition relations:

- **SATISFIED_BY → disposition-record ref** — lawful; consumes the existing
  discharge machinery.
- **SUPERSEDED_BY → successor identity** — lawful; L-7 as an edge.
- **CANCELLED_BY → authority-stratum act ref** — lawful ONLY when authored by
  the contract-admitting jurisdiction or its superior. **Never the debtor,
  never the evaluator, never any mechanical accounting layer** — a mechanical
  layer that can cancel obligations has acquired authority by construction.
  The lawful roster is UNRESOLVED (§13); the separation is law now.
- **EXPIRED_BY — INADMISSIBLE** until a clock/epoch authority and a seated
  mechanical comparer exist. A contract carrying expiry fails admission (§7).
- REMAINS_DUE is not a relation. It is the unmarked default — the absence of
  any disposition edge. It is never appended.

## §7 THE CONTRACT ADMISSION GATE

> **L-8 (contract-witnessability admission law; WITNESS-CONSTITUTION-REQUIRED
> applied to contracts, per DUE-01).** Every event class and every basis-ref
> class a contract names MUST carry a constituted witness at contract
> admission time. A contract naming an unwitnessable predicate — cognition
> (never an institutional observable, ADJ-02 governing law), exposure or
> situation events before the J-1 repair is custodied, unclocked time — is
> INADMISSIBLE at the gate. Refusal at admission, never admitted-then-
> perpetually-UNRESOLVED.

The admitting jurisdiction itself is an OPEN SEAT (§13). This artifact
constitutes the gate's law, names the seat's slot, and fills nothing.

## §8 BRIDGING LAW TO ADJ-02 (historical vocabulary untouched)

> **L-9.** ADJ-02 W-9's per-relation `dueness_trigger` = the
> activation_event_class term of an instance-level DuenessRule under this
> contract form. Activation semantics identical in both: a witnessed event
> class transitioning an admitted obligation from latent to due. Execution
> semantics NONE in both: `DuenessRule ≠ ExecutionTrigger` — the rule
> establishes obligation state and causes nothing to execute.

ADJ-02's bytes, vocabulary, and default-deny law ("a relation with no
authored dueness_trigger never becomes due") stand unedited; this bridge
prevents two organs of law over one phenomenon (the F-6→G-9→J-1 defect class
at a fourth stratum).

## §9 REGISTER INDEPENDENCE (FOUNDER-COMMISSIONED)

Before U-9 exists, this contract proves it does not need U-9 to mean
anything — else the register quietly becomes the ontology because it is the
thing that stores the ontology:

> **L-10.** REGISTER ≠ DUENESS LAW. Storage ≠ Semantics.
> **L-11.** PersistingADisposition ≠ EstablishingADisposition — establishment
> is the lawful derivation under an admitted contract over an admitted basis;
> the register write is durable custody of an already-established fact.
> **L-12.** RegisterWrite ≠ Authority — appending a disposition grants,
> routes, and executes nothing.
> **L-13.** RegisterAbsence ≠ SemanticImpossibility — every law in this
> artifact is well-defined today, with no register built. U-9 bounds what can
> OPERATE, never what is TRUE.

The contract determines what a valid dueness disposition means. U-9, when
separately authorized, gives dispositions durable operational representation
— nothing more. This artifact makes no U-9 housing decision.

## §10 NON-COLLAPSE LAW TABLE (surviving DUE-01 laws, restated at their grades)

| Law | Grade |
|---|---|
| State ≠ Dueness (root; generalizes custodied J-4/W-9) | ADJUDICATED_NECESSITY |
| Admissibility ≠ Dueness; NextAdmissibleTransition ≠ NextRequiredTransition — a terminal's "next admissible transition" is a declarative admissibility claim; absent an admitted contract it derives NOTHING_DUE, mechanically. No label substitutes for this law (labels are non-normative hygiene) | ADJUDICATED_NECESSITY |
| Due ≠ Authorized (one bidirectional law); scoped DUE_NOT_AUTHORIZED → QUIESCENT lives in the second membrane | ADJUDICATED_NECESSITY |
| UnknownDueness ≠ NothingDue | ADJUDICATED_NECESSITY |
| DuenessCanExistBeforeActorInstanceResolution | ADJUDICATED_NECESSITY |
| DuenessRule ≠ ExecutionTrigger (class-level standing prohibition) | ADJUDICATED_NECESSITY |
| L-1..L-13, F-1, F-2, T-1 above | ADJUDICATED_NECESSITY (L-1/L-2, L-10..L-13 FOUNDER-COMMISSIONED, subject to hostile review) |
| NotCurrentlyDue ≠ NeverWasDue; Satisfied ≠ Deleted | ESTABLISHED-BY-DERIVATION |
| Meta-dueness stratification (obligation-about-obligation termination) | UNRESOLVED (§11 row M) |

Killed vocabulary is not restated as law; the kill record lives in DUE-01
@ b4c80e4 and is normative for this artifact by reference.

## §11 CONFORMANCE KILL MATRIX (binding on any future evaluator)

Original ten rows (DUENESS-HBC-0001 §7, as adjudicated) PLUS the DUE-01
extension — all mandatory before any implementation claim:

| # | Hostile row | Required result |
|---|---|---|
| 11 | Contract-version skew mid-evaluation | evaluation VOID; re-run under one pinned version; never a blend |
| 12 | Same species, same subject, two jurisdictions' contracts | must be defined at admission (two dispositions or jurisdiction-collision refusal); silence inadmissible |
| 13 | Retroactive basis repair (appended correction supersedes a basis record) | prior disposition stands on its pinned refs; successor derivable; never silently extinguished or re-graded |
| 14 | CONTRACT_SET_INCOHERENT resolution | authority-stratum act producing new contract versions; never an accounting-layer output |
| 15 | **Held-basis row** | UNRESOLVED, bytewise indistinguishable from UNRESOLVED-over-absent (L-3) |
| M | Meta-dueness (contract whose subject is a disposition or the register) | stratification/termination test; grade currently UNRESOLVED |
| 17 | Media-UNKNOWN basis event | UNRESOLVED, reason BASIS_MEDIA_UNKNOWN |
| 18 | Subject or debtor names a seat/chamber, not an identity | UNRESOLVED until the seat-tier clause exists; never silently coerced to an identity |
| 19 | Crash between derivation and append; register replay | exactly one live entry (L-6) |
| 20 | CANCELLED_BY authored by debtor/evaluator/mechanical layer | REFUSED, and the refusal witnessed |
| R4 | **Two-evaluator replay**: same state, different evaluator instances, different exposure-policy states | same DispositionID — the test that falsifies projection-relative identity; restart-replay alone cannot catch it |

Plus the three original replay tests (500× same-basis → one identity;
restart → same identity; superseding state → predecessor preserved with
explicit relation).

## §12 GENESIS SPECIMEN (narrowed per DUE-01 D-12)

The first milestone of any lawful automation above this stratum is
NON-ACTION, stated as a bounded witnessed claim:

run R evaluates admitted contract C over admitted basis B → disposition
appended (positive register crossing, witnessed) → second-membrane record
DUE_NOT_AUTHORIZED appended (positive crossing, witnessed, OUTSIDE this
vocabulary) → instrumented, named write-set shows no further append during R.

> **L-14.** BoundedNoEffectWitness ≠ NothingHappenedAnywhere. The negative
> claim is scoped to a named write-set with an enumerated instrument whose
> own witness constitution is named — per-run, accumulating, never universal.
> Universal quiescence is a declarative fiction and is never claimed.

## §13 UNRESOLVED REGISTER (named open, filled by nothing here)

1. Exposure/situation-triggered dueness — BLOCKED until the J-1/v0.4
   boundary-grammar repair is custodied.
2. Clock/epoch authority — unseated; blocks time-triggered dueness, expiry,
   EXPIRED_BY.
3. Seat-tier identity rung (J-6/K-11) — blocks seat/chamber-grade subjects
   and debtors; "FOUNDER" as an actor-class token is unadjudicable in letter
   until seated.
4. Contract-admitting jurisdiction — the §7 gate's seat; no contract can be
   lawfully admitted by anyone today.
5. U-9 third-register custody organ — the operational ignition bottleneck;
   construction NOT authorized; no housing decision made.
6. CANCELLED_BY lawful roster (the separation is law; the roster is not).
7. Meta-dueness stratification (row M).

## §14 PROHIBITIONS (per DUE-01 MUST-NOT scope; all binding on this artifact)

No authority grant or seat filling. No routing, actor-instance resolution, or
execution machinery. No second membrane. No model-evaluated or prose-parsed
predicate. No wall-clock dependence. No new occurrence species (the
DuenessContract is a contract-class object, not an occurrence species; the
disposition is a derived standing over a contract-bound subject, not a
free-standing institutional noun — MissingBehavior ≠ MissingObject). No
exposure-triggered contract instance before the J-1 repair is custodied. No
MICROAUTO implementation or code. No U-9 housing decision. No edit to
ADJ-02/R03/v0.3 vocabulary or bytes. No completeness claim — this candidate
awaits hostile review and asserts only what its evidence basis supports.

## §15 CUSTODY DECLARATION

Authored against: DUE-01 @ b4c80e4 (required adjudicated basis); ADJ-02
@ 055841c (neighboring established boundary law); DUENESS-HBC-0001 @ 7c4486b
(pressure lineage only, no authority inherited). This candidate binds no one,
authorizes nothing, and its next lawful act is a lineage-independent hostile
review — `CandidateAuthored != CandidateReviewed != Ratified != Implemented`.
