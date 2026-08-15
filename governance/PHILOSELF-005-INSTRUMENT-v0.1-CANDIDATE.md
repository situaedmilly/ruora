# PHILOSELF-005 — INSTRUMENT

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
REVISION:            v0.3-state-establishment-repair-001 + residual-ledger-001
                     (2026-08-15; same authorization wave; residual surfaces:
                     M-11 capability index cross-ref §3, M-20 dependency digest
                     bindings §9)
CLASS:               philoSELF foundation (5 — instrument layer)
AUTHORED:            2026-08-15
AUTHOR_SELF:         Claude Code session 74633bfb-04bf-48c4-99aa-29d87a2eabb4
AUTHORED_UNDER:      FOUNDER_CONTINUE_PHILOSELF_MANIFESTATION_001_HARDENED,
                     Phase B (CITRINITAS) — new candidate, NOT canon
CAUSAL_PARENT (v0.3-repair revisions):
  PHILOSELF-001 sha256 543e2ba148bca5cbf64034431c3d4bea4e939ab6666639dd6f09e9ca5433ac6a, 198 ln
  PHILOSELF-002 sha256 067d0c596a3a8f93036393a763efee21fccd7c68d6ac770e2155196ed7f54f8b, 298 ln
  PHILOSELF-003 sha256 f8725fc1a9e3ed1c5d673807ad81c219d8d3a75634d0be5fb4078448a74595a9, 323 ln
  PHILOSELF-004 sha256 eaa27c3247af229ccbcc85fd7d7385a8786770ba8dd6e4734d20dbc7995b70a4, 274 ln
  (v0.2 lineage preserved in git history at custody commits 00aab1e/da197c1 —
  prior digests 6ff37cdb / f70945fb / 894c9d9c / 60a2f3a9)
DESIGN_PRESSURE:     PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md (sha 03f49df9…) and
                     PHILOSELF-BOUNDARY-REVIEW-RETURN-002.md (sha e0098a8b…,
                     BLOCKED — B-1 proof-bridge and B-2 founding byte-binding
                     cured this revision; both returns = source evidence)
COMMENCEMENT:        PRE_CONSTITUTIONAL_STATE — nothing herein is in force;
                     see PHILOSELF-004 §4 INV-6
HOSTILE_REVIEW:      ROUND 2 RETURNED BLOCKED —
                     governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-002.md (sha256
                     e0098a8b7e4bba66ff13ecb49b5a082a23fd4d3b93e122b177c051a7e6582971,
                     599 lines); round 3 NOT designed, NOT issued
RATIFICATION:        NOT_GRANTED
IMPLEMENTATION:      NOT_AUTHORIZED
SUPERSEDES:          NOTHING — X1 remains FROZEN and unmutated
```

## 1. DEFINITION

An INSTRUMENT is a constituted mechanism authorized to establish, constrain,
witness, transmit, or mediate a state transition without thereby inheriting
the SELFhood or authority of the reality upon which it operates.

An instrument is the missing layer between constitution and computation:

```
PHILOSOPHY -> CONSTITUTION -> INSTRUMENT -> PROJECTION -> COMPUTE
```

A mechanism becomes an instrument only by constitution (§4 INV-1). A runtime,
a script, a registry, or a hash utility that merely exists is a mechanism; its
outputs carry record class (§2), never instrument standing.

## 2. NON-COLLAPSE LAWS

```
INSTRUMENT                 != SELF
INSTRUMENT                 != AUTHORITY
INSTRUMENT                 != WITNESS_BY_DEFAULT
INSTRUMENT_OUTPUT          != PROOF_BY_DEFAULT
INSTRUMENT_RECORD          != FACT_ASSERTED
INSTRUMENT_CAPABILITY      != INSTRUMENT_AUTHORITY
FOUNDING_INSTRUMENT        != ORDINARY_INSTRUMENT
TRANSPORT_INSTRUMENT       != RATIFICATION_INSTRUMENT
MODEL_MESSAGE_RECORD       != PROOF_OF_DECLARED_PROPOSITION
AUTHORIZED_RULE            != ACTIVE_RULE
REGISTERED_RULE            != ACTIVE_RULE
ACTIVE_RULE                != UNIVERSALLY_VALID_RULE
RULE_APPLICATION_PASS      != VERIFIED
RULE_AUTHOR                != RULE_ACTIVATOR_BY_DEFAULT
REGISTRY_CUSTODY           != RULE_AUTHORITY
PROOF_RULE                 != PROOF_RESULT
```

Evidence discrimination (per-record law — the rule the round-1 review found
missing at B5/MAT-9):

```
tool invocation record   = evidence that the invocation was recorded
tool result record       = evidence of the returned result
model declaration record = evidence that the model declared the proposition
```

None of the three automatically proves the underlying proposition. A substrate
file may interleave all three classes; class attaches per record, never per
file (a rollout transcript is not "instrument-grade" as a whole — only its
invocation/result records are observation-class; its message records are
declaration-class).

## 3. CONSTITUENTS

Every instrument must declare, in its constituting record:

```
INSTRUMENT
├── identity/type                what it is (class per §6, named, versioned)
├── constituting_grant_ref       the PHILOSELF-002 §3 GRANT (by id) under which
│                                it is constituted — a grant reference, never a
│                                bare party name (round-2 C3/m-3 cure); the
│                                instrument inherits the grant's object_scope,
│                                permitted_transition and forbidden_transition,
│                                and never holds authority itself (M-3)
├── chamber                      where it operates (PHILOSELF-003 dimensions);
│                                the instrument is an OCCUPANT of this chamber
│                                (003 §3 definition)
├── capability                   what it can technically do — the PHILOSELF-002
│                                §6 index (manifestation @ substrate, chamber);
│                                one home for capability estate-wide (M-11)
├── authorized_operation_class   which operations it may lawfully perform,
│                                scoped by the cited grant's object_scope
├── forbidden_operation_class    which operations it may never perform
├── witness_eligibility          which transitions its records may witness
├── proof_eligibility            which claims its records may enter proof
│                                evaluation (§4 INV-8); NONE is the admissible
│                                default and requires no proof contract; a
│                                non-NONE value is checkable only against an
│                                authorized proof rule
├── source_binding_requirements  what it must bind by digest before operating
├── lifecycle                    §6 states, maintained admission-side
├── expiration/supersession      how it lawfully ends or is replaced; REVOKED
│                                propagates from the cited grant (§6)
└── accountability/provenance    who answers for it; what lineage its records carry
```

Capability never grants jurisdiction: the capability field describes; only the
cited grant plus authorized_operation_class license.

## 4. INVARIANTS

1. **Constitution precedes operation.** A mechanism with no constituting
   record (§3 fields, authored by the constituting authority and citing a
   PHILOSELF-002 grant by id) has no instrument standing — fail closed. Its
   outputs carry record class only. A constituting record is NOT itself a
   grant (002 §1); it derives its operating licence entirely from the grant it
   cites.
2. **Eligibility is field-scoped.** Witness eligibility and proof eligibility
   attach per authorized operation class. An output outside eligibility
   carries its record class (invocation / result / declaration) and nothing
   more.
3. **Record-class discrimination.** Every instrument record carries exactly
   one record class, assigned by producer type, never by content. No class
   auto-proves the underlying proposition (§2).
4. **No self-upgrade.** An instrument may not widen its own capability,
   eligibility, operation classes, or lifecycle state. Changes are acts of the
   constituting authority (PHILOSELF-002).
5. **No self-witness of self-change; intent compared to outcome.** An
   operation an instrument performs on its own constitution or records is
   witnessed by a different eligible instrument or by the admission side
   (inherits PHILOSELF-004 §4 INV-3). Every instrument operation compares its
   intended record to its actual record; divergence quarantines the record and
   is surfaced to the admission side — never silently adopted (round-2 M-6
   cure: the analogue of 004 INV-2/INV-4 for instrument operations, which are
   not SELFPUTEs and were previously reached by no invariant set).
6. **Founding singularity.** A FOUNDING_INSTRUMENT is single-use,
   commencement-scoped, FOUNDER_DERIVED, with post-commencement authority
   NONE (PHILOSELF-004 §4 INV-6). A reuse attempt produces an act with no
   standing.
7. **Capability never grants jurisdiction.** Technical capability neither
   creates nor implies an authorized operation class — in either direction:
   capability presence licenses nothing, and capability absence discharges no
   authority obligation (design pressure: round-1 finding A4).
8. **INV-PROOF-EVALUATION-001 (the entrance to Observed — round-2 B-1 cure).**
   Standing is established only by proof evaluation, never by record existence:
   ```
   EvaluateProof(w, c, r, χ)
     w = witness record        (produced by an instrument whose
                                witness_eligibility covers c's transition family)
     c = claim                 (a proposition about a transition or boundary)
     r = authorized proof rule (named, Founder-authorized; no rule -> no
                                evaluation, fail closed)
     χ = governing chamber/context
         ↓
   PASS | FAIL | INDETERMINATE  +  standing_ceiling  +  supported_scope
   ```
   Only PASS raises c to Observed class — at or below the standing_ceiling,
   within the supported_scope, in χ. `Proves(w, c, r, χ)` abbreviates a PASS
   outcome and NEVER denotes generic or universal truth: PASS ≠ VERIFIED, and
   a claim outside the supported_scope gains nothing (example: r =
   direct_remote_byte_observation may establish "the remote surface returned
   these bytes at t" at strong standing, and establishes nothing about "these
   bytes are canonical doctrine" — a different claim under a different rule).
   §7.3's Implementation→run entrance is licensed by THIS invariant and by no
   other route; §2/INV-3 remain true — no record class auto-proves anything;
   evaluation under an authorized rule is what does.
   **Fail-closed conditions (R2 integration):** EvaluateProof(w, c, r, χ)
   REJECTS unless ALL hold: `r.status = ACTIVE`; the rule's
   `activation_grant_ref` covers `ClaimType(c)`; `χ` satisfies
   `r.chamber_requirements`; `w` satisfies `r.admissible_witness_types`; the
   source satisfies `r.admissible_source_types`. Any condition unmet or
   unevaluable → no evaluation occurs (not FAIL — REJECTED_UNEVALUATED).
   Activation confers no ratification authority; application confers no
   standing above `r.standing_ceiling`.
9. **INV-COMPOSITE-NON-MERGER-001.** Eligibility never merges across the
   composed classes of a COMPOSITE instrument: each record carries the class
   and eligibility of exactly one composed function, and a composite's
   transport records never inherit its witness eligibility (nor any other
   cross-class inheritance). (Round-2 M-18: §6's citation "per INV-2/INV-9"
   named this invariant before it existed — an issuer phantom-citation defect,
   conceded; cured by authoring the intended law, with this provenance note.)

## 5. FAILURE MODES

| Failure | Meaning |
|---|---|
| `UNCONSTITUTED_MECHANISM_ELEVATION` | A mere mechanism's output treated as instrument witness or proof. |
| `WITNESS_BY_DEFAULT` | Instrument standing treated as witness eligibility for everything it touches. |
| `PROOF_BY_SERIALIZATION` | A record treated as proof because a substrate serialized it. |
| `RECORD_CLASS_LAUNDERING` | A declaration record cited as if it were an invocation/result record. |
| `INSTRUMENT_SELF_UPGRADE` | Instrument widens its own eligibility, capability, or lifecycle state. |
| `INSTRUMENT_SELF_CAPTURE` | Instrument treated as a SELF, or inheriting the SELFhood/authority of what it operates on. |
| `FOUNDING_REUSE` | The commencement instrument invoked for ordinary operation. |
| `TRANSPORT_RATIFICATION_LEAP` | A transport crossing treated as changing the standing of what it carries. |
| `ELIGIBILITY_INHERITANCE` | A child or composed instrument acquiring eligibility ambiently from its parent. |

## 6. STATE/RELATION MODEL

**Three distinct state models** (round-2 C11 ruling, Founder-locked: the
instrument, its records, and the receiver's disposition are different objects
with different calculi — never one chain):

**Instrument lifecycle** (states maintained by the constituting authority or an
authorized admission instrument, never by the instrument itself):

```
PROPOSED -> CONSTITUTED -> ACTIVE
         -> SUSPENDED -> EXPIRED | REVOKED | SUPERSEDED -> RETIRED
```

`REVOKED` fires automatically when the cited constituting grant is revoked —
revocation propagates from grant to instrument with no gap (cures
REVOCATION_LAG at the instrument layer; round-2 C3 second defect).

**Record custody lifecycle** (the instrument's OUTPUT — the object round-2
C11 D8 found unowned):

```
EMITTED -> PERSISTED -> TRANSPORTED -> RECEIVED
```

`EMITTED`, `TRANSPORTED`, `RECEIVED` are monotone event-markers; `PERSISTED`
is a non-monotone state (deletion and rotation reverse it). Resolvability is
NOT a lifecycle state at all but a four-place predicate —
`Resolvable(record, receiver, surface, t)` — indexed by receiver, surface, and
time (live specimens: the same corpus simultaneously resolvable for the
round-2 reviewer and unresolvable for CHATGPTSELF; the same channel commit
simultaneously served and not served by two GitHub API surfaces).

**Receiver disposition** (acts of the receiver's authority in the receiver's
chamber — PHILOSELF-002 grants, PHILOSELF-004 SELFPUTEs; NEVER transport
stages, or completing transport would complete acceptance, the exact
TRANSPORT_RATIFICATION_LEAP §5 prohibits):

```
RECEIVED -> { ACCEPTED | REJECTED | DEFERRED | QUARANTINED | SUPERSEDED | ADOPTED }
```

No mandatory sequence holds among these; in particular ACCEPTED does not
entail ADOPTED and neither is reachable by any act of the sender.

**Projection lifecycle** (AgentProjection records — admission-side maintained;
provisional vocabulary, round-2 C10 #9 content):

```
DRAFT -> CONSTITUTED -> ADMITTED -> INSTANTIATED -> ACTIVE
      -> COMPLETED | FAILED | REVOKED -> CLOSED
```

Every child context is classified (INTENDED / ACCIDENTAL_DUPLICATE /
SUPERSEDED / QUARANTINED / NO_OP / UNKNOWN) and every duplicate receives a
disposition (NO_OP_CLOSED / QUARANTINED / SUPERSEDED / INVALIDATED) — the
duplicate-projection law, now content-parented (specimen:
DUPLICATE_PROJECTION_UNBOUND, PHILOSELF-003 §8 S-3).

Instrument classes: ADMISSION, WITNESS, PROOF, FOUNDING, TRANSPORT, REGISTRY —
and COMPOSITE (a constituted composition; eligibility never merges across the
composed classes, per INV-2/INV-9 of §4). A REGISTRY instrument persists
constituted records; its custody of a record confers NO authority over the
record (`REGISTRY_CUSTODY != RULE_AUTHORITY`, §2).

**PROOF RULE REGISTRY (R2 constitutionalization).** The ProofRuleRegistry is
an INSTRUMENT of class REGISTRY, constituted like any other (§3, §4 INV-1) —
never an authority. The five-way separation governs the whole mechanism:

```
RULE_AUTHORSHIP != RULE_REGISTRATION != RULE_ACTIVATION
                != RULE_APPLICATION != STANDING_ADJUDICATION
```

A reviewer may propose a rule; an engineer may encode it; the registry
persists it; NONE of those acts authorize the rule to elevate standing —
activation is a domain-scoped ADJUDICATION_AUTHORITY act (PHILOSELF-002 §6),
and application is a SELFPUTE (PHILOSELF-004 §6).

**ProofRule** (governed record type, persisted by the registry):

```
ProofRule
├── rule_id
├── claim_type
├── admissible_witness_types
├── admissible_source_types
├── chamber_requirements
├── supported_scope
├── standing_ceiling
├── failure_conditions
├── author
├── registration_record
├── activation_authority
├── activation_grant_ref
├── status
├── activated_at
├── expires_at
├── supersedes
└── provenance
```

Status discipline (candidate vocabulary — NOT asserted as a total lifecycle;
evidence may show non-sequential paths, e.g. REGISTERED -> SUPERSEDED without
activation):

```
DRAFT -> REGISTERED -> ACTIVE -> SUSPENDED | SUPERSEDED | RETIRED
```

**Parentage table** — the constitutional ancestry the round-1 A10 audit found
missing. Standing note: this table parents the *classes*; it ratifies,
implements, and un-freezes nothing:

| Entity (X1 / estate) | Constitutional class under 005 |
|---|---|
| ALCHEMISELF | ADMISSION INSTRUMENT — classifies symbol/type/identity/provenance/standing/authority; authorizes or blocks projection formation, under a 002 grant it can never widen. Standing honesty (round-2 M-21): its live behavioral discipline in the SELF-COMMUNICATION channel is presently an UNCONSTITUTED MECHANISM under INV-1 (model-backed, OQ-2); this row is prospective parentage, not standing |
| AgentProjection | ADMISSION RECORD — the output object class of an admission instrument; a record, not an instrument and not a SELF |
| SELFAgentBridge | COMPOSITE INSTRUMENT (admission + witness + transport); holds no SELFhood; computes nothing it mediates |
| INSELFACTION | TRANSPORT INSTRUMENT output class — a witnessed chamber-crossing record (PHILOSELF-003 §4 INV-2); transport never ratifies |
| Projection lifecycle | ADMISSION INSTRUMENT obligation — lifecycle states are admission-side records |
| Duplicate-projection handling | ADMISSION INSTRUMENT obligation — every child context classified and dispositioned (specimen: DUPLICATE_PROJECTION_UNBOUND, PHILOSELF-003 §8 S-3) |
| Admission instruments | class defined here |
| Witness instruments | class defined here — eligibility per §4 INV-2 |
| Proof instruments | class defined here — eligibility only; the proof relation itself remains open (§10 OQ-4) |
| Founding instruments | class defined here — §4 INV-6; sole lawful commencement mechanism |
| Transport instruments | class defined here — crossings, custody, never standing mutation |

## 7. WITNESS CONDITIONS

1. An instrument's constitution is witnessed by its constituting record,
   authored by the constituting authority (admission side) — never by the
   mechanism being constituted.
2. An instrument's operations are witnessed within its eligibility only;
   records outside eligibility carry record class alone.
3. **The lawful road into Observed — licensed by §4 INV-8.** Under
   `doctrine/specs/SELF-KERNEL-SPEC-V0.md`, the only entrance to the Observed
   class is `Implementation → run`. An eligible instrument RUNS and records;
   the record then enters `EvaluateProof(w, c, r, χ)` under an authorized
   rule, and only a PASS raises the claim to Observed at its standing_ceiling
   within its supported_scope. Authority constitutes the instrument (Authority
   axis); the run produces the record (Implementation axis); the evaluation —
   not the record's existence — establishes the fact. This closes the round-2
   B-1 gap: §2/INV-3's "no class auto-proves" and this entrance are now
   consistent, with INV-8 as the sole bridge. (PHILOSELF-001's own MAT-18
   wording conflict remains unrepaired — outside this revision's surfaces;
   this section supplies the vehicle for that future repair.)
4. Non-operation is witnessable per PHILOSELF-002 §7.3 as repaired: digest
   pairs over the full declared write-set, inside the cited record or a
   separately bound witness.

## 8. ADVERSARIAL SPECIMENS

- **S-1 — One file, three record classes.**
  `~/.codex/sessions/2026/08/15/rollout-2026-08-15T09-41-06-01a005a7-a0eb-7991-a959-c488b16c2d1e.jsonl`:
  line 24 holds a `unified_exec` shasum invocation+result (observation-class
  records); lines 148/149/151 hold "reviewer identity: HBCSELF" and "session
  independence: ESTABLISHED" (declaration-class records). Under §2 the same
  file proves the child DECLARED the identity and never proves the identity —
  the discrimination the round-1 review found missing (B5/MAT-9).
- **S-2 — `router/sia-registry.js`** (control-plane repo): deep-frozen,
  deterministic, fail-closed role/route mechanism — the estate's closest
  existing approximation of a CONSTITUTED instrument, yet it lacks a
  constituting record naming authority, eligibility, and lifecycle: under §4
  INV-1 it stands at PROPOSED grade. Positive design precedent, negative
  standing specimen.
- **S-3 — SUPERSEDED_FALSE_SPECIMEN — the round-1 bracket-hash procedure.**
  Original wording, preserved as authored (FALSE): "(`governance/
  PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md`, issuer receipt): shasum
  invocation/result records established subject stability across the review
  window — observation-class, sound." Falsifying evidence (round-2 SPEC2-F1):
  the R1 issuer receipt contains PROSE ONLY — bracket declarations with no
  shasum invocation record, no result record, and no digest values; its
  pointer to "annex §1" resolves to a projection block holding zero subject
  digests. Why false: under this candidate's own §2, issuer-receipt prose and
  packet digest lists are declaration-class records; the specimen offered as
  the positive exemplar of observation-class evidence cited nothing
  observation-class — RECORD_CLASS_LAUNDERING committed inside the candidate
  that legislates the discrimination (issuer defect, conceded). Corrected
  proposition: the observation-class records of those hash runs exist only in
  the issuer session's tool-invocation stream, which no reviewer read; the R1
  receipt is a declaration-class account of them. What the specimen actually
  evidences: the same session was elsewhere the transforming runtime of the
  subjects — field-scoped eligibility (§4 INV-2) plus the instrument/subject
  separation now enforced by 003 §4 INV-7 are both required, and a
  declaration-class receipt satisfies neither.
- **S-4 — FOUNDING_WITNESS** (PHILOSELF-004 §7): the only Founder-derived
  instrument class; single-use, commencement-scoped; the specimen of §4 INV-6
  and the boundary FOUNDING ↔ ORDINARY (packet-002 cross 5).

## 9. DEPENDENCIES

- PHILOSELF-001..004, post-repair digests as in header CAUSAL_PARENT — this
  candidate is derived from them and has no standing without them.
- PHILOSELF-004 §4 INV-6 (commencement article) — founding instruments.
- PHILOSELF-003 §4 INV-RC-ADMISSION-001 — admission instruments are the
  "authorized instrument" that invariant names.
- SELF-KERNEL-SPEC-V0 — Implementation→run entrance (§7.3). Binding (M-20):
  repository RUORA, path
  `systems/ourself-agent-bridge/doctrine/specs/SELF-KERNEL-SPEC-V0.md`, sha256
  c74228e41e2720bd2a10be4a7ce69c053d55ff832b07e491ab23255f1bd0e86b.
- sia-registry — fail-closed precedent (specimen S-2). Binding (M-20):
  repository RUORA, path
  `systems/ourself-agent-bridge/router/sia-registry.js`, sha256
  1e4cd1bcf9a8f2c60d87bc0e07f74eb1ed86dbbd20cadd7291e1fd979b224752 (five
  `-pass-21aN` siblings disclosed; this binding names the original only).
- PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md — design pressure (B4, B5, MAT-9,
  MAT-18, A4, A10; source evidence, undispositioned).

## 10. OPEN QUESTIONS

1. **Bootstrap order.** The first ordinary admission instrument must be
   constituted before ordinary SELFPUTE begins. Is it constituted directly by
   the Founder, or through the FOUNDING_INSTRUMENT during commencement? A
   sovereign sequencing choice; both are lawful under §4 INV-6.
2. **Model-backed instruments.** May an instrument embed a model component,
   and if so do that component's outputs always carry declaration class while
   only the surrounding deterministic shell may produce observation-class
   records? (Design question with large consequences for AgentBridge.)
3. **Instrument integrity.** What witnesses tampering with an instrument or
   its constituting record — a second-order witness instrument, or
   admission-side re-verification by digest? (Future class; nothing herein
   depends on the answer.)
4. **The proof-rule registry.** The proof EVALUATION contract now exists (§4
   INV-8: EvaluateProof(w, c, r, χ) with standing_ceiling and supported_scope).
   What remains open is the REGISTRY of authorized proof rules: which rules r
   exist, who authorizes them (a Founder RATIFICATION-class act, or a
   delegated authority?), how a rule's standing_ceiling is fixed, and where
   the registry lives so that "authorized proof rule" never becomes the next
   magic phrase through which standing is laundered. Until the registry
   exists, the only lawful evaluations are those whose rule is named and
   authorized in the evaluating act itself.
