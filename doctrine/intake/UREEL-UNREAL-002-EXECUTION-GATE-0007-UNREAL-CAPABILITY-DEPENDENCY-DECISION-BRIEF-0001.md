# UREEL UNREAL-002 Execution Gate 0007 Unreal Capability Dependency Decision Brief 0001

## Status
gate_decision_brief_id: UREEL-UNREAL-002-EXECUTION-GATE-0007-UNREAL-CAPABILITY-DEPENDENCY-DECISION-BRIEF-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0007-UNREAL-CAPABILITY-DEPENDENCY
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_human_decision_id: UREEL-UNREAL-002-EXECUTION-GATE-0006-UNREAL-CODE-BASELINE-HUMAN-DECISION-0001
decision_brief_status: HUMAN_TURN_GATE_0007_DECISION_REQUIRED
gate_status: DECISION_PENDING
capability_authorization_status: DECISION_PENDING
actual_capability_mutation_status: NOT_AUTHORIZED

## Gate Scope
This brief prepares a Human_TURN decision for Gate 0007 capability-acquisition scope only.
Gate 0007 establishes whether the project may now acquire new capability through plugins, SDKs, or Marketplace dependencies. It does not author or execute any capability mutation yet.

Gate 0007 governs installing capability, not authoring behavior. Behavior authorship (Gate 0006) is already closed and remains closed by this brief. External connection (Gate 0008: Bubble, REST, GraphQL, Firebase, AWS, Supabase, Discord, Slack, OpenAI, MCP, GitHub) remains a separate, unopened gate.

## The Four-Stage Mutation Ontology
- Gate 0004 — Existence (project shell exists)
- Gate 0005 — Matter (asset baseline exists)
- Gate 0006 — Behavior (project can execute logic) — CLOSED: NO_EXECUTABLE_BEHAVIOR_BASELINE_NEEDED
- Gate 0007 — Capability (project gains new abilities via plugins/SDKs) — THIS GATE
- Gate 0008 — Connection (project communicates with external systems) — unopened

## Capability Acquisition Covers
Any of the following mutating the project falls under Gate 0007, not other gates:
- Marketplace plugin installation (e.g. OpenXR, MetaHuman, Steam, EOS, Cesium, Pixel Streaming, Substance, FMOD, DLSS)
- Third-party SDK integration
- Engine extension modules that add new abilities without authoring project-specific behavior
- Marketplace asset dependencies that carry their own plugin/code payload

Explicitly excluded from Gate 0007 (belong to other gates instead):
- Project-authored gameplay, editor, rendering, or build behavior (Gate 0006, already closed).
- External system communication and API/cloud/Bubble connection (Gate 0008, still unopened).

## Source Basis
Gate 0006 closed as NO_EXECUTABLE_BEHAVIOR_BASELINE_NEEDED; UREEL-OURSELFCLOUD-NODE-0 remains an asset-only vessel with no authored behavior.

Observed `.uproject` state (read directly, not assumed):
- one plugin entry present: `ModelingToolsEditorMode` (Enabled: true, TargetAllowList: Editor)
- this is Unreal's standard default template plugin for Editor mesh-modeling tools, present since project creation — it was not installed or authorized as part of this gate chain
- no other plugins present
- no SDKs, no Marketplace asset dependencies, no engine extensions added
- repo/asset baseline unchanged since Gate 0005
- no code, build, or behavior mutation occurred

## Gate 0007 Capability-Acquisition Scope Options
Human_TURN must choose exactly one option:
- AUTHORIZE_UNREAL_002_GATE_0007_CAPABILITY_BASELINE_ONLY
- AUTHORIZE_UNREAL_002_GATE_0007_NO_CAPABILITY_BASELINE_NEEDED
- HOLD_GATE_0007_PENDING_HUMAN_CLARIFICATION
- REJECT_GATE_0007_FOR_THIS_CANDIDATE

## Recommendation
AUTHORIZE_UNREAL_002_GATE_0007_NO_CAPABILITY_BASELINE_NEEDED

Reason: no concrete capability need has emerged for UREEL-OURSELFCLOUD-NODE-0. The single plugin present in the `.uproject` file is a default template artifact carried over from project creation, not a capability authorized or installed through this gate chain. Deferring capability acquisition until a concrete system actually requires a specific plugin or SDK mirrors the same deferral principle already sealed at Gate 0005 (Matter) and Gate 0006 (Behavior): authorize surface area by demonstrated need, not by project-setup timing.

## If Capability Baseline Is Authorized
Keep it narrow. A minimal capability baseline may include:
- installation of a single named plugin or SDK required for a concrete, already-identified need
- no gameplay logic, no Blueprint gameplay graphs, no C++ authorship (Gate 0006 remains closed unless separately reopened)
- no API calls, no Bubble/cloud integration (Gate 0008)
- no deployment or packaging scripts

## Recommendation Boundary
The sealed Gate 0006 Human Decision records support a capability-acquisition decision because behavior scope is already resolved and closed. Codex may recommend, but Human_TURN must authorize.

## Non-Capability-Authorization Statement
This brief does not authorize plugin installation, SDK integration, Marketplace asset import, or engine extension addition.
This brief does not authorize API calls, Bubble/cloud integration, deployment, or remote Git activity.
This brief does not reopen Gate 0006; no Blueprint graph, C++ module, Python/editor automation, Control Rig graph, Behavior Tree, PCG graph, Editor Utility Widget, commandlet, or build script mutation is authorized.
This brief does not authorize raw evidence attachment to RUORA.

## Human_TURN Next Decision
Human_TURN must choose one Gate 0007 option.

## Decision Outcome
GATE_0007_DECISION_BRIEF_CAPTURED_NOT_CAPABILITY_AUTHORIZATION
