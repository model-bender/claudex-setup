---
id: todo-and-task-tools-removed-on-modern-models
created: 2026-08-16
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` or Your Task-Tracking Workflow Silently Disappears

## TL;DR

The whole todo/task tool family (`TaskCreate`/`TaskGet`/`TaskUpdate`/`TaskList`, `TodoWrite`) was removed from every current model in 2.1.233, so any skill, command, CLAUDE.md rule, or cross-session `.claude/tasks/` pipeline that depends on it now does nothing unless you opt back in.

## Why it matters

This is the widest blast radius in the 2.1.225-2.1.233 window. A CLAUDE.md line like "track progress with TodoWrite", or a multi-session workflow keyed on `CLAUDE_CODE_TASK_LIST_ID`, now references tools that are not there - with no warning and no error. The instruction simply becomes a no-op, and the coordination it was buying you quietly stops.

It also retires the dependency-tracking workflow this lesson supersedes: `blocks`/`blocked_by` task graphs in `.claude/tasks/` and real-time sibling-session notification via a shared `CLAUDE_CODE_TASK_LIST_ID` are opt-in features now, not defaults.

## How to apply

Grep `.claude/` and your CLAUDE.md files for `TodoWrite`, `TaskCreate`, `TaskUpdate`, `TaskList`, and `CLAUDE_CODE_TASK_LIST_ID`. Then either delete those references, or add `"CLAUDE_CODE_ENABLE_TODO_TOOLS": "1"` to the `env` block of `~/.claude/settings.json` to bring the tools back.

If you opt in, the old mechanics still hold: create with `TaskCreate`, set `in_progress`/`completed` with `TaskUpdate`, declare `{"blocks": [...], "blocked_by": [...]}`, and share a task list across sessions by setting the same `CLAUDE_CODE_TASK_LIST_ID`.

> "Todo/task-tracking tools (TaskCreate/Get/Update/List, TodoWrite) are no longer available on Opus 4.8, Sonnet 5, Fable 5, Mythos 5, and newer models; set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` to bring them back", Claude Code CHANGELOG 2.1.233

