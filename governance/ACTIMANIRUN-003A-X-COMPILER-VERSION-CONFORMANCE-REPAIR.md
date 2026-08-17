# ACTIMANIRUN-003A-X — COMPILERVERSION CONFORMANCE REPAIR

```yaml
record_class: IMPLEMENTATION_CONFORMANCE_REPAIR_RECORD
gate: ACTIMANIRUN-003A-X
authorization_token: AUTHORIZE_ACTIMANIRUN_003A_X_COMPILER_VERSION_CONFORMANCE_REPAIR_ONLY
authority_source: MYSELF (Founder transmission act, 2026-08-17)
executed_by: CLAUDESELF (Claude Code session f6c24428-68ac-4a61-a134-66d20e67d60c)
lease_scope: >
  Bounded lease for gate 003A-X only: the CompilerVersion constant and its
  focused identity tests in the implementation host, plus custody of this single
  governance record. No host self-declaration reconciliation. No adapter. No
  successor. Expires at STOP.
recorded_at_utc: 2026-08-17T11:02:46Z
custody_channel:
  branch: governance/actimanirun-000-custody
  governance_parent: 15a8fbe771cfe847ea668ee4a68e099f24b1c68b
  commit_hash: WITNESSED_IN_GATE_REPORT
  remote_publication: NOT_AUTHORIZED_THIS_GATE
implementation:
  parent: 6d3f814dbc57a0e76d1733aad49588f89d069a0b
  commit: 315dc7af373d67dd8de9aa7305df65b216548b2d
  old_compiler_version: actimanirun-derive/v0.1
  new_compiler_version: actimanirun-derive/v0.2
  tests: 44 -> 50 passed, 0 failed
verdict: 003A_X_PASS_COMPILER_VERSION_CONFORMANCE_RESTORED
```

---

## §1 — SEALED BASIS (reverified mechanically before editing)

**001 §10** — `Distinct identities (none collapsible)`:
```
CompilerVersion    — derivation logic version
DERIVATION PHASE   — pure function: (InputSetIdentity, CompilerVersion) → DERIVED_CONTENT
SameInputSetIdentity + SameCompilerVersion → SameProjectionDigest
```
**001C D-02.1** — *"`derivation_version` is the canonical field name; it is the
SAME field sealed as `CompilerVersion` in 001 §10."*

`SEMANTIC_BASIS_ESTABLISHED`. The field's sealed meaning is the identity of the
derivation logic itself, so it must advance when that logic changes. **No new
semantics were required and none were minted.**

## §2 — F2 CLASSIFICATION AND RED WITNESS

```
003A-F2 = IMPLEMENTATION_CONFORMANCE_DEFECT
NoPersistedLegacyRecordExists != FieldValueIsTrue
```

Red witness taken at implementation `6d3f814d` **before** repair:

```yaml
constant_exported:                  actimanirun-derive/v0.1
runRecord.derivation_version:       actimanirun-derive/v0.1
derivedContent.derivation_version:  actimanirun-derive/v0.1
claim standing in that same run:    ESTABLISHED
```

That claim was establishable **only** through the 003A contract-side
effect-evaluation rule, which v0.1 logic did not contain. The run therefore
emitted a CompilerVersion naming logic that was not executing. A present
emitted-field defect, not a future migration hazard.

## §3 — NEW IDENTIFIER, MECHANICALLY JUSTIFIED

Lineage inspected with `git log -p --follow -- src/derive.mjs`: the constant has
carried **exactly one** value in its entire history — `actimanirun-derive/v0.1`.
Convention observed from that single precedent: `actimanirun-derive/v<major>.<minor>`.

**New value: `actimanirun-derive/v0.2`** — the smallest advance preserving the
observed convention. *Stated honestly:* no governed byte specifies increment
magnitude or a version grammar; only the requirement that the value identify the
logic. Magnitude is convention, not law.

**No identity primitive was created.** No `semantic_contract_version`, no
`implementation_digest`, no `compiler_identity_v2`, no `runtime_generation`.
CompilerVersion remains one field — asserted by a focused test that counts the
compiler-identity fields on a RunRecord and requires exactly one, named
`derivation_version`.

## §4 — WRITE SET (declared before editing, honoured exactly)

```
src/derive.mjs          — the constant + its law comment
tests/focused-tests.mjs — six CompilerVersion identity tests
```

## §5 — MEASURED DIGEST CONSEQUENCES (measured, not assumed)

| Identity | Effect of changing CompilerVersion |
|---|---|
| `InputSetIdentity` | **UNCHANGED** — `22974804…876f` under both values |
| `ProjectionDigest` | **CHANGED** — `f79228a9…` → `4bc32510…` |
| `RunRecord` identity | **CHANGED** — suffix `cdd2f8aa1e88` → `370788ebf457` |
| Projection identity | changes with its digest |
| derived semantic content | **byte-identical** (`manifestations` compared) |

```
AdmissionRecordIdentity != CompilerVersion      # CONFIRMED mechanically
```
The AdmissionRecord carries **no** version field at all; the version binds at
derivation time. Determinism under the new value holds: same input set → same
projection digest across replays, run ids differing.

## §6 — LEGACY ADMISSION RECORD

Search: implementation host tree at `6d3f814d` (all files, tracked and
untracked, plus directory enumeration — no run store, no records directory, one
`package.json`) and the tracked governance tree at `15a8fbe7`.

**`NO_PERSISTED_LEGACY_ADMISSION_RECORD`** — null graded **SCOPED_NULL** over
exactly those two surfaces. It does not cover other substrates. One filename
matched `admission` in the governance tree — `worlds/ureel-unreal-003/evidence/
gate-0007/attempt-0001/human-turn-evidence-admission.yaml` — which belongs to
the UREEL lineage and is not an ACTIMANIRUN AdmissionRecord.

Replay test performed anyway: an AdmissionRecord produced under the v0.1 label,
re-derived with the new CompilerVersion, yields a correctly version-bound
result (`rederived_version: actimanirun-derive/v0.2`, run id bound to the new
value, input set identity unchanged). **No migration system was built for
records that do not exist.**

## §7 — SEMANTIC REGRESSION: NONE

All eight 003A battery cases re-run under v0.2, verdicts compared:

| case | pulse / standing | unchanged? |
|---|---|---|
| POSITIVE | `WITNESSED_MOVING` / ESTABLISHED | YES |
| NEGATIVE | `NO_CURRENT_MOVEMENT_WITNESS` / INSUFFICIENT(EVENT_CLASS_NOT_ACCEPTED) | YES |
| N2 | `NO_CURRENT_MOVEMENT_WITNESS` / INSUFFICIENT(NO_EFFECT_EVIDENCE) | YES |
| **N3** | `NO_CURRENT_MOVEMENT_WITNESS` / INSUFFICIENT(NO_EFFECT_EVIDENCE) | YES — **still killed** |
| N4-A | `NO_CURRENT_MOVEMENT_WITNESS` / INSUFFICIENT(EFFECT_RULE_NOT_SATISFIED) | YES |
| **N4-B** | `WITNESSED_MOVING` / ESTABLISHED + `TARGET_REALITY_DRIFT/FINDING` | YES — **still lawful** |
| OLD EVENT | `NO_CURRENT_MOVEMENT_WITNESS` / ESTABLISHED | YES |
| NO COVERAGE | `UNKNOWN(NO_ADMITTED_SOURCE_COVERAGE)` | YES |

`SemanticOutputBeforeVersionRepair = SemanticOutputAfterVersionRepair`. Every
projection digest changed — lawfully, and only because CompilerVersion
participates in the derived identity, exactly as §10 requires.

## §8 — 003A-F3 · CLASSIFIED, NOT ABSORBED

**Contract inventory** (every `evaluation_route` in implementation and test
material): `fixtures/specimens.mjs:36` and `tests/focused-tests.mjs:469`, both
declaring `'actimanirun-derive/v0.1'`. Sole implementation site:
`src/derive.mjs` cadence drift — `contract.evaluation_route ? 'FINDING' :
'NEVER_MECHANICALLY_EVALUATED'`, a **truthiness test only**.

**Mechanical mismatch test, running compiler = v0.1 at test time:**

| declared route | drift standing |
|---|---|
| `actimanirun-derive/v0.1` (matches) | `FINDING` |
| `actimanirun-derive/v0.9` (no such compiler) | `FINDING` |
| `not-a-compiler-at-all` | `FINDING` |
| absent | `NEVER_MECHANICALLY_EVALUATED` |

**Version increment creates no mechanically observable mismatch** — nothing
compares the declared route to the running compiler, so F2 is fully separable
from F3 and the two stale `'v0.1'` route strings were left untouched.

Sealed 001 §4 legislates exactly one mechanical rule: *"A contract without a
declared `evaluation_route` is admissible as declaration, but its drift findings
carry standing `NEVER_MECHANICALLY_EVALUATED`."* The implementation obeys that
rule literally. Sealed bytes say nothing about whether a declared route must
**match** the evaluator that ran.

### F3 CLASSIFICATION: **`F3_SEMANTIC_DECISION_REQUIRED`** — separate gate required.

To make route-matching mechanical, three things absent from sealed law must be
decided: what identity a route names, what equality or compatibility means
between a route and a CompilerVersion, and what standing a mismatch produces.
Each is new semantics. The empirical law `DOCUMENTED_CONTRACT !=
EVALUATED_CONTRACT` supplies motive, not mechanism. **No F3 repair occurred; no
F3 repair is custodied here.**

## §9 — FIREWALL HONOURED

`GOVERNANCE-BINDING.md` sha256 `33c8d893…3a36` and `LEDGER.md` sha256
`ca3e597d…9e03` — **both untouched**, verified in the pre-commit witness.

```
F2RepairAuthority != HostSelfDeclarationReconciliationAuthority
```

Gate Y (host self-declaration reconciliation) is **eligible**, unopened, and
still correctly ahead of 003B. `003B` remains blocked behind Gate Y: unopened,
unauthorized, no adapter exists (0 files).

## §10 — PASS CONDITIONS

1 version truthfully identifies current logic · 2 no new identity primitive ·
3 semantic behaviour unchanged · 4 determinism preserved · 5 N3 still killed ·
6 N4-B still lawful · 7 F3 classified not absorbed · 8 GOVERNANCE-BINDING
untouched · 9 LEDGER untouched · 10 no adapter · 11 no push — **ALL MET.**

### VERDICT: **003A_X_PASS_COMPILER_VERSION_CONFORMANCE_RESTORED**

## §11 — STOP

No host narration repaired, no Gate Y opened, no adapter created, no live source
connected, no MovementPulse change, no identity primitive minted, no push, no
successor self-authorized. `ClaudeSELFRuntimeReality != CodexSELFRuntimeReality`.
