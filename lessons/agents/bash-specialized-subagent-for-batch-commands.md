---
id: bash-specialized-subagent-for-batch-commands
created: 2026-09-01
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
---

# Use the Built-In @bash Specialized Subagent for Batch or Multi-Step Bash Work

## TL;DR

Typing @bash spawns a subagent purpose-built for running batch/multi-step shell commands (e.g. npm run build), returning only the final result to the main session and keeping its context clean; the same subagent can be assigned via agent: bash in a skill's frontmatter.

## Why it matters

Multi-step or verbose bash sequences (build logs, dependency installs) burn main-session context fast; routing them through a dedicated bash subagent keeps that noise out of the conversation you're steering.

## How to apply

Type @bash and describe the command sequence to hand it to the specialized bash subagent, or set agent: bash in a skill's frontmatter for a skill that's mostly multi-step shell work.

## Related

[[subagents-for-noisy-tool-calls-not-large-edits]]
