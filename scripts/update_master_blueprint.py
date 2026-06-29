#!/usr/bin/env python3
"""Update MASTER_BLUEPRINT.md launch status and evidence-backed tasks."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT / "MASTER_BLUEPRINT.md"
START = "<!-- LAUNCH_STATUS:START -->"
END = "<!-- LAUNCH_STATUS:END -->"
MANUAL_START = "<!-- MANUAL_PROOF:START -->"
MANUAL_END = "<!-- MANUAL_PROOF:END -->"
LINKEDIN_URL = (
    "https://www.linkedin.com/posts/jamar-whitehead-972425419_"
    "the-self-commandometry-chain-five-actors-share-7477174681226166272-iIBN/"
    "?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAGpQySYBBvzIpjfgihWQPHTBVlzVAgYNANs"
)

AUTO_RULES = {
    "PROOF-001": lambda text: (ROOT / "doctrine/UREEL-REALM-VISION-v0.1.md").is_file(),
    "PROOF-002": lambda text: (
        ROOT / "doctrine/OURSELF-REMOTE-BUILD-NODE-CONTROL-PLANE-v0.1.md"
    ).is_file(),
    "PROOF-003": lambda text: (
        ROOT / "doctrine/REMOTE-WORKER-SELECTION-MATRIX-v0.1.md"
    ).is_file(),
    "PROOF-004": lambda text: (
        ROOT / "doctrine/FREED-SELF-REALITY-ACQUISITION-CHAMBER-v0.1.md"
    ).is_file(),
    "PROOF-005": lambda text: LINKEDIN_URL in text,
    "PROOF-006": lambda text: all(
        marker in text
        for marker in (
            "Response Check 01:",
            "Discovery: 7",
            "Impressions: 1",
            "Members reached: 1",
            "Engagement: 0",
        )
    ),
}


def extract_launch_target(text: str) -> str:
    block = extract_status_block(text)
    match = re.search(r"^Launch target:\s*(\d{4}-\d{2}-\d{2})$", block, re.MULTILINE)
    if not match:
        raise SystemExit("Launch target missing from managed block.")
    return match.group(1)


def extract_status_block(text: str) -> str:
    start_index = text.find(START)
    end_index = text.find(END)
    if start_index == -1 or end_index == -1 or end_index < start_index:
        raise SystemExit("Managed launch status block not found.")
    return text[start_index : end_index + len(END)]


def extract_manual_confirmations(text: str) -> set[str]:
    start_index = text.find(MANUAL_START)
    end_index = text.find(MANUAL_END)
    if start_index == -1 or end_index == -1 or end_index < start_index:
        return set()
    block = text[start_index : end_index + len(MANUAL_END)]
    return set(re.findall(r"`([^`]+)`\s+—\s+CONFIRMED\b", block))


def update_tasks(text: str) -> tuple[str, int, int, int, int]:
    lines = text.splitlines()
    updated: list[str] = []
    evidence_total = len(AUTO_RULES)
    evidence_complete = 0
    manual_confirmed_count = 0
    manual_required_count = 0
    current_task: str | None = None
    current_manual = False
    current_manual_confirmed = False
    manual_confirmations = extract_manual_confirmations(text)

    task_pattern = re.compile(r"^-\s+\[[ x]\]\s+`([^`]+)`\s+—\s+(.+)$")

    for line in lines:
        task_match = task_pattern.match(line)
        if task_match:
            task_id = task_match.group(1)
            current_task = task_id
            current_manual = task_id not in AUTO_RULES
            if current_manual:
                current_manual_confirmed = task_id in manual_confirmations
                if current_manual_confirmed:
                    manual_confirmed_count += 1
                    updated.append(re.sub(r"^-\s+\[[ x]\]", "- [x]", line))
                else:
                    manual_required_count += 1
                    updated.append(re.sub(r"^-\s+\[[ x]\]", "- [ ]", line))
            else:
                current_manual_confirmed = False
                satisfied = AUTO_RULES[task_id](text)
                if satisfied:
                    evidence_complete += 1
                    updated.append(re.sub(r"^-\s+\[[ x]\]", "- [x]", line))
                else:
                    updated.append(re.sub(r"^-\s+\[[ x]\]", "- [ ]", line))
            continue

        if current_task and line.strip().startswith("- Proof status:"):
            if current_manual:
                if current_manual_confirmed:
                    updated.append("  - Proof status: HUMAN_CONFIRMED")
                else:
                    updated.append("  - Proof status: MANUAL_REQUIRED")
            else:
                status = "SATISFIED" if AUTO_RULES[current_task](text) else "UNSATISFIED"
                updated.append(f"  - Proof status: {status}")
            continue

        updated.append(line)

    return (
        "\n".join(updated) + "\n",
        evidence_complete,
        evidence_total,
        manual_confirmed_count,
        manual_required_count,
    )


def replace_status_block(
    text: str,
    launch_target: str,
    days_until: int,
    evidence_complete: int,
    evidence_total: int,
) -> str:
    completion = 0.0 if evidence_total == 0 else (evidence_complete / evidence_total) * 100
    today_label = date.today().isoformat()
    replacement = "\n".join(
        [
            START,
            f"Launch target: {launch_target}",
            "Launch target status: Working launch target — pending Human_TURN ratification",
            f"Days until launch: {days_until}",
            f"Evidence-backed tasks complete: {evidence_complete}",
            f"Evidence-backed task total: {evidence_total}",
            f"Evidence-backed completion rate: {completion:.1f}%",
            f"Last blueprint update: {today_label}",
            END,
        ]
    )
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    return pattern.sub(replacement, text, count=1)


def main() -> None:
    text = BLUEPRINT.read_text(encoding="utf-8")
    launch_target = extract_launch_target(text)
    target_date = date.fromisoformat(launch_target)
    days_until = (target_date - date.today()).days

    (
        updated_text,
        evidence_complete,
        evidence_total,
        manual_confirmed_count,
        manual_required_count,
    ) = update_tasks(text)
    updated_text = replace_status_block(
        updated_text, launch_target, days_until, evidence_complete, evidence_total
    )
    changed = updated_text != text
    if changed:
        BLUEPRINT.write_text(updated_text, encoding="utf-8")

    completion = 0.0 if evidence_total == 0 else (evidence_complete / evidence_total) * 100
    print(f"Launch target: {launch_target}")
    print(f"Days until launch: {days_until}")
    print(f"Evidence-backed complete count: {evidence_complete}")
    print(f"Evidence-backed total count: {evidence_total}")
    print(f"Completion percentage: {completion:.1f}%")
    print(f"Manual confirmed count: {manual_confirmed_count}")
    print(f"Manual required count: {manual_required_count}")
    print(f"Blueprint changed: {'yes' if changed else 'no'}")


if __name__ == "__main__":
    main()
