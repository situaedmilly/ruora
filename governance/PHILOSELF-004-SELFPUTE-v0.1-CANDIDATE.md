# PHILOSELF-004 — SELFPUTE

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
REVISION:            v0.2-boundary-repair-001 (2026-08-15; filename retains the
                     v0.1 candidate slot; Phase A authorized surfaces only)
CLASS:               philoSELF foundation (4 of 4)
AUTHORED:            2026-08-15
AUTHOR_SELF:         Claude Code session 74633bfb-04bf-48c4-99aa-29d87a2eabb4
AUTHORED_UNDER:      Founder relay 2026-08-15 ("LETSBALL")
REPAIRED_UNDER:      FOUNDER_CONTINUE_PHILOSELF_MANIFESTATION_001_HARDENED
                     (bounded mutation authority — NOT ratification, NOT review closure)
CAUSAL_PARENT:
  artifact_type:     FOUNDATION_RETURN_RECORD
  path:              governance/OSAB-SELFQUEUE-FOUNDATION-001-RETURN-RECORD.html
  sha256:            f778298075363b896019ee6b06ee792c943d8e79786b6e51ed8bfadebf5f2ebb
  line_count:        327
  lineage_role:      CAUSAL_PARENT
  standing:          SOURCE_RECORD (materialized to disk 2026-08-15 AFTER original
                     authoring — repair evidence, not retroactive original custody)
CO_PARENT:           SELFSYSTEM_AGENT_PROJECTION_001 (X1),
                     governance/SELFSYSTEM_AGENT_PROJECTION_001.md, sha256
                     25896d048a4a39ee9b6661fad9e876caf40361cd4bd400f723fa7fd16272c855,
                     404 lines — FROZEN, unmutated
ORIGINAL_ANCESTRY:   "OSAB SELFQUEUE FOUNDATION_001 return (artifact ee991b56)" —
                     preserved verbatim. ORIGINAL_ANCESTRY_DEFECT: TRUE — at original
                     authoring time this referent was NOT filesystem-resolvable
                     (web-artifact, conversation, and memory scope only). No
                     history rewrite is performed or implied.
SOURCE_EVIDENCE_STANDING:
                     FOUNDATION_001 findings cited in this candidate carry standing
                     source_evidence / historical_finding / design_input /
                     repair_pressure ONLY — undispositioned; NOT law, NOT binding
                     authority, NOT invariant ground, NOT ratified adjudication.
COMMENCEMENT:        PRE_CONSTITUTIONAL_STATE — nothing herein is in force; the
                     commencement article is §4 INV-6 of this candidate
HOSTILE_REVIEW:      ROUND 1 RETURNED BLOCKED —
                     governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md (sha256
                     03f49df94d11c347fe364cc3f0251f6affbc651e6273e5d6791b40e1d3bff6bb,
                     541 lines); round 2 pending per PHILOSELF-BOUNDARY-REVIEW-PACKET-002
RATIFICATION:        NOT_GRANTED
IMPLEMENTATION:      NOT_AUTHORIZED
SUPERSEDES:          NOTHING
```

## 1. DEFINITION

SELFPUTE is an authorized transformation of a bounded reality from one
admissible state into another, performed under a SELF's identity, inside a
reality chamber, within granted authority, preserving required SELFhood
invariants, and producing witnessable evidence of the transformation.

Ordinary compute is `input -> processing -> output`. SELFPUTE carries five
obligations ordinary compute does not: identity, chamber, authority, witness,
memory. Compute that discharges none of them may still be useful; it is not an
act of a SELF.

## 2. NON-COLLAPSE LAWS

```
COMPUTE       != SELFPUTE
OUTPUT        != STATE_CHANGE
DECLARATION   != EXECUTION
EXECUTION     != EVIDENCE
EVIDENCE      != MEMORY
INTENDED      != ACTUAL            (transition)
NARRATION     != WITNESS
PASS          != the adjudication battery answered one by one
```

The DECLARATION/EXECUTION/EVIDENCE/MEMORY chain is the ancestral core law of
this estate — `doctrine/self_axiom.md`: "No declaration without execution. No
execution without evidence. No evidence without memory." SELFPUTE is that law
generalized from commands to all acts of a SELF.

## 3. CONSTITUENTS

```
SELFPUTE
├── selfhood              which SELF acts (PHILOSELF-001)
├── chamber               where it acts (PHILOSELF-003)
├── authority             under which grant (PHILOSELF-002)
├── input_state           bound pre-state (digests where applicable)
├── possibility_space     the admissible transformations considered
├── constraints           what bounds the operation
├── operation             the transformation performed
├── intended_transition   X -> Y as authorized
├── actual_transition     X -> Y' as observed
├── invariant_checks      SELFhood invariants verified across the transition
├── emitted_events        declarations that the transformation occurred
├── witness               instrument-recorded observation of actual_transition
├── proof                 established relation between declaration and occurrence
└── resulting_memory      appended lineage available to future SELFPUTE
```

## 4. INVARIANTS

1. **Admissibility precedes operation.**
   `T ∈ Capability ∧ T ∈ Authority ∧ Preconditions(Chamber) = SATISFIED`
   (PHILOSELF-002 §6) — checked before, not narrated after.
2. **Actual is compared to intended.** Divergence between intended and actual
   transition is recorded as divergence; it is never silently adopted as the
   new intent.
3. **Witness is written by instrument.** The transforming runtime's narration
   is an emitted event, never the witness of its own transformation.
4. **Failed invariant checks quarantine.** A transformation that breaks a
   SELFhood invariant is quarantined and surfaced, not repaired in place.
5. **Memory is appended.** Resulting memory extends lineage; it never edits it
   (ratification-binds-evidence-state law).
6. **Commencement article (entry into force).** `FOUNDING !=
   ORDINARY_OPERATION`. These foundations bind prospectively only:
   ```
   PRE_CONSTITUTIONAL_STATE
     -> FOUNDING_INSTRUMENT
     -> FOUNDING_WITNESS
     -> CONSTITUTION_ENTERED_INTO_FORCE
     -> ORDINARY_PHILOSELF_OPERATION
   ```
   Invariants 1–5 govern ORDINARY_PHILOSELF_OPERATION. They do not
   retroactively render acts of the PRE_CONSTITUTIONAL_STATE unlawful, and the
   commencement act itself is witnessed by the FOUNDING_WITNESS (§7) — never
   by the invariants it brings into force. Current state:
   PRE_CONSTITUTIONAL_STATE. Nothing in this article weakens the ordinary
   rule: the transforming runtime is never the witness of its own
   transformation.

## 5. FAILURE MODES

| Failure | Meaning |
|---|---|
| `UNWITNESSED_TRANSFORMATION` | State changed; no instrument record exists. |
| `DIVERGENCE_UNRECORDED` | Actual ≠ intended and the record shows only intended. |
| `OUT_OF_CHAMBER_WRITE` | Transformation touched state outside the chamber's declared boundary. |
| `PROOF_BY_NARRATION` | The runtime's account of its act accepted as proof of the act. |
| `VERDICT_COLLAPSE` | A single PASS token standing in for the whole adjudication battery. |
| `WITNESS_BY_SUBJECT` | The transformed party or transforming runtime writes the witness. |
| `MEMORY_SKIPPED` | Evidence produced but never appended to lineage; the act becomes unrecallable. |

## 6. STATE/RELATION MODEL

The SELFPUTE pipeline:

```
POSSIBILITY SPACE -> REALITY CHAMBER -> SELFHOOD -> AUTHORITY -> CONSTRAINT
  -> TRANSFORMATION -> NEW STATE -> WITNESS -> PROOF -> MEMORY -> next SELFPUTE
```

Adjudication battery — answered one by one, never collapsed:

```
1. Did compute occur?
2. Was it inside the correct chamber?
3. Was the SELF projection valid?
4. Was authority sufficient?
5. Was the transition admissible?
6. Were invariants preserved?
7. Was the result witnessed?
8. Was the claim proven?
```

(Disclosure: the source relay enumerated these eight questions while naming
"seven"; this candidate normalizes to the enumerated eight. The boundary
review should confirm or correct this normalization.)

## 7. WITNESS CONDITIONS

- The witness is an instrument-recorded observation of the actual transition:
  filesystem delta, pre/post digest pair, substrate session record, test
  battery output. Per the Realm Mutation ladder's sealed law: **Git cannot
  adjudicate mutation — filesystem delta can.**
- Non-mutation is witnessable the same way: pre-state digest = post-state
  digest under a mutation-forbidding grant.
- Substrate-written execution records (e.g., Codex rollout `.jsonl` files) are
  candidate instrument witnesses: written by the runtime substrate, not by the
  model's narration. Their admissibility class is Open Question 3.
- This document's own creation is a SELFPUTE specimen: pre-state
  (path nonexistent, verified), operation (file write), post-state (sha256
  recorded in the boundary packet), witness (governance repo status delta),
  memory (session memory + MEMORY.md index).
- **FOUNDING_WITNESS** (commencement instrument class — §4 INV-6):
  ```
  standing:                     TRANSITIONAL
  source:                       FOUNDER_DERIVED
  scope:                        COMMENCEMENT_ONLY
  reusable:                     false
  post_commencement_authority:  NONE
  ```
  The FOUNDING_WITNESS may establish exactly one fact — that commencement
  occurred. It may never satisfy any ordinary post-commencement SELFPUTE
  witness requirement, and it may never be reused.

## 8. ADVERSARIAL SPECIMENS

- **S-1 — The child review as SELFPUTE candidate.** Present: in-chamber source
  digest verification, subject non-mutation witnessed (`07d77b70…` unchanged),
  substrate-written session record. Absent: projection record (identity),
  instrument-issued authority grant, occupant-independent chamber witness.
  Partial SELFPUTE — the gaps are exactly PHILOSELF-001/002/003 obligations.
- **S-2 — Conversational transformation.** A chat turn that changes a
  doctrine's standing ("this is ratified") with no file delta: what witness
  exists? Under this candidate: none — standing unchanged until recorded.
- **S-3 — ESM C0 realization defect.** Declared measurement without realized
  instrument — a declaration whose execution never occurred; the modern seal
  is lawfully blocked on it.
- **S-4 — UREEL Gate 0007 (positive control).** 8/8 proof battery:
  declaration, execution, evidence, memory all present — the complete chain
  this candidate generalizes.

## 9. DEPENDENCIES

- `doctrine/self_axiom.md` — ancestral law; this candidate must remain
  derivable from it, not rival to it.
- Realm Mutation ladder (R0–R2 sealed) — mutation adjudication by filesystem
  delta; Gate D content-witness hole is inherited here, not solved here.
- Epistemic Systems Metrology — realization law; the C0 defect as specimen.
- `doctrine/specs/SELF-KERNEL-SPEC-V0.md` — legal bridges between declared,
  observed, and proven truth classes.
- PHILOSELF-001, -002, -003 — SELFPUTE is the point where the other three
  foundations become operative; it has no independent standing without them.

## 10. OPEN QUESTIONS

1. What is the minimal admissible witness for a conversational SELFPUTE, or is
   the class lawfully empty (no record → no act)?
2. Where does proof custody live before the deferred memory-organ doctrine is
   adopted — governance/evidence JSONL chambers, or per-repo?
3. Are substrate-written session records (provider-formatted rollout files)
   admissible instrument witnesses, and at what class — they are instrument-
   written but not instrument-designed?
4. Does a quarantined transformation (failed invariant check) still append to
   memory as a failure record, and who may later release it?
