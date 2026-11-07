---
id: is-demo-masks-the-email-on-screen-not-in-the-system-prompt
created: 2026-09-12
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - https://github.com/anthropics/claude-code/issues/81138
---

# IS_DEMO=1 Hides Your Email in the UI, Not in the System Prompt

## TL;DR

IS_DEMO=1 masks your account email and org in the header and in outputs, but it does not remove the `# userEmail` block from the system prompt, so a session recorded with it still leaks the address to anyone who gets the model to repeat its system prompt.

## Why it matters

IS_DEMO is recommended in the corpus as the screen-recording safety switch, which is exactly the assumption this corrects: the masking is presentational. The only code path that omits the block is having ANTHROPIC_UNIX_SOCKET set, so on a normal install the address is in the prompt on every session regardless of the flag.

## How to apply

Treat IS_DEMO=1 as protection against a viewer reading your email off the screen, not against the model disclosing it. Before publishing a recording or sharing a transcript, check for a `# userEmail` block, and never let a demo session dump or paraphrase its own system prompt.

## Related

[[your-account-email-is-in-the-system-prompt-every-session]]
