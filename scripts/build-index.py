#!/usr/bin/env python3
"""Regenerate INDEX.md from the frontmatter of every node in the vault.

Usage:
    python scripts/build-index.py           # rewrite INDEX.md
    python scripts/build-index.py --check    # exit 1 if INDEX.md is stale (CI-friendly)

No third-party dependencies. Reads the simple YAML frontmatter block
(`type`, `slug`, `title`, `description`) at the top of each `.md` node.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# type -> (directory, section heading) in display order
SECTIONS = [
    ("person",            "people",            "👤 People · relationship graph"),
    ("concept",           "concepts",          "💡 Concepts · knowledge map"),
    ("playbook",          "playbooks",         "📘 Playbooks · rules + how-to"),
    ("project",           "projects",          "🚀 Projects · in progress"),
    ("ai-agent",          "ai-agents",         "🤖 AI Agents · collaborators"),
    ("tracelet",          "tracelets",         "🔍 Tracelets · single calibration moments"),
    ("event",             "events",            "📅 Events · key events"),
    ("resource",          "resources",         "📎 Resources · external resources"),
    ("business-specific", "business-specific", "🔧 Business-Specific · project-scoped"),
]

HEADER = """# INDEX · Network entry point

> This file lists every node in the vault, grouped by type. It is **generated** — run `python scripts/build-index.py` to refresh it after adding or renaming nodes.

> In the starter template only example nodes are listed below. Once you use this vault for real, your own nodes replace them automatically on the next regenerate.

---
"""

FOOTER = """---

_When this vault has 50+ nodes, the network value compounds — every new node connects to multiple existing ones._
"""


def parse_frontmatter(text: str) -> dict:
    """Parse the leading `--- ... ---` YAML block into a flat dict (top-level keys only)."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm: dict[str, str] = {}
    for line in text[3:end].splitlines():
        # skip blank lines and list items / nested lines (we only need scalar top-level keys)
        if not line or line[0] in " \t-":
            continue
        if ": " in line:
            key, _, val = line.partition(": ")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def collect(directory: str) -> list[dict]:
    d = ROOT / directory
    if not d.is_dir():
        return []
    nodes = []
    for path in sorted(d.glob("*.md")):
        if path.name == "README.md":
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("slug"):
            nodes.append(fm)
    return nodes


def render() -> str:
    parts = [HEADER]
    for type_name, directory, heading in SECTIONS:
        nodes = [n for n in collect(directory) if n.get("type") == type_name]
        if not nodes:
            continue
        parts.append(f"\n## {heading}\n\n")
        for n in nodes:
            line = f"- [[{n['slug']}]] · **{n.get('title', n['slug'])}**"
            desc = n.get("description")
            if desc:
                line += f" — _{desc}_"
            parts.append(line + "\n")
    parts.append("\n" + FOOTER)
    return "".join(parts).rstrip() + "\n"


def main() -> int:
    index_path = ROOT / "INDEX.md"
    new = render()
    if "--check" in sys.argv:
        current = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
        if current != new:
            print("INDEX.md is stale — run: python scripts/build-index.py", file=sys.stderr)
            return 1
        print("INDEX.md is up to date.")
        return 0
    index_path.write_text(new, encoding="utf-8")
    print(f"Wrote {index_path.relative_to(ROOT)} ({len(new.splitlines())} lines).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
