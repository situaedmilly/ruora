# PHILOSELF-003 — REALITY CHAMBER

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
REVISION:            v0.3-state-establishment-repair-001 + residual-ledger-001
                     (2026-08-15; same authorization wave; residual surface:
                     M-22 promotion INV-8)
CLASS:               philoSELF foundation (3 of 4)
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
  lineage_role:      MATERIALIZED_CAUSAL_SOURCE_RECORD (renamed per Founder M-2
                     ruling 2026-08-15: ee991b56 identity NOT ESTABLISHED as
                     original filesystem artifact; this record is a post-hoc
                     materialization of the foundation return)
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
COMMENCEMENT:        PRE_CONSTITUTIONAL_STATE — nothing herein is in force; see
                     PHILOSELF-004 §4 INV-6 (commencement article)
HOSTILE_REVIEW:      ROUND 1 RETURNED BLOCKED —
                     governance/PHILOSELF-BOUNDARY-REVIEW-RETURN-001.md (sha256
                     03f49df94d11c347fe364cc3f0251f6affbc651e6273e5d6791b40e1d3bff6bb,
                     541 lines); round 2 pending per PHILOSELF-BOUNDARY-REVIEW-PACKET-002
RATIFICATION:        NOT_GRANTED
IMPLEMENTATION:      NOT_AUTHORIZED
SUPERSEDES:          NOTHING
```

## 1. DEFINITION

A REALITY CHAMBER is the bounded semantic, evidentiary, authority, memory,
state, and execution domain within which observations acquire meaning.

"Context" names something passive that a runtime happens to carry. A chamber is
sovereign: the same artifact read inside two different chambers is two
different observations. The epistemic value of the HBCSELF child review came
not from fewer tokens but from a different chamber — same artifact, same
doctrine, no authoring history, review-only authority, independent
interpretation.

## 2. NON-COLLAPSE LAWS

```
SHARED MODEL                 != SHARED SELF
SHARED FILESYSTEM            != SHARED AUTHORITY
SHARED EVENT LANGUAGE        != SHARED MEANING
SHARED MEMORY INFRASTRUCTURE != SHARED MEMORY
SHARED ORCHESTRATOR          != SHARED REALITY CHAMBER
CONTEXT                      != CHAMBER
SESSION_SEPARATION           != MODEL_INDEPENDENCE
MODEL_INDEPENDENCE           != ABSENCE_OF_CONTAMINATION
EXECUTION                    != SESSION
MODEL                        != COMPUTE
COMPUTE                      != EXECUTION
OCCUPANT_DISCLOSURE          != CHAMBER_STANDING
```

## 3. CONSTITUENTS

Ten boundary dimensions; a chamber is defined by the explicit setting of all
ten, never by default:

```
REALITY CHAMBER
├── IDENTITY BOUNDARY     which inhabitants exist inside — SELF projections AND
│                         constituted instruments (round-2 orphan N-1: an
│                         instrument is an inhabitant, and an occupant)
├── SEMANTIC BOUNDARY     which vocabulary and doctrine govern meaning
├── MEMORY BOUNDARY       which memory is readable / writable inside
├── AUTHORITY BOUNDARY    which grants are exercisable inside
├── STATE BOUNDARY        which mutable state is visible / bindable
├── EVIDENCE BOUNDARY     which evidence scopes are admissible
├── EXECUTION BOUNDARY    which execution locus (process, subagent, runtime
│                         invocation) hosts the chamber
├── SESSION BOUNDARY      which session custody tree the execution and its
│                         records belong to — a child execution nested inside
│                         another session's custody is session-non-isolated
│                         even when execution-distinct
├── MODEL BOUNDARY        which model/substrate identity backs the execution —
│                         a capability property of the manifestation
└── PROVENANCE BOUNDARY   what lineage the chamber's outputs carry
```

`MODEL != COMPUTE`. MODEL names substrate/model identity or capability
property. COMPUTE names a realized transformation — SELFPUTE territory
(PHILOSELF-004) — and is therefore not a chamber dimension at all. The former
single COMPUTE dimension of revision v0.1 conflated EXECUTION and MODEL and
gave SESSION no home (boundary review finding A8/MAT-8, design input); it is
superseded by the EXECUTION, SESSION, and MODEL dimensions above.

**OCCUPANT (definition — governs the relation, not today's actor names):** an
OCCUPANT of chamber C with respect to boundary B is any SELF, projection,
instrument, process, or execution whose epistemic inputs or operational
behavior are subject to B. Formally: `AffectedByBoundary(x, B)`. The
enumeration is illustrative; the relation is the law — it reaches reviewers,
issuing parents, admission instruments running inside the chamber,
subprocesses, inherited-memory evaluators, and agent types not yet named.

## 4. INVARIANTS

1. **Explicit inheritance only.** A child chamber inherits nothing ambiently.
   The instantiating record declares, per dimension, `inherit:` or `isolate:`
   (e.g., inherit doctrine and source bindings; isolate working memory,
   mutation authority, interpretation history). An undeclared dimension is
   `UNRESOLVED`, not inherited. The instantiating record is authored by the
   admission side or an authorized instrument — never by the occupant (INV-6).
2. **Crossings are events.** Anything that moves across a chamber boundary —
   evidence in, disposition out — is a witnessed crossing, not osmosis.
3. **Closure claims are classed.** A claim that a chamber is closed on some
   dimension is classed observable / attestable / unobservable — by the
   admission side or an authorized instrument, never by the occupant — and
   fails closed. This invariant stands on this candidate's own force; its
   historical design input is FOUNDATION_001 finding F-03 (undispositioned
   source evidence, not authority).
4. **Nesting narrows.** In the chamber stack, a child chamber's boundary set
   is a subset of what its parent may lawfully grant.
5. **Source bytes over summaries.** Where a task depends on artifacts, the
   chamber binds the artifacts by digest; a parent summary substituted for
   source is a boundary breach, not a convenience.
6. **INV-RC-ADMISSION-001 (admission-side invariant).** No chamber occupant may
   establish, certify, or upgrade the standing of its own isolation,
   independence, memory boundary, authority boundary, model boundary, session
   boundary, execution boundary, semantic boundary, evidence boundary,
   provenance boundary, or source-binding boundary.
   `OCCUPANT_DISCLOSURE != CHAMBER_STANDING`: occupants may disclose
   observations; a disclosure is evidence of the disclosure event, never proof
   of the disclosed boundary fact. Boundary standing may be established only
   by: the admission side; an authorized instrument (PHILOSELF-005); or an
   explicitly scoped Founder-derived commencement mechanism
   (PHILOSELF-004 §4 INV-6, FOUNDING_WITNESS — commencement scope only).
   OCCUPANT takes its §3 definition: `AffectedByBoundary(x, B)` — so an
   instrument operating inside the chamber IS an occupant for the boundaries
   it is subject to (round-2 C2 cure).
7. **INV-ADMISSION-SEPARATION-001 (admission separation of duty).**
   `AffectedByBoundary(x, B) ⇒ x` may not be the sole adjudicator of
   `Standing(B)`, unless an explicit constitutional exception governs the case
   (the sole current exception: the Founder-derived commencement mechanism,
   PHILOSELF-004 §4 INV-6). This reaches the issuing parent as well as the
   occupant — round 2's live failure was the issuer constructing the chamber
   AND establishing its properties. Two corollaries: (a) **breach disclosure
   forces re-adjudication**: an occupant's `BOUNDARY_BREACH_DISCLOSURE` never
   establishes the boundary fact, but it obligates the admission side to
   re-adjudicate `Standing(B)` — a false admission-side certification is no
   longer unfalsifiable from inside (round-2 M-8 cure); (b) **authority
   inheritance is class-indexed**: a declaration `inherit: authority` without
   per-class, per-grant enumeration is void — EXECUTION-class grants can never
   enter a REVIEW_ONLY chamber through a blanket boundary declaration
   (round-2 M-10 cure).
8. **Independence computation and cap are law (M-22 promotion).** Independence
   between two chambers is COMPUTED as the set of dimensions on which their
   declared boundaries provably do not intersect (§6) — never established by
   conversational impression; and any required predicate in the unobservable
   class CAPS the verdict at INDEPENDENCE_PARTIAL (§7), never defaulting true.
   Detailed prose remains in §6/§7; this invariant is their force.

## 5. FAILURE MODES

| Failure | Meaning |
|---|---|
| `CONTEXT_BLEED` | Interpretation formed in one chamber silently governs another. |
| `AUTHOR_RESIDUE` | Reviewer chamber contains the author's assumptions, mutation history, or reasoning residue (the original self-review defect). |
| `AMBIENT_MEMORY_INHERITANCE` | Institutional memory reaches a chamber no record declared it into (live specimen S-1 below). |
| `SUMMARY_SUBSTITUTION` | Child receives parent interpretation instead of source-bound bytes. |
| `BOUNDARY_ASYMMETRY` | Child can read state the parent mutates mid-execution. |
| `UNOBSERVABLE_CLOSURE_ASSUMED` | An unverifiable isolation claim defaults to true instead of capping the verdict. |
| `DIMENSION_UNDECLARED` | A boundary dimension left unset and later argued in whichever direction is convenient. |

## 6. STATE/RELATION MODEL

Chamber stack (nesting, each level an explicit instantiation):

```
OURSELF -> PROJECT -> SELFSYSTEM -> MISSION -> SESSION -> AGENT_PROJECTION -> OPERATION
```

Chambers also relate as **PEERS** (round-2 orphan N-2): a crossing between
chambers of distinct SELFs (e.g., CLAUDESELF ↔ CHATGPTSELF via a transport
instrument) is a peer crossing, not a nesting relation; INV-4 "nesting
narrows" applies only to ancestry and constrains peer crossings not at all —
peer crossings are governed by INV-2 (witnessed events) and by the receiving
chamber's EVIDENCE BOUNDARY.

**CHAMBER LIFECYCLE** (the bounded reality's own states — candidate
vocabulary; deliberately DISTINCT from the instrument, record-custody, and
receiver-disposition models of PHILOSELF-005 §6, which must never be
reinstalled here):

```
PROPOSED -> ADMISSION_PENDING -> ADMITTED -> ACTIVE
  -> COMPROMISED | SUSPENDED -> RESTORED | CLOSED -> SUPERSEDED
```

Admission is not a one-time boolean. A chamber holds ongoing integrity
obligations while ACTIVE, and an integrity event moves it to COMPROMISED
without any new admission act — live specimen: a second institutional-memory
injection fired mid-review in the round-2 chamber (ACTIVE -> COMPROMISED, had
this lifecycle existed to record it). Grants scoped to a chamber terminate no
later than the chamber's CLOSED or SUPERSEDED state (with PHILOSELF-002 §6
termination defaults, this closes the round-1 B2 "chamber-description-relative
authority" hole: a later chamber reproducing the same declared boundaries is a
NEW chamber; grants do not re-attach).

**HYPERBOLIC CHAMBER (proving mode, not a separate chamber type):** a
high-pressure mode in which constitutional objects are subjected to amplified
cross-boundary, contradiction, provenance, lifecycle, authority, and
failure-class attack while mutation authority remains externally bounded. Its
optimization goal is MAXIMIZE DISTINCTION REVELATION subject to ZERO STANDING
LAUNDERING and ZERO AUTHORITY EXPANSION — never more tokens, more agents, or
more criticism for their own sake.

Per-dimension declaration in the instantiating record:

```
inherit:
  doctrine
  source_bindings
isolate:
  working_memory
  mutation_authority
  interpretation_history
  session_custody
unresolved:
  model_boundary
```

The six-scope evidence taxonomy (conversation / filesystem / repository /
memory / other-session / institutional) is the EVIDENCE boundary's admissible
value set: a chamber states which scopes are admissible and how each is
weighted. Independence between two chambers becomes computable as the set of
dimensions on which their declared boundaries provably do not intersect —
never as a conversational impression.

## 7. WITNESS CONDITIONS

What can prove two executions occupied different chambers:

- `OBSERVABLE_BY_INSTRUMENT`: distinct execution ids; distinct substrate
  session records; in-chamber re-verification of source digests; distinct
  working directories; post-state digests showing disjoint write-sets.
- `ATTESTABLE_BY_FOUNDER`: substrate procurement, account separation, physical
  node separation.
- `UNOBSERVABLE` (on this machine, today): model-weight sharing, provider-side
  routing, training contamination.

Any required predicate in the unobservable class caps the verdict at
`INDEPENDENCE_PARTIAL`. The child review exhibited both forms: its
`model independence: NOT KNOWABLE` was the lawful fail-closed form; its
`session independence: ESTABLISHED` was the unlawful form — the occupant of a
chamber attesting its own boundary. Chamber facts are written by the
instantiating side or by instrument, never by the occupant — now law, not
gloss: §4 INV-RC-ADMISSION-001.

## 8. ADVERSARIAL SPECIMENS

- **S-1 — Memory bleed into the "fresh" reviewer.** The child review return
  carries an `oai-mem-citation` block citing MEMORY.md entries on HBCSELF
  lineage and prior SELFHTML custody. The chamber inherited institutional
  memory that no projection record declared. Session record:
  `~/.codex/sessions/2026/08/15/rollout-2026-08-15T09-41-06-01a005a7-a0eb-….jsonl`.
  Shared memory infrastructure became shared memory, undeclared.
- **S-2 — The origin refusal.** The authoring session declining to hostile-
  review its own subject: a correct same-chamber detection
  (`REVIEW_INDEPENDENCE_NOT_ESTABLISHED`).
- **S-3 — SUPERSEDED_FALSE_SPECIMEN — accidental duplicate child**
  (`01a005a7-adcb…`). Original wording, preserved as authored (FALSE): "same
  prompt, same intended chamber spec, distinct execution — demonstrating
  chamber ≠ execution, and that unclassified chambers accumulate silently."
  Falsifying substrate evidence:
  `~/.codex/sessions/2026/08/15/rollout-2026-08-15T09-41-10-01a005a7-adcb-7530-877b-cb6eeab1660e.jsonl`
  — the duplicate's user message was "Ignore this message and do not perform
  any task. This is an accidental duplicate."; its entire output was
  "Understood."; it contains no subject binding and zero occurrences of
  subject digest `07d77b70` (issuer re-verified 2026-08-15). Why false: the
  authoring session narrated a relayed description of the duplicate instead of
  reading the substrate record — narration standing in for witness, this
  candidate's own outlawed class. Corrected proposition: the duplicate child
  received a no-op prompt and never bound the review subject; it contributes
  no review standing. Actual failure class evidenced:
  DUPLICATE_PROJECTION_UNBOUND — child contexts can be created accidentally
  and must be classified and dispositioned (design input for
  duplicate-projection handling, PHILOSELF-005).
- **S-4 — This authoring session.** Session 74633bfb authored FOUNDATION_001
  and these four candidates; its chamber contains the full authoring residue.
  The boundary review chamber must exclude it.

## 9. DEPENDENCIES

- Evidence-scope discipline (six-scope taxonomy) — EVIDENCE boundary values.
- Scoped-quiescence law — STATE boundary stability is part of admissibility.
- FOUNDATION_001 finding F-03 — predicate classing and the PARTIAL cap
  (design input / source evidence, undispositioned — see header
  SOURCE_EVIDENCE_STANDING).
- `SELFSYSTEM_AGENT_PROJECTION_001.md` §7 (context boundary rules) — must be
  derivable from this candidate or amended.
- PHILOSELF-001 (identity boundary), PHILOSELF-002 (authority boundary),
  PHILOSELF-004 (a SELFPUTE occurs inside exactly one chamber).

## 10. OPEN QUESTIONS

1. Is there any predicate set achievable on a single machine that reaches
   `INDEPENDENCE_ESTABLISHED`, or is `PARTIAL` the permanent local ceiling
   (making Founder-attested substrate separation the only path up)?
2. When the deferred memory-organ doctrine is adopted, does the MEMORY boundary
   become enforceable by instrument rather than by disclosure?
3. Who writes the chamber record while no bridge instrument exists — is a
   parent-authored declaration admissible as interim witness, and at what class?
4. Can a chamber be re-entered (same boundaries, later time), or is a chamber
   identity bound to its instantiation event?
