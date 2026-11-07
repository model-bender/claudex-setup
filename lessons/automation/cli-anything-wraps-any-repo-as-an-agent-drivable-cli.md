---
id: cli-anything-wraps-any-repo-as-an-agent-drivable-cli
created: 2026-07-10
status: active
supersedes: null
category: automation
sources:
  - transcripts/sean-kochel/5-claude-code-tools-that-make-vibe-coders-cry-tears-of-joy_QK0B1mbJ-VU_20260703.txt
---

# Turn Any Open-Source Tool Into a Claude-Drivable CLI With CLI Anything

## TL;DR

Point the /cli-anything command at a cloned open-source repo and it inspects the tool's front and back end and generates a CLI wrapper, making non-agent-native software (Excalidraw, a captioner, a Mermaid editor) something Claude Code can operate directly.

## Why it matters

Most software you use day-to-day isn't agent-native, so Claude can't drive it; rather than building a bespoke integration or MCP for each, an auto-generated CLI gives the agent a deterministic, self-documenting handle on any tool whose source you can access, an extension of the 'give agents CLIs, not MCPs' principle to tools you didn't write.

## How to apply

Clone the target repo and get it running locally, then run /cli-anything and tell it which repo to build for; it uses its own commands/skills to read the codebase and emit a working CLI, after which you invoke the tool in natural language ('use the CLI-anything Excalidraw CLI to draw a diagram of X') and Claude runs it, reach for this when you want the agent to operate a GUI/desktop tool that has no API but does have source.
