---
id: start-a-new-conversation-instead-of-resuming-a-cold-one-on-pro-or-max
created: 2026-10-25
status: active
supersedes: null
category: context-management
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21304
---

# When Claude Code Warns That Resuming Will Cost a Share of Your 5-Hour Limit, Start a New Conversation

## TL;DR

Since 2.1.304, on Pro and Max, resuming an inactive conversation that would use a noticeable share of the 5-hour limit shows a warning; the alternative it offers is a new conversation in which Claude can look up the previous one when you refer to it.

## Why it matters

Resuming a long idle session re-reads it without the prompt cache, which is the cost the warning is about.

## How to apply

When the warning appears and you do not need the full history in context, choose the new conversation and name the earlier session or its topic so Claude can look it up.

> "Added a warning on Pro and Max plans when resuming an inactive conversation would use a noticeable share of your 5-hour usage limit: resume anyway, or start a new conversation and Claude can look up the previous one if you refer to it", Claude Code CHANGELOG 2.1.304

## Related

[[accept-the-resume-from-summary-offer-on-stale-sessions]]
