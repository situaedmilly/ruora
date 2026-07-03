# UREEL UNREAL-002 Execution Gate 0006 Unreal Executable Behavior Baseline Decision Brief 0001

## Status
gate_decision_brief_id: UREEL-UNREAL-002-EXECUTION-GATE-0006-UNREAL-CODE-BASELINE-DECISION-BRIEF-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0006-UNREAL-CODE-BASELINE
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_proof_report_id: UREEL-UNREAL-002-EXECUTION-GATE-0005-UNREAL-ASSET-BASELINE-PROOF-REPORT-0001
decision_brief_status: HUMAN_TURN_GATE_0006_DECISION_REQUIRED
gate_status: DECISION_PENDING
behavior_authorization_status: DECISION_PENDING
actual_behavior_mutation_status: NOT_AUTHORIZED

## Gate Scope
This brief prepares a Human_TURN decision for Gate 0006 executable behavior authorization scope only.
Gate 0006 establishes whether the project may now contain executable behavior. It does not author or execute any executable behavior yet.

## Doctrine Redefinition
Gate 0006 was originally framed as "Code Baseline," scoped to Source/, .h/.cpp files, and build metadata. That framing is too narrow and ages badly as Unreal's execution surfaces evolve.

Gate 0006 is redefined as **Executable Behavior Authorization**: the boundary governing whether this project may contain any executable logic, regardless of the language, graph, or tool used to author it. The filename and gate number are preserved for continuity; the doctrine inside is redefined.

The governing question is no longer "does this touch Source/?" It is:

**Can this project now execute logic?**

## The Four-Stage Mutation Ontology
Gate 0006 sits inside a broader mutation chain that this UREEL execution plan now follows:

- Gate 0004 — Existence (project shell exists)
- Gate 0005 — Matter (asset baseline exists)
- Gate 0006 — Behavior (project can execute logic)
- Gate 0007 — Capability (project gains new abilities via plugins/SDKs)
- Gate 0008 — Connection (project communicates with external systems)

This mapping is retained specifically because it remains correct independent of which Unreal execution systems exist at a given engine version.

## Executable Behavior Authorization Covers Four Classes
Any of the following mutating a project falls under Gate 0006, not future gates:

1. **Runtime Behavior** — PlayerController, Pawn, GameMode, GameState, Actor, ActorComponent, Subsystems, Gameplay Ability System, AI, Behavior Trees, Blueprint gameplay, C++.
2. **Editor Behavior** — Python, Blutility, Editor Utility Widgets, automation, asset generators, commandlets, cook scripts.
3. **Rendering Behavior** — Material Functions, Control Rig, Animation Blueprints, Niagara graphs, PCG, State Trees, Motion Matching.
4. **Build Behavior** — Build.cs, Target.cs, ModuleRules, AutomationTool, packaging scripts, CI.

Explicitly excluded from Gate 0006 (belong to later gates instead):
- Plugin/SDK installation that adds capability without authoring behavior (Gate 0007: OpenXR, MetaHuman, Steam, EOS, Cesium, Pixel Streaming, Substance, FMOD, DLSS).
- External communication (Gate 0008: Bubble, REST, GraphQL, Firebase, AWS, Supabase, Discord, Slack, OpenAI, MCP, GitHub).

## Source Basis
Gate 0005 execution pass found:
- canonical asset baseline established
- no gameplay systems created
- no Blueprints, C++, Python, Control Rig, Behavior Trees, or PCG graphs authored
- no plugins installed
- no code or build mutation occurred
- MASTER_BLUEPRINT.md remained unchanged
- repo status remained clean

## Gate 0006 Executable Behavior-Authorization Scope Options
Human_TURN must choose exactly one option:
- AUTHORIZE_UNREAL_002_GATE_0006_EXECUTABLE_BEHAVIOR_BASELINE_ONLY
- AUTHORIZE_UNREAL_002_GATE_0006_NO_EXECUTABLE_BEHAVIOR_BASELINE_NEEDED
- HOLD_GATE_0006_PENDING_HUMAN_CLARIFICATION
- REJECT_GATE_0006_FOR_THIS_CANDIDATE

## Recommendation
AUTHORIZE_UNREAL_002_GATE_0006_NO_EXECUTABLE_BEHAVIOR_BASELINE_NEEDED

Reason: UREEL currently has a valid project shell and canonical asset baseline. No gameplay systems, Blueprint graphs, C++ modules, Python/editor automation, Control Rig, PCG graphs, plugins, or integrations have been authorized yet. Deferring executable behavior authorization until a concrete gameplay or rendering system is actually needed avoids unnecessary executable surface area.

This recommendation is reinforced by external research on Unreal Engine project conventions: a project can exist and function as a Blueprint/asset-only vessel with zero C++ files and no generated code baseline; the dominant convention is to defer code/Blueprint authorship until a system needs to be built, then convert to C++ at a proven refactor point rather than authorizing executable behavior upfront. That evidence supports gating executable behavior by demonstrated need, not by project-setup timing, which is the same principle this redefined Gate 0006 encodes.

## If Executable Behavior Baseline Is Authorized
Keep it narrow. A minimal behavior baseline may include:
- an empty Source/ module only if C++ project conversion is structurally required
- project naming/build metadata
- no gameplay logic, no Blueprint gameplay graphs, no Control Rig, no PCG graphs
- no editor automation or commandlets
- no plugins (Gate 0007)
- no API calls, no Bubble/cloud integration (Gate 0008)
- no deployment or packaging scripts

## Recommendation Boundary
The sealed Gate 0005 records support a behavior-authorization decision because the canonical asset baseline is already created and verified. Codex may recommend, but Human_TURN must authorize.

## Non-Executable-Behavior-Authorization Statement
This brief does not authorize any Blueprint graph, C++ class, Python script, Control Rig graph, Behavior Tree, PCG graph, Editor Utility Widget, commandlet, or build script mutation.
This brief does not authorize plugin installation, API calls, deployment, cloud mutation, Bubble/schema mutation, remote Git activity, or raw evidence attachment.

## Human_TURN Next Decision
Human_TURN must choose one Gate 0006 option.

## Decision Outcome
GATE_0006_DECISION_BRIEF_CAPTURED_NOT_BEHAVIOR_AUTHORIZATION
