---
id: baseline-with-claude-safe-mode
created: 2026-11-22
status: active
supersedes: null
category: commands
tool: claude-code
sources:
  - transcripts/austin-marchese/the-real-reason-the-creator-of-claude-code-told-you-to-delete-everything_kCUZqM8-Z-4_20260920.txt
---

# Use `claude --safe-mode` as a no-customisation baseline

## TL;DR

`claude --safe-mode` starts Claude Code with your customisations disabled, which shows what the bare model does on a task without deleting anything.

## Why it matters

It answers 'is my setup helping or hurting?' the way deleting everything would, with no risk to the files.

## How to apply

Pick a task Claude tends to get wrong for you, run `claude --safe-mode`, and do the task. That result is the baseline to compare your configured setup against.

Checked: `claude --help` on Claude Code 2.1.330: `--safe-mode` starts with all customizations disabled (CLAUDE.md, skills, installed plugins, hooks, MCP servers, custom commands and agents, output styles and more); admin-managed policy settings still apply; sets CLAUDE_CODE_SAFE_MODE=1. Live CLI reference adds that auto memory does not load. Transcript rendering 'Claude-safe-mode' corrected.

## Related

[[keep-the-context-half-of-a-skill-delete-the-procedure-half]]
