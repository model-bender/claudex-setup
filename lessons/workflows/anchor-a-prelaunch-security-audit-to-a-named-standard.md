---
id: anchor-a-prelaunch-security-audit-to-a-named-standard
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Anchor the Pre-Launch Security Audit to a Named Standard and Make It Separate Human-Only Items

## TL;DR

Before an agent-built app takes real users, run a read-only audit whose prompt cites an explicit standard (the OWASP LLM top-10 repo) rather than asking for 'a security check', and require the report to split agent-fixable findings from the ones only you can do.

## Why it matters

A generic 'check this for security issues' returns generic reassurance. Auditing against a published checklist gives the agent something to enumerate. On an app with authentication and Stripe payments already wired, this pass returned four high-severity release blockers plus a critical configuration condition to rule out before deployment, and Nate's honest assessment was that finding these himself would have required a talented human engineer. The report structure did as much work as the findings: it listed what passed (so you know it didn't just drop the ball), what was blocked, and what a human still had to do - flip demo mode off, rotate the Anthropic key, swap the Stripe test keys for live ones. Functional QA had already passed on this same codebase; a security pass is a different lens, not a stricter one.

## How to apply

Clear the session, paste the standard's repo URL into the prompt along with a short statement of where the app is ('V1 is done, we're about to onboard customers, auth and payments are live, you're in the folder'), and ask for a read-only audit against that standard covering the vectors you care about - tenant isolation, prompt injection, data leakage, throttling. Read the report before authorising anything. Then hand the findings back as a `/goal` fix run: 'spin up a team of agents, one specific task each, you are the verifier, don't stop until you're 100% confident every vulnerability is resolved; write and run tests; if something is blocked on me as a human, leave it to the end and list it.' That run reported 7/7 on tenant-isolation attacks plus webhook, migration, and PDF checks. Repeat it periodically - Nate's stated cadence is weekly as users join and the codebase grows.

## Related

[[rotate-dev-exposed-keys-before-production]]
