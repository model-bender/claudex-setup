---
id: parallel-sessions-in-one-directory-share-a-prompt-cache
created: 2026-10-02
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/prompt-caching
---

# Run parallel sessions in the same directory to share a prompt cache, and expect a miss from a different directory

## TL;DR

The cache is effectively per machine and directory, because the system prompt embeds memory paths and the conversation opens with the working directory.

## Why it matters

Fan-out sessions started from different folders or worktrees each pay a cold first turn. Sequential sessions only share cache if git status is unchanged.

## How to apply

Start parallel sessions from one directory when cost matters, and do not expect a new session in another directory (or after a commit) to reuse the old cache. Check the `Prompt cache (main)` line in `/usage`.

Verified: Read live docs prompt-caching.md ("Cache scope" section). `command grep -c -a -F "Prompt cache (main)"` on 2.1.287 = 2. Library search for cache + same/different directory found nothing; verify-cache-folklore-with-the-cost-prompt-cache-line covers only the usage line.

> "Sessions you run in parallel in the same directory build matching prefixes and read each other's cache. Sequential sessions share the prefix only when the git status snapshot taken at startup matches, since each conversation also carries the branch and recent commits from that snapshot.", Claude Code docs (prompt caching)
