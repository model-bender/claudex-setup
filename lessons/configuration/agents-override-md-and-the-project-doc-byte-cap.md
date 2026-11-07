---
id: agents-override-md-and-the-project-doc-byte-cap
created: 2026-07-25
status: active
supersedes: null
category: configuration
source_type: canonical
tool: codex
sources:
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
---

# Use `AGENTS.override.md` for Temporary Codex Instructions: and Watch the 32 KiB Doc Cap

## TL;DR

At both global and per-directory scope, Codex prefers `AGENTS.override.md` over `AGENTS.md` and takes at most one file per directory, and it silently stops loading instructions once the concatenation hits `project_doc_max_bytes` (32 KiB by default).

## Why it matters

The override file is the clean way to run a temporary instruction set, for a spike, an incident, or a one-off migration, instead of editing your real AGENTS.md and remembering to revert it. The byte cap is the quieter trap: past 32 KiB, guidance is dropped with **no error**, so the nested AGENTS.md you carefully added simply stops being read and you debug the model instead of the config.

## How to apply

Drop `~/.codex/AGENTS.override.md` (or a per-directory one, e.g. `services/payments/AGENTS.override.md`) for temporary or team-specific rules, and delete it to restore the base file. Raise `project_doc_max_bytes` in `~/.codex/config.toml`, or split instructions across nested directories, if you are near the cap. Set `project_doc_fallback_filenames = ["CLAUDE.md"]` to let Codex read an existing Claude Code memory file where no AGENTS.md exists.

> "In each directory along the path, it checks for AGENTS.override.md, then AGENTS.md, then any fallback names in project_doc_fallback_filenames. Codex includes at most one file per directory.", OpenAI Codex docs

## Related

[[code-review-rules-section-in-agents-md]], [[import-claude-code-into-codex-and-turn-on-sync]], [[set-project-doc-fallback-filenames-so-codex-reads-claude-md]]
