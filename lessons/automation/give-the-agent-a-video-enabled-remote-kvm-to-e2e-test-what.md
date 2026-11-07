---
id: give-the-agent-a-video-enabled-remote-kvm-to-e2e-test-what
created: 2026-08-22
status: active
supersedes: null
category: automation
tool: [claude-code, codex]
source_type: post
sources:
  - https://x.com/steipete/status/2084988316324397312
---

# Give the agent a video-enabled remote KVM to e2e-test what refuses to run in a VM

## TL;DR

When the feature under test needs real hardware or a weakened OS security posture, a video-enabled remote KVM gives the agent eyes and input on a physical machine instead of a VM.

## Why it matters

It names the exact escape hatch for the case that breaks VM-based agent testing: OS integrations that are unreliable virtualized or that need SIP disabled. The KVM keeps the agent's control surface (video in, keyboard/mouse out) identical to a VM's while the machine under test stays physical and disposable.

## How to apply

Point the agent at a video-capable remote KVM attached to a dedicated physical test box, and keep that box as the only machine with the weakened settings (SIP off). Direct counterpart to the VM-isolation default above: VM when the target virtualizes, KVM to real hardware when it does not.

> "I gave codex a video-enabled remote KVM so it can automate e2e test the iMessage-integration on OpenClaw. (iMessage is unreliable in VMs, and certain features such as read receipts require SIP to be disabled)", Peter Steinberger
