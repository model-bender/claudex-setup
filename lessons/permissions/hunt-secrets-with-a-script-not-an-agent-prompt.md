---
id: hunt-secrets-with-a-script-not-an-agent-prompt
created: 2026-11-06
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xi0cma/asked_claude_code_to_find_every_secret_on_my/
---

# Hunt Secrets With a Script, Not an Agent Prompt: Deciding a String Is a Secret Means Reading It Into Context

## TL;DR

An agent asked to inventory secrets in a home folder found 63 and obeyed the no-printing rule, but had to read each candidate file to classify it, so the values went through the context window with no permission prompt.

## Why it matters

A CLAUDE.md line forbidding reads of .env is advice the model weighs, and reads inside the launch directory raise no prompt, so the rule gives the appearance of containment while the secrets still land in the transcript.

## How to apply

Have the agent write a deterministic scanner (grep patterns or an existing secret scanner) and read only its output, and put the real boundary in a deny-read permission rule before any such sweep.

> "which is why the "never read .env" line in CLAUDE.md doesn't really do much for me. it's a request, not a lock.", u/notomarsol on r/ClaudeCode

## Related

[[deny-read-secrets-with-a-wildcard-rule-wildcard-denies-only]]
