---
id: omit-claude-md-from-a-subagent-with-omitclaudemd
created: 2026-09-24
status: active
supersedes: null
category: agents
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
---

# Give a Custom Subagent omitClaudeMd: true to Run It Without Any CLAUDE.md

## TL;DR

Custom/plugin agent definitions (frontmatter or --agents JSON) can now declare omitClaudeMd to deliberately exclude user, project, and local CLAUDE.md from that subagent's context, while still loading managed (org) policy files.

## Why it matters

This is the opposite problem from the well-known "built-in Explore/Plan agents skip CLAUDE.md by accident" gotcha already in this library, this is an opt-in, supported way to build a subagent that must NOT inherit your style/preferences on purpose, e.g. a naive-user simulator, a blind discoverability tester, or any worker you want judged on the raw task rather than your house rules.

## How to apply

Add `omitClaudeMd: true` to a custom agent's frontmatter, or the equivalent field in --agents JSON, when you want that subagent's behavior to be uncontaminated by your CLAUDE.md; managed/organization policy files still apply regardless. Checked: `omitClaudeMd` confirmed in the installed 2.1.281 binary as a real Agent tool field: "omitClaudeMd:M().optional().describe("Run this agent without the user, p[roject, and local CLAUDE.md]")", and it's listed among the built-in Explore/Plan agent's own fixed config (`omitClaudeMd:!0`) alongside `model:"inherit"`.

> "Added `omitClaudeMd` to agent frontmatter and `--agents` JSON, letting custom and plugin subagents run without user, project and local CLAUDE.md files; managed policy files still load", Claude Code CHANGELOG 2.1.271

## Related

[[restate-critical-rules-in-subagent-prompts-explore-and-plan-skip-claude-md]], [[blind-test-a-claude-md-change-with-naive-subagents]]
