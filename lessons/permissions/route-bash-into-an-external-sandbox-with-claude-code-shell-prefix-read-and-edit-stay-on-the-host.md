---
id: route-bash-into-an-external-sandbox-with-claude-code-shell-prefix-read-and-edit-stay-on-the-host
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: post
sources:
  - https://blog.primeradiant.com/external-sandboxes-for-coding-agents/
---

# Route Claude Code's Bash commands into an external sandbox with CLAUDE_CODE_SHELL_PREFIX, and remember Read and Edit stay on the host

## TL;DR

Setting CLAUDE_CODE_SHELL_PREFIX (with CLAUDE_CODE_SHELL and CLAUDE_CODE_TMPDIR) makes every Bash tool command run through a prefix script that can forward it to a sandbox, but Read and Edit still touch the host.

## Why it matters

A shell prefix gives a sandbox that does not depend on model judgment for shell commands, with network and mounts you control. The mount rules do not cover Claude's native Read and Edit tools, so they do not make the whole agent safe.

## How to apply

Start a sandbox server, then launch claude with CLAUDE_CODE_SHELL_PREFIX pointing at a script that forwards the command, CLAUDE_CODE_SHELL=/bin/bash, and CLAUDE_CODE_TMPDIR set to a directory inside the writable mount. Deny Read and Edit outside the project separately.

Checked: CLAUDE_CODE_SHELL_PREFIX, CLAUDE_CODE_SHELL and CLAUDE_CODE_TMPDIR each present in the installed claude binary (grep -c -a counts 22, 30, 36); the post states the prefix behaviour ("When CLAUDE_CODE_SHELL_PREFIX is set, Claude's Bash tool runs every command with that as a prefix"). Behaviour itself not run.

> "Unlike the other agents, Claude Code's read and edit tools do not run via the sandbox.", Simon Willison, on the Prime Radiant blog
