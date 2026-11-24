"""Time Machine Warning Label — round 1 entry.

Writes the keeper line to /output/entry.txt and asserts the gate
(UTF-8, 1-120 characters) immediately after writing.
Pure stdlib only.
"""

import os

ENTRY = "WARNING: Your past self is armed and considers you a burglar."
OUT = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(data)
    # Verify the gate immediately after writing (shared scratch).
    with open(OUT, "rb") as f:
        raw = f.read()
    assert raw == data, "entry.txt changed between write and verify"
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 120, f"char count {len(text)} outside 1-120"
    assert text.strip(), "entry is only whitespace"
    assert not text.endswith("\n"), "entry must not end with a newline"
    # Keeper (build note): the last word, "burglar", reframes the whole
    # setup — the traveller is the intruder in their own past.
    print(f"entry: {text!r}")
    print(f"wrote {len(raw)} bytes / {len(text)} chars to {OUT}")


if __name__ == "__main__":
    main()
