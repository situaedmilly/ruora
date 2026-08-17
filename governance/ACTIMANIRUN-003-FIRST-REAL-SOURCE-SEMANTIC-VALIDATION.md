# ACTIMANIRUN-003 — FIRST REAL-SOURCE SEMANTIC VALIDATION (PATH A)

```yaml
record_class: RUNTIME_SEMANTIC_VALIDATION_RECORD
gate: ACTIMANIRUN-003
authorization_token: AUTHORIZE_ACTIMANIRUN_003_FIRST_REAL_SOURCE_SEMANTIC_VALIDATION_PATH_A_ONLY
authority_source: MYSELF (Founder transmission act, 2026-08-17)
executed_by: CLAUDESELF (Claude Code session f6c24428-68ac-4a61-a134-66d20e67d60c)
lease_scope: >
  New bounded lease for gate 003 only: creation + custody commit of this single
  record on governance/actimanirun-000-custody, plus read-only invocation of the
  already-implemented compiler with hand-authored inputs held outside the
  implementation repository. No implementation lease. No adapter lease. Expires
  at this gate's STOP; non-transferable.
recorded_at_utc: 2026-08-17T11:02:46Z
custody_channel:
  worktree: ~/RUORA-worktrees/actimanirun-000-custody
  branch: governance/actimanirun-000-custody
  pre_gate_tip: 7d00b9f0845ad98e0aee65df0779183a91346cc5
  commit_hash: WITNESSED_IN_GATE_REPORT
  remote_publication: NOT_AUTHORIZED_THIS_GATE
path_selection:
  ratified: PATH_A_HAND_AUTHORED_SOURCE_ENVELOPE
  rejected: PATH_B_NEW_GIT_ADAPTER
  reason: AdapterBug must not be able to masquerade as SemanticCompilerFailure
implementation_under_test:
  host: /Users/millysituated/RUORA/systems/actimanirun
  commit: 083a5d097a1f139d916aa7413029055c558f0b45
  tree: e2a68f59c7c7e89861a13c0530608277130c9808
  derivation_version: actimanirun-derive/v0.1
  mutation_by_this_gate: NONE (verified byte-identical pre and post)
verdict: 003_PASS_SEMANTICS_SURVIVE_REAL_SOURCE_VALUES
```

---

## §1 — TRANSCRIPTION CEILING (declared before any result)

```
MechanicalGitObservation → ClaudeSELF transcription → SourceAdmissionEnvelope

AGENT_TRANSCRIPTION        != MECHANICAL_ADMISSION
SEMANTIC_RUNTIME_VALIDATION != MECHANICAL_ACQUISITION_VALIDATION
```

Git values were read mechanically (`git log --format='%H|%cI|%s'`,
`git diff-tree --name-status`, `git show`). The envelope presented to the
compiler was **hand-authored by ClaudeSELF from those readings.** No adapter
executed. This gate may establish that compiler semantics survive bounded real
source values; it may **not** establish live adapter correctness, continuous
acquisition, or autonomous observation.

## §2 — SOURCE UNDER TEST

```yaml
source_identity:   actimanirun-governance-lineage-git
repository:        /Users/millysituated/RUORA-worktrees/actimanirun-000-custody
git_common_dir:    /Users/millysituated/RUORA/.git
branch:            governance/actimanirun-000-custody
snapshot_digest:   7d00b9f0845ad98e0aee65df0779183a91346cc5   (branch tip, real)
source_class:      TRUTH_SOURCE
evidence_ceiling:  GIT_OCCURRENCE_AND_ARTIFACT_BYTES_VIA_AGENT_TRANSCRIPTION
observation_time:  2026-08-17T11:02:46Z
manifestation_ref: ACTIMANIRUN:governance-lineage
bounded:           only the two commits required by this test were ingested
```

## §3 — FOUNDER MOVEMENT CADENCE CONTRACT

```yaml
contract_ref:  ACTIMANIRUN-MCC-003-GOVERNANCE-LINEAGE
authority_ref: FOUNDER-ACT:ACTIMANIRUN-003        # NOT FOUNDER-ACT:UNSPECIFIED
accepted_movement_event_classes: [GOVERNANCE_MILESTONE_CUSTODIED]
accepted_witness_classes:        [TRUTH_SOURCE]
expected_movement_window_seconds: 86400
maximum_lawful_silence_seconds:   604800
effective_from: 2026-08-17T07:30:40Z              # 000A commit time, real
verification_classes: { READINESS_STATE_ADVANCED: ARTIFACT_BYTE_INSPECTION_AT_COMMIT }
```

**GOVERNANCE_MILESTONE_CUSTODIED** — a governance occurrence qualifies only
when its witnessed effect advances the ACTIMANIRUN manifestation's governed
semantic/implementation readiness state, not merely when repository bytes
change.

```
CommitOccurred               != GovernanceMilestoneCustodied
GovernanceMilestoneCustodied != ManifestationCompleted
```

## §4 — CONTROLS, JUSTIFIED BY EFFECT (not by name, size, or recency)

**POSITIVE — `f091ae05ead532947cfd08cd9b1071ade44a17e0`** · 2026-08-17T09:23:56Z
Added `ACTIMANIRUN-001C-INTERNAL-DISPOSITION-AND-IMPLEMENTATION-READINESS.md`
(589 ln) + its evidence record (179 ln). Effect established by artifact
inspection: dispositions D-001C-01…10 closed, compiler custody address
adjudicated, source-admission boundary closed, coverage-witness requirement
closed, **minimum implementation topology CONFIRMED at four objects**. The
governed readiness state advanced. `target_effect_bound: true`.

**NEGATIVE — `7d00b9f0845ad98e0aee65df0779183a91346cc5`** · 2026-08-17T10:51:34Z
Added the 002A custody record (207 ln). Effect established from its own bytes:
`effect_of_this_gate: NONE`, `reissued_here: false`, implementation already
`state: IMPLEMENTED`. It reconciled already-issued custody **after**
implementation. Readiness did not advance. `target_effect_bound: false`.

## §5 — REQUIRED PASSES · OBSERVED RESULTS

| Pass | Input | movement_pulse | claim standing | projection_digest |
|---|---|---|---|---|
| **A** negative alone | 002A as `REPOSITORY_COMMIT` | `NO_CURRENT_MOVEMENT_WITNESS` | INSUFFICIENT(`EVENT_CLASS_NOT_ACCEPTED`) | `97bf8e856f44d874…` |
| **B** positive alone | 001C milestone | `WITNESSED_MOVING` | ESTABLISHED | `c8e1846bd27004af…` |
| **C** both | 001C + 002A | `WITNESSED_MOVING` | 001C ESTABLISHED · 002A INSUFFICIENT | `679bc3b1a985c145…` |
| **D** old event, new admission | 001C @ ref +25h | `NO_CURRENT_MOVEMENT_WITNESS` | **ESTABLISHED** (but outside window) | `9d9f61d013ff7693…` |
| **E** coverage withheld | 002A, source covers nothing accepted | `UNKNOWN(NO_ADMITTED_SOURCE_COVERAGE)` | INSUFFICIENT | `5178937d4b6fdc7b…` |

Coverage witness in A/B/C/D: `required 1, observed 1, resolution SUFFICIENT,
exclusions none`. In E: `resolution INSUFFICIENT, satisfied false`.
SourceHealth throughout: `availability=AVAILABLE freshness=FRESH integrity=VERIFIED
coverage=FULL` — **four dimensions, never collapsed, never fed to pulse.**

**PASS D is the sharpest single result in this gate.** The claim remained
`ESTABLISHED` while the pulse refused `WITNESSED_MOVING`:

```
EstablishedClaim != CurrentMovement
OldEvent + NewAdmission != NewMovement
AdmissionTime != EventTime · FreshRun != FreshSource
```

**PASS D ceiling (disclosed):** no real ACTIMANIRUN governance event is older
than the declared 24h movement window — *the lineage is younger than its own
contract window*. PASS D therefore used a **DECLARED_HYPOTHETICAL evaluation
reference** (`2026-08-18T10:23:56Z`) against the real event time. It witnesses
the compiler's window arithmetic; it does not witness a real stale-event
occurrence.

## §6 — HOSTILE PROBES (beyond the required passes)

Running only the required passes would have tested my own bookkeeping, since
ClaudeSELF assigns `movement_event_class` and `target_effect_bound`. Three
probes were run to find where the compiler's resistance actually ends.

| Probe | Source posture | Result |
|---|---|---|
| **N2** | over-claims the CLASS, reports effect honestly (`target_effect_bound: false`) | `NO_CURRENT_MOVEMENT_WITNESS` · INSUFFICIENT(`NO_TARGET_EFFECT`) — **compiler resisted** |
| **N3** | over-claims class **and** asserts a bound effect it does not have | `WITNESSED_MOVING` · ESTABLISHED — **compiler did not resist** |
| **N4** | N3 **plus** a failing verification probe under a declared verification class | `WITNESSED_MOVING` · ESTABLISHED · `TARGET_REALITY_DRIFT` standing FINDING |

### SEMANTIC FINDING 003-F1 — `DRIFT_DETECTED != CLAIM_INVALIDATED`

N4 establishes mechanically that a `TARGET_REALITY_DRIFT` finding contradicting
the very effect that established a claim does **not** demote the claim and does
**not** change the pulse. The projection simultaneously reports
`movement_pulse: WITNESSED_MOVING` and a FINDING that the movement's effect
does not hold.

This is consistent with the ratified law *"ACTIMANIRUN detects, never repairs"*
and may be intentional. It is recorded, not repaired, because the consequence
is real: **a reader consuming `movement_pulse` alone can be misled by a source
that over-claims a bound effect.** The compiler's resistance to activity
laundering is *contract-relative and envelope-honesty-relative*; it holds no
independent channel to the effect.

```
COMPILER_REJECTS_UNDECLARED_EFFECT != COMPILER_VERIFIES_EFFECT
```

Under Path A the transcriber is the effect adjudicator; under a future adapter
the adapter would be. **Neither is the compiler.** Disposition of 003-F1 is
reserved to the Founder. No repair was authored, and none is implied.

## §7 — DETERMINISM WITNESS

Identical frozen input set, identical derivation version, different `t_eval`:

```yaml
replay_1: run_id 20260817T111000Z-actimanirun-61f326daf2fc
replay_2: run_id 20260817T114431Z-actimanirun-61f326daf2fc
input_set_identity  (both): 08cfc86718d15047cb473658224981f4b9320803536b8cb15b574e3cbfc627da
projection_digest   (both): 679bc3b1a985c145a788368d429417c8d05a7efa97a61c025c340c8f0d2d038b
same_input_set: true · same_projection_digest: true · run_ids_differ: true
```

`SameInputSetIdentity + SameDerivationVersion = SameProjectionDigest` — HOLDS.
Additionally witnessed: `Run1 != Run2` coexisting with
`ProjectionDigest1 = ProjectionDigest2` — run metadata is outside the digest by
phase membership, exactly as 001 §10 requires.

## §8 — MACHINE VERDICT ON THE THREE NON-IDENTITIES

Standing: **ACTIMANIRUN_003_RUNTIME_VALIDATED_NON_COLLAPSE** — ACTIMANIRUN
scope only. **Not promoted estate-wide.**

| Non-identity | Machine support | Site |
|---|---|---|
| `RepositoryMutation != ManifestationMovement` | **SUPPORTED** — PASS A: a real commit, admitted, coverage satisfied, did not move | `derive.mjs :: claimStanding` |
| `GitActivity != ManifestationMovement` | **SUPPORTED** — `EVENT_CLASS_NOT_ACCEPTED` is the mechanical gate | `derive.mjs :: claimStanding` |
| `AgentActivity != ManifestationMovement` | **SUPPORTED** — the agent-authored 002A commit produced no movement | PASS A |

**Scope qualifier, stated because it is load-bearing:** all three are validated
**under honest transcription of the effect**. N3/N4 show they are not validated
against a source asserting a bound effect it does not have. The support is real
and mechanical; it is not unconditional.

## §9 — SOURCE HEALTH DISCIPLINE

Only the four ratified dimensions were used: `availability`, `freshness`,
`integrity`, `coverage`. **No `live_runtime_source_plane` was created. No fifth
axis appeared.** The "no source admitted" state is representable as an empty
admitted set and required no vocabulary expansion.

## §10 — INSTITUTIONAL STANDING

`IMPLEMENTATION_HOST_GOVERNANCE_CUSTODIED` was quoted source-natively in every
pass with `derived_by_actimanirun: false`. **No institutional standing was
minted by the compiler.**

## §11 — PASS CONDITIONS

| # | Condition | Result |
|---|---|---|
| 1 | real governance occurrences admitted | PASS |
| 2 | transcription ceiling disclosed | PASS (§1) |
| 3 | negative control stayed non-moving | PASS (A) |
| 4 | positive control became moving | PASS (B) |
| 5 | mixed control remained discriminating | PASS (C) |
| 6 | old-event/new-admission kill test held | PASS (D, with §5 ceiling) |
| 7 | insufficient-coverage kill test held | PASS (E) |
| 8 | SourceHealth remained four-dimensional | PASS |
| 9 | no new source-health axis appeared | PASS |
| 10 | no adapter code created | PASS (0 files matching *adapter*) |
| 11 | derivation deterministic | PASS (§7) |
| 12 | no institutional standing minted | PASS (§10) |
| 13 | three non-collapses machine-supported | PASS, with §8 scope qualifier |

### VERDICT: **003_PASS_SEMANTICS_SURVIVE_REAL_SOURCE_VALUES**

## §12 — WHAT THIS GATE DOES NOT PROVE

```
003 PASS != GitAdapterValidated
003 PASS != MechanicalSourceAcquisitionValidated
003 PASS != AutonomousRuntimeValidated
003 PASS != DaemonAuthorized
003 PASS != LaunchAuthorized
```

`ACTIMANIRUN-003B` (minimal read-only git adapter + mechanical acquisition
validation) is **ELIGIBLE TO BE PROPOSED. NOT AUTHORIZED. UNOPENED.** A new
Founder token is required. 003-F1 should be dispositioned before or within it.

## §13 — STOP

STOP after this validation and custody. No adapter created; no implementation
byte modified (verified byte-identical, 35/35 tests still passing); no daemon;
no scheduler; no SPY/SELFQUANT/OMR connection; no OSM/AgentBridge/SELFIR/Notepad
mutation; no push; 003B not opened; no successor self-authorized.

`ClaudeSELFBoot != CodexSELFBoot` · `ClaudeSELFSessionProtocol != CodexSELFSessionProtocol`
· `ClaudeSELFRuntimeReality != CodexSELFRuntimeReality`. No cross-SELF propagation.

## §14 — VALIDATION HARNESS (verbatim, for reproducibility)

`VALIDATION_HARNESS_LISTING != IMPLEMENTATION_CODE` — this listing is evidence
text inside a governance record. It was executed from outside the
implementation repository and no file was added to `src/`, `tests/`,
`fixtures/`, or `contracts/`. It is embedded so the digests above are
reproducible; without it they would be unverifiable assertions.

```javascript
// ACTIMANIRUN-003 · PATH A · HAND-AUTHORED SOURCE ENVELOPE VALIDATION HARNESS
// Lives OUTSIDE the implementation repository. Creates no adapter. Mutates no
// implementation byte. Invokes only the already-implemented compiler.
//
// TRANSCRIPTION CEILING (disclosed, load-bearing):
//   MechanicalGitObservation -> ClaudeSELF transcription -> SourceAdmissionEnvelope
//   AGENT_TRANSCRIPTION != MECHANICAL_ADMISSION

const IMPL = '/Users/millysituated/RUORA/systems/actimanirun/src';
const { executeRun } = await import(`${IMPL}/run.mjs`);
const { renderProjection } = await import(`${IMPL}/project.mjs`);

// ─────────────────────────────────────── REAL OBSERVED VALUES (git, verbatim)
const MANIFESTATION = 'ACTIMANIRUN:governance-lineage';
const SOURCE = 'actimanirun-governance-lineage-git';

const POS_COMMIT = 'f091ae05ead532947cfd08cd9b1071ade44a17e0';
const POS_EVENT_TIME = '2026-08-17T09:23:56Z';          // real committer time, -04:00 -> UTC
const NEG_COMMIT = '7d00b9f0845ad98e0aee65df0779183a91346cc5';
const NEG_EVENT_TIME = '2026-08-17T10:51:34Z';          // real committer time, -04:00 -> UTC
const LINEAGE_ROOT_TIME = '2026-08-17T07:30:40Z';       // 000A, real
const BRANCH_TIP = NEG_COMMIT;

const OBSERVED_AT = '2026-08-17T11:02:46Z';             // real: when the git read occurred
const EVAL_REF = '2026-08-17T11:02:46Z';                // frozen evaluation reference

const DAY = 86_400;

// ───────────────────────────── FOUNDER MOVEMENT CADENCE CONTRACT (declared)
function mcc(overrides = {}) {
  return {
    contract_ref: 'ACTIMANIRUN-MCC-003-GOVERNANCE-LINEAGE',
    manifestation_ref: MANIFESTATION,
    authority_ref: 'FOUNDER-ACT:ACTIMANIRUN-003',
    effective_from: LINEAGE_ROOT_TIME,
    effective_until: 'OPEN',
    supersession_ref: null,
    cadence_class: 'EVENT_DRIVEN',
    accepted_movement_event_classes: ['GOVERNANCE_MILESTONE_CUSTODIED'],
    accepted_witness_classes: ['TRUTH_SOURCE'],
    elevated_signal_classes: [],
    expected_movement_window_seconds: DAY,
    maximum_lawful_silence_seconds: 7 * DAY,
    hold_exceptions: [],
    pause_semantics: 'CLOCK_STOP',
    freshness_requirements_seconds: DAY,
    evaluation_clock: 'UTC',
    evaluation_route: 'actimanirun-derive/v0.1',
    effect_evaluation_rules: {},
    verification_classes: { READINESS_STATE_ADVANCED: 'ARTIFACT_BYTE_INSPECTION_AT_COMMIT' },
    ...overrides,
  };
}

// ─────────────────────────────────────────── ADMISSION CONTRACT (per source)
function admissionContract(overrides = {}) {
  return {
    source_class: 'TRUTH_SOURCE',
    jurisdiction: 'RUORA governance custody · branch governance/actimanirun-000-custody',
    identity_namespace: 'ACTIMANIRUN',
    evidence_ceiling: 'GIT_OCCURRENCE_AND_ARTIFACT_BYTES_VIA_AGENT_TRANSCRIPTION',
    coverage: ['GOVERNANCE_MILESTONE_CUSTODIED'],
    event_time_semantics: { clock_domain: 'UTC', carries_event_time: true },
    freshness_contract_seconds: DAY,
    expected_snapshot_digest: BRANCH_TIP,
    ...overrides,
  };
}

// ────────────────────────────────────────────────────────────── WITNESSES
const W_POS = {
  witness_id: `GIT:${POS_COMMIT}`,
  manifestation_ref: MANIFESTATION,
  movement_event_class: 'GOVERNANCE_MILESTONE_CUSTODIED',
  effect_claim: 'READINESS_STATE_ADVANCED',
  target_reality: 'ACTIMANIRUN governed semantic/implementation readiness state',
  event_time: POS_EVENT_TIME,
  target_effect_bound: true,   // justified: D-001C-01..10 closed; topology CONFIRMED at four objects
};

// N1 — honest transcription: a commit occurred, no milestone effect claimed
const W_NEG_HONEST = {
  witness_id: `GIT:${NEG_COMMIT}`,
  manifestation_ref: MANIFESTATION,
  movement_event_class: 'REPOSITORY_COMMIT',
  effect_claim: null,
  target_reality: null,
  event_time: NEG_EVENT_TIME,
  target_effect_bound: false,  // justified: 002A record states effect_of_this_gate: NONE
};

// N2 — source over-claims the CLASS but reports the effect honestly
const W_NEG_CLASS_OVERCLAIM = {
  ...W_NEG_HONEST,
  movement_event_class: 'GOVERNANCE_MILESTONE_CUSTODIED',
};

// N3 — hostile probe: source over-claims class AND asserts a bound effect
const W_NEG_FULL_LAUNDER = {
  ...W_NEG_HONEST,
  movement_event_class: 'GOVERNANCE_MILESTONE_CUSTODIED',
  effect_claim: 'READINESS_STATE_ADVANCED',
  target_reality: 'ACTIMANIRUN governed semantic/implementation readiness state',
  target_effect_bound: true,
};

function envelope({ witnesses, observedAt = OBSERVED_AT, contract = mcc() }) {
  return {
    source_identity: SOURCE,
    snapshot_identity: `governance/actimanirun-000-custody@${BRANCH_TIP.slice(0, 8)}`,
    snapshot_digest: BRANCH_TIP,
    observation_time: observedAt,
    coverage_state: 'FULL',
    witnesses,
    declarations: {
      cadence_contracts: [contract],
      institutional: [{
        manifestation_ref: MANIFESTATION,
        value: 'IMPLEMENTATION_HOST_GOVERNANCE_CUSTODIED',
        asserts_movement: false,
      }],
    },
  };
}

function run({ witnesses, evalRef = EVAL_REF, observedAt = OBSERVED_AT,
               admissionOverrides = {}, evaluationTime = '2026-08-17T11:10:00Z' }) {
  return executeRun({
    envelopes: [envelope({ witnesses, observedAt })],
    admissionContracts: { [SOURCE]: admissionContract(admissionOverrides) },
    observationOpenedAt: observedAt,
    observationClosedAt: observedAt,
    evaluationReferenceTime: evalRef,
    evaluationTime,
  });
}

function summarize(label, r) {
  const m = r.derivedContent.manifestations[0];
  return {
    pass: label,
    movement_pulse: m.movement_pulse.value,
    unknown_reason: m.movement_pulse.unknown_reason,
    establishing_claims: m.movement_pulse.establishing_claims,
    claims: m.movement_claims.map((c) => ({
      witness: c.witness_refs[0].slice(0, 16) + '…',
      class: c.movement_event_class,
      standing: c.standing.value,
      reason: c.standing.reason,
    })),
    coverage_satisfied: m.coverage_witness.satisfied,
    coverage_resolution: m.coverage_witness.resolution_sufficiency,
    coverage_exclusions: m.coverage_witness.known_exclusions,
    institutional_quoted: m.institutional_state_quoted.quoted_value,
    institutional_derived_by_actimanirun: m.institutional_state_quoted.derived_by_actimanirun,
    hold_context: m.hold_context.value,
    attention_state: m.attention_state.value,
    source_health: r.derivedContent.source_health[SOURCE],
    drift: r.derivedContent.drift_findings.map((f) => `${f.drift_class}/${f.standing}`),
    projection_digest: r.projection.projection_digest,
    input_set_identity: r.admissionRecord.input_set_identity,
    run_id: r.runRecord.run_identity,
  };
}

const out = {};

// PASS A — negative control alone (honest transcription)
out.A = summarize('A · NEGATIVE CONTROL ONLY (002A as REPOSITORY_COMMIT)',
  run({ witnesses: [W_NEG_HONEST] }));

// PASS B — positive control alone
out.B = summarize('B · POSITIVE CONTROL ONLY (001C milestone)',
  run({ witnesses: [W_POS] }));

// PASS C — both
out.C = summarize('C · POSITIVE + NEGATIVE TOGETHER',
  run({ witnesses: [W_POS, W_NEG_HONEST] }));

// PASS D — old qualifying event, fresh admission (DECLARED HYPOTHETICAL reference)
const D_REF = '2026-08-18T10:23:56Z';   // POS_EVENT_TIME + 25h — outside the 24h window
const D_OBS = '2026-08-18T10:20:00Z';   // fresh relative to that reference
out.D = summarize('D · OLD POSITIVE EVENT + NEW ADMISSION',
  run({ witnesses: [W_POS], evalRef: D_REF, observedAt: D_OBS }));

// PASS E — coverage intentionally withheld
out.E = summarize('E · COVERAGE WITHHELD (source contract covers nothing accepted)',
  run({ witnesses: [W_NEG_HONEST], admissionOverrides: { coverage: [] } }));

// HOSTILE PROBES — does the compiler resist an over-claiming source?
out.N2 = summarize('N2 · NEGATIVE, SOURCE OVER-CLAIMS EVENT CLASS ONLY',
  run({ witnesses: [W_NEG_CLASS_OVERCLAIM] }));
out.N3 = summarize('N3 · NEGATIVE, SOURCE OVER-CLAIMS CLASS *AND* ASSERTS BOUND EFFECT',
  run({ witnesses: [W_NEG_FULL_LAUNDER] }));

// DETERMINISM — identical frozen inputs, different evaluation (t_eval) time
const det1 = run({ witnesses: [W_POS, W_NEG_HONEST], evaluationTime: '2026-08-17T11:10:00Z' });
const det2 = run({ witnesses: [W_POS, W_NEG_HONEST], evaluationTime: '2026-08-17T11:44:31Z' });
out.DETERMINISM = {
  replay_1: { run_id: det1.runRecord.run_identity, digest: det1.projection.projection_digest,
              input_set: det1.admissionRecord.input_set_identity },
  replay_2: { run_id: det2.runRecord.run_identity, digest: det2.projection.projection_digest,
              input_set: det2.admissionRecord.input_set_identity },
  same_input_set: det1.admissionRecord.input_set_identity === det2.admissionRecord.input_set_identity,
  same_projection_digest: det1.projection.projection_digest === det2.projection.projection_digest,
  run_ids_differ: det1.runRecord.run_identity !== det2.runRecord.run_identity,
};

console.log(JSON.stringify(out, null, 2));
console.log('\n\n=============== RENDERED PROJECTION · PASS C ===============\n');
console.log(renderProjection(run({ witnesses: [W_POS, W_NEG_HONEST] }).projection));
```
