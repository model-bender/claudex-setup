---
id: claude-plugin-validate-checks-a-bare-skills-directory
created: 2026-08-16
status: active
supersedes: null
category: skills
tool: claude-code
source_type: canonical
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Run `claude plugin validate` on a Plain `.claude/skills` Directory - No Plugin Needed

## TL;DR

As of 2.1.233, `claude plugin validate` works on a repo with no plugin manifest at all, reporting any `SKILL.md` whose frontmatter fails to parse.

## Why it matters

A skill with malformed frontmatter does not error - it just never loads. That is invisible until you notice the skill has silently stopped firing, which can be weeks. Until this release the only validator was plugin-scoped, so anyone maintaining a plain `.claude/skills/` tree had to hand-roll a frontmatter checker or go without.

## How to apply

Add `claude plugin validate` to pre-commit or CI in any repo that has a `.claude/skills` directory, alongside whatever artifact checks you already run. It costs one command and catches the entire class of "the skill exists but never loads."

> "Improved `claude plugin validate` to check a bare `.claude/skills` directory, reporting SKILL.md files whose frontmatter fails to parse", Claude Code CHANGELOG 2.1.233

## Related

[[put-every-skill-one-level-under-skills]]
