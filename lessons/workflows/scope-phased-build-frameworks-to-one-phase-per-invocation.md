---
id: scope-phased-build-frameworks-to-one-phase-per-invocation
created: 2026-07-10
status: active
supersedes: null
category: workflows
sources:
  - transcripts/sean-kochel/google-s-7-step-vibe-engineering-skill-is-incredible_4bfKyZ7hbsU_20260703.txt
---

# Drive Phased-Build Frameworks One Phase Per Invocation or They Burn Your Whole Context Window

## TL;DR

Multi-phase build skills/commands (e.g. Google Cloud's agent-skills library) will, if you just say 'build,' try to execute the entire phased plan in a single session and exhaust your context; explicitly scope each run to one phase (`build phase two`) and clear context between phases.

## Why it matters

These frameworks decompose a plan into sequential phases precisely so each fits a fresh window, but their default is to keep going through all of them, which blows the context budget mid-build and degrades output - the exact 'Claude eats my context' complaint - when a clean per-phase cadence would have preserved quality.

## How to apply

When invoking a phased-build command, name the specific phase (`/agent-skills build phase one`, clear context, then `phase two`, etc.) rather than a bare 'build the plan'; and where a framework's skill should run but auto-invocation is unreliable, explicitly tell it to use that skill by name (e.g. 'use the front-end UI engineering skill' or 'use the API and interface design skill') instead of trusting it to choose.

## Related

[[name-the-skill-explicitly-when-auto-invocation-is-unreliable]]
