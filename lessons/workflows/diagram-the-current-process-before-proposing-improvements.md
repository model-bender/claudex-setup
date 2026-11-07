---
id: diagram-the-current-process-before-proposing-improvements
created: 2026-09-12
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/the-art-of-becoming-self-educated-with-claude_7DJk83sc5xg_20260910.txt
---

# Make Claude Draw the Current Process as a Mermaid Diagram, Then Challenge Every Step Before Changing Anything

## TL;DR

Before asking for improvements to any existing system or process, have Claude map how it works today end to end as a mermaid flowchart, then walk each node and confirm it matches reality. Only then hand the corrected diagram back and ask what to change.

## Why it matters

Austin Marchese's example is that generic best-practice advice (standard UTM tracking) is simply wrong for a business that deliberately routes links differently, and that suggesting improvements without knowing the baseline is how you lose credibility instantly. He reports clients discovering they did not know how their own systems worked once the diagram was on screen. The diagram is also the artifact that catches the agent's own wrong assumptions about the system before those assumptions turn into a change.

## How to apply

Prompt: 'Map how <process> works today, end to end, as a mermaid flowchart. Include every handoff and every tool involved. Ask me about anything you cannot determine.' Read the rendered diagram and challenge each step out loud: is that actually what happens, in that order? Correct it, then send the corrected diagram back with 'given this baseline, what would you change to solve <constraint>?' Distinct from the architecture-diagram lesson, which orients you inside code; this one establishes a baseline for a process that may not be code at all.

## Related

[[generate-editable-architecture-diagram-to-orient-and-target-the-model]], [[compress-complex-state-into-mermaid-diagrams]]
