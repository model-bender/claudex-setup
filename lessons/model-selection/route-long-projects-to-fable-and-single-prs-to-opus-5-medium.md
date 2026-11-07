---
id: route-long-projects-to-fable-and-single-prs-to-opus-5-medium
created: 2026-07-25
status: active
supersedes: null
category: model-selection
source_type: post
tool: claude-code
sources:
  - https://x.com/dmwlff/status/2080705598585438369
  - https://x.com/alexalbert__/status/2080703118086693121
---

# Route Long-Running Projects to Fable 5 and Single-PR Work to Opus 5 at Medium Effort

## TL;DR

A Claude Code engineer's own routing rule after the Opus 5 launch: Fable 5 for big, long-horizon projects; Opus 5 at *medium* reasoning effort for turning out a single PR.

## Why it matters

The naive assumption is "Fable is strictly better, use it whenever you can afford it." A Claude Code engineer routing *away* from Fable for ordinary PR work is a concrete counterweight, and he names the effort level, not just the model, which is the part most routing tables omit. Alex Albert corroborated the same day: "It feels very smooth to use and I prefer it over Fable 5 for many coding tasks."

## How to apply

Default to Opus 5 at medium effort for scoped ship-a-PR work, and reserve Fable 5 for multi-day or long-running projects where the horizon is the hard part. Pin the effort level explicitly rather than inheriting whatever the session is on.

> "Opus 5 is live in Claude Code. I use Fable for my bigger, longer running projects, but when I need to crank out a PR, Opus 5 at medium effort is my go-to.", Adam Wolff

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[minimum-viable-model-year-ago-test]], [[auto-mode-is-not-injection-containment-isolate-the-session]]
