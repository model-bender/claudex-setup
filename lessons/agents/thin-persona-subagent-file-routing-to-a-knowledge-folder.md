---
id: thin-persona-subagent-file-routing-to-a-knowledge-folder
created: 2026-10-19
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-built-the-ultimate-ai-board-of-advisors-free-claude-skill_nRXHWckVxoM_20261013.txt
---

# Keep a Persona Subagent File Short and Route It to a Per-Persona Knowledge Folder

## TL;DR

Each advisor in Nate Herk's council has a short subagent file that says how the person thinks, the one question they own and how they decide, then links to a folder of markdown files holding their rules, frameworks, positions, stories, voice and sources.

## Why it matters

A persona needs a lot of material, but a single subagent file balloons. Herk's agent files are not long. They tell the agent to read the person's hot sheet (the eight rules they decide by) first and then open frameworks, positions or stories files only when a decision needs them. For one persona the folder was built from about 124 public sources and over 1.3 million words (YouTube, X, LinkedIn, blogs), and he repeated this for all seven. Swapping an advisor means building another folder to the same pattern.

## How to apply

1. Create .claude/agents/<name>.md with identity, the single question this persona owns, and how they debate and decide.
2. In the file, instruct the agent to read <name>/hot.md first and consult frameworks, positions, stories, voice and sources files on demand.
3. Have research agents populate the folder from public material, and keep one consistent file layout so personas can be swapped.
Checked: this mirrors Claude Code's subagent files in .claude/agents/ and read-on-demand files. The hot.md naming is his; the 124 sources and 1.3M words figures are his for one persona.

## Related

[[subagent-definitions-live-in-one-ballooning-file]], [[separate-skill-md-from-references-to-localize-debugging]], [[clone-a-real-stakeholder-skill-for-pre-submission-feedback]]
