---
id: scaffold-the-target-framework-before-pasting-the-design-handoff
created: 2026-07-17
status: active
supersedes: null
category: workflows
tool:
  - claude-design
  - claude-code
sources:
  - transcripts/john-kim/how-to-build-an-app-with-claude-code-no-experience-required_20260603.txt
  - transcripts/jono-catliff/claude-code-web-design-10-years-covered-in-66-minutes_2Gda_ZvV1V4_20260701.txt
  - transcripts/jono-catliff/how-i-built-insane-claude-design-websites-in-10-minutes_xYv4_cTOSNM_20260701.txt
---

# Scaffold Your Target Framework Before Pasting the Design Handoff

## TL;DR

Claude Design emits plain HTML and CSS, so scaffold your real stack first and name it in the handoff prompt. The export then gets ported into your framework rather than dumped in as foreign markup.

## Why it matters

The handoff command is a starting prompt, not a spec: it says nothing about your framework, styling system, or libraries. Given an empty folder it will invent a stack.

Given a scaffolded project plus a named target, Claude reads the design source files and translates them, plain CSS into SvelteKit CSS, markup into Svelte 5 components, poster state reconciled into a store, producing a near pixel-for-pixel result you can actually iterate on in your own architecture.

## How to apply

Before pasting anything, set up the project:

> Create an empty project and get the architecture set up for my PRD. I'm using SvelteKit, deploying to Vercel, using OpenStreetMap as the backend API. Set up the foundational boilerplate. I will be pasting the design documents soon.

Then paste the handoff command and append your requirements to the same message, "build this using Next.js and Tailwind, copy it pixel for pixel", or "make sure to build it with SvelteKit in mind".

Append anything else the static export can't carry in the same breath, such as an animation library ("use GSAP to add animations wherever appropriate").

## Related

[[hand-off-claude-design-exports-to-claude-code]], [[hand-off-to-claude-code-from-the-project-root-not-a-page]], [[name-the-real-api-in-the-claude-design-wizard]]
