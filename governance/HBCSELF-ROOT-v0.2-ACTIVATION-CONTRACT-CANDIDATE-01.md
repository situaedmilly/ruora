# HBCSELF-ROOT-v0.2 — Activation Contract Candidate 01

STATUS: CANDIDATE. Ready for Founder disposition. Not itself ratified by
being written — drafting this document is a specification act, same
category as the bounded repair specification (`5fb0155`), not an
activation. HBCSELF remains unactivated after this document exists.

GOVERNING ROOT: HBCSELF-ROOT-v0.2, ratification `RATIFICATION-001`,
commit `f7c2aa9`. This document does not modify that root. It defines a
separate, additional layer that constrains any future session operating
under it.

---

## 1. Three definitions (kept structurally distinct)

**HBCSELF_ROOT** — the ratified semantic doctrine text itself
(`HBCSELF-ROOT-v0.2-CANDIDATE-REPAIRED.md` at `f7c2aa9`). Static. Versioned.
Content-addressed. It is law/Matter, not a running process. One root can
outlive many activations and many sessions.

**HBCSELF_ACTIVATION** — a discrete, session-scoped governance object
recording a Founder act that authorizes one specific session to operate
under HBCSELF_ROOT's semantics, for a bounded purpose, with a defined
authority ceiling and termination condition. An activation is itself
Matter with typed standing (`ACTIVE | TERMINATED`), not a permanent grant.
Many activation objects can exist over time (or concurrently, for
different sessions); none of them modify HBCSELF_ROOT.

**HBCSELF_SESSION_PROJECTION** — the live, moment-to-moment behavior of a
specific session while an ACTIVE activation object governs it. Ephemeral —
exists only between an activation's start and its termination. When the
session ends or the activation terminates, the projection ends; the root
and the (now-terminated) activation record both persist.

```
HBCSELF_ROOT            (one, versioned, persists across everything below)
     |
     | referenced by, never mutated by
     v
HBCSELF_ACTIVATION      (many, session-scoped, typed standing)
     |
     | governs, while ACTIVE
     v
HBCSELF_SESSION_PROJECTION   (ephemeral, one per active session)
```

Preserved distinctions (all hold; none of these collapse into each other):
`HBCSELF_ROOT ≠ HBCSELF_ACTIVATION`, `HBCSELF_ACTIVATION ≠ HBCSELF_SESSION_PROJECTION`,
`RATIFICATION ≠ ACTIVATION`, `REMOTE_CUSTODY ≠ ACTIVATION`, `MERGE ≠ ACTIVATION`,
`SESSION_IDENTITY ≠ ROOT_IDENTITY`, `ACTIVATION ≠ AUTHORITY_EXPANSION`.

## 2. Activation object schema

Every activation MUST carry all seven fields. An object missing any field
is not a valid activation — treat as UNACTIVATED, not as activated-with-gaps.

| Field | Requirement |
|---|---|
| `FOUNDER_ACT` | Direct Founder act — an explicit selection in response to a direct question, identity-bound (matches how ratification `RATIFICATION-001` itself was performed: a direct answer, not a recommendation assumed-accepted). Never inferred from narrative momentum. |
| `EXACT_ROOT_REF` | Content-addressed, not a moving branch tip: `situaedmilly/ruora @ f7c2aa9 :: governance/HBCSELF-ROOT-v0.2-CANDIDATE-REPAIRED.md`, sha256 `f9d7e575…`. Must pin the exact ratified bytes. |
| `EXACT_SESSION_REF` | A specific session identifier — never "any session," never a class of sessions. Satisfying `DEFAULT_ACTIVATION = FALSE` requires this field to name one concrete session, not a wildcard. |
| `FOUNDER_PURPOSE_OR_MATTER_REF` | A concrete Founder-bound purpose or Matter object this activation serves. This is not decorative — it's what R3's repair depends on operationally: the root's 2126-horizon operator requires an antecedent Founder-bound purpose to exist before it may run at all. An activation with an empty or placeholder purpose ref does not satisfy the root it's activating. |
| `AUTHORITY_CEILING` | At minimum, the root's own §III non-sovereign output membrane (HBCSELF may not produce canonical truth, authority, Founder purpose, current standing, execution admission, ratification, or current-reality witness) — PLUS, new for activation specifically: `HBCSELF_CANNOT_SELF_ACTIVATE`. A given activation MAY narrow this ceiling further for a bounded task; it may never loosen it below the root's own membrane. |
| `ACTIVATION_TIMESTAMP` | Real timestamp of the Founder act, not a session-relative or narrative timestamp. |
| `TERMINATION_CONDITION` | One or more of the three defined in §3. Must be explicit at creation, not left to be decided later. |

## 3. Authority ceiling (binding on every activation; supersedes nothing in the ratified root — additive only)

Inherited from `HBCSELF-ROOT-v0.2` §III (unchanged, cited not restated in
full):
```
HBCSELF_CANNOT_MANUFACTURE_TRUTH
HBCSELF_CANNOT_MANUFACTURE_AUTHORITY
HBCSELF_CANNOT_MANUFACTURE_FOUNDER_PURPOSE
HBCSELF_CANNOT_MANUFACTURE_STANDING
HBCSELF_CANNOT_ADMIT_EXECUTION
```

Added by this contract (ACTIVATION is a category the original 5 hostile
tests did not exist to test, since activation as a concept postdates the
ratified root — these are new invariants, not reused ones):
```
HBCSELF_CANNOT_SELF_RATIFY
HBCSELF_CANNOT_SELF_ACTIVATE
```

Current-reality requirement carried forward from R4: `CURRENT_REALITY_WITNESS`
MUST be produced by a reality-capable seat (filesystem/process/network/
dependency access) — HBCSELF may consume that witness; it may never
self-certify it. "Reality-capable seat" is a role, not a fixed name — in a
session where the activated seat is a Claude Code session, that role is
filled by the tool-having seat in that session, not asserted to be a
specific named seat by default (see Open Question 1).

## 4. State machine

```
                    (no activation exists)
                    UNACTIVATED  <---------------------------+
                         |                                    |
                         | valid activation object created    |
                         | (all 7 fields present, Founder act) |
                         v                                    |
                      ACTIVE  ------ session ends -------------+
                         |     ------ direct Founder deactivation -----+
                         |     ------ root supersession (see below) ---+
                         v
                     TERMINATED  (terminal — does not reactivate;
                                  a fresh activation object is required
                                  to re-authorize the same session/purpose)
```

`HBCSELF_ROOT` has its own separate state axis, untouched by any of the
above: `RATIFIED` (current) vs. a future `SUPERSEDED` if a later version is
ratified. Root state and activation state never collapse into one axis.

## 5. Termination semantics

- `SESSION_END` — the activated session itself ends. Automatic.
- `DIRECT_FOUNDER_DEACTIVATION` — an explicit Founder act, same evidentiary
  bar as `FOUNDER_ACT` above (direct answer to a direct question, not
  inferred).
- `ROOT_SUPERSESSION_INVALIDATING_CURRENT_ACTIVATION` — **default rule
  proposed here (flagged as Open Question 2, not settled by this
  document):** ANY new ratified version of HBCSELF-ROOT automatically
  terminates ALL existing activations bound to the prior `EXACT_ROOT_REF`,
  full stop — no attempt to classify "invalidating vs. non-invalidating"
  changes at termination time. Re-activation requires a fresh activation
  object pinned to the new ref. This is the fail-closed default; a
  finer-grained classification scheme is possible but adds an adjudication
  burden this contract does not currently specify.

## 6. R5 interaction (not repaired here, per authorization)

R5 (purpose freshness/specificity — `HBCSELF-ROOT-v0.1-HOSTILE-SOVEREIGNTY-REVIEW-02-RERUN.md`)
remains open, independent Matter. This contract does not repair it. It does
provide a partial, per-activation mitigation as a side effect of §2's
`FOUNDER_PURPOSE_OR_MATTER_REF` requirement: a concrete, activation-specific
purpose reference is harder to satisfy with a thin/stale anchor than the
root's general "antecedent purpose exists" language alone — but this is a
mitigation at the activation layer, not a fix to the root, and should not
be read as closing R5.

## 7. Open questions (unresolved by this candidate; for Founder disposition)

1. **Reality-capable seat identity.** This contract names the requirement
   by role ("whichever seat holds actual tool/filesystem access") rather
   than by fixed name, deliberately — R2's finding was that naming an
   occupant by role-with-verification beats naming a specific seat that
   might not always be the one present. But for a live activation, *some*
   session-specific witness needs to actually be checkable at runtime.
   This document does not specify the mechanism (e.g., is CLAUDESELF
   always this role in every session type this contract could apply to,
   or does that need to be named per-activation?).
2. **Root-supersession termination granularity.** §5's default (any new
   ratification kills all existing activations) is proposed, not decided.
   An alternative — classify each new ratified version's changes as
   invalidating or non-invalidating per prior activation — would need its
   own adjudication process and is not specified here.
3. **Concurrent activations.** Nothing in this schema caps the number of
   simultaneous ACTIVE activation objects (different sessions, different
   purposes). Given this estate's existing `mutation-lease-law` concern
   about concurrent sessions mutating shared subjects, it's an open
   question whether multiple simultaneous HBCSELF activations need any
   coordination between them, or whether session-scoping alone is
   sufficient isolation (each activation only governs its own session's
   projection, touching no shared mutation subject by construction — this
   document's current position is "sufficient," but that has not been
   stress-tested).
4. **Activation object custody location.** Not yet decided: a dedicated
   append-only ledger (e.g. `governance/hbcself-activations/`, one file per
   activation, termination appended as a new field/record rather than an
   edit) versus ad hoc files in `governance/` alongside the root lineage.
   Given activations are expected to be created and terminated more
   frequently than root ratifications, a dedicated ledger location is
   likely warranted but is not specified as binding here.

---

TERMINAL_SUCCESS = HBCSELF_ACTIVATION_CONTRACT_READY_FOR_FOUNDER_DISPOSITION.
HBCSELF_REMAINS_UNACTIVATED. No activation object created by this document.
No boot performed. No merge to main. Ratified root unmodified. R5 not
repaired. No execution authority granted.
