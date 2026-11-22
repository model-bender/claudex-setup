---
id: move-repeated-review-comments-into-review-md
created: 2026-11-22
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Move review comments you keep repeating into REVIEW.md

## TL;DR

When the same human review comment keeps coming up, write it into REVIEW.md so the automated reviewer checks it.

## Why it matters

It converts recurring human attention into an automated check, which is the article's whole aim.

## How to apply

Add the rule under an 'Always check' heading in the root `REVIEW.md` (for the managed service) or in CLAUDE.md (for local `/code-review`, which does not read REVIEW.md).

Checked: Code-review-customize.md and code-review-local.md (live docs at code.claude.com fetched 2026-11-22).

## Related

[[fix-a-recurring-review-finding-at-its-source-not-per-pr]], [[tag-claude-on-prs-to-update-claude-md]]
