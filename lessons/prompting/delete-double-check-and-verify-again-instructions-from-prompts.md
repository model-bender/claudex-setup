---
id: delete-double-check-and-verify-again-instructions-from-prompts
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# Delete 'Double-Check' and 'Use a Subagent to Verify' Lines From Prompts Written for Older Models

## TL;DR

Claude 5 models already check their own work, so a standing double-check or verify-with-a-subagent instruction buys a second pass over work that was already verified, at full cost.

## Why it matters

The Opus 5 guide states the model checks its own work; the ritual survives in old prompts because early 2026 guides told everyone to add it. Simon found 11 instances of this class of line in his own files. Unlike a formatting preference, this one has a measurable price: every redundant verification pass is tokens and latency for no change in the answer.

## How to apply

Grep your prompts, skills and CLAUDE.md for 'double check', 'verify before finishing', 'check your work' and 'use a subagent to verify', and remove the ones that duplicate the model's default self-check. Keep verification that is genuinely external (run the tests, hit the endpoint, diff against the spreadsheet), which is evidence rather than another pass of the same reasoning.

## Related

[[keep-the-context-half-of-a-skill-delete-the-procedure-half]], [[claude-api-prompt-audit-finds-old-model-prompt-patterns]], [[reasoning-extraction-phrasing-can-silently-reroute-model]]
