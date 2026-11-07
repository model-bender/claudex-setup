---
id: type-api-keys-into-a-local-form-not-the-agent-chat
created: 2026-09-24
status: active
supersedes: null
category: gotchas
tool: [claude-code, codex]
source_type: post
sources:
  - https://simonwillison.net/2026/Sep/20/llm-keys-ui/
---

# Keep API keys out of agent sessions with a local llm-keys-ui web form

## TL;DR

Instead of pasting a secret into an agent chat (Codex Remote or otherwise) to get it onto a remote machine, have the agent launch a throwaway local web form (llm-keys-ui) and enter the key there, then let it read the key back with `llm keys get <name>`.

## Why it matters

This is a different mitigation than the existing "put keys only in a dot-env file" gotcha: that one is about where a key lands once typed; this one avoids ever typing the key into the chat transcript/context at all, which matters most for remote-controlled sessions (Codex Remote from a phone) where the transcript may be logged or shared.

## How to apply

Run `uvx --with llm-keys-ui llm keys-ui --all` (a plugin for Simon Willison's `llm` CLI) and have the agent report back the served URL, including any local-network or Tailscale IP; open that URL yourself to paste the key into the form instead of the chat; the agent then retrieves it later via `llm keys get anthropic` (or any provider name) inside a shell command.

> "I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly. With this plugin, I can tell Codex to run: uvx --with llm-keys-ui llm keys-ui --all Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys. Then later it can use a command like llm keys get anthropic as part of a shell command when it needs to use a key.", Simon Willison

## Related

[[put-api-keys-only-in-dot-env-files]], [[keep-credentials-out-of-the-agent-sandbox]]
