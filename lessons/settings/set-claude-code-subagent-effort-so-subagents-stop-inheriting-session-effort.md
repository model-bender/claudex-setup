---
id: set-claude-code-subagent-effort-so-subagents-stop-inheriting-session-effort
created: 2026-11-06
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://www.reddit.com/r/ClaudeCode/comments/1xlgb5q/claude_code_21316_subagent_effort_is_now_its_own/
---

# Set CLAUDE_CODE_SUBAGENT_EFFORT So Subagents Stop Inheriting the Session's Effort

## TL;DR

Since 2.1.316, CLAUDE_CODE_SUBAGENT_EFFORT sets the effort level subagents run at when nothing else names one, so a session at high or xhigh no longer pays that rate for every grep-and-read subagent.

## Why it matters

Before, subagents inherited the session's effort, and the only workaround was a hook that rewrote effort per spawn. 2.1.317 also changed subagents on a different model from the main conversation to use that model's saved effort or its default instead of the session's.

## How to apply

Put CLAUDE_CODE_SUBAGENT_EFFORT=low or medium in your shell or the settings env block, keep the session itself at high, and check that a spawned subagent reports the lower level. An explicit effort on the Agent tool call still wins.

Checked: claude 2.1.318 binary (command grep -c -a): CLAUDE_CODE_SUBAGENT_EFFORT 8 hits, in the env-var registry beside CLAUDE_CODE_SUBAGENT_MODEL.

> "2.1.316: Added `CLAUDE_CODE_SUBAGENT_EFFORT` to set the effort level subagents run at when nothing else names one, instead of inheriting the session's", Claude Code CHANGELOG 2.1.316

## Related

[[set-a-subagent-effort-level-through-the-agent-tool]]
