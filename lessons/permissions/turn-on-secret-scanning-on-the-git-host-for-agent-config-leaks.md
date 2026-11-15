---
id: turn-on-secret-scanning-on-the-git-host-for-agent-config-leaks
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: [claude-code, codex]
source_type: canonical
sources:
  - https://news.ycombinator.com/item?id=50408126
---

# Turn On Secret Scanning on Your Git Host: Agent Config Files Leak Secrets Whatever the Agent

## TL;DR

Boris Cherny of the Claude Code team says every team should run secret scanning whatever agent it uses; a scan had found 1,122 public GitHub repositories with committed settings.local.json files holding passwords and keys.

## Why it matters

Agents save approved commands and config into files that are easy to commit by accident on another machine or a fresh clone. A host-side scan catches the leak whichever file or agent caused it, while ignore rules only cover the paths you thought of.

## How to apply

Enable the git host's secret scanning on every repo agents commit to, and (inference) push protection where the host offers it, so a credential in an allow rule or config file is blocked or flagged on push.

> "Regardless of what agent you use, you should have secret scanning enabled.", Boris Cherny (Claude Code team) on Hacker News

## Related

[[gitignore-claude-settings-local-json-in-each-repo]]
