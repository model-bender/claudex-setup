---
id: delete-role-only-custom-agents-keep-ones-with-knowledge-or-tool-limits
created: 2026-10-25
status: active
supersedes: null
category: agents
tool: claude-code
sources:
  - transcripts/simon-scrapes/5-claude-tips-everyone-recommends-but-shouldn-t_v9YVQoeSp-I_20261022.txt
---

# Delete Custom Agents That Are Only a Role Title; Keep the Ones That Carry Knowledge or a Tool Restriction

## TL;DR

An agent defined as 'you are a senior copywriter' adds nothing a current model lacks. Keep agents that encode a checklist of your process or a restricted tool set, and let one orchestrating agent decide when to split work.

## Why it matters

Simon contrasts fixed research/writer/reviewer teams with the newer shape where one lead conversation starts its own threads only when needed. Role-only agents duplicate what the model already does; knowledge and tool limits are the parts it cannot supply itself.

## How to apply

Audit your agent definitions. Delete the ones whose entire content is a persona or job title. Keep the ones that carry your own process checklist or limit the tools available. For genuinely wide jobs such as research across many sources, use the built-in research command or ask for a workflow rather than hand-building a team. Checked: n/a (a configuration judgement, no flag or setting claimed). Left out the transcript's claims about the Codex and Anthropic multi-agent statements and bug-finding numbers, and the 'set workflow size to small' config, which was not verified.

