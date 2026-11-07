---
id: diagnose-context-failure-mode-before-fixing-it
created: 2026-09-01
status: active
supersedes: null
category: context-management
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/5-hacks-to-instantly-level-up-your-ai-os_Ek1NBfnnTH0_20260724.txt
---

# Diagnose Which Context Failure Mode Is Happening Before You Fix It: Poisoning, Bloat, Confusion, or Clash

## TL;DR

When an agent's answer is wrong because of its knowledge base, classify the failure as poisoning (a false fact sits among true ones), bloat (too much data to find what's relevant), confusion (a fact is missing or irrelevant so the model guesses), or clash (two data sources disagree and it doesn't know which is current), because each has a different fix.

## Why it matters

The video's AI-operating-system audit skill is built entirely around detecting these four failure modes; picking the wrong fix for the wrong mode, like adding more data to fix bloat, makes things worse.

## How to apply

Poisoning: add web-search or database cross-checks, or require human-in-the-loop when confidence is low. Bloat: segment the knowledge base into smaller topic-specific stores. Confusion: fill the missing fact or delete the irrelevant one. Clash: date each source and give the agent an explicit rule for which source wins, e.g. trust the most recent policy.

## Related

[[audit-knowledge-base-claims-against-disk-read-only]], [[fact-verification-table-for-claude-claims]]
