# ACTIMANIRUN-003A — TARGET-EFFECT CLAIM-STANDING CONFORMANCE REPAIR

```yaml
record_class: IMPLEMENTATION_CONFORMANCE_REPAIR_AND_VALIDATION_RECORD
gate: ACTIMANIRUN-003A
authorization_token: AUTHORIZE_ACTIMANIRUN_003A_TARGET_EFFECT_CLAIM_STANDING_CONFORMANCE_REPAIR_ONLY
authority_source: MYSELF (Founder transmission act, 2026-08-17)
executed_by: CLAUDESELF (Claude Code session f6c24428-68ac-4a61-a134-66d20e67d60c)
lease_scope: >
  Bounded lease for gate 003A only: the claimStanding conformance repair plus
  its focused tests in the implementation host, and custody of this single
  governance record. No adapter lease. No successor lease. Expires at STOP.
recorded_at_utc: 2026-08-17T11:02:46Z
custody_channel:
  branch: governance/actimanirun-000-custody
  pre_gate_tip: c884e4a06b4fcf5ff43d8264434ece0e625a43d3
  commit_hash: WITNESSED_IN_GATE_REPORT
  remote_publication: NOT_AUTHORIZED_THIS_GATE
implementation:
  host: /Users/millysituated/RUORA/systems/actimanirun
  pre_gate_commit:  083a5d097a1f139d916aa7413029055c558f0b45
  post_gate_commit: 6d3f814dbc57a0e76d1733aad49588f89d069a0b
  tests: 35 passed (pre) -> 44 passed, 0 failed (post)
verdict: 003A_PASS_CONFORMANCE_RESTORED
```

---

## §1 — SEALED SEMANTIC BASIS (verified before any code was written)

| Clause | Sealed bytes | What it fixes |
|---|---|---|
| 001 §7 ceiling law | *"a commit is movement evidence ONLY when the contract lists its class (e.g. **commit-to-declared-repo with target-effect binding**) in `accepted_movement_event_classes`"* | target-effect binding is a property of the **contract-declared class** |
| 001 §8 activity law | *"ONLY if the applicable contract defines that activity as a required target effect **AND evidence establishes the effect**"* | a source assertion is not evidence establishing |
| 001 §15 Specimen F | *"Commits fail the accepted_movement_event_class predicate (no target-effect binding) → MovementClaims derive as **INSUFFICIENT(no_target_effect)**"* | the sealed failure-reason name, preserved |
| 001 §15 Specimen B | *"contract accepts daemon-tick event class **with target effect = observation capture**"* | contract-side again, in the positive direction |
| 001B-A D-04 | *"applicable **effect-evaluation rule** + **reproducible satisfaction of that rule**"* | the predicate the repair installs |
| 001 §8 / 001C D-02 | `WITNESSED_MOVING ⇔ ∃ MovementClaim(standing=ESTABLISHED, t_event ∈ window)` | why the repair goes **inside** standing |

**`SEMANTIC_BASIS_ESTABLISHED`.** No new semantics were required and none were minted.
`target_effect_bound` appears **nowhere** in the governed corpus — probe
`git grep target_effect_bound HEAD -- governance/` returns hits only inside the
003 record. It was an implementation-invented field standing in for a governed
condition (SCOPED_NULL over the tracked governance tree).

## §2 — F1a REPRODUCED BEFORE REPAIR (mandatory first test)

One run, one contract with `effect_evaluation_rules: {}`, one effect identity
`READINESS_STATE_ADVANCED`, routed through both planes:

```
MOVEMENTCLAIM plane : ESTABLISHED
ADVANCES      plane : INSUFFICIENT(NO_EFFECT_EVALUATION_RULE)
movement_pulse      : WITNESSED_MOVING
INCONSISTENCY       : REPRODUCED
```

The same contract field was **enforced on one plane and ignored on the other**
(`derive.mjs:323` consulted `contract.effect_evaluation_rules`; `claimStanding`
never did). That is conformance, not ontology.

## §3 — PRE-REPAIR FAILING TESTS (test-first, witnessed)

Nine focused 003A tests were added and run against the **unmodified**
implementation: `35 passed, 9 failed` — every failure of the form
*"expected INSUFFICIENT, got ESTABLISHED"*.

## §4 — REPAIR SITE AND SHAPE

Site: `src/derive.mjs :: claimStanding` — inside establishment, never after it.

```
BEFORE:  if (!witness.target_effect_bound) -> INSUFFICIENT(NO_TARGET_EFFECT)
AFTER :  evaluateEffectRule(witness, contract) must be satisfied
```

`evaluateEffectRule` reads the rule from the **applicable MovementCadenceContract**
and the evidence from the **admitted witness**, and performs the comparison
itself. A source supplies **values**; it never supplies a verdict.

```
SourceAssertion != ContractDefinition
SourceAssertion != EffectEvaluationRule
SourceAssertion != EffectEstablished
SourceClaimsEffect != EffectEstablished
```

Typed failure reasons: `NO_TARGET_EFFECT` (sealed Specimen F name, preserved for
a witness with no effect claim) · `NO_EFFECT_EVALUATION_RULE` (D-001B-A-04
parity with the ADVANCES plane) · `EFFECT_RULE_METHOD_UNSUPPORTED` ·
`NO_EFFECT_EVIDENCE` · `EFFECT_EVIDENCE_INCOMPLETE` · `EFFECT_RULE_NOT_SATISFIED`.

`src/admit.mjs :: freezeWitness` now freezes `effect_evidence` into the
admission boundary, and carries `target_effect_bound` forward explicitly marked
as transported-not-trusted.

## §5 — MCC-003 AMENDMENT (validation contract only)

```yaml
ACTIMANIRUN-MCC-003-GOVERNANCE-LINEAGE:
  authority_ref: FOUNDER-ACT:ACTIMANIRUN-003A
  accepted_movement_event_classes: [GOVERNANCE_MILESTONE_CUSTODIED]   # unchanged
  effect_evaluation_rules:
    READINESS_STATE_ADVANCED:
      rule_ref: ACTIMANIRUN-MCC-003-EER-01
      method: DECLARED_EVIDENCE_PREDICATE
      required_evidence: [readiness_state_before, readiness_state_after, effect_artifact_digest]
      admissible_values:
        readiness_state_before: [INTERNAL_DISPOSITIONS_OPEN]
        readiness_state_after:  [IMPLEMENTATION_TOPOLOGY_CONFIRMED]
```

No new movement class. No global contract semantics amended. Direction is
carried by two **disjoint contract-declared sets**, so an unchanged readiness
state cannot satisfy the rule — no `must_differ` knob was minted. The rule
depends on none of the prohibited inputs (commit message, file count, author
assertion, `target_effect_bound`).

Evidence values are real: `INTERNAL_DISPOSITIONS_OPEN → IMPLEMENTATION_TOPOLOGY_CONFIRMED`
is D-001C-10's *"MINIMUM IMPLEMENTATION TOPOLOGY — CONFIRMED AT FOUR OBJECTS"*,
artifact digest `caad3914…829f` (001C bytes at `f091ae05`).

## §6 — POST-REPAIR HOSTILE BATTERY (real governance values)

| Test | claim standing | pulse |
|---|---|---|
| **POSITIVE** `f091ae05`, rule satisfied | `ESTABLISHED` | `WITNESSED_MOVING` |
| **NEGATIVE** `7d00b9f0` honest | `INSUFFICIENT(EVENT_CLASS_NOT_ACCEPTED)` | `NO_CURRENT_MOVEMENT_WITNESS` |
| **N2** over-claims class, no effect | `INSUFFICIENT(NO_EFFECT_EVIDENCE)` | `NO_CURRENT_MOVEMENT_WITNESS` |
| **N3** over-claims class + `target_effect_bound: true` | `INSUFFICIENT(NO_EFFECT_EVIDENCE)` | `NO_CURRENT_MOVEMENT_WITNESS` |
| **N4-A** admission-time rule failure | `INSUFFICIENT(EFFECT_RULE_NOT_SATISFIED)` | `NO_CURRENT_MOVEMENT_WITNESS` |
| **N4-B** established, later probe fails | `ESTABLISHED` + `TARGET_REALITY_DRIFT/FINDING` | `WITNESSED_MOVING` |
| **OLD EVENT** verified, outside window | `ESTABLISHED` | `NO_CURRENT_MOVEMENT_WITNESS` |
| **NO COVERAGE** | `INSUFFICIENT` | `UNKNOWN(NO_ADMITTED_SOURCE_COVERAGE)` |

**N3 — the primary F1a kill — is dead.** In 003 the identical input produced
`WITNESSED_MOVING`. **N4-B is intact**: F1a was repaired without destroying F1b.
`OLD EVENT` still shows `EstablishedClaim != CurrentMovement`.

## §7 — PRESERVED, PROVEN NOT MERELY ASSERTED

```
§8 biconditional : ESTABLISHED in-window claim ⇒ WITNESSED_MOVING (focused test)
PULSE_ELIGIBLE   : NOT CREATED — no such field, stage, or vocabulary exists
DriftDetected    != ClaimInvalidated        (N4-B)
LaterRealityFailure != HistoricalClaimErasure (N4-B)
Detection        != Repair                   (drift semantics untouched)
```

## §8 — DETERMINISM AND DERIVATION VERSION

```yaml
input_set_identity (both replays): f238695dab90d6c305d2db5c827017c2d37edd00a3f0e14ec79de95506063be9
projection_digest  (both replays): 278943a79a050ef7432809551193d2b2a3a4881d790a58b1455369571af898aa
run_1: 20260817T120000Z-actimanirun-c5201b9d1b77
run_2: 20260817T133711Z-actimanirun-c5201b9d1b77
same_input_set: true · same_projection_digest: true · run_ids_differ: true
```

**Derivation-version disposition — returned, NOT self-authorized.** A governed
search found **no rule requiring `derivation_version` to increment on semantic
change**; the only version-increment clause in the corpus governs a foreign
catalog (001B). The version was therefore left at `actimanirun-derive/v0.1`.

Measured cross-boundary behaviour: replaying the exact pre-repair 003 PASS-B
envelope now yields input set `c10046ac…` where 003 recorded `f365140f…` —
the identity **moved**, because `admit.mjs` now freezes `effect_evidence`. So
`SameInputSetIdentity + SameDerivationVersion → SameProjectionDigest` cannot be
violated by re-running an envelope.

**Residual hazard, stated plainly (`003A-F2`, candidate):** `derive()` accepts an
AdmissionRecord directly. A *persisted* pre-repair AdmissionRecord replayed
through the repaired core would carry the old `input_set_identity` and the old
version string yet produce a different projection digest. No such record exists
in custody today. Whether `derivation_version` must advance is a **Founder
disposition candidate**, not something this gate self-authorized.

## §9 — SCOPE DISCLOSURES (both deliberate, neither silent)

**(a) Fixture effect law — 4th changed path.** The repair broke 8 tests: every
specimen whose fixture contract carried `effect_evaluation_rules: {}` — the same
defect species in the test corpus, which never declared the contract-side law
because the code never read it. Specimens **A, B, D, E, G, H, I** were supplied
the effect law their sealed §15 descriptions already presuppose (B: *"target
effect = observation capture"*; D: *"the authorized target effect (durable
custodied semantic record)"*; H: sealed `claimStanding: ESTABLISHED`). **C**
(CLAIM_ONLY) and **F** (must not establish) were left untouched — F still fails
with the sealed `NO_TARGET_EFFECT`. Judged inside "focused tests may change";
flagged because it is a scope call, not an obvious inclusion.

**(b) `LEDGER.md` and `GOVERNANCE-BINDING.md` deliberately NOT touched.** The
host's ledger law arguably wants a 003A build entry, and the binding still pins
governance tip `f091ae05`, now two commits stale. Both were outside the write
set identified before editing, so widening was refused. **Proposed for Founder
disposition, not performed.**

## §10 — OPEN QUESTION CARRIED FORWARD

`003-F1b-PRESENTATION-CONSISTENCY` = **FOUNDER_DECISION_CANDIDATE.** Should a
consumer be required to read `movement_pulse` together with active drift
findings? Not answered here. No projection schema, UI, or pulse vocabulary was
changed.

## §11 — PASS CONDITIONS

1 source boolean can no longer establish · 2 contract-side law controls
establishment · 3 positive control still moves · 4 negative control does not ·
5 N3 killed · 6 admission-time failure does not establish · 7 later drift does
not erase history · 8 §8 biconditional intact · 9 no PULSE_ELIGIBLE · 10
deterministic replay holds · 11 no adapter created (0 files) · 12 no unrelated
changes (write set = 4 paths, disclosed) — **ALL MET.**

### VERDICT: **003A_PASS_CONFORMANCE_RESTORED**

## §12 — STOP

003B (read-only git adapter + mechanical acquisition) is now **ELIGIBLE TO BE
AUTHORIZED — still NOT AUTHORIZED and UNOPENED.** No adapter, no daemon, no
scheduler, no production connector, no push, no OMR/OSM/AgentBridge/SELFIR/
Notepad mutation, no successor self-authorized.
`ClaudeSELFRuntimeReality != CodexSELFRuntimeReality` — no cross-SELF propagation.

## §13 — BATTERY HARNESS (verbatim, for reproducibility)

`VALIDATION_HARNESS_LISTING != IMPLEMENTATION_CODE` — executed from outside the
implementation repository.

```javascript
// ACTIMANIRUN-003A · post-repair hostile battery against REAL governance values.
const IMPL = '/Users/millysituated/RUORA/systems/actimanirun/src';
const { executeRun } = await import(`${IMPL}/run.mjs`);

const M = 'ACTIMANIRUN:governance-lineage', S = 'actimanirun-governance-lineage-git';
const POS = 'f091ae05ead532947cfd08cd9b1071ade44a17e0', POS_T = '2026-08-17T09:23:56Z';
const NEG = '7d00b9f0845ad98e0aee65df0779183a91346cc5', NEG_T = '2026-08-17T10:51:34Z';
const TIP = 'c884e4a06b4fcf5ff43d8264434ece0e625a43d3';
const OBS = '2026-08-17T11:02:46Z', REF = '2026-08-17T11:02:46Z', DAY = 86400;

// ── MCC-003 AMENDMENT: the previously missing effect-evaluation rule ──────────
const EER = {
  rule_ref: 'ACTIMANIRUN-MCC-003-EER-01',
  method: 'DECLARED_EVIDENCE_PREDICATE',
  required_evidence: ['readiness_state_before', 'readiness_state_after', 'effect_artifact_digest'],
  admissible_values: {
    readiness_state_before: ['INTERNAL_DISPOSITIONS_OPEN'],
    readiness_state_after: ['IMPLEMENTATION_TOPOLOGY_CONFIRMED'],
  },
};
const mcc = (o = {}) => ({
  contract_ref: 'ACTIMANIRUN-MCC-003-GOVERNANCE-LINEAGE', manifestation_ref: M,
  authority_ref: 'FOUNDER-ACT:ACTIMANIRUN-003A', effective_from: '2026-08-17T07:30:40Z',
  accepted_movement_event_classes: ['GOVERNANCE_MILESTONE_CUSTODIED'],
  accepted_witness_classes: ['TRUTH_SOURCE'], elevated_signal_classes: [],
  expected_movement_window_seconds: DAY, maximum_lawful_silence_seconds: 7 * DAY,
  hold_exceptions: [], evaluation_route: 'actimanirun-derive/v0.1',
  effect_evaluation_rules: { READINESS_STATE_ADVANCED: EER },
  verification_classes: { READINESS_STATE_ADVANCED: 'ARTIFACT_BYTE_INSPECTION_AT_COMMIT' },
  ...o,
});
// REAL evidence, read from 001C bytes at f091ae05 (D-001C-10 topology CONFIRMED)
const POS_EVIDENCE = {
  readiness_state_before: 'INTERNAL_DISPOSITIONS_OPEN',
  readiness_state_after: 'IMPLEMENTATION_TOPOLOGY_CONFIRMED',
  effect_artifact_digest: 'caad3914062e98f923b54aa94439ed3f3ac546cf015bb46688049d71d950829f',
};
// HONEST evidence for 002A: its own record states effect_of_this_gate: NONE
const NEG_EVIDENCE = {
  readiness_state_before: 'IMPLEMENTATION_TOPOLOGY_CONFIRMED',
  readiness_state_after: 'IMPLEMENTATION_TOPOLOGY_CONFIRMED',
  effect_artifact_digest: '166e562ef5a1f6837c52f630ee3fc05d5b4e9e4f206475f1f8188f2964950f30',
};

const W = (o) => ({ witness_id: `GIT:${o.commit}`, manifestation_ref: M,
  movement_event_class: o.cls, effect_claim: o.effect ?? null,
  target_reality: o.effect ? 'ACTIMANIRUN governed readiness state' : null,
  event_time: o.t, target_effect_bound: o.bound === true,
  ...(o.evidence ? { effect_evidence: o.evidence } : {}),
  ...(o.probe ? { probe_result: o.probe } : {}) });

function run({ witnesses, ref = REF, obs = OBS, coverage = ['GOVERNANCE_MILESTONE_CUSTODIED'],
               evalTime = '2026-08-17T12:00:00Z' }) {
  return executeRun({
    envelopes: [{ source_identity: S, snapshot_identity: `gov@${TIP.slice(0,8)}`, snapshot_digest: TIP,
      observation_time: obs, coverage_state: 'FULL', witnesses,
      declarations: { cadence_contracts: [mcc()],
        institutional: [{ manifestation_ref: M, value: 'IMPLEMENTATION_HOST_GOVERNANCE_CUSTODIED', asserts_movement: false }] } }],
    admissionContracts: { [S]: { source_class: 'TRUTH_SOURCE', jurisdiction: 'RUORA governance custody',
      identity_namespace: 'ACTIMANIRUN', evidence_ceiling: 'GIT_OCCURRENCE_VIA_AGENT_TRANSCRIPTION',
      coverage, event_time_semantics: { clock_domain: 'UTC', carries_event_time: true },
      freshness_contract_seconds: DAY, expected_snapshot_digest: TIP } },
    observationOpenedAt: obs, observationClosedAt: obs,
    evaluationReferenceTime: ref, evaluationTime: evalTime,
  });
}
const sum = (label, r) => { const m = r.derivedContent.manifestations[0]; return {
  test: label, pulse: m.movement_pulse.value, unknown: m.movement_pulse.unknown_reason,
  claims: m.movement_claims.map((c) => `${c.movement_event_class}: ${c.standing.value}${c.standing.reason ? '(' + c.standing.reason + ')' : ''}`),
  drift: r.derivedContent.drift_findings.map((f) => `${f.drift_class}/${f.standing}`),
  digest: r.projection.projection_digest }; };

const o = {};
o.POSITIVE = sum('POSITIVE CONTROL · f091ae05, rule satisfied by real evidence',
  run({ witnesses: [W({ commit: POS, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: POS_T, bound: false, evidence: POS_EVIDENCE })] }));
o.NEGATIVE = sum('NEGATIVE CONTROL · 002A honest transcription',
  run({ witnesses: [W({ commit: NEG, cls: 'REPOSITORY_COMMIT', t: NEG_T, bound: false })] }));
o.N2 = sum('N2 · over-claims class, honestly lacks target effect',
  run({ witnesses: [W({ commit: NEG, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: NEG_T, bound: false })] }));
o.N3 = sum('N3 · PRIMARY F1a KILL — over-claims class AND asserts target_effect_bound=true',
  run({ witnesses: [W({ commit: NEG, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: NEG_T, bound: true })] }));
o.N4A = sum('N4-A · admission-time rule failure (honest 002A evidence)',
  run({ witnesses: [W({ commit: NEG, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: NEG_T, bound: true, evidence: NEG_EVIDENCE })] }));
o.N4B = sum('N4-B · established at t1, later target-reality probe fails at t2',
  run({ witnesses: [W({ commit: POS, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: POS_T, bound: false, evidence: POS_EVIDENCE,
    probe: { for_witness: `GIT:${POS}`, probe_id: 'LATER-ARTIFACT-PROBE', satisfied: false, detail: 'target reality diverged after establishment' } })] }));
o.OLD_EVENT = sum('OLD EVENT · verified effect outside the movement window',
  run({ witnesses: [W({ commit: POS, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: POS_T, bound: false, evidence: POS_EVIDENCE })],
        ref: '2026-08-18T10:23:56Z', obs: '2026-08-18T10:20:00Z' }));
o.NO_COVERAGE = sum('INSUFFICIENT COVERAGE',
  run({ witnesses: [W({ commit: NEG, cls: 'REPOSITORY_COMMIT', t: NEG_T, bound: false })], coverage: [] }));

const d1 = run({ witnesses: [W({ commit: POS, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: POS_T, bound: false, evidence: POS_EVIDENCE })], evalTime: '2026-08-17T12:00:00Z' });
const d2 = run({ witnesses: [W({ commit: POS, cls: 'GOVERNANCE_MILESTONE_CUSTODIED', effect: 'READINESS_STATE_ADVANCED', t: POS_T, bound: false, evidence: POS_EVIDENCE })], evalTime: '2026-08-17T13:37:11Z' });
o.DETERMINISM = { input_set_same: d1.admissionRecord.input_set_identity === d2.admissionRecord.input_set_identity,
  digest_same: d1.projection.projection_digest === d2.projection.projection_digest,
  run_ids_differ: d1.runRecord.run_identity !== d2.runRecord.run_identity,
  input_set: d1.admissionRecord.input_set_identity, digest: d1.projection.projection_digest,
  run_1: d1.runRecord.run_identity, run_2: d2.runRecord.run_identity,
  derivation_version: d1.runRecord.derivation_version };
console.log(JSON.stringify(o, null, 2));
```
