---
id: set-claude-code-disable-ultrathink-when-the-word-is-in-your-prompts
created: 2026-11-06
status: active
supersedes: null
category: settings
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xlgb5q/claude_code_21316_subagent_effort_is_now_its_own/
---

# Set CLAUDE_CODE_DISABLE_ULTRATHINK When the Word Appears in Your Own Prompts or Rule Files

## TL;DR

2.1.316 added CLAUDE_CODE_DISABLE_ULTRATHINK, a kill switch for the ultrathink keyword, so prose that merely mentions the word stops raising the turn's effort.

## Why it matters

The keyword is matched in the prompt text, so a command file, a pasted transcript or a lesson that discusses ultrathink silently buys xhigh effort on turns that did not need it.

## How to apply

Set CLAUDE_CODE_DISABLE_ULTRATHINK=1 for sessions and automations whose prompts quote the word, and leave it unset where you still want the one-turn bump.

Checked: claude 2.1.318 binary: CLAUDE_CODE_DISABLE_ULTRATHINK 7 hits; added in 2.1.316 per the CHANGELOG.

> "Useful if the word shows up in your prompts by accident and keeps bumping effort to xhigh.", u/emarkosov on r/ClaudeCode
