---
id: upload-pr-images-and-video-via-the-github-uploads-api
created: 2026-08-16
status: active
supersedes: null
category: automation
tool:
  - claude-code
  - codex
source_type: canonical
sources:
  - https://github.com/openclaw/openclaw/blob/main/AGENTS.md
---

# Let an Agent Attach Images and Video to a PR by POSTing to `uploads.github.com`

## TL;DR

The drag-and-drop attachment CDN that GitHub's web UI uses is reachable from `curl` with a `gh auth token`, so a headless agent can upload a screen recording and embed the returned URL in a PR body - no browser, no computer use.

## Why it matters

Attaching visual proof is normally the one PR step an agent cannot do headlessly, which is exactly why UI-evidence rules get skipped in practice. This closes the gap, and it avoids the bad workaround of committing `.mp4` and `.png` proof assets into the product repo where they live forever.

Same CDN as drag-drop, so the attachment inherits repo visibility.

## How to apply

POST the file to the uploads endpoint with the repo's numeric `repository_id`, then embed the returned `.url`:

```
curl -s "https://uploads.github.com/user-attachments/assets?name=<f>&content_type=<mime>&repository_id=<id>" \
  -X POST -H "Authorization: Bearer $(gh auth token)" \
  -H "Accept: application/json" --data-binary @<f>
```

Embed the returned `.url` as markdown - for video, as a **bare line**, not `![]()` markup. Never push proof assets to a product-repo branch or commit them under `.github/pr-assets`.

## Related

[[make-video-proof-mandatory-for-ui-changing-prs]], [[make-every-autonomous-pr-carry-its-own-proof]]
