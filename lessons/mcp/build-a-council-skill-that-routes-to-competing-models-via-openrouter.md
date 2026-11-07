---
id: build-a-council-skill-that-routes-to-competing-models-via-openrouter
created: 2026-07-10
status: active
supersedes: null
category: mcp
sources:
  - transcripts/mark-kashef/you-ve-never-used-claude-code-skills-like-this_EeX7ovArylU_20260703.txt
---

# Build a 'Council' Skill That Routes to Competing Models via OpenRouter for Task-Matched Second Opinions

## TL;DR

Package a /council slash-command skill that, without leaving Claude Code, sends the current problem to competing models through OpenRouter - a config file maps task types to models (bug-fix -> Codex, front-end -> Gemini Pro, quick-check -> Gemini Flash) - then Claude labels each model's raw response, states where it agrees/disagrees, and executes the best synthesis.

## Why it matters

Instead of picking one 'best' model you tap each model's different blind spots on demand mid-task, and a reusable skill with an editable routing map lets even a non-technical user just say 'get a second opinion / ask Gemini / ask Codex' and get cross-model review that Claude arbitrates rather than blindly follows. Distinct from the Codex-only second-opinion mechanisms because any OpenRouter model is routable and the routing is task-typed (and you can poll Haiku/Sonnet/Opus on the same task the same way).

## How to apply

Put an OpenRouter API key in .env; give the skill trigger phrases ('get a second opinion', 'ask Gemini/GPT/Codex', 'consult') plus a rule to never call external APIs without your intent; store the routing in a config file (a default model per task category) plus context-packaging rules (always send the problem statement, the relevant code snippets, and what has already been tried) and synthesis rules (present each model's labeled response, state agreement, then execute the path of least resistance).
