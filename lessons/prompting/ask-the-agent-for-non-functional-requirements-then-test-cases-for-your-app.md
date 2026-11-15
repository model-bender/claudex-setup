---
id: ask-the-agent-for-non-functional-requirements-then-test-cases-for-your-app
created: 2026-11-15
status: active
supersedes: null
category: prompting
tool: [claude-code, codex]
sources:
  - transcripts/john-kim/building-apps-with-ai-is-hard-until-you-learn-this_8fvUXkotDPc_20261108.txt
---

# Ask your agent for non-functional requirements that fit your app, then tests and agentic evals for them

## TL;DR

After the feature work, have the agent list reliability, performance, accessibility and security requirements suited to your app type, build test cases for them and run them, because agents rarely check these unprompted.

## Why it matters

The author found large-text clipping and a puzzle lost when the app was backgrounded mid-save, and names an image loaded at 10 times the viewport size as a very common bug of this kind. He says agents will not fix these unless you steer them.

## How to apply

Prompt: give me non-functional requirements that fit the context of my app, state your app's architecture (his was mostly client side), and talk through them. Then ask it to write test cases for them and run agentic evaluations on those. Add a separate prompt asking what security measures are in place and for a security health check. Run it after QA and before deployment.
