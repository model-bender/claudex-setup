---
id: type-a-skill-name-directly-to-run-it-as-a-slash-command
created: 2026-09-01
status: active
supersedes: null
category: skills
tool: claude-code
sources:
  - transcripts/ray-amjad/claude-code-s-biggest-update-in-months_20260307.txt
  - transcripts/john-kim/how-i-use-claude-code-meta-staff-engineer-tips_20260307.txt
  - transcripts/ray-amjad/better-than-mcps-claude-code-s-new-skills-feature_20260307.txt
---

# Type a Skill's Name Directly to Run It, No Separate Command Needed

## TL;DR

You can trigger any skill as a slash command just by typing its name (e.g. github-release-notes), without a separate wrapper command.

After Claude saves a workflow as a skill, a same-named slash command (e.g., `/fetch-hackernews`) becomes available too, without building it separately.

Even though skills are model-invoked by default, you can force one to run by naming it directly in chat, e.g., 'trigger the code review skill.'

## Why it matters

Not knowing this leads people to write a redundant slash command that just calls the skill, when the skill name itself already works as the invocation.

John Kim shows that skills and commands recently became interchangeable: the skill lives as a SKILL.md file, but Claude Code also exposes a slash command that reruns the same system prompt.

Ray Amjad demonstrates this as a quick way to test or force a skill when its description alone might not be well-tuned enough to auto-trigger on a natural request.

## How to apply

Type the skill's name (as it appears in your skills list) directly into the prompt box and press enter to run it, the same way you would a slash command.

After asking Claude to 'save what we just did into a new skill called X,' check the slash-command menu; the equivalent `/X` command should already be triggerable, no extra command file needed.

Ask 'what skills do I have available?' to see the list, then say 'trigger the <name> skill' to force invocation regardless of whether the description would have matched your request.

