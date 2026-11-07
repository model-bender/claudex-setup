---
id: supermemory-container-tag-for-shared-team-memory
created: 2026-08-07
status: active
supersedes: null
category: memory
tool: claude-code
sources:
  - transcripts/simon-scrapes/this-setup-gives-your-team-the-same-claude-memory-steal-it_PzaC81yCJg0_20260807.txt
---

# Force a Shared Container Tag So a Team's Claude Sessions Write to One Memory

## TL;DR

supermemory.ai's Claude plugin can back a team-wide shared memory. Run its `/project-config` command inside a shared project folder to force every session into the same named container tag instead of the random per-session container it uses by default, so anyone's Claude can recall what a teammate decided.

## Why it matters

Claude's built-in memory is per-account and not queryable by teammates. This bolts a cross-user, queryable memory layer onto a tool already in the stack, which is a different problem from the single-user auto-memory and build-your-own-search lessons already in the library.

## How to apply

1. Install the plugin (marketplace > add from repository > `supermemoryai/claude-supermemory`) and get an API key.
2. Run `/project-config` to set the API key plus a project container tag (for example `team-os`). Run it from inside a shared, persistent project folder: the tag is scoped to that session or folder, so running it elsewhere only sets the tag for that one chat.
3. Invite each teammate to the supermemory workspace **first**, then have them create their own API key and run the same `/project-config` with the identical container tag. A key created before the invite lands in a separate private workspace by default.
4. If saves silently fail, allow `api.supermemory.ai` in Claude's sandbox domain allowlist (Settings > Capabilities).

## Related

[[shared-memory-retains-content-after-source-access-revoked]], [[composio-mcp-gateway-scoped-url-for-shared-login-apps]]
