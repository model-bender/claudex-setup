---
id: worktree-terminal-close-auto-cleans-or-asks
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-workflow-explained-u0026-when-to-use-each_20260424.txt
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
---

# Closing a Worktree's Terminal Window Auto-Removes It, or Asks First if Work Would Be Lost

## TL;DR

When you close the terminal window of a claude -w worktree session, Claude Code checks for changes: if nothing changed it deletes the worktree automatically, but if there's work to keep it asks you what to do before removing it.

When you exit a worktree-isolated session, including one a subagent was using, Claude Code automatically decides whether to remove the worktree based on whether anything actually changed in it.

## Why it matters

The transcript calls this out as 'the nice touch about closing a work tree session... Claude is going to handle the cleanup for us', which removes the manual git worktree remove step people otherwise assume is required.

You don't need to manually track and delete scratch worktrees; unused ones are cleaned up for you whether you made the worktree yourself or a subagent did.

## How to apply

Just close the terminal window for a claude -w session when you're done; don't manually run git worktree remove first. Check the project's worktree list afterward to confirm cleanup, or answer Claude's prompt if it asks about uncommitted work.

Exit the worktree session normally, or let the subagent finish. If nothing changed, Claude Code removes the worktree; if changes exist, it leaves it in place for you to review or merge.

## Related

[[worktrees-for-parallel-independent-tasks]]
