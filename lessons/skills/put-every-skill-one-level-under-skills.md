---
id: put-every-skill-one-level-under-skills
created: 2026-08-16
status: active
supersedes: null
category: skills
tool:
  - claude-code
  - codex
source_type: canonical
sources:
  - https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
  - https://github.com/openai/codex/pull/35105
---

# Put Every Skill One Level Under `skills/` - Nested Skill Directories Are Never Discovered

## TL;DR

Skill discovery inside a plugin is strictly one level deep, so grouping skills into category subfolders (`skills/review/security/SKILL.md`) silently loses all of them.

## Why it matters

Organizing a growing skill set into subfolders is the obvious instinct once you pass a dozen skills, and it fails with no error. The plugin still loads - just with fewer skills than you wrote. Codex implements exactly this rule: direct-child discovery that excludes nested skills and any path resolving outside the plugin root.

## How to apply

Flatten to `skills/<skill-name>/SKILL.md` and encode grouping in the skill *name* (`review-security`) instead of the directory tree. Nesting is still allowed and expected *inside* each skill directory - keep `scripts/`, `references/`, and `assets/` there.

> "Each immediate child directory containing a path named exactly `SKILL.md` that resolves to a regular file is treated as one skill. Clients MUST NOT recursively search deeper descendants for additional skills.", Agent Plugins Specification 1.0.0, §7.1

## Related

[[repackage-plugins-to-the-agent-plugins-spec]], [[claude-plugin-validate-checks-a-bare-skills-directory]], [[keep-codex-skill-descriptions-short]]
