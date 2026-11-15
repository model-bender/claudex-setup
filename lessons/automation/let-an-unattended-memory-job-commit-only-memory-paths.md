---
id: let-an-unattended-memory-job-commit-only-memory-paths
created: 2026-11-15
status: active
supersedes: null
category: automation
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xqdxdp/borrowed_anthropics_dreaming_idea_to_stop/
---

# Let an unattended memory job touch only memory files: revert everything else in git status before it commits

## TL;DR

The poster runs an hourly headless `claude -p` job that rewrites CLAUDE.md and memory notes from past transcripts. It runs in a worktree on its own branch, and before committing it reverts every path outside an allowlist. A job that decides to "helpfully" fix a bug can never land a code change; it logs the bug instead.

## Why it matters

Restricting tools still leaves Edit able to change any file. The post-run diff check holds no matter what the model decided, and the branch keeps every change reviewable as a diff.

## How to apply

After the run, read `git status --porcelain` and revert anything not under the allowed paths. Then commit, and have the job write bugs it noticed to its log.

Checked: `claude --help` on 2.1.325 lists `--add-dir`, `--model`, `--allowedTools` and `--append-system-prompt`; the post does not say which flag limited the tools.

> "Before it commits, a guardrail checks git status and reverts anything outside CLAUDE.md, DREAM\_LOG.md and docs/memory/. It's never allowed to touch code, even if it spots a bug. It notes the bug in the log instead.", u/Sweet-Helicopter2769 on r/ClaudeCode

## Related

[[auto-dream-memory-consolidation]]
