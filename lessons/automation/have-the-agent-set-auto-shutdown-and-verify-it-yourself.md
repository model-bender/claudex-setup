---
id: have-the-agent-set-auto-shutdown-and-verify-it-yourself
created: 2026-11-22
status: active
supersedes: null
category: automation
tool: codex
sources:
  - transcripts/mark-kashef/you-need-to-learn-how-to-use-uncensored-ai_LYYs_jIFPZ4_20261026.txt
---

# When an agent provisions paid cloud hardware, have it set an idle shutdown and check it yourself the next day

## TL;DR

After an agent rents compute for you, ask it to stop any idle session automatically and shut down the hardware, then confirm yourself the next day that the machine is off.

## Why it matters

Hourly billing continues if you forget, and the creator's warning is that the agent may claim the shutdown is in place when it is not.

## How to apply

Prompt: 'Automatically stop any session where I am no longer talking to that model and shut down the corresponding hardware.' Next day, look at the provider's console yourself.

Checked: No Codex mechanism named. The quoted cost in the video (22 cents an hour) was not verified.

