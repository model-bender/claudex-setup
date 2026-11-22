---
id: leave-review-feedback-as-comments-in-a-tool-the-agent-can-read
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/john-kim/how-i-fully-automated-my-video-editing-claude-code-fable-5-2_-EvDMZycpI0_20261120.txt
---

# Leave review feedback as comments in a tool the agent can read, then tell it to apply them all

## TL;DR

Put your feedback on agent output where the agent can fetch it (timestamped comments in a review tool with an MCP or CLI), then give one instruction: read every comment and update the work.

## Why it matters

The creator reviews raw cuts and motion graphics by leaving comments in Frame.io or as markers in his editor, then tells Claude Code to read the comments and update the edit. He calls this context engineering: bringing the context to where the work happens, instead of retyping feedback into the chat. He says it also lets him review from a phone.

## How to apply

1. Pick a review surface the agent can read through an MCP or CLI (he uses Frame.io, and an open-source editor with a CLI). 2. Leave one comment per issue at the exact spot, for example 'this is covering my face, remove it'. 3. Prompt: 'go and look at all of the comments I left and then update the edit'.

Checked: No mechanism named (third-party tools Frame.io and the editor were not checked).

## Related

[[batch-claude-design-comments-and-drawings-then-send-once]], [[bound-pr-monitoring-window]]
