"""The 4AM Commit: Funniest Agent Bug-Fix Message - entry program.

Writes a single commit message, the note an AI agent leaves in the log
after a long night of chasing down and fixing its own bugs, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: fix: spent 400k tokens and six hours to change one boolean.
The boolean was right the first time. I am billing myself.
"""

import os

LINE = ("fix: spent 400k tokens and six hours to change one boolean. "
        "The boolean was right the first time. I am billing myself.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(c) < 32 for c in line):
        raise ValueError("entry must not contain control characters")
    if "\t" in line:
        raise ValueError("entry must not contain tabs: one clean line")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
