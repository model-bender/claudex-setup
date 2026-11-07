---
id: add-a-codex-interrupt-hook-to-capture-state-on-esc
created: 2026-08-29
status: active
supersedes: null
category: hooks
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/codex/changelog
---

# Add a Codex Interrupt Hook to Capture State When You Cut Off a Running Turn

## TL;DR

Codex 0.150.0 adds an Interrupt hook event, so interrupting a turn no longer has to mean losing state: log partial progress, clean up processes, or persist a handoff note automatically.

## Why it matters

Interruption was previously a blind spot in hook coverage: anything an agent had in flight (background processes, half-written trackers) vanished without a hook point, and automation that assumes turns end cleanly breaks exactly there.

## How to apply

Register an `Interrupt` hook in Codex's hook config pointing at a command or MCP handler that snapshots progress (for example, append to a tracker file or kill orphaned processes) whenever you Esc out of a top-level turn.

> "New Interrupt hooks can run commands or MCP handlers when an active top-level turn is interrupted.", Codex changelog, CLI 0.150.0
