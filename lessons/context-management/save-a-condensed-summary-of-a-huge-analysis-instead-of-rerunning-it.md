---
id: save-a-condensed-summary-of-a-huge-analysis-instead-of-rerunning-it
created: 2026-10-19
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tested-the-viral-reverse-engineer-anything-skill-what-you-need-to-know_rL5tw6h78zo_20261013.txt
---

# Keep a Short Saved Summary of a Heavy Analysis So the Agent Reads It Instead of Re-Running the Analysis

## TL;DR

When a teardown or analysis produces gigabytes of output, have the agent write a short summary (how it works, how it does what it does, what it could not figure out) and read that, with finer module and trace detail one level below.

## Why it matters

Nate Herk says the full Loom analysis was over a gigabyte, so Claude reads a shortened summary, and you do not want to be caught re-running the whole analysis because it is already saved in the project files.

## How to apply

1. Ask for a summary file as the entry point and deeper per-module files below it. 2. Tell the agent where the saved analysis lives and not to redo it. Checked: no tool mechanism named; the gigabyte figure and layout are from the speaker's use of the repo.

## Related

[[pre-aggregate-profiling-data-for-agents]], [[convert-docs-to-markdown-before-feeding-claude]]
