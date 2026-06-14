---
type: playbook
title: Weekly review (example)
slug: example-weekly-review
created: 2026-06-14
updated: 2026-06-14
status: active
visibility: private
description: A playbook example — the weekly consolidation pass that turns raw notes into a compounding network
related:
  - "[[example-vault-maintenance]]"
  - "[[example-time-management]]"
tags: [review, ritual, example]
---

# Weekly review

A 10–15 minute pass, once a week, that does the consolidation work described in [[example-vault-maintenance]]. Pick a fixed slot (e.g. Sunday evening).

## Steps

1. **Sweep the week's raw capture** — read new `events/` and `tracelets/` since the last review.
2. **Promote upward** (see [[cognitive-layering]] for why):
   - An `event` that taught you something → write or update the `tracelet`.
   - A `tracelet` whose pattern keeps recurring → codify it into a `playbook`.
3. **Link** — add any `[[wiki-link]]`s you skipped during fast capture; update `related` fields.
4. **Update project status** — advance `projects/` milestones; archive what's done.
5. **Regenerate the index** — `python scripts/build-index.py`.
6. **One-line journal** — optionally drop a dated note on what changed this week.

## Why weekly

Daily is too noisy to see patterns; monthly is too sparse to catch them while they're fresh. Weekly is the cadence where raw notes are still legible but enough has accumulated to distill.

## Related

- The capture / prune cadence around this: [[example-vault-maintenance]]
- Where this fits in your week: [[example-time-management]]

---

_Example file._
