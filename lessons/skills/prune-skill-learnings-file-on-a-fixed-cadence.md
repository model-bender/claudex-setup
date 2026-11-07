---
id: prune-skill-learnings-file-on-a-fixed-cadence
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/every-level-of-claude-code-skills-in-27-mins_20260424.txt
---

# Prune a Skill's Learnings File on a Fixed Cadence or It Becomes Its Own Bloat Problem

## TL;DR

A per-skill learnings/rules file that accumulates feedback after every run needs regular pruning, on a fixed cadence such as weekly, or it grows into a second bloated document loaded on every invocation.

## Why it matters

The speaker flags this explicitly as the failure mode of self-improving skills: 'you can't just dump random notes in there forever or it becomes its own context window problem... the key thing here is keeping the learnings file under control... every week we go through the learnings file and strip out any surplus information that won't contribute to quality.'

## How to apply

Pick a fixed review cadence (weekly, per the source) for each skill's learnings.md or rules file. On that cadence, read through it and remove entries that no longer change behavior or add signal, keeping only notes that still meaningfully affect output quality.

## Related

[[skill-log-file-for-continuity-between-runs]], [[agentic-os-heartbeat-and-wrap-up-pattern]]
