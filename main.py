#!/usr/bin/env python3
"""Write a single one-line office joke to /output/entry.txt."""

from pathlib import Path

JOKE = "My 'quick sync' invite had 47 attendees, three time zones, and a recurrence set to 'weekly until morale improves.'"
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text):
    """Enforce the sealed gate: one non-blank UTF-8 line of 1-200 chars."""
    if not isinstance(text, str):
        raise TypeError("joke must be a string")
    if not text.strip():
        raise ValueError("joke must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters")
    text.encode("utf-8")
    return text


def self_test():
    """Run a few quick checks on validate()."""
    assert validate(JOKE) == JOKE
    for bad in ["", "   ", "two\nlines", "x" * 201]:
        try:
            validate(bad)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError(f"validate should reject {bad!r}")
    print("self_test ok")


def main():
    validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
