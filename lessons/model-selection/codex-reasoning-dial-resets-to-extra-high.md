---
id: codex-reasoning-dial-resets-to-extra-high
created: 2026-07-17
status: active
supersedes: null
category: model-selection
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# Check Codex's Reasoning Dial Before Every Chat: It Lands Back on Extra High

## TL;DR

Codex splits model, reasoning (low/medium/high/extra high), and speed (standard/fast) into three independent per-chat dials, and new chats keep coming up on extra high. Run medium for planning and brainstorming, high for large builds, and extra high only for a bug nothing else cracks.

## Why it matters

Extra high on a simple task doesn't just cost more, it over-engineers the result and runs slow. And because the dial **resets** rather than remembering your choice, you pay that tax by default rather than by decision.

The bill lands on your 5-hour and weekly session budgets, which is the real constraint in daily use.

Fast mode is a separate trap: it buys speed you rarely need on non-time-critical work and burns usage noticeably quicker.

> This is the Codex form of [[max-effort-is-a-trap-quality-plateaus-at-high]], same finding, different product. Kept as a separate lesson deliberately: the Codex mechanics (three independent dials, the reset-to-extra-high default, the fast-mode tax) aren't in the Claude `/effort` lesson, and a Codex reader wouldn't find them there.

## How to apply

Glance at the dial before firing a prompt and drop it to medium unless the task earns more.

Check Settings → rate limits remaining to see what the 5-hour and weekly windows have left.

Leave fast mode off unless you're genuinely against a clock.

In subagents, pin a cheap model explicitly, the noisy investigation work rarely needs the ceiling, and Codex won't spawn one unless you ask anyway.

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[codex-subagents-dont-auto-invoke]], [[leave-codex-fast-mode-off-unless-against-a-clock]]
