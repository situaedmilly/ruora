# FREED SELF 14-Day Chamber Manual Schema v0.1

## 1. Prime thesis

The FREED SELF 14-Day Chamber Manual Schema converts the sealed chamber doctrine into an executable manual evidence structure.

This schema authorizes the shape of the chamber record.

It does not authorize Bubble implementation, database fields, backend storage, frontend build, automation, passive sensing, diagnosis, deployment, or production launch.

The chamber remains manual-first.

Evidence comes before automation.

SELF visibility comes before identity claim.

Proof action comes before reality claim.

## 2. Doctrine inheritance

This schema inherits from:

- `doctrine/FREED-SELF-REALITY-ACQUISITION-CHAMBER-v0.1.md`
- `MASTER_BLUEPRINT.md`
- SELF Axiom doctrine
- SELF Identity doctrine
- RUORA doctrine
- OURSELF Master Command doctrine

The schema does not replace doctrine. It gives doctrine a manual operating vessel.

## 3. Schema identity

Name: FREED SELF 14-Day Chamber Manual Schema v0.1

Gate: `CHAMBER-002`

Status: Authorized manual schema, not implemented app schema.

Primary use:

- manual worksheet
- command-line chamber later
- report template later
- implementation reference later

Non-use:

- not Bubble data type
- not database table
- not API contract
- not production storage
- not automated scoring system
- not passive sensing system

## 4. Chamber object model

The manual chamber uses these conceptual record objects:

1. `ChamberRun`
2. `ChamberDay`
3. `MorningBlueprintAlignment`
4. `MiddayContextPulse`
5. `PressureEventRupture`
6. `NightProofSeal`
7. `ProofEvent`
8. `DistinctionEvent`
9. `TransmutationEvent`
10. `RealityEvent`
11. `AuditEvent`
12. `ChamberScore`
13. `OutputReport`

These names are manual schema terms only. They do not create database schema, Bubble schema, production types, or API contracts.

## 5. ChamberRun record

`ChamberRun` is the full 14-day container.

Required fields:

- chamber_run_id
- participant_label
- start_date
- end_date
- intended_freed_self_reality
- primary_current_reality
- required_identity_configuration
- required_capabilities
- required_operating_logic
- required_distinctions
- required_environments
- required_proof_actions
- measurement_caution_acknowledged
- proof_laws_acknowledged
- daily_records
- final_output_reports
- unresolved_uncertainties
- next_authorized_gate

Rules:

- One `ChamberRun` contains exactly 14 `ChamberDay` records.
- Missing days must be preserved as missing, not backfilled with invented evidence.
- A chamber run may be incomplete and still useful.
- Incomplete evidence must not be rounded up into transformation claims.

## 6. ChamberDay record

`ChamberDay` is the daily evidence packet.

Required fields:

- day_number
- date
- morning_blueprint_alignment
- midday_context_pulse
- pressure_event_ruptures
- night_proof_seal
- proof_events
- distinction_events
- transmutation_events
- reality_events
- audit_events
- chamber_score
- uncertainty_notes

Rules:

- `day_number` runs from 1 through 14.
- `pressure_event_ruptures` may contain zero or more entries.
- `proof_events` must reference observable action or artifact evidence.
- `reality_events` must be reserved for external reality changes, not internal feelings alone.
- `audit_events` must record what was reviewed, when, and by whom.

## 7. MorningBlueprintAlignment template

Morning Blueprint Alignment sets the intended operating law for the day.

Fields:

- Which FREED SELF reality am I funding today?
- Which distinction must govern today?
- Which proof action will make the distinction material?
- What environment will amplify this SELF today?
- What refusal must be pre-authored today?

Manual capture guidance:

- Write before the day becomes reactive.
- Use one primary distinction, not a scattered list.
- Choose one proof action that can produce evidence before night.
- Name the environment deliberately.
- Pre-author one refusal before pressure appears.

Output:

- intended_reality_focus
- governing_distinction
- planned_proof_action
- amplifying_environment
- pre_authored_refusal

## 8. MiddayContextPulse template

Midday Context Pulse captures the live field before memory edits the day.

Fields:

- Where am I?
- Who am I around?
- What is my energy?
- What is my clarity?
- What operating rule is currently active?
- Am I funding the intended reality or the inherited one?
- What drift is visible?

Manual capture guidance:

- Record the field as observed, not as desired.
- Energy and clarity may be numeric, descriptive, or both.
- Drift must be named without shame and without false certainty.

Output:

- location_context
- relational_context
- energy_state
- clarity_state
- active_operating_rule
- reality_funding_status
- visible_drift

## 9. PressureEventRupture template

Pressure Event Rupture captures what happens when installed code is tested.

Fields:

- What happened?
- What did my nervous system attempt to do?
- Which distinction disappeared?
- Which lower operating rule seized control?
- What action would FREED SELF execute?
- What repair action is required?
- What proof action installs the improved response?

Manual capture guidance:

- Use this template when pressure appears, not only at night.
- Do not pathologize the response.
- Capture attempted protection, seized operating rule, and repair action.
- The improved response must become a proof action, not a vague intention.

Output:

- pressure_trigger
- attempted_protective_response
- lost_distinction
- lower_operating_rule
- freed_self_action
- repair_action
- installation_proof_action

## 10. NightProofSeal template

Night Proof Seal distinguishes claim from proof.

Fields:

- What did SELF build?
- What did SELF protect?
- What did SELF refuse?
- Where did time actually go?
- What created energy?
- What depleted energy?
- Which action changed reality outside SELF?
- What proof artifact exists?
- What must be repeated tomorrow?

Manual capture guidance:

- Record evidence before interpretation.
- Name artifacts directly.
- Separate internal state change from external reality change.
- Preserve repeated needs without turning them into failure.

Output:

- built_artifacts
- protected_boundary
- refused_drift
- time_allocation
- energy_created_by
- energy_depleted_by
- external_reality_change
- proof_artifact
- tomorrow_repetition

## 11. ProofEvent structure

`ProofEvent` records a bounded action that created observable evidence.

Fields:

- proof_event_id
- date
- related_day_number
- proof_action
- observable_evidence
- artifact_reference
- affected_distinction
- affected_environment
- external_effect
- reviewer
- audit_event_reference

Rules:

- No proof without observable evidence.
- No proof without AuditEvent.
- A feeling may contextualize proof, but it cannot replace proof.
- A proof event may be small if it is real.

## 12. DistinctionEvent structure

`DistinctionEvent` records a perception upgrade that altered behavior.

Fields:

- distinction_event_id
- distinction_name
- old_perception
- new_perception
- decision_changed
- action_changed
- artifact_changed
- relationship_changed
- environment_changed
- future_option_created
- proof_event_reference

Rules:

- A distinction is not installed merely because it was named.
- A distinction is installed only when it alters perception, decision, action, artifact, relationship, environment, or future options.

## 13. TransmutationEvent structure

`TransmutationEvent` records a transformation claim that survived proof.

Fields:

- transmutation_event_id
- source_pattern
- pressure_context
- old_operating_logic
- new_operating_logic
- repeated_proof_actions
- evidence_window
- remaining_gap
- audit_event_reference

Rules:

- No transformation claim without TransmutationEvent.
- A single good day is not enough to seal transformation.
- Repetition matters.
- Uncertainty must remain visible.

## 14. RealityEvent structure

`RealityEvent` records a verified change outside the participant's internal claim.

Fields:

- reality_event_id
- external_change
- affected_person_or_system
- artifact_or_outcome
- date_observed
- proof_event_reference
- audit_event_reference
- limitation

Rules:

- No reality claim without RealityEvent.
- RealityEvent requires external evidence or observed consequence.
- Internal confidence is not enough to seal a RealityEvent.

## 15. AuditEvent structure

`AuditEvent` records review, witness, and proof handling.

Fields:

- audit_event_id
- date
- reviewer
- reviewed_record
- reviewed_artifact
- decision
- uncertainty
- next_required_proof

Rules:

- No proof without AuditEvent.
- The reviewer may be Human_TURN in the manual chamber.
- AuditEvent does not need automation.
- AuditEvent must preserve uncertainty instead of forcing closure.

## 16. ChamberScore manual logic

The chamber may use manual scoring to support reflection. Scores are not diagnosis, prophecy, identity typing, or automated truth.

Use a 0-5 scale:

- 0 = absent / no evidence
- 1 = named but not acted
- 2 = attempted once
- 3 = acted with partial evidence
- 4 = repeated with meaningful evidence
- 5 = repeated, observable, and externally consequential

Daily score categories:

- Blueprint alignment
- Proof action completion
- Distinction embodiment
- Environment support
- Refusal integrity
- Pressure recovery
- Reality ripple
- Audit clarity

Rules:

- Scores support pattern review only.
- Scores do not define SELF.
- Scores must be accompanied by evidence notes.
- A low score is information, not failure.
- A high score without artifact evidence remains unstable.

## 17. Fourteen-day output reports

After 14 days, the manual schema must support these reports:

1. Lived SELF Reality Twin v1
2. FREED SELF Blueprint v1
3. Transmutation Delta
4. Top 5 Installed Distinctions
5. Top 5 Missing Distinctions
6. Amplifying Environment Map
7. Relational Field Map
8. Pressure Pattern Report
9. Recovery Signature
10. Next 7 Proof Actions

Each report must include:

- source evidence
- uncertainty notes
- proof gaps
- next action
- boundary statement

No report may claim destiny, diagnosis, universal truth, or guaranteed transformation.

## 18. OutputReport structure

`OutputReport` is the final report record.

Fields:

- report_name
- evidence_window
- source_days
- key_findings
- proof_artifacts
- uncertainty_notes
- recommended_repetitions
- next_authorized_gate

Rules:

- Reports summarize evidence; they do not invent evidence.
- Reports may rank patterns but must preserve uncertainty.
- Reports must distinguish observed evidence from interpretation.

## 19. Manual-first rules

Manual-first means:

- human-entered records
- no passive sensors
- no hidden scoring
- no diagnosis
- no covert surveillance
- no automated identity verdict
- no universal conclusion from N-of-1 patterns
- no prophecy

Measurement itself may change behavior. The schema must preserve that caution.

## 20. Implementation boundary

This schema authorizes manual structure only.

This is not Bubble schema.

This is not database schema.

This is not frontend implementation.

This is not backend implementation.

This is not Unreal implementation.

This is not automation.

This is not passive sensing.

This is not diagnosis.

This is not psychological treatment.

This is not deployment.

This is manual schema authorization only.

## 21. CHAMBER-002 authorization law

`CHAMBER-002` authorizes the exact manual chamber structure future implementation must obey.

It does not authorize implementation.

It does not authorize Bubble data types.

It does not authorize schema mutation.

It does not authorize automated scoring.

It does not authorize passive sensing.

It does not authorize product launch.

Any later implementation must preserve:

- manual-first evidence
- proof before claim
- AuditEvent before proof seal
- TransmutationEvent before transformation claim
- RealityEvent before reality claim
- uncertainty before conclusion
- Human_TURN authority

## 22. Next authorized gate

The next gate after this schema is not Unreal.

The next gate may be one of:

- manual worksheet template
- local command chamber format
- report template
- Bubble schema proposal

None of those are created by this document.

Chamber proves.

Implementation waits.
