---
id: fork-init-into-project-archetype-scaffolding-skills
created: 2026-07-25
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Fork /init Into One Scaffolding Skill Per Project Archetype You Actually Start

## TL;DR

The built-in `/init` is a generic starting point, not *your* starting point. Build a skill per project type you repeatedly begin, `/init-nextjs-microapp`, `/init-client-onboarding`, that scaffolds the structure, config, and conventions exactly the way you always end up doing it by hand.

## Why it matters

The creator keeps separate init skills for proof-of-concept Next.js apps and for onboarding a new client, because each sets the project up differently and both are things he starts often enough that redoing the setup conversation each time is pure waste. Generic `/init` produces a generic CLAUDE.md and no scaffolding at all, so the first hour of every new project goes on re-deriving decisions you already made on the last one, and inconsistently, since you re-derive them from memory.

## How to apply

List the project types you start more than a couple of times a year. For each, take the existing `/init` skill as the base and have Claude extend it into a named variant that creates the folder structure, config files, dependencies, CLAUDE.md, and starter commands you always add. Trigger it explicitly at project creation rather than relying on auto-invocation. Apply the usual skill-frequency test first, if you start that kind of project once, prompt it rather than building the skill.

## Related

[[skill-frequency-test-inner-loop]], [[ask-the-wrong-primitive-question-before-building-a-skill]]
