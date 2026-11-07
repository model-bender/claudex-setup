---
id: disable-nonessential-traffic-also-turns-off-projects-and-claude-design
created: 2026-09-24
status: active
supersedes: null
category: settings
tool: claude-code
source_type: canonical
sources:
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  - https://simonwillison.net/2026/Sep/18/thariq-shihipar/
  - https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
  - https://github.com/anthropics/claude-code/issues/95690
---

# CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC Also Switches Off Projects, Claude Design and claude.ai Plugin Downloads

## TL;DR

`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` puts Claude Code in an essential-traffic mode that refuses Projects, Claude Design and `/design-sync`, `--enable-live-preview`, plugin archive downloads from claude.ai, and `/feedback`. If telemetry is all you want off, set `DISABLE_TELEMETRY` instead, which does not trigger that mode.

## Why it matters

The umbrella key reads like a pure privacy switch, and the advice to prefer it over listing every opt-out key says nothing about what it costs. Each feature fails later with its own refusal message, often long after the key went into a shared settings file, so the cause is easy to miss. The mode follows the key's presence, not its value, so setting it to 0 does not undo it.

## How to apply

Before adding the key to a settings `env` block, check whether you use Projects, Claude Design, `/design-sync`, live preview, claude.ai plugin installs, or posting review findings to a pull request through cloud sessions. If you do, set only the individual keys you need (`DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`) and leave this one out. To switch the mode off, delete the key. Checked 2026-09-24 against the installed 2.1.281 binary: each refusal is gated on one essential-traffic check that only `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` turns on (`DISABLE_TELEMETRY` and `DO_NOT_TRACK` select a separate "no-telemetry" mode), and the refusal texts include "Projects is unavailable while nonessential network traffic is restricted (CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC is set)." and "Claude Design is disabled because nonessential network traffic is restricted." The same check also turns off messages to a session on another machine and the Artifact tool, whose availability check returns essential-traffic-only before it reads the `CLAUDE_CODE_ARTIFACT` switches (added 2026-09-24 by the third consolidation pass).

## Related

[[unset-telemetry-opt-out-vars-because-0-still-counts-as-set]], [[flip-all-outbound-traffic-off-with-claude-code-disable-nonessential-traffic]], [[quiet-mode-env-vars-for-client-and-confidential-work]]
