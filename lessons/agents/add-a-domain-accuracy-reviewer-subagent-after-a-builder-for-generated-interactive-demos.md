---
id: add-a-domain-accuracy-reviewer-subagent-after-a-builder-for-generated-interactive-demos
created: 2026-10-25
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/karpathy-is-right-your-attention-is-the-new-bottleneck_IFNum8_oAD8_20261022.txt
---

# When Claude Builds Interactive Teaching Demos, Chain a Builder, a Clarity Reviewer and a Domain-Accuracy Reviewer

## TL;DR

When some of Claude's interactive diagrams and demos came out wrong and confusing, Ray had each chapter go through a builder, then a clarity reviewer, then a subject-accuracy reviewer (physics, in his case).

## Why it matters

Ray reports the problem (some diagrams and demos were wrong and confusing) and the fix he adopted, a physics reviewer "to basically make sure the physics is still accurately depicted". He does not report what the reviewers caught or how much the output improved, so treat this as a pattern to try, not a measured result.

## How to apply

In a dynamic workflow or subagent chain, define three roles per unit of output: a builder, a clarity reviewer, and a reviewer for factual accuracy in your domain. As this lesson's own suggestion (not from the video), let both reviewers see the builder's output before you do. Checked: n/a (a pattern, no mechanism claim). The transcript gives no prompts or reviewer outputs, so how to define the reviewers is left to the reader.

## Related

[[builder-validator-subagent-chain-via-main-agent]]
