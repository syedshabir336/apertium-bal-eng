#!/usr/bin/env python3
"""Validate the staging TSV for Suleimani Balochi -> English lexical data.

This checks data hygiene, not linguistic correctness. A native-speaker review
and a traceable source are still required for every production entry.
"""
from __future__ import annotations

import csv
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / "data" / "bal-eng-lexicon.tsv"
FIELDS = (
    "bal_lemma", "bal_pos", "eng_lemma", "sense",
    "dialect", "source", "reviewer", "status",
)
ALLOWED_STATUS = {"draft", "reviewed"}


def is_latin_orthography(value: str) -> bool:
    """Allow Latin letters, combining marks, digits, spaces and punctuation."""
    for char in value:
        category = unicodedata.category(char)
        if category.startswith("L") and "LATIN" not in unicodedata.name(char, ""):
            return False
        if category.startswith("M") and not unicodedata.name(char, "").startswith(
            ("COMBINING", "LATIN")
        ):
            return False
    return True


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if tuple(reader.fieldnames or ()) != FIELDS:
            return [
                "header must be exactly: " + "\t".join(FIELDS)
            ]

        for line, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue
            for field in FIELDS:
                value = (row.get(field) or "").strip()
                if not value:
                    errors.append(f"line {line}: {field} is required")
            lemma = (row.get("bal_lemma") or "").strip()
            if lemma:
                if unicodedata.normalize("NFC", lemma) != lemma:
                    errors.append(f"line {line}: bal_lemma is not Unicode NFC")
                if not is_latin_orthography(lemma):
                    errors.append(
                        f"line {line}: bal_lemma contains non-Latin letters; "
                        "canonical entries must use Latin/Roman script"
                    )
            status = (row.get("status") or "").strip()
            if status and status not in ALLOWED_STATUS:
                errors.append(
                    f"line {line}: status must be one of "
                    + ", ".join(sorted(ALLOWED_STATUS))
                )
    return errors


def main() -> int:
    path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_FILE
    try:
        errors = validate(path)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {path} passed lexical-data hygiene checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
