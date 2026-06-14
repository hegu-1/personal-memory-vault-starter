---
type: playbook
title: Keeping your vault alive (example)
slug: example-vault-maintenance
created: 2026-06-14
updated: 2026-06-14
status: active
visibility: private
description: A playbook example — the practice that keeps a vault compounding instead of going stale
related:
  - "[[example-weekly-review]]"
  - "[[cognitive-layering]]"
tags: [maintenance, ritual, example]
---

# Keeping your vault alive

A vault is only worth anything if you keep using it. The most common failure isn't a wrong structure — it's a vault that gets three nodes and is then abandoned. This playbook is the practice that prevents that.

## The one rule

**Capture in the moment, consolidate on a schedule.** Raw capture is cheap and frequent; distillation is deliberate and rare.

## Daily — capture (1–2 min, as it happens)

- When something worth remembering happens, drop it into the closest node — or a new `events/` or `tracelets/` node — without polishing.
- Don't organize while capturing. A messy true note beats a clean note you didn't write.
- If you're working with an AI, just say "remember this" and let it file the node (see `LLM_GUIDE.md` §5).

## Session start — re-enter (30 sec)

Before a working session (with or without an AI), reload your frame:

1. Open `INDEX.md`
2. Skim the 3 most recently updated `tracelets/` and `projects/`
3. Your working memory is now restored — start.

(An AI should do the same on first contact — `LLM_GUIDE.md` §2 and §8.)

## Weekly — consolidate (10–15 min)

This is where the network compounds. See [[example-weekly-review]] for the step-by-step. In short:

- **Promote**: a raw `event` that turned into a lesson → write the `tracelet`; a recurring `tracelet` → codify the `playbook`.
- **Link**: add the `[[wiki-link]]`s you skipped during fast capture; fill `related`.
- **Regenerate the index**: `python scripts/build-index.py`.

## Monthly — prune (5 min)

- Mark finished or stale nodes `status: archived` (don't delete — archived history is still memory).
- Mark superseded rules `status: deprecated` and link to whatever replaced them.
- Anything you haven't touched and can't justify keeping → archive it. What isn't reinforced should fade (see [[cognitive-layering]] §2).

## Anti-patterns

- ❌ Organizing instead of capturing (you'll capture less)
- ❌ Deleting old nodes (you lose the lineage — archive instead)
- ❌ Letting `INDEX.md` rot (it's your working-memory layer — regenerate it)
- ❌ Treating the vault as a write-only archive (the value is in re-reading and consolidating)

---

_Example file. This is the practice layer — adapt the cadence to your own rhythm._
