---
id: grow-the-eval-answer-key-one-row-per-agent-failure-seeded-from-real-questions
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/how-to-build-self-improving-ai-agents-with-claude-stanford-s-method_UUg5oij7ptw_20261122.txt
---

# Keep the Eval Answer Key as a Living Table: Seed It From Real Questions With Your Real Answers, Add a Row for Every Failure

## TL;DR

For a non-code agent, build an input-to-ideal-output table from real past questions and your actual answers, review it by hand, and add a row each time the agent gets something wrong.

## Why it matters

Code has pass or fail tests, but knowledge work needs a source of truth. The transcript uses the table as the grading basis for every future change to the agent.

## How to apply

1. Have Claude pull the 20 most common questions you were asked (Austin uses Slack) with the exact answers you gave. 2. Review each row manually so the answer is how you would actually answer. 3. Save as answer-key.md. 4. Whenever the agent lets you down, add the case as a new row.

Checked: No mechanism claim (a workflow). Slack source is the transcript's own example, not verified here.

## Related

[[turn-every-incident-and-revert-into-a-daily-eval-case-for-your-ai-reviewer]]
