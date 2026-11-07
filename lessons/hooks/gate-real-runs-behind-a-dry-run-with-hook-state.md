---
id: gate-real-runs-behind-a-dry-run-with-hook-state
created: 2026-09-12
status: active
supersedes: null
category: hooks
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-the-biggest-claude-code-update-yet_B-YQANvDOq0_20260910.txt
---

# Block the Real Run Until the Dry Run Has Happened, and Show Which Mode You Are In

## TL;DR

Because function hooks hold state across turns, a hook can refuse every real command until the dry-run command has actually been executed in that session, and paint a large marker in the UI saying whether you are in dry mode or production.

## Why it matters

For data analysis and anything with irreversible effects, the dry run is the step people skip under time pressure, and the mode you are in is exactly the thing nobody re-checks. The hook makes the ordering a precondition rather than a habit, and the banner removes the ambiguity that causes the mistake.

## How to apply

Have the hook record that the dry run completed in its store, block matching real commands until that flag is set, and render a mode banner from the same state. Combine with the ask primitive so overriding the gate is a deliberate answer rather than a silent pass.

## Related

[[hooks-for-automation-and-guardrails]], [[draw-a-live-status-row-from-a-function-hook]]
