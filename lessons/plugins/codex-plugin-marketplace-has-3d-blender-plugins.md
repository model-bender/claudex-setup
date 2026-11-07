---
id: codex-plugin-marketplace-has-3d-blender-plugins
created: 2026-09-24
status: active
supersedes: null
category: plugins
tool: codex
sources:
  - transcripts/mark-kashef/gpt-6-astra-can-build-3d-worlds-to-learn-anything_27qpBfBhpDk_20260920.txt
---

# Codex's plugin marketplace ships ready-made Blender/3D-asset plugins

## TL;DR

Searching "Blender" in Codex's plugin marketplace turns up game-development-studio and build-3d-game-rooms. The source says the first alone is sufficient: Codex then detects, installs and sets up Blender and gets a skill for driving it, instead of you installing Blender by hand and prompting from scratch. The creator installed the second too because it helped in testing.

## Why it matters

Saves the manual setup the source otherwise walks through step by step, and confirms this is a real, currently-installable plugin rather than something the creator built themselves.

## How to apply

Verified directly: codex plugin list on codex-cli 0.156.1 lists game-development-studio@openai-curated-remote (v1.0.2) and build-3d-game-rooms@openai-curated-remote (v0.3.3) as available, not-installed plugins. Install with codex plugin add <name>@openai-curated-remote per codex plugin --help's documented add subcommand ('Install a plugin from a configured or remote marketplace').
