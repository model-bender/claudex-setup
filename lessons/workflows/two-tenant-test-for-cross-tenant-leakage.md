---
id: two-tenant-test-for-cross-tenant-leakage
created: 2026-09-01
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Ask a Verifier Agent to Run a Two-Tenant Test for Cross-Tenant Data Leakage

## TL;DR

Before launch, have a verifier agent create two separate tenant/user accounts and specifically test whether one can see or affect the other's data.

## Why it matters

Codex's security pass explicitly ran this as a distinct check: 'it's running a two tenant test and it's testing things out... this is being treated as a read-only security review.' This caught issues a generic 'test the app' pass would likely miss, since single-account smoke tests never exercise cross-account isolation.

## How to apply

When briefing a security/QA agent on a multi-tenant SaaS app, explicitly ask it to sign up two separate accounts and attempt to read, modify, or list the other account's data (projects, decks, billing, etc.) as a named test, not just a generic functional pass.

## Related

[[anchor-a-prelaunch-security-audit-to-a-named-standard]], [[give-agents-a-local-mock-dev-env-instead-of-prod-credentials]]
