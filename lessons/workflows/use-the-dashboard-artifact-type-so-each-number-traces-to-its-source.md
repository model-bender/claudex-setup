---
id: use-the-dashboard-artifact-type-so-each-number-traces-to-its-source
created: 2026-11-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/austin-marchese/7-new-claude-features-to-get-you-ahead-of-99-of-people-using-ai_BgbJFggbTVE_20261106.txt
---

# Build data dashboards from the Data artifact template (formerly Dashboards) so every number can be traced

## TL;DR

A dashboard made from the Data template (called the dashboard template in the video) lets you open what is behind each figure. Use it instead of a hand-made overview page when the numbers will be relied on.

## Why it matters

With a self-built overview page you had to trust the numbers. The template gives a first-party way to verify them, which the speaker ties to not knowing whether an AI-built system's figures are correct. In the video, the option beside a number shows the raw values and the exact formula behind it.

## How to apply

Go to the Artifacts tab, pick the Data template, and prompt, for example: 'Create a dashboard that would be the most useful to me based on this project.' Then open what is behind a number before relying on it: the video uses the option beside the number ('See where the numbers come from'); the current help article says to click the number or open the data sidebar, and that each chart shows its query and when its data was last refreshed.

Checked: support.claude.com 'Get started with Claude Data' and 'What are artifacts and how do I use them?' (fetched with curl 2026-11-22): 'Claude Data was previously called Claude Dashboards'; from the Artifacts tab you select 'Data'; the Data template is on Pro, Max, Ultra, Team and Enterprise plans, not Free. The video's button label was not confirmed. The Claude Code 2.1.330 binary also routes data dashboards to a 'Dashboard' artifact type, described as carrying 'figures with their source and, where there is one, the query or formula behind them'.

## Related

[[ask-for-live-spreadsheet-formulas-and-check-the-cells-not-the-look]]
