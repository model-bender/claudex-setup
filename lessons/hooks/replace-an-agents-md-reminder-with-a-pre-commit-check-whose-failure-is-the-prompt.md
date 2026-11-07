---
id: replace-an-agents-md-reminder-with-a-pre-commit-check-whose-failure-is-the-prompt
created: 2026-10-19
status: active
supersedes: null
category: hooks
tool: [claude-code, codex]
source_type: post
sources:
  - https://ghuntley.com/agency/
---

# Replace an AGENTS.md Reminder With a Pre-Commit Check Whose Failure Message Tells the Agent What to Do

## TL;DR

When an agent keeps bypassing a house library or pattern, add a git pre-commit check on the diff that fails the commit with a message naming the right module, rather than rewording the instructions file again.

## Why it matters

Huntley says editing AGENTS.md still leaves a gap that drifts, while a failing check corrects the agent on every violation. His rule in the same post: if you have to correct the same thing three times, automate it.

## How to apply

Write a pre-commit script that greps the staged diff for the forbidden direct calls and exits non-zero with a message that names the approved module; the agent reads the failure and retries. Checked: plain git hook, no Claude Code or Codex setting named.

> "Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library.", Geoffrey Huntley

