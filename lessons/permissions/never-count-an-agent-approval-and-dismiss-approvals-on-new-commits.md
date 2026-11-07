---
id: never-count-an-agent-approval-and-dismiss-approvals-on-new-commits
created: 2026-11-06
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/john-kim/how-anthropic-engineers-review-ai-code_4m8mq42M_3E_20261103.txt
---

# Never Let a Bot Approval Fill a Required Human Review Slot, and Dismiss Approvals When New Commits Land

## TL;DR

The Claude Code team's rules: an agent's approval never counts as a person's, the person directing the agent counts as one of the required reviewers and is on the hook for the change, and an approval covers one commit, so new commits the system cannot vouch for need approval again.

## Why it matters

The article states these rules in its risk-based approval section, and its adoption checklist adds: use code owners and branch protection so auth, billing, CI, release workflows and installers always need a person, and keep the lighter approval path for authors you trust.

## How to apply

1. Use CODEOWNERS and branch protection for sensitive paths.
2. Do not allow a bot approval to satisfy the human requirement.
3. Turn on dismissal of stale approvals when new commits are pushed.
4. Count the person directing the agent as one of the required reviewers.

Inference, not from the source: Mapping 'dismiss approvals on new commits' to GitHub's 'Dismiss stale pull request approvals' setting is the lesson's; the speaker did not name it.

