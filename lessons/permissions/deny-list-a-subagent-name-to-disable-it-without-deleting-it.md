---
id: deny-list-a-subagent-name-to-disable-it-without-deleting-it
created: 2026-09-01
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Add a Subagent's Name to the Deny List to Disable It Without Deleting the File

## TL;DR

Instead of deleting an unused subagent's file, add its name to the deny list in settings.json to make it unavailable to Claude Code while keeping the definition on disk.

## Why it matters

Deleting a subagent you might want back later loses its configuration; denying it is reversible and keeps the file around as a reference or for quick re-enabling.

## How to apply

In settings.json's deny list, add the subagent's name (e.g. 'macos-notarize') to make Claude Code stop offering or invoking it, while leaving its file untouched in .claude/agents/.
