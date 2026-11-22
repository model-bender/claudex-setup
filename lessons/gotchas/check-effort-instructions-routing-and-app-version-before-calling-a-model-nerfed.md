---
id: check-effort-instructions-routing-and-app-version-before-calling-a-model-nerfed
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-and-gpt-get-nerfed-after-launch-they-admitted-it_BqFimJpU1g8_20261120.txt
---

# When a model feels worse, check effort, instructions, routing and the app version before blaming the model

## TL;DR

Nate Herk's finding is that post-launch degradation came from four things around the model: the default effort, the system prompt, which model answers, and bugs in the app. Check each before deciding the model was nerfed.

## Why it matters

Each has a case in the transcript: default effort lowered from high to medium, a 25-word limit added to the system prompt, safety routing to another model, and a bug that wiped thinking on every turn. None touched the weights. He also cites one tracker (Margin Lab, as heard) whose measured drop from 65% to about 50% came from an update to the Claude Code app, not the model, and says he found no proof that weights change after launch.

## How to apply

The transcript lists the four without a procedure. This lesson's inference for Claude Code: run `/effort status`, check that the session is on the model you expect with `/model`, and note `claude --version` against the release notes when results change.

Checked: `/effort status` and `/model` confirmed in code.claude.com/docs/en/model-config.md (fetched 2026-11-22), Claude Code 2.1.330. The tracker name and its figures are as heard in the transcript and were not verified.

## Related

[[compare-a-model-with-its-launch-benchmark-at-the-same-effort]], [[check-the-per-model-usage-breakdown-after-a-long-autonomous-run]], [[reasoning-extraction-phrasing-can-silently-reroute-model]]
