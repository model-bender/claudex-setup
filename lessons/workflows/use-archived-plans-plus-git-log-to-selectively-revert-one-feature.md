---
id: use-archived-plans-plus-git-log-to-selectively-revert-one-feature
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-top-0-01-user-s-guide-to-claude-code_20260307.txt
---

# Combine an Archived Plan File With Git History to Cleanly Undo One Past Feature

## TL;DR

When you no longer want a feature you added several commits ago but want to keep everything shipped after it, find that feature's saved plan file, hand it to Claude Code with the git commit history, and ask it to undo just that feature.

## Why it matters

A plain git revert of the original commit would also destroy the unrelated features layered on top of it. The archived plan gives Claude Code the intent and scope of the original change so it can remove exactly that, and nothing else.

## How to apply

Keep every plan Claude Code produces in a project plans folder. To remove a stale feature, tell Claude Code: 'find the plan where we implemented that particular thing, also use the git commit history as reference, and undo that particular feature change,' rather than reverting the commit directly.

## Related

[[plan-file-persistence-in-project-folders]]
