---
id: name-the-animation-technique-instead-of-asking-for-an-animation
created: 2026-10-02
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/how-to-use-codex-to-create-beautiful-app-animations_f-Ar8mwm3kQ_20261002.txt
---

# Steer animation work by naming the technique and keep a cheat sheet you can paste to the agent

## TL;DR

A bare 'make animations' prompt gives weak results. Naming keyframes, springs, easing, SVG path, layout transitions, shaders or particles lets you direct and debug the work.

## Why it matters

John Kim says that telling Claude Code or Codex to 'go make animations' will never give the quality of their puzzle app, because AI cannot tell what feels good. Their techniques: keyframes, springs and easing (CSS easing site), gesture, physics, SVG path, shaders, layout transitions, particles, sprites, Rive or Lottie. They made a cheat sheet of when to use each. Knowing the vocabulary lets you diagnose: a button that feels wrong needs a different easing, crooked morph edges mean a rough SVG path with too few points.

## How to apply

Write a short table of techniques and when to use each, and paste it into the agent. Ask for named techniques: 'spring on the button press, layout transition to the grid, particles on completion'. When something feels off, name the likely cause (easing, path smoothness) in the follow-up.

Verified: Prompt technique, no tool mechanism claimed. Easing and spring terms are source-stated design vocabulary.

## Related

[[name-gsap-for-claude-code-scroll-animations]]
