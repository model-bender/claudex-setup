---
id: pair-remote-control-with-keeping-the-computer-awake-for-long-builds
created: 2026-11-06
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/austin-marchese/7-new-claude-features-to-get-you-ahead-of-99-of-people-using-ai_BgbJFggbTVE_20261106.txt
---

# Use /remote-control Together With a Keep-Awake Setting So Long Local Builds Continue While You Are Away

## TL;DR

Remote control lets your phone drive local sessions, but the laptop must not sleep. Austin points desktop-app users to its keep-awake toggle (plus a separate battery switch); he himself runs a custom terminal command called awake, usually set to 3 hours.

## Why it matters

He prefers local sessions so Claude can edit local files, but builds can take 30 to 40 minutes. Remote control alone fails if the machine sleeps.

## How to apply

1. Type /remote-control in the session.
2. In the Claude desktop app, settings, Claude Code, turn on keep computer awake while Claude works; on a laptop also turn on keep awake on battery power.
3. Or ask Claude to set up an 'awake' terminal command that keeps the machine up for a set time (he uses 3 hours).

Checked: claude 2.1.318: /remote-control 42 hits and --remote-control listed in claude --help. The binary's managed-policy text for keepAwakeEnabled names 'Keep computer awake while Claude works' in Settings, Claude Code (case-insensitive grep), which confirms the desktop toggle. 'Keep awake on battery power' has 0 hits, so the battery switch rests on the speaker.

Inference, not from the source: How the 'awake' command works is not shown; on macOS it would likely wrap caffeinate (named in the binary only inside command-wrapper parsing lists).

