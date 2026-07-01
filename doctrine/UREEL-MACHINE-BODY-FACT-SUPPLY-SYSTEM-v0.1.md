# UREEL Machine-Body Fact Supply System v0.1

## 1. Prime thesis

A UREEL candidate body becomes evaluable only when Human_TURN supplies verifiable machine-body facts with evidence. A doctrine packet can name the lane, but only evidence can prove the body.

This doctrine defines the minimum fact and evidence supply required before a named UREEL candidate may enter evaluation.

It does not claim a physical worker machine exists.

It does not evaluate or qualify a candidate.

It does not authorize UNREAL-002 or implementation.

## 2. Reverse-engineered chain

```text
UNREAL-002 Authorization
↓
Candidate Evaluation
↓
Verifiable Machine-Body Facts
↓
Evidence Artifacts
↓
Candidate Fact Packet
↓
Named Candidate Body
↓
OURSELF Sovereign UREEL Candidate Packet
```

The chain is read backward from authorization to the evidence supply required before evaluation can begin.

The sovereign packet names the lane. A named body makes the subject addressable. A complete fact packet organizes claims. Evidence artifacts substantiate those claims. Evaluation judges the resulting evidence. Human_TURN alone decides whether UNREAL-002 may later be authorized.

## 3. Required distinction

- Sovereign packet = intended candidate lane.
- Machine-body facts = observed facts about a real candidate machine.
- Evidence artifacts = proof objects that substantiate the facts.
- Candidate evaluation = comparison against sealed requirements.
- UNREAL-002 authorization = separate Human_TURN decision after evaluation.
- A named packet is not a qualified body.
- A body fact without evidence is an unverified claim.
- A qualified evaluation does not authorize implementation by itself.

These layers must not collapse into each other.

Fact supply is not evaluation. Evaluation is not authorization. Authorization is not implementation unless the authorized incision explicitly says so.

## 4. Machine-body proof categories

The complete machine-body supply system contains six proof categories. Missing required facts must be declared in `missing_facts`; they must not be filled by inference.

### 4.1 Existence Facts

Purpose:

Prove the candidate body exists.

Required facts:

```text
candidate_name:
machine_identifier:
machine_type:
ownership_or_rental_status:
local_or_remote:
physical_or_provider_location:
evidence_available:
```

Acceptable evidence:

- screenshot of system/about page
- invoice/receipt/order page with sensitive data redacted
- provider dashboard screenshot with sensitive data redacted
- local terminal/system report
- photo of physical workstation with no private data exposed

Existence evidence must identify the candidate sufficiently to distinguish it from a generic product listing or desired configuration.

### 4.2 Capability Facts

Purpose:

Prove the candidate body can carry Unreal pressure.

Required facts:

```text
operating_system:
gpu_class:
gpu_vram_if_known:
ram_amount:
cpu_class:
storage_capacity:
storage_type:
available_storage:
```

Minimum floor:

- Windows 11 Pro or later
- RTX-class discrete GPU or equivalent
- 32 GB RAM minimum
- 1 TB NVMe SSD minimum

Acceptable evidence:

- Windows About page
- Device Manager / GPU info screenshot
- Task Manager performance screenshot
- dxdiag output
- system report
- provider spec sheet for the exact instance or plan
- storage screenshot

The minimum floor is a sealed requirement, not an assertion that any current candidate satisfies it.

### 4.3 Access Facts

Purpose:

Prove Human_TURN can access the machine safely.

Required facts:

```text
access_method:
account_owner:
authentication_boundary:
remote_access_tool_if_any:
who_can_access:
access_revocation_path:
```

Acceptable evidence:

- local login confirmation
- remote dashboard screenshot
- access policy screenshot
- provider account page with sensitive data redacted
- written Human_TURN confirmation of accountable access

Access evidence must not expose passwords, recovery codes, tokens, private keys, session cookies, or other credentials.

### 4.4 Isolation Facts

Purpose:

Prove the worker is not contaminating RUORA, Bubble, secrets, or production systems.

Required facts:

```text
unreal_install_location_proposal:
project_location_proposal:
secrets_policy:
git_policy:
production_connection_policy:
bubble_connection_policy:
```

Required boundary values:

```yaml
secrets_policy: NO_PRODUCTION_SECRETS
git_policy: NO_REMOTE_GIT_WRITE_WITHOUT_HUMAN_TURN
production_connection_policy: NO_PRODUCTION_BACKEND_CONNECTION
bubble_connection_policy: NO_BUBBLE_PRODUCTION_CONNECTION
```

Proposed locations remain proposals. They do not authorize directory creation, installation, project creation, access, or connection.

### 4.5 Rollback Facts

Purpose:

Prove the candidate can be cleaned, disconnected, or abandoned.

Required facts:

```text
rollback_path_proposal:
uninstall_path:
artifact_export_path:
account_cancellation_path_if_rented:
data_deletion_path:
cost_stop_path:
```

Required ruling:

No worker is qualified if it cannot be rolled back.

Rollback evidence must identify what would be removed, exported, disconnected, cancelled, deleted, or stopped without performing those actions during fact supply.

### 4.6 Cost / Sovereignty Facts

Purpose:

Preserve the OURSELF open-source-first and no-cost-first doctrine.

Required facts:

```text
cost_status:
billing_boundary_if_rented:
open_source_preference_checked:
no_cost_first_checked:
self_owned_or_self_governed_status:
exception_needed:
```

Required law:

Paid, closed, rented, or externally governed infrastructure requires explicit Human_TURN exception authorization.

Cost and sovereignty evidence must reveal recurring charges, cancellation constraints, external control, lock-in, and any exception required before the candidate can be governed honestly.

## 5. Complete candidate fact packet

The following packet is the required input before evaluation:

```text
candidate_name:
candidate_source:
candidate_class:
machine_identifier:
machine_type:
ownership_or_rental_status:
local_or_remote:
physical_or_provider_location:
operating_system:
gpu_class:
gpu_vram_if_known:
ram_amount:
cpu_class:
storage_capacity:
storage_type:
available_storage:
access_method:
account_owner:
authentication_boundary:
remote_access_tool_if_any:
who_can_access:
access_revocation_path:
unreal_install_location_proposal:
project_location_proposal:
secrets_policy:
git_policy:
production_connection_policy:
bubble_connection_policy:
rollback_path_proposal:
uninstall_path:
artifact_export_path:
account_cancellation_path_if_rented:
data_deletion_path:
cost_stop_path:
cost_status:
billing_boundary_if_rented:
open_source_preference_checked:
no_cost_first_checked:
self_owned_or_self_governed_status:
exception_needed:
evidence_artifacts:
missing_facts:
human_turn_confirmation:
```

The template is intentionally empty. This doctrine does not populate it for `UREEL-OURSELFCLOUD-NODE-0` or any other candidate.

Each supplied fact must identify its evidence source or its explicit Human_TURN attestation. Unknown values must remain unknown and appear in `missing_facts`.

## 6. Evidence classification

Evidence must be classified at one of these levels:

### LEVEL 0 — CLAIM_ONLY

A fact is asserted without an attached artifact or explicit Human_TURN attestation.

### LEVEL 1 — HUMAN_TURN_ATTESTED

Human_TURN explicitly attests to the fact, but no independent screenshot, document, or system report is attached.

### LEVEL 2 — SCREENSHOT_OR_DOCUMENT_PROOF

A relevant screenshot, redacted document, exact-plan specification, or equivalent visual record substantiates the fact.

### LEVEL 3 — SYSTEM_REPORT_PROOF

A machine-generated system report, diagnostic output, or equivalent direct technical record substantiates the fact.

### LEVEL 4 — MULTI_ARTIFACT_CONFIRMED

Multiple consistent artifacts across existence, capability, access, isolation, rollback, or cost boundaries substantiate the candidate packet.

Evaluation rule:

- LEVEL 0 cannot qualify a candidate.
- LEVEL 1 may support conditional evaluation only.
- LEVEL 2 may support conditional or qualified evaluation depending on completeness.
- LEVEL 3 may support qualified evaluation if all governance boundaries pass.
- LEVEL 4 is preferred for high-confidence qualification.

Evidence level does not override a failed capability floor or governance boundary.

## 7. Supply flow

1. Human_TURN names candidate.
2. Human_TURN supplies machine-body packet.
3. Human_TURN supplies evidence artifacts or explicit attestation.
4. Codex checks completeness.
5. Codex identifies missing facts.
6. Codex assigns evidence level.
7. Codex prepares candidate evaluation doctrine.
8. Evaluation may return QUALIFIED, CONDITIONALLY_QUALIFIED, or REJECTED.
9. UNREAL-002 remains blocked until separate Human_TURN authorization.

Preparing candidate evaluation doctrine is a separate pass. This fact-supply doctrine does not perform that evaluation.

## 8. No-invention law

Codex may request, organize, and evaluate machine-body facts, but Codex may not invent them.

Codex must preserve unknown fields, identify conflicting artifacts, distinguish requirements from observations, and state when evidence is insufficient.

No product specification, provider description, doctrine baseline, desired configuration, or candidate name may be represented as an observed machine fact without matching evidence.

## 9. Evidence law

A machine-body fact is not verifiable until it is attached to an evidence artifact or explicit Human_TURN attestation.

Evidence must be attributable to the named candidate, relevant to the asserted fact, legible enough to inspect, and redacted so that credentials and unnecessary private data are not exposed.

An artifact may support a fact without authorizing any action on the machine.

## 10. No-implementation law

Supplying machine-body facts does not authorize Unreal installation, project creation, remote access setup, hardware purchase, UWebBrowser implementation, Pixel Streaming, deployment, Git write access, secret transfer, or worker execution.

It also does not authorize cloud provisioning, account creation, package installation, API calls, Bubble mutation, schema mutation, application implementation, remote creation, push, worktree creation, agent creation, or PR creation.

Fact collection must remain read-only unless Human_TURN separately authorizes a specific, bounded evidence-generation action.

## 11. Candidate-body law

UREEL-OURSELFCLOUD-NODE-0 remains body-pending until verifiable machine-body facts are supplied.

The candidate name is a sovereign packet handle. It does not prove a device, instance, provider account, operating system, capability, access path, or storage path exists.

Another candidate may enter the same system only when Human_TURN names it and supplies its own attributable facts and evidence.

## 12. Privacy and redaction boundary

Evidence artifacts must exclude or redact:

- passwords and password hints
- authentication tokens and session cookies
- private keys and recovery codes
- payment card or bank details
- service-role or API keys
- home addresses or unnecessary precise location data
- personal account identifiers not required for candidate attribution

Redaction must not conceal the technical fact being offered as evidence.

No evidence artifact should be added to the repo without separate authorization defining its retention and sensitivity boundary.

## 13. Relationship to sealed doctrine

This fact-supply system inherits from:

- OURSELF Sovereign UREEL Candidate Packet sealed at `af30f1f`
- UREEL Candidate Machine System sealed at `ff4802d`
- UREEL Worker Candidate Absence sealed at `454207c`
- UREEL Worker Candidate Requirements sealed at `a3fecbf`
- UREEL Machine Identity facts sealed at `a2a1058`
- UREEL Worker Machine Identity sealed at `00ada55`
- UNREAL-002 hold recorded at `ce0cfb7`
- UNREAL-002 authorization brief sealed at `3134de2`

These seals remain governing.

This doctrine adds an evidence intake boundary. It does not replace the sovereign packet, candidate requirements, absence ruling, evaluation system, or authorization gate.

## 14. Current state

- Sovereign candidate lane: defined.
- Named packet: `UREEL-OURSELFCLOUD-NODE-0`.
- Physical or remote candidate body: pending.
- Machine-body facts: not supplied.
- Evidence artifacts: not supplied.
- Candidate evaluation: not performed.
- Candidate qualification: not assigned.
- Evaluation status: `BLOCKED_NO_CANDIDATE`.
- UNREAL-002 status: `MANUAL_REQUIRED`.
- Implementation status: `NOT_AUTHORIZED`.

These state lines preserve sealed absence. They do not report newly observed machine facts.

## 15. Launch boundary

- This is not product launch.
- This is not public deployment.
- This is not a service launch.
- This is not Pixel Streaming.
- This is not a cloud build.
- This is not remote execution.
- This is machine-body fact supply doctrine only.

The body remains unproven.

Evaluation remains blocked.

UNREAL-002 remains closed.

Implementation remains unauthorized.

## 16. Next gate

The next valid input is a Human_TURN-supplied, attributable, redacted machine-body fact packet with evidence for `UREEL-OURSELFCLOUD-NODE-0` or another named candidate.

Until that input exists:

- no body existence may be claimed
- no missing fact may be invented
- no evidence level above LEVEL 0 may be assigned
- no candidate evaluation may be performed
- no qualification may be claimed
- no UNREAL-002 authorization may be inferred
- no implementation may begin
