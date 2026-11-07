---
id: rotate-dev-exposed-keys-before-production
created: 2026-08-31
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Rotate Any Key the Agent Used During Development Before It Becomes the Production Key

## TL;DR

Before launch, rotate every API key and secret the agent handled while building (regenerate the Anthropic key, swap Stripe test keys for live ones, refresh service-role secrets) instead of promoting the development values to production.

## Why it matters

During an agent-driven build the agent reads and writes your secrets repeatedly, across env files, terminals, and platform environment stores, so by launch the working keys have been handled many times. Two independent build workflows in the archive end on the same human-only step: rotate the keys the agent saw before onboarding real users.

## How to apply

Make key rotation an explicit pre-launch checklist item: regenerate any key used during development, swap test keys for live ones yourself, and update the deployment's environment store with the fresh values. Treat it as a human-only task the agent lists for you rather than performs.

## Related

[[authenticate-vendor-clis-so-the-agent-owns-the-deploy-plumbing]], [[anchor-a-prelaunch-security-audit-to-a-named-standard]]
