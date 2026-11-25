"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings (max 200 characters) to
<output_dir>/entry.txt, where <output_dir> is MAKEFUN_OUTPUT_DIR
or /output. No network, no external files, deterministic output.
"""

import os

JOKE = (
    "My alarm clock quit this Monday - tired of being the villain. "
    "Now my coffee wakes me up, and it screams louder than the alarm ever did."
)

MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("entry text is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the entry,
    # byte-identical, with no trailing newline or stray whitespace.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    if "\n" in written or written != written.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")


if __name__ == "__main__":
    main()
