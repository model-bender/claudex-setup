---
id: push-commits-before-starting-a-cloud-session-the-session-starts-from-pushed-state
created: 2026-11-22
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/john-kim/anthropic-just-told-us-how-to-prompt-claude_3F75mndbrxg_20261120.txt
---

# Push Your Commits Before Starting a Cloud Session, and Read the Notice That Names Its Starting Point

## TL;DR

A cloud session works from a clone, so commits that exist only on your machine may be missing. Push first, and keep a session local when the task needs resources only your machine has.

## Why it matters

John Kim relays the article's advice that cloud sessions run in a separate VM with a fresh clone of your repo. Corrected against the docs: when the terminal uploads a bundle it can include uncommitted changes to tracked files, but when the session starts from GitHub, local-only commits are not in it.

## How to apply

1. Push the branch you want worked on. 2. Start with claude --cloud or from claude.ai/code. 3. If the session shows a line naming where it started (a pushed commit or the default branch), check it matches what you expect. 4. Keep the session local if it needs files or services only your machine has.

Checked: claude --help on 2.1.330 lists --cloud. Docs page code.claude.com/docs/en/claude-code-on-the-web: 'Commits that exist only on your machine and uncommitted changes aren't in the session' for the GitHub-start case, and a bundle upload may include uncommitted changes to tracked files. Returned corrected, not in the transcript's absolute wording.

## Related

[[start-a-cloud-session-from-the-terminal-with-claude-cloud-flag]]
