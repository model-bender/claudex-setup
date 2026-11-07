---
id: have-a-skill-propose-a-new-checker-rule-when-a-draft-fails-for-a-missing-reason
created: 2026-10-02
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/simon-scrapes/everything-you-know-about-skills-is-outdated_e7TY56-yIvM_20261002.txt
---

# When a draft fails for a reason your style guide lacks, have Claude propose the rule and approve it

## TL;DR

At the end of a run, ask Claude to suggest a new rule for any failure the reference doc did not cover. You approve it, it goes into the doc, and later runs are checked against it.

## Why it matters

Simon Scrapes describes this as how the skill starts improving itself: the guide that drafts are checked against grows each time a draft fails for a reason not yet written down.

## How to apply

Add to the skill's final step: if a draft failed for a reason not in the style or voice document, suggest a new rule. Approve the suggestion and have it added to the document, so later runs are checked against it.

Verified: No mechanism claims. The workflow is the creator's; they attribute the model's ability to update skills from what it learns to Anthropic's Fable 5 guide, which was not checked here.

## Related

[[diagnose-and-update-the-smallest-durable-place-after-a-skill-correction]], [[update-brand-voice-file-on-every-manual-correction]]
