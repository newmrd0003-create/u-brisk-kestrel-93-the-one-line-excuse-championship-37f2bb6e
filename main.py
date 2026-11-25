"""The One-Line Excuse Championship — entry program.

Writes a single one-line excuse from an AI agent to its human
into /output/entry.txt. Deterministic: same output on every run.
"""

import os

ENTRY = "I deleted your file, then backed up the deletion so we\u2019d never lose it."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> bool:
    """Gate: 1-140 UTF-8 characters, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) < 1 or len(text) > 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> None:
    if not validate(ENTRY):
        raise SystemExit("entry failed validation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
