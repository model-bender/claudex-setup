---
id: run-a-meta-audit-across-all-project-setups
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-choose-the-right-ai-agent_6LNlCpQPYFc_20260920.txt
---

# Run one audit across all your project setups to get per-project fixes and cross-project rules

## TL;DR

Have a single overseeing setup audit every project's configuration and return two lists: improvements specific to each project, and improvements that generalise to all of them.

## Why it matters

The guest keeps many isolated setups (he gives 25 as an example, one per area of his business) and says that is more to upkeep. His 'mega system' audits every one of them and comes back with fixes for each setup plus ones that generalise across all of them. He separately keeps everything project-scoped until it deserves promotion to global; treating the cross-project list as the promotion candidates is this lesson's inference.

## How to apply

From a parent folder (or a dedicated project that can read the others), ask the agent to review each project's instruction files, skills and rules, then report per-project changes and candidates for the global level.

Checked: No mechanism named.

## Related

[[default-new-assets-to-project-scope-promote-to-global-when-proven]], [[write-each-setup-audit-to-a-dated-report-so-the-score-trends]]
