---
id: declare-variation-axes-and-tweak-toggles-up-front
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/simon-scrapes/master-claude-design-in-one-video-complete-build_20260603.txt
  - transcripts/sean-kochel/4-step-claude-design-system-for-pro-uis_mJ98eeC0oDg_20260703.txt
---

# Declare Variation Count and Tweak Axes Up Front, Then Derive From the Winner

## TL;DR

At generation time, tell Claude Design how many variations per screen, what those variations should explore, and what the tweaks panel should let you toggle. Then converge by asking for a new variation based on the winning label, not a fresh generation.

## Why it matters

The tweak toggles aren't fixed, you specify them, and whatever axes you name become free to flip afterwards, while anything you didn't name costs a prompt. Naming light/dark and sketchy-vs-clean-stroke returned both, plus notes on/off, explorable in combination at no cost.

The variation machinery is cheap for what it returns: 5 screens × 2 variations for ~4% of a weekly limit, complete with a README explaining the axis ("A sticks to the desktop mental model, B reframes for one-handed mobile use").

Deriving from a label preserves the winner instead of rerolling everything.

> **Scope note.** [[generate-ui-structure-first-then-inject-copy]] says one screen or component per prompt. That still holds for *sequential refinement*, and it was sourced from Stitch/Polymet rather than Claude Design. Claude Design's variation machinery is the exception for *parallel exploration*: a single prompt is the intended way to fan out screens × variations. Use one-per-prompt when iterating, fan-out when exploring.

## How to apply

In the question round, set variations per screen deliberately (2 is a good default "in the order of preserving our tokens"; 5 is available), say what the variations should explore (navigation pattern, density, layout) or hand it over with "decide for me", and name the tweak axes, light/dark, sketchy vs clean, density, notes on/off.

Ask for all variations side by side on one infinite canvas with callouts, and set the device frame.

To iterate, address the variant by its letter and derive: "do a C variation based on B, and clean up the formatting." Paste a screenshot of the specific defect alongside.

## Related

[[keep-the-claude-design-brief-open-enough-to-trigger-its-question-round]], [[generate-ui-structure-first-then-inject-copy]], [[claude-design-draw-to-code]]
