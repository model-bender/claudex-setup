---
id: summarize-recent-commits-to-rebuild-context
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/andrew-codesmith/master-95-of-claude-code-in-15-mins-as-a-beginner_20260424.txt
---

# Ask Claude to 'Summarize Recent Commits' to Rebuild Context When You Return to a Project

## TL;DR

Instead of writing manual session notes, treat your git log as a diary: when you come back to a project, ask Claude to summarize recent commits to reconstruct what happened.

## Why it matters

The creator frames this explicitly: 'your git commits are like diary entries for your project. Claude is someone who reads your diary to catch up. So when you return to the project, just ask, summarize recent commits.' This works best when commit messages are detailed and AI-generated, since terse manual commits give the summarizer little to work with.

## How to apply

Let Claude write your commit messages so they carry real detail, then on a fresh session for a returning project, prompt 'run git log and summarize the recent commits so I'm caught up' before asking for new work.

## Related

[[git-backed-issue-tracker-as-agent-cross-session-memory]]
