---
id: drive-a-gui-only-animation-editor-with-codex-computer-use
created: 2026-10-02
status: active
supersedes: null
category: workflows
tool: codex
sources:
  - transcripts/john-kim/how-to-use-codex-to-create-beautiful-app-animations_f-Ar8mwm3kQ_20261002.txt
---

# Use Codex computer use to build animations in a GUI editor that has no MCP or CLI

## TL;DR

For an editor like Rive, tell Codex to control it with computer use and describe the new animation in plain language.

## Why it matters

John Kim built their puzzle app characters in Rive. Codex controlled the Rive app with computer use, and they asked in natural language for a new animation (characters putting on a hat). They say that if the tool has no MCP or CLI, computer use is great, and that they had to teach Codex to organize the parts into a good hierarchy before animating. They say Codex has also been used with Blender to build and bake scenes and export part of them.

## How to apply

Open the editor, then in Codex ask: 'can you control Rive with computer use and add a new animation to our characters, one where they put on a hat'. First have it design and organize the parts into a hierarchy. Review the result by eye.

Verified: codex-cli 0.160.0 help lists a 'plugin' subcommand; the existing corpus says computer use installs as a Codex plugin. Rive-specific behaviour is source-stated and was not run here.

## Related

[[codex-computer-use-installs-as-a-plugin-and-refuses-os-privacy-settings]], [[turn-a-computer-use-workflow-into-a-cli-then-run-it-on-a-cheaper-model]], [[run-computer-use-agents-inside-a-vm-so-they-stop-stealing-your]]
