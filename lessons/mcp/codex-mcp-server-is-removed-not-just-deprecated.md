---
id: codex-mcp-server-is-removed-not-just-deprecated
created: 2026-09-13
status: active
supersedes: null
category: mcp
source_type: canonical
tool: codex
sources:
  - https://developers.openai.com/codex/changelog#codex-2026-09-05
---

# Migrate Off `codex mcp-server` Now: It Is Removed, and `app-server` Is Not Production-Supported

## TL;DR

As of 2026-09-05 the `codex mcp-server` command and the standalone binary are gone, not deprecated, and OpenAI marks the `app-server` replacement experimental and unsupported for production.

## Why it matters

The earlier lesson recorded a deprecation, which implied time to migrate. There is none: an integration launching either command breaks on upgrade. The second half matters just as much, because the obvious replacement carries a production caveat the deprecation notice did not.

## How to apply

Grep scripts and automations for `codex mcp-server` and the standalone binary, and move external-server connections to `codex mcp`. Do not build anything production-critical on `codex app-server`. Verified on the installed CLI 0.154.0: `codex --help` shows no `mcp-server` subcommand, while `mcp` and `app-server` (labelled experimental) are both present.

> "The codex mcp-server command and standalone codex-mcp-server binary have been removed after their deprecation on August 24, 2026. Update integrations that launch either command before upgrading Codex. Use the Codex app server for integrations. The app-server command is experimental and isn't supported for production workloads.", Codex changelog, 2026-09-05
