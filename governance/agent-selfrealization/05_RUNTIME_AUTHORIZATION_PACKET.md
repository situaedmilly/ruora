# 05_RUNTIME_AUTHORIZATION_PACKET

**Suite status:** CANDIDATE — not ratified, not runtime-enforced.
**Protocol version:** `ourself.agent-selfrealization.v1`

## Purpose

The bridge document between an accepted `selfrealization_record` (Chamber I)
and `06_RUNTIME_FLOW.md` (Chamber II). Issued by whichever party holds
authorizing power for the gate in question (Founder, or a Governor-realized
agent holding recommend authority that Founder has accepted) — never
self-issued by the agent that produced the SELFREALIZATION record.

## Authority granted by this document

The document *is* the grant mechanism — but it can only narrow, never
widen, what the accepted `selfrealization_record` already declared. See
the binding rule below.

## Binding rule

**This packet must not grant broader authority than the completed
SELFREALIZATION record.** For every authority dimension in
`03_SELFREALIZATION_SCHEMA.yaml`'s `authority` object, this packet's
corresponding field must be `GRANTED` only if the `selfrealization_record`
also has that dimension `GRANTED`. The packet may further restrict (e.g.
grant `execute` narrower in scope than the record allowed) but never
expand.

## Required fields

```
OURSELF · RUNTIME AUTHORIZATION

SELFREALIZATION RECORD
  Reference:                <session_id + evaluated_at of the accepted record>
  Accepted:                 <true|false>

RUNTIME STATUS
  <AUTHORIZED | NOT_AUTHORIZED>

AUTHORIZED GATE
  <gate identifier>

REALIZED AGENT IDENTITY
  <identity block, copied from the accepted selfrealization_record —
   not re-declared or re-guessed>

ROLE CONSTITUTION
  <the exact 04_ROLE_CONSTITUTIONS/*.md file this agent is bound by>

ENVIRONMENT WITNESS
  <environment block, copied from the accepted selfrealization_record>

GOVERNING CONSTITUTION
  <which durable_doctrine / project_instructions / task_authorization
   entries apply to this gate specifically>

OBJECTIVE
  <one exact state transition>

READ SCOPE
  <authorized inspection boundaries>

WRITE SCOPE
  <exact writable paths or systems — must be a subset of
   selfrealization_record.environment.writable_boundaries>

TOOL SCOPE
  <exact tools this gate may invoke>

NETWORK SCOPE
  <NONE | explicit allow-list of reachable destinations>

FORBIDDEN SCOPE
  <everything excluded, stated explicitly, not left as "everything else">

EXECUTION CLASS
  [inspect | test | build | git-read | git-write-local |
   project-mutation | dispatch | deploy | other governed class]

TIME / SESSION SCOPE
  Issued at:               <UTC timestamp>
  Expires at:              <UTC timestamp or explicit NEVER — NEVER
                             requires its own separate justification>
  Session binding:         <this packet is valid only for the session_id
                             named above; it does not survive a new session>

REQUIRED PREFLIGHT
  [commands, checks, witnesses that must run before EXECUTION begins]

REQUIRED VERIFICATION
  [tests, assertions, diffs, schemas, external confirmation required
   before SEAL_OR_HOLD]

ROLLBACK / REFUSAL BEHAVIOR
  <what this agent must do if a step cannot be safely completed —
   default is stop and report, never improvise a substitute action>

EVIDENCE OBLIGATIONS
  <exactly which artifacts this gate must produce for
   07_EXECUTION_WITNESS_SCHEMA.yaml>

COMMIT AUTHORITY
  [denied | local-only | explicitly authorized]

SEAL AUTHORITY
  [denied | recommend-only | explicitly authorized]

STOP CONDITIONS
  [list]

DELIVERABLE
  [exact output artifact]

ISSUING AUTHORITY
  <who/what issued this packet — must hold authorizing power for this
   gate; an agent may never issue its own packet>

AUTHORIZATION REFERENCE
  <a receipt/reference id tying this packet to the Governor ruling or
   Founder decision that authorized it>

Begin RUNTIME_BOOT.
```

## Refusal / HOLD conditions

- Any field in this packet grants an authority dimension the accepted
  `selfrealization_record` marked `DENIED` → the packet itself is invalid;
  reissue it correctly rather than proceeding.
- `Expires at` has passed → the packet is void; `06_RUNTIME_FLOW.md`
  §09 (`RUNTIME_BOOT`) must refuse with `RUNTIME_BOOT_CONFLICT`.
- `Session binding` does not match the current session → void, same
  refusal.
- No `AUTHORIZATION REFERENCE` is present → the packet cannot be
  distinguished from a self-issued claim; treat as not authorized.

## Launch-state footer

This packet, once accepted by `06_RUNTIME_FLOW.md` §09, becomes the
`RUNTIME_AUTHORIZATION` binding referenced throughout Chamber II and cited
in the eventual execution witness and handoff.
