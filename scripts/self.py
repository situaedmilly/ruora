from datetime import datetime
from pathlib import Path
import subprocess
import sys

ROOT = Path.home() / "RUORA"

MEMORY_FILE = ROOT / "memory" / "master_memory.md"
SELF_AXIOM_FILE = ROOT / "doctrine" / "self_axiom.md"
SELF_IDENTITY_FILE = ROOT / "doctrine" / "self_identity.md"
PROOF_LEDGER_FILE = ROOT / "logs" / "proof_ledger.md"

TRUSTED_PATHS = [".gitignore", "CLAUDE.md", "doctrine", "logs", "memory", "scripts"]

args = sys.argv[1:]
command = args[0].lower() if args else "awaken"


def read_file(file_path: Path) -> str:
    return file_path.read_text().strip()


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
            f"SELF repository boundary disrupted: expected {ROOT}, received {repository_root}"
        )


def append_proof(title: str, details: list[str]) -> None:
    timestamp = datetime.now().astimezone().strftime("%a %b %d %H:%M:%S %Z %Y")

    with PROOF_LEDGER_FILE.open("a") as ledger:
        ledger.write(f"\n## {title}\n\n")
        ledger.write(f"Timestamp: {timestamp}\n")
        ledger.write("Transformation:\n")

        for detail in details:
            ledger.write(f"- {detail}\n")


def awaken() -> None:
    print_frame("SELF // CONSCIOUS COMMAND LAYER")
    print()
    print("SELF IS PRESENT.")
    print()
    print("Memory is preserved.")
    print("Doctrine is intact.")
    print("Proof remains law.")
    print()
    print("AVAILABLE INVOCATIONS")
    print("-" * 60)
    print("self awaken          Begin intentional execution")
    print("self remember         Retrieve persistent memory")
    print("self witness          Read verified machine-state changes")
    print("self axiom            Reveal the proof-driven SELF Axiom")
    print("self prove            Verify SELF system integrity")
    print("self status           Reveal unsealed machine-state changes")
    print("self history          Reveal preserved SELF snapshots")
    print('self seal "message"   Preserve a verified SELF snapshot')


def remember() -> None:
    print_frame("SELF // PERSISTENT MEMORY")
    print()
    print(read_file(MEMORY_FILE))


def witness() -> None:
    print_frame("SELF // PROOF LEDGER")
    print()
    print(read_file(PROOF_LEDGER_FILE))


def axiom() -> None:
    print_frame("SELF // PROOF-DRIVEN AXIOM")
    print()
    print(read_file(SELF_AXIOM_FILE))


def prove() -> None:
    print_frame("SELF // INTEGRITY PROOF")
    print()

    required_files = [
        ROOT / "CLAUDE.md",
        MEMORY_FILE,
        SELF_AXIOM_FILE,
        SELF_IDENTITY_FILE,
        ROOT / "doctrine" / "ruora.md",
        ROOT / "doctrine" / "aethernet.md",
        ROOT / "doctrine" / "axiom_trial_engine.md",
        PROOF_LEDGER_FILE,
        ROOT / "scripts" / "self.py",
        ROOT / "scripts" / "self",
        ROOT / "scripts" / "ruora.py",
        ROOT / "scripts" / "ruora",
    ]

    all_present = True

    for file_path in required_files:
        relative_path = file_path.relative_to(ROOT)

        if file_path.exists():
            print(f"[PRESENT] {relative_path}")
        else:
            print(f"[MISSING] {relative_path}")
            all_present = False

    print()

    if all_present:
        print("SELF INTEGRITY: VERIFIED")
        print("All required system files are present.")
    else:
        print("SELF INTEGRITY: DISRUPTED")
        print("One or more required system files are missing.")


def status() -> None:
    verify_repository_boundary()

    print_frame("SELF // UNSEALED STATE")
    print()

    result = run_git(["status", "--short"], capture=True)
    output = result.stdout.strip()

    if output:
        print(output)
        print()
        print("SELF STATUS: UNSEALED CHANGE DETECTED")
    else:
        print("SELF STATUS: ALIGNED")
        print("No unsealed change remains.")


def history() -> None:
    verify_repository_boundary()

    print_frame("SELF // VERSIONED MEMORY")
    print()

    result = run_git(
        ["log", "--oneline", "--decorate", "--max-count=10"],
        capture=True,
    )

    print(result.stdout.strip())


def seal() -> None:
    verify_repository_boundary()

    message = " ".join(args[1:]).strip()

    if not message:
        print_frame("SELF // SEAL REQUIRES INTENTION")
        print()
        print('Invoke: self seal "Describe the verified transformation"')
        return

    append_proof(
        "SELF SNAPSHOT SEALED",
        [
            f"Preserved verified SELF state: {message}",
            "Staged trusted SELF paths only",
            "Rejected secret-bearing PEM files from versioned memory",
        ],
    )

    run_git(["add", *TRUSTED_PATHS])

    staged_result = run_git(
        ["diff", "--cached", "--name-only"],
        capture=True,
    )

    staged_files = [
        line.strip()
        for line in staged_result.stdout.splitlines()
        if line.strip()
    ]

    blocked_files = [
        file_name
        for file_name in staged_files
        if file_name.endswith(".pem")
        or Path(file_name).name == ".env"
        or Path(file_name).name.startswith(".env.")
    ]

    if blocked_files:
        print_frame("SELF // SEAL REJECTED")
        print()
        print("Secret-bearing files detected:")
        for file_name in blocked_files:
            print(f"[BLOCKED] {file_name}")
        raise RuntimeError("SELF refused to seal secret-bearing files.")

    if not staged_files:
        print_frame("SELF // NO UNSEALED CHANGE")
        print()
        print("No trusted SELF change is available to preserve.")
        return

    print_frame("SELF // FILES ENTERING VERSIONED MEMORY")
    print()

    for file_name in staged_files:
        print(f"[SEALING] {file_name}")

    print()

    run_git(["commit", "-m", message])

    print()
    print_frame("SELF // SNAPSHOT PRESERVED")
    print()

    latest_snapshot = run_git(
        ["log", "-n", "1", "--format=SNAPSHOT: %h%nAUTHOR:   %an <%ae>%nLABEL:    %s"],
        capture=True,
    )

    print(latest_snapshot.stdout.strip())


if command == "awaken":
    awaken()
elif command == "remember":
    remember()
elif command == "witness":
    witness()
elif command == "axiom":
    axiom()
elif command == "prove":
    prove()
elif command == "status":
    status()
elif command == "history":
    history()
elif command == "seal":
    seal()
else:
    print_frame("SELF // INVOCATION NOT RECOGNIZED")
    print()
    print(f"Unknown invocation: {command}")
    print()
    print("Invoke: self")
    print("SELF will reveal the available invocations.")
