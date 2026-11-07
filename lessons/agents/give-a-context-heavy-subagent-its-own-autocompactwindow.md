---
id: give-a-context-heavy-subagent-its-own-autocompactwindow
created: 2026-10-11
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Give a Context-Heavy Subagent Its Own autoCompactWindow in Frontmatter

## TL;DR

Since 2.1.296 subagent frontmatter and `--agents` definitions accept `autoCompactWindow`, so a subagent can auto-compact earlier than the main conversation.

## Why it matters

A worker that reads many files fills its context fast and degrades before the main session would compact.

## How to apply

Add `autoCompactWindow: <tokens>` to the agent file (or the JSON passed to `--agents`) with a lower number than the main session uses. Checked: `autoCompactWindow` has 53 hits in the 2.1.296 binary, mostly the global setting; the frontmatter field rests on the changelog line.

> "Added `autoCompactWindow` to subagent frontmatter and `--agents` definitions, so a subagent can auto-compact earlier than the main conversation's window", Claude Code CHANGELOG 2.1.296

## Related

[[set-a-fixed-token-auto-compact-window]]
