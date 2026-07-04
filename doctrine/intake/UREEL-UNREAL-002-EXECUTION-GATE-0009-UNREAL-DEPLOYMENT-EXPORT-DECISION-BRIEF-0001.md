# UREEL UNREAL-002 Execution Gate 0009 Unreal Departure Authorization Decision Brief 0001

## Status
gate_decision_brief_id: UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT-DECISION-BRIEF-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_human_decision_id: UREEL-UNREAL-002-EXECUTION-GATE-0008-UNREAL-CONNECTION-HUMAN-DECISION-0001
decision_brief_status: HUMAN_TURN_GATE_0009_DECISION_REQUIRED
gate_status: DECISION_PENDING
departure_authorization_status: DECISION_PENDING
actual_departure_status: NOT_STARTED
artifact_departure_status: CONTAINED
distribution_status: PRIVATE
public_visibility_status: NONE

## Gate Scope
This brief prepares a Human_TURN decision for Gate 0009 departure scope only.
Gate 0009 establishes whether the project has earned the right to leave containment. It does not package, cook, build, sign, or export anything yet.

Every gate through 0008 governs what the project is permitted to become internally: existence, matter, behavior, capability, connection. Gate 0009 governs something categorically different — whether the project is permitted to become observable outside itself.

The governing question is not "can we package." It is:

**Has the project earned the right to leave containment?**

## The Six-Stage Mutation Ontology (complete through this gate)
- Gate 0004 — Existence (project shell exists) — CLOSED
- Gate 0005 — Matter (asset baseline exists) — CLOSED
- Gate 0006 — Executable Behavior (project can execute logic) — CLOSED: NO_EXECUTABLE_BEHAVIOR_BASELINE_NEEDED
- Gate 0007 — Capability (project gains new abilities via plugins/SDKs) — CLOSED: NO_CAPABILITY_BASELINE_NEEDED
- Gate 0008 — Connection (project communicates with external systems) — CLOSED: NO_CONNECTION_BASELINE_NEEDED
- Gate 0009 — Departure (project may leave containment) — THIS GATE

Notice: nothing after Gate 0004 is actually specific to Unreal. Existence, Matter, Behavior, Capability, Connection, and Departure are universal system laws that apply to any engineered artifact — software, digital product, AI agent, or infrastructure — as it moves from internal creation toward external execution. UREEL is simply the first candidate this ontology is being proven against.

## Three Realities
A project exists inside three realities, and Gate 0009 governs the transition between the second and third:

**Reality 1 — Private.** Only creators can observe it. Everything through Gate 0008 lives here.

**Reality 2 — Contained Distribution.** A packaged, cooked, or built artifact exists (executable, APK, IPA, EXE, Docker image, Steam build, store submission package) but is still not public — only distributable in principle, held by its creator.

**Reality 3 — Observed Reality.** Someone else can now execute the artifact. The artifact possesses agency outside its creator. This is Departure.

A build alone does not cross into Reality 3. Departure begins when the artifact becomes distributable to a party other than its creator.

## Departure Covers Four Classes
Any of the following mutating the project or its outputs falls under Gate 0009, not prior gates:

1. **Packaging/Cook** — `RunUAT BuildCookRun`, packaged project output for Windows/Mac/Linux/console, staged builds, Docker/OCI images.
2. **Store/Distribution Submission** — Steam builds, console cert submission, mobile app store (Google Play/App Store/TestFlight) uploads, itch.io/Epic Games Store publishing.
3. **Hosted/Streamed Deployment** — Pixel Streaming server deployment, cloud-rendered instance provisioning, hosting via CDN/S3/CloudFront/Firebase Hosting, or any environment where the built project runs on infrastructure outside the local machine.
4. **Distributable Artifact Creation** — signed/installer executables, archive outputs, CI-produced release artifacts, GitHub Releases, artifact registries, or any release/CD pipeline that hands the artifact to a party other than its creator.

Explicitly excluded from Gate 0009 (already resolved at prior gates, and not reopened by this brief):
- Executable behavior authorship (Gate 0006, closed).
- Plugin/SDK/capability acquisition (Gate 0007, closed).
- External connection establishment (Gate 0008, closed) — Departure and Connection are orthogonal. A project may depart without connecting (a signed offline build) or depart while connecting (a hosted streamed instance). A departure that also establishes a new external connection requires both Gate 0008 and Gate 0009 open before it proceeds.

## Source Basis
Gate 0008 Human Decision found:
- Gate 0007 closed as NO_CAPABILITY_BASELINE_NEEDED
- Gate 0008 closed as NO_CONNECTION_BASELINE_NEEDED; UREEL-OURSELFCLOUD-NODE-0 remains an isolated Unreal project with no external connection authorized
- no backend endpoint, auth provider, cloud service, API call, Bubble binding, multiplayer service, or telemetry service exists for this project
- no code, behavior, capability, or connection mutation occurred
- repo status remained clean; MASTER_BLUEPRINT.md remained unchanged

No Gate 0008 Proof Report currently exists on disk; this brief sources directly from the sealed Human Decision only.

Project remains fully contained:
- no external connection authorized
- no executable behavior authorized
- no acquired capability authorized
- no deployment history
- no published artifacts
- no packaged builds
- no release channels
- no distribution targets
- no departure authorization

## Departure Preconditions to Inspect
Should this gate later authorize a departure baseline, verification would examine (read-only, not executed by this brief):
- packaging settings, cook targets, build targets
- distribution profiles, store manifests
- signing identities, certificates, provisioning profiles
- executable outputs, installer outputs, archive outputs
- streaming endpoints, hosted instances
- repo HEAD, working tree state, remotes, MASTER_BLUEPRINT.md drift

This inspection is deferred to a future Gate 0009 Execution Pass / Proof Report, contingent on Human_TURN authorizing a departure baseline. This brief performs no inspection and executes no command.

## Gate 0009 Departure-Authorization Scope Options
Human_TURN must choose exactly one option:

**Option 1 — Defer Departure (recommended)**
`AUTHORIZE_UNREAL_002_GATE_0009_NO_DEPARTURE_BASELINE_NEEDED`

Meaning: no packaging, no cooking, no export, no executable generation, no IPA/APK/EXE/DMG generation, no distribution artifacts, no store submission, no Pixel Streaming publication, no cloud deployment, no shipping build, no public release. The project remains completely local — Reality 1.

**Option 2 — Authorize Departure Boundary**
`AUTHORIZE_UNREAL_002_GATE_0009_DEPARTURE_BASELINE_ONLY`

Meaning: Human_TURN authorizes creation of the minimum packaging/export infrastructure only — packaging configuration, build targets, shipping configuration, export profiles, cook settings, distribution metadata. This authorizes the *ability to prepare* departure, not departure itself. The project may enter Reality 2 (contained distribution) but not Reality 3 (observed reality) under this option alone.

**Option 3**
`HOLD_GATE_0009_PENDING_HUMAN_CLARIFICATION`

**Option 4**
`REJECT_GATE_0009_FOR_THIS_CANDIDATE`

## Recommendation
AUTHORIZE_UNREAL_002_GATE_0009_NO_DEPARTURE_BASELINE_NEEDED

Reason: the observed state is still —
- no executable behavior requiring distribution
- no acquired capability requiring packaging
- no authorized external connection
- no release artifact, distribution channel, hosted instance, or deployment target

Given the sequence already sealed (Gate 0006 → no executable behavior baseline needed, Gate 0007 → no capability baseline needed, Gate 0008 → no connection baseline needed), the consistent recommendation is deferral: containment precedes distribution, and distribution never precedes containment. Nothing has yet demonstrated the need to cross this boundary, and Departure carries the highest and most permanent consequence of any gate in this chain — every departure permanently expands the project's observable reality and cannot be un-published once another party has executed the artifact.

## Governing Laws
1. No system departs farther than it is authorized to connect.
2. Containment precedes distribution. Distribution never precedes containment.
3. A build is not a departure. Departure begins when the artifact becomes distributable to a party other than its creator.
4. Publication is evidence of authorization, not authorization itself.
5. Every departure permanently expands the system's observable reality.

## Recommendation Boundary
The sealed Gate 0008 Human Decision supports a departure-authorization decision because connection scope is already resolved and closed. Codex may recommend, but Human_TURN must authorize.

## Non-Departure-Authorization Statement
This brief does not authorize packaging, cooking, building, staging, signing, or exporting the project for any platform.
This brief does not authorize store or marketplace submission, public distribution, or hosted/streamed deployment.
This brief does not authorize signing keys, certificates, or publishing credentials of any kind.
This brief does not reopen Gate 0006, Gate 0007, or Gate 0008; no behavior authorship, capability acquisition, or connection establishment is authorized by this brief.
This brief does not authorize raw evidence attachment to RUORA beyond this doctrine artifact.

## Doctrine Confirmation
Gate 0009 is confirmed as governing Departure Authorization, not merely "Deployment/Export": the boundary between contained development and observed external reality. This framing extends beyond Unreal to any engineered artifact — software, digital product, AI agent, or infrastructure — transitioning from internal creation to external execution. The filename and gate number are preserved for continuity; the doctrine inside is redefined, matching the precedent already sealed at Gate 0006.

## Human_TURN Next Decision
Human_TURN must choose one Gate 0009 option.

## Decision Outcome
GATE_0009_DECISION_BRIEF_CAPTURED_NOT_DEPARTURE_AUTHORIZATION
