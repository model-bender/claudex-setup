---
id: unset-telemetry-opt-out-vars-because-0-still-counts-as-set
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

# Delete DISABLE_TELEMETRY and CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC to Turn Them Off: Setting Them to 0 Still Counts

## TL;DR

Claude Code treats `DISABLE_TELEMETRY` and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` as set whenever they hold any non-empty value, so `=0` or `=false` still switches telemetry or non-essential traffic off. To turn either back on, remove the key.

## Why it matters

These keys gate more than telemetry. With either one set, the AGENTS.md fallback was silently skipped before 2.1.281, and the non-essential-traffic key still blocks Projects, `/design-sync`, `--enable-live-preview` and plugin archive downloads on 2.1.281. Flipping the value to 0 looks like a fix and changes nothing, so the feature keeps failing for a reason the config file seems to rule out.

## How to apply

To opt back in, delete the key from the `env` block of every settings file that sets it and unset it in your shell profile, rather than setting it to 0. `DO_NOT_TRACK` is read through a parsing helper instead, so this applies to the two keys above. Checked 2026-09-24 against the installed 2.1.281 binary: the traffic-level check reads `if(process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC)` and `if(process.env.DISABLE_TELEMETRY)` as plain presence tests, and the `/design-sync` refusal text itself says "Unset it to use /design-sync".

## Related

[[claude-code-falls-back-to-agents-md-import-it-to-be-sure]], [[flip-all-outbound-traffic-off-with-claude-code-disable-nonessential-traffic]], [[disable-nonessential-traffic-also-turns-off-projects-and-claude-design]]
