---
id: skills-edited-mid-session-now-appear-without-restart
created: 2026-07-25
status: active
supersedes: null
category: gotchas
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Stop Restarting Claude Code After Editing a Skill: Mid-Session Changes Now Reach the Slash Menu

## TL;DR

Skills and commands edited or added mid-session now show up in the slash menu without exiting or `/clear`-ing, so the restart-after-install ritual is obsolete as of 2.1.216.

## Why it matters

The old workaround cost a full context reset every time you iterated on a skill, which is the single most common skill-authoring loop, so the tax was paid constantly. People will keep paying it until told it was fixed, and a habit like this outlives the bug that created it by months.

## How to apply

Edit the skill or command and invoke it directly. Only restart if it genuinely fails to appear. On versions before 2.1.216 the old advice still holds, so check your version before concluding a skill is broken.

> "Fixed skills and commands changed during a session not appearing in the slash menu until restart", Claude Code CHANGELOG 2.1.216

## Related

[[run-a-skill-cold-to-verify-it-still-triggers]]
