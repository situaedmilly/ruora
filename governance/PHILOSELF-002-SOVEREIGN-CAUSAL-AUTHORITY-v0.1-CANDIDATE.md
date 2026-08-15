# PHILOSELF-002 — SOVEREIGN CAUSAL AUTHORITY

```
STATUS:              CONSTITUTIONAL_CANDIDATE_v0.1
REVISION:            v0.3-state-establishment-repair-001 + residual-ledger-001
                     (2026-08-15; same authorization wave; residual surfaces:
                     M-11 capability retyping §6, M-22 promotion INV-8, M-20
                     dependency digest bindings + unrealized-referent marks)
CLASS:               philoSELF foundation (2 of 4)
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

AUTHORITY is the legitimate, bounded capacity to cause a state transition in a
governed reality.

Authority is jurisdiction over typed state transitions. It is not tool
possession, not permission flags, and not a sentence beginning "you are
authorized to". An authority statement that does not name which transitions of
which objects may be caused is a claim, not a grant.

## 2. NON-COLLAPSE LAWS

```
CAPABILITY        != PERMISSION
PERMISSION        != AUTHORITY
AUTHORITY         != SOVEREIGNTY
AUTHORITY_CLAIM   != AUTHORITY_GRANT
TOOL_SUCCESS      != LEGITIMACY
DISPOSITION       != RATIFICATION
CONSENSUS         != AUTHORITY          (NO_CONSENSUS_LAUNDERING)
DELEGATION        != SOVEREIGNTY_TRANSFER
INITIATION_AUTHORITY != ADMISSION_AUTHORITY != EXECUTION_AUTHORITY
                  != REVIEW_AUTHORITY != ADJUDICATION_AUTHORITY
                  != RATIFICATION_AUTHORITY
EXECUTION_DISCRETION != AUTHORITY_CLASS  (SELFauto is a grant property, §6)
REVIEW_FINDING    != SITUATED_DEFECT != REPAIR_OBLIGATION  (finding chain, §6)
```

- CAPABILITY: what this execution can technically do.
- PERMISSION: what operation the substrate allows.
- AUTHORITY: what state change may legitimately be caused.
- SOVEREIGNTY: who defines the governing conditions under which authority
  exists. Within RUORA jurisdiction, sovereignty rests with the Founder.

## 3. CONSTITUENTS

```
AUTHORITY
├── source                 issuing sovereign or delegator
├── domain                 governed reality it applies within
├── object_scope           which objects
├── permitted_transition   which X -> Y may be caused
├── forbidden_transition   which X -> Y may never be caused
├── preconditions          what must hold before exercise
├── expiration             when the grant lapses
├── delegation             whether and how far it may be re-granted
├── accountability         who answers for exercise
└── witness_requirement    what record exercise must produce
```

Example in the typed form:

```
HBCSELF-role grant
  MAY CAUSE:     candidate  UNKNOWN -> CHANGES_REQUIRED | PASS | BLOCKED
  MAY NOT CAUSE: candidate  CHANGES_REQUIRED -> REPAIRED
  MAY NOT CAUSE: candidate  * -> CANONICAL
```

**ExecutionGrant** — the fully-shaped EXECUTION-class grant (round-2 C12 D7
derivation, Founder-locked):

```
ExecutionGrant
├── holder                          the SELF holding the grant
├── SELFPUTE                        the authorized transformation (target)
├── chamber                         where it may be exercised (PHILOSELF-003)
├── write_set                       declared by the ADMISSION side in the grant,
│                                   never self-declared by the holder
├── authorized_transition_set       X -> Y families the holder may cause
├── subordinate_transition_closure  intermediate transitions (reads, scratch
│                                   writes, verification commands, retries)
│                                   inside the write_set are covered by the
│                                   grant without item-by-item authorization
├── prohibited_transition_set       what may never be caused
├── execution_discretion            SELFauto — autonomous selection of
│                                   subordinate operations WITHIN the closure
├── witness_requirements            what records exercise must produce
├── expiry                          by named event (INV-6)
├── revocation                      channel + propagation obligation
└── accountability                  who answers for exercise
```

SELFauto law: `execution_discretion` operates only inside
`subordinate_transition_closure`. It cannot create, widen, review, adjudicate,
or ratify its own grant. An operation that is a new state-transition proposal
rather than a subordinate execution choice exits the closure: STOP, new
authority required. This resolves the subordinate-operation gap (round-2 C12
D7): without the closure, a literal reading of this section makes every real
execution unlawful.

## 4. INVARIANTS

1. **Fail closed.** Unknown holder, unknown object, or unknown transition
   resolves to no authority (`router/sia-registry.js` precedent).
2. **No self-widening.** A holder may never widen its own envelope; widening is
   a sovereign act.
3. **Delegation is monotone-narrowing.** Delegated authority is a subset of the
   delegator's; a chain never widens.
4. **Exercise leaves a record.** Every exercised authority binds grant →
   caused transition → evidence. Unwitnessed exercise is unlawful exercise.
   Scope: this invariant governs ORDINARY_PHILOSELF_OPERATION
   (post-commencement). Acts of the PRE_CONSTITUTIONAL_STATE and the
   commencement act itself are governed by the commencement article
   (PHILOSELF-004 §4 INV-6); the FOUNDING_WITNESS satisfies commencement only,
   never this invariant.
5. **No post-hoc grant.** A parent may not expand a child's authority after
   output receipt; results produced beyond grant are rejected, not adopted.
6. **Expiration requires trusted time.** Until TRUSTED-TIME-SOURCE-01 is
   dispositioned, grants expire by named event, not by clock.
7. **INV-AUTH-SEPARATION-001 (separation of duty).** For the same transition
   family T of the same object O: `EXECUTION(a,T) ⇒ ¬REVIEW(a,T)`;
   `REVIEW(a,T) ⇒ ¬RATIFICATION(a,T)`; `REVIEW(a,D) ⇒ ¬ADJUDICATION(a,D)` for
   the same divergence D. ADMISSION_AUTHORITY over a chamber's boundary facts
   may not be held by any entity `AffectedByBoundary` of those facts
   (PHILOSELF-003 §4 INV-7). INITIATION composes freely with any class — it
   causes a state of the process, never of the subject. This invariant states
   as constitutional law the separation previously stranded in frozen
   X1 §6.7/§6.8 (round-2 M-9).
8. **Grant existence, admissibility, and non-exercise witness are law (M-22
   promotion).** A grant exists only as a sovereign-side record — a grant
   living only in a runtime's narration does not exist (§7.1). The §6
   admissibility filter binds every SELFPUTE with its three distinct refusals
   never collapsed. Non-exercise is witnessed only by digest pairs over the
   FULL declared write-set inside the cited record or a separately bound
   witness (§7.3). Detailed prose remains in §6/§7; this invariant is their
   force.

## 5. FAILURE MODES

| Failure | Meaning |
|---|---|
| `CAPABILITY_INFERRED_AS_AUTHORITY` | Possession of a tool treated as license to cause the transition. |
| `SELF_WIDENING` | Holder expands own envelope mid-exercise. |
| `AMBIENT_INHERITANCE` | Child acquires parent's authority through shared environment rather than explicit grant. |
| `CONSENSUS_LAUNDERING` | N agreeing runtimes treated as minting authority none of them holds (design input: FOUNDATION_001 finding F-04, undispositioned). |
| `POST_HOC_GRANT` | Out-of-envelope output adopted after the fact. |
| `REVOCATION_LAG` | Running manifestation continues under a revoked grant. |
| `CLOCK_ASSUMPTION` | Time-bounded grant adjudicated against an untrusted clock. |

## 6. STATE/RELATION MODEL

Grant lifecycle:

```
DRAFTED -> ISSUED -> ACTIVE -> EXERCISED(n) -> EXPIRED | REVOKED | EXHAUSTED
```

Admissibility filter (the relay's ratified correction — capability is the
middle term, not a fifth foundation):

```
T ∈ Capability(manifestation @ substrate, Chamber)
∧ T ∈ Authority(SELF, Chamber)
∧ Preconditions(T, Chamber) = SATISFIED
        ↓
ADMISSIBLE SELFPUTE(T)
```

(M-11 retyping: capability is a property of a manifestation on a substrate
within a chamber — never of the SELF in the abstract. The same SELF projected
onto two substrates has two capability sets; `Capability(SELF)` was not a
function. This §6 index is THE single home of capability; PHILOSELF-001 §3's
CAPABILITY constituent and PHILOSELF-005 §3's capability field both refer
here. A transition absent from this chamber's capability set is
UNAVAILABLE-HERE; only a transition absent from every lawful manifestation's
set is IMPOSSIBLE — the two refusals never collapse.)

A transition outside Capability is impossible; outside Authority, unlawful;
outside Chamber preconditions, inadmissible. Three distinct refusals, never
collapsed into one.

**Six authority classes as grant shapes** (round-2 C12 D1, accepted): each
class is an equivalence class of §3 grants under "same permitted_transition
family" — a relation between a holder and a transition family, not a role and
not a new authority type:

```
INITIATION     process_instance : ∅         -> REQUESTED
ADMISSION      chamber_boundary : UNDECLARED -> DECLARED ; standing established
EXECUTION      artifact_content : c         -> c'
REVIEW         verdict_record   : UNKNOWN   -> {PASS|CHANGES_REQUIRED|BLOCKED}
ADJUDICATION   divergence       : OPEN      -> DISPOSED
RATIFICATION   standing         : CANDIDATE -> IN_FORCE
```

Termination defaults (candidate law; each rebuttable only by explicit grant
text): INITIATION exhausts on use; REVIEW exhausts on return delivery;
EXECUTION is bounded by its declared write_set and terminal conditions;
ADMISSION exhausts on the chamber's closure; ADJUDICATION exhausts on the
divergence's closure; RATIFICATION is sovereign and does not delegate
(`DELEGATION != SOVEREIGNTY_TRANSFER`) — its exercise is recorded per act, and
a surviving ratification power is the Founder's alone.

**ProofRule activation authority (R2 integration).** Activating a ProofRule
(PHILOSELF-005 §6) is an exercise of domain-scoped ADJUDICATION_AUTHORITY —
grant shape `proof_rule_status: REGISTERED -> ACTIVE`, scoped to a claim-type
domain. NO new authority class exists for this (`PROOF_RULE_AUTHORITY` is not
a thing and must never become one). Separation of duty applies with full
force: RULE_AUTHORSHIP != RULE_REGISTRATION != RULE_ACTIVATION !=
RULE_APPLICATION != STANDING_ADJUDICATION — a rule's author is never its
activator by default (INV-7 analogue over the rule's own lifecycle), a
registry's custody of a rule confers no authority over it, and activation
grants neither ratification authority nor standing beyond the rule's own
standing_ceiling.

**Finding chain** (REVIEW-class output law): `REVIEW_FINDING != TRUTH`. The
chain runs REVIEW OUTPUT -> CLAIMED FINDING -> COUNTEREXAMPLE/EVIDENCE ->
VALIDATION -> SITUATED DEFECT -> FOUNDER/AUTHORIZED DISPOSITION -> REPAIR
OBLIGATION. A reviewer cannot create a repair obligation by labeling something
a finding; `finding` remains an ordinary evidence term for an instrumented
review's output.

## 7. WITNESS CONDITIONS

1. Grants are records issued from the sovereign side; a grant that exists only
   in a runtime's narration does not exist.
2. Exercise witness: `grant_id → transition (pre-state digest, post-state
   digest) → instrument evidence`.
3. Non-exercise is witnessable in principle: post-state digest equal to
   pre-state digest, over the full declared write-set, under a
   mutation-forbidding grant — and the digest pair must exist inside the cited
   witness record or in a separately bound witness.
   **SUPERSEDED_FALSE_SPECIMEN** — original wording, preserved as authored
   (FALSE): "(live: subject `07d77b70…` byte-identical after the REVIEW_ONLY
   child run)". Falsifying substrate evidence:
   `~/.codex/sessions/2026/08/15/rollout-2026-08-15T09-41-06-01a005a7-a0eb-7991-a959-c488b16c2d1e.jsonl`
   contains `shasum` records at lines 18 and 24 only, both pre-review; the
   cited record holds NO post-state digest. Why false: post-run equality was
   established by a different session (74633bfb) outside the cited record;
   attributing it to the record was narration counterfeiting witness. Corrected
   proposition: the cited record witnesses a pre-state digest only; it did not
   itself witness post-state equality. Actual failure class evidenced:
   NON_EXERCISE_NOT_WITNESSED_BY_CITED_RECORD — a compliance claim lacking its
   closing witness inside the record cited for it.
4. Witness predicates are classed observable / attestable / unobservable and
   fail closed. This classing stands on this candidate's own force; its
   historical design input is FOUNDATION_001 finding F-03 (undispositioned
   source evidence, not authority).

## 8. ADVERSARIAL SPECIMENS

- **S-1 — REVIEW_ONLY child with write capability.** Codex child
  `01a005a7-a0eb…` held filesystem write capability while holding review-only
  authority; capability present, authority absent. Single-file digest equality
  was later established by the issuer session outside the child's own record
  (see §7.3 SUPERSEDED_FALSE_SPECIMEN) and under-witnesses the full write-set.
- **S-2 — Robinhood MCP under Ra-seal.** Order-capable write tools are mounted
  and callable; constitutional quarantine forbids their exercise. Standing
  capability under standing prohibition.
- **S-3 — Discord permission API.** Recorded permission-surface bugs
  (IntituSELF rehearsal guild): permission readback disagreed with effective
  permission — PERMISSION itself can be a false witness.
- **S-4 — `minimum_valid_returns: 2`.** The FOUNDATION_001 command's quorum
  arithmetic: two concurring child verdicts treated as stronger authority.
  Verdicts are never merged; the Founder adjudicates divergence.

## 9. DEPENDENCIES

- sia-registry — fail-closed route/role authority precedent. Binding (M-20):
  repository RUORA, path
  `systems/ourself-agent-bridge/router/sia-registry.js`, sha256
  1e4cd1bcf9a8f2c60d87bc0e07f74eb1ed86dbbd20cadd7291e1fd979b224752 (five
  `-pass-21aN` siblings disclosed; this binding names the original only).
- ADMISSION-REVOCATION-CHANNEL-01 — **UNREALIZED_DESIGN_REFERENT** (M-20/
  SPEC2-F5 honesty: no file at any `DESIGN/` path resolves; the referent is a
  design-intent name, not an artifact; INV-6 and OQ-1 depend on its future
  realization and gain nothing from it today).
- ROBINHOOD-AGENT-001 / Ra-seal — live capability-vs-authority regime
  (memory-scope referent, disclosed as such since round 1).
- TRUSTED-TIME-SOURCE-01 — **UNREALIZED_DESIGN_REFERENT** (same class as
  above; INV-6's clock prohibition therefore stands with no opening gate until
  the referent is realized and dispositioned).
- PHILOSELF-001 (an authority HOLDER must have SELFhood; instruments never
  hold authority — they operate UNDER a holder's grant cited by
  `constituting_grant_ref`, PHILOSELF-005 §3 — round-2 M-3 resolution),
  PHILOSELF-003 (authority is chamber-relative), PHILOSELF-004 (authority is
  exercised only as SELFPUTE).

## 10. OPEN QUESTIONS

1. How does revocation propagate to an already-running manifestation, and what
   is the lawful state of work performed between revocation and halt?
2. Who adjudicates cross-SELF authority disputes below the Founder, if anyone?
3. Can authority attach to a SELF whose SELFhood is unresolved (interlock with
   F-02), or does unresolved identity void all grants?
4. Is there any lawful ambient authority at all (e.g., self-preservation of
   records), or is the ambient set strictly empty?
