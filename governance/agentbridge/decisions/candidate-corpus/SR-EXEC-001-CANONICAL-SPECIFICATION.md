# SR-EXEC-001 — CANONICAL SPECIFICATION
## Produced under gate SR-SPEC-001 — Canonical Specification Establishment

STATUS: TRANSCRIBED — not yet executed, not itself ratified
CLASS: SPECIFICATION_LINEAGE_RECORD
MODE OF PRODUCTION: read-only with respect to meaning — no redesign, no
  optimization, no additional requirements, no scope expansion, no
  implementation.
SUCCESS CONDITION CLAIMED: Conversation Specification ≡ Repository
  Specification (see Fidelity Note below for the honest limit of that
  claim).

────────────────────────────────────────
PROVENANCE
────────────────────────────────────────
This file exists to close the Specification Lineage Gap identified by the
SR-EXEC-001 pre-execution review conducted 2026-07-29: the SR-EXEC-001
gate registration and its full execution procedure existed only as
conversational content (pasted at the start of this conversation, before
a `/clear` boundary), not as a repository artifact. A fresh session
reading only repository state had no way to reconstruct it. This
transcription is that reconstruction.

SOURCE: this conversation's transcript, the content pasted immediately
  after the `/clear` command, 2026-07-29.
TRANSCRIBED BY: engineering session, under gate SR-SPEC-001, at the
  Founder's direction.
CHANGES MADE TO MEANING: none intended. Two purely typographic
  normalizations were applied and are disclosed here rather than silently
  made: (1) a file path that was line-wrapped only by terminal display
  width (`AUTHORIZED TARGET`, below) is written as one unbroken path,
  since a literal embedded newline would misstate the path rather than
  preserve it; (2) surrounding prose formatting (bullet glyphs, arrows,
  section dividers) is preserved as-typed.

FIDELITY NOTE (disclosed limitation, not hidden): the original text was
never itself a file — it was chat content. There is no independent
checksum of "the original" to diff this transcription against; the only
evidentiary basis for claiming equivalence is this session's careful,
single-pass reproduction from its own conversational context. A future
cold reader should treat this transcription with the same evidentiary
standard already applied elsewhere in this corpus (see the DECLARED
classification in FOUNDER-RATIFICATION-001's evidence legend): its
fidelity is asserted by the producing session, not independently
verified by a second party.

OUT OF SCOPE FOR THIS FILE (present in the same original message, not
transcribed here, to avoid scope expansion beyond "the SR-EXEC-001
execution specification"):
  - A `DECISION_SIGNAL` / `OURSELF_SELFREALIZATION_SCHEMA_ROLE_
    CORRESPONDENCE_FOUNDER_RATIFICATION` template that accompanied this
    text in the same original message. It is superseded in fact by
    `decisions/ratified/FOUNDER-DISPOSITION-001-SELFREALIZATION-F01-F02-
    F04-WITNESS.md`, which records what the Founder actually decided —
    not this template, which was never executed as written. Noted here
    only so a future reader isn't left looking for it.
  - "Trailing tasks until LIMITED_SELFLAUNCH" / "Trailing tasks until
    FULL SELFLaunch" checklists that appeared in the same original
    message. These are a separate roadmap artifact, not part of the
    SR-EXEC-001 execution specification itself.

────────────────────────────────────────
BEGIN VERBATIM TRANSCRIPTION
────────────────────────────────────────

The fast-follow should be registered as a separate amendment gate, not
folded backward into the completed F-01/F-02/F-04 repair. That preserves
the evidence lineage:

Gate 1
Role-correspondence repair
→ completed
→ independently reviewed
→ READY_FOR_FOUNDER_RATIFICATION_REVIEW
Gate 2
authority.execute ceiling amendment
→ newly discovered
→ separately scoped
→ not yet executed

Gate registration

GATE_ID:
SR-EXEC-001
CANONICAL_NAME:
OURSELF_SELFREALIZATION_SCHEMA_EXECUTE_CEILING_AMENDMENT
CLASS:
CONSTITUTIONAL_SCHEMA_AMENDMENT
STATUS:
SCHEDULED_AFTER_FOUNDER_DISPOSITION
PRIORITY:
HIGH_FAST_FOLLOW
DEPENDENCY:
Founder disposition of the completed F-01/F-02/F-04 repair
TARGET:
governance/agent-selfrealization/03_SELFREALIZATION_SCHEMA.yaml
CURRENT AUTHORITY:
NONE
MUTATION AUTHORITY:
NOT YET GRANTED

Scheduling law

The gate should become executable only after the Founder decides the
current repaired schema's disposition.

Recommended sequence:

Founder reviews completed role-correspondence repair
        ↓
Ratify repair or require changes
        ↓
If ratified:
Open SR-EXEC-001
        ↓
Condition authority.execute by role
        ↓
Adversarial review
        ↓
Founder re-review

Do not modify the schema before the first repair receives its formal
disposition. Otherwise two independently reviewable changes become one
moving target.

⸻

Signal command for the future gate

Paste this after the current repair is ratified:

AMENDMENT_SIGNAL
AUTHORITY_SIGNAL
INSPECTION_SIGNAL
MUTATION_SIGNAL
VERIFICATION_SIGNAL
OURSELF_SELFREALIZATION_SCHEMA_EXECUTE_CEILING_AMENDMENT_AUTHORIZED
GATE_ID:
SR-EXEC-001
MODE:
BOUNDED_SINGLE_FILE_CONSTITUTIONAL_REPAIR
EFFORT:
MAX
REPOSITORY:
/Users/millysituated/RUORA
AUTHORIZED TARGET:
/Users/millysituated/RUORA/governance/agent-selfrealization/03_SELFREALIZATION_SCHEMA.yaml
DEPENDENCY:
The previous SELFREALIZATION schema role-correspondence repair must have
received Founder ratification or an explicit authorization allowing this
fast-follow to proceed against its reviewed state.
If that dependency cannot be established:
HOLD.
MISSION:
Condition authority.execute according to the already-ratified role
constitutions, without reopening or weakening the completed F-01/F-02/F-04
repair.
This amendment exists because the independent cold reviewer demonstrated
that the current schema accepts constitutionally forbidden combinations,
including:
assigned_role: governor
authority.execute: GRANTED
assigned_role: planner
authority.execute: GRANTED
despite ratified prose prohibitions.
The repair must be derived from the role constitutions themselves, not from
the examples above alone.
────────────────────────────────────────
PRECONDITION WITNESS
────────────────────────────────────────
Before mutation, record:
- UTC timestamp;
- repository root;
- branch;
- HEAD;
- tracked and untracked state;
- staged state;
- current schema SHA-256;
- current schema version;
- exact ratification reference for the preceding repair;
- confirmation that only the authorized target is eligible for mutation.
Freshly verify that the completed F-01/F-02/F-04 repair remains present:
- assigned_role is closed;
- verifier + mutate:GRANTED is rejected;
- role-conditioned mutate/verify/seal rules remain intact;
- F-03 remains explicitly open.
Do not rely on memory where the file can be inspected.
────────────────────────────────────────
ROLE EXECUTION-AUTHORITY EXTRACTION
────────────────────────────────────────
Read all eleven ratified role constitutions.
For every role, extract:
- whether execution authority is structurally denied;
- whether execution is permitted only if separately granted;
- what execution domain is permitted;
- whether the role may execute its own prior output;
- whether execution must expire;
- whether execution requires a distinct actor;
- whether any narrow exception exists.
Produce:
ROLE EXECUTION CEILING MATRIX
Role
Ratified execution ceiling
Allowed execution scope
Forbidden execution scope
Exception
Source citation
Proposed schema consequence
At minimum, examine:
- architect;
- planner;
- executor;
- verifier;
- governor;
- recovery;
- orchestrator.
Do not assume only Governor, Planner, and Architect require constraints.
────────────────────────────────────────
DESIGN REQUIREMENTS
────────────────────────────────────────
Before editing, produce a diff-shaped amendment plan answering:
1. Which roles must have authority.execute = DENIED.
2. Which roles may receive authority.execute = GRANTED.
3. Whether any role requires a narrower execution-scope field that the current
   schema cannot express.
4. Whether binary GRANTED/DENIED is sufficient.
5. Whether any exception must remain prose-only.
6. How the new execute rules interact with existing mutate/verify/seal rules.
7. How REALIZED gating remains unchanged.
8. Whether the repair is monotonic and non-widening.
9. Which assertions remain impossible in the current schema model.
10. Whether any additional file would be required.
If another repository file is required:
HOLD.
────────────────────────────────────────
AUTHORIZED MUTATION
────────────────────────────────────────
Edit exactly:
governance/agent-selfrealization/03_SELFREALIZATION_SCHEMA.yaml
Required result:
A schema-valid record must never grant authority.execute beyond the
ratified execution ceiling of identity.assigned_role.
At minimum, the schema must reject constitutionally forbidden cases for:
- architect;
- planner;
- governor;
- verifier, if execution is prohibited by its constitution;
- observer;
- researcher;
- orchestrator;
subject to the actual ratified role text.
The schema must preserve legitimate execution authority for roles such as:
- executor;
- recovery, only within its ratified bounded/expiring model;
again subject to fresh extraction from the source files.
Do not weaken any existing constraint.
Do not alter role prose to fit the schema.
────────────────────────────────────────
ADVERSARIAL VERIFICATION
────────────────────────────────────────
Use temporary validation tooling outside RUORA.
Required positive tests:
- one constitutionally valid record for every role;
- executor with properly granted execution authority;
- recovery with any required bounded execution authority represented as far
  as the current schema supports;
- every structurally denied role with execute:DENIED.
Required negative tests:
1. architect + execute:GRANTED;
2. planner + execute:GRANTED;
3. governor + execute:GRANTED;
4. observer + execute:GRANTED;
5. researcher + execute:GRANTED;
6. orchestrator + execute:GRANTED;
7. verifier + execute:GRANTED, when prohibited by ratified text;
8. unknown role;
9. missing execute;
10. extra authority field;
11. REALIZED plus forbidden execute grant;
12. non-REALIZED plus forbidden execute grant;
13. crafted record matching no role branch;
14. crafted record attempting ambiguous branch matching.
Report expected versus actual for every case.
No unsupported semantic property may be reported as proven.
Use:
NOT_SCHEMA_EXPRESSIBLE_IN_CURRENT_MODEL
where necessary.
────────────────────────────────────────
INDEPENDENT COLD REVIEW
────────────────────────────────────────
A fresh reviewer must independently verify:
- role extraction accuracy;
- execute-ceiling completeness;
- no role omitted;
- no legitimate executor authority over-constrained;
- no recovery exception widened;
- all prior mutate/verify/seal constraints preserved;
- REALIZED gating preserved;
- valid YAML and metaschema compliance;
- exactly one repository file changed;
- no scope leakage.
The cold reviewer must receive the source files and diff, but not the
mutator's conclusion.
────────────────────────────────────────
REQUIRED OUTPUT
────────────────────────────────────────
OURSELF SELFREALIZATION EXECUTE-CEILING AMENDMENT WITNESS
A. UTC window
B. Repository, branch, and HEAD
C. Prior repair ratification reference
D. Pre-amendment schema hash
E. Post-amendment schema hash
F. Exact file changed
G. Role Execution Ceiling Matrix
H. Schema mechanism used
I. Positive validation results
J. Negative validation results
K. REALIZED-gating regression result
L. Prior F-01/F-02/F-04 regression result
M. F-03 status
N. Unsupported semantic constraints
O. Independent cold-review findings
P. Scope containment
Q. git diff --check
R. git status --short
S. Files changed: exactly one
T. Staging/commit/push/publication: NONE
U. Verdict
Allowed verdicts:
READY_FOR_FOUNDER_RATIFICATION_REVIEW
CHANGES_REQUIRED
HOLD
FAILED
────────────────────────────────────────
FORBIDDEN
────────────────────────────────────────
- No role-constitution edits.
- No doctrine edits.
- No AgentBridge workflow edits.
- No runtime evidence changes.
- No adapter design.
- No validator implementation.
- No staging.
- No commit.
- No push.
- No publication.
- No seal.

────────────────────────────────────────
END VERBATIM TRANSCRIPTION
────────────────────────────────────────

────────────────────────────────────────
POST-TRANSCRIPTION STATUS UPDATE (factual, not part of the transcription)
────────────────────────────────────────
The DEPENDENCY clause above ("must have received Founder ratification...
If that dependency cannot be established: HOLD.") is now SATISFIED. See
`decisions/ratified/FOUNDER-DISPOSITION-001-SELFREALIZATION-F01-F02-F04-
WITNESS.md`. This transcription does not modify the dependency text above
(preserving semantic equivalence with the source), but a future Executor
should read the dependency as satisfied, evidenced by that file, not as an
open condition.

One item inside the transcribed text is now known, from this session's
direct verification, to be imprecisely worded rather than false: "F-03
remains explicitly open" (PRECONDITION WITNESS section). Repository
evidence cannot establish F-03 as a defined, open item — a repository-wide
search finds no trace of it. The Founder Disposition Record states F-03
receives `NO_DISPOSITION`. A future Executor's required-output field M
("F-03 status") should report this accurately — `UNKNOWN` / `NO
REPOSITORY-EVIDENCED DEFINITION` — rather than copying the word "open"
from this transcription as if it were a verified fact.
