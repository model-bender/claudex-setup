---
id: opus-to-generate-sonnet-to-edit-in-claude-design
created: 2026-07-17
status: active
supersedes: null
category: model-selection
tool: claude-design
sources:
  - transcripts/jono-catliff/how-i-hacked-claude-design-usage-bypass-limits_GPCF1XKYiD8_20260701.txt
---

# Generate on Opus in Claude Design, Then Drop to Sonnet to Edit

## TL;DR

Claude Design has its own model picker. Use Opus 4.7 for the design generation pass where quality compounds, then switch to Sonnet 4.6 for edits, which costs roughly half.

## Why it matters

The generation pass sets the structure everything downstream inherits, so it's worth the strongest model. Edits are small, well-specified deltas where the model choice barely shows, Sonnet costs "two times less tokens" for the same work.

This matters more in Claude Design than elsewhere because there is no audit log and no warning before you run out. One user burned an entire allowance in an hour on the highest plan, then spent $34 more finishing the job.

> **REVISIT (2026-07-17):** the source framed this as a *separate* weekly design pool; [[claude-design-now-bills-your-normal-plan-usage-not-a-separate-quota]] reports the July upgrade moved Design onto normal plan usage (single-source). Either way the model choice is the lever, and if it now shares your Claude Code pool, over-spending here costs you there too, which strengthens rather than weakens the case for dropping to Sonnet on edits.

The picker has offered several Opus generations plus Sonnet and Haiku; reach for Haiku on purely cosmetic edits. The better your design system and upstream spec, the further down you can drop, because the thinking already happened elsewhere.

## How to apply

Pick Opus 4.7 when you create the design or design system.

Once the structure is settled and you're into targeted changes, switch to Sonnet 4.6 for the edit rounds. Pair it with element-pinned comments so each edit is a small, unambiguous delta the cheaper model handles cleanly.

If you're locked out mid-project and must finish, the usage page has an extra-credits toggle with a monthly cap, and the billing page supports auto top-up at a threshold. But the free route is exporting to Claude Code, which draws on a different pool.

## Related

[[pin-claude-design-edits-to-one-element-with-an-exact-value]], [[hand-off-claude-design-exports-to-claude-code]], [[max-effort-is-a-trap-quality-plateaus-at-high]]
