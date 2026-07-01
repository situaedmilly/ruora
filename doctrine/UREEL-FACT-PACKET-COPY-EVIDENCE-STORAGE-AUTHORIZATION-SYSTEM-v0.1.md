# UREEL Fact Packet Copy + Evidence Storage Authorization System v0.1

## 1. Prime thesis

A populated UREEL fact packet copy and the evidence artifacts it references are two separate gates. Human_TURN may populate claims in a packet copy, but OURSELF must separately authorize evidence storage, retention, redaction, and sensitivity boundaries before artifacts enter review.

This doctrine captures the two-gate system. It does not populate an actual packet, attach evidence, claim a physical worker machine exists, evaluate or qualify a candidate, authorize UNREAL-002, or authorize implementation.

## 2. Reverse-engineered chain

```text
Candidate Evaluation
↓ requires
Intake-Ready Packet
↓ requires
Populated Fact Packet Copy
↓ references
Evidence Artifacts
↓ require
Evidence Storage / Retention Authorization
↓ requires
OURSELF / Human_TURN Redaction Boundary
↓ protects
RUORA Proof Body
```

The chain separates claims from artifacts and separates artifact handling from intake and evaluation.

## Gate 1 — Populated Packet Copy

- A packet copy is a separate file or submission based on the sealed template.
- It may contain Human_TURN-supplied claims.
- It may reference evidence labels.
- It must preserve attribution.
- It must preserve redaction status.
- It must identify missing facts.
- It must not attach evidence by itself unless storage has been separately authorized.
- It must not assign candidate qualification.
- It must not authorize UNREAL-002.

A populated packet copy may contain claims, but claims remain intake material until evidence level and redaction status are reviewed.

## Gate 2 — Evidence Storage / Retention Authorization

- Evidence storage authorization decides whether artifacts may enter repo, remain outside Git, or be reviewed transiently.
- Evidence storage authorization must define retention period.
- Evidence storage authorization must define sensitivity level.
- Evidence storage authorization must confirm redaction.
- Evidence storage authorization must define storage location.
- Evidence storage authorization must define who may inspect.
- Evidence storage authorization must define deletion/removal path.
- Evidence storage authorization must not evaluate candidate qualification.
- Evidence storage authorization must not authorize UNREAL-002.

No evidence artifact may enter the repo until OURSELF / Human_TURN authorizes its storage location, retention boundary, redaction status, sensitivity class, and deletion path.

## 5. Allowed future paths

The populated packet copy and evidence-intake documentation may later use one of these governed paths:

```text
doctrine/intake/UREEL-MACHINE-BODY-FACT-PACKET-0001-DRAFT.md
doctrine/intake/UREEL-MACHINE-BODY-FACT-PACKET-0001-DRAFT.yaml
evidence/ureel/intake/README.md
```

This doctrine does not create those paths.

## 6. Evidence reference law

An evidence reference is not an attached artifact. A label such as UREEL-EVIDENCE-0001-EXISTENCE-REDACTED is only a pointer until the artifact is supplied under an authorized storage boundary.

## 7. No-secret law

Evidence storage must never preserve passwords, tokens, session cookies, private keys, recovery codes, service-role keys, API keys, deployment keys, payment card data, bank data, or unnecessary personal location data.

## 8. Storage classes

- `STORAGE_CLASS_A` — Repo-safe redacted text artifact.
- `STORAGE_CLASS_B` — Repo-safe redacted screenshot reference.
- `STORAGE_CLASS_C` — External-only sensitive artifact.
- `STORAGE_CLASS_D` — Transient review only.
- `STORAGE_CLASS_E` — Rejected unsafe artifact.

Rules:

- STORAGE_CLASS_A may enter repo only if redacted and low sensitivity.
- STORAGE_CLASS_B may enter repo only if screenshot is redacted, low sensitivity, and Human_TURN explicitly authorizes.
- STORAGE_CLASS_C must remain outside Git.
- STORAGE_CLASS_D may be reviewed but not stored.
- STORAGE_CLASS_E must not be reviewed or stored until remediated.

## 9. Retention classes

- `RETENTION_NONE`
- `RETENTION_SESSION_ONLY`
- `RETENTION_UNTIL_EVALUATION`
- `RETENTION_UNTIL_REPLACED`
- `RETENTION_CANONICAL_PROOF`

Rules:

- Sensitive artifacts default to RETENTION_SESSION_ONLY or external-only.
- Repo artifacts require explicit RETENTION_CANONICAL_PROOF or RETENTION_UNTIL_REPLACED.
- No retention class authorizes implementation.

## 10. Sensitivity classes

- `SENSITIVITY_LOW`
- `SENSITIVITY_MEDIUM`
- `SENSITIVITY_HIGH`
- `SENSITIVITY_REJECTED_SECRET`

Rules:

- SENSITIVITY_REJECTED_SECRET cannot enter repo.
- SENSITIVITY_HIGH should remain external or transient unless separately justified.
- SENSITIVITY_LOW may be repo-safe only after redaction.
- Sensitivity classification is not candidate qualification.

## 11. Evidence authorization packet

The following YAML is the evidence storage authorization shell. Empty authorization fields remain unresolved and do not authorize storage or review.

```yaml
evidence_authorization_id: UREEL-EVIDENCE-STORAGE-AUTH-0001
authorization_status: DRAFT_NOT_AUTHORIZED
authorized_by: HUMAN_TURN_REQUIRED
candidate_name: UREEL-OURSELFCLOUD-NODE-0
packet_id: UREEL-MACHINE-BODY-FACT-PACKET-0001
storage_decision:
  storage_class:
  retention_class:
  sensitivity_class:
  storage_location:
  allowed_artifact_types:
  redaction_required:
  redaction_confirmed:
  secrets_excluded:
  who_may_inspect:
  deletion_or_removal_path:
  external_storage_if_any:
  repo_storage_allowed:
  notes:
artifact_authorizations:
  - artifact_id: UREEL-EVIDENCE-0001-EXISTENCE-REDACTED
    artifact_category: EXISTENCE
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
  - artifact_id: UREEL-EVIDENCE-0002-CAPABILITY-REDACTED
    artifact_category: CAPABILITY
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
  - artifact_id: UREEL-EVIDENCE-0003-ACCESS-REDACTED
    artifact_category: ACCESS
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
  - artifact_id: UREEL-EVIDENCE-0004-ISOLATION-REDACTED
    artifact_category: ISOLATION
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
  - artifact_id: UREEL-EVIDENCE-0005-ROLLBACK-REDACTED
    artifact_category: ROLLBACK
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
  - artifact_id: UREEL-EVIDENCE-0006-COST-SOVEREIGNTY-REDACTED
    artifact_category: COST_SOVEREIGNTY
    storage_class:
    retention_class:
    sensitivity_class:
    authorized_for_repo:
    authorized_for_external_reference:
    authorized_for_transient_review:
    redaction_confirmed:
    notes:
human_turn_confirmation:
  supplied_by:
  confirmation_text:
  confirmation_date:
```

The shell records authorization structure only. `DRAFT_NOT_AUTHORIZED`, `HUMAN_TURN_REQUIRED`, and every empty field preserve the closed evidence-storage gate.

## 12. Intake sequencing

1. Human_TURN names candidate.
2. Human_TURN populates separate packet copy.
3. Human_TURN identifies evidence references.
4. OURSELF / Human_TURN authorizes evidence storage/retention.
5. Evidence is supplied under authorized storage boundary.
6. Codex performs intake review.
7. Intake assigns readiness outcome.
8. Candidate evaluation occurs only in a separate pass if intake permits it.
9. UNREAL-002 remains blocked until separate Human_TURN authorization.

The sequence describes future governed intake. No step is performed by this doctrine capture.

## 13. No-collapse law

Packet copy is not evidence storage authorization. Evidence storage authorization is not intake review. Intake review is not candidate evaluation. Candidate evaluation is not UNREAL-002 authorization.

## 14. No-implementation law

Neither a populated packet copy nor evidence storage authorization permits Unreal installation, project creation, remote access setup, hardware purchase, UWebBrowser implementation, Pixel Streaming, deployment, Git write access, secret transfer, or worker execution.

It also does not authorize cloud provisioning, account creation, package installation, API calls, Bubble mutation, schema mutation, application implementation, remote creation, push, worktree creation, agent creation, or PR creation.

## 15. Current state

- Packet template is sealed at `c6182bd`.
- Fact-supply system is sealed at `275b973`.
- Sovereign packet is sealed at `af30f1f`.
- Current candidate body remains unproven.
- Current packet copy is not supplied.
- Current evidence storage authorization is not supplied.
- Current evidence artifacts are not attached.
- Current intake review is not performed.
- Current candidate evaluation is not performed.
- UNREAL-002 remains `MANUAL_REQUIRED`.
- Implementation remains `NOT_AUTHORIZED`.

These state lines preserve the current sealed boundary. They do not report new candidate facts, artifacts, intake, evaluation, or implementation.

## 16. Launch boundary

- This is not product launch.
- This is not public deployment.
- This is not a service launch.
- This is not Pixel Streaming.
- This is not a cloud build.
- This is not remote execution.
- This is fact packet copy and evidence storage authorization system doctrine only.

## 17. Clean law

Claims go in packet copy.

Artifacts require storage authorization.

Intake reviews readiness.

Evaluation judges candidate.

UNREAL-002 still waits.
