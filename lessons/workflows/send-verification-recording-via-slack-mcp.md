---
id: send-verification-recording-via-slack-mcp
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/ray-amjad/the-4-levels-of-agentic-coding-how-to-ship-like-boris-cherny_XLA-sTSJ-Wc_20260719.txt
---

# Send End-to-End Verification Recordings via a Slack MCP Server, Not Just an Attached File

## TL;DR

After a sub-agent finishes Playwright/Chrome-based end-to-end verification, have it push the recording straight to you on Slack through a Slack MCP server rather than only leaving it as a PR attachment.

## Why it matters

The presenter's rule is: 'once the verification is done, send me a recording on Slack using the MCP server.' This closes the loop for someone managing many parallel agent sessions who wants to review outcomes without opening each session or PR.

## How to apply

Wire up a Slack MCP server, then add to your verification step: 'once verification is complete, send the recording/screenshot to me on Slack via the MCP server,' in addition to (or instead of) attaching it to the PR.

## Related

[[make-video-proof-mandatory-for-ui-changing-prs]]
