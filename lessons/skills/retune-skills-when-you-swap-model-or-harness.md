---
id: retune-skills-when-you-swap-model-or-harness
created: 2026-08-29
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-know_UsfCe5fJK6A_20260824.txt
---

# Skills are interpreted differently by every model and harness, so retune them when you switch

## TL;DR

The same SKILL.md produces measurably different depth, tone, and rigor under a different model or harness; when you swap either, rerun your heavy-use skills on a known task, compare against the old output, and rebuild the skill for the new target rather than assuming it transfers.

## Why it matters

The creator ran his "storm research" skill identically in Claude Code and in the DeepSeek harness with the same underlying model available: both followed the skill's structure, but one produced ~5,000 words with 26 sources, in-depth and scientifically conservative, while the other produced ~4,400 words with ~14 load-bearing sources, more relatable but at times overconfident. His conclusion is general: "when you upgrade your model or you switch harnesses, the skills are interpreted a little bit different every time", and a skill built specifically for the new target "would probably do a really really good job". Skills silently degrading after a switch is invisible unless you look, because outputs still arrive.

## How to apply

Keep one or two reference tasks per important skill. After any model upgrade or harness change, rerun those tasks, diff the outputs against your accepted baseline (depth, source count, tone, adherence to the skill's structure), and edit or rebuild the skill's instructions for the new interpreter, tightening what got looser and deleting scaffolding the stronger model no longer needs. Don't trust cross-harness skill portability claims without this check.

## Related

[[rebuild-heavy-use-skills-from-scratch-not-edit]], [[run-a-skill-cold-to-verify-it-still-triggers]]
