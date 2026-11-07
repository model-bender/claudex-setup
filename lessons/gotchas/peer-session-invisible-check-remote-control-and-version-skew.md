---
id: peer-session-invisible-check-remote-control-and-version-skew
created: 2026-08-16
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-just-made-subagents-feel-obsolete_oqp6D-ugtX4_20260810.txt
---

# A Peer Session Can Be Invisible for Two Boring Reasons: Remote Control Off and Version Skew

## TL;DR

When `ListAgents` does not show a session, or a message never lands, check the two prerequisites before assuming the feature is broken: remote control must be enabled for a session on another machine, and sessions running an older Claude Code build report as unreachable.

## Why it matters

Both failures are silent and both look like the feature itself is broken. In the demo, a message to a Claude session on a remote server did nothing at all until remote control was turned on - after which the session appeared in `ListAgents` and the identical message went straight through.

The version-skew one has a nasty selection effect: on a machine running many long-lived sessions, a large share were unreachable purely because they had been started before the last upgrade. The sessions you most want to reach - the old, long-running ones holding hours of context - are exactly the ones that silently drop out of the pool.

## How to apply

Enable remote control on the target machine before expecting to reach it, at user scope, and `/rename` the session so you can address it. Restart long-lived sessions after upgrading Claude Code if you want them messageable.

Also note the receiving session's own permission mode gates the work: an inbound peer message arrives as "message from peer", and the command it triggers still hits that session's approval prompt. Put a peer that should act unattended into auto mode.

## Related

[[name-your-sessions-so-they-can-message-each-other]], [[wrap-your-terminal-cli-in-a-skill-so-claude-code-spawns-peer-sessions]], [[cross-session-sendmessage-spans-machines-but-holds-for-approval]], [[remote-control-can-no-longer-be-enabled-from-repo-settings]]
