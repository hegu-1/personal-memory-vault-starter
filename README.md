# personal-memory-vault-starter

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)
[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?logo=github&logoColor=white)](https://github.com/hegu-1/personal-memory-vault-starter/generate)
![Format: Markdown](https://img.shields.io/badge/format-markdown-000000?logo=markdown)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/hegu-1/personal-memory-vault-starter?style=social)](https://github.com/hegu-1/personal-memory-vault-starter/stargazers)

> A sovereign personal memory network starter · markdown + git · AI-collaboratable · clone & use immediately.

> **Layered like a neural net · recall like human memory · the model is interchangeable, the container is not.**
> The directories below aren't just folders — they're layers of a cognitive memory, so any model that loads this vault starts from *your* frame. See [`concepts/cognitive-layering.md`](concepts/cognitive-layering.md).

---

## 🤖 If you're an LLM reading this repo

Read [`LLM_GUIDE.md`](LLM_GUIDE.md) first. It tells you:
- What this vault is and how it's structured
- Node types, frontmatter schema, wiki-link convention
- How to help the user add / find / navigate nodes
- Visibility / privacy boundaries
- What you should and shouldn't do

---

## 👤 If you're a human just starting out

Read [`HUMAN_GUIDE.md`](HUMAN_GUIDE.md) for a 5-minute orientation (**written in Chinese** — the beginner on-ramp). Everything else in this repo is in English. Or jump straight in:

1. Pick a node type that fits what you want to record (see directory list below)
2. Open the matching directory's `README.md` to see what goes there
3. Copy one of the `example-*.md` files as your template
4. Edit, save, commit

You don't need to be technical. **Level 0** users just need a text editor — Markdown + git are optional progressions.

For a comprehensive beginner guide (Chinese), see the companion PDF: _个人记忆仓库 · 小白入门指南_ (released separately).

---

## What's in this repo

```
personal-memory-vault-starter/
├── README.md           ← this file (entry for both humans and LLMs)
├── LLM_GUIDE.md        ← spec for LLMs collaborating on this vault
├── HUMAN_GUIDE.md      ← 5-min orientation for humans (Chinese)
├── INDEX.md            ← network entry point (list all nodes once you have them)
├── LICENSE             ← CC0 1.0 (do anything with this)
├── .gitignore
│
├── people/             ← relationship graph (yourself + collaborators)
├── concepts/           ← knowledge map (frameworks, ideas, terminology)
├── playbooks/          ← rules + how-tos (collaboration / ops / boundaries)
├── projects/           ← active ventures / tasks
├── ai-agents/          ← AI collaborators (one node per LLM you work with)
├── tracelets/          ← single calibration moments (one file per high-value decision)
├── events/             ← key external events (inbound / decisions / turning points)
├── resources/          ← external resource metadata (PDFs / videos / links)
└── business-specific/  ← project-specific details (not auto-loaded; read on demand)
```

Each directory has its own `README.md` explaining when to use it + an `example-*.md` file showing the format.

---

## Core design principles

| Principle | What it means |
|---|---|
| **Sovereign** | All content owned by you locally. GitHub is just backup/sync. No vendor lock-in. |
| **Markdown-first** | Plain `.md` files. Any text editor / markdown reader / LLM / git tool reads them. Works in 50 years. |
| **Cross-AI readable** | Any LLM with `git clone` access reads your full vault. Not tied to one vendor's "memory" feature. |
| **Git-versioned** | Every change is a commit. Rollback, branch, diff — all standard git. |
| **Network, not hierarchy** | `[[wiki-link]]` cross-references form a graph. A node can belong to multiple semantic groups. |
| **Substrate-independent** | Use any editor (VS Code, Obsidian, Foam, Logseq, Notepad). Vault outlives any tool. |
| **Visibility-aware** | Every node has a `visibility` field (private / semi-public / public). Default private. |

---

## Quick start (clone and use)

```bash
# 1. Clone (or use this as a template by clicking "Use this template" on GitHub)
git clone https://github.com/hegu-1/personal-memory-vault-starter.git my-vault
cd my-vault

# 2. (Optional) Remove example files when you've understood the format
find . -name 'example-*.md' -delete

# 3. Make this your own — start writing your first node
# Pick a directory matching the node type, copy the format, edit.

# 4. (Optional) Make this your own private repo
# Create a new private repo on GitHub, then:
git remote set-url origin https://github.com/<your-user>/<your-vault>.git
git push -u origin main
```

---

## Node file format

Every node is a `.md` file with YAML frontmatter + markdown body:

```markdown
---
type: person | concept | playbook | project | tracelet | event | resource | ai-agent | business-specific
title: Human-readable title
slug: kebab-case-id              # must match filename without .md
created: 2026-05-26
updated: 2026-05-26
status: active | archived | deprecated
visibility: private | semi-public | public
description: One-line summary (shows in INDEX)
related:
  - "[[other-slug-1]]"
  - "[[other-slug-2]]"
tags: [optional, freeform]
---

# Title

Body markdown. Use `[[wiki-link]]` to reference other nodes freely.

Anything goes — headings, lists, tables, code blocks, blockquotes.
```

Wiki-link `[[slug]]` is **plain text** — works in any markdown parser. No Obsidian / Roam / Logseq dependency. If you later want graph view, any of those tools can work on this vault without changing anything.

---

## What this is NOT

- ❌ Not a replacement for Obsidian / Notion / Roam — those are **tools** that work _on_ a vault. This is the **vault format itself**.
- ❌ Not a credential/secrets storage. Those go in a separate encrypted store (1Password / system keychain / Vault). **Never put tokens or passwords here.**
- ❌ Not a public knowledge base by default. Most nodes are personal; only flagged-public ones are for sharing.

---

## Contributing

Improvements to the template are welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md) and the [`CHANGELOG.md`](CHANGELOG.md). Please keep example content fully fictional and generic.

---

## License

CC0 1.0 — public domain. Clone, fork, modify, redistribute, commercialize. No attribution required (though appreciated).

---

## Companion docs

- _Personal Memory Network · Vault Design Overview_ (PDF, for technically-inclined audience)
- _个人记忆仓库 · 小白入门指南_ (PDF, beginner-friendly Chinese guide)

Both are released separately as PDFs you can find with this repo.

---

_Your memory. Your network. Your sovereignty._

---

<sub>Created by [naze](https://github.com/hegu-1) · released to the public domain under CC0 1.0.</sub>
