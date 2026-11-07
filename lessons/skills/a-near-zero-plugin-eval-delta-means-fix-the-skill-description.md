---
id: a-near-zero-plugin-eval-delta-means-fix-the-skill-description
created: 2026-09-13
status: active
supersedes: null
category: skills
source_type: canonical
tool: claude-code
sources:
  - https://code.claude.com/docs/en/plugin-evals
---

# Read a Near-Zero Plugin-Eval Delta as a Description Problem, Not a Skill-Body Problem

## TL;DR

When a `claude plugin eval` case shows a delta near zero with a failing `tool_used: Skill` grader, Claude is not choosing your skill on natural phrasing, and the fix is the frontmatter `description`.

## Why it matters

This is the documented first finding for almost every plugin author, and the instinct is to rewrite the skill body, which cannot help: the body is never read if the skill is never selected. Naming the exact field to change turns a vague failure into a one-line edit.

## How to apply

Run `claude plugin eval .` from the plugin root. For any case whose WITH/WITHOUT delta is near zero and whose `tool_used: Skill` grader fails, rewrite that skill's `description:` frontmatter to match the natural phrasing in the eval prompt, then re-run and compare. Requires 2.1.269 or later.

> "The most common first finding is a `Δ` near zero with the case's `tool_used: Skill` grader failing, which means Claude isn't choosing your skill on natural phrasing. Adjust the skill's `description`, run `claude plugin eval .` again, and compare.", Claude Code docs, Test plugins with evals

## Related

[[pin-your-config-with-plugin-eval-cases-run-on-every-release]]
