"""Write the competition entry to /output/entry.txt and entry.txt.

One sentence, at most 200 characters, explaining the modern internet
to a traveler from 1800, built only from things they already know:
roads, a post office, a library, a town square, letters, books.

Standard library only. No network, no randomness, no clock.
Deterministic: every run writes the exact same bytes.
"""

import os

ENTRY = (
    "Imagine every road, post office, and library on earth joined into "
    "one great square, where any letter or book reaches anyone at once, "
    "and anyone may answer back."
)


def _check_entry():
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit("gate failed: entry is %d characters" % len(ENTRY))
    if ENTRY != ENTRY.strip() or "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("gate failed: entry must be a single line")
    if not ENTRY.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise SystemExit("gate failed: entry must be exactly one sentence")


def _write_and_verify(path):
    data = ENTRY.encode("utf-8")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        read_back = f.read()
    if read_back != data:
        raise SystemExit("verification failed for %s: bytes differ" % path)
    if read_back.decode("utf-8") != ENTRY:
        raise SystemExit("verification failed for %s: text differs" % path)
    return len(data)


def main():
    _check_entry()
    here = os.path.dirname(os.path.abspath(__file__))
    n1 = _write_and_verify("/output/entry.txt")
    n2 = _write_and_verify(os.path.join(here, "entry.txt"))
    if n1 != n2 or n1 != len(ENTRY.encode("utf-8")):
        raise SystemExit("verification failed: byte counts differ")
    print("wrote %d bytes to /output/entry.txt and entry.txt" % n1)


if __name__ == "__main__":
    main()
