---
id: default-safe-permission-allowlist-starter-set
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-claude-code-concept-explained-for-normal-people_20260307.txt
---

# Start Your Permission Allowlist With Reads, Tests, Dev Server, and Git; Gate Installs, Deletes, and Network Calls

## TL;DR

A practical default settings.json allowlist pre-approves file reads, running the dev server, running tests, and git operations, while keeping package installs, file/folder deletions, and anything touching the network gated behind manual approval.

## Why it matters

Approving every action every ten seconds kills flow on a long session, but going straight to --dangerously-skip-permissions removes all safety; this split is the practical middle ground the video recommends staying short of full bypass.

## How to apply

In settings.json, add an allow list for reading files/folders, starting the dev server, running tests, and git commit/push operations. Leave installing new packages, deleting files or folders, and any API/network calls off the allow list so Claude still asks first.

