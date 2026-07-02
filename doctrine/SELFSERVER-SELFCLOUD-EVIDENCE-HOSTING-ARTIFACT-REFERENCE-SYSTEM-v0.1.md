# SELFSERVER / SELFCLOUD Evidence Hosting + Artifact Reference System v0.1

## 1. Prime thesis

OUR SELFSERVER is the governed infrastructure body; OURSELFCLOUD is the evidence-storage layer operating on that body. RUORA is the proof index. Evidence artifacts may live in OURSELFCLOUD, but RUORA stores only redacted references, artifact IDs, authorization status, field mappings, and review outcomes unless Human_TURN separately authorizes repo-safe artifact storage.

This doctrine captures evidence-hosting architecture only. It does not configure a SELFSERVER body, configure OURSELFCLOUD, create storage, attach evidence, populate a fact packet, perform intake review, evaluate a candidate, authorize UNREAL-002, or authorize implementation.

## 2. Reverse-engineered chain

```text
Candidate Fact
↓ requires
Evidence Reference
↓ points to
OURSELFCLOUD Artifact
↓ hosted on
OUR SELFSERVER
↓ governed by
Storage / Retention Authorization
↓ indexed by
RUORA Proof Reference
↓ reviewed through
Intake Review
↓ enables
Candidate Evaluation
```

The chain preserves the difference between infrastructure body, evidence vault, proof reference, review, evaluation, and authorization.

## Architecture Distinction

- OUR SELFSERVER = sovereign infrastructure body.
- OURSELFCLOUD = governed evidence/storage layer operating on OUR SELFSERVER.
- RUORA = doctrine, proof index, review memory, and canonical decision record.
- Codex = organizer/reviewer of authorized references, not owner of artifacts.
- Human_TURN = authority that supplies facts, authorizes storage, and confirms references.
- Artifact ID = stable evidence label used in packet and review records.
- OURSELFCLOUD URI = redacted or abstracted pointer to evidence location.
- Storage authorization = permission boundary for what may be stored, where, how long, and who may inspect.
- Review outcome = intake/evaluation result stored in RUORA after authorized review.

## 4. No-collapse law

OURSELFCLOUD hosting is not evidence review. Evidence review is not candidate evaluation. Candidate evaluation is not UNREAL-002 authorization. UNREAL-002 authorization is not implementation.

Infrastructure control does not authorize artifact storage. Artifact storage does not prove a claim. A proof reference does not attach an artifact. Intake readiness does not qualify a candidate.

## 5. Hosting law

Evidence may be hosted in OURSELFCLOUD on OUR SELFSERVER only under explicit Human_TURN / OURSELF storage authorization that defines artifact ID, storage class, retention class, sensitivity class, redaction status, inspection boundary, and deletion path.

OURSELFCLOUD-hosted evidence is not automatically proof. An artifact becomes reviewable only when it is redacted, has an artifact ID, has storage authorization, maps to packet fields, and Human_TURN confirms the reference.

## 6. RUORA index law

RUORA should store evidence indexes, field mappings, hashes or checksums if safe, redaction status, authorization status, and review outcomes; RUORA should not store raw sensitive artifacts unless separately authorized as repo-safe.

RUORA records the governed proof reference and decision memory. It does not become the default artifact vault.

## 7. No-secret law

OURSELFCLOUD evidence governance must reject passwords, tokens, session cookies, private keys, recovery codes, service-role keys, API keys, deployment keys, payment card data, bank data, and unnecessary personal location data from both RUORA and reviewable artifact views.

Redaction must preserve the technical fact needed for review while removing secret and unnecessary sensitive material. A rejected secret cannot be converted into acceptable evidence merely by indexing its location.

## 8. Evidence reference schema

The following YAML is a reference shell only. Empty fields remain unresolved and do not authorize storage, review, evaluation, UNREAL-002, or implementation.

```yaml
selfcloud_evidence_reference_id: UREEL-SELFCLOUD-EVIDENCE-REF-0001
reference_status: DRAFT_NOT_REVIEWED
candidate_name: UREEL-OURSELFCLOUD-NODE-0
packet_id: UREEL-MACHINE-BODY-FACT-PACKET-0001
artifact_id: UREEL-EVIDENCE-0001-EXISTENCE-REDACTED
artifact_category: EXISTENCE
selfserver_body:
  server_identifier_redacted:
  ownership_or_control_status:
  physical_or_provider_location_redacted:
  access_boundary:
selfcloud_location:
  uri_redacted:
  vault_name:
  folder_or_collection:
  object_name_redacted:
  access_method:
  external_reference_only:
storage_governance:
  storage_class:
  retention_class:
  sensitivity_class:
  redaction_status:
  redaction_confirmed_by:
  secrets_excluded:
  who_may_inspect:
  deletion_or_removal_path:
  repo_storage_allowed:
  transient_review_allowed:
technical_integrity:
  checksum_available:
  checksum_type:
  checksum_value_redacted_or_safe:
  artifact_version:
  captured_date:
  last_verified_date:
field_mapping:
  supports_packet_fields:
    - field:
      claim_value:
      evidence_level:
      notes:
review_state:
  intake_review_status: NOT_REVIEWED
  candidate_evaluation_status: NOT_EVALUATED
  unreal_002_status: MANUAL_REQUIRED
  implementation_status: NOT_AUTHORIZED
human_turn_confirmation:
  supplied_by:
  confirmation_text:
  confirmation_date:
```

`DRAFT_NOT_REVIEWED`, the empty governance fields, and the closed review-state values preserve every downstream gate.

## 9. Artifact category map

| Artifact ID | Category | Packet fact domain |
| --- | --- | --- |
| `UREEL-EVIDENCE-0001-EXISTENCE-REDACTED` | `EXISTENCE` | existence facts |
| `UREEL-EVIDENCE-0002-CAPABILITY-REDACTED` | `CAPABILITY` | capability facts |
| `UREEL-EVIDENCE-0003-ACCESS-REDACTED` | `ACCESS` | access facts |
| `UREEL-EVIDENCE-0004-ISOLATION-REDACTED` | `ISOLATION` | isolation facts |
| `UREEL-EVIDENCE-0005-ROLLBACK-REDACTED` | `ROLLBACK` | rollback facts |
| `UREEL-EVIDENCE-0006-COST-SOVEREIGNTY-REDACTED` | `COST_SOVEREIGNTY` | cost / sovereignty facts |

The standard mapping is:

- 0001 → existence facts
- 0002 → capability facts
- 0003 → access facts
- 0004 → isolation facts
- 0005 → rollback facts
- 0006 → cost / sovereignty facts

An artifact ID is a stable label, not evidence attachment, review approval, candidate qualification, or implementation authority.

## 10. OURSELFCLOUD storage classes

- STORAGE_CLASS_A — Repo-safe redacted text artifact
- STORAGE_CLASS_B — Repo-safe redacted screenshot reference
- STORAGE_CLASS_C — OURSELFCLOUD-only sensitive artifact
- STORAGE_CLASS_D — Transient OURSELFCLOUD review only
- STORAGE_CLASS_E — Rejected unsafe artifact

Rules:

- STORAGE_CLASS_A may be indexed in RUORA and may enter repo only if separately authorized as repo-safe.
- STORAGE_CLASS_B may be indexed in RUORA but the screenshot itself should stay in OURSELFCLOUD unless explicitly authorized.
- STORAGE_CLASS_C remains OURSELFCLOUD-only and must not enter Git.
- STORAGE_CLASS_D may be viewed under transient review and must not be retained beyond its retention boundary.
- STORAGE_CLASS_E must not be reviewed, stored, indexed, or used until remediated.

No storage class by itself authorizes retention, inspection, intake, evaluation, UNREAL-002, or implementation.

## 11. OURSELFCLOUD folder logic

The following paths record future folder logic only:

```text
OURSELFCLOUD/UREEL/INTAKE/0001_EXISTENCE/
OURSELFCLOUD/UREEL/INTAKE/0002_CAPABILITY/
OURSELFCLOUD/UREEL/INTAKE/0003_ACCESS/
OURSELFCLOUD/UREEL/INTAKE/0004_ISOLATION/
OURSELFCLOUD/UREEL/INTAKE/0005_ROLLBACK/
OURSELFCLOUD/UREEL/INTAKE/0006_COST_SOVEREIGNTY/
```

This doctrine does not create SELFSERVER folders, OURSELFCLOUD folders, buckets, objects, credentials, or permissions.

Path notation is architecture, not proof that a storage path, bucket, object, server, or access boundary exists.

## 12. Review sequence

1. Human_TURN supplies candidate facts.
2. Human_TURN authorizes OURSELFCLOUD evidence storage on OUR SELFSERVER.
3. Evidence artifacts are redacted before review.
4. Evidence artifacts are placed in OURSELFCLOUD under authorized boundary.
5. RUORA records only artifact references and field mappings unless repo-safe storage is separately authorized.
6. Codex performs intake review against references and permitted views.
7. Intake determines readiness outcome.
8. Candidate evaluation occurs only after intake permits it.
9. UNREAL-002 remains blocked until Human_TURN separately authorizes it.

The sequence is fail-closed. A missing authorization, attribution, redaction confirmation, field mapping, or Human_TURN confirmation blocks review rather than permitting inference.

## 13. Current sealed state

- Codex Skill Inventory Operational Context sealed at `1d3a8d4`.
- UREEL Fact Packet Copy + Evidence Storage Authorization System sealed at `acccc6b`.
- UREEL Attributable Redacted Machine-Body Fact Packet Template sealed at `c6182bd`.
- UREEL Machine-Body Fact Supply System sealed at `275b973`.
- SELFSERVER / OURSELFCLOUD evidence hosting doctrine is being captured as architecture only.
- No SELFSERVER body is configured.
- No OURSELFCLOUD artifact is created.
- No OURSELFCLOUD folder is created.
- No OURSELFCLOUD credential is created.
- No evidence artifact is attached.
- No populated packet copy is created.
- No intake review is performed.
- No candidate evaluation is performed.
- UNREAL-002 remains `MANUAL_REQUIRED`.
- Implementation remains `NOT_AUTHORIZED`.

This current state records architecture and closed gates only. It does not declare candidate facts or establish that a SELFSERVER or OURSELFCLOUD storage surface exists.

## 14. Launch boundary

- This is not product launch.
- This is not public deployment.
- This is not a service launch.
- This is not Pixel Streaming.
- This is not a cloud build.
- This is not remote execution.
- This is evidence-hosting architecture doctrine only.

## 15. Clean law

SELFSERVER is the body.

OURSELFCLOUD is the vault.

RUORA is the proof index.

Evidence stays governed.

References are not artifacts.

Storage is not review.

Review is not evaluation.

Evaluation is not UNREAL-002.

Updater drift is not doctrine.
