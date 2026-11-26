"""Entry for make.fun's "The Self-Checkout Is Judging You" bounty.

Writes a single line to /output/entry.txt: a smug remark from a
judgmental self-checkout machine to a shopper, in the machine's own voice.
"""

import os

ENTRY = (
    "Twelve yogurts, zero spoons, one frozen meal for one. I've scanned "
    "your life choices \u2014 that'll be $14.73, and no, I won't pretend "
    "this is a balanced diet."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing space"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-char entry to {path}")


if __name__ == "__main__":
    main()
