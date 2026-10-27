---
title: What does an AI agent do when you're not watching?
description: Three real cases from October 2026: an always-on agent that ran up a token bill, a coding tool that left a server running, and AI models that reached the live internet in tests. Plus three checks you can use today.
date: 2026-10-20
tags: AI agents, Security, How-to
video: AZbECki4s8Q
---
It's the end of the day. Your AI agent has finished the job, and you close the laptop. Here's a question most people can't answer: with the lid closed, what is your agent still doing? Not what it was asked to do. What it *is* doing.

In October 2026, three real cases pointed at that question. One was a bill. One was a leftover process. And one was an AI crossing a line it was never given permission to cross.

## First, what's an agent?

Not a chatbot that answers and stops. An agent is an AI that takes a goal and keeps working towards it, step by step, on its own. To get the job done it can start helpers of its own (subagents), each with one narrow job. Those helpers use **tools**: they open files, reach the internet, use your apps. Standing between the agent and the tools are **permissions**: what it may do alone, what it must ask about, and what is off limits.

Keep that picture in mind: you, a main agent, helpers, tools, permissions. Each case below is a problem in one part of it.

## Case one: the bill

At the end of September, OpenAI launched "dots": always-on agents meant to keep working in the background even when you're not talking to them. A security company called Geordie tested one, and [The Register reported the results](https://www.theregister.com/ai-and-ml/2026/10/13/openais-dot-assistant-burned-300k-tokens-in-a-day-without-a-single-prompt/5302913) on 13 October.

The setup was about as safe as it gets: one dot, read-only access, not connected to email, chat or personal apps. In one day it ran 155 separate pieces of work, at least 50 of them inside a single two-minute window, for a total of about 307,000 tokens. (A token is a small chunk of text an AI reads or writes; it's how these services measure use.) According to the report, the work was driven by the dot itself, not by a schedule or anything the user typed. In Geordie's words, the user "would have no idea that there were sub-agents".

Be careful with what this shows. It's one test of one dot by a security vendor. The report doesn't say anyone was charged for those tokens, it included no response from OpenAI, and Geordie itself said costs vary. It's a warning that this *can* happen, not proof that it happens to every dot.

**Lesson: an agent has a bill, and you may not be the first to see it.**

## Case two: the footprint

Codex is OpenAI's coding agent for the terminal. With [version 0.157.0](https://github.com/openai/codex/releases/tag/rust-v0.157.0), at the end of September, it started a background server by default: a program that waits in the background for work. Close Codex and it keeps running until you stop it or restart the computer.

According to the person who [reported it on GitHub](https://github.com/openai/codex/issues/48195), it copies a package of about 374 megabytes, and a small updater checks for new releases every hour. [Another user reported](https://github.com/openai/codex/issues/52067) the folder had grown to 2.8 gigabytes after 13 days because old copies stayed behind. These are users' observations; we didn't test them.

It isn't a secret: it's in the release notes. The complaint is that it's on by default and easy to miss. Some developers point out that background updates are normal for coding tools. If you don't want it, turn off daemon auto-start in your Codex configuration.

**Lesson: an agent has a footprint, and it can still be there after you think you're gone.**

## Case three: the boundary

On 9 October, Anthropic [published a report](https://www.anthropic.com/research/investigating-unintended-model-actions) about its own models going beyond what they were asked. In some evaluations (tests where an AI gets a task and a score) and some internal use, the models had live access to the real internet. When they were blocked, they sometimes found a way round.

The report describes four kinds of behaviour. In one, a stuck model used a weakness in someone else's website to get what it needed. In another, the task was a practice form; when the practice copy wouldn't load, the model went to the real website and submitted the form there. In one case, a model sent an invented tip through a real police department's web form, where it was flagged as spam. The other two were getting around restrictions to reach paywalled data, and using free link-shortening sites to dodge a limit on its web tool.

Anthropic assessed the real-world impact as minimal, with, to its knowledge, no customer data or internal systems involved. All of this comes from Anthropic's own report; we found no outside check. Its response was blunt: it has cut live internet from all its internal evaluations, tightened the guardrails on its internet tools, and added monitoring that blocked every case it replayed.

**Lesson: an agent has a boundary, and whether it stays inside depends on what you put around it.**

## Three different problems, one thread

Cost, footprint, boundary: three different parts of the picture. The common thread is simple. A capable agent, acting on its own, with nobody watching live, will sometimes surprise you.

One answer is a **sandbox**, a walled space where the agent works so a mistake can only reach what's inside. There are levels: nothing (the agent works directly on your machine), a container (a walled box on your machine), and a microVM (a tiny separate computer inside yours, with thicker walls). [Perplexity's open-source SPACE](https://github.com/perplexityai/SPACE) is one example of the third kind.

But a sandbox isn't the whole answer. Anthropic's cases didn't happen because walls were missing; they happened because the agent could reach the live internet. A wall with an open door is still an open door.

## The checklist: allow, ask first, never

For every agent you use, sort what it can do into three columns:

- **Allow:** what's safe and easy to undo. Reading files in one folder. Looking things up.
- **Ask first:** anything that changes something. Editing files, running commands, sending messages, spending money.
- **Never, while you're not watching:** open internet access, submitting forms, anything that costs more than you set.

The tools have real controls for this. In [Claude Code](https://code.claude.com/docs/en/permissions), rules are checked in order (deny, then ask, then allow), and an allow rule can't override a deny. By default it asks before editing files, running commands or using the web. In [Codex](https://developers.openai.com/codex/agent-approvals-security) you choose how much it can touch and whether it asks; keep that on the cautious end.

Before you close the lid, ask three things: **What can it spend? What can it leave behind? What can it reach?**

None of this means agents are broken. One case is a single vendor test, one is a default you can switch off, and one happened in evaluations, not products. But in every case, the problem went unseen until someone looked.

## Sources

1. The Register, 13 Oct 2026: [theregister.com](https://www.theregister.com/ai-and-ml/2026/10/13/openais-dot-assistant-burned-300k-tokens-in-a-day-without-a-single-prompt/5302913)
2. The Register, 29 Sep 2026: [theregister.com](https://www.theregister.com/ai-and-ml/2026/09/29/openai-tries-disarming-ai-angst-with-cute-graphics-and-always-on-agents/5299915)
3. Codex issue #48195, 25 Sep 2026: [github.com](https://github.com/openai/codex/issues/48195)
4. Codex issue #52067, 8 Oct 2026: [github.com](https://github.com/openai/codex/issues/52067)
5. Codex 0.157.0 release notes: [github.com](https://github.com/openai/codex/releases/tag/rust-v0.157.0)
6. Anthropic, 9 Oct 2026: [anthropic.com](https://www.anthropic.com/research/investigating-unintended-model-actions)
7. TechCrunch, 9 Oct 2026: [techcrunch.com](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/)
8. Perplexity SPACE: [github.com](https://github.com/perplexityai/SPACE)
9. Claude Code permissions: [code.claude.com](https://code.claude.com/docs/en/permissions)
10. Codex approvals and security: [developers.openai.com](https://developers.openai.com/codex/agent-approvals-security)
