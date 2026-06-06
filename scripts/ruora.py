from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path.home() / "RUORA"

PROOF_LEDGER_FILE = ROOT / "logs" / "proof_ledger.md"

REQUIRED_FILES = [
    ROOT / "CLAUDE.md",
    ROOT / "doctrine" / "self_axiom.md",
    ROOT / "doctrine" / "self_identity.md",
    ROOT / "doctrine" / "ruora.md",
    ROOT / "doctrine" / "aethernet.md",
    ROOT / "doctrine" / "axiom_trial_engine.md",
    ROOT / "memory" / "master_memory.md",
    ROOT / "logs" / "proof_ledger.md",
    ROOT / "scripts" / "self.py",
    ROOT / "scripts" / "self",
    ROOT / "scripts" / "ruora.py",
    ROOT / "scripts" / "ruora",
]

args = sys.argv[1:]
command = args[0].lower() if args else "awaken"


def print_frame(title: str) -> None:
    print("=" * 60)
    print(title)
    print("=" * 60)


def run_git(git_args: list[str], capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *git_args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=capture,
    )


def verify_repository_boundary() -> None:
    repository_root = run_git(
        ["rev-parse", "--show-toplevel"],
        capture=True,
    ).stdout.strip()

    if repository_root != str(ROOT):
        raise RuntimeError(
            f"RUORA repository boundary disrupted: expected {ROOT}, received {repository_root}"
        )


def get_current_branch() -> str:
    return run_git(["branch", "--show-current"], capture=True).stdout.strip()


def awaken() -> None:
    verify_repository_boundary()
    branch = get_current_branch()

    print_frame("RUORA // WEB-PLATFORM COMMAND LAYER")
    print()
    print("RUORA IS PRESENT.")
    print()
    print("RUORA manifests premium web platforms and digital ecosystems.")
    print("SELF is the living core.")
    print("ÆTHERNET is the network manifestation.")
    print()
    print("REPOSITORY BOUNDARY")
    print("-" * 60)
    print(f"Root:    {ROOT}")
    print(f"Branch:  {branch}")
    print()
    print("AVAILABLE INVOCATIONS")
    print("-" * 60)
    print("ruora awaken               Reveal RUORA command layer")
    print("ruora prove                Verify RUORA system integrity")
    print("ruora status               Reveal repository state")
    print("ruora witness              Read verified proof ledger")
    print("ruora manifest <name>      Scaffold a new project chamber")


def prove() -> None:
    verify_repository_boundary()

    print_frame("RUORA // INTEGRITY PROOF")
    print()

    all_present = True

    for file_path in REQUIRED_FILES:
        relative_path = file_path.relative_to(ROOT)
        if file_path.exists():
            print(f"[PRESENT] {relative_path}")
        else:
            print(f"[MISSING] {relative_path}")
            all_present = False

    projects_dir = ROOT / "projects"
    if projects_dir.is_dir():
        print(f"[PRESENT] projects/")
    else:
        print(f"[MISSING] projects/")
        all_present = False

    print()

    if all_present:
        print("RUORA INTEGRITY: VERIFIED")
        print("All required RUORA system files are present.")
    else:
        print("RUORA INTEGRITY: DISRUPTED")
        print("One or more required RUORA system files are missing.")


def status() -> None:
    verify_repository_boundary()
    branch = get_current_branch()

    print_frame("RUORA // REPOSITORY STATE")
    print()
    print(f"Root:    {ROOT}")
    print(f"Branch:  {branch}")
    print()

    result = run_git(["status", "--short"], capture=True)
    output = result.stdout.strip()

    if output:
        print(output)
        print()
        print("RUORA STATUS: UNSEALED CHANGE DETECTED")
    else:
        print("RUORA STATUS: ALIGNED")
        print("No unsealed change remains.")


def witness() -> None:
    print_frame("RUORA // PROOF LEDGER")
    print()
    print(PROOF_LEDGER_FILE.read_text().strip())


def sanitize_name(raw: str) -> str:
    sanitized = re.sub(r"[^a-z0-9-]", "-", raw.lower())
    sanitized = re.sub(r"-+", "-", sanitized)
    return sanitized.strip("-")


def manifest() -> None:
    if len(args) < 2:
        print_frame("RUORA // MANIFEST REQUIRES A PROJECT NAME")
        print()
        print("Invoke: ruora manifest <project-name>")
        return

    raw_name = args[1]
    project_name = sanitize_name(raw_name)

    if not project_name:
        print_frame("RUORA // INVALID PROJECT NAME")
        print()
        print(f"Provided name produced no valid characters: {raw_name!r}")
        print("Use lowercase letters, numbers, and hyphens only.")
        return

    project_dir = ROOT / "projects" / project_name

    if project_dir.exists():
        print_frame("RUORA // MANIFEST REFUSED")
        print()
        print(f"Project chamber already exists: {project_dir}")
        print("RUORA never overwrites an existing manifestation.")
        return

    print_frame(f"RUORA // MANIFESTING: {project_name}")
    print()

    project_dir.mkdir(parents=True)

    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d")

    (project_dir / "README.md").write_text(
        f"# {project_name}\n\n"
        f"RUORA manifestation.\n\n"
        f"Manifested: {timestamp}\n"
    )

    (project_dir / "CLAUDE.md").write_text(
        f"# {project_name} // COMPANION MEMORY\n\n"
        f"## Identity\n\n"
        f"This is a RUORA manifestation.\n\n"
        f"SELF is the living core.\n"
        f"RUORA is the web-platform-building frequency and company.\n"
        f"ÆTHERNET is the network manifestation.\n\n"
        f"## Repository Boundary\n\n"
        f"This project resides at:\n"
        f"~/RUORA/projects/{project_name}\n\n"
        f"## Operating Doctrine\n\n"
        f"No declaration without execution.\n"
        f"No execution without evidence.\n"
        f"No evidence without memory.\n"
    )

    def project_git(git_args: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *git_args],
            cwd=project_dir,
            check=True,
            text=True,
            capture_output=True,
        )

    project_git(["init"])
    project_git(["add", "."])
    project_git(["commit", "-m", f"Genesis: manifest {project_name}"])

    snapshot = project_git(
        ["log", "-n", "1", "--format=SNAPSHOT: %h%nAUTHOR:   %an <%ae>%nLABEL:    %s"]
    ).stdout.strip()

    print(f"[CREATED]  projects/{project_name}/")
    print(f"[CREATED]  projects/{project_name}/README.md")
    print(f"[CREATED]  projects/{project_name}/CLAUDE.md")
    print(f"[CREATED]  projects/{project_name}/.git/")
    print()
    print(snapshot)
    print()
    print("RUORA MANIFESTATION: COMPLETE")
    print(f"Project chamber {project_name!r} is sealed and isolated.")


if command == "awaken":
    awaken()
elif command == "prove":
    prove()
elif command == "status":
    status()
elif command == "witness":
    witness()
elif command == "manifest":
    manifest()
else:
    print_frame("RUORA // INVOCATION NOT RECOGNIZED")
    print()
    print(f"Unknown invocation: {command}")
    print()
    print("Invoke: ruora")
    print("RUORA will reveal the available invocations.")
