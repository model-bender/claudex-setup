---
id: write-an-auto-handoff-mod-that-starts-a-new-session-at-a-context-threshold
created: 2026-10-11
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/mark-kashef/claude-code-now-has-mods-here-are-10-worth-stealing_uvIopT_2sY0_20261009.txt
---

# Build an auto-handoff mod that hands the session to a fresh one at a context percentage

## TL;DR

A mod can watch context use and hand the session off to a new one once it passes a threshold, with a manual /handoff now command to trigger it early.

## Why it matters

Mark says that with a million-token window, quality drops past roughly 400 to 500 thousand tokens, and he does not want to keep checking the corner of the screen. His mod runs at an 85 percent threshold, and he says you could set it near 40 or 50 percent.

## How to apply

Describe the mod to Claude Code in plain language: commands /auto-handoff on|off, a configurable threshold, and /handoff now that writes the handoff and opens a new session. Install it as a plugin. Pick a threshold below the point where you see quality degrade (his own 85 percent is a ceiling, not a recommendation).

## Related

[[build-claude-code-mods-as-plugins-installed-at-user-scope]]
