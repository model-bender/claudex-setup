---
id: set-background-false-on-forked-skills-you-need-inline
created: 2026-07-25
status: active
supersedes: null
category: skills
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Set `background: false` on a `context: fork` Skill When You Need Its Result Inline

## TL;DR

Forked-context skills now detach into the background by default, so a skill you relied on to return its answer into the current turn will silently stop doing that unless you set `background: false`.

## Why it matters

`context: fork` is the standard recommendation for running a skill in isolation without polluting the main context, that recommendation now carries a behavioural rider that changes *when*, and whether, you see the output in-session. Nothing errors; the skill simply runs elsewhere and the turn moves on without its result.

## How to apply

In the skill's frontmatter, keep `context: fork` but add `background: false` for any forked skill whose output the main session must consume in the same turn. Leave the default in place for genuinely fire-and-forget skills, where backgrounding is the win.

> "Changed skills with `context: fork` to run in the background by default; opt out per skill with `background: false`", Claude Code CHANGELOG 2.1.218

