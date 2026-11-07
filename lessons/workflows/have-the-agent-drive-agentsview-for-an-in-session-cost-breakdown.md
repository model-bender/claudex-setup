---
id: have-the-agent-drive-agentsview-for-an-in-session-cost-breakdown
created: 2026-08-07
status: active
supersedes: null
category: workflows
tool: claude-code
source_type: post
sources:
  - https://simonwillison.net/2026/jul/5/sqlite-utils-fable/
---

# Get a Cost Breakdown by Telling the Agent to Discover AgentsView Itself

## TL;DR

When token spend is not otherwise visible, such as in a Claude Code for web session, prompt the agent to run `uvx agentsview --help` and work out the right subcommand to cost the current session.

## Why it matters

Willison ran a long sqlite-utils 4.0 release session with no visibility into spend, and this produced an itemized per-model breakdown without leaving the session: $141.02 for the main session on claude-fable-5, plus $2.40, $2.39, $1.72, $1.40 and $0.32 across four subagents. The trick worth copying is not the tool but the framing: pointing the agent at `--help` and letting it find `session list --include-children` means you do not need to know the CLI surface first.

## How to apply

Prompt directly with: `Run "uvx agentsview --help" and then use that tool to calculate the cost of this session`. Generalize the pattern to any unfamiliar CLI, handing over the help output rather than looking up the invocation yourself.

> "Run \"uvx agentsview --help\"​ and then use that tool to calculate the cost of this session", Simon Willison

## Related

[[subagent-spawn-cap-of-200-per-session-removed]]
