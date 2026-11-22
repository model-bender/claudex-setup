---
id: make-a-vps-remote-control-session-start-on-every-boot
created: 2026-11-22
status: active
supersedes: null
category: remote-access
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-fable-5-2-built-my-website-here-s-how-to-actually-put-it-online_usOWZyFSxsA_20261120.txt
---

# On a VPS, ask Claude to make claude remote-control restart automatically, or the phone connection dies with the terminal

## TL;DR

Remote Control on a server only works while its terminal process runs. After starting it, ask Claude on the server to make it permanent so it launches whenever the server boots.

## Why it matters

The video starts remote control in the host's browser terminal, connects from the Claude phone app's code tab, and notes the link is lost if the terminal stops.

## How to apply

On the server run claude remote-control with --name set to a label you will recognise (the video names it after the project, barbershop), confirm it connects in the Claude app's code tab, then prompt Claude to make it start on every server boot. The transcript does not include the prompt text or the method; a systemd service or similar is this lesson's inference.

Checked: Checked 2026-11-22 on Claude Code 2.1.330: claude remote-control --help lists --name and says to keep the command running or the session stops. The auto-start method itself is not given in the video and was not tested.

