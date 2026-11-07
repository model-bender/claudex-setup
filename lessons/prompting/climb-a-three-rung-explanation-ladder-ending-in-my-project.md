---
id: climb-a-three-rung-explanation-ladder-ending-in-my-project
created: 2026-09-12
status: active
supersedes: null
category: prompting
tool: claude-code
sources:
  - transcripts/austin-marchese/the-art-of-becoming-self-educated-with-claude_7DJk83sc5xg_20260910.txt
---

# End Every 'Explain This' Prompt With 'In Terms of the Project I'm Already Working On'

## TL;DR

When learning an unfamiliar concept inside a session, ask for it at three escalating rungs: explain it like I'm 5, 12 or 18; then give me a level-two analysis of why it matters here; then explain it in terms of what I am already working on and already understand. The third rung is the one that pays, because the agent already has your repo and your files loaded.

## Why it matters

Austin Marchese frames the agent as a stateful tutor rather than a stateless one: a substitute teacher gives the generic textbook answer, a full-time teacher knows what you already do. An explanation that stops at the generic rung leaves you to do the mapping onto your own codebase by hand, which is exactly the step where an unfamiliar concept is misapplied. He showed it on a design-interfaces topic explained at a named age with a sport analogy, then re-anchored to the work in front of him.

## How to apply

In the same session that already has your project context, run three prompts in order: 1) 'Explain <topic> like I'm 12, using a <domain you know> analogy.' 2) 'Now give me a level-two analysis of <topic> and why it matters for what I am building.' 3) 'Now explain <topic> in terms of the code and constraints in this project and what I already understand.' Do not open a fresh context for rung three, the value comes from the loaded project context. Pair with an existing clarify step if the agent lacks context to answer.

## Related

[[spec-developer-workflow-with-clarifying-questions]], [[request-post-tool-summaries-to-learn-from-claude]], [[learn-technical-vocabulary-for-precise-prompts]]
