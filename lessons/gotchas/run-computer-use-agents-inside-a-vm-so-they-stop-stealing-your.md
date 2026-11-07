---
id: run-computer-use-agents-inside-a-vm-so-they-stop-stealing-your
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: [claude-code, codex]
source_type: post
sources:
  - https://x.com/steipete/status/2078318731785359634
---

# Run computer-use agents inside a VM so they stop stealing your keyboard focus

## TL;DR

A computer-use agent driving Chrome and native OS pickers fights you for foreground focus on the host machine, which a VM cleanly solves.

## Why it matters

This is the cost of computer-use that nobody budgets for: the machine becomes unusable for anything else while the agent works, which quietly kills the whole point of running long agent tasks in the background. It is also the concrete reason to prefer API paths, the surrounding post is Steinberger watching Codex drive a GUI purely because "GitHub has no API doesn't stop anyone."

## How to apply

Give computer-use / browser-driving agents their own VM rather than the host desktop; reserve headed host runs for tasks you are actively watching. Pairs with the existing headed-vs-headless guidance, the focus theft is what makes headless or VM-isolated the default.

> "I let my codex run in VMs so they don't steal app focus.", Peter Steinberger
