---
id: subagent-spawn-cap-of-200-per-session-removed
created: 2026-08-07
status: active
supersedes: null
category: automation
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Drop Session-Restart Workarounds for the 200-Subagent Cap, and Bound Spend Explicitly Instead

## TL;DR

The 200-subagent-per-session spawn cap is gone as of 2.1.224, so long-running sessions no longer refuse new agents. Concurrency and depth limits still apply.

## Why it matters

Two groups need to change something. Anyone who restarted sessions, batched work, or pruned agent counts to dodge the refusal can delete that workaround. More importantly, anyone who was implicitly relying on the cap as a ceiling on runaway fan-out has lost a brake they may not have realised they had.

## How to apply

Remove periodic-restart workarounds from long-lived orchestrator sessions. If you were counting on the cap to bound spend, replace it with something explicit: `--max-budget-usd`, a concurrency limit, or a spawn-depth pin.

> "Removed the 200-subagent-per-session spawn cap; long-running sessions no longer refuse new agents (concurrency and depth limits still apply)", Claude Code CHANGELOG 2.1.224

## Related

[[pin-subagent-spawn-depth-the-default-flipped-twice]], [[workflow-size-medium-now-means-under-10-agents]]
