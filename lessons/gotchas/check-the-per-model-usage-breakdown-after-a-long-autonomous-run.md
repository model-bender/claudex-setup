---
id: check-the-per-model-usage-breakdown-after-a-long-autonomous-run
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-made-codex-and-claude-code-build-the-same-app-one-clearly-won_WCrnS09vpfo_20260820.txt
---

# After a Long Autonomous Run, Check /usage's Per-Model Breakdown, the Orchestrator May Not Be the Model You Started On

## TL;DR

A multi-hour /goal run started on Fable 5 came back showing Opus 4.8 as the main orchestrator spawning Fable 5 subagents, so read the per-model split in /usage rather than assuming the session stayed on your chosen model.

## Why it matters

The creator started the session on Fable 5 and issued the /goal prompt, then found the usage breakdown listed three models with Opus 4.8 as the main orchestrator and Fable 5 doing subagent work; his own explanation (some safety-safeguard check reverting the orchestrator) is speculation, but the breakdown itself is observed data from /usage. That matters for cost and for interpreting results: you cannot attribute an outcome to a model you were not actually running, and cost per token differs across the models that actually ran. It also matters for reproducibility, because a rerun may not compose the same way. Separately, treat the totals with mild suspicion, in the same session a summary claimed roughly 447 dollars while the /usage stats across the session and its subagents said closer to 800.

## How to apply

After any long unattended run, open /usage and read the per-model rows, not just the total, and confirm which model actually orchestrated. If the orchestrator drifted from what you picked, note it before drawing any conclusion about model quality from the output. Cross-check any cost figure the agent states in prose against the session's own usage stats rather than trusting the narrative summary. Where the model choice is load-bearing, pin models explicitly in skill or subagent frontmatter rather than relying on session inheritance.

## Related

[[cross-check-a-cost-figure-the-agent-states-against-usage]]
