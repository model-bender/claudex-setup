---
id: coach-agent-writes-a-candidate-file-beside-the-live-agent-one-change-per-draft
created: 2026-11-22
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/austin-marchese/how-to-build-self-improving-ai-agents-with-claude-stanford-s-method_UUg5oij7ptw_20261122.txt
---

# Have a Coach Agent Write a Candidate Copy Beside the Live Agent, One Change Per Draft, and Keep a Versions Folder

## TL;DR

To improve an agent over time, add a third agent (the coach) that reads the verifier's findings and writes a candidate version next to the live agent file, changing one thing per draft and archiving old versions.

## Why it matters

Austin Marchese says the live file stays constant so you can isolate the variable you changed: if you change eight things you cannot tell which one made a difference. The versions folder gives the coach a history of past agents to learn from.

## How to apply

1. Keep the working agent file (the generator) untouched. 2. Create a coach agent whose rules are: read the verifier's report, write one candidate agent file beside the live one, change one thing only, never touch the answer key or the verifier, keep a versions folder of past agents. 3. Score the candidate against the cases the generator got wrong plus the historical versions before promoting it.

Checked: No mechanism claim (a prompt pattern); this lesson's wording of the coach rules paraphrases the transcript's three rules.

## Related

[[skill-self-improvement-loop-binary-assertions]]
