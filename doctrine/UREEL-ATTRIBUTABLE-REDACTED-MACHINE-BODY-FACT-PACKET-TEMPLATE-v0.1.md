# UREEL Attributable Redacted Machine-Body Fact Packet Template v0.1

## 1. Prime thesis

An attributable, redacted machine-body fact packet is the bridge between a named UREEL candidate and candidate evaluation. It must identify who supplied the facts, what machine body is being claimed, which evidence supports each claim, what has been redacted, and what remains missing.

This template defines how Human_TURN may package a future evidence submission for `UREEL-OURSELFCLOUD-NODE-0` or another named candidate.

It supplies no actual machine facts or evidence artifacts.

It does not claim a physical or remote worker body exists.

It does not evaluate or qualify a candidate.

It does not authorize UNREAL-002 or implementation.

## 2. Reverse-engineered chain

```text
Candidate Evaluation
↓ requires
Complete Machine-Body Fact Packet
↓ requires
Attributable Fact Claims
↓ requires
Redacted Evidence Artifacts
↓ requires
Human_TURN Confirmation
↓ names
UREEL Candidate Body
```

Evaluation requires facts. Facts require evidence. Evidence requires attribution. Attribution requires Human_TURN. Redaction protects the proof chain.

## 3. Definitions

- Attributable = every fact identifies its source: Human_TURN attestation, screenshot, system report, provider document, local terminal output, or other named artifact.
- Redacted = evidence removes secrets and unnecessary private data while preserving the technical fact being proved.
- Machine-body fact = an observed or attested fact about a real physical or remote candidate machine.
- Evidence artifact = the object that supports a fact.
- Missing fact = a required field not yet supported by evidence or attestation.
- Candidate body = the actual physical or remote machine proposed to carry UREEL.
- Fact packet = structured evidence intake, not evaluation.
- Evaluation = later comparison against sealed requirements.

The definitions establish intake semantics. They do not assert that any candidate fact or evidence artifact currently exists.

## 4. No-collapse law

Fact packet is not evaluation. Evidence is not authorization. Redaction is not erasure of proof. Attribution is not qualification.

Intake may determine whether a packet is ready to enter evaluation. Intake cannot assign `QUALIFIED`, `CONDITIONALLY_QUALIFIED`, or `REJECTED` as a candidate outcome.

## Attribution Standard

Every supplied fact must include:

```yaml
field:
value:
source_type:
source_name:
evidence_level:
redaction_status:
notes:
```

Allowed `source_type` values:

- `HUMAN_TURN_ATTESTATION`
- `SCREENSHOT`
- `SYSTEM_REPORT`
- `PROVIDER_DOCUMENT`
- `LOCAL_TERMINAL_OUTPUT`
- `PHOTO`
- `INVOICE_OR_RECEIPT`
- `DASHBOARD_EXPORT`
- `OTHER_EXPLAINED_SOURCE`

`source_name` must identify the attestation or artifact without embedding a secret, credential, unnecessary private identifier, or unsafe storage path.

`OTHER_EXPLAINED_SOURCE` requires a plain-language explanation in `notes` and remains subject to evidence-level review.

## Redaction Standard

Evidence must redact or exclude:

- passwords
- password hints
- tokens
- session cookies
- private keys
- recovery codes
- payment card numbers
- bank details
- full home address
- unnecessary precise location data
- API keys
- service-role keys
- deployment keys
- cloud credentials
- personal account identifiers not needed for candidate attribution

Redaction must preserve the technical fact being offered as evidence.

Redaction status must be explicit for every fact and artifact. Evidence that cannot be reviewed safely must not be attached to the packet or repo.

## 7. Packet shell

The following YAML is the exact intake shell. Empty values are unresolved. Doctrine identifiers and boundary values do not represent observed machine facts.

```yaml
packet_id: UREEL-MACHINE-BODY-FACT-PACKET-0001
packet_status: DRAFT_BODY_FACTS_PENDING
candidate_name: UREEL-OURSELFCLOUD-NODE-0
candidate_source: HUMAN_TURN_SUPPLIED
candidate_class: SOVEREIGN_WORKER_NODE_CANDIDATE
prepared_by: HUMAN_TURN
prepared_for: RUORA_CANDIDATE_EVALUATION
created_date:
redaction_status: REQUIRED_BEFORE_REVIEW
overall_evidence_level: UNASSIGNED
evaluation_status: NOT_EVALUATED
unreal_002_status: MANUAL_REQUIRED
implementation_status: NOT_AUTHORIZED
existence_facts:
  candidate_name:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  machine_identifier:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  machine_type:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  ownership_or_rental_status:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  local_or_remote:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  physical_or_provider_location:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
capability_facts:
  operating_system:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  gpu_class:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  gpu_vram_if_known:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  ram_amount:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  cpu_class:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  storage_capacity:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  storage_type:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  available_storage:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
access_facts:
  access_method:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  account_owner:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  authentication_boundary:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  remote_access_tool_if_any:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  who_can_access:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  access_revocation_path:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
isolation_facts:
  unreal_install_location_proposal:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  project_location_proposal:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  secrets_policy:
    value: NO_PRODUCTION_SECRETS
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  git_policy:
    value: NO_REMOTE_GIT_WRITE_WITHOUT_HUMAN_TURN
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  production_connection_policy:
    value: NO_PRODUCTION_BACKEND_CONNECTION
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  bubble_connection_policy:
    value: NO_BUBBLE_PRODUCTION_CONNECTION
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
rollback_facts:
  rollback_path_proposal:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  uninstall_path:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  artifact_export_path:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  account_cancellation_path_if_rented:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  data_deletion_path:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  cost_stop_path:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
cost_sovereignty_facts:
  cost_status:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  billing_boundary_if_rented:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  open_source_preference_checked:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  no_cost_first_checked:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  self_owned_or_self_governed_status:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
  exception_needed:
    value:
    source_type:
    source_name:
    evidence_level:
    redaction_status:
    notes:
evidence_artifacts:
  - artifact_id:
    artifact_type:
    artifact_description:
    supports_fields:
    redaction_applied:
    sensitive_data_removed:
    storage_location:
    retention_boundary:
    notes:
missing_facts:
  - field:
    reason_missing:
    required_before_evaluation:
human_turn_confirmation:
  supplied_by:
  confirmation_text:
  confirmation_date:
```

The shell is not a completed fact packet. Its identifiers define the intended intake object; its blank values remain missing facts.

The four populated isolation-policy values are required governance boundaries. They are not evidence that a machine currently enforces those policies.

## 8. Artifact naming standard

Evidence artifacts should be named without secrets:

```text
UREEL-EVIDENCE-0001-EXISTENCE-REDACTED
UREEL-EVIDENCE-0002-CAPABILITY-REDACTED
UREEL-EVIDENCE-0003-ACCESS-REDACTED
UREEL-EVIDENCE-0004-ISOLATION-REDACTED
UREEL-EVIDENCE-0005-ROLLBACK-REDACTED
UREEL-EVIDENCE-0006-COST-SOVEREIGNTY-REDACTED
```

An artifact name is a safe label, not evidence that the artifact exists or satisfies its category.

Extensions, storage locations, retention terms, and access controls must be supplied separately and must not expose secrets.

## 9. Evidence-level rule

- LEVEL 0 is claim-only and cannot qualify.
- LEVEL 1 requires explicit Human_TURN attestation.
- LEVEL 2 requires screenshot/document proof.
- LEVEL 3 requires system-report proof.
- LEVEL 4 requires multi-artifact confirmation.

Evidence level is assigned per fact and summarized for the packet only after intake review. A high evidence level cannot cure a failed requirement or unsafe governance boundary.

## 10. Intake outcomes

Packet intake may assign exactly one readiness outcome:

### INTAKE_READY_FOR_EVALUATION

All required facts are attributable, safely redacted, and sufficiently evidenced for a separate candidate evaluation pass.

### INTAKE_CONDITIONALLY_READY_MISSING_NONCRITICAL_FACTS

Required evaluation facts are present, while declared noncritical facts remain missing and must be carried into evaluation as conditions.

### INTAKE_BLOCKED_MISSING_REQUIRED_FACTS

One or more required facts lack a value, attribution, acceptable evidence, or safe redaction.

### INTAKE_REJECTED_UNSAFE_OR_UNATTRIBUTABLE

The packet exposes unsafe data, cannot attribute material claims, conflicts with Human_TURN confirmation, or cannot preserve the proof boundary.

An intake outcome is not a candidate qualification outcome.

## 11. No-implementation law

A completed attributable redacted machine-body fact packet does not authorize Unreal installation, project creation, remote access setup, hardware purchase, UWebBrowser implementation, Pixel Streaming, deployment, Git write access, secret transfer, or worker execution.

It also does not authorize cloud provisioning, account creation, package installation, API calls, Bubble mutation, schema mutation, application implementation, remote creation, push, worktree creation, agent creation, or PR creation.

## 12. Candidate-body law

UREEL-OURSELFCLOUD-NODE-0 remains body-pending until this packet is populated with attributable, redacted evidence.

The packet shell does not prove a device, instance, provider plan, ownership state, access route, capability, storage path, rollback path, or billing boundary exists.

## 13. Evaluation law

Packet intake may determine readiness for evaluation; it does not determine candidate qualification.

Candidate evaluation must occur in a separate doctrine pass against the sealed requirements and may not be inferred from packet completeness.

UNREAL-002 remains `MANUAL_REQUIRED` after intake and after evaluation until Human_TURN explicitly authorizes implementation.

## 14. Human_TURN confirmation law

Human_TURN confirmation must identify the supplier, state that the submitted facts and artifacts correspond to the named candidate, state that required redaction has been applied, and provide a confirmation date.

An empty confirmation block leaves intake blocked.

Codex may organize and inspect supplied claims, but it may not manufacture confirmation text or impersonate Human_TURN.

## 15. Evidence storage boundary

This template does not attach or authorize storage of any evidence artifact.

Before a real artifact enters the repo, Human_TURN must separately authorize its storage location, retention boundary, redaction status, and sensitivity handling.

Evidence should remain outside Git when safe retention cannot be guaranteed.

## 16. Relationship to sealed doctrine

This template inherits from:

- UREEL Machine-Body Fact Supply System sealed at `275b973`
- OURSELF Sovereign UREEL Candidate Packet sealed at `af30f1f`
- UREEL Candidate Machine System sealed at `ff4802d`
- UREEL Worker Candidate Absence sealed at `454207c`
- UREEL Worker Candidate Requirements sealed at `a3fecbf`
- UNREAL-002 hold recorded at `ce0cfb7`
- UNREAL-002 authorization brief sealed at `3134de2`

These seals remain governing.

The template adds structure for a future submission. It does not replace fact-supply, evaluation, absence, or authorization doctrine.

## 17. Current state

- Packet template: defined by this capture.
- Actual fact packet: not supplied.
- Physical or remote candidate body: unproven.
- Evidence artifacts: not attached.
- Overall evidence level: unassigned.
- Intake outcome: not assigned.
- Candidate evaluation: not performed.
- Candidate qualification: not assigned.
- UNREAL-002 status: `MANUAL_REQUIRED`.
- Implementation status: `NOT_AUTHORIZED`.

These state lines preserve the sealed boundary and do not report new machine facts.

## 18. Launch boundary

- This is not product launch.
- This is not public deployment.
- This is not a service launch.
- This is not Pixel Streaming.
- This is not a cloud build.
- This is not remote execution.
- This is attributable redacted machine-body fact packet template doctrine only.

## 19. Next gate

The next valid input is a separately supplied copy of this shell populated by Human_TURN with attributable, redacted claims and authorized evidence references.

Until then:

- no machine body may be claimed
- no artifact may be treated as attached
- no intake outcome may be assigned
- no candidate evaluation may be performed
- no qualification may be claimed
- no UNREAL-002 authorization may be inferred
- no implementation may begin
