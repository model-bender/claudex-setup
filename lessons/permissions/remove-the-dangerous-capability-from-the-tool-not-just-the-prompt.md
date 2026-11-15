---
id: remove-the-dangerous-capability-from-the-tool-not-just-the-prompt
created: 2026-11-15
status: active
supersedes: null
category: permissions
tool: [claude-code, codex]
source_type: post
sources:
  - https://ghuntley.com/answer/
---

# Patch the tool the agent calls, not just the prompt: ship a git that has no force push

## TL;DR

Rather than telling the agent not to force-push or blocking it in a hook, remove the capability from the underlying binary. He pins a Nix-patched git without force push for sandboxes and laptops.

## Why it matters

His reasoning is that an agent "hill-climbs toward its goal and does destructive things along the way". A patched binary cannot be bypassed by a different refspec or a shell wrapper. He had Claude write the patch from one prompt: "Can you please use Nix and create a custom overlay that removes force push?"

## How to apply

Where you control the sandbox image or dev environment, pin a git (or other CLI) build without the dangerous subcommand. Elsewhere, use a PreToolUse guard as the weaker version.

> "The best way to stop a model from doing something is to remove its ability to do it.", Geoffrey Huntley

