---
id: compare-a-model-with-its-launch-benchmark-at-the-same-effort
created: 2026-11-22
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/claude-and-gpt-get-nerfed-after-launch-they-admitted-it_BqFimJpU1g8_20261120.txt
---

# Compare a model to its launch benchmark at the same effort, since Claude Code defaults to medium

## TL;DR

The Opus 5.5 benchmark scores the speaker cites were run at max effort, while Claude Code starts Opus 5.5 at medium. Before judging a demo or benchmark, check the effort it used, and raise effort yourself for work that needs it.

## Why it matters

The speaker gives 57.8% versus 52% for Opus 5.5 as the gap between the benchmark's max effort and the default medium, and notes more effort costs time and money, so neither extreme fits every task.

## How to apply

Run /effort status to see the session's level. Raise it with /effort <level> or launch with claude --effort <level>. The docs say max applies to the current session only unless set through CLAUDE_CODE_EFFORT_LEVEL.

Checked: code.claude.com/docs/en/model-config.md fetched 2026-11-22: 'Fable 5.2, Opus 5.5, Sonnet 5.5, and Haiku 5.5 default to medium'; /effort, /effort status, --effort and CLAUDE_CODE_EFFORT_LEVEL confirmed; Claude Code 2.1.330. The 57.8 and 52 figures are the speaker's and were not verified.

## Related

[[default-to-medium-effort-and-save-xhigh-for-the-research-turn]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
