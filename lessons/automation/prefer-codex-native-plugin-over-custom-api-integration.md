---
id: prefer-codex-native-plugin-over-custom-api-integration
created: 2026-09-01
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/nate-herk-ai-automation/master-97-of-codex-in-1-hour-full-course_3TdD8Qv5Tk8_20260626.txt
---

# Check for a Native Codex Plugin Before Building a Custom API Integration

## TL;DR

Before wiring up a service's raw API (creating cloud projects, API keys, OAuth), search Codex's plugin list; a native plugin is just a sign-in, while a missing plugin means doing the manual API setup yourself.

## Why it matters

Native plugins (Slack, Gmail, GitHub, etc.) take a login click; building a from-scratch API integration means creating cloud console projects, enabling APIs, and generating keys.

## How to apply

In Codex's plugin browser, search for the service you need; if it's listed, connect via sign-in, if not (e.g. YouTube had none), ask Codex to plan a manual API-key integration instead.

## Related

[[prefer-anthropics-first-party-skill-plugins-over-marketplace-trawling]]
