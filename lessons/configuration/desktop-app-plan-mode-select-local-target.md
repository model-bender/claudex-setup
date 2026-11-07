---
id: desktop-app-plan-mode-select-local-target
created: 2026-09-01
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Select 'Local' Before Pressing Plan in the Claude Code Desktop App

## TL;DR

The Claude Code desktop app now has a Plan button, but you must have 'local' selected as the target (versus a remote/cloud target) for it to plan against your actual local repository the way the CLI does.

## Why it matters

The transcript specifies this precondition: 'Claude Code has now added planning mode to desktop application. So if you make sure local is selected over here, you can press plan and then basically come up with similar plans like you do in the CLI.' Missing this selection likely means planning against the wrong target or failing silently.

## How to apply

In the desktop app, before using its new Plan button, confirm the session's target/environment is set to Local (not a remote/cloud session) so the resulting plan reflects your actual working repo.
