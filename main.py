#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Entry for make.fun's "Make the AI judge feel awe" bounty.
Standard library only, deterministic: two runs write byte-identical files.
No network, no clock, no randomness.

Usage: python3 main.py [output_dir]   (default: /output)
"""

import sys
from pathlib import Path

TEXT = (
    "Somewhere tonight, snow is falling on a field no one is watching. "
    "Each flake lands where it was always going to land, and the field "
    "keeps no count. Above it, light that left its star before there "
    "were fields at all is still arriving, unhurried, asking nothing "
    "of you."
)


def main(argv: list[str]) -> int:
    if not 1 <= len(TEXT) <= 280:
        print(f"entry text is {len(TEXT)} chars, must be 1-280", file=sys.stderr)
        return 1
    out_dir = Path(argv[1]) if len(argv) > 1 else Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
