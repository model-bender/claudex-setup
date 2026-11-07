---
id: route-planning-to-grill-me-when-it-fits-one-session-and
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://www.latent.space/p/wayfinder-skill
---

# Route planning to /grill-me when it fits one session and /wayfinder when it does not

## TL;DR

Pick the self-interview skill for work whose path you can already see, and the orchestrator skill for work where the end state is still unknown, using "does this fit in one planning session?" as the test.

## Why it matters

The archive covers the grill-me/self-interview pattern and how to batch its questions, but has no lesson on when that pattern is the wrong tool. The failure mode it names is specific: forcing open-ended work through a single alignment session makes you babysit your own context window ("how many tokens am I into my context window? How deep am I going here?") instead of planning.

## How to apply

Before planning, ask whether you can see the whole path. If yes, run /grill-me (or your alignment skill) in one session. If the end state is genuinely undecided, run an orchestrator layer (/wayfinder, https://www.aihero.dev/skills-wayfinder) that splits planning across child sessions for research, prototyping and grilling, and pulls the results back into one document.

> "Use 'grill me' in cases where you feel like you can plan the whole thing in a single session, and you need to align before you go. So most small features will fit into this. Most stuff where you can see the path ahead of you, but you just want to make sure the agent is on board, 'grill me' will work with that. For stuff where you don't know the path ahead, for stuff where you can feel the fog of war in front of you, use wayfinder.", Matt Pocock (interviewed by Latent Space / swyx)
