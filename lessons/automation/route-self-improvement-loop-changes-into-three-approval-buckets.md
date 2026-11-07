---
id: route-self-improvement-loop-changes-into-three-approval-buckets
created: 2026-07-10
status: active
supersedes: null
category: automation
sources:
  - transcripts/austin-marchese/8-claude-loops-to-build-10x-faster_HGCHgD4uGgY_20260703.txt
---

# Route a Self-Improvement Loop's Changes Into Auto-Approve / Sign-Off / More-Context Buckets

## TL;DR

When a loop edits your own agent system, have it bucket each proposed change into auto-approve (low-risk), needs-sign-off (skill edits/structural changes - written to a checkbox review file with approve/reject/approve-and-don't-ask-again), and more-context-needed, and log every applied change to a changelog.md.

## Why it matters

A self-improving system that auto-applies everything slowly degrades quality against your taste, while one that asks about everything isn't actually autonomous; the three-bucket split keeps you as the taste-maker on the risky changes while the safe ones compound automatically, and the changelog gives you a visible record of what the system did to itself.

## How to apply

In the loop's prompt, define the three buckets and their routing; send bucket-2 items to a persistent review file as a checkbox list you clear periodically ('approve-and-don't-ask-again' promotes a pattern to auto-approve going forward); send bucket-3 ambiguous items (e.g. can't tell if a repeatedly-mentioned person is a new client) to the same file; append all applied changes to changelog.md.
