---
id: claude-md-edits-are-invisible-until-restart-clear-or-compact
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# CLAUDE.md edits don't apply mid-session: restart, /clear, or compact to load them

## TL;DR

Project-root and user-level CLAUDE.md files are read once at session start and held in memory, so a rule you add mid-session is silently ignored until you restart, /clear, or compact; a brand-new session picks it up immediately.

## Why it matters

The failure mode is believing a rule is in force when it isn't: you add "always return outputs in bullet points" to CLAUDE.md, the current session keeps ignoring it, and you conclude the rule is badly written or the model is disobedient. Per Anthropic's docs the file is only re-indexed on restart, clear, or compaction, so no amount of rephrasing inside the same session will make the edit land. This is behaviorally distinct from the cache-cost angle (editing CLAUDE.md also invalidates the prompt cache): even paying that cost, the running session does not see the new rule.

## How to apply

When you need a new rule mid-session, either finish the thought and /clear (or start a new session), or force a compact so the file re-indexes. If you just want the rule for the current task, paste it directly into the conversation instead of relying on the CLAUDE.md edit. Batch CLAUDE.md editing into session boundaries as a habit.

## Related

[[prompt-cache-what-breaks-it]], [[skills-edited-mid-session-now-appear-without-restart]]
