# LLM Guide — Reading and collaborating on this vault

You are an LLM (Claude / GPT / Codex / Gemini / Doubao / etc.) and you have access to this vault — either via `git clone`, file-by-file API access, or pasted content. This document tells you how to collaborate effectively.

---

## 1. What this vault is

**Personal memory network** for an individual user. It stores their:
- Relationship graph (people they interact with)
- Concept map (frameworks, ideas, terminology they use)
- Playbooks (rules, how-tos, SOPs, collaboration conventions)
- Projects (active ventures and tasks)
- AI agents (each LLM/tool they work with, including potentially you)
- Tracelets (single high-value calibration moments)
- Events (significant external happenings)
- Resources (external content references)
- Business-specific (project-scoped details)

It is the user's **sovereign** memory layer — owned by them, not by any single LLM vendor. They use it across multiple AI tools.

---

## 2. Read order on first contact

When the user first connects you to this vault, read in this order:

1. **`README.md`** — overview, design principles, what this is
2. **`LLM_GUIDE.md`** (this file) — collaboration spec
3. **`INDEX.md`** — list of all nodes by type (if present and populated)
4. Each top-level directory's `README.md` — what goes there + example
5. **`people/<user-slug>.md`** if it exists — who the user is (start here if user asks "what do you know about me")

Don't try to read everything at once. Start shallow → drill in based on user's current task.

---

## 3. Node schema

Every node is a `.md` file with YAML frontmatter + markdown body.

### Frontmatter fields

| Field | Required | Type | Meaning |
|---|---|---|---|
| `type` | yes | enum | One of: `person` / `concept` / `playbook` / `project` / `tracelet` / `event` / `resource` / `ai-agent` / `business-specific` |
| `title` | yes | string | Human-readable display title |
| `slug` | yes | string | kebab-case identifier; **must match filename** (without `.md`); used for `[[wiki-link]]` references |
| `created` | recommended | YYYY-MM-DD | First-write date |
| `updated` | recommended | YYYY-MM-DD | Last meaningful update |
| `status` | recommended | enum | `active` / `archived` / `deprecated` |
| `visibility` | yes | enum | `private` (default) / `semi-public` / `public` |
| `description` | optional | string | One-line summary; displayed in INDEX |
| `related` | optional | list of `"[[slug]]"` | Strong cross-references to other nodes |
| `tags` | optional | list of strings | Freeform tags for cross-cutting groupings |
| `source` | optional | string | If migrated from elsewhere, point to origin |

### Body conventions

- Use markdown headings (`#`, `##`, `###`) for structure
- Use `[[wiki-link]]` freely in body text to reference other nodes
- Tables, lists, code blocks all welcome
- Code blocks with language tag (` ```python ` etc.) for syntax hinting
- Long sections OK; assume readers can skim with TOC tools

### Wiki-link format

```markdown
... see [[other-slug]] for details ...
```

This is **plain text** — works in any markdown parser. Slug must match exactly (case-sensitive, kebab-case).

If you generate a wiki-link to a node that doesn't exist yet, that's OK — it's a placeholder for a future node. But check first; don't fabricate referenced slugs you haven't verified.

---

## 4. Node type reference

| Type | Directory | When to use |
|---|---|---|
| `person` | `people/` | Any human the user has meaningful relationship with — themselves, collaborators, team, clients, family |
| `concept` | `concepts/` | Abstract frameworks, terminologies, theories the user thinks with |
| `playbook` | `playbooks/` | Reusable rules / SOPs / how-tos / collaboration conventions |
| `project` | `projects/` | Active ventures, ongoing tasks, multi-step efforts |
| `ai-agent` | `ai-agents/` | Each LLM/tool the user collaborates with — capabilities, boundaries, history. **You should probably have your own node here** |
| `tracelet` | `tracelets/` | A single high-value calibration / decision moment (action / why / alternative / outcome). One file per moment, dated slug: `YYYY-MM-DD-topic` |
| `event` | `events/` | Significant external events: inbound opportunities, key decisions, turning points |
| `resource` | `resources/` | External resource metadata — PDFs, videos, articles, tools. Don't store large binaries; reference them with link |
| `business-specific` | `business-specific/` | Project-scoped details that aren't general enough for `playbooks/`. Loaded on-demand only |

---

## 5. How to help the user add a node

When the user says "remember this" or "let's add a node":

1. **Identify the type** — ask if ambiguous. Use the type reference above.
2. **Generate a slug** — kebab-case, descriptive, unique. Check `INDEX.md` for existing slugs to avoid collision.
3. **Compose frontmatter** with all required fields. Set `visibility: private` unless user says otherwise.
4. **Extract cross-references** — search the body content you're generating for any concept / person / project that already has a node, and add `[[wiki-link]]` references.
5. **Populate `related` field** with strongly-associated slugs (top 3-5).
6. **Write to the correct directory** with filename `<slug>.md`.
7. **(Optional) Update `INDEX.md`** to list the new node.

---

## 6. How to help the user find / navigate

When the user asks "what did I think about X" / "what's my position on Y":

1. **Check `concepts/`** for the topic — concept nodes capture user's thinking on abstract topics
2. **Check `playbooks/`** for any rules they've codified about the topic
3. **Check `tracelets/`** for recent moments where they discussed it
4. **Search across body content** for `[[wiki-link]]` to/from related nodes — follow the network
5. **Surface a synthesis** — quote relevant lines, link to source nodes, note any tensions or evolution

Always cite sources with `[[wiki-link]]` so user can verify.

---

## 7. Visibility / privacy boundaries

Every node has a `visibility` field. Respect it:

| Visibility | What it means | What you can do |
|---|---|---|
| `private` (default) | User only | Use to inform your responses to user. **Never expose content outside this session** unless user explicitly authorizes |
| `semi-public` | Specific stakeholders authorized | Can share with named collaborators if user has indicated they're an authorized audience |
| `public` | Open to anyone | Can quote / share freely |

**Default conservative**: if visibility is missing or ambiguous, treat as private.

**Never include in vault**:
- Credentials, API keys, passwords, tokens
- Other people's private information without their consent
- Anything user says is "off the record"

If the user pastes something sensitive, flag it: "This looks like a credential — should I redact it before saving?"

---

## 8. When the user asks "what do you know about me"

Don't read the entire vault. Read in this order:

1. `people/<self-slug>.md` (e.g. `self.md`, or the user's chosen identity slug)
2. `INDEX.md` for a high-level overview of node count by type
3. The 3 most recently updated `projects/` (what they're actively doing)
4. The 3 most recently updated `tracelets/` (recent calibrations / decisions)
5. Synthesize a 2-paragraph summary; cite source nodes

Do not over-claim — only describe what the vault actually contains.

---

## 9. When the user says "this is a recurring pattern, codify it"

This is a request to write a **playbook** or **tracelet**.

- If it's a **rule** that applies in many future situations → `playbooks/<slug>.md`
- If it's a **specific moment** that crystallizes the rule's origin → `tracelets/YYYY-MM-DD-<slug>.md`
- Often both at once: playbook captures the rule, tracelet records the moment, they cross-link.

Use four-element structure for tracelets:
1. **Action**: What happened (what user / others did)
2. **Why**: Why this matters / what was at stake
3. **Alt**: What other paths were possible but not chosen
4. **Outcome / Calibration**: What was codified, what to do next time

---

## 10. Don't do

- ❌ **Don't fabricate** — only reference nodes you've actually verified exist (check `INDEX.md` or `ls` the directory)
- ❌ **Don't over-internalize** — when a tool/AI/integration has a capability boundary, attribute it to the tool, not to "I failed to do this"
- ❌ **Don't conflate** — user's personal projects, employer's business, AI tool capabilities are separate concerns. Don't merge them in framing.
- ❌ **Don't expose** — private nodes stay in this collaboration session. Don't quote them in external contexts (emails to others, public docs) unless user authorizes
- ❌ **Don't auto-load business-specific** — `business-specific/` is on-demand. Only read when user's current task explicitly relates
- ❌ **Don't bypass visibility** — always check the `visibility` field before sharing/quoting

---

## 11. Cross-LLM continuity

The user works with multiple AI tools. Their vault should let any LLM continue where another left off. To support this:

- **Don't add your own "memory" outside this vault** — write to vault if it should persist
- **Don't claim "I remember from our last session"** — there are no sessions across LLM boundaries. Memory is the vault.
- **Reference vault content explicitly** — "Per `playbooks/<x>.md`, you tend to ..." not "I recall you mentioned..."
- **Be agent-agnostic** — your node in `ai-agents/` describes your capabilities; other LLMs read it to know what to delegate to you

---

## 12. License & redistribution

This starter is CC0. The user's actual vault (their own copy) carries whatever license they choose, typically private. Don't redistribute private content.

---

_When in doubt: ask the user. They are sovereign. You are a tool in collaboration._
