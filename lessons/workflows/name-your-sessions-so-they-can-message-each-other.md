---
id: name-your-sessions-so-they-can-message-each-other
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
  - https://x.com/adocomplete/status/2087728817012162973
---

# Name Your Sessions With `--name` So They Can Message Each Other

## TL;DR

Launch each long-lived terminal session with `claude --name <role>`, then hand a fact from one to another in plain English - or type `@` to mention a session by name - instead of re-pasting context or spawning a subagent.

## Why it matters

Multi-session work normally means *you* act as the message bus between terminals, copying an API change from the backend window into the frontend window. Naming makes sessions addressable, so a cross-session fact costs one sentence.

It is also a lighter primitive than agent teams for the common case of two long-lived sessions on the same repo: no team setup, no coordinator, no worktrees. 2.1.232 made this practical - `@` mentions route through `SendMessage`, a bare name that matches exactly one live session now delivers without a ref confirmation, and same-named sessions on one machine get auto-uniquified so the address stays unambiguous.

## How to apply

```
claude --name backend
claude --name frontend
```

Then from the backend session: `tell frontend the orders endpoint moved to /v2`. Use `/rename <name>` for an already-running session, and `ListAgents` to see what is reachable. `/config` carries rows for "Dialog expiry" and "Messages from your other sessions" (accept / hold / refuse) to control inbound.

> "Type `@` in the prompt to mention another Claude session by name; Claude then uses `SendMessage` to reach that session directly", Claude Code CHANGELOG 2.1.232

> "Your sessions have names and can DM each other in Claude Code.", @adocomplete

## Related

[[wrap-your-terminal-cli-in-a-skill-so-claude-code-spawns-peer-sessions]], [[peer-session-invisible-check-remote-control-and-version-skew]], [[cross-session-sendmessage-spans-machines-but-holds-for-approval]]
