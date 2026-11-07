---
id: formally-verify-race-prone-code-with-lean-or-tla
created: 2026-09-24
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://x.com/bcherny/status/2102543349102338309
---

# Point Claude at Lean (or TLA+) to formally verify a tricky state machine, not just review it

## TL;DR

For race-prone or state-machine-heavy code, ask Claude to formally model it in Lean (or TLA+) and hunt for counter-examples instead of doing a plain code review; Cherny got 16 bug/race-condition fixes on the Claude Agent SDK from a couple of prompts.

## Why it matters

this targets the bug class normal review and testing miss (concurrency, data flow, state management), and the prompter does not need to know Lean or TLA+ himself, Claude carries the formal-methods expertise.

## How to apply

in a follow-up post (https://x.com/bcherny/status/2102898067133595992, 2026-09-23) Cherny describes the actual loop: Claude builds a model of the program targeting a tricky/race-prone part, finds counter-examples in the model (suspected bugs), reproduces them, then fixes the code. You do not need to formally verify the whole codebase, just point it at the hairiest module.

> "I used Opus 5.5 to formally verify the Claude Agent SDK using Lean. A couple short prompts = 16 PRs fixing various bugs and race conditions. Video attached. TLA+ also works well. I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt. I don't know either language well, but Claude is excellent at both.", Boris Cherny (@bcherny)
