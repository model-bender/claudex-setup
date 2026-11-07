---
id: claude-maintenance-flag-with-dispatcher-script
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Use `claude --maintenance` With a Hook Dispatcher to Separate Init Logic From Maintenance Logic

## TL;DR

`claude --maintenance` triggers a distinct hook from `--init`/`--init-only`; build a small dispatcher script that checks which mode invoked the hook and branches to the matching sub-script (e.g. npm install for init, formatting/doc updates/dependency bumps for maintenance).

## Why it matters

The transcript describes the pattern directly: 'basically the way you would differentiate between the three modes is you would make a hook dispatcher that looks kind of like this. Then you would trigger a different script each time... with maintenance, you could do like formatting or updating documentation by spawning up more instances of Claude Code and doing stuff like making sure dependencies [are up to date].'

## How to apply

Write one hook script registered for all three invocation modes; inside it, branch on which mode fired (init vs init-only vs maintenance) and call a separate purpose-built script per branch, so onboarding setup and periodic maintenance (formatting, doc refresh, dependency bumps) don't share one undifferentiated script.
