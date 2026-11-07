---
id: bookend-each-work-item-with-the-strongest-model
created: 2026-08-16
status: active
supersedes: null
category: model-selection
tool: claude-code
source_type: post
sources:
  - https://yegge.ai/essays/the-shape-of-things-to-come/
---

# Bookend Every Work Item With the Top Model: It Plans, the Cheaper Model Implements, Then It Reviews

## TL;DR

Don't stop at "plan on the strongest model, execute on the cheaper one" - route the **review** leg back to the strongest model too, per work item, because the review is what keeps the implementer on the rails across an unattended fleet.

## Why it matters

The plan-only version of this rule leaves the implementer's output unchecked by the model that actually understood the design. The author attributes his fleet workers' reliability to exactly two things: "First, Fable creates the implementation plans, and second, Fable reviews all Opus work."

The distinction from existing cross-model review lessons is that this is *same-vendor tiering with the top model on both ends of one work item*, and the unit is the work item rather than the session. A per-session review lets several items drift before anything checks them.

## How to apply

In multi-agent or unattended pipelines, make the strongest model's review a required stage **per work item**, so each implementation is graded against the plan its own author wrote.

> "Every implementation bead goes through this lifecycle: Fable design, Opus implementation, Fable review.", Steve Yegge

## Related

[[run-maintenance-routines-on-opus-by-default]], [[pair-a-max-claude-plan-with-the-cheap-chatgpt-tier-for-audit-only-codex]], [[author-golden-references-with-strongest-model-replicate-with-cheaper]]
