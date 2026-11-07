---
id: ab-test-a-workflow-plugin-against-no-plugin-with-a-clear-brief
created: 2026-10-25
status: active
supersedes: null
category: plugins
tool: claude-code
sources:
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Re-Test Each Workflow Plugin Against Plain Claude Code With a Clear Brief, and Uninstall the Ones That Do Not Win

## TL;DR

Plugins built for models that skipped steps may add tokens without improving Opus 5.5 output. Run your usual prompts with a well-formed brief and no plugin, compare against the plugin output, and drop the plugin if there is no difference.

## Why it matters

Simon reports a third-party test of nine popular skill packs, 450 runs on Opus 5.5 against a same-length placebo file, in which only two packs beat the placebo and the best-known one was not among them. He does not say to uninstall everything, only to check on your own work, since removing a plugin can cut complexity and token spend.

## How to apply

1) Take some of your real recurring prompts and write them with a clear brief. 2) Run each without the plugin, then with it. 3) Compare the outputs. 4) If the plain run holds up, consider uninstalling the plugin, which Simon frames as a possible outcome rather than a rule. Checked: n/a (method). The 450-run placebo study is only described secondhand in the transcript and was not located or verified, so the lesson treats it as a reported result and rests on the do-it-yourself comparison.

## Related

[[superpowers-plugin-enforces-phased-workflow]]
