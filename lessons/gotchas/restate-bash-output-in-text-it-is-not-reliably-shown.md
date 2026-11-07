---
id: restate-bash-output-in-text-it-is-not-reliably-shown
created: 2026-08-07
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Restate Command Output in Your Reply, Because the Bash Tool Block Is Not Reliably Shown

## TL;DR

Anthropic now tells the model outright that Bash output is displayed to the model, not reliably to the user. Anything the user needs to see, restate in the response text rather than pointing at the tool block.

## Why it matters

The output can look delivered in your own transcript view while never reaching the user in headless runs, SDK hosts, and some terminals. An agent that runs the tests and stops, assuming the pass/fail was visible, has silently reported nothing. This is also why "the tests pass" without the output pasted is a weaker claim than it looks.

## How to apply

When a command produces something the user needs (test results, a diff, a fetched value, an error), quote the relevant part in your own text. Write instructions and skills on the assumption that only your prose is guaranteed to land.

> "Changed the Bash tool description to always note that command output is displayed to the model, not reliably to the user", Claude Code CHANGELOG 2.1.224

## Related

[[design-agent-output-for-verifiability-before-building-evals]]
