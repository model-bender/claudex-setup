---
id: set-project-doc-fallback-filenames-so-codex-reads-claude-md
created: 2026-08-31
status: active
supersedes: null
category: configuration
tool: codex
sources:
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
---

# Set project_doc_fallback_filenames So Codex Reads an Existing CLAUDE.md Where No AGENTS.md Exists

## TL;DR

In ~/.codex/config.toml, set project_doc_fallback_filenames = ["CLAUDE.md"] so a directory that only carries a Claude Code memory file still feeds instructions to Codex, with no rename and no duplicate file to maintain.

## Why it matters

A repo configured for Claude Code often has no AGENTS.md at all, so Codex runs there without the project's instructions and you debug the model instead of the config. The fallback list closes that gap in one config line instead of a rename or a second copy that drifts. Per the OpenAI Codex docs, in each directory along the path Codex checks for AGENTS.override.md, then AGENTS.md, then any fallback names in project_doc_fallback_filenames, and includes at most one file per directory.

## How to apply

Add project_doc_fallback_filenames = ["CLAUDE.md"] to ~/.codex/config.toml. Because Codex takes at most one instruction file per directory and checks AGENTS.override.md and AGENTS.md first, the fallback only kicks in where no AGENTS file exists, so it is safe to leave enabled globally.

## Related

[[agents-override-md-and-the-project-doc-byte-cap]]
