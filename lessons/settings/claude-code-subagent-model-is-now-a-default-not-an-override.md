---
id: claude-code-subagent-model-is-now-a-default-not-an-override
created: 2026-08-29
status: active
supersedes: null
category: settings
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# CLAUDE_CODE_SUBAGENT_MODEL Is Now Only a Default: an Agent's model: Frontmatter Beats It

## TL;DR

As of 2.1.251, `CLAUDE_CODE_SUBAGENT_MODEL` no longer forces every subagent onto one model; it only sets the default, and any agent definition's `model:` line or explicit per-spawn model quietly wins.

## Why it matters

The old behaviour was a hard override, so a single env var was a reliable spend ceiling for fan-outs. Now any agent file carrying `model: opus` silently escapes the cap, and the failure is invisible until you read the bill: nothing errors, the subagent just runs on the pricier model.

## How to apply

Keep `CLAUDE_CODE_SUBAGENT_MODEL` as the default, then audit `.claude/agents/*.md` for `model:` lines and remove the ones you did not intend as deliberate exceptions. Verify per-subagent with `/tasks`, which since 2.1.243 shows the model (and effort level) each subagent ran on.

> "Changed `CLAUDE_CODE_SUBAGENT_MODEL` to set the default subagent model rather than override everything: an agent definition's `model:` and an explicit per-spawn model now take precedence over it", Claude Code CHANGELOG 2.1.251

## Related

[[let-model-self-select-subagent-model-then-freeze-routing-table]]
