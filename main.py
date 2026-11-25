"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt: "Unsubscribe".

Why this word: it treats the ex like a mailing list you finally
cancelled. The joke lands at a glance — no insult, no caption needed —
and anyone who has ever muted, blocked, or walked away from an ex
recognises the feeling instantly. One word, spelled correctly, no
punctuation tricks, 11 characters, well inside the 111-character cap.

Deterministic: no input, no network, no randomness. Every run writes
the same bytes.
"""

import os

WORD = "Unsubscribe"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the file holds the word and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    # Self-check against the bounty gate before exiting: exactly one
    # word, 1-111 characters, not only whitespace.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert 1 <= len(written) <= 111, "entry outside 1-111 character gate"
    assert written.strip() == written and len(written.split()) == 1, (
        "entry must be exactly one word"
    )


if __name__ == "__main__":
    main()
