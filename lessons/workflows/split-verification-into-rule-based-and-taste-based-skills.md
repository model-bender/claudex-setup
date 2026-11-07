---
id: split-verification-into-rule-based-and-taste-based-skills
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/boris-cherny-s-4-step-playbook-to-10x-your-ai-productivity_clDlAmHsiKw_20260820.txt
---

# Codify Two Verification Skills, One Rule-Based and One Taste-Based, Before Running Agents in Parallel

## TL;DR

The blocker on going from one supervised agent to five is that you are the verifier; fix it by building two skills the agent runs on itself, a rule-based one for objectively checkable output and a taste-based one for judgement calls.

## Why it matters

Boris Cherny's stage-one bottleneck is stated as "your attention and the need to inspect each response and code edit due to low trust for the model's output and lack of self-verification. You feel you must read everything, so you never look away." Parallelism does not help while every output funnels back through your eyes, so a non-human verifier is the precondition for stage two, not a nice-to-have. The split matters because the two check types are built differently: rule-based checks are pass/fail and can be automated outright (in code that is lint, tests, type check; outside code it is "does the report use the correct colors, the right fonts, does the text use em dashes", or a domain's quantifiable regulations for an engineering firm), while taste-based checks ("does the design look good", "is the writing concise", "does that content idea pass a quality bar") have to be trained with your own examples and tuned over time. The video's creator ships his taste-side version as an "anti-slop" skill and treats it as the favourite of the two.

## How to apply

Create two skills rather than one verification prompt. For the rule-based skill, enumerate the objective checks for your domain and make them runnable by the agent, so it iterates until green before handing back. For the taste-based skill, seed it with concrete context about what you are working on and what good looks like, then correct it each time it passes something you would have rejected, treating it as a thing you optimise over time rather than write once. Attach both to the work that runs unattended, so parallel agents return finished output instead of intermediate steps. Pair with permissive-but-bounded permissions (auto mode) so the agent can actually run the checks without stopping for approval on every step.
