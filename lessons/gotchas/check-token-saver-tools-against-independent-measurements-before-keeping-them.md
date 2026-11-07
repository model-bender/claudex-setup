---
id: check-token-saver-tools-against-independent-measurements-before-keeping-them
created: 2026-10-19
status: active
supersedes: null
category: gotchas
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/i-tried-100-github-repos-for-claude-these-6-are-the-best_HhZdNYI4pJs_20261013.txt
  - transcripts/austin-marchese/8-free-ai-tools-every-claude-user-must-use_DMlBzXvG22g_20261014.txt
---

# Don't Install RTK, Caveman or Ponytail on Their Advertised Savings: Measure Where Your Tokens Go

## TL;DR

Nate Herk reports a JetBrains test where the advertised savings mostly did not hold, and suggests Codeburn to see real spend and waste.

## Why it matters

Austin Marchese presents RTK (input), Caveman and Ponytail (output) with README claims (RTK 60 to 90 percent on command output; Ponytail about 54 percent less code, about 20 percent cheaper). Nate Herk cites JetBrains tests on real coding tasks: Caveman cut about 8.5 percent of output tokens against 65 percent advertised, RTK saved nothing and raised cost at low effort, Ponytail saved about 10 percent per task (half its claim) and has an open Windows bug that can stall every message for seconds.

## How to apply

Before keeping a token saver, compare your own usage with and without it. Nate names the Codeburn repo, which shows spend and flags waste such as an MCP server that loads on every message but is never used. He also advises holding off on Claude Mem (sends usage data by default) and Context Mode (open bug that can burn usage). Checked: nothing installed or run here; all figures are as reported in the transcripts and I did not locate the JetBrains source. Note this qualifies the active RTK lesson, which presents RTK benefits without independent measurement.

## Related

[[rtk-proxy-filters-command-output-to-cut-input-tokens]], [[audit-cross-tool-token-spend-with-ccusage]], [[skill-md-under-200-lines-progressive-disclosure]]
