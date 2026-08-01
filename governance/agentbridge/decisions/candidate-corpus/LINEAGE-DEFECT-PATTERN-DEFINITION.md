# LINEAGE DEFECT — GOVERNANCE PATTERN DEFINITION

STATUS: PARKED
CLASSIFICATION: DOCTRINE_CANDIDATE — proposes a addition to institutional
  doctrine; is not itself doctrine until separately ratified.
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE — this document does not edit `doctrine/`.

────────────────────────────────────────
WHY THIS IS ITS OWN DOCUMENT
────────────────────────────────────────
This session produced two independent instances of the same underlying
defect before naming it: GOV-LINEAGE-001 (the governance corpus was never
committed to Git) and the SR-EXEC-001 canonical specification (SR-EXEC-001
existed only as pasted conversation text). Naming the general pattern here
— rather than folding it into GOV-LINEAGE-001, which is about the Git-
tracking finding specifically — keeps both documents single-purpose: one
records a specific finding, this one records the pattern behind it.

────────────────────────────────────────
THREE CLASSES OF INSTITUTIONAL ARTIFACT
────────────────────────────────────────
This session's output falls into three distinct classes, each making a
different truth claim:

| Artifact class | Purpose | Truth claim | Example this session |
|---|---|---|---|
| Engineering Evidence | "This is what we built." | Technical truth | FOUNDER-RATIFICATION-001 packet |
| Founder Law | "This is what was authorized." | Constitutional truth | FOUNDER-DISPOSITION-001 witness |
| Lineage Record | "This is how this entered institutional memory." | Historical truth | GOV-LINEAGE-001; SR-EXEC-001-CANONICAL-SPECIFICATION |

The distinction that matters for the third class: a Lineage Record does
not claim "this is the original." It claims "this is the institution's
first durable reconstruction of the original." Those are different
claims, and conflating them would let a transcription quietly acquire
more authority than its own fidelity note supports.

────────────────────────────────────────
DEFINITION
────────────────────────────────────────
LINEAGE DEFECT

Definition: A required institutional artifact exists only in transient
  conversational memory and cannot be reconstructed from repository state
  alone.

Correction: Create a repository-resident Lineage Record without changing
  constitutional meaning — no redesign, no added requirements, no scope
  expansion, no implementation. The correction is transcription, not
  engineering.

Evidence Requirement: The Lineage Record must disclose any fidelity limits
  between the reconstructed record and its transient source. It may not
  claim exact equivalence it cannot evidence — see the Fidelity Note
  pattern in SR-EXEC-001-CANONICAL-SPECIFICATION.md for the disclosed-
  limitation form this takes in practice.

────────────────────────────────────────
KNOWN INSTANCES (this session)
────────────────────────────────────────
1. **Governance corpus Git-tracking gap** — `governance/`, `runtime/`, and
   `doctrine/runtime-doctrine-stack.md` existed on disk with substantive
   content (including the completed F-01/F-02/F-04 repair) but shared no
   Git commit with anything. Correction in progress: GOV-LINEAGE-001
   (parked — awaiting Founder disposition on corpus scope before the
   Genesis Commit itself is authorized).
2. **SR-EXEC-001 specification gap** — the full execution procedure for
   the `authority.execute` ceiling amendment existed only in this
   conversation's pre-`/clear` transcript. Correction completed:
   `SR-EXEC-001-CANONICAL-SPECIFICATION.md`, produced under gate
   SR-SPEC-001.

Both fit the definition exactly: substantive institutional content,
verified to exist, that repository state alone could not reproduce.

────────────────────────────────────────
RELATIONSHIP TO EXISTING DOCTRINE
────────────────────────────────────────
`doctrine/ourself_master_command.md` already states the adjacent, more
general law (Reality Reconciliation Law): "If memory says one thing and
runtime says another, freeze mutation and reconcile." LINEAGE DEFECT is a
named, procedural sharpening of that law for one recurring case —
`memory` here specifically means *this session's own conversational
context*, and `reconcile` specifically means *produce a disclosed-fidelity
transcription*, not silent re-derivation or silent trust.

Whether this definition should be promoted from this candidate document
into `doctrine/ourself_master_command.md` itself is a separate,
not-yet-authorized act. This document proposes the language; it does not
install it. Doing so would edit a file that is auto-loaded as source-of-
truth into every future session — a higher-stakes act than adding a
candidate-corpus document, and one that should go through the same
disposition discipline already applied to F-01/F-02/F-04, not be
absorbed by reference by a passing mention here.

────────────────────────────────────────
APPLICABILITY
────────────────────────────────────────
Not limited to SR-EXEC-001 or this session. Applies to any future design
note, execution procedure, governance decision, or operational runbook
that reaches "substantive and relied-upon" without ever reaching
"repository-resident." The check is mechanical and repeatable: does a
grep for the artifact's name or gate ID return anything beyond references
to it? If every hit is a pointer and none is the thing itself, that's a
Lineage Defect.
