---
id: gate-model-switches-with-a-premodelswitch-hook
created: 2026-08-29
status: active
supersedes: null
category: hooks
source_type: canonical
tool: claude-code
sources:
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
---

# Gate Mid-Session Model Switches With the New PreModelSwitch Hook

## TL;DR

2.1.251 makes model switches a hookable event (`PreModelSwitch` / `PostModelSwitch`), so a model-routing rule that previously lived in CLAUDE.md as a suggestion can now be enforced: block, confirm, or annotate the switch.

## Why it matters

Routing rules in CLAUDE.md are advisory and get ignored some fraction of the time, and a mid-session switch also invalidates the prompt cache, which makes accidental switches doubly expensive. This is exactly the class of rule worth promoting from prose to mechanism.

## How to apply

Add a `PreModelSwitch` hook entry in `settings.json` that blocks or asks for confirmation on switches you want gated (for example, refusing an escalation to a premium model outside plan or review work). The same release also hands `SessionStart` resume hooks the session staleness and estimated re-cache cost, so a resume hook can decide whether reinjecting context is worth it.

> "Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate a model switch); `SessionStart` resume hooks now receive session staleness and the estimated re-cache cost", Claude Code CHANGELOG 2.1.251

## Related

[[prompt-cache-what-breaks-it]], [[sessionstart-resume-hooks-receive-staleness-and-recache-cost]]
