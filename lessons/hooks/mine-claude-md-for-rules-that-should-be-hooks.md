---
id: mine-claude-md-for-rules-that-should-be-hooks
created: 2026-11-22
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Point /plugin-authoring at your CLAUDE.md and ask which rules should become hooks

## TL;DR

Ask Claude to read your CLAUDE.md files and propose hooks that would enforce those rules deterministically, then remove the rules it converts.

## Why it matters

Things you have been putting in CLAUDE.md can move into well-defined hooks, giving more reliable behaviour than instructions that can be forgotten.

## How to apply

Run `/plugin-authoring`, point it at the CLAUDE.md files and ask which hooks can be made to ensure more reliable deterministic behaviour. Delete each converted rule from CLAUDE.md.

Checked: Live docs at code.claude.com/docs/en (fetched 2026-11-22), plugins/mods pages: function hooks are documented as 'mods' (a plugin whose hooks are JavaScript or TypeScript functions run inside Claude Code), requiring v2.1.287+. commands.md lists `/plugin-authoring`. The audit prompt is the speaker's suggestion.

## Related

[[ask-claude-to-suggest-mods-from-your-session-logs]]
