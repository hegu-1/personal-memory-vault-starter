---
type: ai-agent
title: Claude (示例 AI agent 节点)
slug: example-claude
created: 2026-05-26
updated: 2026-05-26
status: active
visibility: private
description: 一个 ai-agent 节点示例 — 描述你协作的某个 LLM(以 Claude 为例,内容为通用描述)
related:
  - "[[example-self]]"
tags: [ai-agent, anthropic, example]
---

# Claude (示例描述)

## Vendor 信息

- Vendor:Anthropic
- 当前版本:Claude 4.x 系列(Opus / Sonnet / Haiku)
- 我用的入口:Claude.ai 网页 / Claude Code CLI / API

## 能做 ✅(通用描述,按你实际经验补充)

- 长篇 deep reasoning(深度分析 / 多维度评估)
- 代码理解 + 修改 + 调试
- 长 context(支持长文档协作)
- 结构化输出(markdown / 表格 / 代码块)
- 多模态(读图)
- Tool use(配套工具调用)

## 不能做 ❌(已知 boundary)

- 实时网络(默认无,需要 WebFetch 工具)
- 跨 session 记忆(只能通过 vault / memory 文件)
- 图像生成
- 视频生成
- 实时音频处理

## 跟它的协作 history(填你自己的)

- [日期] [一个你跟它合作过的具体场景]
- [日期] [另一次具体协作]
- ...

## 注意 / 偏好

- 它的强项 / 弱项 / 你协作时的小习惯 — 这些是你自己 trial-and-error 出来的,记下来 future 自己看 / 也让其他 AI 知道你的偏好

## 跟其他 AI 对比

- 跟 [其他 LLM,比如 GPT / Gemini] 比,Claude 的相对优势:...
- 你用哪个做哪种 task 的偏好:...

---

_示例文件 — 通用描述,具体协作 history 用你自己的真实场景填。可以为每个常用 AI 各建一个节点(claude.md / gpt.md / gemini.md / midjourney.md 等)_
