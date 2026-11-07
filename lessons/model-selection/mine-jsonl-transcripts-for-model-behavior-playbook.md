---
id: mine-jsonl-transcripts-for-model-behavior-playbook
created: 2026-07-10
status: active
supersedes: null
category: model-selection
sources:
  - transcripts/mark-kashef/make-any-model-think-like-fable-in-10-minutes-it-s-easy_B95cu7seTm8_20260704.txt
---

# Mine Your JSONL Session Transcripts to Distill a Stronger Model's Behavioral Playbook

## TL;DR

Your Claude Code/Codex sessions are JSONL files tagged with which model produced each turn; have Claude parse them to measure the behavioral delta (tool cadence, reads-before-edits, tests-after-edits, turn count, plan-before-act) between a stronger and weaker model, distill a playbook, and inject it to make the weaker model behave more like the stronger.

## Why it matters

You can't clone a model's weights, but much of a stronger model's advantage is behavioral rhythm - planning before acting, disciplined tool use at the right time - which a weaker model can be prompted to imitate; captured as real measured numbers rather than vibes, the imitation is concrete and reusable across closed- and open-source models.

## How to apply

Have Claude write a Python script that strips JSONL bloat (tool results, echoed file contents, command output) keeping timestamp/model/prompt/response/tool-order; filter turns by the message-model tag to build a per-model corpus; run the same behavioral read on both models and diff the cadence and ratios; distill a playbook.md of 'how model B can act like model A' and inject it via a SessionStart hook, a skill, a CLAUDE.md block, or by tagging it in-session (ask the Claude Code Guide agent to wire the hook). If you lack data for the stronger model, run the analysis on open-sourced Fable-5 session datasets on Hugging Face.
