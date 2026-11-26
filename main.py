#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun program/v1 entry.

An alien tourist's one-sentence review of planet Earth: one star for
the planet, five stars for the food. The program's only job is to place
that exact sentence, byte for byte, into the harness output directory.

The sentence itself is fixed review text. Nothing is computed, fetched,
or randomised here — the entry is deterministic by construction.
"""

import os
import sys

REVIEW = (
    "One star: your mie goreng stains my tentacles "
    "and your rain never stops, but one forkful and I "
    "understood why humans stay on this wet rock."
)


def output_path() -> str:
    """Resolve the entry file from the harness-provided output dir."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def check_sentence(text: str) -> None:
    """Guard the gate before writing: one line, 1-200 chars, no newline."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"review must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if text != text.strip():
        raise ValueError("review must not start or end with whitespace")


def main() -> int:
    check_sentence(REVIEW)
    target = output_path()
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
