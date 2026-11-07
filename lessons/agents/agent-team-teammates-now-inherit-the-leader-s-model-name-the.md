---
id: agent-team-teammates-now-inherit-the-leader-s-model-name-the
created: 2026-08-22
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Agent-Team Teammates Now Inherit the Leader's Model: Name the Model in the Spawn

## TL;DR

The "Default teammate model" setting is gone; every teammate now runs on the leader's model unless the spawn call passes one explicitly.

## Why it matters

If you led a team on an expensive model and relied on that setting to keep teammates cheap, every teammate silently escalated to the leader's model, multiplying cost across a fan-out. The knob it replaced no longer exists to check.

## How to apply

Pass the model in the spawn (the Agent tool's `model` parameter, or the agent definition's `model:` frontmatter) for each teammate, and stop looking for the removed `/config` setting.

> "Removed the \"Default teammate model\" setting from `/config`; agent-team teammates now use the leader's model unless the spawn names one", canonical: Claude Code CHANGELOG 2.1.234
