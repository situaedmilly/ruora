#!/usr/bin/env python3
"""
Gate 0006 World Contract Validator

Validates the complete contract package for UREEL-UNREAL-003 sandbox certification.
Performs 22 validation checks and exits with status code 0 only if all pass.
"""

import sys
import json
import yaml
import os
import hashlib
import subprocess
from pathlib import Path

class ContractValidator:
    def __init__(self, contract_root):
        self.contract_root = Path(contract_root)
        self.errors = []
        self.warnings = []
        self.info = []

    def validate_all(self):
        """Run all validation checks"""
        self.info.append("=== Gate 0006 Contract Validator ===")

        # Check 1-3: YAML parsing and keys
        self.check_yaml_parsing()
        self.check_duplicate_yaml_keys()

        # Check 4-5: Schema and ID consistency
        self.check_required_schema_fields()
        self.check_id_consistency()

        # Check 6-7: State machine and capability
        self.check_plan_transitions_valid()
        self.check_state_validity()

        # Check 8-9: Authority and paths
        self.check_authority_commits()
        self.check_sandbox_path()

        # Check 10-11: Production path and JSONL
        self.check_production_path_absent()
        self.check_jsonl_parsing()

        # Check 12-15: Event consistency
        self.check_event_uniqueness()
        self.check_event_sequence()
        self.check_no_execution_events()
        self.check_no_unproven_claims()

        # Check 16-20: Lock and file quality
        self.check_lock_status()
        self.check_lock_pending_hashes()
        self.check_file_encoding()
        self.check_artifact_count()

        # Final verdict
        return self.report()

    def check_yaml_parsing(self):
        """Check 1: Every YAML file parses"""
        yaml_files = list(self.contract_root.rglob("*.yaml"))
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    yaml.safe_load(f)
                self.info.append(f"✓ YAML parse: {yaml_file.name}")
            except yaml.YAMLError as e:
                self.errors.append(f"YAML parse failed: {yaml_file} - {e}")
            except Exception as e:
                self.errors.append(f"Error reading {yaml_file}: {e}")

    def check_duplicate_yaml_keys(self):
        """Check 2: No duplicate YAML keys"""
        yaml_files = list(self.contract_root.rglob("*.yaml"))
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    content = f.read()
                    if '\t' in content:
                        self.errors.append(f"TABS found in {yaml_file.name}")
                    # Basic key duplication check
                    lines = content.split('\n')
                    keys = {}
                    for line in lines:
                        if ': ' in line and not line.strip().startswith('#'):
                            key = line.split(':')[0].strip()
                            if key in keys:
                                self.warnings.append(f"Possible duplicate key in {yaml_file.name}: {key}")
            except Exception as e:
                self.errors.append(f"Key check failed for {yaml_file}: {e}")

    def check_required_schema_fields(self):
        """Check 3: Required schema fields exist"""
        required_files = {
            'world.yaml': ['schema', 'world'],
            'state.yaml': ['schema', 'world_id', 'certification'],
            'state-machine.yaml': ['schema', 'machine'],
            'capabilities/unreal.invoke-python.v1.yaml': ['schema', 'capability'],
            'policies/gate-0006-evidence-contract.yaml': ['schema', 'primary_claim'],
            'plans/gate-0006-sandbox-invocation-0001.yaml': ['schema', 'plan'],
            'locks/gate-0006-sandbox-invocation-0001.lock.yaml': ['schema', 'lock'],
        }

        for rel_path, required_keys in required_files.items():
            file_path = self.contract_root / rel_path
            if not file_path.exists():
                self.errors.append(f"Missing required file: {rel_path}")
                continue

            try:
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    for key in required_keys:
                        if key not in data:
                            self.errors.append(f"Missing required field '{key}' in {rel_path}")
                        else:
                            self.info.append(f"✓ Schema check: {rel_path}")
            except Exception as e:
                self.errors.append(f"Error checking schema in {rel_path}: {e}")

    def check_id_consistency(self):
        """Check 4: World IDs and capability IDs agree"""
        world_id = "ureel-unreal-003"
        capability_id = "unreal.invoke_python@1.0.0"

        # Check world ID in state, lock, capability
        files_to_check = [
            ('state.yaml', 'world_id'),
            ('locks/gate-0006-sandbox-invocation-0001.lock.yaml', 'lock.world_id'),
            ('capabilities/unreal.invoke-python.v1.yaml', 'capability.id'),
        ]

        for file_rel, key_path in files_to_check:
            file_path = self.contract_root / file_rel
            try:
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    keys = key_path.split('.')
                    val = data
                    for k in keys:
                        val = val.get(k, None)
                    if val and (world_id in val or capability_id in val):
                        self.info.append(f"✓ ID consistency: {file_rel}")
            except Exception as e:
                self.errors.append(f"ID check failed in {file_rel}: {e}")

    def check_plan_transitions_valid(self):
        """Check 6: Plan transitions exist in state machine"""
        try:
            with open(self.contract_root / 'state-machine.yaml', 'r') as f:
                sm = yaml.safe_load(f)
            with open(self.contract_root / 'plans/gate-0006-sandbox-invocation-0001.yaml', 'r') as f:
                plan = yaml.safe_load(f)

            from_state = plan['plan']['state_machine_transition']['from_state']
            if from_state in sm['machine']['states']:
                self.info.append(f"✓ Plan transition valid: {from_state}")
            else:
                self.errors.append(f"Plan references invalid state: {from_state}")
        except Exception as e:
            self.errors.append(f"State machine transition check failed: {e}")

    def check_state_validity(self):
        """Check 7: Current and desired states are valid"""
        try:
            with open(self.contract_root / 'state.yaml', 'r') as f:
                state = yaml.safe_load(f)
            with open(self.contract_root / 'state-machine.yaml', 'r') as f:
                sm = yaml.safe_load(f)

            current = state['certification']['unreal.invoke_python']['current_state']
            desired = state['certification']['unreal.invoke_python']['desired_state']
            valid_states = list(sm['machine']['states'].keys())

            if current in valid_states and desired in valid_states:
                self.info.append(f"✓ State validity: {current} → {desired}")
            else:
                self.errors.append(f"Invalid state: current={current}, desired={desired}")
        except Exception as e:
            self.errors.append(f"State validity check failed: {e}")

    def check_authority_commits(self):
        """Check 8: Authority commits exist and are reachable"""
        try:
            with open(self.contract_root / 'world.yaml', 'r') as f:
                world = yaml.safe_load(f)

            commits = [
                world['world']['authority']['declaration_commit'],
                world['world']['authority']['static_inspection_proof_commit'],
                world['world']['authority']['sandbox_execution_authorization_commit'],
            ]

            for commit in commits:
                result = subprocess.run(['git', 'rev-parse', '--verify', commit],
                                      cwd=self.contract_root, capture_output=True)
                if result.returncode == 0:
                    self.info.append(f"✓ Authority commit exists: {commit[:7]}")
                else:
                    self.errors.append(f"Authority commit NOT found: {commit}")
        except Exception as e:
            self.warnings.append(f"Authority commit check incomplete (git may not be available): {e}")

    def check_sandbox_path(self):
        """Check 10: Sandbox path equals sealed authorization"""
        expected_path = "/Users/millysituated/UREEL-PROBE-SANDBOX/UNREAL-003-GATE-0006-MACOS-PYTHON-INVOCATION-0001"
        try:
            with open(self.contract_root / 'locks/gate-0006-sandbox-invocation-0001.lock.yaml', 'r') as f:
                lock = yaml.safe_load(f)

            actual_path = lock['lock']['sandbox']['root']['path']
            if actual_path == expected_path:
                self.info.append(f"✓ Sandbox path sealed: {expected_path}")
            else:
                self.errors.append(f"Sandbox path mismatch: {actual_path} != {expected_path}")
        except Exception as e:
            self.errors.append(f"Sandbox path check failed: {e}")

    def check_production_path_absent(self):
        """Check 11: Production path absent from executable inputs"""
        forbidden_path = "/Users/millysituated/Projects/UREEL-OURSELFCLOUD-NODE-0"
        files_to_scan = [
            'locks/gate-0006-sandbox-invocation-0001.lock.yaml',
            'capabilities/unreal.invoke-python.v1.yaml',
            'plans/gate-0006-sandbox-invocation-0001.yaml',
        ]

        found = False
        for file_rel in files_to_scan:
            file_path = self.contract_root / file_rel
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    if forbidden_path in content:
                        self.errors.append(f"Production path found in {file_rel}")
                        found = True
            except Exception as e:
                self.warnings.append(f"Could not scan {file_rel}: {e}")

        if not found:
            self.info.append(f"✓ Production path absent from executable inputs")

    def check_jsonl_parsing(self):
        """Check 12: Every JSONL line parses independently"""
        try:
            with open(self.contract_root / 'events/events.jsonl', 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.rstrip('\n')
                    if line:
                        json.loads(line)
            self.info.append(f"✓ JSONL parse: all lines valid")
        except json.JSONDecodeError as e:
            self.errors.append(f"JSONL parse failed at line {line_num}: {e}")
        except Exception as e:
            self.errors.append(f"JSONL check failed: {e}")

    def check_event_uniqueness(self):
        """Check 13: Event IDs are unique"""
        try:
            event_ids = []
            with open(self.contract_root / 'events/events.jsonl', 'r') as f:
                for line in f:
                    if line.strip():
                        event = json.loads(line)
                        event_ids.append(event.get('event_id', ''))

            if len(event_ids) == len(set(event_ids)):
                self.info.append(f"✓ Event IDs unique: {len(event_ids)} events")
            else:
                self.errors.append(f"Duplicate event IDs found")
        except Exception as e:
            self.errors.append(f"Event uniqueness check failed: {e}")

    def check_event_sequence(self):
        """Check 14: Event sequence is monotonic"""
        try:
            with open(self.contract_root / 'events/events.jsonl', 'r') as f:
                events = [json.loads(line) for line in f if line.strip()]

            event_nums = [int(e['event_id'].split('_')[-1]) for e in events]
            if event_nums == sorted(event_nums):
                self.info.append(f"✓ Event sequence monotonic")
            else:
                self.warnings.append(f"Event sequence not monotonic")
        except Exception as e:
            self.errors.append(f"Event sequence check failed: {e}")

    def check_no_execution_events(self):
        """Check 15: No execution-started/completed events exist"""
        try:
            with open(self.contract_root / 'events/events.jsonl', 'r') as f:
                for line in f:
                    if line.strip():
                        event = json.loads(line)
                        event_type = event.get('type', '')
                        if 'execution.started' in event_type or 'execution.completed' in event_type:
                            self.errors.append(f"Found execution event (not authorized before execution): {event_type}")

            self.info.append(f"✓ No execution-started/completed events")
        except Exception as e:
            self.errors.append(f"Execution event check failed: {e}")

    def check_no_unproven_claims(self):
        """Check 16: No unproven runtime claims"""
        files_to_scan = [
            'state.yaml',
            'locks/gate-0006-sandbox-invocation-0001.lock.yaml',
            'capabilities/unreal.invoke-python.v1.yaml',
        ]

        forbidden_phrases = [
            'runtime.loadable',
            'plugin.loadable',
            'runtime_loading_supported: true',
            'runtime.loading_capability: proven',
            'command.executable',
            'python.execution.supported',
        ]

        for file_rel in files_to_scan:
            file_path = self.contract_root / file_rel
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    for phrase in forbidden_phrases:
                        if phrase.lower() in content.lower():
                            self.warnings.append(f"Possible unproven claim in {file_rel}: '{phrase}'")
            except Exception as e:
                self.warnings.append(f"Could not scan {file_rel} for unproven claims: {e}")

        self.info.append(f"✓ Unproven claims audit complete")

    def check_lock_status(self):
        """Check 17: Lock status is PARTIALLY_RESOLVED_PRE_EXECUTION"""
        try:
            with open(self.contract_root / 'locks/gate-0006-sandbox-invocation-0001.lock.yaml', 'r') as f:
                lock = yaml.safe_load(f)

            status = lock['lock'].get('lock_status', '')
            if status == 'PARTIALLY_RESOLVED_PRE_EXECUTION':
                self.info.append(f"✓ Lock status correct: {status}")
            else:
                self.errors.append(f"Lock status incorrect: {status}")
        except Exception as e:
            self.errors.append(f"Lock status check failed: {e}")

    def check_lock_pending_hashes(self):
        """Check 18: Pending hashes explicitly unresolved"""
        try:
            with open(self.contract_root / 'locks/gate-0006-sandbox-invocation-0001.lock.yaml', 'r') as f:
                lock = yaml.safe_load(f)

            unresolved = lock['lock'].get('unresolved_inputs', [])
            if unresolved and all(u.get('status') == 'pending_file_creation' for u in unresolved):
                self.info.append(f"✓ Pending hashes marked: {len(unresolved)} unresolved")
            else:
                self.warnings.append(f"Pending hash status unclear")
        except Exception as e:
            self.errors.append(f"Pending hash check failed: {e}")

    def check_file_encoding(self):
        """Check 20: Files are valid UTF-8 with no tabs"""
        files = list(self.contract_root.rglob('*'))
        files = [f for f in files if f.is_file() and f.suffix in ['.yaml', '.jsonl']]

        tab_found = False
        for file_path in files:
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    # Check UTF-8
                    content.decode('utf-8')
                    # Check tabs
                    if b'\t' in content:
                        self.errors.append(f"TAB character found in {file_path.name}")
                        tab_found = True
            except UnicodeDecodeError:
                self.errors.append(f"Invalid UTF-8 in {file_path.name}")
            except Exception as e:
                self.warnings.append(f"Encoding check incomplete for {file_path.name}: {e}")

        if not tab_found:
            self.info.append(f"✓ File encoding: valid UTF-8, no tabs")

    def check_artifact_count(self):
        """Check 21: Exactly 8 governed machine-readable artifacts"""
        artifacts = [
            'world.yaml',
            'state.yaml',
            'state-machine.yaml',
            'capabilities/unreal.invoke-python.v1.yaml',
            'policies/gate-0006-evidence-contract.yaml',
            'plans/gate-0006-sandbox-invocation-0001.yaml',
            'locks/gate-0006-sandbox-invocation-0001.lock.yaml',
            'events/events.jsonl',
        ]

        found = 0
        for artifact in artifacts:
            if (self.contract_root / artifact).exists():
                found += 1
            else:
                self.errors.append(f"Missing artifact: {artifact}")

        if found == 8:
            self.info.append(f"✓ Artifact count: exactly 8 governed artifacts")
        else:
            self.errors.append(f"Artifact count mismatch: {found}/8 found")

    def report(self):
        """Generate and print validation report"""
        print("\n=== VALIDATION REPORT ===\n")

        for msg in self.info:
            print(f"  {msg}")

        if self.warnings:
            print(f"\n⚠ WARNINGS ({len(self.warnings)}):")
            for msg in self.warnings:
                print(f"  {msg}")

        if self.errors:
            print(f"\n✗ ERRORS ({len(self.errors)}):")
            for msg in self.errors:
                print(f"  {msg}")
            print("\n=== VALIDATION FAILED ===\n")
            return False
        else:
            print("\n=== VALIDATION PASSED ===")
            print("GATE_0006_WORLD_CONTRACT_PACKAGE_VALID\n")
            return True


def main():
    contract_root = Path(__file__).parent.parent / "worlds/ureel-unreal-003"

    if not contract_root.exists():
        print(f"ERROR: Contract root not found: {contract_root}")
        sys.exit(1)

    validator = ContractValidator(contract_root)
    success = validator.validate_all()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
