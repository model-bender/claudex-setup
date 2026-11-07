---
id: when-a-claude-md-rule-is-ignored-shorten-the-file-not-the-emphasis
created: 2026-08-29
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/simon-scrapes/19-claude-code-mistakes_icM0ewXGvAw_20260824.txt
---

# When a CLAUDE.md rule keeps being ignored, shorten the file, don't shout the rule

## TL;DR

Anthropic's tested diagnostic: if Claude keeps doing something you banned despite a rule against it, the file is probably too long and the rule is getting lost; capitalizing it or prefixing IMPORTANT is the wrong fix. Models follow roughly 150-200 instructions reliably and the best-performing instruction files sit around 300-350 words.

## Why it matters

The instinctive response to a disobeyed rule is to add emphasis, which grows the file and makes the underlying problem worse. The numbers give you a concrete budget to diagnose against: Claude Code's own system prompt is about 50 instructions, and adherence degrades as your instruction count approaches the 150-200 range, so a 400-line CLAUDE.md is statistically guaranteed to have rules falling out of attention regardless of formatting. Treating a disobeyed rule as a length symptom, not an emphasis problem, is the repair action most people never make.

## How to apply

When a rule misfires repeatedly, count your file's length rather than rewriting the rule: is it under 100 lines? Under 200? Move detailed context into separate referenced files that Claude pulls in when needed. Run /doctor with a prompt like "propose trims to my CLAUDE.md that won't impact performance" to get a concrete trim list; the transcript's example run found seven trimmable sections worth 4,000-5,000 tokens per session.

## Related

[[claude-md-hierarchy-keep-it-under-200-lines]], [[run-checkup-doctor-to-audit-setup-health-and-context-bloat]]
