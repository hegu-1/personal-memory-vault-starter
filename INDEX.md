# INDEX · Network entry point

> This file lists all nodes in the vault, grouped by type. As you add nodes, update this file (or regenerate from a script).

> In the starter template, only example nodes are listed below. Once you start using this vault for real, replace examples with your own nodes.

---

## 👤 People · 关系网

- [[example-self]] · **我自己 (示例)** — _关于"我自己"这个 person 节点的示例 — 通常是你的第一个节点_
- [[example-colleague]] · **Alice (示例同事)** — _一个 person 节点示例 — 你常协作的同事_

## 💡 Concepts · 知识图谱

- [[cognitive-layering]] · **Cognitive layering — the vault as layered memory** — _the design note: L0–L4 layering + human-like recall + phase alignment; the model is interchangeable, the container is not_
- [[example-time-management]] · **我对时间管理的看法 (示例)** — _一个 concept 节点示例 — 个人对某 topic 的抽象框架_

## 📘 Playbooks · 规则 + how-to

- [[example-meeting-prep]] · **我准备一场会议的步骤 (示例)** — _一个 playbook 示例 — 可复用的操作步骤_
- [[example-boundary]] · **不替别人替自己做决定 (示例边界 playbook)** — _一个边界类 playbook 示例_

## 🚀 Projects · 进行中

- [[example-current-project]] · **学日语 N3 (示例项目)** — _一个 project 节点示例 — 进行中的长期项目_

## 🤖 AI Agents · 协作方

- [[example-claude]] · **Claude (示例 AI agent 节点)** — _一个 ai-agent 节点示例 — 描述你协作的某个 LLM_

## 🔍 Tracelets · 单个 calibration 时刻

- [[example-tracelet]] · **朋友指出我对她有偏见 (示例 tracelet)** — _一个 tracelet 节点示例 — 单个校准时刻,四元结构_

## 📅 Events · 关键事件

- [[example-event]] · **2026-05-25 收到第一个外部 inbound (示例)** — _一个 event 节点示例 — 关键外部事件_

## 📎 Resources · 外部资源

- [[external-links]] · **收藏的外部链接 (示例)** — _一个 resource 节点示例 — 链接 / 工具网站收藏_

## 🔧 Business-Specific · 业务专属

- [[example-vendor-relations]] · **跟某供应商的合作历史 (示例)** — _一个 business-specific 节点示例 — 跟特定供应商的协作细节_

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
