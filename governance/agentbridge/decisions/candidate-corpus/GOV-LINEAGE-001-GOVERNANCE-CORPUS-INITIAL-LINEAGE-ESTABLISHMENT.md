# GOV-LINEAGE-001 — GOVERNANCE CORPUS INITIAL LINEAGE ESTABLISHMENT

STATUS: PARKED
CLASSIFICATION: GOVERNANCE_EVIDENCE_ITEM
EXECUTION_AUTHORITY: NONE
MUTATION_AUTHORITY: NONE (no `git add`/`git commit` authorized by this document)

────────────────────────────────────────
FINDING
────────────────────────────────────────
As of 2026-07-29, repository /Users/millysituated/RUORA, branch main,
HEAD 1a7475a533cb14560f307fa6d199cfeca997323e:

    $ git status --short
    ?? .claude/
    ?? doctrine/runtime-doctrine-stack.md
    ?? governance/
    ?? runtime/

    $ git log --all --oneline -- governance/
    (empty)

`governance/` (30 files, including 00-09 numbered SELFREALIZATION docs,
04_ROLE_CONSTITUTIONS/, and agentbridge/{constitutions,decisions,launch,
workflow}/) has never been committed on any branch. Same for `runtime/`,
`doctrine/runtime-doctrine-stack.md`, and `.claude/`.

Verified this is omission, not exclusion:

    $ git check-ignore -v governance
    (no output, exit 1 — not ignored)

    $ cat .gitignore
    (no entry for governance/, runtime/, doctrine/runtime-doctrine-stack.md,
    or .claude/ — existing excludes are __pycache__, .DS_Store, .env*,
    *.pem, projects/, backups/, systems/, quarantine/)

Conclusion: these paths simply have not been `git add`ed. Not a config
problem.

────────────────────────────────────────
WHY THIS MATTERS
────────────────────────────────────────
Per this repo's own evidence chain (Declaration -> Execution -> Evidence ->
Memory), Git commit history is the evidence layer. The completed F-01/F-02/
F-04 role-correspondence repair, and everything else in governance/, is
"complete on disk" but has no immutable Git lineage proving when it entered
the repository. The Founder can still ratify the content itself — this
finding does not block or invalidate that ratification — but the
ratification record should note that Git-backed provenance for the corpus
does not yet exist.

────────────────────────────────────────
RESOLUTION SEQUENCE (not authorized by this document — recorded for the
future gate that will execute it)
────────────────────────────────────────
This is not merely "the first commit." It is the point where the
governance corpus transitions between two ontological states — working
papers with no external evidentiary weight, and a historical record that
all future governance change amends against:

    Working Papers
        -> Founder Ratification
        -> Frozen Corpus
        -> Genesis Commit of the Governance Corpus
        -> Historical Record
        -> Amendments

Concretely:

    Founder ratifies (content-level ratification of governance/ as it
    stands)
        -> Corpus frozen (no further edits to the ratified files until the
           Genesis Commit lands)
        -> Genesis Commit of the Governance Corpus (single commit or
           clearly scoped sequence)
        -> Future amendments become normal Git history from that point
           forward

SCOPE OF THE GENESIS COMMIT: governance/, runtime/, and
doctrine/runtime-doctrine-stack.md were discovered untracked together.
Whether they constitute one constitutional baseline is a determination for
Founder disposition — this document asserts no opinion on relatedness and
infers no scope from proximity. The branching rule:

    If Founder disposition determines that governance/, runtime/, and
    doctrine/runtime-doctrine-stack.md constitute one constitutional
    baseline, they shall enter Git history as one Genesis Commit of the
    Governance Corpus.

    If Founder disposition separates those domains, each shall establish
    its own genesis lineage under its respective authority.

`.claude/` is local tooling/session configuration, not doctrine content,
and is not a candidate for the Genesis Commit under either branch.

This is explicitly NOT "commit everything immediately." No `git add` or
`git commit` is authorized by this document.

────────────────────────────────────────
RELATIONSHIP TO OTHER PARKED ITEMS
────────────────────────────────────────
Independent of GATE-3-HYPERBOLIC-CHAMBER-DESIGN-SPECIFICATION-0001 — that
finding was an infrastructure failure (disk full) blocking writes; this is
a provenance/evidence-chain question about already-completed work. The two
were discovered adjacent to each other but do not share a dependency.
