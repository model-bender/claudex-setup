---
id: batch-alignment-questions-instead-of-round-by-round
created: 2026-08-16
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://x.com/swyx/status/2088073777779515615
---

# Have Your Alignment Skill Ask Questions in Batches, Not Round by Round

## TL;DR

Modify your self-interview / alignment command to emit 2-10 questions at once instead of one per turn - the speculative-decoding intuition applied to the human in the loop.

## Why it matters

This is a direct refinement to the "grill me" self-interview skill already in the corpus. Round-by-round questioning makes *you* the latency bottleneck: every question costs a full turn of your attention, so a 20-question interview is 20 context switches. Batching collapses N round-trips into one without losing the alignment benefit, because the questions were rarely dependent on each other in the first place.

Reported to work especially well for design exploration, where the question set is wide and shallow rather than deep and sequential.

## How to apply

Edit the skill or command prompt to say "ask 2-10 questions per round, all at once", and answer them in a single reply.

> "human i/o is costly, so after listening to @mattpocockuk and @trq212 i made an /align-me modification which allows for batches of questions instead of round-by-round. same intuition as spec decoding, you speed up by looking ahead 2-10 steps", swyx

## Related

[[self-interview-skill-to-extract-tacit-knowledge]]
