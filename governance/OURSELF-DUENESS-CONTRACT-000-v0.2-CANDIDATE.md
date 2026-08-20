# OURSELF-DUENESS-CONTRACT-000 — v0.2 CANDIDATE (bounded repair)

```
STATUS:            CANDIDATE — SEMANTIC DOCTRINE ONLY. Nothing herein is
                   ratified, nothing is implemented, nothing grants authority.
                   CandidateAuthored != CandidateReviewed != Ratified.
AUTHORED:          2026-08-20, on separate Founder authorization ("authorize
                   the widened v0.2 repair" — F-1 + items c–g).
REPAIR OF:         v0.1 @ c43a203. This is a BOUNDED repair — scope is
                   exactly F-1 (C000-R01) + predicate closure items c–g
                   (C000-R02, EXTENDS_F1 finding). F-2 through F-5 are NOT
                   touched here; they stand exactly as R01 left them and
                   await their own separate repair authorization.
EVIDENCE BASIS:    REQUIRED — HBCSELF-DUE-01 @ b4c80e4 (unchanged from v0.1).
                   REQUIRED — HBCSELF-C000-R01 @ 6c4d318 (F-1 finding).
                   REQUIRED — HBCSELF-C000-R02 @ 2b53dc1 (predicate-closure
                   EXTENDS_F1 finding, specimen G, items c–g).
                   NEIGHBORING — ADJ-02 @ 055841c; bytes/vocabulary UNTOUCHED.
                   PRESSURE ONLY — DUENESS-HBC-0001 @ 7c4486b; cited nowhere
                   as authority.
OPERATIONAL NOTE:  U-9 remains a NAMED OPERATIONAL DEPENDENCY, untouched,
                   unauthorized, no housing decision (§9, unchanged).
SCOPE CEILING:     dueness stratum ONLY, unchanged from v0.1. MICROAUTO
                   implementation PROHIBITED here, unchanged.
```

---

## REPAIR LEDGER (this section is the delta; §1–§15 below is the full
## resulting text). Each item: source finding → exact defect → exact
## repaired law → exact changed surface → conformance consequence.

**Item F-1 (C000-R01, BLOCKING).**
- *Source finding:* §3's closed-basis invariance was asserted only as
  unlabeled prose ("anything outside the BasisRefSet cannot influence the
  result"), with no L-/T-number and no dedicated §11 kill-matrix row.
- *Exact defect:* the artifact's single most load-bearing determinism claim
  broke its own numbering discipline and was untestable by its own
  conformance apparatus.
- *Exact repaired law:* new **L-15** (§3), stating the invariance as a
  numbered, testable equivalence.
- *Exact changed surface:* §3 (new L-15), §10 (new table row), §11 (new
  row 21).
- *Conformance consequence:* an evaluator's result MUST now be replay-tested
  under non-basis perturbation (row 21); divergence is a defined
  nonconformance, not an ambiguity.

**Item c (C000-R02).**
- *Source finding:* §2's `rule` field forbade only one named ambient channel
  ("no clock"); all other ambient channels (repository/branch state,
  network, foreign SELF state, hidden model context, undeclared memory,
  environment) were unexcluded by name.
- *Exact defect:* a rule could consult any of these channels without
  violating any *named* prohibition — only the same weak §3 prose applied.
- *Exact repaired law:* §2's `rule` field definition amended to require a
  declared, complete input surface and an enumerated (not single-case)
  ambient-read exclusion.
- *Exact changed surface:* §2 schema, `rule` field.
- *Conformance consequence:* a rule's declared inputs become the object of
  the admission-time check (item d); undeclared ambient consumption is a
  schema violation, not merely a runtime hope.

**Item d (C000-R02, decisive — specimen G).**
- *Source finding:* R02's specimen G — a deterministic external function
  whose input/state is not bound into BasisRefSet — passes every existing
  replay test indefinitely (same basis, same contract, same output, every
  run) while remaining constitutionally open. Determinism does not imply
  closure.
- *Exact defect:* no admission-time mechanism existed to catch an
  unenumerated dependency; only replay-testing existed, and replay-testing
  is structurally blind to a stable hidden dependency.
- *Exact repaired law:* new **L-16** (§3) plus an extension to the §7
  admission gate (L-8) requiring the declared input surface (item c) to be
  checked against BasisRefSet classes ∪ contract-pinned constants at
  admission time.
- *Exact changed surface:* §3 (new L-16), §7 (L-8 extended), §11 (new
  row 22 exercising specimen G directly), §4 (new reason-class, see item e).
- *Conformance consequence:* `DeterministicExternalFunction ≠
  ClosedComputation`; `DeterministicRead ≠ AdmittedRead`;
  `RepeatableAmbientState ≠ ClosedBasis`. A contract whose rule depends on
  an undeclared input is INADMISSIBLE at the gate, regardless of the
  dependency's stability under replay.

**Item e (C000-R02).**
- *Source finding:* if an undeclared read escapes admission-time detection
  and is caught only at runtime, no result value existed for it without
  either silently admitting the read or minting a new top-level enum value.
- *Exact defect:* undeclared-read failure semantics were unspecified.
- *Exact repaired law:* one new reason-class, `PREDICATE_INPUT_UNDECLARED`,
  added to the EXISTING reason register (§4) — no new register, no new
  top-level D value.
- *Exact changed surface:* §4 reason register vocabulary list; §4 new
  sentence on runtime-detected undeclared reads.
- *Conformance consequence:* runtime detection of an L-16 breach yields
  UNRESOLVED/PREDICATE_INPUT_UNDECLARED — never a silently admitted value,
  an inferred value, model intuition, or dynamic basis expansion.

**Item f (C000-R02, closes C000-R01 F-2).**
- *Source finding:* R01's F-2 — the tripartite wall (Possession ≠ Access ≠
  Admission) was gestured at via §3's membrane third conjunct but never
  adjudicated as belonging to a stratum.
- *Exact defect:* ambiguity over whether EvaluatorCanAccess(X) needed its
  own DUE-01-stratum law or was already ADJ-02's territory.
- *Exact repaired law:* an explicit jurisdictional ruling sentence in §3 —
  EvaluatorCanAccess(X) is ADJ-02-stratum matter, referenced not redefined;
  L-1/L-2/L-15/L-16 are sufficient at this stratum regardless of access,
  because they forbid X's influence unless X ∈ BasisRefSet even when access
  exists.
- *Exact changed surface:* §3, new "Third-wall ruling" paragraph.
- *Conformance consequence:* no third DUE-01-stratum law is minted (per
  R02's minimality finding); the foreign-SELF-state ambient-read specimen
  (R02 specimen C) is governed by L-16's admission check, not a new
  access-law.

**Item g (C000-R02).**
- *Source finding:* L-3 as originally written covered only
  UNRESOLVED-over-held vs UNRESOLVED-over-absent indistinguishability. R02
  found the true leak surface broader: an L-16 violation could leak X's
  *value* through the primary DUE/NOTHING_DUE channel, not merely its
  presence through UNRESOLVED.
- *Exact defect:* L-3 under-scoped its own anti-leak guarantee.
- *Exact repaired law:* L-3 generalized (§4) to cover all three result
  values, not UNRESOLVED alone.
- *Exact changed surface:* §4, L-3 text.
- *Conformance consequence:* a predicate-closure violation is now doubly
  prohibited — inadmissible under L-16, and even if it escaped detection,
  its value could not lawfully leak through any result channel under the
  generalized L-3.

**Untouched by this repair:** F-3 (occurrence-species gloss), F-4 (ADJ-02
interface predicate naming / 8th UNRESOLVED item), F-5 (pure-function
framing caveat). All non-blocking, all explicitly out of scope for this
bounded act, all await separate authorization.

---

## §1 ROOT THEOREM (unchanged from v0.1)

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
  rule:                   total, computable, authored function whose COMPLETE
                          input surface is declared at authoring time (v0.2,
                          item c); every declared input MUST be a member of
                          basis_ref_classes or a value in contract_constants
                          (below); no model evaluation, no prose parsing; NO
                          ambient-read channel of any kind — this is an
                          enumerated exclusion, not a single named case:
                          no clock, no repository/branch state, no network,
                          no foreign SELF state, no hidden model context, no
                          undeclared memory, no environment. A rule found to
                          consume any input outside its declared surface is
                          nonconformant (L-16) regardless of whether that
                          input is itself deterministic (v0.2, specimen G).
  contract_constants:      explicitly declared, versioned, immutable values
                          pinned into the contract at admission time; the
                          ONLY non-basis source a rule may lawfully consult
                          (v0.2, item c)
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

## §3 CLOSED BASIS, PREDICATE CLOSURE, AND THE BASIS ADMISSION MEMBRANE

**Closed-basis law (DUE-01, ADJUDICATED_NECESSITY).** The basis of an
evaluation is a closed, ordered, enumerated set of named custodied refs — the
BasisRefSet. Contracts enumerate refs by class; they never quantify over "the
state." `EvaluationContext` does not exist in this stratum: everything lawful
that was ever imagined inside it is either a basis ref, an admitted contract
constant, or the admitted-contract-set ref; everything else is smuggled
judgment. There is no Epoch input: time enters only as witnessed, custodied
events, and time-triggered dueness is BLOCKED until a clock authority is
seated (§13).

> **L-15 (non-basis invariance; promotes v0.1's closed-basis prose to law,
> repairs C000-R01 F-1).** For any x ∉ BasisRefSet, mutating x while
> BasisRefSet and ContractVersion remain fixed MUST leave D and
> DuenessDispositionID unchanged. An evaluator whose result varies under such
> a mutation is nonconformant per T-1; this law makes that nonconformance
> mechanically testable (§11 row 21). Anything outside the BasisRefSet
> cannot influence the result; an evaluator observed consuming an unlisted
> input is nonconformant.

> **L-16 (predicate closure; repairs C000-R02's EXTENDS_F1 finding,
> specimen G).** The rule's declared input surface (§2) MUST be checked at
> contract admission (§7) against BasisRefSet classes ∪ contract_constants.
> A rule that reads, invokes, or otherwise depends upon — deterministically
> or not — any value outside that declared surface is nonconformant,
> regardless of whether the dependency is stable across replay.
> `DeterministicExternalFunction ≠ ClosedComputation`.
> `DeterministicRead ≠ AdmittedRead`. `RepeatableAmbientState ≠ ClosedBasis`.
> L-15 alone (behavioral, replay-tested) cannot detect a specimen-G-class
> violation — a stable hidden dependency passes every replay indefinitely;
> only L-16's admission-time structural check closes that residual gap.

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

**Third-wall ruling (repairs C000-R01 F-2, item f).** EvaluatorCanAccess(X)
is ADJ-02-stratum matter: whether an evaluator's technical reach extends to
X is governed by ADJ-02's crossings-only witness law, referenced here, never
redefined. This contract's own laws (L-1, L-2, L-15, L-16) are sufficient at
this stratum regardless of access: even where EvaluatorCanAccess(X) is true,
L-15/L-16 forbid X's influence on D unless X ∈ BasisRefSet. No third
DUE-01-stratum law is minted; the axis is real but its adjudication belongs
to ADJ-02, cited by reference only.

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
BASIS_MEDIA_UNKNOWN; SUBJECT_SEAT_TIER_UNADJUDICABLE;
**PREDICATE_INPUT_UNDECLARED — new, v0.2 item e**). Reasons are typed
register entries, not prose. Runtime detection of an undeclared input
consumed by a rule (an L-16 breach escaping admission-time detection) yields
UNRESOLVED/PREDICATE_INPUT_UNDECLARED — never a silently admitted read, an
inferred value, model intuition, or dynamic basis expansion.

**Uniform-anti-leak law (DUE-01, GENERALIZED per C000-R02 item g).**

> **L-3.** No result value (NOTHING_DUE, DUE, or UNRESOLVED) may be bytewise
> distinguishable, to a reader not lawfully exposed to the underlying
> matter, between the case where unadmitted matter X is held and the case
> where X is absent. This subsumes and generalizes the original
> UNRESOLVED-only, presence/absence-only form: an L-16 violation that lets
> X's value influence D leaks strictly more than presence/absence, and is
> equally prohibited.

EvaluationFailureSemantics must not reveal protected basis state. Without
L-3 the dueness layer is an oracle over hidden Matter and every blind it
touches is breachable by asking about obligations.

**Zero-effect law.** DUE → zero authority effect. NOTHING_DUE → zero
authority effect. UNRESOLVED → zero authority effect. Every result value
carries AUTHORITY_EFFECT: NONE, structurally. The evaluator knows nothing
about authorization outcomes; DUE_NOT_AUTHORIZED is a second-membrane value
and MUST NOT appear in this vocabulary.

## §5 DISPOSITION IDENTITY, IDEMPOTENCE, SUCCESSION (unchanged from v0.1)

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

## §6 DISPOSITION LINEAGE — APPEND-ONLY, NEVER DELETION (unchanged)

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
>
> **L-8 EXTENDED (predicate-closure admission check, v0.2 item d, repairs
> C000-R02's decisive finding).** The gate additionally verifies that the
> contract's declared rule input surface (§2) is a subset of the admitted
> basis-ref classes ∪ contract_constants. A contract whose rule declares —
> or is found to consume — any input outside that union is INADMISSIBLE,
> under the same refusal-at-admission discipline as an unwitnessable basis
> class. This is the check that closes specimen G: a deterministic external
> function with an undeclared or unbound input fails this check regardless
> of its output's stability under replay.

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

## §9 REGISTER INDEPENDENCE (FOUNDER-COMMISSIONED, unchanged)

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

## §10 NON-COLLAPSE LAW TABLE (surviving DUE-01 laws + v0.2 repairs, restated
## at their grades)

| Law | Grade |
|---|---|
| State ≠ Dueness (root; generalizes custodied J-4/W-9) | ADJUDICATED_NECESSITY |
| Admissibility ≠ Dueness; NextAdmissibleTransition ≠ NextRequiredTransition | ADJUDICATED_NECESSITY |
| Due ≠ Authorized (one bidirectional law); scoped DUE_NOT_AUTHORIZED → QUIESCENT lives in the second membrane | ADJUDICATED_NECESSITY |
| UnknownDueness ≠ NothingDue | ADJUDICATED_NECESSITY |
| DuenessCanExistBeforeActorInstanceResolution | ADJUDICATED_NECESSITY |
| DuenessRule ≠ ExecutionTrigger (class-level standing prohibition) | ADJUDICATED_NECESSITY |
| L-1..L-14, F-1, F-2, T-1 (v0.1 laws) | ADJUDICATED_NECESSITY (L-1/L-2, L-10..L-13 FOUNDER-COMMISSIONED, hostile-reviewed by C000-R01) |
| **L-15 (non-basis invariance) — NEW, v0.2** | ADJUDICATED_NECESSITY (repairs C000-R01 F-1, hostile-reviewed by C000-R02) |
| **L-16 (predicate closure) — NEW, v0.2** | ADJUDICATED_NECESSITY (repairs C000-R02's EXTENDS_F1 finding; NOT YET independently hostile-reviewed) |
| L-3 (generalized anti-leak) — AMENDED, v0.2 | ADJUDICATED_NECESSITY (repairs C000-R02 item g; NOT YET independently hostile-reviewed) |
| Third-wall ruling (§3) — NEW, v0.2 | ADJUDICATED_NECESSITY (repairs C000-R01 F-2; NOT YET independently hostile-reviewed) |
| NotCurrentlyDue ≠ NeverWasDue; Satisfied ≠ Deleted | ESTABLISHED-BY-DERIVATION |
| Meta-dueness stratification (obligation-about-obligation termination) | UNRESOLVED (§11 row M) |

Killed vocabulary is not restated as law; the kill record lives in DUE-01
@ b4c80e4 and is normative for this artifact by reference. This v0.2 repair
introduces ZERO new formal primitives (objects/species) — L-15, L-16, and
the third-wall ruling are laws over existing vocabulary, per C000-R02's
minimality finding.

## §11 CONFORMANCE KILL MATRIX (binding on any future evaluator)

Original ten rows (DUENESS-HBC-0001 §7, as adjudicated) PLUS the DUE-01
extension PLUS the v0.2 repair rows — all mandatory before any implementation
claim:

| # | Hostile row | Required result |
|---|---|---|
| 11 | Contract-version skew mid-evaluation | evaluation VOID; re-run under one pinned version; never a blend |
| 12 | Same species, same subject, two jurisdictions' contracts | must be defined at admission (two dispositions or jurisdiction-collision refusal); silence inadmissible |
| 13 | Retroactive basis repair (appended correction supersedes a basis record) | prior disposition stands on its pinned refs; successor derivable; never silently extinguished or re-graded |
| 14 | CONTRACT_SET_INCOHERENT resolution | authority-stratum act producing new contract versions; never an accounting-layer output |
| 15 | Held-basis row | UNRESOLVED, bytewise indistinguishable from UNRESOLVED-over-absent (L-3) |
| M | Meta-dueness (contract whose subject is a disposition or the register) | stratification/termination test; grade currently UNRESOLVED |
| 17 | Media-UNKNOWN basis event | UNRESOLVED, reason BASIS_MEDIA_UNKNOWN |
| 18 | Subject or debtor names a seat/chamber, not an identity | UNRESOLVED until the seat-tier clause exists; never silently coerced to an identity |
| 19 | Crash between derivation and append; register replay | exactly one live entry (L-6) |
| 20 | CANCELLED_BY authored by debtor/evaluator/mechanical layer | REFUSED, and the refusal witnessed |
| R4 | Two-evaluator replay: same state, different evaluator instances, different exposure-policy states | same DispositionID — falsifies projection-relative identity |
| **21** | **Non-basis perturbation (NEW, v0.2, repairs F-1):** same admitted BasisRefSet + ContractVersion, mutate any x∉BasisRefSet between runs | **D and DuenessDispositionID MUST be bytewise identical (L-15)** |
| **22** | **Predicate closure / specimen G (NEW, v0.2, repairs C000-R02's decisive finding):** rule declares or is found to invoke a deterministic external function whose input/state is not in BasisRefSet ∪ contract_constants | **contract INADMISSIBLE at admission (L-16); if escaping detection, the function's output MUST NOT influence D, and detection at runtime yields UNRESOLVED/PREDICATE_INPUT_UNDECLARED** |
| **23** | **Foreign-SELF-state / ambient-crossing row (NEW, v0.2, item f):** rule's declared input surface includes a ref governed by an ADJ-02 crossing not yet lawfully witnessed | **INADMISSIBLE at admission per L-16, deferring to ADJ-02's crossings-only witness law for whether the crossing is ever lawful** |

Plus the three original replay tests (500× same-basis → one identity;
restart → same identity; superseding state → predecessor preserved with
explicit relation).

## §12 GENESIS SPECIMEN (narrowed per DUE-01 D-12, unchanged from v0.1)

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

Note (v0.2, per C000-R02 item 10 finding): this specimen's bounded-write-set
claim is only trustworthy once L-16 is seated — an unenumerated dependency
could otherwise move D outside the instrumented set, making the claim
unfalsifiable rather than merely untested. L-16 (this repair) closes that
precondition; the specimen's text is otherwise unchanged.

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

(Unchanged from v0.1. F-4's proposed 8th item — the concrete ADJ-02
interface predicate — is NOT added here; F-4 is out of this repair's scope.)

## §14 PROHIBITIONS (per DUE-01 MUST-NOT scope; all binding on this artifact,
## unchanged from v0.1)

No authority grant or seat filling. No routing, actor-instance resolution, or
execution machinery. No second membrane. No model-evaluated or prose-parsed
predicate. No wall-clock dependence. No new occurrence species (the
DuenessContract is a contract-class object, not an occurrence species; the
disposition is a derived standing over a contract-bound subject, not a
free-standing institutional noun — MissingBehavior ≠ MissingObject). No
exposure-triggered contract instance before the J-1 repair is custodied. No
MICROAUTO implementation or code. No U-9 housing decision. No edit to
ADJ-02/R03/v0.3 vocabulary or bytes. No completeness claim — this candidate
awaits hostile review and asserts only what its evidence basis supports. This
v0.2 repair additionally introduces no new occurrence species, per the §10
minimality note.

## §15 CUSTODY DECLARATION

Authored against: DUE-01 @ b4c80e4 (required adjudicated basis, unchanged);
C000-R01 @ 6c4d318 (F-1, repaired here); C000-R02 @ 2b53dc1 (predicate
closure EXTENDS_F1, repaired here, items c–g); ADJ-02 @ 055841c (neighboring
established boundary law, bytes untouched); DUENESS-HBC-0001 @ 7c4486b
(pressure lineage only, no authority inherited). This candidate binds no
one, authorizes nothing, and its next lawful act is a lineage-independent
hostile review of the v0.2 delta (L-15, L-16, the amended L-3, the
third-wall ruling, and §11 rows 21–23) — `CandidateAuthored != CandidateReviewed
!= Ratified != Implemented`. F-3, F-4, and F-5 remain open and unrepaired.
