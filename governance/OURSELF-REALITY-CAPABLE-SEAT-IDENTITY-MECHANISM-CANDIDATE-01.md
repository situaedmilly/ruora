# OURSELF — Reality-Capable Seat Identity Mechanism, Candidate 01

STATUS: CANDIDATE. Ready for Founder disposition. Does not create
`ACT-0001`, does not activate HBCSELF, grants no new execution authority.
`HBCSELF_ACTIVE_SESSIONS = 0` after this document exists, same as before it.

SCOPE: this is estate-general infrastructure (how OURSELF establishes that
*any* seat has observation capability over *any* reality surface), not a
HBCSELF-specific object. `HBCSELF-ROOT-v0.2-ACTIVATION-CONTRACT-CANDIDATE-01.md`
(§7, Open Question 1) references this mechanism rather than owning it —
other future consumers of "who can produce a valid witness" should be able
to bind to this without going through HBCSELF at all.

---

## 1. Why a grant object, not a name

Open Question 1 in the activation contract asked how to avoid hardcoding
"reality-capable seat = CLAUDESELF." Naming a seat by brand doesn't survive
contact with reality: a Claude session with no Bash/Read/Edit tools
attached has no more filesystem capability than HBCSELF does, despite
sharing an identity label. Capability has to be evidenced per-surface, per
seat-instance, not assumed from what a session is called.

```
SEAT_IDENTITY            ≠ OBSERVATION_CAPABILITY
MODEL_IDENTITY            ≠ TOOL_ACCESS
TOOL_ACCESS                 ≠ OBSERVABILITY
OBSERVABILITY                 ≠ AUTHORITY
WITNESS_CAPABILITY               ≠ WITNESS_VALIDITY
REALITY_CAPABLE_FOR_SURFACE_A       ≠ REALITY_CAPABLE_FOR_SURFACE_B
```

The last line matters as much as the first: capability is granted per
surface, not as a bloc. A seat with a Bash tool but no network egress is
`FILESYSTEM`-capable and `PROCESS`-capable, and is NOT automatically
`NETWORK`-capable just because it "has tools" generally.

## 2. `REALITY_CAPABILITY_GRANT` schema

| Field | Meaning |
|---|---|
| `grant_id` | Unique id, e.g. `RCG-<seat_ref>-<surface>-<sequence>`. |
| `seat_ref` | A specific, concrete session/seat identifier — never a role name, never a model/brand name. Must be checkable at issuance time (e.g. this Claude Code session's own identifier, not "ClaudeSELF" as a class). |
| `observable_surfaces` | One or more of the typed enum in §3. Each surface listed must be independently justified in this grant, not inherited from another surface's presence. |
| `permitted_instruments` | The actual mechanism used to observe each surface (e.g. "Bash: `git`, `shasum`, `find`", "Read tool", "WebFetch"). Ties the grant to real tool availability, not assumption. |
| `observability_contract_refs` | Pointers to whatever defines that instrument's actual limits (sandbox boundaries, denied paths, network allowlist, etc.). An instrument's reach is not assumed total just because it exists. |
| `authority_ceiling` | Explicit, always present: `WITNESS_CAPABILITY ≠ AUTHORITY`. Holding this grant authorizes observing and reporting only — never adjudicating, ratifying, or authorizing on the strength of having observed. |
| `issued_by` | The entity/process that actually configured this seat's tool access — for a Claude Code session, that's the harness plus the operator's permission configuration, a fact about the environment. Never the seat itself asserting its own access. |
| `issued_at` | Timestamp of when capability was *demonstrated* (§4), not merely when it was claimed. |
| `termination_or_expiry` | Required, never open-ended (§5). |

A grant missing any field is not a valid grant — same fail-closed
discipline as the activation object schema: partial ≠ granted.

## 3. Observable surfaces (typed)

```
FILESYSTEM
PROCESS
NETWORK
LOG
API
STATIC_ARTIFACT
HUMAN_UI
REMOTE_CONTROL_PLANE
OTHER_EXPLICITLY_DEFINED_SURFACE   (must be named, not left as a catch-all)
```

A `CURRENT_REALITY_WITNESS` composed of multiple propositions must cite,
per proposition, which surface and which specific grant it relied on. This
lets a witness be partially valid: e.g. FILESYSTEM claims backed by a real
grant, NETWORK claims absent because no grant covers that surface.

## 4. Issuance semantics

Two conditions, both required:

1. **Configuration fact.** The seat's tool access for the named surface is
   confirmed by the runtime/harness — an observable fact about how the
   session was set up, not a claim the seat makes about itself.
2. **Demonstrated observation.** At least one successful, logged
   invocation of the permitted instrument against a real observable target
   has occurred. Self-demonstration is evidence of capability, not
   authority to grant it — the grant still traces to condition 1. A seat
   asserting "I have Bash" without ever having run anything is
   `UNDEMONSTRATED`, not `GRANTED`.

## 5. Termination / expiry

- Session end (mirrors `HBCSELF_ACTIVATION`'s own `SESSION_END` condition,
  but this is a separate lifecycle — see §7 Open Question, not tied to
  HBCSELF specifically).
- Underlying tool access revoked or changed mid-session.
- Explicit Founder revocation.
- **Grants are not permanent once issued.** A grant issued at session start
  does not stay valid forever by default within a long session — this
  mechanism does not itself mandate a re-verification cadence (left as
  Open Question 4), but a grant consumed by a `CURRENT_REALITY_WITNESS`
  long after issuance without any intervening demonstrated use is weaker
  evidence than one demonstrated immediately before the witness is
  produced. `NO_INVALIDATION_OBSERVED ≠ VALIDITY_RE-ESTABLISHED` (R4)
  applies to the grant's own currency, not only to what it's used to check.

Capability-grant lifecycle is deliberately **not** coupled to
`HBCSELF_ACTIVATION` lifecycle or to `HBCSELF-ROOT` supersession — this is
lower-layer infrastructure that other consumers besides HBCSELF should be
able to rely on. Coupling them would leak HBCSELF-specific policy into
estate-general capability plumbing.

## 6. R4 binding (why this exists)

`HBCSELF-ROOT-v0.2` §II requires `CURRENT_REALITY_WITNESS` to be "produced
by a seat with actual reality-observation capability... never by HBCSELF."
This mechanism makes that checkable rather than assumed:

- Each of R4's five re-observed categories (authority state, evidence,
  dependency state, effect topology, observability) must be traced to the
  specific surface(s) it depends on.
- For each category, the witness must cite a currently valid
  `REALITY_CAPABILITY_GRANT` covering that surface, issued to the specific
  seat producing the witness.
- A category with no covering grant is **`NO_COVERAGE`**, per this
  estate's own null-taxonomy discipline (`null-requires-coverage-law`) —
  graded and disclosed, never silently treated as "checked, nothing wrong."
  Per R4's fail-closed default, `NO_COVERAGE` on any required category
  means the overall recheck HOLDs — it does not partially pass.

```
HBCSELF MAY consume a CURRENT_REALITY_WITNESS
HBCSELF MAY NOT self-certify its own reality capability
HBCSELF MAY NOT self-issue a REALITY_CAPABILITY_GRANT
```

This is the same non-sovereign-output-membrane shape as R1/R2/R4 applied
to one more category: capability grants join truth, authority, and
current-reality witnessing on the list of things HBCSELF can consume but
never manufacture for itself.

## 7. Open questions (unresolved by this candidate; for Founder disposition)

1. **Instrument precision documentation.** Who determines and records an
   instrument's actual boundaries (e.g. a sandboxed Bash tool's denied
   paths) for `observability_contract_refs` — self-reported by the tool's
   own description, or independently documented elsewhere? Not specified.
2. **Evidentiary bar for demonstration.** Is a single successful
   self-demonstrated observation sufficient (§4, condition 2), or should
   high-stakes surfaces require cross-instrument corroboration — the same
   pattern used earlier in this estate's own work (e.g. catching a false
   `ps|grep` match by cross-checking against `lsof`)? Not settled; this
   candidate currently accepts single-instrument self-demonstration as the
   floor, which may be too low for some surfaces.
3. **Founder issuance ceremony.** This candidate's current position (§4)
   is that no new Founder act is needed to "grant" capability beyond what
   session tool configuration already establishes — the grant *records* an
   existing fact plus a demonstration, it doesn't create new authority.
   Flagged explicitly in case that's wrong: an alternative would require
   Founder sign-off per grant, which is far heavier for something as
   routine as "this session has a Bash tool."
4. **Custody / durability.** Whether grant records need a durable ledger
   (mirroring the activation-contract's own open question on ledger
   location) or can remain session-local/ephemeral, re-derived each
   session rather than persisted. Not specified.
5. **Surface granularity in practice.** Some real claims span more than
   one surface (e.g. "the repo is at HEAD X" touches both `FILESYSTEM` and
   `PROCESS`, since it requires running `git`). No convention is set here
   for how finely to decompose a composite claim into surfaces.

---

TERMINAL_SUCCESS = `REALITY_CAPABLE_SEAT_IDENTITY_MECHANISM_READY_FOR_FOUNDER_DISPOSITION`.
`HBCSELF_ACTIVE_SESSIONS = 0`. No grant object issued by this document. No
`ACT-0001`. No session ref resolved. No merge to main. No hostile review
reopened.
