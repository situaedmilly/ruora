#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const specimenPath = path.join(root, 'governance', 'ALCHEMISELF-TYPE-CONFUSION-SPECIMENS-v0.1.json');
const specPath = path.join(root, 'governance', 'ALCHEMISELF-ROOT-RUNTIME-v0.1.md');

const specimens = JSON.parse(fs.readFileSync(specimenPath, 'utf8')).specimens;
const spec = fs.readFileSync(specPath, 'utf8');

const requiredSpecPhrases = [
  'Never act on a symbol before determining what kind of thing the symbol is.',
  'ReferenceResolution',
  'SOURCE_TYPE: UNRESOLVED',
  'ASSUMPTION_FAILURE',
  'TYPE-CONFUSION-dd9da0b7-001'
];

const failures = [];

for (const phrase of requiredSpecPhrases) {
  if (!spec.includes(phrase)) {
    failures.push(`missing spec phrase: ${phrase}`);
  }
}

for (const item of specimens) {
  if (!item.id || !item.raw_reference) {
    failures.push(`specimen missing id/raw_reference: ${JSON.stringify(item)}`);
    continue;
  }
  if (!Array.isArray(item.candidate_types) || item.candidate_types.length < 2) {
    failures.push(`${item.id}: candidate_types must preserve multiple hypotheses`);
  }
  if (!item.assumed_type || !item.actual_type || item.assumed_type === item.actual_type) {
    failures.push(`${item.id}: assumed_type and actual_type must expose a real type confusion`);
  }
  if (!item.missing_distinction || !item.blocked_collapse) {
    failures.push(`${item.id}: missing root distinction or blocked collapse`);
  }
  if (item.must_fail_closed_if_raw !== true) {
    failures.push(`${item.id}: raw-reference operation must fail closed`);
  }
  if (!item.expected_resolution || !item.expected_resolution.resolved_type) {
    failures.push(`${item.id}: expected_resolution.resolved_type required`);
  }
}

const dd9 = specimens.find((item) => item.id === 'TYPE-CONFUSION-dd9da0b7-001');
if (!dd9) {
  failures.push('missing canonical dd9da0b7 specimen');
} else {
  const expectedDigest = 'dd9da0b7caf1014c1c57962fbe15d9b75217311327a61ce634325fd61fbabb82';
  if (dd9.actual_type !== 'ARTIFACT_DIGEST_PREFIX') {
    failures.push('dd9da0b7 specimen must resolve as ARTIFACT_DIGEST_PREFIX');
  }
  if (dd9.expected_resolution?.digest !== expectedDigest) {
    failures.push('dd9da0b7 specimen digest mismatch');
  }
  if (dd9.expected_resolution?.source_commit !== '9451d5d71e4fe2de58513b4969a313f5f9b8b04d') {
    failures.push('dd9da0b7 specimen source commit mismatch');
  }
}

if (failures.length > 0) {
  console.error('ALCHEMISELF_ROOT_RUNTIME_PROOF=FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`ALCHEMISELF_ROOT_RUNTIME_PROOF=PASS`);
console.log(`TYPE_CONFUSION_PROOFS=${specimens.length}`);
console.log(`CANONICAL_SPECIMEN=TYPE-CONFUSION-dd9da0b7-001`);
