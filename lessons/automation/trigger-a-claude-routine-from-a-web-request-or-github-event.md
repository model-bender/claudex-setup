---
id: trigger-a-claude-routine-from-a-web-request-or-github-event
created: 2026-10-19
status: active
supersedes: null
category: automation
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-changed-completely-every-new-concept-explained_YAuWBqZ_gjs_20261018.txt
---

# Trigger a Claude Routine From an API Call or a GitHub Event Instead of a Timer

## TL;DR

A cloud routine is not limited to a schedule: it can start from a web request (you get a URL and token) or a GitHub event such as a new pull request, so any tool that can send a request can wake an agent.

## Why it matters

Simon Scrapes says scheduled tasks in the chat window are all time based, while routines can be event based, which makes the agent reactive. He notes OpenAI is moving the same way with MCP events.

## How to apply

1. Create a routine with a name, a prompt, the repo it works in, and a trigger. 2. Pick API as the trigger, save, and keep the URL and token it gives you; anything that POSTs to that URL starts a fresh cloud run. 3. Or pick a GitHub event trigger such as a new PR. 4. Strip the connectors back to the ones the job needs, since every connected connector is included by default. Checked: not verified against the binary; the binary only confirms that routines can use claude.ai connectors and not locally added MCP servers. The trigger types and URL/token flow are the speaker's description of the claude.ai UI.

## Related

[[strip-default-connectors-when-creating-a-routine]], [[trigger-scheduled-tasks-from-app-events-not-timers]], [[managed-agents-for-webhook-triggered-automation]]
