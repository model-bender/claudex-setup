---
id: pass-trust-to-codex-exec-and-review-in-untrusted-checkouts
created: 2026-11-15
status: active
supersedes: null
category: gotchas
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/releases/tag/rust-v0.169.0
---

# Pass --trust to codex exec and codex review in scripts, or project config and MCP servers silently stay off in untrusted directories

## TL;DR

Headless Codex runs in a directory you have not trusted ignore the repo's config and MCP servers, and --sandbox workspace-write does not change that; --trust saves trust for that project.

## Why it matters

A scripted or CI Codex run in a fresh checkout loses project config and MCP tools with no obvious error, so the failure looks like a prompt problem.

## How to apply

Add --trust only for repos you vet (it persists, even with --ephemeral, and does not override an explicitly untrusted project), or run `codex` once interactively and answer the trust prompt.

Checked: `codex exec --help` on 0.169.0 lists `--trust`, described as "Save trust for this project and future chats, including MCP commands outside the sandbox."

> "`codex exec` keeps project configuration and MCP servers disabled in untrusted directories, even with `--sandbox workspace-write`. Use `--trust` with `codex exec` or `codex review` to explicitly save project trust.", Codex release notes 0.169.0

## Related

[[codex-untrusted-projects-no-longer-load-agents-md]], [[codex-directory-trust-switches-on-project-local-hooks]]
