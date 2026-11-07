---
id: give-a-critique-skill-a-blunt-mode-and-a-professional-mode
created: 2026-08-22
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/sean-kochel/i-cloned-a-billionaire-s-app-idea-system_HUMUXeoWtCk_20260820.txt
---

# Give an Evaluation Skill a Blunt Mode and a Professional Mode You Select at Invocation

## TL;DR

When you encode a critique framework as a skill, expose the delivery tone as a mode argument, so you can ask for the harsh read when you want the truth and the measured read when you need to act on it.

## Why it matters

The creator built Mark Pincus's proven-better-new framework into a skill for evaluating product ideas, and shipped it with exactly two modes because of a behavioural observation: language models "can kind of make you feel shitty about things that you think were good ideas", and the same accurate verdict lands very differently depending on delivery. Making tone an explicit switch is better than fighting it in the prompt each time, because the skill's analysis stays identical while only the presentation changes, and you choose per invocation rather than per skill. His two runs demonstrate it, the same structure (instinct, what is proven, what would be better, what is genuinely new, plus a graveyard of failed attempts, anti-signals and a tensions section) delivered blunt for one idea and professional for another. The tensions section is the part he singles out as most valuable, for example flagging that describing a product as graph RAG is selling a feature rather than an outcome.

## How to apply

When encoding any evaluation or critique framework as a skill, add a mode argument (blunt, professional) that only changes delivery, and pick it at invocation. Structure the skill's output as named sections so the critique is comparable across runs rather than freeform prose. Feed it a specific description of what you are actually building, because output depth mirrors input depth: his vague one-line description produced a surface-level answer and the skill took "MCP server" so literally that it assumed the product was only an MCP server. Extend the research pass to scan your own codebase when the question is about your existing product rather than a hypothetical.
