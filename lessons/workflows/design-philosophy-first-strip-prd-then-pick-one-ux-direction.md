---
id: design-philosophy-first-strip-prd-then-pick-one-ux-direction
created: 2026-07-10
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/sean-kochel/4-step-claude-design-system-for-pro-uis_mJ98eeC0oDg_20260703.txt
---

# Feed Design Tools a Philosophy-First Brief: Strip the PRD, Then Commit to One of Three Divergent UX Directions

## TL;DR

Before generating any screens in a design tool, strip the engineering detail out of the PRD down to features/jobs/user-journeys, brainstorm three divergent UX philosophies (e.g. conversation-first vs journal-with-assistant vs command-bar-first), and commit to one that then drives every screen.

## Why it matters

Prompting a design tool with a bare 'build me a dashboard' or an engineering-heavy spec-driven doc returns the generic average of its training data; design tools need motivational/feature context, not technical detail, and picking a single UX philosophy up front prevents the model from silently deciding the product's whole interaction model at 'game time.'

## How to apply

Run a PRD→UX step that strips technical details and keeps features, primary user journeys, non-goals, and the USP; generate ~3 adversarially-divergent UX philosophies and filter to one based on who you're building for, persisting the choice to a file; only then produce per-feature/per-state screen briefs and export tool-specific screen prompts, and default to wireframe/black-and-white first so you evaluate structure before aesthetics.

> **Scope note on the wireframe-first default (added 2026-07-17).** It earns its keep where structure is genuinely open: multi-page journeys, app screens, branding and packaging exploration. It does **not** pay on a single page whose structure you already know, a three-concept mid-fi pass on a landing page was measured at ~7% of a weekly design allowance with the output discarded. See [[skip-the-claude-design-wireframe-stage-for-a-single-page]]. Treat this as a scope split rather than a contradiction: wireframe-first is about *structural uncertainty*, and a known single page has almost none.

## Related

[[skip-the-claude-design-wireframe-stage-for-a-single-page]], [[plan-in-claude-chat-then-hand-claude-design-only-the-finished-spec]], [[keep-the-claude-design-brief-open-enough-to-trigger-its-question-round]]
