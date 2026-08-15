# ALCHEMISELF ROOT RUNTIME v0.1 PROOF

**ACT** `ALCHEMISELF_ROOT_RUNTIME_001`
**BRANCH** `alchemiself-root-runtime-v0.1`
**BASELINE** `9451d5d71e4fe2de58513b4969a313f5f9b8b04d`
**STATUS** `PROOF_PASS`

## Files Added

- `governance/ALCHEMISELF-ROOT-RUNTIME-v0.1.md`
- `governance/ALCHEMISELF-TYPE-CONFUSION-SPECIMENS-v0.1.json`
- `tools/verify-alchemiself-root-runtime.mjs`
- `reports/ALCHEMISELF-ROOT-RUNTIME-v0.1-PROOF.md`

## Subsystems Identified

The root runtime spec identifies these current untyped-reference surfaces:

- INSELFACTION archives
- `interactions/latest.json`
- RUORA governance records
- HBCSELF hostile-review handoffs
- Git/GitHub resolution layer
- memory and cross-session recall
- tool invocation layer
- review/repair lanes

## Validation

Commands executed:

```bash
node tools/verify-alchemiself-root-runtime.mjs
node -e "JSON.parse(require('fs').readFileSync('governance/ALCHEMISELF-TYPE-CONFUSION-SPECIMENS-v0.1.json','utf8')); console.log('json-ok')"
git diff --check
shasum -a 256 governance/SELFHTML-REALITY-CONTRACT-SEMANTICS-001-v0.1-CANDIDATE.md
```

Observed results:

```text
ALCHEMISELF_ROOT_RUNTIME_PROOF=PASS
TYPE_CONFUSION_PROOFS=8
CANONICAL_SPECIMEN=TYPE-CONFUSION-dd9da0b7-001
json-ok
dd9da0b7caf1014c1c57962fbe15d9b75217311327a61ce634325fd61fbabb82  governance/SELFHTML-REALITY-CONTRACT-SEMANTICS-001-v0.1-CANDIDATE.md
```

## Old Functionality Preservation

The SELFHTML hostile-review target remains byte-identical to the prior receiver-resolvable source:

```text
governance/SELFHTML-REALITY-CONTRACT-SEMANTICS-001-v0.1-CANDIDATE.md
SHA256 dd9da0b7caf1014c1c57962fbe15d9b75217311327a61ce634325fd61fbabb82
```

No existing SELFHTML candidate file was modified by this root runtime mutation.
