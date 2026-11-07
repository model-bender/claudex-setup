---
id: give-pr-writing-agents-a-template-to-cap-summary-length
created: 2026-09-24
status: active
supersedes: null
category: prompting
tool: claude-code
about: codex
sources:
  - transcripts/john-kim/how-i-review-ai-code-meta-senior-staff-engineer_b2QkhmQ0sT0_20260923.txt
---

# Give agents a fixed PR template so the summary never outgrows the diff

## TL;DR

Left unguided, agents write PR summaries and test plans as long narrative prose. Give the review or PR-writing step a fixed template so every submission is consistent and the write-up stays shorter than the actual code change.

## Why it matters

John Kim calls an oversized summary his 'biggest pet peeve right now,' PRs where 'the summary and test plan is longer than the code changes itself,' and states plainly that without guidance the agent 'will write you like a giant paragraph, like a story.' A template is what forces consistency and proof-bearing content instead of narrative.

## How to apply

Add a PR/diff template (fixed headed sections, for example: summary, proof/test plan, confidence level) to your review skill, CLAUDE.md, or the prompt that produces the PR, and instruct the agent to conform to it rather than writing free-form prose. Verified: n/a, this is a prompting/template practice, not a named CLI flag or setting, so nothing to grep against the binary.

## Related

[[make-every-autonomous-pr-carry-its-own-proof]], [[read-the-agent-written-pr-description-before-you-make-anyone]]
