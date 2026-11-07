---
id: tag-reverse-engineering-findings-as-seen-inferred-or-unknown
created: 2026-10-19
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tested-the-viral-reverse-engineer-anything-skill-what-you-need-to-know_rL5tw6h78zo_20261013.txt
---

# Have the Agent Tag Every Finding From a Teardown as Seen, Inferred or Unknown

## TL;DR

When an agent studies an existing app to rebuild a feature, make it label each finding: seen (found and cited), inferred (the evidence points that way, a guess) or unknown (could not be observed), so you do not build on guesses as if they were facts.

## Why it matters

Nate Herk says the 'inferred' bucket is the important one: accepting an assumption and building on it as fact gets messy. In the Loom teardown, for example, 11 native add-ons were 'seen', while things the recorder hid were 'unknown'. This is what makes it more structured than telling Claude to 'research it and build it'.

## How to apply

1. Add to the teardown prompt: tag each finding seen (with a citation), inferred or unknown. 2. Review the inferred list before building. 3. Rebuild, then run test cases and iterate rather than shipping the first pass. Checked: no tool mechanism is named (the technique is prompt-level, from the Reverse Engineer Anything repo, which was not inspected); the three tag names are the repo's as described by the speaker.

## Related

[[require-an-exact-quote-and-source-for-every-rule-extracted-into-an-agent]], [[point-codex-computer-use-at-the-app-youre-cloning]]
