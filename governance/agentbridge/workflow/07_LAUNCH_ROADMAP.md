# 07_LAUNCH_ROADMAP

**Document identifier:** `governance/agentbridge/workflow/07_LAUNCH_ROADMAP.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

The single authoritative, trailing task list for the path to AgentBridge
General Availability. Read at the start of every session
(`01_SESSION_BOOTSTRAP.md`) and regenerated at the end of every session that
closes a gate (`06_SEAL_OR_HOLD.md`). Never edited freehand mid-session to
reflect wished-for progress — only regenerated from an actual sealed gate.

## Authority granted

- Read by every document in this stack.
- Regenerated (fully rewritten, not hand-patched) immediately after a gate
  receives a verdict in `06_SEAL_OR_HOLD.md`.

## Authority explicitly not granted

- This document does not itself authorize any gate's execution — it names
  what is open; `03_GATE_SELECTION.md` is what selects.
- This document does not ratify constitutions. Ratification status shown
  here reflects decisions made elsewhere (Founder ratification, sealed
  gates) — it is a record, not the mechanism of ratification.
- Updating this document is not a substitute for running
  `06_SEAL_OR_HOLD.md` on the gate that justifies the update.

## Required inputs

Prior sealed-gate witnesses; current admitted-authority state as last
established by a sealed gate or Founder ratification.

## Required procedure

At the end of any session that closes a gate: regenerate this entire
document from the sealed-gate record, in order, without hand-editing
individual line items in place. Computed, not manual.

## Current state (as of this scaffold's creation)

### Completed

- SL-001 canonical kernel lineage
- SL-002 integration authorization
- SL-003 synchronous proof-path driver
- SL-004 durable storage root
- SL-005 PC-000001 git-read production proof
- SL-006 PC-000002 inspect production proof
- SL-007 cold-process multi-chain verification
- SL-008A bounded git-add implementation
- PC-000003 mutation success proof
- PC-000004 secret-path refusal proof
- PC-000005 at-most-once replay proof
- SL-008A operational stabilization
- LIMITED_SELFLAUNCH Founder ratification
- LIMITED_SELFLAUNCH operating-boundary publication
- Foundation Baseline BCP-000001 produced ephemerally

### Current admitted authority

- inspect
- git-read
- bounded single-target git-add

### Not admitted

- test-command
- git-commit
- bounded-file-write
- push
- arbitrary shell
- T-034 activation

### Open work, ordered

1. Persist BCP-000001 through a separately authorized narrow mutation gate.
2. Decide Runtime Publication Constitution.
3. Decide Runtime Tracking Policy in synchronization with publication law.
4. Define governance-publication lineage and registry verification.
5. Establish artifact schema identity/versioning rules.
6. Establish active-publication uniqueness: exactly one active publication
   per constitutional question.
7. Publish ratified runtime-governance baseline.
8. Begin ordinary LIMITED_SELFLAUNCH operational sessions.
9. Capture limited-adoption witnesses.
10. Cold-verify adoption proof chains.
11. Seal SL-009L.
12. Declare LIMITED_SELFLAUNCH operational.

### Parallel, non-blocking

13. Amend SL-008B test-command design.
14. Classify test-command as bounded repository-code execution.
15. Select effect-isolation model.
16. Bind test identity, manifest/script hash, executable, argv, working
    root, environment, timeout, output, and network policy.
17. Define independent witness and reconciliation proposition.
18. Founder review of amended design.
19. Separate SL-008B implementation authorization.
20. Regression, production success, refusal, replay, cold verification,
    stabilization, and seal.

### Later

21. Admit bounded git-commit.
22. Admit bounded-file-write.
23. Demonstrate complete edit → test → stage → commit workflow.
24. Capture multi-session unrestricted-adoption evidence.
25. Seal unrestricted SL-009.
26. FULL SELFLaunch.

## Required output — trailing regeneration

Every session that closes a gate ends by regenerating this list containing:

- completed gates;
- current gate;
- blockers;
- next recommended gate;
- all remaining steps until LIMITED_SELFLAUNCH;
- all remaining steps until FULL SELFLaunch.

### Trailing tasks until launch

- [ ] Complete the eight-file workflow scaffold
- [ ] Verify scope and full RUORA working-tree state
- [ ] Run a fresh-session workflow recovery test
- [ ] Persist BCP-000001 through a separate narrow mutation gate
- [ ] Ratify Runtime Publication Constitution
- [ ] Ratify synchronized Runtime Tracking Policy
- [ ] Establish governance registry and active-publication verification
- [ ] Publish the ratified runtime-governance baseline
- [ ] Begin ordinary LIMITED_SELFLAUNCH sessions
- [ ] Capture and cold-verify adoption evidence
- [ ] Seal SL-009L
- [ ] LIMITED_SELFLAUNCH

Parallel:

- [ ] Amend SL-008B bounded repository-code execution design
- [ ] Review, implement, and stabilize the admitted test primitive
- [ ] Admit bounded git-commit
- [ ] Admit bounded-file-write
- [ ] Prove the complete edit → test → stage → commit cycle
- [ ] Seal unrestricted SL-009
- [ ] FULL SELFLaunch

## Refusal / HOLD conditions

- This document is stale (does not match the most recent sealed-gate
  witness) → treat its "current gate" and "completed" sections as
  unverified until `02_SYNCHRONIZATION.md` reconciles them.
- A session attempts to hand-edit an individual roadmap line without a
  corresponding sealed gate → refuse; regeneration is computed from seal
  records, not narrative.

## Launch-state footer

This document *is* the launch-state footer referenced by every other
document in the stack. Its own trailing section above is restated,
verbatim, as the final output of every session that reaches
`06_SEAL_OR_HOLD.md`.
