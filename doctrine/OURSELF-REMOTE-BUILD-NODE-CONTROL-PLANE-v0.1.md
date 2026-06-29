# OURSELF Remote Build-Node Control Plane v0.1

## 1. Prime thesis

The local Mac is the command console, not the render factory. Unreal becomes a remote worker node. Web/Bubble remains the logic and state interaction layer. UREEL remains the projection layer. Repo remains proof body.

Remote worker builds.
Human governs.
Repo proves.
UREEL projects.
Unreal embodies.

This doctrine captures development topology only. It does not authorize implementation, deployment, provisioning, Unreal project creation, package installation, remote access setup, or build scripts.

## 2. Three-glitch emergence

The development topology emerged from three glitches resolving into one operating model:

Glitch 1 — UWebBrowser
→ Web realm can be embedded inside Unreal.

Glitch 2 — Unreal storage barrier
→ Unreal should not live on weak local hardware.

Glitch 3 — Development topology inversion
→ Local device becomes command console; Unreal becomes remote worker node.

Together, these reveal a topology inversion: the user's local machine should command, inspect, review, govern, and seal. It should not be forced to carry the full weight of Unreal storage, rendering, compiling, packaging, and simulation.

## 3. Why Unreal should not live on weak local hardware

Unreal can demand large storage, GPU capacity, memory, thermal headroom, long compile cycles, and sustained render throughput.

Weak local hardware creates pressure in the wrong place. It turns the command console into the bottleneck, slows iteration, risks storage exhaustion, and invites shortcuts that weaken proof discipline.

The purpose of remote topology is not to escape governance. It is to preserve governance while moving heavy build and render labor to a machine designed for that labor.

## 4. Local machine as command console

The local Mac is the command console.

It writes doctrine, commands agents when authorized, reviews proof, controls Git, reads diffs, verifies outputs, preserves memory, and coordinates Human_TURN authorization.

The local machine should remain light enough to think, inspect, decide, and govern. It may prepare instructions, review artifacts, run small validation checks, inspect repository state, and seal approved changes.

Local device is command console, not render factory.

## 5. Remote machine as build/render worker node

The remote machine is the build/render worker node.

It receives bounded build instructions. It performs heavy Unreal tasks such as compiling, packaging, rendering, simulation testing, asset processing, and candidate artifact generation when separately authorized.

The worker does not govern doctrine. It does not decide truth. It does not seal. It does not push by default. It returns candidate outputs for review.

Remote worker builds; it does not govern.

## 6. UREEL relationship

UREEL remains the projection layer.

The remote worker may help build or render future UREEL embodiment artifacts, but UREEL remains downstream of canonical proof events and the doctrine already sealed in `doctrine/UREEL-REALM-VISION-v0.1.md`.

Remote topology does not change UREEL's authority boundary. UREEL projects reality-state; it does not invent truth.

UREEL remains downstream of canonical proof events.

## 7. Bubble/web relationship

Bubble/web remains logic and state interaction.

Bubble, React, Next.js, and related web layers may continue to handle accessible interaction surfaces, authenticated flows, forms, dashboards, content, and state interaction. Remote Unreal build capacity does not replace the web logic layer.

Bubble/web remains logic and state interaction.

## 8. UWebBrowser relationship

UWebBrowser remains a possible bridge between web logic and Unreal embodiment.

It may embed web realm surfaces inside Unreal or expose web state to an Unreal scene as presentation. It cannot become canonical authority and cannot bypass server authorization, AuditEvent proof, RealityEvent sealing, or AECHO memory.

UWebBrowser remains a bridge, not authority.

## 9. Repo/proof relationship

Repo remains proof body.

The repository is where doctrine, accepted source, reviewable artifacts, commit history, proof references, and governed changes become visible. A remote worker can produce candidate outputs, but those outputs are not canonical merely because they were generated.

Worker output is candidate until reviewed and sealed.

## 10. Control plane model

The control plane is not the remote machine.

The control plane is the governed relationship among Human_TURN, local command console, repo state, proof review, bounded worker instructions, and seal authority.

Required model:

```text
Local Mac / command console
→ writes doctrine, commands agents, reviews proof, controls Git
→ sends bounded build instructions to remote worker
→ remote worker builds/renders Unreal artifacts
→ artifacts return to repo/proof ledger
→ Human_TURN authorizes seal
```

Human_TURN remains authority.

## 11. Worker node model

The worker node is an execution surface.

It may receive exact instructions, source snapshots, asset inputs, branch pointers, build targets, test commands, render jobs, or packaging tasks. Its output must return as artifacts, logs, diffs, screenshots, builds, reports, or reproducible proof.

It must be treated as a bounded worker, not a second source of truth.

Remote worker builds; it does not govern.

## 12. Development topology diagram

```text
Human_TURN
   ↓ authorizes
Local Mac / Command Console
   ↓ writes doctrine, inspects repo, controls Git
RUORA Repo / Proof Body
   ↓ sends bounded instructions only after authorization
Remote Build/Render Worker Node
   ↓ returns candidate artifacts, logs, renders, build outputs
Local Mac / Command Console
   ↓ reviews proof and diffs
Human_TURN
   ↓ authorizes seal
RUORA Repo / Proof Ledger
```

This topology reduces local hardware strain without weakening governance.

## 13. Data and secret boundaries

No secrets on remote worker unless explicitly authorized.

No raw production credentials in Unreal project files.

No raw production credentials in browser projection.

No service-role key or privileged token may be placed in source, assets, Blueprints, packaged builds, config committed to Git, or remote logs.

Remote workers may receive only the minimum data needed for the bounded task. Personal data, proof trails, credentials, and production state require explicit authorization and a defined rollback or revocation path.

## 14. Artifact flow

Artifacts flow from worker to review, not from worker to authority.

Candidate outputs may include:

- Unreal build logs
- packaged builds
- render outputs
- screenshots
- performance captures
- asset manifests
- generated project files
- reproducible command transcripts
- failure reports

Artifacts return to the repo/proof ledger only after review. Large binaries may require artifact storage, Git LFS, release storage, or a child repo decision, but that storage decision is pending.

## 15. What local machine may do

The local machine may:

- write doctrine
- inspect repo state
- control Git
- review diffs
- read logs and artifacts
- prepare bounded build instructions
- verify proof
- coordinate Human_TURN authorization
- seal accepted doctrine or source changes
- reject worker output
- request reruns with narrower instructions

The local machine may remain the authority interface without becoming the heavyweight render machine.

## 16. What remote node may do

The remote node may:

- compile Unreal when separately authorized
- render candidate outputs
- run build commands
- package candidate artifacts
- process assets
- return logs, screenshots, binaries, reports, and reproducible proof
- execute bounded instructions from the local command console

Its work is operational labor, not governance.

## 17. What remote node may not do

The remote node may not:

- govern doctrine
- seal commits
- push without Human_TURN authorization
- deploy without proof review
- receive secrets without explicit authorization
- store raw production credentials in Unreal project files
- become canonical truth
- bypass AuditEvent, RealityEvent, TransmutationEvent, AECHO, server authorization, or repo review
- mutate child repos unless separately authorized
- convert worker access into ongoing authority

No remote push without Human_TURN authorization.

No deployment from worker node without proof review.

## 18. Security law

1. Local device is command console, not render factory.
2. Remote worker builds; it does not govern.
3. Repo remains proof body.
4. Human_TURN remains authority.
5. Worker output is candidate until reviewed and sealed.
6. No secrets on remote worker unless explicitly authorized.
7. No raw production credentials in Unreal project files.
8. No remote push without Human_TURN authorization.
9. No deployment from worker node without proof review.
10. UREEL remains downstream of canonical proof events.
11. UWebBrowser remains a bridge, not authority.
12. Unreal renders embodiment; it does not own truth.
13. Bubble/web remains logic and state interaction.
14. Remote topology must reduce local hardware strain without weakening governance.

## 19. Launch / implementation gate

This is not Unreal implementation.

This is not deployment.

This is not Pixel Streaming.

This is not cloud provisioning.

This is not a build script.

This is not a remote access setup.

This is topology doctrine only.

No build may begin from this document alone. Separate authorization is required for provisioning, remote machine selection, Unreal installation, project creation, repository movement, artifact storage, CI/CD, Pixel Streaming, UWebBrowser implementation, secret transfer, deployment, or worker Git access.

## 20. Pending implementation decisions

The following decisions remain pending, not decided:

- Which remote worker: cloud VM, Windows workstation, external SSD workstation, Mac Studio, EC2/GPU instance, Shadow/Parsec-style machine, or other.
- Whether Unreal lives on external SSD, remote Windows machine, or cloud GPU box.
- Whether Pixel Streaming is used.
- Whether UWebBrowser is the first bridge or later bridge.
- Whether build artifacts are stored in RUORA root, child repo, or artifact storage.
- Whether any remote secrets are allowed.
- Whether remote worker gets Git write access.
- Whether CI/CD is introduced.

Until these are resolved through explicit authorization, the remote build-node model remains doctrine and topology only.

