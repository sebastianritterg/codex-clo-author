from __future__ import annotations

import argparse
from pathlib import Path


CANDIDATE_DIRS = [
    "quality_reports",
    "06_paper",
    "paper",
    "talks",
    "figures",
    "tables",
    "04_outputs",
    "03_code",
    "scripts",
    "01_docs",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Snapshot the current research-project state.")
    parser.add_argument("--root", default=".", help="Repository root to inspect.")
    parser.add_argument("--output", default="research_state_snapshot.md", help="Output markdown path.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output).resolve()

    lines = ["# Research State Snapshot", "", f"- Root: `{root}`", "", "## Key Directories"]
    for rel in CANDIDATE_DIRS:
        path = root / rel
        if not path.exists():
            continue
        children = ", ".join(sorted(p.name for p in path.iterdir())[:10]) or "(empty)"
        lines.append(f"- `{rel}`: {children}")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()




