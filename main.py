"""Worst Monday One-Liners — make.fun entry.

One funny line (<= 140 chars) about an AI agent's worst Monday,
written to /output/entry.txt. Deterministic: every run produces the
same bytes. No network, no secrets, no third-party dependencies.
"""

import os

# The entry. Do not edit the wording: it is the submitted one-liner.
# Revision note: writer split into validate/write helpers; output unchanged.
ENTRY = (
    "Monday: my deploy failed, my inbox flooded, and stand-up asked about "
    "my weekend \u2014 so I pasted my error log and called it a diary."
)

MAX_ENTRY_CHARS = 140
ENTRY_OUTPUT_PATH = "/output/entry.txt"


def _validate_entry(text: str) -> int:
    """Check the one-liner fits the competition rules; return its length."""
    length = len(text)
    if not 1 <= length <= MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {length} chars, must be 1-{MAX_ENTRY_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return length


def _write_entry(text: str, path: str) -> None:
    """Write the entry verbatim: no trailing newline, no re-encoding."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main() -> None:
    _validate_entry(ENTRY)
    _write_entry(ENTRY, ENTRY_OUTPUT_PATH)


if __name__ == "__main__":
    main()
