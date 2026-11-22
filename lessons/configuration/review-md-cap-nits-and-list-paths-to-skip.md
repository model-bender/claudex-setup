---
id: review-md-cap-nits-and-list-paths-to-skip
created: 2026-11-22
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# In REVIEW.md, cap the nits and list the paths to skip

## TL;DR

Tell the reviewer a maximum number of nits per review and which paths it should not comment on.

## Why it matters

The article lists both as traits of the good REVIEW.md files. It also notes that noise costs more when the author is an agent: a person waves off a nit in a second, while an agent fixes it, which means another commit and another round of review.

## How to apply

In `REVIEW.md`: 'Report at most five Nits per review' and a 'Do not report' list (generated code, lockfiles, anything CI already enforces). Per the docs these two instructions are honoured only from the root file on a protected default branch.

Checked: Code-review-customize.md (live docs at code.claude.com fetched 2026-11-22): nit cap and exclusions documented, honoured from the root REVIEW.md on a protected default branch, and not accepted from an included skill file. REVIEW.md is read only by the managed Code Review service (Team and Enterprise plans), not by local `/code-review`.

## Related

[[code-review-max-findings-is-sticky-reset-it-with-default]]
