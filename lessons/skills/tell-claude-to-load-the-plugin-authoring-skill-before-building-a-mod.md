---
id: tell-claude-to-load-the-plugin-authoring-skill-before-building-a-mod
created: 2026-10-11
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/mark-kashef/these-mods-take-claude-code-to-another-level_UcvD53jqHRU_20261009.txt
  - transcripts/tristen-o-brien/claude-code-just-dropped-mods-master-it-in-10-minutes_LDn7rQKIFro_20261009.txt
---

# Start a mod build by telling Claude to load the plugin-authoring skill and re-read the docs

## TL;DR

Open the build prompt for a Claude Code mod with an instruction to load the plugin authoring skill so it primes itself on how mods work before writing code.

## Why it matters

Mark opens his threads-mod prompt with: before you write anything, load the plugin authoring skill and remind yourself how mods work; go and check your documentation so you fully context prime yourself.

## How to apply

First line of the mod prompt: before you write anything, load the plugin-authoring skill, check its documentation, then build. Then describe the goal and tests (after a few failed tries he gave it a /goal naming the errors to troubleshoot, and it got there after about an hour).

Tristen O'Brien says a mod is a small add-on that changes how Claude Code looks and works; you describe the feature and Claude builds it using a built-in skill, then asks you to reload.

Checked: grep -c -a 'plugin-authoring' on the 2.1.296 binary: 8; the skill is listed in this session

## Related

[[enable-function-hooks-to-unlock-plugin-authoring]]
