---
id: ollama-launch-claude-runs-claude-code-on-a-local-model
created: 2026-11-22
status: active
supersedes: null
category: configuration
tool: claude-code
sources:
  - transcripts/austin-marchese/you-re-overpaying-for-claude-code-use-this-open-source-strategy-instead_WyFrrdof5oU_20260910.txt
---

# Run Claude Code against a local model with `ollama launch claude --model <model>`

## TL;DR

Ollama can start Claude Code wired to a model running on your own machine with one command, so the session is free, private and works offline.

## Why it matters

The speaker uses it for work with no internet (a flight with broken Wi-Fi) and for data that must not leave the machine. No manual gateway configuration is needed: the Ollama docs list setting `ANTHROPIC_BASE_URL` and the auth variables by hand as the alternative to `ollama launch`.

## How to apply

Install Ollama and pull a model, then run `ollama launch claude --model <model>`. The speaker's own example model name is garbled by the speech to text, so use the tag Ollama's library shows. If `launch` is missing, update Ollama; if the shell says Ollama is not installed, open a new terminal window.

Checked: docs.ollama.com/integrations/claude-code.md fetched 2026-11-22: documents `ollama launch claude` and a `--model` example, and advises a 64k or larger context window for local models. Local Ollama client 0.40.11: `ollama launch --help` lists `claude` (Claude Code) and the example `ollama launch claude --model <model>`. No Ollama server was running, so the command itself was not executed.

## Related

[[route-claude-code-to-cheaper-or-local-models]]
