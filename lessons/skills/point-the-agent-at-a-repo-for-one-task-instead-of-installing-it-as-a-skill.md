---
id: point-the-agent-at-a-repo-for-one-task-instead-of-installing-it-as-a-skill
created: 2026-10-19
status: active
supersedes: null
category: skills
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/your-claude-codex-setup-is-a-mess-here-s-the-fix_eXoBC1TY8m4_20261018.txt
---

# For a One-Off Task, Name the Repo in the Prompt Instead of Installing It as a Skill

## TL;DR

When a trending repo or skill might help with one job, tell the agent to refer to it for that task rather than adding it to your permanent skill set. Install only what is needed on most tasks.

## Why it matters

Kashef describes setups where individually useful skills pile up, overlap, send mixed signals and are never updated, so they steer agents slightly wrong. He compares it to sailing from New York to Glasgow one degree off course. One of his client setups had 15 skills with only 3 relevant to the business. His test for a new import: is it needed on most tasks, and would your work be worse without it? If not, point the AI at the skill and have it extract the one instruction worth keeping. Scope it narrowly if it is only sometimes useful.

## How to apply

1. Instead of installing, write: for this task, read <repo or skill URL> and apply it.
2. If one idea inside it helps, ask the agent to scan it and add that single instruction to a skill you already have.
3. If it earns a permanent place, install it at project scope and keep it there until proven.
Checked: no flag or setting is named; this is a workflow rule from the video.

## Related

[[default-new-assets-to-project-scope-promote-to-global-when-proven]], [[curate-a-bulk-skill-pack-before-installing-not-after]], [[explainability-test-to-prune-overlapping-skills]]
