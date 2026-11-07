---
id: a-project-mcp-json-headershelper-now-needs-folder-trust-and
created: 2026-08-22
status: active
supersedes: null
category: mcp
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# A Project .mcp.json headersHelper Now Needs Folder Trust and Gets No Inherited Credential Env Vars

## TL;DR

Project/plugin/agent-scoped MCP headersHelper commands no longer inherit your credential environment variables and now require the folder's trust dialog to have been accepted, including under `claude -p`.

## Why it matters

A headersHelper that minted an auth header by reading `$SOME_API_TOKEN` from the environment will now come back empty, and the failure surfaces as an MCP auth error rather than a config error. The same release also gated these behind trust: "MCP `headersHelper` in a project `.mcp.json`, and inline MCP servers in project or `--add-dir` agent files, now require that folder's trust dialog to have been accepted (also under `claude -p`)", so headless runs in an untrusted directory silently lose those servers.

## How to apply

Move the helper to user or managed scope, or have it read the secret itself (keychain, file, `gh auth token`) instead of relying on inherited env; for `claude -p` automation, accept the folder trust dialog once interactively first.

> "MCP `headersHelper` from a project `.mcp.json`, plugin, or agent file runs without inherited credential env vars; user, managed and claude.ai-scope helpers now run from the Claude config dir", canonical: Claude Code CHANGELOG 2.1.238
