#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "dist",
    "__pycache__",
    "__archive",
}

LANGUAGES = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".php": "PHP",
    ".css": "CSS",
    ".html": "HTML",
    ".md": "Markdown",
}

stats = defaultdict(lambda: {
    "files": 0,
    "lines": 0,
    "non_empty": 0,
})


for file in ROOT.rglob("*"):
    if not file.is_file():
        continue

    if any(part in EXCLUDED_DIRS for part in file.parts):
        continue

    language = LANGUAGES.get(file.suffix.lower())

    if language is None:
        continue

    try:
        lines = file.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        continue

    stats[language]["files"] += 1
    stats[language]["lines"] += len(lines)
    stats[language]["non_empty"] += sum(
        1 for line in lines if line.strip()
    )


print()
print("CR-DSS LOC Analysis")
print("=" * 55)
print(f"{'Language':<15} {'Files':>8} {'LOC':>10} {'Non-empty':>12}")
print("-" * 55)

total_files = 0
total_lines = 0
total_non_empty = 0

for language, values in sorted(
    stats.items(),
    key=lambda item: item[1]["lines"],
    reverse=True
):
    print(
        f"{language:<15} "
        f"{values['files']:>8} "
        f"{values['lines']:>10} "
        f"{values['non_empty']:>12}"
    )

    total_files += values["files"]
    total_lines += values["lines"]
    total_non_empty += values["non_empty"]

print("-" * 55)
print(
    f"{'TOTAL':<15} "
    f"{total_files:>8} "
    f"{total_lines:>10} "
    f"{total_non_empty:>12}"
)
print()