---
id: give-standing-agents-seats-not-sessions-named-identity-plus
created: 2026-08-22
status: active
supersedes: null
category: agents
tool: claude-code
source_type: post
sources:
  - https://yegge.ai/essays/model-welfare/
---

# Give Standing Agents Seats, Not Sessions - Named Identity Plus Memory That Outlives the Run

## TL;DR

Separate the ephemeral session ("a day in the life of an agent: wake up, do some work, go to sleep") from the durable seat - a named, addressable role carrying its own accumulated history - and attach memory to the seat rather than the session.

## Why it matters

Handoffs, messaging and memory all need a stable referent. If every run is an anonymous session, each handoff is a cold start and there is nothing for accomplishments or corrections to accumulate against; the seat is what makes "resume as this agent" mean anything across days.

## How to apply

Name each standing agent, give it an address other agents can message, and give it a per-seat memory/handoff file that successive sessions read on wake and write on close, so the session is disposable and the seat is not.

> "A seat is a named role with persistent identity (addressability) and history/memory, which accumulates accomplishments over time.", Steve Yegge
