---
id: low-effort-fable-answers-from-memory-instead-of-searching
created: 2026-09-12
status: active
supersedes: null
category: model-selection
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-anthropic-actually-prompts-fable-5-1_FBVNS1l5Vb8_20260910.txt
---

# Do Not Drop Fable 5.1 to Low Effort for Research, It Stops Calling Search Tools

## TL;DR

Anthropic's prompting docs note that at low effort Fable 5.1 is less likely than Fable 5 to call a search or retrieval tool and more likely to answer from memory. Keep low for ideation and brainstorming, not for anything that has to be looked up.

## Why it matters

Low effort reads as a pure cost dial, so people drop to it for cheap turns and get answers that sound the same but are no longer grounded in a fetch. The tool-calling behaviour changes with the dial, not just the depth of reasoning, which means a research task at low effort fails silently.

## How to apply

Reach for low when you want the Fable 5.1 feel on ideation, brainstorming and drafting. Move back up when the turn depends on retrieval, or state the tool call explicitly in the prompt so it is not left to the model's inclination.

## Related

[[max-effort-is-a-trap-quality-plateaus-at-high]], [[sharpen-the-spec-before-reaching-for-more-effort]], [[route-long-projects-to-fable-and-single-prs-to-opus-5-medium]]
