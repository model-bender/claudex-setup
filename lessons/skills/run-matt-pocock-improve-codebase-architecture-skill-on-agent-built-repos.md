---
id: run-matt-pocock-improve-codebase-architecture-skill-on-agent-built-repos
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-build-sell-software-with-ai-as-a-non-techie_l8ywUsEJ2XQ_20261009.txt
---

# Review agent-built codebases with Matt Pocock's improve-codebase-architecture skill

## TL;DR

Install Matt Pocock's skills and run `improve-codebase-architecture` to review a repo for structure problems. The guest uses it very often to review their own codebases.

## Why it matters

The guest says the skill covers deep modules, locality and seams, and that its author made it to fight AI slop and make codebases easier for AI to navigate. Correction to the transcript: the guest thought the skill had been renamed to something like 'codebase design'. In the repo both exist: `improve-codebase-architecture` is still the review command and it loads a separate `codebase-design` skill for its vocabulary.

## How to apply

Per the repo README: Claude Code `claude plugin install mattpocock-skills@claude-plugins-official`; Codex `codex plugin marketplace add mattpocock/skills` then `codex plugin add mattpocock-skills@mattpocock`. Invoke the skill explicitly: its frontmatter sets `disable-model-invocation: true`, so the model will not start it by itself.

Checked: Github.com/mattpocock/skills fetched with curl on 2026-11-22: skills/engineering/improve-codebase-architecture/SKILL.md and skills/engineering/codebase-design/SKILL.md both exist; the first has `disable-model-invocation: true` and calls the second; install commands copied from the repo README, not executed; `claude plugin` subcommand present on Claude Code 2.1.330.

