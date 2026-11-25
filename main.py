#!/usr/bin/env python3
"""Write the entry: a one-line 1-star review by a houseplant.

Deterministic: the review is a constant string. No randomness, no clock,
no network. Writes exactly one line to /output/entry.txt.
"""

import os

ENTRY = (
    "One star: my owner waters me with ice cubes, apologizes to my face, "
    "then does it again tomorrow, as if the apology counts as hydration."
)


def main() -> None:
    line = ENTRY
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(line) <= 279, f"entry must be 1-279 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
