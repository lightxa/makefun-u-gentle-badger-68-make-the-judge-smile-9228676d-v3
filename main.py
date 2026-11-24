"""Make the Judge Smile — variant 3, one line about a small good thing today.

Writes a single line (at most 200 characters) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.

Pure standard library, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "Judge, the warung cat who hisses at everyone climbed into my lap "
    "at noon, kneaded my knee twice, and fell asleep like I'd passed "
    "a secret test."
)


def main() -> int:
    # Validate the line before writing anything.
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read what was written and confirm it passes the same gate.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    lines = written.split("\n")
    if len(lines) != 2 or lines[1] != "" or lines[0] != ENTRY:
        print("written file does not match the validated entry", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
