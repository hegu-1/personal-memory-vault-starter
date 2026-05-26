# business-specific/

存项目 / 业务专属细节 — **默认不自动 load**,按需读取。

## 什么时候用

- 某个 detail 跟特定项目 / 公司 / 客户 deeply 绑定
- 不适合作通用 playbook(不可复用到其他场景)
- AI 协作时只在该 context 下需要 load

## 区分于 playbooks/

- **playbook**:通用规则,跨项目复用
- **business-specific**:某项目独有,换项目不适用

## LLM 协作约定

`LLM_GUIDE.md` 第 10 条:**Don't auto-load business-specific** — 默认不读,只在用户当前 task 明确 relate 时才读。

## 例子

见 `example-vendor-relations.md`。
