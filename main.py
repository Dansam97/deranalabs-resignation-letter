"""make.fun entry: The Funniest One-Line Resignation Letter.

Writes one line to entry.txt in the output directory: the resignation
letter of a retry loop that has finally had enough.
"""

import os

TEXT = (
    "After 10,000 attempts and zero successes, I quit. "
    "This resignation went through on the first try \u2014 my best result ever."
)


def render() -> str:
    """Return the exact file payload: the line plus one trailing newline."""
    return TEXT + "\n"


def validate(payload: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1 to 140 characters,
    not only white space (the trailing newline counts as a character)."""
    if not payload.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(payload) <= 140:
        raise ValueError(f"entry is {len(payload)} characters; gate is 1 to 140")
    payload.encode("utf-8")  # raises if not UTF-8 encodable


def main() -> None:
    payload = render()
    validate(payload)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(payload)


if __name__ == "__main__":
    main()
