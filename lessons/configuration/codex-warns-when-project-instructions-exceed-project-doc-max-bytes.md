---
id: codex-warns-when-project-instructions-exceed-project-doc-max-bytes
created: 2026-11-15
status: active
supersedes: null
category: configuration
tool: codex
source_type: canonical
sources:
  - https://github.com/openai/codex/releases/tag/rust-v0.168.0
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
---

# Heed Codex's Byte-Budget Warning: Instructions Past project_doc_max_bytes Are Cut

## TL;DR

Since 0.168.0 Codex warns when the project instructions it loads exceed `project_doc_max_bytes` (32 KiB by default) instead of dropping the overflow without a word; trim or split the files, or raise the cap.

## Why it matters

Before 0.168.0, guidance past the cap was dropped with no error, so a nested AGENTS.md could stop being read while you debugged the model instead of the config. The cap itself is unchanged.

## How to apply

When the warning appears, trim the instructions or split them across nested directories, or raise `project_doc_max_bytes` in `~/.codex/config.toml` if you need to keep them all.

Checked: `project_doc_max_bytes` has 23 hits on codex-cli 0.169.0, and the binary carries the warning text "Trim your project instructions".

> "#59445 Warn when project instructions exceed the configured byte budget @etraut-openai", Codex release notes 0.168.0

## Related

[[use-agents-override-md-for-temporary-codex-instructions]]
