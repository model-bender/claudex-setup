---
id: skill-log-in-claude-plugin-data-directory-survives-updates
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/anthropic-just-dropped-their-internal-skills-strategy_20260424.txt
---

# Store a Skill's Persistent Log in the Claude Plugin Data Directory, Not the Skill Folder

## TL;DR

A skill's continuity log/state file should be written to Anthropic's dedicated plugin-data storage rather than inside the skill's own folder, so it survives skill updates.

## Why it matters

The transcript notes that if you tell Claude Code to add the log via "Claude plugin data," it "will store it reliably on your computer somewhere such that if the skill was updated from the like external plugin library, then the data would not be lost" - a file living inside the skill's own directory would be at risk when the skill itself is updated.

## How to apply

When adding a continuity log or data file to a skill, instruct Claude Code to store it via the plugin-data storage location instead of a path under the skill's own folder, so the data isn't wiped the next time the skill is updated from its source.

## Related

[[skill-log-file-for-continuity-between-runs]]
