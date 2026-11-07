---
id: publish-the-design-system-before-starting-a-prototype
created: 2026-08-31
status: active
supersedes: null
category: gotchas
tool: claude-design
sources:
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
  - transcripts/tristen-o-brien/claude-design-basics-master-95-in-10-minutes_20260610.txt
---

# Publish the Claude Design System Before Starting a Prototype, or It Won't Be Selectable

## TL;DR

An unpublished design system cannot be attached to a new prototype. Finish the review queue, publish, and confirm the system's chip appears in the prompt box before you generate anything.

## Why it matters

If you start the prototype first, the system is simply absent from the picker, so generation falls back to Claude's own palette and font choices and the output reads generic. You only discover the miss after burning a generation run.

## How to apply

In design systems, work through the approve/reject review queue and publish. Then, when starting a prototype, select the system and check that its chip shows in the prompt box before sending the prompt.

## Related

[[seed-design-system-with-a-real-brand-kit]]
