# UREEL UNREAL-002 Execution Gate 0003 Unreal Project Location Authorization Checklist 0001

## Status
gate_authorization_checklist_id: UREEL-UNREAL-002-EXECUTION-GATE-0003-UNREAL-PROJECT-LOCATION-AUTHORIZATION-CHECKLIST-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0003-UNREAL-PROJECT-LOCATION
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_human_decision_id: UREEL-UNREAL-002-EXECUTION-GATE-0003-UNREAL-PROJECT-LOCATION-HUMAN-DECISION-0001
gate_status: GATE_0003_PROJECT_LOCATION_AUTHORIZED_BY_HUMAN_TURN
checklist_status: CHECKLIST_CAPTURED_NOT_PROJECT_CREATION
actual_location_selection_status: NOT_STARTED
project_creation_status: NOT_AUTHORIZED
asset_creation_status: NOT_AUTHORIZED
code_mutation_status: NOT_AUTHORIZED

## Checklist Purpose
This checklist defines the constraints for a later Gate 0003 project-location execution pass.
This checklist does not create a project.

## Source Basis
Gate 0002 proof report found:
- Epic Games Launcher installed at /Applications/Epic Games Launcher.app
- Unreal Engine already present at /Users/Shared/Epic Games/UE_5.7/Engine/Binaries/Mac/UnrealEditor.app
- no project files created
- no Unreal assets created
- no code mutation occurred
- MASTER_BLUEPRINT.md remained unchanged
- repo status remained clean
Gate 0003 Human_TURN decision authorized the project-location path only.

## Canonical Location Selection Constraints
A later Gate 0003 execution pass may only select a project location that:
- has enough free storage for the intended Unreal workspace
- is writable by the current user
- is recoverable by a documented rollback path
- does not require creating a project file to define the location
- preserves a clear relationship to RUORA
- avoids mutating code or assets during location selection

## Location Evaluation Areas
The later Gate 0003 execution pass may inspect only:
- canonical parent directory options
- storage volume and free capacity
- ownership and permissions
- backup and restore feasibility
- naming convention compatibility
- relationship to RUORA

## Forbidden During Later Execution
The later Gate 0003 execution pass may not:
- create an Unreal project
- create Unreal assets
- create .uproject files
- mutate RUORA code
- mutate MASTER_BLUEPRINT.md
- install packages
- call APIs
- deploy anything
- mutate Bubble/schema/cloud resources
- create evidence/ureel/intake paths
- attach raw evidence artifacts to RUORA
- create worktrees
- create remotes
- push
- open PRs

## Required Proof Output
The later Gate 0003 execution pass must return:
1. repo root
2. HEAD before location pass
3. git status before location pass
4. remotes count
5. MASTER_BLUEPRINT.md drift check
6. canonical parent directory options
7. storage and capacity result
8. permissions result
9. backup/restore feasibility result
10. naming compatibility result
11. relationship-to-RUORA result
12. no project creation confirmation
13. no asset creation confirmation
14. no code-mutation confirmation
15. no package/API/deploy/cloud/Bubble/schema mutation confirmation
16. no raw evidence artifact confirmation
17. no evidence path confirmation
18. final git status
19. recommended next gate

## Execution Boundary
This checklist authorizes no project-location execution by itself.
Before any location selection runs, Human_TURN must separately approve the Gate 0003 execution pass.

## Next Required File
The next lawful file after this checklist is sealed is:
doctrine/intake/UREEL-UNREAL-002-EXECUTION-GATE-0003-UNREAL-PROJECT-LOCATION-EXECUTION-PASS-0001.md

## Decision Outcome
GATE_0003_AUTHORIZATION_CHECKLIST_CAPTURED_NOT_PROJECT_CREATION
