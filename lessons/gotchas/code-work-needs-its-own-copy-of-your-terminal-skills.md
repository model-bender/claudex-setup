---
id: code-work-needs-its-own-copy-of-your-terminal-skills
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# Code Work can't see .claude/skills: re-add skills via Customize and restart the session

## TL;DR

Skills you built in the terminal under .claude/skills/ are invisible to Claude Code Work even if you give it access to that exact folder; you must re-create the skill or upload it as a zip in Code Work's Customize window, and because Code Work loads all skills at session start, a skill added mid-session needs a restart before it's usable.

## Why it matters

This is a silent capability gap between two surfaces of the same product: the folder tree that makes a skill discoverable in the terminal does nothing in Code Work, so a skill you rely on simply never fires there and you may not notice it's absent. The session-start loading rule compounds it, because after you finally add the skill via Customize, it still won't trigger in the current session, which reads as the skill being broken rather than not yet loaded.

## How to apply

For each terminal-built skill you want in Code Work, open the Customize window and either add the skill as a zip file or re-create it there, accepting the duplication for now. After enabling or adding any skill in Code Work, restart the session before invoking it. Keep a note to reconcile the duplicates when the two surfaces eventually share a skill store.

## Related

[[claude-ai-synced-skills-lose-bash-and-file-expansion]], [[skills-edited-mid-session-now-appear-without-restart]]
