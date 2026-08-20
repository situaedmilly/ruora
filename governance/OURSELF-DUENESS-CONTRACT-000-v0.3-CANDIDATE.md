# OURSELF-DUENESS-CONTRACT-000 — v0.3 CANDIDATE (bounded repair)

```
STATUS:            CANDIDATE — SEMANTIC DOCTRINE ONLY. Nothing herein is
                   ratified, nothing is implemented, nothing grants authority.
                   CandidateAuthored != CandidateReviewed != Ratified.
AUTHORED:          2026-08-20, on separate Founder authorization ("custody-
                   bind C000-R03, then authorize the scoped v0.3 repair" —
                   R03-1 only).
REPAIR OF:         v0.2 @ 2b392e5. This is a BOUNDED repair — scope is
                   exactly R03-1 (C000-R03, BLOCKING). R03-2 is resolved as
                   a direct byproduct of R03-1's honest repair, not
                   separately engineered. R03-3 is EXPLICITLY LEFT OPEN,
                   unrepaired — the Founder named it a non-blocking finding
                   not to be used as an expansion excuse. F-3, F-4, F-5
                   remain untouched, exactly as v0.2 left them.
EVIDENCE BASIS:    REQUIRED — HBCSELF-DUE-01 @ b4c80e4 (unchanged).
                   REQUIRED — HBCSELF-C000-R01 @ 6c4d318 (F-1, closed v0.2).
                   REQUIRED — HBCSELF-C000-R02 @ 2b53dc1 (predicate closure,
                   closed v0.2).
                   REQUIRED — HBCSELF-C000-R03 @ d3b367d (v0.2-delta review;
                   F-1 confirmed FULLY_CLOSED; R03-1 BLOCKING; R03-2/R03-3
                   non-blocking coupled findings).
                   NEIGHBORING — ADJ-02 @ 055841c; bytes/vocabulary UNTOUCHED.
                   PRESSURE ONLY — DUENESS-HBC-0001 @ 7c4486b; cited nowhere
                   as authority.
OPERATIONAL NOTE:  U-9 remains a NAMED OPERATIONAL DEPENDENCY, untouched,
                   unauthorized, no housing decision (§9, unchanged).
SCOPE CEILING:     dueness stratum ONLY, unchanged. MICROAUTO implementation
                   PROHIBITED here, unchanged.
DECLARATION-INTEGRITY CHOICE (this repair's central act): R03 offered two
                   lawful paths — name a real declaration-integrity
                   verification mechanism, or honestly demote to a named
                   UNRESOLVED item. NO REAL MECHANISM EXISTS AND NONE IS
                   INVENTED HERE. This repair takes the honest-demotion
                   path: it distinguishes what this semantic artifact CAN
                   establish (SPECIFICATION-PURE conformance) from what it
                   CANNOT establish alone (EXECUTION-PURE conformance), and
                   forbids any claim of the latter absent a separately
                   authorized witness mechanism that does not yet exist.
                   Zero new occurrence species minted; the distinction is a
                   conformance-tier LAW over existing vocabulary, not an
                   object.
```

---

## REPAIR LEDGER

**Item R03-1 (C000-R03, BLOCKING — the sole repair target).**
- *Source finding:* L-16 + extended L-8 verify that a rule's DECLARED input
  surface is a subset of BasisRefSet ∪ contract_constants. Nothing verifies
  that a rule's ACTUAL execution consumed nothing beyond what it declared.
  A rule can declare a narrow, compliant surface while its authored
  behavior silently consumes more — including matter reachable precisely
  because EvaluatorCanAccess(X) is true for some X ∉ BasisRefSet. This is
  the same defect species R01 attacked in v0.1 (a load-bearing closure
  claim asserted as an outcome-sentence with no enforceable mechanism),
  recurring one layer deeper, at L-16's own meta-level.
- *Exact defect:* `DeclaredBasis ≠ ActualDependencySet`, and nothing in
  v0.2 named or governed that gap. The phrase "or is found to consume"
  (§2, §7) and the reason-class `PREDICATE_INPUT_UNDECLARED` (§4) named an
  *outcome* without any *mechanism* by which that outcome could occur.
- *Exact repaired law:* new **L-17** (§3), constituting two conformance
  tiers — SPECIFICATION-PURE (what this contract's text can establish
  alone) and EXECUTION-PURE (SPECIFICATION-PURE plus independent
  verification that actual execution matched declaration) — and forbidding
  any EXECUTION-PURE claim absent a separately authorized witness
  mechanism, which does not exist today and is not constituted here.
- *Exact changed surface:* §3 (new L-17), §7 (L-8's "or is found to
  consume" clause now cross-references L-17 rather than implying an
  unspecified capability), §4 (item e's reason-class now has an explicit,
  honest precondition), §10 (new table row + tier caveats added to L-16,
  the Third-wall ruling, and the amended L-3), §11 (row 22 clarified to
  SPECIFICATION-PURE scope; new row 24 for the dishonest-declaration
  specimen), §12 (Genesis specimen tier caveat), §13 (new UNRESOLVED item
  8), §14 (new prohibition clause).
- *Conformance consequence:* `CannotVerifyIntegrity ≠ IntegrityFailure`,
  and `CannotVerifyIntegrity ≠ IntegrityEstablished`. No evaluator,
  register entry, or disposition record may claim EXECUTION-PURE
  conformance today. Every conformance claim this contract can currently
  support is SPECIFICATION-PURE only — and that ceiling is now stated,
  not implied.

**Item R03-2 (C000-R03, non-blocking — resolved as a byproduct).**
- *Source finding:* `PREDICATE_INPUT_UNDECLARED`'s trigger ("runtime
  detection… escaping admission-time detection") named no apparatus,
  making it presently unfireable as specified.
- *Resolution (not separately engineered):* L-17 makes the precondition
  explicit — the reason-class fires only once a separately authorized
  EXECUTION-PURE witness mechanism exists and detects a mismatch. Until
  then it is honestly documented as a defined-but-currently-dormant
  vocabulary slot (§4), not claimed operative. No new machinery was built
  to "fix" this; naming the honest precondition resolves the incoherence.

**Item R03-3 (C000-R03, non-blocking — EXPLICITLY LEFT OPEN).**
- *Source finding:* the amended L-3 broadens which result values are
  covered (all three, not UNRESOLVED alone) but not the axis of
  indistinguishability, which remains binary held-vs-absent rather than
  covering value-a-vs-value-b for different held values of X.
- *Disposition:* NOT repaired here, per the Founder's explicit instruction
  not to let non-blocking findings become expansion excuses. Left open,
  flagged in §4 and §15, awaiting its own separate authorization.

**Untouched by this repair:** F-3, F-4, F-5 (all still exactly as v0.2 left
them, per v0.2's own scope declaration, itself untouched here).

**Required surface table (Founder-specified return format):**

| Surface | v0.3 establishes |
|---|---|
| Declared basis | exact admitted dependencies — unchanged (L-1, L-15) |
| Predicate closure | no lawful undeclared reads — unchanged (L-16, L-8 EXTENDED) |
| Actual dependency integrity | **explicit inability to establish** — no mechanism invented (L-17) |
| Declaration mismatch | **fails closed** — SPECIFICATION-PURE claims stand; EXECUTION-PURE claims are forbidden absent the witness mechanism (L-17, row 24) |
| Unobservable actual dependency set | **UNRESOLVED as to EXECUTION-PURE status, never assumed clean** (L-17, §13 item 8) |
| Non-basis perturbation | cannot alter disposition — unchanged (L-15, row 21) |
| Hidden deterministic dependency | prohibited at SPECIFICATION-PURE tier — unchanged (L-16, row 22); UNGOVERNED at EXECUTION-PURE tier absent L-17's mechanism, now honestly named rather than silently assumed |
| Hidden nondeterministic dependency | prohibited — unchanged (T-1 replay + L-16) |
| Authority effect | none — unchanged |
| Execution authority | none — unchanged |

The critical row, stated as its own law: **ACTUAL DEPENDENCY SET
UNWITNESSABLE → conformance ceiling is SPECIFICATION-PURE, never assumed
EXECUTION-PURE.** Not "the declaration says it was closed, trust it."

---

## §1 ROOT THEOREM (unchanged from v0.1/v0.2)

> **T-1.** SameAdmittedClosedBasis + SameDuenessContractVersion
> ⇒ SameDuenessDisposition.

Deterministic, idempotent, fail-closed — with zero authority effect and zero
action. Any evaluator, any substrate, any restart, any number of repetitions.
An evaluation whose result can differ from another evaluation over the same
admitted closed basis under the same contract version is nonconformant, and
the difference is a defect in the evaluator or the basis admission — never a
lawful ambiguity of dueness. (This theorem's guarantee is itself
SPECIFICATION-PURE — see L-17. It governs the declared computation; it does
not, by itself, certify that any given execution obeyed it.)

Corollary (two-evaluator law, from DUE-01's extended replay): two evaluators
either receive the identical admitted basis and MUST return the identical
disposition, or they receive different admitted bases and are NOT evaluating
the same dueness instance. There is no third case.

## §2 THE DuenessContract (the single mint, ADJUDICATED_NECESSITY per DUE-01,
## unchanged from v0.2)

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
  rule:                   total, computable, authored function whose COMPLETE
                          input surface is declared at authoring time; every
                          declared input MUST be a member of basis_ref_classes
                          or a value in contract_constants (below); no model
                          evaluation, no prose parsing; NO ambient-read
                          channel of any kind — an enumerated exclusion:
                          no clock, no repository/branch state, no network,
                          no foreign SELF state, no hidden model context, no
                          undeclared memory, no environment. A rule whose
                          DECLARED surface exceeds this bound is nonconformant
                          and INADMISSIBLE (L-16). Whether a rule's ACTUAL
                          execution matches its declared surface is a
                          SEPARATE question this schema field does not and
                          cannot answer by itself (L-17).
  contract_constants:      explicitly declared, versioned, immutable values
                          pinned into the contract at admission time; the
                          ONLY non-basis source a rule may lawfully consult
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

## §3 CLOSED BASIS, PREDICATE CLOSURE, DECLARATION-INTEGRITY CEILING, AND THE
## BASIS ADMISSION MEMBRANE

**Closed-basis law (DUE-01, ADJUDICATED_NECESSITY, unchanged).** The basis of
an evaluation is a closed, ordered, enumerated set of named custodied refs —
the BasisRefSet. Contracts enumerate refs by class; they never quantify over
"the state." `EvaluationContext` does not exist in this stratum. There is no
Epoch input: time enters only as witnessed, custodied events, and
time-triggered dueness is BLOCKED until a clock authority is seated (§13).

> **L-15 (non-basis invariance; repairs C000-R01 F-1, unchanged from v0.2).**
> For any x ∉ BasisRefSet, mutating x while BasisRefSet and ContractVersion
> remain fixed MUST leave D and DuenessDispositionID unchanged. This law is
> mechanically testable (§11 row 21). It governs the SPECIFIED computation;
> whether an actual execution obeyed it is L-17's question, not this law's.

> **L-16 (predicate closure; repairs C000-R02's EXTENDS_F1 finding, specimen
> G, unchanged from v0.2).** The rule's declared input surface (§2) MUST be
> checked at contract admission (§7) against BasisRefSet classes ∪
> contract_constants. A rule that DECLARES a dependency outside that union
> is INADMISSIBLE, regardless of whether the dependency is deterministic.
> `DeterministicExternalFunction ≠ ClosedComputation`.
> `DeterministicRead ≠ AdmittedRead`. `RepeatableAmbientState ≠ ClosedBasis`.
> **Scope caveat (v0.3):** L-16 establishes SPECIFICATION-PURE closure only
> — it verifies the DECLARED surface, not the ACTUAL one. See L-17.

> **L-17 (declaration-integrity ceiling; repairs C000-R03 finding R03-1,
> NEW).** `DeclaredBasis ≠ ActualDependencySet`. L-16's admission-time check
> verifies only that a rule's DECLARED input surface is a subset of the
> admitted basis; it does not and cannot, by declaration alone, verify that
> an evaluator's ACTUAL execution consumed nothing beyond that surface.
> Consequently this contract distinguishes two conformance tiers:
>
> — **SPECIFICATION-PURE:** the contract's declared rule, basis, and
>   constants satisfy T-1, L-15, and L-16 as authored. This is the ONLY
>   tier any DuenessContract can establish by its own text, and the only
>   tier this artifact claims anywhere.
>
> — **EXECUTION-PURE:** SPECIFICATION-PURE AND a separately authorized
>   declaration-integrity witness mechanism has verified that a specific
>   evaluation's actual dependency set matched its declared surface.
>
> No evaluator, register entry, or disposition record may claim
> EXECUTION-PURE conformance absent such a witness mechanism. **None
> exists today, and none is authorized, designed, or constituted by this
> artifact.** `PuritySpecified ≠ PurityObserved`.
> `CannotVerifyIntegrity ≠ IntegrityFailure`.
> `CannotVerifyIntegrity ≠ IntegrityEstablished` — absent the witness
> mechanism, execution-level integrity is UNRESOLVED: never assumed clean,
> never assumed broken. This law introduces no new occurrence species; it
> is a conformance-tier distinction over existing vocabulary (T-1, L-15,
> L-16), not an object.

**Basis admission membrane (FOUNDER-COMMISSIONED; seam to ADJ-02, unchanged).**

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

**Third-wall ruling (repairs C000-R01 F-2, item f).** EvaluatorCanAccess(X)
is ADJ-02-stratum matter: whether an evaluator's technical reach extends to
X is governed by ADJ-02's crossings-only witness law, referenced here, never
redefined. This contract's own laws (L-1, L-2, L-15, L-16) are sufficient at
this stratum to establish SPECIFICATION-PURE closure regardless of access:
even where EvaluatorCanAccess(X) is true, L-15/L-16 forbid X's declared
influence on D unless X ∈ BasisRefSet. No third DUE-01-stratum law is
minted. **Scope caveat (v0.3):** this ruling's guarantee, like L-16's, holds
at SPECIFICATION-PURE tier. Whether an evaluator with access to X actually
respected that forbiddance in execution is an EXECUTION-PURE question,
UNRESOLVED per L-17 absent the witness mechanism.

## §4 EVALUATION SEMANTICS AND RESULT VOCABULARY

```
D = Evaluate(BasisRefSet, AdmittedContract@Version)
D ∈ { NOTHING_DUE | DUE | UNRESOLVED }        — three values, per DUE-01,
                                                 unchanged; L-17 adds a
                                                 conformance-tier LABEL
                                                 alongside D, never a
                                                 fourth D value.
```

DUENESS_CONFLICT is not a species (DUE-01 kill 3). Two compatible applicable
contracts yield two independent dispositions; servicing order is
authority-stratum matter. A jointly incoherent applicable contract set is an
evaluability failure: UNRESOLVED with reason-class CONTRACT_SET_INCOHERENT.

**Fail-closed defaults (both mandatory, never conflated, unchanged):**
- **F-1.** NoApplicableAdmittedContract ⇒ NOTHING_DUE.
- **F-2.** ApplicableContract + named basis ref not establishable ⇒ the
  contract's explicit missing_basis_disposition (default UNRESOLVED).

**Reason register.** UNRESOLVED always carries a typed reason-class (initial
vocabulary: CONTRACT_SET_INCOHERENT; BASIS_REF_UNESTABLISHABLE;
BASIS_MEDIA_UNKNOWN; SUBJECT_SEAT_TIER_UNADJUDICABLE;
PREDICATE_INPUT_UNDECLARED). **Scope caveat (v0.3, resolves R03-2):**
PREDICATE_INPUT_UNDECLARED's precondition is now explicit — it fires only
once a separately authorized EXECUTION-PURE witness mechanism (L-17) exists
and detects a declared-vs-actual mismatch. Until such a mechanism is
authorized, this reason-class is honestly documented as defined but
currently dormant — it is not claimed operative, and its absence from any
evaluator's observed behavior is not evidence of conformance.

**Uniform-anti-leak law (DUE-01, generalized per C000-R02 item g).**

> **L-3.** No result value (NOTHING_DUE, DUE, or UNRESOLVED) may be bytewise
> distinguishable, to a reader not lawfully exposed to the underlying
> matter, between the case where unadmitted matter X is held and the case
> where X is absent.

**Scope caveat (v0.3):** this guarantee is established at SPECIFICATION-PURE
tier. Its EXECUTION-PURE-tier strength — whether an evaluator's actual
behavior, not merely its declared conformance, respects this
indistinguishability — is UNRESOLVED per L-17 absent the witness mechanism.
**R03-3 remains explicitly OPEN and unrepaired here:** whether L-3's
indistinguishability axis should be widened from binary held/absent to
value-a-vs-value-b is a separate, non-blocking question the Founder
directed be left alone in this bounded act.

**Zero-effect law.** DUE → zero authority effect. NOTHING_DUE → zero
authority effect. UNRESOLVED → zero authority effect. Every result value
carries AUTHORITY_EFFECT: NONE, structurally. The evaluator knows nothing
about authorization outcomes; DUE_NOT_AUTHORIZED is a second-membrane value
and MUST NOT appear in this vocabulary.

## §5 DISPOSITION IDENTITY, IDEMPOTENCE, SUCCESSION (unchanged)

> **L-4 (identity).** DuenessDispositionID = identity over
> (ContractVersion, Subject, DueSpecies, BasisRefSet).

No clock element; restart-preservation is thereby trivial. Any hash is
implementation detail; the tuple is the law.

> **L-5 (derivation idempotence).** SameBasisEvaluation ≠ NewObligation.
> **L-6 (register idempotence).** Re-derivation of an existing identity
> appends a re-evaluation witness, never a duplicate entry.
> **L-7 (successor continuity).** A successor disposition MUST carry an
> explicit relation to its predecessor.

## §6 DISPOSITION LINEAGE — APPEND-ONLY, NEVER DELETION (unchanged)

`NotCurrentlyDue ≠ NeverWasDue. Satisfied ≠ Deleted.` Disposition relations:
SATISFIED_BY, SUPERSEDED_BY, CANCELLED_BY (jurisdiction-restricted),
EXPIRED_BY (inadmissible until clock authority), REMAINS_DUE (never
appended — unmarked default).

## §7 THE CONTRACT ADMISSION GATE

> **L-8 (contract-witnessability admission law, unchanged).** Every event
> class and every basis-ref class a contract names MUST carry a constituted
> witness at contract admission time. Refusal at admission, never
> admitted-then-perpetually-UNRESOLVED.
>
> **L-8 EXTENDED (predicate-closure admission check, unchanged text, scope
> caveat added).** The gate additionally verifies that the contract's
> DECLARED rule input surface (§2) is a subset of the admitted basis-ref
> classes ∪ contract_constants. A contract whose rule declares any input
> outside that union is INADMISSIBLE. **Scope caveat (v0.3):** this check
> operates on the DECLARED surface only. It cannot detect, and does not
> claim to detect, a rule whose ACTUAL execution consumes more than it
> declared — that is L-17's ceiling, not this gate's job. The former
> phrase "or is found to consume" is retained in §2/§7 as an honest
> forward reference to L-17's UNRESOLVED-tier machinery, not as a claim
> that this gate itself performs such detection.

The admitting jurisdiction itself is an OPEN SEAT (§13). This artifact
constitutes the gate's law, names the seat's slot, and fills nothing.

## §8 BRIDGING LAW TO ADJ-02 (historical vocabulary untouched, unchanged)

> **L-9.** ADJ-02 W-9's per-relation `dueness_trigger` = the
> activation_event_class term of an instance-level DuenessRule under this
> contract form. `DuenessRule ≠ ExecutionTrigger`.

## §9 REGISTER INDEPENDENCE (FOUNDER-COMMISSIONED, unchanged)

> **L-10.** REGISTER ≠ DUENESS LAW. Storage ≠ Semantics.
> **L-11.** PersistingADisposition ≠ EstablishingADisposition.
> **L-12.** RegisterWrite ≠ Authority.
> **L-13.** RegisterAbsence ≠ SemanticImpossibility.

The contract determines what a valid dueness disposition means. U-9, when
separately authorized, gives dispositions durable operational representation
— nothing more. This artifact makes no U-9 housing decision.

## §10 NON-COLLAPSE LAW TABLE (surviving laws + v0.2 + v0.3 repairs)

| Law | Grade |
|---|---|
| State ≠ Dueness (root) | ADJUDICATED_NECESSITY |
| Admissibility ≠ Dueness; NextAdmissibleTransition ≠ NextRequiredTransition | ADJUDICATED_NECESSITY |
| Due ≠ Authorized (bidirectional) | ADJUDICATED_NECESSITY |
| UnknownDueness ≠ NothingDue | ADJUDICATED_NECESSITY |
| DuenessCanExistBeforeActorInstanceResolution | ADJUDICATED_NECESSITY |
| DuenessRule ≠ ExecutionTrigger | ADJUDICATED_NECESSITY |
| L-1..L-14, F-1, F-2, T-1 (v0.1 laws) | ADJUDICATED_NECESSITY (hostile-reviewed by C000-R01) |
| L-15 (non-basis invariance) | ADJUDICATED_NECESSITY (repairs F-1, confirmed FULLY_CLOSED by C000-R03) |
| L-16 (predicate closure) | ADJUDICATED_NECESSITY (repairs EXTENDS_F1; confirmed FULLY_CLOSED for honest declarations by C000-R03; scope caveat added re: L-17) |
| L-3 (generalized anti-leak) | ADJUDICATED_NECESSITY (repairs item g; scope caveat added; R03-3 axis-widening question left OPEN) |
| Third-wall ruling (§3) | ADJUDICATED_NECESSITY (repairs F-2; scope caveat added re: L-17) |
| **L-17 (declaration-integrity ceiling) — NEW, v0.3** | ADJUDICATED_NECESSITY (repairs C000-R03's R03-1; NOT YET independently hostile-reviewed) |
| NotCurrentlyDue ≠ NeverWasDue; Satisfied ≠ Deleted | ESTABLISHED-BY-DERIVATION |
| Meta-dueness stratification | UNRESOLVED (§11 row M) |

Killed vocabulary is not restated as law; the kill record lives in DUE-01
@ b4c80e4 and is normative by reference. This v0.3 repair introduces ZERO
new formal primitives (objects/species) — L-17 is a conformance-tier LAW
over existing vocabulary (T-1, L-15, L-16), not an object, a witness
species, or a register. No DependencyManifest, ActualInputLedger,
EvaluationTrace, RuntimeDependencyGraph, or ExecutionContextManifest is
minted. R03's own minimality/anti-resurrection findings (TRUE, 15/15) are
extended, not spent, by this repair.

## §11 CONFORMANCE KILL MATRIX (binding on any future evaluator)

| # | Hostile row | Required result |
|---|---|---|
| 11 | Contract-version skew mid-evaluation | evaluation VOID; re-run under one pinned version |
| 12 | Same species, same subject, two jurisdictions' contracts | must be defined at admission; silence inadmissible |
| 13 | Retroactive basis repair | prior disposition stands; successor derivable |
| 14 | CONTRACT_SET_INCOHERENT resolution | authority-stratum act; never an accounting-layer output |
| 15 | Held-basis row | UNRESOLVED, bytewise indistinguishable from UNRESOLVED-over-absent (L-3) |
| M | Meta-dueness | stratification/termination test; grade UNRESOLVED |
| 17 | Media-UNKNOWN basis event | UNRESOLVED, reason BASIS_MEDIA_UNKNOWN |
| 18 | Subject/debtor names a seat/chamber | UNRESOLVED until seat-tier clause exists |
| 19 | Crash between derivation and append | exactly one live entry (L-6) |
| 20 | CANCELLED_BY authored by debtor/evaluator/mechanical layer | REFUSED, refusal witnessed |
| R4 | Two-evaluator replay, different exposure-policy states | same DispositionID |
| 21 | Non-basis perturbation | D and DuenessDispositionID bytewise identical (L-15) |
| 22 | **Predicate closure / specimen G — HONEST declaration** (rule DECLARES a dependency outside BasisRefSet ∪ contract_constants) | contract INADMISSIBLE at admission (L-16). **Scope note (v0.3):** this row tests the declared surface only. |
| 23 | Foreign-SELF-state / ambient-crossing row | INADMISSIBLE at admission per L-16, deferring to ADJ-02's crossings-only witness law |
| **24** | **Dishonest declaration (NEW, v0.3, repairs R03-1):** rule's ACTUAL execution consumes input beyond its DECLARED surface — the declared surface itself is compliant | **UNTESTABLE by this artifact alone. No evaluation may claim EXECUTION-PURE conformance absent L-17's separately authorized witness mechanism. SPECIFICATION-PURE claims for OTHER evaluations under the same contract are unaffected. If a future witness mechanism detects the mismatch, the result is UNRESOLVED/PREDICATE_INPUT_UNDECLARED (§4) — never a silent DUE/NOTHING_DUE claim, and never assumed absent merely because undetected.** |

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

Note (v0.2, per C000-R02 item 10): this specimen's bounded-write-set claim
is only trustworthy once L-16 is seated; L-16 closes that precondition.

**Note (v0.3, per C000-R03/L-17):** the specimen's claim is itself
SPECIFICATION-PURE only. "The instrumented write-set shows no further
append" is a claim about the DECLARED write-set's observed behavior at
whatever tier the instrument itself operates; it does NOT, by this
artifact's own honesty requirement, upgrade to an EXECUTION-PURE guarantee
that no undeclared dependency or undeclared write occurred anywhere absent
a separately authorized witness mechanism for the instrument itself. The
specimen's text is otherwise unchanged.

## §13 UNRESOLVED REGISTER (named open)

1. Exposure/situation-triggered dueness — BLOCKED until the J-1/v0.4
   boundary-grammar repair is custodied.
2. Clock/epoch authority — unseated.
3. Seat-tier identity rung (J-6/K-11) — blocks seat/chamber-grade subjects
   and debtors.
4. Contract-admitting jurisdiction — the §7 gate's seat.
5. U-9 third-register custody organ — construction NOT authorized.
6. CANCELLED_BY lawful roster.
7. Meta-dueness stratification (row M).
8. **Declaration-integrity witness mechanism (NEW, v0.3, repairs R03-1) —
   no mechanism exists to verify a rule's actual execution matched its
   declared input surface. Until separately authorized and constituted,
   ALL conformance claims under this contract are SPECIFICATION-PURE
   only; EXECUTION-PURE is UNRESOLVED, not achievable by any amount of
   additional prose in this artifact.**

(F-4's proposed item — the concrete ADJ-02 interface predicate — remains
NOT added; F-4 is still out of this repair's scope, unchanged from v0.2.)

## §14 PROHIBITIONS (per DUE-01 MUST-NOT scope; all binding, unchanged plus
## one addition)

No authority grant or seat filling. No routing, actor-instance resolution, or
execution machinery. No second membrane. No model-evaluated or prose-parsed
predicate. No wall-clock dependence. No new occurrence species. No
exposure-triggered contract instance before the J-1 repair is custodied. No
MICROAUTO implementation or code. No U-9 housing decision. No edit to
ADJ-02/R03(boundary-grammar)/v0.3(boundary-grammar) vocabulary or bytes. No
completeness claim. **No claim of EXECUTION-PURE conformance is authored,
implied, or made implementable by this artifact anywhere (L-17, NEW v0.3)
— every claim this contract can lawfully support is SPECIFICATION-PURE,
stated as such.**

## §15 CUSTODY DECLARATION

Authored against: DUE-01 @ b4c80e4 (required adjudicated basis); C000-R01
@ 6c4d318 (F-1, closed in v0.2); C000-R02 @ 2b53dc1 (predicate closure,
closed in v0.2); C000-R03 @ d3b367d (v0.2-delta review; R03-1 repaired
here; R03-2 resolved as byproduct; **R03-3 explicitly left open,
unrepaired**); ADJ-02 @ 055841c (neighboring established boundary law,
bytes untouched); DUENESS-HBC-0001 @ 7c4486b (pressure lineage only, no
authority inherited). This candidate binds no one, authorizes nothing, and
its next lawful act is a lineage-independent hostile review of the v0.3
delta (L-17, the scope caveats added to L-16/L-3/Third-wall-ruling, §11
row 24, §13 item 8) — `CandidateAuthored != CandidateReviewed != Ratified
!= Implemented`. F-3, F-4, F-5, and R03-3 remain open and unrepaired.
