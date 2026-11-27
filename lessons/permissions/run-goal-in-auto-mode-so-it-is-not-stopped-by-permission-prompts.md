---
id: run-goal-in-auto-mode-so-it-is-not-stopped-by-permission-prompts
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/simon-scrapes/give-me-20-minutes-i-will-make-you-a-claude-pro_-URQjhtvxZo_20260920.txt
---

# Run /goal in auto mode or it stalls on permission prompts

## TL;DR

A goal does not change the permission mode. Run it in auto mode; in Manual mode Claude still stops to ask before any tool call your settings do not already allow, and the run is not autonomous.

## Why it matters

The point of /goal is to walk away; a permission prompt on the first tool call defeats it.

## How to apply

Before setting the goal, check the status bar reads `auto mode on`; if not, switch with Shift+Tab (it cycles permission modes) or start with `claude --permission-mode auto`. From the docs check: since 2.1.283, terminal and VS Code sessions start in auto mode by default, but a `permissions.defaultMode` in your settings, a model without auto mode support, or an organization that turns auto mode off leaves the session in another mode, which is when a goal stalls.

Checked: Claude Code 2.1.330 (`--permission-mode` lists `auto` and `manual` in `claude --help`; `/goal` present in the binary). Goal docs (live docs fetched with curl on 2026-11-22): 'A goal doesn't change your permission mode. To let goal turns run unattended, run `/goal` in auto mode. In Manual mode, Claude still asks before tool calls that your settings don't already allow'. Permission modes docs (same date): Shift+Tab cycle, the `auto` starting default from v2.1.283, and the fallback to Manual when auto mode is unavailable.

## Related

[[set-deny-instead-of-prompting-for-unattended-sessions]]
