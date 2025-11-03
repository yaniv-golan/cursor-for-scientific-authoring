#!/usr/bin/env python3
"""
Fail if any published page prints a bare Jekyll link tag path.

Rule: Any line that contains "{{ site.baseurl }}{% link ... %}" must also
contain a closing ")" later on the same line (i.e., be wrapped inside
Markdown link syntax like: [Label]({{ site.baseurl }}{% link ... %})).

Scope: Scan Markdown files under docs/ only.
"""
from __future__ import annotations
import sys
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

pattern = re.compile(r"\{\{\s*site\.baseurl\s*\}\}.*?\{%\s*link\s+[^%]+%\}")
content_md_pattern = re.compile(r"content/[^)\s`]+\.md")

def find_offenses() -> list[tuple[Path, int, str]]:
    offenses = []
    allow_content_md = {
        Path("docs/resources/about.md"),
        Path("docs/guide/index.md"),
        Path("docs/guide/core/project-rules.md"),
    }
    for path in DOCS.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for m in pattern.finditer(line):
                # Ensure there's a ')' after the end of the match on the same line
                remainder = line[m.end():]
                if ")" not in remainder:
                    offenses.append((path.relative_to(ROOT), i, line.rstrip()))
            # Flag repo-path references to content/*.md on published pages
            if path not in allow_content_md and content_md_pattern.search(line):
                offenses.append((path.relative_to(ROOT), i, line.rstrip()))
    return offenses

def main() -> int:
    offenses = find_offenses()
    if not offenses:
        print("check_internal_links: OK")
        return 0
    print("check_internal_links: found bare internal link tag occurrences:")
    for path, line_no, line in offenses:
        print(f" - {path}:{line_no}: {line}")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
