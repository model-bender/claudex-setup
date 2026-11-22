---
id: review-md-states-what-failure-looks-like-in-this-repo
created: 2026-11-22
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Write REVIEW.md as a short statement of what failure looks like in this repo

## TL;DR

A good REVIEW.md is short and names the repo's failure mode: for a docs repo 'it lies', for a config repo 'it misroutes'.

## Why it matters

Per the docs, the default reviewer calibration targets production code. Naming the failure that matters for this repo is what points the reviewer at the right class of bug.

## How to apply

Add `REVIEW.md` at the repository root, written by the code owners, opening with what an Important finding means here (the docs call this redefining Important for a docs, config or prototype repo).

Checked: `REVIEW.md` has 13 string hits in the Claude Code 2.1.330 binary; code-review-customize.md and code-review.md (live docs at code.claude.com fetched 2026-11-22) document it as a root file read by the managed Code Review service, which is for Team and Enterprise plans on GitHub. The local `/code-review` command does not read it.

## Related

[[fix-a-recurring-review-finding-at-its-source-not-per-pr]]
