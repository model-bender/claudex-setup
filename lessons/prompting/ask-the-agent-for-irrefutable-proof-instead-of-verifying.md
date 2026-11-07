---
id: ask-the-agent-for-irrefutable-proof-instead-of-verifying
created: 2026-08-22
status: active
supersedes: null
category: prompting
tool: claude-code
source_type: post
sources:
  - https://registerspill.thorstenball.com/p/joy-and-curiosity-95
---

# Ask the Agent for "Irrefutable Proof" Instead of Verifying Locally

## TL;DR

When the agent has a sandbox it can install into freely, the two words "irrefutable proof" are the prompt lever that makes it produce the evidence itself, which is what removes the need for your own local dev setup.

## Why it matters

Ball's claim is that the local toolchain became optional, not because the agent got better at coding, but because a proof obligation phrased this strongly makes the agent go build whatever it needs to demonstrate the result. The specificity is in the demand, not the task.

## How to apply

In any sandboxed or container-backed session, end the request with a demand for irrefutable proof that it works, and let the agent install whatever dependencies that requires rather than reproducing the setup on your machine.

> "You can just ask the agent to give you \"irrefutable proof\" that something works and if you have an orb and it can do whatever it wants and install whatever it needs it will find a way to give you that proof.", Thorsten Ball
