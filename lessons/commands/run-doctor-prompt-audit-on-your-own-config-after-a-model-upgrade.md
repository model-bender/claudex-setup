---
id: run-doctor-prompt-audit-on-your-own-config-after-a-model-upgrade
created: 2026-10-02
status: active
supersedes: null
category: commands
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21283
---

# Run /doctor prompt-audit on Your Own CLAUDE.md, Skills, Agents and Commands After a Model Upgrade

## TL;DR

`/doctor prompt-audit` (also `/checkup prompt-audit`) audits your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models, and its report leads with stale paths, stale commands and contradicting instruction files.

## Why it matters

Instruction files accumulate rules written for older models, and the library already treats retuning skills after a model swap as necessary. This turns that into one command. A same-version follow-up made stale paths, stale commands and contradicting instruction files lead the report. The existing prompt-audit lesson covers the claude-api skill's audit of API prompts and tool descriptions, which is a different target.

## How to apply

Run `/doctor prompt-audit` in a session at the project root after a model upgrade, and work through the report top-down. It hands off to the bundled claude-api skill, so it does not work if that skill is turned off in `skillOverrides`.

Verified: Changelog 2.1.283 entries read from the saved raw CHANGELOG. The 2.1.287 binary has 16 occurrences of prompt-audit and 7 of checkup, and contains the text 'I ran `/doctor prompt-audit`, which hands off to the bundled claude-api skill's prompt audit. That skill is not available in this session: it is disabled, set to off in the skillOverrides'. Not run live.

> "Added `/doctor prompt-audit` (also `/checkup prompt-audit`) to audit your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models", Claude Code CHANGELOG 2.1.283

## Related

[[claude-api-prompt-audit-finds-old-model-prompt-patterns]], [[retune-skills-when-you-swap-model-or-harness]]
