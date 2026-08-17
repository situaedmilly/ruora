# ACTIMANIRUN-001B — FOOTWORK GENERALIZATION CHARTER v0.1

```yaml
artifact_class: SEMANTIC_CHARTER_AND_FALSIFICATION_RECORD
gate: ACTIMANIRUN-001B
authorization_token: AUTHORIZE_ACTIMANIRUN_001B_FOOTWORK_GENERALIZATION_CHARTER_ONLY
authority_source: MYSELF (Founder disposition, 2026-08-17, relayed with Milasophahr commentary)
authored_by: CLAUDESELF (Claude Code session c23de3d6-1255-4dec-b130-d9eb8f625122)
created_at_utc: 2026-08-17T08:14:00Z
created_at_local: 2026-08-17T04:14:00-04:00
standing: >
  CHARTER_DISPOSITION_RECORDED · FALSIFIED_AGAINST_12_ATTACKS · NOTHING_MINTED ·
  NOT_RATIFIED — RecordedDisposition != FounderRatification. FOOTWORK remains
  FOUNDATIONAL_CANDIDATE / CANDIDATE_JUSTIFIED_NOT_MINTED (D-000A-05 unchanged).
lineage:
  parent_gates: ACTIMANIRUN-000 → 000A → 001 → 001A
  parent_commit: 723cfe0d5d55e57b245b8827429892c52ea54354
  branch: governance/actimanirun-000-custody
  resolves: ACTIMANIRUN-001 §17 item 5 (at semantic level; ratification pending)
lease:
  holder: CLAUDESELF session c23de3d6-1255-4dec-b130-d9eb8f625122
  subject: (GOVERNANCE-CANDIDATE:ACTIMANIRUN, gate ACTIMANIRUN-001B)
  scope: creation of this artifact + its evidence record + their custody commit ONLY
  granted_by: Founder token above (fresh grant; prior leases not revived)
  expires: at gate STOP; non-transferable; not inherited
authority_effect: NONE_UNLESS_SEPARATELY_RATIFIED
evidence_record: governance/evidence/ACTIMANIRUN-001B/CHARTER-EVIDENCE-RECORD-001.md
```

---

## §0 — PRIME NON-COLLAPSE LAW (BINDING FRAME)

```
ShapeCompatibility != SemanticIdentity
ExistingWorkObjectCanExpressFootwork != ExistingWorkObjectAlreadyMeansFootwork
```

No existing TASK, MISSION, dispatch object, proposal, or Founder question
acquires new semantics in this gate. Every object inspected below remains
byte- and meaning-identical to what its own jurisdiction says it is.

---

## §1 — EXACT WORK-OBJECT LINEAGE (BOUNDED READ-ONLY COMPARISON)

Six ancestors inspected at byte level (full extraction in the evidence
record; four load-bearing laws re-verified directly against source bytes):

| # | Ancestor | Identity | Jurisdiction | Mutation authority | Lifecycle | Completion | Scope | Relation support | Many-to-many M? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | AgentBridge T-object | `T-NNN` (one ID-less entry exists: `TASKS.md:1201`) | control plane `~/RUORA/systems/ourself-agent-bridge` (`TASKS.md:1-6`) | "authorized turn owner only. Append or update in-place. No silent edits." | free text: Sealed/Deferred/Open/NOT AUTHORIZED/BLOCKED — no enum | `Sealed` + sealing commit SHA; "Recording is not ratification." (`:1171`) | single repo; NO project/manifestation field | prose refs + single-valued Dependency column; `TRANSLATION_BOUNDARY: REQUIRED_NOT_IMPLEMENTED` (`:1182`) | **NO** |
| 2 | SELF Protocol MISSION (protocol layer) | noun in closed §4 catalog; no ID grammar | `~/RUORA/systems/self-protocol-suite` | "none may elevate itself" (`spec:216`); verb/subject grammar | 8-state enum in code; divergent illustrative prose | SEALED terminal, append-only transitions | one subject: "Every packet class must be traceable to exactly one primitive in §4 as its subject." (`spec:181`) | `zero or more Artifact references` (outputs only); no Manifestation primitive; §4 closed: "No other primitive may be introduced in v0" (`spec:77`) | **NO** |
| 3 | MISSION kernel record | `mission_id` `/^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/`; never reassigned | kernel `~/RUORA/projects/agent-bridge` — spec `INITIAL_DRAFT / PENDING_FOUNDER_REVIEW` | write-once `intent`; single-writer lease per mission_id; per-assignment grants, zero inheritance | 8-state enum, fail-closed transitions | "Reaching SEALED is a state fact only; it does not itself grant promotion authority" (`schema:63-65`) | one durable intent, one active executor | TaskPacket→mission_id one-way; "Multi-mission relationships … not addressed. Cross-repository mission references … not addressed." (`schema:155-157`) | **NO** |
| 4 | Æ DSL dispatch packet | `dsp-YYYYmmdd-HHMMSS-$$` (enqueuer-minted, collision-possible) | OURSELF Codex v3 (`~/OURSELF`) — NOT under OMR or kernel law | enqueue effectively unrestricted (JSON well-formedness only) | none on packet; file-existence lifecycle: enqueued→drained | **DRAINED = DELETED** — success destroys the packet's bytes; durable trace = Notion log row | single scalar `target` from closed 9-enum | `parent_aecho` single nullable string; no manifestation ref anywhere | **NO** |
| 5 | OMR Founder Question | **no ID of its own** — positional inside `<MAN-NNNNNN>-CANDIDATE` | OMR (OMR-007 generates, OMR-008 answers) | resolve: `authority_role: {"const": "MYSELF"}` | none on question; candidate carries PROPOSED/APPROVED/REJECTED/DEFERRED | all-or-nothing coverage of the array gates the decision; matching by prose string equality | single candidate | NONE — four scalar fields | **NO** |
| 6 | OMR MIG object | `^MIG-[0-9]{6}$` | OMR schemas/migration.schema.json | enters only at PROPOSED; transitions only; **no delete op exists**; COMPLETED hard-requires founder approval + ≥1 EVD | PROPOSED→(FOUNDER_APPROVED\|REJECTED)→COMPLETED | COMPLETED + approved:true + evidence | **single scalar `manifestation_id`**, `additionalProperties:false` | two conditional 1:1 pointers (merge/re-parent targets) | **NO** |

**Cross-cutting byte facts:** the `advances` relation exists NOWHERE in the
estate (zero grep hits across OMR, kernel, ~/OURSELF); `FOOTWORKLOG` appears
in exactly one file (the sealed 000 artifact) — coined classifier, never
implemented; the three governed regimes converge on the single authority
literal `MYSELF`; and **OMR already hosts a relation-record class** —
`REL-NNNNNN` (`relationship.schema.json`): binary
`source_manifestation_id → target_manifestation_id` with `evidence_refs[]`,
strictly manifestation↔manifestation, carrying NO work semantics. Verified
byte-exact. This is the ontological precedent §3 builds on.

## §2 — COLLISIONS OBSERVED (RECORDED, NOT REPAIRED — routed to owners)

1. **SELF Protocol spec/code divergence:** `TASK` and `HANDOFF` are live in
   the executable noun catalog (`src/primitives.js`) and grammar
   (`EXECUTE: ['TASK','MISSION']`) but ABSENT from the specification's closed
   §4 catalog — contradicting the spec's own laws at `:77` and `:102`.
   TASK has no ID grammar, no lifecycle, no completion semantics anywhere.
2. **MISSION lifecycle divergence:** `state-machine.js:24-25` dead-ends
   `PAUSED: []` / `INTERRUPTED: []` while `mission-kernel.v0.schema.md:55-56`
   allows exits from both.
3. **ID-less T-object:** `TASKS.md:1201` carries the full field schema with
   no stable ID — a live specimen for falsification F6.
4. **Two Æ packet regimes share one name:** the unvalidated delete-on-success
   `dispatch_queue` path vs the schema-contracted MYSELF-gated
   `ae-kernel-envelope.v1` path. Not the same object.
5. **Quad runtime evidence is untracked in git** — the corpus self-reports
   its authority claim as "DECLARED, not repository-evidenced."

ACTIMANIRUN may detect, not repair (001 §11 prime law). None of these become
typed drift findings in this gate (subclass admission = §17 item 7, open).

---

## §3 — MODEL ADJUDICATION

### MODEL A — NEW OBJECT: **REJECTED**

Survivable only if all existing identities necessarily distort the required
semantics. They do not — Model C expresses the semantics with zero identity
distortion. A new work-object identity would recreate the second-identity-
space collision (the MANI-/MAN- species) against SIX existing identity
regimes simultaneously.

### MODEL B — SPECIALIZED EXISTING WORK OBJECT: **REJECTED (three kills)**

1. **No parent exists to specialize.** The lineage is heterogeneous — six
   identity regimes across four jurisdictions (control plane, protocol suite,
   kernel, OMR, Æ/OURSELF). A subtype of any ONE parent cannot cover work
   from the others.
2. **Every candidate parent structurally refuses the relation without
   jurisdiction mutation:** T-objects have no schema to specialize and a
   foreign turn-owner law; the Protocol §4 catalog is closed by its own law
   (`:77`); the kernel Mission's `intent` is write-once with cross-repo
   references "not addressed"; MIG is sealed by `additionalProperties:false`.
   Specialization = parent schema amendment = prohibited foreign mutation.
3. **Falsifications F8/F9 kill it independently:** work performed outside
   AgentBridge, and Founder acts with no task object at all, must be able to
   advance manifestations. No subtype of a task system covers non-task work.

### MODEL C — ROLE/RELATION OVER EXISTING WORK OBJECT: **SELECTED**

```
Footwork(W, M)  =  the governed advancement relation between
                   work occurrence W and manifestation M

FootworkRole(W)  iff  ∃M : ADVANCES(W, M)
```

Footwork is not a second work identity. It is the semantic condition of a
bounded work occurrence standing in at least one typed ADVANCES relation.
Attacked (not assumed) — §5–§8 and the 12 falsifications in §9 are the
attack record. Estate precedent: OMR's REL-NNNNNN already proves
relation-records-with-identity-and-evidence are native to this estate; the
ADVANCES class is the same ontological species with (a) a WORK endpoint
instead of a second manifestation and (b) advancement semantics on the edge.

### MODEL D — GENERALIZED BASE WORK PRIMITIVE: **DEFER_SHARED_ONTOLOGY**

A substrate-neutral WORK parent would require amending the Protocol's closed
catalog (version increment + Founder authorization by its own law), the
kernel spec, OMR schemas, and the Æ regime simultaneously. Not required:
namespaced `work_ref` (§4) lets heterogeneous work objects participate in
ADVANCES without any shared parent type. STOP before ontology authoring, per
gate law.

### Relation to 001's GENERALIZE_EXISTING — REFINEMENT, NOT CONTRADICTION

001 §9 eliminated new-primitive and inherit-as-is, and named the T-object
generalization as the path — blocked on "mutating AgentBridge jurisdiction
(prohibited)". 001B resolves that exact blocker: the generalization is
lawful at the RELATION level, outside every parent object. The work-object
concept generalizes; no work object mutates. LaterRefinement !=
PriorContradiction.

---

## §4 — THE ADVANCES RELATION TOPOLOGY (EXACT CANDIDATE — NOT MINTED)

```yaml
advances_edge:                       # first-class RELATION record — not a work object
  edge_id: >                         # derived, content-bound, append-only:
    sha256-prefix over (work_ref, manifestation_ref, effect_class,
    declaration_act_ref) — never a positional or wall-clock ID
  work_ref: >                        # namespaced ref to ANY bounded work occurrence:
    AGENTBRIDGE-TASK:T-NNN | SELFPROTOCOL-MISSION:<mission_id> |
    QUAD:<proposal_id> | AEDSL-DISPATCH:<dispatch_id> | OMR-MIG:MIG-NNNNNN |
    GATE:<gate-id> | FOUNDER-ACT:<decision-ref> | COMMIT:<sha> | RECORD:<digest>
  manifestation_ref: OMR:MAN-NNNNNN | GOVERNANCE-CANDIDATE:<name> | source-native
  effect_class: <what kind of advancement is claimed>
  claimed_effect: <the specific effect>
  target_reality: <where the effect is claimed to hold>
  evidence_refs: []                  # existing evidence semantics (EVD-NNNNNN,
                                     # commit SHAs, record digests) — nothing minted
  standing: CLAIM_ONLY | INSUFFICIENT(typed_failure) | ESTABLISHED
                                     # REUSES 001 §8 MovementClaim standing verbatim —
                                     # no new standing vocabulary (gate law honored)
  declared_at: <typed time, 001 §5>  # declaration-plane
  observed_at: <typed time, 001 §5>  # evidence-plane
  completion_effect: <per-edge completion semantics>
  supersession_ref: <prior edge record | NONE>   # append-only; falsification
                                                  # supersedes, never rewrites
  declared_by: <actor + authority context>        # provenance mandatory
```

**Work-ref admission laws:**
- `work_ref` binds a STABLE identity where the jurisdiction has one (`T-NNN`
  never reused; `mission_id` never reassigned; `MIG-NNNNNN` minted).
- Where identity is weak or absent (the ID-less `TASKS.md:1201` entry;
  collision-possible `dsp-` IDs; identity-by-path across 19 agent-bridge
  dirs), `work_ref` MUST bind an immutable content address (commit SHA,
  record digest) — never a path, never a name.
- `NameChange != NewWork`: designation changes do not break edges bound to
  stable IDs or content addresses.

**Authority mapping (no new vocabulary — gate law honored):**

| Gate term | Maps to | Law |
|---|---|---|
| DECLARED_ADVANCEMENT | edge exists with standing CLAIM_ONLY | any W-side actor may declare; declaration needs provenance, never M-side authority |
| OBSERVED_ADVANCEMENT | witnesses attached, standing INSUFFICIENT(typed) until predicates met | witness per M's accepted event classes (001 §4/§7) |
| ESTABLISHED_ADVANCEMENT | standing ESTABLISHED | DERIVED by evidence law, reproducibly — never granted by fiat, never by W-side authority |

```
WorkerClaimsEffect != EffectEstablished
WorkObjectOwner    != ManifestationAuthority
```

## §5 — MANY-TO-MANY ADVANCEMENT LAW (CLOSED)

```
One WorkObject may advance many Manifestations.
One Manifestation may be advanced by many WorkObjects.
Each edge carries its OWN effect, evidence, standing, and completion semantics.
WorkCompleted           != ManifestationAdvanced
ManifestationAdvanced   != ManifestationCompleted
EdgeCount               != EffectCount   (establishment quantifies over witnessed
                                          effects — duplicate refs to one act
                                          dedupe by underlying witness identity)
```

A single global `completed: true` on W never implies identical advancement
across related manifestations: `Sealed` on a T-object, `SEALED` on a
Mission, `RECONCILED` on a quad are work-lifecycle facts in their own
jurisdictions; each edge still requires its own evidence to reach
ESTABLISHED.

## §6 — COMPLETION LAW (NON-COLLAPSE HELD, BYTE-GROUNDED)

```
WORK DECLARED != WORK STARTED != WORK PERFORMED != WORK COMPLETED
!= ADVANCEMENT CLAIMED != ADVANCEMENT WITNESSED
!= MANIFESTATION ADVANCED != MANIFESTATION COMPLETED
```

The estate ALREADY encodes the first half verbatim — this gate extends, it
does not invent: `EXECUTION_STARTED ≠ EXECUTION_COMPLETED ≠ RECONCILED`
(proposal-execution.js:14-16); "Reaching SEALED is a state fact only"
(mission-kernel §6); "Recording is not ratification." (TASKS.md:1171). The
extension: `WorkCompletion != AdvancementProof` — completion of W is at most
WITNESS INPUT to an edge whose effect_class admits it; it never
auto-establishes any edge. MANIFESTATION COMPLETED lives on the
institutional axis (OMR/OSM) — never derivable from edges (D-000A-01).

## §7 — AGENTBRIDGE FIREWALL (CHARTER ANSWERS)

The T-object is the nearest ancestor but is NOT selected as parent identity
(Model B rejected) — so **no AgentBridge object modification is required at
all**, which is stronger than the firewall demanded. Charter answers:

| Question | Answer |
|---|---|
| Does ACTIMANIRUN own the ADVANCES relation? | **NO.** Declared edges are source truth; ACTIMANIRUN owns only derivation logic, run records, projections (001 §12). It DERIVES edge standing as MovementClaims; it never authors or custodies declared edges. |
| Does AgentBridge own the work object? | **YES, unchanged.** TASKS.md untouched; its `TRANSLATION_BOUNDARY: REQUIRED_NOT_IMPLEMENTED` is satisfied FROM OUTSIDE — the edge store is the translation boundary's lawful home. |
| Who may create the relation? | A declarer admitted under the future edge-custody charter (§8). Founder always. W-side actors as claim-declarers (CLAIM_ONLY). |
| Who may claim advancement? | Any W-side actor with provenance → standing CLAIM_ONLY. |
| Who may establish advancement? | **No one, by authority.** ESTABLISHED is derived from witnesses per the manifestation's accepted event classes — reproducible derivation, not an act. |
| Does task completion create ACTIMANIRUN standing? | **NO.** Both jurisdictions already refuse completion→authority (promotion boundary; recording-is-not-ratification). Completion is at most witness input. |
| Can ACTIMANIRUN read task state without mutation authority? | **YES.** Read-only source admission per 001 §7 (task boards = CLAIM_SOURCE; sealing commits = TRUTH_SOURCE). |

```
ACTIMANIRUN projection authority != AgentBridge task mutation authority
```

## §8 — FUTURE CHARTER REQUIRED (EXACT, CROSS-JURISDICTION)

ONE charter act replaces the T-object-generalization charter 001
anticipated (which is NO LONGER REQUIRED):

**ADVANCES-RELATION CUSTODY CHARTER** — Founder decisions inside it:
1. **Custodian of declared edges.** Candidate with strongest evidence: OMR —
   it owns manifestation identity, already hosts the REL relation class,
   carries the EVD evidence law, append-only mutation law, no-delete store,
   and the MYSELF authority literal. Adding an ADVANCES record class is an
   OMR-jurisdiction schema act requiring Founder authorization.
2. **Declarer admission law** — who besides Founder may write CLAIM_ONLY
   edges, under what provenance requirements.
3. **Edge schema ratification** — §4 topology as the candidate.
4. **Weak-ID admission rules** — content-address requirements for ID-less/
   collision-prone work regimes.

Work-object jurisdictions (AgentBridge, SELF Protocol, Æ/OURSELF) require
**no mutation and no consent for edges to reference their stable IDs** —
reference is read-only. Notice-level acknowledgment is a courtesy decision
for the Founder, not a semantic requirement.

---

## §9 — REQUIRED FALSIFICATION — 12/12 HELD UNDER MODEL C

| # | Attack | Result under C |
|---|---|---|
| F1 | one task advances three manifestations | three edges, one W, per-edge effects. HELD |
| F2 | task completes; only one M receives witnessed advancement | edge standings independent; edge1 ESTABLISHED, others CLAIM_ONLY/INSUFFICIENT. WorkCompletion != AdvancementProof. HELD |
| F3 | task FAILS yet advances a research manifestation | W lifecycle FAILED in its jurisdiction; edge with effect_class `falsification_recorded` can be ESTABLISHED (live estate specimen: the MT5 GOLD ALCHEMY falsification chain advanced the research manifestation precisely by failing). Per-edge effect semantics are independent of W success. HELD |
| F4 | manifestation completed while task historically open | M state is institutional-axis; edges impose no reverse coupling. HELD |
| F5 | two agents on one W under separate leases | leases govern W-mutation (mission-kernel single-writer lease law); edges are separate records with declarer provenance; no shared mutable edge state. HELD |
| F6 | W changes designation without changing identity | edges bind stable ID or content address, never name/path; NameChange != NewWork. Live specimen: the ID-less TASKS.md:1201 entry is admissible only by content address. HELD |
| F7 | task with zero manifestation relations | no edges → no FootworkRole → task fully valid in its own jurisdiction. Role semantics make this trivial (a subtype could not). HELD |
| F8 | work performed outside AgentBridge | namespaced work_ref admits all six regimes + GATE/FOUNDER-ACT/COMMIT/RECORD. HELD (kills Model B) |
| F9 | Founder act advances M with no task object | work_ref = FOUNDER-ACT:<decision-ref>. HELD (kills Model B again) |
| F10 | ACTIMANIRUN observes work state, zero mutation authority | read-only admission (001 §7); projection authority != task mutation authority. HELD |
| F11 | duplicate work references count one act twice | live estate disease (19 agent-bridge dirs; identity-by-path lies). Admission resolves work_ref to canonical stable ID/content address; establishment quantifies over witnessed effects, deduped by underlying witness identity — EdgeCount != EffectCount. HELD |
| F12 | one edge later falsified without rewriting the work occurrence | append-only supersession_ref: falsification = new standing record superseding the edge; W's bytes and the work occurrence untouched (ratification-binds-evidence-state discipline). HELD |

## §10 — SHARED-WORK SPECIMEN (REAL, BOUNDED)

W = `GATE:ACTIMANIRUN-001` (bounded semantic/review act, custodied at commit
`f811d897`, artifact sha256 `c648f2f7…`):

```yaml
- ADVANCES(W, GOVERNANCE-CANDIDATE:ACTIMANIRUN):
    effect_class: semantic_closure
    evidence: commit f811d897 + artifact digest
    standing: ESTABLISHED
- ADVANCES(W, OMR reconciliation surface):
    effect_class: candidate_semantics_available_for_future_MAN_reconciliation
    evidence: none on the OMR side — OMR has never processed a founder decision
    standing: CLAIM_ONLY
- ADVANCES(W, governance custody/review lineage):
    effect_class: review_ready_artifact_appended
    evidence: branch history 65e5f9da → f811d897
    standing: ESTABLISHED
```

Same W · three M · three distinct effects · three distinct evidentiary
standings · zero duplication of W. The model expresses the specimen exactly.

## §11 — FOOTWORK NAME TEST — DISPOSITION

| Candidate type | Verdict |
|---|---|
| OBJECT_NAME | **REJECTED** — there is no Footwork object; minting one was rejected at Model A/B |
| ROLE_NAME | **SELECTED** — `FootworkRole(W) ⇔ ∃M: ADVANCES(W,M)`: the condition of work standing in ≥1 advancement relation |
| RELATION_CLASS | the relation class is named **ADVANCES** (not "Footwork edge" — no noun reification of the role onto the edge) |
| FOUNDER-FACING DISPLAY TERM | **ADMITTED** — "Footwork" may render wherever a human reads the role |

The Founder's original glitch — "some tasks can help multiple
manifestations" — is thereby explained rather than patched: the work never
belonged to one manifestation; it PARTICIPATES in multiple manifestation
trajectories through typed ADVANCES relations. The vocabulary survives; its
ontological type is role/relation, not entity.

## §12 — PRIMARY DISPOSITION

```
C — ROLE_RELATION_OVER_EXISTING
```

§17 item 5 of ACTIMANIRUN-001: **CLOSED_AT_SEMANTIC_LEVEL** — the original
decision ("charter a T-object generalization with AgentBridge") is
SUPERSEDED by a narrower decision requiring NO AgentBridge involvement:
ratify Model C + authorize the ADVANCES-relation custody charter (§8).
Founder ratification of both remains pending.

ACTIMANIRUN remains **semantically safe for a later 002**: the compiler
consumes declared edges as claim inputs and witnesses as truth inputs, and
derives standing — all inside the already-ratified 001 semantics
(MovementClaim, source admission, typed time). Nothing in this gate widened
ACTIMANIRUN's authority.

## §13 — UNRESOLVED FOUNDER DECISIONS (EXACT)

1. Ratify Model C and the §4 ADVANCES topology.
2. Ratify FOOTWORK as ROLE_NAME + display term (OBJECT_NAME rejected).
3. Authorize the ADVANCES-relation custody charter (§8) — custodian choice
   (candidate: OMR), declarer admission law, weak-ID rules.
4. Route the §2 collisions to their owning jurisdictions (SELF Protocol
   spec/code divergence; MISSION lifecycle divergence; ID-less T-entry;
   Æ regime name split; untracked quad evidence). Not ACTIMANIRUN's to repair.
5. Carried open from 001 §17: items 4, 6, 7, 8, 9, 10.

## §14 — ABSOLUTE STOP (EXECUTED)

STOP after this charter disposition. NO implementation · NO 002 · NO
AgentBridge mutation · NO SELF Protocol mutation · NO Footwork creation ·
NO edge store · NO Notepad · NO adapters · NO runtime · NO push · NO
departure from ACTIMANIRUN reality.
