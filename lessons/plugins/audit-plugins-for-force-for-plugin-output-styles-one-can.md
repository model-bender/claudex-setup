---
id: audit-plugins-for-force-for-plugin-output-styles-one-can
created: 2026-08-22
status: active
supersedes: null
category: plugins
tool: claude-code
source_type: canonical
sources:
  - https://code.claude.com/docs/en/output-styles
---

# Audit Plugins for force-for-plugin Output Styles: One Can Override Your outputStyle Setting

## TL;DR

A plugin can ship an output style with force-for-plugin: true that applies the moment the plugin is enabled and overrides your own outputStyle, with load order deciding the winner when several do it.

## Why it matters

Installing a plugin can therefore change your system prompt (and, for a custom style without `keep-coding-instructions`, drop the software-engineering instructions) with no prompt and nothing visible in your settings file, and the resolution is "first one loaded", which is not stable or inspectable.

## How to apply

Before enabling a third-party plugin, grep its `output-styles/` directory for `force-for-plugin`; if your configured style stops applying, suspect an enabled plugin rather than your settings.

> "Plugin output styles only: apply this style automatically whenever the plugin is enabled, without requiring users to select it. Overrides the user's `outputStyle` setting. If multiple enabled plugins set this, Claude Code uses the first one loaded.", canonical: Claude Code docs — Output styles (frontmatter table)
