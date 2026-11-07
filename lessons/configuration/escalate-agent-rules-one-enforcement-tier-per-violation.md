---
id: escalate-agent-rules-one-enforcement-tier-per-violation
created: 2026-08-29
status: active
supersedes: null
category: configuration
source_type: post
tool: [claude-code, codex]
sources:
  - https://yegge.ai/essays/fences-not-sandboxes/
---

# Escalate an Agent Rule One Tier Each Re-Violation: Custom, Warning, Written Law, Then Mechanical Enforcement

## TL;DR

Don't jump every agent rule straight to a hard hook; promote it one enforcement tier each time an agent re-violates it, ending at a program that refuses by policy or alerts loudly.

## Why it matters

Steve Yegge's ~50-agent fleet converged on this graded lifecycle after months of incident postmortems. It keeps the mechanically-enforced surface small (cheap to maintain, less instruction bloat) while guaranteeing that repeat offenders eventually hit a fence rather than another ignored instruction.

## How to apply

Track rule violations from postmortems: a first offense stays a convention, a repeat gets an explicit warning in CLAUDE.md/AGENTS.md, a third becomes binding written law all agents load, and persistent violation gets mechanical enforcement (a hook or policy program that refuses the action, or a tripwire that alerts). This adds the graduated, violation-triggered path to the standing advice to promote critical rules to hooks.

> "Now rules go through a lifecycle, tightening each time they're re-violated: first custom, then advisories/warnings, then written law in the constitution that all agents must obey, and finally, mechanical enforcement: programs that refuse by policy, or observe and alert loudly.", Steve Yegge

## Related

[[let-only-the-strongest-model-talk-to-humans]]
