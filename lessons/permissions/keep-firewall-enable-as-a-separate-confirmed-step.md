---
id: keep-firewall-enable-as-a-separate-confirmed-step
created: 2026-11-22
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/tristen-o-brien/claude-fable-5-2-built-my-website-here-s-how-to-actually-put-it-online_usOWZyFSxsA_20261120.txt
---

# Let Claude prepare the firewall but turn it on only after you confirm

## TL;DR

When Claude configures a server, have it set up the firewall rules and leave the firewall off until you say so. A wrong firewall setup can lock you out of your own server.

## Why it matters

In the video Claude finished the go-live work, reported that it had left the firewall off, and offered to enable it on a one-word reply. The creator says that was deliberate, because a misconfigured firewall can lock you out.

## How to apply

In the go-live prompt, say the firewall should be prepared but not enabled without your confirmation. Read what it reports, then tell it to turn the firewall on.

Checked: No mechanism named.

## Related

[[run-a-genuinely-risky-goal-run-on-a-vps-not-your-own-machine]]
