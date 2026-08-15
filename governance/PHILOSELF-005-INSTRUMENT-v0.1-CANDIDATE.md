# PHILOSELF-005 — INSTRUMENT

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
CLASS:               philoSELF foundation (5 — instrument layer)
AUTHORED:            2026-08-15
AUTHOR_SELF:         Claude Code session 74633bfb-04bf-48c4-99aa-29d87a2eabb4
AUTHORED_UNDER:      FOUNDER_CONTINUE_PHILOSELF_MANIFESTATION_001_HARDENED,
                     Phase B (CITRINITAS) — new candidate, NOT canon
CAUSAL_PARENT:
  PHILOSELF-001 (post-repair) sha256 6ff37cdb0d2928ac2cb8c63a3799dbf3b435878a0f59a00fca03519ea53bde5d, 193 ln
  PHILOSELF-002 (post-repair) sha256 f70945fbf6d350e596b2dd8038784e530dc7ae02cbfe5c2e760e080420c3411d, 216 ln
  PHILOSELF-003 (post-repair) sha256 894c9d9c5322bcee8f400f87975e1fc7869cfec1c886d71864d1e2a6f21d3809, 256 ln
  PHILOSELF-004 (post-repair) sha256 60a2f3a9c675f1501c71b1d986939aab67ac56045964cc35b8f7c29aacc3ee73, 231 ln
DESIGN_PRESSURE:     PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md (sha 03f49df9…,
                     BLOCKED verdict — chiefly its instrument-theory gap:
                     "A foundation from which SELFAgentBridge could be derived
                     would contain a theory of instruments")
COMMENCEMENT:        PRE_CONSTITUTIONAL_STATE — nothing herein is in force;
                     see PHILOSELF-004 §4 INV-6
HOSTILE_REVIEW:      NOT_PERFORMED — see PHILOSELF-BOUNDARY-REVIEW-PACKET-002
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
├── constituting_authority       which sovereign or delegated grant constitutes it
├── chamber                      where it operates (PHILOSELF-003 dimensions)
├── capability                   what it can technically do (substrate-indexed)
├── authorized_operation_class   which operations it may lawfully perform
├── forbidden_operation_class    which operations it may never perform
├── witness_eligibility          which transitions its records may witness
├── proof_eligibility            which claims its records may enter into a proof
│                                relation (see §10 OQ-4 — relation undefined
│                                estate-wide; eligibility only is bound here)
├── source_binding_requirements  what it must bind by digest before operating
├── lifecycle                    §6 states, maintained admission-side
├── expiration/supersession      how it lawfully ends or is replaced
└── accountability/provenance    who answers for it; what lineage its records carry
```

Capability never grants jurisdiction: the capability field describes; only
constituting_authority plus authorized_operation_class license.

## 4. INVARIANTS

1. **Constitution precedes operation.** A mechanism with no constituting
   record (§3 fields, authored by the constituting authority) has no
   instrument standing — fail closed. Its outputs carry record class only.
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
5. **No self-witness of self-change.** An operation an instrument performs on
   its own constitution or records is witnessed by a different eligible
   instrument or by the admission side (inherits PHILOSELF-004 §4 INV-3).
6. **Founding singularity.** A FOUNDING_INSTRUMENT is single-use,
   commencement-scoped, FOUNDER_DERIVED, with post-commencement authority
   NONE (PHILOSELF-004 §4 INV-6). A reuse attempt produces an act with no
   standing.
7. **Capability never grants jurisdiction.** Technical capability neither
   creates nor implies an authorized operation class — in either direction:
   capability presence licenses nothing, and capability absence discharges no
   authority obligation (design pressure: round-1 finding A4).

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

Instrument lifecycle (states maintained by the constituting authority or an
authorized admission instrument, never by the instrument itself):

```
PROPOSED -> CONSTITUTED -> COMMISSIONED -> OPERATING
         -> SUSPENDED | SUPERSEDED | DECOMMISSIONED
```

Instrument classes: ADMISSION, WITNESS, PROOF, FOUNDING, TRANSPORT — and
COMPOSITE (a constituted composition; eligibility never merges across the
composed classes, per INV-2/INV-9 of §4).

**Parentage table** — the constitutional ancestry the round-1 A10 audit found
missing. Standing note: this table parents the *classes*; it ratifies,
implements, and un-freezes nothing:

| Entity (X1 / estate) | Constitutional class under 005 |
|---|---|
| ALCHEMISELF | ADMISSION INSTRUMENT — classifies symbol/type/identity/provenance/standing/authority; authorizes or blocks projection formation, under a 002 grant it can never widen |
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
3. **The lawful road into Observed.** Under
   `doctrine/specs/SELF-KERNEL-SPEC-V0.md`, the only entrance to the Observed
   class is `Implementation → run`. Instrument records enter Observed exactly
   this way: an eligible instrument RUNS and records. Authority constitutes
   the instrument (Authority axis); the instrument's run produces the
   observation (Implementation axis). This is the entrance the round-1 review
   found missing at MAT-18 — identity and chamber facts become Observed-class
   through an instrument's run, never through an authority's assertion.
   (PHILOSELF-001's own MAT-18 wording conflict remains unrepaired — its
   amendment was not authorized in Phase A; this section supplies the vehicle
   for that future repair, not the repair itself.)
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
- **S-3 — The round-1 bracket-hash procedure**
  (`governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md`, issuer receipt):
  shasum invocation/result records established subject stability across the
  review window — observation-class, sound. The same session was elsewhere the
  transforming runtime of the subjects — demonstrating why eligibility must be
  field-scoped (§4 INV-2) rather than session-global.
- **S-4 — FOUNDING_WITNESS** (PHILOSELF-004 §7): the only Founder-derived
  instrument class; single-use, commencement-scoped; the specimen of §4 INV-6
  and the boundary FOUNDING ↔ ORDINARY (packet-002 cross 5).

## 9. DEPENDENCIES

- PHILOSELF-001..004, post-repair digests as in header CAUSAL_PARENT — this
  candidate is derived from them and has no standing without them.
- PHILOSELF-004 §4 INV-6 (commencement article) — founding instruments.
- PHILOSELF-003 §4 INV-RC-ADMISSION-001 — admission instruments are the
  "authorized instrument" that invariant names.
- `doctrine/specs/SELF-KERNEL-SPEC-V0.md` — Implementation→run entrance (§7.3).
- `router/sia-registry.js` — fail-closed precedent (specimen S-2).
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
4. **The proof relation.** PROOF remains undefined estate-wide (round-1 B6 /
   MAT-2, unrepaired by authority limit). This candidate binds proof
   *eligibility* and record discrimination only. Defining `Proves(w, c)` is a
   joint future repair of PHILOSELF-004 §3/§6 and a proof-instrument
   specification, under separate authorization.
