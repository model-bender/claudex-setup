---
id: make-the-agent-predict-the-output-before-it-runs-code
created: 2026-11-22
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-another-andrej-karpathy-using-claude_bvGptCLDhyo_20261009.txt
---

# Have the agent state the expected output before running code, then compare

## TL;DR

Add a rule that the agent says what it expects to see before each run, runs it, and shows the real output next to the prediction.

## Why it matters

The rule comes from Karpathy's teaching habit as described in the video: Karpathy states the expected number before running a cell because, as the video quotes Karpathy, most of the time a model will train but silently work a bit worse. A stated prediction is what exposes that gap.

## How to apply

Put 'predict, then run, then compare' in the agent's instructions. In the demo the agent builds the smallest version on a tiny input, states the expected result, runs it and shows the actual output.

Checked: No mechanism named. Attribution to Karpathy is the video's.

## Related

[[compare-redesign-skill-output-before-trusting-it]]
