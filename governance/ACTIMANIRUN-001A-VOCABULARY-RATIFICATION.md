# ACTIMANIRUN-001A — VOCABULARY RATIFICATION RECORD

```yaml
record_class: FOUNDER_RATIFICATION_RECORD
gate: ACTIMANIRUN-001A
authorization_token: FOUNDER_DISPOSITION_ACTIMANIRUN_001_VOCABULARIES
authority_source: MYSELF (Founder disposition, 2026-08-17, relayed with Milasophahr commentary)
executed_by: CLAUDESELF (Claude Code session c23de3d6-1255-4dec-b130-d9eb8f625122)
lease_scope: >
  New bounded lease for gate 001A only: creation + custody commit of this
  single record. The expired 000/000A/001 leases were NOT revived. Expires at
  this gate's STOP; non-transferable; not inherited by successor sessions.
recorded_at_utc: 2026-08-17T08:00:37Z
recorded_at_local: 2026-08-17T04:00:37-04:00
commit_hash: WITNESSED_IN_GATE_REPORT   # a record cannot contain its own commit hash
subject_binding:                       # ratification binds evidence state
  subject_commit: f811d897f2742d480ac5d4be007529de69c5a9a5
  subject_artifact: governance/ACTIMANIRUN-001-LIVE-PROJECTION-SEMANTICS-AND-FALSIFICATION-v0.1.md
  subject_sha256: c648f2f785ce8e1d56ee4636b67d88fb61235872a828466ab20c40ce9f949384
  verification: >
    PASS — HEAD at gate open = subject_commit exactly; blob digest at
    subject_commit recomputed and matched in full; working tree clean; all
    five governed ACTIMANIRUN artifacts byte-identical to their seals.
  extraction_method: >
    All ratified members below were extracted mechanically from the blob at
    subject_commit (git show f811d897:<path>), NOT reconstructed from
    conversation commentary or memory-organ projections, per the Founder
    instruction "DO NOT reconstruct values from commentary."
historical_law: LaterRatification != OriginalAuthorship — subject bytes untouched
ratification_scope: SEMANTIC VOCABULARY ONLY
```

---

## RATIFIED VOCABULARY 1 — MOVEMENTPULSE (subject artifact §1.1–§1.2)

Ratified exactly as closed by ACTIMANIRUN-001, three members:

```
WITNESSED_MOVING
NO_CURRENT_MOVEMENT_WITNESS
UNKNOWN(unknown_reason)
```

with the mandatory typed reason set (§1.2):

```
unknown_reason ∈ { NO_ADMITTED_SOURCE_COVERAGE, TIME_SEMANTICS_UNRESOLVED,
                   IDENTITY_UNRESOLVED, ADMISSION_UNRESOLVED, WINDOW_UNRESOLVED }
```

"Exactly as closed" binds each member WITH its §1.2 closed semantics —
including the SILENCE REQUIRES COVERAGE law (a lawful
NO_CURRENT_MOVEMENT_WITNESS requires witnessed observation coverage of the
accepted event classes inside the freshness requirement; silence from an
unobserved or uncovered channel is UNKNOWN, never evaluated silence) and the
§1.3 fourth-value rejection. A vocabulary member without its bound meaning
would be a bare string, not a ratified type.

## RATIFIED VOCABULARY 2 — HOLDCONTEXT (subject artifact §2.2–§2.3)

Ratified exactly as enumerated in the content-bound artifact, six members:

```
NONE_DECLARED
WAITING_FOUNDER(ref)
WAITING_EXTERNAL(ref)
WAITING_DEPENDENCY(ref)
LAWFUL_QUIET(contract_ref)
UNKNOWN
```

Bound with: the §2.1 declared-plane law (every non-NONE value requires a
declaration act with provenance and review/expiry); the §2.3 **BLOCKED_CONTEXT
REJECTION** (name collision with institutional BLOCKED; decomposition into the
three WAITING_* forms; unnameable blockers are not declarable holds); and the
§2.2 narrowing of 000 §5's LEASE_HELD_ELSEWHERE into WAITING_DEPENDENCY
(a lease is an estate object).

## RATIFIED VOCABULARY 3 — ATTENTIONSTATE (subject artifact §3.2–§3.4)

Ratified exactly as closed by ACTIMANIRUN-001, four members:

```
FOREGROUND
BACKGROUND            # DEFAULT
DORMANT_BY_LAW(law_ref)
UNKNOWN
```

Bound with: the §3.2 **ESCALATED REJECTION** (escalation is an ACT whose
lawful effect is a transition to FOREGROUND, carrying the act reference as
provenance — never a state value); and the §3.3 placement ruling
(DORMANT_BY_LAW belongs to AttentionState, not HoldContext).

---

## SCOPE FIREWALL (VERBATIM FROM THE DISPOSITION)

This ratification is SEMANTIC VOCABULARY ONLY. It does NOT authorize:

ACTIMANIRUN-002 · implementation · adapters · Footwork · Notepad ·
AgentBridge mutation · runtime execution · remote publication · push ·
institutional-standing projection · drift repair.

No implementation authority was inferred, claimed, or exercised in this act.
The subject artifact's remaining closures (§4–§13: cadence contract, time
model, SourceHealth, admission, MovementClaim, run identity, drift subtypes,
host disposition, topology) remain CLOSED_UNRATIFIED — their Founder
dispositions are §17 items 4–10, all still open. RATIFIED_VOCABULARY !=
RATIFIED_SYSTEM.

## CLERICAL ANOMALY DISPOSITION (Founder-flagged)

The Founder's reviewing channel reported "item 9 appears twice verbatim" in
the ACTIMANIRUN-001 gate report. Mechanical scan of the COMMITTED bytes at
f811d897 (both governed 001 files, full duplicate-numbering scan; §17
enumeration read directly) found NO duplicated numbering — §17 runs cleanly
1..10 and the evidence record's sections are unique. The anomaly therefore
existed only in a conversation-plane copy of the report, not in the governed
record. Per Founder instruction the committed record is NOT rewritten; this
note is the durable disposition. ConversationRendering != GovernedBytes.

## RESULTING LIVE PROJECTION (POST-RATIFICATION)

```yaml
GOVERNANCE-CANDIDATE:ACTIMANIRUN
  institutional_state: SEMANTICS_CLOSED_VOCABULARIES_RATIFIED
  movement_pulse: NO_CURRENT_MOVEMENT_WITNESS   # after this gate's STOP
  hold_context: WAITING_FOUNDER(§17 items 4-10 + 002 authorization)
  attention_state: FOREGROUND
  source_health: DURABLE_LOCAL_CUSTODY (not pushed)
not_marked: IMPLEMENTED · RUNTIME · RATIFIED_SYSTEM · AUTHORIZED_FOR_002
```

## STOP CONDITION

STOP after this ratification record's custody commit. No 002, no
implementation, no adapters, no Footwork, no Notepad, no AgentBridge
mutation, no runtime, no push, no standing projection, no drift repair,
no CodexSELF contact, no departure from ACTIMANIRUN reality.
