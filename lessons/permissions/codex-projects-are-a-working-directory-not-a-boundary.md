---
id: codex-projects-are-a-working-directory-not-a-boundary
created: 2026-07-17
status: active
supersedes: null
category: permissions
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
  - transcripts/john-kim/complete-beginner-s-guide-to-openai-s-codex-app_20260424.txt
---

# A Codex Project Is a Working Directory, Not a Sandbox: It Will Wander and Reuse Other Projects' Secrets

## TL;DR

Codex working inside one project will still search your whole machine and silently pull artifacts from unrelated projects. In one session it found and reused an API key and channel IDs from a different project's files without being asked. Set the sandbox and approval mode deliberately, and point it at exact paths.

## Why it matters

The project sidebar looks like a boundary and isn't; it's just a working directory. Two costs follow.

**Security:** credentials you scoped to one project leak into another tool's session and end up in code you didn't audit. That matters most when you deliberately keep separate keys per tool for revocation and attribution.

**Efficiency:** letting it hunt for a folder burns tokens crawling your desktop before it finds the right directory, and it may guess wrong between similar-looking ones.

## How to apply

Copy the exact path and paste it rather than describing where a folder lives.

Set the sandbox and approval level explicitly **per project** (read-only, default permissions, or full access) in the project config rather than the user config, and leave new projects on default permissions until the workflow is proven.

When it surfaces a credential from somewhere else, stop and issue a fresh scoped one instead of accepting the convenience.

Real containment still belongs at the environment layer, see [[contain-agents-at-environment-layer-not-permission-prompts]].

## Related

[[contain-agents-at-environment-layer-not-permission-prompts]]
