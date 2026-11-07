---
id: fix-one-noun-per-entity-in-a-skill-before-writing-it
created: 2026-08-22
status: active
supersedes: null
category: skills
tool: claude-code
source_type: post
sources:
  - https://www.latent.space/p/wayfinder-skill
---

# Fix one noun per entity in a skill before writing it, inconsistent naming causes strange behavior

## TL;DR

Name each entity in a skill once (map, ticket, session) and use that exact word everywhere in the file, because reusing one word for several things or one thing under several words degrades the agent's behavior.

## Why it matters

The existing terminology lesson is about echoing the agent's vocabulary back in your prompts and building a repo glossary; this is the authoring-side rule for skill files, where a single overloaded noun silently produces confused entity modelling rather than an error you can see. It also reframes what a skill is: "because that's really what a skill is, you're managing the context of the agent you're working in."

## How to apply

Before writing the skill body, list the entities it manipulates and assign each exactly one leading word. Grep the finished skill for each word to confirm it is never used for a second concept, and keep the same dictionary across all your skills so they share assumptions.

> "if you just call everything a ticket, or if you just refer to it in different ways in different places, then it's going to be really confused and you're going to get strange behavior. Whereas if you use these very specific, what I call leading words, to lead the agent to understand exactly what each part is, and you've understood what the information flow is, then you've got your skill.", Matt Pocock (interviewed by Latent Space / swyx)
