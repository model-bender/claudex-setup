---
id: check-claude-debug-for-misspelled-agent-frontmatter-fields
created: 2026-10-11
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# After Writing an Agent File, Check claude --debug for Misspelled Frontmatter Fields

## TL;DR

Since 2.1.296 `--debug` names unrecognized frontmatter fields in custom agent files, with a hint for likely typos.

## Why it matters

A misspelled field (for example `tool:` for `tools:`) used to be ignored silently, so the agent ran without the setting you thought you gave it.

## How to apply

After writing or editing an agent file, start `claude --debug` once and look for the unrecognized-field line before trusting the agent.

> "Improved `--debug` output to name unrecognized frontmatter fields in custom agent files, with a hint for likely typos", Claude Code CHANGELOG 2.1.296
