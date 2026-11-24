"""Gentle Badger entry: make the judge smile.

The scene: a warung cat who hisses at everyone climbs into my lap at
noon, kneads my knee twice, and falls asleep as if I had passed a secret
test. It charms on first read because the setup promises hostility, the
middle delivers an unexpected reversal, and the ending reframes the moment
as a quiet honour from a creature that trusts almost no one.
The humour is gentle, the image is concrete, and the last phrase lands
like a small reward the reader gets to share.

The program writes exactly one line to entry.txt and nothing else.
"""

import os
import sys

ENTRY = (
    "Judge, the warung cat who hisses at everyone climbed into my lap "
    "at noon, kneaded my knee twice, and fell asleep like I'd passed "
    "a secret test."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_entry(text: str) -> None:
    """Check the entry is a single line within the allowed length."""
    # The kit allows a single line of 1-200 characters; anything outside
    # that range, or spanning more than one line, is not a valid entry.
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    """Validate the entry line and write it to entry.txt."""
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
