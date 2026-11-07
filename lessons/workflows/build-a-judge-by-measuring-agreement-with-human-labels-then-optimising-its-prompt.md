---
id: build-a-judge-by-measuring-agreement-with-human-labels-then-optimising-its-prompt
created: 2026-10-11
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-actually-build-sell-software-with-ai-as-a-non-techie_l8ywUsEJ2XQ_20261009.txt
---

# Calibrate an LLM judge against about 100 human-labelled examples and optimise its prompt until agreement is high

## TL;DR

Dave, a guest on Nate's channel) says to have a human review around 100 outputs, measure how often the judge agrees, then have an LLM rewrite the judge prompt in rounds and re-check occasionally for drift.

## Why it matters

Subjective outputs have no single right answer, and an unchecked judge only moves the checking problem. Agreement as a percentage (his example 50 or 80 percent as baseline, rising to 95 or 99) gives a measurable target.

## How to apply

1. Collect about 100 examples and have a human mark each good or bad. 2. Run the judge (a system prompt and model) over them and compute agreement. 3. Give the human and judge labels to an LLM and ask it to improve the judge system prompt. 4. Repeat until agreement is high. 5. Re-run now and then to catch drift, and again after switching model.

## Related

[[error-analysis-before-llm-judge-no-blanket-score]]
