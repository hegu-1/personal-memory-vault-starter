# scripts/

Small, dependency-free helper scripts for maintaining the vault.

## `build-index.py`

Regenerates `INDEX.md` from the frontmatter of every node.

```bash
python scripts/build-index.py          # rewrite INDEX.md
python scripts/build-index.py --check   # exit 1 if INDEX.md is stale (use in CI / pre-commit)
```

It walks each node directory, reads the `type` / `slug` / `title` / `description` from each node's frontmatter, groups by type, and rewrites `INDEX.md`. Run it after adding, renaming, or deleting nodes — or wire `--check` into a git pre-commit hook so the index never drifts.

Requires only Python 3.8+ (standard library, no `pip install`).
