# ENGINE-AS-NODE DOCTRINE

## GUI Systems as Callable Execution Infrastructure

---

## Canonical Doctrine Statement

SELF does not worship tools.
SELF exposes execution surfaces, wraps them in command law, records provenance, and converts intention into inspectable artifacts.

---

## Prime Technical Claim

Unreal Engine is treated as a callable visual execution node, not a mystical manifestation engine.

---

## Reverse-Engineering Correction

**Invalid claim:**
> "I manifested Unreal through terminal."

**Valid claim:**
> "I exposed Unreal's automation surface and positioned it as a commandable node in the SELF visual graph."

The distinction is not semantic. It is the difference between superstition and command.

---

## Seven Node Conditions

A tool becomes a node when:

1. its execution surface is named and documented;
2. its operations are expressible as structured commands;
3. its outputs carry provenance;
4. its artifacts carry claim classifications;
5. its access is governed by an adapter with defined boundaries;
6. its actions are logged before and after execution;
7. its role in the larger graph is precisely positioned.

Until all seven conditions are met, the tool is not a node. It is an unexposed dependency.

---

## Unreal Automation Surface Map

### Unreal Editor GUI

**What it does:** Visual authoring environment for scenes, assets, Blueprints, lighting, sequencer, and level design.

**Invocation surface:** Direct mouse/keyboard interaction. No programmatic surface without additional tooling.

**SELF use:** Scene visualization, manual prototype review, approval checkpoint before automation.

**Boundary/risk:** GUI-only actions are not auditable at the command level. Any action taken here must be replicated via automation before it is considered sealed.

---

### .uproject Files

**What it does:** JSON project descriptor. Declares engine version, enabled plugins, and target platforms.

**Invocation surface:** Text file. Editable directly. Referenced by all Unreal CLI commands as the entry point.

**SELF use:** Version-lock enforcement, plugin governance, project identity anchor.

**Boundary/risk:** Silent plugin drift. Engine version mismatch. Must be diff-tracked in git.

---

### UnrealEditor Command Line

**What it does:** Launches the full Unreal Editor with optional flags for game mode, specific maps, or scripted startup.

**Invocation surface:**
```
/path/to/UnrealEditor MyProject.uproject [flags]
```

**SELF use:** Launching editor in a controlled state, triggering map loads, passing startup arguments to automation-ready projects.

**Boundary/risk:** Full GUI is still launched. Not headless. Resource intensive.

---

### UnrealEditor-Cmd

**What it does:** Headless variant of the Unreal Editor. Runs commandlets and automation without opening the GUI.

**Invocation surface:**
```
/path/to/UnrealEditor-Cmd MyProject.uproject -run=CommandletName [args]
```

**SELF use:** Batch operations, asset cooking, headless script execution, CI pipeline steps.

**Boundary/risk:** Not all commandlets are stable. Must test on target platform before treating as production node.

---

### AutomationTool / BuildCookRun

**What it does:** Epic's UAT (Unreal Automation Tool). Handles build, cook, package, and run pipelines for any target platform.

**Invocation surface:**
```
RunUAT.sh BuildCookRun -project=MyProject.uproject -platform=Mac -clientconfig=Development
```

**SELF use:** Automated build verification, packaged output generation, CI artifact production.

**Boundary/risk:** Long-running. Requires significant storage and GPU resources. Must define output artifact paths explicitly.

---

### Commandlets

**What it does:** Unreal's internal scripted task system. Commandlets are C++ or Python classes that run in headless Unreal context.

**Invocation surface:**
```
UnrealEditor-Cmd MyProject.uproject -run=MyCommandlet
```

**SELF use:** Asset operations, data migrations, custom batch jobs, metadata extraction.

**Boundary/risk:** Commandlet quality varies. Undocumented commandlets may crash or produce inconsistent output.

---

### Python Scripting

**What it does:** Unreal exposes a Python API via the Python Editor Script Plugin. Scripts can manipulate assets, actors, materials, and project settings from within the editor or headlessly.

**Invocation surface:**
```
UnrealEditor-Cmd MyProject.uproject -ExecutePythonScript="path/to/script.py"
```

**SELF use:** Asset automation, scene construction, metadata tagging, export pipelines.

**Boundary/risk:** Requires Python Editor Script Plugin enabled. API coverage is incomplete. Some operations only work in GUI context.

---

### Blueprints

**What it does:** Unreal's visual scripting system. Event-driven logic graphs attached to actors and systems.

**Invocation surface:** GUI-primary. Blueprints can be called from C++ or triggered from commandlets with setup.

**SELF use:** Rapid prototyping of in-scene behavior without C++. Approval-gate visualization.

**Boundary/risk:** Not source-inspectable as plain text. Blueprint diffs require Unreal tooling. Automation of Blueprint changes is limited.

---

### Sequencer

**What it does:** Unreal's cinematic and animation timeline. Controls camera movement, actor animations, VFX, and rendered output sequences.

**Invocation surface:** GUI-primary, but can be triggered via Python or commandlet with a loaded sequence asset.

**SELF use:** Rendering distinction-driven cinematic sequences. Evidence artifact production. Scene proof capture.

**Boundary/risk:** Render quality and timing depend on hardware. Headless Movie Render Queue support requires specific plugin and version configuration.

---

### Asset Pipeline

**What it does:** Import, processing, LOD generation, and organization of 3D models, textures, audio, and other media into Unreal's content system.

**Invocation surface:** GUI import dialogs, or Python scripts using `unreal.AssetImportTask`.

**SELF use:** Controlled ingestion of approved visual assets tied to specific distinctions.

**Boundary/risk:** Uncontrolled asset sprawl is a primary risk. Every imported asset must be provenance-tagged. No asset enters the project without a linked source distinction.

---

### Headless Rendering / CI Possibilities

**What it does:** Using Movie Render Queue in headless mode or via command line to produce renders without opening the full editor GUI.

**Invocation surface:** Experimental. Requires Movie Render Queue plugin, configured render settings, and a sequence asset.

```
UnrealEditor-Cmd MyProject.uproject -MovieSceneCaptureType=/Script/MovieSceneCapture.AutomatedLevelSequenceCapture ...
```

**SELF use:** CI-triggered render production. Automated proof artifact generation from sealed scenes.

**Boundary/risk:** Stability varies by engine version. Mac headless GPU rendering has known limitations. Must verify on target hardware before treating as production.

---

### MCP Plugin Bridge

**What it does:** An MCP (Model Context Protocol) server plugin for Unreal that exposes editor operations as tool calls accessible to AI agents.

**Invocation surface:** MCP server running alongside Unreal Editor. Claude or other agents call tools via MCP protocol.

**SELF use:** Agent-commanded visual operations. Scene manipulation, asset queries, render triggers — all mediated through a governed tool surface.

**Boundary/risk:** MCP is a bridge. It does not prove truth. It executes approved operations and returns proof artifacts. Agent must not treat MCP responses as canonical memory. All MCP calls must be logged.

---

## SELF Control Graph

```
Intent Layer
    — raw distinction, language, doctrine statement

Semantic Layer
    — classified intent: visual / computational / ledger / governance

Translation Layer
    — scene brief, command specification, parameter set

Execution Layer
    — Unreal MCP / CLI / Python invocation

Artifact Layer
    — render, screenshot, export file, metadata package

Ledger Layer
    — Supabase evidence_artifacts row, audit_events row

Governance Layer
    — human approval gates, claim classification, rollback boundaries
```

No layer may be skipped.
No artifact may enter the ledger without passing through the governance layer.

---

## Command Surface Laws

1. No GUI-only dependency when automation exists.
2. Every visual action must be expressible as a structured operation.
3. Every operation must have: input, output, proof, rollback.
4. Every render must have provenance.
5. Every generated artifact must declare its state: symbolic, simulated, or evidence-linked.
6. Agent commands must be inspectable before execution.
7. No autonomous visual mutation without human approval.

---

## Unreal MCP Positioning

MCP is a bridge, adapter, and agent tool surface.

MCP is not canonical memory.

MCP does not prove truth.

MCP executes approved visual operations and returns proof artifacts.

The agent proposes. The human approves. MCP executes. The ledger records.

---

## SELF Visual Execution Pipeline

```
AXIOM distinction
  → visual doctrine classifier
  → scene brief
  → human approval
  → Unreal MCP / CLI execution
  → render capture
  → artifact metadata
  → Supabase evidence_artifacts row
  → audit_events row
  → link back to distinction / event / review
```

Every step is required. No short-circuit to ledger without execution proof. No execution without approval.

---

## Reverse Engineering Methodology

When approaching any GUI system as a potential node:

```
surface audit
  → separate GUI affordance from programmatic capability
  → find CLI / API / SDK / script / plugin entrypoints
  → build minimal invocation
  → capture proof
  → wrap in controlled adapter
  → add ledger / audit memory
  → promote to doctrine only after proof
```

Doctrine promotion requires observed execution, not theoretical capability.

---

## Allowed / Forbidden Language Table

| Forbidden | Allowed |
|-----------|---------|
| The system manifested itself. | Unreal is a callable execution node. |
| Unreal obeys SELF metaphysically. | We exposed an automation surface. |
| The render proves reality. | The render is a symbolic proof artifact. |
| The agent can autonomously create truth. | The pipeline compresses intent into executable operations. |
| Simulation equals evidence. | The agent proposes and executes only through approved tools. |
| | The ledger records provenance. |

Language shapes belief. Belief shapes command. Command shapes state. Use precise language.

---

## Technical Pass Roadmap

| Pass | Name | Objective |
|------|------|-----------|
| A | Unreal Surface Audit | Document all accessible automation surfaces in the installed Unreal version |
| B | Unreal MCP Sandbox | Stand up MCP plugin, verify tool surface, log first successful tool call |
| C | Scene Command Grammar | Define structured command vocabulary for scene operations |
| D | Visual Distinction Renderer | Map one AXIOM distinction to one rendered scene proof |
| E | Evidence Artifact Link | Connect rendered artifact to Supabase evidence_artifacts and audit_events |
| F | Cinematic Proof Sequence | Produce a full Sequencer-driven proof sequence from a sealed distinction |

No pass advances without proof of the prior pass.

---

## Risk Register

| Risk | Classification | Mitigation |
|------|---------------|------------|
| Engine version mismatch | Technical | Pin version in .uproject. Test CLI on target version before automation. |
| Plugin instability | Technical | Test each plugin in isolation. Never enable untested plugins in production project. |
| Mac compatibility limits | Platform | Verify headless rendering support on Mac before CI integration. |
| GPU / storage demands | Resource | Baseline GPU and disk before scheduling render jobs. |
| Uncontrolled asset sprawl | Governance | Every asset import requires linked source distinction ID. |
| Hallucinated tool commands | Agent | All agent commands pass human review before execution. Log all invocations. |
| Agent overreach | Governance | Define explicit permission scope per MCP tool. No autonomous mutation. |
| False proof claims | Integrity | Artifact classification must declare: symbolic / simulated / evidence-linked. Never conflate. |
| Secret leakage | Security | No secrets in project files. No secrets in render metadata. No secrets in audit logs. |
| MCP server trust boundary | Security | MCP server treated as untrusted bridge. All outputs validated before ledger entry. |
| CI cost | Resource | Render jobs are gated. No automated render without explicit trigger and approval. |
| Unreal licensing threshold | Legal | Monitor seat count and usage against Epic licensing terms before scaling. |

---

## Minimum Viable Proof

**Input:** one plain text distinction.

**Process:** approved scene brief.

**Execution:** one local Unreal scene action through safe bridge.

**Output:** one screenshot or render.

**Proof record must include:**
- timestamp
- command log
- project path
- artifact path
- source distinction ID
- claim boundary (symbolic / simulated / evidence-linked)

This is the floor. Below this, no render claim is valid.

---

## Final Law

Intent without execution is fantasy.
Execution without interface is friction.
Interface without audit is chaos.
Audit without memory is loss.
Memory without doctrine is noise.
Doctrine with command becomes system.

---

*Sealed: ENGINE-AS-NODE DOCTRINE — RUORA doctrine layer*
