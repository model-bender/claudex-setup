---
id: codex-goal-runs-keep-going-when-codex-asks-a-question-you-do-not-answer
created: 2026-10-02
status: active
supersedes: null
category: prompting
tool: [codex, claude-code]
sources:
  - transcripts/nate-herk-ai-automation/i-tested-opus-5-5-vs-gpt-6-astra-on-12-real-use-cases_GmLcJVzkxPA_20261002.txt
  - transcripts/nate-herk-ai-automation/i-had-opus-5-5-build-me-the-same-app-at-every-effort-level_QCkHIyEPIYo_20261002.txt
---

# In a Codex /goal Run, a Question From Codex Does Not Stop the Run, While Claude Code Rarely Asks

## TL;DR

The creator reports that Codex raises clarifying questions in the middle of a /goal run but continues if you do not answer. In their six Opus runs on one /goal prompt, Claude Code asked a question only once.

## Why it matters

Across their comparison videos they say Codex asks more questions than Claude Code, which they like because it tailors the result, and that it 'doesn't actually stop': the question is injected into the chat and the goal carries on. Example: Astra asked what numbers to put on an investor deck, while Opus filled them in without asking. In the effort-level test, five of six Claude Code /goal runs asked nothing and one asked a single question. This is their experience, not documented behavior.

## How to apply

For an unattended /goal run in Codex, check the thread when you return and answer any questions it left, since the run will not have waited. For Claude Code, if you need it to confirm details such as real metrics before filling them in, say so in the goal prompt. The second action is the lesson's suggestion.

Verified: codex-cli 0.160.0 binary contains /goal, ThreadGoalUpdatedEvent and a request_user_input tool, so the feature exists. The 'does not block when unanswered' behavior is the creator's observation and is not verified locally.

## Related

[[tell-astra-to-make-reasonable-assumptions-claude-needs-the-opposite]], [[goal-verifiable-finish-lines-with-safety-caps]]
