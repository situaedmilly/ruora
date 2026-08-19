# OURSELF Reality Capability Grant — Q1-Q4 Adoption 001

SUBJECT: `OURSELF-REALITY-CAPABILITY-GRANT-Q2-Q3-DISPOSITION-CANDIDATE-01.md`
(commit `7676edb`), with Q2 revised per the hostile-chamber pass that
followed it (this session, same conversation).
ACT: Founder adoption. Milasophahr, direct answer to a direct question
("Adopt all four as refined"), with an added refinement (claim-relativity
of independence) accepted into the adopted text rather than left as
unincorporated commentary.
DATE: 2026-08-19.
CAUSAL PARENT: `aeaec9e` (reality-capable-seat mechanism candidate) →
`7676edb` (Q2/Q3 disposition candidate) → this adoption.

## What this adopts

### Q1 — Tier-2 scope

`R4-GATING CLAIM → TIER_2 MINIMUM`. Scope-limited: applies only to claims
whose standing is required for R4 to admit executable `MORPHTATION`. Does
**not** apply to all observations, all HBC reasoning, all Matter, all
witnesses, or all institutional claims generally.

### Q2 — Independence test (REVISED from `7676edb`'s original wording)

The original wording in `7676edb` ("disqualify corroboration if the two
observations share ANY of: source / instrument-code-path /
precondition") is **superseded by this text**, not merely supplemented —
that original binary test, applied literally, would have disqualified the
`ps`+`lsof` precedent it was built to justify (both share host, kernel,
and PID-interpretation assumptions). The corrected law:

- **Independence is claim-relative, not a global property of a tool
  pair:** `INDEPENDENCE(tool_a, tool_b, claim, failure_model)`, not
  `INDEPENDENCE(tool_a, tool_b)`. A pairing can corroborate one claim and
  say nothing useful about another (`ps`+`lsof` corroborate "PID 87619
  exists"; neither observes "PID 87619 has not read `~/.agents`").
- **`MATERIAL_EVIDENTIARY_PATH`** (binding definition): a corroborating
  observation path whose evidence acquisition depends on at least one
  materially distinct reality interface, data structure, measurement
  mechanism, or provenance chain — such that a known or plausible failure
  mode affecting the primary path does not necessarily propagate to the
  corroborating path — **and** that distinction is relevant to a plausible
  failure mode of the primary observation *for the specific claim under
  test*.
- **No new schema field required.** Claim-relativity is judged by
  comparing the `proposition_class` and `instrument_semantics` fields of
  the primary and corroborating `observability_contract_ref`s against the
  same claim — the six-field contract (Q4) already carries what's needed.
- **Non-examples, preserved explicitly so this doesn't drift back into
  "different tool = independent":**
  - `ls` vs. `ls -la` — same interface, different flags. Not material.
  - `grep pattern-A file` vs. `grep pattern-B same-file` — same source,
    same interpretation assumption. Not material.
  - `cat config.json` vs. a Python script reading `config.json` — different
    binaries, same underlying bytes; if the config itself is stale, both
    fail identically. Not material for "is this config current."
  - Two wrappers around the same underlying API are not independent merely
    because their binaries differ.
- **Worked positive example, preserved:** a config file claiming a service
  is active, corroborated by querying live process/socket state — these
  are materially different reality interfaces; the second can falsify the
  first even when the config bytes are internally well-formed. Valid
  corroboration.
- **If no material corroborating path exists for the claim:** record
  `NO_MATERIAL_CORROBORATION_AVAILABLE` explicitly (renames, does not add
  to, `7676edb`'s `NO_INDEPENDENT_CORROBORATION_AVAILABLE` — same
  requirement, sharper name matching the claim-relative framing) and
  require the Founder gate `7676edb` already specified. No fake redundancy.

**Tier-2, restated precisely under this revision:**
```
TIER_2 = SEMANTICALLY_VALID_PRIMARY_PATH
         + CLAIM-RELEVANT MATERIAL CORROBORATING PATH (when one exists)
TIER_2 ≠ TWO_COMMANDS
TIER_2 ≠ TWO_TOOLS
TIER_2 ≠ TWO_SEATS
```

### Q3 — Batch issuance (unchanged from `7676edb`, confirmed)

One Founder act may issue grants for multiple surfaces within one named
seat and one named activation scope. Every individual surface grant
remains independently addressable and evidence-bound — the ceremony
batches; the capability does not. `BATCH_CEREMONY ≠ BATCH_CAPABILITY`.

### Q4 — Six-field inline observability contract (unchanged from `7676edb`, confirmed)

Sufficient for `ACT-0001`. `SUFFICIENT_FOR_ACT_0001 ≠ UNIVERSALLY_COMPLETE_FOREVER`.
No field added by this adoption — Q2's claim-relativity is carried by the
existing `proposition_class` and `instrument_semantics` fields, not a new one.

## Preserved laws (binding after this adoption)

```
ANY_SHARED_DEPENDENCY        ≠ NO_EVIDENTIARY_INDEPENDENCE
DIFFERENT_COMMAND            ≠ DIFFERENT_EVIDENTIARY_PATH
DIFFERENT_TOOL                ≠ INDEPENDENT_EVIDENCE
CORROBORATION                   ≠ REPETITION
EVIDENTIARY_INDEPENDENCE          ≠ GLOBAL_TOOL_PROPERTY (claim-relative)
BATCH_CEREMONY                      ≠ BATCH_CAPABILITY
SUFFICIENT_FOR_ACT_0001                ≠ UNIVERSALLY_COMPLETE_FOREVER
CAPABILITY_CLAIM                          ≠ CAPABILITY_GRANT
CAPABILITY_DEMONSTRATED                      ≠ CAPABILITY_GRANTED
SEAT_CANNOT_SELF_ISSUE_GRANT
HBCSELF_CANNOT_ISSUE_GRANT
```

## What this does NOT do

- No `REALITY_CAPABILITY_GRANT` is issued by this record.
- No `ACT-0001`. `EXACT_SESSION_REF` and `FOUNDER_PURPOSE_OR_MATTER_REF`
  remain unresolved.
- No HBCSELF activation. No session projection.
- No merge to main. Not pushed pending separate authorization (three prior
  commits in this lineage are also still unpushed — this makes four ahead
  of remote).
- No new hostile review opened. No universal observability registry or
  global grant ledger built (Q4/Q5 from `aeaec9e` remain deferred).

## Standing

The reality-capable-seat mechanism is now **semantically closed for
`ACT-0001`'s purposes** — Q1-Q4 all resolved, Q4/Q5 from `aeaec9e`
deliberately still deferred (not required to close). Next gate: a first
actual `REALITY_CAPABILITY_GRANT`, which still requires (a) a real Founder
issuance act under the Q3 ceremony, (b) `EXACT_SESSION_REF` resolved, and
(c) `FOUNDER_PURPOSE_OR_MATTER_REF` bound — none of which happen here.

STOP.
