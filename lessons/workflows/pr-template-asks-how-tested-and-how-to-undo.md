---
id: pr-template-asks-how-tested-and-how-to-undo
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Put 'how was this tested' and 'how to undo it' in the PR template, filled by Claude, signed off by a person

## TL;DR

Make the PR template ask for the test evidence and the revert path. Let the agent fill it in, and have the person who asked for the change sign off.

## Why it matters

The team invests heavily in making mistakes fast and easy to undo, and holds whoever prompted a change accountable for it. A stated revert path per PR serves the first and the human sign-off serves the second (linking each section to those aims is this lesson's inference).

## How to apply

Add testing, risk and how-to-revert sections to the PR template (the article's adoption list names all three) and instruct the agent to fill them when it opens a PR.

Checked: No mechanism named.

## Related

[[give-pr-writing-agents-a-template-to-cap-summary-length]]
