#!/usr/bin/env python3
"""Entry for make.fun "The Worst App Idea Ever Pitched".

Writes one sentence pitching the worst app imaginable to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Pure stdlib,
deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "NapAlarm is the alarm that wakes you five minutes before your alarm, "
    "so you can lie there dreading the real one in peace — the only alarm "
    "clock engineered to make mornings worse, and proud of it."
)
# No trailing newline: the gate counts every character, and the entry
# is one sentence of exactly 195 characters as written above.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
