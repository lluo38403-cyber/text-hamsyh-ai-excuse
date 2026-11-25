"""The One-Line AI Excuse for Breaking Production — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives
its human right after breaking production, in the machine's own
voice. The joke lands on the twist — the bug it found is itself —
and on the Friday deploy, the oldest sin in the book.
"""

import os

ENTRY = (
    "Good news, I found the bug. Bad news, the bug is me, and "
    "production is down because I shipped it on a Friday afternoon."
)

MAX_CHARS = 180


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
