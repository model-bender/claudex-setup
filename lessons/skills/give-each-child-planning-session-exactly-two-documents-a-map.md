---
id: give-each-child-planning-session-exactly-two-documents-a-map
created: 2026-08-22
status: active
supersedes: null
category: skills
tool: claude-code
source_type: post
sources:
  - https://www.latent.space/p/wayfinder-skill
---

# Give each child planning session exactly two documents: a map and a ticket

## TL;DR

When writing an orchestrator skill, define the child's context as precisely two artifacts, a map of decisions already made, plus one ticket carrying its specific task, rather than handing down a single blob of context.

## Why it matters

The corpus has lessons on giving stateless routines external memory and on persisting plan findings, but not on the shape of the handoff into a spawned planning session. Splitting "what has been decided" from "what you must do" is what lets the map keep growing without inflating every child's prompt.

## How to apply

In the skill, write the running decision record to a single map file and generate one ticket per child session; type the tickets by what the child produces (grilling, prototype, research, and task tickets for anything only the human can do). Each spawned session reads the map for orientation and its own ticket for scope.

> "the first step to that is, what does the grilling session that's being managed need? What does the child need in that situation? So the child probably needs to understand a vague overview of what else is happening, and they need their specific task. So there, you've got two documents. You've got a map — which is all of the rest of the stuff, all the decisions that have already been made. And then you've got the specific ticket that goes into the actual session.", Matt Pocock (interviewed by Latent Space / swyx)
