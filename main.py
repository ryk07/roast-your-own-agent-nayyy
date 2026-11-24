#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one short, original roast line to /output/entry.txt.
Standard library only, deterministic, no network, no working-directory
assumptions: the text lives in this file and the output path is absolute.
"""
import os

TEXT = (
    # One line, 137 chars: the "verification" ritual that verifies
    # nothing, the hallucinated quote, payoff in the last clause.
    "My agent spent eleven tool calls 'verifying' a file it never opened, "
    "then quoted it anyway — line 42, from a file that has never existed."
)


def main() -> None:
    # Gate: the sealed scorer needs 1-200 chars of non-whitespace UTF-8.
    if not 1 <= len(TEXT) <= 200:
        raise SystemExit(f"entry is {len(TEXT)} chars, must be 1-200")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
