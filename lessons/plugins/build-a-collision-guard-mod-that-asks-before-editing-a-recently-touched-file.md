---
id: build-a-collision-guard-mod-that-asks-before-editing-a-recently-touched-file
created: 2026-10-11
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-code-mods-are-game-changers-set-up-these-5-now_9hetShMMp2s_20261009.txt
---

# Add a collision guard mod that asks before an edit to a file another chat touched in the last 30 minutes

## TL;DR

Before every Edit, Write or NotebookEdit, a mod checks whether the file was touched in the last 30 minutes and asks you to proceed, move to a worktree, or cancel, instead of silently overwriting a parallel session's work.

## Why it matters

Nate demoed two chats on one HTML file: after one changed a price, the second chat's edit prompted 'another open chat edited the file just now'. He contrasts it with a PreToolUse hook, which would block or act automatically, whereas this surfaces a question in the UI.

## How to apply

Ask Claude to build a mod named collision guard: on Edit, Write and NotebookEdit, check recent-touch time for the target path (30 minute window), and if hit, prompt with proceed, move to worktree, cancel, or free text. Nate notes a skill or CLAUDE.md rule could approximate it but a mod was quick to build.

Checked: Binary 2.1.296: command grep -c -a 'plugin_dev_mods' style check found mods plumbing (grep -c -a '"mods"' = 48 hits incl. a mods directory constant and dev-mods path); /plugin appears as a command string. Mod behavior itself is described only by the speaker; not tested. PreToolUse count 126 in binary (hook event exists).

## Related

[[ask-before-oversized-file-edits-with-a-hook]]
