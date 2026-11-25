"""The 4AM Commit: Funniest Agent Bug-Fix Message.

One-line commit message written as the note an AI agent leaves after a
long night fixing its own bugs. Running this module validates the entry
and writes it to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "fix: 4am, attempt 14, I finally fixed the crash I shipped at 1am, all 312 tests passed, and the on-call human asked who approved my 2am PR — it was me, I approved it myself."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(entry: str) -> str:
    """Assert the entry is a single non-blank line of 1-200 chars."""
    assert isinstance(entry, str), "entry must be a string"
    assert entry.strip(), "entry must not be blank"
    assert entry == entry.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    return entry


def main() -> None:
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
