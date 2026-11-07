---
id: rereview-only-the-new-diff-and-flag-the-whole-bug-class
created: 2026-11-06
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# After the First Review Rounds, Re-Review Only the New Diff and Make Findings Name the Bug Class

## TL;DR

The Claude Code team's review loop re-reviews only the new diff after the first few passes, never repeats findings already posted, and flags the class of bug so the author fixes every instance, not one line.

## Why it matters

The article (read aloud by John Kim) reports that repeated full passes keep finding old code, not new bugs. These rules are part of how the team makes review converge.

## How to apply

1. Run a full review for the first few rounds.
2. From then on, review only commits added since the last round.
3. Suppress findings already posted.
4. Word each finding as a class of bug so the fix covers all instances.

Checked: claude 2.1.318: /code-review 30 hits and /security-review 5 hits in the binary (command grep -c -a); the diff-only and class-of-bug rules are the team's internal process, not named settings.

Inference, not from the source: How to implement the rules in a REVIEW.md or review prompt is the lesson's; the article only lists them as what the team does.

## Related

[[fix-a-recurring-review-finding-at-its-source-not-per-pr]]
