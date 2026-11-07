---
id: route-ui-work-to-vision-capable-models-only
created: 2026-08-29
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-know_UsfCe5fJK6A_20260824.txt
---

# Never route UI or design tasks to a vision-less model, the screenshot-verify loop is what catches broken layouts

## TL;DR

Models that can't see images (e.g. DeepSeek V4 Flash/Pro) can't run the screenshot, look, reason, iterate loop, so visually broken output ships undetected; when routing work to cheap models, keep anything with a rendered UI on a vision-capable model.

## Why it matters

The creator built a website with a blind model and got a visible layout defect "that Codex or Claude Code would have never let happen because of the verification checks and because of the ability to screenshot, look, reason, iterate." The failure isn't the harness: the verify step of UI work is inherently visual, so a text-only model has no way to catch its own visual mistakes. This turns "which model is cheaper" into a capability-routing rule: per-token price is irrelevant for a task whose acceptance test the model physically cannot run.

## How to apply

Before assigning a task to a cheap or open-weight model, ask whether verifying it requires looking at rendered output (websites, dashboards, slides, design exports). If yes, route it to a vision-capable model, or split the task: blind model drafts, vision model runs the screenshot-grading pass. Keep a note of which models in your routing table are vision-capable and treat "can't screenshot" as a hard disqualifier for design work.

## Related

[[visual-self-validation-screenshot-grading]], [[route-claude-code-to-cheaper-or-local-models]]
