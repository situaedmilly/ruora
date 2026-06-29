# Remote Worker Selection Matrix v0.1

## 1. Decision identity

This decision matrix selects the first Unreal / UREEL remote worker topology.

It belongs to Lane A — UREEL / Unreal infrastructure.

The governing question is: what machine carries Unreal?

This is decision documentation only. It does not install Unreal, create project files, provision cloud infrastructure, purchase hardware, deploy, mutate Bubble, create schema, call APIs, create worktrees, spawn agents, create remotes, push, or modify existing doctrine files.

This matrix does not authorize purchase, provisioning, installation, deployment, Pixel Streaming, Unreal project creation, remote Git access, secret transfer, or hardware acquisition.

## 2. Current doctrine state

Canonical dependencies:

- `doctrine/UREEL-REALM-VISION-v0.1.md`
- `doctrine/OURSELF-REMOTE-BUILD-NODE-CONTROL-PLANE-v0.1.md`

Current boundary:

- UREEL remains the projection layer.
- Bubble/web remains logic and state interaction.
- Unreal renders embodiment; it does not own truth.
- UWebBrowser remains a bridge, not authority.
- Remote worker builds; it does not govern.
- Repo remains proof body.
- Human_TURN remains authority.
- Remote topology must reduce local hardware strain without weakening governance.

## 3. Candidate topology list

Only these candidate topologies are evaluated:

1. Local Mac + external SSD only
2. Local Mac command console + external SSD Unreal workspace
3. Dedicated Windows workstation
4. Mac Studio / high-power local workstation
5. Cloud GPU instance
6. EC2 / AWS GPU worker
7. Shadow / Parsec-style remote machine
8. Hybrid: local command console + remote GPU/workstation node + artifact storage

No other candidate is included in this lane.

## 4. Scorecard table

Scores use a 0-5 scale, where 0 means unsuitable and 5 means strong fit.

| Option | Hardware power | Storage capacity | Cost efficiency | Setup speed | Unreal compatibility | Remote access quality | Security/governance fit | Proof workflow fit | Scalability | Beginner manageability | Long-term viability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Local Mac + external SSD only | 1 | 3 | 4 | 4 | 2 | 1 | 4 | 3 | 1 | 4 | 1 |
| Local Mac command console + external SSD Unreal workspace | 2 | 4 | 4 | 4 | 2 | 1 | 4 | 4 | 2 | 4 | 2 |
| Dedicated Windows workstation | 5 | 5 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 3 | 5 |
| Mac Studio / high-power local workstation | 4 | 4 | 2 | 3 | 3 | 2 | 5 | 5 | 3 | 4 | 4 |
| Cloud GPU instance | 5 | 4 | 2 | 2 | 5 | 4 | 3 | 4 | 5 | 2 | 4 |
| EC2 / AWS GPU worker | 5 | 4 | 2 | 2 | 5 | 4 | 3 | 4 | 5 | 2 | 4 |
| Shadow / Parsec-style remote machine | 4 | 3 | 4 | 4 | 4 | 5 | 3 | 3 | 3 | 4 | 3 |
| Hybrid: local command console + remote GPU/workstation node + artifact storage | 5 | 5 | 3 | 2 | 5 | 4 | 5 | 5 | 5 | 2 | 5 |

## 5. Option-by-option analysis

### 1. Local Mac + external SSD only

Summary: Keeps all work local and adds storage relief through an external SSD.

Strengths: Fastest to understand, low governance complexity, no remote access layer, no new network exposure, and minimal operational overhead.

Weaknesses: Does not solve GPU, compile, render, thermal, or simulation pressure. It turns the local command console into the render factory.

Governance risk: Low security risk, high workflow risk because local hardware strain can create shortcuts.

Estimated role in OURSELF topology: Emergency local storage relief only.

Launch suitability: Reject.

### 2. Local Mac command console + external SSD Unreal workspace

Summary: Preserves the local Mac as command console while moving Unreal workspace storage to an external SSD.

Strengths: Improves storage pressure, keeps repo review local, preserves Human_TURN control, and can support early inspection or tiny experiments if separately authorized.

Weaknesses: Still does not solve GPU/render/compile pressure. It is not a real worker-node topology.

Governance risk: Moderate. It preserves local authority but can blur the line between command console and render factory.

Estimated role in OURSELF topology: Temporary bridge if no remote worker is available.

Launch suitability: Temporary.

### 3. Dedicated Windows workstation

Summary: A dedicated Windows machine carries Unreal build, render, compile, and simulation pressure while the local Mac remains command console.

Strengths: Strong Unreal compatibility, predictable GPU support, local network or secure remote access options, clear worker-node identity, and strong long-term viability.

Weaknesses: Hardware cost, setup responsibility, updates, backups, physical space, and security hardening.

Governance risk: Manageable if Git write access, secrets, and deployment authority remain restricted.

Estimated role in OURSELF topology: Strong candidate for first real Unreal worker node.

Launch suitability: Good for private beta.

### 4. Mac Studio / high-power local workstation

Summary: A high-power local Apple workstation carries heavier creative and build work while staying physically local.

Strengths: Strong local governance, simple proof review, good performance for many tasks, durable hardware, and clean authority boundary if the machine is still treated as a worker.

Weaknesses: Cost, Unreal compatibility constraints compared with Windows, potential packaging limitations for Windows targets, and less useful for testing remote topology.

Governance risk: Low. The main risk is collapsing command console and worker into one local authority surface.

Estimated role in OURSELF topology: Strong local workstation option, but less aligned with remote worker doctrine.

Launch suitability: Good for prototype.

### 5. Cloud GPU instance

Summary: A generic cloud GPU machine handles Unreal build/render workloads on demand.

Strengths: Scalable, high performance, disposable when governed correctly, can grow with demand, and avoids local hardware strain.

Weaknesses: Setup complexity, cost surprises, cloud security burden, storage persistence decisions, remote desktop performance, and credentials governance.

Governance risk: Medium to high unless access, secrets, artifacts, and shutdown policy are tightly controlled.

Estimated role in OURSELF topology: Strong future worker model after governance and cost controls are decided.

Launch suitability: Good for production later.

### 6. EC2 / AWS GPU worker

Summary: AWS GPU infrastructure becomes the explicit worker environment.

Strengths: Mature infrastructure, strong scalability, IAM controls, repeatable provisioning potential, and artifact storage options.

Weaknesses: Operational complexity, billing risk, AWS-specific security surface, setup burden, and steeper beginner management.

Governance risk: Medium to high without strict IAM, budget alerts, secret boundaries, and proof review.

Estimated role in OURSELF topology: Strong governed infrastructure candidate after a decision pass defines account, access, budget, storage, and shutdown law.

Launch suitability: Good for production later.

### 7. Shadow / Parsec-style remote machine

Summary: A remote desktop machine with GPU capacity provides fast access to a high-power workstation experience.

Strengths: Fast setup, strong remote access quality, easier beginner experience, useful for visual Unreal work, and less hardware acquisition burden.

Weaknesses: Platform dependency, limited infrastructure control, unclear artifact persistence, provider security posture, and possible performance variability.

Governance risk: Medium. It may be excellent for access but weaker for formal proof, artifact custody, and secret discipline.

Estimated role in OURSELF topology: Strong near-term exploration candidate if no dedicated workstation exists.

Launch suitability: Good for prototype.

### 8. Hybrid: local command console + remote GPU/workstation node + artifact storage

Summary: The local Mac governs, a GPU-backed worker builds/renders, and artifacts return through a controlled storage/proof path.

Strengths: Best alignment with sealed topology, strong separation of authority and labor, scalable, proof-friendly, and durable if artifact storage and access are governed.

Weaknesses: More decisions before launch, setup complexity, requires clear storage policy, and needs explicit security boundaries.

Governance risk: Low to medium when configured correctly. High only if remote Git write access, secrets, or deployment authority are granted too early.

Estimated role in OURSELF topology: Best target architecture.

Launch suitability: Good for private beta.

## 6. Rejected: Raspberry Pi / Compute Module

Raspberry Pi / Compute Module is rejected for UREEL / Unreal topology. It is not the Unreal worker, not a control helper, not an edge relay, not a kiosk node, not a bridge, and not a future fallback for this lane. The topology requires a real workstation or GPU-backed worker capable of carrying Unreal storage, build, render, compile, and simulation pressure.

This rejection is total for Lane A. It must not re-enter as an option, helper, edge node, relay, control appliance, kiosk, bridge, future candidate, or fallback.

## 7. Recommended near-term path

Best near-term path: Local Mac remains command console. Unreal should live on either a dedicated Windows workstation, a remote GPU workstation, or a Shadow/Parsec-style remote machine. External SSD may help local storage, but it does not solve GPU/render/compile pressure by itself. Raspberry Pi / Compute Module is fully rejected for this topology.

Practical first branch:

1. If budget and physical setup allow it, choose a dedicated Windows workstation.
2. If speed matters more than ownership, test a Shadow/Parsec-style remote machine.
3. If infrastructure rigor matters more than beginner simplicity, evaluate a cloud GPU instance or EC2 / AWS GPU worker.
4. If no remote worker is available yet, use external SSD only as temporary storage relief, not as the final topology.

## 8. Recommended no-go options

No-go for first serious Unreal worker:

- Local Mac + external SSD only.
- Any topology that turns the local Mac into the main render factory.
- Any topology that grants remote Git write access before proof review.
- Any topology that places raw production credentials in Unreal project files.
- Any topology that deploys directly from worker node output.
- Any topology outside the evaluated candidate list.

Temporary only:

- Local Mac command console + external SSD Unreal workspace.

Production-later only:

- Cloud GPU instance.
- EC2 / AWS GPU worker.

## 9. Questions before purchase/provisioning

Before purchase or provisioning, answer:

- What is the target Unreal version?
- What platform must the first build target: Windows, Mac, web stream, packaged desktop, or internal prototype?
- Is the first objective editing, compiling, rendering, Pixel Streaming, packaged build output, or visual exploration?
- What storage size is required for project source, assets, derived data cache, builds, and artifacts?
- What budget ceiling applies per month or per hardware purchase?
- Who has physical or account access to the worker?
- Will the worker ever receive secrets?
- Will the worker have read-only Git access, no Git access, or separately authorized write access?
- Where do candidate artifacts return for review?
- How will failed builds be logged and preserved?
- What must be true before any deployment is allowed?

## 10. Security and proof boundary

Remote worker builds; it does not govern.

Repo remains proof body.

Human_TURN remains authority.

Worker output is candidate until reviewed and sealed.

No secrets on remote worker unless explicitly authorized.

No raw production credentials in Unreal project files.

No remote push without Human_TURN authorization.

No deployment from worker node without proof review.

UREEL remains downstream of canonical proof events.

UWebBrowser remains a bridge, not authority.

Unreal renders embodiment; it does not own truth.

Bubble/web remains logic and state interaction.

Remote topology must reduce local hardware strain without weakening governance.

## 11. Next authorized gate

The next authorized gate is a remote worker selection decision pass.

That pass should choose one near-term direction from:

- dedicated Windows workstation
- remote GPU workstation
- Shadow / Parsec-style remote machine
- cloud GPU or EC2 / AWS GPU worker after governance/cost review

No build begins from this matrix alone.

