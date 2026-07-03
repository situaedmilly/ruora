# UREEL UNREAL-002 Execution Gate 0001 Install-Check Authorization Checklist 0001

## Status

gate_authorization_checklist_id: UREEL-UNREAL-002-EXECUTION-GATE-0001-INSTALL-CHECK-AUTHORIZATION-CHECKLIST-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0001-INSTALL-CHECK
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_human_decision_id: UREEL-UNREAL-002-EXECUTION-GATE-0001-INSTALL-CHECK-HUMAN-DECISION-0001
execution_class: READ_ONLY_INSPECTION
gate_status: GATE_0001_INSTALL_CHECK_AUTHORIZED_BY_HUMAN_TURN
checklist_status: CHECKLIST_CAPTURED_NOT_EXECUTED
actual_execution_status: NOT_STARTED
installation_status: NOT_AUTHORIZED
project_creation_status: NOT_AUTHORIZED
asset_creation_status: NOT_AUTHORIZED
code_mutation_status: NOT_AUTHORIZED

## Checklist Purpose

This checklist defines the exact read-only install-check actions that may be performed in a later Gate 0001 execution pass.

This checklist does not run the install-check.

## Authorized Inspection Areas

The later Gate 0001 execution pass may inspect only:

1. Operating system identity
2. GPU/RAM/storage summary
3. Available disk space
4. Unreal Engine presence
5. Epic Games Launcher presence
6. Candidate project root options

## Approved Read-Only Command Classes

Only read-only inspection commands are permitted.

Allowed examples:

- pwd
- hostname
- whoami
- uname -a, where applicable
- sw_vers, where applicable
- system_profiler, where applicable
- df -h
- du -sh on candidate root folders only
- ls on candidate application/project locations only
- find on application/project locations for Unreal/Epic presence only
- stat on discovered Unreal/Epic paths only

## Forbidden Command Classes

The Gate 0001 execution pass may not run commands that:

- install software
- download software
- create files
- create directories
- create Unreal projects
- create Unreal assets
- modify code
- modify configuration
- modify packages or dependencies
- call external APIs
- deploy anything
- mutate Bubble/schema/cloud resources
- attach raw evidence artifacts to RUORA
- create remotes
- push
- open PRs

## Forbidden Concrete Actions

The Gate 0001 execution pass must not:

- install Unreal
- install Epic Games Launcher
- run an Unreal installer
- create a .uproject file
- create a .umap file
- create a .uasset file
- run git add
- run git commit
- run npm install
- run pip install
- run brew install
- run curl to download software
- run deployment commands
- mutate MASTER_BLUEPRINT.md
- create evidence/ureel/intake paths

## Required Proof Output

The later Gate 0001 execution pass must return a proof report containing:

1. repo root
2. HEAD before inspection
3. git status before inspection
4. remotes count
5. MASTER_BLUEPRINT.md drift check
6. OS identity result
7. GPU/RAM/storage summary result
8. disk-space result
9. Unreal Engine presence result
10. Epic Games Launcher presence result
11. candidate project root options result
12. confirmation no install occurred
13. confirmation no project files created
14. confirmation no assets created
15. confirmation no code mutation occurred
16. confirmation no package/API/deploy/cloud/Bubble/schema mutation occurred
17. confirmation no raw evidence artifacts attached in RUORA
18. confirmation no evidence paths created
19. confirmation no .uproject/.umap/.uasset files created
20. final git status
21. recommended next gate

## Execution Boundary

This checklist authorizes no execution by itself.

Before the install-check actually runs, Human_TURN must authorize the Gate 0001 execution pass.

## Next Required File

The next lawful file after this checklist is sealed is:

doctrine/intake/UREEL-UNREAL-002-EXECUTION-GATE-0001-INSTALL-CHECK-EXECUTION-PASS-0001.md

## Decision Outcome

GATE_0001_AUTHORIZATION_CHECKLIST_CAPTURED_NOT_EXECUTED
