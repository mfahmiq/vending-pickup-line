"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry
before writing: UTF-8 text, 1-200 characters, a single line, and not
whitespace-only. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "Hey, you've walked past me 47 times and my coils never tangled "
    "like this \u2014 drop in a coin and I'll jam on purpose just to "
    "keep you here."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    text = ENTRY

    # Gate checks, mirroring the competition's sealed scorer.
    if not text or not text.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(
            "error: entry is %d characters, over the 200 limit" % len(text),
            file=sys.stderr,
        )
        return 1
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "wb") as handle:
        handle.write(encoded)

    print("wrote %s (%d chars, %d bytes)" % (output_path, len(text), len(encoded)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
