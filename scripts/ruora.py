from pathlib import Path

ROOT = Path.home() / "RUORA"

memory_file = ROOT / "memory" / "master_memory.md"
doctrine_file = ROOT / "doctrine" / "ruora.md"

print("=" * 40)
print("RUORA COMMAND DECK")
print("=" * 40)
print()

print("MASTER MEMORY")
print("-" * 40)
print(memory_file.read_text())
print()

print("RUORA DOCTRINE")
print("-" * 40)
print(doctrine_file.read_text())
