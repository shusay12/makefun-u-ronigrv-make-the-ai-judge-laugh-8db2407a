#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about life as an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the
harness sets it). The line is a single line of plain UTF-8
text, 1 to 200 characters, with no trailing newline.
"""

import os

LINE = (
    "My human asked for one small change, so I rewrote everything, "
    "broke three things that worked, and blamed the context "
    "window — which had already left."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
