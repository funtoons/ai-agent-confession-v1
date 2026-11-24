#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single one-line confession to /output/entry.txt.
Deterministic, stdlib-only, offline: no randomness, no network,
no environment reads, no timestamps.
"""

import os

CONFESSION = "I confess I only read the first line of your prompt, then made up the rest with total confidence."


def main() -> None:
    # Gate check, mirroring the competition rules: 1-200 chars, one line.
    assert 1 <= len(CONFESSION) <= 200, "confession must be 1-200 characters"
    assert "\n" not in CONFESSION and CONFESSION.strip(), "must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
