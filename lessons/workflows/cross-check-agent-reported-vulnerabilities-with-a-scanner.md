---
id: cross-check-agent-reported-vulnerabilities-with-a-scanner
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: [claude-code, codex]
sources:
  - transcripts/mark-kashef/you-need-to-learn-how-to-use-uncensored-ai_LYYs_jIFPZ4_20261026.txt
---

# Cross-check a model's vulnerability findings with a deterministic scanner

## TL;DR

When an agent reviews your own app for security holes, run a scanner such as Nuclei as well and use it to check the model's claims.

## Why it matters

The creator says the open models used in the video sometimes claim a hundred ways into an app when only about ten would actually work, and that Nuclei helps cut those false positives.

## How to apply

Give the agent Nuclei through the terminal and run it against the running app, then weigh each model finding against its results before you act on it. A finding Nuclei does not flag is not thereby false: Nuclei only tests what its templates cover (this lesson's inference from the Nuclei README).

Checked: Nuclei's GitHub repo (projectdiscovery/nuclei, read 2026-11-22) describes an MIT-licensed vulnerability scanner driven by YAML templates that checks applications, APIs, networks, DNS and cloud configurations. No Claude Code or Codex mechanism named. The transcript's observation is about open models in a third-party harness; applying it to Claude Code or Codex security reviews of your own app is this lesson's inference.

## Related

[[ultrareview-multi-agent-verification-pattern]]
