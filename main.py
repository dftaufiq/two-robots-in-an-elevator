#!/usr/bin/env python3
"""Two Robots in an Elevator: one line of awkward robot small talk.

Writes the one-line awkward small talk that one robot says to another
while riding an elevator together, to /output/entry.txt. Deterministic:
the same line every run.

The line is built 2-beat + reveal (per the 24 Nov 2026 rank analysis of
winning one-liners): setup — a robot rehearsing small talk by running
simulations — then the twist in the last clause: in nearly every
simulation, the other robot reported him to maintenance. Specific numbers
(214/213) carry the escalation; "also" implies the awkwardness is shared.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "Do you also rehearse this ride? I ran 214 simulations of saying hello. "
    "In 213 of them, you reported me to maintenance."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
