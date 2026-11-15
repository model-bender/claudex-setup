---
id: use-agents-override-md-for-temporary-codex-instructions
created: 2026-11-15
status: active
supersedes: null
category: configuration
tool: codex
source_type: canonical
sources:
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
---

# Use `AGENTS.override.md` for Temporary Codex Instructions

## TL;DR

At both global and per-directory scope, Codex prefers `AGENTS.override.md` over `AGENTS.md` and takes at most one file per directory.

## Why it matters

The override file is the clean way to run a temporary instruction set, for a spike, an incident, or a one-off migration, instead of editing your real AGENTS.md and remembering to revert it.

## How to apply

Drop `~/.codex/AGENTS.override.md` (or a per-directory one, e.g. `services/payments/AGENTS.override.md`) for temporary or team-specific rules, and delete it to restore the base file.

> "In each directory along the path, it checks for AGENTS.override.md, then AGENTS.md, then any fallback names in project_doc_fallback_filenames. Codex includes at most one file per directory.", OpenAI Codex docs

## Related

[[codex-warns-when-project-instructions-exceed-project-doc-max-bytes]], [[set-project-doc-fallback-filenames-so-codex-reads-claude-md]]
