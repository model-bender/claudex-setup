---
id: desktop-app-ignores-byo-model-env-use-the-cli
created: 2026-08-29
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/this-stealth-model-makes-claude-code-free-here-s-how__kK_4cOYF4o_20260824.txt
---

# The Claude Code desktop app overrides BYO-model env settings, route to other providers from the terminal or IDE

## TL;DR

Pointing Claude Code at OpenRouter or another provider via the env block in .claude/settings.json does not work in the desktop app: it overrides those settings and forces a Claude model. Do alternate-provider routing from the CLI or the VS Code extension.

## Why it matters

The whole free/cheap-model routing recipe silently fails for desktop-app users. The settings file is read, but the app forces you back onto a Claude model, so you may think you're on the substitute model while burning subscription usage. The creator states it flatly: "if you're using Claude Code in the desktop app, you can't do this... the desktop app overrides these settings and forces you to use a Claude model." Knowing which surface honors the env routing saves a confusing debugging session.

## How to apply

For any ANTHROPIC_AUTH_TOKEN / base-URL / model-override routing, open the project in a terminal or in VS Code with the Claude Code extension and run sessions there. Confirm the reroute took effect before relying on it: the session header should show the substitute model name (e.g. stealth/ox-alpha), and a statusline configured to display the model shows it too. Keep desktop-app sessions for normal Anthropic-billed work.

## Related

[[route-claude-code-to-cheaper-or-local-models]], [[remote-control-off-with-non-anthropic-base-url]], [[one-launch-alias-per-open-weight-model-via-openrouter]]
