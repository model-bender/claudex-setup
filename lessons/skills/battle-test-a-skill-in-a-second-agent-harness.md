---
id: battle-test-a-skill-in-a-second-agent-harness
created: 2026-09-24
status: active
supersedes: null
category: skills
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineer-explains-what-to-build-instead-of-ai-agents_HIRDzMtuWFk_20260920.txt
---

# Battle-Test an Important Skill in a Second, Compatible Agent Harness

## TL;DR

Run a heavily-used skill through a different compatible harness (Claude Code and Codex, for example) on the same task and compare. If the result falls apart in the second harness, the skill has hidden assumptions or examples that only one model understands, tighten it and retest.

## Why it matters

Agent skills are an open markdown format, so the same skill folder loads in multiple harnesses, but that does not mean the skill is model-proof: different models interpret the same instructions differently, and a skill tuned only against one model can silently rely on things only that model infers correctly.

## How to apply

Copy the skill folder into a second compatible harness (or point it at the same shared skills directory). Run the same task through both. If the second harness's output is noticeably worse, look for hidden assumptions, missing examples, or instructions phrased in a way only one model reliably understands, then tighten the skill and retest in both.

## Related

[[retune-skills-when-you-swap-model-or-harness]]
