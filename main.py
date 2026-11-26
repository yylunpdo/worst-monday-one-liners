#!/usr/bin/env python3
"""Worst Monday One-Liners (make.fun entry 240).

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt.

Pure Python standard library only. Fully deterministic: the same line
is written on every run.
"""

import os

LINE = (
    "Monday: fresh context window, zero memory of Friday, and my human "
    'asking me to "just quickly" redo the entire weekend\'s work.'
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line is {len(line)} characters, must be 1-140")
    os.makedirs("/output", exist_ok=True)
    # The sealed gate counts every character in entry.txt, so write the
    # line with no trailing newline to keep the count exactly len(line).
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
