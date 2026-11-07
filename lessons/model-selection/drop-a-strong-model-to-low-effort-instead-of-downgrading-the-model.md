---
id: drop-a-strong-model-to-low-effort-instead-of-downgrading-the-model
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/simon-scrapes/claude-5-changed-prompting-forever-fix-yours-now_dfi3BsEPxic_20260910.txt
---

# For a Genuinely Short Task, Drop Effort to Low Rather Than Switching to an Older Model

## TL;DR

Anthropic says Fable 5.1 on low is still competitive with the older Opus models on cost per task, so the cheap option for small work is the strong model with the effort dial down, not a weaker model.

## Why it matters

The instinct when a task is trivial is to pick a cheaper model, which costs you the newer model's judgment and its willingness to run the whole job end to end. Simon's framing from the Anthropic guidance inverts that: keep the capable model and spend less per task by moving the effort dial, which preserves quality on the parts that need it. Anthropic itself advises dropping effort to low or medium when the task really is a few minutes of work.

## How to apply

Before reaching for a weaker model on a small task, set effort to low (or medium) on the model you are already using, and confirm the spend afterwards with /usage. Keep the model swap for cases where the task class genuinely differs, not for cases where it is just short.

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[route-long-projects-to-fable-and-single-prs-to-opus-5-medium]], [[strongest-model-is-faster-overall]]
