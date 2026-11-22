---
id: ultrareview-multi-agent-verification-pattern
created: 2026-04-25
status: active
supersedes: null
category: workflows
sources:
  - transcripts/ray-amjad/claude-code-ultrareview-is-here-what-you-need-to-know_20260424.txt
---

# Use a Multi-Agent Verify Step to Eliminate False Positive Bug Reports

## TL;DR

Spin up 5 bug-hunting subagents from different starting points, then run an independent verifier to confirm real bugs before acting.

## Why it matters

Single-pass code review tools flag many false positives, Claude sees something that deviates from patterns and calls it a bug when it isn't. Ultrareview (and custom fleet review skills) address this with a separate verification phase where an independent subagent (or Codex in parallel) confirms or refutes each finding. This prevents Claude from making unnecessary changes to non-bugs.

## How to apply

Build a fleet review skill: spawn 3-5 Claude Code subagents to find bugs each starting at a different position in the diff. Pass results through a verification step using a separate Claude subagent and a Codex verifier in parallel. Where Claude says a bug exists and Codex refutes it (or vice versa), flag for human review. Use `/code-review ultra <PR-number>` when available (`/ultrareview` is an alias), it runs 5 finding subagents + 1 verifier + dedup stage on the cloud. For large PRs (>5000 lines), ultrareview is worth the 5 to 15 minute wait; for small PRs, `/review` is sufficient.

Corrected in place on 2026-11-22: the command was spelled `/ultra review` and the wait given as 10 to 20 minutes.

Checked: Live docs https://code.claude.com/docs/en/ultrareview.md fetched 2026-11-22 with curl, Claude Code 2.1.330 installed: 'The command is `/code-review ultra`. When ultrareview is available to your account, `/ultrareview` is an alias.' and 'A review typically takes 5 to 15 minutes.' https://code.claude.com/docs/en/commands.md lists `/review` as an alias of `/code-review`.
