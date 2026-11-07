---
id: env-file-keys-portable-across-hosting-targets
created: 2026-09-24
status: active
supersedes: null
category: gotchas
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit_FqnNL8fnUWo_20260920.txt
---

# Keep API Keys in a Plain .env File Instead of Platform Plugin Connections, So They Move With the Automation

## TL;DR

Codex's connected-account plugins do not transfer when you move an automation to a different host, so keys authorized that way have to be redone from scratch on the new platform. Keep raw API keys in one .env file instead, so moving an automation to a different host or tool is a copy-paste rather than a re-authentication.

## Why it matters

Building an automation inside Codex using its native plugin connections works fine until you need to host that automation somewhere else (an external runner, or a different agent tool entirely); the plugin's stored authorization is specific to Codex and does not carry over, forcing you to re-connect every account on the new platform.

## How to apply

When wiring up a new API for an automation you might later move (to another host, or another agent tool), skip the platform's native plugin/OAuth connector and put the raw API key in a .env file instead. When you move the automation, copy the .env values across rather than re-authorizing each connection on the new platform.

## Related

[[put-api-keys-only-in-dot-env-files]]
