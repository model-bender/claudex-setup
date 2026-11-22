---
id: install-bun-before-setting-up-a-channel-plugin
created: 2026-11-22
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/how-to-put-claude-code-on-a-vps-in-10-minutes_DMdqpLr2DlQ_20261120.txt
---

# Install Bun on the machine before setting up a channel plugin

## TL;DR

The Telegram channel plugin needs Bun. Check for it on a fresh server before starting; having Claude Code and tmux installed does not mean Bun is there.

## Why it matters

On the creator's one-click Claude Code VPS image, tmux was present but `bun` was not found, and the plugin cannot run without it.

## How to apply

Run `bun --version`. If it fails, install Bun (https://bun.sh/docs/installation), then continue with the plugin install.

Checked: Live docs https://code.claude.com/docs/en/channels.md fetched 2026-11-22 with curl: 'Each supported channel is a plugin that requires Bun' and 'Check with `bun --version`'.

## Related

[[vps-tmux-telegram-persistent-sessions]], [[relaunch-claude-code-with-channels-after-configuring-a-channel-plugin]]
