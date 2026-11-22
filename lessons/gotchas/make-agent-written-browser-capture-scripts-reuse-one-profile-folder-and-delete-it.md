---
id: make-agent-written-browser-capture-scripts-reuse-one-profile-folder-and-delete-it
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: post
sources:
  - https://www.reddit.com/r/ClaudeCode/comments/1xufdct/my_mac_ran_out_of_disk_i_asked_claude_what_was/
---

# Make Agent-Written Browser Capture Scripts Use One Profile Folder and Delete It in a finally Block

## TL;DR

A screenshot script Claude wrote to check its own UI work launched Chrome with a fresh temp profile every time and never removed it, leaving 157 profiles (about 8.7 GB) and an orphaned headless Chrome that ran for 27 hours.

## Why it matters

None of it shows up in a diff or a test: the code was fine and the waste piled up on the machine until the disk filled.

## How to apply

Add a CLAUDE.md rule that every capture script puts its browser profile in one known folder, removes it in a finally block and kills the Chrome it started; check that folder and the process list for leftover headless Chrome now and then.

Checked: no Claude Code mechanism claim; the leak is in scripts the agent wrote, reported by one user with concrete counts, and the fix is plain script hygiene.

> "every time it took a screenshot to check its own ui work, the script launched chrome with a fresh temp profile and never removed it.", u/Extra_Aide5999 on r/ClaudeCode
