---
id: enable-sandbox-allow-nested-user-namespaces-only-where-a-tool-needs-it
created: 2026-10-25
status: active
supersedes: null
category: permissions
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21305
---

# Turn On sandbox.allowNestedUserNamespaces Only Where a Sandboxed Tool Needs User Namespaces

## TL;DR

Since 2.1.305 a sandbox setting lets sandboxed Linux commands create user namespaces (headless Chromium, rootless podman), and the changelog says it lets them get around the sandbox's file protections, so enable it only in the repo that needs it.

## Why it matters

Browser and container tooling that fails inside the sandbox now has a supported switch, but the same switch weakens the file protections the sandbox exists for, so a blanket user-level setting trades isolation everywhere for a fix in one place.

## How to apply

Set `sandbox.allowNestedUserNamespaces: true` in the project settings of the repo that runs Chromium or podman under the sandbox, and leave it unset in user settings. Checked: the name has 5 matches in the installed 2.1.310 binary, next to the text "lets sandboxed commands get around file deny rules".

> "Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create user namespaces (Chromium, rootless podman); this lets them get around the sandbox's file protections", Claude Code CHANGELOG 2.1.305
