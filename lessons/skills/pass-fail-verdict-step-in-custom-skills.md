---
id: pass-fail-verdict-step-in-custom-skills
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/austin-marchese/17-tricks-to-build-10x-faster-with-claude_ZzHB2mPHb2g_20260724.txt
---

# Add a Pass/Fail Verdict Step to the End of Custom Skills, Not Just Actions

## TL;DR

When writing your own skill (not the built-in /verify), end it with an explicit verdict step that states pass or fail, instead of stopping once the described actions are done.

## Why it matters

The presenter's example is a 'writing-voice' skill that reviews AI output for style: a typical skill says 'do this, then this, then adjust this,' but doesn't tell you if the output actually passed. He argues: 'it's helpful to have a clear final verdict. Did it pass or did it fail?'

## How to apply

At the end of a skill's instructions, add an explicit verdict step, e.g. 'State clearly whether this output passes or fails the [voice/quality/whatever] check, and why,' so the skill's output is a decision, not just a description of what was done.

## Related

[[classify-skills-into-four-types]]
