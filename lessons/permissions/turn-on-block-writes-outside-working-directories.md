---
id: turn-on-block-writes-outside-working-directories
created: 2026-11-06
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://www.reddit.com/r/ClaudeCode/comments/1xlgb5q/claude_code_21316_subagent_effort_is_now_its_own/
---

# Turn On permissions.blockWritesOutsideWorkingDirectories So Write and Edit Refuse Outside Paths in Every Mode

## TL;DR

Since 2.1.314 one setting makes Write, Edit and NotebookEdit refuse any path outside the working directories, in every permission mode, auto and bypass included.

## Why it matters

Before this, an accept-edits, auto or bypass session could write anywhere on disk, and containment depended on the mode you happened to be in. The settings docs say the key is honored as true from any scope, even when a managed source sets false.

## How to apply

Add "permissions": {"blockWritesOutsideWorkingDirectories": true} to settings.json for unattended or auto-mode work, list extra roots in additionalDirectories so legitimate writes are not refused, and confirm an edit above the project root is refused. It covers the file tools, not Bash.

Checked: claude 2.1.318 binary: blockWritesOutsideWorkingDirectories 22 hits; docs at code.claude.com/docs/en/settings say it requires v2.1.314 or later. That Bash is not covered follows from the CHANGELOG naming only the three file tools.

> "2.1.314: Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode", Claude Code CHANGELOG 2.1.314

## Related

[[tee-no-longer-bypasses-edit-deny-rules]]
