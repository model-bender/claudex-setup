---
id: curate-a-bulk-skill-pack-before-installing-not-after
created: 2026-08-07
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/the-5-biggest-lies-you-ve-been-told-about-claude_yGRtK08BdIs_20260807.txt
---

# Before Installing a Downloaded Skill Pack, Have Claude Recommend a Subset Biased Toward Fewer

## TL;DR

Installing someone else's folder of 100 skills at once creates testing debt: skills you have never run, do not understand, and that Claude may start auto-invoking on its own. Upload the pack, ask Claude which ones fit your system, tell it to bias toward less rather than more, then re-audit periodically.

## Why it matters

The creator's framing is that handing someone a skills folder is like handing them a business book and calling their business transformed. The value sits in understanding how a skill integrates into your workflow and what its output should look like, which bulk-installing skips entirely. Anthropic's own guidance is that effective skills start small and get tweaked through real use rather than downloaded wholesale. This is a value and overhead concern distinct from the security one: every extra skill description loads into context on every prompt, and an unvetted skill can silently auto-invoke.

## How to apply

1. Before adding a downloaded skills folder, upload it to Claude and ask which skills would genuinely help given your specific system and workflow, explicitly biasing toward fewer.
2. Install only that recommended subset, not the whole pack.
3. Periodically, not just at install time, run an audit prompt over your current skills directory asking what can be removed and which skills overlap enough to consolidate. Skill count creeps up even when the initial install was curated.

## Related

[[scan-third-party-skills-for-malware-before-installing]], [[skills-complementary-not-overlapping]], [[skill-description-is-routing-logic-not-marketing]]
