#!/usr/bin/env python3
"""Update YAML front matter `date` and `updated` fields for MkDocs notes.

Behavior
- If front matter has `date:` missing/empty, set it to today's date (YYYY-MM-DD).
- Always set `updated:` to today's date (YYYY-MM-DD) when the file is modified.
- Only operates on files that already have a YAML front matter block starting at the top of the file.

Notes
- Designed to run via pre-commit (on staged files).
- Keeps changes minimal and preserves the rest of the file.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path


FRONT_MATTER_RE = re.compile(r"\A---\n(?P<yaml>.*?)(?:\n---\n)", re.DOTALL)


def _today() -> str:
    return _dt.date.today().isoformat()


def _has_key(yaml_text: str, key: str) -> bool:
    return re.search(rf"(?m)^(?P<indent>\s*){re.escape(key)}\s*:.*$", yaml_text) is not None


def _set_or_insert_scalar(yaml_text: str, key: str, value: str, *, only_if_missing: bool) -> str:
    pattern = re.compile(rf"(?m)^(?P<indent>\s*){re.escape(key)}\s*:(?P<rest>.*)$")
    m = pattern.search(yaml_text)
    if m:
        if only_if_missing:
            rest = (m.group("rest") or "").strip()
            if rest not in ("", "null", "~"):
                return yaml_text
        indent = m.group("indent") or ""
        # replace the whole line
        return pattern.sub(lambda mm: f"{indent}{key}: {value}", yaml_text, count=1)

    if only_if_missing and _has_key(yaml_text, key):
        return yaml_text

    # Insert near the top. Prefer after `date:` if inserting `updated:`.
    lines = yaml_text.splitlines(True)  # keepends

    insert_at = 0
    if key == "updated":
        for i, line in enumerate(lines):
            if re.match(r"(?m)^\s*date\s*:\s*.*$", line):
                insert_at = i + 1
                break

    lines.insert(insert_at, f"{key}: {value}\n")
    return "".join(lines)


def update_file(path: Path, today: str) -> bool:
    raw = path.read_text(encoding="utf-8")
    m = FRONT_MATTER_RE.search(raw)
    if not m:
        return False

    yaml_text = m.group("yaml")

    new_yaml = yaml_text
    new_yaml = _set_or_insert_scalar(new_yaml, "date", today, only_if_missing=True)
    new_yaml = _set_or_insert_scalar(new_yaml, "updated", today, only_if_missing=False)

    if new_yaml == yaml_text:
        return False

    new_raw = raw[: m.start("yaml")] + new_yaml + raw[m.end("yaml") :]
    path.write_text(new_raw, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="*", help="Files to update (pre-commit passes staged files)")
    args = p.parse_args(argv)

    today = _today()
    changed_any = False

    for f in args.files:
        path = Path(f)
        if not path.exists() or path.is_dir():
            continue
        if path.suffix.lower() != ".md":
            continue

        try:
            changed = update_file(path, today)
            changed_any = changed_any or changed
        except UnicodeDecodeError:
            # skip non-utf8
            continue

    return 1 if changed_any else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
