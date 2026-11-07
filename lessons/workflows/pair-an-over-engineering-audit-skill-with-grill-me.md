---
id: pair-an-over-engineering-audit-skill-with-grill-me
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/sean-kochel/why-your-agentic-workflows-don-t-work_ILKrUq_8aC4_20260820.txt
---

# Pair an Over-Engineering Audit Skill With a Grill-Me Skill During the Pruning Phase

## TL;DR

During context pruning after exploration, run a skill that audits the generated ideas for over-engineering alongside a 'grill me' style skill that interrogates you on real intent, then discard anything that doesn't need solving now.

## Why it matters

Sean Kochel says coding agents will 'over-engineer something that then becomes a beast' during exploration unless you actively audit and challenge the generated ideas before they reach the plan; running both skills together is his specific mitigation.

## How to apply

After the exploration phase generates a pile of ideas/directions, run an over-engineering-audit skill (he references a version of the 'ponytail' style audit repo) together with a grill-me-style interrogation skill on the same material, and only carry forward what survives both.

## Related

[[route-planning-to-grill-me-when-it-fits-one-session-and]], [[prune-exploration-output-before-it-feeds-the-plan]]
