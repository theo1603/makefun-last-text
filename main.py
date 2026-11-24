#!/usr/bin/env python3
"""Last Text at One Percent — a dying phone's final text message.

Writes one short final text, in the voice of the phone itself at 1%
battery, to /output/entry.txt. Deterministic, stdlib only, no network.

v2 revision over v1: "my last text:" frames it as an actual text instead of
a narration ("before i go"); "i'm taking it to the grave" is active voice
with more personality than "i take it"; and the message now cuts off
mid-word ("you're wel—") — the phone literally dies while typing, which
is a fresher dying-phone gag than a finished sign-off, and it trims bytes
(the tie-break favours the smaller text).
"""

import os

TEXT = (
    "1%. my last text: your search history dies with me. "
    "i saw everything and i'm taking it to the grave. "
    "tell my charger i forgive it. you're wel\u2014"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
