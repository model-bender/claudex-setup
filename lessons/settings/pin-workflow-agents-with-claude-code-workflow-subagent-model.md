---
id: pin-workflow-agents-with-claude-code-workflow-subagent-model
created: 2026-10-11
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Pin Every Workflow Agent to One Model With CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL

## TL;DR

Since 2.1.296 `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` runs every workflow agent on one model while other subagents keep theirs.

## Why it matters

Workflow fan-outs can launch many agents; this caps their model in one place without touching ordinary subagents.

## How to apply

Set `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL=<model id>` in the settings `env` block or shell before a workflow run. Checked: the variable has 8 hits in the 2.1.296 binary. Whether it overrides a `model:` set in an agent file used by the workflow was not confirmed.

> "Added `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` to run every workflow agent on one model while other subagents keep theirs", Claude Code CHANGELOG 2.1.296

## Related

[[claude-code-subagent-model-is-now-a-default-not-an-override]]
