---
id: default-new-assets-to-project-scope-promote-to-global-when-proven
created: 2026-09-24
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-choose-the-right-ai-agent_6LNlCpQPYFc_20260920.txt
---

# Default Every New Skill or Rule to Project Scope, Promote to Global Only Once Proven

## TL;DR

Keep new skills, rules, and CLAUDE.md additions scoped to the project they were built for by default ("everything is project until it deserves to be promoted to global"). This keeps the global footprint small and gives a small blast radius when debugging a regression.

## Why it matters

A setup where everything defaults to global means a rule added for one project's edge case silently applies everywhere, so when output quality drops on an unrelated project you can't tell whether the cause is the model, the harness, or a global rule bleeding in from elsewhere. Keeping new additions project-scoped isolates that variable: 'because I'm so meticulous about is this a model problem, is this a harness problem, or is this an organization problem, when I can isolate things, I can find the issue faster.'

## How to apply

Write new skills, rules, and CLAUDE.md additions into the project's own config first, and promote to global only once the thing has earned it. The source gives no promotion test; a workable one (ours, not the creator's) is that it has helped in a second, unrelated project. Keep a running sense of what actually lives at global scope so it stays small enough to review, rather than letting it accumulate by default.

## Related

[[scope-skills-per-project-not-globally-to-cut-startup-context]]
