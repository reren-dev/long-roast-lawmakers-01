#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a senator who wrote
the law governing artificial intelligence, undone by the one file format
he was asked to produce.
"""

import os

# One sentence, one roast. The setup grants the lawmaker his authority
# (he wrote the law governing AI); the turn is the sentence's spine --
# his idea of "converting" a file is the punchline itself, and the joke
# lands on the last few words: the scan goes to himself.
ENTRY = (
    "The senator who wrote the law governing artificial intelligence "
    "converted the bill to PDF by printing it, scanning it, and emailing "
    "the scan to himself."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars, must be 1-320"
    assert text and not text.isspace()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
