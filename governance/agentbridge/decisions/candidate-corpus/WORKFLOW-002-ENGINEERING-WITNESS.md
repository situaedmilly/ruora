# WORKFLOW-002 — ENGINEERING WITNESS

STATUS: DISPOSITIONED (2026-07-30) — APPROVED. See
  decisions/ratified/FOUNDER-DISPOSITION-004-WORKFLOW-002-WITNESS.md for
  the constitutional record.
CLASS: Engineering Evidence

────────────────────────────────────────
READ
────────────────────────────────────────
- WORKFLOW-001-HYPERBOLIC-CHAMBER-RUNTIME-CONTRACT-SPECIFICATION.md (this
  session's own authorship, hash-confirmed unchanged below).
- GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001.md (hash-confirmed
  unchanged below).
- governance/agentbridge/workflow/04_GATE_EXECUTION.md,
  05_VERIFICATION.md, 06_SEAL_OR_HOLD.md — directly referenced workflow
  doctrine, read for vocabulary reuse (lifecycle stages, cold-process
  verification, the eight-verdict set, epistemic pipeline,
  PROPOSITION_INFLATION). All three confirmed read-only (mtimes
  unchanged, Jul 27).

────────────────────────────────────────
PRODUCED
────────────────────────────────────────
Exactly one specification:
  WORKFLOW-002-HYPERBOLIC-INVOCATION-CONTRACT-SPECIFICATION.md
Covering all 10 required objective items (invocation authority, packet,
lifecycle, reviewer-selection interface, confidence-threshold interface,
disagreement interface, cancellation/failure/completion semantics,
evidence emitted). Three genuine open items disclosed rather than
silently resolved: exact reviewer counts per level, numeric confidence
thresholds, disagreement adjudication rule — all traceable to Gate 3 §4,
which named them unresolved originally.

No routing implementation. No scheduler/planner implementation. No
execution engine. No production activation. No doctrine file touched.

────────────────────────────────────────
SCOPE COMPLIANCE
────────────────────────────────────────
Confirmed fresh:
  - `find governance -type f -newermt` (from just before this workflow
    began) returns exactly three files: FOUNDER-DISPOSITION-003 and the
    WORKFLOW-001 witness status fix (both from disposition-recording,
    completed and confirmed before this workflow opened) and this
    workflow's own new specification file.
  - `04_GATE_EXECUTION.md`, `05_VERIFICATION.md`, `06_SEAL_OR_HOLD.md`:
    mtimes unchanged (Jul 27) — read-only reference, not modified.
  - Gate 3 hash unchanged: 6292de44...8087815.
  - WORKFLOW-001 specification hash unchanged:
    63e60c4842cb0b97866bc2381a51332baf95e182d8349a2d14ceb2a544861728 —
    not edited, despite this workflow building directly on it.
  - `git status --short`: only the same 4 pre-existing untracked
    top-level paths.
  - No staging, commit, push, or publication.

────────────────────────────────────────
WHAT THIS DOES NOT ESTABLISH
────────────────────────────────────────
This specification defines mechanics for *how* AgentBridge would invoke
the chamber, contingent on a per-invocation decision each time (stated
explicitly in the specification's own forbidden-list closer). It does
not cause any gate to actually invoke the chamber, and does not
constitute routing, scheduling, or activation authority for any specific
future gate.

────────────────────────────────────────
RECOMMENDED FOUNDER DISPOSITION (recommendation only — not self-issued)
────────────────────────────────────────
Internally consistent with WORKFLOW-001 and with existing, already-
ratified AgentBridge workflow doctrine — every interface reuses vocabulary
already established in `04_GATE_EXECUTION.md`/`05_VERIFICATION.md`/
`06_SEAL_OR_HOLD.md` rather than inventing parallel terms, and open items
are disclosed rather than papered over. On those engineering grounds,
APPROVE is supportable.

As with WORKFLOW-001: approving this document authorizes nothing beyond
itself. It does not authorize WORKFLOW-003, implementation, or any
specific gate's actual invocation of the chamber.
