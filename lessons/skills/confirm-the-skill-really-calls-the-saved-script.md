---
id: confirm-the-skill-really-calls-the-saved-script
created: 2026-11-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/anthropic-engineer-explains-what-to-build-instead-of-ai-agents_HIRDzMtuWFk_20260920.txt
---

# After saving a script into a skill, run the task twice and confirm the saved file is what runs

## TL;DR

Saving a script into a skill is not done until you have run the same kind of task twice, compared the important parts, and checked the skill is calling the saved file rather than regenerating code.

## Why it matters

The point of the saved script is replacing 'one fresh guess with a proven piece of code'. If the skill still rewrites the code, you kept the variance and the token cost. The surrounding AI output may still vary a little, so compare the parts that matter.

## How to apply

Run the skill on two similar inputs. Compare the important parts of the outputs and check in the tool calls that the saved file was executed, not rewritten.

Checked: No mechanism named.

## Related

[[skills-add-scripts-to-avoid-repeated-api-scaffolding]]
