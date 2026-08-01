# 05_VERIFICATION

**Document identifier:** `governance/agentbridge/workflow/05_VERIFICATION.md`
**Workflow schema version:** `OURSELF-AGENTBRIDGE-WORKFLOW-v0.1`
**Status:** `FOUNDER_AUTHORIZED_OPERATIONAL_WORKFLOW`

## Purpose

One reusable verification pass over whatever `04_GATE_EXECUTION.md`
actually did. Establishes whether the claimed result is real, bounded, and
correctly attributed — never repairs what it finds.

## Authority granted

- Live repository witness (re-read state directly, do not trust the gate's
  self-report).
- Compute exact diff scope of what changed.
- Run targeted tests relevant to the change, and the full regression suite.
- Perform static containment checks (confirm nothing outside the
  authorized scope changed).
- Check runtime/evidence-store state where the gate touched it.
- Perform cold-process verification (a fresh process/session re-checking
  the claim, not the same context that produced it).
- Check ledger continuity and prior proof-chain integrity.
- Produce the Verification output below.

## Authority explicitly not granted

- No repair of any finding surfaced here. A finding is reported; fixing it
  is a new, separately authorized `BOUNDED_REPAIR` gate under
  `04_GATE_EXECUTION.md`.
- No softening or narrative reframing of a finding to make a seal easier to
  grant in `06_SEAL_OR_HOLD.md`.

## Required inputs

- Gate Selection output and Gate Execution output.
- Live repository and runtime-evidence state.

## Required procedure

1. Re-derive the diff independently — do not accept the executing gate's
   description of "what changed" without confirming it against `git diff` /
   `git status` and, where applicable, the evidence store.
2. Run targeted tests for the change, then the full regression suite.
   Report both, separately.
3. Run static containment: confirm no file outside the gate's authorized
   scope changed.
4. Where the gate touched runtime evidence, check it directly (hashes,
   counts, ledger entries) — do not infer from the gate's narrative.
5. Perform cold-process verification: re-check the claim from a fresh
   vantage point (new process, new read), not by re-reading the same
   in-context conversation that produced the claim.
6. Check ledger continuity: does this gate's evidence chain correctly
   extend the prior proof-chain sequence without gaps or contradictions?
7. Walk the epistemic pipeline for every claim before accepting it:

   ```
   Artifact presence → interpretation validity → referent validity →
   temporal index
   ```

   That is: (a) does the artifact actually exist; (b) is it being read
   correctly; (c) does it actually refer to what it's claimed to refer to;
   (d) is it current, or stale evidence being presented as current.
8. Name the specific failure mode when a claim outruns its evidence:

   **`PROPOSITION_INFLATION`** — a claim's scope or certainty exceeds what
   the underlying artifact actually supports.

9. Map every claim in the gate's output to the specific evidence that
   supports it. An unmapped claim is not verified; it is asserted.
10. List known blind spots explicitly — what this verification pass could
    not check, and why — rather than implying completeness it doesn't have.

## Required output — Verification Report

```
Live repository witness:      <what was actually re-read, with paths/HEADs>
Diff scope:                   <exact files, independently derived>
Targeted tests:                <pass/fail, per test>
Full regression suite:        <pass/fail summary>
Static containment:            <CONTAINED|VIOLATION — list any violation>
Runtime/evidence-store check:  <result, or N/A>
Cold-process verification:     <result>
Ledger continuity:              <CONTINUOUS|GAP|CONTRADICTION>
Prior-chain verification:       <result>
Known blind spots:              <explicit list>
Claim-to-evidence map:          <table: claim → supporting artifact>
Proposition-inflation check:    <NONE_DETECTED | list of inflated claims>
```

## Refusal / HOLD conditions

- Any claim cannot be mapped to a specific artifact → flag as
  `PROPOSITION_INFLATION`, not as verified.
- Static containment finds a change outside authorized scope → `VIOLATION`,
  and this blocks `SEALED` in `06_SEAL_OR_HOLD.md` regardless of how the
  rest of the verification reads.
- Cold-process verification cannot be performed at all → report this as a
  named blind spot; do not substitute same-context re-reading and call it
  cold verification.

## Launch-state footer

The Verification Report is handed unmodified to `06_SEAL_OR_HOLD.md`, which
restates `Steps Until SELFLaunch` alongside its verdict.
