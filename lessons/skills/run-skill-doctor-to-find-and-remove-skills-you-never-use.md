---
id: run-skill-doctor-to-find-and-remove-skills-you-never-use
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-the-top-1-use-claude-code-differently_J9NQTYUP6k0_20261013.txt
---

# Run /skill-doctor to see what each skill costs and how often it is used, then remove the unused

## TL;DR

/skill-doctor reports each skill's context cost and usage. Remove the ones you never use first, then eval the rest.

## Why it matters

Every listed skill adds to context whether or not it is ever invoked, and most people have not pruned libraries installed for older models. The presenter culled by usage first, then ran the with and without eval on what was left.

## How to apply

Run /skill-doctor in a session (the report opens in the `/plugin` manager's Stats tab and leaves out bundled and enterprise skills). Turn off or delete the skills it flags as never invoked, starting with the highest context cost. Then test the survivors with and without the skill: `claude plugin eval` runs a plugin's eval cases against a no-plugin baseline, and the presenter adapted it for single skills, so a skill needs eval cases written for it first.

Checked: Live docs skills.md and commands.md (fetched 2026-11-22): '/skill-doctor' shows what each skill costs and how often it gets used, requires v2.1.252 or later and feature-flag fetching. Installed binary Claude Code 2.1.330 contains 'skill-doctor' (17 matches). `claude plugin eval --help` on 2.1.330: runs eval cases (`case.yaml` or `prompt.md` plus graders) and adds a no-plugin baseline arm.

## Related

[[run-checkup-doctor-to-audit-setup-health-and-context-bloat]]
