---
id: dangerously-skip-permissions-can-damage-your-os
created: 2026-09-01
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
---

# Reserve --dangerously-skip-permissions for Disposable Environments

## TL;DR

Running Claude Code with `--dangerously-skip-permissions` removes the accept-prompts safety net entirely; used aggressively it can damage your actual machine.

## Why it matters

John Kim recounts having to reflash an entire Linux machine after using this flag too aggressively while it was touching the OS; he now limits it to environments he can throw away.

## How to apply

Only use `--dangerously-skip-permissions` on throwaway VMs, containers, or side projects, not on a machine you rely on, especially for tasks that touch OS-level configuration.

