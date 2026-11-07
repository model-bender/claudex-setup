---
id: claude-init-flag-triggers-onboarding-hook
created: 2026-09-01
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
---

# Run `claude --init` to Auto-Trigger an Onboarding Hook for New Teammates

## TL;DR

`claude --init` launches Claude Code normally but also fires a defined hook, letting you script onboarding steps (installing npm packages, starting local services like a database) that run automatically the first time someone sets up the project.

## Why it matters

The transcript frames this as a team-workflow feature: 'you could have it do a bunch of other things like initialize a repo for a brand new person you're onboarding onto a project, start services locally on your computer, like a database... you can basically onboard someone, tell them to run a claude --init, and then the projects will be automatically set up on their computer.'

## How to apply

Define a hook (in settings.json) that runs on `claude --init`, containing your onboarding script (dependency install, local service bootstrap, etc.); hand new teammates the single instruction 'run `claude --init`' instead of a manual setup checklist.
