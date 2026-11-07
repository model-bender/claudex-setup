---
id: max-effort-is-a-trap-quality-plateaus-at-high
created: 2026-07-12
status: active
supersedes: null
category: model-selection
sources:
  - transcripts/simon-scrapes/12-hidden-tricks-that-unlock-claude-code_M2p7OvKLAWw_20260710.txt
  - transcripts/nate-herk-ai-automation/how-i-make-opus-think-like-fable-5-easy-steps_XTBWVVcF3Pk_20260710.txt
  - transcripts/nate-herk-ai-automation/gpt-5-6-sol-made-this-entire-video_J_jswzXhYJA_20260710.txt
  - transcripts/tristen-o-brien/claude-just-dropped-opus-4-8-master-it-in-6-minutes_20260610.txt
---

# Match /effort to Task Risk: But Max Rarely Beats High on Capable Models

## TL;DR

`/effort` is a per-task dial for reasoning depth: match it to the change's blast radius, default for routine work, high for genuinely hard or risky changes (migrations, auth, concurrency, tricky refactors). But on capable models (Fable 5, Opus 4.8) quality and correctness plateau around high: max mostly buys extra re-verification and can push the model into overthinking and second-guessing at roughly double the cost, so reserve it for rare cases and calibrate spend with `/usage`.

## Why it matters

Effort is a dial, not a set-and-forget setting: low effort on intricate logic ships missed edge cases, and max effort on trivial edits wastes time and tokens. The older "crank to extra-high/max for anything risky" advice overreaches at the top end, raising past high doesn't reliably improve correctness on strong models (per timed testing and heavy Fable-5/Opus-4.8 use); it just inflates tokens/time and can regress a capable model into an overthinking loop that ships something worse than high would have. The durable win is matching effort to risk while treating **high** (not max) as the practical ceiling for most hard work.

## How to apply

Keep `/effort` on default for everyday work and bump to high for genuinely intricate or high-blast-radius changes (migrations, auth, concurrency, tricky refactors). Reserve max for rare cases and confirm with `/usage` that the spend was justified, and don't leave a strong model parked on max/extra-high: if it starts running long and second-guessing itself, drop back to high. Note that `ultrathink` already raises a single turn to high (not max), see another lesson.

## Contested: Anthropic's launch-day guidance said the opposite

Recorded so this is not re-litigated from the tweet. On Fable 5's launch day (2026-06-09), Anthropic's Head of Developer Relations advised the reverse: *"Use xhigh/high effort as your default for best performance, med for faster interactive sessions."* ([source](https://x.com/alexalbert__/status/2064467657483829441))

**This lesson still stands, on three grounds.** It is *later* (2026-07-12 against launch day, when nobody had more than hours of use), it rests on *comparative measurement* rather than assertion (a dozen effort levels on one task producing near-identical output, see [[sharpen-the-spec-before-reaching-for-more-effort]]), and adopting the tweet would resurrect `effort-control-for-token-intensive-work`, which this lesson already superseded for saying almost exactly the same thing. Albert himself is quoted six weeks later corroborating a medium-effort preference for single-PR work in [[route-long-projects-to-fable-and-single-prs-to-opus-5-medium]].

The half of that advice which is *not* contested is "med for faster interactive sessions", which prescribes the same action this lesson does and differs only in the rationale offered (latency rather than token cost).
