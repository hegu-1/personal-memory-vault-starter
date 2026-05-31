---
type: concept
title: Cognitive layering — the vault as a layered memory, not a flat folder
slug: cognitive-layering
created: 2026-05-31
updated: 2026-05-31
status: active
visibility: public
description: How to think about this vault as a layered cognitive memory (like a neural net) with human-like recall, so any model that loads it starts from your frame — not just a pile of notes.
related:
  - "[[example-tracelet]]"
tags: [architecture, memory, design]
---

# Cognitive layering

> The directories in this vault aren't just categories. They're **layers** — granular at the bottom, abstract at the top — the way memory actually compounds. The point isn't storage. It's that any model loading this vault starts from *your* frame.

## 1 · Layered like a neural net

Lower layers are fine-grained and raw; upper layers are abstractions built from them. Recall flows upward from a cue; consolidation distills downward over time.

```
L4  telos            why you're building any of this        (the top abstraction)
L3  concepts / playbooks   your frameworks + reusable rules  (semantic + procedural)
L2  projects / resources   consolidated working knowledge
L1  tracelets        single calibration moments (decision · why · alternative · lesson)
L0  events / raw     what happened, re-readable at full grain
```

Invariant: **every line in an upper layer can be unfolded downward** into the finer memory that supports it. The vault can always be refined further down.

## 2 · Recall like human memory

A brain doesn't load everything — a cue triggers it, association spreads, you pull only what's relevant. Build the vault the same way:

- **Working memory** = your INDEX + today's notes (always in view)
- **Episodic** = events / tracelets (what happened, when)
- **Semantic** = concepts (facts decoupled from when you learned them)
- **Procedural** = playbooks (rules that run almost automatically)

Mechanisms:
- **Association** — `[[wiki-links]]` are the synapses; one node cues the next
- **Lazy recall** — load only the activated sub-graph, not the whole vault
- **Salience / recency** — the INDEX stays resident; recent notes get weight
- **Consolidation** — raw → tracelet → concept, distilled upward over time; what isn't reinforced fades

## 3 · Phase alignment (the goal)

Success isn't "the vault has a lot in it." It's the moment a model loads the relevant sub-graph and **starts thinking from your frame** — same priors, same arc. That happens when the right cue surfaces the right layer, and when the vault encodes not just *what* you concluded but *how you got there* (the `why` in your tracelets).

## 4 · The model is interchangeable; the container is not

Because your continuity lives in the vault — not in any one model — you can swap the model and the same "you" lights up on load. That's the whole reason this is files-and-git, not a chat history inside one vendor.

One boundary worth keeping: let the model write the derivative layer (linking, tidying, consistency checks), but **keep the framing and the decisions authored by you**. If everything gets written by the model, the continuity quietly stops being yours.

---

_A design note, not an example. Adapt the layer names to your own directories._
