---
id: sandbox-mounts-break-git-add-dot-and-fake-untracked-files
created: 2026-08-16
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/78419
---

# With the Sandbox On, `git add .` Fails Outright and `git status` Shows Phantom Files

## TL;DR

Sandbox mode mounts `/dev/null` over protected paths that are absent from the project root (`.zshrc`, `.mcp.json`, `.claude/hooks`, and others), which aborts `git add .` with exit 128 and leaves roughly 19 phantom untracked entries in `git status` that the model cannot tell apart from real repo state.

## Why it matters

Two failures compound. The staging step silently stages **nothing** - it does not skip the stubs, it aborts and takes the legitimate files with it - so a commit step in an unattended loop produces an empty commit or none at all. And the agent reasons about sandbox artifacts as though they were real working-tree changes, chasing files that do not exist.

Neither is documented and neither surfaces a signal the agent can act on. The underlying mount mechanism has been open in `anthropic-experimental/sandbox-runtime#139` since February.

## How to apply

In sandboxed sessions, have Claude stage with explicit paths or `git add -u`, never `git add .`. Add a CLAUDE.md line naming the stub paths so a phantom `git status` entry is recognised as a sandbox artifact rather than investigated as real state.

> "**`git add .` fails outright inside the sandbox** — it doesn't skip the stubs, it aborts with exit 128 and stages nothing, including legitimate files.", anthropics/claude-code issue #78419

## Related

[[sandbox-mode-for-safe-exploration]], [[sandbox-deny-entries-with-a-trailing-slash-were-bypassable]]
