---
id: run-claude-security-plugin-before-handover
created: 2026-11-22
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tried-100-github-repos-for-claude-these-6-are-the-best_HhZdNYI4pJs_20261013.txt
---

# Run Anthropic's Claude Security plugin on a project before handing it over

## TL;DR

The Claude Security plugin sends a team of agents through the code looking for holes, with separate agents trying to disprove each other's findings; you get a plain-English report of what survived and it can draft patches for the findings.

## Why it matters

Adversarial verification filters out weak findings, and the speaker's advice is to build this pass into every project because data leaks are what clients actually care about.

## How to apply

Install it with `/plugin install claude-security@claude-plugins-official`, then `/reload-plugins`. As the last step before delivery, run `/claude-security` and pick Scan codebase; read `CLAUDE-SECURITY-RESULTS.md` in the timestamped `CLAUDE-SECURITY-<timestamp>/` folder. Suggest patches writes one patch file per finding into that folder's `patches/` directory and applies nothing itself: apply each with `git apply` or ask Claude to apply it.

Checked: Plugin README and plugin.json in anthropics/claude-plugins-official `plugins/claude-security` (version 0.12.0) read through the GitHub API on 2026-11-22: independent verifiers try to disprove each finding, and 'Nothing is applied for you'. Installed claude binary 2.1.330 contains the string 'claude-security-plugin'. The plugin was not run.

