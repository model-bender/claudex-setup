---
id: one-bad-field-in-plugin-json-kills-the-whole-plugin
created: 2026-08-16
status: active
supersedes: null
category: gotchas
tool:
  - claude-code
  - codex
source_type: canonical
sources:
  - https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
---

# One Bad Field in `plugin.json` Kills the Whole Plugin - Not Even the Valid Skills Load

## TL;DR

The portable manifest schema is closed at ten fields (`$schema`, `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`), and any violation beyond an unknown top-level key means the client drops **every** skill and MCP server in the package.

## Why it matters

There are exactly two forgiving cases: an unknown top-level field, and a non-object `extensions` field. Everything else - a wrong type, a malformed name - is all-or-nothing. A plugin goes from fully working to entirely invisible on a single typo, with no partial degradation to hint at what happened.

That failure mode is much worse than a per-component error, because the symptom ("none of my skills are loading") points at the client rather than at one character in a manifest.

## How to apply

Validate `plugin.json` against the pinned 1.0.0 schema in CI before publishing. Keep client-specific keys inside `extensions` under a reverse-domain namespace rather than inventing top-level fields - an unknown top-level key is tolerated today, but a namespaced one is correct by construction.

> "Any schema violation other than an unknown top-level field or a non-object `extensions` field is fatal: the client MUST reject the plugin and MUST NOT discover or execute any of its components.", Agent Plugins Specification 1.0.0, §5.2

## Related

[[repackage-plugins-to-the-agent-plugins-spec]], [[claude-plugin-validate-checks-a-bare-skills-directory]]
