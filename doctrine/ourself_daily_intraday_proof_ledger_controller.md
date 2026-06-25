# OURSELF Daily / Intraday Proof Ledger Controller

## File

`doctrine/ourself_daily_intraday_proof_ledger_controller.md`

## Status

Active controller file.

## Purpose

This file commands OURSELF-aligned agents to maintain a daily and intraday ledger of:

- new distinctions
- doctrine updates
- artifacts created or changed
- Claude Code commands actually run
- command proofs per session/day
- refused mutations
- evidence classifications
- rollback paths
- next executable actions

This ledger exists to prevent memory drift, false continuity, unproven command claims, and vibe-based progress reports.

The ledger is not a journal.

The ledger is not aesthetic documentation.

The ledger is a proof spine.

---

## 1. Controller Command

OURSELF commands every agent operating inside the RUORA / SELF / OURSELF doctrine field to update the Proof Ledger:

1. once per working day
2. after every meaningful session
3. after any Claude Code command sequence
4. after any doctrine mutation
5. after any artifact creation
6. after any rejected or negated mutation
7. before any seal, merge, publish, push, or remote execution

Intraday updates are required when the state changes materially.

No agent may claim continuity, completion, proof, or seal without ledger evidence.

---

## 2. Non-Negotiable Witness Law

Observed state is the first witness.

A command is not Verified because an agent says it ran.

A file is not Verified because an agent says it exists.

A commit is not Verified because an agent says it was sealed.

A branch is not Verified because an agent says it is clean.

A remote boundary is not Verified because an agent says no push happened.

Verified requires witness.

Valid witnesses include:

- terminal output
- file contents
- `git status`
- `git log --oneline`
- `git diff`
- `git branch --show-current`
- `git remote -v`
- commit hash
- file path inspection
- direct user-provided transcript
- direct uploaded artifact
- inspected repository state

When witness is absent, classify as Unwitnessed.

---

## 3. Evidence Tiers

Every ledger entry must classify claims using these tiers:

| Tier | Definition |
|---|---|
| Verified | Direct witness exists: terminal output, file content, commit hash, inspected state, uploaded artifact, or explicit user-provided evidence |
| Probable | Strong inference from available evidence, but not directly witnessed |
| Unwitnessed | Claimed, planned, or reported without direct inspection |
| Symbolic | Archetypal, alchemical, metaphysical, or poetic framing |
| Speculative | Possible but unsupported |

Forbidden collapse:

```text
Speculative   → Verified
Symbolic      → Verified
Unwitnessed   → Verified
Declared target → observed state
Agent claim   → proof
```

---

## 4. Required Daily Ledger Entry Format

Each day must have an entry using this structure:

```markdown
# OURSELF Proof Ledger — YYYY-MM-DD

## Session Index
| Session | Time | Agent / Chamber | Scope | State |
|---|---:|---|---|---|
| 001 | HH:MM | Claude Code / ChatGPT / Other | Short scope | Open / Sealed / Frozen |

## New Distinctions
| Distinction | Tier | Witness | Doctrine Impact |
|---|---|---|---|
|  | Verified / Probable / Unwitnessed / Symbolic / Speculative |  |  |

## Artifacts
| Artifact | Path / Location | Action | Tier | Witness |
|---|---|---|---|---|
|  |  | Created / Updated / Deleted / Proposed |  |  |

## Claude Code Commands
| Command | Claimed Effect | Tier | Witness | Result |
|---|---|---|---|---|
| `command here` |  | Verified / Probable / Unwitnessed | terminal output / file diff / commit hash | Passed / Failed / Interrupted |

## Proofs
| Proof | Evidence | Tier | Notes |
|---|---|---|---|
|  |  |  |  |

## Refused Mutations
| Refused Path | Reason | Doctrine Rule | Next Allowed Action |
|---|---|---|---|
|  |  |  |  |

## Drift / Reconciliation
| Drift | Severity | Correction | Status |
|---|---|---|---|
|  | Critical / High / Medium / Low |  | Open / Reconciled / Frozen |

## Seal Status
| Item | Proof Complete? | Seal State | Rollback |
|---|---|---|---|
|  | Yes / No | Unsealed / Sealed / Quarantined |  |

## Next Executable Action
One action only:
[write the next concrete action here]
```

---

## 5. Intraday Update Format

Intraday updates must append under the same day:

```markdown
## Intraday Update — HH:MM

### Trigger
What changed?

### New Witness
Paste terminal output, file path, commit hash, diff, artifact, or direct observation.

### Classification
| Claim | Tier | Witness |
|---|---|---|
|  |  |  |

### Ledger Mutation
What was added, corrected, down-tiered, sealed, or refused?

### Next Action
One executable action.
```

---

## 6. Claude Code Command Proof Rule

Every Claude Code command sequence must be recorded.

Required fields:

```markdown
## Claude Code Command Proof

### Command Block
# exact command(s)

### Claimed Effect
What the command was intended to do.

### Witness
Paste terminal output.

### Evidence Tier
Verified / Probable / Unwitnessed / Speculative

### Result
Passed / Failed / Interrupted / No-op / Partial

### Follow-up Required
None / inspect / patch / revert / reconcile / seal
```

No terminal output means the command remains Unwitnessed.

A clean narrative is not proof.

A command transcript is stronger than an agent summary.

A file diff is stronger than a command transcript.

A commit hash plus clean status is stronger than both.

---

## 7. Plain-Witness Proof Clause

Within this doctrine file, the "real nigga terminology" clause means:

> Plain, witnessed, no-bullshit language that names what actually happened, what did not happen, what proof exists, what is still unwitnessed, and what must not be claimed.

Valid usage:

```text
Real proof: commit 32a0480 exists on branch worktree-pass-22-control-plane-resubordination, with clean working tree shown by git status.
```

Invalid usage:

```text
It feels sealed.
```

Valid usage:

```text
No push occurred because git remote -v returned no remotes in that worktree.
```

Invalid usage:

```text
The chamber would never push.
```

This clause does not authorize sloppiness, posturing, or unverified certainty.

It requires harder evidence and cleaner speech.

---

## 8. Refusal Gate

Before any ledger update, ask:

> What must be refused before anything is continued?

Refuse:

- mutation from claim
- command proof without witness
- speculative seal
- public push without explicit gate
- remote automation without firewall
- Slack / Notion / OAuth / webhook execution treated as routine
- Mirror / Forge demotion into chat furniture
- controller elevated above SELFControl
- declared target elevated above observed state
- symbolic language presented as Verified

---

## 9. File Location

Recommended canonical file:

```text
doctrine/ourself_daily_intraday_proof_ledger_controller.md
```

Recommended ledger directory:

```text
doctrine/proof-ledger/
```

Recommended daily file pattern:

```text
doctrine/proof-ledger/YYYY-MM-DD.md
```

Example:

```text
doctrine/proof-ledger/2026-06-25.md
```

---

## 10. Agent Compliance Rule

At the beginning or end of each meaningful session, the agent must ask for or produce:

> Ledger update?

If command output exists, update the ledger.

If no command output exists, record that no command proof exists.

If a claim exists without witness, down-tier it.

If a mutation is requested without proof, refuse or freeze.

---

## 11. Final Ruling

OURSELF does not trust memory alone.

OURSELF trusts witnessed command, inspected artifact, classified claim, reversible mutation, and sealed proof.

From this point forward, daily and intraday doctrine work must leave a proof trail.
