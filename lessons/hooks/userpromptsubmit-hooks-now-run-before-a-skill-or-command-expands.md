---
id: userpromptsubmit-hooks-now-run-before-a-skill-or-command-expands
created: 2026-10-19
status: active
supersedes: null
category: hooks
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21299
---

# Match UserPromptSubmit Hooks on the Typed Slash Command: They Now Run Before a Skill or Command Expands

## TL;DR

Since 2.1.299 a UserPromptSubmit hook sees the prompt before a skill or custom slash command expands, and a block now also stops the command's embedded shell lines.

## Why it matters

A hook that matched on the expanded skill text will no longer see that text, and a guard hook now really does cover a command's embedded shell commands. A skill's own front-matter UserPromptSubmit hook first runs on the prompt after the one that invokes the skill (same release).

## How to apply

Write UserPromptSubmit matching against the typed `/command args`, and re-test any guard that relied on seeing the expanded body. Checked: existing hook event, no new name.

> "Changed `UserPromptSubmit` hooks to run before a skill or custom slash command expands, so a hook that blocks the prompt now also stops its embedded shell commands", Claude Code CHANGELOG 2.1.299

## Related

[[userpromptsubmit-hook-auto-injects-semantic-memory-matches]]
