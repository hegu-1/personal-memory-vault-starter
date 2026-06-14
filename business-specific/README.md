# business-specific/

Project- / business-scoped details — **not auto-loaded by default**, read on demand.

## When to use

- A detail that's deeply tied to one specific project / company / client
- Not suitable as a general playbook (not reusable in other contexts)
- Something an AI collaborator should only load within that context

## How this differs from playbooks/

- **playbook**: a general rule, reusable across projects
- **business-specific**: unique to one project, doesn't apply elsewhere

## LLM collaboration convention

`LLM_GUIDE.md` rule 10: **Don't auto-load business-specific** — don't read it by default, only when the user's current task explicitly relates to it.

## Examples

See `example-vendor-relations.md`.
