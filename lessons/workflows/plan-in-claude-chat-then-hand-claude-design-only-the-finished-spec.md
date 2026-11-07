---
id: plan-in-claude-chat-then-hand-claude-design-only-the-finished-spec
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool: claude-design
sources:
  - transcripts/nate-herk-ai-automation/claude-design-2-hour-course-beginner-to-pro_ovabeVoWrA0_20260626.txt
---

# Do the Thinking in Claude Chat and Hand Claude Design Only a Finished Spec

## TL;DR

Never brainstorm, research, or outline inside Claude Design. Do it in a regular Claude chat, make it emit a markdown spec, then attach that file to the Design project and let Design do nothing but render it.

## Why it matters

Design's job is generation. Every ideation round you run there is paid for in the expensive surface while producing nothing visual, "don't ever brainstorm in Claude Design, there's just no point."

A whole brand, a 372-line pitch-deck outline with market research, and an 804-line mobile-app spec were all ideated in plain Claude chat, then one-shotted in Design. The extra input tokens for a long attached spec are far cheaper than output tokens spent building down the wrong path.

Regular Claude will try to build the artifact itself, so you have to stop it.

## How to apply

In claude.ai chat, brainstorm the concept, do the market research, and ask for the structure. When it starts producing the artifact, interrupt:

> You don't need to build the deck, just give me a markdown outline so I can put this into Claude Design.

Download or copy the markdown, open the Design project with your design system selected, attach the markdown (long pastes land as a text artifact), and prompt one line:

> I dropped you 804 lines of spec, you already have the design system, go build it, ask if you have questions.

Treat each Claude surface as a specialist: chat for research and outlines, Design for pixels.

## Related

[[precompute-the-design-system-outside-claude-design]], [[export-and-restart-instead-of-iterating-in-one-long-claude-design-thread]], [[keep-the-claude-design-brief-open-enough-to-trigger-its-question-round]]
