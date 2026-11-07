---
id: route-tasks-to-a-model-by-the-cost-of-being-wrong-not-difficulty
created: 2026-10-19
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeAI/comments/1x2jwk8/when_do_you_switch_claude_model_and_effort_level/pf2t33a/
  - https://www.reddit.com/r/ClaudeCode/comments/1x0kzbh/haiku_55_is_40x_cheaper_than_opus_55_your_explore/pelz51k/
---

# Route Tasks to a Model by the Cost of Being Wrong, Not by How Hard the Task Sounds

## TL;DR

Pick the model by whether you would notice a wrong answer and how much it costs: work where a mistake shows at once and is cheap to rerun goes to Haiku or Sonnet, work where a mistake is hidden or expensive goes to Opus.

## Why it matters

Task difficulty is a poor guide: a hard-sounding refactor with a full test suite fails loudly, while an easy-sounding fact check or migration plan can be wrong in ways nobody catches. A commenter in another thread states a closely related rule: route by whether the output can be checked.

## How to apply

For each task type or subagent, ask "would I notice if this were wrong, and what would it cost?" Send noticeable, cheap-to-redo work down the ladder and unverifiable or expensive work up, and make the output more verifiable (tests, a checker) when you want to move a task down.

> "the rule i use is cost of being wrong, not how hard the task sounds.", u/London-Boat on r/ClaudeAI

> "Short version: route by verifiability, not difficulty.", u/zaibatsu on r/ClaudeCode

## Related

[[give-code-search-subagents-to-haiku-but-keep-fact-checking-on-opus]], [[model-selection-opus-sonnet-haiku-use-cases]], [[design-agent-output-for-verifiability-before-building-evals]]
