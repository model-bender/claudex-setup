---
id: set-project-instructions-to-load-both-claude-md-and-agents-md
created: 2026-10-25
status: active
supersedes: null
category: configuration
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1x7zbvd/claude_runs_1800_useless_tests_creates_more/ph8nhhs/
---

# With Both CLAUDE.md and AGENTS.md in a Repo, Set Project Instructions to Load Both or AGENTS.md Is Skipped

## TL;DR

The default Project instructions mode, `claude-md-or-agents-md`, loads AGENTS.md only where a project has no CLAUDE.md, so a repo with both silently ignores AGENTS.md; switch to `claude-md-and-agents-md` in /config or import `@AGENTS.md` from CLAUDE.md.

## Why it matters

In the thread, the poster kept adding rules to AGENTS.md and Claude kept ignoring them. The existing fallback lesson covers the no-CLAUDE.md case, not the setting that fixes the both-files case.

## How to apply

Open /config, set Project instructions to `claude-md-and-agents-md` (AGENTS.md loads beside CLAUDE.md, and a file CLAUDE.md already imports is not loaded twice), or add `@AGENTS.md` to CLAUDE.md, then confirm in /memory that both load. Checked against the installed 2.1.310 binary: user setting `instructionFiles`, titled Project instructions, with options `claude-md`, `claude-md-or-agents-md` (default), `claude-md-and-agents-md` and `managed-only`. The commenter's claim that a CLAUDE.local.md alone also blocks the fallback was not confirmed.

> "In current Claude Code, the default chooses CLAUDE.md files instead when a project CLAUDE.md or CLAUDE.local.md exists. The Project instructions setting in /config can load both, or CLAUDE.md can import @AGENTS.md.", u/MonkeyCrumbs on r/ClaudeCode

## Related

[[claude-code-falls-back-to-agents-md-import-it-to-be-sure]]
