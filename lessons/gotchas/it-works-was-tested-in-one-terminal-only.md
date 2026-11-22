---
id: it-works-was-tested-in-one-terminal-only
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-another-andrej-karpathy-using-claude_bvGptCLDhyo_20261009.txt
---

# Treat 'it ran fine' as true only for the environment it ran in, and have a reviewer run it in the target one

## TL;DR

A script that passed when Claude tested it can still fail in the user's real environment. Have a reviewer predict where it breaks and run it that way.

## Why it matters

The demo script pulled YouTube comments and ran fine in Claude's test. The reviewer predicted it would crash on an emoji under a normal Windows terminal, ran it that way, and it crashed before writing any files.

## How to apply

In review, ask the agent to name the environments the code will actually run in (the user's terminal, OS, encoding), predict the failure, and run it there before accepting 'works'. Listing terminal, OS and encoding is this lesson's generalization of the single Windows-terminal case in the demo.

Checked: No mechanism named. The crash is the video's demo and was not reproduced.

## Related

[[add-a-stop-hook-that-blocks-finishing-when-code-was-written-but-not-run]]
