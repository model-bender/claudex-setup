---
id: claude-api-prompt-audit-finds-old-model-prompt-patterns
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Run the claude-api Skill's prompt-audit Subcommand Over Prompts Written for Older Models

## TL;DR

The bundled `claude-api` skill gained a `prompt-audit` subcommand that flags prompts and tool descriptions written with older-model idioms.

## Why it matters

Prompting patterns that existed to prop up weaker models (heavy repetition, over-specified step-by-step instructions, defensive negative constraints) actively degrade newer ones, and they are invisible in review because they read as thorough rather than harmful. Until now, finding them meant re-reading every prompt and tool description by hand and knowing which idioms had aged out.

## How to apply

Invoke the `claude-api` skill's `prompt-audit` subcommand against your system prompts and tool-definition descriptions, especially after a model upgrade. Treat its hits as candidates to delete rather than rewrite, since the usual fix is removing scaffolding, not adding more.

> "Added a `prompt-audit` subcommand to the `claude-api` skill for auditing prompts and tool descriptions for patterns written for older models", Claude Code CHANGELOG 2.1.221

## Related

[[skill-description-is-routing-logic-not-marketing]], [[disambiguate-tool-descriptions-with-do-not-use-clauses]]
