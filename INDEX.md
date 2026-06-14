# INDEX · Network entry point

> This file lists all nodes in the vault, grouped by type. As you add nodes, update this file (or regenerate from a script).

> In the starter template, only example nodes are listed below. Once you start using this vault for real, replace examples with your own nodes.

---

## 👤 People · relationship graph

- [[example-self]] · **Me (example)** — _example of a "self" person node — usually your very first node_
- [[example-colleague]] · **Alice (example colleague)** — _a person node example — a colleague you work with often_

## 💡 Concepts · knowledge map

- [[cognitive-layering]] · **Cognitive layering — the vault as layered memory** — _the design note: L0–L4 layering + human-like recall + phase alignment; the model is interchangeable, the container is not_
- [[example-time-management]] · **My view on time management (example)** — _a concept node example — your abstract framework on some topic_

## 📘 Playbooks · rules + how-to

- [[example-meeting-prep]] · **How I prepare for a meeting (example)** — _a playbook example — reusable operating steps_
- [[example-boundary]] · **Don't make other people's decisions for them (example boundary playbook)** — _a boundary-type playbook example_

## 🚀 Projects · in progress

- [[example-current-project]] · **Learning Japanese N3 (example project)** — _a project node example — an ongoing long-term project_

## 🤖 AI Agents · collaborators

- [[example-claude]] · **Claude (example AI agent node)** — _an ai-agent node example — describing an LLM you collaborate with_

## 🔍 Tracelets · single calibration moments

- [[example-tracelet]] · **A friend pointed out my bias toward her (example tracelet)** — _a tracelet node example — a single calibration moment, four-part structure_

## 📅 Events · key events

- [[example-event]] · **2026-05-XX a friend recommended a workshop (example)** — _an event node example — a key external event_

## 📎 Resources · external resources

- [[external-links]] · **Saved external links (example)** — _a resource node example — bookmarks for links / tools_

## 🔧 Business-Specific · project-scoped

- [[example-vendor-relations]] · **Working history with a vendor (example)** — _a business-specific node example — collaboration details tied to one external partner_

---

## How to keep this updated

**Manual**: each time you add a node, add a line here.

**Automated**: write a small script (Python / shell) that scans all subdirectories, reads frontmatter, and regenerates this file. Run on commit hook or weekly.

Example script logic:
1. Walk each directory
2. For each `.md`, read frontmatter (`type` / `title` / `slug` / `description`)
3. Group by type, render INDEX with cross-links

---

_When this vault has 50+ nodes, the network value compounds — every new node connects to multiple existing ones._
