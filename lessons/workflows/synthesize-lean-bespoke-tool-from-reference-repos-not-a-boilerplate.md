---
id: synthesize-lean-bespoke-tool-from-reference-repos-not-a-boilerplate
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/mark-kashef/you-have-the-openclaw-mind-virus_s-BHmRewyNI_20260703.txt
---

# Synthesize a Lean Bespoke Tool From Several Reference Repos Instead of Adopting and Wrangling One Boilerplate

## TL;DR

Rather than spend hours bending a popular but bloated framework (e.g. OpenClaw and its forks) to your needs, clone several competing repos, have Claude Code catalog and compare their features into a pick-list, select only what you want, and have it build a minimal from-scratch version you fully understand and can audit.

## Why it matters

A mass-market boilerplate carries every modality and abstraction you do not need and cannot fully explain - a real problem for security-sensitive or always-on agents - and customizing it costs more time than it saves. Synthesizing your own minimal implementation from the good ideas across repos yields auditable, right-sized code you own, while still letting you 'shop' new repos later.

## How to apply

Tell Claude Code to git clone the candidate repos; prompt it (as a non-technical user) to explain each repo's concepts and build a comparison / 'feature grocery store' of amalgamated features tagged by origin repo; pick the features that matter and export a 'Claude Code brief' markdown wish-list; then in a fresh session, 'build my own framework from this brief, as few lines as possible, make onboarding easy', planning first (a clarifying-question command or plan mode) and executing with an agent team. Ask it to replicate niceties (e.g. a one-line ASCII startup command) by studying the reference repo.
