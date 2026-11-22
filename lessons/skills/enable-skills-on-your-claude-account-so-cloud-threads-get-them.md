---
id: enable-skills-on-your-claude-account-so-cloud-threads-get-them
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/the-new-claude-is-quietly-incredible-17-best-features_KjuANoI8HDw_20261103.txt
---

# Enable your skills on your Claude account, because cloud threads do not load local skills or settings

## TL;DR

Cloud threads do not load the skills and settings on your computer. Turn the skills on in your Claude account so threads get them.

## Why it matters

Otherwise a project thread runs without the personal skills (`~/.claude/skills/`) your local sessions rely on.

## How to apply

Enable the skills for your claude.ai account (the docs point to claude.ai/customize/skills/yours). Per the docs, a skill committed to a project repository's `.claude/skills/` also loads in cloud threads, so a repo-specific skill can live there instead.

Checked: Live docs fetched with curl on 2026-11-22 (claude-projects.md, 'Get skills, plugins, connectors, and tools into threads', and skills.md, 'Use skills in Cowork and cloud sessions'): 'Cloud threads don't have the skills, MCP servers, plugins, and tools installed only on your machine'; skills enabled for the claude.ai account load in cloud threads, apart from some threads in a self-hosted environment; a thread run on your machine through Remote Control uses what is installed there; repository `.claude/settings.json` hooks and permission rules are not applied in cloud threads. The docs list the plans as Pro, Max and Ultra.

## Related

[[prefix-claude-ai-synced-skills-with-anthropic-skills-in-cloud-sessions]], [[opt-out-of-claude-ai-skill-and-plugin-sync]]
