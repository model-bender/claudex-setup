---
id: dedicated-lean-repo-per-cloud-routine
created: 2026-07-17
status: active
supersedes: null
category: automation
sources:
  - transcripts/nate-herk-ai-automation/claude-code-for-non-coders-6-hour-course_jdbOVepEtUE_20260712.txt
---

# Point Each Cloud Routine at a Lean Dedicated Repo, Not Your Big AI-OS Repo

## TL;DR

A cloud (remote) routine clones a GitHub repo and reads its CLAUDE.md on every run, so aiming it at your giant context repo loads irrelevant context and burns usage limits, give each routine its own small repo containing only what that job needs.

## Why it matters

Cloud routines run on Anthropic's infra off a cloned repo (no local file access) and re-read that repo's CLAUDE.md every run, exactly like an interactive session, counting against your session/weekly limits the same way. A massive AI-OS repo's CLAUDE.md is wasted tokens for a narrow scheduled task, and each run is resource-capped (≈4 vCPU / 16GB RAM / 30GB disk), so a bloated repo also wastes compute you don't get back.

## How to apply

Create a small purpose-built repo per routine holding just its skill/scripts and a lean CLAUDE.md. Keep the routine prompt one-shot and specific, it can't stop to ask you questions. For secrets and outbound hosts, wire env-var secrets and a domain allowlist into the routine's cloud environment rather than committing them (see another lesson), and tell the prompt to read keys "from the environment variable, not the .env."

