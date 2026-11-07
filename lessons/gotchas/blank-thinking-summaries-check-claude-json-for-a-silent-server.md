---
id: blank-thinking-summaries-check-claude-json-for-a-silent-server
created: 2026-08-22
status: active
supersedes: null
category: gotchas
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/issues/75607
---

# Blank Thinking Summaries? Check ~/.claude.json for a Silent Server-Side Experiment Assignment

## TL;DR

Server-side experiment assignments cached in ~/.claude.json (clientDataCacheSlots / experimentKey) can silently blank thinking summaries; DISABLE_GROWTHBOOK=1 no longer opts out, only purging the assignment plus CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 does.

## Why it matters

Behaviour changes that arrive server-side appear in no changelog and no settings file, so time gets burned debugging your own config. Four independent reporters hit four different experiment keys across Opus 4.8, Opus 5 and Fable 5 (latest: "New assignment key, confirmed on claude-fable-5 ... `\"experimentKey\": \"claude_code_prairie_fixture_experiment\"`", 2026-08-21, 2.1.238). Note: no Anthropic-team acknowledgement in the thread, this is multi-reporter user measurement, not confirmed behaviour.

## How to apply

When a documented feature vanishes with no version change, inspect `clientDataCacheSlots` in `~/.claude.json` for an `experimentKey`/`atis` pair before debugging further; the only working opt-out today is purging it plus `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, which also costs Projects sync, `/feedback`, live preview and telemetry.

> "The mitigation documented below (purge the cached assignment + `DISABLE_GROWTHBOOK=1`) stopped working within a day. The CLI's startup bootstrap fetch re-enrolls the install about one second after launch, ignoring that variable. The only working user-side opt-out is now purge + `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, which also disables Projects sync, DesignSync, `/feedback`, live preview, and telemetry.", canonical: anthropics/claude-code issue #75607
