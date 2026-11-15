---
id: let-strong-models-judge-what-to-remember-instead-of-fixed-rules
created: 2026-11-15
status: active
supersedes: null
category: memory
tool: claude-code
source_type: canonical
sources:
  - https://www.anthropic.com/research/components-of-agent-memory
---

# Don't hard-code "record only failures" memory rules for strong models

## TL;DR

Anthropic tested one rule per run. When told to "record only failures", Opus 5 and Opus 4.7 lost much of the performance boost memory gave them. Tell the model what memory is for and let it decide what to save.

## Why it matters

Steering helped older models most: Sonnet 4.6 nearly doubled its score when prompted to read its memory files and test its theories. Frontier models need only simple guidance, such as writing notes when asked or when something clearly matters.

## How to apply

In CLAUDE.md or a memory prompt, state the purpose of the memory directory and when to read it. Skip rigid write rules. Add stricter steering only if you run an older or smaller model.

> "For stronger models, giving them freedom to judge salience was more effective than setting fixed rules in advance, and those rules could end up weakening performance.", Anthropic, The components of agent memory

## Related

[[auto-dream-memory-consolidation]]
