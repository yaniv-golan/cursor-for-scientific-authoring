#!/usr/bin/env python3
"""
Promote completed drafts from content/ → docs/ with Jekyll front matter.

Rules
- Only promote Markdown files under content/** whose front matter has status: complete.
- Destination path mirrors content/ but with these mappings:
    content/guide/**            → docs/guide/**
    content/exercises/**        → docs/getting-started/**
    content/policies/**         → docs/resources/**
    (any other paths)           → docs/<same-subpath>
- Front matter adjustments:
    - Remove `status`.
    - Ensure `layout: default`.
    - Add parent hierarchy by section:
        docs/guide/core/*  → grand_parent: Guide, parent: Core
        docs/guide/plus/*  → grand_parent: Guide, parent: Plus
        docs/guide/pro/*   → grand_parent: Guide, parent: Pro
        docs/getting-started/* → parent: Getting Started
        docs/resources/*   → parent: Resources
    - Set `nav_order` for known Core pages using a filename → order map.

Usage
    Dry run:   python3 ops/promote.py --dry-run   # prints DRY RUN header; writes nothing
    Apply:     python3 ops/promote.py
    Only some: python3 ops/promote.py --only content/guide/core/quick-start.md [...]
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
from typing import Dict, List, Tuple
import textwrap

RE_FM = re.compile(r"^---\s*$")


CORE_ORDER = {
    "quick-start.md": 10,
    "writing-markdown.md": 20,
    "accuracy.md": 30,
    "managing-sources.md": 40,
    "analysis.md": 50,
    "checklists.md": 60,
    "project-rules.md": 70,
    "endgame.md": 80,
}


def read_front_matter(text: str) -> Tuple[Dict[str, str], str]:
    """Return (front_matter_dict, body). Minimal YAML parser for simple key: value lines."""
    lines = text.splitlines()
    if not lines or not RE_FM.match(lines[0]):
        return {}, text
    # find closing ---
    try:
        end = next(i for i in range(1, len(lines)) if RE_FM.match(lines[i]))
    except StopIteration:
        return {}, text
    raw = lines[1:end]
    body = "\n".join(lines[end + 1 :])
    fm: Dict[str, str] = {}
    for ln in raw:
        if not ln.strip() or ln.strip().startswith("#"):
            continue
        if ":" in ln:
            k, v = ln.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def write_front_matter(fm: Dict[str, str], body: str) -> str:
    out = ["---"]
    for k, v in fm.items():
        out.append(f"{k}: {v}")
    out.append("---")
    out.append("")
    if body and not body.startswith("\n"):
        out.append(body)
    else:
        out.append(body)
    return "\n".join(out).rstrip() + "\n"


def map_destination(src: pathlib.Path) -> pathlib.Path:
    rel = src.relative_to("content")
    parts = list(rel.parts)
    if not parts:
        raise ValueError("unexpected path")
    if parts[0] == "guide":
        dest = pathlib.Path("docs") / rel
    elif parts[0] == "exercises":
        dest = pathlib.Path("docs") / "getting-started" / pathlib.Path(*parts[1:])
    elif parts[0] == "policies":
        dest = pathlib.Path("docs") / "resources" / pathlib.Path(*parts[1:])
    else:
        dest = pathlib.Path("docs") / rel
    return dest


def augment_fm_for_destination(fm: Dict[str, str], dest: pathlib.Path) -> Dict[str, str]:
    fm = dict(fm)  # copy
    fm.pop("status", None)
    fm.setdefault("layout", "default")

    dest_str = dest.as_posix()
    if "/guide/core/" in dest_str:
        fm.setdefault("grand_parent", "Guide")
        fm.setdefault("parent", "Core")
        order = CORE_ORDER.get(dest.name)
        if order is not None:
            fm.setdefault("nav_order", str(order))
    elif "/guide/plus/" in dest_str:
        fm.setdefault("grand_parent", "Guide")
        fm.setdefault("parent", "Plus")
    elif "/guide/pro/" in dest_str:
        fm.setdefault("grand_parent", "Guide")
        fm.setdefault("parent", "Pro")
    elif "/getting-started/" in dest_str:
        fm.setdefault("parent", "Getting Started")
    elif "/resources/" in dest_str:
        fm.setdefault("parent", "Resources")
    return fm


def discover_sources(only: List[str] | None) -> List[pathlib.Path]:
    if only:
        return [pathlib.Path(p).resolve() for p in only]
    return sorted(pathlib.Path("content").rglob("*.md"))


def load_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def save_text(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Promote completed content pages into docs/")
    ap.add_argument("--dry-run", action="store_true", help="Show actions without writing files")
    ap.add_argument("--only", nargs="*", help="Promote only specific content file paths")
    args = ap.parse_args()

    promoted: List[Tuple[pathlib.Path, pathlib.Path]] = []
    skipped: List[Tuple[pathlib.Path, str]] = []
    warnings: List[str] = []

    for src in discover_sources(args.only):
        if "templates/" in src.as_posix() or "raw/" in src.as_posix():
            continue
        text = load_text(src)
        fm, body = read_front_matter(text)
        status = (fm.get("status") or "").strip().lower()
        if status != "complete":
            skipped.append((src, f"status={status or 'missing'}"))
            continue
        dest = map_destination(src.relative_to(pathlib.Path.cwd())) if src.is_absolute() else map_destination(src)
        out_fm = augment_fm_for_destination(fm, dest)
        out_text = write_front_matter(out_fm, body)

        # Pre-publish checks: warn if landing pages omit `site.baseurl` in links
        try:
            dest_rel = dest.as_posix()
        except Exception:
            dest_rel = str(dest)
        if dest.name == "index.md":
            # 1) `{% link ... %}` without preceding `{{ site.baseurl }}`
            if re.search(r"\]\(\s*(?!\{\{\s*site\.baseurl\s*\}\}\s*\{\%\s*link)\{\%\s*link", out_text):
                warnings.append(
                    "WARN "
                    + dest_rel
                    + ": use `{{ site.baseurl }}{% link ... %}` for internal links on landing pages"
                )
            # 2) Absolute root URLs like `](/guide/...)`
            if re.search(r"\]\(/", out_text):
                warnings.append(
                    "WARN " + dest_rel + ": root-relative links detected; prefix with `{{ site.baseurl }}`"
                )
            # 3) `relative_url` filter
            if "relative_url" in out_text:
                warnings.append(
                    "WARN "
                    + dest_rel
                    + ": `relative_url` found; prefer `{{ site.baseurl }}{% link ... %}`"
                )
        promoted.append((src, dest))
        if not args.dry_run:
            save_text(dest, out_text)

    # Report
    if args.dry_run:
        print("DRY RUN — no files were written. This is a preview.")
    print("Promote summary:")
    for src, dest in promoted:
        if args.dry_run:
            print(f" ~ {src} → {dest}")
        else:
            print(f" + {src} → {dest}")
    for src, reason in skipped:
        print(f" - {src} (skipped: {reason})")
    if not promoted and not skipped:
        print("(no matching files)")
    if warnings:
        print("\nPre-publish warnings:")
        for w in warnings:
            print(" ! ", w)
    print(
        f"Totals: {len(promoted)} promote, {len(skipped)} skipped"
        + (" (dry run)" if args.dry_run else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
