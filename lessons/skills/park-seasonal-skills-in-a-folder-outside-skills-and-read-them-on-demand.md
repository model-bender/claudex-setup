---
id: park-seasonal-skills-in-a-folder-outside-skills-and-read-them-on-demand
created: 2026-10-25
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/mark-kashef/anthropic-just-donated-claude-skills-here-s-what-to-delete_2IPR6F3cQ_I_20261024.txt
---

# Park Seasonal Skills Outside the Skills Folder and Have Claude Read Them Just in Time

## TL;DR

A skill is a cheat sheet, so skills you only need in one season can sit in a separate folder that is never loaded, and you ask Claude to read and follow that file when needed.

## Why it matters

Mark Kashef says always-on skills each add their name and description to the context window, which at scale hurts. A skill you used heavily in one busy period does not have to load every session.

## How to apply

1. Move the seasonal skill folders out of the skills directories Claude Code scans (for example into a plain `parked-skills/` folder in your repo). 2. When you need one, tell Claude to go to that folder, read the file and its documentation and run any scripts it references. 3. Inference, not from the video: move it back if you start using it daily. Trade-off, also inference: Claude will not auto-select it, so you must name it each time. Checked: Not run. Skill-listing cost behaviour is covered in the existing skill-description budget lesson; the folder-parking approach itself is the creator's description.

## Related

[[skill-descriptions-share-a-15000-character-ceiling]], [[audit-your-skill-and-mcp-loadout-with-drskill]]
