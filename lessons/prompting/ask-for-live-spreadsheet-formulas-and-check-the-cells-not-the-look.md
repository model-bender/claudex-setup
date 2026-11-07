---
id: ask-for-live-spreadsheet-formulas-and-check-the-cells-not-the-look
created: 2026-10-02
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/nate-herk-ai-automation/i-tested-opus-5-5-vs-gpt-6-astra-on-12-real-use-cases_GmLcJVzkxPA_20261002.txt
  - transcripts/nate-herk-ai-automation/i-tested-sonnet-5-5-vs-opus-5-5-what-you-need-to-know_7eo-11K2e3c_20261002.txt
  - transcripts/austin-marchese/stop-typing-in-claude-press-record-instead_FI4NdYXltA4_20260807.txt
---

# Ask for Live Formulas in Generated Spreadsheets and Click Into Cells to Check Them

## TL;DR

A generated spreadsheet can look right while holding typed values instead of formulas, whether it came from a prompt or from a skill built by screen-recording the task. Ask for live formulas, click into cells to check them, and change one input to confirm the outputs recalculate before you trust it.

## Why it matters

The creator (Nate Herk) says they dislike AI-made Excel files that are all static data, because any change then means asking the agent to regenerate the file. In an Opus 5.5 vs Astra test from the same data, they found Opus's financial report had "way more references, more formulas", while Astra's had only some basic sums and not in all cells, though the two looked similar. In a separate Opus vs Sonnet 5.5 test they found formulas "basically everywhere" in Opus's workbook, so "the whole sheet would update". These are one creator's observations.

Recorded skills hit the same failure through a different route. A skill built by screen-recording a spreadsheet task (a Claude Cowork recording demo) replaced live SUMIF/COUNTIF formulas with static typed-in numbers. The skill made the right decision but rebuilt the artifact through a lossy mechanism, typing computed values instead of writing the formula, because from the recording's point of view those are indistinguishable. A human glancing at the sheet sees correct numbers and ships it, and the breakage only surfaces later, when the data refreshes and nothing recalculates. The same applies to any generated file with links, live queries or other non-static content (linked docs, templated slides).

## How to apply

State in the prompt, or in the skill, that every calculated cell must be a formula referencing an inputs sheet, with no pasted values (this step is the lesson's own advice; the creator only inspected outputs). After the run, do not eyeball the rendered output: click into several cells on each tab (totals, ratios, forecasts) and confirm the formulas and bindings survived, not just their current computed value. If they did not, tell the agent or skill explicitly to write the formula or reference rather than a literal value. Then change one upstream input and confirm the outputs recalculate.

Verified: Prompt-and-inspect technique, no tool mechanism to verify. Model comparison claims are the creator's observation on one prompt.

## Related

[[retest-a-recorded-skill-on-changed-inputs-not-the-demo-case]], [[record-a-narrated-screen-demo-to-author-a-cowork-skill-for-ui-only-software]]
