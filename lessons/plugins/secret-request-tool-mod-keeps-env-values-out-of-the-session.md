---
id: secret-request-tool-mod-keeps-env-values-out-of-the-session
created: 2026-10-19
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/ray-amjad/most-claude-code-mods-are-toys-these-are-for-agentic-engineers_Od9706XIXcc_20261013.txt
---

# Register a request-secret Tool in a Mod So Keys Go Straight to a Disk File Claude Cannot Read

## TL;DR

A mod can register a request_secret tool: when Claude needs a key it opens a pane, you type the value there, it is saved to a protected env folder, and Claude only ever sees a redacted placeholder, so the real value never lands in the transcript.

## Why it matters

Ray Amjad uses this to manage many API keys: the secret is not in the session transcript or sent to Anthropic, and requests are made through a placeholder (he compares it to a proxy that swaps in the real credential). He also describes storing secrets in an external vault instead of a local env folder.

## How to apply

1. Ask Claude to build a mod that registers a request-secret tool and a pane for entering the value. 2. Save to an env folder your deny rules stop Claude from reading. 3. Let requests use the redacted ID. Treat the 'never leaves your machine' property as something to test yourself. Checked: claude 2.1.303 binary: plugin API lists 'tool.register'; no 'request_secret' string exists, so that tool name is the speaker's own mod, and the security properties are untested.

## Related

[[redact-secrets-before-they-enter-the-transcript]], [[type-api-keys-into-a-local-form-not-the-agent-chat]], [[keep-credentials-out-of-the-agent-sandbox]]
