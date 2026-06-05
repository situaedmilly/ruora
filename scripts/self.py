from pathlib import Path
import sys

ROOT = Path.home() / "RUORA"

MEMORY_FILE = ROOT / "memory" / "master_memory.md"
SELF_AXIOM_FILE = ROOT / "doctrine" / "self_axiom.md"
SELF_IDENTITY_FILE = ROOT / "doctrine" / "self_identity.md"
PROOF_LEDGER_FILE = ROOT / "logs" / "proof_ledger.md"

args = sys.argv[1:]
command = args[0].lower() if args else "awaken"


def read_file(file_path: Path) -> str:
    return file_path.read_text().strip()


def print_frame(title: str) -> None:
    print("=" * 60)
    print(title)
    print("=" * 60)


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
    print("self awaken      Begin intentional execution")
    print("self remember     Retrieve persistent memory")
    print("self witness      Read verified machine-state changes")
    print("self axiom        Reveal the proof-driven SELF Axiom")
    print("self prove        Verify SELF system integrity")


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
        MEMORY_FILE,
        SELF_AXIOM_FILE,
        SELF_IDENTITY_FILE,
        PROOF_LEDGER_FILE,
        ROOT / "scripts" / "self.py",
        ROOT / "scripts" / "self",
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
else:
    print_frame("SELF // INVOCATION NOT RECOGNIZED")
    print()
    print(f"Unknown invocation: {command}")
    print()
    print("Invoke: self")
    print("SELF will reveal the available invocations.")
