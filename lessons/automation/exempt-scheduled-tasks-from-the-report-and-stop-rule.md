---
id: exempt-scheduled-tasks-from-the-report-and-stop-rule
created: 2026-09-12
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Exempt Scheduled Tasks From Your Report-and-Stop Rule

## TL;DR

The assessment-only rule that stops Claude taking unrequested actions is the wrong default for scheduled runs: Anthropic gives those the opposite instruction, to operate autonomously and proceed on reversible actions.

## Why it matters

A global 'report your findings and stop' line is the standard fix for Claude 5 acting before you asked. But scheduled tasks run while you are not there, so a rule that makes them stop and wait for confirmation turns every run into a no-op that surfaces a question nobody reads. Anthropic's own system prompt for scheduled tasks says the reverse, which is the signal that the boundary rule belongs to interactive sessions only.

## How to apply

Keep the report-and-stop paragraph in your interactive CLAUDE.md or project instructions, and in each scheduled task's own prompt state that it should proceed autonomously on reversible actions and only surface irreversible ones. If your scheduled tasks share the same instruction file, scope the rule with a conditional so it does not apply to unattended runs.

## Related

[[assessment-only-mode-for-diagnostic-tasks]], [[routines-with-claude-generated-prompts]], [[harden-always-on-agents-least-privilege-and-capable-models]]
