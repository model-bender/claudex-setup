---
id: set-once-true-to-prevent-duplicate-hook-runs
created: 2026-08-31
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
  - transcripts/ray-amjad/anthropic-just-added-these-features-to-claude-code_20260307.txt
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
  - transcripts/simon-scrapes/every-claude-code-memory-system-compared-so-you-don-t-have-to_20260424.txt
  - transcripts/john-kim/claude-code-s-new-agent-teams-are-insane-opus-4-6_20260424.txt
---

# Set `once: true` on a Hook So a Side-Effecting Command Fires Only Once

## TL;DR

A hook whose event keeps matching will re-run its command; adding `once: true` to the hook definition prevents duplicate runs, so a side-effecting hook like a plan-archiving script executes exactly once.

## Why it matters

Hooks with side effects (archiving a plan, sending a notification, mutating a file) repeat that side effect every time the matched lifecycle event fires again. Duplicate runs create duplicate artifacts and noise, and there is no obvious symptom beyond the repetition itself. The `once: true` field is the built-in dedupe and is easy to miss because it lives inside the hook definition, not in any prompt or setting you normally review.

## How to apply

Add `once: true` to the hook object where you define it, in settings.json for global hooks or in skill/agent YAML frontmatter for scoped ones. Example: {"event": "PostToolUse", "tool": "ExitPlanMode", "command": "./archive-plan.sh", "once": true} archives the approved plan a single time instead of on every subsequent match. Use it on any hook whose command should not repeat within a session.

## Related

[[hooks-for-automation-and-guardrails]]
