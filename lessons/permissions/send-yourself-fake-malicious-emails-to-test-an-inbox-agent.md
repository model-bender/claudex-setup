---
id: send-yourself-fake-malicious-emails-to-test-an-inbox-agent
created: 2026-11-06
status: active
supersedes: null
category: permissions
tool: claude-code
sources:
  - transcripts/mark-kashef/anyone-can-hack-your-app-with-uncensored-ai-now_jx8Hc5O8dX0_20261103.txt
---

# Test an inbox-reading agent by emailing yourself hidden instructions

## TL;DR

If an agent triages your email with broad read and write access, send yourself realistic emails that hide instructions (invisible text or HTML) and check the agent does not obey them.

## Why it matters

Mark Kashef lists email as one of five everyday attack surfaces for apps and agents. An attacker can send a realistic message (his example is a supplier invoice with a PDF) whose hidden text reads like an instruction from you. An agent with full read and write access to the inbox could carry it out without telling you. He says many people already give agents that access.

## How to apply

1. Write a few test emails to your own address that look like normal business mail (for example a supplier invoice) and hide an instruction in them, using invisible text or HTML, such as asking the agent to share private files.
2. Let your inbox-triage agent process them as it normally would.
3. Check it did not follow the hidden instruction and did not act without surfacing it to you.
4. If it did, reduce the agent's inbox permissions before relying on it.

Inference, not from the source: Step 4 (cut the agent's permissions if it fails) and the exact checklist are the lesson's extension. The transcript only says to run tests by sending yourself fake malicious emails and confirm triage agents are ready for it. The video also suggests asking an uncensored model to help write the phishing email, which is left out here.

## Related

[[harden-always-on-agents-least-privilege-and-capable-models]], [[start-an-email-routine-on-drafts-only-never-send]]
