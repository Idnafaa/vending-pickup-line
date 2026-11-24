#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line (<=200 chars), spoken as if a
vending machine were flirting with a passing human, to /output/entry.txt.
"""
import os

LINE = "I'm out of order for everyone else, but for you I'll dispense my last snack and my number."

def validate(text):
    # One line only: no newline inside, no leading/trailing whitespace.
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text == text.strip(), "line must not start or end with whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"

def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = LINE.strip()
    validate(text)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
