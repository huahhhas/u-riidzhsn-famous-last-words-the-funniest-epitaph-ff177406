#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one original one-line tombstone epitaph (<= 150 chars)
to $OUTPUT_DIR/entry.txt (default /output).
Pure stdlib, deterministic: the same line every run.
"""

import os

# Famous last words, carved in stone: the man who would not
# give up the last word even to death itself.
EPITAPH = "Here lies a man who died mid-sentence, just to have the last word."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EPITAPH.strip()
    assert 1 <= len(text) <= 150, f"epitaph length {len(text)} out of gate"
    assert "\n" not in text, "epitaph must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
