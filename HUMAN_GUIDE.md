# Human Guide — 5-minute orientation

> 给人类用户的极简上手指南。如果你想要详细版,看配套 PDF《个人记忆仓库 · 小白入门指南》。

---

## 🎯 这是什么

一个你的"私人记忆网络"模板 — 用文件夹 + markdown 文件存你的想法、人、项目、决定。

- 文件就是你的,永久属于你
- 任何 AI 都能读
- 任何设备都能同步(用 git)
- 不绑死任何 APP

---

## 🚀 60 秒上手

### 步骤 1:克隆这个仓库

```bash
# 方法 A:命令行
git clone https://github.com/hegu-1/personal-memory-vault-starter.git my-vault
cd my-vault

# 方法 B:GitHub 网页上点 "Use this template" 按钮,直接创建你自己的仓库
```

### 步骤 2:删除例子文件(可选)

每个目录有 `example-*.md` 示例文件 — 看完格式后可以删除:

```bash
find . -name 'example-*.md' -delete
```

或者保留作参考,以后写新节点时复制改一改。

### 步骤 3:写你的第一个节点

挑一个目录(推荐从 `people/` 开始 — 写你自己):

```bash
# 复制示例作为模板
cp people/example-self.md people/me.md

# 用任何编辑器打开 me.md
open people/me.md     # macOS
# 或者用 VS Code / Typora / 系统记事本 / 等等
```

修改内容,保存。

### 步骤 4:(可选)同步到 GitHub

```bash
git add .
git commit -m "Add first node: me"
git push
```

完成。

---

## 📂 9 个目录是什么用

| 目录 | 放什么 | 例子文件名 |
|---|---|---|
| `people/` | 重要的人 | `me.md` `mom.md` `colleague-alice.md` |
| `concepts/` | 想法 / 框架 / 你信的某种道理 | `time-management.md` `my-view-of-ai.md` |
| `playbooks/` | 做事的方法 / 经验 / 规则 | `how-i-take-notes.md` `meeting-prep.md` |
| `projects/` | 进行中的项目 | `learn-japanese.md` `side-business.md` |
| `ai-agents/` | 你常用的 AI | `chatgpt.md` `claude.md` `doubao.md` |
| `tracelets/` | 关键决定时刻 | `2026-05-26-decided-to-quit-job.md` |
| `events/` | 影响你的大事件 | `2024-09-01-dad-got-sick.md` |
| `resources/` | 收藏的链接 / PDF / 视频 | `good-articles.md` |
| `business-specific/` | 项目专属细节(默认不自动加载) | (留空,按需加) |

---

## ✍️ 一个节点长什么样

每个 `.md` 文件结构:

```markdown
---
type: person
title: 我自己
slug: me
created: 2026-05-26
updated: 2026-05-26
status: active
visibility: private
description: 关于我自己的页面
related:
  - "[[my-current-project]]"
tags: [self]
---

# 我自己

## 基本
- 名字:...
- 工作:...
- 兴趣:...

## 长期目标
- ...

## 最近在思考
- ...

## 相关
- 当前项目见 [[my-current-project]]
```

`[[my-current-project]]` 是"互相提一下"的写法 — 跳到 `my-current-project.md` 这个文件。

---

## 🤖 跟 AI 怎么用

### 简单粗暴

复制某个 `.md` 文件内容,粘贴给 ChatGPT / Claude / 豆包 等,然后问问题:

> "这是我对时间管理的思考(贴上 `concepts/time-management.md` 内容)。我最近遇到 X 情况,你怎么看?"

### 中等

把整个文件夹打包发给支持长文本的 AI(Claude 200K context / GPT 128K 等):

> "这是我的整个记忆仓库。请先读 `LLM_GUIDE.md`,然后帮我做 ..."

### 进阶

用 GitHub 私人仓库 + 给 AI clone URL,AI 长期 access:

> "这是我的 vault:https://github.com/your-user/your-vault. 请按 LLM_GUIDE.md 协作。"

AI 会按 `LLM_GUIDE.md` 的 spec 工作 — 知道节点类型、frontmatter、wiki-link、何时读什么。

---

## 🛠️ 不会 git / markdown 也能用吗

可以。**Level 0 用法**:

1. 下载这个 repo 为 zip(GitHub 网页右上角 "Code" → "Download ZIP")
2. 解压到电脑某个地方
3. 用系统的"备忘录" / Word / 任何文本编辑器打开 `.md` 文件
4. 写、改、保存,就当普通文件夹用

不用 git、不用同步、不用学新东西。**等熟悉了再考虑升级**。

---

## ❓ 想要详细版

看配套 PDF《**个人记忆仓库 · 小白入门指南**》— 15 页中文,完全无技术门槛,涵盖:
- 三档难度(Level 0 文件夹 / Level 1 Markdown / Level 2 GitHub)
- 7 天上手 routine
- 工具推荐
- 7 个常见问题
- 跟 Notion / Obsidian 对比

---

## 📜 License

CC0 1.0 — 你可以拿这个模板做任何事,包括商业化。无需署名。

---

_祝写得开心。你的记忆值得被组织好。_
