---
id: wire-cloud-scheduled-tasks-through-connectors-not-local-files-or-keys
created: 2026-07-17
status: active
supersedes: null
category: automation
sources:
  - transcripts/simon-scrapes/claude-cowork-just-went-fully-hands-off-scheduled-tasks-v2_b3OiEUp1GIU_20260716.txt
  - transcripts/tristen-o-brien/claude-cowork-for-mobile-just-dropped-master-it-in-8-minutes_-ZSmeJUJbiU_20260712.txt
---

# Cloud Scheduled Tasks / Cowork Run Sandboxed: Reach Data via Connectors, Not Local Files or Pasted Keys

## TL;DR

The no-setup cloud scheduled tasks and Cowork tier runs in a destroyed-after-run sandbox that can't touch local files, CLIs, or secrets and won't act on an API key pasted into the prompt, so wire every app through a built-in/OAuth connector (or Composio's MCP, or a self-hosted remote MCP) and move any needed files into Google Drive.

## Why it matters

These tasks run on Anthropic's cloud on your existing subscription, so they reach cloud connectors (Gmail, Drive, Notion, accounting apps) but not your laptop's files, local MCP servers, browser-use, or computer-use. Encrypted env-var secrets live in the more technical managed-agents/developer routines product, not this simple tier, so scheduled-tasks/Cowork is effectively connector-only, and a job that truly needs local files or raw keys has to run locally instead, defeating the point of cloud scheduling.

## How to apply

In the desktop app, connect apps under Settings → Connectors (built-in or one-click OAuth). For an app that isn't listed, use Composio's MCP (many apps, one-click OAuth, a free monthly request tier, and multiple accounts of one service, e.g. several Gmail inboxes, through one server) or host your own remote MCP and add it as a custom connector by URL. Move local working files into Google Drive so a cloud task can read them. When you create the task, let Claude do a test run over historical data and review the output before it goes live.

