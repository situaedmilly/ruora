# UREEL UNREAL-002 Execution Gate 0009 Unreal Departure Authorization Checklist 0001

## Status
gate_authorization_checklist_id: UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT-AUTHORIZATION-CHECKLIST-0001
gate_id: UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT
candidate_name: UREEL-OURSELFCLOUD-NODE-0
source_gate_human_decision_id: UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT-HUMAN-DECISION-0001
departure_authorization_status: DEPARTURE_BASELINE_NOT_NEEDED
checklist_status: CHECKLIST_CAPTURED_NOT_EXECUTED
actual_departure_status: NOT_STARTED
artifact_departure_status: CONTAINED
distribution_status: PRIVATE
public_visibility_status: NONE

## Checklist Purpose
This checklist defines the exact read-only verification actions for Gate 0009 when no departure baseline is needed.

This checklist does not package, cook, build, sign, export, release, distribute, or deploy anything.

## Source Basis
Gate 0009 Human_TURN decision found:
- Gate 0008 closed as NO_CONNECTION_BASELINE_NEEDED
- the project remains fully contained
- no packaging, cooking, build, export, distribution, or hosted deployment has occurred for UREEL-OURSELFCLOUD-NODE-0
- no shippable executable artifact, store submission, hosted instance, or distributable release artifact currently exists
- repo status remained clean
- MASTER_BLUEPRINT.md remained unchanged

Gate 0009 decision brief found:
- Gate 0009 governs Departure Authorization: whether the project may cross the containment boundary established during development
- containment precedes distribution
- a build is not a departure
- publication is evidence of authorization, not authorization itself
- no departure baseline is needed at this time

## Authorized Verification Areas
The later Gate 0009 execution pass may verify only:

1. packaging settings
2. cook targets
3. build targets
4. distribution profiles
5. store manifests
6. signing identities
7. certificates
8. provisioning profiles
9. generated artifacts
10. executable outputs
11. installer outputs
12. archive outputs
13. hosted targets
14. release targets
15. distribution targets
16. public visibility
17. containment status
18. repo root, HEAD, working tree state, remotes, and MASTER_BLUEPRINT.md drift

## Approved Read-Only Command Classes
Only read-only verification commands are permitted.

Allowed examples:

- `find` for packaging, export, signing, hosting, or release presence only
- `grep` for packaging, export, signing, hosting, or release markers only
- `sed -n` on manifest or configuration files only
- `stat` on discovered files only
- `ls` on project directories only
- `defaults read` on macOS configuration files only
- `plutil` for read-only plist inspection only
- `codesign -d` for signature inspection only
- `xcrun --show-sdk-path` for SDK path inspection only
- `git status`
- `git rev-parse`

## Forbidden Command Classes
The Gate 0009 execution pass may not run commands that:

- package software
- cook builds
- create executables
- create archives
- sign artifacts
- upload artifacts
- publish releases
- deploy hosted services
- build Docker images
- create installers
- mutate code
- call external APIs
- mutate Bubble/schema/cloud resources
- attach raw evidence artifacts to RUORA
- create remotes
- push
- open PRs

## Forbidden Concrete Actions
The Gate 0009 execution pass must not:

- package
- cook
- build
- archive
- export
- sign
- upload
- release
- publish
- deploy
- stream-host
- create installers
- create packaged binaries
- create DMG, EXE, IPA, APK, Docker, or OCI outputs
- mutate `MASTER_BLUEPRINT.md`
- create evidence/ureel/intake paths

## Required Proof Output
The later Gate 0009 execution pass must return:

1. repo root
2. HEAD before verification pass
3. git status before verification pass
4. remotes count
5. MASTER_BLUEPRINT.md drift check
6. packaging settings result
7. cook targets result
8. build targets result
9. signing assets result
10. provisioning assets result
11. certificates result
12. generated artifacts result
13. executable outputs result
14. installer outputs result
15. archive outputs result
16. hosted targets result
17. release targets result
18. distribution targets result
19. public visibility result
20. containment status result
21. final git status
22. recommended next gate

## Execution Boundary
This checklist authorizes no departure by itself.

Before the later verification runs, Human_TURN must separately approve the Gate 0009 execution pass.

## Next Required File
The next lawful file after this checklist is sealed is:
doctrine/intake/UREEL-UNREAL-002-EXECUTION-GATE-0009-UNREAL-DEPLOYMENT-EXPORT-EXECUTION-PASS-0001.md

## Decision Outcome
GATE_0009_DEPARTURE_AUTHORIZATION_CHECKLIST_CAPTURED_NOT_EXECUTED
