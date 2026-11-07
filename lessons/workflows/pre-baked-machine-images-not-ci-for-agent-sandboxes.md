---
id: pre-baked-machine-images-not-ci-for-agent-sandboxes
created: 2026-08-16
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://hamel.dev/notes/llm/ai-product-engineering/systems-agent-sandboxes.html
---

# Don't Reuse CI/CD as Your Agent Sandbox - Pre-Bake an Image, and Isolate Tools From the Agent

## TL;DR

Once you run agents in parallel, give each one a fast isolated machine built from an image baked on a schedule, rather than bending CI runners into agent hosts.

## Why it matters

CI/CD is the tool most people try first and it is a poor fit: jobs are slow to start and short-lived, while an agent may work on a task for hours or days and edit the dependencies of its own environment mid-run. At volume, startup latency becomes the bottleneck rather than the model.

The separate point is process isolation: "a tool that loads a large CSV and runs out of memory shouldn't kill a long-running agent trajectory." If tools execute inside the agent process, any tool crash costs you the whole run - the expensive part.

Ramp's version bakes the image every 30 minutes, so an agent grabs a ready box, does a `git pull`, and is working in under a second.

## How to apply

Pre-bake the image on a cron with everything installed, so agent start is just a `git pull`. Use a fast sandbox provider - `modal.Sandbox.create(app=app)` plus `sb.exec()` is the hello-world. Run tool execution in a process separate from the agent so a tool crash doesn't end the trajectory.

> "CI/CD (the tool many people try first) is a poor fit. It's slow to start and short-lived, while an agent may work on a task for hours or days and edit the dependencies of its own environment.", Hamel Husain, documenting Adam Azzam's session

## Related

[[cap-bash-memory-with-tool-memory-limit-on-linux]], [[run-tool-execution-in-a-process-separate-from-the-agent]]
