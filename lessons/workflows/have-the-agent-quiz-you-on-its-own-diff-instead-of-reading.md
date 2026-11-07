---
id: have-the-agent-quiz-you-on-its-own-diff-instead-of-reading
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://registerspill.thorstenball.com/p/joy-and-curiosity-95
---

# Have the Agent Quiz You on Its Own Diff Instead of Reading Every Line

## TL;DR

Review agent-written code by making the agent examine you on it (quiz, diagram, presentation) rather than by scanning the diff line by line.

## Why it matters

Ball admits he does not review each line of what he ships and instead spot-checks architecture; quizzing inverts the review so the gaps in your understanding surface actively, which line-scanning at agent throughput does not. It is a review mode that scales with volume where reading does not.

## How to apply

After a large agent-produced change, ask it to quiz you on the change, to produce a diagram of what moved, or to present the change back to you, and treat the questions you cannot answer as the review findings.

> "You can ask the agent to help you with reviewing by quizzing you, by giving you diagrams, by showing you a presentation.", Thorsten Ball
