---
id: repackage-plugins-to-the-agent-plugins-spec
created: 2026-08-16
status: active
supersedes: null
category: plugins
tool:
  - claude-code
  - codex
source_type: canonical
sources:
  - https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
  - https://github.com/openai/codex/pull/35105
---

# Repackage a Plugin as Root `plugin.json` + `skills/` + `mcp.json` to Ship It Everywhere

## TL;DR

A conformant Agent Plugin is a directory with `plugin.json` at the root, skills in `skills/`, and MCP servers in `mcp.json` - and only those two component types travel. Commands, subagents, and hooks must move under a reverse-domain `extensions` namespace.

## Why it matters

Codex 0.147.0 installs portable Agent Plugins and 0.146.0 reads their manifests, so the same package now loads in Codex, VS Code, and Cursor instead of being Claude-Code-only. The spec is backed by AWS, Cursor, GitHub, Microsoft, OpenAI, and Vercel.

Splitting a plugin into "portable core" and "client extension" is a one-time layout decision that determines whether it is reusable at all. Get it wrong and your plugin stays single-client forever; get it right and the skills and MCP servers you already wrote work in three more places for free.

## How to apply

Add a root `plugin.json` whose `$schema` is exactly `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`, plus a `name`. Move skills to `skills/<name>/SKILL.md` and MCP config to `mcp.json`. Put Codex-only apps, hooks, and interface settings under the inline `com.openai` key in `extensions` - Codex also accepts `.codex-plugin/plugin.json` as a fallback overlay.

> "Agent Plugins v1 defines exactly two component types: **skills** and **MCP servers**. Other component types are outside the v1 format and do not affect conformance.", Agent Plugins Specification 1.0.0

## Related

[[one-bad-field-in-plugin-json-kills-the-whole-plugin]], [[put-every-skill-one-level-under-skills]], [[portable-setup-via-open-standards]]
