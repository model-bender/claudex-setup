---
id: npx-skills-add-cli-installer-local-or-global
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/how-to-use-claude-code-skills-like-the-1-it-s-easy-actually_20260307.txt
---

# Install Marketplace Skills With `npx skills add <dir> --skill <name>`, and a Local Flag to Scope It

## TL;DR

The community `skills` CLI installs a specific skill from a marketplace directory with `npx skills add <marketplace>/<dir> --skill <skill-name>`; adding a local-scope flag (heard in the video as `--local`/`-lo`) installs it into the current project's `.claude/skills` instead of your global skills folder.

## Why it matters

Whether a given install lands globally or per-project depends on this flag, so a skill you only meant to trial in one project can otherwise end up available everywhere (or vice versa) without you noticing.

## How to apply

Run `npx skills add <marketplace>/<dir> --skill <skill-name>` to install a skill; check the tool's own `--help` for its current local/global scope flag before running it against a project you don't want the skill leaking into (or out of).

## Related

[[scope-skills-per-project-not-globally-to-cut-startup-context]]
