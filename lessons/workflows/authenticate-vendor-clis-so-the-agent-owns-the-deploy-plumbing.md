---
id: authenticate-vendor-clis-so-the-agent-owns-the-deploy-plumbing
created: 2026-08-22
status: active
supersedes: null
category: workflows
tool: claude-code
sources:
  - transcripts/nate-herk-ai-automation/build-sell-ai-saas-products-2-hour-course_IVx8OSMbTss_20260820.txt
---

# Log Into the Vendor CLI Yourself, Then Let the Agent Do the Dashboard Work

## TL;DR

Run `vercel login` (or the equivalent) in the agent's terminal and it will create the project, load every environment variable, mark secrets as sensitive, run the two-step redeploy, and smoke-test the result - instead of you pasting keys into a web dashboard one at a time.

## Why it matters

Deploy configuration is the part of shipping that agents are locked out of by authentication, not by capability, and it's exactly the part that is tedious and error-prone by hand: a dozen env vars, each needing the right scope and sensitivity flag. Once Claude Code had a logged-in Vercel CLI it wrote all of them itself, correctly marked the Supabase service-role secret as sensitive, and ran the PDF smoke test after redeploying. It also surfaced the ordering constraint you would otherwise discover as a bug: two values (the public site URL and the Stripe webhook secret) cannot be set before the first deploy because they depend on the URL the platform assigns, so the deploy is inherently two-step. The same pattern covers GitHub - authenticate once and the agent creates the private repo and pushes.

## How to apply

Run the vendor's login command in the terminal the agent is using and approve the OAuth prompt yourself; then ask the agent what it needs and let it drive. A useful prompt shape: 'I've run vercel login - link the repo as a project under this root, load all the environment variables, run the first deploy, then tell me which values you couldn't set yet and why.' Keep secrets in `.env.local` (gitignored, so they never reach the repo) and have the agent copy them into the platform's environment-variable store. Rotate any key the agent used during development before it becomes the production key. Expect occasional deploy failures on the first connection - screenshot the error page and paste it in; that was enough to get a 404-on-deploy diagnosed and fixed without you reading a log.

## Related

[[rotate-dev-exposed-keys-before-production]]
