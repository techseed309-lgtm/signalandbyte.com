---
title: "The inbox problem is a deciding problem: a free n8n email digest agent"
description: We built an email agent in n8n with Gmail and Google's Gemini that reads the whole inbox and sends one daily digest. How it works in nine steps, what it costs, and who can use or set it up for others.
date: 2026-10-28
tags: AI tools, Automation, Build
video: wvA0A8yPtqw
---
Most of the time an inbox takes isn't reading. It's deciding what each email is, and whether it needs you. So we built a small agent that does the deciding once a day and hands you one email. **The workflows, the prompt and a written guide are free on [our GitHub](https://github.com/techseed309-lgtm/email-digest-agent).**

## What you get
One digest in your inbox. At the top, the emails that need you, urgent ones first, each with a one-line summary and a suggested reply. Below that, personal mail, receipts, alerts, newsletters and promos, each counted and summed up. The agent never sends a reply: the only email it sends is the digest, to you.

## The tools (all free to try)
- **n8n**, a visual workflow tool, free to self-host for your own use under its Sustainable Use License.
- **Node.js** (or Docker) to run it.
- **A personal Gmail** with two-step verification, so you can create an app password.
- **A Gemini API key** from Google AI Studio.
- **Python** (optional), only to load our demo inbox.

## The build, in nine steps
1. Start n8n (`npx n8n`) and create your local login.
2. Create a Gmail app password. Never share it or show it on screen.
3. Create a Gemini API key in AI Studio.
4. Add three credentials in n8n: IMAP (imap.gmail.com, 993, SSL), SMTP (smtp.gmail.com, 465, SSL) and Google Gemini.
5. Import the three workflows from the repo and pick your credentials.
6. Set `MY_ADDRESS` in the Clean email and Prepare batches nodes; leave `DEMO_MODE` on true for the demo; set From and To in Send digest.
7. Run Setup queue once to create the `inbox_queue` table.
8. Publish Collect.
9. Run Sort & digest now, or publish it to run every morning at 08:00.

Try it on the demo inbox first: 300 made-up emails for a fictional design studio, all `.example` addresses, added to Gmail as unread without sending anything.

## Why two workflows
Picture an old mailroom. One clerk drops every letter into a tray; later, someone else works through the whole tray in one sitting and writes one report. **Collect** is the first clerk: no AI, every email becomes a row in the queue. **Sort & digest** is the second: it reads the whole queue once, in batches of 75, so our ~300-email demo inbox became just four requests to Gemini.

Each request is a form, not a chat: a category from a fixed list, a priority, a one-line summary and a suggested reply, every box required. The prompt ends with one rule: use only what the email says, and never invent facts, prices or dates. An email leaves the queue only after the digest has been sent, so nothing slips through.

## What happened on our demo inbox
Collect gathered nearly 300 unread emails in 4 minutes 39 seconds in the background; Sort & digest read them in 1 minute 17 seconds. That's about six minutes of machine time, against **our own estimate** of four hours by hand. The digest matched our answer key on 289 of 297 emails; the few it disagreed on were bank payment alerts it filed as receipts.

## What it costs (as of 27 October 2026)
- **Your own computer:** free; it runs only while the computer is on.
- **Gemini's free tier** covers testing and demo mail, but Google may use free-tier inputs to improve its products. For real business mail, use a paid key: for about 300 short emails a day on 3.5 Flash-Lite, roughly $0.38 to $1.83 a month (our estimate from Google's prices).
- **Always on:** a small VPS from about €6 or $6 a month, managed n8n hosting from about $11, or n8n Cloud from €20 a month billed yearly (its Starter plan counts executions).

Gmail already offers Gemini features such as thread summaries and suggested replies. If that's all you need, use it. Build this when you want your own categories, one daily digest, and every step where you can see it.

## Who it's for, and setting it up for others
Business owners, team leads and assistants with busy inboxes, and anyone buried in newsletters, receipts and alerts. If you're a developer or freelancer, setting it up for clients is a real service: n8n's licence FAQ allows charging for workflow creation, setup and maintenance; hosting n8n so clients build their own workflows needs a commercial licence. The clean setup is to install it on the client's own computer or server. An app where anyone connects their own Gmail needs Google's app verification and a yearly security assessment (CASA). We can't promise what anyone will earn, and this isn't legal advice.

## Sources
- [n8n Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)
- [n8n licence FAQ](https://docs.n8n.io/n8n-community-license/community-license/license-faq)
- [n8n pricing](https://n8n.io/pricing/)
- [Google: app passwords](https://support.google.com/accounts/answer/185833)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Gemini API additional terms](https://ai.google.dev/gemini-api/terms)
- [Google: Gmail is entering the Gemini era](https://blog.google/products-and-platforms/products/gmail/gmail-is-entering-the-gemini-era/)
- [Google: restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification)
- [Hetzner Cloud](https://www.hetzner.com/cloud/), [DigitalOcean Droplets](https://www.digitalocean.com/pricing/droplets), [Elestio n8n](https://elest.io/open-source/n8n)
