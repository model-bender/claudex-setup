---
id: subagent-definitions-live-in-one-ballooning-file
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/better-than-mcps-claude-code-s-new-skills-feature_20260307.txt
---

# A Subagent's Whole Definition Lives in One File and Can Balloon to 1000+ Lines

## TL;DR

Unlike a skill (main file plus lazily-loaded reference files), a subagent is defined entirely within a single file, so as you keep adding context it can grow to 500-1000+ lines with no progressive disclosure.

## Why it matters

Ray Amjad calls this out as a practical downside of the subagent primitive versus skills' split main-file/reference-file structure.

## How to apply

If a subagent's definition file is growing large, consider whether the task is actually a better fit for a skill, which can split reference material into separate files loaded only when needed.

## Related

[[skill-md-under-200-lines-progressive-disclosure]]
